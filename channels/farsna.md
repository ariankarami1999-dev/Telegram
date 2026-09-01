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
<img src="https://cdn4.telesco.pe/file/u41zx5H1e1syxXueR_Ee0hMXZz9GqG0-Gog22pIFIEgpNw5RcOgftO0lljIcyvMAcjmTUd5mjD1vtWA9W6jNgcASxm_9UFFoiugDlpWGZqTo7iv9prZdG0iFtiOvcEU8ZJUdwSd0Soipw3tpqx4VUaZuyzVNohozQ39USmy2w9g_rHmQygd5LqMjXb123Q7Kb--apRue9opI0jbY5_TNThFf1sl3kJ448idEPzaC8AfusLGfiPZsqLUm-nWjHAieJO337z-3VinIvP2yEFCieeILNjWLCVJ-s4VyQAVrc2QSiFg40JG6ZR1oAyg1_7LSXYQqsBX3f1QM_ayOogx6qQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-459494">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde26b3ca2.mp4?token=vFNEJXaCus2-Pm4Q_d6UWZ9eANQku3qhIKpVFnVuKf7wSj9smW3jIb2M_4Yt_Zeam8lIr_73q2W72eIvP6ve86ZPCACu8oBPwFrb9x7LIbxTDOnSq1JoAj3pLI_hQ-jslGu4F7fxG57NwJVa5PW4OQcuzbPFj9sNzxl_CB48BMqFdsu2BXITBEYelViihxC_cZ-8MWs1s2Q4LwjkXoUA_9BJ1kSq5i3zHE12gl-eHF559mPGePdEGd4zBOt_1zoiUlcpV_Yrf_xEM30dXaH9W_r-qmL5qD22fch-gAPIUO2aox8bB3MUTkD5LTr01hXcCfQqnkbt6VZtP0IpDs7IaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde26b3ca2.mp4?token=vFNEJXaCus2-Pm4Q_d6UWZ9eANQku3qhIKpVFnVuKf7wSj9smW3jIb2M_4Yt_Zeam8lIr_73q2W72eIvP6ve86ZPCACu8oBPwFrb9x7LIbxTDOnSq1JoAj3pLI_hQ-jslGu4F7fxG57NwJVa5PW4OQcuzbPFj9sNzxl_CB48BMqFdsu2BXITBEYelViihxC_cZ-8MWs1s2Q4LwjkXoUA_9BJ1kSq5i3zHE12gl-eHF559mPGePdEGd4zBOt_1zoiUlcpV_Yrf_xEM30dXaH9W_r-qmL5qD22fch-gAPIUO2aox8bB3MUTkD5LTr01hXcCfQqnkbt6VZtP0IpDs7IaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
عراقچی: بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است
🔹
خوشوقتم که همراه با رئیس‌جمهور دکتر پزشکیان در اجلاس سران سازمان همکاری شانگهای در بیشکک قرقیزستان حضور پیدا کردم.
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی، بر…</div>
<div class="tg-footer">👁️ 538 · <a href="https://t.me/farsna/459494" target="_blank">📅 19:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459493">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3nzIGYsBETIN90y030qbCgHRT6QTK7SoQaBMiUU9bbH7g39tpEoteaR_VblBQvbFwa6czFcExHnHjshD9hVhiEWxiYGmfVNNClloeAJv4_XWafrcKCdjvCVXXfgFgZbC3iv1UMc-hN2eGe5mpwAizOQVVQHy3fKT5MNTsxr4VQ7Ve-CVhiIDPzWq7e0bOjOdHSol-lRqX7gxtsbXAvZErn3CMacF70Tz09qGI563UNsfvLHsoA2dCIUJPtZAHyg9qiYuDzO8my4OG0Mlt-vab11tRIWzfOigIiB2l22P4fhncxBqS-xFqLSt5CNpoQIjj8ivOd2ZKzGz72IREQAHvlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3nzIGYsBETIN90y030qbCgHRT6QTK7SoQaBMiUU9bbH7g39tpEoteaR_VblBQvbFwa6czFcExHnHjshD9hVhiEWxiYGmfVNNClloeAJv4_XWafrcKCdjvCVXXfgFgZbC3iv1UMc-hN2eGe5mpwAizOQVVQHy3fKT5MNTsxr4VQ7Ve-CVhiIDPzWq7e0bOjOdHSol-lRqX7gxtsbXAvZErn3CMacF70Tz09qGI563UNsfvLHsoA2dCIUJPtZAHyg9qiYuDzO8my4OG0Mlt-vab11tRIWzfOigIiB2l22P4fhncxBqS-xFqLSt5CNpoQIjj8ivOd2ZKzGz72IREQAHvlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هفت روز جنگ، ۱۵ استان را سرکشی کردم
👤
پورمحمدی در بیست‌ودومین قسمت برنامه ماجرای جنگ۲
🔻
قبل از رسیدن به هر استان، به آنها خبر نمی‌دادم تا متوجه شوم واقعاً در استان چه خبر است
.
🔻
در همان وسط جنگ، با استاندارها درباره پروژه‌های توسعه‌ای استان برنامه‌ریزی می‌کردیم.
🌐
@majaraa_media
نسخه کامل و با کیفیت را از
سایت
و
آپارات
ماجرامدیا تماشا کنید.</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/farsna/459493" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459492">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJcBv2ZCJLNU_QZxc1YwRh6KgvcFr-Xk6SeswHmrUkoAqc1bwOWkIfnYvIbNwnKQTGaeJcpOAFYM5uccsN2M1VNFJuHhoef6N2DJjsvZTrFI4cFYfUJEBfa7WMFvgNmX-y0ftMH69GADleGJnDv6MGl4xgPMVpjZcQMOqqX2zB395ERaPFCs45NEy3Hx6JS4uHyEK0DI3ZIx0wyXfMhqFCIIWtlaqzZBRLBlun1IvTn9MDw5kQ5lxxiedKGSrgAi2NrftY1YWC0bFd0GyglgAQFoXeS3mFL_ApecvzFh_tKihEP4VIa0HqeOwTqPllkeZUPFqMWkd8Ma7NgUNKQaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم روند مثبت درآمدزایی بانک پارسیان؛ تراز عملیاتی مرداد ماه از4 هزار میلیارد تومان عبورکرد
مجموع درآمدهای عملیاتی این بانک در ماه مرداد به ۱۱ هزار و 360 میلیارد تومان رسید که نسبت به تیرماه (۱۰ هزار و 311 میلیارد تومان) رشدی حدود ۱۰ درصدی را تجربه کرده است.
در بررسی عملکرد پنج ماهه نخست سال ۱۴۰۵ نیز، بانک پارسیان با کسب ۴۴ هزار و 615 میلیارد تومان درآمد عملیاتی و مدیریت هزینه‌ها در سطح ۳۳ هزار و 725 میلیارد تومان، موفق به ثبت تراز عملیاتی مثبت ۱۰ هزار و 890 میلیارد تومان شده است.</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/farsna/459492" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/farsna/459491" target="_blank">📅 19:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-TopaHmxlkZA7siDahiCuM2qip50sCZJOGJHtKYcVmd2SvaQzW9ch-z2slYgoBPGDBVKold8kWpAbvxJfuKGDt4NM1IMDp5zU5__IrCXS71WYTuytf_ZrQNCj9FWW3UTBkzkGbsRAZv1HXwr7D1wQMPLP_Pv7cH4q9VpgJY9wHPdOlamxlC6ggWf5K1OS3ZnCsJFbQoixxEdwuqz2akf9CabhxzrMD7cWcRmKQ9j_8bAfeBEoWDez56Q7F-lHgCk5ifOs-0TcNh_J3RQwz9Jnw_Kyr_4DKJxnwl_YYKxCYREIIobkQkLdzMDAe24OgS6a2JeKY2SHWzRxBOx8T_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است
🔹
خوشوقتم که همراه با رئیس‌جمهور دکتر پزشکیان در اجلاس سران سازمان همکاری شانگهای در بیشکک قرقیزستان حضور پیدا کردم.
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی، بر دفاع اصولی ایران از حاکمیت و تمامیت ارضی خود و بر ضرورت اتحاد برای مدیریت روند افول یک امپراتوری بیمار تأکید کردم.
🔹
بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است.
@Farsna</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/farsna/459490" target="_blank">📅 19:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqa4qpvzAztOFwZWivQmBb5QU5P44HnglD_VkupgJlj8R_bHDd509NF-snZ8_VWGPddInrmjLfumQxPgMQstiyt-DXdPXfoHnodCH7isqqaMX-DFnaoOBiajsKrQZ07664BL6Nq-_kR7e4Z2fc6pRH0T0peTrmEkfmi8iJQ_bjos0uP1QABEdP0D_FTRTIoD9Dhx8rsL3B60NIYsW3dsm3i7OcJAi-1oD5O1JPKmWFjabYZAEeZVoM4XQlIwY_Dv__fRWRYL75jvRstMNrNlIP4R2a-tJW-sZzEHjmiPMTWBl1AXVIFNulS19sANEsX299bnHB-GHoFjGxMWqZMuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با گوترش: سازمان ملل باید در قبال تحولات بین‌المللی نقش‌آفرینی مؤثرتر و کارآمدتری داشته باشد
@Farsna</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/459488" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9aac287a.mp4?token=vMCjq-2CcCw1eDFre9fIDzgYTDS3PNOu7ul7-2esAs-lYgMT1VeYoMGBUAN6n_fhlvVMkDZqo9HkqQzQ6vERIje3wwu3ZUUDbrPmZye2VEH9k06OnEtu_jniUTDfN60QTa_22W_hxAvaIMBI7ssdd0IwuWr7Tez4QtLDfZwlOXBV7zsmSYH6cyFF3zH53EeV6Mt9Vw9Un01_azMgVW5u1gaLK3VmzbkzfL1YqjddD57Ebjzw-1i0fba-4_oD1MTaCuFGME60BAWQY4x6QKOpWQHBZnHkLMsLoRL4SBgaZS71l97yabNMx0lM5jmeEbnUwLvV7KXM6u9FiF2sfk85Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9aac287a.mp4?token=vMCjq-2CcCw1eDFre9fIDzgYTDS3PNOu7ul7-2esAs-lYgMT1VeYoMGBUAN6n_fhlvVMkDZqo9HkqQzQ6vERIje3wwu3ZUUDbrPmZye2VEH9k06OnEtu_jniUTDfN60QTa_22W_hxAvaIMBI7ssdd0IwuWr7Tez4QtLDfZwlOXBV7zsmSYH6cyFF3zH53EeV6Mt9Vw9Un01_azMgVW5u1gaLK3VmzbkzfL1YqjddD57Ebjzw-1i0fba-4_oD1MTaCuFGME60BAWQY4x6QKOpWQHBZnHkLMsLoRL4SBgaZS71l97yabNMx0lM5jmeEbnUwLvV7KXM6u9FiF2sfk85Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: همهٔ اعضای شانگهای بدون استثنا، تجاوز به ایران را محکوم کردند  @Farsna</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/459487" target="_blank">📅 18:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e7c1d89b.mp4?token=Zr3YdXSSs2KxqIS8NlXByiwEzFhtU0xhkw3C3oJ1ZVN7F3V7ipbnyVv7kbP5sPPRgzP9-K1EQn6hCOKXShmi9v1pMm62qVD3ta3BCSBODKpbn_V7vb8H5Rbsw6yRoPkArBiONk381N0BCb3aEQE9twigsIJP7ljNlKmP-6UadQeoQKI542KO8yJr-m_ZpzFFXQKsfVlZ3lsbVkaRmpQzReQBNKBIuZY2fc47joOY7bc5ucZiTxN2P19ai-_vCkAvZ8gQOedbSRL_2Wzpu6q5nkIULjIJy1WKdym_e_yyALqPHKu76hb_QgbEzkvQLLKuEShQznKipQ0klsxl1Md4RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e7c1d89b.mp4?token=Zr3YdXSSs2KxqIS8NlXByiwEzFhtU0xhkw3C3oJ1ZVN7F3V7ipbnyVv7kbP5sPPRgzP9-K1EQn6hCOKXShmi9v1pMm62qVD3ta3BCSBODKpbn_V7vb8H5Rbsw6yRoPkArBiONk381N0BCb3aEQE9twigsIJP7ljNlKmP-6UadQeoQKI542KO8yJr-m_ZpzFFXQKsfVlZ3lsbVkaRmpQzReQBNKBIuZY2fc47joOY7bc5ucZiTxN2P19ai-_vCkAvZ8gQOedbSRL_2Wzpu6q5nkIULjIJy1WKdym_e_yyALqPHKu76hb_QgbEzkvQLLKuEShQznKipQ0klsxl1Md4RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس اقتصادی: سیاست قیمتی برای کنترل مصرف بنزین، به دلیل نبود خودروهای کم‌مصرف جایگزین، با شکست مواجه شده است
🔹
محمد‌حسین صبوری، کارشناس اقتصادی: مصرف سوخت ما نسبت به سایر کشورها در سطوح بسیار بالا قرار دارد و بخش عمده‌ای از این موضوع، ناشی از استفاده از خودروهای فرسوده و غیربهینه است.
🔹
با وجود اینکه تکنولوژی‌های جدید وارد شده‌اند، اما بحث اصلی بر سر سیاست‌هایی است که باید در حوزه خودروسازی اجرا می‌شد تا این وضعیت تغییر کند.
🔹
نتیجه این اشتباهات امروز در قالب ۲ چالش بزرگ خود را نشان می‌دهد نخست، وجود انحصار در صنعت خودرو و دوم، افزایش بی‌رویه مصرف سوخت که ۲ یا ۳ دهه است کشور را آزار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/459486" target="_blank">📅 18:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd4e0f9f7.mp4?token=o0W4list1jI-iYYrlcz4t2qcCFb_IlgQfakgs3_WoJ6gdYc4EEnp90USSoV_HkMpRu2NKmHhjr9OFCIjMAfr1OuZ0wjml7lC-1LClmACs9c9J71iahJHAh0Upgri3bpMQYZzd-sTFFnSOlye2oASR3h0ucbrkQQ9ypeAwXCejvlD74RD1gpb-xmSsaQhfKigZj_e_tHoMmcOnHsF7FpayuhxrBeBDWrcT7E5-cN18L4FIo1DHPKbOxTcg9FzVhpiW24I8jMhIbu_jfkD0iic71BfE0E1QgPhntZpUSwgh0jww-5za_IBJk4P1lnCed4opNfbp0AcFsC4WhQTwz3NHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd4e0f9f7.mp4?token=o0W4list1jI-iYYrlcz4t2qcCFb_IlgQfakgs3_WoJ6gdYc4EEnp90USSoV_HkMpRu2NKmHhjr9OFCIjMAfr1OuZ0wjml7lC-1LClmACs9c9J71iahJHAh0Upgri3bpMQYZzd-sTFFnSOlye2oASR3h0ucbrkQQ9ypeAwXCejvlD74RD1gpb-xmSsaQhfKigZj_e_tHoMmcOnHsF7FpayuhxrBeBDWrcT7E5-cN18L4FIo1DHPKbOxTcg9FzVhpiW24I8jMhIbu_jfkD0iic71BfE0E1QgPhntZpUSwgh0jww-5za_IBJk4P1lnCed4opNfbp0AcFsC4WhQTwz3NHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: همهٔ اعضای شانگهای بدون استثنا، تجاوز به ایران را محکوم کردند
@Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/459485" target="_blank">📅 18:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSnR2Y-ZjOUKyLL1PHEqP-h6_wT9hdxQECGXj6B6lHYOwx0uLamk4UaVJP8MEUETy0GjWOLFx5_gXvhOtXKedSNtU-xyBEXUmxxBEarQwFiRD1wbVu5dmvxjVOzVdGyi66GhlvRmVCxfas9Nwn-tg7k-VPV_8fasNcVlXexWmV9ZY3ogfdYy8RhXgwrki1f0FX1H58C1m0t3JxVMy4WJ4espOLBPANgYvlTj6dF7jB48NS59lFTaZU1beo9loNRXpZ-CNZ2wx0G_8xom9tu6JZCBzTb2YPpPpMrgs0DX9rXIMiUXOhualgKNXq6Ihcv6HCnWkZGh3Wy-L6qpa8MVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها قانون بانکداری بدون ربا را کنار گذاشته‌اند
🔹
رئیس شورای فقهی بانک مرکزی: نظام بانکی قانون عملیات بانکداری بدون ربا را بوسیده و کنار گذاشته است. به نرخی پول می‌گیرد و به نرخی هم پول می‌دهد.
🔹
بانک باید پول و منابع را به عنوان وکالت از مردم و سپرده‌گذاران بگیرد و به سرمایه‌گذاران بدهد، وقتی سرمایه‌گذاری کردند ببینند سود تحقق یافته چقدر است آن را تقسیم کند سهم خودش را هم بردارد.
🔹
قانون عملیات بانکی بدون ربا سال ۶۲ تصویب شد و چارچوبی را تعیین کرد که در آن بانک به‌جای دریافت و پرداخت بهره، باید منابع سپرده‌گذاران را در قالب عقود اسلامی به فعالیت‌های اقتصادی اختصاص دهد، و قرار بود از سال ۶۳ اجرا شود اما این اتفاق نیفتاد.
🔹
در حال حاضر بانک‌ها برای سپرده‌های یک‌ساله ۲۳ درصد سود پرداخت می‌کنند و برای سپرده‌های کلان، نرخ‌های ترجیحی تا ۴۰ درصد دارند.از طرف دیگر برای پرداخت تسهیلات نیز همین روش را اعمال می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/farsna/459484" target="_blank">📅 18:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST6aZF9O3JIrQNqkuFUJTwnkcBdf7slD-2rLKPi1b2f4HMrtHya6w8uYombJscrZGQBd_UastQevHM5HN45hmhCzVc7JvVeIRQpwAzQbP0D_hLywnNUmpWwNKO9GdbGcgF4bpE8pZ-dMmI9dfAfe8K8aObMmrfXnjoPmYoj9y43FJylbOWR5GLoLfuGHOCxfEoNixP37H8V5drsR1AohwPsci3Wo4zyhkXhMocQcQU963NHCUXsMjifoRl4ktY8b2cqkfFmewhEmo9kTDU_MvnaQYqpzydhXLNdaNMF2QuwuQq5kVggJ3f04dXbwJXKR6JINWkxhpvjviEorEzAfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبۀ حمایت از خریداران خودرو باطل شد
🔹
سخنگوی شورای رقابت اعلام کرد دیوان عدالت اداری با رسیدگی به شکایت خودروسازان، مصوبۀ ۴۷۳ شورای رقابت را که برای حمایت از خریداران خودرو در برابر افزایش قیمت تصویب شده بود، باطل کرده است.
🔹
براساس این مصوبه که در سال ۱۴۰۰…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/459483" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25637cbe58.mp4?token=ilqi-I8Ip32vXHO3REoS4P9CaMiej50PWVwetwwYFHFQKbgACTo12YFTdnmemFCd4c3aris-oPvX56tZj_I6tEvEGDixwvRA-AidbmH5uF5rNiRjkS46O3366DDKtISiMXITl-9qTPb3YWjfJftaex3iffQiZJpLqSQMB2GJeQcc9-8J7CcZqJqhx6kMwGvraFmVpIzQTt3s7OVyT2Mao2OkjMj_sCgNTny0_0u_r7o_SYNTHVxxCgAO8kVijrUNxTdkLYGOzFXRxWvmxhbiFJrXXQVjnoG1h-d5CCLxTwGTkZkUZoI5kQJZHau0SHPJAi5sJkkBHFnGBL206IoOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25637cbe58.mp4?token=ilqi-I8Ip32vXHO3REoS4P9CaMiej50PWVwetwwYFHFQKbgACTo12YFTdnmemFCd4c3aris-oPvX56tZj_I6tEvEGDixwvRA-AidbmH5uF5rNiRjkS46O3366DDKtISiMXITl-9qTPb3YWjfJftaex3iffQiZJpLqSQMB2GJeQcc9-8J7CcZqJqhx6kMwGvraFmVpIzQTt3s7OVyT2Mao2OkjMj_sCgNTny0_0u_r7o_SYNTHVxxCgAO8kVijrUNxTdkLYGOzFXRxWvmxhbiFJrXXQVjnoG1h-d5CCLxTwGTkZkUZoI5kQJZHau0SHPJAi5sJkkBHFnGBL206IoOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: به ملت بزرگ ایران اطمینان می‌دهم با عنایات الهی، حضور مردم در صحنه و انسجام مسئولان ذیل رهنمودهای رهبر انقلاب، ایران عزیز از این آزمون بزرگ سربلند بیرون خواهد آمد و افتخار عظیمی برای ایران در تاریخ جهان ثبت خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/459482" target="_blank">📅 18:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459480">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373a1bfd33.mp4?token=VEHl7eXzr-dNbHgQ4fEu4InYjGAk49BvlZN2naCr5HxmZUQKy_AEWzcdjtbmf7TwEp439JaGbavf0S_sKvOF1qqQ4UyK9i_LjNccH1o4udUMGVKsfIBCDq6K0MG8TG-43WIooG-uQXlP4X2W3AnVPvGuvbptNOyOsiIKq9gRR2S52P_2hHYKyh84xmwVlaEoWR7l9rE0zrxP5qtFV6FPrrALIGcyfDLDKek7uH-j6MPMRlVrSyKQaojIPyZ08AhitRDDo0q47ojyd9Ll7pHwHVRDo7wliM041_xEDo9gZIggcm1PG2kXM1Z3hp4Xc4Gl3IG0NwCBl2gZfgmE-ovM5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373a1bfd33.mp4?token=VEHl7eXzr-dNbHgQ4fEu4InYjGAk49BvlZN2naCr5HxmZUQKy_AEWzcdjtbmf7TwEp439JaGbavf0S_sKvOF1qqQ4UyK9i_LjNccH1o4udUMGVKsfIBCDq6K0MG8TG-43WIooG-uQXlP4X2W3AnVPvGuvbptNOyOsiIKq9gRR2S52P_2hHYKyh84xmwVlaEoWR7l9rE0zrxP5qtFV6FPrrALIGcyfDLDKek7uH-j6MPMRlVrSyKQaojIPyZ08AhitRDDo0q47ojyd9Ll7pHwHVRDo7wliM041_xEDo9gZIggcm1PG2kXM1Z3hp4Xc4Gl3IG0NwCBl2gZfgmE-ovM5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: به دشمن هرگز اجازه نخواهیم داد پا روی شرافت و عزت ما بگذارد
🔹
نقاط ضعف را باید در اندرون خود حل کنیم. با قوی‌بودن است که دشمن را وادار به عقب‌نشینی می‌کنیم.
🔹
همه ما مسئولان باید بسیار مراقب باشیم و خطای محاسباتی نکنیم.
🔹
سخنان حساسیت‌ برانگیزی که باعث شکاف در بدنه جامعه شود یا پدیده‌های اجتماعی که ممکن است مردم را مقابل هم قرار دهد، اساساً نباید بیان شود. باید روی نقاط قوت تأکید کرده و درباره آن‌ها صحبت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/459480" target="_blank">📅 18:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459479">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12429648eb.mp4?token=HwejwZZ1e6GQ4zNA_J5bb371bge_KbV4r8qKKnU-dBq8TeTF2i39P6tUMTr0Blj1s-T_cDM1P9z4onPt11KvUCaQ_weO79konDGsHl3Zv9LPp6ceB3q9M2UWgqwFqsC9RH3XLR4Vc4MjxgXbJY3fGeQnyBxSX30j6ykH_BwC8x2zQ00AmXBGqmxXjrT12vxYStkW7KAgcjleQmubttQyHxJpFbJ65fgku85w_AuAMf3sbN_uO0MwfWf6L8ACdNHuy0RT3-oOd0XT9LjZLJUM9GsmLWbnsAePBHw7clopd3vS4LjLRKMtpprE1nXo_gAnkQj7GC8mUZ56CBn6CA3Qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12429648eb.mp4?token=HwejwZZ1e6GQ4zNA_J5bb371bge_KbV4r8qKKnU-dBq8TeTF2i39P6tUMTr0Blj1s-T_cDM1P9z4onPt11KvUCaQ_weO79konDGsHl3Zv9LPp6ceB3q9M2UWgqwFqsC9RH3XLR4Vc4MjxgXbJY3fGeQnyBxSX30j6ykH_BwC8x2zQ00AmXBGqmxXjrT12vxYStkW7KAgcjleQmubttQyHxJpFbJ65fgku85w_AuAMf3sbN_uO0MwfWf6L8ACdNHuy0RT3-oOd0XT9LjZLJUM9GsmLWbnsAePBHw7clopd3vS4LjLRKMtpprE1nXo_gAnkQj7GC8mUZ56CBn6CA3Qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
درخواست یک شهروند از موتورسواران قانون‌گریز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/459479" target="_blank">📅 18:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459478">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399ee501a0.mp4?token=qCkFr2xcoBTfcEAmSzSckiZ7eIxefrL15H_gAwD5mqf2J3KaVrUkH9Dqo0zzLjjuBr30zFMayEbXjT2u2fad-SAXYKJa6Gs_2OX0bumlzehgncRGruQag6rxNEm-MktOFE4l5guPd4W22VhsMuHsdCciGlrRO56pBfrhTSiJQW9Ea2fahktGcCgOE7b_v0I7MLPFRW8rmTw8ccAvcMed1c2Tia-N6VBznyY9rsgqXN5AGVUL4KKROG0bwl_UzyORpA9fRiFgBMmzOGIuTihbGrX_6-W_I5QMLPAzNE5E6jrCLioeqt8P1mLT8iEJd8AJ-Kg7RCnjA4XkZ5dBXtD26A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399ee501a0.mp4?token=qCkFr2xcoBTfcEAmSzSckiZ7eIxefrL15H_gAwD5mqf2J3KaVrUkH9Dqo0zzLjjuBr30zFMayEbXjT2u2fad-SAXYKJa6Gs_2OX0bumlzehgncRGruQag6rxNEm-MktOFE4l5guPd4W22VhsMuHsdCciGlrRO56pBfrhTSiJQW9Ea2fahktGcCgOE7b_v0I7MLPFRW8rmTw8ccAvcMed1c2Tia-N6VBznyY9rsgqXN5AGVUL4KKROG0bwl_UzyORpA9fRiFgBMmzOGIuTihbGrX_6-W_I5QMLPAzNE5E6jrCLioeqt8P1mLT8iEJd8AJ-Kg7RCnjA4XkZ5dBXtD26A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوی دریانورد هرمزگانی حکایت جالبی دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/459478" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459477">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8952f37e1e.mp4?token=nVqw7LpgE6MjhHueJE-x1nIbk1d5gzgj_GupP3iMeK-HzyiUfyCLaOOCGhzUaijRQ2VUZhWTqB3iE8IZhujeD4ne7hnyJEn-3r9ymZXd7XREdzJreNucruR_OzeXCLPm4W5OntJYF2FpWX7d7SflBE7BX1qv6sFUQKcGdZpRNV_m4PiZz4w_DyzwAOkp88OHpEMHiLN57hcWCxe3PnCqKbCwZaPF_7KklVBzbuBqOIevHrOtjbdXLKo29m4j6X26BtH7-x3bwKLtIt46aRopdfpJdVxzof5lhOjk-bMasUUHcWICWbsc2Jj6gPVQ3DWdRKuvf1F4duMQjGq33JcfwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8952f37e1e.mp4?token=nVqw7LpgE6MjhHueJE-x1nIbk1d5gzgj_GupP3iMeK-HzyiUfyCLaOOCGhzUaijRQ2VUZhWTqB3iE8IZhujeD4ne7hnyJEn-3r9ymZXd7XREdzJreNucruR_OzeXCLPm4W5OntJYF2FpWX7d7SflBE7BX1qv6sFUQKcGdZpRNV_m4PiZz4w_DyzwAOkp88OHpEMHiLN57hcWCxe3PnCqKbCwZaPF_7KklVBzbuBqOIevHrOtjbdXLKo29m4j6X26BtH7-x3bwKLtIt46aRopdfpJdVxzof5lhOjk-bMasUUHcWICWbsc2Jj6gPVQ3DWdRKuvf1F4duMQjGq33JcfwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: از همهٔ سیاسیون در هر طیفی درخواست دارم اختلافات را کنار بگذارند
🔹
نباید فراموش کرد که همین الان نیز در جنگ هستیم. لازمه پیروزی در جنگ، مخصوصاً جنگ ترکیبی، انسجام و وحدت اجتماعی است.
🔹
از همه سیاسیون در هر طیفی و همه افراد خارج از مسئولیت رسمی درخواست دارم اختلافات چند ماه اخیر را کنار بگذاریم و همچون زمان جنگ رمضان، حول محور ولایت متحد شویم.
🔹
برخی دوگانه‌سازی‌های موهوم و برخی اظهارات جنجال‌برانگیز از اضلاع مختلف سیاسی کشور در این ایام اتفاق افتاد که دشمن را به اختلافات داخلی ما به طمع انداخته است.
🔹
پیام رهبر انقلاب، با ذکر جزئیات دقیق، تکلیف همه ما را روشن کرد.
🔹
هرکس از هر طرف بر دوگانه‌هایی که رهبری آن را موهوم دانستند اصرار کند، خلاف شرع بیّن و ضد منافع ملی عمل کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/459477" target="_blank">📅 18:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459476">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1395dd58a0.mp4?token=pKPDbVyA4BVlZ6LsGqhnTgpYtOPdQGuNvafMu10xdZISZEjpBBAXglCqZbu7DUYLqfxO-l_JVzBqk0-rFL2c1Hao3IkNeHzgWpoJBgcepLdpjgSunxAW_tOBqXKazlwQsaoIvbmGwWyZqYzH1LnX5lRhOo2IzojwPxlkq7PjSlCh79OQAEMVuDceXqVE7ZcngV1m0-5COfMdbM7XSHvKWQt4flOV9V9kCZdraBakZctrMsyhwmAJ0krtU6JMvriO1UY8L_gZO8LEkooXy6NyYKvoAE3VEsH-1I9H8d_JCu3QMjXprSGYFN_74xIREm34SUeB0uU66f348p-KA4xZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1395dd58a0.mp4?token=pKPDbVyA4BVlZ6LsGqhnTgpYtOPdQGuNvafMu10xdZISZEjpBBAXglCqZbu7DUYLqfxO-l_JVzBqk0-rFL2c1Hao3IkNeHzgWpoJBgcepLdpjgSunxAW_tOBqXKazlwQsaoIvbmGwWyZqYzH1LnX5lRhOo2IzojwPxlkq7PjSlCh79OQAEMVuDceXqVE7ZcngV1m0-5COfMdbM7XSHvKWQt4flOV9V9kCZdraBakZctrMsyhwmAJ0krtU6JMvriO1UY8L_gZO8LEkooXy6NyYKvoAE3VEsH-1I9H8d_JCu3QMjXprSGYFN_74xIREm34SUeB0uU66f348p-KA4xZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آ
غاز پرداخت خسارت مشترکان قطع برق از نیمهٔ مهر
🔹
مدیرکل مدیریت انرژی و امور مشتریان توانیر از ثبت حدود ۱۱ هزار درخواست خسارت مشترکان برق خبر داد و گفت: تاکنون حدود ۳۵۰ میلیارد تومان خسارت پرداخت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/459476" target="_blank">📅 18:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459475">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb23fdfbf5.mp4?token=OEbtyfw99fD6YzEt96IeAFFI9b0ozylWtjUVwJu-pidBso8AN1hVLdNwgMbChpYpHC-Libf8plYv3YXvJF26qsg6L4N0VEAP307C-3nz5STvOM-dBoaMEuRznPyXAaebn37xlqceyd4sEpc6N-YNI1fBxXZTsuCqf3fNly4L-gLQ9dk92KAdCxfW1SRkrkrhPLjwjwP8zwsGmxjRcmwvFt12VfQ_qxo6XJhEhVSymIudgFI4VfS5ED4hfsU9fhY6b-jmeZlDe-jHXrR6EFV4KMF5pDLYn7y_jH4Hs3PJBHwaO8y2YZwu3E89ysDykzFwoPb6-HpoBBkl5MTTHNra1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb23fdfbf5.mp4?token=OEbtyfw99fD6YzEt96IeAFFI9b0ozylWtjUVwJu-pidBso8AN1hVLdNwgMbChpYpHC-Libf8plYv3YXvJF26qsg6L4N0VEAP307C-3nz5STvOM-dBoaMEuRznPyXAaebn37xlqceyd4sEpc6N-YNI1fBxXZTsuCqf3fNly4L-gLQ9dk92KAdCxfW1SRkrkrhPLjwjwP8zwsGmxjRcmwvFt12VfQ_qxo6XJhEhVSymIudgFI4VfS5ED4hfsU9fhY6b-jmeZlDe-jHXrR6EFV4KMF5pDLYn7y_jH4Hs3PJBHwaO8y2YZwu3E89ysDykzFwoPb6-HpoBBkl5MTTHNra1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: انسجام اجتماعی، مهم‌ترین معروف اجتماعی است که باید یکدیگر را به آن توصیه کنیم
🔹
هر اقدامی که اصل انسجام را خدشه‌دار کند، بزرگ‌ترین منکر است.
🔹
انسجام ملی، عامل ارتقای روحیه نیروهای مسلح و شکست دشمن بود.
🔹
بعد از لطف خدا، همت و انسجام مردم پیروزی را نصیب کشور کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/459475" target="_blank">📅 18:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459474">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e496db28.mp4?token=LQe6r_6ZMVeNyaKSyd8c-78zU2FR0JJJp7SjjmkZDXSIwMjfJflMjwCCfeLEnic14-b90mVzrG5TChZY1_vcOpC3cTIicGmxjJMmJpCflYoeaixSEB8T5PVHerGjrLCLguy7YBUFkvMJzhuLT9Exkop4PI-rxxQ2eNeyHDoaz7eGsc3MRCm2I9nZsmXwss92I53T6TZuzffYfJxTkcnwunlFY6N-HPQ5br5xR0eLsbqVsgvsZVJ-eWpTKoLN0brrS0SVu-i9vBXNltHr-HxwNTeVFEKn1h3o9CEUwi-7oiJ37DrBkjxZ2wcEgGg1h5Q_8jqmJzE7Sps6mFNq75DKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e496db28.mp4?token=LQe6r_6ZMVeNyaKSyd8c-78zU2FR0JJJp7SjjmkZDXSIwMjfJflMjwCCfeLEnic14-b90mVzrG5TChZY1_vcOpC3cTIicGmxjJMmJpCflYoeaixSEB8T5PVHerGjrLCLguy7YBUFkvMJzhuLT9Exkop4PI-rxxQ2eNeyHDoaz7eGsc3MRCm2I9nZsmXwss92I53T6TZuzffYfJxTkcnwunlFY6N-HPQ5br5xR0eLsbqVsgvsZVJ-eWpTKoLN0brrS0SVu-i9vBXNltHr-HxwNTeVFEKn1h3o9CEUwi-7oiJ37DrBkjxZ2wcEgGg1h5Q_8jqmJzE7Sps6mFNq75DKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: سیاست جمهوری اسلامی ایران طبق فرمان رهبر انقلاب، تحقق شروط تفاهم‌نامه است
🔹
در مدت اجرای تفاهم‌نامه، محاصره دریایی رفع شد و در لبنان نیز، در حالی که در شرایط سختی بودیم، آتش‌بس پایدار شد، البته این به معنای رخ ندادن اتفاقات کوچک‌تر نیست.
🔹
در همین مدت، بیش از ۸۰ میلیون بشکه نفت صادر کردیم و در واردات کالاهای اساسی نیز اقدامات خوبی انجام دادیم.
🔹
اگر آمریکا به تعهداتش عمل نکند، با زبان قدرت او را مجبور به انجام تعهداتش می‌کنیم.
🔹
تا زمانی که تعهدات آمریکا در تفاهم‌نامه اجرایی نشود تنگه باز نخواهد شد.
🔹
شکست سوم آمریکا در میدان دیپلماسی، اجبار آمریکا به اجرای تعهداتش خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/459474" target="_blank">📅 18:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459473">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd85c2a1.mp4?token=N-X-KuQog_GLXDlwjwzNMSNFYpBfOgmlYui2n4LA1hLRcKeyP6mCP1E8jBi5MjP40CcNzyLVJ2kXPIc0ayI2ZT_m1kx6YelBcoyGPFvSH1ZAnks3B3V3iTUqqvzOkpj3Gut7I7GUUwbu2hlRDPQupg0uaYKKWiaqY-wOS_WhXxsN2aCOjXGsI_w8_cO5uNjqCIWvsRezbdV4blErVa9TszU_zGWoq9FzpP33LRv64mRxt4wZw2ow8V-2A6ViTiKqyai75hmHSVqcOJ1IESa-qU2atEDh7yTZdBU0nO7C7GFzbve2KSRw42DOy3g5evxkFbEVpsDTugVclmgYgxzabauwEVajtp5mKU22c5r0unIb3jct2zelobPqXUXmVLtzJxPZJOnFKn4RvVvnfX915w_rGqMX4l7kJer6YBv97jKZNE_aD993fyl9ohNpLU27BZX0f6lgeZo-ka7bUmS4Sgh9R1bqVYK8aXaZkmxUH8Yy5PYp3AV0Lh-6syuZ75zZqrQJakm3e5S2B8xzq5Q4DByB3yGl0YixHjtP3qTIbDkG4UoBBXUiQzGr9Bck-zGZdCjsNT-QsuVms2qU1ugD1cX6HovRm-L1RLwBPRDsJrTZGvnGQYTegTJY6VYVWf1bdq20rY7EQXRHARaxjrT5noHGxDBSZ4I5JMCWJUZH9p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd85c2a1.mp4?token=N-X-KuQog_GLXDlwjwzNMSNFYpBfOgmlYui2n4LA1hLRcKeyP6mCP1E8jBi5MjP40CcNzyLVJ2kXPIc0ayI2ZT_m1kx6YelBcoyGPFvSH1ZAnks3B3V3iTUqqvzOkpj3Gut7I7GUUwbu2hlRDPQupg0uaYKKWiaqY-wOS_WhXxsN2aCOjXGsI_w8_cO5uNjqCIWvsRezbdV4blErVa9TszU_zGWoq9FzpP33LRv64mRxt4wZw2ow8V-2A6ViTiKqyai75hmHSVqcOJ1IESa-qU2atEDh7yTZdBU0nO7C7GFzbve2KSRw42DOy3g5evxkFbEVpsDTugVclmgYgxzabauwEVajtp5mKU22c5r0unIb3jct2zelobPqXUXmVLtzJxPZJOnFKn4RvVvnfX915w_rGqMX4l7kJer6YBv97jKZNE_aD993fyl9ohNpLU27BZX0f6lgeZo-ka7bUmS4Sgh9R1bqVYK8aXaZkmxUH8Yy5PYp3AV0Lh-6syuZ75zZqrQJakm3e5S2B8xzq5Q4DByB3yGl0YixHjtP3qTIbDkG4UoBBXUiQzGr9Bck-zGZdCjsNT-QsuVms2qU1ugD1cX6HovRm-L1RLwBPRDsJrTZGvnGQYTegTJY6VYVWf1bdq20rY7EQXRHARaxjrT5noHGxDBSZ4I5JMCWJUZH9p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: با قدرت، منطق‌مان را بر دشمن تحمیل کنیم و هرگز تسلیم نظامی یا سیاسی نخواهیم شد
🔹
در آغاز گفت‌وگوها، آمریکا یک متن ۱۵ ماده‌ای در خصوص هسته‌ای، موشکی و محور مقاومت ارسال کرد؛ اما امروز وقتی متن ۱۴ ماده‌ای نهایی را نگاه می‌کنید، می‌بینید دشمن از همه آن‌ها عقب‌نشینی و رئیس‌جمهور آمریکا پای این سند را امضا کرد
🔹
چارچوب مذاکراتی را ما تنظیم کردیم و دشمن را وادار کردیم پیروزی‌های میدان را تبدیل به سند سیاسی کنیم.
🔹
اجرای سند به اندازه امضای آن نیز مهم است؛ اما بدانید وقتی سندی امضا نشود، راهی برای اجرای آن نیز نیست.
@Farsna</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/459473" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459472">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51ba267bb.mp4?token=f0p3bT9_lHyYDQaCHyhU0ZI0Umh2MEIkeO9FJNI_bUkKkmWAw6o3E_FnGx7ikS8vwV1dCGcq3XQeZ-JWAM3EIs3uVQ1Ob3BdA-sOuRjIDr4FV-o10kSayuQF3EljeBXWrSwiOK8t_U3QLUKI4bzDXKicGRkDAjO91blMRmNT36KBNkYoCVn7-A6mzRuPDXtDoYqtn3lf_fEJgvb2GbWP9aKIcdRDIpIQmiWkKsoekDqS7WwLCWo-fP2bQwyZK391sbp5ZtaZ-LvkyRvKnuhFbQvPcu3ERYlwtDGhNCg-GAL_guv6_OUEfX1DZvqmo856g-iuzpZHBsVs5UY06Z_aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51ba267bb.mp4?token=f0p3bT9_lHyYDQaCHyhU0ZI0Umh2MEIkeO9FJNI_bUkKkmWAw6o3E_FnGx7ikS8vwV1dCGcq3XQeZ-JWAM3EIs3uVQ1Ob3BdA-sOuRjIDr4FV-o10kSayuQF3EljeBXWrSwiOK8t_U3QLUKI4bzDXKicGRkDAjO91blMRmNT36KBNkYoCVn7-A6mzRuPDXtDoYqtn3lf_fEJgvb2GbWP9aKIcdRDIpIQmiWkKsoekDqS7WwLCWo-fP2bQwyZK391sbp5ZtaZ-LvkyRvKnuhFbQvPcu3ERYlwtDGhNCg-GAL_guv6_OUEfX1DZvqmo856g-iuzpZHBsVs5UY06Z_aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان برنامه و بودجه: در جلسهٔ نوروز ۱۴۰۴ رهبر شهید فرمودند اولین اقدام دشمن ترور همین جمع است و برای شهادت آماده باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/459472" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dafb57407.mp4?token=iGMGxqW3KYhPS0-nbUmVURfUChj_67ZI3vqqTeKfZ16ihi8y8ID_IcOYgF4ndbGybqnrskxQDh660ovsxdbWVzig0d-XdfkgpYeOwsT2Pe86y11fUTiVe33YdHngmBqju5bLxTMvQ2Gq1EHvM2TPDhESzaLnTafEKHPimmB5JtRKDj2guARvtmH46HzgrQ7BH7xQKjJXrpaIFhmouY13pElskfwPuFTMhvLRJCYsMEZ9Df-NSGWZsv-fu6qd4uU0cfhc76dsVBRlRFJfaf27v4ezDq9RppCoBcYZjI3cExhMe8V9XG2lzvHgLuO11bSqUD5S9qsHTQ0ePeF0pelAzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dafb57407.mp4?token=iGMGxqW3KYhPS0-nbUmVURfUChj_67ZI3vqqTeKfZ16ihi8y8ID_IcOYgF4ndbGybqnrskxQDh660ovsxdbWVzig0d-XdfkgpYeOwsT2Pe86y11fUTiVe33YdHngmBqju5bLxTMvQ2Gq1EHvM2TPDhESzaLnTafEKHPimmB5JtRKDj2guARvtmH46HzgrQ7BH7xQKjJXrpaIFhmouY13pElskfwPuFTMhvLRJCYsMEZ9Df-NSGWZsv-fu6qd4uU0cfhc76dsVBRlRFJfaf27v4ezDq9RppCoBcYZjI3cExhMe8V9XG2lzvHgLuO11bSqUD5S9qsHTQ0ePeF0pelAzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: مقصر بخشی از مصرف زیاد بنزین مردم نیستند بلکه مقصر صنعت است
🔹
مسئله بنزین را می‌شود با صرفه‌جویی حل کرد. اصلاحات ضروری باید حتماً با خرد جمعی و همراهی مردم، به‌گونه‌ای باشد که فشار بر روی مردم کمتر شود.
🔹
رضایت مردم اصل اول ماست. هرجا درباره مسائل تصمیم خوب گرفتیم، با مردم صحبت کردیم و آن تصمیم را خوب اجرا کرده‌ایم، مردم همراهی کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/459470" target="_blank">📅 17:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5lE9tgqSTwRCNGcUQqnkJOBS6B_r4YYSyH-kzau8tUnielB9iO0OccHvrczpQlYyUxq2nT5WmxVAH74s0UP5laZMi49iOZQESP-iDn1iNW2OmIDza7zMYG-_fgzktv2W043nfj4FOjeOUm-pWS50hSIoi_LjXw_cs0dhcEtRSEUVvz9ornTEaolw5L979jHoGArGQOI8pK7FxumBs5ksHj_QhQJMIbB2UK3uqR7YS3IXoD9QYjsAG44YIc8jGQjHUPd4Jtlt3lXYD2B7jSyQW7tyEcba70NJQlyXE6aOV8dGYJIDaINt58USdSRJ72-nViE7gbeL2XEWBbNYgltQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران شانگهای: «قانون جنگل» باید برچیده شود
🔹
سران سازمان همکاری‌های شانگهای در نشست شانگهای پلاس در بیشکک پایتخت قرقیزستان بر نقش سازمان ملل برای حل و فصل بحران‌های جهانی تأکید کردند.
🔹
رئیس‌جمهور روسیه با بیان اینکه ظرفیت‌های سازمان ملل همچنان «استفاده‌نشده» باقی مانده است، اظهار کرد برای افزایش کارآمدی این سازمان باید تلاش بیشتری صورت گیرد. به گفته وی، نهادهای سازمان ملل از جمله شورای امنیت باید نمایندگی گسترده‌تری از کشورهای جنوب و شرق جهان داشته باشند.
🔹
رئیس‌جمهور چین همچنین از اعضای سازمان همکاری شانگهای خواست برای بازگرداندن اعتبار سازمان ملل و بخشیدن حیات تازه به این سازمان با یکدیگر همکاری کنند.
🔹
الکساندر لوکاشنکو، رئیس‌جمهور بلاروس، نیز گفت سازمان همکاری شانگهای می‌تواند در احیای سازمان ملل نقش داشته باشد و این سازمان را بار دیگر به بستری برای حل دشوارترین مشکلات جهانی تبدیل کند، نه ابزاری برای فشار و اعمال اجبار علیه کشورهای مستقل.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/459469" target="_blank">📅 17:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361d2a31cc.mp4?token=VsMBDx1kQRudZzrcR6j3Lw6MOCfUX3rG5g4k0C_FdigZQIHFKgx1cu5Zz6eb6qkcgG9a92D2cH-NPIOs6cRsrBDXFNPsiFvKhcyssUAsEvpwjlPoBakFyrevbD2_fLAOvrIYzq7QiUZYJh-WNxIRrs9SNGSaNpJ6zd-8jMqXyzzm7VbagDGiBsYK8dzL_iDIhYeIu8mnQbiyLUs8mTOWgWG0F0p6bZw7qZ1zOexVf9WNWqlh9hSKExJ98unlj47t_mjN7p6Hw6wnjXswJWaaMiasxiWFE9UU_VUrQJb6TU5tV5ZldKVRGF2kaue60tpI-M8TmIIWGk4xGp0ZB4kyHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361d2a31cc.mp4?token=VsMBDx1kQRudZzrcR6j3Lw6MOCfUX3rG5g4k0C_FdigZQIHFKgx1cu5Zz6eb6qkcgG9a92D2cH-NPIOs6cRsrBDXFNPsiFvKhcyssUAsEvpwjlPoBakFyrevbD2_fLAOvrIYzq7QiUZYJh-WNxIRrs9SNGSaNpJ6zd-8jMqXyzzm7VbagDGiBsYK8dzL_iDIhYeIu8mnQbiyLUs8mTOWgWG0F0p6bZw7qZ1zOexVf9WNWqlh9hSKExJ98unlj47t_mjN7p6Hw6wnjXswJWaaMiasxiWFE9UU_VUrQJb6TU5tV5ZldKVRGF2kaue60tpI-M8TmIIWGk4xGp0ZB4kyHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/459468" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e37edd23f.mp4?token=Ug-1Z6d0Lm1cwuP3ftgPAliJDewwTVR6Na-OiD3KLMlZ23gsCX78Rfv2hS0wsm9NP2HTnzshJ_jkUDO_BAZLJVebzDXnOAoFxhPAzGLLwpSQb6JYtJZL-zC2PaxAf5gbXv52vysMTRJvcqvSYGkLW6T4hmWOYnfUo-vu8QW-U8KH5SncSp35ZjObdfI3QteL9t1KzmER6ezvieGcWtlC2MeFFTJyc4-NLcvfdvtMHygGnpq4VJkoqo_WmPegjdXUnaFwObYM3ZYt2cW0R3nXcuaoJxB8s1m-UAagmAdilG6dYGA9b9RTznbkOQ75sixPYQHHgbpDNTaURl3id3Pgzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e37edd23f.mp4?token=Ug-1Z6d0Lm1cwuP3ftgPAliJDewwTVR6Na-OiD3KLMlZ23gsCX78Rfv2hS0wsm9NP2HTnzshJ_jkUDO_BAZLJVebzDXnOAoFxhPAzGLLwpSQb6JYtJZL-zC2PaxAf5gbXv52vysMTRJvcqvSYGkLW6T4hmWOYnfUo-vu8QW-U8KH5SncSp35ZjObdfI3QteL9t1KzmER6ezvieGcWtlC2MeFFTJyc4-NLcvfdvtMHygGnpq4VJkoqo_WmPegjdXUnaFwObYM3ZYt2cW0R3nXcuaoJxB8s1m-UAagmAdilG6dYGA9b9RTznbkOQ75sixPYQHHgbpDNTaURl3id3Pgzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد
🔹
اگر دشمن اراده‌اش بر این باشد که ما از خلیج فارس نفت صادر نکنیم، هیچ‌کس نخواهد توانست نفت صادر کند.
🔹
دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است.
🔹
بخش زیادی از تحریم‌های اعلامی جدید، قبلاً نیز اعمال می‌شده است.
🔹
محاصره دریایی در قوانین بین‌المللی، یک اقدام نظامی محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/459467" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRHUFlXgpbN9sRI-BwuZmy683IOghiYotcRd2gCK-QWOXNyMB2ENEzt4HB_mVuJ70LGnntizVK70TpZWKXKi1wSVfIBpnvLzzICdXDytnSS7QXM1wiIrBWn3I-_-kF2BkttwXpS55oSZbtwa6AZEGJZ3jFtfjE1nB0yX91aE3l3QcK49ghzS5EtIcK81KsZX63CIpRNHtGE2NmnKrISewyk0FIi3fo3fzDQrhBbVmaAIT0KnW9TZF4_ErYPTRR5pR6eRNOwqiNNR3xxztHsZVEflOBEaRXJ1gj5NsMic__fYkqy0PfFr8UwzZQRFwO3v5yvUp9bR3lfhJtMwTWjFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
گسترش پوشش ارتباطی ایرانسل در روستاهای آذربایجان شرقی
🔸
ساکنان سه روستا در شهرستان‌های اهر و هریس آذربایجان شرقی، با بهره‌برداری از دو پروژه ارتباطی، به اینترنت پرسرعت ایرانسل، دسترسی پیدا کردند.
🔸
همزمان با برنامه‌های هفته دولت، پروژه‌های ارتباطی روستایی ایرانسل با حضور استاندار آذربایجان شرقی و معاونان وی، نماینده مردم تبریز، آذرشهر و اسکو در مجلس شورای اسلامی، مدیرکل ICT استان، مدیران استانی، جمعی از خبرنگاران و با حضور آنلاین معاون حقوقی و استان‌های وزارت ارتباطات، در محل اداره کل ارتباطات و فناوری‌اطلاعات آذربایجان شرقی به بهره‌برداری رسید.
🔸
پروژه ارتباطی ایرانسل در روستای یاورکندی با اعتبار ۱۸۱ میلیارد ریال به بهره‌برداری رسید و ۱۱۰ خانوار و ۳۴۱ نفر را به شبکه ارتباطی و اینترنت همراه ایرانسل متصل کرد.
🔸
همچنین سایت ارتباطی ایرانسل در روستای هیق با اعتبار ۱۷۰ میلیارد ریال راه‌اندازی شد و روستاهای هیق و هفدران با ۸۰ خانوار و ۲۶۵ نفر را تحت پوشش شبکه ایرانسل قرار داد.
👈
جزئیات بیشتر:
https://irancell.ir/b/331330/ahar-heris-rural-site-inauguration-1405
@irancellnews</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/459466" target="_blank">📅 17:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVIH4Cygxq-P4kDNPKAJRn9ocQ4H9qjL9Yna0XxYJxR3nUOz5Z6i0byB1jWckel2rNcqCf3FLVpcTogN1v1hPrfwWJoMSuRhRKU__cTy7Zf3uHqgdhQ-KE2UaQw8UVImAHiLOB6ZUkC1JeCWwJ7MYvmV2V_b9ZLQTd3OxkiRmQ8mokGNwyjKeMUDYSGDXKXPr89KRY5v1HETSDGA5dmq5_zfSyvk67Lgimi3jCn3MJc97NZpkaoaeeoZ30lfzXVyGOEbIqbD_lqMNYAl0otOztwmW2q-KRbzKMQw47JD5okjPHfwPwiTViqix8qBqZlFRSClCe784KSq0A1sTuRYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رونمایی از کارت اعتباری گردشگری ریالی و ارزی بانک رفاه کارگران با حضور وزرای رفاه و‌ میراث فرهنگی
🔹
در راستای رونق صنعت گردشگری و با هدف فراهم‌ کردن امکان دریافت و استفاده سریع از کارت‌های اعتباری گردشگری ریالی و ارزی، بدون نیاز به مراجعه حضوری، سامانه صدور آنی این کارت‌ها، توسط بانک رفاه کارگران رونمایی شد.
🔹
مراسم رونمایی از این سامانه به عنوان نخستین سامانه رسمی صدور کارت‌های مذکور در کشور، با حضور دکتر میدری وزیر تعاون، کار و رفاه اجتماعی، دکتر صالحی ‌امیری وزیر میراث فرهنگی، گردشگری و صنایع دستی، دکتر للـه‌گانی مدیرعامل بانک رفاه در محل این بانک برگزار شد.
🔹
این سامانه در راستای تسهیل پرداخت‌های بین‌المللی و پاسخ به نیاز کاربران برای خریدهای اینترنتی ارزی و ریالی، پرداخت هزینه سرویس‌های آنلاین و استفاده از خدمات جهانی، توسط شرکت دانش رفاه پردیس از شرکت‌های زیرمجموعه این بانک در بستر پلتفرم Payval راه‌اندازی شده است.
🔗
متن کامل خبر
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/459465" target="_blank">📅 17:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/459464" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d849a033.mp4?token=Qcz9TFfxx4MNUyhLE51RBdAxCNM_DCGc8mNgI206DJ_cSe2o2PDlWwyP8B5k7V9S4DfK72AleXqcjY8CiqGIW2Y5OihjT_fu5mAhCxJpahybCn-IPgZ4zXwyBMdwLQXwoyFrFYblW82m9yNaJkcJ5eeX1UTP57eCHgAV5WeSD2coL98FQvt2SvLJTw9qDtSm6NPbNlzWRbwIaXINfDuKmsWH8FQ1MJobZN9pP-d53lSY6tozrVD2DzUw1UoVQiB9qEf6M0j3hui44zXSrvObVotRmMkzfQIO1TLsYnHlk2symQ5XiG1Qghdfgji4mY57a_S7cQu16eCIAKmc92V0Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d849a033.mp4?token=Qcz9TFfxx4MNUyhLE51RBdAxCNM_DCGc8mNgI206DJ_cSe2o2PDlWwyP8B5k7V9S4DfK72AleXqcjY8CiqGIW2Y5OihjT_fu5mAhCxJpahybCn-IPgZ4zXwyBMdwLQXwoyFrFYblW82m9yNaJkcJ5eeX1UTP57eCHgAV5WeSD2coL98FQvt2SvLJTw9qDtSm6NPbNlzWRbwIaXINfDuKmsWH8FQ1MJobZN9pP-d53lSY6tozrVD2DzUw1UoVQiB9qEf6M0j3hui44zXSrvObVotRmMkzfQIO1TLsYnHlk2symQ5XiG1Qghdfgji4mY57a_S7cQu16eCIAKmc92V0Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاهدها و وثیقه‌گذارهای حرفه‌ای در قوه قضائیه شناسایی می شوند
@Farsna</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farsna/459463" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82abd9d8a2.mp4?token=rXfJccqkgr88QhNPVqnCxcyL1DStZIunNJ76TlmSFf2J90PuLkrpugK7Oaw0spURmG09dLGDksSpwTmCLS7piE0ParxStkv0ab19ou5LkSSLAFaLz20VdoJGGbHT86cWdTN0vUmBTGTc9dhyCRIgrOM8EZLr_3LbZfSr4tEXR8_nKkwAxGoGC_MONzrMhROmqL-GA4WJkX35f5EM8YPATOBGi9pgy4VGUi3iax1fxzeUZ8To5eRQnNgIJmQEQk9b_YDjBrWrjIY5MkJFr0t6hTvD7Lg4CmIP-Y-7QaXnRTmMQ4K7dwLjk0w87u7_UvG8uFzgCKlmp7h3mZZRmpcahA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82abd9d8a2.mp4?token=rXfJccqkgr88QhNPVqnCxcyL1DStZIunNJ76TlmSFf2J90PuLkrpugK7Oaw0spURmG09dLGDksSpwTmCLS7piE0ParxStkv0ab19ou5LkSSLAFaLz20VdoJGGbHT86cWdTN0vUmBTGTc9dhyCRIgrOM8EZLr_3LbZfSr4tEXR8_nKkwAxGoGC_MONzrMhROmqL-GA4WJkX35f5EM8YPATOBGi9pgy4VGUi3iax1fxzeUZ8To5eRQnNgIJmQEQk9b_YDjBrWrjIY5MkJFr0t6hTvD7Lg4CmIP-Y-7QaXnRTmMQ4K7dwLjk0w87u7_UvG8uFzgCKlmp7h3mZZRmpcahA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: امروز همه، چه مسئولان و چه مردم، باید دقت کنیم در زمین دشمن بازی نکنیم
🔹
مردم در همه صحنه‌ها نشان دادند پیشتاز و پیش‌قراول بودند و دشمن هیچ‌وقت نتوانسته است از مردم ما سوءاستفاده کند.
🔹
باید فرصت سوءاستفاده را از دشمن بگیریم. با برنامه‌ریزی‌های انجام شده و همراهی مردم از این جنگ سخت عبور می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/459462" target="_blank">📅 17:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=LfHvDN36KptRJsqrzgAQRXI3iBv5FiFusgFbyh0p-6rqFko6U2_gkpJgsIbDo21aCxKqWiLExaJPP6LwRLQWYSLqDJi4M1-TkWPHF7bNCDc5DynGcxCR4NVxRsdVEwyIKnJtiVObjL-M-Pvlk93aFsX-LLehgD1UNJb2WZGTCjr3DeI0OpSNMOb7YhVF3PxDIPySkcCUDrUPhue2WBzKP_L3EJPKMyIUCez9JkDwbYyJyuzNe2uGap1lMWxz6FESpVgUuY7PWyAkC7v0esMYiL0CVM0Yo-TEO67ZL5O6f_V02I-O7d3mX1esRZMj7fXXqbDACqKOVsTolf9U_VQkG6FNbtaIAxEzuKTVe1N5tk0m1-zbFRwzP88nlmeQxV2x8jBhzg6F32FjVeTv62mZw09urT3EwD5Zq5LxZWJiX7Tg4B92i8lnDZ9ixH5GoIAOm6EUs2BpFCnX5q1GJJ_JAG9ms65SyWeSxTc4cbQ8EOPTE47Q4_JLf4Pm0q8iFra2C2xuGFEHiDylmL3bsidoDSmgdIWVVqJRW1BfuF31dDKIhGcCaVMSX4e5YdbgRs8flO_fJ6NyBLlVTW4tEE7QDBUvlnYbczclRbK3C7SYrLYfJSoh9UAkW1AFcFQeHw2k9sSAccDmfh82FTsgtjsTK0bo1paQSh86Jox0A3955pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=LfHvDN36KptRJsqrzgAQRXI3iBv5FiFusgFbyh0p-6rqFko6U2_gkpJgsIbDo21aCxKqWiLExaJPP6LwRLQWYSLqDJi4M1-TkWPHF7bNCDc5DynGcxCR4NVxRsdVEwyIKnJtiVObjL-M-Pvlk93aFsX-LLehgD1UNJb2WZGTCjr3DeI0OpSNMOb7YhVF3PxDIPySkcCUDrUPhue2WBzKP_L3EJPKMyIUCez9JkDwbYyJyuzNe2uGap1lMWxz6FESpVgUuY7PWyAkC7v0esMYiL0CVM0Yo-TEO67ZL5O6f_V02I-O7d3mX1esRZMj7fXXqbDACqKOVsTolf9U_VQkG6FNbtaIAxEzuKTVe1N5tk0m1-zbFRwzP88nlmeQxV2x8jBhzg6F32FjVeTv62mZw09urT3EwD5Zq5LxZWJiX7Tg4B92i8lnDZ9ixH5GoIAOm6EUs2BpFCnX5q1GJJ_JAG9ms65SyWeSxTc4cbQ8EOPTE47Q4_JLf4Pm0q8iFra2C2xuGFEHiDylmL3bsidoDSmgdIWVVqJRW1BfuF31dDKIhGcCaVMSX4e5YdbgRs8flO_fJ6NyBLlVTW4tEE7QDBUvlnYbczclRbK3C7SYrLYfJSoh9UAkW1AFcFQeHw2k9sSAccDmfh82FTsgtjsTK0bo1paQSh86Jox0A3955pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند
🔹
نقشۀ دشمن برای همه مسئولان ما روشن است.
@Farsna</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/459461" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459460">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=WOcLz1FLcxlEQERsnnnRbaeBEIEObo7yCk2OZra426NqSiSqTstcWtn5SebJvs52EpMPEe5kcU4xHNqPUnbel8WyvjqfW2AbO0x4P3XmHffHxqpX9SBLeji3UEMhyzh_JwRva9Ep7CiRNuMQmUGvmMLIC4GPLG7v34EueydHFBf24F3b3P3gtm-TVO8WwX4HVCx8AskzSbD2mYJhLwBplTkK7h1CQ_Gu3grkMgj6NzrjU9pJag-OFFuO4_LDByRYDEKyTWrLavUpwNsBK40T4CK1zAoQkAjCCUXTgyK7m-ViE3eY6RWXwWYraFnGgT0JVeK-4qdroiFMzY9XOOtmZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=WOcLz1FLcxlEQERsnnnRbaeBEIEObo7yCk2OZra426NqSiSqTstcWtn5SebJvs52EpMPEe5kcU4xHNqPUnbel8WyvjqfW2AbO0x4P3XmHffHxqpX9SBLeji3UEMhyzh_JwRva9Ep7CiRNuMQmUGvmMLIC4GPLG7v34EueydHFBf24F3b3P3gtm-TVO8WwX4HVCx8AskzSbD2mYJhLwBplTkK7h1CQ_Gu3grkMgj6NzrjU9pJag-OFFuO4_LDByRYDEKyTWrLavUpwNsBK40T4CK1zAoQkAjCCUXTgyK7m-ViE3eY6RWXwWYraFnGgT0JVeK-4qdroiFMzY9XOOtmZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: قدرت نظامی ایران در تنگهٔ هرمز حفظ شده و ارتقا پیدا کرده است
🔹
اعمال مدیریت ایرانی بر تنگه، هیچ منافاتی با قوانین بین‌المللی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/459460" target="_blank">📅 17:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459459">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=aux-c5f57C3wYfQ30QyHIHym2KxpFQ9JMVLBKVV4lh56dkRSUEZE0upwIcyuWQ53b4n7ZbbPqRD8cB1VzAVU5bUE6TgU8FQsoHxCcZoCKR6P_J5i300oCrgQbiulUzRt_k6fZ2FO7mIzUZdG5NGgPGyqkz4HzpjGij6iksiFkZKCo3i7P8ae-eIzzqcnvkO1be2_W13A-KbnvmG9ljE6O0EQh7ZAsXPxprXmchIWLRPAbXI_8fV097hE269eHuhCxLkcFrLVLf5kcUcvqaj7MYVl1bY55CRU9B04dWzb0Tve8FSI43AYYaTHOZCMJZuwavhPOPlohAXbIKVMGKY6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=aux-c5f57C3wYfQ30QyHIHym2KxpFQ9JMVLBKVV4lh56dkRSUEZE0upwIcyuWQ53b4n7ZbbPqRD8cB1VzAVU5bUE6TgU8FQsoHxCcZoCKR6P_J5i300oCrgQbiulUzRt_k6fZ2FO7mIzUZdG5NGgPGyqkz4HzpjGij6iksiFkZKCo3i7P8ae-eIzzqcnvkO1be2_W13A-KbnvmG9ljE6O0EQh7ZAsXPxprXmchIWLRPAbXI_8fV097hE269eHuhCxLkcFrLVLf5kcUcvqaj7MYVl1bY55CRU9B04dWzb0Tve8FSI43AYYaTHOZCMJZuwavhPOPlohAXbIKVMGKY6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد
🔹
قبل از جنگ، روزانه حداقل ۱۲۰ کشتی از تنگه هرمز تردد می‌کرد و حتی اگر یک یا ۲ کشتی هم از تنگه عبور کند، به‌هیچ‌عنوان قابل مقایسه با قبل از جنگ نیست.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/459459" target="_blank">📅 17:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a06fa7c6.mp4?token=L-pi8zca8esFsR1BzC0jZDtOflEdGG2QKJfVdXcHJc4B0QkduWwKMLB144c0YWWMahdVv5jv7qEzPUnuErxDwJZy1fBlfDg2Yvzo4gR80WNqH4bfKhnJK8vPB_qzuTg0BDMz1IXuhcfkwC5uw523tLOch6kltqwFeJ3ZXROtu9Qetdb6Z6r8Taz_HjD72L-GXanlW4HNHG1RGVz17tRcl0S7jw_xiRRyKATgkIekT42bmd1ghuNTVyv-gQ5uMDrI37NAEywzrohQSOxtKe3N_A5wkqicQQPnYGGygVUrSCXWTvKEo5SCjJsbOKtGulCo8aA_Hq99Npt08uXOPr7pF2ZQ4MJajvvAr7vpudOsYo4ky04NpFwQRsmyMr5f6keys9tNW_HyrUS8YK92CavsNIk_XyisYLG1lJLOIW_lZStsYeA50pJH1ijMB9n1gtNIvSBatmPCbjWqc36NqfJzZ5ZgEfda6NbJEeeG5qmYOX_E3B6HVOLpyufzDONWYtK-8wjC7UAePZa3kdQt4U7O-vsiTIsnwVRikiAVPiVoM9zHFSscD-t5Acnwz4YDgN4WXk3sWMFyFWFYeW-Tj4ih1aOzKmQIzb8ZJfiCVlqgJO4hnS2CSvTy0kEPu0ewdaeaJ0ZRDeXFp5EoXuTouJQqu9O76EIBurkw1B5aX948dyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a06fa7c6.mp4?token=L-pi8zca8esFsR1BzC0jZDtOflEdGG2QKJfVdXcHJc4B0QkduWwKMLB144c0YWWMahdVv5jv7qEzPUnuErxDwJZy1fBlfDg2Yvzo4gR80WNqH4bfKhnJK8vPB_qzuTg0BDMz1IXuhcfkwC5uw523tLOch6kltqwFeJ3ZXROtu9Qetdb6Z6r8Taz_HjD72L-GXanlW4HNHG1RGVz17tRcl0S7jw_xiRRyKATgkIekT42bmd1ghuNTVyv-gQ5uMDrI37NAEywzrohQSOxtKe3N_A5wkqicQQPnYGGygVUrSCXWTvKEo5SCjJsbOKtGulCo8aA_Hq99Npt08uXOPr7pF2ZQ4MJajvvAr7vpudOsYo4ky04NpFwQRsmyMr5f6keys9tNW_HyrUS8YK92CavsNIk_XyisYLG1lJLOIW_lZStsYeA50pJH1ijMB9n1gtNIvSBatmPCbjWqc36NqfJzZ5ZgEfda6NbJEeeG5qmYOX_E3B6HVOLpyufzDONWYtK-8wjC7UAePZa3kdQt4U7O-vsiTIsnwVRikiAVPiVoM9zHFSscD-t5Acnwz4YDgN4WXk3sWMFyFWFYeW-Tj4ih1aOzKmQIzb8ZJfiCVlqgJO4hnS2CSvTy0kEPu0ewdaeaJ0ZRDeXFp5EoXuTouJQqu9O76EIBurkw1B5aX948dyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود
🔹
نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند.
🔹
امروز ایران بیش از دشمن توانسته توان…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/459457" target="_blank">📅 17:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG1sdYUFTks3eH-Tnb9DES5sH3N0bN8Bw2SVlW5MtL3ejUnuTARopgWEPmdO87nRJg0u_2BZ034WHkglVexaDJnjmm4WX53pUsme2PQBMhJpy41BSdk01ALRP6QZWmn2SlZLn0qPcfyKM6q3IaETEaOqzDICVjeJV0FYvnYFh4SLqvMTJUbqI7qD0NDjPoHNTHg6YfYijoFX5f7Q9mbg9y6KxIGGTbOF2IMjj8uL5CRVV0RYuLjJDIuUwpVpQ0rreHzkFHF08TekLbYFfD3LmQ4KJlo8_-u0WfsU8a6T_1YqrXU4323B5ixj5wl6VH7u_xoppO29AS4SzQfzeri-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دیدار پزشکیان و پوتین در بیشکک
🔹
در دیدار رئیس‌جمهور ایران و روسیه آخرین وضعیت روابط و مناسبات دوجانبۀ دو کشور بررسی شد و طرفین دربارۀ راه‌های تقویت و گسترش همکاری‌های مشترک در حوزه‌های مختلف گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/459456" target="_blank">📅 16:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c051d5e2.mp4?token=JrPYbmqYgQHTf8nVLHdr2Y080Z19Iz0iFUA_yUXkMAgvmf3N2vpfk8RQURrFRkEG3WDiB7kBzHI1gCcevIqbxOfJNk_GdUV57-1rVzS7EosVwi7Vj1m8DZg77i9nFO-edGAEoK3qLBhx0B-Qb8YyGM9c09MZ_iJiXdw5amBuGNWHQZ9WQkkh_wYLj8ZQ5NOMG0lvpk0EJQ5hKK5BYYI9T9he8QCWUxEsWbw8PX7q-A6EiEVoJBezpkhq0p_v_163hBbbcGhiDVSt8otfFdfp9ZxqE5m4GismBsKTk9PTUW7rTpyD5ir8QXdwJ6qlrUyrnRp2YDRyGzewxcxvAlqiEXJFvQx4T27RH6yPOd_3S4wzCm6qQ3QEvIjUd7Z0fo8QOaU-M4Bu-xxEqdbziqMK_Pdhod0xAvCkjuHznSUa8KYuGFbtCi8djJvC0GUEKSyyxHPYjdoaVUVgPF_nyo_QD6Ir4zvA4TtkGi7jFdCP-gFJumrIN9F2rqcDBefNQn6NBgCa6Smy31-JmUhDsD6JgqNs3N1JoFG_WWbXhADiFKFxMYYhvj0KiCnNPXGjFA97PPZmD8jMNy1-RV0rbuK_1xBBVO04kvDR5Kf4HAVXx6idUUP0qmnUWbPGNqw0S_Bd3PRe-PryMtrPovXsQHJnRYujYbBfxqucwcGM46uWdUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c051d5e2.mp4?token=JrPYbmqYgQHTf8nVLHdr2Y080Z19Iz0iFUA_yUXkMAgvmf3N2vpfk8RQURrFRkEG3WDiB7kBzHI1gCcevIqbxOfJNk_GdUV57-1rVzS7EosVwi7Vj1m8DZg77i9nFO-edGAEoK3qLBhx0B-Qb8YyGM9c09MZ_iJiXdw5amBuGNWHQZ9WQkkh_wYLj8ZQ5NOMG0lvpk0EJQ5hKK5BYYI9T9he8QCWUxEsWbw8PX7q-A6EiEVoJBezpkhq0p_v_163hBbbcGhiDVSt8otfFdfp9ZxqE5m4GismBsKTk9PTUW7rTpyD5ir8QXdwJ6qlrUyrnRp2YDRyGzewxcxvAlqiEXJFvQx4T27RH6yPOd_3S4wzCm6qQ3QEvIjUd7Z0fo8QOaU-M4Bu-xxEqdbziqMK_Pdhod0xAvCkjuHznSUa8KYuGFbtCi8djJvC0GUEKSyyxHPYjdoaVUVgPF_nyo_QD6Ir4zvA4TtkGi7jFdCP-gFJumrIN9F2rqcDBefNQn6NBgCa6Smy31-JmUhDsD6JgqNs3N1JoFG_WWbXhADiFKFxMYYhvj0KiCnNPXGjFA97PPZmD8jMNy1-RV0rbuK_1xBBVO04kvDR5Kf4HAVXx6idUUP0qmnUWbPGNqw0S_Bd3PRe-PryMtrPovXsQHJnRYujYbBfxqucwcGM46uWdUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود
🔹
نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند.
🔹
امروز ایران بیش از دشمن توانسته توان نظامی خود را بازسازی کند.
🔹
ضرباتی که بعد از آتش‌بس به پایگاه‌های آمریکا در کشورهای مختلف زده شد، معنای راهبردی داشت.
🔹
میدان را در دست داریم و این دشمن را به این نتیجه رساند که نمی‌تواند جلوی موشک‌های ما را بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/459454" target="_blank">📅 16:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942ac8dee3.mp4?token=rncw7qoZGswcg01cMvpWFACbZAseGMzbCvSG5bkTpF24Yo1BZ8lohcxa5a7_AW6ldjkcAK_Q-v1dEhk2orZYeHpHyTTVpjUcjfL4546slaEs-ZUALsvrisrXOuyHlneRbcmgHYKB83sBVABCa2LrHnW92ElXeVhy6mbVlzSnAQIoeiBJPBBGFVOl1qegYYgmtnJdXBiWw8nERk_YxRYjGzKGRrxH2YoEnIit6Z6a5vqf7iRYjHJvhXgZiwurmSPYw8Ov4m2z7WkfU_fBL30tiM_ifX6Nj5A6bnnWm2OUae1ypDkFWYtzWvlXqn1ACAB2CE5bpU1tqt-e2osuoaKanjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942ac8dee3.mp4?token=rncw7qoZGswcg01cMvpWFACbZAseGMzbCvSG5bkTpF24Yo1BZ8lohcxa5a7_AW6ldjkcAK_Q-v1dEhk2orZYeHpHyTTVpjUcjfL4546slaEs-ZUALsvrisrXOuyHlneRbcmgHYKB83sBVABCa2LrHnW92ElXeVhy6mbVlzSnAQIoeiBJPBBGFVOl1qegYYgmtnJdXBiWw8nERk_YxRYjGzKGRrxH2YoEnIit6Z6a5vqf7iRYjHJvhXgZiwurmSPYw8Ov4m2z7WkfU_fBL30tiM_ifX6Nj5A6bnnWm2OUae1ypDkFWYtzWvlXqn1ACAB2CE5bpU1tqt-e2osuoaKanjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: از فرماندهان شجاع و همه نیروهای مسلح تشکر می‌کنم و در برابرشان سر تعظیم فرود می‌آورم
🔹
گاهی انتقاد برخی فعالان رسانه‌‌ای در مورد فرماندهان نظامی را می‌شنوم و برای مظلومیت آن‌ها افسوس می‌خورم.
🔹
در زمان سکوت میدان، کارخانه‌ها، نیروها و بخش‌های مختلف نظامی درحال استراحت نیستند و همۀ خود را آماده می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/459453" target="_blank">📅 16:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef5fe4842.mp4?token=vTp2xTnSjPXX_qqloYUMjLreXUpl2_G8naW8nOO4fIIyqAvRA1hw5Qgv23yQ0CsF6S84vfDz03zDFxJQKFCmex7M97KN-jD8lMBaFdXWWUAg2lHdqWtbFX8w55LKNg8f3rfMv-Ihdb5SYT-SNR4y8eq8OlrIx3zCVWVDNfBZ3UNWjfYagQ28AXRewbcjlVHMM2TJKJXkpvEVN_b2D3MR4J1soQIws3pZbOnETsJyQXb-U51BOnhcHYCpj9sb4eg74QZt6OflF0THvFBM4Goc5I7sqZuLZV1q_dbcO7-XKS9m-LdWPoNXWha804I1yZFfClrMo27J0GrQbsgFOFen67Q7_yzx4-KXpqQtwR8USqpLrrYyC08yDfP5u0Q1FRHEszh4XU0cHJyLS6RnXfTW47dtk8A5L6zGhQN6PfnBbdIkKN_nYkSACoaVdoydc3IEP_wqhqGo6iXpmUR7PoEFweZW-MFVhFodzjpSbXVk2krGd1Ivtf69wheWcl5Axydy7PdTzFJhPbsw2ACmbASOTMpAjfN-oDMBVECchR5CnR8WLY8eurf3IsdTVv2zGcQQ5NAAw-S9Cv-dfAwKMAJRf_E8q9HUxv0ycr1pYrGfIFJjn0If0OLErfj978Y48EJ8BIS3wHgeCOHrMsiAk7_mYCtn7BL9RAndHL0V_a4HU3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef5fe4842.mp4?token=vTp2xTnSjPXX_qqloYUMjLreXUpl2_G8naW8nOO4fIIyqAvRA1hw5Qgv23yQ0CsF6S84vfDz03zDFxJQKFCmex7M97KN-jD8lMBaFdXWWUAg2lHdqWtbFX8w55LKNg8f3rfMv-Ihdb5SYT-SNR4y8eq8OlrIx3zCVWVDNfBZ3UNWjfYagQ28AXRewbcjlVHMM2TJKJXkpvEVN_b2D3MR4J1soQIws3pZbOnETsJyQXb-U51BOnhcHYCpj9sb4eg74QZt6OflF0THvFBM4Goc5I7sqZuLZV1q_dbcO7-XKS9m-LdWPoNXWha804I1yZFfClrMo27J0GrQbsgFOFen67Q7_yzx4-KXpqQtwR8USqpLrrYyC08yDfP5u0Q1FRHEszh4XU0cHJyLS6RnXfTW47dtk8A5L6zGhQN6PfnBbdIkKN_nYkSACoaVdoydc3IEP_wqhqGo6iXpmUR7PoEFweZW-MFVhFodzjpSbXVk2krGd1Ivtf69wheWcl5Axydy7PdTzFJhPbsw2ACmbASOTMpAjfN-oDMBVECchR5CnR8WLY8eurf3IsdTVv2zGcQQ5NAAw-S9Cv-dfAwKMAJRf_E8q9HUxv0ycr1pYrGfIFJjn0If0OLErfj978Y48EJ8BIS3wHgeCOHrMsiAk7_mYCtn7BL9RAndHL0V_a4HU3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش رگباری باران در روستای اردلان در منطقهٔ سراب آذربایجان‌شرقی
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/459451" target="_blank">📅 16:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459450">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd8d3229.mp4?token=bk3jgTPBWzi1V81zXX1i3lODiUCWOZ2-j1sdBl0FhLtN3hl0ksvir-v8QtqCM5zCYFahR7J4tN3T_05zwRpXGg7DlH0IHQbWc3cxLLJxEttfL6kX7qtNtkozO50BDHhvsAVPeEViDbueeA5gA8lcMpRADLDQWTX80A6OI7myrQlkovaZtt_yhy3nFAY7300cNlFj7NBtZYFX7YTj3p03-ikYkqG_GsXZZyIi0OKxNwD-ZB6AWFT7BG1Lji-qEnb2XzK03B55LI-uxZsZn21A-d08SBFnmJD_5L_sfs0up9xzI0ZtUm_S_BfKNPk4Ht1otH46bHKU3yw-zCYrX_LtKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd8d3229.mp4?token=bk3jgTPBWzi1V81zXX1i3lODiUCWOZ2-j1sdBl0FhLtN3hl0ksvir-v8QtqCM5zCYFahR7J4tN3T_05zwRpXGg7DlH0IHQbWc3cxLLJxEttfL6kX7qtNtkozO50BDHhvsAVPeEViDbueeA5gA8lcMpRADLDQWTX80A6OI7myrQlkovaZtt_yhy3nFAY7300cNlFj7NBtZYFX7YTj3p03-ikYkqG_GsXZZyIi0OKxNwD-ZB6AWFT7BG1Lji-qEnb2XzK03B55LI-uxZsZn21A-d08SBFnmJD_5L_sfs0up9xzI0ZtUm_S_BfKNPk4Ht1otH46bHKU3yw-zCYrX_LtKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در ۱۵ ماه گذشته، به اندازۀ یک دهه پیشرفت در حوزۀ نظامی داشتیم
🔹
در هر دورۀ جنگ، بهتر از دوره‌های قبل عمل کردیم و جنگیدیم. فرآیندهای بازسازی و تقویت توان نیروهای مسلح در بخش‌های آفندی و پدافندی، به بهترین شکل درحال انجام است‌.
🔹
این اقدامات به دلیل بومی‌بودن فناوری ماست و جوانان ما این کار را انجام می‌دهند و دست نیازی به‌سمت دشمن نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/459450" target="_blank">📅 16:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459449">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIT_xl4T6moNL9Q1QJdJCd0K3q9HmkR-POxGyyDuAVs4YmsXU3g0vesFtMAnE589ky4isTaoHiPtB8hUzrkXGpJ0C98O-7rhwYs9srqbkBh9vf5UER3YC287M3ovWLLE4pBpRTSSmWOfY0keEiQi9g-p1KZXD1pzDPEbs0EiLzPrNtOjckUp14-LkPiYrEXzBpqG0fzBxP0PCIAMws52Oc0P5tdQC5om1pbFBkXtBwqGwnSTWWCwT8uXPNEo3ZLQDzcXOXno8Q4MgZR3KY8GpSaC3M7PkRwMu2vKkazD98o-3tDCPYFnCYKxv1fwz0BJOYnoMYuVLrsTJvYPVFPUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدان در آستانۀ بازگشت به استقلال
⚽️
بسته‌ماندن پنجرۀ نقل‌و‌انتقالاتی استقلال و بازگشت خلیفه به آلومینیوم باعث شده تا باشگاه استقلال دوباره به سراغ دروازه‌بان اسپانیایی فصل گذشتۀ خود برود.
⚽️
طبق شنیده‌ها مذاکرات با آدان مثبت بوده و قرار است مطالبات این بازیکن…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/459449" target="_blank">📅 16:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmvn_0n_4gozkYpdKBfDQLwjPOSVfLgsC_S7ADYSOH_TlQ71CAO7RTu2m9ilruA-aM_LHGZszV3l4xSRBZ39UCccSr0bhZ4SwTGNmh8BNIWPcWVdK4dECA3AM_tVvO0GRO0DtbrTwrYKPxBzESTV2Ic9D_WBAjFTvQ3R5FS2J5kycthERKghVflqJ7ytfSv2NG95GbHg9O2j7r97nlMALRP4xakHuvoVfGjxD2NpQWCIEgGHQF96w_TIQsEkHBG7vElNobtisWUC8D8iVrQLblnBZKPKYFt4zENZED9QAT4gTQIvASms9Hu-dKyUyW8yLmiRchXAO26tc3KnWAQ3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: هر هفته ۱۰۰ مگاوات نیروگاه خورشیدی افتتاح می‌کنیم
🔹
امروز در صنعت برق در وضعیت بسیار خوبی قرار داریم و بیش‌از ۱۰۲ هزار مگاوات ظرفیت نیروگاهی در کشور وجود دارد.
🔹
تا پایان سال، ظرفیت نیروگاه‌های کشور افزایش خواهد یافت و امیدواریم این رقم به‌حدود ۱۲ هزار مگاوات ظرفیت جدید نزدیک شود.
🔹
هر هفته ۱۰۰ مگاوات نیروگاه خورشیدی افتتاح خواهیم کرد و توسعهٔ این نیروگاه‌ها با جدیت در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/459448" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRmM-zXoFsx8PXj5tWtnis5AbAtTPrYqJruO46rusdTg6rViGl8sCYjjCnfcie6MBrfXvTgrz4CPy4PMEQU7B7z6HRCFsZkfs3rW_VpAyemTe-0TpdvifH71JSaPu1VXMPchKT2u9Cf57TPQL_h5iuq_TDBz01IOcLH-B64D1HNLZ4osfQrV4kyzK1n91DEK0WJW7RUFnDgfvy6sSvabC3XYHtjjrAae5TK6FAyzPU-gLiK7HGKxQAACWlaB7CzZUoElHv4P2A8Hv-Rv1ldMR8L9eLgczDix9nQkEC23BkrJ9ZoLxvHftwJ7hs-Ymu45pTXLOO2CDp5r6IVJx05OCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد محبوبیت ترامپ؛ جنگ با ایران، عامل مهم نارضایتی‌ها
🔹
محبوبیت رئیس‌جمهور آمریکا با ادامه‌یافتن جنگ ایران در سراشیبی سقوط قرار گرفته و این بار به پایین‌ترین حد خود، یعنی ۳۲ درصد رسیده است. این در حالی است که دونالد ترامپ خود را جزو بهترین روسای جمهور تاریخ آمریکا معرفی می‌کند.
🔹
براساس نظرسنجی انجام‌شده توسط دانشگاه ماساچوست و مؤسسه یوگاو، قریب به ۶۴ درصد از شرکت‌کنندگان در نظرسنجی، عملکرد ترامپ را تأیید نکرده‌اند. ۵۴ درصد از این رقم را افرادی تشکیل می‌داده‌اند که «به‌شدت» از عملکرد دوسالهٔ رئیس‌جمهور کشورشان ناراضی بوده‌اند.
🔹
بر این اساس، ۶۸ درصد از پاسخ‌دهندگان گفتند که رئیس‌جمهور آمریکا جنگ با ایران را به‌خوبی مدیریت نمی‌کند. تنها ۲۵ درصد از افراد شرکت‌کننده معتقد بودند که این جنگ تا حدودی یا بسیار خوب مدیریت می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/459447" target="_blank">📅 16:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459446">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCroZ5OH65vzGu0hkKiM-30DkBQzaxs1QsjojbCsYvFqsbMB8l9eMUoaq0hxlgxrpKO1bACK16rYnHdUcFE_dNdE31BffSsXVqp-EYda0kgzRCLDX94hKX6kUWf4Uta9GPY5Fbg4dpSTAaWsMebjy5UxxkFz5mih-PRliV2RHU4pStIrVYixlwI0qJbQF0KoDbKvTsCznjMEZ_A6gylQkJIMEZxh3LZnai0p-ndizmowKA93OgwhW7wP_zHlPqE73CYSlvS4fpnqwqaoQUdHN16Qew0oDhFBkE-f0Q0BmuM6BssEhSzjAsWrK1Ou_9DvtNfN3pxs6pz_748vc1h4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبض یک میلیاردی گاز برای برخی از تهرانی‌ها
🔹
مدیرعامل شرکت ملی گاز ایران: در برخی نقاط تهران قبض یک میلیارد تومانی صادر شده است.
🔸
زراعتکار، معاون وزیر نفت، پیشتر اعلام کرده بود که از این پس یارانهٔ پنهان مربوط به استخرهای آب گرم ویلاها در زمستان پرداخت نخواهد شد و این مشترکان مشمول اصلاح تعرفه‌های گاز خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/459446" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236434ed71.mp4?token=aRUo4QYvizUzq3dtiBchzosf7dbzVCpAOGd0as5yjF6KZYXbKKMjsW5NYW7GzOusC_fILISgqldVMzktIEw9nh0vcYsBxkTKb6nBj6uxvx5AqWvEuq3g1LrgHGseyEL5l3t73zSYAYE3rVN31gSqME02dyRZaJUoegWP903o21N_cSi0cEvU1lXGnGys7wUBrt6A7OZNDFimwOWsHPLgfa2-gz45hcphiCP5ycF267OhZtPlIxRIOSrhT0jq8SuYkMB7iJa7ktXEynJASbBOrskc9Yaf6kfcxsj4EQScK-iqUcR4Jyp-fM0eG0sxI7SaINMlrRC4GyNuRz6bS4nm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236434ed71.mp4?token=aRUo4QYvizUzq3dtiBchzosf7dbzVCpAOGd0as5yjF6KZYXbKKMjsW5NYW7GzOusC_fILISgqldVMzktIEw9nh0vcYsBxkTKb6nBj6uxvx5AqWvEuq3g1LrgHGseyEL5l3t73zSYAYE3rVN31gSqME02dyRZaJUoegWP903o21N_cSi0cEvU1lXGnGys7wUBrt6A7OZNDFimwOWsHPLgfa2-gz45hcphiCP5ycF267OhZtPlIxRIOSrhT0jq8SuYkMB7iJa7ktXEynJASbBOrskc9Yaf6kfcxsj4EQScK-iqUcR4Jyp-fM0eG0sxI7SaINMlrRC4GyNuRz6bS4nm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان و پوتین در بیشکک
🔹
در دیدار رئیس‌جمهور ایران و روسیه آخرین وضعیت روابط و مناسبات دوجانبۀ دو کشور بررسی شد و طرفین دربارۀ راه‌های تقویت و گسترش همکاری‌های مشترک در حوزه‌های مختلف گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/459445" target="_blank">📅 15:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00444557cc.mp4?token=fK8m93_AnBFHCU55NCJHfbjHc5X0hWcil41Uxv4QZYtloSPVgJzEEsjd6l6ucUFm5Ko4xDN5aOAwq99aiOTQBKlK0E5qGgaEuIusr1koIW_nYv0yCdgf9dx-tRepbrEFmG4kjsOgvlX4lDQ4NiiYxYfnWJohLJHuaHdgYkPEcf2Z_KlOka83NH6TXs57SLMN3EvbklUvUWyVEGr4N02aeurJ_hwwIqAFhI8Bz8Z3v4riNAYE14CWyPEjSUy342LQ2pCoETM1LBg9c5iBKyQajij4gLF0CaCJFOY4_uGk-5IpBBKGEUgQJ5jJqzPO5ZpYtAzR45SvKL2F6dVF_acOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00444557cc.mp4?token=fK8m93_AnBFHCU55NCJHfbjHc5X0hWcil41Uxv4QZYtloSPVgJzEEsjd6l6ucUFm5Ko4xDN5aOAwq99aiOTQBKlK0E5qGgaEuIusr1koIW_nYv0yCdgf9dx-tRepbrEFmG4kjsOgvlX4lDQ4NiiYxYfnWJohLJHuaHdgYkPEcf2Z_KlOka83NH6TXs57SLMN3EvbklUvUWyVEGr4N02aeurJ_hwwIqAFhI8Bz8Z3v4riNAYE14CWyPEjSUy342LQ2pCoETM1LBg9c5iBKyQajij4gLF0CaCJFOY4_uGk-5IpBBKGEUgQJ5jJqzPO5ZpYtAzR45SvKL2F6dVF_acOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا برای راضی‌کردن کشورها به همراهی با جنگ اقتصادی علیه ایران هیچ منطقی ندارد
🔹
هیچ کشوری که اندک ارزشی برای حقوق بین‌الملل و حقوق بشر قائل باشد با آمریکا همراهی نخواهد کرد. ذات اقدامات آمریکا علیه ایران غیرقانونی و غیرانسانی است.…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/459444" target="_blank">📅 15:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459443">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b03b0b9c.mp4?token=XmbgdziCtsz7E-8QzXCpk0wGfcLBoddd0Od-Pe83qXne3hanWddD5tCTonLCeO9DMhtSofiZj8gW4Z0U2oNObpB0puXbWjXCXluKrmuNv4N7WWE_5Yrwt3_nIbDYzZKp02N9rIyFpsi-_U0DDY5EcsK1LtiFPMK6WeNSrRnuYGmYtU2n4qfOhipzkljyq1_aK4p-GxStYFuchANGWP6znTY5z7pr_uRW26TvS1PJN5kJVPosBbGjqLTUtF7kzU38d9062FRy7AGcI0t5MkKPNT9Ew2QDkhvKeG8k6C4OIb-Q38CpIgMywI2Bkrpfn5ZjlwVbtHkA1z0oRoBu8jsgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b03b0b9c.mp4?token=XmbgdziCtsz7E-8QzXCpk0wGfcLBoddd0Od-Pe83qXne3hanWddD5tCTonLCeO9DMhtSofiZj8gW4Z0U2oNObpB0puXbWjXCXluKrmuNv4N7WWE_5Yrwt3_nIbDYzZKp02N9rIyFpsi-_U0DDY5EcsK1LtiFPMK6WeNSrRnuYGmYtU2n4qfOhipzkljyq1_aK4p-GxStYFuchANGWP6znTY5z7pr_uRW26TvS1PJN5kJVPosBbGjqLTUtF7kzU38d9062FRy7AGcI0t5MkKPNT9Ew2QDkhvKeG8k6C4OIb-Q38CpIgMywI2Bkrpfn5ZjlwVbtHkA1z0oRoBu8jsgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا در جنگ با ایران دچار فرسایش شده
🔹
آن‌ها هر بار برای فرار از واقعیت یک دروغ جدید منتشر می‌کنند. افکار عمومی آمریکا از رفتار دولتمردان آمریکایی خسته شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/459443" target="_blank">📅 15:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ffa0cfa1.mp4?token=qS-dxijoNffE7FRBZHhxQvaO2vK6x1868zvT11k7uUxIf0MYUoUvUhefrS1ZTSM_J1Dt8U-b4WsuwnOfTpreb5toHQ6deAXMnn855wJA1966coO3Y0Ui3eTlwYzmtsE6oo9hUBi_KlCfAFy2ESoa2IGW6DLDDv5KIBD7UdKzoLF6jxZMCg76L0MHtepsZQqt4ZVJ9chCpdP0Vv752V1cVqaVggTF_xNmyxhl3WWkGnZwec-hEP8RLTBjPF7AF_pYiEqfBerWrwQOiah-fTnmD86ibh0n6xydJA0WU6kGXIUJXHiT3hXRpaviQJCHk33Q51o3S_A_JGEAc1kV3ojVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ffa0cfa1.mp4?token=qS-dxijoNffE7FRBZHhxQvaO2vK6x1868zvT11k7uUxIf0MYUoUvUhefrS1ZTSM_J1Dt8U-b4WsuwnOfTpreb5toHQ6deAXMnn855wJA1966coO3Y0Ui3eTlwYzmtsE6oo9hUBi_KlCfAFy2ESoa2IGW6DLDDv5KIBD7UdKzoLF6jxZMCg76L0MHtepsZQqt4ZVJ9chCpdP0Vv752V1cVqaVggTF_xNmyxhl3WWkGnZwec-hEP8RLTBjPF7AF_pYiEqfBerWrwQOiah-fTnmD86ibh0n6xydJA0WU6kGXIUJXHiT3hXRpaviQJCHk33Q51o3S_A_JGEAc1kV3ojVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرهٔ جدیدی با آژانس نداریم
🔹
صحبت‌هایی که دربارهٔ فعالیت‌های هسته‌ای در محل‌های جدید از جمله کوه کلنگ مطرح می‌شود، تحت‌تأثیر سیاست‌های برخی کشورهای عضو این آژانس است. @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/459442" target="_blank">📅 15:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459441">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e569594ee.mp4?token=RgTud1SGsgxBCDXwQL2S6RAzDMjGlIXHFHDvmHkBsRL9M_digqohXO7vQ0JiPnfEasV3FsOqlJDg2Fwo4QN94NfTKsumgdToXqlZsFN_NjhYhh0_5WfrYHVlRY_4sYr3UBEgsuyi0p6-xlpMMqiEvBiHuDUc1jwpi0bPFBdmpPNczQNsxKTSKvqKIxEYrySr7nnW222TPI8g8k1G8w0qm6hwMsoKtavbl0qIioQ7j1EejAn_GXQAaRqbJHYjf4Ql8Ktz64KDGLOzlhY8usyEJTICXw8DUI-ATSnF93YRFr42BAwWFhPmBUdQ14tRzqMK0Bsqy9fF4pOJfT3wFbSu7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e569594ee.mp4?token=RgTud1SGsgxBCDXwQL2S6RAzDMjGlIXHFHDvmHkBsRL9M_digqohXO7vQ0JiPnfEasV3FsOqlJDg2Fwo4QN94NfTKsumgdToXqlZsFN_NjhYhh0_5WfrYHVlRY_4sYr3UBEgsuyi0p6-xlpMMqiEvBiHuDUc1jwpi0bPFBdmpPNczQNsxKTSKvqKIxEYrySr7nnW222TPI8g8k1G8w0qm6hwMsoKtavbl0qIioQ7j1EejAn_GXQAaRqbJHYjf4Ql8Ktz64KDGLOzlhY8usyEJTICXw8DUI-ATSnF93YRFr42BAwWFhPmBUdQ14tRzqMK0Bsqy9fF4pOJfT3wFbSu7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخت ۹۰۰ ساله ارس ملی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/459441" target="_blank">📅 15:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d08d933a1.mp4?token=at2JQhHWn0kPKp2PA6irekm9ZS1wSw9HKQk6SgSJkqCC_MJNz0gwZuSR3nJPwpACKRVwSzB32f-i5z2g3YtY3PsSD5rvHCrQ_wJXJOl_ptdTLfS2U95C_r1D44o-RfQ9EDzc6758Qxe_nDc3CpsVHsxEquZw87T7uGgr0BZu_ouDDmbp7UqPVCdpt0qERPSE-dHf-PTX655xnzqj7-XZdWyIg1PTSPHWROkT1iPDdx3RFtG53eUyjZg50wYyQ3isu1mt66UXxFiEECMV0cO9minnwZXdNjrFo_Et6fEVEHVS08Gf3Sn7wDEIu5BMqyzHB-hcg7hXxmsgjCSdjwuyug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d08d933a1.mp4?token=at2JQhHWn0kPKp2PA6irekm9ZS1wSw9HKQk6SgSJkqCC_MJNz0gwZuSR3nJPwpACKRVwSzB32f-i5z2g3YtY3PsSD5rvHCrQ_wJXJOl_ptdTLfS2U95C_r1D44o-RfQ9EDzc6758Qxe_nDc3CpsVHsxEquZw87T7uGgr0BZu_ouDDmbp7UqPVCdpt0qERPSE-dHf-PTX655xnzqj7-XZdWyIg1PTSPHWROkT1iPDdx3RFtG53eUyjZg50wYyQ3isu1mt66UXxFiEECMV0cO9minnwZXdNjrFo_Et6fEVEHVS08Gf3Sn7wDEIu5BMqyzHB-hcg7hXxmsgjCSdjwuyug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سخنگوی وزارت خارجه به تحریم آزمون زبان توسط آمریکا: آن‌ها علم، دانش، فناوری و تمدن ایران را هدف گرفته‌اند
🔹
اگر ادعای آمریکا برای نگرانی دربارهٔ موضوع هسته‌ای ایران واقعی است، یک آزمون دانش‌آموزی یا دانشجویی چه ارتباطی با موضوع هسته‌ای دارد؟! @Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/459440" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459438">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc92b272a.mp4?token=EHnUdkwzpWDfPRFoowMOcO7e7z-xllN5Z7DKEjXfiHzarqYaSjQXaqSPGiOygYI6Z0qbZh9p4gMEmvJES8L2RJrbi-ss7yTPxkioPxvS4RpAYZUukib7RL-W_HeRgfVeeRBghuQ55lLxxjTSlCvAuqKxrIA5SdR40mj15fOojUaFSwNkHxl7I5xpfTsz_JGZCG30oxRKPP5HAvFtxTt5p21IwqsfNko6eh4dc-edD1HKaOEuhGBqyIN7uqsepIGKNg9osee6KE4-WUPpvBGmuUul1Gt2JoRZDZNle0bWl0pGzrRGkCtsFm7JGrz5fmWdhEqwhlGQGFS5jfSrdBbm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc92b272a.mp4?token=EHnUdkwzpWDfPRFoowMOcO7e7z-xllN5Z7DKEjXfiHzarqYaSjQXaqSPGiOygYI6Z0qbZh9p4gMEmvJES8L2RJrbi-ss7yTPxkioPxvS4RpAYZUukib7RL-W_HeRgfVeeRBghuQ55lLxxjTSlCvAuqKxrIA5SdR40mj15fOojUaFSwNkHxl7I5xpfTsz_JGZCG30oxRKPP5HAvFtxTt5p21IwqsfNko6eh4dc-edD1HKaOEuhGBqyIN7uqsepIGKNg9osee6KE4-WUPpvBGmuUul1Gt2JoRZDZNle0bWl0pGzrRGkCtsFm7JGrz5fmWdhEqwhlGQGFS5jfSrdBbm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز پزشکیان اولین مهمان اجلاس سران شانگهای بود  @Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/459438" target="_blank">📅 15:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfPMwDg8ez_qT2II3-Gqt32zuG02mIYx3LjSDf8ihKiWEDm2NCFMGSaGrC9EWngxTDFGKYdzo4mHZMEouAPE-ZibPQa81rSY9koqAIV_O94QZfbpk_IZG7MO2EgClevaUjDm4XoJpe2qy0KNR21Oim4rxS9sQW8_GQEQCaB5vULGtyyv2Sx_xIkCZXXUfHpfXwOy5MS7hTENPDF_arVWv4goWwtc_OOKH8v6qMZwyakuQC5CQm6WiiR9amSgLzb32BBFjJst37xOwWatX9SMPxZXdiIT4cBj_wfzDEnF3xQtVmm6pQtyrNrGbrN2dA4EKZGcz43CxpqUMSQq8qCaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفتیان رکورد کشوری خود را تکرار
کرد
🔹
در نخستین روز از مسابقات دوومیدانی مردان قهرمانی کشور در شیراز، حسن تفتیان در فینال مادهٔ ۱۰۰ متر با ثبت زمان ۱۰.۰۳ ثانیه رکورد ایران که دست خودش بود را تکرار کرد و قهرمان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/459437" target="_blank">📅 15:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1409465bb9.mp4?token=sYUZsJ-afdyBLsLvP9yADVn1z5tqz-eEWSZE0QPtDCYjK9_WBvaXpP_RR-UknCuN4CxYISLjMzLyEf350GbVzOEWcj-BwCJSLNxboDdKIK9oWGdjdF25i3TndhUdXbDO8HkEKuZwQxyf-mEAZ3w0KDGd6BSXBVMEmeivpeiQWrlWAMXp4C8omOiPBWXm6IRw2ed6LhWq7tfLe4WjLi54pskE-EauWFFDqpjcwlwjw_NFQte82imQGk-b82I0xekmPRXD6UstC3gyffm-ZYb3MZ-z-KKroY_WqqGINtW9RLjfrLl6KEMz-jeCf7D2FYSEoo5octQeyBs1EL_wp7tXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1409465bb9.mp4?token=sYUZsJ-afdyBLsLvP9yADVn1z5tqz-eEWSZE0QPtDCYjK9_WBvaXpP_RR-UknCuN4CxYISLjMzLyEf350GbVzOEWcj-BwCJSLNxboDdKIK9oWGdjdF25i3TndhUdXbDO8HkEKuZwQxyf-mEAZ3w0KDGd6BSXBVMEmeivpeiQWrlWAMXp4C8omOiPBWXm6IRw2ed6LhWq7tfLe4WjLi54pskE-EauWFFDqpjcwlwjw_NFQte82imQGk-b82I0xekmPRXD6UstC3gyffm-ZYb3MZ-z-KKroY_WqqGINtW9RLjfrLl6KEMz-jeCf7D2FYSEoo5octQeyBs1EL_wp7tXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: در تفاهم اسلام‌آباد آمریکا مرتکب نقض تعهدی شد که در بالاترین سطح هیئت حاکمه امضا کرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/459436" target="_blank">📅 15:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHsEIbSKCcogIGC7pkoz-a27nWriBFKkVb7vUFqeLhMy-1TjZ39Tu3eIhcQmDEzob4Vis2rRWeD2Fm_S1k4_jmXuctpvj4aTDhQ6_MENUY0XzKzJau3N9fNlP1VGCu8c4ixDt5UD1Fka05hloWKbhC9iP64wSSoh4BGZ8KzfY7oxc_aiYhsJUT9xZrN9ufasuJB7zaxYI-g0hEllW437JwaesiqfKZCbV6yTqQDfRA3g7txcwROo0MUBy_6pwnSR7y3SlkR46ipsYn8irCbEQVQvLu4OzoYmT8gUorSlt5CAYSyom0W839JP8vJF05aoO84b57kc_F2UM477r9pnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: نیازهای نیروی پدافندهوایی را به فناوری و فناوری را به قابلیت دفاعی تبدیل می‌کنیم
🔹
سردار ابن‌الرضا: روز پدافند هوایی، یادآور مجاهدت مردانی است که در خط مقدم دفاع از حریم آسمان ایران اسلامی ایستاده‌اند.
🔹
نیرویی که در جنگ‌های تحمیلی دوم و سوم از نخستین و اصلی‌ترین آماج حملات دشمن بود و رزمندگان آن با ایمان، شجاعت، صلابت و دانش، از امنیت آسمان کشور دفاع کردند.
🔹
آنچه امروز در این نیرو به کار گرفته می‌شود، حاصل پیوند نیاز میدان، دانش نخبگان و توان صنعت دفاعی است؛ زنجیره‌ای که باید با شناخت تهدیدهای جدید، همواره در حال ارتقا و نوآوری باشد.
🔹
صنعت دفاعی کشور خود را موظف می‌داند در کنار رزمندگان پدافند هوایی، نیازهای این نیروی راهبردی را به فناوری و فناوری را به قابلیت دفاعی تبدیل کند و با اتکا به جوانان و متخصصان ایرانی، برای تهدیدهای امروز و فردای کشور آماده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/459435" target="_blank">📅 15:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2815123322.mp4?token=OtDAOhTC04wBmKRGurWuTVnDcnKevM1C17MZxqLHfGo9K3fXRivrz3JudOtzwgtZ3L9mKCeNfdkNEoCO1XudnreFSTqSZoLEOSZMprZ7kpCuYIQZ65H-ixKpiq5E5X5e0v-ArkNhUkvvEpGKNTsqKJ8VI4KrOiQz_AKkn1DnAbxwClzyfqLETVZDQ7Xp2yhLJmwVuXqcutuJkw73grUgIKFmR7rN3xBWSBe7UH3H82j-_kpXYp9m7IxipHdr6E_R6JPO8J0X0t5qilgQE326qrPYxldf4_PX2ZRmcV87EcG26fFXP-jeh3VEO5SBTe01N6pQUmpm8d1ltjUkEi-0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2815123322.mp4?token=OtDAOhTC04wBmKRGurWuTVnDcnKevM1C17MZxqLHfGo9K3fXRivrz3JudOtzwgtZ3L9mKCeNfdkNEoCO1XudnreFSTqSZoLEOSZMprZ7kpCuYIQZ65H-ixKpiq5E5X5e0v-ArkNhUkvvEpGKNTsqKJ8VI4KrOiQz_AKkn1DnAbxwClzyfqLETVZDQ7Xp2yhLJmwVuXqcutuJkw73grUgIKFmR7rN3xBWSBe7UH3H82j-_kpXYp9m7IxipHdr6E_R6JPO8J0X0t5qilgQE326qrPYxldf4_PX2ZRmcV87EcG26fFXP-jeh3VEO5SBTe01N6pQUmpm8d1ltjUkEi-0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز برداشت انگور پیش‌رس از ۲۸ هزار هکتار باغات تاکستان قزوین
🔹
پیش‌بینی می‌شود امسال بیش‌از ۴۰۰ هزار تُن انگور از این باغات برداشت شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/459434" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fc73ac55.mp4?token=iD3ozy04D0sOkGT6t6qsHpceT9OA0rLTF9tV-zQ0K4z_XR8eM_G4r8JaZjw4EpPGULowaTfkEMYEsd2x8ttcowekZ_D7xuRb7iyg58URRO-baNcGj82TNzgXPDJWRgvLzMcBD8bkh2C3hYW8DZDRF4ItOfaa7QMIqKWCxusEHbWF05vfMJ9z1VMLy23l1ayX5Ksncf1F6Yx8JVKBL9tQgQ6N-IsUZrROgHaeJZ081IAzp8kQ82BMPMiDJSiTE3XAsNMR42UFgmK2kR_2hoxFNlMZPafy9wS1kMkD0YnxeVi3DfRccTOt5OL_W1320CnmTBIJAn8nsF39Nksyf4z5tTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fc73ac55.mp4?token=iD3ozy04D0sOkGT6t6qsHpceT9OA0rLTF9tV-zQ0K4z_XR8eM_G4r8JaZjw4EpPGULowaTfkEMYEsd2x8ttcowekZ_D7xuRb7iyg58URRO-baNcGj82TNzgXPDJWRgvLzMcBD8bkh2C3hYW8DZDRF4ItOfaa7QMIqKWCxusEHbWF05vfMJ9z1VMLy23l1ayX5Ksncf1F6Yx8JVKBL9tQgQ6N-IsUZrROgHaeJZ081IAzp8kQ82BMPMiDJSiTE3XAsNMR42UFgmK2kR_2hoxFNlMZPafy9wS1kMkD0YnxeVi3DfRccTOt5OL_W1320CnmTBIJAn8nsF39Nksyf4z5tTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح‌های جدید دولت در ۸ استان به‌بهره‌بردرای رسید
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/459433" target="_blank">📅 15:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d6ce48f1.mp4?token=SvtqsWwMdSDy72sDXbsBAEs9ZviFto2-3BbuqNyGBgn1U-ds-UeMS-qkCanH1CQEKx2PWpSovb39JnbLVH7Zfg76-aCGwkUx86xivn4C8waL1RN1KJ4V8zxE9ycSiruI-cAVdkmejolJDmSRwEwaRD30A-u95TtodBn24MbzpUkIbGCRURj5neTkHSDPLZW03yreUI767XOWSII7JdWDWjhgC1TkQFAN42L0qOF8rm7RaSk-WxDJmPu_Z04Sc5ojsLAhq_h_m_jz3d_c-jw3WhCPMOq8ZhSx_4rnaWQeSzApCdWnO0IN_-7SWe5Ku-csuCM7cp8Z-VrxmKMaTUfbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d6ce48f1.mp4?token=SvtqsWwMdSDy72sDXbsBAEs9ZviFto2-3BbuqNyGBgn1U-ds-UeMS-qkCanH1CQEKx2PWpSovb39JnbLVH7Zfg76-aCGwkUx86xivn4C8waL1RN1KJ4V8zxE9ycSiruI-cAVdkmejolJDmSRwEwaRD30A-u95TtodBn24MbzpUkIbGCRURj5neTkHSDPLZW03yreUI767XOWSII7JdWDWjhgC1TkQFAN42L0qOF8rm7RaSk-WxDJmPu_Z04Sc5ojsLAhq_h_m_jz3d_c-jw3WhCPMOq8ZhSx_4rnaWQeSzApCdWnO0IN_-7SWe5Ku-csuCM7cp8Z-VrxmKMaTUfbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت. @Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/459432" target="_blank">📅 15:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=alFCG_bmlBojoMLdeZ-Xqy9G020xBBZsadFTdzeXn5-VHhyy6TD24l0nfsIWJWabcs4eVZXdRndta8Jy2pRK34aYLB-sW16q4oDGmJXLJKRz290-g8NIK6PniyPuces_jj_3iQX_QIfvHfNGk-Ns7MTcrE2-2MxmBuzaM023MP19THmbk3XaViX8ySwDLL6COHTC9xcRsIEXTLe6JEwT4PYO1Kg7GUOYJwe9NzU3DkgEjDW1Phkh3IpTUV8ARYEhRQpE00Tq9b536xzezWKUWCZNQn7SzWg6miDh2xLBg58iBdkh2DiMPvxibEVfmjGTVaotJHwIGkVhA-FBtS-_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=alFCG_bmlBojoMLdeZ-Xqy9G020xBBZsadFTdzeXn5-VHhyy6TD24l0nfsIWJWabcs4eVZXdRndta8Jy2pRK34aYLB-sW16q4oDGmJXLJKRz290-g8NIK6PniyPuces_jj_3iQX_QIfvHfNGk-Ns7MTcrE2-2MxmBuzaM023MP19THmbk3XaViX8ySwDLL6COHTC9xcRsIEXTLe6JEwT4PYO1Kg7GUOYJwe9NzU3DkgEjDW1Phkh3IpTUV8ARYEhRQpE00Tq9b536xzezWKUWCZNQn7SzWg6miDh2xLBg58iBdkh2DiMPvxibEVfmjGTVaotJHwIGkVhA-FBtS-_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/459431" target="_blank">📅 15:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGz8IIKGGNZYz6EfTRjqakZ3uL4-3lNonyz5k0lQf3TYUWuHiW9lef4sOGnndUB-OlV25J69L-EU7HsSoKGE1Q9FeRkAfV-fJ5aqdZRC-4sjDbfVX2ePyZ5T9a6EcfSTHpl6rqSAOFiLONb3-q_U52RpagYEt_9IRaMsHfFE2zOht93THi2FGBs40VtIDXn13xVpjVvhyqlN3R5FndqryXb1dpIiGcGh_oQIDN2x8HyruRlKvP2ZyX5mkd5gJGqyawqzz5unzobI-UVHvnEujOAa7LfNT-qKgJ4E1rIr_osNa3ziKAWPOn_d5aAAtWhhi3-OfWpv-gGhBjTz7WuUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بسیج اساتید دانشگاه آزاد: وزیر علوم با مسئولان حاضر در نشست حاشیه‌ساز برخورد کند
🔹
شورای تبیین مواضع بسیج اساتید دانشگاه آزاد اسلامی در نامه‌ای به وزیر علوم، نسبت به قبح‌شکنی و ترویج هنجارشکنی در نشست مدیران ارشد این وزارتخانه با نمایندگان شوراهای صنفی دانشجویی…</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/459430" target="_blank">📅 14:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459429">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ac79f340.mp4?token=UdNcurmQRMBKqGwCreqZ9n5zaL_lCgZIFMEug3YAao1RjCCfKiN7Nxed6RTILErdI7zQqvhBeEIaOMrLPK1XQvjWnlMFXIsI58bejCchJK46NfRRevZKfEiww5cN1xZybivhcchIjKnP7W3V42AUzweOfz1NAfSugZmgEKxKxinqUeEGRSunYN7xLdApLJ_F_knHL0oWP1VOlCD4bNlOBsx1qYGiX1ct-H_rCLJkZMNeviZnZWrxYlaJDZ33lUfI0LFaH8lLLB0wf3Rvv2OlooAQCHfle1g9Kr9rARLdnztyXOETKYHyC57hxoY6v82BEomCHCxFhdB7Alvc7nk4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ac79f340.mp4?token=UdNcurmQRMBKqGwCreqZ9n5zaL_lCgZIFMEug3YAao1RjCCfKiN7Nxed6RTILErdI7zQqvhBeEIaOMrLPK1XQvjWnlMFXIsI58bejCchJK46NfRRevZKfEiww5cN1xZybivhcchIjKnP7W3V42AUzweOfz1NAfSugZmgEKxKxinqUeEGRSunYN7xLdApLJ_F_knHL0oWP1VOlCD4bNlOBsx1qYGiX1ct-H_rCLJkZMNeviZnZWrxYlaJDZ33lUfI0LFaH8lLLB0wf3Rvv2OlooAQCHfle1g9Kr9rARLdnztyXOETKYHyC57hxoY6v82BEomCHCxFhdB7Alvc7nk4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۵۰ شرکت تازه‌ترین دستاوردها‌ی حوزهٔ فناوری خود را به‌نمایش گذاشتند
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/459429" target="_blank">📅 14:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459428">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695fb09308.mp4?token=jj550WUUoEOQkHHyQSlLcE7M0MNI5HtWIQEIB-QlfMSWD6SAuHPV4NuWllmCSAaNSHzeUXKGFW8oV4ROzuybXe-uFj1cpGkxeVURNmJTqxtibrrxK0L58zp8sa2VLBuz1CiR9_nDk5JU39MO3qWhZXeT3Eg90rkmZcBIp5ykgOnTi1aLH5sxk1H8o9TCiJcDGNxNXs1ytpm84Bm1u1spGL9h57exqgkzRR946i-2nDUBoT5c4sFSxrdGKG_e3TWugN2Z8tXH9EBYlSjRMGXprNIxoVF1kCrHP2XxyfzRNjwxkINUujurTDIMB6J5ajRmNfd7bgI59cOqh34pMycDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695fb09308.mp4?token=jj550WUUoEOQkHHyQSlLcE7M0MNI5HtWIQEIB-QlfMSWD6SAuHPV4NuWllmCSAaNSHzeUXKGFW8oV4ROzuybXe-uFj1cpGkxeVURNmJTqxtibrrxK0L58zp8sa2VLBuz1CiR9_nDk5JU39MO3qWhZXeT3Eg90rkmZcBIp5ykgOnTi1aLH5sxk1H8o9TCiJcDGNxNXs1ytpm84Bm1u1spGL9h57exqgkzRR946i-2nDUBoT5c4sFSxrdGKG_e3TWugN2Z8tXH9EBYlSjRMGXprNIxoVF1kCrHP2XxyfzRNjwxkINUujurTDIMB6J5ajRmNfd7bgI59cOqh34pMycDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگرانی جنگ با ایران مقامات آمریکا را مجبور به ‌استعفا می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/459428" target="_blank">📅 14:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459427">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9648bcef.mp4?token=FE44WTus30JkeVgZnDeOeO17VylOxaZnNdJYQOX6lLGSHhwH3ofhDzd_BK5UF7IIXhlP8SIixflGzfzSZkzZaN3XPMmrLTKzIBH0YqKYVu_KPfWnV17T1TgVv0Dd_Ab0jHpDdu0pHDyDuTVECNFRz0LxlVPbuLNydmBN0Rv7XYeTxiJxbocgsrMNENYGllf7QQ54TIma9j0v4K4jwX_KuJ1QdZplqq1YOWO8se-LPFPoy5Bls7Ot91FhwYjrdJh8Vsd6lcROItRxD-KRaXS9u1o4nK45ChNo8XolUXSvTBBejaJ-SlztbZIx80EqUzA0pU3TWxnFy1QRrBEsV0RxVFMxIhYYtwLmqUGTVU1Tt6Bk8F3pJiK4v0CzprYeNDM_-tEmo9kjn5sCiYTfDJoAz11G31eGN_LPkJDQiCvIDUTtOVhfTyrbsGfizA9mvmMdwDfW_gNIpgNnhh_mU_JpHJqCLQ3iypyZqcGib-hl99gPgWuJKXFSruUQHK5uMma96T6W1LqdI0vMEyG7GQGL06ykD6pgriZRSz1pyXFCeSZE7_nfH1r7yot6BAjuwAuD_zKR5mZ-hVePkKbtzyx7pGGL2mdhbqmvVGVUIEjTij9svu_-yPVT62dySuAWVCxz9kr-XEl8-97C6EXn-JygBC0Bt4maBH5M88wqcztvhG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9648bcef.mp4?token=FE44WTus30JkeVgZnDeOeO17VylOxaZnNdJYQOX6lLGSHhwH3ofhDzd_BK5UF7IIXhlP8SIixflGzfzSZkzZaN3XPMmrLTKzIBH0YqKYVu_KPfWnV17T1TgVv0Dd_Ab0jHpDdu0pHDyDuTVECNFRz0LxlVPbuLNydmBN0Rv7XYeTxiJxbocgsrMNENYGllf7QQ54TIma9j0v4K4jwX_KuJ1QdZplqq1YOWO8se-LPFPoy5Bls7Ot91FhwYjrdJh8Vsd6lcROItRxD-KRaXS9u1o4nK45ChNo8XolUXSvTBBejaJ-SlztbZIx80EqUzA0pU3TWxnFy1QRrBEsV0RxVFMxIhYYtwLmqUGTVU1Tt6Bk8F3pJiK4v0CzprYeNDM_-tEmo9kjn5sCiYTfDJoAz11G31eGN_LPkJDQiCvIDUTtOVhfTyrbsGfizA9mvmMdwDfW_gNIpgNnhh_mU_JpHJqCLQ3iypyZqcGib-hl99gPgWuJKXFSruUQHK5uMma96T6W1LqdI0vMEyG7GQGL06ykD6pgriZRSz1pyXFCeSZE7_nfH1r7yot6BAjuwAuD_zKR5mZ-hVePkKbtzyx7pGGL2mdhbqmvVGVUIEjTij9svu_-yPVT62dySuAWVCxz9kr-XEl8-97C6EXn-JygBC0Bt4maBH5M88wqcztvhG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مردم ۱۸۴ شب است که میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/459427" target="_blank">📅 14:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f99bac187.mp4?token=RNXqIC6eAXxstFO4MPFyuI0F7M4rkpApmx-UysHn-7c5-L7Yegx8B1RN93g2unkgW7U2_HJSi_VmkQkjopSkX8RelELfS6ZrvhM3e6H_oVFlTPYF2dY_abbfHQpSs02sUyKD7HQuLrAEf7W9ydIOTB9s7vlrYebMAD4-XozfI1UvHFfmAr4v2A7VIKLqDMjqS2NEF1xuawl6bqI-xS7Nr3CucbzvJpvSMz-fPvpGvwgvKSVW8Wou5KNXFbQRKF7k3dtWq_q8Bg-8--lc_qSp-_yrWfGd1aDAs07iIa4Dd5RVWWO7aHMEeq9grM0t-lbPK8cGfYhMM4ZKd5fYPtDpaAZwTeydVE29OqjhTcptGzOO32SwqmEbc83kMCeaQYoXZgP2uo2lANaC0bgjttm-8kYnW8lFkmheZXWhMygr9vH3veRgd-o3iW-5PpUWwAVJEY0WTEklA7bjHYXhWnlgpMowlQBLi1hPL3KcR4l2tLLB57k4nztPYRU11-IvjNHD_uUIeweWDUkMZ-KLDbuTY9NH4bn200cmhwr6PKgMVOz-Y_Dtc3UXWVsNj3KNwqZAq-u02VrbgZIxA0Uj7v8-lUI4UZk-Ry2S-BYyAeLoBOi8Cab6YSNJyUN-ZWWlEXbQtv5C-uSw_Q1RMIUnDyxh_vV04WzM2E6gDCbHph1mNV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f99bac187.mp4?token=RNXqIC6eAXxstFO4MPFyuI0F7M4rkpApmx-UysHn-7c5-L7Yegx8B1RN93g2unkgW7U2_HJSi_VmkQkjopSkX8RelELfS6ZrvhM3e6H_oVFlTPYF2dY_abbfHQpSs02sUyKD7HQuLrAEf7W9ydIOTB9s7vlrYebMAD4-XozfI1UvHFfmAr4v2A7VIKLqDMjqS2NEF1xuawl6bqI-xS7Nr3CucbzvJpvSMz-fPvpGvwgvKSVW8Wou5KNXFbQRKF7k3dtWq_q8Bg-8--lc_qSp-_yrWfGd1aDAs07iIa4Dd5RVWWO7aHMEeq9grM0t-lbPK8cGfYhMM4ZKd5fYPtDpaAZwTeydVE29OqjhTcptGzOO32SwqmEbc83kMCeaQYoXZgP2uo2lANaC0bgjttm-8kYnW8lFkmheZXWhMygr9vH3veRgd-o3iW-5PpUWwAVJEY0WTEklA7bjHYXhWnlgpMowlQBLi1hPL3KcR4l2tLLB57k4nztPYRU11-IvjNHD_uUIeweWDUkMZ-KLDbuTY9NH4bn200cmhwr6PKgMVOz-Y_Dtc3UXWVsNj3KNwqZAq-u02VrbgZIxA0Uj7v8-lUI4UZk-Ry2S-BYyAeLoBOi8Cab6YSNJyUN-ZWWlEXbQtv5C-uSw_Q1RMIUnDyxh_vV04WzM2E6gDCbHph1mNV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران آغازگر جنگ نبود بلکه از خود دفاع کرد
🔹
در عین حال، ایران همچنان دیپلماسی و مذاکره را مسیر اصلی حل اختلافات می‌داند.
🔹
دیپلماسی بدون حسن نیت، بدون احترام به تعهدات و بدون پرهیز از توسل به زور، نمی‌تواند صلح پایدار ایجاد کند.
🔹
اگر تهدید به…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/459426" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9aBGHhp1S6RH9U9gR4ahYpJFcS9jfZDoc-3lipSLj_6wQNtlH_1GYIr3_p8bWHnbyCSYWCnk78EImHme5GOTjK8jxN6NuVRDHoYWsVhqUu-IEd5bqN8ejg2jGtAjIrom4aKtF8O5ENTzbqADFpe5O9rYbsfjjqYwDndoBmunrAR4oED8Q5zFDNjUueTzacoxXMD-2-c0VKWVOoa_AFzQDoZmRIG92WkbLcipPl5PuA-0MyIoN9q2bhxLTAYjSTyfA6TjYmHSj9xoM3L9z53eaQ3Dj3hfgvrHY1Zv_uHORT93x1q4WCjgPZ1xw6-ZJZojpoFv6T-LqGIbYL21E-Lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌از ۶ سال کیوی ایران به بازار هند برمی‌گردد
🔹
با اعلام سارمان حفظ نباتات کشور، پروتکل‌های فنی صادرات کیوی به هند رعایت شده و صادرات به این کشور آغاز می‌شود.
🔸
۶ سال پیش هند به‌دلیل آنچه که رعایت پروتکل‌های بهداشتی گفته بود، واردات کیوی از ایران را ممنوع کرد؛ طبق اسناد، گلایهٔ هندی‌ها از تاخیر در پاسخگویی به نامهٔ گلایه‌آمیز آنها دلیل اصلی این موضوع بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/459425" target="_blank">📅 14:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459422">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8c04b989.mp4?token=NYl0FKR4266KW20t-M1Qt0JHgzfWsiWAmpmEZFZMXGKTnCKjTgGv3Pi3NtF8t-QJSVAAOwVPeZOFddRKyBpXTpo2uJJ3P7V9Zb-TCoV7topifgTHyOmnlnF5v5h5hOhhC6sNWCxz8s195y-oJ2wMmL8XqTu9SmeWHel-JiBf_hbBbLeJwtq6kBiWs1wftFmUyXyq01lZlGM9FIXPPsqVzczuf2ypFSMlEncCKXQ98SXpPPfcZbhxmY3nRTBMa3pfrsEwLS7YbRDKdrwruqmysCSHhOoGhI-RI-TQT1E8dqKkNZNx9mPuZk87b4arVM0tJWOrdVvGs17DtFOsOLtsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8c04b989.mp4?token=NYl0FKR4266KW20t-M1Qt0JHgzfWsiWAmpmEZFZMXGKTnCKjTgGv3Pi3NtF8t-QJSVAAOwVPeZOFddRKyBpXTpo2uJJ3P7V9Zb-TCoV7topifgTHyOmnlnF5v5h5hOhhC6sNWCxz8s195y-oJ2wMmL8XqTu9SmeWHel-JiBf_hbBbLeJwtq6kBiWs1wftFmUyXyq01lZlGM9FIXPPsqVzczuf2ypFSMlEncCKXQ98SXpPPfcZbhxmY3nRTBMa3pfrsEwLS7YbRDKdrwruqmysCSHhOoGhI-RI-TQT1E8dqKkNZNx9mPuZk87b4arVM0tJWOrdVvGs17DtFOsOLtsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار بزرگ در ادلب سوریه
🔹
منابع سوری از انفجار در یک انبار مهمات در شهر «بنش» واقع در شمال استان ادلب خبر دادند که تاکنون دلیل آن مشخص نشده.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/459422" target="_blank">📅 14:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459421">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ اردوی تیم امید به حدنصاب گرگم‌به‌هوا هم نرسید
🔹
اردوی تیم ملی امید به‌دلیل به حدنصاب نرسیدن بازیکنان شروع نشده، تمام شد.
🔹
حسین عبدی برای شرکت در بازی‌های آسیایی ناگویا ۲۳ بازیکن را به اردو دعوت کرده بود اما تنها ۵ بازیکن در اردوی تیم حاضر شدند.
🔸
عبدی عصر…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/459421" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42630e22b8.mp4?token=PbxAG_GqAa0L2KxpuWwEXYWFTloM4QUC1FfvvIAhxzB47r3euC86Z1mmjfOBYpHMiTQmnRgOdA9xUNij6IjcjqCiH24OZ7J0Zh6rguwavVL_ESOQn_enshnOYaH40PVSvpUaC41IxfyxxekRiqifoEju0YEZQrj_cYIfUzRffWuH7FRNz8wTZf4js9UxSJKa4k6FelrtUzdtAA5iMBgsgvVCq2MX8GoTZCq267LE7E-sbX6XOsKy61iaLEGRhSw10Wkb2s_DHwjOFJYgETnoJN3MOXo0psw4W9xIZrtbjruDKt4Y-9X-1d_iksuW7iL1DqgUEflz0SBBBG9tPea7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42630e22b8.mp4?token=PbxAG_GqAa0L2KxpuWwEXYWFTloM4QUC1FfvvIAhxzB47r3euC86Z1mmjfOBYpHMiTQmnRgOdA9xUNij6IjcjqCiH24OZ7J0Zh6rguwavVL_ESOQn_enshnOYaH40PVSvpUaC41IxfyxxekRiqifoEju0YEZQrj_cYIfUzRffWuH7FRNz8wTZf4js9UxSJKa4k6FelrtUzdtAA5iMBgsgvVCq2MX8GoTZCq267LE7E-sbX6XOsKy61iaLEGRhSw10Wkb2s_DHwjOFJYgETnoJN3MOXo0psw4W9xIZrtbjruDKt4Y-9X-1d_iksuW7iL1DqgUEflz0SBBBG9tPea7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: عملکرد سازمان ملل در مواجه با تجاوز به ایران بسیار ناامیدکننده است
🔹
حملۀ نظامی آمریکا و رژیم‌صهیونیستی به ایران نقض صریح منشور ملل متحد و اصول حقوق بین‌الملل است.
🔹
ترور رهبر ایران، حمله به مراکز درمان و آموزشی، حمله به مدرسه میناب و لامرد نقض…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/459420" target="_blank">📅 13:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3OP0LNkXS_Ny_C-Nj1v-tqcatn2acAopyUz-K-p42BcndaKihXFLCZ98xOdwcthyzXMduBIXwZc9U4HqiYF0XFy5UVt6cxrJnJfhoZuUGfTq3jN7xwXO75J7lo7JFyZZxSF_rFtbJ2DWUPN28fNZ3mt8NXPBv74ZCx5_5WKjG8dH2U5-eguysqoRI6kgxykNDZVs5AFPsME7ZIelV2LahqIN0zmjS3BJMAEn3kUO5-xlh4uu30x60ZtM7lfxdp_nasKE0BoF0gaOGgt1ljkfNv49cIE7BuTIXzJhWxA_ztvuklW_tDHrJGAbGDWv4jGKgCh5dtNwq7G0idAAMoZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام جاده‌های شمال یک‌طرفه می‌شوند؟
🔹
پلیس‌راه مازندران: ترافیک ورودی در جاد‌ه‌های کندوان، هراز و سوادکوه سنگین گزارش شده است.
🔹
از ساعت ۱۲ مرزن‌آباد در جادهٔ کندوان مسدود شده و از ساعت ۱۴:۳۰ مسیر جنوب به شمال پل‌زنگوله یک‌طرفه خواهد شد؛ جادهٔ هراز نیز به‌صورت مقطعی یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/459419" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkVKNeMiltkwCVjOVI7G34tKD_3WKXhHZyggAYD3Id4r3JN0OLu3EHaoKZnt6eQiT8XHIdulfotpAI9VK6cUweXYVCyjHWGn3jRV_zLdqaBU1aIfxIYBunbKGzPvvOALF944K-PNvigZI-pUyzfsZxzvQPAgj8Ml6ifOh1NhUqxfvGNvawLfE61AKHszW2yIDYwxGcdg3gDW1E1d8E6VvQUdjk6UIEVv-5zWBCv3WH6TWAcfWP1BL_7vQ3Ltpwe_8xyKfug_8K_AzT0mtgRLhapKfsNHMZ1LxCv0lkxPg1AJ5IZcCTL_5TXYF92jHDGSUJIphFRPql9MvUJ4TXFqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نظام پزشکی: مطالبات انباشتهٔ جامعهٔ پزشکی از بیمه‌ها به مرز دشواری رسیده
🔹
از سران قوا می‌خواهم در جلسه‌شان مشکل مطالبات انباشتهٔ جامعهٔ پزشکی از سازمان‌های بیمه را یک‌بار برای همیشه حل کنند.
🔹
حجم این معوقات به نقطه‌ای رسیده که ادامهٔ فعالیت برای بخش‌هایی از جامعهٔ پزشکی را دشوار کرده؛ در حالی که با روش‌های علمی و جدید اقتصاد سلامت می‌توان این مسئله را سامان داد.
🔹
چطور می‌توان انتظار داشت که آزمایشگاه و سایر مراکز سلامت با مطالبات ۸ ماهه، ۱۰ ماهه و حتی یک‌ساله، همچنان کیفیت خدمات را در سطح جهانی حفظ کنند؟!‍ این مسئله قابل حل و نیازمند اراده و تصمیم جدی در سطح حاکمیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/459418" target="_blank">📅 13:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر اقتصاد: در جریان جنگ رمضان، شمار حملات سایبری به بانک‌ها در برخی مقاطع به ۱۰ هزار مورد در روز می‌رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/459417" target="_blank">📅 13:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7049a10267.mp4?token=qR44IE4VGv37l9HbjwrHzncou55__qsj57KmwgiXOKX7xxCx88bkpJJMTm-AEaOjsPdM1moWaXcu-Jtr9uIkXuDtdrHKFRFL0f4OmY7VeU7jJ9_Ioz73EDrqIn8wZPsEo7PZ9ZcVWCMe75RQl3zLY2E_QmzMUnsZgNQ-G-RYdivvlpzFxbsqUo2N3oA_lJhYvhgzyG4fTbP9_Gq7D5ZARS2zpz51S9JbHSgphWIVXFI7RmIaoCPoJkBjT-2FF3RKzKaVtAScGu6K5UxtK9FmLAMKMQ4zJGvIuC_9Wd_eBdguW3BSZ-hUECvWNbPTOgm2n9p_9T3Mlb1iH9FF--Jc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7049a10267.mp4?token=qR44IE4VGv37l9HbjwrHzncou55__qsj57KmwgiXOKX7xxCx88bkpJJMTm-AEaOjsPdM1moWaXcu-Jtr9uIkXuDtdrHKFRFL0f4OmY7VeU7jJ9_Ioz73EDrqIn8wZPsEo7PZ9ZcVWCMe75RQl3zLY2E_QmzMUnsZgNQ-G-RYdivvlpzFxbsqUo2N3oA_lJhYvhgzyG4fTbP9_Gq7D5ZARS2zpz51S9JbHSgphWIVXFI7RmIaoCPoJkBjT-2FF3RKzKaVtAScGu6K5UxtK9FmLAMKMQ4zJGvIuC_9Wd_eBdguW3BSZ-hUECvWNbPTOgm2n9p_9T3Mlb1iH9FF--Jc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
گفت‌وگوی کوتاه رؤسای‌جمهور ایران و چین در حاشیۀ اجلاس شانگهای  @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/459416" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس بانک مرکزی: معماری آیندهٔ شبکه بانکی بر فرض وقوع حملهٔ سایبری طراحی می‌شود
🔹
حملات اخیر نشان داد حتی زیرساخت‌های پشتیبان بانک‌ها نیز ممکن است هدف حمله قرار بگیرند.
🔹
بانک مرکزی بر استقلال و آزمون مستمر زیرساخت‌های جایگزین و بازطراحی نظام پرداخت تأکید دارد.
🔹
هدف این است که اختلال در یک مرکز داده، بانک یا تأمین‌کننده، باعث توقف گسترده خدمات بانکی نشود.
🔹
خدمات حیاتی بانکی باید حتی در شرایط حمله سایبری ادامه پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/459415" target="_blank">📅 13:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1c33ca1e.mp4?token=uwCDD_TZBGtY5PU2RIqowHexLG_O4tYu6L9N8LLy_XTjxL3Hp0hOoh7O9LGXJFzIzycIeaLniiDBGTZd4-c5_o6bNoYi_omTyX8jRvWvX6gkZ8_AAGxNQG9k4UaYl0LahWwEAGW9m7Tfo-YcX0xNm_TxSbkxX3x4GJCqiazoih1KHYW0diNF-LMFbeXn37rQ16SZ69e3vJayLIjwApxNae87GRMka5PUaRhbl9X1F_zuozVeXddmoF21794UgNbuuJPfvxyOMAiu7SoTHL-U76MdSZ681NJQ1gWuZ9ET5Nw61c-20L5Ealpwicgh81Db0G6WuCE7vZiGSlrWGmX4nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1c33ca1e.mp4?token=uwCDD_TZBGtY5PU2RIqowHexLG_O4tYu6L9N8LLy_XTjxL3Hp0hOoh7O9LGXJFzIzycIeaLniiDBGTZd4-c5_o6bNoYi_omTyX8jRvWvX6gkZ8_AAGxNQG9k4UaYl0LahWwEAGW9m7Tfo-YcX0xNm_TxSbkxX3x4GJCqiazoih1KHYW0diNF-LMFbeXn37rQ16SZ69e3vJayLIjwApxNae87GRMka5PUaRhbl9X1F_zuozVeXddmoF21794UgNbuuJPfvxyOMAiu7SoTHL-U76MdSZ681NJQ1gWuZ9ET5Nw61c-20L5Ealpwicgh81Db0G6WuCE7vZiGSlrWGmX4nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت وزیر راه از حملۀ آمریکا به هواپیماهای حامل دارو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/459414" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459413">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHUR5LFXT0p79XKSWfFLd1BLhaeP4Afe_VD1bx2rMnZ5cumwbjbSTRBN6XTvXmE8E9SUAGdo1k8I7r-EBEQIt0ZwrwXM7RKq1aUTOftEelJqRNDFPmtLE7-qwQYAl19OwBvA0fN5r_ZjPwdMiDeXchezi1bom9cWu4Smeu5qL7qgep3E5fPZyOBiMqfj5OqnOsn5rSy-fYJkz23Srs-Jm0EXlX8VMc9EaI_kfE6e52NuKJrP-6UU7gJm8FfJxyqnXF_Wz5CMo0AEudA3OHJoD6dN7POu_EvvRqJVJlfbfe38YBlnpFnvCC827IZA1VY9t_-PiuwMP_EnYrl1vy5qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  فدراسیون کشتی: بدهی ۲۲ میلیاردی برق ارتباطی به ما ندارد
🔹
سرپرست دبیری فدراسیون کشتی: دبیر با رئیس اداره برق تهران تماس گرفته و موضوع قطعی‌های مکرر برق کمپ تیم‌های ملی را پیگیری کرده. دبیر در این تماس تأکید کرده این بدهی هیچ ارتباطی با فدراسیون ندارد؛ چرا…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/459413" target="_blank">📅 12:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تکلیف سوابق تحصیلی کنکور ۱۴۰۵ مشخص شد
🔹
پایه یازدهم: تأثیر مثبت
🔹
پایه دوازدهم: تأثیر قطعی
🔹
سهم سوابق تحصیلی: ۶۰ درصد در رشته‌های پرمتقاضی
‌
🔹
این مصوبه از سوی رئیس‌جمهور برای اجرا ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/459412" target="_blank">📅 12:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDB5g3Dv7xfGFa8VQl6bvCt6UzLnV1Trv-ZoKdDu8jU8d1CjOoBIEafN6uRBw8ateicN0Jb_UffiDyA4Z0rRkDur2gv565IfdYr3z2qy7B8TDdAV4Ik3ccAzv4v82PRkQesiValaRE_zEOd5Hd7Ov7BGu_khEQK1WcNiA93nhu1IUOe8IxYWHo3rZ6aIzyBCzoxMh44UOmacOGn3vzI__oApwPy5qK9X9rfb72bmpfiywJc6Z6VA1VNZOgD893CWh-rPIopYxh95oTpXnIlkigGQNCVyOAl3Cu8cxbH6oVO69JCMQsPMM_vs_WTCnQzVI1l6EahqRXXUgv-eIK09UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران صدرنشین جرایم سایبری
🔹
رئیس پلیس فتا: امسال نسبت به سال قبل ۱۹ درصد کاهش وقوع جرم اتفاق افتاده. در همین مدت درصد کشف به وقوع ۹۰ درصد بوده که یک درصد افزایش داشته است.
🔹
پلیس فتای تهران بزرگ با توجه به وسعت جمعیت ۱۳ درصد، خراسان‌رضوی ۱۲ درصد، اصفهان ۸ درصد، خوزستان ۶ درصد و فارس ۵ درصد جرایم را به خود اختصاص داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/459411" target="_blank">📅 12:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcP-LTQqAAoAUVcQ-rbUtm6gv2Hb4xM-_FRNZTRLg-8dk_VblP8ARafzltgnFzuFSftSeSNlRffXeInx0RlDLQsixnCLOsRcLd0xNUmjK7-i0WWfsP7uIslEt91luRhb8u12GhuogzmbTs-kBRTr7iMYR_jWSOW8Pxy3cs1-CJCIwbPll0-l9maqc3R5AIlYrwbLOVekg7Aw4mg9_khQ9C_YwdNK1F3k8b601_86vFhX5YKwCf5gITHJB4CdWSWJ6HrJJc6C3q1o4X2VpdJRWXdeDMQSJVfH_DfNOctigzB_5kKYe6z0CurYaLR7wCCQMJv6gQII1gjgrC6Ukv9IKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از مرز ۶ میلیون و ۷۰۰ هزار برگشت
🔹
شاخص کل بورس که در آغاز معاملات امروز رکورد تاریخی ۶ میلیون و ۶۹۹ هزار واحد را ثبت کرده بود، با رشد ۳۶ هزار واحدی نسبت به دیروز و شاخص ۶ میلیون و ۵۸۴ هزار واحدی روز را به‌اتمام رساند.
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/459410" target="_blank">📅 12:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اعتراض به حضور بدون حجاب در جلسۀ رئیس سازمان دانشجویان
🔹
برگزاری جلسه‌ای با حضور رئیس سازمان امور دانشجویان و مشاور وزیر علوم با برخی اعضای شوراهای صنفی، به‌دلیل حضور تعدادی از دانشجویان دختر بی‌حجاب و انتشار تصاویر آن، با اعتراض جمعی از اساتید و دانشجویان…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/459408" target="_blank">📅 12:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNcACdv_BGGULcR61Q6D92Z5JEBmAO6_lH1Mz5z7JBVs_MEMBcmx0KrKVJ7T71g3tZF_EhlpcvmnqBe2xuWMFO_077Pxe-F5lgrGApFARz7Geza7hT-FQF-ZJpO8U2Mp1svRjBY3RBN-9GTRsS5lW29c-vQiRjG-L6AzmxILT9Gaic3qvKM5ZbelgMmxeMNEGqZszGO9-bloBeAAkTjcOpoCJ9I9qArVSMiVM4tRZ21Qe4R1w5V80sg2zUcvTSbvtWJr4qDADlo22Rw6_5daMqmskDUVgBet4T8wA0khYYFYgzOytjZRH4uXYT7kMiytqdhser8VicTxa-viy3btmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدیان، نایب‌رئیس کمیسیون کشاورزی: نمایندگان با تقاضای تحقیق و تفحص از عملکرد شرکت پشتیبانی امور دام و سازمان بنادر موافقت کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/459407" target="_blank">📅 12:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXjzTP2OIekzxwMPluk5JBblicLzJPuB2Y_JPIgRk27XNh24eY539r5WIlySn0DdkrQ6QDSW_aN_um65qvaHxEP1vQqB3nfNsEVVJpvNNkdMRrmcxlcC7Hm9Ls0CYEVme92R8ykOw1higVNOeaufftWbtAcvXoWhwACY9vaiUK1_VYNHfiKdtKFs427y42eSNSZRPObgYNjbs59bBcekXvoeYw1eWeOhFCy1KRX1Koc0BbCDs-Mphb1HxBHF7ihXIKiCnTrs7uxh0nB2UwBFeXfzXzuB-OwzUoZ35j9rqra9aULVHg_23CKiZAgZKxuZXTyAD2NvVh-yAJfCszjClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه‌های پدافندی بدون نمونۀ خارجی در راه‌اند
🔹
فرمانده قرارگاه پدافند هوایی خاتم‌الانبیا: سامانه‌های جدید پدافندی کاملاً بومی در دست طراحی و ساخت هستند. این طرح‌ها به‌تدریج درحال تبدیل شدن به محصولات عملیاتی هستند و «نمونۀ خارجی شناخته‌شده‌ای برای آنها وجود…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/459406" target="_blank">📅 11:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803a537e2e.mp4?token=R1H715YII-JiIP1UH08icGgXBVp5QMm0Dje3_tq-Xm04hTaS3tdUGT54SxCjecoTM8z4J0KMivzAEPTQEyX4q-XuvH0GLxciuRx-f1qDN9pB4sow4nEcR4hbOXWtngfYJFwL_7SEl2njwRwwLtOngXzZX9EpDeBj9Y5FXb-PQuT7YsgirBj0kcXP2LyFhNe7HjrN4bGgz9yJBLKEfZnvyb9HeDhf3yFJouxNJtQEOHmG8i4Riy4iU6Z7-l-PBabLoX_LkEMhDLQEWPFuVsf0dcHK-xzJzK3uAxGWChVYqWKyYgyzISef4lkJF_HkFWf_wSxKlXlKLW1DwOxHUPQcSF3mSjYIs0_kVj84mZoLY4steX5L52wn7ixVDnotXt9BVIsRFgCQLOc-VvQcJESbh_75uGZwVmmvtVEURGnIdlD5MOFHFcbovYawSVgVz9PgDq_cLoIiQgYl-uKZtD-Y7Ogp1ep4A23cVSR3XuSgm1f4LI6erFpOgQePKIi81Q5XIYaa1WwpVfDXtMS1iAEHfYa2-LkNKZ8KSMtkgKQCV-b2m7q8wActLtvRwIcAloX8QTtwCLFMrchbXtqk6uJ84YtybgiNsdeOBG3ZTwB2BQTv5xFxKFmBco8OuSPq1xkU85PPvxdD17OHYtTFEX5L_P8Sx0fgvH2BUwuO-foQQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803a537e2e.mp4?token=R1H715YII-JiIP1UH08icGgXBVp5QMm0Dje3_tq-Xm04hTaS3tdUGT54SxCjecoTM8z4J0KMivzAEPTQEyX4q-XuvH0GLxciuRx-f1qDN9pB4sow4nEcR4hbOXWtngfYJFwL_7SEl2njwRwwLtOngXzZX9EpDeBj9Y5FXb-PQuT7YsgirBj0kcXP2LyFhNe7HjrN4bGgz9yJBLKEfZnvyb9HeDhf3yFJouxNJtQEOHmG8i4Riy4iU6Z7-l-PBabLoX_LkEMhDLQEWPFuVsf0dcHK-xzJzK3uAxGWChVYqWKyYgyzISef4lkJF_HkFWf_wSxKlXlKLW1DwOxHUPQcSF3mSjYIs0_kVj84mZoLY4steX5L52wn7ixVDnotXt9BVIsRFgCQLOc-VvQcJESbh_75uGZwVmmvtVEURGnIdlD5MOFHFcbovYawSVgVz9PgDq_cLoIiQgYl-uKZtD-Y7Ogp1ep4A23cVSR3XuSgm1f4LI6erFpOgQePKIi81Q5XIYaa1WwpVfDXtMS1iAEHfYa2-LkNKZ8KSMtkgKQCV-b2m7q8wActLtvRwIcAloX8QTtwCLFMrchbXtqk6uJ84YtybgiNsdeOBG3ZTwB2BQTv5xFxKFmBco8OuSPq1xkU85PPvxdD17OHYtTFEX5L_P8Sx0fgvH2BUwuO-foQQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استخرهای گرم زمستانی زیر تیغ تعرفه‌های جدید گاز
🔹
معاون برنامه‌ریزی وزارت نفت: نظام تعرفه‌گذاری گاز پس از ۱۴ سال اصلاح شد، در الگوی جدید، مشترکان پرمصرف که حدود ۵ تا ۱۰ درصد جامعه را تشکیل می‌دهند، هدف اصلی اصلاح تعرفه‌ها هستند تا هزینۀ مصرف‌های غیرمتعارف، از جمله گرمایش استخرهای منازل در زمستان، دیگر بر دوش عموم مردم و یارانۀ انرژی تحمیل نشود.
🔹
قبوض چند میلیارد تومانی نیز داشته‌ایم و حتی مواردی وجود داشت که می‌دانستیم استخر این مشترکان در زمستان روشن بوده؛ بنابراین نمی‌توان پذیرفت هزینۀ این میزان مصرف انرژی از جیب عموم مردم پرداخت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/459405" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbfytgA24jFjkl4k7X3bC2vQlWJgWzBbPrCFPDQVrOIbxYUp7rjinRLOMtRCjPH3yIbAG2fI41QYgFPyWtAnh0zS6-TJjUbyRQO79fBqkvtP2BHeyH2WJiLXKNrg6lnyHw36qC4nlXzoJiqTId_2qd8YbKI-lqu4Bf_TjODUX1CFKYICYgnSkH8zSiCD2VkBv-ufOss_CF0Zpw_kJa81-t2QzOrpuyk9cIZM5JIedWXQ_pGV-Nv8YOFfVm8Ys_Wyqrbmpopo0WxouFV44izD0bvi8blDZp16J6zAWFe1183a8GkPxky1P0Dl2CkEC36IG1TJpvU2uSIc3mOrgSvgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشست سران سازمان همکاری شانگهای  @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/459404" target="_blank">📅 11:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvTsQe8NcGInRdqT4zrgiSsXoxM7tqVqtM1ZhdwuOtSBE4WQEtCQjUTTHyjRQTnQj9PKAh_LOgL0MlO2A5-aW_iHc0k_XHq_npqLSveU1To6coMslRmiX_N13Wl3LDiDPkHe8M_V0pc9DQbtykYw0k9vjrUwiwJR1MEOgph8TVbnoMpB9Fzl8J4znycc6tCQ1ycd43Y27N5cNkdS1yDhKcb2k_vP2Qjdnb-4pWykC9wI4Bz3nhB_YcjcFRchjm2aLy8EiNcTE3fkHxtc7sSlC1gjIMtbEAE_AsJoPwvQu2kqVzcXrK9ddmBgEcb8_AN6pI6VuSybZ3SSwHpmzn_BZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقرار سامانه‌های پدافندی در ۳۸۰۰ نقطۀ کشور
🔹
معاون هماهنگ‌کننده نیروی پدافند هوایی ارتش: پدافند هوایی در سراسر کشور چهار مأموریت عمده شامل کشف، شناسایی، رهگیری و درگیری با اهداف هوایی را بر عهده دارد.
🔹
اصلی‌ترین مأموریت پدافند هوایی، کشف هرگونه شیء پرنده…</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/459403" target="_blank">📅 11:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0916a662.mp4?token=IBq3pDl03iQOI_ZZxmt6SVcog2Ttc2jNRVSSegYaqiBbNsYBVT_kv7HHpa0g31GcO__G1fWxHqHhHctGneJ2R4ZZArRO3KtWpVr5da_4KPxAKwxM872fcgD3B0r2HH6yQe5I2kNYG9LpQtOwaW2cdmDgaFBN6Xg51pYonRpNcvZ_3dtWO6xGiWo4PWe5rrLW5K317Aaaz03ktAgXBEGpnWKfJNtLnpMtkkR-oNCTlx9DamC4M_Kam4MGFYggbQP2TZI7KmnrPCrPPWBatN23j6vZEupCsGWcS6IhyQ4vMNmpDoEBhmDYD0JfI7E5bXuJ3jONa1seIuco9c9kWku6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0916a662.mp4?token=IBq3pDl03iQOI_ZZxmt6SVcog2Ttc2jNRVSSegYaqiBbNsYBVT_kv7HHpa0g31GcO__G1fWxHqHhHctGneJ2R4ZZArRO3KtWpVr5da_4KPxAKwxM872fcgD3B0r2HH6yQe5I2kNYG9LpQtOwaW2cdmDgaFBN6Xg51pYonRpNcvZ_3dtWO6xGiWo4PWe5rrLW5K317Aaaz03ktAgXBEGpnWKfJNtLnpMtkkR-oNCTlx9DamC4M_Kam4MGFYggbQP2TZI7KmnrPCrPPWBatN23j6vZEupCsGWcS6IhyQ4vMNmpDoEBhmDYD0JfI7E5bXuJ3jONa1seIuco9c9kWku6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: هیئت دولت طرح دورکاری برخی ادارات در فصل زمستان را بررسی می‌کند
🔹
سازمان اداری و استخدامی موظف شده برنامه این طرح را آماده کند تا پس از تصویب در دولت، جزئیات آن به‌طور کامل اطلاع‌رسانی شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/459402" target="_blank">📅 11:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441bc9d262.mp4?token=lpYwKMyi8v1b1ReIo7drDvke8GN2DKlmM0PU2sJzwcbMNxwwFJ29rYkakk1To5HWXxbJpk98dukHfJuFevhaW8ij-ZRElcfkF5RdfpIsq6Ju5ccdq3K2-9Xu4sWnzwxLh0qtD0eITTDi7zZH-m9lDkhVfEBMLY2uCp6_CMdQckL7MUMg9L5oxdPmd4F1hImk0DOftVs7bqWB68T79pTio3WVharIPFN_AvM3h0mAV6st7tBonLhCRfqshobFO3vl4OkgVq5hpp2chAVtH_cnRfj3DPFCjhWWRhrP64cMvX4kwOXzt_3RG3NdEFvonbV9eoJRaBH_GNDQDi8amaNPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441bc9d262.mp4?token=lpYwKMyi8v1b1ReIo7drDvke8GN2DKlmM0PU2sJzwcbMNxwwFJ29rYkakk1To5HWXxbJpk98dukHfJuFevhaW8ij-ZRElcfkF5RdfpIsq6Ju5ccdq3K2-9Xu4sWnzwxLh0qtD0eITTDi7zZH-m9lDkhVfEBMLY2uCp6_CMdQckL7MUMg9L5oxdPmd4F1hImk0DOftVs7bqWB68T79pTio3WVharIPFN_AvM3h0mAV6st7tBonLhCRfqshobFO3vl4OkgVq5hpp2chAVtH_cnRfj3DPFCjhWWRhrP64cMvX4kwOXzt_3RG3NdEFvonbV9eoJRaBH_GNDQDi8amaNPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: غیرحضوری شدن امسال مدارس شایعه است
🔹
برنامۀ دولت برای حضوری بودن مدارس است مگر اینکه اتفاق جدیدی بیفتد.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/459401" target="_blank">📅 11:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8c03c1c0.mp4?token=kLVK8XK6eSvXddvq9ttoqcFdFf1VjPOrk2LAfAL4cKCXpTP-qNo_soghW0w-5xgygrhrk4eXUwF4joUnXKbXVNeokfgYeHGH1O5hQv1mNn_Q3doLiXT2mimhNZodjq51oJieLjyTzZyyf1AQEHvBXyv97Qeea833I88P-_07N_R3WiZ9ewu3QszpfyQtFdv0lVthXsBGiqZ5tRUQ4N5myhF8n_0boTBa8vB2erB2nvtmekzBqE64lu4VQAzpfV5OaRi5MtWAPEssuqCSGjwoCu2iVFTUR03DWtipHsD9DARLusNhl-1pRXawvj_1HoFZh77V9kg3sgUJQ9WbTifR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8c03c1c0.mp4?token=kLVK8XK6eSvXddvq9ttoqcFdFf1VjPOrk2LAfAL4cKCXpTP-qNo_soghW0w-5xgygrhrk4eXUwF4joUnXKbXVNeokfgYeHGH1O5hQv1mNn_Q3doLiXT2mimhNZodjq51oJieLjyTzZyyf1AQEHvBXyv97Qeea833I88P-_07N_R3WiZ9ewu3QszpfyQtFdv0lVthXsBGiqZ5tRUQ4N5myhF8n_0boTBa8vB2erB2nvtmekzBqE64lu4VQAzpfV5OaRi5MtWAPEssuqCSGjwoCu2iVFTUR03DWtipHsD9DARLusNhl-1pRXawvj_1HoFZh77V9kg3sgUJQ9WbTifR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: فشار اقتصادی مستقیم حاصل تحریم‌هاست
🔹
مهاجرانی: منکر فشار اقتصادی به مردم نیستیم. افزایش قیمت دلار ناشی از فشارها و تحریم‌های ظالمانۀ آمریکاست.
🔹
دولت برنامۀ ۷ محوری را برای حل موضوعات اقتصادی طراحی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/459400" target="_blank">📅 11:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMNzFOp2HUX-KkQlCOZFa-aV9a8-at8EmH9U2GNlKvJDg6dco9_Lznw4RoVB8Ang_ZDI0CFe4MRI-WR4aYzaTNOEK1nma-APzenSHz3m2K97wKSorDOGVhd45zSwcwU4BxYwrpGeY1XkcLq0Fx0RbE94rMq6zLvJEUxXWZ5dczkhUYoGTROAw7ZUvrIuBSoL-h8niw7WFEZ05YzPl1lVRcHPp0R69koQ5EsSGF3SnCSeCKMZse9pa9y1EB9tiDCYQohtmnwfus5AijZpJja__pmz-Jtl6MWlEYIztRse3qj-RMiZZJhEb_-5oxyNMeKFjNdCtlnat2bDZHGMVfQkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«میدان یار» ترند یک توییتر شد
🔹
درحالی‌که هشتگ
#میدان_یار
با استقبال خیره‌کنندهٔ کاربران، صدر جدول داغ‌ترین‌های توئیتر را تسخیر کرده، تیم‌های سراسر کشور در حال صف‌آرایی برای این رقابت بزرگ هستند.
🔹
از امداد و نجات تا روایت میدان؛ وقتی یک کشور تصمیم می‌گیرد فقط تماشاگر نباشد، نتیجه‌اش می‌شود این طوفانِ ملی. شما کجای این میدان هستید؟
🔸
اگر هنوز جا مانده‌اید، پایگاه‌ها، مساجد و غرفه‌های ویژه در سراسر ایران، آماده ثبت‌نام تیم‌های شما هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/459399" target="_blank">📅 10:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TexjFY7TZ2xba6-JVGEVDB1H0OyxbM9mqEdCdQONRqiy_xpwzAt0wOT0CMVt9pcNfrtO3jKvg7gAb0C4fT_-hGHZsXWDx4ym2o0zHCRWlRpfZ0T6txi0HeTQOpHP4wZGaunoPtAy7DKkCsBN6TOFeJDheL5-7kkXoxFRsgFeIsguKPUJAELD_YUJuxCv_W6qbrkIuWP7dfvjzuJz6VCSIEKEfOu2sJ5-s3C5wxtolC0ZeyQBsJg8-uu5UH9hFNpYbS_h2Lz4JtTcnxHR49shDIDVuDcTR-FyT6Ab2hQEFLpHACy6e3k4CNwNEJZ43sji-c0rV98EP-GCajXOg5bpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ زمین‌لرزه کهگیلویه‌وبویراحمد را لرزاند
🔹
بنابر اعلام مرکز لرزه‌نگاری، ۳ زمین‌لرزه از ساعت ۸ تا ۱۰ امروز به‌بزرگی‌های ۲.۵ ریشتر در عمق ۶ کیلومتری، ۴ ریشتر در عمق ۱۰ کیلومتری و ۳.۹ ریشتر در عمق یک کیلومتری، سی‌سخت و یاسوج را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/459398" target="_blank">📅 10:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459397">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmBJktYfg74zecM8aP90DQIXZzy07dETkpYPxWbvWgyMJrwseDQEsuFcMsGbXSD7pMOdWXzfE1CQLhB_14HSgeBsqCyDO0scB4tos6v6075bdSEYO7RESMKiSYz23cI543K7rLrV53CufBFz-B49TvCqjow0LkWgvXEJDPvP9HT5Wa_Ul2K4V4DvFe4hyqi324EqI1gIM6V78zt1uw5FVgpxTtF_fy9rfJRQ44CG3SX5Q9-yN_PiGVO_ifY8K5K06xDOveh01DK7JCMwS6WnovWt65dX6Cvey_Y8KOhe1HEUNHSezZ-DHBovrF2O83qfgqklj3x-7SDFyrec-QqQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون برق وزارت نیرو: نسبت به سال گذشته ۱۴ درصد انرژی بیشتری برای بخش تولید تأمین کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/459397" target="_blank">📅 10:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تدابیر ترافیکی شهرآورد اعلام شد
🔹
پلیس راهور اصفهان: همزمان با برگزاری دیدار پرسپولیس و استقلال، از ساعت ۱۲ تا ۲۴ چهارشنبه محدودیت‌های ترافیکی در مسیرهای منتهی به ورزشگاه نقش جهان اعمال می‌شود.
مسیرهای ممنوعه به‌شرح زیر است:
🔹
میدان امید ـ خیابان زینبیه ـ بلوار آسمان ـ میدان تاکسیرانی
🔹
میدان تاکسیرانی ـ بلوار فرزانگان ـ میدان المپیک(فقط وسایل نقلیهٔ سنگین)
🔹
پل سلیمان‌خاطر ـ پل شریعتی ـ میدان المپیک
🔹
خیابان امیرکبیر - آزادراه آزادگان
🔹
آزادراه آیت‌الله خاتون‌آبادی و آزادراه شهید رئیسی (فرودگاه) به سمت اصفهان و میدان امید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/459396" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459395">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RertljpdI2-Bgh-QHxBBGP1I81Y7DenwfYQH0yU2ZoHpgJPjwbP5NGhG2frUbJQZV588-1iF7fV95KLqf1NDiGjOKdmnmhxOBqFMWhTVXXJ-0Rr0nlBV7bXltZGafEs3eXsRK5tpRvyRTXgyn95HcSPLSmeuGHGJiblVoNuu-0ZDZq_m9YY9OYopoSE9uMT1kDggQsfVVkVD1hMPLvUJs8HhVprfQnUkvtGOryNESeiyPJvLNcnU0-IbPZNlqwopIedQ1S2SXe9xhV0kiET-zp8oh0PXJ7dXTo8v9vSiVGsGG7VgwPs_4z0WP6mRyH_i8V1I788VMVAZWA0NaAyjcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: جنگ‌های اخیر اهمیت پدافند را آشکار کرد
🔹
پیام فرمانده کل ارتش برای سالروز پدافند هوایی: در طول هشت سال دفاع مقدس پدافند هوایی با حضور مؤثر و ایثارگرانه در خط مقدم دفاع از کشور، برگ‌های درخشانی از مقاومت و فداکاری را رقم زد.
🔹
در سال‌های پس از…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/459395" target="_blank">📅 10:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG-WK4yK8Ir6deYYm9sbfzbjNUBCgKE8lodcKpOkbdFCaEfQMclY9T6D0JY14f-CzAwRqCnhCZBagRrk1q_ql61gsDq2dv6ngN2zgSMwHutuP7nN2safsRlZ0dyvDkj9yKgiTkbJu4aXfFXQ5bxeS_qtrUi6cl2zcpJGUsmeihVeAtE2Mimi5jxAJnb5p19I9RqCvaJows9xHWOJS6oo0YCazQz1-mqAeKsDDzJHJi3hZa8vYlVurL4-ZLowkMUKNfq_kzqlkprEJG-BwB0ijW29aaDthI1FlkBFEEsM0zp6vl82N_8TRoxzHjBMYNRDAiAjmFuujOmWoxnquTdxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: جنگ‌های اخیر اهمیت پدافند را آشکار کرد
🔹
پیام فرمانده کل ارتش برای سالروز پدافند هوایی: در طول هشت سال دفاع مقدس پدافند هوایی با حضور مؤثر و ایثارگرانه در خط مقدم دفاع از کشور، برگ‌های درخشانی از مقاومت و فداکاری را رقم زد.
🔹
در سال‌های پس از آن نیز با تکیه بر دانش و توان متخصصان جوان، مسیر خودکفایی، بومی‌سازی و ارتقای سامانه‌های پدافندی را با شتاب پیموده است.
🔹
تجربۀ جنگ‌های تحمیلی اخیر نیز بار دیگر اهمیت حیاتی و راهبردی پدافند هوایی در تأمین امنیت و حراست از حریم آسمان کشور را آشکار ساخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/459394" target="_blank">📅 10:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459393">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeeMnSjH6kvFcTLlJePaqwbC-MQv5OYGeA-gfXPpBTcgwmmQjO-YViHbyJ-G-7m_vjMRQjefCB5ZD2brdwv_4MyCzs1H6RDfX11J56R_lMzBOWFrBVGsaTvB9jypvagDkmG0WiEhsjFHeJS2tXBzldMtsh95PyvRITleF3l8MYMhEK_DjiusL1tmMP9y4peERSVHtQKHh4NHFYNQ5rkwbSnOFUZlxAx0Ipn2n3ElnsCrKhIEga3XxY0-IJRXTc8zX2CzLGKk7KFXIXN0YrYHvrzf9J1GyjeJhXMzV9y2oieGQFwF-y16d6Q5aZD_wuVoVB-DHDxNZmCVxCYSGGqAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان یک چالش طولانی در صنعت پتروشیمی کشور؛
✔️
تدوین نظام‌نامه علمی «انتخاب لایسنسور در پروژه‌های پتروشیمی» در هلدینگ خلیج‌فارس
🔸
سلیمان‌زاده، مدیرعامل شرکت مهندسی نوآوری و ساخت فناوری‌های نوین خلیج‌فارس:
🔹
انتخاب یک لایسنسور اشتباه می‌تواند سال‌ها تأخیر، هزینه‌های سنگین و حتی شکست کامل یک پروژه پتروشیمی را رقم بزند
🔹
با وجود چنین نظام‌نامه مدوّنی که پس از ماه‌ها مطالعه گسترده تدوین شده، دیگر موضوع حیاتی انتخاب لایسنسور به دست شانس، سلیقه یا روابط شخصی سپرده نمی‌شود.
🔹
مرکزیت بخشی در تأمین دانش فنی مورد نیاز هلدینگ، ثبت پتنت‌ها، خلق اعتبار بین‌المللی و دستیابی به رتبه‌های برتر جهانی بر مبنای روش‌های فنی -حقوقی از اهداف ما در تدوین این نظام‌نامه است.
🔹
این اقدام نه‌تنها ریسک پروژه‌ها را کاهش می‌دهد، بلکه گامی بلند در مسیر خودکفایی فناورانه و ارتقای جایگاه ایران در صنعت پتروشیمی جهان است.</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/459393" target="_blank">📅 10:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glV2saAncMCf1cIxRWoTRaL86N_7Ult2s7pnQDAxFekKuzHHl0jAphGzfDmP6JlzyvTld0WfW_23DCa2enDjac0y1XkF18QHhedWn90lRMwzkIHFZ8ZHGsnkdpNgWC8UQ1poBnVRwjK9dCTZZgvGxzHj4hoh44l9BYwz8qOs3AsWN8lls-CHmOeLFIjutq3j3hLkjpdT0mYcTQNvm_e8HFR9R-j6v6ZvaQw5Jadrc0wFth1V2DGBapewcCdNZZzhISbKPFWIS33kS91HY8_cLyTeXVXt95ivvcyR5HlhTkCqj2MORDLkryKPXMPU5ffZORxqBhWnJvWttr4tqRfJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
در ۵ ماه اول سال ۱۴۰۵؛
آغاز زندگی مشترک بیش از ۵۲ هزار جوان با تسهیلات ازدواج بانک ملی ایران
↗️
بانک ملی ایران در پنج ماه نخست سال جاری، با پرداخت بیش از ۱۷۷ هزار میلیارد ریال تسهیلات قرض‌الحسنه ازدواج، زمینه آغاز زندگی مشترک بیش از ۵۲ هزار جوان ایرانی را فراهم کرد.
🔗
مشروح خب
ر
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/459392" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459391">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/459391" target="_blank">📅 10:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459390">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c41f3847.mp4?token=F_lmKylN-ZC_s8mh_F63SXpa-FhwvHc493V9KXE9CSGcfUoFc0Z8OsH5qLpXeFCXYKOOxjswnvU3_f-rzC917WI-pFXSSA1q-czchoy_S8IJKIl5nTWRDg4MLTHGY8huys_czpwWDJp9j1p-3XEJviWTSOo96hKKSF0TdjqAX1cCYGJwiBtQ-IMX_hDBevvFrs6sTu3VPLT8znHrBeOXeUxJGnXabWzS9WwZeuRSyI5557OixfBXnWsB1TcxJz7NocDONaegXGPdPyRUKJ54fm04jmCjdJQkw5o0EdxPZsCiGkgu5nmkaae_zPKVYDpszvgmWf-2XxxEWGfkN8ziLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c41f3847.mp4?token=F_lmKylN-ZC_s8mh_F63SXpa-FhwvHc493V9KXE9CSGcfUoFc0Z8OsH5qLpXeFCXYKOOxjswnvU3_f-rzC917WI-pFXSSA1q-czchoy_S8IJKIl5nTWRDg4MLTHGY8huys_czpwWDJp9j1p-3XEJviWTSOo96hKKSF0TdjqAX1cCYGJwiBtQ-IMX_hDBevvFrs6sTu3VPLT8znHrBeOXeUxJGnXabWzS9WwZeuRSyI5557OixfBXnWsB1TcxJz7NocDONaegXGPdPyRUKJ54fm04jmCjdJQkw5o0EdxPZsCiGkgu5nmkaae_zPKVYDpszvgmWf-2XxxEWGfkN8ziLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناریوی آمریکا برای القای باز بودن تنگۀ هرمز چگونه شکست خورد؟
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/459390" target="_blank">📅 09:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec51668b4a.mp4?token=S3GcwxVsC4lXZXUXTgywTRV7PFGjnXtLrGqomMavkPgPz7tUH9j1QuZaLCdg2WBQXHJA7CmKSRPplgT7cqMsgUSp_ovo6l_j0XEvWhFzdjK4jGUy0Tl0ipwOO2mT2avnH2PR3aPuWmlZabUrhyqlrOteverflCA8WRUpLDOpjXJ39qtmyGtGNXTlrshgig4-yd5bnOllkWVy5FsWa_lQaIRxaCZsiVAMbKragJOaKwT6LinkSfztelAjBL2NSLWxU0wTZstTLZetvkbvtwMBTzbddqszPcOfbR8pUY33dTpXAJeKN4NXAivSaMPyPYCpe0gH0cB05puAR7nnV9eGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec51668b4a.mp4?token=S3GcwxVsC4lXZXUXTgywTRV7PFGjnXtLrGqomMavkPgPz7tUH9j1QuZaLCdg2WBQXHJA7CmKSRPplgT7cqMsgUSp_ovo6l_j0XEvWhFzdjK4jGUy0Tl0ipwOO2mT2avnH2PR3aPuWmlZabUrhyqlrOteverflCA8WRUpLDOpjXJ39qtmyGtGNXTlrshgig4-yd5bnOllkWVy5FsWa_lQaIRxaCZsiVAMbKragJOaKwT6LinkSfztelAjBL2NSLWxU0wTZstTLZetvkbvtwMBTzbddqszPcOfbR8pUY33dTpXAJeKN4NXAivSaMPyPYCpe0gH0cB05puAR7nnV9eGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل نپال از ۹۰۰ نفر گذشت
🔹
سازمان مدیریت بلایای نپال اعلام کرد که تعداد کشته‌های سیل هفتهٔ گذشته در منطقهٔ مرزی این کشور به ۹۰۳ نفر رسیده و ۴۲۴۷ نفر همچنان مفقودند. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/459389" target="_blank">📅 09:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FD2AxSoRppVdY6UyEqSq4rimOi6uieFtEc7-SvD-7VoGUFVhEt1Cx2JTlnkr8lU5A2Bj013qhTYe5eKVtpTcy6-XecRPkofnQTjPc3Q-8b8rH3vp12PjEAvxNv9MSHPjbNrZ1823Vl10AbBjm8le3AN8b-bCTBwpl2SQQNz7PgG9EpfXoCOIPafPvONcHj8YQcg8Cojst_-BsmEpYyfqnHWroFwd48mswaVLS6sua2TNCCbj9b2QyvVXnw1ev2wv7LxUUEbL1rZDIKAWnWDuOO-BgtP8YRDQmHr0XXDvTF0RZrf0HcVP5b_oHHf1Y23ZwFOU3AstIriqxXRb4uU7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2KxaEGvsJ-MCVc-vbyJlgWXGMjW6JZK3FvOxNOcZd6fQ03pRkQ46X1YYysU-TN7ho0ofBgd7UOB8DKL6mXO4HvXZFws0dzE5qKizke9l2m_0gF_ntpulg87F4HP-CrwVh-uI4kRPrDaFAce6qfU6G2AokJeG5NjPNghjYmaDp_UwVh-fwyvf1Mzpl-9xIxZHRZrbBd4awXkr6XNIerPchQKeu1X8LqtjIwxCY6HGBayUKCRmTbrdapg9H_5S2x0YWbicmfUXsRe4NdzvDeK2mnEV5KTz6Xdul5biVkX4Kkhvqya7e3zuC75LGlxXxHxMmIvzhFxLv_EBYfr3b_-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1fnV37lrcm1oSdHPEJlIvPWvfEFaMQb-Uwl_-V4WurtF8Y85BLBSzniNvbraF6e9RksU5svgDhz1J6wAno8zuM3D2UCKZElz7NtDe3gwSe62prFIaC-Ky3Dpp3lo0c3C-uYHc54qilKpWVzcCxZ4DIqKLz04WB07gh-SlN1JqCUJ_7k8O4YwzV6o8yophGBNAM9lZs_8w9U_droCM5rhksCOt2MVHes_Kuh-qv9ICZ9SRcT1FG58mmwu44WMULsQNpvpfF7d33M8fdJX11jiXZ7cDrnjkBmlQYCvf30intfEsMT2o28fnTP4yijR7EsKhXhFbCOWAsvLkDiNx45pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXzoIPMNzbV8ZIB1-RLHDHkvHxvTGmXmRyXLKY5ix0_WMV7F5v2clxX7VD-_g7TsmZZkvaEH2avVr9qWbRfET9KxUAI_6o6E75j21M6SJBTvb1hNpgVabyFvv1g9XjLA4Vv5s87hAVETmS6mFcZ6I_TIGKNdVKA7H9XLnk1WgHj5hMIrY074vnY04gGV-rgKjpZ8EC82BLlEfMciPVw38nAlIPqElAHQBqjVnLh5FHnacwKSTBkpQ2pzpSS2zR7iy2rWCaXQowbqGQx5r1PeKlwaTrSDkGkVPmK3IhsMn-yiL-GQafsf6PlJI1aX3Ivj6XpciRkYf6iG7Zk7sc3Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6Xcn7KVIAwYGy2eHC7vRKhfgkUUmptO4bIdNNs-0eR5tgUW6qV5ONUPBll0NbyxEvJ0nSeLuFEhQPjSK9_9XMjBJmFQ1TFsWr1MMgzGnk7GlkLs0RIRD9XXN7fiW7fHBAaqintThzsyskS2wj-d4JKbktWT6B4Xvl1A1jYOQxAjT1E9jpiPicRcyNsyXsjtTutoFljT0doQGAyh5Kt6lIsUHNdYi6jDl130ChxpZWr-dsFRpW_NAPYl_z8BOwMYxf0IYH69unKzYa7gRyJy7WljiHQZxFb8so1yiPKIiYeezb76sK3p4mW-mdFdY5O1V5MXV5CvLPdLGd7oq6xZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sshkNIZRONjo8A-gWHX4-o6xjw6K1PJabYeFyhzRvagEMyiDvmGDtmF0Vxl8uxZUcT48GLtP8FS1oxbcq45VwBZ2PPKD9lhUrY3Jnle6psH_fl_IJoNQMlm-OntgYWvGyhBv8dmR3nU493gg00khfSS7ya16HAC8lztmS9rtq8Fn_pHNiCzhE3KcgjD-nhgMYtkhaY-MtUMSfwjV4sS5Xq39LUfPsxTJ4ujCReDLDWAklTS5yBY9ii7DJYQ0pzeJgDWuzmgbjU096VnTvBWakFpnjLV-b_EEJJ5Z_xfXBIrceGPC1Yl6CsOln7nCE0hJ3FpRe9R8oQNCnbaLzWwecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZUnBQAzzTRFuy_P4GCkrpACquu7BQvxOOPQot37aVQz2ZuZB25rtbA_Nl8PLHu9P9GJ9E_l-NN9UZ3Ui0jLciJKhFJHQgrvl4OYQ7kjNM_Xo8gLH40eYyp8QZFluJ42Ga_7WJEAqHferzQ0kyouW8T-ww6afgrJGUvajutu7ssPGafYvzsJfcYIQMtA48ENyAwljirajfbYUJpHL_SejENJePSrDIZAY5xvhO62xZHUoeCFjjAKNd4R2Jj9U4S5QqwpGfVq002LkM85B6biSE6XKxYC7pIVyfMHPuqZGrlvklDcbjq4yMTxSmNU4W54Qm5fQ0lkx9NhxuMuVAs5Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: رئیس‌جمهور آمریکا زیاده‌خواه و بدعهد است
🔹
حدود سه ماه مذاکره با میانجی‌گری دو کشور دوست و برادر پاکستان و قطر، نهایتا در تاریخ ۲۸ خرداد ۱۴۰۵ به توافقی منجر گردید که به یادداشت تفاهم اسلام‌آباد معروف است.
🔹
اما تعهد آمریکا به سندی که امضای رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/459382" target="_blank">📅 09:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbrjKpDXOLuBAwhiQ1r08p5mixhPusmI4fVBF47bwp03S6LAUkUKDumZR1Sd28Eet7X7SmCpNm8QvkzALL0OxZdkE1dI3WyI6VNMcmmwsS9E-JPFd9R5BdCbW7yWc63LT6jNqfvwZ4OWoroVck-Ql0dcwXG99tGJUx27TJPvgkQb6wd7Km8sMKlt_eWsvNx38C4MTIyN6GJn1QNexgOFM1KltnNr740EMM6Hh9uM3FnHMvvdcgmD3JEcdk8Kl-oEiizn5lzwtvTt5es8mKMv040tMV--N-I2mmY0PUP0wI0A38X7wMPZOAFnL485ZMworXdT9Rg9133yCmompCADFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/459381" target="_blank">📅 09:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxgrK54jlUwDIX7JFx1sWSQ-dlEXGyvUb4FHgBOCrV0zfFRjqPMmqyOGie6vKuvHLd2n4TS_t-otWYBBHNl1qwqh67UA-UqKc_0vpeELWzf6tIuQ-Y5X3P0vocXmyZw14jqpiKg06eSCt-i8pSh4IuwE3xvHbtRBif7rOTBLayYJXMqww_kjbH_k7O9oZuJKlXcM491FuVxcI77Vnh_Ukj7ukmaZFqv9jqYab8I2elJv7JayNf7ZV4EnPg8swSMeFzz6r2DB9CYBQK5WjCawvJkU3u1blJ5MFCXN0BQUDrWjTyUBJluLaO8LYy7UPcZb9_QBVryTeegIZIj4GIgbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در نزدیکی عمان
🔹
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش هنگام عبور از تنگۀ هرمز هدف اصابت ۳ پرتابه قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/459380" target="_blank">📅 09:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXCdeDvx8KY2QjX7NdTkORvvn8tz8C-TiMrI4O3E7Gt0bYqZiSO46dbgL6e93j76x-6JjNryBlZJitL1GLTbyRJq54HiTFgxhBXZu7Zyke7KzMtdb3_EGX75EahP3Ouk1KgbcGP3CWLsHOrPIDsQtl8XN24YokBktFR2bOLdcPCPb5YUYvzp_TgBjhDhiB6q8W6W7mTapCfTol8rcIC9q_kJmuT3TqA798N59qa-coY1T3lSVgOh2EO8NnwSttzoKQV1w9vI-BPUXXhhNrVaQGeIWtj-O7zskmEFdhHCHt5DSvT5JmDlwFA5JX2CF0FHOZNoXmK8hjTt_rrVsWARhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رئیس بانک مرکزی: ارز داریم؛ به قدر کافی هم داریم
🔹
این ادعا که ایران وارد فروپاشی اقتصادی شده، به‌طور قاطع درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و کشور علاوه بر آن، از ذخایر داخلی نیز برخوردار است.
🔹
منابعی داریم که به دلایل…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/459379" target="_blank">📅 09:26 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
