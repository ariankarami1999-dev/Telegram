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
<img src="https://cdn4.telesco.pe/file/cQ79wbpHrLoLNW_V08LYYBqZCW7DauVVwShr6iOeZvfqQdj8SSg-QuMkso11oqHTqQ3kA_-RV7rQwWNWbd_IHFnkC2rzvJC5f8KRCUf0ft9FSZ31PPiYFuhXweAr9el7ZlYmsJylD68F1Dl5R0cRVmosC6OFYK5hOxDaagLqNpKLO9rxMsZuq8DPo_xr7XYAxWPVsxPuJ7OwgwsZstWrHJK6vlTukEQzy2amHc6oDbSQS9GRmOTgu4F_oLGQUQawHmhKYo-eiA7WFop5JXz3r1yk_kYn83BgNruI1Eu6Yc0aQsGDmR_pLnuvFR-SvnmcAa6e2pHwqNVtgz6_ndJnBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 961K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-137897">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvHCiZa1VJUf1R7652CDtdtVYYvpZdK1QFWfUsvFLh0C86hHhQkTHvPzagYln3QoOz0qc3BiwsPpXsrYlRCrgf_HQkF6uHOyyQ1hn_ATZjSmjuhbW0eJ9Wzh_BANTjAat4tWdsYsisYC10GE60soA4YCA7VMPmp07cJ342gJw6ClxL-zcYc-8NStYJqr9w9jNRfyo2bM_1_8oHwe42i2Yx8_zOX16yRzvt9DYDGBkkJECjaAcj4hDDFYTItsi8EDGWWCdraTLVp0GW7h0Y_yPa5Fmq5_jJYNQW16Ejm_nJvW3X0QvSP64Ds6WumsFKKSnr20ySPqQpfxPLTCkHfPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: در سه چهار سال اخیر، ما بر خلاف بسیاری از کشور های پیشرفته، رشد اقتصادی خوبی داشتیم. ما الان بعد از چین و آمریکا و هند، چهارمین اقتصاد برتر دنیا و بهترین رشد اقتصاد اروپا داریم، حتی بالا تر از اتحادیه اروپا
🔴
البته که می توانیم سریعتر هم پیشرفت کنیم، اما خطر تورم و نتایجش رو باید در نظر بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/137897" target="_blank">📅 15:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نیویورک‌تایمز: به نظر می‌رسد که ترامپ به دام افتاده؛ او اکنون برای یافتن راهی جهت خروج از درگیری که آبرویش را هم حفظ کند، دست و پا می‌زند
🔴
ترامپ سه گزینه اصلی پیش رو دارد: تشدید نظامی، سرکوب اقتصادی یا اعلام پیروزی
🔴
شاید دلیل تردید او برای شروع مجدد حملات علیه ایران این باشد که جنگ، ذخایر موشک‌های رهگیر آمریکا را کاهش داده؛ زیرا پس از ۱۳ شب متوالی حملات در این ماه، این اعداد به سطوح بحرانی رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/137896" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668353b1c2.mp4?token=A5NbShaCC4xOzZo185EgOrhSsMgHU1bctpKHE0a49T2zsZWwc0YqhbOXAgW2PBryexIojnaiZ927hZ4IQTnUeVkNGsA_P35sO7C_5RNSdcGfIfcPf090aWr8yxDHdR8XaF0lvpQqM0JZfIsubc7oNCHsuZvtMRWJpL3n0FrVQ-YmKaqN2nG-7asXu5xehxzDZCOcL87a7mVVa4u5e2lxffpUzRfpM84FkuYzuvF5MJ8pJbMJFOe6UrY82Pkj98Zk1cAYbzgzP0XKcnqdJ-ZHL1I_vJdvElgPIhmoHLkUlmPHCQ_8p0W3W6R_Sd5BW2oCCa7AmJcmvY-2QxnrfJtqUCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668353b1c2.mp4?token=A5NbShaCC4xOzZo185EgOrhSsMgHU1bctpKHE0a49T2zsZWwc0YqhbOXAgW2PBryexIojnaiZ927hZ4IQTnUeVkNGsA_P35sO7C_5RNSdcGfIfcPf090aWr8yxDHdR8XaF0lvpQqM0JZfIsubc7oNCHsuZvtMRWJpL3n0FrVQ-YmKaqN2nG-7asXu5xehxzDZCOcL87a7mVVa4u5e2lxffpUzRfpM84FkuYzuvF5MJ8pJbMJFOe6UrY82Pkj98Zk1cAYbzgzP0XKcnqdJ-ZHL1I_vJdvElgPIhmoHLkUlmPHCQ_8p0W3W6R_Sd5BW2oCCa7AmJcmvY-2QxnrfJtqUCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد تند جی دی ونس به اقدامات اسرائیل و منحرف کردن مسیر مذاکرات با ایران
🔴
«جی. دی. ونس»، معاون رئیس‌جمهور آمریکا، در مصاحبه‌ای با «جو روگان»، مجری و یوتیوبر آمریکایی، به انتقاد از اسرائیل پرداخت و گفت: «من قطعاً فکر می‌کنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بوده‌ایم که تلاش می‌کند مذاکرات را منحرف کند و مانع رسیدن به توافق شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137895" target="_blank">📅 15:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3afd948ec2.mp4?token=BJ6WhT1h2K8Mv9jMpzV6Br86aamywTH0qgsfdN6f4QswgPNzRgYFT36o0hP5GCcxXtS8484D7MzlcUI8Egtj1KPSOeIBe1pnlT_ubk607Xtouc_ah9jYy0OGhm87wqgrF0loBpnH0S-KpZGWfvdEvKxjThuFctEsZ8X4ar74sh8O8lfpDba63q11MrYveUCwyj1tDEeXj7gmmAAuRybnUMUqf334LPOvT8WaXtPfdj5GVslB6L8DJ8Id9n_Kd3GG4zTynEplYuARXboB8DIvRNwri8RcHGrdUqb2KogUpevr6qdxxRw7thYxRlJw7yNW5KjGAEBQ4Gmhbbd95wOpgrDlV3ukpRKeqG6JTrxKRfjqXqpkX-gMVGNOtjNS3g_ZAZjE2YNPwNwZXf9T99FY62cIuwz6RScmTbyk2Og-uKRHyqWmwX-7trI0vslfKzVCCUGYpgp4e3DVvKn3itxrvFZCREpVk9WHH2qlMGow8CTy2jKD-STfmr1Rvbj1F9Cei7CAGpguAv4BHIh8cpPXuwALQxRIHkUl7e6NH2c7dqzw4eSu0ZI9nHEwJkpSqaFGCQnVuFdV-2CTuvMWlDEjq0IqgvSezC9Esnysk5Wx4aXoGrjvMl39lotKZupnA-jz85dHFHI_YVDrUKAbXfhkeTx4s9YEbVcj2UCKasQnoO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3afd948ec2.mp4?token=BJ6WhT1h2K8Mv9jMpzV6Br86aamywTH0qgsfdN6f4QswgPNzRgYFT36o0hP5GCcxXtS8484D7MzlcUI8Egtj1KPSOeIBe1pnlT_ubk607Xtouc_ah9jYy0OGhm87wqgrF0loBpnH0S-KpZGWfvdEvKxjThuFctEsZ8X4ar74sh8O8lfpDba63q11MrYveUCwyj1tDEeXj7gmmAAuRybnUMUqf334LPOvT8WaXtPfdj5GVslB6L8DJ8Id9n_Kd3GG4zTynEplYuARXboB8DIvRNwri8RcHGrdUqb2KogUpevr6qdxxRw7thYxRlJw7yNW5KjGAEBQ4Gmhbbd95wOpgrDlV3ukpRKeqG6JTrxKRfjqXqpkX-gMVGNOtjNS3g_ZAZjE2YNPwNwZXf9T99FY62cIuwz6RScmTbyk2Og-uKRHyqWmwX-7trI0vslfKzVCCUGYpgp4e3DVvKn3itxrvFZCREpVk9WHH2qlMGow8CTy2jKD-STfmr1Rvbj1F9Cei7CAGpguAv4BHIh8cpPXuwALQxRIHkUl7e6NH2c7dqzw4eSu0ZI9nHEwJkpSqaFGCQnVuFdV-2CTuvMWlDEjq0IqgvSezC9Esnysk5Wx4aXoGrjvMl39lotKZupnA-jz85dHFHI_YVDrUKAbXfhkeTx4s9YEbVcj2UCKasQnoO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رامبد جوان، بازیگر و کارگردان سینما و تلویزیون تاک‌شوی جدیدی برای نمایش خانگی طراحی کرده که به زودی وارد تولید می‌شود.
🔴
نام اولیه این برنامه «اتاق رامبد» است و قرار است در آن چهره‌های محبوب حوزه‌های مختلف فرهنگ و هنر و ورزش از ناگفته‌های خود درباره زندگی و زمانه با رامبد حرف بزنند. احتمالا رامبد جوان این تاک‌شو را برای پخش به فیلیمو بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/137894" target="_blank">📅 15:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137893">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6qim61unEYps80rmtW5MdKX3BYdVl5KwVbfR3OpjjyY5Q4eDW2RVPM_ZiVeSrMVbRLTdp6AYejcGUbpilkuFjFOQhcNjPsbwnLqpMCnH-DT49WI3HkDAMZKqk4BWusVuzw3L4VedoRuy19FRFFFxjguufMIAFptmrkrHWoJx2lCQj4AdyFopdW3zdRrGHVBWZpDx-d1F-2Nca2ou5dJk9oaz4YBJrz6RM33RbY3id4AlZq-Lh3QUPfm7xa45HVvwOljXqitly6hjrwowT8WFLmNLpU5jPW2I6y_lP2pjsuISaO6w51eGUP5IVnHIqeLgA3H5CD8O7zvnUTgts9Krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال کاربران از قم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/137893" target="_blank">📅 15:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137892">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQL8LiBvAoop-r1NyUnl-3M-LMkZtR77WPKQZ_wjSI1ZI1-DR_GX5b31nfx4Xhe4TiQpgwzPcTxDElW2tvJYHk2nRHijt03VOR-6hemhPCx-q1UKNcCSHQzoAFYsFR4wN369aj3NOh6dzW_PPYiUpG91A7NeWHGhY2APOy5m5j-WVvXi9oKrKxy8qLuuxhCXP2jUI3xcWURx_Chn-TCEPsj-RkekTdUe_F15HsYBU6Pq6NayIOP4RcTgXJKN11GzLVYxQW9WFOm3g0jHp7SUJAcuVlfVt3qKY-SuopndE3-Om6jmb82UbthyDlJBi6D74eJtkwSEy6o9iV6pIiiTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
🔴
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/137892" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137891">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343c49ad52.mp4?token=ZAp_r8HHAPT7aRKYJH3v9GK8BlKUUqdR30GsG-u2Q68nYQgywlQIgjAxzD1xvUNjUWXvzcle4qeyiVseNdnvhQ6Qy5B3xvnMNiUotq1uLv-Z8pXcfpxC-WmjfwRB-qHTKfSLIdc1Z81gHlJW4G9_zggI4RGTVweRz4hDTD7Tt-FQxe2pYuDcyXUHvzIaRnUFA0UZDiVsbynSkAWeI6AVrRZt84GmpgDpvHL5q1nOkwSb4hV2OwRs3TstDXTwX8CLGOfawAoxTamic-c5LBd9AR_Zulso3FSF0R_10J2qMAE8XLO4x1Ba-dOW7oHs9zkjrrrnY7fKdoqGuvdFniyj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343c49ad52.mp4?token=ZAp_r8HHAPT7aRKYJH3v9GK8BlKUUqdR30GsG-u2Q68nYQgywlQIgjAxzD1xvUNjUWXvzcle4qeyiVseNdnvhQ6Qy5B3xvnMNiUotq1uLv-Z8pXcfpxC-WmjfwRB-qHTKfSLIdc1Z81gHlJW4G9_zggI4RGTVweRz4hDTD7Tt-FQxe2pYuDcyXUHvzIaRnUFA0UZDiVsbynSkAWeI6AVrRZt84GmpgDpvHL5q1nOkwSb4hV2OwRs3TstDXTwX8CLGOfawAoxTamic-c5LBd9AR_Zulso3FSF0R_10J2qMAE8XLO4x1Ba-dOW7oHs9zkjrrrnY7fKdoqGuvdFniyj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید از آتش‌سوزی در پالایشگاه نفت جیزان شرکت آرامکوی عربستان سعودی پس از حمله انصارالله یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/137891" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اطلاعات نظامی اوکراین (GUR) در شب ۲۵ و ۲۶ جولای، یک پرتابگر و یک رادار 96L6 را از سیستم پدافند هوایی روسی S-400 "تریومف" در کریمه منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137890" target="_blank">📅 15:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb592bb5c.mp4?token=V-KGqloZxW8jL2Hl8R7XhtQZO-qp6hy_vwg1Wv3jKUWZEacRV9q1LBvFQhBOE69dWqp4Cy9N0Ekj6YwddMHvqWNQcGESPo_AOk13VFFMySQGjV-DmhWyokt244UCfCLqoGv3Nk9hNT0W6HDUhDheUmvdSofPJ7pvLiU6zY-JT-JSfmykV-mF0YWEC4AqO37fMTa3NwasC9YaRPMOexJacILO8waKmcWSLjSLChfHv2HbRLdD4XELaOsDibDpExq6vHC9Sfs5H_A0_Tt8a_AtiR0tX19fd-VDikEIF0rHX-iAuFNzuuP377I0263oBizUjfkytUPAuuRMEq6AdTSwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb592bb5c.mp4?token=V-KGqloZxW8jL2Hl8R7XhtQZO-qp6hy_vwg1Wv3jKUWZEacRV9q1LBvFQhBOE69dWqp4Cy9N0Ekj6YwddMHvqWNQcGESPo_AOk13VFFMySQGjV-DmhWyokt244UCfCLqoGv3Nk9hNT0W6HDUhDheUmvdSofPJ7pvLiU6zY-JT-JSfmykV-mF0YWEC4AqO37fMTa3NwasC9YaRPMOexJacILO8waKmcWSLjSLChfHv2HbRLdD4XELaOsDibDpExq6vHC9Sfs5H_A0_Tt8a_AtiR0tX19fd-VDikEIF0rHX-iAuFNzuuP377I0263oBizUjfkytUPAuuRMEq6AdTSwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو پیش از عزیمت به واشنگتن: ما درباره تمام موضوعات دستور کار، به سرکردگی ایران، بحث خواهیم کرد.
🔴
من با یک هدف روشن عازم این مأموریت می‌شوم: تضمین امنیت، قدرت و آینده کشور عزیزمان، اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137889" target="_blank">📅 15:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
صداوسیما: علت حادثه آتش گرفتن انبار ضایعات پشت هتل استقلال بود
🔴
این حادثه تلفات جانی نداشت فقط ۳ نفر دچار دودزدگی شدند.
🔴
آتش‌سوزی در حال مهار شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137888" target="_blank">📅 14:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: جنگ آمریکا و ایران موقتاً متوقف شد. ترامپ راه مذاکرات برای رفع بن‌بست تنگه هرمز را باز کرد، اما دولت او اعلام کرده تقویت نظامی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137887" target="_blank">📅 14:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3777c0bf3c.mp4?token=snwrk-Pqj2nUfnZMIduZEcH9QyJKTvo1BX9GLNu6ivrQRAiovlpAyY_eOUj35lXiFNUhzsJ2-GB0Hdk7y0p9VU-W4j0naydFl-2R3qiSax88eVZuAdhyf9JyYtf6M5R7NEspOSTJYpsbH9fAX_80dswGkAXGcc6tS6Cd9hJ_YMjShAf2CWa4k2f6q2Flyixlq1_QzpiwTg6cbHMopUxwjvyCotdxS1FqXWpASkjacP77MCumHOaFel9_sd--kYx2Q92IaVt-Ps6zWRHPA99BvMdX3vdDTuMQ6J1cFK0420fh1sui2s61QY4FoFWCXQyHliF96pX9nNqNW2JxgtvJgCuTFNlILLNYcKIrez77Pu97sc5v5DRyVFgiGgF-qA6LTFO6Hzg1GlNE1rOtdpSLeUJqn7NMaXxo_8O5IzvYsv6Gea3dqgw6x_TzZ6NnwGLXm95oNJ3Hm2tmwuV15Q9iOrGYDgXepwsZQ6SHTMHfXLa3_W27HTJ8u_y2UJh3YzZCTTWMkWFRcy9vIkhCvIuvDfT54GK0RP9L9YGsfoQle2zl3pqL5v6EB7uO4Wscr3APsvZmn0FruFE7EFukQcKL9m2TmI9CMIxMoHY6y4455fGZImpR7hBP3IYXM8WHKtsaNJd_x8KgMfluiGHlr5tlyjDo5irCf1j2V2MW63czMrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3777c0bf3c.mp4?token=snwrk-Pqj2nUfnZMIduZEcH9QyJKTvo1BX9GLNu6ivrQRAiovlpAyY_eOUj35lXiFNUhzsJ2-GB0Hdk7y0p9VU-W4j0naydFl-2R3qiSax88eVZuAdhyf9JyYtf6M5R7NEspOSTJYpsbH9fAX_80dswGkAXGcc6tS6Cd9hJ_YMjShAf2CWa4k2f6q2Flyixlq1_QzpiwTg6cbHMopUxwjvyCotdxS1FqXWpASkjacP77MCumHOaFel9_sd--kYx2Q92IaVt-Ps6zWRHPA99BvMdX3vdDTuMQ6J1cFK0420fh1sui2s61QY4FoFWCXQyHliF96pX9nNqNW2JxgtvJgCuTFNlILLNYcKIrez77Pu97sc5v5DRyVFgiGgF-qA6LTFO6Hzg1GlNE1rOtdpSLeUJqn7NMaXxo_8O5IzvYsv6Gea3dqgw6x_TzZ6NnwGLXm95oNJ3Hm2tmwuV15Q9iOrGYDgXepwsZQ6SHTMHfXLa3_W27HTJ8u_y2UJh3YzZCTTWMkWFRcy9vIkhCvIuvDfT54GK0RP9L9YGsfoQle2zl3pqL5v6EB7uO4Wscr3APsvZmn0FruFE7EFukQcKL9m2TmI9CMIxMoHY6y4455fGZImpR7hBP3IYXM8WHKtsaNJd_x8KgMfluiGHlr5tlyjDo5irCf1j2V2MW63czMrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
مردم روسیه هرگز تسلیم نخواهند شد.
🔴
این هرگز اتفاق نیفتاده و هرگز هم نخواهد افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137886" target="_blank">📅 14:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT8f59t8-SrZi0QjlB6b5NJwaL9Qgai_jPHHmW5g97eRvoRXL2-tjrrvIeT7JouZLFPmaYflDuUfYjyf3WIUqCEUFe13AHm77RQkgOb0SFm3xYAf5RQ1X5FKr5A9v6EpuvnmuAqpeF6P-mC4Rll991WUN3hi-Tc9IKhkuUngEWISiods_fr1zczn4GO3SVljp7nXu6xYZyFGx3vdNGoRjHpFkjC8Ocg59TY4S62A08K9fVuOuKAZ7l6-msUyEClQc6G-DLpcLnpVsv5VZRuOeS--GZ-jm6VLEyG42YN8EzSgq6aWMzpGlsmYSRnRFxEdfiBL7dzFFVKvGgJPLobHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آموزشی مدل L-39 متعلق به روسیه در منطقه کراسنودار سقوط کرد. این حادثه در حالی رخ داد که خدمه هواپیما در حال انجام مانورهای هوایی پیشرفته در ارتفاع پایین بودند.
🔴
هنوز هیچ اطلاعاتی درباره وضعیت خدمه هواپیما منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137885" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWYDYem2SZj9w1-ie-iBU8BDKd19ecmgPT5e8H3r-TQBKKxtMVhRsQIsKyPbSwVrImB-L7zTNiSG6_DZGlJv9HSRIHyTHlgunEVwoXGIMYeIKDjRgWQ-iQn1q1fa1PgMHexhys4ASfs7VN2b6u5lx3ly0-X_VDi1GEPvIhiE3u1PSBRjOTfHOI826JeXdgFcTz3gK6wdz9JyiiGzzsoSLo7oP7r_4uM4nwVbTiI9ffKqmbHxoUjJoaViPqJ4Cpi-auyd24cEFBxbPgu_k5L5QDYll2hkvh-ISD97NN3YZrFE8elwIgsvBPgxd46_tTHSiKecVLuen39krM2zdN9YUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاملا هریس آمادگی خود برای شرکت در انتخابات ۲۰۲۸ آمریکا را اعلام کرد.
🔴
این موضوع باعث جشن در بین جمهوری خواهان شده، چون معتقدند گوین نیوسام به مراتب رقیب سخت تری برای جمهوری خواهان می تونه باشه تا هریس
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137884" target="_blank">📅 14:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
گزارش از صدای انفجار در شهر کرَکِ در جنوب اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137883" target="_blank">📅 14:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تلاش آتش نشانی برای نجات ۳ نفر که در طبقات هتل استقلال تهران محبوس شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137882" target="_blank">📅 14:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd0y9twe9nIVWjY2f_kBm04UdKdjo_IstXCptv8x1nNp38bScaK_61qM8DJfRcNeN6B8qJRBgLT2tbAF39xGi9NQQwMb6imXqcBTXITh1k-Z_pVscTW6nKkgFjqrZ-3Sng3GkZA9TjHs0ytyE4VfFpmOj9UgIpMvJsyqnQBUZJKcku-ZV9VYKYaSpaTWzqzdzO4x7SspHnjKe8Cb96tu-n63NMq2_4VbxeKiySSkk_Ka33-H-z3KzNawefMWQcqH6fLMhmZ8BwXoE8pC2VbDb6jduvoKbo3bFnFaGvbT2L9eOwBCjeE8t-Swos0SNyO9KMOG0RCAAtnsuzScjzJNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انصارالله یمن: تاکید میکنم تنگه باب المندب به طور کامل به روی عربستان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/137881" target="_blank">📅 14:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4aac8d1c2.mp4?token=QqRPJEiidVkugm-p8Fpz6Hnp2JHq4S2yBOPU3sJDlXb6d5K4_LivkczMLrykBZdt0RLraZwflLWO2_P5fwl-30b5DA9G3DnanJvE6tpjObUtxEQB7Bsp5EvfVgVok8pVumwG80XhisNcQmzS1Z804JkdL8Z4A16qAvAjilbTaMc8D5BdJ5HhvogPm8xuTbCtAbvSuF_38CBV65ohMroreSEw1Mnvlwruw7NCMqDNMhbzkaTSGxG99I-CeHhKaMJhx31U2wfhxYC9xkky8FYG2dJ7WQjeKBRN6U8OeQYmhBS1nzx_hPlB0XYzJeOvSJdVu8nIVpiGHhg3I49cNzmLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4aac8d1c2.mp4?token=QqRPJEiidVkugm-p8Fpz6Hnp2JHq4S2yBOPU3sJDlXb6d5K4_LivkczMLrykBZdt0RLraZwflLWO2_P5fwl-30b5DA9G3DnanJvE6tpjObUtxEQB7Bsp5EvfVgVok8pVumwG80XhisNcQmzS1Z804JkdL8Z4A16qAvAjilbTaMc8D5BdJ5HhvogPm8xuTbCtAbvSuF_38CBV65ohMroreSEw1Mnvlwruw7NCMqDNMhbzkaTSGxG99I-CeHhKaMJhx31U2wfhxYC9xkky8FYG2dJ7WQjeKBRN6U8OeQYmhBS1nzx_hPlB0XYzJeOvSJdVu8nIVpiGHhg3I49cNzmLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نفتالی بنِت، نخست‌وزیر سابق اسرائیل:
نتانیاهو قطر را یک کشور پیچیده می‌داند. این کشور پیچیده نیست. این موضوع ساده است: قطر یک دشمن است.
🔴
ما باید از این کشور فاصله بگیریم و علیه قطر به عنوان یک دشمن تمام‌عیار که می‌خواهد ما را نابود کند، عمل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/137880" target="_blank">📅 14:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137878">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / نتانیاهو، نخست وزیر اسرائیل به سمت واشیتگن پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/137878" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / نتانیاهو، نخست وزیر اسرائیل به سمت واشیتگن پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/137877" target="_blank">📅 14:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری / نتانیاهو، نخست وزیر اسرائیل به سمت واشیتگن پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137876" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
العربیه گزارش داده است از سال 2011 تاکنون 35 میلیارد دلار درآمد نفتی دولت عراق گم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137875" target="_blank">📅 14:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
زلنسکی :  ما سمت درست تاریخ ایستادیم
🔴
اینجا کشور خودمونه، خونه خودمونه. این خانواده منه و این کشور منه
🔴
من کشورم رو دوست دارم و هیچ‌کس نمی‌تونه منو ازش بیرون کنه
🔴
چون اگه ما ضعیف بشیم و پوتین موفق بشه، مطمئنم همه‌چیز رو از دست می‌دیم؛ آینده بچه‌ها و نوه‌هامون
🔴
ما نمی‌تونیم اجازه بدیم این اتفاق بیفته، چون پوتین هیچ‌وقت دست‌بردار نیست، فکر نکنید فقط اوکراینه؛ اون جنگ رو ادامه می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137874" target="_blank">📅 14:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر دفاع جدید انگلیس: از اقدامات تهاجمی علیه ایران حمایت نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137873" target="_blank">📅 13:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oehLTtG9hpJuDXGY740XgHRMrgOgi8Qo50XPC3IdaPO7jUsyzTe3inzT1iN-YFfU2uQmh-4IuD8bPRfktp4KwH86JjVdYQx-7F5lUyxqb3y2Okr-dfhMx3-tSYULgJ3nho6-hfuFaxsaAJBOVd_ed928sjsXcIrHH9sIvTGl4Y3DaUSltY6D_uidw_Tr1iekyvCHDMEOhpWVTJaHK1hFLxYff1JERlFQUUuPtDT7FX8A9w-_X3L9JajscCH3lFujfkorSVU9Si_eyCxyioYmYCPac913H-05wxM5TbPRmHEZRzHSIVfo5b2LobJsY_mFDnAFsucebsRvtKlPEOBbmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که ترامپ از دیدارش با قالیباف (هوش مصنوعی) منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137872" target="_blank">📅 13:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFMEDnXeQtN6z3Hn4mEuq78QfAMQpmIlOMSlcQlKzyp6cAuzojizuVsePXEV82qumZEIV3_qE8fBo-1Jtni7HEuzfYMBv8WwVs9aurgEomFvhqlCd-EO7ypcHsm4bC-ajaoUmasJUT6yT_4IVLgXM6Ae5c4hRWY2jzzKWANRhp3JuRSZurvAsZGkP24G7kXdxpvTwyk_6ZNSORFK_JwQP1Kuav1PG2Lud_L2ISMKjseCVMhn7ZW7rhtqSLjt1est1YLmCdN-4zvs6exvVxSNqykbSZcarbendgIgUaLocVOeWcKpsBH2aXFE_2K2Sl_ROSosWzM496tsHXViYyInQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس: الان اسبابش را نداریم که از آمریکا و اسرائیل انتقام بگیریم، اما بعدا انتقاممون را خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137871" target="_blank">📅 13:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز با افزایش نسبت به روز گذشته، ۱۸۹/۴۰۰ تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137870" target="_blank">📅 13:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ادعای نفتالی بنت، نخست وزیر پیشین اسرائیل: قطعا کشور ما توانایی سرنگونی حکومت جمهوری اسلامی را دارد. اما یکی از فرصت ها از دست رفت، چون نتانیاهو قبل از حمله به ایران اقدامات لازم رو انجام نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137869" target="_blank">📅 13:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137868">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O506F6x_FxUk9O6fx_Ka-FP1n_ZknZRWDigeMOZd8BzUphNkcKX0z_BVYzEQS9X0mLkKzBNOjX0wbbkviUd0dXA7r1sN0QxHJxexdHosd1qJ8My_J5t_9CacxrlpuUl9eOKSxwGeFk1pkMTbSJaZMHhPlvUnyEOwD6DWqLtt7f7thuEGLnHTbq1KmOJYKxzYaAe8E76rnkd75Y1aS0z5NByqYhAdoB3onCCr--tFEW_aH1Jy9yVfgRLHPiEG4kFQVMGmc7nV71acMyRZJO83doPbOpO7ql1wKBO4V55wR5vxV7UmdLeuO5lZmXRarVFBMfsD3Tm1rQDVjPaYWuKkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری دیگر از آتش سوزی در هتل استقلال تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137868" target="_blank">📅 13:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137867">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تایمز اسرائیل: پرواز نتانیاهو به واشنگتن به دلیل نامشخص به تأخیر افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137867" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137866">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وقوع چندین انفجار در استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137866" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137865">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959eba656f.mp4?token=ma2o4TFbqMla0M4FjuS4J0AY0bDy-Y59IxfdyNba5Meguw8eSuAdFYLdoutVk5NcYekinAwJzqWGothWKB2ZpFX6rTgtiEPh__xr9_AGEZZzPLk4LtX5RuBa4iw5bOSmBnKBEG15m0FB-eGBy6idaQj-nHPehEOijtyZeKtQ0cyqtyGg5rUJXXdLG7kuSyY4ejzXsMm8mh4xiIEj7yKLZt1DMjGnIbbl73sciUyZEw9T_AzFJYnhEGYn9Dg4a8JWDZL9WXrMYECqU-9au0XQVIikPYyjCgbOHEsTCaL4DEOXPmzYbmZWhQs0A8Xeboz8WJW18kgrBXc_lfomtj64Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959eba656f.mp4?token=ma2o4TFbqMla0M4FjuS4J0AY0bDy-Y59IxfdyNba5Meguw8eSuAdFYLdoutVk5NcYekinAwJzqWGothWKB2ZpFX6rTgtiEPh__xr9_AGEZZzPLk4LtX5RuBa4iw5bOSmBnKBEG15m0FB-eGBy6idaQj-nHPehEOijtyZeKtQ0cyqtyGg5rUJXXdLG7kuSyY4ejzXsMm8mh4xiIEj7yKLZt1DMjGnIbbl73sciUyZEw9T_AzFJYnhEGYn9Dg4a8JWDZL9WXrMYECqU-9au0XQVIikPYyjCgbOHEsTCaL4DEOXPmzYbmZWhQs0A8Xeboz8WJW18kgrBXc_lfomtj64Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلاش آتش نشانی برای نجات ۳ نفر که در طبقات هتل استقلال تهران محبوس شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137865" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137864">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304d57163d.mp4?token=GjAicN5eForgMOecigC5fptB8jvsWUhNFrhWPAoZo7i3WyWwNZCtJlbLzK6toL2hQDlsEwwdwT3H7RHpAsE21EGHVazAI-glFeOCrVankXPGziXn-sUboR_rlJ1zir9xUWaj3jnWd_A54r3VZlxNDIlHCIZOOwNqTJ44tXrkRk4djliErXKsuiQczPqfqrpR4tKdney_dqyIATqXsMLTLM68v3wgKSratwqSoqMgpprH5MkpMaqrU3drygZq8l-LD33d7zFqPEOYqxb9Fbbq-WeERznRzcFzoA6Ruo8KZ5Wvha-mIb0zT4YXTVHByeQjrHDewKUJEDCvbxLAnLrtqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304d57163d.mp4?token=GjAicN5eForgMOecigC5fptB8jvsWUhNFrhWPAoZo7i3WyWwNZCtJlbLzK6toL2hQDlsEwwdwT3H7RHpAsE21EGHVazAI-glFeOCrVankXPGziXn-sUboR_rlJ1zir9xUWaj3jnWd_A54r3VZlxNDIlHCIZOOwNqTJ44tXrkRk4djliErXKsuiQczPqfqrpR4tKdney_dqyIATqXsMLTLM68v3wgKSratwqSoqMgpprH5MkpMaqrU3drygZq8l-LD33d7zFqPEOYqxb9Fbbq-WeERznRzcFzoA6Ruo8KZ5Wvha-mIb0zT4YXTVHByeQjrHDewKUJEDCvbxLAnLrtqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
زبان انگلیسی را ترویج نکنید چون میراث دوران طلایی پهلوی است!
🔴
مدرک تافل مجتبی خامنه‌ای موضوعی است که توسط طیبه ماهروزاده (مادر همسر وی و همسر غلامعلی حداد عادل) در خرداد ۱۴۰۵ رسانه‌ای شد. او اعلام کرد که مجتبی خامنه‌ای پیش از خواستگاری از دخترشان، مدرک تافل زبان انگلیسی را دریافت کرده بود.
🤔
خودشون اگه یادبگیرین ایراد نداره ولی واسه مردم عادی خار داره. یکی نیست بگه این مشت گوسفندی که عربی یادگرفتن به چه درد خوردن جز اینکه بالا منبر نشستن دروغ تحویل مردم دادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137864" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137863">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d584dd517.mp4?token=i63Dv2isbNTDo41XIySaF2ogdruEY-H9LZdU2HUddMy2jiUDlEyCqzPvHVHKV8vpsATS-mfW7JI6kTaJ0yznHmpsV8LorNEskYulrC5DZ3zzDv9eYGmBeXWnQbi8J_9W9DUU7YsI4zrn2xxwIokDbK13Hht-GaGMEBXSyqKgCEVrbu6wTgZgHQs6FZ9qf1juoj89AgOzw5YvJ2bKf-BVaXgcbphZNRh8Yqs83__6PgwHvvbv9md_gLG3TnzLXp2B7srMzTU2nd9QCr9duxaeto2WEDmfNpzWZRP5hFvAH3ooHEtpwvxEP8DfRhqch862ZLktmQzTKXNuF6VNHh84eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d584dd517.mp4?token=i63Dv2isbNTDo41XIySaF2ogdruEY-H9LZdU2HUddMy2jiUDlEyCqzPvHVHKV8vpsATS-mfW7JI6kTaJ0yznHmpsV8LorNEskYulrC5DZ3zzDv9eYGmBeXWnQbi8J_9W9DUU7YsI4zrn2xxwIokDbK13Hht-GaGMEBXSyqKgCEVrbu6wTgZgHQs6FZ9qf1juoj89AgOzw5YvJ2bKf-BVaXgcbphZNRh8Yqs83__6PgwHvvbv9md_gLG3TnzLXp2B7srMzTU2nd9QCr9duxaeto2WEDmfNpzWZRP5hFvAH3ooHEtpwvxEP8DfRhqch862ZLktmQzTKXNuF6VNHh84eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از حمله پهپادی ایران به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137863" target="_blank">📅 13:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137862">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mujO9Vl0W48_tm_v-K4NM74KFdcuUDW5_l1ngXl4RL9qB7hgdTmHk2MY7ajcth6LA6vz1BEFvK2YCVwYyhmJDtNv3ceulH5BJNmR7B6EuU8WCJvm1vlFO_zRABDqbVOPKuKJG5_6tTU-6e-FHI06G1APbVyfxLPbb7wPFh_nbBQNNwjmyqvX7zzoEVomB1WWIHDu_Q_yqRsOH0o7fZQDP2XWcNsk25wXTW_z3GVWanIZCDwQDasfyfiyHzWsmGeEcciMI-JDj8QjG1tDZRWReCEfyhUfYdZWG7nS810XfCpnGBlcFxA5M8y09HXfS5PXziBarBJ5_JMWRK80aHC7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بروجردی، عضو کمیسیون امنیت ملی مجلس: اکنون فرصت بسیار خوبی برای ما فراهم شده تا تحریم های آمریکا را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137862" target="_blank">📅 13:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وقوع چندین انفجار در استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137861" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فووووری / برخی منابع خبری از وقوع انفجار در اردن خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137860" target="_blank">📅 13:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0203c0440.mp4?token=SGbGFli1gZ7xO6qIKRQsCIkvYoFrpZSCJKdL6TLzOZyrqYb7FSZFimjCQim4v649j4Pgmv8foFYua8DpaaIatTkGSZonpOBjZpKVWeCYsrqwUqWBF2-1pbAJmKNSLgpZiHZXDLxOzNLrUEvphWQpuYpqxyVa4CfnJpa91mwH-X4RYgsmDwI2lSAVljPJiNt5-fGBWAZsf73omgKGyC55Mrdvdb17DqMOYKxqwOW_g4HeDzyf9p1VhYEqOamkixJUvP87lsv68OAOicC9ZJvoNxmJih2zPfJuzXL2LxPHdSYcV5ZlyN1L4o4tVbdX6Yw5FAsb-QCB_23PrTJR5kiIrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0203c0440.mp4?token=SGbGFli1gZ7xO6qIKRQsCIkvYoFrpZSCJKdL6TLzOZyrqYb7FSZFimjCQim4v649j4Pgmv8foFYua8DpaaIatTkGSZonpOBjZpKVWeCYsrqwUqWBF2-1pbAJmKNSLgpZiHZXDLxOzNLrUEvphWQpuYpqxyVa4CfnJpa91mwH-X4RYgsmDwI2lSAVljPJiNt5-fGBWAZsf73omgKGyC55Mrdvdb17DqMOYKxqwOW_g4HeDzyf9p1VhYEqOamkixJUvP87lsv68OAOicC9ZJvoNxmJih2zPfJuzXL2LxPHdSYcV5ZlyN1L4o4tVbdX6Yw5FAsb-QCB_23PrTJR5kiIrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویری از آتش سوزی در هتل پارسیان استقلال
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137859" target="_blank">📅 13:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فووووری / برخی منابع خبری از وقوع انفجار در اردن خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137858" target="_blank">📅 13:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ریاض: گفت‌وگوی تلفنی وزرای خارجه عربستان و عمان در مورد تضمین آزادی و امنیت تردد در تنگه هرمز
🔴
وزارت خارجه عربستان اعلام کرد: وزیر خارجه عربستان با همتای عمانی خود در مورد تضمین آزادی و امنیت تردد در تنگه هرمز گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137857" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / دفتر نخست‌وزیر اسراییل از به تعویق افتادن سفر وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137856" target="_blank">📅 12:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، اعلام کرد که در صورت بازگشت به قدرت، قطر را «کشور دشمن» معرفی خواهد کرد؛ او قطر را به تلاش برای نابودی اسرائیل متهم کرد و مدعی شد که این کشور بودجه سپاه پاسداران ایران، حماس و جبهه النصره سوریه را تأمین کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137855" target="_blank">📅 12:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwNbnM-7Dmidd9MuNDtOEgHDH_dbK0AqqqxuWxV820g6U6CgWmRDCX4T6fbByh7ayAIXkoZJ3TYYFlscMHV0iho-FUcpCMcLJ3iAsKlvLRMF8K46QCrgTng3GjXf8cGzjbZIIhnd8Co2YyTtvR24nQko_g25ihIlzXEyLSk4pa3miokQxOPjfQ0rLvvn0515z2oqjlzbgzLs1O302fCKi6gonO9u66CtIlIKqcKZShq9IgAV0mcBeCogL11QOoiyJvAC5m2z8DuEAqlpyk8rFX_vhKrUVMlMXXbvi-iReKi7VgR6naISgvC_s-PmTP6-5SaVQn8GqFqikX_lqjyRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در جریان معاملات امروز شاخص کل‌ بورس با رشد ۴۹ هزار و ۷۱۳ واحد در ارتفاع ۵ میلیون و ۵۲ هزار واحدی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137854" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سازمان امنیت داخلی اسرائیل (شین بت)، گفته است که ایران در تلاش است تا در انتخابات پیش رو در اسرائیل دخالت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137853" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8195b31d40.mp4?token=d-BgWc-XGLxN6xFsyccFCPEO6je0-1FPn9_rPTtdGwigmnrwTFSjEETmATmyGHH44B8vTJ5XNMY1g_MuFPPQfUDU71f-XIGCR6gTxDGIgN4mPtcoVwo9i6NKWLp1d-fRRlIcdJDEipp00wpponpFxVl5u5Z0fpgqV2SUXX81L0qFC_RDUsEDlULvkmTaaAJumVQlMW8WgqbFnuhz0iqFnFWQLQjZEAnQ-23NHhEYDhbtC2skfwnI6k-LcYtQSyO-w9NHC3p62r_-IZQ4AqZ-aJ3TxTlAJH5r1nW2BqsHIOhYiaZQa4zibyrf5F4-_X_1SrFQQ7AMSOqQeLY3UvoV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8195b31d40.mp4?token=d-BgWc-XGLxN6xFsyccFCPEO6je0-1FPn9_rPTtdGwigmnrwTFSjEETmATmyGHH44B8vTJ5XNMY1g_MuFPPQfUDU71f-XIGCR6gTxDGIgN4mPtcoVwo9i6NKWLp1d-fRRlIcdJDEipp00wpponpFxVl5u5Z0fpgqV2SUXX81L0qFC_RDUsEDlULvkmTaaAJumVQlMW8WgqbFnuhz0iqFnFWQLQjZEAnQ-23NHhEYDhbtC2skfwnI6k-LcYtQSyO-w9NHC3p62r_-IZQ4AqZ-aJ3TxTlAJH5r1nW2BqsHIOhYiaZQa4zibyrf5F4-_X_1SrFQQ7AMSOqQeLY3UvoV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنتونی جاشوآ بوکسور سرشناس بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه دیشب خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی خواننده سرشناس ایرانی وارد سالن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137852" target="_blank">📅 12:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز: کاهش حجم حمل و نقل دریایی در دریای سرخ همچنان ادامه دارد، این در حالی است که حوثی‌ها به تأسیسات نفتی عربستان سعودی در دریای سرخ حمله کرده‌اند. تنها 11 کشتی باری روز یکشنبه از تنگه باب‌المندب عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137851" target="_blank">📅 12:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137850">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2gRVJTxO3KxusR-fDc1TsE3vvyoXyfGVsdvVCOiVhNMVFq3qPOrbcwPwfXlnclh9gc9BCXxCXRoYIeOnGwZnkkVnzWRkMzzT0JeUh7RlAuMJMOkbwl9qmJfGVsQdWKv_4inrgXIO3algHxhwcupGJlwNudV1EQnCNc93wFGFRZqvS1Zqiy2M1Kz-QLNY0krtsudkWv8MldfBpd9YjZ7j4UsA4xZ4EmCx3LBE2MlY7dIjyUg1h32h3qRCryvH6fVMwXwxcVMK7U0fiLOggDqbqyVQQmYEGO8WpyzfsNhfsWB_2jXtvaCa1TcFsu9Tm7t288Vf1c633s7BeTqHQrJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری پر بازدید در ۲۴ساعت اخیر
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137850" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137849">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68be3b8cf.mp4?token=a_BE0Gi0YdVzw5tdyrZDd0hV7itZDRNP-dxpkd93JiavkjZmZP3d1rFS7WsuiZkjBfgvQIdJ3Son5HwAAQYG8yg9flQT-ups-_QOyu7-sf7ByWUXXIgn8zC6lexAX6klrU-HZyYcMU-w16vSnlYxbtYF-Qocfk0Ft73jpAFbF3s5ZIMq28EING0UrFiJgUPkCRlSMfXckXbXnbiFZT0jgjTHasHFaUdt9doGLq-B5O5EADKVRh6JrXftiU7OwraNwR15X4HH9H6V9VWzPKeLHuzuw2XGjtD_-Tg_yNdnWp1qL2xo5OqETIBFPYvL5GV7RMhH1l635LHZXJmK2ozD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68be3b8cf.mp4?token=a_BE0Gi0YdVzw5tdyrZDd0hV7itZDRNP-dxpkd93JiavkjZmZP3d1rFS7WsuiZkjBfgvQIdJ3Son5HwAAQYG8yg9flQT-ups-_QOyu7-sf7ByWUXXIgn8zC6lexAX6klrU-HZyYcMU-w16vSnlYxbtYF-Qocfk0Ft73jpAFbF3s5ZIMq28EING0UrFiJgUPkCRlSMfXckXbXnbiFZT0jgjTHasHFaUdt9doGLq-B5O5EADKVRh6JrXftiU7OwraNwR15X4HH9H6V9VWzPKeLHuzuw2XGjtD_-Tg_yNdnWp1qL2xo5OqETIBFPYvL5GV7RMhH1l635LHZXJmK2ozD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشون می‌ده یه مخزن سوخت تو پایگاه «موفق السلطي» اردن، مستقیماً هدف حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/137849" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137848">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت دفاع روسیه: بامداد امروز نیروهای مسلح روسیه به حملات خود به بنادر مورد استفاده برای تحویل محموله به نیروهای مسلح اوکراین ادامه دادند.
🔴
دو کشتی باری در بندر نیکولایف در حالی که محموله‌های نظامی را تخلیه می‌کردند، با پهپادهای تهاجمی روسیه مورد اصابت قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137848" target="_blank">📅 12:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137847">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رئیس اتحادیه تلفن همراه و لوازم جانبی تهران : با توجه به نوسانات شدید نرخ ارز در کشور، امکان پیش‌بینی دقیق روند قیمت‌ها وجود ندارد، لذا توصیه می‌شود متقاضیان، تلفن همراه را در زمان نیاز خریداری کنند؛ چرا که موبایل کالای مصرفی است و نباید به چشم یک ابزار سرمایه‌گذاری به آن نگاه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137847" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137846">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
🔴
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137846" target="_blank">📅 12:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137845">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9015499bb8.mp4?token=ocZRf9GvHqWnWkFUsUf5d8590sEcvtaB_h1dhm6ejv2VG7scGsPT6x8WUo6czkIj9oL8PFmrwwCxOtx3uhDQ8wbz-XQqvg6kWMkNwocKWrOXygViLApvnJE6XiSD1HcbRFu_raFHYD2ZYjP_HQ5h0w-7YrtuwoVr2Vhyj9iH8eEVbSKmVhJramKl5DrxQGSxamkE9z0Z9QG8pGa6rDC3gt86IP8EM72cD5CpL59b65qIKtF7IOD57wqSOM5XtZ_I_fndKolbTh8xmfijeMHrxLBkq6EacHYrTYc-VwnJtUhoIegXeGSz1zHIZ_vAMMburMhXoZbUknml_VdsZKbTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9015499bb8.mp4?token=ocZRf9GvHqWnWkFUsUf5d8590sEcvtaB_h1dhm6ejv2VG7scGsPT6x8WUo6czkIj9oL8PFmrwwCxOtx3uhDQ8wbz-XQqvg6kWMkNwocKWrOXygViLApvnJE6XiSD1HcbRFu_raFHYD2ZYjP_HQ5h0w-7YrtuwoVr2Vhyj9iH8eEVbSKmVhJramKl5DrxQGSxamkE9z0Z9QG8pGa6rDC3gt86IP8EM72cD5CpL59b65qIKtF7IOD57wqSOM5XtZ_I_fndKolbTh8xmfijeMHrxLBkq6EacHYrTYc-VwnJtUhoIegXeGSz1zHIZ_vAMMburMhXoZbUknml_VdsZKbTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت ساحل دریاچه ارومیه را مشاهده می کنید که غرق در زباله و کثافت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137845" target="_blank">📅 12:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137844">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErqnzHgbKuKr4kHGuyW-3FUErgGGmiit5LL60d1f4YJbjxMDUU6gSc1xcFMP5OLVv7kzxwJAxP8f3JCjiW4ZvlmINjOw1L7FFUyKwMnFOogkQQyLNvu0IVCoBNqNYAtlck3UM5bWe0VIeTPdhzEIeDV2lw6GadB0gkLAcE9iPeEKsejIiiD5G-gfZcix46wYMHsV4o0CL4-vj5oGenNbaZhCtR4HihifmZvJLEB4uCypFwrFutnrbb0LWiByuBlDevy_v97wor3KZvfkc6_nHlbekboLLJN3RReZESLff-KFlIdiDMjl_XbjAwAXvScW_c3TrNGkXMKaufOsFFyEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نیما مرادی، جوان انزلیچی که در حمله اوکراین به کشتی ایرانی در دریای خزر جان خودش رو از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/137844" target="_blank">📅 12:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26576790db.mp4?token=uSIdil5fM43E39cQ3tSkiJV02bzBlP0M1Gq3piztqvTHiZBtp6yflktV3hlJ1VMJchRzwwJpOez908akSKd6RQhrTshu87L5IXFKyoeY4sTzgOY7wma8KlK1t3FK-9IuhmFRNCUM1z8Ne__nzexqfXEjDME40qZMK3RBeuWxwr9iJPmasxSXMMiF1qEer12eA1ozmZJq00HqBIfeA0gMQqYDcIyzw8qYwPFVJA1rVY_PN4ikKrPE1R1RQhtXZFxq8f2RNQiYDsw3SAyS_uEPm2IYp8GEOlvy0MsYyT03XwX_QiC1GlZqKDGk8PGaKbDcjPscdVoH6sdE9d-0K-tuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26576790db.mp4?token=uSIdil5fM43E39cQ3tSkiJV02bzBlP0M1Gq3piztqvTHiZBtp6yflktV3hlJ1VMJchRzwwJpOez908akSKd6RQhrTshu87L5IXFKyoeY4sTzgOY7wma8KlK1t3FK-9IuhmFRNCUM1z8Ne__nzexqfXEjDME40qZMK3RBeuWxwr9iJPmasxSXMMiF1qEer12eA1ozmZJq00HqBIfeA0gMQqYDcIyzw8qYwPFVJA1rVY_PN4ikKrPE1R1RQhtXZFxq8f2RNQiYDsw3SAyS_uEPm2IYp8GEOlvy0MsYyT03XwX_QiC1GlZqKDGk8PGaKbDcjPscdVoH6sdE9d-0K-tuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی :  بخش زیادی از مردم و نمایندگان پارلمان بلغارستان با میزبانی از هواپیماهای نظامی آمریکا مخالفند
🔴
دولت بلغارستان باید بابت این تصمیم پاسخگو باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137843" target="_blank">📅 12:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بقایی:  موافقت ایران با آتش‌بس ده روزه واقعیت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137842" target="_blank">📅 11:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری /
بقایی: هرگونه اقدام آمریکا با پاسخ قاطع ایران روبه‌رو خواهد شد ، در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137841" target="_blank">📅 11:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بقایی: نمی‌توان اسم وضعیت فعلی را آتش‌بس گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137840" target="_blank">📅 11:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:  چند دور مذاکره روزهای جمعه و شنبه بین ایران و عمان برگزار شد که مفید و سازنده‌ای بود.
🔴
این گفت‌وگوها درباره نحوه مدیریت تردد کشتیرانی در تنگه هرمز انجام شده است.
🔴
هدف این است که ایران و عمان، به‌عنوان دو دولت ساحلی، سازوکارهایی را برای اطمینان از کشتیرانی ایمن در تنگه هرمز، با رعایت حقوق حاکمیتی دو دولت ساحلی و همچنین حفظ امنیت و منافع ملی ایران، تدوین کنند.
🔴
درباره وضعیت تنگه هرمز نیز تأکید می‌کنم که هیچ تغییری ایجاد نشده است. کماکان، به دلیل اقدامات تجاوزکارانه آمریکا و ناامنی‌ای که این کشور بر منطقه تحمیل کرده، تنگه هرمز بسته است.
🔴
این مذاکرات هیچ ارتباطی با آمریکا ندارد. موضوعی دوجانبه میان ایران و عمان است و گفت‌وگوها نیز همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137839" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در مورد ماجرای دو دیپلمات فرانسوی در ایران:
آنها به بهانه ارتباط با جامعه مدنی، مرتکب مداخله در امور داخلی ایران شدند و برای خود مأموریت‌هایی تعریف کردند که اساساً، طبق همه تفاسیر معتبر از کنوانسیون روابط دیپلماتیک، مصداق دخالت در امور داخلی یک کشور محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137838" target="_blank">📅 11:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a72fd89b2.mp4?token=iKgfclxTjhpwo9mf2Wbxeop0TrRSwU6liW4JITItEPd1Vk5EqzA7TR22jle0W_RKpCVqEEqtz86EZ3wDRfp458KZuFKvstgoD_d5mz7nFdVKfvvKaM4USWOlwcutOeS5QI98-DHNbCWnP03ziRuJgie9a-ReV0swzgFpEPXe0-VmqVLfrV43NYUsWsRqDxia5_Qo4b6rPP0UPc1BBLWozkAA0CuMQpOz7NCv_6Mlq9S-8KpBE7M1684JxfXdzalYq_ytS5MQHou40MA3K8zswR3CTjx0YwvRxREWHff3jAB1cBy_X_1NHcY_iKztUL-LVWy1OMvmAlqi5UqbqfgE-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a72fd89b2.mp4?token=iKgfclxTjhpwo9mf2Wbxeop0TrRSwU6liW4JITItEPd1Vk5EqzA7TR22jle0W_RKpCVqEEqtz86EZ3wDRfp458KZuFKvstgoD_d5mz7nFdVKfvvKaM4USWOlwcutOeS5QI98-DHNbCWnP03ziRuJgie9a-ReV0swzgFpEPXe0-VmqVLfrV43NYUsWsRqDxia5_Qo4b6rPP0UPc1BBLWozkAA0CuMQpOz7NCv_6Mlq9S-8KpBE7M1684JxfXdzalYq_ytS5MQHou40MA3K8zswR3CTjx0YwvRxREWHff3jAB1cBy_X_1NHcY_iKztUL-LVWy1OMvmAlqi5UqbqfgE-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: شایعه تعطیلی سفارتخانه‌های اروپایی در ایران را به حساب جنگ روانی آمریکا بگذارید که در آن استاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137837" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تصمیم‌گیران بلغارستان باید در قبال تصمیم خطرناک استقرار هواپیمای سوخت‌رسان آمریکا در پایگاه‎های خود پاسخگو باشند
🔴
اطلاع داریم که بلغارستان پیش‌تر نیز اجازه استفاده از فرودگاه صوفیه را برای استقرار و بهره‌گیری هواپیماهای آمریکایی، به‌منظور پشتیبانی از تجاوز نظامی این کشور علیه ایران، صادر کرده بود.
🔴
مردم بلغارستان به‌خوبی آگاه هستند که مردم ایران هیچ مسئله‌ای با این کشور نداشته‌اند. ما طی دهه‌ها روابطی مبتنی بر احترام متقابل با بلغارستان داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137836" target="_blank">📅 11:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etOcoDooijkbHARVUMmct4oALxNAYApGSWlOiCFAauEydXCIun7469R3XoamRxRBMYsnAU7zt_kexjAx-SQ2EjF8MuxVI8SkDBauc5Z1MzTmqvxUNcZLo_KIqlOsVsvdL61jam2Yptz6CSVKpQwn9Li_RcuSw2XvV8LenPN-5lXD7A00GiAjBhdK5phL22U6zqkm2rD3ufG8ZRW2xpXkO9rylBwBRV6-12StDYeMtK2WI0Vmshb7PKMtjXp02Kk0LdCXTjsghK1xVuR50OBWPsmb-Wb0s5topYhPbmRrQ0kHSr9_A4x6gW7jXx8GFdgw_CZk5d3Sy4J1kOA6qulogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماجرای عجیب قاتلی که همسر اول و دومش را به فاصله ۱۵ سال به قتل رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137835" target="_blank">📅 11:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : دو پهپاد تو مرز اردن منهدم شد؛ منبع پرتاب در حال بررسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137834" target="_blank">📅 11:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=eHdM4jUADq9aKPu_I398EOGKgMSlDG-h31GGTMSO475yVwzuPoFqgohHNY2Yj2cg62aveKibr-UZZOT5Y-90Nq60WDRWCPnJp6nToKJ2_YwbTP1Z-neq74NC4VcKGwZ2Pj6eMUhXddd5ViW5y8snSANV3QenvHH6wdKNmhiNoCrFudbGzzMEyDhVeIiWa7LtBromlxY-53q7Me8H_Ilu0H-0V0NZlnKp9Ss42MdGAfawpB4bs3w_Ub5WmYYvG2Jm72j7W3g0b1JQouwFFOcqqE1ZwadsM_S1SSimSi_7zev0zPQWUQE0XjTHWI09AxhGm0RMQUrWhmgtD5W13aCwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=eHdM4jUADq9aKPu_I398EOGKgMSlDG-h31GGTMSO475yVwzuPoFqgohHNY2Yj2cg62aveKibr-UZZOT5Y-90Nq60WDRWCPnJp6nToKJ2_YwbTP1Z-neq74NC4VcKGwZ2Pj6eMUhXddd5ViW5y8snSANV3QenvHH6wdKNmhiNoCrFudbGzzMEyDhVeIiWa7LtBromlxY-53q7Me8H_Ilu0H-0V0NZlnKp9Ss42MdGAfawpB4bs3w_Ub5WmYYvG2Jm72j7W3g0b1JQouwFFOcqqE1ZwadsM_S1SSimSi_7zev0zPQWUQE0XjTHWI09AxhGm0RMQUrWhmgtD5W13aCwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا می‌خواست در ۳ روز ایران را تسلیم کند اما حالا بعداز ۵ ماه در باتلاق خودساخته گیر کرده
🔴
تصمیم‌گیری دربارهٔ منافع ملی کشور معادله‌ای چندمجهولی است که در یک روند مشخص با مشارکت همهٔ دستگاه‌های تصمیم‌گیر انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137833" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رئیس پارلمان لبنان: اهمیت ضمانت ایران، عربستان و ایالات متحده برای حفظ ثبات لبنان
🔴
تنها راه قابل قبول، عقب‌نشینی کامل اسرائیل در کشور ما است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137832" target="_blank">📅 11:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97719a0a75.mp4?token=gAJkZjk-_JVD22TNvxnwsiFs1ayWdqhbcdsBFv1bhmMSpSsFenV_Uztv-3Fa9fRDrsof1YaM9NI2YEzu1gXqqMX9N5zD7gdBdB7e0gCqzK3bcR3PKO3WPwm-4VYj_lhmxqSiM1BIe7IsLJlYkPFFmCypYkqPQwRBXj3SPDPnoPD4Epv5ThsYSCP3Rj7KY2CNNXmIhy80K8aPLTx7_jJX5ZoYZYZ9wX5avAu7Kr9B9iOsEvigb_zB5V1WMv5bp-18eJnG4lKLTfs15p0byXfTG_htdAn3dQoCc9AHcPwGPM7pAd78xZv8P1TqVFb96rgjHr7NOhsDtmsps1AOstEctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97719a0a75.mp4?token=gAJkZjk-_JVD22TNvxnwsiFs1ayWdqhbcdsBFv1bhmMSpSsFenV_Uztv-3Fa9fRDrsof1YaM9NI2YEzu1gXqqMX9N5zD7gdBdB7e0gCqzK3bcR3PKO3WPwm-4VYj_lhmxqSiM1BIe7IsLJlYkPFFmCypYkqPQwRBXj3SPDPnoPD4Epv5ThsYSCP3Rj7KY2CNNXmIhy80K8aPLTx7_jJX5ZoYZYZ9wX5avAu7Kr9B9iOsEvigb_zB5V1WMv5bp-18eJnG4lKLTfs15p0byXfTG_htdAn3dQoCc9AHcPwGPM7pAd78xZv8P1TqVFb96rgjHr7NOhsDtmsps1AOstEctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: بزرگترهای زلنسکی باید او را کنترل کنند/ ماجراجویی خطرناک اوکراین قطعا از طرف ما بی‌پاسخ نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137831" target="_blank">📅 11:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQv_-YNWo_A6IFPSD2YBz4zUQOwfOwtuLi8qZhOIbBhc9VSNJI6BqACDRk71qCAZMaiQkUIQtE2Tw-n-dOtY8QiVgZYCBW--7J_Gx8d5fsOqsHKgQpMKRVTDOeXv0b52AxF0XU7xvRJ6moZVMawZgAH0_jbS2OSSVchYasVnhiLHzwQpvrlpFH8j5xSyBZNLSFyr8J_7EQ-IZK6M2eLuEnwY6tW3z_IlwrgBgZCVi152vDqPxZXTHzPO01pv63jTXeTZ4_Ly3MMzDVGZhwpas8Mwa6AeozbcQ9B2Awcr8K51S9h9VVggWu9G771-dCJwpoMnI4LOiyFRGRXqUQOubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvPDQTaXx_P_kC0qsuiSQmSCUgGSdLPjZQUTDBKmE-s6uxfl5DU4O0QcAWRKY4GwInuYu5g1zY9OlzGmsjGr_LATc6PRZi4bHIA9X3E7JcvUGwa1IAMFmb0EOI-8VFYwymETb86W51a621fj1F6Z1uKTI0tMviF6qIf3jKLDdSXgryERObl9DotbS5HRw8BvrfFxTY3JiFu4Zk6RtELrYJVPCB8Fa49xYGo0B8KE5ZviId5ukX8JhUVH_AnJPF8LsGelWLZfxsoTLB5Eq5GMGRXmW24nNtGh1JiXFAt8r2Hee6Kz_fZfCC4vY6KIa2H4o22Vn0nWI_ZGkytE7bOjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQ75LD1DpbjSWtqzj1-DeelxdZnGuhbExrYpCsH0c-oqtlOpA54ZmWIHUKHURsCaghFmBdYLkNwar56ZR1_7zpskPeUZ3KSXqmPNCVDBbj6eZJLIzh3cneAOKneY08NSlayeFJmvPln3xzt-JVvWPqoza7FwiPGWDRykkISfHbHIbU0lXCk6MxBYr8s8s3r6hLFUuVr5MiGG-spEv7TfXp-YkIv3ePk4p_9zBuYOBWOE1mE2SrFPyrV4xSMc4tfNI5KBC0qYhC5rWymd4X4e66BA01kHPkct3OKFC7TKWwBGQcE5ddJq-xyxSmLecraXFWjsyAqlf2qUM9spQK-7Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی گسترده‌ای همچنان در پالایشگاه نفتی جازان، متعلق به شرکت سعودی آرامکو، ادامه دارد. این در حالی است که سه روز پیش این پالایشگاه مورد حمله نیروهای یمنی قرار گرفته بود و هنوز هم دود سیاه غلیظی از مخزن نفت به هوا برخاسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137828" target="_blank">📅 11:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هیچ وقت اجازه نداده و نمی‌دهیم آمریکا تعیین کننده زمان جنگ باشد.
🔴
هر وقت منافعمان اقتضا کند دفاع می‌کنیم و هر وقت احساس کنیم از ابزار دیپلماسی استفاده کنیم حتما از آن استفاده خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137827" target="_blank">📅 11:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند
🔴
۲۱۹ شرکت خصوصی به‌دلیل عدم رفع تعهدات ارزی ۲۳ میلیارد یورویی به مرجع قضایی معرفی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137826" target="_blank">📅 11:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
اکسیوس اعلام کرد که دونالد ترامپ رئیس‌جمهوری آمریکا فردا سه‌شنبه در کاخ سفید میزبان ولادیمیر زلنسکی همتای اوکراینی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137825" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سی‌ان‌ان: موساد اطلاعات کوه کلنگ را به آمریکا داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137824" target="_blank">📅 10:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ولیعهد عربستان، محمد بن سلمان، در گفت‌وگوی تلفنی با نخست‌وزیر بریتانیا، اندی برنهام، درباره تازه‌ترین رویدادهای منطقه گفت‌وگو کرد.
🔴
نخست‌وزیر بریتانیا یورش‌های حوثی‌های یمن (انصارالله) و تهدیدی را که برای آزادی کشتیرانی در دریای سرخ پدید آورده‌اند، محکوم کرد.
او همچنین بار دیگر پشتیبانی بریتانیا از امنیت و فرمانروایی عربستان را اعلام کرد.
🔴
دو طرف درباره گسترش همکاری‌های دوجانبه و همچنین بررسی رویدادهای منطقه‌ای و جهانی گفت‌وگو کردند. محمد بن سلمان نیز گزینش اندی برنهام به سمت نخست‌وزیری بریتانیا را به او شادباش گفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137823" target="_blank">📅 10:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44efd8a92a.mp4?token=U0kJk-cnwi2aacLndhVlgD-acZQAgDpmH9RqudML2mltOVFWkWp_vGyx6pBgzpA8MjJP8mZdic-jwlyWT6RxCd26SnbUBcfNOiS7ppeZ7m61YBT5mUDhfJeglz7S1s-GOIxFg5yNcONulCoUe0NB_eCRhnpthhNYUl_C7m9M9FwF62-hX6d5ryWPWWw35DmLfmk8dq2Recxfjtc2roqXEut5Up8GXHlPKvE9Vx1w-T3-PKbMuteQgnN_AVq-FCfIwpmGYwkgR9nx0hG1oMP3K_oReNxYmctK-D3f39AqUao76DkAlkvU1bwvRE03QS-JCPobgmBVkbq0ko8TiwPG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44efd8a92a.mp4?token=U0kJk-cnwi2aacLndhVlgD-acZQAgDpmH9RqudML2mltOVFWkWp_vGyx6pBgzpA8MjJP8mZdic-jwlyWT6RxCd26SnbUBcfNOiS7ppeZ7m61YBT5mUDhfJeglz7S1s-GOIxFg5yNcONulCoUe0NB_eCRhnpthhNYUl_C7m9M9FwF62-hX6d5ryWPWWw35DmLfmk8dq2Recxfjtc2roqXEut5Up8GXHlPKvE9Vx1w-T3-PKbMuteQgnN_AVq-FCfIwpmGYwkgR9nx0hG1oMP3K_oReNxYmctK-D3f39AqUao76DkAlkvU1bwvRE03QS-JCPobgmBVkbq0ko8TiwPG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های A-10 وارتاگ درحال اعزام به خاورميانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137822" target="_blank">📅 10:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a9d77e38.mp4?token=VhxPSVinMq7kaxLB-ajue8ifbNoOnK1Aq0dd58VwR4jAoI5nEZB5IdhfvZBjtpUSZ633z0193L8mBnwBCsq6Ag3HeJRvkP72oAp6hbAXGKgYYPfnHxoBN7BY1yEeTHU-MmUYAcg2YSRJq77LXlfVGSYp4XC1y1y7fMtQH6h2M9XVno41jOEV1fZ754NY6cy6k0M8uPQ3ntB1zw7tQzlxeLpC8grarJhttBxQNSks9WMY1ySKbq6cwFcRYnjXHmxreYEAZYKw5eRZK2sGMfyQi2w8KFqDvDLkCf6WxdfytX1p8snL0QQecvs1cKRf-Jv79xYG8xLQwhCzGhmgMVNUoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a9d77e38.mp4?token=VhxPSVinMq7kaxLB-ajue8ifbNoOnK1Aq0dd58VwR4jAoI5nEZB5IdhfvZBjtpUSZ633z0193L8mBnwBCsq6Ag3HeJRvkP72oAp6hbAXGKgYYPfnHxoBN7BY1yEeTHU-MmUYAcg2YSRJq77LXlfVGSYp4XC1y1y7fMtQH6h2M9XVno41jOEV1fZ754NY6cy6k0M8uPQ3ntB1zw7tQzlxeLpC8grarJhttBxQNSks9WMY1ySKbq6cwFcRYnjXHmxreYEAZYKw5eRZK2sGMfyQi2w8KFqDvDLkCf6WxdfytX1p8snL0QQecvs1cKRf-Jv79xYG8xLQwhCzGhmgMVNUoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بازرسی:  تراستی‌ها (افراد مورد اطمینان حکومت برای انتقال پول نفت) خیانت کردن، پولا رو برداشتن و زدن به چاک
🔴
جالب اینجاست تراستی ها رفقای همونایین که میگفتن تحریم اثر نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137821" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۳ تلویزیون اسرائیل گزارش داد که بنیامین نتانیاهو در نشستی با وزرای کابینه اعلام کرده است ایالات متحده خواستار خروج نیروهای اسرائیلی از غزه، لبنان و سوریه شده است
🔴
به ادعای این رسانه، نخست‌وزیر اسرائیل قصد دارد با این درخواست آمریکا مخالفت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137820" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137819" target="_blank">📅 10:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روزنامه تلگراف:در آغاز جنگ، اگر یکی از سکوهای پرتاب موشک ایران توسط نیروهای آمریکایی منهدم می‌شد، ایران برای بازگرداندن آن به چرخه عملیاتی به حدود ۱۵ ساعت زمان نیاز داشت.
🔴
اما اکنون، ایران توانسته این زمان را به شکل قابل‌توجهی کاهش دهد و قادر است در کمتر از ۳۰ دقیقه حملات موشکی علیه پایگاه‌های آمریکا را از سر بگیرد.
🔴
به نوشته تلگراف، این موضوع نشان‌دهنده افزایش سرعت بازیابی توان عملیاتی و بهبود روند استقرار مجدد سامانه‌های موشکی ایران در طول درگیری‌های اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137818" target="_blank">📅 09:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شبکه المیادین گزارش داد که نیروهای مسلح یمن طی ۴۸ ساعت گذشته سه نفتکش سعودی را هدف قرار داده‌اند. این شبکه همچنین مدعی شد که از روز دوشنبه هفته گذشته تا روز یکشنبه، ۱۶ کشتی سعودی که قصد عبور از تنگه باب‌المندب را داشتند، موفق به عبور نشده و ناچار به بازگشت شده‌اند.
🔴
بر اساس گزارش المیادین، این کشتی‌ها اجازه عبور از باب‌المندب را دریافت نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137817" target="_blank">📅 09:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL8d_QJxFQs71EHVa6hfz4qukD0CJcStqfSii7rVfgReSwu4VRVVIqin5qbE9ktkf1Gy-XR2mgwVgl5vpbK0E620EBKJXQi71TRwEtdTdkrLSSidgJOt4XTQzOJhxVql5uh9O9VN8HhYGCJ0zL698wDdgB94kU62TBiyZTxSsbGK5YuxdkJxJeh4U6q12LldGU_ElXUPH__5tJIVErlAwbjxvPTmzgupXKAPBOfcxou6IrTaVw7DP5W-MMCuFsO8ugorIqI091YNl7VmYV834STwAE2clZROr-XPvDfkWyP-O0jJq_oDeRTv9hKOAi83vCbe3QeHAcNAtGmrb1U5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت 92 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137816" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCF-Yn7KVnqnAyr_MfqIXW5W1JQYprxucPJHJTBDuQ4h7XWCxVvmUg4V1sTqzU8xZTWQaU-Iq_cHq_wly-z3wvTCCb-zUJTUGtzoeMSDK_EvgqKtqBIMiRFK9DzyntcPVHi9Wma1oQWGzTxz1oh4RwvbrCZOkFGSVU9uMaQwgjcR0LjDBnxMXt64ojzNamOkdmwSTA3n0cPs94zhjaziZs2j2_pWJN4y2GyuIXXkbSQ7kzkKPWP3DWQgNGLEhQitVVy4jECpKGM9p6aerNgMDUBAfgTVIDl8FMDPQ1UBxzn_MH6IAv50Xqm_yb4ZBjieBWKbFZngIO-GYE1a_f2khQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران هزینه داره و آمریکا و اسرائیل این رو خوب می‌دونند
🔴
اوکراین هم ممکنه به‌زودی بفهمه که ایران اقدامات علیه خودش رو بی‌پاسخ نمی‌ذاره
🔴
فهرست کسانی که دچار اشتباه محاسباتی شدن، همچنان در حال بیشتر شدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137815" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سی‌ان‌ان‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
🔴
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
🔴
از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137814" target="_blank">📅 09:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیویورک تایمز:مسئولان آمریکایی اکنون نگران هستند که پوتین و شی جین پینگ ممکن است کمبود مهمات آمریکایی ناشی از جنگ ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند: در اوکراین و اروپا برای روسیه، و در برابر تایوان برای چین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137813" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کیهان: فریب آتش‌بس ترامپ را نخورید؛ ذخیره تسلیحاتی دشمن ته کشیده، وقت شکستن محاصره دریایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137812" target="_blank">📅 09:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رویترز به نقل از داده‌های ردیابی دریانوردی: در طول تعطیلات آخر هفته، روزانه کمتر از ۱۰ کشتی حامل کالا از تنگه هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137811" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک پست: سناتور جان کندی روز یکشنبه مدعی شد که ترامپ دوست دارد هر روز به ایران حمله کند و از آمریکا خواست به‌جای تعلیق حملات برای اجازه دادن به ادامه مذاکرات، فشارها را تشدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137810" target="_blank">📅 09:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2054add09.mp4?token=M5k00xP70DxYvFmxD79kE3Uw60SOa9WMIdmwrGHDBB9mVZvRQzMo_rRkfbgLXuaNJO-nF3JiJptLoDt2cChfdmNlPN6btghUpx3jjy3AlxPZVTOHe33xPe0j8h-lH3QmptolNlfComSqOKSPNIUAiYT6-SisoDLxtZhdg2ah-gZmdAh1XaByvKYN6CDtFlmWZ6pyOvYiUOgq9ofLnB3SLFuxcEs5JW6f9uoWAIjESTLBQNXddQyotwMaA-IYZ68Wh_U_5UCdphicE4wlZr5hAFWe54XZIrHg9IH7OhKQVWXVnYkNVQUOk7GO5wyASoCLY_lJmhW-C8tTcevMe2wMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2054add09.mp4?token=M5k00xP70DxYvFmxD79kE3Uw60SOa9WMIdmwrGHDBB9mVZvRQzMo_rRkfbgLXuaNJO-nF3JiJptLoDt2cChfdmNlPN6btghUpx3jjy3AlxPZVTOHe33xPe0j8h-lH3QmptolNlfComSqOKSPNIUAiYT6-SisoDLxtZhdg2ah-gZmdAh1XaByvKYN6CDtFlmWZ6pyOvYiUOgq9ofLnB3SLFuxcEs5JW6f9uoWAIjESTLBQNXddQyotwMaA-IYZ68Wh_U_5UCdphicE4wlZr5hAFWe54XZIrHg9IH7OhKQVWXVnYkNVQUOk7GO5wyASoCLY_lJmhW-C8tTcevMe2wMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو موزه ملی کره شمالی، جلوی تابلوی کیم جونگ اون، رهبر این کشور پنکه گذاشتن تا گرمش نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137809" target="_blank">📅 09:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
خبرنگار: آیا نگران این هستید که ایران به خاطر اتفاقی که برای کشتی اش افتاد ممکن است به اوکراین حمله کند؟
🔴
زلنسکی
:
ایران از قبل به ما حمله کرده است، زیرا سلاح‌هایی را به روسیه ارائه می‌دهد، امیدواریم جبهه جدید جنگ با ایران باز نشود اما ما باید آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137808" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77fd55a10c.mp4?token=DG_S0qaHg1zZ9uqyAa7cSGYLV5Ik_AMbvtWsbO3cZ5NvwBtIIY5xUGO1BfIbgvj7RJxNr62Rw0MVTDeBtMrUCI5iJL4QwOhxYCcuLwFQ2FOBnkwwLEkvLWn3tqYSxzQX5cQd9oVSJNV0OgD4vAfHM2Bf461wUJCpLzoFvo8_Pwx4-2yTFNi53v9I_VRYE6J5t6g1bGXmfhhSWzSdi81jVFQKg6SgeyDkUwTtmvjNe6OZUA4_6C6hHMLOeWth8elOxNgiFvO3ggEB0rHqhW86JFh3RAN6zRVgq1_wbdRAYYOPCgJlV77dgTpA0u9Z3DzpLjazj9GPMxSpKFWXei7XjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77fd55a10c.mp4?token=DG_S0qaHg1zZ9uqyAa7cSGYLV5Ik_AMbvtWsbO3cZ5NvwBtIIY5xUGO1BfIbgvj7RJxNr62Rw0MVTDeBtMrUCI5iJL4QwOhxYCcuLwFQ2FOBnkwwLEkvLWn3tqYSxzQX5cQd9oVSJNV0OgD4vAfHM2Bf461wUJCpLzoFvo8_Pwx4-2yTFNi53v9I_VRYE6J5t6g1bGXmfhhSWzSdi81jVFQKg6SgeyDkUwTtmvjNe6OZUA4_6C6hHMLOeWth8elOxNgiFvO3ggEB0rHqhW86JFh3RAN6zRVgq1_wbdRAYYOPCgJlV77dgTpA0u9Z3DzpLjazj9GPMxSpKFWXei7XjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهین‌های شهبازی به پرویز پرستویی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/137807" target="_blank">📅 07:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6494dac8a.mp4?token=o9-uq5LjUEj811jfsIJMgKEEvon07cwSaKpRWDYTsjeb5u34-RS3aJK9NqNKKwXYV2s_cCUoSNNOuc8fYkCPcUUBXwIYAkYan3W76AlvIV-kWoLqsI_M7fhvWjgZ89UqHkGsCTIMrhxyknBCoj4DCf_UCIHMGpANdx09z_z7ShwROR0O_mgyWDsxI7xoYx6K1-4TbpST77ZdWTEpZrCh7XNjPkUKz0OdULACzVS0LbhV8MUzJzyeJp8HBrNBg0fbyR2LmIf0g0W-Z7Et0AOg-kRKEHgrca1lwZe2WTkyhvCptw6_v7ON1mVVSnflrOdq3guRKHLydh6pIG1QVGuR1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6494dac8a.mp4?token=o9-uq5LjUEj811jfsIJMgKEEvon07cwSaKpRWDYTsjeb5u34-RS3aJK9NqNKKwXYV2s_cCUoSNNOuc8fYkCPcUUBXwIYAkYan3W76AlvIV-kWoLqsI_M7fhvWjgZ89UqHkGsCTIMrhxyknBCoj4DCf_UCIHMGpANdx09z_z7ShwROR0O_mgyWDsxI7xoYx6K1-4TbpST77ZdWTEpZrCh7XNjPkUKz0OdULACzVS0LbhV8MUzJzyeJp8HBrNBg0fbyR2LmIf0g0W-Z7Et0AOg-kRKEHgrca1lwZe2WTkyhvCptw6_v7ON1mVVSnflrOdq3guRKHLydh6pIG1QVGuR1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدتقی نقدعلی ملقب به شپش:
آمریکا و اسرائیل نمیتونند جمهوری اسلامی رو از بین ببرن، ولی این وضعیت برهنگی مثل خوره به جان فرهنگ دینی ما افتاده . سریع اجرای قانون حجاب اجباری رو راه اندازی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/137806" target="_blank">📅 07:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj1GHz-KOUkGw-1P01qEmAntaRj-8dqa6MCINZphBl3YL9I4X0TYmUs0ylVr-_FZokCm7bqOKl0jsBfcAWGR8az3F4jxj3b7VTkxGAu5cpd6r-fVLRqTiL3Xh1SsQojq5U8PnJCwrcNMVunb-Xs6_OryiSJkWLt-HgKVmQ6L-l8z8m1SruB6mCYWsi_1q2iGm_yVqUwWZOYg57xRiZvMoZnC4_HfFULjQp5QX6nWSpD3lY9M9zAAvqgqoAZKbts62ZPp5jnO9a0YvxMGdG_YImLfBu05MLKo8k9-zVBS9ry7SRPQUNNc-2GdzFL7rtjq55_PVSwT9Azsia8Sfd3tMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/137805" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sklPqnC3DI_EiV77R-T5v5eCUiHH7EbNZ07D8DeT5DFKnNNulishe2CnfP6wIPDVyh6xhu7kdUTzoXWpMJRrTpgXVN-M1PaGuuSMFQF0pU_IX-eAUDAMjyIfJVTH2_dDIpwhfAS5g1z-9RrNXPqbjSQUCfT8znra_e45DO_ouRYA3XURcOftLeuyFEXMeX6KI-7WS7IPCvkYlk8b-ZYLaCx5uVDjKsZCuucqcjZeKPTx-Sli60cXccB2mRMxNNkOibquVHHLdWCbuWYjO8AXdcCU7q5lntdmSiFGYO5rLB1VOnfF-Y2P4qdi87Yp6Gw1jLGE37HfcweTiZ94WPLGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلوی هست.
حستون رو با ری اکشن نشون بدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/137804" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_e44PjddYWHkPSsNrWYCXBhdiQqRmtDEkxGE26kVezKnVZbmMcsY_cHhvj7syXidYo6Nu2SqL4MIP7ycVU370OxszHqsTjYPb9i6OYr8Z1TrYuy3SlF242FnWzH2dyG2P7_48ad1XhuT-hozWMhiVRn7yWSfDY9sofTfN8o0jlGgdvyt-xr_fTkf7vWUyx1KRDVtL6yJiO7b5fN5J29_2bXlbM_byMLQ8myofQH_6MRXiB77aXrgYA6RVImBpEBlcxc_-yRM7w16Pis4N_-QEIVk1wtPkaGT0YRLuUloorsu8fejy8OrMy7dxgYJnhCzT69Fx6Rs88LM2nIAjaN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک منبع نظامی خارجی: به نظر می‌رسد نیروی هوافضای سپاه پاسداران در حال آماده شدن برای تلافی حمله سرویس امنیتی اوکراین (SBU) به یک کشتی باری ایرانی در دریای خزر با استفاده از پهپادهای تهاجمی یک طرفه است که منجر به کشته شدن یک ملوان غیرنظامی در آن شد.
🔴
کی یف تقریباً 1850 کیلومتر از تبریز فاصله دارد و این شهر را در برد موشک‌های بالستیک سجیل-2 و خرمشهر-3/4 نیروی هوافضای سپاه قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/137803" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufBo3to-97oAbl4NRk6IKfJeTvC6xZ7ZMqOuR6HYDSGInxDfKbVpN_etntPXtBc2L-v9LQ6u9iADsBDbPiDFyuhyp9W69gbIKLJao7hzwSjiq4e9Asp7J08UHZYr_qPIO_jJpGQU8EcijvNoB4QQkggcT_RgChbSss6nN-igJWtO3czewHsVpaRlrZPEEvs17u9bFGGP331QnX2YqhvK77Vw10aWxBu-DQDlqvsUeW425P0yiDXmme49Ro3G73MpTqCu_t1H_WydtMKmitexDGYl1DOcn5w9AI1dKASnmL5v1EevH62rcbPo7BaEDHz9UQjFyAT8WObs73ERkiLquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ادامه خودشو تبدیل به دکتر کرد و نوشت:
این ستون مهره رو میبینی؟ این دقیقا چیزیه که می خوام به جمهوری خواهان برگردونمش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/137802" target="_blank">📅 01:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-C6HVHJcJ5hQVwQ7lp7PmI24ORdiL3UuJuXsYbiUE8Zboy9f8sSFyPfp_jDT7MWFQp-uSMqaCo2mV1KKsma0F5zbAs93AKvazGPxJAybLPEqeNS4lK80VeqvJi2tD2l9zrkZpFiiRBDW8I4H9vFOPoPKwb5rAH0wv-u5zLWYnHNUJBCwdqoGC5x9xnrHyZwrGYl-W7nOvKPouZY5UOYOhkIfgAXE2WIDBoA4MC2sX-Gs6jA6E7muOVEyN7oYYHTJaqjTwuDpDb_TNdTb4Wv4dKSX55GLMICok-1kqQjVfFjwDb1xG8VvxS57VYEGKlQNffAxWnuDL03QwhwpxJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: این نفتکش حالا متعلق به ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/137801" target="_blank">📅 01:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137800">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گویا آرام بعد طلاق از سپهر وارد اونلی فنز
😐
شده و داره تصاویر... رو به طرفداراش میفروشه
😐
چندتاش رو خریدیم و گذاشتیم
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/137800" target="_blank">📅 01:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG6pXlRuBzxIIS8Wcb_SetsEbm9Kcboma3DxrAV77z6LK9tE3NEiZ6czsjbord9lLQdb7QQfGYo1KISuYcDLERoZPc_-pjE3AUIYnYvz_OgDCXNIcLTFg6-9LQ7S7Eozc_GRvOqsH4LZGdTbQNFYwNoXoHXozTh4wLmWFemmo3De91pYN9cKCCJR95hm-gn6WGcc_IOxSt9I9TI1rqOzqYjITlNXiIsHB7d4_b1iULcjyU7ilQkHt3N9H6YBh7yMnNHDNCfyT3mAB-GXkd5zbHgPD8cmOdciGdPMXQe89blrmOn7vb43QR7w7mjW1FuZPFwt6GqpAJxDQiOVwM2F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت فروند هواپیمای سوخت‌رسان و یک فروند هواپیمای هشدار زودهنگام E-3B آمریکا در نزدیکی سواحل ایران در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/137799" target="_blank">📅 00:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv0tP_DElC4xbBeP2JOufMv7VxsbIhUqrGYcdqGWqr5-bW7yJIYa5mb3hcvx49AdkT4A1Yt48OsZdyG6z1ivImenvOwTMtHaaNLBX1DOzDt7vP0J8bpVUP3-evv_NZWBee9YxV4tK2BXIFo5Tu70CNPgyP2loyGOIvjcNv-J_Fr8NIlved70ymNgeF19bneV2FgE1lhHKUlXTxxDFHcSctgXiAUQrrVuQI9oZxiIOxKrN1m-Au_ytAd828xMbiNEAJsRJ5iNz-P8qziemKxIsF6iLexHbTi6wcEOgDXKFk43Sy4RkAYds0PbhZ7bQF3Yinao8-wjIFzF8amnDiCksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید دونالد ترامپ:
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/137798" target="_blank">📅 00:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca4847374.mp4?token=uluX-FnO8ntJD4EYXaEHH9cb8dhektlnuuXcvwIaxauVJy_gdGVUYxJKxxebdlbHnuWzxNoG1mSagi_7nkx69R_7yZWTCcPBPwSRihQYNmw9DwbuvbKL69wGxvIZzQIPnIB_hYiOB96B3ADodWu2uf0IB_jODzwcbaItLpxO-dK7hApEaS5Y98OBJD7E0Z9r80fKwYKdkDIWlb4HBe8m7gPsDhXtJK4P7QFlJqC69L0nJR9MssGT2-HPdiyxaTWgVUWbGCub6q4jq47onp5L0JGdNy8FdvhupD-0ZzbpwkqpLpohDytEhv97W-alKiLSHvnDypvyhTNtmWzCLz-doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca4847374.mp4?token=uluX-FnO8ntJD4EYXaEHH9cb8dhektlnuuXcvwIaxauVJy_gdGVUYxJKxxebdlbHnuWzxNoG1mSagi_7nkx69R_7yZWTCcPBPwSRihQYNmw9DwbuvbKL69wGxvIZzQIPnIB_hYiOB96B3ADodWu2uf0IB_jODzwcbaItLpxO-dK7hApEaS5Y98OBJD7E0Z9r80fKwYKdkDIWlb4HBe8m7gPsDhXtJK4P7QFlJqC69L0nJR9MssGT2-HPdiyxaTWgVUWbGCub6q4jq47onp5L0JGdNy8FdvhupD-0ZzbpwkqpLpohDytEhv97W-alKiLSHvnDypvyhTNtmWzCLz-doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرف‌های حق شهریاری به جوانک مینی کمونیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/137797" target="_blank">📅 00:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/137796" target="_blank">📅 00:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKBVVKWGsNwe9DDxkHIY95IWc7IuTg1n3atKJQVCr95aa3LBjG_hPIWbEjiIBr4m-BhmEieUDWkJR0dB_cMnaAkUnpVRhsn891-1t6ByH2nZYPbzFo6DvYtnneFW5cwi-TNxgVSQ8rjfAdZ_sfPoQYdHo0dCVq5T6l0vCcRUhjpSKa5xFiYHjzz2aBBB8LA3ygwdIkCTVYVuwuQz61DjUM6zVFpJ_8XvSIKoAhZEhku0frjAK6JgoO2MxC2oe5yrPKo0NUYAqRftW1_wCPYIGra3zrRJSpwtUMBdNYjYTi-c6i_28nipcD1_oKuJHbhfpMhwyq0aIuG8DoeRK40k4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆕
کانال میلیتاری خبریه
@Breakingpersian
@Breakingpersian
📌
رو داشته باشید  لایو 24 ساعت اخبار فوری جنگ</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/137795" target="_blank">📅 00:31 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
