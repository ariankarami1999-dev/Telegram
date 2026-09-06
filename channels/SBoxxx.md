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
<img src="https://cdn4.telesco.pe/file/db90F712AeJFnLnDt7gj4x6UmXMQz3gRumlwCruerUqlCD9Vo6T8aefjLWYGzaAqX3LfaoLAxqsX0r2Lzei26p7rWzje6M_sel4MriJUYyrsMT2OKdTSCoSF9hhrqb2h6c2B0B4Mmy9pzPf6UAWUhUPVFdMlUtaIeL1lfVpKqfRm8viffPCMk0gZ3-wa9s0UO91TzSZhRGsIu3fWJDmia0600pl36vxbr8d3HY3T0bzYr3gxOc0PVKoBd8-or1tTEkMPndKx5Tvze58jfbD8yNfzRDsew_NbSP7FtyRixE4G-JtAvKah_zU-Zq8WYrVNq59o2TYKGXcM-ABIf0AAvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 00:07:11</div>
<hr>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIhjeQQTk5_lWggEA94_h59HCAHS9ckn5pIqskvsnhO5aohZPk_B3_yGapFbZ9BJNpmxCERMLoU4PrjeRVeht_y01oM1s7opjvvXJZ6m23kN8JX4dOKGvp2FWh8y03tQ03CPKUeCI7bM7b25LwTsYS3nQnIRp7Vo2AljtapKG3Pztlp0tmxemxyvFbybpd28igILDzUrDZoN3sKZ_2vjTMtSj5t5hhkOm79a2sexT3IAbFuORtfnMmwLTM7tT5nX6SN5zHWf_M8aGCBPXCefPA21oBtudPqLgPUuf209U7tdA_AdfXMqrVKdvobGCZZBQZNB2K8SWq_v5WyC_Y0g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/20610" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سرلشکر رضایی:
برای داشتن وحدت باید به رهبری نگاه کرد</div>
<div class="tg-footer">👁️ 526 · <a href="https://t.me/SBoxxx/20608" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDwxTf-DrfFrb3nnp-2AmyED1O2z1b_oxj-b900p_bm6AsPK_kPtfygNNidiVomosCDV12Gh0Y6imt1lXfQTiP_akVd_MorlEfQtmgfrtiNxfpqim9pghirZtipHehJ-D7W-9oAtbCW4rNNuxojFBVPaREAlaVr_kVT1OH-_z04XV_746eJwnoVIuU97_2t0Kfq-BFHvwt-Z25y5fQZwhkGMoPYxm1AVzZq350v0vC13LXp6Xf7r9W_IlSuq8tV09Vq135dPH-HNe21MkvUOQ941U3s2SIlXPXVSu2L-1zerXRLaSe5jngraFNe1PVudCtWaXnYCFMbwaS_Jhbzzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/20607" target="_blank">📅 23:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTFRqtJqr7HGSDE_gWrwHsLaYY5AcH2OG418MZKx8xpPvi_6TJd4_BuHRo4deJ8dRAoYOLZPTHnlQWlskneo_mnDiWiEeTUhwVWJi8nC6jRMv1qLhf2wfFZROx1vGF0qX1ijVZ-Knqg6ugjsCKZEasQq77Ro3neA_jQzqWZWclwJahlSPoHoIAhdDxMs9EeSbR2a4ravVxB-TJjGLpPW6RmF2nQ2vzmMb5AZTpa5ok9GqHMx9l9mnQUmhVzeT6JeY_b15parafngr6o_ysZDu3eHPgx-xzRIrPRduNgbVNDQMafHZGXvHlznzl6elS5gi0zbnf49bJM-ngaId5YCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه ما خیلی سلاح های دیگرمان را تست نکرده ایم   مثلا شاید طبق مورد ۷ بخواهیم کوههای البرز را ببریم تنگه هرمز تا این‌‌ تنگه برای همیشه بسته بشود و اسمش هم بگذاریم تنگه ترمز!</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/20606" target="_blank">📅 23:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سردار رضایی:   ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/20605" target="_blank">📅 23:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سردار رضایی:
ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/20604" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH92k0wLuKtujwtZZWabGhRiiLtAO54fzR6O3lTLkhWxgBXq_DXa5AmHQ2Yx6FuskNp58k1Q_6HyrBnwRDygxUJ33O20KSiJwWGQwnUkPgNBrn98eWTD1VjSMf_DJ4HhnD-I41SN_0aKYgpfkh2D1ToQc7DQ5_yAvVYypvpYQdB3f0O5BKcjQ5XGnLOlAjJ3HctPntr11rF08b8Ug6THLpClaMD1sGxmkKmAxB9RR2fhrJhgB-ZYZ5d9fH5oS95S8qOc9YRSFJY8nQHYy5zaK-Mplnyde_yPym7ERR4Y_cYY0qR2yKH7097tUMhuCBiGvloY_zc7w7GRELb9U-x3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/20603" target="_blank">📅 22:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G009UnlJ6--dlFs62G08PWYSAFlkQiywpBjdaF_tGkjlFGRU_IKZkIzSYekzbHbBBMVyis9D4uuUroDDxet2UBkP8pdZ6qGXtrKa7iIVk5vxc7fcgK_wYKKpRASupRmeT8hsnOJnmrLpxzt4r5p8U8PZOZXal6IoUGWPiHd7yTRTf-RV5teziCeSrSjQEk5SIul4Jxucoaspf6NtFPrzJ4HGSEIOoA2n2cBjxU1blLaLeP7vQSwKsRNtf_KRylVX0n7CvYdYnnmnzabz6agHuKFS6-sgHyRABDKo8tMF7AgmV34bfzhlURhGKk8uV0bNLLswvWE7Dg1ExuZBiE372Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!
به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/20602" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/20601" target="_blank">📅 22:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=KLMNyYQeEnnI4Ik5gNKiJN5YCrmr373JT9kXgs_gPXv1L8DHWbZHFiZev2KIUvh3UBiCuzE2atlcWiRr1sqEHomDpaS0W_zCB6itEwZMO4d1zBQjmUegbWBi7g7qHlRTZ4-pfjFRIl168KgLJX0LWdXzSyshrenzYiIOcKqU9uQVHZEnhLUMi4-rRi_VM-73RVs3d7x5mYeUwOqtRg9UtpDb7GEFFOH9bhR3hhPSWfCONmVcZlfqVL1nGlzZGXkbGyL4fIZew_ed7wIAEs78IptZJSFRhF4AktzGxaTHylZaEzknlZATqCUwiQvLwSCEsKylMKc9EafKD-OhBUZTZ52NCDFwpbMbcVNkLrO98cnQgub7rqTzcmrtpCChMj6W5hk65a-sRRo0oPXeB1dI7LwMRB8X6_1cieQelGrWot39kIPWHU8LN4I0BkWUB9xB7TGrEyHOeej9tlbQTIZjKZ9PBLVMDkSPjR8BuQE9bJG1osUijw7kfa4CMwzRCuirdL-9emyICWUC7xsrrTnJTz2WOiox4r9WxXDeuj19me-aFtEA80K9p71TACQcrlXwKtTtWjvV63hkSHnt-j_HTFwxX0-UuEWqwTgnNerKhydiaSuH2drPBll9eiN9tOR60l5dyOfPDWWuoUbDR0MvvqMiD0DTeZDHS47Vvoa568c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=KLMNyYQeEnnI4Ik5gNKiJN5YCrmr373JT9kXgs_gPXv1L8DHWbZHFiZev2KIUvh3UBiCuzE2atlcWiRr1sqEHomDpaS0W_zCB6itEwZMO4d1zBQjmUegbWBi7g7qHlRTZ4-pfjFRIl168KgLJX0LWdXzSyshrenzYiIOcKqU9uQVHZEnhLUMi4-rRi_VM-73RVs3d7x5mYeUwOqtRg9UtpDb7GEFFOH9bhR3hhPSWfCONmVcZlfqVL1nGlzZGXkbGyL4fIZew_ed7wIAEs78IptZJSFRhF4AktzGxaTHylZaEzknlZATqCUwiQvLwSCEsKylMKc9EafKD-OhBUZTZ52NCDFwpbMbcVNkLrO98cnQgub7rqTzcmrtpCChMj6W5hk65a-sRRo0oPXeB1dI7LwMRB8X6_1cieQelGrWot39kIPWHU8LN4I0BkWUB9xB7TGrEyHOeej9tlbQTIZjKZ9PBLVMDkSPjR8BuQE9bJG1osUijw7kfa4CMwzRCuirdL-9emyICWUC7xsrrTnJTz2WOiox4r9WxXDeuj19me-aFtEA80K9p71TACQcrlXwKtTtWjvV63hkSHnt-j_HTFwxX0-UuEWqwTgnNerKhydiaSuH2drPBll9eiN9tOR60l5dyOfPDWWuoUbDR0MvvqMiD0DTeZDHS47Vvoa568c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/20600" target="_blank">📅 22:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محسن رضایی:  ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/20599" target="_blank">📅 22:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محسن رضایی:
ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/20598" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: ایران از خط قرمز ما عبور کرد.
در یک حمله غافلگیرانه، آنها پنج موشک با سرعت ۸۵۰۰ مایل در ساعت به سمت نیروهای آمریکایی شلیک کردند که هیچ اصابتی نداشت و هر پنج موشک سرنگون شدند.
اوضاع درست می‌شود!
در همین حال، ما واقعاً به آنها ضربه خواهیم زد؛
اکنون نوبت ماست که حمله کنیم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20597" target="_blank">📅 21:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS1vKMLGBjimYvoQ5oc-8Vq-Pw8D33ejtwhPjOHuM2Yp6QYPReUo8aK6Bkibae8yhNwhAB4jQPvgzTlasG4Ex721QYbhmIByS96aMzm4EHvRog34mJEAnvZTZeKS6TlO4DPj7N8rc-p1iHHzNBFm14ZlW53qqsnJbdb_yiLViXNm-inv2Ow3KZsTKEZ2DZfEtDuHRDkPEXmeyWZ3rDNCQaOvtVrCrtdwIYpEmilGP8FGzgotYORbnXtCYbEJTKujp-syyS8n9kaGE0rTRxaN7CTbIGEWyS7r95YDnoLd_ViaP2qeSSFg7wk9xqCbHZuVtbsbgHY7MbwcPTncNmMZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20596" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20595" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام:
نیروهای ما تا دیروز ۹۲ شناور تجاری تغییر مسیر داده، ۳ شناور از کار انداخته و ۲ شناور نیز توسط نیروهای آمریکایی مورد بازرسی و توقیف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20594" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gknar_ZYBd35adkKhv4M9BNPyBQbDTA7CrrpJqpLcRT1f-07lrN57Bx7uDPyhdFInqiLsT2zGB51fpdu9bi1fYUANXwVGHvbdXB4EIxsbGoRwpwFY44UL4OGISEArTxG8hiZ2ljiGU5IFH7blOplALWJ58WBQ5cpHIAT6x1QUZzV3dfnRiWXiPfg1KnlBP5JVc7evgbLtypz_pqgwSSYfXeFPGnal-tfKxMgfSm3bv5Fe24w9d2vdR-x09gUc0SZNkdQLyaRg31Cdqa6PJcBi78j5p90jfnAfhc0DDhhZ65h0g13hqJjusO8gFcQWw6H319O6ukyb3fS8O4cNPfd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار سوخت گازوییل در آمریکا وارد تنش‌آورین دوره سال شده است. موجودی جهانی گازوییل در یک سال گذشته ۲۸.۵ میلیون بشکه کاهش یافته و به ۵۴۲ میلیون بشکه رسیده است. در ایالات متحده، موجودی‌ها از میانگین ۵ ‌ساله نیز پایین‌تر آمده است.
دلیل اصلی، کاهش عرضه از روسیه و خاورمیانه است. ممنوعیت صادرات روسیه تا ۳۰ سپتامبر تمدید شده است.
وضعیت در خاورمیانه به دلیل اختلالات در تنگه هرمز پیچیده‌تر شده است. محدودیت‌ها بر ۳ تا ۴ میلیون بشکه فرآورده‌های نفتی در روز تأثیر گذاشته است. در نتیجه، نرخ بهره‌برداری پالایشگاه‌های ایالات متحده به ۹۸ درصد رسیده است که بالاترین سطح در ۸ سال گذشته است.
بازار از قبل با کمبود مواجه است: بر اساس تخمین‌های CERA، کسری ۲ تا ۳ میلیون بشکه فرآورده‌های نفتی در روز وجود دارد. در ۱ سپتامبر، گازوییل در نیویورک تقریباً ۲۰۰ دلار در هر بشکه، یا حدود ۱۴۸۰ دلار در هر تن قیمت داشت.
اکنون، خود ایالات متحده در معرض خطر مواجهه با کمبود سوخت قرار دارد. تا ۲۸ اوت، موجودی ULSD (گازوییل با گوگرد بسیار پایین) در ایالات متحده ۹۴.۱۸ میلیون بشکه، یا تقریباً ۱۲.۷ میلیون تن بود. در یک سال گذشته، این میزان ۱۲.۲ میلیون بشکه (۱.۶ میلیون تن) کاهش یافته و ۷.۴ میلیون بشکه کمتر از کمترین سطح پنج‌ساله قبلی (۱۰۱.۶۲ میلیون بشکه) است.
تا ماه اکتبر، موجودی‌ها ممکن است به ۱۰۰ میلیون بشکه، یا ۱۳.۵ میلیون تن برسد. این اتفاق در بستر اوج تقاضای فصلی رخ خواهد داد.
اکتبر و نوامبر احتمالاً ماه‌های دشوارتری خواهند بود، زمانی که تقاضا برای سوخت برداشت و نیادز به گرمایش همزمان افزایش می‌یابد و برخی پالایشگاه‌ها برای تعمیرات برنامه‌ریزی‌شده تعطیل می‌شوند.
در آمریکای جنوبی، موجودی گازوییل در پایین‌ترین سطح فصلی خود قرار دارد یعنی حدود ۲۱,۵۰۰ تا ۲۲,۸۰۰ هزار بشکه، یا ۲.۹ تا ۳.۱ میلیون تن.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20592" target="_blank">📅 13:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….
به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20591" target="_blank">📅 12:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20590">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خشم روسیه از تغییر الفبای قزاقستان به لاتین!
این دقیقاً در راستای تحقق رویای توران بزرگ ترکیه می باشد که من آن را به عنوان حوزه بعدی تنش میان غرب و روسیه (و احتمالاً چین با توجه به جدایی خواهی اویغورها) تخمین می زنم.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20590" target="_blank">📅 11:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20589">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:   سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20589" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20588">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F66SyRvkXGJsae6NfB0rGnmw2C4JJx-HBuikkYaLgquDfhoDt2GxrmxTGmk52j4s9YD08uG3pHpCnciFlWpRbKLf7FZgM4QiiQMJS9W5k4iqGEWx8GaFUGrRYJZc92exMWWmXw64YHcbVd5iMQpD6K5OXvOv14uJNSQzlywOJ8eKbmS622BuR96elN5arGtFu0mSMHLEyK6h1GkeuX9mViQr6_LnS3M6oOFx7cMEyMYqv2zwwWVu11c3RxZbgWb52L8yOq5OQsjfIFU9l61cGerm89gCgR4ZWgkIVwvlQIt1gRkuBL8Qdf5kW_u6lIBi0r44E7rDEtEr9VmnoqYJmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروش تسلیحات آمریکایی به متحدین نظامی اش از سرگرفته بشود واقعا؛ یعنی گزارشها درباره فرسایش ذخایر تسلیحاتی ارتش این کشور تا حد زیادی اغراق آمیز بوده است.  نتیجه بعدی هم این است که روابط ترامپ با روسیه و چین دارد تنش آلوده تر می شود</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20588" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20587" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20586" target="_blank">📅 20:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبرگزاری ریانووستی (RIA):
پوتین وضعیت پیش‌آمده در مذاکرات کرملین با ویتوف (Withoff) و کوشنر (Kushner) را دشوار خواند</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20585" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20584" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دو ایستگاه برق دیگر در آلمان هدف قرار گرفتند و مواد منفجره کشف شد</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20583" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادامه انفجارها در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20582" target="_blank">📅 19:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ گفت پس از آنکه بایدن ذخایر راهبردی نفتی آمریکا را خالی کرد و از پر کردن مجدد آن خودداری کرد با نفت ونزوئلا دوباره پر خواهد شد!  این توافق مهم شامل بیش از ۶۵ میلیارد بشکه نفت است. این امر آمریکا را در مسیر سریع بازسازی ذخایر خود قرار می‌دهد.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20581" target="_blank">📅 18:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نقشه جدید کشورهای جهان بر اساس ابعاد واقعی شان!  طبق این نقشه که ابعاد کشورها را مطابق با اندازه دقیق شان نشان می‌دهد، سایز کشورهای غیرغربی افزایش قابل ملاحظه ای داشته است.  رنگ آبی: نقشه کنونی رنگ صورتی: نقشه جدید</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20580" target="_blank">📅 18:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUi34EZy_-bkwjBeB4ZtgZlekkwcRmrXpuEEFcyp3sk1tFrtAjEYG14mqdlveWmStS-iLKeLBnVuQNZzJtzNDTqLR2b4ZV6kSRIuNfD7_ci9hxH-RkoyeOWowMeU7pGyiLKo_lAdOOYI6N5p1w8utSE_KjZur4s0ZKbYyRa-cSk2NTOREwZjBYae_d2BnSEycK717cXAR1IgX3d7Yp8FImqbj88eHNgHryUXXBUSM6rvFPH2P_OWOww-Pqtj2OGImNoFXU1KxLb9fmK_3-yJ0zm3Hb7cU0mj_o5MiHQi1iR8eW3DiACa5MB-pc5otom8bWlSeBS1jqp5OoOkOwsvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1vHqeegnxgbmfo2zTS7q_tNYJOlsb-C1eObz2ib_Jfoz5YkaxGbZB7vZPS9ozFeU5hfBFdOmiR5eWOc1uJBGs_VrzhherVOxI5YxPG_9zgda1S9xTUk6iPrTqKTo1xf3KHIR7s9XUxk2bEpIcJ3xap2-gh3SkQW3nghF4Yoke3dX6chCOnhTe8QxEjJwcp7q-U4ZiaRyHuZaL3GnXwyoHBfFJrAzKW9DJ_ilnQNtC1WSf50qfX-X33Fa5N3_BX2wvVcbz8P7gXnIk0nS97H5RM6eUE2CJTInME35ZUrqvlofk8H_XGmI8PCUtCF0bmD1sPLF9yZhuwP7_C_VgGGKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه دیروز حداقل 3-5 بالستیک ضدکشتی به سمت دریای عمان یا تنگه پرتاب کرد تا شناورهای آمریکایی را برای پر هزینه کردن محاصره برای آمریکا بزند که به نظر اصابتی رخ نداده است. شناورهای غیرنظامی بزرگ در فاصله کوتاه عموما حرکت ممتد در خط مستقیم و قابل پیش بینی دارند، مگر مسیر خاص باشد. اما شناور نظامی میتواند پرتاب موشک را متوجه شود و مانور خاص انجام دهد. شاید یکی از عللی که حوثیها در هدف قرار دادن شناروهای تجاری حتی در فواصل دور موفقیت نسبی داشته اند همین مورد است (اما حتی هدف قرار دادن چنین هدفی هم با بالستیک بسی پیچیده و مشکل است).
اما مانور شناور شناورهای نظامی کارایی مطلق در برابر هر موشکی ندارد. یک موشک پیشرفته میتواند بخشی از این مانورها را ناکارآمد کند. در هر صورت موفقیت یک موشک بالستیک ضد کشتی بسیار وابسته به اطلاعات دقیق از انواع سنسورها میدانی است. وگرنه شانس اصابت جدا از طراحی موشک کاهش خواهد یافت.
🚀
🚢
(
بحث آماری پیشین در رابطه با بالستیکهای ضد کشتی حوثیها
)
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20578" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنتکام:
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20577" target="_blank">📅 17:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js6e816m4r3EVpHjay1hqRMSZgJLeth7YMzd4hjBuxwwLnDWmyo9Ejgm3Z3kUIFGHi44Z1PMLLw1HwP-Q4yUwLVrtV8yEsmwZu5TGf5zPE2Khlvh8oGQjlRoDZyS73Q5UFqzYpR1ZBrZ1XtXRPC-TZuCz61MEvfj-hRLNa2HVVSxXBa-LEaJD8PoMOqj88gv3TwKD5vQiQw9H3Tbzp2aWgfxRqyMlP56Pu201ksMcUigkVfT0ajTlSjOvJgzThk7gf6qmmy7ba09n2KPYy_sRjOODTQpIE3Gq--0Auhe8udfUMogBIfcMIIGxvgG8twr6Wg52KCY_VoTURFrglyffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان  بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20576" target="_blank">📅 17:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انتخابات اسرائیل</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20575" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تمایل شدید نفتالی بنت به سرنگون کردن حکومت ایران را باید دقیقاً در راستای صحبت آخرش — از دست دادن آمریکا و حمایت جهانی — ارزیابی کرد.   یعنی اسرائیلی ها چون فهمیده اند حمایت جهانی را از دست داده اند میخواهند خاورمیانه را بازمهندسی کنند تا دیگر تهدیدی برایشان…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20575" target="_blank">📅 14:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20573" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqKV3yE2pIiay5YXf2EXKh7RxiGiGQ-WCoLiWre7ey4bzN8jn8ntKwZsCxGyLRoubJhTkRzSseWJ0PvkqadEI_qK6oS4_pxAwdNWYqqSmZmwPxfI2lNVJy3Jg04ycj06qPH8kM8qh_TvrnNpAZjsVBnKvN4C9KYZ_2VOjK9BmuFOyQoUiSLcV0WBCOQjE3e9cI7b_rLm2mbpcztMi0HBLFuoAq8afHdyqgpT-dO9CC5_RQan1xXmSan_pQm1G9FL-mCKWmk4N0di5Ict7V62Evn1fCWlikPdEY3-zXwyokpSHRPl0nbkvu0bAC_nl1B8t5zyBVp9bNzMz7fb-loRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد تهاجمی جدید ژاپن؛ به اندازه یک چراغ‌قوه!
ژاپن برای نخستین‌بار تصاویری از یک پهپاد رزمی بسیار کوچک را منتشر کرده که ابعادی تقریباً در حد یک چراغ‌قوه دارد.
تصاویر منتشرشده توسط NHK WORLD-JAPAN، پهپاد را درون یک محفظه لوله‌ای و با آرایش چندروتوره نشان می‌دهد.
با وجود ابعاد بسیار کوچک، این پهپاد برای انجام مأموریت‌های شناسایی و حمله در برد نزدیک طراحی شده است و می‌تواند به دوربین‌های شناسایی یا مهمات مجهز شود.
از جمله اهداف احتمالی آن، خودروها و تجهیزات زمینی عنوان شده است.
ابعاد بسیار کوچک
قابلیت حمل در محفظه لوله‌ای
آرایش چندروتوره
امکان استفاده برای شناسایی و حمله
مناسب برای عملیات نزدیک نیروهای زمینی
این پروژه نشان می‌دهد ژاپن نیز مانند بسیاری از ارتش‌های جهان به سمت پهپادهای بسیار کوچک، ارزان و قابل‌حمل برای مأموریت‌های تاکتیکی حرکت می‌کند.
#ژاپن
#پهپاد
#پهپاد_رزمی
#پهپاد_تهاجمی
#نیروی_هوایی
#فناوری_نظامی
#دفاعی
#Drone
#Japan</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20572" target="_blank">📅 14:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زاکانی:   به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20571" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زاکانی
:
به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20570" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسکات بسنت:  چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:  ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SBoxxx/20569" target="_blank">📅 12:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20568" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYkF9Ol6i0UUn_PeWaoQ32gPf0sQRDB44EgdcUQghw_0yXTpaDD_ztfaM4wvcNrHh3nOxNxJZbsboPEfxK1TJzhnUcOSKH8wQrFLoGHcX2HkAqQZl3nRlVDAmhkDeMd1_LTfmSfyOGLrphwuKiVg8306yaJCaJ0JnrtXdeEVR-tsg2_5WJ5CVVDUq6No7QJwfgTH4TVycIWKnsyAQaRwN2tHDjSE0EO-NXzeJch8EuHmJqvCtab5Qp_M2zuFHMko2TctbwMTwzqFmMzwZfVQZTDqPPX3AYZSaowk5UPBFIPKgxRnQIEaQHyCTQiFj0f1TamjJaiVaSPAQ4jOnqILwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/20567" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS2XXzg-oB8b4k1OZrjKMtCjz--XSxET3EHW0DOsunsuG-piQmS6iYb8iWA9dQcOINygHKhILbxCFSUeqUgUtg7S3C2-1qLPLUkv1PrJFUDaNxukSk6PwgPercsv1YZZpJobnPZaPkNFWLeIPBJLcYAGtKi3kX9VAaspVHd_O39rp14Bf9ykLol37zxPiBV7ctXycE9mdyEgw7li9twuWH7h6K2jzanM0sztk9xNll8OC4Rp9Hc01ZlyZ2PYqqWC6_n7bBlgd2SatjN3Xlhyby0QPrkC3LhwwqpiQqvIq3mIuHez87Aik5YpIjsvO0txIwNO-JBKK6-RAVZAKBzKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دوباره هما خان سعادت در آسمان کشور مشاهده شده....</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20566" target="_blank">📅 00:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— شلیک موشک‌های کروز ضدکشتی از سیریک به سمت تنگه هرمز.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20565" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1hmaxksCDVH52XDnlWEXogTHZJhKAcY_WrWJltz09vXSv7eudZgI4q-0xhyF239TDvXrfCRxouIV0Xuw34t56PHAk0XYihwEnV6ZC72MHXzNICa6uo0Z0LeesVAB0GBVhDv_ghNo1T2HkR31W63pGuM3hx2wfilLTc8k9BryJx8C3UhxnaRECBrQoko3kt5Kjg2pPYDwLwY6U4wDzT2ifqgDO3yVt_ZscEWWXZMOslt5u7g57uZICMszxtc2cTJ7cHhyTwDb4g_UDkPSsCLAyhfOL4P9ZhmYoqhuDHLIz_38B4WiKltUOtfCJzssOYSzbwon3Pom8o37qnG8uCB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تکذیب کرد!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20564" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم.   |</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20563" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ
:
ممکن است خیلی زود کوه کلنگ را هدف قرار بدهیم ، چون حس می‌کنیم آنجا اتفاقی در حال رخ دادن است</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20562" target="_blank">📅 22:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib4hJwzBM2kAMs4yUqc7QSjnzCo5jVQL-6heMGoM_MsofttOd9aJnQgM56VWUlVYN28iLzahlLMTE9-5Mc0Icljw_SSswxozW6jQD4D_fpBPokTShsPprjHWLJAgr_nex0RqebnFX56qXBjPpDHvxmmQZk3X0YTigyW1fo5KfQL43ut0M12HalqrJHXcxb9VM8kcOtSb-CgoVHeIIR75DD6c5j6yhxNoLirngk2OmDgYW_x9Y0uQ7aOBqphsy7R9pDgNgoz51Qg3itU1xo806AKHg9ZyGaJYT-KoNIphC47ksy_Jq6IuJUHly1rhIqAaHhR5sPj_3M3WsroYkYoV8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/20561" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برخی سایتها و منابع خبری از حمله موشکی ایران به پایگاه‌های آمریکا در اردن خبر می‌دهند</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/20560" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسکات بسنت:
چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:
ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20559" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">از نبطیه چه خبر
نتانیاهو راست گفت که مسئولیت نخست دولتش‌، تامین امنیت کشور و ملتش است و در این باره منتظر کسی نخواهد ماند(به خصوص امریکا). شاهد، رخدادی است که از ۱۰ شهریور تا امروز همه خاورمیانه عربی بدان چشم دوخته اند. خبری وایرال شده.
ارتش اسرائیل کنترل عملیاتی ارتفاعات علی‌الطاهر نزدیک نبطیه را به دست گرفته و زیرساخت‌های زیرزمینی گسترده حزب‌الله را پاکسازی و در حال خنثی‌سازی است. این مجموعه که طی دو دهه با هزینه مالی کلان ساخته شده بود، شامل اتاق‌های فرماندهی، انبار سلاح، ژنراتور و امکانات ماندگاری چندین ماهه می‌شد و به عنوان مرکز عصبی واحد بدر عمل می‌کرد. در واقع هتل-قرارگاهی چند ستاره.
موقعیت مرتفع آن امکان پرتاب موشک‌های کوتاه‌برد و پهپاد به شمال اسرائیل را فراهم می‌آورد؛ و مساحت و تیپ ساختش ماندگاری طولانی را برای نظامیان فراهم می ساخت. ولی از مدت ها پیش، با شناسایی دقیق ماهواره ای، هوایی و تجسس زمینی‌، بستر برای تصرفش مهیا شد.
این عملیات ترکیبی از محاصره طولانی، شناسایی دقیق با پهپادهای حرارتی و ورود مهندسی بود. برخی نیروهای حزب‌الله کشته یا مجبور به عقب‌نشینی شدند و تجهیزات مهمی به دست اسرائیل افتاد. از دست رفتن این گره راهبردی، توان فرماندهی محلی، ذخیره‌سازی امن و پرتاب محافظت‌شده در محور شرقی جنوب لبنان را به طور محسوسی کاهش داده است.
البته این  ضربه به معنای فلج کامل یا جمود نظامی حزب‌الله نیست، ولی موجبات شگفتی کارشناسان خبره نطامی را فراهم اورده است.
حزب‌الله سازمانی غیرمتمرکز با ذخایر پراکنده موشکی و پهپادی در عمق خاک لبنان، تجربه جنگ نامتقارن و پشتوانه ایران است. نابودی یک مجتمع، هرچند بزرگ و مستحکم، توانایی بازدارندگی کلی، عملیات چریکی یا بازسازی تدریجی را از بین نمی‌برد. نمونه‌های جنگ ۲۰۰۶ و درگیری‌های اخیر نشان می‌دهد این گروه پس از ضربات سنگین زیرساختی همچنان توان پاسخ‌گویی نسبی خود را حفظ کرده است.
اثر واقعی این عملیات در تضعیف الگوی «جنگ پایدار از زیرزمین» در جنوب لبنان، افزایش هزینه بازسازی و تقویت فشار سیاسی برای خلع سلاح یا عقب‌نشینی بیشتر نهفته است. اسرائیل خود اذعان کرده شبکه‌های مشابه دیگری هنوز باقی مانده‌اند. بنابراین، آنچه رخ داده پیشرفتی واقعی در خنثی‌سازی نقاط کلیدی است، هرچند حزب‌الله همچنان بازیگر نظامی فعالی باقی می‌ماند و سرنوشت نهایی به واکنش‌های آتی، وضعیت آتش‌بس و توانایی بازسازی بستگی دارد. ولی حزب الله دیر یا زود ناگزیر به مذاکره و توافق است. دقیقا شبیه حماس.
#یدالله_کریمی_پور
#Karimipour_K</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20558" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارشات تایید نشده    از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20557" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amn8oR35cK8jxJxcki_LlXL9J6YtWgkgzan8FTIG7NXt3hP6bnl2lMRp-IXh-PkVRtZTnhoDZ_sHUkyDD6Dj9wX9Rxjo8rlcwFqqC67AA_7VJQdQExDxTH1bL6OZjKXoPWQQtTv2F1wqIrZWnPUcBMvwQyTeyoudq5by8IHoIUx54GINBkcTtVETXUbMKdA3qhOiQOYHkZwGBCZJilwWZbLdjjeIPuoNEX1BEjm4RlipDd7avA4TW-vsWB806PQH5B3aSN3iE6o_evKsuE_wpC0C3B9MTov-JM5yer4BAxuxKkOvYkTpavECOwMSUEebjspCKrvpdX9l9J7Ni38BrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20556" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCh-ka3juWuisMmW22LmMAyfyGpNHTyOuYdresnj8AoYW8CUUCj6IzBzBnlwpOjFy6oAh17lUR4UA0GzcOHfuaQDJ4UsGxN8GeoF9oUKcyZRsumf2rPuu9X9-kMRc9TtC7S8Q8clb84gCA-noiakAB72tg4B65qGIXQJZMWMUnzHhb_qYGERkgt-tHzzEy0Api4LtbGCRWAQd-JATHKYogVCRUftEEyic7jKyr0BukQB5jA2_MGI7r0WXzPaQIeUJgjseXvD83xL1or1xgHThHAovGZn2uhPYOKRy6e-FzZeA-BzWP27xiqtOrkyPZItFqSixi0C69RlonwU4x2vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20555" target="_blank">📅 20:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارشات تایید نشده
از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20554" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از اپوزیسیون هم شانس نیاوردیم !
این قاضی زاده تا دیروز فعال سیاسی بود از امروز شده فعال بازار شت کوین !</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20553" target="_blank">📅 19:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایالات متحده تحریم‌های جدید مرتبط با ایران را علیه بانک ترکیه‌ای گلدن گلوبال (Golden Global Bank) اعمال کرد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20552" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20551" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20550" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این ترامپ رسما دیوانه است!
رفته خودش این کوین وارش را به جای جرومی پاول آورده بعد امروز وارش را تهدید کرده که یا نرخ بهره را پایین می آوری یا تجارت با کشورهای دارای مازاد تراز تجاری با آمریکا را متوقف می کنم!
همین هفته پیش وارش گفته بود تورم بالاست و تمرکز ما روی مبارزه با تورم است و شاید نرخ بهره را بالا ببریم!
جالب اینکه همان پاول فلک زده را هم خود ترامپ در دوره اولش آورده بود و بعد هر روز به او فحش میداد که چرا نرخ بهره را پایین‌ نمی آوری!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20549" target="_blank">📅 18:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش مشابه</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20548" target="_blank">📅 18:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20547" target="_blank">📅 18:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا اینقدر بچه ها نگران این تپه نباشند؛
ماشالله اینقدر تپه هست برای فتح کردن !
مثلا یک تپه ای هست به نام امین الطاهر که کنار علی الطاهر است و هر کس به آن نگاه می‌کند طلسم می‌شود و فیلم «تپه ها چشم دارند» بر اساس داستان این تپه ساخته شده.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20546" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=OotjsRIh02FffzPReTR-yUUQezJ09qaixMZEOwL7E3YFt9oMv_q6sRQkL6WvWrnZea3gIT17q6VGZfAsrUDcTqxBofRzKrmpH8GIacn7ZM0mwtPblY6iLW8U8LpzIdMaY-OZcgvv6DrDL4Altfhw4oyAY7rrCrTVnJjZWFoAhZ9v-JKj_HrOdKPKrO38laAnsGx6nrEwRgQ30W0vs5C9Dhyud9Vk0-RoC59CFfcxm1JaTUI4O53GCkz1iX18aMiJFcdWkVzAfODk467vaJqfzmDfWjdja2xKA4AF1pzafX0G_FDl0_zrep1ldpGKaT8f9DTd6Ct-e5nBEdrv_cbnKVqIF8xrg_opRMWqGTsQzZWv6Tope4U5kyrv6rreFhtwZkciEltSyUyaHvF8LRGwEDM8QZOFH67dpkMY1nGXS15TW2-Kt5Mehz7ZloKADB_jqXt08eKVEAG4kdavPp1A7aGjPqt_8u0t5Gzmqj3Mz5KGQOkkDi1jcfdAaYhH0kVJsYdZAR9_1UeovF4mbgaAhgiFdbtd6pKophgpGwH2xPJmN7AMw9cWCwS1RLw2CpFFFLlfOE92KE6nkZWzf0J0LCMH_m2c2VafanJ51KlS9t7ap-SxILaK_b4hG9yLwvTQTp0yOLCKwUlQOKka-hClkZMKPe7Qy6uanq2yQz21XsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=OotjsRIh02FffzPReTR-yUUQezJ09qaixMZEOwL7E3YFt9oMv_q6sRQkL6WvWrnZea3gIT17q6VGZfAsrUDcTqxBofRzKrmpH8GIacn7ZM0mwtPblY6iLW8U8LpzIdMaY-OZcgvv6DrDL4Altfhw4oyAY7rrCrTVnJjZWFoAhZ9v-JKj_HrOdKPKrO38laAnsGx6nrEwRgQ30W0vs5C9Dhyud9Vk0-RoC59CFfcxm1JaTUI4O53GCkz1iX18aMiJFcdWkVzAfODk467vaJqfzmDfWjdja2xKA4AF1pzafX0G_FDl0_zrep1ldpGKaT8f9DTd6Ct-e5nBEdrv_cbnKVqIF8xrg_opRMWqGTsQzZWv6Tope4U5kyrv6rreFhtwZkciEltSyUyaHvF8LRGwEDM8QZOFH67dpkMY1nGXS15TW2-Kt5Mehz7ZloKADB_jqXt08eKVEAG4kdavPp1A7aGjPqt_8u0t5Gzmqj3Mz5KGQOkkDi1jcfdAaYhH0kVJsYdZAR9_1UeovF4mbgaAhgiFdbtd6pKophgpGwH2xPJmN7AMw9cWCwS1RLw2CpFFFLlfOE92KE6nkZWzf0J0LCMH_m2c2VafanJ51KlS9t7ap-SxILaK_b4hG9yLwvTQTp0yOLCKwUlQOKka-hClkZMKPe7Qy6uanq2yQz21XsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما:   ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید شورای نگهبان نرسیده است</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20545" target="_blank">📅 17:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20544" target="_blank">📅 17:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXZVzroFG_-KtBi6JlVIHrHCaTd4ls8caztcbmhtZkI9wvGJreKhkkGJG9XVH-FP4m1Dv30R4Tbic7gETOdmUOK_tQH_spWl3zgxYNDUBmJndxMInqcwCUj6-iE8nXHfTowcJZxEqQuAz4VrQzf6zN89EmztjqXTeWBoqBi9f-n0XEXJbfzL_4GvTzIPwFoK75QO9w2T6MWecXsAEAUFYvIHnmkvKXv1OsR1BkLVE88xcZp5Sb_Gm_4mpgdmVTd89Sdb6PjCJYYpMAcls-8dv40PyiaeuVRWWOVGCcQHrMA2pqT7Jj11KwGH2OIAZrvnunCsPLrBKvhKgrTQ1KQclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20543" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">در‌ روزهای اخیر باز اسم عاصم منیر مطرح شده بود!  سبحان الله !</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20542" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20541" target="_blank">📅 09:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ظاهرا آرژانتین با حمایت ضمنی ترامپ به دنبال حمله دوباره به جزایر مالویناس (فالکلند) است.  جالب است که به محض انتشار این شایعه، استارمر بحث تروریستی اعلام کردن سپاه پاسداران را به جریان انداخت تا شاید از امتداد شعله خشم ترامپ جلوگیری کند.  اخیرا بریتانیا تصمیم…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20540" target="_blank">📅 09:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_SnH3MFlm3SjXAT3orX3wuHNtbtshXF1PVuFnvfsNI0Wbn8PDUzVZA5fwUn6RQUnVy-vXa0-rpAxRkupyp7t4rDn-29qBIF3BFxUP-ucY_Q9zsGJfLpei6uHNX4khmzwMSiOmsC79MW26JmpOuD86uYVAuTzjqFSDORcbF8b1qcR01aXwralouYg-OTNf-ZViYkkhSB19l6Sv5vprPo60SbiEhuKgT1d9vaCXkfy16Qnbs_sKQmle5ymrY4zsCSy8ZDKwmNYruY9WAkC89uC8xsR-dovd2y6l9R9KyxgQ4V7M0oAywKHT0Sfse-bgVYpZgBSb9yHNrzn9KwbzAwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش خنثی سازی مین ها از راه دور
این روش عمدتا توسط نیروی دریایی بریتانیا به کار می رود که تخصص ویژه ای در مین روبی دارد</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20539" target="_blank">📅 01:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEjmhkuRKQMjT9v1T-fDYbqoPUzotAnVaxRxGk4yUMUJzZYqymv0w6Yar2BzyWioSFzcRZQK5lafs4P2X0GmQD04BAEsbzNONaLWOvU1fDUc5Es1HcqyJ3-z8F1QMMkMdc2g8xul7j4PqIjbfjlx0I44jn0eLlbp5q4980s7e6U-0wDAi0FiM_3C-IiJj7VfPIwUtB7IxwO0AzVoDXTYYjuHgpFZmky5sy4iRrBVSigWQZXrfx-Wl03ftM4NWgvGW6Ws0AAXfePpD4PoVOCWhEUPUf3eqXObRT3WVE-bVZK1lfFuofM0u40mSBn2Z2mslv7krUpRdaF0n0ofN2QV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.  مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20538" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20537" target="_blank">📅 01:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=tFqhGQa0KkFIUs2tw5E1Edi7uN4MDi742XhG7-WvMaAQasNeI0hX26wURSvyr6Fag7DtKk6j3GynsTgTjGoJlwfzQe0KSMICOmiZlTDuifPfmrmhg76fi1pgBNqJOWl4enY_jnsQcRbfU3JGbjHNqtb-KRs1eVscPpe0n1rIJ33fvgzWosFyzezn0I6fYRv4i3y85HANYdpfFvojkniaJWrhPrTBuaOQZKPgq-48h6sED2cXvaGM7epm0Li227JIzwzuO7VMJkE9wHb-oyiFNmJLN9GX4P5xRAnskDRWdt8NmDcZeeBA2a7Z6sW_5S9ihh4Ff1erVHkoMeLOzk8dOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=tFqhGQa0KkFIUs2tw5E1Edi7uN4MDi742XhG7-WvMaAQasNeI0hX26wURSvyr6Fag7DtKk6j3GynsTgTjGoJlwfzQe0KSMICOmiZlTDuifPfmrmhg76fi1pgBNqJOWl4enY_jnsQcRbfU3JGbjHNqtb-KRs1eVscPpe0n1rIJ33fvgzWosFyzezn0I6fYRv4i3y85HANYdpfFvojkniaJWrhPrTBuaOQZKPgq-48h6sED2cXvaGM7epm0Li227JIzwzuO7VMJkE9wHb-oyiFNmJLN9GX4P5xRAnskDRWdt8NmDcZeeBA2a7Z6sW_5S9ihh4Ff1erVHkoMeLOzk8dOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20536" target="_blank">📅 01:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سوریه به فارسی 𓂆</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=T9ixXvRjMu3W-YTSQVM4I485IryU9_9-afVUVCos7cctzn7KgXf80RpUJRbn9-fnQQ71fWy9-lPP_xUxE1J4I0TDWrcToNUV4-UzCBaDalojVQHJ3yBEXw7VBfDfZQFxCvfM0eeWqgF81YTvgRsX290aPizfP4kXsk_jfoqYIoutOzIPBItSiKneC-XqvGidSEJkRfoEJb316Rfeqf8Mvh0OYD-qIcLSMoDgz2A5tESdMT8xYZXthIXkbr7SfvsSoc5A43QGY9rdzqy_8XIFj_iNkzCsuM4utZl5yPtNAop-oT6wEzbNnsYDQ9S65ouqFquAWtcCWFuKmJwHSIB6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=T9ixXvRjMu3W-YTSQVM4I485IryU9_9-afVUVCos7cctzn7KgXf80RpUJRbn9-fnQQ71fWy9-lPP_xUxE1J4I0TDWrcToNUV4-UzCBaDalojVQHJ3yBEXw7VBfDfZQFxCvfM0eeWqgF81YTvgRsX290aPizfP4kXsk_jfoqYIoutOzIPBItSiKneC-XqvGidSEJkRfoEJb316Rfeqf8Mvh0OYD-qIcLSMoDgz2A5tESdMT8xYZXthIXkbr7SfvsSoc5A43QGY9rdzqy_8XIFj_iNkzCsuM4utZl5yPtNAop-oT6wEzbNnsYDQ9S65ouqFquAWtcCWFuKmJwHSIB6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا درسته اسرائیل علی طاهر رو اشغال کرده ولی اینکه ترامپ پای یه کاغذ پاره رو امضا کرده به شما حس خوبی نمیده؟
@SyrianToPersian</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20535" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فشار اقتصادی آمریکا بر ایران در حال تشدید است
رویترز
کارزار آمریکا برای محدود کردن صادرات نفت ایران و بستن مسیرهای دور زدن تحریم‌ها، فشار قابل‌توجهی بر اقتصاد تهران وارد کرده است. کاهش دسترسی ایران به ارز خارجی، محدود شدن کانال‌های مالی و افزایش هزینه شبکه‌های غیررسمی انتقال پول و کالا، توان تهران برای مقابله با تحریم‌ها را کاهش داده است.
مهم‌ترین ضربه، افت شدید صادرات نفت ایران است. بر اساس داده‌های Kpler، بارگیری نفت خام ایران از حدود ۱.۷ میلیون بشکه در روز در سال گذشته به حدود ۲۶۰ هزار بشکه در روز کاهش یافته است. این کاهش، درآمد ارزی ایران را به‌شدت محدود کرده و همزمان با سقوط ریال، تورم نزدیک به ۷۰ درصد و افزایش هزینه واردات همراه شده است.
ایران همچنین با محدودیت ذخایر بنزین مواجه است و یکی از مقامات ایرانی ذخایر فعلی را حدود دو ماه برآورد کرده است. اختلال در کانال تجاری امارات نیز فشار بر واردات و تأمین کالاهای ضروری را افزایش داده است.
از منظر سیاسی، واشنگتن امیدوار است فشار اقتصادی تهران را به مذاکره وادار کند، در حالی که ایران تلاش دارد هزینه‌های اقتصادی و تورمی جنگ را به مسئله‌ای برای سیاست داخلی آمریکا تبدیل کند.
برای بازارها، پیام اصلی این است: اگر محاصره نفتی ادامه پیدا کند، ریسک کاهش بیشتر صادرات ایران و فشار صعودی بر قیمت نفت افزایش می‌یابد. در مقابل، تشدید فشار اقتصادی می‌تواند احتمال واکنش نظامی ایران در خلیج فارس و تنگه هرمز را نیز بالا ببرد؛ بنابراین بازار نفت با یک ریسک دوطرفه مواجه است: کاهش عرضه ایران از یک سو و احتمال اختلال گسترده‌تر در مسیر هرمز از سوی دیگر.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20534" target="_blank">📅 00:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20533" target="_blank">📅 00:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P99AgU2ircdeEsEOXnPnF8Xp7Jl_MKWkWAMYAJYnJToCMUL0f2ud4QOnqU7fpO9h20P41gnORzKGwhbpKvC24IC24pWHH98R5q9jK1k1_v4GmfyFbrzLA4GYzjy-QdDcc6HuRbwn38UB3XMKN7p09GMHpg43YXZt4iwKFHH4G-nA7vf1t_BLJTre1cO-MtYZslK7YHwJAXzt5gDkMZHB7VQ3FnPLZFXdUg36kNYgHjl243PaMlFJfUQiIw9YMHn2IBC5VgWHZQmYcI50_328qJR1brj6sBkWKu3yeQ-Ta5hGYqaaSn9ZHP-6L2ljgOGojI0OnAZNNGzISVCh6yW8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20530" target="_blank">📅 00:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20529" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-k6MB4_ovZApIgUO9uv6Qhw2tJNRUguQHcJ_eX3KBc-5BiqTZygyxzx7UKixwqvMVZOjUs3MdO71Xy1CYA1_4i0fsscim8qBuo0yrzWwM5Hxl__EpPASMTCFlgMvAIQTv6_6Wt38_qutjJkrk_D7qm9FZPmt_UHhT0KfSlI1pZP0gLXrdknpmVnS-9-URnxb6Oe1gX4Zbsc_K2v91v-T3mHAWE-pENWJLr28GVeBs5cThcLloh2LlwmznSzOliLZ4XAMeM5Viltpmm-N9LOkZSvKndQPinzHNIBrytn0V9cb5FL3o7LQ1hSOkFKJk4ZcMAuJbpwN0oHVQF3BMfG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۸ سال بعد از حمله هوایی ، اسرائیل اعتراف می‌کند که مشاور اتمی ارشد اسد را در یک حمله شبیه به سبک مافیا به قتل رسانده است
در ۱ اوت ۲۰۰۸، غواصان اسرائیلی به ساحل سوریه در نزدیکی طرطوس نفوذ کردند، به ویلای تعطیلات سرهنگ‌کل محمد سلیمان، مشاور ویژه رئیس‌جمهور، حمله کردند، او و مهمانانش را در حال شام خوردن یافتند و سه گلوله به پشت سر و گردن او شلیک کردند. این موضوع را اهود اولمرت فاش کرده است.
«در روزی که سلیمان حذف شد، جنگجویان ما از آب بیرون آمدند – تیراندازان چابک ماهر،» نخست‌وزیر سابق در یک خاطره‌نویسی جدید نوشت.
«او را با قطعیت شناسایی کردند. با وجود اینکه تعداد زیادی از افراد روی ساحل حضور داشتند، هیچ‌کس متوجه آن‌ها نشد،» او  مدعی شد و توضیح داد که چگونه کماندوها به‌صورت بی‌صدا به خانه سلیمان نزدیک شدند در حالی که او و مهمانانش روی یک تراس باز نشسته بودند و از فاصله‌ای حدود ۱۵۰ متر به او شلیک کردند.
«سر او به عقب افتاد. بلافاصله پس از آن، جنگجویان به سمت آب عقب‌نشینی کردند و راه خود را به سمت قایقی که آن‌ها را برداشت، باز کردند،» .</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20528" target="_blank">📅 22:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز چند بار تتر تا ۲۰۰ تومان ریزش داشت!  به نظر عده ای دارند نقد می‌کنند   تارگت کماکان ۲۴۰</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20527" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl1-AxNNtY_IIBQ-PKkXDH8ZMtFiYuJcINxPsN3YLV332F1UswuUONCqOgi5KEpkI1vTZiCtHtpb1thDJLzTQbMrg1MitoBQRua2W1Tjm-Fu8q39Br_gW2b8G94n7xTPJTW3ejVQZMn4X8m1v6NnGTfeN0i2I6sA_XILsntwCu5SWAv_nPtpzkM0AEWU4AhBjDCK7_Z7cVPJpkU79CEiad_u10x57NuXoRDmMacEFWx0AQCzziZzxR4rYDgSRjkkpjLYWu8zpfOvV4Fk7cROxFiNmn-XpngXclOnSs7d0qfa-r0L3bTPdsxhcX7c2HldAQzTPZt-iJrAHRkFdB2Ylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه  وقتی روی مواد هست  گوشی دست نگیره  مرسی  @PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20526" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20525" target="_blank">📅 20:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سبحان الله این محمدسامسینگ ما چه انگلیسی اش خوب شده!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20524" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20523" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnG_3Pl6haWYOf_z4cZ8wDgO82DtuO9gtXHw2rtRcQCasXDCkJcs2syLLG4JNpWqigrr5tSJUp53mLarD-kN_HuBTQhQKCCx_1_7cUZnj7vExKEmGlFg9Bmb_-8ZOALKhGH0vaEE0fGdkVtVHPgoz1k-3BAtTfib7mm1tPy6ToKBUgacxdUXLLGWQSEksX_e6odfR_iIoQm7hj5OBUq_yCTb6JZsDTcegVlJVaL3V4xc_2oRtKabd1cRqWRxno-XvCFD-u4ae-GYAbpObw9dwZ3wZPskHRHWjbVD2Z_Tmr0GBYK-BUxy5WHzhoB8tSRLxGUxsAprvrFOXU9Q7mJtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف خطاب به وزیر خزانه‌داری آمریکا</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20522" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">موشک‌های ایرانی به سمت کشتی‌هایی که مقررات تنگه هرمز را نقض کرده بودند، شلیک شدند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20521" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:   ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.  من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.  این ماموریت…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20520" target="_blank">📅 19:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل، در مورد ایران:
ما با تهدید نابودی توسط رژیمی روبرو هستیم که می‌خواهد از بمب‌های هسته‌ای برای نابودی ما استفاده کند.
من به توانایی خود برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم.
این ماموریت اصلی است که هنوز پیش روی ماست، اما نزدیک است. غیرممکن نیست؛ در دسترس است.
آنها بی‌دلیل از حمله به ما اجتناب نمی‌کنند. آنها به همه حمله می‌کنند، فقط به ما حمله نمی‌کنند. آنها قدرت ما، قدرت بازوی ما و عزم ما را می‌دانند.
من به طور کلی به دشمنانمان می‌گویم: با ما درگیر نشوید. اگر چیزی یاد گرفته‌اید، با ما درگیر نشوید. ما قدرت، عزم و وحدت درونی برای غلبه بر شما را داریم.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20519" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.   گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20518" target="_blank">📅 19:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۱۸ سرباز پاکستانی در یک حمله چریکی در منطقه زیارت بلوچستان کشته شدند.
گروه BLA مسئولیت این حمله را بر عهده گرفته است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20517" target="_blank">📅 19:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بفرمایید:  پنتاگون آزمایش کمبود تستوسترون را روی مردان بالای 30 سال آغاز خواهد کرد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20516" target="_blank">📅 18:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20515" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjnyHTH_YL4e6XUN7Nw0BuhyQ8BcFtAqJyrOjh-cbg_UGb7njNiO8J1wX4Um-DuW59l5B-50zZeBQknurrLwL6NUZBWvafjUUlTp3zmIiv__vby5E_KJm1SZm4v-4jYdsMgQzd98nZoEAweI0PSN8g7KidhHKUPN-XOIvSRcCFztbB06moKmGnIakuek5cc1D4n9Sh7U0rFpmF1_nc9qxL8IEBeh9XI2YTb6Hu-DEv_UpCwFA79BwioXKXrt-jWfxhgb-5yrem9-5VCU31hQBLJnZvJ34kYMo7AGHIvSNwYydd3996C_zTBgVkoB3DiJk3oPewNz05Xkufx2vOZqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل دقیقی است. تمایل جناح تندرو تداوم همین وضعیت است تا هم فشار برای بهای نفت و اقتصاد کشورهای منطقه و نرخ های بازدهی اوراق بدهی آمریکا حفط بشود و هم هیچ تعهد جدیدی برای خارج کردن اورانیوم بشدت غنی شده و برنامه موشکی و .... داده نشود.  طبق این  دیدگاه، نهایت…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20514" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ :  برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم،…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20513" target="_blank">📅 18:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ :
برای آن آشغال‌های  خائنی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کند، ما عملاً مقادیر نامحدودی مهمات با درجه متوسط ​​تا بالا داریم، بسیار بیشتر از آنچه که می‌توانیم برای این جنگ یا برای هر جنگ دیگری (که بسیار بعید است!) استفاده کنیم، جنگی که به احتمال زیاد می‌تواند رخ دهد.
علاوه بر این، ما در حال تولید مهمات در سطوحی هستیم که قبلاً هرگز دیده نشده است. ما در حال ذخیره و آماده شدن برای هرگونه احتمالی هستیم. ما آنها را برای خودمان، ایالات متحده، به جای فروش به دیگران می‌گیریم، اما فروش به متحدان به زودی دوباره آغاز خواهد شد.
همچنین، لطفاً اطلاع دهید که دولت بایدن مهمات بسیار بیشتری را بدون هیچ هزینه‌ای برای آنها، نسبت به آنچه ما در ایران استفاده کرده‌ایم، به اوکراین داده است. صدها میلیارد دلار به اوکراین و ناتو، رایگان، داده شده است که اروپا می‌توانست آن را بپردازد - اگر فقط از آنها درخواست می‌شد، اما ما آن پول را درخواست خواهیم کرد، هرچند کمی دیرهنگام!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20512" target="_blank">📅 18:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20511">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzYTuEkyx__-cvnvfeukWhkozpwh9f-Rbrce_0lplRqOhDqUpQK94qdX1zQvBPv1EvtnnFNpeY7tlC6kMDESmenyoD_WKXubX17ITbnNfgjjrw8CaiCDtvn1RjMCqbasg3WnbDjGIFApOHGSChp70EVdjJA9ffxJphCn5LCZ2mrd6eR8RE8xFI9A10GYK3yhXbIzXawhdla7tyCdZnugRaM1rjnVfszWaoDugPxBHJlMubxVjWgYf3oou0Fw1byeuu5dc2DucYxNdprFJt96a215IMIcvRU9fzfmGfr5E6RhggNSjio7vAyLMIt56d7uua_Tn2nYjDasdSMCXPuMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار باز دارد پارابولیک رشد می‌کند و من خوشم نمی آید  فکر‌کنم تا ۲۰۰ پولبک بزند.  تارگت کماکان ۲۴۰ در گام نخست</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20511" target="_blank">📅 18:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20510" target="_blank">📅 16:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20509" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#سکه  عیناً مطابق سناریو ترسیمی رفتار کرده تا کنون. شکسته شدن خط مقاومت مورب یعنی سکه دوباره برای بالای 200 میلیون تومان خیز خواهدبرداشت. (برای موج نهایی صعود)</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20508" target="_blank">📅 15:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">در حملات هفته‌ گذشته آمریکا؛ ۳ خلبان و ۶ افسر نیروی دریایی ارتش نیز کشته شدند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20507" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20506" target="_blank">📅 15:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایران از طریق عمان پیامی به ایالات متحده ارسال کرده و هشدار داده است که در صورت هرگونه تهاجم اسرائیلی به ارتفاعات علی‌الطاهر در جنوب لبنان، به‌شدت پاسخ خواهد داد؛ جایی که باور بر این است که نیروهای سپاه پاسداران، از جمله دست‌کم دو افسر ارشد ایرانی، در کنار جنگجویان حزب‌الله مستقر هستند.
— رويترز</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20505" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
