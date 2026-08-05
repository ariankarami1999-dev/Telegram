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
<img src="https://cdn5.telesco.pe/file/iTBzodE_UCx794G3vGbEbUCKZIZSVFLA0j0AHhZq8l4mOts-zDCa-Qq1pMB_hKWwAmIswISzzkha4X57htRvf3lyytkH4UgnZQDXkDEml35A9JrfHtem5bM5vIX33sAw67DSHSO1CHlXCxC0Y-JSTVmThfvC5O8G5gjRgc__W_iDL1irWry24y7L6va47caScFBjUnoX4sGnsP228kTK7P5AlCrbT5uqgF7MNgiZR9AHdMLtzo1F4U5ByUG1hSZVHJMRMy8kdv0QFy7l6NzxLuKkIOhIkVFbQHO-r_QvZs321DES5hX0dxPSfrpUHT1kcOvPTYBMr0m_67uD13Tq1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 494K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWLVSjpY8R-fTH6MeBdDzPG-8uswfQGLKQ8Z0e7TooU3YRSZ1t_Z70XRwZMrdA81nsWn5J3362sgaNHM0dtW1Cv2lH2b3nqg2jAYq1sxCQddG54v1D8y_jlOvzk5L-f8DHYTMbFxbF648C0fZo1oo_XY6jJ7ivIx2xCDx43i8lWDRbxSin-iwp_M_VeUUoVW_O0UokA1TMemUXsnS4k-wicT2CZxfTrin9dDkzUlauX9DCXsIKfhuBBi8o4fvND4HffCQW8RpRuzmCpMLYu8_WTrohFU-nNrT_6kpETk_WmPFFlGBAsiQZ0HmQ9nLda9mhRVoYPbU6LkAUPwimmOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDVQIuEVBf9PpBHSqIwcXZzfdnb5XndiO59QEDaryP165XTkxldn7AlccIjhYiittBsVGpkybOWV6FI2RaswmlSLLaaHVISCRG8eOmf9hnQJtSLLtoM0BwJ9rPiEnJExbzOGAj7vkqhQnVk8qmmIoQvbnmCSkK0Ed9BLOlL9uPWzVWyaC9xu9hDGNnC6_hW51twvfTtaNRKqn8vZPSqXuZgcpJrccjrIk3t46DL_Lis_zuctiVnFayXMQnfqZlfx6Svv13PNSoti_8B52Pi8bzUq97SSX-KkZoQneenbfjk_jT6b5sfhYnmyYJHfURKqAOZBHOpUWepRWWsqllxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0EFZeN3xeLeUGJdDzn8tLmoMj1drgpK-Kmu-HXgg6wOePobzMGQhQeuGTNLQEs7J9ksuQB59Nuc8w09uMvCncWDprDvlHI2nKb5v1EQtAYJqa8npeG042epiMzkKiMDxlfSMzOMeW2Xz6eLH7MIUyRLUivA16GFEjkeK3jet328IVExHga83WhzPSb8-nc1xtGKIcyJflf6PgwZDFsHbQygvW7SRoAKsIAFJDoDmBMwIQ1G3VHd-Gy9p4-5G2Xxlpa1do0f27CyTvzBQm6qcrONC1kYubeT_07-8CGSPqirQX61kO7DjO0fi84NNHErIpR8lngkdeQMv0WEhcjT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkYjwiq0J5LPSPOdGRTa26jMTjxNR4AEasVyFHPu5FkvzG0QyhTgaAx0c5y3TiRGi--GIMyy4DcOm7tOrrNMfJzwsFjQntfpWLzF0d0cc4TRfi51cIaxoBevwVWM9G-orfDGvo_GamIxiDkby-hHcT2E98N2eKX9OAsqanW9zwBUhDyUnknzfibflz58WAiDgz6a_owDBcxQrGp-_GzZpvity7wSK-sl3Ai9BFJs02guUSfRShtukk9PtNejvljHXAz2peBawFBGmt8gDlQ9rNSc8kVAz5EHryipIoqnXYEQpuVPqVdXxWQTyEJuWYou_XEeBS7k7xSrW7pFLbgjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPujSNbe-ZyZYG-4f6FMpP9RbMWS4xCOXtY_-_pOr6OTJ4iFLyUFPb7vBF1alcX6plDOzA6XfRuAH8qIfrKFgNyEBhrObeCpytarQZOg7y5yKgYS4Svu1OqflenYGLRpqGPQeEMxW1XIq5PUt9YFjgLNtPBqwamVw207kepcWsvS8kXk5H10KHJqVGKG5k3xu82L-LFOIhAjYfFNfDEngWh3QIswAAnsGLnmz1W7kmZVxavxXo0QkTi2dnO_wpvnkXc4ge7bjuZRzoR351SU_8Mc4QVUMULTXCXX3BmLB_nT4zQSGjSeyF20bTy-5ekvk_UUKDPzXZhWXWWesqv_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfQTDFqT15Iab5cY22cCWv8Rqz39gGqEniLvnsQwiTH5ZJlV4jEpnlfBxaL8lKrrYVOu7gEc-5h6y71mHYYSGOe3yC6KhtSL7rugBm1oylQ4MdsLglMjjhyco3V5Y5sGYE_F3a1gWA3lwu9mnw69WPWjUb20gN0lQi6Ideinl1cYiJNR2tURQj5Lu6yM9OXfIyeRa5m8HhM9EJqVt4d2mp8iyhSmP8d-HVuo3CWvZikqNwSNNvdDEdl56wa01VNtMEL4pznMpVuGpNKePEjIs6I3twpTSAOo6VbN9h8zjJKro8A9iy5IIPSboLSKOfaNbEX-O5nLm8JFILVvNAGcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102754">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بنده خدا احسان علیخانی خوب مچ میثاقی رو گرفت قبل اینکه بخواد علیه عادل کودتا کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/102754" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102753">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpSa68N18Ni385jC-I9XFsK93hsPVoO9mwOxYwsCdsJC-MSeoQzGi8MIem5yOqlMEo2zTb9daJhEJlQizfQriG22oadLWFh_NbVH39c4i_1AtDeEGMj7lT8_GEbUCIEEfNvjHyCFAgzmQ9kyqfO7l3IzsaynTnHPschNzFFnXkfwP6Pg65ppqpnwqyteBPjQKvIHzrc6AkfSaSUn-uya96pldEhvvapbFkrYdWHxL8vEHwt1lWNK2eFtksyhH_JYZXAuPFkq3GEStZ7j7r-AubdgyfHBq_tM2bVoGEC5jLS8nBWk_LKD6ydRbwn9Z1xu1XPeVRhww730xaFMB142Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
بازگشت دیومانده به کمپ‌تمرینی لایپزیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/102753" target="_blank">📅 12:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102752">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7jA_Dri-rABMwaaREtZH4-i-TRJsArb1LcAyrVemQi4VgQ4KDS50D7w2j9gx7DY7avEUd2MRpE-c3Hway-S5ze4O6fydr1pxP4wB-JrM43KXzPiR1E-QvIHlAQD3yx913LLzNlnUURN5NVIi5nl7DQKNvLYwl0xmapMb8SP-GMn1tbUvp3IebrX_oqyQPBwbM92MXihY_VDK6-IhlQ7L8HkGIOFWvNeMpzLsMx3_LBUigR6qLUzCIFhdJme1Y6wFXcnanrZTH6fLZARbuoP5FHvlmHXH86iC2UASshp36_ZXIFbUjEyD3MHVVbL0DJf8dFA_tPtHP7VJddOukMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
با اعلام رومانو، ماستانتانو بازیکن رئال‌مادرید با قراردادی قرضی راهی فیورنتینا شد
Here We Go
✅
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/102752" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102751">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_13zn0NENMR1Tj6xFSFyuZkzkUpot-bkeZ23kZtOhp9MtXEMgp54oeeJlQ4sZ6zOi__3VmDdazlCLs3Upmlai01t95wjswAIg4UlOid2SSm6OYXqJTuTqjl81G6XOl6mkkEdED07DpeJwyw75WQ5aa61MHyPLw-RqoRa1qDxafCqmLpCB3j2cgpPDs7fAVwc58AAUPyjboiiyuyvKiew5GCK2kDD-eH5pPAmSg8mmkZ-SqBvbts0GM7vsgJcsVHIOXxhbTURegxNBicxP8FcwltOi753tHN9FNuwGvzMO4XyB6wsKq7dwd8ZhBg-ijJoCdx9eRAGgQZnxW1U7qvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامین رضاییان رسما از استقلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/102751" target="_blank">📅 12:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102747">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YL5lan6UvaTHgo1s148G7UJZ7HeUmuYA1tNlT3maxCmQRAdrWE46EN-pVroSzxc9LZQ_0UAvvQ13zaqHMlDBGhnRu5nO3SfqigM2Dnf5eTc2iUV5MhIWR0HqdBQh5Rn8ttbwTGqLrIT_B7u9xA2PnHCjZU0yT83KEHbz4In3-ulORI_jcUAcQW83GS50lITXPlwXP9562lTp3J9V3VMimmaBcHUZVdQ-FBQW5EJ92sN5-P-Hy19W-JDT6BgJgE8dFcA6TOy0r0G1mIQQpKjY-4SUcsaGXxw-kLmreS9pl2bvPxGYdYACUuEMdSWVZiFrb0SI9qFm509fkQ_qkHb7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sii5pMjVrHeo5GNFhB8BXbgQ6gcAdOzMLgquI9_fm4vPxkQB_yRTVfupEcBqHIMxRFkTco0KhhlCnzUc4Bn2-CV-WY6yZQdy4zhz4KO7pwOS-Fd15MBCZWrX8uC7QPtqdqT46U5TmFwExdIAU-SEjiIwhBK3qxVBFpbmvXGLtE2Asb5SM9ECujExdjirIvZ69YfpkDjgnE6h0SQR4nXqHm5g1JCMpZUR-xeJqMJjeaVvUHI6YYgZLO7prYhsrkqiWULVcqVN3wBwKPRKP-k5awzjLxPvntgbTEgtY4KduYWbCuqRFrBxAFXzjkEKaizXI9QmyQR9q6EL3vIQkRVJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqYmCAp5ni6ukfeB-94lFL-lnX6QhMIwFY-bcI16UIkweNo42cNc8mlkBbIIeH6oOpuy4OHDYL6r80g0ry2pF8PHvBdbU5Igh0R-z-_24c6yjfbp-FOuYehX8qTi3bnWP9fUFd9939YPmBkvUtV92hCWqGYSmTJIVkXvhJv82N2i3flDzfAX0_9B_bgX6Cnwo69O9Sdi4NX0viu7eqHGe4gXG7HncWkZhBEcVpe1uxPY1ow0jDVGthd6UxO5bHdBbR1V7KtMyWTvlO--vM6HOeb-fGLzc-2yQFX2XvX29by-ZTddef79_OMeqV1OLqnEClS3vBpRiwd74nA1uTdP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d56wTIX-rWPEewTFbPyxpsXA19ff3_qgosvS5lpmWG9f1WXAXQVdZUJcb4U6wFczREpvJsafVki_7iZRdtWCD1vSfMx467BdEWyLSeY9EmcrnhG1bB4GDFwaIg-PgKTEOu6hZINTZKM8Ob2-VhF-cNLqaknloK4u9f_5Nhs00iexiqzZHTyCdWgDnyvaRF-7h7Kr298Bv3PkPhbEZdcVmO7JyvIE4Fj6Uxc_exQueOxPX_CHIny4pdTHoYwytgtWMEXrdFsXyhT4J4ul4hxwmoNQFcslkntsWN-IFhNN0pIp_we7SnDkBCklt1uziqAP0KYpSVN2qsQLioirpXvKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔺
تیم کومو 7 سال پیش تو دسته چهارم فوتبال ایتالیا بازی میکرد و حالا به لطف نتایج درخشان با سرمربیگری سسک فابرگاس اونا فصل آینده یکی از تیم‌های حاضر تو چمپیونزلیگ هستن.
🔺
جالبه بدونید مجموع ارزش کومو تو ترانسفر مارکت تو فصل 2019/2020، 2.4 میلیون یورو بود و الان به 489 میلیون یورو افزایش یافته
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/102747" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102746">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=MoZXCZGuhdVm5dk30I9ys-K-02K6mc6OrqDplWKT98bt0ODCHsnZ5VQQXDE7JeS_RzAR9YWk3JIJ7sXUH9yfjqMhg6ymMv-HdxiGP-JPDHe7Y8fI47Tu9mNoq8cO0JU_yXSVKcGpdc3QIOhPkBtqTVjsHpkn6SEgqJWFccq25OVySvIvlHCGLkBa5a2cPehEnTDn9Z5GLqOT7B1F5Fv1OKERYJGrtsr6w9M4-dqiV2ZARbyMlfGbi30ZXftPXmcLvaq8xntTDoYyPhSnVy8kU3vvOlRY6BPgNuHmCDf5I8fiA6WlYZ96RbLW5yFE9s5xjZ0nGU5MJ22G8v4t4HQqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=MoZXCZGuhdVm5dk30I9ys-K-02K6mc6OrqDplWKT98bt0ODCHsnZ5VQQXDE7JeS_RzAR9YWk3JIJ7sXUH9yfjqMhg6ymMv-HdxiGP-JPDHe7Y8fI47Tu9mNoq8cO0JU_yXSVKcGpdc3QIOhPkBtqTVjsHpkn6SEgqJWFccq25OVySvIvlHCGLkBa5a2cPehEnTDn9Z5GLqOT7B1F5Fv1OKERYJGrtsr6w9M4-dqiV2ZARbyMlfGbi30ZXftPXmcLvaq8xntTDoYyPhSnVy8kU3vvOlRY6BPgNuHmCDf5I8fiA6WlYZ96RbLW5yFE9s5xjZ0nGU5MJ22G8v4t4HQqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
✅
رونمایی رسمی باشگاه ترابزون‌اسپور از صلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/102746" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102745">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=skEL0ShAit3BxYEoS0NBSEhLCojxqyfwhmkg8CJNQFV606pcGbech3Do9JuFETC189dF7uB6RDzIRMQ3OEJF8MsiGFKyyxTrySIpo_P6fCgl2S7Jru5CKXbUYJ8YNj8tv4g0sF7cYF7MRF9cgZinlDeDwhuUmBXFErtNV19BXcRrIqqwz73YI16mKr3VdVraeqWHyLxmK48EOM4qZr9JBR6VsisTrAoAO8iRMK95DyeJfU6BlMJFeZQ1Rb_4-Dbu2xt-0f8bf-8ReN3ZKIeoIyhl6Ofl3LvBC8KPEDx_VqpS7Sp0hixAnzrUFQSgOSqSC6Bnshhgawj8fqVGTEjceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=skEL0ShAit3BxYEoS0NBSEhLCojxqyfwhmkg8CJNQFV606pcGbech3Do9JuFETC189dF7uB6RDzIRMQ3OEJF8MsiGFKyyxTrySIpo_P6fCgl2S7Jru5CKXbUYJ8YNj8tv4g0sF7cYF7MRF9cgZinlDeDwhuUmBXFErtNV19BXcRrIqqwz73YI16mKr3VdVraeqWHyLxmK48EOM4qZr9JBR6VsisTrAoAO8iRMK95DyeJfU6BlMJFeZQ1Rb_4-Dbu2xt-0f8bf-8ReN3ZKIeoIyhl6Ofl3LvBC8KPEDx_VqpS7Sp0hixAnzrUFQSgOSqSC6Bnshhgawj8fqVGTEjceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این وزن و هیکلش یه حرکتی کرد که واسه نصف بازیکنای لیگ مملکت قفله:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102745" target="_blank">📅 11:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102744">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcqfIRxofwrLuw_ZZI9k5Y6ZDjszU47rF7zQCk3omByXusK3dOM5pRYErluvAaQTzGIgxkzs7U06EqtxYVKSuSPJegWRjrm8-spNzhr12Hs1Da8L1uXbvJzTKZSxBDtszB8Twe8YexGuXqqN5K17Oi7u_7C4zBICoGWsMt038UmF_LV5I7BmDIuAuGrJo9nDwZlGsvmrh9D4m9FoJIaiSQ5QEKZL_hquWHrUOgqxWqT0s_NSoBVr6VHgfomblV33yKi6Wl19uusqFcuyIfBgN-EECr8Q5CA6eRNe-Ca0k-VTMit3ZuzTgzxPS8KRFfuzFpZGefRpTnxbvWpkmg3i8xcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcqfIRxofwrLuw_ZZI9k5Y6ZDjszU47rF7zQCk3omByXusK3dOM5pRYErluvAaQTzGIgxkzs7U06EqtxYVKSuSPJegWRjrm8-spNzhr12Hs1Da8L1uXbvJzTKZSxBDtszB8Twe8YexGuXqqN5K17Oi7u_7C4zBICoGWsMt038UmF_LV5I7BmDIuAuGrJo9nDwZlGsvmrh9D4m9FoJIaiSQ5QEKZL_hquWHrUOgqxWqT0s_NSoBVr6VHgfomblV33yKi6Wl19uusqFcuyIfBgN-EECr8Q5CA6eRNe-Ca0k-VTMit3ZuzTgzxPS8KRFfuzFpZGefRpTnxbvWpkmg3i8xcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚽️
⚽️
روزی که لیونل‌مسی به مورینیو در الکلاسیکو درس فوتبال یاد داد و پاسخ تمسخر سرمربی رئال‌مادرید رو با درخشش فوق‌العاده‌ داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102744" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102743">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102743" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102742">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXaHCFBdjt-0evBlIevLCmbAn2suwb1T2sEWVQMWpwgmLNneO4iYJOwwKyQZGImC_RLbNmFFIsZ37f2SqIrIDmjfduDyR8mSoyUcoMcRM3kSAscVA8xqRTfFwvb5gvNKIcaOYwf14NwTeO4UoV0L3tge0Te4oCxAnGwhIAiRQPpJF-NhEBkAuMMHVgpeJKVb8ItzveE_M7gIo9sy64i-ZNpS0N37knPAFFCaNIjMCYx5Oh9iZ9e0vz_LKfobkgUkV3yyAARcizld0ABgF790tqfvyxIkLb1xKfzQWe5Y0A-uNHIEAuMtqBpbyk1IMhrQKn00bB6ID4Ade1GAFhN6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102742" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102741">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=ezo4jkx3KK1ji2MM43WgXYxMaYrkruqDOMvXj99PjVFgzVDLLe7F5473R1y5-l9oaw7NFcX5q8IFxz41_jo-yJ6iC01H4_bkDcMahqGg6uW1PQtZ0b-mVJkswWhwqzI2n-MSWxEaqm60xyrCFpZdDDOtHpqQ8TbLn2aopaVVRUO6ghSvgRcVqK6r51RuUMpqywHMcahlgxynjAchRwQVmPGmetMC1a_GdmRN2CtIsqQu4VpixrdOAiC6bLm_DmXyxjdt3GAGBXTpyCkMImqFZODmlyFb1Hy6oVQJ6YrVzClwEv4Z5j3myqZJzvRsPFbTuw1sg_0Qe1Cfd0pulGxFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=ezo4jkx3KK1ji2MM43WgXYxMaYrkruqDOMvXj99PjVFgzVDLLe7F5473R1y5-l9oaw7NFcX5q8IFxz41_jo-yJ6iC01H4_bkDcMahqGg6uW1PQtZ0b-mVJkswWhwqzI2n-MSWxEaqm60xyrCFpZdDDOtHpqQ8TbLn2aopaVVRUO6ghSvgRcVqK6r51RuUMpqywHMcahlgxynjAchRwQVmPGmetMC1a_GdmRN2CtIsqQu4VpixrdOAiC6bLm_DmXyxjdt3GAGBXTpyCkMImqFZODmlyFb1Hy6oVQJ6YrVzClwEv4Z5j3myqZJzvRsPFbTuw1sg_0Qe1Cfd0pulGxFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
▶️
تیزر دیدنی ترابوزان‌اسپور برای محمدصلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102741" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102740">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqf_6JTthgi9uLRawa5VnOVDLlTua-ezXuHo9IW1HtUfCgRys7qlXpqGoJoL6OWC4eJo_Ft_2KGP3Y6f9gQhk0m_J133O9zW7glHAhNRzePAJAsmcUUbZeU0PC0c280DtIQLc-QTEtSpobDO9iY2cdQEpSJEkPDlYqFFQferhuVMUCbxkJ-h2zbG_A-ZBIOldjEIyXstcBhyxAVn9waM_XvjxFdy80V4_q3F8KDvXVklRVmmMKic0QMbHhtSMXcshMm91D2s2cVGnbmROe4DWuzcJgVRyeBWeEO0wx_tZ_1cE0YlmCr2OsMOfuG2gI5GpUGk7kG6RUSxxSci4LqpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ وینیسیوس و وکلاش برای مذاکره با رئال‌مادرید وارد کمپ این تیم شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102740" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102739">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=To1b7XoNLQW3eQTfr05aPrIEWT0aX8iCoKdajU39I9Fyo4qWDmjtFu85QJWuAGEml9d0cwiVhfBq-ELKT5dNEgwQNDhREOoVDEGOcmZffDoV6OofhGldAeSFeeJTeq_HWAKpwA0vbS2LbK4Yzi8dXcvE-styy-gPHu7GgTXMcmGyuPSO5QDQFUbrvDBdhKSFyPArugtavtD88bLrmU8NFeKfGu2VIAEU1sT7uvZjHRBGIkSgErjDV7vhNNeHApfM3NhPTSwwyr4AjD7hRW_X-GIsGQTglbp0iLgZqHRh9373iyakyXEPQ_co4NMNpoqKrez0Jb3vkp73uj9ocOHv1XHWlftN2feJwap9cUcMJiPolTogO8iNEM4XCIhKl6nS2XlfuVRjKC9GOXAacOxfsuGVMa4Zq829ZmijavN3ODJ1X7CzTmvwD7QFmbwXJrm28MSuYYIDAjBdsAHhRY6Kw9tggWMquf8iTBHoX0G3VFOvIeHryyuXSPgBgfCSXgLPdMTw-tRkY1sz-VQOVwPjdpKtgemXDHJI7xPlGwJrtJFG_2CaiHqq_5dRN6st3WaJe3Sd9jKdf_Lb9cd7ecNJltdj9JzLbcM7Ref5En_QYh55kGoz_bux_IuU8YuKzJ5XaR46mGILEbfpViOOWfvojyTlFihEVw_StTVTkT2j9VY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=To1b7XoNLQW3eQTfr05aPrIEWT0aX8iCoKdajU39I9Fyo4qWDmjtFu85QJWuAGEml9d0cwiVhfBq-ELKT5dNEgwQNDhREOoVDEGOcmZffDoV6OofhGldAeSFeeJTeq_HWAKpwA0vbS2LbK4Yzi8dXcvE-styy-gPHu7GgTXMcmGyuPSO5QDQFUbrvDBdhKSFyPArugtavtD88bLrmU8NFeKfGu2VIAEU1sT7uvZjHRBGIkSgErjDV7vhNNeHApfM3NhPTSwwyr4AjD7hRW_X-GIsGQTglbp0iLgZqHRh9373iyakyXEPQ_co4NMNpoqKrez0Jb3vkp73uj9ocOHv1XHWlftN2feJwap9cUcMJiPolTogO8iNEM4XCIhKl6nS2XlfuVRjKC9GOXAacOxfsuGVMa4Zq829ZmijavN3ODJ1X7CzTmvwD7QFmbwXJrm28MSuYYIDAjBdsAHhRY6Kw9tggWMquf8iTBHoX0G3VFOvIeHryyuXSPgBgfCSXgLPdMTw-tRkY1sz-VQOVwPjdpKtgemXDHJI7xPlGwJrtJFG_2CaiHqq_5dRN6st3WaJe3Sd9jKdf_Lb9cd7ecNJltdj9JzLbcM7Ref5En_QYh55kGoz_bux_IuU8YuKzJ5XaR46mGILEbfpViOOWfvojyTlFihEVw_StTVTkT2j9VY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
نیمار دیشب اینجوری بعد برد تیمش برای هواداران رقیب کری خوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102739" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102738">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/102738" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEk_g1s2aUTF8j9-FHKROmX8goxBjpBfKxfa0zEWldq0CdQTmZWRxsVuTO0wgybyjlCDAYM4zoJXiUq62qiZ_hC-iKI2NKVxgVM4mwpclHqc_YEWbUZJQoXptdVvx_U7QqFoLugXqS3nH9H3qWAiQDWu-Uj4X_cO9R4g22emwean-fISy75UdaAAe1gZUSfo3W7OZmKd5Uf7K49vfJB0V05P7en3pJ7xm5iiV5LZgNHPa_gLmIE5-erSb38eYs9io4NYnoMPMCY-FByYf9YGSF18lqBDGn0BPsGwm1G4yuTV2awz6UiJHNkWCg6sLLWwJtBippQHYXnpo2meL9FLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102737" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102736">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
🔥
نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102736" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102735">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45508d652.mp4?token=H4l2AAGwvkbDYgv-u9qAb611oRD-TrU2OFCr-AAX6iNPIgx0jBAhn57NAOj1pR6_DXq5lTf4w_T9_7WWo0n678ifrMyJ5kZyro0Ec_mUwOz9aQ7Rh0_bWuX-_uhNIXJYIhO-gElMdLmZjJ6_2H7f29Yjpwrd_awQ2sMEiiY0qm4wAV_njPDT5dJS32rWmYg_9wOau3axahw08rChpixPKkyjEjcd-a1XacdNSUlbjAiMOUpICDByKrSowWHpenbzLG3Yx-PTAmbWtKmT-y7BM_nVC13aRDeJ6ovC0SK0F-4357yLyv3yun1Yu6aKoi6IIjNgUrzP6XQGwHHc8mfxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45508d652.mp4?token=H4l2AAGwvkbDYgv-u9qAb611oRD-TrU2OFCr-AAX6iNPIgx0jBAhn57NAOj1pR6_DXq5lTf4w_T9_7WWo0n678ifrMyJ5kZyro0Ec_mUwOz9aQ7Rh0_bWuX-_uhNIXJYIhO-gElMdLmZjJ6_2H7f29Yjpwrd_awQ2sMEiiY0qm4wAV_njPDT5dJS32rWmYg_9wOau3axahw08rChpixPKkyjEjcd-a1XacdNSUlbjAiMOUpICDByKrSowWHpenbzLG3Yx-PTAmbWtKmT-y7BM_nVC13aRDeJ6ovC0SK0F-4357yLyv3yun1Yu6aKoi6IIjNgUrzP6XQGwHHc8mfxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل مدنظر شما چیه؟
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102735" target="_blank">📅 09:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102734">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNQeJHdyp9muzkZy1Zp2Q0xGhyZDbSpIU0BZZ-7GIAvU3m3dygSECzaOVtkow_2ovT0juHckrr8Uaf-DjA7Mm9zuSFHVE-cQ9TPI49GVry98cLRY37-f5uHZ6udu_rEgyL9GTP8cVxm9sQHMJqdVbp0cnu9Tj6mAnzISWYe9Ndw3cyxm-Uw9P1DggbMn3C1hHesk54GXM9FGChA3VRaufVVDzfIe4dArc_HRr1popCQI7X2P4yZr83omF68ugW1Pql2moTOtuU1bG7IVagqI0kbjcIFgB2IHC1ehNc9XKeRY7mV7QmuBw9L0S8a-t2Vc_PM29zcyDn5VaksT8g_SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🗓
روزشمار آغاز رقابت‌های فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102734" target="_blank">📅 09:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We2VHkbWPbPomLXdpthdLemoHycfiqL8nZkScy-6q9yXv-b9PEmNyfl1SpPZbXJDdWSoTC6m4FyeeeFTWjkaOybH98tLjB-Rnf58m719LUymANVfVaSN024e9FvgUEHhngUApNlt70EyUqfn1Snk-blv_tbiz0VU2IDwO2hSMPrQVRmZiUR31YU1Jk4I9iU_oWaxdwd3RSf50pjsX7Ex8--LaAMR76l3qo9lL8EuyXafMz0Go9RYfoubUgX6-xlNY7Oq-fOYXaxCdtfyHsWzQUrQBTkUjElUAXQpI1qvMNPIbtjybsoCTNHDkAu5xNlIRX_G9B2DbIMAPc80hjqzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیم اگه تا الان مونده بود کنار هم شاید یه لسترسیتی پرومکس میشد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102733" target="_blank">📅 09:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663702a362.mp4?token=nhFFO6n64Tyns4GC_vIs3re06ySMt0gVPtJj84vx46Kx7HwnzSdZc8Kvl5ciEl2-ERhBEvCEsexpkTJobWEOdiKUFIt2C3zixYpKuJHMBsyqIUYC1nvJ7E7hipSUovDWDE0QPLbBi1_EQMI4YUlJd_QBFZarcdxnRu8sKjNUvQqGdsKX28S9hA16GLBD-g1FU_x2TyJcuBVf3F_OhMS2AR95Gx_zmgD_GnuvcssrygSrIKsdoOgqibrS-ANmtEQqdh79q8xk7VZaVn2pZP3ZtbYRM-p5N4WgdPYFaEJcVLwV5zbhLFenwDf9StX-omo88rgT0rR4YlVcLF1ByWCHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663702a362.mp4?token=nhFFO6n64Tyns4GC_vIs3re06ySMt0gVPtJj84vx46Kx7HwnzSdZc8Kvl5ciEl2-ERhBEvCEsexpkTJobWEOdiKUFIt2C3zixYpKuJHMBsyqIUYC1nvJ7E7hipSUovDWDE0QPLbBi1_EQMI4YUlJd_QBFZarcdxnRu8sKjNUvQqGdsKX28S9hA16GLBD-g1FU_x2TyJcuBVf3F_OhMS2AR95Gx_zmgD_GnuvcssrygSrIKsdoOgqibrS-ANmtEQqdh79q8xk7VZaVn2pZP3ZtbYRM-p5N4WgdPYFaEJcVLwV5zbhLFenwDf9StX-omo88rgT0rR4YlVcLF1ByWCHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
دیماریا: دربی روساریو با حضور مسی خیلی سخت میشه، چون ما همه آدمیم اما اون از یه سیاره دیگه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102732" target="_blank">📅 09:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102731">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZBQ0UvPjeSkAIM5XXQ05YZY0GM-uJoIobbeZkM-j09BjKf1kzh2FzAP0IsTzNEFBWHEbg0P6JPhcpEtjNvnA_TguQjRZs6_33zay_bPCly3f5oR9y7dKKNApxvQ5C8fkhCv_EJbrxZFdlgOExRZO3NDuugY0UyTn9HNxT4qZFW-O-I1OW3RYfWJG9foN44wJS3xHy8LaYoY5oLQav3f4CqCukR_JL7vZ7drWwF1XJJ2L-OZFPQUyrQM-iutuIdzRHfNr6uEXRFJFn9EvLfk2RPYtqf1CFDNpovvBvZOL7tPiBGupvuuAzX9w88PiCiORVvXkq43GaFAgle3v58npA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
💔
#رسمیییییی
؛ اتحادیه فوتبال اروپا، تعداد کارت‌های زردی که منجر به محرومیت می‌شود را در لیگ قهرمانان اروپا از 3 به 4 افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102731" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYxRQ_qsTry8zeXsnrjWUic4g9S7IonhTZ9SMBdFeZyyGWbcnovX6wqVQScVOXcWeSEiSecOmYThrKlexzKQT1PXSeamZZ23Ih0C0Af70cWodBLSj6A051F7rWmi8MZ3od8_ALuZ3zLajpGS49qiXo5ZCjZthYhbQQ7UUqfC4E3ISzX9kWxfbfyBaLF0QrYxLm90KUMCXGAarunLPliYMVfRmzoctfvejiTPNNDKQC6pK_zBohjCbRSUq623Fl9GqfURtn4ZfJa4xNHs6UGDlxX9oGLmChIfvKB2znJyiUuxTizIeeM3VaLHOXCwbAeDQz4QbmeMFrOcfYGIN9fs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ به نقل از روزنامه SER، جلسه سرنوشت‌ساز رئال‌مادرید با نمایندگان وینیسیوس جونیور فردا چهارشنبه برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102730" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffk7-L3npFGMy0Flq_mWoy05F2RMmpl-LHSR0RJWoflP20YmUAPYzQRKUNCSuWJ_JeHhaSFDiF49inpzxv3sLlMrXQBVfz-7TScOYriOZm7Md33feTKsgJwIlkJcL_EmoSpCkfqp-ioBHl-Ux_NaQIiIj2QeFA7QBBTfl5s1OvEFGw9-1gZyDJ44-1-ReUZhc7T7pPqhBi4Lp8eakJPWw1__O7OWY24Ssq4cryHwGTFwED0w3-CksCDpRdkP_1tTib-HN3zBIhwI7QfmyDaMV8GwrZHn4SDXLbpEXLxCjAINbtWgORa9VqXSkyTswJvcDi2RsOwGGFJI5yEhhSsmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
👤
جوادحسین‌نژاد در مراسم رونمایی از کیت‌جدید تیم ماخاچ‌قلعه روسیه حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102729" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0hnk9ShkY1fzA7xMKcKzetk9dIdI2Vcd6ByScyE9BlBNfVR92_MAz9qmljanHcauAm3DurxUFxuPAzYG5m4tFfeCONJhlK6WLIE865hd0ORP5NoD0pumO66Wn1rDKirnYqJ9UzmYbM_-Fm7Yw5AqCQRlp2R9vetq1m-jyvhPlDcm8X8UNK66Wa40_x-29q3dTQ5IpgJU61HU2Q01JZZpym3WjbYkWgN-CHx6uAhNqZCl4kKgUOPHwCfZUA4CEJOYu6dilPqbRevUxr3PxmiAaVE6aGY8LyfyG8-ovX6iwdjgUg76kurVtjqynS_XoaGgF6WVtGs8zo5RP4OpteEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت انگشتهای دیدا در مراسم تشییع بارزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102728" target="_blank">📅 01:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102726">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
فریادهای مجری کشمیری تلویزیون جمهوری اسلامی درباره تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102726" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102725">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5XIXA2DSq7M6FhIrJJSlyrKhvzzQqP4W58NrGobspwdImmBDpanBv25uZk0CsDeUbxI1BIL89QLqUDt_i5aHhawsQg5OunaSHI1N-3FsnXCNEUZljlThfCrDCoAMBXGwfCW-jzBIGwFEEjdTQCLAkis3o0kKwtJ_Dd-b3rsqwrVNFx5WcDnYTT6P0UByaQS3K1IRtxxwF9h4eKPCGwuVw5HzWAAkrJimY9iywgj0UlXcbVRLxWpa2l8cmVtHTycdjei2y0Ejz3Ta_GkwcFpwUFOG-apN8RCUS2Ec42ZG3kOq5ANl_C7ZnvY8NyTzTei6mgL3iQONrRCx3lOfKA6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
باشگاه لیورپول درحال تلاش برای جذب ابراهیم امبایه‌ بازیکن PSG است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102725" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102724">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
بازگشت ستاره سابق استقلال در آستانه بازگشت دوباره قرار گرررررررفت
💣
💣
💣
💣
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102724" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102723">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWfzYlPl0Kvu7gJ6oRJFPqJngKzIQtRGeCqvUTCZEYAz1VgDuwLKH9XPZ5_dGkE3VG05ffE5VblPQ0thJbngueXg-Gtxqt457Yn_qyWTdZONkhe8Z0KHf6Rie6UYC1JKsuiflQ9-ZWqY7n4TN5Oqs1zWNnW50kvn7tkBSo4sUBkJDvEtIO506n2aONexXw0ty1121U6fpVGpaO-OJMVVMsdMtmJ0Moz6jWPEcKXMba7lT-hVOt5rA9okUuBPyDr9sg2MEDGN7DDiYdsCSKj5m1QPqIno9Z-WkSR6MspGukXbbokC2K3BB_K-RRxWdM5ztk5NeGEEqL2jbCzmzhHcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیکن را به استقلال پیشنهاد داده است</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102723" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102720">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUrPfvyjyjHWhr-To9k7TIIhq-6BkJFvqVduwjqd3YBG92LZYA7ggcAJob7y5zCEUB-AVAwioIK5a4PXRgjRaCKE8ffI63zTj-SxMirL6VT-d1OFHzQW6kDbO1UgDbW8ZcOMr0p4CWZKlxfdRjLDGXcj4dygW3sOMnFq02YC_LLiwpD1xyJqBCwOqozDHbiOs5bVTNk_I5CRf9UNhTCdYL6uWss4D0Mf2Yg4o7fJtak8aIwhllIYRJN8UJdWewLaFxSd41FDtqN1YwmDSj861Gk_FlkDksEI1GQih8UUNWngEukkJWy8kbsCHyV9Jq-AsiVdSUfHFKSpFGeq8ht6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMIfFiIo9fn-Z9WaloJzMk60EIxUH8kEA2XZbp1ErWMHiaW8w3at4vLO3VVumQ9kyQQMXmqSY73Je_daIJdH1ZfK-eta8S6s1IFp36sccdCwYviX4me2h34_u41d-69tmOla17BL1_tHgZ2OBDWanOzzd3gEL4eO9pOzuoUTEkaUmabLk6puVNHvQ-AMCOUmTy4VocU2Bhq7nxFu-uvKEa7quzqB4fGNQ29o91Q8e4rgQEaDqbiPCmbNTgv2RRn_jsAB9xpWLM6-pFZsN_ugvYRyfWQZLfINiV2bejOLikUkMoEp5zW0bK4L6VKztQSkk271_G9i37nhwk7y4BFczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUrsmRM4w9VPn-Pl4b6TUn10qQf6JSmArSWtXUpCSHH-yrSAR0uO80w7CXX4-s0V0KaU7Omn1RR4__riTUDEAmx3Z273GoDZJOiU_ojNOkhNNYOKqcGYp2VlK54RSKK5kELQlxv4CSOZ7Dc3i5n5rQyj56sI8euLg0K36EqZWExr_-hFO-J7mtGFBcz_iuLW_mUu3EfnX408m7Ii_0h7yo_MuTDxz3ygBGoCfkbpVVycOcQ_pHkkp-fLUzMFewsj6KD6ZegmKM-UebKMYUXP-h9Iyntb-XmiCVwtraKr7TAUO8k4W-1_P27yaoJgOCSbXuxTUO6dtGWzSa44k4dzyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو اینا رو با کپشن: « اسباب بازی های من » پست کرده
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102720" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102719">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhu0m8nJhuIwdyxLKTZkg-JDCLu-QGqKPt5AZO0zrhCf00Bet7g8O6Fu7YAT_HOvds6X6ayFZHcp1d4vZKie3SddOfjZ5lyXnSZeZiRjBT5YYhOz_9b5Upr_HYyWzWz5oWgMyrXPhChq8_SZp3mq3u1FPj-laA26g9HNkZZlhsZJgsV_dJZrqta5eYBKehR3oosjAMF13OFg8ty_k7ojBfwoiNRSP3tfzmWEvJabNagHWWIAtXPRB7cR1yDWM99e5aON2gzNlz2EC8ByP7szJfzjwdKjSTyA1o7UG0NPw9_W6vUafXBYsuPN2ZHxz3Jg4kxqKr49cN_5HYRjCUA6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
۵ سال پیش در چنین روزی؛ لیونل‌مسی اسطوره بارسلونا پس از سال‌ها درخشش بدلیل مشکلات مالی کاتالان‌ها از این تیم جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102719" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102718">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSu_oe_Auh7UGBMdqZtGESjxg3D3_xfnxPZrNIe75_RqGlU1RukzhB4oAT2sSl1L50Rz9U7bwnoHw94y_PAomZjIYR4C_R1dRu02R-Tl0F0dHYag6Uq2Gxye2ohyrWsxoQqiBxigXCXHvCfmX9uyRN4w5CCTUKnjXFUYh4o3v2sUYKshBCG_TP3Y8a06WrDkt04x7e0J1i6pU0nq_im_7wm5Vfa2AUSIQ2AHb5B4OIbjIDLh7xtDr1Ng3krfYvpST1ti9OZlzKqSa7OR6lt4Th1xtQ_fr_SrmFYu4EDLoI5ltDloATPtp0dBDFAJaLocW0IuRKCNiYD9Eb76WAydGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
فنرباغچه ترکیه بدنبال جذب پاولیدیس مهاجم بنفیکا هست و برای این انتقال باید رقمی بیش از ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102718" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102717">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfkrmJSN7-i8EOpu4q2hffjxJ9gEO7_ndi-d4nzTnTt1FjSFAeAWlvCBm3SJHRlnu492L4ySLJ5sIrWqNZV5m2uvJs60S096dE9bfrLjgvw-7IO05B1dAVmKfwG0S9ED-LIMETKCJH_OrGNuXJgTSjQ2JcqV6J69By8KfrJ1dqO29BCxI-7POBz3i5ggWAAAzCH5su-hwdk6CxDXu343L-84KFps3jZugBrThJgfpc4eMWMGY1M2WQxmnHTqDZIGuscEWb6J5QCy-39djqskQO7QHQ17y68J1wW29R0mSJw52S_z9s5a420SZJFzwsGO8JW_yOcH6H3qzAoRIPn9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102717" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTHnxdxM5M-huQtcVp809YTbWQ6kB1C0HilXnsSshgFE5fgssC-0VZMqE2LgHiaPjEHFw-Q5RbVqSJeuemhdegJG_KfbVsrxkzEAeKKS1rLohyS4rQftuULAdw6q-xZEQ9xvg7k671-i5EbWchJr3UPqUZ79sUv5UpWxvLvudchHECkxXKQp757ELAzu2rEqCSRFSPayLg8vtp3-d5PEvRVvHQ_a-oULqVRfZ7Nv-WjNxO3S7k2D2wBcBt6hYkuD3pDUiSV4WlHCYHAgF04Rv3YypYw_UShFsXMhQ3YHkPTyE2Q8UhjH9LDZ1SKGpWDhE7zEPitSe5GiF58D1jlEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5UP0zJBsVhzhz1rvsLhaif0yXTvndCI01nd_n1ZuqRrlqhy33-eK-qq8uPHObNG8wHpVZw2i0KXN15DxAv-juTRQHXSYOshw9UYVXT0CbvZzJJiESsTLgU9Lu0RPDz_5HEUEhxLnpoX3Iky1paHvPqB91e-atji6Zwq1aik5PxWYcdiaW4-cgGpug0xXOjbocYy_H6w8Rw-XzG8QofYBGEYDQYpFi9ETchgGZeYo2wWa4Rs213UTB3INB2Cr8DDznetiLZWxwtluH4A42ahgYSMF4WCAbT7_BOL225FdVdmZQ2158va3KAMZOsZ7qrQdG2H4lvdybDTPyqHbXXvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hge0yQmggCcbhCBCydkdrx_dRg5IaEyciZgGKwobSeNuYC6pbTP5UQ95vfDtLdxzuOi9d8fE_KZJ4Pay9yXN3Dm8H2RHogQZt9QcfwXVNX1Xkbir4hBMa6vrwncpnALFaQIfPT26tTIarJbzKWiIYloivh1DjrXFA88myZ8b2y1o-qqNPe-TQC4XhF0O16_pANSr-lHboHJfiXt5LSMjvU7WSTdC0JZtJPebEl7Ro_D5rgfE6iYdeHsj-YuLO87N9gf0pzJWozVmrKH6XALR0VTMobRrf0F1E7D2hIlXdepRymflr7mZgzRV7tlkUcXOuMpTQ19q3A-4qEqviSWz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIHMkWJ2vBmylzIS-Xlvo5D7p9svGngx2OEn72UtQ1JclTUL2_fOozf7iyIRB6Th_R82lk-_m_nPe7r9qXY7n5Qe0rhoUxfwRzGL6wFOKMNFMHWrTJDUpJ_pQvjXburYMeRjBLKZVXwlRD2Iad-JPV1kZZJ3k70Cm0-f6UjRegAiVhqhfBDVxN79EbTe-fBQ-HAJOsLIBlfuZZ36VomZ6gCQNJ0dwrQQV5qM2fD-oALEuyw_f2GnP9e0Znyyp2rU8IMwB2zs7O91xl2OS9MH03YGQxfNYJnpMIB3y1SCieaeHI9PVv5egfgdaCwrfUmreU-mlfNt64uQ0x5m7F4SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrjYYzzm4Nojd3rztrjdBYfJnNfvme-4nxML7MRHOl2wqZfDUjHgSgnHoq2IHKmtSHQF6jiLXmb8IdelnaacpsmeQLphBBKdsLAzhXwE6_5labmj8hF7BuwTPUf0v8ytOgm7AxEGAzcUELlzAvhD4a-raebtZ0vNGUSA9cMwDmwbc1acOsFny3pox-cMUn5gXJkru_HyCidIRxzOgfR1OPmwf2HkOz06apYyvGNMMVmpc3rYDCsEZyAcnzWrlk3ViYyb4IQfX8tOFQsDXf-NEJbolmhhrslqY-HybN5bWRtLZCqamOQpGYSNOQsqa4Kg_QQWC236qTy-FxSWA9Yzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at9g2xbaGzqwp3pA95rm4JHP3PUxNMk5BA9tpjOtdtHECQ62WvfhXNi3tH2CZs3mpwWIchcvKAdfUYx7YC4Xr0pxghzWrgtEo_MP1ekXPw8RDIEAJqaTh7t1bhPvX6e4cK9PhEjvZeDatsJpfaAn2h7_gzJ4a28tAcXWKzQgOxLc89p4AeU7Z-LvMVcA4Of6j-ukvLLLuQ7XwdTMwQtMaqXR7u_0ywNQpfSaMLFIzpsSQ9Z6VTCMiZ30Wd_Kk4wsfAil6QOkQ4nGD4Tozqy-QdFCfwyac8QpFokTIamZTm_DxHn69GSpXxWEjzPiqQKtWTePak8BClW0cXdA96UxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMayle_26TOtK7J_9IA7TDW_pnTwA_r0cnnzeZI_q5Eg5ZXeHkEr1B4gx_mJyZBe_xddbKQ8td-07HiRl-uQDGpyiIRNX5-KXefQnvQM7OVIBdMrOYJd_1ah0WwVaQ4Y0OEZCT5CRB-fhSlZP01cezGX9Xo1uwYsPSWi_PtZ0KTDiBVdIROezLaCS_SaFTze_msYlU3QrHkirRg_vh_11zi85xTvo-80MS93MphVOSkqpVnDmEkfeEACERtQS5KoUYHi6DK_cXVTTdXO-nygk3Hr6sJrvAsn-Rv1ciRhnZWDVLXX-G0ouTgYIpjmSyq0efKBONUYZCeJoD2m23saiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVndqOc5tM-lc1bpiJVz2fkk3_j6d72rJAeqNJWZwrPGf0JR6aw6MAdxqhAhoEgLbWJ71tb2WLSeSXCyv5znKaaRnf3EoPtKulsTFjE-rES-BwrRErsJmSmPYY9q3kBgLjBMTYtdc0w4OmJVbtxJb8VihOYRwNT6vIu3BviIx0s6M_l24iAuYVRxgDswHO2UhadCJQtOsH_gvndxcmaRsydYePvZgkzqWAhmtkV8buUZh0IzmOK1Mp-hhfWom0HcbvxgKZfoyjjJU_MF03p4GLpuKL348B4nG8HP0gpuUFQY344dNGM0fM8zA-9DdM4IT2qpeFOOW3RInnnPzCX0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGJG8gxBc8UhysTcR_LEgrXKpz9qDc3g5q66ADYBHn1VfBoV-jXE5AaJbOHTY8bCNkUQj6FgdvZTjRAZiOI73k0i_rjA2iREuhzFzvGzhJ3Z8_88rWvySzGDt_bJ4YJWnJf7uRhdpkW9RvMtCgZulrtst4imTR3A2powATfkN7MgeMztg-6mBjiN16vujjUmHzVZdjN8f7j0hlqLPiuEMMv-QlSJXzzLLcaBJhulYliaD8LKDhJcIxifrJ51pgygGK2Up_9Egy9Lvdo2gfgjMCvdwLQWAvYpDCmWI3QXms8gl5qyItm1EBhZOdQS4KfDrU8iZRxoQts_PyXZ0C4iEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW7_qQzPAOvHv6eiVHq6vhkD8R77o12bHAQbNxY1uSL_UUsBZk6cZnnT9lEr0OBWA2E1KQQxzo7Om8xOsuIK8ID2hiG_Iz2alqM4xkURMfNoEfKd6q9hjhmjzapjN8LuTTc9TePwagW4sdK4dX_KgCaGOL1FKfrWW52TyOxoDmjC1cfJkqzHC3hukCrAsC4fSoEIOAU7TWacAguJOr2eN7CXEcTPz2KbBi966oOc6vvVS9e-07Nj-NuzO4whSR57iWPs6-48VN03VKcY_7Gmm3xYH0Ys6VRFhJ7jClJbYBuQOsl_D4d-L3S9xUlz5O2W2i6OU1OwG_cGBMIuA3RBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxYPZRyLEnyjoegFslWzIXUmbgdmZhyjS0NU54cj-Q3oTVtFW440Ovl9gSQeqCdJvEvc4RmMXKbPTPrqhOJnb-VunjPrEbxKXsjuVsRz_qsIoqYAUoCJZo69aYDE-6d6Em0xYXFKmEpp0jAv5sCaTJu-rh_5qHv72rNzQkRBGo_XXaku7jjEDShBB44ShT8gWGt-t2XjVZ64NDZ_8U8i5UlLSL921f3GiyY2On6YDVv-veRJ9_bSkyOjGbRZ2SCkTwDF5H121p5CGaKNvcn0vAwxApR1h9o_sLHXg375D2RNqWzLDZshWnB8uPquI-4t3Iby_4DJ_eGVXiVrH1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc4YbGMVcNPeLSzeRaspAHQHIsez-55Zylyjl-3fEFmo2-qN_FZRYRVHoLaAgpYxFiodpx291KbBGpfX3gOcKfec0hxFzqU7wLmI7Yywds1F9VPVp7PUVdiu7nG6ATHGZapqTdb5hVn0pafdreId7UIF71nYXjIfSfA_28b_jRI2OQx5r09YCdnl5czAVe1zBYf6BfDvkTHrYhMd1lGjSkhFyHyj0abZCFabO99qOqt8Gxmk_joHBvhStYxARdMPRiVmUY1FAzMnCPd-d2DN5Q6I6dI6nRlQFWclO1TEx_vWfZkidEL0hz9cyGsj9PdX0ujfylSuADQtNidSBd8r6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lxRnwBA5QHIglGFVopTlnKNKI1jZOsaLYYDD9OPK_a7qXGuaEH6i26K-b6LKHtgRackHu3yWqfg9iSoR1tQc8mkuuZQGIBSQXrk6yIHCQW48uE4kyR0hzCxzCbarAdb8RcuUjLANYO5Zut0EHZvAh8KnvhgCW2pQA0mz3hbOB89PFDve3u92_iAXwnd7t0IsayFAm8EwHRKfiliCrvcgU9E3NvgmPwg3o1eOmrJoC9S_1t-OsUPhf2gbTKwK4r3k52yUST7TylzYR2OWK4zQs6YSwZ2OgTk_gtc7x2WOmiAN9_ftPNQdDCx6ZTkMneFhzTcIX4SuVZWt1YR894vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJNwkAi0zu2F_lxeGtaUozy_FqKZcJhe8t8X8j7w0MK9CteAMvrbNAy0upBcogla085h3gSy_N7HAV6txCtcpSs9_0Co3R-G8FVibJiqTeYGYKCZF9L5PN-V-B3PS4UcuMIOwGaCgSHD-VZMJW0Ya7v75G-oaMc0tObIbbmjseG7cSARlfy3FM6SAQvmTqudlPjq8ZgQ2zet-RTKC5ngo3GlH8WEviax3QjSWOKTGlfr9naFie5GH6rzL3v63Hl3I05CroSWXV1G30AM1etJtQh60_SurSPguLZoEZ1xrgYgKRexAqDGqAikxdpgn2XqMuiMwejZtQGBovXpAbWKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Xi0zXGUFmevZ_CjQb0Cx8h9XRYnRoQAcnoRLXK8bThD4f7XV-kM9U6YVZzd8leuKCPUBMKEc3iq4KG_a4bWvb3iu0--ok6ICvYPNRYA-Ouh0HsASGGjOksaSHJSaNBoO-mOLnmdYLZ3twKg56ThBT-aHdTHatznxS2h_FHII7CWjoLkhZaC54YwDMoIy6d8IQ-Bp46OrvRydQyKEbotYxqd55CKypJP_jgIv6D67uUCd7FgI278fe8cHmec3O8Q4LbjLLrr1FDBKouGYm8lkg4tl5lb1_bGnI3jLXx0VKP-6HymrVhr-2n70yPuNmgD9Se4t54ORpP9bURDdYR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJXyCjAw5gDNEDNhN283lGTQb1yobskak4nj8EgcKbsA3w1pDUn-N802y6MRfEudehSjyHeoqZWxDdHMjs6OnsouYxkasZ7_QbwOWlcEGuQulwz_pSbjI4Fwyl7idTu9cCPuNb3sm60x7PX-RkP4N6w7Tb6UAMH0bc9-I8VARQBK-B_ErDCwwkeBKhMkNx6BPnBlg2T1YFA03QM20ZszXlIF4k-ezPgWOQufC1SHml-r3prpMYWqAwBiYCK-ZbHiR2YclGRDbiWt1edsEopU8w2Tcm9Agfmc0TcDx2K1P3ZLAK1GuNT2wiC2BrcdQ4e8J7M9CFvqSqsNfIajoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsfl2lj2JMIgSlmrMCInOqgfkAxdevHeVQAZAUGEq6HZC5hJCTTlozZTxvGgZaNAyerMeVLL3uA0ctvav5EMNIyGYv0hLk1X9mmQjXDg25En-nDUdwUv7d6Jv0R-ddp_oo81a1139sd6F3gMN7XjpVKvNkmAKJs7pfU9FYN_DJp9n9rbjwA-WG9xwil_chHzbXFymUi-LUTmay79LMlBk3MMtnxpZCQmeU-z5NtGIPWZsHSqs_eeAQx6E7wpUWuB8dWXxuhwwwKa-nqWKDPaCwop5tlfuvWw3yfT1Dy7eGSX-YTmV-hm606RPA6dMgiMC-NNdo4s0QTWQhf0y01NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD2jUiZh0l6DghX-Ln8C7uA8c8ARl2q6jAz7vx_QaMm3XmUfqu3paDqlaDX_bMl1sGxsQAplXnFxgjvhzUcI4NQew8BC2Pvqg3r7Z2DW2Luxd2O5R_jjfWjaqSdRJcIhx1U5AoydVfABhlWedCct4d0EAaUjYj5kfONmIY4o3cTf6fLZYmMEHl7HurE8QEitKQlfLVD8kaqLe9i9bhPOvJtDz40BQC5c_kdSKupb9AhDN1ANam4Nl-pTceupbLf4IPlT3KCkDgZ2FeoGqFhV8g75Gh4S4LC4VTQsEeWNrYxPMxHFkHkJ5s1taCrGLlYouc1I2JPt09do8xr1gaNKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAzhvSeqx8YE2QDwDc9KvctTDESf2n3lcKlsthNPoxjylcLQfXmdX-GuAX0i2rFIq8tWjrQidvPquhfatsCOJ8zjko_ekrJnjwqVYcfxZNVfhw7Jqny4a1Y9nN37gMlwo7txgTgDGmOQLXi7UrqP7uHI8MM-5FsHX3VIgz-689hYvHOuKoTRqcmRsGOx_EJZVFq0Vc-KZx9iGejS8sYPunhv5NT-GJorKndm4nfp82dA7L1f-v5Gw7-glM1ugwdHJmgpUACIAGorPJ1Q7pJNQyVmmQ_Qe01Zo1qn0KxHG_tvkkcCspM-GasaQ-hv85JoGS4PG3YtXLFaLh_5t3UHOziM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAzhvSeqx8YE2QDwDc9KvctTDESf2n3lcKlsthNPoxjylcLQfXmdX-GuAX0i2rFIq8tWjrQidvPquhfatsCOJ8zjko_ekrJnjwqVYcfxZNVfhw7Jqny4a1Y9nN37gMlwo7txgTgDGmOQLXi7UrqP7uHI8MM-5FsHX3VIgz-689hYvHOuKoTRqcmRsGOx_EJZVFq0Vc-KZx9iGejS8sYPunhv5NT-GJorKndm4nfp82dA7L1f-v5Gw7-glM1ugwdHJmgpUACIAGorPJ1Q7pJNQyVmmQ_Qe01Zo1qn0KxHG_tvkkcCspM-GasaQ-hv85JoGS4PG3YtXLFaLh_5t3UHOziM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ دیدار فرزند رونالدو با مسی فوق ستاره فوتبال جهان در حاشیه مراسم توپ‌طلا سال ۲۰۱۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxylJGOYH8HFsHwOwwLSx1vKSsnZDZ9bxckDkNc7ewtGjlwV22D1Jfjqk6IitF1BhK_6G1yIH80Llr7bO-FsqoD6NPu19zIP6prUy7XBuupm8CIEZP6-gyggDzPX7_MlWPyrHY-Lq1hZKsNaomTwhAhPdqGvQyIwu-8xTTBTRfrBupbFPQChIEnjUopDHIcH_itVNtu8q3Cmw644-0wUNAGapNbNsSaBaQJRqAtt2nZcaEt8MTPXrhtQuukgonFCY7XQpHU9ok4igYOGZFHb7HMkwfo-OZXd25U8qqErGwGiVzrAVLQ7jnWkfkdR8CzDgNxERs4mIpl68lYJNNPy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بازیکن سال 2003 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2004 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2005 آفریقا: ساموئلاتوئو
🟠
بازیکن سال 2006 آفریقا: دیدیه دروگبا
🟠
بازیکن سال 2009 آفریقا: دیدیه دروگبا
🟢
بازیکن سال 2010 آفریقا: ساموئل اتوئو
🟢
بهترین گلزن ساحل عاج: دیدیه دروگبا.
🟠
بهترین گلزن کامرون: ساموئل اتوئو.
✨
بزرگترین مهاجمان تاریخ آفریقا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE4-o8BKimngj2V6hmWa5m1YGaBQJRPNmQHQhDYebL1G45UnBngieyC3-XJOd460tyN5YOMb4sxKsweIeonm7SLUfQefyAUrrUdpJKn2N2pduZ4G7xQnrQnWTG7YF6zV04kl5gfpDlfEI0N7agUe_eubCGDfOVNBQWG1TSGZb4bes0fiqaYZwp94I1XC_NaUqaLEQRGkbXS1r_ulThcRM9lPr-dOLMyCHCS6cz8ziJDlje0KQoTrais3mrp937r_TWXuwKY_zC65bfY_W5vg4VVA3OHLQidaYnjZ-nylXWIwXdlbfMwNdGWanhntLnzfFV5wLWJ5k_3qS6kgzXPJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAIedibtgAfqpuFnhbmI40DgrjsSPYU2XdI3QiUTYVDtZyc_IjUscdTXDh4HFVJhcWC8y5zCG49FZTRRvOAZ4kYwCP1HC8fsl0zv8d6vT1G5wvKqL84-bP7z8yeCYogrH7wsULPWAYVDfL12SjJhBjGpG46K2ndT0FN2GMj-7NuQEy0YhvmizHMOV50dUNFiqp7V39s6NCvkBNbW6z6nmuVjtbYe-q15KcS4YUq0Zvx2UrhYN8-3kF_Ol-t94sZ4q7zkh_zqakePlhLlV_Ntzl4FVRSRY-vJFNKX7N02Z2K86KSE723gzuEx2Oa1gMeKFQcb-yksofvyBuz0WcppwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7APQ9i1SCYeoLwn5uFJofVylrKUHAhDFKlcZ-9m00DDwljJiEVMkUmHUq0Rv8Nt8t_ej6YzHg4C9h5yJJSRfsJvoW-RldWOvgbpLo5Gesya_uN4UyR_ZFNJjAQ6IjlkXD3tAJpPsFVs2nlHaHSLeOWZaXqwb7gc2QntRA0JiIfZqHfRnvvaTgq6S02nKp973Wpszz1zRP2sSyAOmfHRMMVlLZPoPQ9MG8tbBlpss88puZVhcQkveAiZc_k4GDHhqnrFGTXAb_SfHNstOnmWRoOASvvz8znRt7gXA442x9tbOwSvJ9C5HsKzUVSsx8788oPTXsmx1485JrOfmlTnhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AceDAJz9KevIt_jqG7J5qMyC4bkHzsrPhPJp5-zBLv-DhbPLY8PwL2pUs04bD_1G0mTm40w26hsrBHdo6_1eN72_rplBaoK1dPhFs_x4Vsv8kqamQ3P06RM5DImNQZ_W8weli0fCw5SA7P1pDioxA35Bd9PsCIJiUX8MWu5DeJxyqatQ-VIpBUVsOREHzGCDBNxCwd6uhfEC25BgBT55NiOGMzLYEARBQBAXypCRcuFr4MZk1ATFJAAitTyKuz75IS2_y36M7UXgaqvRax5xfaFu6JSm0qO2xlPhHEQhOnrpu8dTmasBD6tGMSgH5pbVdJlHXhPpBJKzlth6SWyaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b336809.mp4?token=DRBKgIU7yKwVB9rt-r1OLEru8-UQqRwr7MxjeYIAI1WP59ze3QKERhTIJcDoC4oBnj0RcyzlbCd1wTBOf-ZJ_r2BYaTa12fbM40TWYbHbFmCuSjEdSY4e6cKkKYkLQO17FFVVbjcrUjWndJAEpf37phRuEmdAMSzxvblFJdE_UPSENIiXtygAse_v_LhXaXzXDN45iZW4Y-a-cr1kEWWxbrlCh5AXPeUtZkXANEIqgkXOcDxPbqmsr1EuofihI7j0XSFUJke2xdPnIz0MWVTRd0oUjTTZEuMWlSg-WgjdkcKmrJJFzQeRMeDUeSXVnGUuEt3XTqaaXmZg2glK3Hklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b336809.mp4?token=DRBKgIU7yKwVB9rt-r1OLEru8-UQqRwr7MxjeYIAI1WP59ze3QKERhTIJcDoC4oBnj0RcyzlbCd1wTBOf-ZJ_r2BYaTa12fbM40TWYbHbFmCuSjEdSY4e6cKkKYkLQO17FFVVbjcrUjWndJAEpf37phRuEmdAMSzxvblFJdE_UPSENIiXtygAse_v_LhXaXzXDN45iZW4Y-a-cr1kEWWxbrlCh5AXPeUtZkXANEIqgkXOcDxPbqmsr1EuofihI7j0XSFUJke2xdPnIz0MWVTRd0oUjTTZEuMWlSg-WgjdkcKmrJJFzQeRMeDUeSXVnGUuEt3XTqaaXmZg2glK3Hklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
امشب، سالروز تولد پهلوان مسعود ذات‌پرور است؛ مردی که از باورهایش عقب‌نشینی نکرد، شرافتش را با هیچ چیز معامله نکرد و در کنار مردمش ایستاد.
🔹
نام او برای بسیاری، یادآور ایستادگی، غیرت و وفاداری به اصولی است که به آن‌ها ایمان داشت.
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9AUZcFEdz84Cj6L6c3F95FfPkmhmcNLkdQmDtjw9a6WBegosY4weNHW2dTAhsQyE1aPvOjpACJE1c_OXvxL9ZiXNQl9Jo2_SR2qYHhroPBwsjnj5h1iLQ4QYOiDf6PIDoVIobQhWoGq-ToJZ5htu_GaMh2CTD12ZgiWNzUUf-kRLLKyJSKVSCsE7EbOTR4vrbjOFo8r38xgrDvWnSYhSkiUN13KYjpKUXe1ihQTRB_ATRmZuOi442vJUG6JUnqw0mjNkbPMSmyREjX2NR31VrtK-_-d_n9VGcX54yZ--vOvgIDcUwafiRbtZ--9ghKpf69O8P89vRPGAy516Fd1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=gOwxdzbl74j8OvlNJ9m-G-q09JFwAB6Ogd4iil1gn6F7QMdPau3LsZSAtg1JqQkKUZ6grznjw0QA_vPBQLFZqaGMqGvGV6bybnF0_qr3y4ErnAgpKR0DxXFOPDvxNGcoGBI-E8nqUYMQzj-zw9rFH7z2yboSHFjzJsa6g0l5cVWwHjPQ2i04mlDhBbehprZeNBtt_sblaW9TD6SCcSbXL-6LW6AQ4XfIeP0RznvlmiwyrEb9n9jo8z5aMEud0HTBtakdr1XqWYIEyxERVkzHqRBNWGGaLIEyXxdIsxcST0XoopX44pODFHOxXlnNhaJ2LPagVU-gVWDhZRHyb2UShw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=gOwxdzbl74j8OvlNJ9m-G-q09JFwAB6Ogd4iil1gn6F7QMdPau3LsZSAtg1JqQkKUZ6grznjw0QA_vPBQLFZqaGMqGvGV6bybnF0_qr3y4ErnAgpKR0DxXFOPDvxNGcoGBI-E8nqUYMQzj-zw9rFH7z2yboSHFjzJsa6g0l5cVWwHjPQ2i04mlDhBbehprZeNBtt_sblaW9TD6SCcSbXL-6LW6AQ4XfIeP0RznvlmiwyrEb9n9jo8z5aMEud0HTBtakdr1XqWYIEyxERVkzHqRBNWGGaLIEyXxdIsxcST0XoopX44pODFHOxXlnNhaJ2LPagVU-gVWDhZRHyb2UShw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#نوستالژی
؛ هتریک رویایی علی کریمی جلو کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=S4NtfgUthNx_FvswfUWHdBApgYu85dDODyoi-_c4nTFZgi-8pOpWI2pR60WSe9ajz9QvvVu2vnEIlhmhDktEdjpabS5rJRiMw8D4IBIb7DCI8TnzX01A3DdJx3x-HFRZqw3IcBxlmDxDSDgRqvf7QwHGTpVQ64-LDsjDE63PDQSEAOhOMnbRxLnbUuUhuC6eaBA7OcYMfiTsrCVVkiN6T4LicwJ65gvKCg0JPCTynEU-Il713ezMx64LIZv9RW7ibIFWANEpffhz9RJTnS-_5iAtkGSI5aaBGf6Y6rWzGoAMFo_oLoPE6M1llEKfKc78YjK-wK3tF22olughLMii7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=S4NtfgUthNx_FvswfUWHdBApgYu85dDODyoi-_c4nTFZgi-8pOpWI2pR60WSe9ajz9QvvVu2vnEIlhmhDktEdjpabS5rJRiMw8D4IBIb7DCI8TnzX01A3DdJx3x-HFRZqw3IcBxlmDxDSDgRqvf7QwHGTpVQ64-LDsjDE63PDQSEAOhOMnbRxLnbUuUhuC6eaBA7OcYMfiTsrCVVkiN6T4LicwJ65gvKCg0JPCTynEU-Il713ezMx64LIZv9RW7ibIFWANEpffhz9RJTnS-_5iAtkGSI5aaBGf6Y6rWzGoAMFo_oLoPE6M1llEKfKc78YjK-wK3tF22olughLMii7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
عشق‌وحال یامال و زیدی همچنان ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arLkpDtL5bifofTHJGe96TgnInDcp2YXr_W028jWAm3ONRXnIaw9XH6aWA-sTU4vgV6gYIRHh9dZupKtETh89NPSiQG8YmHAqEk7Esj6Vo-l64JWTfAyAVJ_O3UzfSG_GP7JfDUQ2DBDSc2rm8XtK2Dqpxd6bexIQlS3-WH4d9t_iwwAGSSaRRt0Be7cgIRdijnn8Yaj3h8VtLIoSewoSSfoNXZr8Inqrgt-DEa0nEZg71UBQwkSmzCN-t3qw0lwTf-zIDSjQMsqPEVRvTsj_qrH1BS9-hx4wXp6begFecWPz-wjjw_kEZ1ui5n_6TP5GGqC4RU_UrOmFO3kQSWhPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXVZCeDTZ6WseKWxDK1v78StypPs845Xz5PFhRT2wWJxR2b6MUS9pmPXcL5OCrtaTX03c6BqGQXaHYn63V3XeVJdJ5z__VDluv1zKRnNnJcwb_Z_3vDEe2W7oo9YxhKD57rkHlWGSWKR8CKGt2puJaTXSP2y9Cu5yGwo9ZSSIJiM1gRzXN8xak9gEUP7OhI-4knnzGZQAyC38SprrmYyxbpBmO71fQ_dfAz5yfw5rfuyX2hmrF69cADCke5bCNpPsz7ZZvNyWMXaCRD4Ad5R2iic21R-f7HUoVkIp8-y1X-lIacYGkuPbzo2jPHccwr58h0jBmmtRZoCKlm8JUhVOpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXVZCeDTZ6WseKWxDK1v78StypPs845Xz5PFhRT2wWJxR2b6MUS9pmPXcL5OCrtaTX03c6BqGQXaHYn63V3XeVJdJ5z__VDluv1zKRnNnJcwb_Z_3vDEe2W7oo9YxhKD57rkHlWGSWKR8CKGt2puJaTXSP2y9Cu5yGwo9ZSSIJiM1gRzXN8xak9gEUP7OhI-4knnzGZQAyC38SprrmYyxbpBmO71fQ_dfAz5yfw5rfuyX2hmrF69cADCke5bCNpPsz7ZZvNyWMXaCRD4Ad5R2iic21R-f7HUoVkIp8-y1X-lIacYGkuPbzo2jPHccwr58h0jBmmtRZoCKlm8JUhVOpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
هفت کارت قرمز عجیب دروازه‌بانان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgJE6qfglgOzd8sJegzddSbaqSyVW-f6Aesl1XmFdCWNWMMjWAqiAf3hqYncbiJIxzTJGI-FMyVIN0q4tFID51aO-tlUx44nlnvyEVPDV13M0RyXiKMBHADalRHrpe2nU8FiR4A8I-IF6vKhAx8uHUAEZdXr1kGcN6hkCg0VmH6l-to0vRQfW3ua4bPtzS1jWAexh_iPht4x6WqHGlObbMPZhf0GWURfz2MLfAcnAll54otZvQKmWq3ihEplk-PpG8CDB7A4hHUGAxjxFomQXcd-36LVbj3SJp64d9Q-I4zFKvM-gcV-oDaHT9-9fuDhnq3RHkFiXHxqHzd4dwofFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drToTK20eMc1wExDQxZaz88z5IaGJ_hvDHvDsEv7lcMBWLbdhEY0XdhOO8aga070AkIRX3gSx7VD5DEOfjw3FLdspeW_bDKmB9vXDe-FD5zApAxTu7Bmd1Rh-4IP0Q15cBmjy_K0dsxZ6yFTVxDkxiHDYzMUjWVYT62_Oejx81iKV-VLCeeNFf9CVe4tAsTYTlV-VacIT2AXP7YJZvmHtePyYYPdf4V9ALvqO12QdbgE7QINoUMgQYQvI4qWIvXlRRRHFbMeolBbzsU7LTty4GXH6WzagdekDhfcZp2NeG6S8GL0dOR917MCJxuOnrKeALgMvL01IrtBDSJQgl22tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=ALDGstQov7crcntJulVwhT9jTHnOC5t-9WXiKFReQ7Y9b7jm1ScQFhKl5TUR-RQMMT4iav3Ec-GFXibkLr8P0aGKnCPBA0QR4IJJG-ftkSe-ELtqw85MiyfAVh_yrN-8N1rQaeMtBgcQYEYURbheWUI_eCzYtTAaZ7gAZsv_7DtyNcG_tdhbG4vSF63IvIYzZnQPKpqy024OJxZJ6ximKmjT0ve2QCxomYF6mN5wMLxvUrfWbZQ3P-KVDvCPZvZzvuEKJPSaYUOLnSQcdaJPCJj4vNwiDQ9SC6FJoCGk3yAAUfbTHkxRcv7dDS1QbSQxr2HGGcvoQSK13rm6hsoU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=ALDGstQov7crcntJulVwhT9jTHnOC5t-9WXiKFReQ7Y9b7jm1ScQFhKl5TUR-RQMMT4iav3Ec-GFXibkLr8P0aGKnCPBA0QR4IJJG-ftkSe-ELtqw85MiyfAVh_yrN-8N1rQaeMtBgcQYEYURbheWUI_eCzYtTAaZ7gAZsv_7DtyNcG_tdhbG4vSF63IvIYzZnQPKpqy024OJxZJ6ximKmjT0ve2QCxomYF6mN5wMLxvUrfWbZQ3P-KVDvCPZvZzvuEKJPSaYUOLnSQcdaJPCJj4vNwiDQ9SC6FJoCGk3yAAUfbTHkxRcv7dDS1QbSQxr2HGGcvoQSK13rm6hsoU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
برخی از ریدمان‌های اساطیر‌فوتبال :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A75TIpPWSKikny07VCYOpNfebudpeOM41QifoS9lv_88Oy0rzXz24sC7nd_6utLFE7YikA9IfuceavISo4l2kmLb-wdoCpEcgyPZr1gHD5KCNYd2T2x6ZYSkpAuFPeDvDslzukZ0Ck7lPi_MeT88zLtKJM_92unWlb9cPaV2v_q9VDZk6J_J-pN7bH8uSqJS1izDCnmOxLTFa-HwS-1_i7vFXw9WcdqTZx4DNEfI06WSGWDOMAKOpFzFvm3RWBnD2bzoFPuXFxCK82vJtdY2UCGW9jeiKmKkNl4qYo63qBp3SqINO6ZoGz3hb5nh-NqU2hVQz0sioGENjx7Zf1WZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=W-D1uKxZH_SxyLLJKUTmfpn1EDIHjMx37joOFOAEj1mrmNlQ19ZF_XzeBfmEJgXMeEcKPk6ZT-pth9N5t0RfgjOyRZ1bm5n1ZOktq-RssRtt8E226cVuRo5KOdUaI-g2nhaoJjnuv48PMRySTeblPAqzK9Zs31bCJwClalW0rBihiLAxeGaM7tzOK1K7d7OO8FOPTr6R_tWnWVxGZEKaAoAENIqpap9Xrqv2ehgK5FiyYgfU1xQZg1gpmYij33Lm62XWYIk_kxfurk_d-ysbmDPFwYBW7MQAZfombKZJHJZx9zLd-WyqiDyKkHKhy4DW_xal4RiWce_DCbEh-M7nKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=W-D1uKxZH_SxyLLJKUTmfpn1EDIHjMx37joOFOAEj1mrmNlQ19ZF_XzeBfmEJgXMeEcKPk6ZT-pth9N5t0RfgjOyRZ1bm5n1ZOktq-RssRtt8E226cVuRo5KOdUaI-g2nhaoJjnuv48PMRySTeblPAqzK9Zs31bCJwClalW0rBihiLAxeGaM7tzOK1K7d7OO8FOPTr6R_tWnWVxGZEKaAoAENIqpap9Xrqv2ehgK5FiyYgfU1xQZg1gpmYij33Lm62XWYIk_kxfurk_d-ysbmDPFwYBW7MQAZfombKZJHJZx9zLd-WyqiDyKkHKhy4DW_xal4RiWce_DCbEh-M7nKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مثلث آلبا، سوارز و مسی که بارسلونا رویایی فصل ۲۰۱۸/۲۰۱۹ رو رهبری می‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-IyGjkiimSGHXCgJRqU59ptwmAv0AZDYqPuQRjZrBDkUl0Uu2L3hoD5r55UD5_TheK2zh0cokU-7-nmuI-OVIRPeNwPWNcr4PXEDlNKzjRqMILJH6wgAjWPA8wHvQKU0SOEKYw2nlMF8Ap9HF3JPR9BnfEG92i3TVZht5DEjAcUXtjIdzlTkboQAgDtBdM3HO0hhho5gFcK_uOaofJrzSzHMZOuK3wUDZMgneHI_ulNSYLCrgnkGeqAyHlLlidChPTZFQ3nB67vJ__Z2-VLnAbw7eAxqC2drbCWbqhwKiKzwLMGiF3bfKIF8QKM_05zDmqDzhmoAJoQsnppfPXSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jewkDhgN9Nxe45ZPqIN6Ielh2m9AevlcdAf1SEUcgEnuIaZT82iaqPOlP5Omu4-nEfdMYwlZ5--OBbVBq5-7-LMCFJf2fIybA3ir6dLnyepqpMH19OGfT6VBDm_XXqOcZfGnOa1GPna-oUfg1L5PKgkaMqueztxeLw8DPmFOcTA55LP7KBSPPHOXJtXMMUF5ERKfOuyoNuxVM9I59JCkv8a4xQBY084QAEFRv1REY9Jvdg2xa2eSW--27E8zlScF_LAdtXZPg8lRzMUCBr2badwVMCduonteMqpm9ZQosxUPVRJCTKljly8Nw1rcdQU-wqpVBF1sXZwpOcr2qg8DQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=Z51jY-mZMcaFR31btJWShDGHgeKKq62c5pnGLBFJuvSyCRAA1B7SZomPm_MX7h4iKFxUgK7XPRHkrNMhBKFOyDlG2Evr0yJaBW8A09RvVf8fnfk4yqynyVG_eP-DW2uQ1IPkSyk-ix6PlmBOWUwybUHORUJSuuT_xwe0zjFvqIxGya4sjUJrNC2mKeSievnhh1oTkLLa4Zp31qXlYric-GdF-LbXODvUk8_VNBh7zgB34G9B71qp5Jkqa7noN1GV0dJF-Ko3kmUnqZkwrPDvpudH1JUk3p4xX-QunN-8waPC9V6pl5uotZG_QPPUOHPVImBaZjSdvdXk3JpStPCc0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=Z51jY-mZMcaFR31btJWShDGHgeKKq62c5pnGLBFJuvSyCRAA1B7SZomPm_MX7h4iKFxUgK7XPRHkrNMhBKFOyDlG2Evr0yJaBW8A09RvVf8fnfk4yqynyVG_eP-DW2uQ1IPkSyk-ix6PlmBOWUwybUHORUJSuuT_xwe0zjFvqIxGya4sjUJrNC2mKeSievnhh1oTkLLa4Zp31qXlYric-GdF-LbXODvUk8_VNBh7zgB34G9B71qp5Jkqa7noN1GV0dJF-Ko3kmUnqZkwrPDvpudH1JUk3p4xX-QunN-8waPC9V6pl5uotZG_QPPUOHPVImBaZjSdvdXk3JpStPCc0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
روایت‌ایووبی بازیکن سابق آرسنال از تقابل با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7pwZuR5sbM4qFkNVikCxMLcmhcq1L-QE8F7sTDxj1EqaO9fzim_rio0A3_mI7gkuU6kHhp8shMwoXC6uTNCSQVVoLRSBleVGy64H6dkzRSA8Rb2G1OJK9dwwlp5rJ12I1qf9JMBEoImG8w-fLBFOFT8TGlc8P9mQBKhxvmDXzL24hLYEjT9yNurrIUHWMQwUX4gDpUpnUNJlwcHyVGMM4XpccSY4ciMlZpKk0paGkRqFTol1nhg-qoCL-dEe1SexTie-7VA5K_UNkpZgPnshUGpxCe_p2DIIiG5rhvDdBWooxnzuLR7-AthyvahU4CyDbZU62jbcTwVeGiRWTZhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=KIWTPX-93j5ph8VCrqSOuxgFzh3RfCJl-0fRvkB2gnLmHBUk0JVCKwQaUCoMTcg2KOlFiQMI31hkMe8GzV2TNC8zSCvdjXAHMVKqLJMbCzv-2I5r7IvuA9YZX_05DQf3-2z8WnqMDeiIwCaTohTmV26CL0N0hRszgyLFIkWOH3yhv5Y9Q6AbGsQWBMVptrezpt6Q_SsvKYvlVRuJDrf5XbUbnLD27FNkuuagdc3FPPySUzjiPN48jQbhO7aPbzBaK4a8ej1xpS2h3jn9s2TRHnOyEEuoEf9ux-mRaVWCjn31lxrB5gCa3dCSW5MkojBKhHfybOrP4vZElR6FtA674g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=KIWTPX-93j5ph8VCrqSOuxgFzh3RfCJl-0fRvkB2gnLmHBUk0JVCKwQaUCoMTcg2KOlFiQMI31hkMe8GzV2TNC8zSCvdjXAHMVKqLJMbCzv-2I5r7IvuA9YZX_05DQf3-2z8WnqMDeiIwCaTohTmV26CL0N0hRszgyLFIkWOH3yhv5Y9Q6AbGsQWBMVptrezpt6Q_SsvKYvlVRuJDrf5XbUbnLD27FNkuuagdc3FPPySUzjiPN48jQbhO7aPbzBaK4a8ej1xpS2h3jn9s2TRHnOyEEuoEf9ux-mRaVWCjn31lxrB5gCa3dCSW5MkojBKhHfybOrP4vZElR6FtA674g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اوکراین دیروز کسخل شده و با پهپاد یه ساحل تو روسیه رو هدف گرفته که چنتا مردم عادی کشته و خیلیا مجروح شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=AQfPFQmmWIOkvkCkX5sWen_qTojqwKr_ElYKMHQK7QCfm37AeUf-SaVUCE-AWJCZrmnSooN7KvF8DOZRCacyCiksgU17BW22QC-kafqIOabVt9SGkabOo2xlCQEA-w_b27iHT6Zk96J9ytT8n2cXnTrz8NEVkcvqv9txhK015_70vyWwbuidG73Vlkmhae7pXaGEF8a28fL6VE8iNfmDjg4XsqU7L0EXOqQGxkHutyIAhwSJkNJ9BKPsEKLRuXx8-62BIKBhPKStQN5ZxQXSn4VsjHx-FGXsFGrqxohDIT4iX5GTaV5fewadHf22fdcO39laD9U7NLOw3l2EHEOWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=AQfPFQmmWIOkvkCkX5sWen_qTojqwKr_ElYKMHQK7QCfm37AeUf-SaVUCE-AWJCZrmnSooN7KvF8DOZRCacyCiksgU17BW22QC-kafqIOabVt9SGkabOo2xlCQEA-w_b27iHT6Zk96J9ytT8n2cXnTrz8NEVkcvqv9txhK015_70vyWwbuidG73Vlkmhae7pXaGEF8a28fL6VE8iNfmDjg4XsqU7L0EXOqQGxkHutyIAhwSJkNJ9BKPsEKLRuXx8-62BIKBhPKStQN5ZxQXSn4VsjHx-FGXsFGrqxohDIT4iX5GTaV5fewadHf22fdcO39laD9U7NLOw3l2EHEOWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=CAYAdNmD_4Ll_oP0mU6HzUuDed4e_xQW3szKzwBJ7KscPGgRiyPxWnBYsgVpSGlwX9uVXfUaXTp3BkM_8wg09ArJWMEWarERdq1PUj3ppBwPSO4rbTqPLFY9LZM2qlVnT_te_JqJWORQ7LonkL6Snq1opLUTUVBgn9TV7luvBLcddSrcECZa1Q0KgGOFR7bigcgq75a4cB5q2Hvroy63QTvH2JbokFoQ9nJIg6qwo9akq412fXO2e8WXZaC68Num7jycVXHBYW51Cb9-6U3hUGOjhRWSbZNOrQHbyWs887n73P7FJ_sZaSHU4SWJB8jQRCv8BFV6GzmO6AdE8cdgeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=CAYAdNmD_4Ll_oP0mU6HzUuDed4e_xQW3szKzwBJ7KscPGgRiyPxWnBYsgVpSGlwX9uVXfUaXTp3BkM_8wg09ArJWMEWarERdq1PUj3ppBwPSO4rbTqPLFY9LZM2qlVnT_te_JqJWORQ7LonkL6Snq1opLUTUVBgn9TV7luvBLcddSrcECZa1Q0KgGOFR7bigcgq75a4cB5q2Hvroy63QTvH2JbokFoQ9nJIg6qwo9akq412fXO2e8WXZaC68Num7jycVXHBYW51Cb9-6U3hUGOjhRWSbZNOrQHbyWs887n73P7FJ_sZaSHU4SWJB8jQRCv8BFV6GzmO6AdE8cdgeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=F4mNw-1LvQEj-W0CD4CnaT3hifA417PvlKPsS0yQv9x3ouP8RU1EizNnJ_h7TWIDibYgsbIyYXNGWUdR3Y8mqj12QKnvh89xInf54GrrWcZEItcrMIm9zjBhoVeBBHOiApK0eq6pltBbM4PChageVaqFtwEeusA2-UUjFSaubKd3e7bv0_0AGE7RV9BssAZrciA8ABONENbcDfsUVVXluCChPB54AowraixFSf5qYfAMZky3g_vtoyDbROhaAVOrFTt40KTkzmc_KT1HEcgnJdgiXAxhPFeQlvA7M_IB-Xu7j5u9caEipiBf5RXBAsFTowskabM65SAPbIV0oe1nyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=F4mNw-1LvQEj-W0CD4CnaT3hifA417PvlKPsS0yQv9x3ouP8RU1EizNnJ_h7TWIDibYgsbIyYXNGWUdR3Y8mqj12QKnvh89xInf54GrrWcZEItcrMIm9zjBhoVeBBHOiApK0eq6pltBbM4PChageVaqFtwEeusA2-UUjFSaubKd3e7bv0_0AGE7RV9BssAZrciA8ABONENbcDfsUVVXluCChPB54AowraixFSf5qYfAMZky3g_vtoyDbROhaAVOrFTt40KTkzmc_KT1HEcgnJdgiXAxhPFeQlvA7M_IB-Xu7j5u9caEipiBf5RXBAsFTowskabM65SAPbIV0oe1nyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPbtgZePiP4J_QAjZHRojVVPYvHcum_sQ2Z1-rEhakbGbfTX1PNr2x-TEACzaTDmjjRCH4SKTwcsG0PAUmd0fB-2wgy9s6YmFx_aeIlossIUBm7IeGrhNiMadBlzgEsNHYICZjkKh2ZrNXxbm2U8tJEQjs-jUXWbI_AN3IKAPef1NkADnxwqLKZBK85z_27w4D6vmzwo-XBKdMrBxHb3uK-Vpa90VmPmdXQqSgQks8TvJew4LpMVagw0E0mJ72xjACKn_7xSoBJvXEseukEJ3zq3chNgFTB4U18pqhD_McK8BjeQuzrORrWBrrgQSe708XqM1C0bT4yJrX3OQLbEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5TiZWLsSgP7ChOIKkEtNnhwOOYctITRMjUhGCD4KiU7QRY9BIm826Z34psAGTMs4hW3UzAaoxVF-D3h6cxh6nF11NxWkKxwnKbvI2DK5HT1YsuuEqAC23hbJoGZLzBp1PccmmHBnVVZDXSf3NFStYUMXJ2zWCRuSPKESsdRuYYavtRfy9m78NFnDaixwR8oE6MNIp_7YBsuBidP878xFWqNvF5p-yuizydVJUgbN1iWIxDilc_RBro11w_bb5pdewJNbPTetLkGYqyvAl7EIGrJsEPrUrelqQvb7YgwTt8WcdeQazMq2a92gS4YiPfFD3yfWjMnPlmByNsBI_47OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxW1A-TLVnD3m8UN4feH_gVUMvwp_aN5ezFwYSu3KW9V6IknGWB6pGt43QR6a4cR_S1L31ox7iMEu891Uoj6hFmHEqyEMD9wB4EbQy4t4hndHYuk56TArzHWfxr5GKIFKz7B00TgJanN_Bq3N8XAaM3CxNwSvZee6wl5QZoT8yRz0Omait9AAutB1rafyi43CVhRhg0cnKZujI7FQCXdHiNLPo-x7526ts6ThZ7CiVs5S-9KQsE3wdPuHoN-Ytda31dpOMBFAOvp8_d3ZrKOoiYd9s6IDW8qMEfamg_0VpWvvbL3yveVPxt9uxqwqEbStKlSgXX4ZRvScHH7vUliHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MOi0qyHxBhCGweCBPSsCB-H-wnz46c9ziJ-JqMXHSELUH5m4kTHjZG-yTFy1V5eeN_x9mQNjPJvsOlfktnogMY0dAvrrtkCifAgBi022sdnmWRl-O__w1AB59B1q4ganmJMKdg-WsmDtHBoLIDpr28fDWddp5lLX-ZlPjEW9o6XdyR1cK5_DI1M-HObt0ozwctat924KeQ5y5Q1N-9C2lMe76yATXymcb-Uq15t9uSYUvHJE9Dm7H9dOf9ocbs4ERMzJVbO833YKUIlVAK0MElvMUwJzye7uAhheFzsoRYbnBRXfRfBO89CA7lf3NxJmU2Gw0laa5NFtmHCq4gZcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R77ZZpGZeOfzS_Pdbfrb5B43wZ2DEMC8oQTHbg4mUmjyfcmhaVT8-nE0fu1I3tT1NpMzhBtUcHxmRBXAIUZ6ED58vwf7ccM0cYaPTJRwUVUzsqF04qBT0-o613E2usqj1rS_1e76PLoK1w_9E8kCAh5sJMj8DSOHN4I62RbSl7auD38AhgJh3TlvFn8GgRr66xtWxOKoP11TGGWxmSt-XERaXRlr8wSJ1ix-jvHciYvVnUHEm58SahJMAHwjHQNxiH0Sl62aHYRjI02Mhyrr0DCFep0rBTyiQlybiJ-0QFURuRQuTqeeJnWifX4LDSIcMhitYgH9CvU08vQretaUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=XHr0jyWYjVfyCebkyCMZBW55mxpPgbThRF9Hq6fIbc5oenXTsSCo201NMw_ptZBO2dap8wkvzNJITPLsslDPwIeXFoiaruBfn90w_nvZmp28c8Mkanu5LJh4Im-IEfMc9Fc69bddFrh6Sqe5tmqFqyb084R45Dc_IRrYAZLRMoMqwTHjwNCBF9TJnJt1KoGSELwUSl1lyM9f2yNcGoEc4hNkBw941ng5284vfJfZ9I5COWrqoFJHcRPt4Y5b0mDF7acoUtbGgGzlw5rt8URG4pQyasGCUVi9IZC_YOHmTNfkl-CIcAMYvDjfhXqCmXhHtv3pihW6uFkelf3_jsx6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=XHr0jyWYjVfyCebkyCMZBW55mxpPgbThRF9Hq6fIbc5oenXTsSCo201NMw_ptZBO2dap8wkvzNJITPLsslDPwIeXFoiaruBfn90w_nvZmp28c8Mkanu5LJh4Im-IEfMc9Fc69bddFrh6Sqe5tmqFqyb084R45Dc_IRrYAZLRMoMqwTHjwNCBF9TJnJt1KoGSELwUSl1lyM9f2yNcGoEc4hNkBw941ng5284vfJfZ9I5COWrqoFJHcRPt4Y5b0mDF7acoUtbGgGzlw5rt8URG4pQyasGCUVi9IZC_YOHmTNfkl-CIcAMYvDjfhXqCmXhHtv3pihW6uFkelf3_jsx6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
پدر تشریفات ایران آداب استفاده از آسانسور و پله برقی رو بهمون یاد میده که بنظر هیچوقت نمیتونیم رعایت کنیم
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=qwVSylc1FPNoWLz_byaP0Yp7tRvWAf4iz2zZbOZthBQsDTd6Ux73A2kk2qlwft3oF98fSne8xJUv1ozZsZda3DLFnORhNGTqcyh2DLrd7qGP-LMfMtVxF45ax_iBVDH8-4HWp0KsuCRFU9dlfEvBOZbw2wi9zGzWLzGmRhS_cMQrdgXx9PIg0rISQaVH381y_WgNUKd2b1sFaj_1MxGKXThc4BufOJymGOivnGEqTClMpgsZn02SWJo0NMLOPxdqkX8cENromU8r3APiV1P-XGxhCBXSY4Og4wAWYUoRkikA6iFhH6mL0mCGBS1M4EpN86WEuJbNWXyz3DoBk6z2tFQGRZD5e_-oUszJlRfZhieX7NdrCvxTrvabZUQdBew-Kwnq-djWBGFVcmNKVKo69XYaCUbbNY8zN9BrODlDcBzlt1TPhNe-kB1pfnSW6ADg4dlRGYjsJGCBne6mNwNWsLCQPuRRP0r0e6huZG1FzVoA5hmwgGD9-hZ4ev1UkcxXCovxzAc4cTc-1nxCn8JjyxMWap-nkN0-4xCKRqz-uAEIlaQomb1kgz_h12O2mC5HOuiM1tSjhKveOrWapUPV3tlYh-1dggDXvy3fT7mgaCOAjHUr0DUpZodlwSp4L6rR0xp8mIanP7VqMnndVKDK7kzuVvwvgYgs1vVuUDslEo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=qwVSylc1FPNoWLz_byaP0Yp7tRvWAf4iz2zZbOZthBQsDTd6Ux73A2kk2qlwft3oF98fSne8xJUv1ozZsZda3DLFnORhNGTqcyh2DLrd7qGP-LMfMtVxF45ax_iBVDH8-4HWp0KsuCRFU9dlfEvBOZbw2wi9zGzWLzGmRhS_cMQrdgXx9PIg0rISQaVH381y_WgNUKd2b1sFaj_1MxGKXThc4BufOJymGOivnGEqTClMpgsZn02SWJo0NMLOPxdqkX8cENromU8r3APiV1P-XGxhCBXSY4Og4wAWYUoRkikA6iFhH6mL0mCGBS1M4EpN86WEuJbNWXyz3DoBk6z2tFQGRZD5e_-oUszJlRfZhieX7NdrCvxTrvabZUQdBew-Kwnq-djWBGFVcmNKVKo69XYaCUbbNY8zN9BrODlDcBzlt1TPhNe-kB1pfnSW6ADg4dlRGYjsJGCBne6mNwNWsLCQPuRRP0r0e6huZG1FzVoA5hmwgGD9-hZ4ev1UkcxXCovxzAc4cTc-1nxCn8JjyxMWap-nkN0-4xCKRqz-uAEIlaQomb1kgz_h12O2mC5HOuiM1tSjhKveOrWapUPV3tlYh-1dggDXvy3fT7mgaCOAjHUr0DUpZodlwSp4L6rR0xp8mIanP7VqMnndVKDK7kzuVvwvgYgs1vVuUDslEo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8UYwbWrUjG5ycJHO1MDpVeS0W1r2PkiIdfx39kT53imY-BUEX5TNl50jQixMhJGaTJzvkYUMHvTb4KlINgGx4iZJW2AoweGR9rO5dhVijUrq4R7skkUKZqxhd6MXOxL-Her4o3kp2XK4Q0EVSPccwIBahrc7SZQ9uyT6ensCsBfmUvCKGvhVHlRJBLTiOxKdV8ZUH75XclFwF4di1CDXwdOM0RZrncKsIfCARXGr5vbeIdILon3h6grsM1-2DQr_-vyQer5HSuz9dQrHzeu27AdJ-bNz1SBmQoZmhqu5a18nWNsXxaxjdTwBMBvEqvz_qiBX-bVWzy-0RkThpTO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
