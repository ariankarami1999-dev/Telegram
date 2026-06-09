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
<img src="https://cdn5.telesco.pe/file/OZ0kO7YCOaPhZVJM_qAYITFKP-GQ9UlfiMZcIVc_7r0_QuK1_2pIqB99mHEcVlFPCmFIXPEloULgymVVa238xJETU1OrUXKYP13cGRcqu23592m5HkSwGE7x3IMWhoRoy8TJqSSae24QcxJ2dSX6rK2-BG6ZIPZOUEf4A9edlz-ju4KUTkydvvuFEgeskiETUcQYAoloZhWz-f6lKruLI04oU6SFSQassomQRIMXDwrv5B-wTg5o16Y8WdU7HLSUqTWTxw_Wwuj9YvgVR-sdR3pvVIwuwNSnEMPtApcomS4RdFDD7gGVCwpNreLjj8WGu9aoiUSJY5YOQI5UxSsWuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 304K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الان توییت میزنه و میگه: جنگنده‌های فوق العاده زیبای ما در راه ایران بودن که فیلد مارشال عاصم منیر بهم زنگ زد و به همراه چندین رهبر کشورهای عربی ازم تقاضا کردن که حمله به ایران رو متوقف کنم و اجازه بدم تا توافقی صورت بگیره. منم قبول کردم و همین الان به خلبانانمون…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/91752" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=cWi2wTsEPPY1VIf6BRXk2OVgIQibUD-HnOtXqaLW6pv1UTix9jT-lM_C4VUjdbYGgrHfOg1DYuwCieSjGP3t7UPsj5e8mHzSpEpkcYiT7VSL7MVtLl2eK1PPVzyfazJL7mP_JTQgqWUcHcAp2OXfR7YXvRPi_aFvj4v4eBvuxhePpRQvOuUl44pcq2jyuYN3lg4sOkXYlasC_LwJRrDJ6_PkbMBWZxtN2IGTvjh1woKJR9d0jW3aK3HX7o3kzkzkuP1ssBV9y9m9Q2zP4SjaItyuBYnoW6C4Sps5VEzu51gzIuLK8wT1tUare8KXLj7eiWMsVtRzkyITR6HYwoxipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=cWi2wTsEPPY1VIf6BRXk2OVgIQibUD-HnOtXqaLW6pv1UTix9jT-lM_C4VUjdbYGgrHfOg1DYuwCieSjGP3t7UPsj5e8mHzSpEpkcYiT7VSL7MVtLl2eK1PPVzyfazJL7mP_JTQgqWUcHcAp2OXfR7YXvRPi_aFvj4v4eBvuxhePpRQvOuUl44pcq2jyuYN3lg4sOkXYlasC_LwJRrDJ6_PkbMBWZxtN2IGTvjh1woKJR9d0jW3aK3HX7o3kzkzkuP1ssBV9y9m9Q2zP4SjaItyuBYnoW6C4Sps5VEzu51gzIuLK8wT1tUare8KXLj7eiWMsVtRzkyITR6HYwoxipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/91751" target="_blank">📅 23:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=RlZBjAJKuL2Bux1HLcw548BVBherpNFOtigWR6fFPJQWVBi4gltRUIhYmQ_HJRF1FSN1DipaYN-9Eb9u4tuN950O83i_EsPvkCxVUwF7VH3HvR_Y-7a068P2twzyq0MmVP9OjeTmt4Tv35oaesvTECSOiILX7fSxKQqI_3zLJ3mO4NpDEazSZAM13i7eJ5xj0eqr0h0TeW_aDr1iRf6qhNaaXpLbZlsYNF1rTyRSgnQaDwhxbKTE9yXaqUeKvN38yOn3vywpG4ETBw-eXz_iQnmigEykIZdHwgMdMsurLFXzgbGTQj02-hASr7o7bn5tRHOsZCiIOGfQXVVqNl9RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=RlZBjAJKuL2Bux1HLcw548BVBherpNFOtigWR6fFPJQWVBi4gltRUIhYmQ_HJRF1FSN1DipaYN-9Eb9u4tuN950O83i_EsPvkCxVUwF7VH3HvR_Y-7a068P2twzyq0MmVP9OjeTmt4Tv35oaesvTECSOiILX7fSxKQqI_3zLJ3mO4NpDEazSZAM13i7eJ5xj0eqr0h0TeW_aDr1iRf6qhNaaXpLbZlsYNF1rTyRSgnQaDwhxbKTE9yXaqUeKvN38yOn3vywpG4ETBw-eXz_iQnmigEykIZdHwgMdMsurLFXzgbGTQj02-hASr7o7bn5tRHOsZCiIOGfQXVVqNl9RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🚨
🙂
سوال روز از رئالیا؛ دامفریس رو پرز فرو کرده به رئال‌مادرید یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/91750" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/91749" target="_blank">📅 23:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cUM30ZKtVLdmiunf8Q-n3E2MXmMnFqzYVSOgwKqrAef-VTAtI7tvosnXr00vTJgXQ1U9g1VTuBuBKjaNx1p9lwzxVQJj9eAEFwo6946Xppnq3E0G6oiN8Foy4SfavCFXBiHYGDShZ_gTHLwdxhbxsNeaY4z9Z-52WmBXe9dYnTWdVPJfCXS5NgyYVswC9W5cBIK4YzHGUnwfIvl4Qy5a6RB4HxONB3YsXUJqjyAabA7utQLRkgvcBh6KUUmW1rLZKvjW8a4xUO418_yHXeu7rlvpA1JANQ19uC9k_imky-irR8xy-qvOUO0PD9Q2h-6e2eQGoCFZs8XFU4vwHT8zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
۵۰ بازیکن برتر جام جهانی ۲۰۲۶ از دید ESPN
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/91748" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXLMrBk98tU303dm0C_fLuo53tRHs-kXm18ZcVIsYCjDvaB46jALW4b0OJfoHK5v6NO6lBG4bI9nsm8olmflQ71YqjISN8XOJm4pvGiodcrDcEmC_nPd-ijNzxMrDl-DYd9WjhVYOru9NDVzIyU8rVVEfNhebLdGZpEehOOa2rjaTjVDSGGOIlZr3hIPCElYUzwGRY-WAfYsHn2bHqrzBUpBUbeSUX8AtTjsbPYGI3_PvsVj36CNxgHxAdn38AB41ETNg6w_x1oYUzmMbeud7A6pnmk7b10Vp2g6c4kj5yNMLeL0lNQoUAqxnrgFCBNvw4JnLa5uDcFfJ4YUBR08sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💪
🇮🇷
🇺🇸
فضای پروازی ایران کلیر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91747" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
کیه‌لینی رسما رید به رئال :
⬅️
فکر میکنید اینکه رئال مادرید هر سال توی لیگ قهرمانان یا میرسه فینال یا جام رو میبره، فقط یه تصادفه؟ توی دنیای فوتبال همه میدونن قضیه چیه، ولی هیچکس نمیتونه درباره‌ش حرف بزنه.
⬅️
حتی اگه توی زمین همه کارها رو درست انجام بدی، وقتی طرف حسابت رئال مادریده، فقط با بازیکن‌هاش نمیجنگی؛ باید با یه قدرت نامرئی هم بجنگی. همه‌مون میدونیم وقتی داورها اون پیراهن سفید رو میبینن، دستشون چطور میلرزه و موقع سوت زدن چقدر تحت تأثیر قرار میگیرن.
⬅️
توی لیگ قهرمانان، بزرگ‌ترین رقیب شما یوونتوس، بایرن مونیخ یا بارسلونا نیست؛ بزرگ‌ترین رقیب‌تون نفوذ و لابی خیلی قدرتمند رئال مادریده که توی زمین روی داورها اثر میذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91746" target="_blank">📅 22:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
بیانیه باشگاه اتلتیکو مادرید:  - اون قسمت ویدئوی پاپ رو بریدین که می‌گفت طرفدار اتلتیکو هست!  - ادب و احترام رو با تشکر اشتباه گرفتین؛ برای اینکه سوءتفاهم نشه، هیچ تشکری هم ازتون نداریم.  - نه پیشنهادی برای خرید خولیان رو بررسی کردیم، نه اصلاً بهش فکر کردیم.…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91745" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqg9ncPNTWJ4oMY_qwa0Wvst1Rpx6V5r8hXKnSongtUS0UHju6vHr3Y47HWAMusR4mVdlGx7q7MR2QiOBFlBdg1-Y7TweRAQk1y13kdN26ib4lzebQ-NClgsiNkT_UhgoqFYONyHkrLPgRFkYJT0ZJTAVWM4Ve0EyE1_71ZV0W1_BWJjxWX8_V5xukfpUhQAhP3effV5hlRyappCO7m7qCI4zHVeoTRLkdur18y_Vooecg5RhDL2TM6_IHQkra-yoCkEpcurishRtnpRVPBMUao1BZxAW1ykjR6jqftbM_B8_89ufli9zcayF84a_ELZaBpCwe_w8u4U4yh8aRLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیانیه مجدد اتلتیکو مادرید:  «پی‌نوشت: با استفاده از رابطه خوب با رئیس جدیدتان، بیایید ببینیم که آیا از «دزدیدن» بازیکنان از آکادمی ما دست برمی‌دارید یا نه. خیلی ممنون، رئال مادرید!»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91744" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
#فوری توییت اتلتیکومادرید:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91743" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LQ5q_PEpIz77sYlQuoMAv2JybnI5DD13NNh_OgMiTxBKIxnvQ7kTY2FbpRI1jV1RMv-4yiab1UrTZHBNBmcUrBKv9YXZ1wAQEkVgYpOEP3ACYTj3N0ychl43KUtw2T1f-HauYbg-Lgk5uXng0FSEPPWHV05SWpPJ55vHAGoKP36bdrlov2FuC5dfzJljvKytv5khZlH2DqQeT82agaau-XviBXPjoJjs5JL7LiLoUKGLY4eDREW9bZgLIC_UnlYdGEPeKbHMtpX_I08HewbGx19xjlQ2qx-0Qhvnrv44GYxNlSbLcHIbJlBejfIE7XUYVYEHIKm5As84Mm0rM4iKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91742" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adQPFJsfE5nsszSW_3rmNYurMl0bihsJge5i3o0jmjYosjv70AYCjG3okgKna8tcy0MikSTGFeD5TYLalkCiiSYT3WApPsxfwwELiTdv_0BHODA_WAW_ASpbEiwohkHK-aw37x503B3nlFdCFYhiIMy6V7ZJXKS43ApQdTOZXXE5ia04cFBk-DFb0KWr2zUxP_L_QpL_ijNrmQ7VEr9I1IeGUMFjdUDtuAzpusEl518VWYAoukYjoE35uUg7pjETQh-PvJZ_k82cRsmk1QV1mUKlK1oKtObJoCaJw4ntPrchcrEo_UhRMREljv2qwkPQ7cA5phyX-EGvAi30Nc-GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91741" target="_blank">📅 21:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NDnAF5rOV0Z1lR_IH_fXSGlQ50nzzqDQM3DIggX6IBc1oyhPCXhy3B6ANOqAmTn2rcELb51zK6-3mpFMxSgDYP0zz96AsUSINfP3saLocEeF1myPXWlWdM9A5dnBQ7v-xJ27kbF5SsNjl9Kgifq0Vem5SY2j0gXkNLxt7rKhXcF5hzyPMMZA4fReL6fecvB_f2enavYV4Uj4282je2t4rmxl68fFlC6p-48Jlr1vP9_Rwkjcf-X0zp7Mt03FdIVPXOxk-oEZjnNwUcFrRE0hH8dognKIJRZ2bUq0bJ4lwl4KaTntWuHlyQ-YplzvZ5MPtNxOiPl6ibk3wbK92s7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
روزنامه Ser:
در بارسلونا تأیید می‌کنند که مدتی است می‌دانستند رئال مادرید این اقدام را در مورد جولیان آلوارز انجام خواهد داد و این پیشنهاد رد خواهد شد.
و معتقدند که این موضوع تأیید می‌کند فلورنتینو پرز بیشتر مشغول آن چیزی است که بارسلونا ممکن است در بازار نقل و انتقالات انجام دهد تا تمرکز بر تقویت تیم خود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91740" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91739" target="_blank">📅 21:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91738" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
بیانیه جدید رئال‌مادرید بعد سه هفته: با نهایت احترام اعلام می‌کنیم که قرارداد آربلوآ به عنوان سرمربی به پایان رسیده و‌ از تیم جدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91737" target="_blank">📅 21:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تو تاریخ‌فوتبال بین باشگاه‌های بزرگ هیچ تیمی روز اول ارائه پیشنهاد بیانیه نداده که پیشنهادم رد شد و تمام. پرز با این حرکتش هم یه ذره میخواست رئالیا رو آروم کنه هم کیر سفتی حواله بارسا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91736" target="_blank">📅 21:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXZo6JGkfwlMVH5LI0t0GLsOU6iGfCfLdaohJ_lwDWt_4QiApD2wXbbOtKeufFWrvrUNnake6Z1oWHbgLxLCF4DH0mRvly4PwZfXiqk_hWltyP0b2UqRQYB_aHXHMR9qLTfqGRYVdAFvRJDGQYe1MM6TiqGrmhSR-O_KnG7Tle8O3FeVhiUvzM_BOOmDJegNoWviYHdAJ1J8EPfohCNPPdtbfKcDVbGI_tkw0ASXseuXcIqL-ZPz6dwyVXqTNwPzEjQq26JFUtdfPkNvX6C8_EsHDc_Y9yyhNfsvy3nqMGAYNhXhnrZvWcBc6P5HMxlE06RUKYBErNq19gKlPr57TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: نظرت راجب مسی؟ امیدوارم اونقدری بازی کنه که نخوایم به بازنشسته شدنش فکر کنیم و‌ بابتش اشک بریزیم
وقتی به کمپ نو می‌رفتم تا مسی را بازی کند ببینم، چیزی بود که شاید مردم به درستی قدرش را نمی‌دانستند، و آن این بود که در هر بازی که می‌رفتی تا او را تماشا کنی، بازیکنی بود که باعث می‌شد از جای خود بلند شوی.
همیشه عالی است که هر بازیکنی گل‌های زیادی بزند و پاس گل‌های فراوانی بدهد، اما کاری که لئو انجام می‌داد بسیار دشوار بود، و آن این بود که در هر بازی چیزهایی به عنوان یک بازیکن منحصر به فرد ارائه می‌داد.
فکر می‌کنم مردم وقتی او بازنشسته شود این را درک خواهند کرد، و این چیزی است که آرزو دارم هرگز اتفاق نیفتد، این چیز باور نکردنی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91735" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ولی عجب کی,ری زد پرز به رئالی های که بهش رأی دادن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91734" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91733" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییییی :   اولیسه ، وتینیا ، نوس ، پدری هر کدوم با ۱۵۰میلیون یورو به رئال مادرید پیوستند
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91732" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇪🇸
#فووووری؛ اتلتیکومادرید اعلام کرد که فروش آلوارز در گرو پرداخت ۵۰۰ میلیون یورو از سوی باشگاه خریدار هست. در غیر اینصورت زنگ نزنید مزاحم نشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91731" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91730" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇺🇿
#فوووووری
؛ ماشاریپوف بازیکن استقلال بدلیل مصدومیت جام‌جهانی رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91729" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91728" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw3CqJb3g_VO4oIYzRHkgkjphRmHfHNo6wkZRUFmhaiOh2lDIQUzU8BnuaWvumgn1smIiSaq1bwslk6AkRYfuRn7bIVr68ReBKYDxPXir4zcJUgWle6amMtRRtDbL6th2ITmEScPFXLgxEx4XkDP4YFW6tyo6stHouUkPIdMpZ7ASeLLixjeoZOXHWFxNQXHFm9ldvWK9HbwRMfFTbZpUWu2Jbbe2vKSUoRIEtLRSH25EkbJ8DWFLA5U2Gm3jN2bGorVsG-Kx3rUxHdL81DCu5WSn2ZkNsgcZ-ukm5KuoT4Ub1xYHJBVWevXby0WENv8U3hjbuddyUXMlPpZrrgbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91727" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol29XM3-8cw09S0gOlE9YCuv3JXLQGZDpsLUtMoNAFGWJ_TlYaNM35X0AnEDeEJexQ9Zrfn7Z99Rw5PXRGjIX9SuqrhXt5tdlWo1H88BXDLUWu9gBEmTZxlzXrzTmifkyscKfzCSjAm43VpDM12-krMQldSlgM6ahdtQep0m5w4lewzr-lO2ogCEDSnQ6suMQfsVWN33tEc8R46kbXEveThLKGG9JaN0aY6rmla4EHgQu2OZwpyL8yvDkRjtv-Wp0Odeq56K3uvUzdQSiVtMtrPfoUOPXJUDADA6tBLYp-RacHO4xiSD0LHKQCao4-Mr8jhIZufWOqRcCpQLg_0XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری
؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91726" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvZFJd-gra8HQwOEB3QipviotTLIuNDlwV0H4ko6N1zDrZCl4lT26nX27WHGbXKG9TPvMCmkXCur1rUZoVweaRy9G1j9Phitl5tdEyovapTThC8AOHQBqF51ay1C-AtV_4B3BBxc5AKX4gdtqv5aNmaduVMYZD37-jl8Xenj9IKQMf0sygL9x5FGiTvbV2cUXs0hnmPB0giCOl8_1zCpKjBzrJrdyKfZrIV-W0Z70mNjxVWPL2Yh2awjesfG7459dkMGkTC788wXMdKSgALs_dvN2E7ANd_09kyDRSqK3ME8tzjQI5HCTGS7UBJ534oFxX9MqcU73D4p5CpRmG1o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو ناتالیا اکس نیمار
چه جواهریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91725" target="_blank">📅 20:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91724" target="_blank">📅 20:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5kjlJU8_fIZEEHGGa0TT-gmB_XjUgvh_n3BY4DbcTaAl8Xh5VtB_iLQ2eZ9-5TmiC33-maLFNe8mV92DXY49X3Rk1xOjZn9oYYz7wPXc0C5hGeA3-sBwnTqdeWHpbOemnU3Rj8Ns4Ik_ARzRqa6nucIAzrVsyVe5ufkRyW2JpKo-E3E2kio0VHdFIC2sm3s0EHq34rMvg4d959xzmqxFtwc0_5w0uC_r8ujjC9ZRz1I3A6zXrFFGDtKnX998tEGbSZc47aJ3-85Ge6eS19zqjNqYNfrvhbkok6_3QfTok2ZbWfNxfRT4ckM8WVoRfljA3wYhzU-8Qg8DxpkhrNz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:
«همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن.
دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91723" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgeExQTIDGEQH_g3LewxxiUssl51JXyh4tlC_l9RJAPIMsxUgmcpE-GvR6hrbgm0W2sfWoZGghAIgt_bTLPzEUQ5o0OO1BKyVc0yf1JzVSovC7HqI-avCVa6DE6E1mrO3osYQEJOMB-lilF_4aw6UkD9NkgJTyeox7y25qHhuTm2wQgPJPSuvhXrZx0aY_pC7aQrWdtEffco42JCcl89k2hgF4hmV4-j2yZ7IvHmojOv_5FZT0bBw-_d7pI_SO-_0gSt_S0Wi3xk7VCwZG0UaauZh4Z3jDkZ5lZWri2xQKWA8oed47Kbe47C1Bh7K5ggB9xwNgkmkZK93SSlc0QdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندها با بیشترین تیم در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91722" target="_blank">📅 20:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/itCNQ8gL7P-auI0udxrpdGTuKNGpZLBPehy4ukUg-Hcrj3TS5Y2yaOpaYs3onydo1aeFdk17fHw6M30x7d_2FcVKNte3hedSC9irjisoZRsK_t9ZAqLx9Gy_JoKckF_EW3trxKDL9CjQDDcyzJspcDrsCGwtoRLZ-h3FEJeYsvyWuLDQjJhR8sNU1JquIVi_jHQeYVurLCxpaITfL5qzZtrh9QIfIQAlyBBrX70J2DBBbUHyw5tTKEnSTag4IPyfEetypqQZtxBQePEnfyMqbfsyp0RLIA5mtd9HXhJnqTdV6rRsPuTXTMlPZQy8xPOk2b0lWENC92AObF7XH_2Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
فرناندو پولو خبرنگار موندو:
⭐
-
برناردو سیلوا هرگز اولویت بارسلونا نبوده. برناردو خودش رو به بارسلونا لینک کرد و گفته که رویای بازی در بارسلونا را دارد.
بارسلونا سیلوا را فرصتی در بازار می‌بیند اما بدون فشار یا عجله! مدیریت دوست ندارد بازیکن از نام بارسلونا برای بهبود سایر پیشنهادها استفاده کند، اما این به آن معنا نیست که او به بارسلونا نخواهد پیوست
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91721" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=AJaHQPkoRSwe8wAhoupnjE3pe-W7mp2PFzp_JbpeBNwNCFGV-JQzsEkGyfksmBaTfkFX18pukKU-uilcsK3zTcApYpXeOL6CE_qu6lWD5R5b--0Ba7I_mgR0o0YIbHYo5w1r2rX9DrldfOiMo5H9S3F5UyoXN6N5lEFgJ17C5wRZiELB9lsy-4kqbDXfsBVG5YZSvlmawTXDLlRPFfG1QiSF1C4CahWQ8BsDJMpc-d-6nKDpW4nkAkbiqpcHAb8XW8fcft038fFUF__sehq7fCxv3qTMvivGNL-qFL9J9s2cCIJ51Y5wYPVk__QaqPKtju5DhGwKBMAOjEX_G_7i6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=AJaHQPkoRSwe8wAhoupnjE3pe-W7mp2PFzp_JbpeBNwNCFGV-JQzsEkGyfksmBaTfkFX18pukKU-uilcsK3zTcApYpXeOL6CE_qu6lWD5R5b--0Ba7I_mgR0o0YIbHYo5w1r2rX9DrldfOiMo5H9S3F5UyoXN6N5lEFgJ17C5wRZiELB9lsy-4kqbDXfsBVG5YZSvlmawTXDLlRPFfG1QiSF1C4CahWQ8BsDJMpc-d-6nKDpW4nkAkbiqpcHAb8XW8fcft038fFUF__sehq7fCxv3qTMvivGNL-qFL9J9s2cCIJ51Y5wYPVk__QaqPKtju5DhGwKBMAOjEX_G_7i6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
این سوپرگل تر و تمیز رونالدو به عنوان بهترین گل فصل لیگ عربستان انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91720" target="_blank">📅 19:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
وزیر ورزش:
به فیفا اعلام کردم اگر تو ورزشگاه‌هایی که در جام جهانی بازی داریم پرچمی غیر از پرچم جمهوری اسلامی بیارن یا شعار علیه تیم‌ملی شریف ما بدن قطعا بازی رو متوقف میکنیم و از زمین خارج میشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91719" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTy1o1gKSap6KOtIkDkYWpstzSgY_w_bAhZbvJWuyyLceBR3Euv0LgkNf7YXvdJOUkaa2aiwZGRfZsNBgnQNVRPAEdyQbQQ3eCXfQLuxGL35ugTdbxers2hax0IE4Z7C6KVjUYMoPjUiUTFpMhzCJjbXMJSOKNQo2NVE-55zmXjb2MSFGvdFyth2_4DToA-1w5sDko_EO0P9_0jZw-kZ0tJ74DZAu6lniJ4H4ZpVWirJQMcUVMP8APfnATnuaPLIC9VlhJ3dhk9gIzPQjSsEeZuUhvfZbm9KnWa_JNv24B8afyUVYqsouwXhTjYaXFPA6qMBvB6--ZhXtXcSJKngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم غنی شده که تو پات نداری داش دیبروینه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91718" target="_blank">📅 19:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
فوریییی
❤️
🇪🇸
یه خبرنگار نزدیک به اتلتیکو خبر زده آلمانی مدیر ورزشی اتلتیکو به دکو گفته از جذب سیلوا کنار بکشید تا ما آلوارز رو با ۱۲۰ میلیون بهتون بفروشیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91717" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PenFtPvUyRB6rlI48eTpIFURySt2LPbsz1eWQPxwBIhchx5K1pU1OclPzOSO7Vkr5_rDdcSuHXsotsD13cD_3suFAU9aPLKapLlYxmuslfhg0LqITBP4PB42E15QGach-cK7OWBsQXVAm2S_pYR-Wq9GOltvqLg_UCs8Kl6qbdPP7PPRL_uu_n-XhZpIypIn13fAyKK7BHWQJu71A4Mz228RJJ3FsKZYDPPC6VHVeKmFItGmq1lJgmikj_UDRY2eaUrQW6rKNks32vzfL-QlwLro4ACxdFKrWcxEEHx1A-D1MySuyHUjVO57UMVjzl_PNM6LJV7AGtMhr7gQiLZ5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgUxyv85noRDZEZ1hB0XZp-GB2XL9x-MBUxWu9Mp0B6Fn_-NXaSUST9cWAefj2PYqkgfdFtp-rx7FIdQZQEHgux1lAs_MEEY5PJ1dZLGMMm-Tykb4oqbk19BObbrZA5W8x54EcH16Tc3YA9CNSmiPNJ9H5d0TOVe2VFKpWv2oru5E8rTDbwYVa932WQnmqclZMXAx4-AWwRkbcthGezFiPtPdCo6tr4GpwGCqpl18reD5vf3gZ50l9k4m2jCOQuVl1nGl_SFNLUKx4A75cLKLiGKVywCm0a68O48VuUUcXRob3jgzNlCohN728RajF6SqmL7TkYrt5Fu2U9WcbMcjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😀
🏆
- ورزشگاه مونتری (Monterrey Stadium):
مکان: مونتری، ایالت نوئوو لئون
افتتاح: 2015
ظرفیت: حدود 53.500 هزار نفر
🗣
با منظره کوه‌ها پشت جایگاه‌ها، به‌ویژه کوه Cerro de la Silla، که یکی از برجسته‌ترین طراحی‌های بصری در مسابقات است، شناخته می‌شود.
🗣
استادیومی بسیار مدرن در مقایسه با سایر استادیوم‌های جام جهانی (کمتر از ۱۵ سال پیش ساخته شده).
🔺
چهار بازی در جام جهانی میزبانی خواهد کرد (۳ بازی در مرحله گروهی و یک بازی در مرحله یک شانزدهم‌نهایی).
🔹
مهم‌ترین بازی‌هایی که در این ورزشگاه برگزار خواهد شد:
🇸🇪
سوئد × تونس
🇹🇳
🇹🇳
تونس × ژاپن
🇯🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91715" target="_blank">📅 19:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حالا فکر کنید روی بازوبند مشکی حاج‌صفی اگه به فرض محال که اجازه بدن، قرار باشه بازوبند رنگین کمونی ببندن. چه شبی بشه اون شب
😂
😴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91714" target="_blank">📅 19:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3648d1bt7mkzOTu2Km4FrGH_FGXfHI5Mk6Z2GcmGURad-rn6JcRPx6Z2zRvHsmmzDy-wSy_k-8lEJprSR2WlbXAg3vHHUakwGsG6fcjdSNzxImaHierPLu8BOkVAy7WFErgf-2IUK419PBjx_EsSNvuvCgZlK-lLVofPf4S5_RVgEUBT_SByA-57-2I4yhS7vIQfWdUKSsi-Wjc5Jt5akg4zmNw5J9Oa4PlfNHx9ZARXUKLp0OnpUvuUzF6qC2gK-IphDhCNKnN17etmzSXcw7-QLsNEk1FHQxs3yigumFTEGp7I3MLNzKvJa6w9_yT5cm9JlxMx6sSYOSJ5MAWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مسابقات افتتاحیه جام جهانی:
◉ بزرگترین پیروزی در بازی افتتاحیه:
🇷🇺
روسیه ۵-۰ عربستان
🇸🇦
(۲۰۱۸)
◉ بیشترین گل زده شده در بازی افتتاحیه:
🇩🇪
آلمان ۴-۲ کاستاریکا
🇨🇷
— ۶ گل(۲۰۰۶)
◉ معروف‌ترین شگفتی افتتاحیه:
🇨🇲
کامرون ۱-۰ آرژانتین
🇦🇷
(۱۹۹۰).
◉ از جام جهانی ۲۰۰۶ به بعد، کشور میزبان به طور رسمی بازی افتتاحیه را برگزار می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91713" target="_blank">📅 19:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcYCMDuMQmimkEUKiNFWHEGzLHYc9Kvo12oKwhWfmtsIfUGFC33a3J93clY57AL2BY2KEkRorPAo9Vn5F3JzE93Rv8eQFH9yxPWEbHxtqBM-aKnKO4cQAedeS7ThqadofAJOfwH7WZxTYAg2PaAD8fJTiDsMV34RX5Ib8OYiLg5RWuYTOXFMWEHXKD8FBcZAzQFE0K3Dl6WVackEBLwyFlJs-vYat_dE2i1yWGN6QE99nH38zj3mWqZBGH0OJP4YZmlaOvK9DClq7YisJC1vzQuXk2Z7DSmzoNwywWbpd-GpVdNn5cdZER6jpk1MC03cap9hnat8U-KqZkJK1KKO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
| آیا می‌دانید؟
👀
از جام جهانی ۱۹۳۸ تا جام جهانی ۲۰۲۲، تیمی که برزیل را حذف می‌کند، در سه تیم برتر مسابقات قرار می‌گیرد.
🤯
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91712" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYzOPOvYFX1Kx9nwhcTh2l_q2Zd1H4z2LLOYyoGj8alNQeSjukbO0OoVg9UC6NmD3q0MvOvQC4WEJiOlQFTi-x_tzDq5a21mcSm2N0-mSjZ3B0CLdDHfqfZ8nZlpFmO4Ki4PcAd7n5qhyuy-e_2A-yBtGqfAOyaJa1cXXJUrQ4c7JBSJmgQcd3SXRmdncl1l2kktzijeFeD97MIZXRl2oONl-XxWHjFXzhVH3j2kxonwFxvLm4obBSR8kKaILeUpS2RHFFzCzZqfjYFRWiWmkP5ZNdNUSCKGejJMxmIeNNZ_HaibG7OTKjDkqMlZWsiDmxYc_i9yndwDaHF9bOq82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی رسمی فیفا از جایزه بهترین بازیکن زمین جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91711" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqcMINlpeOOpkby8v_O9cdCe7qaxTL_oFs4of08ExyQOkBQt2RIR9bMjHtcDd9QWVv5tP5UC24CRPUyjeoLlUOcsQpqC60cVNZXFyfcbK7l48L5c0Vj5vUmAyB-gANt7C9FGKXxkW0wst5FaVsVseTY2M0ALJ5OIhPfBl1buW_m-M6v6KB7UOdy-5Y9XfBsFbaKTE5qRCqR_rupLBp1TrHts0pI0RHUbx9NxkJvy8y3o5U0FPZ1DORKxlfSOXnECBjy6DjnYycGcRyzUSxEs2gHnhhGlJ3h4-9nY98O5zVUhLxmJL5k8CFAZCCGE2piQJQ217phh_RIbKHSA7w82mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو :
🇪🇸
🇮🇹
یوونتوس خواهان جذب براهیم دیازه اما تمرکز بازیکن روی رئال مادرید مگه اینکه نظر باشگاه دربارش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/91710" target="_blank">📅 18:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJE5UmgIdCbBOXlbaRR0tuP8GCtEH_spAOMRVJavsRYy5jc1p3XMkNDnZrP9ouU-yuXr-1v-dkMNXPYyJKpd-gezQEVd3j-HfFQ6zI5Qt8JNRYiCN9m8JJa0hP-oa2TX3cIdOtftj4YI4AjPAp3PGz_ZdT2k_eIPY-F_jopoxKsRmjVXK2OZRx2fH8LiAE3XJcn4DeCVDp3Z8hPUnK4oipfu2gS-89E42BWFhjdVmTs1wPCb2Y8F-JbubNGGtPg-Fm3yXPo-LIPMTCXPI4BiM-6yC5SMK3Dw6DIWvDh31rXScJPsGw0p6glhTMAK2vAoDnKb_6NUbltwUFG8CGUd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6vuGVqjnt2GrcPyFSpF_1wIXc9ITXC-Z9ArZ8xuU_pzPn3G9rox_iJVAQ3kmqMRF-VmiE8L54BofSc-SlIpFIPeQuIjK3QHAVrBxp44lkN2q5JYFocDMiRsAK1POgDxKFoEgx95HBHPufJ6aasr-p6X-_gucocXEcV3lCMQBf8ca5oqkyyfDubJ3ZTK6GEcTZSBluNKNruPg-epyF8Ul2CvyiMohH3lMqfShdx8FOXfls2hziIhFQ7Kv8oH4_OPa6o-SIj3E7jIhPH2PIr-uYXXba5MkIKu5X0Ikk1uZq9vlm_6U39vfYCq-KK2CZMi2veN8nEZfyZRZGXWWNc4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/An_2pUkQeRblHAyI5adBc9ABOZEssIbt8pzbU4huOdyz-tYMLLXO2qIXUdan7KfDHdQjCVhoOYg3KoRrKno91zqpN315x0db4H7cr2GGnx97FSofxocFEabdzwIo_6___kPbNXOVeoi-OAswMxPNxaOe6DdQ-DbbLqXw7_s03UgC4MBQxYGVFFSDKplWslpmeKky4pKu8TV1mr0DBg4bSV3oFnw7iwi1QRfIeGQR4Mj3yDWehhmIV3gv5vSJQ7zEZ6tnz4WqAcDTOHAGpZj69hhCllR2nOObRKyc0-ekXqDts0L090UV9CFgq2EIQM2b4J1Tu8LOc4rbxaCRJM814g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دختره توی اونلی فنز فیلمای لختیشو میذاره بعد یه پسر برای قدردانی و تشکر از اینکه دختره باعث شده خود ارضاییش لذت بخش باشه یه BMW آخرین مدل براش خریده!
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/Futball180TV/91704" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=AHzskiuIprI4USxGvuaqsZqbnMi7DDRsT2aqLAeoI7Hwp4fhia4ekXpIEfzb831mYAFa_uiSMc5BbOu8gzgPEyjtzjAv0wxGna5FikYbVw2wi3hvk8OeFPEZNTJehL1MixPsnk2kyQVJ1kTmqzP1gqJ-4XL6LgjW7iGpQzMyrEkF_lVqCl82CBCTYedJ4BskboMUgK-pfy1bFDzj3kUvLQziQkhfQm1zW_6y6rFx3HUKYFZraLc5gM3F-DtKa6vg4dJNT1yqWRr1e4UMMj4V3Ubi5iGa_GWP4a-wKe9VX7F6GTkAe3PJx6LjauJogrNd6JMMzkNc8l0A5oKsWHqTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=AHzskiuIprI4USxGvuaqsZqbnMi7DDRsT2aqLAeoI7Hwp4fhia4ekXpIEfzb831mYAFa_uiSMc5BbOu8gzgPEyjtzjAv0wxGna5FikYbVw2wi3hvk8OeFPEZNTJehL1MixPsnk2kyQVJ1kTmqzP1gqJ-4XL6LgjW7iGpQzMyrEkF_lVqCl82CBCTYedJ4BskboMUgK-pfy1bFDzj3kUvLQziQkhfQm1zW_6y6rFx3HUKYFZraLc5gM3F-DtKa6vg4dJNT1yqWRr1e4UMMj4V3Ubi5iGa_GWP4a-wKe9VX7F6GTkAe3PJx6LjauJogrNd6JMMzkNc8l0A5oKsWHqTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
۸ سال گذر زمان و تفاوت از زمین‌تا آسمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/Futball180TV/91703" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4wu-OnAWMDXlqufqhNF00n35WHCqaRp-C97gcnYtW0O-257HpZlRglLUNUti2K_8jtErOvsD9AbOsykgQbqvhKm0er4p2sEZ28X1rB8cadQMkRzJaCC9373J1j1AHx8tKWUlFvr9QvxckYKuoL1k9n1btmDpB3TS3iJan1P52317eWVedGUDbp1cOqHNsiZfpdnmc6wlm8Hip7Wnq-N4A0IRN2Xufp88ju84AI8ZiLQs3lETVoEl2E-q_1lPkEc6ohinfxKn6RRBCznIt_2xfBLOR2XBnhmFvXGgvTAjofyWppvaJsxDIl-kLAsNQMWp4QIW11YcLFISoQf9G2g1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوریییی
از رومانو:
⚪️
🔵
نیکو پاز ترجیح میده به جای اینکه الان به رئال برگرده یک فصل دیگه هم در کومو بمونه!
تصمیم نهایی با ژوزه مورینیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91702" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtgQdtYLCwaJErx1119mk9nhaSfhmDWc1DQ1MTg5haD-eNGQgq0fpGQ_SLTpNLMTHelqnz53pGqVVsLGDarjQfUpYxRan229yqmj0EkMBSH7Q8O1xzzcL7PjHIdYqwOv13RUcMP8rNGs0MBfU3xPq7NY4Xp2N5vgRp3goQdaJOiZwbcGu5GTvdDR_Y_lznhPlzbC9kB0bN-Ce_x1oeQAdTyZauewLEf8CbYt7YPQMIZqJcGmpjprwCthz2WrdgjxY2Pqztb58qAUQCxYU_OpHJhDdu4cqA2Cby02jprtWslcd25dVy9yRvB6e_E4cCU8b9WPpGTxjK1Hy9AzaYRyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتواسپورت:
پاریسن ژرمن طی چند روز گذشته افتاده دنبال جذب لامین یامال و میخواد شانس خودش رو برای جذب وینگر بارسا امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91701" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8M9_a-Re0O9XDbnfZvNUVMlu3jWQDGPTSeTIK5PE3a3FHntSX4AgUARV4apofPgIAsP2pyEpvZyAl3FCkiW8mrvJrNzKWAtEGs6PXfVyQU4D9ObuGpOg03-dDdhAeD7S-mu3hysb8LXrzYbLyAWsB89-qXqagn4My55_NiVFWcKg-3QHNWHeSZBOGC0kFPGzpfJBMJ5abx79x2q0L0hsvuUSkdhAhdxCXQLA8DOwblEHDgv35kwTVZJ85gbo9q2Eqn-s1TPr60OY7S_TzAQApBTKYIyvEopFtbQed1tBEtu9CLivZtD0pb7W54mLNZhqmWqlNgO4ttHKWdyT6RIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91700" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=GmSgRqWp8jhfYAwoNuj5UpdkBz5rCPSwK1ZuRuRlZm70Bl1yA2PCQUu9o8bE_h3_l77xneVq60vvOCf5YWU-7OkpdqUjWZYy8eRKbakZVhZUX37uIYhFJZOeabjHyIIo0MVlzyD9BPofVskVMMNxi-wBQsj4plB0qXslJ0P2G-TlwY-HWTA724arozxy3byRbZHhiIgCRsFrG51YiZSzrRT_hb_VDqyZrKGrE-eoS6ZsaOjvSfI-F7TUh6DHxUq9Atd3DeSWZRJkZSZls6JJ4ncGNl8NfC6Tod2MGrxf8YzPSNAn2_CZG2Uva7CN6X7MktbSlmrZ_kG_WwCoaYAGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=GmSgRqWp8jhfYAwoNuj5UpdkBz5rCPSwK1ZuRuRlZm70Bl1yA2PCQUu9o8bE_h3_l77xneVq60vvOCf5YWU-7OkpdqUjWZYy8eRKbakZVhZUX37uIYhFJZOeabjHyIIo0MVlzyD9BPofVskVMMNxi-wBQsj4plB0qXslJ0P2G-TlwY-HWTA724arozxy3byRbZHhiIgCRsFrG51YiZSzrRT_hb_VDqyZrKGrE-eoS6ZsaOjvSfI-F7TUh6DHxUq9Atd3DeSWZRJkZSZls6JJ4ncGNl8NfC6Tod2MGrxf8YzPSNAn2_CZG2Uva7CN6X7MktbSlmrZ_kG_WwCoaYAGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تیم ملی نروژ برای جام جهانی به سبک وایکینگ‌ها
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91699" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9dyeHqB_GKfs9NwxQIiwp2YRVQOmqSxH4Su-Ju0kRHXf1YA_VnYmZnuE-4XNVDyW9SPU1ZRfg7xTKpZ6E0l5NrOlivt-dBapGpd6UlMQ--dJekRFzMUKT_IKY-sg3uFCH52Rz4Qp-zXYddBwEEJZrQd9myfFvvJh9VoXcdZXzfe04R-JidgRf0x4JEih-zILVCIv7MupJHI9w8FXyoTCRPgge2HmfzFuG5e5weECl0fJx5DxAvFofM7PzsSs10QB4JwXAd_eo2NVwpCxrzIwQIj0bWSX3sZUuuEMGMiG72fbALvvT07fveYwNnEGWPM1f3eAnvZn-ydgZGEEdvlvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmHeAskCCNQJPZ28qs8du10XasWEyT_N00-pa88QA4oNNJFu1cfSxib25QEIeQ3wQVS3napGhxxiTvXIOg21Aog4sFsjl_ON93Mq0q0j6VMLyRn-34NEeyiSUeWNPMi8RF9nmEveRZrIkPVpAanqzjwaiqYRdV2swwhxFZDZVgMqviJ2fTaM0Z1pPoLA1Pt_5zSwSCihf3qNVi2vd4L9bjYYh9MbuoM9XJwyUYT-3t7GZqWpv9Z4BBMU6iLtF9LKbsETOjIA-79Ie0T2z1bu9wmvAWNaycqzm9sqtvFRxqUj3_RunY14LE1Jjo8LW79aZ_ozVwi-z0wUuXZDJa0okA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Newcastle
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91697" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGyakcYs_iqF2Yz6tjAjl1i-rS5u-VSuIVn-VcxeiyyL2bPiunBPKO02eLSOKePr73teeRYhd97DZdVba5FkJAAKESu7gJL4aX44Y2YK8JBiXodRmJRbROpr4CI5N5wBt7nDUSsaoNTmVqIktQY_FB0DnkTVEEZaJuAdlAb0rJbz4TiTwwl5QrXPMMhkSDfUjymlmyaStI_4uyeE3tHFk81uHULIyzLthmVVHExPVQpjgyij7dWpe5rbxU1Kt06X1U48IMk2uIUlk9LMRFSIYrFHN32z_AW0dBWuhjU9kOscLY93IiBIUnEJ5ZRrYZW7jZYMxn_6aeDLIgCMW0fDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گلوبو: نیمار ممکن است مقابل مراکش به میدان برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91696" target="_blank">📅 17:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc3ct75_ftNgaUXh4a9ZmO1Kc6mjAwmYHQbs9eBUq4vRa-oip4CHluR7P21ZHKQjij-xVBuZXwcty79YkbkqZE-7XmZgrl-8ie_PEJBexOyraoJC0GGif9pBiuLIRk80fzMiruJ_YCVXX4QOA0ekN9WkjMI2D8vvG9sXlfomq0W3nBpPcyEuAEZwS_Pn0h97EPTY4CiNttplS9VY-YmqYGfqPe3n_fJaIVFtYCthdonSt2FUys-NAZopINmBes75xTV9rp-08xUI3rwVfxadrHLwcNly9Y_SiYXFuifusKqgDgAFV6LynS26XZS2yXqnSbi5nOYAsDQGuYvtWFd_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91695" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jY8SFNV-UibqR6rPQiLE0gBOLREdB2_1fTnbf2MjdYXrXW-QR55acfjc2UD9aXv7I2HnXSg2FVyYXT9L6gUPWpgAIqWwNwm2s_f2ZqIkcYACSN6jIuUJWnoh6UVAWNocBaYJrQVu7fpy13_49j95Ru9o03Xau7GyMaOF6_08NBQZYJg8s1kLZQ8IBiPEZKnt8N7roAuzawpW_oHhDBzW9w7vKFDNXHa5hNEGhBn5SSDIFa8sUsN1tu2KvQyrTdRNE0SOtNUSkY-vwvitublFE4XcPKduvFnK7P5M0SAm78avBVBHvP14UkCCi18PT6S2z-axPrFzUQ2FShffWp3-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
رومانو:
براهیم دیاز میخواهد در رئال مادرید بماند و برای جایگاهش سخت بجنگد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91694" target="_blank">📅 17:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp-REOOU7t8FX3b-bwd1wwxeP51_FgQxUiZsztwyWVq_AWHy-rH_ZQqyjbdHRmVXZ0A7Eqx0uHi-qtYYsdPuvHhQV_fQ9ANV2A2tEJG-dH2qLehNkJRaS3ac5L9JYSTucziF_OIjRSC-Lapu8dqdcnpbOquFYo_-o55clkpzN0vN5DDKrqh8g4ymyUUJtZUrIA0YxFqaDQhotZQ6WYowjcuE7pPwSap1tyibTmSi8KEdeCx5VN-Qrko25MBbG7cbSPFpYxk5j5x_4TvKxXGDvd55_8lVgtsL2MeYJFtze-SIL8VR6rqkHxzqn0EU2w4drXYQn6CwJD1X1wDDT1niUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYfXNifr4TunRmYHvDikRRGHHEwLdAF8A-eesclgd3nzbzcovaHqazDSQcOq6ptjqZ3F5OPe2SODkQ3N6fUE_rllpusDOoDitwrfoITSpiDekG_3rH4XLATHN5REc7S5d-UZUEPAIBskazB99Caeh0fBGOK5dC4gGwOj349pqexXy_doFrWCjcBjWXQVMMn6F4uS5Fd-P1A2gSFL73dWOHAviHGodpNSu4UgNfiKvpig8N0CuqdKv_el6CaMTdeWvTPxNcICLvdG8vTQtcUqAxaW1LInX_Qh443eynaZyJgvyFabSoTHXKBpPkYFL1x9yE_Mwms7H4pQw7t0Xc7xTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاینات پزشکی رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91692" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
#
فوری
؛ پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91691" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=gZJB5BIfFh-0pNsmD7S5cBXfB9UDcgGTqQfkncDTfzXdny9OfhUg4Om97Zv0f-H7mtaBlJ2LWAYaqgECyffVtngk_jP6lcVvWTuVm3AT2iwllnMtqBu6hizqtpHi6-E_Rj-X7YeefKefDhwGOPluBevjeNlOXxBsZRqIWA8WqTqGUU6z9PRtYltpYCDyTuG4DzXMfEanOiTbMfUII9iuOqWIYG6YfxvV9vPOZeXny5c0RDpOkxET0m0HQgh_5kE6hk93ukrjg-yHFjyLVoyGKHrh21IvQtEoB_i0dWwZjhwqSKkHDEFZMHZLNb7Dju2DPUCsjWASfGuKhpIjJk-kIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=gZJB5BIfFh-0pNsmD7S5cBXfB9UDcgGTqQfkncDTfzXdny9OfhUg4Om97Zv0f-H7mtaBlJ2LWAYaqgECyffVtngk_jP6lcVvWTuVm3AT2iwllnMtqBu6hizqtpHi6-E_Rj-X7YeefKefDhwGOPluBevjeNlOXxBsZRqIWA8WqTqGUU6z9PRtYltpYCDyTuG4DzXMfEanOiTbMfUII9iuOqWIYG6YfxvV9vPOZeXny5c0RDpOkxET0m0HQgh_5kE6hk93ukrjg-yHFjyLVoyGKHrh21IvQtEoB_i0dWwZjhwqSKkHDEFZMHZLNb7Dju2DPUCsjWASfGuKhpIjJk-kIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیروز وسط‌تمرین یوگا‌ کف تهرون و صدای پدافند؛ چه ترکیب متناقض و عجیبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91690" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=gHAwCIrnPIdXtACYCCJBmzPkFIqvka8PioPcctP0hqBIxXj9sWVH-DueRksjLA18DkdeE17z_j6hYD1AkK_0Vif1cGUtSY2ocABrJWEmMy9OkWbces8qRjmg7wx62swwILp5BdhnmrSX4fF8Ke4aGMLnrReEPYakeugl2LypU72IKkr8zBdT_Cncor7PtJKjQJgr31DfC5DXdtQQ-79PG5_-oL8KiPJP_hgTR5ZxnKRn9zUwdbcP9JIKj_MIYjwJzU1C4JO1vcTEv4wmbXokbFAaWK2AzeJzfLYSyEtPCv2figzjKFd5ZG4e5NFNVn1n5wbmKwfKow_g06pPHt8mrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=gHAwCIrnPIdXtACYCCJBmzPkFIqvka8PioPcctP0hqBIxXj9sWVH-DueRksjLA18DkdeE17z_j6hYD1AkK_0Vif1cGUtSY2ocABrJWEmMy9OkWbces8qRjmg7wx62swwILp5BdhnmrSX4fF8Ke4aGMLnrReEPYakeugl2LypU72IKkr8zBdT_Cncor7PtJKjQJgr31DfC5DXdtQQ-79PG5_-oL8KiPJP_hgTR5ZxnKRn9zUwdbcP9JIKj_MIYjwJzU1C4JO1vcTEv4wmbXokbFAaWK2AzeJzfLYSyEtPCv2figzjKFd5ZG4e5NFNVn1n5wbmKwfKow_g06pPHt8mrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ازبکستان روی سکوهای استادیوم یه‌ پسره اومد اینجوری از زیدش خاستگاری کرد که دختره کاسه کوزشو شکوند و جواب رد داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91689" target="_blank">📅 16:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=AquwbKSTQZQlOGUoyj0cA4dHrRXolHGierK0WQdFzRX_adFZsS6X__YOdyjDQtlreGNaTZuHjyY0OjWX8R71c18Ec2_fd7jP5ZvEhDxaHBmX1ZnCkayyHwgh8HYpv1AVHE3Yp2on6AI-YLffpIHu922x8f_HuA6ZTRdOJ-_-v77ha6PV2i0GM5FF7G4w78cVZBLfA-zmGcN0abOFkSRs3sqF9zEyfIzF_XE8xsNZNIKtX6rvGcJdreCxYKcSOlbyieoXGJEbbw3WU1XM7Iub8tolvlRe13Tzug9UR-NvKoIRmfHw3kNNyc_rMPjRfDU_-Sug8w8VrEijW9JvmaFsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=AquwbKSTQZQlOGUoyj0cA4dHrRXolHGierK0WQdFzRX_adFZsS6X__YOdyjDQtlreGNaTZuHjyY0OjWX8R71c18Ec2_fd7jP5ZvEhDxaHBmX1ZnCkayyHwgh8HYpv1AVHE3Yp2on6AI-YLffpIHu922x8f_HuA6ZTRdOJ-_-v77ha6PV2i0GM5FF7G4w78cVZBLfA-zmGcN0abOFkSRs3sqF9zEyfIzF_XE8xsNZNIKtX6rvGcJdreCxYKcSOlbyieoXGJEbbw3WU1XM7Iub8tolvlRe13Tzug9UR-NvKoIRmfHw3kNNyc_rMPjRfDU_-Sug8w8VrEijW9JvmaFsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکم رونالدینیو افسانه ای ببینیم
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91688" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=PDpslp62kaY9sNEvDmtIhe2ZfRniig8u3T5UbjuaH898L9HDeOVx9UXgHxI4etRR241LnM3Eg6TqRKSMdYfkd84kpfbqep9FxdevuKgZQLD48bIWyL8ysDdV8rxXdLU2tlVK-9Vh1igNsMdiMb9ktyGPBTsKleSksfzWA3ou_gPahj0pZaralGgD8XURK7aJ4BeW3xQckClhIMy1Zz_R7uWt5q4czMN-F--lCyLSglhwPA4hf97G-hVIalZaIjCOeGHA8TCroinjJUnARKX4I5aguXv3Qj05cBOVjFala2NV87Wy12_OmGB0D9vdlInBp5EnO7jf-6xG1l7-mjIBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=PDpslp62kaY9sNEvDmtIhe2ZfRniig8u3T5UbjuaH898L9HDeOVx9UXgHxI4etRR241LnM3Eg6TqRKSMdYfkd84kpfbqep9FxdevuKgZQLD48bIWyL8ysDdV8rxXdLU2tlVK-9Vh1igNsMdiMb9ktyGPBTsKleSksfzWA3ou_gPahj0pZaralGgD8XURK7aJ4BeW3xQckClhIMy1Zz_R7uWt5q4czMN-F--lCyLSglhwPA4hf97G-hVIalZaIjCOeGHA8TCroinjJUnARKX4I5aguXv3Qj05cBOVjFala2NV87Wy12_OmGB0D9vdlInBp5EnO7jf-6xG1l7-mjIBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
الهه منصوریان بعد زد و خورد شدید و فدراسیون ووشو: من در برابر بی عدالتی سکوت نخواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91687" target="_blank">📅 16:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=u8F-5HzjbaiJ61kRJqTTySs2Ud2vuqKuqek3XtREGkag-ENezGXCe5TWCohzlAjG4G_kyb9WtR4dR13abYkTklfUsGz5mZBRdWTH7uyr-qv0fDtEqIne5y6dQP0exn3yLeAraFgnirxWwhl8QdjYDHEZkClmgXPFVlURhMoOcE8AbZeaBb9ohHY_IiLckTGWZOX12wHJ1awal4xBmKksidCbb5w9JQjffEuVmuSyCl0lBO6cvOxR49LTK1IrYovX6LdifFuXxrxY5GNFZS8wunsD1W0zvuHNU0um-WMdI_i2WabJoqWxQEikMR06a4ZFd-Y_CXolNMdDDVHgbd2qDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=u8F-5HzjbaiJ61kRJqTTySs2Ud2vuqKuqek3XtREGkag-ENezGXCe5TWCohzlAjG4G_kyb9WtR4dR13abYkTklfUsGz5mZBRdWTH7uyr-qv0fDtEqIne5y6dQP0exn3yLeAraFgnirxWwhl8QdjYDHEZkClmgXPFVlURhMoOcE8AbZeaBb9ohHY_IiLckTGWZOX12wHJ1awal4xBmKksidCbb5w9JQjffEuVmuSyCl0lBO6cvOxR49LTK1IrYovX6LdifFuXxrxY5GNFZS8wunsD1W0zvuHNU0um-WMdI_i2WabJoqWxQEikMR06a4ZFd-Y_CXolNMdDDVHgbd2qDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91686" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCnoXDXgCMM9d4OnZOCt9I-caAPOrIx7yATgUdfcDiycfLxQaAVJDzfare2UIyHF84fpdmxPaFTR-24RSLfI6xTK91GFo8L6v5hv2UFFw5zjCfdw02eGh_DMtt-Dk3HeYhIX7GEHOhpAQUvQN6ustFcMNRnpMDsvyyiSbnYOO57mQU4aMfwyVz49qa-uv-ROIkXbPg0Y_pQ3Ap_kP_5CUqWjmAEnPRU4SqQd0Svdp4lYM7XdreWZoQkj5bQ1Q07ZdY2AqLkveFrs9LrMh-e7rYfczdT4EqcM3jaV_J0B4o9M_XoOl48xJH66S1XV9GseYtU1Lkr1J390Oh06015z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو وارد مادرید شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91685" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=gGgGmWa2WYRlPxH27DQ-X8-gJu3OrIthngBuLNnU12Kiz-7lG_yPdtKuJBFi9o6qmA8ZYDbcWTK3tjqSyV6BES7mCaL6X_0q90szcM4iFSfjcRokYBnmh-aJ9R6Q3eDQY8uVpKy1g_5myfJwxfdOACHRVm27hpm-Dfn_Rlx9DddCwBGhmMHRUIH150PuOmkTibWvLBLNhzE-rhvLEyM7bhu_JUQzq5AgAnW6RVq5RcngHiSMMxtsy6bN79CxIU46ZkTddLWpfAOW5VnJEWlB3rb0F4rC7EtngnKv_1hFntvfatoKaO9Uzo2lWysS6TSWDGWHztxTkqoSidAS9_b7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=gGgGmWa2WYRlPxH27DQ-X8-gJu3OrIthngBuLNnU12Kiz-7lG_yPdtKuJBFi9o6qmA8ZYDbcWTK3tjqSyV6BES7mCaL6X_0q90szcM4iFSfjcRokYBnmh-aJ9R6Q3eDQY8uVpKy1g_5myfJwxfdOACHRVm27hpm-Dfn_Rlx9DddCwBGhmMHRUIH150PuOmkTibWvLBLNhzE-rhvLEyM7bhu_JUQzq5AgAnW6RVq5RcngHiSMMxtsy6bN79CxIU46ZkTddLWpfAOW5VnJEWlB3rb0F4rC7EtngnKv_1hFntvfatoKaO9Uzo2lWysS6TSWDGWHztxTkqoSidAS9_b7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی اینو با این افکت صدا توی تیک تاک آپلود کرده:
صبح بخیر عوضی فوق العاده؛چه حسی داره به عنوان خفن ترین
مادرجنده
دنیا بیدار بشی؟
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91684" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUNTzFsB_jNgRzrNjsqvAk8EyJwkCbZH7SF7LeQCTal8eoe2ZJsC70gODZ-vf2i8vUcLDIHccPJ6vj_s_BHP5Y8XV8M5-mFbb2ChX8WvCFDGqmrtaQzoZp4w8X-XkS7ZX4IS1z-xCxLAs0MWapkvlB8pEDTOTE99g0a3hHUmJqIueU7qOlYoFfARvJdW3xYtzDo_tIQYcPnoA1OUoGVSBxVLen4X8HISyvEbSojglRp7nyHP8ePXjXqpH6YpX4-SVho3ME9EOrTxeio6aw_elj0mVLX0HggdsAdF28BefPAznod38rC3CUHL0OOw2BQliKsrdekTBnLGHWu2O1h8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
بارسلونا همچنان روند جذب آلوارز رو دنبال‌ می‌کنه. ۱۲۰ میلیون دلار حداکثر پیشنهاد بارسلونا برای آلوارز خواهد بود. مذاکرات در روزهای آینده انجام خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91683" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiO3B0vNl-Xcq_Yrd23whKAaASeeH31JiF9NKnw3nLcbmiliccBfnZmkAvAvMDYxoag5zjNtB8z3y3gly8LaTuohYr-rqjTyWTFSxps0SDjH4yujKXKfLUE0FNewFH-_0nuB9da8IKr1gvGYy-Pi1vxNhm5r8O7hIZtdOboYxWK4gkoHr_-w8Fa_ytKuEY7u4TdCRI-ffVUdH_iqeEw2HI3s4IGGuXccaNdnTdhaGc9anCSFcwDzAwRXJx2jmFlCc6Ia6DPdEPB64uGU2BhZ7YuSlMFgg__gQaWdBmoNW5rs_Dq48VWbthQ_Rj38Pumn-OPDayhtHecG07Rs5Ail9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
خدای جام جهانی؛ زاگالو با ۴قهرمانی جهان با برزیل
🥇
۱۹۵۸(به عنوان بازیکن قهرمان)
🥇
۱۹۶۲(به عنوان بازیکن قهرمان)
🥇
۱۹۷۰(به عنوان سرمربی قهرمان)
🥇
۱۹۹۴(به عنوان مربی و مدیر فنی قهرمان)
🥈
۱۹۹۸(به عنوان سرمربی نایب قهرمان)
🏆
اوبه عنوان بازیکن، سرمربی،مربی، مدیر فنی قهرمان جام جهانی شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91682" target="_blank">📅 15:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=iIQqxBo1ekYp2B8mD43LxdBVsutzKdkFYGNAJajeOEzsZOzJ7GZ9ds9-uRXbqax2NnphBoJ-_UwJ6DMKMfzEpgokuaEtwLnfzxjsOCvs-oEBBZDvmbaS5In2inzYQDD3D9B9PIOFGU7cSoE19IjKzyhY0Qoyk513YT2Hwkv1ZL_V63lVdlWr1CLPpLzS-Z3m3c1j-cFMY1FyxUAiNyvyRdQrQK0OC5mUdvgBA8QxWy3Zr5uN_QelkgmTtb8XbRITE11vAGmnrRC_Nnrfo6SyH1QTrR7XM4Tlp_8SyppnmCOF51A6Xr3vRdOszTbCCwJmzTq5J0v4wMVKN4DpVZfWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=iIQqxBo1ekYp2B8mD43LxdBVsutzKdkFYGNAJajeOEzsZOzJ7GZ9ds9-uRXbqax2NnphBoJ-_UwJ6DMKMfzEpgokuaEtwLnfzxjsOCvs-oEBBZDvmbaS5In2inzYQDD3D9B9PIOFGU7cSoE19IjKzyhY0Qoyk513YT2Hwkv1ZL_V63lVdlWr1CLPpLzS-Z3m3c1j-cFMY1FyxUAiNyvyRdQrQK0OC5mUdvgBA8QxWy3Zr5uN_QelkgmTtb8XbRITE11vAGmnrRC_Nnrfo6SyH1QTrR7XM4Tlp_8SyppnmCOF51A6Xr3vRdOszTbCCwJmzTq5J0v4wMVKN4DpVZfWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها این ویدیو رو‌ از اعضای تیم قلعه‌نویی منتشر کردن و‌ نوشتن که تمرینات فوق پیشرفته ایران در اطراف استخر برگزار میشه و اینقدر امکانات اونجا درخشانه که رو دست نداره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91681" target="_blank">📅 15:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=kvrZTLHWQ6xrBUgSYJAHhGNneLBodod20wYN3F2cuawK5nvz6cHInJDGKouBzXBa0wk7Ac1aYanUSzy7kMC28U8xgOb3UCfzkOzFlvdm_sAjBxuljReABOTivhy_ry546iSp4zC02SL67afhS72AbrXELRa1Y8wkEwXa0Jk0Y3yBJ3_XYORhcPuch_Nae6IqgW0ZKrm9CyXj5sXXFPkgsl7kvXzPn_JoYJmJo4qCwCw5gz7qF0YKasVu6VN-6iS6WhJT8rvXSetYUdYGw9ZIqDQG43p9orbSis5uRFbL6pKwQCQrOaHoBVBLhbZukD8rqZxnPW1Jhb2nL7XZOUB1kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=kvrZTLHWQ6xrBUgSYJAHhGNneLBodod20wYN3F2cuawK5nvz6cHInJDGKouBzXBa0wk7Ac1aYanUSzy7kMC28U8xgOb3UCfzkOzFlvdm_sAjBxuljReABOTivhy_ry546iSp4zC02SL67afhS72AbrXELRa1Y8wkEwXa0Jk0Y3yBJ3_XYORhcPuch_Nae6IqgW0ZKrm9CyXj5sXXFPkgsl7kvXzPn_JoYJmJo4qCwCw5gz7qF0YKasVu6VN-6iS6WhJT8rvXSetYUdYGw9ZIqDQG43p9orbSis5uRFbL6pKwQCQrOaHoBVBLhbZukD8rqZxnPW1Jhb2nL7XZOUB1kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب رفته بوده فینال NBA ببینه که باز انگار تو حالت چرت زدن سوژه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91680" target="_blank">📅 15:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnvpO1h-WuvFaksMKJPvAgcXNyVLjm3ry7zVjUYy1usDU10o9JwArUXfhYR99svsGQQLrrU1aBGUWLGfUdq3n7MlfsnY-IhXXlGOsygYH0YoEE4Nn1DVOQHBqe44HMT_BVztdTNeUQXqczRRsXEI-IzDJcfU1dzPJh4MUqy41vY2MygKK33Pg-oDrUKHjqVS24fvjusmfgr1643e50A_R5amU3FDVYhHXV0vh5BY9lyYDNP3pO5YKmJHUlqKDqRpKG6ufHPLJ2HvNtbej0G3ZX70WwCvFFrJSs2dwK3RSjm9au4q4nrstENPSteCwzIJHe_AVr75J-qyDXadWg5djw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:
«بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم مسی.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91679" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏆
اینفانتینو رئیس فیفا درحال خط‌کشی استادیوم نیوجرسی آمریکا در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91678" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn_-aWIC5WVtU05QK0y4mRIQ3gMmIwrYHUIfR1n1EKnGXeFAf7S1yuIDofEVE4edE-XGTZlJHIpGG-euTY9vCKrIdmVvukkkRwnjjvIcrLdayGTIpy799-VypaUYyx715bXErKDeI7L-K3VW1P85OLUwmAgTBDjH2eRWF9P0kY67WKLg4ZFkOC5PBFkfgR6SEyNJhTrpmy6iN5gyEYTtG8cu95hyHqzUoNi6v1luZYigPNgA3Wr25R1ZBAH8VkCWY1TxRkALC32bxF91uUKZ0K5ctGLgCStWCjJZFrAEyUNNoE6IqwcNVFxJi2BgKimDHSIsKH4C1MZMdG74VK2-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر نیمار به همراه بچه‌هاش یه ویلای خیلی لوکس و خفن تو آمریکا اجاره کردن که تو این یه ماه کنار نیمار باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91677" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📰
⚪️
اسکای اسپورت: هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91676" target="_blank">📅 14:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk533J3fMl7dXMfB4yQsJpV0u3STHyfeer-tVEHYdZNeMrvoRI_lGBtcYL8P8FATajbhl1d8WQbPJGWTVs3zSjTe-_NNhzPbY5gEsEtnokFc6bzQQTmqQhyoFa8if3YsTtzXhorUO76hEB2MJhm4VgdwImwmyCmMrQaTDXJliLJBFrRbVVOvjCzHdjZtam7gQxx0nOFXrvUHFvZ3aBIKPPif5GWEh2_Oc8vYNchGoDHtJiIFZRkSc3GDXW0YSJq7-R2ErsMlT5HMVzeW7qHm_p9mCUG2eEqeYTXS-3_9xpz85ms1XXu1tG1i3ryZ_wgw86QskRP3rouxN7mrLLwhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
اسکای اسپورت:
هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91675" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UcjZ3ykHnSZTPbUS6d9zyNamtl9pvk3dLf4lWhfFLCwShvMvMMzRshtka14W0BeHQmE1dmha6UK41YxMyrw4Pb0u3p71ys6z5sXvaA-vwGw4wPSi2Fj7LjNrlW_Aof8Ih4qgREylre28UsJ4pnkMHCtY0vYVFsZxuBD6Hw_3aqhw4tM4CRIMgqMABS5oIIewWuo2AvXkBr74c74rTJ7urkrUlRDXv2w13SPcQS099Ush-mrXztRcMkz6CK7uJ4amy0hXpTjd_tYIROINxMNo7Frzd6mnj1wNR4lNb_SfCe1Uhu33CAL8kltX6qMdVC2fVuVpNtsOnul5cbQei2oaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q628hG9ZeF8hrFzdOMHpX7SgepM0g0mf_XDzcueltNLzvjHxHT-IhQXzvopxp_LWky_X7huzIlzn69HsDInLrX_hYkw1XRa6Kss_Bpt_HfST2H6hEubgGwAIGF5j1KaWYMyrMrLeI1Amzzbi1pcRvccRGnLauIK5p7huhYJombcqHq2NVojJvXR69cQqHKhBGBlFMrtjBZr0RjxBUD3SD9SnfkmFjbRIuKvBZWgc27OU-0ddBKq4GDtcgsKyNtIYkOIrNrLmm5Gg7xqCbdzqvuzVn_ZfY088wdGFAbjw5V43Oxz4YUxVlhUuUAJ_eQ2ZEpsl53zYtWNN-0XeN0o3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAcsi4hOqbMCagflNcNfFVY8ZnW1L8TGCJOYDSkWrz2Cs1Wt0btE-UGRtTQOGK-hWBc2cwdXZmD0ju_d72YsNHPWrjyVRnpd2SD8GTNDFzOofrpKAta2rNjWATMthChBWqofErcFIjSjXFpkBdo7T7gy3HL892TK1TCjZ-DJHQdwh2pTs0I2mp-mr7Ug68hHP5bs7-yXnj6d9a8ZHHSr79nm6o4xaMmb5P8TeYRcmieNxgjprTEjEWDL5fhzuVOf3QzpLbSAdX14W74HFSr5ydt-BPDVwncZGkaXobsF-e-jbHmtLoQwjNFt8fXL5CwkmN3BgeJefeJbp0f0eRWsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U084L3OwoQAp9dc8BjghKwDoKHNuRwyir_X7vPBmunGrodqxF3KqpuO6e5_UxzrcrD074saSY1BG5Rd84ECOQKBbczA0lgzPmPgTxU_sDQYlOs4aihxjjhN-1NU0DM6vgIPgrP2BdPiRYodnR8DvqRwbQAp4VJEtD7ZOM1lTv6bMIHZQp7u1C2WQWpck68KMSh0zG3UacCYdfTqdzzxPqcnNH0yyu06YYYaRrqN9yDQhVLiUisjdwyUd9HlFuKawFNya_Vj7B2V_sPm3rpsqJi5GVJG5WJo7unUQrkWqmwpbOXuvWnfJrTS9DfvUYjfoDh7JsHF106PlzkAYl9kLoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجری داف و جذاب شاختار هستن.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91671" target="_blank">📅 14:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=L74Gp0cfuuGw97lVgmS8MR4mAyMZjjPNVPunaWJqM8QErzkWfrAjs2qw1fJGtdfCt7V2dxYjZvzHMzTEY91ScbN74DoAl-bpKcdWAuYPMbLOTWbp8-1Z02TjX4NePhZ1ph1AoHcSgg2vyhfodxbMPelopXGJYVeCynaWd2r-rTNftSTlVyndmTcKml0vutOqgOakQLTa3UtEnv0WfSA_1d7XErpRD3lVQ0COoU0gy0pGYUOX8r5qOdD-xVcwlfixoKhcKOjHavjgYrvIV5FO5m5kHLY5z217zTgIND4lagG2CDjyDjcBmCl0sVLycGTVf0hz9HNKQhJO_sQwGUeKdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=L74Gp0cfuuGw97lVgmS8MR4mAyMZjjPNVPunaWJqM8QErzkWfrAjs2qw1fJGtdfCt7V2dxYjZvzHMzTEY91ScbN74DoAl-bpKcdWAuYPMbLOTWbp8-1Z02TjX4NePhZ1ph1AoHcSgg2vyhfodxbMPelopXGJYVeCynaWd2r-rTNftSTlVyndmTcKml0vutOqgOakQLTa3UtEnv0WfSA_1d7XErpRD3lVQ0COoU0gy0pGYUOX8r5qOdD-xVcwlfixoKhcKOjHavjgYrvIV5FO5m5kHLY5z217zTgIND4lagG2CDjyDjcBmCl0sVLycGTVf0hz9HNKQhJO_sQwGUeKdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
صحبت‌های عجیب و کنایه آمیز شهربانو منصوریان: من راه میرم روزی ۵۰ میـ‌لیون درمیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91670" target="_blank">📅 14:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91669" target="_blank">📅 14:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_Hs4Hyxh8qzLVbe81mQ5Qot192UXc4E4QB_NGUnFN3DcUvHBD2MSzOumlDFqJlTV1EZ5K6a4GLY6vcBttoDtR7ju5xUK_r6UBQka7hZH11Cns3ceeOrATi0BKbHwV842AbIyPKg1m_5asSIVNzNFhxoizly5y6eNbPJwFCIimRSJFfxNDtsgcMkyWeBVuXcLnXo5Duk6D5uabLi54MWuT_rBzuTuE-8roC7a-QSSOOSeNtMKzgJyh4hG4WUFdqocOrSlYR1MaEkKfZCTYYrjJJmIz-biQ4g9CiNIPbsofLggvPA9LNr7i_PnEfXEX2W3pa3eUGKq0DGCOYLcJFA4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLMM3vQzmyO2_Zq6GPPaHqsG33hLWjwkWaJADJAHu28dC7UwTBz2eVaFzYi9ib34NZuLiSaKnnK6sDgW5ADJKS7rW27QUqF3zQ4C8Ix_WIuGE4_lXTCCXJc1NbDyjNIf3L3m6NMDW62hXYabY_5pA5A-9svXUNajZxWWW5L5gFvM4q5jWrH4P2KTQvHp07jPrfxjVyxWgh4slnjtB25JbJl0OBFhGv7eJNDIO8-q8901Gy7EG5iKlY-fHsWwqWWqwv8MAGRbSJzGyXZaltQx5PbhO--JtZceb4ZJFVnubgWyHL2TD07mBYpmAjr4EzQM2JI7-bsVBGnrgjPDbjzkBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
مسی قلب‌ها تو تمرینات آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91667" target="_blank">📅 14:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOptxp4IPIH5-QQG1f0Rlm8WvADcfOdmt8wjGOsXDBYj3e9nTACMJKeD3CFQuyJGtDTAHr67Od_xKIlwnNx50iquqyH11PM2wrmZQSW9fdkFeG2MBZ1L-sSxX3cV9hTOH37IYx9AXRAHWv4u0hCjmcHgUGYLPEBZVNmtCmzWGKZ845zQHIvHLvfKAS6vgPw64DAL0ta8YXXeRls4uEkkGv07qNPa5wo7jSk2z4MjnmNoP0_x84FvQkivwWjYRcDCCBJP1G6n2SgqY9gaPajG0dHd4HRMqoxHq3YDH-Ee3JXnxu8c05kXNTtrcBUnv4ggFsxfwObnVlBYzNv7RH-Mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین بازیکنان تاریخ جام جهانی از نظر امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91666" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=NZT12-Z38Nri8lE_ZJBaXqoD7ggI7IKl0e7mKF2D80T8dQkUvWVG5a09k-Hbebo5A3Jw1Uoqm8Okco1UqttDpRUM58oQ_Y1jprBMYRZlwpIyeH8oDM3k6Hf6G-k0mrE9hx5ExG2QxSZbNdx2JlX3NpQgF6nKvkrTJ3awlIxWzK6SlUI0F1mMx9pvCiLmT_tVusYtLD_m0O8CNKClys1Yv8EQyG1mqUDRPNIvyDBcJ9MvR0JIS3bDMJNZrEjZz5m6bEiLw8roY-JMIuX4lPW_8OnIpFUKkjpq6THb9EpLam-LVXH1igj4IQcJO9K7McIQTbBXoYQn4PSRgPLFe8_q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=NZT12-Z38Nri8lE_ZJBaXqoD7ggI7IKl0e7mKF2D80T8dQkUvWVG5a09k-Hbebo5A3Jw1Uoqm8Okco1UqttDpRUM58oQ_Y1jprBMYRZlwpIyeH8oDM3k6Hf6G-k0mrE9hx5ExG2QxSZbNdx2JlX3NpQgF6nKvkrTJ3awlIxWzK6SlUI0F1mMx9pvCiLmT_tVusYtLD_m0O8CNKClys1Yv8EQyG1mqUDRPNIvyDBcJ9MvR0JIS3bDMJNZrEjZz5m6bEiLw8roY-JMIuX4lPW_8OnIpFUKkjpq6THb9EpLam-LVXH1igj4IQcJO9K7McIQTbBXoYQn4PSRgPLFe8_q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💥
بعد شکیرا، اسپید و شیدا مقصودلو، حالا نورا فتحی هم موزیک‌ویدیو جام‌جهانی منتشر کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91665" target="_blank">📅 13:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=O4TCLBgNrmDreT2Tf-4NhFNUSIplOv8GIFwJKyXAvKayYGr-ReyvzkXT1t3NtiRoAjZqS-zM-2_aNUlY7a_pDWmA61Sj7InG6e9JFJ1trzBT8zvEWYd6r3ASvEyvKZi7efiDjaHpSZEJcFVcSQEuaszooxJXLCoX67Xvm5ihjKjLDvCPY8BEBCP9yi9QKjWsI3ljvK7mFKnxqfJ-5xmrsEEMjmCzWgfD6siTDCjMbPXFL_ITObBvTG2kobkFHiZ5XZ1oM3SqAIww-lCHWa04dURpv8qqIWCWB-5DLkAOqdd-VJeuSDN2FO-tJUI0oVMYX66aWBBN46Cg3yVTfO26cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=O4TCLBgNrmDreT2Tf-4NhFNUSIplOv8GIFwJKyXAvKayYGr-ReyvzkXT1t3NtiRoAjZqS-zM-2_aNUlY7a_pDWmA61Sj7InG6e9JFJ1trzBT8zvEWYd6r3ASvEyvKZi7efiDjaHpSZEJcFVcSQEuaszooxJXLCoX67Xvm5ihjKjLDvCPY8BEBCP9yi9QKjWsI3ljvK7mFKnxqfJ-5xmrsEEMjmCzWgfD6siTDCjMbPXFL_ITObBvTG2kobkFHiZ5XZ1oM3SqAIww-lCHWa04dURpv8qqIWCWB-5DLkAOqdd-VJeuSDN2FO-tJUI0oVMYX66aWBBN46Cg3yVTfO26cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
آموزش رقص در ایران با موزیک دای‌دای شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91664" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIikM8wV3crsQJQQg_H3p0ycIkBdSqPKehnx_TVsLquPFbPxZG-5KUy1o286w4JhFBryixPg3sEyV0ERQM_Ta_EPZsMux0MwSdBXi4ppBSeswy4EfZGz9JetZOxlauyi2Rs-AmwE0pydMf3WBhtfvZTP4lrpSTf2NFqKxhUlBrBxw9nV5d05iosuyghPT5F_SONrWbIbI4ykQWvk1IlIUYakDE2E1-nrBDMEB2B4VMSu2cCunaNe6Mx_hOuolRSmrBPHF3P7k-LWbz94A8STaH7ZsrvaKAifSod8DfOOUbCymhfPde1drAwb-3YMWft_wyMl7KfrSX9YLaIh3lD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
✔️
پسران رگنار و عکس رسمی برای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91663" target="_blank">📅 13:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d43531369.mp4?token=kgNq4ts20ftvd-NY87Uu7dErakvH6wrU25pdUiLSeF9fPyPoO8tx_Hxha7w6nGZQ7_E5rJV-Nmb8q0lfV21F8_DTsAOENel3oI4foB_upFRLCnTo_K-dXZbjA0mhAjOVxsj4FoyqFaxEsQhO-lQbW9HH0FHqEBjWrUI2CrRRRmIrsvRgTvJHKja_gr_EsZsfW78G1BjhlV7omzL19mI_WcCjFWUJ5UBY7SI-H5LqjQJ_AQFlkULi8k9QXVmkbEXDrkovUFH37xa6B9FWKPcljzkWuyE-S_Yr3DFdjvZ6a-hM7aSb2hi1vWBL22JG1L-2hPTFBVoTWUSGkZ4i4Q5X-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d43531369.mp4?token=kgNq4ts20ftvd-NY87Uu7dErakvH6wrU25pdUiLSeF9fPyPoO8tx_Hxha7w6nGZQ7_E5rJV-Nmb8q0lfV21F8_DTsAOENel3oI4foB_upFRLCnTo_K-dXZbjA0mhAjOVxsj4FoyqFaxEsQhO-lQbW9HH0FHqEBjWrUI2CrRRRmIrsvRgTvJHKja_gr_EsZsfW78G1BjhlV7omzL19mI_WcCjFWUJ5UBY7SI-H5LqjQJ_AQFlkULi8k9QXVmkbEXDrkovUFH37xa6B9FWKPcljzkWuyE-S_Yr3DFdjvZ6a-hM7aSb2hi1vWBL22JG1L-2hPTFBVoTWUSGkZ4i4Q5X-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحبت‌های یه خانوم دهه شصتی که ده تا شکم زاییده و میگه هنوز این تعداد بچه کمه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91661" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91657">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEMUAPWVLs1BbSTzx0cIyyALClYMJOFe6ecQ1AtCt8rpb7H22JLSSiNKkbcOtB-swjgAO3VLAp6AZCnU0-JFzNokmR1RDtxbRM9YHkTQ3RdOnqIW5xzlm7BTqXdDrJAM0Uc1XRwub7AGClW4KRV0pDXiph8sIjgBFu6w7u8PpLhW7g3SiYr8eUT-yfAFd8qbVHEyJYB2twVqu-KhxCHRlW8rX-WTZDvSuL3Bp0L6OV5iSpAJJuwjiVN37DG1O6TgVR0KoHmQsgVTLHY45QnxHtVetN6ZliqpOD92cJW5-k3v-NUDZBRRF3dKdny-NM-vBV6jxHljyogvaEATo8UsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQOj9ypmIBa-bT5ZROI4k7iOyQTHxEuxwcLqltRwf23SUHAfyzoUQccU8HK9LtXgBCCCfrstDRKATuVK3ZBrn8Xzrlj6VwrfEfYMfX-H63wpAAw9KgjmSkgDHcJDIuGB_BqPcHf8XtW-RlvcsYEH07f-qhexxzGz0ipC2I9w71E6m6XcKAZ05Z_HKWaQ4tcSCkCFjSemzORUoNEPfTV9LQFxjhMz7GV1rJ2ranskotLFc2Wxnym1tMq2TJrW_bsENL6TnzQICE8Zggz1g7rHrhXd9-V7opE7mpPy9OHxl2inpLEnrnTLjcn2PiZZhzEtOx_2DL8djTYBxVvXYsnbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxZxTTSMCss9L34omLxgbJquVGVky1BErEY7UTLwYQSUfZhaRIt1RH-yQKKuhdi-1rqDJylpdT6sCBh3-Y6LHHnIeGL1Vil822PJ8lN9SdJ6eZ6xaKCwilcWa3aCRlMX62ZbI9vM7TZ5vt4zxqNT1BVNHQxd9ZF0SjNzjdPdbPuu4Zl-aWWpqrLtSZ3zVO7vaRBpC_oC7OBD5WFDlUnsXVqeCaypwiMQCy1XFJs-1LCl9ikuWWlOzzl1JFYWn68GHOUzWcNuguo8p2bbFTKumTKhkDgfF_ioYYT-8NczD-0Lat3BQGHtrFpTMnHV355HAKScCvHJ7YCzBLDFfJu6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2KbJlNN0WOBZDmoFmjwUdr88dFyEwJ0Kv_z6To1_ueDxtgOdLtcnIL2xAljebMwFZxqhzl_WS9KtiW8eq0SMNvArp2kgDA--fUF26J40CPH1AvYF2wiQLB6UeB6m0JODOCA5y9wS24zANa7A1vtlvnsILdnssTYdtP5p4HNnmYfs640yHm5qiZcSBQZqMY8a8-WV-0JvOPfK2oB6Be3K4_RY5pQFD_NMt6rQ8WZ_z3WpIEQgXkQys5-9Dt_XONauDh7uFzJHurBn2hfMez3ZZlnPfiKL4OBhndQH-65TxAcb6obiF12GthfPhbHZpW1Go6BgWUZK_UpC-cYujO3Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
داوران چهار بازی اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91657" target="_blank">📅 13:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91656">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=ZTnc4uPk3jSpLMqif3kpqPbqG9NfldzrVRsO88ZbzJzNXGZuGaS9xayyFDVu97h89ufyUKR3ff6-l3UmPpNoBfPVth3iBZeAn9FWwLDItsxblHb93iIcqIVZN8A-cwh7MOQzk6KEfKuP2jce_o0DvBgVCBarvJDsVrdbZAQnLspjA2g93vd_CFMv_Xw1AkcoiCmSPLiUtxLqLF46Ohf3Vns96YN8qz7zCOJClkEPIYpYUk0QbUpSjtbHD4FsJKa3Mtm-TwNs8Y43qPDwDZusItfEAIafpSklCbVm_7CZBVBGwv5_uFAej-GjDMn2SgPh5zaW1S0vqbCsVsxtZzcVig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=ZTnc4uPk3jSpLMqif3kpqPbqG9NfldzrVRsO88ZbzJzNXGZuGaS9xayyFDVu97h89ufyUKR3ff6-l3UmPpNoBfPVth3iBZeAn9FWwLDItsxblHb93iIcqIVZN8A-cwh7MOQzk6KEfKuP2jce_o0DvBgVCBarvJDsVrdbZAQnLspjA2g93vd_CFMv_Xw1AkcoiCmSPLiUtxLqLF46Ohf3Vns96YN8qz7zCOJClkEPIYpYUk0QbUpSjtbHD4FsJKa3Mtm-TwNs8Y43qPDwDZusItfEAIafpSklCbVm_7CZBVBGwv5_uFAej-GjDMn2SgPh5zaW1S0vqbCsVsxtZzcVig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری راجب وضعیت اولیسه و ری‌اکشن پرز
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91656" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
ادعای
مصطفی پوردهقان، نماینده مجلس: رفع فیلتر واتساپ و یوتیوب در دستور کار قرار گرفته و بزودی این دو اپ بدون فیلتر در دسترس مردم قرار میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91655" target="_blank">📅 12:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68f156545.mp4?token=cWNH32mM0EvBZq5o7bZI7OqzyAPjY8ESWy0iNtrQ2aAzw0VPkl5X3aZpkqYDcPlU1r6P0Ce0sBtpns3sUDFHjM-jeMAnODoQKuslhm6_hXl9UE6W3qUHzEk4B_SADO-O_muGXmQMtBe3SY3kMYRzKI3g4H5AY84QUCFGbpcmOxRwNZLByRIK8XskrOvOhL8aQ8A9llCzywLHirkyymSSavDkyN3nDRGZK9PhiHKiEMI7mX8VdeHJn23gUBwOtuQp-2JSScvfmvSNtMrI9PvFXMZYB3YW9F14R-V9G8DCOmYMKjM1Qk2hDU-vdvDsVtm82T5MJLW-uxN_GlMUi6Dgqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68f156545.mp4?token=cWNH32mM0EvBZq5o7bZI7OqzyAPjY8ESWy0iNtrQ2aAzw0VPkl5X3aZpkqYDcPlU1r6P0Ce0sBtpns3sUDFHjM-jeMAnODoQKuslhm6_hXl9UE6W3qUHzEk4B_SADO-O_muGXmQMtBe3SY3kMYRzKI3g4H5AY84QUCFGbpcmOxRwNZLByRIK8XskrOvOhL8aQ8A9llCzywLHirkyymSSavDkyN3nDRGZK9PhiHKiEMI7mX8VdeHJn23gUBwOtuQp-2JSScvfmvSNtMrI9PvFXMZYB3YW9F14R-V9G8DCOmYMKjM1Qk2hDU-vdvDsVtm82T5MJLW-uxN_GlMUi6Dgqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
لیونل مسی: «از نظر اهمیت، بهترین گل دوران حرفه‌ای من در وقت اضافه فینال جام جهانی مقابل فرانسه بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91654" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAc-3NY2oXKtp8rHtW2U4JYDURkeR90J_Fw2175kNQ-hmKS5K-sfeu5BsJV2bbHAP4g5Cmd9GyqpS8dsTp5AOsJ6m5CXldjH7K1glE2Vz4ph7zvCJAgoRfHH0K8KtqlgkkZ-aZWxObro3cf38z_eCXnC16Q2UnogbswlsUpvte8m6y8Yam-rcggIKrPaMwS4zPaIjbhJXwpxNxw7O3QKGndNcCS0GQI_Et7oH2ISZ5cgwzinAc8p_xH7Phy3ZBBc0HRQQzS9ydF2pJGCxiu-vi1H6TMmNXf0JLO3g4cOIRMXkKP2Vq3S984btlI8dPM82iKqoGhhSWuwipNbmeTMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔙
هواداری که به خاطر نوشیدن ۳۲ بطری آبجو از کشورهای حاضر در جام جهانی مشهور شد، دوباره برگشته است…
🔺
این بار او ۴۸ بطری از هر کشور حاضر در جام جهانی ۲۰۲۶ دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91652" target="_blank">📅 12:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3RlGVvQAMnrs3MRo4SSJ_C0tUoImItky1dhiOQyTKw9xOe0ywLkv6UcwtklVAiSH93NzSVaDQ1jl_dq3R-Rt873PL172Aq36WIBNYhYskTnjLUX87d1WlEyWJSZWUzqTj2xhDDSiWeQZKJtlx69AiKrgkpwTajtN-WRAJzRLfZ9Ofi7HCuvY91fJlpXQxzLNpYbIyFKehBECGP0jEnmO9ScIFEJElu7Y3UuCSGZxegWbxQxRW7hLdYr1AZDx2ZseezxLxNlanHKhUA5jkX13WX3C2wroEORCz6M_l6mfFyPKd866di8KRLgo6rcH13ACIEux-zFWKXRc3ab7XPJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژوزه‌مورینیو دقایقی‌پیش وارد مادرید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91651" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTE1HHWNOVBWW9bPh_gRrNJvq0Hyy9suLvG9EFI9boxRzRj2woYhesK5cZSGcZ1ulogP36ES2ob7U3XO3DumDJpMGzOtEeA6JYfyR-rBNqTPFFhe53yrHgIKWJAg81wysVGIT98LBuYtnC3RBRu5c2UJH-S8Li9QswOX2GAdiwkZYc6HXN2Km0r9_myiVUNzVWxZlDqQUVBKkh_EqunMKXM3SXfFwr3bTV7-14jVe0EseIE7GKp9T8_HMJJZniNCUFQK-O0mCaniUIy5PgpqAhU6rOgGfd-D4FfPV_M6NrZFfMjcw40H5Fv5LVztWmbvdeXe1kz9Mc3DLhymQ02Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فرانسه در گذر زمان..
انگار دو تا کشور جدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91650" target="_blank">📅 12:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAWUgLMiN0MUdL83Bou4S5h3J7Da7lT43xvmny2_Ltmu2xa85PQK-wnbngal0MBI955v4kJkoYW5ThMrN1F2nAeTzh9nlmXXZPo2nf2IPe6KtEv0szVvk0n18NKGuhcPwjH9lbvPD6xHXyQJb-UoBCaLq54KPbylFXmqKtUW20rxGHzqslNYlTprgR-PjzbTbcLfVZAVktnb_baQfxrfElBaEZqwqo8xjo6U799OuaiMigBoIU-GcHdbtjy61bTDleVrYa88CFJW8an2t-iD_MTYUWdLUTP1InNcA31SjJLo039RwYXZh64lP43pw-XZUfiV4w-YixPwaymkftAASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ دیشب سر زده بلند شده رفته فینال NBA رو ببینه که باعث شوکه شدن افراد حاضر در سالن شده و از نکات جالب اینکه تمام ستاره‌های دو تیم فینالیست توسط ماموران مخفی آمریکا بازرسی و تفتیش بدنی شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91649" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=d0HjC3uM5a7IxUWrpMYF6bMJPFNOqnqvq-msPkLkVNLZV4_FyadIG64lgOc1UdnPXgpbcW9612v4SjA0_SvngqOEIZTHHy2Fxq4M5t3aP1s4cyeUxTEGDKvDm6f9rK5Jz51QBY-tZJ_hfiYUftBno5ksH4M0o6LakadZoh43pp5fpM76eD_ef-em-lPQgzY-R1U_fe-E2p7oSR9bANqgl-PQljbaSBoE7q-jFmZzwX_hWYIkJftbv1aKvFXq_QWGLqWkfOp3TpkyVpaDBl8p9-m3H4HSlyn7jGvy0S1pm1pILOPyBonc7CqrQ86t-pKqEQFD-OZ14qkinIrn6zNarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=d0HjC3uM5a7IxUWrpMYF6bMJPFNOqnqvq-msPkLkVNLZV4_FyadIG64lgOc1UdnPXgpbcW9612v4SjA0_SvngqOEIZTHHy2Fxq4M5t3aP1s4cyeUxTEGDKvDm6f9rK5Jz51QBY-tZJ_hfiYUftBno5ksH4M0o6LakadZoh43pp5fpM76eD_ef-em-lPQgzY-R1U_fe-E2p7oSR9bANqgl-PQljbaSBoE7q-jFmZzwX_hWYIkJftbv1aKvFXq_QWGLqWkfOp3TpkyVpaDBl8p9-m3H4HSlyn7jGvy0S1pm1pILOPyBonc7CqrQ86t-pKqEQFD-OZ14qkinIrn6zNarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حمایت و تشویق کیم‌کارداشیان برای لوئیز همیلتون دوس‌پسرش بعد نایب‌قهرمان در رالی موناکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91648" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔥
🏆
برخی از درخشان‌ترین سیوهای تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91647" target="_blank">📅 11:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91646" target="_blank">📅 11:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTa9qWK_WZN43ukRBPePOTzrFnuAhHPW_SCQf2WwTEeaxULxySmFmY1RWuxvTzhov1eX1Y_q-Mdp0r8GZ6bmiqx8_j3K8YRhc5ebXrsdhXzemHZyWiA1isoc0s0ekf9Ciczz9Q0rj7LelPlhwPWYh-y7CiBMsAS7_bM5YEl47mrzYZOIzTbmpaEgC8L0dbxRkwRpbPaqCvKyOm0_X6Im6lnDRBb-KhenU6wE67zb2NljY78yRG-_aTyY9WQmShmFq2UA-TtuwnDKvrZWpwkWhKqqLbpaz4UNeLkjB0xIH59KPEcG7bTYNd-Sn2V4_7vX6azoG_Rmo_8ji-VSOf4YJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از اتلتیک؛
بایرن مونیخ هم به جمع مشتریان یوشکو گواردیول مدافع کروات منچسترسیتی پیوسته و قصد داره برای جذبش تلاش کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91644" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY_DZhyyhhC2v3AXNFbZ7J8x9vIhCvFydyePBGDCpyxPSfvJfCDFqHGmu7fpCW--xq7pye7f4ocUSMWKuUByfJepVMYpZSlxJ68t8N6IhyXigpSeToPCF1TMHnCHHsTjw9UeFjDdwt_dnDy3eHmoPTINksV3MYj95XdrjNLImqlPl31m2gfsRWknNfjkdgDV0lglwO8G9MvqK1EDu6ROFMeIqAK6Nwz31lZeKpFKu_SFiQhMBPdDgu3oWr6bhw6gbwXO2fr-lk6wVONPTevWhNAH4e2PzXb47SeO0cTqQocciyUQGlUhpnCiIXK4PKoa9yXPk6Y-c3MISSzdW3m3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🔥
لامین یامال از زمان جام جهانی قبلی ۱۰ سانتی‌متر قد کشیده است. یامال که برای اولین بار در ترکیب جام جهانی حضور دارد، با قد ۱۸۱ سانتی‌متری خود جلب توجه می‌کند.
✔️
در سال ۲۰۲۳ که به تمرینات تیم اصلی بارسلونا پیوست، قد او ۱.۷۱ متر بود، اما با برنامه تمرینی حرفه‌ای و رژیم غذایی مناسب به سرعت رشد کرد و به ۱.۸۱ متر رسید. یامال که هنوز ۱۸ سال دارد، پیش‌بینی می‌شود تا ۲۱ سالگی قدش همچنان افزایش یابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91643" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91642" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🙂
دیوث بازی مرحوم مارادونا در جام‌جهانی ۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91641" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
ویلای ۳ طبقه علی کریمی به متراژ ۱۱۵۰ متر مربع در شهرستان لاهیجان توسط قوه قضاییه مصادره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91640" target="_blank">📅 10:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=bunpyT7Ew1uFoBzLMT4sqpynks2dos_dquTn44_YdjESQwpQi6KEVXLHL6thGfbOYhU90fSWM42f9dPAvq7fHwr8YbI8t8m9nh-Fh3eGcKrRqD17Ba0J0bmgoFVZCRIEHBt0EGLyV5mzR9TXp4qZ4g5MQng-KoMMpKZE7I4mbad2LHJvohMbiN2e9vO55ogiEsb2vY0uutvKudGO15YiBWvjxjtNGXXzyRqwiw8xI5UwExqw0oYb9HXiHdILGvB8dZ_3KAbeMUaSlEhmmSembXYzWeLCKAV1wb8VgKefCg7WT4-CCZ8G8HXU8sk2O2RhDdBEQpUAS66-VcuvyOR1Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=bunpyT7Ew1uFoBzLMT4sqpynks2dos_dquTn44_YdjESQwpQi6KEVXLHL6thGfbOYhU90fSWM42f9dPAvq7fHwr8YbI8t8m9nh-Fh3eGcKrRqD17Ba0J0bmgoFVZCRIEHBt0EGLyV5mzR9TXp4qZ4g5MQng-KoMMpKZE7I4mbad2LHJvohMbiN2e9vO55ogiEsb2vY0uutvKudGO15YiBWvjxjtNGXXzyRqwiw8xI5UwExqw0oYb9HXiHdILGvB8dZ_3KAbeMUaSlEhmmSembXYzWeLCKAV1wb8VgKefCg7WT4-CCZ8G8HXU8sk2O2RhDdBEQpUAS66-VcuvyOR1Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
سوال روز مخاطبان فوتبال: یعنی آنتونی گوردون با ۸۵ میلیون دلار رفته تو پاچه بارسلونا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91639" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایران میخواسته یه بازی دوستانه با کشور گرنادا که کلا ۱۲۰ هزار تا جمعیت داره برگزار کنه که لغو شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91638" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=AL077hlcgRvA8APh5ZjUiDtcokCdceyknKtzeiebHRBbRMTkfWjxLeuzr135A5il3LqFMUnCrzHyqSn3hDwZ1uQF_zi0i_FGErRcos-TAtuQ2bhy1RGM2B7C3XJJLHWivyAjZIt2xwE_ii3bi58BD1WsyQjlTjv-hh9gccvnlqoHQdlNK8yCOrXDAdM_qTzpjUOYZNHZl5Un4TA20RVabPyxROb-LaEFQDCcS3U3ef0G_oWANMtpG4GiiGl8nuN1yTREq_hVLYWNPQ31mvz7qcviQorYsZv_Wr2TcFnDush16NTKjcWIUMahBDKFk-kfZ36PbKohh4Rj4G2uTbbZgH3cy7Q4Nt6CRJn-ZknirWXuass6kbqVDxPpu9RLixKGdR-s9YdrtQ0L_jpIP-VAJJffeJqKtc3i9XS9vf32Q0wSWMfZSGB2JqD2nSgUKA2zIoXQI37CvpZFpWWK706VqjYGuCT97SYIxcRcZWerCpqNMjTIMEfsZFc6_3xO_WJ0mEWdCOCyf-BQ0EaG1DksTNuTtvOuKectABqeERB4yZw7U46O_83yje3046AVnU3tCWVOQ3exDF91y-1p9FPIywbNaiZPtqwZl9YtBfKHRwD6mDNaVi0NOg8v_aMxGYu_J1Y8Wt_gq2Q-Wl9FVsGparnvpkH9tMJB6QXyy_lAYTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=AL077hlcgRvA8APh5ZjUiDtcokCdceyknKtzeiebHRBbRMTkfWjxLeuzr135A5il3LqFMUnCrzHyqSn3hDwZ1uQF_zi0i_FGErRcos-TAtuQ2bhy1RGM2B7C3XJJLHWivyAjZIt2xwE_ii3bi58BD1WsyQjlTjv-hh9gccvnlqoHQdlNK8yCOrXDAdM_qTzpjUOYZNHZl5Un4TA20RVabPyxROb-LaEFQDCcS3U3ef0G_oWANMtpG4GiiGl8nuN1yTREq_hVLYWNPQ31mvz7qcviQorYsZv_Wr2TcFnDush16NTKjcWIUMahBDKFk-kfZ36PbKohh4Rj4G2uTbbZgH3cy7Q4Nt6CRJn-ZknirWXuass6kbqVDxPpu9RLixKGdR-s9YdrtQ0L_jpIP-VAJJffeJqKtc3i9XS9vf32Q0wSWMfZSGB2JqD2nSgUKA2zIoXQI37CvpZFpWWK706VqjYGuCT97SYIxcRcZWerCpqNMjTIMEfsZFc6_3xO_WJ0mEWdCOCyf-BQ0EaG1DksTNuTtvOuKectABqeERB4yZw7U46O_83yje3046AVnU3tCWVOQ3exDF91y-1p9FPIywbNaiZPtqwZl9YtBfKHRwD6mDNaVi0NOg8v_aMxGYu_J1Y8Wt_gq2Q-Wl9FVsGparnvpkH9tMJB6QXyy_lAYTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از هواداران ایرانی بانو شکیرا هستند
🐸
😊
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91637" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🏆
🇺🇸
🇮🇷
کشور آمریکا خبر داد که تمام بلیت‌فروشی هواداران ایران که از طریق سایت فدراسیون تهیه کرده‌اند برای جام‌جهانی مصادره شده و حق حضور در خاک آمریکا رو ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91636" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2iPeMczBGKYiuN-0Sq6IMnNmsPcsBcd3ABxeIxJTrOVMIsL9A0Lo0TvVxcrsOp-DyQ0vyztdDKQTD50EDl5ER6zgDhPo7xsnlgIFDvdvCfiaVfppSys7AMuHbt6hjbwz3yuTvoyWbzTYZRn13u0wtwOKUqaYlGEqqyshz3r4LZOSszLmESrBMzzmTPllDy_9qdb9Re9219ZqKwRUASu5cSdPtDXJXo6LOYEBZuZ9-JmTrA1i42ffPQh-7TNTvM9eKsfJqGqpnQyBbWHyCKEUwTjRQUOvSAnI0ERDfibg8N5seNhqdMXyIiRgh_kgtryjK3PnMLOBOjIs-kH2HiXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه مدل موهای نیمار در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91635" target="_blank">📅 09:52 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
