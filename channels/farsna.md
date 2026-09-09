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
<img src="https://cdn4.telesco.pe/file/YkBAmxpM1qMvavHojMnzuxqEjN_7pE690vnV_H_QW8qGWMps_-_QYuTsV-6d8QVbOAkJMAE6ce5mKVlaxaEyokhSNiiD4kJ9-_COQVmWISry7w0CB1ElwxQvUWtFWN9N_n5nyXx6svPTL8p-dxCnmveoRea48AdOaaHn5u9EhU-e7MMEOt2CoA7DnavPLPoKy7-2fU9EOKRD0TA4zofJ1YB5ChTJnT72jzWEzrByXPTHzPMVxW7aq9RD0fdhneJNo5hiiuwtsh_WN_LUzazI69lSKDef2dQBru2safT95mwX93cMaWsWyz-NBuMi0ybTDIdBSYaaHQgMoJ0hU9kckg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 22:26:57</div>
<hr>

<div class="tg-post" id="msg-461148">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db4f0dd22.mp4?token=aEW4dWb0mgwDDHMYfFiMoD8aYrk7tOS3SbBBZEKfLs8zoT7qqYLunQZx7rs9VxVTz9dU2S4No2yXVKWk_72GMAhMY_rGWVI8EsBZetLU8ucmkGi9wdm1Okkwnm5bNRt3TcCOEU6RCVsNhNFEbuVtDPCsFWFw0EpTdHrHnHPXDSskWqr_eJ5Q2tF-hmNGMp797cw3E3yy2lkCkvaQmLgQ-nayBvPlGyaI0t8F_7dtJonvSfpDbhgxrkyOY1k1azOs5cxCLZUgeokcWYYDf-lmlyGJf9_2mr28PMW7zSygwW_i0X8tTCGClbvF1koDm6VW1Cid8e_Sgv3hwuLyM5VDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db4f0dd22.mp4?token=aEW4dWb0mgwDDHMYfFiMoD8aYrk7tOS3SbBBZEKfLs8zoT7qqYLunQZx7rs9VxVTz9dU2S4No2yXVKWk_72GMAhMY_rGWVI8EsBZetLU8ucmkGi9wdm1Okkwnm5bNRt3TcCOEU6RCVsNhNFEbuVtDPCsFWFw0EpTdHrHnHPXDSskWqr_eJ5Q2tF-hmNGMp797cw3E3yy2lkCkvaQmLgQ-nayBvPlGyaI0t8F_7dtJonvSfpDbhgxrkyOY1k1azOs5cxCLZUgeokcWYYDf-lmlyGJf9_2mr28PMW7zSygwW_i0X8tTCGClbvF1koDm6VW1Cid8e_Sgv3hwuLyM5VDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به کشتی‌های ایران حمله کردیم و حملاتمان بیشتر هم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/461148" target="_blank">📅 22:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461147">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954e22293b.mp4?token=MOiLFrtTmFOJtNGSsiAm_ddeYiYdLF6kCDR2Mhy7rDvcN_yHEInI0xnCUj-1lYnZDgVXp_SFA561jEpcuRVG8XP--5387-Ztlzak2ESnJM3ecvqa4HuiKXDzhJFE9Ri5lT9hnVcQ-CibvoNzB-YvUJhvBrlF59rjla3MrdYdOWqBVuAERNv0Ge3vJSdbAy99iGgzAN8aAHbBeM7CXSY5tx_KDhXKx0wY9bkCo5_Uq93CGNyDsMnAfbnXPO8ZPEjFsUDDFF-64zOo6LTH2lrbR1hijGiuXjIYVLF06b_0SWLLil9XeBzCqDSNFA7YtoR0jxjUUyLNEIVFUsRJpPVc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954e22293b.mp4?token=MOiLFrtTmFOJtNGSsiAm_ddeYiYdLF6kCDR2Mhy7rDvcN_yHEInI0xnCUj-1lYnZDgVXp_SFA561jEpcuRVG8XP--5387-Ztlzak2ESnJM3ecvqa4HuiKXDzhJFE9Ri5lT9hnVcQ-CibvoNzB-YvUJhvBrlF59rjla3MrdYdOWqBVuAERNv0Ge3vJSdbAy99iGgzAN8aAHbBeM7CXSY5tx_KDhXKx0wY9bkCo5_Uq93CGNyDsMnAfbnXPO8ZPEjFsUDDFF-64zOo6LTH2lrbR1hijGiuXjIYVLF06b_0SWLLil9XeBzCqDSNFA7YtoR0jxjUUyLNEIVFUsRJpPVc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌های مجلس: نبرد هرمز تعیین می‌کند که نظم ایرانی حاکم همیشگی منطقه شود یا نظم آمریکایی
🔹
غرب آسیا آن‌قدر ظرفیت ندارد که بتواند ۲ نظم را تحمل کند و در نهایت یکی باقی می‌ماند.
🔹
با ایستادگی ملت ایران نشانه‌های پیروزی نظم ایرانی به مرور دارد نمایان می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/farsna/461147" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461146">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است. @Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/461146" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461145">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3jp6SQA4LlCUcfki70TE-qlV-fViMljdjfTfNj6BeK4HqYAuYUL-zhyOa4VvpRZAs7_duy4YlVl8C3Rx4GqycaLPnKOnk_w1EdlsenDrSvO0yATkfb5h2EPe-6dL9o-pcpSrBjEHqE9hI2okdvfEApHZZ4u0u_m7XhRtgzrKcO-CVQyNJEbIaj2g9uC1A-3jxbfbyK4SmTPSUCj1VNtTb_FqJOXnFovK7peBw99P3Ln8V2sMt7Ijz2hjKkWMiKjAAoJTHN7ImOpxE0rBZYobsKtscT_Z1cIWeLPY1eLmUs221hhFln_ltKiH0ZHYeXV2uqt1_B9m5dqbm93VvR4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است.
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/461145" target="_blank">📅 22:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461144">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38fef9656c.mp4?token=WgKoxARVBWMvyZM4h-9NZyhfmdoj899MwyShQBDRIMPqA6NgmhGPtCZ1wkFucgkW1jyFbc5zD_-BhMkUx15auorQflq8PR-nw1XanPmYPCacwxYP669vYaJ4Vg5RcbIc1Y-OOpo8ExOA2Mm3TnUoqfokca0gqbMbYBYpfTOmq1wdcdD_1AsuQ5tLq_V6y9gW4Ym9_iGz45Px67zfBBlLIgE5SewQYWsZSv4Po3A04SZs12fUYurVrbIODrDDYusSD4MS_DQADG-G11SjuhRB0cWBMhhfjaJJn1ButVIb05xQRaxFjBTzdPfiydu9R_QlZPz7wt3zXCsHzeUCT3vjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38fef9656c.mp4?token=WgKoxARVBWMvyZM4h-9NZyhfmdoj899MwyShQBDRIMPqA6NgmhGPtCZ1wkFucgkW1jyFbc5zD_-BhMkUx15auorQflq8PR-nw1XanPmYPCacwxYP669vYaJ4Vg5RcbIc1Y-OOpo8ExOA2Mm3TnUoqfokca0gqbMbYBYpfTOmq1wdcdD_1AsuQ5tLq_V6y9gW4Ym9_iGz45Px67zfBBlLIgE5SewQYWsZSv4Po3A04SZs12fUYurVrbIODrDDYusSD4MS_DQADG-G11SjuhRB0cWBMhhfjaJJn1ButVIb05xQRaxFjBTzdPfiydu9R_QlZPz7wt3zXCsHzeUCT3vjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهرم در شب ۱۹۳ همچنان پای کار مقاومت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/461144" target="_blank">📅 22:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461143">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس دانشگاه سمنان: شایعۀ تعرض دانشجویان عراقی، دروغ بزرگ است
🔹
رئیس دانشگاه سمنان: بامداد دوشنبه میان چند دانشجوی عراقی و ۳ رهگذر، شامل یک زن و دو مرد درگیری رخ داده و به زد و خورد منجر شده است.
🔹
براساس گزارشاتی که در اختیار پلیس است، آن ۳ نفر حالت عادی…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/461143" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce568ac68b.mp4?token=ohUu9Ri0G8G9_gb6EL0w6HvYBCJz6BTBdxz-XGc3GylD_Hk2eSKy-QXEHmmvns007NMByosbCYU9a3YZajHGcDWs-MDxIWUmR3b34Oe2-L0dvA7x2N-FTAg0ZKFgYbFEjZhDT5gFHjR-qWw7Q1cQWX6Y4puLKE3sjiDvZfaQcJKr6WZSLloXD57syCkZ5ewyF7xDyUbaizX7atwwumwkXbWkCOLu_zjgmK6P6__PruW3lKMJJasAKHhsFHwuWgG74xkBbxlX7aNMVM-rMWbTcbKQz9fHkCcmF2LRdoRGpk_-cwYploT4I7dnQFGgpdd8LpQYsUCaMRqu71X_NSk44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce568ac68b.mp4?token=ohUu9Ri0G8G9_gb6EL0w6HvYBCJz6BTBdxz-XGc3GylD_Hk2eSKy-QXEHmmvns007NMByosbCYU9a3YZajHGcDWs-MDxIWUmR3b34Oe2-L0dvA7x2N-FTAg0ZKFgYbFEjZhDT5gFHjR-qWw7Q1cQWX6Y4puLKE3sjiDvZfaQcJKr6WZSLloXD57syCkZ5ewyF7xDyUbaizX7atwwumwkXbWkCOLu_zjgmK6P6__PruW3lKMJJasAKHhsFHwuWgG74xkBbxlX7aNMVM-rMWbTcbKQz9fHkCcmF2LRdoRGpk_-cwYploT4I7dnQFGgpdd8LpQYsUCaMRqu71X_NSk44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌به‌خودی جدید ترامپ در تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/461141" target="_blank">📅 21:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461140">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌ سخنگوی وزارت خارجه: کشورهای متخاصم با الگوی رای گله‌ای علیه ایران رای دادند
🔹
تاسف‌بار است که کشوری مثل ژاپن که قربانی سلاح هسته‌ای بوده به قطعنامه علیه ایران رای مثبت داده. @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/461140" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461139">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌سخنگوی وزارت خارجه: اقدام شورای حکام علیه ایران یک تناقض آشکار است
🔹
عدم دسترسی آژانس به تاسیسات هسته‌ای ایران ناشی از حملات آمریکا و اسرائیل بوده و ایران مرتکب عدم پایبندی نشده. @Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/461139" target="_blank">📅 21:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461138">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Illxirs7dONBcCvyMXW-G19L4Om43dh983qkMRYe9A_FviE1kGkty_Iyd6z0I4_2rpXdg85KFPfgLTPwnNsbxSJYImTjC2-VaRU18iajsfTy6wpsC2kZ4uagLy4ivbC0KuWoyzS9QS8SSO-DU4LSGMIm5IGTvpp1z5lcEIZrQpPJWNGpTxyRLcmol9M7L2P7TXn7_89xVg7Qm7YqTA57JEA2cJvHlnVzjxOd9LpF06t97Mbu4btlpCHLDCsSoXb-jinHNzMffTvC7MDVcs3lz2qQOs3TaKc-V9JGZnHwQc-vWA1qCJRNSN8sz-sqorrTkRnfwLAgsNb7iN6N4Wbc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نمایندۀ ایران در آژانس: این قطعنامه مبنای قانونی ندارد و نتیجه‌ای درپی نخواهد داشت  @Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/461138" target="_blank">📅 21:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461137">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceeb4b5605.mp4?token=FYOISLkwfuzvPd7OH6cLIvdy3E7go6ECol0I35CONBHxAwlVHMCse-iRSR_eGsEkVd5_kVbBCqL1pkRMREOp_lT0UH0jApn6WADAJsKU-LrXqIAMEQDFtVcTYR9m3Ocvx9sLil2a8Z-UC57GGJ5CyD1cTi3vCi9Dw-HZ4fpzu3ZunMTBEvU7rNAPca-5_pP8rU9LoPJcetKjyvWHRRxxObMjCcRgEK4Ky-fM6vuJAGbwQ2mt6UlplazGlzjbMma7T8jPBpAI1NSRwox_2zYITGVLRqJMI21b_eRzEb9qoivXziLIBozFeZrzqS4yIZu05c6wz7UXPJnBG2hXx-4l_08a2DYCIai_vpfODkx0daOtbTGOZ7c30ewHUa8DWupJoZggIyTXaVL-ZT1-3JbfcNFOGWOEPXlHQAtllE8bbcmnf-G7OC9rxGbFAc3HPJwhS6MHMvgBuFBxjIVtze0WX4TVbMmiVKkiWvYXoFvjUffM7kXZ3D5MqmxBnxGa-BY7TIZDY859VrCaFIr4V0O3W_CCK-4lAwwXpzNqmRVqot0pLrA0Hq_Et6agCnCR8BH2D0YtppDLHVf1jXYSzcYX4aXXaW7RCrzvEvql7_UCQp0Vxgl3XT42UFgXEdng8hK2NjuOi2CkgkL-otojfOtkU712VoHZ3lYpyYjgVUResIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceeb4b5605.mp4?token=FYOISLkwfuzvPd7OH6cLIvdy3E7go6ECol0I35CONBHxAwlVHMCse-iRSR_eGsEkVd5_kVbBCqL1pkRMREOp_lT0UH0jApn6WADAJsKU-LrXqIAMEQDFtVcTYR9m3Ocvx9sLil2a8Z-UC57GGJ5CyD1cTi3vCi9Dw-HZ4fpzu3ZunMTBEvU7rNAPca-5_pP8rU9LoPJcetKjyvWHRRxxObMjCcRgEK4Ky-fM6vuJAGbwQ2mt6UlplazGlzjbMma7T8jPBpAI1NSRwox_2zYITGVLRqJMI21b_eRzEb9qoivXziLIBozFeZrzqS4yIZu05c6wz7UXPJnBG2hXx-4l_08a2DYCIai_vpfODkx0daOtbTGOZ7c30ewHUa8DWupJoZggIyTXaVL-ZT1-3JbfcNFOGWOEPXlHQAtllE8bbcmnf-G7OC9rxGbFAc3HPJwhS6MHMvgBuFBxjIVtze0WX4TVbMmiVKkiWvYXoFvjUffM7kXZ3D5MqmxBnxGa-BY7TIZDY859VrCaFIr4V0O3W_CCK-4lAwwXpzNqmRVqot0pLrA0Hq_Et6agCnCR8BH2D0YtppDLHVf1jXYSzcYX4aXXaW7RCrzvEvql7_UCQp0Vxgl3XT42UFgXEdng8hK2NjuOi2CkgkL-otojfOtkU712VoHZ3lYpyYjgVUResIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرسایشی‌شدن جنگ به نفع ایران است یا آمریکا؟
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/461137" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461135">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به چندین شهرک در جنوب لبنان
🔹
رسانه‌های لبنانی از حملات جنگنده‌های رژیم صهیونیستی به شهرک‌های صربین، حداثا، حاریص، النبطیه الفوقا‌ و الخیام خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/461135" target="_blank">📅 20:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461134">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec7416fcb.mp4?token=NSSy_csfL62TgqBtTpzhFEqTm3EoFVXHvxe4nkj-G8oXts0Obtu3yzF5aMO17sGb4-NP1QkY_o9izj8e8TlQuWfu_XtAdw1TRp76GMaVa5M_eDA_Qpp0FdXB4oo18Wtv2AYrfRIAbZjpw9WCdKifuRA1ls3BEiNHJHSnmhw52iGDx5XhY2MiMXkKBVKp-J23TSdp12pvFDNyveL7Va58rreqo0GcWgdVLNkoB9lpRrpLtp3He-enmqTMURAb1N0fQ3_BoRmEzgH9WjsDV1OXJPFOQTk96kyj8j_7gLHomhKqz3dn5MQUp5hnxfc0i77rt7Pk6unw4HURc4d7zFr7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec7416fcb.mp4?token=NSSy_csfL62TgqBtTpzhFEqTm3EoFVXHvxe4nkj-G8oXts0Obtu3yzF5aMO17sGb4-NP1QkY_o9izj8e8TlQuWfu_XtAdw1TRp76GMaVa5M_eDA_Qpp0FdXB4oo18Wtv2AYrfRIAbZjpw9WCdKifuRA1ls3BEiNHJHSnmhw52iGDx5XhY2MiMXkKBVKp-J23TSdp12pvFDNyveL7Va58rreqo0GcWgdVLNkoB9lpRrpLtp3He-enmqTMURAb1N0fQ3_BoRmEzgH9WjsDV1OXJPFOQTk96kyj8j_7gLHomhKqz3dn5MQUp5hnxfc0i77rt7Pk6unw4HURc4d7zFr7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
واکنش معاون وزیر خارجه به تصویب قطعنامۀ ضدایرانی: در شورای امنیت هم نمی‌توانید کاری از پیش ببرید
🔹
غریب‌آبادی: به تأسیسات هسته‌ای تحت پادمان ایران حمله می‌کنند، روند عادی راستی‌آزمایی را مختل می‌کنند و بعد همان اختلال را دستاویز صدور قطعنامه در شورای حکام…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/461134" target="_blank">📅 20:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnOO4FSgbZrCFPS7hwA1RHRoiA8lSU2IK2fdyYk60kUL-nehyLHR4QjUEVEQ7ghngsCbdTmtkzPoBgnjOO1v7a7v7o_o0f8sVpLexQde9JFib_A0Fy9Oiz_7-r4la1qoimgFcnzapjbsAgqaiJb2JnNJKYny3QT3VF0NZectWUWoOR84aP9z1xqKdbTMN7_KuftMSkfhmEOSQxpvB5hU8J0Upb7r05SWjraAMdb4tdD7_x9RdiUmT1HJuYMGLZ_kMjfaFJKQ0yzy-CmpPNckZM5RALWWJvsjppQAwk_Y9sw5t6krOY-9XF3udIQebAJwSaQ_U52Tjt6ub9LQ8RXT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: به گسترۀ ایران، از اعماق زمین تا اوج آسمان، به زودی خواهید دید
...
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/461132" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461131">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96386b7e8.mp4?token=omX-6IWb8CNaI6nFDm3dSKygMLDtwSJKPQw1z0g7Eu5zo3GPmoqxvciTo6XiNeAmRfXeEWHjw5jglgbmIiylP9dopj71sBNLMydPteqyoOlSWOjnfCPQoI344xtpEAIpJniLKIiYcUyaK7ifB8a4rh_SW_PVf6fG9586W0d9YcHAbfuk9kOaa3pri9shA5Z-G5n2kjrkHl9Cm4fvsSxyR3JmG4cid2iFnLy8tPT6-oAk_d0GdPXD5NeCNkm9V1-WegDdw6CdIusvnWX2GIrdsP7cnzcI1-9LCDaPVkA0GyEVGu1TUq3T4uGkx03-mMd23yMCyODDqEdJVTq0ggV0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96386b7e8.mp4?token=omX-6IWb8CNaI6nFDm3dSKygMLDtwSJKPQw1z0g7Eu5zo3GPmoqxvciTo6XiNeAmRfXeEWHjw5jglgbmIiylP9dopj71sBNLMydPteqyoOlSWOjnfCPQoI344xtpEAIpJniLKIiYcUyaK7ifB8a4rh_SW_PVf6fG9586W0d9YcHAbfuk9kOaa3pri9shA5Z-G5n2kjrkHl9Cm4fvsSxyR3JmG4cid2iFnLy8tPT6-oAk_d0GdPXD5NeCNkm9V1-WegDdw6CdIusvnWX2GIrdsP7cnzcI1-9LCDaPVkA0GyEVGu1TUq3T4uGkx03-mMd23yMCyODDqEdJVTq0ggV0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی روحانی بر «تسلیم» لباس رونق می‌پوشاند
🔹
حسن روحانی، رئیس‌جمهور سابق، به‌تازگی در اظهاراتی گفته: تنگه هرمز نباید تنگه جنگ باشد؛ ما که نمی‌خواهیم همه‌اش بجنگیم؛ تنگه هرمز باید تنگه پررونق باشد؛ اگر رونق نداشته باشد آن را می‌خواهیم چه کنیم؟
🔹
این اظهارات…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/461131" target="_blank">📅 20:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461130">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW-VWbRUXUbn244fpCQnSsgYKA4KUFlPKn_ISQeXAURxGUNKv80xG-BDCM5-xrgEHxhFylq4uLmlYHET3GCpFAkXzGdOgaU8l6xLl1p0JfipJqvBci8g0kIV0SV0_Y6kcgzJEe_cEUjzW6MY8JmKC1Eo9oPutNi62JvGDBEs06kN4rqvYBhqgGfoS_Pn7ZRwod0gfXQIdEd4dp37gof3hWwPxKpeEhdZvNmGgJmZxY21MDXWFZKsRe5rhiS-maNy9suRY88Uh3RILQD2AtmoXQl8PeUXanoBZPTEf5LsVNPHyPnKOjmaOql2M8PYpbCiIeHg5OLV5PSwDGvNw8FTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آژانس پروندۀ هسته‌ای ایران را به شورای امنیت ارجاع داد
🔹
رویترز به‌نقل از دیپلمات‌ها خبر داد که شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
🔹
این قطعنامه…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/461130" target="_blank">📅 20:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461129">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guQ-9BlOmah84VwwcToRVAhz-BcC8r7fKV5VEeiYl4nJznY5ILC0tcFjxJ52EjBakwxEnZvHH-xuqWkahNXNAgsR5duXmmi5EyS5t0uy9_fWgVmm4415XqkzOzsufGbba84vwqAcQnLLo-vpDya_cYuRnSPBFeLSfIPEd_V_qZuRPeP2I8-yWz8om-rX5kK8sptFJreoOEYlV_c7mNta0p9nhwp7etTno3ffhSQQZe9QCaVyUaAxdn6aPMQ5cZmAF_IuE1spFxeuJqcrIxepH3PXnUJUOJVAbGPACd6yFhKi2iEaPLh5IjV8gM8KgSbz5CvGi4Lg8qVZQ-evlki83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون پس از ۲۰۰ روز یاد شهید مدرسه میناب افتاد
🔹
«ماکان جان تو باید امروز پشت نیمکت مدرسه‌ات می‌نشستی، مشق می‌نوشتی، بازی می‌کردی، می‌خندیدی و برای فردایت رؤیا می‌ساختی». سردار آزمون، مهاجم شباب الاهلی امارات، چهارشنبه عصر، ۱۹۴ روز پس از ۹ اسفند و آغاز جنگ، در استوری اینستاگرامی از ماکان نصیری، دانش‌آموز شهید مدرسه میناب نوشت.
🔹
آزمون در بحبوحه جنگ آمریکا و اسرائیل علیه ایران در استوری‌های اینستاگرامی از شیوخ دبی تمجید کرد. امارات در این جنگ ضد منافع ایران عملیاتی انجام داد و از مقرهای اصلی اطلاعاتی اسرائیل بود.
🔹
معاون رئیس‌جمهور در امور توسعه روستایی و مناطق محروم دوشنبه درباره بازگشت آزمون به تیم ملی گفته بود: «آقای پزشکیان خودش شخصاً موضوع را پیگیری کرده و می‌توانم بگویم که ۹۰ درصد مسائل او حل شده.»
🔹
حالا آزمون در استوری‌اش با بیش از ۶ ماه تأخیر بدون اشاره به عاملین این حمله نوشته: «کاش هیچ کودکی در هیچ جای دنیا، معنای جنگ را با جانش یاد نگیرد».
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/461129" target="_blank">📅 20:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf0NOzJrU5NasH3FgHtx_lPpXgL_r0Vartx2NKZ6qrUqycGvPZrO4ldzPfDMIbAuGCTVtHbH9aGdTrhSOtrQ2We8OvFBJWamJDfYLA1MrudsATDbzj1OI5pMS0QB6WuHCnd-vHhdZzWKRWqpsNaOVxbTS_hZEEFKAt9aoABOT8hLGsoIfF2Tmt6zgaFiHUmmeCzJKxi0zblkMuZFmdGFdKw8DVi2vm2steqpmvjiHtNmnDzkuMVJSVPeMllZP3O9q5S6cyymdFjBP-BFNXUw_M-FOKJUSZorhii88bLPr2jDktveCvF3kz1PHcLAgFdQutF8naDSBg91LJQtws8GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله جنتی: هر تجاوزی با پاسخ محکم‌تر روبه‌رو می‌شود
🔹
اقدام سپاه در به غنیمت‌ گرفتن یک زیردریایی پیشرفتۀ آمریکایی جلوۀ دیگری از قدرت ایران است؛ ایران قرار نیست در برابر زورگویی و تهدید سر خم کند.
🔹
همان روحیه جهاد، تحرک، سرعت‌عمل و فرماندهی که در میدان نظامی وجود دارد، باید در عرصۀ نبرد اقتصادی نیز دیده شود.
🔹
دشمن اگر نتواند ملت ایران را با جنگ شکست دهد، ممکن است از راه فشار اقتصادی و سخت‌کردن زندگی مردم وارد شود؛ بنابراین مقابله با این جنگ فقط با سخنرانی و توصیه نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/461128" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌ ایران، روسیه و چین: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد
🔹
ایران، روسیه و چین در بیانیه‌ای مشترک در نشست شورای حکام آژانس، پیش‌نویس قطعنامه آمریکا، انگلیس، فرانسه و آلمان برای ارجاع موضوع هسته‌ای ایران به شورای امنیت را فاقد مبنای…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/461127" target="_blank">📅 20:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6djHlbeMY9JF05L1VkMrWh6iylKaUdCU0BJdPHmnKRYGpvbBjv5qK-QQxE08a3kmSiA0bkDO_P_9iRMDA1XZ5T4qEyLX6KJ80tSoJ-sKykQZ9Q_vn3Q8Q72QE3yBd4cOZn-288GwQTsLWNBqyN75i82_AcWvR8TXRdytnDzjwEg0SLkrpf8XV36Rw0fSyzhoFlnPiCVInJmQBJ2Bhcxnmyl3zAT8LMbNCT0saxgP42PSj_fWSGZzSsRl8g3ZEJ0uMg_U-4y-10hqyPhglyuN_S8N8ZO9PBTHX_V_R_Pz3CDOz-wRMd5_L3DSOL9EtWfiASHX2iGNW4D0Gf09GFi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۹ هزار نفر از بانک مرکزی اوراق سکه خریدند
🔹
در نخستین عرضه «اوراق سلف سکه» توسط بانک مرکزی، ۴۱ میلیون و ۴۰۰ هزار ورقه در بورس فروخته شد.
🔹
هر ۱۰۰۰ ورقه معادل یک قطعه سکه است؛ یعنی مجموعا معادل ۴۱ هزار و ۴۰۰ قطعه سکه از کل ۱۰۰ هزار سکه‌ای که بانک مرکزی در این طرح قرار داده بود پیش‌فروش شده است.
🔹
سررسید این اوراق ۳‌ماهه است و پس‌از آن دارندگان امکان دریافت سکه فیزیکی یا فروش با بازدۀ تعیین‌شده را دارند.
🔹
قیمت هر قطعه سکه در این طرح حدودا ۲۳۵ میلیون و ۷۰۰ هزار تومان است و ۷ درصد سود هم برای خریداران تضمین شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/461126" target="_blank">📅 20:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شنیده‌شدن صدای انفجار از سمت دریا در جنوب جاسک
🔹
حوالی ساعت ۱۹:۲۰ امشب صدای انفجاری از سمت دریا در مناطق جنوبی شهرستان جاسک شنیده شد.
🔹
براساس گزارش‌های محلی، شماری از مردم ساکن در مناطق ساحلی جاسک این صدا را شنیده‌اند.
🔹
تاکنون جزئیاتی درباره منشأ، محل دقیق و علت این انفجار در دست نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461125" target="_blank">📅 19:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnYm8B2-PxhWB0-jjDPugoggznu98sKfpr0UX_jVE9rdL3_wvCHlsDTFE4oUjPBRmDVnwSp1dYBoKDrOwBv-ywv4-fhgjAka13zkhEe6s99f3i09kb2avRH8-Dg9pOgluwRI9rLngOeBysXJLACWyJNYAqq6qCpXxOgB3rfrvObrRxsZEBAdl2RDdQGIjFHdCQTWucN6PWBjd61zHGt__-T017J7UKW6HS-27b_NdqUf6EqYJHifO4N8xi8Mt3Bt5OLrxZkAtojfHdi0fAHl8SUKDK7WrJi5bR4mNfLwXopwOwN5czIwsRuukj3l_2OWv8sppTjnRJnbSt7CxhE4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۷۷۰۰ بار توافق با دولت لبنان را نقض کرده است
🔹
ارتش لبنان: نظامیان صهیونیست از زمان امضای توافق آتش‌بس با دولت لبنان حدودا ۷۷۰۰ بار آن را نقض کرده‌اند.
🔹
هدف نهایی اسرائیل، ضربه زدن به اعتبار ارتش در داخل لبنان و در برابر جامعۀ بین‌المللی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/461124" target="_blank">📅 19:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKuijd4tyVdW4HAYxtCnU2Ea_BA40zilhPnq26p6S0yFu210cw9eaUrlZeWIOQxiWL4D1iYtn6kcgYpG0lRL4EwFBI8RzhV_2rJ_6srSgmrtuB_hLk7WJKg3sOFfgE69Ds-Q0vESIAxU-Vw6kSC0VBnDq723U5MdIjYqWwZ6oRm-S1zKa-qPayI_d_AeHCPTSLgmZtNpSnTN4XSpBxwxw-hvja3on2t9bOw0sQ9hl6fpb1iE0XVxwluMbPT5qjVX3oy7eJ_-3VLBCA1U8t1s_Ti55uNhH_qOj2eN5CmyAuTeGLfnquFrCR1CWA63q6fiaa-GGZPzfUq861cQdzseZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
راهی جز جهاد و مقاومت پیشِ ‌رو نمانده است
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/461123" target="_blank">📅 19:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
فرمانده‌ای که این روزها نامش با تنگۀ هرمز گره خورده است
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/461122" target="_blank">📅 19:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: رفتار آژانس و گروسی یادآور داستان حکیم عضدالدین ایجی و خان مغول است
🔹
هرجا که در حوزه‌های دیگر کم می‌آورند، سراغ آژانس و شخص مدیرکل می‌روند و بالعکس، مدیرکل خودش را عرضه می‌کند برای سوءاستفادهٔ طرف‌های اروپایی و آمریکا علیه ایران برای…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461121" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461120">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe01945e1.mp4?token=SjoizEciBBqYfKgHF72W_6vcGddFok4dFKUCgheJ690c5pv63dSBJGUPwyhzukm8vSZEg6FKK3NgeK2FpPtZVpBKU-EIg3sLnIGbBrmZdhmawV8zlkpjQ_DayLJK5m9xEV_eNlIl_6fA3fHPvvmYfbjc_wEyeIhh_ITftjuzr38gx7qwchMgtcHc7eJqKLMtoQuknTRV21mcBFscn1orl00FTGLV_7fsXSu3C3geKVH6Ba-VjM-BCt70rSwV47LmGFoPa-eiuVKQRHj0GEzSa_Fl00P38-DBvYZqUoosrOKXZ9NGdIxaplpBilDU_Wxty93QRtWgjMxxjqOReneSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe01945e1.mp4?token=SjoizEciBBqYfKgHF72W_6vcGddFok4dFKUCgheJ690c5pv63dSBJGUPwyhzukm8vSZEg6FKK3NgeK2FpPtZVpBKU-EIg3sLnIGbBrmZdhmawV8zlkpjQ_DayLJK5m9xEV_eNlIl_6fA3fHPvvmYfbjc_wEyeIhh_ITftjuzr38gx7qwchMgtcHc7eJqKLMtoQuknTRV21mcBFscn1orl00FTGLV_7fsXSu3C3geKVH6Ba-VjM-BCt70rSwV47LmGFoPa-eiuVKQRHj0GEzSa_Fl00P38-DBvYZqUoosrOKXZ9NGdIxaplpBilDU_Wxty93QRtWgjMxxjqOReneSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب منازل مردم جنوب لبنان به دست صهیونیست‌ها
🔹
ارتش رژیم صهیونیستی در شهرک بنی‌‌حیان در جنوب لبنان چندین ساختمان مسکونی را منفجر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461120" target="_blank">📅 18:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461119">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smhmeuspk_YA7KngJWzdNpwJfZnf1hXdr62ib2GaH_YUMDDEV-3K-yvbiQKaOKxxSUI1sta3RDZ-QVPzuTU-5vx1yR0qx4eYMNPVJ4V4ee9RvpvBCaQvcvo4zhOxsC5qdewTO0bk_7zKPzJ5SiSpM1J5MD0qW31FdelkM7K9K3GQsTF-NL_BQJcgAIQs5cZF21JO_uF_Kow_xDldqZYz0ISNT2DZQsrfxhZyVED9VhRykaVdd4D8JjQr-Xxz7Vapf-cuTmzFA2HMSqyNMXHYpaN4jnpBTqSjrpAvmotg5VXJ9ps0SHth4G0RtZzyUSgSBhs39pGukQDsSrPfAD5gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: شکار زهپاد آمریکا می‌تواند فرصت جهش در سامانه‌های خودمختار باشد
🔹
اوایل دهه نود، ایران«RQ-170»را تصاحب کرد و کمتر از یک دهه بعد، به قدرتی اصلی در عرصه پهپادی جهان تبدیل شد. حالا یک زهپاد آمریکایی می‌تواند به فرصتی برای جهشی تازه در سامانه‌های خود مختار تبدیل شود.
🔹
ترامپ کاش پیش از اخراج ژنرال‌های باتجربه پنتاگون از آنان می‌پرسید طرف حسابش کیست.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461119" target="_blank">📅 18:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461118">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b0723c32.mp4?token=NJjT9Lmap44C35KsvVWCt-tTJLG_jPf7OtYrHVzANHd7Mjc_hQPImgZvanqOlsahKMRD451_Qfdx2fOyZbHM78fAUI1UmCQqZ1eOBtMNWhFye_IOrl-yutL3CsHXUPZKLgXrM7nVaBWv_FrwUggQ0pshrMWVKD2Rw-9fvhDGb9hh1jDVcSBCjuWVxl0iT6Z0i0HYgAmezK01Le4ggsPpvKqWTQqKo3xdFOjfviaY1D8bCizeMU7XwS6_BFukIjb29GuKMGeWgUbBgREM9sRvfLh_T5tmJqq2DK5Pg6OiG4_LqxmWHDI4JMZA1JnKfu4xtEUb3lx3vy4p0mTTtxI7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b0723c32.mp4?token=NJjT9Lmap44C35KsvVWCt-tTJLG_jPf7OtYrHVzANHd7Mjc_hQPImgZvanqOlsahKMRD451_Qfdx2fOyZbHM78fAUI1UmCQqZ1eOBtMNWhFye_IOrl-yutL3CsHXUPZKLgXrM7nVaBWv_FrwUggQ0pshrMWVKD2Rw-9fvhDGb9hh1jDVcSBCjuWVxl0iT6Z0i0HYgAmezK01Le4ggsPpvKqWTQqKo3xdFOjfviaY1D8bCizeMU7XwS6_BFukIjb29GuKMGeWgUbBgREM9sRvfLh_T5tmJqq2DK5Pg6OiG4_LqxmWHDI4JMZA1JnKfu4xtEUb3lx3vy4p0mTTtxI7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه‌هایی در اردن و اربیل که آمریکایی‌ها فکر می‌کردند از آن خبر نداریم</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461118" target="_blank">📅 18:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461117">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJQhShroPnYKobS2nrBe5xM64Sb6CwD8_EWraLvXhhd7GymTz7f0mrfWqClk1LrGUbDCylVvIUxPgdC0YqIXrwRAkm5gciG01dYQO5i-WaBHPBvN-gz8mvZ0584kx8ikerAafg0h1rzbr5TxBwpRIPU8iJ7hkjeCaQtv57GC4mBK-fLnawXvU8O_rZY8lapXfqzZNawvxqzy5gnn5SZre9CrPCWvLIQcrbzO2yvjcC80dx99yQ1LZLXYQs4340TgzxCksVMpNCcN-a6ANQ1-y_Nh2zqgVYJjMOI68N3qhYnIBYq1jPJN4gy9sv3SAw5OpVrhyMmzoIl1JLJ39HCLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانه‌ای که ۱۲۰ روز خالی بماند، مشمول مالیات سنگین می‌شود
🔹
براساس قانون، هر خانه‌ای که بیش از ۱۲۰ روز خالی بماند، مشمول مالیات بر خانه‌های خالی می‌شود؛ «سال اول ۶ برابر، سال دوم ۱۲ برابر و سال سوم به بعد ۱۸ برابر».
🔹
طی ماه‌های گذشته، با اتصال سامانۀ بانک…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/461117" target="_blank">📅 18:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461116">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c8a3f97f.mp4?token=qModi0i53JtyOqv-Hpj52dRgmjadS_0ePwnDeHU7V-pQ3tIWQfISVpJpzQRefZVdstWQjk4K83nRgsnGAq0u6wt-_1rhN_5M9KZ4sUvjPfNO2dkiuwUU8UIO2RwEELEoEo1BQfPQn8Pl8yqQtQkDYedI3UDcB3CE1tmEvrolCQRSV_Eal5y-RoLNPE-LZ1bRkh9f7kYyV1NYXXNytNbrEt975e_Bv1dRobqJfbZjQ5fh5vMOAvOesF-ZTpOGTH3NpX7pW6WZgveJgxwu2a3G3oMhZM3BGOcM3_9W3z33aiEPFQD1aFr3ySynF12YIy8mtCh3yRVjlsIFK5NaioiSww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c8a3f97f.mp4?token=qModi0i53JtyOqv-Hpj52dRgmjadS_0ePwnDeHU7V-pQ3tIWQfISVpJpzQRefZVdstWQjk4K83nRgsnGAq0u6wt-_1rhN_5M9KZ4sUvjPfNO2dkiuwUU8UIO2RwEELEoEo1BQfPQn8Pl8yqQtQkDYedI3UDcB3CE1tmEvrolCQRSV_Eal5y-RoLNPE-LZ1bRkh9f7kYyV1NYXXNytNbrEt975e_Bv1dRobqJfbZjQ5fh5vMOAvOesF-ZTpOGTH3NpX7pW6WZgveJgxwu2a3G3oMhZM3BGOcM3_9W3z33aiEPFQD1aFr3ySynF12YIy8mtCh3yRVjlsIFK5NaioiSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر فقط می‌توانستید یک نفر را ساکت کنید او که بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/461116" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461115">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkNEwztw3xMl2bMJyTtppIVZYvNRaTbSt9RUPFAtalB06qahn77a0dgqS8Bsn_BOS_2ZysM74W0hfMNKiA_KjCclBDIvF8r9_XXsBJBpZnL-Tsl28kW3zXyLQOMVX5CjAmgZTLO1COiYseK9zv2Rjc6egnGTKmTUbfKtLS0ZDpvsgocIHXjm-j78fj06KKpE8sOho7z9_-XOlDYQy2cugs1OCGwhsKNN_0xTzylUjUS88-U7alR38-Crz19ejE4trRXTWmCgDwsHJkAEhGm21SC1VQrOfqFFNOJz-Gp7VT-IXxz5Rr9McJznPIeYjavBoGP6BLGMtEEI9xJou33tlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمه گوشی، قسطی روی قبض همراه اول
🔹
همراه اول با راه‌اندازی سرویس «همراه بیمه»، امکان خرید اقساطی بیمه موبایل را بدون نیاز به چک و ضامن فراهم کرده است. مشترکان می‌توانند بیمه‌نامه گوشی خود را با سقف پوشش دلخواه تهیه و هزینه آن را در ۱۲ قسط بدون سود، از طریق قبض تلفن همراه پرداخت کنند.
🔹
فعال‌سازی این سرویس با ارسال عدد
۰
به سرشماره
۸۱۱۸
انجام می‌شود و مبلغ اقساط در صورتحساب با عنوان «خدمات دیجیتال» درج خواهد شد.
🔹
نکته مهم اینکه بدهی مربوط به این سرویس، باعث قطع میان‌دوره یا پایان‌دوره سیم‌کارت نمی‌شود.
http://mci.ir/-06YRG5
@mcinews</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/461115" target="_blank">📅 18:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461114">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | Moallem.ins</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n34NIeNRBfZSEAM99_Z5l8QUzz1QTaIK_bbTmrolFUAIzDEhloksqb45iRGEuxfE6kbcyAXvA0-ho1nXAXtZB6EdPcYeY0g_JVn8OBIcNiuxHnsk1jT3phOmXKnqtrDcFDv-glv9XLkCFpoo5K_nQd4F3JRipK0sFIcG8J2-UqGIwKVqJMcviZJJhyi0HUPbXSP2miS8QldkJza0Fwbc5SRJHoReYw2gCPshLHlXkWkjsLemLmaDVKFE6n9aKl9Jn4WlKGTbaMiA9oqNACC9AY8WOR3_hyN9754nbVSh39rn47WSLldW0n1uDiqo7I9CRTexdBjgepDZuONtgiuaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میدانی بیمه معلم در مناطق سیل‌زده
مازندران آغاز فوری ارزیابی خسارت و تسریع در پرداخت به سیل‌زده‌گان
🔹
در پی وقوع بارش‌های شدید و  طوفان‌های پیاپی و جاری‌شدن سیلاب در بخش‌هایی از استان مازندران، بیمه معلم ضمن ابراز همدردی عمیق با هم‌وطنان و آسیب‌دیدگان این حادثه، بلافاصله تیم‌های تخصصی ارزیابی خسارت خود را برای رسیدگی فوری به وضعیت بیمه‌گزاران به کانون‌های آسیب‌دیده اعزام کرد.
🔹
به گزارش روابط‌عمومی بیمه معلم، به‌دنبال ورود سامانه بارشی ناپایدار و وقوع طوفان‌ها و سیلاب‌های اخیر که منجر به آب‌گرفتگی معابر و خسارت به برخی از منازل مسکونی، واحدهای تجاری، مراکز آموزشی و زیرساخت‌های منطقه شد، بیمه معلم به‌عنوان بیمه‌گر پیشرو و حامی جامعه فرهنگیان و عموم شهروندان، با تشکیل فوری ستاد مدیریت بحران، اقدامات ویژه‌ای را جهت حمایت همه‌جانبه از آسیب‌دیدگان آغاز کرده است.
🔹
بر اساس این گزارش، با ابلاغ دستور ویژه مدیرعامل بیمه معلم به سرپرست استان مازندران، کلیه کارشناسان و تیم‌های ارزیاب خسارت بیمه معلم به حالت آماده‌باش کامل درآمده‌اند و عملیات پایش میدانی، بازدید از اماکن خسارت‌دیده و تشکیل پرونده‌های خسارت از نخستین ساعات پس از فروکش نسبی آب با جدیت در حال انجام است.
🔹
علیرضا بزرگمهر، مدیر مجتمع ساری بیمه معلم، با تشریح آخرین وضعیت اقدامات میدانی اظهار داشت: اولویت اساسی ما در این شرایط بحرانی، ایجاد امنیت‌خاطر و ایجاد آرامش در بیمه‌گزاران است تا ارزیابی و پرداخت خسارات در کوتاه‌ترین زمان ممکن صورت پذیرد و مبالغ غرامت به حساب حادثه‌دیدگان، مدارس و مراکز تحت پوشش واریز شود.
🔹
او افزود: بیمه معلم از تمامی دارندگان بیمه‌نامه‌های این شرکت که در اثر سیل و طوفان دچار خسارت شده‌اند خواهشمند است برای تسریع در اعزام کارشناس و تشکیل پرونده با مراجعه حضوری یا ارتباط تلفنی با شعبه سرپرستی و شبکه نمایندگی‌های بیمه معلم در سراسر استان مازندران اقدام کنند.
🔹
بیمه معلم در راستای تعهدات حرفه‌ای و ایفای رسالت مسئولیت اجتماعی خود، تا برآورد نهایی، تسویه کامل خسارات و بازگشت شرایط به حالت عادی، تمام‌قد در کنار مردم شریف مازندران و جامعه معزز فرهنگیان کشور خواهد بود.
#بیمه_معلم
#ارزیابی_خسارت
#سیل_مازندران
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/461114" target="_blank">📅 18:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461113">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/461113" target="_blank">📅 18:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461112">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f75710fa.mp4?token=Jy8VJMKr_-RqWW2MRZxVAcsD6qjW-I2lb5hmbpPYJ07iM31EKSXEtKo25aWquZGck1WcZI-D16T0wQz2WEov1DyTyprdD8WUuJun-lRaD3L7VmeoHFj0P218hVWGXf1_vO1y4nPLuKAkhr8kNrs59jH5_FPfdeW025_IdskcEsbBQMQloJWX4GheYsWZiQfsiSQYXQQ4QUzfoa9odbwMB_lBJHzYPMgU2YYWRUQ7-ZLcw_t89BvBg3BCtVDU9F-aVlLr0dxP1bmCtVSI8SASJ0e6IqNQ3tIZzDo_rNIwNPfkyILZEBMKtQzayjM7dx1AnWWRlg0-W74XYBBmLxNhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f75710fa.mp4?token=Jy8VJMKr_-RqWW2MRZxVAcsD6qjW-I2lb5hmbpPYJ07iM31EKSXEtKo25aWquZGck1WcZI-D16T0wQz2WEov1DyTyprdD8WUuJun-lRaD3L7VmeoHFj0P218hVWGXf1_vO1y4nPLuKAkhr8kNrs59jH5_FPfdeW025_IdskcEsbBQMQloJWX4GheYsWZiQfsiSQYXQQ4QUzfoa9odbwMB_lBJHzYPMgU2YYWRUQ7-ZLcw_t89BvBg3BCtVDU9F-aVlLr0dxP1bmCtVSI8SASJ0e6IqNQ3tIZzDo_rNIwNPfkyILZEBMKtQzayjM7dx1AnWWRlg0-W74XYBBmLxNhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار و قدرت بازدارندگی لازمه جلوگیری از تکرار حملات دشمن است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/461112" target="_blank">📅 18:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461111">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۹.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/461111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۸.pdf</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/461111" target="_blank">📅 18:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در ابها و پایگاه هوایی در خمیس مشیط در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/461110" target="_blank">📅 18:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546c5b3993.mp4?token=nWnDTkKN6dAs07BnYiOx-f_7EjwD2oXy1Nze47aQcHyAw7NOTRbD6AedIapNa6qLFY1d8pRa9p-novCfC5nTX_6whpAPhtXXIrxqEpTY6VgCD5WQMPGcZf1D6ALhDlmBy0pG6TxpShHtUtba3zrXE13xckSCE1ts-WYXeVTatXjzyeIoFOox7MPfUASSrJ_4xj_TgprTccanMXyUenKs9aS80ObDUqxQRCG4j9Glsbt20pY6Av9m_1taNWZzXi54osVXMqD1TcLik-VttkiNWQmkzv3G5ZAYTVwGVJENhliumHcpQVCW6qhbOrArxomwekgsmihevTWim74RWzSEOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546c5b3993.mp4?token=nWnDTkKN6dAs07BnYiOx-f_7EjwD2oXy1Nze47aQcHyAw7NOTRbD6AedIapNa6qLFY1d8pRa9p-novCfC5nTX_6whpAPhtXXIrxqEpTY6VgCD5WQMPGcZf1D6ALhDlmBy0pG6TxpShHtUtba3zrXE13xckSCE1ts-WYXeVTatXjzyeIoFOox7MPfUASSrJ_4xj_TgprTccanMXyUenKs9aS80ObDUqxQRCG4j9Glsbt20pY6Av9m_1taNWZzXi54osVXMqD1TcLik-VttkiNWQmkzv3G5ZAYTVwGVJENhliumHcpQVCW6qhbOrArxomwekgsmihevTWim74RWzSEOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم آمریکا از پیروزی‌های خیالی ترامپ خسته شده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461109" target="_blank">📅 17:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امسال ۱۰ هزار دانشجو راهی عمره می‌شوند
🔹
معاون فرهنگی نهاد رهبری در دانشگاه‌ها: طی دو هفته آینده ثبت‌نام عمره دانشجویی آغاز می‌شود , سهمیه امسال به ۱۰ هزار نفر رسیده است.
🔹
نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها رایزنی‌هایی را برای افزایش تسهیلات وام عمره دانشجویی دنبال می‌کند؛ پیش‌بینی ما حداقل افزایش ۲ برابری وام است.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/461108" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279caefb98.mp4?token=BpdykumtPCn7qzGaUJxtrfjrlAyL9aVjMYVVPE0MiCxDkSdGk1ELPXpH1bEav8G7DaT1D-hW9NPoiK8RoWs2IJbL1PgOi9XNY8NI1Rwr2JA8f7wauOZX4hLrk82y-AvaEom3d969tn1cR_fNLARUwakr0t2xoRt0fZ67dBLEe_WHxAJ1Sg1AuKrVhGC_WH5QC8ax1y0tvKZMDofkr4M5g-6L3kSifluUMD9xH2ccFrre1SLQ2A08XjZI5f1YSFnTea2TtnquAWDdvJIXsQ60fdjIxMFo-NhN4cgmu9ITyaBmwXIpL4DKHHgETvjkug6QByScnNW-sX_SIcDvhi3oMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279caefb98.mp4?token=BpdykumtPCn7qzGaUJxtrfjrlAyL9aVjMYVVPE0MiCxDkSdGk1ELPXpH1bEav8G7DaT1D-hW9NPoiK8RoWs2IJbL1PgOi9XNY8NI1Rwr2JA8f7wauOZX4hLrk82y-AvaEom3d969tn1cR_fNLARUwakr0t2xoRt0fZ67dBLEe_WHxAJ1Sg1AuKrVhGC_WH5QC8ax1y0tvKZMDofkr4M5g-6L3kSifluUMD9xH2ccFrre1SLQ2A08XjZI5f1YSFnTea2TtnquAWDdvJIXsQ60fdjIxMFo-NhN4cgmu9ITyaBmwXIpL4DKHHgETvjkug6QByScnNW-sX_SIcDvhi3oMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکنیک مذاکره‌ای آمریکایی‌ها برای جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461107" target="_blank">📅 17:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461106">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-rHScSgvfV1nUW1wDhSI-zZ3piNi_QwiSn0bq6LC0QNyCl8L9Xz5Aglbucnba91d4ihEXrBq_6CV3SWrIx-S6DtibgcTfU3TnioFyERYShNA3VcAmwDZyptrkvPegQkuot_ivBm7ONKoN3KoEYOlcL_muLMDZR76qDk0x5XoK-HVRkV27qcFbhaIpMiOvHKoUdERdzB2ngHrAuwkMmnXTCC4M2-5OdKmo5UnGOYWvcqN7FJ4pXYI-wnWlh5UiFal0BER4tH_6tDYqlZW0TYelaHOsL8G6X-ZmCntOt2sRUsWovU4Q_P6J7HjEhvoyNIsUjwTPTUMVp7Of8UeNNEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف هزار تُن فرآوردهٔ نفتی احتکارشده در چهارمحال‌وبختیاری
🔹
فرمانده انتظامی چهارمحال‌وبختیاری: ۱۰۰۰ تن فرآوردهٔ نفتی به‌ارزش ۲۵ میلیارد تومان در شهرستان سامان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461106" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
انفجار انبار تسلیحات در شمال غرب سوریه؛ دست‌کم ۱۴ نفر کشته شدند
🔹
در پی انفجار یک انبار سلاح و مهمات در شمال غرب سوریه، دست‌کم ۱۴ نفر کشته و ۱۱ نفر دیگر زخمی شدند.
🔹
روزنامه واشنگتن‌پست به نقل از رسانه‌ دولتی سوریه نوشت که این انفجار امروز در نزدیکی شهر
سرمدا
در استان ادلب رخ داده است. علت وقوع انفجار هنوز مشخص نشده و تحقیقات درباره این حادثه ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/461104" target="_blank">📅 17:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انهدام چهارمین پهپاد سعودی در ۲۴ ساعت گذشته توسط یمنی‌ها
🔹
نیروهای مسلح یمن: یک پهپاد شناسایی تهاجمی CH4 متعلق به دشمن سعودی در استان الجوف سرنگون شد.
🔹
این دومین پهپاد از همین نوع است که در ۱۲ ساعت گذشته و چهارمین پهپاد در ۲۴ ساعت گذشته است که توسط نیروهای…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461103" target="_blank">📅 16:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
روایت صیادان ایرانی از وضعیت تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461102" target="_blank">📅 16:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461101">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b202f4951.mp4?token=JNmT9jxnGxmT9HYb3VSR22WTprGRj-QaBLnJVeJTka6tVSR5YFWQWzXx6TNTdn6USwgF_WFaahW2HDvn3Bd35PMD2lbhKpiOn-ZT1h9Uul4K0x3pMzSYJXQ2JUoOFNfBV7v1tvO5sa2yOa8LlF887nH_8wenhdpVJwB7Jv_tsZmhEWwjlh5yuGcOpLsMhl7U7_ox-tN73ngiG_MVCFkFpFlSLu2PC-XFtuUmwTEnxDBZ9f9bqvt8YiFe1hi_G-CzeuhOkQ84Sm_gTfvU4PUIHSnLFdKGeB_fYRZ3kG_mi-RqkgQGLYdt9bCNXYCZvKP6p9B_Gg-vW-jVFQJ_AEiCVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b202f4951.mp4?token=JNmT9jxnGxmT9HYb3VSR22WTprGRj-QaBLnJVeJTka6tVSR5YFWQWzXx6TNTdn6USwgF_WFaahW2HDvn3Bd35PMD2lbhKpiOn-ZT1h9Uul4K0x3pMzSYJXQ2JUoOFNfBV7v1tvO5sa2yOa8LlF887nH_8wenhdpVJwB7Jv_tsZmhEWwjlh5yuGcOpLsMhl7U7_ox-tN73ngiG_MVCFkFpFlSLu2PC-XFtuUmwTEnxDBZ9f9bqvt8YiFe1hi_G-CzeuhOkQ84Sm_gTfvU4PUIHSnLFdKGeB_fYRZ3kG_mi-RqkgQGLYdt9bCNXYCZvKP6p9B_Gg-vW-jVFQJ_AEiCVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده مجلس: دستگاه‌های نظارتی به بحث ارز تخصیص یافته به مونتاژکارها و خودروسازها ورود کنند
🔹
طی پنج سال ۳۰ میلیارد دلار ارز به مونتاژکاران خودرو داده شده که سهم مدیران‌خودرو ۶ میلیارد دلار، کرمان‌موتور ۲.۸میلارد دلار، بهمن‌موتور ۱.۸ میلیارد دلار و باقی شرکت‌ها زیر یک میلیارد دلار بوده است.
🔹
ارز را دادیم و خودرو را دوبرابر تحویل گرفتیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461101" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461100">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
بازار گران‌فروشان لوازم‌التحریر در آستانهٔ مهر گرم شد   @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461100" target="_blank">📅 16:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0329723d7d.mp4?token=Uw3vZavUv_OQV9obmnSMQ3HzoKc1fjs6_FjZ-3gUF0yMdRW3WBDIlN3z_j2GE7QytkinCPoEMrR8kvCSvwOKQUooI2Tni1QOLn-YcRQNsAeKD_4tQKIM_y5VGT0AlTXi6V6gvJSfRXGS0vMxJy20g4xpIvc2uGMue4shKtRVroHqps4NX9bl3PD8YucO2wg6X_q3JL4NrmBXqGadZWWGvOBpB8IeUCdbjLDEWlZBuEoJQL4UNCAqRUMCqdgbsVGq1-xx9LDDdQkUpzjihDcblgp4thCjRzUocsxIymQNy0ppnKSD-wx7kzg6kqJ_n_4u4gsnnWpk8agooKqfcfymPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0329723d7d.mp4?token=Uw3vZavUv_OQV9obmnSMQ3HzoKc1fjs6_FjZ-3gUF0yMdRW3WBDIlN3z_j2GE7QytkinCPoEMrR8kvCSvwOKQUooI2Tni1QOLn-YcRQNsAeKD_4tQKIM_y5VGT0AlTXi6V6gvJSfRXGS0vMxJy20g4xpIvc2uGMue4shKtRVroHqps4NX9bl3PD8YucO2wg6X_q3JL4NrmBXqGadZWWGvOBpB8IeUCdbjLDEWlZBuEoJQL4UNCAqRUMCqdgbsVGq1-xx9LDDdQkUpzjihDcblgp4thCjRzUocsxIymQNy0ppnKSD-wx7kzg6kqJ_n_4u4gsnnWpk8agooKqfcfymPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۶۸ بار حمله به یک پایگاه؛ چرا العدید مهم بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/461099" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciJe5CIVE9CFJ6qwA5u3SSPO5TQ7-zh_mH9qabQDP8TRB_18Vo4NJdDAjtSIHoiphC7fGUqiEXOkiJy1UdbRYSBuEdWFaI8hlfBHvNl4GIh0i83MC_HEzpZVeHef4BabIJLYf21iluPa2aM9G-u0Ytvw2HolhKbuHVw_FprWYQrfv4EjE1pf0SLOSjw7phu4jHVR4rXa1w50zhcZDjxngbGAvLxe33RnQRYBKSh8YWExPOs_KRh4olePPB9z-EIodfqDd70HHh30pO-G4dwNaJHe2x1DDiiGf6DlL-avPAyzzh5ZuQXykyRyujYtPszId8KnaF3boHVADboa0Wl0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  تلاش آمریکا برای کنترل روایت در ماجرای شکار یک زهپاد توسط سپاه
🔹
یک مقام آمریکایی به رویترز گفته که یک زیردریایی نظامی آمریکا «بیشتر از یک روز قبل» هنگام فعالیت در زیر آب با یک نقص فنی مواجه شد.
🔹
وی که به شرط عدم افشای نام با این رسانه گفت‌وگو کرده،…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461098" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f36b2c83.mp4?token=cUfclegIY09P1gknuXdffJwKur0deciaiBTfKlzBj1bNjGSNqpqXUFDef626zHA3Qmu2tA4F1BosKOM74krjmGWRvzinV6cZ-hzquoW1onE3ukGfAIbT-jjjqiBWxeQJfboJ71EBi0AynRjvqspnkOxtuz-NYSO4dWYzr0knEvUemb6U_OXJgEJabKzw0LW9gQdkrkcbHSzhgdhUoHCnEPup6UWIcdhJqcJMuUXZM1S-J_gC3hOs9usmf5SCKsXAiwAwzHHDaiyiKW6zYFIrrz-76_SR-cLYtBI0E8eCRsbxcMjA-rqZfju-AeJS-Uyq169f-YZS0gNtu1AW8Fhk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f36b2c83.mp4?token=cUfclegIY09P1gknuXdffJwKur0deciaiBTfKlzBj1bNjGSNqpqXUFDef626zHA3Qmu2tA4F1BosKOM74krjmGWRvzinV6cZ-hzquoW1onE3ukGfAIbT-jjjqiBWxeQJfboJ71EBi0AynRjvqspnkOxtuz-NYSO4dWYzr0knEvUemb6U_OXJgEJabKzw0LW9gQdkrkcbHSzhgdhUoHCnEPup6UWIcdhJqcJMuUXZM1S-J_gC3hOs9usmf5SCKsXAiwAwzHHDaiyiKW6zYFIrrz-76_SR-cLYtBI0E8eCRsbxcMjA-rqZfju-AeJS-Uyq169f-YZS0gNtu1AW8Fhk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نفت، صنعتی که بدون وقفه در کشور ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461097" target="_blank">📅 15:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzogmJcmHhdMHLBLvZ6EIzGLJL2OKfUaaAR3oVHR8RuWMJ0p6z-oU-ItlIRpxUfJlhkxlIjVmHZ6bgfpQsZqz2OyfUAtigucGfvgU_ICrekveLyl0elchiOpivxg0c5EUY0ZR4HwNbb6yfocs0RPBysIhf1qy0-DdHpMpE6E8a_wx7n3LntsfjnMMCpgtgkQh38BgE9ARQiMcjv6LUpl80QyoqvJ4s6n6kLruKZpXo_uichn86Dq3Ywz45vL8LjpD1P9bvfS_mQW83Fqmxon57BU94KRkItye5J0fGnHLOleAW3_C61tQiJheTieSXM0Skae61plbCzoMtOMD5Tt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
🔹
جنگ تحمیلی با بزرگ‌ترین قدرت‌های ظاهری جهان در مقاطعی به‌پایان رسیده، اما ماهیت جنگ همچنان ادامه دارد.
🔹
این جنگ برای اولین‌بار، آسیب‌های راهبردی را مستقیماً به خود آمریکا منتقل کرده و معادلات امنیتی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461096" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461095">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtsAPGWlc0unsfxU0pfuJ4_ylV7xCTNw8STFPqXlqOQBWMtWdDL99WzW0ruYAe7CCYj2kmcJShuah3i-FJPvRbeC_JENHxPXqzgI87PYJ4LqDi5d0cFpR7D1vD1koA12ZzX_W3DEQG-Dm7h0ROa5kQDqKi2h-7SFlL3XLtbYfXQpSJNTD6KZ7GKM94Gka7FxIbiPEk_syLaCnLkGXjQj4S6WXP-hgfT06dgSp73KnFNdAon6TVFohuwCc_7FW6p2p9SP3psGTGivWCCjwTvYROYFdR0EcU-OPIwpLt7KFLD_UXezQPLe3W1cNtR8jWXJAE3ipgzFcBiV6QEanHfAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش‌ها از هدف‌قرار‌گرفتن چندین کشتی در خلیج فارس
🔹
سازمان تجارت دریایی انگلیس: چند کشتی تجاری در شمال خلیج فارس و دریای عمان در جریان فعالیت‌های نظامی منطقه هدف شلیک قرار گرفته و از کار افتاده‌اند.
🔹
همچنین یک شناور لنگرانداخته در ۲۴ مایل دریایی شمال غربی…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461095" target="_blank">📅 15:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461094">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7391170a.mp4?token=uWHsxYEvcsj1J1iVxkqxAx-8Dh7SRUK0GaojpP1Vdf2jf4p22VLnCyhQo_Ay2XpRcieyDkJ7te7RWYvUnJNx9t8BS02GGWKbzoahuutdphluO3WabNgD4K2hl7QCFUlCE5VHyRZH3xX5wYvKqwocvASqrXCcygOx6GxYZlOZsGgPX-LhouCudkTSwdhDX64tXC3iii2ctJy21THxbo3aGxck4vQbOYbcu99fkHo1A7aOJViFyyD-4WhK5gYWYEkTd-WHxSc1Lib6uAasERC3vHQ28YP4p9kQrJOl2-sw9GLXqNpCMLrgjs2IrbuhffKG6CnnoVOhCAYVwTiGKkyT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7391170a.mp4?token=uWHsxYEvcsj1J1iVxkqxAx-8Dh7SRUK0GaojpP1Vdf2jf4p22VLnCyhQo_Ay2XpRcieyDkJ7te7RWYvUnJNx9t8BS02GGWKbzoahuutdphluO3WabNgD4K2hl7QCFUlCE5VHyRZH3xX5wYvKqwocvASqrXCcygOx6GxYZlOZsGgPX-LhouCudkTSwdhDX64tXC3iii2ctJy21THxbo3aGxck4vQbOYbcu99fkHo1A7aOJViFyyD-4WhK5gYWYEkTd-WHxSc1Lib6uAasERC3vHQ28YP4p9kQrJOl2-sw9GLXqNpCMLrgjs2IrbuhffKG6CnnoVOhCAYVwTiGKkyT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشرفت ۹۷ درصدی بخشی‌از جادهٔ الموت-قزوین-تنکابن
🔸
این طرح با طول ۱۶۴ کیلومتر، زمان سفر به شمال کشور را نصف می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461094" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461093">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fe26b148.mp4?token=On4e5twa0FLTBQQbPG2rwsZ0xuHjJeB1D1a5GOsD0GUak4X7PutvIB3rZk1Z9dPIlxeXxtE8JDgkHF9I_vX32Wu6QVRycbePZsGVADEOeXV5srgEm-IEeLVoxWZMsXvlhlEkox3YQpbX5SL6XVLkqxLgQsmZMFFoJOeYIahXaUt7i3rvdz-EA5lWjZYLQwSXjXYb2luF-kmLODAky-lg6QeAfJD1wN17y_3lKOfAH7obPB36LLIhsc8pWrQckKknM8efx4oAnClXOMaCOu6zA95IAzZckxDcW9JqB-ouDWamocrziKiiLSKjXspkcHa8x1WWoGqfvK4WPXKUiTtZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fe26b148.mp4?token=On4e5twa0FLTBQQbPG2rwsZ0xuHjJeB1D1a5GOsD0GUak4X7PutvIB3rZk1Z9dPIlxeXxtE8JDgkHF9I_vX32Wu6QVRycbePZsGVADEOeXV5srgEm-IEeLVoxWZMsXvlhlEkox3YQpbX5SL6XVLkqxLgQsmZMFFoJOeYIahXaUt7i3rvdz-EA5lWjZYLQwSXjXYb2luF-kmLODAky-lg6QeAfJD1wN17y_3lKOfAH7obPB36LLIhsc8pWrQckKknM8efx4oAnClXOMaCOu6zA95IAzZckxDcW9JqB-ouDWamocrziKiiLSKjXspkcHa8x1WWoGqfvK4WPXKUiTtZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری طرح میدان گازی پارس شمالی: به‌اندازهٔ ۲ فاز پارس جنوبی از ۱۴ چاه میدان گازی پارس شمالی، گاز تولید می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461093" target="_blank">📅 15:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2b194c0e.mp4?token=jk4ljaSSi_eL1HSWm9t9Lj_jGSCmLNkAxUSViSscGLOebSFXLdyNBeKQA7FZnsbI5XGQ7asf643SHs6R2GLG9_xPXeoebmm1XBKKadOSrp24L4XhdMx_MFXXQAl11duWxsDbs2DgmPY9CT4vHKCSm4H73gRzy5kHJc6PFg6awBxAzK7-gHQrdG-5aPgC5QprFIQMqPX2fq6Tj-HiX9oD-G7KRxX74VAGKOCvQaAHMYX8kTXLt15QCMyS4cVyvr9kHlc9UdFxkfz0DKQO2-E09AFgq6qR_-3TL_awNQ4EfcY-Phher6LsQ0qCcZR6CENSCOwOI2oZEcJ4_8HFlBbIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2b194c0e.mp4?token=jk4ljaSSi_eL1HSWm9t9Lj_jGSCmLNkAxUSViSscGLOebSFXLdyNBeKQA7FZnsbI5XGQ7asf643SHs6R2GLG9_xPXeoebmm1XBKKadOSrp24L4XhdMx_MFXXQAl11duWxsDbs2DgmPY9CT4vHKCSm4H73gRzy5kHJc6PFg6awBxAzK7-gHQrdG-5aPgC5QprFIQMqPX2fq6Tj-HiX9oD-G7KRxX74VAGKOCvQaAHMYX8kTXLt15QCMyS4cVyvr9kHlc9UdFxkfz0DKQO2-E09AFgq6qR_-3TL_awNQ4EfcY-Phher6LsQ0qCcZR6CENSCOwOI2oZEcJ4_8HFlBbIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار گران‌فروشان لوازم‌التحریر در آستانهٔ مهر گرم شد
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461092" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f256a249.mp4?token=bqx3-xAFAhJ8aT3VhP92XZ6wiB4uQB7PrIEl4sQOtkJ9gAZZ-QmRpXPCy99LJfFvOb2X3k-7Z4e0zzvLAvJBy07obEwN75CLYhqjsTa1TahZTrbcTvEX-lHNyDMxgn8Ls0Jx60FwKNY48mIkuJABy_IDBNRkXKEGdKe3seZcAfPt9jdQ-jRlOapkuA6j3G7V4z9Lo50JueXQSU_C9Qe4E7ZAIea8AAMEHTMl52HFAqVL74zJs4h85sBC9PFg-kY241Od0YLipJ2XFL-lVMNprUSRsJpq-ya-knt66ObYtD5xj1jwQMg9yxrq9PtPoUO5U8qBJQz6YidqyPRGdCN3nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f256a249.mp4?token=bqx3-xAFAhJ8aT3VhP92XZ6wiB4uQB7PrIEl4sQOtkJ9gAZZ-QmRpXPCy99LJfFvOb2X3k-7Z4e0zzvLAvJBy07obEwN75CLYhqjsTa1TahZTrbcTvEX-lHNyDMxgn8Ls0Jx60FwKNY48mIkuJABy_IDBNRkXKEGdKe3seZcAfPt9jdQ-jRlOapkuA6j3G7V4z9Lo50JueXQSU_C9Qe4E7ZAIea8AAMEHTMl52HFAqVL74zJs4h85sBC9PFg-kY241Od0YLipJ2XFL-lVMNprUSRsJpq-ya-knt66ObYtD5xj1jwQMg9yxrq9PtPoUO5U8qBJQz6YidqyPRGdCN3nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب گستردهٔ شکار زیردریایی آمریکا توسط ایران در رسانه‌های دنیا
🔹
کارولوسکی، تحلیل‌گر آمریکایی، شکار این زیردریایی پیشرفته را تحقیر آمریکا دانست.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461091" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461090">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E28sS-a_ooC6sKffZtrnGo5TjKMd68jL3msycW2j5zCmYNrJh3i-BRDVGvTpUmv-khFIDNHAIgHBU_Cib8zQp8x6VudK5JIav-Us9p_KwbGJbsu8POIJMp5gLT6zeQJWkO7QlLP4B6gsDzldNe_qTE9o4kQW929HWP45F9RTXwq_oezYcTXXP-WryuzTI2DTivDy5YEEi7pqd8IfUsGvdNKKwjPRyiwPlAB2zfNcBG9AK2tXyoLrMBySUAAJNwZFpWtRwNVWrs87Co1s_oPOMhEOav2PE_oDyzZvc61MsyJZRy5GWDSKBgJLMx561Knu1bM1yF-beoojsYFv_fnx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
🔹
جنگ تحمیلی با بزرگ‌ترین قدرت‌های ظاهری جهان در مقاطعی به‌پایان رسیده، اما ماهیت جنگ همچنان ادامه دارد.
🔹
این جنگ برای اولین‌بار، آسیب‌های راهبردی را مستقیماً به خود آمریکا منتقل کرده و معادلات امنیتی و اقتصادی این کشور را تحت تأثیر قرار داده است.
🔹
اگر دشمن خواهان پایان این وضعیت است، باید ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد، ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند، محاصرهٔ یمن پایان یابد، ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
🔹
به‌جایی رسیده‌ایم که اگر دشمن ۲ یا ۳ هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461090" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5910e1c.mp4?token=ssN87vkZNl0icDGd7Hwm2JlwMe0tE2q1Z-WJ9DT_92E3v0LsRUkeYCwdO24XkWibBYwKgdlVg_Ey_V3rFO1BVA5lnUKHh9mq0d6Fclfq8h4y6qByH2_M8BbFGOHKIfYnU6QKBCqt81lIg8qO_yMnd3j51ubT4cbvIajnvWbeDk0U4h-27O4owdIjXptAurIixeoJ554ioQZL6LnQ2BUyKhObp5VWZen0AM-d2cW2ly1j6mh0dU9_TwA49JeTljt4pHIBNcfJMzEtfPCO0B0GKQouHpZ3_RKhvZzhgOTI-9HH5JrxbBPbimsU6xfr0DONI54HDA3FMxKrMPNYEEpszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5910e1c.mp4?token=ssN87vkZNl0icDGd7Hwm2JlwMe0tE2q1Z-WJ9DT_92E3v0LsRUkeYCwdO24XkWibBYwKgdlVg_Ey_V3rFO1BVA5lnUKHh9mq0d6Fclfq8h4y6qByH2_M8BbFGOHKIfYnU6QKBCqt81lIg8qO_yMnd3j51ubT4cbvIajnvWbeDk0U4h-27O4owdIjXptAurIixeoJ554ioQZL6LnQ2BUyKhObp5VWZen0AM-d2cW2ly1j6mh0dU9_TwA49JeTljt4pHIBNcfJMzEtfPCO0B0GKQouHpZ3_RKhvZzhgOTI-9HH5JrxbBPbimsU6xfr0DONI54HDA3FMxKrMPNYEEpszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461089" target="_blank">📅 14:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461088">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCSNu01Lc-PSafPyAqpecbNP6Aa7ROIfWj2CFMTGH7A1QcOZhtyUGYu5Cxzkmv6-RvD9nh_72LvMEI6iiTtTG06jCKbdj4wwsg55QO0iGA6pFuzpARY98xNimSnwsaGLcy5_PGIVbvdvNpFFYYk2iD4Jat4mRNCdNKADxdrVu6HscgvGKyXkw5V7irfA50dwzBNK3zyqIIQk4oO1dwXeHMBinWm7cCJom6AgbQ-9r-agXio7sFmixwrErdJRNYkJpKZ4_p3A3rNTBMdaKL4iXKtcELWD-WSpBkxi7PKJ8RKn16KHvQL7SnDkE0i0IPgrwgsAjNsCrBdMxWIbWkR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گویندگی؛ هنر نفس‌ها و مکث‌ها
مهدیقلی، گوینده و مجری تلویزیون: «گویندگی فقط صدای خوب نیست؛ صدای کنترل‌شده‌ای است که با معنا و موقعیت هماهنگ شود.»
گوینده کسی است که نفس‌هایش را می‌شناسد، مکث‌ها را اندازه می‌گیرد و می‌داند هر کلمه را با چه انرژی ادا کند.
انتخاب لحن، مثل قاب‌بندی در عکاسی است؛ بعضی کلمات را برجسته می‌کنی و بعضی را آرام می‌گویی تا مفهوم درست به گوش برسد.
📢
دانشکده رسانه خبرگزاری فارس، تو را به دنیای حرفه‌ای گویندگی می‌برد.
آموزش همراه با تجربه‌ی عملی در باشگاه خبرنگاران «توانا».
🔹
بدون کنکور | مدرک معتبر | اساتید باتجربه | معرفی به بازار کار
⚠️
ظرفیت محدود
📲
عدد ۱۴ را به ۵۰۰۰۱۰۱۴ ارسال کن
🌐
یا ثبت‌نام در:
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461088" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461087">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cebd3b25.mp4?token=KTZKC-06NifEq29LT6oS0McBAebiBsotkuaXo_M_82XrMDn0BanTdnU0wQ4eVRydTYgax58V1oxipUvbTX3TQg--KTkO5uv6iaLRYdLCjLP_fLt8jOC64Ayk2ArcdWZomE-c5Hd4oiQ9ci9lhCEFgmUT6j0RCrAPG8gNjK2TrWGvrR2X1_aQZiGcfJa8AO1iUjvL4ocWdqX02wcXRqq8q7Y0PGuPNLtOy9lgZd-YAl9PhSE44UF6c8l8kPMZ7YKTX5ZzPL9JSe8Cpt0iBEQNZ77zdIhzR-dgEe9QcVR0_r05l_Bg_QwORaurRTsGNL9wFVCG13fPBVC92PQHLfbvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cebd3b25.mp4?token=KTZKC-06NifEq29LT6oS0McBAebiBsotkuaXo_M_82XrMDn0BanTdnU0wQ4eVRydTYgax58V1oxipUvbTX3TQg--KTkO5uv6iaLRYdLCjLP_fLt8jOC64Ayk2ArcdWZomE-c5Hd4oiQ9ci9lhCEFgmUT6j0RCrAPG8gNjK2TrWGvrR2X1_aQZiGcfJa8AO1iUjvL4ocWdqX02wcXRqq8q7Y0PGuPNLtOy9lgZd-YAl9PhSE44UF6c8l8kPMZ7YKTX5ZzPL9JSe8Cpt0iBEQNZ77zdIhzR-dgEe9QcVR0_r05l_Bg_QwORaurRTsGNL9wFVCG13fPBVC92PQHLfbvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
🔹
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461087" target="_blank">📅 14:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461085">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lX_cF-ErM-khMGrg__n0x7hPLiFSJGZ5E8xzq59Kn3D7PO-GVOSpmPw16tYTf8EdpmSvtfCPZ3yLXP-v5uf2LEP7T4g75SAxt2AxEO5gQPgNRK5HdLW5RRbyRiXQSqnEi7Q6lUyS1Gtm9BcKgsRla6KY7bk5r9w3rJD-PdZfJjEbzon7N-pLVX4GNvGLVD-vcUiKGDi6GZ7M9tImc3UxGVLFWvXvT4GHp0R7Q-iN5RZlL-2mhzXHkd92fcZ-IolT_N85_lF8I-04tDgUHSWx8iM7JgBppXr19y3HFnOic3Y7wk_-N66y4vPZWR47Szmjj0O4SqXD16oXwjw_T0SeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FaX1_Us3G_7Nuw6-EseG1mFw9_U31Wx-WGkYdDNLX_-RHlgjPE3ij8kT2OjGFreSYDn0saKWAdIuBi6zh0swsxooqirt49zy2M8HEYHWmzawMEK7L8m0-AyBfuomAygOXo5l-Iz3uw4fTqxO7uSI4d6xsdoyrgNWpdGVeeC_RK8jKhR92SR_TUwUPgu3cknVyD54xmz7JOkrqPaaIHZmh1gyCpwuQYjcOSPnbA-9PnwKa0ZrX48AmabUwqherEk8zc53lo3gUeoPeTeWJ9PVSfh9Q-QQOL-OON8zdzg4WOEq_NdbVXYPN-sGrr5tyhJCKuVLNoZkTXBFSRQBi4pwXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با کره‌جنوبی روابط خوبی داشته‌ایم اما هر مشارکتی در اقدامات تجاوزکارانهٔ آمریکا برابر با هم‌دستی در تجاوز خواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461085" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461084">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrO8iXxOyWNbmhl8vh6jzb4Xc5PJqIoZSfWpTkzGCCvbCYaJYnNIXixLCveDr_nGhVAo2A2lxG2pPNuBofKsTszI6ye04V_Wc-pW1i6VcIQywgE893H9ScTUMpi26sEThWcY_fF3KRGy8RpQQWelRhjllxCyz4ahItEkx3P3-OzKorA4KMFi2wsm-Cai9PjxHdCIQnxKckBNWMKL9CK37MLUFHEFvGAFAZUGP97JS00-uDF2NocxV5TxGWaQY7ykfR-4N0GW4ZVg8NKevUYV9z2rpYyIW0B7na-a_neAQ2C7OY1OYpyhUVsRZLNz1wRoc3AyJdvEYTi4SfGu1prp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نرخ سوم بنزین رسما ۱۰ هزار تومان شد
🔸
از راس ساعت ۰۰:۰۰ بامداد ۱۷ شهریور، نرخ سوخت سهمیۀ جایگاه‌ها از ۵ هزار تومان به ۱۰ هزار تومان افزایش یافت.
🔹
نرخ ۱۵۰۰ تومانی سهمیۀ اول و ۳۰۰۰ تومانی سهمیۀ دوم تغییر نکرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461084" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461083">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6mqYma6l-gSUi9P-Ys4tR30P2rzTo9KvSoWN5DNfxiHcvy1gTFuRkGlgNM-XAZlQQhKjvIIHr_65xBGY1zcbjX-yIuiPjTJ_6GAcGs7SXKp23eEQMQ2s5tBN_BaH8nlZ5rBKPh_Dil7ohdM3dP6FfYAZR_r8c-9Q5rizck0CC1frRG-wyxqiyxY1sfJVqEj_oEtUnR9mg65ARqrzKl9YmQ62Jrv1lNfhnxcvdeN3gsCww8NBRJEKAx7iLIha6PKM564FuUVejCS5_5aVdL1VKGeDgvpVmfcDSpG7IeAp1kgOvoK5_2GCH5Xv0zI7aQA5Tn3gx7Lklk7urM_m9cF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461083" target="_blank">📅 14:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461082">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ccdbf695.mp4?token=gxk_ggnVi59MEKBlry18orkcmDztGwsAYupLf22h7xGB4tN9DaPB2cbIj5kHE7i6D-82NvEy-nwzh4Jj1qFHf4qj-ifwZtrvdTPaoywHLMMtx8K-4z-dsgavWk-pO71RyaMRJImjQyUs7DVE0-8lVLZh6mCs22-rJtQuAVX1xv9LVplZ8xfp0w20cS430GsE1TC2rrwz_Gfhl0pPx-j-tqlOnOAKz6xc2DYIWi2frIeaFnM_p4QFSHUzzVL9k4Ba3NkU4sXlt9w_9_hKPTIQXKQWvukNyqWVh1LzEwmxizozZVt2i_OljyI2sIlwszSdazm3s4UfrMZ_KOgzShEdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ccdbf695.mp4?token=gxk_ggnVi59MEKBlry18orkcmDztGwsAYupLf22h7xGB4tN9DaPB2cbIj5kHE7i6D-82NvEy-nwzh4Jj1qFHf4qj-ifwZtrvdTPaoywHLMMtx8K-4z-dsgavWk-pO71RyaMRJImjQyUs7DVE0-8lVLZh6mCs22-rJtQuAVX1xv9LVplZ8xfp0w20cS430GsE1TC2rrwz_Gfhl0pPx-j-tqlOnOAKz6xc2DYIWi2frIeaFnM_p4QFSHUzzVL9k4Ba3NkU4sXlt9w_9_hKPTIQXKQWvukNyqWVh1LzEwmxizozZVt2i_OljyI2sIlwszSdazm3s4UfrMZ_KOgzShEdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوشحالیِ مردم از شکار زیردریایی آمریکا توسط سپاه  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461082" target="_blank">📅 13:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461081">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه استان تهران: صدایی که دقایقی پیش در ملارد شنیده شد، ناشی‌از خنثی‌سازی مهمات بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461081" target="_blank">📅 13:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461080">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پاداش جام جهانی برای هیئت‌رئیسه گران تمام شد
خبری از نام تاج نیست
🔹
«شکایت سازمان بازرسی از برخی مدیران فدراسیون فوتبال ظاهراً در دادسرا منجر به صدور کیفرخواست شده و این تصمیم قضایی مقدماتی است». رئیس دپارتمان حقوقی فدراسیون این را چهارشنبه ظهر گفته.
🔹
برخی فعالان رسانه چهارشنبه مدعی شده‌اند در «پرونده فساد فوتبال» نام مهدی تاج، رئیس فدراسیون هم در این کیفرخواست آمده.
🔹
بااین‌حال پیگیری خبرنگار فارس نشان می‌دهد موضوع شکایت سازمان بازرسی کل کشور پاداش ۲۰ هزاردلاری به اعضای هیئت‌رئیسه فدراسیون پس از برد برابر ولز در جام جهانی ۲۰۲۲ قطر است و مهدی تاج، منصور قنبرزاده، احمدرضا براتی، بهرام رضاییان و میرشاد ماجدی از دریافت این مبلغ خودداری کردند یا همان زمان آن را برگرداندند
🔹
مهدی محمد نبی، طهمورث حیدری، احسان اصولی و خداداد افشاریان دیگر اعضای هیئت‌رئیسه در آن زمان بودند.
🔹
حالا رئیس دپارتمان حقوقی فدراسیون مدعی شده تشریفات اداری پرداخت پاداش در آن زمان به‌دقت انجام شد. دیوان محاسبات این موضوع را بررسی کرده و اقناع شده و تخلفی را احراز نکرده است.
@Sportfars</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461080" target="_blank">📅 13:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461079">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-dhLPVetX12KraZ0hn-IUfFB9GPUZZVQr2WDFyq7bpYF-Sdisozm_Iq0d2h4Z8xxyOMXo0vp6eHptykuVF1jwgEhEQLF2H4BwowHrMz8p9FGSrFwoP9ledIjrTRFGQNEye9TLZ-2z0Z9rJJpQtUw2NHW-kEDucEtQ7xz0AqT50MWSZBfQUypUuHZqTPK1urhVO3ZrOrtEyEk6eW2sEpuZAdgCf_zWjKa3ZRi6uAhseomIGWIHqv9SBKcvFSZIlDg1wZYsOu0exG-d0tf6oM87WKrAG4kFRHqAPA2SBosK6LDlyh_mEGcnqHCCiUyV0Z8sIenh7nvvGnjpYQ9vsIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی شاگردان پیاتزا مقابل چشم‌بادامی‌ها
🔹
تیم ملی والیبال کشورمان در آخرین مسابقهٔ مرحلهٔ گروهی مسابقات قهرمانی آسیا با نتیجه ۳ بر یک مقابل چین به برتری رسید و به‌عنوان صدرنشین راهی مرحلهٔ حذفی شد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461079" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461078">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrazUUi3DJdQqEJGu7O8oPy4Y7t3lwKdiPzkrnGDLDy7zkDLNz-nKEh1He_hFhKVqR8QlWOj6R6jr0zuIQCuk8e0ksoUeWHSnMKX0xcw5OywRQzxHgI9_nVnUmBIZWD4rBo43abJpqNP-FpRpQeL4xDSmlW_12dd2pwlqPG4CfcihczTk2nrcIMLvkAifWWP-CgMVkOcT-RhzRjRuikC_a-lkqJg9GFVsGGRlF8pzpASN0lNEngsZV8MHr9iSJELE4RSG9c8iSN3ymYzdvWqJFr0YWc3ZNdaaf1IaL2imBefO_GGn9r6Px9Ubk0bykDPb5AFydT9pk4mT4fi8p8vxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش‌ها از هدف‌قرار‌گرفتن چندین کشتی در خلیج فارس
🔹
سازمان تجارت دریایی انگلیس: چند کشتی تجاری در شمال خلیج فارس و دریای عمان در جریان فعالیت‌های نظامی منطقه هدف شلیک قرار گرفته و از کار افتاده‌اند.
🔹
همچنین یک شناور لنگرانداخته در ۲۴ مایل دریایی شمال غربی بندر راشد امارات، احتمالاً پس از اصابت پرتابه‌ای ناشناس و ورود آب دچار کج‌شدگی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461078" target="_blank">📅 13:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461077">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e1466598.mp4?token=AapEv4YFg3AFQev7fE91ml0PfCOmmQIPa1iasiHU6On9uCOJjV-8sGbU3QT10bTS4w-UkJAOjhGi4pU7d0YBXT2U3iM0Mix-WItWDN1qkLHlt1pZ_prMybqrPDRaf-C7xomAQQDoOyM36OkGjaSpaqRHBHIu_JpJmgKBF6fn0xRlT7k0F-c8WiV_2ldsMfLlaiWnW3xkU681_X0KYx6IJzQobRKPhlf1OYy99ZDHAQTHr4DoXiKanY6-nQyhg4r200NphWmRmq6Rju4in2itNalUAsE2ZOAmWZe7npasoMBCsa-Ya5mgGyuviTBhP71TfRVwtSwsCKdfBMPyV-O7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e1466598.mp4?token=AapEv4YFg3AFQev7fE91ml0PfCOmmQIPa1iasiHU6On9uCOJjV-8sGbU3QT10bTS4w-UkJAOjhGi4pU7d0YBXT2U3iM0Mix-WItWDN1qkLHlt1pZ_prMybqrPDRaf-C7xomAQQDoOyM36OkGjaSpaqRHBHIu_JpJmgKBF6fn0xRlT7k0F-c8WiV_2ldsMfLlaiWnW3xkU681_X0KYx6IJzQobRKPhlf1OYy99ZDHAQTHr4DoXiKanY6-nQyhg4r200NphWmRmq6Rju4in2itNalUAsE2ZOAmWZe7npasoMBCsa-Ya5mgGyuviTBhP71TfRVwtSwsCKdfBMPyV-O7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی امید راهی بازی‌های آسیایی ناگویا شد
⚽️
از میان ۲۳ بازیکنی که عبدی، سرمربی تیم امید از آن‌ها دعوت کرده فعلا تنها ۱۵ بازیکن در کنار تیم حضور دارند.
🔸
استقلال و تراکتور فعلا از تحویل بازیکن به تیم ملی امید خودداری کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/461077" target="_blank">📅 13:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPyQvhSXY7eGF-Pwa84M6hFpzF_bZMMxWi8xFhLiHOpxgldAMXpPKD_uQqWGYngr6dYjdKGUmNXyDpMvN8PxUMCcpmXh-t_b97X1_6PTE6vEHfl6VS6xdr4cNpBAH4vGVRG_3836PxsB7p26TRqvyzI0XfZkqVtQD3Pfhu1guDjXhOf0gyllBXMA-8unw-selcm1XNjc95XPRgEl0zRGc2V8c8a0pbv342QX2ZqsAY1HPJQ55dro7zP8BmzJozpvFWpD4siOQFNNnRqQAIBOJUfhgc1OtSZLgrokZgsN_9HPGq_8kdj4WmTVIDNUR3TrUd5MUw1lYtAR4MmWzlBqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه عجیب ترامپ به دستیار زن خود؛ ۴۵ هزار دلار نقد!
🔹
هدیه کریسمس دونالد ترامپ به یکی از نزدیک‌ترین دستیارانش خبرساز شده است؛ رئیس‌جمهور آمریکا ۴۵ هزار دلار پول نقد به ناتالی هارپ پرداخت کرده؛ رقمی که تقریباً یک‌سوم حقوق سالانه اوست.
🔹
این مبلغ در اسناد افشای مالی کاخ سفید فاش شده است؛ اسنادی که نشان می‌دهد ترامپ در مجموع به چهار نفر از کارکنان نزدیک خود ده‌ها هزار دلار هدیه نقدی داده است.
🔸
هارپ ۳۵ ساله از نزدیک‌ترین دستیاران ترامپ محسوب می‌شود و تقریباً همواره در کنار رئیس‌جمهور دیده می‌شود. او به دلیل اینکه معمولاً یک چاپگر قابل‌حمل همراه خود دارد و مطالب رسانه‌ای مطلوب ترامپ و پست‌های شبکه‌های اجتماعی را برای او چاپ می‌کند، به لقب «چاپگر انسانی» معروف شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461075" target="_blank">📅 12:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaBerpwsfndxgC4uCtif_voPc41xia51BDE2yD6ekMZpfzIAQktbha5bMJ1VNHJw8a_ltuJCvZQUI7HIFhFgyPfa8GzuDdsh2A2kGLVLfq35onZ4UGS60cwpKxPL8KR07TUcga2oS6Yba3hCeT-fvuoQndWv-3r_1n8bhPJrqHEo_qtpl95QNe28vQWFpB1Gm7UmW9F3rpKZRTlv5r6-TP4YMWSU0Vo7zKGonbjbhWRS3xUwP3taOotMpLLh6XxpQvee7o1cR_MZRAPpJw-ug_w1nt31ExNhmL-FA5QVvCGSVOZJSEj4MrGxMVgXf8mZSW9dL44Mx9vMDmQ5KO7uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس همچنان رکورد می‌زند
🔹
شاخص کل بورس در پایان معاملات امروز با افزایش ۴۷ هزار واحدی به ۷ میلیون و ۱۲۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461074" target="_blank">📅 12:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE0zAHYu8y-XJREzOQRechHuZ25cybRv1EovkAaRTNIeVytWqDKPZ3qkkZM12Zz3FCkgvO7t3vr_PSVdd6G1J-6_xIqTaWOnD3ilwSBrRAs5XXzJoazjcjvGK-fKPKr84ZGbBSEH7vdWLmVVhf6Z8DvjT2abYROK3oQeF4LpnobCf88AxXvMelLBn1QF9BtfuHAF47Gpmyc6soDuIV2G6z86b_jHkpVccZcqhLaN1O5FB-lW2DEMaNDu_LuYhSE-adx8ZlEy-qYn1wrScLNijdK8VZoJ5hpPREjHTBlf-77YNHbl6WOWoxinY8dhtfd47iFEhsbcWKC06I5Z4tLwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک بسیجی توسط گروهک‌های تجزیه‌طلب کردی
🔹
سپاه آذربایجان‌غربی: ماموستا محمدنزهتی که سوابق طولانی با بسیج اساتید، طلاب و روحانیون داشت، توسط گروهک‌های تجزیه‌طلب صهیونیستی-آمریکایی به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461073" target="_blank">📅 11:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfLl-6pHKFlu_zM4Fj14y6VZZ3azrkXXGNRL3J07SD9PFoGKDANs5qYOaahKVoVXMJStD324MZsSV5cDuroozU3flGpDknkiQ8FroqTbyEmUcJEjGyQHbEvG2GTB6zThnPNi9gnmE6ueU8ENIfA9vDcae_Qo2DrRoNphSWZ4fBNxfkbtg7PMYQ_6V3RpVs0LR3dmVU9yn7fLTjcsfe1Z22Tjl6iQkspgsoLp2Y7Ujfg3cnBX8ZgoSvvqjMY2o_0sQgVVVy7HbDbUgSWjGqtfE5kHZfxkZCw_apZ3RLydauQSSyE_yMKZg2wOWwNNYadNCUx_vxnw8zL8obx2iSas3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۵۶ کيلو مواد مخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: در چند عمليات ۲۰۰ کیلوگرم تریاک و ۱۵۶ کیلوگرم شیشه کشف شد؛ در این راستا ۱۱ خودرو توقیف و ۱۰ نفر دستگیر شدند.
عکس: مجتبی گرجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461072" target="_blank">📅 11:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZmUrwT-h4_CD5E5lVHfqLorDgdFX68vtE5O-vHIuuDGTMzgjCtG12PVrOl_FYZLCyZz2tYqTK0VuHIq2HU4F8dNo33vgtIIHCp8rwOojfrm65VkmNmhKI-PTz2iR94KSSNj_lxDt7QTEwMjs6bgupDuKGUL0CuDCueLvQm6tvMq85pVSbEivfGspVnakWd1nfRFjC4YmzcithskT4KIH8ILlrd8YStnQU3N08tkZgz9eD5vX67R6nGG4-7vCvzZp3S2QRdY54crIANwuALb8BHxPLuyw2SCFFwCzfEcxQCCFc6gJoObt8J-F8c2iK284MLdr5xmbFf2pywiRXutkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ آمریکایی: وقت اخراج هگزث رسیده
🔹
نشریهٔ آمریکایی سالون با اشاره به استعفای وزیر ارتش آمریکا و انتقادهای فزاینده از عملکرد وزیر جنگ ترامپ، هشدار داد: «وقت آن رسیده که ترامپ، هگزث را اخراج کند».
🔹
یکی از صریح‌ترین انتقادها از عملکرد هگزث از سوی تام تیلیس، سناتور جمهوری‌خواه مطرح شده که نوشت: «من هرگز چنین مدیریت نالایقی را ندیده‌ام.»
🔹
این سناتور جمهوری‌خواه اقدامات مدیریتی هگزث را در بهترین حالت «کار آماتوری» و در بدترین حالت «مرگبار» توصیف کرده و پیش‌تر هم خواستار برکناری وزیر دفاع شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461071" target="_blank">📅 11:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec5df6375.mp4?token=rhh8XID0zngXbBcl5ayDoe3tc3kAQj7x1Wrh_E2XrCHX_uTjXhBzQHv8njYc793sNOKkAXfZkPTOAYpWhR-VixUzHoftu3tW_TbBpHDmPapnsgvKEuIQZofpmMw19zfBzdLcI4P9qSfWMMPYwkzxS4Rdb-BxmIM95-54hoqUJztvyX1ws0kpXjSYW3TjFYvOEh-P_ueQDJPnI90XC1JctFbCREdvDfp7AMUIpA9qCULo2ZCsbYbUElYlKgMl8pGA9CFSR-QUGUrQ2DvYTB5vdsCgX2vm8ND2NLejB6N5zSOpD7iBYyfZ8lgG2qPCid6PmizYk_5xW-cM3Ekks-LLzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec5df6375.mp4?token=rhh8XID0zngXbBcl5ayDoe3tc3kAQj7x1Wrh_E2XrCHX_uTjXhBzQHv8njYc793sNOKkAXfZkPTOAYpWhR-VixUzHoftu3tW_TbBpHDmPapnsgvKEuIQZofpmMw19zfBzdLcI4P9qSfWMMPYwkzxS4Rdb-BxmIM95-54hoqUJztvyX1ws0kpXjSYW3TjFYvOEh-P_ueQDJPnI90XC1JctFbCREdvDfp7AMUIpA9qCULo2ZCsbYbUElYlKgMl8pGA9CFSR-QUGUrQ2DvYTB5vdsCgX2vm8ND2NLejB6N5zSOpD7iBYyfZ8lgG2qPCid6PmizYk_5xW-cM3Ekks-LLzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بسیج اساتید: از ما نخواهید که بسیج ساکت باشد
🔹
هر مسئول اجرایی که در راستای اهداف انقلاب حرکت کند، باید بسیج را «نِعمَ‌العَون» بداند؛ ما حاضریم برای مسئولی که در راستای اهداف نظام حرکت می‌کند، پادویی کنیم و به او کمک کنیم، اما اگر مسئولی در این مسیر حرکت…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/461070" target="_blank">📅 11:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49cc49bb7.mp4?token=a5De2eo5lhh13MFbkPAUzaa_Bee5okUrFeXNlWnFYQAoyO_VGnhsnc8cd6qZSo5UjD5R4Q1_BcPG9-Vjer0gXri8mDvZ01y7rY1bPvC2Bf_Xb9eXk9DxO-w2Q7EjyAXOGB1ydJXIYfZ_QTuUxGQoPEpXiNFNUKr8Psup_AJGF_kP6iSniYjObqhp0Xh9Vf_298TXXhMfM3WFW64LPnvKP1oyDuQOouJzN5vrOVWq4q_Wf-9xcepH7cA8I8XXPEEhxlxN3HhNGGL7gM4gvFtZMdrEAIET0eIW7VSa_eLP4ELbkgOOcvadWO-i3jcraGhCsgBWPJYtExZcUhPZnNgtHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49cc49bb7.mp4?token=a5De2eo5lhh13MFbkPAUzaa_Bee5okUrFeXNlWnFYQAoyO_VGnhsnc8cd6qZSo5UjD5R4Q1_BcPG9-Vjer0gXri8mDvZ01y7rY1bPvC2Bf_Xb9eXk9DxO-w2Q7EjyAXOGB1ydJXIYfZ_QTuUxGQoPEpXiNFNUKr8Psup_AJGF_kP6iSniYjObqhp0Xh9Vf_298TXXhMfM3WFW64LPnvKP1oyDuQOouJzN5vrOVWq4q_Wf-9xcepH7cA8I8XXPEEhxlxN3HhNGGL7gM4gvFtZMdrEAIET0eIW7VSa_eLP4ELbkgOOcvadWO-i3jcraGhCsgBWPJYtExZcUhPZnNgtHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مالکان
ماینرهای غیرمجاز یک سال برق یارانه‌ای ندارند
🔹
مدیرعامل توانیر: با دستور وزیر نیرو از ۴ شهریور امسال، دارندگان دستگاه‌های غیرمجاز استخراج رمزارز تا یک سال از برق یارانه‌ای محروم و تعرفۀ برق آنها تا یک سال با هزینۀ واقعی برق محاسبه می‌شود.
🔹
مردم قبل از نقل‌وانتقال به واحدهای مسکونی و صنعتی جدید از شرکت‌های توزیع برق استعلام بگیرند که برق آن واحد به‌دلیل کشف رمزارز غیرمجاز غیریارانه‌ای نشده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/461069" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp2UvO76kp-bJlNIjfdKlxquKNEP9uFbRkklJLwS3LKQI4YkJsexTLBkcNQJz4EA_VNtzs04mYzbXRouoL72AVAW6CjPs2zdJD2CTcJytIkP1QsVt6GK2BFBdBSASSN6Gk-0Lze6n_kFO3tWMlGpeKbN5dassWpRmHufbhELqb5aCSOUJVl2IkLbrilCewJOiC7iNE1wsLfJjCUb6oeFg-kPVjkjH20Z2HtozWmNaoXMBwc4g9_Iz3NevKLRUruvixL9S1rONQRIxhXkrYCmWawJ3pQaNbhn-6fTBGM7OR2f8rrfLmotD5STP8cLWtv_D7mLTzv13I8ZxJ2pU3UIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیر بانوی ایرانی، طلای هند را شکار کرد
🥇
در ادامه مسابقات سری جهانی پاراتیروکمان ۲۰۲۶ هند، امروز چهارشنبه هجدهم شهریورماه، سمیه رحیمی در فینال ریکرو انفرادی بانوان به مصاف حریفی از چین رفت و با نتیجه ۶ بر ۲ به پیروزی رسید و با ایستادن در جایگاه نخست مسابقات عنوان قهرمانی و مدال طلا این رقابت‌ها را از آن خود کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461068" target="_blank">📅 11:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA4JoM7453qBrKsfxQYyeezbkQLxzc--SBF9LxWCgZsn7XkYnfOo41-O14qwwS7GgkunEnwJVucdcffp77oheyOZZxgvzOu1kesCKONUYnZr2Os9Ds7QnLrTXgbsJA6SOigEkkoZhYn74pQKV6cfmxTNT6Y5UdOKu3lwc9hm1LfzzzWA3lmjuBxVvpyxt5313RbGdPEkCnqppA7_aGRU4IW6qrU-GHsWUNXfQVkwCj785M0M2b_tBAFFZS7pAE3ino4Ay9rfk68mwRzku3feBXmNt-kEApDkVcKLWN5sQkrRoIneBzTgDRQR9PGvO4QykYIXuVi3OI0xX99mSeFGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت برنت به ۱۰۰ دلار رسید
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461067" target="_blank">📅 10:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461066">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19139f9901.mp4?token=lPh3a3ccJ3avq4am4gnn9evoOxvTzpaU7mmqsxf_Q1t00Zd6Cls_-Q9jG-V5_P2sPGvOhvzE78GxUaymvjkDGHpToO0NmAr0XXa9gNLuCTOFA7W3eoBiqV2KIvAnManyCFgr28sLntTq9R-zix6Tz6pd3g2NggZkHU6QCmNcgwiqNTCmwihuIpEpttqsBY0zH8fXfTwi0AQZI9Fy2IEk3syxoXbf4QZx5r92W3r3XHJRnpyykL1YmhLwsWGzaVH3_TUSRa5eBMxv3hv2tQ9Lr7VNyEJ_3xTnXYUaqvyVvVWWoRPGVrI_19b7FqNNg7HTxoKEUpIeIlqIZYT2C257IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19139f9901.mp4?token=lPh3a3ccJ3avq4am4gnn9evoOxvTzpaU7mmqsxf_Q1t00Zd6Cls_-Q9jG-V5_P2sPGvOhvzE78GxUaymvjkDGHpToO0NmAr0XXa9gNLuCTOFA7W3eoBiqV2KIvAnManyCFgr28sLntTq9R-zix6Tz6pd3g2NggZkHU6QCmNcgwiqNTCmwihuIpEpttqsBY0zH8fXfTwi0AQZI9Fy2IEk3syxoXbf4QZx5r92W3r3XHJRnpyykL1YmhLwsWGzaVH3_TUSRa5eBMxv3hv2tQ9Lr7VNyEJ_3xTnXYUaqvyVvVWWoRPGVrI_19b7FqNNg7HTxoKEUpIeIlqIZYT2C257IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ انفجار تانکر سوخت در سنندج  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461066" target="_blank">📅 10:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461065">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار کنترل‌شده در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461065" target="_blank">📅 10:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461064">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxkDQl10KNVzVcxDoMvQyIN-Jex83ipXJQiJ9ARM29JBALUdddvpt4bkiIoJbWMNu8O58NumS5Fq4PRZ41MLduUhtpRjk1Y7XFl1-xf3uYwQjHuD7FI4tuz1gCXd83aHHxWmpDj_wnKJYu9rhXmjjHbf4yY72T3yaGn6YYMOCDuaqJYNGirpd3TUXpI64lLbrCeEG1qkRWSkg3l3xIIOO1VxitIn1pHbt4EC1j5HNFEnGm942rXxZhsCGsb3JPlNFYsfjuP_JdPiGHjURULwaqn3ei2nw-435iIR4zlPZuII52wSZNrUObwpksIxVlIzcK23wOxauljisXYK6C4G9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار اراک با ۸ رای موافق شورای‌شهر برکنار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461064" target="_blank">📅 10:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461063">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAd-0efagcS0-tdECOg-6rtDBPQsQQZu5EdvntQUbFrYx6JY7C4ofZFH7qufoeDU9uxZ9VGMyu6L27xNKm6U4TRPtIMMW5sXFl087aS28L6-ZUvOhyfZSvQuJ_nTDaCNZvM6eNyx5twhqxAQW-fvXDvBXvEDE3wJl2fc3HH3ZD_95wX0pqFkMuKi7tZAxHKPbUB2pU83SYGwx-oYM4bxwzxpMvpwpaL1IDFeNw1hmEhYDwsXm3vt88QaqTt1_cGKmsGasvE-PDnsRBL_lLkPlW8ykL5YdGDxRt4kynwjQoDf0S7TNKSGWHzl3TdRb3tfxlI00KKvSDjAUlgbKwKDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازندهٔ چت‌جی‌پی‌تی معمای ۱۰۰ ساله را حل کرد
🔹
شرکت OpenAI، سازنده ChatGPT، مدعی حل مسئلهٔ مشهور  ریاضیات «ناویر–استوکس» یک قرن حل‌نشده باقی مانده بود، شده است.
🔹
این شرکت می‌گوید حدود ۱۰ هزار عامل هوش مصنوعی به‌طور هم‌زمان روی این مسئله کار کردند و در ۸۸ ساعت به راه‌حل رسیدند.
🔹
با این حال، این ادعا با واکنش و تردید برخی پژوهشگران روبه‌رو شده و دربارهٔ دسترسی احتمالی OpenAI به تحقیقات مشابه نیز بحث‌هایی مطرح شده است.
🔹
برای حل این مسئلهٔ ریاضی یک میلیون دلار جایزه در نظر گرفته شده بود که OpenAI اعلام کرده قصد دریافت این جایزه را ندارد.
🔸
این مسئله دربارهٔ معادلاتی است که حرکت سیالاتی مثل آب‌وهوا را توصیف می‌کنند؛ معمای اصلی این است که آیا حرکت یک سیال می‌تواند در شرایط خاص به وضعیتی برسد که سرعت آن در یک نقطه بی‌نهایت یا غیرقابل‌کنترل شود یا نه.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461063" target="_blank">📅 10:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی از هفتهٔ آینده
🔹
رئیس‌ بانک مرکزی: ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی با هدف جذب منابع ارزی، تأمین مالی پروژه‌های ارزآور و توسعهٔ ابزارهای مالی ارزی از هفتهٔ آینده آغاز خواهد شد.
🔹
براساس این طرح، دارندگان ارز می‌توانند بدون تبدیل ارز به ریال، منابع خود را در صندوق سرمایه‌گذاری کنند و واحدهای ارزی دریافت کنند.
🔹
سرمایه‌گذاران هنگام خروج نیز معادل ارزش سرمایهٔ خود را به‌صورت ارزی دریافت خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461062" target="_blank">📅 10:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5425e82eed.mp4?token=AbuNoWSm-dOpoYcB_5H3FdjyebO98pnlNVsH4eJBxIXxjkE0sHCGDdv5j2kY_ALN4aX-tZChRhOeZfg5LQThGy9jf2po_4y9dtMvBZpi64lc5Wwj2uF2Y654xmfcWq8JtVUozOpJWJZXUrwy4OQWUNkhu3zpsDcqSqxDtnVYfc0EhcJjxB7qhGRjoMZDFqheHlMgSifOk7gJwX6NoLFCqVbXKp3i0mM8K8QT23b49gqKAwKHxnjPKjwiHik2s3Ln1mS80bT1J26LuzMK9etPOONw8qXxsvxDPxXsBnmuMbqcrf9YGaTcs3qRKqSpOdAaeUGAMsG5AXHa_weKQ_TZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5425e82eed.mp4?token=AbuNoWSm-dOpoYcB_5H3FdjyebO98pnlNVsH4eJBxIXxjkE0sHCGDdv5j2kY_ALN4aX-tZChRhOeZfg5LQThGy9jf2po_4y9dtMvBZpi64lc5Wwj2uF2Y654xmfcWq8JtVUozOpJWJZXUrwy4OQWUNkhu3zpsDcqSqxDtnVYfc0EhcJjxB7qhGRjoMZDFqheHlMgSifOk7gJwX6NoLFCqVbXKp3i0mM8K8QT23b49gqKAwKHxnjPKjwiHik2s3Ln1mS80bT1J26LuzMK9etPOONw8qXxsvxDPxXsBnmuMbqcrf9YGaTcs3qRKqSpOdAaeUGAMsG5AXHa_weKQ_TZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار
🔹
مدیرکل طرح‌های ملی وزارت ورزش: جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌واحد دولت الکترونیک یا سامانۀ جوان‌پلاس ثبت‌نام کنند..
🔹
اعتبار از محل وجوه…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461061" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaFP0nJB4j-_nbH4wPmjvmF_LFOxF82zPupyxG0ao1t-KWS41Q83KYtlcIQhphjVLCub2mtfq9m3ROD-_UVWnzNM-O46A5Mvfi3mt69DFISwDON9z7qfpLlzySryzX2HwbbPxRO-eNkqORAaRPgy07P_5LgDEi9cDRzRHoHYCI1OVXH0si27PuawvWh6G3j-AYCQzniKJDzIKhcvh8lNiwORhnix4sMPNpPuCy2Ws4pgf8GNBRoD9dKGa2OzKVaKMjWkJUdTu_FqKyia6hGhtB9Sq1SErsKAs0o-hJSJxbeKpIbKGClIODjp0u3QYnjECf75_Y_eTOg_lR7ybuEUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQT5VeVcfxsP2LyvtxoqHMgeRBPOSVUkgl9up_62LuY1tkl7HhpOK8-AUYpHdwV6CDBrgpapCgw7XUmfxrua3NUEknsS4TNUkgMpt_03ZvhAmoCGPj4o2gUgPot-DnNo1yMf2j-yzRYawhvzx2rrEayQUdIbAn8E5wCaoByADjT6ZOtzpZEbkUA_ns9uqvjgXzSZ1VcKUxU6Iv0j25NAaWpWNbtgys-2SdES0wPmqBexCJimyNcnIedQrT_91CY59fXkip_RxQSOfcfLGViqzlvMfdS9mfYwD1ka23F21vCaSJYMLJwxBh1sgBjT-z6jdyc_do9lP0J1eOTR43Wa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3350ssxkwsr_q8hKdJ3zDLsYO9MFkhpVQjzu612UV-ygetgvkeKSqp5SCbfJQmrzWXw_MBldxpxBpZQ88DXt5C97h8KtwFpBlnMUToEZYweAHrzI83-oQoNUmj-34clvs18hzcF85TpxftLMbgO4o9RQBI6n9PDVOhallwuZMN71w_rLO6eovIHsRgyAlW51xCeO09hCg6618LgBunVWPQOG6T7J2qV1M6SP4QA3334sFejUvhYzeap_IfARlHeAwI0n045dHfRmu6H7YQ0ykwRYWKCgXermPnFRBeOVa1A8Jy-JFbvoZX5t0w6mo9irA7_s1LLx6RXv-CMPp4o3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7QrY4Viu08C6XeiOyCh8jFlBt048xd7-oFMVcXhlt1sN81cuJlJosq_k3cNJFcfU_g35FRfJiOXox1-W7LKfGC3w_JffDE-FAoJixK-691u-ttjLxeHRoPhAMWfABnhgwvsF3brl5TsuUcfupQwxXgDMZbYd6cf2jX1dhhSTp4-AS2MQT0qanDk4sAOyIzr28DJGz9qInecb7a5NfnO4A4TVc-pyJo4LPQjOc6N97nsm20drDrAj1IHL_xXlQKvjj6EF5SH_ENkVNYsajSM43p8cPBbf1vdfXF-FFZvVQdQ-H2QFczsW9Ldn4bhzwFWvTEyqVwLQ19TYB-d7ijcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzaFm6qF5QTF2t0259fqy03Ve1W94h13NzGzvbUd8UphDsBqoXa6zPIgWPKcCYI55KRVs_9fJkuLRvlfJfFjr14cmb7lF0K45RHUeww8Ql3zZWiN9RW-cnlbDR2_frUirEsVCmHJpyJBg-eFkMEQghqAR_qmjTXoBHc8gGXg2SUVrPkErZwzMU1YWobQPGU64Ojbea-UFAJKL192TRQKLfjQD1EKW7XGlVEU61mWQLOr6zBrCclCf6Xg_fn5y5gsPPTO7cIvcEsOZan7EMcELRnXV9Y5_8kRh3Sic4M1rqcAHMdKTiGktSl-OQJOs4F6ws85_K_AAyzmv2Pbk9ODsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شور کتاب‌خوانی در نمایشگاه کتاب کردستان
عکس:
بختیارصمدی
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461056" target="_blank">📅 10:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=H7OYqfBD-V6lS5U9AC7SEzux-lEcbhLcVRL9XPxFtS_OeJbalQXhsnKb9B4yhSO3In_D_yjueXYOC5xCMdnwgzat1UDCv0WpL6anqJOraE1mYWFz7u_sqR4mk4z9YcpFNWIN7wD_fN9WKOUlzjdf3rVtjuWyOZUy2egiaHetKLvgBcdO1xIarVc4V4zn5RMCTt-AJnw3tSeGJkmonoU3i-R5wsY-_9baztc34QJcOmu9WCWJpSxiGJ-Di7fWeFFK0dgpwYISeNsqyHtADCFA5bjFwpLBFwwQ75c8-rx5gBpocRk3-_VWLzH99THasJDpNVBsZXq99tAapENEpvU0yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=H7OYqfBD-V6lS5U9AC7SEzux-lEcbhLcVRL9XPxFtS_OeJbalQXhsnKb9B4yhSO3In_D_yjueXYOC5xCMdnwgzat1UDCv0WpL6anqJOraE1mYWFz7u_sqR4mk4z9YcpFNWIN7wD_fN9WKOUlzjdf3rVtjuWyOZUy2egiaHetKLvgBcdO1xIarVc4V4zn5RMCTt-AJnw3tSeGJkmonoU3i-R5wsY-_9baztc34QJcOmu9WCWJpSxiGJ-Di7fWeFFK0dgpwYISeNsqyHtADCFA5bjFwpLBFwwQ75c8-rx5gBpocRk3-_VWLzH99THasJDpNVBsZXq99tAapENEpvU0yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترمینال نفتی روسیه در دریای سیاه هدف قرار گرفت
🔹
پهپادهای اوکراینی دیشب به یک ترمینال نفتی در شهر «نووروسیسک» که یکی از بزرگ‌ترین بنادر روسیه در دریای سیاه است، حمله کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461055" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انهدام باند فساد اداری در کلاردشت
🔹
رئیس دادگستری مازندران: پس‌از انجام تحقیقات در پرونده‌ای با موضوع فساد اداری در ادارهٔ جهاد کشاورزی کلاردشت، ۲ نفر از کارکنان و ۲ فرد مرتبط با پروندهٔ به‌اتهام رشا، ارتشا و سوءاستفاده از موقعیت شغلی دستگیر شدند.
🔹
بخش عمدهٔ جرائم افراد مذکور، موجبات ساخت‌وساز غیرمجاز در اراضی کشاورزی کلاردشت به‌عنوان پایتخت اکوتوریسم ایران را فراهم کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461054" target="_blank">📅 09:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV4K7QkJqTjltft4XTAe3wRmR6vpahrr3YL89XW_28mFOObMK3OCFjr5uHZVxdTy2Z4VhGL8aKbACGdhqbc52WKaGYp0J4nAq-DHYHkc3U6PhScqQhLzHR3zCw4Al7Fu7Zw7EuX5WHNPl0aDI4msAegtmD8QnUnZWlruj30DwPARbNO0cASzVFV6llc8MM8EYC_FXeYf7qofvvZlgYp38emUBWc2VBTS4aJTqYSdXsluhUYEkZcN1mnmWAMqdJS8-HbNiBQC0FU6ZI_mEmgKiu7bkIoijEQUBGlZwMXGOePE47esvHC-KB0e9A30oMtyhaBflCfuR_TjUkv3hMmpFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461053" target="_blank">📅 09:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tns9U7-8NkwK318n3Ne5HFW9Uoha3C_tbrgr1RO1tBBIAZxIy-elt7BHyb8U3ELkE1VdORokAdVG4x1ZtX2OtabzFalvTsYLDG3zf1gnRybLWTKTfzAZb3yMbg_HPV_TPUhL8Xpwnapk7G5gtbtSSVGsJiiTJyKxnfQmxOIN3GPWWzQJQuEya2z3DS9HtRN58A7irgnw5QFFdin_S-l63EWt80JSMbboRWthZJ-J4x1jur3CDYyTfEY_6lWe8Ji5AtpVLSyoDjp3PqSQtOF0o2JaOq4vsox6ORnBPkc0p-8GL70Xm9JBqUMbl0Vry_pGxHRQKEU7Qh33E6DSpN-REA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت کندی اینترنت در ساعات گذشته
🔹
مدیرعامل شرکت ارتباطات زیرساخت، علت کندی و اختلال اینترنت در چند ساعت گذشته را «قطع فیبر نوری در ارمنستان» اعلام کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461052" target="_blank">📅 09:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کندوان مسدود می‌شود
🔹
پلیس‌راه مازندران: از ساعت ۱۳:۴۵ مسیر شمال به جنوب جادهٔ کندوان مسدود شده و از ساعت ۱۷ به‌دلیل وقوع بارش سیل‌آسا و احتمال ریزش تخته‌سنگ‌ها به‌طور کامل بسته خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461051" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09b7c06c0.mp4?token=koIJG7DK-Brj7nz-YqQUEalrxHZ-ZRBevVL05bDnwRVpNEH3eNnSFMxx5DlD7R1GCyj5xT5cXe4oI8Npifwln06WG0hLNY3sYx1m1Vw8kDf7moXgFEixnIevISBLPDBOlMkuTW3DNw2_JG7TQJrjTkaCWvN8LGtAkye2eas5r5bFIUjskA3IUTbzyNq-A9gs5ocRPwGSdSq9Q50e9QWeLVaZ9_TDupyRIkr3VB8letSklkakaqsj6ydWJg_jU5-wwUfqioyo3ehOtc_yPoKNcahynhFfhs-m7hcENjBuQ1GeU0z3_ukp6DFiRhM6ZCpiEz-bEZvw_ybDDti-JmUOtWNumbigQfD3hCX2PaJyH2GxOZ0QIIzcigfjkpiWEi_CiFKgyAD-ydgp8alw9FIzJdnW26DCHAT8riCwFsH9bebxL3ESpgFlfBtHRQ3w0fkaQPw6m92CGMd7EGgsZ1q7xCKmwRPV0aFZFDRRbuRcc5bdTS2DK790fmsu_cAYam32eEtiknh99z_5neV-NcDCr3vgUNjYKg-hpLDx2kBuVpgTzuT4h9SEughMItdnyqsg_7_mAKkL_sMbVhktEmClicFx_1B2LK-ULAHfRnzoskiAGg29zCPU6znd6jvaB9CZbTzyvU8zkxAwPXx8u47TNmzOjKcKXEOln2OnuGYxr0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09b7c06c0.mp4?token=koIJG7DK-Brj7nz-YqQUEalrxHZ-ZRBevVL05bDnwRVpNEH3eNnSFMxx5DlD7R1GCyj5xT5cXe4oI8Npifwln06WG0hLNY3sYx1m1Vw8kDf7moXgFEixnIevISBLPDBOlMkuTW3DNw2_JG7TQJrjTkaCWvN8LGtAkye2eas5r5bFIUjskA3IUTbzyNq-A9gs5ocRPwGSdSq9Q50e9QWeLVaZ9_TDupyRIkr3VB8letSklkakaqsj6ydWJg_jU5-wwUfqioyo3ehOtc_yPoKNcahynhFfhs-m7hcENjBuQ1GeU0z3_ukp6DFiRhM6ZCpiEz-bEZvw_ybDDti-JmUOtWNumbigQfD3hCX2PaJyH2GxOZ0QIIzcigfjkpiWEi_CiFKgyAD-ydgp8alw9FIzJdnW26DCHAT8riCwFsH9bebxL3ESpgFlfBtHRQ3w0fkaQPw6m92CGMd7EGgsZ1q7xCKmwRPV0aFZFDRRbuRcc5bdTS2DK790fmsu_cAYam32eEtiknh99z_5neV-NcDCr3vgUNjYKg-hpLDx2kBuVpgTzuT4h9SEughMItdnyqsg_7_mAKkL_sMbVhktEmClicFx_1B2LK-ULAHfRnzoskiAGg29zCPU6znd6jvaB9CZbTzyvU8zkxAwPXx8u47TNmzOjKcKXEOln2OnuGYxr0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار
🔹
مدیرکل طرح‌های ملی وزارت ورزش: جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌واحد دولت الکترونیک یا سامانۀ جوان‌پلاس ثبت‌نام کنند..
🔹
اعتبار از محل وجوه اداره‌شده وزارت ورزش و جوانان تأمین و با همکاری صندوق کارآفرینی امید، بودجۀ ۱.۵ همت به استان‌ها پرداخت می‌شود. اولویت با استان‌هایی با بیکاری بیشتر است.
🔹
شرط دریافت تسهیلات، تأمین ۲۰ درصد آورده (نقدی یا غیرنقدی) نزد صندوق کارآفرینی امید است.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/461050" target="_blank">📅 09:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac68404.mp4?token=QKaOa9JGvOLD6-mokoj0jtVutrm_gfuKQirbLf7zQKIyWuaa4aMrhHtdZtRUbNkyXm3409u8faCsXTx3Ai9U8bbDbiKoCJ2hwky8E3n32hN9N8XvKEURmA3-aPQDqDFe7UMREidsI6Nq5GunDXi7a_dZMnAtb7RY8eRmPMXeZtgOijl4-dsHUYkiUyVfjENYdfuHQymU_NbB3eIYJy3Wa7ZRGF4LKUPFLwPY4qDlRyXm0j4XhFX6qHcN1pwpj1hVvDGMm4cTpSarI4tUJXEaIJkamRgCYwxPo3pAvCXmnYUqCgL5Kr1-nE18QSKCm1M3io4tMb6v0GeUfVkhCuGnug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac68404.mp4?token=QKaOa9JGvOLD6-mokoj0jtVutrm_gfuKQirbLf7zQKIyWuaa4aMrhHtdZtRUbNkyXm3409u8faCsXTx3Ai9U8bbDbiKoCJ2hwky8E3n32hN9N8XvKEURmA3-aPQDqDFe7UMREidsI6Nq5GunDXi7a_dZMnAtb7RY8eRmPMXeZtgOijl4-dsHUYkiUyVfjENYdfuHQymU_NbB3eIYJy3Wa7ZRGF4LKUPFLwPY4qDlRyXm0j4XhFX6qHcN1pwpj1hVvDGMm4cTpSarI4tUJXEaIJkamRgCYwxPo3pAvCXmnYUqCgL5Kr1-nE18QSKCm1M3io4tMb6v0GeUfVkhCuGnug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز هم سامانۀ بارش‌زا به‌کار خودش ادامه می‌دهد
🔹
سامانۀ بارشی جدیدی روز جمعه وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461049" target="_blank">📅 08:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461047">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d41b703ea.mp4?token=E6vCfVW-reYN3xbj_NYWmDy-_SuS7QiQNMZb4DG_ieUwYq-frVGBuj8qYse290whmimcsrVb6al8WFC49Tujr4-8sW1gTONcxD0GwdYAAAot_jOm9RUazhdGmJgK4iRwog3eXo5SoAGI1C6sO--1Hk3Hsh_X_723x2SItKdlFTkr-_9NPVLMBoFRVADA-sy-MyLSJcnIqpMYHL2KXfYPz4rwGZ90Otk7D2nqeifpllDZCdx86opjgojz276L_JZyXBbldkrKNHZ2lTro9eMulkKoyGAY4hC-Hj6RPvevd1ynfc2cCFjGzfs2Sf1v0nOZ2NDPF75MMu5raELP7dQpHkRGBapOje9r_xq2N0jvmEC0zKzWGdeVNXb8Gx5ECYdqKTkhCWCDX-ePNFDxsUTtVy9Ic9X4moo0yh5EizaSDWWsjtioAzRXhW2u0Wj0k6qs5dkcvgRQg-lG0dmZ0gq1GL2qtjy-aSxuzXQhtcuPSVTLmb-hoc9u320khXXaxm-PqkvbJu6E0lsIkjrTKjZS8R0OgmEcq95LssVlYLpONwaGon6F0Xulay1u5LoMaZtFemexCr2R-Ld-Lz2StnRc9v1I0G0qM_nkXYzw_dNTr714fy3GrJNezeylltRQTMHuVj6RWrcnF7BB8Wi_gPsTiDt6o8IYcSgT40XF_Pd9KBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d41b703ea.mp4?token=E6vCfVW-reYN3xbj_NYWmDy-_SuS7QiQNMZb4DG_ieUwYq-frVGBuj8qYse290whmimcsrVb6al8WFC49Tujr4-8sW1gTONcxD0GwdYAAAot_jOm9RUazhdGmJgK4iRwog3eXo5SoAGI1C6sO--1Hk3Hsh_X_723x2SItKdlFTkr-_9NPVLMBoFRVADA-sy-MyLSJcnIqpMYHL2KXfYPz4rwGZ90Otk7D2nqeifpllDZCdx86opjgojz276L_JZyXBbldkrKNHZ2lTro9eMulkKoyGAY4hC-Hj6RPvevd1ynfc2cCFjGzfs2Sf1v0nOZ2NDPF75MMu5raELP7dQpHkRGBapOje9r_xq2N0jvmEC0zKzWGdeVNXb8Gx5ECYdqKTkhCWCDX-ePNFDxsUTtVy9Ic9X4moo0yh5EizaSDWWsjtioAzRXhW2u0Wj0k6qs5dkcvgRQg-lG0dmZ0gq1GL2qtjy-aSxuzXQhtcuPSVTLmb-hoc9u320khXXaxm-PqkvbJu6E0lsIkjrTKjZS8R0OgmEcq95LssVlYLpONwaGon6F0Xulay1u5LoMaZtFemexCr2R-Ld-Lz2StnRc9v1I0G0qM_nkXYzw_dNTr714fy3GrJNezeylltRQTMHuVj6RWrcnF7BB8Wi_gPsTiDt6o8IYcSgT40XF_Pd9KBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اولین تصاویر از زیردریایی بدون‌سرنشین Dive-LD آمریکا که امروز توسط سپاه پاسداران به‌غنیمت گرفته شد  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461047" target="_blank">📅 08:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461046">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آتش‌گرفتن یک کشتی در قطر
🔹
قطر از وقوع آتش‌سوزی در یک کشتی در بندر «الوکره» و مهار آن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461046" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/461045" target="_blank">📅 08:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461044">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۹، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/461044" target="_blank">📅 07:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461043">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWpxTha7uIXP3INWntIassnRZnvGlKa-03zV2a6QvqTplSLV3916V6U7xyRMbecdrlZaBBRYaSkOYZZdkNoEx-drCI1przGHJRYjEToikc6bjIAlq5Xfk3PThurH3Rm-934xkVFasX6zO6eSIt-zGKhx93iWs72zCGRNe0zD5DBVHcZO-DkDIk7Y20Swl9_DdlgxNz1-1ZYLBOD7Qx-X2WV600KGc6K1vBXJTdz-AIDDsiIJihfSN0SFh1zGP7iXButxSjKiZBpDikbyK5UhwkjxYbAvGHrgB_w0QnzByX5u5krVvlYMr2BzERdtnfbdOuo0Anqvkz5T0eYPswqYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن به بهانۀ ایران سراغ هوآوی رفت
🔹
دادگاه فدرال بروکلین میزبان محاکمه‌ای است که با بهانۀ روابط تجاری هوآوی با ایران سناریویی تازه برای مهار پیشرفت فناورانۀ چین طراحی کرده است.
🔹
محور اصلی پرونده، ادعای همکاری هوآوی با شرکت «اسکای‌کام» در ایران و فروش تجهیزات تحریم‌شده به یک اپراتور تلفن همراه است؛ اتهاماتی که هوآوی آن‌ها را رد کرده است.
🔹
این پرونده از سال ۲۰۱۸ و پس از بازداشت «مِنگ وُن‌جو»، مدیر مالی هوآوی، به یکی از حساس‌ترین مناقشه‌های حقوقی و سیاسی میان چین و آمریکا تبدیل شد.
🔹
محاکمه در شرایطی برگزار می‌شود که رقابت واشنگتن و پکن بر سر هوش مصنوعی، تراشه‌ها و زیرساخت‌های مخابراتی شدت گرفته و هوآوی نیز یکی از بازیگران اصلی برنامه چین برای خودکفایی فناورانه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/461043" target="_blank">📅 07:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461042">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQW5x8TIRL5PApw7XaOyETVcJ-N3CZ3I4TRcOQc11Cr7Cu-H2Ek3tOBi7NnFZYKQTzgjgSWJ7UwIdcrfvF8sqn0Wh6ov4uOeH6HqBLHW5RGpT-kHCYj8_AOMbccNkt5pBOJvlVIPQ6bucGL6dHIG4I-mjcN5hAUVN_FMYBWBV3cLOZTJ5AuebmnUBmpefqOXUq1UrRs2ETz2C2KIEx6p9f0RJMXPylzUkeRiblMEFafasCH94ReVnpS3JMM-bBcyPi0CGBfz4XJhuM7eOhPFpssWKc2qwGeSiQVAy8GuGzMnGeX3B9bgotlib7w_2G1NN68xj-RzHLpT1JQ3NxNRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم انگلیس و فرانسه علیه رژیم صهیونیستی
🔹
وزرای خارجه ۱۲ کشور غربی با صدور بیانیه‌ای مشترک اعمال محدودیت‌های تجاری بر کالاهای تولیدشده در شهرک‌های غیرقانونی اسرائیل در کرانهٔ باختری را اعلام کردند.
🔹
این کشورها شامل انگلیس، کانادا، فرانسه، دانمارک، فنلاند،…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/461042" target="_blank">📅 06:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqYC3dB2SxrFDFCfnzYWlMvodrtl6ZQYQNQ3GryaBcIjBfpWLo5B8J6a4w83xDC0hhRRYg7LtKLBgJ4uWOFbX1sfdmyca2_MWhWSlfLyrulB6rPtBvxZuvkAryLSl07ZVheru-jtT_h97kWBVbwHqErmsZsu-L5UxRgOC8ajweWIOKfRbVwvomCUPXbkTVKy6ebnFkS2vO5G9XYk5Wi8DY_hN7w9nmTU8VyuC5IdB-67mXlhHWj5Fg_IJw8TExnHDIJ7XPNWPavVJzIs8gFB6RU-l53UZg8e3jd6TVgjIiCA7JPOFAKU9gx1Q7Nsm0GHWKtcZ0Jlsoe3MLQft7YZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vU4j8kpNtbkXoHKm0SCjzTPgQur9_LiiAirk3N1JiOswbgzrAElc0vB9FcL9fbqQwQ3e59VYTWuf37twXW6zHpcj81u1mFRJcIZFd3Rbk2Vcuq91MXYO3rtJz2EFoV6Br1P65vhSamHBNdRK7_l3uiZPhHdR8uod-cNaCf7TLFhZJb_U3Lj0y7UL8qI3tuYQCrVHsEFMCM2lnM3d0pOOXUQ619A3NHC4SnJ8RqttUwBnSuCJrDaDRpJnDolzLK72tPdryNP3Cqa-yhbnlQCz5ZftT-HH-niBCgaQfyKNeSVtFZ2MjdmdHALES8V6eKUFikRxLNshaVZq0wVC85tVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkKEeMG-P3RuLwgy6SASIfdzLTPHqAEdC4ke0zdHJr4e8Ekaneb4Atr_rbWt3AlK8NTgjgikJayPW3yEkYAsJBETVcdjGtE4uy9-vQkq9ltu14RZdpZDX-RiPDZh_M3m6Mk_Ni91cV0g_1ApV1op0AH3o6qfLFrpcdweDYK97omrUB6SMcKwmPUVdAC9zXhagaPD9Km9H_rp1OnXnrCbg6atIUHHkuT2NO4UNVHTBBK3jAhjyJXh7RX9J44y3g1DpqegW1AWPM-7-01DqF2zrNUFsiknKjIe8r2IExWAZ-oRqBLM5EnOGSEvF_C2GxXPOwToICiKCLLu44TXF2b9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDOaU5_ryJhvfJCeEc9_D8Pe3MH_696d2e1NzpC0UXzeEMsnlUxXhk3aL0udiFDd_sq4atKP4GhEF-oN0UXzP5uWI3j1npTStQCtfvQifgos2kOXqXLRN2BHFGqdPlpjlgaMSqshMozLXwxnzOSTsozOH8M4N120MxvDYF3JnyYLJVRlyuxR9UWyYCSWP9B5qmTUBySow2JykNjQISLt4MdbmuRWk3l2QLbIv-HsM-3lhKkfFuglcKjXFDqqXOZPjizAFBquS_mzwyuh33nPQ8okXqx92efmDf-LwOTcrlsQBy1P88GoIWR2LRkyCXcpRLoeQStmLUGj_HZgo4BWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ0DJ8_UCkYpE4gCewPxax9mLxjIUYu1tREpPSCSzm1VTuCz7yBuwt-GvhgxX825hzA28MqQZUzolJ5K0U2-fTHyhRoq6gsETGpnz9YcIAwBidngaeryNiwKH3l4o9PCS7IdyH4b-hqvxwM24j-IlVZVmqELS_N-kgs7is3la13I_2fFJhg9WF16rip2D0pmtdjhvDyyvFfVte3a84MALwFnIp6yeHRVG67wBudgvAtq_wnthDPGj496HJPSbpN5kCu883ED9yyztA2KPcsfOSLUylb6_hmWpeyQZJc37HiXbcQVO4rSBeHoqSYxzwlETPPO6iAZfZNILzZHku_H0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tex8jSkHZ5nly4bKe9YmAOGTJ30Pj-ThdN7OMP-I45Zk8I6hdCBd1P_98QEuNRaMWyu-i1LySgVi93F4EGZhcd0D94gwo1mZuiGAmQsCiInzSG54X88lI-So8vQO0ESgTwD3Sf7wl1SOQITW5ak51I7PHmOUCTUHWw6PfNFvQCvRowddZ_kLCqlaH54ev0LVfDgr8kKHXHbapU80cHP3Q7zrObsnQGcI-_fLTwa-Xz2zT4Cc0upJ_taeSuHPqFzLKd0LsojI6MvlCqi4bcFwC3RCEVzoz3NWwY_Zy3QwetWU44S5s9PjPT1GAcccV2KFFs8QW8Vjzk8hivodSlzzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZVX7W1vLDLl2qFuvdjwsrg6qnjDXcfG7fuAk7d2pBzva1YvHvvYNl5Xc23-g4TK1sA5RpccnaD0R-Yopa84srRS3W9cWahHnl5hVHvUcKVSr3pMh0IA6zKJWxTxP5E_UucoQnfg0_INrQmWNp-xXg-Ali6SXqmOeQka0Ck0TL52KdT8PJeyQ1v76WbQe1S3fwnRvUpoZ70BmXKU_hN1Vo09MLDr2XmHuhNZwGANgCOpSJ4-qKGtaMAR0nAC_bw5oqY7uTOccXVDnOqH3C-xtRD6krVj68JkmjJFih4JDdl6E4MYcre0t41LTs8aK_MH3mGm0VysCEmA_TBuEeqWtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
مسابقات اسکیت سرعت آماتور
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461035" target="_blank">📅 06:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-NtQmTdLbla9LF5zANoo_hGiU0CDvyYLMHgaS7wFWbFwIrT-vMTqShfK-TBpso8ch-ve6X7OSVdPjjromhQ3Ej6embL66wOkgbfl0nbjlmNJw6GUWbGvmXbqwALcy6dGlmDoVnzxNk44H3BvClefLp2tmNXRCckozwSkO7CoS7SWIQ01VIe5TO5Ge6g9g81ITewSvWcinHiZuIjrW_hwmRwnTsVlFp44Dm787CzmF91qIPNF75SYjrnQgmw2HgAsM8NDJGBkDjqmOOJenZH1Nw_4VKk8ZztjW7knF2V-ajpwtj7RFhpdDr3irvIz8WWUxuYRNzNCjDK1lGldJmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استخراج اورانیوم از آب دریا سریع‌تر می‌شود
🔹
پژوهشگران چینی ماده‌ای متخلخل به نام «فوس‌کیج» ساخته‌اند که در آزمایش با نمونه‌های واقعی آب دریا توانسته تا ۵۰.۴ میلی‌گرم اورانیوم به ازای هر گرم جاذب جذب کند.
🔹
این میزان حدود ۸.۴ برابر معیار تعیین‌شده توسط وزارت انرژی آمریکا است. پژوهشگران می‌گویند ماده در شرایط آزمایشگاهی تنها حدود پنج دقیقه برای رسیدن به تعادل جذب نیاز داشته است.
🔹
غلظت اورانیوم در آب دریا بسیار پایین است و وجود یون‌های دیگر، رشد میکروارگانیسم‌ها و دشواری جمع‌آوری جاذب از محیط دریا همچنان چالش‌های مهمی محسوب می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/461034" target="_blank">📅 06:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643cb9a38f.mp4?token=GedYedAR96msWwYaxXw4qLTVRi5qpq0-803fmk-FO5CSwohwclycjJKLXZPQrBKyE_H4qdVOr1vTQbEyA_1tpLD6GpLK1kTOUODRSdEkL7bzhbbkW5KnLk_FVOr27asp04kKZwPqN7WJ-Efpazy1lz84FXY6pn4-gg4EEl0SAk9sQp-8Yx0xn1J-X_J-vB-JjVqm8EPC7djE1BFdqppzCfxZ7NVmd0m7JfOvQyEij9Ubk28ERG-S4yez9j-kXjbMsS1agkQ5yN3iJelmTUcPXaDVS_erbwtFdTF7fso6vsrOeM4AysVN9KoJrrRb6GFrJWLCKMFH8rl6Ij3rWhU0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643cb9a38f.mp4?token=GedYedAR96msWwYaxXw4qLTVRi5qpq0-803fmk-FO5CSwohwclycjJKLXZPQrBKyE_H4qdVOr1vTQbEyA_1tpLD6GpLK1kTOUODRSdEkL7bzhbbkW5KnLk_FVOr27asp04kKZwPqN7WJ-Efpazy1lz84FXY6pn4-gg4EEl0SAk9sQp-8Yx0xn1J-X_J-vB-JjVqm8EPC7djE1BFdqppzCfxZ7NVmd0m7JfOvQyEij9Ubk28ERG-S4yez9j-kXjbMsS1agkQ5yN3iJelmTUcPXaDVS_erbwtFdTF7fso6vsrOeM4AysVN9KoJrrRb6GFrJWLCKMFH8rl6Ij3rWhU0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: ۲ شناور آمریکایی، ۸ نفتکش و ۱۰ کشتی متخلف هدف قرار گرفتند
🔹
روابط‌عمومی سپاه: نیروی دریایی قهرمان سپاه در پاسخ به تجاوز و شرارت ارتش تروریست آمریکا در حمله به ۵ نفتکش ایرانی در خلیج همیشه فارس، تعداد ۲ فروند شناور آمریکایی و تعداد ۸ نفتکش را در این منطقه مورد هدف قرار داد و خسارت‌های زیادی به آنها وارد کرد.
🔹
همچنین تعداد ۱۰ فروند کشتی متخلف که با تحریک و حمایت ارتش تروریستی متجاوز آمریکا قصد عبور از منطقۀ ممنوعه و ناایمن تنگۀ هرمز را داشتند، مورد هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/461033" target="_blank">📅 05:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21aa83f910.mp4?token=ndrQzURGFrR91qz2azrMSlnF9oWE5CQrAPr-jvSvs1IH6w0JVjtu874rNH_y_XdvsnumHr0hxaw66zuQAQUdycym1py1TXyDN0lMxUr6I_4KD1pi9JMcxn_JdE2oQGUHiT9zJOpryk70M1xs5lyvcQsvip3RXRUN3IrBmxv_ihVGe-kU3fzGHM44xh63kKOyjfPPTDoGjPd240p9ArsDmvoLjpPLdDgNLAPSoh1uZNEu2W7oEl1BskxOSbHshasH-JiBNigBw_iBBCDFs7qyRp-QbImgdX_H1Dg_jqMiCtgpBko9b5HnZFMEnEL2k6Sa-Ds_9sfcf7RXthOUR-20Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21aa83f910.mp4?token=ndrQzURGFrR91qz2azrMSlnF9oWE5CQrAPr-jvSvs1IH6w0JVjtu874rNH_y_XdvsnumHr0hxaw66zuQAQUdycym1py1TXyDN0lMxUr6I_4KD1pi9JMcxn_JdE2oQGUHiT9zJOpryk70M1xs5lyvcQsvip3RXRUN3IrBmxv_ihVGe-kU3fzGHM44xh63kKOyjfPPTDoGjPd240p9ArsDmvoLjpPLdDgNLAPSoh1uZNEu2W7oEl1BskxOSbHshasH-JiBNigBw_iBBCDFs7qyRp-QbImgdX_H1Dg_jqMiCtgpBko9b5HnZFMEnEL2k6Sa-Ds_9sfcf7RXthOUR-20Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار تصاویری از اصابت موشک‌های ایرانی به پالایشگاه «حیفا»
🔹
ارتش رژیم صهیونیستی بامداد چهارشنبه اجازه داد بعد از نزدیک به ۱۴ ماه، تصاویر اصابت دو موشک بالستیک ایرانی به پالایشگاه حیفا در تاریخ ۱۶ ژوئن ۲۰۲۵، در جریان جنگ ۱۲ روزه، منتشر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/461032" target="_blank">📅 05:20 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
