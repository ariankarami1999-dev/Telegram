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
<img src="https://cdn4.telesco.pe/file/JvI_Ll3TxU1S4dgjv-yKfbhgKeQ1kW4EJzo2BpOnaXOitQ22tF2S1qugbGUdO54sjjPIQ7qhph8JSPjGR0fL7Pzhd8RIRxhL_OEk6JixUToEWC0M-t8tHMOfM45Z-6kz0wcPApewsMJ8iOA7HB_cObaAOY_qe1Kycq_c6HbZEh861dncB0PWSuHULIDMw2mSQx7xOUiGQSuSJtahCwux5G5yS0_T4zM4PJr2sXnLFzyRyz_Rh1E1pXT0RUUzShMhgIACkWyBP2TLbrTlB1rp9QvYZFfSo245Qj9sIbBcqysWs5-H3P_I5IZwsfAa4CzFMCq3YlpavAxidq7zuq63sw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=Z2eqyq7X2x8eDQdQhfY4OlxB4oj5XluAlaHi2EtDHxVH50P1_3BYDpk6fvtvUs66qVPXw0RsTFXIrDnq5mpODU2VQLk2QslbP8brSRA6RfDfQosnFnpWwET-69h3oqI0v4Xjj7OqvRMw4OJJokqN91NP9mZvuMzJfeQEas55D31QmdUpaFzXwK2MoQz5rSjWTNHVUlqCu2MobzkvwNy8-99k1I23rGWpILpea1MZdAhEpSU4T66enQ6kXUXxgJQxXqEnVMpLvjwESGOQcUGF61O5XJ4QIfEMrBTROVR6ywBmWxXfgJALshFzijiwHDgJbpSCM5VxgAHkfh8r8x7sww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=Z2eqyq7X2x8eDQdQhfY4OlxB4oj5XluAlaHi2EtDHxVH50P1_3BYDpk6fvtvUs66qVPXw0RsTFXIrDnq5mpODU2VQLk2QslbP8brSRA6RfDfQosnFnpWwET-69h3oqI0v4Xjj7OqvRMw4OJJokqN91NP9mZvuMzJfeQEas55D31QmdUpaFzXwK2MoQz5rSjWTNHVUlqCu2MobzkvwNy8-99k1I23rGWpILpea1MZdAhEpSU4T66enQ6kXUXxgJQxXqEnVMpLvjwESGOQcUGF61O5XJ4QIfEMrBTROVR6ywBmWxXfgJALshFzijiwHDgJbpSCM5VxgAHkfh8r8x7sww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=Ynk55h9yMrgweVROen7IorKN92PKpWa_FEbHI1-X7l66gaIb-nRYwqANcxzFcAZ4RE6w1bnIv1SGPwNm0kk71_jDeSzJOs5uoODX93RdF0bPgK5I4RDqmlstYJPWSzYsXsFu5ss_W01fG3KoNaeLpZxu7SV6xx6XtlRrOr66XWVETjmcPlO0kbtleN-XYpG9jirUP9nf9Dn4-HABi-Q0wvqcA69T99eEYLubbeWqQaAjBaDTf2uBCG8o_lh9XlAQnIpDbuojsHOeNhP9WyuXc8Zl-2RBQo0Yfl1fmQT5_B1GcSnVLA-8e384EZwH6Wcp1SYFRNSXalbhvEhlEG8H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=Ynk55h9yMrgweVROen7IorKN92PKpWa_FEbHI1-X7l66gaIb-nRYwqANcxzFcAZ4RE6w1bnIv1SGPwNm0kk71_jDeSzJOs5uoODX93RdF0bPgK5I4RDqmlstYJPWSzYsXsFu5ss_W01fG3KoNaeLpZxu7SV6xx6XtlRrOr66XWVETjmcPlO0kbtleN-XYpG9jirUP9nf9Dn4-HABi-Q0wvqcA69T99eEYLubbeWqQaAjBaDTf2uBCG8o_lh9XlAQnIpDbuojsHOeNhP9WyuXc8Zl-2RBQo0Yfl1fmQT5_B1GcSnVLA-8e384EZwH6Wcp1SYFRNSXalbhvEhlEG8H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7mDL43DLXTWW8WOfhKd9lFS9rtu1NpQRjGOFeOJ3rQN7tH40Q3avI4G8ocm665h0ZFMgtBMX0uFzNCqs1ZUSYIdqGNuzR3o4YKfiOuhRUo9aiXeKu97_uLjgeGfx11R4sRYVL50JSKHQ0UXjK6S9OsP8Aot5mBCN0ut1pWfbGHATrVzfpZ40Z_pE18Rv4DN6AjwZ-1UUT_yRaactyzW8ydWbrv8xjHf_oz6Nw9oJZBXs2TWlza9UCTzQUkbI5xFcqBKpi9MHMFLPPlMD6_Em8MROGPwIBrdPh5zUL8GvsvcV_6Rdu43KHLPbDOAh2WY5TJZ-OVtxiAzQd08qSLgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLUOtHDCnq2osnmSLuKItdOv8Vtdfijq18537w0yTd4RLI3aF3QFle1bXerXlp0LYFJbM0HhpYSoRZiFYJBYt9s0j5hQpyRgzZjR4UMFw_LlEtnobDWu3ldvLoX-Yq1UlzrZ4WCL9wyNd7QxScZNEk1HCT9UnS8dPMmCPq666BR8q0hVQaoKAZ_vnNj88fOOGKi5hdwezWRaBcucGGMrKr92AU-kjavZ7FLG1A8L5eKhMbXr2OtC9iILZfoGNbsxryRLrze84orAKa6OaSxJoGWEAslOEl2cFwapez_kDrnC_yw1pTTgwSl5Mf6eYQzeW1prIgljFonablkrRC5SQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=K-0Kh5gJztqZUAFRPOSCMl6IM3VQSp1CC1zMWVWCwpoXd9GuYP7wNhaZL3WMDAmc5FX0Nh7nPyVkVdZbvCSBMMaaM3Udlybc9OkQg_zh3F9AETZiaFIUSegBrqDlKCCx_vaIM1xj9i5ylKtdxOYDwwl2JK_KSzO1sgqBXTzmi7JaA2HP3R1z-QsryX64fjPueJL-zvdPgF2bzWdWs2MKFpC1I5HazPS6wjUkkU2KjRna8pDOMunXBfEpGeJAPgKWAvzvQyrMZ2PJ-KqiL_AiEF3KQh7nTCvr3ShNJ5hH6jgWxwottDGAH7DTeLc7klhV6D764BXO0kvZ3VerEdqfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=K-0Kh5gJztqZUAFRPOSCMl6IM3VQSp1CC1zMWVWCwpoXd9GuYP7wNhaZL3WMDAmc5FX0Nh7nPyVkVdZbvCSBMMaaM3Udlybc9OkQg_zh3F9AETZiaFIUSegBrqDlKCCx_vaIM1xj9i5ylKtdxOYDwwl2JK_KSzO1sgqBXTzmi7JaA2HP3R1z-QsryX64fjPueJL-zvdPgF2bzWdWs2MKFpC1I5HazPS6wjUkkU2KjRna8pDOMunXBfEpGeJAPgKWAvzvQyrMZ2PJ-KqiL_AiEF3KQh7nTCvr3ShNJ5hH6jgWxwottDGAH7DTeLc7klhV6D764BXO0kvZ3VerEdqfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPeqSvT3v2QV5_4zBuMAy8luEskrtYTEf8JwEvEE25e1SjJdtT4Gts3YhgTgO3yZEsH5d-P8snb4r-O85OM9N3qG6PageyWOGYIApTzaqwLvmJltG16I8fARr4D4ZT-dRGUDaFauY96nO-BAaxjbjI9U5rgkZSLSjMFyb7p6hIPSs6ExCPywcVF92mnmL5GKHuzrn7OdSHbsJHhgqJWv8Am_Kt2eRfmVtQrm5IItnjDfkYAqx_XcEcKtBXoq35mF56Z1GCo8XC1kYGbdI372TLIK_kueC0ahRuOB_cTCeIsCsQPeAKrsyHwzYH_1qgKKlTlRS5J285hp2ElUTzWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYpHd4VTDooC5AIEwzeutZLhEgeKvLlgwEBa-x8TTPZL0n77aXn58I83qVQUXy76-2mWy9mKlHsIeJufXLx4dCgHOYQvVlGxssOseZIG8Z21SP8l985wJpX_AG2_MMNOm4pTLfKQjwDKTGV9eagR30FAyqteJKFctF5cRl0WyLa1YAwP5_1m-1sOaiHz0W2KJq4CmlLRJxyyM71O7BxZVsELv7I0duKbUN03l2z9BFpjGkJ15QTXou8_uFUre3awwxoDC5pw71ab6Y5JdMj-QKGgyVAhvF0qCpDTLJXGbvNeZCtLa40SoArOSSuM6mASIaIRonqGJ_K2LKdHuwMmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4z_QOqhHVx5OJ8tU3cQSPwN44pxWEXg11BxhXjb4RBPIUuHMaIqWi2HyU7V-dfjIddaik98NMwmWJdghuNkJhfqK5c-LsA5DU-oXbdAunMeZL4fh7GSmzr5Yq-FKKE2QxNsChEoacoWAjvMax5pIJnc2uS-JVuFDUWdMW6Y5YY3ctTCu1zWDgIk3KFU2srb0gRglwg38bz1dLFomjLrt2R6NwGmWLPhWjj0tBDuIhFj7EagdgW4mFjleRmsus0LRt-KlLgoWpE9aYczhDE4ojUZTiF3CEDX_zWWkKqwWzixVXCGPuta7uBUCeASInItovmv0OrepBhtU97B5TZS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCJYqEiDNqYsfV1W8EG4s3fW-sVqn9RAfPNG_m0NAIkqNfIFK05a9K_Xjxr8bUxSNGgQK0-O3QsXBA1A8paOpO9gR6ooUWOZWgQr5C6jObj4Q5mNcqerqaHU_tAXwyH7Tq2aAeiIFipm7Ej1MPi6p2gd0t-Th64RE3g8-6W_KKU6jr0MGb8WB95N8-4bi3OMuVvtA_2jKrrkQKrB9LXzfI9_JZVgZCfHSMRHxnojdKOltZ4eyjXi2wymDSoFs2OhSUAnaOVvWidgsyoeUbN9wpv-o6P83lWTzWeovuu1oNpqInR2UeIjmU_bFPvtBeHLvHJ21P_3l_ThHcS2rBJf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=ahs_AAG1AretrSeelRGTz7V_S_zlsCUCSt4ABA3zvcoo0QRXW2bhqneHX0CoVAxmGO-BI8gTYImfm98xlBXlTeJjyq34qR5nKzmFi09Damx8nqYcSp9_hzAxTHE2D5Iogk705Fg6dkiwSlEvQqIs1K1L3LPI1iigRwK3SwXCQMkAxXreprimL12zqh8D8ULgkS86uyhiUvXMdL7AyVIs5YJnOkL8FA9bxqY49bGrM2KYuoeXx2et4Pn64l0T6IruJOLaNe17MJWN-eXDAu-bDjWBlSPRsc6EF2sKfwHjjpBmRgzNLwFRFdneTEbGqJy3QRP7hfOCV3KIolI9bl3LgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=ahs_AAG1AretrSeelRGTz7V_S_zlsCUCSt4ABA3zvcoo0QRXW2bhqneHX0CoVAxmGO-BI8gTYImfm98xlBXlTeJjyq34qR5nKzmFi09Damx8nqYcSp9_hzAxTHE2D5Iogk705Fg6dkiwSlEvQqIs1K1L3LPI1iigRwK3SwXCQMkAxXreprimL12zqh8D8ULgkS86uyhiUvXMdL7AyVIs5YJnOkL8FA9bxqY49bGrM2KYuoeXx2et4Pn64l0T6IruJOLaNe17MJWN-eXDAu-bDjWBlSPRsc6EF2sKfwHjjpBmRgzNLwFRFdneTEbGqJy3QRP7hfOCV3KIolI9bl3LgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=NfzripWQvihxivf584_tnT4uLqtjU-bAu4vDyh6liHyrjSikQm2rdJfxzgeKs-lMvK00n14XJtZ310r8ghyIf2Zl336Vepwdl7g38EGGSh02xwLf-1LhuPNs2BEzZPOMw_7CvXtRYtxHBiwlDqyzhVtHaIIA7HgpabSbGYOcRshPKsdYwOzDXhd1ac69_fg4j5euYnAMqy7Z4B0QcRusQ-RyjthBRAvqbB_RSs5-EBwDeqhX_kI46dzQzjBBJRooYZB9o3-VDjUnV7PxbLsLWp1w-niW9H98D9y3ixDB7mM9ObNBBRZi0GJkbIvdzq6faeeDfq0ZNSx-aHqU4P0mUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=NfzripWQvihxivf584_tnT4uLqtjU-bAu4vDyh6liHyrjSikQm2rdJfxzgeKs-lMvK00n14XJtZ310r8ghyIf2Zl336Vepwdl7g38EGGSh02xwLf-1LhuPNs2BEzZPOMw_7CvXtRYtxHBiwlDqyzhVtHaIIA7HgpabSbGYOcRshPKsdYwOzDXhd1ac69_fg4j5euYnAMqy7Z4B0QcRusQ-RyjthBRAvqbB_RSs5-EBwDeqhX_kI46dzQzjBBJRooYZB9o3-VDjUnV7PxbLsLWp1w-niW9H98D9y3ixDB7mM9ObNBBRZi0GJkbIvdzq6faeeDfq0ZNSx-aHqU4P0mUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnz0GLPHbMKB86Q2SN8KQCUjIndu5eNbZiBL98KJxHy5464fKpyJtmK9SmlgLOdi8qLWrfILpBCQsl4Gb8UPLo1bXrin4CYFqnogdlbRu--GSPoqxYn44KNchSFCO3NBARCbXJeT2GV0KZX3UY4gXPUlcBZV2fOlqZqfQCmobfzvozs2FTXalx-zsmYzo3jF4eYqRPG_Pah3osDm3kZCXc_XQX14Jd6rKv8bqddXWHF3ogL4G_zcf_wnf3kWl7Y6c2l2xm-ZhMSf7TydpR_8xIUbrvOQRBFYbIUf1B_xMSLlLKtX5om8d_xb31oHFr0P4xGbIl1392OrTWC3MHhY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4z-P1VkAfRkUXZ2t9lHPgu9ogX7T-EVG1KaEHlKQ8gje1FwZkMKYNtaWhQLD3Ags65NTDV4GDw0QP09os51jGshFzwEs-mtn7eQLliiawLUohbrktP8VTJ-27cjTNZEH_cQiSWCBLrhVEACNi28M31fz8sM39aaaLsJyvDP8D_r3RUW1c02YNL0qUOPezKXTni4PeWzWco4rFqupM6xM98cgCKa5WlId2iXiQ6X6hEZ3C-RCjeKwSjQymTgvzIdtEFaxFtZG3uiUpFGMqk8-kRJVz7xs8FQ8QQXDSiA0mj-7gEUUZ3obFRHpOYnxk1e16CY7F65uVe4GFna_wO5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV9N-bQbqishj43Z1vm96NsFvEnRCD139Wj63JfrVplB6n_TkaX3IcpBZa0FCE-CZDKAaTFcoHPNYmqheA-KqT5dMNInf1CyQKOUe5jIHcjkmb0uILOh9uUUeSNHO5kNxmPrKfZIyU-upRTfqHnwJCdLmB9ItmxBKk0Qn9crQYwwNa1JN-c36WvXJ3Z3E3AaTHwRi6gMvUkr10M5zvBfaIgwtbQL4JLxwG_nSsjqIE6tv7BxprBQ7vauCgrbHTVpH_2lWjmeHe9a8oQP_1t3tXj0YnZs1hBaebc0gVAN8ZyfQ22PBU9DymYE7KG4BeimTjBBQbJ04UMImJMho_mmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=KHP04yA3iH0J8QRL08iwDK57lm-6n-ScnKHql6NaV8QAKu9OCCUS-LD-4UZJ4qlNAMRiBNvPAODNq4wZ9hlp-EUy1_C_AEJO1kvYH-s3AhA2DZAjtB33mFL7jL2IWWPu-t2lD5P35jrGLOwawOoonL1vMBUbDBlTfxdg78b5dQ7YopaELU4nxHz8SG5Rlx61M_75iE9mJwAm2uzLLL4ZspzJej1KnIH52uk0a2WphjuBV8reDNR4NaWRuHfBJ_z_ouyODJmY6bfDixw2PCYROAt0rRcKSSQwvJe5hcDhtWGi_VgwoPg6op57S9WeQ8u5QUSu81sEuzHRSH8JH0MoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=rcIiCTLvAVpEK-7Cnq05n5hfTDDER9roYLFYt_w7XhNTX1XcL5a3FpwE6_4ziGnQXDcnlx6x9b5RqamijHluP8LLTnRpMOpjg3JtIoOG4_LqyH2mltnuUT751JthOSPNuDBdkT9etBtTNIzhXkFzKlEx0f_xVog89tNVU-IASAENMRqosp5thtncv_gDbSKo0SukzqE8VtHj_cNIQ-Gixehx0vI1QPk9VeuWxAK_FQioZVIzcZG4arMHCA8YANySXCfttL_DzBxGC_-wQPamRafi-7b0MyTu8gHDGY4HUYySTMo6w9G7C6Q4FNRVOyJ5XjdI-gUBUjZFKHP_TqaFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=rcIiCTLvAVpEK-7Cnq05n5hfTDDER9roYLFYt_w7XhNTX1XcL5a3FpwE6_4ziGnQXDcnlx6x9b5RqamijHluP8LLTnRpMOpjg3JtIoOG4_LqyH2mltnuUT751JthOSPNuDBdkT9etBtTNIzhXkFzKlEx0f_xVog89tNVU-IASAENMRqosp5thtncv_gDbSKo0SukzqE8VtHj_cNIQ-Gixehx0vI1QPk9VeuWxAK_FQioZVIzcZG4arMHCA8YANySXCfttL_DzBxGC_-wQPamRafi-7b0MyTu8gHDGY4HUYySTMo6w9G7C6Q4FNRVOyJ5XjdI-gUBUjZFKHP_TqaFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین.
مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است!
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uik-_fd8AiqJefXtWIA_TebJyD4D3F3Rs_yYj2wtbsfcRu1Poxg1IupLzl9u0SPQJe557otqv7OrWYS7hjBD3rCIwG0TYVLVmk8Wt5tnqvNtUkrgqwcGF9-D8saRaTUODl08DqubtgsO3haKuodKa0y3FSenGgWhQhplirzcYkX2EeJjDOsWPLHpmD0S-k8WL5ol8IlfzH9EI3sV-Wo515XfZOc1JpewHZE7Ej-hh_Xpi-gcwuvSz_ShO5mEgsy4A_NBO-a-KC3m6hxzL_4Tjusrp9AYYBH0QCOKwcRZ66IyRSwWE1J-L9OJy-QJoLXkIb7V5ZeYu6iAPxeCSpHSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6R9RdIxQDkReLFAwpGwOitUsrWjK1puIM1QtqcxqlXdJLwiZ-7gyaxMw0f7IBBiuurlAIS8Us_8MGy6y0WrjPxfGH-fDatA9xXgA56jUNtYAftkZDxUhbDcpEIgQIwjKAJD0jBHBPjPXZ_xz5G1TbrOk2a-NMrCgwLBV5QMn32mJiK6Z1q0Zo_EyWKKsw-G0WAMlcqaHQ_clEXEnFtCKTY6jUeha8SbU7FPgxI_GyKJRifohku7_aDSc-wVZ4fZbKny4z9tzzuD-6CTe8BytFoRIbrxpqd2LSzPcBAOqlF_iAXQa34uzwmcmN1g1JIg4l0E3pxegl6ovQnpQ37S4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E45Cqh6uuj_fm48N8dCJdYnIvAYY4qhwMLgUSHPe5mGSn1M_TuGfJdBSQD3kpmr97B6XlsTDdQRJLsY-4lMUyqGwksmHw4l-gTEMqujCJ5-H7SRJ0uNhlfboYzu0gbEKrG1hXq8-sHLKZxspxO4ON44BOXxSmkL8hLUBpRzemJv-ZrFgmYHLLaJ99qh_wp2LZwojqr2WmclNJvZ0DstidKt2iMWUITTsAnwGldpHRypOQLtnyIDJkWGtBO56VCEm_upHDe_6juToG3bOLZJW4u5wriSjorTLeuSC_ph-sSzRqH6VxMzvDXhGNq7C2frzCKxeORJbDRoInVyGWjj9JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECYQWsnKOg39QdR02Vcrlx-THOJQBZH_jGLpmWJtmN8fhdeFVJwZLAG0xBGpTOygYSKOKppbwUyGugMKFV6qFavyWaGxthRxmoWMhH_3jVQuszx-M-4IPv0mQAj7hv9ayik3jLXFZXPLgdBdZf1OsbytYxaVyM7DxJgTKPvwAHu_2TdyGTiMaJT0o88wvpYX_BKyu3haSiEeB5Lf4KReiS6TJ06cvQFq1xQBWEym3JPg_krQCPEyaAHaVqft11zRI-oIrugeUF47urzfXiawimWspSSEWITKLBuqQiHHYXqRkf0TF2a5-AquKCtkwMQLn6yBHJwoDW_1NMiuORkeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IipNb9v_29pRqYkuIeWbqNq4z0VwDnlmqRS9vOn_QX2QMuJvIFUUQdYjsWmEph_1ylvnRxqrfwEzEnGXmbv2ViJ-l8LogTelaBBJjB4P48afsJs20PDsCPCudGBy1TV-dXqdBh270V-cr09Xo27keo5XYxsn-XogMm3_-gjfYINzWecrX6HdTVY6Ip3JKs5nr6-tguh9JYb7EcQFc70zWI_bljRKNP3bU0a2IKpXZEupo3hiuntG2gmaNr4mPqbTYuSU0LkcuX27FSEcN7UGKVbsTClMTbHujJvbFVTg8nlrdEUPxSaUwlnc4aLx0MdO4gy-UACFiD60gVV4WRmWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1zBKsXOaxjBp0DCVkG5FBgjyt1W5kdAgC2Mnx99huhTA8TufrkGd4RhAR5xX1TyvdNH68cj-xV7Z1oIb6SyJrX4V_zgBO-ZW0fnHU1sJDRH-AXILMe7gEBXuzL2RrekbGLXQY9j5rWrQV-FITY5uwWzl93tHXoqA4Z9joE4yuTmRvBvcZLO_CSs_Ok-UliIcaZtts4PxSWxcBmrBPSOX2MmAY8-TxJMAFzEXz1c4CBczATjKLiI_qrAFxQdWisPld-MTesbA4jcJilhakwCBeMSuXiYWMSiU4m2NcPyyF80-B8bF2DxodqF2LaGoDJKFUa-L-AhxUTfLG4VYBqpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16443" target="_blank">📅 17:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیویورک‌تایمز به نقل از منابعی در سپاه:
مجتبی خامنه‌ای خواهان حضور در مراسم خاکسپاری پدرش در مشهد و اقامه نماز میته، اما مقام‌های امنیتی تاکنون با این درخواست مخالفت کردن.
به گفته این منابع، نگرانی از احتمال سوءاستفاده اسرائیل برای ترور یا شناسایی محل اختفای اون، دلیل این مخالفته.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16442" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQGIZrMZ5FOHPmP7Isy1IQcXdXD8SL-mxYzEltQQYuw6bDpz5DsAxQeCFKsHUS28tqB0rreGylLdYLClNNsFrTDxMR1RxMyxZEHXcfHLSqSzezZpAOkPcpI0nkD75Tum0PWxy8itfjyQyFsSsUOzA4gfHLo8vZFZpNLMUwUS1qKu8kBdjOR8jBJMpeA8-CeGC0mjwyQFHAxiNgxxKBwgOeKtTUJCSNXWeC59qKGpQevADciEBkYFXOlFwJ7yXQHPpjDGqpo7D2OYi7nwPplOdr313m6WJkF3jaak2ZVYMP1dcR1Ru3PVIiy8zjumRVsu6Ep-uXXzU79tBp46bm_vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار علی عظمایی امروز به عنوان فرمانده جدید نیروی دریایی سپاه معرفی شد.
فرمانده قبلی سردار تنگسیری بود که توی جنگ کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/16441" target="_blank">📅 15:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=DgYd1RuJ2Skb_sNqD1OS6qxzVNA3-fd32Ep3rXVFB4bvz-q5t6C861URKYJVNk5_mxwuFPW681QbQHwKdxCtqStSUYP-khXcF-__lT02yNior9kicm6oJhjJhf4-QQ_bx9H46Cm7lWl29zDFpAKH_cTVPBt0PsBiJ5K55VLqGwY39SjWk4uWsUdnWQza0vSPJiK8LDsqJbo4v-Br_fLXBe2BZv4Nf8pxIro1PsHngiNfyEdkXzpQgitfLEGVYHcHTJfvZ-sB8Y5eK-ugaNAxxyUDMytW9t5kzpvDXIRQWgFoXX6uIF6nfQI36JdfmoN-UKHkL7pFPP5Uqyh1vxCouFglFeRT3OOj6W2F7iymaO6Sta5ovVzae__jsOs9vhseeNGR4jE_mQQWlVT3kUvHIQKeIQ14HOe8mdsamPqFc1FN1HUoJomltHs68TCiNXydW21cgJ6W3P5FaNmVv2m7igh6KEwt251869zgoF9mS0H4GfsFfy5cd2lh7SGHY9TkQBJGuFnY30o_tFIE0sq9zPWclFkaU4IrtGY95ocCIqhJ6y8yMVfc1rZdhYRlOdKXOtQWRYiFQhRrDovbEScUlYMNCWpWuUzHeQF828Bi8U0owIX7Hn9SK-qvg-Jo2-0OQgcwj725GKiI-aWyDJJxyxVGUA3KuQFg1Pi5h5ZcRjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=DgYd1RuJ2Skb_sNqD1OS6qxzVNA3-fd32Ep3rXVFB4bvz-q5t6C861URKYJVNk5_mxwuFPW681QbQHwKdxCtqStSUYP-khXcF-__lT02yNior9kicm6oJhjJhf4-QQ_bx9H46Cm7lWl29zDFpAKH_cTVPBt0PsBiJ5K55VLqGwY39SjWk4uWsUdnWQza0vSPJiK8LDsqJbo4v-Br_fLXBe2BZv4Nf8pxIro1PsHngiNfyEdkXzpQgitfLEGVYHcHTJfvZ-sB8Y5eK-ugaNAxxyUDMytW9t5kzpvDXIRQWgFoXX6uIF6nfQI36JdfmoN-UKHkL7pFPP5Uqyh1vxCouFglFeRT3OOj6W2F7iymaO6Sta5ovVzae__jsOs9vhseeNGR4jE_mQQWlVT3kUvHIQKeIQ14HOe8mdsamPqFc1FN1HUoJomltHs68TCiNXydW21cgJ6W3P5FaNmVv2m7igh6KEwt251869zgoF9mS0H4GfsFfy5cd2lh7SGHY9TkQBJGuFnY30o_tFIE0sq9zPWclFkaU4IrtGY95ocCIqhJ6y8yMVfc1rZdhYRlOdKXOtQWRYiFQhRrDovbEScUlYMNCWpWuUzHeQF828Bi8U0owIX7Hn9SK-qvg-Jo2-0OQgcwj725GKiI-aWyDJJxyxVGUA3KuQFg1Pi5h5ZcRjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5cXMNhR7ZaZY88QG2qJ27fln_M7Kg-gk-kgBYQ1vEZbI_cYG2mh8zWuyx_tyhGaBMPxXs0ZkBuLRz5SQEmYJmkpjB-I7lh6y_KD_UVixG2CKw-p2ZSlmsoTBG4u6YwLrMJGyjZ5AdH23LQzCfW86LBJvEX1uZbRpcFQJwjsD1SKxhWn8QETsDG8b35x6l74pij5rUuh9NkIKlpOTzQwyR7en90JH9Do-kdy3AWNxgO785VZktZGLXteg7xLGZPj6yqwYXzFSetprYh2nr7pvy6KAcv40DHvQQxZxlyhxCgabZUqrvKTJb1Q58BbqBlbkTkDiRA1Sy9vwO9-i1J8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiYl7bGxSJ-GBAJjHWFjNfwwZc7A_5wYdfCj-nGiaptTCYAES5F5amr5oO5EObAVx7dmSvEKBwPQQLUKlrhVemWRAYG1nVtnrYpgsfhAHyJ-xR5__oritn3B_mdAMoyqPMxIMV9lO8LGvbY4Lj-qtd9GWBsBwCvJZD4g4qkFiO8uGHaJUJYtBaKaNS5gsP7J6vFI4J7boAtYnpgB3q5GTkvR9sXTGlRUH-aKOxuwN87VxWdbqWS_dgUDa2OaXpqz_fVBWbeCjHE7W9N4edEhk8U66AXg0nwoErR2oqGwf55fQlkg3TnHXBw1ti387Q404bMfL9MHeXbjzCQ-OH0fhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXT7WdN-q0zqPAUZbBMU70lXGbVIZihi_bxXIEV4xq8qjDYkg6bTWEhS4L-AlQEFtHwaMpDL6thpOnqai1t0ovDrWWYq4p5J2bubQKrIF_KB6htV4eQ06ACmEzcCEbiEhbAwn1JYbUhCc6W617sgTaXenQTHZmRJKlMRSWfhtK-In3vySohJWOm6rMsdf9On2dMwsvJQaiRoudYOHe9MSrO8FEATqT3nMpDe5RBoHqh7F_EAImO9M_2IvR5aIO-p06ZRCKNE8J4Qz3dMqmrxs-qBWUyCvfRu2mGPouKcS0fytHw_9X6BhhbldBCy0jt1IQ84vkTZj07UnTHHUEfp0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb9X_7kyYC2laGSGBs4-cuVwy3fWEfhsWSstdWChw4CexbuC5Wd8T3z6r0jijNjtbN_Q390poajLDPIJbnLNp7z0RKZDZPOWBUdA8h2C8XkERTXFQhdc1lE8-rAVX6pRp-s6l8VcxgovlEblmvjtAhSNNeUQGRYDne493kOHCqQDGIfqQ5KJTi3F_IFqo36Mrsc6rqlxGJm5ZlxXzTMnLuYoemP-NsJxOrtwvTB5d77u1IhAtPlLuxFRynBhHz3ODeot-yjaA05L9A1t7eWGsoyqTH5-D-wYMG3RENFo_HygBlTOj-oF5_sEUuXeEOaqikxHsRyqf2tTg558wmVBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=DsC1ehPHrtULl_pzS8twZeJ-_y4-g1Ig6sOa2_CnS-pPyhPKjqzG8WjQyOSfFSkGw6J1QX8dLg6Et0p4ZjDnAnpLFiJxQ-TFFoSmEKFaOUW2AfvowvQgRqhfdS0ytapoeNPH1veZDtHD6MMwuugANawKFAXOhfNtoYfW4sZ1aJ0P3dEdyN5l6NyG7Of8RL-HM5gFw5jUq0UpBdXXCpyVDLcq7C6tpOufaEsbl0gjv0vinLVQyr3m_5idVLf-IezaDTCIKElrcDXjaCfAIsUPCgyW21NHzJNva9Swgu-lRAXCX2i0CbmbQvZQ3nfFesL-Cezr7oXxJ8Jy9xw5BouKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=DsC1ehPHrtULl_pzS8twZeJ-_y4-g1Ig6sOa2_CnS-pPyhPKjqzG8WjQyOSfFSkGw6J1QX8dLg6Et0p4ZjDnAnpLFiJxQ-TFFoSmEKFaOUW2AfvowvQgRqhfdS0ytapoeNPH1veZDtHD6MMwuugANawKFAXOhfNtoYfW4sZ1aJ0P3dEdyN5l6NyG7Of8RL-HM5gFw5jUq0UpBdXXCpyVDLcq7C6tpOufaEsbl0gjv0vinLVQyr3m_5idVLf-IezaDTCIKElrcDXjaCfAIsUPCgyW21NHzJNva9Swgu-lRAXCX2i0CbmbQvZQ3nfFesL-Cezr7oXxJ8Jy9xw5BouKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=slNtj0mtuop4EcRfnZyqbEeN_MC3N-EfByoAl1zZLqL-UmDlpKrO6i4zV09re0RnmSwy2zjoYrtD4BDktE18Gns7idCBg-nQMzRxTwz-CZR_ydOYC8-Wfba4fK-8Tnjo3DsBHriZjJHQhl8FCHe-2Kv4vDufhuEe0nN9PieMffOJfSCMQ9FVopxlU4hsbu9bj5xNLt0sj0Z2sWlDRQ-ZQjvFyxy22ZfjOr3fEeLubjWyl5tF09LY6FBQOuUBnVzVR_gOeJwzsHONhoCsF7aJFvSxA73mbhPli4QFD3h7CsXK5maOt6kCh49XWlSWH-Kubnrvq750JIQtdg1jLuAiuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=slNtj0mtuop4EcRfnZyqbEeN_MC3N-EfByoAl1zZLqL-UmDlpKrO6i4zV09re0RnmSwy2zjoYrtD4BDktE18Gns7idCBg-nQMzRxTwz-CZR_ydOYC8-Wfba4fK-8Tnjo3DsBHriZjJHQhl8FCHe-2Kv4vDufhuEe0nN9PieMffOJfSCMQ9FVopxlU4hsbu9bj5xNLt0sj0Z2sWlDRQ-ZQjvFyxy22ZfjOr3fEeLubjWyl5tF09LY6FBQOuUBnVzVR_gOeJwzsHONhoCsF7aJFvSxA73mbhPli4QFD3h7CsXK5maOt6kCh49XWlSWH-Kubnrvq750JIQtdg1jLuAiuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTEFJ3i95LRoypsS1_KSgKaHjKFS2MCFTEtqLCYci__T43Bnuwq7_zNKHQ5vz9kTeo6k8fzbVkxr-GsJgVHjqDoaf5igPQJugidtznPbWJ5RpzADSOD70_a_kTz04qvQ6ZttyRTJipj8NzZOve2wICboo9sxKv1HyRZeWj0qm9IU2R-NcL6OAW2GC-8nrzNG0AGAALFrDrlHrMyLMmuODaUSc_V6CpAmTx9_XcWHKwRZ_6JXJ-v5SgSPaf7H2nNQ2dMbcBC8-tiCwkCVV6BEnMjXkkDiTs4DakJc8prWBcV_AY7dqq9T2-lzcPjbaQCQLaDnrjodq5Qly2VcUIGrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME3cTBgYNDzadoUgOdTuJfu0AApmW8VHB8ApMgVUsErmK8P8tNpcJ-ZY54HcJSK27w-psv0SFvmpVJbuRA6Ik2uiELlqkzaZiczGdjETQyfi0D1iaxP13pPa9O7_CaWAsklYmgiX_IDmfM8fuvHAnrwLhzeDoJiHdXcINak5B6mcvOJJGh64T-27FUlGUhUNiZEly6AEeTPjclUCSvbwrDBq2tTLiKG0o9h-rrGaCnkQXV4XPn3Hj2oKYeV6rasw1p0-Q70du-KLjfXiXGv5hDvkBB1FWAEtg4WIQCNcnSqnr7gxXfo9obu2gkLpnmTuLnH9rbaLnRFDD_KOxpX8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16417" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تعداد کشته‌های زلزله در ونزوئلا به ۲۶۴۵ نفر افزایش یافته است، به گفته وزارت اطلاع‌رسانی این کشور. همچنین اعلام شد که بیش از ۱۲۰۰۰ نفر مجروح شده و حدود ۱۵۰۰۰ نفر خانه‌های خود را در اثر این فاجعه از دست داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16416" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=Rs3Sv8guTRqcOwofjQuH0mCNaBvIxfLM2-YFH270I7qNNV3mzqxN0SWnstsvqyhFblUAOn8ygm4k3YAGj-Xt3ROHcQfCKXF_Qsk0eICOOCjn94znsg6VHvTTJrGx8JaVOTr_lkUUKYxKQC4Og6Q-ABPceJTa10H9F5y9WhyVgXpvR4sZZSIubE9DeQJNNJbczrU8Rhk_XOa1ieyr-M3EC0JKJmX_06eIgVu0g0X4GcN7HA2UI2KvcMPPUwB-j7l5o66XIvTnqERNQcl2wfwumqDsPcLJCliVkYFcbaW9TxrhYD-b18kg46wd7r0kZC0joRPal37eqrBeDcQelBvS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=Rs3Sv8guTRqcOwofjQuH0mCNaBvIxfLM2-YFH270I7qNNV3mzqxN0SWnstsvqyhFblUAOn8ygm4k3YAGj-Xt3ROHcQfCKXF_Qsk0eICOOCjn94znsg6VHvTTJrGx8JaVOTr_lkUUKYxKQC4Og6Q-ABPceJTa10H9F5y9WhyVgXpvR4sZZSIubE9DeQJNNJbczrU8Rhk_XOa1ieyr-M3EC0JKJmX_06eIgVu0g0X4GcN7HA2UI2KvcMPPUwB-j7l5o66XIvTnqERNQcl2wfwumqDsPcLJCliVkYFcbaW9TxrhYD-b18kg46wd7r0kZC0joRPal37eqrBeDcQelBvS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و قالیباف امروز
😁
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/16415" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16414" target="_blank">📅 23:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وای نت عبری : هزاران نفر در مراسم تشییع جنازه در تهران شرکت کردند، اما در اسرائیل این خبر خنده دار بود که "بسیاری نه برای عزاداری - بلکه برای اطمینان از اینکه او واقعاً مرده است، آمده بودند."
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16413" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">المانیتور:
مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16412" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=Nrx4-Jy6OvqJ3cbpojBwg9uUAH68Tcborb90IpqfxLWyZV0-VQYkZ_2s8zvDT7KabeGez748YeIlHnjmQsgbI4hwOtVy8xhymWnRkKBeMqNQnViDe29dehS6shp8ot_QeF0Qnn8-V9W-ZErGzqrzbIJakbnN_KFjfbRVrN7_U1Z4T2iolKH-H0c4DZspFIYmZz_6FpmN5-8K7mQAkK1gZ35xa9DL7OLMHxffiUQQyGm3Hp2ar6BsJEtnuWGLJaKMZvxTqjtASS0AfaTysACln5K9Dj9yrWDe-K2XXUZq34S7NmeBFnJXTcVAYdX_4UN4aJoXKiyzcxUpUfofKaZp7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=Nrx4-Jy6OvqJ3cbpojBwg9uUAH68Tcborb90IpqfxLWyZV0-VQYkZ_2s8zvDT7KabeGez748YeIlHnjmQsgbI4hwOtVy8xhymWnRkKBeMqNQnViDe29dehS6shp8ot_QeF0Qnn8-V9W-ZErGzqrzbIJakbnN_KFjfbRVrN7_U1Z4T2iolKH-H0c4DZspFIYmZz_6FpmN5-8K7mQAkK1gZ35xa9DL7OLMHxffiUQQyGm3Hp2ar6BsJEtnuWGLJaKMZvxTqjtASS0AfaTysACln5K9Dj9yrWDe-K2XXUZq34S7NmeBFnJXTcVAYdX_4UN4aJoXKiyzcxUpUfofKaZp7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمل پیکر علی خامنه ای در کامیون یخچال دار
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/16411" target="_blank">📅 21:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یورونیوز : در پی انتشار ویدیویی از زنی که با لباس زیر در پارکی در شهر یزد قدم می‌زد، مقامات قضایی جمهوری اسلامی از بازداشت عوامل انتشار فیلم و «برخورد قانونی قاطع و متناسب با رفتار آنان» خبر داده‌اند.
خبرگزاری دولتی ایرنا با متهم کردن این زن به «هنجارشکنی» مدعی شده که وی به «اختلالات شدید روانی» مبتلا بوده و بعد از بازداشت کوتاه اکنون وی به آغوش خانواده‌اش بازگشته است.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16410" target="_blank">📅 20:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
ترامپ امروز با نتانیاهو تلفنی صحبت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16409" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16408" target="_blank">📅 20:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تکذیب خبر نیویورک‌تایمز درباره ترور مقامات ایرانی از سوی دفتر نتانیاهو
حساب رسمی نخست‌وزیر اسرائیل در شبکه ایکس نوشت:
«طبق معمول، آخرین گزارش نیویورک تایمز درباره اسرائیل و مذاکره‌کنندگان ایرانی، خبر جعلی است. یک جعل کامل واقعیت.»
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16407" target="_blank">📅 19:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صفحه‌ فارسی وزارت امور خارجه اسرائیل در X:
واقعا توی اون تابوت چی‌ گذاشتن؟
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16406" target="_blank">📅 18:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حوثی‌ها ادعا می‌کنند که با هواپیماهای سعودی در آسمان یمن درگیر شده‌اند، به منظور جلوگیری از فرود یک هواپیمای غیرنظامی ایرانی در پایتخت صنعا. حوثی‌ها اعلام کرده‌اند که هرگونه حمله سعودی دیگر، "با حملاتی به فرودگاه‌ها و منافع حیاتی در عربستان سعودی پاسخ داده خواهد شد."
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16405" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16404" target="_blank">📅 18:51 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
