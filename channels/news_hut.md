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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 188K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 16:09:05</div>
<hr>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY1i3-zYKbvImSsuNGFBGq8AKs_W3ir6QzGRuRbBdHImZghylSoat-5jMd7IIb7sRnOeqK5nt5sy7MiJjpnYHHEZt5NuvHDkoqpo7Y-7EDSgsMzzn478Pq2VQzv-Uc4soIIvRPuNtxg55Jcag5z4bWtBzu1uaKbgHGdtJ7-h5AR0KBV4XRFWL6H5DhSgBbB1XGvbldcKLNoXEZa-daIueYZf-XJa_c1iwh7hAcD_hgLotEXMsJgg-SDTsrShKBIcEICbNICejQo1ad2hVi3AIcEo587kNv9hxoZm3X8VAWmOD7X4NwFI8BGnFQ6A50i3muXQungJKNB3vcsmkJpBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4niFslqZE0AoBZJ-dmltWAWiO_SCAmrBELRcjebG9bGaF0oA6OXrYPFo-CNaN78SNNUV8c84axNMDp8PdUqqIlUpaq8INLezNLXwJBFw_ohvxcsTnpeaq6l2ptEIG-ZbSrZR73fovMYw0TDb-GdIFxLbqSwgCbhhmAsgVqglFUT6790J0kwhS7nakj9QQRevpdvLWmogh4_W-q3xJ4A6w-ztFWjF6_wXWv72lcE4Vcf15UfRetSzPWYzfXMFGGyq46nRXJL2CRNxgyxv6-1o-L5LPE-v0CcmASgrQfFaRTihQ2NK36FSRRW6SJ9tBCNyCrsOBxqew5BX8wrwnWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwga0J5qoQpDy7fdgNWSFyD6jtgsob4p1o6RLRVe_bbKM2Yv986DG5qn9jPz61nvjgCrHM93CyIQx2qqrhFeA3kHuDdkVgCzoq6W_P4PoIdkr3IDxS2oEf9C1_Qvtl04ut-OvLpHEztSWGRp5B4Z-aGQ1nO_GOh8VSWOARsj-j-qQ4m3YKHAX-w4x56IOvL4Z32lxOjEuWvW5y4SlGng_3C52VGaUc2oNK7pmtaqkiRFqNGTKUfGL6o8bZ1U9WEcXUYlgJReQgjS_RNNMcz0OnVd7i8tF-3dtDgT-glPY03ouPHyzYp-dYH0JNPHU-vDfGBpsOsNnj_BKk5DW-GtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kq3T_2CavGcuAVoxUfplfubHnE7OTK24HASaEC8iwpuFC_esIer8aLaXW_7jmxjo5JKMrUz4phhOGo53KOwJUj_wcJVJYwrHnE1hEyokspFho86RoYZRXSv7y6vdMDI_oMj4D6t9-nl9JfXl9u-wyl_e3sVcsGMdAuvmGKwZHA2_uLNzUBTDy0530nxB493NfUxN4I4eP24UmRQhj6y-hdUNnnIfJMA6XsmMwsZOeZCOG2daM0FRde-Dc35HVZQBwe_5r4SOvQytdlO-RdwZ2hO2KWECNYPp66U1ypJmhI9VkAmUf8t9AAxKeEMizMfH3BSeGDQll1J1ZwROVEYF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmFOMTM5g9RP4M1hg-JuNg-mRtQBtk8IcKNERE1jr3sHd3hQi7TtQ8OJrf5v-6kZb7Zd20S4JblJKy2_ZcXIEPlzkJ53q_i28lpQ6QHaHy4jderSpM6l0EAU78TLUcEHdBIX0KhpEh23l5IunTbIR2axqGtfrJox7fB2ZR1tgUqiBtFV_g40fg4RJXiniDSTASgjMxVLIM5pFZ2y7vGupPvxcgni4PQZi6iCvXgPAhpUs-5dQLPzgvmhWiddAlP0h3lUFkL5ZKettFkte9bXGd3HL8__gIdqQP3cDvLBn2u-B4gzokejN4xRki6G70Vt4MJHn-WP4G3I52OkXAgyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_SCRTXIZ3SnESPG_wvKLm7eAk5tTQrH-orNFDMkurHTpU_u1G3kin7aokjf8YmViDpBkhlO2bC_HPKmoWgv4kJ53PYBF8krzyLKhP2EtlSagyLyRIg_cb7RBWrL0Y1JsXJIzxYRyuSVy6RgGOFbf-6PBxw2dd6rFBgtQ0BgSxwscMp7mYbscfO0K-sfmdD5PeZS1xw3Rs3bGXYIS0VpaKW9pj6roKFBMNCRhJufaMlOihs36iTzJiEt4kd9OV4BuvRc5ZcsvYrrFMInNiJVo5TUTivMECtYrDOOrvJbzjghHxpvbSfcE7_DQ3_7yLRYe83pWfmjX6I9euk324Rv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjEFofRyaqinnTPAYE_vo6TWPvN4TIy6wuLFCgWDgEnbwMkya8aSpDIAbH-QuexISsrNl7R9gUbLRdDJxc99j39sJm2mZrbDrVXsCELDhFhBV3CXpG2Qxeu7Cme5380fsjAB5NCmpuzDeFSKXHyDmsRAmjvc3m1NPY7CC05XAEK3xC-1e4WW1w9IabxK7MPzhFlBRmsShwpzGG5dZbVS5AJcamy5-0fC4vf8ZFLSbWz41E_d-KqyFQ8B9MqJDctIzsIjU6icovdJgNUxShV5BBNDfPDnjlRngGyUywkxOyLB9NAtj3dMKk8Tz0c9MdIggRuGT1maadokqnwtB6m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEK68BX4eNB5pxr7MKeKZ6h1UZyTZDu2qFLQbNM2l8NNPzwIhrsrcB9oRTYKKBDu6PMejC9MpqoRAA6pgxDKlIpgyBDchZjjKNquY2qdYn9KJoGHo5XFFYDcoM1fE6SPJOjeAbrnF4NdhDj1KiKWDBRxnCjP5DjFvagyJv63o9Y6E-UFBa8rRiI5zW3sZUVkl9qmCPAUxRClsB9lD5t7xjkYaR-teTyE1vEQcX86elXamiTWbF5YpfRQXwNke9r-eeaz8Pm95SwqizPPjGMPdlAf6g_0OxC8z_H6FuaaKEkOHzQS_-J4q0p2WzjGYC5FkOPmQG0J5NbDlShTGctk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=oBpbErkQc_yEOwRjmXUqm_HdVK6U9AkswOzIJqn7XDs-qhH9z81KO7x1FPDxqi1AGGOYq6TVbHeqY2hhL_xsb_XCk4UmTMBkRtPRTnN4Tokk5Zft7mDdfB7rVZ_13dIQOhj-AkWk9iH-amaz5zmJL1LY8v2CZSVJAvUkmdRaKSYVsUo4JsFr_kmM3vMRMB8Er21OhrLXICSuxiFbIokN6Y2oxf6PXO0duaoPhjEwK_PpeZlmaeJj24KsV-PnSi5EUXjehid6UuZzUzKSCjefSq7CYGx9Dn2AprZh1NH6ZIaLW5SxBiKVkTu5Ry5S0dzuzAGB6uah90KsAfrF2SBTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=oBpbErkQc_yEOwRjmXUqm_HdVK6U9AkswOzIJqn7XDs-qhH9z81KO7x1FPDxqi1AGGOYq6TVbHeqY2hhL_xsb_XCk4UmTMBkRtPRTnN4Tokk5Zft7mDdfB7rVZ_13dIQOhj-AkWk9iH-amaz5zmJL1LY8v2CZSVJAvUkmdRaKSYVsUo4JsFr_kmM3vMRMB8Er21OhrLXICSuxiFbIokN6Y2oxf6PXO0duaoPhjEwK_PpeZlmaeJj24KsV-PnSi5EUXjehid6UuZzUzKSCjefSq7CYGx9Dn2AprZh1NH6ZIaLW5SxBiKVkTu5Ry5S0dzuzAGB6uah90KsAfrF2SBTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpHNCPtw1Ni3XZuJ9HafMRWp4O9vC_brNZ4mh9ZEA_UmPnGh3w6G0uIF_haMScRy7D0iZkC036PTkIIOVYEgky-9Eq7cGI_IQSidw2azmp0wgjmcjmxP6U_qvKdQMb7DeqNq1Gf0QJrI2zBbqN_5BIE3bfJAkLEG7L3U5kA-omYBNjxve5Ld9hLspUs8Q1SxDta11_aG1IcaArxoZCqVZ-GxLVrOWzY3QE94cQRwAbuXSuy2b_aZ7z-oNQjucdTVgigRxd8WtggwVE_Zyxg1hUp9ZvGEYzyMNphMQE6T-870sDiP_uBDLnXA3VFO96i7xxRbcB5AMnS1txWK6wvFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOJGMtSuoDQ2gyGZZBfY15s8czaTQKAjGQog1RGy6YX6kB7r5jOYZ3d1yTn8zJ5CKillijTYUCNKqDcx3hSY9NFya_MPtSOb4sdZX56gmaVjkW46KxT1OuTbu55FlEVOkKrUzCIVnM3GLbR8dvwfBI2vmz5dld7Ua6YqcuGVwmy6MdMm72fu_Sq9Ls6St72hN3JLEc8iN7zNNypHhKE_x8GkBo34jXIRGVbgfSNM3xPhdv7e3B3qHflaPKVM_IOe4Dl0mgc3WyqODEC_kRtA6TIkPJuuEdGQu0awCesP1f9DVaMFG31e6gIfiw-kjSy3QPcMAgNwIEn0AUDHQ1Xg2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcFiZON5azZP76-oOOtg3LuVS5VxdBt7-BEuvW7eIRhjS8EgQlGzcHTkBEle-VmmMFaNoF0k2h3Eos1rjffPR80VsX6tvPM-GZQ6Iw1F2dllPK2DwfVMLyuSZCB9wZpqwfEHs0EVl69_yp_dAg2vm2U4C0plBaiZBLRjhp4i9pJ3mmjtsFZXcTEboaT0LydsMwI4Snhker4s3pYbvKQiXLz5-wHxxB5aRZqbOfPNCKlM7HBeQwI_hevWMKSQeYrKT7xsmTBB74Q7-qOVNqXEcJtmSfp0zbqAxQdpqjFfIYMv2a1iSP9Mky-C3ZYcngPyXbf0sm9hz4-S9ekJTGzJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4Pwe0PjFXca-KvlzYZI-JtH-DYurEoUyVxe9jrcDi1KHAMCOjRUE70iJOqpUFYSGjkACML84ur9incu33aYNt1QlBAquAmsDIKmLC20fDtG9SKbouycoC1l-eH_u-184EJ_Or43XtDffcS9tSnN49fJnAroVNxBInWaeUZtz-OygOMbIJem51JdfMIB9u3umlz4E7ClZszUQ3s6sEXAeyFHjHjPI6ddpbWHCRj9bSlHZKmUY4oKC9odnGzMbWsnvsOrFMbdkXaQbnQxLiPZdTMUaO6boCEb62NohIuap8SMIyzG64vbMISFxjPlnGxpu39obGe-ecrxW9wYxMfeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=JSqO6ujRrvVhDNl-FKgEGVlTDTUgYoyk4cwoiDL5gJr_XJsby58Mh8cjSWiXAbLEGkN-NfiE-tOlDK2Ks-tivh-gIwaNmtmek05fXv72LFF0Byhiu7fckqBe3VxD-7_uGSBE09k0KX9c_FiT0XRWc_zS-fNZzIL_7CQOHd8VwOYLbfTsFuJv2tfoPQdxdukY1SgqWWbwJZnQNBVdbolC5rsCBySwq9e4-6hxrooWmn12HOPPVXdChWt_wc1-4QSYUoNvo7hTiqA5HPT6AP5ywjeWh08yEW1qOxi1jbmerOOTKJUx2IGees9rn9vb1eMNYBTrxXW0SFnd66vaThNK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=JSqO6ujRrvVhDNl-FKgEGVlTDTUgYoyk4cwoiDL5gJr_XJsby58Mh8cjSWiXAbLEGkN-NfiE-tOlDK2Ks-tivh-gIwaNmtmek05fXv72LFF0Byhiu7fckqBe3VxD-7_uGSBE09k0KX9c_FiT0XRWc_zS-fNZzIL_7CQOHd8VwOYLbfTsFuJv2tfoPQdxdukY1SgqWWbwJZnQNBVdbolC5rsCBySwq9e4-6hxrooWmn12HOPPVXdChWt_wc1-4QSYUoNvo7hTiqA5HPT6AP5ywjeWh08yEW1qOxi1jbmerOOTKJUx2IGees9rn9vb1eMNYBTrxXW0SFnd66vaThNK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=e8QNZD9G1RB7icoUEua8ENFk-cemn1Tq9EXWBFNuiQSXsKDj2JuT7yZxevTS9PSfPoYi3o66mb__vWn6z0nITAoD0abS0_rAw4ocEzPjJjqCMgnQddZaAo0W-J9j8-4kIU8rY4SKnwfqEQnecfrxB7ZX16iDWEAKnAOM5xjS_2zrBZZkoeqNSt0phXR7WgbiP-kUOH4C5jqT0P-EF7R6EwDZMni9nbQ_1AXP1f_YjVb-K2NC7Us1C8ygB7wRaWygAWowHZOovM705lPP0Fop7MSJ8qiVpmg2_hVOEFtjYr2Tf2dJj1NU2ehnex8q9lQSoJsYNW2sGvYIavtAjAsN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=e8QNZD9G1RB7icoUEua8ENFk-cemn1Tq9EXWBFNuiQSXsKDj2JuT7yZxevTS9PSfPoYi3o66mb__vWn6z0nITAoD0abS0_rAw4ocEzPjJjqCMgnQddZaAo0W-J9j8-4kIU8rY4SKnwfqEQnecfrxB7ZX16iDWEAKnAOM5xjS_2zrBZZkoeqNSt0phXR7WgbiP-kUOH4C5jqT0P-EF7R6EwDZMni9nbQ_1AXP1f_YjVb-K2NC7Us1C8ygB7wRaWygAWowHZOovM705lPP0Fop7MSJ8qiVpmg2_hVOEFtjYr2Tf2dJj1NU2ehnex8q9lQSoJsYNW2sGvYIavtAjAsN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=puBSpCSgeuaoYSgOFhXKZKTaHEaOoTeUTkRXYBDR-6uLNSfrEJjXz0yRn7tsp7dqj6NOeM3o35z9OaJWcm3LFRWWPuGIEVv4NKMf0Q_rI_NSSfgubD1zHq4uTFsr5sjXYYt8EvHW8CHIBXNYc9Vwr9kovgnipW4Oy81Q7x1LzXXsq7pXHrIHvcRwYkfO073tgiOCYNPr44FcYhwfX9VC5YWn0ZoJF2B3-Axz3OaAdqNathIR4mjnmYlcfrkIMSe3BjDtKAv9b77LK_h6G7Xix4gsy9O4JWsc56Oyqtyxm2A8QiLFxG30bDHbmm7rvoCY0YyQ7MwUPRBD1its5nZlUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=puBSpCSgeuaoYSgOFhXKZKTaHEaOoTeUTkRXYBDR-6uLNSfrEJjXz0yRn7tsp7dqj6NOeM3o35z9OaJWcm3LFRWWPuGIEVv4NKMf0Q_rI_NSSfgubD1zHq4uTFsr5sjXYYt8EvHW8CHIBXNYc9Vwr9kovgnipW4Oy81Q7x1LzXXsq7pXHrIHvcRwYkfO073tgiOCYNPr44FcYhwfX9VC5YWn0ZoJF2B3-Axz3OaAdqNathIR4mjnmYlcfrkIMSe3BjDtKAv9b77LK_h6G7Xix4gsy9O4JWsc56Oyqtyxm2A8QiLFxG30bDHbmm7rvoCY0YyQ7MwUPRBD1its5nZlUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxEhdil6cqXzh35PZwhRDo8jQ5MWVROAIunajw4Yl__fuyFFgT8NKlGr45p-2IbxPPPdCgrbInHwO9RbsylzpAL1LU33jXh3FmYAhJzxWN5DlftfgzgzITOH3YQjMvOhTgQ9-viOubIlwglLWBLjt7Rvfki6YjbL7hX650iXoQ7rniN5yiPc03fegjdkB8QGuHuH2WoIsktDYZ4if83U5lE6J7FehMe8iZQymlQJjBmEZ9fgb9tNn5QISLt4bHmybru4RcrECs4NMkCvmWVm40hBWlSI0AWChwoDrbxlVNXmmxQeDPZ9zCSHb3HOORbmYXIvV2nULkYTKR6er1lVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGxctQFFvofxKk0Hki0IFriE6KkObffhrl4B1KJOCuIqV6-EbT6RO4aA5HQFdLvWHTdxC6JIzWAQ4C6XVz8e-VTKNFJJeEfze2HoOThR-yy1x2gJoBWSZL_isOUxsx-E4BsNVGUIVrPYIgLdpCkaeRj4wOc36wRD54nNI8VwTELUritq1T4i05LgQ4BovCfCap_xxdOqyXeHmBA6gf1EbnZEzvzTwEslhFaF725ZeF0qR3DnMS06wslsEstoz3b86rCotgjchYLBDFC5hguR_Kwcj3ShnOU4sm3L369vySydclNi28WmCMA0n3a8-eYCceTSicDAUwC8uPO_oXilvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=ffh4vy4n-FltcytYdoK5le0qTQB-K-ENe6DxfSeFSOXR1eHkxXF4rYd8h6nsnI32X2dYKKErZplYVqAVLP2RVu7kqyxe2UTLxVrFMq4wd8r47brCO-UUVMpj74NGjIM-4dnlkHvvPUaAuenDzUQf_qd7irbq4Tvl7tFLdjCuWWAOOFi-OzN3GdmTgyuuHKiY7zksFFQmstnTJfKozbcvYDG--cSD-U18svV6b6Gsiprho8AIieKhrVm6jz-Wr5Jkz_yxNSZfR8vV-N_gtECGlVkpPA9FJDp0emHXMgmrOVXLfRSNRHFRuV87Q66nzwy0zoOvMZ3PM5ug--ocrcIm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=ffh4vy4n-FltcytYdoK5le0qTQB-K-ENe6DxfSeFSOXR1eHkxXF4rYd8h6nsnI32X2dYKKErZplYVqAVLP2RVu7kqyxe2UTLxVrFMq4wd8r47brCO-UUVMpj74NGjIM-4dnlkHvvPUaAuenDzUQf_qd7irbq4Tvl7tFLdjCuWWAOOFi-OzN3GdmTgyuuHKiY7zksFFQmstnTJfKozbcvYDG--cSD-U18svV6b6Gsiprho8AIieKhrVm6jz-Wr5Jkz_yxNSZfR8vV-N_gtECGlVkpPA9FJDp0emHXMgmrOVXLfRSNRHFRuV87Q66nzwy0zoOvMZ3PM5ug--ocrcIm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=CS1Ul752HgdiIZA_1CA3Bf84qTbXwDQ_pTkb24Nfk1yxoG1dAWYmX4m_Lh_uFH1hba0I7Ac3MKIHUy0pzviBq3EjiUD1SMUrLzlMdpmRLLbfTtXCaUCds8ACTwDsm1Asprn7_9ZaE3ejUTu6o6jt-sK0j9F2eWzVbNsrU9iKbmzq69EvdbFdoj55uwEE5FCSGw8VBVaGB7McgaUC2PJf1hcUJzoNx1MeyLLxo-fadbfLkd-U9yM_cLKYeZEL7TcEAnatW36sA24xFYcpaDCbQgNmUx7ovWL6vmnBXV431XDnsv-55r6QoI9prDZyWlEv84_npQ02vQGfoTFW9XRB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=CS1Ul752HgdiIZA_1CA3Bf84qTbXwDQ_pTkb24Nfk1yxoG1dAWYmX4m_Lh_uFH1hba0I7Ac3MKIHUy0pzviBq3EjiUD1SMUrLzlMdpmRLLbfTtXCaUCds8ACTwDsm1Asprn7_9ZaE3ejUTu6o6jt-sK0j9F2eWzVbNsrU9iKbmzq69EvdbFdoj55uwEE5FCSGw8VBVaGB7McgaUC2PJf1hcUJzoNx1MeyLLxo-fadbfLkd-U9yM_cLKYeZEL7TcEAnatW36sA24xFYcpaDCbQgNmUx7ovWL6vmnBXV431XDnsv-55r6QoI9prDZyWlEv84_npQ02vQGfoTFW9XRB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moKXk8VjQteeyT84KrN1xq-x7-3K4JKHFC_8uXitNKBQ9XJn5SK4wtZuPCL8jYdv1qcodRNS8dv5T7Z9GCfJo4p8StpkF9hM42YU3Pc79ymlklSrWRv6EnQ0kl2raUav1YP2yaD0OQKk3Jzq9ztO2aTWkf99MFc9e6FEzgfA_ecj6nPVwC_c1-scaukgdDdorb3s7nkNXR0iq2EYHw_wae12ix65Nnbdb8nm-qQ3Ic1zC_-wTc9aaXciUEQr80JRf8YinUlbcmFhN8YCoQRYR9vaFGE8lzcaxx5mq5QvPFOWMXpwsz4MD1JYjfAof5CmYX0wKwIeVKMEfvyX3xvz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp5RrHFdMxwFPIgYajxYyXUoqq-MRosqYhO7WiPS80eFgi7OkUo24jDeGh7aA94gWxxLAEBuq2IoEBtVMvyE7OY52o5qkICfPIs_GmPnuolwfUtLqR8xk31XKItW5Lwm12BBWFPO41R7bD-oQNB-IhD1hs2eZEyuFfkTZrX40kl_HmHdcPML1AjGe8aGzNQlYh3UpfR7KGtn41bMBVxN990sNUy86XRdklQoJ0MNkYvDBUUvLAhyty8IzwXHaveUyLc0SNBaCs1gG05GitWqQwV8beXgdTo11wHzTEVq6PYxP9lO02EovWI4rHvF7gVzG5eTCPc1ezU98KsXOgFp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-fMMZQEl46Cqw5yWUXeMFaJ_8LCHEY4dExeNjLCebRvEgcJQHPnBS1pjy5ZuORer2U1v6ZpVg_LqcQq4xTP6l2EJyGDQ6UwJ1q53RcJwtx50mqI0Cm-nEx0oPXQTKqbT7y3n0yq7XliH5fLWrGC8gjvUqBAWpKVDn60Mkzi9Jqz2_atkhJwZiq0kAnkmlVwetfVAKda3_CGrvGwqy6xr4xrHHqH5WAqHkgsLlG0MWpZQfinJB04DLk2T1hX9cF04e3dOMnOkEaUFgyq9k-gVJXGdt0yfjXrbm1hZVh_a7BSfxhlXwuPh2poV8qgTvc3oopntqGRO6WomccdzlgCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=j0laNPQogauEGF-J6D9NEesK8SD_YnoUaRHB03xFH1uRBvMc32jweetfLvlk08iUgTWjqekDnX8rYWzrsubLxEUvQkEuK-LjfOiuQuBS2wvBFAQlNNGely5GIN-5HV0wU6dAumBqVFhYKRPiuFOnfBXs9z80smvnqgi28ViEAw6He80EOmRryHXRXQb6z8Eo_Bt5RnikYhL3DXYfE1nOuDD0zB0a3JQ6tMgk1F6_RXT1dtkZYc75X8ahF_PaIrKgf1Vu39VShZol3PzCW3nxU4MDMq-89YzRTDeZ7ptkwKQo4D0bld9vKu6AuWlqWQnzQBucEbqb-HppzoiAKehMFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=j0laNPQogauEGF-J6D9NEesK8SD_YnoUaRHB03xFH1uRBvMc32jweetfLvlk08iUgTWjqekDnX8rYWzrsubLxEUvQkEuK-LjfOiuQuBS2wvBFAQlNNGely5GIN-5HV0wU6dAumBqVFhYKRPiuFOnfBXs9z80smvnqgi28ViEAw6He80EOmRryHXRXQb6z8Eo_Bt5RnikYhL3DXYfE1nOuDD0zB0a3JQ6tMgk1F6_RXT1dtkZYc75X8ahF_PaIrKgf1Vu39VShZol3PzCW3nxU4MDMq-89YzRTDeZ7ptkwKQo4D0bld9vKu6AuWlqWQnzQBucEbqb-HppzoiAKehMFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=kypPenpwBqjn-IhS6iR9F91O4HpOrwAuMhzLqY_SAmIGaGv647h46yhdkox7M7_UgFhEy1x2HfN-wkPHT-YZyTGimBEVbOu-2Efwzs6ZU4lUpjMXZ6XVGTPdN1RR4M74Oiyd2v0iVNYsOkWSLOipHLrf4ye8bOtQSn7bkNv4ysR6J7aNqFlfrwefVEDuLc92NXNkXqtE1e3HSCzQQKxwR7lCP_JwJbhYNrtysNjjRn_upyQ6dc2watVmJ8Cw3C0zT6QH39Tl0kJC7TjUvWGQMKItSNs7eIzVumbjEN0JsXv0u_W87YkXYwYON4MWS5UjWoHn_rs6xkoBdJH_TS5kfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=kypPenpwBqjn-IhS6iR9F91O4HpOrwAuMhzLqY_SAmIGaGv647h46yhdkox7M7_UgFhEy1x2HfN-wkPHT-YZyTGimBEVbOu-2Efwzs6ZU4lUpjMXZ6XVGTPdN1RR4M74Oiyd2v0iVNYsOkWSLOipHLrf4ye8bOtQSn7bkNv4ysR6J7aNqFlfrwefVEDuLc92NXNkXqtE1e3HSCzQQKxwR7lCP_JwJbhYNrtysNjjRn_upyQ6dc2watVmJ8Cw3C0zT6QH39Tl0kJC7TjUvWGQMKItSNs7eIzVumbjEN0JsXv0u_W87YkXYwYON4MWS5UjWoHn_rs6xkoBdJH_TS5kfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=drQxeuYmbkWZ6jzHJ7Bd7SB8DooFu0D47Z6pmr_zqD0QXrkGanruHKs-smbz-aemqW-bQrN2e7ahg8_MG1dsdxLJSqlW47CdSoE82Nk5WFP7zTdaAvq1j0hsy59WOtpFJUbb80JtJLQSdzQmcdRTF4rnxe7hxdioM6ODxvLqptuz_hXQrfst-GeE5dKMnNkLbZgoEzlMq2q2WHCSydRzmH1dYU0iM62xuMiAjxMfjR53d0dytIxPR4ID3NyXpK1OzO8_7l4n-OSAZG2b2V7dA73ni6VF0NlpC2b_gE7LjYtEC8oaMXxmyZuB-ZsdwJ7Ff3vk1Q7N3x2iPAmG9E-2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=drQxeuYmbkWZ6jzHJ7Bd7SB8DooFu0D47Z6pmr_zqD0QXrkGanruHKs-smbz-aemqW-bQrN2e7ahg8_MG1dsdxLJSqlW47CdSoE82Nk5WFP7zTdaAvq1j0hsy59WOtpFJUbb80JtJLQSdzQmcdRTF4rnxe7hxdioM6ODxvLqptuz_hXQrfst-GeE5dKMnNkLbZgoEzlMq2q2WHCSydRzmH1dYU0iM62xuMiAjxMfjR53d0dytIxPR4ID3NyXpK1OzO8_7l4n-OSAZG2b2V7dA73ni6VF0NlpC2b_gE7LjYtEC8oaMXxmyZuB-ZsdwJ7Ff3vk1Q7N3x2iPAmG9E-2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=f14_Wavni3CZyHEldcH3Im3-Kna_lDuxd2-ktkBnw5OKMrLf6LP3QUq1V_DiB2RE-SSF90x1JWCZ-OvP-HTCSOlA7HdTywZa00dyV6w_REnD6he1jENw2VO5wdOYIykejvn1DUgLa2yEu0OXMDHYb5jCvV15U32qzMWwD5QTO5GdBy9d1KDUlqS99n84k_7kptx7tbrRkzKRjTWCJZkhzFWR-cX4EITSnO_UHmwRpqxWcORWA2JAOcW-aQ39omOZ8yfWTVgCdmi2MQF_blPIEHajQqHjCN6Jh3qIVxyNGHD6hoL-KIicJHag4ngHlqTou9l68IhDk1M16g_BhT80KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=f14_Wavni3CZyHEldcH3Im3-Kna_lDuxd2-ktkBnw5OKMrLf6LP3QUq1V_DiB2RE-SSF90x1JWCZ-OvP-HTCSOlA7HdTywZa00dyV6w_REnD6he1jENw2VO5wdOYIykejvn1DUgLa2yEu0OXMDHYb5jCvV15U32qzMWwD5QTO5GdBy9d1KDUlqS99n84k_7kptx7tbrRkzKRjTWCJZkhzFWR-cX4EITSnO_UHmwRpqxWcORWA2JAOcW-aQ39omOZ8yfWTVgCdmi2MQF_blPIEHajQqHjCN6Jh3qIVxyNGHD6hoL-KIicJHag4ngHlqTou9l68IhDk1M16g_BhT80KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IurBklA5MUwJkAa2hiILdOWpUBXgg1OGelwaWy2TySYv76fH2QqkqIpV_XsDl30_pGpZ69ra49t4fAwDcOF31s_TWWFa3nFOkUCoxRwRHfi1unoJ2M2F4SuCPYaiYD3h0BhbFiKz_LQSz4ZMem2jTJuMcjBmGpp14fDalp7FZU0ObTfEzETro7PyaTaQTjaV-DyV2Tb0x1c4rT669x3heDNmZZPf8qVeq8eKmVnB6EzjDdYWRkbsRR_CPAY9pcE44ShJ0e7zmnhvj9wol_mb8YrRlXFArm0EMGhBoIBqay1Elu5aipdSEATQmSAqOJU9XEgks6u7RMSmTR4LrdTadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=tFy8-hZGyr14cZ63khJ5eTUalMlDZENJKvI9bAxyVz9ntm2FyOyXKUzOn9swToDItLp_xB58WxdvlhEsOVjIFtl5Np94USQNA3qSgBvSI4gi45CPePh-vdN2qiM8yaoW8MMmNoJrWAg4wgH9MRKtzGGiO0jyZNELBElhwdo0_XtL-Ea55CsKEhPUjyJf_L9_Xbd3_1AmINgm1FSoWJoQ7upISCK7tODpWF10CMJ8DQ7yfej1F_2NItxr0t98Ovq3jtP2aA4xfGmlWAKyRlwkHo9Vigchr8VYTVm4jD3G9vpUnmvpnwruUnd40nK8Tikl55-28QCWVM28nowVAk3WYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=tFy8-hZGyr14cZ63khJ5eTUalMlDZENJKvI9bAxyVz9ntm2FyOyXKUzOn9swToDItLp_xB58WxdvlhEsOVjIFtl5Np94USQNA3qSgBvSI4gi45CPePh-vdN2qiM8yaoW8MMmNoJrWAg4wgH9MRKtzGGiO0jyZNELBElhwdo0_XtL-Ea55CsKEhPUjyJf_L9_Xbd3_1AmINgm1FSoWJoQ7upISCK7tODpWF10CMJ8DQ7yfej1F_2NItxr0t98Ovq3jtP2aA4xfGmlWAKyRlwkHo9Vigchr8VYTVm4jD3G9vpUnmvpnwruUnd40nK8Tikl55-28QCWVM28nowVAk3WYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6XKueJJw-lEfPcLTohkkb5dur3pPLKNls6EuHO2kXF5Sy3Wudtr4cFF4lsUW45_WASkEWbNe1GUirG2JYLrfuZRrawoBZp9SGs-U_ZpvRHD-zh0WuHKaYe-AlmS3nbUPzaYzMKJI27n-TUnbpENRKyJ9UCupbGUgsmXv2lMP_1WXRu472ZOncPgrBoZt_sdQ57djoq4OlVyMM_6u8Cz5qRlERHWCL2leRJXT4M8JPgDCABJ03FNeX9K58wqb_E81j_7r8_s24FBtkekIfdivxkAVkGsLcmpwt0sdr3MmWvY96zdzYmlOBYzmGXqHmr5joe9AaVPuK5XVNXcqso7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0W9Q-JOUR8rhGreqfSkIsJLDwHLHKw7KSsgjG65Pc0DsNlP0fNJfJavLT_QzYPeGrFrxC2qkVrLRe7vcEdemoom5QPWqtKZUh0mlS2ImfNfUSwIGtgAfp2QLc0UHFdrx2JeWKutxT7HaGegcdl6pbEz2WLKsMM1Uc3LVZHWEH7sTheOOrJC6csQ0LY0pLhpiFQC6zKYzOglkiMAodc_40HAyBfCY2UgSOJUNcKg85-BWuV7Xm7MelrtYWgrZjdzzyhcCGSfVhCQoUd3uSXU2zcj4nmGI-PwHOSLD63d9zjreEYkCVui7iOvcsDaKhEliTgnuBcXkl2hKJp7-mqRFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ccb3nlmZGUbG-mZUHSHxOaoHBVtK6TaPQ_0V5k-qTCobA-1V1CJ_jJrovJG9Om7YNnYnGGidVf-q2z0N61xoIE2Aklt2yF1kQCwJDogyz6U2ml2IKB_p6RHEduoiC8HSdXg5afF1UzZLi1-jZzTVyV0fiEGlPwi7ZAbygHzvBwZadhwE2GdW6WpkkyPXVDW86PMUtrhhbXXYc4qa_QsCmtOENX8Wx-Z3RmFUME1VzP7HjNm9vgwaWyr3Jh9qlAvKWNRBWjEZveWgL4bz_QnwCdiEVg48MFPIDtoGgDNfXDedHpcKzMP-Tv3tY3ABlypBRh5no-XTr-0ohAVSs1vVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAL22GiKoZS7mDgat436BBuJ5BaQyRvjtLU2Ylcg54J0HY0vy1HPCw-nSTGvir84p5aSB9R9nsgMdJi3yRkTM9aNZU6r9N_U_A0rdXqV1yLgzklEsUcN66m6Niz4kuu7_1EbbG-8-NPQezt-7NbYujRuWWN2OcEmavIjm0KFuXDdInoX0GMdltMvoXbfGVKf-74ctDRgIJMGG-6qiiZpQGnHDNiRXFv87iAWK8lo8sFWc0k5uZJmku60oahzFKGBFpIinWH34LkklOuw7lDg2EZx3KrZrA85zUBVEiIwB6EnmVQxCndCVDWGe2yetiT2-wmGNOdJbi5d5IQbBA9wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=DjuOIK29Re5Ju9k8aVTXeibbeg_74QLQ8pSLJunOCjoCndLWM3LEj9Tx2-9UQ4oMrXcDM_nrOKvoxsPjuW1sgOYD5GMwVP3jtc6ENptRurkkEmS8XAxc2ICtY3M7ttvuk-nH2r6TuZEuQ5lJogmWTpCIYjz1f6dapiy0gJmuy432PPjsEjsCE5xElOOTle3sPkpCsi6c4iEbLu1Xed7j0p_3nlteExNDkoveb0At0FzJPibMRbDy-UeKsBFLZimppYSeRYCTtP2STUWO33Xz7BGKLaIQ0hbdnuhfrZHr7KcdsvW2d-IZSQ10e2Si0dXLJF43MDMDL9b_h2wk7BGrkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=DjuOIK29Re5Ju9k8aVTXeibbeg_74QLQ8pSLJunOCjoCndLWM3LEj9Tx2-9UQ4oMrXcDM_nrOKvoxsPjuW1sgOYD5GMwVP3jtc6ENptRurkkEmS8XAxc2ICtY3M7ttvuk-nH2r6TuZEuQ5lJogmWTpCIYjz1f6dapiy0gJmuy432PPjsEjsCE5xElOOTle3sPkpCsi6c4iEbLu1Xed7j0p_3nlteExNDkoveb0At0FzJPibMRbDy-UeKsBFLZimppYSeRYCTtP2STUWO33Xz7BGKLaIQ0hbdnuhfrZHr7KcdsvW2d-IZSQ10e2Si0dXLJF43MDMDL9b_h2wk7BGrkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=SJq0tyADT6JJbXOwYaOpzzXWTGTnmYdKurnrXzvloKYACDeBAu4EkEYQEeuLasyFSQQNOKD6t_qxuHkQMoQftCHKBmUY0I7zor_Oy2Pdtc9vPvb1MQXRu0YYyld_wM4xZMX9_CcyM8rzvVn2eY5z35cFIjBMgbVmapPDXAJLlnGbA3AP4ErDIZlci3n8S415nnXRaPFjBz--pENjMjLvH8Iqa9hWHvH9YrjTFqhIwMnZvBYOwKNTJ2qJNtwFFOnzwrc3OU1nN_d6uXI32rPZjAE76j8btLo_JrLZe1ISDOrCmRAHm56sk7ijrmzr5lPzEdVX6Lpd6UiULE9IzmSBk1C-pwdoYLzqAvpSlSZRT9Z4DVAegICXZc1SrBBbI02TN-yAYLyYtDKtb7NWb4hbP6_Ol7rqUDsCVBLBnH_AtCSkKgEts--1b7-Ox6B8BfymVq90C6BD0U069lursyJXaYPO04K8VpTXhRotT3Fy7e82Cr0a5SbHOT_axOhtGFDw0t1fYs_jUSRvKfNSWy3QALRL_lpRAASrXJ896yLu2peZh-RtEQ103Ytobz6MDsRJ7F56-h2lP3iFOsFW3M9dHG2lrxH4LKcGZXx7HhkcD30xZmAXdraW4_sZBsQ9zRQz0q_lTZmebHAFlHA3o4ddGvvEZnkuFIcXqqLf1xKz89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=SJq0tyADT6JJbXOwYaOpzzXWTGTnmYdKurnrXzvloKYACDeBAu4EkEYQEeuLasyFSQQNOKD6t_qxuHkQMoQftCHKBmUY0I7zor_Oy2Pdtc9vPvb1MQXRu0YYyld_wM4xZMX9_CcyM8rzvVn2eY5z35cFIjBMgbVmapPDXAJLlnGbA3AP4ErDIZlci3n8S415nnXRaPFjBz--pENjMjLvH8Iqa9hWHvH9YrjTFqhIwMnZvBYOwKNTJ2qJNtwFFOnzwrc3OU1nN_d6uXI32rPZjAE76j8btLo_JrLZe1ISDOrCmRAHm56sk7ijrmzr5lPzEdVX6Lpd6UiULE9IzmSBk1C-pwdoYLzqAvpSlSZRT9Z4DVAegICXZc1SrBBbI02TN-yAYLyYtDKtb7NWb4hbP6_Ol7rqUDsCVBLBnH_AtCSkKgEts--1b7-Ox6B8BfymVq90C6BD0U069lursyJXaYPO04K8VpTXhRotT3Fy7e82Cr0a5SbHOT_axOhtGFDw0t1fYs_jUSRvKfNSWy3QALRL_lpRAASrXJ896yLu2peZh-RtEQ103Ytobz6MDsRJ7F56-h2lP3iFOsFW3M9dHG2lrxH4LKcGZXx7HhkcD30xZmAXdraW4_sZBsQ9zRQz0q_lTZmebHAFlHA3o4ddGvvEZnkuFIcXqqLf1xKz89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=m2VCb-xzDLUtaUPwpfVH0J_LctgxYleZPUdGcp7X6v3hdwHKpGjHHWBVheSSrwz60ohERWwQz6Q1_8SMqDxCDRR52sDlpN-qG94ARUv-8LSJg15xF0gDveZXxp93jF6XUzEiQSA2yqqCVNoFOHZYfMzeGwa6A1WE6GLLFdwh7DyFPFc4Hw5L69uRTtRBX3SRsfABgBT7DpiXrimpNEUuhO8nT5iS6TPdemXfh3JLHpkHKiBVBE2c861-ycWZB1OGbCPr3awnT-cLif0vqPmdr0NKs3Z8Bk1sJgWvJAVEYWRJ92mj5NsnHPS0KHjTNlXGGzi0t6FvwMHG0yFOgoL5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=m2VCb-xzDLUtaUPwpfVH0J_LctgxYleZPUdGcp7X6v3hdwHKpGjHHWBVheSSrwz60ohERWwQz6Q1_8SMqDxCDRR52sDlpN-qG94ARUv-8LSJg15xF0gDveZXxp93jF6XUzEiQSA2yqqCVNoFOHZYfMzeGwa6A1WE6GLLFdwh7DyFPFc4Hw5L69uRTtRBX3SRsfABgBT7DpiXrimpNEUuhO8nT5iS6TPdemXfh3JLHpkHKiBVBE2c861-ycWZB1OGbCPr3awnT-cLif0vqPmdr0NKs3Z8Bk1sJgWvJAVEYWRJ92mj5NsnHPS0KHjTNlXGGzi0t6FvwMHG0yFOgoL5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=BiA37ahvavbZa1iZI7pSlKSU-SVnRxhBsrOCpx39A6DXa4Nr5Msb5t9iLT34PEKrFsNoRuDzEYpOzygGv_jCQZtD8Db3cUKliLFrAr6A9yKq4-u7W-mHUoXpHcFWvKl--0TzrUKhljiqztB8nFpuqXSsz-JMSgGAZGwmsX0dpYKq2Zobyi7euqU-qFM8-7ao7P_02AHKvzUT8IRqTZSSkTqBQgdWAIxonSt0d4g_LeTlLRzmokb9PWDUHCaaR5z7nPSZeOx9UFa_8FC9G-5BGDmhlUfbKp9lR6RxXFNHOzaE2MD7EZnCS7GdgfSctTxqbce3DEQvE92RKLFUmwUyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=BiA37ahvavbZa1iZI7pSlKSU-SVnRxhBsrOCpx39A6DXa4Nr5Msb5t9iLT34PEKrFsNoRuDzEYpOzygGv_jCQZtD8Db3cUKliLFrAr6A9yKq4-u7W-mHUoXpHcFWvKl--0TzrUKhljiqztB8nFpuqXSsz-JMSgGAZGwmsX0dpYKq2Zobyi7euqU-qFM8-7ao7P_02AHKvzUT8IRqTZSSkTqBQgdWAIxonSt0d4g_LeTlLRzmokb9PWDUHCaaR5z7nPSZeOx9UFa_8FC9G-5BGDmhlUfbKp9lR6RxXFNHOzaE2MD7EZnCS7GdgfSctTxqbce3DEQvE92RKLFUmwUyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkgQnX5rG38qJYRINpckkQ6eavmWis2QNFC1mLAhe1R5T-9QTimeQrvVJ-eJLjc2xam7nxHGA7oeC_PhRu6lrQIjixwdinQ65cjx5DsJkLx50KY_4k_PlOEg4XoyVMcPxTSUNODd5UVKD4uhhbw6u51CXfChYZkVfoh2WPJq5zskGCpN7GV65iGzDWV54Jg330bT6FcHmL8xcK4maqCC2bU_QkF-rezmXGnPidWVrj9aexDP8DQnVZxTyif9KOMvL6DlAxY6pubb9xVEQeA3xglKVWejxuTH-EfXMSsN3hvttmZm0aj5hvspvDGqZwL5Ho9hjG6aB9gyhKVKJP0Xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPn_Y5zfdh_ggW_OYsQloojypX_Ihm3K__Zgg_CsGhS3hsc8036_ZSFHXd6HGBVC0G2HBdmTckGYEXJ6TQr97-e5jyQ1QgwkrRzsO0kreBDf_9cJJx2AczoVnHblA-Yoja_huPZof6a-gBrV_X1mP30x2DQH2HVJ1IMQvjOr0BB4tTm0p4RcUGtAMLlwk4a6SIqAaxt1w2mZK6GD6qySCAut1GGi270b8BYaFN10XDY2rFltaKP4d-BtMQv6E0XMT8rWVPlVts-yCrfYyf-70h0eLrL06D4c_bs50x6hPUmWw-IxgYV0L6vpzm_BRF2Fxiay7CeWsdAEbEyxpBnmEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIa2EgvXv6jNJP0CKJlKwvY6rZHZARva4Cp1qQpQTo40jpaF59GaQlrbJUJr53gvNRgHSkXr7e9ywWRKbMiwdjdi2b1V4BcnaIkp5hejLzbodsi2pRDvPw8CNfETazbXllgX8s2jpOgiF8Z3LLGz3irXrKeBWUPIeutuLgrHLQGf3pdpTaFiJOPS66D0SOGXNUj1mpzktNibfcPAw7eUCJhayh4jWAgGMztsHd3QE1lU0IVBLKWAR3n6IwR5AnQxJu1Mu70kgL6XgGTxRc8wHJ-2PVZnqkUMdQWXXeZHZsBwoJyi74M_HKYAxz5dxYDTSsz3aR-Sdne38xd52XFaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daI3_mREkdOXnqiM-ItH-l4VpNuraqKYnbFSyYe6LtKjhjvCkDtLqRmuiI8pLkZrJYPGaSGRFS5skEQda5vbyxPXH2Ijl4u12jrwYXxYq1FwKyeY_twAFfrbC7szh07oPkJinsihdVjO9xK4P23KYI2SKdmOnn1rmlNuXHvAqDz2XG_uVvm8c0gXuS2vUlyrylXaraV8YJX2Yogg9N7S82YEOe8A-5EW8aqmxvXykcDtwnxwC_IFDsAd3CHx3YGP-baGWhqNREaiJtmz3mMsK6Mwk9_NXyaz1kUbqDFqQEYo7tk9h-1O0ziFTgtzph_ajAnzpgbBXxr2P7CwobfmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7P2rOtzWXPImx2-FlJ9g7jrkyxTH1LX1NTTx9pEguEdyO63-nERbNLsEbLM2nqSJAkAgwNSE3ofnMXXFPyvzXPwrzB0-Uq0QPYCSxHJifuU4E-mZnYczbQ9vaA3Cq-ZCFCjxCw5e8y1iGm2oS0Gmo97YZUlFnEIV1TxpDRsWmar_jHqSGEwig3o8339D9ecM4KeNrwn-6XjgkzwcJcVdV9igldMByPCY6Nzg6xfReu2tSoYcR6GZTahEqpGMkFZLEH-fXAm73SAek_xoWK-3_TClRrGd9PY_70crODUJtinDeIS6x3Vxi8WP49Q86KGBeWsASHxkCA1-yJ4VHqCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sijoM-WC2nW5yhfScZJGwbDmfu2nAP3F1OBMdt8CfnJu6L_q9cAMEHmBcjASsXWqFhB9yBvZ_0AN5W9tSauHO5hIpsteVA1zXk8jcQxoPBeFolEjQ68zWbMcqA1_IZ0VGvTs_1RS7qI9_QGcS1U8BjGQcjGFXJ1Fo2YyxBUgFDmJXqtfpFhZ1tZ5tqqdycloapOwrDe9EXgI2FLM_yu4htWaKQz27cHjxjaVQJbsSI46SErBiQh6cCSe2d4pvS2YGG7mvQb-bX02j5Nq1s3-naf3RPupKUaJ79K6LzeG3H9FBCKF_JiRuJUlBbxF67PxP4z-aw9_lqQntgbirVjIWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULZ7I6k78LQaMhO9Yo7lJMxmr_TZigfdlejuUtHsqzr06b4QvHAAOmBsHfzjgsq8CXALcCWYD6jI1h43M_gnbJYd8OBvDJ-2hVtKxnZ_cQ16QSEILzcYZ_f-iIFMY5ur9_eBBkn5H7BOS-TC8FA7Ji_wExIrzQ4902GfQoXBCpmi8T6-YPbJZPCfCB-nmCdKi1gxKMVRGJkcykcHNw0Vt7tR1VH2k4IrOl-UBmkQs6UmzSY9cbCoXESY8S08wqx6CenFWvD8RfD02vvnY_Ghe5T5ZyK3TQxQ4QM5D36g4XZ7tAMQQCDjqo6wvwt2W2bQkqo_H7PwTzEUfpNZlkPkNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRUnh9MmRHt4zM8UWt4h7FJ1v7Mh5sg0AR1j10Lp7tWwCLxstlZdP8FQ33MwQ5wwDe5pi_jAFyeip-CZXEqjG89Yzvtst2C6mNWhwyXGzwmf_agQnmuRd199ykKZ-Yu1YHgSnLHNl8H6orlMVQf-1J_oH0MiKumbX00i7zmH7T_RQHLBZ07quT8NaCEVXcYTxRZOsTqfb__YwIzumbHQaDV9GTnc71uEVebYnOd7kmv3eOxncJylTak6BidxsZMgxQu3WQ9Iv9jHWg19wLinNypmOhCTcGXmy4oCE9q8M8lEfd6gPuEJBU7tgvzdjAAS1d7cNO0RTsypXVihwAvs0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=BjCJLm5xAsdKcW4jWpQ3RtCmDGM9afcXCqm5DiIMDGnKuH1gZ3mTykex50bNzph4fMrSWGmRGv2eqDYW8xqhLIQI31aCeH2-BwUgB7C3Le9dTln3BU8lSoLr-ztOio2PjWSwGdzpa8zI14LyJ28Qm98t694z3BxqMUsUz9dNxZMLzP1h2cMBRM60XsvdSsl9l04eeNhVL8m0nbMeJAE9vuHbDo6JA5WPA17xURT6BOUAL7Q02GgdKU22YeLrvx08NXUAD-XkK8BKoz_9G_W0j5jq_iSIixHvfd9Q_zJJ5hGKwBNzTMU03h7wa6NBbENshktkafNXs631pmdySuKGqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=BjCJLm5xAsdKcW4jWpQ3RtCmDGM9afcXCqm5DiIMDGnKuH1gZ3mTykex50bNzph4fMrSWGmRGv2eqDYW8xqhLIQI31aCeH2-BwUgB7C3Le9dTln3BU8lSoLr-ztOio2PjWSwGdzpa8zI14LyJ28Qm98t694z3BxqMUsUz9dNxZMLzP1h2cMBRM60XsvdSsl9l04eeNhVL8m0nbMeJAE9vuHbDo6JA5WPA17xURT6BOUAL7Q02GgdKU22YeLrvx08NXUAD-XkK8BKoz_9G_W0j5jq_iSIixHvfd9Q_zJJ5hGKwBNzTMU03h7wa6NBbENshktkafNXs631pmdySuKGqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=geGgRfayUA3_LgYwRqbPb9rmIBBJwRHH_ZzNAJWYewtxL9bxrt45Brf4BOafG_LB8DoW0DY61NCkUTfBM78lfD_8vsdTqRhnO2YyOoWt9Huh_sibuIgazdbfXSlXBhpAQlHMjnUJiMMB6MKCT8qhvZo9sY9fGAYlYJftjSTDLT2FcfZELBg9uU97frwcNOK372PPZUK2UysCBGRBeK-lnJkrkoTkfcncfXuWel5PuC6J_XfMChKQJSsjNfbjO12_YajvNT6o50cttbHXyyKl9Bl5Hlxp-1kM_uwTAdIk1ybf8r35e29d9Wfggjh59ZyirloLvtrkTQwBbhrrn-Jz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=geGgRfayUA3_LgYwRqbPb9rmIBBJwRHH_ZzNAJWYewtxL9bxrt45Brf4BOafG_LB8DoW0DY61NCkUTfBM78lfD_8vsdTqRhnO2YyOoWt9Huh_sibuIgazdbfXSlXBhpAQlHMjnUJiMMB6MKCT8qhvZo9sY9fGAYlYJftjSTDLT2FcfZELBg9uU97frwcNOK372PPZUK2UysCBGRBeK-lnJkrkoTkfcncfXuWel5PuC6J_XfMChKQJSsjNfbjO12_YajvNT6o50cttbHXyyKl9Bl5Hlxp-1kM_uwTAdIk1ybf8r35e29d9Wfggjh59ZyirloLvtrkTQwBbhrrn-Jz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvj8y2z7bbC4COrYKL4t4Y63_lyYWncgNRCdOWrg0CwdYLn6kUpuvHJ9J0WPkRI7Ck9aXwTgT1PVs0TAv1YmPFEzhXMsVlaO1o_w3fCxoGNza9ngWgwkqq5AJw4V2iSrgYXWoOI_xfm8E243rteTJPNjFhGGMpZFYXY5OhkRWszbGJ1a0k3_PtLcbgnWzF0osvm48O4MxFTNCIQ2gbEX_M0lCUWTMkpSJxM1hjZVrEmNhdnVqU0-JIyX1bXsLINFIKpoDj2tWjANL10NihUizcGsyl1pljw8Y8RBkDaxa_HgwbjHs3HNDvm3cLgJ5zEnLeN10MhfFkQU8ZikHKEkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=fs2iD6HgbyXq20rC8XPAYtxKSTvvq6Rpy0n3A60S1YCXYyOzUiuub4No6qSLmgKLWYo1fL5kK2i-lqbGGqBRjA7a3VGbhEvHbv6NCUI8exHUxG_-xO8lmKc3Y-wLbT3IIpqCkx-eUgtugurzijR7pyKwAuvwxE9HloPBNxCmJz-sQ_zk-3eQJcLlED_yd_roMOtcsx8FOkJ4cVWM20kUxgetCxGXgaJZJMyEUnfumwVgEAudIgNQdmAqidXWqU19M4QgFDkvSxJbeDjnrfIotJxo-lEj3U4OywpOzww0VfuCHWcDypFB1dmzxRTACutd70M9Aupkbli6gedIjiIsPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=fs2iD6HgbyXq20rC8XPAYtxKSTvvq6Rpy0n3A60S1YCXYyOzUiuub4No6qSLmgKLWYo1fL5kK2i-lqbGGqBRjA7a3VGbhEvHbv6NCUI8exHUxG_-xO8lmKc3Y-wLbT3IIpqCkx-eUgtugurzijR7pyKwAuvwxE9HloPBNxCmJz-sQ_zk-3eQJcLlED_yd_roMOtcsx8FOkJ4cVWM20kUxgetCxGXgaJZJMyEUnfumwVgEAudIgNQdmAqidXWqU19M4QgFDkvSxJbeDjnrfIotJxo-lEj3U4OywpOzww0VfuCHWcDypFB1dmzxRTACutd70M9Aupkbli6gedIjiIsPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=V-PeExG3aohQqmvqi05JjXfUrWIDzmbaFpcjwXax1wwahdobAzif5zG1BG103NqeNh-wrd-q5nAJvuwITJi1k02T5OEEC7pdcD-N17n4Ytzx7e5wdobASyL--VEiJqdJ3m_8gU2A1sxVooP6FpNIzDtrTG2W6DjphG0ZUqvCwE6OIRqwnTCg-BBf3qQExkWumQNkGYBDXfUlpDokNyPlVlkBuM2UtBl0iRpT3YoIosF1AOtA5Q681noKWIH5_yXo4Eiw-5vyacfxVmaqXGDwjPRnWb4NcHKvTWNiHQbHSt9469caxIopF8_EWgJ1klosh4GB3IbdwjqDbymHb0cI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=V-PeExG3aohQqmvqi05JjXfUrWIDzmbaFpcjwXax1wwahdobAzif5zG1BG103NqeNh-wrd-q5nAJvuwITJi1k02T5OEEC7pdcD-N17n4Ytzx7e5wdobASyL--VEiJqdJ3m_8gU2A1sxVooP6FpNIzDtrTG2W6DjphG0ZUqvCwE6OIRqwnTCg-BBf3qQExkWumQNkGYBDXfUlpDokNyPlVlkBuM2UtBl0iRpT3YoIosF1AOtA5Q681noKWIH5_yXo4Eiw-5vyacfxVmaqXGDwjPRnWb4NcHKvTWNiHQbHSt9469caxIopF8_EWgJ1klosh4GB3IbdwjqDbymHb0cI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PCrcZg_u9t9V4fhAVtiW2sfwtDtmcil24r48271GhkSJhsCBETDxZ18WmiZxqjwhz0Rq7172OAzBfDg4vDT9zN5EPSjIBSnmL-l-AnwO1AnoDLBhlAiQX7-_exnHH0-nVxRUKPf8Hyg5qV5GpbWCtjryL7itizeEIy6T4mFCOgBgKt0DS9_Ny1_4Qv5R5zK3QZwdVIRjl40Ju2RhrRbZUYxPo-Mya60nI9T61FAv2cUwfGoQpcNM8c6HEf6EOw6uabsU2t8EhRQ61ujvU4EeQ0tmUUQcwTS8HMIh4cx8IyVJgDECP0XgKiXsZlETEhS5GT9jcHIlCBTM8wV7B_SdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9q4liN4TMaY3kmbuLE7cCFO4KG7MH50tjJKwbwS4XexDAn9spSL6QU0hLuG2Pe4n8zPOrvnnG65qI2t40kSEfCmCKSsh264CrXT9S3KyDx1k9qraN_FCt12uOrkaxe206A5co-pr81Ew3NuUWLDJNRm0g7YCJTIJczDOrEzQJarXJS27k6xjTB9aXG4mmvK7cJuVOMoVX84tlX9D739JszT4pvnnBrGxOe2rk2O__9QhMm2zkmFMKOMe7oowIDnAAp6IBah6PEWMr_X06RbJ_gM9NMahCi9L-RZN4lKXMqmjEwJoxzJ9pZHNYgJ3dkcZm5e5XRCNsPYRVI9A6Dvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqOn8D-jxEvS0mfwoPlLksw3BGsZwmn1tLJVZcCdR1wg3WNe5ZX21WLPy79FNPA1YdV8D4xa-6F599kgjKaI5TWNnECZBmTLj7IeXy73SF64huvJGUZ40Ak0aCcne_4LCGaYV3NCY6pG-bpHpY5s_BlyHG1_Fs_6dj-YywHoFsC1197SimEgpwSSX8zyhqczxca-GoTcUSOzpAdwaGCFLw2hY-5qEvqfZ9U8Ho288DdjZfix1vzmw5IPzJz8OlF99hJOilnotXjTisvHXGqiflaWmitD3YDOP8SHR6yjZwdZaMKN8o7l0pISeFllwYiNL580L-CoJ22yUYWn16o-DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=EeiBYzLoWMHhnXb7MPg-K7Hg6vzRnuZozqtLgL6gnz5wbnlmfmVLOKz_7HRI9WkUkUDMsDmp6TjvsyDwF8PjdjPxOwdk9kcDNnBAgUCPyiGWMitnPeSDGl0G7bnuW6ufOenOPpC0Ebrh3k-a5IH-bOla-6CzXG0Xb8_alOv9sMdKIrl-gqdydBWYJMfLSgWL5zLN8fP675myI9rdmNYf3291q0re_KKPb7D1VRSSpPlSS8577alexuuI2uH90R36ptY-O38u-gVNcX78kWMHgMVzaKNt_D7kTu0P9l83wI7zUD6eY8_x6yeODEqMy-DTzl8rL7sx0-fjpD7Klq3Zcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=EeiBYzLoWMHhnXb7MPg-K7Hg6vzRnuZozqtLgL6gnz5wbnlmfmVLOKz_7HRI9WkUkUDMsDmp6TjvsyDwF8PjdjPxOwdk9kcDNnBAgUCPyiGWMitnPeSDGl0G7bnuW6ufOenOPpC0Ebrh3k-a5IH-bOla-6CzXG0Xb8_alOv9sMdKIrl-gqdydBWYJMfLSgWL5zLN8fP675myI9rdmNYf3291q0re_KKPb7D1VRSSpPlSS8577alexuuI2uH90R36ptY-O38u-gVNcX78kWMHgMVzaKNt_D7kTu0P9l83wI7zUD6eY8_x6yeODEqMy-DTzl8rL7sx0-fjpD7Klq3Zcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4ibxnyoHIz8aBeeWQIyTVoyaGtr6-_2f8_9XQcnCsog0yO7sEZzgiZotBeSxjudxDP8pLBfNrJLsz4MsX581qmzr-MEWocHN2sfnc029BSJaeGi6m-LGmf-L3R5g_GCFP5XkbrVysLnHF6dtsd1J0v2OKQsXbjzxr-Gq-QR2j8BW3dy7P8e_DGKdEwXm-U2ECeCOBWFzl9inRW7rrdnOBBg2JB0lr6Q2E_AaQPLyZEhPfu7eH_8uH-kXMGTHxU2zXtosDabd__k17KjWK12v-EANfTqR51pC13tmc5yF7y0xPftZGJDrKEHetsHjgQ9kXJJQTCYqwCeptxrPTouFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XP6PAuzPb4-YB9SYfUpwxz7_x37lqPR5NLjyU-24jnUD83V3SiJwNQu67hkvqViSjs_2jJC7QsrFghGEunOk3ZdohJqmcscKrK2a5VutwoA4ysFFKgzJ9lbhOTmGq3fszWkhWCEcBHJPlQciEOtbufxxJmmr9Pv-G4tKmALNnhG3sz7qhCj_nv9vg3ilbZPfKmWW3C_vUkpm-Q3HzZZdZT9fB5VBLVWbrQGCPAI2XEAu-YLw2Rzg7QeIeXZQhOPBm7slVJfRVEPqpI8cLoXkYmWYGyLyM4Uixg3LDH0NvenT-gUg6UwjFOfhhxmsXTm3UsdUuiaomgFge8JndEWSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSlOdx-Q2bdQouz3is6yhakS4Zn3BweO2qJX9VAijMQCaOXk_11thxYrdXdZJcfV3YpZ21MfgbqLAVER4CvrM6crEskghKEKpD6QXQMzThKX0khzlaIB83XfQYvWIrDdCQRWgrnlH9BVuY3DCC8iQ3fu5_h0L8DmRvgSNc2Hnl0jdudkSafqg_VOP_dwvpMKxdrQmcFDXLwciqxCwDIwm-SltBWYWdwX23Y3kShuJa7UsT3jKON7KmMf4-oJ8DKCRHabggscHCKFCCpCcDyPCvIf68JsUJR1kJpjHErYVQIxDccjfvGzibBH5d_ovbtsUXN5oILGm2ZMV3Eji55hAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=lxlOIazA5-lu590mPH5oYl9u4BaZMWlVDz3lE0oMoe-1woA7hE0Eypz9jmSBvk_81oqDycCsEyHNZqVpKr4AWkCmfhg2aBxXUkZVCXTL-IPNuFSrgJwhIyOoX3TJhHLKsMVEafo7cSo_nMVAf-8XDg0C49laaj7GyAS8MvnVbeu1-yDdHMuKYHjISaVRfZ1SkHhQPfvu9K-wJpauahw37hilJi3fxLhtVCxHsxbTxuutJKnx1HGHkPPvhg3KubXgm3GuXTj9jIe1BeX6IUH3J6iIbqzWwfwIYm3dYj2pFifrFb22skX4Hje4z-ANvrVNErFNXgEFAEhkKz9IzKczvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=lxlOIazA5-lu590mPH5oYl9u4BaZMWlVDz3lE0oMoe-1woA7hE0Eypz9jmSBvk_81oqDycCsEyHNZqVpKr4AWkCmfhg2aBxXUkZVCXTL-IPNuFSrgJwhIyOoX3TJhHLKsMVEafo7cSo_nMVAf-8XDg0C49laaj7GyAS8MvnVbeu1-yDdHMuKYHjISaVRfZ1SkHhQPfvu9K-wJpauahw37hilJi3fxLhtVCxHsxbTxuutJKnx1HGHkPPvhg3KubXgm3GuXTj9jIe1BeX6IUH3J6iIbqzWwfwIYm3dYj2pFifrFb22skX4Hje4z-ANvrVNErFNXgEFAEhkKz9IzKczvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=nb6goN18O0LHwWOL6wCdM3SuMzYZ7cOK87UTeZgFDrmB85x444SdYhgg69_eK6Zv33BzcbA1VCAIh_3y1pjGwFY4VcbdNo9wl95AgLzsqNS5qs5yUPkogae_Iqo3pHTeddjgUsFAZWtt6Y_DkTh9NlsFmkI7apI2x9sEnJ3-bKjrGIcJCgebBDhWxygAOK1vABL-h7cb9F4Qw29LebybUezW71wTTtJTWVk6lD1sU1rlEENG4kPydcNW660UoYBqXNw-_zNJqiIPDmS7LTc8MyU9ixjE7VDtWbw_83LcfKfiOO5F9p_eUly_0wpGz4MFNGYQgtMe5xFUhbm1PZcqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=nb6goN18O0LHwWOL6wCdM3SuMzYZ7cOK87UTeZgFDrmB85x444SdYhgg69_eK6Zv33BzcbA1VCAIh_3y1pjGwFY4VcbdNo9wl95AgLzsqNS5qs5yUPkogae_Iqo3pHTeddjgUsFAZWtt6Y_DkTh9NlsFmkI7apI2x9sEnJ3-bKjrGIcJCgebBDhWxygAOK1vABL-h7cb9F4Qw29LebybUezW71wTTtJTWVk6lD1sU1rlEENG4kPydcNW660UoYBqXNw-_zNJqiIPDmS7LTc8MyU9ixjE7VDtWbw_83LcfKfiOO5F9p_eUly_0wpGz4MFNGYQgtMe5xFUhbm1PZcqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=ffk-UgE9IPeC3bruILX-_CFD6JDFKsMUcGzRV9wZf1FEr6-CgNrkjtkKM3O-FzHCUmRfjLlL-PtaL4AWmtpUlWGOblISWoh147_UI05WKceYcu7zRuWP_y69p7Wbf9uhTn2KJDDFq4cXD4qqENbF7kq2Yf8TjHhMWEhXwkTkfWsDNS7cv3vdrwuz0ZF9glxulHGESVZ_4Bi1kywos7hBd4WIZ7-GGIW2Jc4cQX-H2FqCBhdMqmsYVuQZwd6Ko6Ywu7xjdgCcpovjklTxJKqlPgZuRnw60Hgsn5hxIMLigCpwmO_iM4uoMcEQ1BncoQ_6S8bjtluUMK4206ZprT2qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=ffk-UgE9IPeC3bruILX-_CFD6JDFKsMUcGzRV9wZf1FEr6-CgNrkjtkKM3O-FzHCUmRfjLlL-PtaL4AWmtpUlWGOblISWoh147_UI05WKceYcu7zRuWP_y69p7Wbf9uhTn2KJDDFq4cXD4qqENbF7kq2Yf8TjHhMWEhXwkTkfWsDNS7cv3vdrwuz0ZF9glxulHGESVZ_4Bi1kywos7hBd4WIZ7-GGIW2Jc4cQX-H2FqCBhdMqmsYVuQZwd6Ko6Ywu7xjdgCcpovjklTxJKqlPgZuRnw60Hgsn5hxIMLigCpwmO_iM4uoMcEQ1BncoQ_6S8bjtluUMK4206ZprT2qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=TBB6VNDz_wpINwEOCgIXo9i_PpJ23MgRk0skx_u3JSvNmSKZGMOyLkQ5i5-lcO8JkKhwl5cDlim7F6a6Uss7LuPNABXYV946-wiIm1kQoJfwDhR8GpMk0H8vyWuPyxw9cfmfNWTyE0KI-QrEZGQc8IXH3K7GUYhK5QpKeNbPRGzMW3NtQxoJ1Y8_sZ7PvO4piaIT5ej5KQtht8YgME4XHalYIVsv391payYb3ut22DKFANf3bh5evinPPvLNaMWPCQnhQMLtd3QHAKSKCSev7kjXMXprbRr72TpVlmCaAiOvShx2hnRt8gpIjJXP3gKvXfvpu9P8qgmOyDnEAYlfQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=TBB6VNDz_wpINwEOCgIXo9i_PpJ23MgRk0skx_u3JSvNmSKZGMOyLkQ5i5-lcO8JkKhwl5cDlim7F6a6Uss7LuPNABXYV946-wiIm1kQoJfwDhR8GpMk0H8vyWuPyxw9cfmfNWTyE0KI-QrEZGQc8IXH3K7GUYhK5QpKeNbPRGzMW3NtQxoJ1Y8_sZ7PvO4piaIT5ej5KQtht8YgME4XHalYIVsv391payYb3ut22DKFANf3bh5evinPPvLNaMWPCQnhQMLtd3QHAKSKCSev7kjXMXprbRr72TpVlmCaAiOvShx2hnRt8gpIjJXP3gKvXfvpu9P8qgmOyDnEAYlfQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=K1YDnvD7XVrplBd2i8kHM40r8b9Bob7ahhxdevg9mZ00MVS7_F1XzvJr6kjJZxuJRYLaflLu8prsPId6jtp2cNI6aVFyUGnL3WJDM0tSTpDp_cOd1deci_H-cwpOs9w8z_mXpM8BUma-9SlGGnZfpT9sgZuobWyarlpTInq1Xq8QPfaMyfu2EPLI3_PJTXJh1xgHlPJj9lEnbx-MEHSsGwwMG_j7m9qyHz2-92SzqGKr_2CIsBtjh4TfQDB47e3x6K-8SWHUTihx9ndn4Co1GpAo5JqvybR1pdd6-jqqTNplUXDJC7YPHk41Sh8NaIAKG5FgsHwMKDy8W1EVFj51zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=K1YDnvD7XVrplBd2i8kHM40r8b9Bob7ahhxdevg9mZ00MVS7_F1XzvJr6kjJZxuJRYLaflLu8prsPId6jtp2cNI6aVFyUGnL3WJDM0tSTpDp_cOd1deci_H-cwpOs9w8z_mXpM8BUma-9SlGGnZfpT9sgZuobWyarlpTInq1Xq8QPfaMyfu2EPLI3_PJTXJh1xgHlPJj9lEnbx-MEHSsGwwMG_j7m9qyHz2-92SzqGKr_2CIsBtjh4TfQDB47e3x6K-8SWHUTihx9ndn4Co1GpAo5JqvybR1pdd6-jqqTNplUXDJC7YPHk41Sh8NaIAKG5FgsHwMKDy8W1EVFj51zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX2bPBMXdgu99T_6cdnTtwfbfVyhVh1xTuFyrGi5sF_3La-YR_cUlZn8XzA0Aue1gMDZMkO3rYVl6ilR7u9a5RYOlzR5nVqRzLZmDWJCNll0EhcgoQ388E7rM12_omOcT6bAmWgFOzb6g8h6MysRaU5B3-04Ol3jTNYbff4VOZ0IStYk2QGJzy7hgwZsmRAxaKw-CHlC-sxzn-6jRo086r0CU3HsJ3v8ppZhUl9CuRFwz3rhPRM282dAFL20alvNrwOqUK2MWt3cyAhP3OcrjMvf_cV6SNh1sqLh9sOtU1cQuzQ_cL6PVf6_MgLsPXDFAJIng4OfRbmPYOUzktszGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5viTt3PcoxO8XjJChoDpYOW1jSNkEKXdsyxaAFhtbqyP9sWKxwh-KdrVKfsC_fIspfqbc1WoGFvaC22o_GnC-kAdCchVIDfBIGufiJ-cxAXCEXymzB78Xj0tosWTNEaIeMyO_te7vl1u7bNAWyd62489kzCFpLPXW0BA0y0SAxVSh4YLw_vOY9pANC90iLa7I_aP0PBa8LJcrU2vwDRwSrzNqi5qNmQgMir3ZcD9qBNyFKqgmjHjcXPchRXdvNL-kEYVQAMPpSoGT8MR8Upp6GNkwfXULN9Gk8jXoE8PbUoowgpKAowgBI7roTZE5-IocBiig2ojcAh8IJ1qPhrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=Py124tdvRW1onGbieLYB_oaBpv2Dly3l6TR7bkSq7Fk9aLe24nLKguUwzqCGc13LehxOrLl1ivhJjIi_doKS8SuhVIR3VbmXDnnz6VYv59J2kZd4Mk6bDBx6AgWs2gCDL87eotIxMCw3AWlDf3ohOXGrSLos9OEHc276dhNwUWzm15IaZpQbQRXQ3-9Skj0fnxnEp9DPUqjcMKAPj_ZEGBksI5yFIJF50JTCTp508V2iUjbuKaRNb-Ru8FR4dPFLWViude2FvFN3j1ewgzFPBvSFdkCX9853qtI6tYwcLzI-RmsHcX_K8gGW-PQKmEt0pYs8eO-tPO5csfLWad_Gzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=Py124tdvRW1onGbieLYB_oaBpv2Dly3l6TR7bkSq7Fk9aLe24nLKguUwzqCGc13LehxOrLl1ivhJjIi_doKS8SuhVIR3VbmXDnnz6VYv59J2kZd4Mk6bDBx6AgWs2gCDL87eotIxMCw3AWlDf3ohOXGrSLos9OEHc276dhNwUWzm15IaZpQbQRXQ3-9Skj0fnxnEp9DPUqjcMKAPj_ZEGBksI5yFIJF50JTCTp508V2iUjbuKaRNb-Ru8FR4dPFLWViude2FvFN3j1ewgzFPBvSFdkCX9853qtI6tYwcLzI-RmsHcX_K8gGW-PQKmEt0pYs8eO-tPO5csfLWad_Gzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
