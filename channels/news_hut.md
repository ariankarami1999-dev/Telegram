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
<img src="https://cdn4.telesco.pe/file/jA0K8baJmMmMnPAfSP4H0MiMvLrasszTqdjZK5FYaHDGOOxHBYPwS88mWIkKOR9-cK3bJJJoMstjYhcz7s0r0l9PkuF6EuHXNwB9KXAp1SalohM8fj_Q8bSCu1KQaSxvKD2R_PeoluWq78D8rLBkU0T6m8AGo10pPdD6zoI-EgaqSA_LtMREWJpPr88mvxUaMnj6nN_OBZoBx8oUMr9OZeeubnPKo0lBXrHfERNrh_SMEVxNrMfXu9gvJfwqi8vD06YLx-piszm5F5hyZYy2bUqBMR7lKf8x9NMjYdKZxc3RYrYAld704pLKb4BjEgaOt1HC62tm3tG4U_o8HYK0qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 110K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh77uiDscwS5cFtxaX2vW6VHB4BwhI3-BY_7Pcnv4MHZO8HO3YKOp8hj-RQblogz3TjPXUe4GO9LG36H2W_n1x_LUqULZmBwVkiJVuYEHDM6FCFw82xtjt5CSiRbZKHuLFxxcTLoznjdrMHRtgtaFtLPgPdp0R9_Tr9qkuPQJg2HWAih2EIhrnmA-RurdL6tVxz3M2R1LVGfNNDjujKanHIhKo5u5bcSTCpYowa5Om8K6DrgF24d9ZrW8c9_wbRMT_r8VRldq66MSzXj3aA8iZWMDaqkSZF5sqpXLRQz6m7fLJGWhjPy08QILLmJTzLBOJdIn4Ntktimx87AwltJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 246 · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsXG0WlGe3znJbIqCF_brXEoPVyBT2lzLNyxUd8gsnPJZ-cICprOAoYb7OJLvlyRKQQwQWDoIS90bf2z3vyUdKFI9_12q8FbYpFL4SV5Sha-N_Nd2yIzio5Y0WTE-wxmdfe9Qod5bGTG5iHotjVEV67DhPTx6x5euwub1XvY8RPGaXqGkbC0gjR0Ug1dHqzjYicNc1JCo20aF3_73H72cBJt_E2d8SxiKbaEyWmiaqnUZY4N9e2qZf09GOU-MIsgZRvlJUttZLAuXX1ut0xGL6e3_EXAggbPlCphKEjor4KwFN_AFmag-Vk1S5JnvhBpoBfd8WOe1bXS3vVoROriXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrDuqbNKLXhqc_lrNr75EoRL8zoozDnj40LIESNF1I3yOIGihs8UG_GOWHcmna531c8Dc7HZdc8xScUrJ15MthMrIRntZiVaOVhzV1RSdv-JC3k9aWKE1w5X6Bz33IDy5eCjITCxS7WlsjGhqRmoHNcBfnBhOw42Oe_ME8ltCc01MkNu7239lW1_MCWfpPdUF4buJyqlPM3amg5aqGK3diov9bpgnTJargefKsJv0Z4w5qoYNIOikCWIixFlhT4ROakV4cUbE-BbDy6TjJ2Fl3WOwK3vW95TujRHMDMZnzNl2UAIfOdTKVxxei8_suOrUOLn6mXF4PqOevaKOiWp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=gzXkjx259SgSV9tABWZdtKPB-MEOrmjFakibXeTIdysti-Ao9SiZh-lm6xoPVunsZmKhQ6TxcsUhD-iqynqOQ1L6Ue_O3u1gRMTCuzRl8B1WEQ2hOuOK07Sa-Xz3w--OouuF_wIj_EecOEwCPoNWzJcLxUdaq9Siy-667iSrEAfa6RIqOCxYYEo6zyLwt2Uu_rCnAwp7PmdSClsh00lZwSjUbKGcsa3CeFwaTvWWMc-SwTnoDRXFc3xhClGUhI_9B-pRfz92WcoVBMg13B7hWj9bOfJ3dT8BUN2agZMd6q3BqfAG7U1g96hWi3zISrocigKgJFoMYazkS7Ql7Jugwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=gzXkjx259SgSV9tABWZdtKPB-MEOrmjFakibXeTIdysti-Ao9SiZh-lm6xoPVunsZmKhQ6TxcsUhD-iqynqOQ1L6Ue_O3u1gRMTCuzRl8B1WEQ2hOuOK07Sa-Xz3w--OouuF_wIj_EecOEwCPoNWzJcLxUdaq9Siy-667iSrEAfa6RIqOCxYYEo6zyLwt2Uu_rCnAwp7PmdSClsh00lZwSjUbKGcsa3CeFwaTvWWMc-SwTnoDRXFc3xhClGUhI_9B-pRfz92WcoVBMg13B7hWj9bOfJ3dT8BUN2agZMd6q3BqfAG7U1g96hWi3zISrocigKgJFoMYazkS7Ql7Jugwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=IA9zrriYkZQ2e5AQ0dvjWtlXeYVndl5jEZKqVlIHH2rCRhF5GWAFaIsNVO7vA5fmUsFJ_qaS9j14vx5wEj0wh11Z2OdNxUMxtnmwvFkfB9zhSJxWi-LzNCVS3xZWF7V05bJdUbq0WBPArd43I-NBfc3EwWxSwJ2lBIktEVJ3ZBRYb1kQAB_u2LKEFNKk9KKeuW16fEVYsOXiziuRjzAi-6W_OZqiqe07bB73gO3Xwrr9jsaM393mKMI_w7PfaZ9VlY9pQliknhy0sKdA4fJKGn0Cks5ASY-wwzmIxGE0ytu-jpivE5CHb-mH0Do_UrPIhTudnTZB3y4Fb9Tv7C_WFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=IA9zrriYkZQ2e5AQ0dvjWtlXeYVndl5jEZKqVlIHH2rCRhF5GWAFaIsNVO7vA5fmUsFJ_qaS9j14vx5wEj0wh11Z2OdNxUMxtnmwvFkfB9zhSJxWi-LzNCVS3xZWF7V05bJdUbq0WBPArd43I-NBfc3EwWxSwJ2lBIktEVJ3ZBRYb1kQAB_u2LKEFNKk9KKeuW16fEVYsOXiziuRjzAi-6W_OZqiqe07bB73gO3Xwrr9jsaM393mKMI_w7PfaZ9VlY9pQliknhy0sKdA4fJKGn0Cks5ASY-wwzmIxGE0ytu-jpivE5CHb-mH0Do_UrPIhTudnTZB3y4Fb9Tv7C_WFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Uxnb51uYJVlRK1DRd4RMbLem4s8pGWkLCTG0jsqaLdkKbCHSqBpe-cyZrENcZRBalm6NBu9jFF1dEN70ikseXD-6nAWPPaaK1cyVPe_aPsVRtDT25wo5lfElr0wJBzjagXCWI1xPMza3B6GjOoFDKClmS0301aifk47oKE72mz1IE0WRVnHShIc-ldWrOJSuMyj--btBbsOXrIbqHXAFHhFu6i4fiS_K6oLUiNd-dY7RE-0CN41h8bORbGJeeilfB36Pkkugfcj3Aks6KRCkP8OdJb2UQf5hntKBriMZ9x6NiTEg5_-0s_BLW8spxTCQnQyUhduIL_q-kVcCSiWwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Uxnb51uYJVlRK1DRd4RMbLem4s8pGWkLCTG0jsqaLdkKbCHSqBpe-cyZrENcZRBalm6NBu9jFF1dEN70ikseXD-6nAWPPaaK1cyVPe_aPsVRtDT25wo5lfElr0wJBzjagXCWI1xPMza3B6GjOoFDKClmS0301aifk47oKE72mz1IE0WRVnHShIc-ldWrOJSuMyj--btBbsOXrIbqHXAFHhFu6i4fiS_K6oLUiNd-dY7RE-0CN41h8bORbGJeeilfB36Pkkugfcj3Aks6KRCkP8OdJb2UQf5hntKBriMZ9x6NiTEg5_-0s_BLW8spxTCQnQyUhduIL_q-kVcCSiWwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oXLinVcZbyZVgwtMiP55Okrtg0cEnUvyikaDz0lM1HdCbIUpgZZc2Zw1vJIsrsDyMyyVAtTJl8LoIrGnFubAPX5jCRdgZO7Eya5eoGKbD5nbYPOGqVaCEC2Wm19mn_xERVoMAvB32f7KuKvrN3ens4INCA1VeZ5vip6x9tkMTdDvG6vf7LHJUKV_OvaiQgeGha89wAwZka4dC1r56--JsHuuANJELHK7BV5C1sPqdWADdegBUXTKyHKVGvb62pc_37X3Gj--Y3CShO16Yl9IpALUBLs7uN2Z_pC2UJjhggF7zAZ16CjEFJiYNGw0MrXTT-jX_EBIVGZzY0AqJ_V8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oXLinVcZbyZVgwtMiP55Okrtg0cEnUvyikaDz0lM1HdCbIUpgZZc2Zw1vJIsrsDyMyyVAtTJl8LoIrGnFubAPX5jCRdgZO7Eya5eoGKbD5nbYPOGqVaCEC2Wm19mn_xERVoMAvB32f7KuKvrN3ens4INCA1VeZ5vip6x9tkMTdDvG6vf7LHJUKV_OvaiQgeGha89wAwZka4dC1r56--JsHuuANJELHK7BV5C1sPqdWADdegBUXTKyHKVGvb62pc_37X3Gj--Y3CShO16Yl9IpALUBLs7uN2Z_pC2UJjhggF7zAZ16CjEFJiYNGw0MrXTT-jX_EBIVGZzY0AqJ_V8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVMzAd4wSGjRJaHpN08c8w7YQnsN2-b0OGS8O2P0JxIOihaFls_y7MqXGzPqiHXtBx4F9QtC0t0qb2DBB0QMoHvztPDC9xNYuiKU1t7C_AUTZc0_0jXIOeFjCtJI0grCYyj_aRgTj9UsUodsOFVRnFQEu0FkRLP3Yli7HQbNvgaGRHhzYVpHxzRT58PMMuK1qp9TJFZ3HUz7iNGFYxo4VctbgZhkna3MpccbCGKgS0zljflIMX-GFqLsxQzEkUHxrcMy8HBSWeJ14My6Ar-g9fQ3J0yyIj0O57kaM7QhQoWASy479YOc10rTy_Ur6PqecovXRiTGrciWWuymrMDcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIDmMeufIKXNZ8R4XIz80JcYf863dpoC_D4fcDI8Lgw9Li3ldwM6GDJjELsjsXZYxu7SOSFCGT_mWNgKoOUOu8AqBK-nBHDHt9AKW0Guhv9UUV_oqKf98mHytoRg1zZoaoJLpAwWYJO6omdZICf6vHyuHgpeLM4mHG_BchmrAh1fVRcPcyyQfm4tn_vM0qiRIgbwWHS1RcFQ8OCkZ_2xgdSrdW6gHdGXZsz4xZywUb6zILa8KWdWu3sLq2AVHcm69f8xHzDHW3kX_QO50VweSILlMMqRE4Pj3Uo-XMWMQ9WfS7pKOu64clhENEppp2Xcxp1v4zMQqa-6RB3sfqIuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kva-lxxIwH3mH8gUW2hvHc2W6yK-ML_sTxHdLHxNSClQeeHwr09w5LMvmHd9AFGA_sCLbLVY8LkJODSKKsYDn1CDl6-TKUWcjGKV9Z_KvlQ9BAvMCVFHm_TDhyRJ6DNK06t1WC4ROZAYZ-YOdVhqb0X-Y-ttuXbpR-WJpQIeRz9BmaJumOy3TQvWLIzjyiTShwCrpY9nWystkLhsXuR66QnLV89QbQ0DBTy0m47jNEh3zzMwcJb37CEQnGlxuhqJ2x036gtHizkKGZLuxFRm4FZo1ZyNiMUBb2KpQl2rG8LzQ-M_gi4FwkNxtsHJ40oimFihSt9Ox5Oqz4K8rvvvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADUewyMLtkbS6r0yJr2o_5q8XCijdHuKiUA9hKY-DGXnXyNR96NgFdiHNejDPa64a1F6IQya5Rjl2ce4zTKLE9tvOWNuAZBsMqW1WCRQV7zKoLTGrCRL6HxnZRIYgX_UR8C6nJxrhMHJor596FTXZ9HjTX3Hpg9M-iM38GCFrTZqjlKt9QSom2_QMOHAcQOVvUGedFtaMRS1KyutpCqYgC6TwlPLASjxcgeyDO4ajDKk5k05Oyluz1cw8WUNlB-vrOSlNkgNmicnriYxYQcHqw9gyqzLswAYOKRgBT-uqn4iluYA-SKBIGG5s89d9HT2IIVSmgMunE3vKg41uZ3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=B7QfaXtjcVmIVPzaqWuXqWTo9EijNuhIn8TzQdoPfkN-vwJ6fHFIa-gpjbhpg_0b9Vl8Dac4HFv-9GWoS72W3buQR2Pp7Wx_bfBxdxA1DITo-crJ_SF0rzRBlM81n-b7w0nM6gVNTNcauRm7oUuA35SvgRAw7_uKpDqSXCsbCnTw07YIee263vZVeL9Bg60Phh3LVufSxW2dV0q8cxp08sv2rAlEOF_g-Ec27GrRAm0p6KMKBtBoS5xxA5z3YK3xu1Sdq8HO_iC2F61rAVONYv_wkccJaUvXO0le_EJxRpLVDXXue6FxiG12pSadFeW-TXDGZGJffzKBBHgEfH5xsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=B7QfaXtjcVmIVPzaqWuXqWTo9EijNuhIn8TzQdoPfkN-vwJ6fHFIa-gpjbhpg_0b9Vl8Dac4HFv-9GWoS72W3buQR2Pp7Wx_bfBxdxA1DITo-crJ_SF0rzRBlM81n-b7w0nM6gVNTNcauRm7oUuA35SvgRAw7_uKpDqSXCsbCnTw07YIee263vZVeL9Bg60Phh3LVufSxW2dV0q8cxp08sv2rAlEOF_g-Ec27GrRAm0p6KMKBtBoS5xxA5z3YK3xu1Sdq8HO_iC2F61rAVONYv_wkccJaUvXO0le_EJxRpLVDXXue6FxiG12pSadFeW-TXDGZGJffzKBBHgEfH5xsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=htZ6lIwQdcEmxZB4aVi_p2DooG2LwlLB34ZBS7OBZcvrQM1ORCCfuqbdqdXP8sRjNXYGv031gpJe1JfNw_7b5dpY_op1Av0k0AvbAxoFWrXHhytv3XPfBupU157SxnG4WNVYTWubEQ7ZjxXfdXuFgJCs6xZftQrA_9ZBbgBEdq8wvpE6EVH_zlzoZ3ET1zrDXjVymL4k1Rf82keqbTI33kaj_a5sSeOVjTZi4hzZIZlQr6Ske7UMuJV1xGNXS5CpfPe9ZjZuundVnvh6lRtmEUY_2Z5IrFcXMLsu21QuQawV5Cn_teMkv-FAweVyULwp1ZN-690JSiOhXy5RCxSu7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=htZ6lIwQdcEmxZB4aVi_p2DooG2LwlLB34ZBS7OBZcvrQM1ORCCfuqbdqdXP8sRjNXYGv031gpJe1JfNw_7b5dpY_op1Av0k0AvbAxoFWrXHhytv3XPfBupU157SxnG4WNVYTWubEQ7ZjxXfdXuFgJCs6xZftQrA_9ZBbgBEdq8wvpE6EVH_zlzoZ3ET1zrDXjVymL4k1Rf82keqbTI33kaj_a5sSeOVjTZi4hzZIZlQr6Ske7UMuJV1xGNXS5CpfPe9ZjZuundVnvh6lRtmEUY_2Z5IrFcXMLsu21QuQawV5Cn_teMkv-FAweVyULwp1ZN-690JSiOhXy5RCxSu7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icEOHvYSrD7bW-8wo9wBRA3okd4_Fq6-aJLstuKEGKBCdTJokuTob-AUE0jTQlcWVFybRF9MkuVRYq3OaNgeC6Itr0BpOYq0Qyi-uALb4E69ht0EzN1CAKImYnzEtqt-NL24870b61mUoEW8rUGWxUeyiWQose-g0LVGO43r9OFf1V2ghNSD-hOJIcxupfQyNu_FeOoVWV4z5hek4nZOEEjlB22yyrvdcUoey0d1AdqZtw3AtDAxk8FS_FD9Zy_pIxyorD7Gzm88XyB6Y7FtMSSMUBwY1dOKl_4wuYfnHNzHQYtk4MpSvQaa1wB5L_wAFMbL4_06dCfZlsjHa2HzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRFvICSGAsETo_zpiGEOgzzs0CRZU9TrKf3ZEYGe0IMCez1F5RCiLQZ8drxbUcEzjOJ1dKcj5gfV-oR4AGjH2g2Tb1VhRV874SCJTD-dFMxnFMF7TYOhgQeCWk-VDV4OrIeyXZFi2R4x3Zqase78_WD8F_Dk6sO52oJmNwovSDOoFVhBJ9n8klTjRYMwqTV9sN3iPwfE0JX5b2WC9QVrhkKjxKJPde2EaZMbrA9OUefT5vbkexepcma85MEUPXRufIIM2n5W29-JzUdkhWT_AxBO4oOYAGlgdbe9d1yziLc4cf7INBr8kWaSrdqdggkODqZ_YF4Sd_qbBrwDIUBqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=ulhMcsjdIvr3e_-SzE8iVxid1DuoZRGEQIbW_8NyrMMHrLMRMxsibXEcXDM4YFhxk_MkE2ZkeSbRhnUiyjaaczHms52suicxscwGMaxCRaNkFyeYBuMr_DBHEDWcN_QI8QUsflTrrZ8Nk4_JTYsmh9s82jSOTO_jxozfHH_BUwCPpfCBHm5G_AE6mCPT_XIYRKYgmT3i695t4rRGzgKl6xDt7laM4iaSGkJ3dtN3QeL1noy3a3WAPcK5ARTPlnGW0PpuVrme59Gfw1siztUCJowW9fNj96FAuf5dgcwwrHCFBsZelTvdYfBlaUALDwzffe_Tc4lNv1XxmVXPDJGW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=ulhMcsjdIvr3e_-SzE8iVxid1DuoZRGEQIbW_8NyrMMHrLMRMxsibXEcXDM4YFhxk_MkE2ZkeSbRhnUiyjaaczHms52suicxscwGMaxCRaNkFyeYBuMr_DBHEDWcN_QI8QUsflTrrZ8Nk4_JTYsmh9s82jSOTO_jxozfHH_BUwCPpfCBHm5G_AE6mCPT_XIYRKYgmT3i695t4rRGzgKl6xDt7laM4iaSGkJ3dtN3QeL1noy3a3WAPcK5ARTPlnGW0PpuVrme59Gfw1siztUCJowW9fNj96FAuf5dgcwwrHCFBsZelTvdYfBlaUALDwzffe_Tc4lNv1XxmVXPDJGW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=v18qfxlFqVgDbmHmxFbJ5idkSgz0gUidHFxzyK4ckb2SdH-6usdM9d3kKe7569B3_wHsbM-Huq_BpFyGKcHDBtej4LTLQDi1UWfxToc3Dpnw62qPkSChCUR7qq6VSdyeB_h5VKcCd6g9i87alRwShZWu_j43dxJmRO0L_Xjk8a5j0ejJzGTTE0CsEqYNm7EqT9h-ecidzrDHuDe-EM3FVHKOKvD5e60Q27SP-FpyOLufhA0ij46FTxyKLvEhQi-1_5tP_jr9wXR8ge_dVlHUubkesNEw45poUrpIFiHpRgf_liT1_iFUUCOVaz-CoQXIUXwLDvfVlarf1IsYCK9F9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=v18qfxlFqVgDbmHmxFbJ5idkSgz0gUidHFxzyK4ckb2SdH-6usdM9d3kKe7569B3_wHsbM-Huq_BpFyGKcHDBtej4LTLQDi1UWfxToc3Dpnw62qPkSChCUR7qq6VSdyeB_h5VKcCd6g9i87alRwShZWu_j43dxJmRO0L_Xjk8a5j0ejJzGTTE0CsEqYNm7EqT9h-ecidzrDHuDe-EM3FVHKOKvD5e60Q27SP-FpyOLufhA0ij46FTxyKLvEhQi-1_5tP_jr9wXR8ge_dVlHUubkesNEw45poUrpIFiHpRgf_liT1_iFUUCOVaz-CoQXIUXwLDvfVlarf1IsYCK9F9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=dgkqhOuglU1LGhtE7TDLYI1a8yBhtfUujhKhKdM5W0NvpD6nDCjwMM2seW4B7u2KvAdRPIe7OMYymuxaX0fN1uwf-pAx5IHEgIvKCO35v51-vO1fz4_vDi_AbGutFqzRqsj6D4jkcSSEKYsjCWJzBrfx-zodOU7mREsz6DrpBTk3gFrv1wn-aB70-8SkXi0oTkRKGkh_W8d231r4ppKoDYHBiYQ-3iWBOX5lUyGpXSIExXLi5JVn-Ei9ru8tpowNEDe8Msr0hUIHNohhsYuW31Vs13lL8ZIdeMhV3iJ_hh5ScKen2a_KwGQDqMWvFCB_cGVWpSTSMqSAHT-puj_mfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=dgkqhOuglU1LGhtE7TDLYI1a8yBhtfUujhKhKdM5W0NvpD6nDCjwMM2seW4B7u2KvAdRPIe7OMYymuxaX0fN1uwf-pAx5IHEgIvKCO35v51-vO1fz4_vDi_AbGutFqzRqsj6D4jkcSSEKYsjCWJzBrfx-zodOU7mREsz6DrpBTk3gFrv1wn-aB70-8SkXi0oTkRKGkh_W8d231r4ppKoDYHBiYQ-3iWBOX5lUyGpXSIExXLi5JVn-Ei9ru8tpowNEDe8Msr0hUIHNohhsYuW31Vs13lL8ZIdeMhV3iJ_hh5ScKen2a_KwGQDqMWvFCB_cGVWpSTSMqSAHT-puj_mfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=MAlTmJ5O_yOIK_IqWZXGbik1qItIX7t7UlOQZhofHWAtMv5pYdzJ_8wq3CGqOsWz7ClsErb2MhB92tIz0hAmhgeUZXIIk0t-r2Elfhcl3evMgFbiLxsqR8LhV2GKcwwfR-SJYVeCSoScCkANoBG_AwF-NujDijOiY9aK8lOkZblX6FrMYKy1_UVgAFZ_5VJtHeNGg4rvkSNyG3kam3mcmongawFP_n7C3TiDBZ1Yr-DEK203oQ8tKlPJ8J5vzBJWhYnZPB_gcFyH0HzISsxMiVvvPBQlcUJYkfY02KFSngx64NBQillK2IJIWZnhqamECmxlMQ4L3WYJNJh7iI2v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=MAlTmJ5O_yOIK_IqWZXGbik1qItIX7t7UlOQZhofHWAtMv5pYdzJ_8wq3CGqOsWz7ClsErb2MhB92tIz0hAmhgeUZXIIk0t-r2Elfhcl3evMgFbiLxsqR8LhV2GKcwwfR-SJYVeCSoScCkANoBG_AwF-NujDijOiY9aK8lOkZblX6FrMYKy1_UVgAFZ_5VJtHeNGg4rvkSNyG3kam3mcmongawFP_n7C3TiDBZ1Yr-DEK203oQ8tKlPJ8J5vzBJWhYnZPB_gcFyH0HzISsxMiVvvPBQlcUJYkfY02KFSngx64NBQillK2IJIWZnhqamECmxlMQ4L3WYJNJh7iI2v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=PpkoX6mcqhfJF-KyWWoxsWeVxzU_VllEQ0bkZT_FyAS5p1kMaXo3JUzztZ16sgKNr2ANwVNEgA1TibMp7B4PAOlWML4SIHFCom4tVjKZp-tdBqPo72neGxG1XqjkT78lq0aYyVY3Aer90AxI3fuf_XbbrOb4YcOzXddbnEJbnx7buBFBDXO0wBKaHl_qfL1qflbIgpp9JP28YIBXsqJzLy2TKXM2sLu5O1Nu-DKUhN2XNAlHu67UlURNvRz-uStArGxB_avhuCUrn3_uZv-dowLNzcRXPonGoMg-ALv-llSqmCxgaCK4GcAk6md0Gb7i6iJJ7rqxcjcdnJAXDzBm_IwNIrQzgigVYPIB9i4QloBaO8JMDFG3dGL-1VmKkBLVsLFqi_sQQN0wTcot5-uDbBm2g7ot3lFHARfTK7W8pM-WMXetAdVDV2IUGWSplzr7jcbZzriZmdTZdA0Hy5uwJOXeuzFMp5EapRfDQJYnT8NCN6ZEpVfy3d_380IXGl_RZHODtjuwFGQeuW93lPwZp61gNaRvksLQevgGwze3I9fkqU73EtDvkaIpMXmASLEYsLcUDh4J3F_DpGfyYZFC6KJ7S6X26vPr0dfOYZ7KbkYlC6U1IZKZ_4XBIp31OGX2DfJcxNN5fPKx9smG2R5wkZmUwBvd7D8IEG7MWM6mdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=PpkoX6mcqhfJF-KyWWoxsWeVxzU_VllEQ0bkZT_FyAS5p1kMaXo3JUzztZ16sgKNr2ANwVNEgA1TibMp7B4PAOlWML4SIHFCom4tVjKZp-tdBqPo72neGxG1XqjkT78lq0aYyVY3Aer90AxI3fuf_XbbrOb4YcOzXddbnEJbnx7buBFBDXO0wBKaHl_qfL1qflbIgpp9JP28YIBXsqJzLy2TKXM2sLu5O1Nu-DKUhN2XNAlHu67UlURNvRz-uStArGxB_avhuCUrn3_uZv-dowLNzcRXPonGoMg-ALv-llSqmCxgaCK4GcAk6md0Gb7i6iJJ7rqxcjcdnJAXDzBm_IwNIrQzgigVYPIB9i4QloBaO8JMDFG3dGL-1VmKkBLVsLFqi_sQQN0wTcot5-uDbBm2g7ot3lFHARfTK7W8pM-WMXetAdVDV2IUGWSplzr7jcbZzriZmdTZdA0Hy5uwJOXeuzFMp5EapRfDQJYnT8NCN6ZEpVfy3d_380IXGl_RZHODtjuwFGQeuW93lPwZp61gNaRvksLQevgGwze3I9fkqU73EtDvkaIpMXmASLEYsLcUDh4J3F_DpGfyYZFC6KJ7S6X26vPr0dfOYZ7KbkYlC6U1IZKZ_4XBIp31OGX2DfJcxNN5fPKx9smG2R5wkZmUwBvd7D8IEG7MWM6mdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=D7iLVKp4QvJYKhEvp6s7qgShjgWDNtXPkft_XCVTi9bQfy7JR4JWS5bsrFgb0_R-nv0xSasCXTQAUmm0LpT8Xwjv4zisJhHZPuDSsDThwKQdkVNDkojrkYZoBir3pw_616wq4S8PBiRJQy1LJ5Pt3PZ-MOBM-GyknlXFPvqzLdee16CIKKjRPwGvH6X2x0iTp2CtUjY8MwybRZzvdxvZuFfC2Etv4W2TxPrFRh90pScGzHd7X572nB6RDVoiXX-vH1ZqHstLbcuzw3YGnKauGqw3BOoN6pNUZDh70SvqIh4L44MK0Kc1Lg8toyhz0H75iIPNEyfAcvEe7oCS1kO70oMVarrgXLKij37Y_AFOlFlkarwp4nToBjbW1dE1cb9SONbgrltvd8xUgFWNqePWxzkzOp46QLKS0o2RR9Z2AmxZihpWa5uMJVajHg3ezbdu8iLDcbeUnK-oaN6S4h99e6zJtVcfNCN5Wz8sm-U6T6h77rTREGZrZbNYVHH7QvHUsNIm_UAd-u3kY02I6lP73rkih76gsXetUKtNysYR76soonDZ0VQK2SCP08tHogtRNgI8d2mzqL-tRyrhf2U5Y3uG1e-eVMp5T2R1kGtBx3XEdubwrKoFl7KFSmFY0T5Ltouc2kxGdYE4Ef3H_Xiqrg26m_YE0pdTn3ZutPMLrmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=D7iLVKp4QvJYKhEvp6s7qgShjgWDNtXPkft_XCVTi9bQfy7JR4JWS5bsrFgb0_R-nv0xSasCXTQAUmm0LpT8Xwjv4zisJhHZPuDSsDThwKQdkVNDkojrkYZoBir3pw_616wq4S8PBiRJQy1LJ5Pt3PZ-MOBM-GyknlXFPvqzLdee16CIKKjRPwGvH6X2x0iTp2CtUjY8MwybRZzvdxvZuFfC2Etv4W2TxPrFRh90pScGzHd7X572nB6RDVoiXX-vH1ZqHstLbcuzw3YGnKauGqw3BOoN6pNUZDh70SvqIh4L44MK0Kc1Lg8toyhz0H75iIPNEyfAcvEe7oCS1kO70oMVarrgXLKij37Y_AFOlFlkarwp4nToBjbW1dE1cb9SONbgrltvd8xUgFWNqePWxzkzOp46QLKS0o2RR9Z2AmxZihpWa5uMJVajHg3ezbdu8iLDcbeUnK-oaN6S4h99e6zJtVcfNCN5Wz8sm-U6T6h77rTREGZrZbNYVHH7QvHUsNIm_UAd-u3kY02I6lP73rkih76gsXetUKtNysYR76soonDZ0VQK2SCP08tHogtRNgI8d2mzqL-tRyrhf2U5Y3uG1e-eVMp5T2R1kGtBx3XEdubwrKoFl7KFSmFY0T5Ltouc2kxGdYE4Ef3H_Xiqrg26m_YE0pdTn3ZutPMLrmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=v8G0vIPZUZt3VimVI6t4WyLF7nc-jEBcx9_SgUptp7TK11jpZxEDesQrlzG92TdvIneN-rKzEnRtUSCG-IWNO-UGxS6T_rhsIauMgwvuwreZ_ub09Ws1bvo_D2EpeiBALZQdpkM3G5LNGUDfApZm8VSsXMVez04fMjg0rGpfu15_xjHd9xiTcyN-aaEOihd6_hf0ZRGc7yxxWCMFHJK0JjNXc879cZgNpXj573WJZUEDn7lV5ekiwF_UPF0VbBks4H5Aw_my--1tMiYvjEfDmyRoEnTv4izrm3X1qNXzYqCLazYpGhCzLv0HeUo99ioCGKe52b16Dph7vW7Mevic0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=v8G0vIPZUZt3VimVI6t4WyLF7nc-jEBcx9_SgUptp7TK11jpZxEDesQrlzG92TdvIneN-rKzEnRtUSCG-IWNO-UGxS6T_rhsIauMgwvuwreZ_ub09Ws1bvo_D2EpeiBALZQdpkM3G5LNGUDfApZm8VSsXMVez04fMjg0rGpfu15_xjHd9xiTcyN-aaEOihd6_hf0ZRGc7yxxWCMFHJK0JjNXc879cZgNpXj573WJZUEDn7lV5ekiwF_UPF0VbBks4H5Aw_my--1tMiYvjEfDmyRoEnTv4izrm3X1qNXzYqCLazYpGhCzLv0HeUo99ioCGKe52b16Dph7vW7Mevic0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=cboU2peQgkZHecH86ApFtALJ3Zc1g-mLUy7w3uenmaCBaLKcmfI4EN_9c1gsZBkAhfxIE9Zx5en9KWambtiADlXk-JsAEgiSsslmg-crlinhiwNRIY4YUFxfoAQO65N7X2NoSk9QqvfAYxV-qnk-y80BNIOrEKUdoczqFI-a_X2mB2jOjwKI2IZpmtTEcgYLgtOthED05I0XEe55IDCu-GshncZ1eLon-kve27RCTv0f7bzsMbmvNlsoI0BRil01tQlxwOMRO7BZLIhYn_k0eWiW82FpW35f2FDjy5uYmyNu-Qw4nOJsROIM-G9tykCT0PYiZpyi8pGCetoCPZum5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=cboU2peQgkZHecH86ApFtALJ3Zc1g-mLUy7w3uenmaCBaLKcmfI4EN_9c1gsZBkAhfxIE9Zx5en9KWambtiADlXk-JsAEgiSsslmg-crlinhiwNRIY4YUFxfoAQO65N7X2NoSk9QqvfAYxV-qnk-y80BNIOrEKUdoczqFI-a_X2mB2jOjwKI2IZpmtTEcgYLgtOthED05I0XEe55IDCu-GshncZ1eLon-kve27RCTv0f7bzsMbmvNlsoI0BRil01tQlxwOMRO7BZLIhYn_k0eWiW82FpW35f2FDjy5uYmyNu-Qw4nOJsROIM-G9tykCT0PYiZpyi8pGCetoCPZum5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=UnKeeYr9WGtD9ZwaWaFnBJZ-uwiWTxdKknTT0N2Z32zNY_LJ7MV-iNaBtN8XB02wGRa88mcIg8hSbve7DL_xONZOu4YD99L4mgpYoAvZSEvn8kVEkdIHYIVZP-Lm5FEI1SRkLrej7ictDIGF3aw6A8Nkgle5t_Cs45tSB5JLJc6siCZEd9D4yn6WKuIO_lyrYMR8h5WnLkU6nBglT47wkiRflXgi83DRI-QtHK_H-za4arm1J0o6PKpbRNPbEXKCcRR2gL6slTxonEf2zgKlGZ1BEwe-7OqjESPjmR9xgi6xLT1tNmCdGshGmy3MeJrNS55g2swk6GLGgnsaVbrm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=UnKeeYr9WGtD9ZwaWaFnBJZ-uwiWTxdKknTT0N2Z32zNY_LJ7MV-iNaBtN8XB02wGRa88mcIg8hSbve7DL_xONZOu4YD99L4mgpYoAvZSEvn8kVEkdIHYIVZP-Lm5FEI1SRkLrej7ictDIGF3aw6A8Nkgle5t_Cs45tSB5JLJc6siCZEd9D4yn6WKuIO_lyrYMR8h5WnLkU6nBglT47wkiRflXgi83DRI-QtHK_H-za4arm1J0o6PKpbRNPbEXKCcRR2gL6slTxonEf2zgKlGZ1BEwe-7OqjESPjmR9xgi6xLT1tNmCdGshGmy3MeJrNS55g2swk6GLGgnsaVbrm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=E7LjR5nE39-Fy0mPrRkWGM9bMPCRKSWepZdrqphcX7T9mlv7Q5rjZpv5yFerU36LQmRco-8hyd5PSwzTFxEZqOlZaWYZORYjmai0g8kZsXBtEz5Scr7bmjP1_C6UrrrpgS5PlwpDXKgGha1UNGL7RrV7lL2ADmpbpoUg7Sgy7KF8dyLcuNVHO1OpS1IjJYB_2BKx3t16mBS_n6AU3TAMAns3uQgiXtEcBh5QoOaYsu0t_hRB6Wy0kdYlM-BkoIcxViWR6ZsxjFW2fOd0uG4BmC4rQzEtXApJsqF9LFI9rWbuh0w66HufxkgMfxN21n5zUdFtWgxeT5fK85lJbs1oaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=E7LjR5nE39-Fy0mPrRkWGM9bMPCRKSWepZdrqphcX7T9mlv7Q5rjZpv5yFerU36LQmRco-8hyd5PSwzTFxEZqOlZaWYZORYjmai0g8kZsXBtEz5Scr7bmjP1_C6UrrrpgS5PlwpDXKgGha1UNGL7RrV7lL2ADmpbpoUg7Sgy7KF8dyLcuNVHO1OpS1IjJYB_2BKx3t16mBS_n6AU3TAMAns3uQgiXtEcBh5QoOaYsu0t_hRB6Wy0kdYlM-BkoIcxViWR6ZsxjFW2fOd0uG4BmC4rQzEtXApJsqF9LFI9rWbuh0w66HufxkgMfxN21n5zUdFtWgxeT5fK85lJbs1oaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=TbiXA71URw-hZwb01Qgwh7kzxylzbmcUaq1sw1dOhFqLgFZmaHzDpp1Z2vxjgSH2HnWFQxZy8kJpWjvOJKb5Aj9FACKIJm4SmIy9VzaRAqBlenG44wqm8XvBcVscxSmAU6IruVYTZYGXazC1HV-95bPWMAbaTKdCr2UDThFOgTcoqP7Q5P9tMs_a-8bIhEG4Bj9wDR80Y5t8RmR25JasS_yb85XGgMkN7CfrAarUoN51FQCV7liAw1Uk1fInFpotblWq4ZaETP4qkLc7p9Tan8WNQNU3KHDSHqoaPwti_Nohlp8sVl_O8FvnLjQuTXUX8eQDQ49ZzXXv91IcW2usyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=TbiXA71URw-hZwb01Qgwh7kzxylzbmcUaq1sw1dOhFqLgFZmaHzDpp1Z2vxjgSH2HnWFQxZy8kJpWjvOJKb5Aj9FACKIJm4SmIy9VzaRAqBlenG44wqm8XvBcVscxSmAU6IruVYTZYGXazC1HV-95bPWMAbaTKdCr2UDThFOgTcoqP7Q5P9tMs_a-8bIhEG4Bj9wDR80Y5t8RmR25JasS_yb85XGgMkN7CfrAarUoN51FQCV7liAw1Uk1fInFpotblWq4ZaETP4qkLc7p9Tan8WNQNU3KHDSHqoaPwti_Nohlp8sVl_O8FvnLjQuTXUX8eQDQ49ZzXXv91IcW2usyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=ANhrSRm1U0K0ch45_3MDujA7770Eg2NS3uFXD3QhW_i723YULwOqyyP3LYlOIMVeutBVYVCJbZfMdo1Zl_HQthU49JnJqDyl-Cc1PUpxv2BKL6fHl_9MbXUTNpoRYx72lGpwMzFHNBCT_hCc8_YX_twYT6llmLLg60MxgZEAD19LMO60H7BiNY3Smmg600mlKAyjUAHNu5dJlHFnFouy_IDMtWtrYIUaeSvOqAu-EIqARDQT1_IJ1Pw_d4L7Eq6P4dvIHhL_RfM_U6TYPGEO6LBdR1flEM9IP6Ub9oXFRWXBvoFnez0TNJZLSIaaMrILzUfsp_Cbl-u3JEbHuTrcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=ANhrSRm1U0K0ch45_3MDujA7770Eg2NS3uFXD3QhW_i723YULwOqyyP3LYlOIMVeutBVYVCJbZfMdo1Zl_HQthU49JnJqDyl-Cc1PUpxv2BKL6fHl_9MbXUTNpoRYx72lGpwMzFHNBCT_hCc8_YX_twYT6llmLLg60MxgZEAD19LMO60H7BiNY3Smmg600mlKAyjUAHNu5dJlHFnFouy_IDMtWtrYIUaeSvOqAu-EIqARDQT1_IJ1Pw_d4L7Eq6P4dvIHhL_RfM_U6TYPGEO6LBdR1flEM9IP6Ub9oXFRWXBvoFnez0TNJZLSIaaMrILzUfsp_Cbl-u3JEbHuTrcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woq7ojaT2qw5-7iOcTFJMKuNhf5xI5CxiQ2-oqtJzAo94BQUrizHfAtEZKEkHLZASrYaxXsZXuoWTczpYlJF1a04YsJSNr2m6qxxHo9jfdEljErjvt93cB6LKIEBjGyTdt1WISlitiGVFu9r-CqY7KVLYAVrHpkQh9MikLFLr8BxJdsiBNB3B6Uw5xagoQRiEIkG2YQajyGfAdqCj_jwm0fJvUGQpxIlljzzZkZ2H-TJg9Sl4HZbiqnTq9GgDt9fIodshmW95uhI0DybvYpvyyWXIMtWgCSX4S3YJ27ZpXjN1lw9ImA_yFHvQNRyrOfvljLDB1dAWRpqITKRRCXaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8VduBH5ixV8oBQoa2_sqIO0dIqlB5ZoT_nl6hC12GXKnGj4pUKm0PiAR8Dv6fgEwciOitBTIoOeFKCvN62rXhew-IgLwHoGSPd8CEbPWuyWeV18OToOmhUYd3bFCnE6P0gjpOEQg0qKZB3gTzmZ2U8OuHhzGoUVmmO20CLhnm-wS_xAu_lx4Zc17EGdSjG6xPVyR0t0e0Kw-RAfZ3T6qLgR91IWR2ruWoDtZv6mAwc7B6kmVLpjBuw2_hKNOnnaWvL75SYQNPTpZgIu9H4i3T5o1HDl9OrqJhyDk4i0bI-EHGKGCFPblAWNre0ud3w84yFqVTIjMx7jx58oHBJ3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ied6cP_bzgzvHEze7M8l1MFGUDsDrBfZNFeytNPsTI0d7O05VoDW2HYCcuV7moUovkIV-Hbu7c7G7YxnyqLSYAsYgFlY-NvFfbhZvk8QMSVFq_cjysVS98IEfSGh5N5trXmNmDX6lQtqZlpE7lItSj9fNVyzN8K6nlU565KUCapPayBZgUZvbsZrXwVXrb8tRkT6Vg4BI6Tu7hcpvxQKKqfwWx7NdmfpONZnmZ0nbdH7n_nPZwc3Exf7-oQG7FyNHxXSKTUqERX642k7U0qV2DE7EGIGQuDcbfrN5-jo1yRIz0UuU5aney14Z_8U8tnnA-yVVHJdYm6GhCrwI5vnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J58H8SckyeclphSRpSA6R16dFn-YUeDkoZ6ftqNk7HqL0TgqZNIdKWTJWl1kCFHwVZg2EMnqR_cBWqVaHR7un92H5oxBBUu0YUTY0RFPZzVF1fI9bd8BW5yzmXs_s7S7v6foijTTujuT9bryKyu7Gv28MA4QTiIhbZeHhW2mBiUG6IKRkxBkIrOjUTSDFExAZigGOv1bMJu18q-lz02XZc6QVpQ0OgHwh7IW3Iahe-6gRK8XLSj6iwWS0mAiS-34TAOUUoTAAmRChUAMXfXGGevoZF1enW1KMuiCp7fnV2CfrjGDacpTLr9IKvz0GUtxoGrKtaUfvHzE6jRVm2wxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=Vox7wNW_dHagDpbyzMCaF7_aYPgcdKXAqFqfg1r6FNoMpwI2QLG6U3x9WoVkXoxvFkA2sf1KF0XSaAFER9OCSNbQzgCO1xGVA6YJ82UOz39-UvPveSJFN8wh9wQJhCvmDUiPEURngKiRZSFw28KHVzIKAzllUjbkZD22ZsK2juX28ynePWO3Ylb_A-EW1a_mQMyaFZmoq7LDDRrdMaSRoNHhrWu_Y8xTr8KqFEU5t_S5bf9hKY9Sp2IfcI00DimDfO4jSZLc5wz4gRWdDyAfwQfNN9Eywqj74j9OVDnsTlr-nVzq-6WrHYX0inevy1K8-OOpzDqll8qgjJkaFx2gUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=Vox7wNW_dHagDpbyzMCaF7_aYPgcdKXAqFqfg1r6FNoMpwI2QLG6U3x9WoVkXoxvFkA2sf1KF0XSaAFER9OCSNbQzgCO1xGVA6YJ82UOz39-UvPveSJFN8wh9wQJhCvmDUiPEURngKiRZSFw28KHVzIKAzllUjbkZD22ZsK2juX28ynePWO3Ylb_A-EW1a_mQMyaFZmoq7LDDRrdMaSRoNHhrWu_Y8xTr8KqFEU5t_S5bf9hKY9Sp2IfcI00DimDfO4jSZLc5wz4gRWdDyAfwQfNN9Eywqj74j9OVDnsTlr-nVzq-6WrHYX0inevy1K8-OOpzDqll8qgjJkaFx2gUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=KrC7H60psR_RO8fLeOIfbuIHzli2hVIigX8oTl4I3fVEXphs-Fgu8HbivqMSZgzhGOBv7lpmlOaQwmgGbzCyxOll5YsTdKe25YBY7vsYq9z-0WIu--lzKO2ZzgHHBVqNpZcaw1EcUvhsBL7PLx3kbyTp74fFsc0D4abSMQfB2Ws50R9OQxaRp7e484Kk0K88sPM6oTUjqTj0-z0hWB8DWNuW2B9n8dRJIjGocsJ6hf9lS1QPysUhzo0yENigzu0-BYFyHkPY6hYy9YfQBd6sy5AdL4JwzXEemPYiHAarq2qvPueWu9I-2nns6wazMRPVNH19yjOTDotTIW4H5qarzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=KrC7H60psR_RO8fLeOIfbuIHzli2hVIigX8oTl4I3fVEXphs-Fgu8HbivqMSZgzhGOBv7lpmlOaQwmgGbzCyxOll5YsTdKe25YBY7vsYq9z-0WIu--lzKO2ZzgHHBVqNpZcaw1EcUvhsBL7PLx3kbyTp74fFsc0D4abSMQfB2Ws50R9OQxaRp7e484Kk0K88sPM6oTUjqTj0-z0hWB8DWNuW2B9n8dRJIjGocsJ6hf9lS1QPysUhzo0yENigzu0-BYFyHkPY6hYy9YfQBd6sy5AdL4JwzXEemPYiHAarq2qvPueWu9I-2nns6wazMRPVNH19yjOTDotTIW4H5qarzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=oL0lmSImjC3Q-mYHmk6uuCprouuU9btUBNiNo-pDqsXa8bGkbt3AlZr5nXaId93x3dq37CFjVdfmxo106ej4K0xbnigrjXH4yfLV0wN8A7kyTJZ44wETocHjDqWA10GLDldCFuIhhsg76hTdcVn8HEfLyiF7LW_C1OVoUajJqlsU9wg9qdlQA1zK0uPuQetPINqaKaYUIPXQx1JrSs87UJ8AxPJeqHIGtOkcIW5LQHXDhOaL7PCl__tL7l24C3cLraWrZBaJmNkLnOELn6wBs_2DZxfnPxB7PHIFmHr6QYVaoRKE-Qgx7UFDVKW5urhixvxD081eraNXXGSTPVImnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=oL0lmSImjC3Q-mYHmk6uuCprouuU9btUBNiNo-pDqsXa8bGkbt3AlZr5nXaId93x3dq37CFjVdfmxo106ej4K0xbnigrjXH4yfLV0wN8A7kyTJZ44wETocHjDqWA10GLDldCFuIhhsg76hTdcVn8HEfLyiF7LW_C1OVoUajJqlsU9wg9qdlQA1zK0uPuQetPINqaKaYUIPXQx1JrSs87UJ8AxPJeqHIGtOkcIW5LQHXDhOaL7PCl__tL7l24C3cLraWrZBaJmNkLnOELn6wBs_2DZxfnPxB7PHIFmHr6QYVaoRKE-Qgx7UFDVKW5urhixvxD081eraNXXGSTPVImnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4NGupTLCIGPgVUMQLbNSYD3zGBIzEQWlsqu1GpRISqckbjWqM2D3GW2IKJt6MFAhvOMVTvZd9XqlHVIR8zV3iVwlbaDgr32VpGXt94ixt1Gjy_fXOEAH_Jvtag4fzNkJTXq-9JBxRXOVnIqsPxFyICFNB_mw2-PGIFyWGxOac-Bcxna1mbEJZxdRou6zY-daGvZu1d0xUMGwRNOrGMbyT6Z8kR2hjmjI4H5rCboQ_y0W6PpKFmEKiy6xF_M0KnIPJCDzCjac8ZXZj2bu5mPrMnazEAruLBnb2lAU64ILf8DTHVYg6EaDCrVuFJr4RGALsbMVmyfpiZdObxOV6s-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=I7GUFwOfE0ZDOYAQ06AnLjNTaQIZamutAveJtJMc7QEeu9RfBXe0R4KMGvtcJJ5sSE51VImKnIk7TG_7NWOUrCWjctMFeDb4dIB2zwKrEmzsbm5p1SLheQ8S_YXNraZE-BffohvDz-lq11FW0bUNyunzitN-guiK_awkYp8ltrLVndgCciL4LR292RO-j2ow4scG9aownqMtl9qbdpBLBiN0WSVab8QJi1VATu_EQ1ppCypfgH7qF7FcTAU-mnZLNokp7vmRiOPFbW3AC1oU2Q_5FGfbrZ4Bfmc-43YnsJ-NUr3oytnS2JxZDTheQKxRRwWHW6h5ZUNGPGBURjtw_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=I7GUFwOfE0ZDOYAQ06AnLjNTaQIZamutAveJtJMc7QEeu9RfBXe0R4KMGvtcJJ5sSE51VImKnIk7TG_7NWOUrCWjctMFeDb4dIB2zwKrEmzsbm5p1SLheQ8S_YXNraZE-BffohvDz-lq11FW0bUNyunzitN-guiK_awkYp8ltrLVndgCciL4LR292RO-j2ow4scG9aownqMtl9qbdpBLBiN0WSVab8QJi1VATu_EQ1ppCypfgH7qF7FcTAU-mnZLNokp7vmRiOPFbW3AC1oU2Q_5FGfbrZ4Bfmc-43YnsJ-NUr3oytnS2JxZDTheQKxRRwWHW6h5ZUNGPGBURjtw_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=iBIGFoMJdlUgSa_bteaGUH7H0wgADqwXstVvTb0rc89WphOJp6uNE_-UA-TAq7WWQ0pt9--CX-vCof1jKjMhFmVrkyefHALIslMTSA7h1B4o_h3Y64OO3XF4tKm1Tg-RX10mqchYUbXTX7soufa5YAT1D6rYVTrwRwzzZJzz7NQg8hL6jKdTJBHCU4mhEWEviSqiQIPP7jAEikm10pdkXA3sBPQ1PaZ6ZzP2og3ywwMsnGYscS1fUJE0PFlPxq05AEQxXdpTFoU4CJcyMRo2sDNrHlnAzH8vU7JK3EqOBR2UuUkz3GzVfyNcUbh6CJluEx08kck8euGErYnuGR73aUuqbaTbexRMWT_Fv5-XHpjCmvIXBMWqoznUWMpq4xs7-SPjGdb1VoxbBtK_sXHWpyeEM9o1pYOuRjUPdvHcMdepruDmdleeXYNM2-G4Rc0NsS6T7jNk3z_zoLkq1z0QJjgHhxWIX-zPlHKnrWnNMiXRYM3Evfd5u2ZU7LgIWTcRrqUb2F07O-HvzYFXm5l0vibrsTCtsWbdA9bG3Qb4NQzMahVMWLVdtPfuUMkg18XmVjR20IlzkcdQ64xM2uRs83ETFvEAp6Qe2fJ1rb76l3naEGiLTZq4Frl9AGMqbvcihtqJz1R0Gu3xIJkRTmhHP-YzKOsTI1ZHYSXeGuBI-rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=iBIGFoMJdlUgSa_bteaGUH7H0wgADqwXstVvTb0rc89WphOJp6uNE_-UA-TAq7WWQ0pt9--CX-vCof1jKjMhFmVrkyefHALIslMTSA7h1B4o_h3Y64OO3XF4tKm1Tg-RX10mqchYUbXTX7soufa5YAT1D6rYVTrwRwzzZJzz7NQg8hL6jKdTJBHCU4mhEWEviSqiQIPP7jAEikm10pdkXA3sBPQ1PaZ6ZzP2og3ywwMsnGYscS1fUJE0PFlPxq05AEQxXdpTFoU4CJcyMRo2sDNrHlnAzH8vU7JK3EqOBR2UuUkz3GzVfyNcUbh6CJluEx08kck8euGErYnuGR73aUuqbaTbexRMWT_Fv5-XHpjCmvIXBMWqoznUWMpq4xs7-SPjGdb1VoxbBtK_sXHWpyeEM9o1pYOuRjUPdvHcMdepruDmdleeXYNM2-G4Rc0NsS6T7jNk3z_zoLkq1z0QJjgHhxWIX-zPlHKnrWnNMiXRYM3Evfd5u2ZU7LgIWTcRrqUb2F07O-HvzYFXm5l0vibrsTCtsWbdA9bG3Qb4NQzMahVMWLVdtPfuUMkg18XmVjR20IlzkcdQ64xM2uRs83ETFvEAp6Qe2fJ1rb76l3naEGiLTZq4Frl9AGMqbvcihtqJz1R0Gu3xIJkRTmhHP-YzKOsTI1ZHYSXeGuBI-rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctHLTY-Q-UE3ysfC4YqYtXp4uQuPOj0wiQQ7mUl97EdSB1y_rkpkqfvofvGb5dtEzqf9QmKTeN6nOfBbJbq21QytcSGsrWo3LE98JQdzUZ84z3_z5mZI4xvm2m7zFvQtxPq1ihbx0Ey8Xep_S4fFTmTPqd1P2wC_Di3Sbm9dXrhZYgton5MZtgJj7iKxoegz88ZlFYwDcwvK41pMo22de9177gH2XoTPxnG7zwrh0oGW1dkQlpaIwqVgT1VQG-ZPUa7vCcRWVeMT5BZ7QLcgC7DgsxT7UUGMjP8Uc2oJnWSt_V1SL6GPg-Kf7xUQnoWrB36d-beomF0Hi2okJkTEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=ucfmuAkfILMagFp9O-eUZt7W2lS0G_f1d2Rb30nSu6O7TBorwBWs30eOKp5fT1ukzlE4kbxJIHPCIii4__HlT6uVO38nndJuLqUV9IbmNu3GR831dgSw8cWM6LeVnUE7W7lRjy-Z13CSqKUDMqU0N6jLxqQxRBIQDKtOJChkJHRTh9b4EgpAs1ExeXQ4hNCH3cJkJ6Asj2DkVZzew3BqUykGJwSm0fgCymr0K6S7zK-sAYxgX1EUnWBOLQXnytpqFO0J1-a5yVTNngCmBLn5QOW5k8SYf16bK2qRtYIM-UnhHwsios5rrhxIIbhLU5ojCPOX_Ps0a7hy_hNVRBPlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=ucfmuAkfILMagFp9O-eUZt7W2lS0G_f1d2Rb30nSu6O7TBorwBWs30eOKp5fT1ukzlE4kbxJIHPCIii4__HlT6uVO38nndJuLqUV9IbmNu3GR831dgSw8cWM6LeVnUE7W7lRjy-Z13CSqKUDMqU0N6jLxqQxRBIQDKtOJChkJHRTh9b4EgpAs1ExeXQ4hNCH3cJkJ6Asj2DkVZzew3BqUykGJwSm0fgCymr0K6S7zK-sAYxgX1EUnWBOLQXnytpqFO0J1-a5yVTNngCmBLn5QOW5k8SYf16bK2qRtYIM-UnhHwsios5rrhxIIbhLU5ojCPOX_Ps0a7hy_hNVRBPlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmqXCN_AUpnJVTTJn39XU5ZjGmFCCdHrb4Uvn-dSbOLiTK_4k5TzhCCTuhOXyoQW4H6kK88cd6E390SEkmPINGTsCHcMY2mEvPPUfptn4M6abuPbkgUJg3OnzaGSJXKilWw1qbMo_V684xZBb7vzOvdq30bVnueKd-SaPGNCqCKRK0AL-a8TAakpIxtPl2-Vkh77X83xHvOL_cjGYSRDjvuIdMWEMGvV4QD3yIlizzn-vac6P2pOrvr9i2Cdit1KhUbsh1lrtzMPXA0KazPrF06DhM49m5s05IIJe8o2qIdVLn1KbHnbSVnTJ1jEGyaKGPeMYsoLApqF6Y1RSVOoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ME1Juq0bSzyuHhD2KXX9PdPwfeDFyiBt-fiM1GRohZWaWDgeOPxcWETFd5cIkzyo_0I7oLX28_t449r291mTCUQ82rgK7YWVYI4FIgmHYByP-1p8trxFFEAAbdlA14sIs9JqoSBWiwsh4RlLPUo6AsKuh-mxatsTqlkPkKsVTOHKkcRljRxLENyb6LHr83vozaazvJO8Z5Q44EVo9W5_5ed2P_bdN516IKJqB4F9F_ZRVIgnsW3vMazyR-6QO8a0Z8qJDSge7R1czLPkGacTm8t3Al16y1fRL7Kh1YIk4ZFB_wnmMjzMuPwcDogmgY5nGs-zuqf_ntYWQoYryIcvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEnOckDgqA4C6ts33EoifNAJ1g69qv4edmfNN2HFE2E0cD0a9RlC8yPABvMPIWicPkQhCuDSjAVTwXp1mBERDJkXqtZt_3gZGNvYfieuZ7kmijAr0LRkPzvzxhn5tWiIhmivWqLe5yAyf_WctFQE7d9pTzDHCoxE5G87yL51R_Qb1UyLWzIiqYm0mi6P-0Ua3yJbMmOVapmbHQLhzxlheXhO3JeVPi2lrNIJfYPTC7OI1moSfW-5udgSlBRg_MTvtY4Sdq99jE7UugGPyC959EdLUtE6JNvRoE6NGwe383m5qtx2AmuvglH_dR_hzeEfhQ31DqcVxj_AzI4rjsf2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=mj5_vIPWt7eru1EhPOyMcDrJ3xhHEsy35Dsf71kht84XpOEDx23hRkkyO5qT8Up5E36jsX-DCCBU4bGAC_t313QMPiae5gkTRK0v9DY6AeA4bG3qi0OBrIOMH-rhbKV-mD8GQMbZ5WuAaTnCgknImmWpxhmeYvzO7K9If7Ahh2OL8toSpz0Bx7rU5VqKAXOu7iqlXbKdWcePkrvgi-KiZGUlq650WoarJFskid_zH4zA7U2BITCrHECxLcG1Iz06xM-GPKj7UuKycZ0Ou_QKqxnOD_OO7fnocHa9177RcGr-U5K0_l87Xa1O7yuK7sjwKSA_DRAg26mFn6tXRNmZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=mj5_vIPWt7eru1EhPOyMcDrJ3xhHEsy35Dsf71kht84XpOEDx23hRkkyO5qT8Up5E36jsX-DCCBU4bGAC_t313QMPiae5gkTRK0v9DY6AeA4bG3qi0OBrIOMH-rhbKV-mD8GQMbZ5WuAaTnCgknImmWpxhmeYvzO7K9If7Ahh2OL8toSpz0Bx7rU5VqKAXOu7iqlXbKdWcePkrvgi-KiZGUlq650WoarJFskid_zH4zA7U2BITCrHECxLcG1Iz06xM-GPKj7UuKycZ0Ou_QKqxnOD_OO7fnocHa9177RcGr-U5K0_l87Xa1O7yuK7sjwKSA_DRAg26mFn6tXRNmZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=QAZczl_cLRDyTG3q4DXs9sHuRss1y6edXS2RCtv6nJPsWe7tZXolpA7eSHXSeRNHTwYf9ds3nlUGt4r5fvTucvmbIEQXnv1tpbrl8x3A5qAIHj0eI9JkawySCws_8Gwcot2aEVvGW7496tCG-qa-ngACse6Zmo3sniM_vC_GA3Qi1Zhuq2VZbjgbFShfJKGO9Mh0FzuqQWJKE601EPVrfq51mOqYyUv7unCMPIZQBSFxJ8YEcNYP947ELZjgWB5gjCTp0PnITw26Eqz86PldTwkU6d06TCaXkiTegqf06Sx4hz8bWBGC31Yo_RVi8MuYL5ndTmwqtwNkdPLJOZ6Opg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=QAZczl_cLRDyTG3q4DXs9sHuRss1y6edXS2RCtv6nJPsWe7tZXolpA7eSHXSeRNHTwYf9ds3nlUGt4r5fvTucvmbIEQXnv1tpbrl8x3A5qAIHj0eI9JkawySCws_8Gwcot2aEVvGW7496tCG-qa-ngACse6Zmo3sniM_vC_GA3Qi1Zhuq2VZbjgbFShfJKGO9Mh0FzuqQWJKE601EPVrfq51mOqYyUv7unCMPIZQBSFxJ8YEcNYP947ELZjgWB5gjCTp0PnITw26Eqz86PldTwkU6d06TCaXkiTegqf06Sx4hz8bWBGC31Yo_RVi8MuYL5ndTmwqtwNkdPLJOZ6Opg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=cdv6XRs3c1TIpHiH-1yP25z31pOiQbYm4i1XphHX0-uds7R9taBcU_0YPNf7EeUOyM_sVEkw0Funp_dsCZpW6AVjJJyMi7GO_bvzK5pZn1i6ogSIQSSVeL-rVv9MYY3W-1Hdq9gzaKnc76tfFIirIUOFz4cEVMt5Y_ZZfnqoB_4zgKAh0i2NUJWtSYfcfv01ITgFZzf5hNX1sw_YnPMlI4r9iHM2XNt-m4REHqEQD9xs70JFpLlQCFI7xxrJiZ7CT_opG5sd98FYalmXWy5d8Fo0-lJqF5LH2EvuUhj-4oeh5kX7L0AFLwC2QirCGHTSXvNCUDu-9NoF4fgXg5BsXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=cdv6XRs3c1TIpHiH-1yP25z31pOiQbYm4i1XphHX0-uds7R9taBcU_0YPNf7EeUOyM_sVEkw0Funp_dsCZpW6AVjJJyMi7GO_bvzK5pZn1i6ogSIQSSVeL-rVv9MYY3W-1Hdq9gzaKnc76tfFIirIUOFz4cEVMt5Y_ZZfnqoB_4zgKAh0i2NUJWtSYfcfv01ITgFZzf5hNX1sw_YnPMlI4r9iHM2XNt-m4REHqEQD9xs70JFpLlQCFI7xxrJiZ7CT_opG5sd98FYalmXWy5d8Fo0-lJqF5LH2EvuUhj-4oeh5kX7L0AFLwC2QirCGHTSXvNCUDu-9NoF4fgXg5BsXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=S9AF6lmpEE5fB-OfcFbv9IhJHrIRttNclF_J9cQO5ArVl9L-Pmj95ZCyZbblnC_FgYBzJmnQCLZUek-UmSFb19X9yQwcUwKciO_q8-GgVT1nMe95FYpFA8CjZGhymGMbnawIIDzoQXEWUeN13HdnLe5J7xkFeHO_S4ZmpOhbvBYWTtzqLyHM_QeYd80uTCk65YHKQ53B9rMR8lLNyj3KFGqZk7T4SrMy5AQnO5GygB8BzAn9muALJCQzdL52Xn9BtFFNeGi37WRFpNTXbO5yZYo_4Ac1w8ce-sXgCnEDkVsq9Hw8XNnRfcG6m-oUe9owCgBsofw9EgK6E7Na7IIlWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=S9AF6lmpEE5fB-OfcFbv9IhJHrIRttNclF_J9cQO5ArVl9L-Pmj95ZCyZbblnC_FgYBzJmnQCLZUek-UmSFb19X9yQwcUwKciO_q8-GgVT1nMe95FYpFA8CjZGhymGMbnawIIDzoQXEWUeN13HdnLe5J7xkFeHO_S4ZmpOhbvBYWTtzqLyHM_QeYd80uTCk65YHKQ53B9rMR8lLNyj3KFGqZk7T4SrMy5AQnO5GygB8BzAn9muALJCQzdL52Xn9BtFFNeGi37WRFpNTXbO5yZYo_4Ac1w8ce-sXgCnEDkVsq9Hw8XNnRfcG6m-oUe9owCgBsofw9EgK6E7Na7IIlWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=m621zphixrPFz-wwTrl9mWFMAQpXmr_OxArOM_NxbEbnRYW74eWzK6iElB0MKdLJGgijRtYeLozcQDQUU5byLUKyakKCJefrw0-KumOF0LuJtS11VRe3G_DeWytrHeXmiIf6YcItGX7EgRLsZU_07UPRKbpzHO79eGDEmTsk54s4dpaBcv6uamvMwUsdF0zNmZhyjMRzeRSiV952QsG5mP8DVNtUGaME6bLpHnDVWrrJ25kJnQBLD2DlPur68ob6fcx0_9pqSIhRolg06wsFr9KS7EwwX401ikIoeJSKvDtu6gaAE4YXVBbRQPo-yTWLMWwqvnE6rCVT1HVQrGuumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=m621zphixrPFz-wwTrl9mWFMAQpXmr_OxArOM_NxbEbnRYW74eWzK6iElB0MKdLJGgijRtYeLozcQDQUU5byLUKyakKCJefrw0-KumOF0LuJtS11VRe3G_DeWytrHeXmiIf6YcItGX7EgRLsZU_07UPRKbpzHO79eGDEmTsk54s4dpaBcv6uamvMwUsdF0zNmZhyjMRzeRSiV952QsG5mP8DVNtUGaME6bLpHnDVWrrJ25kJnQBLD2DlPur68ob6fcx0_9pqSIhRolg06wsFr9KS7EwwX401ikIoeJSKvDtu6gaAE4YXVBbRQPo-yTWLMWwqvnE6rCVT1HVQrGuumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRMb9oOrEAcgpzG4g9VKEUsCt3AmavnV0Mogy57HjBFVyFTsgh5EJo6KkBoaeDT9bf1TmVDxnXLnDhwU2NYDWmwqI5BWqNTLdkN7sE_rQrZQ62DlprqSQMtA32Pi0CRbnLmwyIPAAQfDTiEez5n9QVgBESIwEWWP10AnKY40J26qkDjfLMXSxE-Sp3ojcFPIh67hfSHaXTdlrIVncfudvrV-uYSu7SvImYcp3lP_nhYsF9kGze82jM_J-ZTojTKkK6bTpANxG0Wfkfuz07Uz4ARGcUiN7hqhkpEfkyvZW30xugtiUs9QPMgxjgG5xhbU9mHAbqSQNlLgblTSMozWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qo6CrXVx0-6q7zMZcVWLGHBK39QxOMdgbB8u774zG0-Y67iCxvoN2yu48mWjUfXkGShLNGxlYo2BMI-tbko5WhN4mJfNdFENpd8WcZClCOASueOZosDtqonsjP2-jAuhNJbXQUjQXSurP3dA_lSDT89cX_1CLzSS76D53CJOvRmOyveeCJr8BLdJbWIDse82Q_g4V-_33LUzgnWr80fOyCtwDeA1BalyVs_R2ouUB8oXrOBRUlbb29fcW0BT3V4TTUBo7RPRGaFYnv5WGijr2vDYzg9IGSaUfjMVy12e0iQfKPcueHjF8RQMylEYiRnRAvzTtVCITK8hDTLLyrCjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klVDmI1ytK6d-Kkr9xhVnrjns3Qar3tZkmlG6t5ZIOJAmBcqJFx5J6c4pBjXJrEQoqK5nsTQOEbQ9-Ih35dkG2GMh6pxU2OL-2aL6QB7jY-5LDFFEVnlVrzYRJj2p7WNuoulFELOWx4r4CTGROHtHiNJnAyKi665hXvDf7Sd993BnzLbmSLC4OzTmnTqq9H6Je0DCw2h4gF15Hti4j2OM9AZiMMHICWCAzf20atoaf7aoWKiUO4FQNsQ18StMyPzyOp0JxKN0A_UQ94atluzphT0lweR809zuOihnrp7PUsYU_uJrtgyLIbwP-dqeBImlHYDLj9menNPqXyUswJWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sr4sgg_Z-Bx1_2Et7SZzkNPk1DSwwCvFKs9YFBOHMmFurohoDtpFLhR1rHcMwAdmn-mAf-_5z8g8zn6n9MdeL_3N1YJVx2z7hrTCYX7b0wvQlO54VK1zSXEdyG8VtAoxXVy4x2U5ihNM_RKqJpfy8vyKy4reT6ySyZrIYeEGGxLQ8Fl75uRQhg9hC_CZRNUEDVgho1YljI_uBreMalpYZ-90u7LZpX24ytluqjQ1vLdUpfdoHzLYXsfPyy1OrcQWMItnamSm6ddArh2YCTN1v5Y0eD1qjBTF8AZIJ022XCKM7Yr5BW4rJJort2RCJGjGORVJykD8QR5DenqYyoV6mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=SaNkK4a_tgugm9fyUXgNS4w_bVFk2gXHeilvaJ0BfjjOXKFYz3YU2eHTJqSJk2sdBKncQhgApJezXeVwIKa7yzMMitYdZlYwX5wmvql9K7dsLXOeNYKI6wdf5ZI0rQ-OP-vyzhBuSn6S0Nww88fpjSukPJhkClCNyVvG6JzzooJGSwaumvjzZXLZWVV4Jq_OG4UxJZS2Nj7Vz7xhB6OUTfOrFPnJXqII0_Zi-EapHSIhvvk_lmErtM22bOBJqiW4P9Dy_gNCXkihMji6TfkkkJbiRhRn1zvf7BfyYwAvY_N1z6d2Lvia9FcWg6UxWmFb7hUN7-6ZFiU0EOve71EDWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=SaNkK4a_tgugm9fyUXgNS4w_bVFk2gXHeilvaJ0BfjjOXKFYz3YU2eHTJqSJk2sdBKncQhgApJezXeVwIKa7yzMMitYdZlYwX5wmvql9K7dsLXOeNYKI6wdf5ZI0rQ-OP-vyzhBuSn6S0Nww88fpjSukPJhkClCNyVvG6JzzooJGSwaumvjzZXLZWVV4Jq_OG4UxJZS2Nj7Vz7xhB6OUTfOrFPnJXqII0_Zi-EapHSIhvvk_lmErtM22bOBJqiW4P9Dy_gNCXkihMji6TfkkkJbiRhRn1zvf7BfyYwAvY_N1z6d2Lvia9FcWg6UxWmFb7hUN7-6ZFiU0EOve71EDWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcWqnjfa_1_Cg-xc6UtsAlk45owzJiwDcPQtW5SxQrKaEZhBiSZUMlRdB1C0LYsaev3AkR6Y0d2cvIbqYmXllmj-H4wR8Wtqchj0FgSnJ6NM15iG9P18271WHuijuoDlRl_uCusf4yACVFdIutTtRDrs2F_-Jb4GvJjVgCPDK5RZB59-UXAlFwUtWdm6uRVl6DP5tfiIquPWNX-F2HCvPpfC08AUlxqWdK4GpPENGLHPk4yEG73r0s89R0lQ4Y4ecbr6tFu-8tXYCDwvwsa94t3WcVGcaWqV4Ozpvda0JSFDquwUcbjOrIz_3imB2ZtB_9KvL6Di57uZOH50n99B_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=Q3kb58mHtbye3UqHo5Wr-kJF6V1AM9sbV8k1wWF3L2VZWTRg9uK4HtBfv1FjOYQpenCMNVfyHY5ZW0s3VI3VRTgZ568mEgQrdKWze1-m5g_YBT9RiOKwaBK8yS6wNNbL0wEp-p1zUbwYKyfqanAL7lPwfZ57NfYUYwijgNynhQaUO6KUn0384G3fBualNVOxlzNJJ_QlXkkRJnNHhl1xNd5dtmeYzEnvmEn8IVK6jNIm_r1gYpaMu7Q56RAitjulppNg8ts1ekrqW-HRmK-B4-_jmih80aOMgJNX9_ZoTHDkTe4fg0zh2qQMiYF6g6-wIYQjd-S-SN_oBhvf4BPXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=Q3kb58mHtbye3UqHo5Wr-kJF6V1AM9sbV8k1wWF3L2VZWTRg9uK4HtBfv1FjOYQpenCMNVfyHY5ZW0s3VI3VRTgZ568mEgQrdKWze1-m5g_YBT9RiOKwaBK8yS6wNNbL0wEp-p1zUbwYKyfqanAL7lPwfZ57NfYUYwijgNynhQaUO6KUn0384G3fBualNVOxlzNJJ_QlXkkRJnNHhl1xNd5dtmeYzEnvmEn8IVK6jNIm_r1gYpaMu7Q56RAitjulppNg8ts1ekrqW-HRmK-B4-_jmih80aOMgJNX9_ZoTHDkTe4fg0zh2qQMiYF6g6-wIYQjd-S-SN_oBhvf4BPXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTZA6B0gUDu-rSb08TXolezkV7cWBB2hQ2NxW8n1GgUycss9Hdd_IKlLjIwiFSeW_H__UIiQRzJYzJHfegmos89BzgwoVUdyJ79Z6W_xGJ2ELO1_-1oGGdrVFCTefStaWg_2vcm1kh7waSqAOSFiWCTFmetLlR0DDHQJp0RMjJWE0_TOy8HRt1dWFVF1PgrHKWwSCfH7vYqP8PAHqAFRqVPtlHR-sJs02f_dI3gl6B4EJJ0bMoy1uvBvCTqqiWbdjp-AZg4S3Rdq2uvfqz63avzxqWCOV06NQGDW6RMV5E_z8sNL1iFFRmR5d8rQ4H1yLxOtDEEISFfnyqMn2rc6-Myg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTZA6B0gUDu-rSb08TXolezkV7cWBB2hQ2NxW8n1GgUycss9Hdd_IKlLjIwiFSeW_H__UIiQRzJYzJHfegmos89BzgwoVUdyJ79Z6W_xGJ2ELO1_-1oGGdrVFCTefStaWg_2vcm1kh7waSqAOSFiWCTFmetLlR0DDHQJp0RMjJWE0_TOy8HRt1dWFVF1PgrHKWwSCfH7vYqP8PAHqAFRqVPtlHR-sJs02f_dI3gl6B4EJJ0bMoy1uvBvCTqqiWbdjp-AZg4S3Rdq2uvfqz63avzxqWCOV06NQGDW6RMV5E_z8sNL1iFFRmR5d8rQ4H1yLxOtDEEISFfnyqMn2rc6-Myg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=XWS6uxjUl2gZoLhcTXTu3gAXNSB1U6R5UdhsZ7v7B8hu5MPOLGR0LjxvT5Ji1pvyr-2jG0-d-1CKgcwYyOJBbMqWDrdtabzxvOye5_hEQsbOVHYrhtaLC_Cx0AP7Yx_-97nO4XjvwXxvqyaGa7JFs2pj4WXYLx4JPZ-KBkzE50hZflZtNTrXhJSujfuxi5XFss_8ODInjmccBtqpJNDDV-wzl0mkYRbjX-nalVrszYg2XY2jkOHNWCZBNj4chDcqzDZQnBG3SVtU3sqECsN4iPbd8-B46yJ5QpnGcvSp-ig73qjT-2d1RK5kSjNvMy3IP9pV4bcGwro21ZVy_uq045O-GzaB7AVMOU8STWuEqjjUTU2G5gG5SQpquFpzjPi3HFFO5Zbqx42v7mcq8ZIM-xjm5h0M4nJ6SYZu1t-HkLjZU3tHXJ1tBcR8-UaTtQdaykuDJzumVhqGCa8wHuUIRMIAFU14z89oLlK7zLLzNyQZIRxL7StxbSCZiQ44_VOwVjPJkuCJBhxaECkgL7QFDgg_JwhpXqPETGqGFtNVXQvjTWjQDdA6WPbX3L_8ovVEMzePvGav7R4LICNdKes6zMe7iEf2hp5g7cNSpRC_Bltodc2UqTHHHn8RiGSFGSBYL1EiRfjToIFNvtdwLg1rEa0K9wd68ldkeXJotR6rU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=XWS6uxjUl2gZoLhcTXTu3gAXNSB1U6R5UdhsZ7v7B8hu5MPOLGR0LjxvT5Ji1pvyr-2jG0-d-1CKgcwYyOJBbMqWDrdtabzxvOye5_hEQsbOVHYrhtaLC_Cx0AP7Yx_-97nO4XjvwXxvqyaGa7JFs2pj4WXYLx4JPZ-KBkzE50hZflZtNTrXhJSujfuxi5XFss_8ODInjmccBtqpJNDDV-wzl0mkYRbjX-nalVrszYg2XY2jkOHNWCZBNj4chDcqzDZQnBG3SVtU3sqECsN4iPbd8-B46yJ5QpnGcvSp-ig73qjT-2d1RK5kSjNvMy3IP9pV4bcGwro21ZVy_uq045O-GzaB7AVMOU8STWuEqjjUTU2G5gG5SQpquFpzjPi3HFFO5Zbqx42v7mcq8ZIM-xjm5h0M4nJ6SYZu1t-HkLjZU3tHXJ1tBcR8-UaTtQdaykuDJzumVhqGCa8wHuUIRMIAFU14z89oLlK7zLLzNyQZIRxL7StxbSCZiQ44_VOwVjPJkuCJBhxaECkgL7QFDgg_JwhpXqPETGqGFtNVXQvjTWjQDdA6WPbX3L_8ovVEMzePvGav7R4LICNdKes6zMe7iEf2hp5g7cNSpRC_Bltodc2UqTHHHn8RiGSFGSBYL1EiRfjToIFNvtdwLg1rEa0K9wd68ldkeXJotR6rU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=ues5Q5Dy6IdrSgc4Pl8gQVSmVZH565l7AMIQSNmiUIwPUWdAYmvPlpgwTQNWoIYSGx8Z9UgMwV-y4cK8LdImKdW-XSOHu0QptaS3H7BLRU7-yeSCo3wO2hMie-__B-QziQCQmi4vogX3NWOJLH4OB-cwyAY8hi02vL_EHhcoznAU4S8DT0KEClF1O2Fy-czPnPGIzlrblMbTGunlPus0_bTukmBqS2Zl1W8HkEnW6_1vulUxxOf5RXfe8rcx5Eu0Q7F3WMPb7mJ5tiO3F1TM7VGJgpgMaNEjXWS6BRZ30nEUwBqvhbix7XfgQExDoEhsoqOdmyEnlvHqxpgZXpicpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=ues5Q5Dy6IdrSgc4Pl8gQVSmVZH565l7AMIQSNmiUIwPUWdAYmvPlpgwTQNWoIYSGx8Z9UgMwV-y4cK8LdImKdW-XSOHu0QptaS3H7BLRU7-yeSCo3wO2hMie-__B-QziQCQmi4vogX3NWOJLH4OB-cwyAY8hi02vL_EHhcoznAU4S8DT0KEClF1O2Fy-czPnPGIzlrblMbTGunlPus0_bTukmBqS2Zl1W8HkEnW6_1vulUxxOf5RXfe8rcx5Eu0Q7F3WMPb7mJ5tiO3F1TM7VGJgpgMaNEjXWS6BRZ30nEUwBqvhbix7XfgQExDoEhsoqOdmyEnlvHqxpgZXpicpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j56CA6guxzAHHlt0G9KNMZNvr3YI8y9sj2A0wsufMwEXWaCGhBDTTxLQTe49UMPbWL1ij6s9Cp9uuXaAzl4ptrMXzEBRAFTqGS1bf3H3IldSHIJ3_4s8iaEmd6aNpZOfOBB65ZJRt6ibuCUgYidXBke14-U3updOrk_qzad3H5r9fjwMf1fetVSeI78F2_wNdyePZjtHKWDT0Ahtnr2vgtSFSZDsoD-J3xd6FnH4lsXAm_-Lcge3KTtGZ0Qskx3udQQ4Z-6t3J3KEe0Acq7-GsAKxFsFIOh53QFWy9My4mPe8xEZFSIyw8nMzR-Csf2IsHSzugTPrNPoboIPMC1w1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=rW6rMBmVF1xIJQeOEVPQgJZUERs9Tmf0etKnnMwZuFE8-n1GrVlHbLeT_WaJluHNm6-IMFlkJFOoaF3zJ1kgm2dFBdl_mhDok0qUyvOTdQ76zZnSqqznh5g7k7dll1_D4_9pOD134Hv9cgIXh6JNkhN2J4TvCvFHXX_ZKniWF3O4TDS_4vxFBr6ExXjcepYXbcVFBa9JbH0cD7AWsl2ZnMd2wGBeNlFV3OW5GSHBLwmkrJiKIsnhFQimFGgsgt9w2XEosRdlPx-rlXbinUmmXz_hY5AxbhzwauHnaErnDH9mzCfrnvGrWNDLSpcwjhRVNR8MDHLYR6lRqyHMpzp_2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=rW6rMBmVF1xIJQeOEVPQgJZUERs9Tmf0etKnnMwZuFE8-n1GrVlHbLeT_WaJluHNm6-IMFlkJFOoaF3zJ1kgm2dFBdl_mhDok0qUyvOTdQ76zZnSqqznh5g7k7dll1_D4_9pOD134Hv9cgIXh6JNkhN2J4TvCvFHXX_ZKniWF3O4TDS_4vxFBr6ExXjcepYXbcVFBa9JbH0cD7AWsl2ZnMd2wGBeNlFV3OW5GSHBLwmkrJiKIsnhFQimFGgsgt9w2XEosRdlPx-rlXbinUmmXz_hY5AxbhzwauHnaErnDH9mzCfrnvGrWNDLSpcwjhRVNR8MDHLYR6lRqyHMpzp_2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=RmllHmD5mICzEycoo2v2JRZK9T1ofVxFU2XEUrHPbj5n0JP9rGEy4HM9xt_aLvJpciJQO7kmb7nO9RiDw4R9HkIDofV4dwEEA2h2hHoH0I5j_eVAp-opG_OmQKrbfdI2ngswfad-yLRSellMF6DLIoLBoNv-bBgh7MJnYtg_rf67EboqU9xBZX0ssx6oDcQ9L1rGmJsWaoEjjA2fU5dyNTo5ntQ2Idbqs40RqZhc0A1n4oAjONoKDmuCExEyhhtMU1CEsqDc0FCA2lfpAi3126RlqQ2FZwWYao_vL-9TXcEo4XLpGZMDJdnI0bJO9KDyZcKzMj5soIzkFE0tb_v76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=RmllHmD5mICzEycoo2v2JRZK9T1ofVxFU2XEUrHPbj5n0JP9rGEy4HM9xt_aLvJpciJQO7kmb7nO9RiDw4R9HkIDofV4dwEEA2h2hHoH0I5j_eVAp-opG_OmQKrbfdI2ngswfad-yLRSellMF6DLIoLBoNv-bBgh7MJnYtg_rf67EboqU9xBZX0ssx6oDcQ9L1rGmJsWaoEjjA2fU5dyNTo5ntQ2Idbqs40RqZhc0A1n4oAjONoKDmuCExEyhhtMU1CEsqDc0FCA2lfpAi3126RlqQ2FZwWYao_vL-9TXcEo4XLpGZMDJdnI0bJO9KDyZcKzMj5soIzkFE0tb_v76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=HWisO_dEGYOf2hMM6pWU_al0epsg6OK4kOeCcRtykBRR1n5-QlA3xkpQUdD5dwiiG-ZCTQB39JQ758mj8WziaPxbV13dmJhgX5D8gJPCOHcqFudQmvC-YqwNMAiGHlW-d7i7OCAyjOprXNX4S32Bm3YFQy-cCp4ks-wqhrh_Q9C17LYi8KP-LMu5RNv9fNXmP_1v9b4Ay7RVNcBE_HUzohLzulS_ZnPCoXZ4qVl6HbUIC_qZZdC7kS5O69uxzLS8iTZqX2bJ2LYUOdw6aCwBaPcPQPZf03fp4EOI0JYdgDGC-Aia_9sJ3mfIcXRnqA3BfFBGVC3h8SHj9bRHfAT2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=HWisO_dEGYOf2hMM6pWU_al0epsg6OK4kOeCcRtykBRR1n5-QlA3xkpQUdD5dwiiG-ZCTQB39JQ758mj8WziaPxbV13dmJhgX5D8gJPCOHcqFudQmvC-YqwNMAiGHlW-d7i7OCAyjOprXNX4S32Bm3YFQy-cCp4ks-wqhrh_Q9C17LYi8KP-LMu5RNv9fNXmP_1v9b4Ay7RVNcBE_HUzohLzulS_ZnPCoXZ4qVl6HbUIC_qZZdC7kS5O69uxzLS8iTZqX2bJ2LYUOdw6aCwBaPcPQPZf03fp4EOI0JYdgDGC-Aia_9sJ3mfIcXRnqA3BfFBGVC3h8SHj9bRHfAT2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms-RXTGf5EiwquIw597wCCh0DeewFVE1_kRUrnXrhkN76ZQtCeTezbrARf9flCDVqsSJ2yMoKVPjQXOjxDOx4I1GyKX7P3bRXvAj3j_ZYjoWtpxpF8UbXY5Mg92MjUrbjPbGoFg2y40ACozB5XATaKg4a2RlbnePMB48Ez3tmpIi3X22A42nri0a8ralabfw-WPKu83HyKkn2SNRkntDFBQl7fxC4tp8cjl-ayZGC1WB-9bZeGa3qylY_e92lMG__R1XsEnEYjj_-klNiS8HxRg5qBlLgzSvT3VCKNZJyHB7IgpIZwMi8_uLp4OCh-luQhm1JbiZl1-CuIPBQbNoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZI7N0wPrY0UyxGmNDti-R5wAtwuRjd7agoOzzqrhX8oG97PgTFVE9AmhW5h5aQAJ5l7ejOKVevbwnZXf4MeQFxLNUfPRpq3U3qTsdoTj_A6Z9LDnHMN6yIXWmQI6JkwjZCSWVHfitvq4Pdzb1Ini1LlbQd6J3fm-WeuGyOgztrY7Z1a6n2TOlCw1i9B3GIIqqYH-pDiYPXs7VzZjjoVmHLLWYmF9LPJ3f_Tbmkj3oUvzrzyli6oUNFE_kciOiIIALs-6uVbSbiNjlCdkafMt6nxh2XZLwQ9cTuIwoWClT5PPvU8sHvTImsnYH1S7ZY5sOGQXxYNo62BoR9e8PLwIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mi_81w_GLx8r0rYTMz60q4pplhoqRICc7ffcZA_kyu2nAVXWA1je1A0H0MAsnasIuhlHAqOrceEQu4FnByo59zuxyDWG-l2BP1JdfyoddVyfiiGtBJzrG3EEcdENEQgSiOg0QugH3u6xvWT1XmoS3H43BNPBbz9cubutBsbgcOf9hl1RSMZxv37n4co-oUfxw9iuLdtj8XT1DslffzS_eukD-oDy0Y5vpFG_GnOgNlbpS6Lfo4qz0KJw7RIOjLUEyO4UVn7uXLt_ldgWhf4mhQeoSwqZrQxV2pC1puWw64k-KB5oH38XZNNqmKRmv_BDhsgGF788DF8jTqrL0Psipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQL6QN50wBVROAfKT-7b6th4TwTEo42jmWgyFGU11YGMUpAP5E7IGL5hUBPLEY3p7ttKzM10MUhNI1DN7ak1n2PPYyfrlP5wDPtcKYGMH084IyNjjxUdvtwHOhs02r7k44RLP8hQtPTTIvxNLAqrMIYALFX2VLEzpFQySUgx5cd6VVDQ8Xk1AGLyGqvDoMlTEpMkiJTzMrdDBaRDn912xNufVK8PnaFkA_0L4HEH0vir3EDP-l8RkWqy38RStEX0FdYtdvWy9mJzffnrNdz5k8vI3LxNdb7Lcl5Wtc6GjBin6_Lx4YjLzYztkI0ylUSXDYIQop_75Wrx0cnMliNJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCuMV01sQgtQNLsB1ZwLTFMgVfXJEC6kfaWLKtvmwbkWqdcWyicGEJrOIcPywxCxeBA9zEbxPEvZ3Wh_0Kesy3RMW2Gl4ywbZtcApDyuYS01d4BbWO8pYopx3sl4Y9ZmJMmxk0O-C9RvnHU4nKi99XzhTkC0C5CeQ1Rrkgmy99mdL_xj-40OgE24Zm4mQrtC7EbRNPks_3qPGSONlbMDCnOC_-WAEf46U0PXeXKERGBz4mGNi66OYcpaqt0QJIQeYYd87MvHeei4KGJuxzaFfxKihJy9Xp1rEGqpPqfSYng4ElmhzE_I1ejZ9n9AW8GY84gElw_ushfjaDoiwBeqlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=L4OsQULhRml2jsIumvgu0mJgIy1MqwovoCDcr5mf0TEfDnXLAKUXgkzZ7GpWkBRWBYiNClJycWmWkOweOaq_3QioZbqNdE0fU43NmViIVzagMNmQP3rH9Zc3y5goQsOZKC-5g9moT05UBkZGjeu3aLQzpM5r90mhUDCBbj7M6GWrCKGN2so5QUnd-bWnMQHG9Ce8cnibwus4HHcvfIDXQwpFHuvm9QG4tmsESDob_AD8D_rnPpNH6_ZQ20shXUOm9yoQbHRAK3zcXDEVHbWg354-vezehm057SCrRhaBAOEEQWWfsnhIjrceDNJ4EbNn7Z4FsobVTksh0ORrsExayA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=L4OsQULhRml2jsIumvgu0mJgIy1MqwovoCDcr5mf0TEfDnXLAKUXgkzZ7GpWkBRWBYiNClJycWmWkOweOaq_3QioZbqNdE0fU43NmViIVzagMNmQP3rH9Zc3y5goQsOZKC-5g9moT05UBkZGjeu3aLQzpM5r90mhUDCBbj7M6GWrCKGN2so5QUnd-bWnMQHG9Ce8cnibwus4HHcvfIDXQwpFHuvm9QG4tmsESDob_AD8D_rnPpNH6_ZQ20shXUOm9yoQbHRAK3zcXDEVHbWg354-vezehm057SCrRhaBAOEEQWWfsnhIjrceDNJ4EbNn7Z4FsobVTksh0ORrsExayA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jE2rdo3YZF96wT5gLJ1MCJYJus9KhUZIoJwJN4E-DmeREji1iRAHYMnxmNmvpmuJnWTapGOco4dE6MT-7RaE_M48EgJENNHH0nGxCLwZIIk__FymAjR0Ee7OgcRr2uMfSPo2Nt06-Ifq8S07a_GpFBzRu-uC8HOoAj7jhtS1CVWX6wndvxNIp3kEdCQF7May_de-yllM9FkuDK8jpXWTSqmlBaD96qA0pYn97W4S_PkcsnPPecWJvKGJ7gN5UGP5oHKkncB0nCIe-RwWuioE4B4ATZTlVNfZxNm8yLXmcs4dxH2EYpp2WBFUnNyvCQUrLKhL-1NIzF07JT_4tCTq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
