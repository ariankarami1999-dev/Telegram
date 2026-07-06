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
<img src="https://cdn4.telesco.pe/file/uj3oj40kWhW9OP3fKi7TzvQqREeVC10_UiJKzSzUDOH3Rtj1i60XZ6RSpNeNo4ezQQJSOI6r0wfEC4dBC9_rCI95Q_cdCWNH8BC2VWasfGgB-JBzd4VtrxdGDML-J29Dy5S2LV9UFrLVG7HulKEM6ZfABw8IzIvBcvYn6joamEuzPoxzBF97Jf0VzvmwMptw8jy_asIvK-IQuTa2tBH9Y_tJc2kCU6UvTV6axICsJmPfa3HxVQqjeSdd3i7xLnYCF5MVtzlCZqYAYUQUtNHK5Dl6hE3frUmuc_bDZcy0MM1Y3VDBFKG32xEfZqnUZWKs-5HKU0HtHQbNOsRXMwE0eA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b422331f5.mp4?token=DO7gSDSqxld4RBhKd7ZgTZpFsQ7dPFurjKDX97jsqvB3krp2ZOolOMZ4s-GSB3zafXO0XIlB6pLPU5e8l62xtjD8XPlCth2NjYZ104BnHFOY3ivmFi614GQo-kiiy-5z6LVuLHTq_lMNVpo5hZSv_xmX_EuNPoDzVFGv98BbEnGWaH3dmpuJPvRM7E60GvVwSH8LNC3oR7zmw3PzpG6pG4Q0oQIoF17dvFO_elRRjY3dKSUGIb5fE5rOO9VnH_rTEKGIQ6v5hsWGqbjNqDBNrFwYRWhBVdCOzK332hp8N0tn9SWxzSaHnR3RVKiMkfXVQ5H2x53pJ41_RqR7VvoKoTl-vyy8pSV9OSZA4T-B8UNoggZ83mIwEsx8IkW71pUJX0hT-zOqG8DYHfhYXQ6gBwwmCHOAIh24VI7mn7AnQFA8Mg4h9oG-xYBGzevNQkKvlOxQAM1H7wr4TIW-86Pk__4xOFqmd_-83Z02sw4Ri2EBWkzGD7f5SBJ5mbHd1wniwBDcBCcMqoPIYBIy_FtpdDV6s-IxQ-oRD67CusV1uOqOZ3I4B0BCJJDqnCVZNOBZt0PymJVKeWB-slp6XZOvJfKFf3cpCDBikyVpjPfsJkWv6Xrm5HpCZh2Op7Sea_QXblyMm0MQf75bvlQXkUJeAzqQw6NolA7TVFFpOkdIB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b422331f5.mp4?token=DO7gSDSqxld4RBhKd7ZgTZpFsQ7dPFurjKDX97jsqvB3krp2ZOolOMZ4s-GSB3zafXO0XIlB6pLPU5e8l62xtjD8XPlCth2NjYZ104BnHFOY3ivmFi614GQo-kiiy-5z6LVuLHTq_lMNVpo5hZSv_xmX_EuNPoDzVFGv98BbEnGWaH3dmpuJPvRM7E60GvVwSH8LNC3oR7zmw3PzpG6pG4Q0oQIoF17dvFO_elRRjY3dKSUGIb5fE5rOO9VnH_rTEKGIQ6v5hsWGqbjNqDBNrFwYRWhBVdCOzK332hp8N0tn9SWxzSaHnR3RVKiMkfXVQ5H2x53pJ41_RqR7VvoKoTl-vyy8pSV9OSZA4T-B8UNoggZ83mIwEsx8IkW71pUJX0hT-zOqG8DYHfhYXQ6gBwwmCHOAIh24VI7mn7AnQFA8Mg4h9oG-xYBGzevNQkKvlOxQAM1H7wr4TIW-86Pk__4xOFqmd_-83Z02sw4Ri2EBWkzGD7f5SBJ5mbHd1wniwBDcBCcMqoPIYBIy_FtpdDV6s-IxQ-oRD67CusV1uOqOZ3I4B0BCJJDqnCVZNOBZt0PymJVKeWB-slp6XZOvJfKFf3cpCDBikyVpjPfsJkWv6Xrm5HpCZh2Op7Sea_QXblyMm0MQf75bvlQXkUJeAzqQw6NolA7TVFFpOkdIB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعجز العبارات عن وصف هذا المشهد المهيب، حيث يجري تشييع قائد الأمة وإمهاما الشهيد آية الله العظمى السيد علي الخامنئي (رضوان الله عليه) في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/naya_foriraq/81173" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الدفاع المدني الإيراني:
لم يتم تسجيل أي حادثة حتى الآن في مراسم تشييع جثمان القائد الشهيد.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/naya_foriraq/81172" target="_blank">📅 11:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5eWGfwRqq_DJGKO3DCGWPwMHL8Rf3DHb84N5RRTknjDnxjt_z1hvbPpDBsioU3w8-9lT7tW1-xxaIGYPJgYmLgpDAeGC8_ViVVsLuiPaAhy_5qFPuEos8Ql3hAStx-kx2uTFMb_XXhxKp1fR4NDLOncNB_r5GnEGh7xM62Y1tdaFVvY5-F72f4w7Oq2Ifgch6aTFDJ-uw462XxncijwUZn634vk5GY--NK-4nmc4HvVQGd4RIqVsHBWn3ZwcuTNgUjySkrQajcow6DH2e9sV6Q6FVWMO_eE4SNL2EmZw8EtM6YK4CDeLtjLo5FAy0-erFaBm3PiPLut-6dWrAtrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
السيد مقتدى الصدر:
أهلاً وسهلاً بالوافدين الكرام إلى تشييع وتوديع الولي الشهيد شهيد الجهاد والإباء تغمده الله بواسع رحمته.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/81171" target="_blank">📅 11:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42524754b1.mp4?token=tiFFjTpmH9BHXM3jDKcvMpMpTQX9NSln0g0Qf_tG_RQ4CrWoOQDu_jePRRQqiNXh9ziphx9Y3prLWDKsbskI8MskckCAPNBaPG9SP9BkaHXB_hfQ6WUd9dc55gyH3liRC7FjgJkuux2k-whgKyt1fQJABU7SFUVqlWlSseiX3vei-rJ5Dnyqm-BNwUCNt_gcS4gRkxh3clqTH1xZPJOMR_JDouKtAerqs1ECZhucSqRBC6lQUUfytEQE0CIfqemuZzWzW02vJjs3R_fjLDScdoI38v-7DCW708k-D2wMEkAoawurwvhs15QBBTjkeTTWMR2hiblFvoAaXrJy1lpIMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42524754b1.mp4?token=tiFFjTpmH9BHXM3jDKcvMpMpTQX9NSln0g0Qf_tG_RQ4CrWoOQDu_jePRRQqiNXh9ziphx9Y3prLWDKsbskI8MskckCAPNBaPG9SP9BkaHXB_hfQ6WUd9dc55gyH3liRC7FjgJkuux2k-whgKyt1fQJABU7SFUVqlWlSseiX3vei-rJ5Dnyqm-BNwUCNt_gcS4gRkxh3clqTH1xZPJOMR_JDouKtAerqs1ECZhucSqRBC6lQUUfytEQE0CIfqemuZzWzW02vJjs3R_fjLDScdoI38v-7DCW708k-D2wMEkAoawurwvhs15QBBTjkeTTWMR2hiblFvoAaXrJy1lpIMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شعبٌ لايَترك ثأره.. سيدة إيرانية تعلن عن جائزة 20 مليون دولار لمن يقتل المجرم ترامب.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/naya_foriraq/81170" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvwAQfTsQdc_JdXcCvDKyoj115mfY-BrWp4pINLiAD6uk76zGj0iNeT0uCyxdBOHWXqq-9QfDQVM421gz-jUkLUzi9_yvXNWrZaRSnplglU0fvh7FpbD5ARfpNlYtODn9e_WF2i1Y_AqsmmK4wwHKg5LGJ7CyLrdAUoozIa7A4MiFhgKHSbQMC3DSaWnuGdjnS2Ss6nyphlM3zF7pihmo-Hxa0V5JpeR_JzTudnrZ86dZxO1gGk-ArMCmxAxq83hnTi1QZ09AWsLHU8OlaznqcyQzMu6o4gedzpzoENFsR-_7QMafGqS3KRMj38iTPcaPtHVzAs0s-UA1Vzis5VmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شعبٌ لايَترك ثأره..
سيدة إيرانية تعلن عن جائزة 20 مليون دولار لمن يقتل المجرم ترامب.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/naya_foriraq/81169" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vup6y6ghFYOcPsM6nYeuP4qC0YrzmSETbzdN4gbFbPu6NHXqPtcDhryRqnc5njRPMGuF2aT1089Ine6kKQIfEATk-GEqMMFVzZOGpsFIvUPopIJoevLxL4ss0FYFqAPibOypb5HztuBoOy3zLdijp7I1ICypbHtLLy6uaE4jHiiQ62zST8ZuXmxO3Uh22B7eqRlfa8oP1XQXNfZ1ps6O5UvGM0EC_Ah6yCLDdzShwBI3uq_4VGnZvGmzuf28vM4mGZMyXlOMujXW0T8uJpTOOW4UZxib0pePzaDC9HbWENbed70f0ZU5uOMH6du42mTs-oVZOAe05CkxubB7_ozWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
جينه نواسيها اليوم السادة.. أبناء العراق العظيم يشاركون في تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/81168" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭐️
إحراق أعلام أمريكا وبريطانيا والكيان الصهيوني من قبل المشيعين الغاضبين بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/81167" target="_blank">📅 10:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
🌟
مهاجمة صورة ترامب في العاصمة طهران من قبل المشيعين خلال تشييع القائد الشهيد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/naya_foriraq/81166" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d247494ec.mp4?token=TByIqNSldn65nHiV0xMCodG5-W2bJUxzg_MF4LhWOXTlbcyauQ8NnHG-WtD1CSzU8X9kjJ_rLVBnLa2M2DT3JRQ1zUYcRGOlukDoNpdlCLTG9DGLrw2sUhLfUNgAuiP_pGGq8Za5zV6SZVAJthXGVQ8qsQ74zNG8l4toxeocdi9PsbjmG5dYG9D-esjsSGBEKurVA_1pZ1TJvrKlE5mVh9M0HdvXnTTFKopriYTDBYKbeT88yOSTB_zRH3EtKemgymSKgn9ifa3nvAWbYzoI2XX5-pqzW0zu2aTe8NTengUUPM8trCz4Wbff-EKFlnsgxTQXijKiqXZmuviYX6plYqOZmKuqW7ImYS9_TAHMiM1o7VMdg-yybu9BJHmYer9rmKm7EzkIcWM6sAWGdJQ7Dv6I_8ai5RD74agIwSkoaM0dYL8dkeEvVSHs1zmJiRC-71GwNsBvGPo5VDO7O8bV0NvUgJH2DHMEAmf1H69JQ55itFmRPBB-awcu_FSzL20oa7icBLiXJzy7p56Oehll9Bs4Zza70t_XeHu8axOTG8yxQJRckxF2cDR5-E1H3zN__GTH550Syg_ZM-HT4J1qEW0W2QKl6x_sF_0wzRK3-851Pieh7S0lXTUDzMy9jTeChiluuWgwgkOAukYul1VkoEZP2SBfeIe5MU-UHwAgY8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d247494ec.mp4?token=TByIqNSldn65nHiV0xMCodG5-W2bJUxzg_MF4LhWOXTlbcyauQ8NnHG-WtD1CSzU8X9kjJ_rLVBnLa2M2DT3JRQ1zUYcRGOlukDoNpdlCLTG9DGLrw2sUhLfUNgAuiP_pGGq8Za5zV6SZVAJthXGVQ8qsQ74zNG8l4toxeocdi9PsbjmG5dYG9D-esjsSGBEKurVA_1pZ1TJvrKlE5mVh9M0HdvXnTTFKopriYTDBYKbeT88yOSTB_zRH3EtKemgymSKgn9ifa3nvAWbYzoI2XX5-pqzW0zu2aTe8NTengUUPM8trCz4Wbff-EKFlnsgxTQXijKiqXZmuviYX6plYqOZmKuqW7ImYS9_TAHMiM1o7VMdg-yybu9BJHmYer9rmKm7EzkIcWM6sAWGdJQ7Dv6I_8ai5RD74agIwSkoaM0dYL8dkeEvVSHs1zmJiRC-71GwNsBvGPo5VDO7O8bV0NvUgJH2DHMEAmf1H69JQ55itFmRPBB-awcu_FSzL20oa7icBLiXJzy7p56Oehll9Bs4Zza70t_XeHu8axOTG8yxQJRckxF2cDR5-E1H3zN__GTH550Syg_ZM-HT4J1qEW0W2QKl6x_sF_0wzRK3-851Pieh7S0lXTUDzMy9jTeChiluuWgwgkOAukYul1VkoEZP2SBfeIe5MU-UHwAgY8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اليمنيين يشاركون في مراسيم تشييع إمام الأمة بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/naya_foriraq/81165" target="_blank">📅 10:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180cd7b6ea.mp4?token=e41JP-pj-RX3OUvhJxLf9CDuIi4V57QEwEIFVeMcd9OikPB8OxwaGzlLafUDmER9uNwzyyG4z4U5tSrkhzHpF67MCoa2_h0Wu4Znv5g_Kbe7fAgvpWJeer6mlXIHQzYjLek78Q7jKYJEt6_9sQAO7fA0SY3xPkf6U8NyEwvK9_b1SGneSwcIRlb9_3IqTaVwK-ZS3YPsKvfbQMRLBdrSN6h0B_XRNoPDVj08ltUlkTikqx_4ME3Ui_RQ2aBCvGjbEYvD-DSQZz93TMxX6go4N5Un6P9P66CJGioY9834mvgxncNFLpHi6wISRo5oTMD3-nOQxq_u9S4cOjCC8S4EcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180cd7b6ea.mp4?token=e41JP-pj-RX3OUvhJxLf9CDuIi4V57QEwEIFVeMcd9OikPB8OxwaGzlLafUDmER9uNwzyyG4z4U5tSrkhzHpF67MCoa2_h0Wu4Znv5g_Kbe7fAgvpWJeer6mlXIHQzYjLek78Q7jKYJEt6_9sQAO7fA0SY3xPkf6U8NyEwvK9_b1SGneSwcIRlb9_3IqTaVwK-ZS3YPsKvfbQMRLBdrSN6h0B_XRNoPDVj08ltUlkTikqx_4ME3Ui_RQ2aBCvGjbEYvD-DSQZz93TMxX6go4N5Un6P9P66CJGioY9834mvgxncNFLpHi6wISRo5oTMD3-nOQxq_u9S4cOjCC8S4EcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
إزالة صورة المجرم ترامب.. غضب عارم في شوارع العاصمة الإيرانية طهران أثناء تشييع القائد الشهيد، مطالبين بالثأر والإنتقام من ترامب والمشاركين بجريمة إستشهاد الإمام الخامنئي.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/81164" target="_blank">📅 10:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0db34ce8d.mp4?token=ISR9ADFDEWUNeocR9ONCTYh2E8SLqKXJ0GZYpif9pefXTr3E2f2x-zimCQX8-00hJG9j1pvx3ZMLVyaFcCU6ApE2v6aHAyJnhhRjJfW9y8NzRPmD2oMAWZZ6i77sMwj8m5RHob3ijwJb_mrZAqcqC7Bj82VKCrcq9211GJQusM4hrBGKGqY9AZ0sN5LleZ_1DooLA0Zk90I-z8C8lv7eCblXUQRCdk--G3Z2ylD4hEc23ADLLUlzMG75ZJFfISR6hhzcLT3R2E0vI0i8K2you8GbnyG-0GZGZ5naXooh_ztmfkMIpB0T-idYpgT2TMQpDBlDFyzKlC2tIr66lQkT8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0db34ce8d.mp4?token=ISR9ADFDEWUNeocR9ONCTYh2E8SLqKXJ0GZYpif9pefXTr3E2f2x-zimCQX8-00hJG9j1pvx3ZMLVyaFcCU6ApE2v6aHAyJnhhRjJfW9y8NzRPmD2oMAWZZ6i77sMwj8m5RHob3ijwJb_mrZAqcqC7Bj82VKCrcq9211GJQusM4hrBGKGqY9AZ0sN5LleZ_1DooLA0Zk90I-z8C8lv7eCblXUQRCdk--G3Z2ylD4hEc23ADLLUlzMG75ZJFfISR6hhzcLT3R2E0vI0i8K2you8GbnyG-0GZGZ5naXooh_ztmfkMIpB0T-idYpgT2TMQpDBlDFyzKlC2tIr66lQkT8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
مهاجمة صورة ترامب في العاصمة طهران من قبل المشيعين خلال تشييع القائد الشهيد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/naya_foriraq/81163" target="_blank">📅 10:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b95403b3.mp4?token=p88NUeAIFOOjKAT9Tx_xmXa7i0TIYefO94VIh3ZErq1_MwEsifmz5XiQTvyyosN9Y5JfOIARxM-fxgrYHc2bXeg19BfHj6QzEjlm_YXFCgvb2g5pIIi_KoFDkE5jCSSOHI8Icbro3dUCVMDaltoohzEfp4xh7BDSTHuPHlx3nqW-XW7vmNcf1eTN1XNfuGeGC54yA5_avMKhbvZhHxl0-26ek4uuZwTYAKwaPTsCP511-FG6cgA91PNvut3NMmVfQXNsZdg1K7sJH7gZuq-CmyMNCuGkL7bKcFvqci4dMxpmjUuCedT3mWDCEVFiW42dvtkl2I9c_kCKpJtSILRLiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b95403b3.mp4?token=p88NUeAIFOOjKAT9Tx_xmXa7i0TIYefO94VIh3ZErq1_MwEsifmz5XiQTvyyosN9Y5JfOIARxM-fxgrYHc2bXeg19BfHj6QzEjlm_YXFCgvb2g5pIIi_KoFDkE5jCSSOHI8Icbro3dUCVMDaltoohzEfp4xh7BDSTHuPHlx3nqW-XW7vmNcf1eTN1XNfuGeGC54yA5_avMKhbvZhHxl0-26ek4uuZwTYAKwaPTsCP511-FG6cgA91PNvut3NMmVfQXNsZdg1K7sJH7gZuq-CmyMNCuGkL7bKcFvqci4dMxpmjUuCedT3mWDCEVFiW42dvtkl2I9c_kCKpJtSILRLiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
يالثارات الحسين.. بحر من المشيعين في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/naya_foriraq/81162" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abd840738.mp4?token=TMWnvIBjYgZds02rZGJqMmevXdVWPGbSeGGMv5j1I63CS5mo58-vidsEu3KBx6vcqm1OhshP5cf5DTKEXQsHi3ayCeOBWJ__SHOg8BAXdLpiEeTasneOw3XC_bLpoUH3TsocaYmmYClloW_-mm2yqhnCU1loTRoxxrI1X5iIvgv_JtS-6Z2Hv6XVxe23ymqJRabOpwrZu0seNU7R51QOnp2w9qSO76BmmarJEU6KN3BVeYQk8N24g-5P7Z5FS1lH5Qx8QU9FBjqcDbAimI8biAo_1UgURk2Lyt51a_KeSJoagSmwff7PvLKCil-tYU8ifoJVHlzqqDy83BA4WoKN4RkJcVO-05v1yzniGf2bR6MYbjLURCxvfCFSXG3-CsFM7NCfbWxEEOTDwtbhavIofn67kV08j0fmYuVQ2AePL6bYbI03Ou6X2Iy-KwdM_kv6JaBiuReH_4lmbh4jAr5zxvWY19yojq50IXlfIYKIs0S0RNttZz9TUEm7rqKBZaLKmREg9_Akral25ZajrGklmxCJPzI27phRySa5KcQPDhPCQU2T8O5MJUnyfS_as5FEplJoK_rTM-nikjD_wI0DPf-8XSTFoDH1Dvu1dxwTS2EUYslmO07TEZgIBHMceYZJbl7y9ut93uTgDDp6OwWCPWXONbpNkLh1Jo_0GTYqFkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abd840738.mp4?token=TMWnvIBjYgZds02rZGJqMmevXdVWPGbSeGGMv5j1I63CS5mo58-vidsEu3KBx6vcqm1OhshP5cf5DTKEXQsHi3ayCeOBWJ__SHOg8BAXdLpiEeTasneOw3XC_bLpoUH3TsocaYmmYClloW_-mm2yqhnCU1loTRoxxrI1X5iIvgv_JtS-6Z2Hv6XVxe23ymqJRabOpwrZu0seNU7R51QOnp2w9qSO76BmmarJEU6KN3BVeYQk8N24g-5P7Z5FS1lH5Qx8QU9FBjqcDbAimI8biAo_1UgURk2Lyt51a_KeSJoagSmwff7PvLKCil-tYU8ifoJVHlzqqDy83BA4WoKN4RkJcVO-05v1yzniGf2bR6MYbjLURCxvfCFSXG3-CsFM7NCfbWxEEOTDwtbhavIofn67kV08j0fmYuVQ2AePL6bYbI03Ou6X2Iy-KwdM_kv6JaBiuReH_4lmbh4jAr5zxvWY19yojq50IXlfIYKIs0S0RNttZz9TUEm7rqKBZaLKmREg9_Akral25ZajrGklmxCJPzI27phRySa5KcQPDhPCQU2T8O5MJUnyfS_as5FEplJoK_rTM-nikjD_wI0DPf-8XSTFoDH1Dvu1dxwTS2EUYslmO07TEZgIBHMceYZJbl7y9ut93uTgDDp6OwWCPWXONbpNkLh1Jo_0GTYqFkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لافتة كبيرة تحمل عبارة "سنقتل ترامب" باللغتين الفارسية والإنجليزية خلال تشييع القائد الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/naya_foriraq/81161" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd3ecf504.mp4?token=nrZV8CITA1kLmg55jvc1RcCik9-UV-u5vnKEL-8Uzap0feJ1kOa02uqRtPBXGqpm4uds92mB8xgllvwpmrIJ7kB1LaCaohYpjutURyug5piXpnI38NLyMbqXtcqP4UjsO7idiimWHLXzM0Xem4jKGZTv8E-ekBSvGsneeT85x0bhU_6fn57N_7lKiFtxGukHPQo33kG8AZvMHZeqj6jx0nQvcxzW5fljVzEYoh22pKNeQdSflKcUtCvuKuaB3i7-k47hXWEZEJcGt02wGMIivLLmulQxZ3pIj9iuMonO5LWI0R6_m9k0AtNVaq1PQdTszMVo-EI73dV8znJR74h8ORlKF5FOfrEy9Xz-IMB2OwUlu1Wjg6V2axCKy0n5rYB60H9g17qlotSYg2QZSqqAvJprz8QlavcpU4Hfeo_uHnet203iyJyuFBk-OKugxCOf6SdPL-vqObyGJS9s5mUMoRyGMlSo0z3p7kaAo5x_mmbDPxlBTmmlLFDx2xf8fhs41StmcNwHsPDiUTREvYcfSea4-Z01AkxzJ9mahxRUW5AyzgpLZShFdmqg2KKlSRysae88ojzQV2kNNQiRKSaE9S5tu9CCtDZ28vpZr-Bz1oefgpVdvlTyUp3Ioxncz0i50Rgyx8DtdVaMWPHjc01qORmk63QLhbp-dlJD5kkuo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd3ecf504.mp4?token=nrZV8CITA1kLmg55jvc1RcCik9-UV-u5vnKEL-8Uzap0feJ1kOa02uqRtPBXGqpm4uds92mB8xgllvwpmrIJ7kB1LaCaohYpjutURyug5piXpnI38NLyMbqXtcqP4UjsO7idiimWHLXzM0Xem4jKGZTv8E-ekBSvGsneeT85x0bhU_6fn57N_7lKiFtxGukHPQo33kG8AZvMHZeqj6jx0nQvcxzW5fljVzEYoh22pKNeQdSflKcUtCvuKuaB3i7-k47hXWEZEJcGt02wGMIivLLmulQxZ3pIj9iuMonO5LWI0R6_m9k0AtNVaq1PQdTszMVo-EI73dV8znJR74h8ORlKF5FOfrEy9Xz-IMB2OwUlu1Wjg6V2axCKy0n5rYB60H9g17qlotSYg2QZSqqAvJprz8QlavcpU4Hfeo_uHnet203iyJyuFBk-OKugxCOf6SdPL-vqObyGJS9s5mUMoRyGMlSo0z3p7kaAo5x_mmbDPxlBTmmlLFDx2xf8fhs41StmcNwHsPDiUTREvYcfSea4-Z01AkxzJ9mahxRUW5AyzgpLZShFdmqg2KKlSRysae88ojzQV2kNNQiRKSaE9S5tu9CCtDZ28vpZr-Bz1oefgpVdvlTyUp3Ioxncz0i50Rgyx8DtdVaMWPHjc01qORmk63QLhbp-dlJD5kkuo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
جموع المشيعين يحيطون بالمركبة التي تحمل الجثامين الطاهرة المتجهة نحو ساحة الحرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/naya_foriraq/81160" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c809f5d37b.mp4?token=bKQdL5diwIgbLc8Lur25OcPLX9s6t-aTV_IPwS7N0Az5oddcCfKasxi09R00bZVeVPT9ZZXkC6TxmdpkdMDF6aiB4eeEt_kz3tbToT2MIKAbcZz6JGjlv-wXXCAKSfuo08y1aOB5xXtJKY2w3XRPTXOaMmIknh8d8YcpbCgxLMTNjbFm1XdKCdezWdkwj98TOv5_pZyuHqANa3_-aPoxfy0MMMhqGxWH7WyoffFsw8n5QMkVvMhnfvmFCks4Dgzj0ePz0-b85jvp5W-ZtXLb5fo795i3EXUS9vUFR7OuW_TlxV4eYg7KGDXbW69R8IeaVe76MBiosyWIF3DjZXzql6L7uB1A-JSfv36iZrJwmg-2j3XkacX6Q6-Quj-VeaBcSrcfJKnOhqMlgYoIzJ56lHXdi9n65FAJv10oJRvLP6H0m7wW4ABI23X9I4LiZUYa8O3ojqre8V5gEQe1kZtc26xKm_ZhbSgPibnulpkHIXV318OmeWZf8vYSyBc2UnLL1F6b6o97pUPeuTb5zpPz968WNSv-n63mn0pRJXwYlOscKjZjss5s3Vo9CjYvR2w1qcZN4oGQUWlut9ZMSjP7ISmD4RzaNDlWAxpzLFHZG4-nio9zRuAJy6kQ00v7b4NexGIuqHJlfjbCKivzbIOvhIeqRSdCpKvjlfGIeu4dp50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c809f5d37b.mp4?token=bKQdL5diwIgbLc8Lur25OcPLX9s6t-aTV_IPwS7N0Az5oddcCfKasxi09R00bZVeVPT9ZZXkC6TxmdpkdMDF6aiB4eeEt_kz3tbToT2MIKAbcZz6JGjlv-wXXCAKSfuo08y1aOB5xXtJKY2w3XRPTXOaMmIknh8d8YcpbCgxLMTNjbFm1XdKCdezWdkwj98TOv5_pZyuHqANa3_-aPoxfy0MMMhqGxWH7WyoffFsw8n5QMkVvMhnfvmFCks4Dgzj0ePz0-b85jvp5W-ZtXLb5fo795i3EXUS9vUFR7OuW_TlxV4eYg7KGDXbW69R8IeaVe76MBiosyWIF3DjZXzql6L7uB1A-JSfv36iZrJwmg-2j3XkacX6Q6-Quj-VeaBcSrcfJKnOhqMlgYoIzJ56lHXdi9n65FAJv10oJRvLP6H0m7wW4ABI23X9I4LiZUYa8O3ojqre8V5gEQe1kZtc26xKm_ZhbSgPibnulpkHIXV318OmeWZf8vYSyBc2UnLL1F6b6o97pUPeuTb5zpPz968WNSv-n63mn0pRJXwYlOscKjZjss5s3Vo9CjYvR2w1qcZN4oGQUWlut9ZMSjP7ISmD4RzaNDlWAxpzLFHZG4-nio9zRuAJy6kQ00v7b4NexGIuqHJlfjbCKivzbIOvhIeqRSdCpKvjlfGIeu4dp50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الحشود المليونية التي خرجت للمشاركة في تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/naya_foriraq/81159" target="_blank">📅 09:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02d27f89c.mp4?token=il8rwsAOAV-dQC-VE8puU02lmLCcJCdobwvxx8hi-5xzeGLZcMZdXctY3DrKExw-wkMGeWJbremZ3nIKsP3GkdaPLTrW8F2sidk0taksTD3lYE-iW19GeptpZZWRbPRP54bNmuFbIxMT6pFpEpk22XAfEA2ct490IBNRQaaMmBkH0LT_zwW9usSyOa8SlbWvlEJjCe5h9Ba46frjaBGhf26LqEzWk5a4MqYwVl1FA0Klhw135bnsyXzcTuPjnc4x-RUBJDjGvMyOW8wSHoXmyDGYxr_wpulxsONcsMdd35fiyz2eX7pdTgXm3oSBOzlYfoxjF9r4UYY4IjrtxBNo37DcDNKXT-oVnw6FIPjC2lkJB6FKduW2G7mtx02eASlGfvgPgxJURUmLxVt_OEGimue4hzgf2am9c5Vyz7igSEcYnnNzeSPp7Kc9g8MWXZPmjAV6t5yk3TkkP1g2Y1RgK5tmpqP-0KQQD1xCuiF4E4aIRheO3PkhEhR4j4pdA3zuNk18ni1pvnjq1PSRx9vqKydrRem-7PGVXh3TW5gCpAmd2oP6c2ysKOrUTwLBHR8LBT-692cdVxgwaCDPuM2-KEYNZBQuZYZvvaUUHrOe8hKPzFYvI1uKHlziF8MqUEmWme4_TFURngRW8RS1CPTFj3op3fgoq43HVyAXyX_w0iI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02d27f89c.mp4?token=il8rwsAOAV-dQC-VE8puU02lmLCcJCdobwvxx8hi-5xzeGLZcMZdXctY3DrKExw-wkMGeWJbremZ3nIKsP3GkdaPLTrW8F2sidk0taksTD3lYE-iW19GeptpZZWRbPRP54bNmuFbIxMT6pFpEpk22XAfEA2ct490IBNRQaaMmBkH0LT_zwW9usSyOa8SlbWvlEJjCe5h9Ba46frjaBGhf26LqEzWk5a4MqYwVl1FA0Klhw135bnsyXzcTuPjnc4x-RUBJDjGvMyOW8wSHoXmyDGYxr_wpulxsONcsMdd35fiyz2eX7pdTgXm3oSBOzlYfoxjF9r4UYY4IjrtxBNo37DcDNKXT-oVnw6FIPjC2lkJB6FKduW2G7mtx02eASlGfvgPgxJURUmLxVt_OEGimue4hzgf2am9c5Vyz7igSEcYnnNzeSPp7Kc9g8MWXZPmjAV6t5yk3TkkP1g2Y1RgK5tmpqP-0KQQD1xCuiF4E4aIRheO3PkhEhR4j4pdA3zuNk18ni1pvnjq1PSRx9vqKydrRem-7PGVXh3TW5gCpAmd2oP6c2ysKOrUTwLBHR8LBT-692cdVxgwaCDPuM2-KEYNZBQuZYZvvaUUHrOe8hKPzFYvI1uKHlziF8MqUEmWme4_TFURngRW8RS1CPTFj3op3fgoq43HVyAXyX_w0iI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الحشود المليونية التي خرجت للمشاركة في تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/naya_foriraq/81158" target="_blank">📅 09:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed80a1b5c.mp4?token=UB4VfJNdtP60H-sINc7F7RNMIP6ki9ekSYvsN42VNQtH436kYvsvK95Opn3oJDeEmahk8c8JXgzXQX8Xj8YTH8hp3ADX6-leX3m12klQv_19Ng8tDvjNolBhOKpBrsvQMSRQX9xtqt7VqS7KRcy7FXr8ULrRhJBMIqc4T2t96jUXkcsvp4Ui8tV79_XtqtykqXmxpXxY3SfrVy5J6sfuYj7IYC9aeGBdQ6UjwpnMKaID2Z7AqQG_aLXubhRrZzYmm0YLsH5y77r6iGRgRJ90BptUe2kMnzB0H8cpjApkqR9d5nP7duaNCIjP0H4LS3ukL_yF3XodhGBP301ycUHeDXnZ3iwQT9ZIIj2g66boxanngIsq6_zC7Oht1TSTSNBPMITffhOEExdvKFcPfkxtnyh1s_eJTQxcgoBPbBFOf3dPf9aNdnYtEjXFcLDUkfQWSP4AEsBThkM70-wWH2RQ_FHiS1rjKT1sqizuqZb9fwaoUZzacXK7yHerRPWS-orRcHRo_F2s6mWdm3zJahJHO7vwv63nwXhXdrYVp4ILbBavwOm8pDJKtZeIkTcP5kTFzYdk2I2nW_h5HjXdupWbkiTHbgmbLr4Zyc_idP5kQgIS99OaMp-Ln1GB_9GcMKm8AyxTZU2l79oC7c3TZ2AEwRyPWGQUfC9xgg8e9NocBFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed80a1b5c.mp4?token=UB4VfJNdtP60H-sINc7F7RNMIP6ki9ekSYvsN42VNQtH436kYvsvK95Opn3oJDeEmahk8c8JXgzXQX8Xj8YTH8hp3ADX6-leX3m12klQv_19Ng8tDvjNolBhOKpBrsvQMSRQX9xtqt7VqS7KRcy7FXr8ULrRhJBMIqc4T2t96jUXkcsvp4Ui8tV79_XtqtykqXmxpXxY3SfrVy5J6sfuYj7IYC9aeGBdQ6UjwpnMKaID2Z7AqQG_aLXubhRrZzYmm0YLsH5y77r6iGRgRJ90BptUe2kMnzB0H8cpjApkqR9d5nP7duaNCIjP0H4LS3ukL_yF3XodhGBP301ycUHeDXnZ3iwQT9ZIIj2g66boxanngIsq6_zC7Oht1TSTSNBPMITffhOEExdvKFcPfkxtnyh1s_eJTQxcgoBPbBFOf3dPf9aNdnYtEjXFcLDUkfQWSP4AEsBThkM70-wWH2RQ_FHiS1rjKT1sqizuqZb9fwaoUZzacXK7yHerRPWS-orRcHRo_F2s6mWdm3zJahJHO7vwv63nwXhXdrYVp4ILbBavwOm8pDJKtZeIkTcP5kTFzYdk2I2nW_h5HjXdupWbkiTHbgmbLr4Zyc_idP5kQgIS99OaMp-Ln1GB_9GcMKm8AyxTZU2l79oC7c3TZ2AEwRyPWGQUfC9xgg8e9NocBFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وسط أجواء حزينة.. تسير العجلة التي تحمل الجثامين الطاهرة، نحو ساحة الثورة بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/81155" target="_blank">📅 08:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13427680a.mp4?token=XanDo2v4l1SyCoRs2_BObca6bWqymBDpT1SzG7xMqIdYohb5qzZ59ybvPouDjGlMLKdOvIxvsY13T-UL3iDRgKTy8_nXH5mqj9HRu2fJ8otZyMsZk39iyt0iM8iINyjvGOMN8IcSkdsm-TEWGh85lt1tFBmjtcSGrAaq-nqfLJC357wdse4r2wG0a-Nu7Qlk96Sid6Y9_BDrRwDravx9yur1aTC3n9jpbiQ4q6bEkTc4-QNzAnNc1a53uxwpXeaPdkeGRMZPOkiLT2ydxfrvOoM4N9Knm0Q59FD9dM24lCXjuY0E25DsQ7eqfHPZio_uVLyeXgD_DK9m6z9l-_13uDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13427680a.mp4?token=XanDo2v4l1SyCoRs2_BObca6bWqymBDpT1SzG7xMqIdYohb5qzZ59ybvPouDjGlMLKdOvIxvsY13T-UL3iDRgKTy8_nXH5mqj9HRu2fJ8otZyMsZk39iyt0iM8iINyjvGOMN8IcSkdsm-TEWGh85lt1tFBmjtcSGrAaq-nqfLJC357wdse4r2wG0a-Nu7Qlk96Sid6Y9_BDrRwDravx9yur1aTC3n9jpbiQ4q6bEkTc4-QNzAnNc1a53uxwpXeaPdkeGRMZPOkiLT2ydxfrvOoM4N9Knm0Q59FD9dM24lCXjuY0E25DsQ7eqfHPZio_uVLyeXgD_DK9m6z9l-_13uDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/81154" target="_blank">📅 08:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbmBB0QK7eMkt55qH9Rujz9Tuov0fEKdH0yUkhz3-sd89tYqI5YeMjXitLudVlrYDe0rqlKnZLM8Shmo-Atg6JUxf9VTqxoxokTx-ZaWmJlhEHtMOYlL0qXzkRsVCoQSI5Iw1vRJUbS605P3o8GeIlPcvf1SNpzYWiNDDgm2LXgOpnS2JzETHlLf4j1Paf8c-wnKEu1x9MOs7CGL0FtNS2lgwvTaltGKLjgEj2-oIBBJ1Tqhb5WB-g3Jae3pS4QGhXkNceOOqyhtIYAlyIViqAfPqzK2JY-ICUGu5ygZClHtVh3ibcP_cP4Jz8zI2puBlUEo4zqUzAZzSW589svN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/81153" target="_blank">📅 08:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6616f0efeb.mp4?token=SGaxxyOhk5epNHGvDh1qQQQuZenHZMYp8RRf-LPmjw8dqJ1Cr9pA8YlAnIwklQQ8LWp0qW34FOf-aO8CcKJMH21Sh5JXhubHA9UIJxxVsf57ybVM9PsAjY4CKG99nyGOJ26SHFKJf_KpAlW91JQlnyOOWhTmsC9TlcxxTiIrpcFfa7usH9gJevsfPx6laK4Sxo04IVxxQl6evVTyQb1flxj48aqbweEOsw4Pga4-fBZ8egbkow9deMyhl5p-DKYrCLkuYoIKKVybrPgvUjE1aJ5eXYN1vaJTlyHE3CttJuNVU7KNqI3KnE5Cd5EdHLgCx7X6Mfv3VOgd-sKtwdSMcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6616f0efeb.mp4?token=SGaxxyOhk5epNHGvDh1qQQQuZenHZMYp8RRf-LPmjw8dqJ1Cr9pA8YlAnIwklQQ8LWp0qW34FOf-aO8CcKJMH21Sh5JXhubHA9UIJxxVsf57ybVM9PsAjY4CKG99nyGOJ26SHFKJf_KpAlW91JQlnyOOWhTmsC9TlcxxTiIrpcFfa7usH9gJevsfPx6laK4Sxo04IVxxQl6evVTyQb1flxj48aqbweEOsw4Pga4-fBZ8egbkow9deMyhl5p-DKYrCLkuYoIKKVybrPgvUjE1aJ5eXYN1vaJTlyHE3CttJuNVU7KNqI3KnE5Cd5EdHLgCx7X6Mfv3VOgd-sKtwdSMcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/81152" target="_blank">📅 08:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7081ef9.mp4?token=FvncyP4gu3OtBAEbrxj20Bd0jpOFHDbWHU33Z-wgCF8aqKNoyYimKVxh9G-dUg1kzI6A7e9qdNf4MnIFbAh2Qmabgye4Qvif1V47uAHxAa2pZ40mQ8Cz5DF8I5tMtc-CTUFRHMBG5f5ZXJkzAtxiy14ZVJ9igidkChyaVxVeMd7YyEuBxh2globvaHtkQo5c7InlrhcGQTnbbS3fFki1QXP-WMxj0uiMH3deMgITwHihQjTBilT1HMIySnyGMfQgv174pwz8R2nzkIuCnVHp-fk-0jGagPPh1LeRIh5iufWw_ItX60iVrTRE0xILIuEu8YA97D43snXnmjRzdNNgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7081ef9.mp4?token=FvncyP4gu3OtBAEbrxj20Bd0jpOFHDbWHU33Z-wgCF8aqKNoyYimKVxh9G-dUg1kzI6A7e9qdNf4MnIFbAh2Qmabgye4Qvif1V47uAHxAa2pZ40mQ8Cz5DF8I5tMtc-CTUFRHMBG5f5ZXJkzAtxiy14ZVJ9igidkChyaVxVeMd7YyEuBxh2globvaHtkQo5c7InlrhcGQTnbbS3fFki1QXP-WMxj0uiMH3deMgITwHihQjTBilT1HMIySnyGMfQgv174pwz8R2nzkIuCnVHp-fk-0jGagPPh1LeRIh5iufWw_ItX60iVrTRE0xILIuEu8YA97D43snXnmjRzdNNgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همه آمده‌اند، با پرچم سرخ انتقام.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/81151" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22423dd0b.mp4?token=Q_yR3P2xtTaAq07xIZ1B1o1-UXc3Wav7zdogp8__KefLJIlk8tyT36vA6DlHUCkvOqT7RYSCKXv-pDggb0ysDMefNBULn5G7WEbmRPOFBfCICWCUXHzwgBPPqlho65VqMmInkDCGBs_yzNf3wBbsdK77GBWCeyc_alRwtDmBUC5erF3LuLI1U55Br0i4k9G57eVs8rsH_UNzTv9rKIpRVzgQCzgouYF3rr6bXUjQrBq0ChVKoNpGM54-C8mRVD5ua7H50IuIu31Lq3osempAZEGiGWkbRNrBy3kB-gO1mpoOdJyAXZ7ccAue0cBFdQqAw0fXQfP-VdBjLWvi-7LfqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22423dd0b.mp4?token=Q_yR3P2xtTaAq07xIZ1B1o1-UXc3Wav7zdogp8__KefLJIlk8tyT36vA6DlHUCkvOqT7RYSCKXv-pDggb0ysDMefNBULn5G7WEbmRPOFBfCICWCUXHzwgBPPqlho65VqMmInkDCGBs_yzNf3wBbsdK77GBWCeyc_alRwtDmBUC5erF3LuLI1U55Br0i4k9G57eVs8rsH_UNzTv9rKIpRVzgQCzgouYF3rr6bXUjQrBq0ChVKoNpGM54-C8mRVD5ua7H50IuIu31Lq3osempAZEGiGWkbRNrBy3kB-gO1mpoOdJyAXZ7ccAue0cBFdQqAw0fXQfP-VdBjLWvi-7LfqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحشود المليونية تنتظر وصول الجثمان الطاهر للشهيد القائد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/81150" target="_blank">📅 06:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-lSAwcuLFxIBxY5bOcwZgjO4ARWH1kxhRoY1My_dFFOaK9cfdaFLbL9kskT2dvzoSxSMx_avarVysaqyV3B9JXiqdSduryzygvW1zkF_RJOWWxgrEo4_WhpMo6tvcBq-TSU_7ei88aZmWdpXaiJhHCG9nxQoUd_-IJo44A54PnILM3xjp6nhaUOJYjmd0B_I9oiq6sT4OTtt4NjTcMznMNREWTVNeDfN8Z3i8nqMAU56OHfzziGTfdS88ZhHKcDiw3YljFK6KIYEcfzh0RSNJNvoqbruwTz6fMUjl2Gt3lDIVAbSC-6tZ4w9AGJZwikxdrIMvsAvh3cCU4EyKb9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
سنقتل ترامب..
الشعب الإيراني ثأراً للإمام الشهيد، يتعهد بالقصاص والإنتقام من المجرم ترامب.</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/81149" target="_blank">📅 06:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy-c3cI5a45HI3bMI0_ycwixgDQ5l5RhW8-FKtqU1OHmUTcY-cOcyDSfxCrN3xx5rhlbBqLhCPgZrKzltFVmbSYciu-BaRMS9uQOpcpYoTJg3JGcoVD2t9Uu_bO8kyv7H5Sh1m-VnmFNXkCepnHiww5XFs21CnaGABchaN_h6TI7FayRPxD47ZzO6zemtGUiUud2FCm2kGf0N2SZVdXvIY8beo2pKT36YNDQ9e2-dOqvvZk2Tn-nGIDfQxnDJx0L1P7nkEEtbd8BblkA7lDMy9cQhRpktjnENw7ctBir_cL9DLQb42c1jG9-v2Gtwc5N5VOMvN39z1MhWWhqyM0V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحشود المليونية تنتظر وصول الجثمان الطاهر للشهيد القائد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/naya_foriraq/81148" target="_blank">📅 06:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d52e5f01.mp4?token=IBkRnqZRjbU8GxXIRX1b3aNugx8mHgAJTeX7nPGAI7bSr-j3b0V-mLdH2p93AGVaXBNHYPJ_k6uflgekmRBuc0GlvOoSJmB9yvIfbQsYLXdCVeWdLUETFTuF2hO15Vp-nHrRMvTnl_pSap6G6z9e4pZz78nhkQOMn_vupRmCrsQmz3Xj1WeFqAM0IxCZrNXpcBWHYoPJyR9rjAf4qQXiTRPliSVUkePgZWZbl_g6Y0SS46OLRIhi4B1RG93QcA5mh5fm27zf8DsRdaLZ53AsXqEKGfJ8nmFEOTzN6nPH_iuGMq8UoYVJ_wAwKrOYnNKuvNS7sCsE2u_CAd-6S-QdKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d52e5f01.mp4?token=IBkRnqZRjbU8GxXIRX1b3aNugx8mHgAJTeX7nPGAI7bSr-j3b0V-mLdH2p93AGVaXBNHYPJ_k6uflgekmRBuc0GlvOoSJmB9yvIfbQsYLXdCVeWdLUETFTuF2hO15Vp-nHrRMvTnl_pSap6G6z9e4pZz78nhkQOMn_vupRmCrsQmz3Xj1WeFqAM0IxCZrNXpcBWHYoPJyR9rjAf4qQXiTRPliSVUkePgZWZbl_g6Y0SS46OLRIhi4B1RG93QcA5mh5fm27zf8DsRdaLZ53AsXqEKGfJ8nmFEOTzN6nPH_iuGMq8UoYVJ_wAwKrOYnNKuvNS7sCsE2u_CAd-6S-QdKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أبناء العراق يشاركون في مراسيم تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/81146" target="_blank">📅 06:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1119c62728.mp4?token=Ir3K0xaVWAHF4rAA6anrpi40IeQyWYLZnrFbPQRkOQ9yoyJANQIDreAX4ixaPUBVdUYz1jEYSy4y9sL81IIf2l5FpkCs4sHmKSki1XohaxwB0irsSCIw0mSTTx-6onOXJ9DTnhdeT2tPgg4ipgS6dm4EGA5JCGdolZHyfgi3CLmqG-U0SW9SbYv5Rvbra2AejtBKWS33NxGEOk7sPokmfWMDC94SCkT9Fw_jisMPCC8eUMdu3XHVogwvXLn15OSGfpgW6WrXRaSvU8ktIr-elsKhQBZGqnwvwit7-U5l3Bztap25L3a4iJtYD48OvAgZp_mUOHrNWW8Jq7sm1qDy_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1119c62728.mp4?token=Ir3K0xaVWAHF4rAA6anrpi40IeQyWYLZnrFbPQRkOQ9yoyJANQIDreAX4ixaPUBVdUYz1jEYSy4y9sL81IIf2l5FpkCs4sHmKSki1XohaxwB0irsSCIw0mSTTx-6onOXJ9DTnhdeT2tPgg4ipgS6dm4EGA5JCGdolZHyfgi3CLmqG-U0SW9SbYv5Rvbra2AejtBKWS33NxGEOk7sPokmfWMDC94SCkT9Fw_jisMPCC8eUMdu3XHVogwvXLn15OSGfpgW6WrXRaSvU8ktIr-elsKhQBZGqnwvwit7-U5l3Bztap25L3a4iJtYD48OvAgZp_mUOHrNWW8Jq7sm1qDy_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بدء مراسم تشييع جثمان الإمام الشهيد بشكل رسمي في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/81145" target="_blank">📅 06:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
بدء مراسم تشييع جثمان الإمام الشهيد بشكل رسمي في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/81144" target="_blank">📅 06:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae73531a85.mp4?token=XdLkCc5ER7hpsXrFL8OvXNAbJ_QaIgFFeK0IcKDdkfaLvph5-uXw4bEAhKtK6WqtFtIl0tB-zVOqXFpU9B4ymPFfX8_XMPVD48OFTcozoSIlwne6W6KEKzXIOeK4gV7d_1WTsbm1lk7F87PxkfqBiJgiebrRlxg1MuLZMPpAqu7r62VbR0f0fmGBjkjf8KmlQOABNQegRBJl39hYZXBuGQ4T5OuKkCBGk8wXcdh9pWUgLtgQ-0sxpQsNFb3bWTAgF9ZTq5K3N2w27cSnNdF9UjeqZa4Lne1UCpbIYdYipTfkAqIWP2SwaNj5KFmnudkY6PWh9sGRA9OKYFjD28OrUqb1uXQhWVYVjcQxLF4UwTGaMcWw9ilqJSdzGepxtDXtOmq_nurLimct2eURkRm3AYupE3ccbis9jat8mxE38C8HyHzn5EwgpoObtluhujNxVYzNkwMZJvIYP-9hqihNCge5vZSBjsLGNeNi25dgw9ge-aJiMwc6YlwTHcXZgF-zAbUkjAjBZ07OJFz5uyIVtxvgKfcs5HznOcrxKLSD3OSb4w81alk_vVPKFRVF7OpNUFfPU6okIdK5SQUZ4OJ_gceF8LJLB9Zjt7x6XOJ4_3e63qZP_SLbXoEq6PeGX_bTsZUtZj4HJL5ncKi6Ve_2Dl8XNRucFPYPVmLdQgSw1Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae73531a85.mp4?token=XdLkCc5ER7hpsXrFL8OvXNAbJ_QaIgFFeK0IcKDdkfaLvph5-uXw4bEAhKtK6WqtFtIl0tB-zVOqXFpU9B4ymPFfX8_XMPVD48OFTcozoSIlwne6W6KEKzXIOeK4gV7d_1WTsbm1lk7F87PxkfqBiJgiebrRlxg1MuLZMPpAqu7r62VbR0f0fmGBjkjf8KmlQOABNQegRBJl39hYZXBuGQ4T5OuKkCBGk8wXcdh9pWUgLtgQ-0sxpQsNFb3bWTAgF9ZTq5K3N2w27cSnNdF9UjeqZa4Lne1UCpbIYdYipTfkAqIWP2SwaNj5KFmnudkY6PWh9sGRA9OKYFjD28OrUqb1uXQhWVYVjcQxLF4UwTGaMcWw9ilqJSdzGepxtDXtOmq_nurLimct2eURkRm3AYupE3ccbis9jat8mxE38C8HyHzn5EwgpoObtluhujNxVYzNkwMZJvIYP-9hqihNCge5vZSBjsLGNeNi25dgw9ge-aJiMwc6YlwTHcXZgF-zAbUkjAjBZ07OJFz5uyIVtxvgKfcs5HznOcrxKLSD3OSb4w81alk_vVPKFRVF7OpNUFfPU6okIdK5SQUZ4OJ_gceF8LJLB9Zjt7x6XOJ4_3e63qZP_SLbXoEq6PeGX_bTsZUtZj4HJL5ncKi6Ve_2Dl8XNRucFPYPVmLdQgSw1Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بدء الزحف المليوني في العاصمة الإيرانية طهران للمشاركة في مراسيم تشييع الإمام الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/81142" target="_blank">📅 05:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb1cf7016.mp4?token=JodKAG6rdMkz4N3j4N5lw-wnVUMQWma_GWwIg4Drc3LbTqVBkzP_KkTPWaR7nkZ1J8iCelYOcapoAfvylFKw1KgQqogyDLYev0nLtXSyFW1OOvE6_pE0iQu3u8XdnTerRRVk2vo5pbfn4_QtJDtEls356HQfht2VTn8L6lyBREUUvV138Sv-4iqzsszYxno74aVSYNyHA5P03q9fKGs_G58jJLisb6aO2mJXxI3s9xzauswOp1ki0q1D2hKJxgEDF9ITPzxhH9keWHGZMf8sYupfO8Eb_FSzTjuePIEURt-33rRaOoVlBePVhcjDE24Ui4VMnizR0OQ-TlJFWP68K4ODG6ei41v5qZpHYBFsBASVbwAygAVPwggUUyXbCRJOVtn_edcd-Keg1q5u8THkxkT5NRptziuGuG2VCm3jeS_EEM1an4ZSrjDO_pPZqydqMHAJ_EMfHDteaXa68ZKLbMXzAIZvsL2ygYRRj9_TUI0Ziw6EpHPZ15vp_Gw7YG6cntoydkWulQ_SwVvp8Wc1IBn7V2mn4MUI7VassJWSHaaNNcpmf1KFvwRGtNY_lRTDB3AkBLP6DKNKoMOxHUEagRBhrSBlZGB3AV28o9wfhUG01R8PGk4RocfBkrSndnzPNcVKYmgaU0ZMw0cD3i7iJ1YUiWEINa61DUpjzikwMBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb1cf7016.mp4?token=JodKAG6rdMkz4N3j4N5lw-wnVUMQWma_GWwIg4Drc3LbTqVBkzP_KkTPWaR7nkZ1J8iCelYOcapoAfvylFKw1KgQqogyDLYev0nLtXSyFW1OOvE6_pE0iQu3u8XdnTerRRVk2vo5pbfn4_QtJDtEls356HQfht2VTn8L6lyBREUUvV138Sv-4iqzsszYxno74aVSYNyHA5P03q9fKGs_G58jJLisb6aO2mJXxI3s9xzauswOp1ki0q1D2hKJxgEDF9ITPzxhH9keWHGZMf8sYupfO8Eb_FSzTjuePIEURt-33rRaOoVlBePVhcjDE24Ui4VMnizR0OQ-TlJFWP68K4ODG6ei41v5qZpHYBFsBASVbwAygAVPwggUUyXbCRJOVtn_edcd-Keg1q5u8THkxkT5NRptziuGuG2VCm3jeS_EEM1an4ZSrjDO_pPZqydqMHAJ_EMfHDteaXa68ZKLbMXzAIZvsL2ygYRRj9_TUI0Ziw6EpHPZ15vp_Gw7YG6cntoydkWulQ_SwVvp8Wc1IBn7V2mn4MUI7VassJWSHaaNNcpmf1KFvwRGtNY_lRTDB3AkBLP6DKNKoMOxHUEagRBhrSBlZGB3AV28o9wfhUG01R8PGk4RocfBkrSndnzPNcVKYmgaU0ZMw0cD3i7iJ1YUiWEINa61DUpjzikwMBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أبناء البحرين المظلومين الغيارى الشجعان، يقيمون تشييع رمزي لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه) رغم التهديد والتضييق من قبل عصابات آل خليفة المتصهينة.</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/81141" target="_blank">📅 05:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
‏دوي انفجارات عنيفة في كييف وتفعيل الإنذار.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81140" target="_blank">📅 02:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81139">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
تنويه صادر عن اللجنة الإعلامية الخاصة بمراسم تشييع آية الله العظمى السيد الشهيد علي الحسيني الخامنئي (قدس سره)
تودّ اللجنة الإعلامية إعلام السادة الإعلاميين بأن توزيع الهويات الخاصة بالتغطية الإعلامية للمراسم سيتم من خلال مركزين معتمدين:
* المركز الأول: العتبة العلوية المقدسة – النجف الأشرف.
* المركز الثاني: العتبة العباسية المقدسة – كربلاء المقدسة.
وسيبدأ توزيع الهويات اعتبارًا من يوم غد، ابتداءً من الساعة 12:00 ظهرًا، لذا نرجو من الجميع أخذ ذلك بعين الاعتبار.
شاكرين تعاونكم.
#المديرية_العامة_للإعلام</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81139" target="_blank">📅 00:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0193183dd9.mp4?token=VMpKpwAi7nHw54IcZGqD64bWh0XKZdKIYIazCKBTJ8J7bNofoM2_l3zBac8v1GAIF17bQOgqacz45YJqHQlszetHOo9DLzaAhEtCtApgGljAkfmLwivB5MYGfngeGTpxB2FLRdWw5A2QUi_3iAhL-UwwYLSL21Hnee3-vCr7W-USRuBNhmOy66Rr7yfWyQmmw_Wx0a607_1qADC3DBQd1sWqDBtOtgrQtx2hz6bFVQPj68gpUY8HFQwELQFFRPz-Ak0A5KZL6hdXqiFgp-2c025_VLAeMWjkWcHEbppKBEAHppUzPmXLB111qGSRrFgkJnCQMftI_sqx876-jLQ5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0193183dd9.mp4?token=VMpKpwAi7nHw54IcZGqD64bWh0XKZdKIYIazCKBTJ8J7bNofoM2_l3zBac8v1GAIF17bQOgqacz45YJqHQlszetHOo9DLzaAhEtCtApgGljAkfmLwivB5MYGfngeGTpxB2FLRdWw5A2QUi_3iAhL-UwwYLSL21Hnee3-vCr7W-USRuBNhmOy66Rr7yfWyQmmw_Wx0a607_1qADC3DBQd1sWqDBtOtgrQtx2hz6bFVQPj68gpUY8HFQwELQFFRPz-Ak0A5KZL6hdXqiFgp-2c025_VLAeMWjkWcHEbppKBEAHppUzPmXLB111qGSRrFgkJnCQMftI_sqx876-jLQ5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إرسال مدرعات عديدة برفقة الطيران المروحي إلى قرية غاردا راش في محافظة أربيل شمال العراق استعداداً لبدء المواجهة في تمام الساعة 8 مساءً.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/81137" target="_blank">📅 23:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3defccdf92.mp4?token=RSq-LeGilNZh-0U2zFbBBHbQKlYKDE9iuVYX44iyxpXQalwa2Si0CAXJocNAQd7Mvvs7UlAYJaLcwY1MYYM2ffDKoG-yWtDMCMeQey26dTIyIl4zVQoqCdcfeYHbQpjb6k9MWkAUSG6MFOtSxIDI0cTa4R93IqyVWoEXyPNrhEPRbyv7PrFi-3h9A9-Y9aYMORIQoCdZG5Cceio6r0-COfjWpK5fbhF-IUf0eBvz-0xHev05aRy1ze6VHwknGmT79bDQEh4QPBms_EYSV1Q5L8CItV4khqlYp8aH_I_POmIQrTwyxQ-DdTjLQ9uiiH9reV0G5IzxWDrONGzFRcfr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3defccdf92.mp4?token=RSq-LeGilNZh-0U2zFbBBHbQKlYKDE9iuVYX44iyxpXQalwa2Si0CAXJocNAQd7Mvvs7UlAYJaLcwY1MYYM2ffDKoG-yWtDMCMeQey26dTIyIl4zVQoqCdcfeYHbQpjb6k9MWkAUSG6MFOtSxIDI0cTa4R93IqyVWoEXyPNrhEPRbyv7PrFi-3h9A9-Y9aYMORIQoCdZG5Cceio6r0-COfjWpK5fbhF-IUf0eBvz-0xHev05aRy1ze6VHwknGmT79bDQEh4QPBms_EYSV1Q5L8CItV4khqlYp8aH_I_POmIQrTwyxQ-DdTjLQ9uiiH9reV0G5IzxWDrONGzFRcfr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في ظل انشغال الجولاني بإثارة الجدل حول تدخله لقتال حزب الله في لبنان دفاعاً عن إسرائيل ؛ جيش الاحتلال الإسرائيلي ينشر مشاهد لعبور مستوطنين صهاينة إلى محافظة درعا التي تعتبر واقعة تحت سيطرة حكومة الجولاني.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/81136" target="_blank">📅 23:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
انتهاء مراسم التوديع للشهيد الأممي السيد علي خامنئي وأفرادٌ من عائلته في طهران</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/81135" target="_blank">📅 22:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📰
‏بلومبيرغ عن تقييمات عسكرية غربية: التهديد في مضيق هرمز لا يزال كبيرا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/81134" target="_blank">📅 22:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇸🇾
دوي انفجارات في مدينة أريحا بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/81133" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇸🇾
دوي انفجارات في مدينة أريحا بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/81132" target="_blank">📅 22:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f8442434.mp4?token=IO6SXaNS_uxEPMPDz0ABKgxI9E6R3QtQ4O1WPIwefB-v8igNul9U5dwdWvPB7Mha6-LxA_ZAO-L1hElTkNrlFp01hsD_7fVFGRUqqSyp_io5vDpmLZbEJhQj1Fe6AL66PRh1OpsjcNiNsK3_pr9-Bt54I9HyueBVijZ1TlL1YFmTRDT7-LqEn0iNTw9TY64fUc6W_cuXhlI_l1Vz6zEUN3Z1RUql8mUHtvphzfJrlpvg6D_bqP2SjypMbHv8vyLzt-wffbx6QFJ44knkbgng27nvQb1fcw9DVo_7GB9cLrE400sumhGPuGTZqfJK3lOvUszv-PYo_w6AFDS9ljcb-LJdR6OzLFxeDIUB613XUNZOqhKB-Tv61OfEDS0T1TIcRp8UV5Q-KnG9JfWAkNx8w-cstnAUDmycjJjE2GofAtpOskCMiQbBVu8HCR2jIjmT2e2xDW6aWyhOOUejaO2YES2PsF_V1TheNV6gM3LwftxViHCRFmXoSQ1QmikUHXQrtLZ1jZlFJ-QaZiJIaiCMlD07c5Jy3o771eyYphd39Ni5MyQB3D6RShptw7xaagmTDMOh3FyXg1FYoCfS2D7Rp_hGiyE24sp2ZMl6kooibP069MXf7h5ZvCFGkhVFep0t9Qd4HWEOXxanXDuAW4vgvDV8qlLkhLLnkmoz2O8t0i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f8442434.mp4?token=IO6SXaNS_uxEPMPDz0ABKgxI9E6R3QtQ4O1WPIwefB-v8igNul9U5dwdWvPB7Mha6-LxA_ZAO-L1hElTkNrlFp01hsD_7fVFGRUqqSyp_io5vDpmLZbEJhQj1Fe6AL66PRh1OpsjcNiNsK3_pr9-Bt54I9HyueBVijZ1TlL1YFmTRDT7-LqEn0iNTw9TY64fUc6W_cuXhlI_l1Vz6zEUN3Z1RUql8mUHtvphzfJrlpvg6D_bqP2SjypMbHv8vyLzt-wffbx6QFJ44knkbgng27nvQb1fcw9DVo_7GB9cLrE400sumhGPuGTZqfJK3lOvUszv-PYo_w6AFDS9ljcb-LJdR6OzLFxeDIUB613XUNZOqhKB-Tv61OfEDS0T1TIcRp8UV5Q-KnG9JfWAkNx8w-cstnAUDmycjJjE2GofAtpOskCMiQbBVu8HCR2jIjmT2e2xDW6aWyhOOUejaO2YES2PsF_V1TheNV6gM3LwftxViHCRFmXoSQ1QmikUHXQrtLZ1jZlFJ-QaZiJIaiCMlD07c5Jy3o771eyYphd39Ni5MyQB3D6RShptw7xaagmTDMOh3FyXg1FYoCfS2D7Rp_hGiyE24sp2ZMl6kooibP069MXf7h5ZvCFGkhVFep0t9Qd4HWEOXxanXDuAW4vgvDV8qlLkhLLnkmoz2O8t0i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إجلاء 11 عاملاً كانوا محاصرين داخل المجمع التجاري الذي التهمته النيران في شارع الظلال وسط العاصمة بغداد ولا تزال النيران مشتعلة وممتدة إلى الأبنية المجاورة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81131" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
قائد عمليات الفرات الأوسط في الحشد الشعبي اللواء علي الحمداني يعلن استكمال الاستعدادات الأمنية والخدمية الخاصة بمراسم تشييع شهيد الامة السيد علي الخامنئي (قدس سره)</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81130" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd87060b8.mp4?token=PROcDdYfQPEoBUBGt9r9liyM2FRVuSi1DK4x1HjpEi-tW-5QgE1FcjR-KRi-WVKmTWU0BBkIAs-HspSrwTXD3K1vhaPZK_ffxsnOBFCmNIprkAIuwelK2yk87mkRX4hJLZyIAHh9s0uDGGEnfhDHbZcASRPK9o3EpoX90V_oqJnCot6ovS5JubK2EZ5mbcGt0bfQWVjGNqCv9fPeDjfuspO-Aonfd3D4tOo7LuJlTlGWSJKbGuB5xQ9Sf9XRHHFqAjkouzY_UOjMpjON1y3DEe495RqZEgm5lhl4CnTXwJzY2sTqPKhve9_Lq-oH52KqosdjWqBhtKDuonr58EqhshiR3N-u4CxgpzAOoSdiesLfIaSjUrzfjBd6YFS_xgw_e0uufrygoN4GZJVA-aoAmKLR7R_R_XYa_flZc-tjE_mOoRagyIXmEfuqsGwoNt77a5Id4-GMfgkZrEdkeJ5Abvfr4U_qh7KIg9xEadFQ4pfX1r0WV176THz0-9MY1iku_6E2qx61gtGj4-FsT6qjjw8WGtB5-Z5agzfecUrRm34WdVRruSyDBW6yGDns73z3dzWJhC6F4LVK8YQIBs9-PtfXe8cCQqhchpdG31LQ6-xyO3w05wED_JithyC0uK2GKrBaqwiFk0E_QuwcD_y1uINQAjOJYo-jykIl6XJmUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd87060b8.mp4?token=PROcDdYfQPEoBUBGt9r9liyM2FRVuSi1DK4x1HjpEi-tW-5QgE1FcjR-KRi-WVKmTWU0BBkIAs-HspSrwTXD3K1vhaPZK_ffxsnOBFCmNIprkAIuwelK2yk87mkRX4hJLZyIAHh9s0uDGGEnfhDHbZcASRPK9o3EpoX90V_oqJnCot6ovS5JubK2EZ5mbcGt0bfQWVjGNqCv9fPeDjfuspO-Aonfd3D4tOo7LuJlTlGWSJKbGuB5xQ9Sf9XRHHFqAjkouzY_UOjMpjON1y3DEe495RqZEgm5lhl4CnTXwJzY2sTqPKhve9_Lq-oH52KqosdjWqBhtKDuonr58EqhshiR3N-u4CxgpzAOoSdiesLfIaSjUrzfjBd6YFS_xgw_e0uufrygoN4GZJVA-aoAmKLR7R_R_XYa_flZc-tjE_mOoRagyIXmEfuqsGwoNt77a5Id4-GMfgkZrEdkeJ5Abvfr4U_qh7KIg9xEadFQ4pfX1r0WV176THz0-9MY1iku_6E2qx61gtGj4-FsT6qjjw8WGtB5-Z5agzfecUrRm34WdVRruSyDBW6yGDns73z3dzWJhC6F4LVK8YQIBs9-PtfXe8cCQqhchpdG31LQ6-xyO3w05wED_JithyC0uK2GKrBaqwiFk0E_QuwcD_y1uINQAjOJYo-jykIl6XJmUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أهالي درعا جنوب سوريا يعلنون تشكيل حركة ردع الاحتلال بسبب الاعتداءات المتكررة عليهم من قبل جيش الاحتلال وصمت الجولاني المتكرر وتجاهله لما يحدث من احتلال للأراضي السورية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81129" target="_blank">📅 22:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي تنشر قوموا لله يا أبناء العراق المشهود.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81128" target="_blank">📅 22:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3dd24b03.mp4?token=qxVXJk94FPoUbltYaaDaQ_kCZwp0r0R_RdJcDCD8UTRiS2MqIymvH9ZT1ofpBFCGLnROVc6sHobH1nBvtQ1TMy5ysRvpRTDZhc3e1eWnm8CUvK6PQad4vGrGcrq90zXyeM6tdyOMc_3HvMXG1gXsC8QMgLjMzTFGGr2zdRMKBPmC0NHbPJOYRaevTwc1kW8l8LkcRxiGmmcpPkRhdL4t1OFdEgIOOf-ID-R7WwawDB3aZnqOwlVFf_HBLJ5tUap7JSLyo3BYWp8m4X98Dmjhq8LR0JY6a7JIoOE1e0G7c4wX_zTjFXQ85622RGGUoCQdPx7CRg3qRd7dbXF8fwodQ1oU-yKveCYmJl5Y_evYtTJYJNyO6fdrkWVaW-alkNbiRymIObupz4O-8V9OYe01UJSRfjluDomVGFggbPG0zOkl8_KHxB-E8oajqUzN5p3EazSIAhVDbSR8xCA2TU76uJ5n6N0OP746OWL9U0GOMiwkwjVUpPna4Ra6RcV2aE9Kfgc3ob959j62GtgW-qQr0uRnOvgMV2T_62ABt_wSV97nU4czZN9ktIOukx0Sy8tFrIUlwLt5umDCR3jEyfvL2O4XAugi53kxEBkXj1P0ZP-4tw1XJhyfFpUbm0sPzPq4Zr0fZ78gO_7YS_NUZy2dKjAT6PGynGiu1KLml2bVixc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3dd24b03.mp4?token=qxVXJk94FPoUbltYaaDaQ_kCZwp0r0R_RdJcDCD8UTRiS2MqIymvH9ZT1ofpBFCGLnROVc6sHobH1nBvtQ1TMy5ysRvpRTDZhc3e1eWnm8CUvK6PQad4vGrGcrq90zXyeM6tdyOMc_3HvMXG1gXsC8QMgLjMzTFGGr2zdRMKBPmC0NHbPJOYRaevTwc1kW8l8LkcRxiGmmcpPkRhdL4t1OFdEgIOOf-ID-R7WwawDB3aZnqOwlVFf_HBLJ5tUap7JSLyo3BYWp8m4X98Dmjhq8LR0JY6a7JIoOE1e0G7c4wX_zTjFXQ85622RGGUoCQdPx7CRg3qRd7dbXF8fwodQ1oU-yKveCYmJl5Y_evYtTJYJNyO6fdrkWVaW-alkNbiRymIObupz4O-8V9OYe01UJSRfjluDomVGFggbPG0zOkl8_KHxB-E8oajqUzN5p3EazSIAhVDbSR8xCA2TU76uJ5n6N0OP746OWL9U0GOMiwkwjVUpPna4Ra6RcV2aE9Kfgc3ob959j62GtgW-qQr0uRnOvgMV2T_62ABt_wSV97nU4czZN9ktIOukx0Sy8tFrIUlwLt5umDCR3jEyfvL2O4XAugi53kxEBkXj1P0ZP-4tw1XJhyfFpUbm0sPzPq4Zr0fZ78gO_7YS_NUZy2dKjAT6PGynGiu1KLml2bVixc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇵
أجرت جمهورية كوريا الديمقراطية الشعبية العظمى اختبارًا لإطلاق 12 صاروخًا كروز طويل المدى قادرًا على حمل رؤوس نووية بشكل متتابع من إحدى مدمراتها الجديدة من فئة Choe Hyon - وهي أول مدمرات حديثة موجهة بالصواريخ في البحرية الكورية ؛</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81126" target="_blank">📅 21:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d8b18868.mp4?token=E2iJJdhdwFANjCOpIMn_Z2AQfVHI9KZr2mQpTmMciH0MkvLZnl8f4tyytKomHR1d3KKPetqndrH2FM_qOM1G4_iDay3xy87FIOZPW7zUIvlFqwkmaUgmcPIRzUTsHj_UQxaD-iAAq0OwShH7Tc5rkErR3beYZ0y1C-GBMfhZA0VBa_wGq53weqVlGjjNgOVNEy2E9n6m0kPI3UNdHY5ZkxLQjKDFxfUIm_-PAHNsdZqYCwBVb5wMKmWlcFPRKxB0eA8KDT7uV8aGGDhDHLEZsoJH9AlVMCDen2gCqzJC3eK3Z9mbD5jrXfUaasWAElUS4-_YJl5jS9AU99VUY1DoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d8b18868.mp4?token=E2iJJdhdwFANjCOpIMn_Z2AQfVHI9KZr2mQpTmMciH0MkvLZnl8f4tyytKomHR1d3KKPetqndrH2FM_qOM1G4_iDay3xy87FIOZPW7zUIvlFqwkmaUgmcPIRzUTsHj_UQxaD-iAAq0OwShH7Tc5rkErR3beYZ0y1C-GBMfhZA0VBa_wGq53weqVlGjjNgOVNEy2E9n6m0kPI3UNdHY5ZkxLQjKDFxfUIm_-PAHNsdZqYCwBVb5wMKmWlcFPRKxB0eA8KDT7uV8aGGDhDHLEZsoJH9AlVMCDen2gCqzJC3eK3Z9mbD5jrXfUaasWAElUS4-_YJl5jS9AU99VUY1DoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع اشتباك عنيفة بين حراس أحد أعضاء مجلس محافظة كركوك عن فصيل الجبهة التركمانية وحراس مستشفى وطن بمحافظة كركوك ؛ ما أسفر عن إصابة اثنين من حراس المستشفى بجروح خطيرة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81125" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d7f0de29.mp4?token=J3XOdCNWoH1ivTBG6bketNaBnC4ZuSjGcyGcUESHByVsFjLWalpoGzvQbrsk_2qLKl62hMawJRnn0sQbSWPb-DUnpYHqz8wfZ-qlFA0WPvgi_CMMEYHStJ__1jMXkfJkapYGj-2l60aAHrFU5fbNQC1IwkkgSxlBtzGEg2uouoNIkM5kPtyRskVmEjW7JatLuvyjSkSC9oqdG4ljy6gIEnhMnJveY4R7OTpOAkwJ7Q9OKxD7M1WUFxtG8caGJ2KMcEDVRmPi6FxhQWq1YTujTzgvwAsQkHrNDNZPdrpwQ3-TJeyLLIxxo4vrGTtDT-cfGHgFomv-KmpuuGORmHPc5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d7f0de29.mp4?token=J3XOdCNWoH1ivTBG6bketNaBnC4ZuSjGcyGcUESHByVsFjLWalpoGzvQbrsk_2qLKl62hMawJRnn0sQbSWPb-DUnpYHqz8wfZ-qlFA0WPvgi_CMMEYHStJ__1jMXkfJkapYGj-2l60aAHrFU5fbNQC1IwkkgSxlBtzGEg2uouoNIkM5kPtyRskVmEjW7JatLuvyjSkSC9oqdG4ljy6gIEnhMnJveY4R7OTpOAkwJ7Q9OKxD7M1WUFxtG8caGJ2KMcEDVRmPi6FxhQWq1YTujTzgvwAsQkHrNDNZPdrpwQ3-TJeyLLIxxo4vrGTtDT-cfGHgFomv-KmpuuGORmHPc5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أقدم عاصمة في التاريخ تتحول لساحة معركة بعد سيطرة نظام الجولاني الذي كانت أبرز صفاته الإرهاب والفوضى حيث شهدت ساحة المرجة في دمشق اشتباكات بين مسلحي إدلب وقرباط دير الزور إثر خلافات داخلية بين عصابات الجولاني.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81124" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4285da2f6b.mp4?token=netIwDspYtAEuivNoZq3ItROykbsHuFAVm8kFLIBtQK5X3m9K8rW3cMYZXqOi8irH9eCO2qRi__79Ea0CR3hEvqUNaGuIP8liNOL6p4kQngZXHeD0pyCMt50nOhTP19WhHRfeiGH94Y0W6eXfNgsMez4ZFnLOvP49sPPeEh2-RlRkAAxSNaU0-0Yuh4Own_cB0IXUAMj5WBWAYd5G7tahQ57h2P6j5gDyK_thuaqS6mdCv8lk92E0JnioHD2q8gaRwXK0ZJejOoHzyR0T_0Yog1quCv8ErAVV999qOscQEZw7BTz_eq4EF9crqnFhc9Gip-EdJUFBN7x6bZgjb2XKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4285da2f6b.mp4?token=netIwDspYtAEuivNoZq3ItROykbsHuFAVm8kFLIBtQK5X3m9K8rW3cMYZXqOi8irH9eCO2qRi__79Ea0CR3hEvqUNaGuIP8liNOL6p4kQngZXHeD0pyCMt50nOhTP19WhHRfeiGH94Y0W6eXfNgsMez4ZFnLOvP49sPPeEh2-RlRkAAxSNaU0-0Yuh4Own_cB0IXUAMj5WBWAYd5G7tahQ57h2P6j5gDyK_thuaqS6mdCv8lk92E0JnioHD2q8gaRwXK0ZJejOoHzyR0T_0Yog1quCv8ErAVV999qOscQEZw7BTz_eq4EF9crqnFhc9Gip-EdJUFBN7x6bZgjb2XKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا طهران حيث رايات كتائب حزب الله تشارك في الوداع الاخير
مشاركة واهتمام واسع من قبل الحكومة الإيرانية بوفد التشكيل العراقي الأكثر ايلاما على الاحتلال الأمريكي في حرب رمضان</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81123" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f731e28c.mp4?token=H7KbnrIsptv86LEMJeP4LgbRXvL-phdSDBqnXOLMSXyLaDHH8kuDkROklpZ2C7FPw8-BpRm8SLFA7q0WxntpYE3cChl_FClaNuUyr2MtpYb9eZfMjF-af-sVSAzNRgph9YguciPQP1oVHIuxxFlxlc6grjzDrSQ24FZzlJnBYWnln-13mVswpcnqUGbYMkqEHY85vZSGFQ6nLMXKcdP83rKHEhrh1hwLVktLj31Fl9mGNfYXVEivHkKMZHhQ9twtX49W0DZrKJuIvyZJhfqMYhWJG1U241bUH72irEid3JDzcZWAPvkV7TsA0XNxxv9VvyATgAY0Gn29n_VSWzIPJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f731e28c.mp4?token=H7KbnrIsptv86LEMJeP4LgbRXvL-phdSDBqnXOLMSXyLaDHH8kuDkROklpZ2C7FPw8-BpRm8SLFA7q0WxntpYE3cChl_FClaNuUyr2MtpYb9eZfMjF-af-sVSAzNRgph9YguciPQP1oVHIuxxFlxlc6grjzDrSQ24FZzlJnBYWnln-13mVswpcnqUGbYMkqEHY85vZSGFQ6nLMXKcdP83rKHEhrh1hwLVktLj31Fl9mGNfYXVEivHkKMZHhQ9twtX49W0DZrKJuIvyZJhfqMYhWJG1U241bUH72irEid3JDzcZWAPvkV7TsA0XNxxv9VvyATgAY0Gn29n_VSWzIPJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إجلاء 11 عاملاً كانوا محاصرين داخل المجمع التجاري الذي التهمته النيران في شارع الظلال وسط العاصمة بغداد ولا تزال النيران مشتعلة وممتدة إلى الأبنية المجاورة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81122" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700c45fc9e.mp4?token=D77kkTNuaPyPNoIhCyOyO3rRuGckS6wZH7m_yOVrlXlRqNP9xPO_xJjNGnCqCRKMkuecQljofNrBcdTKVO5vs7mw2mWWQq8C3EF0iWOeytIgpAa9BCXUYzAV2Ec-LchJuys5aaAXmmFI2_KpqHC0_MA2ha2m1G7VmEaSBzCkhHDch9LS3IMObnusaLpN-NwWcgUNvXoT-X-Kb_MVp7kSHLHftWnY-NZyLP5MQBVTiWxzr0JhyxF9ikoiclxAxXSxeBZ29Rz1kLXv5xa8J1ndJ0jfeFZUcF25V0boBJiAbvoZRnjz19R2MXVSF---dk-2J6unSvMX6QWgfE4okZ9SRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700c45fc9e.mp4?token=D77kkTNuaPyPNoIhCyOyO3rRuGckS6wZH7m_yOVrlXlRqNP9xPO_xJjNGnCqCRKMkuecQljofNrBcdTKVO5vs7mw2mWWQq8C3EF0iWOeytIgpAa9BCXUYzAV2Ec-LchJuys5aaAXmmFI2_KpqHC0_MA2ha2m1G7VmEaSBzCkhHDch9LS3IMObnusaLpN-NwWcgUNvXoT-X-Kb_MVp7kSHLHftWnY-NZyLP5MQBVTiWxzr0JhyxF9ikoiclxAxXSxeBZ29Rz1kLXv5xa8J1ndJ0jfeFZUcF25V0boBJiAbvoZRnjz19R2MXVSF---dk-2J6unSvMX6QWgfE4okZ9SRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلم ابو حسين
الرايات الصفراء الراية الأقرب لقلب الحاج سليماني والسيد الولي تشارك بالتشيع الرسمي في الوداع الاخير</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81121" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-text">كلمة الامين العام لكتائب سيد الشهداء الحاج ابو الاء الولائي (دام عزه) في رسالة الى الشعب العراقي العظيم.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81120" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVPoCo9UtZJHQrH_PE_Tt3L6fE86eI4k6WYY3mF4iZ0cOAL-AbnbtRSE8kErjOxOOd4nZJQboRqnlgs1C0O84igvs48Cv_1I7V44yeZFqDUCTHlBu7TqMeKTqsyazI3csyNVVtOQL02keeKk_afph_yGFMuBcR4_G9wuUgKkpp-Jt4rvySuVpp9JPvmuXfadz6BRThJxkJFt-wZl9fEgLS96ViAX1fuz8KsTcGgsYw3PdND5iHUHCtPUHKpzsKb7tebFsnLF6Q48WpldgJ67AWTlX7ticrcyv-BEXHVaO-ef__oagI1zAouiUDdqttGM12mtFwWJRtJodx7TqTpJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: شكرًا لك FIFA على فعل ما هو صحيح، وإلغاء ظلم كبير!
علماً أن الـ FIFA قد ألغت البطاقة الحمراء لمهاجم المنتخب الأمريكي ورفعت الإيقاف عنه قبل مباراته المقبلة في المونديال!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81119" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77100992bb.mp4?token=JU1Q_Ktuahk2r0NFlgo8GmOspRXxjisIBRA_RGA5OoaAxUpGAW-chsle1r83fhA0zwwofv7ordBDq7Etp8wvhOQNhgNe-G30WzoTzV6HKB58JCsloFcgCq7KdxPqvJhKrRSVnj3iiyXiMTQyoisJ5UCQhEiXGjnznT9Xr7L_eLdZFKpY56omibYXaDI54CtgSSkWlY9kiHuOaPMNwoI5TID9SWDhzbAPBec69vCrxFJXQYhqkUUtEFTfkJE7Fg0tBFEh7DB1EXfpqIWADs4Yn5PrttjQ_FY5GChghSutkY8-BZ7ZahneetBCOOXQaI9NcpVeb1JRxS1fuuKshUSruBCwpykcR6WHNZUybivQkRm5Iv-XErr9dorB8w3XE-sL5XZKbElN09RZAL4X8zXgA7jawQEhhdmsPusvCTcKpC4n7OCRqpxZsBvKXqe9djGcpiJIN-5ArPP4puhZXu62yjdZ4eemg36idLHGWQgXTEqfPUuMYM5BZykxBokTUw5mIeHJpBn2Tf_gx_fVXFiy23yimMzAYejctKyMyS4iUOIdaAFWX5HI3dmaZmipu0qLNoZvrsdkjCiJWRg62SRw-le9HKDUZ8xam2z3PtzcVVi6O6M-TP2SH8ixN7NfcPdhxYXyZ8uU-GWoWgIwvU4UWCfSKUOJWc2EOIfDFBr0XDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77100992bb.mp4?token=JU1Q_Ktuahk2r0NFlgo8GmOspRXxjisIBRA_RGA5OoaAxUpGAW-chsle1r83fhA0zwwofv7ordBDq7Etp8wvhOQNhgNe-G30WzoTzV6HKB58JCsloFcgCq7KdxPqvJhKrRSVnj3iiyXiMTQyoisJ5UCQhEiXGjnznT9Xr7L_eLdZFKpY56omibYXaDI54CtgSSkWlY9kiHuOaPMNwoI5TID9SWDhzbAPBec69vCrxFJXQYhqkUUtEFTfkJE7Fg0tBFEh7DB1EXfpqIWADs4Yn5PrttjQ_FY5GChghSutkY8-BZ7ZahneetBCOOXQaI9NcpVeb1JRxS1fuuKshUSruBCwpykcR6WHNZUybivQkRm5Iv-XErr9dorB8w3XE-sL5XZKbElN09RZAL4X8zXgA7jawQEhhdmsPusvCTcKpC4n7OCRqpxZsBvKXqe9djGcpiJIN-5ArPP4puhZXu62yjdZ4eemg36idLHGWQgXTEqfPUuMYM5BZykxBokTUw5mIeHJpBn2Tf_gx_fVXFiy23yimMzAYejctKyMyS4iUOIdaAFWX5HI3dmaZmipu0qLNoZvrsdkjCiJWRg62SRw-le9HKDUZ8xam2z3PtzcVVi6O6M-TP2SH8ixN7NfcPdhxYXyZ8uU-GWoWgIwvU4UWCfSKUOJWc2EOIfDFBr0XDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أنباء عن محاصرة عدد من العمال داخل المبنى المحترق وسط محاولات كبيرة للدفاع المدني لإخراجهم.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81118" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏البيت الأبيض: ترمب سيلتقي الجولاني على هامش قمة الناتو</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81117" target="_blank">📅 20:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6de9f8037.mp4?token=gxOMPUPNzBMjSPXU4Qh8Vw3eJpVRe-ReYT7Mo_rFdXnXMVmB08G__np6kllPeWyaqHvmVXvEK11kJOtjSFB40c1b7HTkpbksvfUHUHIRQwx5qCVsv0DNKid6b9P5fenQTdM6_SvaBBKDIN43ihPa-1QirmJDmARr8F05wtUejgivvxJAOn9V-e0_hZhYnbjL9RBzfWNkrZG204Q41cqhqAZtrMfrCfV7Qdd2cknNH3O5u_MB0R9KYDJDLcjwGQRxdZM-0OP9XwhQsK8mjNtJNyvXHmK6_dF3UczMrCYubwAeiMqI0VCjrahBpHbv7ySuMxuUCOwq82KAWBxN6h-DAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6de9f8037.mp4?token=gxOMPUPNzBMjSPXU4Qh8Vw3eJpVRe-ReYT7Mo_rFdXnXMVmB08G__np6kllPeWyaqHvmVXvEK11kJOtjSFB40c1b7HTkpbksvfUHUHIRQwx5qCVsv0DNKid6b9P5fenQTdM6_SvaBBKDIN43ihPa-1QirmJDmARr8F05wtUejgivvxJAOn9V-e0_hZhYnbjL9RBzfWNkrZG204Q41cqhqAZtrMfrCfV7Qdd2cknNH3O5u_MB0R9KYDJDLcjwGQRxdZM-0OP9XwhQsK8mjNtJNyvXHmK6_dF3UczMrCYubwAeiMqI0VCjrahBpHbv7ySuMxuUCOwq82KAWBxN6h-DAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحريق يمتد ليشمل الأبنية المجاورة للمجمع التجاري في العاصمة بغداد والبدء بإجلاء السكان من منازلهم.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81116" target="_blank">📅 20:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af75ae984.mp4?token=AJhRAVZt7wClKmpC0__0rHsdPCIQvza2_4FirEcyqypp6Ce8wDEk2S3V9ProPMTUcMB9h4FhWEIKWbaJTJTUjQswTDfIoCZ3VpCCRp3kGQZrLVomNLDbWcXBZxUeAX_9t8-gEFB8A_CrXBqf02sGUzcgUePXdOX4qNo0_4SGawmKOtbIqYSbXVO_dkJBXq4Qd2Vi2K9RlDKUR3nG2OWN_zhNHJB8YH1QPQZIO4zCF6EL_VYrmhOmPuyd6m4KbYxYESiKGbDfXVM5E_-ofGtO8HVVAdxzQfZZcVY2sMBjzy2o4noSrPjOSVmrWaW3Xu-2t21nYYREuDEPrPaq-omQpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af75ae984.mp4?token=AJhRAVZt7wClKmpC0__0rHsdPCIQvza2_4FirEcyqypp6Ce8wDEk2S3V9ProPMTUcMB9h4FhWEIKWbaJTJTUjQswTDfIoCZ3VpCCRp3kGQZrLVomNLDbWcXBZxUeAX_9t8-gEFB8A_CrXBqf02sGUzcgUePXdOX4qNo0_4SGawmKOtbIqYSbXVO_dkJBXq4Qd2Vi2K9RlDKUR3nG2OWN_zhNHJB8YH1QPQZIO4zCF6EL_VYrmhOmPuyd6m4KbYxYESiKGbDfXVM5E_-ofGtO8HVVAdxzQfZZcVY2sMBjzy2o4noSrPjOSVmrWaW3Xu-2t21nYYREuDEPrPaq-omQpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق شارع الظلال في العاصمة بغداد يخرج عن سيطرة الدفاع المدني ومخاوف كبيرة من انتشار الحريق إلى المنازل المجاورة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81115" target="_blank">📅 20:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95438bf709.mp4?token=Yc8Jfl33zGoxeoNsqFRFe1Jj8FXTjr42qdDc2pwHRyFESC4zQ2gtLvNOC7hXw3f78U6F_v_MQhlv1rGIrWU4SGa-xtIjy8ReRdkSmLaOWwwes_FG-OQS2-ZTsxxmeyKW8tB-wrLtBCwXXAC0QpAH28tFpYVFexg6HdtwWdit33JQ13uqLqLTi8d44_SP1N6YNsOwUB9IDFnaKaTof66Ivor0s-aUyp2kaGH851yKWQDlaaUbIMnnjZHVllHtr9_ylJdHt7Va3PuNe2NaFiFU0V0cpevshHBQJzhwRCob9AZT49sF1ztHc1FCJhXQyv0fm51sA4ITgsZMlrX5gBNp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95438bf709.mp4?token=Yc8Jfl33zGoxeoNsqFRFe1Jj8FXTjr42qdDc2pwHRyFESC4zQ2gtLvNOC7hXw3f78U6F_v_MQhlv1rGIrWU4SGa-xtIjy8ReRdkSmLaOWwwes_FG-OQS2-ZTsxxmeyKW8tB-wrLtBCwXXAC0QpAH28tFpYVFexg6HdtwWdit33JQ13uqLqLTi8d44_SP1N6YNsOwUB9IDFnaKaTof66Ivor0s-aUyp2kaGH851yKWQDlaaUbIMnnjZHVllHtr9_ylJdHt7Va3PuNe2NaFiFU0V0cpevshHBQJzhwRCob9AZT49sF1ztHc1FCJhXQyv0fm51sA4ITgsZMlrX5gBNp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار محاولات إخماد الحريق الضخم الذي التهم المجمع التجاري في شارع الظلال بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81113" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇸🇾
انفجارات شديدة تهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81112" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c020bdc8b.mp4?token=hrDd7PS7WLqy7Fc7KuGBAT63lj8Y3MrgXb2ELsn9tSv8LNJrQGpG0B9jxl0Q9PM2AfHkT1iRuJMGwpfSciA8Sr6yrG8GbIgPptSkFJ0s-3XgOY1P4uOzCZMzKf553PD1WpkbqoCrMobOFVdJHQS4XDud-dy8b6bGFfGKCeSE6fKHyOtTZcuKACo3aIkSzxTB4LvStnnjgYLWIhQTey_Ex2tzwvntt5bxErG2I7YDpTs7tM1tKtxA-TybdJHq2plk36cXCyRYxBZCP9Ub3g5PDhfaJfampCO7cDimGCXIDO2BP7bahPHRjrTDy5otWtSDD-OdByoKFfGg0D9_iuYtybA6uiwn-m676xuprCJeoj7KlRuf0I8JqucsD2c9RHZIFuhfKJVSsQ8V2PB2LUjvVLB2BwcvQJ4Z9n0pKlq1yRfmBIyA0ZxJ3zIRqPDciBIr8FuNq00W98u2bFhz5qwsqVGmU_r9M1bWMw1G88IQBtqi9bSgLh9oN7nusMv6DSsCkurcmz0k6ca03IEkGhL4h1sIY9EsPFars-eCOJVhVmQfpLK827lJiy8Zo6v0dxHUUUB9D5VreLig23E7KX4W160P-_tx1RxpF1lwfS7bZA7wWXXn87tr7hULXAJC-JiCIHjldw-3dXZd6a8wJa9LaK6E577KwwWMDGddQSgccyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c020bdc8b.mp4?token=hrDd7PS7WLqy7Fc7KuGBAT63lj8Y3MrgXb2ELsn9tSv8LNJrQGpG0B9jxl0Q9PM2AfHkT1iRuJMGwpfSciA8Sr6yrG8GbIgPptSkFJ0s-3XgOY1P4uOzCZMzKf553PD1WpkbqoCrMobOFVdJHQS4XDud-dy8b6bGFfGKCeSE6fKHyOtTZcuKACo3aIkSzxTB4LvStnnjgYLWIhQTey_Ex2tzwvntt5bxErG2I7YDpTs7tM1tKtxA-TybdJHq2plk36cXCyRYxBZCP9Ub3g5PDhfaJfampCO7cDimGCXIDO2BP7bahPHRjrTDy5otWtSDD-OdByoKFfGg0D9_iuYtybA6uiwn-m676xuprCJeoj7KlRuf0I8JqucsD2c9RHZIFuhfKJVSsQ8V2PB2LUjvVLB2BwcvQJ4Z9n0pKlq1yRfmBIyA0ZxJ3zIRqPDciBIr8FuNq00W98u2bFhz5qwsqVGmU_r9M1bWMw1G88IQBtqi9bSgLh9oN7nusMv6DSsCkurcmz0k6ca03IEkGhL4h1sIY9EsPFars-eCOJVhVmQfpLK827lJiy8Zo6v0dxHUUUB9D5VreLig23E7KX4W160P-_tx1RxpF1lwfS7bZA7wWXXn87tr7hULXAJC-JiCIHjldw-3dXZd6a8wJa9LaK6E577KwwWMDGddQSgccyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من استقبال الأمانة العامة للعتبة الحسينية المقدسة لوفداً كبيراً من عوائل الشهداء في الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81111" target="_blank">📅 20:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
مطار النجف الأشرف الدولي: تعليق جميع الرحلات التجارية لأسباب تشغيلية حتى صباح يوم الخميس المقبل</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/81110" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68bd6daac.mp4?token=FSrinV_Zj5NAKBJwhjrRFT0NOu_FuZMzyWbTNKJ7ONeBiBwNBN4HPxZN93dVF7NGSAi2kGm6UKFSe8xKm_9xqH_lCfkrczw8rhBHnw1DKDlRyx5WRy6kZk43gqH_FXQwi-G8Xxn43WTkOfDrMkTYC8xCD2Aioz9mJ3n9giiDZCE0OLOhR8F0v2iF3pDj1Fm5ptRlDmQZqs4soCK3qANk7mk8yXzyCJQHsr9wRIo-cI9-fRmGqaP8yqF9e7vBhQPixRgyvkJnLVYuoZW6kbQOkjTPLkuLvYGEX51582RvHdbc9vlIVRHxVVVc3yNRrv21H1rLgmSt-qMev0khaslfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68bd6daac.mp4?token=FSrinV_Zj5NAKBJwhjrRFT0NOu_FuZMzyWbTNKJ7ONeBiBwNBN4HPxZN93dVF7NGSAi2kGm6UKFSe8xKm_9xqH_lCfkrczw8rhBHnw1DKDlRyx5WRy6kZk43gqH_FXQwi-G8Xxn43WTkOfDrMkTYC8xCD2Aioz9mJ3n9giiDZCE0OLOhR8F0v2iF3pDj1Fm5ptRlDmQZqs4soCK3qANk7mk8yXzyCJQHsr9wRIo-cI9-fRmGqaP8yqF9e7vBhQPixRgyvkJnLVYuoZW6kbQOkjTPLkuLvYGEX51582RvHdbc9vlIVRHxVVVc3yNRrv21H1rLgmSt-qMev0khaslfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم يلتهم مجمع تجاري في شارع الظلال بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81109" target="_blank">📅 19:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09643659f3.mp4?token=TXuqWSABDYnALJQEg1GC86LPKp7B7cYx_D2BwiaKlTHlCspocBaEewf1Kc_RH-udoWt-l2H0Un6FAU4pm-1YHIUdysk5SZzIQnHxyRvZ5rkebGHqBtY3jFNxi_RR3TvY7SqvUsBS11JJBHiuFFQ7H8Dl0j8o50kqhlekOGrTPcFypa9otlYErJqfdBdNSOplLF6_bpKhx0sV6ttx7jTqOezm7pdH9b-Vl6Za-wUVB9T9S7bu9HEkUqwU_FEuTii06ExwzLibCxma2EtJC3GUI4MEe2w9OzIYxMxSm4cpKViUNrLt51HfxLoyoP1dhLBR1iKsLW0lgRHM-DGtuGtwoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09643659f3.mp4?token=TXuqWSABDYnALJQEg1GC86LPKp7B7cYx_D2BwiaKlTHlCspocBaEewf1Kc_RH-udoWt-l2H0Un6FAU4pm-1YHIUdysk5SZzIQnHxyRvZ5rkebGHqBtY3jFNxi_RR3TvY7SqvUsBS11JJBHiuFFQ7H8Dl0j8o50kqhlekOGrTPcFypa9otlYErJqfdBdNSOplLF6_bpKhx0sV6ttx7jTqOezm7pdH9b-Vl6Za-wUVB9T9S7bu9HEkUqwU_FEuTii06ExwzLibCxma2EtJC3GUI4MEe2w9OzIYxMxSm4cpKViUNrLt51HfxLoyoP1dhLBR1iKsLW0lgRHM-DGtuGtwoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الساعات الأخيرة من مراسم توديع السيد الشهيد علي الخامنئي قبل صلاة المغرب مسجد طهران</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81108" target="_blank">📅 19:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f791916ef.mp4?token=hKQ129HGiM7a2y4ckN68VVKaZdOEnN5lF9t2wHTlMMoUDbRbmJ_teldbDcjNVfAfoHJfq7fJL2M7lh50VOImHRiDwaaphLgwRLyEybRyfN0JfecIAm0rkn3D1I-nsxW8hjvU6o1gVtT1GdxeXW7uJnyXXLyCzxzocq9zoBRbeSyG11J-tNk46kcASUXX2F-nHj6w_M9G3vXclc0-X5qmLOkCaguiJPOUdI9v8zSQ8TFlLPuxFqv27CG3CLkJgs-nQ-rSnaKRC9vSfoW8YsppaNEamHoW60KW5amf5YA9viAIPHC5TLYfL_gWTwglBR0Y7zPpPyDwU5iKSHl2KrG4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f791916ef.mp4?token=hKQ129HGiM7a2y4ckN68VVKaZdOEnN5lF9t2wHTlMMoUDbRbmJ_teldbDcjNVfAfoHJfq7fJL2M7lh50VOImHRiDwaaphLgwRLyEybRyfN0JfecIAm0rkn3D1I-nsxW8hjvU6o1gVtT1GdxeXW7uJnyXXLyCzxzocq9zoBRbeSyG11J-tNk46kcASUXX2F-nHj6w_M9G3vXclc0-X5qmLOkCaguiJPOUdI9v8zSQ8TFlLPuxFqv27CG3CLkJgs-nQ-rSnaKRC9vSfoW8YsppaNEamHoW60KW5amf5YA9viAIPHC5TLYfL_gWTwglBR0Y7zPpPyDwU5iKSHl2KrG4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طائرات مروحية تحلق فوق منزل خورشيد هركي ومدرعات منتشرة حوله خشية اندلاع حرب بين قبيلة الهركي وقوات البرزاني.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81107" target="_blank">📅 19:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107ad2da99.mp4?token=AK0D09ob499FO95zNAEejtwAea20B0PvbWFSIgY-NpFCpxnQ88kwbdIo5blQA6eqRxZtBju7g6TCmsXetkgBKcpkeomUGmsT3319ObQAir1ovnGsktQR3WJBe23Rr3FSO55_-am8T6xifdjkJCrb2LdOUBYd2ZShJX7V5sC8vJuvpb80h-5tlFdQ-F3s-JqQF7NfamvxC-xOYwiQgvT33Euu3ln3k2Ix_ZdViO5eoUcUtktZca5uJQpv5I0SxpAl1MQ0OiBUIibAuS1DAxSsYPMP2aYh_zNkjaryz8DWFsTs8QlrGrB4-5UvbKSNTOgQztlZZJpxIlnKNsRYkgEU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107ad2da99.mp4?token=AK0D09ob499FO95zNAEejtwAea20B0PvbWFSIgY-NpFCpxnQ88kwbdIo5blQA6eqRxZtBju7g6TCmsXetkgBKcpkeomUGmsT3319ObQAir1ovnGsktQR3WJBe23Rr3FSO55_-am8T6xifdjkJCrb2LdOUBYd2ZShJX7V5sC8vJuvpb80h-5tlFdQ-F3s-JqQF7NfamvxC-xOYwiQgvT33Euu3ln3k2Ix_ZdViO5eoUcUtktZca5uJQpv5I0SxpAl1MQ0OiBUIibAuS1DAxSsYPMP2aYh_zNkjaryz8DWFsTs8QlrGrB4-5UvbKSNTOgQztlZZJpxIlnKNsRYkgEU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم يلتهم مجمع تجاري في شارع الظلال بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81106" target="_blank">📅 19:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3abe6f8f5f.mp4?token=o2q87lKGmAgcuXjBgTnlD5XY-whTFNeN9qo0gdTOinV7zd5TuI2z8LbFGsyzwJ3iiKGWYbnklablY26a4wfqi-2UJvhi-9Ud5pOiPvXMtW9izYnIkY36R4MHLHoD6sxnbf3fmbQtpFyqekrffWZJhUfyjKllN3AFkLE-zGohohkGngfJXfnq_AiEGaw1G4_hDjKTArW-FIYlKHHdizBvysVHjmG_RPBzF7VOjU9C9c8JWE3lLuxtm_oswfHq-mRN5FczrP5ouLfO2cZURAEaaKeBWgamxDlWRHhYaVDtcz3mWzO3H9ZGmsPWn1t9kGvdpcWfnQsovpYwgC5F6lLe6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3abe6f8f5f.mp4?token=o2q87lKGmAgcuXjBgTnlD5XY-whTFNeN9qo0gdTOinV7zd5TuI2z8LbFGsyzwJ3iiKGWYbnklablY26a4wfqi-2UJvhi-9Ud5pOiPvXMtW9izYnIkY36R4MHLHoD6sxnbf3fmbQtpFyqekrffWZJhUfyjKllN3AFkLE-zGohohkGngfJXfnq_AiEGaw1G4_hDjKTArW-FIYlKHHdizBvysVHjmG_RPBzF7VOjU9C9c8JWE3lLuxtm_oswfHq-mRN5FczrP5ouLfO2cZURAEaaKeBWgamxDlWRHhYaVDtcz3mWzO3H9ZGmsPWn1t9kGvdpcWfnQsovpYwgC5F6lLe6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مقابلة حصرية مع الأمين العام لكتائب سيد الشهداء في العراق..
⭐️
في هذه المقابلة، يتناول الأمين العام لكتائب سيد الشهداء أهم التحولات السياسية في العراق، والأحداث الهامة في المنطقة، وخاصة الحرب التي استمرت 40 يومًا، ودور هذه الكتائب في استهداف القواعد العسكرية الأمريكية في المنطقة، وإلحاق الضرر بالمجموعات الانفصالية الكردية خلال أيام الحرب المفروضة على إيران من قبل الولايات المتحدة وإسرائيل، وتفاصيل حول قاعدة سرية للجيش الإسرائيلي في عمق الأراضي العراقية خلال معركة رمضان، بالإضافة إلى بعض الذكريات الشيقة عن شخصيات سياسية إيرانية بارزة وقادة محور المقاومة، مثل الشهيد سيد حسن نصر الله، والشهيد الحاج قاسم سليماني، والشهيد علي لاريجاني.
⭐️
"سيتم نشر النسخة الكاملة من هذه المقابلة المرئية قريبًا".</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81105" target="_blank">📅 19:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
محافظة ذي قار تعلن عن توفير سيارات نقل مجانية للراغبين بالمشاركة في مراسم تشييع السيد علي الخامنئي"رضوان الله عليه" حيث سيكون موعد الانطلاق يوم الثلاثاء الساعة الثانية عشرة بعد منتصف الليل، من أمام مبنى ديوان محافظة ذي قار في شارع الإمام علي (ع)، باتجاه محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81104" target="_blank">📅 19:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58ab0b0ae.mp4?token=pai0nEKW36SFiQV-VWvprLbp4U9IVTGzH_FNyNCCTtrYnWp7UElpi2gzedM-VTkpjxaaZELINUVFU0vakG0P07uPQ6MbNIx6wqSIGdyj9PcoemMgMEM-bRVXgmLpcxOJvWDq8oulL9cW1Kd_sxDLGA_IOdgzKM8F4WS0WtF30DSPGuthRwvDJb2jjZOybK8oqTt1GVz22EK-Lu4HBO0QvBhBVTGMszxiLSJIwNRhMIiWOvBjewHsZNtK0YomimWUKMvarTBr2s75nnUAuaazYl45P6oA6cV5_AloON0fyXGkMezbeGQ5TS8b3PLuBq5esWaxefgHHODMQjmbomKH-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58ab0b0ae.mp4?token=pai0nEKW36SFiQV-VWvprLbp4U9IVTGzH_FNyNCCTtrYnWp7UElpi2gzedM-VTkpjxaaZELINUVFU0vakG0P07uPQ6MbNIx6wqSIGdyj9PcoemMgMEM-bRVXgmLpcxOJvWDq8oulL9cW1Kd_sxDLGA_IOdgzKM8F4WS0WtF30DSPGuthRwvDJb2jjZOybK8oqTt1GVz22EK-Lu4HBO0QvBhBVTGMszxiLSJIwNRhMIiWOvBjewHsZNtK0YomimWUKMvarTBr2s75nnUAuaazYl45P6oA6cV5_AloON0fyXGkMezbeGQ5TS8b3PLuBq5esWaxefgHHODMQjmbomKH-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحزب الديمقراطي الكردستاني يبدأ البحث عن جماعة الهركي لاعتقالهم قبل بدء الحرب بين الطرفين في محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81103" target="_blank">📅 19:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b2955c79e.mp4?token=iZpqwIltBfP5IxbDqBLJfw8tJRJMXUvYfY5rcuWexZv_WYWLwHfuYGlTDmocg9Lz7-5R3ZZpL1ukF3cLj1lgsAakLiXpTb8RYxx-B_7U5ibPwCzijecA2WuP3_Zqqd1O_wsGsQyEB0UG4r96IXI85HO_N_B-P0uSLveWYKJIVUO6f-C3bE6bHcWWnEnB1Oinuthgaey_XhCZP4RG8QEu3T_mC4CTPjXm8_nYCv_oo2vPMkHQ-I4MbTViZObD_PUq6RHS6xppN03HI-MzvrODRAn17rgPd1pg9npVoVlBeJLgWXR12RkXjcZ2LOk38z5ssh9J6Q-yoNT2ifzsBjFkIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b2955c79e.mp4?token=iZpqwIltBfP5IxbDqBLJfw8tJRJMXUvYfY5rcuWexZv_WYWLwHfuYGlTDmocg9Lz7-5R3ZZpL1ukF3cLj1lgsAakLiXpTb8RYxx-B_7U5ibPwCzijecA2WuP3_Zqqd1O_wsGsQyEB0UG4r96IXI85HO_N_B-P0uSLveWYKJIVUO6f-C3bE6bHcWWnEnB1Oinuthgaey_XhCZP4RG8QEu3T_mC4CTPjXm8_nYCv_oo2vPMkHQ-I4MbTViZObD_PUq6RHS6xppN03HI-MzvrODRAn17rgPd1pg9npVoVlBeJLgWXR12RkXjcZ2LOk38z5ssh9J6Q-yoNT2ifzsBjFkIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مقاتلي قبيلة الهركي يتجمعون مدججين بالأسلحة الثقيلة ويقطعون طريق أربيل_الموصل الرئيسي</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81102" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72be292d0b.mp4?token=WbqN6qeqR8rEVa59MhIRxJwJjHXCpwkK7TyrbXdTVX_pxImfnP8CtYHeN0neabrbstom4iXnH-v6gzbdWJtVdzvmkpzbMZXSucLxes2KzhjIj4MFmMyQiDgwFDiaovaKnW3N7vTPI7Q97sS43ruV6nHVdPQRl5mNFwLdSJml5VrNyRMoBf-fSkuCKyl_lVGeUeJQeGAvsyWbqZRaipnqajvgAyWl4H8zoOrD8OouAAR03Vwyt2RePwR0fJC_xbafMM3lAQ_m3L27UunirrjqyAz3Q040rKRjW7zyoDNzEVHV3O9lgpOM3nH8-53lzkI8M7mKC_UGK1eNMycNiBUhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72be292d0b.mp4?token=WbqN6qeqR8rEVa59MhIRxJwJjHXCpwkK7TyrbXdTVX_pxImfnP8CtYHeN0neabrbstom4iXnH-v6gzbdWJtVdzvmkpzbMZXSucLxes2KzhjIj4MFmMyQiDgwFDiaovaKnW3N7vTPI7Q97sS43ruV6nHVdPQRl5mNFwLdSJml5VrNyRMoBf-fSkuCKyl_lVGeUeJQeGAvsyWbqZRaipnqajvgAyWl4H8zoOrD8OouAAR03Vwyt2RePwR0fJC_xbafMM3lAQ_m3L27UunirrjqyAz3Q040rKRjW7zyoDNzEVHV3O9lgpOM3nH8-53lzkI8M7mKC_UGK1eNMycNiBUhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تجمع المئات من مقاتلي قبيلة الحركي أمام منزل شقيق خورشيد حركي في محافظة أربيل شمال العراق مستعدين لمهاجمة مصفاة لاناز ومحطة خباط لتوليد الطاقة.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81101" target="_blank">📅 19:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_buzNS39DBF-V0zIsVcgjrVfyMRaeZNtP_xH6ICuIsEuDDox7RbizLLofnu52hOYo8Bol5EQHBLILQq02eKlbyM83q4fJKHK7th3m_T3p1yLi_pSirADKmesayNAiqYmrjIHciKiS0bydYVHyNHk7hDNGKF5p55CrT01HwrBAg4VFSgJAy89nAJD1U_W0owvCx5uQ4mm3dORpAU4UpM-7ZtbmEpaQr1WJCtj807bV5Gm_lh2BgyriDlpTAAD1mdM3vXXGkyHGXaQpsiAFrH2xa0w3T9HCVlAYNRhKGWng87O9dMVrYpkr-_-fMPU_LeCE8jtUZAjV0O_m5KDk10bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعيين محسني إيجئي رئيساً للسلطة القضائية بالجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81100" target="_blank">📅 19:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7984718766.mp4?token=rxHchq839I7fg-lLbgkA2OYjtLJKXLRP3_hqYeIUPR16y02TIBnM3USkedOm-vhPe-F_RT1tcKMRycYUETOy-t4caz_Bs4vU21Xl-ysniEYom7NOOv9CsopyJdPB-2tWWpHAp4NGuvi6kInjxOqRBDP82QBuqFt4lsPMEs2y4mIsUCi_z9OSJEM7wR02pPb1gNeE3XxdYlHfQuA164puBhxvB2j1_ZEPzvGoH8NucbJ3vkK9n63iGMd0Ul--GKcEhbvCgTmDpVkaR-ZAzIbK3psOrJuoCLU3K7ZHzmFWYm10NsOhF0eVitdMqPjI3o9z3hdpa3A3YkR110qMibqwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7984718766.mp4?token=rxHchq839I7fg-lLbgkA2OYjtLJKXLRP3_hqYeIUPR16y02TIBnM3USkedOm-vhPe-F_RT1tcKMRycYUETOy-t4caz_Bs4vU21Xl-ysniEYom7NOOv9CsopyJdPB-2tWWpHAp4NGuvi6kInjxOqRBDP82QBuqFt4lsPMEs2y4mIsUCi_z9OSJEM7wR02pPb1gNeE3XxdYlHfQuA164puBhxvB2j1_ZEPzvGoH8NucbJ3vkK9n63iGMd0Ul--GKcEhbvCgTmDpVkaR-ZAzIbK3psOrJuoCLU3K7ZHzmFWYm10NsOhF0eVitdMqPjI3o9z3hdpa3A3YkR110qMibqwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبيلة الهركي تمهل سلطات البرزاني حتى الساعة الثامنة مساء لاطلاق سراح خورشيد الهركي وتهدد بمهاجمة جميع المؤسسات الحكومية وخاصة مصفاتي لانز وكار</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81099" target="_blank">📅 18:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
معاريف العبرية: تحذيرات من أن مدينة إيلات في جنوب البلاد قد تكون هدفاً لهجوم بري.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81098" target="_blank">📅 18:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
قيادات الحشد الشعبي تجري جولة استطلاعية ميدانية للاطلاع على واقع الطرق والمحاور الرئيسة استعداداً لتشييع آية الله العظمى السيد الشهيد علي الخامنئي (قدس سره) في العراق.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81097" target="_blank">📅 18:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇵🇸
رئيس مجلس قيادة حركة حماس محمد درويش: كل بند في اتفاقية إسلام آباد هو انتصار لإيران وهزيمة لأمريكا. إيران تمكنت أيضًا، في ساحة الدبلوماسية، من تغيير الموازين لصالح الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81096" target="_blank">📅 17:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇵🇸
رئيس مجلس قيادة حركة حماس محمد درويش:
كل بند في اتفاقية إسلام آباد هو انتصار لإيران وهزيمة لأمريكا. إيران تمكنت أيضًا، في ساحة الدبلوماسية، من تغيير الموازين لصالح الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81095" target="_blank">📅 17:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية:
‏مقتل ما لا يقل عن 14 جندياً مدعوماً من السعودية وأصيب 23 آخرون في هجوم شنته حركة أنصار الله على مواقع في حيس، جنوب الحديدة، تضمن الهجوم نيران القناصة والطائرات المسيرة وقذائف الهاون كما سيطرت الحركة لفترة وجيزة على المواقع.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81094" target="_blank">📅 17:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81093" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">البحرية الامريكية تعلن مقتل عناصرها المفقود</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81092" target="_blank">📅 17:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">البحرية الامريكية تعلن مقتل عناصرها المفقود</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81091" target="_blank">📅 17:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81089" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
لجنة مراسم التشييع:
ستبدأ مراسم تشييع جثمان القائد الشهيد يوم غد في طهران عند الساعة 6:00 صباحًا. يشمل مسار الجنازة شارع دماوند، وساحة الإمام الحسين (عليه السلام)، وشارع انقلاب، وساحة انقلاب، وشارع آزادي، وساحة آزادي، وطريق لشكري السريع.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81088" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4l6oKRH0N_qCZHXS5LAnO61kMR6Tf5fp8roWLun4pPR647goR-1eFgsKsm6SkGR43EGUEz-Hk8BkOu4M8jeSOOxp4XPIy-h_ozKZczOSzDjI6Q0s2-FDs2uYzPEryzEXx9Tf3CX-GBc0oPipvABviIXdxJA7w-MZDUho8I17wboXtXL4HJSqtfxms8DWg20UJdBjCTvD8YY0NDXcOmaISnBa4Ier-K9tpZVL7xvli2XQeL6RsypPQzB3c-WK-yLpnSGuVOPn0M68LkBd2aDgNpBKAEfvQlD0rhar8nhYZJKkQzqu6xAKrBSqJSfU_XrWBxmSgoQDHB0YyOLnpgr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحن، الشيعة، نعاقب قتلة زعيمنا.
من مصلى الامام الخميني في العاصمة طهران</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81087" target="_blank">📅 17:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">متداول:
قوة من النزاهة تدخل مصفى بيجي وتعتقل ثلاث اشخاص (مهندس منهل ، احمد النامس ، زياد الراوي)</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81086" target="_blank">📅 17:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
اشتباكات مسلحة في ابي الخصيب ضمن محافظة البصرة جنوبي العراق بين قوة من جهاز الامن الوطني وتاجر مخدرات تسفر عن إصابة 3 منتسبين من الأمن الوطني.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81085" target="_blank">📅 17:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
رئيس المحكمة العراقية الجنائية:
- نحو 3300 أمر قبض غير منفذ بحق أزلام النظام السابق من المتهمين بجرائم ضد الإنسانية داخل العراق وخارجه
- عدد المحكومين من أزلام النظام السابق بلغ 160 محكوماً بينهم 26 نُفذ بهم حكم الإعدام ونحو 270 مفرجاً عنهم
- حكم الإعدام بحق صدام حسين كان عن قضية الدجيل فقط في حين أن هناك جرائم كثيرة مُرتكبة توقفت الإجراءات بشأنها بعد تنفيذ الحكم
- المتهم سعدون صبري أُدين بقتل الشهيد السيد محمد باقر الصدر
- بعض الاعترافات الواردة ذكرت مسؤولية طاهر جليل الحبوش عن جريمة اغتيال الشهيد السيد محمد محمد صادق الصدر
- صدور حكم الإعدام بحق المتهمين بقتل مقلدي المرجع الشهيد السيد محمد صادق الصدر والمصلين في صلاة الجمعة بمدينة الصدر
- ثبتنا باعترافات المدان عجاج بارتكاب عمليات اغتصاب لنساء ومقابر جماعية
- رئاسة الجمهورية لا تملك صلاحية تعديل أو تخفيف أو إلغاء أحكام الإعدام الصادرة عن المحكمة الجنائية العراقية العليا
- جميع أحكام المحكمة الجنائية العراقية العليا غير مشمولة بقوانين العفو العام
- إجراءات الحجز على أموال المتهمين تتوقف عند وفاة المتهم</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81084" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">متداول
اطلاق سراح معاون مدير مصافي الجنوب منتصر حالوب بعد أيام من اعتقاله بتهم فساد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81083" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محافظة الديوانية تعلن تعطيل الدوام الرسمي يومي الاربعاء والخميس لإتاحة الفرصة أمام الجموع المشاركة في مراسم تشييع جثمان الشهيد القائد سماحة آية الله العظمى السيد علي خامنئي (قدّس الله سرّه)</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81082" target="_blank">📅 16:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d08e53336.mp4?token=lpDkhgTsBmxZH-P7mTwWu1XeM6CyfNteQZDandRQorP_efsyTj5ZuXwDl6-RA05oSi1bx_uhVdLF4Ty4OHJsjyF0kbhxSoSQ7hgcM62Rgk4IP6fH45d9PhXVtxt1Zrag0NPjrZ6yrbip_5n5IZ7RflHqCEveBBoadebct5qlPezYj8YzlO9jF28_0atVTEj_Eg_EsZ4xlHv_WoqnuWUxMNlRoQE37ToWuz7bkRZQ9ClT-QQOS48D-uDPTmb0nQ4G_SeKnQ7OFIsMrI7ugT1Mt7sm9hqO7I7e2HlJ79ofko40a_o9nRG98MK2Gt4Ol_ESIAWnRaGWQPGh5xQ1_5mUgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d08e53336.mp4?token=lpDkhgTsBmxZH-P7mTwWu1XeM6CyfNteQZDandRQorP_efsyTj5ZuXwDl6-RA05oSi1bx_uhVdLF4Ty4OHJsjyF0kbhxSoSQ7hgcM62Rgk4IP6fH45d9PhXVtxt1Zrag0NPjrZ6yrbip_5n5IZ7RflHqCEveBBoadebct5qlPezYj8YzlO9jF28_0atVTEj_Eg_EsZ4xlHv_WoqnuWUxMNlRoQE37ToWuz7bkRZQ9ClT-QQOS48D-uDPTmb0nQ4G_SeKnQ7OFIsMrI7ugT1Mt7sm9hqO7I7e2HlJ79ofko40a_o9nRG98MK2Gt4Ol_ESIAWnRaGWQPGh5xQ1_5mUgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار امني وعسكري في محافظة اربيل شمالي العراق على خلفية اعتقال خورشيد الهركي زعيم قبيلة الهركي الكردية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81081" target="_blank">📅 16:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11259c8a0b.mp4?token=Dtdj42Tv3sOya4IsA_W4Rpa5Hgeo8XTmnPVrMZ0aTurzx7d9YGFweX6lUfhZMALzJEhedGaeADzadbxPObEaxz5nF9V3Olzb5JVk6ZgqQuIpNrcP3ErjRU8QtwsB6RwyduZHzxMFLgq4M2bAFyf4FeEC8KvlK5pqAHA3HpIS1g3EKN1t7EZjShNDITVScZKc2UcB9rbHwmMskD5vkmGrVmK7udKWtRvSFW-vrniLR79eGZF8YsxyLeLVYA7WwIBu93Oa8OxC17k7S7KbZISKQheD52PbnmdMwey4Jh9_ptUWAmKxPluhsQWavj7vkONVMZo_9kjhaI-AojzKftxHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11259c8a0b.mp4?token=Dtdj42Tv3sOya4IsA_W4Rpa5Hgeo8XTmnPVrMZ0aTurzx7d9YGFweX6lUfhZMALzJEhedGaeADzadbxPObEaxz5nF9V3Olzb5JVk6ZgqQuIpNrcP3ErjRU8QtwsB6RwyduZHzxMFLgq4M2bAFyf4FeEC8KvlK5pqAHA3HpIS1g3EKN1t7EZjShNDITVScZKc2UcB9rbHwmMskD5vkmGrVmK7udKWtRvSFW-vrniLR79eGZF8YsxyLeLVYA7WwIBu93Oa8OxC17k7S7KbZISKQheD52PbnmdMwey4Jh9_ptUWAmKxPluhsQWavj7vkONVMZo_9kjhaI-AojzKftxHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتشار امني وعسكري في محافظة اربيل شمالي العراق على خلفية اعتقال خورشيد الهركي زعيم قبيلة الهركي الكردية</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81080" target="_blank">📅 16:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🫡
قيادة العمليات المشتركة العراقية: طائرات F-16 العراقية تنفذ ثلاث ضربات جوية ناجحة ودقيقة استهدفت ما تبقى من أوكار ومخابئ العصابات الإرهابية في الحدود الفاصلة بين المركز والإقليم من جهة قضاء الدبس</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81079" target="_blank">📅 15:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">طيران الجيش يواصل التحليق فوق مواقع يختبئ بها عناصر تنظيم داعش في محافظة كركوك بعد سلسلة غارات جوية على خلفية استشهاد عنصر من جهاز مكافحة الارهاب</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81078" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356bbb9ab8.mp4?token=r54iswxwk7tIYkK4XqU5-YlydR-Yg2LCdt4FSJzSiv_qDwuthWn626sBEEO3kaxD2KqqfhLZSk0Z0Xb3tRtUKwCzi82uGuCF3oFRLAclNL3CrrGFQNQiM4CQY4squAXGxgrIsPJIq_Htk3G_vt5yTJtBgXk3IAA0bgEBLHSbDfnadH2F9b9XeVcPpH32vlhjzbt98F0Rq8q1mYTAHjDqVQfSzrPOqXx4Yn9j7qLbeYhuQSc0XdMTKdnO_6SZrReGavwDG6qtiFvzqxgYJAIT7jUfYBA_-Ezra7bVzNvChlaOPwsCUiE_YkBwEkmss--LW5BRNS4HX-P8nCcHGUax8Rd0V_9IjJEer-FmQTRGYywAmru4HKmCLkXjQ7Nfq0j1PmQPOASDATCjVg4ma2e2Ib118WS7_VMgKRbCIh8ZR5kSiqhMFm1cT4XWMwSW65FGVCCBRD-nO1-zwaGh3AjN2OFrXZur5pTywZaP5EM6kiZ6M2RNj91zQMD_3sMrlaQn26E4P5Hx77cW61ZZzHILt0AwLVJCm3HdGd7L-yNsOFQW97qZf1OrJgHAnyRKkLlab_hRDlpjWRXMC1HxjUmqWiXSQ3Q4xyrjvhVUQOgQgbEFjZc3TuwvQtbUr1BCwmZzznFhfOyZ5zFqGJf23s3JFV-cQGwPVeJv12cpOdJUza4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356bbb9ab8.mp4?token=r54iswxwk7tIYkK4XqU5-YlydR-Yg2LCdt4FSJzSiv_qDwuthWn626sBEEO3kaxD2KqqfhLZSk0Z0Xb3tRtUKwCzi82uGuCF3oFRLAclNL3CrrGFQNQiM4CQY4squAXGxgrIsPJIq_Htk3G_vt5yTJtBgXk3IAA0bgEBLHSbDfnadH2F9b9XeVcPpH32vlhjzbt98F0Rq8q1mYTAHjDqVQfSzrPOqXx4Yn9j7qLbeYhuQSc0XdMTKdnO_6SZrReGavwDG6qtiFvzqxgYJAIT7jUfYBA_-Ezra7bVzNvChlaOPwsCUiE_YkBwEkmss--LW5BRNS4HX-P8nCcHGUax8Rd0V_9IjJEer-FmQTRGYywAmru4HKmCLkXjQ7Nfq0j1PmQPOASDATCjVg4ma2e2Ib118WS7_VMgKRbCIh8ZR5kSiqhMFm1cT4XWMwSW65FGVCCBRD-nO1-zwaGh3AjN2OFrXZur5pTywZaP5EM6kiZ6M2RNj91zQMD_3sMrlaQn26E4P5Hx77cW61ZZzHILt0AwLVJCm3HdGd7L-yNsOFQW97qZf1OrJgHAnyRKkLlab_hRDlpjWRXMC1HxjUmqWiXSQ3Q4xyrjvhVUQOgQgbEFjZc3TuwvQtbUr1BCwmZzznFhfOyZ5zFqGJf23s3JFV-cQGwPVeJv12cpOdJUza4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اطلاق النار على المتظاهرين ضد تردي الكهرباء في قضاء قلعة صالح ضمن محافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81077" target="_blank">📅 15:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81075">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏴‍☠️
رئيس اركان جيش العدو:
منطقة البوفور هي منطقة استراتيجية حيوية مليئة ببنية تحتية لحزب الله بتمويل وتوجيه إيرانيين، قامت على مدى عقود ببناء شبكات أنفاق تحت الأرض في هذه المنطقة لتهديد مستوطنات الشمال. يجب على الجيش اللبناني الوفاء بالتزاماته بموجب الاتفاق والعمل على تطهير المنطقة من مسلحي حزب الله.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81075" target="_blank">📅 15:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇸🇾
في اول جلسة له..
ما يسمى بـ"مجلس الشعب السوري" يعلن تأجيل جلسته يوم غد بسبب زيارة ماكرون وعدم قدرة نظام الجولاني على تنظيم الزيارة واقامة الجلسة.
بارعين بس بالتفخيخ
هيج سوالف صعبة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81074" target="_blank">📅 15:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي:
من حق الشعب ان يتساءل: أين كانت النزاهة الحكومية والرقابة المالية والمتابعة البرلمانية من جرائم نفط الشمال التي تجلت اليوم؟ فهناك تقصير واضح.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81073" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyiqL5dT2UEfyhH9kPVK3aUTlDei79fh70ki0Ab901V7JcoYhkSrq_8M_L8o3JfutJlnUZLZ8DzeU0TO8jdd1FhzAuy98fcnh30sdmMNpg_urXqgyGh74JCISPDGQ4UcZRbIbJy1dhPpcsy-Tyt-SibBuoRi0bx5usHaTaH9C3mgD0d00a90k9S1fkBJ7jg2pyyagaWmbwpR2KBoFt80x51VGBS1Rf_YanC29ogdSMCd6rQiyYCBO9lYoEEf1jEXEmoSdvg99jf8WHGoUZsjzBa3MZSfLUstgR9mjxtavk0RP-i9NHPEsdny76vjqh6SOUAB1QGgj73mKX0A-yK5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارة الامريكية في بغداد تقول ان العراق يمتلك امكانيات هائلة وشركاتنا هي من ستطلق عنان هذه الامكانيات.
وبمعنى اخر العب لو اخرب الملعب</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81072" target="_blank">📅 14:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81071">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
وزارة التعليم العالي والبحث العلمي العراقية توجه بوضع الإمكانات اللوجستية المتاحة لدى الوزارة وتشكيلاتها في خدمة جهود اللجنة العليا المشرفة على مراسم تشييع جثمان قائد الثورة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81071" target="_blank">📅 14:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لحظة وصول جثمان قائد الثورة الشهيد لإقامة صلاة الجنازة.
#قوموا_لله</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81070" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acfd2392b1.mp4?token=DHaxb0ZGNm-fN401igeo3b2FBk9vM25iMPEBaeL-wzo2SxJPRdSbR0-6ymPiRArRM_hPnk3dsz_jvLpM1DHdmb53WH_jCX2dlDSHNVELQ_FacI6u1DOZRCJ8sUpgRz4DSwQDBHJei2_FV9JtLh0NRLW35n67-nXSZFcetyrlvMSvwss49J6XuequNfza-GNQj6zx_coiBMv2cY3ti1DFWA78XBBzugE9-xMNPjl5XtQLlbebLa8Y0iroEdMpcebmzusI7lZ5d9_inviAssUdKFMRccLNhH_l9ZSQXFJL7UHdIqpaY9ZkJ1LMDp6PWFeuvfzDT1EKYQ3A-XoOjJUbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acfd2392b1.mp4?token=DHaxb0ZGNm-fN401igeo3b2FBk9vM25iMPEBaeL-wzo2SxJPRdSbR0-6ymPiRArRM_hPnk3dsz_jvLpM1DHdmb53WH_jCX2dlDSHNVELQ_FacI6u1DOZRCJ8sUpgRz4DSwQDBHJei2_FV9JtLh0NRLW35n67-nXSZFcetyrlvMSvwss49J6XuequNfza-GNQj6zx_coiBMv2cY3ti1DFWA78XBBzugE9-xMNPjl5XtQLlbebLa8Y0iroEdMpcebmzusI7lZ5d9_inviAssUdKFMRccLNhH_l9ZSQXFJL7UHdIqpaY9ZkJ1LMDp6PWFeuvfzDT1EKYQ3A-XoOjJUbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران الجيش يواصل التحليق فوق مواقع يختبئ بها عناصر تنظيم داعش في محافظة كركوك بعد سلسلة غارات جوية على خلفية استشهاد عنصر من جهاز مكافحة الارهاب</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81069" target="_blank">📅 14:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
مقتل عدد من عناصر عصابات داعsh الإرهابية خلال الضربات الجوية للطيران العراقي في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81068" target="_blank">📅 14:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5I9hStKsV9D0-Pa3ogbbHPWL226lbcGLDiwBjBpLJ1V9_5AC3Fg2TgV4AMx5nysBNJbrJQXhbWJSxacpF6bEsD2vF4TnMq5MdxSORMgvV3K1fNWeKGl4Y49g8gGOeEHIW5G8-vLuIZSwr50RW2f4X5XmVDcBR0FVY88wFaWVKj6vLy1lm6PpYddENR1eTnJ0WhS5oz499BMRzN8BrvLvIcIum4qKy43P93dlKOu7KQ1xKMjMbrcsEX83VWsGpq_ioherDcT-oBkDgLmd8MzcIOO6QPGen4xRpOocGSNKzBb3A7KRyrUbj0p3e_koXL1bPlUMqDyUo2iCejkPO18MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
اليوم، شهد الشعب الإيراني الإسلامي الأبيّ الذي لا يُقهر، بصوت واحد، لإمامه المجاهد الشهيد قائلاً:
«اللهم إنا لا نعلم منه إلا خيرًا».
ثم نهض الجميع صفًا واحدًا، وهتفوا من أعماق قلوبهم:
«يا لثارات الحسين (عليه السلام)».</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81067" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
‏الدول الـ7 في أوبك+ تقرر زيادة إنتاج النفط 188 ألف برميل يوميا في أغسطس.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81066" target="_blank">📅 13:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj-7TEonLnFOFqtlJ2Fw-5bXHQx7D4vikkeGckkMGQGec9B-Lb79L_jge1NHfSkgUzRNSN0W_2tWm72JiDfehixR-NakWuz8HC_9T9X2oTc3Fjkld9qhSoTo3OzdxM0qDxZjlzBNT0fJlL0b7sk8CqLuJWpd4dJ_oUqjaAydS8JbOODp-HBaPAL1Sz1YTPrI0sFVswtQVQVH9_o9tLx0hqSpVQE8Jmhav4wbNroXvgvpq60--4DZT0dv2xsLN58Co4xAOnmJYRGu5MVtaI_DyvJZnoVr4X9AfQrHe0UgOggwzSz54UBSo63Ib4IJ4oyQ5DAlhoIlmW5OD6ICbmTCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المجلس الأعلى للأمن القومي الإيراني:
راقبوا إيران خلال هذه الأيام القليلة.
هذه هي إيران التي ظننتُم أنكم تستطيعون إضعافها في غضون أيام قليلة!
هذا البحر المتدفق من الجموع، يرفع الآن شعارين خلال مراسم الوداع والتشييع لقائدهم: المقاومة في وجه الأعداء والانتقام لدم القائد الشهيد لإيران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81065" target="_blank">📅 13:44 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
