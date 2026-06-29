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
<img src="https://cdn4.telesco.pe/file/GqPjsC8fnTI1h9DSArFKyY88nYzUyyqvjWsQ9SxBq437Fzqp6aUmPkOzzCCvCjBeI9U-uXU46NGm5xnS74JDk9LkePyhw7gqtSqVaQUyilEEjGwGvnwlM76e6qplViV5nMBE-raX6lXOYOamZqtTgQbb90ofL95WAgHHk8SKvE0D-2VxYbHqWln6CXD-YFQl9kqn318MwjgNS-EqBsXp0PCivfHOEZF7Eay7rTI_77WzYe7_Z4r0oCop7Ewxw20CGSCH3GSUe0x4uXQts37EeIFxRWEc-HQcPgaK9I7K1hIcS5f_WczzseyajQklgbf5zvz1s9kjF3JwrlzTECDrXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=W9K0aaYzXKkogDC09EjsQrHW--IFmjI_o48cJxhPaSd641tXIisW2oAvqK9TXl0Ue4aS7MScn-ZLeVpPVubM22a6jWmcGUZN143JyTNaipCwMjd5AyEwVFDA770k4P_t_pZR71FtWSxh_avclzi4r_b3lrJbIBZ6rw632lLN3ZsrvQ0LJPUPFUV0dFQP3QbHaCBgFMPjZLQN_SRhuHaXwq3Dm2Y8DQfTqFFjFSIpwUZLPmi_y24hsrHWLXbqLtTctZeH3MC2_uvX5lgZe4fCCpGCTLZ0xAYPPf07J_0apBjqrVNfo7rWyQcm4bKu27mjrmOMlQQifpvNDsWaBo4v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=W9K0aaYzXKkogDC09EjsQrHW--IFmjI_o48cJxhPaSd641tXIisW2oAvqK9TXl0Ue4aS7MScn-ZLeVpPVubM22a6jWmcGUZN143JyTNaipCwMjd5AyEwVFDA770k4P_t_pZR71FtWSxh_avclzi4r_b3lrJbIBZ6rw632lLN3ZsrvQ0LJPUPFUV0dFQP3QbHaCBgFMPjZLQN_SRhuHaXwq3Dm2Y8DQfTqFFjFSIpwUZLPmi_y24hsrHWLXbqLtTctZeH3MC2_uvX5lgZe4fCCpGCTLZ0xAYPPf07J_0apBjqrVNfo7rWyQcm4bKu27mjrmOMlQQifpvNDsWaBo4v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC_qbp_ehhZLKouky5yBMjqgqFbbPuC9QpgUYObg-JPm3C-GNvdNtAWCLw7g6BavAdS58gs0ZTV9dKW3Y6viVzY_ncD_p8TkqrtTPwmXJEy3sBozLcDS7EmOJpukd083i94iHbJzTytA7OFHVPv6p6EDbFiRWGoBavDYsue6UqvG70tls0qHCKsiSQ-qBEWcGLRGvCe6KlNYZ5cTCDUXE011x_ZLsm4GZg9Uj90YSx554UV__5GrJxpLc5Jy7Hw0u9j49FRE8siBdGvssMTf1Ec8-tV74z0G0NS1QoG3q3-iRmDm_XQKruTrIzWBrf94fyUCa_HAi9fz_clbJCDI4EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC_qbp_ehhZLKouky5yBMjqgqFbbPuC9QpgUYObg-JPm3C-GNvdNtAWCLw7g6BavAdS58gs0ZTV9dKW3Y6viVzY_ncD_p8TkqrtTPwmXJEy3sBozLcDS7EmOJpukd083i94iHbJzTytA7OFHVPv6p6EDbFiRWGoBavDYsue6UqvG70tls0qHCKsiSQ-qBEWcGLRGvCe6KlNYZ5cTCDUXE011x_ZLsm4GZg9Uj90YSx554UV__5GrJxpLc5Jy7Hw0u9j49FRE8siBdGvssMTf1Ec8-tV74z0G0NS1QoG3q3-iRmDm_XQKruTrIzWBrf94fyUCa_HAi9fz_clbJCDI4EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 710 · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQ1Eu_c7uc0qLfFMRBbg_5EnQUhrhw6-mQB_l0sK15qH0JL6lHrNRyxFmQvt_emo0xCYYusi2_fpbfg4CgJgXYfRVEN2siVv-C5AY3--xrRVvP_s6600S2jm2fe3zI54HseA-XDr-VcRySrRhPm4IaXZm5ryRsJwfxGu0qXLFWc2qKj_H6yRnX9RkASK3xDszs0mWoRtcqTcBGTizmlki6Tgm1fmGHKbYDrTeUPGPkrXFktyo-t-GrvyiLR4uTnnd582eYoni7OKwPqBQpcOFE5Kcj6wD5ORbhhnbdb23miYvCmn9M7YCwH_QvmKUAmnPuI3UX3_7aaBW08PlbXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Pp5CvmChm2_VFJ5bi61zJSdsWFw_bFPJwiK8WO3inktA2wqBbQc6B8h5Im-KmCfkcjIGvbSEfBT-gr5s3UCLM8OUos5F52Q6sHOA-d2eERkbzBbkslekOqxnpssrioj1ygXKFc20rMvfVEyrbGkn0yDRjyhSEt2ifcJR3rny3JdU_zig-ZWAwRc8m4--sFtT-zKBBvo-wntYrK_c00spE7oE_pIPM2z6RLL-l0iBsOwhLy-_fqZ3bdL3b5WDNnVa6A6Uj0JCnsg_4dpei9CHW0zssFemDybPGG-3j4hR34_kAwuHKaDA4kn-Qb-T-i8lA3XO4Ibt8-IKUWG33R8NRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Pp5CvmChm2_VFJ5bi61zJSdsWFw_bFPJwiK8WO3inktA2wqBbQc6B8h5Im-KmCfkcjIGvbSEfBT-gr5s3UCLM8OUos5F52Q6sHOA-d2eERkbzBbkslekOqxnpssrioj1ygXKFc20rMvfVEyrbGkn0yDRjyhSEt2ifcJR3rny3JdU_zig-ZWAwRc8m4--sFtT-zKBBvo-wntYrK_c00spE7oE_pIPM2z6RLL-l0iBsOwhLy-_fqZ3bdL3b5WDNnVa6A6Uj0JCnsg_4dpei9CHW0zssFemDybPGG-3j4hR34_kAwuHKaDA4kn-Qb-T-i8lA3XO4Ibt8-IKUWG33R8NRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4O0MwHF3GmuG9-4-GBdtOHGa-JbZnz8qlhK7Z8IVeniTihw0j4XZSh5CbwRu6fyAO80I025IiwMTXd2Zf0W3XUwKLyQVieLX4khthgrfZRhtmb3XxmEHnK9XD0uPsvmY5bUE5QZLkbhWoWUvZykDtKVoyZz16qzsm-uPDP4DOoQBOxNBwjLHvty-KUCEgJfsWVyEjTkUtk7CcXnwjN32iSJ2t5d-pMe_i-lyYDQaJs4WOaX17dgOLiAPyCJuABhjivEcbCtPukMY9Ngg0Hbv2YnuEp59HVcIvQDz7QdoMeNa7m6H7WDWHdrimgUUtDGTurh45Mb402Lr9ZshrsPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=sFXhCu7IXspHxMQwXoNuo1GRc6PG-YLrVttlIRN1Xq8iKsb1w7JEUWafom8MfI-eoJ7bN4yobLO4vBpWFheNtxYxey5xC1tPCG12ofLd1MCpPsAm0WdqzwkSHjph3vhVYUSyx3BK2Zi3YYFDKtgCJps2CEbgl2zUDJZ_nxnVvhqbJketFAn83iqu5HgtQqosnZMzlT7KFPgfRHv0oOqnAAF65k7_1Nn4V2WxQvs9mWE_PnLD0Ur6ngLDVKwvTQ5iQgEONLkEye1Yr8PICjeAAJyqzlwJJfwoun-2oiRtMejDvhA-nSb-PhrLAzvbdkl96Qow8v_egxDAv4bz217Bb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=sFXhCu7IXspHxMQwXoNuo1GRc6PG-YLrVttlIRN1Xq8iKsb1w7JEUWafom8MfI-eoJ7bN4yobLO4vBpWFheNtxYxey5xC1tPCG12ofLd1MCpPsAm0WdqzwkSHjph3vhVYUSyx3BK2Zi3YYFDKtgCJps2CEbgl2zUDJZ_nxnVvhqbJketFAn83iqu5HgtQqosnZMzlT7KFPgfRHv0oOqnAAF65k7_1Nn4V2WxQvs9mWE_PnLD0Ur6ngLDVKwvTQ5iQgEONLkEye1Yr8PICjeAAJyqzlwJJfwoun-2oiRtMejDvhA-nSb-PhrLAzvbdkl96Qow8v_egxDAv4bz217Bb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=aWX1Kd0xnyv_FbRl5uQoj9L_tG9cm21uD42z95tHvzAl-Vb_6aXCSF6bN_OCzCTTsJBGGUMREi0vWUVhTqGJST0zmAFqHTa0Tx3wkFTY9y8Cg030ARykwUz0AQE6tmI63q3B0aMZk0kEMkcYE2CS4IeG-q5T0ocW-VTcO1nVrmUfykqO_8ThCcMAlaZF65o82wxAsrRf5t-1Cf9VcwRQzA4pu7TNGn7tDFe2VykzyB3nNlyJkR5pmla7UrAkAcD07GIwqCo5-MKqYrVc2oeIHUMNxdUnsROnGXXWfAh9ED8d86w25taGpTJngxmHDcCWcdV2Srw3jSm9LrU3cbuevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=aWX1Kd0xnyv_FbRl5uQoj9L_tG9cm21uD42z95tHvzAl-Vb_6aXCSF6bN_OCzCTTsJBGGUMREi0vWUVhTqGJST0zmAFqHTa0Tx3wkFTY9y8Cg030ARykwUz0AQE6tmI63q3B0aMZk0kEMkcYE2CS4IeG-q5T0ocW-VTcO1nVrmUfykqO_8ThCcMAlaZF65o82wxAsrRf5t-1Cf9VcwRQzA4pu7TNGn7tDFe2VykzyB3nNlyJkR5pmla7UrAkAcD07GIwqCo5-MKqYrVc2oeIHUMNxdUnsROnGXXWfAh9ED8d86w25taGpTJngxmHDcCWcdV2Srw3jSm9LrU3cbuevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=bLXjwm27Lb33g4glsWa1W-gVxQAJTH0_L1b87zrD_k6eLkXKkB65I1BP9qHho7f5YjbvrluTlm_2oBMoBMWI7aTdeh-5_iwUoelHA4lkglDiYViZ9q2yLLcEfpG0RFwNZZo_R8ySThe1p5KgmcMPW69WFbvGUOc5cen92xyvYVtXLKhCuT8KhJjcNAaWrfpdhepcDTnlAD1eQUcekoVjO2K5wxJ6Y7tGw7vH9CUetYUx-9qDz2MLh2ZWfVnvRhRWsWEKpT7NriYAt-ySaTUqbL2vnO-9Xis5QroEyT_iQkGqhC4nlyFR_ZYDgdJedvJ1ZdSeNZeY6p85gjyT6w7MEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=bLXjwm27Lb33g4glsWa1W-gVxQAJTH0_L1b87zrD_k6eLkXKkB65I1BP9qHho7f5YjbvrluTlm_2oBMoBMWI7aTdeh-5_iwUoelHA4lkglDiYViZ9q2yLLcEfpG0RFwNZZo_R8ySThe1p5KgmcMPW69WFbvGUOc5cen92xyvYVtXLKhCuT8KhJjcNAaWrfpdhepcDTnlAD1eQUcekoVjO2K5wxJ6Y7tGw7vH9CUetYUx-9qDz2MLh2ZWfVnvRhRWsWEKpT7NriYAt-ySaTUqbL2vnO-9Xis5QroEyT_iQkGqhC4nlyFR_ZYDgdJedvJ1ZdSeNZeY6p85gjyT6w7MEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=WaRHR9_-tQ2vSMqAHTQheZJv8VCKZOoG7WIJ8z727-Junb63NJssxAuuPuE3pI5Jtbf8dTG2N4OGQK4j3cnHWjh_YwZ_dX59bHWyHNhhIeUzPOxx9SyMdz7U2oKaB6PyBQupUUz12cdKmNmzLNb04HLwJzgWwT2xMqsnwHu3ysQ-F27bKujQeUpDVeqMMJQKS6i5rMhXvcxLePnxbW2hsjd-alaqYwDojCXWMccBjdJWUyjavfyMrNr1NfcwoIhDjo-7TLLZ5gjs-tBCl5jX0ARZD2sLxXmxcOjH9IZka44j17qUTsHr1Z63aCsVTVlJGR8UufMrrrgSIu5ai4lX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=WaRHR9_-tQ2vSMqAHTQheZJv8VCKZOoG7WIJ8z727-Junb63NJssxAuuPuE3pI5Jtbf8dTG2N4OGQK4j3cnHWjh_YwZ_dX59bHWyHNhhIeUzPOxx9SyMdz7U2oKaB6PyBQupUUz12cdKmNmzLNb04HLwJzgWwT2xMqsnwHu3ysQ-F27bKujQeUpDVeqMMJQKS6i5rMhXvcxLePnxbW2hsjd-alaqYwDojCXWMccBjdJWUyjavfyMrNr1NfcwoIhDjo-7TLLZ5gjs-tBCl5jX0ARZD2sLxXmxcOjH9IZka44j17qUTsHr1Z63aCsVTVlJGR8UufMrrrgSIu5ai4lX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=mCAyh6JCj2KwFEC6UdBUN_3VL5cUFjoCnlUNRpgq0M7ylXxdCLWs4IjZW4Sb1oQXt-wOc1_siHZIx5QX0lZgNDera-Ud5Wvi0NNdW1SYbKdgfBowF8FZc5UGnoTfiUDQGmN5GVIpL_5iIQLCoWfyl0_K6CLVojB6mcPq-ymeGKoEwbJksWHR69PmvxYI8UAHLjUtIS52C6pdg38EIvrmMJg-CBH8zmUzymsCRI5cp4QqIDoZZBelz4hDAR9qFkuW-w5OvYiopn_Fy2EZPv65mToRYSqNuIEQdtT35N12Rc4FOP-ZsAPTzAxmatxi2XkXKSxO5R16zhYMDpTm5COMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=mCAyh6JCj2KwFEC6UdBUN_3VL5cUFjoCnlUNRpgq0M7ylXxdCLWs4IjZW4Sb1oQXt-wOc1_siHZIx5QX0lZgNDera-Ud5Wvi0NNdW1SYbKdgfBowF8FZc5UGnoTfiUDQGmN5GVIpL_5iIQLCoWfyl0_K6CLVojB6mcPq-ymeGKoEwbJksWHR69PmvxYI8UAHLjUtIS52C6pdg38EIvrmMJg-CBH8zmUzymsCRI5cp4QqIDoZZBelz4hDAR9qFkuW-w5OvYiopn_Fy2EZPv65mToRYSqNuIEQdtT35N12Rc4FOP-ZsAPTzAxmatxi2XkXKSxO5R16zhYMDpTm5COMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=RonKPUjP6T7WmSo-Y-_vXcKSaUCzYbNBPqQ2IDQGYkkxyREgvfjg8Q8Dyeqgk7lGBYwmUVO6GsxhEECO1ZY0vcjUmHslc3Uo56Qv76vYrQP0HmGghIaMSUrQA6qH7lAKPC1boCkk7XNpGfOxSnbCU9hwmVVX3UhQV8aUwEWVDrBMPh0CM8t_Bym8X1dZCdVTMXG3f06-NWLFeeU_kW2pZbipOk8cZ7erf-SrUvp9jVnu9CGE04FzUOgDV0xIk00u41YT0tGeUe8LuI0oD2NP4NvqYr3kefYFCplhXImIBWu52VHjROYi5zZNAA7iSp_RIesG38FnINoqLSFDmKl0Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=RonKPUjP6T7WmSo-Y-_vXcKSaUCzYbNBPqQ2IDQGYkkxyREgvfjg8Q8Dyeqgk7lGBYwmUVO6GsxhEECO1ZY0vcjUmHslc3Uo56Qv76vYrQP0HmGghIaMSUrQA6qH7lAKPC1boCkk7XNpGfOxSnbCU9hwmVVX3UhQV8aUwEWVDrBMPh0CM8t_Bym8X1dZCdVTMXG3f06-NWLFeeU_kW2pZbipOk8cZ7erf-SrUvp9jVnu9CGE04FzUOgDV0xIk00u41YT0tGeUe8LuI0oD2NP4NvqYr3kefYFCplhXImIBWu52VHjROYi5zZNAA7iSp_RIesG38FnINoqLSFDmKl0Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=BPLc6_2ms4X03eDVQCSuygjGXj7orD1K9-MtkQ9dmeGDfV9GHJpypbSD-fkR03ZDRBE4Exp8diOu8yyVjWdia0_E4eyq0Rmmkxhu_DY3Lxp8DxATNCpORYlncQhzTl7q15aZawPtnQ1XNS4eyUcQFiDN5VTMz8JFlgyU06LpjvPEPn0MgmM-W2lgHuygHTYTMOUnETz6GSC66hL3bHjWkpvxf-0bYH-90WsiBNpaXQ9Mjn2eBN-qU0lSkvRbSujgnUQxgzZAQL1PiBAvulpZfedibzY_1cTjrHRi0MMyXNPp2IslDycANZ6r1RN2lpiVoAH79eI-kLutFbozV-Sv4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=BPLc6_2ms4X03eDVQCSuygjGXj7orD1K9-MtkQ9dmeGDfV9GHJpypbSD-fkR03ZDRBE4Exp8diOu8yyVjWdia0_E4eyq0Rmmkxhu_DY3Lxp8DxATNCpORYlncQhzTl7q15aZawPtnQ1XNS4eyUcQFiDN5VTMz8JFlgyU06LpjvPEPn0MgmM-W2lgHuygHTYTMOUnETz6GSC66hL3bHjWkpvxf-0bYH-90WsiBNpaXQ9Mjn2eBN-qU0lSkvRbSujgnUQxgzZAQL1PiBAvulpZfedibzY_1cTjrHRi0MMyXNPp2IslDycANZ6r1RN2lpiVoAH79eI-kLutFbozV-Sv4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcooEuKYzXSrS5sDVJzabcHgqG0EcdBMB-Y_JCg3C8Krzl4HvTlej8Ah9ieEJa-8oYkYj2cwe9VS_IaGO49-r-nz4K81ZWeyNxxzRsI4bGKZ2vSTdmKzKJHBv_FQzj7JjmEThHj4B8z18N_2fR6mQwUKRmorjZIEKs7qPAW9711LLLYqYM5jFfVHOMXzYF8_E0pUF0Evdl8OC9Xh0G2s4Fwpbkt0woRxE_PCNN1oVQ7atZbvwSzWrp8KfVTlqKPOP6VqiZ3gPU5vV7pzGSrFdp5cy2K8AE-xC1BWg6DObrlrBt5X9UtPF1vrGQyGAf_Mxw_U_ZPX4nrEufemfFlhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR3otybLs2aRRcLN4mW4OkqeTKkxlqjQIUkEX9Wppe6FrF1XrFFepfsgZ0p6YWjrHOC8MLaM3SStfuqvSoRPDgUjWPl5BBmtgZFvzREdI1oG2ouBPBme07EIvxJ5CZQfWPEt-EhN44sVZj4VW2F2AXV94glHalycAk0SUClFD25PNXRFUFgYDkpKqKPItnXNMwiUY2AP9_7Czr0AlxPrJpn_rM8LdRVZB-boivAty_yQ4ZAcrre6vSHfEQq6d7tL8oN0PfBc-TSF3U0e5PpQwSZp54FN6wlqRSgzNr-uT-sbqPms6EzoCRUG6Qp-H98VXbei18GrI1KiWfvlWaLrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mu3hUBLJ7-enozJzDojnB_0_o7SdXlX_oD9SvTu5lOjXBsse-b9fJnH2EB0kj5QDuQ7V2jrw7K91GU1KCjfu5q7DHgffLbrMgcS3aHTDbqm9FZlIU6dt0sbtWip_0NYlTOsEjo2tsYd1Vw1sPQzZIhIQBrSM2Fem7E4E8TwAUTfNBw9wI5vMQzcdDSqKh91CCUWb25F2eUqxFdK588luEb96K1mSmVUI8NKNIVFCYd5MU4saGRrRpy4HSaIvt3u6xb5-GlMaYDtH5U81dDpDzDcChUxlD7fliBfpfAvZdlzD8IStE-tL-bokFfRnqkYaNKp4cbBnbOthvzN6mQqlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=o0va46qdIpLUVhtLwk-dfVjI7-Dps5LsldJAQANvLdwrUOsmOGC31LpQPm_UpSbdJeO7wrGqsTLIGLI0cDG3J56wSjGULLeMZ2PPEuittMrJt1JrlgqLsDHfUsxReBE1tKeOu_mtB26P8P02l6Fww-2_qpcsOzc3rlDOlRGNygZSkG8fruNayz4GJFMJZVKm0UwFBKWBZSRYW-3pImWdbORepn5u-sD2gOcHDsZRoggXTdLiVS3oyo1P2PqsvIKbXj5MMIQ4EbjOfUSd5J_onlgpGTPVCxt-xKN_zMXf1xmqESg8q8Nir5Dh3uPtmHniUopu6VsU_1AM4qQsuT5g8rvy9hwLjk8ZB99iDJxqgCMPDc3JL_uZiT5jARHL03lOmaJre0c1ExtlDHDyN5pIg98QNl5hjN5f1O0L70aCFXYgPW4wXmCOofWzLhZ9evLuaRc6zQ7PbEkclKHXBQpZ0R6m7VOl0TCu_71ebkhqFSbOeWFbUjyUWKROqTj-sh82SpfwyNv0H8Ca_63kkbRmR3lP25mHN0Kdc1WGiu5pOmUDhxghh3QKfehO-UWv_ppLBf6ruuvPA0_4ru2RSVIX-gKwInl8qLMbLU6KFsQCNL7fYEfLpFppOK0XIh0erGG_P1HBylVKmfsDd0Y7Q7MZzPRLGwOID2x9LO2KkUHAahY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=o0va46qdIpLUVhtLwk-dfVjI7-Dps5LsldJAQANvLdwrUOsmOGC31LpQPm_UpSbdJeO7wrGqsTLIGLI0cDG3J56wSjGULLeMZ2PPEuittMrJt1JrlgqLsDHfUsxReBE1tKeOu_mtB26P8P02l6Fww-2_qpcsOzc3rlDOlRGNygZSkG8fruNayz4GJFMJZVKm0UwFBKWBZSRYW-3pImWdbORepn5u-sD2gOcHDsZRoggXTdLiVS3oyo1P2PqsvIKbXj5MMIQ4EbjOfUSd5J_onlgpGTPVCxt-xKN_zMXf1xmqESg8q8Nir5Dh3uPtmHniUopu6VsU_1AM4qQsuT5g8rvy9hwLjk8ZB99iDJxqgCMPDc3JL_uZiT5jARHL03lOmaJre0c1ExtlDHDyN5pIg98QNl5hjN5f1O0L70aCFXYgPW4wXmCOofWzLhZ9evLuaRc6zQ7PbEkclKHXBQpZ0R6m7VOl0TCu_71ebkhqFSbOeWFbUjyUWKROqTj-sh82SpfwyNv0H8Ca_63kkbRmR3lP25mHN0Kdc1WGiu5pOmUDhxghh3QKfehO-UWv_ppLBf6ruuvPA0_4ru2RSVIX-gKwInl8qLMbLU6KFsQCNL7fYEfLpFppOK0XIh0erGG_P1HBylVKmfsDd0Y7Q7MZzPRLGwOID2x9LO2KkUHAahY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdEhpHlpzfRLUmIiiACtbk4VruEym-8yMhJUI3ws_KrtOOVah5v4yncrkoT24qXAJod9AQUAmz9oT6WdH9esAUF8j2JF50fuBunxsyanTppbajCWi131vuUkREO7GwwADzYU3gGFV2t7JI-IddVi4oaxIxTVAPk4kAxGOJuWYWnczK4_PX6its-vvHYrM8UZyMELaghydCLvkPrS3vL1Ypd9IQuWSws-EPykhhlpi2CxTyDpPmhOdR7OOoGgc8C-ydC-rc0ywcgaGxZbQIMApbxi9JfJS_B1gJhfgTaQW7F8rV6HIYkgabftrtYEAc3AcEUWbUWnkqA_LkXLEIin_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=G406c2S-_dYlMw4kDTU66txGuG2oFeEIxTiJZJ-JULqbAxjiR3jnnjgmxPNmHCzpLOltf2ysRwMLhxx5CGDjUwztFRIYGkHC6KyFwTWNXAJLUFOR1mos1MbDRByAGxq7NiLwKLKaNtH7lhIKy1JlwGmuszC-x9ly8uGzPfZRf0ziau5yMF8iUWkYnvq4soNZdcdyK02r3nWMlkGNPmdo0DKfM5hOGauY_vC2iHTGSrLWGjwY6KbvyB4XQG9xo0JLy1gaV84NjGKLL5XuJRqZHWRXt_kgEkQIKlxd3FwPLF3uqCfMxAK-9jWilpCfAN7XgVKWOHHIGJ-pcmj8S_pZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=G406c2S-_dYlMw4kDTU66txGuG2oFeEIxTiJZJ-JULqbAxjiR3jnnjgmxPNmHCzpLOltf2ysRwMLhxx5CGDjUwztFRIYGkHC6KyFwTWNXAJLUFOR1mos1MbDRByAGxq7NiLwKLKaNtH7lhIKy1JlwGmuszC-x9ly8uGzPfZRf0ziau5yMF8iUWkYnvq4soNZdcdyK02r3nWMlkGNPmdo0DKfM5hOGauY_vC2iHTGSrLWGjwY6KbvyB4XQG9xo0JLy1gaV84NjGKLL5XuJRqZHWRXt_kgEkQIKlxd3FwPLF3uqCfMxAK-9jWilpCfAN7XgVKWOHHIGJ-pcmj8S_pZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=a2H8XsKrIa5N9tvRoARqQi0fIp-oCavmu7n5CdHQpWGHOfUpSi6g7JHN4DwsTVE-2PB5m9EKs796bYvUgeZ0FOuPK0NLH12QeWXCP_jHnkHwK4uGRgQufcpsOy0pOuZTp67aRvGHQttjeCds2xqYnnIJmnSfuUZw5zyG2GlxYaAzluPy3Vebq7r6us1fS6INOZQBQLr7K4UcviOj99486jxzG2PCBKA8kyWSNrf7leO3kyKWwGcJNAbg69OWFDjwgJce9J3pl9bvVsxBSeGNfI33-EfQbSTrY2p9Fs7ik7YDgVyugiHSys55ebVK8krkZXFvwuSJXbh4jdUXdeknCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=a2H8XsKrIa5N9tvRoARqQi0fIp-oCavmu7n5CdHQpWGHOfUpSi6g7JHN4DwsTVE-2PB5m9EKs796bYvUgeZ0FOuPK0NLH12QeWXCP_jHnkHwK4uGRgQufcpsOy0pOuZTp67aRvGHQttjeCds2xqYnnIJmnSfuUZw5zyG2GlxYaAzluPy3Vebq7r6us1fS6INOZQBQLr7K4UcviOj99486jxzG2PCBKA8kyWSNrf7leO3kyKWwGcJNAbg69OWFDjwgJce9J3pl9bvVsxBSeGNfI33-EfQbSTrY2p9Fs7ik7YDgVyugiHSys55ebVK8krkZXFvwuSJXbh4jdUXdeknCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=nFstDO0puA0PKfLIsGDB7gSffiPESqA1GmWe8CoMspohaSFEQsBYFLSNPq80YMgBYCvbRyCml_V5Iy5sElxPQPSdcyIlsha1D-PzaEm-1ycr1BmRvacSdT5ToaRULoQfhHlcI9eJHIixZOWg3hzEj0jnLnSxyGlmD_vyqU5X-KGOZkwzbtGypcz7Pzev7cAmj8E43oynVChO1A5fjaGqGaQOjIDxLJjyXQh7QFPsgTKHrfkEzs2M8WnoivI6Efisa_pvnrU-vnM_utogPm1uarqh6ABVGdn8z3iCciTZ_CNfbD1lZMCbHdkw2XY3qfSvZlAcI9UfQBxJqNKFNcrwtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=nFstDO0puA0PKfLIsGDB7gSffiPESqA1GmWe8CoMspohaSFEQsBYFLSNPq80YMgBYCvbRyCml_V5Iy5sElxPQPSdcyIlsha1D-PzaEm-1ycr1BmRvacSdT5ToaRULoQfhHlcI9eJHIixZOWg3hzEj0jnLnSxyGlmD_vyqU5X-KGOZkwzbtGypcz7Pzev7cAmj8E43oynVChO1A5fjaGqGaQOjIDxLJjyXQh7QFPsgTKHrfkEzs2M8WnoivI6Efisa_pvnrU-vnM_utogPm1uarqh6ABVGdn8z3iCciTZ_CNfbD1lZMCbHdkw2XY3qfSvZlAcI9UfQBxJqNKFNcrwtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=tMbgw8EXpigUC-SVqV-UTWKYl4CGG929eOBvXKkGDLH6qeD9mByOehdb-dK-g4f7BtC2Te57XHi0sfN4N6D32D-DTHMO5Qxu7_tat1o_yehqdObgUFkRttEKXcZknV7WyBCH-DNYFFe-Y1vGDs0yKkC0-G-Kd-ywPuCeBrQULD0ewK9DDSM8p6xi7kd6Clf0yuGwgIX9Wqc7G53-5kRWXxoZ5ybnGlq-U6qPEJjt1ia1TVl5BZwy9XH2GQV8B5vXtUHr4Lnz_XGsN-A2gMtqSIMZoJBNjQoT3KVn3nZF6IHAgSHKfieoWkUwTEnk86KRo2iG1MM3xfyup1G2Zgvg1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=tMbgw8EXpigUC-SVqV-UTWKYl4CGG929eOBvXKkGDLH6qeD9mByOehdb-dK-g4f7BtC2Te57XHi0sfN4N6D32D-DTHMO5Qxu7_tat1o_yehqdObgUFkRttEKXcZknV7WyBCH-DNYFFe-Y1vGDs0yKkC0-G-Kd-ywPuCeBrQULD0ewK9DDSM8p6xi7kd6Clf0yuGwgIX9Wqc7G53-5kRWXxoZ5ybnGlq-U6qPEJjt1ia1TVl5BZwy9XH2GQV8B5vXtUHr4Lnz_XGsN-A2gMtqSIMZoJBNjQoT3KVn3nZF6IHAgSHKfieoWkUwTEnk86KRo2iG1MM3xfyup1G2Zgvg1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRmKh7nnoiq_slPtrr3Fdqxci7VwlvKthqGrG1ZbdRd6qs6NtVUYN15HzKPOoKOKlvsDSxn142MSm85U1UNCGIoQhzmyF7VTVp6Dft_h21YiCRtUfTUuWLLt27yTK2tCFt6VwDcfXXV8gfu799HSFdOWE0xmqzuAB_Fy7SDXEkqN41qdy-7CpKeSaU6k8kXJN4tdKiYJeiz0unUk7SsfsjXQMqI6NagWjLXpxpRpTqd2RYyLA8h0jO7vqr72eurz6c8tuscLm72b4E917uWuIkSUNlBBg5t8PB8TWRlOMQifF4vGk87lq3ltsHq57-eanyEBotUxDn3ulgZtlnFwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d3I5-z_7Y7DNTklRrH5f7YcXFj53m6IkciNAwH4e0f9Q9dVakBRKo-w5XkmF6z3gHsZADx8JWMdfmubYjBP4hThsv1twz9vgfjoM7QffqKPgWY2wiVFlQV6dStKWSlLY9T-gRlQ4rLFdJFxAWhjtmm_9ai7YuGKocI7y9f_3_uitDgirsCh67Awi1Elb87wGEDZ_KWIVUrsfaYcinAMK0ZZ0NtC6_nOGx4Rl5cUTcpJyrv56K3UT8PlqJjahWyPC2vZAP7S6P8EM8n-UTa9hM9nbW9Ye-Z5n4Bzhk7mPhP4HMs8QEbhTvfLq9vX13Lq52T2QkzUcWTUzv9WfdPm2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=U703xLSKUrBylcF8ZjRPUA0t-4HkgL2Xt1kAQ9FexaQfwJ9M24RIqdutFNrOM-U4_NX_hEtsf6YLWOeYjHTYdqGtkOeMM4XrUfDeALnemob4xKX2duntZQzBPRpwBJgTeMQAalgbVrUraBTstpeLzZ-VYqLQePCDp4DBfcNHbGdJWjtprP34SsHKbsx1A4YlDD37zwf_EeWeOdBzf6QAcpOANVePYdh0dOdv5_s1H8-iPnmm-ZJ3XwpF0_3IWbTQaXS-av5lOfVvhWrxisJc_CakWwQGlWJylCdCdzWEaUh4R77OCVwCGoZMgk2ob_U4QosQjkzFrLSKlri2JbVJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=U703xLSKUrBylcF8ZjRPUA0t-4HkgL2Xt1kAQ9FexaQfwJ9M24RIqdutFNrOM-U4_NX_hEtsf6YLWOeYjHTYdqGtkOeMM4XrUfDeALnemob4xKX2duntZQzBPRpwBJgTeMQAalgbVrUraBTstpeLzZ-VYqLQePCDp4DBfcNHbGdJWjtprP34SsHKbsx1A4YlDD37zwf_EeWeOdBzf6QAcpOANVePYdh0dOdv5_s1H8-iPnmm-ZJ3XwpF0_3IWbTQaXS-av5lOfVvhWrxisJc_CakWwQGlWJylCdCdzWEaUh4R77OCVwCGoZMgk2ob_U4QosQjkzFrLSKlri2JbVJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=b_gA2j5SJsjea9Vra2-JhfXwi8F_3vdAYXSiBm5_himwXeji-H35Ied1JIwHS6i8jjAAN6gLKWlBsboE3FhaCHa649CLsVUEGyB6CxiIHGQr0372DfHXdTIzKhmtT1v3WCjXZm2hbWof7djyjOoepxFdTzBnP97I9qTcGfp0BH_qPUFa2W2XBjHnH3QA0aCn6DZX94pK_enehxklKUzYbP0DEC4wvagl77yX94iChxADbo5n5VlddCXcuIvmE1mtV7GXd_eo1_N8G4KKIjoNDIDWhkYlNuyENQyzHa23lGyYrqLgftnoAQmR-rbUz5UmmtVBe4aAPdM6GM-JYptwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=b_gA2j5SJsjea9Vra2-JhfXwi8F_3vdAYXSiBm5_himwXeji-H35Ied1JIwHS6i8jjAAN6gLKWlBsboE3FhaCHa649CLsVUEGyB6CxiIHGQr0372DfHXdTIzKhmtT1v3WCjXZm2hbWof7djyjOoepxFdTzBnP97I9qTcGfp0BH_qPUFa2W2XBjHnH3QA0aCn6DZX94pK_enehxklKUzYbP0DEC4wvagl77yX94iChxADbo5n5VlddCXcuIvmE1mtV7GXd_eo1_N8G4KKIjoNDIDWhkYlNuyENQyzHa23lGyYrqLgftnoAQmR-rbUz5UmmtVBe4aAPdM6GM-JYptwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIKyAcbe6jOalI81qg-Wf2PYNGxS3Xyc1NGroEx7GYosQOaIfFpkECFF1dZ7VW6yvmcKO3z0B9qXpwZ2C1JMv2NeVDfHd7mItCZXdBABAnJ2-96_n_N3DAF7Cp4ZOqyaP-iiWPP9NoGxlDyhnV67AK9ldZrgpRiN4tNUf286VqrKEskmJSaInyyMbmC3hPIj-uyHRaYH0pRDD8oqoiz1dI9s_vJFVtLVdwTJFn1U7kaYALtTByQfh6frgCiNXwX93u0Nvpr2qT9EhqjGiaLdHbxbvvzADh8hRRkk5RhfSMlffjc8Bgs3F2lAyuDOlZRTOrHgJAyepFSog88sHHlBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=KgDK9MXozrVHAzR-jl2WfCwdfifWQ22BoGIweyPWmG9SJ3cdDoj6xr8uce-szzjEdQz_UcNb0sJNjLk2eK2NhFsWf-R6_MyMAMVhqlCZPeblq0znic-LDcSkO7B9KHV4TNo27sJBXh74kwzy6qm-IO3BTaVgr84NtII6nD4f9iYrzeEkqWlmlC5aORxThqLWd1wX8JHVfoi7s-a77DjgF23YVks3TMhDWpM2zKhzyxtB2vcxoyLQy4egu5owbyBwyIpOjRg_etGcsaIBU7flVaMHXiyCC1S6gw0bmSRc-o_Pg7_N9PTIDaa0EhhL6yQpzSrVv4LmbDIPEmGM7hJTCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=KgDK9MXozrVHAzR-jl2WfCwdfifWQ22BoGIweyPWmG9SJ3cdDoj6xr8uce-szzjEdQz_UcNb0sJNjLk2eK2NhFsWf-R6_MyMAMVhqlCZPeblq0znic-LDcSkO7B9KHV4TNo27sJBXh74kwzy6qm-IO3BTaVgr84NtII6nD4f9iYrzeEkqWlmlC5aORxThqLWd1wX8JHVfoi7s-a77DjgF23YVks3TMhDWpM2zKhzyxtB2vcxoyLQy4egu5owbyBwyIpOjRg_etGcsaIBU7flVaMHXiyCC1S6gw0bmSRc-o_Pg7_N9PTIDaa0EhhL6yQpzSrVv4LmbDIPEmGM7hJTCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=pSnT9hS2m9Z-qZAKNnBF4Psk_vtKenEy1dRqQ846nZvKauEaTGtwNgfcOeHsjubzwss2qHWhln5tVMXey7UsGbU9K8l8TPc_T-3oWYBewC2XMDAby2hMB46YPr2b7Ap22Y6OwXHX3sxToZo2t_5o3glB8dQpfzQvkO5QkD7fP6wX3lY5Wn3HP1T74LSAbQw0SbFa5t829nz4ZEeE1CzM94StSiJ5aHc-SInueoGminyICCfTBjWGLqqA3hYG0xKjepPNAu1ZbvGfg8c5Xch3SMsaBNllbDHqghy0sOwbCc5olPHdnBEw48s9Q9W6w3Kxtk7ZLoome6P21g0TEQb3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=pSnT9hS2m9Z-qZAKNnBF4Psk_vtKenEy1dRqQ846nZvKauEaTGtwNgfcOeHsjubzwss2qHWhln5tVMXey7UsGbU9K8l8TPc_T-3oWYBewC2XMDAby2hMB46YPr2b7Ap22Y6OwXHX3sxToZo2t_5o3glB8dQpfzQvkO5QkD7fP6wX3lY5Wn3HP1T74LSAbQw0SbFa5t829nz4ZEeE1CzM94StSiJ5aHc-SInueoGminyICCfTBjWGLqqA3hYG0xKjepPNAu1ZbvGfg8c5Xch3SMsaBNllbDHqghy0sOwbCc5olPHdnBEw48s9Q9W6w3Kxtk7ZLoome6P21g0TEQb3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzEEGbKZw04pM43XFg9hVOKS088sU5WONtVi-EKHXnOSEHmI8yJyP-kcI5g88Du0pFgX_U5OkUTlMrf_M39NctiZ2ziV7upKI2iMQn7X7dCxXBuEMQJ33LB4iqHP3KR7u8NPswOZrBhxK1SF0GGQqwxAes0EZXM9DVVJ8i6Vj0Yd2yVfmNAy-v8RjkeDDcKVEgm2un5PtVexxgr0OUZn_ll2pbDyGKrFXsLNDhNOsf5bkDofrqkOvx0Aux_S9ThJr1-mxVSH8W6O_lQYnUbYhA6w9TaQ--NerhLfl6lzqgidpFFfb6Iz3DyQslOaUxiEQXeWcU4bvKDnHDhANjrLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5CbxqBCbZNfKB-oicOdslLQwd2p-mguZrWJAdEWoF_PyYASCrFcuA7ku9agFIorEquIbvdCk9-7ZVLZL0n_fE3WRb2poAR7OAcLHKAfhKgK1_oaZrIXTX4OfGAcx5p6aqrK17R1NNaZ5omW0kY4lJ7GsTtRWTds7P5KXJvcNRa1HKhXOK4turOl7XWhdFxiSWit6u_7_ZYNoQR7eoKFkBGCnw5XLGsJfANjqvhjusvMlyqI1DI0An39zqi33JBM6lsHsfXRrV-aYUh2dbZLEsYBnSpbW4UXS3Td2Q5m1gkKNzFEVSGECUgw29avmXQhJ53EVqNOGaNYGk8aD9p8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g_cdoHUzktIDI3yvzOs2fnShIlJ4oqlxi6hUynUQ9AD6hOVr9UP-QbWc6fKNEI9_wODSty_a8Wv22qF4lBW9iNtGuyWTx0BldvA6enxFyOb9DzRLrfsCVDLJWSg8I8Zek7axcV9M78f7Yjl2znf2SAVtUmm9F5ggrjl3nU2VsdRtpfr1_r9eogscCW6cfySizYmdl8-ZBQb7pU48_F-3cPIFmTIperDvFI8-XSjdA1DO8aAejRdVAGzDHV_zcDIl7fvYNBw2Zm4USHx5g0hXqTpqwk3dHfKqV9Jsw21hfsh84ULdsmXtafkMzklHsL5XramXNbONQkdT-AVMtM95tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=RM8URCoPja9_-GldV3Tqds4lN7xLGInjj3Dfe5ovHNK1br6L5yJYVhR2UzzP-vyY6FG8-ylZEYCZvfnhvF_nWuP4NDkwaUkTBQRper9alaeqDjACnQ2Fl4qnYHqhfbkpCsyqMvwEn3xCjwhdeXKBgoSeFLiejCvNHcDHYdyVMlDM5ZSWo1MDAUzWy6geBzv5QHlDPif2dD26O7eA1vx9P3SbWRZbMkvPjxfHtpYm1LHvwSU5i_DCgrPQWrgbFrieI0rFoLGuz6Pw6dqC-7VeRyMvx3yD_gPr8CdGvVQOF3kMsovk2liXFNr-liiGa9YAGWnAxycTLQ7XvTWk-I1Bdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=RM8URCoPja9_-GldV3Tqds4lN7xLGInjj3Dfe5ovHNK1br6L5yJYVhR2UzzP-vyY6FG8-ylZEYCZvfnhvF_nWuP4NDkwaUkTBQRper9alaeqDjACnQ2Fl4qnYHqhfbkpCsyqMvwEn3xCjwhdeXKBgoSeFLiejCvNHcDHYdyVMlDM5ZSWo1MDAUzWy6geBzv5QHlDPif2dD26O7eA1vx9P3SbWRZbMkvPjxfHtpYm1LHvwSU5i_DCgrPQWrgbFrieI0rFoLGuz6Pw6dqC-7VeRyMvx3yD_gPr8CdGvVQOF3kMsovk2liXFNr-liiGa9YAGWnAxycTLQ7XvTWk-I1Bdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7KuLaq3DTSJDRmwCLuSw4b0ow6pEhDJF8X5BGWLEDI5mjzy6kcTacpw5cIYS1DxFIFdgWT1Kqwvy6x-mTjkBHqCfK3ghBXlzoa-HzVi7uefpxaQwAlW_z63q8foM8B3AQz6bbMUKvSIm-iWbm9gFZT7ZnS4Jx7EJb-nsJXTmR9ociKtTfYzVEsHGFMeVTNMIUglAv_JjNtcEZ2kW56TKm28W3OqJjOph4pegeMd1RWVuMop1QHRuB4FcJbCCJZk_ENFeNFiUc2UlH_DR4Cmwft0zX6l-MQMRq_AptSYtX4Xy2RPxzNNJydHmPHmcVncoAbLl7SQKGwt-_Of2ibNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Furxq85L9NPxuwef1tu0dE38GlHie1bgp2N08zTtDMYN1oFX_H-psuRENdd_KCq0QOPpVqbvjedz2bO3qFjMNjRpAGulCKVNc0-GaiXtsbMUQxZxC7T10-bkj7tmpXkvjhEaNb-a_UDKPm6zeHBeN_vCcNsQxFRiQKwyy4eeFE_9WWtw-kWJltap_aJhKvP15SaarB5ckzHay29oOly6nZIg5ikKzFC6ATd8dCbdt07da6frIujbKKFZjvpbnmFrVjaCCJp0ETc0pNDG2d5Zc0iuyUe-TVBT_Rpme9PO_1OVQjLrZFzH06CCNXqI1C5_sugwWArF_bfV2OTiZoBVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=RoxVfxccfwIsMajAjp3jAjrxzCLWsnZj7PKFunEurZGRGSUnIcS2sJmtkyOha8WKarUbQboqonRjBwcwZesv00IOoejLq_GbWj8sFhJYBFYHhy40g_X8dGqcFZV_aw9VCD6f9npE-ZJgrFM0dU8ri0EMdZtDxdbadWzamK3lGGeg3suLHOWwMd-8PuhzHKalEU_ZiubWl9A_thbzthkU5h4s-8Tpj0nNT32UUiJGEAYgxxqyxQcWpwFupNExPtqb40nwV8b315noWGsqkvR7ZfWjsnoWLesWuohO-62eeWcuHducWCBSJ-2vAbSeRxoINN6AyVbbE8NhDWSpYZ7-Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=RoxVfxccfwIsMajAjp3jAjrxzCLWsnZj7PKFunEurZGRGSUnIcS2sJmtkyOha8WKarUbQboqonRjBwcwZesv00IOoejLq_GbWj8sFhJYBFYHhy40g_X8dGqcFZV_aw9VCD6f9npE-ZJgrFM0dU8ri0EMdZtDxdbadWzamK3lGGeg3suLHOWwMd-8PuhzHKalEU_ZiubWl9A_thbzthkU5h4s-8Tpj0nNT32UUiJGEAYgxxqyxQcWpwFupNExPtqb40nwV8b315noWGsqkvR7ZfWjsnoWLesWuohO-62eeWcuHducWCBSJ-2vAbSeRxoINN6AyVbbE8NhDWSpYZ7-Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=ICigWhJg8jkew0irU7IJUVBevsgS355CRUMI8j2Rf77hKyZZHt4XMQKpIeI5zD1MHlNQqqfUtNpbDAPa2HhgjiX_g4kX9XtIg6hD2Cr_EYXSENZySPiXkH9tQ5z3LfP7k7-ahbZhiArxqUO2ZCh_pkbbUVojux30IM3VMJw49SqeX3f3bGdao0MXPvreHiv-d2dU1Dbu4eYjYHjPcXnp-2zCFPPjyytVSUjlUnu843TlCbOfZBRtVJVHPRuYyEMi9BlUzz5Q_r4CEcrtAo1prCxXdABc5I3j3d1u6tnCx7cjDIZCt1K1DStKKeaUWsLJjgB3da4Y5PP4vhWz8NkKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=ICigWhJg8jkew0irU7IJUVBevsgS355CRUMI8j2Rf77hKyZZHt4XMQKpIeI5zD1MHlNQqqfUtNpbDAPa2HhgjiX_g4kX9XtIg6hD2Cr_EYXSENZySPiXkH9tQ5z3LfP7k7-ahbZhiArxqUO2ZCh_pkbbUVojux30IM3VMJw49SqeX3f3bGdao0MXPvreHiv-d2dU1Dbu4eYjYHjPcXnp-2zCFPPjyytVSUjlUnu843TlCbOfZBRtVJVHPRuYyEMi9BlUzz5Q_r4CEcrtAo1prCxXdABc5I3j3d1u6tnCx7cjDIZCt1K1DStKKeaUWsLJjgB3da4Y5PP4vhWz8NkKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=SQwM-jkEJE7Pc_3a1DZ5LSiG7BbizDnNYsqqQNNnGSvzvYJ33YKq_2nlJZWepcXQjeX7FiwBvrWl_2XoYgW1wSSr3fRcsRg9gu8ptyfChNOS6zQRnbhRPowJ2sXHcKbVl9hCDNeJxflPjtAMG7Z2AR3mXQoqgT0aoQlLUjxPjyNqP2UpmIS1PrDUvMO3-SoZxRFo5hAzsHdpFyWzaEE4KKdfo853Pm66PiBTcoe49dflY08mN5U7o-sRGN8RT1r4t1JDNHXef1WuAY3GtXE_gtbr-C2ThwbCMHiuxqiQ2PJoVLCSCVig7bJK40WH8uLyp16nBUd6A-8hZ-g1z4zhmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=SQwM-jkEJE7Pc_3a1DZ5LSiG7BbizDnNYsqqQNNnGSvzvYJ33YKq_2nlJZWepcXQjeX7FiwBvrWl_2XoYgW1wSSr3fRcsRg9gu8ptyfChNOS6zQRnbhRPowJ2sXHcKbVl9hCDNeJxflPjtAMG7Z2AR3mXQoqgT0aoQlLUjxPjyNqP2UpmIS1PrDUvMO3-SoZxRFo5hAzsHdpFyWzaEE4KKdfo853Pm66PiBTcoe49dflY08mN5U7o-sRGN8RT1r4t1JDNHXef1WuAY3GtXE_gtbr-C2ThwbCMHiuxqiQ2PJoVLCSCVig7bJK40WH8uLyp16nBUd6A-8hZ-g1z4zhmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=DA26gUzNfOJm7MDcR6eTzxGX6yJlNwYugwAb-luM-tIxDIuJ7OvopVBtEerm9t9wUaGMoUDoJQR5KUgGvx25QGGyRwC_DZxxoYb9UcTeokt94Glzq1tWKJcQRKkfDYn1hslFyA4TURtbQMjM1xORHkFH9Ve8iEYx8RqytfntKCdzBEMTj5G3ZS-RWGIfDOOkBWFuVKOFLgR8Kzcp7WWjx1235ZtYwzjIO0zWp7Pd-23E3BdwJx52dQh5kd3x10aaZFFgyz8jPOFGShFt_X4Eby7TDgebkPk4iLImnrd1CMbpcsTR01GecDh6cc8SBJpihjI_SQn3lqqvZ7sD3sYHpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=DA26gUzNfOJm7MDcR6eTzxGX6yJlNwYugwAb-luM-tIxDIuJ7OvopVBtEerm9t9wUaGMoUDoJQR5KUgGvx25QGGyRwC_DZxxoYb9UcTeokt94Glzq1tWKJcQRKkfDYn1hslFyA4TURtbQMjM1xORHkFH9Ve8iEYx8RqytfntKCdzBEMTj5G3ZS-RWGIfDOOkBWFuVKOFLgR8Kzcp7WWjx1235ZtYwzjIO0zWp7Pd-23E3BdwJx52dQh5kd3x10aaZFFgyz8jPOFGShFt_X4Eby7TDgebkPk4iLImnrd1CMbpcsTR01GecDh6cc8SBJpihjI_SQn3lqqvZ7sD3sYHpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFmozWRgE-HCCQdQnPUEiLzeCvULWFKcfJPEqmKKyR_sLKXXtCMjjD8YfhNLthMl9_TFAgaw83l4Cs7U1Y2MWpozm_VI1QErB_X75g2vENYMFlfl9UYsRD0jne8f2u3UNIYd8bJCZy78DzAYDtgaWsa07gkbbhuyH2b7mLyLuGMTZCuiMz69Mbv_JlNyHIFZkBqA-ucOJpDiPOVC_Jn1UrJd26r1hxaA7QeOhdHHZjB2eP5NcFl5xu7Um7tTlwS-TUyBIulGpARfoMPAfcaY8OEHs_8fEjsTN1nwZrcWD14Ck1S3cUMjlMYTkuP9jdmyfxAsWwaRiWNz1iKEp-8mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=CNoglvSsAPjG4fZ6nO4tn0yfXq_Zya8j3mKlIHA1Tsy0QT2Jnn1Q0IiznxQLB3dTUlm2QY4b111S1joHlmCP_0IljEk7x2C-yIatc3W40KFcRWZObm0V1kkmr2gOkSoaALW3ihILK6hnRPWEjoHaUVNFhbJpgliDLEN0mbBOknDSmY_vC-MSXXB6PxL1IJg8XDlK-3-GovuSQPAmePYaL49VXnJcNKh759QxGFOpyoF1wNIjJtWkrAKuNTFJGsHYWKcaKcBrdUDz7n-pFDnstgEYrIvfMxl7k8G30_m6dqRQCeT194uZQlnqNf1OdihfhsrRUEbUzC2ZE7wcQN6_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=CNoglvSsAPjG4fZ6nO4tn0yfXq_Zya8j3mKlIHA1Tsy0QT2Jnn1Q0IiznxQLB3dTUlm2QY4b111S1joHlmCP_0IljEk7x2C-yIatc3W40KFcRWZObm0V1kkmr2gOkSoaALW3ihILK6hnRPWEjoHaUVNFhbJpgliDLEN0mbBOknDSmY_vC-MSXXB6PxL1IJg8XDlK-3-GovuSQPAmePYaL49VXnJcNKh759QxGFOpyoF1wNIjJtWkrAKuNTFJGsHYWKcaKcBrdUDz7n-pFDnstgEYrIvfMxl7k8G30_m6dqRQCeT194uZQlnqNf1OdihfhsrRUEbUzC2ZE7wcQN6_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=FcD7vio-DEYYEppdf74dGQnP6-SOOpbBBOvtsTllCWvRLIjVX-HAATVfSSdpiHgQf6i7zhJAAI2KX6rGA7kU1mFpfI0u5Lj8w2g6HEhjjSDeQFy3BFJjpswk7N1lCzi2bAzkUjcUr5Ftn29ki-BiS6IM7xUgtsMSUtwd5VRjE31g_tYxEc_zxSTyWy4toeY_PiogkairF_md5ZNNxXVsGjD982v0XxSn94xwnBuT4iWBzvrd2pZTTrIRgwNhd1SEGQNlcGJGLPyzWmx79ayiAHDa8vSPlscesuhTuIMQhP-xT0PltGdRvAJUemY0TMreREXR7hxO_EreKUseBy5nQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=FcD7vio-DEYYEppdf74dGQnP6-SOOpbBBOvtsTllCWvRLIjVX-HAATVfSSdpiHgQf6i7zhJAAI2KX6rGA7kU1mFpfI0u5Lj8w2g6HEhjjSDeQFy3BFJjpswk7N1lCzi2bAzkUjcUr5Ftn29ki-BiS6IM7xUgtsMSUtwd5VRjE31g_tYxEc_zxSTyWy4toeY_PiogkairF_md5ZNNxXVsGjD982v0XxSn94xwnBuT4iWBzvrd2pZTTrIRgwNhd1SEGQNlcGJGLPyzWmx79ayiAHDa8vSPlscesuhTuIMQhP-xT0PltGdRvAJUemY0TMreREXR7hxO_EreKUseBy5nQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKsznp0JhZU3Z3XxggJMRnz00YWrzxtGBgAbeZjpDfwP0hRS8yiHjy8CF-iOcohlWJ5bKhsyP09V9vPlrNR58TttWvRmhkyjoLlc4IysevAhdEul84-sfOHm-oslrJsh-XCgETDVP_8BNsbd6Ysx8GBxxDZEnULs27l65Qj0OiRLYF77C-ZQ1D-lIAMDOXqOqOFlHfID3sH4E_8whsLPsCgoHr1R8yVo4_eeVGRrOal4Bt3XikxCGFlo--gb5MaSr5wukRasagC9csn_fdrsihycotc_ze0u7vdWye8WSFLoERqmGvBlfSs61cZ3ESv9IMBuHFb7QepFOIV0OKFTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3nvzLHrYibUNDhkAkZhOLCiVp4Jsl2huVVR6bIGdfpE3Y5uu3cVwVt0f1DEGLsAHdpeW_wpZx3v8BsC7IVL695-2kquQp3A9hF7xo26yNfmi0Wupqk5U2S7OhEnyEYub2aSj7U6E_x7BamP8qR1AR4hdMcp98_cVKpmYIXLrrsN9P1Rwo6qXP7qqE3GKuzBpR_YoSeAeAxZiaV4Eyfyg1ckE9R3o1xeWzepe6D_1mLXu60MziUrEGv_E3uGMbxoFs7tqtP9RDC6_qlnV1qRFvGCkJheYarn6uGn1iaX2heH_LwNP4AYWGiz7AL1Cz5i4B65vTlwD1tzQ1cKydElww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqCfrNSY41FFBzPpBQXR4R9IiVvYgaEX7zSNQaRstlkX1NELbmLJenZrOr-AINx4StwNqnl237OZe0yPcb3ppl6tI1QWvS_By20MTFlhnn3JrhmyYS8j4P6W8jfqy3-XdUMYBNItI_LJXtpTa9yA5L_gDgZTsxx8eHGEemFnqqCR5Icm0BXUT8zckv5rnRgrwkncPpEb6aUcm7Aj_67CalTCdNAp2mZXQMNFcQfTUu4xVX1janhRasWY71judS3FsekE63lRqBuz7DM9ZOzBM8agYQy0d1-aaf-tkiPQwPctF9GECwKP9VRt4VW5KooE0FOHlsEq84ZWYoogV28BCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=EOKt34CTXjrHd0taJTa5GZlIWwlF0SAvx1dAJyqLJQv0tAzw9UDVUIGIU_xPUuzWEBzGNWUac8vbFBFj5RhJhDR-SwLb7uBq5PJ6VUtnXuAb3Uw8i-9kK14rLC79i1zQILD0wTNlYzumQc5VusOBo9vBZo6_DyB92rYbo-q_WgWvm8Uy4WBX1bKw9lWoUxwC03bJvsYtRCIYCrPNo73K1gpEjhcLqIzt_c631TiE5toWAB-jyC7YkHM_df3HnvXY9ckHPZEwfIVIGN2CdND_4CkqOez3TsxAh_pXDlcumSNrDmjSAIJkCkOqmrzphg9Qa2fw4tYmQ9LqrYKRrJn1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=EOKt34CTXjrHd0taJTa5GZlIWwlF0SAvx1dAJyqLJQv0tAzw9UDVUIGIU_xPUuzWEBzGNWUac8vbFBFj5RhJhDR-SwLb7uBq5PJ6VUtnXuAb3Uw8i-9kK14rLC79i1zQILD0wTNlYzumQc5VusOBo9vBZo6_DyB92rYbo-q_WgWvm8Uy4WBX1bKw9lWoUxwC03bJvsYtRCIYCrPNo73K1gpEjhcLqIzt_c631TiE5toWAB-jyC7YkHM_df3HnvXY9ckHPZEwfIVIGN2CdND_4CkqOez3TsxAh_pXDlcumSNrDmjSAIJkCkOqmrzphg9Qa2fw4tYmQ9LqrYKRrJn1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuIV1-RJVsQjc4NT1_lxA3abxjy3HkkCa-m_YUFevwkcfKtYJse8XDJvltTZYNabCksNRV9J3UXyP8t-yMN1V9W6DsvZmYK7DicxZajpRHiu1lBVC8gM-nNJsu5NGAJlwl5X0FeiiJOa7WVA1WKGnddGa8jpGV6eIq83S6fjlGC4EU1MQhHfnSTswQAEy0AXvYxeE0sSeFAju1B-za1f_aItssSOYaReNphXcB4QuWyXrqDnVQB6uZoRPwCNVL9bRmqEZc9rxCIlVYp7An3UFG4foqJ3YpuRxogz3zEATWy8cHajUdDTkCanaiP99Llq-OBAlfWeaMbOYhn99YjKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=o-Fjz5kduuzpjOiherp5ZHp-NxVQh96BWCvmBbScvcYhT3Ewnt4YWbKpCUKX409eSOsVBxBgsOPX4xSBaBzQMVNTJZe8jRbrU-N3khuRw7O75WDcuDxlI8uykTByvtoNA1TSXA5v5QUejdlYTS44w88yAtKsodUbb6-QYb6Y0TqFwE-_9vU-m3H4fwnkm0HZoeoGvKK7HUrSRBVSYAOmdAm61yFZYpE_Y3eWE54Z12V9bIJT-4X_nhvAq61YeB_VpV4kt8Ljg3DTUk4jUnYIgbMlZn97l3qGLF3NOyPa9K970HRmUsTrQ9E7vXuZA8PCO4nnaKA2_FrRKsXOX4qtAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=o-Fjz5kduuzpjOiherp5ZHp-NxVQh96BWCvmBbScvcYhT3Ewnt4YWbKpCUKX409eSOsVBxBgsOPX4xSBaBzQMVNTJZe8jRbrU-N3khuRw7O75WDcuDxlI8uykTByvtoNA1TSXA5v5QUejdlYTS44w88yAtKsodUbb6-QYb6Y0TqFwE-_9vU-m3H4fwnkm0HZoeoGvKK7HUrSRBVSYAOmdAm61yFZYpE_Y3eWE54Z12V9bIJT-4X_nhvAq61YeB_VpV4kt8Ljg3DTUk4jUnYIgbMlZn97l3qGLF3NOyPa9K970HRmUsTrQ9E7vXuZA8PCO4nnaKA2_FrRKsXOX4qtAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=svdQjPH_M-oSwCzrnZkPw1yWabgSVJ8BP_PvR9Aa8EBCkh39QfK9JylST7lVm-Z5SUrjUVH8V4C4qG8hqw1dZK2m6PWsQmDBMSe074s8BF7EbHP4fFOezL_Sfv7RbJw1oLcyqVLo_2UOo6zSBlrVKfArHHLWmoWs52NDebC30CjokjtzfNciB2fmjBX5KLLJfKbd55DiG6eUk339f9RNfkX_ujWxowPTj6NzOMusAkT8f22NSH2wd4saNJoS-RUdIHWsch5g5Sg-2rgQQiHGwh9XVkrFeOOWNxoabPfSHx-R4E9b79KPPc9xQ4zl144FRWCw7tcSL52m57WtkIh3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=svdQjPH_M-oSwCzrnZkPw1yWabgSVJ8BP_PvR9Aa8EBCkh39QfK9JylST7lVm-Z5SUrjUVH8V4C4qG8hqw1dZK2m6PWsQmDBMSe074s8BF7EbHP4fFOezL_Sfv7RbJw1oLcyqVLo_2UOo6zSBlrVKfArHHLWmoWs52NDebC30CjokjtzfNciB2fmjBX5KLLJfKbd55DiG6eUk339f9RNfkX_ujWxowPTj6NzOMusAkT8f22NSH2wd4saNJoS-RUdIHWsch5g5Sg-2rgQQiHGwh9XVkrFeOOWNxoabPfSHx-R4E9b79KPPc9xQ4zl144FRWCw7tcSL52m57WtkIh3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=PdEvDNbpqzcmn-UpWP1AaTM024kaChDKZk5RXI_ZBGam7JtgWtf40FEFExyZfznmDZKm26foxt9KNQMVj39K36Tq2ax2IPImcleH4Ev2IKh29jIu2RyjXP4iNwv8lBSe1nuzWRdA2-VcgcayXMpN_8ZXyD5vSKBaDUihFAx4HU2Bna7pzR6eQcX9rvKWcdyR4n0MHi24TTO2-MFay5g9UbhYdgLe-8a11ss7hhq94zjyrEExtO5bJ_a3JdWdDeQmAJkD1QdMTUe2xFBIdy5Ag3P9h3m5WVDy6P9JaL4srSrVlxPqIWMk8pc6PjQFbSlM8DkEfOBe1PUj6IE91StF2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=PdEvDNbpqzcmn-UpWP1AaTM024kaChDKZk5RXI_ZBGam7JtgWtf40FEFExyZfznmDZKm26foxt9KNQMVj39K36Tq2ax2IPImcleH4Ev2IKh29jIu2RyjXP4iNwv8lBSe1nuzWRdA2-VcgcayXMpN_8ZXyD5vSKBaDUihFAx4HU2Bna7pzR6eQcX9rvKWcdyR4n0MHi24TTO2-MFay5g9UbhYdgLe-8a11ss7hhq94zjyrEExtO5bJ_a3JdWdDeQmAJkD1QdMTUe2xFBIdy5Ag3P9h3m5WVDy6P9JaL4srSrVlxPqIWMk8pc6PjQFbSlM8DkEfOBe1PUj6IE91StF2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=ljK7M1F6IDIrF_h1gdxyw3Eittik2UgYDw_BQkKs_hu1RgK033VIn8P49xpCtvSCd7mQs3DjMq3tcJXzCRQdCKm8YewH40tG94HcaiRnz3jybx4qrTxnBS5GA5ExMY_4WY9uXFCB_3Qr4N9819afa1t409JkdHlLusHe_2J9WaQu78vdfwO4S866TyseNC0QmONfV4YmbLZx5J4PAMEb9Km8E555NMU-APfGdgBK6hQM8iZvOfZE7vldRF2Lw7nrIHco4OAxFz_E--zymhPYVk9fMx7I04I4P_NFajeRoOpUNQSOZ3zti8vGYvQyqAyRmwTPn5jgwYOFb_2IkMwAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=ljK7M1F6IDIrF_h1gdxyw3Eittik2UgYDw_BQkKs_hu1RgK033VIn8P49xpCtvSCd7mQs3DjMq3tcJXzCRQdCKm8YewH40tG94HcaiRnz3jybx4qrTxnBS5GA5ExMY_4WY9uXFCB_3Qr4N9819afa1t409JkdHlLusHe_2J9WaQu78vdfwO4S866TyseNC0QmONfV4YmbLZx5J4PAMEb9Km8E555NMU-APfGdgBK6hQM8iZvOfZE7vldRF2Lw7nrIHco4OAxFz_E--zymhPYVk9fMx7I04I4P_NFajeRoOpUNQSOZ3zti8vGYvQyqAyRmwTPn5jgwYOFb_2IkMwAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEybgw2HxlT0S3OMtvOfETPoyP67j7buIzYlV9nqM3uCxQLUuDo6A9HejVGZN1yE6nssyBod_Br_p5zfnsJWBQFqJ3atu-c2on5f2R9JwSDosV8B5OV-HhpyJaTi6km_udslluJ1q9IR3aLELceLIljNGMhFrlJPQFxbw3CIspmQi77G6CCtMLq-6BpSoys8RIZl-IO7u-fSkwML7IqLMX_EXQ7X_PJ0oAdnKE33LbTbQRZynW1FWyQ0-lmGiq8IpAIqo4nw-z2ER3TEzSoqWlzO6lODntHeqATzqkJUGyMaBrLCmO5AMfl26jgRLmuUcYAs9xsoptzT7GcwNVnS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f26avGBnM_HLFHOu4NaOdmeiyZJf_spRJqM3f-xNGm3S6L7V91pY8aVmSh2vle8dG-z2xj13pba6sa8scYJcidViO34H7Zg5IULF3PKHBWKpLAKP6Jst2eButl1wQTe72RiZB_swsc5QURSPaOebVCkSMGU3s8t1xzgWFqp44jDnmQqpV_c539KpBUiMY_viwmTaOAwh8_L8f1tVw2rpyL5jpB6_o_1AI1sT0WThbP7yTy2cWjCjJjOYUSf6tGvepsAzqul3nKwcTSZCAsoXBXZFv2ctcmPnbIKGl2rUfk6KY2qjiipa6Qb2OZJM-kmCDHRglVy3rhmVnwwBIBYH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=nVwagq0mQe4aeDN3qFtxYWulDiZMFhMQPGY_WMZJwg4qNcuGdZ9-irsQTw-IIYMomaWcE62LabTxlWo-iJhm-A1bBg5ixFor4VXUatJPCoRjzfiGKRy7f4-oK5pJ4Yf2L7Zo3X4iGbrZlylvwq_NhpO9oQIBy99767BWflOwx6uVXPGwb4dfSz_HvElf_km9UULNQyZv0STP5MAYlk_qSWlKz2YnmzYWBcMCLmBEN6YcKKm45sRT-hvfh5qdLmeH51hZnexj1Wo1VxO9lEzBDU3QTZNKrfiFXaU4YRSjGDOJXxDeJ1bylYDpsog4IqBrQxFMHpVu6maLnjmCRw4aqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=nVwagq0mQe4aeDN3qFtxYWulDiZMFhMQPGY_WMZJwg4qNcuGdZ9-irsQTw-IIYMomaWcE62LabTxlWo-iJhm-A1bBg5ixFor4VXUatJPCoRjzfiGKRy7f4-oK5pJ4Yf2L7Zo3X4iGbrZlylvwq_NhpO9oQIBy99767BWflOwx6uVXPGwb4dfSz_HvElf_km9UULNQyZv0STP5MAYlk_qSWlKz2YnmzYWBcMCLmBEN6YcKKm45sRT-hvfh5qdLmeH51hZnexj1Wo1VxO9lEzBDU3QTZNKrfiFXaU4YRSjGDOJXxDeJ1bylYDpsog4IqBrQxFMHpVu6maLnjmCRw4aqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=art9M5vLDOeHAwVBEaheBslOzINWa1_qxF4FWDN_TmuLO0wWdhXE7vMGjfuPaU71f3HzryM8eqfkt-2Zm8HVZw4jdscrkhASJILZV9Jp3-vY1fuVdflufM7lq4TsHXxJxtU5OL9efEeZTrQ4Jwv0DlEN6zymKAAYuvfRnnWnUgci4eBD5okHFoxqQXznz5OSMtSAIz062Oxp3cXgre9wKXjdH6wK84D7MoyQXRh1vUbE6mScGxoGLYMaQed4XutVeal8DFyQ2l6ZZTsV23PvwwzfpR32Agaz8kcMf351-K8ndBpTPC10hdHR32DY_Ighr0b02jXmoBCodGzVYBCdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=art9M5vLDOeHAwVBEaheBslOzINWa1_qxF4FWDN_TmuLO0wWdhXE7vMGjfuPaU71f3HzryM8eqfkt-2Zm8HVZw4jdscrkhASJILZV9Jp3-vY1fuVdflufM7lq4TsHXxJxtU5OL9efEeZTrQ4Jwv0DlEN6zymKAAYuvfRnnWnUgci4eBD5okHFoxqQXznz5OSMtSAIz062Oxp3cXgre9wKXjdH6wK84D7MoyQXRh1vUbE6mScGxoGLYMaQed4XutVeal8DFyQ2l6ZZTsV23PvwwzfpR32Agaz8kcMf351-K8ndBpTPC10hdHR32DY_Ighr0b02jXmoBCodGzVYBCdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDKmlyp3ZLweLSgI2WXtZhmGi_LGt4uDg5KicisJPfHxNOfcDvkYUmZAStkUjD1wIxw5LNsRt_a5vGOMLlbaqcGnqg_9ZHOf950mEDmI8pkzktuSHmo5IzObkoL_ROR-GwhAe70YyrWfZHrXux3r1SuXhxApvU6UzI3nnttItu06ZOJ7hpq3488aa4ZFhup4VTiGUivZlpm-rgFtL24RF1ktm4ISIOAx3bI5EIuGfIyPWrunS41_h5sbxps3vj9Ie-_8f8hDI68UVkueXsvMta3HowkeEslkvV15QTPm6eySFmQktMmAGgGhffUyNY28DZOAvEsYr4ik0xGB2VSkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=H2QIrLsQ2zqV8Bh7iUQROLgDOKlNHjtD6R5TbWJZwKCHtX-2rBsATlOcNSDRPv6vL_aldRQDmFcu1S_areTot7QL2HabCixCN9Hy-QYwHssGgoqIo_Mtwflaqdt6qk34agjs8P3B3BV54b3DU06KKixV5wVy8gorrEmWePD44LYUwpmBtgKJ6r7jJccF5U4rWP0Fm5aEtfPSkpknwXX01VBGmZuR6BCDrQR7Ya1KusaZMa9UoF9Y65FpTvE-4D7s0cL1pSJ-DI83BtrE_0TW4D_1mFi7-E87yrt9rky9nhNbPvOqov8NFEa3AGq_2u9ck88XIEej1br81z4iCety0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=H2QIrLsQ2zqV8Bh7iUQROLgDOKlNHjtD6R5TbWJZwKCHtX-2rBsATlOcNSDRPv6vL_aldRQDmFcu1S_areTot7QL2HabCixCN9Hy-QYwHssGgoqIo_Mtwflaqdt6qk34agjs8P3B3BV54b3DU06KKixV5wVy8gorrEmWePD44LYUwpmBtgKJ6r7jJccF5U4rWP0Fm5aEtfPSkpknwXX01VBGmZuR6BCDrQR7Ya1KusaZMa9UoF9Y65FpTvE-4D7s0cL1pSJ-DI83BtrE_0TW4D_1mFi7-E87yrt9rky9nhNbPvOqov8NFEa3AGq_2u9ck88XIEej1br81z4iCety0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=c22qDJc0VxireABessv_NA8d4nZ_yjbQbYXYjyRujfXyBDGcDy4BZNNIGwXWKpAtPzFkrmgyXBUEF0Xo_ylAvOCz7TH6Ej_74jCr041OfBFToEt59x23xgS-OASBFwD7IgDqfXVxJup45c5QJnd5Db_1XAhnApq-hroTGqYEEhAyWDck19oV2gShKDeT8uZgh31YjX4vBJgkca5hrrY2Ok33TzBMUyEd3ZP4PkBRj3xduCfEzvKAXNtTBKKJs7phUOsOGZerMC4lB0DhAU83O7oiMXqL4QbHYotMXJd7tIK9THgN6hkb1ada7qDt5yVLhnyBHPLUxytbxzPWoMycvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=c22qDJc0VxireABessv_NA8d4nZ_yjbQbYXYjyRujfXyBDGcDy4BZNNIGwXWKpAtPzFkrmgyXBUEF0Xo_ylAvOCz7TH6Ej_74jCr041OfBFToEt59x23xgS-OASBFwD7IgDqfXVxJup45c5QJnd5Db_1XAhnApq-hroTGqYEEhAyWDck19oV2gShKDeT8uZgh31YjX4vBJgkca5hrrY2Ok33TzBMUyEd3ZP4PkBRj3xduCfEzvKAXNtTBKKJs7phUOsOGZerMC4lB0DhAU83O7oiMXqL4QbHYotMXJd7tIK9THgN6hkb1ada7qDt5yVLhnyBHPLUxytbxzPWoMycvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=Hp7zNwWc2Q6g0fuiyOtEImpNh874F7I95paXRvjymPbS_4v9WURq2L9g3euob-xHHU5QwiPV4PneuTMFBoNn8c8CsMANboAhq_OHOSUnlEQ5-qDBQcKqhlrYNhMcTNkqzWlwrAdoZA69FPvhGwmuIcoX0KnpTVPtddX_65JIkiWH7QGbC1k9oPAXZveS53phXaKGa9G_pI_9k26c4m2f_e7FdadkjAjsiyCv5CIzE4DxLFEBbivTYsy6NSUzZMPa7KSrMtLUDjoaytFMiutYJrYPbKTA_-WyFKAjKMX0Tk4DNZCd9n9pt1pY0G6iV8-sfu-vOwrrM-O7UBI889XJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=Hp7zNwWc2Q6g0fuiyOtEImpNh874F7I95paXRvjymPbS_4v9WURq2L9g3euob-xHHU5QwiPV4PneuTMFBoNn8c8CsMANboAhq_OHOSUnlEQ5-qDBQcKqhlrYNhMcTNkqzWlwrAdoZA69FPvhGwmuIcoX0KnpTVPtddX_65JIkiWH7QGbC1k9oPAXZveS53phXaKGa9G_pI_9k26c4m2f_e7FdadkjAjsiyCv5CIzE4DxLFEBbivTYsy6NSUzZMPa7KSrMtLUDjoaytFMiutYJrYPbKTA_-WyFKAjKMX0Tk4DNZCd9n9pt1pY0G6iV8-sfu-vOwrrM-O7UBI889XJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGue5JE-HDLK4xzmNow5YHfpmiSv5u1nq8X0fSqwuZbQEjOvY_T4Jg0o5ROaylRo_uhSupPFsT6G7_cCD3ATyvdxGTtd7lbg7q4rnp9nsfQZTsUa_nvt2Biov3BET0vS-qtXxA6vV1-JoMGJ8qWMnlWr2cuNO3eVUS3GCdyh7pVKdNEfssUdkuOlqlN5rrxy225SWFOHCAfRuArid66u6kvKeIwLlcxCFSmpkgXrSNbsLQyDM6thQhg_r8XCEzTTWeEyDkovlGVv-yvQO2qaV842cIne-yagtglwXaBbrzscSEj5GXX081jsydKxFd4g8MaOKti2Cbh25qv8Gh8kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP9qWPVRmo3LSLeM-QBianGXNIwgPwakfO9iutnrgJMmImzru7RB2t9oXYm2PCtNrEjUf1XrjHNaS3ifxD99DOfGvNHyurRLIA8BYFLHluFcqz-6t2ycfbIEYt1HvvvWd6jPatzuzftcEr4mv3m06379wlBCnH8ORQHrfucBlprr8FhD4ZCb_2W5pouTaoL0eP0YdSScWxRddNvb2hlRIPQO36POjVxJtY6kCjgT5Zjt2_azp9cFl68zgGXCZIy9Wxyrqx05440GGEwEjkc9rK8eyYZC2NH__q7JCcMxh-Vit3kuqW4YQ3YP9DFJ64l4wm1ylgjLwpfNQCYHgxn5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQsxloBKwqYSVohuUfep0DpNUyREYJ4vW6Ti80IVjs9zkN388KYj7x9U7leCu-S_9TKUPJ8AkW1SkD6tRIhHT3lFYPab_9oYQ3S8dxNulKODMO9Gbg9T7LdDU-6VIcFdhWATzikwGmVWtDHKDE_UArYUZ8O8c2PrXq_57DenAGujUD2m2XlhqbCGBM_UEFOJHPgxiDTLmwTUtoNykPUrEait5ch8rkQ-4Z0ZkUcDad_1YAaf1IKzQ0iTTx8QXEjopgOmcQUFJSq6nFQXe_9dj_irDzyAzTUfoUX7-3oanRJcRWHklV7NSYL_c8PRGG1TW3EXYBbEktdTpe3Ooex6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZiD47VCxJEH1qMwtvf5aW8d-QAofUeMLJUEzUF6RaW1xgmDaejizgwIPWmX5PuCgJik_A-SvF3xc3y4ZYMBSJ8jC9QRJsoWMF44YHvH4MRXDXM9EOC6zZ3QQcQLc8KXxbXaHEUP-oWE-Bm360bwJF3KYTBUveBqnfyk0c5Zw_FAIcAvYQXQeoTdflaNgsv9Llg4sK_HQhhoJz7G6hjsCqc75WzxvobNCSJk5jSQeXkWz1VeoVoHeEQ535SwqQlEA9B6WNHAvcEDsosw_6epierWvc1R2p_HhgagwOxJfm-M1gVwqKirSqjfILOde6faFbTjK4w3D6vXt4W3eHAssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=Z12u38jsWNBeZxtmORx9ilfvYsPYHgTfmw31DAJD9DizMr9lp_13xw11SeWX3rBz0CNDy-vhPw3QPKB2VOTkwDjw9ZyWMkNaIAKteZPiWUpJNZNUoob3UkUckhXdN3V5mMqvmGjq2p0L9T-MdTtfuRQiTS0rSJQMojCEvX7vj-kMtBNU0DlkhFXRzgRSdK0ZXpgWjY9vpqokP225oiN8XFK0td4noTesTeOAZt3oXFMpeaE35mS8TMRHHBQf9rZXpvNS0_myEluvK3l1IpMYrkfxnaGetAe8hcs870LaDcEktxmWpo3ix2asR1ypdHh34AOyvGVlJSkfwpm0h3OVQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=Z12u38jsWNBeZxtmORx9ilfvYsPYHgTfmw31DAJD9DizMr9lp_13xw11SeWX3rBz0CNDy-vhPw3QPKB2VOTkwDjw9ZyWMkNaIAKteZPiWUpJNZNUoob3UkUckhXdN3V5mMqvmGjq2p0L9T-MdTtfuRQiTS0rSJQMojCEvX7vj-kMtBNU0DlkhFXRzgRSdK0ZXpgWjY9vpqokP225oiN8XFK0td4noTesTeOAZt3oXFMpeaE35mS8TMRHHBQf9rZXpvNS0_myEluvK3l1IpMYrkfxnaGetAe8hcs870LaDcEktxmWpo3ix2asR1ypdHh34AOyvGVlJSkfwpm0h3OVQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X75uIC6O4xH3gvfZUjQXIC-xX3KCNCUCEcgmQhKu62JYGyX2fAsnwrK1RjcokXagsiBrz-cCjN2bzh_niBkE43mo2LmPjimFPby1MPeIUlrNQ-3R8_C3CFU-SDFkShb8wnmvvsATNhvSouniD9M8_bPmSpgic3lPcbi8WJttdHIXUPfk1qR-hNAnB5eeZNVo1P-ODYBiCh6d75RIwEE_jZzFdR3YwAt3seWBwrkpYiANYtnNfn3DlQ3QnrAnm4qqzLsu49LJlvSEmWOxeIFo4EekhYMYQ3A6QhUrroUNQe1I8o19k66GdkiyE7Y2oCxwWlVQfb4Y1GYC1PxT4sJFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYwM7A7UIC92TXXF3unwgH5cxx8c3yn2y9z4rRA6y_pGT14eGeIEDGGoymGjYZeMj65Ht1KYRnmEEx6J4euTLB_2bpcOyBTcZWPHVKpRZ1HvLnNnhwBvffU8_wVxkqgu4VrC95xTYKDnIDv8kC69a86VzixY-04JSL0Ui-Yp5if1kQEBXr3DPwjopRLyld_jtWIHss9g7MB_xcm4Y1Sw1vr-mu8wC3tnaez6v-yddNUvHoAqhW-9xLw_rVKJO612djT-5LjPKElbrEmT2l667cbmX1kihkVJ2awkOs0kh-jMWFg-BpuIvnDxrc_YnxCALN-rQLj_zW0GWB65_-BqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObcxpjbuHpJ6nUtanrfnpH11ySsvLzJ7ui7pT5jcnQHzHfdlwQPRo70PBqpsNM1MKjcqKPleEVTXcyCzRQHt1_hAhc4XeHJUICMxdzhz_ZSt3a3OqSJxwNwZnINp8aXdfcoChCAgsDKKMSIwmzTXcQ3sh4fjl_T9DNcvqbX3kJPYuQi8SaODZr1-w6BtS9AIL-4e5YdM5Y2l_8s8g1nNB6mn0ChNCNraxUnrcvytiYokPEqGFnkLADGVot3vh0vrIHcHAf8vPzqZSmWuyOnGgpVLDXOaOvnBitgI85TcQQdqabaD-OQdp-j5-pWO_z_S97W3exUDkaLsTgRKjpP2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gInKfeTDmYWhReZNqWjeXqnXiGT148nsf1BP-P8LD-cokc6MX2vcyRuQKKbvhkOLmrWAoDGVJPpfiRrift6_7ANEudWx6RL0WiyNXHNVxJS3zeykvYm74Z8PUui17mZJYUiTTMcQGy3uOy3h8c2aRK57ciP9d-Iyr9CbNXjarHvJI2RI1uZIf-4BRTv6Ok0jmHaj6LSoJ83KF36xoEbYeCsBBPfxLdKtXkOd_NSWbMfxjlGWOhUrQCd80Vv_BnzTAJ_O5v7vqHbImsqqjnU7AmT_kjgU3HGueoZiDsEtdEu6qpmkD_qe7os37Xu-KA9GvFF9ZJsIPb9zCtBE-ejX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYZh8FpmbRhahsBR8VvJsNp2VtmEVVb0c9Vpgaf4BMjCSy76IdSAE-RyrqzeXtMPMjGW5FCnigBezzG2IABYc6azKIimSW8NpACN8AC_0CNoMDOdY4lfm1ALurSBQWCAIHOHkT1op3jPgFVaLWFnCMBV3pw9EnWmOMvzeDVxiVRk6c9eXDR33UVTL-zhTblPTTKF2KMbsbQZKVcwY_sER87C5YlYRXX46pu9VkOxm1WVogqISaRU21mtQE7xlGmVw6GHZpfabjc2I36adJL1bR--7ItZMdcKKVARLldwr4I_A9IzCCRL-zLZVNgGDG8MAUF82qI-RKgNupBAxV-f5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=dmkYbxzG7TWeEbUGL65U_N7T9ugt2H4PRFJmpPWCtHaUCkvb08mCXYS1LX-GEP3voHywmJGP7HF6LBfLH9qWPocIM_89FHx9QfDr3DZB8xGoX9scCKvKWI7SN6mKDU738xAdeWPy98-neHhuBcNMi7PsU9kz15W2SAVipwfpTUQuJ_HfvrCiD86V7GfXt7inb0uEWr3NAEWHkDa54j7Woi6FBcbn2pyR_nWEwPtdEtIfDnN1uL_ZQ-7-lQ26oCBmd8u66KoVB3pYkn6HSWpDHGCwRySiVVrtRG1MKwIaUN8MBeRLJUqo1teR0FJckmDwBptmsaM51DmaH0ejLT1ZJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=dmkYbxzG7TWeEbUGL65U_N7T9ugt2H4PRFJmpPWCtHaUCkvb08mCXYS1LX-GEP3voHywmJGP7HF6LBfLH9qWPocIM_89FHx9QfDr3DZB8xGoX9scCKvKWI7SN6mKDU738xAdeWPy98-neHhuBcNMi7PsU9kz15W2SAVipwfpTUQuJ_HfvrCiD86V7GfXt7inb0uEWr3NAEWHkDa54j7Woi6FBcbn2pyR_nWEwPtdEtIfDnN1uL_ZQ-7-lQ26oCBmd8u66KoVB3pYkn6HSWpDHGCwRySiVVrtRG1MKwIaUN8MBeRLJUqo1teR0FJckmDwBptmsaM51DmaH0ejLT1ZJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=MJdbGwciyZixTuTqgUm0ouOyfkAGaNoz0UOFTyUMeZt9K7ywzQVRzzPlKrcDlPTvvhpuW0uXJwAj_8zZ_wOuGGE9pdqeycOQ1phj3kSffM3njKEr7ebKOpCfzMXWdm3sSbPR7uwFdxWqboCMX6guxLQX_6CfvrAFrUjoTiq8Efz8wqwClYV187mPLmb8k2CvouidbtesPZmaNZlv7BUXzG0jDK45XVHFNT2A4iLDZOBSnQ4ihoZDwJVPgLBYKHGszWTHTnPGxL3X-fRELU6tCY3oYpB_weGJaiHTuAoLiE8gc6qzmZ2Yk7pg3fFgA5fW7LJh-1o49ukAqYbDdlYtag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=MJdbGwciyZixTuTqgUm0ouOyfkAGaNoz0UOFTyUMeZt9K7ywzQVRzzPlKrcDlPTvvhpuW0uXJwAj_8zZ_wOuGGE9pdqeycOQ1phj3kSffM3njKEr7ebKOpCfzMXWdm3sSbPR7uwFdxWqboCMX6guxLQX_6CfvrAFrUjoTiq8Efz8wqwClYV187mPLmb8k2CvouidbtesPZmaNZlv7BUXzG0jDK45XVHFNT2A4iLDZOBSnQ4ihoZDwJVPgLBYKHGszWTHTnPGxL3X-fRELU6tCY3oYpB_weGJaiHTuAoLiE8gc6qzmZ2Yk7pg3fFgA5fW7LJh-1o49ukAqYbDdlYtag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=PXgXElOaxn1oE9gn22KzC-HcYpLDa-ALtee2mUQohBj_K5M_PYeqGKaMkelPA3LhGo0AHepS0eNms4XJwDmL5Kvd0bEqhKebfEMjlrlddP0qcUlaRMBjRfZzgkAaX7lk_jidI5IYIQVYP0oUTCEMcJ9SkYrBC_W-Ii_Vr1iKuOxjvkfux4havAjKEq-xNZYYu-hM74xnWMBvf4HAu1gb1Yyj8-PuRneHa5-sT2WkSwp6qPIOQek2OGl0zOu6JRHnkEC7hHkjV8PbmLo6V9Gog4u5dn5fHQkxyuifjZIL1ul6xZtUsDUc8xfksT2sBfequZYPevvQVgm0jQgMV2Glpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=PXgXElOaxn1oE9gn22KzC-HcYpLDa-ALtee2mUQohBj_K5M_PYeqGKaMkelPA3LhGo0AHepS0eNms4XJwDmL5Kvd0bEqhKebfEMjlrlddP0qcUlaRMBjRfZzgkAaX7lk_jidI5IYIQVYP0oUTCEMcJ9SkYrBC_W-Ii_Vr1iKuOxjvkfux4havAjKEq-xNZYYu-hM74xnWMBvf4HAu1gb1Yyj8-PuRneHa5-sT2WkSwp6qPIOQek2OGl0zOu6JRHnkEC7hHkjV8PbmLo6V9Gog4u5dn5fHQkxyuifjZIL1ul6xZtUsDUc8xfksT2sBfequZYPevvQVgm0jQgMV2Glpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=QTIkRWO91skyZZYbOBd_vTKiRCT_jQvJctG6AHYQKVs3KH-5R4QJUT1kd5wkbvVZfT6056YNRXRgN4fLJ7_RGjpRNrFforFMNbCP8yJ-2HM61mMqZGuh_n4bByIo9kgqqJWI5KK7mm1ZS-QThuRpoNZ85hBtzrbSyCr41-mS4ddt0wUmNkobxUxGd4sI3HRO1VWGmGSHw6OS4n4iqNwo0Zk2JVIhBlmqBaeVedSBSgJfQhyNidM5jlHD8T1l55oYZWYnEYyifAMyzA3HXZRTRb938IMaZAggjXvA6ee_scSvUQHpma9LjENo7YEOE8njRm0Abfbpb4LVwIYbctd1koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=QTIkRWO91skyZZYbOBd_vTKiRCT_jQvJctG6AHYQKVs3KH-5R4QJUT1kd5wkbvVZfT6056YNRXRgN4fLJ7_RGjpRNrFforFMNbCP8yJ-2HM61mMqZGuh_n4bByIo9kgqqJWI5KK7mm1ZS-QThuRpoNZ85hBtzrbSyCr41-mS4ddt0wUmNkobxUxGd4sI3HRO1VWGmGSHw6OS4n4iqNwo0Zk2JVIhBlmqBaeVedSBSgJfQhyNidM5jlHD8T1l55oYZWYnEYyifAMyzA3HXZRTRb938IMaZAggjXvA6ee_scSvUQHpma9LjENo7YEOE8njRm0Abfbpb4LVwIYbctd1koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
