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
<img src="https://cdn4.telesco.pe/file/JrcdLPVoSWmdR8xeAAa-jWDZeC4M_onXXPkasPvqhCmVWm9ztMGhXs5ip9cD6YArjg_4_cJWAD1IhY4xrK3LhuZvUzMcMiw4u8hkEIHpoLQudnSN6yEAweK8tTjJuv26PAjq9gW-0mLOS7H1FfngV-WW_0ut0Uv7QJnYBFSD6ONRjmycQl1u6Z4BYzUwFH39BqJjEG4DadAvio0hGXViaKajM_EXcS512POC2wr8ajK-fend86VqoI4ISgNVHDaAD1rVNhy8N7igAlCKeRdJLVM5GgurshbcH8JzjtBSudCM_YcMCVvhhz2-r_t0rH0Ip1zd_eC3khsbOqGIpWfFag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-462987">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7touxZ7lXmHBLXCPoA527piSSmlnVK30cFFFcFx0nuRVxYZP4RyAchbPd4n2sq55seCT-1BUWaNILCUEiR-Qaed9xuqnMYP11Fz5XI7e4DEjKiWFH2phiCU6EmThi6db3XpY5fLuSNuocNanfJlpElKrShTpMd_-hDYltNEjsWKcWush001IodtRN0dQtNJk4i_GYcyeD2WOsparM_PtY1kcKolfcQDVqCk7zKeCkcv2Q__QeiL6Crm4Wc8kvclSmBxYl16S8NPC72FPPbYtq0Y9LGxnDofMb1NQ7P2jqDeFy5j252D4mYFlKn0oouKI8Ym4xJgQbCi5yExsFgXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل مازندران به کجا می‌رود؟
🔹
خوشروان، پژوهشگر علوم دریایی: اگر روند کاهشی تراز آب که در حال حاضر حدود منفی ۲۹ متر است ادامه یابد، جغرافیای سواحل مازندران دست‌خوش تغییرات جبران‌ناپذیری خواهد شد.
🔹
مطالعات جدید نشان می‌دهند که افزایش دما و در نتیجه افزایش نرخ تبخیر، این تعادل را به شدت به نفع کاهش تراز آب تغییر می‌دهد.
🔹
بر اساس مدل‌های اقلیمی، در سناریوی انتشار متوسط کاهش حدود ۸ متری و در سناریوی انتشار بالا کاهش حدود ۱۴ متری تراز آب تا پایان قرن پیش‌بینی شده است؛ هرچند دامنه عدم‌قطعیت در این مدل‌ها قابل توجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/462987" target="_blank">📅 15:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462986">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امتحانات نهایی در رصد پلیس فتا
🔹
رئیس پلیس فتا: همزمان با برگزاری امتحانات نهایی دانش‌آموزان موضوع تبلیغات فروش سوالات امتحان نهایی در کارگروه‌های ویژۀ عملیاتی پلیس سایبری کشور درحال رصد است و بیش از ۱۰ مورد برخورد انتظامی و قضایی با مرتکبان این جرایم صورت…</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/462986" target="_blank">📅 15:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462985">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2c369a7.mp4?token=FXD2FiXe0_F22sJRA8amqoLDbzhQW9BsChg-mN3Sdspb9oRojvftzuwF_Df03EG2KmnRB2lsFcf-CyRGrC13z-RbiOIzQNOTnNuGNc6unb4zx6TgqA0A18C-X0XiKYyi41X6dhUHxc1osaYJgLKpauiYq_KbnFpK00RiKalZvwG3e9Uhzz7s88qsmX0N3Mw-hSIHFxcBoiB8SFANYn91rL1GHonHjnBuFf7OCq358xsNsWGVD1AbXwo-HySNwkoADwX2pq_6rV4BjF7uscUhW9DLygfwg_Aa1nk-K8GDUHX-_2aTlUZyG0NHY4B-iz5sbNaYS-XGVFgMp21ifhq3iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2c369a7.mp4?token=FXD2FiXe0_F22sJRA8amqoLDbzhQW9BsChg-mN3Sdspb9oRojvftzuwF_Df03EG2KmnRB2lsFcf-CyRGrC13z-RbiOIzQNOTnNuGNc6unb4zx6TgqA0A18C-X0XiKYyi41X6dhUHxc1osaYJgLKpauiYq_KbnFpK00RiKalZvwG3e9Uhzz7s88qsmX0N3Mw-hSIHFxcBoiB8SFANYn91rL1GHonHjnBuFf7OCq358xsNsWGVD1AbXwo-HySNwkoADwX2pq_6rV4BjF7uscUhW9DLygfwg_Aa1nk-K8GDUHX-_2aTlUZyG0NHY4B-iz5sbNaYS-XGVFgMp21ifhq3iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان بسیج: رزمایش جان‌فدایان محدود به تهران نیست
🔹
موج‌های بعدی این رزمایش عظیم و مردمی به‌زودی در سایر استان‌ها و شهرها برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/462985" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462984">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📷
رزمایش ۳۱۳ هزار نفری جان‌فدا با حضور رئیس‌جمهور  عکس: دانیال همتی @Farsna</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/462984" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462983">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311e3e5dac.mp4?token=BM0cf00qqEOaHVfASqgkqpsvfmaaIcN66lOkPIhuYWs8LvEW5xHRsdDUeaK446KFP8JbJcFn_KNJW3mhktDoF4cRjW5ReEp5UL3_tctYYMOzPNEAhqIp4AY5IQdECU84vhBqsuyUcQWPt9cm5ZJXu3o7otiQBCVUjH9m30czGSj2J1uhUH4yqUGV9T2BX2Rh57p0B4cs96eNpG7sUSiz8QcwT7vb32rY3UnjgM-pyijOwr408yTlbeh0jytAFs9F4FXr-okNAMhR7yWoeAVKyVsMCwFeWAYu3wkttmcaSyreEeuVNgdm79A7V2tM7edy5uDosZIl6lMYz29JgYzMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311e3e5dac.mp4?token=BM0cf00qqEOaHVfASqgkqpsvfmaaIcN66lOkPIhuYWs8LvEW5xHRsdDUeaK446KFP8JbJcFn_KNJW3mhktDoF4cRjW5ReEp5UL3_tctYYMOzPNEAhqIp4AY5IQdECU84vhBqsuyUcQWPt9cm5ZJXu3o7otiQBCVUjH9m30czGSj2J1uhUH4yqUGV9T2BX2Rh57p0B4cs96eNpG7sUSiz8QcwT7vb32rY3UnjgM-pyijOwr408yTlbeh0jytAFs9F4FXr-okNAMhR7yWoeAVKyVsMCwFeWAYu3wkttmcaSyreEeuVNgdm79A7V2tM7edy5uDosZIl6lMYz29JgYzMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.  @Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/462983" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462982">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvmwfQhaZsSpWGdZa6_FvtzPmDTChU58iFyzTxZrQkMPO2Lp7s9lPPtBe1dULqJ4m_7LZeSg800hETja_IPjlbJQmDtnxauzVE502zEBIij1foJxAnNoQ84tZfqMEFYyFmiXXHdG_d52UwMyuSSXaByLpnBd8Y3gT47O-d_5joZiT7jTnfK9biPIPLc6Rb3okujRjj1kq26V6wESJS10--fF-BV7t9RKVh__JNFp07I61MC8tNtTZFIBYMZhdcf28HjYs6z1UGv94rgUlCgRKx-awg66d9etWoGg6zj9NjT1ouWlBzi_ypMaZDnAUlrs6BNxBqkkUmVwtDxj1lJqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروی خارجی وارد شود یا نه؟
🔹
امسال بیش از ۱.۵ میلیارد دلار ارز به واردات خودرو اختصاص یافته؛ رقمی معادل نیمی از ارز مصرف‌شده برای واردات دارو.
🔹
موافقان واردات می‌گویند با جلوگیری از واردات خودروهای خارجی ممکن است سرمایه قشر پردرآمد را به کشورهایی مانند…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/462982" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462981">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0cd9dfe8.mp4?token=vSvhpL6fw9-GcMv8PMIBQGUo_kgHi_jdUjlurVVbkQzNM9RJleLNGUHBOLlTO3TrtbEamESPs3sIkp8KM_vm8HauSbFgsyqM3LBUq26u5o0u7hF3UvW36KYKtUgCBIKzqV3Y1pzDKZjeQcW4aVqNFvhfbYE4h9KnOAExeBCXUMW0eKgz_YFPlgw4VG54oCwNlndae1HN6MkWoLuAxc9iFt0qW17kaVotg0F-Cx4v1adj8s9260iucH29J9uKChcPpyMf_HBseFyKLSzvDIJ_xs87lNbHOSeJTa-h3ZKQPohB19skKsUR58zPl2WGDLzm6ql_lORKnuckvKo4b3WJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0cd9dfe8.mp4?token=vSvhpL6fw9-GcMv8PMIBQGUo_kgHi_jdUjlurVVbkQzNM9RJleLNGUHBOLlTO3TrtbEamESPs3sIkp8KM_vm8HauSbFgsyqM3LBUq26u5o0u7hF3UvW36KYKtUgCBIKzqV3Y1pzDKZjeQcW4aVqNFvhfbYE4h9KnOAExeBCXUMW0eKgz_YFPlgw4VG54oCwNlndae1HN6MkWoLuAxc9iFt0qW17kaVotg0F-Cx4v1adj8s9260iucH29J9uKChcPpyMf_HBseFyKLSzvDIJ_xs87lNbHOSeJTa-h3ZKQPohB19skKsUR58zPl2WGDLzm6ql_lORKnuckvKo4b3WJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال تحصیلی جدید دانشجویان آغاز شد  @Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/462981" target="_blank">📅 14:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462980">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II-Mc7hqv7BVtlLRiMXFgWqTpttLCa2OyQeZZaoUSU13OcMCs7w_hbHx4p1H_AA3UpttNyW360-OJoGp6UN6RysHx0TCl8nLfv3BwE5mRdx4k0hGzrGj9v8vcEYJIie2jz4tcCxaH1GJT5sE0g88r1wNULK8vkxOKGUjxg2munXAlAiOQzsePPxFLMMyZjM5BwP5HkiZF_v-ZTB4Bsixgqrz6IcMdZzpsuRodl-jLY4XlItdU-GfCpTp778j30roBAVFPwRLpF44zv5OkNYGXqwsaKydR_pjD-fl0bnbZvysyr7MR5Reac0oEbwK9dEKSoTiAZtJQlE4y_VZNqURMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب شهریور ایران از دلار نفتی سرریز شد
🔹
درآمد نفتی شهریورماه ایران از ۲.۵ میلیارد دلار گذر کرد. پیش از این در ۵ ماه ابتدایی سال بیش از ۱۳ میلیارد دلار از فروش نفت وارد کشور شده بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/462980" target="_blank">📅 14:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462979">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjj7GRADhvtAnC1-PAcQntqek8Qkmu-EaDtGmf-0H_8ggMXayIxhDSH9-FiJ5b4Z0jkzNfJXwVzmFyplsg3s5Iw3Sx3i2q86kc-VAIdrublkxgOAPP3sNLjbwLtbB7K4yNlTt5P45nDDSzF4XGD-9CrQLv08C9UFcXimhLB637sNdLDjrdyxjjPDdIa50KD7onZjjXF4pBLfJkiftcO2VYX-dy22zTwIDi8jlcsuVkUz1h2mx-YLWBRQR14eXx0sP6iwgwxjwcL_zefS35CXp8c3pdsV03jYPnMf39bSI3lfkfH2jsxv1JEt58n6vQlx2hy8Ewv-Ki7IOA80psPFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی با انتشار تصویری از مشاهده آتش و برخاستن ستون بزرگی از دود در نزدیکی فرودگاه ملک خالد ریاض خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/462979" target="_blank">📅 14:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJkpTI33dxhst_FNp2dPrBqwD1O_39vPbXjBwuC3FzIgT1D5qrgtOTovYMv1RejYcxeVDFgTUkV6STFwSZUMAIBgrszd_93T40vfunxVMOaheWQqMak73--Eg8D4X5amQiLp-MZTrgbI-kKs7-8RR8l34v3Q2jthnHZqb4meOzH3W8SFfbRhTc1i_3E-G2WlzaS4ZAKtLoP5Av0WOIICL0qfRpM7eAJWfHJ3Xb2efuZ9tRczSHBlt_e4HnYDRCViwEkHeY6E2b53LWGCNYCMyxUTFi_A-BIl5UBbpGqduk5u_GZd5C1z60Ld7dSVGtYZX5tt-rekcNOGUOLaW_5LJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyB0KEm2ztdAXbNyXCEmbgzs-K9LeQqdDz7jEIx1f4kyUC0ZVdQNmzyO1ebMGzI9h_FbHQtil1G913ZIbtxrPLy759-dKzdojm4XC7VjoJUKXc_n6WusY0Kt8BCGVuXschAypMYynymyy-PKDDuxWLr1AR1DyEIV9W1IP4ToTsURO8xOk9ZbgYUn_L3Bj39cJM_7y6QkYz7wCaWCcl58A_x3oTHYaAzg0wkN-rmf9n75LSayZYljcB-75BjF1xQh12aD8YDm1tOXhluhVU5Dd7QXln4M2MWUS-GtjM6_lZnlfdWUVMB13WssBbDKuRRDoNB16eRlMoDhfJY3zOqXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TheLsrTVJ_Xp9LHRxhtxBANdmuJ8Yqa3EYsOzK5DoUGWhCi622hEPLBhLkjbXMGli3NPAoebyYCJ6RddoNzmtk99Ga0mFegaM_8IVU6V-JVkJtFi5y7Sv2-2b7hZnTo6E6xzIFynV_8ZTOB2wDlo_wXR208ozv9R7z_oF_3Rs6-JUttPkV7wowvYcmja3tGHcGTDvqB0SD2WKTG9trhYIw-orSYJ8dWO3KXwV-qsTatWZ2eu3bAXxNvRTtMmug07z70Ygh91l4fRbZYH8Z11lQAzvWuzzyu4oVF1jwskfviOc6RbiXZBgDbkU5MKWrYBA55IGZLYc1ylUxczHAJkXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPUfOMNfAnXVYlSa8RptY15IGkD8lRCqA6wyO67dO3L6ZjrdaWUwFxpQfydEVhTG2U8ldT8wZzZUfKmv0mblLL98QWO32K1NQf1xtds_GdtqgQylUdIxEeymiVni8Bm3ZjU6rzhM91_6dylcA_al97tFeENIJc-hi1k_RUQG-wKSpgVCk0wqnfjif5xH3ypDuElxoB5bFClKnYe8QvulI9iW8UEWCMnnKK-LgJlR1oLJsz50LDQFA7nwpLSiXgWPBpdLAw1Lhy2CyM_Y8D9Z40N8NvHg-te_CYnKk8x-Myde0RW9gD4ZYHd4vGGI1cU5AE9QJgQMtORS-dO7eKjvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfHQ_77Fk0Q0pok4OkS4eOPgH0v2CziyAaGE6xbWI7V0DD-2C1dXCqDl80HYxXmmJ5AN8hdTdXSshhxSyxe6Iirg9luyuSVq1xbbbZSrHa5niM65w8UKnKyxksakeGkfDRTyJz21UjCW2BzCqzqoUDUZYnMoiOLtp4LRD4MRZ6slOIJbywR3oP2rS405yoUyvnr71Z27Hel2vgZXbWGhzMpofTvB4roNgA28ofniknzCLRBN8UdSjOHiL_jwtQYSj3p9nh6pyh3X9ka399jq0T9km6ee_b8MFh2T21ct-HctXCUfxm7pDx4gRbSheVM79RPDWCUeM4jSXECh4KOwtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایش اسبان اصیل ایران در رفسنجان
عکس:
مهدی امین‌زاده
@Farsna
....</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/462974" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmakd1ARNF3St6vTihhQnJCHE8xXkS50kMTc-qNXW00OSPUlLDUy9g1D6OELoNuNqPDAiThqVLpGTL3z_ZK_nRwfFsfTvNEJOeKcChcQVqPtvgNdR6nlh0Krfanzhl-z2uVO6zwH3Nb4xzEwFz2TMZfVnhfnUUfjOx31TCiMlkrhWucz1sIUBsnlaDp5CnfcowN03Vjk0TOz9T9Nhsy1hUPQrCD-tGkXAbJeJO-_JzTLEdFQI4zXUsZ2dWY5qZqZ1AtCgLDYoiJ45s1IZU54czn3ppxM_T7A2xcfEZoUEqv0Ew9gkyalkhR1zNcRhv49RJS2JrOGDdECZYo7fcxhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی با انتشار تصویری از مشاهده آتش و برخاستن ستون بزرگی از دود در نزدیکی فرودگاه ملک خالد ریاض خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/462973" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c0bd9395.mp4?token=roCBjlWvQRJseko6HiWHJooTTcA8EsfVLzjDDEUy-4zMv7OTN_kjhYPM17xElneB69bEQXurjMfy_cV7UvwBKuFrPhNNbkquJ1ubatnbDzC_v0kGRoGWSVfv-9GbKEJHzj3Ki28qzEvWLeSiUsycBF2Mtqht5eEe42inkjGTVjpTaQ0O1Ln8L0D5z3gTuoGiYBVeE8nriTeMp-tcfb3BGaJSOfn96mE8BlDtJ_qRlcvfD2p3tCVVxvAo1k3tZDFj3hqJ6L1iMBk5eNpxe4py6j6hHulMdU50SbyOuDWitIuMLivlhzVMUM62fmXpjDIZTDYR7AUa5vkZL4bMFQ0UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c0bd9395.mp4?token=roCBjlWvQRJseko6HiWHJooTTcA8EsfVLzjDDEUy-4zMv7OTN_kjhYPM17xElneB69bEQXurjMfy_cV7UvwBKuFrPhNNbkquJ1ubatnbDzC_v0kGRoGWSVfv-9GbKEJHzj3Ki28qzEvWLeSiUsycBF2Mtqht5eEe42inkjGTVjpTaQ0O1Ln8L0D5z3gTuoGiYBVeE8nriTeMp-tcfb3BGaJSOfn96mE8BlDtJ_qRlcvfD2p3tCVVxvAo1k3tZDFj3hqJ6L1iMBk5eNpxe4py6j6hHulMdU50SbyOuDWitIuMLivlhzVMUM62fmXpjDIZTDYR7AUa5vkZL4bMFQ0UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعدام خائنی که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار می‌داد
🔹
حسین پدران، فرزند حمیدرضا که اطلاعات سایت‌های نظامی حساس کشور در استان اصفهان را در اختیار موساد قرار داده بود، به جرم جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/462972" target="_blank">📅 14:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6bfc600a.mp4?token=o9aT-JXojQkLlPUmGfh94VTz2ZI00odVSVIydgPULIGnFm79vgjh2cr3IaSlRglJNOQrExoW2KysLts2SauzN4pMg2TJSpkIQtOp_Kh5SHVcVjk5ZNE3WEQFH914HTZGvif7awIYumlUY0h8IXoMLMEFftjgPrOhkQalbppwIUIkkyKsZ_yrGHstFFm8gzo0v3K4ZMIkw2JmDYQkbqH1Q2vou2xcLBioxJMWnXpMpBINWYOH6W80Vx7XJu4h1WbE-ftTmMMlWjhCK0KFQcPql00oh_EzjxQJ6HC4Uku4slpWs5OWMiYdyNz-xOhCoXAlOuZ-xkeKjvC_UJ5YQ9UJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6bfc600a.mp4?token=o9aT-JXojQkLlPUmGfh94VTz2ZI00odVSVIydgPULIGnFm79vgjh2cr3IaSlRglJNOQrExoW2KysLts2SauzN4pMg2TJSpkIQtOp_Kh5SHVcVjk5ZNE3WEQFH914HTZGvif7awIYumlUY0h8IXoMLMEFftjgPrOhkQalbppwIUIkkyKsZ_yrGHstFFm8gzo0v3K4ZMIkw2JmDYQkbqH1Q2vou2xcLBioxJMWnXpMpBINWYOH6W80Vx7XJu4h1WbE-ftTmMMlWjhCK0KFQcPql00oh_EzjxQJ6HC4Uku4slpWs5OWMiYdyNz-xOhCoXAlOuZ-xkeKjvC_UJ5YQ9UJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال تحصیلی جدید دانشجویان آغاز شد
@Farsna</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/462971" target="_blank">📅 14:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBUizdV3XFNDc-AMzKA2jKOiLyXfCFebc25ceADaqryjSQSFqfkpv342draSKRgAIeQGHP14nwUPafVYiVMvir8UfsupqqH-NYnANed9RBc1Iboy7ohvL27WmHWncpTaepUoZ_VlQHLJc9fwsp6NG35HxZtm9TDJqa42ZsetJtXMvKLOVwE7vnfoADbwQh9353YwvY-OWPd7yIRUs8ZTvigTY8yqV6MKuPLPw18OGe7ceUSHQ14zNMui8iJuvwV1WWIuqLwiqaOUtvvTySfEjPgYAnwrqguw6pXG-83VEuZXu4UcyEBSlFAQIq4tsHLB1D570nUQXSowHrFOkzcmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWwe8gzQVvYYCmyxpl_L5Z9hYtAAVs-V5hLXC-M4yiGT84FXFyLVSsBFOmvip9zIM_Ddz2Scw0-XIJtYZ-TqtABzIjA-u7BYrO7Lk1cUqvpDxgnNdIs269uFNIawNtzqEhX4MAglT8Dwa-FbSihTNm4uo3Kc4a9N1KUflWUJZBU_wPRFggUH3CV1o5ZdRQvD_nQZb6FgMz_xckO70_Pwgu7SNY2AQICTg0SMG5Wixup25VnDFkZlYAQxCq9Af62DC8CRqsBD_SLKcK7R0yuUB0nHDQvaigSE_KrP7GU4doc57nseXyVN3kJ5VUdWNugeUbphYRU9-vI5rDjDZqRCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWL78tYpNJuJiFfTVxe2GkDogmXqt2KlRWq7HilTTNilM4OpdvMGtFYVJHP1LE6tUeYVM6AujKxkrNsbhAntICNPIZsY7CAsfDlcY8xRZmFh8di6tNfZoZ0sjnxSENZPy_xQQu3DebOVrveg1-RBQxtiVh81gDKr1YNVstE1EXb15HcxJa4OXeMaMgGTnF0y3KpiNO_AlGDbP7ZAu3XnM08l0FfhGiutnSh30u3wNosqZU-nU1d2iKZm_b-T0UFC6TCqe4wLQdAM4hrS6aM1E15BbHaVYjn12dD3T9NR6uaGqq2Py3EoZrno6jztPTCH8EqdWF7IGCkp5LPVFYuOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBi02-UllATIjl13w-CJfyiu2RHfiQh23H7vl8l1kvvKk-wSVjYDvCZf9yImD62LH-I8IbFt5k1yVmt671NarnTJkRJxE7Bb2h6RbGasj51IHYRYhfS-IiGzj5XExNced2j0LjyMLHYSbdTVHZsvDBITAo0eJyQHQpr-xGbX6OzwGy91Fsc8bMLvirC26xd7fX0nOi0n7pkO2srIgljIjffiGIe1r6-I7e4oPhtU-7TdmPgppPLcKHE4iFWBt8NhrqY94ZR4xUOl8YNhZehgL3WpH5WTkans1xh29_7ucQ9PXZDhPSblTFCalxG9wb4RkFSOo1hpSbK4FlP4R3FRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNLWYz0cCkHyBXD9hfFeA1Y3-Pfo26aJRwMlJJcsFmm2vLQkKqYjEDUDYRnRon_UCjowgj09RCMJM9eSCLLCEemYM1JwbLyIhCjMEpJ0smiOQAqir2ir6A54T0fsd647FFBDkzHzrCrVDn1hyWt5jFSGvQoVn_QymVAbdaRqMEZd4S5gp_TGbb4OV_sqc1PdKm3SXAKgUQAU-FDuQ3fZetJtpQyP3hsDalGec4gNoDrKb7cz48fgJcq6T6rnYlIdAUYH60E5Sb7Zry_rQILAZqkGVPfFEEYFGu_JWlZMO3RcvjgsrgqOGEKmtEVYmBbjECr2bvFHILKhK9h7zXz2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxEgr6GX9XNYB7sbuHyEP-H6TVS3v7mdeCJUgkuFmlf5_FnStLWr9sbdZzWe0ceCrwrsX-2KcfViXECaxsuXbroo5B7GXjXKFZjAtKkiZFs3uFKzMymx9f7WVUZMQY1vUQ7u2zFeXYFTF-5eJKgwg3qZ29wV1qL4rZgcYrr_41AFYCCc6aLjgIvQEgQhVEBu92E6y6ctofDfklbtcW5SW9uW1g-HMI5I_cu--135WXzdu2098TFfL1BohsvMR57ED3ZCwIddBrFDkG24g9Y4DDeqXDgQnz0SqHaY65fVnLCDpR89XSJwFY4hpCAW-iQrICasoQTk2Jz4WaHx2nohvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
صحبت‌های جالب در مورد معرفی کاروان ایران توسط سخنگوی ورزشگاه
🔹
دائم گوش می‌دهم ببینم دیگر کشورها را مانند ایران معرفی می‌کند یا نه! گویندۀ ژاپنی کلا سکوت کرده.
🔹
بالاخره احتیاج به نفت دارند؛ اقتصاد را هیچ‌وقت دست‌کم نگیر.  @Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/462965" target="_blank">📅 13:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2a09ef29.mp4?token=U8_1b5f9-dwROFYayiFiJCgAAdHUSpkpttEupIkPC4Tox1uOeRv9SxNbvnq0epmiAcBmL_WukD1RGlnLVrwFS-JUf8_CX-Eb2QdOVNH1fq-1nn1nlPuGXLso-sVyS2PeJLb9cT8TlTPteKF0hkaExnGo7UcHzEs_aUG-6O295Bq5HhgLzc_3vgLH1L68OOzYYGhHjJnYvGht35nrtPBZroqymmi42UeUIILN6RcFV8LD6M7AvL70aM9VU7yttG45eMjB45207BBDdAlkW6c-Ne7mtDX3hvUesILvlWFImfYPA5wmcaoVSDEgCKL2FUnpwKsPL3w9Ph7j_lXSSknkFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2a09ef29.mp4?token=U8_1b5f9-dwROFYayiFiJCgAAdHUSpkpttEupIkPC4Tox1uOeRv9SxNbvnq0epmiAcBmL_WukD1RGlnLVrwFS-JUf8_CX-Eb2QdOVNH1fq-1nn1nlPuGXLso-sVyS2PeJLb9cT8TlTPteKF0hkaExnGo7UcHzEs_aUG-6O295Bq5HhgLzc_3vgLH1L68OOzYYGhHjJnYvGht35nrtPBZroqymmi42UeUIILN6RcFV8LD6M7AvL70aM9VU7yttG45eMjB45207BBDdAlkW6c-Ne7mtDX3hvUesILvlWFImfYPA5wmcaoVSDEgCKL2FUnpwKsPL3w9Ph7j_lXSSknkFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار کارگر: تجهیزات باقی‌مانده از حملۀ ناموفق آمریکا در دشت مهیار اصفهان در موزه‌های بنیاد دفاع مقدس به نمایش گذاشته می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/462964" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGRscFzC61SUUpqKVOslJ5ddtfUqt6jglPlHSYdhYC6m_aIbcXCTs9LcjkbhZAL_5COEOhu5KAEtl25NAj5kfwG2t_UrSLpVd-yadxcneZR30F1EAoKcEuAoGIyxRlireplGoVEM2PTWxMDCkpFZl5fCM4Fjg7Csxrvf0UzgaLIyTiVtDx_wtj_d59yCJCNSYxW0V4lHusAtHXIrPRc57HUOVu_sgKZgQ8TFeh8-lRo_tU-Lt3Mdk-uhH8K63A8SrjETeObBXJa7gvoRB7FxWqu6BUGTZVMouQd5lEMW1suPItZu3Mesf_GD-ICka3_QiA1kJM_QB1RwgfmjiSsTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست یاری پلتفرم‌ها به سمت رئیس جمهور برای فرار از نظارت
🔹
پلتفرم‌ها در نامه‌ای به رئیس‌جمهور، با انتقاد از نظارت ساترا و آنچه «نظارت بی‌ضابطه» می‌خوانند، خواستار انتقال مسئولیت تنظیم‌گری شبکه نمایش خانگی از ساترا به وزارت ارشاد شده‌اند؛ وزارتخانه‌ای که خود به‌نوعی ذی‌نفع این حوزه است و رئیس ساترا نیز پیش‌تر از «ترک فعل» این وزارتخانه سخن گفته است.
🔹
روابط مثلثی، کپی‌برداری از آثار ترکیه‌ای، رقص، مشروب‌خواری، روابط آزاد، کمرنگ‌شدن قاعده ازدواج و چیدن مسیر دوستی، نمایش خانواده‌هایی با بنیان خیانت، خیانت مرد به زن و اخیراً زن به مرد و... همه اینها بخشی از محصولاتی است که شبکه نمایش خانگی در سال‌های اخیر به مخاطب عرضه کرده است.
🔹
حالا نامه‌ای با امضای نماوا، فیلیمو، فیلم‌نت و... خطاب به رئیس‌جمهور منتشر شده که در آن، این پلتفرم‌ها خواستار بازگشت تنظیم‌گری شبکه نمایش خانگی به وزارت ارشاد شده‌اند؛ همان وزارتخانه‌ای که بنا بر اظهارات جواد رمضان‌نژاد، رئیس سازمان ساترا، در این حوزه «ترک فعل» داشته است.
@Farsnart
_
link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/462963" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f11843d50.mp4?token=JQaiLnPZUXo8pyNTEb6tIwYLpDlJDjaLCyeZ3BingrhJef0JfgAUCfkOclKNJodTd7S6uqaHFH-AWpO10YGio6Op8uOupFibKGUfA5upNZVDiHfv1YOif4ptuOl2Eq5I5o0KPIT3V6yMGx9chZZAMDB2hHgKMowRWjBL_mkc-V3ggGc045_Cjz_40HfUcw1uYeacrmAXAzl02MLV4uMvt1FfGsTVIO8dAygp2smdG59wJWg5zdwwSVkpcpXxqWxguy3E8ihf2viU0-AcMQA0JmJ-l2D_Pn_HDyKb9E-fvtfeaRl35nAJVJVPdNSHFDU87qL1aDGptq1j_plBWjX5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f11843d50.mp4?token=JQaiLnPZUXo8pyNTEb6tIwYLpDlJDjaLCyeZ3BingrhJef0JfgAUCfkOclKNJodTd7S6uqaHFH-AWpO10YGio6Op8uOupFibKGUfA5upNZVDiHfv1YOif4ptuOl2Eq5I5o0KPIT3V6yMGx9chZZAMDB2hHgKMowRWjBL_mkc-V3ggGc045_Cjz_40HfUcw1uYeacrmAXAzl02MLV4uMvt1FfGsTVIO8dAygp2smdG59wJWg5zdwwSVkpcpXxqWxguy3E8ihf2viU0-AcMQA0JmJ-l2D_Pn_HDyKb9E-fvtfeaRl35nAJVJVPdNSHFDU87qL1aDGptq1j_plBWjX5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ کاروان میناب ۱۶۸ ایران در افتتاحیۀ بازی‌های آسیایی ناگویا  @Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/462962" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4XXXXSCES6zAPt5uD94EXTtob7jHFx1DANKJQP1KCggDO5-PSAlH7p6fc9xun00CI0Xp0nyGM5Cr744ReGPibpQ2mp75PAkiq9tGOdOWiGk-48IJUsKnw0Jf3l_5KzEw3Ce7v11LlERms0Qe7JdNnv2p98BtgrSzQmxT1aylRGd6bfQjhWbMl2nKIDp7jENxJq1bCvOZ-vuWhParJ_WYneg-zIpY0WHS-4APijVzme3TJkS6rtzMZVENj7iQtSC5WQT5Y4vC2RdCEMrWXspiHq_hRULPAXLXTigyws6ZTmb2ckCoe7ywGzKYK6SogfEF14Xvm-djrwEIITLmTRo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره‌شمالی در واکنش به آژانس انرژی اتمی: ما یک قدرت اتمی برگشت‌ناپذیر هستیم!
🔹
وزارت خارجهٔ کره‌شمالی در واکنش به قطعنامهٔ آژانس بین‌المللی انرژی اتمی که از برنامهٔ تسلیحات اتمی پیونگ‌یانگ انتقاد کرده، اعلام کرد: جایگاه کره‌شمالی به‌‌عنوان یک قدرت اتمی «برگشت‌ناپذیر» است و این جایگاه به‌پشتوانهٔ بازدارندگی هسته‌ای حفظ خواهد شد.
🔹
همچنین خواهر رهبر کره‌شمالی در بیانیه‌ای آژانس بین‌المللی انرژی اتمی را به داشتن «استانداردهای دوگانه» متهم و اعلام کرد: دیدگاه جانبدارانه و استانداردهای دوگانهٔ آژانس بین‌المللی انرژی اتمی، عامل اساسی فروپاشی نظام بین‌المللی منع اشاعهٔ هسته‌ای است.
🔹
در بیانیهٔ کیم یو جونگ آمده: آژانس بین‌المللی انرژی اتمی در برابر فعالیت‌های آشکار اشاعهٔ هسته‌ای آمریکا و طرح کره‌جنوبی برای واردکردن زیردریایی هسته‌ای چشم‌پوشی کرده، اما در مقابل، قطعنامه‌ای را علیه فعالیت‌های هسته‌ای دفاعی و مشروع کره‌شمالی به‌طور اجباری به تصویب رسانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/462961" target="_blank">📅 13:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8aa05441.mp4?token=Eprs0xv-mr7m3_KEsJVYW_AEUm_-v9F5Y7tSSNR2JhIfA-ZmmstHePXSC2xE88fAtD4yeg2ToFvM3VBSk4rtmx4A8IYQGNlxmlDxP237326hSYmZnj_vdndsQA1IHHOoGiam4vBXUBA_v2C_fCZNWtnjM2NC5oYJcXer7Ocd_L34UnrNm06kPwYc-TmXX9ukEGRqH5BuEi575fobZI_lQrOsT5mxSvhELh7Ta2lMpk9g8WR0J3IXtc4PSomcsdg37qgsYnNWq4PmCiDA7g86V2gi-Sm6ckkYdvTcPkqV9rvjlSZponbNhCqMPvqpiQti7wjgCPyPBp7WvGLYVOK5sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8aa05441.mp4?token=Eprs0xv-mr7m3_KEsJVYW_AEUm_-v9F5Y7tSSNR2JhIfA-ZmmstHePXSC2xE88fAtD4yeg2ToFvM3VBSk4rtmx4A8IYQGNlxmlDxP237326hSYmZnj_vdndsQA1IHHOoGiam4vBXUBA_v2C_fCZNWtnjM2NC5oYJcXer7Ocd_L34UnrNm06kPwYc-TmXX9ukEGRqH5BuEi575fobZI_lQrOsT5mxSvhELh7Ta2lMpk9g8WR0J3IXtc4PSomcsdg37qgsYnNWq4PmCiDA7g86V2gi-Sm6ckkYdvTcPkqV9rvjlSZponbNhCqMPvqpiQti7wjgCPyPBp7WvGLYVOK5sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیگنال تازه در نقشه‌های بارانی ایران
🔹
نقشه‌های هواشناسی امروز نشان می‌دهد شمال، شمال‌شرق و ارتفاعات کشور همچنان مستعد ناپایداری و رگبارهای محلی هستند، درحالی‌که مرکز، جنوب و جنوب‌غرب بیشتر تحت تأثیر هوای گرم و پایدار قرار دارند.
🔹
در شمال‌غرب، سواحل خزر و…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/462960" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3445e3d598.mp4?token=OFOtdrfJcJRJz_rlxHW0mjhzTv0lgjVFw2pokIKcrum0fbNEGcTuMXsQ8cwuSSBrWJkrM-L9YJk6weSZYjqSrQqoGcqgbS4HYzh9StilBtVI2Q8g8HonHI8IoV5cGlPkmCYC0_Urtam-qi7-jh4yACZYT-2O4pb4oHqLakNBzW6tt8Ps9x7TDMWv6_bZ41jXDdKuY9cucdu6BVcKNvERDVXmnrVhIiziKuQfjqvN4Jfrw3QfBiHyBc746s5-uam72hm8RXr2UpO0KSzhaF2fW1EIwcBwAoB3g-3G-oUgXHo5qcX3rgyu_SAjEqZ5BSogi8x7tMPe-cuD-QRvqwMKcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3445e3d598.mp4?token=OFOtdrfJcJRJz_rlxHW0mjhzTv0lgjVFw2pokIKcrum0fbNEGcTuMXsQ8cwuSSBrWJkrM-L9YJk6weSZYjqSrQqoGcqgbS4HYzh9StilBtVI2Q8g8HonHI8IoV5cGlPkmCYC0_Urtam-qi7-jh4yACZYT-2O4pb4oHqLakNBzW6tt8Ps9x7TDMWv6_bZ41jXDdKuY9cucdu6BVcKNvERDVXmnrVhIiziKuQfjqvN4Jfrw3QfBiHyBc746s5-uam72hm8RXr2UpO0KSzhaF2fW1EIwcBwAoB3g-3G-oUgXHo5qcX3rgyu_SAjEqZ5BSogi8x7tMPe-cuD-QRvqwMKcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم افتتاحیۀ بازی‌های آسیایی ۲۰۲۶ در ورزشگاه میزوهو شهر ناگوی ژاپن  @Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/462959" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبا فولاد خلیج فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kavy3C4JcXGqRyt5V-O2KzE3cweHofBhjKhFeOj5uWtU2om5OHRY2-kPl6gxpy4O-XNK-qYMkdg5f7vP050opcqKtfd_8QQneWeaPmyZwgSmZ4wOSpC938fVxcUSC6J49we5UI1xSUF36e1obaS04_0JbuyXocB4m4uiRADDtbgi0ID7CBmynAbUL7FjWSRweamvqIrg8neIMQVtvEd21wjIih_rItEDP_P8_cyUcc1tf16xM0VVzjAoILbY82-jtUN3SiLV4cv5lJG4tLKgEYC-r-KaCM0mY7DsxoAehp-X2sBa6RahYhvvxtZvLR0iZM1nukUDAg4Pl6bLgbSWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خون تازه در رگ‌های سهامداران صبافولاد خلیج‌فارس
صبا فولاد خلیج فارس در پنج‌ماهه ۱۴۰۵ با جهش فروش داخلی و بین‌المللی، افزایش درآمد و رشد شاخص‌های بورسی، تصویری متفاوت از عملکرد خود ارائه کرده؛ روندی که برای سهامداران، نشانه‌هایی از بازگشت رونق است.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/462958" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPkQ1vVdlecu4zGLwsnVqlCKvBsoTq7StBdWmMp6kMjcIubqizDBoalBG7ZHVB6mr9X31GAfVtRbPJ7afxNqy6UF8GGAYk6F0lrAozGheXAnenYNpCBmqbq-cNxt7FY-rnuyxJ30EkVdLwiCjdFUohCcRddrapBtss9qCKSddAno9K18ZweXy0qxnIEuBi1DgpBLCiSMJnWuIwJCtx-qDbSV_GZ28ghg-_iKOaqWGApvM2z8tbzJAHo_SRcdozwZdHZwaN7kgfIrM6U-2VF-COKQDf1ae9DShBCdxYJNF31Gagj6Xb7ypwavn3OC22gtjogsQmtvZ2DleCBlP8cY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/462957" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/462956" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786c37f584.mp4?token=eMcCe7TUN4u1vMbhpVHEJuQRXB6UeMAmNs8uJxaAGuOJ584LDdoOoBlL2QXNMNcF7eMwBTXfvpOhERI7CdNqh0AiOgs0_s36z3gnb_WQgqSsEdQBdR_Pb6rl1Pci8xgeqWSAnvjesBDdMO6zYhCJuJxFDUobdwZvDlhIiW1-WcGw1LGRy28zVC0-dj5o2eIaFVgEOO5SMIByxLXajDcsInA5XRyHcmaQSg6JPJL3lt5kOUvf9pUHHgCRF2z6eVMQJ_VapFztgTf_sNLaFkQe47JIRmzVGgQ-mMvvz4hY19_V4z4SfRW7Id1Oba7fi6wKhtfLN0rURuBJlIpXflsEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786c37f584.mp4?token=eMcCe7TUN4u1vMbhpVHEJuQRXB6UeMAmNs8uJxaAGuOJ584LDdoOoBlL2QXNMNcF7eMwBTXfvpOhERI7CdNqh0AiOgs0_s36z3gnb_WQgqSsEdQBdR_Pb6rl1Pci8xgeqWSAnvjesBDdMO6zYhCJuJxFDUobdwZvDlhIiW1-WcGw1LGRy28zVC0-dj5o2eIaFVgEOO5SMIByxLXajDcsInA5XRyHcmaQSg6JPJL3lt5kOUvf9pUHHgCRF2z6eVMQJ_VapFztgTf_sNLaFkQe47JIRmzVGgQ-mMvvz4hY19_V4z4SfRW7Id1Oba7fi6wKhtfLN0rURuBJlIpXflsEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم افتتاحیۀ بازی‌های آسیایی ۲۰۲۶ در ورزشگاه میزوهو شهر ناگوی ژاپن
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/462954" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjSCHkuTgKHXH2LUIkCVeTw6s6pBBx_EeXbjRPuKkYhnnA2o5mB5hr7mRpU2jcU5OMwJU_efaD_WdV6jSoBIkZuWU3G27b37O49Fj77dh_vkGhAJypnYr9bcfVUauQgA5vZfNNKzfGkfUZtVOY1ydAGTk-S5hkJ6Zqzxr7f6oYF7n0wuLbmAIt-irjVPQxUS1ojlrIuLtZlpOLTxzrlAs4qGw6AtwDut8Ot65yUYHmC2oplNCu6Bw7RHfUGI34ClQBQ_mLdIOF_KWBVA34aWYaujGF6hisXq1ihhCLapXOXoLlii0lmQo8lf1lCAXDYR_GOSsJ0xKaSw6nqauQPAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش بورس به زیر ۷.۵ میلیون
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۹ هزار واحدی به ۷ میلیون و ۴۴۹ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/462951" target="_blank">📅 12:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آیت‌الله سیدموسی شبیری زنجانی به‌دلیل عارضۀ خونریزی معده در بخش مراقبت‌های ویژۀ بیمارستان بستری شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/462950" target="_blank">📅 12:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNFsaCXz3yimVGDpfQvUbLHXQpetPE5CbTBNYZdk6T9I0PVoOvBiswRQaulAIqS6RJtgfeCWQ2nTLgAnilHcqNfWTRh3pJMgZZ0wUoxednvHAIpH60iqlvD5q-jxRW7PxzbixbKIew60X8uwN8IcMk9n6EQTKZQiiE8JWxK89Q9Pr5FUVGdMMC6LsL9QDCKqJ_QY2WOnlvb4Jbwie3FaLZyLNzd1JMYnE5Fojwv1w_LrVT4ojzULOO7gCd4_5hK1CDU0vzVAjb9o1hVCUg3iOIq0DtkEivx7aAuIs72L-HG-Grf5xyjbJZ-7eDDAbMKfWsvNMW464ZwcM_ARg_J4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز دور جدید ثبت‌نام عتبات
🔹
ثبت‌نام دور جدید عتبات از امروز برای اعزام تا نیمۀ مهر باز شد و زائران می‌توانند بسته‌های کمتر از یک هفته، یک‌هفته‌ای و بیشتر را انتخاب کنند و زمینی یا هوایی راهی کربلا شوند.
🔹
با وجود احتمال افزایش هزینۀ سفر عتبات در پی نوسان نرخ ارز، زائران تا نیمۀ مهر می‌توانند با همان نرخ قبلی راهی کربلا شوند.
🔹
دور قبلی متوسط هزینۀ سفر زمینی ۳۰ میلیون و هوایی نیز حدود ۶۰ میلیون تومان بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/462949" target="_blank">📅 12:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نفت فیزیکی ۱۳۰ دلار شد
🔹
اطلاعات رسیده به فارس از یکی صادرکنندگان فرآورده‌های نفتی حاکی از آن است که با ادامۀ اختلال در تردد نفتکش‌ها در منطقه و کاهش شدید جریان نفت از تنگۀ هرمز، قیمت نفت فیزیکی اکنون به بالای ۱۳۰ دلار در هر بشکه رسیده است.
🔹
انتظار تورمی در بازار محصولات پتروشیمی که پیش‌تر با کاهش واردات نفت چین مطرح شده بود، تا ماه گذشته با کاهش ۲ تا ۳ میلیون بشکه‌ای واردات نفت این کشور تقویت شده است؛ به‌طوری‌که واردات نفت چین از ۱۱.۴ میلیون بشکه به حدود ۸ تا ۸.۵ میلیون بشکه در روز رسید.
🔹
همچنین براساس این اطلاعات، جریان نفت عبوری از تنگه هرمز از میانگین ۲۱.۶ میلیون بشکه در روز در پایان سال ۲۰۲۵ به حدود ۴.۹ میلیون بشکه در روز در سه‌ماهه دوم ۲۰۲۶ رسیده که به معنای کاهش حدود ۷۷ درصدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462948" target="_blank">📅 12:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjBNeVnez6lYeVKmF9ikW69Sth1oDixkMHnX9V5QgyHwSswZijpJOl2Medx4v9ai7sVcZc7LOzFZWcqkfa2hm6wHWhrNyzfvIau3dsIi9RZ-mbANlO9bcmpeRh76Bu6Jc3bREc-cSselfwY2l8GvvejUPYQb1ONgJ2IK6nYG3loXWcKQ6OUBzlm_FkaBa2G_ozt6K2iY2p83JXGG7F54wec81Xn1Bi9-yHVwQ3_l7shTmaVHHUoNl7vLUGzzm_uG6x-6J0_-GIpIixs_ebUz3p4_PXuBCFGrRJm9IcLAYW5FpIyIgcBn63hJ3ZDVDbFMkIIyrcHLZQBnRxHADvzmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیگنال تازه در نقشه‌های بارانی ایران
🔹
نقشه‌های هواشناسی امروز نشان می‌دهد شمال، شمال‌شرق و ارتفاعات کشور همچنان مستعد ناپایداری و رگبارهای محلی هستند، درحالی‌که مرکز، جنوب و جنوب‌غرب بیشتر تحت تأثیر هوای گرم و پایدار قرار دارند.
🔹
در شمال‌غرب، سواحل خزر و دامنه‌های البرز، رطوبت و شرایط همرفتی می‌تواند باعث افزایش ابر، رگبار و رعدوبرق محلی شود. این بارش‌ها بیشتر نقطه‌ای هستند و لزوماً تمام استان را درگیر نمی‌کنند.
🔹
در شمال‌شرق نیز ارتفاعات خراسان‌شمالی و رضوی و در جنوب‌شرق، بخش‌هایی از جنوب کرمان، شرق هرمزگان و سیستان‌وبلوچستان مستعد رگبار و رعدوبرق محلی در ساعات بعدازظهر و اوایل شب هستند.
🔹
در مقابل اصفهان، یزد، قم، سمنان، فارس، بوشهر و خوزستان همچنان هوای گرم و خشک خواهند داشت و در مناطق بیابانی احتمال گردوخاک وجود دارد. تهران نیز عمدتاً پایدار است، هرچند ارتفاعات البرز می‌تواند با افزایش ابر و ناپایداری محلی همراه باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/462947" target="_blank">📅 12:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/462944" target="_blank">📅 12:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c05b437b.mp4?token=p8S9VKoxfL-h3dG9ohBBoMAc9J2h95aUfC6jWQx3MincNqDxx0UmklU1EE80VDEtDlPoBuQOnYfNsLSEq_52iBY4cXmDtm5lDWV-7VvTyQOGFnk2Rm1uwS11ZSeS9K8TGuNJeg6pEEG3-A-HyQTcWqaGp_cZOCpq-g7WRSPn_gVKfSqdpwPPxUGyKZYypwoNd7jHJdIGmYg7i2oaiAfz89HNkT1CKXu_kIzV2YpNUsMBhifkN77OGhSP9Q3PLxSzSYisEJ1y393oxrSrTElqgHIxCWz31P_cAJ9NOZnND3Kt_ipaXbyhDl6a5wNImsGEI7AsaK_HplW9BNOA7XvHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c05b437b.mp4?token=p8S9VKoxfL-h3dG9ohBBoMAc9J2h95aUfC6jWQx3MincNqDxx0UmklU1EE80VDEtDlPoBuQOnYfNsLSEq_52iBY4cXmDtm5lDWV-7VvTyQOGFnk2Rm1uwS11ZSeS9K8TGuNJeg6pEEG3-A-HyQTcWqaGp_cZOCpq-g7WRSPn_gVKfSqdpwPPxUGyKZYypwoNd7jHJdIGmYg7i2oaiAfz89HNkT1CKXu_kIzV2YpNUsMBhifkN77OGhSP9Q3PLxSzSYisEJ1y393oxrSrTElqgHIxCWz31P_cAJ9NOZnND3Kt_ipaXbyhDl6a5wNImsGEI7AsaK_HplW9BNOA7XvHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ صدور کیفرخواست در پروندهٔ شهادت رهبر انقلاب و اعضای خانوادهٔ ایشان و اقدام تروریستی منتهی به شهادت دانش‌آموزان مدرسهٔ میناب
🔹
دادستان تهران: کیفرخواست پروندهٔ اقدام تروریستی منتهی به شهادت رهبر انقلاب و ۴ نفر از اعضای خانوادهٔ ایشان با تکمیل تحقیقات مقدماتی…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/462943" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پشت صف‌های بلیت قطار چه خبر است؟
🔹
پیش‌فروش بلیت قطارهای یکم تا سی‌ام مهرماه از امروز آغاز شد و بلیت مسیرهای مختلف از طریق اینترنت و مراکز مجاز فروش عرضه می‌شود.
🔹
مدیرعامل راه‌آهن گفته برای پاسخ‌گویی به تقاضای موجود، سالانه به ورود ۳۰۰ واگن مسافری نیاز است و تا پایان برنامۀ هفتم باید حدود ۱۲۰۰ واگن به ناوگان اضافه شود.
🔹
در مسیر تهران–مشهد نیز با وجود فعالیت ۸۲ رام قطار، ظرفیت این محور به سقف خود نزدیک شده است. راه‌آهن برای تأمین فوری ۳۰۰ واگن مسافری از محل تهاتر نفت مجوز گرفته است.
🔹
از سوی دیگر ضریب آماده‌به‌کاری لکوموتیوها حدود ۵۰ درصد است و افزایش هزینه‌ها نیز فشار بیشتری به شرکت‌های ریلی وارد کرده؛ نرخ بلیت قطارهای مسافری از ۱۷ خرداد ۲۱ درصد افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/462942" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZWKGmHiepXlHLp6wBEzMuMaACf8Owyop-Ks-UqdkUu18KOU1SMHShxw4UYXuSRSVbCjLmkfbrRPOTsoII6NHVEKFtXcmZBxxG9Xzi7E85hBjhlNOQkfiPz7kJrZCLCPIiDjYuWNLdHIMPO6aRz-fVjTdHVlPfyyjdDXutA3zySU9vQrutVg6_hUNFKaEMgMuZy_328unIR2QNEjE_QZFwERyVuLNbyqMo8xLp6Vs6zCHzorF0Wg27RhNhgdIFo__VW9jSjlKGrS_DwvDoGiXvfei3_zjJaE9seJIs5KKwO9fPoQ1CjExNoy7Omlq9Y93V0_uF6BLPvxOoOKIbK1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام جرم
دادستانی علیه عوامل برگزاری دوی ماراتن تهران
🔹
درپی برگزاری مسابقۀ دو ماراتن در بوستان ولایت که در آن موازین قانونی و شرعی رعایت نشده بود، دادستانی تهران علیه عوامل و دست‌اندرکاران برگزاری این رقابت اعلام جرم کرد و برای آن‌ها پروندۀ قضایی تشکیل داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/462941" target="_blank">📅 11:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a2334d95.mp4?token=eRKL0KAexQsxXcYt5ncdxPrmy8Ptr1my__HejvbKBWLEwERY_iBYJKuRuYQcNnvCQRdlogVuCfkLmT9oxtHdmK2RJFCbLFFlWImQaCJg6hEg7_sPCdca9bvDrFW6wTymjldttgCjk9nZrm1Q48P-InyantdqmKJBWvuLSjCbIoFRPvuwLBn4xa_839ZRqgEf54IK6aHoK0Io31pI-9fJc92VT11mvaCttxxER6WUAVpFrmbXSGVXmpQzcDctn3MSY8Z8yESYDM-89nMNdBkAckiaY36nhvRc9eNx6lGHNZL9MaRKC6Cyh2VB5FvAsULjdWAcf6kwtY-D_Oj-5ToOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a2334d95.mp4?token=eRKL0KAexQsxXcYt5ncdxPrmy8Ptr1my__HejvbKBWLEwERY_iBYJKuRuYQcNnvCQRdlogVuCfkLmT9oxtHdmK2RJFCbLFFlWImQaCJg6hEg7_sPCdca9bvDrFW6wTymjldttgCjk9nZrm1Q48P-InyantdqmKJBWvuLSjCbIoFRPvuwLBn4xa_839ZRqgEf54IK6aHoK0Io31pI-9fJc92VT11mvaCttxxER6WUAVpFrmbXSGVXmpQzcDctn3MSY8Z8yESYDM-89nMNdBkAckiaY36nhvRc9eNx6lGHNZL9MaRKC6Cyh2VB5FvAsULjdWAcf6kwtY-D_Oj-5ToOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی شورای نگهبان: انتخابات شوراها به‌صورت تمام الکترونیک برگزار می‌شود
🔹
زمان برگزاری انتخابات شوراها در اختیار شورای‌عالی امنیت ملی است.  @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/462940" target="_blank">📅 11:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ee14176c.mp4?token=iAURAhaQ6TXx6sfiUB92B-U6N3evcoeT9ra1fBzOIeObfeC2fSqucvdOrn6iDaL7jt6U26CqOVzx91kenWZN86-B3_pi34ighM3DbqZ-sN9QA_xpKl3v6b4MxmcUtYIl2feEx6725UQj99RzTRXlhcyYUQ1yaQUobVHTn86zXDJp7sjZ3kwCsWDpmAz-Uya_bA1enhudqhxb5oTPEcwchHVZBEVzjsGg8d3nGamWn0hDmk-ALq9lnAyqdRHCRiS51ofC-bED069meVqS837umoYTNPx4EWy1fNzbhQjCbi_xGbPEYliEp39HHN3_4t3NhwvkRgnkcklZjhI4-21mjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ee14176c.mp4?token=iAURAhaQ6TXx6sfiUB92B-U6N3evcoeT9ra1fBzOIeObfeC2fSqucvdOrn6iDaL7jt6U26CqOVzx91kenWZN86-B3_pi34ighM3DbqZ-sN9QA_xpKl3v6b4MxmcUtYIl2feEx6725UQj99RzTRXlhcyYUQ1yaQUobVHTn86zXDJp7sjZ3kwCsWDpmAz-Uya_bA1enhudqhxb5oTPEcwchHVZBEVzjsGg8d3nGamWn0hDmk-ALq9lnAyqdRHCRiS51ofC-bED069meVqS837umoYTNPx4EWy1fNzbhQjCbi_xGbPEYliEp39HHN3_4t3NhwvkRgnkcklZjhI4-21mjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: احتمال دارد انتخابات ریاست‌جمهوری و مجلس به‌صورت همزمان اردیبهشت ۱۴۰۷ برگزار شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/462939" target="_blank">📅 11:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d442ae694.mp4?token=a0RuWXtmZkaN045mC0Up2NP3lyk2aGJS2ib6FFObGpvG1oXyIIACzMNr_EGLXFiLydzDYFdA8dk5p1Nzi7yLWI_bJbo8MkBVvVl_DIriVCcKDKd1rHM030sd9elZgTPFl06W45hwPalDeamIc20aS8twF17-6bOOId19Y1qD6AJl4-n7EjpjVmuVWrlaFLqn3lxFEOQM1Z2X-DD_EW9Q3NOEqKHeI3GfwSIFhhrC22SBd83knizyAwpHNpNKJncS3_3Ee0afdOtZb48_MJ5jj-mk9jbIRGiSZOukRGIpayzt_qv0r3UjTBHllLq2JheyKSWtNFurmw77jz0ns4lWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d442ae694.mp4?token=a0RuWXtmZkaN045mC0Up2NP3lyk2aGJS2ib6FFObGpvG1oXyIIACzMNr_EGLXFiLydzDYFdA8dk5p1Nzi7yLWI_bJbo8MkBVvVl_DIriVCcKDKd1rHM030sd9elZgTPFl06W45hwPalDeamIc20aS8twF17-6bOOId19Y1qD6AJl4-n7EjpjVmuVWrlaFLqn3lxFEOQM1Z2X-DD_EW9Q3NOEqKHeI3GfwSIFhhrC22SBd83knizyAwpHNpNKJncS3_3Ee0afdOtZb48_MJ5jj-mk9jbIRGiSZOukRGIpayzt_qv0r3UjTBHllLq2JheyKSWtNFurmw77jz0ns4lWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: ۴میلیون و ۵۶۳ هزار و ۱۱۸ نفر اتباع خارجی شناسایی شده‌اند
🔹
۳۵۲.۶۳۶ نفر از اتباع امسال به کشورشان بازگردانده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/462938" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">لغو مجوز فعالیت یکی از شعب بانک ملت در ترکیه
🔹
روزنامه رسمی ترکیه اعلام کرد مجوز فعالیت یک شعبه بانک ملت در استانبول لغو شده است. نهاد ناظر بانکی ترکیه دلیل این تصمیم را اعلام نکرده است.
🔹
بانک ملت چندین دهه در ترکیه فعالیت دارد و دارای ۳ شعبه در استانبول، آنکارا و ازمیر است.
اما آیا این موضوع سابقه دارد؟
🔸
بانک ملت پیش‌تر نیز با محدودیت‌های مشابهی در انگلیس و اتحادیه اروپا مواجه شده بود که موفق به رفع آن‌ها شد.
🔸
خزانه‌داری انگلیس در سال ۲۰۰۹ محدودیت‌هایی علیه مراودات مالی با این بانک وضع کرد که در سال ۲۰۱۳ با حکم دیوان عالی بریتانیا لغو شد.
🔸
اتحادیه اروپا نیز در سال ۲۰۱۰ دارایی‌های بانک ملت را مسدود کرده بود، اما دادگاه عمومی اتحادیه اروپا در سال ۲۰۱۳ نام این بانک را از فهرست تحریم‌ها خارج کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462937" target="_blank">📅 11:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9b1fb122.mp4?token=nYeUtJ3XmHbnsKFe-5hMViExMQTIuckk4Am0_3glCyvhFDxfxf1vGHJaCuTihhmupLmkEDo9uncbKW6nzODJeuzetj46p_zcKjN3y8SMhJmvNk3AtnwLpPK7MXN7xDx1rFgnia-3iTYVS9ceKGktn9-yeC_Op-ZFD62rOW7LweIq6_7-eC19Wmd1iW8SaPysLcmg5xeBoHApiRRUG0b70bJCdvCAbspS-6maYWaYMAVydjQZ_GmZWeXq1Yrv3urPSc-xJnvXEpPs_4kPgcB9iv2okgQ6wCUnm2vMh9zbDBB8y0uMliwLCSKkqxNsFvLZVGXMaLgjEDkL76kAWD3XsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9b1fb122.mp4?token=nYeUtJ3XmHbnsKFe-5hMViExMQTIuckk4Am0_3glCyvhFDxfxf1vGHJaCuTihhmupLmkEDo9uncbKW6nzODJeuzetj46p_zcKjN3y8SMhJmvNk3AtnwLpPK7MXN7xDx1rFgnia-3iTYVS9ceKGktn9-yeC_Op-ZFD62rOW7LweIq6_7-eC19Wmd1iW8SaPysLcmg5xeBoHApiRRUG0b70bJCdvCAbspS-6maYWaYMAVydjQZ_GmZWeXq1Yrv3urPSc-xJnvXEpPs_4kPgcB9iv2okgQ6wCUnm2vMh9zbDBB8y0uMliwLCSKkqxNsFvLZVGXMaLgjEDkL76kAWD3XsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران: تا ۸ مهر عملیات عمرانی حتی در معابر فرعی متوقف می‌شود
🔹
ممنوعیت تردد ناوگان باری به‌جز دارو از ساعت ۶ تا ۱۰ صبح مثل هر سال اعمال می‌شود. مجوز دورکاری اختیاری یک روز در هفته از اول تا ۸ مهر برای کارمندان به‌صورت اختیاری تصویب شده است.…</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/462936" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr772VgMp-BAJmSYRjmkGUBdOwmGTz-d9KmDjcZ63zKL7G6_bLnw17x2f5dxrWal9sPRlZaexCy23rULHtILkrnpcFaICKEmwRCLstq9QRynq-k09gIEgO4dy0I9yTegYQtBOxiF2rVik0_VbHEVSorRpzkIdHf2Jp_EJFD3Xfk_n076DAYpmvjEtadA_l8Z7ec3nj3fWbhYau9CcFlnvxEwlnFHf2Frl7KillLJb0VMe5a4if9ZIYhtRKA4dMXSE5vHy671oxsMYQSTYIqgWDXe0WNLFzcxas3kw05nXOUQo3Tzcg10JeCNXbS52sJwdM80tATUxIStbPK6bzXAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پرسپولیس ب» کنسل شد
⚽️
باشگاه پرسپولیس که قصد داشت با خرید سهم یکس از باشگاه‌های فرد البرز و بعثت کرمانشاه تیم دوم خود را در لیگ یک حاضر کند درنهایت موفق به خرید سهم باشگاهی در لیگ دسته اول نشد.
⚽️
به این ترتیب پروژه راه‌اندازی پرسپولیس ب در لیگ یک، دست‌کم…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/462935" target="_blank">📅 11:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcaQjlqXnbS2TREm9jFH0GX4QieOLVMS4834gMpL8VDOtGHhAPvWEhOkMrAsVO41TSMLAu156wEf5ovzoIzTLtU--EEPHWBElNPfwcRObBnMjwujd6-VRRnj5JqRbMRdQD12ieRXWfqSyFexL4QinXpIEB6sC0OVQ4HK6ePj2ywYOMLUUHiSTNJv1Eposc2W1apm20ZCmtBlB7T0W8I3s7Z99-2VrCQVtqcGzNUCT4HtHsNdRqRNqi40NlrpVCdtapJDMZ41opaID80RC1cFany7mS3tpNHIPXf_CXUHcAel-ju2WHK27o2VXsNUAeoGE-uiOmttH-nqkS1wR7gAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سیدموسی شبیری زنجانی به‌دلیل عارضۀ خونریزی معده در بخش مراقبت‌های ویژۀ بیمارستان بستری شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/462934" target="_blank">📅 11:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecf6MQ-eGGze4_XfdA7K_2lOI3vhyOA6ObYB1ZzubTxn_19lcuXks5eYdKmY48nIeFq6LArzkjnqysbuMrOv6DGfFIU55O9Te8BpZEwJGwClrzVsyVZhzIgQAb-HZRm9Mj-EMWsYmtjewUUAKWIy6iEFG4sHcHS4QaKU4rDpxKvlPt67IDvu_2I3_o6fTRHwW-01eZ6rG2FmF1EkkoyutFrap2CsYmT-ymD6TJcAlhpuUeVP56rEPMzkQoxZ2670aAE_tcvSzXVDdJ2eA19VS1Mqi8EfCFcDKobRtXxwwfws7_h-buXt2xayv0p_QVuLq0YLoyg7qVYav1rTUbKwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ لحظه‌شماری نخبگان ایرانی برای کالبدشکافی زیردریایی به دام‌افتادۀ آمریکایی
🔹
کارشناسان حوزۀ نظامی معتقدند غنیمت واقعی ایران از شکار زیردریایی هوشمند آمریکایی در دانشی است که از دل این سامانه استخراج خواهد شد، و آمریکایی‌ها باید نگران روزی باشند که فناوری…</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/462933" target="_blank">📅 11:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462932">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf99e50f39.mp4?token=e1ovyFYHpyPZzYyk-VdIauHjr7H0U-k0hZF_6DVkGt4mPCTzqvnZFLd01S9rfWfxbMAraC3nKYW_gIB6eXHMWm68gCmENFaQLwmd52GQIjSmnO2H6euafdVPQHd1Nvf9cIoKZriojfJjAB4bYr3qQkOn7gf_6FE1JdSptdC3Qv6F482zCIZWN9sGLEn6wC07f0tVWLnwWxQLL90-1L7lUnijKJkbsKZJSl1Ky6DM5GhxZg09m1PHxircElIv-bbumsDzJ8Z4z1rijH7Mj8qvHCic1SXqd1pq0gyB32ovXJ2QOTvfcTHvNWIdt8HjW2bddMEbTK8HRAojW7CnSeu2oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf99e50f39.mp4?token=e1ovyFYHpyPZzYyk-VdIauHjr7H0U-k0hZF_6DVkGt4mPCTzqvnZFLd01S9rfWfxbMAraC3nKYW_gIB6eXHMWm68gCmENFaQLwmd52GQIjSmnO2H6euafdVPQHd1Nvf9cIoKZriojfJjAB4bYr3qQkOn7gf_6FE1JdSptdC3Qv6F482zCIZWN9sGLEn6wC07f0tVWLnwWxQLL90-1L7lUnijKJkbsKZJSl1Ky6DM5GhxZg09m1PHxircElIv-bbumsDzJ8Z4z1rijH7Mj8qvHCic1SXqd1pq0gyB32ovXJ2QOTvfcTHvNWIdt8HjW2bddMEbTK8HRAojW7CnSeu2oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران: امسال یک میلیون و ۴۰۰ هزار دانش‌آموز در تهران داریم.  @Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/462932" target="_blank">📅 11:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462931">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ef82db5.mp4?token=SbFbN3v-fckJKM-7Oqdh05WBAmOABk9fd6CltST6f4AYbXsBpSbQ0gi1JAPxNE7wBrdZPnBWTvyiLh3v6Jj2LsVCyDzbp4cl0kZJ60eRFNLIlSdPU1gu8xp6_75X0io8xbpPAa9BpehGkm_Ajz7_2llCxPQodO_chVfYSDB7BlehZ-u7N6TMI7-HpaOF2PinNYXFFVvgf5Jk532IR8GWD1uvIW8JsKqo9PTDOrMWYYUumbqi6h98o30EuuBG4417W0isDD5-571iR7cPAx8vmrLAzZH4E8mGkKf3v90VepCcTMPXNSfOZIStyan_fbwG58_Seacd8QKyHpOo-lsYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ef82db5.mp4?token=SbFbN3v-fckJKM-7Oqdh05WBAmOABk9fd6CltST6f4AYbXsBpSbQ0gi1JAPxNE7wBrdZPnBWTvyiLh3v6Jj2LsVCyDzbp4cl0kZJ60eRFNLIlSdPU1gu8xp6_75X0io8xbpPAa9BpehGkm_Ajz7_2llCxPQodO_chVfYSDB7BlehZ-u7N6TMI7-HpaOF2PinNYXFFVvgf5Jk532IR8GWD1uvIW8JsKqo9PTDOrMWYYUumbqi6h98o30EuuBG4417W0isDD5-571iR7cPAx8vmrLAzZH4E8mGkKf3v90VepCcTMPXNSfOZIStyan_fbwG58_Seacd8QKyHpOo-lsYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: نگذارید جوشش خون شهیدان فروبنشیند!
@Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/462931" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462930">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d4b05f527.mp4?token=oNka_moy43DhW3knDMFKCmkmflvik_X9mNZqO_rnens4JHZiVZCMlYDp6Lgair71A3CKn20Nw3WulFDiuTMmB5_kjqHxIkhlaiPJ7wgyTNNx03IziJx-6f9qNIXSZqTkaG3CU1q8_aBb9H__TULu6t4bBd0yKqauLdY8CinHp2rLaVGNigiadvVLGvrHkIKWrSau61HbrQK42kT7zB-DBR1Ktq9WkmRcIC8JEEljkU06uknUhhrwKlNJwJjY94fz9OF1iBacv-iVFGIzgzBfNxOQ2IlrIfZeFeoci3rRFB9hywbizzNgQgqdFp2IxrDpCY9cP6pBwWUnLftPtr-1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d4b05f527.mp4?token=oNka_moy43DhW3knDMFKCmkmflvik_X9mNZqO_rnens4JHZiVZCMlYDp6Lgair71A3CKn20Nw3WulFDiuTMmB5_kjqHxIkhlaiPJ7wgyTNNx03IziJx-6f9qNIXSZqTkaG3CU1q8_aBb9H__TULu6t4bBd0yKqauLdY8CinHp2rLaVGNigiadvVLGvrHkIKWrSau61HbrQK42kT7zB-DBR1Ktq9WkmRcIC8JEEljkU06uknUhhrwKlNJwJjY94fz9OF1iBacv-iVFGIzgzBfNxOQ2IlrIfZeFeoci3rRFB9hywbizzNgQgqdFp2IxrDpCY9cP6pBwWUnLftPtr-1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور تهران: امسال یک میلیون و ۴۰۰ هزار دانش‌آموز در تهران داریم.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/462930" target="_blank">📅 10:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462929">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plp5VZxndNjg5b-DxVlJgXc1BP77ssg-QlC1hmqF7clLgMRQnLOKb9iqeRh_6agAwMnpLrLJ9J556fts-SgXxTvsK406YLZNbA4E11DvPV6BHpxzSy2hMoAW5f0ogmAK_FAPlWULMeJPBcmEIBmVdLImz_pbz7R20qEVJ9NHrHQnfwWX9CRpEyHx3VYsTdNy0BSjQTYqZpQ3OwK2EEiZmKy2IK6WT2fLh1n9An82iAfXvdvgbkiq0w7P2WunfCIskwVnZ17kFX9iyGvZ8ukW9CZ7GBkUdBO1bCeIiy9Y55D3GOBgdJxBOGR-rXkhoFx66Uig-wXvg6PMNxvCsVp4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنظله تصاویر سلفی ۷۰۰ نیروی امنیتی اسرائیل را منتشر کرد
🔹
گروه سایبری حنظله در پیامی با اشاره به «نفوذ گسترده سایبری به تلفن‌های همراه صدها نفر از افراد وابسته به ساختارهای امنیتی اسرائیل»، اعلام کرد تصاویر مربوط به حدود ۷۰۰ نفر را در وب‌سایت خود منتشر کرده و مدعی شد این افراد از طریق ابزار «ناعِم» هدف قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/462929" target="_blank">📅 10:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcb37fe03.mp4?token=e4_HAABUkPZC00x4bgQ34xUrTvxLHPNuZymvnSJVGn2lFINVf6gQrf08SXvLnlLNHds6sSKxppfGlDsh0nMhxHc1DyZq6bG45hTbzyuA1AI6gO88FXBN3J6n3U12iiggsS7DSt96Y5mW9U384058yKcOJK5o4-PW8_mWdnkvT3qv9ULfY0Cjur5aXHkgbN0XDE_znz94C77b40Gz-eYvUjv2125JiSUmAUy7G4FkVj7UNYcsU-1aEcDjxCUjQHJZqK8cx-_VNKjl7KOdV3MBMi9fgfRLDWSgocm0Mw1RjbGU4sFfU8UpKK6iHeSnDAttdCFbAHKB6CTpqXXZlTcaXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcb37fe03.mp4?token=e4_HAABUkPZC00x4bgQ34xUrTvxLHPNuZymvnSJVGn2lFINVf6gQrf08SXvLnlLNHds6sSKxppfGlDsh0nMhxHc1DyZq6bG45hTbzyuA1AI6gO88FXBN3J6n3U12iiggsS7DSt96Y5mW9U384058yKcOJK5o4-PW8_mWdnkvT3qv9ULfY0Cjur5aXHkgbN0XDE_znz94C77b40Gz-eYvUjv2125JiSUmAUy7G4FkVj7UNYcsU-1aEcDjxCUjQHJZqK8cx-_VNKjl7KOdV3MBMi9fgfRLDWSgocm0Mw1RjbGU4sFfU8UpKK6iHeSnDAttdCFbAHKB6CTpqXXZlTcaXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پرده انتخاب اهداف نظامی دشمن توسط تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/462927" target="_blank">📅 10:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj1Ix30iAPEaoZ5JPEfnNWlFWpjgizWkK_CyoMPOEQxJG3oi3kSmeQOs1Ogy5gaviNunby5mleB3ktgzEYLXIg4IGubG25QAiY4r_ykjPpCrPqFKLweFA62airCr_X2CoA2Fyq7iYnFu8K_ijC7ZQg5DmK_3mfN0oYP5Vq4ksrcXq_TF2-Gs75FLZDh2HqCajBtlShT6P0ILYGKniztROjcIN27H9EpsjLhRRF1UUlOliCgk5oYBkcXl-ccsZz95UCdMwH21B8hDMLMvldnjITNFxp1dMkSwPi8G6LLVLqHsES6sINd2DhW3-pcF-1Hf57l6BWQkPI0dCyqqpHd4mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/462926" target="_blank">📅 09:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg1s-nD5EzzNb_DaaE6WU5GPdxSck4gh09SKmWLD5jDNgguK7xwUkofo62GV5WXJv49zbeXjpZgxIbnVlR9ew1I7KM4CTkv46EKPvwxlnFj4OP5_w57gDuDMk66WNd-sZL1HCDOhSXFlpB0q0ptKKYgZ1YZEvLyk91Q_ZkHNMPJ47sP89VUu-jcHMR9KzjLyeSpGHNGDi0_oXuJpWNcPVeu5Zrr7LPa87XluzwI8hex-3RI7v-b8XzT_wczi4HQC54BORbAVVqsjx6a74PT6IyhIYbzioXb9GKmgDWQvw5EWR5sD8RSuXVocH-9nN86cuoo8JYUShnA-Yj-hBdHmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ عراقچی به وزیر خارجۀ فرانسه: اشک تمساح بس است آقای بارو!
🔹
یک‌ونیم میلیون الجزایری در جریان جنگ استقلال آن کشور توسط فرانسه قتل‌عام شدند.
🔹
پاریس کم‌تر از یک‌دهم آن‌ها را رسماً ثبت کرده؛ ولی همچنان از هرگونه عذرخواهی بابت جنایت‌های استعماری خود خودداری می‌کند.
🔹
اشک تمساح بس است آقای بارو؛ سکوت شما در زمانی که آمریکا کودکان دانش‌آموز ما را قتل‌عام کرد، گویای همه چیز است.
🔸
وزیر خارجۀ فرانسه در اظهاراتی مداخله‌جویانه دربارۀ ایران گفته بود: «ایرانیان باید بتوانند آزادانه دربارۀ آیندۀ خود تصمیم بگیرند و حقوق بنیادین آن‌ها باید رعایت شود».
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/462925" target="_blank">📅 09:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa65aa3a39.mp4?token=gROaW7M82BlceZ1CKd4ImiwlJroWCWZK9X63iqDsgpy15ggFRGD5yF6pJAf57TfNa5GImyLV25AOb0p99mMSE7JilYvPo-WdJTifksfy_3_rpEObJ64_L9GCMFtsHB1aZlIzF3Jtph1SZ3meSHhSb40hEsXwEPff7FxF3681bk3pMbZAUFSQWiptJC0-36tODaZpAlHgrw72A-aXSZUedWbqK6Th1Emb0t8kDouc3SxvgeUxtjIe1i8oUiOMBeq1vV3zumI-V1ByHne3WLlM5DmqMie_KvSqHUbmw8i0IILYeRGN4At9PJ_LBRWWEkueOWHLmBvIlJfbT3WITvtzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa65aa3a39.mp4?token=gROaW7M82BlceZ1CKd4ImiwlJroWCWZK9X63iqDsgpy15ggFRGD5yF6pJAf57TfNa5GImyLV25AOb0p99mMSE7JilYvPo-WdJTifksfy_3_rpEObJ64_L9GCMFtsHB1aZlIzF3Jtph1SZ3meSHhSb40hEsXwEPff7FxF3681bk3pMbZAUFSQWiptJC0-36tODaZpAlHgrw72A-aXSZUedWbqK6Th1Emb0t8kDouc3SxvgeUxtjIe1i8oUiOMBeq1vV3zumI-V1ByHne3WLlM5DmqMie_KvSqHUbmw8i0IILYeRGN4At9PJ_LBRWWEkueOWHLmBvIlJfbT3WITvtzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان نیمۀ‌اول بازی هندبال ایران و کویت با برتری ایران  ایران ۱۵ - ۱۳ کویت  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462924" target="_blank">📅 09:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq5eLjTFAADX9CC7sh4RgHdnDQ7hae6RX3cGNqhpAq9HMR1S67L5f3hfIeGGBoSfHWH_kVwy4swSOfLSAN05rK29H1XPDgD7ukNqC-9KTvE3z1rTUtp_jLKZqgWqcwp8o6uQfqGE2VfsX7hh-Nxik43iKHeZs7JHOtvhRaZgcDq0w6s5opcCuxlGzuk2LoiEbR9I6lovE3U0v36r1j8mg3VapUd5r5g7A_3GFVZxYlz5Btbx1eOvHOSv3yjRCRKwuJoGkHcGxqIJiglqG7d5kBdoIwNQm_tX0_9FLdHNkiqgL-WIzeGHZ78PYRT28PX-uJhR6xS8nPZqMm3goegOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام خائنی که اطلاعات سایت‌های موشکی اصفهان را در اختیار موساد قرار می‌داد
🔹
حسین پدران، فرزند حمیدرضا که اطلاعات سایت‌های نظامی حساس کشور در استان اصفهان را در اختیار موساد قرار داده بود، به جرم جاسوسی و همکاری اطلاعاتی به نفع رژیم صهیونیستی بازداشت و محاکمه شد و پس از طی فرآیند قانونی و تأیید و ابرام حکم در دیوان عالی کشور، به سزای اعمالش رسید و به دار مجازات آویخته شد.
🔸
در جریان جنگ‌های تحمیلی ۱۲ روزه و رمضان، دشمن صهیونی-آمریکایی برخی از سایت‌های نظامی حساس کشور را هدف قرار داد که مشخص شد برخی از این اهداف با همکاری عدۀ معدودی از مزدوران و خائنان به کشور مورد اصابت قرار گرفته‌اند.
🔹
حسین پدران از جمله خائنان به کشور بود که تلاش کرده بود با ارسال اطلاعات حساس و طبقه‌بندی‌شده به سرویس‌های جاسوسی آمریکا و اسرائیل، در راستای اهداف دشمن عمل کرده و در این مسیر بنا به اعتراف خودش به منفعت مالی دست پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462923" target="_blank">📅 09:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145990c427.mp4?token=BL24nSLstvKM-1aDnqPDUy5gcZSFor5lnuxnck3YawsFXeqDm22sQkal5pS-b4eV6w4GGltLqaJBJNIKLyAW1fkyb5MjOQf2MYnFy2NZJu-ijnlpeR09SYxSFhKCX2J4Vl8SASS6WlWygJ80EQ_yYp34fJy9EBprsVEx5rMQZuvohWEvSvVAVgPdfhgRr0Ji7F9dUHv8Awi_ZVtikjGzBHYQVmYwN9r_mAjOPurMrCLSZDKuqOry1sILc20Su5n8lySt82ahYLT6SVeit7sz5of5fC0i5t2H4C38HsNukVcX5v9DwhJshDksfwretQwLuQSD6t4k_-Pg5yClxr5tjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145990c427.mp4?token=BL24nSLstvKM-1aDnqPDUy5gcZSFor5lnuxnck3YawsFXeqDm22sQkal5pS-b4eV6w4GGltLqaJBJNIKLyAW1fkyb5MjOQf2MYnFy2NZJu-ijnlpeR09SYxSFhKCX2J4Vl8SASS6WlWygJ80EQ_yYp34fJy9EBprsVEx5rMQZuvohWEvSvVAVgPdfhgRr0Ji7F9dUHv8Awi_ZVtikjGzBHYQVmYwN9r_mAjOPurMrCLSZDKuqOry1sILc20Su5n8lySt82ahYLT6SVeit7sz5of5fC0i5t2H4C38HsNukVcX5v9DwhJshDksfwretQwLuQSD6t4k_-Pg5yClxr5tjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در ۵ روز آینده در بیشتر مناطق کشور جو آرام خواهد بود
🔹
در ساعت‌های آینده در گیلان، مازندران و گلستان باران می‌بارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462922" target="_blank">📅 08:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آغاز پیش‌فروش بلیت‌ قطارهای مهر
🔸
پیش‌فروش بلیت قطارهای مسافری برای سفرهای بازهٔ زمانی ۱ تا ۳۰ مهر ۱۴۰۵ در سامانهٔ
raja.ir
و سکوهای آنلاین فروش بلیت آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462921" target="_blank">📅 08:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b167cf75d.mp4?token=UfI21jX8k5YD5XWY0qbRbGxmlWBWlBPEkj7M5uvx2li0HkPn7dBmiMUrpLHYaoCL3Lrk_Bk3nC2tqBzNhUblhXX6uzxs0IoKttkmGEZZaEm5893a_ktP4V0bCRzJu-Skxnk7igZ_C51ox572GokwBTPRhqejcbFTrZIi0ptPJcw0P7Cg-dAADJvavrlpZqyX3LWMQw1UaFrOA7dPYCAYhquPvT-V4zUh2X_BAhrPEhU6B3ZfMJzVMZd-lYUVWR5Bk6ovTh5dc5oiNvovFPnK84wyHqRgol0tq6xVPz9lwQCQ4GzvdOr0YhRZt7zuJL0Qi9uieUhku8IcCTB-G3kC1FV3LHsNxE6FGGGi4JV5kHu1wdsJ1fCMqNE5o8NIfm4_DEA7Yqch1zeEKFHzCnkqZ5rqFJWwdFtoXyFWUW5gac3GowOqwkA0fCqTAlMq1iFT-5fi_lS29qJKVdK1A6x-3HXK-oMQmOtcPH23bZWJ1eSp_uJuwewxn9c1jFrG0zrkPlIVjmbMETYn6JvyzTJmF0actImUQWY1knraUImMC8pf5Q1aKOuGXnKH-2HF-I6x9q1f-G2PcMWtrhRyls-MBuTiT6kaUZXxXPeHj5GvWJYxis4koQTlONELRk-akmtwoS29ftgpzdpOZK2a9FiKxLln8hbc1GvhxvFr6mxaZ3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b167cf75d.mp4?token=UfI21jX8k5YD5XWY0qbRbGxmlWBWlBPEkj7M5uvx2li0HkPn7dBmiMUrpLHYaoCL3Lrk_Bk3nC2tqBzNhUblhXX6uzxs0IoKttkmGEZZaEm5893a_ktP4V0bCRzJu-Skxnk7igZ_C51ox572GokwBTPRhqejcbFTrZIi0ptPJcw0P7Cg-dAADJvavrlpZqyX3LWMQw1UaFrOA7dPYCAYhquPvT-V4zUh2X_BAhrPEhU6B3ZfMJzVMZd-lYUVWR5Bk6ovTh5dc5oiNvovFPnK84wyHqRgol0tq6xVPz9lwQCQ4GzvdOr0YhRZt7zuJL0Qi9uieUhku8IcCTB-G3kC1FV3LHsNxE6FGGGi4JV5kHu1wdsJ1fCMqNE5o8NIfm4_DEA7Yqch1zeEKFHzCnkqZ5rqFJWwdFtoXyFWUW5gac3GowOqwkA0fCqTAlMq1iFT-5fi_lS29qJKVdK1A6x-3HXK-oMQmOtcPH23bZWJ1eSp_uJuwewxn9c1jFrG0zrkPlIVjmbMETYn6JvyzTJmF0actImUQWY1knraUImMC8pf5Q1aKOuGXnKH-2HF-I6x9q1f-G2PcMWtrhRyls-MBuTiT6kaUZXxXPeHj5GvWJYxis4koQTlONELRk-akmtwoS29ftgpzdpOZK2a9FiKxLln8hbc1GvhxvFr6mxaZ3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۲ شب مقاومت ملت ایران و اعتراف دیرهنگام شیطان بزرگ
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462920" target="_blank">📅 08:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febaebfe43.mp4?token=hrjTxX6oogYcImcyOvZYCwOaixpDV_o3X5tCPpPUHjiOvOILHWQKdo6IetEMtg4t_6bUNVk6AGj1xHS85IPzZc8S97Klbi8vYGidrncofxhOHH-6M_r83nUEzxPCwN1tl2UOdiImoIQQ88fAu6yK7SjHS-LJZXeBcHWDuM6PCHr_q9J3BcP6BkLKSKaTh1DIoyI8RtqTF-kvy32480Hs4FswxWJfSnrbGD0mmUeHAhehXhT-d0IM1MfcGR4fMxsv0P_r73hlKkNpEeAKooPlq_CkzF1V70jH1u8c3C6IDr4N3Q9j9FFq3sBm2i_T11no6wjc_U3EoBKNGsTBPAQAlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febaebfe43.mp4?token=hrjTxX6oogYcImcyOvZYCwOaixpDV_o3X5tCPpPUHjiOvOILHWQKdo6IetEMtg4t_6bUNVk6AGj1xHS85IPzZc8S97Klbi8vYGidrncofxhOHH-6M_r83nUEzxPCwN1tl2UOdiImoIQQ88fAu6yK7SjHS-LJZXeBcHWDuM6PCHr_q9J3BcP6BkLKSKaTh1DIoyI8RtqTF-kvy32480Hs4FswxWJfSnrbGD0mmUeHAhehXhT-d0IM1MfcGR4fMxsv0P_r73hlKkNpEeAKooPlq_CkzF1V70jH1u8c3C6IDr4N3Q9j9FFq3sBm2i_T11no6wjc_U3EoBKNGsTBPAQAlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان نیمۀ‌اول بازی هندبال ایران و کویت با برتری ایران
ایران ۱۵ - ۱۳ کویت
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462919" target="_blank">📅 07:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اعتراف پنتاگون به هزینۀ ۴۳.۶ میلیارد دلاری جنگ با ایران
🔹
پنتاگون در تازه‌ترین برآورد خود اعتراف کرد جنگ با ایران تاکنون ۴۳.۶ میلیارد دلار برای آمریکا هزینه داشته است؛ رقمی که هنوز خسارت‌های احتمالی واردشده به تأسیسات نظامی آمریکا در ۸ کشور غرب آسیا را شامل نمی‌شود.
بر اساس سند ارائه‌شده از سوی پنتاگون به کنگره، این رقم از دو بخش تشکیل شده است:
🔸
۱۱.۲ میلیارد دلار هزینه‌هایی مانند سوخت، حقوق و مزایای نیروهای حاضر در عملیات، خدمات پزشکی، قطعات و نگهداری تجهیزات و دیگر مخارج عملیاتی
🔸
۳۲.۴ میلیارد دلار مربوط به هزینه‌های جبرانی شامل هزینۀ جایگزینی مهمات مصرف‌شده، هواپیماهای آسیب‌دیده و سایر تجهیزات و دارایی‌های نظامی
🔹
به این ترتیب، بخش قابل‌توجهی از هزینۀ برآوردشده جنگ نه صرفاً به هزینه‌های روزمرۀ عملیات، بلکه به جبران مهمات و تجهیزات نظامی از دست‌رفته یا آسیب‌دیده مربوط می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462917" target="_blank">📅 07:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrQox7nbTagy_-so4YL3fSZwSOIx67QQvZzY3Xh47eRuwUWG9nIEKQHjbUvDUG9o07zxqQNH7xnjQfoEeSYfYdWf8jcZge0HPL6IwApDTqPTITdSwcbnCF_nua-BynJuEHV9GAAd8-7cR0YWS3ZmnaRP3P6EYr_lZ30YxFT-hU3XmZHE8qa9zMiamrGV8FhDxLivV_Rh8eBsjZ5TN9olDFtURN6qZ5MPaUTeP9lamkzqlV6qiqcRVexyoXDybItEIBHIb0JlM_EpJw1DV3v-_tW97njZuLuJA7OsVwxd0TYyi850O3oYfll8vk0tYBtG3ibT27j3EawyhD8HlBNyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار به مسافران شمال کشور؛ خزر مواج می‌شود
🔹
مدیریت بحران کشور با صدور هشدار دریایی سطح زرد، از افزایش سرعت وزش باد و ارتفاع امواج در دریای خزر خبر داد.
🔹
این شرایط از امروز تا ۳۰ شهریور، مناطق ساحلی و دور از ساحل استان‌های گیلان، مازندران و گلستان را تحت تأثیر قرار می‌دهد.
🔸
از جمله پیامدهای احتمالی این شرایط می‌توان به خطر غرق‌شدن شناگران، آسیب به قایق‌های کوچک تفریحی و مسافربری، اختلال در تردد شناورها، و اختلال در فعالیت‌های ساحلی و فراساحلی اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462916" target="_blank">📅 07:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRtYvYFH4QxUj-6LcCvyguGTRoCVh4bHeWJTNdXbXwqFmu56nHHSYaBtlmGxIQW0zJOOyi1_04gtIFlIrkQvCq87ylKTfb2EDXySm6EOzFrhKSzVnij87LkH8FPfJNFGec6EMCWX4Xph7fmXIVfD3P-37g5OVEgYYp-IKV74BBWAx0X7i1217GV6Ipcqp49MXArtyELUtvT3YYLjHTidfwVJwfGxNgne3weTbuAIyFDFv006D4f2CDuMFw-WUFq6flhktNykCpTWjnyuDp3INWJRxoyjMxu1qstaVQw22xq_H44IJPyUFyDxZ0fgGEhKGzi6OqfGkjWLyrmEKLUmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز حضوری مدرسه‌ها با ۱ میلیون و ۱۵۴ هزار کلاس‌اولی
🔹
آموزش‌وپرورش: امسال یک میلیون و ۱۵۴ هزار دانش‌آموز کلاس اولی وارد مدرسه می‌شوند و جشن شکوفه‌ها، مطابق رسم هر سال، پیش از آغاز رسمی فعالیت سایر پایه‌های تحصیلی در سراسر کشور برگزار خواهد شد.
🔹
تمهیدات لازم برای بازگشایی مدارس اندیشیده شده و آموزش در همۀ دوره‌ها و مقاطع تحصیلی به‌صورت حضوری آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462915" target="_blank">📅 06:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub7Frn_yh6cAblLcT0f5hhjJpA8Qj1NujyS3cwxG-5lsUHXf4sKasxMcU2j_FYqpXeWoI6OEt6kc8HhyCeRo3x1JmSdJTNsCH-KOSgNV1psXQY8PiKl18vGVQFxzJfN0Z-wJv1v-IGfvelG-1U1QejPxgfnm6VRPNyqrZeF0Cmak-qJPT-mCDznog3YuChKtfPVzz0ZMBRHURd16BTOdwb04pJQZRo_H4j5UJLS5KERZCIB8iP0p2aOzcuBTIdz_TLW5KAj4ytqaoVWYgcZLq07KR5YLkWTs8NGii_PSjZJfsxa2CzEpTAFNleyoFlRtRYIdpv8qXXCvP42aGTC94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز ربات‌ها در آستانۀ جهشی بزرگ
یک شرکت چینی فعال در حوزۀ هوش مصنوعی تجسم‌یافته می‌گوید ربات‌های انسان‌نما ممکن است تا اواسط ۲۰۲۷ به نقطه‌ای برسند که بتوانند دستورهای طبیعی انسان را بفهمند و برای اجرای آن‌ها مجموعه‌ای از اقدامات فیزیکی را انجام دهند.
🔹
«اسپیریت اِی‌آی» اکنون ربات‌هایی دارد که در خطوط تولید شرکت‌هایی مانند «سی‌ای‌تی‌ال» و «جی‌دی‌دات‌کام» فعالیت می‌کنند و نرخ موفقیت آن‌ها در برخی وظایف ساده و ساختاریافته به ۹۰ درصد رسیده است.
🔹
اما ورود ربات‌ها به خانه همچنان فاصله زیادی دارد؛ چراکه محیط خانگی بسیار متنوع‌تر و غیرقابل‌پیش‌بینی‌تر از کارخانه است و به داده‌های بسیار بیشتری برای آموزش ربات‌ها نیاز دارد.
🔹
این شرکت برای جمع‌آوری داده، حدود هزار نیروی قراردادی را به تجهیزات ثبت حرکت مجهز کرده تا کارهایی مانند بازکردن یخچال، بازکردن قفل و آماده‌سازی مواد غذایی را در محیط واقعی تکرار کنند.
🔹
به گفتۀ مدیر شرکت، سخت‌افزار ربات‌ها با سرعت زیادی پیشرفت کرده، اما «مغز ربات» همچنان ضعیف‌ترین حلقۀ زنجیرۀ رباتیک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462914" target="_blank">📅 06:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آمریکا با فروش ۲.۷ میلیارد دلاری تجهیزات پدافندی به اوکراین موافقت کرد
🔹
وزارت خارجۀ آمریکا با فروش تجهیزات و خدمات نظامی به ارزش ۲.۷ میلیارد دلار به اوکراین با هدف توسعه و ارتقای توانمندی‌های دفاع هوایی این کشور موافقت کرد.
🔹
به گزارش رویترز، این قرارداد بخشی از همکاری‌های نظامی واشنگتن و کی‌یف است و بر توسعه و به‌روزرسانی سامانه‌های دفاع هوایی اوکراین تمرکز دارد.
🔹
با این حال از زمان تأیید وزارت خارجۀ آمریکا تا تحویل تجهیزات به اوکراین، ممکن است ماه‌ها و شاید سال‌ها طول بکشد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462913" target="_blank">📅 05:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMZa_dOkfXTXcsow0yk0dVn4mexj5UanD_qqi7pWlCYe0oH-jvJPJPGmqulE2jtX9u_cDU57eNhwFSidOm8-RbxC-ttAKXEVa2h11LD2gJ1BR6asWtu9r_PGMx_ratYrelAssaVqsj6dmbsGZywolYeWDAhFCMi7Pg9AZpDy0jrQZX4fhD9GojYVAhc7EtnuCjRhU65rxlPzN4IRTfODhOZo68P3dYE6mWRTdf01MF2WDMdg8bEGMyoioDUk2mr6K85YvLUC7W-rSOi0aEASZVoR964ZHhgdehDBO4XVdSoyD2w62QyPBbLTF_J8ExAzuC6x6t11uO65m6A9uYitbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAfsDcqazWUU4lf8uZ1k6JLHylvaq-3p3Yb3kXhZtM2cbmWKHAaTrsXCC1uqg-BbENgGILypHikQt9hKVFxRG7JUznBB1pgcVkVifkJLFemUMVpbWdG-gcc2lX-FtT2cbphH2eq8tP3_3INAAZkuAfLXglBhYOpf5soRJkkA3bnFnOdIxA3maLC3_uyrIkRxjJdeD96GquBMHrCYRMFHc0VSQzB2WKsAQxmv0NI4hgQc0JBU9wTYE3KmyMOuFChQUL-emC4mNBKTZVEfiBcwQRmwEvfqolbGPb7szcaZC8PGuknRpIdML37XD4kx7Qx9qcSG28x71CVla5vkDKLtig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدستی انگلیس در جنایات آمریکا علیه ایران
🔹
فعالان ضدجنگ در انگلیس با تجمع مقابل پایگاه هوایی فیرفورد، تاکید کردند که لندن با فراهم‌کردن زیرساخت نظامی برای حملات آمریکا علیه ایران، در معرض اتهام همدستی در جنایات جنگی قرار گرفته است.
🔹
صدها نفر از فعالان ضدجنگ می‌گویند بمب‌افکن‌های آمریکایی از پایگاه فیرفورد برای انجام عملیات علیه ایران استفاده کرده‌اند و بنابراین نقش لندن در این جنگ فراتر از حمایت سیاسی است.
🔹
به گفتۀ آن‌ها، زمانی که هواپیماهای نظامی از خاک انگلیس برخاسته و به ایران حمله می‌کنند، لندن عملاً در این جنگ مشارکت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462911" target="_blank">📅 04:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/513f35c074.mp4?token=tHMhV_819MvyLjub-HmVPg-6Co-E1EKe_e50dTn-5x-zpVCUXEDrL4vqGH8tx52hahkgBlRS8p45jN9JLr4xE9Qn_nAxWcg1OkLaYpvD4ealEQ-zFPHCQScECFQQCImSm2Y8-gunRkPigS-2Fr4LRZjzQQhbEyjNY65fJLP8mmPlWQk0LFiDnVWla5Iw0gLD1c4Ez_HM9bXzMVAQqRBVBZA44_My6O1uDRd5duLf6yeVMa8_MCYaNSczCxpGRg6DfgqA-412qDPv4Sq9LrTaIX1sXjnJ9aK4cZb1TxN-3LTeZ32JKI4UI-omFYoREnMOVartsxOHxDeOeVnKWSG1DYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/513f35c074.mp4?token=tHMhV_819MvyLjub-HmVPg-6Co-E1EKe_e50dTn-5x-zpVCUXEDrL4vqGH8tx52hahkgBlRS8p45jN9JLr4xE9Qn_nAxWcg1OkLaYpvD4ealEQ-zFPHCQScECFQQCImSm2Y8-gunRkPigS-2Fr4LRZjzQQhbEyjNY65fJLP8mmPlWQk0LFiDnVWla5Iw0gLD1c4Ez_HM9bXzMVAQqRBVBZA44_My6O1uDRd5duLf6yeVMa8_MCYaNSczCxpGRg6DfgqA-412qDPv4Sq9LrTaIX1sXjnJ9aK4cZb1TxN-3LTeZ32JKI4UI-omFYoREnMOVartsxOHxDeOeVnKWSG1DYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایمانت ایراد دارد اگر یادش در دلت نباشد
🎙
حجت‌الاسلام کاشانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462910" target="_blank">📅 04:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9375f31c39.mp4?token=qKZPaOgMk6j0yD0dYHQjFIM2NYG229XYQ69PCE-fMYwzzNoeQvRy-2sogzWnyoaA2H7oCxXK40RXBGmqgIuo7l3IALKQJ--yTst32kMZFHqAXdiJU-F2PE2QWOsVfXGcMghlcH1MgwGnpfgseDibrDi5jpsEbxmNVdHhURlgv7932ckQ44GUiAt82ptaMtsYkA3wsTVLVRr9bLv5uNItqTWNffYIys_U_uzQsz9Iz3iE62xhYk8s2xKGdMVZvyVKPOLxG5bEp_25rtY3ywu1-78dMAv0FP_IAlGEW6ovK0-GOhlYgBwKyWjvn3TrYCEMcm_4GX3409SRDGniecsA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9375f31c39.mp4?token=qKZPaOgMk6j0yD0dYHQjFIM2NYG229XYQ69PCE-fMYwzzNoeQvRy-2sogzWnyoaA2H7oCxXK40RXBGmqgIuo7l3IALKQJ--yTst32kMZFHqAXdiJU-F2PE2QWOsVfXGcMghlcH1MgwGnpfgseDibrDi5jpsEbxmNVdHhURlgv7932ckQ44GUiAt82ptaMtsYkA3wsTVLVRr9bLv5uNItqTWNffYIys_U_uzQsz9Iz3iE62xhYk8s2xKGdMVZvyVKPOLxG5bEp_25rtY3ywu1-78dMAv0FP_IAlGEW6ovK0-GOhlYgBwKyWjvn3TrYCEMcm_4GX3409SRDGniecsA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئوی منتسب به موشک یمنی در آسمان شهر ریاض  @FarsNewsInt</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462909" target="_blank">📅 04:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d160a38e6.mp4?token=YzR71sgjM7Dr2cGE_U49R2IbIPJ8AvMN2o3oUh0yEQ1mB4bpdZf4n6x9N-uMm9Y4jrtFP9OxIwTIeqxhfeK_XWGoJV4d2weXymSVajoY4XccELwH1PwKsTj-J1EfflD8Q1NvN2vQZX2DuahcFQyfKBNLHecmo4K70VPfCJv2tuhiwTOoNscwE_cDJftlfaCbiRp0LqiVqyZCUezjv5ucp9eukcdYmq-75d1JVwFbQEQ6HRyniODL4gKljK4p3sbCVF7XFBkC-BrQUwxmbTAjV8yWZxFdybaVmRThS96PPWQhot2chnzvDMx907A1DNtPHVUIIIKG9HACpQhInpAXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d160a38e6.mp4?token=YzR71sgjM7Dr2cGE_U49R2IbIPJ8AvMN2o3oUh0yEQ1mB4bpdZf4n6x9N-uMm9Y4jrtFP9OxIwTIeqxhfeK_XWGoJV4d2weXymSVajoY4XccELwH1PwKsTj-J1EfflD8Q1NvN2vQZX2DuahcFQyfKBNLHecmo4K70VPfCJv2tuhiwTOoNscwE_cDJftlfaCbiRp0LqiVqyZCUezjv5ucp9eukcdYmq-75d1JVwFbQEQ6HRyniODL4gKljK4p3sbCVF7XFBkC-BrQUwxmbTAjV8yWZxFdybaVmRThS96PPWQhot2chnzvDMx907A1DNtPHVUIIIKG9HACpQhInpAXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئوی منتسب به موشک یمنی در آسمان شهر ریاض
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462908" target="_blank">📅 03:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حملۀ موشکی یمن به ریاض، پایتخت عربستان
🔹
سازمان دفاع مدنی عربستان، در دو شهر ریاض و الخرج هشدار امنیتی صادر کرد.
🔹
منابع عربی از شلیک موشک از یمن به سمت این شهرها خبر داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/462907" target="_blank">📅 03:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOUb3zb4dN89Z9LdA6b4_VcGS2ubLSVShIc09uyZgCSQgHwBPpvFBd2oqm8YndIsodP5qkNdQb2WbrZicBvgMexiZ-3C6t42YWZ7WK8tHXFvsqRe4KHoOVMktmrJVQCFSDEmB6evF3lDWyawvyP-EuVuSB48N72QqDrTLSNm_4Q1r-tRvahuLT6PjlSQZOv8M0guz4pLJLysBD5wTmPCn_EUHWOU8In1yMqHb9w60Zp512fUWHJxK98qcvZRYQFo0Ua_19pEtlOBwolLczioO8K5G7Prvwti1_CRqBw1qas28phGKU0uhnAEPBGerb6LskyWgn7ERfLsJItzi6mzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ خبر خوب از اقتصاد، فرهنگ، زیرساخت و فناوری  زیر ساخت و خدمات عمومی
🔸
داراب و زرین‌دشت با افتتاح ۱۴ طرح کلان برق، پایداری شبکه و ظرفیت تولید انرژی پاک را تقویت کردند
🔸
سازمان غذا و دارو سامانه هوشمند پشتیبانی داروخانه‌ها را راه‌اندازی کرد و ثبت و پیگیری…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462906" target="_blank">📅 03:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdVEpEkcGry-_8ECyTWBY04XtKTSnjNLUW94sDc9wdaFP5hUAYKHUoFYcVRAGkDQsdlIjxIGO3hxjYdAGPsJTvNjEaDDwhG2HSwSYIGqN1Oly1AN-PxHrH933OMLxuK2BeqbEFacb7m12faDckxCLYZPA05dv6IUYADky4tucE7zyrU6A85vs-V_QnsAhCAwqIL4z7CorSK5LiI6o8-jgCJxVgq9QiL_KVBSbVHMuUAXp7DEXpVf0Yj4J98uFBaWrMZV6kgQKLo6q55SfBvmQ2m5w3Va4MJUaLo6ejY6krG9damqZvEDK8rjEeIFNO1ZKVwVVV8wnH14ySJsTYjrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار گردشگران ورودی و خروجی ایران در بهار امسال
🔹
آمار وزارت میراث فرهنگی و گردشگری نشان می‌دهد در بهار امسال، ۹۲۸ هزار و ۷۴۶ گردشگر وارد ایران شده‌ و در مقابل، ۲ میلیون و ۸۵۵ هزار و ۱۴۶ گردشگر نیز از کشور خارج شده‌اند.
🔹
طبق آمار منتشر شده، عراق مبدأ و مقصد اصلی گردشگران بوده است.
عکس: امیرحسین ترکمن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462905" target="_blank">📅 02:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLMfgaZK3psKFfO9zQh8BDnz329x6EC-iKC1FsDWDWtfV4zLf9hNvhqxVR1uucNW7pFIlysoAb5jb5D5cOgRbkvuGSWK3HrXoW8ZvslFLJJCl9i09mU86MuAR-2oTzYJQxgOFipHMUJPfJv3eCC7siMszjLH954mLV3iXJ7RePP5CjJdmyRvnxoRNPaLEia8jlF8oCzhpQiFK2BPSjxX7APoSBL-X9JvGxnFBneXv1Voel1KTd0CP7zpveehHqNu6X--NhUeMH0RIASQn_guNlpwbCh8O2xLxyH4IyNHSqRrDoxdjYATBxiPfT14AO7TZOeQ-tU34V8utaDU_jixbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر اسرائیل، اطراف شهرک القنطره و كفرتبنيت در جنوب لبنان را مورد حملات هوایی و توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462904" target="_blank">📅 02:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I86Pr8uq4aopeug42Tx47uzSKvTQKXUaVnxG7hLvQRxTH8hs2khtdzgKsnWT_TnLCdZQErhEVBMCKedAs1-2I0R8jpYxHwJ4eKwI_q3cbpd8aSaB3USq6nI1I3BklPBa3Wzfm-VVGtmC1s38IabRyVaFqiKGErwpVgl5UTcLiJ4eX1EB_96zrtAi6ClIuerApyT-KSy6GwNmZYtFhwow9KLsuFJqADpo0h45OCugXZEtvlQ7cRd6N9H8coDjVSJBJQRmzgoQJBsJsqyQ4kzhevTT-NAZz42w_fisIIrq_tsm2PnxSdd9lRYLN5XHme_yeQoUZYS01dV4mI4m2Za0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔹
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔹
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462903" target="_blank">📅 01:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">منابع عربی از شنیده‌شدن صدای انفجار در جزایر فرسان عربستان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462902" target="_blank">📅 01:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌ تصویب طرح تحریم روسیه و ایران در مجلس نمایندگان آمریکا
🔹
مجلس نمایندگان آمریکا طرح تشدید تحریم‌ها علیه روسیه و ایران را تصویب و برای اجرایی‌شدن به کاخ سفید فرستاد.
🔹
این طرح موسوم به «قانون تحریم روسیه و ایران ۲۰۲۶ لیندسی گراهام» با ۲۶۲ رأی موافق و ۱۵۹ رأی…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462901" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462897">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqQ2R7R4iZrYjenGkiiuHO3bru0nlliOehjKQj_MI6a8JB2EUDMimrt484OC5-UvXu-9TxckrYTtVHLDTazPWC_Jr2aACSLONlEg7tkX8DOJt2VpzP6XF_qx3-87IF14CkVDJiXJI3BPiAChoCDFx_1RBKRuxPyrPVOw1dtGtLlI7ZCZhAV87gzPWic_PSigvwyZqhpc4wRNKmrYez7gYxtMsuQfWjZBKan2v7xOXhziea_BtcDbVKpPfuOc4tZ-76Ph05LaDUIQH-SP33ZlgcOpiQjDQnMwYWIQ6lYSSb6IDZRj9BnbKBXe6zR5dnVl1qMEtdXbdUdr25L6mDFIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIK8-5BYidTAe7CkMgx_5IWo_lUF9MikWZJ0wmyMk6zHxl2ZRTCmT6ll1RIXxohnNdg-85nV9exU67epd37I3dzariNtMwhAkkgByOx9AbBl49a0WgOeGQ1Ymy8vQi4UXdlAfeuRMkqLhGlGWgTtZ0JgiGigb_6S2pB-w5heMZ2H8W7R8xvUKV1TpQMOojXmtgJdd1aw9Diuf8AuU4QPqxdDhqvcphsxw-qAVO6K9LgyARWUXG1rTFmxV_rbjCcpaFOhPizlc2xtNksX-P2GfNKDSSCj7VNQhGHX_HbtuWA0TIkFTPUoAN64bBh7PEjtt5orTg97nlFvx8VykcgsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uy01ZdvvFqlsj6oc2zpFpLHgSj-V-M3MZ1iXClJR1P3AuhFH8-JRph3VMsxRK6KJx8K4gJX_LQFCy4-T_OKAlG22bgHzRjWuIi6LQTVVeSuOW-0r-5OrJf_18FVHoypm4DrBQDi98hUlqFDO_KJJQyuMvmAIkmfJxzpSowwaoN69V0Z-0f5WnAIWsDph8dIGBu4kx06TAUK_8OvpmK_7lIpESc-_eb_2FzRjNSuvqkWtjySxYvF15MK_7_Z_AymEv5hy8Anu4WhKjr1-qg2dBnvS5WOVTysZogrguLUm34gy5Zd6aXXR1AxNUi5aB3fWOBoTJNmFa07oxwNnLfZBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRo9mOIm8LjpoOY_78vlBquTHNYiKXeiu_VmjMsXv7QVwYrFt-17Mv0PfoFIzxFyjxf5PFR_4PR3KDtxTj9znQ_1Md9UcQkuqR1Kw3KY0pDpaWad_XmCTOfQq93nnvOrsB6yPRQoO97lf6zBFhdfr_SFTwD4X_iRD1WpXdZo3V_PUXH9HZ_1-0MUAJCYm1LR7TETPfDD_Kq2Y61qLyiNPLFECsTzht9jk7zQXeyZtDg0TBW11Lo0sXDVm3xiBQcCQte4BZ5znxpS36T89Oz8sPYLHKoa3qAFq3sqtwXl3kJaXdS_LPJOaZCcayh_KNmxLzi8i6IAK1kagao1hQA44Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر تازه از ویرانی‌های یک پایگاه آمریکایی در کویت بر اثر حملات ایران
🔹
وبسایت میداس‌نیوز با انتشار تصاویر تازه از یک پایگاه ارتش آمریکا در کویت، جزئیات تازه‌ای از حجم ویرانی این پایگاه در پی حملات موشکی و پهپادی ایران فاش کرد.
🔹
در این گزارش آمده است: به‌نظر می‌رسد که چندین ساختمان در این پایگاه به‌طور کامل تخریب شده‌اند و همه‌چیز در اطراف آن‌ها نیز ویران شده است. ساختمان‌هایی که قبلاً در حال کار بودند، اکنون به تلی از خاک تبدیل شده و آوار در اطراف پراکنده شده است.
🔹
نگران‌کننده‌ترین نکته در تصاویر به دست آمده، مربوط به یکی از پناهگاه‌های پایگاه است. این پناهگاه‌ها از جمله سازه‌های مستحکمی هستند که سربازان برای پناه گرفتن در هنگام درگیری آموزش می‌بینند. طبق تصاویر، این پناهگاه مستقیماً مورد اصابت یک پهپاد قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462897" target="_blank">📅 01:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462896">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462896" target="_blank">📅 00:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462895">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسمومیت با گاز ۱۶ نفر را راهی بیمارستان کرد
🔹
اورژانس بابل: در پی نشت گاز منوکسید کربن در یک فروشگاه در جادۀ بابل به قائم‌شهر، ۱۶ نفر مسموم شدند.
🔹
مصدومان این حادثه در بیمارستان‌های بابل بستری، و تحت بررسی‌های پزشکی قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462895" target="_blank">📅 00:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462894">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6262f03803.mp4?token=cnK3LSCLcgBCaodSHsC_6AhUbI6outzEWgLwtA3fgpkswK7M4bUDkVy_YGpC6Xy9cHV3B2WtcvgqxLLeDvxQRuJQYXmuJ6yja6Y5XiwEL7AL67hArAWLvIrNOXQKrFPIjK5HsZTLAF0rEy_VcIk7-BkQv9IhSao18R8Y9KJjWX6ff025Hj4iykmxhC29oCzCXrdArzHOTfDywafA-Bw_9Gp4QGY56qu_J25jPiX6diEULeyQYP7tK67uMbKyDQZINnzkZApBWmz_MwuHNFP8E8vaFS4-6NkYrhPbaCOVFo7jmO1Uz8_94SveK54RTjS_SXaW9Bx3wDiwLANYJHPQIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6262f03803.mp4?token=cnK3LSCLcgBCaodSHsC_6AhUbI6outzEWgLwtA3fgpkswK7M4bUDkVy_YGpC6Xy9cHV3B2WtcvgqxLLeDvxQRuJQYXmuJ6yja6Y5XiwEL7AL67hArAWLvIrNOXQKrFPIjK5HsZTLAF0rEy_VcIk7-BkQv9IhSao18R8Y9KJjWX6ff025Hj4iykmxhC29oCzCXrdArzHOTfDywafA-Bw_9Gp4QGY56qu_J25jPiX6diEULeyQYP7tK67uMbKyDQZINnzkZApBWmz_MwuHNFP8E8vaFS4-6NkYrhPbaCOVFo7jmO1Uz8_94SveK54RTjS_SXaW9Bx3wDiwLANYJHPQIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیرجانی‌ها در شب ۲۰۲ در میدان حاضرند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462894" target="_blank">📅 00:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462893">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
منابع عربی از حملات موشکی و پهپادی یمن به پایگاه هوایی ملک خالد در خمیس مشیط خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/462893" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462892">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجار در جازان، ابها و طائف عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/462892" target="_blank">📅 00:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462891">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
مردم فسای فارس ۲۰۲ شب است که پرچم‌دار هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/462891" target="_blank">📅 00:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462890">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
دفاع مدنی عربستان برای استان‌های جده، طائف، خمیس مشیط و العلا هشدار خطر صادر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/462890" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462889">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5938a453.mp4?token=K0EvV9qzPwUMsYV24QaNZ7UtJvrZRqt30zz5RvEu96IeHePXXPNZ5-JYEJOHSGWVUITSUePaUwEymNcZnfOZ3vvJWuZbNvzpxvFLUclYZJwVJyD1F5PMRMsPqC33dCYbTACzZZLP1f8aaIT0JGaO_HcMaNKTP10lyG7Y4CSZHMsxLX9kvFhwvdTd4GqFvcFr6LryoFGQKtHCDoCwOhoLOEU7Avh7PBi6DXMsrztjTWGSFllzoLt5HOlf2lvqDJtds3b6_SuVv5bT48F_1mXP7kzMs3AtqsaDqW6QX2zDTFJPyZDvxwexT7M23_u_p1WFha4JrPys9o4NqhVF5CUvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5938a453.mp4?token=K0EvV9qzPwUMsYV24QaNZ7UtJvrZRqt30zz5RvEu96IeHePXXPNZ5-JYEJOHSGWVUITSUePaUwEymNcZnfOZ3vvJWuZbNvzpxvFLUclYZJwVJyD1F5PMRMsPqC33dCYbTACzZZLP1f8aaIT0JGaO_HcMaNKTP10lyG7Y4CSZHMsxLX9kvFhwvdTd4GqFvcFr6LryoFGQKtHCDoCwOhoLOEU7Avh7PBi6DXMsrztjTWGSFllzoLt5HOlf2lvqDJtds3b6_SuVv5bT48F_1mXP7kzMs3AtqsaDqW6QX2zDTFJPyZDvxwexT7M23_u_p1WFha4JrPys9o4NqhVF5CUvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب‌های اقتدار کرمانی‌ها به ۲۰۲ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/462889" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462888">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
دفاع مدنی عربستان برای استان‌های جده، طائف، خمیس مشیط و العلا هشدار خطر صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/462888" target="_blank">📅 23:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462887">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b154b3e348.mp4?token=RwCdTsxl53N_MzB8enyN9PWMnoILf0ZwCzAi-rKfDW1HmN2qUVyt12NeTdYGD-5JuZSMzROBL1GeqER3zjT5nTGHf_jIKqeeJg45gzfGy8ewEtdtxW1yQDYp2B0XkeiamIuz61RaEW9odULVlev9wDxZJQKINVkq1s4Y3GbTCrGyEh6jJjHk45lr_J36EO57JconvujNelTcEru7mY2OWFC-DaO-Exg1TwmxtWMYi1_wsGBZ29dxl0sigz1PJ7ERrbxIHyGErTY6pYc91kZoPtKMZrn_cu2DrW3iOGA4Oc1nVmuBplkZl6tWU-qNYdU_CcUonT-dOFSQwzHpH5NEa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b154b3e348.mp4?token=RwCdTsxl53N_MzB8enyN9PWMnoILf0ZwCzAi-rKfDW1HmN2qUVyt12NeTdYGD-5JuZSMzROBL1GeqER3zjT5nTGHf_jIKqeeJg45gzfGy8ewEtdtxW1yQDYp2B0XkeiamIuz61RaEW9odULVlev9wDxZJQKINVkq1s4Y3GbTCrGyEh6jJjHk45lr_J36EO57JconvujNelTcEru7mY2OWFC-DaO-Exg1TwmxtWMYi1_wsGBZ29dxl0sigz1PJ7ERrbxIHyGErTY6pYc91kZoPtKMZrn_cu2DrW3iOGA4Oc1nVmuBplkZl6tWU-qNYdU_CcUonT-dOFSQwzHpH5NEa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم مردم گناباد در شب ۲۰۲ همچنان بااقتدار بالاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/462887" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462886">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUNX29NzSsGJitT7SajXb99PNQ7wm302zxBeaV6LO6AqtdnzyJWan03BFK2Ex7Jq2k64QgNMt4acbikm_GCg9sm3MR0F6HxbprKRh4fpi9oJFrUDmVZByrWhSSl0gZGFaG21rg3_bPqVM4VyGQtiwedUYSIQxKE4N_XFNL-7HUwc7U8Ob5FFPt4wEPNYQLrm5NBlVlqQOWLMhLw49R0pMmIETj4iYiwsmLm0KQXC_UQuD1CRe-sFPl6QIYUGjNRbHce6S-FmY6t6wF6gzn1h4XE-TbvX1rS3-FBX95ICxiTh3NxXigtOoqI5DgqpETkQ5h7EcX0tlPL_G60DpMulOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال لرزه بر تن رقبای آسیایی انداخت
⚽️
استقلال ایران ۳ - ۰  السد قطر @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/462886" target="_blank">📅 23:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe2c81d8d.mp4?token=leWJaVIV9lbGjLC0Q8o98SzgCDQOp87A0EjM--DFGX4IRmUTmHxWk5jxkfovfaaObGIGm0_80JiCojE60P2kg8vFqMiTK1bWjP_MzpNwjB4bI-YWjyKBRXBMywGXxP0i7BOZab4T4_AEkto4xu_m_CyPFaI8iHOW3wvHan79YAuLbcULEvvbYKhmtvxp6qso4pUytbFg8WWZEMdXfreo6eT4RFZREVoqXpfqzzECMrdttIhbUcH5XwBPamJd9H3zMR8gSGF0qhnp5cJpma7efsmsodOQvgGA_eH_bDopfbuwTNuLGA_blcuvF970JRJU64wr2930X91w_j9biDXcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe2c81d8d.mp4?token=leWJaVIV9lbGjLC0Q8o98SzgCDQOp87A0EjM--DFGX4IRmUTmHxWk5jxkfovfaaObGIGm0_80JiCojE60P2kg8vFqMiTK1bWjP_MzpNwjB4bI-YWjyKBRXBMywGXxP0i7BOZab4T4_AEkto4xu_m_CyPFaI8iHOW3wvHan79YAuLbcULEvvbYKhmtvxp6qso4pUytbFg8WWZEMdXfreo6eT4RFZREVoqXpfqzzECMrdttIhbUcH5XwBPamJd9H3zMR8gSGF0qhnp5cJpma7efsmsodOQvgGA_eH_bDopfbuwTNuLGA_blcuvF970JRJU64wr2930X91w_j9biDXcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انیمیشنی از جلسهٔ شورای امنیت سازمان ملل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462885" target="_blank">📅 23:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f6d0aef8.mp4?token=Uwoc1yJ0I8kXLUJYl7mQ1bsFjKoY7ISN5eSHm1bwxx3ySCQMkeePr9JcdTqbRPGbjFXqBpCrrENLm5Md9pAT0ZOFcnDwmb85oTj61qD9ECvDlK-Z8p6yydB8_0faIjA89Yn9gQzqq8C9YFvSk_GK3UwfwPJahNXmO_bdARtPLqsL7EEjvLg-HZtakwYXnerFjBFtUBQnPwpkPpIpd8W8IteuOKPiQ1GfGhxklEruNaYa8funTOgBKKL6dcsT5QyuFpXmmMYs2ZJ0jSSeHY2Y9j0Go0T62x3w4m0mZYPARgDobdSMwywKgkQpxvDbHXCZaAyyPzeKcrADUbMR47Rd0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f6d0aef8.mp4?token=Uwoc1yJ0I8kXLUJYl7mQ1bsFjKoY7ISN5eSHm1bwxx3ySCQMkeePr9JcdTqbRPGbjFXqBpCrrENLm5Md9pAT0ZOFcnDwmb85oTj61qD9ECvDlK-Z8p6yydB8_0faIjA89Yn9gQzqq8C9YFvSk_GK3UwfwPJahNXmO_bdARtPLqsL7EEjvLg-HZtakwYXnerFjBFtUBQnPwpkPpIpd8W8IteuOKPiQ1GfGhxklEruNaYa8funTOgBKKL6dcsT5QyuFpXmmMYs2ZJ0jSSeHY2Y9j0Go0T62x3w4m0mZYPARgDobdSMwywKgkQpxvDbHXCZaAyyPzeKcrADUbMR47Rd0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهمن عظیم در قفقاز روسیه ۱۷ کوهنورد را به کام مرگ کشاند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/462884" target="_blank">📅 23:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd35afbe7f.mp4?token=StGdZH4N-OQO_9jOMHJY14DSiAapkpE62awwutFV3_iVk8nVXYqwvq9wGRwvCwWzFEmosNLOzfmoCPGO3X_tfA_cfjrcQEZnoYtQMbV2MtcB6kfJbmiy1cruIa8lTO7I_zS57iO5eYYEuQrLZoxlnpGXgb6X2HYQmY5LVVZAQxu9-zwpMvHpK_BfhVb_P962wIHRrqi_IYPDEFNR41RrK53mkEkK7w9gOn6RjPhmo5-znT3Ovr3gukcS6iifB6lDqR6jJXJQC7R180DU_sS8JnEzCo8K3f_Kyc6dVGzttIEkHUvn5w3S7XyHgo5Ef5bYPeNFw4v-aY8SO0DOVXhTHW27B9r3FZJ-PSLrFIXyYXbqGPRfQMdHnfCx3FZq67SFtP2diKXCNc48v4vnzqHooNL3qW7BfUSWraU6Dz5bHG2JvPBp8lgJDMkToBumvYPKhJCutLopHxEP-MoB3iXlwqiWlqCH6GYq7hg9QFcCIraK2yWE73HvyspuTxXht7-FSOBeuESjFL2e0KO-L8MIaSoDKWrkvAmQbtkIfgBqrEYzy8xsloGKZmHBas2kKbySlYlUqOuuTB-8x-hVfai5rm_4VhVuRr3IsUNdpJxzMo4dz6yVrv-5xuv5s8DCxm_IkvX9F8f0yKBw-z94yBnDlyoT9uYREAFYQHjReHXSh8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd35afbe7f.mp4?token=StGdZH4N-OQO_9jOMHJY14DSiAapkpE62awwutFV3_iVk8nVXYqwvq9wGRwvCwWzFEmosNLOzfmoCPGO3X_tfA_cfjrcQEZnoYtQMbV2MtcB6kfJbmiy1cruIa8lTO7I_zS57iO5eYYEuQrLZoxlnpGXgb6X2HYQmY5LVVZAQxu9-zwpMvHpK_BfhVb_P962wIHRrqi_IYPDEFNR41RrK53mkEkK7w9gOn6RjPhmo5-znT3Ovr3gukcS6iifB6lDqR6jJXJQC7R180DU_sS8JnEzCo8K3f_Kyc6dVGzttIEkHUvn5w3S7XyHgo5Ef5bYPeNFw4v-aY8SO0DOVXhTHW27B9r3FZJ-PSLrFIXyYXbqGPRfQMdHnfCx3FZq67SFtP2diKXCNc48v4vnzqHooNL3qW7BfUSWraU6Dz5bHG2JvPBp8lgJDMkToBumvYPKhJCutLopHxEP-MoB3iXlwqiWlqCH6GYq7hg9QFcCIraK2yWE73HvyspuTxXht7-FSOBeuESjFL2e0KO-L8MIaSoDKWrkvAmQbtkIfgBqrEYzy8xsloGKZmHBas2kKbySlYlUqOuuTB-8x-hVfai5rm_4VhVuRr3IsUNdpJxzMo4dz6yVrv-5xuv5s8DCxm_IkvX9F8f0yKBw-z94yBnDlyoT9uYREAFYQHjReHXSh8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۲۰۲ حماسه‌آفرینی مردم فاروج خراسان‌شمالی در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462883" target="_blank">📅 23:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc472d17c4.mp4?token=BmPMfZisR8naE_8QIr7XmTbI48Zax3kT9gqDh_nIadV2Dh7w1UDdEQfS7TNO-lt9Onw_uKG_cA75QcnpczIW7hFRpMVwOGnSDy0yu4jA3dTcmTqA5xBroaP0NBrp3mxOT5y1Tw3cr4aAhUbSo5r-ACTCyedFsVhci_35DLCKtYTObewSjd7JRyIfoj6rvb3stpr8XLsykb5Ua3VbGGYPbyGiuxA44kbRr5qrdQCaJa-gnF6b8l_XMCUiy8QCMmRi_5hPbgmbZLbGIyXsrOJ3CR6y7QHirp2LofZEdSr06SFvMQM7hdQoq8JGXnpqDyOVvYZdWssWwJjpLnWDpgxREA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc472d17c4.mp4?token=BmPMfZisR8naE_8QIr7XmTbI48Zax3kT9gqDh_nIadV2Dh7w1UDdEQfS7TNO-lt9Onw_uKG_cA75QcnpczIW7hFRpMVwOGnSDy0yu4jA3dTcmTqA5xBroaP0NBrp3mxOT5y1Tw3cr4aAhUbSo5r-ACTCyedFsVhci_35DLCKtYTObewSjd7JRyIfoj6rvb3stpr8XLsykb5Ua3VbGGYPbyGiuxA44kbRr5qrdQCaJa-gnF6b8l_XMCUiy8QCMmRi_5hPbgmbZLbGIyXsrOJ3CR6y7QHirp2LofZEdSr06SFvMQM7hdQoq8JGXnpqDyOVvYZdWssWwJjpLnWDpgxREA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال تحصیلی جدید و جای خالی دانش‌آموزان میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/462882" target="_blank">📅 23:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIvvjjJD8mDNimtwV29-eqJxZEicoSnYoIVcCOZiS5AGfAFz9-uHB7Z8kZa3ajL6971C5z1YtvXQB30_AkTBSO9iubmgSRpRgQq8yad6jj1qe1HPhSRCIPR0_tB3YDre3wMQB42FIVws5R7vb8kwUeyBqLu7-c5ubmBqhnTdfqHjvNmRfJxAe2q0Ctmu3U-6A4FpnKdrJR2tKj2OuVd7ivKYWJZWMCYi5Imkp4et2Wt62zUHT60wNkFuBt_EMaEs-r5uciJk8KBnXiNb4qJwO1Fv6fqVLg1LykZ-H2djL2ub2RlYSkSQp8NitsfFDvUE9lsQ_6Z_bN6CqcO-nttdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ورود ۳ رسانهٔ بزرگ آمریکایی به کاخ سفید را ممنوع کرد!
🔹
با اعلام ترامپ، دسترسی «سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو» به کاخ سفید به‌دلیل آنچه «انتشار مداوم اخبار دروغین و سفارشی» خوانده شده، به‌طور کامل لغو شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462881" target="_blank">📅 22:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiP8JVW9Z73zZ4BkKx-N8aPWuhnoAAV8dJln32PrIAhSEkGlJxVW722w7_bFYLDK4w_NSE1AusPikqoqTFqpcpxx0H3QjoHSGHyjXcAHiJGXa19ihqMJP8AfK4mgEDPnelvYUv0Nw-jq9eqq7YPxKBt2How2_eI-ZeBrdQVvCJjoaZRTtqKQycDw7q4vYBWFaqFl1HVIPQihgqbWKbOhwY1S1C4mKqwXxYnu88TqCcPypuLjeKk0WJf8ZHB5XR3oPA_GNzHGb3hLEqNilJXsfX602v5V2DBpESU4ZnydXdoWPjluPCxDIhhahHKLQNYdjwBPe9FVFBmdS93uVPxSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDVzge2eLISsSMUSOnVszSLlce7vmFQrmFXDlnlmN9nXyBu3sKmPL191avIeAqTNpQOxyAZtBd-TyNIR2lJ0Gy_1htLpLD0BoxpB6f9WC4J9QjXqg-gGp0Er_SJP5yOVScSxI6QPe5ba3NmlQpPZtQdO2CnP4IQmp0GN7OY0GV_b7cHgvGsZGb6UUtkQTRS9H965SgLeiqCTgbRahOZE0KS16vO7RWN5cw74V1JMlad4h80alcvsn98jMA_jiS4S5T4t0AyTgakZti4E5z_dSIFfM-O_MXl9s7N-M4cFRGdwaXFZs_f0TPRLAntVfejvXPqTVR1SMg1EXQMN5pWk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L98vRFq6Eladq70CSQLxRIgTcHDDx-y5xVfS4KHQJ0pBEdVmurXW-DpBQn9aI9XNHJNXDbF-p7tem8uXrZ-z2F7LzsK9C49a6cL1V_3KTTb1XB6-O5JPU2rBtgUaWnrruoYVYGPTy_drdDVjXCOqUsu1KVuwL8yBlmeMNoLW3AbL3M7eF8wjCOi5VkMiGnTmIIpvTiETG5jLoffXNCy1eurUakVThWA6QRRy0aCBLKNqd4xkiQiKhOYqq4KVodnq9ehignd2z6-FftQtbB-AHV_nlxz32zCqcvYfVOOWICQrqu__cokm0UvYRVLqA1ff3nvRJvVkJJZR5yjBqdn0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgteko0JqmX_ReGOa0twy2YqeKVrMi71cCztwJpKoOcUAPTkRnqUPzBq-HfwzrzRZSiIDhTl02l7MOmMuAbnH5SYoBTnGYC0amNypHBamhFA5yqsZ9oVi9rg8hsGwLQEcrjb-oEbbt7ymWelinJM7hn3pLzsScpAwcYv-nHzA0SvqAd3vXYfXkDDRPk1BPT07Y7DL65x-2W8vbe6-QhSgZvanhkvfgJ0THycfOWeIlyWVAuulkzxS1cJHQ8E4YER6aCFEq42uNB3gQnaXYKFqufNqnivPmbFzQYDoF-TePn6BoRZ3ChBjm1J-MeOnbiMEBrpSXhnfeMqmMrjrKhFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vjj66bzAvdAAOLkGCvJfC0s_fU_XbuyGYwrh_P8kaqifqpAYb6SkJGN8fGXG0m7_0LezhTH32P3P9Tzqw8GE-WDTYdSqjTuB0ZqU7p1lYNso8ICh6_YOmF4LDxJydf1SYngXmosFnQGkcdCwkQyqY-fEW8kqsxp2MlJyR05pLBHU_D13wjTOZ56GVByI42pT6MM3GvzC-3iIqjg5VUvG11ihYpKwWfP5CEWzTL7GvB5hczwY3KFLgjhyUjnU2UF0lJyW-qYNpDm9zPhT4mY0lrSLGfAkqjSorZIDvnqy5_hE6zdnGhz8w8-HE8WBUPHAy7dWpDLA0gOj46qH91aANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRRbrDgW5X5czkqeiikIPVf00JF4kS63ECivBPY3n5k_OS7sdLBzYv2lqk4WbCU8FGJ11prV7PpW7RvCl2nuxKLnaTiFfCi743cHdSzIiyKiwVVfhtG3rP5vnA97oU-1NWFgw-PRcXd7jTHOD0jLRrRGckGxk7lgG2WFs6uXIQcFQm5oytnYniGIkGWEKxEUZ2asFBVjioCYXAKfaXjQv64xxwfdYHm3mVFmQp66Yu4mL5poFOUbNO6XIK67s8Hvf5TRGg7EcntxWEs6SwLaO4baowQSiglJwjMnlwja5lSq6roNQjb7X-eIn-j4q_JlWnjjAFkjbPI7waSjo45AGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzvJswYG3mOHjNK-jG6-CHN13kRyEDR_H3eC1X17Vto7m5aLy32F6ITIxH3HdFdZgA0vOPfNcNlU3Ee_g6r1aQg9Bj515Zrpm5bkT274O-CUnbVniUf2ku9ALpym44T9tPmm6nr5MUkdp42RtJYnPH-7Y4DaRyWPyVZFGBcqxlpof9B6ItsXqm5n9W0n13d_3HpAkDVKvq7GUeEfy_YEZCfcI10mB6Em4Bzyw0xZy-HquUzLARCnq1WjCQuHJ3MfuvVmZE-lun9xQT-g3V7fRbgsTKLMr_MmXRmFqVnjJkHFxWr-z_iS0ifrexmPgBZh0mX_XYy8eBpKvR0xbw7Kdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cg5ho4fzNEOLvP2oWmS6ho8_kc24QEupNhyCbAWLvRo2nZlytMYOKxSmuM9wXREECACtpl6EHIfFXWvt4Q-iyX9zFodEbKYLsweWt9j27Goi3zDepGZTSU8-utofeiBOs4cmHSiUceYhvPhK5wR6nmE-_gPhaMDySD3AujDPDJKVbh2njXF3jUgYZFtrD6ms9XfaO_pRNUa0g-1YU0z0kjm9Ii5E97g8UTrA_kPyM9XnGFDenrC3wFa-5dMOyAu3iiXDEcuJLC8AdnmsvDD719p3CxKcKLxusQPn7zAknMBwAxBCN9y5BfJ2b6UbQFiZJs2sv0VvO4Dc8Lni4-NT5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایش اقتدار ایران با ۳۱۳ هزار جانفدای وطن
عکس:
الهه آسیابی
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462873" target="_blank">📅 22:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-F6s68SeYUJ7dcnu_0t7cu71QZ6ZJ8ZghPe_tfmFhCk9EDQ2aDD9_u13GXxqrdKBQBw2U6tPJJZjXBjF1H5e_hS6qt-Jc7hkfMbmAp8CxE4L_SVpJ5FkmbFmu2DDgoQrmD_CIUCJytUonNbgEXXO4NUiHR7nBgyC86UiOo8spGEC0mJIs8qle-6nM5TNab0bqQuOb8RPn3yeG1zCEAHoBQNCzaT7kCydyzMzdZSgqOd-8WP4xrNbAYvafsgMKuMMU4Xaaf0gxW6L0vKFVfBfOnobmJOUtypqTOPNX7kQ_X-k0LIG47pr7tnODnjJd2Ed57AFO42BS7IW_t8fAqeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: دروغ‌های وزیر خارجۀ آمریکا در رابطه با مداخلۀ ایران در موضوع یمن-عربستان، نمی‌تواند جای واقعیت‌ها را بگیرد
🔹
سخنگوی وزارت خارجه در واکنش به ادعای بی‌اساس وزیر خارجۀ آمریکا مبنی‌بر مداخلۀ ایران در موضوع یمن، نوشت: دروغ‌های مارکو روبیو نمی‌تواند جایگزین…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462871" target="_blank">📅 22:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462870">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fINTfo0NnrUamRmDFovo2_SxIpussrjrhaTicJe3cIn8ULfkc5RQ4qg7Fh93lKBixCb_DCplZVzqLy9nrVW7-Z4bb7zsMCg8y7LbF68oXPqTTktSlCSlV-u8TmnErSkNjBHJkcq8kbbGSJ4hAmSyolqTBOKnrkTpxx77w7dy9BaHs7a6eDh0qTySlLYDidJuC-1FwRDW03K64HOVcxKSAro9nKaKgXNALPcRRIBB6woOimdSdk95w2sAQpcUt3nuPEPXaDzzrRfWpsYRdSEUtgoGvPILIt5I5u4MF1ir21uCb_5hnDoTSU_fE_jTQIQ5DyNjs_GCeH3a9Zv9fOc55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۱۳ قاچاقچی مواد مخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: در جریان ۳ عملیات مشترک فرااستانی ۳۷۱ کیلوگرم انواع مواد مخدر کشف، ۱۱ خودرو توقیف و ۱۳ قاچاقچی دستگیر شدند.
عکس: مصطفی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462870" target="_blank">📅 22:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462869">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQAlVqkGbNcjZRSejkM1zFZfAPKP9UxfstNtMW7yPc_X_mREp029ra6uv6Rk267o2dx5GW6GUfOZVaj0Y1ssiPGi8QVH8_X9JkDDWUG-jMFA43WdkJnBYn8GV7RMwrkBS-dZVwFpCQBCmVBSPvRSkn4NVoRec2xentLbq1H0M1IXe3oyWOiY-A1nnjiCCvz90MtJ2RUBf3V7gkTXK-ufSljGFP5WKoWPTc47JkOIn2jTHYkFw3RLysOEX49FrX_kBqIQl3y852Hkms2sisgT8-FhF3ag-MKx1qbTlX_Z2xRs1ZJppI-ZOYm_g5vbHa8khzXI90kA1d0pAgk2RO1Dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط سنگین مهاجم خارجی استقلال برای بازگشت
🔹
داکنز نازون از طریق نماینده خود شرط کرده که ابتدا باید مبلغ ۶۰۰ هزار دلار را که بخش بزرگی از آن مربوط به پیش‌پرداخت فصل آینده‌ و قسمت دیگر طلب باقی‌مانده از سال گذشته است( طبق ادعای بازیکن) را دریافت کند و سپس در…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462869" target="_blank">📅 22:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462868">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff2597e4b.mp4?token=bvApDFaiwc2lSnXXISz28ovXFc7Cf7MtokUCa4RMvOadTV2SD2RaOKEKqcJA4IXzWxeVLwB7YGdTjGZZjddWLyv7aMergD8806x-vMAS9JrGL5BSb15LNUetgrnWrxfcRVQaNpNMxkzMeC32V3WjbV3Z7VXSiEuajq0JY_ox0kYKlQFarwtlVChTCTvwsLjar8jODEalmBCuSy1r31oaBoiknyQAQPLj4d5rVKPC5TDlv6FaJjDUjeyNgTkLleKdOU_wIg4xhLVyD8SwbASXKvRx9Ei-gZemWoDkCGNmmf15EB7bPX5-4WJlnnSqAIKWCBrqs0HZXxURJkUiGeUogwh8j5YdmGr7wURAbhnAxgeFsibKjy-n9-xYe3wxXLfkrxDplQ_r0b6oUh0nYe4tFwNVRtW4qTlSrK_tgHOmC9TYlf_70s-hpZUOqt2PdHRONCxb7-owMrTxK3E2_yKPOwNDxL4H1EBT4321gKm10n-IwfFz6IFqW_op7aaKQJGfDhDmtFfY0d4sPyjk_wmiJBMsjWzBWApYUwOhVcaaYeZgOYQt0tibpUJ-7SacdYml95bjRlHrcFZxzTqig1s1QvkZR5LK-oy8r63V7Iz_wZwGoMdBhO3Gmp7mnHxL99NyMtgsDrTLHNWQLta9pODEFvfrEk-fQ_sWxO7VIJyjzDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff2597e4b.mp4?token=bvApDFaiwc2lSnXXISz28ovXFc7Cf7MtokUCa4RMvOadTV2SD2RaOKEKqcJA4IXzWxeVLwB7YGdTjGZZjddWLyv7aMergD8806x-vMAS9JrGL5BSb15LNUetgrnWrxfcRVQaNpNMxkzMeC32V3WjbV3Z7VXSiEuajq0JY_ox0kYKlQFarwtlVChTCTvwsLjar8jODEalmBCuSy1r31oaBoiknyQAQPLj4d5rVKPC5TDlv6FaJjDUjeyNgTkLleKdOU_wIg4xhLVyD8SwbASXKvRx9Ei-gZemWoDkCGNmmf15EB7bPX5-4WJlnnSqAIKWCBrqs0HZXxURJkUiGeUogwh8j5YdmGr7wURAbhnAxgeFsibKjy-n9-xYe3wxXLfkrxDplQ_r0b6oUh0nYe4tFwNVRtW4qTlSrK_tgHOmC9TYlf_70s-hpZUOqt2PdHRONCxb7-owMrTxK3E2_yKPOwNDxL4H1EBT4321gKm10n-IwfFz6IFqW_op7aaKQJGfDhDmtFfY0d4sPyjk_wmiJBMsjWzBWApYUwOhVcaaYeZgOYQt0tibpUJ-7SacdYml95bjRlHrcFZxzTqig1s1QvkZR5LK-oy8r63V7Iz_wZwGoMdBhO3Gmp7mnHxL99NyMtgsDrTLHNWQLta9pODEFvfrEk-fQ_sWxO7VIJyjzDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در شهرهای یمن به خیابان‌ها آمدند
🔹
میلیون‌ها یمنی در ده‌ها شهر این کشور به خصوص در میدان السبعین صنعاء به خیابان‌ها آمدند تا حمایت خود را از نیروهای مسلح یمن در برابر عربستان سعودی اعلام کنند.
🔹
شعار تجمعات امروز آن‌ها «برای حمایت از نیروهای مسلح، معادلهٔ محاصره در برابر محاصره و افشای دروغ حمله به مکه» اعلام شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462868" target="_blank">📅 22:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462867">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptBzG7_XNzX-WUawdz--jvFXxNxxiBedUA2oBRLpO4FJ_vvVkUW1uKGoYBJgf1ln18A8TCv5w5nHBa0c9ETAAyhqg613igXscc9m3tTbDbu1DmCMbSb6jXZsQ9bnSMmDWA4z65QxizEUVA1haCIg6S1s6eJecMdGZf684QMBK8gIvu8nvIBLqxx1pWu1T6AGe5XjO8X-oi35JkN__I8Bci0HEMGiw8s-3wkF1iDyFolfJiwIECCyavuOfhX2orHMkIDPiR7gN64ZScBVR-Up7XaLS5s8t1YQi_d1NBlc0S1WPYRrifsFxh5hsXhRYpAhdSkjlARONvApAdbe1yGaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ حامی ترامپ به رکوردشکنی مخالفان جنگ در آمریکا اعتراف کرد
🔹
نظرسنجی فاکس‌نیوز امروز نشان داد که ۷۱٪ آمریکایی‌ها معتقدند که دولت ترامپ برنامه‌ای برای پایان‌دادن به جنگ علیه ایران ندارد.
🔹
علاوه بر این، ۶۰٪ آمریکایی‌ها می‌گویند که اقدام نظامی آمریکا علیه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462867" target="_blank">📅 22:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462866">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
تو را به خدا وضعیت
شاهین‌های تحویل‌نشده
را دوباره پیگیری کنید. سه سال و خرده‌ای است که منتظر تحویل خودرو هستیم و هنوز خبری نیست. واقعاً این وضعیت قابل قبول نیست؛ مگر کسی نیست این
خودروسازها
را پاسخ‌گو کند؟
🔹
شهرداری اهواز
اعلام کرده بیش از ۳۰۰ نقطه از شهر با مشکل
جاری شدن فاضلاب در خیابان‌ها
مواجه است. با توجه به نزدیک شدن فصل بارندگی، ضروری است شهرداری و آبفا هرچه سریع‌تر برای رفع این مشکل و جلوگیری از تشدید وضعیت اقدام کنند.
🔹
خواهش می‌کنیم به مشکلات
شهرک ۲۰۰۰ واحدی مدائن در پاکدشت
رسیدگی کنید. متأسفانه هیچ‌کدام از مسئولان شهر پیگیر مشکلات و مسائل این شهرک نیستند و مردم با مشکلات مختلفی مواجه‌اند. این شهرک عملاً به یک
منطقه جداافتاده
تبدیل شده است.
🔹
خواهش می‌کنیم به وضعیت پرداخت
وام ودیعه مسکن در شهرستان بروجن
رسیدگی کنید. ما مستأجر هستیم و به این وام نیاز داریم اما
به هر بانکی مراجعه می‌کنیم می‌گویند اعتبار ندارند
و حتی اعلام می‌کنند چند سال است وام ودیعه مسکن پرداخت نکرده‌اند.
🔹
نهضت ملی مسکن
برای ما به یک کابوس تبدیل شده است. بیش از چهار سال است که منتظر هستیم و من برای تأمین آورده، حتی مجبور شدم چند قطعه سکه بفروشم تا بتوانم چهار مرحله ۴۰ میلیون تومانی را که چند سال قبل اعلام شده بود، تکمیل کنم. حالا بعد از گذشت این همه سال، برایم اظهارنامه آمده که
یا ۸۰۰ میلیون تومان واریز کن یا امتیازت لغو می‌شود
! از طرفی، سامانه قوه قضاییه هم دچار مشکل است و حتی امکان پاسخ‌دادن به اظهارنامه وجود ندارد. واقعاً سؤال ما این است که با این شرایط اقتصادی، یک متقاضی مسکن ملی چگونه می‌تواند یک‌باره ۸۰۰ میلیون تومان پرداخت کند؟ ما به امید خانه‌دار شدن وارد این طرح شدیم، اما حالا نه می‌توانیم پولمان را پس بگیریم و نه توان پرداخت مبالغ جدید را داریم.
🔹
با وجود اعلام
آموزش‌وپرورش
مبنی بر اینکه نباید بابت ثبت‌نام در مدارس دولتی وجهی از خانواده‌ها دریافت شود، در یکی از
مدارس شاهد شهرستان رفسنجان
به‌گونه‌ای مدارک موردنیاز و چک‌لیست تایپی به والدین داده می‌شود که هیچ اثری از مبلغ درخواستی در آن نیست و فقط حق بیمه ذکر شده است. اما در نهایت مبلغ قابل‌توجهی به‌صورت دستی اعلام می‌شود و حتی گفته می‌شود در صورت پرداخت نکردن،
اسامی دانش‌آموزان به‌دلیل عدم پرداخت در کلاس اعلام خواهد شد
. اگر دریافت این مبالغ قانونی است، چرا شفاف اعلام نمی‌شود؟ و اگر قانونی نیست چرا با متخلفان برخورد نمی‌شود؟ متأسفانه به نظر می‌رسد تا زمانی که خانواده‌ای شکایت نکند، این مبالغ از مردم دریافت می‌شود و حتی مشخص نیست نظارت و حسابرسی دقیقی بر نحوه هزینه‌کرد آن‌ها وجود دارد. از طرفی
خانواده‌ها نیز نگران‌اند که اگر شکایت کنند، فرزندشان سال آینده با بهانه‌های مختلف از مدرسه کنار گذاشته شود
.
🔹
واقعاً نمی‌دانیم آیا مسئولان این مطالب را می‌خوانند و به آن‌ها ترتیب اثر می‌دهند یا نه؛ ان‌شاءالله که این‌طور باشد. عید غدیر سال گذشته، ۲۴ خرداد بین خودروی لیفان و یک دستگاه وانت نیسان
تصادف
شد. با وجود اینکه مقصر حادثه ۱۰۰ درصد وانت نیسان تشخیص داده شده، هنوز بعد از گذشت یک سال و سه ماه نتوانسته‌ایم به حق خود برسیم.
قاضی به پرونده رسیدگی نمی‌کند و حکمی نیز صادر نشده است
. ۱۵ ماه است خودرو در پارکینگ متوقف مانده و ما مرتب برای پیگیری پرونده به دادگاه مراجعه می‌کنیم. در حالی که طبق نظر کارشناسی حتی یک درصد هم مقصر نبوده‌ایم. این چه عدالتی است؟ برای احقاق حق باید به کجا مراجعه کنیم؟
🔹
حدود دو ماه است
آب شهر طرقبه مشهد هر شب از ساعت ۱۰ شب تا ۶ صبح قطع می‌شود
. با وجود پیگیری‌های متعدد از آبفا و مسئولان منطقه، مشکل همچنان پابرجاست. مسئولان می‌گویند مشکل از برق و پمپاژ است اما نتیجه برای مردم فرقی ندارد.
🔹
آزادراه حرم تا حرم
در مسیر گرمسار تا قم و بالعکس،
دو بار عوارض دریافت می‌کند
اما
وضعیت آسفالت
بسیاری از قسمت‌ها
بسیار نامناسب است
و به خودروها آسیب می‌زند. از طرفی تردد خودروهای سنگین در لاین سبقت نیز باعث ایجاد مشکل برای سایر رانندگان شده است.
🔹
لطفاً پیگیر
وضعیت چاله‌های حدفاصل تقاطع روستای خین‌عرب و روستای فیریزی
، به سمت محل باسکول و تخلیه زباله‌های شهرداری باشید. خدا شاهد است وضعیت جاده به‌قدری نامناسب شده که برای جلوگیری از افتادن خودروها در چاله‌ها، باید در چند مرحله مسیر را تغییر لاین دهیم. این جاده کم‌عرض و آسفالت آن نیز فرسوده است و تردد در آن خطرناک شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462866" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462865">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68556d2192.mp4?token=hwifWgPVHeI-LDbX9Q3TgfNEcQkC88zdjnxz2tGA95vXZIpa8USIM8vec2HQxBSEw_dmjik0ilIlZUoLsvksbe2HqsQ3K7K8OgV1qektB5F6igO7_FaUum5SCqLYHwyGdxiPazQltBvJVdOs4BDELBTtL3awNxvtCC5swXix0samz8Sh4kYi6okMeRZZSbdw2nQP0P0xH1Z2mfiqogSg_jkUqS2ZRjcWhtlWdHdXfQyIOqpu-KCBLjO9koZrVuUQOP99YJ4AoE1ie-u2gB5BrM6vVj-_TrLOKBiGRIRI7IpXCdEW-w_eqe9kMDRiJN1MstZvgaAEcqgheMD8VsOTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68556d2192.mp4?token=hwifWgPVHeI-LDbX9Q3TgfNEcQkC88zdjnxz2tGA95vXZIpa8USIM8vec2HQxBSEw_dmjik0ilIlZUoLsvksbe2HqsQ3K7K8OgV1qektB5F6igO7_FaUum5SCqLYHwyGdxiPazQltBvJVdOs4BDELBTtL3awNxvtCC5swXix0samz8Sh4kYi6okMeRZZSbdw2nQP0P0xH1Z2mfiqogSg_jkUqS2ZRjcWhtlWdHdXfQyIOqpu-KCBLjO9koZrVuUQOP99YJ4AoE1ie-u2gB5BrM6vVj-_TrLOKBiGRIRI7IpXCdEW-w_eqe9kMDRiJN1MstZvgaAEcqgheMD8VsOTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از تجمع ۲۰۲ نظام‌آبادی‌های تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462865" target="_blank">📅 21:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462864">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ae86d509.mp4?token=nS0vmcaft8knDNjf_mJnNMyvVqoWcRvuFP_f9iR-MGu8JEkdqt53wH8St500VguqTcO4mXeYoGY6UXZBuECKcVx0o8bBv34iC4e8qVOTRzXuAHtcROlLuAqB-lAyLi0v9sQdMEXQyeHjBv1Xhdu__22u8j6i3yiqOO3sghvJIGvlSyD-Vey9Sb10fj9iqYPInk5LZdZleQhT93s8JQ9N8QjoZXYchHZeers1e7uvVETf7ccqGNvsYWOnZqG8CYq4WwMaM8R_dNkHfroFFuZpViDxs-juu1Ydh6uy8ekNwGlE2qS0MELAUfYngoUEIDDT5jsfeOmeHHH65iJy7FvHPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ae86d509.mp4?token=nS0vmcaft8knDNjf_mJnNMyvVqoWcRvuFP_f9iR-MGu8JEkdqt53wH8St500VguqTcO4mXeYoGY6UXZBuECKcVx0o8bBv34iC4e8qVOTRzXuAHtcROlLuAqB-lAyLi0v9sQdMEXQyeHjBv1Xhdu__22u8j6i3yiqOO3sghvJIGvlSyD-Vey9Sb10fj9iqYPInk5LZdZleQhT93s8JQ9N8QjoZXYchHZeers1e7uvVETf7ccqGNvsYWOnZqG8CYq4WwMaM8R_dNkHfroFFuZpViDxs-juu1Ydh6uy8ekNwGlE2qS0MELAUfYngoUEIDDT5jsfeOmeHHH65iJy7FvHPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از قدرت‌نمایی امروز جان‌فدایان ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/462864" target="_blank">📅 21:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462863">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9kFIEGsOW9lEEt2umJ8wKBD5YVuUtD1tnDdg_ZakeN6BEYB1zNBW6ppDCCJUufXl7OQkLS7XOwTDdoFY9BFVi6ZpMxJo8DUWeKM_3L91_i3FAB6Ys6BWc9F4x6LgmXQt14rTEkraP0nUiHJ16GjglP2f_OlWS9n1VUR1gCv7_gkAU-bj9fBUgOvtp_YonQugOKHUuSM-SxL1EuadUmUy2kCMPLoVjIzf3hkL3miXN4pRBjL4QtRHON10xhDSY1oYH4qFQMY5CmyXHB5VfObwFa-Z-aF2beAcK8YpIXWhmYuzJpofWeurg_KWNGeSgTym00MCRwI95L2gMkcu1sg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال دست‌یافتن چین به قطعات حساس F-35
🔹
نشریهٔ پولیتیکو: این تابستان، قطعات حساس هواپیمای جنگندهٔ F-35 به‌طور غیرمنتظره‌ای به هنگ‌کنگ منتقل شدند؛ درحالی‌که قرار بود از استرالیا به ایالات متحده برای تعمیرات ارسال شوند.
🔹
این موضوع باعث ایجاد تحقیقاتی در کنگره شد؛ زیرا نگرانی‌هایی وجود داشت که ممکن است فناوری‌های طبقه‌بندی‌شده در اختیار چین قرار گرفته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/462863" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462862">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbijRk9zwd_XSgBHK12lqQ9Lq5etVN1HjMCa4uh-0yhnlnLUnqhsseBzokdqTZ9HXTg7lJgSLYA9zryhU1ofvTGF4XldRHJgQMlPNTuQCwwLoCpKW6x3gM6FYg6pqVtuJPx7M7OgH63ZjRWO7OeGVgMzomUGyoRKSIz4Hh1Xqe1K5HyFlS02TBVlws9tqA54jF9g9CZj6_R03Yce4HFlVMQyHJYXpwmBQsLGI-8nmfIhBRRal3RHtLZE6d06ZQ2JiGWelRfltI3-liGgfw1GUPR6Ja3mKkQPfQDLfoN76yNiB4D7rdbsZWhgatkEYL1VZylRASve44y6JaDO_DycKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ قالیباف به ژنرال دن کین: آنچه روزی برایتان کابوسی وحشتناک بود، الان به یک روزمرگی تبدیل شده است
🔹
رئیس ستاد مشترک نیروهای مسلح ایالات متحده آمریکا پیش از این در کنفرانس نیروی هوا و فضا و سایبری ارتش آمریکا گفته بود: از این به بعد باید این فرض را مبنا قرار دهیم که یگان‌ها و آرایش‌های نظامی ما توسط سامانه‌های خودمختار شکار خواهند شد، در سراسر طیف فرکانسی با اخلال مواجه خواهند شد و به‌صورت لحظه‌ای ردیابی خواهند شد.
🔹
قالیباف در پاسخ به این مقام آمریکایی نوشت: دورانی که در آن F-35ها و F-15های شما شکار می‌شوند و شما مجبورید گزارش دهید که فقط آسیب دیده‌اند، همین حالا هم آغاز شده است. چیزی که زمانی صرفاً یک کابوس وحشتناک بود، اکنون به واقعیت روزمره تبدیل شده است. با آن کنار بیایید.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462862" target="_blank">📅 21:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462861">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIZ_Ty3Z3qp-MEfVTqT7IKis1QLj6srbeQgWC78SDOQ7fBBiCFaPRUZGOAiVSVAf-51pa3nP1S6xC1o4t_9jPUpbxvY18OreY2Q_0BnrVftJAxsCpU8iFGKQKRrg2R_4Jt-yMEu_qOjQIPIWEeN-ujiRpRDw76QR8RtrvE9yw8ma_GrRqLfPeVQswUnl2SgKDZtsPdusU9BH7ofQptdr_EuXmnQWn4itOc8OPnEcQEsp1ALcwdMpU5kE8wwU0ZBgutXoZSyzgnclmafMm_YMFz-Yw-qYOHheGyOG9VTpA8DhYmYxv92Ra2BSZeVGKnw7fOWSHY_WncFZ0Q3sEh4uHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳ ریشتر در عمق ۱۰ کیلومتری، دره‌شهر ایلام را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462861" target="_blank">📅 21:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAxXPZjm2uZ9OzWsChZ8qhsLa5b9ty2d2cSJgpgyNv9IDUJrJ5j5YLGdTsbvzMc2UkpseKIexcisJ0nQI_cprN1zEDTPQFSC7-RTYzHL6FZocfzN4MmfD47QWYPVNmDOJl0NexpSgP9Z9UbsWErgRLSFcpRh4ZrHiXncwS0spnX09i8PlHkex0J8CJOwyDjAkb_Zuji5111t-d4W50aOsjXWwWIv_8RSQvHlwUD9qwc5TRWQ6CmX3sMy4EhlEA-6i18dHlFLD0SruS2DtC9yojTvbjYO5diqvU8o1_3zS5dwb_SI0Fg-wdTrIcE5rxsN3xng-GT-p0I9Ac-7BZi6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یادداشت کمتردیده‌شدهٔ رهبر شهید خطاب به جان
‌
بازان حزب‌الله در جنایت پیجری
🔹
عزیزان من! از امتحان الهی سربلند بیرون آمدید. صبر و استقامت شما یکی از برترین جهادهاست. شفا و عافیت و عاقبت‌بخیری شما را از خداوند متعال مسألت میکنم.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462860" target="_blank">📅 20:54 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
