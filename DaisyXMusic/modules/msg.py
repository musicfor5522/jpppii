# @Arwa_Foda (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**🛕مرحبا [{}](tg://user?id={}).**\n\nيسمح لك تشغيل الموسيقى في مجموعات من خلال الدردشات الصوتية الجديدة في Telegram! 🎸\n\nلمعرفة كيفية استخدام هذا الروبوت ، يرجى النقر علي » /help"
    HELP_MSG = [
        ".",
        f"""
**اهلا بك عزيزي مره اخري في {PROJECT_NAME}

🎸 {PROJECT_NAME} يمكن لـ تشغيل الموسيقى في الدردشة الصوتية لمجموعتك بالإضافة إلى قنوات الدردشات الصوتية‌‌

🎸 الحساب المساعد >> @{ASSISTANT_NAME}\n\nانقر علي الازرار بالاسفل للحصول على المزيد من المعلومات**
""",
        f"""
**Setting up**

1) قم برفع البوت مشرف (المجموعة وفي القناة إذا كنت تستخدم cplay)
2) ابدأ محادثة صوتية
3) ارسل /play [اسم الاغنيه] لأول مرة من قبل المشرف
*) إذا انضم البوت ، استمتع بالموسيقى ، إذا لم يكن كذلك ، أضف @{ASSISTANT_NAME} إلى مجموعتك وأعد المحاولة

**لتشغيل الموسيقى في قناتك**
1) قم برفعي مشرف في القناه 
2) ارسل /userbotjoinchannel في المجموعه المرتبطه
3) أرسل الآن الأوامر في مجموعة مرتبطة‌‌
""",
        f"""
**اوامر الاستخدام**

**💡 هنا الأوامر الأساسية**

- /play: تشغيل الأغنية المطلوبة
- /play [yt url] : المحدد في تشغيل الاغنيه
- /play [الرد على الاغنيه]: تشغيل الصوت الذي تم الرد عليه‌‌
- /splay: تشغيل الأغنية عبر jio saavn
- /ytplay: تشغيل الأغنية مباشرة عبر Youtube Music

** قائمه التشغيل **

- /player: لفتح قائمة الإعدادات الخاصة بالمشغل
- /skip: لتخطي الاغنيه الحاليه
- /pause: لـ التوقيف المؤقت
- /resume: لاعاده تشغيل المسار المتوقف مؤقتًا
- /end: لـ انهاء التشغيل
- /mute: لـ كتم تشغيل الاغنيه
- /unmute: ـ الغاء كتم تشغيل الاغنيه
- /current: لـ عرض مسار التشغيل الحالي
- /playlist: لـ عرض قائمة التشغيل

""",
        f"""
** تشغيل الاغاني في القنوات **

🎸 اوامر ادمن المجموعة:‌‌

- /cplay [اسم الاغنيه] - تشغيل الأغنية التي طلبتها‌‌
- /csplay [اسم الاغنيه] - تشغيل الأغنية التي طلبتها عبر jio saavn
- /cplaylist - عرض قائمة التشغيل الآن‌‌
- /cccurrent - عرض المشغل الان
- /cplayer - فتح لوحة إعدادات مشغل الموسيقى‌‌
- /cpause - وقف تشغيل الاغنيه
- /cresume - استئناف تشغيل الأغنية‌‌
- /cskip - تشغيل الاغنيه التاليه
- /cend - إيقاف تشغيل الموسيقى
- /mute - كتم مشغل الموسيقى
- /unmute - لغاء كتم مشغل الموسيقى
- /userbotjoinchannel - دعوه الحساب المساعد الي القناه

🎸 إذا كنت لا تحب اللعب في مجموعة مرتبطة:

1) احصل على معرف قناتك.
2) إنشاء مجموعة مع tittle: قناة الموسيقى: your_channel_id
3) أضف البوت كمسؤول قناة مع صلاحيات كاملة
4) أضف @NINJA_MUSIC0_BOT إلى القناة كمسؤول.
5) ببساطة أرسل الأوامر في مجموعتك. (تذكر استخدام / ytplay بدلاً من ذلك / play)‌‌
""",
        f"""
**ملكش دعوه انت بده 👍**

- /musicplayer [تشغيل / إيقاف]: تمكين / تعطيل مشغل الموسيقى
- /admincache: تحديثات معلومات المسؤول لمجموعتك. حاول إذا لم يتعرف البوت على المسؤول
- /userbotjoin: قم بدعوه @{ASSISTANT_NAME} الي الدردشة الخاص بك
""",
        f"""
**اوامر تحميل الاغاني ❤️‍🔥**

- /video [اسم الفديو]: تنزيل الفيديو من youtube
- /song [اسم الاغنيه]: تنزيل أغنية صوتية من youtube
- /saavn [اسم الاغنيه]: تنزيل أغنية من saavn
- /deezer [اسم الاغنيه]: تنزيل الأغنية من deezer

**اوامر البحث 💡**

- /search [اسم الاغنيه]: ابحث في youtube عن الأغاني
- /lyrics [اسم الاغنيه]: احصل على كلمات الأغنية‌‌
""",
        f"""
**اوامر بــ آلمـطـور 💻**

 - /userbotleaveall - ازاله الحساب المساعد من كل الدردشات
 - /broadcast <الرد على الرساله> - إرسال رسالة في جميع الدردشات
 - /pmpermit [on/off] - تمكين / تعطيل رسالة pmpermit
*يمكن فقط للمطور تنفيذ اي امر في اي مجموعة‌‌

""",
    ]
