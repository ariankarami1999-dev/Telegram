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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 972K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-126008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
منابع عراقی: نیروهای امنیتی در عراق هشدار جدیدی در نزدیکی منطقه سبز و فرودگاه بغداد اعلام کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/alonews/126008" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: رقبای نتانیاهو در عرصه سیاسی اسرائیل از این وضعیت سوءاستفاده خواهند کرد.
🔴
از سوی دیگر، نتانیاهو نمی‌تواند چند ماه پیش از انتخابات به چنین وضعیتی برسد، زیرا این می‌تواند فاجعه‌ای سیاسی برای او باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33 · <a href="https://t.me/alonews/126007" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ارتش اسرائیل می‌گوید به عملیات خود در سراسر لبنان ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/126006" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کانال ۱۲ عبری: به دنبال وضعیت امنیتی، کنست (مجلس اسرائیل) چندین جلسه که برای فردا برنامه‌ریزی شده بود را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/126005" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: در حال حاضر نتوانستیم با نتانیاهو تماس بر قرار کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/126004" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: «اوضاع بسیار خوب پیش می‌رود.»
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/126003" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: «اوضاع بسیار خوب پیش می‌رود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/126002" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اسرائیل: آماده شلیک موشک‌های بیشتری از ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/126001" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
حریم هوایی سوریه نیز بسته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/126000" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تماس های تلفنی عراقچی با وزرای خارجه فرانسه و قطر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125999" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ما برای احتمال ادامه حملات آتش به سمت خود آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/125998" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل در یک کنفرانس مطبوعاتی ادعا کرد که رئیس ستاد ارتش، ایال زامیر، در حال ارزیابی وضعیت است و «طرح‌هایی را برای آینده تصویب می‌کند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/125997" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری /  سخنگوی ارتش اسرائیل: ایران اشتباه بزرگی مرتکب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/125996" target="_blank">📅 00:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تابناک: پدافند در بخش محدودی از غرب تهران فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/125995" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صداها در تبریز مربوط به پدافنده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125994" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ارتش اسرائیل به زودی بیانیه ای صادر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/125993" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
صداها در تبریز مربوط به پدافنده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125992" target="_blank">📅 23:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ به باراک راوید: هر کدام از آنها خوش گذراندند. اسرائیل حمله خود را انجام داد و ایران هم حمله خود را. ما به حمله دیگری نیاز نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125991" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125990">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
العربی الجدید: رئیس سازمان هوانوردی غیرنظامی عراق سقوط یک هواپیمای مسافربری در عراق را تکذیب می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125990" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125989">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ:
منم با اینا مشکل دارم ولی بحث بحثه وطنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/125989" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ : «در حمله موشکی هیچ‌کس آسیب ندید. اگر نتانیاهو پاسخ بدهد، این روند ادامه پیدا خواهد کرد و ادامه خواهد داشت.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/125988" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تماس‌های تلفنی عراقچی با وزرای خارجه انگلیس و ترکیه و فرمانده ارتش پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125987" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e3d13213.mp4?token=Jzq_MCig2RpaQ2fN-LdEax1Ka5ftI3BFvFZKVqHU70QSObWDbs0oS86d_pXUT_w9eqeKwmmURKLIpnTtNLbZvGf8oAqyjVQaY2H21s9htbc5lU4_Ft1QTR9nJsHpig89oKILGYHPIicrNn2mDe0DQxWuWoeTweKlv_iUP4UQEX18QB16ZTR2-ntI_El5y2X23ewC5eg-pgLK8WQEe3jHk8SGpKL5NORYGHWA0zNwfkOzNBuv98ub7EL5grj4wTaZWCTk6wg3y0tSgmH01vZUxm7iiDGd_NpHm7lC5QvYSSF1U16PYwwTE0qInUQ0Lwl1EKuEEihi5qFn-zd30IexmoUXIS0Ey23MAcIMV02D9VMoZES6zhKB-pGLqN2_2th5jQFQC0bp25eqS7zw6mXAzhm6jXLOOqIakO19D5SG3lE1ph0ghr0_TcQR1E08KBB3Mr23rCPfO2Aak4NfDm768olboIiYZ4Zx9qJ4md-iym8NuxPlC5IAHXQfs9vrkiMxchYa4ArDzPipZmmXqU_KxV--v3UbJd2j10CK_RohabiLi98XTuihzSBOB0JWEXMLf6HFoiNHsxaS3JmzbNyIHmxaDg58h367fKy2H4NrzLucPdA-aJU2SoFd21f6S1kew2g61q-GC3y9lLBeHlhS6KCFRMQzCxO3dffvDXCqfeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e3d13213.mp4?token=Jzq_MCig2RpaQ2fN-LdEax1Ka5ftI3BFvFZKVqHU70QSObWDbs0oS86d_pXUT_w9eqeKwmmURKLIpnTtNLbZvGf8oAqyjVQaY2H21s9htbc5lU4_Ft1QTR9nJsHpig89oKILGYHPIicrNn2mDe0DQxWuWoeTweKlv_iUP4UQEX18QB16ZTR2-ntI_El5y2X23ewC5eg-pgLK8WQEe3jHk8SGpKL5NORYGHWA0zNwfkOzNBuv98ub7EL5grj4wTaZWCTk6wg3y0tSgmH01vZUxm7iiDGd_NpHm7lC5QvYSSF1U16PYwwTE0qInUQ0Lwl1EKuEEihi5qFn-zd30IexmoUXIS0Ey23MAcIMV02D9VMoZES6zhKB-pGLqN2_2th5jQFQC0bp25eqS7zw6mXAzhm6jXLOOqIakO19D5SG3lE1ph0ghr0_TcQR1E08KBB3Mr23rCPfO2Aak4NfDm768olboIiYZ4Zx9qJ4md-iym8NuxPlC5IAHXQfs9vrkiMxchYa4ArDzPipZmmXqU_KxV--v3UbJd2j10CK_RohabiLi98XTuihzSBOB0JWEXMLf6HFoiNHsxaS3JmzbNyIHmxaDg58h367fKy2H4NrzLucPdA-aJU2SoFd21f6S1kew2g61q-GC3y9lLBeHlhS6KCFRMQzCxO3dffvDXCqfeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیانیه قرارگاه خاتم الانبیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/125986" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ بزودی:
و من نصر الی من عندالله عزیز الحکیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/125985" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/or5DyRxsSRLEXsgcAfz7Ihjbki3gf46247MTX4JMEIWOukXuxfe8Dyr_Afc8xtSsxEUlPykkAg7PPQbLjlAPPC0AZp8Phsksv6GTengQcaIVGObEcm6DJ9IO1OygvCYdiGW_T4-tf6eKX-G_afpSmLwAWTB5MZvAGgKZJ2YileeLGMkndkvU1b-BAWkyvFMok9LfCPVvk-xVpyYWG3KksVyfrC1Zx9eAlrsxIUTTlQggIM9NIjoaeEFUK_keXTaA0XvFFv4Rmx9k-joXdWLlCD0tkNXyc_lq8DiSjHIdE5Hsvbc7dZLZtbqHQutrGaHovGfhKCrS8wu_buW5VYfFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس هم تایید کرد، ترامپ زنگ زده به نتانیاهو که به حملات ایران پاسخ نده!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/125984" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f9652347.mp4?token=rWnCHnKuT5vY7G97BZ9rdJRDm4oSnx9qx54_Gga7vjHn5tzwcBkWc2dWjIvdAeu2di2ulUqTDjyqZIyVkemaYOYRY7OOk9S5IuP4S8WhNiU0s1W1i4zPstFHui_U2R5V5E9EUFuU-EJ9V-MlNiLhIv6tbVWcjr4ftKJSAuWiChWcu1jpPZIsjHIcS_xvq7ISQR_PUHfED9Em9msI7TXcsVk3ZTcaoOFI9vbN1S1mOR5LvRgby_RjSgULz--llEZVznCgiTWcr5t71qDg35KYq8aoKSEF18iIaSerrwCY5-xm2qODCcV4h7scBe-ZYDqin3qJ95GorO0Tiytt_On8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f9652347.mp4?token=rWnCHnKuT5vY7G97BZ9rdJRDm4oSnx9qx54_Gga7vjHn5tzwcBkWc2dWjIvdAeu2di2ulUqTDjyqZIyVkemaYOYRY7OOk9S5IuP4S8WhNiU0s1W1i4zPstFHui_U2R5V5E9EUFuU-EJ9V-MlNiLhIv6tbVWcjr4ftKJSAuWiChWcu1jpPZIsjHIcS_xvq7ISQR_PUHfED9Em9msI7TXcsVk3ZTcaoOFI9vbN1S1mOR5LvRgby_RjSgULz--llEZVznCgiTWcr5t71qDg35KYq8aoKSEF18iIaSerrwCY5-xm2qODCcV4h7scBe-ZYDqin3qJ95GorO0Tiytt_On8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر واضحی از لحظه اصابت موشک ایران به هدف خود در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/125983" target="_blank">📅 23:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ به خبرگزاری کان: فکر می‌کنم اسرائیل به اندازه کافی واکنش نشان داده است. دیگر نیازی به واکنش بیشتر نیست.
🔴
ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/125982" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125981">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نزدیکان ارشد ترامپ به اکسیوس:  آمریکا بخشی از این تحولات نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/125981" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125980">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رتش اسرائیل : وضعیت هشدار و آماده‌باش به پایان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/125980" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125979">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d39dd6.mp4?token=AFjsQ5lJbCjb3EJDAFFrvrH7GKzKRwuxsTUvW8JPekPdMOpa2J4RXY5pUu7nHKznsGJiP5afTqFqnTQFbzaOhyzUk2L2Mk_reCiUihxRxYCgVMxDzZTPuq4RsEldQVhGx5Z2Tqq1N8qoN5wuv393kAC0GkZPKqW9njtnZP8kvpMrNqoVGhr-v4hnOjH70n6AJ-8VwSCJ9QrISafJO1Cn2GtSMajlhMG6eUK_50OmHbAu1kB_cE7Xjr6S1m3dpNh89M4ZGqV52p3VdfmiSfE9KswnGxDhKYI2oNvauHAYVU5UR3BQJK30O1jauMVmbIEnVOBoWh8RcCQ6hR4VCVrGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d39dd6.mp4?token=AFjsQ5lJbCjb3EJDAFFrvrH7GKzKRwuxsTUvW8JPekPdMOpa2J4RXY5pUu7nHKznsGJiP5afTqFqnTQFbzaOhyzUk2L2Mk_reCiUihxRxYCgVMxDzZTPuq4RsEldQVhGx5Z2Tqq1N8qoN5wuv393kAC0GkZPKqW9njtnZP8kvpMrNqoVGhr-v4hnOjH70n6AJ-8VwSCJ9QrISafJO1Cn2GtSMajlhMG6eUK_50OmHbAu1kB_cE7Xjr6S1m3dpNh89M4ZGqV52p3VdfmiSfE9KswnGxDhKYI2oNvauHAYVU5UR3BQJK30O1jauMVmbIEnVOBoWh8RcCQ6hR4VCVrGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مگر می‌شود پدری که جوانش را با گلوله از دست داده ساکت بماند؟
🔴
روز ۲۰ دی در کهریزک، مردی میان صدای گریه و خشم فریاد زد: بر باعث و بانی‌اش لعنت ، ۳۰ سال بچه‌ات را بزرگ کنی، بعد بیایند با یک گلوله بکشندش؟
🔴
وقتی به او گفتند ساکت باش، پاسخ داد: آب از سر ما گذشته
🤔
عرزشی حرام زاده ، این صدای یک نفر نیست؛ صدای هزاران خانواده‌ای است که عزیزانشان را گرفتید و هنوز دنبال عدالت‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/125979" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125978">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ : «امیدوارم اسرائیل در پاسخ حمله نکند. اگر نتانیاهو دستور حمله بدهد، با یک حمله متقابل ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/125978" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125977">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فعالیت جنگنده‌های ارتش بر فراز آسمان تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/125977" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125976">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فووری/ ترامپ به کانال۱۲: به نتانیاهو خواهم گفت به ایران حمله نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/125976" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع ارشد ایرانی:
تمام پایگاه‌های آمریکایی در منطقه در صورت انجام حملات از سوی اسرائیل، اهداف مشروعی برای تهران خواهند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125975" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125974">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کارشناس صدا و سیما: خونه نتانیاهو رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125974" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125973">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فاکس نیوز: مقامات ایرانی معتقدند که ترامپ تمایلی به ورود به یک درگیری گسترده‌تر ندارد و مصمم است جنگ را تقریباً به هر قیمتی به پایان برساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/125973" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125972">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: حمله ایران قطعاً به مذاکرات کمکی نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125972" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125971">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ ادعا کرد که از حملات امروز اسرائیل راضی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/125971" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125970">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پروازها در غرب کشور متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/125970" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125969">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2AR5ZNAdbDvAyatjmI3Pd1_iqBcX4xqssW7wVPtAJFAi6z0eGVEEwNd46zxlisb1MKWbAojapkw_tQ_xRo59U43gME532rpkZ6LOLDHMucFucgb-CY7ZeB_oan-V9Tf6o8kny-gJcq6EXkedKHz0rzHNaq8t1D7JRhtsfV4_nu7zgGreLKgkgWhSL04xeWx7aptpU33XOxZuX470ibuuOjMVBKs89oZjFUjwvGThKf6TORCLCi7uFB7t-L9yfF4GQaaOpZHJ8Q00mGXVIOMerGn-P6pkhTLPOz_XDAlDjYcwEjNF__fmC0gC6V6dL-4E2os08I5x7P3KyhYwa43FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / عراق نوتام اعلام کرد و حریم هواییش رو بست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/125969" target="_blank">📅 23:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / سی‌ان‌ان به نقل از دو منبع اسرائیلی: ما به پرتاب موشک‌های بالستیک ایران با قدرت پاسخ خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/125968" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXIuRghUZYK0U-IvI5I6lK8q4in7kTze55jiXa595ipazos6gIfWNDrh5q8c4KNymwB3I5C8YbI8ySQPyHa2iMm1WT4HTMOHrJyrNrvWZ_pCZIcOFjMMTsDHvH-8OvrvFIdt1VjF6dS7L2EoWVW7siyQQHvMMz3D9CYaMJHrcmB3YxaKeo8T2Gs3h5zjr5I8ybQry75OZeOBrydU-Hh9d5wAOGpeJS83arnnHuuRe2ciFHiwVnkyn-KddBGWcmfqvYbBy3ZYp8lm_liw80PQct_pA1b8rfAojULeyH53BGz91DxmHpvJJiFmCR8VmdL0vi0XRtp0GCSiR-YEDNDWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/125967" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125966">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یک منبع ایرانی به رویترز: اگر اسرائیل به حملات موشکی ایران پاسخ دهد، ما نیز قطعاً پاسخ خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/125966" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز: قرار بود بگویم که این توافق دوشنبه، سه‌شنبه یا چهارشنبه امضا می‌شود و حالا این اتفاق دارد می‌افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125965" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125964">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOJSvAVuQL8kUULC5qG_Zm6gxvp26R8RPV4NkwOxQKLK1P3YGVb1ncv6W91TL-_XwcU_8hmCTUV7IpqiWakgeC6x2vjLuMgPR062_UswipZgJjtD9dC2N_ffY11YbupyQgmmvWL2uCwZaYWty5ruKhvDPzHuzwmRW0WCtghAjAmJ67cF8qxXiszUGdPKxtV5Fv2WzHceTXu7viiRMZ_DXomf27tN4hm_GryKpjokH9DDxyT9eeibV9ixE5_lwH7vuxhiNn_QGB7ccwqCniar9cq-UZ1dSe85XCYEV7y-bX6cZgY4yzrnzXWIqHkNL_yZPRcaa0ImS56P3nHf1mT4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانفیگ فروشا در راه تلگرام
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125964" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / ترامپ: نیروهای نظامی آمریکا در حالت آماده‌باش هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/125963" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ارتش اسرائیل : در مجموع 12 موشک بالستیک شلیک شد که تمام آن رهگیری یا به منطقه‌ای باز اصابت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125962" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اسرائیل هیوم: تمام موشک‌ها رهگیری شد و یک موشک به جنگل اصابت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/125961" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: به توافق نزدیک شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/125960" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز: به میز مذاکره برگردید و توافق کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/125959" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=K-qORzQ84_QMu7KOg4yJdm1T1rooxWDZDrw3I5ZVaG5Ijzak1Ybu9pzr23ihp1e3LTBB2lPb9utmwgsSBDwqdtW3jY8iqsRsFc5o-Rc1RT6k1Rmnf4kFBVttrOiO2CM5jJi11RHcj_Cy5CN4B-7PUNid_Y-vqiIZxZW8cd2P8DoYEu-lQErPKG46jk7JN1XMdY0qbBp5XjX1W3v3Rkh7MKkY1FjRHv8Se-Q2UDXv2Ac6yJWqio33labS2Vhv5wg0C2PXveCN-DqiBFZMnoQwyWKGCXh95FgfNS6HhzxSU-I6jq6e2iZs1Ut8KDVuLTGeMev7CBb-E7e8s3_kaHgRvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=K-qORzQ84_QMu7KOg4yJdm1T1rooxWDZDrw3I5ZVaG5Ijzak1Ybu9pzr23ihp1e3LTBB2lPb9utmwgsSBDwqdtW3jY8iqsRsFc5o-Rc1RT6k1Rmnf4kFBVttrOiO2CM5jJi11RHcj_Cy5CN4B-7PUNid_Y-vqiIZxZW8cd2P8DoYEu-lQErPKG46jk7JN1XMdY0qbBp5XjX1W3v3Rkh7MKkY1FjRHv8Se-Q2UDXv2Ac6yJWqio33labS2Vhv5wg0C2PXveCN-DqiBFZMnoQwyWKGCXh95FgfNS6HhzxSU-I6jq6e2iZs1Ut8KDVuLTGeMev7CBb-E7e8s3_kaHgRvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت موشک و در پی آن آتش سوزی شدید در نزدیکی یک زمین فوتبال در کفار ساجور اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125958" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd3c2476.mp4?token=O5zQ6GhyPvCgLJJceU8QZXKhCdugm3sscjkhb7MSJu-l9fv93KhU9HWFuhI2cz-oBOgG9kjuXYbQ8qBmJiPe8VQG9I79ahF5so_YqBIFUC9tfDD9TXhxw6bo3sKfuIJ_OrSyWiDTTxO5DBQl90tzyXInKax7bnTeEgTpp7Chowvf3zRKsSfsX2veu00T-3TYBkV1jSOu-4e0pGslgg2aE2-bx2AzShs9SiFJjTuKzVMIMfMG6hCugBw3pKMP5-5QMME5Oigfv1hmao0yJIgTWnL55WADQ9NRg81ufIfTnwJqnXKGtEMGGekOe52_Da-OJ5E502STYF-27n4Onxa3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd3c2476.mp4?token=O5zQ6GhyPvCgLJJceU8QZXKhCdugm3sscjkhb7MSJu-l9fv93KhU9HWFuhI2cz-oBOgG9kjuXYbQ8qBmJiPe8VQG9I79ahF5so_YqBIFUC9tfDD9TXhxw6bo3sKfuIJ_OrSyWiDTTxO5DBQl90tzyXInKax7bnTeEgTpp7Chowvf3zRKsSfsX2veu00T-3TYBkV1jSOu-4e0pGslgg2aE2-bx2AzShs9SiFJjTuKzVMIMfMG6hCugBw3pKMP5-5QMME5Oigfv1hmao0yJIgTWnL55WADQ9NRg81ufIfTnwJqnXKGtEMGGekOe52_Da-OJ5E502STYF-27n4Onxa3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت موشک و در پی آن آتش سوزی شدید در نزدیکی یک زمین فوتبال در کفار ساجور اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125957" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/ترامپ به فاکس نیوز: آنچه به ایران توصیه می‌کنم: موشک‌هایتان را پرتاب کرده‌اید، همین کافی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/125956" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حزب‌الله: آمریکا وارد ماجرا شه پایگاه‌هاش تو عراق و سایر کشورای منطقه رو می‌زنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125955" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سپاه : این فقط یک اخطار بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/125953" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
جبهه داخلی  اسرائیل اعلام کرد که رویداد در شمال کشور به پایان رسیده است. می‌توانید از پناهگاه‌ها خارج شوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/125952" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83918f4ab.mp4?token=VOGpqzOZnHmbrdXQiqjC3x9bTSHyp0bD6Lu3QDP4C6yPEpdcDty5UPofL_ygVvU74Rv4aJqKHRckidaK5ga1Xf_qJV7uoIaypxgRvgUy9pyAS19zNQWg35Mob_bVeb0wm-gbjknGfJWNEDZCYPv8nBqfnNwJLsZSnikcDYch__5ms23nLvImkZNdzGaS8qSKH8_hhKFK7uSEJ-SAjFUkIm4g3cUZoy26vhkKQgawEUDRYsfqFljEadU7sV6w0aofahKdXCI0Jj7QduUVMG-MiH0LQJATpgXDI5gDN3w1ieuNj3S7q6g_qzaBmK9SzQf8MFthxLmRs0fMemLsSFgfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83918f4ab.mp4?token=VOGpqzOZnHmbrdXQiqjC3x9bTSHyp0bD6Lu3QDP4C6yPEpdcDty5UPofL_ygVvU74Rv4aJqKHRckidaK5ga1Xf_qJV7uoIaypxgRvgUy9pyAS19zNQWg35Mob_bVeb0wm-gbjknGfJWNEDZCYPv8nBqfnNwJLsZSnikcDYch__5ms23nLvImkZNdzGaS8qSKH8_hhKFK7uSEJ-SAjFUkIm4g3cUZoy26vhkKQgawEUDRYsfqFljEadU7sV6w0aofahKdXCI0Jj7QduUVMG-MiH0LQJATpgXDI5gDN3w1ieuNj3S7q6g_qzaBmK9SzQf8MFthxLmRs0fMemLsSFgfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت سهمگین موشک به شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/125951" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMCVCZKCjTHRqWPcJ19WZ532VBJqrEln3If3OK-JY--Fx9GUuNvB6SQWi73Rhzf0tdhXMa4t85_6cnnh-yf_haKwHP6QqAwM93SQnfLtbfT_0fDp0wCohz7yUOms3UEnj7jhLXYmgCuTF-eTO5nrc7UWLnJD0kvvQfqnhUaMdJ4i6PpRL53k4-bBE7bJYPqWLSryfKv3BAk0EXmIa9F8eR3Ioh55pbhZ7DQIYenszVebUO14WMoRASP4A85N1GMV9s9Swy5Bv8FT0Xnx5d4dMcjNwrrMdgSq_f6jlsiucrNLddK6VeSddwRhb-K9fKVrQPa6a4hNPTNyoBt9t6PQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید مجید موسوی: الوعده وفا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/125950" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سپاه : پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/125949" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دو اصابت موشک‌های بالستیک ایران در شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/125948" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / گزارش‌ها فعالیت پدافند هوایی در کرماشاه و تبریز!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/125947" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125946">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری/هشدار ها در اردن به صدا درامد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/125946" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125945">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/هشدار ها در اردن به صدا درامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/125945" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125944">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e7f5f849.mp4?token=IyEryGXw9Inv8ZuCSLCCquroNfNpqWi2hmuQNEHRX4ps-xmycuzymp_DXaiZ2-akCIu42F3eWyrt3ltqhQ26Lqr7EURoOWgbLClA52cdBRQystWlrnpVEBxsI0kY6WvF5MzmNvufQb6P4xuKXsGrxiAkY8yC-0-gXMcIRSZSdYUKAmjowSNhTqLcMYEontbruJ_JZG2GM4SvVb-PTnuivFr5RQTN53VNH1v6eyunJn1r2m-A05b9-yZ0gZKjMUqtw1SnKgakCUdj2N6RFpUJZwsiMFiLqtp5cN1tOyIAXuXqUKgg66NmIMPjb4SRn3SWArQ1-Oi1c3ZSzNDxE42MbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e7f5f849.mp4?token=IyEryGXw9Inv8ZuCSLCCquroNfNpqWi2hmuQNEHRX4ps-xmycuzymp_DXaiZ2-akCIu42F3eWyrt3ltqhQ26Lqr7EURoOWgbLClA52cdBRQystWlrnpVEBxsI0kY6WvF5MzmNvufQb6P4xuKXsGrxiAkY8yC-0-gXMcIRSZSdYUKAmjowSNhTqLcMYEontbruJ_JZG2GM4SvVb-PTnuivFr5RQTN53VNH1v6eyunJn1r2m-A05b9-yZ0gZKjMUqtw1SnKgakCUdj2N6RFpUJZwsiMFiLqtp5cN1tOyIAXuXqUKgg66NmIMPjb4SRn3SWArQ1-Oi1c3ZSzNDxE42MbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرتاب موشک بالستیک از کرج، ایران
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/125944" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125943">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ارتش اسرائیل می‌گوید تاکنون تمام موشک‌های بالستیک ایرانی که امشب به سمت اسرائیل شلیک شده‌اند را رهگیری کرده است.
🔴
ارتش اسرائیل می‌گوید پدافند هوایی اکنون در تلاش است تا آخرین موشک شلیک شده از ایران را سرنگون کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/125943" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125942">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
اینترنت درحال قطع شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/125942" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125941">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: بزنید بدتر میزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/125941" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125940">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/والا نیوز: اسرائیل در حال درخواست چراغ سبز از آمریکا برای هدف قرار دادن تأسیسات انرژی ایران است!!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/125940" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125939">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فووری/موج پنجم حملات هم اکنون، اژیر ها دوباره فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/125939" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125938">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/والا نیوز: اسرائیل در حال درخواست چراغ سبز از آمریکا برای هدف قرار دادن تأسیسات انرژی ایران است!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/125938" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125937">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نت بلاکس: ترافیک اینترنت در ایران ۲۵درصد کاهش یافته و اختلال زیادی داره
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/125937" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125936">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ede2c31.mp4?token=alFpCk8S6ZFmkVt7jiwdC5_Pq_3_ybvV-GWftFEyXmC3cLlaJ7kjtMHzgGebOfZYQ4Ombbf0ew5V_EVXWDkb2i2RPkMbCyUIk0XiMs54k0j6wxS6vb8EQYvLrA31F_-NxngDxorZEJ8GneqUrF0XOgoUJZgSLQMEXAXmEe-lhoITlid0Ln83HkLzdcSdaJ806TDYQoItF-qttlOmv2SJN0tt_Avmaoii0D-smDM1yDNkXWLzdyCmhlWDXuj51FbhAOGYlFEFp9Oo67ClC7flBL9bzLvQkBp-jdUXEKNqAA8I0dASLIhO25oTyekMtxaHaCI1S6mdgchTEoeltV8_FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ede2c31.mp4?token=alFpCk8S6ZFmkVt7jiwdC5_Pq_3_ybvV-GWftFEyXmC3cLlaJ7kjtMHzgGebOfZYQ4Ombbf0ew5V_EVXWDkb2i2RPkMbCyUIk0XiMs54k0j6wxS6vb8EQYvLrA31F_-NxngDxorZEJ8GneqUrF0XOgoUJZgSLQMEXAXmEe-lhoITlid0Ln83HkLzdcSdaJ806TDYQoItF-qttlOmv2SJN0tt_Avmaoii0D-smDM1yDNkXWLzdyCmhlWDXuj51FbhAOGYlFEFp9Oo67ClC7flBL9bzLvQkBp-jdUXEKNqAA8I0dASLIhO25oTyekMtxaHaCI1S6mdgchTEoeltV8_FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از موشک بالستیک ایران در آسمان اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125936" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125935">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نت بلاکس: ترافیک اینترنت در ایران ۲۵درصد کاهش یافته و اختلال زیادی داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/125935" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
‌
به گزارش آکسیوس ترامپ جلسه اضطراری در مورد ایران و اسرائیل برگزار می‌کند
🔴
یک مقام اسرائیلی به من گفت که اسرائیل قصد دارد به حمله ایران تلافی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/125934" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
العربی الجدید: صدای انفجارها در جلیل و آژیرهای خطر بار دیگر به صدا درآمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/125933" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125932">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اگر اسرائیل پاسخ بده اینترنت‌ها قطع میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125932" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125931">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / شاخص پمپ بزنین رفت بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125931" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125930">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
اکسیوس : ترامپ در جریان بالا گرفتن تنش‌ها بین اسرائیل و ایران قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125930" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125929">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ادعا شده در موج چهارم 10 تیر موشک بالستیک شلیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125929" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125928">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/تعداد زیادی هواپیمای سوخت رسان آمریکایی از فرودگاه های اسرائیل به پرواز درآمدند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/125928" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125927">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آکسیوس: ترامپ در جریان تشدید تنش بین اسرائیل و ایران قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/125927" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125926">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حملات مشترک با حزب الله آغاز شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/125926" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125925">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/تعداد زیادی هواپیمای سوخت رسان آمریکایی از فرودگاه های اسرائیل به پرواز درآمدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125925" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125924">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZEHDDjOb7csJBYVFnVUyfAqir6jatpKA3AKXcWPOzSawbDVHt7jwEQywhPHKTTjucOJs6MmewCdjSf75yxOOM3Ps_zQdEBgQJ8MurK7kusIlGiKyzE1lzzVqUkuo34AnLofOZv5o-xh_cKT6rRL142vrpRK7sFug86UojeplXK0c0mQCp4fvqi2rQ33eJOnRx4XWqxXhU47lZsoxSnYdE2JeGIlW0V8me5c4e7SVWWkYnEUE5q0voJ67yYX4v8USm8ToXjvIvcKHAyKafjs49K7S_QfUq5Uk0js0PxuXVdhD06gUtmX_Dz1177WYSxXGlAefleyQ_MpA5SR2KPiBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس
🔴
Damovpn
امکان اتصال به
0️⃣
1️⃣
لوکیشن
➿
➿
➿
➿
➿
➿
➿
➿
➿
➿
➿
🔒
آیپی ثابت
🎮
سرور گیمینگ
🚀
سرعت بالا
⏰
پشتیبانی 24 ساعته
➿
➿
➿
➿
➿
➿
➿
➿
➿
➿
➿
🎁
10هزارتومان هدیه ورود به ربات
🤖
BOT
🖱️
|
@Damovpnbot
|
✈️
CHANNEL
🖱️
|
@vpndamo
|</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125924" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125923">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6Nl6uq5zuIH7uXDX-9f-wVEtJplvPcs__mTvEG7dEjgsm3-Biwnw7pNTUOxwJoPyRrRGo7ajUNi-36kdXw-CRaD-0P-AFOtayZlYoLr4NqOwrLYx4HPRIAcQ74QAc1JcA2dB-7D8lYPklDMWmoCs0lyuWXICWizK7ekisthXpcBdgPIG9nFR5YX9RnfVhVIavyJdJI70faYoQEXdlpLq1KAVEb99xZnJ8NxiiAr20nYMM5X9XkgPO1oH2EIdfGb7zhqLcSPaBD2q4NsL5lD8cgvcP-ZGcfvMDgJIvKqENzUMccf5cU8wZkjrSdtZgGeeYURFi11dpV4PCsdjj3WDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موج چهارم به سوی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/125923" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125922">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری /  یک مقام ارشد اسرائیلی به i24NEWS گفت: پاسخ در راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125922" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125921">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پرتاب بیش از هشت موشک از اصفهان و بیش از سه موشک از تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125921" target="_blank">📅 22:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125920">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / موج سوم حمله موشکی آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/125920" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125919">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F95FDFvb2aAQmmlnDZD69g7XlXQCzC1PNrYkAXSx8Sh7GCmNmsU2WiEVQ-W4O3IP1EH1nigKAfMLhTFVWTkcBEU0vFz_HM5Px6ys3m0arE8Bt9JSgPYV4tRLj3MbQzK5EepQSnnfxEC2iwy1pqXq_Ok9SixZdGKqAmh7P4zh-37UT6tbX6WTa1DwBDy_vRJs0reLOcKUM55q-7If4FOnd0Mp8vBJ41agsq1xAuqcv8vSRkmJV7HsAJb8xdFZXMxbknCZ2fPpWYKX4n2lYeqCgx2wH8SYj4FNRNyhtMJ-nMQ8oOcMiX0MR9fDPqlGwB8ZgpXzJavqm95QReAZF0IMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست
عباس عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125919" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125918">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فرودگاه بن‌گوریون در اسرائیل تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125918" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125916">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گزارش شلیک از تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/125916" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125915">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lyfjZtcyVvUcqinoPzsyuV5s2EtKwfbLLF7SFSVaXD8Z2EAv_oquieezwVTH5msLXNX8zSG8aWElw96b_2J69LbI5TmtO9t2Cjv5GuRHBfocC2ufpLviambYhv_t9v84BATBxQ7cDGDD7Bi2J_dL7E0tAR9Ej8TcWwXY9k8fOoauT4YDgyuC7uGgHpsKa1QWj3BPKq9pWssxNSHoQzM1v3sJpostKKsPs-r1VUN-WWKdJrc4rJPZPP72hJLrXrRO7nQPvf012By5wy1sVZiJZO9x_urONH-t4cAYh2Nat-N6jHqZywMju8RyMUcCRmxviHLOAdGMKtj2VqsTj4Dbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل
:
امشب تهران باید بسوزد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/125915" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125914">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به کانال ۱۲: ایران می خواست معادله جدیدی از آتش محدود و اندازه گیری شده ایجاد کند ، اما ما اجازه نمی دهیم که این اتفاق بیفتد.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125914" target="_blank">📅 22:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125913">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوووووودی/موج دوم حملات آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/125913" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125911">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0b7022f1.mp4?token=ritcJLfkZxyfpD2vRmRM0exe-TdmLcH15Q7xGbPwqfW61VCJXlyUN8zzkXYJ3LjtTDhcOVYUABD_f8QebI92DEwTFgQ1rhqHbfnUnjx6s4_S98HcTjqIy5i2kjHh_3JseTCDVD80At1f9AERg8dP_k7OD8QrFriSkpgHMvf46ivLb4OjGggK3c0BCpzy9DRkmJaBFCWE-aaijN1zEyKy01lU-aKAmC6qpCWvY3j11Kjcgq3nZOgyzzS3eeKHvDSH5HY1OYaWT2Z3pkKah0qsnaNzNSasDNpVWxb2_8dFX4bWw0h4u3mlrSwqFvuFhbF2Z636CWOwNK-UOFcK5uxwvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0b7022f1.mp4?token=ritcJLfkZxyfpD2vRmRM0exe-TdmLcH15Q7xGbPwqfW61VCJXlyUN8zzkXYJ3LjtTDhcOVYUABD_f8QebI92DEwTFgQ1rhqHbfnUnjx6s4_S98HcTjqIy5i2kjHh_3JseTCDVD80At1f9AERg8dP_k7OD8QrFriSkpgHMvf46ivLb4OjGggK3c0BCpzy9DRkmJaBFCWE-aaijN1zEyKy01lU-aKAmC6qpCWvY3j11Kjcgq3nZOgyzzS3eeKHvDSH5HY1OYaWT2Z3pkKah0qsnaNzNSasDNpVWxb2_8dFX4bWw0h4u3mlrSwqFvuFhbF2Z636CWOwNK-UOFcK5uxwvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا ۱الی۲ موشک رهگیری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/125911" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125910">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/یک منبع سیاسی ارشد به کانال ۱۴ اسرائیل: «همانطور که قول دادیم، پاسخ خواهیم داد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125910" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125909">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQCdJAK9PnUPMmuwCw1oJJyhOhfzE3zT45gUlcQzBIxdEtJECPKEI3TTH7XetP2WagmvxvkcmWUtDZGwbK7GltcHNrlqt9eXDZ0dG81z8kw5WqTwoa_qm3ON_1VFCn3zaVjLfwlM3dxnnbzPUrX-4hyPczJVwJk9iE85Achf0zIskJm8Uws0TKBZPZ1aH2InyKS7Q6LzZPGapIN0KCAaWuTDCh7iH0yECKVEz2_3jhiol1bqoq22bohLwrlfqKv0xmUOvUF9sJJJtKSn4WWyjVTC8ZRFOGaksZxaa9kPuxFlp4ZhYzMjwN5mSuhNnYgvhdC4e9yeZ4I5VayxMYD7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125909" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125907">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / منبع اسرائیلی: واشنگتن متعهد شده است که به اسرائیل آزادی عمل در حمله به ایران را بدهد اگر با موشک هدف قرار گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/125907" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125906">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جبهه داخلی اسرائیل از شهرک‌نشینان خواست فوراً وارد پناهگاه‌ها شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/125906" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125905">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گویا ۳الی۴ موشک شلیک شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/125905" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
