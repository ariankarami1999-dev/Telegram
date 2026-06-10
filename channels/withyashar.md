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
<img src="https://cdn4.telesco.pe/file/FndBMVPKIZfOBegxH5jLnafjadZaEVRrJev0Lm217Ei9x8ZL97LI4ptgU5a2VOMcbyQ4FRNQPkr-0BnIpV129S33EcTtI76vipQah_C4IzEihKFqZOq_e_BSUZUzw5nyKHVHgs5W0l_JF2DQSThElX2jpwl5Hu_B5id_npnenOp5Hv_W63hQ9GzmaX8hjfhPZ6lwNJt71EuOS3pjsT2ubGVd9TbsWxb7RvDEfI8md1s1LBhJYJc5QA72yJKBzITEeYZuH8V9E3UkXAjENmYlTLVI6cdR67l5ELR4MwGI6wSd3FAxQeirKRkZg0waxFObmbJCBDskiVO9x_571XCX-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 316K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-14437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رسانه عراقی «صابرین‌نیوز» گزارش داد که کشتی‌های آمریکایی در نزدیکی تنگه هرمز هدف حملات موشکی و پهپادی نیروهای مسلح ایران قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/14437" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14436">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرنگار I24News  :  عوامل آمریکایی: مراکز فرماندهی و کنترل، انبارهای مهمات، رادارها و واحدهای پهپادی مورد حمله قرار گرفتند
@withyashar</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/withyashar/14436" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">المیادین: منطقه تنگه هرمز شاهد درگیری شدیده.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/14435" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کان عبری: اسرائیل نقشی در حملات امشب نداشته است
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/14434" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیشروی ناو های آمریکایی اکنون در فاصله 150 تا 250 کیلومتری از ساحل چابهار هستند.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/14433" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پرواز سوخت رسان های بیشتر از بن گوریون رصد شد. سوخت رسان اسرائیل به پرواز در آمد.
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/14432" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آکسیوس:مذاکرات ایران و آمریکا فروپاشید
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/14431" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجار ‌جدید قشم
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/14430" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فاکس نیوز به‌نقل از یک مقام: امشب چند مرحله حمله انجام میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/14429" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14428">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش از برخورد موشک به فرودگاه بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/14428" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14427">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مهر: یه موشک کروز در عسلویه رهگیری کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14427" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : مشخصه که هدف امریکا متمرکز در‌ باز کردن تنگه هرمز است در مرحله اول !
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/14426" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">منابع عراقی: پایگاه آمریکایی الحریر در اربیل (شمال عراق) هدف موشکی از ایران قرار گرفت.
وبگاه المعلومه عراق نیز خبر داد، ایران یک رادار آمریکایی در اربیل (مرکز کردستان عراق) را منهدم کرد
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14425" target="_blank">📅 01:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مهر : همین الان سپاه با نیرودریایی امریکا درگیر شده تو تنگه
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/14424" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e48872fd.mp4?token=MQEeoK77kBxfhy4BX8lhR7rGEeELhnxChGl0onUNBm08gqRe0pWzxtx_pX1Z_0mPUDjSKeBOX3kFV1eErgJx3Sm0d56kxS7dVDHpX83KjXG0CgpvnCTL5Pik6ddvY1UJ0VGOOUuKqhMuAeFpJ58WZVF7TDIE-RHj5fNuceagHCGTN_dB4T5_YwiWiWsVUm0kRNHAARqubn9vAREFd7nS_2BC2yBQgkVwWZvutsWAMRrzbuesohdLYACPKMgmVyXu4u9WvayiqGxi36LCfayek8YK9qVh0rYewrgOuX0LAJhd1y39SnwTmryMG2EcdqZjKOVpQAD4PZxdSf379FCk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e48872fd.mp4?token=MQEeoK77kBxfhy4BX8lhR7rGEeELhnxChGl0onUNBm08gqRe0pWzxtx_pX1Z_0mPUDjSKeBOX3kFV1eErgJx3Sm0d56kxS7dVDHpX83KjXG0CgpvnCTL5Pik6ddvY1UJ0VGOOUuKqhMuAeFpJ58WZVF7TDIE-RHj5fNuceagHCGTN_dB4T5_YwiWiWsVUm0kRNHAARqubn9vAREFd7nS_2BC2yBQgkVwWZvutsWAMRrzbuesohdLYACPKMgmVyXu4u9WvayiqGxi36LCfayek8YK9qVh0rYewrgOuX0LAJhd1y39SnwTmryMG2EcdqZjKOVpQAD4PZxdSf379FCk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/14423" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تا دقایقی دیگر پیام سخنگوی قرارگاه مرکزی خاتم الانبیا(میلاد مدرسه ای)
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/14422" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام آمریکایی به Axios گفت: تمام اهدافی که مورد حمله قرار گرفتند در جنوب ایران هستند و شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/14421" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پدافند سیرجان فعال
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/14420" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صدای انفجار در کنگان
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14419" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الجزیره: اسرائیل هم امشب به ایران حمله کرده و تو عملیات حضور داره
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/14418" target="_blank">📅 01:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14417" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114223d040.mp4?token=mDUMM-aBhXkfgtELOX_MMXLcXXclR0LcdmY_i7H03OJQt2g_67dxTkXVXQCnP2cyq0t8fjHK7kNth73kg1aY1BlN_FpvRgO9b5kLMQDZF_skJNCjKKGPIvFkRpHWXLCG_s4VXM26ha24AC6i3gXKYuRGsqj--F0M-VDmCZ6wj3HNzCpF9Jb6ESNa8hzPADjAPVHJAW_GhXV_pl6qz-OanmUibZpDvuY-pRJVGIWHPfB4jNIBMxpBwPWLxN2MNGlFA8dZD_nr6AF194knMUgQw6Y9S5sEm3Aw4sOJz7VoFxANDQ3XeKf7574bZyxRdVP_lByLcqYv5qoLJOeTn0ZtXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114223d040.mp4?token=mDUMM-aBhXkfgtELOX_MMXLcXXclR0LcdmY_i7H03OJQt2g_67dxTkXVXQCnP2cyq0t8fjHK7kNth73kg1aY1BlN_FpvRgO9b5kLMQDZF_skJNCjKKGPIvFkRpHWXLCG_s4VXM26ha24AC6i3gXKYuRGsqj--F0M-VDmCZ6wj3HNzCpF9Jb6ESNa8hzPADjAPVHJAW_GhXV_pl6qz-OanmUibZpDvuY-pRJVGIWHPfB4jNIBMxpBwPWLxN2MNGlFA8dZD_nr6AF194knMUgQw6Y9S5sEm3Aw4sOJz7VoFxANDQ3XeKf7574bZyxRdVP_lByLcqYv5qoLJOeTn0ZtXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/14416" target="_blank">📅 01:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a8425054.mp4?token=d2Enb57dpQC2Cd_XZhaP_xgSTjU2ositWTf8Z6tKILJk_HlpzekMTbzDKXc_wpDlZbKDnJrQY_S8GStAjXxnn4uNEfF9sE_OTkqflqCVadBgrmkGuT5oDTpxQwjIC8_oXmdO4braAALRi1a90XQ268gbYRUDFsxXw1xtWnFmR37w8ofoElA9BMkOr8zP4dmf1SPKLfkppEL3mSnq931VVinP2MR5K-xG532J8VF7awE5JMj2pM_bZcXaRpLhYL-SfV9HJQCRLiKH7xpyMgzZB6X2Mj8NTfjupbFaC49Gob0eohunGNJehS2h98teMvcciIfOkSbB_SHZx5HZ6-TJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a8425054.mp4?token=d2Enb57dpQC2Cd_XZhaP_xgSTjU2ositWTf8Z6tKILJk_HlpzekMTbzDKXc_wpDlZbKDnJrQY_S8GStAjXxnn4uNEfF9sE_OTkqflqCVadBgrmkGuT5oDTpxQwjIC8_oXmdO4braAALRi1a90XQ268gbYRUDFsxXw1xtWnFmR37w8ofoElA9BMkOr8zP4dmf1SPKLfkppEL3mSnq931VVinP2MR5K-xG532J8VF7awE5JMj2pM_bZcXaRpLhYL-SfV9HJQCRLiKH7xpyMgzZB6X2Mj8NTfjupbFaC49Gob0eohunGNJehS2h98teMvcciIfOkSbB_SHZx5HZ6-TJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های ارتش بر فراز تهران
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14415" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer"><a href="https://t.me/withyashar/14414" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">منابع آمریکایی:حملات برای آماده سازی برای ورود زمینی انجام میشود
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14413" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">طبق گزارش‌ها، پایگاه نیروی دریایی کنگان برای چندمین بار هدف قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/14412" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل: آماده پیوستن به حملات علیه ایران هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14411" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منابع خبری آمریکا: عملیات امشب سنتکام در تمامی نقاط حیاتی ایران خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14410" target="_blank">📅 01:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر جنگ آمریکا : حملات امشب مقدمه حملاتی بزرگتر است
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14409" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پدافند کرمان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14408" target="_blank">📅 01:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار در کارخانه پتروشیمی در عسلویه
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14407" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سنتکام: نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعدازظهر به وقت شرقی، به دستور فرمانده کل قوا، حملات دفاعی اضافی را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تجاوزات بی‌دلیل و مداوم ایران انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14406" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">العربیه: پدافند هوایی در «عسلویه» در استان بوشهر فعال شد.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14405" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بندرعباس زیر زارتان زورتان شدید
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14404" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فارس تایید کرد : شنیده شدن صدای انفجار در سیریک و قشم
دقایقی پیش صدای انفجارهایی در قشم و سیریک به گوش رسید؛ همزمان پدافند هوایی در قشم شروع به فعالیت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14403" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای اکسیوس: حمله آمریکا به ایران آغاز شده
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14402" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تسنیم : تاکنون صدای ۴ انفجار در سیریک شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14401" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تسنیم :
تاکنون صدای ۴ انفجار در سیریک شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14400" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش شلیک موشک از غرب کشور
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14399" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
وزیرجنگ آمریکا از آغاز حمله به ایران خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14398" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای انفجار بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14397" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14396">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فعالیت پدافند شیراز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14396" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش انفجار ‌میناب
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14395" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۲۴ اسرائیل: شروع شد
💥
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14394" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قشم صدای انفجار
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14393" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صدای انفجار‌ در سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14392" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پدافند تهران فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14391" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOvYUD65RTObY1K7G8GqiGJKs_FjuAPzgAvcNnu8FZsU_btBRNN0X1MVXrxsXwL-Q8SPOL_KcwnOTtVhprzAEO1KvUdjxIF7aEcek8RL5OYzJzG_9o4xg6EYrswltd9ULTvpvN0FehZVLIMTscpxsAYG6CuG4pmxJn2qk793xuWlK6nv3kTfqq9sbPv33TtOaEns9XCt7dKp16QML3Jf70Beb9GUA-sihjEpy4S05KkQ0LMSRkRriVyv2On5Q3Ihv76ZphGkmWtJYplQxi-8BzbMBsATCws7jOTj769gsuyLaAUz8YhUv2NvMAvpySghRUxu2CNX5FJiF4Mh054FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تعداد سوخترسان فقط یعنی چندین اسکادران جنگنده و جنگ حتمی.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14390" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14389" target="_blank">📅 00:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یاشار : اگه جنگی بشه هم جنگی‌ که بی بی کیک آف نکنه برای ما جنگ نمیشه !
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14388" target="_blank">📅 00:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدا و سیما: صداهایی از در نزدیکی جزیره کیش شنیده شده است که منبع آن در حال حاضر نامشخص است
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14387" target="_blank">📅 00:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14386" target="_blank">📅 00:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر جنگ آمریکا:
بمب هارا تق تق تق روی تاسیسات کلیدی ایران خواهیم انداخت
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14385" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر جنگ آمریکا درباره ایران:
فرماندهی مرکزی امشب بسیار شلوغ خواهد بود
@withyashar
💥</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14384" target="_blank">📅 00:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر ارتباطات: از سرعت اینترنت راضی نیستم
@withyashar
😂</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14383" target="_blank">📅 00:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">منابع ایرانی (برای بار چهارصدم از صبح )به الجزیره گفتند: هرگونه حمله منجر به پایان مذاکرات خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14382" target="_blank">📅 23:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آکسیوس:  یکی از گزینه‌های روی میز، یه عملیات نظامی گسترده اما کوتاه‌مدته  هدفش هم اینه که ایران رو تحت فشار بذارن تا توی مذاکرات موضعش رو تغییر بده.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14381" target="_blank">📅 23:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شبکه CNN: فرماندهان جدید ایران ریسک‌هایی رامی‌پذیرند که قبلی‌ها آنها از آن اجتناب می‌کردند
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14380" target="_blank">📅 23:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آکسیوس:هم اکنون ترامپ و تیم ارشد امنیت ملی خود در اتاق وضعیت کاخ سفید در حال برگزاری جلسه در مورد ایران می‌باشند.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14379" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ :
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14378" target="_blank">📅 23:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">استرالیا و کانادا از همه شهروندان خود در ایران خواسته‌اند فوراً کشور را ترک کنند.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14377" target="_blank">📅 23:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه های اسراییل : ترامپ خبر از حمله بزرگ طی ساعات آینده به ایران داده است ٫ ارتش اسراییل اماده شده
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14376" target="_blank">📅 23:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش صدای انفجار از نجف‌آباد اصفهان
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14375" target="_blank">📅 23:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">24 ساعت دیگه بازی افتتاحیه جام جهانی شروع میشه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14374" target="_blank">📅 23:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جواد خیابانی پس از ۳۵ سال فعالیت مستمر در سازمان صداوسیما بازنشسته شد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14373" target="_blank">📅 23:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">میانجیگر قطری هم تهران رو ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14372" target="_blank">📅 23:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
طی ساعات آتی احتمال شعله‌ور شون جنگ بزرگ وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14371" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">باراک راوید: ممکنه مذاکرات ظرف ۲ تا ۳ ساعت آینده به فروپاشی کامل برسه!
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14370" target="_blank">📅 22:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز دو فروند هواپیمای گشت دریایی P-8A Poseidon متعلق به نیروی دریایی آمریکا از پایگاه هوایی سیگونلا (NAS Sigonella) به سمت شرق پرواز کردند؛ مسیری که احتمالاً به خاورمیانه یا شاخ آفریقا منتهی می‌شود. اگرچه این جابه‌جایی به‌خودی‌خود قابل توجه بود، اما آنچه توجه علاقه‌مندان به ردیابی پرواز را جلب کرد این بود که یکی از این هواپیماها به نظر می‌رسید کد هگز ICAO متعلق به یک بمب‌افکن B-52 نیروی هوایی آمریکا را ارسال می‌کند.
این ناهنجاری به‌سرعت باعث گمانه‌زنی‌هایی در فضای آنلاین شد مبنی بر اینکه یک B-52 استراتوفورترس از سیسیل به پرواز درآمده است. با این حال، شواهد موجود نشان می‌دهد که هیچ B-52 از سیگونلا عملیات نداشته و هواپیمای مورد نظر در واقع یک P-8A بوده است.
هواپیماهای نظامی گاهی به دلایل فنی، عملیاتی یا اداری داده‌های شناسایی غیرمعمولی ارسال می‌کنند. در برخی موارد، تنظیمات ترانسپوندر ممکن است اشتباه باشد؛ در موارد دیگر، آزمایش‌ها یا فعالیت‌های تعمیر و نگهداری می‌تواند منجر به ارسال داده‌های غیرمنتظره شود.
اما برای تحلیل‌گران متن‌باز (OSINT)، چنین ناهنجاری‌هایی می‌تواند پیامدهای قابل توجهی داشته باشد.
نمایش یک B-52 بر فراز مدیترانه مرکزی فوراً توجه‌ها را جلب می‌کند، زیرا این بمب‌افکن یکی از اصلی‌ترین پلتفرم‌های حمله دوربرد ایالات متحده است. گزارش حضور B-52 در سیسیل به‌طور طبیعی باعث گمانه‌زنی درباره عملیات احتمالی نظامی، تغییر آرایش نیروها یا آمادگی برای سناریوهای منطقه‌ای می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14369" target="_blank">📅 22:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
بمب افکن مخوف بی-۵۲ آمریکایی همکنون وارد حوزه خلیج فارس شد. قبل از رسیدن به تنگه هرمز یک هواپیمای سوخت‌رسان انتظارش را می‌کشد. خواهیم دید چه خواهد شد. @withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14368" target="_blank">📅 22:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaGfLaCIibeN8ossoi61Gtu8nT7OAam3NCgUDrAQjV0Cgvjc_Whnru0kxWt_oelBeXP4CyGqCv_4oxC3grbkNmeu0a9Jcfb_tUzK7oeTuGSln6D8BPxscnVWAw7gl2joYh1GGX25LnRMjW5HgOoc4gQA9K7MerBnwjopuS1VYQQFFGc9k8FdBpa5LIhuaUAi96kegh8Io7XJqlO3wr8VBs6lXn7gMQ2m1GNu7VggZ3ptj4UJcOUFLJSSBdjetM7NwJQFRTjJx1xDjVQkYXPNvzbZ4Zi9KsBh9JE8wmaLrALLO7nnfmtJ6_7iA4VAYpARGEpaLVysBc1Lg1GFqyshbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
بمب افکن مخوف بی-۵۲ آمریکایی همکنون وارد حوزه خلیج فارس شد. قبل از رسیدن به تنگه هرمز یک هواپیمای سوخت‌رسان انتظارش را می‌کشد. خواهیم دید چه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14367" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پدافندهای کل کشور به حالت آماده باش 100 درصدی درآمد
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14366" target="_blank">📅 22:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابع عبری: اسرائیل درحال آماده سازی جهت حمله به ایران است
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14365" target="_blank">📅 22:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس: قطری‌ها امروز سعی کردن یک دیدار سه‌جانبه ترتیب بدن تا مستقیماً درباره شکاف‌های باقی‌مانده مذاکره کنن، اما ایرانی‌ها نپذیرفتن.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14364" target="_blank">📅 21:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sph9GUIx2Bd5K60m31-kpiyntt57SkoX8WuLhTkPfWNgjOf81lihsdAXIp7g6EEHWfut8jWIJLpt-fbSgKpOdG2pn-zKqWyBLJJfpSdH6wTcHQXz0iL0cj7MFU9vnO9uvsxbqLXhb3F65zJQQGofaIxvOhwub7C8jm1FSwda2vnvfy76wlTmd3hwJFMj-Ixupg8rpvEuOLsShHLgVkXbAn5YGzksgYhsvty10OKspEeZ-5UhNz3t3_UtPiAya9MKp6XL_Zrp2jB2IvrlsZLFjYrCnJOsg3VOK1DQ-rBqOtLyVGlOjk-HIxDjV05juW0ddEhjib7W5Fh2REwO4iX1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
در ماه گذشته، من ارتش ایالات متحده بزرگ رو برای انجام یک ماموریت مخفی به منظور حمایت از نفتکش‌ها و سایر کشتی‌های تجاری از طریق تنگه هرمز هدایت کردم. امروز خوشحالم اعلام کنم که این تلاش منجر به عبور بیش از 100 میلیون بشکه نفت از طریق تنگه و به بازار آزاد شده. بیش از 200 کشتی تجاری با امنیت از تنگه عبور کردن. این تلاش بسیار موفق به دلیل کنترل ایالات متحده آمریکا بر تنگه هرمز است.
نه ایران. ارتش آنها شکست خورده و اقتصادشان نابود شده. کار ایران تمام شده!
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14363" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دیدبانهای اتاق جنگ مثل پلنگ آمده هستن</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14362" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعمو آریا</strong></div>
<div class="tg-text">سلام یاشار
اندیمشکم پشت بوم نشستم بخدااا سه تا پهباد تا الان دیدم دارن رد میشن هرکدوم به یه جهتتتت یاموسیییی</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14361" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایران ما، امروز بیش از هر زمان دیگری به اتحاد نیروهای ملی نیاز دارد. چه با حمایت خارجی و چه بدون آن، سرنوشت ایران در دستان خود ماست. ما از این رژیم فرسوده و درمانده نیرومندتریم. ما از مزدورانی که برای نمایش‌های تبلیغاتی به خیابان فرستاده می‌شوند، مصمم‌تر و استوارتریم.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14360" target="_blank">📅 21:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر دفاع اسراییل کاتز:ارتش اسرائیل آماده حمله‌ای بسیار قوی به ایران است
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14359" target="_blank">📅 21:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
به گزارش i24NEWS، ایالات متحده در حال آماده‌سازی موج گسترده‌تری از حملات علیه اهداف ایرانی در ساعات آینده است که فراتر از دامنه حملات قبلی خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14358" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سفیر ایالات متحده در اسرائیل مایک هاکبی:ممکن است به زودی اوضاع در منطقه کمی داغ شود.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14357" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCv0yc6FvV5CupdH4r6yREaayIR_vZJfl_1iHb7ZmQ4TB9LRxB458_GkcCXN7babcCFfiwvAtzvJgpiCg3y-ey1aJOkJPMrbKlIh_JT67rsRTsKQrQZ0DD_VwpbGzrScsBvUXkvq7TzKKG0hLkB-aXLnTUGTO_aXOvUw9CQwycLYiBwWPF2FRWEoYkJ5F0uaF2S-Fl2DVZ-bubn0ZLQ_-AZN_VAMtorOear0Zxi26BS1WPQxPv6ZHnkuco_q76LiN1lYDfohlfSGOAVS2IEECPorcKS4X6H1sxARTuYweMUOW9KW4TDc9FIXdnoMTV7ZBJU7ZSNIoSWdQbcLRWleyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی ۵۲ هم اکنون روی آسمان سعودی است
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14356" target="_blank">📅 20:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فعالیت جت‌های جنگنده ارتش بر فراز خرم‌آباد و کوهدشت، استان لرستان، غرب ایران نیز گزارش شده است
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14355" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14354">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ خطاب به سازمان رادیو و تلویزیون اسرائیل: ما در حال پیشرفت عالی با ایران هستیم
بدون من، اسرائیل وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14354" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حنظله تهدید کرد !
گروه هکری حنظله: به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست. ضربهٔ ساعت‌های آینده تلخ خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14353" target="_blank">📅 20:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14352">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDANNY</strong></div>
<div class="tg-text">یاشار ضربه اخرووو بزن</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14352" target="_blank">📅 20:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSkNAR-Iidsr74_Y3jXrpnqENvrhAzbvsTsa2HK-JP5Row9fIj6ChrswX_FKHHYr5E7MBtLrwnAjEZ8DZsKfOumMVdqOTD4TPkeFueWY9-Mi29AhJR40AYrwBhCuX0UI8oG3iEaNBnuxqpuXNAJ7RDZyP2atFPwjtmlrqMgO85YMLGqtZdDhiVczgWYDUMGfXU1neGO3yO4jdWSJ3c8wH-AO098dchEnrd9EvhSIaRn4Z5GOX2CSAwROzaTkWBzE8CoBhzj2BZ3VKyNGWsSA0Wo3cxETmt_HQJh5dS-EZ46EIStd13qOvXWXHb-3VXJ50sgfldTFqY0mCByohvgrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش مردمی: آتش سوزی بزرگ میدان قیام تهران
انبار فرش ، بغل پمپ بنزین زیر پل ری!
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14351" target="_blank">📅 20:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdMx05tT6u8L-mf68vxDonAfE6bUkWqaOWmzq-NGRNGLQ_h39ZBlnVyVxnIorIW2p73QBM0jF_1kE9dOxIEm-_eJNWQbudPGxD_7zhlhl-Tx_hfyK01MbfqAr-in_fF6uElWPIIWCsDC8eyIyW3LCIDwS63juE10jjYtgdJZr_TVz_xGA461nqmQRly44l92LrAz8E8l_2dDno6_hHGRRgMWLODdUh2A8OX8LnQkE2XzWVUztJsv2NSiNa-jw_P77FRpu5Die9cOrK8OCL4WpuaXasl5C-O535fd9J7BLVQv3-N_YLV-7tZtrwEVDSJXyzOuL9DbUAYggmAiBRU3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران داره از همه جاش دود میزنه بیرون.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14350" target="_blank">📅 20:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شاهزاده رضا پهلوی اعلام کرد امشب ساعت 21 پیامی برای مردم داره
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14349" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14348" target="_blank">📅 20:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: با بمب‌افکن‌های B-2 به ایران حمله می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14347" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAfshin T</strong></div>
<div class="tg-text">راست گفتی باید پوشک ببندیممممم</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14346" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: عینک دودی مکرون که در فضای بسته از آن استفاده میکند از سلاح هسته ای خطرناک تر است، به عنوان دوست به او میگویم اصلا عینک زیبایی نیست
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14345" target="_blank">📅 19:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: فکر می‌کنم آنها بخواهند معامله‌ای انجام دهند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14344" target="_blank">📅 19:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ :  وقتی این جنگ تموم بشه، تورم مثل یه سنگ سقوط می‌کنه.
ما داشتیم میلیون‌ها بشکه نفت خارج می‌کردیم؛ اینو امروز برای اولین بار اعلام می‌کنم، اما مدت‌هاست که این کار رو انجام می‌دیم. هر شب نفت خارج می‌کردیم.
حالا دارم بهتون می‌گم چون ایران تازه متوجه این موضوع شده. حالا که فهمیدن، می‌تونم درباره‌ش صحبت کنم. برای من خیلی سخت بود؛ دلم می‌خواست زودتر بگمش، ولی نمی‌خواستم این عملیات به خطر بیفته.
میلیون‌ها بشکه نفت خارج شده و به همین دلیله که قیمت نفت به‌جای ۲۵۰ دلار، حدود ۸۵ تا ۹۰ دلار در هر بشکه است.
اما ما قدرتمندترین ارتش دنیا رو داریم.
به درخواست پاکستان به ایران فرصت دادم. فیلد مارشال و نخست‌وزیر پاکستان آدم‌های فوق‌العاده‌ای هستند.
ما جلوی جنگ بین پاکستان و هند را گرفتیم
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14343" target="_blank">📅 19:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عرزشی ها ریختن دایرکتم دارن دیوارو چنگ میزنند
🤣
🤣
بای بای بی پدرو مادرا</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14342" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۴ اسرائیل: مشکل ترامپ این است که تهدیدهایش دیگر نه تنها در نگاه غربی‌ها، بلکه در چشم ایرانی‌ها نیز اعتبار خود را از دست داده است
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14341" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14340">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: ایران وقت‌کشی می‌کند و من می‌گویم چند روز دیگر هم به آن‌ها فرصت بدهیم، اما آن‌ها همچنان به تعلل و وقت‌کشی ادامه می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14340" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ : پاکستان همین الان داره تلاش میکنه تا ایران راضی کنه توافقی انجام بدن
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14339" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: شب گذشته و در گذشته برای هدف قرار دادن رادارهای ایران کار کردیم
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14338" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
