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
<img src="https://cdn4.telesco.pe/file/UGrTOBhuWzgOww0wXNEREE5BjVRiLPYFKvrvgDLUziz46mHJSGeuuPqkaGPQ_oKyab-gueii-mR-MpVg9nudsQyMrhY2ccggKL1HVOUmt6we3D6ZKsym2BO4B-Oa8FBcTHNLxNM3vU-YX9r77PYHLJ_RUwd3x4Ee8o6rjJISRJay-zYpBjOfUkF8nJrti_78iHuSH3y6zaGf1xy6kfTYRhqrgcayfChYNJlCt2PgooL6PMl2yyxC0Ks-6SL4WZvPe8X1vMii7IB8FdBAbjiuJrXkgTCoN3YyeAfHvqiCwI1Yc-FFi9zgR2Pcvn7Q-uaunI5pVhWoa0xXVAvqxJZu_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLBI_814qgol_DQ-CIl1yYSfSaQxp2B1Wh4_IPFEmFgWj5VT2ZvlYgB9pb-ulo1GouS5z2tOfgb9OfNsrEo72Uz-5QdMHBy24nQbSTQMWih68uQAlNetn9-OoPgStEbfTHFcNbAxwHyQjDhm_c7q00qEh2N23igLiJzk6T1eJ8ppq2b6sqSJyXgaMIG4_CQWnN_Up9o5Or7YKfnf0QzqRt-lTdMKVWG162UQws8oCy_JDAK6ndbTkLL6z_PnTkX45uNns93HqbTJtqcf1XxoQj5cfl5zLfRBkViNdqFWpaxr4lMiagnhqhX5G0GklWkwuhTKnUbRg0f396JybuvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_V24fwnlSEn8pBtox3mpxpxImaYlFd8e44Kta2sIesLQWwRF7pDZ-lW_UHBH-F9OuUJXOBB1FfbiCJ1RibqaJ-snqF452VaujAF8rVwShBgO3Pk6yq55d_s2H5xZqJ1BmADKlUdgg7wCMYaL8kKomfWkB4F4aY63FA4JZmD_ZrXB_3XfVCVWmlGHdiiwsZmmIxrZdOLcLTU6DWWVfKm6fl0IAFlw74qL4ai0_-dPjszTWYa0THkpBJL_fHzGRBcshnkDDHwcT6yhQb-_h4SsAVMeeYzTPhMhtUFGHL-48vTp_vJzh-paPiVuic2vTSu7ImpBdUH03OUVD0BtmS7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r65_cUMVECRh1d_kX9m8b7VQ0FZmDfcKjK5LsxSJDbvxHVp5xnYLKbeowLxfnN1TP8Im_mqoLpJkqLYkiQVBqM3GLdgd4iJJ-NJDgn0ZsSdo2fsakhBlvVnfI862S-zi1kWLoGe-xCe0YhQLYdCoes_jWGYN8dvH3lV3PhVnD2d3-vmdFEVO1Qjg8eGhBmeew8YDn2JCZ2m88iTbZLu2zI87dlLKDFjSdfoB-B00V3poqMiinoXrZ9ej_lJaaMkHyCNpihs3nT_PfmFbiyHpxISRFAdpcxHFXmAdXp0ULkmpgwd_kG1eNBm2gu3ADaJW0KDnI9h3O4PyiZLz8k4Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZeYh9RPtt8JT0oV05Krm6lQKse0sDn_VbsiLgusg5UJq7DLfgfvaO5DDXBQlVhPXjlMKV1zwjh8f9sqoKU28GzsB43QIYDpxpTJ0e0g-KrtHHhGS4692cNY6hU0e4x2iwC2T8MP9Bc8nb4mtxanQfjCtlht9UuMqRv_ynJipik5D4GgMNpaoQP_Ctq3ZFL4DpjdQJXZKYEfWK81xvCSye8Fer2WIZME9s9zGIwVPkT0Y0zjQFfxA5IloeqiV33Wi0Crvmt31e3H3ROTSHrl8HBryESJBwAU6jJfnYAAmNkR0jIQUB4C3TzKXOW-UabBhSWAIMjUBi-s25V_fnufYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwwhQ_ldICT3cRxJOC9cnEmlZb48JEnIKoph0JojT3KgH-O8p28FTG36Cvr07UgOAhgc9_mFZHzr4ei0ZyZGrhY9cQHi_7RMxCp5g3omnn5u4oFU3FLJCe7vYMtNB73PS3tcuT8RIk772Ow3mPhqKPnNnFifO3HiTw7uauOX_XKGFuI1IG7InrMtof-xF2z_cdpoFbvRKxx16w4nNVLU1B7Vh2kmaJTbqs7p1PFrDC6yxyeYt0kZZFevLf-eokatdnmAE-4qY-IH68ha26oHawX3LVsRHeXX8UlrWFeNnqoExJaiy2C5AWA4OsXMQfpniReeBSU_PDFLKZFT4L-lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF-bgGTnmS1Orhyf88CBJNFxheUlj5iGZi-vOPKYWfk1DF0KSi_IlL8qoO_tztJELxNyE3VtAm_1UgBVhLOiDLBYtL-08TwenFMoM2R0fp2iiyVTgCA1XjBtHJIFGDpLz5hyi5n6ruvcstrj4LdmKbNUsn2sY_csSx2KZyP_YYTfWwShvugChMEXt9F3o0DKLD9jYgk2vj-IsXSZ4DXgJhICu5sy0mIMWLh97pmGZMaukT9q2VKO21TbK9Lq1fV1WXDTrMF9lV9LnOCMroyoakVKNsyMOq_bNPSNFhyEn5FWDWJbrI4EIuHrPSWws2RvbH0p2H9E8ZLKeS66lD402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSff7t8ACHc96vKiMwUCL9JW-CshwMOjQPWMTpUxXMnjItKktpQ8VS9baK59qQ4xT1huavybta8psXlG2q4-2tkIfANrboUISw0QwPvEGoE4Nty2hGQAmTIChxcYVX4VmPXuNzCChi9fWbNPZBUtrUUuCLdKAnhQNwd5DFxnBLng1eK0KSaDlXNunlOwfE5h3-BLqHpZew5ZYDmbQbbUnGQbRRV9EmpUWl8uS55eI-9_rEo8W8GTS1dYL3GRGU4GWlQtxrmmve8ATkgEwkLC4Ke-xopzSiVqDGxUfAOgTWUsMEMHJbH6bBa4YysGBCucq0QyOech6f4fxHaKcjJSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVA0ZzOUVcIvYWXZPZ5h7eWQ2B7U2Vo99iygSHuN0Q77-lXV-0w3teaco_EqH_PkFZnpFVBIadowMQWag_dh3zVc8H-n45Xw7pBbZ1mHxEgbf5rZHpuO4HMpwfhll6KdZPXAFch7Jbi7oZ1FNI9s69sR_AC-emDjTlSjlCalq5PGx1YQyZ4p8ST_pa0iqPWS5RxmY_AYUBygluwCyf_qltOfRWy81Lef7IWtqorPcLG_ythiaKwFC8LdYFB0u8KcNcWcl4YwCzW8WUy2EcQXGpfAI5UaEnVvSU-OhuFMj_fGM5scYKxXoUHgWr61I74gLyoqIzk89dUEGych85nbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qknrC7mLksBBdTnTuwUOIkYayIGk9Nkx9iF3GIMi8x207GNsWiz1k3hVXKm4rnzUGKYs9zV9qRwYHNULh0fLF1SCqs-RPAUoSTfk_sUHYESVjMGrArSgO-BlGNJ-8OeK061tMEM8tX2W_qLaeSkdqZEIuELoIeYWNc2zPIYRJU-LZWMYwFNyfxHx7ZTLqVKboVyYGIqARaJ9m8AA19qQGMBG1999BFDaK75gb7zDlaV52niRu1Hm81b088ywfMNp740zkx8TzqXp757qmunCHkcjTF3C69judb-2VA_GK3mZCC39dgdD0izwQq6noQ2_nV2sSNX2SSbItfT2Wsg--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHLfuIK0_jaLUUcwKuufdyRkMMbuR1R7VLmNbMIcv7Av9xpiokEo_iC4NRNCtNRMqKSgrFbjHii2edyYbDfbyPBy7_xL6bkZtPSMcELNZFnD4B5O1bvM62CiiY_Rvi6g785MwUl5K8iBvH8HpIRXJWf55E82zhGTfii0oE1aYcxTMA2NnQejFcqeAi99HQ3yx5W5TXuCObl28TaDTAvfXZAz22hQy3N6XXap6gesRsyW60SFkT0Rq511g_l-3hqJRnl3ZGFRtd8rgjy7GU3soxHXAbkd1ex7xKfcSEP5RPxBSXRh_RlrAug-43xUDem5wemNitk_7j4XMXYjjcv2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPIk-GNaZWqVNXWen8xZoB6wOOgtW5npGo6zc3kD4fFO43R1ty5ZOh4BL-PLaStUGSqJUPFDAGIgc3bYSeCLZrpfxOKL-nm7fvo1yy_i3sIQ7cJSlXZQIcF6mElsqhyYTSl5gWpq40acEP3zhjNzmBumUE05Fuk_q9H8KA-gxfJb-xAF5DXFUiDkPZrk1AiAdCKSs2iS9fdxCMOi7PGjnv5l7NvPyyhva3s81AXoY5hTR4lwMN2WwxcTFC1_JKEDqzSFhjd_SL5cij5cMrr8Dk-_vwe3hSRQo0f98dUWnLmM9bvFwgef_Ouzw893lgUGqM8se-FbygD5CIGufh_VWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSctVH-X-7hZFRC2ETULIo9Hks8l-rYB2Mu9Xrnp9sdyRZ4h2oCo2zchtcB6n2g_pSn1_a2CdXXzdJRI9Y8fCjWrfQNy6gZ5eVfOudkiU43ske0a6DN4A4J8M001gN1v2PtdVsJUyjMEUO4cUTARIFpXfSor6Yr-5mpbyKkzrvvd_mOGFGH1BIRgWl27yUmAs6pq-aCcFnq5-ItsVXyiKszWQjwiREfXK_JzvcRV6AG9a6HsafOgBU4qfSs5dDE1CNQFXCMpVsS1iuyIMKhfq3Qki5SLcLF2Uwh4gjQYGH9OQOtG3G580trmPymDq8lW4ffGGgv81VaurF7BCmeJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_b2l52hAjiL-EeMdDHR1xGf_fzbROaQmO5t2hFVZF3wTDt62IjZwm1QXrgQObpL7cBts_LCtj-lxgIM5yLM0s8bW6EaClT6tOaJ_a2JpmtMqOWGujiFODXfdoZFhP9-ddEf5Zr0uMdN-Ieu8tUfuA-Nj69qMYgOocWCqxv7hKBDDyiOmUvtgWzBXzaVy-6qMSdG5EUN6GRNRumt8yabzo62L1r4KxS09ZhQI5arbG_D08tlz7LWgHsS7lHMie2AemGflaNVXdzYr5K7wSYKn0r-KDx-XErgu15I4ROlqdcvVYuTRrgJpvdUzvb33pL-uJ5OBDq5GED0-ushqmCIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH8QORERHTPcg-mKdWkpu5uy_Je15Q0r3TW0klxUF8ssw1kRoQeKeWqstisCiAe1XtPvJ-uf7GJ9zjNaeQIVroKEgRbry1FFm_VsOQ8haJpHmdnjZvnKATh2xq0QcxWqil--tBIp1AUToFiILXuS3Qhw5Qz5I6DYhNbfHcmuR7P3EYjgQH6Z2AdJFFAHac_bRWf4u8gXxehK0-Qcfjt4rl3N-gAGyrKnPuSJzhu1flxx-x3tH_E8aAbIp5fjXaH9Ba2NOhFisNPZ9ylF4Y4dvMNcS92nBpoRzCkEbixZ7LUKEtxWM2R0vlmH6A5pCNP_PfcAlNUL0G5vL45RWJa_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRDnQ5rgm-mbFE7Ed19m1oa5xz5NJXQ7PrTHCAVR13WASOAMvVlm-BVofPT9NioyrCtnTu1p4uwreFs3Jh-S3BDoc5eEx2VV1iJ3OU5JcvQLY0ni3RiykHl2Bo5B0fViNt8ZmBdrb0v3DoBZKx-8rDRLcbUwMPwnCDvzKWLdEjDfELZAhBBwzYr6Xju4QWwP67Olz11GkWPhLE4ImKzMyePSgf4f6_q9KazOB0_yhemDzA7HT5ixZCE3tTrEnPqh9O3VW7aljH_by5OK7BV0C2vP0ZIMCM1aaThBrBdT87FZJcnMlcQyAAslsbxXyxxxPgK23gdrduPTlQpGrJaYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI3uUYB-uvcMKoQSFW9AbZeulZ1Rkyw04mxm6dKnFme5Ky_pFEdkBTSrjybSN2SZlVM196Zbo0ZsJMFbF7ftgOr8Xe5aiQ8J9OKXN_ak56ufYJYXVM4AKhso_NYKmwArG-_RIAffDAkzDxbYcQVvvwqsxPuxzFkZAsy6aj8Q1EHW-NCxeX6VWCYrK0nrMnqs13pnBC1bHEVMkN9xT_-uJuPHlYp3nnnR3OhTbGmijeN4Z5-wxxrQzNkRADFC-2suXcKTs-F65QG11jlUyX2VpoxTpiZqLJ6cSxFMxjFAkGQ4TFHa82AArLCcWjDAW8v6zRcZRW-JqX0_GNUurf2iXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTSKbkLiUO2yNu12ZHXzoIqmuY2tDgtybnU_4djjbWPZ71cnnMAl6qdRlcQqqljG8Lbjle-IBH-w3_zDVJi87mNZYLSbaX1KmKzc4vUiEtaxbJOiL3TLoO5C5c7P_p5FUflk8Nh0rW1Rn5IxbNZUTd_sdtgYUhfmsqZW3tsBWLtJy5PZumfHm0sEf1AYtPyjvtkzpcVndg4JxuC2DmDr-rG6gUySsoxXbt9QSzK8sYcngJNpfYU5PsmdLzDGJKcsY8qjOhc4h2tMzhHx43Sp8bNAKQrxXsH712IHBkyPApwqFCsI6beTY3HAk3_iHhxj83iay19lNPm-D1NfczE9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPixLH5UxuOpBFzYW6Qa4MPIScuRHBMthLu1XyoR8y7iBrrrKYUyH_K1ujoF5HJekQzfM0TfQHLJZ-JHhEtt_I2U_dDz_HlUIDdWEQ3NoY4KW5v60FsN91hfzc5Mwq5CIWYPVhAatGlXFTEekS3mpjuLA5C12JDbRzyFiEm7OgjAYw-Y5Hy-saJdPoLbsz12HNKm1Zoh6Y9lrveY5JQ1uMLo6wLpPSUj-KH8ijz6LmNAQZn1n3dFZl3cGhhHHdXW6UvNiYUvnuogMSshP7-NPrr_oCwXXlLWT78LxmPnowcjYO3yPiWvhpCV-43IN7VDv30YNNIVV3kVwoXrTlv1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6wLox1pUDilSxavPvuoUAcC9p9aPtf9AsSSBlSQS-VaKfxIXYYAzvydxBnRq8choKf685s4qLfskHNMqf7VKaGCrUWSKJOXqy0c7HEkYi8y2821FszEEx3qK4QnOpf7ENICQkamiEL6jJx8-rzZj9ja_8YXwxdc_jyLf9bojUUsZNO6mb-B6E7oIDzugKTj15H75dGajiURtVLUFs6GtQkHIGlphkzngm3YZ4kkfKztAUXKar_KZw8xtdqr_PnQSdFok5mi9jc6SyO3yMY1FTrCgkuR-WtizqVVare5UBih6yZ3jU_4YO4isrd9W0ZbUOdl3XbfMGcLdsVXJ8AneQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=hOKC1ySYF2t1-cbcvORTCvwd1QK2kyUyDcn7qBKn_8HE3jhSodRA2BvyClqIxmOveu9voUmSPbS2RcMDbjI5uw8rQaK9BhLxMEaIhimshP11_2giEB0lnGN0W2ffEouYQsVKzjTz4vSlbfV9TnZxkrNRKBkQZdXNFD2T0bajnxF1i4egONwq9_O-x1vkstVXjwIyLCjwLfvX4KuKwww8R4HilZCaGqeSOBtTmHDmPa_lMqmrBOkLH7o0IJXpNpTCUg_krWgASzqPD2VO88SkVijUrSGkVuXrVnYMA_bR6eqUXKrbSo7PFncT_7AYyVoekNEk0QWT8XcHN91aqbZnqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=hOKC1ySYF2t1-cbcvORTCvwd1QK2kyUyDcn7qBKn_8HE3jhSodRA2BvyClqIxmOveu9voUmSPbS2RcMDbjI5uw8rQaK9BhLxMEaIhimshP11_2giEB0lnGN0W2ffEouYQsVKzjTz4vSlbfV9TnZxkrNRKBkQZdXNFD2T0bajnxF1i4egONwq9_O-x1vkstVXjwIyLCjwLfvX4KuKwww8R4HilZCaGqeSOBtTmHDmPa_lMqmrBOkLH7o0IJXpNpTCUg_krWgASzqPD2VO88SkVijUrSGkVuXrVnYMA_bR6eqUXKrbSo7PFncT_7AYyVoekNEk0QWT8XcHN91aqbZnqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf75VGo2JxFUmtP1BoywEi-GaxTE6uk-60--X_vJa6Dx7b9v8RIrcUQ1-HlbtVZwyHY4TFf14fLEqLKCcyUXYvG3q2ZNx2KRlO4QenQwoM-4CHOT94tzzdoGRSv5nbb8lACv0ZQ578VIMGZI01mOMt-znpekd-wLl-XWvH81KD6wGp6HuwSM3lNgHaVkBCQSKnBucDuapCQSKaLnRfW-SzcEVnC18YuXRIRPxhna6gOa6wQ45wO_FZsHCh4FyIbvAtpgYUzNrarwxfC_ez3QXugt-jK1nZzo63jWt_Qo-TMLYxoo0AFuFf7xnqE5dQVofvx2bsvihxRp6kjzRpw2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=DpkMSneGflVNrUn2bxIBk0P9K79qZtv3G74BZJLGh-XZIPe5K-wawnQmnoToRA7ouvsZuQrcxXb8RVQgf4AK_lVdii6e3Yvsir9RMXMxaGZ8oesFpS4qtMFjWoFytlEJ36W-GxJXo68M-W1v1IlwcTIMWo9CKY0nLFzQnOO4uFgPbgCGfi2S2xntNspTBplhVLOVtMh-L32ZC5LYItuzszZEyQaB2IPEjYFMW7yypPSBrGZpIMtHAje1q7Rg5Um_5ZuTJYeyBntjtzsZ40Up_wQW3K8MrwE_52AFYgi5Bn5h2cwA4SXRTF-BDNP6zVfhbmgcbcVOu2lr11sRR5O9Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=DpkMSneGflVNrUn2bxIBk0P9K79qZtv3G74BZJLGh-XZIPe5K-wawnQmnoToRA7ouvsZuQrcxXb8RVQgf4AK_lVdii6e3Yvsir9RMXMxaGZ8oesFpS4qtMFjWoFytlEJ36W-GxJXo68M-W1v1IlwcTIMWo9CKY0nLFzQnOO4uFgPbgCGfi2S2xntNspTBplhVLOVtMh-L32ZC5LYItuzszZEyQaB2IPEjYFMW7yypPSBrGZpIMtHAje1q7Rg5Um_5ZuTJYeyBntjtzsZ40Up_wQW3K8MrwE_52AFYgi5Bn5h2cwA4SXRTF-BDNP6zVfhbmgcbcVOu2lr11sRR5O9Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=nGo229QEZ2PaGWk01aVrVk66tqmRX_jnuPzNZEKadmUNJrMftptCiBqVF67O9vbVf9B1Mdfs4m1Jq55iBZSZ6Df-0r7F1D4UKWK8npIE0iqB4PbT40qBnSfe9_sHJStMaBXh9hko33zvjhMVqGEZ2iZUDKv4vHJptzZZASLE-zB1MBualaLozdNnvAHZKA4mMhw_13s6n8O4dRMjNFiYhOYAqEggFEO_gvgWgKv7mk5R-hU-vEpBk0nAvNbFPQVtx17sxhqHv0ZjUlJTSulameH6GqZxWqsuAdfILiGxaXBqAXnDG0t9BAPteDfKi5hUWGmVUqKyKkvV3qlZTC4duA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=nGo229QEZ2PaGWk01aVrVk66tqmRX_jnuPzNZEKadmUNJrMftptCiBqVF67O9vbVf9B1Mdfs4m1Jq55iBZSZ6Df-0r7F1D4UKWK8npIE0iqB4PbT40qBnSfe9_sHJStMaBXh9hko33zvjhMVqGEZ2iZUDKv4vHJptzZZASLE-zB1MBualaLozdNnvAHZKA4mMhw_13s6n8O4dRMjNFiYhOYAqEggFEO_gvgWgKv7mk5R-hU-vEpBk0nAvNbFPQVtx17sxhqHv0ZjUlJTSulameH6GqZxWqsuAdfILiGxaXBqAXnDG0t9BAPteDfKi5hUWGmVUqKyKkvV3qlZTC4duA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYY564moLdhhrQUGpa1ACo0Syhq0ZFkTbdL3gHPwGXF8iciTWSCeC47mrZFhaWRZFz8pDz-goOoS4PrO6JqVLo2AkOFZmKSEKUiRPcIeYsafvm3270HfvEh65tw0UAwoXVtRa7sv6_iXBNs7w0p1ZJ3vSy15uZCwBpRJBiS4yzpcrZjkp0p2zNvQaAnA49oEHA62RJFbLzEHtgQU3OVOJ8nKyFmP8nEJM4hdht-_gMC5ztsv3Nuph7pRxXdsnA4LFwiX2H6LVrNpLB-G1GM7s77d6lAdoEwenaJ17SL_GaK0eWOnQRurkajvQSj_Q1isI89hkiiW7JrmPN3uySQ9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nuQtJ3OFeLfuJcz2PCxAlTXWKhbs3ehxNavY8Jhl4CLIW5Jq9GxywZTehtT_REjW-K41zT2jJN5AlFhsBc_rG-3V04YxxLws402DhY4l8wpbg3Y8UGVjUOT73OKjI-I_A9ag9o0GlolZJIm4da7yB8YCemnnvqOPs0EBUNMUfBOFB-ryxT51USol56-Kbc96kFPiE7_zpjSr4Epk_po1e-xcgB9zI4u83LhFTJGk-qouqZaFcDsyUpwr3VLo1uHBV6RPlcgXJbR424F_pVX0grs9EdMBkeEwZVCkXYedIo1t99rfdbAt0PgYtiTQQEldVo7rPNjQeJQylMjAp2cBsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nuQtJ3OFeLfuJcz2PCxAlTXWKhbs3ehxNavY8Jhl4CLIW5Jq9GxywZTehtT_REjW-K41zT2jJN5AlFhsBc_rG-3V04YxxLws402DhY4l8wpbg3Y8UGVjUOT73OKjI-I_A9ag9o0GlolZJIm4da7yB8YCemnnvqOPs0EBUNMUfBOFB-ryxT51USol56-Kbc96kFPiE7_zpjSr4Epk_po1e-xcgB9zI4u83LhFTJGk-qouqZaFcDsyUpwr3VLo1uHBV6RPlcgXJbR424F_pVX0grs9EdMBkeEwZVCkXYedIo1t99rfdbAt0PgYtiTQQEldVo7rPNjQeJQylMjAp2cBsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5A0Etty-xJqI_siXj-sS_ga2J1TdYuHCZb6sk5jvWzrv4D5QfdctZz1cvi6NouBWpRxB9reL37aub3KmNl89fjXv6wXls03IbExLi_qGS8lBW0NFWgatkovYrxLGIBBv10SFXNklSkxCa3rqHZ5NPJ9nrgW8xY1U1ff0pxUUBTnEaVnfYeSIgzRmhFrHUrtsnnF8YVgotvEmG1Xb9oj6CnLnY4eiwQ63LUO2ZvBIby6pI9Hlr9a_htitvh0BxrAjyGsLUhnua9y5td20wdNjcGxy1JjZb_6245c2h05N0B49oJsqxC6_G5qqr8kIIfA9DWu7TGf6woNgXdIkxzHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQgKVoxqhXxnOUO_zJUqKGyswB-X2BfnqScXBQZKYNOT9EF0xnmgkMJrxWB-PsW9__FyrrpCoEHZ_KYk6c8OkXc5fzCVex0L9AKXbC1W8_nMRc4s79IXCyk1O6D2Pt96NKgNxrW1naWIkzIOLxuFk1uCwznQrWIvo-RKVWEJ0Uo60GZT4hvB2yqgvvpogQNXrQLBLxe7izvut83CbhOU6nMFS3I0pu0Xe3At32mbP4qIpz36y-ttW5Ghx9K4scNKc6s09BX7M2SiuJ83eGIUwhToc8fN0L6p--vtAg4WK3JRLJeQNf39yWYTfI7MsIfvSP7kYO7VoCTNCgPZiLk8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibreCFCkD2lSmsL9JzqBkr78FkIJes9rRsli58BD0w5rrwMDhj5ANcN-5mswrEJeabnMe3it9M_r0Dxq70ApkBCipdZNJvu__LhP2nQ0KAVR_Hdwqp0cE4BIwubd0tg4Ap8fYIsCYDPzymZJMyPqRelfQ3fOckIptAa_FDAwRVbX-F0o6wmfPODUH2Q-7NI-ltNCkkMvJKyFiPzNLr79Yzalp9Kv3BEejyE1DbHQpg_ZNSpvcS9CVtKtYx1Fpv0Nl-w4xPNLDD2qv4iA5WgRvrd2rU44p3nNhIqDsxaUqF30LAwszP4UWm2jGcQitRvphHA3WGQ7b7FmS8G0Hq68Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdBcqrZ4hxo00eqfviiE3AqcDJpzDkBn4FVMSquuagrn6_MMOfU68qoMdrRxMrVnZIYm3O7OkkdIO0G6PGBfLIzGsX6rZf9QM18n-5rbRVnN56zdsc4ALk7NppUNad0ZYvOOtCUvMPLpve8HcSr2LDtnzfMzCSRplWO1J659XSsPDWeMSR1in_pqHuWDhmBy4vFsp0w0wzhyI02xS80aF_0sKb4jxwVs5y3iQCCa_4xtab1D2fuC0SGTOZDcPSzY_X9U_P1ekt7K9y1ANIrgctxhfefhx96cfEcFuDLuUuXFS9iEXcbSj0kvFVOPxja0CSQ4iZK_yjiLbGGRwfrXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=XpW4eeIWuRKjFRv4uVyT5MqR8LFp4RSx0Mpi_7VSJm3ArtMcAihezmzUCISKufwUGp3DWMfsQYE0uoKZLnplRiL8qZaZcSQ7jJOJ-doUaGwyTRUws3wgUnL8ahgc9oimVUaW7PsOZU5fRER1lfg9eJadv-3YXuDNY0AZX4UN8kQMF8hMHqiiCfz-pMwPaWNmZG6l5I6ZXtkfqF25Y3h7U4RCcdt4X5yGeWKnhy1l5LTV-0jXOQuZXXwK0u4YEk1ctt8kpk_F331dZZwloMd3WBE3pdqN4-MVit6GvhX2oiSajUBk0mynKfuYKNO0wMNBF3R1bG_KU6CtZICva-IrPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=XpW4eeIWuRKjFRv4uVyT5MqR8LFp4RSx0Mpi_7VSJm3ArtMcAihezmzUCISKufwUGp3DWMfsQYE0uoKZLnplRiL8qZaZcSQ7jJOJ-doUaGwyTRUws3wgUnL8ahgc9oimVUaW7PsOZU5fRER1lfg9eJadv-3YXuDNY0AZX4UN8kQMF8hMHqiiCfz-pMwPaWNmZG6l5I6ZXtkfqF25Y3h7U4RCcdt4X5yGeWKnhy1l5LTV-0jXOQuZXXwK0u4YEk1ctt8kpk_F331dZZwloMd3WBE3pdqN4-MVit6GvhX2oiSajUBk0mynKfuYKNO0wMNBF3R1bG_KU6CtZICva-IrPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=TwDQmbktOODxKDIMDMgHxMhtEygUEg0NXboiqZo1kqufjMEq7fl15Q_k9aRq6VDZqXwR-BX_kz1iN_ZLR3iCgOb9gbUSpBnfNjaw_YXF3sOttk5AYe0Osw1vPHxarIbGQm9i7rv9FvZoPKHfd6W4F98HNwhAbyoU_CuVo_eO0bXLVLO_wNikJGKPaHBy6lk0YW5WZdOxyDe1G9HLSEabA433sLQcmAhUMzTJ-K0Wk0ICHMRf9Lltv_uOeLewAlCWOh7B0wdMTDGp2Jubk7Z4k7jLjZ18Q0KDZ9wjrvF9e_9a7NvjkCCmE67P1bICMUof_pKKbFWDJ3bNJT-qy8r-eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=TwDQmbktOODxKDIMDMgHxMhtEygUEg0NXboiqZo1kqufjMEq7fl15Q_k9aRq6VDZqXwR-BX_kz1iN_ZLR3iCgOb9gbUSpBnfNjaw_YXF3sOttk5AYe0Osw1vPHxarIbGQm9i7rv9FvZoPKHfd6W4F98HNwhAbyoU_CuVo_eO0bXLVLO_wNikJGKPaHBy6lk0YW5WZdOxyDe1G9HLSEabA433sLQcmAhUMzTJ-K0Wk0ICHMRf9Lltv_uOeLewAlCWOh7B0wdMTDGp2Jubk7Z4k7jLjZ18Q0KDZ9wjrvF9e_9a7NvjkCCmE67P1bICMUof_pKKbFWDJ3bNJT-qy8r-eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=a62epc3oi3-_jN0LHt9WwQMtgMdtXuX7Ky5fYzYdKMojyfC8LBJ6H9r77hHV5SyM_Je1W2NTJJk6W8teQScpnmDZmRaMKD34gj12QkJNX0pBuzUFZjnle4F080DGCt0sEs1UD_M7HuIT6hu9t_0rCC5hLRZmhwXDQbUQPim-7JSgN7nNN_Gip86z30gJg-mgQucsrR376T2e5MgBW9yeCPE7IJs2K7AIzX7k714FIE-1vcRxCDeNg-pQ5yrkO-kA7pHMfBz9LhePIL57B0s4lzxuhDK3qihFtR1IvJKFbwjeUTk2yu1RL7EaMKWsIGyp6DiiIZ9CaRJNhMjfohVLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=a62epc3oi3-_jN0LHt9WwQMtgMdtXuX7Ky5fYzYdKMojyfC8LBJ6H9r77hHV5SyM_Je1W2NTJJk6W8teQScpnmDZmRaMKD34gj12QkJNX0pBuzUFZjnle4F080DGCt0sEs1UD_M7HuIT6hu9t_0rCC5hLRZmhwXDQbUQPim-7JSgN7nNN_Gip86z30gJg-mgQucsrR376T2e5MgBW9yeCPE7IJs2K7AIzX7k714FIE-1vcRxCDeNg-pQ5yrkO-kA7pHMfBz9LhePIL57B0s4lzxuhDK3qihFtR1IvJKFbwjeUTk2yu1RL7EaMKWsIGyp6DiiIZ9CaRJNhMjfohVLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=RgqA-nBjVWQ7urz9dLflRTsJHAVyNxOYZrix7cjpOKoWcgQV5kQRQVDvh8_WPFnzgO8uhFgSUWa8TyXUxjafiIyx9T9nLPefO-MXxmtuFJI-Se8uTnAWRpArbJBamZ4QJ1vy73eiyH3lXzit8iVH0ymkSgKq8d2JUzWXqbrawiPBB_J4giB562maJYP-1rB86pV7OPoayXWF2rboRFNJyzpfgbHDVpRVnL-ISpF6t37HS7CsYPm3MPJoYf38KbKJ9qIFjq2H5GXG8xpswm2ReHBWmTE2HC9XE4Qo_PKoe3VczPh_ykTOnmocBInoIOJkABHsV2FmQQk9yuuVSZ-9HrERae4O3wN9TIle2sHsbOmXbSwxtOai5pDHZR015ASPD3HoObp71uYIIu2evap28AZC5_cX1k5MatEcgeuHHHXiHK5X0OYat4Ug_AwUs1fJd2iIsMyjr4D762Og_c2v6oNbcSqtK3RmI7P0EfR_iF_1XOeQlVzRkDhMU7RCD_vXwBLep7Y-bmKtCBxhBGDhHApNZF21KmEFc2WETBUdc_Xc1v8uNydR7UdA49idnJCPOlSTlaXAVjCde77Kt7H0pMbKzOL6-LilHQWVMZbfNVRxdJFYNtEsMjpsVaCpOphzkrqQrZ64mJE1XbKJDYJouz8M89-6y8rPsLmZXaT3T80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=RgqA-nBjVWQ7urz9dLflRTsJHAVyNxOYZrix7cjpOKoWcgQV5kQRQVDvh8_WPFnzgO8uhFgSUWa8TyXUxjafiIyx9T9nLPefO-MXxmtuFJI-Se8uTnAWRpArbJBamZ4QJ1vy73eiyH3lXzit8iVH0ymkSgKq8d2JUzWXqbrawiPBB_J4giB562maJYP-1rB86pV7OPoayXWF2rboRFNJyzpfgbHDVpRVnL-ISpF6t37HS7CsYPm3MPJoYf38KbKJ9qIFjq2H5GXG8xpswm2ReHBWmTE2HC9XE4Qo_PKoe3VczPh_ykTOnmocBInoIOJkABHsV2FmQQk9yuuVSZ-9HrERae4O3wN9TIle2sHsbOmXbSwxtOai5pDHZR015ASPD3HoObp71uYIIu2evap28AZC5_cX1k5MatEcgeuHHHXiHK5X0OYat4Ug_AwUs1fJd2iIsMyjr4D762Og_c2v6oNbcSqtK3RmI7P0EfR_iF_1XOeQlVzRkDhMU7RCD_vXwBLep7Y-bmKtCBxhBGDhHApNZF21KmEFc2WETBUdc_Xc1v8uNydR7UdA49idnJCPOlSTlaXAVjCde77Kt7H0pMbKzOL6-LilHQWVMZbfNVRxdJFYNtEsMjpsVaCpOphzkrqQrZ64mJE1XbKJDYJouz8M89-6y8rPsLmZXaT3T80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=oRcowbpIxhBgD-H8REY9cJtfUSyH927a9YwOM8ASkqBZxRftz8t0el1Ye5y9hdrofyd7SMocT-G8oarfn5nkXM8tAR2Lo0ZshIQ5_36fAKtFnD93msLbiyVkM5uGCsHzcyZ8zdrzXwG2s6ZKfQRN95kKzrSTtCJAqatTfjO91tMFokWbjvuetzgTUDmbRGnlHGXWiPbfzUBwSEZMP_GzOIRdOSImISQG61Fk0pVfk87vtAQwYuVkDSQ9IyvTgG2lnwsVi2ruczqn5UEcK8E6d5xR8I8KOToXzwAa5Fs1-F-QNPsX7ls4CGvI2b6o4qQN2oWlCtVp37QNkF6LiYwSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=oRcowbpIxhBgD-H8REY9cJtfUSyH927a9YwOM8ASkqBZxRftz8t0el1Ye5y9hdrofyd7SMocT-G8oarfn5nkXM8tAR2Lo0ZshIQ5_36fAKtFnD93msLbiyVkM5uGCsHzcyZ8zdrzXwG2s6ZKfQRN95kKzrSTtCJAqatTfjO91tMFokWbjvuetzgTUDmbRGnlHGXWiPbfzUBwSEZMP_GzOIRdOSImISQG61Fk0pVfk87vtAQwYuVkDSQ9IyvTgG2lnwsVi2ruczqn5UEcK8E6d5xR8I8KOToXzwAa5Fs1-F-QNPsX7ls4CGvI2b6o4qQN2oWlCtVp37QNkF6LiYwSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=kxpf1OLQiiPPLJhjGIhoun6GbluNYeavYGY_1AS7CmcNmVF6HEnUjs3y6Jtpwqwjf35309cx8SVwPW9kfy5BfiCCaRH3DFAYE5q3vUD-dXoXIf6SVq8s-RXSzNNj4WZfZcmLQCLcZrtVkgbK50AwK1vLdw8bIjwHP9RQa4SHvIJBiR1MHPdbvuE1ZOELa808ypy30IDyAdn4pBFeoaazY0awZAoz4svramOoOYACVcT5Y_tvyVw7JoI5X4SZ-8LuOHCiMspm0aUdeXQ-ZB5-g6qWGE3L7CGeXGnqWtGyYuC1VgiX7gqCQQ6wqp0Eg6-MCsgsxsRGOeLUmy-J_KO2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=kxpf1OLQiiPPLJhjGIhoun6GbluNYeavYGY_1AS7CmcNmVF6HEnUjs3y6Jtpwqwjf35309cx8SVwPW9kfy5BfiCCaRH3DFAYE5q3vUD-dXoXIf6SVq8s-RXSzNNj4WZfZcmLQCLcZrtVkgbK50AwK1vLdw8bIjwHP9RQa4SHvIJBiR1MHPdbvuE1ZOELa808ypy30IDyAdn4pBFeoaazY0awZAoz4svramOoOYACVcT5Y_tvyVw7JoI5X4SZ-8LuOHCiMspm0aUdeXQ-ZB5-g6qWGE3L7CGeXGnqWtGyYuC1VgiX7gqCQQ6wqp0Eg6-MCsgsxsRGOeLUmy-J_KO2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrGoXt2liRCHiqi1Pr8LPIpt7YlxyfD3hOZsXPedvydjO71ZkxIOD7coyWTvqJqM4i13Fx8nL6zSF9lQV44jvyfPsr_tT0PxAFfkbQi7hDA7bcnlq7U7hhFjt6qlrSAUMaNuYD7_GbieEJ_rl00miFkHBwIZKQ1On_nSjc1H1Oy-3nNsHdq-316xKGRj1duR56Cg6hqFbe56V2_W1qK7mtsCDa-gal8mVP-NZPrAXdUx0LozhjfLkPTX5LmIBm8BR_t62butz2lsLyC6jirk1nXlsFv9-YD-3Drb2ojizWFX8s9lersvLXuS5GpYdMBUZUCqNP5t9eA9QRj13nhleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=qy26VWL5yBpkKkAYyVKkKfTcXMy1scLqo-Gs5If2EAZcfo8i9sJrCeU_MZMvcwPCOfNxb2CSbSJilSCnxN9sgbAr3f8i8BJNEvzNMt50Dz8XIPhOEd2V4t34PRSCwJvwYyZ1tLVCPuKAPMWtmTvyB2hAEOuWrfuvA8Cy-ctxLcV7f-B024W4HQEOhruERLUmEgkFSqBrFnQ5kKSNQE0riKH76iVAh-dolfK5GGh4XnqHHD_9DyNthgk53XAIIppkvO0-OjntXaqvIvKV6ojWgn80aJ0FTPN3mPZJcRSoUg-gu_ierWofK92bPQLY9lYMfVVMurFm86XYUC1GQIct6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=qy26VWL5yBpkKkAYyVKkKfTcXMy1scLqo-Gs5If2EAZcfo8i9sJrCeU_MZMvcwPCOfNxb2CSbSJilSCnxN9sgbAr3f8i8BJNEvzNMt50Dz8XIPhOEd2V4t34PRSCwJvwYyZ1tLVCPuKAPMWtmTvyB2hAEOuWrfuvA8Cy-ctxLcV7f-B024W4HQEOhruERLUmEgkFSqBrFnQ5kKSNQE0riKH76iVAh-dolfK5GGh4XnqHHD_9DyNthgk53XAIIppkvO0-OjntXaqvIvKV6ojWgn80aJ0FTPN3mPZJcRSoUg-gu_ierWofK92bPQLY9lYMfVVMurFm86XYUC1GQIct6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM9BmmMaIIJJE4iIts0UWElwn7KHBeqRuxi01vGFEu5c-CipnL7xOsMY3zidn-SGtu-jwJGHeUBuVV117jQ3Dg5deWOp0CwQCf2mA_4mlsMqL222d0boi8PIwieWE61LPNge0aBjm5-r5FN5yhvg0GjhSp4W-tK0meZOp0aLG-mpwxTmfB971ek0tz0Cv5llLZxUO-lwiSHPdPlNGeuSLxTy2DMe4FwcjO26bRjfhNw5TnoW8r48NwvSH4c0RZHlL-aFoF_Zql3sJ2xQiSWtvvCyBiFPxpJ_WiBJ3RJNvSXy11APGMPGu61Yo7QrRv3Klw3DcZdvMjSp1Gv65bQv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCzMVWRIByjyRZIXnp_kgV1Nm-DwThuUKrDo9G4eo1xsAd95ddIegEDmIsLzgQURboNO83jGNC0UMi5zpoKmDQ_8m7yP2K7UY9n_TpBQa4hDtWto8qe1osbNFeSvew7Fhnogttn37vwVdP8iNWk6mgGjjGLIjmnSnFll1AD-Ssg2pekIYeQ4zkZLymFscQfd6UJoac5UJdeHe5qYzT6UZnTTZYk_RZuTfDGj_9gtwWm9dOZkOilX4YEHF-lem6CqT13fpFFT6R5bVYx0mMu-7EFM8fEPz1MNZWJzqOiSs4zV0n74WHh03GnI4SuiGHgTWoMn3gaZY436994dHXt9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=RNc1tozFM97NugChiXx1mZa09TTpcFk0E2WTd3LoaUKijSzKBcxIR5p920diGL6KAGIa874rT1zK7CYZbSxRBfWySHhCKyzi28qW49pjRpYOdVj6j8NIDqfV3vDTGuue-D9ATefWM10NctXgKkDjlJmoi2YrjWIR2eoTphRK7qQWnOKYRI4881NXPEngq1v10CGmg7pHABTnZ9QoIC4yCMC5C2PG7rZQ-iCLb8HyUYwE54zEzJjj8JneQkYg3TchJOzspvrPQrzHA762sM5x7Qi1yB0tc58_UMp-wvqXtnm75CvBUYoH_xSuiytn4HLuAmawIydbNg8bpI79YZl2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=RNc1tozFM97NugChiXx1mZa09TTpcFk0E2WTd3LoaUKijSzKBcxIR5p920diGL6KAGIa874rT1zK7CYZbSxRBfWySHhCKyzi28qW49pjRpYOdVj6j8NIDqfV3vDTGuue-D9ATefWM10NctXgKkDjlJmoi2YrjWIR2eoTphRK7qQWnOKYRI4881NXPEngq1v10CGmg7pHABTnZ9QoIC4yCMC5C2PG7rZQ-iCLb8HyUYwE54zEzJjj8JneQkYg3TchJOzspvrPQrzHA762sM5x7Qi1yB0tc58_UMp-wvqXtnm75CvBUYoH_xSuiytn4HLuAmawIydbNg8bpI79YZl2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=k8fA4YUp-xwU_pS-V1qzbGNAICft08Y_8SYmvg_H4plXyTjY3XJ3XB3XI4mdY98RoQdaF8cXBUP7p_ZPAoAO8_EuoLQqhch7rz-so81QDZef6QxkILMINsStAWMk0L3ONGUVq5QrppzhziU80xzkZFZu58hVW6Q3UgfqqJUQEQVr2DpgH65lgdWa1im4P-04xbI4NDs86RAPolIbjwcA8iNZpo_njDLPo9mZpO5cuKdokv7vawLngNBBMxvEobP1-rSULhaURtgyVR4QrbZzOQGZwCAVJ2BEquaC_4OfIvi8I07h3BMKff2FOKwxcuJH49e8WfwNj-1Ct5jNlehSNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=k8fA4YUp-xwU_pS-V1qzbGNAICft08Y_8SYmvg_H4plXyTjY3XJ3XB3XI4mdY98RoQdaF8cXBUP7p_ZPAoAO8_EuoLQqhch7rz-so81QDZef6QxkILMINsStAWMk0L3ONGUVq5QrppzhziU80xzkZFZu58hVW6Q3UgfqqJUQEQVr2DpgH65lgdWa1im4P-04xbI4NDs86RAPolIbjwcA8iNZpo_njDLPo9mZpO5cuKdokv7vawLngNBBMxvEobP1-rSULhaURtgyVR4QrbZzOQGZwCAVJ2BEquaC_4OfIvi8I07h3BMKff2FOKwxcuJH49e8WfwNj-1Ct5jNlehSNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=eOODdhJRz7UKZ6ywYzq6gbhEYMSg9O2hXRY0JBsh3K6SG426lc3FDxnd1G4Fah2e0Ep5odZuCSjjRPkJfj8IIIbOIfH20GrF0c2QZxa7Il6LJo2dbNdrXjvA6UPDcdp2mJIrpGiJddPWR02t0u-gFGPOtwBnfGe9-fWnAxuhPOLih51WNBuNVRFzJ8ULPkGX2IMsOnC9M3PhGBuVTifznngbfha1qj_X-scNCCML4YRhnOO-ilkWlv6sA8qSUEn6tWj1LtZjxemk8iVWdFZiwg0jl58Tj0oQr-J8WSxow3G8lvQcWovq2bOPCN9dOysyawUBn5P9UVfdxZuXCMYLjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=eOODdhJRz7UKZ6ywYzq6gbhEYMSg9O2hXRY0JBsh3K6SG426lc3FDxnd1G4Fah2e0Ep5odZuCSjjRPkJfj8IIIbOIfH20GrF0c2QZxa7Il6LJo2dbNdrXjvA6UPDcdp2mJIrpGiJddPWR02t0u-gFGPOtwBnfGe9-fWnAxuhPOLih51WNBuNVRFzJ8ULPkGX2IMsOnC9M3PhGBuVTifznngbfha1qj_X-scNCCML4YRhnOO-ilkWlv6sA8qSUEn6tWj1LtZjxemk8iVWdFZiwg0jl58Tj0oQr-J8WSxow3G8lvQcWovq2bOPCN9dOysyawUBn5P9UVfdxZuXCMYLjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdc4daluRd-9ozcUIzw1hSH7BU2OgbACuHaBIFuMX_RFMAPQ1wI8CCGKxOZ1w2sYO-TR2dNW4X7hB-EoqiXslxl5QOgcyadTHkv7qCrq1aWMxzPNPaKyOWUaf-lzo1wfj180OutGhvnrM8PNFEJtB0tOEFU89hchDanS4jXxUhQc_xMnTjYDw5rqelOdIZcSu36lbq64jYjjHNWmk8yH-fkbnSOu_FtoLPsTRnqVzgTPe1DlZPN6G2ZnNk7RpzIzZUMIow6pbG94xiz3g2QNCjUVCpvxqxquvclSd5kwXo0i3MlVsvqll4RlV0tdw7DRUn_Z7jzDCB0mZPH3ir6TRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=NwQv7CKH4XR_zQsCGRUxUcJ21FfN5xUUGHGoXceDicsLQOM1kZi5Sccu0SAeHRc3iAmS2jAZ524RYBttAyj7-ObHfSozDf9Zj1CvrLaEY1J62VdgXJYJ6hVio5aMIup5A7KbjM47beKpfgptqyARYnB_BW6j_NJthzJYkz-9gYBq1AkV2UN4KCiqug-J48K7Gz2IovtL31MeGQhC5MyIbNcJV1anwNMgbvyoOoeOYaLaqTgieUXs5rlqT_3iFkH9iptUZj3_PAAxLYGNJ1FJwDKXMjgu2GEJkiGbE5DdVBTeUl1XRRQvS8cHWFPMZiInBy_kShEoWVIKq7PHIZlgig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=NwQv7CKH4XR_zQsCGRUxUcJ21FfN5xUUGHGoXceDicsLQOM1kZi5Sccu0SAeHRc3iAmS2jAZ524RYBttAyj7-ObHfSozDf9Zj1CvrLaEY1J62VdgXJYJ6hVio5aMIup5A7KbjM47beKpfgptqyARYnB_BW6j_NJthzJYkz-9gYBq1AkV2UN4KCiqug-J48K7Gz2IovtL31MeGQhC5MyIbNcJV1anwNMgbvyoOoeOYaLaqTgieUXs5rlqT_3iFkH9iptUZj3_PAAxLYGNJ1FJwDKXMjgu2GEJkiGbE5DdVBTeUl1XRRQvS8cHWFPMZiInBy_kShEoWVIKq7PHIZlgig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=sZks-qT3s1vubyajwU2xE5KTiOMVD5iw2k2aH01Vbc1ZY6H7uRTJ0-xpKCuHUz1TcEeglkwF4SqZ1kBglE3H5qvb9tM3iHYQ3jz-5PGz-WsFOakmt_g6t2ezm4nUR3uub5k-NAdqVkj-NJgcqHsqjxVNufg65VZfmhyPu_DDDyui9ZmjpyfB7hfeTDF8qE08KY1TvMURAI5vOrHAMMSpFqWUgNRrER9hlV2pvphvS3C62VPOONYg8oyjZ4fOBZ3-5Re6i4Ik-G_GzDmNDGYtLjlpQkhQhuDvnXV6Gx14hyC7UzNhEdziQQmdStjz4Vk41-tXK2LVLC27aYxnxnCHow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=sZks-qT3s1vubyajwU2xE5KTiOMVD5iw2k2aH01Vbc1ZY6H7uRTJ0-xpKCuHUz1TcEeglkwF4SqZ1kBglE3H5qvb9tM3iHYQ3jz-5PGz-WsFOakmt_g6t2ezm4nUR3uub5k-NAdqVkj-NJgcqHsqjxVNufg65VZfmhyPu_DDDyui9ZmjpyfB7hfeTDF8qE08KY1TvMURAI5vOrHAMMSpFqWUgNRrER9hlV2pvphvS3C62VPOONYg8oyjZ4fOBZ3-5Re6i4Ik-G_GzDmNDGYtLjlpQkhQhuDvnXV6Gx14hyC7UzNhEdziQQmdStjz4Vk41-tXK2LVLC27aYxnxnCHow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=JLP8GYb4VFGKCKWnAI7JJYPT0X0Je7Q-0aMIqFpgKpFUfehb-fpUbx-IIGxK3sIIwUSkf-S1R02DRol65w8q6_uxatgnsBRf5LNlOJvmpARvZ7qS1n5Y7LWS-uqvf5np_xab1xWxeXrFdJXjxOBC7k7Al49e5QVb1zuLx17soBeL0cqijyeYkHIFQldvOxRGE-F0A6Q5QN4vI8U6AdrBP9JTWqnz4LYWcpWSt-w1B-B7DXCXQRkVkUvZAEAmbMxXwBgsnYrzmOx66X1X29rJsq_BJihdF8XhAVuUtYAAKSviX2Od73P1Q_tgeXOjXGKvdtzIyK0MJZui0M-CaKSv-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=JLP8GYb4VFGKCKWnAI7JJYPT0X0Je7Q-0aMIqFpgKpFUfehb-fpUbx-IIGxK3sIIwUSkf-S1R02DRol65w8q6_uxatgnsBRf5LNlOJvmpARvZ7qS1n5Y7LWS-uqvf5np_xab1xWxeXrFdJXjxOBC7k7Al49e5QVb1zuLx17soBeL0cqijyeYkHIFQldvOxRGE-F0A6Q5QN4vI8U6AdrBP9JTWqnz4LYWcpWSt-w1B-B7DXCXQRkVkUvZAEAmbMxXwBgsnYrzmOx66X1X29rJsq_BJihdF8XhAVuUtYAAKSviX2Od73P1Q_tgeXOjXGKvdtzIyK0MJZui0M-CaKSv-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H474MawnQPd-ZXLb1pCrm_VLCDdbUc6Hw4sP_9kV4hP2aYSi9M-nY6mix37JCt6rFvXNqJZ8Bo2qRwk_Jm6OsnDnh8gK9LrcNQLSgDgHInNTmi171890PYeTnse18d-xPsgqtnmXgNXdqVBm_ONipz8O9Ah2rYsRN-NLQxjQybabR6jc2oizYtXVgkHbmWyR-JZQBdTtAhmfBcNYMukYxDede7Mzno6Q54hX1ef29GT63tlsecplhtTPCasEWp7TAVuQswjJiz9vDKPO5ihvstRlpGvYMR5cu70e9R2CUjwEhyP6HZP_gR9dGo7KmwC-QlFDyshOD6UEaU2NU2Xaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=KVIBwXbuGz9LbLFK6MTF-kym8BWW6ju658z4YQMT70bzdeeLoUHGdw2kpAODa3uLbfqYb5mu53FGlpQlKrOkDzW78Pe-JWIRBGbixvNGwcGnWM93b2uTLjRe1_A9cpVoM1sZLZhihQgtWpogiWbs5x4uLGAP-z_z_5rYf_0GrH7by3u0RDYPuET7_fHl5RFBEc-tLuP_85Fi0oT5nAH76RvxuNUTN9H5jXEnl7VF4FePr9IeyUSxz5390JcRcZLFgzY-hfkcx7rwXgGhc7GP82HBnvCo-Fs4kg6gEeBZassVgqAHKMAHVqL7FW1tV5FZIU62H1A6mfBMGrc9R_qHmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=KVIBwXbuGz9LbLFK6MTF-kym8BWW6ju658z4YQMT70bzdeeLoUHGdw2kpAODa3uLbfqYb5mu53FGlpQlKrOkDzW78Pe-JWIRBGbixvNGwcGnWM93b2uTLjRe1_A9cpVoM1sZLZhihQgtWpogiWbs5x4uLGAP-z_z_5rYf_0GrH7by3u0RDYPuET7_fHl5RFBEc-tLuP_85Fi0oT5nAH76RvxuNUTN9H5jXEnl7VF4FePr9IeyUSxz5390JcRcZLFgzY-hfkcx7rwXgGhc7GP82HBnvCo-Fs4kg6gEeBZassVgqAHKMAHVqL7FW1tV5FZIU62H1A6mfBMGrc9R_qHmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOWwLKfR84O_qjzDb0quLG91CbC4NUOzqrQDvI-n0eYgueDIzA2JKDg_NsM56eMvBsMwk_m9TADD_JiFzthJ81Q4J2SetuC5xwZj7IyDBuUefR_s0t2IUU7PFGleN4FJB-wAYTV2-Nz1si7D07i1WYDBS9PtZ8HcbHNZINmZw96kvtWL1N40WWO41BQR2qGfRxxvM-Hbjh6cbX0s-7sUDhpEYFvUK-8j0wFheUpWSYQcLY0E0G9FFFBqVUQF7gUHI8F7IB0AMV3kJlD4-rURlaW4_OcU6VslL3T5HiPUBpHkaVK3KPngUKZvWeN9iAh6zS_b37u0Yy2mG3R6V7iIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=s_InCsSi9IZqSpJrtaXrEKI_3WxE58XVHT1JdOKOmLQuNhCG7Q1UbNumR6HVGQKsGnF1opQdWjV2VttaeyCLUQwUILdrEhA2l9y513FD7AvD1W9u7oInAsnsaUxMoIXWREPoMl69ZnNUtLv3M3YSURgMXcpD8uErQFGsJJaAbsimdWgqCRRJl1yvb_gav9N3_cMf9IEDkpkGqojV3HtCHKLcglA50Bd_-voHEarEKnRMSPvj5NTj6G2k2JXJulv26E8TedApqKbfMdccX50suJ7T7gbYzJ8v1NQN6qSGzE9GZ66GGcuFb8x-_atXwQ_vP-rRXg67zj-aR0_lCCjEhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=s_InCsSi9IZqSpJrtaXrEKI_3WxE58XVHT1JdOKOmLQuNhCG7Q1UbNumR6HVGQKsGnF1opQdWjV2VttaeyCLUQwUILdrEhA2l9y513FD7AvD1W9u7oInAsnsaUxMoIXWREPoMl69ZnNUtLv3M3YSURgMXcpD8uErQFGsJJaAbsimdWgqCRRJl1yvb_gav9N3_cMf9IEDkpkGqojV3HtCHKLcglA50Bd_-voHEarEKnRMSPvj5NTj6G2k2JXJulv26E8TedApqKbfMdccX50suJ7T7gbYzJ8v1NQN6qSGzE9GZ66GGcuFb8x-_atXwQ_vP-rRXg67zj-aR0_lCCjEhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv8InVJXOpMf5QGgyJH49MuioRda3BYPRZQNv-0SKYPCkETQVd85jVNgeGs3jJpcIlj3qa75VCdU43vblpl0Fqz2QBWpqDu5M0kJJZi0esCJmOt2yf1R-oOUOBFc-Z2Xeq_O-Rs-nhZec-PJOw4WeEizsnFIsgeBCRwU3jTE2X9H50LwXSnsnyh0sx9be3jBdk6Gw-3-OCMQweV8m00NmfJMeJDgCHVZ55tL_RTlGOioVvgu8d3RZ7Nw_lMO8cbZBxy8eusV1vhcOWPhxj0-Mu4d3QTH6sAuTa-qGUuZ-YxaCX5L_M-HFp0XFKMcgrff9EKBBN8u2tPTWV8nWPDh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=JCkWlOK4X9bu2lx92K-XGesJUthfsmWJ_5zyjo-TgewYYwefuLF8QV8KBTIVMsbQf96Nk31XPGaKukpu6tX70kTXvSMagYQsHA1AhM3GSn7R6YP_dzPP0XmpnHanpAR-pdwzRknF3xM5Qxb_akmB6f2Oh6-EpW3tJzZtifKUMfUfilAKY51eoNjvflIvR1WSHu6TAVyNQBUix3hsgY9p_bsj6RyF5miVtDDAaPUDTZwbqKYNeZrEC2XFJ-YspeU1lJc8f8LGmjylmsyv7GMkvITb1ZCT-ARUlut9NZW61mr6Z0XbUPRpntbPuijKEj5W-bH-EFzV399Mgw1gQ2sa2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=JCkWlOK4X9bu2lx92K-XGesJUthfsmWJ_5zyjo-TgewYYwefuLF8QV8KBTIVMsbQf96Nk31XPGaKukpu6tX70kTXvSMagYQsHA1AhM3GSn7R6YP_dzPP0XmpnHanpAR-pdwzRknF3xM5Qxb_akmB6f2Oh6-EpW3tJzZtifKUMfUfilAKY51eoNjvflIvR1WSHu6TAVyNQBUix3hsgY9p_bsj6RyF5miVtDDAaPUDTZwbqKYNeZrEC2XFJ-YspeU1lJc8f8LGmjylmsyv7GMkvITb1ZCT-ARUlut9NZW61mr6Z0XbUPRpntbPuijKEj5W-bH-EFzV399Mgw1gQ2sa2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuuaKCNuPvkCJq3Nxjx6IjAYTPc7bCHIV0SxrI1gbTF5GC7_0B5cJ1lr3Yt8UwfCjOlATdQZEAxafS27-mcRdLggGb_XNptpwRSwRsU6nbkQqmg8U7xuLDaQHv7P36ArYlZMiJC7FDjDTBVlSdHCxN898rmQ1xnjDV8QQYb7v0MeHL1SqOh39MIL2ZUmqrhY3IuV1uASyJFcs99tBFo4PhcbE8uQaFm3Bbu5n9Rnjnp5tvm7Te3G3ksYMxxAMYuMIz9jW_9g_hj9cAroZX2-rsOH29BvxL9oWC30naawEjpfMn-OFqkXd3dKBLxHAksiOspTs6X0vbm9Fw_n268XGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgK8ieBsX0zecOjvkcIQZ5-laxuEzd4xcU4LnxGaQoXMVexzR9Gmp85cSOIg8wDEtWIpoXy3twFzxHBTzBzK7vcpBPm2TiZ6rKKxMRIUtIhsQ6yitUsrZZ1ZS_laz0g8KFV1z3VTK8U2Y758Vuc-__EtfXxz_FXO2BD5zSmkeFHBALLMK-jgOR7yXvLu0AhUHpghjiryjl7IiouV0jL4CIeBQZHsBXpn-a09Qkr1WkKcSqaI_C_tyWOZKhca-YKTmGuHqCfhZbe0_3rbyWAlTkvA018zUy4zyVBzVNexS-q7SkrOnH0CcKyDk8ti0MJB18TQOj2WGmfSGsrdwIZ0ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=pApfRQwit1hATUqpYztg1vUiqQMdiSxwlAj3_TAq9L8h581BwU3rPkF7z047nNaZK-UP8I-6Dj5jx1GRfpE4MJg2GgLWC3JOkwC78rGfRNrb3zS9ZBwkK8p2U0ATULZrnEuScidHxQhyf3ZXmIW66H0QGPtGC0tIvCxnxl9DEboWMDyeQsPUKnvJwXlej81AY4yImvTM6cl3rbiaZJ-QAigXTA2lAt2UTz8A50HCjmUNQvfXvNzzFhVetxE70RQ86k_4-W3AngBGOfUm-bcw8-AeSJ6vT7mPdW_ZWPJu1DHqtmLjXu2uDItzY9nMnu5UapBefYH8nOjJGgcCbXnrwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=pApfRQwit1hATUqpYztg1vUiqQMdiSxwlAj3_TAq9L8h581BwU3rPkF7z047nNaZK-UP8I-6Dj5jx1GRfpE4MJg2GgLWC3JOkwC78rGfRNrb3zS9ZBwkK8p2U0ATULZrnEuScidHxQhyf3ZXmIW66H0QGPtGC0tIvCxnxl9DEboWMDyeQsPUKnvJwXlej81AY4yImvTM6cl3rbiaZJ-QAigXTA2lAt2UTz8A50HCjmUNQvfXvNzzFhVetxE70RQ86k_4-W3AngBGOfUm-bcw8-AeSJ6vT7mPdW_ZWPJu1DHqtmLjXu2uDItzY9nMnu5UapBefYH8nOjJGgcCbXnrwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzoxPubp5Zc6kJ86APTa5_qB3txhJvRF5vMUj9QNxySljhvBjpTAHEhaDAb-jQIHMwYwjK9plyHqvFuIMXkDUXZ_GOUB8OB92fCIOoxNnbpW2jop8sCcH5RlVg-3NSSmslaVgC2Mv7ljuK4jEHQ_jjY6BrDBf9OdmhkKxflTJgE__l25cSbbErixY7oREf7In1DaZBFyL6uSDw302wmUO2L4VhsOspbo7F_SR0k0LaJqDG_2_JVRhI9nf5zsGZ9FGkhnvFaeWQhj0QM201iAlXyXgcGwIWCutkTuznamfe-OBX0AXRJTI1Mgii69YvvarS7sNeGQqa9e2oHejTI9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqqwhISpmhWS738kZjPCBiO_fJ5t96FswLTmLUHbYytXz7IKG44CHqsyPIunZ4mQh0P0RMUmEtoy1kg8K-fUeQDw5xBLFpWxW26K9mO5Tzj9h1RU-8xAqPehFxKtGGBOvCvZshnS-_bMEUHAf4ctiQkBVpuh3Rle9m-24bc1raDIT1rxTwr8NYav3-pm37S1pS0jiJwdC0XUiA8vnFwh1VYbTUIlH34ZSdOMSJkK2rIWGAwSjG57A2oqs4Ysb9rCRsS_U9WGsy08bBEipffB_hUJuzJvmjWzD_AyJSNCHKvctBrg4-QI9OwcGZyPS-QaYNL6iTP5UOJWgSyIZxA_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWQZqgcplirj2Kagt7T8xivsRERBElDug6CQ1rkowTUcRESYYmDvnBDNutZn1Qt09P9_GUWzIwLEymDwDE33_DnHnwWtWmh72zCvFYbbrNPEULX0fOf-s6PNTBKIQ9hkdpGkV7pVRNln6Px73p453vw7Z-aGJ1mTkMkHKIj9H-cuoqL8fli6CU_ZLcYoUy0V-hVhYwR4aKG7NVI5itWTIy-RsEQdPeZayo8vYM5DI1tNxxKe0JdpoONvbZLypej-epEh8wmchKRD72ggOaNa4JujFn-gwpc89Oqgx0Y0os8r-dtTaAONWm6DTn7XkPQDwtZvyK35OQVQZqtUlaN1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_9SM7uRRyLGF6Z_-vV4hDIsvlufOuzxpDy7ZT026n59ixc0JSctpipzmFaM_G3d3S40A_tZqveUT3gq4zqEVEbSeJoQ1OAhccI9TYY74ex8V7bOB6M28F10Oh3fQk8nFg0yePKDN6yFxyCFEfh3gKUSrLjOLZnHt2D6ca6jAAuPFuXOnl5Vgybqhdiyhb0UtCXSZ4dHmu3HuVo6_TFrTUeCVIQMr2qPPgFl7i3XKpMQ9uJCBKShwh7P_MRD1K5TA3IQvlqzAHM1TJuJFepbm3qniie5xXP0K9T1GiGGeDZ4pbxmCnD5yIz3EQ1zca_kw_1qSsbCK8Dqo4lnMw1NzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq8Wtel8FRmnrVxWvjMfrs1KMSL44hTTc0e1WkjSSKLaATKMKiaCGec7okNPDoBVO3NLMEtS7uakFDFYvkL5RrRiOv13Q2Sq-sxd0WuLrOW3xjoSKu0ZOVqOYww4NlGOfL8e1ncZt5kijuttj6DABIJKL-_ocbkTM8dv6KTnXhEO1SKPc0JqfdNUsArm2piJ9NYf6z5LxlhqNVyQOV2FN5LbjcR7NeEuxJHdZVZQ54Cot5MC6PAnv_FMJtIgrG4xJLS_qBjeV7ite9zu3XLh9RJCQTLZ9ee8PoHSYd7a--30u3n2diZ9Nur6RvdE4S-tylxfi92uuCbGQ-jHsQFqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=L7z1Md4YAJbzQHBXa78kVBeG67v5SKSVVpZoObCeepGE0ukO99LF2sE9w6GDTN33yl3bT-waSQ7Ntmq8Nswt7MGOdVy5y2U6qaSVa6_mQVPejLDBluft-pj3TBpnwRTsaWUwVcuP4f_9yxwFuhesl0Ph-yB3gFZq0W0sAYDmQjvzA8qdGxhkUWYP6mqp-CVVfvEl_OLqwKXdqK6NBvhT5adzskOFDyrV2LoZfDG0m06t1ibUhi_byjRKMtbF2k-awxa_BYuIqM084xzcXQVkI6n0p8b_V4L6AkZc7KhsR6Lahxrz3rv-lON4wVkKk9vwfOzRAc-tRFtZ4rlss6_R9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=L7z1Md4YAJbzQHBXa78kVBeG67v5SKSVVpZoObCeepGE0ukO99LF2sE9w6GDTN33yl3bT-waSQ7Ntmq8Nswt7MGOdVy5y2U6qaSVa6_mQVPejLDBluft-pj3TBpnwRTsaWUwVcuP4f_9yxwFuhesl0Ph-yB3gFZq0W0sAYDmQjvzA8qdGxhkUWYP6mqp-CVVfvEl_OLqwKXdqK6NBvhT5adzskOFDyrV2LoZfDG0m06t1ibUhi_byjRKMtbF2k-awxa_BYuIqM084xzcXQVkI6n0p8b_V4L6AkZc7KhsR6Lahxrz3rv-lON4wVkKk9vwfOzRAc-tRFtZ4rlss6_R9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=JvXiZ3oZG4MGRaapM5VdqCy329p_oKS20p3xfABWp1kp2Y-qWMpwjBxYTGMQDVQX0yZHV3Uii3_pmsQldH8dCST-2A-yrbEBNYqbPN5VHH0DrxqBdkoURc-wB907uGJWFtRVctx8AyD8rCWr_Sb4DBIqD2RtD_yxNzAfBJ9pbyeG3xp8SDEApIbAwfJJcDuuO6push-MH3uwvHtc127jMeDC-WfYUjHRprElkFgjl4JQueHtfwGBQNGQqYvIvzyczSAVYfw3aQZYtSoE-FzYW-StRDXRwAF5sw0MVPKB_ysY2sIqa55cugImOarhBsQHJjmCDi4_b977GYkiqQiPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=JvXiZ3oZG4MGRaapM5VdqCy329p_oKS20p3xfABWp1kp2Y-qWMpwjBxYTGMQDVQX0yZHV3Uii3_pmsQldH8dCST-2A-yrbEBNYqbPN5VHH0DrxqBdkoURc-wB907uGJWFtRVctx8AyD8rCWr_Sb4DBIqD2RtD_yxNzAfBJ9pbyeG3xp8SDEApIbAwfJJcDuuO6push-MH3uwvHtc127jMeDC-WfYUjHRprElkFgjl4JQueHtfwGBQNGQqYvIvzyczSAVYfw3aQZYtSoE-FzYW-StRDXRwAF5sw0MVPKB_ysY2sIqa55cugImOarhBsQHJjmCDi4_b977GYkiqQiPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=k3FzTES5wIhInpXeb8fA5kZ94kED4rqU7ovOgwRg_3XpCpv9i0XJrsib2FYkZ7LjzQ2gs4S6F9mtgzON2sqNJhNGN4E1fgBLyXI2_5HyXmYqVtunXHxZ2HiWHjQ9j66FhkNef2RNlvJnSL9ZRaav4yl2DSz3qnL2GXlJWqSXxIcbySf3zPjnNc9n0SMu379vsnKk8yCKdnSqJp-UjUMbXFDfeihjwN6XVH6nLiY-9KubT6oatw2jE8RfRY7SAAkimIDJX55ubL9KZfMeKcNXeZg2Fq3vmbEmIBFz-QIrRf41NZxgmBq2bxhKurerd-mqdJ89yRw2sTQBYKob33z96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=k3FzTES5wIhInpXeb8fA5kZ94kED4rqU7ovOgwRg_3XpCpv9i0XJrsib2FYkZ7LjzQ2gs4S6F9mtgzON2sqNJhNGN4E1fgBLyXI2_5HyXmYqVtunXHxZ2HiWHjQ9j66FhkNef2RNlvJnSL9ZRaav4yl2DSz3qnL2GXlJWqSXxIcbySf3zPjnNc9n0SMu379vsnKk8yCKdnSqJp-UjUMbXFDfeihjwN6XVH6nLiY-9KubT6oatw2jE8RfRY7SAAkimIDJX55ubL9KZfMeKcNXeZg2Fq3vmbEmIBFz-QIrRf41NZxgmBq2bxhKurerd-mqdJ89yRw2sTQBYKob33z96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=Nwf_Yqz1F0wCX_2BPOQg8Uyozc5SODYgEJC6sAkJow4oJ8dFuoWJd3qVW5UJB0o7R5Vvu04KF2wmTiW0Mk-Il5U5pR9WUZQPlAmMC6IqB2y9q8ut0q4bhYCOaxu-zaWlfiP84zCnbDlg_D3M3oQU3QNP6PJrm1fTlHrTncUJTcL0HBxU73i3OPEpKtsGfaBGKyGV77265x13LKmwP5kazEC88G46kR6a3cZZMXoZwNcwavYN4IpQZT-NpH2_0fINXe92R9PqGZV3l__UUUnWPVSIH2HLlORWYEbgypn6ILZc0aYMTioazZj1y336wP_PtYgylQeLp9MvPZxAnUvRzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=Nwf_Yqz1F0wCX_2BPOQg8Uyozc5SODYgEJC6sAkJow4oJ8dFuoWJd3qVW5UJB0o7R5Vvu04KF2wmTiW0Mk-Il5U5pR9WUZQPlAmMC6IqB2y9q8ut0q4bhYCOaxu-zaWlfiP84zCnbDlg_D3M3oQU3QNP6PJrm1fTlHrTncUJTcL0HBxU73i3OPEpKtsGfaBGKyGV77265x13LKmwP5kazEC88G46kR6a3cZZMXoZwNcwavYN4IpQZT-NpH2_0fINXe92R9PqGZV3l__UUUnWPVSIH2HLlORWYEbgypn6ILZc0aYMTioazZj1y336wP_PtYgylQeLp9MvPZxAnUvRzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hacwLDzZVdyKp2ZRx-4eE0hLb1pYICDHMYf4NEDN_Ay4C90G770j5y76gl0uBGSuRrXNdzl0d6jXr22kzzKLfuvyECNAn45bsilbv355TPXPQTwKDDHG6B4KW6WVl5edEI4d4kRRuiZpIzdL1G5yEAbaoAm10j8J2tN23nu_RQfJ6H8lJKAwQ2YCbTDhgiVObgCrPohxQGDd-KCobZOB_Z8mFjqjr-3tWJZcvoumQiR_NzOs3D4Gphbq2e2GT-9ewgXtQpWxd7BwFJJU9gQJEAGDlGSc2P-UgLv1eVN6BA3DTdB_zFXXn66RYJufTv8wMWANCT7HHOm_hXY8nT_Acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5CloHa8p3BGxXWZySFZszYkIFbxDG4pPVioLMgtOAaO-31MxOwgZcQ9a8e9NZogzkQslkYpyFHYShK7tVBv16h4TDL0B5z8nB8nQqM4QT4IUmIkUbI4Vx6g_61WpXHIus5uQGEZf7CR5j11oXm-Di7kwJxHLAsBbskERsSvg97euLVQHZpLLkYM5tVfwsmCjO2uKEshUqznYaew2fNb4LTXjDiUF2DAfTTQvOmmr-iJXKbdljEs_KTJM_HWVaQiSAy6CSGh1b13Il_c0sNqkgIFw2OjsKamKz9lDa4xnmhrLouWNdib_HVS7H01n9PU6pKEJsuPB8wAPOnNWQ2KtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=TU3iLU5D9KyX69J2e1-yC7HeOwA11RqrcqsjyFbD-BrmI5ZkPWoWliZ9JyZHphcZrw9B8mS_482E8VyGo5sxKsCRMSNFy9n5qEqIy3E0VYUhHUuZsIBvV7A6HV13YqgeFYaNhHqPt1FqOBCbdwYUKHh2K3HDclu2RKtcxmMMa7oZkpPGwJ8T3aHx9f9HHBPFNYbQkzvW9qIr8UzDo0ox0MX55Wk72n0VSnc37ooBUTUo0poaAgAgHg98cvpN1vv82LGal65ZfhWMApct1LmtDuztKKZIgtyL5UpK-UzrmeanFrNbcwG-qvDRYBT2uKE4dTjjYNf66cbid5FX660aXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=TU3iLU5D9KyX69J2e1-yC7HeOwA11RqrcqsjyFbD-BrmI5ZkPWoWliZ9JyZHphcZrw9B8mS_482E8VyGo5sxKsCRMSNFy9n5qEqIy3E0VYUhHUuZsIBvV7A6HV13YqgeFYaNhHqPt1FqOBCbdwYUKHh2K3HDclu2RKtcxmMMa7oZkpPGwJ8T3aHx9f9HHBPFNYbQkzvW9qIr8UzDo0ox0MX55Wk72n0VSnc37ooBUTUo0poaAgAgHg98cvpN1vv82LGal65ZfhWMApct1LmtDuztKKZIgtyL5UpK-UzrmeanFrNbcwG-qvDRYBT2uKE4dTjjYNf66cbid5FX660aXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvRG7NERfhDydga9KMqsIDrOq1TNVQm6ZFHala64vBVNLA5fTy18-OLu-cQA2-O3FsiywGFYB_eOXb_M1VBCzYC3bHdRNYDcS4dr2thR_qbQH6eE1qJ7Msqne-4qErHuwBC1dypnPthajdhfg9cob8B2Y-Q0LZaUyZ4xSzDQjhOjyki2OWMBZ_ij-XHkhUNws7ZsGmpddj7-oJimccvrwcjhc6JQbF6JAZnoBIZGe1DKs5eCWanUQWnzC2yv9w4vn4Bj3jg1rQYG7cj-nGC0yFmXlx7xfkEdiFTHg_qVWqenyh4JNSfPmTkMPqlutw3ee6I-gJVwKhubMW35HLY0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=WDxUlOXeyXpDBMDq9S1tzNQPh5SKoW6q2B2Z8xJkoNFc1nh1zzDcTK-ZZWfehUKfTCsozCnf0Fv9j8aJbo3b6PhYB1zxcwlIrcTWvworH4OGyoaq6r4LAQ1pSW2ns3qpFBGAzEWAR48FDOD_0thEshQ4goFSgCbferVaTYdu0U7NfFVrMnRHbZ54dFyQoT9Hf0qvxzWsIfz8e6LmolRd010kHF28IZijcNkiKJ74hOosaz5tHVhlle6iFYtRL-f3eAcugDKXAQFmYU-0ZR7OMFBvbTmYa0bqpvz6WT7Lb6NtHx56cek7Pqp9pIlNE313OrLV5rM36w0QhlRZIK6JTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=WDxUlOXeyXpDBMDq9S1tzNQPh5SKoW6q2B2Z8xJkoNFc1nh1zzDcTK-ZZWfehUKfTCsozCnf0Fv9j8aJbo3b6PhYB1zxcwlIrcTWvworH4OGyoaq6r4LAQ1pSW2ns3qpFBGAzEWAR48FDOD_0thEshQ4goFSgCbferVaTYdu0U7NfFVrMnRHbZ54dFyQoT9Hf0qvxzWsIfz8e6LmolRd010kHF28IZijcNkiKJ74hOosaz5tHVhlle6iFYtRL-f3eAcugDKXAQFmYU-0ZR7OMFBvbTmYa0bqpvz6WT7Lb6NtHx56cek7Pqp9pIlNE313OrLV5rM36w0QhlRZIK6JTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6Bd214OtYE0ov1gQ1SKkpUVWA3e2HTHMz_pfB9Bp5OLorg_9pLc3xPO4W4K9iFPvm3W0DBphtqEjxuHi_aU7F1-ex1CePUX0LiuzMX-JnAn_cX517pBQ7uF5unb8m4HAtmWmMms-7K5wtr12GC8q08x7LX8JRwTt6kr5g6eRoxKSz_oILyFdSoj89scJwpFl1cypagskgaTuIVgtbO40a119G2IDgRbZj3XabQuRYf3tr7pRDEw5CPR0dIXDJ1-1PYkmauByJ7ocBuanFHYWEE8pGi-D0pF0VQn7GMvqdDImdxCloT6_f8dG1frW9Q32nghoqR5hoVRBGUjydz56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqn5ZnyiEf--nAXSNuL8asy-7uTJ2P-HhBaQpHZ07d_Ztrn_4TekpkIwKzUkW8VfKMBttkNTbVcV5Eh_IhHtHOVfyfbEFa2ir1FMVIzC0gPbOd45tTGcYjgmh2I5IsJftaZqWo11ddGPutaA7Y85QNY5HzfHnBGYje8wMiiKPs6YhlkmXr4ifw39qW2DJfaG30q9subK8vXhLWUThjU3Q0lVD_rHiIIERROSQ0JnNBWJcl9iTHjYPntyr-DdQEzghLSKaowLeCnuARsm3KAC6RPztzwrrHa7Xcmggyn82zI0o1UQwB9wuJTWse8rbS6RA2I3oLqq9I7EtbrLocI0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=hMFrPLnvMtIbj8-C2OEJZVfKC_Y4tyhax-vAmOftS6r1L5xB-fn9lsT9b5u-FnE4gmUwj-17Vl1aOHdPi_0JqwIcy0NDQyVCl0Nk-yCVC-T1RwbdJK15kmuWTNuBfC9TBFYblqkEAXwGPgbpEa4Y4ZuwkwHGShL6UY5eb7ws-VdM9JtBmvX8FmgQ0O72igKvcwrqIy4wXlkXKSDa48t-n4N_AssjR_68Lpz3asw2hbj0NTueA5LO0fcPmVx2xX2h6aKU0ObxXqPWK8LL-UhHJmjvisV5I_hPMM138ekLIVZkiAWlLgD8OrYd_DAAXKVRKO1bKo4h6CDBU4DgW-QBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=hMFrPLnvMtIbj8-C2OEJZVfKC_Y4tyhax-vAmOftS6r1L5xB-fn9lsT9b5u-FnE4gmUwj-17Vl1aOHdPi_0JqwIcy0NDQyVCl0Nk-yCVC-T1RwbdJK15kmuWTNuBfC9TBFYblqkEAXwGPgbpEa4Y4ZuwkwHGShL6UY5eb7ws-VdM9JtBmvX8FmgQ0O72igKvcwrqIy4wXlkXKSDa48t-n4N_AssjR_68Lpz3asw2hbj0NTueA5LO0fcPmVx2xX2h6aKU0ObxXqPWK8LL-UhHJmjvisV5I_hPMM138ekLIVZkiAWlLgD8OrYd_DAAXKVRKO1bKo4h6CDBU4DgW-QBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=bcF-S6M8iIl7RjrVcidWmuG8A8k42t-kP9tvH0FYTkEhv7Cy1_LqeTcGfbjACodvNA4nGjFkKiPyS4xC2JvCvTwqWAo1_h-1AY_f-zyWj-7iBz9vZdBjKIEKWyiWlAGD5ZZQSlGdnjZfg1JjCFnYp4GDZsOwYEzGDmS1d5UKILXRHeem0tBElxN6Ukc9kPRWvhtTTqqX9XFlVY2hDC7DFkRDG64DIuTYlfiTGc6Yb466uwrvbfJ5BngO_tQVSl25ucGhjt55isihwKFiRu07Fb3UJ5B7gTh9DpQg8yYyzmXv5mMGqVJ25hMcz8kvpY7yR4CK4-fSscomwATl5JifGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=bcF-S6M8iIl7RjrVcidWmuG8A8k42t-kP9tvH0FYTkEhv7Cy1_LqeTcGfbjACodvNA4nGjFkKiPyS4xC2JvCvTwqWAo1_h-1AY_f-zyWj-7iBz9vZdBjKIEKWyiWlAGD5ZZQSlGdnjZfg1JjCFnYp4GDZsOwYEzGDmS1d5UKILXRHeem0tBElxN6Ukc9kPRWvhtTTqqX9XFlVY2hDC7DFkRDG64DIuTYlfiTGc6Yb466uwrvbfJ5BngO_tQVSl25ucGhjt55isihwKFiRu07Fb3UJ5B7gTh9DpQg8yYyzmXv5mMGqVJ25hMcz8kvpY7yR4CK4-fSscomwATl5JifGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OInpr2tfRAhYGJlhJXoNn_X6P5P2SGJ6OHo-ZLKOYu7Lm2Qa9wjXg0akeRKWOBtrTdJEqojz-RtTH2PSSJauyLj2uGevsrPngSC84Nmrn1Fxh7bjt0b6wx16e6ok69FWAiFEVsNnZo9muocm-tBmuDIqMN34Ra9Xyto7k8OKjONV5W00w6_apHR8wtnItXrkNSKGUKXV7wpvUNATGyBII-xnxI4Lp005Y0wbSoQEfBv9r-egDQheX7kgLb-PsFvKn9XhafkmGuJ9Ni_X2pdGgc1zeW-g83mt2fhz2P7H8gIIndezXM-2_JPbo62Ecd9h7uS57Nb3DlkVVCtv3EVGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BARc76MywKkwTGYMnNcajVfF6Gl2_u6TxPvTMw1mf-ExeKSBsTpelZjSkYTUCGjlg0T-o1ucRbUYW3VSEYb0pisCWXcARB_x89tVmqEPbMnoWMhd6sJ5EJgEsJBz1TfPGHJNBoV6_ePtSuAXRhTDNnyyGBB93bZQTgqnloWfzogAKl9flPlWmta20QvANkqqCHNRPYV7JjW12wwb3ZEPXsLI3GHsFG0Ko0w-4zTPhxFSXkNmt62ido4vHBoAWPwXP1byP2PXMuKzIauVNYxoWUx4HvRaYMWCGJuJMYeVxpm3E31jhVRR89Hil9MQQsZNQo513N_EmhWNk3aWS5lxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrh5Ie1l6dhg4_UH872z4zsbwc6X9-j7YSw5kglt4ImIWDk4q2Y1Xt2fKXowmLf8WGH_qQldxqbRovgEACgIZxr7cgBrsmtkpyfDwhur12W0Rzlg1ZtLvgRrDAfk8KlALk1FonBfG4Q3fpMZGMLIwPOgEN_ux61DWm7s8CBUfFZUYhXnab27NL40rGcFVcJbqYSNZsfjS1izUW9ULpnAVH85fMftRuAlslMy31ZThmsD6wLrNI5sr7ljdRk-q9xpPyZ2Nt3RPUvbLfYdab7wydexUXi6C9ZxyzzTEU1uG-fJ01ANlxQjv1nk_xDmjLSJCVaxs1sCvlhmkc2qfqf6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=E8b30ta9fg5DYvmdpLmvKAEFMsVfe9Lq65AANcGP0DA15PBfRKugnBC_MvuevAaPIr_oL_ajCaqeGGWb6sVSM-N4tAAS7EeCcowRzlil_MT8AklMlITEYPGltPVbCmyaax8pKr8bmh852BWX45q954W2Ivk2Rc8khQuy5dEzHK4kBFeJsJqn4U2DZWRXVzHRQWl-4k6YCGYKn5Eh7et-FiRAI3t0COX85PsgHyKtY8N3AmWDcool_UXHAMOoGghxuYuQ0efUbWM-4H-q-GGapEZ4Mpw7wDufeVcApaP0YzWtJPNk6I-iGt2T69Foa58phsTWrx17alJUx2id35GBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=E8b30ta9fg5DYvmdpLmvKAEFMsVfe9Lq65AANcGP0DA15PBfRKugnBC_MvuevAaPIr_oL_ajCaqeGGWb6sVSM-N4tAAS7EeCcowRzlil_MT8AklMlITEYPGltPVbCmyaax8pKr8bmh852BWX45q954W2Ivk2Rc8khQuy5dEzHK4kBFeJsJqn4U2DZWRXVzHRQWl-4k6YCGYKn5Eh7et-FiRAI3t0COX85PsgHyKtY8N3AmWDcool_UXHAMOoGghxuYuQ0efUbWM-4H-q-GGapEZ4Mpw7wDufeVcApaP0YzWtJPNk6I-iGt2T69Foa58phsTWrx17alJUx2id35GBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5GMwdnSI2eYQ291qlJm-utAX9Uvgu_HeLQN5EFe1o1ZJzNErmz4_uvv7vR8YV9Be5ZmQBxK_MYn0Ns1_aEzMBy8oyEfnk-nyyznY1JVsZZAHd23ncptFS3T4BPV3w1aJUTYVhGe6Sy0j20-OMu3j1qhx3JVitf2gtNEnU5CtKIsqhgncvlQt4FMbSUi5pUZxlI9uFmNgRIX2i31mxGLUwWXd0bdN1ggYp8XmupuDamNcj5FK6Ns915N071CKHBJS2E6nC9GpkQ_uyqqCSZHEslhwjAoR2DgJUc9ApkjnPPk0MiX8hRR17AuoEicgQ8DOKJBXDyUIK5JLS0WTFbbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
