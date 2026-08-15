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
<img src="https://cdn4.telesco.pe/file/LXXJysPkfnr6ohUwwySTf_PLF1oj5fiy1NAp47WWeQrAWGddwEtwj3eNK5YwIALbs7BoLCSmD1bJmTPfxI42DsY_satgGzeZdVmBikov0lglnS2KyWOhsNScdJhTzhROVqcjuluSloIvWe_CyNrqTsxx3GL2hbA7GC3sXTZmu19eD8pP4ii5VTyLbo2FgzAaWVSCnX03CbuO607R14eWaBVCBxNy0aFFbQJ_UC097_t7zX-5tLnm_g62CqAo_J_3JtdOeDBqyQLMMIBtk167HLBHfe3BAs2jAV8oAGNLP6tDDStik_H1RtujevZxAwFCMw0kIO0ZKgeMWaJJhHnzGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 964K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 21:12:19</div>
<hr>

<div class="tg-post" id="msg-141889">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eoyr4n37iOlNvUZq6TXtBbxZiQcKvLbnpbi_xzeG5mgYQNzVv85M6fOk7Fc4l8X3xdDPpWgBrJS4quccU6q7P6MyBj_xEOkJRmAAzhxcOYcjuQ_RCykPq7gkvC-vTOunhyp2pOQqWOQyGuNaaUoBGXKojXWHMZNmDAVYso7bdQZbeBeDV9H2BVAZYXdF2_xmPao_QQHC8MvHj4gp-T_BoKrAjBunz95V8AzNdHlu-06tYC-blbgZMo3prQ52EbpTdh3dHyt5V0Cd_rI8FaUBdycnF-P4x0KnJdfgUH2WAUXqjiLI1GO5cfmv8pDeQV68cbYgm9BN_15R3xLpJj5QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ساعات اخیر انصارالله یمن حملاتی به دو پایگاه نظامی صحن الجن و تداوین در استان مارب انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/141889" target="_blank">📅 21:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141888">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd309</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/141888" target="_blank">📅 21:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPt3O48LMG2-u5-iKjyU1C995miQCGVc_lHlkJ4QuxnxAwFK0Hbaqo5n2HNLw9Jdd0cHcIZVZjDwxyk0tRoUbjqgAbXwEq32k1eWLQbg07TtSb2D7miMyOlSnQilrqBwuQITAiXDxIFQgEhf_S6ivI9UaWH1xUyEo4MfrHyWL2Erv9Nhr6lvw8-jZq0A5nfD0tuCrY0yR2c5HQ0kHip-ObichFnON_yXAllo0QQqxKyQwpP62k5oUsGtDj88py7e4HxD8IdaG1sI5w53P4YuIm2zIHH390njByzvnYhzN8M_gVIFpCBIZx94o69PTLIKGPxqoLjgaFXOUhBaP4wBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اندی بیکر، مشاور ارشد امنیت ملی کاخ سفید و از افراد نزدیک به ونس از سمت خود کنار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/alonews/141887" target="_blank">📅 21:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
آتشبار توپخانه اسرائیل به شهر عیترون در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/141886" target="_blank">📅 21:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I40bByWKOF2fdlMkOXtX56jpvDa6T7tntzr5HUtX6F4o1uWLpZnY5ONPJG5RYv_D8L6DbomjwCoqQDqyL4weOKIcwbLidShB5xVCuG_68JLRW3Gh2ZVv_bAQfo8bY15T57jo_STsWNrIJida9ZTCH_-9KeNQ7zPZoFboWU4VmbARGe8UEpFt0DC8kmws9JeRCCrub_ghcqcZJutY0jPDsEXML2Iv7GwHWiiBvLPN1ra2XgcLkhXOPAOene7U2GyOpllO41XbFLaiQHGGiP0bXvFH9F9pwh1ZZYpRRmBM9_5QIIWdrSNZfDohwFAebSaTxPAndV1SwtkEvbCoonWfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجاری در طلوسه، جنوب لبنان، به دنبال فعالیت‌های تخریبی اسرائیل مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/141885" target="_blank">📅 20:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی 6 درجه در مقیاس ریشتر جزیره «میناهاسا» در اندونزی را لرزاند. این سومین زلزله بزرگ است که ظرف 24 ساعت گذشته در این کشور رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/141884" target="_blank">📅 20:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS7qvOWA5y9gslBzDyf-XK7ZQy_IRBcnH6ZDHBD5GbL_bzU5Njp5Kngb0gpH3iTQXL2ul1Xpf_9U9diHBq-Ttbh2eH5WOHgAWqAaKTtvLR-7WfY3JgsBRyxxFgSyV6In7frVHpB6AHejfoFSNjcR0uIaZuJRwBTE-AzmThVBPjkkbhtAPPovPJJUGbvyCdhbjoG5zlfBBO23T5h7LWA2lAaNd-B4nU__YcQNGRSA61V1mxUxSma1j2gH5QJHBgCMFHVVTitVnIC506NYa88Ke4mOixRHN70KJNLnrrvaGXVaYL-wxsjIkeX7M3B7p-SZI3VB4oypTBu9hvQERl5zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورنیوز: ۲۶ خرداد، تفاهم تهران و واشنگتن شکل گرفت؛ ۲۷ خرداد، در منامه مقاماتی از آمریکا، اسرائیل و امارات دور یک میز نشستند
‏
🔴
موضوع فقط تنگه هرمز نبود؛ مسئله، جلوگیری از تثبیت تفاهم بود.چراغ «اتاق تخریب» درست یک روز پس از «میز تفاهم» روشن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/141883" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txT31zW3PMDX5b3S-4sF3hDryXa0bNBQo4uGlyX-zRHMKtiZBRczSsoyTD3kQfsJ7g6MSEBF0jOawcq9R6EmKh-M_BmIBpvjrsleArh2sx5UiPF8IYJuEqK951FVon4DFpKRm2q_nNj_iK-wPHQWjEM-f2UxMS7jCpM01HR1yhyqYn1S685aInCfyQ1YdVo3UgWaJARX8aBuN2DARRCC8wLayv93uLmTQzTaUSgs57vwwKPFXXH3hALrPFjxBT4kB1PzG9OCtk2CGoyqBcdnFTCuDa1AeAliFyvShRYnZf1TIsvbk2LlH22wuPqHmJdHQSdOrKdZXhhIMfxKcImmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماس اعلام کرد دفاتر خود را از قطر به ترکیه منتقل می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/141882" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9091137d97.mp4?token=uy32GdfhMJjeszCzwN0JbXTKNJHEB9j6SCkAXCUjvDU2C_abbwUk9U-tAdIQEvOt4S_REWa2kzLzgMeJyl6vtPwFKHwHaT_Or-d8gx1SIEGP3RJshU5PBZx-Vwid04jVRwD35vHRMr85FVYnk2DDlbQPPsTIRxwdT1koFZ7RlTsVDSZduQtJNr1ho-6H3B9AxY9LTB3P4ZYs2xzQxl36F3xI-ZkJaGiVlxl3btHctkf0VC_ltzMpdsjMQtA3hGJp6eitgvHLIKBPbZCtqoELySpqPnsVckplz40YWhmsdgnV2boe_KtG5jGyfHGCNV1l0DUQmPVOL5n1blnoVejXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9091137d97.mp4?token=uy32GdfhMJjeszCzwN0JbXTKNJHEB9j6SCkAXCUjvDU2C_abbwUk9U-tAdIQEvOt4S_REWa2kzLzgMeJyl6vtPwFKHwHaT_Or-d8gx1SIEGP3RJshU5PBZx-Vwid04jVRwD35vHRMr85FVYnk2DDlbQPPsTIRxwdT1koFZ7RlTsVDSZduQtJNr1ho-6H3B9AxY9LTB3P4ZYs2xzQxl36F3xI-ZkJaGiVlxl3btHctkf0VC_ltzMpdsjMQtA3hGJp6eitgvHLIKBPbZCtqoELySpqPnsVckplz40YWhmsdgnV2boe_KtG5jGyfHGCNV1l0DUQmPVOL5n1blnoVejXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمین جالب FPV روس علیه نیروهای اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/141881" target="_blank">📅 20:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141880">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نیویورک‌تایمز: اروپا که نگران است ترامپ بدون حضور کشورهای عضو این اتحادیه درباره جنگ اوکراین مذاکره کند، در تلاش است تا جایگاهی را پای میز مذاکرات کسب کند
🔴
فرانسه، آلمان و بریتانیا در حال تدوین موضعی مشترک هستند و انتظار می‌رود که کشورهای دیگری نیز در این روند مشارکت داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/141880" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-vD86uJR_YaJVVqrh6Eor2l2JrpijxLLOiQEeDebFOsNhh2H_pAYaDIcWmICjviNPuLus1f1wT3ga6I9c_SlKy4ugR84OzYcrot-bATvx2nHZ3oxn-2_FDrY_NbBC44H2dD55ogGKVhUqV9X7gyYPSCJI-Fa48xPO2BPC-TtJR3ZMgR64YN0kAf57AbTBuAz7J9Z_0xqVMNhMDJAKLug1HYc_SwHQV_nSvPKp2hGGS0mOmUdMKlXbmzlH4_iqQvZtt35kyzeGrGRH5OnDAXK6fklrT1x-vTke5UKX8F7R7MGwBJzYWgJ_jvxKjMuevGE8UEtICOF_mPZ0tk_T19mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
نیروهای نیابتی حکومت ایران شرارت محض هستند. حزب الله کودکان را جمع آوری می کند و به مناطق نظامی می فرستد. آنها نظامیان اسرائیل را می کشمد با اینکه می دانند این کار ها بی پاسخ نمی ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141879" target="_blank">📅 20:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141878">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJJ2e6bwbb5_2bdBAOs9PJxdQTJp8Ns3wMtTKtJP9Dn2taY38j0IJPb0SUmn1UJdP9hfdBxLnpJ2nsavSFxOwX1RrG40IPeaqmmdWL1PZos2QBe-rPT-weeU2_s0OYVUl7GmT2L-AUYzP08m-PhZdG32tpQXo9z9Ui0JuDe1SCteFs_ozGifzMjIyIFgZ0Ku5Ba18AdGr04mPDz5pXrDDrhJJl8qyRYtoh6kaZ1w_-1Vo3ej2hF6coOexXalWmWx5JYcxiSD88J-MUM50vXATWWBPzEl2N4pDocWTxFyhTzEjt2FcI85c5m1tqmIcwLe_vSb9Ntxh0hycFYI8UoMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی جدید شبکه CNN: محبوبیت ممدانی در شهر نیویورک در ۲ ماه اخیر ۱۱ درصد افزایش داشته و به ۶۹ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141878" target="_blank">📅 20:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141877">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: بر اساس اکثریت قریب به اتفاق نظرسنجی‌های فعلی، نتانیاهو در این انتخابات پیروز نخواهد شد، و آقای ترامپ و مشاورانش از این موضوع آگاه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141877" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سوپر اپلیکیشن "بله" از پلتفرم های ایرانی بازار و مایکت و... حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141876" target="_blank">📅 20:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبر عجیبی که دقایقی قبل اومد
😐
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0
دلار و طلا میریزه
⁉️</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141875" target="_blank">📅 20:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141874">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7k3DY2SSDE9bVz2ppjYefy3CkEtCAZJghaDtX7VgkkgYGVZOZmzqm1_8lcCCUkAIUyonhng9QCE_Hs9yAHdCq3VJGLQwO-7R_IpZJqt4gExYWokAcsYidr8nYn1Hfp9vwK-bJBzT-6HBNwlaDDgYxencB7kaX7WIZT5bYTs85EDg9gt39IAskW4V_VGIcuCOvm6QAvIgcAdKkhXlmNQbIaU5L5K6aPb3TaIMRk-QyW5EKWKHV18zZKYasF-POnrBBwsk0wLyFPr3bxonEjVpNOaMvMtW9XAfOJ_4fOJOx31M7A65XgOfqtzFe9nO-b5EG5hfc6mgC_HGLcFp15Kpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری تابناک، سال ۱۳۸۷: خیز دلار برای گذر از ۱۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/141874" target="_blank">📅 20:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وال استریت ژورنال: کاخ سفید در هفته‌های اخیر بیش از پیش نسبت به دستیابی به یک توافق نهایی هسته‌ای با تهران بدبین شده
🔴
دستیاران ترامپ با ارائه داده‌های خسارات تحریم‌ها، او را مجاب به تشدید فشار اقتصادی به جای جنگ کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/141873" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141872">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuYFUPTFISadT7MG_99X2sseMIBDaJQwebp5pP6A82X2baZk_8nLfih422sk9DVzVwK-F0QhybmZi4EhA-2C77i27U_2PVOXi_llTUeyfl080hc9mySyweXHegB3aevbYd6JPb8woZJtSmySXgVUiEiyFc1Z5MOqRbM5IO7OSmz8MeMdsenFhhSSlQlTvloc0OKIJI4Arjn1w9DbPB8tEG2Y1XICkJxaiA4NnXULx4oCB8tqbbN60a7ZgDnYWxLV5vJQh1uulxtTJcGi9N3wBGg8GjDbSFectTxr53_Wgq20P30G5aBVfOX_su3yN4W6j7PqmOi5q6oKr1OaXkAY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم!
🔴
‏دونالد ترامپ درباره تصویری از خود و رهبر کره شمالی نوشت: با وجود نگاه غیردوستانه در این عکس خاص، عکس‌های زیادی هست که در آنها لبخند می‌زنیم؛ من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141872" target="_blank">📅 19:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okBkzBDNN-JsajLPk3sBBR_bHxZV49mG-owWy7J8lGLIykQVMwD8LnlCMvOVSXGNLEGwiTFgR_a4eSMjrt5_DP0TZJdA8qLrjz59Wf6gUChHXUWhpxMdZawIIwkjUXmdlbo0tajkRPq7Ao1PGNWsOc3kRvCaMtYr3laHdU6PQGRbNIWCKyN39m9eRNP6p_nbuL8nDeNg5S7O-cK9o9ctAq7z9HmoZl-TmkkSYO2VeyiLfC3rVwycw-NSkDiog9iiZdhndYgsY2LOvwLaITh08QYXIoZeia6DU0KP566f5GzfcOQsznw9sK2M8PWsW1LoNXUVrbpCDx1BeE2Hnou7UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله لبنان در بیانیه‌ای اعلام کرد پاسخ حملات سنگین اسرائیل به جنوب لبنان را خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141871" target="_blank">📅 19:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136da7e3a1.mp4?token=hHX4p2vnKwhnScbRRWnUNaboxS_7oUbbh_QIxzW2UDp8B5Kd3vJ6huHmj8lEUO3CEiya0b9la7X2Ngq_Epets6pQWlH1LfPtsqdmPx3U-b9Tso-_uiR_QEf6Sb5Ox0FZ76h5CdDChM1w3Ee3fv0qQtHheSXbH3lA0gmpx2AccQyg27fcZve6_6VN4vpgm0I_QNe3X-ub1YWHgdEICTV9epLIQYecB6ZGpgqtvCe-iqgz6WISajNHASWyGSjBSgC3_7QIHaU6xMY2MFj3M7XPc7Q8r-6-fkQCTtEcyMRrvtE2Jd5j03bkrK5KFB5ofx_Ge9qIjjyg8TxGgijm2JCMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136da7e3a1.mp4?token=hHX4p2vnKwhnScbRRWnUNaboxS_7oUbbh_QIxzW2UDp8B5Kd3vJ6huHmj8lEUO3CEiya0b9la7X2Ngq_Epets6pQWlH1LfPtsqdmPx3U-b9Tso-_uiR_QEf6Sb5Ox0FZ76h5CdDChM1w3Ee3fv0qQtHheSXbH3lA0gmpx2AccQyg27fcZve6_6VN4vpgm0I_QNe3X-ub1YWHgdEICTV9epLIQYecB6ZGpgqtvCe-iqgz6WISajNHASWyGSjBSgC3_7QIHaU6xMY2MFj3M7XPc7Q8r-6-fkQCTtEcyMRrvtE2Jd5j03bkrK5KFB5ofx_Ge9qIjjyg8TxGgijm2JCMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سربازان گردان موتورزرهی 64، که بخشی از گروه نیروهای "وُستوک" هستند، به شناسایی و هدف قرار دادن نیروهای اوکراینی در منطقه زاپوریژیا ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141870" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141869">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
شجاع خلیل‌زاده: گل من به مصر درست بود؛ شاید ترامپ گل را دستکاری کرده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141869" target="_blank">📅 19:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141868">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سازمان تبلیغات اسلامی: تجمعات تا هر موقع رهبر بخواد ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141868" target="_blank">📅 19:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141867">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی نیوز، دونالد ترامپ نگرانی خانواده‌های نظامیان درباره شرایط دشوار زندگی و خدمت در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» را رد کرد.
🔴
مأموریت این ناو در خاورمیانه به دلیل جنگ با ایران بیش از زمان برنامه‌ریزی‌شده ادامه یافته و همین موضوع نگرانی‌هایی درباره وضعیت خدمه و فشار عملیاتی واردشده بر آنان ایجاد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141867" target="_blank">📅 18:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141866">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkHQaR2iIPwLXz4aB5sYrKzJyFgckeizZeRg3NIYDb7_KA1euHQ1_nZigdLNdz-QcX0kdjHTBDRqtz34Z2UTDquSs_T4g6TKBXLt3fDR64ZfJNI8XDoJW5SUw8qf1TIBirdweLaIb90LBBpe3v51ZKZ6yJw7QAb9gGj4OyUwK0E8hEVdMFykeUvTW0hW7qP2HxlxljnCNSnNozx8fMPfMKe2zfoplCiuzeywRqcw-BU61nrJ-YjoSw6afCRfJ0890ylDYd24KfYb6x7BHw9OOf8qz-ArPCFCh1L-dp4S5USPcRV-w9v6YVYlx3NsTdPGOBcsxzUlgntvo3Cy2l0QmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل از ترور حاج علی سمیر حاج حسن، یکی از مسئولان نیروهای رضوان، در حمله به انصار جنوب لبنان خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141866" target="_blank">📅 18:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141865">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e77374a26.mp4?token=OgrTlYcHEzziZUp7EYcXc38nmpSRtmiyrZuKkyBV4IyTGYurKLcgQ-GikrEn6Xvy2plxRtqjR6wEa-5TV0gHqs64iO6A-vb6yubi1adirnxTWcCz4M3RXUnO3DQ4psla-hJI3Noh3rZ7dj9oAWHvU2mtOFk4Y_XmYam9cAautIWARlvUl-EcBM5ew74Nji87gbN7798JA3htmISKgurqueTaMs5NVindpCD3jT4hqzeMwZ1QLPW1QhSD7A6wj0xo2oyppSwvX0wSPAAmQN9JHbAggvPbWmpNsQzlQ63bIlRM5X_eg6FcaO768J_O5VOChIpTdNFX1vyjGbz2f_lumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e77374a26.mp4?token=OgrTlYcHEzziZUp7EYcXc38nmpSRtmiyrZuKkyBV4IyTGYurKLcgQ-GikrEn6Xvy2plxRtqjR6wEa-5TV0gHqs64iO6A-vb6yubi1adirnxTWcCz4M3RXUnO3DQ4psla-hJI3Noh3rZ7dj9oAWHvU2mtOFk4Y_XmYam9cAautIWARlvUl-EcBM5ew74Nji87gbN7798JA3htmISKgurqueTaMs5NVindpCD3jT4hqzeMwZ1QLPW1QhSD7A6wj0xo2oyppSwvX0wSPAAmQN9JHbAggvPbWmpNsQzlQ63bIlRM5X_eg6FcaO768J_O5VOChIpTdNFX1vyjGbz2f_lumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گوشه‌ای از جشن استقلال پاکستانی ها که دیشب گرفتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141865" target="_blank">📅 18:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141864">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه : ترکیه نمی‌تونه غزه رو تنها بذاره و هر کاری که لازم باشه برای حمایت از مردم غزه انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141864" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141863">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8AqIMPfdkVbDPvNYGlE8KyKrJXPooc0sXbwMcswUbOkjulDfukZlfnPYXI5cpOsqfr7sfF4hDrefisZGQcfrBR_-Tr2ro33Sz9ZxmfRANkeGtQ5iqqXs92l9GJVrEw3TBFHIPgpAjIUtKRGMrEJ_Wy2-k-8uHvWtoxcGLxPqrxdvga-GI4061KpozvmZW7UTiioft8JZ9Hd7XJeoyku2f8f-CyK8W9EeuvrI24y3jiwtIaJEyfCTaITpRVYqoflXtkjOp_lsBmmQNSAsGScjaxJfG7SdLcawrGtocO3hAePospF0Xd-dNnnqMe5GNfVGpFMtqlGMKkxkITJE9cN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیاتی از وزرای تاجیکستانی با عراقچی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141863" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141862">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رئیس جمهور ترکیه : در آینده نزدیک به سوریه سفر می‌کنم
🔴
سوریه رو تنها نمی‌ذاریم و برای حمایت از ثبات این کشور هر کاری از دستمون بربیاد انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141862" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141861">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رئیس جمهور ترکیه : در آینده نزدیک به سوریه سفر می‌کنم
🔴
سوریه رو تنها نمی‌ذاریم و برای حمایت از ثبات این کشور هر کاری از دستمون بربیاد انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141861" target="_blank">📅 18:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oespFjSlW5cxlGNlB5FE1_AX5dTnOi8OPMrN8Ei3I86KEAng861byBgAFdb8PJhtb1MDNYWga_q96hTnpVMDZDuNWSluS3a08mfySbSg_yDmSYlLR-SkNg2NK22MgTnv1wdJjrqaLLK2_4uODxf88Vxi3j7mocwpPVfvMgcbPKar7lFP2KT71FwbC89GyrhalCSf4FLByQNPflQztDiZIn_bScqB7NRU2GqaiIEcgN6kzzuEV2p6kNIXQ01x6QupR-cok6PbuGo0w2-D4f8hu3HCZoK7-qIXtprvmwA7P4NDM6tJGrkI_0EIDmAvxFply_ChC6g0ejUVrV_RCclbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش احدیان، دستیار قالیباف، به تأیید تفاهم‌نامه از سوی شیخ نعیم قاسم؛ خطاب به تندروها: بیدار می‌شوید یا خودتان را به خواب زده‌اید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141860" target="_blank">📅 18:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141859">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر انرژی ترکیه: شرکت های تکنولوژی سعودی قرار است در ترکیه نیروگاه های انرژی بادی و خورشیدی بسازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141859" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141858">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx2n-Z7iJ-MRp9FvI7Pmis3sSzp3CpAMJXiXpmDLdTjJ7cYPU1ATJHtu8bKxfl6MInRK0zqlnqvWjidZ2_vAmsQUGOeiD5gs48tW_5am8A51_0LjrzN-ScyyepOsGIKlZlpUC2IlcpeLK0NxsCrMbvyL3CXJPI7n4senp4zD4fW7B1qBKc6du6rwir9FlnBygLV6JNY9cFT2uA3YuKKMKCUdqXAb_6PnkfNxF_lNaPRlX1k3IHs0YvM07LMj6lwAJshzKQ3QVBvN0FMNpjysCIuMWC5izmp1mEhH5Ccnh4Y53GFIM8vuYwZPtx3rLiJX2e-yMHFa55mabEPasHk28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر انرژی ترکیه: شرکت های تکنولوژی سعودی قرار است در ترکیه نیروگاه های انرژی بادی و خورشیدی بسازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141858" target="_blank">📅 18:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141857">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
واشنگتن پست: مقامات می‌گویند ناامیدی از ترامپ در میان متحدان ایالات متحده در خلیج فارس رو به افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141857" target="_blank">📅 18:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141856">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOmt3Yivoyi8nGwDzfrR95pLMCB4kg8KVYmMMFQN9z9nYNkxs18JbujHfRNjXj4syuGY6cCa1hBxprVdhfvYwbEK79vvbw7ksh0huCbe_QIMOWt7zEdNjzkSQfldCP40EhBcgxhVtkodw3I3gg6XIHoAf4HSXo1r9BVzJOak6x1JcBaEO5P0ZmS3-7kfEWmxt2qjKHszrH8nSaxIaFBbfqYRSGyzLQZM-kUZvPftBQG9Hos0DwOUy8C-cVJ60uXZdR59ugaruW1a1OFAXgoF9k4-lYf-P9zj6Snadueiy1X3kEl5Q-t4WsRR2yUXIMy062RDa2ZdZD2KWDheLmu0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141856" target="_blank">📅 18:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141855">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
زود بیایید اینجا خبر خیلی مهم
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141855" target="_blank">📅 18:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کارشناس صدا و سیما:
70درصد مردم تو تجمعات شبانه شرکت داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141854" target="_blank">📅 17:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOoXhswhJjZ2zL3-5Tis4927vQK6uuSboKzR60q2qTnaDYXURxyz62IyJxeLfk5uGdgQoPcO4z90L0qWUy1ft_5mTc0jyi4WT4URFtfKxcTSnBxK7-ruHqxRgPJ4oVi7gAsWzAIaDEyd3Mb4a5bxYA_VqGNdJBc9bg4_iMUbLS3WflhfUiQOqSALCiVgXdp2-NwcDrnxvyQIKlCzBcK5D6dleZ-z4VkbMwih_d0UtEc85YVDLHeZFI2FANJs1X1J3VYVyza9etdkxYeKzbYoynp9J6vVNIhmhl4ObAs_zLk205B4LgqgisJ1FY5ld0XcCRUstaJNvBsCzz49hH1ZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: هیچ توافق خوب و قابل‌قبولی با ایران نمی‌توان منعقد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141853" target="_blank">📅 17:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=hUMEQsK5lEYrxwLAxyDGOnxqUm1LoChN444HmL8RorDBmxRIAf-Ss1tdP7nPIR4hYuVMG8klrZ6FgP_2m3xHfRixuiFS8_2pscK9F2EnkOu3sZjYNvK6jJFiK01CdTWM8g2K3-26PcfgfdiASTDqf1fXfDAc7l8ZwLVUk76aPyxtaj1PUTmulPXaqIeXz5Dv97E5AsJE3doJrGxzvg7ti0JPmuxmDqFxvJ6JCUFue26YSSEvMUUn07eM16z4Ezro6U1D2rPzWtkng5mc1zRNZI0ixDnJR40HXQIFN0IXCTTexDWKnBj958AR1MMuDWMtgcUF01sGgH49r_Alm0rKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=hUMEQsK5lEYrxwLAxyDGOnxqUm1LoChN444HmL8RorDBmxRIAf-Ss1tdP7nPIR4hYuVMG8klrZ6FgP_2m3xHfRixuiFS8_2pscK9F2EnkOu3sZjYNvK6jJFiK01CdTWM8g2K3-26PcfgfdiASTDqf1fXfDAc7l8ZwLVUk76aPyxtaj1PUTmulPXaqIeXz5Dv97E5AsJE3doJrGxzvg7ti0JPmuxmDqFxvJ6JCUFue26YSSEvMUUn07eM16z4Ezro6U1D2rPzWtkng5mc1zRNZI0ixDnJR40HXQIFN0IXCTTexDWKnBj958AR1MMuDWMtgcUF01sGgH49r_Alm0rKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حمله نیروهای انصارالله به نیروهای وابسته به عربستان تو بندر المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141852" target="_blank">📅 17:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894cf0030.mp4?token=dgqKIIW-v_MnWuI3zwxCtYt-nB2BwJEEWJB_3yIuKJ8-ZRng13VyrleNyd2O7qsd4JSB9InMtNVSuk74-HhBs-8k0ra_01qonFhkgFsQYNrZ7_m7IYvUmAjhqVwZVLx3-srDnX5c6AxkEUomvmVmQIYCbifMp9n_7L_w62jfLl7WZzIF2DfwJCuBh61VUq1__rA54XFnzfkO7FSbl1cZovwT0tjx_rRAp9wT9ChhanluI2fbjMr0oDThVdww_db6tRgPR6ZsoYecQwrTDDnmhNXtntgAbxWew-p60wiYc1EOj1E6hUwUvig3h1F_sby3yTH5VAzPgAP97I0XKOu1jmEWB5iyUPQDhv2LD0Z2Gvtys0aElaxFMGCs_mDwUfrvkpkTEVINQxtoEQb4uCyq-v3mdSmN_cHtSwJkFf0yiQwyQ2d6j1jK4CKDtLc-r_ITLiQybYI0Qvy9mrXYTLZNO8-wjdTY16H0ONwsTjZRcfZan3_PaNgxm0qbu2fWK0czpkM2sTgHe2UpeykcPLtZ8ZGOesjc8QPfqEkTikxPEwF-1AMKLV7aaWyc90KUlBhGjyDRbeHuuW5p-Nwg1s96VpxtYqFtsXCICIVl1mEc12_l_8UEvaQdcpprTvn_7Ei4Z0h-JiHK_4-iTJTX6OX-UphwiOPzKSKV5bkz9kpBppI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894cf0030.mp4?token=dgqKIIW-v_MnWuI3zwxCtYt-nB2BwJEEWJB_3yIuKJ8-ZRng13VyrleNyd2O7qsd4JSB9InMtNVSuk74-HhBs-8k0ra_01qonFhkgFsQYNrZ7_m7IYvUmAjhqVwZVLx3-srDnX5c6AxkEUomvmVmQIYCbifMp9n_7L_w62jfLl7WZzIF2DfwJCuBh61VUq1__rA54XFnzfkO7FSbl1cZovwT0tjx_rRAp9wT9ChhanluI2fbjMr0oDThVdww_db6tRgPR6ZsoYecQwrTDDnmhNXtntgAbxWew-p60wiYc1EOj1E6hUwUvig3h1F_sby3yTH5VAzPgAP97I0XKOu1jmEWB5iyUPQDhv2LD0Z2Gvtys0aElaxFMGCs_mDwUfrvkpkTEVINQxtoEQb4uCyq-v3mdSmN_cHtSwJkFf0yiQwyQ2d6j1jK4CKDtLc-r_ITLiQybYI0Qvy9mrXYTLZNO8-wjdTY16H0ONwsTjZRcfZan3_PaNgxm0qbu2fWK0czpkM2sTgHe2UpeykcPLtZ8ZGOesjc8QPfqEkTikxPEwF-1AMKLV7aaWyc90KUlBhGjyDRbeHuuW5p-Nwg1s96VpxtYqFtsXCICIVl1mEc12_l_8UEvaQdcpprTvn_7Ei4Z0h-JiHK_4-iTJTX6OX-UphwiOPzKSKV5bkz9kpBppI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، اعلام کرد که ایران و عمان به توافقی در مورد طرح ترانزیت دریایی در تنگه هرمز رسیده‌اند. این توافق پس از پیشرفت‌های مثبت در مذاکرات صورت گرفته است، «با وجود موانع ایجاد شده توسط ایالات متحده».
🔴
بقایی افزود که این توافق حاصل تلاش‌های هماهنگ بین‌سازمانی به رهبری وزارت امور خارجه ایران، با مشارکت مقامات دفاعی، امنیتی و محیط زیستی کشور بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141851" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRN9tVxncLf7x0mNQGNkbyZc_w10IhqtBi1FZ09bqmBs8k6EBpd6osjcJgF_sDg7eSiIYMKO5PfZQartIaXmNZWA0MhQGpTeQzeGJH6NHRpQhwY5brDkyOSWtV528DMttM2DfQNaX-SbeTrentItPMTHSsiscspzZcdlEIfQ-jJg2HezaZkwR0YZp3NP6F38A3fsTXrLlnAN57C6Izb6uPhR5fho9FnQfPYNbetKp4nZH-IbPmOl_paZjganTEF5C7OAv4wNzhJM39tWLnQWGboZcBD2L9SGYhC-7pNGhaQMb8fXWv3y3KqHHy9Pg7y-jE_T6oI5rJA7Lfu8kw3c_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل دو حمله هوایی به لبنان انجام داد و ۹ نفر کُشته، و زخمی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141850" target="_blank">📅 17:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ژنرال کین، رئیس ستاد ارتش آمریکا :رژیم ایران یک ساختار ایدئولوژیک است و اکنون خود را پیروز جنگ می‌داند؛ جز قدرت نظامی، هیچ ترکیب جدیدی از تحریم و فشار اقتصادی، تنگه هرمز را به وضعیت عادی برنمی‌گرداند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141849" target="_blank">📅 16:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skn4QOWBX87GEws-Sp8N-A2jvglTPGheaZTTqn53ZzN461o1v58mTyQyCqK2dU42v9XX341AiIJJE2vzXN82oRTjQ8zJaUYN98ResQHCu3121zxmxlfhmQWaVTiPvQo7LaGeEI2BN7xTEGS3ZpZNNCwv1FQh3Lcc6dPTl2qVQNA9qJa7aOe0lvdfVDMlOzD96AzONpta9IJfCFO0p-7GCfi5saKOpGEvvxcdcJ2YFAYMVDgdtZfWy6tzSw-wquvMp-e1WqBkrjXsz5w6-1TS-qWPB-BsYOtfg-hYLvF1buh9KrOHztCy-Crel0aFECSp3rM-aTNOMpkhRVnXsnzNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات توافق میلیاردی رونالدو و جورجینا برای روز جدایی
🔴
در صورت جدایی، جورجینا ماهانه ۱۰۰ هزار یورو تا پایان عمر دریافت می‌کند و مالکیت خانه‌شان در مادرید، به ارزش تقریبی ۶ میلیون یورو نیز به او واگذار خواهد شد
🔴
این توافق همچنین از سرمایه‌ گذاری‌های شخصی رونالدو محافظت می‌کند و در عین حال، نقش جورجینا در تربیت فرزندان و مدیریت خانواده را به رسمیت می‌شناسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141848" target="_blank">📅 16:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxr_4zUCpDPz5S32fbZOjCYZABKnVALJ7Xzt_i0TzANO-46iS9gdLaB1Zub8ymP2yyFTTfuKYzMxeyA8Pk5ln8TRdCnSFzGrEQH9yN3wrK1T7_XkhFQO9mBy1-Bzu80lmRzo7Qt_uQO8ZlkroN8i7c45BuAHWf-DN9NCMpjaeQzA56ukdmBLI4X0JZ9BMsVHLrHG5KpI18AvYsdwIdVNd1w6nFl5VNLz8xcAUkUilLtbHWTqo7mwx1i-SIHJoeyPzOdRq1qNRmEZcPz9zM6oYw8BNM_eZ8SnRidZqGQ24eW2Y_6lo6At-ttGFTt8Ka0dDvFHH0oefS3SDS6vYulQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عراقچی: با عمان بر سر نقشه مسیرهای عبور از تنگه هرمز توافق داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/141847" target="_blank">📅 16:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b35919d9.mp4?token=qjDdGNtZSwK-jvUyoPCmd6SC-RmnRylERUxrXktcFDsLEVLCdz_lJt2pC5rcFhxU9NlUgl5cpqlgPC1ViWcVTgGtfqXTFqkEYjPs8msoz-Uj5sA2ywseZGGgMR-S0VcTVdi81lW5v68DmlzPEgYG2Lrv78hVI33fkdhHYJButLHOLkNqlEVMKu1StK6efjKgHaGrG7ciS0702fwCXbkIPSu37aQFmbDZzOK54SgVAF8LPhhBfWANlp2tSGeg8BpAolVZjiTaCcfKpHyAZIATsA2V0zF1lsGtOg1QmSGbGJKA7NoSjBICOljErpHYZ14YS7Anl4xinzoLVViOg2wEdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b35919d9.mp4?token=qjDdGNtZSwK-jvUyoPCmd6SC-RmnRylERUxrXktcFDsLEVLCdz_lJt2pC5rcFhxU9NlUgl5cpqlgPC1ViWcVTgGtfqXTFqkEYjPs8msoz-Uj5sA2ywseZGGgMR-S0VcTVdi81lW5v68DmlzPEgYG2Lrv78hVI33fkdhHYJButLHOLkNqlEVMKu1StK6efjKgHaGrG7ciS0702fwCXbkIPSu37aQFmbDZzOK54SgVAF8LPhhBfWANlp2tSGeg8BpAolVZjiTaCcfKpHyAZIATsA2V0zF1lsGtOg1QmSGbGJKA7NoSjBICOljErpHYZ14YS7Anl4xinzoLVViOg2wEdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طرف داره وانمود میکنه که داره به پیرزنه کمک میکنه؛ همون لحظه کل طلاهاشو از دستش در میاره و‌ فرار میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141846" target="_blank">📅 16:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آتش‌نشانی مهاباد: انفجار بنزین ذخیره شده در یک واحد مسکونی، ۸ نفر را روانه بیمارستان کرد
🔴
۳ تن از نیرو‌های آتش‌نشانی، ۱ نفر از افراد حاضر در منزل و ۴ نفر از همسایگان، دچار سوختگی سطحی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141845" target="_blank">📅 16:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf8b9dc48.mp4?token=dF0J9MJrXePB06jCI6iN3RppgYwbD274GIqn-_hRM-u_SNvLc5Y12oGsA1NM0usHZN7xQV4qSgSfLjCui9VEPX0QhZV7lY-ZSm0rBVqkdoNOqadzUDY9c3lhJmyMmW-Quihx4qH34g3a4Zxq8AbNc9QVYdF-FfDU2WWq0mAY7LSxSvEchKD6IpvihZBdKsidBUIVjkqKXbIioW7_KeOm_2HcK-F-FIWz0--TqPXQHfJwaUtJYn09dWER-gbGcB7T1p3hFYQGzDyooY69FdUtHdf6Il7uW8hc7p9uoTCJMuLIRTcB4C-I5PsdNGnhnkAKs15bl-oIzbe9AFNZLJfLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf8b9dc48.mp4?token=dF0J9MJrXePB06jCI6iN3RppgYwbD274GIqn-_hRM-u_SNvLc5Y12oGsA1NM0usHZN7xQV4qSgSfLjCui9VEPX0QhZV7lY-ZSm0rBVqkdoNOqadzUDY9c3lhJmyMmW-Quihx4qH34g3a4Zxq8AbNc9QVYdF-FfDU2WWq0mAY7LSxSvEchKD6IpvihZBdKsidBUIVjkqKXbIioW7_KeOm_2HcK-F-FIWz0--TqPXQHfJwaUtJYn09dWER-gbGcB7T1p3hFYQGzDyooY69FdUtHdf6Il7uW8hc7p9uoTCJMuLIRTcB4C-I5PsdNGnhnkAKs15bl-oIzbe9AFNZLJfLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لهستان بزرگ‌ترین رژه نظامی تاریخ خود را برگزار کرد؛ دونالد توسک هشدار داد: «فقط قدرتمندان از جنگ دور می‌مانند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141844" target="_blank">📅 15:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده دائم روسیه در سازمان‌های بین‌المللی در وین، اتریش در ایکس نوشت: «دونالد ترامپ رئیس جمهور آمریکا تهدید کرد که تنگه هرمز را قلمروی ایالات متحده اعلام می‌کند. این یک شوخی بیش نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141843" target="_blank">📅 15:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز: امارات متحده عربی اعلام کرد که ایران به یک کشتی شرکت ملی نفت ابوظبی (ADNOC) حمله کرد در حالی که این کشتی در تنگه هرمز در حال عبور بود؛ این سومین حادثه از این دست در کمتر از یک هفته است که یک کشتی ADNOC درگیر آن شده است.
🔴
هیچ آسیبدیدهای گزارش نشده و شرکت ADNOC اعلام کرد که وضعیت تحت کنترل است. امارات متحده عربی ایران را متهم به انجام حملات بدون دلیل کرد و خواستار بازگشایی کامل تنگه هرمز شد. ایران تاکنون در مورد این ادعا اظهارنظری نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141842" target="_blank">📅 15:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
زاکانی: مترو تهران تا پایان جنگ رایگان است
🔴
‏مترو تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141841" target="_blank">📅 15:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic3JCD62OfefLOvHYkl5xV7rRvWItNDJ_QQ8O_Zi76Br25DMT9I8Cw9wymcn8iOlCbtsR9PAPmhyo6wswsZ4L1icfcp2BU-dfLr2339jYY67PGm_ZasXsaQV1RMBu59kaxaIauiGpau8KnBk24uL1AuNdCZDU7UOper21GQyHew8n5C2npJ4w5BHe2BgUy5iiXpZWS37IQwXVXz0nRdS5MULm6dwM0x6QzsS06iX1AdFdLf4_8WTyq-qZVXd2H1nYV8T-Dxje4A5R_EWVarBxuZJAhJOo1fXlTlid5Ecr8SjEKIYIgNG5JuwjCiAihxPXMaVcRf1sO7aDwExM_4fgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی گزارشی در رسانه ایتالیایی، قطر ده ها میلیون دلار به اعضای اخوان المسلمین در ایتالیا کمک کرده تا مسجد بسازند و به گسترش تفکر اسلامگرایی و حکومت اسلامی در ایتالیا کمک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141840" target="_blank">📅 15:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41653dd3a0.mp4?token=a9PI1wRr4iMuuFwCEZ7BAGqP27Iv4WDjkBjwtTBhNsU0x94gZYnAYTCPCDHCWJO08ORdYmv10IMHihsLN-tbUoYwvm6W6e8b-B8UJzNUKh3fSaENnS5aAXwNDm1Gy8awRq4xLf8SletlXcjemSFStHr7L_MFx0SXrq37C08Ja2GZrMFZUR_--UdWrzcPPtwiZtb7hITJjJu01kn2fyibAgILyYLXzBWpo7ELPXjeIvyFDCLR743_g7jBxZroR8XMa0NIL1DKJdC1BPct0oRkR4qOyaWpqy_so1NYrUXNh24Lbswf5qS8yIZEmoYuuVt9vXcFvQ3hat7ybRYa-lMPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41653dd3a0.mp4?token=a9PI1wRr4iMuuFwCEZ7BAGqP27Iv4WDjkBjwtTBhNsU0x94gZYnAYTCPCDHCWJO08ORdYmv10IMHihsLN-tbUoYwvm6W6e8b-B8UJzNUKh3fSaENnS5aAXwNDm1Gy8awRq4xLf8SletlXcjemSFStHr7L_MFx0SXrq37C08Ja2GZrMFZUR_--UdWrzcPPtwiZtb7hITJjJu01kn2fyibAgILyYLXzBWpo7ELPXjeIvyFDCLR743_g7jBxZroR8XMa0NIL1DKJdC1BPct0oRkR4qOyaWpqy_so1NYrUXNh24Lbswf5qS8yIZEmoYuuVt9vXcFvQ3hat7ybRYa-lMPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار اولیه کشته شدگان حمله هوایی اسرائیل به دیرالزهرانی دو کشته و ۹ زخمی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141839" target="_blank">📅 15:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuYYJ86roG3YHDT5KTwBC7Zi7GSwj1PTz_zqN94Mru3UnesoKNRWubOjoBUsVSQIpwUcjX6J8-YQk1jZjsotniakXSQJHi2u86lWk1qYtMSpv_q3fMMuBIvax5fsEf0rmose18TV6VyzsR06zSTxSf42XzfE9i579CkiP_5R7fnU1ON8Nn4KXmxvU7gSDDe5u8BRe8FAr6u2mHK7FCh8KxJzP4kdzdMAPcKbIize6xVcb1xannOtI51Wi3ZTQLK7UfNX5Ydg2MYlSEHyjYEUfFBHXcAsuCDz5oXVgNAbq202qzMKQF-vEudpqOUCznUrHB3desmz9PdrgZhom0mmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff856ea1ed.mp4?token=KvIvE7mCv0QsjCoiiQPnBw7RV0JZusj3GMExeVqA0tWf6VbfbAk7TxcOI5wQ7eiKJ1tytMZyBnCAkiAFUoHpzy4G16yjME0xjsb3H97Dfdx50g56BZx5Y2FLl6Y-q64LDD-l3N-1x0WSjqQQbE2KZO5qdPmH0qSIG7-_oDKYXXwWOp9YOom7j85JcuSchagVuUwaobz0xaVBSsIRc9jAr9TrpwRsztwoOxVqLJt-BWp7CaHgbPD_X7OX7OV_92WGxpYp1eVSKquGSU4hShXoApeGtdBVkytMCNJm7Kxucgoe4Ia4B4cwk1iWM1ooS_RADu27DPC9Syx8zHWOAxACiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff856ea1ed.mp4?token=KvIvE7mCv0QsjCoiiQPnBw7RV0JZusj3GMExeVqA0tWf6VbfbAk7TxcOI5wQ7eiKJ1tytMZyBnCAkiAFUoHpzy4G16yjME0xjsb3H97Dfdx50g56BZx5Y2FLl6Y-q64LDD-l3N-1x0WSjqQQbE2KZO5qdPmH0qSIG7-_oDKYXXwWOp9YOom7j85JcuSchagVuUwaobz0xaVBSsIRc9jAr9TrpwRsztwoOxVqLJt-BWp7CaHgbPD_X7OX7OV_92WGxpYp1eVSKquGSU4hShXoApeGtdBVkytMCNJm7Kxucgoe4Ia4B4cwk1iWM1ooS_RADu27DPC9Syx8zHWOAxACiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش یک حمله هوایی اسرائیل دیرالزهرانی را در جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141836" target="_blank">📅 15:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: طبق اکثریت قریب به اتفاق نظرسنجی‌های فعلی، نتانیاهو در انتخابات پیروز نخواهد شد و رئیس‌جمهور ترامپ و مشاورانش این را می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141835" target="_blank">📅 15:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
معاون دریایی بنادر هرمزگان: تاکنون بخش عمده‌ای از آلودگی نفتی سواحل قشم مهار شد
🔴
عملیات جمع‌آوری پس‌مانده‌های نفتی تا رفع کامل آثار آلودگی، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141834" target="_blank">📅 15:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141833">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=WmU6oiwOYuB9DoaaHdbJy65qcXkqPKdKiFZrRWU5YcakkuhPjRqLg8ix80WHrfOtvzON51YGU24ecM-R21spZXElhplAYE4Mhfo5MPzOOyE3CFwswgMLtwAT9ANsAGDvd7M9z2PhVk4OFShyex0E6rijsS_733E35GeGU2v3DGj719sPB2PDzuryjptGC8w4TS26CBrMg6HUN-2VL0orPWy5fMsIgnCTJOwNIcUxr7EoBIuHEkkuukpNQvZrM45uRa4ZFytRTuNCBMBf9kB_OI5MflbgX43-3AObjrmVJ0tQbfPap6kXaxq-_i8ctaH7_dRaHts185iAXRuxCuD2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=WmU6oiwOYuB9DoaaHdbJy65qcXkqPKdKiFZrRWU5YcakkuhPjRqLg8ix80WHrfOtvzON51YGU24ecM-R21spZXElhplAYE4Mhfo5MPzOOyE3CFwswgMLtwAT9ANsAGDvd7M9z2PhVk4OFShyex0E6rijsS_733E35GeGU2v3DGj719sPB2PDzuryjptGC8w4TS26CBrMg6HUN-2VL0orPWy5fMsIgnCTJOwNIcUxr7EoBIuHEkkuukpNQvZrM45uRa4ZFytRTuNCBMBf9kB_OI5MflbgX43-3AObjrmVJ0tQbfPap6kXaxq-_i8ctaH7_dRaHts185iAXRuxCuD2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حمله نیروهای انصارالله به نیروهای وابسته به عربستان تو بندر المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141833" target="_blank">📅 15:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpwpbipO45pTb1ob2HLh2_SXjKGAp8uQ2Pa7PTF9awepoLQfLQtOUg1_-ND9PMZfgRV0W3ajvEbNJBiNg2vYansiqRlEJpXRiZpTi2LnbyqEuWNN9vpDPyJmv0eRILabLl3ReC2GC7R0frt8wbv15Jg8Hnm5RPoDBuq_hEmemvWfzaikNew6qOk7_UaL1Azt26e6-AZWMe9B2zcSEdzklaIgcSqSEajz2voUlFnN56JXY2C6D29MxkAnqKccEuggcULBvPEaZegwQXYd-ImRll1YO-5vmjFSWk7M1Y9MJt6Nk-HGSP8pQOYyffL84OPlo4C9qwAAmw3A7XZCSaGL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار باقرزاده: 3 خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141832" target="_blank">📅 15:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141831">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69d06dd3f.mp4?token=eUXUKrV6hzDEX4NikWsqjA0SyBXKTnSUU8HPIsuJlUbOdEBT4vXdXCdsrG-uNUj6P16K9GcbvnOnhRsOmgv-CmLD6bH-3rCVUOR5cp1R9Kej3w8nZKXJYK5Ut6mSFlM-C8LTQlTB22kvsyxPC6n4XvAl2k5uJWAFhSV7a3dY6yAkO97eTqFDSY-A8f8RVSnl2weDZhdX97y7wxc2njwoKWiBHjb39NpZSMd0C0_sKD7A6vsuqKoGkq-WbKFAWggZlu9tXV7q-86Etczo8gDyKiQ9FUu-ljXq0ChBQrP4Ho-oF_SavmHQbZMoRnQj0t_rvGdyzvAW-Lcc4KxKtA059Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69d06dd3f.mp4?token=eUXUKrV6hzDEX4NikWsqjA0SyBXKTnSUU8HPIsuJlUbOdEBT4vXdXCdsrG-uNUj6P16K9GcbvnOnhRsOmgv-CmLD6bH-3rCVUOR5cp1R9Kej3w8nZKXJYK5Ut6mSFlM-C8LTQlTB22kvsyxPC6n4XvAl2k5uJWAFhSV7a3dY6yAkO97eTqFDSY-A8f8RVSnl2weDZhdX97y7wxc2njwoKWiBHjb39NpZSMd0C0_sKD7A6vsuqKoGkq-WbKFAWggZlu9tXV7q-86Etczo8gDyKiQ9FUu-ljXq0ChBQrP4Ho-oF_SavmHQbZMoRnQj0t_rvGdyzvAW-Lcc4KxKtA059Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه استفاده از پهپادهای «کمین‌کننده» رو گسترش داده
🔴
این پهپادها کنار جاده مخفی می‌شن و ساعت‌ها منتظر می‌مونن تا نزدیک شدن خودرو رو تشخیص بدن و سپس فعال بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141831" target="_blank">📅 14:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770937ef36.mp4?token=QvIKBzMaoFVvjGcMPhzIOZZ2r0b8kB2HNE7dHUEokE-sbohOqWbcw2Z6lf6kWF_qV2CH4-Qp_A-0kEw6Xf5Il_rpXTg4PDKuXgDE7-eSbknaKszupuquBdYPBQJQ1trcr6jtVxSk4jngOYy_lIc4O41sqk05Dnr48XDvznDg0DkNjIViIl0thV6FxYjDz_-SCE6dWW31SmvUQStEVRDxudJfky6CACBEJoaVeoEmJp5jIyzKz1we47GHzCK47PVAe-WMvNsSpVgop6xTPJ-2i5VrULXgQwXvQY4fjrwBOM29ZltLx7Gs17C411ytNhv2yKsdq_127MJiAtWt4I_wXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770937ef36.mp4?token=QvIKBzMaoFVvjGcMPhzIOZZ2r0b8kB2HNE7dHUEokE-sbohOqWbcw2Z6lf6kWF_qV2CH4-Qp_A-0kEw6Xf5Il_rpXTg4PDKuXgDE7-eSbknaKszupuquBdYPBQJQ1trcr6jtVxSk4jngOYy_lIc4O41sqk05Dnr48XDvznDg0DkNjIViIl0thV6FxYjDz_-SCE6dWW31SmvUQStEVRDxudJfky6CACBEJoaVeoEmJp5jIyzKz1we47GHzCK47PVAe-WMvNsSpVgop6xTPJ-2i5VrULXgQwXvQY4fjrwBOM29ZltLx7Gs17C411ytNhv2yKsdq_127MJiAtWt4I_wXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پدر یمنی داره به بچه‌اش تیراندازی یاد می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141830" target="_blank">📅 14:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تام فلتچر، مسئول امور بشردوستانه سازمان ملل، هشدار داد که "ویروس ابولا" در جمهوری دموکراتیک کنگو "در حال پیشروی است" و این شیوع، به عنوان سریع‌ترین شیوع ثبت‌شده در تاریخ شناخته می‌شود و در حال حاضر، تقریباً هر 30 دقیقه یک نفر بر اثر آن جان خود را از دست می‌دهد.
🔴
سازمان ملل متحد، 30.5 میلیون دلار بودجه اضطراری اضافی اختصاص داده و 20 کارشناس بشردوستانه دیگر را به این منطقه اعزام کرده است، اما فلتچر هشدار داد که ویروس همچنان "از واکنش‌ها پیشی می‌گیرد"
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141829" target="_blank">📅 14:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aazWBsCg7RtsFZQ4PZxJfJT47uK6d1qwT_TLC9cgBLySMV84zigvo-z6ZmWTxjKgeld6VBaptwgG2jtD3AsdtjJTxTJ1kNybDtmwAMWPurN_FjGe5YkJ1t_DuDUFI-4vVRWmEB3QsWe5LZH0E9q7RnA0Y2xRkdPcAJaKhgID_66pqh9tWr6ktRny7_ciLGoLaHxPiJ3ZNwdGTeO2sBXmWuNKHBuC8Err6u00uFGKS4A_OExFtIy2w8OOyBXTC5lG5pC_3PcpacQR7NGMChSe0-3Oh1aBjIP54u2_D4cmeEs9DAL8LSaKfswQ7HaNSnXfQTtIqYqTEAK9YfJjuen-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف: ناو هواپیمابر جورج واشنگتن برای جایگزینی با ناو آبراهام لینکلن عازم خاورمیانه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141828" target="_blank">📅 14:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141827">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhA6akn8dKlsyu_MdN4F4tCQIqPmzkAkb2rB77yjJRJr8-TPYqoTRKKG0BH93j523kyV1gVZPHmomwszAaspczFtwaZssbH2t4evMksso50OkzLwfv_c714_yFkSg2vvG7OU12VGfNmAzJ3eGgHSPfKe9_bKePqTgVcL3vnF-FO5DEUTe_bvxzf9SpvSsfFoS4A-itquYjfx9mAtbh5nLw-ok9QH3g8TQnSjdwIYsLFrxaSntcg5etEAg72_NBUzjoWvJPiuthBcu9om2KQaFjo8Bj5IPgkptbazjG0AEqEx-CXOOrgusCyuSO3ZIUz_5XTx1B3mmXLDUVAiQg6wSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر ترکیه در سوریه، نوح ییلماز، گفت که رئیس‌جمهور ترکیه اردوغان قصد دارد پیش از پایان سال ۲۰۲۶ از دمشق بازدید کند و او را «عاشق دمشق» و مشتاق برای نماز خواندن در مسجد اموی توصیف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141827" target="_blank">📅 14:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با نخست‌وزیر هند:
اراده ایران بر تقویت روابط همه جانبه با دهلی‌نو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141826" target="_blank">📅 14:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / هدف قرار گرفتن کشتی اماراتی در تنگه هرمز
🔴
وزارت خارجه امارات رسما از هدف قرار گرفتن یک فروند کشتی متعلق به شرکت «ادنوک» امارات در هنگام عبور از تنگه هرمز خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141825" target="_blank">📅 14:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت خارجه: با وجود موانع‌تراشی‌های واشنگتن، با پادشاهی عمان درباره نقشه راه کشتیرانی دریایی به توافق رسیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141824" target="_blank">📅 14:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مجیدرضا خاکی، دبیر انجمن وارد کنندگان برنج ایران: از ابتدای سال تا کنون حدود ۷۰۰ تن برنج آمریکایی بدون ثبت سفارش و توسط اشخاص حقیقی از مرز عراق به ایران وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141823" target="_blank">📅 14:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شنیده شدن دو انفجار سنگین در مارب، یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141822" target="_blank">📅 14:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۳.۲ ریشتر در عمق ۲۶ کیلومتری زمین، مرز استان‌های هرمزگان و کرمان در حوالی فاریاب را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141821" target="_blank">📅 14:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رئیس اسبق سازمان حفاظت محیط‌زیست: برای رفع آلودگی نفتی سواحل جنوبی کاری از دستمان برنمی‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141820" target="_blank">📅 14:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کارت ورود به جلسه کنکور سراسری ۱۴۰۵ از ۲۶ مرداد توزیع می‌شود
🔴
کارت‌های شرکت در آزمون کنکور سراسری ۱۴۰۵ به همراه راهنمای شرکت در آزمون از روز دوشنبه ۲۶ مرداد تا روز چهار‌شنبه ۲۸ مرداد از طریق سایت سنجش آموزش کشور منتشر می‌شود.
🔴
آزمون اختصاصی گروه آزمایشی علوم تجربی صبح روز پنجشنبه و گروه‌های آزمایشی هنر و زبان‌های خارجی بعدازظهر روز پنجشنبه ۲۹ مرداد و آزمون گروه‌های آزمایشی علوم ریاضی و فنی و علوم انسانی صبح روز جمعه ۳۰ مرداد ماه در ۴۱۵ شهرستان سراسر کشور برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141819" target="_blank">📅 14:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بهشت زهرای تهران: ۵ هزار قبر در بیابان‌های اطراف تهران برای سربازان آمریکایی آماده کرده‌ایم، برخی فکر می‌کردند این خبر عملیات روانی است؛ اما واقعا آماده کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141818" target="_blank">📅 14:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کف حقوق کارکنان دولت در سال جاری  ۱۸ میلیون و ۷۰۰ هزار تومان و سقف پرداخت ۱۳۰ میلیون تومان تعیین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141817" target="_blank">📅 14:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si_b0Ln1LChQkc6CAB9wmicU667CIzulnQqNcHoK1QmcKPbH6LcEMD9yWMuiMhHtdj6gVs5f7h9WP2AwVHJmVy25afQWMOrlbgK2XVjZBqqLOzkZq8sRh-C7A2yQgBGLMNR9543tcA5DTQHM0HNW_mSupRTR0vZ9PL039r7JbBnNherauFqNgQkzym4uT8kxk0wlcsoqrT8Nyh7ZJyg4cu9MbL-ub9xg7dv_1zWQc0RyCxH8AxVDraMOPHr_qKEkQzinzjtQlFbNOpUyEtKJIs7rewyzioCsAVIBGMNt6ONzFmlTz_wa8cqgTARrZkPfG73qno2vzavMl6N2nF9IYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده به لاکهید مارتین قراردادی به ارزش ۲۱۱.۴ میلیون دلار برای تولید پرتابگرهای اضافی THAAD پیکربندی ۳ برای امارات متحده عربی اعطا کرده است که کار آن تا ژانویه ۲۰۳۱ ادامه خواهد داشت.
🔴
این توافق ارزش کل قرارداد THAAD امارات را به بیش از ۱.۰۵ میلیارد دلار رسانده است. تعداد پرتابگرهای جدید فاش نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141816" target="_blank">📅 14:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk1YEogSTPutGDqtGTMCNnMRYvx4Y8BcnfLCsSPvtgorbuNvesHqHDj3xJ0jt7eak3UNQ2diGwi-UeH4UnPPwjR7YXVC35m5l_fytteYIhTlQelwf6xDTI8rAYmQtvr4nJgYSyTz0bK5AcqrdNugbqjLEaQI2Lht_JlU-BvfhqPsf5WgmHKlJouXwUNTTZyZ_zvIch0zMKad6coYbS3gvClMC2TURZ3dn8ioO7mhMgENgtnUr7fMYykeezf9eP4dw6v5fh_XB5v6z_CwZN42ePErOd825fJxj79aKBf2NsscAGxOt7vqlqxnMyUWVSQWKEI1zZc36AOAcJbee9mMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طالبان امروز پنج سالگی قدرت گرفتنش تو افغانستان را جشن می گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141815" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91310e606.mp4?token=isjOnfPGxCCG2fOZ8it095cOAArK0Z_GTN-chH2RmtbQJeCbv6_myeBHE9iJnWv1biIbBlZsljoxfPGaZa3o3XJdegfEmmO3PELSUuFMIKsk8d6Myzn_j3Z70RHHISMMIujLvBw7Aqaaom7QrkKQA1rG7hz8fnl7defFHTykbQcZILT4nYGx3ZxG5dkrXaa4UYqC2x3VmITiGBv57lAU8Tbv6h3BsSKu_e5TpCCRpCMm2owNFZcZVIixLFMfisq2dDVfwc7nLYn6sIzVh5NGbehoVhbX6Ft4eb30Dc0kZLo3VpbfBiC45wkG5C51VVmMX-t29CsltGK9E9XxfP9EY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91310e606.mp4?token=isjOnfPGxCCG2fOZ8it095cOAArK0Z_GTN-chH2RmtbQJeCbv6_myeBHE9iJnWv1biIbBlZsljoxfPGaZa3o3XJdegfEmmO3PELSUuFMIKsk8d6Myzn_j3Z70RHHISMMIujLvBw7Aqaaom7QrkKQA1rG7hz8fnl7defFHTykbQcZILT4nYGx3ZxG5dkrXaa4UYqC2x3VmITiGBv57lAU8Tbv6h3BsSKu_e5TpCCRpCMm2owNFZcZVIixLFMfisq2dDVfwc7nLYn6sIzVh5NGbehoVhbX6Ft4eb30Dc0kZLo3VpbfBiC45wkG5C51VVmMX-t29CsltGK9E9XxfP9EY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراف میکنن که به مردم معترض شلیک کردن.
🔴
چطور تا دیروز میگفتید تروریست ها حمله کردن که؟!
🤔
حرام زاده بودن از صاف بارز طرفداران رژیم هستش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141814" target="_blank">📅 14:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / حمله گسترده جنگنده های سعودی به مواضع حوثی ها در یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141813" target="_blank">📅 13:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یگان مبارزه با تروریسم عراق از دستگیری یک تروریست تکفیری طی عملیات امنیتی در استان الانبار در غرب این کشور(در نزدیکی مرزهای سوریه) خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141812" target="_blank">📅 13:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8e792f1.mp4?token=eVHtdQD-wn5trlBGvyhg_hmpMaW3kH8D0N_drQc0hDG0F3D4n3ccaqvTwhVSAv2-hPbQ5UTJPkF-xQBb3uKfKJu5XH80oAoEd8AdOD8JoplTUECwZhgVOXXy5tuSZHDHbhzf03vyYwdZQZ41OQI6RHPS3DFwRZAdAuU1WCXNj2qsueIX2AZgk3JhEN_UFDEqJ8ZqzVg4XyF-IzJ1VBuMY99bIUYP8n5oDtnQEYt7WUuYTQLihLLvL0rfZK0_WO6POwpzGhP-UMQ-t3r5XVslcm-4e5IS151zNg_8vvOGeQZiL7RmvNTJ38-muHplm4yQvIF6DyQaD0zYtGz4ie2TRYqeOYHO9bupBKjefMoVlqy8I8KPneYGN1q-3W_-2KWAKBM0z2IcpUNLznT8FIipduceAf_9z_gMfp11cIfgH0p9oPUBQO7IqI7_ju4PBSOrH1d8wciT53VFvZaUHOl47gg3WXRz-irlEDo8xicePUYsCwVpWL81bKe_WAmaTsOgCwHVRHxjZP8Gk7qtV99Kd3R--ngu96YazGXGrETKihnBI33G-_EyWfZMoE1E-o791G2logaQT6aPcBXiEOg8t2TD52NA1MqHxBkxCLgrm5ik3V59Y3juffIhM4yg2eeeF1Etf3NTUDlsTleozDHh7RdZKAovs3nhBh6l-_JkoKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8e792f1.mp4?token=eVHtdQD-wn5trlBGvyhg_hmpMaW3kH8D0N_drQc0hDG0F3D4n3ccaqvTwhVSAv2-hPbQ5UTJPkF-xQBb3uKfKJu5XH80oAoEd8AdOD8JoplTUECwZhgVOXXy5tuSZHDHbhzf03vyYwdZQZ41OQI6RHPS3DFwRZAdAuU1WCXNj2qsueIX2AZgk3JhEN_UFDEqJ8ZqzVg4XyF-IzJ1VBuMY99bIUYP8n5oDtnQEYt7WUuYTQLihLLvL0rfZK0_WO6POwpzGhP-UMQ-t3r5XVslcm-4e5IS151zNg_8vvOGeQZiL7RmvNTJ38-muHplm4yQvIF6DyQaD0zYtGz4ie2TRYqeOYHO9bupBKjefMoVlqy8I8KPneYGN1q-3W_-2KWAKBM0z2IcpUNLznT8FIipduceAf_9z_gMfp11cIfgH0p9oPUBQO7IqI7_ju4PBSOrH1d8wciT53VFvZaUHOl47gg3WXRz-irlEDo8xicePUYsCwVpWL81bKe_WAmaTsOgCwHVRHxjZP8Gk7qtV99Kd3R--ngu96YazGXGrETKihnBI33G-_EyWfZMoE1E-o791G2logaQT6aPcBXiEOg8t2TD52NA1MqHxBkxCLgrm5ik3V59Y3juffIhM4yg2eeeF1Etf3NTUDlsTleozDHh7RdZKAovs3nhBh6l-_JkoKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش
‌سوزی گسترده در اسپانیا به نزدیکی خانه‌ها رسید
🔴
آتش سوزی گسترده در اسپانیا به‌سرعت در حال گسترش است و شعله‌های آن به مناطق مسکونی نزدیک شده است.
🔴
نیروهای آتش‌نشانی با بسیج گسترده تجهیزات و نیروها تلاش می‌کنند از پیشروی آتش و رسیدن آن به خانه‌ها جلوگیری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141811" target="_blank">📅 13:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141807">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izoLff5csVzcPUvNYIKKdyKLxYaKdSiUt6rCwp6ERaXIfu7hzormNbAfWYcId7u35LVoiGdtdsQHrzsHTNEo8DV667k5Y0ooznQ9fQ5u8bB-C_nxeIVmk5Tx0rx6H67aBIzDkUTGtEl-kfcdtaxumIJvqN8q3TtL3FVlAg8MRHrxiBC5riVV_gi4wF4g_iVrjcM2G3wIguEadzr8idaDryV0qadACRZGKagOd2j6fjCvzNST5XAhc3CPgkDVb0pkfxyd1U3Rmv5jl36YwGO3w21DyJvU4edzhmM2AoKd-FFSdVgF2rBXCGQkzX_HFrYAVHYxjcoCqMW1tM6TitG02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596d386743.mp4?token=ZN9T2gmxkA3okN1kwv0ANLCaEdpfSde06iZvOVUqhpqkUmthI7TzKN-X_CHlZECryk9J6tAH2fu3wDehoF9M0wrdiq276YAr6xLIaZzwFCGhPWgD4kehjCaIxDRw9MxmZ46ome_ddJieAiH8rIncGmmfJeaL1IdpTqH_GUKMTmFMpnBPz2hVecfnZ-EObn0naCKPmusJ4igh2z0gG0pEG5bbFLBV5uc4Wny9Y2FolcBGX0StfvFRUZcCrWiqTod8g5S1wpfoyUosLfO328ntvC9rNwnxPDCHmkr-LIHNcMCRbki07pie9zXOMp1FVUAUrQBJcyseVh7Vom2qoUWYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596d386743.mp4?token=ZN9T2gmxkA3okN1kwv0ANLCaEdpfSde06iZvOVUqhpqkUmthI7TzKN-X_CHlZECryk9J6tAH2fu3wDehoF9M0wrdiq276YAr6xLIaZzwFCGhPWgD4kehjCaIxDRw9MxmZ46ome_ddJieAiH8rIncGmmfJeaL1IdpTqH_GUKMTmFMpnBPz2hVecfnZ-EObn0naCKPmusJ4igh2z0gG0pEG5bbFLBV5uc4Wny9Y2FolcBGX0StfvFRUZcCrWiqTod8g5S1wpfoyUosLfO328ntvC9rNwnxPDCHmkr-LIHNcMCRbki07pie9zXOMp1FVUAUrQBJcyseVh7Vom2qoUWYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب جنوب لبنان در پی حملات امروز اسراییل
🔴
لبنانیا دارن از جنوب لبنان به سمت شمال فرار میکنند
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141807" target="_blank">📅 13:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141806">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368619c5a2.mp4?token=RYdcVv1s41JOe6sIMc8bui8RDUQz17x14ZklGTkG8meZVPEQGRNWFg3LcgslC54mAanWuxheXNB8lzMam7mry1MBsV1JOxYN-OgdgIiuY9E0S9OozCeATZFd08OrcQIYPOZSL_j5f9N-Tnb2VPbu3J3X9t2pIqDYncf-pTdcfWQLx3TwUeROJtXDWO54w092bG-UHoJRYvtmBEh7vJNkd0rxCVlUU5iEi39JHpFzLKSQg4fqABue1KB_2mx_vLtSMYI_qsVp2IDZsApRymnQ6HckDbfTWPUL2o9utUgafP5HdfFXI0ZBbvuOJpwj3O9mZt5pd8pM4luXu642GVYLkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368619c5a2.mp4?token=RYdcVv1s41JOe6sIMc8bui8RDUQz17x14ZklGTkG8meZVPEQGRNWFg3LcgslC54mAanWuxheXNB8lzMam7mry1MBsV1JOxYN-OgdgIiuY9E0S9OozCeATZFd08OrcQIYPOZSL_j5f9N-Tnb2VPbu3J3X9t2pIqDYncf-pTdcfWQLx3TwUeROJtXDWO54w092bG-UHoJRYvtmBEh7vJNkd0rxCVlUU5iEi39JHpFzLKSQg4fqABue1KB_2mx_vLtSMYI_qsVp2IDZsApRymnQ6HckDbfTWPUL2o9utUgafP5HdfFXI0ZBbvuOJpwj3O9mZt5pd8pM4luXu642GVYLkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراف عجیب مجری صدا و سیمای جمهوری اسلامی: حتی به ما هم دسترسی به آرشیو های پهلوی رو نمیدن
🤔
خاندان ایران ساز پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141806" target="_blank">📅 13:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/titEr8fwJjRnVzRSg1_wGUqWZRU-P-i3M6RxBQu_D-pkoej_lf1G4Suxhkp-uIzbZYf4I5xtYRDSiG130yIZ1vpDgdUY2Kq_D7Sf9nNkD2vmJRai421naznF_kuBydFILP6v8c6GPjNPOtzgsDkW2I3J3a0hAZWjMcb1OdZ1-Hj1P1k118JLbKS-HvdowpBDtRI7aFkeW6_0OLCosz5OM17L-D1mxZPvmA3su85XZnMWyuCjiaX0tfKafzYiI02lABm1DOqEgOSp0TZ4XqmYejtflzcENxJhuypXWHtLl78-V_ipVy1TaNN_4Z4RO_SR7YerhC5-n3eSZPiwZKj6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تریتا پارسی: به نظر می‌رسد احتمال آغاز دور سوم این جنگ احمقانه بیش از پیش افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141805" target="_blank">📅 13:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
طالبان خواهان از سر گیری رابطه با آمریکا است ، وزیر خارجه طالبان گفته است که دیگر دوران جنگ تمام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141804" target="_blank">📅 13:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تحلیل الجزیره: آمریکا نتوانسته کنترل خود بر تنگه هرمز را تحمیل کند
🔴
بازگشت این کشور به تهدید‌های اقتصادی علیه تهران، نشان دهنده شکست گزینه نظامی است
🔴
ایران همچنان چندین اهرم در اختیار دارد که تنگه هرمز تنها یکی از آن‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141803" target="_blank">📅 13:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اژه‌ای، رییس قوه‌قضاییه :اراجیف ترامپ درباره تنگه هرمز ناشی از توهمات این فرد سبک‌مغزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141802" target="_blank">📅 13:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e629cfdde.mp4?token=vkUlGYM8U1smh_5g-aFKg0lgrTAOARrjNmA3PULBcTzzQ83amWV74aWXhvVgbCqliOl2AsQLhmwAbERV1dKvmhd81GccuTDtlQNr6XFgPpokoeNoCRaVG3JUwh4-inot9yPLkUXb-42ltsjoptl6EVRmsTMDx7NVM-jiPlibFNZGAFE1ryH6FhStDzfRw0V-2W2M7rGLPu-rq1jCpfvsx1JAbeZjuD2is45g90fszN5piUgNYQuzOD7-JP540HCdrMCsYfoWB0QSy9EtjXuL1jTXagvvCSY1zScO3mZUy3Z7DT5Yxa9XB_L4M773tujNCXLA8kdwI-7bIpGweugmsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e629cfdde.mp4?token=vkUlGYM8U1smh_5g-aFKg0lgrTAOARrjNmA3PULBcTzzQ83amWV74aWXhvVgbCqliOl2AsQLhmwAbERV1dKvmhd81GccuTDtlQNr6XFgPpokoeNoCRaVG3JUwh4-inot9yPLkUXb-42ltsjoptl6EVRmsTMDx7NVM-jiPlibFNZGAFE1ryH6FhStDzfRw0V-2W2M7rGLPu-rq1jCpfvsx1JAbeZjuD2is45g90fszN5piUgNYQuzOD7-JP540HCdrMCsYfoWB0QSy9EtjXuL1jTXagvvCSY1zScO3mZUy3Z7DT5Yxa9XB_L4M773tujNCXLA8kdwI-7bIpGweugmsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری که پیامدها بعد از حمله اسرائیل را در شهر دیر الزهرانی در جنوب لبنان که خارج از «کمربند امنیتی» است، نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141801" target="_blank">📅 13:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
چین با حدود ۳.۵ تریلیون دلار ذخایر ارزی، در صدر کشورهای جهان قرار دارد.
🔴
ژاپن با فاصله قابل توجه در جایگاه دوم قرار گرفته و میزان ذخایر ارزی چین تقریباً سه برابر ذخایر این کشور است.
🔴
این اختلاف نشان می‌دهد چین همچنان بزرگ‌ترین ذخایر ارزی خارجی جهان را در اختیار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141800" target="_blank">📅 13:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mu4lu34iKLXtT1DjhU23M1I0HcpBK3af1ve8SHgx27H5W6xCKO1gJpVmQ0WK06Gm2fEaY7QUGSWh_h4xZ396MFD_CzYfK-BOSTUYK8kLH1wiy0P9W2uZgGX4DNba8rGttanqNTGOpq70Y2ul1-tSxTwkfwgT2VLujZBviYhV7-UFGzMk0nTqZZB91PQ3gF1SoRExwkGSGog8JI9b8cwqKxCr6uKHzsYOF35bb56_kdwWxh-UxylDx5OecuCUmexLH2-phP70mcn-QRqEKqUi23sxdzJsc1BLdMim867tQJ8Wr-0A7ADKZ-yDXqpk8ZWQRu7UcahNp5S-iUAIrvYv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه ژاپنی : پزشکیان در تماس با نخست وزیر ژاپن به وی اطمینان داده است ایران از کشتی های ژاپنی عبوری از تنگه هرمز هرگز عوارض نخواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141799" target="_blank">📅 13:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: جنگ آمریکا و اسرائیل علیه ایران احتمالاً وارد مرحله «بن‌بست» خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141798" target="_blank">📅 13:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تصاویری از پرواز و فرود جنگنده های اف۱۸ و اف۳۵ روی ناو هواپیمابر امریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141797" target="_blank">📅 13:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOITZ56OxiasI9KbQys1jG0G3aTT3pisFXEjWLSvWbeLMi3I94Ei9phISh2yPtWtxQU4ASmJTAD6RO8Cw6Vg6ZtFClCLY5u3XMwA4RU6GhewKcWu_xLL_ub1YA3N0y4hRcwWyYgfwBHspwJseYmbDoesFDrES5uo15XwhRhkqVMiPF4RMT5fUSsyPBRDCKFSDB29Ris7e3qGZkVM94HBHYvrTM5OGyYmZ80DC7eUVm0hAcPnqscRAIINkpTHzWR6eWGLE8iZoRiKbyDvNa5vsC2ets7I53d7llyhwA3L1B0UjWme3ItxaKjAKnDc3WtGKyH_3VLJCT_lpvVuFnaNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بارزانی: در طول جنگ علیه ایران، کاملاً بی‌طرف ماندیم / مانع از آن شدیم که اقلیم کردستان به سکویی جهت ایجاد مشکل برای ایران تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141796" target="_blank">📅 13:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
عوستاد خوش چشم: شروع مجدد درگیری محتمل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141795" target="_blank">📅 12:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت اطلاعات اعلام کرد در پرونده دو دیپلمات فرانسوی بازداشت‌شده در ایران، نشانه‌هایی از نقش سفیر سابق فرانسه دیده می‌شود و پاریس باید در این‌باره پاسخگو باشد.
🔴
این وزارتخانه تأکید کرده ایران اجازه نمی‌دهد میهمانان دیپلماتیک از جایگاه خود برای اقدامات مداخله‌جویانه استفاده کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141794" target="_blank">📅 12:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۸۷ هزار تومان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141793" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: رئیس‌جمهور کره جنوبی خواستار گفتگو با کره شمالی برای کاهش تنش و جایگزینی آتش‌بس جنگ کره با یک رژیم صلح رسمی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141792" target="_blank">📅 12:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سه بمب‌افکن استراتژیک Tu-22M3 روسیه از پایگاه نظامی اولنیا به پرواز درآمدند؛ احتمالاً برای انجام حملات علیه اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141791" target="_blank">📅 12:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPccfOWKlehrcDOB8OOutZZy4jolaGmSbBTwyxYnywWU7TQdkDpx1ULCcQwDHqRX60xLu_P8oKdyZ_3RdXpj8FQDB0yTTjOHk4wHhCzStmChD0WfAPvXQlWRfEQd_gwtb4l09l7JR9MRSCs4IJ_r0dimLszwIp8h5kM8p5pZElRYyN9LMDhbMN0DmtxaqVnQVFaMpliC8aI1PFEPaY9M8-IvxIT8Y2lL1sVeTpsZhylsuOLiAgSaAkwuZbItzojOC5FDLPASkzgtWlq4VlD5ojelCuH5H0O4DrYtkALcFzitSyTeainM2zBYk4MnWxiE2eyLIow9MPokAYEBr5uG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه جدید کارواش خودرو در ۱۴۰۵ / روشویی تا ۶۰۰ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141790" target="_blank">📅 12:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZd0qnF8Flv_KApoDm8OpP0eKe4FuMsoTs29gWEwBatL_77rx4xIzS5gddWk42YSC17uOnwS8YDO20--DQMKWE8wd72PN8vIPFN_nJ1zGaySoSsszgxNsseHsfKbPhcXtL3WSsG_q1qrELkFRJUZAXfP5oR507g2Z-4VCveeym10slGHRYa6amp7CF-sF8x2RbV627UxsLREyZaubQm_HKRE56flwukOrFF37ANRQljzMCm1bzrfYi1zeuZNqBtnATAmD8fYwNgiW5U1rZQc8CDoZNNAHXEKsq2d_qn7xZ1fHT5pmlTf1-b6j4K8V9S3vT2zcB1z9zSnuWZVUHtkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMTgnENhkkF1wgssoti5toK8SJ6TZYE8yqhiNe5oZUZSjssdXPubP4eHGy5NT9jFOkna34Ex0iLm707hPmEFqSwjppph3Imq7gQUJ4KYeHiIwUrDjGjQD4izW2_fYRGC3MrIp8BdQjFC2IjPThtBQI7jgIaq-V1XZkprDcggSQIcmiXPSvbcIZfxhreAALLjCa_5EK7UAmIc6ZXSggdn6T6EqlcFuJQ8ZWJVW4QyUMOGjtW_7uhZ7pPObbhpfcoqIgogD9kkPj6DyFtJE9n5ISxIcMdtrxg8KfNM3mDskdmQ6ci8X3ZXZEQFl9DCDilxEHYX5bXJu_DiMtUax2pkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKFJ5EvopFIe5AZ2Yr2CDOCUnQ07gOviv6MPq0Cn7SekdkaAOmKkPgpBetcPljj1cymk_9o00GU42OrNuufpdWc8D9IHIpbFSsJBVlZb-thTqzoEZhxyOvlfY4rkp2svl3wolLS436Fh45fbcOSZEQaElJDocWC8Mvv8OD4Nu9fsdwjIrm3ECBR_fx7H6I2MKgPrWTMXpzcRLh7cMRvq0b79H_U9_GzrJqCG_CpC6A9jlCoysm1p6OKy1FHeX7G03wz2nbCXn2zkpdIwcVmPgd9UVO__EV_kY0jbhAaqA7ydoBO442lYVXE4ti8J3b0bcWoDg0ycFiK_HF-G_Qtt1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ، چند عکس تولیدشده توسط هوش مصنوعی از خود و جورج واشنگتن را در سالن جدید کاخ سفید منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141787" target="_blank">📅 12:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141786">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czSa-dsVNCcHenJS-zuQj27cyu4KMxrYa320g6z5RhPONyMDSfVBsKfdBPxJcTJg640q0iBfAUTzN1NRi2pGa5pCifwL3Ob7srE2voBXOtwUt9YDjwMfhefykb7gvNRRmqCHk0ZrDxV6wutPnZxn9uBzYBAMawYKYq2kV5vhTuz7ldIJPGGWw0i_TDqpI4bBCfFNIl63BSBGtllcDGpiTzzUKUzcX1IYgNXX_EyMdWnrJqp8mB6kQI6Dr98KoMHIqXy-U6go9MvYJG32n-kMmGX8smeOr_5McoD6GhL31XeX_qSPzCk8s2L5YLMmPila-fjk7waVt4zcVEvI525R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفظل اقبالی از نزدیکان جلیلی: انقدر وضع حجاب خرابه همه مردها تحریک میشن حتی خود من
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141786" target="_blank">📅 12:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141785">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141785" target="_blank">📅 12:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141784">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سلمانی» معاون سرمایه انسانی سازمان اداری و استخدامی کشور: بر اساس اعلام وزارت نیرو تا ۱۵ شهریور امسال ساعت کاری ادارات از ۷ صبح تا ۱۳ بعدازظهر تعیین شده است و بعد از آن در صورت درخواست دستگاه‌ها، تغییر ساعت اعمال خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141784" target="_blank">📅 12:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141783">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ارتش اسرائیل: به حزب الله اجازه نخواهیم داد که به نیروها و شهروندان ما حمله کند و به از بین بردن تهدیدها ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141783" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
