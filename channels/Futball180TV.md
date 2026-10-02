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
<img src="https://cdn5.telesco.pe/file/s_4NxRMfBBVDCCKRNPKIRT2Jss9VcKfcbnKChn_DvLTOfega6QPjOA5tatf_y33h0kemTvJMQeACEoAXay5vMAK_N9fLHjC1BEpokfHb0E9uAy6MVOmaewUltSdWed2TrIVbs-Zamjgtw1WLIwMtGwUE6kDeYBkK7abf48CopMHwdUR-b8VCdsQAGNHrGaspOyd64i6PupnrgELPtystIAVdqLkOSWh4CtAhPDwWddduW7-SwCbXaB5-Nd8osSlC07mVsCG-NhmsbqNDCMO0zCGpFzn0Q6E5oi0fTMPjN5tlzIL9ObihCsCypsBfRaV3WJmoioG97Uk7SKWdSl0QAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 394K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-107696">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=MbJGRKSnvbtGr-lSHv0z-ArPaje0XcXRWHF3HbDftE06ljQJjKxbxCEOl7HtsADH4dsGkSVYc0fzCogcVcqC5zy4N76sXRCWFXdXE_rGkpOezcPaUiTtwTrHuYCsZuKHT5BlXlExm_PH1YV9WvmvPZ-UicBIKPqrCZYD1SIQBBKFwjPeK8xDYwOvGISCDVKXZWHhV4jhEkOxOIFqnSxq1QCgFGhnWQhSVuUjV3Zx-b7IWLaezDZMY3ewkq3gCevPY502Te7iG57fSnRKOfugcb1Pt-BQrmBBysHP_Nc3kOtBWYzdVjUhjl_SA-bxIKfIb-cfXs3vuaK-7yqLWHQk5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=MbJGRKSnvbtGr-lSHv0z-ArPaje0XcXRWHF3HbDftE06ljQJjKxbxCEOl7HtsADH4dsGkSVYc0fzCogcVcqC5zy4N76sXRCWFXdXE_rGkpOezcPaUiTtwTrHuYCsZuKHT5BlXlExm_PH1YV9WvmvPZ-UicBIKPqrCZYD1SIQBBKFwjPeK8xDYwOvGISCDVKXZWHhV4jhEkOxOIFqnSxq1QCgFGhnWQhSVuUjV3Zx-b7IWLaezDZMY3ewkq3gCevPY502Te7iG57fSnRKOfugcb1Pt-BQrmBBysHP_Nc3kOtBWYzdVjUhjl_SA-bxIKfIb-cfXs3vuaK-7yqLWHQk5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
✅
کیفیت تصویربرداری با آیفون 18 و یک سوپر دوربین فوق‌العاده از سونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/Futball180TV/107696" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX-45bSnKkd9vgsgoyTNzegGHLPoz0OAs8qRd-WFSNVOErUJvciuPAAzc48z-y5IJQK8L4MnYemAuSm0-rU-ero5e26pT5QYJEG1aTQiI1i-PJLobV5l5UoVymN1-Obi9r1cz46fNvRV_vWqbN5VQFJsPiUDBAB5kSNa6GrARrCWLg2CutewfCVpE9xnNcLYES0986qJR8QwC1ZDi1lCJvKj0MBDNiZNmYoRCObsnx4pGw3SL1Lncbh8DyrSrsyQQycibG2ZEM79V5ySsDHbngvbcopVtjvk94JvGsRQ1Cr6ngrEgPgaFEhO_zSzMziJiFrZNLjmyXwQphtp_5W4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
پرسپولیس در دیدار تدارکاتی مقابل گل‌گهر سیرجان با گل‌های محبی و محمدحسین صادقی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/107695" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhA3ezB-uT2kQBqaLX5IrP_iXPv0C4HWK_vUGpPfnVaL4Ezf1GbJuYXoXU2q7aiJ4sun5Ne3TZJYLEmlONSFxcoxa-gNRpa3VH7gNB0XBtxaeCA8HbCF-0lH9yUUqIJvEpuwtstpyw-LkfdfW0fIVIWDDV51QIXMP8Fh1HFQuFYCgTZHq7z90yBJMgOOAnXrJXAMCFOlbzppsV-pd1S1g4pfLTxh7inyRT5f5iKXl12jF56j7OnDBJURGp55822fBlvx786lEDZXnLadkb5qWhRp76bIpc9h86w0saxua0bAlfWM6Mc-Xd-dyKzLDuApwejvicqthsDTGjQ0kt1NjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
یوونتوس قصد دارد تابستان آینده به عنوان بازیکن آزاد با ویرجیل‌فن‌دایک قرارداد ببندد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/Futball180TV/107694" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=kJ_SB-R-g7x3d8WG1z1Q-kK5DUe1JZOsD8VtyUtl56c9O52Gt0DeI0IokZLfluRM4YMVRs6ikfnvl-nk9OIvkhCq0cK39q8uiofMecT5PgqJDWo7xeqi_2fhGtUar1hqbeodfStUfCgIkN6NT9iJb3YR1WJWYixE8wZi0KrWI7W47GBjGAe3aBJbntd0r30JX8cZvi0XCAF9wixW9JtrbEgQok_04w21b0geBcXEychxQR8tYKu6igBdR9eBaw8TakqlrKGnbjK0h10VZvcRarnNdUWblUP43wqKc4ma18bnkdail5eBsOfmNcw51mke7ZnAUfrc9Rz0yOOhT_u3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=kJ_SB-R-g7x3d8WG1z1Q-kK5DUe1JZOsD8VtyUtl56c9O52Gt0DeI0IokZLfluRM4YMVRs6ikfnvl-nk9OIvkhCq0cK39q8uiofMecT5PgqJDWo7xeqi_2fhGtUar1hqbeodfStUfCgIkN6NT9iJb3YR1WJWYixE8wZi0KrWI7W47GBjGAe3aBJbntd0r30JX8cZvi0XCAF9wixW9JtrbEgQok_04w21b0geBcXEychxQR8tYKu6igBdR9eBaw8TakqlrKGnbjK0h10VZvcRarnNdUWblUP43wqKc4ma18bnkdail5eBsOfmNcw51mke7ZnAUfrc9Rz0yOOhT_u3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین صادقی: علی منصوریان بهم گفت چون شبیه نیکبختی، یا باید زن بگیری یا نمیذارم فوتبال بازی کنی! با حاج محمود سفت وایسادن تا زن بگیرم حتی شاهد عقدم بودن که خیالشون راحت شه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/Futball180TV/107693" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107692" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/107692" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp7JQR8-HXw3yRthlOu0sVZPr97nS7ndff9q3f9d7BZcMPnp4Uztn75bWGgHYnrqUii-KYTKQZ7wWmptwpQ3aC3YoiI_amtfS-MHK9hICr-VhHxeoiDOypIiWj1WtcphdOBOGM3ndC9q8jfHpTEWc0M7VJ_7ALkMI7YzGOg6mHHQnszA2jYQ4cvpkS37_mYo7Km8FJkaM3onVg7nQx5bEFtJARrOI4V9iDhBISgSUS4pZKD5dk0F5KxMigTg78dikTMnyoc-SD9AiqnxeRnkiX1Xo_LP37w6knhzYflj6PcO_9qTI4xL5zOUcV6XyOjqMTiAwHHgRdV4tvRuJF86gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/107691" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=GRk0f3bIMRhEdZZUSJdVhhKXsvCEU8YqrGAPROm49_ux-2obLm7GK4WJAt4uqFUnkqT2IQw77TIsuhY4m-I5Dprw8926sWdPAfxI8_I55aTaCBv9ERqmNODmc1sV6kddnz2GCbSjEOMN4h87x4HHTMNuZKyKhm7h4CMaK9XrpuEpscbyNZyHV7zxv5pTaJOa51wiSgGfHikiDxwYXB7wa4-GUmnoRsphhXCc7GdTVYW8tv6cUSh4kfIu0_-e7Cb3mxAMAFbsW8qmycKnnG2_5A_I7fgYf42U-YdWSgwmshgd0nKCxoTxqBpgV_4iN-zvuDJ1ApkekpKZpvehI1P5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=GRk0f3bIMRhEdZZUSJdVhhKXsvCEU8YqrGAPROm49_ux-2obLm7GK4WJAt4uqFUnkqT2IQw77TIsuhY4m-I5Dprw8926sWdPAfxI8_I55aTaCBv9ERqmNODmc1sV6kddnz2GCbSjEOMN4h87x4HHTMNuZKyKhm7h4CMaK9XrpuEpscbyNZyHV7zxv5pTaJOa51wiSgGfHikiDxwYXB7wa4-GUmnoRsphhXCc7GdTVYW8tv6cUSh4kfIu0_-e7Cb3mxAMAFbsW8qmycKnnG2_5A_I7fgYf42U-YdWSgwmshgd0nKCxoTxqBpgV_4iN-zvuDJ1ApkekpKZpvehI1P5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تعجب و عصبانیت قیاسی از قیمت دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/107690" target="_blank">📅 17:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=l6DxHWHd-9_1y18ku6rpYjajbZ2SvxJJ0llte8UB2gRg7-RZeOUb1vb0FceMorf49QG7PgP44tm82im2dqH87zzZLYwbZq68Vson8cUwNiuQzir54AeHLeVnCrp6GGzXv1alfyHJtt4f4SP987NO5UDY6gvg5Er9Mnf0wj7Z3slw1zKwnxhDUz6qo1LlTMfiLBCuIkcXz96D2M-ysyex-RUCRp-ZDwZgX5vaxJTto2L7rmsUG8s8SBu24oNoFpevFU4n3lFb3VP6P9RVdzP-BqVcNSpgYNHsRNKLexDawAh0HY6z8DTzmH1ljb7h2_x0rJBDqZz8UGvHEOJ1BzrFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=l6DxHWHd-9_1y18ku6rpYjajbZ2SvxJJ0llte8UB2gRg7-RZeOUb1vb0FceMorf49QG7PgP44tm82im2dqH87zzZLYwbZq68Vson8cUwNiuQzir54AeHLeVnCrp6GGzXv1alfyHJtt4f4SP987NO5UDY6gvg5Er9Mnf0wj7Z3slw1zKwnxhDUz6qo1LlTMfiLBCuIkcXz96D2M-ysyex-RUCRp-ZDwZgX5vaxJTto2L7rmsUG8s8SBu24oNoFpevFU4n3lFb3VP6P9RVdzP-BqVcNSpgYNHsRNKLexDawAh0HY6z8DTzmH1ljb7h2_x0rJBDqZz8UGvHEOJ1BzrFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرمحمد، خواننده آهنگ سنی نردن گوردوم رو بردن برنامه تلویزیونی ترکیه، اولش براش دست زدن و کلی تشویقش کردن،
ولی به آخرش که رسید دیگه نتونستن جلو خنده‌شون بگیرن و همه زدن زیر خنده :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/107689" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107688">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=s94qVjOOUXGjy97inFM_YUwXwuniL-Cr0I6Q6rcslvChQarolXW1FRIqKdQ-fjYdaEPvStITWerJ2w3Ku_Cb6ZYRUooEjwNjn5_Ulf_nPOIfcrPW1E_FAnFaYuZHQ340_uxsFb_Ua1nkgm0QeLT2g04FoEkngtRKcxreAmH0LNbUIG5o8p6gdl9vYh6fPEpLWhVeq67jsBGVMm9KPww4NsnG8tj3ahfBvHP8XiSb3pcz4n8OlgxssZsQxOTb1CGpX1U1bQQNNageqK0diMKDz8xS5PMnVJVcSweSjieU4FgrxxVRY4MKqGyMEMHYZkBPWWqHlIyE2k7u939mFXk2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=s94qVjOOUXGjy97inFM_YUwXwuniL-Cr0I6Q6rcslvChQarolXW1FRIqKdQ-fjYdaEPvStITWerJ2w3Ku_Cb6ZYRUooEjwNjn5_Ulf_nPOIfcrPW1E_FAnFaYuZHQ340_uxsFb_Ua1nkgm0QeLT2g04FoEkngtRKcxreAmH0LNbUIG5o8p6gdl9vYh6fPEpLWhVeq67jsBGVMm9KPww4NsnG8tj3ahfBvHP8XiSb3pcz4n8OlgxssZsQxOTb1CGpX1U1bQQNNageqK0diMKDz8xS5PMnVJVcSweSjieU4FgrxxVRY4MKqGyMEMHYZkBPWWqHlIyE2k7u939mFXk2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
خوانندگی فرزند محمد شریعتمداری وزیر اسبق کار و صمت و مدیرعامل هلدینگ‌خلیج‌فارس مالک باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/Futball180TV/107688" target="_blank">📅 16:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107687">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=saKFKfShaoquLMk5pXeTNXuxMLbD3jJ7ASiD9NjBeFsNNRPiuqnJ6clcvUl2mf1oMDHp9RHhuXYWoG30bZbWPHVX6uIBJzu-Hal2o4fuB0uyFjmmPn3M3PoMF2b_Mj_sMLDtHC0rX1LM7FPQikMTcfBv0x0LbJZ__rcWCaOxizkfo2EtGcoxSpW_mrcmFAWwRfGw3BmYQJqcSsCFV8beFaV0kiGaq8IZh2qX8yPyz_mTPksuN0RlvBWHeEuZszq_qrEbvgoQ7qv44nfaycYOB2C5s3G2vEKoz2p0rZmJ8XdxEY3lGpFkT7jEOj-cp3wdGna-su9pGREZtqN3pnxrwYkt7b0BYBP2dTwx9gqppDQAB8T7ptLjGuUgI6ocuqgzZQB6GtYctnnnhUj_JvRZkidzGKCWRt-JIS3Gy8d_WbVfiaaJbBWcbZxZ5s7s-LrpLACJm4x1F2DPz5O3LM1m6seTeKpnQM7f-3BrLrtDGvZep02vbvkLNllxY7_9ERBDkFBVRa9UxzqGWbh3z60VQAudJCb2A0-7fAxCYN5ftXIf_QJSVRz6EEzeoIgykjWuX5xgMPL8907Y639ERVlsVW2FI5INDvej9YfMzCn6EAxZadLeFw7-R3V4m9V9BvWfhHZWcMIO3rXSaQD4t1NKD59RvnQflp3VKQIEm8JmiiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=saKFKfShaoquLMk5pXeTNXuxMLbD3jJ7ASiD9NjBeFsNNRPiuqnJ6clcvUl2mf1oMDHp9RHhuXYWoG30bZbWPHVX6uIBJzu-Hal2o4fuB0uyFjmmPn3M3PoMF2b_Mj_sMLDtHC0rX1LM7FPQikMTcfBv0x0LbJZ__rcWCaOxizkfo2EtGcoxSpW_mrcmFAWwRfGw3BmYQJqcSsCFV8beFaV0kiGaq8IZh2qX8yPyz_mTPksuN0RlvBWHeEuZszq_qrEbvgoQ7qv44nfaycYOB2C5s3G2vEKoz2p0rZmJ8XdxEY3lGpFkT7jEOj-cp3wdGna-su9pGREZtqN3pnxrwYkt7b0BYBP2dTwx9gqppDQAB8T7ptLjGuUgI6ocuqgzZQB6GtYctnnnhUj_JvRZkidzGKCWRt-JIS3Gy8d_WbVfiaaJbBWcbZxZ5s7s-LrpLACJm4x1F2DPz5O3LM1m6seTeKpnQM7f-3BrLrtDGvZep02vbvkLNllxY7_9ERBDkFBVRa9UxzqGWbh3z60VQAudJCb2A0-7fAxCYN5ftXIf_QJSVRz6EEzeoIgykjWuX5xgMPL8907Y639ERVlsVW2FI5INDvej9YfMzCn6EAxZadLeFw7-R3V4m9V9BvWfhHZWcMIO3rXSaQD4t1NKD59RvnQflp3VKQIEm8JmiiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یک‌دقیقه با اسطوره رونالدو در لباس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107687" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107686">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=Jx6Xg1rmF6PMFxM2yeix1-Y057nlaQbpRDSjzNxDK_hEZaZ2x-qNoGEsPkCN8jnqOt-cWI0w4penc6WY4MYbiVWLa9r8d_uupUMTkmDy1qjK47BzU3AYEF1XfRdT7ZoCQ6cHps3Pul-FFBfy9RkLcmk7UQLrWFgH9uAJBf97BaKC3t_TFf2sNAxMxr9ac03t9j6TT1v2UbTrUIHL15z3BHZiScZEuHZ8Ok2bk6w1lX9eJ9-ZgN5ZmFH0sjQJN0Cn9gby3DOVPTssxGImKMcKsW5-ghSQwDHx0RZMYE0kH3gKH0eR_zWi0Cf7mBX0ijRAUNsl-ARLyjrTSYKlcjQ01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=Jx6Xg1rmF6PMFxM2yeix1-Y057nlaQbpRDSjzNxDK_hEZaZ2x-qNoGEsPkCN8jnqOt-cWI0w4penc6WY4MYbiVWLa9r8d_uupUMTkmDy1qjK47BzU3AYEF1XfRdT7ZoCQ6cHps3Pul-FFBfy9RkLcmk7UQLrWFgH9uAJBf97BaKC3t_TFf2sNAxMxr9ac03t9j6TT1v2UbTrUIHL15z3BHZiScZEuHZ8Ok2bk6w1lX9eJ9-ZgN5ZmFH0sjQJN0Cn9gby3DOVPTssxGImKMcKsW5-ghSQwDHx0RZMYE0kH3gKH0eR_zWi0Cf7mBX0ijRAUNsl-ARLyjrTSYKlcjQ01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ابراهیم شکوری تا رحمان رضایی ...
‼️
در جواب ناکامی بگویید: یخورده سرما دارم
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107686" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107685">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086fe81733.mp4?token=uqP2mNQ1cMPf7jt_vyEBlO6gzgx3hkN95Y8MnjfddzxENcu2XcSkiyS8aJJL4X634sv_cKhcvY4n0k07zs2lof4PU6ZhWUpeX66CYIUR8J1ibWwH1qE8dawh-SgyGeslSuPrPKjgLknmaVjNI_BCGOv_aRqQGa2UhUJjxM_zK0Q-2BUDZZYiHSjMk-RnxczAhA6MQZJGvrnORVlslzVsPS5p0GAiNYfat1eHuL8zmAV5sQ63fDOepxKRu_JggsSdvr_B3F0GD8dwsLJxhkCpWg9SIaroagHZ_jNzU7MwgeCVxtqZHQDu2Q_rRuKAyC3IhiHMUoxPq1GpUSowx4h1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086fe81733.mp4?token=uqP2mNQ1cMPf7jt_vyEBlO6gzgx3hkN95Y8MnjfddzxENcu2XcSkiyS8aJJL4X634sv_cKhcvY4n0k07zs2lof4PU6ZhWUpeX66CYIUR8J1ibWwH1qE8dawh-SgyGeslSuPrPKjgLknmaVjNI_BCGOv_aRqQGa2UhUJjxM_zK0Q-2BUDZZYiHSjMk-RnxczAhA6MQZJGvrnORVlslzVsPS5p0GAiNYfat1eHuL8zmAV5sQ63fDOepxKRu_JggsSdvr_B3F0GD8dwsLJxhkCpWg9SIaroagHZ_jNzU7MwgeCVxtqZHQDu2Q_rRuKAyC3IhiHMUoxPq1GpUSowx4h1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
رونالدو رفت و پرتغال تمام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107685" target="_blank">📅 15:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107684">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXo_wKYEaxbxXfBaworgDwhpHCMDR-io0xWR9KDVeOerhc2VISsZLNuBQehY2pHzRIf0E7kSkL8NTJEHbt9ObJ2hFRnwXiQG1GkmehWRWBPuNIGHi_dIwd0Yv6n_AhocLnnDvk-k1c4n_XnqdFnaPyyNpedQ1GrGTVm6bSixvtDeu3FRlCD5b2VzDwfaODnD--ueFWg-FBj3q0mW8AQMFabdjvT-Gtak93nC92XeKuZACNRFU9qCf-aIvN5y_tMZnRkLuhZWskATuTBmBAhYs77fOppEbGUNuPRyO7QZ02DoUjF598FTCNOT4HX1dj3I_EIorhVXDKiof07Qt0_xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
🇪🇸
فابریزیو رومانو:
🔻
نتایج آزمایش‌های کادر پزشکی بارسلونا تایید می‌کند که مصدومیت عضلانی رافینیا که در اردوی تیم ملی برزیل دچار آن شد، جدی نیست. رافینیا از هفته آینده در دسترس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107684" target="_blank">📅 15:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107683">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=W19ABO0rpDZAGCdBlw0gfvDCNV8PM_ZGMLJD0hMAIbRAx-4cN4thEamgDKjq0EEJvNLQuIz-cMMbsFAMAIzhSUpvxOvz-VHywO-v4DhN3zZj3HKR_Nc1-BE_vt7YZC-4QVgpK3PhjueYH5a7x9uM3XKymyLM0VwblY3jhj4eoF-OU5Hzu7rkloJMo8gliHjUB4Urj782Z1oSw3xHvhZR5XDrwoWhl7SdrPFfgXkMfX_zOa7vpdWL86Ggvpe1fwRct2Axp45WPbh-_BKFs3Ncu38QKx6wKa2DRRK0i42CyOF6K5LwvbWbhzUwH9u3yFWBTuuL6Ekvc_cucs1PcDDjZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=W19ABO0rpDZAGCdBlw0gfvDCNV8PM_ZGMLJD0hMAIbRAx-4cN4thEamgDKjq0EEJvNLQuIz-cMMbsFAMAIzhSUpvxOvz-VHywO-v4DhN3zZj3HKR_Nc1-BE_vt7YZC-4QVgpK3PhjueYH5a7x9uM3XKymyLM0VwblY3jhj4eoF-OU5Hzu7rkloJMo8gliHjUB4Urj782Z1oSw3xHvhZR5XDrwoWhl7SdrPFfgXkMfX_zOa7vpdWL86Ggvpe1fwRct2Axp45WPbh-_BKFs3Ncu38QKx6wKa2DRRK0i42CyOF6K5LwvbWbhzUwH9u3yFWBTuuL6Ekvc_cucs1PcDDjZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
🌟
رسانه‌ها با انتشار این تصاویر مدعی شدن که نیروهای خنثی‌سازی هسته‌ای آمریکا همراه با یگان 75 عملیات ویژه، شبیه‌سازی و تمریناتی برای تصرف و پاکسازی تاسیسات هسته‌ای زیرزمینی ایران انجام دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107683" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107682">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0274908694.mp4?token=DqjBqkhpNjg6DWmgrBUrpZw7qGXVrlF-ncz1jT5xUYN-ErEjOoMApKfpMmKnbTTsRTYhHx3SzFqXO9frYYelM-aEpeagAD0djbRmTN-V-Vb1vAZ_RIxUL-bimWopFwMpiG5xa6qu8IO3GUOBwZNwUzzaw1EJIoh6R01JFA3elSQyOMmg8lW-bs1ZCKb9XP7jATWKFhw26op6U2b1vAViX6WDuTe1NkMZOXX6_E612K1el2k4Zc87nXYUj8MVHpoaJUkMDVnGoMK-MxTnFk4dvyBAcDJJcX1RX_N61wa-WAQolCbNyVvYryDgVZ1C84MZPaMKLrtaphdF-aL-vFxs7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0274908694.mp4?token=DqjBqkhpNjg6DWmgrBUrpZw7qGXVrlF-ncz1jT5xUYN-ErEjOoMApKfpMmKnbTTsRTYhHx3SzFqXO9frYYelM-aEpeagAD0djbRmTN-V-Vb1vAZ_RIxUL-bimWopFwMpiG5xa6qu8IO3GUOBwZNwUzzaw1EJIoh6R01JFA3elSQyOMmg8lW-bs1ZCKb9XP7jATWKFhw26op6U2b1vAViX6WDuTe1NkMZOXX6_E612K1el2k4Zc87nXYUj8MVHpoaJUkMDVnGoMK-MxTnFk4dvyBAcDJJcX1RX_N61wa-WAQolCbNyVvYryDgVZ1C84MZPaMKLrtaphdF-aL-vFxs7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚽️
پایانِ متفاوتِ دو اسطوره.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107682" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAqh6JVaOxK6HKSFGf1so0WNuMv0K11dbajlujiYRBYZDlkIWZ-Fv92krIywyT1uNCQ6eZj78Iqd0ceqScAa6HAohvPrQiRZneY_utwrcBuvONt_f2qihjx8RAHD1hTNcNxbp-xXIRq_AjrED430TTTgG5RQNUQCU1w_W0wxbtsgaFa4ohhY-T6mVFptRKySPLfonH7oFIfQ7uagyFWQIOG7rgAWHKurYxOTy-WKcr93hrSZ3-GBtCR1fI_U-bTfWII2rQD8_xDH3UjKEIVyGqNnWNg74hK5jGykBRXyjh5IuLiQI4x7hRYrfqZy7PvueKdbsEHOFZhE-IMP1dEArF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAqh6JVaOxK6HKSFGf1so0WNuMv0K11dbajlujiYRBYZDlkIWZ-Fv92krIywyT1uNCQ6eZj78Iqd0ceqScAa6HAohvPrQiRZneY_utwrcBuvONt_f2qihjx8RAHD1hTNcNxbp-xXIRq_AjrED430TTTgG5RQNUQCU1w_W0wxbtsgaFa4ohhY-T6mVFptRKySPLfonH7oFIfQ7uagyFWQIOG7rgAWHKurYxOTy-WKcr93hrSZ3-GBtCR1fI_U-bTfWII2rQD8_xDH3UjKEIVyGqNnWNg74hK5jGykBRXyjh5IuLiQI4x7hRYrfqZy7PvueKdbsEHOFZhE-IMP1dEArF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
😆
😆
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107681" target="_blank">📅 14:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107680">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyDw6chQW65B9ocuxepk0IAwXLs5hDGh230X62ZxN6emMDmITsFzXy4OrDZEwni98NOZ-yA19iSWfykfjTYq2jCStZo5_xKNqJjXKbRH6p1UoeEeEkeXbBVSJpF-n0tQkigAO_DwMuVNox5bQ1jGcDbAvexBS3X2n9fkutDmLIFZaqD_IoxFOSFY23zXcisnvX4iQO-E9Eh94TLLwODDkLN7HYSxZg_0nOBsJyYpsAP4Wkatb92zhso-Vw0GDryavfH15gkiWPAGXsSAZh3KW6bT7HGUzZy2rfxnPSjZ3yl_BHGi5kaqXjEi9l4MD_vdLX1rMROgiLrZsNEIISTmTAAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyDw6chQW65B9ocuxepk0IAwXLs5hDGh230X62ZxN6emMDmITsFzXy4OrDZEwni98NOZ-yA19iSWfykfjTYq2jCStZo5_xKNqJjXKbRH6p1UoeEeEkeXbBVSJpF-n0tQkigAO_DwMuVNox5bQ1jGcDbAvexBS3X2n9fkutDmLIFZaqD_IoxFOSFY23zXcisnvX4iQO-E9Eh94TLLwODDkLN7HYSxZg_0nOBsJyYpsAP4Wkatb92zhso-Vw0GDryavfH15gkiWPAGXsSAZh3KW6bT7HGUzZy2rfxnPSjZ3yl_BHGi5kaqXjEi9l4MD_vdLX1rMROgiLrZsNEIISTmTAAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط امیرحسین زارع با شکست حریف چینی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107680" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107679">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
وضعیت عجیب عدم پاسخگویی اعضای تیم قلعه‌نویی درباره نتایج ضعیف اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107679" target="_blank">📅 14:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107678">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDR0JGAtaYxJHQ2ZGqUb0aBEU5riZyvaHDh6LYP7j_tsZYx7fMsOQtNuBbqYhDvEklIO3U6PQWaKbRB9pMK1evyAoGBHWdxK3BgYmwDZXLSraLUgAPwVpE1yCTdf4L-g4rf15hgLaZzKmErI5UiSEwOqTxL1qaqNNT-42JuRLSLOcM8DqpouX4VSaM03Ie9iQW6e95IFhkgdawm4hz8fB0g7DKNEKNavnnqZy1eYnJ_HEHWke1-D1s23gH81niGkNQWTIJ77Ux0rr6Y73LF5tzVZX_lC7Wyi8FnD4jSVTPkB1E32RX2Wb7RpBELiBqkdwaNkgvWPj7mViqDA6v2Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
⁉️
مسی یا رونالدو؟
👀
🤩
توماس مولر:
"در طول ۱۰ سال اول دوران حرفه‌ای‌ام، همیشه کریستیانو رونالدو را انتخاب می‌کردم و همیشه در مقابل او شکست می‌خوردم. اما وقتی به کل تصویر نگاه می‌کنم، متوجه می‌شوم که لیونل مسی، بزرگترین فوتبالیست است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107678" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107677">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=XpH9ac6dmWI3FGZKl1RSCnSzicNiIt943W_AUjYR6c6lfAaEBAUJcscsxdxjCIrYIykTMccCOfnmq4ZIpDtJx-G4xx_4e9r7_DpBE5jFwvhXQLpMzU8KHJ8GzO0u5d2vPaRPVQfLufeXGNFTKDxaFq0OhqmDujMc0ddItJti5lpyRRvVrAkd0PwxzkTyaLj4R5QQ5vBTBuoX5uQD3FiHaqS-1FiR-2A7xUUFrZeKoQfE1iiG9ZCmvVUNJgQHcdzfrvUbY9GD0We6qE_zeeMmPLp6uhB8BSGTNmen04Ql2MVy8MeTPoWhsNG5y4g6DTem_1LBmaHhE-hLYeKmQjzH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=XpH9ac6dmWI3FGZKl1RSCnSzicNiIt943W_AUjYR6c6lfAaEBAUJcscsxdxjCIrYIykTMccCOfnmq4ZIpDtJx-G4xx_4e9r7_DpBE5jFwvhXQLpMzU8KHJ8GzO0u5d2vPaRPVQfLufeXGNFTKDxaFq0OhqmDujMc0ddItJti5lpyRRvVrAkd0PwxzkTyaLj4R5QQ5vBTBuoX5uQD3FiHaqS-1FiR-2A7xUUFrZeKoQfE1iiG9ZCmvVUNJgQHcdzfrvUbY9GD0We6qE_zeeMmPLp6uhB8BSGTNmen04Ql2MVy8MeTPoWhsNG5y4g6DTem_1LBmaHhE-hLYeKmQjzH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
دیس سنگین ژوله به قلعه‌نویی بدلیل سوال عجیبش از خبرنگار ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107677" target="_blank">📅 14:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107676">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eade000140.mp4?token=AqLbJXcrBShB2cH1_ELqn5lhYN8FJ7bPConT_08Glbe6VvD-_H__7FgYwV1B2oq9fkX610UE4Vj4E76gSO0TQaWFsHZ-I6oyIiEzXZfOb3_KGo9A4iOCK9X63iJ-GFxoB1B1U6vlTM6LE2oGyNEN7OwA0DxqvUuPkUqyatPSfSVZ95ow59hUqMuSDbbti-G37wet1ohlj-pbrQ3Yjrnl1Iut7aThGB-eodZASVc4tEjPFpwTg4rv4QDNt3JUsn38hl5vaFfI54REPaIRskuQhEN4ba3dc2jgBxVLpPpRCPrIVUlmA1o__50tY2wCylipRkooMdg2knM2FDgHGdQsYbaaxCTDFzU6ZPH14gKStZuMmzJgw8lTED0ErpsBeeM4iRWcTpovjtn7yuusPg7V7YuB49PdQptoPouEe1HWmV7zOMm6mqzRUVBPeueUi67kVZYcb9BvSeQt-EyctbrTVmLqAg8o8_kY9mT5scwJnA_ogcuBYSCAHVhDN7rUboUT_93EPn-pQhrFoFfUfWQxrehpnsR7Rq5C0ZalNVY9CV88PGZoclwYY2kHAzbZZrpzl8h7Ujzf7OrNv_HOCzyGwxs4Nck5elh7vRXjdX_zlzoQQCQhZ4u1TfejFBS5XQjW8uK0vRqw-FZN3yWtJ-woxA1fbM9OfWtmoaXOd0bBVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eade000140.mp4?token=AqLbJXcrBShB2cH1_ELqn5lhYN8FJ7bPConT_08Glbe6VvD-_H__7FgYwV1B2oq9fkX610UE4Vj4E76gSO0TQaWFsHZ-I6oyIiEzXZfOb3_KGo9A4iOCK9X63iJ-GFxoB1B1U6vlTM6LE2oGyNEN7OwA0DxqvUuPkUqyatPSfSVZ95ow59hUqMuSDbbti-G37wet1ohlj-pbrQ3Yjrnl1Iut7aThGB-eodZASVc4tEjPFpwTg4rv4QDNt3JUsn38hl5vaFfI54REPaIRskuQhEN4ba3dc2jgBxVLpPpRCPrIVUlmA1o__50tY2wCylipRkooMdg2knM2FDgHGdQsYbaaxCTDFzU6ZPH14gKStZuMmzJgw8lTED0ErpsBeeM4iRWcTpovjtn7yuusPg7V7YuB49PdQptoPouEe1HWmV7zOMm6mqzRUVBPeueUi67kVZYcb9BvSeQt-EyctbrTVmLqAg8o8_kY9mT5scwJnA_ogcuBYSCAHVhDN7rUboUT_93EPn-pQhrFoFfUfWQxrehpnsR7Rq5C0ZalNVY9CV88PGZoclwYY2kHAzbZZrpzl8h7Ujzf7OrNv_HOCzyGwxs4Nck5elh7vRXjdX_zlzoQQCQhZ4u1TfejFBS5XQjW8uK0vRqw-FZN3yWtJ-woxA1fbM9OfWtmoaXOd0bBVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط محمد نخودی با شکست حریف ژاپنی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107676" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107675">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=I2TZg1YRoNF9hEAxbcTGjx1YYzBpo2LhXl8uFcafik0Ko28LrLrlIpnsZh1c6qRuZfjDJvHNQ8RQi6M-uO9Iwr3dgtgzokkIxhIHY16Fh0KjpxrWp83PA8Uc5Cqnf5vjqxF9V-jxKnnokK4pSO5w6Diu-kFHbOVROK2K6qsA-qyzCZzUXdYsqRWifR5x83mXSVUvc7BzJKbxmmTC4GnQlyqjsqkvLgF2AHxRp1-AahzNLs-MiCYFtPQpa7Gc2mPZ1c04I2EIRbDqxonoR_CtlpqIt8ctvlREj4GGsGi0B03VorrgPkZSa6kDADDNJKYSQvcrMWP_ecRC_uBXwvSebQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=I2TZg1YRoNF9hEAxbcTGjx1YYzBpo2LhXl8uFcafik0Ko28LrLrlIpnsZh1c6qRuZfjDJvHNQ8RQi6M-uO9Iwr3dgtgzokkIxhIHY16Fh0KjpxrWp83PA8Uc5Cqnf5vjqxF9V-jxKnnokK4pSO5w6Diu-kFHbOVROK2K6qsA-qyzCZzUXdYsqRWifR5x83mXSVUvc7BzJKbxmmTC4GnQlyqjsqkvLgF2AHxRp1-AahzNLs-MiCYFtPQpa7Gc2mPZ1c04I2EIRbDqxonoR_CtlpqIt8ctvlREj4GGsGi0B03VorrgPkZSa6kDADDNJKYSQvcrMWP_ecRC_uBXwvSebQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آخرین اردو تیم ملی قبل سربازی =))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107675" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107674">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyyW3AQsoI49JVDj8HlCS0IxEE-BMFft8Zq5D7QWp-JaECSXdSl0Q-ZF1QDthtOD9ikweH-_c9KJ9Yk_YPJfwVxq18E_qD2qqp0kG7AJPCeMa5iuP8BkYY4mEIerR8-AL_cEVf5EYyI_nytWDYaBLHxb_j4pBwykPN0cLfq4wJNJVnAo92EOZPcxQ5Dm2yeJ_FuiTwvXhLz5KzR6qwYy8unaORPRlCrP8ryuLG6JvbWRcACZZxZiEZPZRBECKN0_7io7icNkC_Txi-lupSyA42hs1nNgAKvM5lSm1NztTszRafymC3oy8UhGi48oqoG52_c6GgqFoqCVoagoHmC4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
هویلند بازیکن تیم‌ملی دانمارک: شادی دیشبم برای ادای احترام به رونالدو بود و هیچ قصدی برای توهین به بازیکنان و مربی پرتغال نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107674" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107673">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=fXjXoJEtQQ5rYyax8fEajFiJ3Ida5U26VoywPZkr9FNv6IJ1N4BjOJ8CjomQ0QLIzpZZxH6rYqWFkkJCFHwDqcrtfIGmjKhGe7BZG-Yhw01pAxJQG0TVKqkIN60J2K7m8w6IR-XZirrq1YImat62U11r3qJsr1XYRS0Y44jiBH3XwJNzXfH5UZ1zV9gINcsx-TqFHtrKZDneF5XOQ6COB3B_VVbO_GBsw0_ZomVUT49i2LBH0DhjwTHR5dvjLac3C7u6hDOaujv_gTFISD5KDRmxJ5ohJKUxWcSKHMen6Q7-pHB4ou0hT20NMU7ghbCrHzuyVlJq9oYgpfa07DAqF3GAH38fbGkqwshtZfZ_S-_0tZyaHarz27epCtqMVSnIws7i_Y_sY65BKsWG75ZAu0v7zhIlrsTmOrT1e8zBbvSsIAtABJRwI41FNyqfaR7IK1Mk9RtncpKI3rnlUjJt-wOLSK1FNx7Gd90XPTqlb8thluG2oYizhkBQ3O0SNxHeRb8A2QIW92UH82tUEmYtCtg4meH3iQT-mys5DZAVEp7fy9AXzzWGSkd5sir5XkAkgUUO0Qpgtbt9KsZmfxzG2yV26aVMgsvPanjCsDAwCVnnMYFgZaGPqb-bXOC1UwJ3bmCxs-bkhhaYHdpUI6OfHpglrbaouT-fOgvZDBJb7X0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=fXjXoJEtQQ5rYyax8fEajFiJ3Ida5U26VoywPZkr9FNv6IJ1N4BjOJ8CjomQ0QLIzpZZxH6rYqWFkkJCFHwDqcrtfIGmjKhGe7BZG-Yhw01pAxJQG0TVKqkIN60J2K7m8w6IR-XZirrq1YImat62U11r3qJsr1XYRS0Y44jiBH3XwJNzXfH5UZ1zV9gINcsx-TqFHtrKZDneF5XOQ6COB3B_VVbO_GBsw0_ZomVUT49i2LBH0DhjwTHR5dvjLac3C7u6hDOaujv_gTFISD5KDRmxJ5ohJKUxWcSKHMen6Q7-pHB4ou0hT20NMU7ghbCrHzuyVlJq9oYgpfa07DAqF3GAH38fbGkqwshtZfZ_S-_0tZyaHarz27epCtqMVSnIws7i_Y_sY65BKsWG75ZAu0v7zhIlrsTmOrT1e8zBbvSsIAtABJRwI41FNyqfaR7IK1Mk9RtncpKI3rnlUjJt-wOLSK1FNx7Gd90XPTqlb8thluG2oYizhkBQ3O0SNxHeRb8A2QIW92UH82tUEmYtCtg4meH3iQT-mys5DZAVEp7fy9AXzzWGSkd5sir5XkAkgUUO0Qpgtbt9KsZmfxzG2yV26aVMgsvPanjCsDAwCVnnMYFgZaGPqb-bXOC1UwJ3bmCxs-bkhhaYHdpUI6OfHpglrbaouT-fOgvZDBJb7X0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✔️
نکاتی‌که قبل از خرید آیفون دسته‌دو باید بهش توجه کرد؛ برای رفقاتون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107673" target="_blank">📅 13:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107672">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdYlw9zq_tQAI3Of__LpLwlf4QZsBtHGFMoQpz0X418-BqdijYKOtt72JeUMqOYJytduDFpLrj1CHOpzz_VoBenCzQk5IZUPCnTqFI1hv2p0wptu1IYj9CHZaQdc-LgMIX55szvaN-TEWveHwVI29HN2VY0BTZH-ysqjfXu-ccepZpEx6PgwNwiJiqwakxQqjma6LNmnuVvTa2wkTErzE4ynJS2Wjaoyrb8lwOeWtzEz7HNlmPXk6Z1NHJ1X8yLS3B6hqiIq_LJBwlbJ3uJVEPfPOu61Jpe44udxJeK_xgzJOQYdm3IOYoX8rgk5ulL05kbgkhkFDHWx65KbGwqweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
استوری همسر رافینیا ستاره بارسا!!!
فوت‌فتیش هستید دیگه چرا علنی میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107672" target="_blank">📅 12:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107671">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=U-sPNSbjWHhRJx1r9aoMuWR7bu9hsYZIX41J1nE4L-1RJVfOrl-_aLFvhwUH2GN6-SCZhcU_vluSVSLBnNeso9gtLONkxQ_LTJ-66mIAw3JDgRWrF9xhK9nj8e8smvV4vTTLHdKnmHWiadWEOStVUJ2Nv13CGFmNP1TpK4qMm-betqOZY6SNQ4yVBgD5UNmYDb5J5qpI8QGodyscOgQTtq7j1602we11UHk7ADSa-_9aQCL8nDTFslSBPog5SQB06R2FPRJuFFH9GoLgfQH9L8HT2NOUcn8rhsKaEFonvK8-iVqq4mhRbpTHnahZSQvnvLe_VBta1t2LIRBZ20d9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=U-sPNSbjWHhRJx1r9aoMuWR7bu9hsYZIX41J1nE4L-1RJVfOrl-_aLFvhwUH2GN6-SCZhcU_vluSVSLBnNeso9gtLONkxQ_LTJ-66mIAw3JDgRWrF9xhK9nj8e8smvV4vTTLHdKnmHWiadWEOStVUJ2Nv13CGFmNP1TpK4qMm-betqOZY6SNQ4yVBgD5UNmYDb5J5qpI8QGodyscOgQTtq7j1602we11UHk7ADSa-_9aQCL8nDTFslSBPog5SQB06R2FPRJuFFH9GoLgfQH9L8HT2NOUcn8rhsKaEFonvK8-iVqq4mhRbpTHnahZSQvnvLe_VBta1t2LIRBZ20d9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
🎙
واکنش متفاوت بازیکنان تیم‌ملی پرتغال به خروج ناگهانی رونالدو از اردوی تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107671" target="_blank">📅 12:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107670">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKX--JdrIUrvHlYWdTYRCBKzDtkneEchf4skgPwWfBslkljxuG5QFQl45i-tWVOy_WV5knXfqzTcf32qmQ9Rlf9KoQz_52M073Gg224k_WeqbyKS82XymCe2aWHkLm7t3sxoAzD2mdinIFMjt2_bkWZorvpWiZutzRNJP-d-fr3cOlZOrlpMlEwrSZR2_3ECCa81cZlBsVnUWtPnbTRAM5UxWmOOa6ARqZU1g1ayzY7hPcBWyHvgnBRYmCwE35KtO7Jss2_eEkWAzGHbCLFrRHaF0F1gdmgF1EkdWhIy-R41GLTNIMc5DCJSs7uRs_sgVlrEgv89w0njpatHTtzQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تایلر، د کریتور (Tyler, the Creator) هنرمندیه که تصویرش روی پیراهن بارسلونا در ال‌کلاسیکو رفت مقابل رئال مادرید قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107670" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107669">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWM_oNJJ9s0NEV0r2K2rHKkWVdnp4ULZBAGYeRC-zIAWIRO7RFM6pTALKtmbHcC6EAxW_ddER0Mbhc07WnGvkUhma4vihAceBTCCFRlDdO-kO6xteEBZ442rkZ8hHGaQU8eZMWCjCBr5wsSJfZepCt38IV_pXImi26zK8RZVeqT1MEWu1s9Vx4IzFmAfbk_P8wclupVkPwddQjQx9ZzqQ333BL2vnGghOQ0rgbpDvLJm22QQetidNUKjVv1NoTpg2PbWapUzAy9Fmdb7PXTtZZN-N2rnFzw5NuQ4khDincp4EDwYomvNiqm2-VWCrCsnm3Fhhi1b4liQ6S-4zbE7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇵🇹
خط‌حمله پرتغال بدون حضور رونالدو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107669" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107668">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcXqdFMdvuIAGyz77Y6c2FFhamEO7UtKOHzeVkIR5y6cZKoDnpMZhnLa7V3knJp5qvMo9m3Hvz9QN_tH9WVoIYirX03H8KDwGzYaRpxCVhqion3XTWmcIQuxW3N8zS5Y-lAdvtLOtFF6i5S_MPLO632SjdA6WH9F15LY0ZDPw3QNC32-5tOk9u4l3kAnr8iMpq9-P2JQEhxbzbaE2NLzaJGcJthpfakJj4QhH3TRnC5yYMziHwCG0o0sGXG0wjAXJkod8TBNZV4s21wkhH6caJYNmFGOXAwexB6oMBVq88XGWBjTE9OvXj3MmKpcan-HofCcBvYz__-oZpX5OT0dmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
📊
بر اساس انتخاب  بلچر ریپورت ، لئو مسی بهترین بازیکن تاریخ فوتبال است.
۱.
🇦🇷
لئو مسی
۲.
🇧🇷
پله
۳.
🇦🇷
مارادونا
۴.
🇵🇹
کریستیانو رونالدو
۵.
🇧🇷
رونالدو نازاریو
۶.
🇳🇱
یوهان کرایف
۷.
🇫🇷
زین‌الدین زیدان
۸.
🇧🇷
رونالدینیو
۹.
🇩🇪
فرانتس بکن‌باوئر
۱۰.
🇪🇸
آندرس اینیستا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107668" target="_blank">📅 12:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107667">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=OVLfjw0JAxgsV_Jq_N6EfSoEhIoohRnnrI8-fg-E8FkaBM6iU75yH5_q_3620vH91WUI7zVg-thSGx0xwQ0gL7mw8ZDyk5ij8ZJojDL5GbUxOxVM4JtSIN1oa5OHBhniWx9UXbtsTS-z_zk0g44OhH7POTYSD9A5a6pmiX7zYA9CaqtmMR5mEswxgcURYQ7I-AfzMIZpScqTvdFPrAJJ-WUjmkG3chf2bRjHz3ODaUsWWa9uXjNuwRfHhrqNkSMXb2kOlnRcxZJcTySDy6YRSuaDUolTS2tiR7VmqntyvbV4c7-LcYx-5JNb6G32pAR0cmZnR3c9XYWqGy9-wRvXpXfmVLufB2Dw_zgrM_SUiENL6yIigX2Ftvc265At0Ugc1DuwQzoNM1m4AQILRFUjVqPOJA7N1sA8gOnXBVi-w6pECYx8aVRkOZe7C_Epz1UNEd3MYhYy2f73r-bYfjBAD1fHKNMlHDzGA7UL8GK8HxzZ-kyuSG06lkyiCZBcJRiMu_Ec4_BeFH5iWWDaL0npkdqd4lCW7IZOtFpfljm_OXIgnhnKmNNzI2b8qZCW7th7xUcwnHih03N5yhdTGbFOfwy2J0sX8ORyMSbh15mX1iT2XVcTT_y6ARSqU5s3bWiYK0_AhLZjZEosGy1SvftqxsHaifBTDOPdnlhCMmB7ilU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=OVLfjw0JAxgsV_Jq_N6EfSoEhIoohRnnrI8-fg-E8FkaBM6iU75yH5_q_3620vH91WUI7zVg-thSGx0xwQ0gL7mw8ZDyk5ij8ZJojDL5GbUxOxVM4JtSIN1oa5OHBhniWx9UXbtsTS-z_zk0g44OhH7POTYSD9A5a6pmiX7zYA9CaqtmMR5mEswxgcURYQ7I-AfzMIZpScqTvdFPrAJJ-WUjmkG3chf2bRjHz3ODaUsWWa9uXjNuwRfHhrqNkSMXb2kOlnRcxZJcTySDy6YRSuaDUolTS2tiR7VmqntyvbV4c7-LcYx-5JNb6G32pAR0cmZnR3c9XYWqGy9-wRvXpXfmVLufB2Dw_zgrM_SUiENL6yIigX2Ftvc265At0Ugc1DuwQzoNM1m4AQILRFUjVqPOJA7N1sA8gOnXBVi-w6pECYx8aVRkOZe7C_Epz1UNEd3MYhYy2f73r-bYfjBAD1fHKNMlHDzGA7UL8GK8HxzZ-kyuSG06lkyiCZBcJRiMu_Ec4_BeFH5iWWDaL0npkdqd4lCW7IZOtFpfljm_OXIgnhnKmNNzI2b8qZCW7th7xUcwnHih03N5yhdTGbFOfwy2J0sX8ORyMSbh15mX1iT2XVcTT_y6ARSqU5s3bWiYK0_AhLZjZEosGy1SvftqxsHaifBTDOPdnlhCMmB7ilU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
📊
راز شروع بازی‌های پاری‌سن‌ژرمن چیه؟ این آنالیز بسیار دیدنی رو باهم ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107667" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107666">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBewNz-7r1tm6mGP2jFMAWMir3vIrCvROBISB8L4wfl3JSP6ozZTJLTU07CZQo0ykUXf7XIbinZMeDVngFh4uCQEV-OGvo7kOzKTk00uwUtuNelD34yjVrO3GdPhtNtm4oin9f07xZUcjX4ZnebBN2SGkJLk_msFQhj1sr_krJXIF50k_w14fACHngQXUl8UbNtSAogSJa9hPjMCgYjqjcPSO1bSEfGKdA0Mbwbe0ET-VswypJtcn3hNzeyeYRAPbbL9A9Og-nH4Li3XMRPKXSn9RyfdzLbrLOgEfWLufiI3_UJwK5JTox8q49kCOBNf4bmBLfKGoO9cPbUF1WFSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تیم‌ملی والیبال ایران با برتری مقابل پاکستان راهی فینال بازی‌های آسیایی ناگویا شد. برنده چین و ژاپن فردا به مصاف ایران میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107666" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107665">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXX3cwdbugeuENd8lyk96EMMLgItxCBmcxOPDK4fP_CH7JZ-iNv2fABk_CriZqJyvskvKkr6lAtR6fLGcG_tBdDcU0YIQ1MQzAz_s6YGpXjZp79lV8d_HCeQcQqH0Fs9OxLf6QRHfUuwmOqZ229U_Xn0KwUcuCPLjTaPw-JEERZWs_OcvO68WC5hxlMyfCZIXCKZ2dhF3L_o4l2pvlMTpsQmvlvKGp230GWLoyGeGKRasGTH_K0ndxmnfcqTyZUYiVVCNcvNcSZ6V78SQtm1HXHh6-SR-M7AtJMJJYYWLQkcpT9TFXNIVsKjaQ5pHb-HiFch4gUQOodQ2GaKwX1Ydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال نباید فراموش کنه که رونالدو عامل کسب سه جام ملی مهم برای کشورشون شد:
🇪🇺
یورو
🏆
لیگ‌ملت‌های اروپا 2019
🏆
لیگ‌ملت‌های اروپا 2025
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107665" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107664">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107664" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107663">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWJdAEkHMVpyKro5DH9Nk7nBE5kAWgpiVOaaC2JCgh4ZlieQ5ZoC27ubL6wIQaRqIrnw1rVwe0Ii-yt5qWxpJZELrprZ3hd1R_yMswSUYQCtSonS96HQg1KMJk5etVdRv3OWW8piy2-xvhkd4trFXf-Te96KuiN1O0KVYlFjj0lVQaJ6bTTza89x12vNRRxeVYQwOVsouWiaDbynoGY9WZdUYFrVtEFd9nxS6ycWeYkw1sNvOyqxHaRaGHKBcAEAX2FyA8WlfvmyddSud2EEH12mF776-qMVR7hig-tPT883dRK7LyXPQ9-lfYPdpCuvafnQ6lSmsWjSfMWiD15vFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107663" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107662">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw8ECpsFqe37D5NVbTvVXYpadViFV9Eo-O4JrZPUDTEsm-ySBqvEOxfLsxtEZvtYwqG3HexgRHLP_8PFvUVIENskM9j_-aigwKullpC4O2E5kjYEysFzzPJlacPqiOnteZKFptEGW9oZz0UkQk6_hYuX18pDe-HKJPYue8WLS3ZwxFNIuVkitT3z0DSOlEvN7a7MmygrLJvxUfU2Bc01v1tewllv1KVPhxlsTzNbthxBNGQFeRqIBhoxPJ6JNcoB4kSzzBk8ltCWWP1YblH5_iM_ttqYK_EjVdXfxHUw1_0DitfzLWeazix1Q0A_yimmlKMldXsNsEo_pTmD6DgY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری یاسر آسانی در کنار وریا غفوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107662" target="_blank">📅 11:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312a800413.mp4?token=f2IxpmsBOByO19rbiRuinkyBLcNJRaZjWHdo06eivnJU7G_9gi50ToaHkZJm8F8jw2TU2V2NkNBaQOf4nQkj5NpK-gsoHZpXlESj8tOtON_R9bdKv4o-KEP7wn0OxxA51i7No_J4hWMzQGLXOz5VNL7giCvLAJXVpRAYbv6uXDtDYQt9pSeRqk6E18PMJxz0mmRXT-3_dsq_WnQA2Kyl43vPj5M5H87n2OBuhJdSGksn7QOPE4OBi3lzoUmqqB58oQUb6l6YM5wXTs8jWJUjDi8x8RJY6HGTccTTlm1X2k67HomGvJC_NKYXR2US-IOWskmZRT_AVhgHUwVH6Vmplgy5H9NPn-oT3FuIY1QC2ITHn0wmuqkP1bpDjlmayrLZjrHjkSwJRmKrs-BK9asdb7EXuf2rBXrkHZ6Aug2DFhP3R9FQp4pY898THIxeUxpu6OitJfFVyqvQVYSWOTx-MqXNKWoYzeiHxbNeILKVPF1Jb8uSBJb2ReSgpjfSsrmXpgmSZ_Gq9WfN8bXL7DebjeETA1s46nV2G7rWmPerbOZ_bLOkzK8Ov2M8-V3xBvqtzVmL83pcYG1vNyPJ9u8FZLGxTnlIymi3TtYkTaD1TBHSBMkjmf4w1z7Nh-ZoGYcu9g5-zvg0WYC1vgg7zMzJqdVUcWf7nvwCPyMCeydYDtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312a800413.mp4?token=f2IxpmsBOByO19rbiRuinkyBLcNJRaZjWHdo06eivnJU7G_9gi50ToaHkZJm8F8jw2TU2V2NkNBaQOf4nQkj5NpK-gsoHZpXlESj8tOtON_R9bdKv4o-KEP7wn0OxxA51i7No_J4hWMzQGLXOz5VNL7giCvLAJXVpRAYbv6uXDtDYQt9pSeRqk6E18PMJxz0mmRXT-3_dsq_WnQA2Kyl43vPj5M5H87n2OBuhJdSGksn7QOPE4OBi3lzoUmqqB58oQUb6l6YM5wXTs8jWJUjDi8x8RJY6HGTccTTlm1X2k67HomGvJC_NKYXR2US-IOWskmZRT_AVhgHUwVH6Vmplgy5H9NPn-oT3FuIY1QC2ITHn0wmuqkP1bpDjlmayrLZjrHjkSwJRmKrs-BK9asdb7EXuf2rBXrkHZ6Aug2DFhP3R9FQp4pY898THIxeUxpu6OitJfFVyqvQVYSWOTx-MqXNKWoYzeiHxbNeILKVPF1Jb8uSBJb2ReSgpjfSsrmXpgmSZ_Gq9WfN8bXL7DebjeETA1s46nV2G7rWmPerbOZ_bLOkzK8Ov2M8-V3xBvqtzVmL83pcYG1vNyPJ9u8FZLGxTnlIymi3TtYkTaD1TBHSBMkjmf4w1z7Nh-ZoGYcu9g5-zvg0WYC1vgg7zMzJqdVUcWf7nvwCPyMCeydYDtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
عشق به مارادونا، با توصیف آقای گزارشگر
🎙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107661" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=YyfPCrokakhVoqpZ5kz3lV4han_s2jWJAedDoCM2Mke0qRUV6gVkuaAd4-lEBBVJAFa_mVGGmJhymU9gm6fi5HWXpMlP3Hdf0D8Fee_PYSQgRYXKJD_SsxcGoubXVH2nBjEQuoXmLW4iEzLC3FDvO6b4bi3UuQGbZBJ5F_gR_LlOOVxFWdpcJ1zlVf7fjSmA6gzqrtLdfFjZd6dMns8BnCRecoWBTjMpImF8IHurb3Tecm07py4NqTHbJJTJA-XGjfK9i6Lq9KarHyu15_DuKX9hC5B9FROHXp5hN4zllEv2UID28xsjMgfAG67FqjXBdWVMoICL8BIPtnOh4l5YEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=YyfPCrokakhVoqpZ5kz3lV4han_s2jWJAedDoCM2Mke0qRUV6gVkuaAd4-lEBBVJAFa_mVGGmJhymU9gm6fi5HWXpMlP3Hdf0D8Fee_PYSQgRYXKJD_SsxcGoubXVH2nBjEQuoXmLW4iEzLC3FDvO6b4bi3UuQGbZBJ5F_gR_LlOOVxFWdpcJ1zlVf7fjSmA6gzqrtLdfFjZd6dMns8BnCRecoWBTjMpImF8IHurb3Tecm07py4NqTHbJJTJA-XGjfK9i6Lq9KarHyu15_DuKX9hC5B9FROHXp5hN4zllEv2UID28xsjMgfAG67FqjXBdWVMoICL8BIPtnOh4l5YEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اون بعضیایی که میگن از صفر شروع کردیم ولی خب ؛ صفرِ شما ها، صدِ خیلیاس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107660" target="_blank">📅 10:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNkZdjYlpOsX6HSl6uIsGfREB59BmCvTl6k5VP7juIcU9BmLOUdE5qxo3VRHkvGDghVSJqqBvy7CkIEcnGv9FRMPqSevbyRU1yZcc03xeGRONKd43sL7jWC_jgvY5jESpIqVtYCxjW8PsLIY3IEi2i6mBJVwlponTgOO1hB9DRBZxMFpakcIn-52uvmTeakoljh9nqBjV1OYn00tpvqQEndOgolIz5OJsSjIyvGo3f23MhueotsNRFHAp4v5y0vl5oybKiPysuUnyHfJEXChSDr1NHTs65Nx39azb3OpJRaR4_rpdm1tzlX934bwtlFwNjb1z16daIywrKMN3I8FVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
بزرگترین ورزشگاه‌های تیم‌های ملی در جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107659" target="_blank">📅 09:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkAHAN0aEddMZHKoUw4sRF28pLwhiN9wo72lFG0OnTUQ4hzBdJSDMJQOR-Is1dAlvHtj0n70pF8X1JdxST6qVqCzD1rSsvSPUSLF4nxPp84OkcsLd5JH7bFzzHG0A7Myc7K4idvGrXYIvh3mAGAVi5DQqu_Su9lbcUW3nDoPv2vlW_KZ1TiWkwGfSnS0ngX70hBCgvEbUSbMUL6R24_X-nRhs5Cps7vntEp_lya1lnF1cVnSldHBVvgwyvRScuAspM5FLfUDMznUdLIghAKwHf8vj1OgP6MlQvsTIPgOJqAz8AiS3WF7BDbmSCgx-kakuNUq5sn4wiUtNKL-qh_t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🔥
آمار و عملکرد مسی در تاریخ کریر فوتبالش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107658" target="_blank">📅 09:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85455aa172.mp4?token=D8rmm8ktWsm-Vq5hslzIFUQmFae3PP1M9DXD715m34iO3q22SNdWRI-Egb9rTJVjHXr5Nlo8t_1UKPNS3cjCVpsz_FetFAx8ZzuMB6pRd4SGOqeoaO3sArUn7rxiaf3c6E_a04ljvBeCYk8QA1VSN4GLEe1PkB1NHKgklY1UpkCDocgoFYwRpgw3q3iHu4a887lzwkgf4PEM_8cfBL3rJEqGHyA830Jq5bPkpZXh4ZCoe3cl35_y0IS3hHviGaUaDqXrwih_yOnr_AaYsNcTm8j73DjR-kBmLPJwbQ8F6ocDmAVo_r4WGJofVY7qu2FzMLIMOrvSCiNW4O07sfurF4a6hUiYzPNaucZsRRCUYm0WQNFEDXadeastlWMJBy2piwfOcdRzx7mN1kjBcKTwDY9cLefgDJKGrv5CO6Ix9A7cWbC-UYj8QqzEvd1P2-R2WILkESsZAx68D5TUcbbFsuXxxJe25CIyvcfdrIB-iVGH7OhujocaR_Re4SQ8XkWC_vo5yZHcxqC3EZ2nYGwdatloV2bERaw716c2V447V3yVIMkBGLTGGUMnVT09SUk7YYsyN9ZEx48leMcFIl_eFlToA2ZpNOddXsDGkg9rYQpqfJYyli3d7JPB9Jua_C_fkv-k-lF_TDCaDDALW8ppCxvouWMp_bHLNrQh3WsvmtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85455aa172.mp4?token=D8rmm8ktWsm-Vq5hslzIFUQmFae3PP1M9DXD715m34iO3q22SNdWRI-Egb9rTJVjHXr5Nlo8t_1UKPNS3cjCVpsz_FetFAx8ZzuMB6pRd4SGOqeoaO3sArUn7rxiaf3c6E_a04ljvBeCYk8QA1VSN4GLEe1PkB1NHKgklY1UpkCDocgoFYwRpgw3q3iHu4a887lzwkgf4PEM_8cfBL3rJEqGHyA830Jq5bPkpZXh4ZCoe3cl35_y0IS3hHviGaUaDqXrwih_yOnr_AaYsNcTm8j73DjR-kBmLPJwbQ8F6ocDmAVo_r4WGJofVY7qu2FzMLIMOrvSCiNW4O07sfurF4a6hUiYzPNaucZsRRCUYm0WQNFEDXadeastlWMJBy2piwfOcdRzx7mN1kjBcKTwDY9cLefgDJKGrv5CO6Ix9A7cWbC-UYj8QqzEvd1P2-R2WILkESsZAx68D5TUcbbFsuXxxJe25CIyvcfdrIB-iVGH7OhujocaR_Re4SQ8XkWC_vo5yZHcxqC3EZ2nYGwdatloV2bERaw716c2V447V3yVIMkBGLTGGUMnVT09SUk7YYsyN9ZEx48leMcFIl_eFlToA2ZpNOddXsDGkg9rYQpqfJYyli3d7JPB9Jua_C_fkv-k-lF_TDCaDDALW8ppCxvouWMp_bHLNrQh3WsvmtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ابوطالب آماده ورود به فساد فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107657" target="_blank">📅 09:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107656" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107656" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ8FYAjqNpR61yasaUJHMECuMHlRCkL5w7JRjNuVVOFnd3wmYrBk5hljA3pPR5phzrz92yGKbA_YamJ8mAhlccj4QEED70mrNxAAL6qExwsvS5BvzR2yTSpsTzQV9uI1O87y6uaT5KU-dIZoFGqiSwA4J9cmui5FUyJw9FkZ9Zgj-WKL_vV37bGO8OIEZKcgBoBAO8sUlBdo49yboMWQLS0f4GGQn3yUFd6LMvtMZPTEeliyW3bFnwuDqZD-gVd2HUZ1FhZTljZAJGY022NUuVF5sfddilb7D2LwmOg0oSwFYLFWff5HhnVi5HnikXxKx2JenfYr5mfz3yTzmJfJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107655" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107654" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7X8ojgSWaIWf7aU-6pgth32ikSDHf14A2FonVkRF5n2Toi3zgHNbdNvXADxSDzbw0qK0Ct5mcbkO4KjhHpgHrEopLRbvkxh9mVFYIRV9SYD4HK0RmDvcUs-AWtfdnbqC9HAx1Gax_lTILrIp60bVtPRYyqWJw48F_8Gen1NYFsnMvtzm1c0ntWVQLkQIbZ-0caAUvaRFdzhdstE2_4ZYQXCLj6CTRlEPpu2CzZUgefnShmJ5DoMlB-6fCOZqReK24yL7sy1hc1HPv7urEM10dL4Mv9ClfnICP5z2OCrDfgDOf_GUSU-103h9smCMp18QgyGFODpE1zjn3a4EFyFsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107653" target="_blank">📅 00:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URyNP9NFD64NVbx5Np3OqGYLHdvmN9F0WVNtPBmxA-QMwEPcZJJXfEQiU7toHnqe4SxYbefZE2CLeE9aci8HpJ-D8OjWeU6Zl8Z6x_j-hsMrkws5fU31VJa5_6ohv4hhSZInP6RcWBxXw21RcyBV8mQ0U19XtAqT71Mxj8rifBKzXqu3zu0FkkZ_DhNUEaO6CsBAlqtOHA6ufTO-FFtbqNGHDJbLQDwz7nSEtv5AX1WzJJrttOc2Q3-Xc0s32MvLyUWNM1100TwIBCXqDP0R6IAtpn4UAiDbvOgXFcJQ5VExVZtLIpeV3yaMNULItcHs3ZOWywhAyLMS_vl3Lsvt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107652" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzODLpAOEJEdrhJFvauTmYyCxQ8lVUEWOP9-Ri-SA_LE7Oh9GkBBD10p6tmunaF4CT775NSpG4o5CVqQCUPP0wuQkwDvsGYdetVSAJRO3OI9IyquQdtyxHl4x4-tJKhgg2goEnctLZojBDOcG9NJTrtArd9ESba_Gz5qsQwb98mhmzccPk-zmIPwXs6X0Tcbmzz_S5vGmrGF7bsSr24FVsabx8TAuvmG-_OWPZIn3n4U6Yzx_3esOJYwfF4v7MS50ggiB-f7NWdfSaLjX6pluGqqeeh_dFGwSfuuOgv09Lnyo2n-o3GrPncH9-dfnA-kkQeBKay0T5gZ-kgSsQMRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
عملکرد فِلیکس تحت رهبری خورخه ژسوس در تیم النصر و تیم ملی پرتغال:
🏟️
50 مسابقه.
⚽️
47 مشارکت.
⚽️
29 گل.
⚽️
18 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107651" target="_blank">📅 00:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=YYnrc38xNlj35P996aGJbYX9ciLseBLQl8hePWlrYKYVJESzsV_6JnYujgG1L0FCn2jVxV0udF_130Lc0NIo04aiPr3I9f0y5kmTUKBkCBP38VrFiQlv58M-jVM-adgl8IZ1jP-6uLuqBapib9_kCoGA8u43Yxym6yPz2m-YLrBVX8XCseo2hjTIDN6oJVzxs2gV1UVgebyf_PKcZtrn8yEKH8t5LtwMkCWwzuP7YkwwHAAA_RMJFf7UL7gXLdmTTwfRnnfmW1RIEPMvzBLBpIP8C3ZpjogcsWvG6fhaxuGUEcSd9sy4uve4E6pRz0XZWyaBhEiHxzRhzQlF7_gaOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=YYnrc38xNlj35P996aGJbYX9ciLseBLQl8hePWlrYKYVJESzsV_6JnYujgG1L0FCn2jVxV0udF_130Lc0NIo04aiPr3I9f0y5kmTUKBkCBP38VrFiQlv58M-jVM-adgl8IZ1jP-6uLuqBapib9_kCoGA8u43Yxym6yPz2m-YLrBVX8XCseo2hjTIDN6oJVzxs2gV1UVgebyf_PKcZtrn8yEKH8t5LtwMkCWwzuP7YkwwHAAA_RMJFf7UL7gXLdmTTwfRnnfmW1RIEPMvzBLBpIP8C3ZpjogcsWvG6fhaxuGUEcSd9sy4uve4E6pRz0XZWyaBhEiHxzRhzQlF7_gaOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌چهارم پرتغال به دانمارک توسط ژائو فلیکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107650" target="_blank">📅 00:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلگلگلگل چهارم پرتغال توسط ژائو فلیکس</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107649" target="_blank">📅 00:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbdf1dbe2.mp4?token=YKZ3Zi2btPWbi0x2uHv4y0g9B4NxUf4qhrJ24f8iK5hO5ZhYZqiegCpd-fXOJz7m_hHpLxHHBu9xOpaLGeIfvMnzbV2xbdOchVT29hIvcweMESB-DwozSfXnqpfLc_9F_s1E_p6Z5VJFLJPFxi4jrRhcFhRRrEFpHLGWgPdPNBMTwJD0oycMpr7j0ZhepHL9KhzTEA_fWDQCL87xdIIP34jzJ_XtL1ArePdXxL9dqB1ak6ZjavSeqFrqWkQ61jxfDz8eSlUgEHEg1F3f1gvndo7Sv25R8THfbpCrmmbGr0B7sglOzaCgT7mYowBTJ_VZJFdOKf3MinKOAiHvYKZ2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbdf1dbe2.mp4?token=YKZ3Zi2btPWbi0x2uHv4y0g9B4NxUf4qhrJ24f8iK5hO5ZhYZqiegCpd-fXOJz7m_hHpLxHHBu9xOpaLGeIfvMnzbV2xbdOchVT29hIvcweMESB-DwozSfXnqpfLc_9F_s1E_p6Z5VJFLJPFxi4jrRhcFhRRrEFpHLGWgPdPNBMTwJD0oycMpr7j0ZhepHL9KhzTEA_fWDQCL87xdIIP34jzJ_XtL1ArePdXxL9dqB1ak6ZjavSeqFrqWkQ61jxfDz8eSlUgEHEg1F3f1gvndo7Sv25R8THfbpCrmmbGr0B7sglOzaCgT7mYowBTJ_VZJFdOKf3MinKOAiHvYKZ2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌سوم پرتغال به دانمارک توسط ویتینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107648" target="_blank">📅 23:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگل سوم پرتغال به دانمارک
ویتینیا زدددد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107647" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هلند گل مساویو به یونان زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107646" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
وضعیت هلند تحت هدایت ژاوی جلو یونان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107645" target="_blank">📅 23:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b7e5010a.mp4?token=DGbjntJi91t6cMWh0wxTRJz80i5dAbbqL5qfTbtzuFTTtAlZWooj-MlO7dcNS9raCNM4XDVcyKzxL2w0C0wAexWRC-CkiZmV6QGccDPXO01fXavaMbxW6KAiQeo5bPu2tlF6HK5RHo6zRlvbBEkJ_biga6F-nMyGdWrJwNzvXlmq4cKzN47lFKk6xa6gqPJM55Ml3fuSsnQfcn3DhOKvrC_J7eCfwqvl2VtGoB7VRfAFpMq_psL90vjdTn2HX0aRZdI2_RafhPtQWeJYgv9_qugUmeSn2A8rt0pjGHOjelY5BvhB7q8l6Y6BPRY_IKna2gpjsbUnHlCG0_RSOW1_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b7e5010a.mp4?token=DGbjntJi91t6cMWh0wxTRJz80i5dAbbqL5qfTbtzuFTTtAlZWooj-MlO7dcNS9raCNM4XDVcyKzxL2w0C0wAexWRC-CkiZmV6QGccDPXO01fXavaMbxW6KAiQeo5bPu2tlF6HK5RHo6zRlvbBEkJ_biga6F-nMyGdWrJwNzvXlmq4cKzN47lFKk6xa6gqPJM55Ml3fuSsnQfcn3DhOKvrC_J7eCfwqvl2VtGoB7VRfAFpMq_psL90vjdTn2HX0aRZdI2_RafhPtQWeJYgv9_qugUmeSn2A8rt0pjGHOjelY5BvhB7q8l6Y6BPRY_IKna2gpjsbUnHlCG0_RSOW1_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
چیپ تماشایی هویلند مقابل پرتغال و به ثمر رسیدن گل دوم و تساوی دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107644" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnTuh2GGvblZMS1_t3IIoM_5Qc1wvDExZlA3ZakXS0VYZlPDe-Ya9eGMYLlTackt3ZM-KLDQYf4tgWWmi4p_7ugr3jMDvn4mnwFv0BrL5I2HcBfvh75ApolYlLZYD0zXdafzRRgWwGUOeyzCqr2CN5y4MYrTWoRgEJH7691bRwu35DfUvNf3S4csku_tuiIWeOLQVTv-e-ciJSQOuv7eXE6PNGsKs_zPiuNStU0oDZvQPtNN3UC4XwIEKRVOb_XTrl9VG1M1ewR8hLSHojz3CkrI2WzMJ200wUoYx-XrYK3BqtiwP7u8gJNt_nbREz3wJPJCfVaOGJcahYfe8FkF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت هلند تحت هدایت ژاوی جلو یونان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107643" target="_blank">📅 23:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhwuLEWBzxdibunIRoyRcE3FZwHoLnP8zHJ3jKAMXSadRsm8MulnnTXMuX1vYMya4ppeCNmj6CXzx3UCdXTOdelMIdJGxxy_mlJZewdpuXhsPUOTvDaSoIubO57N4i4BaNhNVxgTuLFZfHSlo-3P_I2PyQLwOyyZ32NZtXxpaUyMFif6YYSXx1Jt6t7p39BLPEs40au-sYcRRtMhXi4RlnPWRulcgmW2oDyN9KEXZCovYAbfABLfYUnX8CSpkMOE6Kj8VzziaWKXjnLe2gnpM12pVDHdJL9z57B-4dqo0PKJ4ZkQRGMqusvJ2e9ocPJoGrGfR5xuouMFOr6Ew1m62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🛍️
فوتی هدلاینز :
🔻
آدیداس قصد دارد در سال ۲۰۲۷ لیونل مسی و لامین یامال را در یک پروژه ویژه کنار هم قرار دهد؛ پروژه‌ای که نماد انتقال مشعل بین این دو خواهد بود.
♨️
همان سال ممکن است آخرین سالی باشد که مسی کفش‌های اختصاصی با نام خودش دریافت می‌کند؛ در حالی که آدیداس آماده می‌شود پس از بازنشستگی این ستاره آرژانتینی، لامین را به چهره اول جهانی این برند در فوتبال تبدیل کند.
✅
انتظار می‌رود مجموعه‌ای ویژه با نام «Messi x Yamal» عرضه شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107642" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069b82ea6e.mp4?token=ftrUAuV4RmBS1jv2NyKFvR8EUB6CJZqWnDlGrRxPRyGINgePvxghRQf9pUoQj1CbHiegyPKe1RJbsvYZsQxvAko-TfIHfd78BSIqDxg6mKuBal298yG_jhkXgMBSeA_aLqu6hVfL0qAxe61P0JlSuDeXVjFzVsSweOp_rg6HpennaPAOP9pkh5-rgfaXDYi7v6eGItp3J4IZH5VLcDZ_ojOqtij31Szz9-O4uczHsme2_zNjoAZN17RTnizX_NBMFSSxHpcgClosRuUaggUTsy6t5dZo3aG6kS4DYt7L3w3T65DvtdMoy2bBshd9n9bVrr8_81CD97DRAVW2ymHIdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069b82ea6e.mp4?token=ftrUAuV4RmBS1jv2NyKFvR8EUB6CJZqWnDlGrRxPRyGINgePvxghRQf9pUoQj1CbHiegyPKe1RJbsvYZsQxvAko-TfIHfd78BSIqDxg6mKuBal298yG_jhkXgMBSeA_aLqu6hVfL0qAxe61P0JlSuDeXVjFzVsSweOp_rg6HpennaPAOP9pkh5-rgfaXDYi7v6eGItp3J4IZH5VLcDZ_ojOqtij31Szz9-O4uczHsme2_zNjoAZN17RTnizX_NBMFSSxHpcgClosRuUaggUTsy6t5dZo3aG6kS4DYt7L3w3T65DvtdMoy2bBshd9n9bVrr8_81CD97DRAVW2ymHIdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل دوم پرتغال به دانمارک توسط راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107641" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753494da36.mp4?token=nOee6PDD_0OlJglGfNDxDDeuWordDTp8yx16Z8LpIlgg2SDjwZxiorqCkVk70SQMiRkAjldgbspHEXa9P-u9Vg_6Sy6djvl2zUJE0Pq4F6229_vf0zp0GskW1aeOGgEeeTVWXl__0PNQa4Nz1TmUKQ9Y_ehT_3DveMtK72zd8HirRL1EgJrTqXMnvKMjrVCuyV6aTO7lNQS_XLnGsQPVg5tSyDcHVq2slHDxdoe2ScMqHkLHpaxtiqAUngVtM-iLnismodG76nsOFxxMe5-1WJEszvqdKor7hPQ6shBR-pSVaRe-Hhidl-miBRpJv6sY-Wm_NcnHWBVf-FCrUeKZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753494da36.mp4?token=nOee6PDD_0OlJglGfNDxDDeuWordDTp8yx16Z8LpIlgg2SDjwZxiorqCkVk70SQMiRkAjldgbspHEXa9P-u9Vg_6Sy6djvl2zUJE0Pq4F6229_vf0zp0GskW1aeOGgEeeTVWXl__0PNQa4Nz1TmUKQ9Y_ehT_3DveMtK72zd8HirRL1EgJrTqXMnvKMjrVCuyV6aTO7lNQS_XLnGsQPVg5tSyDcHVq2slHDxdoe2ScMqHkLHpaxtiqAUngVtM-iLnismodG76nsOFxxMe5-1WJEszvqdKor7hPQ6shBR-pSVaRe-Hhidl-miBRpJv6sY-Wm_NcnHWBVf-FCrUeKZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به دانمارک توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107640" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=NIboviPVY6U0HC8dIBgHzD5vGHCJv87V8rpDbEyenFAEJs85vm8JLboekYP8pRCsGbzQ4q9lRMQlcjXL9Eoil6-7yTZrBhCZMPzwt1bIGV9C_NG1-n0w7giA0hW2qI8k_qCCPZgmrMYQkF5O0ID9OJJkfUvgu6ncJnbl62rYUq-hMZda1B2laQJ-W3x6NDv6upo9NU6PEdcKUucIHIOrFlCv5-CLI7LR2qFUYJSlv8Y8n7d5CuxjXcV1henLAxAfoJ309pVZuhCEdQueOmiTD-K431EvdlpY4xkTkBI_ODQ7cbn4Euk8U9NOVEcc21NtrGCU_dFPRaN4VkNM_oEbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=NIboviPVY6U0HC8dIBgHzD5vGHCJv87V8rpDbEyenFAEJs85vm8JLboekYP8pRCsGbzQ4q9lRMQlcjXL9Eoil6-7yTZrBhCZMPzwt1bIGV9C_NG1-n0w7giA0hW2qI8k_qCCPZgmrMYQkF5O0ID9OJJkfUvgu6ncJnbl62rYUq-hMZda1B2laQJ-W3x6NDv6upo9NU6PEdcKUucIHIOrFlCv5-CLI7LR2qFUYJSlv8Y8n7d5CuxjXcV1henLAxAfoJ309pVZuhCEdQueOmiTD-K431EvdlpY4xkTkBI_ODQ7cbn4Euk8U9NOVEcc21NtrGCU_dFPRaN4VkNM_oEbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برونو فرناندزی که خیالش از بابت کاپیتانی پرتغال راحت شد و به خیال خودش از شر رونالدو خلاص شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107639" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ژائو کانسلووووو</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107638" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پرتغال زد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107637" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گگلگلگلگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107636" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یونان یکی به هلند زد که آفساید شد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107635" target="_blank">📅 22:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107634">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-buD6LaThMwGPfYv4eJrkCaTxxKOzNqay8FK5_xMBorZIsaszagVSc_8megkcnzuyuZmKKOvYW6mmBcpwQCb_6gHfhSxWNtcpevoxSi0CSEjWRbOSbNIC71qGzzjI_yF-687A_gOk7eFV_3QLZQirxlYtrIjSUtZhIOX7J5zBhzeA2JJjZeye8TYWKzY0MYMzavvpKYVopIskQl3zlZRDtBMI1ENHgM4z2UjvgXsE3771c1wslQK6SjO_3039fiZTw7EjcqDhJoUHxSOPeEGjodQrzvqgnkvHcEyRIB3D2TI0CZcxQek8G-sW-hZhhrOrQoTCa-p3lOPxamYUQAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
شبکه رسمی رئال مادرید:
🔻
کارنامه آقای گواردیولا، آقای ژاوی و آقای مسی، همگی زیر ذره‌بین و در حال بررسی هستند
🔻
تمام جام‌هایی که بارسلونا بین سال‌های ۲۰۰۱ تا ۲۰۱۸ به دست آورده، زیر سوال رفته و تحت بررسی قرار گرفته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107634" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEc67fNz-drlrG-XIcrEkaO6-BifTtJx1AJGjzOjN1obGR6gjblhajerozCykeBop6XF9WQUgfy5dsE3hk8FJCvIOv_9o3nbFXWe9uFP-SCwuQ3LGkm6TajFSrIBEFDE-ce1KbcXWy1JOXFO7s3IY5CxES8OruvwLkh3rZ5HaVu4eEm5AaaJZWA1-FmekoBrTsSn0gGIoRJywJaKaF3H0DLZnNi4FW0YbO5w8V34D4-3ZLzqumPnKXyWBO6bBqOHCKF9YgD-NfjbK3quSRQ9272vP3Wh2Ljy-h4I6ygg13hyG7h_ngcEmZae4CJsyTvgkt2ww8OKhW-gtDImjq0yWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
باسکال فِری، رئیس سابق تحریریه‌ مجله فرانس فوتبال و مسئول سابق جایزه بالون دور:
‏
🔻
در حال حاضر، و با صراحت، من از لامین یامال کمی تحت تاثیر قرار گرفته‌ام. و شخصاً، جایزه بالون دور را به بازیکنی اهدا خواهم کرد که قهرمان لیگ قهرمانان یا جام جهانی شود. این دیدگاه من است.
🔻
یک نامزد، کمپین‌های انتخاباتی را در تمام روزنامه‌ها و به زبان‌های مختلف انجام می‌دهد، فقط برای اینکه بر رای‌دهندگان تأثیر بگذارد. اما من با روزنامه‌نگاران و رای‌دهندگان صحبت کردم و آنها تأیید کردند که این موضوع اصلاً به آنها خوش نیامده است.
🔻
این بازیکنی که من به آن اشاره می‌کنم، خودش را به عنوان "انتخاب شده" معرفی کرده است و من فکر نمی‌کنم که او این جایزه را ببرد. و اگر برنده شود، با وجود اینکه من این را باور ندارم، این موضوع برای آینده این جایزه خطرناک است و باعث هرج و مرج خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107633" target="_blank">📅 21:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a570eeee2d.mp4?token=MLYkdBq9n9cCY8uKzAHLfSpgjWu_LioSDXUavGwOhHHAo0jMUmYvfZmwNg9rCrX_FJ-V3Gnnqc_B5k6XACGZel6qZyKYc2gY84l3hyw95RasAWZeLLnFdGX-Ats0aAfbeaXzyLmnF-6XE7-E-ukDIxBrWSwU4vq02fWWCGCfxZW2DcAq6VfRvxVA5K3pPdrWCpJZ77RRptQQ_FBJpEa67vzUg_gFygb79W7nbVWRleSoJyrmKEeIpm5NRJc_AsAeoyzg3DnqFNEZjU7wnwJ5pXD4dBfIwxp4LWKdzrwNSCdNTL76IcU00xGlTVak_kBoU1rUCeO3tH_gADdEO1NBVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a570eeee2d.mp4?token=MLYkdBq9n9cCY8uKzAHLfSpgjWu_LioSDXUavGwOhHHAo0jMUmYvfZmwNg9rCrX_FJ-V3Gnnqc_B5k6XACGZel6qZyKYc2gY84l3hyw95RasAWZeLLnFdGX-Ats0aAfbeaXzyLmnF-6XE7-E-ukDIxBrWSwU4vq02fWWCGCfxZW2DcAq6VfRvxVA5K3pPdrWCpJZ77RRptQQ_FBJpEa67vzUg_gFygb79W7nbVWRleSoJyrmKEeIpm5NRJc_AsAeoyzg3DnqFNEZjU7wnwJ5pXD4dBfIwxp4LWKdzrwNSCdNTL76IcU00xGlTVak_kBoU1rUCeO3tH_gADdEO1NBVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
میلی گلد این فیلمو از طلاهاش منتشر کرد و گفت دزد نیستیم و پول مردم رو نمیخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107632" target="_blank">📅 21:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpQPYfAgyWN7eHXhnhnkP9uK1r7CGEC6EHOzjKHJCYOBbh12O9-u7VhRc_YrQNZQwLMG1P808xq4015_8MMquYdohB9Sl1RgstGJzh60K7FULH6JUa_EDTtovTkcM0iFQJ1b7gagcwddWHGZkBf9rqG2U3IiJNx8_QKEJx25A6praNtav-s8Qjn7o_8kTT9yGPI9GB_QO_tbCfnVOXQIkeWsihu5xYIq1ulGv2JF5k7Eyyn-zWWUn2sWARgYIsadgl8nKyIrpnco-lrqnjudkdpi2Y8nEZ3fhiQXdk0M4lhT_7xhDjWd8WdJrBtBOUS2dylJcDmckd5EJkYwMGAIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ترکیب آلمان برای دیدار با صربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107631" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇵🇹
ترکیب تیم‌ملی پرتغال مقابل دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107630" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxzEsi94n592H_wSWmugLjqGdRHjCpDdZs-7HZUgxW-XrorUMOVtJcc_m0PESs1CS9DQdrAl1Qkfxfoe4hdQ1YBL3PLDOvXKrmM5j4cWP7iCnaPxUgcuIuATsXlFPb8FJI-JIxV5ZQGXS7OdyJEMNDKetKQQER7MUqQMS0B0zJpF3XkU9vUPmgIFZtsXh2J67n87ZunxcYYvLtssmxX9wAtxiJHsHjxj0nunOzFlDK_nqhPKqR6AKpEhaiUsUpKyRwKYEbj3L_8coVdNkSEmxRtUx-zLsxMEDeAWNFv0ONR05Rn5suHfh14iK88UULLfnErF45jW8enWXCsYuJg-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب تیم‌ملی پرتغال مقابل دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107629" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI2z5kNJMtI4joQcBnzuEtLJ2fTyh3CTpR2i3EODCAXhuTPwbT7kviqqj09DbyK52MZEtTtnCJXzN57qStfn8VZLGEWpgepK0DCp1rAYIXhP78w06VzkxchqmLXqAXFr3_bxK8MRu50FaXMZjaWzGvD1lr_mpMlixymdjuUqU3piX8M4ACgp_mGp46wd7MCmz52Mn6KTWVyKDEYPGRClaP6XNJi-4p-cMBF2IwYAr5RNkHNK-r_mCsSjhlsJafjOeG_MuI0KxzhpeMxMWWr4Dquh6wAUOrQ565m0zrm0A8l6Aktv1G-Mm8mB4ltxBYzAScLMGSUqoemZogio-BL23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیونل مسی، مالک جدید باشگاه اسپانیایی سی‌دی الدنسه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107628" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b37d3dc9.mp4?token=b6BaSrin3OuXIKQ-SeCtAa79cHRpadn8YNho_O2iIdag1dPgaZrUSgevEMl0DjqoqoEl-vdRsz00l-OVlmcpv5-2B6k2xoNSY72PrtaGrddYCH-wYYLK1LNqscy-uRERPFDvmSW5Zd8CXfENkd-hf7_f0qMOG8JulHQexB68HCdsaMqPYUy6FO1F0OYJCxmpvylLZgAEKSFkb1UU26U1rN9lwJnRs-53DabhDr_JqI6vqCXb2qkr8yKBpQtuajv-vHguKyJQ4orp80J1vXCVcVt1ky76r97S_aYEBK1X6evlVGtEd9WXJDvBP6cTTJlGjRYGnqGQ0ewslmba91Hajw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b37d3dc9.mp4?token=b6BaSrin3OuXIKQ-SeCtAa79cHRpadn8YNho_O2iIdag1dPgaZrUSgevEMl0DjqoqoEl-vdRsz00l-OVlmcpv5-2B6k2xoNSY72PrtaGrddYCH-wYYLK1LNqscy-uRERPFDvmSW5Zd8CXfENkd-hf7_f0qMOG8JulHQexB68HCdsaMqPYUy6FO1F0OYJCxmpvylLZgAEKSFkb1UU26U1rN9lwJnRs-53DabhDr_JqI6vqCXb2qkr8yKBpQtuajv-vHguKyJQ4orp80J1vXCVcVt1ky76r97S_aYEBK1X6evlVGtEd9WXJDvBP6cTTJlGjRYGnqGQ0ewslmba91Hajw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوضاع فوتبال ایران با این آدمای لجن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107627" target="_blank">📅 20:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d318c00047.mp4?token=VcfP90rsEc1mDy6_uvueKOhYMH0H63qDpPDKxGOm7aU6tbNLAk5MDVEA14xL3SdPOFEaLXxedEQUM2y_LrlXp1CDsIfMyzqnz8DzSgBF7a9AV0oG3KSkYSEAGP2bM-mi8cvqSjqi-rU_SO43W9fnlqwi53_80fvANAlNbNc_-oLsF3e9MKikJt2jTWEzhGPjZ7K3BmvPt2pTWU0BTYApwSWcAb72t0dSTcAo4CPJetg0P28HOB_6_7KHFofw76NPQsIjfWHEEK_F4qf1VAmDDkesaeDhA3_jnd_3UXXrQlaa0ltah8iUTHiJd7jK5qu2s6h0cvmtpPByu-6p-KLAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d318c00047.mp4?token=VcfP90rsEc1mDy6_uvueKOhYMH0H63qDpPDKxGOm7aU6tbNLAk5MDVEA14xL3SdPOFEaLXxedEQUM2y_LrlXp1CDsIfMyzqnz8DzSgBF7a9AV0oG3KSkYSEAGP2bM-mi8cvqSjqi-rU_SO43W9fnlqwi53_80fvANAlNbNc_-oLsF3e9MKikJt2jTWEzhGPjZ7K3BmvPt2pTWU0BTYApwSWcAb72t0dSTcAo4CPJetg0P28HOB_6_7KHFofw76NPQsIjfWHEEK_F4qf1VAmDDkesaeDhA3_jnd_3UXXrQlaa0ltah8iUTHiJd7jK5qu2s6h0cvmtpPByu-6p-KLAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇷🇺
پوتین:
اگر حمله‌ای مستقیم توسط ناتو به روسیه صورت بگیرد، از تمامی تسلیحات متعارف و غیرمتعارف (بمب اتم) علیه آن‌ها استفاده خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107626" target="_blank">📅 20:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8054bb57.mp4?token=me1edHyBGNmyQyyGNTnmw7gmT2tY9x8ZStt6XyTn-FlgCxZyb0x5YPB96w3mxXWJxhPAz0uvSWlLHrmlwAbpgwo1xDHfe8TScQKwbo2aw00L8S6mHfqS5IPv-q7z1jToaLAX7AFrD0haNIJOlCRaKzjMfhVG2ZlQIPLIScNxj_2kDrfQE51RQFGoOMdYQFvNAZrQVAqxn0NkR4r0a8J97MGdq441EaZd3mVyb4V3X1iLYK7LN2MSCWt9paPpFJ1wBZLe2Qf__pGfgkXMK8Df1XqlwYBd8vk-i4uQzWnE2XVODup7HWF9FzRz6AgIms3C1WCNq4rOFKQjPjEcw7AFvIHNx7jI8AVfw2kV16BwHMJSnjt-nN8XAJ7GM7nPEi8OoOhlYJev6W9148tZtDAS_Iu0HDUP9v5LAYeVYu-KztPJZzLJshe9nBLsc4NN1llvUgXNl3x_ozepcC7uuWtBpUuzArJtXqoQ4mqKbg_LybRihgbBlYZ5Uf-CEC0gogTNrYn16piKHsnk4dbp1v7__cM6f2o3Qb_bTtUENN1XWRj26MsFSqRlhB0Ds9-v6gskQJIxgy9wTsWsQjda8904N1dzAvZzic09lr1wJe2Ixbm77yXY4RguwKQbN70yI-EsiYm_5PYI61FICurBCvGn5Ji0exUIrwGyJVzDJBg20B0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8054bb57.mp4?token=me1edHyBGNmyQyyGNTnmw7gmT2tY9x8ZStt6XyTn-FlgCxZyb0x5YPB96w3mxXWJxhPAz0uvSWlLHrmlwAbpgwo1xDHfe8TScQKwbo2aw00L8S6mHfqS5IPv-q7z1jToaLAX7AFrD0haNIJOlCRaKzjMfhVG2ZlQIPLIScNxj_2kDrfQE51RQFGoOMdYQFvNAZrQVAqxn0NkR4r0a8J97MGdq441EaZd3mVyb4V3X1iLYK7LN2MSCWt9paPpFJ1wBZLe2Qf__pGfgkXMK8Df1XqlwYBd8vk-i4uQzWnE2XVODup7HWF9FzRz6AgIms3C1WCNq4rOFKQjPjEcw7AFvIHNx7jI8AVfw2kV16BwHMJSnjt-nN8XAJ7GM7nPEi8OoOhlYJev6W9148tZtDAS_Iu0HDUP9v5LAYeVYu-KztPJZzLJshe9nBLsc4NN1llvUgXNl3x_ozepcC7uuWtBpUuzArJtXqoQ4mqKbg_LybRihgbBlYZ5Uf-CEC0gogTNrYn16piKHsnk4dbp1v7__cM6f2o3Qb_bTtUENN1XWRj26MsFSqRlhB0Ds9-v6gskQJIxgy9wTsWsQjda8904N1dzAvZzic09lr1wJe2Ixbm77yXY4RguwKQbN70yI-EsiYm_5PYI61FICurBCvGn5Ji0exUIrwGyJVzDJBg20B0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتایج بیلدآپ کردن امیرخان در تیم‌ملی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107625" target="_blank">📅 19:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce141f49b.mp4?token=QhWwFWDwWBJ0_OQ3y1CcCPD29RR62WdSdcCwVP0vuHnX0CwwnXEGUiqss0w3XUI0xqfmXGXLemfyHA3_bq55GapRksi4Rmr3M9e2ekEtb_mikd1-C_OtyDHNxODzhtBC_2w6LT9mTAf941HEZ3o_2aVSjUU6vQG_yKnGsNB01bkb_KFMeCnTgewL1qLnO_6mEtGBb0uZOo32JgIZAaKEDBt7TI0ntEGCRe-m-lfSxa-mKk2IP-pJcbuFElJabRX2uFgfQiCpVrmKTI_m-uNr5t33SPn1SLESyN4QGYTT2Xm-3CHgqOrafc6iyyMU4On7Jgt0w1qn3ybCTIjX-RRL5zHM-Df-SBfcjfMzsowhtokbmnsGUa9bYfhJusk8hvviYzuGBnQvi2lFipayDKbd981cMqUjWwB0NOYwIqNLMmk1hpbulAKwb5JVkCXiznuURDXRlohcEOyqBUr__3vMMS2Lcct8m5wk1c2ypJ7tBE4LtcobpspgL-qbNsQvpYUK9qVMkSk4YxgsCFCMEvKWPgEM9nNUqQqygXMQMYNij6DipnkVe-WDiLCcbNB04OAT-Ll8lFjp72bTd7Wf7g__h0OPvYMrIfUHz9bahTtatEA9cwp3LMUj6oGcRooNv6EXmyhW8-SkFa6jeZf1OdZAfa99YQ3zVe-qeaS72gLn6RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce141f49b.mp4?token=QhWwFWDwWBJ0_OQ3y1CcCPD29RR62WdSdcCwVP0vuHnX0CwwnXEGUiqss0w3XUI0xqfmXGXLemfyHA3_bq55GapRksi4Rmr3M9e2ekEtb_mikd1-C_OtyDHNxODzhtBC_2w6LT9mTAf941HEZ3o_2aVSjUU6vQG_yKnGsNB01bkb_KFMeCnTgewL1qLnO_6mEtGBb0uZOo32JgIZAaKEDBt7TI0ntEGCRe-m-lfSxa-mKk2IP-pJcbuFElJabRX2uFgfQiCpVrmKTI_m-uNr5t33SPn1SLESyN4QGYTT2Xm-3CHgqOrafc6iyyMU4On7Jgt0w1qn3ybCTIjX-RRL5zHM-Df-SBfcjfMzsowhtokbmnsGUa9bYfhJusk8hvviYzuGBnQvi2lFipayDKbd981cMqUjWwB0NOYwIqNLMmk1hpbulAKwb5JVkCXiznuURDXRlohcEOyqBUr__3vMMS2Lcct8m5wk1c2ypJ7tBE4LtcobpspgL-qbNsQvpYUK9qVMkSk4YxgsCFCMEvKWPgEM9nNUqQqygXMQMYNij6DipnkVe-WDiLCcbNB04OAT-Ll8lFjp72bTd7Wf7g__h0OPvYMrIfUHz9bahTtatEA9cwp3LMUj6oGcRooNv6EXmyhW8-SkFa6jeZf1OdZAfa99YQ3zVe-qeaS72gLn6RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین کم مونده بود اینو بلندش کنن ببرن ترکیه با سرآشپز معروف ترک‌ها ویدیو بگیره
‼️
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107624" target="_blank">📅 19:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWeeNWkkZJJmsETfUwhBicFZWiPFLa3QypyVhqJiyZ24A9ki61MkafXS_1U1UprSLqxQIH-LMYx5GOPbTxRG1NT2V94lusdDaDsb2Yqb5Cs0IMqgAh-zZckS5gITRv1Pm_6GX2Y-j1QCUJxcGcwQbVJd5wMhXXTRzw610OD11BdW4bJ2r_dRTBoaWwhUDifIA1EJnMh-eJrQ9-CF4RyFJhA8MBpAESXctsy7Fk0maRzBfAPcJGJPcAPnf8WvufkqFhBclUa0z3ZrFAe-xCKWgv5xL1nwRmvbqr9FOyUbU4L_RrGIMsDFJK24ZfX3owsxka59oRLvmjMw0fCVPAtp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپورت:
🔻
باشگاه بارسلونا تاکید کرده که یوفا فقط شکایت رئال مادرید را دریافت کرده. برخلاف آنچه در رسانه‌های مادرید مطرح می‌شود، یوفا اصلا از آغاز یک پرونده تحقیقاتی صحبت نکرده.
❌
یوفا همچنین تاکید کرده که پیش از صدور حکم از سوی دستگاه قضایی اسپانیا، اقدامی در این رابطه انجام نخواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107623" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a15cb946b.mp4?token=KZxrb-k4OCWiaORhgm6CPYGwrAdb35W6P5jDIUxqWIdf-wFdtRuFfx7FVGxL--PBSDMOy5_mVXL7wdePTzLoVmKciGjrpqa8LCqyBPGr3IgNQueDFBPdniAX2YWjBpO-ih5dIlw8lQG7pRgE1GVt7Vpb8NXhwSh9zJCxBiNfYTHzgEojAB8en-O1m7r4ZpRUfYqSWqhUx99n-JtzFcLEgloT7NeP0JhCc_j_PEKYRB2IohiWAYuhD_ayoe_0MwGJwg4yW_v5yA9jgbP6N_nTDBQKGmJZjS8YTpvUaD9Zj_MblrhrCLs1aCfXOARbIl5JcoilOchFHVQ0HkZG5zoAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a15cb946b.mp4?token=KZxrb-k4OCWiaORhgm6CPYGwrAdb35W6P5jDIUxqWIdf-wFdtRuFfx7FVGxL--PBSDMOy5_mVXL7wdePTzLoVmKciGjrpqa8LCqyBPGr3IgNQueDFBPdniAX2YWjBpO-ih5dIlw8lQG7pRgE1GVt7Vpb8NXhwSh9zJCxBiNfYTHzgEojAB8en-O1m7r4ZpRUfYqSWqhUx99n-JtzFcLEgloT7NeP0JhCc_j_PEKYRB2IohiWAYuhD_ayoe_0MwGJwg4yW_v5yA9jgbP6N_nTDBQKGmJZjS8YTpvUaD9Zj_MblrhrCLs1aCfXOARbIl5JcoilOchFHVQ0HkZG5zoAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری پشم‌ریزون حسن‌روشن پیشکسوت استقلال: فصل‌قبل که استقلال در کیش اردو زده بود، ساپینتو هرشب تو هتل دختر میاورد و وقتی تهران هم بودن داخل سعادت‌آباد بساط دختر بازی راه انداخته بود و هرشب با یه نفر می‌خوابید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107622" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107621" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107621" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av83p0wYFt_7Eem_Zpn6JVc2zx-YWB0cmIib27gJGJy8rxH17dZQ1aGn4X8SgPMPR6W7PUhBmaTM9_FhPb_B9462e-dxMljqbsgIqce_2DDx_CszSGBRFtSljgu-VQWueXJeanbKGUpz7jZSVIpwviQgMtrhoRBJCWHg8kAa4xBotwFv7WVG6rlqNUk_uHx0k1vGgSmvqRWNTi0xNLeSSRlMFyN-YNouG33iejFiwmpiSz3SvOidmcaBprv2h2IG6DQl0aX3PMb-lLD_1AUoZQ_x_f4u4eLDjkX29NcInmc2OmZTHJ9WnWc7ENFGHjnyv0ljBCNg6wYA_QNVpLoc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107620" target="_blank">📅 18:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107618">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
❌
🇪🇸
🇪🇸
فلورنتینو پرز به اعضای تیمش قول داده که در آخرین دوره ریاست خود باید تمامی جام‌های کسب شده بارسلونا در قرن بیست‌ویکم را پس بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107618" target="_blank">📅 18:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107617">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-9RYxPMJUPGnIXM1tekUtGwV9CgnoONHSaPz9rkcKAWmD_YWR3XCrLeNHaQtPL1d8NzjMfcB5MmgdLQLRc1d5EuSzES-BWtpMX-YbOxo00QT9Y3PluO_SXYs9MZLFom6Qe-Ivt6citExco02w4wfyGxzR5DPND0ktAdYfkiqRDvhbuhWOZK5JaUEBrRnj14aadyAeNEykbAIhEpnKqQTPwt1gM3P8Df88OlR-YvmiGabzIV1rCMUnK3e3uSyDYB46i0dkaGy2_oVhNn0vEvacSj0nKmCSRKVlFP7rz2BkU4tCG6FsoXRbbxdhwFbWSzQiz1qHTbJ8bzsvCeNNuN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!  محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107617" target="_blank">📅 18:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107616">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoNiz8r-BV1teeRHdm7FczX_m-n5rxeZOyBPN8kGDacagJGRxfVLKhaeQj2YEgvhjrb6FXnehVaDCzSSjU4c4Hi2ap6gnbSrRvkHMyJU81esN2OoKRVWZYrMb0BScIUjNAvgR3RhkvBId7RyqlfL6q3aL7f_YJXw8Psuncxxr1-bseM6KCGKjMmc2xpGyTGCATobi2gR8Tz6_MM9daEsIY38FiyIHwBAplTnbhL1aokIbp15CGDELcOXTQajmF3tQTInpBU60bT1Oisgfv03Pc2bqEJKZPpdoJGg6QwzIZLUVFzBTxXkF3-pXxEtyRuwabNToJaRDuqd3j3nX_mUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🇪🇸
آاس: رئال‌مادرید بیش از ۵۰ هزار صفحه مدرک علیه بارسلونا در پرونده نگریرا به یوفا ارائه داده که برای حد فاصل سال‌های ۲۰۰۱ تا ۲۰۱۸ است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107616" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107615">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoqxKrYZLbsUvv46DX_cgFvfX5mxVQ_xPeHAPuZuumf8BvINktWgKhY_zUujhmJhUh1U5w3fpVEfj-IZRmSJy9Gqkeuo9JsGtpMO4hos3P1OdYUWphwJtpjnnOKUcaXzFr4dm9AwrqxFJBbPR7B3C2y_4SGavuzfQnGw2iTvy-CUjWt2TJkbFIIxjts2Ldw6nCIR3LYPUJxMOSKd1mXMiFb_7KgsNLkEE7mKqeu78-0J0qLtBdWMgBozYgEn-w8cH-fTUVctjHbTHzvgWNOLgHSuXNb8uQi1NHPHSO4p0N8Md7q5iZSuH40qRiZevgAxkUgxHj_YO93qdkZd2akwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
یوفا اعلام کرد که حجم قابل‌توجهی از اسناد مربوط به پرونده نگریرا را از باشگاه رئال مادرید دریافت کرده.
🔻
این اسناد در اختیار بازرسان اخلاق و انضباطی یوفا قرار گرفته و در چارچوب بررسی‌های جاری پرونده مورد ارزیابی قرار خواهند گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107615" target="_blank">📅 18:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107614">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4dK4ttj6WfsJJCCk9RuOYAPoMbsdoyWqBTyNtBFJoQbjZNhrzO6vQjAIDuj-xY8an16b37ZySwwy-LK43d3h1H2DIVCjRP8vkW7JHeamYGsdw6d_H5vJ3rY2j2smBlDSy4P6f_-53ydBqTpZv79w2efiNlFZyJyILKRHbi-UNTUxwYrqMH8djRg83slAAiReVahinSCkFlTeYMZR-Izf0fOvxFuVFyj-9I4xVMRENDEDmOrLRw0Ly2hykBqL6DUxpKeaVOMAISlrHqmSX1pGtIwWJS_ZYeMjm6pCAOHGdRtgb2kClxiaY2JmLszx35YOXwzlSuNOHNz9rqBHWyKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
یوفا اعلام کرد که حجم قابل‌توجهی از اسناد مربوط به پرونده نگریرا را از باشگاه رئال مادرید دریافت کرده.
🔻
این اسناد در اختیار بازرسان اخلاق و انضباطی یوفا قرار گرفته و در چارچوب بررسی‌های جاری پرونده مورد ارزیابی قرار خواهند گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107614" target="_blank">📅 18:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107613">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015e854338.mp4?token=vrYxZy7emeD9aS3KwSY7yWMTh4xXtec3c0oDRGhAqmqoUhxrMBRf8ivBSBN6fZ6x-5jVHRcXH5uwOz-br8qegGxvBwNoqQjbk4WTW9NF3hUdLr7pBmlyIkcrxleBkbsTPl2BhNXkYizh9SSWFlNlGXFJayMk16wODo9FVIeJ1gZl0DRokv922UkZl8VbmueyM2x0An1O5a56HH7u44KzAWaxJtN-ZAY9oe6vXZvUhyijhypNclSUWKCRatrQZ4rRVxWjHsgW6-JAECDiiWESYLpfBrUAuBlz99KcdcDePMyv1XPMkE6uNq9-V2F9XGouclEXjd_wyzVXbcU883raRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015e854338.mp4?token=vrYxZy7emeD9aS3KwSY7yWMTh4xXtec3c0oDRGhAqmqoUhxrMBRf8ivBSBN6fZ6x-5jVHRcXH5uwOz-br8qegGxvBwNoqQjbk4WTW9NF3hUdLr7pBmlyIkcrxleBkbsTPl2BhNXkYizh9SSWFlNlGXFJayMk16wODo9FVIeJ1gZl0DRokv922UkZl8VbmueyM2x0An1O5a56HH7u44KzAWaxJtN-ZAY9oe6vXZvUhyijhypNclSUWKCRatrQZ4rRVxWjHsgW6-JAECDiiWESYLpfBrUAuBlz99KcdcDePMyv1XPMkE6uNq9-V2F9XGouclEXjd_wyzVXbcU883raRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اصطلاحات مثلا تخصصی الهویی که باعث بگا رفتن تیم‌ملی و قلعه‌نویی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107613" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2985c6ba3.mp4?token=n4RXVyzEIlEhPUws2B582YUUa0BWkagWNuXqw3HUEJQwCgBzFVCqGvOiSUQhfnXuC8tAVz-XUh2tO1d4dvQcxks63oco-BUumOYxhTDbGJTvRJbWiffwTvn23Z0rkjKn__T7LjxZp_A4EbUT7j8JF_wd9c0XlcUnzHaVp8Id9ckcsy5ag_7Rd3KRDQcdvKjcvJPJprwlexrJanSnm5EqKEMTmSeQDNVJ8ChaeiQaYMWOsNAHVuGf8gJ57KRqnyfBKA37BM_DTDDFXmqPODuA2z7zIzHMp5L-wcKLX5xuRQxocSD5gqQhBVD6DghEeH5ofrjGHOiQZAWo-zxV3GCfQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2985c6ba3.mp4?token=n4RXVyzEIlEhPUws2B582YUUa0BWkagWNuXqw3HUEJQwCgBzFVCqGvOiSUQhfnXuC8tAVz-XUh2tO1d4dvQcxks63oco-BUumOYxhTDbGJTvRJbWiffwTvn23Z0rkjKn__T7LjxZp_A4EbUT7j8JF_wd9c0XlcUnzHaVp8Id9ckcsy5ag_7Rd3KRDQcdvKjcvJPJprwlexrJanSnm5EqKEMTmSeQDNVJ8ChaeiQaYMWOsNAHVuGf8gJ57KRqnyfBKA37BM_DTDDFXmqPODuA2z7zIzHMp5L-wcKLX5xuRQxocSD5gqQhBVD6DghEeH5ofrjGHOiQZAWo-zxV3GCfQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🥈
اولین تصویر از رضا علیپور پس از کسب مدال نقره بازی های آسیایی: پارتی من خداست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107612" target="_blank">📅 17:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e174f30bb3.mp4?token=jXiaChARfiKGIFwrotz1ho8LIwDvCxQUiDBidNHcBznH6JcV5pKVBukX0Vwkcf1TCFBQujh6YhGT3THiFSkM_9PUJwr3YC60uCdq__91z5i7l4WE_tsdbmCponCQAP2tGOPkMEo1bn4wgFZX8WvVxL5_veCdXn-ArumoIxH0o1lk9dMODVWiEk83wzQPjfMDFkteG8qyESaJIkqiviBjTnZcHTivu7Puoqh5t00T-X97UQtEjc1Q9C1-GyCjN2HASN92IxYQKmlowN8LEJ9BMlAmrVU-bxgHoUXuZGHP1K7vxui3n2JX2Gwtqpcypaw9mkUYbI5KE5NFS0pOwHnjZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e174f30bb3.mp4?token=jXiaChARfiKGIFwrotz1ho8LIwDvCxQUiDBidNHcBznH6JcV5pKVBukX0Vwkcf1TCFBQujh6YhGT3THiFSkM_9PUJwr3YC60uCdq__91z5i7l4WE_tsdbmCponCQAP2tGOPkMEo1bn4wgFZX8WvVxL5_veCdXn-ArumoIxH0o1lk9dMODVWiEk83wzQPjfMDFkteG8qyESaJIkqiviBjTnZcHTivu7Puoqh5t00T-X97UQtEjc1Q9C1-GyCjN2HASN92IxYQKmlowN8LEJ9BMlAmrVU-bxgHoUXuZGHP1K7vxui3n2JX2Gwtqpcypaw9mkUYbI5KE5NFS0pOwHnjZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیو جدید لامین‌یامال و زیدش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107611" target="_blank">📅 17:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خلاصه مقاله جاناتان لیو‌ در گاردین در مورد ابعاد ژئوپولیتیک پرونده منچسترسیتی
🔻
برشی از متن: شما به جای ابوظبی(مالک‌ سیتی) و عربستان سعودی(مالک نیوکاسل)، به راحتی می‌توانید جف بزوس، عضوی از کنسرسیومی که اکنون تقریباً ۴۰٪ از سهام باشگاه فوتبال لیورپول را در اختیار دارد یا متا یا ایلان ماسک یا بنیامین نتانیاهو یا دونالد ترامپ را بگذارید:
یک طبقه کامل از مردانی که هیچ مرجعی فراتر از خودشان را نمی‌شناسند، کسانی که به سیاست و تجارت و ورزش و فرهنگ همیشه به یک شکل نگاه می کنند: بازی‌ است که رقیب باید به هر وسیله ممکن به زانو درآید.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107610" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=vK2zA6ugdvvTXWWaTDjdxKMYI4bRX-YpKgDLAUFiVxfN0wktaeC3WUPO7JWLPna1DHrGdZhyf6G91MYgWZoEp6GMbGjVrA3qZtjFXKtf4vWG_P9qntRuU4myU49R_60BhB2aYXjj5PvcanWe8R61MqkafKavzSrO0sgHTFurcb6AX1poMnYha6do2RHVsIT6Gvi5n4gJ0kXuAanEzX6xiStUbmkmxhTbniQvFJ8gt50ohJz8Oc-LZJgEvNlFGlNrIhK87yM28dq_CUssnimire_4WJXY8FNIHBmNwixd_6gsqtU16s0NfFCie0gnTDScf-qNfH7Fvu9M0yUpWZuWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=vK2zA6ugdvvTXWWaTDjdxKMYI4bRX-YpKgDLAUFiVxfN0wktaeC3WUPO7JWLPna1DHrGdZhyf6G91MYgWZoEp6GMbGjVrA3qZtjFXKtf4vWG_P9qntRuU4myU49R_60BhB2aYXjj5PvcanWe8R61MqkafKavzSrO0sgHTFurcb6AX1poMnYha6do2RHVsIT6Gvi5n4gJ0kXuAanEzX6xiStUbmkmxhTbniQvFJ8gt50ohJz8Oc-LZJgEvNlFGlNrIhK87yM28dq_CUssnimire_4WJXY8FNIHBmNwixd_6gsqtU16s0NfFCie0gnTDScf-qNfH7Fvu9M0yUpWZuWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
دور دور بیژن‌مرتضوی و زنش در تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107609" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=BFikfraURBsjpEA2JKBNT-40GpfmNehK8EynMmW5MtpvFLYDEB3pw7tVEUaXObh70lBk0yvn8goNwAYzcq77jfx8HA7x4whOp7l8dW_j9RODMVA2p_6xLg3v6xBLdhITfQ9Qe-I7xujhiF7HqovmCR3RkPUptjBqMto4OTTLUQLKLqFWrZzlnMUB4tWObdet3OHsfqf7cOZcsqTFl1uTv1aK6zVnCqT_1AV0bLT-naY4Fqg6AHGBQXFDwwwaaJG2iKp-KuCm5snblP_C8tpISBuOYmw-r2GTN13MKSHtFdbcJOD3A9fpY509cW5GlBgh8iB9MxFjgpbNBLO6I7CSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=BFikfraURBsjpEA2JKBNT-40GpfmNehK8EynMmW5MtpvFLYDEB3pw7tVEUaXObh70lBk0yvn8goNwAYzcq77jfx8HA7x4whOp7l8dW_j9RODMVA2p_6xLg3v6xBLdhITfQ9Qe-I7xujhiF7HqovmCR3RkPUptjBqMto4OTTLUQLKLqFWrZzlnMUB4tWObdet3OHsfqf7cOZcsqTFl1uTv1aK6zVnCqT_1AV0bLT-naY4Fqg6AHGBQXFDwwwaaJG2iKp-KuCm5snblP_C8tpISBuOYmw-r2GTN13MKSHtFdbcJOD3A9fpY509cW5GlBgh8iB9MxFjgpbNBLO6I7CSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
حنیف عمران‌زاده مدافع سابق استقلال:
من توی دربی که چهارتا خوردیم هم بودم.
آرش رو گذاشتن وینگر که فکر نمی‌کنم اصلا اون‌جا بازی کرده بود. حالا دلیلشون چی بود؟ این‌که رامین رضاییان هی نفوذ می‌کنه از آرش بترسه و جلوی نفوذ رامین رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107608" target="_blank">📅 16:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e980239cb3.mp4?token=Keau7pal3vjQAJQMXQnTGGh7WhKLqwQnLqvVtHTFxZN1PQfg5ZCIs55gVGMhK0-BoNT6vDyfhuMq3u7-iOLFcIVCLCiw8iemKtBZxV2ZKzQDTbKsS8WxIoaZJyOc-RJz0XyF0BEtMP2On9al8dvdZScHHt0bdyKOwujlwJQZkNVlfuRkm9zerCBMraX-f8kJ9s3qFug3vBMV9be-qssXQFHSDUxbBwmul7dWs2hCzp7Tz_VHRDyPun6eiWWdI27i0AzBrelKj_4hVZc5jqTdBj36U5blN5R43Ru_9TnPIB0NDkQGzkFw9gfqDH53BlXK08rGaEONbcZxRzEJNflHsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e980239cb3.mp4?token=Keau7pal3vjQAJQMXQnTGGh7WhKLqwQnLqvVtHTFxZN1PQfg5ZCIs55gVGMhK0-BoNT6vDyfhuMq3u7-iOLFcIVCLCiw8iemKtBZxV2ZKzQDTbKsS8WxIoaZJyOc-RJz0XyF0BEtMP2On9al8dvdZScHHt0bdyKOwujlwJQZkNVlfuRkm9zerCBMraX-f8kJ9s3qFug3vBMV9be-qssXQFHSDUxbBwmul7dWs2hCzp7Tz_VHRDyPun6eiWWdI27i0AzBrelKj_4hVZc5jqTdBj36U5blN5R43Ru_9TnPIB0NDkQGzkFw9gfqDH53BlXK08rGaEONbcZxRzEJNflHsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
صحبت‌های شنیدنی و جالب احمدزاده درباره اسطوره ملوان مرحوم سیروس قایقران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107607" target="_blank">📅 15:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgQJ4x-74axz7jt_zyZLFbrzgfp8vMPiaD7ePMnXcmhZmfd0YtI1lAm6sYsHNoZdfLQ30zt5v7xpxqc030bWhVldoYrB_Nf-JCAvw4eNIn6UEVmPxVVVHq1lcJeNdbzO-vuC93AGG_BGV08mW1tcxnM1zM99oLPt7eWDsXoer-fe2gAgmX_7pqIn35rBLYlxz9WlBctyF2pwaeKjtryjA829kY4Cv9qba5iRRP_jjGDNe2Z1zBbiIsDhd4CC0a42y7PJDtUqwoAesdsFx-EtpL6eoTNbRzl4KeDHFbsMU_sft7cKDAP9oYX_zLFhrJOvvsItpCDu_okudcMQqLDPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس دیاز: کادرفنی رئال‌مادرید تصمیم گرفته که کیلیان امباپه مقابل ویارئال به میدان نره تا با آمادگی کامل به استقبال الکلاسیکو بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107606" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5204393f.mp4?token=uSCDfE8b-YY8VgU-NsZj9XeBBp2gZ2rwzQd4rlXu0oMiGY1SLzX_UB1uz4x4JqoH8evilleFGf0wHHxNP5FZnHmviNc2KKUBmbSdfAeMZLPgdFByueF6LozCJFOl4WaVw_o_7pqD5tGBO61nvBP6PbF2GF1Ez_A6TM2S8FUpttHeefpvXRuz8INBYLeAlQzhiJc6oxVRTyyR-cCmOkf4SPGnl_HqEZk-e2RFHbMmLsA_gzFNNfkjhIgg9sIDPxNoR62EKe22OSYN5C7k6Z_WCtGWrpQsu6ccpis9zIKIlgxXCrvbij59duer9-tzVHiN8dw6OKlJYZSAeUWhCFH5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5204393f.mp4?token=uSCDfE8b-YY8VgU-NsZj9XeBBp2gZ2rwzQd4rlXu0oMiGY1SLzX_UB1uz4x4JqoH8evilleFGf0wHHxNP5FZnHmviNc2KKUBmbSdfAeMZLPgdFByueF6LozCJFOl4WaVw_o_7pqD5tGBO61nvBP6PbF2GF1Ez_A6TM2S8FUpttHeefpvXRuz8INBYLeAlQzhiJc6oxVRTyyR-cCmOkf4SPGnl_HqEZk-e2RFHbMmLsA_gzFNNfkjhIgg9sIDPxNoR62EKe22OSYN5C7k6Z_WCtGWrpQsu6ccpis9zIKIlgxXCrvbij59duer9-tzVHiN8dw6OKlJYZSAeUWhCFH5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
استقبال خانواده بیژن مرتضوی از بازگشت این نوازنده در ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107605" target="_blank">📅 15:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297bb4ba61.mp4?token=OIDfxIJz4CMLEncVuMZE1e9b0UFHrHMDjo9B9KI0xXlt4gYLMXUUeipNrtQu0-Da7q2Cwyyoi8DvfYaHyVNPGecA3I1fMq-QnOC2e0E7k0cllwf_qPlUQ4UtG__SXPbf9wZXnvvXlx175b3fvFiLb_Sr-JYSIRL6FXkNLWpmbR7ODEpSgtk6hYD8JJ309JQbdHIFsuEa9Mk9jMXCIHQwFQg13lBck8Z9b96WYX8ciCVSTsActRwogG3uiw3gY2GvcuzYyftP6iNPprb2uz_bZRZI2MzzhCGJAPOwViYZrw6e7ds3EHWP4gNnXTenD1Q2WK4NtTPE06PK3u6tMn2FPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297bb4ba61.mp4?token=OIDfxIJz4CMLEncVuMZE1e9b0UFHrHMDjo9B9KI0xXlt4gYLMXUUeipNrtQu0-Da7q2Cwyyoi8DvfYaHyVNPGecA3I1fMq-QnOC2e0E7k0cllwf_qPlUQ4UtG__SXPbf9wZXnvvXlx175b3fvFiLb_Sr-JYSIRL6FXkNLWpmbR7ODEpSgtk6hYD8JJ309JQbdHIFsuEa9Mk9jMXCIHQwFQg13lBck8Z9b96WYX8ciCVSTsActRwogG3uiw3gY2GvcuzYyftP6iNPprb2uz_bZRZI2MzzhCGJAPOwViYZrw6e7ds3EHWP4gNnXTenD1Q2WK4NtTPE06PK3u6tMn2FPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
✔️
🎙
مهم‌نیست در چه‌تیمی فوتبال بازی میکنی؛ مهم اون انسانیت هست که یاسر‌آسانی به خوبی در ایران به نمایش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107604" target="_blank">📅 14:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc7d01e79.mp4?token=L502I4FEhpggEYOPU14Dvp4vC3ySoIkCnxAxDTvZaCcMNIdkG849jPKBdU1Q867wfrBm7Y4ExXVNDBjXVbg6l39i2PIpexfIIkAW_uufbIMIOi_tcjBjTywN-2Z9dN3gSVRz-co9x-hFYu5iFwCLeP7IGYwQrK8q5_9RB28vulWnt6PH-gcB-0swuXKX1rHtS2P5kL_cIZFJp6ZVCFSs4In6PJr3Ohwdr33fvST0vVBS6Lu0RCUZyYt6b_D-t_ct8xT2EX1QSmia2VtLfvqvTw22ZSrO1elgCPwmYTxWH7GFk2CHvqvT5R4mVGsqgqQt6XiBiafAOqH082RqUytecg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc7d01e79.mp4?token=L502I4FEhpggEYOPU14Dvp4vC3ySoIkCnxAxDTvZaCcMNIdkG849jPKBdU1Q867wfrBm7Y4ExXVNDBjXVbg6l39i2PIpexfIIkAW_uufbIMIOi_tcjBjTywN-2Z9dN3gSVRz-co9x-hFYu5iFwCLeP7IGYwQrK8q5_9RB28vulWnt6PH-gcB-0swuXKX1rHtS2P5kL_cIZFJp6ZVCFSs4In6PJr3Ohwdr33fvST0vVBS6Lu0RCUZyYt6b_D-t_ct8xT2EX1QSmia2VtLfvqvTw22ZSrO1elgCPwmYTxWH7GFk2CHvqvT5R4mVGsqgqQt6XiBiafAOqH082RqUytecg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🇵🇹
‼️
ژسوس درباره ماجرای رونالدو گفت: هیچ بازیکنی، حتی کریستیانو رونالدو، نمی‌تواند ایده‌ها و تصمیمات من به‌عنوان سرمربی را تعیین کند. نه او و نه هیچ فرد دیگری.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107603" target="_blank">📅 14:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmwbYfB-T0599V7RG6fzFenIPBsvqFln0tF-gf_Xo433luiN_b2nGEpiDYUNgJ8gmlZFdImGw-E7wMLMFjPEjEJo0h35ut6IREw6fTdBG1hrep9H7vzwlnaGbu775A6k-lWjPi7sVr2wDKdLsgn1J2qgZiGy626nP_nj4r2LjNVfNRIn3FvHyIM0lRKzTtrmes4COjtovBzcrdVbHvtqm0WM-XicbL1jmq28gcCLRONnIfguT6A743tW8hfO4mD8q6o5SxP6QKgeStsizUDijfnI67vdU3lljZQv5ml4d69X1tM_6_j9Ly7KPkw-ps7qgqfHa2PtUmgqJuURoMMMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
‼️
فکت
:
هر ریال ایران حدود ۰.۰۰۰۰۰۰۳۹ دلار ارزش داره، در حالی که قیمت هر واحد همستر کامبت حدود ۰.۰۰۰۱۷۱۹ دلاره
یعنی ارزش یک همستر کامبت تقریباً ۴۴۰ برابر یک ریاله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107602" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df216dbd92.mp4?token=iMugdIkRkQLic4x0zWGZgNtL_LJrxyaFuONdVWTtsljnBgGWtZlu-VTd7kFe8iL9A_EPS6Wi30usbnkxddIk7zVgNIKWAv-DxiLMxhNz6ZqAsFn0iXsqzaeKhNEsQfa4IowyCvwFSdZvZPenSbNVEZtmRK-fgxIz07FqvloPj5poeA4Cp_-Er1ruCFcbqRMuwUbZ3nL6OTfCrV2KiSaxy5a_s6FL5iRLIdQKI_N4fPoH79UkJ25H0qQR1EoIX5mTwUrxhti4pxGtheiQLRd9I9Z0x8_TsGCGKFUmwDxSp2ponDB3LFIodvcVACT2QTNG-4ah6u_EaUIUzpsGY9BF1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df216dbd92.mp4?token=iMugdIkRkQLic4x0zWGZgNtL_LJrxyaFuONdVWTtsljnBgGWtZlu-VTd7kFe8iL9A_EPS6Wi30usbnkxddIk7zVgNIKWAv-DxiLMxhNz6ZqAsFn0iXsqzaeKhNEsQfa4IowyCvwFSdZvZPenSbNVEZtmRK-fgxIz07FqvloPj5poeA4Cp_-Er1ruCFcbqRMuwUbZ3nL6OTfCrV2KiSaxy5a_s6FL5iRLIdQKI_N4fPoH79UkJ25H0qQR1EoIX5mTwUrxhti4pxGtheiQLRd9I9Z0x8_TsGCGKFUmwDxSp2ponDB3LFIodvcVACT2QTNG-4ah6u_EaUIUzpsGY9BF1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بعد نتایج درخشان قلعه‌نویی بد نیست از این مصاحبه طنز ساکت‌الهامی یه یادی کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107601" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsX-qHO4fyl4tPqg5c2UwGMowJWGDsObGskoFUcqX1n9bomRD5Li2uWfCzVKYqV7oUwjBmTNfD_NCytsRLH9eJX11I3M1XqpVlkayP_Eqa3IAP_i5cJSt3YlowhxSBSVxM_cvbatR18OBAT8W9-ckIN0f8CLp05KVVwPv8HEuDXUdZX2y_dsJ96ZBa8m6qsrJhthb_OGVMMnPsICO2ZsMayzduC7KO6TrNAcLyp6RhGA9Z_uQ1pjK8vm_GKZsXSEXlDsv1Oa6N5gVABO1Jl7ZQ_QfygDYQH0_zOS_-RdhQ2pPfnw0jsBrM5aCEa5eF0T1h5AeIOOfUFeSVHQCs8ErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇵🇹
⚽️
ادو آگیری، نزدیک کریستیانو:
🔻
«ژسوس در جلسه خصوصی بابت توهین (گرم کردن ۳۰ دقیقه‌ای و عدم استفاده) از کریستیانو عذرخواهی و وعده عذرخواهی علنی داد. اما ژسوس در کنفرانس مطبوعاتی دروغ گفت و وعده‌اش را نقض کرد؛ این خیانت باعث خشم شدید کریستیانو شد.»
⚽️
…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107600" target="_blank">📅 13:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972dc1e1fc.mp4?token=qWmpTvoyQxi1dtV2gu1QxC9u-ZeTvzTIzP1laWCWFPr4drQoT4814u_q592U1IkfnGhVHgCX45KV9Z5naK7wHOhsxAtjuLVR1fLwaGdI2UwN0f9cVMAlDFr5n0ntPdX7dAGMFkidSlOU9kPI1w0QYbFco-bjLcLEMwRDRJYbXwEB4YR6MxVNqgdrFtp4IiyUBSIc4ACNbJ78dlhWAL_X4DVByShJTVnfSSPm33cHpyjfatqe2ZrKTzoVnEwtxN_jEpaHqciIXoXeg3tTfHMIk054Zf8h3Bq98MFY2X74zGxZnnnAetkPxLirAywBu_YpsdwNcNErjI3NDQtVKwEF9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972dc1e1fc.mp4?token=qWmpTvoyQxi1dtV2gu1QxC9u-ZeTvzTIzP1laWCWFPr4drQoT4814u_q592U1IkfnGhVHgCX45KV9Z5naK7wHOhsxAtjuLVR1fLwaGdI2UwN0f9cVMAlDFr5n0ntPdX7dAGMFkidSlOU9kPI1w0QYbFco-bjLcLEMwRDRJYbXwEB4YR6MxVNqgdrFtp4IiyUBSIc4ACNbJ78dlhWAL_X4DVByShJTVnfSSPm33cHpyjfatqe2ZrKTzoVnEwtxN_jEpaHqciIXoXeg3tTfHMIk054Zf8h3Bq98MFY2X74zGxZnnnAetkPxLirAywBu_YpsdwNcNErjI3NDQtVKwEF9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عدم پاسخگویی مدیر اجرایی منچسترسیتی به اتهامات وارد شده در پرونده فساد مالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107599" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL1K6QR2fLEM5HN49VmwNhF1jPEzevn0pDQL0SfqD2vU5dRONaKONFvP3UwCE6vSqMuEW2tN34nXbgeu3HrgHlR-GOgvx2t_-cQ-6WbMrCUI1juAo4bhzg0QkD0A1HoDeiW2ak_HgNYcpzCHMsQq6fct5IcEfnpZa6LPaYg969dcBqeE6XN3FOlvbtEr9Hrfv6NBPWj3CWKe6TeWsX-GQEXaL93u6zgIH0PBrcVO-dlhlUyaErlOTp6CHvdM0M9hu39JaYz5IzAj3niciuXqVDuaDe6G2ss5Gs-3zrmDl5I7rkEzXJ23R851q-6gGpQ2zLc0001qhiUJtZVunH1ZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج اخیر قلعه‌نویی با حقوق ۱۵ میلیارد تومانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107598" target="_blank">📅 13:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQdKPJ0mFHhJ_ct8z68dWmh2Gwqxkgr-s3P4U1cDYrV75nXAZSscriFD5n4K9JYVgeQNVpJDxGAJ35-GMisaS-fgNxUynXoLNlmiYJJKkUXqLXertx1PeovTMosbVyomsmrzt2TYVnM1mHXDYTmnxcl7rVx8VmxDRU5VLw6JfMQual966nuH7cxZrJCUevDsBsH4zyjNcnqF_BmBeCnDJtArHMvoAVp93DBTkDKokvdpMqB7fHdGi4N2A5n2ISCp1J8XHYT_JqPAEXrvvRMnM-nQP0hdKX4590vDUpYcK2UNyzJVvCkHFmjge_2Q3OVyU4sSv9LXgLDMbdX8fdIP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
#فوری
؛ رافائل لیائو وارث شماره 7 تیم‌ملی پرتغال پس از کریس‌رونالدو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107597" target="_blank">📅 12:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f7d3031e.mp4?token=qWDb6fNuIMhVeMoeY7Avfgpb9PleTJUezt0rg3izeSOCMxHa9udanNZKpNRsQlb4rWxKdXIX8Ah6EoRFifBXEaOzX_Mw0eMg4yx42Y6eOMpSST4wS0nSkOSfM_5iLnPfP-TG910brElLmxaRT47QaHFTLuaesW844MU02pJwBMDBtKJZZyhJRjyXmCspYea-58mX_herRtw5JEhD8XLPFe7p8u3UuLVxVVrzINcODQy071RRyrCMqZ6UNQa7M5miA_01ws3NspgP8IBDUMpW3Mj5I9E1xEWKXlUFAm_hrwSbl6mBdT9EJzQupObjbF1MUGpOPFJ8dUkOcJ7ZlnKzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f7d3031e.mp4?token=qWDb6fNuIMhVeMoeY7Avfgpb9PleTJUezt0rg3izeSOCMxHa9udanNZKpNRsQlb4rWxKdXIX8Ah6EoRFifBXEaOzX_Mw0eMg4yx42Y6eOMpSST4wS0nSkOSfM_5iLnPfP-TG910brElLmxaRT47QaHFTLuaesW844MU02pJwBMDBtKJZZyhJRjyXmCspYea-58mX_herRtw5JEhD8XLPFe7p8u3UuLVxVVrzINcODQy071RRyrCMqZ6UNQa7M5miA_01ws3NspgP8IBDUMpW3Mj5I9E1xEWKXlUFAm_hrwSbl6mBdT9EJzQupObjbF1MUGpOPFJ8dUkOcJ7ZlnKzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند حسن روشن پیشکسوت استقلال به امیر قلعه‌نویی: رئیس مافیا سرمربی تیم ملی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107596" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
