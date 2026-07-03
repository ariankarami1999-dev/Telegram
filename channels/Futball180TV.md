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
<img src="https://cdn5.telesco.pe/file/hUEp8XfCtW9Z6zlJulYiyVgtsTiHF-ATVrStROt45Au4lncQBrxpxkxE7MvsHaoE6Zzypv5CecIUaIn9aYTa55D7qhKNd2Vngcow0IOj6Umwcwd4b-edKrosf-w1w425pidIkYSQV3Qdb7y4ZL2MrwEUyVKmuPjcVKW111328VUdbsaei5kQxiNrTjUSLn4JeCOXsUqvsKrI9lzosuOI6nBw6JBlGS3gM_Sz6SXo0_e2SKkn-e25XQe4MakN7q-C4pq7pVTW1eKe_F5Az6keGmkQ58VWRcVod2aEOO1fLVT-udjXUOk75JkbwNwi3UguNq6Que5AjQA_57XW3YpmiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 650K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 18:07:48</div>
<hr>

<div class="tg-post" id="msg-97885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHHmJaFh_i6k-tkhlSi8Eojla8mc4oVGfynfT2Duth5B8E5zh8BJ-JT90k_pLOTbDO5BBPb6h9xA_6FESFswtXqyBw2IofPykDcd_1rUxjuSyRCLhar0b7JExi63aXkz4N2eZuN2UokwORbRhrq_vR4ey461rX163Wg54Uu0jq818_XC7ch3oT5_D6q6QSPnxjkSoFlM231VuD23k3wlRhS6a5MLda3YNbarzgGGpKZSoC9nmkFhrXF8-fWsp1Mt6J7vejnZhewq65BdLRAn_UoHSzdqnU8pd1aBtWBdxyaQF24RfXZ1SaiSXJ2kqj_QNlKp2Zt8_7pNJ2bgpK2aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPy9EEB_3AQunj1TvUapQrFi9oN_sbOyJP0x9wosenA2Bm4fQGo_JVWHhJjdhov7J2qPbQpN6TZIXmffmwt160gSqj8HBLJKMeztAONtgQep09NXBwiFywN5brAW4F4UeE6beqdeaTNAh9hdnHa88TZB5zvKDlVflBrGsb1xPxs9W0T4CuJZ91dPXX2PF4weOK50uyxgQHwNpBoR0O3JzyhPl6j_rrSJ05AmtdtFqBCpFUjgK2jLcMmA1OposYR3KvzxTaxT5c2Zgo8D_BTpnQv8DvjbViInJESoXyHFGt0ExTbD0k2Ysu5pOklYFQor--ZdGD-Big7AekX50cfKxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🏆
#فکت
؛ تیم ملی کیپ ورد 22 موقعیت گلزنی ایجاد کرده است، که بیشتر از تیم ملی آرژانتین (19) در جام جهانی تا به امروز است.
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/97885" target="_blank">📅 18:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT60MVy0P_JuTcY1S7Ze6oym-0fEvLfZT2BgBSyoo0ptlr5A2iLLJ03LpIN8XyC_aPXUI57hk275smysBRRG9RY15wzfX7YcjhBASfiKmThWP5cMgW0tyaWgJEgo9CLnkn2jPjwAV91zRksonFZ_E-W1hynUbFg6xFkeDCYB-701XmGhNKZUWjAKK5th-chI6mkdcLcqrh7_jnbXcduq-SScObpraBlUMpvfkhHEn6rgeZyUrdKmd7ztB2lsEM4095kRCHvH-vMJJDjqNEmQzVEvpoeSYSSK2spkcOIkUgntdSg1gBsN7xaMvpUYFI3btlnqMC9Ep-nZ-IAH6eZXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇦🇷
🏆
اسطوره مسی در بازی‌های مراحل حذفی مسابقات جام جهانی:
‏• 12 مسابقه (11 مسابقه به عنوان بازیکن اصلی)
👕
‏• 5 گل
⚽️
‏• 6 پاس گل
🅰️
‏• 11 مشارکت (گل و پاس گل)
⚽️
🅰️
‏مسی، به همراه امباپه و پله، از جمله بازیکنانی است که بیشترین مشارکت در گلزنی را در تاریخ بازی‌های حذفی جام جهانی داشته‌اند.
🐐
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/97884" target="_blank">📅 17:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d6124f5f.mp4?token=bYJ5dE6HYZQFZTq14j6RTnQ3oOUYTJ3dv8oEiT23Nm923rHyLSEpxcfN_L4oGAYWT8lQj7j_oWiXQYw3mBPdj_R9SnLGj-b18LlNkq15BBNwa0mXPGLIUxuwS2HYIw_y_us8G2dcTGGKCbZRFDRbjNGIg-SBl47GTAmMANJ6vWk4q5Wlk-pBUxQOOjBVzfySnQgj0W7PRrVje2QoHwZGRnu6hRxIMKo-mpOITTBRWJMdVm7ZZnFs41KC4mLft5hK2f83vMXcYODTx19pM_C0oiN8jUPW8cs1xLuC7mLoAgXt1wvtJeu8kydW7LF9vumMA_CaAgN8oKAwpa88PUgUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d6124f5f.mp4?token=bYJ5dE6HYZQFZTq14j6RTnQ3oOUYTJ3dv8oEiT23Nm923rHyLSEpxcfN_L4oGAYWT8lQj7j_oWiXQYw3mBPdj_R9SnLGj-b18LlNkq15BBNwa0mXPGLIUxuwS2HYIw_y_us8G2dcTGGKCbZRFDRbjNGIg-SBl47GTAmMANJ6vWk4q5Wlk-pBUxQOOjBVzfySnQgj0W7PRrVje2QoHwZGRnu6hRxIMKo-mpOITTBRWJMdVm7ZZnFs41KC4mLft5hK2f83vMXcYODTx19pM_C0oiN8jUPW8cs1xLuC7mLoAgXt1wvtJeu8kydW7LF9vumMA_CaAgN8oKAwpa88PUgUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بفرست برا اون رفیق فوتبالیت
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/97883" target="_blank">📅 17:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ1DOwVQ32FGpbtjsRY87XUBwNgX9bNCY8OqG6IwAF3vIfTJLf7HUR2ORyPFLuNah4L3WSUpG2dAmvodFnCzi0p4JztU5xw5-gizDScoOzpZabClX9m_J5GjQG0oXT16kpjLZpoMFLpsnv56glxJ97GrYNBPvvgEwpkkJbIkT2i5v7RJX3uaMlxcH-D7uTBs2KwgMoxUE2UlnC1y7sswECBqnJwF3efMKSJqRH-I2ZO0ls31m7_S5YwDyGO18UAG245wZjvEJ3ayjieR8xPVP9g4ggHkf76GNYrw8mQYw9VxY6KcEtT7Bt7CrSpqRF7vpPW0XOpkuuiWlGV3CXwWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/97882" target="_blank">📅 17:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtiNSnNPId3PXf7G9CVgcuZoKotImmKMB05LGV03hvDSq2ivaEFJNc6tYUSsPqoLUGC3D5OKvjKddfo86MZjG4RWmyEUx7P97zSrMm-HNihn4j8Z8iUOvNS5jFlvnJgN6LoR8Uvmv-jDjOWwB1iC-F5FvP7tgVRY3WfETfDukeU2SfhOl7AW3uAWzss-9n_nlDMhFoIvv2eTrQJxbZ6fZpv_S2W0wNjMN3OOPGyrh8ccPnJLLJluT-xnh4hQXsqTptdP_qgEIjxcpKnpPtOM9xE_iMQ_9I7RgWOgf2uYOqya7_G-UXA0s8C2vba5NsOitrruQZiZCLAYdUYpvj-giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاقی که برای داوران در جام‌جهانی دوره‌های بعد قراره برخ بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/97881" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497eedaf5a.mp4?token=ZWgZo_vKF9HrRM55B_dsYx7I_E8QQ5yCoNiTve9bdNVGg7gjEk68lbylzF7hU0aZlyZ2ghKDwBG5IfDLhIYMQP-SxvywdnzawYAD-rW3IQOSVD1ujfSBrtgqkYb_pv6O3VR1UQTvtXGd45W58lQ5l6vL9AShV81wkb0N7UjDxGkTqe5jR81SvGGF_20e26etFgVPu9sTLV0DdI799o05VO6syaT-Q4sxcNJWiQhtbpJvHcZt2M4lHi3D8gKVffnN-a06pRtTPnskYJHaH9EpoRl9wZARWG-3fNgUc9KMBRYVwW-D0VXlFWpbELkZf27MQQsn1CeBhZdBuxWRD_kVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497eedaf5a.mp4?token=ZWgZo_vKF9HrRM55B_dsYx7I_E8QQ5yCoNiTve9bdNVGg7gjEk68lbylzF7hU0aZlyZ2ghKDwBG5IfDLhIYMQP-SxvywdnzawYAD-rW3IQOSVD1ujfSBrtgqkYb_pv6O3VR1UQTvtXGd45W58lQ5l6vL9AShV81wkb0N7UjDxGkTqe5jR81SvGGF_20e26etFgVPu9sTLV0DdI799o05VO6syaT-Q4sxcNJWiQhtbpJvHcZt2M4lHi3D8gKVffnN-a06pRtTPnskYJHaH9EpoRl9wZARWG-3fNgUc9KMBRYVwW-D0VXlFWpbELkZf27MQQsn1CeBhZdBuxWRD_kVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه سیاوش خیرابی راجب حضور در برزیل برای تماشای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/97880" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlMn_M7XvP1dv6i3xQ_TxbisXuxYEuZBGB9b9GEE_nfaunsQQ_2g8onehSPtSuOkGPoPZskppu-XIaeP9HQL-fBgrvy3lxZXpdgTbR_HG849ItuwCbkjC9MQH91fOjz4dhi9OBy5bPN4wGIVfp5Cgr7wE_bmMCBH3HmdcnTg_Aasohk1JeAFEYixeRd0HEf389_g7ceWK3EgixU_yP3bVghdsu-HjNpDtIisQmX0WdUGX7DOnIQhkn9xE3ra7RhKWtLi4AGuVMjjjeRNdZPQdHNr12ZkRLn4SyUT1V-LqI9uKT4zq10zldMikI-lwbFwK3WPlgC19C4sq4mqbMYdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🏆
🇹🇳
#فوری
؛ فیفا پس انجام آزمایش از بازیکنان تیم تونس در‌ جام‌جهانی متوجه شده که ماده ممنوعه "کلنبوتیرول" در آزمایشات دیده شده اما این ماده بر اثر کیفیت پایین غذایی در مکزیک بوده نه مصرف مواد خاص! در نتیجه هیچ محرومیتی شامل فدراسیون فوتبال تونس و بازیکنان این کشور نخواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97879" target="_blank">📅 16:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx5Fc14wqqZ_KgFe25-mkJQth3Vhk2ee6f6SDrDQ0kZe9CQdXkA1GDHgwrv0h6Mz1owbGlLa2UCCZfiCOfFZUiSwJfZ3GdaXYUNmWASNOmRVY1kIuQ94w1b4v3IUF43gk-Byv2myTbfVGhzrAJ58e_wdrxAQ5FE88ARwwIvIVaikzOHcLkBuUWDeDZfVKSQx7fLcBaNMF-uMOILez6G-Q1K1Ja8SVwT0oX2Fi5jSEt3cq_gaHvm8ncWusqtC0Q4XSZVRs-ZqcuGP7J7_z60a7YKrBbX9ygGVLR8E5QTM3abMZbfMYgeKf58tcRXNQf0diS2VF70-yfHS618sXbEFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سپهر حیدری اعلام کرد از همسر پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97878" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYdwXXkR8ZbeJyzdx8pmZ0oKDVapEa3cxavl2W-uNncQyTvU6zLQs1TmdWJjNVTaqOVkdTHMPvSBLbpjLYF1AhcwdVPKZnkqpC48vEZTMsjQuQLdxTYGwVhWsUDyYEy-B41mu2VXDN2bSXSv8np99CjmR_UOefStFnblWLS8vEn0OgFDOssG9WAQ8ej5WmGdVO1BKa6ocFzi4AYsYYln3GiXlH6dDBP8MHTf9EnNoIsFIHkfBcn_8cVFENMGsaeHuXQdMYVlC-M3hsLGlBJfXLEG_VlqkySSTVfObvrOFDJRBPP8Oubnmw1fl5OLnxw80yvBk6q8qtLHgvOd_xaUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارلمان انگلیس قصد داره به پاس درخشش و تقدیر از هری‌کین، لقب و نشان "سِر" رو به ستاره فوتبال کشورشون اعطا کنه
💥
سِر هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97877" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50819de74.mp4?token=IEK5oS1LJU_vk1Rm4fBe4D8BvlFC8A1A632zfx5Fx3Ih_MK4zEThQLTbFjuosSxqC5NmUebW5rUcDoXdeetDgVNk9AvshQweXknqee5EeiAlQeLZTieZ6c-eZ0SaXuehVi_5MkF8BoTcobLpppcipm3Zh4O9TI0ZIIsEvlPef5HhLUWR0Y5M5v9oh_AktbY26x_mceqBeulkeBhM_rCjTTxYj6uoMrEbPsUsME0949Gy1EjiaDUNLVZspoqpm5e0htLDzmtmbRarCiO8sBxIapAKZiP7X9xSXBn8kBVx50MbQD0ZK4e-pUsxR0ai6Vk1tWQS_lBmFNQiapUO8_pNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50819de74.mp4?token=IEK5oS1LJU_vk1Rm4fBe4D8BvlFC8A1A632zfx5Fx3Ih_MK4zEThQLTbFjuosSxqC5NmUebW5rUcDoXdeetDgVNk9AvshQweXknqee5EeiAlQeLZTieZ6c-eZ0SaXuehVi_5MkF8BoTcobLpppcipm3Zh4O9TI0ZIIsEvlPef5HhLUWR0Y5M5v9oh_AktbY26x_mceqBeulkeBhM_rCjTTxYj6uoMrEbPsUsME0949Gy1EjiaDUNLVZspoqpm5e0htLDzmtmbRarCiO8sBxIapAKZiP7X9xSXBn8kBVx50MbQD0ZK4e-pUsxR0ai6Vk1tWQS_lBmFNQiapUO8_pNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
خداداد عزیزی Core:⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97876" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgJaeMWUYce7-Ua6o1gUEGHSJ1fUxFlNBoKuJEGb2Q3I7jGhLTkWVANrmjG9uLO-R65ZdGImcj-MFgnDUGLjv6MCigfSgcufzHl7WRsUnt5itzHkVRRNtclIyKXyPaaxLmCMqFBDRlnAmjI5m-fvTF857RCebX5Y3lUZWGESl2_l3F2CkQYA119rOERfYxKlRJE3De2j65yHoN6obmv3rC_v8V_fwYuz4At-pQtY_fhq9MMM0k7i1ewQQxMKhuFbob0FxEe8kCCEhsk-vm6FoxcVthMv2lHFW1045ExjmObvoAfWKFrHuDa2cw_a6bGPWsys0lNmhxWq83IpDqLtMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
⚪️
فوری از ماریو کورتیگانا:
انزو فرناندز و رودری از لیست اهداف رئال مادرید کنار گذاشته شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97875" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97874" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97873" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b016be396.mp4?token=snil3OWwK8u3ZXneLCnGTG6z-qGBhaQ5wDnoaHWEUt1sJGwhZvuL5Ay-CXYsxjSnDeuqVFRP-_P9fm3Nhzi7Ic6GW48ylOdvus3BYqjN7k_LJz6iTkdgLti2SgZKJJt_UzXrndod9NStKk-htz3V2Ghqhb8jCFjs36n7wcs6L0fT1XoOjaiiXBjMV_YBnvnBNroZAvW1TLj0cI7SCy9AR-DjdTFOEfc8tj-gT-hIVlDKyhgsM3Mfru8eM2Bw3F92kLzXJ62Nf_bARg4gVhli3rUavMonLTIl4ACi7cuHEIrQFl10Qu_18mnuK43C8YiOfeRNUHa5g31LewtM8NqCtZemHL1FovJj7654Qcs3o-PkiL60C4ubWZyrPOi_pOeHbHOW-ngJfPXEcLsy91hWyWKTDUvfFTYnkgwbFm8BtdUD6TMhw-Xk6SZTL0wTvq9aK85CxRoUspW44lPQ7r7tPefLxh4XpAETaecPV2s9jM-uu8VcWQcOgCFUVOPDRRBfiVD8l42I2t0ua7nkAOpl_PB2FRc4ZVRLzFocIfFGAI_WVMq0FfpX64Ylc0YR4jGlgzWGbvFAX8pPlkzP6Ieh8joHMZ8nAK3kr6sv2nVwqliIIO1Iid2egnJqmiwKxySWqvNErSY3r1oHWydbrRHMpErO0JmgpiPpXAXjbiCxOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b016be396.mp4?token=snil3OWwK8u3ZXneLCnGTG6z-qGBhaQ5wDnoaHWEUt1sJGwhZvuL5Ay-CXYsxjSnDeuqVFRP-_P9fm3Nhzi7Ic6GW48ylOdvus3BYqjN7k_LJz6iTkdgLti2SgZKJJt_UzXrndod9NStKk-htz3V2Ghqhb8jCFjs36n7wcs6L0fT1XoOjaiiXBjMV_YBnvnBNroZAvW1TLj0cI7SCy9AR-DjdTFOEfc8tj-gT-hIVlDKyhgsM3Mfru8eM2Bw3F92kLzXJ62Nf_bARg4gVhli3rUavMonLTIl4ACi7cuHEIrQFl10Qu_18mnuK43C8YiOfeRNUHa5g31LewtM8NqCtZemHL1FovJj7654Qcs3o-PkiL60C4ubWZyrPOi_pOeHbHOW-ngJfPXEcLsy91hWyWKTDUvfFTYnkgwbFm8BtdUD6TMhw-Xk6SZTL0wTvq9aK85CxRoUspW44lPQ7r7tPefLxh4XpAETaecPV2s9jM-uu8VcWQcOgCFUVOPDRRBfiVD8l42I2t0ua7nkAOpl_PB2FRc4ZVRLzFocIfFGAI_WVMq0FfpX64Ylc0YR4jGlgzWGbvFAX8pPlkzP6Ieh8joHMZ8nAK3kr6sv2nVwqliIIO1Iid2egnJqmiwKxySWqvNErSY3r1oHWydbrRHMpErO0JmgpiPpXAXjbiCxOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
پشمامممم ریخت چجوری این جیمی‌جامپ بازی پرتغال بین اینهمه مامور از رو سکو پرید وسط زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97872" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374849cbee.mp4?token=TEPbvFNNGz2zV8-n3MtkZhpKyNelvAsc0DzI27RUFNWGAWW54VvoCMbQF3z2EKQnvmN97aUNVv3SFx_N4U3GSg7FDjbrkNC79_rgmtXSJHA40j9pzdSlyykb8KGPwYxWEWHhlftayxC6a1CtL__mBSB4YbjQXkO4NBwfhRsKM9eFFrtWEdkCegX249QWW27TfRBRcT3p7twp_JAGzd8uislYfgyVkSMrUIWWtuUqcwG1NCrv02n9hqRhXCXpalUuuJk1g842pOBLUfSyjUMC5I5tqD08Dfk28GcAo4QSB5zC-9nKcqWkuN_ZNYDBSAU3a0fpNB9vAoxl5JLCkCM65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374849cbee.mp4?token=TEPbvFNNGz2zV8-n3MtkZhpKyNelvAsc0DzI27RUFNWGAWW54VvoCMbQF3z2EKQnvmN97aUNVv3SFx_N4U3GSg7FDjbrkNC79_rgmtXSJHA40j9pzdSlyykb8KGPwYxWEWHhlftayxC6a1CtL__mBSB4YbjQXkO4NBwfhRsKM9eFFrtWEdkCegX249QWW27TfRBRcT3p7twp_JAGzd8uislYfgyVkSMrUIWWtuUqcwG1NCrv02n9hqRhXCXpalUuuJk1g842pOBLUfSyjUMC5I5tqD08Dfk28GcAo4QSB5zC-9nKcqWkuN_ZNYDBSAU3a0fpNB9vAoxl5JLCkCM65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
چرا فوتبال شبیه به زندگیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97871" target="_blank">📅 16:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b751ec19e0.mp4?token=YuTiObVSLY5fbi8gOjz_Az8ef05NejEh8noQq2iqfIqJAnm9gRv45Brn3fyE4Fo7yyif7jskn4sUqa_4aWva88asVccu3z1pOx6fpbcIwdHG1N0NY-hjv_TdsGprLnm7hr51MijDa3ltvHVgEsazWd9F8l3jvxGnPygf3ITRTGyYTRYVLS5hp3ussh3jOeyFjaBkyGfPdiPw76CS5hT0rj9yAZ6vxs4j9j4nx6t8F0--FHDVcuFqTIuNSG39ROzNbnb6y9iSUQKwoXphYVKmU7uLjjVojVerwfCWDRiuTu836vAK971gEdOCVgfNERzK32ZnaoGTdOHDBXoCZ2zO8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b751ec19e0.mp4?token=YuTiObVSLY5fbi8gOjz_Az8ef05NejEh8noQq2iqfIqJAnm9gRv45Brn3fyE4Fo7yyif7jskn4sUqa_4aWva88asVccu3z1pOx6fpbcIwdHG1N0NY-hjv_TdsGprLnm7hr51MijDa3ltvHVgEsazWd9F8l3jvxGnPygf3ITRTGyYTRYVLS5hp3ussh3jOeyFjaBkyGfPdiPw76CS5hT0rj9yAZ6vxs4j9j4nx6t8F0--FHDVcuFqTIuNSG39ROzNbnb6y9iSUQKwoXphYVKmU7uLjjVojVerwfCWDRiuTu836vAK971gEdOCVgfNERzK32ZnaoGTdOHDBXoCZ2zO8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
وقتی رامین رضاییان، تصمیم گرفت بدون کم‌وکاست به تک‌تک آرزوهای پدر برای خودش جامه عمل بپوشاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97870" target="_blank">📅 15:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e7bb3043.mp4?token=EoKOL2jxEjMOejmSJK91wqEsysZ0zIy7DQDwS_9m5e6uPavtTrGFWgMoBMXMgrBqG3DAUK_PRK6_mf7onXcfVoGHc47XlDeZKecKb4Hek7DfnDxZpTkcN3kkFaFaLDpzwfC4lk7H15kCOMnGPrJ4DfGuVc0COhkNGufriN5QfIqovFzNsSIndtcrCAX7bLGLY5wb9A83gUFbapY0vr2vQC8cALOq7jL3ILZ7ME2XTemd1o_kdk8F80TG7TaKHQ9kVMpI4Bl39r6MtBvlJsCjBFMjjKUimR8PbFkvkq4Gwdgl9qi6Ib4aZ91DE4hgp4Q1qvVy2noOVD5poNXq4RDOYngWpLrMEVUAi1odB06pqSUkXQjkG_8NGUG8lCtuDpXv6em73-LFelMxH-IN70hBOSDJpztLrg8-2hBTMW0JaoBpLdjWZl7UnRWr0662TnRIZZ4WFVh4NCafiY2IkAl5aA5u0Mp_7AdHod6rFzn2NIUb1tlnnZNopaMj5FY16DCxsX3F39UVMpkzYiWPri10ayyfLSGfGKe74H66vwGHeQJtTMfsbNCIZANjErVkgwjpMk8CaKaGCeVYxf2iPLTKF37sgpy9slHRRHKip6h3JcoRoZA8cQGIjGaQ8zik33P2cdurICm5u_D1oog-F2e7QDKD3w8DIKsCYP1GzO-HfQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e7bb3043.mp4?token=EoKOL2jxEjMOejmSJK91wqEsysZ0zIy7DQDwS_9m5e6uPavtTrGFWgMoBMXMgrBqG3DAUK_PRK6_mf7onXcfVoGHc47XlDeZKecKb4Hek7DfnDxZpTkcN3kkFaFaLDpzwfC4lk7H15kCOMnGPrJ4DfGuVc0COhkNGufriN5QfIqovFzNsSIndtcrCAX7bLGLY5wb9A83gUFbapY0vr2vQC8cALOq7jL3ILZ7ME2XTemd1o_kdk8F80TG7TaKHQ9kVMpI4Bl39r6MtBvlJsCjBFMjjKUimR8PbFkvkq4Gwdgl9qi6Ib4aZ91DE4hgp4Q1qvVy2noOVD5poNXq4RDOYngWpLrMEVUAi1odB06pqSUkXQjkG_8NGUG8lCtuDpXv6em73-LFelMxH-IN70hBOSDJpztLrg8-2hBTMW0JaoBpLdjWZl7UnRWr0662TnRIZZ4WFVh4NCafiY2IkAl5aA5u0Mp_7AdHod6rFzn2NIUb1tlnnZNopaMj5FY16DCxsX3F39UVMpkzYiWPri10ayyfLSGfGKe74H66vwGHeQJtTMfsbNCIZANjErVkgwjpMk8CaKaGCeVYxf2iPLTKF37sgpy9slHRRHKip6h3JcoRoZA8cQGIjGaQ8zik33P2cdurICm5u_D1oog-F2e7QDKD3w8DIKsCYP1GzO-HfQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کنایه‌های تند عادل فردوسی‌پور به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97869" target="_blank">📅 15:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqAO9fBa3Y9qJ0A93bOoI-Gcs0ghh8ERpklyjYD51lzrJAn7jLJFfx9KiBwkRrjl9a2A3bo2qrQt9T0T2YhMPDt9DIQOLRQkH7GYvqB82V7g8WgzjwVKhv814pJ7-VXmuhk2izXd-sfL5zA2RndH8wvrPP4SrfuR_6NhTFEDF_dZnWeb9V4t_--V7BwupjgUMHIqbdQJqzfsShh-uoec8_2_IkonvfaDlCFFg_sDopCHGkhQmJ4xGzv4c2oUGfAilz5HlrulAmgwK_I8amx-8gSXudD6MEQiQuh8K7FpM6Dykl4g5PdlLABG-k1wre3j3XZAfG1yJLsoJ7EXMyxbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3eb4669c8.mp4?token=r8yS2_tPopaxmjYiPmuPIVP6SJrCPBpKbNMiT9UuMjdMddTTill8JZhsv94ZL-6kNdZQ3SyrLTBWyHwxV3fr1wP0RqEKsRv-cgcxDp0bbOIN_PckOJUHl-TC5kkB-g0cmZ8E51Bk8bLz2_B9xypvGJ0FgkceZgZel36i2ZC4m1ZSBIZH5ltZdthkj4C73ZQG48q5Fa9Gnkwjl_x_VkPLFECCtKoMovqLvkUXVpotw4AH45z-Tmp1zmjpUhie02vDc3WvqR6bsG_he28u5gzqDPPjzR4-w6WcOobgrXAQiDJiUJ8pxdqGeTcXAJc_ONXQbGQL6g2Q4czLU9pTVQrcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3eb4669c8.mp4?token=r8yS2_tPopaxmjYiPmuPIVP6SJrCPBpKbNMiT9UuMjdMddTTill8JZhsv94ZL-6kNdZQ3SyrLTBWyHwxV3fr1wP0RqEKsRv-cgcxDp0bbOIN_PckOJUHl-TC5kkB-g0cmZ8E51Bk8bLz2_B9xypvGJ0FgkceZgZel36i2ZC4m1ZSBIZH5ltZdthkj4C73ZQG48q5Fa9Gnkwjl_x_VkPLFECCtKoMovqLvkUXVpotw4AH45z-Tmp1zmjpUhie02vDc3WvqR6bsG_he28u5gzqDPPjzR4-w6WcOobgrXAQiDJiUJ8pxdqGeTcXAJc_ONXQbGQL6g2Q4czLU9pTVQrcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هالند تو اینستاگرام این کلیپو لایک کرده و برای وینیسیوس کامنت گذاشته:
🇳🇴
هالند: وینی باید این صحنه رو بازسازی کنیم.
🇧🇷
وینیسیوس: خخخخخخخخخ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97867" target="_blank">📅 15:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx9yQFwiDusWGPMbVbfk9WmXSd7JkT9HXiWIs3aINDL1tatp5q4KhMfXkmCy0vpQZQl3LF4XFgDNStr7m54JoeAc2Fec9ykZc0JowU4TdvqbVOltXoxlegyehnbw6kOdaMcALys6RStrJqHaLLPg1z73RwyrG92gsJZaZxbzseg0Q-IJOoHGPco6swl-wujGrU8uTZgSo76Q5-enOVcBn7SdYtxXYT5Qml7ancDKafZRGZUBjInQ3ZQSKEAb1z15VulR7BVIwAmer3ortVmyXu16jv_WZEJDi6iJFA0-Qp7w2L-YOZIM8-MyOQZ1iP5m56JM--0jTeTVBNjEqijDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کل افتخارات روبرتو مارتینز:
صعود به لیگ برتر انگلیس با سوانزی سیتی
قهرمانی جام حذفی انگلیس با ویگان اتلتیک
سرمربی اورتون با صفر جام
و کسب مقام سومی جام جهانی با بلژیکی که ولش میکردی اونسال خودش قهرمان میشد.
تاکتیک که نداره، ذهنیت برنده که نداره، تفکری ام نداره و الکی فقط تعویض میکنه.
نه سبک خاصی داره نه فوتبال قشنگی ارائه میده.
کرواسی با چندتا پیرمرد برات مشکل ساز شد
جلوی اسپانیا میخوای چیکار کنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97866" target="_blank">📅 15:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97865">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خب دیگه بالاخره از بالا دستور رسید امیر قلعه‌نویی و مهدی تاج برکنار بشن
🤡
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97865" target="_blank">📅 15:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97864">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d611a1c585.mp4?token=BKtOi9_GUfyjtTCdz6ftecwumcWEJ1LNqAFHwTwesaUoAF7eWVcvZNIlcmJXDQbNNOqOPJLe5yOd0lfQJN5Ti91PPrfvhU1ohz_KRX8TOlAOWEmaTwRlLy3ymARF4593Rbdm5kzIf6pgxyNXhY0FRvhBq3yeOnVhU8SK6ImacPO201cjN_EUxeY8aNyepJGel0nJdQzAnNhFTOLbhz6DptBK0RozTOZC_mZN448p_1yGlDbxWN6_z6eY2ZTRN_JAnqnoMp0IfoVkVASf535P97xVqef6oAjRmARRxXbjgn6KYJbcuppiz1Pqx2a5Rm_L5ZQF2O_DprIFxFuWS9mIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d611a1c585.mp4?token=BKtOi9_GUfyjtTCdz6ftecwumcWEJ1LNqAFHwTwesaUoAF7eWVcvZNIlcmJXDQbNNOqOPJLe5yOd0lfQJN5Ti91PPrfvhU1ohz_KRX8TOlAOWEmaTwRlLy3ymARF4593Rbdm5kzIf6pgxyNXhY0FRvhBq3yeOnVhU8SK6ImacPO201cjN_EUxeY8aNyepJGel0nJdQzAnNhFTOLbhz6DptBK0RozTOZC_mZN448p_1yGlDbxWN6_z6eY2ZTRN_JAnqnoMp0IfoVkVASf535P97xVqef6oAjRmARRxXbjgn6KYJbcuppiz1Pqx2a5Rm_L5ZQF2O_DprIFxFuWS9mIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇭🇹
🇧🇷
Ronaldinho vs Haiti.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97864" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97863">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42e2e0f70.mp4?token=Sc9idXlcdDhch7nx5pL7SSsCyX49H_BP0-jgtLf29V0CJsxeNxtjDIqCODtnLrTkWzQ_xxf8A_KGwPJLczd7SIfKDKBMWKTazfwOov9-t17HWazh0Y42fnp77Ib_aE1gtGZzrhio0A6yjTIV2ws8mlvYBKnbdoJQJHnZd1N6qET2rwmjbl-_Bz5vSKvuoXNTwjA795XLwupMVG-C0Z2f-EQiFwhWvLzksyosMRF86Rw9kMwMi22kaOvtDRcqQN6SnmR60IYJkVSLJZdhA_tS0GrH05eVRr2ZzWGC5cCpFC8lA3JXnEjRPBhSe4jT3nz586LCslg5_ZdAWBYSVX-YfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42e2e0f70.mp4?token=Sc9idXlcdDhch7nx5pL7SSsCyX49H_BP0-jgtLf29V0CJsxeNxtjDIqCODtnLrTkWzQ_xxf8A_KGwPJLczd7SIfKDKBMWKTazfwOov9-t17HWazh0Y42fnp77Ib_aE1gtGZzrhio0A6yjTIV2ws8mlvYBKnbdoJQJHnZd1N6qET2rwmjbl-_Bz5vSKvuoXNTwjA795XLwupMVG-C0Z2f-EQiFwhWvLzksyosMRF86Rw9kMwMi22kaOvtDRcqQN6SnmR60IYJkVSLJZdhA_tS0GrH05eVRr2ZzWGC5cCpFC8lA3JXnEjRPBhSe4jT3nz586LCslg5_ZdAWBYSVX-YfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدل ارلینگ‌هالند رو داشته باشید. خیلی باحاله ناموسا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97863" target="_blank">📅 14:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97862">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f9d77bef.mp4?token=DKCUgI2vJa8utv08zdTzbmchKgnHGiQwJug9V4ZYlGfC5oEw51pHZiEZW_1QUeARs40KhUP0oBMevSI7tcwMutErGyiWO4h3P1ObxSCCjVfZ1Cy9nHUd1_Qz5lGP-_0DW7pQ_4VV99m0p6N4l9uNog3IV-IbAXngNR_oZcB58-l7AqnyuX4sv4G9mfdTDXDUl_Xg8qQxEAsuL0z0Yy70PhJnH4vsQ08viL9bT-aZx6BtE4SvN2ef7esYfzay1IlEqdXHB0bIE-psUwlFC2T7rxEq3zPJ9zIuo0de_bZj2O7lgFEs03iNs_IAJj5PvzLMVkeJ8bqXvGL0kAJqJWQhKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f9d77bef.mp4?token=DKCUgI2vJa8utv08zdTzbmchKgnHGiQwJug9V4ZYlGfC5oEw51pHZiEZW_1QUeARs40KhUP0oBMevSI7tcwMutErGyiWO4h3P1ObxSCCjVfZ1Cy9nHUd1_Qz5lGP-_0DW7pQ_4VV99m0p6N4l9uNog3IV-IbAXngNR_oZcB58-l7AqnyuX4sv4G9mfdTDXDUl_Xg8qQxEAsuL0z0Yy70PhJnH4vsQ08viL9bT-aZx6BtE4SvN2ef7esYfzay1IlEqdXHB0bIE-psUwlFC2T7rxEq3zPJ9zIuo0de_bZj2O7lgFEs03iNs_IAJj5PvzLMVkeJ8bqXvGL0kAJqJWQhKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به همین‌راحتی مدح و ستایش فیک برای امیر قلعه‌نویی و تیم‌منتخب ایران برملا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97862" target="_blank">📅 14:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97861">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad396b4fa.mp4?token=jQz3UJi9zu-1_X7ofwIpqes3xWRTEB2AydQFab6HqetFXgl5G3O-PgDxh2_YMQI7Iq7jas2JjPzbovmnsAjrgI-m_2CJ5KXZD7nE6L_8fA29eohtv-wtFim6LyJ38TrgjPoAu09sZWTniX6REwf3chfXw-xMCLdvjgm1KfzZ1Xxx_xf9ZK1KALSRb78_Bw-y8EJKtMd1z1qnlC_cRsojTnDQZVjOIP35bpKJgKqK5-4c2Xxns5l_phYgph7lMn--l6ibqWTOoXNdn0rlXGIj0H3jqVoIKLK8f31nJKsSX2tfv2VaGR5MDihZAyNU0agwM0AclTq8RlQRgEbVISJJSDnlZ6EAL0vjbXlSIysxtkU0ksVDFN8vARA9G_doSfDaOvGDzGYQ_s7GUEIf6pigVpZ4y1k8qrbNdLg7xSaMFayAbWoRlWqLDdVuTWWewIGYgTTw6Y-R8VV-HOyFc22Z18h6NjdR7YEvObleCopFNpqiq39RzT2Zp7QVEjEF9DZNRoxGOl_1dXG09oxF9DjDaQDzhpC80AP6Az8mgiYBSjbxvdDxH2-Su8ZbVv1uqPd_0DvT97mPSk9QMAgJUSBUCYPZtbvcodifxxvzA-TGF15q4ixLJ5DlaMo_AefXlevIOR4mf1i_XcsuJD6AVF9ivNy2-P87VK-8YEPGA4biH7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad396b4fa.mp4?token=jQz3UJi9zu-1_X7ofwIpqes3xWRTEB2AydQFab6HqetFXgl5G3O-PgDxh2_YMQI7Iq7jas2JjPzbovmnsAjrgI-m_2CJ5KXZD7nE6L_8fA29eohtv-wtFim6LyJ38TrgjPoAu09sZWTniX6REwf3chfXw-xMCLdvjgm1KfzZ1Xxx_xf9ZK1KALSRb78_Bw-y8EJKtMd1z1qnlC_cRsojTnDQZVjOIP35bpKJgKqK5-4c2Xxns5l_phYgph7lMn--l6ibqWTOoXNdn0rlXGIj0H3jqVoIKLK8f31nJKsSX2tfv2VaGR5MDihZAyNU0agwM0AclTq8RlQRgEbVISJJSDnlZ6EAL0vjbXlSIysxtkU0ksVDFN8vARA9G_doSfDaOvGDzGYQ_s7GUEIf6pigVpZ4y1k8qrbNdLg7xSaMFayAbWoRlWqLDdVuTWWewIGYgTTw6Y-R8VV-HOyFc22Z18h6NjdR7YEvObleCopFNpqiq39RzT2Zp7QVEjEF9DZNRoxGOl_1dXG09oxF9DjDaQDzhpC80AP6Az8mgiYBSjbxvdDxH2-Su8ZbVv1uqPd_0DvT97mPSk9QMAgJUSBUCYPZtbvcodifxxvzA-TGF15q4ixLJ5DlaMo_AefXlevIOR4mf1i_XcsuJD6AVF9ivNy2-P87VK-8YEPGA4biH7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😛
برخی از کنایه‌های افراد مختلف به میثاقی یا همان مجری معروف‌صندلی دزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97861" target="_blank">📅 13:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twcnBv7cKqrscpmMdJZqUje8HNEMyBiKQzw3zLttDQl9LBcYIG_8EOvV3mmLXPz4I-4L0llMy-0CMM8a2L1A4LtWULFrVKeucsOEXVGyOiuwqfqA9AqmKEfx-MCpicoWZ-DCU7iT2QsQKatRShfUoHLXiI2IzKwigWntBZcuSQ5RBrVQaR-C60QQUF_14eLGMiW4ZVXDcWPmSt7IbiG5PWzSMto0m1-ts9oJv2n60UdDpb5BrnCVEY8-9fDh9qERpZtHvsSAZqaOxVtgvcDnoX9Wh4jDZ-iv7x293l0f7XPt_mmAU_28K-TgDI3KPCqi4lT5kFECDcIgrpRXROqDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فدراسیون فوتبال آلمان رسما اعلام کرد یورگن کلوپ تمایل خود را برای هدایت تیم ملی آلمان ابراز کرده است و مذاکرات به زودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97860" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQsjmisoM3oixiqJsADn7VKBswdlka7ctYuyIozTDB1pKdYoINxg4b7v2iWLTrxsXAYPd7jHbp5ynZKAP0o2_VF6MwxyzVrFQxeOHgPwf5rEClCBffUbmq7Nn5C3H5iFC3zLckOb0F0BjnWLBshULt6IvxpyDkC7rv7pd87zA2wykzk8Cvvv0pcq6rqqzKFmxJzJPUE_n7d996y2aFVy2cGUFcPi-_HrsTgsstpXaCn2eCCnG0tC7LxPcTlbyFlk0GEQoFjY8KsexhJOIfuP4HHPUUQ1TrZluVnwgOGstjmNv8nQer6h8a9XaaYIKVXFvgQXZW2uXBl7Tk888lJCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
ترشتگن قرضی به آژاکس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97859" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97858">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df46960b2.mp4?token=ObQoQYLWUlrEy2uvSknc9D9iyqQjOLQvenPljlwYrVQfslyODCm8ctB2ZhWW0B0O-BXSd-ML92V17PGlL_-nxbB5jUm3l48he5uH31yWATeRyrEO8rvVO2cIinKNZChXQ35BVe-QLAlv_zf2wpQ6mNbZmLOuXWl7CSLUp3E_GuM8TJJCUCg5ZtW60Ueu8pOnmheaACAriaWgnDxjzED1e17KSXHbCN_8NkKTkZ0kKl-rb5wzlBQtwRqLGie7j_0lZv4j8JbYGTKKxsSto25GL7jK4kIBbobJukY2067sxo4-RsY2H3J0iYy3sDkvIYHUW8RuSpTrQ0YBIB575B7qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df46960b2.mp4?token=ObQoQYLWUlrEy2uvSknc9D9iyqQjOLQvenPljlwYrVQfslyODCm8ctB2ZhWW0B0O-BXSd-ML92V17PGlL_-nxbB5jUm3l48he5uH31yWATeRyrEO8rvVO2cIinKNZChXQ35BVe-QLAlv_zf2wpQ6mNbZmLOuXWl7CSLUp3E_GuM8TJJCUCg5ZtW60Ueu8pOnmheaACAriaWgnDxjzED1e17KSXHbCN_8NkKTkZ0kKl-rb5wzlBQtwRqLGie7j_0lZv4j8JbYGTKKxsSto25GL7jK4kIBbobJukY2067sxo4-RsY2H3J0iYy3sDkvIYHUW8RuSpTrQ0YBIB575B7qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره مشخص شد که چرا سالار عقیلی در رختکن نساجی ترانه «ای ایران» خواند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97858" target="_blank">📅 13:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97857">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afX0mGWbijTEGPl8QUFLXlSVaW2DXaXUxpxfwPY9ujdxIPB-LjbE4dLnDLgWSAnjQl_A-F9nt745v3FfM7FlfEMn21FPhDbhECx0my3-Og8lTPa5RRX0lrdwEPi32YKWdpDtTLI7SHivn8BoTUh_VHsZClo_JWTIiuNUqh3t_Wh7qAI4c-tBwws7I7QzsA3M_RRwxou08lyNaQu7aBk35KkdhfrbGVBnQYXX56XDDtd8esfwRZyvp8jFK4IVgygbTDGZBdVTPQ3YxruFiueSXUDqTRwbAwgwvHu7YPHQTB9fIIbuSYFbHvGVGQ42GKonR9KyrjPFgVC_yJ_ut0SAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرمی مونگا با ۱۰ میلیون پوند از لسترسیتی به منچسترسیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97857" target="_blank">📅 13:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97856">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=nKquPjkqHMt1_wi3BQitxdn5zS-UINl0oyToGIM1wmZDE_gWRZftVCytxjT1yvmrRcpc84U8osqeI3dEOWQqqRGg2_G24Qcfjpwf4LQfY-3LF7jisam_DyxWUvdLSsEujpzvGMACP8PooD8HU4Fpm9XqmvGubFMYtOq5p0Ij7nqwtCBz-_gL-_AeP1iyXNzhoZsw5t3Vxo9r9W54J_49AoEeB6HVlmLtDG6gdGMTNIDWS7UoXqwBeWi1AGrhqFo4LAPjerziw-TtutjaZ8aRLhGC4T9dcY2GmKi4SiyC2b5apDA0pJ85VqWpV-iE97hkXgLVVNxuOO0hpbJFrAC93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=nKquPjkqHMt1_wi3BQitxdn5zS-UINl0oyToGIM1wmZDE_gWRZftVCytxjT1yvmrRcpc84U8osqeI3dEOWQqqRGg2_G24Qcfjpwf4LQfY-3LF7jisam_DyxWUvdLSsEujpzvGMACP8PooD8HU4Fpm9XqmvGubFMYtOq5p0Ij7nqwtCBz-_gL-_AeP1iyXNzhoZsw5t3Vxo9r9W54J_49AoEeB6HVlmLtDG6gdGMTNIDWS7UoXqwBeWi1AGrhqFo4LAPjerziw-TtutjaZ8aRLhGC4T9dcY2GmKi4SiyC2b5apDA0pJ85VqWpV-iE97hkXgLVVNxuOO0hpbJFrAC93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تلفظ نام مسی اگر در کشور دیگر متولد میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97856" target="_blank">📅 13:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97855">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51882d6736.mp4?token=bjgY8MHZhoh-saptBbYQTddGzLIjjxOVBV6GOIM5BMCggMELW0M1VKmiSBTL4z6FGese0iqv2_rFwpOcOGg6m-nLPgfx9iJA_GLyEFM0IR_ViKq_rc86K5fR5k94brKGqOuQUAmlp0UuQGCkbg0cEgk80IGngyt7v4XlnXJbiXQuvb6XWSwduoztdMftFoPdgsZ8GUCsexIu8aLJLFYRVwWeth0TkXOwBxE4jM9SOvMa10cEPdS-DjpMHfpXT2YaXnnJJAZ1-clH2q0h9w4QC5cjU2ZEeUUCi-RshlXN0h13DvwI6ECPpZ0-0bqXi8lWH7M3iGBLGjh9B3qkFw8_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51882d6736.mp4?token=bjgY8MHZhoh-saptBbYQTddGzLIjjxOVBV6GOIM5BMCggMELW0M1VKmiSBTL4z6FGese0iqv2_rFwpOcOGg6m-nLPgfx9iJA_GLyEFM0IR_ViKq_rc86K5fR5k94brKGqOuQUAmlp0UuQGCkbg0cEgk80IGngyt7v4XlnXJbiXQuvb6XWSwduoztdMftFoPdgsZ8GUCsexIu8aLJLFYRVwWeth0TkXOwBxE4jM9SOvMa10cEPdS-DjpMHfpXT2YaXnnJJAZ1-clH2q0h9w4QC5cjU2ZEeUUCi-RshlXN0h13DvwI6ECPpZ0-0bqXi8lWH7M3iGBLGjh9B3qkFw8_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود پرتغال به ⅛ نهایی جام‌جهانی 2026.
🔥
🇵🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97855" target="_blank">📅 12:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97854">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImoaQIR8-XiVjGl9T2dxXVFG1qMtU7i-5teohj8VjNmHoiGaAc6fepp5S6Og06tSlrkDcVLssU3GOgip43b0-ovcNnoCA2tHnfS8PBY7cxzhe3r6ez0aqHI9IxTGsHwJV8Iy3ndzF-0IPzAEwlyyRW2ajGoRZ9KyjFy4LVwrZ9tmV20bhGFtmo0278RalgVagLbhAnxocrqdghG3Rim1u0rq0mzE0JuVZgHnE5v4ZCazOhuWy-jpCas9zTSKb0ydWdtnpP2XedE-VSAVodWcCGpuWIbjsq9ZeD1IJABS2bel5fJORpUn-SmgSSDDwJ4qJEFROyM2-ytNaJ1l5ysXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه لیورپول اعلام کرد که یک بنای یادبود دائمی در کنار استادیوم آنفیلد برای بزرگداشت دیوگو ژوتا احداث خواهد کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97854" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97853">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCxJ8X8wiFIaI4rdFVA4GMeQ9iMebtwbjuhJ52sgTI_fSM11i2ufHVirDSnzgXp9YxNEr2bQyG21MV9GfsjVn0y9gYmX9JagGzJtZFV3crNrelX6l-w-MmGBOo33E8YaMl5hPK-3Ou3-INjt4HWc6xvla_JIOH7JeR7lPKMKvTyx0J3W1DeP0mNl5g3Ksd9hdf5Km20MHBaHdFFukdxbMr27Y_cNZmzX2FrdjKPt-4Q3FbVrGgB1DY3yuakG-_rz9xkITGlBaTrkuWacTr5lnLLYVPSPCZY7uoLAqfDovk2DDs_6iTtZEl-4Ghfa3ORvA9l6A3_BRxGHMdraZRSfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
👀
صرفاجهت‌اطلاع:
🇫🇷
فرانسه در سال 1998، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇫🇷
فرانسه در سال 2018، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇦🇷
آرژانتین در سال 2022، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇵🇹
پرتغال در سال 2026، کرواسی را از مسابقات حذف کرد.
🤔
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97853" target="_blank">📅 12:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97852">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO9Xu77HybpoAO4xZ2nnawbDY9P2nSKGzAFq6ERnwvjI14SmWIuPiaRPM5eHBm9qB0cr6ShEUUqTzEdbge3yEd61GzBt854S_vnJTlq5mtXYEvhGZjbbMtu-t1yVIiiKGDvomDW6sn_CxW0f7mB3Ak06YH7GxfopzwD1CgA0eCgUX4GaT32Kh2dpQNW7fpJQgYVP_e3PoAhkNeuHArvBzVOQDjI3LfKoebIrXj-QOO0eVQjdCDIAEBSXDcKGUvvyGF3LF5AMDgik6AzUJggo3o0XLiC1Hbw8Bt89qwAjPyJdQ1FAhXArQDEoiiOwyNnQJifezfmdtuN0_Jq4Z1gMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جادوگر غنایی بعد اینکه‌پیش‌بینی کرده بود کنگو و ساحل‌عاج حذف میشن، حالا گفته که امشب نسخه آرژانتین هم پیچیده و مسی باید با گریه از جام‌جهانی خداحافظی کنه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97852" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5nEYVqTRyOIlFwmkksm6qtcS11tIWPa72HIEed2yk2mK8PCiQv_RM0Ia3gFG_w5dSNJRAyoVK_H5OvitQGynM_tYqLAyXmcL0kpuK-PNA8bcNqKZs4UG0ZGCNEzU3_RfrRL6Ch9qvbGE3cChRepD2etX6GoKvtKWcs3csh29Yq6_6Dpm60iMGeGKXEVHgftYeOyeWz71EiCeOmpBSeTQJuXOYaH6nM699KbGi3EMJZR9Tpa-3iBpNYrooqVkBAQ7G8ggRDGkvv3LNB4P1IKGpS8F6EnzttFkFf3NCBkKOVXo3UrAUFVEjJIYizeaZAZPZcFkXOcO_oRcLU-WAhtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97851" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97850">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyI72qIGbMZ9fvQ5V199o2Fd8BuWG05SBiA5ytQxjkGOByiLKr2lDvDhsecRfzzP_wS7mysTA62Qy8kwpNMM3F_X9YkRYdpZchExt1yzWVDKfxdIWmxWWxo20ltQpZZXfVk3eEi_6Adb5WupBneUyXQGbedCQtKsynzZ9P9dMgjnTJrjCPqCbbFgSy2LyXxTkZBs7I2sSDUM1ochCGXDiM1xuiYhCW3CH9FekeTcAn7nXwSeXAk52LQwX32zcGTdKODzfuSHMwBa4v3vjLDyisHwDnA6uMCELxEJhFh_aA6LmYfKmOM-iNDKF_URo1LmFxHBKbyt1f7VXgz1UDHYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بازیکنانی که بیشترین بار جایزه بهترین بازیکن مسابقه را در جام جهانی کسب کرده‌اند:
🤩
لیونل مسی — 13 مسابقه.
🇵🇹
کریستیانو رونالدو — 9 مسابقه.
🇫🇷
کیلیان امباپه — 7 مسابقه.
🇳🇱
آرین روبن — 6 مسابقه.
🇭🇷
لوکا مودریچ — 5 مسابقه.
🇺🇾
لوئیس سوارز — 5 مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97850" target="_blank">📅 11:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97849">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFx-9rrRbO-GJWzSoL4nL0_VGuqgVPK2OSpSzHjwzsMXR3wfVOeJwmPCVAF062VAurVlnoVDbtYFGdt3yEeQ6XtiTvXwWz4p5qQYPX0dPemU5Hv_qal9xDil4JaQhevFHUHQt0hS29Q4B5ktLMSLwQ8JuotHa8L_F9iymnELThxrK11D4wyGpwilSrYWjZC9vaTh-6sLjv__K786G8emtGFJYUbR7gQLbv7s1tI5yqJ5JsjIMXeqB1P_Yx_ZhxVphL0G7WYQA_yflSA9BDBK4fpcNBTZpWT5eYWDvF7hyETzAcVVW5EcxZOn2kr0-nGhMBPkKQ72ruQ-0FKFq_sZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇵🇹
برای اولین بار از سال 1966، پرتغال موفق شد بازی که عقب افتاده است را در مرحله حذفی جام جهانی (در برابر کرواسی) به پیروزی برسد.
لحظه تاریخی قبلی، یک اتفاق افسانه‌ای بود: پیروزی با نتیجه 5-3 مقابل کره شمالی در مرحله یک‌چهارم نهایی سال 1966، زمانی که اوزیبیو با برتری، نتیجه 0-3 را تغییر داد.
و پس از 60 سال، "بازگشت معجزه‌آسا" دوباره تکرار شد.
🔥
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97849" target="_blank">📅 11:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAUsOeTgNu5PjPtM9nctzoOO5BGOrr1WrfVK9j4LuPStNiOfvk4dwxvo5mKU8IaeGHy3V8FYpzUZqZG7AejfqJ5CEj5JKAo-iWcIrz5pCsvgzR2c0amcK5E8TgYDmc63V5uVpQRRMF48vDJZeW_SP-92h3rfzpYmyXlbbyK4NG7YClbugr6Exte0ruUmpczq2rfw-I1je4CeVKOM7DNf_eGrQJrRUiDvhdtddegKm_xuACz4-I9lrIffIbkHmOqN8U1Y7OGWRNfUr8WI6VFBCPZYHH9wXzrsgXbXyc1rgsZ1T9sf3lRZOkGGRAX8CfQ9paF2Juwf_JZxzRiE5_kLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97847" target="_blank">📅 11:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVV0Y0uqI2mN58Prf8uKkbShCsWMfCrKfALlEpTCSKrd4g9NuAcFx4_6ZJLwoCaW_xbMQ-RSq5NtNFjIVhGprbjUQ_rmK0Xzyb3R-Y_3JCHA6g89rD7nOQIqjYw6wFr1doTKHsZJm26ozDx_qmkQJYGhEoYRfyhFC1-6_CzTQXn4KvtPfZ-ta05UYSXZ-YlZzWqN4PqIPW1OjYo_LC_nfRgekecwwlWa_xI13qAnSsd7gUuOUeiDxqfyQDRk_UCsS4EXbXJ5gyyKsiIihVh8rXiz2fAqJ02jlYt0DUYEZWGNMav0OXNLQt7CiZmgNnbM5n5fESzIdZEgCfgLehyJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید علاقه خود به انزو فرناندز را تکذیب کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97846" target="_blank">📅 11:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f386995eff.mp4?token=vL2gYrL0BfKLuJY0TC7fVswHUjZZRcDhq7uugBS771X9GDISHox9QIDKaFFrrzo4wvW7DsGqAZR5Rtmr8lF4JAMgDcfeMhDUYbNEd7_0Ir0I39qI3yaRSsgeUCs3rAzS7SjR0wlAkXw4DJB7GaAQ8R9d4Pm8HLFTEoYwqo6kBYdz9JznX3rJKej-O38LFcBA6ubqzb8cG3rkp3tuMHMifQNRpTBD8-CxCeS8JU_1tkJH2V-zSA0HQqhOgI13pLHpW6tmotoy3NOEeglEGhkBkyiCRr0QIuYCyOLAiL6aJZDifpztZ1tV1HfCRW2LWplKQ8fA9463Pp18WS9Qs4CWrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f386995eff.mp4?token=vL2gYrL0BfKLuJY0TC7fVswHUjZZRcDhq7uugBS771X9GDISHox9QIDKaFFrrzo4wvW7DsGqAZR5Rtmr8lF4JAMgDcfeMhDUYbNEd7_0Ir0I39qI3yaRSsgeUCs3rAzS7SjR0wlAkXw4DJB7GaAQ8R9d4Pm8HLFTEoYwqo6kBYdz9JznX3rJKej-O38LFcBA6ubqzb8cG3rkp3tuMHMifQNRpTBD8-CxCeS8JU_1tkJH2V-zSA0HQqhOgI13pLHpW6tmotoy3NOEeglEGhkBkyiCRr0QIuYCyOLAiL6aJZDifpztZ1tV1HfCRW2LWplKQ8fA9463Pp18WS9Qs4CWrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
🏆
🇦🇹
ایستادگی برابر قسمت و سرنوشت
دوران فوتبال عجیب ساشا کالایجیچ، مهاجم اتریش مهاجمی که تا ۲۸ سالگی، ۳ مصدومیت ACL را از سر گذرانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97845" target="_blank">📅 11:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwKOVrp3o6y_pB4O6jK5FqX5g6ofxnr9a35sxEXnLi_NAESb8Jv49GKvC_zeCz_2luAJVPHf7Ywtj8A3dwqmz_r-MjUvRqn8nGwpr-Dfc2gIYW3gLhFi0Gu6LxMjrBWhVP-f3iA0On-f5tMKn8fzR5dE8jIAsyntSOLqw-BHVIXua5eTXjw_yRlTyUzz-aObBFvlssTFzare9cqbl6htGEV4Ece262nsbnT50fmudTTSJ1tF_n4SBb7NWhpI6IM4Z07qYCkpe_25AQQPNCb5SM7G-KepeAy8nm6zW6bvd3UOcBDrZdEXBvy9_H_DLJswPH8iAHGvFRkF9dRmVwKRZsAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwKOVrp3o6y_pB4O6jK5FqX5g6ofxnr9a35sxEXnLi_NAESb8Jv49GKvC_zeCz_2luAJVPHf7Ywtj8A3dwqmz_r-MjUvRqn8nGwpr-Dfc2gIYW3gLhFi0Gu6LxMjrBWhVP-f3iA0On-f5tMKn8fzR5dE8jIAsyntSOLqw-BHVIXua5eTXjw_yRlTyUzz-aObBFvlssTFzare9cqbl6htGEV4Ece262nsbnT50fmudTTSJ1tF_n4SBb7NWhpI6IM4Z07qYCkpe_25AQQPNCb5SM7G-KepeAy8nm6zW6bvd3UOcBDrZdEXBvy9_H_DLJswPH8iAHGvFRkF9dRmVwKRZsAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ریکشن‌های اسپید در بازی کرواسی و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97844" target="_blank">📅 11:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SomISN3GH-UG0uiNob9w8fHuOlw5OhddByx6CtryvPkWBUTYJ3D9JJIDla_Af09pop_nrUEOT7WBdPHIj6OwWVQaGtWLJMVIGl5cgyf_xJ_WLt82ih-gvoSgxis2NJo9DXEFDTbnNWJdyV3KDN6_yjf68h0a24FJ-GPH0OuK3-2UsAatc-At_ORo-4fMz5g90SomrttFsUiMr6txDceaS_iISeJx3AO4Znnw2UUO9a4NKFOVsmeUwu0GhLv1mR6obnT3lHHcxUCTZfBnTIb3ji3NSpKQT-iBExtufz1cZlxjLyKS0p2p5m6DAjwtgxl9j6wyCqqhTZg9GJSRPC030g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارک کوکوریا اولین بازیکن اسپانیایی تاریخ است که در یک بازی حذفی جام جهانی دو پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97843" target="_blank">📅 10:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=MNnx62oo_ZKfPjAHgmQNKi1CrioWIjfauLWEbAglok_BQVIcN7G99zRTH3uuStfvcIANqtBmpAwDqmwbefNjDIz4wMioV35iJPoOhLlCin1KNI9lcN76RbsoKowHYZ-qULcT_yam27vUe6C5Ixdx6xDhNfBhEanKGRf1l5S_NvWoANSFmVr5bEPx5ME1w-r1it37rJ5N2rKRpktosdevSTWLYREYhQsd4R4PIE3onA3dD6JH0Hlt0dbUkaRQMYm6sVFcFV86YoP5NYMR1iKfzHIX4YHWeL1FNOpUvJLecFEtaFcjgs8mIM16md2U8rpSR62_S52KxNixNvoM-yDFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=MNnx62oo_ZKfPjAHgmQNKi1CrioWIjfauLWEbAglok_BQVIcN7G99zRTH3uuStfvcIANqtBmpAwDqmwbefNjDIz4wMioV35iJPoOhLlCin1KNI9lcN76RbsoKowHYZ-qULcT_yam27vUe6C5Ixdx6xDhNfBhEanKGRf1l5S_NvWoANSFmVr5bEPx5ME1w-r1it37rJ5N2rKRpktosdevSTWLYREYhQsd4R4PIE3onA3dD6JH0Hlt0dbUkaRQMYm6sVFcFV86YoP5NYMR1iKfzHIX4YHWeL1FNOpUvJLecFEtaFcjgs8mIM16md2U8rpSR62_S52KxNixNvoM-yDFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇵🇹
شادی رونالدو در هتل اقامت‌شان پس از شکست دادن کرواسی و صعود به مرحله بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97842" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0MKU8gu2rRhvQXcPQOk2nsdV6472YrCtX9lCvTKcqf_IzAs17HVqGTOb0r1jD9vLeiOfSdIsp9drqY_R5ernFx5ETQGDgE657y_pU2RorbPcPV9TPGxDe0n4hwvfmaDea-dn55OtzPWJCQb39tiqVRHQx7vrpfNDneDnonUCmutO5ST3f8o6dHfrlSYeBgoC3k9fsqFmdGG1by6gajYlvuWWKv_NGnM4Pdgahav9vwBUt_ForwPKJ0HdtDoFanV1JJ4ykRKvo4clpYCBIPfEY0yhxd4cD4YdMh9VFEu4xzu12Qy_lzjcSp08B4sZS3Arsxzmo9crrAqxh5VgAjReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97841" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=XiFQZ44J4gauuOc0NGG2ZUq4hznVlaOcNmOeQ8rBO9XDXIALYehm_Z72LMC68UQKBnG0-nQcp21rHCGNX_CwjrsgyvsE5OsZGgoOdxWTfPj9mC0hjGPXU_rzn1JPTURINy-8dqywLNvpEaQJAllyLNFRsuZr-lMfLtXmw_NqS-pBpV8-ANI_0pnTs8rHC6bVY3qvdEPq88BBNdrPlFUkZ4ZWgMqz5Wl5_43V4qantX9jt2aD339ueLsEYM_M0U6hAgA69uEf9zGilbwjxifiZtdhQTYUsdR1TAhYRJPY1gsPVrJEeCiteXla-BNwDOhMNj9VuOxgpYhc4KYAWiVSPmfBsfUfHjLge_Z7nC0LusykncJWXs4CUg0ices8cLpiXHf0SAi1ctAMiNxXFUi1lMCPj-xBjNxl5lmUAhfhHhwoluzzkh87L46xjRQ0xe6TcS7irkxQolPWqPd9zdqy2ewK20HG64aY1ADH73QzvZK_zktMYYbg534FGNxkemphZYCHy8i2tdKj1VOQASgsIr1xhXYnp7CKwtbriVOlBJI6w7nQcVEsFlu26ik6ilvMoA1_rlqMI8xlmxR3y-4ZjOBhSmD5nkPqMuXH9IPNO4PEwAtee6te-syGbi3l40-xTOPfRrILFPCNKPuIJcVTL5zss7X1HZ922SJw0ZAMtnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=XiFQZ44J4gauuOc0NGG2ZUq4hznVlaOcNmOeQ8rBO9XDXIALYehm_Z72LMC68UQKBnG0-nQcp21rHCGNX_CwjrsgyvsE5OsZGgoOdxWTfPj9mC0hjGPXU_rzn1JPTURINy-8dqywLNvpEaQJAllyLNFRsuZr-lMfLtXmw_NqS-pBpV8-ANI_0pnTs8rHC6bVY3qvdEPq88BBNdrPlFUkZ4ZWgMqz5Wl5_43V4qantX9jt2aD339ueLsEYM_M0U6hAgA69uEf9zGilbwjxifiZtdhQTYUsdR1TAhYRJPY1gsPVrJEeCiteXla-BNwDOhMNj9VuOxgpYhc4KYAWiVSPmfBsfUfHjLge_Z7nC0LusykncJWXs4CUg0ices8cLpiXHf0SAi1ctAMiNxXFUi1lMCPj-xBjNxl5lmUAhfhHhwoluzzkh87L46xjRQ0xe6TcS7irkxQolPWqPd9zdqy2ewK20HG64aY1ADH73QzvZK_zktMYYbg534FGNxkemphZYCHy8i2tdKj1VOQASgsIr1xhXYnp7CKwtbriVOlBJI6w7nQcVEsFlu26ik6ilvMoA1_rlqMI8xlmxR3y-4ZjOBhSmD5nkPqMuXH9IPNO4PEwAtee6te-syGbi3l40-xTOPfRrILFPCNKPuIJcVTL5zss7X1HZ922SJw0ZAMtnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇪🇬
مدیر تیم‌ملی مصر تو هتل محل اقامت این تیم پیش از بازی امشب با استرالیا با یک مامور پلیس شدیدا درگیر شد که شانس آورد پلیس کوتاه اومد وگرنه حکم بازداشت صادر میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97840" target="_blank">📅 10:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=WedXP10kt2eNYt_dx_qpSVMYXDKy0AbrPspQavfbkv4zlax-iEH2gLm9UERMV9Qxu0Jvfu1Ghw5F5LcRDXgOD1gK2gvP8_-S74D3t3kGesk2D7h-M2-Mu06Bez2Pt8EuBqjj6uKTfa3AF6lOC-nNUxKQuzlQ9qpM6TGt6tAkCchqtl69LedEiRO62tIWGJllk3lSWMaps8D0GXDNcc8ExPI5RcvELdFNvK44NBTUOgQ3OgUUj2f518Rj0p6X6E_FqrA7nMJtIesqc5F5Kd4dkJwUrjrHCnY8lrVAkaMw8dg9SZDNiIqChP3OE9kOVJyEeGPyL1csIBbXfngLhoP7hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=WedXP10kt2eNYt_dx_qpSVMYXDKy0AbrPspQavfbkv4zlax-iEH2gLm9UERMV9Qxu0Jvfu1Ghw5F5LcRDXgOD1gK2gvP8_-S74D3t3kGesk2D7h-M2-Mu06Bez2Pt8EuBqjj6uKTfa3AF6lOC-nNUxKQuzlQ9qpM6TGt6tAkCchqtl69LedEiRO62tIWGJllk3lSWMaps8D0GXDNcc8ExPI5RcvELdFNvK44NBTUOgQ3OgUUj2f518Rj0p6X6E_FqrA7nMJtIesqc5F5Kd4dkJwUrjrHCnY8lrVAkaMw8dg9SZDNiIqChP3OE9kOVJyEeGPyL1csIBbXfngLhoP7hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بامداد امروز شوت رونالدو به جایی برخورد کرد که شبکه سه مجبور به سانسور شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97839" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=GMfwloVlmvn-uZ0Y5eVvrU8Uu8OGT3HTCqgP_dvSZFu5XGnzNfgI43Ot0EFt4yFsJTKIqwQBqrUvQB16L_kFfjxQIgsNWTOIfC706xnqJb1gnaTwx4AGaKyvw4PlZxWb1UQOlDZC5YjzoAX0xvc-lL_Lfy-Ph86ksNw3O3_Z4OBNTuaFPI489ru3R-eQfkNH158HlyDsG8jVWlI_SUcRzoiERZme_46EWpSmqYYR15uGiWOa5z4bZTtcp7cxYXgl8O6gcVfwoqFBgAX2wjvVi6W7skEbLmDArrlB6yWI43V1XJcPWrpskTOeAZcipj_-8-TgBeQF3gNLok-eLQBc4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=GMfwloVlmvn-uZ0Y5eVvrU8Uu8OGT3HTCqgP_dvSZFu5XGnzNfgI43Ot0EFt4yFsJTKIqwQBqrUvQB16L_kFfjxQIgsNWTOIfC706xnqJb1gnaTwx4AGaKyvw4PlZxWb1UQOlDZC5YjzoAX0xvc-lL_Lfy-Ph86ksNw3O3_Z4OBNTuaFPI489ru3R-eQfkNH158HlyDsG8jVWlI_SUcRzoiERZme_46EWpSmqYYR15uGiWOa5z4bZTtcp7cxYXgl8O6gcVfwoqFBgAX2wjvVi6W7skEbLmDArrlB6yWI43V1XJcPWrpskTOeAZcipj_-8-TgBeQF3gNLok-eLQBc4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇭🇷
🇵🇹
جیمی‌جامپ بازی دیشب پرتغال و کرواسی که با سرعت نور داشت سمت رونالدو میرفت ولی در نهایت پلیس به سرعت بازداشتش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97838" target="_blank">📅 09:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=o2FIGrWLu_Aigit0w0potQJLFsytxC1B-byplnGtf1bMLsCJWkBjPGmbN07HfRztjPouckp5XtsIBg98ncJZBKXTKN9p9daLw4A9XEucLf9LT2OP1KFv4U_p0AF1ZBpII9knxLvHht1nxojGeMwr6oRpHqp9ElpZOoLp-7RZNgK1sErZiZ65AXqYjN7N-gnzVaK6Ejr5skJqLLP_8STOAbPScXJPXGQI1ZG7jC_Pd7QjvlkIomrtIAgRwYkUwd4uAzxbPdsp5MlKNbN94cKEzUq4MIdxpqt8O5Y_1wQD66MfjUcX6Po8sNXDqHUcev06VcK26Not--UQk1Hw5p0f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=o2FIGrWLu_Aigit0w0potQJLFsytxC1B-byplnGtf1bMLsCJWkBjPGmbN07HfRztjPouckp5XtsIBg98ncJZBKXTKN9p9daLw4A9XEucLf9LT2OP1KFv4U_p0AF1ZBpII9knxLvHht1nxojGeMwr6oRpHqp9ElpZOoLp-7RZNgK1sErZiZ65AXqYjN7N-gnzVaK6Ejr5skJqLLP_8STOAbPScXJPXGQI1ZG7jC_Pd7QjvlkIomrtIAgRwYkUwd4uAzxbPdsp5MlKNbN94cKEzUq4MIdxpqt8O5Y_1wQD66MfjUcX6Po8sNXDqHUcev06VcK26Not--UQk1Hw5p0f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
🚨
🇸🇳
سکته‌هوادار سنگال بعد گل‌سوم مقابل بلژیک که در نهایت فوت شد و به دیار باقی رفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97837" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇲🇦
تو اردوی مراکش یه شعبده‌باز آوردن جلو یاسین بونو که از لیوان آب مار می‌سازه و گلر مراکش میرینه به خودش
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97836" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🤣
داستان جام‌جهانی و پارتنر بالای سی‌سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97835" target="_blank">📅 09:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJl66wayZJb7bzy7T9XsbIGjwhzb8TrjDZFF5d7zOLLxDDWJBRT9HqHc1EGU6wJ5kQLcBNYmI7Jjbs6Wcs6GEWmvrO1TwGw4e8OgpNrmGWnGxq9O4PSpYwutOOdz3NH4fPTK6wu6ERHuudJiwRG9gFxOeKryi8DR0WGw6oUGTaOU2_rAOFPsDlmmVWKcRnqrhbJ2c0zKXFk4k6n1kc-gPHY6jFeo4Xkh5V-0JnVNq-_PYxO966-pbm6IVENHJe4S8pEcsrUL6xFJs5j5vWLZqK9zN2PM3bhECxsKOZjLtEVONnD9SnieYqhvTCB0FY9wOw-d3crcsgXZVAF-4ih91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری
؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97834" target="_blank">📅 08:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🏆
مسابقه الجزایر و سوئیس، آخرین مسابقه‌ای است که ساعت 06:30 صبح در جام جهانی برگزار شد.
❌
❌
در دور بعدی مسابقات، فقط دو مسابقه در ساعت 03:30 صبح برگزار خواهند شد: مکزیک در برابر انگلیس و آمریکا در برابر بلژیک.
بقیه مسابقات در زمان‌های مناسب برای خاورمیانه برگزار می‌شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97833" target="_blank">📅 08:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfyuLFQPXfNYLdrMmzhGedrBUzHNNKXH_DXT-NfwbDesbb0knoxFEqi1JPU8p7s121kOA8U4IQy-b6mh8rDxyh796MPKowO21GS9eudL-UH6t3SW4DaqMwioHxbcIfKjUS1Peja6xdlA5Wwy4Q-P1p0GTNVsYHbYolmJCXfCgYlMA8W-YatPeVKiGpeY7A9oZweWAcueOAql0CMGqEq4mcWtHtpwO31Fj8ZAnNUzpb_f8QX1RxdQQN4UHgwMkFdqeLc4Wa66VoVgcgJHctn53k_IxWginXKTWAXcwyF1JA46Pf11NpHhlSz_UIGv-XydnRnUQlpQhsiNucUMFRwEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇿
با شکست مقابل سوئیس، ریاض محرز ستاره الجزایر از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/97832" target="_blank">📅 08:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZoUeH7cYRu4kiF1eY7LjCkSHQjr0WwmIgpuzDlu7iDlNU_r1Sj1WVeBwWiA0E-VgpHxzC2_npZt2P8hTs0CRsB3gqIDciJfCQss9-Vm8JPrXashHNe6gaPdb3dRt4rSISuXLcI8AQKoMmZePZQG81XKmNo7Z7hCLtdGt7HOfDHBnL_zoxQoGZbpC9zN9Y14_x9dXTPUoAjG0fhVRV5CWYIp9MtFDuizNnPuBR15FXjevR5QpCV21CACzMjf-yJ26MGFqNnabh5LVZUPcCQHsO5PLH9LMsfXL_XdBFm7Lveh_IIjKS70BFhfUjrWKB4oaF8rgCqp9gwuoK5bG7suBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آخرین آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97831" target="_blank">📅 08:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97830">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sic8tkUFG6zSCvmdOj44UB797TOLygWY_wStfpWdqWPYoX2PSjayBwHIR9rpHGi6cGRCy6sVJAosb169P5S-dMKCKeKRKuQC9sXmeNPGZxWriyR1dyS0w6-iQn3AqSGKz4atmxjLJezdFVX0CxfsCR-jhOlL-PewAJUy8X8rRyZMJSGUKcVAKtdAcoAEg6hZGpv2KlnIaJJk7x6PPhzE14VPvccr962vX8Y2eqDb8aillcxMShqzYYPOM_Dr8ZF7FAA6SBBvg0L6ma2QKsXtSqRlFCwW1kubyK5oiXHf2156eIVfPkltjl4HssQevm2S9AbIKdKrC7wiAjS-llo77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهاجم سوئیس چجوری اینو گل نکرد؟
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97830" target="_blank">📅 08:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97829">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الجزایر این همه زور زد که گل بخوره به اسپانیا نخوره که اینجوری جلو سوئیس تگری بزنه؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97829" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97828">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d083e293.mp4?token=fzalUwnvl7kOgHqKBmBmwqcVA_ik90wzhpuByr8orhDq4ICoSB7Gf7fbvivvU4k9QK4_IblkCcAYBPqkHxcfwWjzNc5_w3W0Wa-zFURjXzFZQ0yYb8t8s-A0Zkp8FSIinzSYHsmf8TujnJHOXRfpe7rGBmRMq1kri6KxtcTwlhRXaPVPYBC9ZhSzp-8_ogdfyJc0935nOx9llHbeaRbPCwiWfUHrYPanZaO_hrSyC05m0LiK8dRf_uUIhg-uHRYI06nq4-EuXKvODTAlmFoQaGGlELAxLXM-BjakIYo8xotifZ460jpfRN8rt90xLtMS1lZWKJMOcZE8fTlD7OBKsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d083e293.mp4?token=fzalUwnvl7kOgHqKBmBmwqcVA_ik90wzhpuByr8orhDq4ICoSB7Gf7fbvivvU4k9QK4_IblkCcAYBPqkHxcfwWjzNc5_w3W0Wa-zFURjXzFZQ0yYb8t8s-A0Zkp8FSIinzSYHsmf8TujnJHOXRfpe7rGBmRMq1kri6KxtcTwlhRXaPVPYBC9ZhSzp-8_ogdfyJc0935nOx9llHbeaRbPCwiWfUHrYPanZaO_hrSyC05m0LiK8dRf_uUIhg-uHRYI06nq4-EuXKvODTAlmFoQaGGlELAxLXM-BjakIYo8xotifZ460jpfRN8rt90xLtMS1lZWKJMOcZE8fTlD7OBKsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97828" target="_blank">📅 07:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97827">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شروع نشده سوئیس زد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97827" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97826">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گللللللل دوم سوئیس</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97826" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97825">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97825" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97824">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7toF7RRqCzdpqZ7f4oUNnlP2An7rFW90Rn1PblQl6NBqnEsCc_confrjwBFkrQYr8QmSYCXP6G6OvCttwBGcEvlaYwFxGDKzmsdVYbquaXMVIhFvdfTtQ_GqaArIqjwxdbHV8NUkxNQH9RIxwfMcasBIgGhx5rTDK2RKWCRAdt8DeKAdoKDb-W9B8aIDQIatC-YJJe3TnA-oaOieXBnwIYzpBoRuZKelDMjAvDuWxEK2TWGWALXExWHwX2LW3j2_b_J0GcssVcAzKae5AzypJ1MsFKsaqUbDupvDOqBdaGwS7kkMhpeTPi_K4z3V2F7V-wSd4E6ipyyENtmVvax5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
یوهان مانزامبی هستن پدیده 20 ساله جدید جام جهانی:
⚽️
3 گل
👟
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/97824" target="_blank">📅 07:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97823">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=DWWHM_u0ux0NcrTA5PuE-nNC-gymqCWp9RoT5tnxgjqYBGA005GD2uXa_CfcdLV_DLRr1RVAH2Oc7AtQGrn2N0EQpF41ONR7Fc8XRTeaLWa95518QFgZUH6AHrI6JQellUAGwjSp9PTycCRratU1cNQhb1ZcPhsyRN6mfOgvlmIOo_lDgN5M1bhbEwTQovD8Jiv8nb6yvY2QdwM0HtReNTvF37WuXhFoShHdO9NZNY1RAbcketKGRz6CQyg8moGlFUCVJHstmtWFYvXTajuc0zaEeAyi7mLKSRt2Tgq80eLVxSNXKKdy0W_K2SJpdXJT9aimh2RAtdc8T0AP70k4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=DWWHM_u0ux0NcrTA5PuE-nNC-gymqCWp9RoT5tnxgjqYBGA005GD2uXa_CfcdLV_DLRr1RVAH2Oc7AtQGrn2N0EQpF41ONR7Fc8XRTeaLWa95518QFgZUH6AHrI6JQellUAGwjSp9PTycCRratU1cNQhb1ZcPhsyRN6mfOgvlmIOo_lDgN5M1bhbEwTQovD8Jiv8nb6yvY2QdwM0HtReNTvF37WuXhFoShHdO9NZNY1RAbcketKGRz6CQyg8moGlFUCVJHstmtWFYvXTajuc0zaEeAyi7mLKSRt2Tgq80eLVxSNXKKdy0W_K2SJpdXJT9aimh2RAtdc8T0AP70k4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل امبولو به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97823" target="_blank">📅 06:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97822">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امبولو</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97822" target="_blank">📅 06:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97820">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گللللللللللللللللللل سوئیس</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97820" target="_blank">📅 06:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بریم برا بازی الجزایر - سوئیس</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97819" target="_blank">📅 06:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=NvpmVYWS1gNX2Qzhdirri5_fhLCWP4hPhnoFp1ZM6KFFxb6ED_YwenYJ99EGuPsLmDuGCUd17XP5tvDsQutfmBUj5JMizEBy9q_noXc1kA4faCjvmupfNV-EQBhOzsv_jb_Xl2T4xvX7bqxcoM4lMaMaZmHgltVvELYpaDDE0Z5Lknb65OMhLr5IctWnISpRpKZggD0IOAJC88S41GT7u7a7yZ1DEqG64xIUSSRtvcFShRZoeS7sIkEqfkAh8n05M1Ms4nuxPS_Pqr7YR0ipB1pFr2i0WyvYxb8IC9ye1tYRKKl0pjEWLA2GLNm8xV3Jh4ajnM3gAbIP0bVG7j7cgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=NvpmVYWS1gNX2Qzhdirri5_fhLCWP4hPhnoFp1ZM6KFFxb6ED_YwenYJ99EGuPsLmDuGCUd17XP5tvDsQutfmBUj5JMizEBy9q_noXc1kA4faCjvmupfNV-EQBhOzsv_jb_Xl2T4xvX7bqxcoM4lMaMaZmHgltVvELYpaDDE0Z5Lknb65OMhLr5IctWnISpRpKZggD0IOAJC88S41GT7u7a7yZ1DEqG64xIUSSRtvcFShRZoeS7sIkEqfkAh8n05M1Ms4nuxPS_Pqr7YR0ipB1pFr2i0WyvYxb8IC9ye1tYRKKl0pjEWLA2GLNm8xV3Jh4ajnM3gAbIP0bVG7j7cgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیدی ژائو نوس رو کاری ندارم ولی قطعا ترکیب استاد باقری و علی یاسینی یکی از دلایل صعود پرتغال به مرحله بعد بود
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97818" target="_blank">📅 06:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YugBTLIw6Tl_dH5k1FlIfvnkiC4iLuTs9MjG1cASDJEA0frPjk9OMJYWRJJAiJqB9wLynITnnjmwN5uhdD-rutWx-6DX4tShlbfySaSnQGlP_fWtWuXNhKY5bQfyOPzCffEFTnzDI966kOvkENZfb2dH5HRaCPamx9SU8aGRL7AmVfeEzAG01CQbtOhYlTLCdDCddn0e33SYyjvJ-gTYYNWS_0RHparCgwe_nSTdjTjnMxDCSA6DX1WK64LSITlGNpZ4dlWaak76f5nVE1gy0hxdB78xuLAnzxKlhv91_hhIZMDoOIN-rikE_ZPvE_O2FFZax8Iz47ZTcBsE4A7tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"حواست باشه بعد بازی کامنتای اینستات رو ببندی"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97817" target="_blank">📅 06:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97814">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFYuT7mlrKjg947kHAbH05uAbGUibSxCd5T9HZijcpSqpcMvuR7wVCnKF98qnaUJaYdW2rwCWqSOgHYpQWaDqyaTnFusoKseIYKQfkIdjUd7eJJpq6-TWzr8h_t2CVA3QwTtvk1qPeX7ojjiTzoRIMjdxNK5KmslUZ8rJ0kOItRJ39TZE33kpy3F_46gdtyUcxQsdesCV3BPhVDfAWH_j2cq2ObZFUpbYV7hMTEpT_88ssIBCvvL_BbnxLEzFob4zD3tvVG9QjxcPSUVA-MMVChTrWbFd9tqIXxqGyIHOsvLXQ3k6zSBYpLXFBhp0wL4lsid9gcFvUucp2skpLlZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiSlhZ6JP9SBXWOWQ0ewdjAoaZz7Q1JnqMlPu_2HMCUL3fehVC-4c57STD9zvLWlSLO6kg4ulw4_C34pL7QGod1nLcBi0-UKLj_9OnFg0NVGWS7MG9yLM9ratq4ltjwyItJd6PrYSil7mdQfyaKwx8JeRTrAj_qs31NmvGSDP_wxCUXSDXcu3ur7P2_gDg5t9Vvyxd9iEeB1a6SsCn0q6HqBUSWxzB67dtSnIIezTUYVCo4fnsdR8HjTjiX6oXdQ6Oj0M3lnqe9cditRPPR25q8wH5RO5lEmZCi_xK1THB_Yum76ZWCYI8C_q2rjGMFCKHHbHZi5iKgTDQK8U-iL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvWyDS3Ui8WKnX2-M2vntpOUnjJ3xpt0IAE6zopK2whyOboRVZGTihTEfpUDqiavU5knLnBxwpx5DkN-LDBTgFIKvwO6umwXG6R6OtZLUCEnCQyK1KpoGDx_DhlKygrLbl520vlXtMmWtjvMfpYa7xtv6H-vQTFbXJtApmWGFFwYIqo9J0f6vBGmf8LB2cqn1Qv_RMrR5U3pDrZ_FIQXpZYI0IspYh5ezqdq9AnWloQHRHDJbZttiCv9i7TLY6syIrdZcHy3JiR5jSdb8-hv3Jim070iDQLtU7VZSJh42zwbkccZNBFNyIFUiBUbBbJ1MQxlorXXZjWHhqVmFYKWFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
از دلایل صعود پرتغال در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97814" target="_blank">📅 05:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97813">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTBxPeXHBUceyt_zKlp99fJyJEyMtNY-9FAWYVtykRhSSMIXxd6PPhfFmrdu0aHYojxYlON-LIeOSafFk1XGt_Swi0rZcr5pDazmDeXH3QM6zIfDarBVA_JLXTT2aVFmXrcZ34W2FdxfqJ_ea9uRmNCKszw3zZTwXoEuhW6ES7QIn_7eqxBUz0B2pUde_LFdR49Drb5QGCHVpY6nxZ1TcaIylLvia8MwgaqW4lxrvZowHWUZKTqaw6RnqE75b3GV1D-otmIwqPBoCyMKx1lAmjStS4XjUR7xm63f2_e6ZuZw516YIOOcnRRuJr3-fuC0DA8o5AUGmQA4_9gfAHSVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97813" target="_blank">📅 05:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97812">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Viunr8XjGttSiB1A-y4ESPNVC77KKK6S4IycIsM8CQsYTpbueglD7G_bnZmp9h2HyjyLbu9-cOd7LJtOypz7jObyTWXKHmG5hgduPXX_6S2Yt8jfA68iv4sj4smViS1H7P1Wo51Kc2M9RsHvXmbR1hM9LtboCuNBWih6jfYwtnZsgFJbsnOMGLSZWsE2DuArRQTJUiCtn57jbV3WAvJ04L4Wjv5dMwIvN1NrwTPRwR_mBZEoZQ3nbX0HCbDzj3PC7KiW0mvHmsKf5YptVb75EfGiq79z45TwUfqIVWBf7owTN9VrxbWW8lzc4h-nYkxmjRiPe32_DdRXNZMCsyEfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
قیافه لیائو قبل از پاس گلش به راموس:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97812" target="_blank">📅 05:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97811">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU9bAYUhwYRsJ78BmyK5s2PWq7PLcP8oCs1ESdrlMlDYi3VrdvbVpALcGqDb0HCq1Kbz1V9WegP1vad8qdiYciB-AaFKTar25S-EOdj6qht-qH4KDsu31qq6q2e2ZTHKPZo7lRhkEE14xC4pNhyL27mVyNQRF2ofgWGNMT57RnOvOZbAqHOk2Hf7M4Ti6GGrDBXFUMYqFjEyRvsDsXk6DLBIbpEQXX2vRKRPpSYjZPC7kbvh5gtG5D5L_Wo2yz_K0j5HynxVLAywLT44LnfmG0XcmYyOo04GioUlasWaCLCDFtM9aQ8gGAqnWGAMeqvVbivopYLouKDORFNU4O0ing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد برونو فرناندز در مقابل کرواسی:
❌
0 گل
❌
0 پاس گل
❌
0 خلق موقعیت
❌
از دست دادن 2 فرصت مسلم گلزنی
❌
0 دریبل موفق
❌
10 بار از دست دادن توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97811" target="_blank">📅 05:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97810">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3znK63TPr-pjSakV6Au5aL65p10_SpCdVoL_2rVKwSHmBcvKQrWoMkH2CG-L8BONJrT2plBs01ZYjkC7cnpInvAOQUDQ6-0ZqvliLDOzgEtj09qpet19UDFzQBL5pb-TGFkna5-SNWMNBzf4NoX2WXNmTy5p3c5-Muz142azxpDq61GRFVTc_MH2cS07K8mRg0Icp-OzE918MYEVUrFvFp9pEgp44RsA28qy9477oNIx0Zi7DyvGWAQ1YbkC01JBxkrsdBNnNPSuT2EJfoTY7QzYE6ioKwVgxCFXP29CmMCxO6EywH0pgYbDnmDD1zYeLZXMpLlLPzro-f1iUlIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کریستیانو رونالدو مسن‌ترین بازیکنی است که در مراحل حذفی جام جهانی گلزنی کرده است.
🔴
کریستیانو رونالدو: ۴۱ سال و ۱۴۷ روز
🔴
په‌په: ۳۹ سال و ۲۸۳ روز
🔴
روژه میلا: ۳۸ سال و ۳۴ روز
🔴
گونار گرن: ۳۷ سال و ۲۳۶ روز
🔴
ایوان پریشیچ: ۳۷ سال و ۱۵۰ روز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97810" target="_blank">📅 05:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97809">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97809" target="_blank">📅 05:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97808">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2J-F5hVi5xXll3WDQ-fFgKxYt6Boy_1SePp0fyLMz2B-6uAo7hQBKFEYpr2ZR0EfeC5R9HVnTVtKs4RICQucf82cNp-3vmFBC3lmMen4pKTl-qGYD6fCeLmIQ2OiPZ7eALTLrtj72UyHgdFLatjtN7DiMNjQgKWD1aDvujxwNXI_NkMhzKhm6oYlh1lJ2lcFPH2HZtidw0Jo504hUmHITsB_32wZqHk9c0JB1zBsuvjGlNvQOL8ewQOEEy7uVP3hmfyrZH1QPWrQWQq6UArYs_1pQmqj8kLY0980XQueqVwu0r4OFjqOVB-XRqWEKYPFXT6tI0rBwByUNXS_qiuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خواهر رونالدو: رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97808" target="_blank">📅 05:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97807">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=Eo4k9IYHisz8dVNelDswtNMNIHIpdlbrg54To7zTLGGHZ-mmvrMSpQ-UC7BMZH0gD_yu8OizonlL4truLK76DRVxGlcB3CsCX1rCp_JzFcUNbYQhtKRKIrMJyGPC8qWP0IFdAz4ATkji3Fl3rvnxawb7elMQk99xihROKuw8rp-KQD8JUGLJOcg4nVK7kOzqfnxjPipDqBS-wbPjGLPPtnkDAmU6_agXiGwwySOsMWpZiY7mkwn0OZ9IBkfCU5sdK--HH9E4eDekP5l9BxP6ANcIII44wSkHzR0PsHl3cqnSpQhmgsE9AapKmI5oD2gJOPX3_6iBYNnc30Ib-Rt_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=Eo4k9IYHisz8dVNelDswtNMNIHIpdlbrg54To7zTLGGHZ-mmvrMSpQ-UC7BMZH0gD_yu8OizonlL4truLK76DRVxGlcB3CsCX1rCp_JzFcUNbYQhtKRKIrMJyGPC8qWP0IFdAz4ATkji3Fl3rvnxawb7elMQk99xihROKuw8rp-KQD8JUGLJOcg4nVK7kOzqfnxjPipDqBS-wbPjGLPPtnkDAmU6_agXiGwwySOsMWpZiY7mkwn0OZ9IBkfCU5sdK--HH9E4eDekP5l9BxP6ANcIII44wSkHzR0PsHl3cqnSpQhmgsE9AapKmI5oD2gJOPX3_6iBYNnc30Ib-Rt_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینجا که دریک رو صعود کرواسی بت زد دیگه آخر داستان مشخص بود:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97807" target="_blank">📅 05:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97806" target="_blank">📅 05:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت؛ گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97805" target="_blank">📅 05:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HootG6F1jj7S9-QSYJo5KLrlbEXrGKL03DAep90gcjUQo9d0nIgnYFmI6-0_TShsjvc9XyJJmhrFqEygSYmSeQm1ZneC69or7m2nq9zEsg5hsfLRHOUTfqWcK3fC76-_Ulva3WSvHJUMjWe7skh-G3EvsRSZ9xA5ZzPZIxbWdtHZydqEWRQx1u-3ZpKLfXnCg9owXEsPkTfYpIJ_GlysTQdhNAQN6z-J7NQVwBPUCN-zYSfL_XEpvQBPFlk2en4RaSCYK3omS3vtkpPRpvKdJ3rDsqwPOvpI2QdMzsl2yzADaP9TdJvSGdihTO3P5fPtEHpKyJe0FC8eEi6y7qNTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇿
🇨🇭
ترکیب رسمی الجزایر و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97804" target="_blank">📅 05:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2ToQ8rwCEOS6CW__2vdmUSW2mfK6nnV3weldXDUtGSV4O9LWJQenmf2y0u8h8QI2pvYpCjBQ2dP2XPjncwngXcLA-wiR3TaHVaQt3nSb4VJzleeLklyTlyxqkJJorRdoSFXueF9oY3FTs6FT3i0R09SVZBOo6oWxoNrOT9M59P9oauY4UWgPvza6BZWnY9barQUZdMQRBR9F34z5VxzjG3TB5EXDqBA9AdHBMLVjKVG2dk6wnWP3Ezq1-wQkJyaCQj50SKFn151CgJYrz2xCpdLY4R__6QLDz9S3WV7ArxFVtGxg_Of8ZMfx-jeUuQScLpHS883SBAz4lFGD6IhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97803" target="_blank">📅 05:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9ut8kbzOWZwQHzEUWVHMVWzs7rQcy22l1170YKc3TCl2wlJCB0N9VXqPdnyVeN0iprou1TxI0zkE90LpuKw10hq15pFpI4QAd6JEeZ_yOzHGINST4rqXYwBKM2j0O75RqWsttk1nX0wEo7UtTJOkmfs3IG-yrAYFO52cZMsHMj-Pi_0-svs_02IG504w8YufC9m3MKdiBlqqjEKSUMVIO1TVh5ig_T11Lp8_MiL7qnsuN_qk_0FlNq4vPk3OfWHiEqCkNXrMVoW4-Py1gXxkfz9EXxpYbgPGsyBkabBZiCdBG7BW1O3pHPFjfcsofiVtDc7E6TOkqBD8a2vn51FPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت
؛
گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97802" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5-zsv7ZYw1KO1HJ013b3neRkbNo-KNO6kpc32B1D4IlTHRMC5toIGli_S7voxHWPKCKl2w1E4zKK6kHNM7iQHq__BiadLH0d0CaXlfP75JE_yHttPHArNXX1hwjd8CwWXR7dHs48UGQAGT5QkdrGrNU-VGVR5psJtQPOQLIp7oqo5hKcFLjvlk5IYJ5giuVwghnIUxf_J1bvXxdmJQf-IyU6jWQF-O4iNLBe09MLpl9FrMY9_IEYqiQZ__giyP5TK3pGxaVn5nvaL7mIay35t-wuAp3cLwSFJcrA19C1LE9yM3tbsb_Cye6dDo7sHFQHZ8r2NqAWnP5GOq7jDzXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های کریستیانو رونالدو بعد دیدن تصاویری از ژوتا
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97801" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97800" target="_blank">📅 05:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTM_WhE3-PWuWUENgYxN3AmPoW2tN6HF5MkG0RxCsPhW9cTUe2rmByVTWZZzpKhKFFlqC42586SZ_GeXhApC5uzFCt4wtLq6jk2wCF2oyPzj9wIPFsQFTfkK0kRTL0lNLF8UP5nrvLsm6H_tyQ4-41J8s2GivY0e1RbLheFei4T3FGCAdJvb-WnfV7CeqFvmGS4Lcj73Ge4Y2F87Mdt-7aTwhIKLgoSvbsp5gmvIk6yWNqkfC0my4xK-65fbZOq73CqwcAl_CScHS2M4CL8rdgYepig1fxYuVFmDhFg37wDirJxny8KBzJ5lRYohhzhFeZkYfi3AVL3OjPI6FuYCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlpjDOWzJVlirGnLb4E-M4JncTtfdZworml2__lPDuHIMg9NFuHG0WJJdtG5Cz9GWlRmgtHvS70F6vM2oluKgB1HNWUsS0bljEVZgsjc2-rnL6tFOGGPX3j5FyeTmKO6-iKwaBma2m92uG_t9ytdBp1j37qckkut0SJFgnmpSdcVgGTAy9ozuyypBBI7kb3AWlIBk4YjMk08D4-KPfi3QOhUjY69leS9ktq_wq4RwGT7LYHM-Z57do6SuNVjlhYVQRBtXL0QSNxs7bGHV3PE5JcmFCzgLH8zrznvElMygvjXPnfvdOyI4yPC9v8rrtarfWxNaZdIl7RhrDrxQSNwAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به افتخار دیگو ژوتا.
🇵🇹
🇵🇹
🇵🇹
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97797" target="_blank">📅 05:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97795">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhgn0A4gHf6P1ZiM2c5f4m4adHu281CRpDLGOlmwkR52_jXY5MbpuKbJwA4bDzICARnkzjIxVmviJotwdLjZSwDRHiCB5icC5YUad9YJNSxoBqbkH9uUg7NQ23WXTRM1TD3fnkiHIZnm6z-qnTlmlIhOQ-pJbB2aG4k4-TS-VwWdS-5FanjjCfcJuonnct7t8H_olGuGMbFkqo2R_-csbQAZDvOuIL3W0beCROIZlNRoCtqJjGPJBaqZZsVMUoBJ5TWfZo97C3_oMWIPLu6cFwIPWulX_tA3EyFkX7l0a084RozJksK9ueIWJ-v9COvZCFl0xSL_CrksXGgA2Jfsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97795" target="_blank">📅 05:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97793">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jP0YUdAZFTmHmlPFYw87PxtY_x3DjZCDTnWdQIKT1mT0K4f0mNOVsadO9Gefck-IBRxDyI5vomP1qenEB4-1pjehFGY1jTl0ypmH_ptFgg6bVMx_8Uynu1jvLDCny6qhuYFTCgJJN7oKdpKZwbIR7Zky_hTdN16Z-OUvyrYT9tr7lWxS4KjP8mskuWGKKGPQK5vQL_br2uGPwIbNGQ9egbk0GaELcltii_F1es_KVeMUtMMgSt7adI6S7TyeZemWp0Rd9DRaR0xwjFJpARQ6Dqy9xoh4qZo4sRNhQHSE1Grn5Ih8WAbdECosgYmSkO5ed7KNjxpV-QT4UVk92no6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfBjFHvkdfHz_ubi44KOBXniDlm4LOTz8Bikf32vChfsSuXvrDY60gEtVXdgD-s_A7LoZ2a1A9qrYWg-ZrSfKnkPV17-FEZbgtPF6BnbBiwQa5VJJ_rgaoNjmcIQOij_tN0ST1-Hx4JKgajADqjVZIMDDehNmbSHXhZTCvG3cVqJIZaiFbjkF9nbKRbzyex5diLfFTli18ZNpT_vhuMTKJBeahRJ3qlSmFGHu6tHOWFyw40o10A0FBVHAMnctkRb7AFhPTjELhSCAGZNxsBU1df-uZyqwxX0US58jWKcT9WWog2gUiiHH6o_pFL98Q00TiLgQx64H7uvPW_0LmVTTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقابل دوباره و این بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97793" target="_blank">📅 05:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97791">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qClpduj6VgXyc7ulavkeHfkx4e9bek68JTOshmOxGnkdexTEjPyL3hqRSelQ3Q2rQr2YzB0mbp8n-qHeIAU35_CqXehyaJwSNKVeqEjfQctDrFrIl-JonaajvvUB40_aS3Uq2jFNhsjmBAe4zscvMrAigpocTNYSgrNrQopKjWn19QKINeyUMpdd2cGCmSGSKij7hSLtHgRCFILSWe8FMMKYVUUyYcUhOkO66tEfDYPO0JvQMROKlbB6v-0ZcWUDnqqPyTJI3OWz38htllbVxHIt0imJ8twRrPT7diuibRMXc01Qs8gzIQUh9RFCynwuLm_JOsyhJco2JAfgdWypNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97791" target="_blank">📅 04:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97790">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGf6uarlPweB7Zfktv4MWhEKz3MdvllBz19LsYQ7IiABkLrlD-8Ko_8AFQEvFsU6awBpoFBX2iYZ_vt6TM3DFFQMSgzd9JC6ek4F77cDT8cEQzI66FkmhyHhAaq_MqJazTsdXYVgF8WnliXmQubZUdY7XPKkMm5ZVOdJ9BvjKyPQJgOdaxfE-H4Hps8tcB3VR0YT_rxE1aUzB6K4bAVYCZuDWARwnV0OSPuM9PwbK-9KUxpdwQ4SHc0ZMzL6KIaF_4-5QVS1wtIY8LBC55Xmv4I4Ajz8V6cc6A1dfvHJ16rsx7xEf_R5HBHi-M207n4peva1hydGDjJzHhAiWaLiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97790" target="_blank">📅 04:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es9ZnAefikpKUfU3wecQ9xaNWrgYhIFgW0Dp2hUwDu7QDrWXLxlPCRD1amz8wQY2tl5O1cfD9gAWw02etzylP1d2H7t3U2y6MXvf8srdQGb-9crtyy9z4soLiGVI4JnDWsHZ2UFQSjKcr6fXZ-QX9FB8w8zl9q4iPI0V-kgafZ53xOecy-4unQiaS96efVap0Q1VXoTvvMA_pnfgO2skg02rDpYfNCkcSLyrDTSZu2OK1qCoAL6qmzOYRuFS7M0bHWvyUBjhB1Y7GEsm1WWbxbBkLA1CexNG0IjWwMDRlZzCwGtZV_Z9Y2WXjWt6_0A25WqcLxucCQr0LJY0hEJwAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇵🇹
• کریستیانو، اسطوره فوتبال، اولین بازیکنی در تاریخ شد که در مجموع مسابقات جام جهانی و یورو، 25 گل یا بیشتر به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97789" target="_blank">📅 04:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97788">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCgQdq2WL6YwpEw5wm3Rx5_zUKCAqIt-R86BW_K2zfCIn9NuXeqZlb_SL6Kdsn_h0WK68zAKDDp3VTiMIh1pdib2s-85phpwVN5_pBaZ_t4JwmvaJiPuBAgFO2S-GHmCNARqZ3W4ZyrFq-FmKB1CAAl6aF11NI78sNHwLwhPZ4eLsSZc-70Y7NvZ9m8gGfvAOzaco-vPrpAZcEqgPeOgOaHPwEEEao-_C3_XZdhOG8MqT3ufcMr05h1406cZ8KFcg3j79zcwAykoJQqoplQ9lHU-zTJlGH6dGjcl3gzMWcGP3qbd9tGsV4hqJObwIwAwZmYDGmWNmOuDVK5env60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97788" target="_blank">📅 04:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdsBzuaLCNDwzrvlVEeFKsiaHf0YTO8Whn20VtZyOsgYVVAWCshQwD_zDIzq7oTQ7e98gAMDB-ULrTMyLFRuOm97DnEmr3IGHyd37AdT4u0E2_sK3Fl8mbNwmuq5XN7L7xYRQ3a0_oVff74FaC_nEt85tLsk5UnBzeCEniFg91BiYNHPTjFfwIiM0V0MJtYzXAzLAyaN4uItjZzISB3dTc65Z2o5lP_TWoT7M2CwaNZpI1uWXbGmAkW_XCB5cf5qZtaYGJ-ZxMzpODP0cN_HrwUPncRJRUDE2BsNusMhEg-Xr-Q9jiYDA1tJ8OEngptqEWcJcErkNewFzcGLGDXIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97787" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiDNeamFsCxXylbrzDI7STDP9qJ1LBWKCSDrMfV-v5Ke1mflPs59aY_BxLW9k-9PIiPspZgFGSOmQSzG8C74iI4PNhB8AdfdAMsdv3JRg7kC_riEpcCkvr-gnBH73GL4dO07cVU2wET1QDES8_kUfXXOJdwh7OsOBTW4EZdCZ3NksHzcah-wIeBOIKp4u3HCKqgxpyy5U66z3mN3FJYJvwLr_fLNTScElket_dqpvnaU0q0AzHW5R0t8CKjQtv5B6ceix_cPVq3qmmsoOJ4_cRidnFYjsCNqE3SIJuJDJ_1DYjKcyf1QAYv30z6MQ7RPPAqIrQul-CVKPUJ-R3yOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97786" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97785">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfwHkUttmW1rLfqDDH6okfBcQXD4qQZ3UBdYds9nX9JMZXhydW3aFpMY9I7iX5J-GWt9j5Z3PcfkvU6EBZeWYGv6djpPVCITrHDeadXtdXJibArql20CBlhpOC4uuTF1fUUhKmsoVqS07Y7d_NgnFlpzCUWAsorJOyfDUaU9d3LoWC0lXES7cHYTHdq5D46uyWzN45dmdF6C1JhMvFZKhQh2Ax8i9wdtQe_9JZCBS4PgdBuT1t8Eut4K5hIWtX040LhvBCFtE8d90cImisFUc66BguTlmOm7AV9x6Tl6ZksB2n_vJ2KdSP31SD-dRib1PofacjkgjjkoqKLCQfNArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97785" target="_blank">📅 04:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97784">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0kG7DAqE1NoZIIJPHkvoNSMfU3Vd1nPZMsJ8Z6bF-lo7-fx3_fzragBKAaRspU3fxAoo7_Gaj0U2C0Y3wb-7nArBO5ciDJSkFjUdOJrkTY5CNifr8kg-AGG3XsAovhZ04OCyg8odU0_bz8BI3kFJJdNjb-lQRK05RAtdNz-A6YXSt7-1tlfPe88ECF6cabJcQAEREkHE7CyXCAHkUjvA022praSwKCFZaNFJ3Q6OwQs5FY1ikJ74uJibeOxnFLjRCapBNqh7MDZ4qKMvCwtezPCZM-cw0gLoIHEHzswPSb8Dcbw6y4Vpj06EKf_1jcG_s170djAtte3mHuMm0a_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97784" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97783">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تبانی اصلی اییییینه
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97783" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97782">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تبانی اصلی اییییینه
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97782" target="_blank">📅 04:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97781">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imXA7PlRX4xqZSaqj7lqwJ6HcjIbHE4rfmfpvKwhzgTBVBvPbgV2v2Q4kz0qJfRH-B3E7VQuQdBYNkr-jMnELSZxPfpAgl2pcepwGZiTMw9-tSR9jWYF0b47a-pwhgH0ZexJPI3x80i2P0VuOqFoIjL_bQ-A8e3ihgf59U4nVjd_nvW8GpXcE50YjVnGp9jF1K-a-YqfISX0pLtJV5GMOWmbCOYsCOvTqWd8W19ZNO-EmKnWakxpojurOCWrJtMyddcC6TWet-HW1dqCPbjYWebosBzH4Nz0_bVjJ9iDJLm9boR1DSqS3hWgeyNr19AjVnlLO1QMVQEtj-h-pfUnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97781" target="_blank">📅 04:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97780">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYD8yKSY3yfBqWGe-Xsd68oJs5MygCM7JWRHq3KExmtHQ_AtzBdFF-2v0H4FYErwt5A8z6O1oKNLvKqtOz3INtdSA6uIP3mn3AGmZDmTfv2So_uYFDBuFCNSkcKMYlyOAG98Td4gFRA8E-a1zvd11iptgSYFYN2kYfavVob0eTid57AIVtzWyH2GZGdl-jCxxfUqB97dop5YoFZajvrn5YX0dLrArgBJwRgqf3ADgaHipxtCDDuFqDXIQhCpDmbW6G6AATqUOaMXAZQataACnV2rw0xAZfF41UpCPJCv4XzXAllcA1A221btgkcionNiVjW7c5MzCH0Msc9dlT5j3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درد دل با کس نگفتم درد من گفتن نداشت
خنده بر لب میزنم، هرچند خندیدن نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97780" target="_blank">📅 04:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97779">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رونالدو باز خندید
🤣
🤣</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97779" target="_blank">📅 04:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97778">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">از کووووون آوردددددد
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97778" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97777">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گل ردددددد شددددددد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97777" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97776">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رفت خودش ببینه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97776" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
