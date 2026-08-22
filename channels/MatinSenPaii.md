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
<img src="https://cdn1.telesco.pe/file/RIW496k3-CEDinpz_3jaAvV75Oje2vMkXXevJ4LPlH9g1SwU7_Xz8JGO-Ri4cpaGCIewopCaUNPqEk2QfdTL-CdwVc998HLDZbQMEExNsnCJROj_J5n5JswD1lKSBMA44myn9tVirkaGZW5CrqvxBVzypOGNrzTXSBZv0YrmekUkpwcZk-pcyzHgvQ-5wfq3A0lKZULbuW4xWOf_EIvmEPSh5CvJdmJuyK0e_X83mm7V2IX5eHNuwwbpoOrfGcz2Fm-VtLEhszrdczA6h-11V0_T_uquRO7pNm5sVAoxVVg-5Jp7FzFLBJv-P-DmgangxskAAT0TWSfuqB0L_zRtzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 22:46:28</div>
<hr>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NbBfNEsmMklYXmvEelsSQijRyKGj77jgvVeFFIA_JIKl1qrfBsbfmAIMGjEodJR_YOAZ7UqpN-pKol-QDK1FDwT8HLwGhs-83yhyCpNi2lsT9WaseYIfV8zDiotPtrLyweGxsspdPLzRBqCwO3ETzvTcxNX5N0I6Scy0a0Q6R604LnlYcEa_KoiwbmYKMXvEsaX1zjVeyiV5ssSM09wpdZ7J7r4g_xtgVsf1ecsD-OxqrdVrVB8AxO1z1so7h3S2K6HrS2QVZfX_GX3cWTAR5tKyHMqDXTzabnj74w9TT0AM7anGcYshIqmOW9snvVh0TcmpufjhbrHFVtJZACtTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hm0yTdzOTeXhndYNWMt_XF5zjug-yOSBHKFd4_t9H4TKstTatijJl0F8sQiZoEPi97zNk1MaodjQCAJoWYtGpuixg2fTNijEXT48Xqb1OVEC2yu0WpeWxTJ76ClSgBPA9yhyNJ2eqT_rzr_gJWGZebMEbNxY4AaDxvTNdhcn1eD3H6OSEuJGc0W4OIN0Gwf9bgkxUdJt-Fa4B98L9-_wuGtL62CNunnTDRQuCeyhMf-e0d1Xj4eFUp1GynTa4PZNIPMpMBppyE-V5_g26lLd5NjsFpVYfe4Aab7422m39h4YmyJaf_tW2ZNczfpQRYSkCdP5loBh02t8ZbgE_6uXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tVADmiuXs2MsHHFaMwNeXXefPMSoc5Im847Hiu-nYqSxK5SJv1QZJh6neQg6mRSNgqsM-pQXOv7GQhmrYu4GJ-XuUgnJAPW9uqmQ7T0xfZw918IL43fN9JaqTRlFQKtJ6Y_--A2TuhFJilbpYAFW3eSm8EawvLrFeRpHAN_C8B6hAV9szNRv9-CEmMAw-A9O6VZroFWt1eHqYGgn9nWvZuTn-sy4rzY_yyyNLkMqJbEPWYam3KOV_pEGR1elxQt0wgEo7vbuufbZj6AV0g0DdNT6fSNNgi_BiJtR49fTRGgc4TEBFTCvRwpnLi_QYnoky7r95edn63baMDLtLxLXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/te5Ge_PLZWMLVAvnyrS2JC8bnijsS2Q0WYDzKLwHvEJ_Sg4eUiAy1uGvx0ge-ifU4bp1Tn-dsWb9uHueOBgowzoef6OAL2H5vOx7r9BZQgS8hlqYq1yEvC_nWWRQNCo3nL1G_7LaBZx6bNbmRk6zTW79EI4HWNlLOAvaDlcSSFPfO9WgRW_J1HmmDRqE52J8lh_mp_uFOo0MDa3oqfnPa5zAShhfzwdjnjg2Ra7aqvpPbvTJlrckIh0cdyLmqfeBLFz_avzlu-eQp69S-0j6-OqnkCUTp5pC_yVnJ4XKr7QJ9ciEfwVpWB6lu1TEWQKCIbEGB8f3PhYGK7myvn7dUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mrUaAH3m5OOajGdshWwTnNKu2sTrDZwAKNSwWSrK24GeoGPnyz6aZoslsQIQc-4nI-11XfIdBFEPXFq1RGnXLneAoaD8uB-dLVZo3PSS3A1pvs0W1DcqisBwoYCghP-Ew-Q79rvi1J7TGFDlZ9sk1H0wvFejIxoQHVHO8_p5HxHTT8hc8gAjbYuLQiuUXi55_8ppQiVNa0_2zCVYVVYJffcANj8eoslpn7FhZ9g4XcQ8u2fuc-J288Q2QEYgruWF_m5ihD43eH1SggOo96qSz4O--p3cMBkzmnqPhPaHWFI9FwkoLxMeBo4Kyjro8H6aKpqZKGBQIafuv4pXfEuyCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MUp1fQWPaT8Qa4PL8AFksuNey_28t7v1A2h-a7HW9PmknZ_fiJYpEdfUQAFzXdBoUilxEu7MMzctecn5Grwg1a04UWS0mVBQEVoLMY8cGYFP8R-dktY4JOlcqi-ZXt_mIq1nJ11Iea76dSA-JoQtr7dquYidnfvMmSyXnK_V5QnUXBvwSP04h9NVIsPHaiR5bu0MJmx4XvHLKIA4mMvppiZDHzKR-a8G-5xiTdIiVuDYt4krF_yWOkiyXAzrYlZoPrTu9ZA2RU_vIrMJrBIavaEkFAOFgXDaMJ5LaLAM5B3Kdc0Is1TklMR1VhW6azeKEC0WGWcRerQ5LXzWA25MIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XLH3lkLc2IrHlGJODjEBAnC34IZ0AGDJtOCni-5xqxMTTPEsM7orDPKusEdx8JztMjrG6GYr02fIMC4tSX6Twq9232NZf1RdJO0ZSCXVzu2gAPpZNd-qFldm5ki-C2BBh3oqkpEzSST88HmXvFHIFYEvbSG38KDF29x5reL1Qtzs7DKs7oqnMQTFpCXsq263wXc5EhWaQlDjE2-KUb7kHU-cuizeJwGs1f_LS60DsmCANLa4LmjN3dKrj5-CN0u_k-awzpMeqA7umdoYvCFmCcFXsMpXH3NmUeuGH_P-hqNovYLeW6Wj_Ynxu7Zbmz24BtVkVPookCi3ub-Ey3yX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UO_UT7Co7BVM9rGExnMTHie9FUb5bhRrmBh-uywTdDayZgCkYnrIJxwhnn8CwA_ycn0Edq8bdRz2-GNZsFgEKCrbYBAg3_bl6QV-9J4DawH6wObJ7j8R5x4Y_jk-F8g6VHTp435b97e_PRiwTTdAHtcgeuh2mIDRD_iI8Uw5etaTJd9jJk2hgREBjCgJjN-pkltzT91ryq-IKDeUu0Ee1K4Ca4zxymR9DSI3ZQgFUkR9TE3cVJ0xxtCqHfHh6ji8slIrhoUU1ADlTfPBEY4paYCXN_B40XG5Wsz7bm98U4v6Mmztevrqj1NoaI2FyeG8xgTy0SxUZPIVBLJfV53xSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kXrVnGsOthYxzSUeDee-X9DfKQPBRVMvqTg0AuD5wueSt226PyED3FLx0HfLVQcGi9E7ZviIvXR5p2d_yU0Ko782cVvkbA_uOt-FbbcxkhjKmFPEtWpuPXv-v4qlVX_FtCAhrNw__F5HEZaFOzNa8oGbMdPmJubE9cXiy6RxR2wV99BjfBNiMwl_8xbCKat1N1KPWj7Jt6TzCcoY4R3LWFWLsrt9603Og7EIsiY0-ofGsLce6we7iMGkwuKoKA1-2LikU4u1LVmq_1RV9bW9kFvTzTx_ngc51ejE1IqUpyDtHw1Srmb-EAqGKG4Ibgs7WwJngabAZCK-rSysdSjTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uby9svQxC0R7BIUoiZe3m3C6fqY1DL3Z5R4oA0vRinKIV-dRq1pIawN0f1cVDKKMXOozvjhLFkoONCLUjia6HMtL_nLjqwbte9z30F9B5ZR93SWMkhy2UqpxVZcaonOpIPYIeoc-EHJbrGq_QwWuUj1jrJR71CZ7Sq4sQNnS7OdusW3HnmWKWiBi7SgRr0xWXO7Q1w_fHj6IIt5_GeDmTdusykVoAl85mSxoXaTti4PYtb4xa_IPZzxdTq7W1K3c5shEwphxeTfBx-ao1-eqAwpwB45ytP46CD_9yJ1hBcwTl5xwSGjwh7_xz2oMdGixra-_5_iAiSzgR3HD0z9T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gn-VATNXdEAS24Shrz3J-5zQwIzw0T5K3n_eg9-mkWAuMBoudgdqYjejOUeEcQfH5O1Mlmxzura544I6i-eVFixo-xUajd9LQUeALEpXXMKEFjF9eZfugOWPq6s04HBtqaTjzegRkK5aL5tZAc--1ekt6vHWdU6HWsUJLsDRyl4ddmaAIqW_aoK98STlDIYV7SwecSTfbsoUyuDGm3cDzz8O8CAoAXIPQq530jbt5wE5am0nBMbNmdiVujEbPNtBk8kpiHiiJ21hVXUrkSzVoT6Cu3xJwAOJV6-3sE-c7iEcvQlyOUUaNqc9p8CjVxRo3GDWnhB2hTHF6LvAgXKXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lTBUvWNa6hu6mU9xns0ZFNUEuhOSCh_4vA0Z0fPmh5IZziG8uGB5zXcwlO5DxzCWJXRQyEPzi7cJ4SmZmFITaZrHRcbAmnAxaIYYLbaOueLBv3bAjG8CpCwSvf2WIVqlioebbjDs2H_2WCaYZxdF--cL4gkndsebK5FS8QKUO3qNGhhBkfAaCovMJ-RgJLFDQ9-i6bvObREt40Hsdl0XGg_lE7gwHsdYhHc80hc2F2R5ODIPw2yDddVBaAzgaYUhXPc0DTtly0LRQulJLp38Gj-44Gl3k1rOKARdSIYd4SX3o9m9NxfdSfCLrxbNa8E06z0VT8GuM68TfaOv85xa8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzES6TmbWAjoO00q13NqXMLXMKTMedrcJgbQWhxD3srPBUTtCjF_iC_JbNMUGUM4YgB6kwG4INGKCnLS2NwZgojBG1V46psq5Qjz7pZj2QDsfrPCyx5ovcRdu7hUyOkQIEn7dYxE7rHnqf9WZxQ2uo3_wbqp97gNXcWgsCyrBOETorLGnxpnDszTSjXZk38GzeoRyZ0tO-rUTRouqvwrUDm08-2msYyRfwZB-fESEjtLk_QZOy97CuugelSsGCv4yGYyCe9xeSakacfbWixMI2Sg2tTQjZfh-9SDDGgJtU7RJ9u0g5KlBvuop0h2Gjpb8aQ2HetZ6j3gr9zn23ArOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7jZx_fG_3cYZZ6lbSoxp8sc0lFMPdFdEFVUh5sS3OrerMFKiOVZrYpNFhnme6IVbSgztxTyex-YBprq_CNXa7iq54XyWUoO0S5ZDE1jBXCwXk5pp557IL0RjaiI-0RxIgbIsD0PUczXwqdLFkCios2gOs0UuvgcIVuDm4KSvx9DXCKQnFO2RJy9eDo2s1EWqdDPUPLtGX5haqW0ThbDQMyxRi9JrrezcsYbsAS57xDI33cRB6APyLxCBU0SZZ9dhmmduAyC8JVjmsLzI4hvCJsPIAToiuLbWZ4JO3y56hi7UGx4uI3jfdAtZScmGkUQvzJeHw5LOYylQ3dXurSN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lSBykPFfNN5tPKNpTnVk5XLJ2T1s6MsJUowSHUamkDzoU56O-2beZB59s0MK50cPK1IZ6A_W7TE6dxwq32RL1DVMK615q6529qQx8dsjlieq2PLHWxJjNXGWnPB2SVZKtD2jlA_CPYmC8HeJAeuDtr5U1RVXuyr3fkBcMDASUJDj1CdtVyAkgNJD5RajYkKLcZ8eqhLx20AjqXWdAL3XduN4USR65X8Wik15HVqJaQOFlM4KWHXbWjx8Pu8h9QJdSOH1I0jzAQfL9Mqvhq80o9M0aaO-znGE3sgWvj6Xob87vGYXUGfDZkel9n06nJ3iEjTLf-2utwnuFkdid9T7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H0VXC_N9NRClJA6Haoc9HEFxNn5WemK7t2uxkgz-ScE96YVIq_aq3K0g8qTHZgGiVkOWIM6CrizIJhu1-JmI_EP2s8gQZwWMFzXhQ5ZH7pcS-VJz-e7HNcJyuA5d8laM6SYOBhlDesODrvimiq_aTAsfSBGrCCsB6xFLBYmWzVaSEvZHhQ2QyDLu5wW1cPc4i2HahQEdqZ_fB3hs5F7ucekhB-WlR8EmjjM_b7tPCRv9Kf7udG0T1tMD9Kfy2FU20gSIm88_D8_L12kO3Ew2uer8gKPJFwlC1SnoYIcgZ8cIOLFXcrHskIGpTKJK2BkpDkocnTb5rrgEgaL0FYihzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FpPPx6O7Edg4R6YntrnH9X101m1YUAE08BBZxshEixY_kgnb6vV4zZx4kiJPq4O9mmCWWyJi1FKHNtuFGdOth80St0W3p5VwQf138MyRNGYMINZJ6CycpVt2HHRzhEZOx30hECHl_GKNM6_x-0K8tjgu_7p7HcxHMzNmByS-f0my0zlr2Av3SM1yJ6D_YXlphgQ0Ng7ErjuSJRwReXXrTKFRJvXq0n6d9bUNhx51yMT_GYJtJU9-f9Gr8eBsnX-Gym_gbQTWFBIMD4dgPCclKfpDzDyKdv8l_ILASg3etfn6ik_nLZ8fTVjB_TO6KSe23JxKskeRxAlwtXR7mx4cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZmVs5cMQoWY2EHADxp2nmkSogdFdUWXiFi-20ud_cVITdLjIfjmk1bhsUe1iRxejAT-MZCqhLy0ROJj-e9Zn9TYc8Fa8COboghtU_pPQWavF5rDnrhuEflFDmvSJkMj0oyj5NUYn9giWuh5PDa1g-Jfru48GgCjP9etb4q_gR_xM-IZfFourG0bwVcdefW5MBczDI4zuc7x0C3Rs43_a_auC2b-86CIiCWgE0dL_o03X3LRTqNVDU7RZaM_mr0n72LJylbXXbbuiVhoITvqqEO0lYUfECKSWXPwMBMGyAy7_1sxkZ2w9Ng2-XVvnD4Dh4ve4I5yvrZKBTereE0p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D6dsZDmIAragbG3nXJ850z9qpZVySTV4YgeOFXdvhmdQmJgV89TGjbDtWynAlHcAYJGNU4io4lNw9WpNwO_-UojON9PGEPGj7CA4L5ky_-iTiiBuK_ENTbHrsCuxkOeEnejoMuYBIRklPNcLm75ucNfZLGiqPN8WZp92Uxb_wTGUbofx_USpOqrhJqL_I2V-p4nyCiMS14aJqKVC5vxj5_io0F75yJIj1VN7COnV8JSbsNKG5tSA7q7qKXTDUXwGew8qiXvNlK6zptJzFq2bnDWJ6XwheYY0GJQW1P7WJf9BKQH0CP1dGmFaVtZmm5NAiwgDq9KZD6bsdwtDf24Unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/towcAF6ljgFjumWZGSffnPBolTjPNuYy6rnc2kwpc213hqZ4PBJeqjfBG9LuJ-h2afJ8eU1CmXkMSNQVq13OtNR-3g0rz1WIY029F5zKJZPz72X7v-fzMT03GJALKA8FSIYdwy-YTgOcZ9Xcpp95Nha8x_smAfi5PJ5_JWJKEm2H9pqNkLjmutQsvBHM8nYWBYz6lwLxXA-Ol37Devjc-JksvJQ6IbOxiqh1CeywZoXcCoEIbEwxTKunua-v9qvsHSqbbgZz_rbUD6XlHaIkcn3JQY1z8uu-EBRX051mcCMrhx9qpUEU6BjiG3U5SKgETZqRglCRXXkhmbZqdABSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkXq5q4pvGNbeTf-sbpuQ2wA2M2GT1ymt0RImV3YNuK7WzZ6t4hYXQet_-Ok7AYO-gtiq2q3ZuZJCD1uHGrYevU_0k3UCQardd4VOeIL7YJRhTOS0YbcSIz7rAJOv24AknNJsWdzSYZHX7c3HVCJUmn74PT2qc7eHMjv0-UEs_qKLQVtxmuVhUtgsPpN2AbeZdJ_HJuGB9VPu6Wd9uWkh6TBJWJtUNXxcjvYXrDzCG3pDks_I5sp_C0bZ8bVZINP3OGDw2MH1nM4iFNgMW6PiSCXNFRunQpHOM1gqkpnLEcou6_5wdob0Siws8ezpiBFtxGC7Y9hn6JG8VubUY7Odw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bT3cUNvYLINIKbHxEHRTW9oZBvIJvolKMmLkqt7pxEpgTXXqBU1FlWGUkmByk5y-pjGmt91iccS6-MtsN-r-obEWDV3fgKm_KBc1C-ZEDhV4nS7Yx_yOeuxkeYzcziAabBMOUdcBmCxX0VCGLaqD_K99cZvTPJDKt1lRHzexMMeATaMYQ2Tvuww8UNefh1VMPt8wnM19KfYqPAcfsLAgNqIXKCdRvKxfYSio3Dv9LfBwnpaEascah3cqh-gGQXJM8z6vDZv20AhLvu5Pbc1y82TJVAMj316YXunOqSuTBNb4W34rwrX-ejMsiJXyzpFJ9RFVnoZaStvQBJ0H4k_vAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_WYlzvxwd5xEiUr22ZxF-ICOquw9HUFqUbcoCY4MNGZkhlFsWIjHzXWQdOnTa9Mx6avK6dROKWAp-t9fZAhA1paDsTWzpOOJEK-hXadSYrfMhsV0kYH_UyfkjOUqy7fBNY2UrEsCfYyMun3wocl59JYaXIgQ1JyuUZJqwAvgqgGWRnyziSyor4USmokmfCSV3w2oX-0zn_kcNRp9264Dm_clmTOjdQlSdiU-QftV3ShtR4SBf73Zuoi9Z6kBiwJihqvzdTswAUMe2pBUKKNBOASyM_vrKLh5bXx9kTS9jwrBkONT8Z09VcIvplmEoxVFneNbHyxu7opZy_AZDCIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rPdQULg8CP8N_EA0m1NEsgdDHUI_pPf-KVupEipdetvek5aipHF9bxilZFTazXnoyrP5UW1Zcro3aMuKN4WUIvhO9UgVyuunI7nM8qcsvLc4F6f8pfsNinQQWPL9fnjZObcz_BWuAuENLP2bKsgsCxF0nzjmGsg9wTDncMbineA2xZ8vipTYMYW_44sOvfxH4wZoOFdkKA-JUnnUirVCLDZdQKKkjfsfSWQFeicot15PbUvfzPhqL7Lb1XR9M96Wk-OpM4umv2NKavWySbBN9sAKDXatdvpLxVC2jb7o_-nCtXKzlwfpHT5evXXHF8FLpC8RK2zPVJLRy0G4h-Likw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vlHz5cjIxM82kxxazOSF1ybSRdnhAf3-kYN8SYpu6Gb1jGHZdeIYPeS3iO6I3rBeZRssBL99nChJczG6J2uB955lxvZ56T5BR2Gqd7MwEFjtfkLBU3_engzrd_o1B54_OJXVBp8JeSh5DvdJDsrv3IOk-9VFD_iKjmaIGydi6NwBDSUrC99p6hGOvnCT-7gcUyiz0u5gFqjbOqh-FuxMM2qBt9N9JWh49CLhsNCWH-1C8_FGptcDDVVX9ljNWR90jFsGbQoCWYMXT949TbVYM4DIU_AV8PiXlwj98PiVwEnNOi3fXYmqv3UAmnOBa8Yc-omxu07dyCZWCRl-gSd0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fVEROHs6gp19__YYkDgqaPIW70_I7divgG-hZr3kdzMlo7uQJrZDCxBP7BQ3GrEJz2SaBbxj0CtEBvg-N_6R1VsSeLozqO2zJUsHrQpGjuzEVusi5BILp1oQ_0_gxDpVss4z_G44XFRVKXDJhokYDZLe-5EUpz10fu39_fGWKnQmCWzd4NmK0NJaA_l4kJ4l3kECsYXnSWh4ranYHLiW_GtNPkMPsKjGSnbaZtpf_IBBjdaRfOyi5HvLlvaOY1iDh_h-GcKDP23yOFf_sQb1Rbv75f7NIK3fQHO6a6q9He5xnypKICZ90mtvZxWcmUTTXfWmgWrr4Q1vZZL50ij-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PMZARRkNb7faBBWKrrORdydiqqIymSDFFQMgRTrl8VPxK54hyUYyPoXaWWyoYVLiXOTK-u5WguymfGnMBc9Iv-FxQXpFS7cOF1sTDNT9Y4MoowuFP2U2OrKX0UIIdw2M69LBSwNTV16etKUHwgFVHRQX5gtCvQi2fRYgiQmCYjqaKoK5hUTx_bugINyy2wj9NamIoZ5BCSeJYUmh1dxElm5pAS1lBcglGZmYrr8_-TQghsQEv0drnqeJxuoxhssD2M0BdmUdSPNelJuSDXKUqbdQJxGfjmjm6JlIAuPPxU-ZC66sTGqj2hG7QeO11RQHUhQzGidFDKXsJFicg-hqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tVLgwk9f7V5eiUjqhRuIWoR3AQtMddeTu6TO8bv6LiRUWn8UJKCcTxw99nFE3CCGCZ3f5bp2T5cAOBqErb5JMl6jka8Nxs598S-5V-xFJ2dTfYQU1ZS3LX5VOaOhaDP8kni138LbeHz53KpuqGN63FWBozB523rBOPkngCkQ3JFJrVflXrAQ7WwaZ_2-Vf1Zab3rbEFEKGGFDaASSjmxNEoPLf3cHJSFfD3--8otpbcO1KrN4BVivmQ7zI66Tn0WAbNlwn0rp2EZpWkHH9tnzYYyEqtqO53Xj_hyF2ZVH7f4AluoHYU9dixORuTbW-Qev0mwwVsZH0xAb2OS8BlM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXWVISBG2U6jglS6DgEP5l7FIXeepWrLhf_GompP11aLpUb4rGL_RvuAvV4hU-5mDWlO4QQVFVWCIc6IRlSAHLbShUe4Vmth8O1-dJN42l9yMYR7_7eivnIbc_zVowlI4w8K07w_QyQM9cFa0A8RorBQHmP2LT11EZzvm3T_7UPQ7zVOs4FwZI77Ba8MCNgPLOHnZL-JxOkfKGkSu9dHXyr56Lw6fIobvNCljbAyM0QIbivnJWK8A73HINwmKo7xTNLEsESgmb084pE24CCcR0UblQGSvf1_dwFD8yNyNFRMyPKJXFfvn-VyCp_4cc5MaBZogQOm7Nt4md0IHfohig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=L_5V8FTNt_ptVzSP2A0haK4EFY7dq69f4UATtsJyRI2XUZj0zzbPFJ3gxWsYP8sCZTkvN_RrBbU-PlaB3rIgwqvO6CiE-2a511gUZ_xJkhHHyhgo7qaVt46sxI-u3fo_z7HIs3QE4cLrlZMTGtKcuPso6qu5mtmIOcI1iNI2sgSskSecVzHzegs9r409cwwzBTHgNCvFtPXE0oMwz2tV76JZs5rPGuHgkp1kmD9UZCP86SLOCRU5zp5_FgdSzeLcfoqVwVr9hKE_qHRUt6Vt8NGqi4KGmLTHa-2IVGcXr3CPgOPXGWpuRUqaLN3URvMVXYndrLojbZlQe0SDpJsGlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=L_5V8FTNt_ptVzSP2A0haK4EFY7dq69f4UATtsJyRI2XUZj0zzbPFJ3gxWsYP8sCZTkvN_RrBbU-PlaB3rIgwqvO6CiE-2a511gUZ_xJkhHHyhgo7qaVt46sxI-u3fo_z7HIs3QE4cLrlZMTGtKcuPso6qu5mtmIOcI1iNI2sgSskSecVzHzegs9r409cwwzBTHgNCvFtPXE0oMwz2tV76JZs5rPGuHgkp1kmD9UZCP86SLOCRU5zp5_FgdSzeLcfoqVwVr9hKE_qHRUt6Vt8NGqi4KGmLTHa-2IVGcXr3CPgOPXGWpuRUqaLN3URvMVXYndrLojbZlQe0SDpJsGlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGE-hREgE723vASaYlHoPxFVUn4y3Ab2Weu_HkWzk2sj0mcY-D5351tHB847GKBmkdwS-ElM0OAmRokvPfgFf3JS9qodTEoEgpCDilIJzScgT2onsdnZ__RQ-tSbxqYniwNkbHlQxecg0zfCMIOYazYS4OJTzont88MYJ_sluUGt6iQ0CrQcG-veXI0hFbbDgPbti6ZuCJWA3TVYgFm6EplevOW9QUU03_vFpY9UJQ05UuNlDhfODWKPrLugdrqC5JKw5ai87WRsrVeCKIMp_56K-XonAWLvsogIumgKUkjRA5K2H_yFNwz2AWo4jRwV_W2a4WxCh4pKZk4-7Y1PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jwUX1z0kVVcbP3nuwGk7ZHVFm7wx1oNPg7TcMS09kIe-JmONXl8vJtGtXaaCeRXectfWqiBmaEImagmQjRMK9s3tiYvg9vayXhMLh3TRYNwurAZ1bjsmnNTWkqpUYarx3nihBYg6D79mqjgvDr821h11cTCoeLce6Fn2ZRRFy1JA7Xa5r_6iOrxf4X-5QwKLjOqpwt7CUH5YdB_xABpQIJsGIVdzYtaJfr_qTOrFqEM4K8iNSshAf6sMNpJeYQDMsi0ooisPO31pIIGvUZFnTNmmrPyMaqv0NZAbid7s431mgTpvywemV8Z4U0jTWTQRsgwGIRzJfMfldjINwaukXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BqDX2oIEAJuecYh-gKRfwWhYzWFInhIN2WvJqX4ZP6p4HEKSbsY0HUPrv2IPyC1pfdtke6FFbAi24Z7OjdJYnQVNybC8pXCxAw72Pq_Uomk49NGk6V1IjqW3EQOWebFGG8IjwfGyzIv9fJUJYXIg-HeMpWsrJToLdt-9WrLG-gZJwb6Auc00JLBENRIiDeuiX2SKKF86RiMayOYlaVpFPoR7u6Mn2VymSK7aAVsVLvCRSpjov8PGnLcYmtKJoIXj8yI7cnpfeyYcQosNQswKiFrs9MtICzNjEkUvqBhWjWIdMorVAMR7nwNnV3UYnBFIwjWJEp37aozmQfCyIT11dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bZaHLDfUs34axTkVKHxx3xY7qvI4xqcTWYKq7R-rhHYhgFpEAq42C_vCYlsaRfB_kue1L4X8aAUAHNw4MOJS8G0psPgzSGZ11InS43V5b6SBxvqjPjc2aTYrtjXlHEW6g3GUaNC5eYeEeRXyJjoDadQGQ3Cu-FaDPnLRI7183BWlYhc-hxrJ4V2TM87eonmFxC2xoRBe6Dh-odsHXeRyvXL41WaPNO7o8szjpnDvIX9qmtBknepeSaMEBmOT7HcEKkGo7kkguOBa4egVjrHMS12dw9jVeIjlb6bUIFHhh5j_teIGxWvZQkuh5PjW1sQD7zq4uZpYaWrAcTYdLogfQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvRQW8XN8Qf3Hzf8Dr9CfFqVYjkLBSCwACnNGC5fOI8_qZm4rA6PQ9-Djui5-9RbklOePTT7cmGUXUmkQ7kJOpNclNTIpnxS3siwkESR5TeLHSuWKOFbAj4pzWBc414ufcYe02zmv3hI6xEFZd-pUG1gryaH8Td8aCFVxi6FdhXyrulKPcYJveRIRhK0l1MZ8-JeHvi-Dn8mcZFggpoV4ywbKTlwHOCEn3s1FFkvyTTweA2PydAfrZMx3UF93dt3kwVNFa7PaGmxMQr29cn7shrPy-Wkc-SVNmdpPk7g6uSekanpJeGzJf-ns9iF7-DNYn_tPEANUstn9AGAPAVEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-LCxi-rNoY8eRn0DLo-EXSJ52Ta9tXCg3x88krhYFvICm0oh8X-LV6F3l7t8RyAuoUFXN8769kS2Cs6ijnVgqyUEKv3MHKUE2EUy0JbMGZ21eNsgmZWUTRyze3Z20mOP7XUbpp46W7hwY03sha5eCy9b13VGffwCdJv_H0OB_C6L5lGAVB6mMe1whNp-x_1MR1WttbJ7kxJRJWYSHL9AO-2u1OpA8Z7YBxJN4gpB5dWcmtgCHVFXLgREgUX2AEP26BvyjGgvt1QFWgFkSRqV-TWRReHXutnlyAAU06v2HFsUAoAQMxHmg485Y3IDlmnXbORwMd-ju7tclwtj80Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XRbRIxM0HC6YmJXer6uHluF8xIWVN4aT8jSNcRz62eADBN1v1EbJA4efCZyeBsuXzReUlQtbnaXBq0_JCRMQk_AB2vabDextRU_ac8uJMcwbEqF_DO4itj6wpqpheowpr02fp3bQWYnMdOiKU7QfDJoXUU7Ka_AazNn7ezXgoRZhpYJH4kacQgx_C2GlG61Jm_OsqSM_LAGYQU6kQ_aik68Axnsnn8s-XzMO_Ng9LD3Mp8ySiwBusKhlxnB_2J0QPYWyCl8O7K3k3sTDfHvis7X8seV3gzXEQMDI-bP4sYVob3rFnf9KDPTYnJFwCLvP58W1AY271l6_14IqUWu0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llAc3itgsw0GmhdsOOVc4Y0iexRiXGxpVrGU5JB3U_rrcUNuwyOYjR6PJ-5gwz80nB3V8bgB3HMLp6pyrA5wVhfHdIu5iYq_CELKCrLGJufUBXUuaIW9NcXHD9ekyL1okWUADej2XRpJ-LZiBADw270yX8VTIhTn_LYqFxxaoL87HM4uo0EpEWPQ84P6NjHDDwbfM2NhgQMRFiuvW8_IiobPEBJzue--9MVDwQzcUJDDZ-MtbpqvS3KLDy_bTGvRzNvHEdQohtG7zKw9EWvAAJesGPNovOQ7Zc8tPjLAuEvC0A9UHLn-TcymrUSN8rnsjPPwGoI3P_60Ay-BFUzoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfhsESXPR62bJOp7YmR7dj6bLgy6c1hYn9OtAGgOhbfLBTm9N4h_XI4bBNN_9Mo1lpXMloq8FjXtL0Z3eoVa5zYcsKk35e5hkC7hvpeR-2zFpa_c6SbV8P6b_w6P7K6DLAMLs4hnAwgqo2yXk91UoUnFKB5PlhiPTph7RRVAlqHPz4Hlr7Kk5DaZdrcW8fdaYhji4W6UFGhXDTfXaeE5IcJ2zKPGGqaZnL27AAUDxSKWyvJfY6XI8-qViAMCdv4yBzhnxJ8EVQ80cNsmLnD2tVmSQvW3-eOq4MggZiwA20qni3apBiJYeVzMOSo7GgyeK2S3Metf733UUy5xYjSL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hd9fgF1-0blBeHq8XLkfH-KnPddVsB_jjeEivP4xmzgIDQR6xQE4wTIZ7HkmkFr8t5T5m51TTckElhJu72owalWnVnLDClY_LfUIp_F-L7NqL2f8mmPHP380GTWA49QzN9tUknsRL_qM_QG5IY4d2QvgP2fTtK9RfSIG3ENrCuZeMHIRjSB8aIlJL1wmr4LZ8dupM_uvspd7SPmAPKBwknlBi35G4yI3y3OOx-l_yTrY7i-bCI1NJ4LQ9mD2tkkhaiO9dJptMC6fYkk5mkpxmqXgGa6moLDPLdRm1FgSmij3CGAwiE14yjLe5ct6TJBXVGPop-zu42lnJGjMNHw_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OVzV4fusZm61SK_toa6J34teOy2e1okaJZj02VNsAJYEbgOQaDFP0D0MprEbcgMPKnDYxjBTOiv4yPwhdLqV-RCFFYSAYuYJDAHNK6bp8ovgcshC6nd7b3Nl1n-693XbbyBY078UQkwhwctgHwQucEUtc9Aul55aELlaq3Cs2R-ohpgqFjAkRBgMIlpuQSXB9A5v0dps3KwYPHp8FEQI_Z-QmfZGR8CvMtmMhhp8VSYOhwQJdZKiM1a6o2u-2moN3ba3tb2pTQ4NxwCMlPHaQFVVbUV2c9Z-eNqY5K9SVKYBuxzeb_PfZ48_MVt2QtTp8sYJuPig9r9vUQbtbFR6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJGbByNv1V8YKn6es87-2F_P3os-cpHGm_NLw4SUVrpw_B4Z4uLaapKkDk4DI2AEF3ZU214F8UFWSJiY-M79nFoofYfq9_6EfTYH-NBdyn-wlnQKSf6XjjOK9f4nXJ4xC_dR5cTk5okGLsvqvLJpvJGE37z3_WmMQM10ApuVK8iSmY5d4QGWDqVteDsfAfNZs2yNIkXJG4gxNeVTu4k0mT6mPJpioyz0VLn8GNLmzXCttV92ww_va48Jft7eYiWc8QYefA8yDVij5EpVg8IIQ9Gjqbhog4JE8DoVJmtoydLX0ttpkJ1TbP00rJN_0RpdMPf_T_Hus-Kt9maXb9zx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cnHr6Cmv6mOmb5dQEuXjtVl6c6coGtUdOXSGJNPpZl2O-2sRpKoJMbEtgSAC-aagNni1s8YXHm6M0Hv76MhxGT0hrIfvB73J1CIqDar4_VDBbgYFWJQ0kvOAsHBPHzS4hGFI5gsTbjDGxc1LsFWliaLKAzLEjNMBrvp9esj4IhzBkFfDt6GkrmI8r22Hr2snDYWm1LG61j8cL6esRLU1JLSqFekrylKdaAufZ_PF2HOWD0NUufElvJfx14MDN2668xZ3AX8UhPdwJr92oAHdzcaZE-72V_bSe2EWBNviRxY9D-OEiNaJ47cEfid72E08sO40oL6BQ0wijYWK8ie2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qamPBhFMXtbJ5-QplyBqfsm9zgrfyYRQWfLDiDuV5nBmh8tmDafYkoe_-B2PeYM072ZocUpSEZXGb-NrcZ3cifxeft87hISewu_1IJZnHX0bGjpd8hI8RyIEpoJ9rFRUjBirNgC4hm5n2EOKcFGgNCcL3ne04mby7GTI8gI5BRnoagp7FSHM72GE2vi1tsI3oxCNJB5VjsEI-ruE4Et6g4uxgg-DnV9HLdweCDeL7PKCEqOeUUHcGlrlXOIbS99Fts1aVJJebNiiVBP8SHkw-I4X7zuT3-PFhbqi0wK45Jf66ticzNtW6pFEKxFNEAumuEPQ0YZQZ-tAfWzmy1FeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SZ8DuEkMd0wfSFzqpLa_QS3hFQljq5QrCe3NkrUtd-CPeyOAk2Uh2ItGW5JdgL20l5wdwC2SrQJc1m4g_W7IXr3EnawDfxC5f20HaOPuF4O5O9d928-557z-9nThqNxHkt_1Sd7ZFs-JCutipTDgBZymWd6Fk4jF3U3LKQm6zeXV3gpRsWDoPSDHZ9x4vPlcVxdE1uqMGTknR16uO6xwzIGRvVRANwVHLw6ttBsSlio9M2AuFLtjhFH1GVJFmVlN-atB4jcScQ-A5JKFF-9psRN4v7jPsr5zrUQ1yGOz2o2LQ6-5r4YvVij7WhhW6SGtKle1Yx1phOnG7f7UmBAQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpNuAKnEDSEJNEncK_A4X8JDxVfyIXuxR3PcF-xt1qNgesLRGsyfhJUSX8wEDb_z5O9P4wgCpoTXSZIOEcf_vynwPi-dsbEyFlodzYeka7TjU9FQhs4hDBFxCasY9ovwaslQ3yo-onxlH2uJSPqq_TPHYTOzyWxk_PvmT5PVpfmeDX6q6CrwptU2LXcoiLbCfXTxmbp55xlcqad13e6-twN-8UB46PoSd5yHm4NPlFIOpjZfyjASHPhf1wrsLEDeP9q7wre0RQuW1USLcACzKaZ4Fj52_O9ZwDaNhdHcYNcgi12NCQdh_Em0kyI_VtFANXtono7ZgKE0qrXnL8pjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlaHOOll49aDAn_sWwulsbOTeA2d9uEmaD554zJoSObqqJjopdu6ATQkeZ07Feul6ICsyKmL5A4dT0WjsQrHgu1lICYrDsfq4n3ldec-wI2DeTm11rKnoriWxTJy7u5oRW2AEaAcHQHjll6JgNsk5FqcN_-UazUzen76dhDeX_7UsIaCQv-sVwKwo1gCTr86G7dtnVUwwZogiy8zZbFuQ3Ewe3iyG2wPYLSD9CkHTzrb3KarwbFDbu1jGETljAodp2S1BQnKYH5gUXWQfQ8ds6EmOtZbIL--22kM_4esG2FfzEaiSa_79TohK27GFbAoTnfw75PTZ7niAZk03WjoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C0Q7VnN7aYFwN7sG10pMG2JErayk1VrFKh5q-tjpIVDy8cVnoYTqij6fZH75QD3z7lZ0kbH-7YjZ1v44IHT39oHgeMgARYxR0vnwK5H9DXpvv-db_4dBZuZs79SC9GQch0ZIM_O_MzUBwKXmNBDJTwyQVPrKLgk5QTvCp-ZkAFQAd308DUOJAupRhg6pAR2ExvSrbUK0dcVv7WVoqilxhuj5a1Z3T2QnnapljXotKs92x8VLcBWM8kY4VGSnXqcnFdArqrfMFd4PDrGDFsd7N6fIp7Bk2WqyUW3WerYPC7_4QGP1RXOu2n44GnjhFzspRle5c9GqEp2xtoKPcFBBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oL1uUj29jQ4Xpk8zjrMpcT4j6tjkomfw6Az47rFCVmh00PLRS5vdqOWO5eyCt2Sz6-xDds62D4fisJQ3OzysM119sYRuBq-muAq51fO1YBExw-Bdtnj55DDtpQ4gI76keXG8QTYOpJSTeSDfOOx2X9Ez3frhU9-lXbZqRgHGkhYHUglTFAmZsAdueOBowiXCjsV3kJZkgA84znSDiDGwvk7QzhturU6-csBflowCo0pbZBz0PGYYk5pa0wLqaGVYhT24vLZ1wHtwiUg_zrWx-7fMl-LxjTqft4bgyqbtAykswnI7rBlCduomhwm-laLTv2ienfSgJ2hhmPiOto-CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CAETuAAgjDv3fUrEkpsvuSeqHXYi1JrlRdJK3gZD0a8Vtb2NF5zDS5FhToFjEsF1JTBoP6Otl3gJZVGrvzlwa7vpGbzc4xoDDShB80J-W_f1cl1zgckSgHLQ9EGlHDj-vzRWG4_w0oMMJXgEVAh_vpyQ4yNKcfO-LODFHA-CrTja6-QeS5b3lOGLhqn4fpRc0lhZyUiibDjR7C7KGNl7t-wWDYuKfYC-RZZ3Wm3N7N14lNMklcOh8tfVdJmMThY273f9kKJoGbOD2UeeIDVklh_4ruTE8dyPxwY-ayoe2VeoPF0VT5COyie0ICMPbFxozBTa87kX22uyfkVAsN-9_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش
پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی اکثر سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
اینم جاهایی که خودم تا الان ازشون خرید کردم(رایگان و پولی):
https://t.me/MatinSenPaii/5016
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CzuE5l5_yeqNuS6ecU1dsNMA1uSPJRFKXX71ZIe_SjKgIcCADIBr4XYLicdNFdi3FxSWxS4-CKnWC_IqF6-WbDyd996WE0vNkIPKDw-CNd_06X6wY8aOsRyiCcBlkDMhv_qcL2BN1CVvEs12rv6XA4iJ5BLlF-ouYQ6IJtbTs4uevpJgS3er_aLCxy-oc1ijotj2cP_5aVdIcawpSbusc9mUQSy_LechXA1H0yJ-NmMqlvcDQaYyvmf2R6QqCNBNWpC96lZNz5eDc4Qe8eMXsinj5oDreRuTlEx5MARuAmflkpSTYUOo0VMBx8DrpgPlKKg9nUgDS2ktgWNM-ODTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agT7LYs_xXewteHnH7dGvZ7r4k08E5gtVgS-hqj-1bsjP4aGALnQ-hySmXy8rDk_-aPm0iSCBxeY3wTnbQ7lfa6lXyTIX2u3Sf29aCAI9UAroNfCe4m7hV7vvrGqTFRZX6EtGyu5cSu-FhaHTbNMXYKjQ6LrrIfo3J8Aj6KtxjJobVLziR3BiOStNXSkTCrItrVHp9fKNggPpxqjW1HKC635WoG6ygtAFvmM7bE-Vydust8LBqJUBSoFbob9f_M5Jj3q6hcNR37_kGOY8lxRmJ1MF65ucNEoyC80xahFMqYlq9jexWxrgKMBN0gHowD25xAbz1yt7HhjKUUSDPTCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7VdskjPfigpup9iNBxwg4VNBKfDOZB5irFfqlM73-hkeavIbYMhrgu6dmuA5-ZmnOYj853ZQSlYI17_uO4tdze-WuoKFZKo0ziOZYdYipfm7zOeK-a4xVa0FKHn6C-kZkUvhB_fIV8eGE7msjhIgwUS9VNter3_PResNhMB_29S64Huzu0c-q-_-HVRO7zNsfU4H3_ifeLpNRPmg1YVGiRdZC9QsBiWc9vFgfOP5Yw9mFzRcKHHEfWpRyAjOw_HU6dkfp7AKg-qtOwahGAV4vfIIkxM-HlQrG_ikEoRYo_Fh9xp4TY0V31h_Jwj2O1ZwYbFxokty2vDTcdsT-I7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxbBgDBGuN-BhfDXg_oQG2SxSBNQaWVn2O9xdWC2mzX9YMnZ4JWxTzotoRaUngy50rKK3Md7bUWJ6TvH-iCbx1YkPRrgD0OBerp4lLeGzhDxIoA_WfD2iuqQYEWgULM4EGCwpbGDLiXhxDwPxSD4ZFEmMZLNP0UAKXwY8slPejDgNBlfbdTQsiH0hWu_TBhQ7bWhIi3UrRcBbgF5VtdTEmMfZdPrteCY_7NwG5f8-_DgyoLUm8OOvu7CJnCsskKgliIPscCu8dCAoB6oG1QKVART4f6IjUGSEIv7fUljyvoUnQ-su7ZhyZXqjuB4HFCYTo5ObF4Jm0x2rvVXlV0Vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
