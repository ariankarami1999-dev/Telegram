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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 12:33:46</div>
<hr>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/139627" target="_blank">📅 10:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/139626" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/139625" target="_blank">📅 10:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/139624" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/139623" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
⭕️
🚨
🚨
🚨
🚨
خداداد بعد از اشتباهات داوری به نفع تراکتور در زمین جنجال می کند بعد از بازی هم مصاحبه  جنجالی را چاشنی کارش می کند تا حواس ها از داوری پرت شود. یک سناریوی تکراری! اما آقای عزیزی! عالیشاه رکورددار نباختن در دربی در حد شما نیست؟تفاوت شما با تماشاگران…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/139622" target="_blank">📅 09:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/139621" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/139620" target="_blank">📅 09:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/139619" target="_blank">📅 09:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/139618" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/139617" target="_blank">📅 09:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/139616" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/139615" target="_blank">📅 00:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139614" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139613" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139612" target="_blank">📅 23:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=EXqOiJKGalVO4kAqBhTPYsWpiCIShUlnyelr9NlZa6kSa82hrRJaPUDWXl6OFiJ_DTXbvK3od2oj7D8okb5ORob95W1BIQvUaG-vD1bPf_O0fhb4rNEsDLHjaItAjbEAr-ErNsJVGChATbzyIdo6DLh0Eq-m5RTBHsP6kKCUiIKyiVGGjlJzAc94RZ6UhgCOk7qr9CQkC4fTJBtDBm7g6vU4ozjuolyWqZPul18aX5RbDKPa_OnVesqEfMd0x3pbYV9v7Fcqnv_uRICaxk5W6jlefbTglANcE0gHbKNfyLXa2HLqGtrqWy9_E9QugSsGVW8UZYDNkxRMJbawj-ZUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=EXqOiJKGalVO4kAqBhTPYsWpiCIShUlnyelr9NlZa6kSa82hrRJaPUDWXl6OFiJ_DTXbvK3od2oj7D8okb5ORob95W1BIQvUaG-vD1bPf_O0fhb4rNEsDLHjaItAjbEAr-ErNsJVGChATbzyIdo6DLh0Eq-m5RTBHsP6kKCUiIKyiVGGjlJzAc94RZ6UhgCOk7qr9CQkC4fTJBtDBm7g6vU4ozjuolyWqZPul18aX5RbDKPa_OnVesqEfMd0x3pbYV9v7Fcqnv_uRICaxk5W6jlefbTglANcE0gHbKNfyLXa2HLqGtrqWy9_E9QugSsGVW8UZYDNkxRMJbawj-ZUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139611" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Halvc0kYdPTPAgihhcITlPCSp2B_npNHpaKyZoVYThj5ZT3x_pGAD6SEkT-qkYadTwd2EVr3r6A8VMYK0kL5jx2Ck7a0ezgvkGoE-UP8x_lLkD5HkI6ioq53PH-4zGrIm7COn7b1BDOIbg6DhkEIfP9jyNCtDcZ4d67JVptUZfT24D01b1L4ThKBTpVylRzqWwFyMEw9YJjDBZOOUrDt7CBxvMoGnibk6EZWCtrJmQRndQxNYcOmSqhGkPHhRvRLCyY2ougrBdn4NBRcdBvmsosy4V9H_NtQoNsxs7abm0RG937pmOhmonHRSpTqMKanSUoK_Qp-4535ry9ucYcGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از تمرین امروز سرخ پوشان بعد از یه روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139610" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
تارتار: ۶ تا ۷ بازیکن من تجربه بازی در دربی را نداشتند، خودم انتظار نداشتم اینقدر خوب بازی کنند
🔴
بگومگو با سرگیف؟ همه بچه های تیم مثل فرزندانم هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139609" target="_blank">📅 23:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139608">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139608" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuSgnei_DchAmOQ987KzEPgM1TH2nKZ4UKEiW9x0KBLNzAhBJaQ_OxmHug4aeLHKsxrBkRQPDHi7yOVbFXsWh75nyZYmFheQ8aFeR8yQBGikNKBb6iZvFR_DIqwXUpxJYts-UxQTIluUKWyaobGMVIMsvgwrP27i0c-Gs1uqAagvLMWjSsoSlTwWxUs4WpoE3X2OmN3VDs8-dVX--wi9aA1oSfYrq4IOQCqYCsfgxv1EGxBOhHU24mv5A60rGugaxcLmF82U1oTXpWNWyWSSIe0trKkYBa7EdV6EAC4cRKNnKayOIyul8akFDLPRCu-CPQIBJb8_QaOMg4FDq8rqFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139607" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139606" target="_blank">📅 22:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139605" target="_blank">📅 22:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=s3nxav7dJ4Pcav4aFWkDdY7P4cDrL5Mq0P-Uc2NHffPWn-6b2Aw6tPkKgN-WCQUZ5A56Q3ITOwaRu-QrYNnwB1ixEzPpVIg84HTolP6lhyxyra9We3YeTFm5pnR8QsOxBmJH1f5rxS-JC1OpPfdJ1IbXXjsrJB-UTcK9G_SvjOq-G_PPX-QgS79NWj6LmdSvPxefFwgvu6V3qmJKseaxUX99xMT0Zzbz0zYOi2dM_xxNb3Fbo0KiLUiQ7kzeTipvjrfR5G-RxOPBz-novxg_UPRMR8Xn3K7mzh-cVhrv4EIDbwZhOj9wFgL_xWpBL7JeY1pvlLWjQBqHJaMt55_xbZsdV5ivO0P_XmAI8GB7nJDLLegsbKk7WlmAKfgUJsZXlhCZsERvsoWJdwRhH5YgJ1Pe0juiyxZJ9piDwVHi37CIwNDoVyjxILk4HVlKQO85qnA4-vjHea6I7mcvODjA3wm9xY5_uY0b9Zm21U-D6EGem4F_NyNUxiOcd-ntly6yFzq2zzIZFm1xxA8JtO9PMSsePcV2F89MZpNpRTNaSYbdnu2cZ3-mE8B2Y-W_4lQ_wrMqZn6yzUQ5iCXtk62KmDJZOXgX_UCy1M3AzmygeGJFnk-sBA9XKcgMuCKHiuXC-xM9A1drQ7la1zEvmd95kLeghVvoR4I0cRNFAgOP918" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=s3nxav7dJ4Pcav4aFWkDdY7P4cDrL5Mq0P-Uc2NHffPWn-6b2Aw6tPkKgN-WCQUZ5A56Q3ITOwaRu-QrYNnwB1ixEzPpVIg84HTolP6lhyxyra9We3YeTFm5pnR8QsOxBmJH1f5rxS-JC1OpPfdJ1IbXXjsrJB-UTcK9G_SvjOq-G_PPX-QgS79NWj6LmdSvPxefFwgvu6V3qmJKseaxUX99xMT0Zzbz0zYOi2dM_xxNb3Fbo0KiLUiQ7kzeTipvjrfR5G-RxOPBz-novxg_UPRMR8Xn3K7mzh-cVhrv4EIDbwZhOj9wFgL_xWpBL7JeY1pvlLWjQBqHJaMt55_xbZsdV5ivO0P_XmAI8GB7nJDLLegsbKk7WlmAKfgUJsZXlhCZsERvsoWJdwRhH5YgJ1Pe0juiyxZJ9piDwVHi37CIwNDoVyjxILk4HVlKQO85qnA4-vjHea6I7mcvODjA3wm9xY5_uY0b9Zm21U-D6EGem4F_NyNUxiOcd-ntly6yFzq2zzIZFm1xxA8JtO9PMSsePcV2F89MZpNpRTNaSYbdnu2cZ3-mE8B2Y-W_4lQ_wrMqZn6yzUQ5iCXtk62KmDJZOXgX_UCy1M3AzmygeGJFnk-sBA9XKcgMuCKHiuXC-xM9A1drQ7la1zEvmd95kLeghVvoR4I0cRNFAgOP918" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139604" target="_blank">📅 22:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139603" target="_blank">📅 21:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139602" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=dXBT_w-jAaKFpHDRsp5dbubT7h2YSrjVZiaBUZeXv5Lw3i1pdr8N6ha846RFGHnpYv0N5xZcmfj-c3LGH4jyEM4v3iNOflExpYs7ce5RkECISAnwRvRTvpwqIXoM3B78WNhWVzBnQheawZmYMWOv6CA-bOsAxKj48Aus-axDn74cez95oa3NFaZ5yVZp6sr4WrE0X5YvSwH4m6UoO-2WetcoFMRSMVuPGaAizcLRx06DB8bxR2IX3jUEI1fsqNtB3dOuhEsLuxC9mHLGb_Nu99BCrHtMx55d2BBKa_CtxT7HT-eZ3NUKwmvHxKeszPnIPufhroW_TrIyTviPnWFkkzLaGiz2jrM87eK5pxkkRbFNbuPE-T2goa2KTL3PX12kQRKpepDiTxfU8XpDEaamGDnEYmK0Zuc_sU8M-SrUGMPyr-_jJwBe8lck4XMX4hfBOTWYRf2Hd7vyAihM7uf8AN5L-tVOlhDvFXGMViWvSL0fuZItmlvEfcmIJMGSe9W9I1hkJGxtvIu2YmYZywDkMfY4tvH3KG3CbWQYK61wt_s_ozmrxqBCFc4pnAXf02EVMb0kLL6ziTf_dkVpq4-FZgQFXb_oXFSmEePeBwg-m1Jt_cSCCUB5GRBZkA4fRmPnkBNrogvBZ5_ccc6PpRrMZfcojxycyZlX_qPvERHquvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=dXBT_w-jAaKFpHDRsp5dbubT7h2YSrjVZiaBUZeXv5Lw3i1pdr8N6ha846RFGHnpYv0N5xZcmfj-c3LGH4jyEM4v3iNOflExpYs7ce5RkECISAnwRvRTvpwqIXoM3B78WNhWVzBnQheawZmYMWOv6CA-bOsAxKj48Aus-axDn74cez95oa3NFaZ5yVZp6sr4WrE0X5YvSwH4m6UoO-2WetcoFMRSMVuPGaAizcLRx06DB8bxR2IX3jUEI1fsqNtB3dOuhEsLuxC9mHLGb_Nu99BCrHtMx55d2BBKa_CtxT7HT-eZ3NUKwmvHxKeszPnIPufhroW_TrIyTviPnWFkkzLaGiz2jrM87eK5pxkkRbFNbuPE-T2goa2KTL3PX12kQRKpepDiTxfU8XpDEaamGDnEYmK0Zuc_sU8M-SrUGMPyr-_jJwBe8lck4XMX4hfBOTWYRf2Hd7vyAihM7uf8AN5L-tVOlhDvFXGMViWvSL0fuZItmlvEfcmIJMGSe9W9I1hkJGxtvIu2YmYZywDkMfY4tvH3KG3CbWQYK61wt_s_ozmrxqBCFc4pnAXf02EVMb0kLL6ziTf_dkVpq4-FZgQFXb_oXFSmEePeBwg-m1Jt_cSCCUB5GRBZkA4fRmPnkBNrogvBZ5_ccc6PpRrMZfcojxycyZlX_qPvERHquvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139601" target="_blank">📅 21:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139600">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139600" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139599" target="_blank">📅 21:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139597" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=uLvo4H946kkj83F4odEHpP2rl7xIqojcEQPhS4mlbJktpoYDXrI2UF7hDUqUEC-_CvoXEpP5v2JxgYHO4euO_bWNIyu6gPAy-noJlImNe0JLogQLYs6KYX6Y506YuiNZoL222CJnq6NWPIWLf4nq5flXKEW5w3YOFxcrRWlZaQtlbIZd5nW2dDIWIEHQ1IeMVf3l_QDJFqK5wuvq0kTOpgPKiFxR-V5UpFj39dhvResKD3gsg-ZzZjg5dTRXMwmJ8IUvtMiIwMcikYEYGECjqcYR_3WreaBaSzvQ6uszERqoitsZHqKyqyDlOcHzn-sLq_BJIc6rGNSBRYZBrvtJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=uLvo4H946kkj83F4odEHpP2rl7xIqojcEQPhS4mlbJktpoYDXrI2UF7hDUqUEC-_CvoXEpP5v2JxgYHO4euO_bWNIyu6gPAy-noJlImNe0JLogQLYs6KYX6Y506YuiNZoL222CJnq6NWPIWLf4nq5flXKEW5w3YOFxcrRWlZaQtlbIZd5nW2dDIWIEHQ1IeMVf3l_QDJFqK5wuvq0kTOpgPKiFxR-V5UpFj39dhvResKD3gsg-ZzZjg5dTRXMwmJ8IUvtMiIwMcikYEYGECjqcYR_3WreaBaSzvQ6uszERqoitsZHqKyqyDlOcHzn-sLq_BJIc6rGNSBRYZBrvtJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139596" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
با اعلام سهراب بختیاری زاده در نشست خبری پیش از بازی با آلومینیوم، صالح حردانی کاپیتان کیسه از این تیم اخراج شد و دیگر عضو این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139595" target="_blank">📅 20:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139594">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139594" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139593">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139593" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139592" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
سومین باخت متوالی رحمتی ...و  بعد از شش بازی همچنان گداوند گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139591" target="_blank">📅 20:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139590">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139590" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
✔️
و همچنان ادامه داره این سبک چکش ..یک هیچ یک هیچ بردن ..دفاع اتوبوسی و گلی نخوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139589" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139588" target="_blank">📅 20:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139587">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139587" target="_blank">📅 20:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
فدراسیون فوتبال هم از احتمال برگزار نشدن جام حذفی در فصل جاری خبر داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139586" target="_blank">📅 19:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=h4DyvJPLEJqQQ4ZtPg3aTzjPJxVz-1j4ecCm5N2z4uJXTz3mA1fLjE8XiK1LdiSmEgpnMdHrQ5fZr2uskdEIlLgWlWsdp0pEADyQH5dytD_-VFb2f14VdH3JdZZcnMZVwDmVs4dXAD_alJcZSKNNE2WVsTIWZ5TEKLWCdvXmxWIaQMe4_hQMLfzc3yikHXk8T_T9CFo7Bs1BH47cSxa8hoPCUK9rnEx5C690ndC-w_mLmPFLGwiA0NsDVADeGq9KsLoMOvpDAJyHxJiiAYfMsFlpUOlntWhV-3XhRrIeSDZcqz6HzrZBuMkgrG4CA8rbHEJHU6bl3uM37RTV4C4l6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=h4DyvJPLEJqQQ4ZtPg3aTzjPJxVz-1j4ecCm5N2z4uJXTz3mA1fLjE8XiK1LdiSmEgpnMdHrQ5fZr2uskdEIlLgWlWsdp0pEADyQH5dytD_-VFb2f14VdH3JdZZcnMZVwDmVs4dXAD_alJcZSKNNE2WVsTIWZ5TEKLWCdvXmxWIaQMe4_hQMLfzc3yikHXk8T_T9CFo7Bs1BH47cSxa8hoPCUK9rnEx5C690ndC-w_mLmPFLGwiA0NsDVADeGq9KsLoMOvpDAJyHxJiiAYfMsFlpUOlntWhV-3XhRrIeSDZcqz6HzrZBuMkgrG4CA8rbHEJHU6bl3uM37RTV4C4l6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139585" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139584" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
🖥️
وی ای ار داره چک میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139583" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139582" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139581">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139581" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139580" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست  مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139579" target="_blank">📅 16:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBhpYnn8sugJhJCwbeHa5DNtSyrmfEDHLoKAxz_izWNCBhTcJbg6EK3UGYex_4YL41PsGfzowxN7DhZDDDOhB2A4RpSV6yN2aMdFz1IVchcfmMkT_hpLeMUkxSkXiA3Dkf2VRnEtbe4x8grCCI0GA_tLeZY-3uAH5cMHRGvtEgCBC79JwSlWShGkJ3zp39fxMmPSvXzS1odVfptBlca4xJFkpa8x4Uas2oe9VXDq81p-a41UVN6TYgzlSHSpNgT15ldFVhjkebIHwtto-ECKQZFCyhDmv2R-CHF05vxyaY4VysMrOGMlF4T3-2xUUR1jxNdFvSQmGksCc_ybQrzzfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139578" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
✔️
روزگار خوشِ «مملی»!
❌
❌
محمد خدابنده‌لو بالاخره در این فصل به فرمی که هواداران پرسپولیس انتظار داشتند رسید؛ هافبک جوان تیم تارتار حالا تبدیل به یک مهره اثرگذار و مهم در ترکیب این تیم شده و روز گذشته هم در دربی ۱۰۷ فرصت داشت یا یک سوپرگل خودش را در قلب…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139577" target="_blank">📅 14:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdayXxzdGWRO9zt6WzNNoWS85i_AGdOIfTZYYY-d6F1JL263m0P6ZGIxnWAQVPHpFMhz0LonsK-Efcs6OOPDdatH9FYG_dZ8kBLn3tekYZ2PXKB_BFnZ5JHeIUTbJpvClLGYET1jvGO7XRzJTwLS8Y1sleiggj58mO_lFQb2A8YheyEVCzNCBIC9muh6FNeFSqzYmZQfxACtikSewJYd_bqrp6LBiyOHd4AAG_juebbG_wOjKwCLdr1Y4xYq2Cj7bcogIP_22Z0tSeiEp8qv_56yK5pjmCGqJ9Ec6lihz_Otx86JWYriWAwMtsLzwxGtXx06B3cuMIKAgpszyEqT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کنعانی‌زادگان به ۱۱ دربی بدون شکست رسید؛ اما رکورد همچنان دست عالیشاهه با ۱۸ دربی بدون باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139576" target="_blank">📅 14:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139575" target="_blank">📅 13:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdbyM1DiOrU_1f-anUv3Go8_26xawSiQTPL2Uw53Jas-UUjIIkBqZPe8mVUStt0SSWRgBQBv61A9ZsyHv1EFykaFuVrlkiCPVE88TZaLvliatTnEdL8NeJ_zwY8FHQvi4hYf_vH1ywS0PX43xoXiJDt16jLhr6RKOjHFMkEc0Qw5CM0QXTp2NlE6kBtzGoiGtCjWGmSPVo7BxIMCs-d_7hOYPq4jbBOaZkBAjXbz5JxfHy11LxQM28rnWpD_nBfaJO8v0bIo2DYGJYxE0pOFIj_rYgZcS8u_uzP4pgtDm0c0rBW4Wy4fRdRbrV5pV9FUa-i8Up1RXIR6wKy3dG58jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139574" target="_blank">📅 13:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCNUN_v4fi_fhUJ1xEWOcPqkosU5mhN_pWaiGkyfhlYh0zgaBgqbiajIAS6RESgTdefKUVFKuQf--XTSFAOH4QnTxU8yoCeHTotWcAF3KZrhyOws6QC9xNtMvSmu1YrPBPMlG0DvS7qqkitH6XEFS5Q8X5H6blKsuiksSoo_ufKDQ8OP9k0QXUJbyTPDnYdcqmljLwUFuGUparNt0KPyMib1ewgBoI7vnH00z-_fBN7iemofR_VvXvcoe55uuWzqK2QRNQc-ZanVkWY0fC3Es_hE32KI_Y2dWaAvlGBcmZFKTILNj-rW2HORf5bUsytDglv1bqRoxFziuGk991CKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیس از سوی کمیته انضباطی ۱۵۰ میلیون جریمه برای استفاده از مواد آتش‌زا و سر دادن شعار علیه بازیکنان حریف و ورود تماشاگر به زمین در بازی با ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139573" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
احتمالا در بازی با ذوب آهن بیفوما زوج علیپور خواهد بود و وینگر چپ پرسپولیس تغییر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139572" target="_blank">📅 10:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139571">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139571" target="_blank">📅 10:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم در واکنش به صحبتهای قلعه نوعی که گفته از خودگذشتگی کردم اومدم تیم ملی تیتر زده که آقای قلعه نوعی میتونه دیگه ایثار نکنه و از تیم ملی بره و برگرده لیگ برتر همونجایی که تو ۱۰ سال گذشته هیچ افتخاری کسب نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139570" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139569" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV3C0_d79SiLyXxJEwNaIZVXO_Y3nbRTLzPQMYwjxjg3Aegdr8fhGlM1XvaOfTVxhGTjeAjrmxg0EjoqKdbOzCPg1wsNjoZoVKA9qhacSFtOALOX2TfeaZIaxbFoOmCXbL2h5Xw_tHP6AszFVKD65o76jjbpAaOz7NC7NreZi34VPK_DGh3Cd4X_1JJOsLUCQt4QK8LFSyQRn9XVEONz8W_LWKbCJUuhkKgNkc1RTPzJ8mOxY4uZfYCK1p8aIDm-EcKf6Y8Ho2Y6T3eXRowYHhFmRWxjqypFy6sMNtfW2k-8p5ddCs0MkBTTQvzjrGa7g9uJTg85-B59mFmJ4aaCsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139568" target="_blank">📅 08:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERXO6ruqP20mfJsel0g49YLcHkn24Me-FTTH6uhtHPb5VeAyod4SCJNJ1ke7x7BoDKDqGJiRFKuF-zwbDrg8427gTIlfrvqT3kheVpedHJvCnb9iqd_4k5CjE6kaa6yeI7EDiHCui9LLxww12zUn_Rq-2EbSk3j_MXaDtJ5sfTXlYQKR7gmO1HkjtO1QBuUGrahI_7wgD5UZA1LtTmUG6XcuHsrwaDSqBgPriXCQ56EaCAX16zWBTioJKCe9_AgIt4M3F1OPH0iQo-zAGLcp_F5v4voH1W4xeOIygyar3z_0fw_vExYAoJGa82t8HEhKfT0sxpGREJ0Ka1_JIQxxtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139567" target="_blank">📅 02:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139566">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139564" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=KXYUlBxJ2r-fhlM862Qk1dVwaH3b6ed13s_EdwUrLdc4KTRXr3udIZzKI4b20tBYALp-VSK8mgddqf6NRyrc8dgcROSSQsAD7cm_LDrHkwozB28iA8co-RUnM-7dP9jAXEzRf3CPNgs0QAs_3Mp2EpIlIu-hke6idy3RF0mdpJgToJ9DM71G09CuQGDmsqmlPrIKp2f6tI9b6yWL-K-f5dm3gqe_BheuSJrwBdLYL9l2YVGXtLZfrrpwbeV-_VTdRnxsfd9qmdLZ-eJ4ADRz_nheAPp2lWZlRp5Ep6awwM7j2Hy-HJ3iiJWsVaHltVbV9swAeHAFdrkFR8R_Yiwing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=KXYUlBxJ2r-fhlM862Qk1dVwaH3b6ed13s_EdwUrLdc4KTRXr3udIZzKI4b20tBYALp-VSK8mgddqf6NRyrc8dgcROSSQsAD7cm_LDrHkwozB28iA8co-RUnM-7dP9jAXEzRf3CPNgs0QAs_3Mp2EpIlIu-hke6idy3RF0mdpJgToJ9DM71G09CuQGDmsqmlPrIKp2f6tI9b6yWL-K-f5dm3gqe_BheuSJrwBdLYL9l2YVGXtLZfrrpwbeV-_VTdRnxsfd9qmdLZ-eJ4ADRz_nheAPp2lWZlRp5Ep6awwM7j2Hy-HJ3iiJWsVaHltVbV9swAeHAFdrkFR8R_Yiwing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139563" target="_blank">📅 00:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=sQO0-QsxuGzUzFeluQHzsj4MhKPdGGy8Wz38j30AaMPiP6IaIDMFg4kbY3TbQA_6neA3drizezRNzRfeOBeyZiVrs0gxAmBJ-HiOruv_C2sa01FvbQd2L0B17lboo14QKWrgu4UCFFrPgXM9vileHbsLQ_gVJc_Xtsi9kKh3lvAHIxmRfTdaWMdVR2pG1s5JkYQzVi85l0WBZCK5GRU-JKjfaj2oQHG0O1rUqSD0R0GzLbM1M254XhB6Q12d7VupHT496o_Tlw-sCf35zS2TegQqeXFc3txpVyzjc7ynBMZe7ER5PLuD_XuOSKl2oCDaXmU3wxXKN_4nxUH4dFLSrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36a4cce3e.mp4?token=sQO0-QsxuGzUzFeluQHzsj4MhKPdGGy8Wz38j30AaMPiP6IaIDMFg4kbY3TbQA_6neA3drizezRNzRfeOBeyZiVrs0gxAmBJ-HiOruv_C2sa01FvbQd2L0B17lboo14QKWrgu4UCFFrPgXM9vileHbsLQ_gVJc_Xtsi9kKh3lvAHIxmRfTdaWMdVR2pG1s5JkYQzVi85l0WBZCK5GRU-JKjfaj2oQHG0O1rUqSD0R0GzLbM1M254XhB6Q12d7VupHT496o_Tlw-sCf35zS2TegQqeXFc3txpVyzjc7ynBMZe7ER5PLuD_XuOSKl2oCDaXmU3wxXKN_4nxUH4dFLSrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139562" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139561">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=niOrVZJkdqtca0dDZWB8FetTzOaidHiY6KX_0xgFSTP26rP1QcO1ALoF0ogwj_gKDathqGjn46KX9B-bI_a6XZggbHaLmondBO8EysJP73602zetW28rJU4SxBopWpWNxKwMWX6y4iYEugr2fBxCwTzkCerz4cOG8W8QWfxfGyS2943aeYwmcBI8Alx7y9pLYSmqulBPJqTQEURt3S_XajLOJ80dLgoJ1upzysZRWU-SPF9nJNa1EEh_Q9NdZvof4vGzHKHVlatcY8yVg9XXp2rgxSDkqD3dR9VXO7O3KkJGWjj8bE6QKOjPFGp6ltY9aGhiSyQBNt5RReOMLD_z5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdba32ee42.mp4?token=niOrVZJkdqtca0dDZWB8FetTzOaidHiY6KX_0xgFSTP26rP1QcO1ALoF0ogwj_gKDathqGjn46KX9B-bI_a6XZggbHaLmondBO8EysJP73602zetW28rJU4SxBopWpWNxKwMWX6y4iYEugr2fBxCwTzkCerz4cOG8W8QWfxfGyS2943aeYwmcBI8Alx7y9pLYSmqulBPJqTQEURt3S_XajLOJ80dLgoJ1upzysZRWU-SPF9nJNa1EEh_Q9NdZvof4vGzHKHVlatcY8yVg9XXp2rgxSDkqD3dR9VXO7O3KkJGWjj8bE6QKOjPFGp6ltY9aGhiSyQBNt5RReOMLD_z5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139561" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139560" target="_blank">📅 22:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=vPqOyUM5AB5dehDffbH-FQdytBlPwWCMkJ9h5m-DQeDUIOLe6s7XO6PKynXQqypOI7uEklDWJuWA1XdQMAGG2Tym9ofDHm9Zw_ZFnK0ZbsP0K924ycwQSzEfhWIw4UiuhnmtkppgFEkkCBZpCsDVP72zGfcW41XtisFzYf8WauLMkCvZxykncbAoJLsPA0NvBmT77mPmudLm9Kh6fVinW3x6NIsuJAIA12H6QrFW_j-dHKodRgShRtv0LrHhFknPWT8nVd6MrrK1K8QygubwRiOyVMoXKJcWHwpi7DR_X1j7W9NG4un2r8_7Sr2iggsYXuyMGBXDBD2gwyonhHFtKk0mc0DJRUeeGvYoXdS8cdPYnJXAYRFnl-Ke4WR_ByZjfJcCv7s6yH80TVE1_8AoP_k3SZJpBpbfaYm_kTx693xhsYoX0hxFesZ98jLjDEP7FZwaeBwBUtp6FSpM5usZrGy1mzMbAB4J7vE_780lTam25h2ut3XzqaQfB5i0QrbozNYmb2chdMzkaBbF1GT7uLcMibOFwcoKB4iG2Ig0lwDjj4783i4zSWJ7SxOdGqOV-4oKNaaG5Ir8tU7O_FIt2SQImH2KQS2UN4_Eu6lcCaJevx0n5RKpqF_jxfeIbeQLkdJlIGfURtST8m1etv0RGfMRV9rC1dgrcv_vbkaW7lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f9d5f0dd.mp4?token=vPqOyUM5AB5dehDffbH-FQdytBlPwWCMkJ9h5m-DQeDUIOLe6s7XO6PKynXQqypOI7uEklDWJuWA1XdQMAGG2Tym9ofDHm9Zw_ZFnK0ZbsP0K924ycwQSzEfhWIw4UiuhnmtkppgFEkkCBZpCsDVP72zGfcW41XtisFzYf8WauLMkCvZxykncbAoJLsPA0NvBmT77mPmudLm9Kh6fVinW3x6NIsuJAIA12H6QrFW_j-dHKodRgShRtv0LrHhFknPWT8nVd6MrrK1K8QygubwRiOyVMoXKJcWHwpi7DR_X1j7W9NG4un2r8_7Sr2iggsYXuyMGBXDBD2gwyonhHFtKk0mc0DJRUeeGvYoXdS8cdPYnJXAYRFnl-Ke4WR_ByZjfJcCv7s6yH80TVE1_8AoP_k3SZJpBpbfaYm_kTx693xhsYoX0hxFesZ98jLjDEP7FZwaeBwBUtp6FSpM5usZrGy1mzMbAB4J7vE_780lTam25h2ut3XzqaQfB5i0QrbozNYmb2chdMzkaBbF1GT7uLcMibOFwcoKB4iG2Ig0lwDjj4783i4zSWJ7SxOdGqOV-4oKNaaG5Ir8tU7O_FIt2SQImH2KQS2UN4_Eu6lcCaJevx0n5RKpqF_jxfeIbeQLkdJlIGfURtST8m1etv0RGfMRV9rC1dgrcv_vbkaW7lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
⚽️
وحید فاضلی مربی پرسپولیس: میتواستیم بعد از گل عقب بکشیم و به راحتی برنده مسابقه شویم اما فلسفه تیم ما این بود که برای گل دوم و سوم تلاش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139559" target="_blank">📅 22:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
برخلاف شایعات هفته هفتم لیگ برتر کنسل نشده و قبل از فیفادی برگزار می‌شود.
✍️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139558" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139557" target="_blank">📅 22:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139556">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
✔️
کم بازی کردن اورونوف بخاطر ترس از مصدومیتش هست و داریم دنبال راهی میگردیم که نهایت بهره رو از این ستاره بگیریم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139556" target="_blank">📅 22:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139555">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139555" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139554">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139554" target="_blank">📅 22:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=f4UGiJDexhH4_oDspHI1l5-s1SCa7mKDOnpp5ICQ7Vn-buoZs_juWhIlZS1_kx6E2Jeq6iTg6K_yFUQ1DO3wiB5GPOAUUU3-dnoS_XhAbWpFpR9wlIWMvLmK3MLa9TGT5Sj2ffgB1T5n7I63JUeIIXZlsdtTVYoXrmD8oZIJB_OWS38vsaz2p03d08aT8SIcA9SRWVV-9kCJaPD2tNYGFV0KUjwMe45Zo-JzI_JFM049yPzgL8o3p6UpC3CR-s3hwDKbd8QwgpQFBJ4GZORLIFUVtiBCDxpwCDwaT2wB6HGdjj5bYRN6Bj0zsg3_8Qj8mKmHylSy1cq5kihpbQMeBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf52d5a19e.mp4?token=f4UGiJDexhH4_oDspHI1l5-s1SCa7mKDOnpp5ICQ7Vn-buoZs_juWhIlZS1_kx6E2Jeq6iTg6K_yFUQ1DO3wiB5GPOAUUU3-dnoS_XhAbWpFpR9wlIWMvLmK3MLa9TGT5Sj2ffgB1T5n7I63JUeIIXZlsdtTVYoXrmD8oZIJB_OWS38vsaz2p03d08aT8SIcA9SRWVV-9kCJaPD2tNYGFV0KUjwMe45Zo-JzI_JFM049yPzgL8o3p6UpC3CR-s3hwDKbd8QwgpQFBJ4GZORLIFUVtiBCDxpwCDwaT2wB6HGdjj5bYRN6Bj0zsg3_8Qj8mKmHylSy1cq5kihpbQMeBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139553" target="_blank">📅 22:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139552">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMv0JwM9TbLzIfhg9NvXyJv-bDT8-3DEULdxY_gECDMSoOSPT3tckY1BoX6Kqk_sYiMihnm7MbJavWgduj44GsJsbXSGM07zXvVYV0fJxMQUSyP5qApXiEyVNggS2hF2coCUPbn-UGoAaVEYSZVrwFe-u83xxwbwgc_NgYwHxYOM5B26pkyyXl0V_FnzqttuLe3cBzb10npIXaclHXIdAjb_LbeAOpVT_Ax5-EUr_0w8nv5Ru24xXhw-yscAG4wCrzzpSdxcFahdqEVH-XMDv-uGfNo0ckYEJ2J66PdpQyNY5IKKlWa-XKzRCvHphYGHDB0mL7sxazI709mV40_e0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139552" target="_blank">📅 21:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139551">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139551" target="_blank">📅 21:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139550">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWh7AsTLyWpftV0UtkJ_awY265qWKZnK5VCIxHQNfc6_9A0tYfQm68w-uik7LrrW37Bt8JVbjmKYQJGLkqKC81YRGj77pDv-ecniJLPu6tgOV74WspMzVzh5gpODRlZx23T7qGVOK3ugIjC4fslx7wTj62EFE6MObolWQ6b4Mbnu9myMS5cJ5kiuk9SwRKu-2chIdC02ibYKdYJvWYMO_JOt812Oo3qLMlZ2utznrAuHQdy05UW3ovA3-Ja0DpKwLZjag4qu83y0J_fNq4CArssWWp_vcqiv2eQb-nDv4ucCjNMS0Qz-oVy88Tz-msdvXeOjiLaaO4B8vRpPoTYm5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمجید ویژه پیوس از وینگر جوان پرسپولیس!
◀️
امیرحسین محمودی در دیدار مقابل مس رفسنجان آنقدر درخشان ظاهر شد که فرشاد پیوس، سرمربی مس، از کیفیت بالای او تمجید کرد و حتی از بازی نکردن این بازیکن جوان در پرسپولیس تعجب کرد
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139550" target="_blank">📅 21:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139549">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6yNy26MUnkgvSgcI1qbfwJ1N-HzmqkYRGgtvHANLE3iiG2w4V0pX5nrxDvhrl-jTKFXXdUAEk-hV4vLa0mnFx9udkRBtGhCR3JdwDfUSlVIWE3P1hjtdXfgnw8yKHfc6nMVVHRQS_ddOnfRhEbVb27V1owdKUyklwNT9N3jO8jYvzbG802mbvVQY9h0N3rLLmP-MKSpVajwN2gckecAKNc4CGwmeKZR_FTMaP4JITMbexQUBYQ1Zv7nL6idY36JM3nNPz04gI3EPsbBcT0DVHVHYElqabCoWEevCqq3KK2QRSUpAOI2Spptk4h-RaBv9IniAvBUz7ZU4lctx6ll0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139549" target="_blank">📅 20:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139548">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139548" target="_blank">📅 20:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👀
❓
محمودی ۱۵ دقیقه هم بازی نکرده امسال… اقا تو پستش ترافیکه درست ولی نمیتونی هر بازی بهش ۲۰ دقیقه بازی بدی بازیکن روحیش از دست نره ؟! محمودی چند ساله دیگه عصای دست پرسپولیس میشه اگر آقایون نسوزونن بازیکن رو…فقط بازیکن هایی که از گل گهر آورده رو بازی میده اقا…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139547" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
با اعلام باشگاه پرسپولیس، آکو باتری اسپانسر جدید این تیم خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139546" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPqmVgHn5JLYewv18tztpQCiXIXLThWJoBjr4CTqPmGntnyhSIcBOOWJ8USWveqeXJLIIuXT8lyITu6LO2GjrV77rnKxVPHZyMau1PaFOgge1qWDvcDPcPtjz8dqZwh4msO8Ef_ffXO8KxWLLo9AccfBz21a_SuJA_yMvuRB9QDQnq5JoSRMbNcVOnwe3zUIHFex-WQuLub-66V8LB1ml7-gFoDcimuLlgr-63qwjYgcCkNU0-0DNqPVCbFLgQgHMrNCunePwt_Iy06Tq0Mj9ECtcu-qRHVSJ2mqGbequjQ6F8kyIUYjSezbEPZo6m8eonG23Ut1hDuMHagFuHmv6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139544" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139543" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139542" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚪️
⚪️
⚪️
فوتبالی: سهراب بختیاری‌زاده به حردانی، مهار اورونوف و بیفوما رو سپرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139540" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=eJu9igxTU1slWN1sXwWLIQ0DKblsd7pTHpkzPP9UzHk5yEHXdcO88FBGa8Ayc4_dJkWBXGnxn3vNcJfmUocjyxMQJHcNKzrr2mWf369zEXW-FOEwCU23OVkXJ-CIyasJuWB3v3lEK2TJymu9ogRKtTOdYRcFJHyRU2M37igQoYZDhC2aiqKiknM8latTY-V50Nbj6WZlaTqJ1v87TZblQ053V5ABcKL7oRFXV-m9nIthiKGDrPgMX5_O0FwyDfJd5bNV0l08IxU_jLfikrCOAn6o8FPzYZ3aSCyeDtfvTPew2cHk0MPTB3JdP9NI1RSQecfEC3nrZQwMDxcxORllAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=eJu9igxTU1slWN1sXwWLIQ0DKblsd7pTHpkzPP9UzHk5yEHXdcO88FBGa8Ayc4_dJkWBXGnxn3vNcJfmUocjyxMQJHcNKzrr2mWf369zEXW-FOEwCU23OVkXJ-CIyasJuWB3v3lEK2TJymu9ogRKtTOdYRcFJHyRU2M37igQoYZDhC2aiqKiknM8latTY-V50Nbj6WZlaTqJ1v87TZblQ053V5ABcKL7oRFXV-m9nIthiKGDrPgMX5_O0FwyDfJd5bNV0l08IxU_jLfikrCOAn6o8FPzYZ3aSCyeDtfvTPew2cHk0MPTB3JdP9NI1RSQecfEC3nrZQwMDxcxORllAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=FKRkzE68C9xUM-8ZYPnoDG8mC0tt_Qgvfw03UZQrG-sra_WBry7DhP07LaUVEMjjyZMu4saWGnY5v4W6lJNgF1vsrwf5yr3PbNbeCDGBcDo-Hs8PlsM8dc36l_-A3yDWPppm-8yfADjMmWzlnGXZ7MCalVY47wik0MUZfxSB5qPIwWcvWuYeGfgT3E9DW7eeEEhwjtL_hp-NTIB68zeFFqEyNAJVnnW20jdoEYeBaRKPxKupnlxsVn0dOqf1kuE_0MpeUnJSA0zXQmysBkj3dO_VfJ-1_4KO9ejA5xtIHwnGCyI97eG8SbThWAInyM5LPncoTnsw4odLr5eIFaKCaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=FKRkzE68C9xUM-8ZYPnoDG8mC0tt_Qgvfw03UZQrG-sra_WBry7DhP07LaUVEMjjyZMu4saWGnY5v4W6lJNgF1vsrwf5yr3PbNbeCDGBcDo-Hs8PlsM8dc36l_-A3yDWPppm-8yfADjMmWzlnGXZ7MCalVY47wik0MUZfxSB5qPIwWcvWuYeGfgT3E9DW7eeEEhwjtL_hp-NTIB68zeFFqEyNAJVnnW20jdoEYeBaRKPxKupnlxsVn0dOqf1kuE_0MpeUnJSA0zXQmysBkj3dO_VfJ-1_4KO9ejA5xtIHwnGCyI97eG8SbThWAInyM5LPncoTnsw4odLr5eIFaKCaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139532" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=i_rlX1pqa_yaneKjOeIsnOpVNKZ5IFpEi9sKkJhj-Nc1JU0dU88DhplOXmf7DHI0sNeK5b4qLHEYT7mLcBIoaA38ozA0NOrB8FZ5RT9geydlUiOFLuh3UFkjpBuT7vnkn8_8nJWaKlVFBGdMa3UEcIdbksxsU9S1f7WT50hpHWREg3Ib6yVGCPoj-rspZU_KoJhf4XCkjQIB18SjpiV4hKs6A9JWXRXRNjiBmRv2cluq9VeEBlMR4i3by8YG3vAEsIuOjF5XyPvYUvXTQ1ZfGcHhizO77i9Mxiz80-RFtoCQTgHUM4bpQYn3R1ZukuzGUIFkzdH9_jbmKycu65ZxWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=i_rlX1pqa_yaneKjOeIsnOpVNKZ5IFpEi9sKkJhj-Nc1JU0dU88DhplOXmf7DHI0sNeK5b4qLHEYT7mLcBIoaA38ozA0NOrB8FZ5RT9geydlUiOFLuh3UFkjpBuT7vnkn8_8nJWaKlVFBGdMa3UEcIdbksxsU9S1f7WT50hpHWREg3Ib6yVGCPoj-rspZU_KoJhf4XCkjQIB18SjpiV4hKs6A9JWXRXRNjiBmRv2cluq9VeEBlMR4i3by8YG3vAEsIuOjF5XyPvYUvXTQ1ZfGcHhizO77i9Mxiz80-RFtoCQTgHUM4bpQYn3R1ZukuzGUIFkzdH9_jbmKycu65ZxWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139531" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139530" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
شنیده میشه که همکاری یحیی گل محمدی با باشگاه دهوک عراق به زودی به پایان خواهد رسید و این مربی به زودی به لیگ ایران باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139529" target="_blank">📅 12:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
فرصت به ستاره خاموش سرخپوشان نیز خواهد رسید؟!
✔️
✔️
مهدی تارتار قصد دارد بصورت چرخشی از بازیکنان جوان خود در ترکیب تیمش استفاده کند و در هفته‌های اخیر شاهد بازی کردن بازیکنانی همچو سلمانی و لطیفی‌فر در پست خط هافبک سرخپوشان بودیم.
✔️
✔️
حالا بنظر میرسد…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139528" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
پافوس قبرس با هدایت ریکاردو ساپینتو از پلی‌آف لیگ اروپا حذف شد و راهی پلی‌آف لیگ کنفرانس اروپا شد. تیم ویتبسک بلاروس هم که میلاد محمدی را در اختیار دارد، از لیگ کنفرانس حذف شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139527" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: هوادارا فقط میگن چرا اورونوف بازی نمیکنه؟ خب وقتی بیفوما در آماده ترین ورژن ممکن هست چرا اوستون بازی کنه؟ بیفوما خیلی خوب بازی کرده و حق دارد فیکس باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139526" target="_blank">📅 11:58 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
