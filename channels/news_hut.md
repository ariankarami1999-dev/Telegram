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
<img src="https://cdn4.telesco.pe/file/X8NG3rU_VPDH4CQ8f8kwC71K2QnnyQN67trcyFtZwgo_RqpdHEOn9hjksb_PHK0m89suYa3t0TN9O585AMzNXfMAHoAiApcTlkWlRd8zUn8Osi6VJO0Ak8W8HwsGcxLsJP6_NjTe9mQzFmqdrPFw9QiRniDYEEtlPSN-hW08tSpB8HwNT0t95WbskzwyYs70iyuEBhzs8OuMb-692oq1eyAwjcsTVRwx8aT5s92qxA_1d4eRQUFSHP0uPy95vhrNYIU9LWYQFYKQ0qRn1m44RWmuatPrv8eDD3PiHHkOVY6DeFYy5WhXoNrtg1jpgDzNHktzfixmVJU9yx1kwM2Q_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 229K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBI0WcjaE_syMQSrkLGGORbIwldp7Kj58J4qMh3VZRSfoU6RQ8Vqr1q4XEqAig_xfeT_riXzXmEjMcnSm-WR8FlHN6yfeVO8Xq3-uhb7HYP8g6igo4hBHhSWShj5wb-tOU9sW_mEd1g12_7DDKUIQfoYWfRyZ5sPnP2xYN-seTl-pvonpNObcuV1gMEV2CNMST2EaX32gtky3FKfygCtHYJTZZJ814bvFAw3GrWXgYF8THBzVhXFD79wUm-lFeEn9ILm2FPVt5IkQ_jOFJLDKuA29sCwJoJncZOcHQkYgeoXAuAa7PDpjhup7xZwJyLA4af-DCYYDGVyw4JJxwDmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCB05YnHxNSzcIynJW2Od0o5FOhqEQ_n14IQ78JV3cWcvBakTopEpY64MKBb_qMEOWRFaMmCNTc3QgIvo-fJlSOXsgindcU05pJkx9yOaxT4Bfv93B_c9CneehY23UjLVVrOpfapyZJ_rUPiXEj3er31RgVnNLvzCU1nMa7Hg3BvkUW7iIsgvQp2N55PeczO7_rYynSqdKWvY65BkcBEmcWQ-ZL1SPO-ZKosqx5BF_HDBLpoSLKazYEo4CTYGS-jrMW4ZulHbramJV0tS7v2nDcuJpkhTtiTxApU-BsUXCv19aG_DvtUa7IirfPv14vhQYyORyoVglTFEUdcEYR_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در ۲۸ بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در ۷ بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپانیا  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر عراق  ۱.۸ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۲.۵ - ضریب : ۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fapL9i97oPPcxuF7b_ULQTDmnEz1ZTYDj1u6USZri8Kj6a5MkgpCKzNqP6klmYm_HtZOzEzSx9XlTC4S1m3Q7IHVAistgRXiJJkdI1Z4JsKueg8-O3G9gnFbkyA18WzvGIM16tOkDWUOGDE4JGafR-BRw35-GOxFsc895-VIaji00jB1-z9i8zL5wp6uiAgkWXyD5NDr0KkeTo60_DMeaWGot3sW3KtALBBTLWBZM1O_874nkEyuV7xY84K323lHCfpleSQS4Wfj40dW-crV6ItyrrY2VfAVNT2bP9mrYovhVervww5HVpD9sMvLB7RkUIX5S_DdFj2vmEDDd6iJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB76IeXPa1lGkgHpHQxLsJB2QTSRHyEqj5_3XW33SeHClwtHQetTF9Y8rLEw30udtq_7DL1AxjqIKSLoTjTZYnbX80FaWbqA9xO6uIAEKvhqD-KFTdufnOv_OVwN88c1UrvH02ajbIbyIVJkfrSRpSoQw612xKOqdCUtd6tdfkaAubYhJUy7AsARQA29FLUJ0ObTN37ZGVBWTBjG_a6gz7AdZ7Gc9YwTymZBXc3yzx-LvyzqZty4Yj_xbWc-baijckmT-xJ5ZuGcno6CHJC6ThCHG2d50KWD4h79KCBBAUpsef56-A0cf-fZrRnZPe-im6Zn_kJngMU_Eph2xds_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Q6AK0kulPOVm02YDbclbXVg7jrgyiaD0WvURwnVhJk4Apj4P7aOFsQm4f6dE1bBVKksyXeQkb0ZWVo6Nhjd6iQvR_NJ7MJUq8StweYEbDvdiuvKZKa9pulrZFBMXVHx3vlrLYYktj0ajgisvGNld960qlrRFDVg0llqsOfYWFDI7jFcELy0UEUxN_LkWBhama6Z3VVSRlMrEMYdY51Y6_s_kPYTocG-2NflZCPwZC3RqefLWHtVaCvZjz96oAU6kO4mp_uGRoqkuCedRT7xZJeXp1sYWuTvit6_evFJH-7vaE1Mt-VUbTh-mflXc5epY7Tg81UsOnMWtzyVdaB_9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Q6AK0kulPOVm02YDbclbXVg7jrgyiaD0WvURwnVhJk4Apj4P7aOFsQm4f6dE1bBVKksyXeQkb0ZWVo6Nhjd6iQvR_NJ7MJUq8StweYEbDvdiuvKZKa9pulrZFBMXVHx3vlrLYYktj0ajgisvGNld960qlrRFDVg0llqsOfYWFDI7jFcELy0UEUxN_LkWBhama6Z3VVSRlMrEMYdY51Y6_s_kPYTocG-2NflZCPwZC3RqefLWHtVaCvZjz96oAU6kO4mp_uGRoqkuCedRT7xZJeXp1sYWuTvit6_evFJH-7vaE1Mt-VUbTh-mflXc5epY7Tg81UsOnMWtzyVdaB_9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU5vf017DH5K0K2rJ4sAfabkSz00gHeSs81upJzf0LAoqkefl0J6Ve2bMrFo1PmTST7Kzfk73sNLK7gmwc_OiEVv4CpsBwDnqkjsQ-viy4dio6_nZmOriU4CjxdE_PAegMaNygurlwZNrmR6ccxmGtFRKDHF_2cz8x7iB65gPGpbBxp5m9pG1QYfXKcap104alvbqICVECC9m1T6AOfBnvdCgnruCyL7FffACUk3eklJUI5EbZ7zyJXFlrRAVgLhJbddv5QSyT_q8L7LpbEcN5DmWdASKNxzyB8jj841qJ21YT-WVFt3FzDidTHuHukucIvXpXQpkKGzNBeDXi1XnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcVyN21k_wYF1g4C5KypUkxjqkC6ZfeF-_kKOTWqsueoiCjvfW0vJOZxaGu4iV0KHV40dGwS6Kjp2fQXnSUfRTUBYf-gU78KpypI7BH04Uo_9tlWoOb6yubEC1eVukkLD_BCG0Wa7Vbvh38sP8eBZNslkSrnoODhOK2FNn1PNpHvwqjO-AzjN6EZEZ6TVtHuIQMwrru8zJD5B3n7X7KuoPdXESQMV5sPPLKIJ69UJSapvqYf9tJw4L7hJwW2MQ0qQAYBHE3XNLq_Kp7g3cSwtUstj-MargDQ8Hh5RQZHNMNVfi-RbliF1Zi6g7UKf0OS-KeGzkxVA6JznU_77vNM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf8EEJgL-c6J3PSUgX5B6Bex75Sy2z9Moy3KWfKKf4rfxObf0ujs_kygjaiM-6-iCrpQrbR0v4vmdontBJkPmASYkBiWdK7vT7tPVbr4YLtoAuZOJxJYOFK9IeUUh4_d2IeEGoM-nUzbANnrmDl902ddoHiAGbMUuhJc05mXygpGoTXXgXBwvnLLGaWKLe8VsI_x8CwM26c71cVpu_mlU622-p4AfLhovIUAnH_LCHWLH9_XDh77p8vR9QHKjn3COwfT6QYL3OAEFM6I7Bc9E-hvlUY7QsGlRHm20iKm6iR4PALO-JL_Dnc0bWwTQY_LJQJgb7VrVqHW6tKUHPsnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLKYwPa5aNodM6sNNIXta2yqrB4YXJuLpJusGQGcG52Hl-CnYOQUXKjhaL_hL-5nH1_ABIdOa-egm9Vh8AK9WfWJuZMs3DgAko3w2pFbYFC0gNvQcb998ig2niHIv_kFLcqBVgMLRRLlQlOE5Qc8isb9L84lx1tmqRTnKGAoXO1__J1JCkRpX0PzQR9kr1CPOEeYv4HvoMHpsK0Udah5hLH8F7UoLNUnUBfuNw4vEI-0yZZQHIud_JjV_8uiGnn8sMrC_kKoDhW-_fxkDnev-x1RsKcPVZvpPgbmHM2bHnPmmBjke_joHFvEvi8xr4U-u85fC-PDFNX8zucDTy8XgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYmtunbqNlC3nor_cdTSGPV5BINoZTHo8GnRO6Z3_4QRAg4Yy0rGt0HqLjiN-BSKfVb7EKhvfcSff-M7Tzb17V9Wrpgsg6B9Qzg4M7X82Pz9RO2wvLPTuHvvGLwStxbd3Nu4xZsB-Ze-xFKIBWIjeNRAlxS55QVQeqLAVlEPrtR5M0UZT9lWllHlwHQboMPsZfntxrsbqfXfqNlFkI6YUjBLVKBjhlf8J-4M9Ov38KtdxNDll5XOgAhdAsk1BkaaV8t_Fl-OZmup2tQbgRB03JKVjgNVdSSYT-SZiLkvqJZyVr8G2q5RrXV0PCunJ7_ljPya1yBc4JlyhgHHst_h3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8fNzYt1TSwr5o6QgyLV-5jB1m7jEVmqsSTfHADlh7LMOcPGarkYq6jWTrbIeKK7x8G7KcjTzR-wWx1hSboVTDSC-Ki4TzK79n1JKzy1z4n8rVVNkgQAawj3Ajx-zPqZIJHuioN8vyhmc7lDI-YFxSnz-Gchy2k669nlKXvzI86NSzhD7fmtHjGLciHpPyQ7_u0aXXDu41cpl21j6IoiItpgDqE6TWJhTASUaD467dgoicuH1CN1YhbhgVZkfY-0JEIOK14c-M1Z4QKqGEvA9b-DOqAbICXU9L3S1YVsUMkRI2dNljvDBuVCibsFmm0m4aK1xForvnOW2Xj8phY-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLYY7DiTHhRR2VuVXo1P9aLjmIb5G0gLO-K1Z_2bTvDBM7DVxJEAbF-u8MnU7ifsu7Hdc2a5Cb597BMYoqrXwxI_fTcSd9bHQxXyv00Tv1icW-09W2ugWb6PzMIy3AJKQ49G9tywXyMxYCctR1xvp4Xn767ZCxssguNeMoFMeqQn5zc01b3LKx43LrhhwYtcmlOyvwxNVw5afQPBcPfasvEPSn9UjRAOPfE9bvSILngcwUwaPqCW9HVzCJh2mR_TKs0sodtnDOp60rzVZP5UuoehDcuCOfu-3bFVeux_azDJoKWIMvDemHyyMCKBp-vXmqPeEJdV_56gxTPEa4uB1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVzFa_lTmTw1h3Qg1e1MO6822jHmxdNo2qhrci8TKUioHWYhO_wdO3npkqBu1ha9wvNbIzerkifEljkFV3LLQNQni0nt3VpAfKfovxtODWxAFSJTz3iBR9R7HS-Wuhex4HcAYywONwyoWlaqFmzvP9wr6thUwSIR0KeAn1xm2SssnDgS95iMoYIEiMKoICVSqphRQ8dYWQnDJLwcAsPwxo6dsNGLklVvwJDjxF-yp08rJNgwBOseWyhHlCcfNZJeTHwI6n3zfuzUBVKeYVUPNKlfqMULwJqd-QbYNIhDRGv8gU-3DCQ4UD1QNPLX5srvqQunFLtffbUjWd7nWDSbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmo6T1EovbtJ4A0ooXOqj7brZ8xQgTGxXSWNi73zU0sFie8q2nJQqZVUyweuEoO9RT3ehwHfS1AJt4N0Dx7gEWbNUJ7WFIsF0C1qQADU8KspuICk2_R7mJzETqjU6MlbzsR5NQPvHw249P_5Nw2ei4KL2DFAjIPR_r8ZghF54T8FzwTK1ILNhoaV1AiL3ivdYesJCfNJydDbcEyFD5pDmlkLCl-Ykq6WUZeFHck4Q9RHK0QtX3cCR1CwT-j8PDFfsIEiQpPWVfWMAdbP7M3GawQ0CuXeAqiigojNXi5FsVPKd--SWI13hgTzXEOs_E-9MgrnD07MoEfv2vm-GFY2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cneegZuTcZTJCfGqG-t6tH-9_BO2OBVDiC0jvYhumQHnz6br95Rp4K5ADNUKsiVEPQGtoWeveTaFg_kxU8DFCXz-3ikRAItbIysOCFlY5_X0VB4cWNwzvVZOmqWXp-02kNUJgaa8Wz-N5KrYyoGxOMOC_AcUrM9GvVrIMyxQyunY1A2yfGZ1YQtUT0JUF7SWCasefGbZfOw9F5RK43vyNlTm3ftQUSLgAO_yS1O4G4a5OMqfauwY50R3EAS4161kTt3VQjkRyp9_hm89aYg9GCJHBUqBN4SptL0VqnRUynr3mkI6OOcZSijBimbcGYstARNp7yOXjcAIC2JdClIGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWw61NcWQW4MSMr6UJIS0HiOjPhEj1_G1T5Z5XYjG9Yy_7hZP7isq0mv76fXaXtTo_5UthRMFioTsCXKlOdr9qDZw13092jNnH2ko15KgWIikCRu1OCVzbchXL-PcxVhKAPtk75OWaR3-UaxQTSd58MqB9k3KzrqrlFRc0jW6y1xoDTfdI0tX79pmFDLSI4KhWQJnA6F-i_drPmAmxDJKR3Jh9BOgTOdEeyFOkKYZMflE47PuHCBB1tLa2NTTzZIA1mN-hiHnteWfmVw8gRttL9DJDI75c2ayLFgpZUkTt1w9FoIpQxZVteYdI4akE7R2RnKIsT8gucNfq7Xj-xmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=AClk8qfF6ht-iaJMwTrRCR0jRj5u46rc7fnFe1cK2ndlOC8OwYm19izqwrOnThBrUc2F8CtjkSHvhe1hm7QO_aQ0-2PqplDm53nw7UzxyHtbdUsq8wGDMAqiPB1rMVdarVMIEgo9JiZo2M28axQGivXsHBkhrS3HYgWBmashQn8n7DopBlV52uNqOWJ_8Qi-ssxs4HXWGju74jgpGsHBEofr2fYCCGeJ02q0dozkxHpH2mO3mIpbDk9C0uQSV78R6iMBVJGzfJzTGc6E-g0UL-TtHhso75d_-bxZ91dDRmd3QwItekjiD8bLEdwMewBXwlDCfGIjzw6pZc6NAFgWjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=AClk8qfF6ht-iaJMwTrRCR0jRj5u46rc7fnFe1cK2ndlOC8OwYm19izqwrOnThBrUc2F8CtjkSHvhe1hm7QO_aQ0-2PqplDm53nw7UzxyHtbdUsq8wGDMAqiPB1rMVdarVMIEgo9JiZo2M28axQGivXsHBkhrS3HYgWBmashQn8n7DopBlV52uNqOWJ_8Qi-ssxs4HXWGju74jgpGsHBEofr2fYCCGeJ02q0dozkxHpH2mO3mIpbDk9C0uQSV78R6iMBVJGzfJzTGc6E-g0UL-TtHhso75d_-bxZ91dDRmd3QwItekjiD8bLEdwMewBXwlDCfGIjzw6pZc6NAFgWjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=W1TlL1axMLw9iSeA2uKqtnmmr572bgJ8ZhigPhfWdghQ9nJbNBKq6IOTWirn_KvBr0Gw-tdhzOdqILAFGX3npJZRb1z50CNJMo6lG0P6vn6qoGLTxhN1gPJBLGdI9DHRUl4JMTqeqUJ2GbPf2mPtJPki-eQ_6SUMZA4CzfJMSh0kLE6vNAKY9Or4VKm_jI1sbzLA94pia9hVhdlWPSW-nyHC7NhE6po5D1vkwX45HSydAArZJkZJT6P0LQPD8p7SBiyYPE2PI-xsPKAOOt52xyHbMbJJXBNpd7cIesf2N9AK3U_k5kvWyzqGxA2bYmwlowly-RwBIFaj_kZWFBwn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=W1TlL1axMLw9iSeA2uKqtnmmr572bgJ8ZhigPhfWdghQ9nJbNBKq6IOTWirn_KvBr0Gw-tdhzOdqILAFGX3npJZRb1z50CNJMo6lG0P6vn6qoGLTxhN1gPJBLGdI9DHRUl4JMTqeqUJ2GbPf2mPtJPki-eQ_6SUMZA4CzfJMSh0kLE6vNAKY9Or4VKm_jI1sbzLA94pia9hVhdlWPSW-nyHC7NhE6po5D1vkwX45HSydAArZJkZJT6P0LQPD8p7SBiyYPE2PI-xsPKAOOt52xyHbMbJJXBNpd7cIesf2N9AK3U_k5kvWyzqGxA2bYmwlowly-RwBIFaj_kZWFBwn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=h8A7yfm_RPvzDCvpjAkll3iAsKRtLm_Qc5FURYlro_nNqkoiOdhqSbPXma90S87rgUIQq57XVu6CfJ7-55PUVUnzqJO3OYe8IjXNzVUv7STh-uglNdQbvJBXByBRroay6SbjZhEjnQnhRBYBB3huiBr2qBn5vrUCr1ggmQ7PDeiVYmLA9RbBzf6Qo7KZBeHaD8H86ugxaGVgIODDccF57Bq8OTJZ9vMJb9Y6_La9bA7ArmWhnbggqMyN9XqigJT9X19oidgupzKKOqzB6MWU4AJxauk1aJ_W_bgICiwIa3CosK1f3FMYst7_6r4l1Lgg_tiGZtSKu4GZfyabj31MuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=h8A7yfm_RPvzDCvpjAkll3iAsKRtLm_Qc5FURYlro_nNqkoiOdhqSbPXma90S87rgUIQq57XVu6CfJ7-55PUVUnzqJO3OYe8IjXNzVUv7STh-uglNdQbvJBXByBRroay6SbjZhEjnQnhRBYBB3huiBr2qBn5vrUCr1ggmQ7PDeiVYmLA9RbBzf6Qo7KZBeHaD8H86ugxaGVgIODDccF57Bq8OTJZ9vMJb9Y6_La9bA7ArmWhnbggqMyN9XqigJT9X19oidgupzKKOqzB6MWU4AJxauk1aJ_W_bgICiwIa3CosK1f3FMYst7_6r4l1Lgg_tiGZtSKu4GZfyabj31MuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URJjLZhhH9VqxG8adHe2b6AJdguA3BWZt00NdSN6RW4Xr6ik35PLTW4n7J9bzXqw9dW-DF4KvNLPc_Hx2SFCqneGH1MPkqMd5gGqr3Vlv9vBZnDB5hBZB-dqgkGuD4kMTP6ow1DnDbELpF3v22Bcg1YZxEBBxwbvrpcAVNlaUC5OthgswnqFn0Epm1fNGYCZKHj73CL5wbxFqQtl4GvAIQRhuukxqQ4-opmvl9LaUHdOlsvKruMngfxc95qfL5RmgXYOQ0TJ5B7u6YW5KcL63ZR8_4dhDvfrTPtK_j3-5S52GjaRCnON3IkMWBgHQd0C7Qagxup53w0PE_vzgcPumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=QiyKG9466jFoCSQDp3QYPLSOldeHwXUiQTV_T_ECuwDjpLVhwbz-tyxyxTP7ZZyFUxYYbc67O_1cnyHefGhfSM_ChXMiQna1iGhUbpvAH3a3lSIA8yvhRmts49KynqJVFj8GTNwUsu3pYq8rhGT299n5-EeLQQ4sc79RNZkA77Hk4on9j-rtI1zwD8zE5rcyqAbqqhZ22coFAh2KshVWDTipVVOAvRZcEyRlvUnI3_hhuu6eqibljVxfY0GcahR01UciVv7tHTOawIHwRt9jpjN5cD2XygCD3pluL3n5HhY2FNa7mH-_SRecu4xctIo37EmzXuzK8RANK31MrIDFcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=QiyKG9466jFoCSQDp3QYPLSOldeHwXUiQTV_T_ECuwDjpLVhwbz-tyxyxTP7ZZyFUxYYbc67O_1cnyHefGhfSM_ChXMiQna1iGhUbpvAH3a3lSIA8yvhRmts49KynqJVFj8GTNwUsu3pYq8rhGT299n5-EeLQQ4sc79RNZkA77Hk4on9j-rtI1zwD8zE5rcyqAbqqhZ22coFAh2KshVWDTipVVOAvRZcEyRlvUnI3_hhuu6eqibljVxfY0GcahR01UciVv7tHTOawIHwRt9jpjN5cD2XygCD3pluL3n5HhY2FNa7mH-_SRecu4xctIo37EmzXuzK8RANK31MrIDFcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=UPOGUVdNlShbcoi6tchHhdfak9gueYTkfIxJo0PGc1LweWPFdixQqPkQSJndKj1s-qZUvk4KTQcyNCX6UEwGObjodjjs69SrcJxXArjXtbPZloWOJgTnJCSS623iGC03g3kg6DrVUnhtxkvz6RNgvB8o9cDM7rWqdcQNBOjp1ZD1ltiq-cSwqc51FqKW1WEPCWtOndlFd7bRKW2qxmv6nJgacxcRQvAmXBqy9yQbkyrqN5GoRrH2BtnrvZz-87NdJk110a2a1HCvqgQX5P3cQnvqTl-2fBjtxjmPTSWTzhUxXjDUmoncr_qhhHiGHk7JrU_5UCIA7JW6wDFTRSktgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=UPOGUVdNlShbcoi6tchHhdfak9gueYTkfIxJo0PGc1LweWPFdixQqPkQSJndKj1s-qZUvk4KTQcyNCX6UEwGObjodjjs69SrcJxXArjXtbPZloWOJgTnJCSS623iGC03g3kg6DrVUnhtxkvz6RNgvB8o9cDM7rWqdcQNBOjp1ZD1ltiq-cSwqc51FqKW1WEPCWtOndlFd7bRKW2qxmv6nJgacxcRQvAmXBqy9yQbkyrqN5GoRrH2BtnrvZz-87NdJk110a2a1HCvqgQX5P3cQnvqTl-2fBjtxjmPTSWTzhUxXjDUmoncr_qhhHiGHk7JrU_5UCIA7JW6wDFTRSktgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=YX_JphyDJxKHuje78yVSSGcvwSf8pd1YXwW6xMNZTVcwKggbgWTZVoMIbKF0xv6ryk1-zAsatFiY_PZFgxdJ0yEWvZfqMAZE9wEyXr405PZew15q22MZ83nXImAHKCCmvw4QTkyIoTQqP0aj0cJS1zqhSmQED1VqzY11q-eY-r8iUmPJxdEiPWJSb8zedQwDXAQ49ymrHwAayforaLfJNIjN_5kyXZUukCA1L6dmnEdDaymzXAzDwRxlnMcYqmxKWKnvmoqdIHbOkcaXPIcHzwiXOv-GAWkzLo550Y_MHcFTv3V0nveZB3KwdUsQL0T35GqA7dKQXjfwfMawCbO0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=YX_JphyDJxKHuje78yVSSGcvwSf8pd1YXwW6xMNZTVcwKggbgWTZVoMIbKF0xv6ryk1-zAsatFiY_PZFgxdJ0yEWvZfqMAZE9wEyXr405PZew15q22MZ83nXImAHKCCmvw4QTkyIoTQqP0aj0cJS1zqhSmQED1VqzY11q-eY-r8iUmPJxdEiPWJSb8zedQwDXAQ49ymrHwAayforaLfJNIjN_5kyXZUukCA1L6dmnEdDaymzXAzDwRxlnMcYqmxKWKnvmoqdIHbOkcaXPIcHzwiXOv-GAWkzLo550Y_MHcFTv3V0nveZB3KwdUsQL0T35GqA7dKQXjfwfMawCbO0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=RrRksiKG6QQQsnmfbGg7psCcqiO1KcAJPJMOz_vYZb7Hyhayh17_VcAXRh3DM-8kla-TYbvtsdtZe4gYQuCUkoKtTMgOYn-vpEdvYA1DbkRRMt6j56SI9CLkbQfnwalStYoPjd54LfS8DyGXdEL4g4GT7TxJ82GHhAuw0WuEjS7TNpOxm_SVI4GXVaKE0uCO8iglDR1aF6SpW9C2sQ6kq3EYmUDJOgZl9hZ4iwfQsiupbToX7Os35CbjMqLKlt0RvWw7F9E88FndCOjpu5irqHygtPwUAVGohQrqi2vMjoLIe--qFbVtlJMXjQiRDWvxP_xigrpUUnq4p5GRilp8yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=RrRksiKG6QQQsnmfbGg7psCcqiO1KcAJPJMOz_vYZb7Hyhayh17_VcAXRh3DM-8kla-TYbvtsdtZe4gYQuCUkoKtTMgOYn-vpEdvYA1DbkRRMt6j56SI9CLkbQfnwalStYoPjd54LfS8DyGXdEL4g4GT7TxJ82GHhAuw0WuEjS7TNpOxm_SVI4GXVaKE0uCO8iglDR1aF6SpW9C2sQ6kq3EYmUDJOgZl9hZ4iwfQsiupbToX7Os35CbjMqLKlt0RvWw7F9E88FndCOjpu5irqHygtPwUAVGohQrqi2vMjoLIe--qFbVtlJMXjQiRDWvxP_xigrpUUnq4p5GRilp8yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpjkfmgRVJcKl9_731z-_HNzZES5B6ITaf0L2lgz6gLROqeTffcxgrUBeVIQLvqIZUvGLUOAywj4EZ67jS1VyYI5AIcC6sFXzQQV-ugpb-GEsuijz2AD3cvNywtODPnJMNoaOYWlDFtTzlmrKNf5iIUxmJ0LmbBIp192-nJN394yyMnnquoHwrQrKCHQSx9AOW9rtXUaiXa_7FvsS67Vh5PYyYTHqoO3qS6fJ7y9o0qw_LM0vcVEEmDF08QcuvPV8FSHvf4WciiNALhe51cR-taVD3vANptvwWO_FEf9t7B1XixGRNSk2lT21JS2ToMTT80cQyZFRIaPDsTkVszwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g19WcP1JtQIQ7iT_5xgQ2zpswlGjguLUREFFuvcCRN82_zkTdZusXAV-8PFPaw9Z6tdNk6KCaBgG7clvpF9z8TtKTSJCpJHD5P_1j6L8npgd_MZuJHPLyeo91GFG5_UKfvNsVAP1HBMlpAfPqmX87tHbY0uIixalhwgE91F13VS8VVhHC1VYNjI4pV2U_0w0ABL7Xieo3OS0RlmHYiDC1CI_fp9l8zzRTU6PaGByNvdilJkqD08rFBTb9YM4axXuD7QPoIrbPi69TrfQiZQ-oHMYww7f2nqhsbyRW2lM74G-2B-H7VwEsdTx1eLMYtwJsWGLz8xYAASGm7EFScHoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niEo6Ki_Ct5tPUBErsCV0SZ9OetB44Odb2kb1sbzJ6umttWSOVB1w4TUAn9hNtpplxPBclSubmc-4lDC6FYw4P4yUPemKEXNtD4cjXSirGomZl0o1-omhQofRrVzXmV1Sn2Eu-y6OJ45EZLA2Fpb1ODsLSqi8fadzOUiI7mOdsd9KTrpB-YGkeL8Nm_-JPmGQBSjl-1Oqfpo9TRuOZQuscnlJhrzPcwJ6TDOroB_09ivPzd4IbNsUA2oF9K8kMzx1ISzZP72_s2vQAFpTWRdmz7RbJygm1Lhs2tUb6rp7NW-ose6ie5BeqztoATa4lP_iwuzYUGbDwg3t0Fb--8Dag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JGc7Ut-p6ZGcLjX8oTN6cswtLLexPAHqJrmJpZ46LzHxR2LE0-U3CFvF89pcQ8hdFZVfgVwTo3Htj_xGWGDAGGXZPK8UDgMBVEj2djWy3NPdm84qGdug8ccowGrVvixfgKnFol_1-LPoPLRT4pXfqSfeuTgHsr2xONbXzOUsFt7U38oTqjb-_DfoV_PMmm9b-mErw09iw7Tkon0SYX91JLkSzocJkLuxwKh6ueYP_ibwBTxcDqkKSetoIjsQF8-SYGvZRh0OT6j591ygrs-rb3016uaA_7Tb3LvnUmlcEgC1R52daC_IXdHpaE6kbRrpBrZJ84bO-Jwsyh0AB0I4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH05-xQsZF1YsJzxUQCOwxLPSsnE_F_clcwyaC7WjQv70CeBGnjzZnlIKb9NlxOsyqoxm0rorQ9M8RpC_Nhe0eGpxQ3txPFhI4sMr6hGI5Hz4wqA_jjJ376ya8BPvGgBx3dHZpvt6HFFx-kJi17etpi-HtzRrU165Xiu1FsjYWOyNS3yLPyrbWxiV3t6AMkYn6C_5FpTWyqOQHZKxwx_2MfKoMzBaQAgskmfbRs5jYcr-mVVrMrOtgZ37ErB3xMOZyuSEisHOmYu8ufXAYqJJNgyvfwHMNsfqYxoml8U3Zw_K3MrN0NQi1S4OGYob-D2sHscdPg7pxWyuHUNuDMCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6tHG-8GyIw0XLu3LU_kv-lB5BBc0z3b8YTySW4yEO5_IctK6kqzk2W97HqJYZpyvX_kmXONaWpx61cTLBDpwIAgjOLTt6H_6Pw2lkkLPt1iiogvUVAtoDmmXTHQjtDPC1WPznMoyuuk6fyKQO74nJ--KxLw36CRmlLlqtFKWb--zav9SoVu5lK5HjeIPWf4UvamlozKmNZ4aKyrVqeB_sCRaRkV_KplmYfK8vr4F1NGLTpAzIsdnlTXhd9SxO5xcluzmfSDR8h1xwmvJ0RAwMea628StVBbXeY3B3790azBZWQiZTB_VSgI_p2royJBIxoXlRBJAg7IimKlONwPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCSPDyIpZFkkL5YredEO5_RheeXHdCySxD8-l2Y4TbSyX2pbsPWM-9KQ5QLouTnmdRWcb3pgoBwt43fz06nWYQTHjcGlUtiJJEo6TiZYIoVpkDt6ZsyEKmykRTOOmQdE2pp4H6jr_jIJ2jQB_vhNriEFki5f0aVR258cHOFFv3Pq6PgrZKGJxDgNJcKfVslevGl_jsgdc1YrL78saVWfA3upR8-c-Gksj1nYwJzw-ty8TuKTaVLKHlCK2N2ixj1l_QLpGNDZcc8Fw_NxhEPkq9MzaP2MYX3cYbh1eaN8ZUHhOKggOR2xfyHpo5X5jTwZx6LZ6YSrwW5_07OF4rd9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5u-6oUKyD-7qctV1ZDYqIMcltGBKdIAKNckWiFvuXStKpX-P1cTekQ4wVp8hsYuJ5mLR8w_79H3gQR3R4mKHurLHr2FxjmIFtNfEtyGF4Zx2za4VbzrywsCZ8nmJQ26XXUrhU5fYa03Ap4z6uGPxKVgV9aAhUPZvBA8QQOFYp36AQ960-N_SzzeD-mc8o3FIOFzeX_TKcpYgoiUD50cN8ZbjxkdqtQQY5Xe6THFxMlpLVww991jRoPRSfBTZR3uyb6oJTpzgvd7P-EAx1opHL13PRjOXQdLn1dwxZlQiwapU_A2Bro7aKC3i3j07k6vv3rs2xsLS-NvpCrcx4snfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzEh2t6onZ_SA_gBa0fJZnLVN8MGH2MAbdlazMznAFlLK5JAliP2WV4-XnMh6Vi2Vh6kvz3J-jgU6Ennnh7E5uZ7AjDSkd8t39AK7-BQNg_gGmUPzHOg5P0xWg5YamTMCUlIyJ0z9muL6sOATdKKPqUhqzjbVauoiX-HpU7Vo8Ignj41i57HoN3hfSZaJGTwOKvPBxy82cV5Kqdp0ZaBXbkXNKZ4dFRSBuJHNX2C6DTQPMmReaT9nPgxjqDwNBbF5_4I_cWJzMzIWyOMSc38V-52KStY9Pfvexh2uz32cFguhVSkum8VoPEehYQvAJb6PVyN1EB9KWWf-_Fsrw7biA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=HtQTW2EdTEtNyyygbI1ikAfUsoD7hOEVTUX9C0NyUrLY1pdTBfV2c52a8LrVhCa3fdgWCluGQDH_Pw8Q64JjVGBpCrn1cln4uZRVDql7noj9dnvSjahCSs9buYGhPw2Mf6CL81DhwfT-Tea9zDgQRmvZJdaDg7Vt_g288_m85sNndHIJuDea5j3gavfqEEtfle6HoMY0aOSC1rzrvvzAfNRuWTCl0UuRKzA5LU2YODqKDyqbWCW5-FeOgU1sZioJzyXQI-StIqTKAQpFiEJCUgOBRssrluV_dLS4n4a-sglDUDELcW_-N19zETONg3qH6VvBnl-RSC7z7E5bYFr8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=HtQTW2EdTEtNyyygbI1ikAfUsoD7hOEVTUX9C0NyUrLY1pdTBfV2c52a8LrVhCa3fdgWCluGQDH_Pw8Q64JjVGBpCrn1cln4uZRVDql7noj9dnvSjahCSs9buYGhPw2Mf6CL81DhwfT-Tea9zDgQRmvZJdaDg7Vt_g288_m85sNndHIJuDea5j3gavfqEEtfle6HoMY0aOSC1rzrvvzAfNRuWTCl0UuRKzA5LU2YODqKDyqbWCW5-FeOgU1sZioJzyXQI-StIqTKAQpFiEJCUgOBRssrluV_dLS4n4a-sglDUDELcW_-N19zETONg3qH6VvBnl-RSC7z7E5bYFr8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oESd7NZy_8zOCcecPqo9Yg2rJQ8e1MChB9n95UAoCzi_Za5n8Y0dK67wjQkk7hLf6ZaUhl5xfgeLzraqMraVFEqURkKgNgV1RJmZ1II_a9upNBegpMKdh3WxQczOSsTwSsyXoXt6BOHhtuFLMl-5CO8Ny65sGXqxwBSMGSLWsJph-TsVNlIG6yACiwX-DGKdyDXiPTspIl2pNuTrKio0jkgNLYAVrv7ApwBeXKHAcSXokU_NzhVG1skkVvNaEK1YRVaAmnHbaOE0yDKCKfihwZSf1woVRFu7RW9IFJoLa1FkS3tpi4LQlc1LWvyQ6q5_kbEGurLNnSwUb9DJcUuM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwStFbBFZrpJ4lSPgo97oDLXzOklJIGhvmstYtqQtJDEPt3T0feNn9PBg_9us0mhqxp_t2aWm7Y966eiioeb5bxXBrGCdqZgLa9CIDyb3Ex6Grtr3-76JAkAjc5je8bW7gQ8guURub59zBBV_9mxYX1gtaySST-_hzVdO7QHS-0ZBP9HmqhtI7ZzYU_gbvxhDQFLvBnWWOMnbiPmrFl2xdqPzPmzbteeJ1R-HIy9vIWMl2m_Ueu4CsY9eLATdP8W_LfftWxCNe3wVOuVEj7AbkdFI1MchI-d0HdtMaRojwmYkLM3r_DwfOxI7LI9A5Efx7qZGHR1flZULdrO_xY5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_6GGOpi0JVvFzx_ntKCUOJVOCIn0P6SU8TlAAAXgkua5S1hZyqVQrbtJvaISZdyC4eo0pgeYneX23_pLo6hxlAbaXvlEJwvBwfpT0UUPW9Vqpl4_5S9DTCK8RczA5Bypy1y-CO7LOWTaxqF6tijPIi69vd8yZZQ6rTZ6KkgIxiiZoOHTVCF29TVyhrNsbEDOkwsCRC0tPvNyq6qTWcIG2edjkfxDgbeKoM9Ze3BWUchWZLFWoKBG-wR46f0-fCYetZB6lByriyHUKRTfp2_0ZtOtcrK-FNBN96ZOckfLo5FgAh7pK02QQgn-KpTnwilSPyIdg6145AmhSzeZCNftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmzXUmW5bv_845QkLLffl7yuGcAQLWcOml57UF7GxLk7xRaWH5SCvqXzRWVD5QCFoyxkwBI4AueCUL39tEPUsdYwg9tajss-i_am2Sos-_NitygWXK_j1HbfTaLHcBGPLUa9LN5aIB07KNz8m57NYwjuPwfv4bzM1MKtVnrWIOQvwvh5XFAIM0Y57rx5YBmUTdVXaVObWQLhA0kmvdN10GWTYcJnygckqSWU3McIvtYpYEWUj-Z0WVpQ2gvNpZatqbGwu6q6IKDGgbLvHOctJeWRR34I7cl12bbsSn3Re9yvtyvjAZOsS2AmxV5IaQIYDX9VLdz9WvSOtr9UA7Ad2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=K93kNmyW6ULa9cthnkr24AsQJw0zSyg62fieLnx_rEUaTQ0zLhOtiqX7E87UnqcG_z2vaLrmc80osZ7tXhB2tXW0HhMUL4QmJPtFGbWJJEPj7A9tGvk7UEceuw26Q7SJMIRf37Y2RSH_IRaNSjYrxUpmK1REH7rQWNxEvsSOR5-YXltKUpdUJqbFXSJI_yzo_7TQhfyHjLqVkZoQ2kTtntXn9119kNxy7UOfZRPDwUvg-8K0rBuoILEk9KRz33cr47gje_HucVlQe582hDqJE-D79KoMmLH0akJwZsxCmf-nHDHsgIPZT4N6SDNA6tQiGGMqmhFLhIplXsNTWHJDJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=K93kNmyW6ULa9cthnkr24AsQJw0zSyg62fieLnx_rEUaTQ0zLhOtiqX7E87UnqcG_z2vaLrmc80osZ7tXhB2tXW0HhMUL4QmJPtFGbWJJEPj7A9tGvk7UEceuw26Q7SJMIRf37Y2RSH_IRaNSjYrxUpmK1REH7rQWNxEvsSOR5-YXltKUpdUJqbFXSJI_yzo_7TQhfyHjLqVkZoQ2kTtntXn9119kNxy7UOfZRPDwUvg-8K0rBuoILEk9KRz33cr47gje_HucVlQe582hDqJE-D79KoMmLH0akJwZsxCmf-nHDHsgIPZT4N6SDNA6tQiGGMqmhFLhIplXsNTWHJDJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q86zV0m-qcO7pJ6cVULzcYDssW7gM6mrVTR-nibKCvgUq8fx8fvmcNyJDL3xeZCNHsp2LND6yKNilCj2DaiUykicyefdMPE9BB_hDgHLUPZT0NutG86CMKDfLNsrAtnawIYUIvMpgkl6cj6zXoomPAwUCWD_m9_kUv3kIlvN37WdXKggq5T5v2sMdU5w-DR7h1H6ltkJRMPEFYxtH4_stlUQ5b4vnB_8hwrn0PacbPzmmVvgC6odEj7X7AgkRBTl3w6zsdI6sQVootNgAPkK5-Jd_1BBZrGdobBFILeezkO9hyYz9_TTgLnpXj3iNfJzwuDTTesfbB2DegUuWR9GUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=pj1ofYrlmwPKZfnky38zMwCm9iGQtToGKnpMHdkUoh9rtcL7J3PCJUurIr3SOINIzn0x8W_Nv_R_VQ4YI-4RscUNH7Bi_BOa1dQjmnO1zv7o6fPri2tcd2yK-TxmzkFmWw3VmlP0Kn0IsVzIpKwDs9a8xWFOFKc6xdjavYtZ-zzF5oRPcjXS1o_8z3VaohDlLDpCNiX2t3WizCeNgyNtWnHo_1IbtJmyR5ANIpVHrPP2Lb42O4aGqN3Ns3WWjY0xvjhl09zvI_HMFWZjoUZ7t-CYii0w_ppXNBypC10r6wxhNkXl7ocWyT7Cu4ElncyIFGhvuEZk-xW1JmpE3qDkxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=pj1ofYrlmwPKZfnky38zMwCm9iGQtToGKnpMHdkUoh9rtcL7J3PCJUurIr3SOINIzn0x8W_Nv_R_VQ4YI-4RscUNH7Bi_BOa1dQjmnO1zv7o6fPri2tcd2yK-TxmzkFmWw3VmlP0Kn0IsVzIpKwDs9a8xWFOFKc6xdjavYtZ-zzF5oRPcjXS1o_8z3VaohDlLDpCNiX2t3WizCeNgyNtWnHo_1IbtJmyR5ANIpVHrPP2Lb42O4aGqN3Ns3WWjY0xvjhl09zvI_HMFWZjoUZ7t-CYii0w_ppXNBypC10r6wxhNkXl7ocWyT7Cu4ElncyIFGhvuEZk-xW1JmpE3qDkxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbY5kV5qZ2NeTclJGh6AY9esVVyi1j1JNWGPI-5u-3ID7U8AeJAlaPKg0ctP0-1DtxutAuXAlZOIjksKTYOoIf6gRlKLEpJ-WgzGG1t2NjonSun8vl7iUIQLUfHD7qHSQvU2l0_IH2MacK6QtvMIZkD5hX8to5aVDVVm45tp7KWIQVAdeRSNOxfGwUMcaWZx2_VPsXVaJNtpiv1dG85rJkmgq37GB4WE7156A-iiBOWfhWWMk83BiTTQRB9rhXw_f3-fxbrs3CdGM4ZmokvzDtzVXgzwo6n1WJNF0Cdp9MbitlvEC8c4yDwaeBQXNC2LbbUQhIRwOdlRF4Oi9yOhyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=TK4rU62B2w23GLw0j20Sgpc2Z68Ll75GbPBXs3jn2xZmlDyKmeFT-TGLn4OOaUR-JMPsVYtQEplGPu8UUohGQF1i0VSkF7l2nOle0prARmiJcwuxYAOEGysUY5zQYiOoaq0FbWs6Ed2XM18CL5yyqwqXBn04Jyn_0m-AbEOyFxoxoLtYzzdXFQP6vFXTcpctAze8J1sN31J--whe9g8jaq9hPeyFCLggv2sDt-_hxcv7Epfp7n5t8C-bSzijbC1mV45tcO7-vcSWCLW4i5yWBbh2psxc2a-pZWgKPY4aPDMW2QSm-bZOU92aVGEEbvfM12c7ZlJiT-LqE-7T7dtTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=TK4rU62B2w23GLw0j20Sgpc2Z68Ll75GbPBXs3jn2xZmlDyKmeFT-TGLn4OOaUR-JMPsVYtQEplGPu8UUohGQF1i0VSkF7l2nOle0prARmiJcwuxYAOEGysUY5zQYiOoaq0FbWs6Ed2XM18CL5yyqwqXBn04Jyn_0m-AbEOyFxoxoLtYzzdXFQP6vFXTcpctAze8J1sN31J--whe9g8jaq9hPeyFCLggv2sDt-_hxcv7Epfp7n5t8C-bSzijbC1mV45tcO7-vcSWCLW4i5yWBbh2psxc2a-pZWgKPY4aPDMW2QSm-bZOU92aVGEEbvfM12c7ZlJiT-LqE-7T7dtTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=jAgnwH9JKpai2OhUEl1Oow_v_0unAms1K8wl44jrVBsQnx-oOxyz6RUM3pFv76wb8LwZ19khVq1tW4t_kI5zydrK3ee0x9AhewwN5pR7FTQSEE95oSOHxoTmV_cCHEGbuR5pQqA3A1-5dcr26COmAItQiqhpYaLHBh7DqhZkzrWc3E3WzyvnrmQZvYudYOyXqbZr4RatnBzo3piEf-yBMig5KP8qUtLnN5qPFpY29umq6BmoGfVqwJtWyDiOh_oqC8Uqx8ebdAPJGBTepRDqAxhVX4ieNxx40z7u58T6XzZD3B0I728YcWJmmGQYnTLep0gV3MABAVihxC_z4S2eWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=jAgnwH9JKpai2OhUEl1Oow_v_0unAms1K8wl44jrVBsQnx-oOxyz6RUM3pFv76wb8LwZ19khVq1tW4t_kI5zydrK3ee0x9AhewwN5pR7FTQSEE95oSOHxoTmV_cCHEGbuR5pQqA3A1-5dcr26COmAItQiqhpYaLHBh7DqhZkzrWc3E3WzyvnrmQZvYudYOyXqbZr4RatnBzo3piEf-yBMig5KP8qUtLnN5qPFpY29umq6BmoGfVqwJtWyDiOh_oqC8Uqx8ebdAPJGBTepRDqAxhVX4ieNxx40z7u58T6XzZD3B0I728YcWJmmGQYnTLep0gV3MABAVihxC_z4S2eWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=fdgpdgCJDb2H_QbBr30rVzLkzNAV7mz2_DxCeX-YCPjmdWCzG1nEpoUcrmNTgrgh59c7TXBVH17aAgdvKUW9fHwY45c5P6sOzirngutK0dQqAIL8zH1lua7U35xvNHTatd0N8QxA5tpPfcX9yPtU-jGZMVo8f-5SYNcHhGsY5J1Nw70ZWASLfxBSfwyidQF5XfXI5fWZtkP4_TaXRa57g1AFCniNK9W8F2VP3WMC6mNLZrQRppOjF6-rnWGsAVFECQ2YSS5Wct2OzJHDs9rN8S81AdTjaI5QqX2IZ2BDaTIv88yd9gjSC6vvaWLCZjt5lag6Bu8A7NIjK19AkMxImg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=fdgpdgCJDb2H_QbBr30rVzLkzNAV7mz2_DxCeX-YCPjmdWCzG1nEpoUcrmNTgrgh59c7TXBVH17aAgdvKUW9fHwY45c5P6sOzirngutK0dQqAIL8zH1lua7U35xvNHTatd0N8QxA5tpPfcX9yPtU-jGZMVo8f-5SYNcHhGsY5J1Nw70ZWASLfxBSfwyidQF5XfXI5fWZtkP4_TaXRa57g1AFCniNK9W8F2VP3WMC6mNLZrQRppOjF6-rnWGsAVFECQ2YSS5Wct2OzJHDs9rN8S81AdTjaI5QqX2IZ2BDaTIv88yd9gjSC6vvaWLCZjt5lag6Bu8A7NIjK19AkMxImg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F232kqFbJnczKPcPCM0UglHWCfeXAUgdyhDg9lSxHwBfsUNwQSz4-55oo0Dz690Y-zwVrdQiGMED3HtXOwcH1kq8A3n8a5LHrYx9gK5RyLqTLGY3peokVB86D3XUQhenAbFvyMQ6Yr_4OXQr5Q70xek8vvXNpVaj72kztm7QHhxN_6hj_c9kdc63toPvIiT8lb6YMB1fU50llI1ErsWv-pYNIbLwrgWFHLdF5SXfwXrfyFSzglJYUaw_mvWb9hKew_JpPtmR60m0QPeOi7jhqad1KRHoruuVgAFz9O5UCDgUoYGVrwMMsG8AQyup627b59hNVL1w2vs8igWJnTqMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RSHRbAfgBU9MVj5ezYRmyRyiiMe5-oBluRBg6rzX37pfDQ0FKwe5UnpVqq0gEP3qJM5wG7ZIFjkL6Vv_41tPuk-EAnDxaze7z2iUAlyEGu0bktl3O-GVOqvJB_41jEEv8_UHukqLrKwUCwNzzVoJoqCI8Td5WS07iMBm5ivIVi6opT9cs2D_IX-BzvgrDCdKA69KyX_DOHw7GkKg-NDeqyk3KGIiQbZ77yScizMPwvTcgZzZ0i0EF7KRUN6hGmxp7RZ7rqVwFZ47BuC2FzMn-ww2rkKhczfe5SRuTUteNwMUuTE9NiieDbFzkTdht4gjtCi4zeuSPPPcCF2fwWRVLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=oMXzVsXLMOVlSjQlGwAja-C0aGYOpmLnDTEVv8WsPyQ6SgUq3h_Fdy-9jl4ZZXsXSnuy9FWXYKdo278FS79i8DxCELlkfQw3CiZtAEKdsoetxSPzq40jXpQ2tb4at6D-4sit1gelTLxktZc0Gbn6tM__nEJmZrqXO5LWHfODhbHBW8bEcsNqArqZhgUxkchMJLRKd8xAEs0gnEcVGxQ0osWLUPBHt-JT442Z1AfK7aRGWDCggix6UF6gbakqn1HWP8k1MWLGjAcy7iEhcNoNcHgU0MCYFr2F3RGnPW2S0IfyxJwEaBmhRCG_uwDbq4Z8PqRfqeqbWZ4Ug6TtyaaAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=oMXzVsXLMOVlSjQlGwAja-C0aGYOpmLnDTEVv8WsPyQ6SgUq3h_Fdy-9jl4ZZXsXSnuy9FWXYKdo278FS79i8DxCELlkfQw3CiZtAEKdsoetxSPzq40jXpQ2tb4at6D-4sit1gelTLxktZc0Gbn6tM__nEJmZrqXO5LWHfODhbHBW8bEcsNqArqZhgUxkchMJLRKd8xAEs0gnEcVGxQ0osWLUPBHt-JT442Z1AfK7aRGWDCggix6UF6gbakqn1HWP8k1MWLGjAcy7iEhcNoNcHgU0MCYFr2F3RGnPW2S0IfyxJwEaBmhRCG_uwDbq4Z8PqRfqeqbWZ4Ug6TtyaaAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=FjArCbdvAMnj1Qf-rwc62TTc02U1oqbYesGleUFxWxT_k_y2DuBNstUT2ItQOdLjY0qEtmtB7Ww1pd4D0A0Gc6XpJS-qpuBqk1wp3KsEY-HzEhBEQn7Jef0U1NE8zW3fknM6O4TIfH4LWiIfmGij-g0JlxTw_I-DSwCR43qvxZolVaeEG2KjELRPBPd7WoyQfaNv-Dz4iyRwacysaRdFujSp_VzvuCQrplcMWmy0wAG_utxu3ZokXcLTi7gqGwrBs1EFCjzu-709QFd44yPRXCJTOevXzVDe7Je7uPWopkGqdDxvIw41NtORsZwPno6opnL9vEajoUeDiU-FYR0F9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=FjArCbdvAMnj1Qf-rwc62TTc02U1oqbYesGleUFxWxT_k_y2DuBNstUT2ItQOdLjY0qEtmtB7Ww1pd4D0A0Gc6XpJS-qpuBqk1wp3KsEY-HzEhBEQn7Jef0U1NE8zW3fknM6O4TIfH4LWiIfmGij-g0JlxTw_I-DSwCR43qvxZolVaeEG2KjELRPBPd7WoyQfaNv-Dz4iyRwacysaRdFujSp_VzvuCQrplcMWmy0wAG_utxu3ZokXcLTi7gqGwrBs1EFCjzu-709QFd44yPRXCJTOevXzVDe7Je7uPWopkGqdDxvIw41NtORsZwPno6opnL9vEajoUeDiU-FYR0F9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsaOO2d26oV7DKOCWiASuj7oFWqycCYWDNeJb1RVov8D97Rqud2cBQFSqXwzNLzekfvKYdpMmlC9qIDumLq3d3feteJ4gu1lwRJhMZP5bsJaoi7UmAy_1fnXVu93v4aE-owBcPK4z-RDplirPbuznO7OtmgrDDWWnvxmvvcu_lrqoNdRq_uvywyTWpLnCWBh9Z5FWIJDYoRVKpFnWh6bCtnlAfNjagv4R4jszmnjGp-kSYIdi1BIWsVMSOU4ccOnh9t7k_BAiaMhNmmhhcEMd5_gg1MXvPUbEFxfaDr2jFbLkrQojJlrJYqIF9mUxGTBEep7DQHngVjZ0KasCX5DgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncy7KK9GgdfccDwHrVLf9_6h2li4kurwQOmm1fEwEC4erTYhpF4mnDJPLDEIucyolgAbYUtOG_OUESXb6rLK92J6_XzXC0tA9f1COsSluk4oQnH6wE9VKITDfl41-fZ6J-7T4-0kaZklnr-OcwDsEFIEPCF31Us01vYqYifta_bstb8s--QpkgkAHhoXKH1GWgRYRPFcOOrtC3FgLe_l2hQgPVTR0SlRnHU82lt5i12hVqILLXwaYmLp0YjCcSbPo1T-U-oVQxecZKf3ItN9j7p7se-F-X2BgnF80Tr7UbcCBBlaMWIEXCPBKE4bwL09UdLPwQSfi9bdof_SN-n6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mOdb2XoOT55BfjFPWXEd0lR777kOjXRqGybUSLFFHkGDcq_NxMOKWd03yDRqq6zyZRXUY04K9MFDX25Rl8WgDzDMLYAgq-0DnY6cuzPwDC5Q8a2W59AXBEe1zP0Mi4VgYf_ap5wULslg0Z_v51IxUlDq6pTTK9cwXXTprqQJZgAk9p7E5sWtLqZvAaHlNWc0Vjm4CEQyk48b-eZAPfcCe09EzWCVn461D2m3BkXttRwu-ZOk-Gq6ACO-HzuV87ZFJvhlEuCVVrJqkh_g2wuN_XPcyQaF4x9Yh8snJ0LLRR2E7DG46NA9M4WAlmuwc6YuXO9BfWVFeMe2sNnvi1PSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYRQczgzQ3jonnWK2lgk04MAoAU4BRaexbKIMKiMm5ASHv4hcrPVGEH-S0lGtfGQseF1AVthfNrcBjQoLL5NmoF5ZFu4r-W-YDmHmxzHzidh1m1gDkLRaTUaa_8VtMdU--w6h8PTZ6V8-TIBvvEoRCFAEyqlqct6EOKyX3FLnnsYPogngLHkFuyYzdYaBCk3j3zTcV6_99sp636K3Mot1A9wCNl29AEyqCSfWwYAmP0zAVltcuc4m46dLmB9i76wXkWlhP3ulbwty3HmJCd69L0ah1Xr11rptotQ0zrXf86MQR-4DQ_C2QouKMlxqrAh_uOsMxZxF10zW_o7gykwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHyyB9H71s9oEkXGoMEPNTqWx1SzIpP-zvDnpODoIiEbO_Z35EWhnfVOhT1tWaE4HkyekvY97SfWtmIZCnZfWByeo1P9zpoyzvzrJZgNzONiGB_zfod76qsGSRu-cBDss0fst4fjghw26rXVlz7_pHVMiYdBmRhO8o0I-bSQhYNJdIIhRokZSQ5qQBRVz7sohDgHnJXvgE4smwX--nGcSMQ0YMyaQtk_B-mtfZFFzf07jWkh2FvyOEFS1-sal8NWrICp9KyOPNS8ewdvJFfAb2Gt90u7yRRnB76OGGBW_WyUWUF2mr2d4Shw0Tc28Q6ZyiqnhPYgxVbUuHkLalMtow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J2xBvVzoh-BUKfVFDPOEwsyotN7mL5P9XR9DWuCeSTXPNloJcYVCV-FZlu0CEyS7-OMo8TL5QlRdoq1qzKvMqdnpVO_-hLMwkhD7kB3EaTRmCWVG5jkCfCqlA6YiB4z202mPX1DYDYoA58iLNTkHQgq8z7WWvYFQwXvnpvGC79fBBd0oHE_FqpbgMD2taGX5X1wxvZ4j_IC7q4Y6wDP1gwSuYJucMAnqiYgxnNGrm-ejis5xZKklMophQGvmIhzIHSSu5Y8Zgn8xxpoJgUqZbzWj4a3ZVsFczjQsQgtqKXmltKOCw7ku6_pXHxv7pGWAVpLaZOCj-zEhGy_CW8Cn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vPAKCADYoUZhNiUa0_Q2lluo8IbwygRXNlZ-HLqzfzN3zzamZ0YgcK6Rqtmlt-FfbLrLcRaVZGG0qlLW6ubKqM0zzv2TuTXcrpbxMQJhEFWy-UzrV94o9ViRn28BYcHrswkWTSgqmwqq3rdIxKMyIDtwStc039wE6xpKkHyC7J58jbfJbOFSYFYwp1B9P64Nzd6a7XR2-8s_fD1QhCPOu2VFGhWTaDypYSQRm61PGMFG2lk1N5suxVK3KbLx0SXmXJUlKR_3HUWkoCbv1C7jRXYxQrpd2V7aTJbD3Ta7JOZSvFbRGYjWcgHpU2xvaQh82oQ2TVIvdUGyVTAUl7Vn3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vPAKCADYoUZhNiUa0_Q2lluo8IbwygRXNlZ-HLqzfzN3zzamZ0YgcK6Rqtmlt-FfbLrLcRaVZGG0qlLW6ubKqM0zzv2TuTXcrpbxMQJhEFWy-UzrV94o9ViRn28BYcHrswkWTSgqmwqq3rdIxKMyIDtwStc039wE6xpKkHyC7J58jbfJbOFSYFYwp1B9P64Nzd6a7XR2-8s_fD1QhCPOu2VFGhWTaDypYSQRm61PGMFG2lk1N5suxVK3KbLx0SXmXJUlKR_3HUWkoCbv1C7jRXYxQrpd2V7aTJbD3Ta7JOZSvFbRGYjWcgHpU2xvaQh82oQ2TVIvdUGyVTAUl7Vn3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKEUBQeF-BehK0Oq3Fq5V33hFDG9cPJg0bHzFnQT6laPE_ZblRwIJB6Yi5qBteUXNRWG-osPUX_6pq8c8A4NG5bwlzzAj-yYsTyEGZ4CeJSyD__BS4IYMt3Vs73zg8uCdktP-sly8yEVysPy0xv0SQeyHF9wPdD91fcGM0sjHtiSU7AbeeIBjispZdcNz_5fu6tfn44O8cUrMuFd2ZmNK7TlQfJjpw7nRwAexkaXB3bhH-gcZPiEZEBsJioVslOwQZA-WyYZ82ImaFAenNu8wHnhWTGfQfExhEsliqzcImhQH4WJhG8A6eCGULRCLgFBYBqKL_kog35H1asulGqhIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fhd6z2pZ-ZZ6g0IAsGhiaFNa61jKyN1dk78snAv3nZy9BfKob0hxMooRlsDzgX_g1vie1w1TTFOFMMhCxXg3EwXipS0UacIDPhy4jviE1UfKfENxyhjmf9UHrcaM2JMiRC6vy1PjWgsngI_NaVuRhX9_zlNonIxWdH9qbszQE-_E4gT1dS4LtQy390o7qJnhEcUXvj2T5eSWfulTEznUpYGWf0XESx9VLJKG79ggkOo6C2BsIuQBLEgeLqFUBlwj_l_7qCUOHdlu1zTMBer8ocjUSCqxlEkd04_EC5eB_YZuBSy1PxwiwFy_lmxEnHO6yJQKDpMLjDMhiwILqPuG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuTtdd8VbfFn4L5Zu7l0caIDCVDhMn6bHcfUzjHHwabQr_eN_pgujUjZN-1gjWYNEYUD4ATSsby5XzHhSu5w3dQzRshAU0uYESBvYBWXa5W5qpICSHh6JbucwThW6d0hLluHIDoOucqtimC2NKsJ18glAgrHlJDEeji4KUpSOqvPAi2jT27RC5BlWxJsNfy4Hz2crH6MrD65iDVpxuIAPOexZcDOkZQwujO81zSvdSgMaBiPS4c5OR0oIyrbRuYx92GMkvb3YlXaSCpNpydbWP_PYX3uztAAqs1PkzV_mfWydN4ii1jg6nR-HwlTSLMQWTv1376rONyWqnxSwyIZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf9-Y3yPU194HuQmUHhRVLCn6vzx1UqkOEqoSFcRflRzNzdgjQf0Ff5TEuXYqtfKbqbGmBB4f_TT_wRYKbHBspWB9RItlHkS8ucOi6rXXNQJRz5KQKWNVVM7ocwxqYmz2iVUDudzWNPL0L5azaywjziwxFUTKRwPeZmjEroZRf_i44B2ED2DSfOv6SL8SG0aUqDVCvbplOYER4i9T7EzCCeTdmB7Nh3Q8A9Eya0f3bf-BpBysJ8pel077PNynLXd1JvrByXtEqel4nFQanQpyA3B9fugr_034Fw-tPdO4gJ-9ZqJW9bohjSt_ei34liAwkmf8d6vkmtRXosjHeK1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/szugW7vrkh6sONHwNEulBrMufNLs6iVafkqdnDyISZxXNOJGA43JkcAA0rSv1VOO_TJu5NRa_R3J2A34oYeQH3w01Z_x1mkb4nadHLz4xTaRux722v7Q4GzVoWTqntArvz1Ge-Yey2dHHCsUfHXOwhAglpz-ZH8ooDNI7NjuNeWq30cUpX_uzYplwkkmYWvQkuEnr0cYY-hWq1Cdqq3A-3jGuFhOxrWh3L9hpqz0S7Bh7q_mx4csB4ZAyoAHZrkyt_o9al39UlV_DC75Q3nk-YHojj1hHjw2PKlAN4-1oKkeoFkSyA3Gisg9WbypfXr3V7K_IvePLw_avLTt062CgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jULe2OSEviTKcC_aPxJ-OAfrswD6eH-I5uL5p_bSCFnORZkD-cba1OMosu7m-RJxOYfjuHKGUBeyEYau490eBalLUS267d2VhHTIntvYWq8gsYgrBrOuqTrdduNdMQE6hDvybapUaeVC5oBQyfsHyOwrEDH7P9iN-2OqDVzYrxFj6ArmrvK8sAJp5TleXpzhdjJRzr7TANOs9tmfDLszqOjawqQC4kZOanEtkv_w9EQQj5JRmzF313TjFuWLTX79D6bBPtv2dj8H5S5xgc-c8A1wDlyiHa-I3UGQUq9g_JMWfxhawxkjVIeMy97cImEOsvTJ2v7bmP86YwY5izF8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=m_ys_KMe0PfgOZYg1kHpEkGx6dzP6FY-Vwplr4Wwvv4HeiqyfIU90USFLloFTE9AFmdW7ELVZFBNhZXh3B6Ju1MnhNEZPrZ-8kltJ-BMYsVqg-uJ5d9tOx4EtjSAF-vpCrBXQW0ykfI7uCT0Hgg1CpbCH3roh7QC1yPyFo3llFCBaDkH2LMX1nYOB-5NClhTYacGQL2LwsACOIP8nW9c2e59h5qKM4l7RseITy0V_zVlCX9_MkHBP1uotq2iWV1jCUdea47IRrK28pkp5HXWRPjYyAQZYE_ZflsEDFF1Z_WJVYC4OoSJaH0A7LM_DHlxWvwmSsga0K4fhaKaVZbBbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=m_ys_KMe0PfgOZYg1kHpEkGx6dzP6FY-Vwplr4Wwvv4HeiqyfIU90USFLloFTE9AFmdW7ELVZFBNhZXh3B6Ju1MnhNEZPrZ-8kltJ-BMYsVqg-uJ5d9tOx4EtjSAF-vpCrBXQW0ykfI7uCT0Hgg1CpbCH3roh7QC1yPyFo3llFCBaDkH2LMX1nYOB-5NClhTYacGQL2LwsACOIP8nW9c2e59h5qKM4l7RseITy0V_zVlCX9_MkHBP1uotq2iWV1jCUdea47IRrK28pkp5HXWRPjYyAQZYE_ZflsEDFF1Z_WJVYC4OoSJaH0A7LM_DHlxWvwmSsga0K4fhaKaVZbBbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDy72fSUf2iYt0zvw5dEQ72kevx3l16rlk77P14UhlQbrHnIKOtqO3XmU8xsGgkTL_N2S0wIjoToRRZiibB_nFxL9LuX7KHzVlwOPMNOvpdjq5affkuskFPltvedCbyxyTlFKzviuPAlxnEqSxpQpsx1OE2yBPJ987JXsCyHJW33W5TjMMG5MX0Z5ZnCqK6oNXTRlbdL4AGASDGKvZdwtbhpNEF7TBeWp_mS9O2fXS-2ZIm0bc2_-nfuPLGGwyzX4HnKT5DRTO_XToHClV5g7_edDo_38RvJmbHfYm1gVEeT-yp9JasE6I166ZvRamzkrV5goIOqfCjWoRYHxFAOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
