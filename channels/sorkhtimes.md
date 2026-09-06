<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/RG5-AgYyTVcaE5pp3Ke9zprjkK9aKEfZOnjCW0_6V5a6JYCSn5S8psgBBzjiqoz-5EFz-pMxYxyS6V77oEYmrZtArNi2IzECRWP_n1HJuBRqDCJhpOnyJu6divH_E1o6TgcHC3Xi1FG4V2uXzPDvmeSHVyV763B9P33AltEmJoZN8zn_ga7u2R-VRpAO8lrYICXAjZ5AwnA3DWEq6y-IzHcYhFyc6PhNxHOE4an21RGnWXQqqPTTtcWxVukc3mkXZsphNx9-F_46acTCU6oN4wEEfkPaNXKHSpUT5zDhykgmIQJtG9I8BfGaY0aBEDIeKWokcqzICN2hxoJ2T4rwlQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-139634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbFQVuq1y4aViOzh8KG1URthi8-ec5eB1Ntugsbv9C33fEZviNDxIyt0prm4M_hy9pL20SZAiP9fePqqy22s50hyxypb88yhGWheHOasEHgN3Mzr7CthPoJgEd_abP-ugbsxAGjUzkiLYn4JjfGT2rA6U3tF_c2VHyIOhsHZ8ebCkJg5rwbGx3Z8xgmBa2izsTlRP0PMyydFtc3vSelwwQ3nlWLDHDeRHd5MXIuBT35jzCibB2N2LCFJfYpTFm__PDjdXfV4gRFRcS8V1YKPivKQ2dgwIfFsQHxxtYtuPP40aAbCvSWwh42gvHhfNz_BbkQ9JE9MN8_NE09je4L_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مرتضی کرمانی مقدم:
✔️
امیدوار بودم که کادرفنی از ابتدا از اورونوف استفاده کند ولی این بازیکن در ۱۰ دقیقه آخر وارد زمین شد. من نمی‌دانم چرا باید از دقیقه ۷۵ به بعد تعویض کرد؛ اگر قرار است بازیکن روند بازی را تغییر دهد باید حداقل بیشتر از ۲۰ دقیقه بازی کند تا بتواند کیفیت خود را به نمایش بگذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SorkhTimes/139634" target="_blank">📅 15:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ9sDkv01L_7dNASw6Z3qa8EQXr_KLDz-pp4kVPgUvfBC9PMf3b4sq750K4uuFl6SFJ80cBTpUVWHN_BN9Ic5givWLEpgxfptaNhQZsNLrVmkIT47CNm8BTJUnRzFe42QUTpLsC7wUW8NYpV9aLWQ-_rqxapiJYz2w9jXpP5trhb0XaUAmi937TUx0OhH6YeempB666P_QjnyRoabJFZmt0k6IL_U7C0aFY3PHNkUFrGBMgjkv-mnbdxV-WRT9ZHV18b47qUGFnoKHb5CXd8x3o6GIZs_Syk2Ha3pR9AbbJddxDZJ35YaR1FwBkZ8tcrgT22Ku7fPuA0pcPAKEDYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
با اعلام کمیته انضباطی، خداداد عزیزی، سرپرست تیم فوتبال تراکتور به دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف مدت 48 ساعت دفاعیات خود را به این کمیته ارسال کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/139633" target="_blank">📅 15:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
فووووووووری
🚨
امید عالیشاه قصد داره فردا با حضور در دادسرا از خداداد عزیزی شکایت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/139632" target="_blank">📅 15:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-FVE_lvhD-Xw6X6ucU1EEFNr86Rz3vKe2dTU0JBnkDw8ajZJ8TceVCgPxadUz7z-kkIWLvBRn4wO2yAt_YLDK6urbsIcEhIuCjLU3df7WG63t8Uf1fJXwzndiye8ISy0sgdGMbrhejgpm0Uda6Ui2I5Nyy2FFn8hphdqb2yoBqjVrlxvxFVO3zq-ui3gGAT39Equq7NtUtX9aDHyzTHueiBLju1zMdlP-RQJRfyqdYyrYybk_Ca2gqjqSU3XsCDkbmjit0I7v58ofZX07TqetBdIoR3w58Uv_Kg0rE1mgLBYrhQqyYefqbjwtggzCnPoRNqeeHbmrUC59GvVOd3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاتالان‌ها در مستایا آماده شکار خفاش‌ها، نبردی برای صدرنشینی!
🟡
Valencia -
🔵
Barcelona
⏰
Today 17:45
🏟
Estadio de Mestalla
بارسلونا با تکیه بر مالکیت توپ و قدرت هجومی، به‌دنبال کنترل بازی از همان دقایق ابتدایی است.
والنسیا می‌تواند با دفاع فشرده و ضدحملات، برای خط دفاعی بارسا دردسرساز شود.
با توجه به برتری کیفی بارسا، کفه ترازو به سود آبی‌واناری‌ها سنگین‌تر است.
📌
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و پیش‌بینی خودتو ثبت کن:
👇
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/139631" target="_blank">📅 14:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/139630" target="_blank">📅 13:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
✔️
تارتار قصد داره در بازی فردا مقابل ذوب آهن از شهرآبادی در ترکیب اصلی استفاده کنه
📝
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/139629" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/139628" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139627" target="_blank">📅 10:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHqLAotvYksGBLh6u5Rdl5Jedf54HsIhNI8Ry3UwbEgXf3c3fXl9y49pxn1mA0NXwspkxFwbIkEgIrsDJ5gSpaoT91SyowzoSblikieL5luncqY15e_0CHhKhJKZzcjgFcqQFEpHpmNuA5hmxdMH84z-mQavEXpWCoH3gncdXSawVCI5nj7EGswUqd1IWkZXHkqCPHgpVOORQ3xbl75tuxPq81zUlGnmUe-6vG4binJbDNQb3z1MkBeskybXxD4aqg0uqohEvJbHGUEz07BmSXlLHel-W-o0PyHZeokqhP5EZ31J-m1cq5gfeJTYgelwavYEkJVShmUBVZWYZeWy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
ازاون اتفاقا که فقط تو ایران میفته
✔️
فرشته کریمی کاپیتان و اسطوره تاریخ
فوتسال
ایران با عقد قراردادی به تیم
فوتبال
پرسپولیس پیوست
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139626" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139625" target="_blank">📅 10:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=hfm-RdrWquVziNaB80Ulze62XmdIUwXrq_Y50VLv_IuqvqnpUgt5wSNt6F2iJm5fPpGG-p3fWCvNnvIWnXfEjbXguVTcEWBwGIuip7msJW_0gwRv0mAJRDUJU4-i1gm-2jok41Nd-n2rpqVcnfGOAJ9ueW1gI4l88rxKbm7ZtybcwIFQRasSnLDzDw_wCMyFyg1gCgR8uh8z6RcjiReKeOWo-bkoIZYh2l_g6Qfnvz6SEovwcW9EAticBJ8wDwsTaXWQ4m0l5U-GsntbK6GI11xdwut-sNKsleSMPNuDxTuDaiWyPfY2qVRWltD1IdALI43Mg58QCtyqrALwxpb6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=hfm-RdrWquVziNaB80Ulze62XmdIUwXrq_Y50VLv_IuqvqnpUgt5wSNt6F2iJm5fPpGG-p3fWCvNnvIWnXfEjbXguVTcEWBwGIuip7msJW_0gwRv0mAJRDUJU4-i1gm-2jok41Nd-n2rpqVcnfGOAJ9ueW1gI4l88rxKbm7ZtybcwIFQRasSnLDzDw_wCMyFyg1gCgR8uh8z6RcjiReKeOWo-bkoIZYh2l_g6Qfnvz6SEovwcW9EAticBJ8wDwsTaXWQ4m0l5U-GsntbK6GI11xdwut-sNKsleSMPNuDxTuDaiWyPfY2qVRWltD1IdALI43Mg58QCtyqrALwxpb6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه باشگاه گل‌گهر به بیرانوند: وقت‌کشی، کسب‌وکار من است! چه برای به‌تعویق‌انداختن سربازی، چه برای کُشتن زمان مسابقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/139624" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/139623" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
⭕️
🚨
🚨
🚨
🚨
خداداد بعد از اشتباهات داوری به نفع تراکتور در زمین جنجال می کند بعد از بازی هم مصاحبه  جنجالی را چاشنی کارش می کند تا حواس ها از داوری پرت شود. یک سناریوی تکراری! اما آقای عزیزی! عالیشاه رکورددار نباختن در دربی در حد شما نیست؟تفاوت شما با تماشاگران…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/139622" target="_blank">📅 09:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139621" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/139620" target="_blank">📅 09:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/139619" target="_blank">📅 09:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139618" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=WlOXHnGyXc6KbrmyjTuCWGUm2mQIx6oPFduhmMbtfgBDtLvj2jhcB2BpYnkmW32z0Wmat9paJAeSWLvDuOItgpVN8Dmj_qcgGyh9H6uWEpF7yqv_XgVpy_3yQL-ldldb48JXIq12hRethb3d6dhKl6XOn5iig68FNfCMwa8kMF54vZ6jPu0ruoSsEokxpC4oB5BrECRPJ9NWK9Oe0JyOhYKlh8wkbX9ZsbZ9Sx5rfDXG3HVijyxTfhFqzUu1D6kVgM7PDy2fPvyLjL0rmwhiJunbXk78FvFZSqk6I_nFg1peVbcDDFL6yikx3xGErVuWUkLaSVl8nVfmud6qtb82Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=WlOXHnGyXc6KbrmyjTuCWGUm2mQIx6oPFduhmMbtfgBDtLvj2jhcB2BpYnkmW32z0Wmat9paJAeSWLvDuOItgpVN8Dmj_qcgGyh9H6uWEpF7yqv_XgVpy_3yQL-ldldb48JXIq12hRethb3d6dhKl6XOn5iig68FNfCMwa8kMF54vZ6jPu0ruoSsEokxpC4oB5BrECRPJ9NWK9Oe0JyOhYKlh8wkbX9ZsbZ9Sx5rfDXG3HVijyxTfhFqzUu1D6kVgM7PDy2fPvyLjL0rmwhiJunbXk78FvFZSqk6I_nFg1peVbcDDFL6yikx3xGErVuWUkLaSVl8nVfmud6qtb82Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139617" target="_blank">📅 09:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEEHZ84FGmCr3O4VIZWhhDWHidhCgsuuzgZKEFiMkNFvusBwBmaxxgHgXtByEYAEcjWdnB-Z-tb4UquqyUuYrFI16RQclVFevNDoxUWokFZq3gU3NbBMc6VQP9e07DsNxnIVnjWYjsEKT3cpR5cjR9bLc1RMK1dyC7o8w-3xzDm2E9-jEum4O-XV0s2CpfsK-l6htfTbkFMAz268nVu-xrsMQ7qED8tD5d_wnKwzr8669KOMlvoEOQQrPEgFMTGKlaDkZHQzHl2jwnrLQBRV0WJD9ktXqTqv2nFSYqzkjOd2nsBmdKqd8ce2_NwcJ_taN9h_wHbCg4VTnzo7OUVAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139616" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC1JcqbndYLCQ2jkg5aE2Au1kX7SHswyQXn8fHaApePKpVi5UUsSpk1tHkoK6TMXB25NlG6yN6fArAHfk7gMi5nF4ph1Aol2aMQghfElLyf6auqKu5rweHOp8LMLFn6H4QZ3OPS7YvL9U-Ic4qYFe_vxvw_iI4Jjz6xGXv5lQ4Xr1FVTisxLpszzwZIqd4FXpIq2nudvNenJjxz0ap5AthEHJgRYlYGiMbaHdsJwo6hqUSNbysMKhhGnLU4F6t39mBJwkzQd49mxGggOiwrs_dqaTgFlwvEQKEmIoEs7HsFuXaj-zPjgygpy81teHKz2wQRBssxidfrYTvEDKAhj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
زورف و تابیلو؛ زورف با تجربه و ثبات بیشتر شانس بالاتری دارد.
تین و منشیک هم جدالی نزدیک و جذاب خواهند داشت که سرویس‌ها می‌توانند تعیین‌کننده باشند.
🎾
Zverev -
🎾
Alejandro Tabilo
🎾
Jakub Mensik -
🎾
Learner Tien
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139615" target="_blank">📅 00:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139614" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139613" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139612" target="_blank">📅 23:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=SRMxoHNJjCrBAAwSiCiO_Af3KUe6fBTFwVNbyqY6tYy1njoncdmAgFgdIkltIhdpyk9yDSVOCMOHM5NSfLS4FyxEJymg3WN6bAr_bllKzCTuaRQuT30k7apAW-e6gmismrDHhnjCVqR4ip_reHrssb0uiguiN7_Pfcl99k2-26TrSVyWvdVAmoUSkTBrL3GjIlZCGHJX_P4AHJnsAGq0j-IaDbrrJPM9yNfQ_IGStPCV4E-ThdXQ1NRGSJ4VA_20QYSXOpXDku8_4PQR8Qc3idYFDE3UuRGhl0pCjQC_ydySxW0b920WGtU1MJVX98OTW_OoW8GLuoCNsgWTlrBdgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=SRMxoHNJjCrBAAwSiCiO_Af3KUe6fBTFwVNbyqY6tYy1njoncdmAgFgdIkltIhdpyk9yDSVOCMOHM5NSfLS4FyxEJymg3WN6bAr_bllKzCTuaRQuT30k7apAW-e6gmismrDHhnjCVqR4ip_reHrssb0uiguiN7_Pfcl99k2-26TrSVyWvdVAmoUSkTBrL3GjIlZCGHJX_P4AHJnsAGq0j-IaDbrrJPM9yNfQ_IGStPCV4E-ThdXQ1NRGSJ4VA_20QYSXOpXDku8_4PQR8Qc3idYFDE3UuRGhl0pCjQC_ydySxW0b920WGtU1MJVX98OTW_OoW8GLuoCNsgWTlrBdgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جواد نکونام : نمی‌دونم داوران با تراکتور چه مشکلی دارن و امروز هم یه پنالتی و یه اخراج نگرفتند هر هفته داریم ضرر میکنیم
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139611" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFJFYWIHmAsPTueN8DFA-pfKkd-nrkvPYH6zPeRiK7jdVb0LMJxyA4ZAP6yNT0qqEbt6vXgtzhPSvPOv5A1X2Ry3gYlLauUNobbU3y-Sxo_PuODcINBAlwHmm_MrFAxVzAtk7xBiW6Otj-6xkM81VQHfAZkeYGAzgAvzP-Althdej0noRlZZssuqDB63RvNFU-c1rv2bVw2qrc17fz6nY3nN4g7glmCBBXonKuL58mY5rw3WA0IK78kVkIAtGtmHTpG-pzQ19UKK7-MuF8QAsCJZkWpLtegalU_gvVMMGONSW9mssysrAfux5nyWkBL1osWIwySfKImGR_dRiaZvDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از تمرین امروز سرخ پوشان بعد از یه روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139610" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
تارتار: ۶ تا ۷ بازیکن من تجربه بازی در دربی را نداشتند، خودم انتظار نداشتم اینقدر خوب بازی کنند
🔴
بگومگو با سرگیف؟ همه بچه های تیم مثل فرزندانم هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139609" target="_blank">📅 23:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
داوران دربست در خدمت تراکتور؛
🗣
بازی با پرسپولیس؛ اخراج نشدن مغانلو در دقایق ۳۸ و ۵۵ با کارت زرد دوم
🗣
بازی با چادرملو؛ اخراج نشدن حسین زاده
🗣
بازی با گل گهر: گلزنی با کمک، کمک داور که اعلام کرنر کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139608" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxzEwxBU_UA3L1TsMxoVbsldTaS4d08Y-zmiNvAw5cUXaPC6OABarAg-vnp9y2bDZMcpMjIBwuiBqDFlN1TOEoAQTpjlYMZ4C2hp8FnVvtLHSF1yJPFGF9Gupg6aPVFaN3PT-Zj3rXiuPYztt2gLsjyGXzu7521aKpgmHjeUIn2YF6FzKhCC9T8C60UECBTIoo27HcG9ww5ndm-4f2Y0pbSJUNFyYwWGZKRXrTC4G0CH8E1JPMmQ_eAcLaKwlgkq9XGlOOgi7iyNmQsfrUQENSD0XLKndKam77lUbrbr6q_ht9JQ0NOgkG85HzGgmDoZ1WtzNUy4anWcFBo7mcnZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139607" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139606" target="_blank">📅 22:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
🚨
🚨
🚨
🚨
فووووووووووووری
🚨
محمد عمری به علت مصدومیت از ناحیه زانو دیدار برار ذوب آهن و خیبر خرم‌آباد را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139605" target="_blank">📅 22:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=bYkefs1559o0CGVKF9VisCG9Y5sGF9za7FbkbxZX9q4fKMCsnrKV4UFZXNJmLuAyu2_S2DOKlc7rIYXx9VTxnYhKL1EOiwwSChkcvI4996BkvjvCAXqMNGQr_80Ho5G8Dm62ZMvFBDVf_hUIzpNSTievrSaszgG8qieUkchHlCHUEmG8LJiOyEVS5sROUZp7cetsKl-JzmLbYBy5J8KsoE3kN2782GLohPR8axQf9F-pcv33n-7yZIFCh-byZEYHsMxm8NT81W4vfBpv0CDWWOKoD5XR8yvAJ6dkjDiePLfQuLtlpEmvIocTPRXeIh4RAmLqoLMoIPU2TbPYfrJoSLoQbfCKw082d_YV68zOlK2eShn_oAS9QvoBJqTYtbxIDsvk_21kYjT80O79IfWFlQ5dPFP2dFsUxkJCQ-gI7RGfq50nt1soNLJNQH04h8kK8yghseIflxfL9BtFaWcD17fHroHxVlYapKdzXOxyKn0_hbxcddO5tFkKpWlk7GKwWx02Y9b_zHXHczZcRG5yd4uL8pxeqVTY2IeaJlhq2RlvAxvF2S_uez13if2iGGjUPHkP50zKPELW1oNrYT1hfDENRcryUh6cwjChvwEPAu7COoxYoc0pjSeQ-yQ0lbylcYZ-Dx2CnFPVNHIArVqOG8tq4aSfsn7p0wiNAsD1r20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=bYkefs1559o0CGVKF9VisCG9Y5sGF9za7FbkbxZX9q4fKMCsnrKV4UFZXNJmLuAyu2_S2DOKlc7rIYXx9VTxnYhKL1EOiwwSChkcvI4996BkvjvCAXqMNGQr_80Ho5G8Dm62ZMvFBDVf_hUIzpNSTievrSaszgG8qieUkchHlCHUEmG8LJiOyEVS5sROUZp7cetsKl-JzmLbYBy5J8KsoE3kN2782GLohPR8axQf9F-pcv33n-7yZIFCh-byZEYHsMxm8NT81W4vfBpv0CDWWOKoD5XR8yvAJ6dkjDiePLfQuLtlpEmvIocTPRXeIh4RAmLqoLMoIPU2TbPYfrJoSLoQbfCKw082d_YV68zOlK2eShn_oAS9QvoBJqTYtbxIDsvk_21kYjT80O79IfWFlQ5dPFP2dFsUxkJCQ-gI7RGfq50nt1soNLJNQH04h8kK8yghseIflxfL9BtFaWcD17fHroHxVlYapKdzXOxyKn0_hbxcddO5tFkKpWlk7GKwWx02Y9b_zHXHczZcRG5yd4uL8pxeqVTY2IeaJlhq2RlvAxvF2S_uez13if2iGGjUPHkP50zKPELW1oNrYT1hfDENRcryUh6cwjChvwEPAu7COoxYoc0pjSeQ-yQ0lbylcYZ-Dx2CnFPVNHIArVqOG8tq4aSfsn7p0wiNAsD1r20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139604" target="_blank">📅 22:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139603" target="_blank">📅 21:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139602" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=PidrzZ9cOIDK6pi9GwwLZGtQwM-JwxxzUIHl4kJl1KbR6ACYqyerXhQ72TUDcFeOULsQoS6LX_eRG0XhiSrDcj9SXp2A4i-zcFLqSYNu5gd007-flGPai2jdQ81Yp_yrORaLQ_9I7P6gD2wk-vLLrxl9pn5-lZMkHXHEWLlerpj_QakMUaRatKYiU7islfAUSloDUxomy5f8XUOHgU2B5wpb5vI2kCPY7MU2DLJIZ5fyuoV5jKFvhAQooAYbCX_918fputnN9OsaFmtJ6o6sF4tpG3shOKy9OM_4nTrc5DACygPWktaHoURLSU2j78IiDkkNhXg25Nd0ZtI2w9t5JrRkaZCxQMrmzPxMrNlCBmlEI_4VKhSYgMsYz4xb3r5jIpcHCIrUrhC-4BWx8ktnex8F7pT2HJDtgb1QcsEn0RloWHBEml6QP_GsByduE-RQl4lRMSTIBVQL9IaROMO4VPWWmzXHhOk7FAVUC7sawGARpKpDShwHQYQaoFpad30oF8tl-pqrCE3fq8jPHz87Fis3G4yAL_bAHcu34vJgDA7Z3zLisosVVha6dmyamsyY6MS42xQ23EGuI7_papBpy6VuhGT2zzz7AMpF4TeoVcptLRcPxggLAqSuCCN90TTUFGg1zgAzo_M_MaCrSSfaNC16o_hom1fB-ImWGm8JIBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=PidrzZ9cOIDK6pi9GwwLZGtQwM-JwxxzUIHl4kJl1KbR6ACYqyerXhQ72TUDcFeOULsQoS6LX_eRG0XhiSrDcj9SXp2A4i-zcFLqSYNu5gd007-flGPai2jdQ81Yp_yrORaLQ_9I7P6gD2wk-vLLrxl9pn5-lZMkHXHEWLlerpj_QakMUaRatKYiU7islfAUSloDUxomy5f8XUOHgU2B5wpb5vI2kCPY7MU2DLJIZ5fyuoV5jKFvhAQooAYbCX_918fputnN9OsaFmtJ6o6sF4tpG3shOKy9OM_4nTrc5DACygPWktaHoURLSU2j78IiDkkNhXg25Nd0ZtI2w9t5JrRkaZCxQMrmzPxMrNlCBmlEI_4VKhSYgMsYz4xb3r5jIpcHCIrUrhC-4BWx8ktnex8F7pT2HJDtgb1QcsEn0RloWHBEml6QP_GsByduE-RQl4lRMSTIBVQL9IaROMO4VPWWmzXHhOk7FAVUC7sawGARpKpDShwHQYQaoFpad30oF8tl-pqrCE3fq8jPHz87Fis3G4yAL_bAHcu34vJgDA7Z3zLisosVVha6dmyamsyY6MS42xQ23EGuI7_papBpy6VuhGT2zzz7AMpF4TeoVcptLRcPxggLAqSuCCN90TTUFGg1zgAzo_M_MaCrSSfaNC16o_hom1fB-ImWGm8JIBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139601" target="_blank">📅 21:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
🚨
🚨
🚨
🚨
فووووووووووووری
🚨
محمد عمری به علت مصدومیت از ناحیه زانو دیدار برار ذوب آهن و خیبر خرم‌آباد را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139600" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139599" target="_blank">📅 21:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139597" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=OgLAE9Kfgdbhs7nyTsTk75mfnvWZQWGYXX-Q2uFy2tAT6QqV6RJUdGmrZd0hOYKWxx2RuHn6qnYw5-gc2BX-FYZTxxjX00orWqt8rZUO_cAsUjnRq3mSt2ijiBGlYGS2uk5hSghDAfXhcEe3T8ZYi55Sm-Yhcg1o4Y0JjR7ePacAc9ahsiog0Rj5qheRvjEzB5lBMeHs2PWmvsW0h6uFKBPjKbGC-gMK1DJCItaNQE9RHpPlzENkqLcLccTOMnnrs2eZpTlQ_jn5SHDQt2ej9LV5YZHtuHG7xmG0LOn-O5vPMDHBcqFKVTZfhMNvYZGxYX2fBFlVzVRrzhbhQ_gvvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=OgLAE9Kfgdbhs7nyTsTk75mfnvWZQWGYXX-Q2uFy2tAT6QqV6RJUdGmrZd0hOYKWxx2RuHn6qnYw5-gc2BX-FYZTxxjX00orWqt8rZUO_cAsUjnRq3mSt2ijiBGlYGS2uk5hSghDAfXhcEe3T8ZYi55Sm-Yhcg1o4Y0JjR7ePacAc9ahsiog0Rj5qheRvjEzB5lBMeHs2PWmvsW0h6uFKBPjKbGC-gMK1DJCItaNQE9RHpPlzENkqLcLccTOMnnrs2eZpTlQ_jn5SHDQt2ej9LV5YZHtuHG7xmG0LOn-O5vPMDHBcqFKVTZfhMNvYZGxYX2fBFlVzVRrzhbhQ_gvvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139596" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
با اعلام سهراب بختیاری زاده در نشست خبری پیش از بازی با آلومینیوم، صالح حردانی کاپیتان کیسه از این تیم اخراج شد و دیگر عضو این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139595" target="_blank">📅 20:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
خبرگزاری آنا: صالح حردانی بعلت درگیری با آسانی در پایان دربی و مجموعه رفتار های او در تمرینات از لیست استقلال مقابل آلومینیوم خط خورد
🤣
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139594" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
وزیر نیرو:
✔️
✔️
دیگه قطعی برق نداریم برید عشق کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139593" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139592" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
سومین باخت متوالی رحمتی ...و  بعد از شش بازی همچنان گداوند گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139591" target="_blank">📅 20:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
بلیت دیدار پرسپولیس
🆚
ذوب‌آهن از همین حالا قابل خریده
👇
🎫
footballeticket.ir
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139590" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139589">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
✔️
✔️
و همچنان ادامه داره این سبک چکش ..یک هیچ یک هیچ بردن ..دفاع اتوبوسی و گلی نخوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139589" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139588">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139588" target="_blank">📅 20:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139587">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139587" target="_blank">📅 20:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139586">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
فدراسیون فوتبال هم از احتمال برگزار نشدن جام حذفی در فصل جاری خبر داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139586" target="_blank">📅 19:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=kQP8pw6CQT9bnQ3QSVdYlqwu_BpSJAfUMzgNttb_-JfZSlwbgEdlnD8_UfKNFPf86gN1a4bm0XVnhfouMEKXFN2OkFT498IBZvpRPNc3W9xDzma6kAkba47zE_sDn0PQ628BiOOe2BWl5YheXntS1dfyMKFO57J43HW9xyaOqN42yWvWmDQuAEYAO_xopdMuX9XJQ1FxHFO7KYhnpq5Aov043P8kbxpUue0EzblDSMm29JvOiQqpZ88_YKFJs78bdIG7Mw2qi5uGIk8JZLaEZ19rB0nFoGOkfVA3F7LcrPiSqiLdxlReZJAQmi3lHjifORRQ4ox8zWcTXCOH8vDn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=kQP8pw6CQT9bnQ3QSVdYlqwu_BpSJAfUMzgNttb_-JfZSlwbgEdlnD8_UfKNFPf86gN1a4bm0XVnhfouMEKXFN2OkFT498IBZvpRPNc3W9xDzma6kAkba47zE_sDn0PQ628BiOOe2BWl5YheXntS1dfyMKFO57J43HW9xyaOqN42yWvWmDQuAEYAO_xopdMuX9XJQ1FxHFO7KYhnpq5Aov043P8kbxpUue0EzblDSMm29JvOiQqpZ88_YKFJs78bdIG7Mw2qi5uGIk8JZLaEZ19rB0nFoGOkfVA3F7LcrPiSqiLdxlReZJAQmi3lHjifORRQ4ox8zWcTXCOH8vDn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
داوران دربست در خدمت تراکتور؛
🗣
بازی با پرسپولیس؛
اخراج نشدن مغانلو در دقایق ۳۸ و ۵۵ با کارت زرد دوم
🗣
بازی با چادرملو؛
اخراج نشدن حسین زاده
🗣
بازی با گل گهر:
گلزنی با کمک، کمک داور که اعلام کرنر کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139585" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139584" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
🖥️
وی ای ار داره چک میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139583" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139582" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139581" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139580" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139579">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست  مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139579" target="_blank">📅 16:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHw00V7NF-nsMkth0gvGg_OKCtE7p3pOu7UeHhh5FpKjm0R82uiP0cFRh8pRFrWxH1wxaWSDajaEth3xmoOh4yiIyaqpwR1d3Ogc-56xZY28bazSc7aPXdMnC-MZIGmd9kpaFhLNm2O1rusFw0jR8Pi20Ji6lz02GRcvYiTEHHxa4D1g6yN332dR7LFnZEpT6WGTxxQ1jRVr0SryBSeP3Uy_P6FgPSABpylanoM6j7Er9rH1ZDElAxV4DIa2-ORZIVNRkeNPR-bmpdtAA_h8oCGQ61v1p995eUQFSuuD5GBQMXvteDzWFFBrK8IVBJ_R0vvRwY0IbjKUXPJvHDaJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
حکم سنگین فدراسیون فوتبال علیه مهدی قایدی
⚪
با رأی کمیته وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش از مهدی قایدی، این بازیکن به پرداخت مبلغ ۱۸۰ هزار دلار بابت اصل خواسته و مبلغ ۵ میلیارد و ۴۸۹ میلیون و ۵۷۰ هزار ریال بابت هزینه دادرسی در حق خواهان محکوم شد.
⚪
نیکومنش مدیربرنامه سابق قایدی است که گفته می‌شود واسطه انتقال این بازیکن به شباب الاهلی بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139578" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139577">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
روزگار خوشِ «مملی»!
❌
❌
محمد خدابنده‌لو بالاخره در این فصل به فرمی که هواداران پرسپولیس انتظار داشتند رسید؛ هافبک جوان تیم تارتار حالا تبدیل به یک مهره اثرگذار و مهم در ترکیب این تیم شده و روز گذشته هم در دربی ۱۰۷ فرصت داشت یا یک سوپرگل خودش را در قلب…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139577" target="_blank">📅 14:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lchQke29vR1o1rAIMo3SbhtId1CThaGjUiFEtV3e6e32nfJYym2PfTtb0ibnV8VNVJ34hBK2SweNV-pxMfq0rusjjRIi6ds1WmGcUL2y3NzLF3mRAGmFzEOjLDLKrXl4sXZZaJy1iPfoEe9mEjrLhH0cxIJd4gjtFUEdC1Lo1LqODiJG5UWGyOrUA0cjo6AEJ3nMqt5hdZYmMfaT4cAqanZcL7TWzAmsiNDiDhXITh59tNuR-iH4ugHEZJWM5QFHnhu3RlZHcGTtN92AxbWLyHOi5uDpIgVXMznfGoxzyvADJ3nbHsCn5jWO70DSryMX2JpX3mlpOGIoAP1BDcy-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کنعانی‌زادگان به ۱۱ دربی بدون شکست رسید؛ اما رکورد همچنان دست عالیشاهه با ۱۸ دربی بدون باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139576" target="_blank">📅 14:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139575" target="_blank">📅 13:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlOvmcHuemnuz3_ZH3hG9g81hZ0CHQyEIrPIST2bt3ftcSR7TJGvDGfFJuBOAoHKP6Ry6SNctcmyCaR2pCPe4p5wmUoDhKJGyD1yKfphzRhmD9LIf1AB66Ok9PLgVSPPiCi34Kih4dSvj8Ayj2Tfs4-_Xq7KKOrUNqajAz5Mx5YOV2gi0n4fV7bqdviqYP6nRnL4NopO0iRhfy12tp_BUlCzpjs4PBZfnfjXmzXx_WBi4vmbRMle1BTvzZblOx2BeFf819AN75qPNhURNPEh6louuWb9toPIyPkOjieSmsmXfNh4fZxWRvP9WWpPLTEDqpOP1zUuzIdzOxI_g03qjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد بزرگ در جوزپه مه‌آتزا
🔥
اینتر و ناپولی؛ جدال برای صدر
یک شب سرنوشت‌ساز در سری‌آ
[
اینتر
🔵
🆚
⚪️
ناپولی
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139574" target="_blank">📅 13:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuZLcwdC8hOP8MIO3VxFBGNhkdUG_jeWoND8GgdFeeiZCsK6rTv1PBiv6nCdVOTriFREkVM3Sga6bWHlDfca4EDv_cUSen3AedJBytx5tou8C-Rmg2D4aXy0zWp3UFvx6E5My3A7WKrMqhlYp-kBaFT-pF3YCWlVxXV3LA-Ct0fMY0r82v2BCXQoI70t7CqKJ4rHvGUSvyD5BHRtbJLU3t0mI18nixAiQwplJNt-wPp1KydPok_ZR8wNA2q5Lx3Gsyj9MonXZpzP_kfamKr9W8cWTp6lFvtLbcU-Pb0URlwNwS-OLPBPbHWY2nsX-UasvGnxFrQPUSjSXE3jjUbsxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیس از سوی کمیته انضباطی ۱۵۰ میلیون جریمه برای استفاده از مواد آتش‌زا و سر دادن شعار علیه بازیکنان حریف و ورود تماشاگر به زمین در بازی با ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139573" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
احتمالا در بازی با ذوب آهن بیفوما زوج علیپور خواهد بود و وینگر چپ پرسپولیس تغییر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139572" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139571" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139570" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139569" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHe_7V_vmKmbrhh2g1Shbkd1LjidTl0qLSn-XDH5t2KXv0f2XszcBOLNn-2sqnRXs64nr8c0yFlggRR78l1whWF--D4fy9tXtlYBVU5GpquiAGfsqb1jBm2LPQiP_O2wX5cOc2JEEgxdmnhJKcnkM0tbVv8bUh3Wq1no57TLSJszSKM3WHtHhmWZmaGiwMCJ3BLA6qSCNUCp7O8-HFs1g2Qx8iADERlCQUpmc9NnvUMlwPq_Q2UgOv2mn7dEK-u1GgT1LCBt4Xk1coS-Bc6qjFztxE_m1qTXXPOSAInj9YRuoxUS4f58pi9490M3YFnHgQ3OKMrylV8Gwk4eMKEoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139568" target="_blank">📅 08:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT28unPafYHKVbgvSqvT4GgBm983_uKf2dFQT7cR_5R_UXZAx6p9JPYqlt0YxOXOalSEC2CiCAejjiSMoskySrVqP8Z8M_a5aN5wV7y3CW53u8HG5WIbPKGwht4DEiL6pu_h-exIL3u34E6gPBc-zwapl5Guusm-VxcAXKNj9NDLLEBK2FhVte23uB816-ekQ4wNTz6PggjED3l6suVCN8SOBQzs6yduevMpZFm8IeAItr5Z5hZvqi5mIMwzSWfoTbBuyjn7CWaeDf22vrpQw6uzArd3RvR3rErvQHST6H-tzSctC70qX3QgTiNOyNaDNRlzlv3r8oJuoUPfrbsJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبردی تماشایی در یواس اوپن
واچروت و تیافو؛ جدال قدرت و سرعت
شلتون و شاپووالوف؛ دوئلی برای صعود
🎾
ولنتین واچروت
🆚
فرانسیس تیافو
🎾
بن شلتون
🆚
دنیس شاپووالوف
🟡
کدوم ستاره‌ها از این نبردهای هیجان‌انگیز موفق بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت نود:
👇
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139567" target="_blank">📅 02:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه عباس کهریزی ستاره جدید فوتبال ایران پیشنهاد اولیه استقلال رو رد کرده و گفته تمایل داره پرسپولیسی بشه /ورزش3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139566" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
✅
پایان دیدار تدارکاتی:
🔴
پرسپولیس 1
🔴
آلومینیوم اراک 1
✔️
گلزنان: علی علیپور برای پرسپولیس و عباس کهریزی برای آلومینیوم اراک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139565" target="_blank">📅 00:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
تارتار در بازی با ذوب باید به بازیکنانی که بازی نکردن یا دقایق خیلی کمی بازی کردن بیشتر میدون بده تا بازیکنان اصلی هم کمی استراحت داشته باشن
💬
خدایی نکرده دچار مصدومیت هم نشن
💬
🗣
🗣
مثل ایری، محمودی، سلمانی باکیچ
💬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139564" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=vLP6EPw7IjOtOzDykeyXJOni9NUwJ9BGFrugVPfD2Jv9BAJW3aiuiWHfzwXDdq5DT-5_7wrQAXVWEBWqviCrU9Suq0fPKrjW9Ok_lqyhz7P_Tq3OH7IjcFFOq-zdcmD4Dwm8QAfIVm1LiqwDM1OvWGsvrr7Hkx65lv0UktMsLDfEhcWBHFcENd5klKtPsjs9zUy_yHTsRELYGxvj2iieLnMqnUcvuy7HltCHrgmp8cgh8AAvkKBPJk79-ZXIWWdG81ftj6O1j8g_N6wlRa1RIFk_LBG3p4dcmBne1RkD80VN4sE7FwRVqnjg63QqWv5Sv5vaNEsbgqbVPxJESTv_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=vLP6EPw7IjOtOzDykeyXJOni9NUwJ9BGFrugVPfD2Jv9BAJW3aiuiWHfzwXDdq5DT-5_7wrQAXVWEBWqviCrU9Suq0fPKrjW9Ok_lqyhz7P_Tq3OH7IjcFFOq-zdcmD4Dwm8QAfIVm1LiqwDM1OvWGsvrr7Hkx65lv0UktMsLDfEhcWBHFcENd5klKtPsjs9zUy_yHTsRELYGxvj2iieLnMqnUcvuy7HltCHrgmp8cgh8AAvkKBPJk79-ZXIWWdG81ftj6O1j8g_N6wlRa1RIFk_LBG3p4dcmBne1RkD80VN4sE7FwRVqnjg63QqWv5Sv5vaNEsbgqbVPxJESTv_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد تقوی، در برنامه هت‌تریک در آنالیز دربی ۱۰۷ استقلال و پرسپولیس گفت:
✔️
✔️
«از معدود دربی‌هایی بود که همه راضی بودند؛ تماشاگر راضی، مربی‌ راضی، بازیکن راضی. یکی از دلایل موقعیت‌های زیاد گل، دفاع نامنظم دو تیم بود، هر دو تیم به سرعت به فاز حمله می‌رفتند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139563" target="_blank">📅 00:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=jr1XCfghRPrgTNqQUKHJtxhOBAuGCV_HKuhEsdr2kCKUcUHOKMvGlYdRl5aSMLFVUghH9F5llq1aPMQ_N87OSCQhW4CMrklb2y9eu_ehf_0p54agoeOnDRaybZD8UDTcDA-WpO3m2KdhfkolesbRVgMIqUql8RhIZQYrN-erUxcvo90RXl5HuoJ-7V8HC20CrmUB1LTGjZYBC_EqNndCaq2q4E5UeVuZy6vsTOf0sTuGbmSpF5Mwed0sD-wS8CCCtfXVTCL7lHU2A1J3gNPmkoIfo9nx-U3aMM5raJMaRsqdT3F6G1q-XuWxFiobO0yUuuMC4-EzCzcdMnoh4rXNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=jr1XCfghRPrgTNqQUKHJtxhOBAuGCV_HKuhEsdr2kCKUcUHOKMvGlYdRl5aSMLFVUghH9F5llq1aPMQ_N87OSCQhW4CMrklb2y9eu_ehf_0p54agoeOnDRaybZD8UDTcDA-WpO3m2KdhfkolesbRVgMIqUql8RhIZQYrN-erUxcvo90RXl5HuoJ-7V8HC20CrmUB1LTGjZYBC_EqNndCaq2q4E5UeVuZy6vsTOf0sTuGbmSpF5Mwed0sD-wS8CCCtfXVTCL7lHU2A1J3gNPmkoIfo9nx-U3aMM5raJMaRsqdT3F6G1q-XuWxFiobO0yUuuMC4-EzCzcdMnoh4rXNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139562" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=SM503mCw4aiEacOoJUY37f2OUuuzDIvmBcDEjiIOiyMyKPT2OZBmyWUQYhK5rpH8tb4qOak275_-SDxMXZMqgyeYPuilVsVQHtIkETNuMJTOMF04Vp7HmO05I8pDE5isL9LnGa-MkBrsdQ0jUuY4tBD1qE6k92i8Yj5FIzE8xL31NfT8ptjqQ6vzoD7b81B90QsFi8YYy1iPHMVsdkB4d3jxoHrOyxc5ZiWaRYejAWYcMuCs-LmnuaykdTFk0VtkzuBPH8AsGuLCaUE7fIYGGIhpcJjTibFjXt9yF4k9_U3u3LajzP2DRb4GXusOdsC88Pi_b1AXBjYEzb2Mf8NjNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=SM503mCw4aiEacOoJUY37f2OUuuzDIvmBcDEjiIOiyMyKPT2OZBmyWUQYhK5rpH8tb4qOak275_-SDxMXZMqgyeYPuilVsVQHtIkETNuMJTOMF04Vp7HmO05I8pDE5isL9LnGa-MkBrsdQ0jUuY4tBD1qE6k92i8Yj5FIzE8xL31NfT8ptjqQ6vzoD7b81B90QsFi8YYy1iPHMVsdkB4d3jxoHrOyxc5ZiWaRYejAWYcMuCs-LmnuaykdTFk0VtkzuBPH8AsGuLCaUE7fIYGGIhpcJjTibFjXt9yF4k9_U3u3LajzP2DRb4GXusOdsC88Pi_b1AXBjYEzb2Mf8NjNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش حسین عبدی به عدم دعوت از امیرحسین محمودی
🗣
حسین عبدی: امیرحسین محمودی بازیکن فوق العاده ای است ولی وقتی من او را حتی ندیده ام چگونه دعوتش کنم؟
🗣
‌‌پ.ن: ما که از خدامون هست دعوت نکنی ولی این حرف عبدی توجیه قابل قبولی نیست
⚪️
بازیکن کیفیتش مشخص هست
🔄
همین دقایق اندکی هم که بازی کرده برای تارتار نشون داده قابلیت هاش رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139561" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139560" target="_blank">📅 22:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=vPqOyUM5AB5dehDffbH-FQdytBlPwWCMkJ9h5m-DQeDUIOLe6s7XO6PKynXQqypOI7uEklDWJuWA1XdQMAGG2Tym9ofDHm9Zw_ZFnK0ZbsP0K924ycwQSzEfhWIw4UiuhnmtkppgFEkkCBZpCsDVP72zGfcW41XtisFzYf8WauLMkCvZxykncbAoJLsPA0NvBmT77mPmudLm9Kh6fVinW3x6NIsuJAIA12H6QrFW_j-dHKodRgShRtv0LrHhFknPWT8nVd6MrrK1K8QygubwRiOyVMoXKJcWHwpi7DR_X1j7W9NG4un2r8_7Sr2iggsYXuyMGBXDBD2gwyonhHFtKkmnD_1fz0Ha4UqX6tcMXq_jBI17WK_-VFGrFCEWqJii8OqyoaxzEUWYYpY1sjNX7zAg761gSh5E6duAgIdTULzPs8uPPXONBptwLlbgfjtjx_WUV4IGcjEKFg0eyaBazt2t1w4CCoeBlnQhp8l4RxFCaeciWHFVYu4MCl-qVgg7-mlJP5hVsddVcNRlRXMSLO5F0vh13v1jE34724Hrrpu9oIOkDVrKDIXEVAEt6LQjur_RLPpZFCjUmDXffC7G6-q2H6Hk7drZVTTXM2XhE2hUKM6rtDPz7ddJX5oeRibwya9UBjjqkhHOo-fiiA6f3LBMH1SKa1fcWQBkzR2GhNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=vPqOyUM5AB5dehDffbH-FQdytBlPwWCMkJ9h5m-DQeDUIOLe6s7XO6PKynXQqypOI7uEklDWJuWA1XdQMAGG2Tym9ofDHm9Zw_ZFnK0ZbsP0K924ycwQSzEfhWIw4UiuhnmtkppgFEkkCBZpCsDVP72zGfcW41XtisFzYf8WauLMkCvZxykncbAoJLsPA0NvBmT77mPmudLm9Kh6fVinW3x6NIsuJAIA12H6QrFW_j-dHKodRgShRtv0LrHhFknPWT8nVd6MrrK1K8QygubwRiOyVMoXKJcWHwpi7DR_X1j7W9NG4un2r8_7Sr2iggsYXuyMGBXDBD2gwyonhHFtKkmnD_1fz0Ha4UqX6tcMXq_jBI17WK_-VFGrFCEWqJii8OqyoaxzEUWYYpY1sjNX7zAg761gSh5E6duAgIdTULzPs8uPPXONBptwLlbgfjtjx_WUV4IGcjEKFg0eyaBazt2t1w4CCoeBlnQhp8l4RxFCaeciWHFVYu4MCl-qVgg7-mlJP5hVsddVcNRlRXMSLO5F0vh13v1jE34724Hrrpu9oIOkDVrKDIXEVAEt6LQjur_RLPpZFCjUmDXffC7G6-q2H6Hk7drZVTTXM2XhE2hUKM6rtDPz7ddJX5oeRibwya9UBjjqkhHOo-fiiA6f3LBMH1SKa1fcWQBkzR2GhNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139559" target="_blank">📅 22:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
برخلاف شایعات هفته هفتم لیگ برتر کنسل نشده و قبل از فیفادی برگزار می‌شود.
✍️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139558" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139557" target="_blank">📅 22:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139556" target="_blank">📅 22:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139555" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139554" target="_blank">📅 22:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=JB-VDnQ2hSo0yHrXWCgpjvOwW7m4vobIVrpJDvxCEcERXVhNoyBm0ovLSr20t3CRti-QX1tZIC7FFRKHX1C8dssOAA6T72CyQ09G2El5IKH4uxrGEUUcTj1kRuRb-TfW5GTY8C8qkIWAVKe3j-cOGa-XdLTjYTUTjaPTn8Sd8eauaG98kUdP6j3q_nNp8Fa1EhB6fLICV-Sk3mkrgjPCmfRA8JxvMcjd3xemSBQqy4lZRENGdUBSD2_aCG6ETVnvkObADlnMVa3MWwTruNE3K2WVTjFisu2oYfa3DIFSxdFHNVp2tVKQVSXBkhTuOt7pImyKxVet7CbQjo12MgnV3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=JB-VDnQ2hSo0yHrXWCgpjvOwW7m4vobIVrpJDvxCEcERXVhNoyBm0ovLSr20t3CRti-QX1tZIC7FFRKHX1C8dssOAA6T72CyQ09G2El5IKH4uxrGEUUcTj1kRuRb-TfW5GTY8C8qkIWAVKe3j-cOGa-XdLTjYTUTjaPTn8Sd8eauaG98kUdP6j3q_nNp8Fa1EhB6fLICV-Sk3mkrgjPCmfRA8JxvMcjd3xemSBQqy4lZRENGdUBSD2_aCG6ETVnvkObADlnMVa3MWwTruNE3K2WVTjFisu2oYfa3DIFSxdFHNVp2tVKQVSXBkhTuOt7pImyKxVet7CbQjo12MgnV3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
#منهای_پرسپولیس
👾
عبدالکریم حسن دفاع چپ سابق پرسپولیس، به این شکل با پیراهن الشمال در لیگ قطر گلزنی کرد
🚀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139553" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVwXTlMgTPmqKWRVqzZMb6LtT7i8oJ4yqTJi0EYUsopHIaVEL3Rf73U2cbgqfx2at5LaclSc1cCkDLqKo2Uia0VupD1u1oGE5JG_4ebSe84ioENxwfWCLSseWwFALQw_TrJvrXYjEPnGCi_VoVGwiSuF4kR7PjuuMoY9hSvG98eIoWCiGqEz6A2KDJ9OLX9QZJlAOQwTjso3sSQEX84O5n-DucnnhYrd3e7Vv-t2TwkgGxs35Vrsen4CevYYgcpArSivEly06kkSyS1bduBB6WQlaEA7xuoh7zzfqpe4KgUdPcwrpH7ASNoRnRJvR79QzqixSiDLAq2NIHfIasIwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیورپول آماده‌ی شروعی قدرتمند
ایپسویچ سد راه قرمزهای مرسی‌ساید
نبردی برای فتح سه امتیاز
🔥
[
ایپسویچ
🔵
🆚
🔴
لیورپول
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139552" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139551" target="_blank">📅 21:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAW08f0QKqS9obHlGz2FaIT2WsS5Ez-cyd58RFSqCF5NUhrg7LO4nSQHkXElWYJmwuwetQ3ZfGjOkgpX6bDUxQvG2H5mHYRhj0TEqHE39106qjGqHKnPoX_G4zo-YaXcTM7hNuMhTmMtMLtsA1_ErLqLRz3Yqs7NeNBgINZw4jIx42TgCbTQgweuCSM3WH--Bl5PRKGKo2FBJPPm2iNOId0lAZdb9MZZpkAcfkXDmYaeWCR9hFxni6EU1TNV5xIfVQE1YgKvdMFFn9y0KVPTmP8q0L8Mvc_zuuuud4ggMZnrg361L6l-L05Xjf2fyRoco0t0HwJEz4KtshQ9-oRmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139550" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW1vqhnj1Hsq6Ri8xJSKjzfhehSGAk-8Oau3isOqyCushaA0goQxWOm31FU7KBcox3jzF-aq5t9rw0_ZH8UyGvxjcylVx4dogw9L8J7RMv6w_WRpsJEcRRgDGI-wPF3G1r_p842NBFmcITtmipDV2QG7sCeRT84VRnBtGQbs0hPDzIup6zOhwk26io8ISMro38oNQTrZEl8q9-C3yPOOEOgRFdVmZjAxm7j_xtfHn6dw93MQhvboKsluJvsTEYccTzADDYmftdxz8xKzy3YR1bFjZdXnzKStRyvIczN9mVtArhnwkob7MIPbZNfkoQw_9bDbvDnR-0jth5xjC8yh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده نداره پس سکوت کنید بزارید خود (CAS) معلوم کنه شکایت به‌حق هستش یا نه‌...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139549" target="_blank">📅 20:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139548" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👀
❓
محمودی ۱۵ دقیقه هم بازی نکرده امسال… اقا تو پستش ترافیکه درست ولی نمیتونی هر بازی بهش ۲۰ دقیقه بازی بدی بازیکن روحیش از دست نره ؟! محمودی چند ساله دیگه عصای دست پرسپولیس میشه اگر آقایون نسوزونن بازیکن رو…فقط بازیکن هایی که از گل گهر آورده رو بازی میده اقا…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139547" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
با اعلام باشگاه پرسپولیس، آکو باتری اسپانسر جدید این تیم خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139546" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKEPTac0TYQHjkSHY1Iy7jOChdjNTCM_xVhtrIN1uSXz6QpraqTbqg_q-GNtZfM3Mjp6OJi5aZYy9_H-Opc-0JMo2ixZg-q7E6Wm4CC4hGC3i2uk5DrZz250UR5WtE77_-NL5MULD4hiNToeKEsSbEPisS-BZBn2sqNjMIyUrsmbq_IAw7b89xCZ25yJPNhSRNqc957NWAqH1U78Hh9y5iqkMbtPD-5JZz5xhgu8dUhs_DzpaequMoG1MRxm1TN_VTZ11bgCRb_YQ5EgDoVEbi28pix6T3ST07DZo9edslXUwgrL0RO1qRXXteCVBe3y7xhF1qSwf1jmPCCQq0Oy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139544" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139543" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139542" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
جنجال و حاشیه در اردوی کیسه؛ با اعلام سهراب بختیاری‌زاده، صالح‌حردانی بدلیل رفتار ناپسند و درگیری با سرمربی و یاسر‌آسانی در بازی دربی، تا اطلاع ثانوی از حضور در تمرینات کیسه منع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139541" target="_blank">📅 18:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚪️
⚪️
⚪️
فوتبالی: سهراب بختیاری‌زاده به حردانی، مهار اورونوف و بیفوما رو سپرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139540" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=u1ePb5_ziyGG56oc-ahTzCzltgi3vEtJtLyvcvjAiBeIxsn2WycsrM8-4Ut95E-Kj3Q7Uy0t-pNUpmCC2geFsBERc7Epnm80pksAqYJtv17ShBHFjzk_djtxHPpPTU3ecIRKZ5phqhFlCofmdcZ6J8py9nfLkDbEpPyRjXdF_wWe-TQn_MtEFtVgEYya6QNkLDL1Br0gCxaufqqcuEASoRxGur6oydMyO0ZGQwVfyD7CUzEriPDT2dkEv2qMBIJrgQH7HFR6eLUA8m50sUbou7z8FnLmH_FtgJrXs34Z2tq1-KA1bNO9x5yyPkX7xam2VMfRgh48ZuLYvdSvVHy8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=u1ePb5_ziyGG56oc-ahTzCzltgi3vEtJtLyvcvjAiBeIxsn2WycsrM8-4Ut95E-Kj3Q7Uy0t-pNUpmCC2geFsBERc7Epnm80pksAqYJtv17ShBHFjzk_djtxHPpPTU3ecIRKZ5phqhFlCofmdcZ6J8py9nfLkDbEpPyRjXdF_wWe-TQn_MtEFtVgEYya6QNkLDL1Br0gCxaufqqcuEASoRxGur6oydMyO0ZGQwVfyD7CUzEriPDT2dkEv2qMBIJrgQH7HFR6eLUA8m50sUbou7z8FnLmH_FtgJrXs34Z2tq1-KA1bNO9x5yyPkX7xam2VMfRgh48ZuLYvdSvVHy8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=uOoo2elgooqZEjwXG2X5hJzrjC348jlFJyGaQm-hK5VJ19Qmd38AIL7Uus0ZWlORnLgji0wTmYy_Av3MuJka5o52tYSEGc_FYGoedUDFCF7xfh9jigUo4FpbvvAJBklDicMpMcR3Em-yFtsC-80G4Ah2mYdib7aAF67c5DYqOpsQzRIv6LHM2UQ_9zQrGacPX7rUL-1aNdqHmd0hTtJCaxQJ9ZwO0YSQriQo15EgJvZlCLzsXaNaiqqMECdQAAYlUm4YeFZTMBtsgU-475z0DEm6GNgbA2mOps7jUKTlYIqZP_6TMhJ2RBUKifrGlju1TkJJoRDxMkgc0gVPz3gaVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=uOoo2elgooqZEjwXG2X5hJzrjC348jlFJyGaQm-hK5VJ19Qmd38AIL7Uus0ZWlORnLgji0wTmYy_Av3MuJka5o52tYSEGc_FYGoedUDFCF7xfh9jigUo4FpbvvAJBklDicMpMcR3Em-yFtsC-80G4Ah2mYdib7aAF67c5DYqOpsQzRIv6LHM2UQ_9zQrGacPX7rUL-1aNdqHmd0hTtJCaxQJ9ZwO0YSQriQo15EgJvZlCLzsXaNaiqqMECdQAAYlUm4YeFZTMBtsgU-475z0DEm6GNgbA2mOps7jUKTlYIqZP_6TMhJ2RBUKifrGlju1TkJJoRDxMkgc0gVPz3gaVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
گل محمدمهدی محبی از زاویه‌ای متفاوت
▫️
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139534" target="_blank">📅 13:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
