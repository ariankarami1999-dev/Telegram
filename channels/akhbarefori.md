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
<img src="https://cdn4.telesco.pe/file/Jx89lhYv5oG-8bZc6YxvVyFZS09K52PAJ0wE6dVsAmjr3E-OJQf95fRsheSoai4WNlYJxQSQe6m5onuPjOaQ8WwCn5AVAYyOnucHM79zGQ3mZOZzCBGgylDSv3U2nP6NoP6WbE_uGDb_Q3kS46THm_OsqvEjMygqjoG61IT3L_gz8uSPcF3-ITxILdFumLwKLGonrj0tg8DJRHxAZ3cAX3N01MkhSzkmQTBXAybUfq0gATpNVKxgzDB7m7BcAeqHnsKUioIbTMBEDVOvgaou9W5t0rs2birIqdF6FjvGob_1inBAyimuA4_JUbxq1B0IYJA-LMqgMOEXF417OHLlhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-655493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee5d44296.mp4?token=v0ns2Xk8jf3f3XyLQOE7iUHZZg73RkMnrditIbEoiY5cj1wv55lKhR15shR3hEJvh2rQJUjtAwqIOZ1itdJ9ahePq0Wyvzz-XPrRvq0UiEjBhBqAvThE37HL7NvGnEPLKWkJtHZj-mn34JqPqfNc03MmbGB52bU73OBrgiiy7O88kot5IA_fAP-8PnNK-q6JM7mJFvuAu2okhKaa-xjCqkjhnpYPRRf8ZV0s4UGnY73tCClLOH9JbzYmpskwnvQgH9GWLj1MOqfvg-mvM6Nr5AQUK7yNc0VThAWA321uZSX9HX86sgKaHwmRaiu4fGkl6DuijH5NKV7Ec5HKons9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee5d44296.mp4?token=v0ns2Xk8jf3f3XyLQOE7iUHZZg73RkMnrditIbEoiY5cj1wv55lKhR15shR3hEJvh2rQJUjtAwqIOZ1itdJ9ahePq0Wyvzz-XPrRvq0UiEjBhBqAvThE37HL7NvGnEPLKWkJtHZj-mn34JqPqfNc03MmbGB52bU73OBrgiiy7O88kot5IA_fAP-8PnNK-q6JM7mJFvuAu2okhKaa-xjCqkjhnpYPRRf8ZV0s4UGnY73tCClLOH9JbzYmpskwnvQgH9GWLj1MOqfvg-mvM6Nr5AQUK7yNc0VThAWA321uZSX9HX86sgKaHwmRaiu4fGkl6DuijH5NKV7Ec5HKons9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشتی حنظله ۲ حرکت خود را برای شکستن محاصره غزه از سر گرفت
🔹
کشتی «حنظله ۲» در ادامه سلسله‌اقدامات بین‌المللی برای شکستن محاصره دریایی نوار غزه، سفر خود را از پایتخت سوئد از سر گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/655493" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7306ca33dd.mp4?token=kIpB6VoiorbNYh1MLTdELbJyKnLyUkvE9_tC5UMlAUMWaw7j2hdU7QmYxtYALnpvwlm32qkiYCi0C-dfGLzqznjeWsGPaI_lFeFG8qFM_IieXBSwXcSVTomw_aQdrMG41kCiYQJNKqcpG-gRDpTky65AVkkFTGRvfmFkQcuTsSMUUmgwdGOuGqCTB5Amb6PnX5d9w0axoVkyRdc8tBAVv58jChHeh2sJTUWv-p1V2anREM51a7qwG-hmYx2t0LkV1lYq70JbK2FR0FloUBt_6pA7uHm4WB5ItDoWjlPHUllcBNYVizsX4DU0ixEeqHxGEuBUVmBMDWdLNlJdfQdQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7306ca33dd.mp4?token=kIpB6VoiorbNYh1MLTdELbJyKnLyUkvE9_tC5UMlAUMWaw7j2hdU7QmYxtYALnpvwlm32qkiYCi0C-dfGLzqznjeWsGPaI_lFeFG8qFM_IieXBSwXcSVTomw_aQdrMG41kCiYQJNKqcpG-gRDpTky65AVkkFTGRvfmFkQcuTsSMUUmgwdGOuGqCTB5Amb6PnX5d9w0axoVkyRdc8tBAVv58jChHeh2sJTUWv-p1V2anREM51a7qwG-hmYx2t0LkV1lYq70JbK2FR0FloUBt_6pA7uHm4WB5ItDoWjlPHUllcBNYVizsX4DU0ixEeqHxGEuBUVmBMDWdLNlJdfQdQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💚
پک استوری ویژه عید غدیر
💚
#عید_غدیر
#استوری
#امام_علی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/akhbarefori/655487" target="_blank">📅 17:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VERXBh0ZKalVS0akxHDFSs9w_NsG0AuPcOOAGxBCpjWbOsInCUkx_YRIc7emB1SDWIXPSGz1eLWWgPColuM-j7Vg1lKJExdf8-_s3zKSHSQMFeIUZwJxlj79E-naWF5q_fXZTiY6d7v38WIvXmqOvFDdyF4XRxJqgz4OR9qat2qapqY5Dkb9TFbZni8SxTAf_FIg4tVXJnZw3nybrAUVd3Q6S_D5aiMowVKXPVrJEXGMUR3V2_rG5Gxmkv42rAd8jcJIJqO7uaz_brHvh660pAY8KcFr1bCenoxftuFuG0xT7RvOu7ajoXuOziqmxkhzUS4GDXZywl7XEsOuRUI51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ویلیام پولت به عنوان مدیر موقت اطلاعات ملی خدمت خواهد کرد
🔹
تولسی گابارد در پایان ماه جاری میلادی از این سمت کناره‌گیری خواهد کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/655486" target="_blank">📅 17:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
روایت فوربس از قابلیت جدید ایران برای مقابله با آمریکا
فوربس:
🔹
متحدان حوثی ایران در یمن می‌توانند با هدف قرار دادن احتمالی تنگه باب‌المندب، آبراه حیاتی متصل‌کننده اقیانوس هند به دریای سرخ را ببندند.
🔹
گرچه ایران با تنگه باب‌المندب هم‌مرز نیست، اما حوثی‌های یمن با آن هم‌مرز هستند و می‌توانند آن را تهدید کنند.
🔹
طبق گزارش آژانس اطلاعات انرژی آمریکا، روزانه ۴.۱ میلیون بشکه فرآورده‌های نفتی از طریق این تنگه عبور می‌کند.
🔹
باب المندب، که پس از عبور از کانال سوئز در مسیر دریایی به آسیا واقع شده است، جدا از نفت، حدود ۱۲ درصد از کل تجارت جهانی را به خود اختصاص داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/655485" target="_blank">📅 17:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt1SSiO-8hJl4imBY9whSdvSmfh7DAOosCZVLaMfq2-tlmt1TZHOdHhz6vNWRCtryp6LU9i2M9IMmDleFZnhyI5CqBOdYhsqMwgyKP8LDB6iJGM2QM6uaf4Oe5wWJsDD2rAekP87M3W7fJqpmib-UeJtLW2r8VbXM6fSmYOqdAY4Fa_4G-WOKp0fH6dDufbXu1C6-X9xfZn5bKrbKF-P0_xkmF86iZTovVWjopE98dz9sFDXXkzy7quu5GxUAB1hKyDZqDfA_Tm5X_7AL5zsjBwxtgrBLfK88QYX7BwjlpjLozWR20IbnMblBGR_PEenv3LU2A9gZpsKloSgG5hcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کیم کارداشیان می‌تواند رئیس جمهور آمریکا شود؟
🔹
در سال‌های اخیر، نام کیم کارداشیان نه‌تنها در دنیای سرگرمی، بلکه در حوزه مطالعات فرهنگی و رسانه‌ای نیز وارد شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219908</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/akhbarefori/655484" target="_blank">📅 17:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به چالش‌های کم‌آبی، آیا راهکارهای کاهش مصرف آب در خانه را پیاده‌سازی می‌کنید؟</h4>
<ul>
<li>✓ بله، اقدامات متعددی انجام داده‌ام</li>
<li>✓ صرفاً در حد رعایت عمومی (مثل بستن شیر آب هنگام شستشو)</li>
<li>✓ تصمیم به تغییر الگو دارم، اما اطلاعات کافی درباره روش‌های بهینه‌سازی خانگی ندارم</li>
<li>✓ مصرف من در حد استاندارد است و تغییر خاصی در رفتارم ایجاد نکرده‌ام</li>
</ul>
</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/akhbarefori/655483" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5fb0ee7.mp4?token=OJiNHDsKpHLTcvpppA3V0yMKMmzwFyxA8xE6bWul5VXKrMPBmsoU9NqfesBhrRHdN8Htt5h2AsbW1AvawKzizw6-Hp5r_pf5GEkyO3QwHK_95lotOEIDYpkFLv55nXbVrrJPDyOpHNaEv3Z0__kmqnq7dB2MSeMa-uxASt1Q7M9p_YEIcO2k8fHw4fCEyzeCo7QdR0WOSm46hAxbLeu897t1OjwvLzgfXrlqlKcjqF3FuubkzvKDrNeWsD5twuf7P8pBMo5-SKd07GmhEyEHY-K1Mic3ZFaYmGiU2aKQSjAtAPxs14fRB4vh8ioEXnzZWhNODfWu7YDGfHm8MJdA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5fb0ee7.mp4?token=OJiNHDsKpHLTcvpppA3V0yMKMmzwFyxA8xE6bWul5VXKrMPBmsoU9NqfesBhrRHdN8Htt5h2AsbW1AvawKzizw6-Hp5r_pf5GEkyO3QwHK_95lotOEIDYpkFLv55nXbVrrJPDyOpHNaEv3Z0__kmqnq7dB2MSeMa-uxASt1Q7M9p_YEIcO2k8fHw4fCEyzeCo7QdR0WOSm46hAxbLeu897t1OjwvLzgfXrlqlKcjqF3FuubkzvKDrNeWsD5twuf7P8pBMo5-SKd07GmhEyEHY-K1Mic3ZFaYmGiU2aKQSjAtAPxs14fRB4vh8ioEXnzZWhNODfWu7YDGfHm8MJdA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتسب به آیفون اولترا طراحی اولین گوشی تاشو اپل را نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/akhbarefori/655482" target="_blank">📅 16:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دستور پزشکیان؛ برق صنایع به هیچ عنوان قطع نشود
آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
مدیر عامل توانیر هفته گذشته گزارشی را به دبیرخانه شورای سه قوا ارائه کرد مبنی بر اینکه امسال در زمان‌های پیک ۱۲ هزار مگاوات کسری برق داریم.
🔹
سال گذشته ۲۲ هزار مگاوات بود که امسال ۱۲ هزار مگاوات است که نسبت به سال گذشته ۱۰ مگاوات کسری برق کمتری داریم. نزدیک به ۷ هزار مگاوات نیروگاه خورشیدی در مدار است.
🔹
رییس جمهور هفته گذشته در اتاق بازرگانی دستور دادند که به هیچ عنوان برق صنعت قطع نشود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/655481" target="_blank">📅 16:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip-OxPqtXaXawhMPPINUTA7jU1_n67ocduFYehIZOEs1iSYBCJU8B57b0jWQrblASzTxZHfFAhfjEgkmJ7om3doivPZ_5s41JmLTIJ78zeYXwbpu1rXBuORLw7oPIyyk5PPM_AKjoK6GeDeKV8t-e_H352O0YLMVO04lAGNPIL882hJTdaauejvWsji0OcizWBv6bmRRyCZC1HuL_Fnfxvzt52yLp9tKJShib7Euph2C5J8PpyocY6ILw5kP5OHnI0-o2vM2q9n4jaCUF_4XW-h80H_T6uzMdu1r6hgIpEtmgHFzIuPCOcZMQjOizI_pLIZ13kgnGF6s0Q64Sl7BFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده کنگره آمریکا: مفقود یا کشته شدن ۱۱ دانشمند ما تصادفی نبوده و بسیار نگران‌کننده است
🔹
جیمز کومر: ببینید، آنچه در ایران می‌گذرد به قابلیت‌های هسته‌ای مربوط می‌شود و این که آمریکا نمی‌خواهد ایران به سلاح هسته‌ای دست یابد. ما به‌وضوح رهبر بلامنازع…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/655480" target="_blank">📅 16:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc6VGtu41Rb0VzA0rXsVnE3Gj_sddhFX_B6k6v4ZSGsKXV0nsVSjbgNwg5nUyXW2sjTFyO_mcI9vldoG3_G2g6ILK_1uyJSU0ejujTcukhUmlXNH2SLL4cqqntpuGJuXdjDb-BPbC-V1EBcqJxBXS2W9U4Lc_tfWRnsLJaoWjjygOb1qBmZ0DUN4ZfSBbZw0tz3AmXsVjzHdBByZh-KpBUZw3C15tK-vQT8zl4qypDlIvIEmdVcIgeKwV6tXuhwDjysTbpCXEwo0JDlV6-gW4iJkfKah8hs0ZEL8rtCjTwHyFJccervvddmnedD9oca46eXRjBcaJW67SI9i0R5qVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: ۷۰ کشتی با کمک آمریکا از تنگه هرمز عبور کردند  یک مقام رسمی به نیویورک تایمز:
🔹
فرماندهی مرکزی ایالات متحده در سه هفته گذشته به عبور حدود ۷۰ کشتی تجاری از این تنگه کمک کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/akhbarefori/655479" target="_blank">📅 16:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea08292349.mp4?token=JcNI8hxUZSDd1rtR718zxKtC87c6DcxRDpYHETeh356qQ0GD6bDrs4UBt3S_7lci5UYztuZoHfo7CLXQRYCZJrM_DfnZvEi8dhlIrXdHAQ9b11UNhLmTnypaA7HtFo6qB5xLKZOPy_oZImjIE3WxwCgw3B896NMEW1svrB2ET7Fh1nq5GhWa2o7GIDtiVjm4geFWm1REdKvMwhQx8e6X8AebztLmTNOZOIoHu7KQjYDkAJAOhnuvTdMBNH8sK3lS6vTg7HIyGyEzgrQ4e61ReyaXfVJyWOYa-UXX3hdHTF-YFkAI7uUbbpc8VBlUMJ5nTIujG0YFZadu2y3Eu1-5Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea08292349.mp4?token=JcNI8hxUZSDd1rtR718zxKtC87c6DcxRDpYHETeh356qQ0GD6bDrs4UBt3S_7lci5UYztuZoHfo7CLXQRYCZJrM_DfnZvEi8dhlIrXdHAQ9b11UNhLmTnypaA7HtFo6qB5xLKZOPy_oZImjIE3WxwCgw3B896NMEW1svrB2ET7Fh1nq5GhWa2o7GIDtiVjm4geFWm1REdKvMwhQx8e6X8AebztLmTNOZOIoHu7KQjYDkAJAOhnuvTdMBNH8sK3lS6vTg7HIyGyEzgrQ4e61ReyaXfVJyWOYa-UXX3hdHTF-YFkAI7uUbbpc8VBlUMJ5nTIujG0YFZadu2y3Eu1-5Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور ترید کنیم تا همیشه ضرر کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/akhbarefori/655478" target="_blank">📅 16:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تبادل پیام میان ایران و آمریکا فعلاً متوقف شده است
یک منبع آگاه:
🔹
در حال حاضر تبادل پیام میان ایران و آمریکا متوقف شده و دست‌کم چند روز است که هیچ پیامی در چارچوب دستیابی به یادداشت تفاهم اولیه میان تهران و واشنگتن رد و بدل نشده است. این در حالی است که برخی رسانه‌ها و مقام‌های غربی تلاش دارند روند ارتباطات میان دو طرف را عادی و فعال نشان دهند.
🔹
برخلاف ادعای اخیر رئیس‌جمهور آمریکا مبنی بر اینکه گفت‌وگوها با ایران با سرعت بالایی ادامه دارد، آخرین پیام جمهوری اسلامی ایران به واشنگتن، پیامی صریح درباره لبنان بوده که بازتاب گسترده‌ای در سطح بین‌المللی داشته است./ فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/655477" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جام جهانی ۲۰۲۶ با قوانین تازه از راه می‌رسد
فیفا چند تغییر مهم را برای مسابقات جام جهانی ۲۰۲۶ در نظر گرفته است:
🔹
پوشاندن دهان با دست، بازو یا پیراهن هنگام بحث و درگیری با سایر بازیکنان یا داور، می‌تواند با کارت قرمز همراه شود.
🔹
اوت باید ظرف ۵ ثانیه پرتاب شود؛ درغیراین‌صورت توپ به تیم حریف واگذار خواهد شد.
🔹
بازیکن تعویض‌شده فقط ۱۰ ثانیه فرصت دارد زمین را ترک کند؛ در صورت تأخیر، بازیکن جانشین با یک دقیقه تأخیر اجازۀ ورود پیدا می‌کند.
🔹
در هر نیمه یک وقفه ۳ دقیقه‌ای برای نوشیدن آب (حدود دقیقه ۲۲) در نظر گرفته شده است.
🔹
هنگام مداوای دروازه‌بان در زمین، بازیکنان اجازه ندارند کنار زمین بروند و از مربیان دستور تاکتیکی دریافت کنند.
🔹
سرمربیان می‌توانند در زمان توقف بازی از لپ‌تاپ و تجهیزات الکترونیکی برای انتقال نکات تاکتیکی استفاده کنند، اما بازیکنان باید داخل زمین بمانند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/655476" target="_blank">📅 16:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ساخت «اخراجی‌های ۴» پس از بهبودی حال اکبر عبدی
مسعود ده‌نمکی، کارگردان سینما و تلویزیون در
#گفتگو
با خبرفوری:
🔹
با توجه به وضعیت جسمانی آقای عبدی، فعلا ساخت و تولید مجموعه جدید اخراجی‌ها به تاخیر افتاده است. بخشی از کار به وقایع اخیر برمی‌گردد اما این‌طور نیست که بگوییم کلیتش در ارتباط با جنگ است.
🔹
پس از مساعد شدن وضعیت حال آقای عبدی، در مورد کار تصمیم‌گیری می‌کنیم. آقای عبدی از بخش عمومی برای ادامه درمان در خانه هستند و حال عمومی‌شان بهتر است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/655475" target="_blank">📅 16:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc8KeshBA7yLpYDpsi3b6lmlSVQPtfAC9-8Oze_3iXEBH2ldn3BMB68yca6BHi3JU7lz845gJURz9Oy9mZXpfdT16PL8stZyjddipDj3ECscJJsNGKvf_ROVI6jEj5KDDbu3orm5F7rsZ7tx6dk2Z2HjA0-SiWHY50e0gmAkm9lXOiWLaa_A6kCM7RCMjIx5RYeJ7rDQjBCX93TZ7qmHby5y_Zi_xoMEzH48I3kB70fy9cyRRxy04QanV9HOZNG1S85MmHSaJp4f8kg-xHXKHw_oInFX2fbCHX3uAo5gPVpvqRYqjUz4Ct6KTa-j3hM1lr9LKrWeKgestCLk4eq-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی AI حقیقت را فدای مهربانی می‌کند
🔹
طبق نتایج یک پژوهش جدید، چت‌بات‌هایی که برای پاسخ‌های دوستانه‌تر و همدلانه‌تر تنظیم شده‌اند، در برخی آزمایش‌ها تا ۶۰٪ بیشتر از مدل‌های معمولی اطلاعات نادرست ارائه کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/655474" target="_blank">📅 16:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac4a7e999.mp4?token=cTW1J3e4rToS4krhXX8jKXUcQ-SxEsFHd8D76-DTAjta7cfqeT3Zkp0gjwWQqSc5bkfk8j3vBSDwba3oMY3c2Q_WhL1siYKknb4VTqDg4qorJsH9jMkJTS6vwrZS1mGcPC2pC3keKoCwOf4-un923wXrtkzMrq5pegcIDherTLyku5Yxt6mPZqdu2GPlv-QeSQLFjgL_N0fISgvofhCgVpLEGymu73dDJAmewXQrcfJjo6BuVQtmAxqGbWKik9oeEOhMT-oi1BlYqyFTbc2FwyAep3aiSFH23cXr95qHVk3AOYPiu3Wqps2gPDpmQ7wmN3tegy3WkBIWa1dHDJJQpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac4a7e999.mp4?token=cTW1J3e4rToS4krhXX8jKXUcQ-SxEsFHd8D76-DTAjta7cfqeT3Zkp0gjwWQqSc5bkfk8j3vBSDwba3oMY3c2Q_WhL1siYKknb4VTqDg4qorJsH9jMkJTS6vwrZS1mGcPC2pC3keKoCwOf4-un923wXrtkzMrq5pegcIDherTLyku5Yxt6mPZqdu2GPlv-QeSQLFjgL_N0fISgvofhCgVpLEGymu73dDJAmewXQrcfJjo6BuVQtmAxqGbWKik9oeEOhMT-oi1BlYqyFTbc2FwyAep3aiSFH23cXr95qHVk3AOYPiu3Wqps2gPDpmQ7wmN3tegy3WkBIWa1dHDJJQpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شست‌وشوی ضریح علوی در آستانۀ عید غدیر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/655473" target="_blank">📅 16:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USH1y8DBK50am_29FpOpgE6rhfBgf0vZLi2SJcH_l1gA_LM_EdwJ9fIKffppwdo9vU6GGRmAh404MWyxNwBtSWD_6JNoIq0t_rSvK4tDWo3_xt1ogAPuesyIJDa1MGnJ32JdZaaVEemMvpwdvtSTIQxCXvH5kUyzectqTfPm199ITBB7fFSbUV-flThJZUckfXOZUtK2jYiLXqIeHAkqGPXwxFP0MapH7yDdK_baY4jKX6122fXPijmg_2ZYfcbvZfmb8VJCSAncrinaCL_XPeXlYknlN51liQII3a04sz64EQ7DMYwI6cevbh-CYF5rA2biT-6AAc-3qqCA15RWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت باشگاه سپاهان: برای اخذ مجوز حرفه‌ای، ‌مدارکمان را به کمیته بدوی AFC ارسال کردیم
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/655472" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
معاون شهرداری تهران: تشییع پیکر رهبر شهید در سه شهر تهران، قم و مشهد قطعی است؛ در حال تدارک برای جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در پایتخت هستیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/655471" target="_blank">📅 16:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG1y3e2aWr9Ur3nONKTxVa-5EWwRfUeL8qaFRmiNa6pVAjxd2M52tutQjCPwnYfsNYjFJuyhFF7yuzxvtTgYatyMzVCe3Hz1-LFbLZP4opOBloOGNSHTGJ5N-bM-b1GYcjYDFsHgdg8rqyv_vd5dooXha_U-t6hgDjEgf-Ud0iOV_Zte6wouomAX6euIaNz_81CEudxIP-5nHDMSg8ENUNo8ugHVpusf3udyLnpjis06Xnu71C75exOKmRWA4aWXWPM56UBrFAr1KThmOEDZCMAyzloVqJ3hMdCwE7f4D6wtx938nrjs4yVdmRK5w9U_g7xHPTI-uhyJnZxOQyYlVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سود هنگفت سوریه از جنگ آمریکا با ایران
رویترز:
🔹
جنگ ایران در منطقه، آسمان سوریه را دوباره به شاهراه هوایی خاورمیانه تبدیل کرد. در ماه می، ۱۱,۸۰۱ پرواز از حریم هوایی سوریه عبور کردند که بیش از دو برابر فوریه و جهشی ۳۷۵ درصدی نسبت به سال قبل است.
🔹
آسمانی که در طول جنگ داخلی ۱۴ ساله سوریه منطقه ممنوعه بود، اکنون به مقرون‌به‌صرفه‌ترین مسیر برای خطوط هوایی منطقه‌ای تبدیل شده است.
🔹
دولت جدید سوریه نیز با دریافت ۴۹۹ دلار از هر پرواز، ماه گذشته نزدیک به ۶ میلیون دلار درآمد داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/655470" target="_blank">📅 16:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piZhbq0b_QKxGJpfvll5d1zNWsug6MAb5RwObr5nAiTpYsiBvHW3FwQvTjWj1s7F2ym2GKYj2EBxPv4Wav4dkqYj5v8XhO-JH7rwMYJLPN6fVSczqUDRqBu7Q-Km40lQd1NG84rwqsdiOV1KeA1FGu2xK6DWOtIrpTqpiNDg16ORFfGsjfbFBD1-8Cg9DaOCbLlfM77lwUyK6ccMOWNczow-5X4PZYHEXzRLCFnyp7bBXiQYZy0ifXNjbcUQvQbVwVF3U2t_px5bfR4UTJqpzXPXTiUkOqRfJyLEseCTzWMGXuokbcIGCuFzxuwsZHqcNC_AsokMvQ5v4YFRQD551A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/
نوشهر
📍
چلک
۵۰۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۵
استخر روباز و استخرداخلی
شمالی-جنوبی
چشم انداز جنگل و دریا
سند تکبرگ و مجوز ساخت
دسترسی عالی تا دریا
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/655469" target="_blank">📅 16:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=m_1cRd9l4nC_ej6l5ozjN5xJiLGnn3SkRUV4guFFLiDyGKEoxDldB6bfe9MhdYezypXmnkzDrgesMNOEY3HZFEc5Qk5THL5MXwKAx_0KOTUzd-oOWrZXYKTO22x_BcGGaj0ThyG85vWCAKjFPdtiStQoxTp0blLTR889aValjhZdohDIo9323nuaLoYc2zFXpZ8pymEi2_U9tQj1MKj-PB99YwufjE6rGGjOBs1AG9nETcMCwjvbbWCK7_6kIX84oxlpKVVymYUr3KF7GDjdc0MQAKvjLfZgX4MiXvj_PwcU5Xo0vUox15-V5agL3QeAzKxKbpu8-APQCRH_jxPMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6192aa3cc.mp4?token=m_1cRd9l4nC_ej6l5ozjN5xJiLGnn3SkRUV4guFFLiDyGKEoxDldB6bfe9MhdYezypXmnkzDrgesMNOEY3HZFEc5Qk5THL5MXwKAx_0KOTUzd-oOWrZXYKTO22x_BcGGaj0ThyG85vWCAKjFPdtiStQoxTp0blLTR889aValjhZdohDIo9323nuaLoYc2zFXpZ8pymEi2_U9tQj1MKj-PB99YwufjE6rGGjOBs1AG9nETcMCwjvbbWCK7_6kIX84oxlpKVVymYUr3KF7GDjdc0MQAKvjLfZgX4MiXvj_PwcU5Xo0vUox15-V5agL3QeAzKxKbpu8-APQCRH_jxPMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تازه‌ترین تصاویر از تنگهٔ هرمز
و کنترل ایران بر این آب‌راه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/655468" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPJhRWum5FHFhLdhk2Q2-qs3wd_GB08x7b1RJvMD7cwgTqqmdBcbLWaLsC34Z_zaGVCz46buhQ2TTb0DmLZRDBsW3-IvElTmp8zfHRVyOfvHOvfBvfC0mE8VSrZ4386Tc7mfowF3ZxXbE3m2TSqZ9lJ2pR-3e5-6rG8cfgmI3Y-_1VjbmNQ3G4kDDCAzcGTc7yZjdPJvO0XamUPV5vqTWgIZ8Tt1ePMwPOuHw-oJBP0V3Zf6wtJwlgI6u-RDYQPT1m8_8ZbO9NMzYGc7yU6wluJI6FNhAlblVxt3_vQRJs8-HF3DK4a2bejHusJD316QSVmOJhxKvTy1BZf1-61JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پر باران‌ترین شهرهای ایران در بهار امسال
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655467" target="_blank">📅 15:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655466">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حماس: آماده واگذاری اداره غزه به کمیته ملی هستیم
حازم قاسم، سخنگوی جنبش مقاومت اسلامی (حماس):
🔹
این جنبش آمادگی کامل برای واگذاری اداره نوار غزه به کمیته ملی مورد توافق را دارد؛ آنچه مانع فعالیت این کمیته می‌شود، رژیم اشغالگر و نیکولای ملادینوف، مدیر اجرایی شورای صلح است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/655466" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655465">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
جزئیات ادعایی نیویورک‌تایمز از پیش‌نویس توافق تهران و واشنگتن
نیویورک‌تایمز:
🔹
در این پیش‌نویس، نوعی توافق عدم‌تجاوز با توقف ۶۰ روزه درگیری‌ها قرار دارد که در صورت پیشرفت مذاکرات، قابل تمدید خواهد بود.
🔹
واشنگتن می‌خواهد تنگه هرمز فوراً بازگشایی شود، اما تاریخی برای لغو محدودیت‌های باقی‌ مانده علیه ایران تعیین نکرده است.
🔹
احتمال ایجاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری برای ایران که به‌عنوان بازسازی پس از جنگ مطرح شده و در صورت نهایی شدن توافق، آمریکا به راه‌اندازی آن کمک خواهد کرد.
🔹
با این حال، مسائل زیادی هنوز حل‌ نشده باقی مانده‌اند؛ از جمله جدول‌های زمانی، سازوکارهای اجرایی و شکل نهایی توافق./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/655465" target="_blank">📅 15:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655464">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
مرگ مرموز پیرمرد پس از درگیری با داماد سابق؛ تحقیقات جنایی آغاز شد
🔹
پس از فوت مشکوک مردی ۶۷ ساله به‌دنبال درگیری با داماد سابقش، پرونده‌ای جنایی در این خصوص باز شد. دختر متوفی مدعی است که در روز حادثه، همسر سابقش به پدر او حمله کرده و ضرباتی به وی وارد کرده است؛ ساعتی پس از این درگیری، پیرمرد هنگام تعویض قفل در ناگهان جان باخت.
🔹
با شکایت این زن، بازپرس جنایی دستور تحقیقات تکمیلی را صادر کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/655464" target="_blank">📅 15:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655463">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e270db2232.mp4?token=IfZJibbbg_u6nJd6u0VVxbkUDwIgfRioU5vWSGTkQMyRLklD-3ZxkqTrttLInS5QgxMxL8AOTGo__nxP592x4PWXQ1OnGN30IAQ_Z9hKIJ8Qnk_856hUdI44i2iAcEW109JGryROIv2SFLGHP4Djy3TBV1b7OZ5hIhh5qI8AOGbGVrEYSSz1HyaeHx-EvLqChNELIEIrGbgtAa2rHxnXIdnw1qRuVlTqFuLC-hguH970NDzgdbG0Hoz1ZDomg3JI5WP54Cxf1yYxbMFIppZAF4a9mcUkZgMnYJcl08S52mK0BQuFreugX-7ymKGTwLB9reV7pMY0QdcBo8EfJK3HZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e270db2232.mp4?token=IfZJibbbg_u6nJd6u0VVxbkUDwIgfRioU5vWSGTkQMyRLklD-3ZxkqTrttLInS5QgxMxL8AOTGo__nxP592x4PWXQ1OnGN30IAQ_Z9hKIJ8Qnk_856hUdI44i2iAcEW109JGryROIv2SFLGHP4Djy3TBV1b7OZ5hIhh5qI8AOGbGVrEYSSz1HyaeHx-EvLqChNELIEIrGbgtAa2rHxnXIdnw1qRuVlTqFuLC-hguH970NDzgdbG0Hoz1ZDomg3JI5WP54Cxf1yYxbMFIppZAF4a9mcUkZgMnYJcl08S52mK0BQuFreugX-7ymKGTwLB9reV7pMY0QdcBo8EfJK3HZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده جرقه‌های قرمز مرموز بر فراز آسمان تبت
🔹
جرقه‌های قرمز، پدیده‌ای نادر که در ارتفاعات بالای طوفان‌های تندری شکل می‌گیرد و تنها چند میلی‌ثانیه دوام دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/655463" target="_blank">📅 15:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655462">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سازمان هدفمندسازی یارانه‌ها: بخش اول مطالبات گندم‌کاران به حساب کشاورزان واریز شد
🔹
در این مرحله ۵۰ همت از حدود ۱۱۰ همت مطالبات گندم کاران پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/655462" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655461">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">معاون شهرداری تهران: برگزاری مراسم تشییع پیکر رهبر شهید در عراق در حال بررسی است</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655461" target="_blank">📅 15:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655460">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون
شهرداری تهران: برگزاری مراسم تشییع پیکر رهبر شهید در عراق در حال بررسی است
🔹
روسیه:‌ انتقال اورانیوم غنی‌شده ایران به خارج از کشور ضروری نیست
🔹
زارت کشور بحرین سفر شهروندان خود به ایران و عراق را تا اطلاع ثانوی ممنوع کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655460" target="_blank">📅 15:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36b489d38.mp4?token=CTfkCa8YWwa40_8-WeG4JuWDzGiji07F2XyIKSf2OpXvKN0Gq2oA4mTvhzOBfq_jQ4y4WGTo67sgQp_rAlgmkyF_NqKQP0q6AH1KTxgNfh4-QJRGwzsjFTvqnMjTR_NoGPwfWrb_zgP0dGjvvqcMh88Hn56kkM8cQe5Ph5w_FycpGF-FRaaZN-vjavipy-BCL1X-oK-A_EhvmvcEuCel1VEWLJCZ1jQP2vXKsjbKjvyFm29wkR6IQjxJ6BeNEBiUKQS5A4aXGhPIzVr6725DLpxDsR6whM7oGaNY2N6d6JARSPLG7encRIK7GwTvgUpvzhPF5vtM2lZgIBBwnHDSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36b489d38.mp4?token=CTfkCa8YWwa40_8-WeG4JuWDzGiji07F2XyIKSf2OpXvKN0Gq2oA4mTvhzOBfq_jQ4y4WGTo67sgQp_rAlgmkyF_NqKQP0q6AH1KTxgNfh4-QJRGwzsjFTvqnMjTR_NoGPwfWrb_zgP0dGjvvqcMh88Hn56kkM8cQe5Ph5w_FycpGF-FRaaZN-vjavipy-BCL1X-oK-A_EhvmvcEuCel1VEWLJCZ1jQP2vXKsjbKjvyFm29wkR6IQjxJ6BeNEBiUKQS5A4aXGhPIzVr6725DLpxDsR6whM7oGaNY2N6d6JARSPLG7encRIK7GwTvgUpvzhPF5vtM2lZgIBBwnHDSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوانندگی آقای مجری در پخش زنده شبکه سه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655459" target="_blank">📅 15:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رای دیوان عدالت اداری برای تعیین محاسبه کسر قیمت وسیله نقلیه در اثر حادثه
🔹
هیات عمومی دیوان عدالت اداری تبصره ماده ۶ دستورالعمل نحوه محاسبه قیمت وسیله نقلیه را که محاسبه کسر قیمت خودرو در هنگام حادثه را منوط به حداکثر ۱۰ سال از ساخت خودرو کرده بود ابطال نمود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655458" target="_blank">📅 15:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تله بزرگ در پلتفرم‌های درج آگهی
🔹
در برخی پلتفرهای درج آگهی، کلاهبرداران روش جدیدی یاد گرفته‌اند که به راحتی کاربران را فریب و جیب آنها را خالی می‌کنند.
🔹
جزئیات را در این ویدئو بشنوید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655457" target="_blank">📅 15:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655454">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ثبت بیشترین ارزش معاملات بورس در سال جاری
🔹
شاخص کل بورس امروز با جهش ۴۴ هزار واحدی به ارتفاع ۴ میلیون و ۳۴۴ هزار واحد رسید و شاخص هم وزن هم ۱۰ هزار واحد بالا آمد. ۶۱ درصد نمادها امروز سبزپوش شدند.
🔹
اما هیجان اصلی جایی است که حقیقی‌ها ۴.۳ همت پول تزریق کردند، ارزش معاملات خرد به ۲۸.۵ همت رسید و صف‌های خرید ۲۰ همتی بسته شد. با این حال، صندوق‌های درآمد ثابت با خروج ۱.۱ همتی نقدینگی مواجه هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/655454" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655453">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شبکه اجتماعی لینکدین رفع فیلتر شد
🔹
شبکه اجتماعی لینکدین پس از بازگشایی تدریجی اینترنت بین‌الملل، بدون نیاز به فیلترشکن در دسترس کاربران ایرانی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/655453" target="_blank">📅 14:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655452">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAzRqGSg54pz6K4vJ81aYvBjqwf8DeCnSsE4mLdIQUp5JSoBywstckF5lc5xskwNfSs25srzWQDWmNevPnCxJfsNvnBDndrusBBfkUj5jXx9WhGCOdeKKtj7TiwoLww7oOaHI-Sxou0GAQ1YC1b6ikZNig8ymkJhwYrp8kdlsxrjLtp-CKbl0xW1yCqeb0R1PrQgQa2xb_hjjJ8mnoXGeScv4-pvjlcBcbJUO8Y1yDoPJ71am4szke5fdSnyXyY9d7nkAwCIjARBbPd-sdr-Dwx0hFVRSFsNVx6JNXOt6IlaNerObLAYQ3Vt55ojUIhqJTqgL_gQRrzg_XVqiFbDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰۰ بازیکن برتر حاضر در جام جهانی از دید رسانه فاکس
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655452" target="_blank">📅 14:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655451">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTD7wiSTNO7O2eZywLB1odL1tNbiOCJe_A5pSPpUiLJltN4aD9829KB5uJ4z4AeHtQxkok3gTS19s6F_O9bjjEkU0rZ0vcRMGGpTcKZ8ebsfnf8UvKWR2ESyeixw2HZb4mt1V0iOBY3FG1d1x6BF2YrX4c1Kk5x036-mCYuJEomjiqh8t2fyPgH_rmK4NNCaGsgC05kK2nnZEflgkUXyxt1Jx1o5BOPREM7P1zDKkC6siPBMmg3koRZg3YxkGKrwJxigniIpDU68yrdDHAFGStYjGlhFtlMqTP5j7K5iWSozJbYWQsbk4lxeSBsRLr_fJXOnPl5galIfymQouyc3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازدهی بازارها از زمان آغاز جنگ تا دهه اول خرداد
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655451" target="_blank">📅 14:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655450">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
برنامۀ آموزش‌وپرورش برای برگزاری امتحانات نهایی
وزیر آموزش‌وپرورش:
🔹
برنامۀ ما این است که اگر بتوانیم مجوز بگیریم امتحانات نهایی را از ۱۳ تیر حضوری برگزار کنیم.
🔹
پایان امتحانات را به گونه‌ای طراحی کرده‌ایم که دانش‌آموزان برای کنکور یک ماه فرصت داشته باشند.
🔹
اگر نتوانیم آزمون نهایی را حضوری برگزاری کنیم، قطعا مجازی برگزار خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655450" target="_blank">📅 14:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655449">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سقف کارت‌به‌کارت بین‌بانکی به ۱۵ میلیون تومان افزایش یافت
بانک مرکزی:
🔹
سقف خرید با کارت بانکی ۴۰۰ میلیون تومان تعیین شد؛ در انتقال وجه غیرحضوری نیز سقف حساب‌های غیرتجاری به ۳۰۰ میلیون تومان و حساب‌های تجاری به یک میلیارد تومان رسید.
🔹
انتقال از طریق «پایا» و «ساتنا» همچنان تا سقف ۲۰۰ میلیون تومان انجام می‌شود و سقف برداشت نقدی از خودپردازها ۵۰۰ هزار تومان است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655449" target="_blank">📅 14:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655448">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
عبور ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی سپاه از تنگه هرمز در شبانه روز گذشته  سپاه پاسداران انقلاب اسلامی:
🔹
طی شبانه روز گذشته ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655448" target="_blank">📅 14:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655447">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
این خانواده‌ها به‌زودی ۳ برابر یارانه می‌گیرند
🔹
طبق مادۀ ۱۳ جوانی جمعیت که در سال ۱۴۰۰ تصویب شده، سازمان هدفمندسازی یارانه‌ها باید با حذف یارانه ۳ دهک درآمدی بالای جامعه، یارانۀ خانواده‌های دهک ۱ تا ۴ که حداقل ۳ فرزند دارند را ۳ برابر کند./ فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/655447" target="_blank">📅 14:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655446">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7RhQTBWupeDtjTrJLdumcYDh2o1nhj9aPk7XBwFFCBKUMCncx8mNgcoKxHwQ3j33Fb9gvwUM4jFmuGbJ5FYEVSjO-ZuOtBJHvqvTwCE9Ekg_t7VfgS9E2_Hv77QH0R8leScmS2Yo8Q8PBIsQcTRsosdmetFMpHAohUX2ryDb01XD9QQm19cVOxeymf4K9fK8oSZZP0XkeYiTG7-WMWruD4Xt5hAMkeOrgnb6XQU3IWfS6KOzE7oj1wHFZ01UYS0AZYCD9k2I0DgEdZPPVO_R0Gm3YgMUEedgIBEdar3qgQWEwA-DNQSa9CgQffgo9NaI6okO5a_iGNNSbFGX198fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی تاریخی تقاضای طلا
🔹
تقاضای جهانی طلا در سه ماهه اول سال جاری با رشد ۲ درصدی حجمی به ۱۲۳۱ تن رسید؛ افزایش بی‌سابقه قیمت طلا، ارزش آن را ۷۴ درصد جهش داد و به رقم تاریخی ۱۹۳ میلیارد دلار رساند.
🔹
به گزارش شورای جهانی طلا، تقاضای سکه و شمش با ۴۲ درصد رشد، برای دومین بار رکورد زد و سرمایه‌گذاران آسیایی پیشتاز آن بودند.
🔹
خرید طلا توسط بانک‌های مرکزی و سرمایه‌گذاران نیز تحت تأثیر ریسک‌های ژئوپلیتیک و تورم بالا ادامه دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655446" target="_blank">📅 14:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655444">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل سرایا السلام(گروه نظامی این جریان) و پیوستن آن به دولت و مسئول کل تشکیلات نظامی خبر داد.
🔹
بعد از انتخاب علی الزیدی بعنوان نخست وزیر عراق زمزمه‌های انحلال گروه‌های…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/655444" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اجاره پراید برای تاکسی آنلاین تا روزی ۸۰۰ هزار تومان رسید
🔹
با افزایش قیمت خودرو، بازار اجاره روزانه و ماهانه خودرو برای فعالیت در تاکسی‌های آنلاین داغ شده است.
🔹
در برخی آگهی‌ها، پراید با نرخ روزانه ۳۵۰ تا ۸۰۰ هزار تومان اجاره داده می‌شود؛ این اجاره‌ها معمولاً با شرط حداقل سه‌ماه، ودیعه ۲۰ میلیون تومانی و ارائه چک یا سفته ۷۰۰ میلیون تومانی همراه است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655441" target="_blank">📅 14:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تیزر قسمت پنجم از فصل چهارم
🔹
در این قسمت روایت اولین تجربه نزدیک به مرگ آقای محمدحسن تاج میری که به دلیل بیماری کرونا به کما رفتند و زمانی را میان مرگ و زندگی که از باز شدن پنجره‌ای رو به زیبایی تا مواجهه با خطاهای گذشته و اشتباهات دوران نوجوانی و داستانِ بخشش در تقابل با تهمت‌های سنگین که باعث روبه رو شدن با خداوند شدند را نظاره می کنید.
🔹
قسمت کامل این برنامه در ساعت ۲۰:۳٠ منتشر خواهد شد
#تجربه_گر
: محمدحسن تاج میری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655440" target="_blank">📅 14:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f33160888.mp4?token=jFO9sP-rvYgu80TJyC3XDPW9Qajb9q24GJKII4w_zI_J0SVT1pn4oqW3yDtAUIxt45oF8nW0ytrCLeH1cC_OnC50yBRBDg8zSTHA3V5luzvHVDMilUKukygeKZE2Jlml7TLh-XYgxoTs9oZjsnlJmC8PVVCVcAt5XagUG9vLfwVQDY05KLrps_WpWkJk-MUxhRaUeJSMiynsnz_n7txCenZTfvD7Uwzvk1cTEY71CdCRf2ylEKSobJcKfM3aUgWgDxD-0DTuqkSZetV3Ow1CEhFGFTOc4ADKV8DM-hBd_m93sDncaxUAkyDjda3ZVspuMMsYhDZUD7qfQA3zejjMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f33160888.mp4?token=jFO9sP-rvYgu80TJyC3XDPW9Qajb9q24GJKII4w_zI_J0SVT1pn4oqW3yDtAUIxt45oF8nW0ytrCLeH1cC_OnC50yBRBDg8zSTHA3V5luzvHVDMilUKukygeKZE2Jlml7TLh-XYgxoTs9oZjsnlJmC8PVVCVcAt5XagUG9vLfwVQDY05KLrps_WpWkJk-MUxhRaUeJSMiynsnz_n7txCenZTfvD7Uwzvk1cTEY71CdCRf2ylEKSobJcKfM3aUgWgDxD-0DTuqkSZetV3Ow1CEhFGFTOc4ADKV8DM-hBd_m93sDncaxUAkyDjda3ZVspuMMsYhDZUD7qfQA3zejjMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی ترانه اعتراضی باب دیلن در دنیای ماینکرفت
▶️
Reimagining Bob Dylan’s Protest Song in the World of Minecraft #ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655438" target="_blank">📅 14:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655437">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPQJ3Gf-GvmPZnacvD0nVRPK4lP7_avPUaO9qy9YyjW5zb0yurcY1QRAL_pEIuaymdPhBUz-pH047U8_gmq-Rps_e9HADh4RgdXq6mLcpYOYDejn4esPIsiQc4BCdMM5ZnAc3jCFZMQYitEjWZn8NF4FlNX4LPfDh3OeolXfgplNL91fsyD3yj4EhQ0gQOwP8lcGo2BBN5X8m_d-yM25inwi_SZI3B15QoGxqK14mFwmdP4PGeQhmoMjdnA9S5OiqgIWqGm4rGCW7gy624pflTefE2poacA3h-K_9NGuwtwBEsM3XzRhdfFI2clHtWqhfTdr4HSa6FiM8-eQY5F_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
از مدارک مهم تا بسته‌های تجاری؛ ارسال بین‌المللی ساده‌تر از همیشه
PSP Express
با ارائه خدمات تخصصی حمل‌ونقل و پست بین‌المللی، این امکان را فراهم می‌کند تا مرسولات شما ایمن و قابل رهگیری به سراسر دنیا ارسال شوند.
فرقی ندارد قصد ارسال مدارک شخصی را داشته باشید یا نمونه کالا و بسته‌های تجاری؛ PSP Express مسیر ارسال را برای شما شفاف، سریع و قابل اعتماد می‌کند.
برخی از مهم‌ترین خدمات این شرکت عبارتند از:
✈️
پوشش گسترده مقاصد بین‌المللی
📦
ارسال انواع مرسولات مجاز
🔎
رهگیری لحظه‌ای در تمام مراحل
🤝
مشاوره تخصصی پیش از ارسال
برای مشاوره تخصصی در زمینه صادرات، واردات و حمل‌ونقل، از طریق راه‌های ارتباطی زیر با کارشناسان ما در ارتباط باشید
📞
🌐
www.pspexpress.com
☎️
+982142281
📱
09204228195
@psp_express
#پست_بین_المللی
#واردات
#واردات_از_چین
#واردات_کالا
#ترخیص_کالا
#حمل_و_نقل_بین_المللی
#لجستیک
#تجارت
#پی_اس_پی_اکسپرس
#ترخیص_کالا
#ترخیص_کار</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655437" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655436">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تیم ۱۶۳ رنکینگ فیفا حریف ایران پیش از جام جهانی!
🔹
تیم ملی فوتبال ایران که قرار بود در آخرین دیدار تدارکاتی خود در آمریکا به مصاف پورتوریکو برود، اکنون حریفش تغییر کرده و باید به مصاف تیم گرنادا (رنک ۱۶۳ فیفا) برود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655436" target="_blank">📅 13:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c50c3bba4.mp4?token=bVByfXABglwGRmIxGNj68onu5e_NMZ5rTjyDIPBookhnWQuj2-TnrvMz-UZdliQx6gAXa7exXVCog1jjqiR6cES1pYEYcN9G-43NM2RUeEUwXIntjSaBzHfxjtYw_ZP8aovdiKeoqwQw5Wp5ywmF7Mrg37VwE06irbWX4TPURRdby5yGZU_rTvDGvDubNmsUwl2JvnfvmIfAoz_n6ib1_XXKx59xIaVooIInf93K7TQT7C0-19KnJSFzBJS-8xkQau4VEc7E98clfkpv_40eA4m74bSqbBopi0NbHTJW3ESvwpZLeP_CgMmld4R4NZvELVltsGUKbE3RLUkSbFiebmQIMXkxConRucmL_xGOMcbVrMZpW3IVkgha5Noe5A9v9FLKaUFs3QGUWEkemzeNi6JFcyVbeeExmZ8nlOekhN1AmKJiqkVRAJQwg5IMgdgFvvT4ZW8VLw-8yXq1YmNSzRGWIe-8_7Ty-oom5ePMe8diLzVF5p8u_9dH9cVVOfofTXiqtslq5eXmYM5QFF6oV_PmttQbCmjAIKVRAZO4OqlQK4OR6FPrVq05kzka8dwzhAIU5PAGinEj1p9sWLH532b7rqbVVNHok3kLEeoRqg3Jrf_uv0uKg2asNFdQmTfrXnCiPiqrx7s-emdEgaEC26BTLfbsuaIoucHTgdyN_qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c50c3bba4.mp4?token=bVByfXABglwGRmIxGNj68onu5e_NMZ5rTjyDIPBookhnWQuj2-TnrvMz-UZdliQx6gAXa7exXVCog1jjqiR6cES1pYEYcN9G-43NM2RUeEUwXIntjSaBzHfxjtYw_ZP8aovdiKeoqwQw5Wp5ywmF7Mrg37VwE06irbWX4TPURRdby5yGZU_rTvDGvDubNmsUwl2JvnfvmIfAoz_n6ib1_XXKx59xIaVooIInf93K7TQT7C0-19KnJSFzBJS-8xkQau4VEc7E98clfkpv_40eA4m74bSqbBopi0NbHTJW3ESvwpZLeP_CgMmld4R4NZvELVltsGUKbE3RLUkSbFiebmQIMXkxConRucmL_xGOMcbVrMZpW3IVkgha5Noe5A9v9FLKaUFs3QGUWEkemzeNi6JFcyVbeeExmZ8nlOekhN1AmKJiqkVRAJQwg5IMgdgFvvT4ZW8VLw-8yXq1YmNSzRGWIe-8_7Ty-oom5ePMe8diLzVF5p8u_9dH9cVVOfofTXiqtslq5eXmYM5QFF6oV_PmttQbCmjAIKVRAZO4OqlQK4OR6FPrVq05kzka8dwzhAIU5PAGinEj1p9sWLH532b7rqbVVNHok3kLEeoRqg3Jrf_uv0uKg2asNFdQmTfrXnCiPiqrx7s-emdEgaEC26BTLfbsuaIoucHTgdyN_qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف عجیب در اورست؛ چادرها و کمپ‌های ناشناس و رهاشده، منظره‌ای شبیه «شهر ارواح» ساخته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655435" target="_blank">📅 13:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eflRo3pCP48PdR_8hngqmvr2Glq77zikP1Pd13V_aLhNEw5bclP6qhX-RDm8F1qkzPS8UbnUv9vr-f5SMDvy8Pb-iUYHTi39TVnzeIAVEJm3nqKfc3tA72V9Uoc93pFRfNbntu6Vq_EJYO2tTWhJ2yyrNqCf5n9XRoL4tZBA7RUd9u4GjkHcDrPutcrNqMHja9aj-BVZeJrqCzkTN9M8lX86xSeupKu9PEzb939nnzFQ-z2JLxF4M0yMQZN5t4Jw9qAdjOc5lia_fmrCDZM4DRCwWUDwoDeNpePMYq_wwcfSskQQchUsXy-z7l8W3BBjRPFtXSf3U7GyZeUmB0Tj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس همچنان در مسیر صعود
🔹
در جریان معاملات امروز شاخص کل بورس با افزایش ۴۴ هزار و ۴۱۶ واحد در سطح ۴ میلیون و ۳۴۴ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655434" target="_blank">📅 13:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT70_5RWgiUYwy5EUcC7_WtR0m8bz4JQ3rUa2T7n2p7JZMnZKqowwyf-Qm0dR8PXwQenrwCoPGM6J5wD0ENyS5mJ7VkyII9z_BVxqv5pQMD1FzoQqHUSMciesKwa4jeA1dYJwwNFjI-R4A21DerP6Q3TjCBM0MPMqcjV76Gy7jElIocMB_gW-DBblv-80hWNd8Mh7BleXtyATB3WBSvb8vc2BhNuzCar9Vana3uDwJ-SRLgbvlEFGQT8FxNaZTukp8UWUym8PBs70f4ZvYw6JOQaM3aWgSP6k5RORsqCJBZzF6pikiC6Dv50EC77F2v57weTNtcJFE07rAfyJEmBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر اقلیت سنا از کنگره خواست جلوی ترامپ را بگیرد
🔹
چاک شومر، رهبر اقلیت سنای آمریکا، خواستار رأی‌گیری کنگره برای مهار اقدام نظامی احتمالی علیه ایران شد.
🔹
او در سخنرانی خود در سنا، مدیریت دولت ترامپ در قبال ایران را به شدت نقد کرد. دموکرات‌ها برای بازگرداندن اقتدار کنگره در تصمیم‌گیری درباره جنگ و صلح، فشارها را ادامه خواهند داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655432" target="_blank">📅 13:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای واشنگتن پست به نقل از منابع: مقامات نظامی ایالات متحده در چندین قاره، سطح حفاظت را در انتظار بازگشت به جنگ افزایش داده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655431" target="_blank">📅 13:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
اسپانیا: در هیچ اقدامی که تنش با ایران را افزایش دهد شرکت نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/655430" target="_blank">📅 13:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioMzcNqmVv_nsWMZS8W8JqxtfRzi6CiYz0uQ93DZ-H7hUwax7_yjQsaEPYv3yNta2t7KSdoEEHFLp48uw-wbxsOa7ehyiXTEyXIbczies2Bf9DQSf5idirjRyHGc5Nlq0PR5QdmNRLgNCnA8SleXvvJgBXDHXyfeEQM4HWo767gHjwjBcBXpuEs4w2LKO9UuuDcXG5JkVFJSsphlx_UuabbY-fu4hpJXMMQxgS9Yuv3pc8tKc1JytIpOL59Jezx5EgHwxPPE5KPR91mPUazXHWcr3LG5pm4Et01XNMCItbgnRhRHukEMkL0ICmbfZakFtsfd2DIZFaiTSfwAckW76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین سنی تیم ملی ایران در جام‌های جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655429" target="_blank">📅 13:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7a3d1bc9.mp4?token=Z92M5U1uAg_4EAJSm68X6GEsArGJ4ho_HwkJGC82xZ5zzC8C51OvOqq0LI3J4J3WFbH7TqH32kSej6vHQsVl8XkEU9tp8rm4ghIQvX8wGawz_gU-ZCt7TjDsFrzr1sgeWYiYRjPc4_aOH6389On-XiJ9kTK83aHV56lmkdjHLIvBkXLINr40Rk-ggi6xo9P_k6-NeY-6SYKsoHIn2LqcDxGJdfeqlLkT4zFfayxv4uI-5yeFeFRgCwkYFtTXtaOUH0e9wZtORNV7FAfJWwlUls_B3dwd5S2U1O9LWLzcbz4W0qiky2GwyUm99sjJlhcFOI_IUlLjX4SMLtl9i6cZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7a3d1bc9.mp4?token=Z92M5U1uAg_4EAJSm68X6GEsArGJ4ho_HwkJGC82xZ5zzC8C51OvOqq0LI3J4J3WFbH7TqH32kSej6vHQsVl8XkEU9tp8rm4ghIQvX8wGawz_gU-ZCt7TjDsFrzr1sgeWYiYRjPc4_aOH6389On-XiJ9kTK83aHV56lmkdjHLIvBkXLINr40Rk-ggi6xo9P_k6-NeY-6SYKsoHIn2LqcDxGJdfeqlLkT4zFfayxv4uI-5yeFeFRgCwkYFtTXtaOUH0e9wZtORNV7FAfJWwlUls_B3dwd5S2U1O9LWLzcbz4W0qiky2GwyUm99sjJlhcFOI_IUlLjX4SMLtl9i6cZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری مشهور آمریکایی: ۱۶ میلیارد دلار به اسرائیل می‌دهیم در حالی که مردم پول خواروبار و بنزین ندارند
مگان کلی، مجری مشهور آمریکایی:
🔹
آن‌ها (آمریکایی‌ها) توانایی خرید خواروبار را ندارند، توانایی پرداخت قیمت بنزین را ندارند، توانایی خرید خانه را ندارند، توانایی پرداخت هزینه درمان را ندارند، و ما ۱۶.۲ میلیارد دلار فقط برای یکی از همین ردیف‌های بودجه به اسرائیل می‌دهیم.
🔹
آن‌هم در کنار هزینه‌ای که برای جنگ اسرائیل علیه ایران کرده‌ایم، جنگی که هیچ کس نمی‌خواهد. هیچ کس.
🔹
در عوض به مردم خودمان کمک نمی‌کنیم. آن مصرف‌کنندگان یارانه‌بگیر بیمه «اوباماکر» متضرر خواهند شد، چون ما اولویت‌های دیگری داریم؛ این واقعاً خشم‌آور است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655428" target="_blank">📅 13:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54688560ff.mp4?token=KUePslwK9fa3rOJutOp9380wo5LNlOoWRvnQGiezCRyBAsvKTFWqY_05ak9b_IpbGCfBR-RfXcb6RGASuTSkkqW7mNg1qb6ZKqpARkR-tNT4kV6vg5W4n1KI_aVufg2ujXd8O-xYZy_vfTSdOHAEFFhR60UMV1kKMvIbhGOvo78JZhKvi4vJetbsl26Qw8fybAWr5EdDb1xwNzXc2j_a5e7JVcunaAeqvobC5bvLH4DDvWLRGGi6l2Wl5xtiY0M_5H_kjkq5FjzEaXD34e6CGt_gp40NQvnZMgzZdwDoFeojY_HQNkPcDpBvcwfN6oNr9BBGTb1rzv5J3Jwu13ttdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54688560ff.mp4?token=KUePslwK9fa3rOJutOp9380wo5LNlOoWRvnQGiezCRyBAsvKTFWqY_05ak9b_IpbGCfBR-RfXcb6RGASuTSkkqW7mNg1qb6ZKqpARkR-tNT4kV6vg5W4n1KI_aVufg2ujXd8O-xYZy_vfTSdOHAEFFhR60UMV1kKMvIbhGOvo78JZhKvi4vJetbsl26Qw8fybAWr5EdDb1xwNzXc2j_a5e7JVcunaAeqvobC5bvLH4DDvWLRGGi6l2Wl5xtiY0M_5H_kjkq5FjzEaXD34e6CGt_gp40NQvnZMgzZdwDoFeojY_HQNkPcDpBvcwfN6oNr9BBGTb1rzv5J3Jwu13ttdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ده سال تراپی خلاصه در یک‌دقیقه #سلامت_روان
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/655427" target="_blank">📅 13:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWe-i7LhmKbLurz2I6eYS8VDQbouf7Vxr5CM44QOLZD8L8fbuTvLFRhveJ4gCNzHWzpMHopat8H4o4Pq5dxtQkaZ3uMKdBdByHsM3o4p2K3OgO0WEFEPycwMCu9cw85RSPhuFAo09tXVB9iIw_s2Kq2QuiLkgn6npHEmuj1elIDzbdqPJJ89KnLziUwkXCnCc_TGx1DUBqlLpPK8T15LcWt-Wb99Y7V6e3qAqZ_A43rXPT1GBAGgSF2vAm7Jm6LJKyBdLsSYtk5B4Kk3K_mEQ77xiPJfrU621BQc2HuS3J11eenor1gJ7CnCjOALu565MjY20UFlPOdqmgPHBJVOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4_yI2B70egX4d-jsqvoNK27t9_E7lmBybFRrWqGRvuHHbufBaY2dpckwY5qT5UmBgDS4BKsrZXE8vdf8fIP6oBPDEEeZiblaEPc-_13VnhUKtkN7sn3omemywkRoptGWYYDctqYxalwXglIulJhCciTdMW4YhXAWh91SmqXyGBMze4PXEht6IunngmTablX19h6VHHzaHo5eOLeocpF_Ud1Mdpv2ejMctqZsjSU4rULEWSqOWl4Gh7iH8b-bqMoqTN0bGdqQRylUSRf9hE4Tx7uD-jakgwL-J905yturKnwo9uvl6HtKn-DaVn62VaVNcaqF-yczsjbCFACM3oX2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین پرواز آزمایشی تاکسی پرنده در قزاقستان
🔹
این تاکسی پرواز آزمایشی بدون سرنشین خود را به مدت ۱۰ دقیقه‌ توسط خدمه زمینی به پایان رساند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655425" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
امتحانات دانشگاه شهید بهشتی در روز پنجشنبه ۱۸ تیر به علت تداخل با کنکور ارشد، به شنبه ۲۷ تیر موکول شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655424" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
عبور ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی سپاه از تنگه هرمز در شبانه روز گذشته
سپاه پاسداران انقلاب اسلامی:
🔹
طی شبانه روز گذشته ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655423" target="_blank">📅 12:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjY3NJmF-9udCEkAigN8Rj8FR6J0qS-IBMaEbVaqLnHGcXmEQzT6whZ5e3MszrRk-x2QpvdzPiW1Y5OW2ubEsRDVetDU0d4qxVQfYjeygV4-p8V0IZ5Jr4l12NeLgU7vjqE8HqbaOk3AwKQPakkLcdWmQWHE3lwgBTc4iEmy1Eyc1gueLcH2pdDN_JLB9sVFzv0yHnTSBnCbRXXhbbEqf7NLDT3DHsToOKWQ1SFS_ZpksGBFnG4KZrx0BJ9U3kv1pH3ojyDoVc7lbAD1qVM23oPRdxnoegFzwMzI1bqLYw-RnlTfWaKJ5DHwk3-WCANkSTN6Kg2NoFSAYAzz5oRh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: ادعای ترامپ دربارهٔ منصرف‌کردن نتانیاهو از حمله به بیروت، نشان‌دهندهٔ نقش مستقیم آمریکا در تجاوزات رژیم صهیونیستی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655422" target="_blank">📅 12:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_af4aVwqPf70jHLsjipaIyJaqysczTdDH7s8WZ5UvEa5J3UHK1WFmWLlRQu0CZvv3Rywbku3rjQ53dRnPQDfc1JJqjEyTGRYL8wTjDjKL803ez9wsJYcoqAkvF-mAaF2KEYRPI_20nwzRBT-X7gMogGqWghT0NsL2P-o_Xb5T8zsAPBKhPQMjQF-Ku4Tdcjc203VGi9-I0Ap3JXe3MZnZZrwFcYScFgawld7InQbYT-ccrPeeNOo7HTlMoF54JHV-dBxMWAC3N5m2IkyW0SsSejSqqETj3BtVovtW1xQ8JHb1dMvf1RhEWagHJuGV77L4rmJ57bEqIVmT82aeQMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ایالات متحده سلاح هسته‌ای خود را در اروپا مستقر می‌کند
رویترز به نقل از فایننشال‌تایمز:
🔹
ایالات متحده در حال بررسی استقرار جنگنده‌های قادر به حمل سلاح هسته‌ای در کشورهای ناتو است.
🔹
این اقدام در زمانی صورت می‌گیرد که دونالد ترامپ، رئیس جمهور آمریکا و بسیاری از دستیارانش از متحدان اروپایی به دلیل عدم صرف بودجه کافی برای ارتش‌هایشان و اتکا به ایالات متحده برای دفاع از خود انتقاد می‌کنند.
🔹
این تصمیم پس از گفته رئیس کمیته نظامی ناتو که در صورت فراهم شدن شرایط در مساله تنگه هرمز مداخله خواهد کرد صورت می‌گیرد
./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/655421" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تکذیب خبر معافیات مالیاتی فروش تا ۶۰ میلیارد در سال ١۴٠۵
🔹
سازمان امور مالیاتی کشور در واکنش به انتشار خبر نادرست در خبرگزاری ایسنا، ضمن تکذیب شایعه «معافیت مالیاتی تا سقف ۶۰ میلیارد تومان»، تاکید کرد: موضوع برداشت اشتباه خبرگزاری ایسنا از سقف بهره‌مندی از «تسهیلات تبصره ماده ۱۰۰» بوده است
🔹
به گزارش رسانه مالیاتی ایران، سازمان امور مالیاتی کشور شفاف‌سازی کرد:
برای سال ۱۴۰۵، مشاغلی که مجموع فروش سالانه آن‌ها تا سقف ۷۲ میلیارد تومان باشد، می‌توانند از امکانات و تسهیلات مقرر در تبصره ماده ۱۰۰ قانون مالیات‌های مستقیم استفاده کنند؛
در این صورت، این مودیان از مزیت «عدم نیاز به ارائه اسناد و مدارک و اظهارنامه مالیاتی» برخوردار خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/655420" target="_blank">📅 12:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پنتاگون ورود خبرنگاران به دفتر مطبوعاتی این نهاد را منع کرد.
🔹
انتخابات هیات ‌رئیسه کمیسیون‌های تخصصی مجلس، ظرف ۳ هفتۀ آینده حضوری برگزار می‌شود.
🔹
سینماهای سراسر کشور در روزهای ۱۴ و ۱۵ خرداد تا ساعت ۱۸ تعطیل خواهند بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/655419" target="_blank">📅 12:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjzanW3KeZGVjgL1O-A6-zR2uUU3t7fyLASoV5Zp5SRzxMEEL-30WnXLR-wshczSJIDMiggtnK4go2grZXOnN2NTgVTglyQIrQaRkFoFpq0xn6f4mtfarUrympkUBgR01vz88t5DfCpacUReCRS40K6ROE8LZAo2haUa6-ECC6Wx7zZWxSnlh0a0xgg45E0TqngqQUTO7bkcry8ZeP5b-2s1vJOiE9Fl9-fpm7-nFL4nWfXpjqMj7D1pO_GmcFLs5o54KvFGQH2jnulBD51NtvrYMOK62Hwy3jDuwl4tbfBFqz4rjV60eVpfHDGEaabyYq6uecTBIa81I73jnWrmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مردم اخبار جعلی را باور می‌کنند؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/655418" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJYqx2xXp_IqhwK0UhWNPzDWug03dPzAixoL8IurvPrngLGZ6Nfk09P1FM9D8q4fI35IVDEE-Yn_ZyMIJ08q0GDew6g7q7abOqjEmPqZnpDOhPzb1v0m0OSDYo76FIhKLOIW0mQIUuq9kjVx_QrGS3WmxH8_M5vQegEivJm_sPlG6vXqX49WvmUeaKbDtwdG2eOPE14EriF81WLIE-CyEpb9FBHMgUntYyYTS5BJ2OZk0kN9wGgHDlm5XwI7e3DHmu7djYb3Sy3f3hYLw2ZoSzB7kwm0Quq6LfT01F70yaoj4kh10QSrx_XM489dFsDh7v25V-i5XKW_ZeI3J8CcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3KfVMJkbIOZKRay0hv9XAswqAxEO92j4e3DynulJNIV9aMhS4LaGlYlCj_6K8yUjdAr-4jguJFzSK5SOJGknJCZ_5kAYQDRYEfO43dZREEe6y8bdOwvSxPY3UyYVqDj3_gCv-gudj_lgwefGSqfTUAHVjEkK9eq-40CUAsh4hvcjR2MDaccKYhMGyGLU1vhdEhE5-qpbc5bh9yh6g_mAVzbAJNzUapRNckeDwVSOl0x3iv-j8Cgg6iQIcLvWQW7hFJBkqCdU8gHPO058twTwOKexa1dngAprSL-UfaxI3sVFuFKBwP93mKBqs8mzBWD8uhxOwfosu6GgBPGlXFNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlSiwdXw4bZqZcZBh_kAeO5-EB-4-o31IBZGslTY5kX_Y-If120OqeAMf0s9-VJUPA_6lranSu_VkW59gRemIwOo5ZpHu0wjnrtBq3YW8BlfkkbpzLqZoNCKUgNSj3le3kBY9jnzKJUuqpcnQXc2LEzTis4hTKiTUkv6bPsDD_3Cw0qIwveqXmbIajL379I354nf6hUxM1gb9NpMaN98m69N0-67Tqu63EukbEgZxbqAXKBmnJv3h2zmF9DlInhi1Aq-T7slVKLWVjZslMcsXEX8Fd8dDabIkk4cvZz_3XLUfgeClK5oIbWW4ccgokr5ssVOAC8gUscjWob15Brdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUGiOqN_bk22ktzzHPQZzAj_0t2X5ga5IET8a8f5Tekp5t58bQYM_aMYHfXang2kF6BOxABDzh3uoxOXEuV2hYUV4kFP1vvuDMT-QJ2Yhis2JxchGfz3ghQKpWiKvwHjVW_b1eA_gcJVYDLyeEoUqyxcz2U9lBenZx2xfNJv40H7tJHis21xcOYqNl1naH8XdYSlTegSHxehWKgutXJXqEQeXm_sKGvQFr6xcPHAGtDK7psawhNOmZ4ncFeyvtguFImz9-LrTQTFJSZLyV95MqDv7tcyWb7VGhuM1N8kIwmtokwhfgU2cgCYzHq86TFp7OLm0FalXyDcqFe0Gy6bGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLGnqEcUYTsd1gpwton0IEzC1uZNkUXysnoXfx1khW9HjtLP4FnEMRujNBA9qImcz0sVZXu2UQIb4TnXrDULUJhrJawj8ARoWO3OUJdLtTUuldxSeuLx5Z9cHsIYTBSz_bdsSGjdO2kVE5JceBMwv0zc7I2gvaVYa1DOCp-PVsmoW6L48isg0BM6DLAzOknGfEmKl4QQ5WXgIteCJZPUSNfKtEPXIYU_IWkgj59HCQy4OKZtoa-xWIDaQXxUTDwN0pnQG2Brc49cFFauBXsaxYRuRNgtlIvjhvtRdYCdlu4sW8du69BHIxlTDNhUaSq2XjhocKMo2W5J6VvLatID0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شگفتی سراسر جهان از طلوع زیبای «ماه آبی»
🔹
دومین ماه کامل ماه مه ۲۰۲۶ شب گذشته نمایشی دیدنی برپا کرد.
🔹
ماه آبی کامل ماه مه، نمایش خیره‌کننده‌ای داشت و آسمان شب را غرق در نور ماه کرد، در حالی که ستاره غول سرخ کژدم‌دل(آنتارس) در نزدیکی آن می‌درخشید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/655413" target="_blank">📅 11:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQE5-Sn0Rt7uwiOJvlxeFo8nBiUdGkqOswKqI873AnkVZP5cACGIMWZSkOoIIWX-gTTiNxJVq3L8lkWDEovF7nOxklUBqCoL29pTGv380Gb7TKR9YU8sqoU7aGIP6k6xq-AbhTb7ZWbllvNYH8wM1lrZ2NhSWLUMzjR422pa-hpq-sDbkZuBA3CGDRiE3wSUvrN3gDKL1o7yg_xhAJt1a7S-YgAAxH5BA1n590JWKCZcAz4BV6KuI_RtlgbV9Vmxl-vbSvTasFzSTpXuFADXxY2SbQ8SZwvJJJoraCokDS9J7xeaDy6utm8rBJn4NsjL1NXeY0gDJe0Bnneye52SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرعت رشد اجاره‌بها کم شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655411" target="_blank">📅 11:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319da7afec.mp4?token=jyteRk2SITl5PPfVYh9CnWF3oAAfUp3uBhCKZA4_XXR7PzDGhD5IVEE6czhKspinOvaq19v2bPIA4ksCnX8UEhljrecTnCKCVd8rMs1JhixAKPUbD1UmS4-1e6l3VKbzCwHv59ApWjRQWD8VcL-ZscKnfLDEJtxhsOv-6NJPTpwWmwBFYw7HmIKq3p_YrTQ8PS-bILGYOklY8zdpVAWo35dA1ksWggeiYQ8-ZE2JxCtfWkUNN2aUosDjPXQJF66CK90Sb9l29uUsmvuymuz2wA5mVat8eUZhF_VZWVI3WDQKHqEc19Gniebp5GTa4C6wfAkII6lJMxRFzzAIcJ3zHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319da7afec.mp4?token=jyteRk2SITl5PPfVYh9CnWF3oAAfUp3uBhCKZA4_XXR7PzDGhD5IVEE6czhKspinOvaq19v2bPIA4ksCnX8UEhljrecTnCKCVd8rMs1JhixAKPUbD1UmS4-1e6l3VKbzCwHv59ApWjRQWD8VcL-ZscKnfLDEJtxhsOv-6NJPTpwWmwBFYw7HmIKq3p_YrTQ8PS-bILGYOklY8zdpVAWo35dA1ksWggeiYQ8-ZE2JxCtfWkUNN2aUosDjPXQJF66CK90Sb9l29uUsmvuymuz2wA5mVat8eUZhF_VZWVI3WDQKHqEc19Gniebp5GTa4C6wfAkII6lJMxRFzzAIcJ3zHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از دوربین مداربسته در یک فروشگاه لباس در ویتنام وایرال شده است: این تصاویر نشان می‌دهند که فروشنده فروشگاه و یک مشتری، به مدت یک دقیقه به دور خود می‌چرخند و سعی می‌کنند یکدیگر را پیدا کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/655410" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مدیران خودرو، اجازه فروش ندارد
رئیس سازمان حمایت از مصرف‌کنندگان:
🔹
به شرکت مدیران خودرو اخطار کتبی داده شده تا هیچگونه فروشی با قیمت‌های خودسرانه انجام ندهد و مردم از خرید محصولات مدیران خودرو تا تعیین قیمت‌های قانونی اجتناب کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/655409" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655407">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9956f384c1.mp4?token=SOwUtynC8vQ_M3Qx5_d96FobsutkHANcX6JgU7_DvaUEoUV8Kxvq1YS5y76hsH1U1iTEcmk0638DrUbyOBKHF-lFTAEJo1jxuHJFdzHdHf0P3EHJg5GaTI2nmtz6vHQ9FlE7bC1iWAA_rt4LqTGkUlf6OvR5xKaNlkuYE7wnXTD8fCWOwBGxux4sXjQI3MCSZbq4KVUCH9ZV-bUC9aNuu8ascwDiLEkFYUECEInMGXrSOF4PDzG3tKaW8yBsk6wxUz94MtNQykq7j6JBIqcdECN89hROI_E9Ae3bFsFiTsQPRN3v5wzh92kiGCh7g7lgO0YSQwMwiGCRD0rNUrGULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9956f384c1.mp4?token=SOwUtynC8vQ_M3Qx5_d96FobsutkHANcX6JgU7_DvaUEoUV8Kxvq1YS5y76hsH1U1iTEcmk0638DrUbyOBKHF-lFTAEJo1jxuHJFdzHdHf0P3EHJg5GaTI2nmtz6vHQ9FlE7bC1iWAA_rt4LqTGkUlf6OvR5xKaNlkuYE7wnXTD8fCWOwBGxux4sXjQI3MCSZbq4KVUCH9ZV-bUC9aNuu8ascwDiLEkFYUECEInMGXrSOF4PDzG3tKaW8yBsk6wxUz94MtNQykq7j6JBIqcdECN89hROI_E9Ae3bFsFiTsQPRN3v5wzh92kiGCh7g7lgO0YSQwMwiGCRD0rNUrGULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مولودی خوانی غدیر به زبان انگلیسی
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/655407" target="_blank">📅 11:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655406">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgojGgHQbcmt19YsQLRGIeOJhyjYHo9vu-g3sbgkhhKgCTwjLAeZ_vR3SJNRqnkwSSxoT4dRPmn2lSw_jBRCjkuMMnMV9hYcflUIkvcp7zXFjT45uZwHaoQscMXVhYIGaT458qYfQXJRlUnzbIRzwyMwwXcs_1ZuxP-1Ejj-rx3DqeB-b3uZlnEmu_JWirfnF20ZW7J_cxTDNVfV05li8zE-mI8QmwXRH94wFsjUxBZsGQtqFgKo-u8iZideXGSlpAG1s2FZb7nbIlb6Pqkh1znEeYoFhrerki9Z8UJi-kTk5HIYmzEQUSFK9NSpq0Caat-1qmnUMOspW-OwF53ItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پردرآمدترین ورزشکاران جهان/کریستیانو رونالدو در صدر این فهرست با درآمد تخمینی ۳۰۰ میلیون دلار
🔹
رونالدو تنها ورزشکاری بود که در یک فصل از ۲۰۰ میلیون دلار عبور کرد.
🔹
این مهاجم پرتغالی ۲۳۵ میلیون دلار از درآمد درون زمین را از قرارداد خود در لیگ حرفه‌ای عربستان به دست آورد و ۶۵ میلیون دلار نیز از فعالیت‌های بیرون زمین کسب کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/655406" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqNGkIqsCuMmZUd6w3FQA5VDBo3w_65uzVjcd_b184_AP5sGELp4ThwWs78Y1DVcXue9EA-avSVj_zCetg3eVVBHM8d1wegM1lbCc36wzgH4ulCXl0u5_SQoyS8Shcr8G6bovCZhcaJ2v9_x7BRdz7DWpIVd8CzFKvuDGuHEcTsjNkPppCDQ_sgq8bFfIdyl02bUAYPr-Vfy_EODNIcPvSG3ilzS9gqcAh8f3Cr_zhfi06bh7T1vClEW4FfyTRgqIEMhwCP8EHQbbFM-4kCwvfHU8JVGszVRBZ-zxJdwmkxKshF51S-4_B9Q2ZoeeGH6q9Wf09Lixht7ppgUDompRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار اسدی: هنوز برگ‌های برنده را رو نکرده‌ایم
معاون بازرسی قرارگاه مرکزی خاتم‌الانبیا:
🔹
بارها گفته‌ایم که هنوز همه برگ‌های برنده خود را رو نکرده‌ایم و برگ‌های زیادی وجود دارد که اگر لازم شود، از آن‌ها استفاده خواهیم کرد.
🔹
آمریکا فقط خواهان تسلیم کامل ما است و ملت ایران هم هرگز تسلیم نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/655405" target="_blank">📅 11:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgtuZuWVCK4d1T243BLcI6XT-ik2jJJIDajJ7RfGp4XC8W3tKYdOvr1xQF8bbCD32ozruOyDZvuun2JqsvXeyy578lZ3bMpuQG6GsLOqka2wd-WN-cgDTGfm4ywPY_T_oMLQ7ADsxwWcWKeB0BC5J_Yh7vqDlby6VPq1YxEWW_i1T62214jkj9r-xYWYhwyE4UOlIDQPCYtg1UZltPx76RET2m_a3IUF6atYZz-0LwOpxrP8sFqMpVhYGQOInpB8Z0VA3UFR56v5DSb-EeFB4UVM56vN1msVimjpTg7Sl4rE6DqcttxPeZvVVbW1JPDvyEB-nWPGTwvwkESbOYQNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الگوی مصرف دخانیات در ایران، چه می‌گوید؟
🔸
در این نظرسنجی بیش از ۴۹ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۳٪، بله ۳۷٪ و تلگرام ۹٪ بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان تا به حال هیچ‌گونه مصرف دخانیاتی نداشته‌اند و ۲۲٪ هم به طور مستمر و روزانه دخانیات مصرف می‌کنند.
🔸
با وجود فراگیر نبودن مصرف دخانیات، مصرف دخانیات همچنان در بخشی از جامعه رفتاری پایدار و ریشه‌دار است.
@amarfact</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655404" target="_blank">📅 10:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
چه کسانی از ثبت ادعا در سامانه ساماندهی اسناد غیررسمی معاف هستند؟
سخنگوی سازمان ثبت اسناد:
🔹
افرادی که دارای سند مالکیت حدنگار یا تک‌برگ هستند، نیازی به ثبت ادعا در سامانه ندارند و مالکیت آنان پیش‌تر در دفتر الکترونیک املاک کشور تثبیت شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655403" target="_blank">📅 10:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwwYqQCZlvNA6iCuSOt_3hAj7zU_i0lwFmvfOHg9hE_ZHNAT8uuRwAohsm7IyjDu00ti5OHiThZbnVBN-iT1xLLMPy1d5z99AADiJ36AwBPhRBDUwzdlbWxaqAwT6jCQFGexCmlj4yxXzrGP73-1-1Qy4dJqUFgqsMSUe4vuFG50jnVCaEqCHxkX2p-OJzPKgAoq7HihjMz66JQXR0EcUnLrZxiY8vM9IwCRStOFBgO2xbpUau-wQhAwpLZn2b-c_LvBJpbQstakxcanR0DeoHTE_G5AckHdtVIY_q-ZK9WNap9XgfAJ1GVF1v4x2yGKmiENNYUJrXSdMvfc0TXUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655402" target="_blank">📅 10:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ایران در هر ۳ بازی جام جهانی سفید می‌پوشد
🔹
بر اساس برنامه اعلام شده از سوی فیفا درباره لباس تیم‌ها در جام جهانی، ایران در هر ۳ بازی خود در مرحله گروهی جام جهانی با پیراهن سفید به میدان می‌رود./ایسنا
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655401" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655400" target="_blank">📅 10:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhC1XnLExRt3si-OZ5beAR6B7Of1ZxLZvz1WW1OhFyeK0PyS0AQYEX_z05pnGamxoERHn6BVVCgHTLZyiBsQwnjUfPWhiqS6uixmtmcV3BhEOf435-iafIZJju8fCFPdF-kdH63ykprPml3sYje5Jpg6ImiDIuAzs3SbzkwZGWWhnl_JIyc9WbK5ZRVCPwqcEGcXw7SibTMaeKreuRmRZDtHmPy5ETUPBwJzk4mfIgLI3Axu5gc3B2Z7TYO0lmaF4i5zXcLQd0UBS2HIbXlT3h6VSlXTnEWEyluOm5zptO01HX48exkSrAC78fyXo06i_Ibc3qYvzJ8Xkv1Mud1ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در بیش از نیمی از کشورهای جهان سفیر ندارد
🔹
به گزارش NBC News، آمریکا در ۵۶٪ کشورهای جهان، سفیر ندارد.
🔹
همچنین حدود ۲هزار دیپلمات آمریکایی در یک سال گذشته از خدمت در وزارت خارجه کنار گذاشته شده‌اند؛ چه از طریق تعدیل نیرو و چه بازنشستگی اجباری.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655399" target="_blank">📅 10:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منبع آگاه: متن نهایی ایران همچنان در حال گفتگو در تهران است و هنوز پاسخی ارسال نشده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655398" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96d4703e7.mp4?token=UO87cwkrXKa_IXeJNXtAqL2apweh_NsUfczqjdDg0GtghiniR-eDND4Nj2ZRg2_NWUlvfH-9_imKbxRErx_A6zJMRceVCzhMne62mYr8-CGa2idQKS3lhhFjWPtPn44nlrm-Wx4CFldkOHkG0DHEPhnIMhj-djXgUqhGeHEqil7efTd0YTioU4Wlb1L5fP-uEFA4FptRtTMv_aYYnLriuptNbJSt_JxLBivrR2dKv8L8jy1NoJ_CLNjeI1IV1dF3lDZxdQigTH06DKXy0cdOV5SLDdijztaiY-PipXlCujkiCjMHVCL3ntsl4-fz3vLGETfdQNf9Cma9_bPKx-ebKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96d4703e7.mp4?token=UO87cwkrXKa_IXeJNXtAqL2apweh_NsUfczqjdDg0GtghiniR-eDND4Nj2ZRg2_NWUlvfH-9_imKbxRErx_A6zJMRceVCzhMne62mYr8-CGa2idQKS3lhhFjWPtPn44nlrm-Wx4CFldkOHkG0DHEPhnIMhj-djXgUqhGeHEqil7efTd0YTioU4Wlb1L5fP-uEFA4FptRtTMv_aYYnLriuptNbJSt_JxLBivrR2dKv8L8jy1NoJ_CLNjeI1IV1dF3lDZxdQigTH06DKXy0cdOV5SLDdijztaiY-PipXlCujkiCjMHVCL3ntsl4-fz3vLGETfdQNf9Cma9_bPKx-ebKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
التماس علی‌نژاد برای حمله به ایران
🔹
شما یهودیان صهیونیست هستید که می‌توانید هم دموکرات و هم جمهوری‌خواه را در آمریکا متحد کنید پس چرا در مورد ایران مردد هستید و حمله نمی‌کنید؟!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/655397" target="_blank">📅 10:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
مجتمع فنی تهران - نمايندگی استان البرز (کرج و فردیس) در حوزه های زیر دوره های آموزشی و تخصصی برگزار می نماید و می توانید ثبت نام کنید:
@mftalborz
🔸
شبکه،برنامه نویسی و هوش مصنوعی ، طراحی سایت ، اسمبل و راه اندازی کامپیوتر ، ICDL
🔹
معماری،طراحی لباس و خیاطی وگرافیگ
🔸
حسابداری،مالیاتی،معامله گری ارز دیجیتال و طلا و نقره و مس، فارکس
🔹
زبان های خارجی و IELTS
🔸
عکاسی، تدوین فیلم، ادمین اینستاگرام، تولید محتوا
🔹
نرم افزارهای فنی و مهندسی, تراشکاری، فرز، جوشکاری، تعمیر پکیج و کولرگازی،برق صنعتی
🔸
برق و الکترونیک، برق خودرو،تعمیرات موبایل و برد، PLC
🔹
تربیت کارشناس منابع انسانی، فروش، مدیریت عالی کسب و کار(MBA)،فن بیان
🔸
مراقبت از پوست(فیشال)،گریم، آرایش و پیرایش،دوره های زیبایی(ساختمان مجزا)،تکنسین داروخانه
🔹
دوره های تشریفات و آشپزی(پخت نان، شکلات دست ساز، کافی شاپ و باریستا، آشپزی ملل و سنتی )
🔸
مهارتهای دانش آموزی(۷ تا ۱۷ سال)
🔹
عمومی و خصوصی، حضوری و  آنلاین در رده های سنی مجزا و مختلف
مرکز مشاوره و ثبت نام:
☎️
026-34127
@mftalborz
✔
كرج پل آزادگان ، فرديس فلكه سوم
🎯
آماده عقد قرارداد با سازمانها، نهادها، شرکتها و مدارس
📱
صفحه اینستاگرام:
https://www.instagram.com/mftalborz/
🎒
ثبت نام اينترنتي و اطلاعات دوره ها
🌐
www.mftalborz.ir
مشاوره تلگرامی و پاسخگویی به سوالات:
@alborzmft</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/655396" target="_blank">📅 10:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا عمان را برای قطع روابط با ایران تحت فشار گذاشت
روزنامه وال‌استریت ژورنال:
🔹
اگرچه عمان در مذاکرات ایران و آمریکا نقش میانجی را ایفا کرد و در اوایل جنگ اخیر برای حفظ کانال ارتباطی کوشید، اما دولت ترامپ اخیرا رویکرد عمان در قبال ایران را به عنوان رویکردی خصمانه در قبال آمریکا دانسته و مسقط را برای انتخاب میان تهران و واشنگتن تحت فشار گذاشته است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/655395" target="_blank">📅 09:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رئیس پارلمان لبنان: هیچکس جز دونالد ترامپ نمی‌تواند آتش‌بس واقعی امضا کند و او تنها راه برای این کار است/ حزب‌الله آماده آتش‌بس واقعی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655394" target="_blank">📅 09:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbfH0OiJ6qb0HGTKfdHJrkiBnmGJ_6NTwhYPmcBx2yIdlQSnaNeafLenOkX5JrBMo1KGoOrWy4D4lxY0UE9XWRKBPOo53lg8tBB3wo5X3jNrj4XaZGcx75J7P1PiheIcbSXih36wL9-YM2EHF_l-4cuOo3cBhWm5nObKzlOj3YKUEgBtkGBN2LrnpZDxsKR5epqZ3WBQv1tR7R21XCt82ko7ZKo-eUe-hLcMoeBUudnhBoMFXg7m-cmvOkvxdlDZP1ClMiZEH7GlEv5FKNJAr3mTxaifDy1EyoHMJ1w7ax2rxg-0MOEHcpYIrMJI-XWd9bhmFYmQn10X0Hu_md4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید اکانت ایکس سفارت ایران در ارمنستان: طولانی‌ترین دوره ریاست جمهوری ایالات متحده
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655393" target="_blank">📅 09:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3e885240.mp4?token=C_i-4tfFNZmC_4Sa1z1OgIhuH5uYIWUOsA4XuAoWNhhFSeHdu-USLSabyJW-YCSG2YuX1jPWG4NN8WQzp7D2Qm-vqPG2_P70TjHGwiP4ru3Aqtr8lI0rlkUbc2fIz8ItuBDbkSjXhZe3x9tSlxQjQWijbk3fABP6kKkj5nFL8jBAnv5Mqu_C-ujgFxoKO_qfLYFyMoBqywWIYOqXLTxLFlRiFnG0DK_UXEHoIWFc3i6u2rgBqwZ4Z52Ia44_z4OpfH1DopFAKdI88mbm2XEuF1vCD4uk8ATNZhljYiDX6NIpwkAq-gH6TVmkY8O3CvrU2U440z6PJjM8Jck2H5skEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3e885240.mp4?token=C_i-4tfFNZmC_4Sa1z1OgIhuH5uYIWUOsA4XuAoWNhhFSeHdu-USLSabyJW-YCSG2YuX1jPWG4NN8WQzp7D2Qm-vqPG2_P70TjHGwiP4ru3Aqtr8lI0rlkUbc2fIz8ItuBDbkSjXhZe3x9tSlxQjQWijbk3fABP6kKkj5nFL8jBAnv5Mqu_C-ujgFxoKO_qfLYFyMoBqywWIYOqXLTxLFlRiFnG0DK_UXEHoIWFc3i6u2rgBqwZ4Z52Ia44_z4OpfH1DopFAKdI88mbm2XEuF1vCD4uk8ATNZhljYiDX6NIpwkAq-gH6TVmkY8O3CvrU2U440z6PJjM8Jck2H5skEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
املت سوسیس و قارچ
یک صبحانه یا شام خوشمزه و مقوی که در کمترین زمان آماده میشه!
😋
‌
🔹
اول پیاز را خورد می‌کنیم با کره تفت میدیم بعد فلفل دلمه و سیر با پیاز داغ تفت میدیم بعد زردچوبه میریزیم و قارچ‌های اسلایس شده را به مواد اضافه میکنیم تا پخته بشه و در آخر سوسیس و تخم‌‌مرغ را اضافه میکنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/655392" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-lgwAJZ7qB3_8aIJLtxrGNcUY2wgpw-eI15XP7-nkJ7OwiVSvnPF6knktgG2mbxMoeXRdfC2w0UFzFoglCXxkoMtNXq5w_jQqbC89lkOFYrQZ0mH6wYEBRbApQPUjA3lS4Xhi-N3Rr1SfoH25AeCKbApJX4vllII77ua0lSdr8mppAPFV5BVsbx-T-FAhkFWI2KEDRFSYV72TguYmzVo0Y8JZNf3Sfzf0gcmeyjYaXiPobzWt99tRf8lFsV_lqL9OkOXnD5FeXpYiHN5z28TFqRuBuOkpxEltVudQcTXlolfsjTGSQpE3plvwgVQj-f4lxUm7A1pxVUNd05qkqKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین لحظه در سرمایه‌گذاری طلا: فروش به خاطر نیاز به پول نقد!
🔹
بدترین لحظه برای فروختن طلا، همان لحظه‌ای است که به آن نیاز داری. چون مجبوری، عجله داری و فرصت چونه زدن نیست.
🔹
خیلی‌ها توی این یک سال، فقط برای پوشش یک هزینهٔ کوتاه‌مدت، طلاشون رو فروختن. الان که قیمتش سه برابر شده، تازه می‌فهمن چقدر ضرر کردن.
🔹
حالا فکر کن می‌شد طلات رو نگه داری و در همون لحظه، پول لازمت هم به دستت برسه. این همون کاریه که
وال‌گلد
می‌کنه.
۳ مدل اعتبار با وثیقهٔ طلای خودت داری:
اعتبار فوری تا ۱۵۰ میلیون تومن برای ۳۰ روز/ وام بانکی ۱۲ ماهه از طریق های‌بانک/ اعتبار خرید کالای تارا برای ۱۱ هزار فروشگاه.
هیچ‌کدام نیازی به چک و ضامن ندارن و طلا همون‌جا می‌مونه و همون‌طور که داره ارزشش حفظ می‌شه، سودش برای خودته و فقط مبلغی که وام گرفتی رو پس می‌دی
جزئیات و شروع
👇
-استفاده از اعتبار فوری  -
وال‌گلد به کارت میاد٬ تا بدون ضامن وام بگیری</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/655391" target="_blank">📅 09:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655387">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKyJ3mfNSZIBgc83UxrK4_eORSLd2YE6C7LBkF_b5rjOWSxdyiMeVSJj2qin-dacXXbHP8SndXzEbxO7dAygrsHXCN7N-XymcqT68puFiuyrIdjPeAo7M5y9S6imUwxRrTYGHPp-QSfZR_O4axHeX-Eyn8Zrn2Cbgpx8OVyYMOjGWn091ShElhHvBV71NcTxxgrXvHeTTl8J7TDaBpg2Kk5K1Pt50cBoN57xo3pIiKGYaaVPkcfnpXpx10cWfC5EoziYw1F1nHiN9QxBtkY5nLMopHeCX6NuVRqoZ9iIpfSB-BUnzI-D6-hAbWogqMOezhk3DlMRNR0yHFZ-3t79_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF8G-howhDQJy3NJ8foGXd62xak9kHz7aO9E_2pzlo-gL66dtTTL-oA-5HAJnAHMHUK2A1HDlLqRMwkx4vc_mp5iJEL45rk-_sHJc7pUZWBRZoIHDaPPqm-QgmgiepEobu5Wg-hbtZFUiwGixTLMtpBr61mvQ4pfk4YPbG9mhRxPqfmnRmCWCz_M2ekJck-e6ZJskhg_oZWXF3aSshQZeeS0Sh2WYXUthKxkQfw9tlL2SR-8SmBpz0PoRVnRoEKJ5kP66rfm50ubc4RviLSQyUHVUuOKKFDjerg8SRHddtbDmgJf6H11u9vvjOdMPiIyEEcvnboNoJ5qYqTS4-9e5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh_e5_R57IYLDvJlKXAf4PMa_mu5tZZbi_aye4rIlqS5wP2NIrk2WyA47Al9aoBRwUMXo7La3OOSW67XJprrIo3fsA1DH05WMBMzV7coU0QUhd-_NeQtLcSI7mB2wH9P8_ZbJPZbioLmt5Y_jEUsqr-ndKg1FViCS5dVRq5LxKXXA9JKQiEAO1m_8BgfLIaRusVFrt8gRNk9ybMcN-yV4qt7pBgfEIAzdO8cHB0nNMWCsHu5mSGzP98quuOLmGq4OLrlu1YLWii1lpNNuVHCXj_J7ZIu4BaSjn-gA4JG5LDWogVH0_iPwH3NGzyAtO076yy5HUng2COhhUi2hum44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL7d3HvgDKZuWYxz0PO8Yt_1_T29g-I-5WtGcTf_HXKfvsJBQVHjAZpRAzXXDogvlbLMwqB479BmZTIJZj4Ux7XNhGuBB2zK_fBmOyngv_FFY5KqEkr4CXdq5IDWmRSIwMO4eUSD-DSbf70M713jpkloJCr0j8FBuoYRsIh7tOmMV60DgnJ8qFkxxUqqQeqgBkzah4mnhrSkUkjtXFB7Vvv4GCF14s4hnsdkUxU4kTml5vl7UF6hEDIdV-OBPd2mLvCuCEvAByviEelhpb8EnJRL9WANCLDYeYFK1we9tPcTa6yAC6rjX1JdSAiwN9iWsa9vXsx7_boX3WfernMACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رنگِ "آبی درخشان" یا "Luminous Blue" با کد «۳۸-۲۸-۱۲۵» به عنوان رنگ سال ۲۰۲۷ انتخاب شد
‌
🔹
این رنگ به عنوان ترکیبی از "تکنولوژی، طبیعت، انرژی و آرامش" توصیف شده که گذشته، حال و آینده را به هم پیوند می‌زند و یادآور رنگ‌های سُنتی‌ای هستند که از گذشته تا الان همراهمان بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655387" target="_blank">📅 09:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655386">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DikUaQOgSUTS8a11v3-QbDnjqW7_qnGrJe83buw9ufcVmXhJd3lhKTAfxXABWxtU7b6nvNSgYd9Cs8yYttREpEplfZAKv-dwMkFiwWACzhG8Cff157Piv6cgUQLZYlek9IjVlSe3o1ZG3gwtmMY0tkG-FLka6hiNbdkiAaGnmOtDYPHswtSm50TvVKRQR6G-8MLsLlqBa980LCehsigca3hkQi-gB4WqFDL6LnRdwYpxIXphSq5Hc1RbsJni1S-U6io28QnxyfcT-Q7lzIDAQKLwsj9Gz3mEXMJo4IiLKLyvCHd8dQBmzfrNEa6RibihMJ2MalJfb7K1jjCp_b9HnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا پدافند جدید ایران قواعد نبرد هوایی را تغییر می‌دهد؟ | شکارچی خاموش؛ پایان عصر پروازهای بدون دردسر
🔹
برای دهه‌ها، برتری مطلق هوایی یکی از پایه‌های اصلی راهبرد نظامی غرب و به‌ویژه آمریکا به شمار می‌رفت.
ترجمه گزارش میدل ایست مانیتور را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219663</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655386" target="_blank">📅 09:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RizwCarb8eA2DJ-LbQFfmZrzlXXER9dp4a9eIilMZnpX6WZnyWlUHSJ8BfxATIh9gES3v-LeLvM3eiiQ-9j2gZy68oR9IoOZdEQXLxwjJqL8P13KuqdI8GHU4A0p_k5DpFPzsz0YwBxx0RRf9Mv10z4l0bvXoBgGJ8nQ3Sbyx8E37HWOUpDUTMCvOCq7um9pR4B1WG53djLmVG9qeEOovxmmmSAT3Wy6XFRYkmSnZnS9gDOEOxNR7cQh_M9WbODCV755pSt0iwvBVJRrHxL2s5q6EQRTkCRNSLmjgRfzhGsnoBr2HB47qwBClFc-rLfS7NXQXg2KTvrcVByEtF-rPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت نفت: ۹۴ دلار
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655385" target="_blank">📅 09:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
یمن: اجازه نمی‌دهیم حزب‌الله به‌تنهایی بجنگد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/655384" target="_blank">📅 09:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzQLaOdiO-MVCpul6jXmm2Tru7-veQeDgiDkz1WBnMBM2mUMkYQSxdjz9H2gmOxY1s39JHDxOY7WP4T6Ore0pcrWKmkn2R4iJilk0yBCpOYFWBx2J4OVnxfA5TrSE_0qIWZz3twz2CPqy4XyHDicwBIZiKa43CUJmTGtWxPNoEXKN_5E3Uelp3_xn__ePWJ5RxjFrFKroQPdD1WmL2oM8WCqvG5utQ9GU4pDOGpsIrhzqEhbTFRHH-BRqOI_8me6jPADwiQWoewzKikivU9W1mcVGM9dwCEsliQoAKAVim4yJVe6asiRrRXlybH0fbBN-pk-L6zOWNM52Pb8-Fsxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا سرطان در میانسالی خطرناک تر از پیری است؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655383" target="_blank">📅 08:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/655382" target="_blank">📅 08:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3f80a299.mp4?token=CLlC4NWqVPAYd2BK3szjAnf1YwZHqqROsKzeDGbkZ4EHyGy1vKcWYyBfOpXYb7Vci-_eE6HhpjFO0v5HBSqcHDoLdIgxa61OSVQEZmB5uZk4BoaXZGIY56eQ0nm4QOq-euvlxtRY8LTf5pLgOvsDwwNDu_zR4cx3xzhuNgnyGyGwqQFLlV7skIbkAciTKqidDYCz4v3bCHBdx0VVsir0U_snhPxyUPUkXDMGGjtJ745GCdNmq8rlBH_CcuKVQzssoDMTIr2B2Qzm84SjeIHBWLc37HNmuZHrobjO8-lv6h_Pkelogjg9ER3RM7eSH4dhc7vTNIitIGbt6dVb4DsyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3f80a299.mp4?token=CLlC4NWqVPAYd2BK3szjAnf1YwZHqqROsKzeDGbkZ4EHyGy1vKcWYyBfOpXYb7Vci-_eE6HhpjFO0v5HBSqcHDoLdIgxa61OSVQEZmB5uZk4BoaXZGIY56eQ0nm4QOq-euvlxtRY8LTf5pLgOvsDwwNDu_zR4cx3xzhuNgnyGyGwqQFLlV7skIbkAciTKqidDYCz4v3bCHBdx0VVsir0U_snhPxyUPUkXDMGGjtJ745GCdNmq8rlBH_CcuKVQzssoDMTIr2B2Qzm84SjeIHBWLc37HNmuZHrobjO8-lv6h_Pkelogjg9ER3RM7eSH4dhc7vTNIitIGbt6dVb4DsyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف مقام سابق پنتاگون به قدرت نظامی ایران: بمباران‌ها بی‌فایده بود، ایران از حملات جان سالم به در برده و در حال بازسازی لانچرهای موشکی برای دور بعدی جنگ است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/655381" target="_blank">📅 08:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌هفتم - پادکست کافئین</div>
  <div class="tg-doc-extra">خواجه نظام الملک طوسی</div>
</div>
<a href="https://t.me/akhbarefori/655380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
خواجه نظام‌الملک طوسی
🔹
چرا در مسیر توسعه فردی و کسب‌وکار، تکیه بر «انگیزه» و «اراده‌ی فردی» دیر یا زود به شکست ختم می‌شود؟ وقت آن رسیده که توهمِ منتظر ماندن برای یک ناجی را کنار بگذاریم و یاد بگیریم برنده‌ها چگونه در سکوت، «سیستم» می‌سازند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/655380" target="_blank">📅 08:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62860bc349.mp4?token=JQEJUjCEqgJ5E4Bn4J5JB9NyU1h-x1r07lvuZZM_g5F88Vy4H_o0Sz5dcCFfp0snT4eZu1dsQTVwFeadltdqOR4C8O0aO_hry-p4mFjxqYyGGFpjieuKHiZb-sN16Vz2BmQHYPvQiEBzKIPyLMu0y4F_IQYP8pTZ5toa0Lpf8NFz744f7D9F5Htj_CKOS1esn5FmfI9AYM3uAgAG32I6s86l5dpsuZP4yuH62qY9d-S-taI8oUbgr0Xybg9NthbXgMmnOP7qCAbrO0fHYFsTRWHqUlslXHAw5T3EJO0U5NhS3BIgUuzhuJJK2IALQ7zZg0bf_sruyO8zQGYdPEPIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62860bc349.mp4?token=JQEJUjCEqgJ5E4Bn4J5JB9NyU1h-x1r07lvuZZM_g5F88Vy4H_o0Sz5dcCFfp0snT4eZu1dsQTVwFeadltdqOR4C8O0aO_hry-p4mFjxqYyGGFpjieuKHiZb-sN16Vz2BmQHYPvQiEBzKIPyLMu0y4F_IQYP8pTZ5toa0Lpf8NFz744f7D9F5Htj_CKOS1esn5FmfI9AYM3uAgAG32I6s86l5dpsuZP4yuH62qY9d-S-taI8oUbgr0Xybg9NthbXgMmnOP7qCAbrO0fHYFsTRWHqUlslXHAw5T3EJO0U5NhS3BIgUuzhuJJK2IALQ7zZg0bf_sruyO8zQGYdPEPIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویاروییِ خونینِ خواجه نظام‌الملک طوسی و حشاشین
#پادکست_کافئین
| قسمت بیست‌و‌هفتم
☕️
🔹
در این اپیزود به سراغ مردی رفتیم که امپراتوری خشن و پهناور سلجوقی را نه با شمشیر، بلکه با قلم و دیوان‌سالاری اداره کرد. او به تاریخ ثابت کرد که انگیزه‌ها فروکش می‌کنند و قهرمان‌ها می‌میرند؛ تنها چیزی که در طوفانِ بحران‌ها شما را از فروپاشی نجات می‌دهد، «سیستم» است.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/lah9ra3
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/655379" target="_blank">📅 08:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
الجزیره: آتش‌بس لبنان مدیون تلاش ایران، قطر و نبیه بری است
🔹
بر اساس ماده ۱۳۳ آئین نامه اجرایی مدارس ثبت نام در مدارس دولتی هزینه ندارد
🔹
اداره هواشناسی مازندران: دریای مازندران تا پنجشنبه مواج و تعطیل است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/655378" target="_blank">📅 08:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
انگلیس موشک ذخیره می‌کند
نشریه تایمز:
🔹
انگلیس در بحبوحه خطر فزاینده حمله ایران یا نیروهای نیابتی‌اش به پایگاه‌های متحدانش در خاورمیانه، در حال ذخیره‌سازی موشک‌های چندمنظوره برای مقابله احتمالی با پهپادهای ایرانی است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/655377" target="_blank">📅 08:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cca25161.mp4?token=i1QKCdic410cWjSWBQht352LWXpCBUUzMHGdL4ttwKBcUo1RAFh3vYCyX-t9UlXxrsQhw6-O5QuYHFu-7ZXAzZlVxlrhn20MW_jRIHuXruU56x81l0YkemVOvqhvOtwHfdo1nHm2xZO5_yqdfGOHKazXEQm4qeWj_FklyWRgVd2g8vAydOgKfj68vX6c7MciKDO-8bAagclrJaPBB1s72DR63d4J4tLbrlECUEh4Dh_PlZtVrFrD3Z2Ag1zQePU7vvCANEDOvImNMEwYHNMun1jP-kZzX-jtKQClnlzWi9q69dp6VFghf7QsIoMnEXnMGG6G_auR2yTZ_WDBSVoehA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cca25161.mp4?token=i1QKCdic410cWjSWBQht352LWXpCBUUzMHGdL4ttwKBcUo1RAFh3vYCyX-t9UlXxrsQhw6-O5QuYHFu-7ZXAzZlVxlrhn20MW_jRIHuXruU56x81l0YkemVOvqhvOtwHfdo1nHm2xZO5_yqdfGOHKazXEQm4qeWj_FklyWRgVd2g8vAydOgKfj68vX6c7MciKDO-8bAagclrJaPBB1s72DR63d4J4tLbrlECUEh4Dh_PlZtVrFrD3Z2Ag1zQePU7vvCANEDOvImNMEwYHNMun1jP-kZzX-jtKQClnlzWi9q69dp6VFghf7QsIoMnEXnMGG6G_auR2yTZ_WDBSVoehA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پایتخت اندونزی | بیش از ۲۰۰ خانه طعمه حریق شد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655376" target="_blank">📅 08:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I41_w7SIMbU0LLwZyX8bZIk6pOgCXJqkE_DASyweFwBayaYNmjyWO5_t8IWBV7bbyyHGQPaaCg4SRvnmnob8KESLpBWsTt00wJd_5aUXZzG179TEWgGCZVf0AlN3PbjDEtuaUjVhkeDSs4Icy0buQg8mKTVgW_wq7dRz6mJZMlC1yS6LZBM-fkfHFKWJ-CbipAULSUpX6o_YuBXR3s6EahwLXN_L2p02iJi5yceUdUkskMJD5Fo1laojO367NXy8G7eQoMa5W4xAObWQYuJLRZ7XsQ0BIJ3RnvmaA4dK_kELiHMaILpnX17TFAYBcZsKw_v91mZI_lAV47RZX1wicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: روزهای تاریکی در انتظار آمریکا و اسرائیل است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/655375" target="_blank">📅 08:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784e30ec43.mp4?token=TtSXpqYRCUMkrZXPbaEWSnNVqP7yyGIHpsAnQ_DUqLZJnndVFqPcCk0BdqxBcYeJnWlKEp4YKZGFXPDJdGf5aVRfX3bwZs777I2FlRjExmWDKCEtaQvuLQUmxiRkzoxFD-ZUyw6CijS4E1iQ4n-6osHyEODcgoae9ANnG3YHzvTC-p6u2UEMRJTZFmJNxS66hYyPb5yh20w-9q3IqgF-STCXPn69dRSHCmuGLxHnbEYNwbhpmLKL4Fz-Z_DETh0apTxaPxrTMUJoSPN-TY18ajqDVENlkM6P27nJuLlpItbQN3qQtk4FMN6F4tdfFlSclRrjeQ7rXz1HZJs7lFaYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784e30ec43.mp4?token=TtSXpqYRCUMkrZXPbaEWSnNVqP7yyGIHpsAnQ_DUqLZJnndVFqPcCk0BdqxBcYeJnWlKEp4YKZGFXPDJdGf5aVRfX3bwZs777I2FlRjExmWDKCEtaQvuLQUmxiRkzoxFD-ZUyw6CijS4E1iQ4n-6osHyEODcgoae9ANnG3YHzvTC-p6u2UEMRJTZFmJNxS66hYyPb5yh20w-9q3IqgF-STCXPn69dRSHCmuGLxHnbEYNwbhpmLKL4Fz-Z_DETh0apTxaPxrTMUJoSPN-TY18ajqDVENlkM6P27nJuLlpItbQN3qQtk4FMN6F4tdfFlSclRrjeQ7rXz1HZJs7lFaYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقویت عضلات شکم و و میان تنه با این حرکات #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/655374" target="_blank">📅 08:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
گروسی: خروج اورانیوم غنی شده ایران غیرممکن نیست!
گروسی:
🔹
خروج اورانیوم غنی‌شده ایران غیرممکن نیست، اما آسان نیست چون به شکل گاز و بسیار آلاینده است. گزینه‌های جایگزین شامل رقیق‌سازی است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/655373" target="_blank">📅 08:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2ac1f166.mp4?token=iW2umE5uVG_b-eyTmT2kTKLGjgE6gc7kOQLqWp0Egu_mOljW3IBVYMudB6DUDxzx4xEHVEztX8RmoKLy85DU0NcPm9rlwqL-Gun0ipBwe2sAMZrEE6v7CuQuQHw3flV5QwD52R6B-xTWKyThBhaaHsuPNrBnIk9MekjbZHwr4o4WRKmbpebmvaQNiEMmD5Ds6LCWRJ_nPcL9DCfLZ2gzx9bMYR9by1k0a7NTNCs0DsW4jEaddrEXzeTehLfi5EueFflbLaGs6khR2FoUh7vqbnuq2e_1I-_lXXQIjJMq0EBAmP4GQ9LMAXwIsn0wLmOtNrecE9lh8wIZwEgvBcclzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2ac1f166.mp4?token=iW2umE5uVG_b-eyTmT2kTKLGjgE6gc7kOQLqWp0Egu_mOljW3IBVYMudB6DUDxzx4xEHVEztX8RmoKLy85DU0NcPm9rlwqL-Gun0ipBwe2sAMZrEE6v7CuQuQHw3flV5QwD52R6B-xTWKyThBhaaHsuPNrBnIk9MekjbZHwr4o4WRKmbpebmvaQNiEMmD5Ds6LCWRJ_nPcL9DCfLZ2gzx9bMYR9by1k0a7NTNCs0DsW4jEaddrEXzeTehLfi5EueFflbLaGs6khR2FoUh7vqbnuq2e_1I-_lXXQIjJMq0EBAmP4GQ9LMAXwIsn0wLmOtNrecE9lh8wIZwEgvBcclzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیخوانا امنیت دارد یا تیم ملی با کارتل‌های مواد مخدر در مکزیک روبه‌رو می‌شود؟ پاسخ‌های جالب مهدی تاج را درباره کمپ تیم ملی ببینید
😁
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/655372" target="_blank">📅 07:49 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
