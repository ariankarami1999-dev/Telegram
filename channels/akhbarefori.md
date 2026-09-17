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
<img src="https://cdn4.telesco.pe/file/GCnh-bCLnt0Wqg2N7c1X17BohsVdYaVSj7or_mjxLFuS6ZBRCd9pEM-yeb5lwZupsLKjS2Fm_IbVhY8xylyHe5TZVFgPsr7ijObyMjsMHtUFRTZa2QD20b4IqWC4ACrBj0X5AO15Ag38Nt1M9VALkCIJTUulDTN4OiTQAtfCEJ3NjyNxka_Nx8YXTYAFsTxolJzpgtWXdmxqzHAsk8e7pnsBtg53kQKTv1T36oSzirGAo40cUBOh1FV6o58Lc3Ck_Fgd-rrRnkF4liJv1Ig767xZ1IafbLqOzJDi1C9HSTJdXn9hdN87cOdMca9X_ozUl4yX01RknuhowxrEoyIB5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.09M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-690671">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab06e42f5.mp4?token=lHgn1f8lzJp-vyACiuXB_Azyq8aA7FTOhLQhvl9mPDhv8jKUX_r618_PE_l9Pv4ub0WrIBYX_p9cJckriTrtEEIG0er89PDEHgMXQRB8OIDd2YypvNTVcjhAIM122INmE1YQ-TyPdfrqhmKk-FP1P3f2YGxev78fc-qeefUT8w6ece83Eo4wqYMjKdriGdugS27itNkGBq6Jf0VupZpZC0XT20VdAcq4GAOKpH9vs9hdc2OaHVy2TuwbCeYpI4w-ZdtgB0w5LuZugpIQox-pKGxKrxBCO5lH9DOxjigqY05rTYS5whDOLl6dKwmLGyuHrMpZX5YTIf8t3cM9b4XOGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab06e42f5.mp4?token=lHgn1f8lzJp-vyACiuXB_Azyq8aA7FTOhLQhvl9mPDhv8jKUX_r618_PE_l9Pv4ub0WrIBYX_p9cJckriTrtEEIG0er89PDEHgMXQRB8OIDd2YypvNTVcjhAIM122INmE1YQ-TyPdfrqhmKk-FP1P3f2YGxev78fc-qeefUT8w6ece83Eo4wqYMjKdriGdugS27itNkGBq6Jf0VupZpZC0XT20VdAcq4GAOKpH9vs9hdc2OaHVy2TuwbCeYpI4w-ZdtgB0w5LuZugpIQox-pKGxKrxBCO5lH9DOxjigqY05rTYS5whDOLl6dKwmLGyuHrMpZX5YTIf8t3cM9b4XOGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انگلیسی یک سری کلمه‌های جالب داریم که از تکرار دو کلمه شبیه به هم ساخته میشن و خیلی کاربرد دارن #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/690671" target="_blank">📅 18:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690670">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24536a38e5.mp4?token=pZ-EQbd7enxT0_VQbPf1kGREGkt0eB4sSZIPs0XMgxFIxvwRDTnSOJiaHnRcWKUboqEkf8S1QM6WtELaO67RONc3RzvvOgOk-UsrtQTbppKqOjfl0JNFDH1KOmdH3Ww9PdV-cQLusvTlWwLPKGh_V1YBxnNAtXmV0tSxu0YROnFDNEh6I4EijdMnby2sT4AWvO15NPg4en6tgBXn29JR-RQsRX6Tpmxk6oVaA14hQi4UCrXotQ5N5aKM5dt9Jx5vSb2L9o5itsVs5d-aNeHYOk5-cA7Z_uV4OfJDy4vpo2e1QanC_qJGsVerX_24bvy57GoC-ns64AUCddgx1fL1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24536a38e5.mp4?token=pZ-EQbd7enxT0_VQbPf1kGREGkt0eB4sSZIPs0XMgxFIxvwRDTnSOJiaHnRcWKUboqEkf8S1QM6WtELaO67RONc3RzvvOgOk-UsrtQTbppKqOjfl0JNFDH1KOmdH3Ww9PdV-cQLusvTlWwLPKGh_V1YBxnNAtXmV0tSxu0YROnFDNEh6I4EijdMnby2sT4AWvO15NPg4en6tgBXn29JR-RQsRX6Tpmxk6oVaA14hQi4UCrXotQ5N5aKM5dt9Jx5vSb2L9o5itsVs5d-aNeHYOk5-cA7Z_uV4OfJDy4vpo2e1QanC_qJGsVerX_24bvy57GoC-ns64AUCddgx1fL1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدیدترین بیلبوردهای شهری تهران که واکنش‌های زیادی در فضای مجازی به دنبال داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/690670" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690669">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/690669" target="_blank">📅 17:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690668">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346fb64e2a.mp4?token=RZFZ61nF0nxU4A6N0_KutTpICGaWBhPqB2u-T7Q9uFTfRGhvvbd1484Xf_qNK-WPdo6vWC6NwTDImwMIHtkRIGRpFKTMvldD_KHQpMW7rEU_2OEyxIlZk_2TNCSGSQcYsNQAnzIey9qFvGPb-In0jNLXPTDA_NXlvJzuZUgVmrJvEV8Nb3EO3aiJp9jTpct0I9rDI-AKJu8AhTyjXbT8SxOOaSCB5vdYtg2HwwTxFjE_piuAbcnK3NEw6e6yiTIoVQaiMpTe06nFP5k3CcFX7iNwCijVXhCyTnteYDrnbRTb0WEXyDk3kv5RlKT-tHm-UHuFT4aS2NgnIeqZUMHGJ1VonhaxehI-tH64TgFSwxfP057fvL_ur1JjxW-2HHumfolRK8G76Ll-he2Z91Lc4NqXGrLH9pGC7OyXAJolr7IxkrX6khThUT4f8YyLIQfntRzyJxS6K5uSUvuGU_-uM1KwpEygEyRhgunt7nbOjE-ZDp_rT2dZB9_BvHNca70Lezg93H730C-4pxGoc_oZyvXj3QwedmhngxijLxHcBPrKnBTs1OCbgv9E2nUCaL1Llm6zBkAZxggtxoBLI28z6sdOIkdZWqcCzPo6jmwTCqea_jGHxfkiVkJSl405CyG5P9TNo3FX39q_xihLSJAemhC0Z0KUen3jdBFZ1rr0rnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346fb64e2a.mp4?token=RZFZ61nF0nxU4A6N0_KutTpICGaWBhPqB2u-T7Q9uFTfRGhvvbd1484Xf_qNK-WPdo6vWC6NwTDImwMIHtkRIGRpFKTMvldD_KHQpMW7rEU_2OEyxIlZk_2TNCSGSQcYsNQAnzIey9qFvGPb-In0jNLXPTDA_NXlvJzuZUgVmrJvEV8Nb3EO3aiJp9jTpct0I9rDI-AKJu8AhTyjXbT8SxOOaSCB5vdYtg2HwwTxFjE_piuAbcnK3NEw6e6yiTIoVQaiMpTe06nFP5k3CcFX7iNwCijVXhCyTnteYDrnbRTb0WEXyDk3kv5RlKT-tHm-UHuFT4aS2NgnIeqZUMHGJ1VonhaxehI-tH64TgFSwxfP057fvL_ur1JjxW-2HHumfolRK8G76Ll-he2Z91Lc4NqXGrLH9pGC7OyXAJolr7IxkrX6khThUT4f8YyLIQfntRzyJxS6K5uSUvuGU_-uM1KwpEygEyRhgunt7nbOjE-ZDp_rT2dZB9_BvHNca70Lezg93H730C-4pxGoc_oZyvXj3QwedmhngxijLxHcBPrKnBTs1OCbgv9E2nUCaL1Llm6zBkAZxggtxoBLI28z6sdOIkdZWqcCzPo6jmwTCqea_jGHxfkiVkJSl405CyG5P9TNo3FX39q_xihLSJAemhC0Z0KUen3jdBFZ1rr0rnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی فداکاری، معنای واقعی شغل آتش‌نشانی می‌شود؛ نجات دختر ۸ ساله از عمق چاه
🚒
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/690668" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690667">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رهبر یمن: دشمن سعودی تجاوزات خود علیه یمن را با پشتیبانی آمریکا و نظارت اسرائیل انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/690667" target="_blank">📅 17:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690666">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJAhamEJ37QQRiYgWATgcmeBh0uOspKMndORr_zfHDWX_UprnkXp1aN9ugorZZSqYAac3KzLyCuFL7UW90zQMWc-QYtfwgt9IHM8JQE-peO6We37aANeIhhsFlY-pTA9csVlgJROmI-k6dT9ad3uWQHtnN2WyzbBI2Ja9GhTtMQYBVDqqskmt6CQvgGxptcWFZuFRYXI4eJNR2jGy_B6Xp-f5tOwlXz11O6b5lSjNeT3bdmk0cL9lLzrgTNuAJRYZJfEVhYszv5gFDI6uZIu3QQIpTCve7ssI1nQsC6hitYCVNKv6NRcbEO6vxWeB5zCDykBim_jw3COoEV11OBaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای کاربردی word که باعث میشه سرعتت بالا بره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/690666" target="_blank">📅 17:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690665">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fd05d5a7.mp4?token=QrfGIa71r-i70lsrXuR4FZyQ9eB7uPM750KpalOlogd7JF9k7AYGRtkyhCJpt_p1Tc6oWiehNMahIx-GOBmheusy6jfRgOZ5AaBWMA0-8c8a_sdtnE6Jkfq7Cfq7KcgvxGWaElkB6xJUz-cOk8ld97Wsv_uj7HsFleYx_8fJd18LZR1V7b7wyIzHmkXIO42oc_Fr1UwmNiGiDidyZkFizLE9v5VhiVYu0clTu84r--aju7At0mQa8oo8U1sd8Qs63KF8gna9uI6QdEZAkC3T0qipQuzxJuef28vw0XS7PfYNJuUlChLPihyNz3hhe92wg-11X1hLcMCWPIZnXnLIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fd05d5a7.mp4?token=QrfGIa71r-i70lsrXuR4FZyQ9eB7uPM750KpalOlogd7JF9k7AYGRtkyhCJpt_p1Tc6oWiehNMahIx-GOBmheusy6jfRgOZ5AaBWMA0-8c8a_sdtnE6Jkfq7Cfq7KcgvxGWaElkB6xJUz-cOk8ld97Wsv_uj7HsFleYx_8fJd18LZR1V7b7wyIzHmkXIO42oc_Fr1UwmNiGiDidyZkFizLE9v5VhiVYu0clTu84r--aju7At0mQa8oo8U1sd8Qs63KF8gna9uI6QdEZAkC3T0qipQuzxJuef28vw0XS7PfYNJuUlChLPihyNz3hhe92wg-11X1hLcMCWPIZnXnLIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر نوربخش دوبلور ۴۴ ساله بر اثر سانحه رانندگی از دنیا رفت
🔹
او به جای شخصیت‌های انیمیشنی زیادی صحبت کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/690665" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690664">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آمار مشارکت هر استان به نسبت جمعیت در پویش جان فدا
🔹
زارع؛ سخنگوی ستاد مردمی جان فدا: استان‌های تهران، خراسان رضوی، خوزستان، فارس، آذربایجان بیشترین ثبت‌نام را در جان فدا داشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/690664" target="_blank">📅 17:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a596aec23e.mp4?token=ZyNXLXeAi4fJhvoDmWfoBwKITFb79Yb6j6f_giM2y2vhigWZffaou4vTPn-beqOCsIjM-yRMzh_NjGeGo7ucChi-LbgloYLwAv34SEF8PP93zg1nWS--oonfHQzl8CHMSbKXQAAIlRU5N5cs4IfKf5HTDR778QYTEbwQl8zfnlovqXgJ0Mj0ucFCTVncJmB2Zgam1vZS_vpsCegj2Y9n873L4hu_6KWHaDR6OP19UFQWoIuXL6UdfIhrv9RKDzblfKpyBduHms03Aj-E6myk1CWTFf25Hp9Ui8-4MOqgcR6C5nS69mle-cQeO2pttdrwzXJNdUhPN7OrC1f9JSHSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a596aec23e.mp4?token=ZyNXLXeAi4fJhvoDmWfoBwKITFb79Yb6j6f_giM2y2vhigWZffaou4vTPn-beqOCsIjM-yRMzh_NjGeGo7ucChi-LbgloYLwAv34SEF8PP93zg1nWS--oonfHQzl8CHMSbKXQAAIlRU5N5cs4IfKf5HTDR778QYTEbwQl8zfnlovqXgJ0Mj0ucFCTVncJmB2Zgam1vZS_vpsCegj2Y9n873L4hu_6KWHaDR6OP19UFQWoIuXL6UdfIhrv9RKDzblfKpyBduHms03Aj-E6myk1CWTFf25Hp9Ui8-4MOqgcR6C5nS69mle-cQeO2pttdrwzXJNdUhPN7OrC1f9JSHSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهد انصارالله یمن در حال حفر خندق (حفره) در اطراف تنگه باب‌المندب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/690662" target="_blank">📅 17:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
متکی، نمایندهٔ مجلس: در این مقطع نباید از مذاکره صحبت کنیم و نباید پیامی به آمریکا بدهیم و پیامی هم از آن‌ها دریافت کنیم
🔹
دیپلماسی همیشه به معنای مذاکره نیست و گاهی دیپلماسی یعنی مذاکره نکردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/690661" target="_blank">📅 17:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBPlFBCHAoBxC-fVWXdNuRnmfPWwi-H-hk6_Tzmj8_Lf89BZPCkxTMcN6fXyJVnIFnda7DQa8ngrgCr42FuYHyrvd3oCLhKseLvilZ-hsarxJJYa10jOcGPknI1Bbkeudm1C8oomk3F1ZZkVo1yVhZuVltEL7T7RRMvYYTrtdq80NsxtiUR6bxObHK08tcW7cTyDvK4g5__RC7vvpk_J6fdWL1gLZGqsf_MH2UT07RDK9yyrmOqgnzxSG7ttMPXZVFnGL22EOXrkJV2t0IljlKHxa_G0G4211_f_ziOdxvX0Mqw0BOxZzYaYv_yemPKEaS5dy_qnuF54Xv_Eb-Ufow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا برای مقابله با ۲۰ موشک ایران، بیش از ۷۰ رهگیر شلیک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/690660" target="_blank">📅 17:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قطعه‌سازان دست به دامن دولت شدند؛خودروسازان بدهی خود را پرداخت نمی‌کنند!
محمدرضا نجفی‌منش، رئیس انجمن قطعه‌سازان خودرو در
#گفتگو
با خبرفوری:
🔹
برای وصول مطالبات خود از خودروسازان دست به دامن دولت و بانک‌ها شده‌ایم، چرا که از دست خودمان کاری برنمی‌آید.
🔹
قیمت‌گذاری دستوری باعث کمبود نقدینگی شده و راه اصولی این است که دولت دست از قیمت‌گذاری دستوری بردارد تا خودروسازان نقدینگی لازم برای پرداخت بدهی به قطعه‌سازان را داشته باشند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/690658" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690656">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز به نقل از مقامات آمریکایی: چین می‌تواند از طریق جاسوسی در عربستان یا همکاری‌های امنیتی و اطلاعاتی با این کشور، به فناوری جت‌های اف-۳۵ آمریکایی دست پیدا کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/690656" target="_blank">📅 17:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690655">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
بلومبرگ: محاصره دریایی آمریکا علیه ایران بیش از ۷.۱ میلیار دلار برای واشنگتن هزینه داشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/690655" target="_blank">📅 17:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690654">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223070706a.mp4?token=IJYSUkxZLZm6X2awbZGDc8vQvRPKcK1tiVQugJl5ogXsLHDGpxwhSCfkkjP0Mgp4wH6-fEwHuQacfKLUo7x8wos0zhGC0tVpKQrDO8abMOd4IjKMDekMI9knsbkrr9VUthvLGHwsDqM_GBWY0x-hDErJRhGyI7UUBYt0J9geeBx6tfJjPJNABuCHlxC1m1MNFsXPO-vnG-rgLXXoeSfrFyp6oKWIWZV8RyR22PadhZcNRQ5jCBUUFk5ZiI0NiwMEY2998a9vQVDAwuNVSqNb5MdUYerhbklaNvBZEjb_oYp-glcb18GE9xAPNytcvuZgHpT062tpZbaISGztnLSFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223070706a.mp4?token=IJYSUkxZLZm6X2awbZGDc8vQvRPKcK1tiVQugJl5ogXsLHDGpxwhSCfkkjP0Mgp4wH6-fEwHuQacfKLUo7x8wos0zhGC0tVpKQrDO8abMOd4IjKMDekMI9knsbkrr9VUthvLGHwsDqM_GBWY0x-hDErJRhGyI7UUBYt0J9geeBx6tfJjPJNABuCHlxC1m1MNFsXPO-vnG-rgLXXoeSfrFyp6oKWIWZV8RyR22PadhZcNRQ5jCBUUFk5ZiI0NiwMEY2998a9vQVDAwuNVSqNb5MdUYerhbklaNvBZEjb_oYp-glcb18GE9xAPNytcvuZgHpT062tpZbaISGztnLSFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از مصرف امگا ۳ چه اتفاقی در بدن می‌افتد؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/690654" target="_blank">📅 17:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690653">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/ رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا
🔹
پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور ساعت ۱۰.۱۲ صبح امروز در آسمان  جزیره قشم…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/690653" target="_blank">📅 16:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690652">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQyDvw3Y-8lLtGkXdoiWgJMjLKZbYU5JeCdzldssK0Zn71uTk0ppJU9trpm3zHM1v3W38IQYJJs3s8qLITZdQsVH3SBMzEYSXIm4v3GpqG7cyu7ezb4xOXenAC7eAX1lPcrPQpt12qy_ena0J9jkEGu-HlUeBV1wE5t5-D82c1irJnAZbauDh_8Z_6B2VbQEx1TEOvv2yUJnRiX38FwWiFpKEmuK27rAZFlzKsKm5AOmUiGAujpnPJc6LJXIHP_HY6rQYJ6ECjVouX6jBICEIFy_wRfNJ3xTuAr5CNT0YVVMmepYaeRC5feuz89WHATOovzXDgio-q1gNy3ZiOxEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلنسکی در آمریکا محبوب‌تر از ترامپ است
شبکه CNN:
🔹
رئیس‌جمهور اوکراین این روزها در نظرسنجی‌ها ۳۱ درصد محبوب‌تر از ترامپ است. برآیند نظرات مثبت و منفی در رابطه با ترامپ ۱۸- است؛ درحالی که این آمار برای زلنسکی ۱۳+ است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/690652" target="_blank">📅 16:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYLla3Z3z5yRqT1yfGfy1lf1rdf6mMavHaLhzupozP9MsrZzTMstReekaOWfHglZsvCx2EA6npiMO4xUdHExwYz5hZGE_-awX6cIXuJj6sHBTsDiWTwbCAN6lCt8O8rLIzjEZq62vjUhopsPXRbAEytNuOSDui2pTSudIDmS6I1VQ6I7amR3-VgRHaiLrS1KeaGi86sfGpoKsKLquXbuy688jZd0U5BsHlbPXsXdY48XGMlKOYGkrg-57qn9NlX6MxZn1W_nkkRLyOk7VLyWEF5HzKbwQatdXRIYgjcENhW7SwQn7ctkH5ARWaD12LpAXdvFT0-M7oik9SdILlM8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaFyPZnOJ0rO4LaXGKhMmXD_mZh9f--FcMH1FEaqQZnRNPiXtCge98R4Av0qo253PZso6whJIFQjWC3gZkoXwrfqJ7gZeYG7oPEDWSbdfA7NXk0Gm4zrBfbYux9M2WJ6ATXJAAS2J5xTVwIFSS2sRo1XwsrEkUcpQQQyJWnHyVBCcb9seKhQetwv0dWfL_Nr9iyx2ZLC619RG3H3LUJaCdzCfwttFiQlmmANBxmNX85XUqpPGnt5ZA6xNWmWLETKXxoJhHvCBYB14ScbMcCgUtf8aaPadNZNP7ocUl4J_BRUR7eP3DTpty4riUrKLYQwg9AsbW2cIE3wrAYixL03oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfFmdXBlOg5QVfobqTJGLKPxCe3Gp1XP4IUECdKIIKDagm-5EsZ1barX_RIwXjxgpMcRpLcPVfK2E4NFZxNBoOegrHW761bAvoXD9haKW7hUGkp4gYgOeOihab1zhGv7a1vw2YzoAyDHWwTHN8pfYcLkJ-LisIVzXe5PouqodeFlJkGR1neCSckhV5jzlEkp_dZngDdfev1c9FrPL_7_hfgxYUmPsnktKdL7CkRgT3Wy4wpbSpn8gUKirkTyBou49hckZWV5Ilrl4FY8P5_e0XJPsKoOxyGZuvgc9BH3U_yOO4cXkpBt6g4hL6WqKnI-FdbjDw4lyg2OIPT0qo6kwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUbVSnGrvOaxS1edYP9dSLn9MQqyao1lna8Dtln-YdFpbH8adokmyLxSgGJzuQ2VrIoot60s6SSRSeG5wgLB89xwTEVNHLFCeEgAL2wYPnYhFs3obk_yWapPR3Nfib2mn3OgdbYW9NU4DD7GwshSJcioodFswU2Z2dsF-maZ5JZC5uRm2IuLF1zbG8yi48dY9gjhv4Q_iyr7knkJjHxiQF0xvorFPbuk20LzxYMtmIQoQLMnDkKE0GdEM6coeJZMxKybrhT5c4MIOJENwHcZZNtikpbM2T4t5wxX8eHA04fhnb8gVk2K91BGzg7NtRCxf6cMkDrQca9yX2GQz2nu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_K2sQPkDEn_hrrc-c2E5kCB-Tnc3iDxpPrdnhaRCg5WCJiuNRuv6K0VOIzD8udfJcV2NCpUJO2kFSc6v9kMooHQjrSt_8vqHMuff1hou9NJClYlIv25zx3Qd1dp3kmq49IReU9RvY3j1jikKTbKssX0d7JCBpMrjPgUii8dSyf1uLo4QoLdnVXN-wNgBESmfGKSdbE0eSfpwI1oBPJ5I_1xNZI87RA7ooYIF6rPWCRSy-87JzeD9DOKgMHu4A1FlwdElh8vLNqThscc6ELIPpnmL27NxTjU99WZej12IgQeGbyqFEs3ujCgA6DfWQum2Ori_f5D26ni51IpQoxvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukH-rgihIka_nhTAupm8D-Nz7uYlPpvTU_zQ5cdsN1-BFttW4xNhT5OuR2swKyZcfKQa3rXDQ7HXxCf9GyBIr4Pg1EDnkrA7rH0qIHSJS2fMPr8Y65D4RsTGQ4hDV2eAA6AHFJR5yadMnZjefIkOiM_ppKkmtPvx6m7LwNG0aVxZwaz5qZrXYuNt09IMv9oV4DIYQ7U8nTZYiYemu4DHiO49sHHVlJa5YD7zF7lb4IscCC01n6TaYsOPBdKE30ubqEfMGdpIwsHmBWRvXp2a7kTdm-jXRmfJquGfCTMjeATNdWDY0GMfn5SJxJSdt7mpcDUdiRk2P7w8-jUci6LVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5rQPiYZUkRH2VMqEk457C0CA90GTTsdBnl661wL40NzwYYjZXOfp7K-3uLxU3oUNrXl2VHnYk6THPHJ6o3Cgxsc-vJLIReLn6wdyBWLx8qpfpalN7IP33fVubnxMjmZzZnsrn_LAdiUn5suBSrI77bTJpwspi9whC3G8XnAx9QUas1g5FzGCA-g6VFeiP106u4J5yrBXJbHgMkIAq_N2p_qYvuFAYq0ll-wBZFNxznDetV-QwhNKlUVmvWbGR1ue3BfyuW3v8kALf0xGAev9qqU5m348YGK-MP-tMoQrmQ3qqFSSvLo3gJYN2ozPWTcnvQBoxJ8CJp7-vrEw8oITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kermSMDvlQ2LrE1hVEZXD44kKVo76QkO2ZahC6R6pEAZZC37rCtIocUAlAKn0HaoBBQNGoumAfWBj8AT-Sj6U5Aq4azavS9lAjQ5oX3zBbe0U9SoKK8Q5VTgekPbngwIOZAnfe6PLa0VVCNMCjhtFadTXMsZFJeTK93W_VUVOTGouBtE380SlhMnB9mVq6TidGMe-DCfGCroibvSskQowARe2agVqDmY3GGqKNSxD6Om831RKiTLZ2qS0TvKpDXKAE8vQ6YL54RHsUPzj1LmCz9HRDWeXX9Ncc0ZgezA24zPWQz2iiG9tBN_kkmjS1Fbb55nOU0MmTE7HZvQIi0Tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi_A-baDoTld80YyP2LeN3zbMOdmXHnmTpcZlULLn4YRaMq8HHY9yJSW1EVBnitchJ1VHRpF-gagUauAtGqzN3xZ406ztNKdMD0_EcqajiySSj6VwBUCbwM6TTsOWYgV7FdTCRjMCRsVlo_s0KYOu1WgBtvs0yD4JvBkWhkbCza4nfyanwJNa9O-J2s2sEE3_B52CHOnLbK_jJhA64PRvhWDcr728_2UCPUrbnCa_2R0NAD_ck5XigzDrJOjE7e1JZjFu7JLOMgRBZXXChMgy09KrSNBxI9-Jz72Vw_J96R-LMjduudaBYUDKhImuiSFMPMh2nI6vqogX9UTUIRPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErbcVtsLy5KMR9Mv4atOJMiqzYingw5jS0rJVv47i0f21QAwHO_t24pWnNiGdB2_TLXNV2i3BoxCpgmILU_gJCc7OTfW2cmWQKAl3XTWrXWghOpYSh0V-XNer05c9IFz5jr7v2gos0vLmmuAE7eMFh2gwo3YTGCfVswlfXIpMIgetyV_6y-al2LkZ1H5pvQi_fk5KktE9r9aGFa-xCLzXvEswAU5b2RIWetxqYxhnPkVO8sfo-Sp9O_9s4ywkmTQbx8h3xfbXIOZgtDmPN-5IkDNmXVOo7GTVsVpcqkCybwbBtzFCSu2cWIUxk3yXLVjL11WZqN8_a1vP-V1860gdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
روایت دغدغه ها مطرح شده از سوی مخاطبان الوفوری هم زمان با آغاز سال تحصیلی جدید
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/690642" target="_blank">📅 16:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-tcoo-Bn5UXqanpw2P5jB8fiRKg1csafdQso1caL_CxqF0bkEZF6oQv4jYVf5E97jx_6qUmLqhsuOAaOeILYnTL9rpNKhvOhJmbiyCz8QLXnNpu1p3mYQWH7-7nJN-qvpbS2WfburZ_fn4l6giIZnoxZiuDcgWCti7NBCO8M5oNLW_qSOoDlhtcvWrVgwTQBgvtYUwCTUcd4-0BT8sP0LJwB-iZcBMwTkn9aEbc-q1V8PCLKjogrXOKbW5ycnv-Rt-Eocm_CcNouNL2Nw9MTj62BsJ0SxzKIB313KM2qsZFtxYds9OwbIgiykN_VUN4TVeW06gPpYwXViqq0NChpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdGJggK5iaahHxT-sz5DQ_vsFT8KuHuFB4KDjNtP0NLVKITLJFI9WYzxf1UXQRbabedaDT_AiIkiHwl69kHnmtaLl1BG5sFlBEq3l5lSa73BIVVG9d4Ois9PR9MlS8UpRmTlzahQB6EZaskQ8r0g_t0bWt_HYCwZ2GWueGdv43U12K6vIgWBKQHF3AxWj51PWOFFaxWaulEiSA-0T5oPLoVCnz9A1FDODmVIyDn1folz-vXQRjktZaLuf-4YXXKQKhPMzXq9C2eV-o9yiyoEtgpJRpGNZ238nm7Pfr5RsRgBggOCeTTEflOQETTM3Kf4F8KfgAkJJuJa5zPIvr3qzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عاملان رفتار نامتعارف با متهم در تبریز تنبیه انضباطی شدند
فرمانده انتظامی آذربایجان‌شرقی:
🔹
ویدیوی منتشرشده از رفتار غیرمتعارف با یک متهم مربوط به ۱۴ خرداد ۱۴۰۵ است که پس از دستگیری فرد مذکور در جریان یک نزاع خیابانی رخ داده است.
🔹
مأموران دخیل در همان زمان، طبق مقررات انضباطی فراجا تنبیه و «انتظار خدمت» شدن
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/690640" target="_blank">📅 16:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwAJ7LGSW6_KFQl0WnFt7OMPgNZKaAnFnR-jupD5ts2WHQH8AfwpVidL2pU6eMwtcCyUt6Guj9yt6PFhDYE6VIOKOM_h_XiH7JdhllmyIlpdooQmcrH-qWwlPAoRxnfVTcNVIb5RSAlvMGimOdzExDf1joc9aZADiuAQGpv3VKkO0A9LQS891XwkGDfPPP-A4jGZd9TbPoA2K_b5XsbAwJfwpfOH3j84F-jjBHknOxhaOHFtOzdrMaq9huljTYkvBbyWVSd108OW4epbEO99QRuUFX4DzNOdKnVp4b_sBipSVlcT73zZwgAh6JEouSMNp14VTnCYz-rQwDUkNO_UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ۱۰۲ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/690639" target="_blank">📅 16:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
المیادین: عربستان از طریق عمان از انصارالله خواست آتش‌بس دو هفته‌ای برقرار شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/690638" target="_blank">📅 16:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNT6O5JAALEz-dKXK8a5Qq7ufn6ao6biJ13IQU4FfaunMZRhJQYv4K8ns-w6TlHgGWLl2HuvkpEIHn2_V4JKHTcLtKhTKIZd2_18C9SvByJjcTSBgZlL3xFBndjbTdntmjwns6t2ESmlD7i-KOtEd8C-QQKFlkGaLC5t1VNBF0bgZhKlrT4NJFFRY-U3-VxXb95Nw2HjwDukJlm6eUPjCCdIJYJ_DyoP9lLOg-40tOKkJK9qRfvXBnG53qxovetYyg6PGR5whoW-4aEpEdNZBTRoTYbwaDEtM0YGgIGsTgrLKbfljAp3u9OhUaH2K18d0WhdNq2B_1XtfopwEKiIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوسه نادر با رنگ‌ نارنجی در آب‌‌های کاستاریکا مشاهده شد
🦈
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/690637" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
احمدی، عضو کمیسیون انرژی مجلس: کارت‌های سوخت جایگاه‌ها به‌ تدریج جمع‌آوری خواهند شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/690636" target="_blank">📅 16:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مشاور سیاسی رهبر انقلاب: تا به زیر کشیدن ترامپ و نتانیاهو، تنگه هرمز را نخواهیم گشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/690635" target="_blank">📅 16:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0629df4d41.mp4?token=F8gElEqYEL0BImC3sz2AJmGiRzm7aUWab3JoqNqtxdC2W6rdOTBSSG5z4YVxzs7q8gbJVEp6Jq5bvkgepgT1QLsMjt4h44bjr1lNZXtb_FwdPs2NIZcYCQXlZ7AQiKrwreDnCvWyMvi0gsPY5FqsP04F3sW_Yyf_nfQP4kfjtTw5RFgURA8oNIywOwvbzMTz7n3c_dginkx3mGE03EZUICWbCvF4RXTx3dN7OU83im1TUqYjmaxTHcOXpn4j6CsemOYgnibVFo_osQmQHyeYkoZcNF5_axH2PgaXiDXWAlJ-GSJt83-RdMk1BSi4LYRd9y-ky1pPsqxFy8q6wIP1r6wGHKZBiP2xbt5sTZAutNwjGOzHu0Yc3NJTAK5ziHGuJrFDGKAUBpamslOnRPl9ltriyVp_qMAvhsaIK1PPloNDBX3oDV4B-L6cLb0di0eRUYjTqgruJ4Vab1QIqdmYYEFQWeuTO7BVLAUTpy_QYlz7XHFl2nJ-dOqyDYCKTz6UHh_LP6Xli9ede9DdzTNuSW4ZahQnfqzYxs1zd6di_SK0VBmVR7u_QHcVyHQm6pRo42DylrRQQ9TOKUbje5nxeyfB5h8mFIVicQsRD8fAWoTzg9yt3v_FOpjglV7zlARnJSmOibjBJLjQIZdgvhiwZG5wmza_6za0vhCkQO2DQQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0629df4d41.mp4?token=F8gElEqYEL0BImC3sz2AJmGiRzm7aUWab3JoqNqtxdC2W6rdOTBSSG5z4YVxzs7q8gbJVEp6Jq5bvkgepgT1QLsMjt4h44bjr1lNZXtb_FwdPs2NIZcYCQXlZ7AQiKrwreDnCvWyMvi0gsPY5FqsP04F3sW_Yyf_nfQP4kfjtTw5RFgURA8oNIywOwvbzMTz7n3c_dginkx3mGE03EZUICWbCvF4RXTx3dN7OU83im1TUqYjmaxTHcOXpn4j6CsemOYgnibVFo_osQmQHyeYkoZcNF5_axH2PgaXiDXWAlJ-GSJt83-RdMk1BSi4LYRd9y-ky1pPsqxFy8q6wIP1r6wGHKZBiP2xbt5sTZAutNwjGOzHu0Yc3NJTAK5ziHGuJrFDGKAUBpamslOnRPl9ltriyVp_qMAvhsaIK1PPloNDBX3oDV4B-L6cLb0di0eRUYjTqgruJ4Vab1QIqdmYYEFQWeuTO7BVLAUTpy_QYlz7XHFl2nJ-dOqyDYCKTz6UHh_LP6Xli9ede9DdzTNuSW4ZahQnfqzYxs1zd6di_SK0VBmVR7u_QHcVyHQm6pRo42DylrRQQ9TOKUbje5nxeyfB5h8mFIVicQsRD8fAWoTzg9yt3v_FOpjglV7zlARnJSmOibjBJLjQIZdgvhiwZG5wmza_6za0vhCkQO2DQQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریجستری موبایل؛ هزینه‌ای که بی‌سروصدا گران شد
🔹
در شرایطی که خرید گوشی موبایل سخت شده، یک هزینه پنهان و اجباری هم وجود دارد که گران‌تر از قبل شده است.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/690634" target="_blank">📅 16:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfdabf7cc.mp4?token=WBk7Pm-l2WPINDVmlsRpurc19-QvjSQ1q0rH57fsQEufU7ClxwVBBcqW_nmvIJbTWhMH3dnjGvM5Ll4PC-O8Phx7uMDFB1UcUuBRL7-wz7PI64J15a-6l8Ko64j42aVUyZdsMYMIRJcw9RY67UGgs6bx6ACnYkBQy4HFdK1a9o9Dt8dOV11CKRtEnYydRZtVFDWRuq_ZBVMKXv6x3J3tVNrJTZRTldI5A9v-BJ6VoZ3ztsMqJQI9YsTUg9GhOVqJorlnHXUtixavu_OGumAj4yN0qhJPhBm60mHmNnEpbUn6CTUPQ6qsR4fZAmlYZOjv3D8eG0WqgMfn95CvwHH4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfdabf7cc.mp4?token=WBk7Pm-l2WPINDVmlsRpurc19-QvjSQ1q0rH57fsQEufU7ClxwVBBcqW_nmvIJbTWhMH3dnjGvM5Ll4PC-O8Phx7uMDFB1UcUuBRL7-wz7PI64J15a-6l8Ko64j42aVUyZdsMYMIRJcw9RY67UGgs6bx6ACnYkBQy4HFdK1a9o9Dt8dOV11CKRtEnYydRZtVFDWRuq_ZBVMKXv6x3J3tVNrJTZRTldI5A9v-BJ6VoZ3ztsMqJQI9YsTUg9GhOVqJorlnHXUtixavu_OGumAj4yN0qhJPhBm60mHmNnEpbUn6CTUPQ6qsR4fZAmlYZOjv3D8eG0WqgMfn95CvwHH4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملک بخریم یا طلا؟ کدام تصمیم بهتری است؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/690633" target="_blank">📅 16:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e19e8cd2a.mp4?token=XloRrUPEsMzvRmgmFkGkXZgt8SiDPKgAhIUPLc57nqGWJMcAaaqOS6z73ww5JQAsmzCsecMKNIA6EFzQMdJmFhbMHQoqgax3uWMBLDZ0vg0T1YutD7vkW4B3tjhJFzVwRsfWputLNHGpDY24PwWu2NirAEi2Y51OyMMISXtpHFhWmNwX5LRFFjy_Zhx6ybJjnFb5OixSSYurf189EkQOVJmYEvt8EXu5Sy-A5zq0gnz42CCjgLOOenZ8EGwWI7C6kWl8pY6Hekl6p24KdkN9z8-MZY9q4OzuiG5nND6HI0s7xEoOF3sl6rg7P3DJyoPiOYfm581LZJjl3yEQAUr4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e19e8cd2a.mp4?token=XloRrUPEsMzvRmgmFkGkXZgt8SiDPKgAhIUPLc57nqGWJMcAaaqOS6z73ww5JQAsmzCsecMKNIA6EFzQMdJmFhbMHQoqgax3uWMBLDZ0vg0T1YutD7vkW4B3tjhJFzVwRsfWputLNHGpDY24PwWu2NirAEi2Y51OyMMISXtpHFhWmNwX5LRFFjy_Zhx6ybJjnFb5OixSSYurf189EkQOVJmYEvt8EXu5Sy-A5zq0gnz42CCjgLOOenZ8EGwWI7C6kWl8pY6Hekl6p24KdkN9z8-MZY9q4OzuiG5nND6HI0s7xEoOF3sl6rg7P3DJyoPiOYfm581LZJjl3yEQAUr4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو: نظام ایران را سرنگون خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/690632" target="_blank">📅 16:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIZhqJpgPVX4RHD-kRQO7m3BmeD3CijZZNCSrZv6IUYZoPSvXyLO2eXf18ao-rz1SXB-COX9vyiGD4pq7X42X07foy2cHH4IyN6jjLSEGZELyGGg3MKIqSVqd_Nv44S7M9t4ZPg8t4XYEV6Rxb9VcHcK4D0iNTkNrLUobqW6y7C0ilvP7FZ0a4qr8HVCsh7kPDQu56xq5DSKlxW26YZ_KdaUJL-SzfbFdGduHCqFLO-iPVYS40d9Iek2lxWVY041dw0OuUFOdA633J4lVNi67lfKXjP1e6UIOgLFltdLkB8nuvfk6tgwlgbtWweUVNbBO0RJc_vmQjcAc49G6xS4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهای جهان که اکنون درگیر جنگ هستند/ هرچه پر رنگ تر نشان دهنده نبرد سخت تر
است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/690631" target="_blank">📅 15:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پلیس فتا: در سایت‌های خریدوفروش آنلاین پیش از دیدن کالا، بیعانه نپردازید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/690630" target="_blank">📅 15:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQPn-M3GiBUIlY3vj4mUPyhSAw0PR4nMYHa_MAQT82mj8bftQyfHUL19cYR83OroyJCp_jlD8chMgRqcwMy62k0ZwqTqFWh9BAGgreLpvS8isOUkpBF08SGeAE2z6LRlE5gr7gc1vN7AW4ygr9BUSGlQPwrunL6GKdTkNpDzYF5ZRKEFc1BI0Ay2togGoH01nGJtWIIFyPtz1qj7RVVth7Joh652HWlW0ETBryrSD3Mb5Oo6foK6yiarbG1z9cf96xWCk0PADT7COJEgjjqep7su9hiFeQTpg6y4_f6Z1YUWOFMY57J5e2e1CKqC-4J1bwaJCZV40Pb2Zpyficxw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d007ce2bd.mp4?token=UoT--RRytwrv_fGXzC_DqtcWS4KIGryO4C7s4sdWpgMyf08z12B8GXkKptAnZCmI1leh3r-6JdcwkVu-SN_Z8YZn7U-FAoCyOXXjlUbkhp1Xeyec7LGBsaOVVEnYW83zovXBbYGne3SINZvrJ7OAHKJfFRm6mcD6K06VzyF3OS1xn_-0gKnsUV8-0xFtNfU3xAOgNxgltF6boPaNJcdLESKQl3B91-8lJflVRYVDvN_nvW2f80_l5CeO1Pye2hA0Bn6WcZ8UdNnUnsu0xRpZCYpucRW2bhJWObxNSNO4Arvq7RZzfp5eyI1RXdEEcr5esHGJ8wddERGsmIz8YUnMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d007ce2bd.mp4?token=UoT--RRytwrv_fGXzC_DqtcWS4KIGryO4C7s4sdWpgMyf08z12B8GXkKptAnZCmI1leh3r-6JdcwkVu-SN_Z8YZn7U-FAoCyOXXjlUbkhp1Xeyec7LGBsaOVVEnYW83zovXBbYGne3SINZvrJ7OAHKJfFRm6mcD6K06VzyF3OS1xn_-0gKnsUV8-0xFtNfU3xAOgNxgltF6boPaNJcdLESKQl3B91-8lJflVRYVDvN_nvW2f80_l5CeO1Pye2hA0Bn6WcZ8UdNnUnsu0xRpZCYpucRW2bhJWObxNSNO4Arvq7RZzfp5eyI1RXdEEcr5esHGJ8wddERGsmIz8YUnMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«قورباغه کرمیت» گونه‌ای از قورباغه‌ است که الهام بخش شخصیت عروسکی معروف بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/690628" target="_blank">📅 15:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cf4fe2cb.mp4?token=vXd45NICxr9f6oVQ4xdNcgDJ-sw7lAMW4GVwl2cvq2uhnXw0x8FOCbEo43E3lFStyMGYv1d-aORo3rOG5Wn6qeuc7qElhnXIZwGo-Yo2DOW_K81Dcc8eq0QpLahJxWcx9j28fnP38Glyi73H4D2DdisWmvIdXaJTKHJ4RHdwyLDl8ATIyQ8sm-oltQ2wzlkvnIjek60rbjNFWfb9Iu7Sx4Aofk0VtVsI6uQTKS0FM7ZFotSt7RLwkIhykl_s4KNWDFWAj3Nf53gZ9ZC9DlyA95D3cSDBz1GmUDQO7DGd7N_UIGVzyRONITAiDB3d7kDOJmdrygAk13KQMHmhzYYnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cf4fe2cb.mp4?token=vXd45NICxr9f6oVQ4xdNcgDJ-sw7lAMW4GVwl2cvq2uhnXw0x8FOCbEo43E3lFStyMGYv1d-aORo3rOG5Wn6qeuc7qElhnXIZwGo-Yo2DOW_K81Dcc8eq0QpLahJxWcx9j28fnP38Glyi73H4D2DdisWmvIdXaJTKHJ4RHdwyLDl8ATIyQ8sm-oltQ2wzlkvnIjek60rbjNFWfb9Iu7Sx4Aofk0VtVsI6uQTKS0FM7ZFotSt7RLwkIhykl_s4KNWDFWAj3Nf53gZ9ZC9DlyA95D3cSDBz1GmUDQO7DGd7N_UIGVzyRONITAiDB3d7kDOJmdrygAk13KQMHmhzYYnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب یک کاربر فضای مجازی به پیشروی یمنی‌ها: «اگر همینجوری با دمپایی پیش برن، مکه زودتر از غزه فتح میشه»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690627" target="_blank">📅 15:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
خبرفوری/ رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا
🔹
پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور ساعت ۱۰.۱۲ صبح امروز در آسمان  جزیره قشم رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690626" target="_blank">📅 15:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dg2SN-fnq5TKQmRINfrvxLKf_kxnnO94E6QY8Wcmz0ZcLVNn63RXhPedt3NyfHS1c21SizIQlsWVkoZN3iY7qJkGH6_sRwwbOw7wNP1yJefMaTMKQp5_Wz3bRB0h-GRn_lKxGnq-6uHju-iv5mjKX-6sG839eTHiw0zc5CK2wmiEt07bg4YNPK3nTPJYHl_Z0NefCl7_mlDB1zpuVB9oL9DnPV3pC7T6ja7gUqU2YunPdI4VvPrPG0UDnmwPOAdlHNrXcDThs-eZskGNGAH0_31CtsZEdG8lNWW-JGCaGIeEGcSdO5q8quJcR7C-6lzdNVpKb7YU3QlIkE8IUPsIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«مبارز با فریب و دروغ»؛ لقب تازه ترامپ متوهم برای خودش!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/690625" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf34568fe3.mp4?token=iVLd7i3F2gb3bylwHAjq8n507Kb2KTJRY2sEDHvdUTy1mlEjs8_z6bGkyrVwxtalQGyw5tritUnT-CF_ZkklrFPNST5DIau0KeyLVDtXwHeLE4XXM8qxlD6g4nmNhbDD4TXZlO-4K3BfJ3Zl88j4u-Y3VeGYBfEEXV4_Tu5fmOZFW7zb9re-Vy0G-gOPo1c1_aFIEify0Rq8qV7o3zWvAd8gCW3n1VJsQ8ecnQX7IpyjbQkRdiUHE-qi5NTCYfVPJzul9gn5GL1POmPE-fm8ImEXo87lLRBYrVgZCxR_Odr2RVOc0DBCMQWHDuhZ8ujSmjE2eXe0fP1YXiCXQ37LgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf34568fe3.mp4?token=iVLd7i3F2gb3bylwHAjq8n507Kb2KTJRY2sEDHvdUTy1mlEjs8_z6bGkyrVwxtalQGyw5tritUnT-CF_ZkklrFPNST5DIau0KeyLVDtXwHeLE4XXM8qxlD6g4nmNhbDD4TXZlO-4K3BfJ3Zl88j4u-Y3VeGYBfEEXV4_Tu5fmOZFW7zb9re-Vy0G-gOPo1c1_aFIEify0Rq8qV7o3zWvAd8gCW3n1VJsQ8ecnQX7IpyjbQkRdiUHE-qi5NTCYfVPJzul9gn5GL1POmPE-fm8ImEXo87lLRBYrVgZCxR_Odr2RVOc0DBCMQWHDuhZ8ujSmjE2eXe0fP1YXiCXQ37LgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکنولوژی جالب یک پمپ بنزین برای دزدیده نشدن کارت سوخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690624" target="_blank">📅 15:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLEZTb53IgOHLONWYnXZhwTup_nltsK5jeajU3lhm0HViruEfJcWbRyBxnS5ok53ZAykPdcgFUHtD3pTFAcY2vO0MZY73GxtH-CfxbrLHFRtfEDYl-zh3mwCsm1omjq5Qn32fMz0Ti_7mCnRmUHoz9zvAmkK4gTyMPWfQd-P5itVy50xQ-kbYwNPiiXir0tU8UHu__CPIR2Xw7zLJDBV7hiwUmdsD1uP6FrBLPan8mubdJyGg2oJYtcFNh8Yk8lEHh3z1GhQEMhbzHreZZUtBS7lXneK9YktGAodeiLgx2A1_9366pfrnjo6hKHEd0mRl0xFnfG0RETtuJZB7LzjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها با چه وسیله نقلیه‌ای تردد می‌کنند؟
🔹
بر اساس آمارهای سازمان حمل‌ونقل و ترافیک شهر تهران، «وسایل نقلیه شخصی» با ۳۳ درصد بیشترین سهم را در رفت‌وآمدهای روزمره شهروندان تهرانی به خود اختصاص داده‌اند.
🔹
ناوگان «حمل‌ونقل عمومی» با ۳۱ درصد در رتبه دوم جای دارد و «موتورسیکلت» نیز با اختصاص ۲۳ درصد از سهم ترددها، نقش پررنگی در رفت‌وآمد شهری ایفا می‌کند.
🔹
سایر وسایل نقلیه نیز مجموعاً ۱۳ درصد از کل سهم ترددهای روزانه پایتخت را تشکیل می‌دهند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690623" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هیئت حقیقت‌یاب مستقل سازمان ملل درباره ایران اعلام کرد؛ «دلایل معقولی» وجود دارد که نشان می‌دهد ایالات متحده در دو حمله هوایی در ایران، از جمله حمله به مدرسه شجره طیبه در شهر میناب، مرتکب جنایت جنگی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/690622" target="_blank">📅 15:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCvK6lno2JGlyxb9n8pZ0p146LZrJMETjWNQE6XIIWAFi3Mx5nru86fnScxILFIOno4Y1keI6XlhmRm5NUTfXsDV7OS-nOSbdWi5NZHiaHhZ1veYDjoYOYg2cbAZOfq7sD4R-qmNGxk2KYzNBqJY2P7HhR9-40QODj8DTTd9VeeAYAyaZb86O0xsP8_vXpoYN6K1Acanwp79lPhzr7tu6mwrIxtfdWQLjjDVBH0sjaWfjdZLyLADv2vrJgg2o5QFZirLUMg8EPUn9ry0rIE7OM-nRuwuGsUt4MRG5QkgEF_a-FoXkiu1qPe5Fb97cNBJx8pTsUjKu_trSFGUWf30PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسعود بهنود تا پیش از نوروز به ایران بازمی‌گردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/690621" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: «توافق مکه» در صورتی که عربستان با حملات بیشتری روبه‌رو شود، می‌تواند فعال گردد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/690620" target="_blank">📅 15:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39774e207.mp4?token=N1jGTK7r2D4mtbWJ7I23mrTASEBI7aZpJ3L268tFZgBV6c2hIo8B-wJT9NdjVoUcZKO_i1BQqCxFhOiSCClQ2Ec7HU6AhSeZ_xygKBgbmmfjR0ajBFVj6FW08Hr3F_imi1P0jpXaMOzLi3kaHivO1TJcCUxgK3r7_nIlT9re7WsipLIKG1gaF-f0D30Uc1TC7U9IGLHYeMRBxOGLHV0KBX8vZhe6yoR8w7nCjGHH2uDHNlRlkacg45Mm7SB2TI9Crdj5iGXp9hp06w9ia2B9KgfBQzSunHNbtP_mpiSE1ucqT5ymg3k6BNVIUQpMwvLbAdg7fikYV8OAGx85O4iuWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39774e207.mp4?token=N1jGTK7r2D4mtbWJ7I23mrTASEBI7aZpJ3L268tFZgBV6c2hIo8B-wJT9NdjVoUcZKO_i1BQqCxFhOiSCClQ2Ec7HU6AhSeZ_xygKBgbmmfjR0ajBFVj6FW08Hr3F_imi1P0jpXaMOzLi3kaHivO1TJcCUxgK3r7_nIlT9re7WsipLIKG1gaF-f0D30Uc1TC7U9IGLHYeMRBxOGLHV0KBX8vZhe6yoR8w7nCjGHH2uDHNlRlkacg45Mm7SB2TI9Crdj5iGXp9hp06w9ia2B9KgfBQzSunHNbtP_mpiSE1ucqT5ymg3k6BNVIUQpMwvLbAdg7fikYV8OAGx85O4iuWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپی وایرال شده از شیرهای آب پارکی در تهران که برای جلوگیری از سرقت با بتن پوشانده شدند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690619" target="_blank">📅 15:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b19e47999.mp4?token=FHRVaQkQOT__tAOaPXHq3Jzru-jBWcprZ81MBHLHbRxFm80HVS_L_U-HkGRkgVyL4dSqXWTaLpaQ7hauCdoBx4bYoCffVd8aR8gAv723XjEwRnjgoFmV21ybp1ZoFUjxas72Yta2tvNecjPKHISRnIXBsIdLz5PQnVmw5QUzJRGtuiJLaRpMay81YYrT_MFHM8r1mV3OOkMD0YsBrh_CSgw08nMxwPlfekSLo_oLOJ3dOBeNphi7l8Dp3BN7y16gteKLqhkCaFIsaYYZ4nlhH40_NPxymEPkiodNaTlne-Lm9bdDfF5tvijEz7Z417jIKpoLltKGrc0mLZVvPURP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b19e47999.mp4?token=FHRVaQkQOT__tAOaPXHq3Jzru-jBWcprZ81MBHLHbRxFm80HVS_L_U-HkGRkgVyL4dSqXWTaLpaQ7hauCdoBx4bYoCffVd8aR8gAv723XjEwRnjgoFmV21ybp1ZoFUjxas72Yta2tvNecjPKHISRnIXBsIdLz5PQnVmw5QUzJRGtuiJLaRpMay81YYrT_MFHM8r1mV3OOkMD0YsBrh_CSgw08nMxwPlfekSLo_oLOJ3dOBeNphi7l8Dp3BN7y16gteKLqhkCaFIsaYYZ4nlhH40_NPxymEPkiodNaTlne-Lm9bdDfF5tvijEz7Z417jIKpoLltKGrc0mLZVvPURP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز هوایی رژیم سعودی به منطقه الحوبان در شرق تعز یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/690618" target="_blank">📅 15:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690616">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhZhD-Wep_nNmUYJMbnwtm2Nv5JlDK-uE3YjHZiW944IKDJnd108aLyWbgp0FHWDpbU7dlUet4JyBhX0UMPrmqK8IoVj44KfTYVFL92sSpGTpQ-MdENvHtkt_xLdPPZ7yfyVEl1ezzohBo_wxq3KhlOctVeH1h7SqF1IAvUKTll_zmLushOLJ1NkeHaOxYUJcPCja5AtfqxTZ0_kP5ofsKTlu4I7-4A-wagDB9QWtm3mGkseG5FAbW0utUjXV9X_hC5XzwieMF-i9gt9M5K0RcM-147t-A8mUgHEQzjSrn7L7FjtgNyYIWeXgquHijOYNaiCSTO_tZfctcYtuSqqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMTiu4gkx3vyo1EYqPb4urSQbkYWTI4FoRHtrYfeuYO62w-4GzDaK1vGVGu9N4Nc33pcB31ARjdeRJsMCZyIIA6ll_9--4qrWRR8lgYvJ5xgXAVc9nYKfoa75KETXp81EGriIZnBLWIIpUtq_ECA052I9LAJZURH8DIqbxuopZUb_tEGlJ8z2O44pUXz-ptuKk4ugYNaqlsgSaR7SvLpEj8c7fPe1Ge2cqF3_zdeH5d4vrz9WVZGZDrYJaXRkRiUz3pqoMpwLgAovdoJP754Rr65QhyrEqNV78OGm6ovvfy65b_cYLIeev9JwlDdCiJ-5NcMI7xvrN8GPciu3QnH1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
علی ضیا ازدواج کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/690616" target="_blank">📅 15:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
وزیر جنگ رژیم‌صهیونیستی: به ایران یا هیچ گروه دیگری اجازه نخواهیم داد که حماس را دوباره مسلح کند. اگر اردوغان می‌خواهد به آن‌ها کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما غزه هرگز محل قدم‌های او نخواهد بود. نبرد با ایران و سایر جبهه‌ها همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/690615" target="_blank">📅 15:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f887250b0.mp4?token=VwKJHarUyc-sCbqI-BHyaEN4TUmux9rKLxPdkv1TRQ1yyhzYo7QJUNarhHatO-PR9lcIOT1Qyxd_Qbhpu17oTPrlEF0EsIrqDHs0zC9meDLibYzOM83TVkhPvjekqo4H_h74tmipjwXlplTy3jqznUy5EMW_CFULUpv9HCQIgfQTclLUgtagOjp6hGg4C_0X9yMPhar-g650RhQBw-LFoXe-eckPXJmkMLUWfnBH6SQmw5BltoJVUOxDnXE-qeYTiBIugDa2T7HeHm8eRzU8pMS_fTsMa4vVjfqLSdDRnkLRc1Q0h9tPebZxzfu2nMC8fXX4L_7DohuJjCrXhtchzzj6aF-YKGk5vLBC2DLZHPl_FRxQaO3Xr1JSiTY0Q0WCURTpPQKyuo_1hLYN-a3huedUs6Rnfbnfrbn7VRtIbbaHOuVBhkS6579LwVKFtWxjc9k_fA87zX1XSzFPkxsO_3PRo0AaoBZpigYcNvpih7x6erHi7RW5oQVx_6bLy9QddSeL8MpmFz96wq488K6J3A_O76qTsQwVqbzneJLSVVKzjuvKGTs9lbyJKglAN4PackQu1MAf6BlRtn7HudA8cjhxtw7D163CEL87DAkmlFWAZtRk-3KRPDn9-UYAai1FYpl91SA9a6cfQttxGP3d0XWzSKg70W89OOvt24plSnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f887250b0.mp4?token=VwKJHarUyc-sCbqI-BHyaEN4TUmux9rKLxPdkv1TRQ1yyhzYo7QJUNarhHatO-PR9lcIOT1Qyxd_Qbhpu17oTPrlEF0EsIrqDHs0zC9meDLibYzOM83TVkhPvjekqo4H_h74tmipjwXlplTy3jqznUy5EMW_CFULUpv9HCQIgfQTclLUgtagOjp6hGg4C_0X9yMPhar-g650RhQBw-LFoXe-eckPXJmkMLUWfnBH6SQmw5BltoJVUOxDnXE-qeYTiBIugDa2T7HeHm8eRzU8pMS_fTsMa4vVjfqLSdDRnkLRc1Q0h9tPebZxzfu2nMC8fXX4L_7DohuJjCrXhtchzzj6aF-YKGk5vLBC2DLZHPl_FRxQaO3Xr1JSiTY0Q0WCURTpPQKyuo_1hLYN-a3huedUs6Rnfbnfrbn7VRtIbbaHOuVBhkS6579LwVKFtWxjc9k_fA87zX1XSzFPkxsO_3PRo0AaoBZpigYcNvpih7x6erHi7RW5oQVx_6bLy9QddSeL8MpmFz96wq488K6J3A_O76qTsQwVqbzneJLSVVKzjuvKGTs9lbyJKglAN4PackQu1MAf6BlRtn7HudA8cjhxtw7D163CEL87DAkmlFWAZtRk-3KRPDn9-UYAai1FYpl91SA9a6cfQttxGP3d0XWzSKg70W89OOvt24plSnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چک بی‌محل ۵ هزار دلاری ترامپ
🔹
۵ هزار دلار برای هر بزرگسال، وعده‌ای حدود ۱.۲ تریلیون دلاری در آستانه انتخابات. اما پول این چک از کجا می‌آید؟
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690614" target="_blank">📅 15:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b5c3313b8.mp4?token=CVsc8vs8NV4i-VJPLaVkjAxObWZ6cW5RVzS6nFbHsSm4wivQ1AV9Dyit1E2qekIDO135TQUi3oVU-m8ckymMvanZxyTjtf-iXNMDExvqNythzLOHN6-SA7WDpMgqVexHSOqCVjMTKKsCQZ6EVJraAw9xfNshTGGFaslGSJ1Gf1lc3XmUK-BAiBUQ-nazuhcsonJ38ZTNHurzzlS5CXRDWxM3mUAWlWoDsmKnXE5O0CtYFZfriIqVD-jMJElMV1awPLSI0ReyS9BL_9ICCiXsO4ldmlVudod3hS7MxT3P4O_v5dDECH2OiG_IqUjRETIwkmsD4ONiv9H-bOVmd67Nuqzubxbi-nVseNZYx5wayWSwUzuOJfaO_9qLonf0wKdLcnBhpkQCBQ8oIP6gMwvsdIAP0AyCnLYMCwhD2KcRmZqg_K41ApEBXHV3jvTi_GZMfAWDrak9QTwe6CQgm_6voysFLIV7ozNhbxeywNHsee_dymbD9T8_rcaWKZ5a_7bMBg3QrOdVDcNYv_fyisKzcrQMNKPXZ9iIXx6sqiNKIDj25yf7nnz-sLbG2JejXW1WA3bX8Xs9EI0DBLO9pWIXzBScNVtLKaFBMB1pdGQkiN3B0gx-yYrXwFZqGuOFhepnR5OuUX9NGHKoLwrKg7UNptu3nYGnSWynDPO-G-NKFXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b5c3313b8.mp4?token=CVsc8vs8NV4i-VJPLaVkjAxObWZ6cW5RVzS6nFbHsSm4wivQ1AV9Dyit1E2qekIDO135TQUi3oVU-m8ckymMvanZxyTjtf-iXNMDExvqNythzLOHN6-SA7WDpMgqVexHSOqCVjMTKKsCQZ6EVJraAw9xfNshTGGFaslGSJ1Gf1lc3XmUK-BAiBUQ-nazuhcsonJ38ZTNHurzzlS5CXRDWxM3mUAWlWoDsmKnXE5O0CtYFZfriIqVD-jMJElMV1awPLSI0ReyS9BL_9ICCiXsO4ldmlVudod3hS7MxT3P4O_v5dDECH2OiG_IqUjRETIwkmsD4ONiv9H-bOVmd67Nuqzubxbi-nVseNZYx5wayWSwUzuOJfaO_9qLonf0wKdLcnBhpkQCBQ8oIP6gMwvsdIAP0AyCnLYMCwhD2KcRmZqg_K41ApEBXHV3jvTi_GZMfAWDrak9QTwe6CQgm_6voysFLIV7ozNhbxeywNHsee_dymbD9T8_rcaWKZ5a_7bMBg3QrOdVDcNYv_fyisKzcrQMNKPXZ9iIXx6sqiNKIDj25yf7nnz-sLbG2JejXW1WA3bX8Xs9EI0DBLO9pWIXzBScNVtLKaFBMB1pdGQkiN3B0gx-yYrXwFZqGuOFhepnR5OuUX9NGHKoLwrKg7UNptu3nYGnSWynDPO-G-NKFXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فکر می‌کنی اندازه واقعی اندام‌های بدن انسان چقدره؟  #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/690613" target="_blank">📅 15:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اتحادیه اروپا با رونمایی از «قانون کودکان» استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۳ سال را ممنوع کرد
🔹
طبق این طرح پلکانی، دسترسی نوجوانان ۱۳ تا ۱۵ ساله نیز منوط به نظارت والدین و محدودیت زمانی روزانه (حداکثر یک ساعت) است.
🔹
پلتفرم‌ها همچنین ملزم به حذف قابلیت‌های اعتیادآور مانند «اسکرول بی‌نهایت» شده‌اند
🔹
این محدودیت‌ها که در صورت تصویب نهایی اجرایی می‌شوند، علاوه بر گروه‌های سنی زیر ۱۵ سال، برای نوجوانان ۱۵ تا ۱۸ سال نیز استاندارد‌های «طراحی ایمن» را اجباری می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/690612" target="_blank">📅 15:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b75213502.mp4?token=LBHZ7WidA2SWUpSFJEV7GvNur23PBDTSC3G4H1VHqu8jbGZW14a5nsIQrmV5sHng0GA6HQoyS6Be0W4cgILyQqupvdOsZM9Tzg_bFwWs34LaUglt6ZeA6injzOq2SYM6r2XPAombQ1PKbBS1X9oqFed7SxliubqWZzDmBGBq6nUL26MFeRS6iO2eSkJ0Hxy8CMllBqw1usKuVWjTAQ_L6lWLUbG1CXc9-e3lZs9tco04jCxcO9kT3xogC2hA24IfvtPxTR2a0jqxaHKxmHqZRFXC_FmzbnNS2yJExAkwTAVG5YYaj5-etL73Dxr02zdSlluLmUAiyfZhQKVOl8ZDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b75213502.mp4?token=LBHZ7WidA2SWUpSFJEV7GvNur23PBDTSC3G4H1VHqu8jbGZW14a5nsIQrmV5sHng0GA6HQoyS6Be0W4cgILyQqupvdOsZM9Tzg_bFwWs34LaUglt6ZeA6injzOq2SYM6r2XPAombQ1PKbBS1X9oqFed7SxliubqWZzDmBGBq6nUL26MFeRS6iO2eSkJ0Hxy8CMllBqw1usKuVWjTAQ_L6lWLUbG1CXc9-e3lZs9tco04jCxcO9kT3xogC2hA24IfvtPxTR2a0jqxaHKxmHqZRFXC_FmzbnNS2yJExAkwTAVG5YYaj5-etL73Dxr02zdSlluLmUAiyfZhQKVOl8ZDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس اینترنشنال: باید زیرساخت‌های اقتصادی ایران کامل از بین ببرید. پالایشگاه‌ها، تولید بنزین، نیروگاه‌ها و منابع سوخت را بزنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/690611" target="_blank">📅 15:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
آناتولی به نقل از منابع پاکستانی: عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/690610" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035fb6a3c2.mp4?token=jkYILkqNhK3xy7qfJGzxgOGFPAHyys8PjUEv6Rzk1rxTwwOOktOFfa_6T0dPZRWUPIxdsEXlM-mIogcHHE6UKnDRJTOjloq-fK8r1wGqvbePi6PQt5r-TCkoQH3W4vVbH7hPRL9NAR_MPGaIH_Hcs3YGzFNvfRuRnhla6Nqz3BIUiAwHSgHGYJDdmrqzUWFzSIN3V9wLd9otZWjdPzaJDNtkKEiR-eG3ZHK1KVimewdCJk9ZmBvfiN5u1TfLuWNGmSI3d6ulG4eB2qjI8ih1c07HZdLicyumhDJxvx_7xhAnzpzPHW5StzAE4ThLKSvKQdSeIsi41NbJkg-CCYdg1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035fb6a3c2.mp4?token=jkYILkqNhK3xy7qfJGzxgOGFPAHyys8PjUEv6Rzk1rxTwwOOktOFfa_6T0dPZRWUPIxdsEXlM-mIogcHHE6UKnDRJTOjloq-fK8r1wGqvbePi6PQt5r-TCkoQH3W4vVbH7hPRL9NAR_MPGaIH_Hcs3YGzFNvfRuRnhla6Nqz3BIUiAwHSgHGYJDdmrqzUWFzSIN3V9wLd9otZWjdPzaJDNtkKEiR-eG3ZHK1KVimewdCJk9ZmBvfiN5u1TfLuWNGmSI3d6ulG4eB2qjI8ih1c07HZdLicyumhDJxvx_7xhAnzpzPHW5StzAE4ThLKSvKQdSeIsi41NbJkg-CCYdg1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین قشقاوی، نماینده مجلس: قبل از جنگ به ترامپ گفتیم ۵۰۰ میلیارد دلار به شرکت‌های آمریکایی می‌دهیم، اما جنگ شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/690609" target="_blank">📅 14:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpr1tZqKWcxl86MovXvUNiWD0PT1RLujAhsVVMpCL-xJnBNFCtpZAwEWQCEQ5RP_UR0HpUehv2b_p9vsXhGxVKyIOx68SkiEponkRk7S6sBWT_0x9QUfSRsEpoRHmd0z5Fua8ZDzoTDM_TD44-RDTdtiOBUrA3_VXehPCCuM4xCpf_61nz7RHYdL6WXDQaP8ue1e83uLdc9gElsGWbaoMihKNlbvvsz1LLA60jUMkXTAtsmXOdPss4OzUVo9w2_KueeCYqHBCeQ0hg909jEDLuPgRteky1PruJKUNzf3_0XPwyqyrvs6xJTRRdo2y3lexta7OqtgqKh9-vhd1kcDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر آمریکایی:
خانم‌ها و آقایان
،
این هم دولت ترامپ
🔹
رئیس‌جمهور یک پدوفیل است.
🔹
بانوی اول یک روسپی است.
🔹
مدیر اف‌بی‌آی با حیوانات رابطه جنسی دارد.
🔹
وزیر بهداشت یک معتاد به هروئین است.
🔹
دادستان کل از پدوفیل‌ها محافظت می‌کند.
🔹
وزیر دفاع یک فرد مست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/690608" target="_blank">📅 14:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هدیه سهراب پاکزاد به دانش‌آموزان در آستانه سال تحصیلی
🔹
همزمان با نزدیک شدن به آغاز سال تحصیلی، سهراب پاکزاد، خواننده مردمی موسیقی پاپ، طبق روال هر ساله در یکی از مدارس اطراف تهران حاضر شد و در یک اقدام خیرخواهانه، هزار عدد کیف و لوازم‌التحریر به همراه پک‌های تغذیه را میان دانش‌آموزان و کودکان کم‌بضاعت توزیع کرد.
🔹
پاکزاد در این برنامه با حضور در جمع دانش‌آموزان، لحظاتی صمیمانه را در آستانه آغاز سال تحصیلی جدید در کنار آن‌ها سپری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/690607" target="_blank">📅 14:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690606">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84498c10.mp4?token=PpYlxysvF--_ciUmNP8qLNZfZgrMTfylOpgxhL6bPkU57R33yRfhuNyw8UwDcD084L3qroYbNOMuJ_-xzcrZqKlBOtn6F2ZwZkXCl-LEzTLkXaXW_dfGl3jQe1ywM29mVFEuny9FrJYWfyAS8YWc80h0F8EeXgFxBWdyDuxDWb2qI2l288cYhZYmLqxjpz5EGh7aoFCs5y7fWOTiyg_2ixyUz3ZdvBoWJ3bU2jgQuSSa8rpumirZRLKWk9Jqt_879882e1aEJkwVqUQiPKTGvirNmyHrIhTs0Xf-b7cUZiEBf4msxYRnGOhrd1WjL94OlYX15rBenJdeO-gVAvr6yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84498c10.mp4?token=PpYlxysvF--_ciUmNP8qLNZfZgrMTfylOpgxhL6bPkU57R33yRfhuNyw8UwDcD084L3qroYbNOMuJ_-xzcrZqKlBOtn6F2ZwZkXCl-LEzTLkXaXW_dfGl3jQe1ywM29mVFEuny9FrJYWfyAS8YWc80h0F8EeXgFxBWdyDuxDWb2qI2l288cYhZYmLqxjpz5EGh7aoFCs5y7fWOTiyg_2ixyUz3ZdvBoWJ3bU2jgQuSSa8rpumirZRLKWk9Jqt_879882e1aEJkwVqUQiPKTGvirNmyHrIhTs0Xf-b7cUZiEBf4msxYRnGOhrd1WjL94OlYX15rBenJdeO-gVAvr6yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا قبول دارید که فدرال رزرو برای کاهش قیمت‌ها، به‌دلیل جنگ با ایران، نرخ بهره را افزایش می‌دهند؟
ترامپ:
🔹
نه، آنها نرخ بهره را افزایش می‌دهند تا شرایط برای ترامپ تا حد ممکن بد پیش برود. مشکل آنها این است که ما بهترین اقتصاد تاریخ را داریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/690606" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690596">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-8BJterMgmEeAOeD8ywMHkDQtGWiMRh7lNGwVJ7gXGl8R5F7lx0P03iUN3bQMjpeSgP3DL6dHhIb3JCupyOqMuh8x4LWBzuAOkBbfsyPwtd-nYym1tF4dO_UUjGhic6Mp0OVdwEjLFVlg9Ryf8mJP_5L7Dg7V3AeU48ms_0Hwmj6uhaUS12mALPWvqCfKgwuQE2QBR0i_STC8FeeODIDfMSjQTYMrVrv3FzgV_ujXhw-V5qJ1scZcCoq4eYIyKATIAAgedQ4LpqmTu5In9r68oaQS6mBkCXtOBgA1D0gR0dEtbojTa0deMLD_YxygjIyKFQgGKR33v-lFpPeGvsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIBBhI4kexzGuBdWfcO8L5orNQNWyW-HluVZc9ZTPDo5yHE88hGYnoXLTY73jNOg-lzysUZRvkAZpBk8lj-ZjhXONAmo2gtIO0m8NJkS5X36cYfrwvjFQMkGjJvejm-e2rL7QZFbpsxawvLPgxFF27icZfhX13EW4LbGEfxFGdlJa3JmVXJXdIPn7kOF7A4-2qOqBEK-kvzhRQYFccJR5o1q5wyLL8-LoQKwzlzH1--jRkz6y1DDdeL46KeBDdl_euY6EY7NhI5V1jaqSG4dykcNTxNxupjUIcOW3WvfoIoW8mCyIakoDewJdZZx8wi3YuKPqCykOd4NGZ9GVxk5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9RVySxyMRsiIp-WnA6S4FRhTXOyJKOd834jOE1ri0AxpBKHZItEB-sRZw6-7NfU7cQWAY7p778FhAjIIoowqK9QdgtjN0ZUH8-E_q_InEjls1Fa8tYmgG-Zhl6KyFrJmKjDicLSzdw76DHQx1gablStUB20oPDnPLz_vxRYWrp-8Ly4JSCuSRZk6J4St9GoQnbJB0C8JYLhFAOrktTVrLmJZ-TMw9S1nofz1NULj-YM9bHIIUdTW99c4ZPsWpSKwm1vd4ZnegiM63z6c0BXs84jw5OKL8lt5FdgpBMKVvmTDh7-lLi4avtcuhZFXgt-2jX9to1NojOE5of1kolcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3Khu40ViVjNGIGGPTOVcjgTKTh5gAqtjiza38X8UX-8_F2txgPxJKr3B54CkBn-uhAJDj0gRZ87emd_0KEDEEr1lqG4wIWeaq-yfULaWD0XAtNPlLy2VxeXdmYLL0wVcs51wYA-RH951Ttc3QvrI8L6NeFb9-5ljBGVwNWm9tRHmrygKBP-TxsP158Ii3c0C_KCCBsuYlNSySBHo1IT-fUoGptzlyo14yCEAkTP3R5dr6e8nxiUyXM2usuAlvbNikQXWOyZyAGyWpsdwIOTOsCEzSj-cgTYE8OhGHjY3S4tZcrgcVmmxDt9zwUHuUmZbU5pSJpHbQbCZkA5fxJWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3OYdaIs_L_3A89exGNp1S1P_Z2V1o9IIOfRVcRq5dz3nmTGvpLNsgLQONV20sk1VlSRun32I8CwXdCvSDBgW9T5y96dd2u9gz734SvKTwCZBKQaDXAPGZJnGHJn7aouDRqgTACncacfLhsr9ElR3eAUgWHBNg3dXHLa_RPW7A1Qrm3isj3gs6KmDqsHaKCI6wI72DgT1wCmOLX7RXV3u9FYlO6T_MIf23_Z-4maehHE5-jcDfmIhR7YJEHM-z78918me-zYezuDtucRDotFoVNjF4r-PeHJt6v7x2AOqPylkkxSflXcmeS0HouXTOGuAnGmW8oR7l8A4bbQ3M6O0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/th18-nWGyTxF29uFckiF9XvnsVCyYRB4dvMmWaUJeNDWOMlN5WTV_9iWvGB3dO4dYpWt0X153XHuEmt7v6XsxgtpPVQjq-WetR91elVCMFpnfwXPfUjKv4PXQdv9O6nehpTS6rLCltp8uxXbLcfQQxrvi0Dr11Q5_MalYB60SLWUy_5ZQXgG_iVJbOPzCUgtx6V6foZ95Nzdeihif9rIeHjRh3xdJm24lyk5YiuV6ByaOU9Zgkh8IrWtEtgp48sWi1skcBVziujuvTD7hebr-kiu_bTqMWI_bpj_CHXNH9f5-0eK_fqlD6AItNOmiUVeAYZoT0FDVxHpHizFJxiNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xu6fwLOv5_2siv2AUGtmTEKn0kjKyCWJxcKEheCj8ZE2g7TZ6BecQqZ6tsZqPAwl9Y8YKGp8xXSj6UnaBTs749J2lIG3IyqptRMZUzB0j6jTBTj3_64L4mQUu4pNRK5ZwTagtFBDLGCKhXQnbOrInoPL3k9d1e0Bcux9_iqjYuEtvc91H03BHATexGIAIW2E5m7b10yFwVzS0UUqzeYXuymNmk8_K3gRoU9f3WBCGxL-yhaGFlDzGy4ABXK2QKxT3O-zTE822lmh03nwQWJTc665zDHhMtfuaCwzL6Gn32OyfRkoFlPgou84wb-IMCToGqkKsAZq-2WgkNKGy43XNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkVYL3syWgiDMPxzLd-TY061HXxNREKut4aGpkkdPQp305t9Im5pStngvm98EU4paExRY8-URIc3A-7Q4itku_3ZNgSLozBSZqp8NX7ElcDKW6ppn_9lLH8SICmY4JhRK37ukvFnqRgG_y2dp4PcgKMdNAaVRv9d7jK0_XLem9g6KFB_tufN6PHqiJ_wwYZ3jYHC3e9OkWrVJfyklWD4eKUlOJf-bSZqUqfkAKQMO0NLS-ZaWR1TrWCghxNiQ68aB3h6Hick4yzHlcvvWbuNy0J58l_ug4rrUPMzULG6OKEqMgc1HyrSa3uwGRMUsnak1A8drcTGASH8fNrsJxbEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrUu4WZCqRkG_LggAuRX19ZOY--P4UxSlCX9wf_UVPneskPO1TwLP8j3WEOjXEuKi83twJK2Z34JBjVi1Awgxsu4QSlG6yxmth1_YaYJ2gzDZ_pFGl3HHG5lk8mpcSw94NHyM2GU-E9St4IdchRLJMoVShPp1Ct-ZfJrc5q6l8rFt2avxcmbXCalwUSV7MZKPPS7hXT91lTGx_5rEa04FMRLFK4jd8MY_NnT7epYup0Q2Y2fupblGapGSkjmSYS3udylsCNmg5fAQiE96a9DzTK2eD-rfohq20L91gXprqvPDoySsov51MahTvWoffCIpMLfXk6O4VM9PvomPOVt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ic25A-JVtJax2W5SmuBo1iTDhT1U9zJiFOwanA6FZJAsElXu_eBLfl0m0QDOwF3lcLFKknJ-iYOZ5mAmZkhl39bOckeBRa0nn2kg6hjGX1MZ8I98jyodsktNtAOuMUqmYiIwnU6FJ4J9uxMbYnxKLwTZ_JhMQucetyt1s8zsXoAqdY4Nk8gQhkLKHE-A1QHvLMg-VyWfbBimLRZ-vHcom5SyRdYygDyyfzjqo1vTDdbXu164u_O0tENygaKFHowsuLC91f05Mjd3rY4qvZ8ks1mXIi-aLHhYG-Zd7OWUB6li5hljsilV5BvUNfZN2VUQAdvMofAfPNOgBOJxPevbQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت شما از سختیِ دسترسی به داروهای ضروری.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/690596" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Adql7peXknPYKiitaDe8lxHoOtFoS62gO0jr97HisPWVyKTRoHJONso8byB9u69uSqcrCVkhtQSRFgyDl0wFeoxEHhLgWwE8IyMjaCFTgEl_av3asFLm8Ec7fy6wjINT9osW6n2vJah0oVASt_zuhttZu8I42qsyQyaDSJswWyn-yXeLQrMtP7WoZRf5nysHU8q8kfFV2I9NfusYZbM1zai9i83wlB9MlOszGo3Mn0M62QvWW_HXi5aFBzYiyCRQpDJ71vc149s4dTQizpl-5NsOPbPkExcS0yejaYCK0WIIExH3MpOyPTDbaGiwmxMQv1EdU2FHvHQKypB6u8F8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین عکس از یکی از دو قاتل پرونده قتل عام ۵ عضو خانواده در پونک تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/690595" target="_blank">📅 14:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690594">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVgbrqYs3MJ_SfOCbr6SuFPwA55wrfpW9WIUFYUmRxB25fdbSxvN-creakhdG2_W8EAD8-dO_wKXdalFSYReaLtMNH-jPUbCTGJAwlDEzYh0awEXBMbt6HYBeBoc_btVdiyIxpPd2gH8kzWu1oy6daw1qW0XOIBycOTCeSEeTo8HJykTd4p4eYVijd_XbbMKAOzBMSuyJrzbzvTxv8QSvW2tCh-8trJlhtpefRR0dqqhSGDHAvK0TCbdY0Mk6X-YbW85k-tAAuf2MvsOviba0GB3GknqtJYhY87rUpvPmC6OgN24zJpnlqKf0yQ_c55MUB3PQfXhJvVJLm5AFMPSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات بیشتر از کشف اجساد پنج زن و مرد در تهران
🔹
اجساد کشف شده مربوط به یک مادر، دو دختر و دو پسر خانواده می باشد
🔹
سال گذشته دو برادر خانواده که پس از سرقت طلاهای میلیاردی به پلیس مراجعه کرده بودند مورد ظن کارآگاهان قرار می گیرند
🔹
در ادامه تحقیقات، دو…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/690594" target="_blank">📅 14:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690593">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7759637e24.mp4?token=BrGhSY7rXZQPXerZN5Jfj8pX9X6amUU1S5QdwkichzI4PfQ4INPtyn1ZC5JqslPcRjP4AcPtnsNoAn_9OhmXGoXu63hdiJba7xWYA31La3UqmQDjBnUeVmFuxxPjf1wx3IBajtQJ3bKhPX4vS-WMZnsQTIzfwlUQv2GiMPxQnceDzTwCU-m-Ta7JI6IRVfe-s8SXn0Uyx0KjVQ2DeXjBpECZhaOpZ-x1kh7hdJofIUiFe-cgaIg-6XFhYiUb7EXZ7UmyPBys0v0DuA8Fv1jj0OyhfbEob4sffQBndHmr8dKH8M4Ej8fljnOY88LDOxL7k77i_P5aFYOdDjimMiXuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7759637e24.mp4?token=BrGhSY7rXZQPXerZN5Jfj8pX9X6amUU1S5QdwkichzI4PfQ4INPtyn1ZC5JqslPcRjP4AcPtnsNoAn_9OhmXGoXu63hdiJba7xWYA31La3UqmQDjBnUeVmFuxxPjf1wx3IBajtQJ3bKhPX4vS-WMZnsQTIzfwlUQv2GiMPxQnceDzTwCU-m-Ta7JI6IRVfe-s8SXn0Uyx0KjVQ2DeXjBpECZhaOpZ-x1kh7hdJofIUiFe-cgaIg-6XFhYiUb7EXZ7UmyPBys0v0DuA8Fv1jj0OyhfbEob4sffQBndHmr8dKH8M4Ej8fljnOY88LDOxL7k77i_P5aFYOdDjimMiXuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش شهروند آمریکایی به افزایش قیمت بنزین: سه بار بهت رأی دادم ترامپ و این تشکریه که ازت می‌گیرم؟ تو خائنی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/690593" target="_blank">📅 14:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203cbac51e.mp4?token=cm7ofC0KabK_fD1SiQ_tAynzzccIyZb_AR-B2cWfOLyw2-zo3tsVlI9a4maiO3CEbTo6gQAygIA0uYek2kjlIKjitBt5KYkVpOnVDdvINJvuQ2-b57XzDPbdPbo-L1CKmISSAHa9lng6WgNWtRU-jaQyff-AMKnKLG1zi5TQEsHPU-zVgcRnd2-e0zfQyM5Id0uUWSQa7QcFNrWXwA9irS7_ODSi2ocuCC7y8_ttTYXkikdTajitbJmUsD_jbB_ZQwUQvT1scE8ErGobWAsyH9Lf0OAbOyziM-ptWl5G1AKv74brK0IEeP_Um1mdFYvxKi4t59mT9DTEjPhM2_IcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203cbac51e.mp4?token=cm7ofC0KabK_fD1SiQ_tAynzzccIyZb_AR-B2cWfOLyw2-zo3tsVlI9a4maiO3CEbTo6gQAygIA0uYek2kjlIKjitBt5KYkVpOnVDdvINJvuQ2-b57XzDPbdPbo-L1CKmISSAHa9lng6WgNWtRU-jaQyff-AMKnKLG1zi5TQEsHPU-zVgcRnd2-e0zfQyM5Id0uUWSQa7QcFNrWXwA9irS7_ODSi2ocuCC7y8_ttTYXkikdTajitbJmUsD_jbB_ZQwUQvT1scE8ErGobWAsyH9Lf0OAbOyziM-ptWl5G1AKv74brK0IEeP_Um1mdFYvxKi4t59mT9DTEjPhM2_IcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مفتی اعظم لیبی: بر مسلمانان واجب است از جنبش انصارالله در کنترل تنگه باب‌المندب حمایت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690592" target="_blank">📅 14:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
زنان سرپرست خانوار رایگان تحت پوشش بیمه قرار میگیرند
رنجبر، سخنگوی کمیسیون اجتماعی مجلس:
🔹
زنان سرپرست خانوار در روستاها و شهرهای زیر ۲۰ هزار نفر به‌صورت رایگان و با پرداخت هزینه توسط دولت تحت پوشش بیمه رایگان عشایر و روستاییان قرار می‌گیرند و در آینده از مزایای حقوق بیمه یا مستمری بیمه مربوطه برخوردار می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690591" target="_blank">📅 14:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxFZgfw0sEQqY6YA9yBKyyosreUvYR6n1rmvh4syta-O7f29qQL-jfsOkpYLnM7abbsNX0hPe30MN5v4dD1WMGT_g8ST9vP94PH1KOYmCYygw1HSZ5OY35FR7YEnQNsA4H8NSwHNR4PXS4YyYrOL0XjplFcfUSQhe-llz76Q0h--lBmAaLZBknQiNYRpo-sGEKnFwlNtxfjyJRpdXoUiy3ukJUsAf61KE8CIOi0Z8RX0nnjBhAyQsWJMAPi8ivkwdi1DgCPCxPazRAnXuC3EpAXFm_qrEln-SHpU7oLLGC2vzCzGI_l4aGsUURHaKkIMT1qasHY_h5p9asVXUzqNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آبغوره را با چی بخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/690589" target="_blank">📅 14:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJLNVkPHQHVNh5PjwxD8DvB50OqaTF0ZG-GNXvGI4LLu_N1wMewH-oJ5DUtaV9dNVHvx9klq9IJLZJp3reSEcW60ovovj-Qh-RnZhzWmdWf1rvsY2KmYLxgXKsFe_XyC2-jzmldxj6iPe2fUbvXNhB-wRcegnEZ0vMileFng1ISO4aX2WHEhKUe8bvuxqucBYmW60PRapk8Rl73-mnR3J5A1TKAfQUWS5PIeGEhJ7dBso8QwrZCAOJw2Hd-HrcT59Zb3pdKPnqcn3K7swpz7tenxjcVe01lLZtoHlysMd8-RQDvNbdcgPchL2WsaBNm2iFrtZ1pXsl1ZyJNa9GjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۶ شهریور ۱۴۰۵؛ ساعت ۱۳:۰۰
🔹
بازار، روز اصلاح قیمت‌ها را پشت سر گذاشت؛ با آغاز معاملات، فشار عرضه بر دلار، طلا و سکه حاکم شد و هر سه بازار همزمان در مسیر نزولی قرار گرفتند.
🔹
در این عقب‌نشینی دسته‌جمعی، دلار آزاد مجدداً به کانال زیر ۲۳۰ هزار تومان بازگشت، سکه بهار آزادی افت محسوسی را ثبت کرد و هر گرم طلای ۱۸ عیار نیز با کاهش قیمت همراه شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/690588" target="_blank">📅 14:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ‌ متوهم: من آدم باهوش و دارای ضریب هوشی بالا هستم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690587" target="_blank">📅 13:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690586">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccf9ef6f9.mp4?token=lyWIUQIwq8x-w2fnCVQa1W5u8r_togBGpg6tH_RAAU2Us7hMxQkPfClMA3kCEiBFUaPEpFlXg5ERhuADme4T3Mu7-zrwXyddO5IHMIF3mJvVH5kaWCrzR2EoT-qMQaw4BKhZWGB-T8inTggYq8MKCeI6pQocWPyDNdRO7gCGmokadjpXc_rkV5I61jlCv6rznkUBOeyXqGiZu4XvE_P9OpKJHR7X23saoZaDwDpar4R78cGHF1aPpqgAvQHs1W0TCm1KBHLUR9on3rsYBpotBHjzZuEE4hxs6p1-bcZEXNCG5qvHDv3w2Ktw59_FaAZbMdbGyzSdjpe27FD_8l2HAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccf9ef6f9.mp4?token=lyWIUQIwq8x-w2fnCVQa1W5u8r_togBGpg6tH_RAAU2Us7hMxQkPfClMA3kCEiBFUaPEpFlXg5ERhuADme4T3Mu7-zrwXyddO5IHMIF3mJvVH5kaWCrzR2EoT-qMQaw4BKhZWGB-T8inTggYq8MKCeI6pQocWPyDNdRO7gCGmokadjpXc_rkV5I61jlCv6rznkUBOeyXqGiZu4XvE_P9OpKJHR7X23saoZaDwDpar4R78cGHF1aPpqgAvQHs1W0TCm1KBHLUR9on3rsYBpotBHjzZuEE4hxs6p1-bcZEXNCG5qvHDv3w2Ktw59_FaAZbMdbGyzSdjpe27FD_8l2HAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: به اتفاقاتی که در مورد ایران رخ خواهد داد، توجه کنید. این موضوع به یک نتیجه بسیار خوب خواهد انجامید #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/690586" target="_blank">📅 13:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690584">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
تعریف اجمالی از پویش جان فدا و استقبال مردم و تعجب پوتین از این پویش از زبان سخنگوی ستاد مردمی جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690584" target="_blank">📅 13:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690583">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
منابع یمنی: صادرات نفت عربستان را برای ماه‌های طولانی مختل کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690583" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODiOOsx7fLuDU5ZsczZlE4WLePXVACRsIqkcJ0U6eXhNqLpJndS0zBSz-6OhahpVTJQyVYl4UZFkC3n0vYc4vH6NTOTB9oAzP8I7FEreUhHPOCTaLWTj15rc2_MMWsUJ5z1cTJDrSkRvAh4JMFGljzxf0G5mKDDSgvy06DART3KT4WlspF6156oMwUSvh3le1yMhXqUGxC4WwqKrvvz48_PKKb54MSzT1oBTRfShxe7JD5DRJiYJCoyMDtjJjHyuMk9eac1wefjBOEP7mvuz3pCgELvlbj1XL_UubnVRtDJOiEZMalyJ65BJtVtO4nLqLBqBk5HXcP6WkTXVoR5WmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقیف تویوتا متخلف با راننده ۱۱ ساله در یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/690582" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b64b67f23.mp4?token=UmM4Ae5Dra3nhfrcQsrYSivzzUE36h5kK-HtwIWe-N9R9LcJeACnvS1YQCSzz-KfsTyzJ5IrW0nL0a9nBWC8xpnU-Un_hOg7Ll1oCnqIKAb9c2vsXYpQHBjqESMEUifS8yqugljXqXXebq2ID4zFZnmBMLI7FCjYlDW7Ow4ryAOoW30NZ6ng9cbhg_rtHMAbZB6PWxCDY2VAv4hzpCq2lA3FBtWKb3v0iQY67-PRzNFYN9j0y1rzoccIVOccW8V4liqshy8lhtO0qpGYYMgZjUVfGkdvWoVsEEWw7O3TE9GXuFDHFf5d9EznniablAj3M5M_baKNrRArelCorDbigz3U0SNy-6RSZGlBgWDUpthHHgBXB2O97oYBiQIyX0qvU6o8yTtDTw0LMDbgxrE3FSeQ_ujB2T-TZCyGJvnZQ_y3KkM6o_YOVv6L6qPjUWzfSZoy4bE8Yeg6gT6SX_oPEaRUqhfuN1xZveaPZ4aY--C1A_F7XBrjcUNjsCxMA4mt1elbEHy5fWCwSs9jxPF3tuLYcbXLIs41DPUT8OwROKri7Vb3OeN_mPcydcOAUZNqZjaqArI0VRT55KYtOd7D-yh890eWOANzk53crB7znqvo3PCBUm8WFaKIExYOw0i166Vv6RZD3sLC5FVFmXM2dsbErt2vDPHQg04kEpL7mPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b64b67f23.mp4?token=UmM4Ae5Dra3nhfrcQsrYSivzzUE36h5kK-HtwIWe-N9R9LcJeACnvS1YQCSzz-KfsTyzJ5IrW0nL0a9nBWC8xpnU-Un_hOg7Ll1oCnqIKAb9c2vsXYpQHBjqESMEUifS8yqugljXqXXebq2ID4zFZnmBMLI7FCjYlDW7Ow4ryAOoW30NZ6ng9cbhg_rtHMAbZB6PWxCDY2VAv4hzpCq2lA3FBtWKb3v0iQY67-PRzNFYN9j0y1rzoccIVOccW8V4liqshy8lhtO0qpGYYMgZjUVfGkdvWoVsEEWw7O3TE9GXuFDHFf5d9EznniablAj3M5M_baKNrRArelCorDbigz3U0SNy-6RSZGlBgWDUpthHHgBXB2O97oYBiQIyX0qvU6o8yTtDTw0LMDbgxrE3FSeQ_ujB2T-TZCyGJvnZQ_y3KkM6o_YOVv6L6qPjUWzfSZoy4bE8Yeg6gT6SX_oPEaRUqhfuN1xZveaPZ4aY--C1A_F7XBrjcUNjsCxMA4mt1elbEHy5fWCwSs9jxPF3tuLYcbXLIs41DPUT8OwROKri7Vb3OeN_mPcydcOAUZNqZjaqArI0VRT55KYtOd7D-yh890eWOANzk53crB7znqvo3PCBUm8WFaKIExYOw0i166Vv6RZD3sLC5FVFmXM2dsbErt2vDPHQg04kEpL7mPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
رئیس‌جمهور احتمالی فرانسه: ترامپ تصور قدرت ایران را نمی‌کرد
‏رهبر حزب «اجتماع ملی» فرانسه و بخت ریاست‌جمهوری این کشور مارین لوپن:
🔹
بهتر است ایالات‌متحده را متقاعد کنیم که به جنگ با کشوری با تمدنی کهن نرود؛ کشوری که بسیار قدرتمندتر از آن چیزی است که دونالد ترامپ تصور می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/690581" target="_blank">📅 13:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وزیر نفت: ایران بی‌نیاز از واردات گازوییل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/690580" target="_blank">📅 13:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da604860a.mp4?token=CL4qIFkrbAqGPnOVWt-WIS_NsWQR1vFrcTOJ98lFx0WPr0l3b_m81QAJxPfdrAXRMuiLLXyNSZJNR1_VpaoQU7cWvLIQ9ySYTPRaRrAKT6Eoyf-aQzfmSdEbT4c7RPw91TUzaKERIDXSxVuQRHx7QzRTDOWsxKbfnW3Sz-8dSyb7lc3TWo78t8gS8ixyY4ebVeSkuNjnubwBpZvb_4tuAAv1vqQNBn3WXRvQRaUFLcLZFXvht-pEfEbi1cQoZfkFH9pNFNh3LIqwZ51BblVdufnUdgux8hyfxjq-c7jQG8O9wFSsXqrFwfyZ8ILBvYVWXO0S-M48B1fnyBINMN7e8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da604860a.mp4?token=CL4qIFkrbAqGPnOVWt-WIS_NsWQR1vFrcTOJ98lFx0WPr0l3b_m81QAJxPfdrAXRMuiLLXyNSZJNR1_VpaoQU7cWvLIQ9ySYTPRaRrAKT6Eoyf-aQzfmSdEbT4c7RPw91TUzaKERIDXSxVuQRHx7QzRTDOWsxKbfnW3Sz-8dSyb7lc3TWo78t8gS8ixyY4ebVeSkuNjnubwBpZvb_4tuAAv1vqQNBn3WXRvQRaUFLcLZFXvht-pEfEbi1cQoZfkFH9pNFNh3LIqwZ51BblVdufnUdgux8hyfxjq-c7jQG8O9wFSsXqrFwfyZ8ILBvYVWXO0S-M48B1fnyBINMN7e8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش توانایی‌های شاسی‌بلند شهری ZEEKR، نگرانی غرب از رشد سریع خودروسازان چینی و افزایش فشار رقابتی در بازار جهانی خودرو را پررنگ‌تر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/690579" target="_blank">📅 13:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ماجرای کنوانسیون دریای خزر هنوز به مجلس نرسیده است
محمدرضا محسنی ثانی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
کنوانسیون دریای خزر سال‌هاست مورد مناقشه است و به دلیل درخواست‌های کشورهای حاشیه خزر، ابعاد حقوقی گسترده‌ای پیدا کرده است.
🔹
این موضوع اکنون در وزارت امور خارجه در حال بررسی است و تا آمدن آن به مجلس فاصله زیادی وجود دارد اما اگر قرار باشد کنوانسیون یا قراردادی بین دولت‌ها انجام شود، باید به تصویب مجلس برسد.
🔹
سهم ایران در دریای خزر نیز در گذشته و بر اساس وضعیت سکوهای نفتی، حداقل حدود ۲۱ تا ۲۳ درصد بوده و باید دید مذاکرات فعلی در نهایت به چه نتیجه‌ای می‌رسد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/690578" target="_blank">📅 13:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690577">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزارت خارجه سوئد در راستای اعلام حمایت خود از اسرائیل، یکی از کارمندان سفارت ایران در استکهلم را اخراج کرده و سفیر ایران را نیز به وزارت خارجه احضار کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/690577" target="_blank">📅 13:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58fb01550.mp4?token=bqXaBjUIGSozjMYZHbG3bo-vKZ4vR3o0n4_HENrOZPme9GtY44eGdyR8DJBol1s8_OPZTyCFAXXB3f2nJ5QSyQvPRwK_tjkjrWqDF1MHvEAEhkCcFE3orQkeZI_feDzcJimvvNy6lAVpSrqeRGgkcy5hQY86RZuZg8bEUqVRUdXMXPRE84kpJWEpNTxq91JROdc3qXoIhNum4GjJa33i5fSUQaLXRZS-qkXurQ4pTSjR3enZBH-o5T5e7V1VQcygszjljqkJANnD92CxwADxa6oUDF27i4HqmY1IiCl78EdnHQSSQBFTmcTAEMtbku7AJa0yHsk76fMkaRcSyNgagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58fb01550.mp4?token=bqXaBjUIGSozjMYZHbG3bo-vKZ4vR3o0n4_HENrOZPme9GtY44eGdyR8DJBol1s8_OPZTyCFAXXB3f2nJ5QSyQvPRwK_tjkjrWqDF1MHvEAEhkCcFE3orQkeZI_feDzcJimvvNy6lAVpSrqeRGgkcy5hQY86RZuZg8bEUqVRUdXMXPRE84kpJWEpNTxq91JROdc3qXoIhNum4GjJa33i5fSUQaLXRZS-qkXurQ4pTSjR3enZBH-o5T5e7V1VQcygszjljqkJANnD92CxwADxa6oUDF27i4HqmY1IiCl78EdnHQSSQBFTmcTAEMtbku7AJa0yHsk76fMkaRcSyNgagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کپی‌برداری از پهپاد شاهد ایرانی به مکزیک رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690576" target="_blank">📅 13:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbff5dc1db.mp4?token=iVVJafNLG_PoS_Fn9CPZDM_DYBQXRDYSrKOzDz9ZHAe-hluWvB5Hi4a0s2bazX3pKnuBLDcE1hcw6I6yKfuSMb1t7J-UJd9zd93n0TotKM9DT3kApblld21kA2soi-kNAAAwXvwhoBAz0AwOR1uPEa7LTqenpSWFAC_oI8y2sZKRc-liVh5YPPLVAlRmO2LXR5uCF8zUm3w2-gyDdIUgIXgPMqVmLA-wIsybaywoy1CTDJCqmjo_Fq1b5Sk1x1D3z4ouj3DJ7UmKZeWNcOGnr7XIED2Gw6ajGrJJvlvYCzztBRyi2wiB3mjjNK3cr0Opo_XvLMebx2iFa2rcNUjxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbff5dc1db.mp4?token=iVVJafNLG_PoS_Fn9CPZDM_DYBQXRDYSrKOzDz9ZHAe-hluWvB5Hi4a0s2bazX3pKnuBLDcE1hcw6I6yKfuSMb1t7J-UJd9zd93n0TotKM9DT3kApblld21kA2soi-kNAAAwXvwhoBAz0AwOR1uPEa7LTqenpSWFAC_oI8y2sZKRc-liVh5YPPLVAlRmO2LXR5uCF8zUm3w2-gyDdIUgIXgPMqVmLA-wIsybaywoy1CTDJCqmjo_Fq1b5Sk1x1D3z4ouj3DJ7UmKZeWNcOGnr7XIED2Gw6ajGrJJvlvYCzztBRyi2wiB3mjjNK3cr0Opo_XvLMebx2iFa2rcNUjxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مطمئنم نمیدونستید با این ترفند میتونید سرعت موبایلتان را چند برابر کنید
#ترفند_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690575" target="_blank">📅 12:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa946db76.mp4?token=DtukdcOQLQMJNPrucMkcd8M5SwfrTIRqFfLnzQt-JqbahrAfJaLVJrw566GSRjU_g0RSHb76SOXrggYnca1xb34bbX5IGHSaNP5L_O8yakHVHR4UPelJX5SMlt0gK_4bfAuqTSLaegtFufvMR2OFqQWh_SVKtInge1ljTLFT7K26E0hE6m8hjJ6Z3LoyO1nvkmsEH-Z2d4hzLmh69ob6bL-iDDYfmdRoBFFoGDud2_BgAJkTF40Ow5FO-IND--E0OIDPyIwpnMweHNeuoBVqMMUxqaqZrAH6NgGD66aeyHuKr3cYUqozDBChCAKoW9YZXZ8VEA0OgOWYAL0HDKOOdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa946db76.mp4?token=DtukdcOQLQMJNPrucMkcd8M5SwfrTIRqFfLnzQt-JqbahrAfJaLVJrw566GSRjU_g0RSHb76SOXrggYnca1xb34bbX5IGHSaNP5L_O8yakHVHR4UPelJX5SMlt0gK_4bfAuqTSLaegtFufvMR2OFqQWh_SVKtInge1ljTLFT7K26E0hE6m8hjJ6Z3LoyO1nvkmsEH-Z2d4hzLmh69ob6bL-iDDYfmdRoBFFoGDud2_BgAJkTF40Ow5FO-IND--E0OIDPyIwpnMweHNeuoBVqMMUxqaqZrAH6NgGD66aeyHuKr3cYUqozDBChCAKoW9YZXZ8VEA0OgOWYAL0HDKOOdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهای خوش شریعتمداری به سهامداران در مجمع فارس
🔹
از رشد ۴۸ درصدی سود خالص فارس تا تکمیل پروژه‌های نیمه تمام و افزایش سرمایه ۷۵ همتی در آینده نزدیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690574" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690573">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ترامپ‌جنایتکار: اگر پیروز شویم، به هر یک از شما ۵۰۰۰ دلار خواهیم داد. این تمام ماجراست، خیلی ساده #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/690573" target="_blank">📅 12:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf87199f71.mp4?token=A15KQnd6LNZIdrjC5X5M1dszNJPpJ39zGD-NQ4JiCLMq2g3BrDjvjvkZTtwbo4BMY1gOTvOiNAGwqmyRB-FnAKNY1SwfMVuHvO2_PefT38vheKbOUElz19Ci7quVupymXvd7csYY8s-A_Wmyv57Ahwsfyg3yyxcmX5nXC8tBfYw6onuPElPf4YlO6bVxrwuZJiPaEBpEWC7w4cAn7CPRcYxXHdQCogMzcacgztNDj4rl3CoBNbF8dCgfWvrJIDN_DLVgq3LcmP43zvgZsyDasc-BOZtGR7tonY7sjsO-mLls_PPveVQAoRyJAVDUShygyv2JfLvheEpBBqqFEwvhng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf87199f71.mp4?token=A15KQnd6LNZIdrjC5X5M1dszNJPpJ39zGD-NQ4JiCLMq2g3BrDjvjvkZTtwbo4BMY1gOTvOiNAGwqmyRB-FnAKNY1SwfMVuHvO2_PefT38vheKbOUElz19Ci7quVupymXvd7csYY8s-A_Wmyv57Ahwsfyg3yyxcmX5nXC8tBfYw6onuPElPf4YlO6bVxrwuZJiPaEBpEWC7w4cAn7CPRcYxXHdQCogMzcacgztNDj4rl3CoBNbF8dCgfWvrJIDN_DLVgq3LcmP43zvgZsyDasc-BOZtGR7tonY7sjsO-mLls_PPveVQAoRyJAVDUShygyv2JfLvheEpBBqqFEwvhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی متفاوت از تهران که در فضای مجازی وایرال شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690572" target="_blank">📅 12:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca85298042.mp4?token=dpsXgegqhbWOvoykqC--jkRi7iuwPoaLAeR2zCJmKhzxo0dyNqPZpWOYx0VBL4sTwD4il9KT0W7_QjNmnA-ZQT7yTZMFAHZCRwYDg_uze1Rcva5AAeq3swkTJOdW5DM-YDyb0pCB6TtMNeicGMZlmgKGeMjvLDZRDT6e0Y-fxUC7-kMBp0Gj8CX7QUUmbCiNsJ6IbZTy6QXTLVeH-1ZMHNDUlxNefU9uN8soq0d4OwNP5rFr_ALBXMIqGbGPJqeAFpc2ygLE9gHcMwX5aU4ZOJ4BYQFSI23_X25pa4-Yqg0uM7XIS2MvzKvMlXLRs4AF-yHgSqbil5qE_PoHu5mrUHMUHhTLX2baB2sZTUqEiw636C_p72gTz0wKRL4Hn512F3TXgl0iVnEcivsd_uVl4kxHwPaynYMuV3_8cDXGWSje-cIvJycqIML24i448SvDG-Fuvxnxy_jMDmA-PIYZ2ixSXi4vqvm4xLhSpr-okYYKfcKvR280eqwnh_sjj-gN5xlfxY68RR3nnOKh_x5s7cQKWE7_SkGSlqFa-6Y3bYzS8hqbtg-loOvfC57ikNlfNuLvPtm1mjNpGOd0GFgdlzE_tGgbdI7eVFx6dD8yO0nEcZd8i5eeddo8fVvrYRLyyETcGEdQcezYkQhYJlKnUyMT-AAlqx-B2JZyjx_nU90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca85298042.mp4?token=dpsXgegqhbWOvoykqC--jkRi7iuwPoaLAeR2zCJmKhzxo0dyNqPZpWOYx0VBL4sTwD4il9KT0W7_QjNmnA-ZQT7yTZMFAHZCRwYDg_uze1Rcva5AAeq3swkTJOdW5DM-YDyb0pCB6TtMNeicGMZlmgKGeMjvLDZRDT6e0Y-fxUC7-kMBp0Gj8CX7QUUmbCiNsJ6IbZTy6QXTLVeH-1ZMHNDUlxNefU9uN8soq0d4OwNP5rFr_ALBXMIqGbGPJqeAFpc2ygLE9gHcMwX5aU4ZOJ4BYQFSI23_X25pa4-Yqg0uM7XIS2MvzKvMlXLRs4AF-yHgSqbil5qE_PoHu5mrUHMUHhTLX2baB2sZTUqEiw636C_p72gTz0wKRL4Hn512F3TXgl0iVnEcivsd_uVl4kxHwPaynYMuV3_8cDXGWSje-cIvJycqIML24i448SvDG-Fuvxnxy_jMDmA-PIYZ2ixSXi4vqvm4xLhSpr-okYYKfcKvR280eqwnh_sjj-gN5xlfxY68RR3nnOKh_x5s7cQKWE7_SkGSlqFa-6Y3bYzS8hqbtg-loOvfC57ikNlfNuLvPtm1mjNpGOd0GFgdlzE_tGgbdI7eVFx6dD8yO0nEcZd8i5eeddo8fVvrYRLyyETcGEdQcezYkQhYJlKnUyMT-AAlqx-B2JZyjx_nU90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا کشور با بحران کمبود پزشک و پرستار مواجه است؟
دکتر محمدرضا ظفرقندی در
#گفتگو
با خبرنگار خبرفوری:
🔹
موضوع کمبود کادر درمان و توزیع نامناسب ، دو بحث کاملاً مجزا هستند.
🔹
واقعیت این است که ما در حال حاضر به‌ویژه در زمینه پزشک و پرستار، بیش از آنکه با کمبود مواجه باشیم، با چالش «توزیع نامناسب» روبه‌رو هستیم.
🔹
برای حل این معضل، باید سیستمی برقرار شود که با تأمین معیشت مناسب در شهرهای دورافتاده و مناطق محروم، انگیزه لازم را برای کادر درمان جهت فعالیت در این مناطق ایجاد کند.
🔹
درباره «نقش مهاجرت در کمبود پزشک و پرستار» از وزیر بهداشت پرسیده شد، اما این سؤال بی‌پاسخ ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690571" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
تصاویر جدید از شکست عملیات نظامی آمریکا در اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690570" target="_blank">📅 12:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hidxqx0ciyP517ChikzAbYvePw3I_ZCXsEdx9LZ-YvyI84krLbED0OmyJsZ3yAeDqWcduNH6f1_Fdyt4KeYycc37geKKKwnXe86HBmz-BdoHwl8yj0n1Ae3z-OK7bRblimrComoxnd4g6MpYXTdWrwIdO8P9-ebVuBvMorJlGM-zi786cGpBJaMdYqMOGvZLErLltDe_uDWhHmYrRVLiQYuboznRHC2DgG-ZtAm99plP332qYcxgLUHQPHHnNwm8jqx6V010p4ZxymB1AEcvbvpfRIlS9IzY3D92VKJiXkxA-mtYD0j1ggm82MPC9xli6nkmX162FFExmCkfBiXIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از هر دو کودک زیر ۵ سال، یک نفر موبایل هوشمند استفاده می‌کند
🔹
۵۱ درصد کودکان زیر ۵ سال از تلفن همراه هوشمند خود یا والدینشان استفاده می‌کنند.
🔹
۲۳ درصد کودکان زیر ۵ سال هنگام استفاده از تلفن همراه به اینترنت بین‌الملل دسترسی دارند.
@amarfact</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/690569" target="_blank">📅 12:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690568">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aec07825f.mp4?token=WlsqR1uw_08cmgo-MMG3YkHmANdNEkA3kMZS6MZI-Tds8XENHslI0ofET_cqiPM39ba9nkLcNI-qgH8Om8Z86ZufDBAEO0_c1xCMAgshFBMsakmeDDmxloSa8nkLzRDCrPTEQ_gMcpMH5-VfN2IH4Bbeu_rJ9Oewwukk6QZRRr7cUFxyUQGMuHD7AegyjQiy6DwE6MPwYvM8aXmutGK3lSZ4Iuxf3rNNa6jHtBgt5OOKBjNBGmYmwb1aK9kb6veaNwMCQ6xYF7_ID3HfH8CL8-JVx2k9eUQOMylYiaUH1TeCLMbBF18_wdrBKIYS7NH8AJc0zHQSjkvKs5lsb48SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aec07825f.mp4?token=WlsqR1uw_08cmgo-MMG3YkHmANdNEkA3kMZS6MZI-Tds8XENHslI0ofET_cqiPM39ba9nkLcNI-qgH8Om8Z86ZufDBAEO0_c1xCMAgshFBMsakmeDDmxloSa8nkLzRDCrPTEQ_gMcpMH5-VfN2IH4Bbeu_rJ9Oewwukk6QZRRr7cUFxyUQGMuHD7AegyjQiy6DwE6MPwYvM8aXmutGK3lSZ4Iuxf3rNNa6jHtBgt5OOKBjNBGmYmwb1aK9kb6veaNwMCQ6xYF7_ID3HfH8CL8-JVx2k9eUQOMylYiaUH1TeCLMbBF18_wdrBKIYS7NH8AJc0zHQSjkvKs5lsb48SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به تازگی دعواهاتون با همسرتون زیاد شده، سخت نگیرید؛ شاید فقط دلتون برای هم تنگ شده #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/690568" target="_blank">📅 12:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
وزارت اطلاعات از انهدام ۳ هسته عملیاتی گروه تروریستی - تکفیری با دستگیری ۹ تروریست و به هلاکت رسیدن ۳ تن از آنان در جنوب شرق کشور خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/690566" target="_blank">📅 12:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ماجرای تلخ مرگ کودک ۴ ساله تبریزی به علت گازگرفتگی سگ ولگرد؛ کلینیک واکسن نداشت
🔹
امیرحسام پس از حمله سگ به چند بیمارستان منتقل شد، اما به‌گفته خانواده، نبود واکسن هاری در نخستین مراکز درمانی باعث تأخیر در درمان شد. این کودک پس از چهار هفته درمان، جان باخت./ هم‌میهن
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/690565" target="_blank">📅 12:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وزارت بهداشت: واردات واکسن آنفلوآنزا هنوز قطعی نشده؛ شرایط، جنگی و دشوار است
🔹
نکته جالب اینجاست که در همین شرایط، برخی به دنبال تامین ارز برای واردات لوازم خانگی هستند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/690564" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fb03d7c.mp4?token=LzGW5geyDjs1x4_V277fkKc30ycxIAiCoPxuxby3vbKK_fuZgb0ZT5gTfXtwmYYChyMufeL9xKZyH5PtCJb6n5c2ibfhT1hdLMEM0QQ4V0BqulZ6N_bsUKAAaWWyb9YZfy_mjhxwn0ygN2eXxf8fsHE5uRXZj-RVcoqoPbm3Q2d7jFCp1Wl6r-TSaUZ80Ta1qoInsyaowFwRUzyllnFb_jxQc889W6FCKxsAo_Z5sAyf9PKw_y93fpUoKyFYsToiQip8oqyyDBiRUSf5Xf5nWX2mGMFNa4LRee0r-r9dynVhuDEJfn0hyrt1YybgNyErsJwZyJNq6gIJMx44Syq83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fb03d7c.mp4?token=LzGW5geyDjs1x4_V277fkKc30ycxIAiCoPxuxby3vbKK_fuZgb0ZT5gTfXtwmYYChyMufeL9xKZyH5PtCJb6n5c2ibfhT1hdLMEM0QQ4V0BqulZ6N_bsUKAAaWWyb9YZfy_mjhxwn0ygN2eXxf8fsHE5uRXZj-RVcoqoPbm3Q2d7jFCp1Wl6r-TSaUZ80Ta1qoInsyaowFwRUzyllnFb_jxQc889W6FCKxsAo_Z5sAyf9PKw_y93fpUoKyFYsToiQip8oqyyDBiRUSf5Xf5nWX2mGMFNa4LRee0r-r9dynVhuDEJfn0hyrt1YybgNyErsJwZyJNq6gIJMx44Syq83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوک قیمت‌ها به شهروندان آمریکایی؛ وقتی بنزین گران، چهره واقعی ترامپ را برملا می‌کند
🔹
یک شهروند آمریکایی کنار پمپ بنزینی با مشاهده قیمت‌های سرسام‌آور بنزین، با خنده‌ای تلخ و تمسخرآمیز ترامپ را دیکتاتور خطاب می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/690563" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
لاکچری‌بازی در شرایط فشار اقتصادی / کشور در محاصره است، اما برخی عطش برند خارجی دارند!
🔹
قیمت یک دست مبل مینیمال در ابتدای سال ۱۴۰۳، ۲۵ میلیون تومان بود. امسال قیمت آن به ۱۵۰ میلیون تومان رسیده است. ما نسبت له قبل فقیرتر شدیم اما در کمال شگفتی تمایل به زندگی لوکس رو به افزایش است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245847</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690562" target="_blank">📅 11:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEF9O3oQ2Yogh-TrinauzjrMvtOvXaybzNPiqzESWoJsiI2PyhJgzV75xCC2wuWZsG3JeTUchMigpfS39Uga6-XP74_V3fKLWppyTiuLgccL1qd0DDNTkPgTkSQyhOiVct__0RFIXR6fc1IQSq0zlIURzgm1iPEWOobmFB4405Rq08rt9qa4OFVfJGY3uxnfSTKsGoY02GdtspngUDD-OsuNETQ2iCOhfD8bkULUS1JxScCspK1POYeABrAVIBOR9QYSPU-EX2zyC_PX4XjBMhKAo-q7CJOzQuKrH0qEJ84QvPgejMNaNQisGPGP864q4CIlFGUSFJWqSE6or1ByPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ غذای دانشجویی سال تحصیلی جدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/690561" target="_blank">📅 11:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129b6ba29c.mp4?token=gaACiM6WkZ3AL_EpIKR_BUDAkw9W9Guy8EUebaw3CcfJK9b5fnGfn7w3158phsVsRZVOduDuZGj_7fI8lc1IvtcrDxG1SWXjbk7UB7TiYiHfK9ngV7qa2-ODriv7zfLtCZ5uBJygTv0pCELFkavJGITblHW4CJ5oyA9B583BKKfSibBW7NOG4e35n4onku7so5rhXzocfbETvRhKadSrGgLpSh7DrTHTJ20zDuvnHelM8yRjAEeqhgE3Di0NlkOIb1dvaYQzA6DUDi-YUcbfsgOszTYF5jXKrHEmvViuJfwX0uFr20iBajO2Oj9m2XmbqyY7gUtJFQRX9Z8nRWDQEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129b6ba29c.mp4?token=gaACiM6WkZ3AL_EpIKR_BUDAkw9W9Guy8EUebaw3CcfJK9b5fnGfn7w3158phsVsRZVOduDuZGj_7fI8lc1IvtcrDxG1SWXjbk7UB7TiYiHfK9ngV7qa2-ODriv7zfLtCZ5uBJygTv0pCELFkavJGITblHW4CJ5oyA9B583BKKfSibBW7NOG4e35n4onku7so5rhXzocfbETvRhKadSrGgLpSh7DrTHTJ20zDuvnHelM8yRjAEeqhgE3Di0NlkOIb1dvaYQzA6DUDi-YUcbfsgOszTYF5jXKrHEmvViuJfwX0uFr20iBajO2Oj9m2XmbqyY7gUtJFQRX9Z8nRWDQEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشایی تنگه هرمز باعث کاهش قیمت‌ها می‌شود
مایک جانسون، رئیس مجلس نمایندگان:
🔹
ما در حال پایان‌دادن به این درگیری هستیم، بازگشایی تنگه هرمز باعث کاهش قیمت سوخت و مواد غذایی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/690560" target="_blank">📅 11:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رئیس سازمان خصوصی‌سازی: واگذاری سهام عدالت به جاماندگان فعلاً ممکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690559" target="_blank">📅 11:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2BGZHejrmmhIKlgPzrLBX1V1TzT-qikbBBPS2t-8VyzHss5v3C9P-ZH6PzfqgzNc4d_T2tHIElWNxurjTkei9SdsYz4uRuUclB6d6Rd4yqn3wlEkjsdv1pUr5d0mkl1pCeddvsnw1tZjEJ6Gf9QNxT3mci40AGmdsKtyHfjZw9jVSTXtv4RAeGe5cbi6jUWuyDOfyYQHj_oo6-YlfXMK4r7JpfuDIJYNxtkHfkGJT6Dc-YAMw7k0PRmAnyG1e4prrdK6zx2L0DQOVN_GsBf-Rn62Mt3knZvU5YWTB3L4hkHLl2-7unKUAP9Gm9MpVdQzjmiE1ioT0Seq21JrpTscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار شرکت توسعه منابع آب و نیروی ایران: ال‌نینو عامل ۷۰ درصد سیلاب‌های بزرگ ایران
🔹
مدیرعامل شرکت توسعه منابع آب و نیروی ایران: نتایج بررسی‌های این شرکت نشان می‌دهد ۷ مورد از ۱۰ سیلاب بزرگ کشور در سال‌های تحت تأثیر پدیده ال‌نینو رخ داده است.
🔹
کامگار: بر اساس یافته‌های این پژوهش، ۲۹ درصد سیلاب‌های رخ‌ داده در دوره‌های ال‌نینو در ماه فروردین و ۲۱ درصد آنها در ماه آذر اتفاق افتاده است؛ از این رو پایش مستمر شرایط جوی و نیز افزایش آمادگی در این مقاطع زمانی از جمله مدیریت بهینه و‌ هوشمند مخازن سدها به منظور فراهم کردن امکان تسکین و‌ ذخیره‌سازی حداکثری سیلاب در این مخازن و استفاده بعدی از آب ذخیره شده جهت تولید انرژی پاک برقابی، از اهمیت ویژه و‌ دوچندانی برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/690558" target="_blank">📅 11:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc014bdc8.mp4?token=t1_Ro7WLEy6v4E93V-cD9NgimQ7wJWVOw9w4sNjYsrjbbtm3dwS3-ze_CWoenJlh5Oezu-u8zhOG1R-OEe8uKpdsACFawZUqWZD0R9O1cdxWzUtfYpnJdoURK-JmdBP2c16ZMS0ikibbgQ0xxGjXvvRcJBDNlMu_sQJAo0XKouCrD2DDFIrZZmIdq_R9JboAeyMUlIrAdDlRkei73K0V8zhiIjwAsG3NVSUgQkl4k59Sfvkpyi0FCYQcZx1K-7iIXBVfhawgm42jUFHpw4NbwdM362kH4itPbZ4WIDCnmSo3m3-N76m1nXkJBRe8gBrxljT4Ab0B5WmLkW7pSXa-sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc014bdc8.mp4?token=t1_Ro7WLEy6v4E93V-cD9NgimQ7wJWVOw9w4sNjYsrjbbtm3dwS3-ze_CWoenJlh5Oezu-u8zhOG1R-OEe8uKpdsACFawZUqWZD0R9O1cdxWzUtfYpnJdoURK-JmdBP2c16ZMS0ikibbgQ0xxGjXvvRcJBDNlMu_sQJAo0XKouCrD2DDFIrZZmIdq_R9JboAeyMUlIrAdDlRkei73K0V8zhiIjwAsG3NVSUgQkl4k59Sfvkpyi0FCYQcZx1K-7iIXBVfhawgm42jUFHpw4NbwdM362kH4itPbZ4WIDCnmSo3m3-N76m1nXkJBRe8gBrxljT4Ab0B5WmLkW7pSXa-sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کی گفته که آمریکا می‌تواند برای همه دنیا تصمیم بگیرد و بقیه باید اطاعت کنند؟
🔹
ما این را نمی‌پذیریم و سر خم نمی‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/690557" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm5uJsp4eK_aBxm_oWW37HKzsGBwg5KVvdVMPAFS5hM-Tx3x-r5oy2f6LvvbqBj6JVEMIhgw34TlDpC1SBv89XTla58ZiGsOpqZtJ8Odmmt0QJvpMJ_7Oz71cmrE9BNTYhd3lvvWgAY6d6MQcfRtdu9EDJLbIYExfiDyve_G3yDTevxJ376uOQkriqZvGiDOpDCmKENEpTkYn15jGPuCDzRZuOmDZ_8RwBNPSVdQRMCOstIT6EXexx9SjE-J_L3Kx0efsY_LH4244uQpvWZkcnQpyiHu2eqmFd_iBkQJwChdYSfE_XLMWzScxTeCtBsMaps_WQfO_Q7F72zKcoH6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست ۱۸ بازیکن داخلی دعوت شده به اردوی تیم ملی فوتبال ایران اعلام شد
🔹
چهره‌های سرشناس غایب در لیست تیم ملی
روزبه چشمی، محمدحسین کنعانی‌زادگان، علی علیپور و شهریار مغانلو چهره‌های حاضر در لیگ برتر هستند که در فهرست آخر تیم ملی برای جام جهانی حضور داشتند اما در لیست جدید جایی ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/690556" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd9a6d7d5.mp4?token=NAP1aeBTZ3Af6KoVkOb_y4iqw2F2GDPYjHzu8_AZcMnerYz7zmrr7FrocgjaVJnWIzl2qK-QGVQVxQB1Zakh6z6nv_htQgqoG6FSNq-4PrYXiDXRtWDZ-tT1LtEmLviMWivNorFMbBBzP9-0ieZgC70fArEx7uGwgLodX1UIeOFsjKnf9fkhZoCSiZcbW-KVa8gzWpNpZN0hANgMfM_iaVM6Z9xvFhUp1H7xT7DSrkKz3_DKCICR6g1CddQUrVL7BF4uG6i2Ywhvy8XhUYoY8oIsWrijil4d9x76VJRMJ5gsmp4F3pvr1PqI6Exbtn651SoAfm-j_NSo_b0d0nrTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd9a6d7d5.mp4?token=NAP1aeBTZ3Af6KoVkOb_y4iqw2F2GDPYjHzu8_AZcMnerYz7zmrr7FrocgjaVJnWIzl2qK-QGVQVxQB1Zakh6z6nv_htQgqoG6FSNq-4PrYXiDXRtWDZ-tT1LtEmLviMWivNorFMbBBzP9-0ieZgC70fArEx7uGwgLodX1UIeOFsjKnf9fkhZoCSiZcbW-KVa8gzWpNpZN0hANgMfM_iaVM6Z9xvFhUp1H7xT7DSrkKz3_DKCICR6g1CddQUrVL7BF4uG6i2Ywhvy8XhUYoY8oIsWrijil4d9x76VJRMJ5gsmp4F3pvr1PqI6Exbtn651SoAfm-j_NSo_b0d0nrTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر رهبر شهید به شهید رئیسی درباره امیر تتلو به روایت استاد رائفی پور: چرا به تتلو نزدیک‌تر نشدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/690555" target="_blank">📅 11:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
کشف اجساد ۵ نفر در تهران
🔹
اجساد ۵ زن و مرد که گفته می‌شود قربانی قتل خانوادگی شده‌اند، در گور دسته‌جمعی داخل چاهی در بلوار سیمون بولیوار تهران کشف شد.
🔹
عامل جنایت دستگیر شده و تحقیقات درباره انگیزه و نحوه وقوع حادثه ادامه دارد.  #اخبار_تهران در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/690554" target="_blank">📅 11:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تصویب طرح تحریم روسیه و ایران در مجلس نمایندگان آمریکا
🔹
مجلس نمایندگان آمریکا طرح تشدید تحریم‌ها علیه روسیه و ایران را تصویب و برای اجرایی‌شدن به کاخ سفید فرستاد.
🔹
این طرح موسوم به «قانون تحریم روسیه و ایران ۲۰۲۶ لیندسی گراهام» با ۲۶۲ رأی موافق و ۱۵۹ رأی…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/690553" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690551">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
کشف اجساد ۵ نفر در تهران
🔹
اجساد ۵ زن و مرد که گفته می‌شود قربانی قتل خانوادگی شده‌اند، در گور دسته‌جمعی داخل چاهی در بلوار سیمون بولیوار تهران کشف شد.
🔹
عامل جنایت دستگیر شده و تحقیقات درباره انگیزه و نحوه وقوع حادثه ادامه دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690551" target="_blank">📅 11:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA13a1NNOSd4I0XniIdtw4KJ0n8-4nG7N59Eyos8XIAWBJ1NgpNwKOWVHhHzuKjrFyf7MCG-1yy0B8HDY6rQSjJaxRKkoHu_kF1SS2tSa7ISiZlFpMuCcvkmYJ2GHyVk70dxQuexi8N1Zhk7aXq2gXxD8DPkSsoVvpvoDrJH7IJpTWS2NB3x0FVnGt2VL97Ny1H7LO0Qrf5MkXOiWn--nmxH3vJL2QtKF7hjFcfIwjom53HbhnHBeGKsTtJnkaySosAl1XvmgVvtr_p4IITBVFaStLli219Sye5UTE9Pxnd1M3ZdOTsGzLuSd2edhayQa8BJK-hKM_i3GPkz1jWz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج سفرهای جاده‌ای در روزهای پایانی تابستان؛ پیش‌فروش ۸۰ درصد بلیت ناوگان حمل‌ونقل عمومی
🔹
معاون حمل‌ونقل سازمان راهداری و حمل‌ونقل جاده‌ای گفت: با توجه به موج سفرهای پایان فصل تابستان و افزایش تقاضای استفاده از ناوگان حمل‌ونقل عمومی، بیش از ۸۰ درصد ظرفیت ناوگان به‌منظور تسهیل سفرها به‌صورت پیش‌فروش عرضه می‌شود.
🔹
مهدی خضری اظهار کرد: در این راستا، هماهنگی با تشکل‌های صنفی به‌منظور افزایش بهره‌وری ناوگان حمل‌ونقل مسافری، برقراری سرویس‌های فوق‌العاده و تنظیم برنامه زمان‌بندی حرکت ناوگان صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/690549" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_QxRokRBC8pNChndVsIc2n1brPx2w9F02jkf-1IbVml7nal-VQs6yRshe14HhAddtdT72jvVY00-OXJRnWmlMLl5rqsoFTVjmaJLKcEovnCUEOyJgNsruID3GC2M-NpEoroVmCnRdhh9JdyOlvU9XZw5NCpIj-gYWTnl2GXtHJAQgbv3ADuHZ9NdebRCigGHmvq610hAjeFPQ969wrhFs8WwedLPXk3onSUFhCv9kLhtnQVPt9Hkblm3sCgNQXNxlYVd2Q6E3yrTF2En-9kKzdS5bWa4enMnAFRvciBKBhMl9jIqwt7rb4tVPvM4ezCACuOjEliGo66F1wbFucz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HspCp-KSoUe3VjydTcnbJ79PugoEJ-lLGYcd7b4Hi1vLUOk4_RQOP0nRp5Rd5YCOI7DY_VptMF3CdW7VpaZmpkggz8nVyGvp0VCvZPFnnzecSVZeQnXBwUvvicibwNB56iGVFgEQGsPFt0S_jfFqX_hqHE0MWDfkCuxJhCg-zOIiiyp2APkmd04E-T8P_6FZoxnfFkU1aPIr3VbgCFR0ljA9Pby8pO1eu2x2DMRoFPcXm9oWXx-TqJise-proAj2YzIQLswR9DdUXDA6iSYaSACiYD0C-TjLq6nYrzqEBtDQBtmgw8c0wYCDTUsSrTNTZY8NPurnz2Rtef_iNOS0NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازگشت آواکس آمریکایی با فرسودگی شدید
🔹
یک آواکس E-3 آمریکا پس از ۷ ماه مأموریت در خاورمیانه با آثار فرسودگی شدید بازگشت؛ این آسیب‌ها به گفته گزارش، ناشی از استفاده سنگین و مداوم بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/690546" target="_blank">📅 10:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyxdz4LL9eFP1uZ3k0-ijhX0z2v_Jl-FDSDOtzEdm-qYiMwHrDzybmlOacITp1Xo_Ttu-fdzHitZMh0dpLqwRn5Husk50gzsSlyCznpbVzpwB8IHEKNQOWpc66wXSjFMvEg5vMv5EUaVpLovU8c0EyshO4BnnBTexngjphKLySQp2h5mf-Zl_3eKsWTfIH_mpS6JJdBuwOLKw8262r7IPX9AcjlTw3m-ontHzYicOLvbvXyH2axbTktaXDI9U3wzppKWV1dZXg8o9aiSg7ATuscQvUK5LD_VEaB0ForSrKkARY6YFRmMnHmcf4YhYdj2LXRvl-57V65QrLLbXjNvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویق استیضاح پیت هگست
🔹
مایک جانسون با تعطیلی زودهنگام مجلس نمایندگان آمریکا برای هفت هفته، رأی‌گیری درباره استیضاح پیت هگست را تا بعد از انتخابات میان‌دوره‌ای به تعویق انداخت.
🔹
جانسون دلیل این اقدام را بازگشت نمایندگان به حوزه‌های انتخابیه اعلام کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/690545" target="_blank">📅 10:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690544">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgfI9sIr-FedWGBwh-9KL7uIkWGRxpTJX7toulGMy0RJQffqpLI3K35ir30tTcTW2ZamRUcSF1mvLcfcK4TblYalW5meB0G5PfCWvOBH7FLD0Gds0Sp5g3LPHoFC9QnxavMbru15P02h2xngkhFjC8-GO6uH6gVYRY9mGgUnxvGIxOZfVwnAQkUN65XYnQe3MHu2GDn29ayf_LufJJ1bOB4Q971xLK9nrQEH6w1HqOgMi_-WrpKb0EsEwnEAutfYGw30zr0kZQ_4XymEQ6YBsHH4qWKT9-eBXxxB5TO1vcWnvwSQFGtX3wPTB2lt3KKpLe0c5n_kNL85kZmw4HvyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهریه چه زمانی معتبر است؟
🔹
۶ شرط مهمی که باید بدانید
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/690544" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe5662b69.mp4?token=Hyyd_MwOnidc5KVGOKdLcSzE3Wt9NRk1cWeL2YjyBkypgwbUzpiHDvbHGZCVKQQMLZpV21Zlhl2oZWCUc1M-P1n3qt-jdYs3rht7fSV3lmS1mFF59eVfIAphGsaYSa1jD_VrYrwGB4VcdtBd7K_NVxh4LIqU0DheU08XLBlyVAg_M417kUFUgmRQRFy8wVr2qEezyB7wTgtdsGW2s1qgDuoSkxNJvwlGqOdW8yuTR4CG7gyRJVMJrahiIBXO54lhKV99sLCGbuZH1e5_KFhX6rO2sTFm3SiQEoO_ZV383aRcJfbBpwKb0uKjIbInINErPtqk3dMnHdpv6EUbb-5kuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe5662b69.mp4?token=Hyyd_MwOnidc5KVGOKdLcSzE3Wt9NRk1cWeL2YjyBkypgwbUzpiHDvbHGZCVKQQMLZpV21Zlhl2oZWCUc1M-P1n3qt-jdYs3rht7fSV3lmS1mFF59eVfIAphGsaYSa1jD_VrYrwGB4VcdtBd7K_NVxh4LIqU0DheU08XLBlyVAg_M417kUFUgmRQRFy8wVr2qEezyB7wTgtdsGW2s1qgDuoSkxNJvwlGqOdW8yuTR4CG7gyRJVMJrahiIBXO54lhKV99sLCGbuZH1e5_KFhX6rO2sTFm3SiQEoO_ZV383aRcJfbBpwKb0uKjIbInINErPtqk3dMnHdpv6EUbb-5kuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف، معاون اول رئیس جمهور: از مردم عذرخواهی می‌کنیم و  شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690543" target="_blank">📅 10:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_a8FTod6XC0SKCAkNJwkRxrhWkHdHVHI6qtVUW_bnX7N7IinnIn-FCUb0ScuRI6H6C8GHc9QXvCwvSdKc9rxd4lguYhRCuIqx5A2nzm7YMGm7WCl7vtdOOs-4kt7EJQuCZ_iJt9oGBZCOQoYvDL0CSKHMhFGwKuBbifFz-BlvQ6zxXd7pujnUMTV4lSq9gh6vIKy4Hp3gV1Oy6WZCtchgHu6A3suReyfUfIRr4v4dUwT9ZvNKGB7m-5NE5A3uxCH_vIdXJF67UygFmWDnFEJbGVU73-UO9wjQRa_kzJkEiLZBVkTUqNj4I67SNsLSRE3UyahqGCc1TTO_rNdNL0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام دانشگاه‌ها سال تحصیلی را مجازی آغاز می‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690542" target="_blank">📅 10:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
اوت ۲۰۲۶؛ گرم‌ترین ماه ثبت‌شده جهان
کوپرنیکوس:
🔹
اوت ۲۰۲۶ با دمای ۱.۶۵ درجه بالاتر از سطح پیشاصنعتی، مشترکاً گرم‌ترین ماه تاریخ ثبت‌شده بوده است.
🔹
همزمان، یخ‌های دریایی قطب‌ها کاهش یافته و بخش‌هایی از اروپا با خشکسالی شدید مواجه شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690541" target="_blank">📅 10:20 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
