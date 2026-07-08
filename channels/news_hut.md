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
<img src="https://cdn4.telesco.pe/file/QR1ePsiGx-a3pmKpiBAZi5GXhn55iS2k6AzlIscQ0VJDiQb2HnzNbIy58kmgMKbhI1yLumAOisYkIUNJGGylo6lB-4lOC1V-YJ_8k3rDr5crH4q1ZSfaYJEtEtzILLeNGBHD9794uPZBZKE3_1YBaiVeU6PecCpmEuS4gYEbv0_XWbewkNx4WpjL1S9QQn8SgjI2V2xsjfRMWqqH6HbDMKrJvt-Ld17QT5VkrI0K3V1ep7OkTLrFC4w_GWu_Z74-k62-BsJZI_f8qTXhNcYfvvCF71cWG4mMN1IHVciTjhWYmKIqb8wV_1nYgsAZS2Wqsiyi_rO6_CsD3xrTHsfsKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 193K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 13:38:29</div>
<hr>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Gjs2HGQGsz6bcn_MtNDYC-dvhJYEmRpGyv4BZ-9ythAC8ujBFj1kAHYCvaex6m2wYJBQBOmzRKHWEeTkb3XO2vq885Es80CWsbXiGxOr0A7DoNxQnef72Vxg2LbyMfXtud3b1j_ebHaezvGmFo0wbFiRyNmMwVuXpV3_P4P-3RWjJwuV3LvtsSrLJG57AHdw5wQEy42EkQvO2ZvgD5KS_58RRKjFrHYage8EBXtKBIXdmr2r1E1YNse-pcbWNZp9S2EQ8m8WPfImxu6PeOw-0KfCIu8Phrtm6oYuRgiez0kcEd5Q_zU8rzqXmgTZpsn_Btlwbq-JXt4hvI2HIC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67508">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyoxHQ_Y0RbH3W5EjSHeNpR-5gBfUgXLMskniYu08QUSqglQmwYRm0ar47cAne9k2eP9_8DpWvMQtrOvIk5dHP2rUY51PMbTIuJ_gV_Av9Eoj7o6z5YBe4xlNIwd2sBT5tpGN_zF65uWLSfg7jMUHBkkl2hxw9rtqo7UlULlwjoENSsUE_vprG2GPedAk9iE71BCKjT5CDkKLNvhlurBO8HRQV3fiYMfHwgqIUjqt10DJ8MUhx84jZ3-xCM7nU8Fyx6tSj5dAo4hPEYfFuK4AL6S0CIUDA1ATbZXRJ8Fpv5mv7UKJgl19_Xo94dQcF6jg9fXuiCUcZ8ay4Cy5D5H_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمیت سگال:
پیت هگست، سفر برنامه ریزی شده خود به اسرائیل را لغو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67508" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67507">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
«ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67507" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67506">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=Q7WZoVHx3ne8mt9NXLHZ8sWOIOqETsRQ0HKvg7TP6K20P5a8O8cK5vFkA1cVxc-kEMkyQFvEwkBIP1TlBtIpUAu25uP1V5WizCAsrcS0M9IJQPdIAYMKein-_nVJIRS1C7MEyinN-UuJvHBUq2Pbm95-Ap9wPSJ0Y68FQaFozRCGwj1l7aetzP66vDyRWmwYheoaWdDONyegyFxdNdfeJX-LAr910laPGFLSCSWT2ognSy_rX5e2z2yoZygNcrwryXGG724NJgkeF3j3aQyUgbe3oIubu-FI58StYevEFlvxBpvrb_ktXU5lOiEBai7xMcMEOPxDzVbWhe5p-0QRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=Q7WZoVHx3ne8mt9NXLHZ8sWOIOqETsRQ0HKvg7TP6K20P5a8O8cK5vFkA1cVxc-kEMkyQFvEwkBIP1TlBtIpUAu25uP1V5WizCAsrcS0M9IJQPdIAYMKein-_nVJIRS1C7MEyinN-UuJvHBUq2Pbm95-Ap9wPSJ0Y68FQaFozRCGwj1l7aetzP66vDyRWmwYheoaWdDONyegyFxdNdfeJX-LAr910laPGFLSCSWT2ognSy_rX5e2z2yoZygNcrwryXGG724NJgkeF3j3aQyUgbe3oIubu-FI58StYevEFlvxBpvrb_ktXU5lOiEBai7xMcMEOPxDzVbWhe5p-0QRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره مقامات جمهوری اسلامی:
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما حتی درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67506" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67505">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=MTm7AU852rfhFwv1Cu6N9a4lqxanzBBTB9N3mHKlJN13smqSkCjZduGydss8MMFze8BoUbQp_HPXnBHfmZKJTEQtPC-OZPhohTlfbpIvsRslbkn-54QeAlAsPllkvikh7HeEHhIHrSjF_IJWO4TyFO7yk9GQEh6J2Twymt7oLGpTojp4bJw_X4PEfS4RdeHipZkOvOi6NNGjwNlJz6ZgdgblQOkpnKPOjjN7GjGSKu2kDukaGG1Y7iRDrrbRJR8_rlraKKgMluEhgTGPPDsY2a0rmMXTlk58Ug3XMhbq0ys4dnB7JP7j1LK4Nys9-SFlTjikmtZEY2eHftUE-p1vKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=MTm7AU852rfhFwv1Cu6N9a4lqxanzBBTB9N3mHKlJN13smqSkCjZduGydss8MMFze8BoUbQp_HPXnBHfmZKJTEQtPC-OZPhohTlfbpIvsRslbkn-54QeAlAsPllkvikh7HeEHhIHrSjF_IJWO4TyFO7yk9GQEh6J2Twymt7oLGpTojp4bJw_X4PEfS4RdeHipZkOvOi6NNGjwNlJz6ZgdgblQOkpnKPOjjN7GjGSKu2kDukaGG1Y7iRDrrbRJR8_rlraKKgMluEhgTGPPDsY2a0rmMXTlk58Ug3XMhbq0ys4dnB7JP7j1LK4Nys9-SFlTjikmtZEY2eHftUE-p1vKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
به نظر من، ایرانی‌ها ناکارآمد هستند.
اگر کارآمد بودند، ۴۷ سال پیش یک توافق انجام می‌دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67505" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67504">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=nFvhBbzybhunBmgAkj_pVd4TXYDD4W2wDTGcz4_FT8DQtncTdCBl3Gkg6rr_0A7-HsHGCWS-CCMALdtVtSVJSSK5ehNXXIAmLdU58od1UdYKjm0hjP1OMpJ8-aFwtcDAnGmyhVBZmvQJk30cFxvTgCII33SKQE4gptgKhIuFvbh5_eOV1YRP5b6esyuLXlaV8tSmOrqaSsgwDnqq2evqlgaKO_oMi6ay6QaxXZWpISxFhw-z0OHbBj5oHBi3Jir9fSr3AWDwe5SIpaf5wLipxlH8W-8WQ9q8xH-hpqbhSQrVgZVighbW26REvSA0tokogpa0DM4TFTB-c8Gyb3-VTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=nFvhBbzybhunBmgAkj_pVd4TXYDD4W2wDTGcz4_FT8DQtncTdCBl3Gkg6rr_0A7-HsHGCWS-CCMALdtVtSVJSSK5ehNXXIAmLdU58od1UdYKjm0hjP1OMpJ8-aFwtcDAnGmyhVBZmvQJk30cFxvTgCII33SKQE4gptgKhIuFvbh5_eOV1YRP5b6esyuLXlaV8tSmOrqaSsgwDnqq2evqlgaKO_oMi6ay6QaxXZWpISxFhw-z0OHbBj5oHBi3Jir9fSr3AWDwe5SIpaf5wLipxlH8W-8WQ9q8xH-hpqbhSQrVgZVighbW26REvSA0tokogpa0DM4TFTB-c8Gyb3-VTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
من در تمام لیست‌های آن‌ها قرار دارم. و تا به حال، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی برای مدت زیادی ادامه نیابد.
چون این‌گونه است که مسائل پیش می‌روند، اما ما افراد بسیار خوبی داریم.
اما این‌ها افراد شرور و بیمار هستند، و ما باید از شر این "سرطان" خلاص شویم. این "سرطان". و شما می‌دانید چه باید کرد؟ باید "سرطان" را در مراحل اولیه از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67504" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67503">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:  فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67503" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67502">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=pN82QCw7B47lKDWsXaRvs8A8JgbI21-j3QgejPYNdO4OLUl3TApoO245OZ6Rq1-rsSv2GzeueK1VWyOSeqrHgin24dgEjkTqsi2CHNcdhyjzc4TUMjW_6WwcRVp2kLOLFSYgIlVK2rnN7vvKu9iBp_NCoxcekmvrbpovjMvGpF6oH0FuVWOrzuLhACV_1M1BhFh0XFpxbJO6bYYvTvbJGry8ut3gIsYnmjAJ8nD-GDWquDclOepWs7AUYkzOcgqh26V_rQVjo2DopYnW9dNG2lywMBFXTojFuhhrXDYQIardPP8NI8ZrcPkoNiTrzTfrk1GscvQQsJZ2t3OpRWD-V4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=pN82QCw7B47lKDWsXaRvs8A8JgbI21-j3QgejPYNdO4OLUl3TApoO245OZ6Rq1-rsSv2GzeueK1VWyOSeqrHgin24dgEjkTqsi2CHNcdhyjzc4TUMjW_6WwcRVp2kLOLFSYgIlVK2rnN7vvKu9iBp_NCoxcekmvrbpovjMvGpF6oH0FuVWOrzuLhACV_1M1BhFh0XFpxbJO6bYYvTvbJGry8ut3gIsYnmjAJ8nD-GDWquDclOepWs7AUYkzOcgqh26V_rQVjo2DopYnW9dNG2lywMBFXTojFuhhrXDYQIardPP8NI8ZrcPkoNiTrzTfrk1GscvQQsJZ2t3OpRWD-V4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:
فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته باشند از آن استفاده خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67502" target="_blank">📅 12:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67501">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeLOm9B5bxROvgwnFkCYSLMsAVKo3cXa005mNeeYoB2lIjot45E30XFQgmQeLUF_9-U25XAaV21NiPVSiNvD49LWdeKgL7pcbYLoSsnV59ppkU8sDGUIId4AcVANivHINqP73A0484qNhB2YYr9yKdJBcY1vUl7WVvozGcCvxJodPfPj7XjjO7ZHNY6QqeNB_WJPFvXK7xEbQLRm9CMvBAADy-dk7-XtyNSu-ugAD3aETvoa_WbVAhvhtjb-1AbQpbM1ItGgGXaUKE9hJO8UIANGQ7KkJyEg_H95uJ4Auf496Uj8VMSmf6sNXF2U1AXXrMM91K1iFFN4Eau3wHMFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67501" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67500">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=lyJxXCo64Kutqr2c8lIsKcXYKHJlM3naOtyN0ZOG5RW_IrjnpJjWxJXs_UhqdmkmY9YMiW150jM7NuHdC0ZG-4Rp3Ty0KCCkOlZvHr392kB2CSf_fgP-5_ptcXk6n7mptPpjcbnHPKFNyNuTMwBk8gsHIADOktR9SmXrMQotc2VH8zg_SYkwhwcP6L4LEXtAyqLPNMR7xTn6eanhmwjpH-x-A2rrP8ZM_GMhZW174IXBLcXD0p_blV5sl0QOQCOId6FKdSjzlOe42ArXvQm8Q_oSZgc5hbwVRf-rydNT8sDon7X-e-Qi5nPIT0xbhcj_rhXa17ca1KTvBpUv02hZmUGkaaTjfTKbdJMSP9eNzUFNSxsyGRozoAUxzmOkklrviHbJrJrQZagZJ3HDBDh_ZI_gsC-mzNVohFnlydznVQD78rWRyBVNY5cxyV8QikGBGOmVypBgAWLwNfRgsZRcmg8z4FO2ASGzJnvSsPuIqxD1tnDD8vIWrvcbTMEP3PNWtj3am4yRuN7_KdRlTXJjkUJxn0RVwTlDosjrxDIkPlLOwYbPDTlUK1vrL3mmEWbvP6xhclWY5wm6vBFHQDyJWJbkanxpJ7iq7mY5Vfh6YzF_QWAVrUIqwzUa_itK5wiSgWHDJx8HxR8Ezfdz3Cwuk9keuVYAfygMyV2BG8_eHVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=lyJxXCo64Kutqr2c8lIsKcXYKHJlM3naOtyN0ZOG5RW_IrjnpJjWxJXs_UhqdmkmY9YMiW150jM7NuHdC0ZG-4Rp3Ty0KCCkOlZvHr392kB2CSf_fgP-5_ptcXk6n7mptPpjcbnHPKFNyNuTMwBk8gsHIADOktR9SmXrMQotc2VH8zg_SYkwhwcP6L4LEXtAyqLPNMR7xTn6eanhmwjpH-x-A2rrP8ZM_GMhZW174IXBLcXD0p_blV5sl0QOQCOId6FKdSjzlOe42ArXvQm8Q_oSZgc5hbwVRf-rydNT8sDon7X-e-Qi5nPIT0xbhcj_rhXa17ca1KTvBpUv02hZmUGkaaTjfTKbdJMSP9eNzUFNSxsyGRozoAUxzmOkklrviHbJrJrQZagZJ3HDBDh_ZI_gsC-mzNVohFnlydznVQD78rWRyBVNY5cxyV8QikGBGOmVypBgAWLwNfRgsZRcmg8z4FO2ASGzJnvSsPuIqxD1tnDD8vIWrvcbTMEP3PNWtj3am4yRuN7_KdRlTXJjkUJxn0RVwTlDosjrxDIkPlLOwYbPDTlUK1vrL3mmEWbvP6xhclWY5wm6vBFHQDyJWJbkanxpJ7iq7mY5Vfh6YzF_QWAVrUIqwzUa_itK5wiSgWHDJx8HxR8Ezfdz3Cwuk9keuVYAfygMyV2BG8_eHVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره رهبران ایران :
«آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
اگر مذاکره‌کنندگان فوق‌العاده ما بخواهند، بگذارید به گفت‌وگو ادامه دهند؛ اما من امیدی به نتیجه نمی‌بینم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67500" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ :
سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67499" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67498">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67498" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67497">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67497" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67496">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه از بین برد. این احساسی است که امروز دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67496" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67495">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
قرارگاه خاتم الانبیا:
هر نهادی یا مکانی که برای حمایت از ارتش آمریکا علیه جمهوری اسلامی ایران مورد استفاده قرار گیرد، هدف مشروع نیروهای مسلح تلقی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67495" target="_blank">📅 11:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67494">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=gSLmKSjm_JU2G7PPE5HEVjtWVABslunYzhI2HK1TpfCiy8dhhjAyy4XI9m0uuPsJ5wukFsT9L20912FzFhyaW6lUgnnmeZ-Bs4vFR5rRzHnUSnMmF83WlO3YnpH1KIKgl462ZamjIddeeDHpcYYVYVp99LcMqrlo5LFOZuaNO5LRTU34fApatQknEnS_XudnWQ-g1By7Jc3XcL_1YeRrpI9en-UB2xehJOh9cCJtuaV-CHf41TGKKze_JKXIf11q3bTpBjGKe6w0NVhJkyLDwe-ZV-aQGE5xwATDiTLTd273eChkqN2GqYZmPhX76Eddg97x16UkvcWDyMHlaHa5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea62c3daa.mp4?token=gSLmKSjm_JU2G7PPE5HEVjtWVABslunYzhI2HK1TpfCiy8dhhjAyy4XI9m0uuPsJ5wukFsT9L20912FzFhyaW6lUgnnmeZ-Bs4vFR5rRzHnUSnMmF83WlO3YnpH1KIKgl462ZamjIddeeDHpcYYVYVp99LcMqrlo5LFOZuaNO5LRTU34fApatQknEnS_XudnWQ-g1By7Jc3XcL_1YeRrpI9en-UB2xehJOh9cCJtuaV-CHf41TGKKze_JKXIf11q3bTpBjGKe6w0NVhJkyLDwe-ZV-aQGE5xwATDiTLTd273eChkqN2GqYZmPhX76Eddg97x16UkvcWDyMHlaHa5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن رضایی:
مخالفان مذاکره صبر کنند، خود آمریکایی ها آن را از بین می‌برند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67494" target="_blank">📅 11:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67493">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67493" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67492">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=QIgc3Gl5pSYv13LuXvt97UJUNlPa_8RKnH6U_jFkBua08r6TS66YuEXEIoYCNI2lvA5795mOX5dtPpRdzjTCEKeZfREoVf45TvMhAe0MNvJYpGcqHg-YFJecc9noFEIH57NHhKMAaTX6g-T7H6whH8IsLqYFaOoJG4T4ZOw58nNO9_H__mLUh7NqcQmTWad9pujZ0yLP_jgRdSIiyDoUZFVxrk66k2UYKG582EEq7ChF-vsgGTYXKEn463jUc1YO_23kN0lYwwdFOXgg2hm0gBMUGdSlfqytPkYmAc34i6iBCzlP5Pg9bz7bHVNX77AM5bDwCnyjttwlZmd9AWEBIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6356a25b5d.mp4?token=QIgc3Gl5pSYv13LuXvt97UJUNlPa_8RKnH6U_jFkBua08r6TS66YuEXEIoYCNI2lvA5795mOX5dtPpRdzjTCEKeZfREoVf45TvMhAe0MNvJYpGcqHg-YFJecc9noFEIH57NHhKMAaTX6g-T7H6whH8IsLqYFaOoJG4T4ZOw58nNO9_H__mLUh7NqcQmTWad9pujZ0yLP_jgRdSIiyDoUZFVxrk66k2UYKG582EEq7ChF-vsgGTYXKEn463jUc1YO_23kN0lYwwdFOXgg2hm0gBMUGdSlfqytPkYmAc34i6iBCzlP5Pg9bz7bHVNX77AM5bDwCnyjttwlZmd9AWEBIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مستند حملات امریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67492" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67491">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجار به سمت پایگاه هوایی عیسی در منطقه صغیر در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67491" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67490">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBWoiH_M2a3Tfg1-YBWd4syIFQ6x3TCb31v6zP8DTmMLKsKL_Ka0zOyt6xpZovbbhaam_fTdQCFjSEVeLihFEbgIs-ltRfm7ARhp0SSr27I0dPY0tGNSj9K1eqs0aedPZ_ktecfB4yZ72OizeoqXddiujNuxzJ__QDoPfiBXCECdxfjXM9LdBkGFqO76gQzXaNjU-gTXwvtE7SdYmODbYAzUkWAeDihbB8HBkGmkyLQDHj08mMYOFHw4jHp60nEXSN8tgHRrsqsAp5-RkW_5hGHEeg8cHA_ilpeHsuB18TYqvLywMRY9C2FgN7D-lomkmBUVM8Ashfr1Q2eguHlQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف؛نقض‌های عمده تفاهم‌نامه توسط آمریکا:
نقض ترتیبات ایران در تنگه
تهدیدهای مداوم به حملات بیشتر
بازگرداندن تحریم‌های نفتی
حملات به جنوب ایران تداوم
تجاوزات صهیونیستی علیه لبنان
دوران زورگویی و باج‌خواهی به سر آمده است. این مسیر به جایی نمی‌رسد. ما تسلیم نمی‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67490" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67489">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF-NTGkSoqIiwHLoxY5lv_M4Sv8NIcSMgIYa2Wxz8MbtH5BndN2Qtd6rKdtXcdrLljDKCm9FaSINN2v7D0ME3gFqO1dw54End8GJ0Q9Nvo3-gjMJv1sW9oFdrVZD1sCwBlZ9fRcTp62T1G60mdXbtkSb4dDavM4vwQTyFBKXeauYH-QSDwhv4PhA7suupjZ7DvsZPGNY3GgfN2oG_D6GYEPfYoqvjdS-UzqQgvGnamQmoWfGInsaZvdABZDeRZILhT4lEK1Ewnayt0l0zORZwctI2nHp7UP1MaQofs976ugIgvMS7AFBwUWjkaBD0dw9oQ7nm0vmhHYmAejdQp_WQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یک هواپیمای آمریکایی مدل P-8A Poseidon که در حملات علیه ایران شرکت داشت، امروز صبح نتوانست در پایگاه هوایی خود (پایگاه عیسی در بحرین) فرود بیاید، زیرا این پایگاه مورد هدف قرار گرفته بود. در عوض، این هواپیما در پایگاه آمریکایی واقع در عربستان سعودی فرود آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67489" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67488">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجار در بندر عباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67488" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67487">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های غیررسمی از شنیده شدن صدای انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67487" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67486">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920364084.mp4?token=sDIT5-cFQyel0Bm271k48XQ7Dx26vvd3HldxdQRjNGSCnLBTtxTaKZKLvjqqoB_MPjW3OBACjBd_Qv-YtRapl05E3DbU2_h3kpsoEXimKUdVDHRQW8tmTqH8OX5r4l22YLiA_ddvDLrBCPyKwTFKNX19DBBrSMlesIyc7wEqG-vmkEOa25i8TZwjB0pEHfGvXeXAPuUNV_1_C7zCrqRSfdwELMh9rMYSYp5dsV0gSo5PNGw_Ar-gzZmWAA7cv9_NeIxwDHjAkHUJITJMBAoNyrfmH5YZ4J1VD_NtoBAw0a2XV4nWSjsKvW-n8TZr1JOcBMar2sp192yJwx4V4KILHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920364084.mp4?token=sDIT5-cFQyel0Bm271k48XQ7Dx26vvd3HldxdQRjNGSCnLBTtxTaKZKLvjqqoB_MPjW3OBACjBd_Qv-YtRapl05E3DbU2_h3kpsoEXimKUdVDHRQW8tmTqH8OX5r4l22YLiA_ddvDLrBCPyKwTFKNX19DBBrSMlesIyc7wEqG-vmkEOa25i8TZwjB0pEHfGvXeXAPuUNV_1_C7zCrqRSfdwELMh9rMYSYp5dsV0gSo5PNGw_Ar-gzZmWAA7cv9_NeIxwDHjAkHUJITJMBAoNyrfmH5YZ4J1VD_NtoBAw0a2XV4nWSjsKvW-n8TZr1JOcBMar2sp192yJwx4V4KILHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی‌ها خطاب به سعید جلیلی:
نزاری به مجتبی خامنه‌ای جام زهر بدنا؛ ما امیدمون به شماست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67486" target="_blank">📅 09:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67485">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au4AMouTjHZ24iz2vsg1UtCXHSmIVhFq3gRvOFKGP3vK_LE6TMKhdTCUf3yqxhfPUaa-ELaFcdQF1gdAvR7Cfz5fxWPI9b09al_o0EVVz5UMWl4nuFNwQCVglDU_ORRjGYGnifdh1AK_diNMpkHDECP1u2VOPrdAZG6GHAQa8PLeYB8D55bK6lGvr-tGJN9b7MF0JinxLoPMHaBiHgLTp9_leY2IGlO61s5yraDwrieWx3AJR1wzfwme0TgA2DX_7vZ37QzGBupEc5YEMiXmpucHutRJ_BkQ6NL5adYQxVU5DVoSImqqGuoobDSZBDSRioKVA06xNzTwj15-fFJj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه وزارت امور خارجه ایران در مورد نقض آشکار ماده ۱۰ از یادداشت تفاهم اسلام‌آباد توسط ایالات متحده:
کمتر از بیست روز پس از امضای یادداشت تفاهم اسلام‌آباد، اعلام لغو مجوز عمومی صادر شده در ۲۱ ژوئن، نشانه‌ای دیگر از سوءنیت، بی‌ثباتی و عدم اعتمادپذیری ایالات متحده است. این در حالی است که ایالات متحده، در طول بیست روز گذشته، بارها و به طرق مختلف، چه به صورت مستقیم و چه از طریق اقدامات رژیم صهیونیستی علیه لبنان، به مفاد مختلف یادداشت تفاهم، نقض کرده است.
از زمان امضای یادداشت تفاهم در ۱۸ ژوئن، جمهوری اسلامی ایران با حسن نیت و تمام توان خود، برای ایفای تعهدات خود بر اساس این یادداشت تلاش کرده است. با این حال، دولت آمریکا، همانند روال معمول، همزمان با نقض تعهدات خود، سعی در توجیه این اقدامات با بهانه‌های واهی داشته است.
وزارت امور خارجه جمهوری اسلامی ایران، ضمن هشدار در مورد عواقب نقض توافق توسط آمریکا، اعلام کرد که هر اقدامی را که لازم بداند برای حفظ منافع و امنیت ملی خود، انجام خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67485" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67484">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67484" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67483">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYpHLO-yAwtIhIUFUbUe2GZkQwoAupbym5_pwAtsHmFEPyMU0zIqwk69Ck7mGlbvs___hmXLNcyEX3rrZgeIjJPzFgsnWkajOnNtwNXnUzW_aoPkx-EDcFn4pdbNPLXp6HFqgyMX2S3VEx1Rs7aHQimtKM6eg8QmQUr1JTn5zFHbADZVj681usel4U_q9mHL9UX4NGhsZK3SlLYsgABuLujNhc6hRLkrFCqr6coR8ahIzrF3iSaf-WPkFrgsXlh-MCwew4TiEU3ZwrGFsubHztAvvypxGQe-YH5Ytlf9Paq_GG6ksViD_F8ClFastev9XE-NMygaY7kogn1F296pgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67483" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67482">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHN-axy_0M-fYRbHglWa6AGJoKfJWo4p4txMru6biCUWeEiOGMZWXGNor2jVV-oJv9sTw8wNDQMSJj4FZ-OttPNJvWnz8SwBgIbjZZpP8ocEfwkkQ-VeXeJuO5J4pNNTJ3oyahRibDGIt3Miqhzr1fW2Xdrmv192H6vJNeZeQSywgesxGBZ9DbIoEZQQuytYWrvT2IA2DP_Qaj4AWxSF8Au1D-YjTAYF-QZebofjxp0k5wSlduRjDfp9vIRf1DI0UiVdgwJDmUcSODv3H_E9Bxo1kS5G8TlZNbekqvSb6pyEF71lfozTzu1tTDdbWDuuLU7ifhj1bwtZo1b8NTyWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پسرا فحش میدی واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67482" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67481">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMGFHSHin1CWgMh90X7WZ2gopoYZeEMuQDot-9uKTRYm6EvHVBrFwmllr5cl5W6cpxka87sJa1QDzBlSROhZm-OBA3pf2Fospc_BxjRgw3XzGRukij2s7XB3XPz-BkvcUuvm1e1MQ96S8rO4cNxXFpPE05LYBS9syYX7yz8uZDaNSsDMJYImRerGJm3kmA22BAxH9zFqxXwIaf8Z6JZI4ZKdJpbtynaZgW9RYQgXP4VK8IWrx8t_nHPsgWta4OGEJiIoyFfsULOpAPGQkIq3KyGx1DUu3qInUk5kkn__r9pIpOLz9IP-74CMfY7QonUVSmAnfCbksVOGQY9BcjktEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداوسیما: وضعیت بندرعباس کاملا نرماله  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67481" target="_blank">📅 02:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67480">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بنظر من زود تموم می‌شه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67480" target="_blank">📅 02:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67479">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSor60</strong></div>
<div class="tg-text">به پسرا فحش میدی
واسه دخترا کنشی و واکنشی تحلیل میکنی
😒</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67479" target="_blank">📅 02:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67478">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEydeuJz_lPL6REKt6uG13r4OgVZ4WWn2JKgxhRfGCgZHnHP-63QGa5BC-1aTUl2HOYy9Me_lucUwW3C6xo2sNW4ioSTj9phQmQ0o_uVCU6AqrSlUIDi8Y_aM99S5VqXbIsojaFc8GtVWWa5XXO5VfozXBKw7d39fGZ-92hjN0pHy2PJezWd8kq7Xtc-yGLrpWm8X-mgwOqs8N7dHperln7-LVfblooEpU-Rlxq3T_PI1jGETR_pxezyt7uyei1z0CIgXnVkhXTK47_cdirJl96MMLs6c24BeqTmW7YRgeEEtcnxZsR5Id5FZOhxwqsTJJFJAnh_TvzATxKDsv4KkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اومدم بعد مدت‌ها، و تازه متوجه شدم این ادمینا تو دایرکت فقط جواب دخترارو می‌دادن متاسفانه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67478" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67477">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67477" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67476">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67476" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67475">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67475" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67474">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67474" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67472">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80cdbb5e99.mp4?token=mRTzFErg6Esf6xWUDglLYAlnyMqEI8iXbzWLEn_-wQbfz-KvlFHZUq4curdYI2ddk_XpiYK88FnfteMkYBbHzGgygnPdTnMBtnPCZVQpN05bCtTiYFCSdsTR9zofWE4oFJulnHgAOp9yqvzVXCG42zLEZ9VzitvAjmSUzJuBjo4N11_MfGphEBRxHPyx90_xu3s09K5n-guaJlHJtMnVdl35-1ElrAj9C9jTja8NE-DibAZAWkVymlaAVcxypZJpZO4Grcy3WuuZI5BCAdeDQQz-MH5J4Cyhm5Dx26HWVUknmGWBfr6SVme1XfLcCKEKB8bOQ9D0R3DBG-2xuf4w6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67472" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67471">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
پرواز جنگنده های آمریکایی در نزدیکی بندرعباس در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67471" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67470">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
انفجار مجدد در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67470" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67469">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEouIJbfPNLRVsoAiKGSUYyHBOyK1EXsq_nBT4rC4EJn_2quDINSKUr8akbVFS6CYXr5zuY6UAvZF4eaCZlyGIRvXTm7VtEnR4qas830QudmUMQCkIJov29fOPculs69HNtVwmYw0uW0jqkt0tHwvCEWsFwl3fuAa3KDMJE3fDZvZNokrrmp2NcwShYSJAIylW-k05P4QOoE4MJLrig2kpewjF3wHKzToouF8VaIhlb3n9JNjhhcGniu1NdHeo7DDsOT6ERf5Si8-EjKBQUricC9MZnyJQLKNafrtzOaF4H9N_sPTxnc-Vaoeg08khunqGaKKPzrX91K1wnXd6BIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
مقام ارشد آمریکایی به من گفت که حملات ارتش آمریکا امشب در ایران چهار یا پنج برابر گسترده‌تر و قدرتمندتر از حملات اخیری بود که حدود ده روز پیش انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67469" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67468">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmQzLijl6-MWybeuasyOLJubHsI5xxwlyG4pM1bs_GD1DOl7kozm-gD00cv7XudprC-YJqhrXyEivzPEVXxesJePLur9o3gB7vZbax7O6FzLc7MX3B7_UC32eHjv4h9cFy21680veFtoIKWoeCrvVKaIFfaza4PlkQcP5EktdvetGS4PcAn10H1qbN0JelQyuE3OCHVvCXT0Ggnx6o28mKi9M84qxbO0R1S53QF_cEwcl6dhLvtlkztr0vLXjoVFmer2meu46m9F6ERBFdOz98Q0-uYmtbbrqd-hceyLFXWeEcjxOozrqrbyP5xsBF83b6tkiZaFfAZjF_jnq6uEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67468" target="_blank">📅 02:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67467">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
قطعی برق در کویت و مناطقی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67467" target="_blank">📅 02:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67466">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
انفجار مجدد در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67466" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67465">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Atu9glSdsba52NKRAp-oG2aZ3wJ2vdCl11lFjLWk-SIKYDnJ52JWN-4iaolr5lSaIXjvkemi4NMrtGyYh7JwCljtcWdudE4YFrcfU20RoyLhIs67w9n2AC3Dwsr83YIWfi6Y868NlTdZnhCaka6hOX5tSO95sGEvzlgDpL11mk0uamvY8ZvNdknSB-_vUBdpvyIWMMUG4Xmz_R172AmKnMJP_LTxDLuRVmuqcmhH_dQQW0Eiijjn-eLLgOYRW3FztcO8lvz4F1D-M7-y2Ara4VzkMe1972ohchK9bTFpEwl5mwakBUrcJ9cpb-zDXgVucGytKx1wjGWaaN-47Wp4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfe17753a.mp4?token=Atu9glSdsba52NKRAp-oG2aZ3wJ2vdCl11lFjLWk-SIKYDnJ52JWN-4iaolr5lSaIXjvkemi4NMrtGyYh7JwCljtcWdudE4YFrcfU20RoyLhIs67w9n2AC3Dwsr83YIWfi6Y868NlTdZnhCaka6hOX5tSO95sGEvzlgDpL11mk0uamvY8ZvNdknSB-_vUBdpvyIWMMUG4Xmz_R172AmKnMJP_LTxDLuRVmuqcmhH_dQQW0Eiijjn-eLLgOYRW3FztcO8lvz4F1D-M7-y2Ara4VzkMe1972ohchK9bTFpEwl5mwakBUrcJ9cpb-zDXgVucGytKx1wjGWaaN-47Wp4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67465" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67464">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSgEZ5F1oE0Pm_wIXmaen16mYIisoeKTA6kzmJyiUXo0z8sNrJUfnIBM0TyGXVs0w-RwDC307bX0Ay244-xWKX57_esDL3t5NHm0r6PzRp8Y_UvikiH1wG1OFEO7gviFfjiakYGZjo7EfnywzYBUHgTRxqNfqNFlUIioDES9O6_TqOxf3EnKZofLLEG3pczj8GOqOp8giJrSbKwtkQNUYIRjdA5pVLlvluQ1OtF3eF0todYlexbAiHZtd70ENxYbUi4wT2R2NsdsfXj8UP4gwJqOQV9hOw2iu0YsPwU9vt6zQ3UgssFFlUB1J1SZppEE7uG_db2E6EgfZ8kvJ4ojQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابوالفضل ناصری، عضو فراکسیون مجلس:
آغاز موج های جدید و بی پایان سپاه
‏تا دقایقی دیگر…!
‏شدیدتر-ویرانگر! ‏
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67464" target="_blank">📅 01:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67463">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
کان نیوز :
در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67463" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67462">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=JCrNoZ8SM0pVC7LsqopKGiJdrETXSw87nOAYyYt7eQAh8EIw5xs2SHTnbjRlHqay2g__7AvFFtX-dSdImrKVTzpd6lkpnXthKEtBYGc2T4BsuDS8V6WCx4e7RjEA8cOakddGXetMrtwXpKx8ZG5YzIaCZVz3VdFJIpzbh7rL6udeAIHwCfs3Nlklqitdc8wKXuONdOuH0si2uSr85GcAG3JoXxeSPsQW6GGZ8w2FgL1AZnsUYTIIlizDdWwlrWKlAj3ys6-Sty2ok1YLmRw5YJo7cWsfxH_jwJ9fRU9B-1RaClWy4cYZGwlI58rNmHQDjM__5rPcnaHd49Ep2BxHEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d35d8f8a5.mp4?token=JCrNoZ8SM0pVC7LsqopKGiJdrETXSw87nOAYyYt7eQAh8EIw5xs2SHTnbjRlHqay2g__7AvFFtX-dSdImrKVTzpd6lkpnXthKEtBYGc2T4BsuDS8V6WCx4e7RjEA8cOakddGXetMrtwXpKx8ZG5YzIaCZVz3VdFJIpzbh7rL6udeAIHwCfs3Nlklqitdc8wKXuONdOuH0si2uSr85GcAG3JoXxeSPsQW6GGZ8w2FgL1AZnsUYTIIlizDdWwlrWKlAj3ys6-Sty2ok1YLmRw5YJo7cWsfxH_jwJ9fRU9B-1RaClWy4cYZGwlI58rNmHQDjM__5rPcnaHd49Ep2BxHEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید و آخرالزمانی ارتش آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67462" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=p8tiy-JmhwrElQeYn73NRi88c9DbFPyO4Vcroyfd6GEqGOX2dDsQ3QsmptL_mGf_PAAvf1ogRq_Hdd_CGA8umSTlTYLUMYM4qE41SeEQ5W6ThEyQ_aHv_Xr0oPNOiFjVI0fhrKqJ-KDh_oVGykhNcPzk3JfBThIN5JN8pZ2phz0WMPCVNgSrvpLDS4XwIbrF3VkIHLYZYSh_JaG8VXaZsmJB__ny2tWz5119V478zwhBo0oyEo-8rrYAkd8lWrKcphyciRD5zib7Tj6ICmPBYThoqYpTmJ9YK2uLSooRjhUV3gnzFovMG-2Befaly0mNSA0QmByJZFOXvYdvJ1Ra7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eaffe3050.mp4?token=p8tiy-JmhwrElQeYn73NRi88c9DbFPyO4Vcroyfd6GEqGOX2dDsQ3QsmptL_mGf_PAAvf1ogRq_Hdd_CGA8umSTlTYLUMYM4qE41SeEQ5W6ThEyQ_aHv_Xr0oPNOiFjVI0fhrKqJ-KDh_oVGykhNcPzk3JfBThIN5JN8pZ2phz0WMPCVNgSrvpLDS4XwIbrF3VkIHLYZYSh_JaG8VXaZsmJB__ny2tWz5119V478zwhBo0oyEo-8rrYAkd8lWrKcphyciRD5zib7Tj6ICmPBYThoqYpTmJ9YK2uLSooRjhUV3gnzFovMG-2Befaly0mNSA0QmByJZFOXvYdvJ1Ra7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنوب کشور
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67461" target="_blank">📅 01:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67460">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های مجدد در بندرعباس سیریک و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67460" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXdcQBfZPPPPb5wmpEtt_cGtTiBt9my2VY7ifOmJo9Khg6ZHo2HCDA6tFQ-lEkOZ7K1RkttpHIeY9cjXhTPOIED5eJBCvKBL_TJuDDOw1pboJJzBvWPKRYrrJBu7TPSuv9yNXSvDAHRHDJ-raHMhQYZOfY0RhbzlWdwLvcVdDf6sRMXVawVv4aduLuFvpUIayVMU8q-u_609Nt6VcUnECscBqG_qEP6Q67HedDHL35mne32tVyXohIRRUA1U7t2SUfUOa3u8ZsVzG_AmAvYBzjdyKOD4lLdVk1zgsTjOyipTXlk4vc1KegyBY--RD9tVeL7o7VgsGKbneNWnPlh8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تحرکات فشرده هواپیماهای ترابری نظامی آمریکا در منطقه رصد شد که شامل برخاستن دو فروند هواپیمای C-17A از پایگاه موفق سلتی در اردن، یک هواپیمای C-17A دیگر از پایگاه ملک فیصل در اردن، علاوه بر یک هواپیمای C-17A از پایگاه شیخ عیسی در بحرین و یک هواپیمای C-5M در پایگاه Alhairates در پایگاه الحائراتس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67459" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761109e119.mp4?token=XcV2VKEYMmD7B3J4ThClgkrjHNULLrgl9e3a1JPvbsiCcK6WcJeqLqfqG-BMbbsntSG5S3A1s1lZgamaf25TsDiVfdUDnd2EzuH3ngDp6l5r2umS7s3rpGTGK4H62aF_LK7u_HPwVavZ2CbBIc4y_gVznPxiWgqbNO8UTzjnVbjwBB2VR0tBdOr--iTRxqS-mlcNt6J44cpHshpJrlQOckRhQspVu8Pig3INW3-S54h23VJkFrCHAGa5_2l_htUWli3-94xcqu9PcnyI7eKNlDw5_52mkqPEhNXF3Xa20P7Drpf1UE_NryagflSll-dxgISL9y7xUIMReAHDD-0PlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761109e119.mp4?token=XcV2VKEYMmD7B3J4ThClgkrjHNULLrgl9e3a1JPvbsiCcK6WcJeqLqfqG-BMbbsntSG5S3A1s1lZgamaf25TsDiVfdUDnd2EzuH3ngDp6l5r2umS7s3rpGTGK4H62aF_LK7u_HPwVavZ2CbBIc4y_gVznPxiWgqbNO8UTzjnVbjwBB2VR0tBdOr--iTRxqS-mlcNt6J44cpHshpJrlQOckRhQspVu8Pig3INW3-S54h23VJkFrCHAGa5_2l_htUWli3-94xcqu9PcnyI7eKNlDw5_52mkqPEhNXF3Xa20P7Drpf1UE_NryagflSll-dxgISL9y7xUIMReAHDD-0PlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بامداد چهارشنبه؛ بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67458" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=didFiXIfKNqbcdYgPPX4HeQab5NP5Zd0NguCoewZHzC6SPRkrCBSQiGX-kT0lUnhzuhy9kkEqdoCjYJLfuPSTfY-02pFNj6HktwAlIjMmKKH5zu2plDiz2JVEANZn4NpM76sOrMbBraHD0ulGZL9wRwC3rnMwnZhwThyI_s1xyXA0Mf9I-ygSj3lUSf-5N3mDWoLjiEmR-XkMnyxeNztqe5xhr5djKoPqo9RsmdFnAhqK1iitDZkGNjnkOG44cCb6dyBQEDHB7SvId8UPdd3Lzkypvw-XojU4oZ7nHfw1MkrvZXwscAZzbSeqi6paEorj_yAYU22l0-8tSn3V_IeLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=didFiXIfKNqbcdYgPPX4HeQab5NP5Zd0NguCoewZHzC6SPRkrCBSQiGX-kT0lUnhzuhy9kkEqdoCjYJLfuPSTfY-02pFNj6HktwAlIjMmKKH5zu2plDiz2JVEANZn4NpM76sOrMbBraHD0ulGZL9wRwC3rnMwnZhwThyI_s1xyXA0Mf9I-ygSj3lUSf-5N3mDWoLjiEmR-XkMnyxeNztqe5xhr5djKoPqo9RsmdFnAhqK1iitDZkGNjnkOG44cCb6dyBQEDHB7SvId8UPdd3Lzkypvw-XojU4oZ7nHfw1MkrvZXwscAZzbSeqi6paEorj_yAYU22l0-8tSn3V_IeLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما که نقض نمیکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67457" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=sWGY5XHFCJ52uQ1tO_MKQh2l2Ucp7-Qrsm_7kO1C6VY6mVyepC5FD6hAbJPbNe72EHFk0H3qrKzyVERDAyTbGIwyKcb8belNVHcSUpJaZgtI7t8BtpOfsDqmfgeJKl3hCMmSgF8AZ9-4nOD7MkdUyToJ1p3wbKV6DhAveSzF5tNJTM_serE8WjM1OHZa9xf3x8y0JLEAjGL4ZthP8-Plz9QhbA4Dt8iq9JfWu5bTzj_pFrYCClaSInuUbpdrZ9xCvpMM1tNumb9eBVjdz1TCXBZ8Fb13E-GcVA4-ea_ZE-r909YqALSgZEZwmTX1VeuINJ0y-Cq0i4TuNdS-wo3YkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=sWGY5XHFCJ52uQ1tO_MKQh2l2Ucp7-Qrsm_7kO1C6VY6mVyepC5FD6hAbJPbNe72EHFk0H3qrKzyVERDAyTbGIwyKcb8belNVHcSUpJaZgtI7t8BtpOfsDqmfgeJKl3hCMmSgF8AZ9-4nOD7MkdUyToJ1p3wbKV6DhAveSzF5tNJTM_serE8WjM1OHZa9xf3x8y0JLEAjGL4ZthP8-Plz9QhbA4Dt8iq9JfWu5bTzj_pFrYCClaSInuUbpdrZ9xCvpMM1tNumb9eBVjdz1TCXBZ8Fb13E-GcVA4-ea_ZE-r909YqALSgZEZwmTX1VeuINJ0y-Cq0i4TuNdS-wo3YkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بندر عباس دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67456" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67455">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=QqT8Yc9IJrKjyh4uMAh195XxogZr6OiENE5-TEHO99C3mfXkuWGksZETDtlna7PMKV7de3wAMCgJLklinAfKS7nXNzYbuvgBiBw627-rEQocCtRZAQql989kG0K_wCAj8sfEXrURS2zOu0phofI0WvIpq91YayqwkZB9H7CJHBthg4rM1uqpcafoCEOlYFfDD5txTiHr0556ecWaQrkqW_nGHzKSjeTfa579-fSW7dmfe4B9CBbvKqddWRPn1T_HzeLg2IOcUIcjvvDrfKnQVaf8pQ2TZ77gEVRMDpwDBTOUK8LRQRxNg_epS3R58rWN_1G_VLB5bffk6vbpIEZGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0245f958.mp4?token=QqT8Yc9IJrKjyh4uMAh195XxogZr6OiENE5-TEHO99C3mfXkuWGksZETDtlna7PMKV7de3wAMCgJLklinAfKS7nXNzYbuvgBiBw627-rEQocCtRZAQql989kG0K_wCAj8sfEXrURS2zOu0phofI0WvIpq91YayqwkZB9H7CJHBthg4rM1uqpcafoCEOlYFfDD5txTiHr0556ecWaQrkqW_nGHzKSjeTfa579-fSW7dmfe4B9CBbvKqddWRPn1T_HzeLg2IOcUIcjvvDrfKnQVaf8pQ2TZ77gEVRMDpwDBTOUK8LRQRxNg_epS3R58rWN_1G_VLB5bffk6vbpIEZGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندرعباس دریابانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67455" target="_blank">📅 01:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال:
کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67454" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb48bc0feb.mp4?token=X1Fgzq--qdmyIGv3uLRmNxVXx9st9RL2WInJrbaok41Q0_9AulW_E4vUmMwc3_sEM4HLGxj60b-ShtB41ugigQ9IHC8xOVvgmaYZzBTBowquCzDkSVDbjbHRZbUanOYTwaJIpdNajvI3OVNskGXcRIsd5rPShXB2DOELxCX1Gaa8chG_a7J4aEXDDbkSTHEtNnDDAiHrCpbZudBq25NrjCOyZgCbp14j346DPm-DW934br_ajFAYcDlzl9MsM6rV4_-M-3b25seVrue5evZw0NcwrkZLIMvP3Up0Qhs-v6X0_4Mhdt2khLK7V1FFrAHy2sgYH1if2rk75RE91Sp4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو ای منتسب به پایگاه نیروی دریایی سپاه در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67453" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckVu4k7auW6NY0LUnRH33lAjPyiqPM-GGUej_qe97MeNZSEQ5Tc45zwfWDmUV7N4kOO4As2TW7iOesTlJOvlGE0jYP48nMlNRqoSczH1McaSqCrSv3wNtX4lICCeZyZ1O4-3S4QDyC4PF3xOwKk-egma3erUpzd_jTit0UxSOuq2bRO8vkOaydaUfUFxDJ-kYR7Nh0PmqD7rHiDeAvZKN1YTb_r4E4tqUBpPvBcCINy8Ho9GIZXyQupMsKU_wkXK-w-hCb7bBIMqPd-K2_XyiFqL1VO3yqnTVm3eIB13pD35qa2EyMnvAp-U6_O75J03feYzQ1K_to3HZ5cvQEs30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بامداد چهارشنبه؛ مشاهده ستون دود از سمت پایگاه هوایی بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67452" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koy7Woynbuzrc4nNyMCvORH8anRdLuMwr8Wv0s4kKlmZCvesJO_P4dg1h8KQNCkQj1aXZlCd9aNiV0ZxhfADIj2xxWIGzxmHFKDaClBaBXboTDMc_Eebf_MMl2dYnOMSuuqqFhheZafVliJvRbghfO9gUTPnJnt3p_PBrjvQ8pX0PazKFaV9mbMpG-S3wKaFBcAE4xHOs4IZ57ve_1wKfWx46HgTqUrOlqB_6Yr6spG4oAKatZfX7jnowWAgBs23nAyYDj5V11Yyore-0Pb_BJarQVQsJqN5qDoyYv6HYQ0YVRAU-Z7LyiUIIabIk0twvDR40j-Ej4EDp9kYMaRcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67451" target="_blank">📅 01:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG7QaG845zqQCM2K2J_MQ6iPDy9VubEG7IdHzrfUccy1k2DKtSpmtSzB4uH7Zdk6J2yqB13tEmhshsPgM2lFaTkeE1Yv-NDcdRqb8lzMuk9ayml7SgaZAeTraMxGZDG5iuubDsazWGLr20p15FHWSAGO-0IIKbfUSc9r844mxju3UB97nLO_a3lnra6K7LgaRPRJtkYuiHZLEpVOmn713nPPQZ0ok-Tko-gW6AykZH6Cqeh6pxYzw6nt3HY1hHFTU9DwGaPNrOcYmmBXbBXfHcuYRvVI9ZrtdPOk__qC2_70FFO7-3r-kWxE5xUNvcwqXlFvwGi69D7Jz1mb5U9ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه حمله آمریکا به یک اسکله‌.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67450" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuN5EcDBgfkBP-hK7B8IKpdfcMxVWkDqkDo4_OX-L-RQ9D8L0a--Yhi7lUijZ-3743xiFk6b-TMiJFmPtfDnDuEcAQHq2Nas_1_oa5zv0VOBoU04arZnLVp5titcYiobeoMAS4PpzxgOSTlITbbBzL1NfyIBeQS6ipd8ngWaQZtuOTKFfaZYxfeup7vmJR9HMvojkEdXHiv-zNITJp0c7RI0idXEbdoHSmdFY9kDj5PFlU2ARtFpbxxXvkfKowWI0EsA-uq3crJd9FSL6nT7Q64M_thStR3m3hheZVmO8GDrqkYNLZAh85rUfsKxlUBAoy39d2CKLWRfpGpHI_qrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری منتسب از سیریک هم اکنون
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67449" target="_blank">📅 01:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gi9DpAumRQcIRqvAjzYwVdVR4gZ4GBiHeMPOSjw4GP6fc1U1Ynrjma9yZYKuyiQp5TtICNV7xX5HLxn4iHUuHdP0dUpQtB3fBHMkre0tnF3DsSQcMYyHYvyPmgcOswwYLaxUnxPmpPNjndwUInd9UxtSMxn4j4tfT9oEEw1K32cOpKzlmm-KqguybERXB9aDw12UeIvffOo1LV69rR0wJtQeBLBD2kOEhE3dWHV80fRqIgsx5VGEU1_5SwV7Vyy-0-j4201O4XFog3z5BX-H92AHVKnV09YQ7vSmc4hnUv74WSkuOCSSLSHWlnuHEZMlggppissohbT6wEB_UCSPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسکله‌ی سیریک، شناورهای سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67448" target="_blank">📅 01:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQ3FxVA3m2eYKgH8_wSz53HH9zWj_0NgvJ3mBerWjDrJiuNhVAW0vHc_ZTGxuG2uRmg6RdKDb2GNmYXzm6u2tEhqXBXyX9AGidLAqMcYk-M4Xn0eVuYoH4waXMqdB2DViKgf1JjIil8tqzpMcDGJY0El3EOK0BMyT9bv-o74B5KJc5-EJQeYZdEzTuGS2-22Rvjhhu5hpJFoaF_VoIZjdvlMRkenVDJUo70NCglDAwfC1s6fQ1O5Q8P98PV91DdGkdeTLJjBAMtZLqHLzioTFbEuUmi1DN_qnMFSRvAuEJBwj4_GMEYaOlKiVtE5yJ98OZTyeJ7gYaZA9co-e99Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات جدید آمریکا به جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67447" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از هدف قرارگرفتن فرودگاه بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67446" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=fiL2oP1rYfvLSKgEJj4v-gdyaKaxS5KEcXphOwo1q0HehO2wNRdU0b_hTq6KnhIJr73_wuLS0wDo2lhd4IVA92A92rTpUniQImIomV1DzEA9Ps4z4z5htyfqDqNSxL8iemgOKmerEOeW8sgwWc7RGV0I1qV7M-nuz4vDU9Uz9T-eQc9vjVJ6LOcKW0Ru4YBMteftAcLwpwwtTwRawq8cc3NnwjdSTvWM_h2slHeU0fqCflC_CJzSRDwugVNPrF2ufiMpJqxM6OlTlKO2xVwTyS82A821qTfRIZ5PgUf6ZkVKzFQYDvqxsDYuEtuqVRs3AlnkUUnVjmVcrzOYKKgjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3287ab1c.mp4?token=fiL2oP1rYfvLSKgEJj4v-gdyaKaxS5KEcXphOwo1q0HehO2wNRdU0b_hTq6KnhIJr73_wuLS0wDo2lhd4IVA92A92rTpUniQImIomV1DzEA9Ps4z4z5htyfqDqNSxL8iemgOKmerEOeW8sgwWc7RGV0I1qV7M-nuz4vDU9Uz9T-eQc9vjVJ6LOcKW0Ru4YBMteftAcLwpwwtTwRawq8cc3NnwjdSTvWM_h2slHeU0fqCflC_CJzSRDwugVNPrF2ufiMpJqxM6OlTlKO2xVwTyS82A821qTfRIZ5PgUf6ZkVKzFQYDvqxsDYuEtuqVRs3AlnkUUnVjmVcrzOYKKgjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
جنگنده‌های اسرائیل حملاتی را در مناطق باراچیت و بیت یاحون، در جنوب لبنان، انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67445" target="_blank">📅 00:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67444">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ از ترکیه و بیخ گوش ایران، دستور حملات به ایران را صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67444" target="_blank">📅 00:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67443">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
حملات مجدد آمریکا به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67443" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67442">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz9FDfvQ2uh-yX_irp40wrf-Qse63rNRtlJWK7q8wnno4womMrcq1D6RUQxAK0XKJZJcddoRHRNIoeinjysU6HD3KAu6fh9QwmZXSnsAkSx2TyrcdUlK3NXwBYbo8Re7p1QzRsg62yKVkFBrpMrUwSqjpz7fVE6VTe_c4ac7dhRXntW_lND3XQ8vo4yi_IOR9HuNvRW5el_54PvSpqqLDHsuBD47clqlJw-beiZpxjGmwT46AzFCAmIMtVfqaCmZnSDUujq4kVJOflZ0TyIIiYEEJ6FBF3W1xpPKiJzozq5qaO1AmE9t-ImjXb87TL8BdvPXcd9gM2Xy_OnVCqi3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنند.
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67442" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67441">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووری
؛سنتکام هم حملات آمریکا به جنوب کشور رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67441" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با حملات آمریکا به جنوب ایران، حملات اسراییل به جنوب لبنان از سر گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67440" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67439" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67438" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67437" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=XhP7KrnVFTOgwbwZTliWtrpwk3lhoIfWcOjmgG0AtRKe4cVqoHOy-Ksln6vaw7ZCuU2FfSnC4POd6ArYJpkzU_woWCD4vWY9FJti9H6kEAWAcmZFZ0HLFXAxACFksekixrqZ75Jat7lxX-Wl95yOsbqkUUU_znQXvDDtXOfoSlr1uiMYqVnzznO5TL4jWgbT7wGMARDcRiPr74vpcr-Jcg59QKW0rQUSAnJuZNq9ENispAVglkaSBFcLlCigEk5ueXJZMnNnlw7cV2tJJUhB6scz1YlDCLLAQQ2jZCTRRgiaF3_QSn41f_pYetnBS9v5ltamzD8UPLBU043NTE4lDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7c257f2f.mp4?token=XhP7KrnVFTOgwbwZTliWtrpwk3lhoIfWcOjmgG0AtRKe4cVqoHOy-Ksln6vaw7ZCuU2FfSnC4POd6ArYJpkzU_woWCD4vWY9FJti9H6kEAWAcmZFZ0HLFXAxACFksekixrqZ75Jat7lxX-Wl95yOsbqkUUU_znQXvDDtXOfoSlr1uiMYqVnzznO5TL4jWgbT7wGMARDcRiPr74vpcr-Jcg59QKW0rQUSAnJuZNq9ENispAVglkaSBFcLlCigEk5ueXJZMnNnlw7cV2tJJUhB6scz1YlDCLLAQQ2jZCTRRgiaF3_QSn41f_pYetnBS9v5ltamzD8UPLBU043NTE4lDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های رنالد ریگان درباره جیمی کارتر و نقشی که در سقوط نظام شاهنشاهی ایران ایفا کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67436" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
مرگ ژوزف استالین و نمایش سه‌روزه جسد او در مسکو، اسفند1331
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67435" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67434">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLfMUgZog-S2a19_dbNjQooLwCjUoazCHdneG-xAb83tv6GJgP3MuSahvQm304HSQkYNgE1kPuc9YgR6B37ln7u4yQlgzPYUnNUDfi3wnx5MMU0EBiMjJFlbpwncfTAZMLrtkGDJrD6ywkSRLLS8z7IiK_2XSwX5Lbdz_oMZipy4w2PsRItGLWlqn4IT2GZMzqibOgcsSwMTX_nMlxfu6WA-xMrXnPMDxGqucEGl_6ozbI3CnJqldhf1cRjr66IkBJVpvLQCvqJgMz5F_Ei1weDErdkLp0InzfnRqp9nb9gqNBzleFdnMx_fCanRpbyWvJFZ3lk4waj2Ej0J_amX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا چخبره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67434" target="_blank">📅 23:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67433">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد».
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67433" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67432">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
طبق گزارش ها یک نفتکش بزرگ دیگر متعلق به امارات نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67432" target="_blank">📅 22:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67431">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzLyaImZaVdqXqrqOUg_Z1q0FDZh0Mo2Ko2I9wggTmfsZNelxwrEnfIia1p632CIKBejOJFrQq86rmzcDa3PVQfXgZLbD4HcEEZh1-5U_NxyQiprsvzPdKayoREke_1XjjXuikpa_ATFu054O4hOvbju4ADFWA-YOPas_so7BTLl_PN_kuls3jtVn9_iZGSwxGhf-nMco44637YrRMxnz81X1dVXaJ9b-gnAxksbo5QLLGMX-sCkzwdE-yvCB6_qKHa-34BeXoq0ofE4KSEj1QKAr1ZAXbACfl4yK_W4-luf5S2iP5AC_uYrooxkSeiCaBHUlulNcTxfwWyOkVob9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67431" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67430">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99630c1014.mp4?token=XsfHJ3gqm-5eIOJh-eHBAB8Y9KDPl-6EzmnsoNUWAzJ6iZicEb3Ug5EDOeilmPJVn9_V-ctHybPvjXqYElKxMOQJhpkU4O9giEsowIeyOCqSh4_8hu_iJQzgwmEXxKswJ3v_WJxnQEZZPwHttoJlw9bsQJdlIflJvGDpsS9uTafJT42_XAGLAvAOgdgErN6atETkcF5G57bCVwAO3cyBctdLexV2oDMyErfWj0IbKdSLJ4CTFfVkjevL6_FHxOLTjPCQknvW3O8vex9JRlTHEjNeIUVjcn4yrmIdgiUxWD_KAHf0i8ekY6ff7paNqnGhb8Yx21GCZjs4_MfKoJsh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99630c1014.mp4?token=XsfHJ3gqm-5eIOJh-eHBAB8Y9KDPl-6EzmnsoNUWAzJ6iZicEb3Ug5EDOeilmPJVn9_V-ctHybPvjXqYElKxMOQJhpkU4O9giEsowIeyOCqSh4_8hu_iJQzgwmEXxKswJ3v_WJxnQEZZPwHttoJlw9bsQJdlIflJvGDpsS9uTafJT42_XAGLAvAOgdgErN6atETkcF5G57bCVwAO3cyBctdLexV2oDMyErfWj0IbKdSLJ4CTFfVkjevL6_FHxOLTjPCQknvW3O8vex9JRlTHEjNeIUVjcn4yrmIdgiUxWD_KAHf0i8ekY6ff7paNqnGhb8Yx21GCZjs4_MfKoJsh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ترکیه:
من در واقع چندین بار با ترامپ درباره فروش جنگنده‌های اف-۳۵ به ترکیه صحبت کرده‌ام.
به نظر می‌رسد همه درک می‌کنند که علی‌رغم دوستی شخصی که رئیس‌جمهور ترامپ با اردوغان دارد، این موضوع ترکیه را به یک کشور دوستانه برای ایالات متحده تبدیل نمی‌کند.
برعکس، این یک رژیم است که با اخوان‌المسلمین آلوده شده است که از ایالات متحده متنفر است. او حماس، تروریست‌های حماس را پناه می‌دهد. از آن‌ها حمایت می‌کند. آن‌ها را تأمین مالی می‌کند.
اردوغان دقیقاً یک متحد الگویی برای ایالات متحده نیست. او نیمی از قبرس را اشغال کرده است، یک کشور ناتو دیگر (این یک کشور ناتو نیست).
اردوغان تهدید به نابودی کشور من، تنها کشور یهودی می‌کند. ما یک کشور مستقل هستیم و قصد داریم مستقل بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67430" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67429">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAXwNfIx20ZIk3OGumKc3ntCr4tIcODqKbIBKf3WCNioX89OTs5c5Ayf8A_enxucZYTObKskMO5LcXyZiW-WsSur0GuQlypdiOv_MP_N7yX_DHeeT9cTdDbMqr5JTQEFd4Y3JFGIhuL9KTXNsrjo7_X81GnBFNXvfL8uDZBPpKtiacS0qC4O-Bh3gMSkiwTu2KzeJgo1dooQigpmwSP10GcbwhUzC6QC7-V5oWN67SdjPBKZPxsLvsR9g0o2y_we8PeRWSuyAgjj2A5hOQSYxBEyv5CC3Mmuc2RN5rbzfQhDx8koNm6v49LEo2D9i2gdR5-d-YdPF-tf2jZr9MsdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه یه دختر ۱۸ ساله از فشار کنکور و امتحانات نهایی و بخاطر فشردگی امتحانات رگ خودشو زده و خودکشی کرده؛ این پیام رو هم قبل از خودکشی منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67429" target="_blank">📅 20:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67428">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJqcRKZf5uX7V8B8UZNPzzA9FTEhARvaQllsnYfcGvD7IBItgtRB0lcep0tMiBfajCKJB-2jhqMPDyDhpQwIAdWpmLY0Hrxg5WSx0YqouW__c0UDhrkx84SY05JGwPaCd6N7CtaPoCzUljHCXHEkmTVT55IBYP2JjsVmuIfuLtZu3ceq9_SOq4lye6I3MlVy_1jBN3VhEGjVcLmCFJGO_jMhLVm8ugmYIXhGL1kez1y1T_5_dYoc89MKRxMz7cLLNIn3huANyepWOClc69xLEZhAd34zcrF-lLRF9dT6lRQ1TnAlg9x_aQ_lJ021-y3fNplhuvYDgWsIcnQQ1Sw5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ان‌بی‌سی به نقل از یک مقام آمریکایی:
ایران شب گذشته با استفاده از دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67428" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSyZnB40LDvNvVZbexxUA7SyQ3fl8y_SLzqEsZQpe710IkYId5tM2w3UWMBi9LjUZwxz9Sed7HN7mdnPNSw-O3yKU8LQwZhkOA-4ZXUGJ_09xnpnGkQQp4ZvDmODsEypApn37cY2lCZMOPPTHq0NbiT4oiVzjqkddMPu02xI2p1VFocTQPTA93DmbJVwUcSvieBYJp6fEm6mw0MpxcLVHOF3TjE9d5ry5n9shAI32FaDlyISt1t0wDN71EgtSkaHU6ybZYd-8HXWJuvyaFulhJLPfUGtnefdrlZmLi3qgYQbOwyhMTtSUJXXK-m05Jk7008kUS7UMbCw2H34YymPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D551cLm8vOMgOj_P6PAnhJYq2WS1kLAZ2-E91qlOnGCV2w2sU4xLEYfxFQ8KSkFXk3l_Wm673yZ4Lk-w48S8MRyIItl_RBxkZjM-ZSW_eX77r-Sn1FWI2C8LUIR7QTtgjQsUaZI7TwrQGOyzB1j-o-D_lIKzK7z69VA_jgTpUnzfVDVjb2Z_xLPskNFyNL8bVPgiov_8qHyD9oVUNe9IDTbecxrGAPNu67tahd4lxsuIGYojQ-Dv0Q-rGxvfsSrdmBAOteD-xJN-ylc9YEYKKgeg98cOL283jEXEzzI7UqFR2bqETFF0yO5cifDw59DyoScRTPUjYC0x4bI7zB4t_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صدا و سیما این تصاویرو با زیرنویس جمعیت میلیونی مراسم تشییع منتشر کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67426" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=OdR9de04yA4M3MgCRm8GkWw0nE4wspd7LKsb451-DfJBNmU_5M0BpLipteCXyue78-b3-eXYU6AbrrQHSltM5AxCVOfUyUAYYRiA0xPSfVNOvXwnVt7uddYz0ijaQ1GTpu0PFkOlGyAot6PdGGggo0Rxbx9BpBMQqp4PfRrfLAyuWnQEBy_CiWOK52D4vgQLwWxPmkPX5Sd1g9xQ8A5D-aNY2uASTupx0xVRZlBXv7M9qIQMWNmDKfVHU_C1cdssmNncOhhe-WXSq39r6Bi2Omxl9qAf3sAOdLajbqKBOdddNpFBUljDBMwoxisqwrqjWrff_gvYtoQDHgCZL2Ru_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3431abb0e.mp4?token=OdR9de04yA4M3MgCRm8GkWw0nE4wspd7LKsb451-DfJBNmU_5M0BpLipteCXyue78-b3-eXYU6AbrrQHSltM5AxCVOfUyUAYYRiA0xPSfVNOvXwnVt7uddYz0ijaQ1GTpu0PFkOlGyAot6PdGGggo0Rxbx9BpBMQqp4PfRrfLAyuWnQEBy_CiWOK52D4vgQLwWxPmkPX5Sd1g9xQ8A5D-aNY2uASTupx0xVRZlBXv7M9qIQMWNmDKfVHU_C1cdssmNncOhhe-WXSq39r6Bi2Omxl9qAf3sAOdLajbqKBOdddNpFBUljDBMwoxisqwrqjWrff_gvYtoQDHgCZL2Ru_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی، تحلیلگر سیاسی و فرزند یحیی رحیم صفوی، از فرماندهان سپاه پاسداران و مشاور ارشد رهبر جمهوری اسلامی:
🔴
دلیل اصلی ناکامی جمهوری اسلامی در دستیابی به اهداف هسته‌ای «برتری اطلاعاتی طرف مقابل» است و مسئله اصلی، نداشتن بمب اتم نیست، بلکه ناتوانی در حفظ محرمانگی و پیشبرد برنامه‌ها است.
🔴
برنامه هسته‌ای جمهوری اسلامی یکی از پرهزینه‌ترین پروژه‌های هسته‌ای جهان است که این برنامه «نه به تولید برق منجر شده، نه به ساخت سلاح هسته‌ای و نه به کسب مشروعیت برای حکومت».
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67425" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhB6aeDmHY7GLF61-c3RLo2GzihUc6ZeKdkhFIZdiuLKg-L0sL_vCdmjJZFRQlzhLKmvpCWqf-ojZ4chSziCR7fuX0A8Etadzi46UG8kBQEHc3CzDk61LsfQK3drZFoymbQ0Q_Ejv8pAku9_yfE1LpPpvxun9GQb17Ctvk5rQ6IEzind9POw3dSI1TQwp78jP-NhiQJEGSaHm-W7_zDlY-r54G4VXhz64HLZLN8aFddzpFPT9XHyqIXBj8wydKeNr--OWdV89sn1oMDX5au2RTyEPscXdgcvLoqP-XWrN9yBGDxmTKyKla9IHwPouh_9nkwzguASZU1zwb59rkA9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67424" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67423">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=bMRgxdLR3zrLSXj4GoYhMBJt7EKwJlEVpxaXmapRmeLRz8bQKMxvz8LNQ-mflk-hJCfTpMnB2_d2JUqX_VgQEPnbo0lSjGhrzEIhu-Gw_OeQAWXUPkRKjtAAPFylzqIotoFs_vIFEafYX1ROSGn17cxJys6hT-j5IzaWBx1P3if7tMr0mL0uVWCqVjCOsCn-CqLq8-QklURwlFuC3_4piKW3fAgd014PyOoLzxT7MJIZ3QSVgCgjAcXu1zVafNtfYtLlh8BFChig476UHr9ktKM1IC76TnDi8SKKy0pD5Y2byT1eATaPuV8pu4BjDiqfhVk0pSRBwcMhIOz0LZDTZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07aeb18ec.mp4?token=bMRgxdLR3zrLSXj4GoYhMBJt7EKwJlEVpxaXmapRmeLRz8bQKMxvz8LNQ-mflk-hJCfTpMnB2_d2JUqX_VgQEPnbo0lSjGhrzEIhu-Gw_OeQAWXUPkRKjtAAPFylzqIotoFs_vIFEafYX1ROSGn17cxJys6hT-j5IzaWBx1P3if7tMr0mL0uVWCqVjCOsCn-CqLq8-QklURwlFuC3_4piKW3fAgd014PyOoLzxT7MJIZ3QSVgCgjAcXu1zVafNtfYtLlh8BFChig476UHr9ktKM1IC76TnDi8SKKy0pD5Y2byT1eATaPuV8pu4BjDiqfhVk0pSRBwcMhIOz0LZDTZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تندروها عباسو گیر اوردن دارن بهش اشیا پرتاب میکنن و بهش میگن بی شرف
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67423" target="_blank">📅 17:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67422">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=QWSiUZqj8XO4RiM41LBuhyV_VAhcBGS38yVvml3tequqe0WvhWEI8pJvl_4T5Dy8dvnN3zsU08hlJqyG-W3aM-iuIqJOwtVVCbqr8MA27SOez_Nxjjw9vHYtvh2g8AxAQMXsObrnW8-mEbosB-72Pkb-V3ujPKC9B6yOeCoBzgo81S26O2KlBju5POrRQqTnUrn_HVhe10B45LaORARVhkWxbhf8olpBiU8mSEE8FFnryWNNVJcvJsQ3wtMxGmZKd42AGPqgp6JJZxkwSjC6XhStUlhJctTFPPHXLwx9hh1VgCGcHhfNVPWFcnz-YfsnzO9Q7sFZBeSQuPQhKtXBd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f260072fd0.mp4?token=QWSiUZqj8XO4RiM41LBuhyV_VAhcBGS38yVvml3tequqe0WvhWEI8pJvl_4T5Dy8dvnN3zsU08hlJqyG-W3aM-iuIqJOwtVVCbqr8MA27SOez_Nxjjw9vHYtvh2g8AxAQMXsObrnW8-mEbosB-72Pkb-V3ujPKC9B6yOeCoBzgo81S26O2KlBju5POrRQqTnUrn_HVhe10B45LaORARVhkWxbhf8olpBiU8mSEE8FFnryWNNVJcvJsQ3wtMxGmZKd42AGPqgp6JJZxkwSjC6XhStUlhJctTFPPHXLwx9hh1VgCGcHhfNVPWFcnz-YfsnzO9Q7sFZBeSQuPQhKtXBd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توضیحات واعظ موسوی فردی که تصویرش به اشتباه به اسم مجتبی خامنه‌ای در فضای مجازی وایرال شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67422" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67421">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=MX2Wmt2xI6c8DH0nU4W9iBKCue97VQ7VvF9JV275i6lNXKJSAwuDXq4TF6pVJFYb6zW43VqXElVZmxHUDhH0Xw8_6p_VGfFVxwxQ4Wg8RsLzOhSJdixix00K3ptmad-kEd5Z0HItSEk8VU1ST7axbHnCN9cPKeJqCdj5csEF6CkvB4T5wj69YP0uZ7kfO-_HYtCYw3H76T40Ig1UK_N1Fs08XFXfjWNqQAdFJa97_Tk7IQwPxuOFFMG4mVVINkTjfN7Cl_XSIm-2knM4oE1aUhy8RNLrzgGM_ijgWbJGUsvDJrrOdODS8NoeqtI0SGpAZ0ul2uSlEdu91q6qSp514Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6696a22a99.mp4?token=MX2Wmt2xI6c8DH0nU4W9iBKCue97VQ7VvF9JV275i6lNXKJSAwuDXq4TF6pVJFYb6zW43VqXElVZmxHUDhH0Xw8_6p_VGfFVxwxQ4Wg8RsLzOhSJdixix00K3ptmad-kEd5Z0HItSEk8VU1ST7axbHnCN9cPKeJqCdj5csEF6CkvB4T5wj69YP0uZ7kfO-_HYtCYw3H76T40Ig1UK_N1Fs08XFXfjWNqQAdFJa97_Tk7IQwPxuOFFMG4mVVINkTjfN7Cl_XSIm-2knM4oE1aUhy8RNLrzgGM_ijgWbJGUsvDJrrOdODS8NoeqtI0SGpAZ0ul2uSlEdu91q6qSp514Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های اخیر علیرضا فغانی از ظلم‌هایی که فدراسیون فوتبال در حق او انجام داده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67421" target="_blank">📅 16:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67420">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ51SBsV7pa71gfT7clILG1FVAznR9Ya0mBvzFvilaaOwMqeJRgvDQ52FZXR1nz3K96dQtTrz7xu6t3OX1eIAQIj8Dg5L_o2dAQ7wChpKp0mcPFbmbhlHlA7ulzcCRL-zv6Q8KwzXjS2zuQ9w76igreIHLNksnLtPZnF4jLHD-mQCPFDn58GyS8R1VnnZ4XKFv3WM3TwSGjR-eBeEEr2_oBK59fIjXIU5jRYdKAR26zIdrxw_0ZaRbqCzZNd4tt5zFOwkoAacxTWGKpU9mXGZBOPqUi5mi_lPcijTLK7bob8UzgAf8jobhPATNWKkFpC_SYeG7ExlAzW-ZsignsyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری
CBS:
علیرضا فغانی قضاوت فینال جام جهانی 2026را بر عهده خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67420" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67419">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=PyFmTLPHivoVedjUwBtM_jQosLK6JCl2524LosX4N4iOWF7b3hIkwO17jCQdWByUVeH-oq2S5UczFX9ASuI6zJfi3jxy4U4L9fZ_44bLeDmYto9Me4YxnUnpclUqf9wm1wu_9IPGv3nmo93GMVDpv_Noe8KSmsJI8cNpdWjQQ-Woc8WhuV0tlE6qA-16KyiEsN95ixSuQVij7j94ydGXOlQifmyYDX6My0cON09vAN5pp2P41QQ_OgIwWLCGrK4EMBSyxPhHzAV9rhBrjk59PT-SrRan78Fx2JfSqjoI-ifTN7C1C0fE3Z4DugQbx-iUC0JVGSIP-w-LZuGNHpwsXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca7d1936.mp4?token=PyFmTLPHivoVedjUwBtM_jQosLK6JCl2524LosX4N4iOWF7b3hIkwO17jCQdWByUVeH-oq2S5UczFX9ASuI6zJfi3jxy4U4L9fZ_44bLeDmYto9Me4YxnUnpclUqf9wm1wu_9IPGv3nmo93GMVDpv_Noe8KSmsJI8cNpdWjQQ-Woc8WhuV0tlE6qA-16KyiEsN95ixSuQVij7j94ydGXOlQifmyYDX6My0cON09vAN5pp2P41QQ_OgIwWLCGrK4EMBSyxPhHzAV9rhBrjk59PT-SrRan78Fx2JfSqjoI-ifTN7C1C0fE3Z4DugQbx-iUC0JVGSIP-w-LZuGNHpwsXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ برای شرکت در نشست ناتو وارد آنکارا پایتخت ترکیه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67419" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp8UbOgkxoKsvfgs9gyAYYTbUC6Nedv8FhGDl47QaDxTMuEo8X81Xta8BO95qEOZkVYoZXoxz7SKZPtECDYTeOKBTepmBwXJ_rFWFKB9ub7ZGl1iZ5s9IFoO3mDBqscIoUbqqwWX9oGbHjcPUj3xGSzD5Y3LnlPd9sPbn-Doe4B0JTdgmeSwM6Nns0eZqiZbm3V3j7l6YgyaWQM6P3Ku3LyEnMg1Oz3bskhHUBD-7iqPX5cIPAht_7HqeTMBc4ZqFm8JgF3O3d-dvhRvktO_LE88oc9nZWwRGcT2JXFtSUNzBasvaD9OzphMQ6HGo9TSY5ae_OjcSvReCIweB-89Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acF7Y_W64z4sM6jsMbBIdDSdIeuuv9WHY9ijwrwjVp7D2xewLBsYmtDrtJodIha16kps1NDAEBwn__87Obzep-qkSubQRRqCVG8JKmB9XUJ46W0SkR-9daAiR5UVLZaUtctSGRfh5fjX8Qi5OOXOs79IT6kdW-ZXqw8XwW65JTN57qafVsIa8A9EKUcZ40tqyUFPyEbK78X-Yl0Jz7biEm_PtpYBhYmB-WUNiBs7z82lBiAGZebaeljPs1KduL3N9ctXg4jUlTPJ63WBpfPIigrBKJkdiT04l7QMWFS2kQ_SBHwcBwPRKWI4uIn9-VE53HJ2bBjvzgJM-vHL4koBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=AEOEsLsxOIrh9GcDsNwAH_yzkTJ-O4hF5WqKJuzahz3upBsjhEbDC7O3hrELtC25XXK026E7iuLr_ixqTa3y0H23e5K2Z2YuZdVVTtuEp4YCwr8OscHfilBJzYCVSyWJzA6PNHaprgO8d8AY5sKAzkgYc029aGxp60S8sD4XABjgF5ZBAokNMClIJDo0tje0ZGqIa-VqtMF7LnGNInIFnhfjQgpfnJ3iT8_nNqp2ucbP8KOU5I2ueqUcgGzokKVfrnWUcyKvee3ieehcUxUiSwgzDNrZg3RU7RHwaSr4805QjX13gXC8lDbtWMOyX6UE_oV5n_QHiuLiqDDWA5JZ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=AEOEsLsxOIrh9GcDsNwAH_yzkTJ-O4hF5WqKJuzahz3upBsjhEbDC7O3hrELtC25XXK026E7iuLr_ixqTa3y0H23e5K2Z2YuZdVVTtuEp4YCwr8OscHfilBJzYCVSyWJzA6PNHaprgO8d8AY5sKAzkgYc029aGxp60S8sD4XABjgF5ZBAokNMClIJDo0tje0ZGqIa-VqtMF7LnGNInIFnhfjQgpfnJ3iT8_nNqp2ucbP8KOU5I2ueqUcgGzokKVfrnWUcyKvee3ieehcUxUiSwgzDNrZg3RU7RHwaSr4805QjX13gXC8lDbtWMOyX6UE_oV5n_QHiuLiqDDWA5JZ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=ZKGya88mOgocS303B95C99dzAbzuIX3x0qakR86IeCNaCGIUllznYJUPgjMP614pjUrdDsCz7K1i6YiJFmJE_JSh-4eulXwE8C87RKcCIisEqrUK6ssjrsbEODmFm8nIinsN8gL8o5EAWTbS0TrrNZcJf4hRO6qGZzSgIYziGhqlDJRaALwGD4lcIlNcjFp7UQE41rRR952usblpJXkDsMBNV8LJTHzUctnpplBAW4NpjzC3_ukpihZc_qZ3UJe71ok6afVY7-u3a-MCyR7yHUEir42hqQZ_Au--XEWzprIiF2BVh_ZcjA5KXOmXHgh8LO6Ca0DrbY3jI9i2URZrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=ZKGya88mOgocS303B95C99dzAbzuIX3x0qakR86IeCNaCGIUllznYJUPgjMP614pjUrdDsCz7K1i6YiJFmJE_JSh-4eulXwE8C87RKcCIisEqrUK6ssjrsbEODmFm8nIinsN8gL8o5EAWTbS0TrrNZcJf4hRO6qGZzSgIYziGhqlDJRaALwGD4lcIlNcjFp7UQE41rRR952usblpJXkDsMBNV8LJTHzUctnpplBAW4NpjzC3_ukpihZc_qZ3UJe71ok6afVY7-u3a-MCyR7yHUEir42hqQZ_Au--XEWzprIiF2BVh_ZcjA5KXOmXHgh8LO6Ca0DrbY3jI9i2URZrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=YQAtECl2uUsvHXZaMGDYtPmPBHcSX-_35NW7CFdGN-eh-iSUlq8I6zM2ZtFfvngGZZNpR2ZMDdwkIvHSDmz_iALn4o5_m5JHjhH3ngfnppF0SwSVqOYtubueKxGiSF88jHP-XmyY3eXmjxxtSHOtZD-pBTTXxaJ3TUoCHMZVe66NmIe8jiw8Mm8oAfq0pD6f2SFb8QtLNUSK7hVGZLXTK0ZTdcPO36sQaDpH8P3swMNbNyf5yceW5YW6-4674qD193ZGhaAVC89iTCTspyfc8aKCjfOC83N13PeLTHvpvtlGHjVo4B23teaSHjqi_MMKfE7Xx1J2vXmkYUrRg0noAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=YQAtECl2uUsvHXZaMGDYtPmPBHcSX-_35NW7CFdGN-eh-iSUlq8I6zM2ZtFfvngGZZNpR2ZMDdwkIvHSDmz_iALn4o5_m5JHjhH3ngfnppF0SwSVqOYtubueKxGiSF88jHP-XmyY3eXmjxxtSHOtZD-pBTTXxaJ3TUoCHMZVe66NmIe8jiw8Mm8oAfq0pD6f2SFb8QtLNUSK7hVGZLXTK0ZTdcPO36sQaDpH8P3swMNbNyf5yceW5YW6-4674qD193ZGhaAVC89iTCTspyfc8aKCjfOC83N13PeLTHvpvtlGHjVo4B23teaSHjqi_MMKfE7Xx1J2vXmkYUrRg0noAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEHI1Q_q5zbwzfMf0QG5PoSI9c3cI0zsAMPzytHM_eFZFxY0bjCXsVDg4dSDUcpNFaGveagr9ATYHcC_z_5Aq4-fOz5NLCTxEGJ5GZYlVMeyZL-Sx_J1aIxVFzxoQlg6RAwzUpnBzTMuxd7tRIEUKzS00PmhE2gnd590gq4eQ-ewnEvk1wb0VndckCYXOrEaMIC0TI_vQvNjBf4Wj9vJP7ZX29o9sT-UF84ZA2ekQdMJn4LN_aeh_uPF7U8tvGJuEsDp6-1oSC1pQDd5fE5ak-tvM6T_FUS-hCrr5ibzFVeEMf1WMd6lX8kRKjkN1jxmesO03_06ukYkRIU1ws2Cgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=fUKEA2uVp0T_gxjcLlCHzLTxxbmwsjEEsd1aMzHg4zPSjkAnBKjJX6FWmTmqP2nwb8HxkFbwL_FzSCyubZd7Kjnm7u0B0LO67QCv7cBHH2md2LgpBsppvUie0s9R0pNgWnF4qSt1iPfx3U0_GWhJcSfH3UkSDRQpzrAOmo7PQScV0a80kLgnmClkS77u4sbprYHi4q39IcqX0qbyzQJ4CwA3HzIqihKFvFaSluVQtLIvC8hlxtTFhZGtQwxYlfMUO-GnT89dz5YfBI1_V5CdTAP3KC0k2t2twjzA9bRi-7DSyH01kYlkixEBczZ-pdEwJecFqJKdouT5lMcbhDDvUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=fUKEA2uVp0T_gxjcLlCHzLTxxbmwsjEEsd1aMzHg4zPSjkAnBKjJX6FWmTmqP2nwb8HxkFbwL_FzSCyubZd7Kjnm7u0B0LO67QCv7cBHH2md2LgpBsppvUie0s9R0pNgWnF4qSt1iPfx3U0_GWhJcSfH3UkSDRQpzrAOmo7PQScV0a80kLgnmClkS77u4sbprYHi4q39IcqX0qbyzQJ4CwA3HzIqihKFvFaSluVQtLIvC8hlxtTFhZGtQwxYlfMUO-GnT89dz5YfBI1_V5CdTAP3KC0k2t2twjzA9bRi-7DSyH01kYlkixEBczZ-pdEwJecFqJKdouT5lMcbhDDvUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=pZwF-_uKhOxJ5L-rgHaPhvt307R4qBcTUpMp1rObAAxKgfNfLTNKjCS41etotEbv7-646eX1TqfueYodNUr47NrXmwXcGP70CRUmpOTqbt5M-CV9sT5XqQHQlGLxLpMjL8nulPBDr_IovTCnbpct4XIOqkwLSCSVOQcg3ceuc14h1akIkBsAIpNQiPj8aw35WnE9DjDlxK__Cg3ams-ewv-fA2oWbbytg3wO0fcUsNp_lFFlWCmPsWye0WrFJ77CXCyrRw9YORU31BaoQJq3cdz8U9Q4ABqWzZ-FufUniQW7fN-yuso09VgT4w5c8XM8dw9mMx_JxQRSmsOBXZZRvgE0oyOtZQFiOvVANhy26ec0740yQvheKD0OaxRpYUqZs-x6Z20fuAtI2WDNvYHDFjv4yNDU6eN6iD2xbzI3g9Z8I0b0Nsfp4oAVhoBgvGrZBi67JiTcPo3B0ifY2kf2pa-ITTMfFzzjILvMhwMo9nu73cTkivAtUZk6LnoazrM1yaqKL6yUn7Ee-fQ25ZOQAGY4cL1JGqYBVixairNrXBEUo3pEngJhSVueaHmBnhJzFlDldw3HC_6OxBDuzB9e4wr8U7hIoTMF2t3hMOGjh6Rvm0DtQ1XRCSnx2l-xPMXUk93CkhykJkJ55PyRXeVOH1DaIO3vjOhHRlRffapqWxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=pZwF-_uKhOxJ5L-rgHaPhvt307R4qBcTUpMp1rObAAxKgfNfLTNKjCS41etotEbv7-646eX1TqfueYodNUr47NrXmwXcGP70CRUmpOTqbt5M-CV9sT5XqQHQlGLxLpMjL8nulPBDr_IovTCnbpct4XIOqkwLSCSVOQcg3ceuc14h1akIkBsAIpNQiPj8aw35WnE9DjDlxK__Cg3ams-ewv-fA2oWbbytg3wO0fcUsNp_lFFlWCmPsWye0WrFJ77CXCyrRw9YORU31BaoQJq3cdz8U9Q4ABqWzZ-FufUniQW7fN-yuso09VgT4w5c8XM8dw9mMx_JxQRSmsOBXZZRvgE0oyOtZQFiOvVANhy26ec0740yQvheKD0OaxRpYUqZs-x6Z20fuAtI2WDNvYHDFjv4yNDU6eN6iD2xbzI3g9Z8I0b0Nsfp4oAVhoBgvGrZBi67JiTcPo3B0ifY2kf2pa-ITTMfFzzjILvMhwMo9nu73cTkivAtUZk6LnoazrM1yaqKL6yUn7Ee-fQ25ZOQAGY4cL1JGqYBVixairNrXBEUo3pEngJhSVueaHmBnhJzFlDldw3HC_6OxBDuzB9e4wr8U7hIoTMF2t3hMOGjh6Rvm0DtQ1XRCSnx2l-xPMXUk93CkhykJkJ55PyRXeVOH1DaIO3vjOhHRlRffapqWxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=Olz6T4y6mw7IUE9_tK9IeFoxi5N4smkhGdk65Nq5fD4bfL6i0klFmLHZgELofYFrODioVk6ogO2Euzd4jv8AdLCByGUUYyWX-eezf4Z_EOmRqp2aLvjPOr834AS41CdCqd4KZ2_9FHKXK9L2sKsPn0biWOLOh6aw4DiXIXbY0mjQK3TqXgMgX4AWdkJPVSf4GT91-1wWid_hIpYG1kdL8UrWaDsu5-IWJ6eyijlg4gsGASbzZt53ZgfvDhK7ef6XEorArP2qFDkEOAKDi39XBJuDffpse4GaGEKD0RuDZQpkbBYa0X-2cV8jYXh7g85BuKIoJNI9AiwO1r7xv2YsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=Olz6T4y6mw7IUE9_tK9IeFoxi5N4smkhGdk65Nq5fD4bfL6i0klFmLHZgELofYFrODioVk6ogO2Euzd4jv8AdLCByGUUYyWX-eezf4Z_EOmRqp2aLvjPOr834AS41CdCqd4KZ2_9FHKXK9L2sKsPn0biWOLOh6aw4DiXIXbY0mjQK3TqXgMgX4AWdkJPVSf4GT91-1wWid_hIpYG1kdL8UrWaDsu5-IWJ6eyijlg4gsGASbzZt53ZgfvDhK7ef6XEorArP2qFDkEOAKDi39XBJuDffpse4GaGEKD0RuDZQpkbBYa0X-2cV8jYXh7g85BuKIoJNI9AiwO1r7xv2YsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnQN4mlAm7l64me1xUwEkzXIo8Vz9sFGqWTjlQ_eOUYvLhFdiQWPJLZxsM8EZD3yVKbr0eTyeNp7MCRQrQc1skfNggxrB_ge3B4ip2OVyAyqBnc7Ac8zfBW9fKUctCpD5qkk3KyL7Pk6qIKoY-9kldvU0tH80beFCln5PE5qdtC2lXFvrT9SRNml2fx2nSGRVeTdhfoyDCjRJTzw7QrIRqNCWLlMMfK1J4q8iWvujRCg8c4qxYA8MIOx5np-w_JeVk2oDn131umRtiWOhrRZiR5OSwDWyaoJINMaRDh49T10k30cgGZTd5NXKU_PEHavU6GglBhRsY74ULmr6OyNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
