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
<img src="https://cdn4.telesco.pe/file/edHwB3Tg161wjMCQG7ePdnsXc2Z6NyfSrKNlpYg-SzjP0Cgot7dwF4Yij4Tv6P-9fLaXrVgRhVLvqTOWS2V2oOv0uVHRPMF-jT2c_o2zPhhYg3gfAANjNfTdwiIOdBTCSr5QWfK3TAyYUIRkhSgg9aCCnVrXhIIuvBc8BM_0lYxxW1BXs1RUucr7bJCJve7aqktPaveTkNY3lFBWTiQE_U08iZ0R5UzF_MbOpKPLNLmL1uolgpNECjbEKB5wznPDf5sXJoVh-qdWWLYNJTeuMHqzKlxevTdUXYHGBo7Z4bS6BX7_kLjFmtsrJ2OOUXdURgNyVuC1uQlNVyJAGrf4wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-670646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEudFHjVLXOqoKX24VJC3Kgyn7cB-TYcLTvNs_HKvXRiLxFcPDYtKwimzuFQRhrUbyhqnvb1G29ZTxKX85ePsbOfB9SmxLLrybJ1RWiTTLUP9m8VredSziBUZsX88Qk4B0mkvL4G0179GJUjXMvIHcShwo2DSEgBIYeFs1ur2cKvRUYuQJEQq_giyjALNqlMioaXKXOvdb5aFnl-uC9nSGfgVCiFXZX36iG8jpcFWNo7vdmbEIS7MhUr7wkkCA4azZKc-ugsAG9e__FzYnG4Q-W5vjTGCHrUQ6YTKs-xP9OnVVao6zYswhsgiYb8VQjTA3kq5ka4Sk5ZmYhyo1N1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: مهران (۱۳۹۸)
🔹
ژانر: درام اجتماعی، دفاع مقدس
🔹
خلاصه: پدر مهران به جنگ رفته است و مادرش هم مدتی است که فوت شده است به همین دلیل او به خانۀ پدربزرگش آمده تا به او در میزبانی از خانواده‌های جنگ‌زده کمک کند. مهران از شرایطی که در آن به سر می‎‌برد…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/670646" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQgzQAvz_nTGLbAHTHgUTR8FZ41p1QDa4JkCTELqFswhnyFKLTuRJBEw75wzR7uWOmFyp8dSQnT6eckACUNNJMSoYh1kxzBHpmqEY8I80EAkf7rRfWFFraGv4jXQpeqzP5a7NAGMtks2scbi0QZrUhkOl8NmwpU9lT6LbL19m-1Z1rIkSPcIl7Q6UHtKbOTIVNOtarpWOUw8ijz7MG28XTevNH3O5VzFnwpj3O_KB8BeCccOkrD4cvCc0S6MTCFMKy9AhjXgn6rL7zu-HQcSo-PJ93KZ2iAjSCDeEi7MpgopGfcZltYglEZWiTmADO3nUXIcBgnTjNGSctDIwXXGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار قیمت تتر در ساعات اخیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/670645" target="_blank">📅 21:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb62dc134.mov?token=rLufnwwmckDi6ReSXgrvVTFO6LvkamP6b-ztjQZFt2y5nRyuTMSHu1CLhHCyP3Wc_DsjWHQWKbv7s7RvvJ4TlVNg7l2bnh_Sl9JzHngTtPkmqa0syxuZCWnelbwXIt-KnCNpG7eZd01YOnYsaMWg3nXhcfvUDcdg2UU-gTxypdz6oxc1EmM44k8mAPiUOkkkP7wI2R99RuU8QAooaTCmY7kmdhGeUJPuNmJlCBxTwen_QNTPgTZu8GqlWl6k28el-XAC8yaxwdP--NKSnd0uZEcQGLyXzDvTNPNAHWvrRgAZFNRf1_CjUuhA18atiL9KpEXZ93B2dNohKJIvzstsAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb62dc134.mov?token=rLufnwwmckDi6ReSXgrvVTFO6LvkamP6b-ztjQZFt2y5nRyuTMSHu1CLhHCyP3Wc_DsjWHQWKbv7s7RvvJ4TlVNg7l2bnh_Sl9JzHngTtPkmqa0syxuZCWnelbwXIt-KnCNpG7eZd01YOnYsaMWg3nXhcfvUDcdg2UU-gTxypdz6oxc1EmM44k8mAPiUOkkkP7wI2R99RuU8QAooaTCmY7kmdhGeUJPuNmJlCBxTwen_QNTPgTZu8GqlWl6k28el-XAC8yaxwdP--NKSnd0uZEcQGLyXzDvTNPNAHWvrRgAZFNRf1_CjUuhA18atiL9KpEXZ93B2dNohKJIvzstsAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی که گفته می‌شود مربوط به  لحظه اصابت موشک به فرودگاه ابها در عربستان سعودی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/670644" target="_blank">📅 21:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670643">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e961e08c.mp4?token=dBhAopjj_H0JT3kkbjEtcVJ-erSS84P6L2i7Qg2f8JcIqjlJQSUEtoLj6Y6iZKoVh_9GoLjEGcIU6eqS4GYX_hXYsUttdNogBTNvpriL5oXRL0Jsx0VgIOPGEiDv5jp7ylo1MmbzaylL0n93fw26LF4E2TP_CJsH1Vlmlon-qNv8vLIRiHfwtKz_JYwLqkYO61DzkH23QKkEQJiIKEpyIOggabH0peWgUbWfFht-WEYb4OKUCShf2f0U6WeNVMKgfEAjfPGtJIlUTM3sVN6HNphsB26NLkV2xaUlGWfWmpe8FaUAy7OvIVeO_gBLm95qogzARy8Ul4IANJjt0tyBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e961e08c.mp4?token=dBhAopjj_H0JT3kkbjEtcVJ-erSS84P6L2i7Qg2f8JcIqjlJQSUEtoLj6Y6iZKoVh_9GoLjEGcIU6eqS4GYX_hXYsUttdNogBTNvpriL5oXRL0Jsx0VgIOPGEiDv5jp7ylo1MmbzaylL0n93fw26LF4E2TP_CJsH1Vlmlon-qNv8vLIRiHfwtKz_JYwLqkYO61DzkH23QKkEQJiIKEpyIOggabH0peWgUbWfFht-WEYb4OKUCShf2f0U6WeNVMKgfEAjfPGtJIlUTM3sVN6HNphsB26NLkV2xaUlGWfWmpe8FaUAy7OvIVeO_gBLm95qogzARy8Ul4IANJjt0tyBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای با کیفیت، از اصابت‌ها به پایگاه شاهزاده حسن اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/670643" target="_blank">📅 21:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670642">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6bbc5d3c7.mp4?token=TSObALnLdT5EVwnVVXUe7S0wpuJYrUL91L3pt6lpZYNTE1ugFiw7MOSf0dslgYPlsvi7nb1GcI3yWHZPpHl9Y2cvLjwrPHhdXa4kdbGAONtoSLhZDDy-P2cH13ecy-7-IUIjpyU27o64VmndbqzQ6AEtKgtqWDZU0G5_IdRshwjmvGOl6xi62iKsccpXMmxFnHOwP3yKnR3kjJ48QqY0G_g3ncaBnUXIvB3MPANMYH5g3mqHElrdSRzRCKbUyCLV2PC1Cu59uyoq6ARcUV5-QHHO4S5T5hedIylB9vVtQnEshm2x7hO-FtegbNzOlxUVDCPyzRyCAL7VpvN6EVBQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6bbc5d3c7.mp4?token=TSObALnLdT5EVwnVVXUe7S0wpuJYrUL91L3pt6lpZYNTE1ugFiw7MOSf0dslgYPlsvi7nb1GcI3yWHZPpHl9Y2cvLjwrPHhdXa4kdbGAONtoSLhZDDy-P2cH13ecy-7-IUIjpyU27o64VmndbqzQ6AEtKgtqWDZU0G5_IdRshwjmvGOl6xi62iKsccpXMmxFnHOwP3yKnR3kjJ48QqY0G_g3ncaBnUXIvB3MPANMYH5g3mqHElrdSRzRCKbUyCLV2PC1Cu59uyoq6ARcUV5-QHHO4S5T5hedIylB9vVtQnEshm2x7hO-FtegbNzOlxUVDCPyzRyCAL7VpvN6EVBQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم:  قدرتمندترین ارتش جهان را داریم
🔹
رئیس دولت تروریستی آمریکا  که به تازگی باج گیری را نیز در کارنامه  خود ثبت کرده است، ادعا  کرد: ایران ۴۷ سال است که اراده خود را به دیگران تحمیل می‌کند، اما نمی‌تواند این کار را با ما انجام دهد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/670642" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670641">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-SLl4Ae98cM4Oo8w-X-d438C9mtZOg2JBEGdCy7MGXoi_daVpVwoOFtTV5qj5rqTj_4mZ43R0E6roLrrugwTxSN34lnkGPM2pkZqqnlUBe8WLxpr363T-KtF9ukRaYg7y8jKDLCiBlLsoGxQdm9JTE8YoFyVbTY4nvGPKv6DTvxQ-3JotOylf8aJLpSMLX9ozyd2PQAKra4Au06hwJoQ9n3614Rdes3gn4RMB1C9kd4n_cQZMej37SKaO9S4svYNTlvtrjiWgVS_SVJYCnD2MdZNrLdeSxgXlnVT5uDgVLfNRhBiJ0jVjgLL4rn2SWpS7N9YIjsqlO37ZLWGnhRgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین قیمت نفت ۸۲.۳۴ دلار /انتخاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/670641" target="_blank">📅 21:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670640">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز: با اعلام محاصره بنادر ایران توسط ارتش آمریکا، قراردادهای آتی نفت خام برنت ۸ درصد افزایش یافت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/670640" target="_blank">📅 21:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
روایت مهدی قربانعلی مکبر نماز بر پیکر مطهر رهبر شهید انقلاب از اتفاقی که در اجرایش افتاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/670639" target="_blank">📅 21:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670638">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79310f2783.mp4?token=Guh7d-_3x5ndWyLHhLe-vSRznmRXU86lvd2Qd2x8sKqGAZhWHykzpWrraBtT4y7cyDDgJYILMRXwaKn-6En7snEl2FCEWscvBHrBXS9jHT5r-nqzAld2dy9YZ5wwylX5f5cLFj76rhSZCT7HZukwQOWfT3aftsZAp5zdjVXSm9CXWdDrw5bkxKvZD82PczYorMs5RuMrNxLvVROOUge1Qc9sZNMCV1YDVcHbKTqkNvRyK8gc6e9QpRZwIegNLc1q-tIAEkJPp_e2DQNRzVrYDvH1vJEztxoNiljR9HXA_gXFUS3jOHrqx6sqB641NsyGqttveOoGvq3eVbXDuHZ59IRdJuQl_EAO1jrFf3pGOu0vMKLEAxOi6EmBTzuqHAElUQ70edq2lmh06uhP3a6T4a8df_vrGo-9XOT-DKm5xzRmtR-55J_R_tqCpP2WCF_KMn_l1pFlRSwZoAweC3DfaNP0lFsb0SrRyxvBk2Z7-nbbYiDgDXFD7_no3AX-2lb8xekOITv9RJFBDmBKg2lhWeWJjbaxkDcZZbjsKfGoR55wrH_1ipzWVzhCwvKLKbtC6EKXHZhXsr1ufJ8aZRDH5wMB_n4k2RtL4qWtra7V8h4mcaSCTxWwNuQS6pUAuXxxjKuadNybXzigRoSphXrKx8h6hxLipHu8ciYGR1tYg_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79310f2783.mp4?token=Guh7d-_3x5ndWyLHhLe-vSRznmRXU86lvd2Qd2x8sKqGAZhWHykzpWrraBtT4y7cyDDgJYILMRXwaKn-6En7snEl2FCEWscvBHrBXS9jHT5r-nqzAld2dy9YZ5wwylX5f5cLFj76rhSZCT7HZukwQOWfT3aftsZAp5zdjVXSm9CXWdDrw5bkxKvZD82PczYorMs5RuMrNxLvVROOUge1Qc9sZNMCV1YDVcHbKTqkNvRyK8gc6e9QpRZwIegNLc1q-tIAEkJPp_e2DQNRzVrYDvH1vJEztxoNiljR9HXA_gXFUS3jOHrqx6sqB641NsyGqttveOoGvq3eVbXDuHZ59IRdJuQl_EAO1jrFf3pGOu0vMKLEAxOi6EmBTzuqHAElUQ70edq2lmh06uhP3a6T4a8df_vrGo-9XOT-DKm5xzRmtR-55J_R_tqCpP2WCF_KMn_l1pFlRSwZoAweC3DfaNP0lFsb0SrRyxvBk2Z7-nbbYiDgDXFD7_no3AX-2lb8xekOITv9RJFBDmBKg2lhWeWJjbaxkDcZZbjsKfGoR55wrH_1ipzWVzhCwvKLKbtC6EKXHZhXsr1ufJ8aZRDH5wMB_n4k2RtL4qWtra7V8h4mcaSCTxWwNuQS6pUAuXxxjKuadNybXzigRoSphXrKx8h6hxLipHu8ciYGR1tYg_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه جنگی یمن مختصات فرودگاه‌ها و بنادر مهم عربستان سعودی را که احتمالا هدف حملات انصارالله قرار خواهد گرفت، مشخص کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/670638" target="_blank">📅 21:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670637">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTP2MaU9m_9RYxmBlwjB2NvWWoUJdUzwVyNkwSNVirLJfXCG_d0M52T_QAGDKEpws3vq8u4ShLqzN0_da8QH0dGfn7g4oHRW4M5CZMArJ8umnQ1edQKGC3b_HzPzRc2kuZh9RyK-lENLgXNuti1QxfStopFPcjgjYtiEeV95SmR3g5Kuo_AXI1sN0Vidq4G5NArJndelmEU7gESN0RxkCmpoU78Gqg4yt4sTm-UTfoX5MgI32mvI1HYuOOD2Qxiy_39Z5SZOoaI-jQGIF3RoLzuta9e9KRJ5B_FSF09FCXyxIII5Lwg3AaZEd83-6WIPpMc4GzpLk6GkN9F8fmv-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ترامپ رسماً کنگره را از آغاز مجدد جنگ علیه ایران مطلع کرد
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/670637" target="_blank">📅 21:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670636">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای شیطان زرد: ما داریم ایران را تحت فشار قرار می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/670636" target="_blank">📅 21:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0-1nibP4xUMoiTHM4n2ME2iNIC3T52p_lXachi1ge3e_wjBx1HGhfxs_jKcKVBFbIIpayJ0kUzQs_M92IYkJV5sEQCudsLm_-rTm9FM7XMbA0QgZdvgGL_hC3syTz12r-ZXOPJOupl97nhFwpWoSVAxkKof3wT1MdWmTbEE_mlmwuSixREOoMbhSyoyGWlCinWgD4vvYTjQAO41E23QRmgKYN7V2uFjcFEFLe6SNKXB4bkOirlQ2ABgYtRKzwsvnjEzvM7iztrsSNXjH2klYunntxkSFeGrreKQgGGt2K7JjYXjqlgJkihLUEqvquBWB6SmpYZg1SaB7-obBKLQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lfy5rp3VXUHCKgxEr8ZuhpXg2PchmgIBCN5E3HvD9hvVT4If_RP3GCMKgWYrMq-ZTpvVoilp23W6eaIJrtSJjhgX92_7iRSl_r4jFqEf2GTxlonTTzBlpcRr3p2FJ7pyJ96zVN58mjJ0ePduQdQ3OSqnR4QHjScVvGqvlwT3Q25wCz5qgpsPjqTRe1L6UuVXeHyxiP2lSdcS3Rl77bjFb8ieP-eCyZCVPPb3HQYepdV_EgOHSRUCRcZpf-5BFyam3bR0Jn3trJWqH5ozF5RcwMQXX4tEQqr05xxLlM8IE0ZT14HfDSk9B25qFfM5YQqGDvxe_K9nvVN0842rLgOPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iD1DB48OjPSRyRUSV6eP8S560IsVTcQUdNdc-uhpydohb0gyx7GrpnOWNAxEcIbTt5lgybNfgKKZuSYEhvtT2UYaTinFztEuSY-rbd5umfUjlyxG-Qvl6YqNXFfxb3HuekH5EBvVfpWu6a7EMcxD3i29sskc-c5lS9-DM_OBu8__c_tdC6fMvpee8kFXkCPa_SH_dCMoeC-pCtqaUjWGu1DXyv8Vf-vIOujrAbQJlsVw5lMdv5KYFLCnNYv9xB-_4qkMBJnCokWV1sm88v4IKi6SYehGfYncm3x51KmUL70auz_k3BG6WRwxIMkzICTgXk1n8PZrTI-DU5u0GNmJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP5rief4GAv9khl2zfwxW9BjCpbP7mtsyUWYJ8DWQxMG6VuHXUhhpOvINNCZNOMKYqe2BRPclyhr-QlpjtZydaePzOMfQ4H25d1cKvA2V3zsIYbKRR48Ye_5Lk4eg-4AMf1Jtnl7oeaDP0Qu5hh1yYNfuOKEBjjpLPEDqgR09_AOT_8ir5ESFohZZmWOfUtHwJ3_9DOJODct0dwEVA5NBqWvKHvjW6gB62l4Qix4I40f4K6OgkBkP_A_pXT7QMzH2A5hfQAE8_MDubmX8jvzIbeQ2sGXej02xItY0Z1dmBaM8Pj3BpOpCtr8FTIpnDODvGdsjohqM-rgto81M805Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rannSnkz_8hGPLuJEpVlo8cSBhKF-u0_97U4NTs529ut2S0-XvmAnPo_L8rrc7kLHMitvr0cfeu85r6HdjuSFpsjXeYNM1euEZmeHgMoeIQb2Dm98JBGXaB9AW47qhiMeF8lSzkcLFbH3YwECA1E-p38_kq83iHKSo-MSWNg0trIAp5VpIuAqFKToF0xf1JdSpJ90bbvGhbGK1N_AHcWjDPcbYuoekr1Zw6HvVR23SdqZXzU05qjilHS3roxFE4MK2fN6lnPaNjt1oKTCLRsPqMwhJP0lS_ZvZQOSnv9Fjrg9KTopcYnfCcfEidAPTM7Pg4-aSRVTog4CWNsrdcgfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dH54arFUwgilSqP5bApvjyXdKyvVMTkrLCMSFsYDYt1mSG_egdFa-F08Uf8OcOrTjht1Kxejzn08dRuxf9gVCoOFX5JiJn3IPKVWDhxE2cZlTAaGBNeu_i2Bs2pfIO9mxJx6fkNmxNWfQ1gIoTscHlTPQefilXQ-41P0rKyWUR95bD8rTlnaGCJkfpGgqlZghvggrKRE6hfxSojrCwekaDbL1PNhhZ36slceuo7njWsM0uX4r3J9KGv-4mHaES9w-QwgfxhvbWRrBAkMoSqQMEAwo7BS1APrzT30tcfeY9EaLerJFOOa8gHBsmO0QFygz9tJdRQFNtrfrIHSEmCK2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تغزیه های مفید برای هر عضو بدن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/670630" target="_blank">📅 21:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670629">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8bd931c1.mp4?token=kexdpdGB-3_AuZHIZCT1SQ_zjbDKxzjiYBg0r9T2NmyAJFnKKKvzKX9SAg7ZZMfavzfwH5VbiAFy8-IfEYUp0TiVq_sfU-vMWOrmjuSsie2CW4g_7Hg1toD6SqS4CzC0B4H30aRb_NHWxU-NDey2QZQWuasnjgZkKNrUTm__3l8njfGL52Xzce90zLOI7MYi1KbmRpZHMVAmV4SY_oQZEW01DqxnvAFqug9_sbUUS1btB1UdjEwEsRPvjaIx7VnGY6kQAgO_4L_9m9mu-DEvRRVIu1wxaxmuDBylxbo01ftgbQe5reAtHUbtFvWTgfwDxe22JOdrhfAo3iGgQMLYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8bd931c1.mp4?token=kexdpdGB-3_AuZHIZCT1SQ_zjbDKxzjiYBg0r9T2NmyAJFnKKKvzKX9SAg7ZZMfavzfwH5VbiAFy8-IfEYUp0TiVq_sfU-vMWOrmjuSsie2CW4g_7Hg1toD6SqS4CzC0B4H30aRb_NHWxU-NDey2QZQWuasnjgZkKNrUTm__3l8njfGL52Xzce90zLOI7MYi1KbmRpZHMVAmV4SY_oQZEW01DqxnvAFqug9_sbUUS1btB1UdjEwEsRPvjaIx7VnGY6kQAgO_4L_9m9mu-DEvRRVIu1wxaxmuDBylxbo01ftgbQe5reAtHUbtFvWTgfwDxe22JOdrhfAo3iGgQMLYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخباری از وقوع چند انفجار مجدد در عربستان
🔹
برخی منابع خبری گزارش دادند صدای چند انفجار در جده شنیده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/670629" target="_blank">📅 21:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670628">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfHe1-cUgCOW1N_u5fXb815vGYHqBJ3sYePRhFgCJidWY6suhuH4kC1tbthEq241akeC7f0tBTyO4bSAuijwaaJVKlJyeQRbgk-Y0dSrjGNyy6_W3wN7Irb0aTI3cRJS244bgp73uiRD5-29xbp4g6MfYckn6ffDk2gC11GV2ugrHj0Q4-rGpLm_GTfQHVbjea4xbg4G8zqKuuJ0VC4rt_Yyhgp6hBIcp3MPCP1KFBRjYWhddtRRDvnhMKnppOmKTrUSLKDlue3zmF4x6IMeY14tyN5uxr68fj2g_NVK4XAGtPwQD3_3kF_xf8_9QkQCPxBLD5u1PgoIcnwX8WzZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه عراقچی به ترامپ: ما منصف‌تر خواهیم بود!
🔹
رئیس‌جمهور آمریکا کاملاً درست می‌گوید؛ هرکسی که عبور امن و مطمئن کشتی‌های تجاری از تنگه هرمز را فراهم می‌کند، باید برای این خدمت خود پاداش دریافت کند.
🔹
ایران همیشه نگهبان تنگه بوده و برای همیشه نیز خواهد ماند.
🔹
البته ۲۰ درصد خیلی زیاد است؛ ما منصف خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/670628" target="_blank">📅 21:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670627">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سنتکام: ما اجرای محاصره دریایی علیه ایران را اواخر امروز آغاز خواهیم کرد   نیویورک تایمز به نقل از سخنگوی فرماندهی مرکزی ایالات متحده:
🔹
ما در حال کار بر روی جزئیات و هماهنگی برای اعمال مجدد محاصره دریایی علیه ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/670627" target="_blank">📅 21:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670626">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
عربستان تصویربرداری از اماکن هدف‌گیری شده را ممنوع کرد
🔹
وزارت کشور عربستان سعودی، پس از حمله موشکی یمن به خاک این کشور، هرگونه  تصویربرداری از اماکن هدف‌گیری شده را ممنوع اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/670626" target="_blank">📅 21:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670625">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بهای نفت برنت از ۸۱ دلار گذشت
🔹
بازارهای جهانی انرژی با تداوم تنش‌ها در منطقه، شاهد افزایش قیمت نفت بوده‌اند که منجر به ثبت رکوردی تازه در ماه‌های اخیر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/670625" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
انهدام دو فروند پهپاد لوکاس در بندعباس و لار
🔹
دقایقی قبل دو فروند پهپاد آمریکایی لوکاس در بندرعباس و لار توسط سامانه های نوین پدافند پیشرفته هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور، مورد اصابت و منهدم گردیدند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/670623" target="_blank">📅 21:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادارات بوشهر چهارشنبه تعطیل شدند
🔹
استانداری بوشهر اعلام کرد به‎‌دلیل گرمای هوا و حفظ پایداری شبکۀ برق تمامی ادارات این استان روز چهارشنبه ۲۴ تیرماه تعطیل هستند.
🔹
همچنین ساعت کاری ادارات در روز سه‌شنبه ۲۳ تیرماه تا ساعت ۱۱ خواهد بود.  #اخبار_بوشهر در فضای…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/670622" target="_blank">📅 21:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دادستان شهرستان دورود لرستان: فردی که اقدام به ارسال کلیپ  از محل برخورد پرتابه در دورود به شبکه اینترنشنال نموده بود، دستگیر شد
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/670621" target="_blank">📅 21:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i68W_7U2ZjT_hXshANSL2VQb5ftBe6t5hJnyXnu6p5dXtB5Hvb0rP5W5izRF7cYnh-fGzDl46_jwBDn7RF31xeqjP8Jq5cSLYaUSlW53lf1svXdcoEr-Awz2Y9z2COxCAzalhBO3kUexsUwNhXmMQ50vorrZ2rubejIcaoJhgW6895sL1eG3tXJBfO0_pHKxbWIibrjAI-ITHrD-OCyvkDMJXqBWN60MciaB-6dMae-gKiHimqXxcoqMKzX6cAolVv4ASvcxZUOT1JDCroa88e8RrD567ZL15eXVAu8Jr-9r41QjrHZPsLSmiGGS2QX7uhhe5k0uL0i-ZGTToKSMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/670617" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2e83436d.mp4?token=b7E9Gq8mJu1EPNr6u4F--9V9qzchw_ie4wVXzhGs7tN38SQE8EPZ3UFLgCxAaBC9rAg3VHFla6Zpbcc9UUTiA7XymG59tS6kF0Yg4CaZy82M5leWv5EN1urWaa1Qj8z0yuRLkhTUZPkqodJ2jfvjRzMuQLocmdaKrNy7eE37KM9HEvmX03boTI5zi-EcX5CRHvVNQizhENDFGT1t_0F25GCSMRKdfDzdI5KAX7Jar98qM6XtMzYdrbncMN6kKVksXw1uXLjycRKGgTqeBcBLLzZotggMlpzkYw9hIv0K2iYCZjAMBKuM8nJ4RV8b0EzYacMt45z6nsihO4PUlB98WBANVw8L55Ac5NQltyQ7EYRVzE9UlGqJ6UVzJ3ZnknhyLA2tYPC82cb5ZPg7rfMyC4-0OtOU5_NQKfNoDX2lE9N7XImS7Jvbd_zOoCnE3tzZeGyzHFf3YkCK3-wRKedcgnCXRl3aqZIcyr5ggEi9cv9j6HjSHLWroOI72DRLEXylBWdBRCEWc1btaxdsDIvGYqUyU-f-7tzy9WaKG4LuhvE6M3wahZuKXYUoCCQlxGaeVOuNiTtgOFXlY23cvHI_brr-DwrqtCEzI0GmbjPj6I1XdClsCU_aBPt1ByiTSqzCQRSfCHx9FAU2pyynSvczKUrcHpuFWZEBQ2k1Tbmkukk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2e83436d.mp4?token=b7E9Gq8mJu1EPNr6u4F--9V9qzchw_ie4wVXzhGs7tN38SQE8EPZ3UFLgCxAaBC9rAg3VHFla6Zpbcc9UUTiA7XymG59tS6kF0Yg4CaZy82M5leWv5EN1urWaa1Qj8z0yuRLkhTUZPkqodJ2jfvjRzMuQLocmdaKrNy7eE37KM9HEvmX03boTI5zi-EcX5CRHvVNQizhENDFGT1t_0F25GCSMRKdfDzdI5KAX7Jar98qM6XtMzYdrbncMN6kKVksXw1uXLjycRKGgTqeBcBLLzZotggMlpzkYw9hIv0K2iYCZjAMBKuM8nJ4RV8b0EzYacMt45z6nsihO4PUlB98WBANVw8L55Ac5NQltyQ7EYRVzE9UlGqJ6UVzJ3ZnknhyLA2tYPC82cb5ZPg7rfMyC4-0OtOU5_NQKfNoDX2lE9N7XImS7Jvbd_zOoCnE3tzZeGyzHFf3YkCK3-wRKedcgnCXRl3aqZIcyr5ggEi9cv9j6HjSHLWroOI72DRLEXylBWdBRCEWc1btaxdsDIvGYqUyU-f-7tzy9WaKG4LuhvE6M3wahZuKXYUoCCQlxGaeVOuNiTtgOFXlY23cvHI_brr-DwrqtCEzI0GmbjPj6I1XdClsCU_aBPt1ByiTSqzCQRSfCHx9FAU2pyynSvczKUrcHpuFWZEBQ2k1Tbmkukk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از ترکیه اومده ایران به عشق آقای شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/670616" target="_blank">📅 21:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در عربستان؛ فرودگاه ابها هدف قرار گرفت
🔹
منابع خبری از انفجارهایی در عربستان و حمله به فرودگاه ابها در عربستان خبر دادند. این منابع به توقف کامل پروازها در این فرودگاه اشاره کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/670615" target="_blank">📅 21:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
محکومیت حمله به فرودگاه بین‌المللی صنعا
🔹
اسماعیل بقائی سخنگوی وزارت امور خارجه، حمله به فرودگاه بین‌المللی صنعا را محکوم کرد و آن را نقض آشکار حقوق بین‌‌الملل و منشور ملل متحد و بی‌حرمتی به حاکمیت ملی و تمامیت سرزمینی یمن دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/670614" target="_blank">📅 20:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای نماینده مجلس در خصوص افزایش بیکاری: آموزش‌های نظری دانشگاه‌ها به آمار بیکاران بیشتر اضافه می‌کند
فضل‌الله رنجبر، عضو کمیسیون اجتماعی مجلس شورای اسلامی در
#گفتگو
با خبرفوری:
🔹
با وجود تعدیل نیرو در دوران جنگ، ادعای کاهش نرخ بیکاری قابل تأمل است و حتماً باید توسط مجلس مورد ارزیابی دقیق قرار بگیرد.
🔹
اگر تأمین اجتماعی به‌صورت مستند آمار بیمه‌شدگان اشتغال را اعلام کند قابل پذیرش است، چون بهترین سند برای ادعای کاهش بیکاری و ایجاد اشتغال، آمار جدید بیمه‌شدگان تأمین اجتماعی است.
🔹
آموزش‌هایی که به‌صورت نظری در دانشگاه‌ها می‌دهیم به آمار بیکاران ما بیشتر اضافه می‌کند؛ ما باید سراغ آموزش‌های کاربردی، به‌روز و مبتنی بر ایجاد اشتغال برویم و این آموزش‌ها را به سطوح مختلف جامعه برده و حتی رایگان کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/670613" target="_blank">📅 20:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حجت‌الاسلام شریفیان: هرگونه مذاکره بر سر خون شهدای میناب، تنگه هرمز و حزب‌الله لبنان مردود است و باید در برابر آن ایستاد
🔹
با نخستین شلیک گلوله در جنوب لبنان، باید معاهده را پایان‌یافته تلقی می‌کردیم/استمرار پایبندی در برابر خیانت، تفاوتی با همراهی با خائن ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/670612" target="_blank">📅 20:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
برخی منابع از اصابت یک موشک یمنی به پایگاه هوایی ملک خالد در نزدیکی شهر اَبهای عربستان خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/670611" target="_blank">📅 20:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
عربستان سعودی حمله به خاک خود را تایید کرد
🔹
ائتلاف به رهبری عربستان در یمن اعلام کرد که با موشک‌های بالستیکی که حوثی‌ها به سمت منطقه جنوبی شلیک کرده بودند، مقابله کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/670610" target="_blank">📅 20:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر عسیر سعودی
🔹
منابع خبری از شنیده شدن صدای انفجارهایی در شهر عسیر سعودی خبر می‌دهند.
🔹
شهر عسیر در جنوب عربستان و در نزدیکی مرزهای یمن قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/670609" target="_blank">📅 20:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf8nYHFgoes1GA3GBWfUVa2p44X5AU_G-LNvYdqG4yCxvx6Ud-Y98ibRsVvFI9NnfNT4nnr7W2zUH4eSO45V-OQjVrOGvIA3LZ4yeVV3wayl3JZHLYS34LAHyAZGRsM5cQga4bs2AKLTU2FU3Z0JcsYekeGOhosSdTk98qENDgf7Z4kBieFUAbgvaD8Hkjo5H4JIcjq_mH-G0XG__4IzAzV7JDQ_bPn3DmX2XAQ6AepA6hGR4RRO6W_-fc7bqTK2piBazNAvcn83ERPt01Noufd7HxdKnd_ExDRjq2hayqi9Uq9INETkztWEjaujs8FPjpwm84Lcag95KN1iuxTnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/670608" target="_blank">📅 20:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5629bb58a7.mp4?token=MP8YSkr37-97U_eMfHmQ8kos9FQfWETTzQkZVivpv1IZjaoMBH_YA7KaG1jUiyUz9qE4AOXXw6sy03Z9dz_gyIKBL0jXioV2va69zp6zr74DRWLqKJ5mr5bo1Fpohsc6NoGXDz5DshGZvt60HwkxSWn5H5OBCrfDYwOmQW14p1Qrn5MZqMbipi-Uy_co5YBed5l-iDomFuZBOYbF8pkzzengHyHnKgTm7xe-Z7nFSIn924QoOHtKsV3JL4aFAkbYANrOfiD8StGQE3retAVNU410aiweeXXRXAy2Nvhzl9naRSZ0RtkuRcPqS2n6mEdhHzipQPfZ9HbGiwS2PF-tPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5629bb58a7.mp4?token=MP8YSkr37-97U_eMfHmQ8kos9FQfWETTzQkZVivpv1IZjaoMBH_YA7KaG1jUiyUz9qE4AOXXw6sy03Z9dz_gyIKBL0jXioV2va69zp6zr74DRWLqKJ5mr5bo1Fpohsc6NoGXDz5DshGZvt60HwkxSWn5H5OBCrfDYwOmQW14p1Qrn5MZqMbipi-Uy_co5YBed5l-iDomFuZBOYbF8pkzzengHyHnKgTm7xe-Z7nFSIn924QoOHtKsV3JL4aFAkbYANrOfiD8StGQE3retAVNU410aiweeXXRXAy2Nvhzl9naRSZ0RtkuRcPqS2n6mEdhHzipQPfZ9HbGiwS2PF-tPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجله ترامپ برای مهار قیمت نفت باعث شد تفاهم‌نامه‌ ایران با شتاب و مبهم منعقد شود
دنی سیترینوویچ، رئیس سابق میز ایران در اداره اطلاعات نظامی ارتش اسرائیل:
🔹
این تفاهم‌نامه‌ای بود که آمریکا با شتاب به سمت آن رفت، زیرا رئیس‌جمهور ترامپ از افزایش چشمگیر قیمت نفت هراس داشت. به‌همین دلیل، همه چیز را به‌گونه‌ای شتاب‌زده و با ابهام‌های فراوان بستند، به‌گونه‌ای که هر طرف برداشت متفاوتی از آن دارد. از منظر ایران نیز آشکار بود که آن‌ها هیچ‌گونه عقب‌نشینی از کنترل بر تنگه‌ها را نمی‌پذیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/670606" target="_blank">📅 20:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
درپی حمله یمن، تمامی پروازها در فرودگاه اَبهای عربستان به‌طور کامل متوقف شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670605" target="_blank">📅 20:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thelittleprince.pdf</div>
  <div class="tg-doc-extra">1.2 MB</div>
</div>
<a href="https://t.me/akhbarefori/670604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل پی‌دی‌اف کتاب شازده کوچولو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/670604" target="_blank">📅 20:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670602">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAtkLMkk-5nQyqo1mZ-ApsGBj-M4nkZeCmtcXXVvY5G5n575DnWCz8LwFBi61SVFNWSmJ7_4PbUCY58h6q-FDZdMGOX3NfXVM4Ez-j6RYvvbbY6dwXTsxHH62-wziegyJSQyOr7YbU3thj2FQKqrWZZdB9KhuF93F-N17si_pEdbO1-IUTHBJYzrsatrCjjhZQRn0pn2IjDYxNZLlzzSUHkDmsA9eLPffzwPSWLPaPnDSB7BMUSPKTmbTVk5VUeFwVI-6429SbHfFi11n1rywgYUVDuYeTEGj6VPB2JVNthrwau0uOfIsiRqTSWyaMqjmabykZUJuGd9j0aSpeqJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hguz70MX0mdYpPvcEX1-gTErkJYbFe_l7MXyn9gr2HDSXG-fVLyJyBaZZ-SvnqbXd7qj37OHRHBdWV7vKRt5oYVMTeTCrHqEwLC9D6PeIPt9SDnZWv5f5Ft95JtVFONyIRDlz24Xf6YL1FT1ExdAmvr0e0nanhH35_9gOBeIekZWAJZzraIuZPw4YT6A7q7zNqsHKZK30NJaip5v4C537J_WTPMJTsyxTAxskgwPrDSKf_Z7PZEQ0JmrB0rCw5Bfmc4K5rERNIV319Hb0FtwqHed-oeOc_Ai5j7A5rcJJG1ElqIqRTkephY8WgXq92wRUFB_OvJsijDh18zfEbrecA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کتابی که نگاه بسیاری را در جهان درباره زندگی برای همیشه عوض کرد
🔹
«شازده کوچولو» فقط یک داستان کودکانه نیست؛ سفری شاعرانه به دنیای عشق، دوستی، تنهایی و معنای واقعی زندگی است. آنتوان دوسنت‌اگزوپری با زبانی ساده؛ اما عمیق، یادمان می‌آورد که آدم‌بزرگ‌ها چگونه در میان اعداد، پول و ظاهر، مهم‌ترین حقیقت را فراموش می‌کنند: آنچه ارزشمند است، با چشم دیده نمی‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670602" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شلیک ۶ موشک یمنی به سوی عربستان سعودی
🔹
منابع خبری از شلیک دست‌کم ۶ موشک از یمن به سوی فرودگاه ابهای عربستان سعودی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/670601" target="_blank">📅 20:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مقام یمنی: زیرساخت‌های عربستان را هدف قرار خواهیم داد
🔹
محمد البخيتی عضو دفتر سیاسی جنبش انصارالله یمن شامگاه امروز دوشنبه تأکید کرد که این کشور قطعا پاسخ تجاوز عربستان سعودی به فرودگاه صنعا را خواهد داد.
🔹
البخیتی با اشاره به اینکه این پاسخ «بسیار قدرتمند…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670600" target="_blank">📅 20:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادارات هرمزگان در روز سه‌شنبه و چهارشنبه تعطیل شد
🔹
معاون توسعه مدیریت و منابع استانداری هرمزگان از تعطیلی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه خبر داد.
🔹
امتحانات نهایی دانش آموزان و دانشجویان…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/670599" target="_blank">📅 20:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مقام ایرانی: ترامپ باید ترتیبات ما در تنگه هرمز را بپذیرد
🔹
شبکه المیادین به نقل از یک مقام ارشد امنیتی ایران گزارش داد که رئیس‌جمهور آمریکا، دونالد ترامپ، فراموش کرده آبراه تنگه هرمز، طی هزاران سال متعلق به ایران بوده؛ یعنی حتی قبل از اینکه آمریکا وجود داشته باشد.
🔹
ترامپ متوهم،‌ مدعی شده آمریکا ۵۰ سال است که از تنگه هرمز محافظت می‌کند.
🔹
دولت آمریکا هنوز درک نکرده که امنیت و اداره تنگه هرمز را اراده حاکمیت ایران تعیین می‌کند، نه توئیت‌ها و کشتی‌های جنگی آمریکا.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/670598" target="_blank">📅 20:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4534901185.mp4?token=u8gSJCs64CZG5WHb0hE5DQOyEQOz5XOaxnE2W4Hfq31UMnTq-4wDZXRNnYxDFID_123E4jiqCKets7v5WRDNlZY3s6hrGK5YJAZAFqNYoxv_oT5VSpYL8BX_eiEI1anyyH4W1sFyeGCQSbtggROw5P4_xiS2zTtqjIsCZDooKNeSTxOxO4Khyi1m9YRqFk6L7tjv6sfTBlkwOVSySH7FlAjC0F99UY-tT7ab7WUPn-KwqAdyRvkxUjzCJCZ1DDyh92jn4WJ0kpzpdXBkVEWluzzAByhxCeSiIbw7nVtIum5ZmjxCJ2YBdw0Bq9hfHA9wlqaKZ7Vj6Xrd1QyYt7llig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4534901185.mp4?token=u8gSJCs64CZG5WHb0hE5DQOyEQOz5XOaxnE2W4Hfq31UMnTq-4wDZXRNnYxDFID_123E4jiqCKets7v5WRDNlZY3s6hrGK5YJAZAFqNYoxv_oT5VSpYL8BX_eiEI1anyyH4W1sFyeGCQSbtggROw5P4_xiS2zTtqjIsCZDooKNeSTxOxO4Khyi1m9YRqFk6L7tjv6sfTBlkwOVSySH7FlAjC0F99UY-tT7ab7WUPn-KwqAdyRvkxUjzCJCZ1DDyh92jn4WJ0kpzpdXBkVEWluzzAByhxCeSiIbw7nVtIum5ZmjxCJ2YBdw0Bq9hfHA9wlqaKZ7Vj6Xrd1QyYt7llig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی به ضخامت و اندازه کارت بانکی که برای کارهای روزمره استفاده میشه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/670597" target="_blank">📅 20:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بازداشت یک فرد مسلح در نزدیکی ساختمان کنگره آمریکا
🔹
پلیس کنگره آمریکا از بازداشت فردی خبر داد که با یک سلاح گرم در بیرون ساختمان کنگره حضور داشت.
🔹
نیروهای امنیتی به کارکنان کنگره و سایر پرسنل دستور دادند تا اطلاع ثانوی از تردد در این منطقه خودداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/670596" target="_blank">📅 20:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670595">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
روسیه در سیریک نیروگاه می‌سازد
🔹
در این دیدار پروژۀ اتصال شبکۀ برق ایران و روسیه مورد بررسی قرار گرفت تا  درصورت فراهم‌بودن شرایط، امکان انتقال ظرفیت محدودی از برق جنوب روسیه در فصل تابستان، فراهم شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/670595" target="_blank">📅 20:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670594">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مقام یمنی: زیرساخت‌های عربستان را هدف قرار خواهیم داد
🔹
محمد البخيتی عضو دفتر سیاسی جنبش انصارالله یمن شامگاه امروز دوشنبه تأکید کرد که این کشور قطعا پاسخ تجاوز عربستان سعودی به فرودگاه صنعا را خواهد داد.
🔹
البخیتی با اشاره به اینکه این پاسخ «بسیار قدرتمند و درآور» خواهد بود، خبر داد که نیروهای مسلح یمن، زیرساخت‌های عربستان را هدف قرار خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/670594" target="_blank">📅 20:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670593">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxMnmufH3ZeyIJE4BMfEcb4SJ05I4lBB5QclPZGtHFd5oWXhtQ-mm0b8h_kkyHRRhQbN8Qsho--F9hm3wmdqFY6QVfW9EutDbHb1O_Krr3NE8MXzbzQNoZK3Indr_SgtTUnveAZ1QQzgPu8fKUS0zh_kgcXBb1QBSMSaPFFmNr-H1QCW3_YzzM1qgLbVlVniKfTQ4XKole9BgshjepJu1__AIUH9q9UXkL3bEsezuHnzL7gqPhnGt2iOUQS0ebazRvEwb9_r3jL9np7nbuIf650Ti5U3YgFofhsR_VHJehONYARAhu7KzhkfZqErfIa8Iz1-KvZiWP7R857J-tF0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ها خبر نمی‌کنه... فقط وقتی می‌رسه که دیر شده
💎
اجرت از ۳٪
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
🏦
خرید طلا با هر بودجه از طریق بانک طلا
🔄
تعویض طلای سالم با عیار ۷۵۰
✨
بدون مالیات ارزش افزوده
📲
کانال ما
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/670593" target="_blank">📅 20:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670592">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
اکسیوس: یک منبع ارشد در خلیج فارس گفت که آمریکا موضوع احتمال دریافت عوارض برای تأمین امنیت تنگه هرمز را به متحدان خود در منطقه مطرح نکرده بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/670592" target="_blank">📅 19:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh05-3H42ZST4tYzOLm9-6CFCGvqgk-3Hvb2ylN7BCZQZuwweQAqV7L3bDtVOYf1do_CFR3CvekcxF7zcjzfXZ8fRtQb_ZW1Gf37VNv3VPoTrVrx4JrUe4VLVocmAJEO_qc_Tmhf9HREhpuL_LKJbZdaovTZYY-SHJGwtd6LExoWRzxZZ2vjh7f4pFvXI1qERRTNZmi_i_zu8DkBfNvECq3Vuzw95BopHI9-7iAWsiby1IkZKdKhltP1lPRUC2gu7w8kS8aODwy45Pi9KQ8tfFiWPH2aNjfFak1uct6d462KPKOxjmACJ-HPkTF8BPIIY7GNkvNDQoU3v_Uvt8zpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر آیت الله سید مصطفی خامنه‌ای فرزند امام شهید سید علی خامنه‌ای در حال زیارت مزار حضرت ابالفضل العباس(ع) در جریان تشییع رهبر شهید انقلاب اسلامی در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/670591" target="_blank">📅 19:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مصادره ۳۵۸ کیلوگرم طلای غیرقانونی در اقلیم کردستان عراق
مسرور بارزانی، نخست‌وزیر اقلیم کردستان عراق:
🔹
بازداشت متهمان پرونده‌های فساد و تحویل آن‌ها به دولت مرکزی بغداد انجام شد.
🔹
دولت اقلیم کردستان همکاری خود را با دولت مرکزی برای مبارزه با فساد، جلوگیری از هدررفت منابع عمومی و تقویت حاکمیت قانون ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/670590" target="_blank">📅 19:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inBHJ-VV3k8FguImCDJwlzaYu7c8bikgZPgRUOPiAq_3X3VUel60VwtaOJyK7isFeScHK3CtIFEwWeAGpU_mGJOPxL9WFlfJGYEBC0ooB3TNKRSWvU1RHnY1pL8F2C5qXojKj3cMrspCPo2e2NEuCT1uyZahXHxvvQQPNgIRyEPB6br9P5hGtNKlbBiMpZHOcSLc7fxEGuJI9B75H6NcbkHH23NVYg5QKgedC8Hi_fosrX3c3zRjJjmv7i-VmkHbl8S_juRDLhNvVTenFfm0oS78KjCbcCMJ7FuH7F6LMmNjNjxvjQQrMXOIlFAZNvqZWIMi54IeoJDGq6maYgTt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتقاد ۶۸ درصد مردم ایران به سرمایه‌گذاری در بازار طلا
🔹
نتایج مرکز افکارسنجی ملت نشان می‌دهد اعتماد سرمایه‌گذاران همچنان به بازار طلا بالاست.
🔹
۶۸.۴ درصد مردم، سکه، طلا و صندوق‌های طلا را سودآورترین بازار در یک سال گذشته می‌دانند و بیشترین بازدهی را برای سه ماه و یک سال آینده نیز در همین بازار پیش‌بینی می‌کنند.
🔹
در مقابل، ۱۳.۶ درصد پیش‌بینی می‌کنند بازار ارز و زمین و مسکن در یک سال آینده بازدهی بیشتری داشته باشند. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/670589" target="_blank">📅 19:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وزارت راه و شهرسازی؛ زخمی سرفراز روزهای مقاومت
🔹
در بررسی پدیدارشناسانه و واکاوی هندسه‌ درگیری در نبردهای اخیر، اعم از جنگ تحمیلی دوازده‌ روزه و معرکه‌ رمضان، تقابل جبهه‌ جانیان استکبار با نظام جمهوری اسلامی ایران از ساحت نظامی و میدانی صرف فراتر رفته و لایه‌ های بنیادین حیات ملی را هدف قرار داده است. اگر با دقت نظر به راهبرد خصم زبون اعم از توحش عریان رژیم صهیونیستی و جنایات ایالات متحده بنگریم، در می‌ یابیم که آنها با درک ناتوانی در مصاف اراده‌ ها، عقلانیت شیطانی خویش را بر ضربه به زیرساختهای حیاتی و شریانهای حرکتی و ادراکی کشور متمرکز ساخته اند.
🔹
در اندیشه‌ راهبردی، مقوله‌ راه و زیرساخت حمل و نقل، صرفا مجموعه‌ ای از سازه‌ های عمرانی یا ابزارهای ترابری و سامانه های نرم افزاری مرتبط نیست؛ بلکه دالّ مرکزی انتظام ملی و شبکه‌ عصبی یک تمدن است. تهاجم ددمنشانه به بنادر، فرودگاه‌ ها، خطوط و ایستگاه‌ های راه‌ آهن، پلهای مواصلاتی، ناوگان حمل‌ و نقل هوایی، جاده‌ ای و دریایی و از سوی دیگر، ضربه به مجاری پایش، ادراک و داده‌ پردازی کشور نظیر ایستگاه‌ های هواشناسی و رادارها، نشان از یک طراحی پیچیده برای انقطاع پیوندهای حیاتی این بنیان مرصوص دارد. دشمن در خیال خام خود بر آن است تا با قطع این شریانها، تاب‌ آوری سیستماتیک کشور را دچار فروپاشی کند.
🔹
اما در همین نقطه‌ تلاقی بحران است که مفهوم زمخت زیرساخت حیاتی، از یک اصطلاح تکنوکراتیک و مهندسی، به یک مقوله‌ وجودی و جهادی استحاله می‌ یابد. وزارت راه و شهرسازی در این آوردگاه نفس‌ گیر، در قامت یک قرارگاه عملیاتی خط‌شکن ظاهر شده است. کارکنان، مدیران، مهندسان و متخصصان این مجموعه، با تلفیقی از تخصص فنی و تعهد ایمانی، نشان دادند که ماشین‌ آلات، سازه‌ ها، تجهیزات و فرآیندها زمانی که با جوهره‌ مقاومت درآمیزند، شکست‌ ناپذیر خواهند بود.
🔹
تقدیم چندین شهید والامقام در این مسیر،
گواهی صادق
بر این مدعا است که صیانت از کیان اسلامی، محدود به سنگرهای مرزی نیست؛ بلکه هر رادار، هر لوکوموتیو، هر عرشه‌ کشتی، هر پل استراتژیک، هر خط ریلی و ... خود یک سنگر مقاومت است. خون پاک این عزیزان، به مثابه ملاتی معنوی، استحکام این زیرساختها را در عالم معنا تضمین کرد و نشان داد که توسعه و امنیت، دو روی سکه‌ استقامت ملی هستند.
🔹
امروز، وزارت راه و شهرسازی را باید زخمی سرفراز این نبرد همه‌ جانبه دانست.
جراحاتی که بر پیکره‌ راه‌ ها، بنادر، تاسیسات و ناوگان ما وارد آمد، نشانه‌ هایی از ضعف نیست؛ بلکه مدالهای افتخار و اسناد زنده‌ پایداری ملتی است که در برابر طوفان کینه‌ ها خم به ابرو نیاورد.
🔹
این پیکره‌ زخمی، با تکیه بر ظرفیت های درونی و عقلانیت انقلابی، نه تنها به‌ سرعت بازسازی و احیا می شود، بلکه با صلابتی افزون‌ تر، مسیر پیشرفت ایران اسلامی را ذیل عنایات امام عصر ارواحنا فداه و نایبش امام سید مجتبی حسینی خامنه ای حفظه الله هموارتر از پیش خواهد ساخت؛ که به مصداق سنت الهی، هر بنایی که بر پایه‌ تقوا و ایثار بنا شود، از گزند تندباد حوادث مصون خواهد ماند.
راهبرد| افشین فیروزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/670588" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4JL7GSAAF8b1hn_jL3qAA1a1BA6qWXTsEBY3IpqOZ8M-hiCupD_3qIYmbOWiQH16RipuMtzxLZANJ0aLcMzmv9UtLOHxxkipnweY93c0pAhVsH4FiW1Sb1IRhC2KYnz4d8fD5dgbVOtekb2pBch-dKR82Yr18V8YMBCh_nAF_9gxWqw_vPYcLaU1yFWyT097-yC_Ehbguuth3CM8lfruQPrcwybV53fwitthda13GN2HWkpjE1yiRn0Y6fww_cCYf8OlIVMrAqbg9P6iJ10INm5gf3qru-qAJoxip4_2LlspvPJTVkNUZv62_L8ULdjS3QjzuxF8e8oE3ou3BTXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمانه بر سر جنگ است
🔹
نقض آشکار آتش‌بس و پایبند نبودن آمریکا به تعهدات و جنگ‌افروزی‌های اخیر ایالات متحده نشان می‌دهد که مسیر تنش همچنان ادامه دارد و چشم‌انداز صلح بیش از گذشته با ابهام روبه‌رو شده است. بی‌تردید، صلح عادلانه بهترین راه‌حل برای همه طرف‌هاست، اما صلحی که بر پایه فشار، تهدید و حمله نظامی شکل بگیرد، پایدار نخواهد بود. در شرایطی که تعرض به خاک ایران و فشارهای راهبردی ادامه دارد، دفاع از امنیت، حاکمیت و تمامیت ارضی کشور به یک ضرورت تبدیل می‌شود. در این میان، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران است. گذرگاهی که نقش تعیین‌کننده‌ای در قدرت بازدارندگی و توان چانه‌زنی کشور دارد. حفظ جایگاه راهبردی هرمز، تنها حفاظت از یک آبراه نیست، بلکه صیانت از اقتدار، امنیت و منافع ملی ایران در معادلات منطقه‌ای و بین‌المللی است که باید برای آن جنگید.
🔹
هشتصدوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/670587" target="_blank">📅 19:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
محکومیت کارمند آمریکایی به اتهام صادرات قطعات الکترونیکی به ایران
آسوشیتدپرس:
🔹
یک کارمند سابق شرکت «آنالوگ دیوایسز» به اتهام دور زدن تحریم‌ها و صادرات غیرقانونی قطعات به ایران مجرم شناخته شد.
🔹
وی که دسامبر ۲۰۲۴ بازداشت شده بود، به همکاری با یک شرکت ایرانی متهم است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/670586" target="_blank">📅 19:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نوین، نماینده مجلس: بدعهدی‌های ترامپ، ضرورت خونخواهی را بیش از پیش آشکار کرده است
علیرضا نوین، نماینده مجلس:
🔹
مقام معظم رهبری در پیام‌های خود بر خونخواهی و عدم سازش تأکید کرده و فرمودند که میدان‌داری تا زمان قصاص ادامه خواهد داشت.
🔹
بدعهدی‌های ترامپ در سه سال اخیر و شهادت رهبر انقلاب ضرورت خونخواهی را بیش از پیش آشکار کرده و قرآن نیز پیشوایان کفر و پیمان‌شکنان را به جنگ دعوت می‌کند و این وظیفه‌ای شرعی و قانونی است؛ راهکار اساسی پاسخ نظامی قاطع و سیلی سخت به آمریکا است که وصیت امام شهیدمان بود.
🔹
وحدت ملی و جلوگیری از نفوذ دشمن از اولویت‌های اصلی است و مسئولین باید با الگو گیری از روحیه جهادی شهدا عملاً نشان دهند که خونخواهی را جدی گرفته‌اند و با هرگونه اقدام علیه دشمن تکلیف جنگ را روشن کنند.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/670585" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsrVMlOmH0UnRlweli5wymIBO-yl7xjVr83cFKlZQOv28kectT7L3c-gYQ8GjwJm2ygOIerJb-RNRBHt5CNZXOFuREvvNbaU7mFe7tUG_JfN6gZ0JjTuIcFgTtGlLlCuzz12tvvb0I06zqxUdNjtcmkFGl9CtjXN285Df9A8C0Ez17D7iby3pMs7TK3ZTeBuHhJcuuITG-mWIxNR_SVac25aH8FBTks7aTzbHncw-Kn0SCL0WpRere3J0_GR-6aagkslhXmpUuCOkqYG650VsSYHdQAFcLY0-92KCqKTfNlJ86wolC5PQoc_KiatLXjLkP207FpMNA_ZEKxvybp5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنک‌ترین اماکن ایران برای فرار از گرمای تابستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/670584" target="_blank">📅 19:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادارات هرمزگان در روز سه‌شنبه و چهارشنبه تعطیل شد
🔹
معاون توسعه مدیریت و منابع استانداری هرمزگان از تعطیلی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه خبر داد.
🔹
امتحانات نهایی دانش آموزان و دانشجویان طبق برنامه از پیش تعیین شده برگزار خواهد شد و تعطیلی شامل آن‌ها نمی‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/670583" target="_blank">📅 19:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/670582" target="_blank">📅 19:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWCqTqqjCIc0h2hasd8FICkkZ3x3-yYNbbVrl3eqs_EUA7pUc3Cv1JNd-6jcBKaAAvn2QZOfeoDp5GHSC-6qk9SmmgR_O7ZpoSqDSD97sZsTOHLvbjnymLKc7f1fVSpFbi-VmwK3K8wsY2SCiBMpINlsgcKaR-H-PvuGmght-WO5MlwNxrBPIP-mhA2AwKcQm5CjhYLgaHWo-obzXl1ct6YjYYrRA_qK9XPBfdwR4svsdFDQlvsUQCwxrLFKwDnfrBvSj-2rSorJzkmAdTEFx6bKdixKfO_WGxLiBTXe6-my_e_xNjCGkJ_L3jElGleE_4YXes89S0_j-Vab5Oy-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین بیشتر از کل جهان پنل خورشیدی اضافه کرد!
🔹
در سال ۲۰۲۵، چین ۳۳۶ تراوات ساعت به تولید انرژی خورشیدی جدید خود اضافه کرد که از مجموع تولید برق سایر نقاط جهان بیشتر بوده است.
🔹
این کشور ۵۳% از کل افزایش ظرفیت‌های خورشیدی جهان را به خود اختصاص داده است.
🔹
برای درک بهتر این مقیاس، باید بدانید که افزایش ظرفیت پنل‌های خورشیدی چین در یک سال، بیشتر از کل برق مصرفی بریتانیا (۳۲۲ تراوات ساعت) بوده است.
🔹
انرژی خورشیدی در سال ۲۰۲۵، ۷۵ درصد از افزایش تقاضای جهانی برق را تأمین کرد.
@amarfact</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/670581" target="_blank">📅 19:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اخلاقی‌امیری: استیضاح وزیر نیرو، با امضای نمایندگان همچنان در نوبت طرح در صحن باقی مانده است
حسن‌علی اخلاقی امیری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در ایام جنگ، مشکل کمی در مدیریت برق داشتیم، اما در دو سه هفته اخیر با گرمای هوا قطعی برق بدون اطلاع قبلی در برخی شهرها رخ داده که جای نگرانی دارد.
🔹
دولت سال گذشته با صرف بودجه حدود ۲۰ میلیارد دلاری پنل‌های خورشیدی وارد کرد تا امسال مشکل قطعی برق نداشته باشیم و انتظار می‌رفت قطعی‌ها با برنامه‌ریزی و اطلاع‌رسانی مناسب باشد که این اتفاق نیفتاد.
🔹
استیضاح وزیر نیرو مربوط به سال گذشته است و با امضای نمایندگان همچنان در نوبت طرح در صحن علنی باقی مانده و با شروع جلسات مجلس احتمال استیضاح این وزیر وجود دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/670580" target="_blank">📅 19:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-text">🎞
|
#تماشا_کنید
❇️
بانک توسعه صادرات ایران، در سی‌وپنجمین سال فعالیت خود،با تمام توان و قدرت در مسیر حمایت مالی از تولیدملی ، توسعه تجارت خارجی و شکوفایی اقتصاد ایران است.
💢
۱۹ تیرماه سالگرد تأسیس بانک توسعه صادرات ایران گرامی‌باد
🟢
سایت
|
تلگرام
|
بله
|
روبیکا
|
اینستاگرام
|
آپارات</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/670579" target="_blank">📅 19:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Fj8P2c_FqURNuhaxG8qpku00ogTJsx7FpOH5YSruNqmADkiRveXZgYmwyLxgQirOovBba4X-rRCu2ECde4pY2R-VH9mqx11GOGhoXDudr7BKuRwAA2KCMsLcZkY2WuaOX6shYJk7seXVN-cNR3Jz1iQWBsaCuBH_fEPws-kinDvnxIHM6HDGyRfglal_zsPazARIAy79__fiFY6qbkDSOxTBmPjShp9KqflgQVKs8EGJo0dHpw5f3Mx6T8ij71Oz5_l0CaW6r4m4sNgPy0spxTAs9Wy94E0HLXDpSMN9ee4ktgAMq4u7ekaM8Pdwfcz36WLuDgskSF_2NuL-6qHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/670578" target="_blank">📅 19:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYfJenGfBpj5sG4OXuvWUy-xSUDc-JGcJpkrzYYqI_Aq4u3O9i8IrrNJSffkeJmfKNJTMF75JUkP7ycDWKHrGqt8hIySlyK1FTwc0hmSzZVdj8x8-HwMdn3IXRhL6_lUHEXZpaDZ3ZqbtsWchvap2Y1cvn0FGOyPFf6w_ArQdoL5pfWrORSm8-KpVZ0XvhgEdmcvOeWjtAIf6IS40kNtvdlHNBBwuN8cgtt5eHj1oQ0C42aGGkVQ9lDUQxFtkxw8apuuojdMgtHtTamAZvUoPPu2mLCSb0ysAZlcML_cgXcU5lYLTEj_k1cQL0Lk3GAmMLJiRtIPh_0oIUD3m7RhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک‌زرد: آمریکا حامی تنگه هرمز خواهد بود، اما ۲۰ درصد از تمامی محموله‌های ترانزیتی را دریافت می‌کند/ خبرفوری  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/670577" target="_blank">📅 18:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHLsToBrbgoxCK_bMp1zioKK7Y4_-ZNt0kKlsDx4U_h6_tU1kG6il0uwh8HRQ4P0_hAvQR5Mrvf-N6IhiiScLcaA1OIus8unmik3m4ddBCTEjGNAjLLq4Pl8tv3vCxffGWXwCDlXyN_E-3KwrUU1_DxmhEsBZX6jfsS6hYAphLRWjNcZj4u9AVwtfz866xQNOWYV7Ack0IuFj_obwCB8e0NQkktFlNpuinusB_fm_BES8iIyj0DTIyWR_aSiIhk6MyRRaQSMN8Pt6DBIWUDVtcC-uCU7X6n6glEx00sJlKtv4QIUxWIFgSL9jCJkuCYbf_NhQTZDrT4fxCVVL3Z-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل دولت ترامپ با دیوان بین‌المللی کیفری؛ تلاش برای تضعیف یا انحلال دادگاه
🔹
دولت ترامپ اعلام کرده است که در پی تضعیف یا انحلال دیوان بین‌المللی کیفری است.
🔹
مارکو روبیو با دفاع از این رویکرد، استدلال می‌کند که این دادگاه با تهدید حاکمیت ایالات متحده، زمینه را برای پیگرد قانونی مقامات آمریکایی فراهم می‌آورد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/670576" target="_blank">📅 18:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
افزایش تولید نفت ایران در گزارش جدید اوپک
🔹
گزارش ماهانه اوپک نشان می‌دهد تولید نفت ایران در ماه گذشته میلادی به ۲.۴۴۱ میلیون بشکه در روز افزایش یافته است. در همین بازه زمانی، قیمت نفت سنگین ایران با ۲۴.۶۲ دلار کاهش نسبت به ماه قبل، به ۹۰.۷۷ دلار در هر بشکه رسید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/670575" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
طرح جدید ترامپ؛ ۱۵ دلار بر هر بشکه نفت در تنگه هرمز   خاویر بلاس، ستون‌نویس بلومبرگ:
🔹
ترامپ از بازگرداندن محاصره دریایی علیه ایران خبر داده است؛ طبق این گزارش، واشنگتن قصد دارد برای تضمین باز ماندن تنگه هرمز، عوارضی ۲۰ درصدی از تمام محموله‌های عبوری دریافت…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670574" target="_blank">📅 18:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شهادت ۳ رزمنده در حملهٔ هوایی به آبادان
🔹
در پی حملهٔ هوایی دشمن به شهرستان آبادان در روز دوشنبه ۲۲ تیرماه، شهیدان ایرج سردارپور، اصغر سردارپور، علی تاجبخش برای دفاع از کیان نظام مقدس جمهوری اسلامی ایران به فیض عظمای شهادت نائل آمدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670573" target="_blank">📅 18:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اظهارات متوهمانه ترامپ در مصاحبه با فاکس نیوز: احتمال ۹۰ درصدی وجود دارد که رهبر جدید ایران دیگر در قید حیات نباشد/ صابرین‌نیوز
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670572" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dclBZN0wNMiYr21F6AynRHzTjAEvSfhFweNRbpHg_gEF09-tuODWsouQYVX8I5vwIomzPAVq7k6gzMS2I6rjoRtBce6JGA14o08P_KJJfNLXqxtKq8-C_T2S5rrJw0d8645bsZfbg_Es8u3H98Kl1kMYwKU0aCPvZ9FX2mWPkN299y1jBeYgyfEZ1l6YoBfNMyDtkEfdFjQqAuUoLdFt08CyHivfNQE5AoQfuRQXTonO8bUwWstNxE3vdxTNUf06Jwp7xMuFUeg0poQ5RLFWSde2N1Z3ibSJPLmsUz4VqQns0LseBSaEVZvT7kd8TSmyD1iLOa6WBAtyeoE5mlx3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهاءالدین خرمشاهی، مرد نام‌آشنا ترجمه‌های قرآن را بیشتر بشناسید!
🔹
بهاءالدین خرمشاهی فقط یک نویسنده نیست؛ او از برجسته‌ترین حافظ‌پژوهان و قرآن‌پژوهان معاصر ایران است. پزشکی را رها کرد تا تمام عمرش را وقف ادبیات فارسی کند. حاصل این انتخاب، ده‌ها کتاب، ترجمه‌ای…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670571" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670570">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr4Bs3x49S91zn160QVNY8S8o-kZZGShfFTavAnnuIfKzxQ18FZI2B0uMGmupLh0JHFjHZ9PlQtmzNs6pxLOyvZlBGGrci515i5kC_GF089FLlcdnk30qAZMZvKtacmg9ZTA8BFQnLXREjO6INIqWtw6zcChh6Uqn9HciP5e7Pv1ZRp3cFJ8XZtRmCQnVhpYHUtOXByHOdWaW0wAH-Lq98Hzd2AdAeLX8pAVSVtfxDpKAIA7lpSlmoHzvVnx0IiKaTUl9fFSm0Tqz5HBQHVZH8hQEDzQiX3GS-4mGCXmnYeS6UBkjB6acrxSNzb7LlPuUKuaNCyWSPU-M4caU6RYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات مخفی اسرائیل برای جذب محمود احمدی‌نژاد | طرحی که شکست خورد!
🔹
بر اساس گزارشی از نیویورک‌تایمز، اسرائیل طی سال‌های اخیر تلاش محرمانه‌ای را برای نزدیک شدن به محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، آغاز کرده بود؛ تلاشی که هدف نهایی آن، تبدیل او به یک مهره اطلاعاتی و در نهایت استفاده از او در سناریوی تغییر حکومت در تهران عنوان شده است.
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230082</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/670570" target="_blank">📅 18:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای خوک‌زرد: آمریکا حامی تنگه هرمز خواهد بود، اما ۲۰ درصد از تمامی محموله‌های ترانزیتی را دریافت می‌کند/ خبرفوری  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/670569" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHjxs9OPKuxY1pRNXHXbqF0CdzqSr8xCJApWJwTUDx7nCVLdqSkWnY2aeY8EOb8oqjMzbsF_PnRzrYNWl2m2KVq4LQl39vgpCoNDbGzgMBaxFOaiHmuGyeY-kkrpZi-wmiG3c_jgYA-K70YZWUblpWoerUryT-oAwtFPfInIkCk_ml6Wq5SfMRiTucjySLr6umK7_I6OmSOCWHSTeNs6N_8R8V8vta0sGiK7q14lDb6dk-XdtWlN1MZOn5cNCIWs2bHDeCaewyAPNdLXIQJ8SM0QqENIaMhUsUsE_QsNiioyE2FOCc5gsqKP1Yif_hxJZszX7E22CZ1IiTpNQwwwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از هر ۱۰ متقاضی وام ازدواج، ۴ نفر هنوز وام نگرفته‌اند
🔹
از میان بیش از یک میلیون متقاضی وام ازدواج، به ۶۲۲ هزار نفر بیش از ۲۰۹ هزار میلیارد تومان تسهیلات پرداخت شده است.
🔹
با وجود این پرداخت‌ها، همچنان بیش از ۴۱ درصد متقاضیان واجد شرایط در صف دریافت وام ازدواج قرار دارند.
@amarfact</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670568" target="_blank">📅 18:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای
سازمان تروریستی
سنتکام: برای اولین بار با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/670567" target="_blank">📅 18:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
هشدار انصار‌الله یمن به آمریکا
محمد الفرح، عضو دفتر سیاسی جنبش انصارالله یمن:
🔹
در صورت تداوم این وضعیت، تنگه باب‌المندب و تنگه هرمز در یک اتحاد عملیاتی بسته خواهند شد که در نتیجه آن جهش بی‌سابقه قیمت نفت به ۲۰۰ دلار در هر بشکه خواهد بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670566" target="_blank">📅 18:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
یک نماینده مجلس: تعیین جایزه برای مرگ ترامپ، ضرورت امنیتی است
مجتبی یوسفی، نماینده مجلس:
🔹
حضور میلیونی مردم در مراسم تشییع رهبر شهید پیام روشنی برای دشمنان داشت و مطالبه خونخواهی و قصاص یک خواست ملی است و اگر هزینه شهادت رهبر و هزاران هموطن برای دشمن کم هزینه باشد این جنایات تکرار خواهد شد.
🔹
تعیین جایزه برای مرگ ترامپ و پیگیری جدی قصاص یک ضرورت امنیتی و اقتدارآفرین است تا دشمنان بدانند که تجاوز به ایران بدون هزینه نخواهد بود.
🔹
در کنار خونخواهی، مسئولان باید به معیشت مردم نیز توجه ویژه داشته باشند که کنترل قیمت‌ها، حمایت از معیشت کارگران و بازنشستگان و پرداخت مطالبات کشاورزان از اولویت‌های فوری است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670565" target="_blank">📅 18:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670564">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/670564" target="_blank">📅 18:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670563">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAsvJufaoYAYAdI6kok8ZdRh9FZnj1YJhJ7aYkrfM0etEk9016fV6bSoLbCxgIg2aeg4WpoLDWRbIiLYSR_ogfHO9ifbZtIunC-I5GEaZ7Us0KrnSkHAC5z3DiJkuTQc8nH96cNqT5EU6hf7ZK1oXCPde0li0IhcpHnzCOzyoy9PeGphpZozuvY9pnP2iAlchT9r0rLzudCsKk4Y4GhApEoFFpf691eFdBZgGsrgcilZeQ7JlP1oOMZVK0ll_mbLV4XILF07MoNH4Hok16DP-eUgBp183Yo1IhEBqHCW_faq8E0p7_g6XzXgHOQjax9ekHj1LQsx_4diZKfXVAAJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/670563" target="_blank">📅 18:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670562">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/670562" target="_blank">📅 17:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670561">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0UOunocfZyXUwhXjmvkTXmYnS1JzVtNeVWbh6hiDNUH3FoB5h38-ZLw93P2OPhA0HnWaIowhVDY9XEqQ0DMDUNzIwiv-iTXVJCmr1kGcL2D7guoW26TBo9WojCjs-egaQLHm6lFJQRgJFwTSLyP-UB0IkBeAAUuGF_CBJBprLr8UVXKfFvAKdK2cCcDp-mG8ZuFBBi5BtSnWN291yiO6JfIagzX0KWtdIbxCzHW0r0sArdngvcVmzkdrwyBX6cnNJuGkzxdMNCsJnyQfvSAcIoYSPsrjDiq1kwwYR1pxisOuA_ldneH_cDCRIy1G36Qa5HY4Q_pVvcAWXgB06duPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: محاصره دریایی را به ایران برمیگردانیم
🔹
تنگه هرمز باز است و چه با ایران و چه بدون ایران، باز خواهد ماند./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670561" target="_blank">📅 17:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: احمدی‌نژاد در حصر خانگی است
نیویورک‌تایمز:
🔹
احمدی‌نژاد تا دوشنبه گذشته که حضور کوتاهی در مراسم تشییع آیت‌الله علی خامنه‌ای، داشت، دیگر در ملاء عام دیده نشد؛ وضعیت فعلی او همچنان نامشخص است.
🔹
اما چهار مقام ارشد ایرانی گفتند که احمدی‌نژاد در بازداشت شاخه اطلاعاتی سپاه بود و اکنون که ایران از بسیاری از تعاملات او با اسرائیل مطلع شده، در حصر خانگی به سر می‌برد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670560" target="_blank">📅 17:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv5MyhfMpxpx8SSXlTShfmOrCPApkYYaiSNuEh9yAoYYLTgNlb6JDUss15H5Wfp0-dfZ_QYAQ9DY8LpQo1BF9L142FQu9pddIX9we5jtKddd-byIXj4t-9GNTa4ubjIdbX9CAxYD2BmGaoDfUAAsdgMCTWvB-yhnWrpqoHqi-gx3iSqviwg-zkg2UgbnUOUnluG3CXSHBVAYpkDTVemLxWm_IblXsOStPZKKpbDjj82rn0XUGlSj8OltbBVe38u1F1bnWP3U3uTOUCHo5tr8bHvkPP-68_-Qo4fdMySvB4YoWKaS5OvBXp09AvLye3zPdYkz0gYDQDsbSohQkJ5lqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داستان عجیب سناتوری که همیشه علیه ایران بود
🔹
در این ویدئو واقعیت‌هایی کمتر گفته شده از لیندسی گراهام خواهید شنید که همیشه علیه ایران بود. @Tv_Fori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670559" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
صدور کیفرخواست برای عباس عبدی و مدیران روزنامه اعتماد
🔹
متعاقب انتشار یادداشتی از سوی عباس عبدی در روزنامه اعتماد، دادستانی تهران به دلیل جنبه عمومی جرم علیه نویسنده و روزنامه اعلام جرم کرد و پرونده برای انجام تحقیقات به بازپرسی ارسال شد./فارس
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670556" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">خرید ارز اربعین؛ ساده‌تر از همیشه!
💫
امسال با آپ و بانک شهر، تهیه ارز اربعین از همیشه آسون‌تره.
📱
بدون مراجعه حضوری برای ثبت درخواست، با اپلیکیشن آپ می‌تونی ارز اربعین رو برای خودت، افراد تحت تکفل یا دیگران ثبت کنی و تا سقف ۲۰۰ هزار دینار ارز بگیری!
✔️
کافیه وارد سرویس «ارز اربعین» بشی، اطلاعات لازم رو وارد کنی و بعد از انتخاب تاریخ و شعبه مورد نظر، ارزت رو از یکی از ۱۱۰ شعبه منتخب بانک شهر دریافت کنی.
💢
یادت باشه قبل از هر کاری باید توی سامانه سماح ثبت‌نام کنی! از اونجایی که فرآیند نهایی شدن ثبت‌نام در سماح حدودا ۲۴ ساعت طول می‌کشه و پروسه تهیه ارز هم زمان می‌خواد، حواست باشه خرید ارز رو به روزهای آخر موکول نکنی که فرصت رو از دست ندی!
⏳
#آپ
#ارز_اربعین
#اربعین۱۴۰۵
#بانک_شهر
#اربعین</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/670555" target="_blank">📅 17:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186f179d33.mp4?token=jgx5_McgRVop0TAgY7wF22xWG9rVGwzmTtrRfgWfTL9HEbU_mZYzX9bXRqDD4zcVASKi_P_7ASigLMSlfPnPl395dhOPC1x2siY3QD0ohNXtDNhKwkcDCL_O78Ndgmus8D8GQG7-QMUt282q-qEV1P9mVAy8GjYIiitExLn22hrw-_E_X8MpW1vG64pTQ7acO52c4hLad17XqTra8ztn88k_1X8YvMRfJmxkzz-bl-ODtpZ0u_mfwamMdqEbS25h2kxdhQqpZ3HRtG3SnhMZvHb3fdFw_juPDLdnzaEB0fHQi0wDTd9ag9wAXsmDSIoM0i9b09m8unLnKN84zw1ejg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186f179d33.mp4?token=jgx5_McgRVop0TAgY7wF22xWG9rVGwzmTtrRfgWfTL9HEbU_mZYzX9bXRqDD4zcVASKi_P_7ASigLMSlfPnPl395dhOPC1x2siY3QD0ohNXtDNhKwkcDCL_O78Ndgmus8D8GQG7-QMUt282q-qEV1P9mVAy8GjYIiitExLn22hrw-_E_X8MpW1vG64pTQ7acO52c4hLad17XqTra8ztn88k_1X8YvMRfJmxkzz-bl-ODtpZ0u_mfwamMdqEbS25h2kxdhQqpZ3HRtG3SnhMZvHb3fdFw_juPDLdnzaEB0fHQi0wDTd9ag9wAXsmDSIoM0i9b09m8unLnKN84zw1ejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ پیاده شدن مسافران یمنی هواپیمای ماهان‌ایر در فرودگاه حدیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/670554" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a93e52233.mp4?token=QbX1V5Amu5iY273VdO3ziDsTma-g6MlfqFZ8Ep0XDFkijxQO-Pv57bH6A0GEkerHkh-C6iFsEcfuq-sKQSLpLHGCiwUKDVbNdwrp6kQbkSMmJO1F-DdAtKOaty6dRKEy6qpsNSVxUT3ZRBwQyPAFnXr6aAYP0hZvWI6lFe0GrFPNFYp4xdiXUGwXg1skDYBeS4ULQAFQPHD8vxS_9q6oM0PcpATCTEvziTvwDhwwcpiPci7pbFWB5SnhoDmD05nIrhRIF3QzKP0_-ru8nl4Sug6mwNhaQ6WxutVx6qpimgddSt-9E4RC4UV-DN64-xSdJ4fg7xpHcHG_5D0nPjBFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a93e52233.mp4?token=QbX1V5Amu5iY273VdO3ziDsTma-g6MlfqFZ8Ep0XDFkijxQO-Pv57bH6A0GEkerHkh-C6iFsEcfuq-sKQSLpLHGCiwUKDVbNdwrp6kQbkSMmJO1F-DdAtKOaty6dRKEy6qpsNSVxUT3ZRBwQyPAFnXr6aAYP0hZvWI6lFe0GrFPNFYp4xdiXUGwXg1skDYBeS4ULQAFQPHD8vxS_9q6oM0PcpATCTEvziTvwDhwwcpiPci7pbFWB5SnhoDmD05nIrhRIF3QzKP0_-ru8nl4Sug6mwNhaQ6WxutVx6qpimgddSt-9E4RC4UV-DN64-xSdJ4fg7xpHcHG_5D0nPjBFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ترین‌های جام جهانی تا اینجا؛ از آقای گل‌ها و گران‌ترین تیم‌ها تا مدعیان اصلی قهرمانی در یک نگاه
▪️
قسمت سیزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/670553" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu6_iDsesRXK0HuXOmY6cz4wJX1VRDreYVtVOUbCrM8d40eqsy38_VQ8gCRCwkKtkfFRfXrHn09VY9tEe52TqYomls5X7ZLchw8AjXYWnUyRFOCKIkZ2OxCmlFtxH6pd9beX4moebqNY5yiI5P4YR7jUOklJKCbRFp3zOQ5y0mrNlSMjTLDv9pRHLQusqmRzA4XU9nUGfEGk0x_jMsn-E2RNlfn4J9ssENfhaZHBzOFhEseh6c0BHsya2PqqjlQxco3zDzvZDN2h1Fvhjkl9iIrq9tBZgHwI-SfnyFtLrRMcr8FKhQRMQulspOYP4hJJML4M3ro39RqBIFjri_7EZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ پیاده شدن مسافران یمنی هواپیمای ماهان‌ایر در فرودگاه حدیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/670549" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2WMZ0__USCt6BqDJBl-HyuQG_CCybo9HxWLQx3yHSs0RVs_NFFU6C-jOf25tBcOLNYtif-v1_P-SwXSEwycCVUykakklN0kR3nx6fMh3wDVO8IaDc81x5SnSJg3WkybvnpGf-R0ZM_9eiDLvSc0JQk89hVGP9HSKCMKuB7oX1ZtLKCx3Ss79i89s8K_Qm4yqPPW3AS9aHBFVFjLWAOswz0GY0vovj8O3-ZicS-kgiiJVqflm8RrYDm21xoHtE_n6-IK9rTeHeVQxTqvzUxjFd4RrCqNNJkQACVmtlOl3JhoMmUF0nsrFrMEJSHmlkcpH05pttQHvs3GT4tlLQgeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با یک آزمون، استخدامت رو تضمین کن!
🎓
کارفرما دنبال مهارتِ روی کاغذ است، نه فقط ادعا. آکادمی آریاداناک این فاصله رو پر کرده؛ بدونِ نیاز به دوره‌های طولانی!
✨
آزمون تخصصی + مدرک معتبر + رزومه درخشان
فقط با چند کلیک، اعتبار حرفه‌ای خودت رو بساز و از رقبا پیشی بگیر.
🎁
کد تخفیف ۲۵٪: aria25
🔗
ورود به آزمون‌ها:
https://ariadanak.com/ariaacademy/
📞
مشاوره و راهنمایی:
۰۲۱۲۸۴۲۴۵۴۳
۰۹۹۲۶۶۶۸۴۲۴</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/670548" target="_blank">📅 17:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ماجرای سگ زرد دروغگو و بمب‌ اتم ایران!
🔹
ترامپ امروز: ایران تنها چند دقیقه با ساخت بمب اتم فاصله داشت!
🔹
ترامپ چهار ماه پیش: ایران تنها دو هفته با ساخت سلاح هسته‌ای فاصله داشت‌.
🔹
ترامپ پارسال: ایران تنها دو ماه با ساخت بمب اتم فاصله داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/670545" target="_blank">📅 16:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
♦️
سخنگوی قرارگاه خاتم‌الانبیا: به سران کشورهای منطقه هشدار داده می‌شود هرگونه همکاری یا پشتیبانی لجستیکی از ارتش آمریکا، به‌منزله جنگ علیه حاکمیت و امنیت ملی ایران
تلقی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/670543" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670541">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff97123423.mp4?token=C0ERI12SLiiKDNYhVyL9_Ftrxd7-q97AI8695biiT2JJwP_rKdb4cT2SYKe5Jqv4wwqiBsnQqd81UdyAqFT8cPn-r5RiYJmfgrXh-jcxYn-lRRKkfgkpF9Cux4ViaBcJjBgki7oOIjNafTPbYTt3HTqGBt_FYlV3CFkSP9R3awy7skkOv2mDwBpllpbDVa6TDa4M5fEBx4Uz5Gd_W3iEw6lP6_E6V6NTsM3Kqm_6OIo7-ExTKpcqFYQWxqh9OwTOm7NW0rrLqkFfhVc2Xas8WGrYyE6RqmGqvZpdWg5plipM09mI3x8IggK9fql9xa8I1NliwNPibJZHYjTzMe4O1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff97123423.mp4?token=C0ERI12SLiiKDNYhVyL9_Ftrxd7-q97AI8695biiT2JJwP_rKdb4cT2SYKe5Jqv4wwqiBsnQqd81UdyAqFT8cPn-r5RiYJmfgrXh-jcxYn-lRRKkfgkpF9Cux4ViaBcJjBgki7oOIjNafTPbYTt3HTqGBt_FYlV3CFkSP9R3awy7skkOv2mDwBpllpbDVa6TDa4M5fEBx4Uz5Gd_W3iEw6lP6_E6V6NTsM3Kqm_6OIo7-ExTKpcqFYQWxqh9OwTOm7NW0rrLqkFfhVc2Xas8WGrYyE6RqmGqvZpdWg5plipM09mI3x8IggK9fql9xa8I1NliwNPibJZHYjTzMe4O1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: نمی‌گذاریم آمریکا در تنگه هرمز دخالت کند
سخنگوی قرارگاه خاتم‌الانبیا:
🔹
ایران با هرگونه ایجاد اختلال یا ناامنی در عبور و مرور کشتی‌های تجاری و نفت‌کش از سوی ارتش آمریکا، خارج از مسیرهای تعیین‌شده ایران و بدون مجوز نیروهای مسلح، با قاطعیت برخورد خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/670541" target="_blank">📅 16:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d76806ced.mp4?token=lCDWpfIs-q5vHRDduldfNExpvhry-8lJq9ZWaFYeqeWF2hmAL1e8sVxfTueaxg_Hkfo4yglEof6n2Wosk67zLaq_ebx42tDrGl2Chy2mb31jHXSCP0D2pAlwpR_jJipqeqAuGzh3aEIdckLAjX8K_KVCPETqni7bYZhd6tgD6lrwV8RzZXzpO24GFgy348msGbVZfP3PH81Hy_AHXFm3SwYOFyG_EpR4cE5SOJCq-VU5MsU51h97Ssef1AnAj9Pa17CYOCLTDUB4CpkLqSvVKRgjjrKitVdCemg0ZKnauREoIlKD_2Uu7FYSTIFhMbjJRFUiUCtnB63PVltrx7JkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d76806ced.mp4?token=lCDWpfIs-q5vHRDduldfNExpvhry-8lJq9ZWaFYeqeWF2hmAL1e8sVxfTueaxg_Hkfo4yglEof6n2Wosk67zLaq_ebx42tDrGl2Chy2mb31jHXSCP0D2pAlwpR_jJipqeqAuGzh3aEIdckLAjX8K_KVCPETqni7bYZhd6tgD6lrwV8RzZXzpO24GFgy348msGbVZfP3PH81Hy_AHXFm3SwYOFyG_EpR4cE5SOJCq-VU5MsU51h97Ssef1AnAj9Pa17CYOCLTDUB4CpkLqSvVKRgjjrKitVdCemg0ZKnauREoIlKD_2Uu7FYSTIFhMbjJRFUiUCtnB63PVltrx7JkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک نجس: نرخ تورم در ایران ۳۵۰ درصد است. شش ماه پیش، این نرخ ۵ درصد بود
.
🔹
من سلیمانی را کشتم، اوژنرال باهوشی بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/670540" target="_blank">📅 16:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670539">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08115117b.mp4?token=c_vcEHC2schW-Yjy0W6YAswZAg15HYp0FAnC47Nm_o3ZVNGq9QNqTCjrTi47Y8-0M2cxDu8o97dZBjKBsrsJfT5YDDZ_DPFEE_SfsHU1j6i8drs3Asd7mOtjGh-teJp-iu9HEroMn57ns5CJoB7OBeIVZF9GT5TQ0txkBHjheJpRfVmMYku3LZ4shcqh8q6tsXBdnDxPMEu08Z60zb3eIXYlfxIrnbRkjnq6Y6HzMmXa4QEwc46p-5jZgMR5SF_WXb-0WJpVjW7vSGEa7Ds0BhzJRipjQoTjAdFt8h_hmBaDGgiAc5D3zipjPKcHJG3wE9dzXQc7uLqww8OpKRwyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08115117b.mp4?token=c_vcEHC2schW-Yjy0W6YAswZAg15HYp0FAnC47Nm_o3ZVNGq9QNqTCjrTi47Y8-0M2cxDu8o97dZBjKBsrsJfT5YDDZ_DPFEE_SfsHU1j6i8drs3Asd7mOtjGh-teJp-iu9HEroMn57ns5CJoB7OBeIVZF9GT5TQ0txkBHjheJpRfVmMYku3LZ4shcqh8q6tsXBdnDxPMEu08Z60zb3eIXYlfxIrnbRkjnq6Y6HzMmXa4QEwc46p-5jZgMR5SF_WXb-0WJpVjW7vSGEa7Ds0BhzJRipjQoTjAdFt8h_hmBaDGgiAc5D3zipjPKcHJG3wE9dzXQc7uLqww8OpKRwyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/670539" target="_blank">📅 16:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670538">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7491e8f22.mp4?token=U66NHzwTDIR_d8zJLue2cNDzkSVB-MfMug_ZRQ6b0h2qOKP3D9H5JyWXudvLqUq__IO2gCm4wRy2jPK634rSZk8wHiPhccPXCHdd_CYfvHym2wMS_kahuvTL7ntUzXyqhSQg8nXH33ZD2cuYWYwN9awux_VGAkKcOWcWnaQFsXhWZdUX0rPo5Rz5JdpmrI1Qp5KDHnj0xA3d3ouPaeEJOwwY0PEHY8YK73-BlLF0vQ8-IWXmz07ENKuynjXCgR4BNHiqxOAe8fNNJRs6Sm2WTI25byFA3op4SgHfcZRUZepjaLN9mTkNqtOiUwq8LUg31VPn2Sm7BPRnW6Sz7RMIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7491e8f22.mp4?token=U66NHzwTDIR_d8zJLue2cNDzkSVB-MfMug_ZRQ6b0h2qOKP3D9H5JyWXudvLqUq__IO2gCm4wRy2jPK634rSZk8wHiPhccPXCHdd_CYfvHym2wMS_kahuvTL7ntUzXyqhSQg8nXH33ZD2cuYWYwN9awux_VGAkKcOWcWnaQFsXhWZdUX0rPo5Rz5JdpmrI1Qp5KDHnj0xA3d3ouPaeEJOwwY0PEHY8YK73-BlLF0vQ8-IWXmz07ENKuynjXCgR4BNHiqxOAe8fNNJRs6Sm2WTI25byFA3op4SgHfcZRUZepjaLN9mTkNqtOiUwq8LUg31VPn2Sm7BPRnW6Sz7RMIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/670538" target="_blank">📅 16:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cb46e412.mp4?token=YRsTGfTNPazhbzQDZj9ud6NlGToaKK0pB-Hxv2ADnWoE0hgFdBefCYIU3aRUEf6oAPBhTx0iB-gEZDv9bDIr5QOxK44GcqquRAiMpSfmewauS6UhfQSYRbptLnm7PwSjkiMHOmYEZGixpyPMjCy04apWFNuuVR6xqFUC0a0swdLC_UYzuCj8vKrBtT0bp8gKVsM-DRHTnflkK5o1hMNZBwrTOZXOPqd4NGvpzwOHBAFl1_WUIde4whKwQ2joW780r28wSJQ-5Vvfbizhw-B9lq1vpsL8AKuKOCFrZuqPvDIAG34IEzHiZduBMun81EM4H9HLU9_KUAZunJ3jTEekqgdam75n2cVK1HJu5GDV-UfuRQecr6okRuKOEwyBAgtpQ5SIR4RTR5xuIntc2Lf7QOGwDQDOMImdUHac8up3RqQZdgtAQtRRuVwI5xgU38i2F3d-mJFY5M_xSZnYvLLzpM4QCNLQvDXw7yM4Het65mT2Y3M3q8A5Omgk8MQgInxvGuSxoRZGtudupGjFIsxB-Qge4PZg6A5-mT9YvhrkxSQ1KAqMQnmIqZozDSn4y25Gro9ArVHRCA2z48kOg-MnS8l4Psv7ecAwNOQ7nr1GHAQNUuRhE7AYcjhPIpH168msL1gc2cZgTvWPJzYJdcqq6OVTlIfJVAxhZnydCBqRORE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cb46e412.mp4?token=YRsTGfTNPazhbzQDZj9ud6NlGToaKK0pB-Hxv2ADnWoE0hgFdBefCYIU3aRUEf6oAPBhTx0iB-gEZDv9bDIr5QOxK44GcqquRAiMpSfmewauS6UhfQSYRbptLnm7PwSjkiMHOmYEZGixpyPMjCy04apWFNuuVR6xqFUC0a0swdLC_UYzuCj8vKrBtT0bp8gKVsM-DRHTnflkK5o1hMNZBwrTOZXOPqd4NGvpzwOHBAFl1_WUIde4whKwQ2joW780r28wSJQ-5Vvfbizhw-B9lq1vpsL8AKuKOCFrZuqPvDIAG34IEzHiZduBMun81EM4H9HLU9_KUAZunJ3jTEekqgdam75n2cVK1HJu5GDV-UfuRQecr6okRuKOEwyBAgtpQ5SIR4RTR5xuIntc2Lf7QOGwDQDOMImdUHac8up3RqQZdgtAQtRRuVwI5xgU38i2F3d-mJFY5M_xSZnYvLLzpM4QCNLQvDXw7yM4Het65mT2Y3M3q8A5Omgk8MQgInxvGuSxoRZGtudupGjFIsxB-Qge4PZg6A5-mT9YvhrkxSQ1KAqMQnmIqZozDSn4y25Gro9ArVHRCA2z48kOg-MnS8l4Psv7ecAwNOQ7nr1GHAQNUuRhE7AYcjhPIpH168msL1gc2cZgTvWPJzYJdcqq6OVTlIfJVAxhZnydCBqRORE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: خیلی محکم به ایران ضربه خواهیم زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670533" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670531">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIhZXBT35inJXX3qVHCv2rNZvRReZUt-SzxQfCRN4U8TguQhOlJkiiEfueVQIkLlLg1CkXXsTyYLV9vIgY6trRnVa4np3dhArrt4y42-JpDIyosKvCr0IIaeeXXIbDc_EBDbgXlrxrwF69SgutBewcTSX7vfS74TPh4M_pv-XC7Mf4gJVc7w6RFaGJmx5zfpxuT250uleg5IR68sK29o1m0W_HbsAFOD2VEbArZU-VlNPV7DBT758FTedTUIv95FpCD99hdUALpNsbzHO-9uvunqLyUCv4r5dIOGUAaXQXTN8m1WTETIr_g7HowooUFx21trglVZAkpiLaXbdG5_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/670531" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670530">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22da5e019f.mp4?token=MEZH6B1v8EPE2jXs31m962phJQtBXmbSzIQmK4oGFYQd-nn74aQTrnco5bEAjDjrMrjJcO2__ANp0lumlOB8LYuNuBy-EUnwNE1HtVxklN3tsZ-lnYGMWfOouDn4utK_qyoCF5Ej1fb3iZiSewwwQvxLU_q7ra9R0MvuAsTluz9JCNF89FFIHUGY7neDdfqjknUhtWuNxyVvxBKWID2oMxQgVEhi6PaIgJACh-oCuIiWU1IhRZ9IQORrF0DEuyii3xye9n_ZKV2oMY4R9DNb3mWxUYiAaMEXUwCsHRL5YvRC3f4eXkeJxxMm4MOt6bQMKmzzn3w1RhuOzrPPhUEMnSV3PogXcbLQ-20EB0ZgSTOl8d7E3jB5Cfp-njbKPE2UvELl7PO2bb6xZfDzbjrCOi9rLpPy28Xj2sDRztFmHDYkaFkqKDW3OoeB8tNADZJYSbD3sYzFafc97iq43CSUZG43eZAJ30Qg-CL4XGH583e18x4PRwwBlpV4rpi41GqOoz71rP5YC4nOjpCXCK_l72r-tEHp3jXT13S3RyzcLHl9uDCiikFLbmQoo9Clyl_Xhv6L1pzzhZw8SGp5i-uNWm1_ImeNmnYAqb8-B1uREGUOrw0GeIfFj_ncfywnVWTNrnUnlm0fPjoIPaA_ZMrsMZrXKVBrFyUTMYsl_17SdLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22da5e019f.mp4?token=MEZH6B1v8EPE2jXs31m962phJQtBXmbSzIQmK4oGFYQd-nn74aQTrnco5bEAjDjrMrjJcO2__ANp0lumlOB8LYuNuBy-EUnwNE1HtVxklN3tsZ-lnYGMWfOouDn4utK_qyoCF5Ej1fb3iZiSewwwQvxLU_q7ra9R0MvuAsTluz9JCNF89FFIHUGY7neDdfqjknUhtWuNxyVvxBKWID2oMxQgVEhi6PaIgJACh-oCuIiWU1IhRZ9IQORrF0DEuyii3xye9n_ZKV2oMY4R9DNb3mWxUYiAaMEXUwCsHRL5YvRC3f4eXkeJxxMm4MOt6bQMKmzzn3w1RhuOzrPPhUEMnSV3PogXcbLQ-20EB0ZgSTOl8d7E3jB5Cfp-njbKPE2UvELl7PO2bb6xZfDzbjrCOi9rLpPy28Xj2sDRztFmHDYkaFkqKDW3OoeB8tNADZJYSbD3sYzFafc97iq43CSUZG43eZAJ30Qg-CL4XGH583e18x4PRwwBlpV4rpi41GqOoz71rP5YC4nOjpCXCK_l72r-tEHp3jXT13S3RyzcLHl9uDCiikFLbmQoo9Clyl_Xhv6L1pzzhZw8SGp5i-uNWm1_ImeNmnYAqb8-B1uREGUOrw0GeIfFj_ncfywnVWTNrnUnlm0fPjoIPaA_ZMrsMZrXKVBrFyUTMYsl_17SdLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/670530" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670529">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de61a4eaa.mp4?token=k9ReRy_HLjAknvCNJhWI3vovmz3B-ne6XySnnh4NIcBIWFRt6Jz2KdKK6IY3FLMQWNPlN_-X-BD0_epHTQbqqcP2z6KCxahtaHDCmI1JecOMt2i2Hf63WU4HIcwW7x0vFRsEYICI03Mh3YNjRl0tSY5Aq0MmjYyRHfzBxDZc-NfR8aUWoJ35eChh1E_Wq-C0GbZrqcfCuk5gThQzTZQmXmPlZcIGq8NG0w2xMKZohDlVPfNm3rZDfUFDMVTNRJ4H1VIXwVTE5FEgpKYbgbfxwfBWxKHDAri7X6KKuDtGYoDg1EeWL-bukOxNjBwsoBkbyNfwOSNuG4pIh8Y0odtlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de61a4eaa.mp4?token=k9ReRy_HLjAknvCNJhWI3vovmz3B-ne6XySnnh4NIcBIWFRt6Jz2KdKK6IY3FLMQWNPlN_-X-BD0_epHTQbqqcP2z6KCxahtaHDCmI1JecOMt2i2Hf63WU4HIcwW7x0vFRsEYICI03Mh3YNjRl0tSY5Aq0MmjYyRHfzBxDZc-NfR8aUWoJ35eChh1E_Wq-C0GbZrqcfCuk5gThQzTZQmXmPlZcIGq8NG0w2xMKZohDlVPfNm3rZDfUFDMVTNRJ4H1VIXwVTE5FEgpKYbgbfxwfBWxKHDAri7X6KKuDtGYoDg1EeWL-bukOxNjBwsoBkbyNfwOSNuG4pIh8Y0odtlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/670529" target="_blank">📅 15:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670528">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amDgqQPnbtuSce5_LbzYk-Rl-SPu8R6KNSG0djAXiRTJx2Qlcx-kcPoKM98-gwCJ2M73D9ECW3ayd8KR4PPMGwbNDBa-bJMGn9bIgnibFpaV-7rYrNcyzeo6Nxjy5Iq6-I1IZa45UCQLGPj42i8O98WZlMnqcCKM7qVGOU9HfygZqmzITeXWcKsqF2ZnKvm4AtEAUAhPkh1PrFYujeVVcw1TZBBsksd3ysBJH9pbuE9pCPGAUequ7UDg1eY1QDN5s_lJr3KTr16yQE1FwhmXtecyf8wCSgxehhZl5WcD0oYym0u80gSONsG71AZHJe59Xd7whGS7YmCa8Av8zplgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش: ساعاتی قبل، یک فروند پهپاد متخاصم دشمن متجاوز آمریکایی با رهگیری و شلیک موفق سامانه موشکی زمین به هوای دلیرمردان نیروی هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی کشور در بندرعباس، مورد اصابت قرار گرفت و منهدم شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/670528" target="_blank">📅 15:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670527">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">💠
ماجرای جنگ ۲
💠
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/670527" target="_blank">📅 15:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670524">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I63SxN7RRgJ0Rn7tnkr3Iye9fzkSNu0vNEx_eXP6eKBhj9RZDzvWbtgbKoatUA7zNfOFOtAplebUOmp_w1U01bJAYD3G94SUeb1qMlFg0aUiayIyPX6SSb3YeS4gLxOGQL94chxqrrz1UakdJqEUZfqvJLvU2jL2tNJETi0_MQ-Eq43S4FiJ8AcgfI_bLUL_JXo_skMkYCI5vQHowkHPY_G5I9YUkW15eNfJYpU9HCROU_t4bhLnjqzXRGIxE-KgUy3MfvjP8HoZbpEpNSjFnBfaDz0XkLWhV2qZxCI6U_61FV_hpsiRt3JtQQSpDCiQFeGg1X54tZUTIePg8B-KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fp7Lty5xh67yv3ARIcwTo8mUaJFKlCr8TQdf4rVlCM7w3XEHJlmUb2rOnBrWOoDzukMLVPJ1LkxHlf-UihotNQ87rORxbhGmfHoiRldv41Pc2jLDKgrHCdtUeG3BDxqgVGF_JLar5q8LxUgckkA4bdREpolDmW66fZJM_c7uSffqYlNtxFCtCHMDK1-xv9eHYL-iOBv89YW0omhIT1pUK3sAZTgRRQgNMfXXZGYSSfy9VXNGD76WpN79N-I6j8zP2dIeXsfBCRDDG1SXlkJizq_4ljKfEgkJgdznOGRvMqXJwGbHvs_cbHjQYev_uuyB4DXZADGGgcMF_3VmCUOydQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عضو دفتر سیاسی انصارالله: هواپیما با موفقیت فرود آمد و محاصره شکسته شد
🔹
هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/670524" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670523">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c02f55f5.mp4?token=PQYeKD9TshLyvKx2C-y3kYhsJKmyQM4_O28HIv_Q6LbmM9cb384FdKY50bBZoVgLntdoBpv0DHPPsbKaYFYBr_ptyDHkxwsPHzxXRYRU3OrS0tM-yypBvBFOcgDFu1YqxZxPX_HGFA8FHmxeXXvLij45ODtISgEmtcBbfRoSR8lXxCdoaOP_I_UsmlVy9r7kjDe8M9_TJlBHpFEBTQiFCIfbxyNgUKaWpLlTe8XYexqksYjtLbbiCaD_EyWI4ByWtkgOHlSmhzIYzDhgtkuXNRVQiFPQxo581lH66eEUsqUxc6rPHJsdUn4WyCerjdcipA-r1Wny0CIiFG2N8FngqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c02f55f5.mp4?token=PQYeKD9TshLyvKx2C-y3kYhsJKmyQM4_O28HIv_Q6LbmM9cb384FdKY50bBZoVgLntdoBpv0DHPPsbKaYFYBr_ptyDHkxwsPHzxXRYRU3OrS0tM-yypBvBFOcgDFu1YqxZxPX_HGFA8FHmxeXXvLij45ODtISgEmtcBbfRoSR8lXxCdoaOP_I_UsmlVy9r7kjDe8M9_TJlBHpFEBTQiFCIfbxyNgUKaWpLlTe8XYexqksYjtLbbiCaD_EyWI4ByWtkgOHlSmhzIYzDhgtkuXNRVQiFPQxo581lH66eEUsqUxc6rPHJsdUn4WyCerjdcipA-r1Wny0CIiFG2N8FngqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای شما هم همیشه سوال بوده که این صحنه‌های آخرالزمانی در فیلم‌ها چه‌طور ساخته می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/670523" target="_blank">📅 15:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670522">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اقدام خصمانه انگلیس علیه سپاه پاسداران
🔹
دولت انگلیس در اقدامی ضد ایرانی و در همراهی با سیاست‌های خصمانه آمریکا، نام سپاه پاسداران انقلاب اسلامی را در فهرست ادعایی خود از گروه‌های «تروریستی» قرار داد.
🔹
طبق این تصمیم عضویت، شرکت در جلسات سپاه پاسداران انقلاب اسلامی یا نمایش عمومی نمادهای آن اکنون در انگلیس جرم محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/670522" target="_blank">📅 15:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j48lCREzcsrXJ7H055fh4DTYh8Vrv-2IBp0IXxnMr-mC2BbzLY84CziVhTnFBje2M2cTuZhn4jv68tV4BIclhk08gUrcePL2mAY3kQpjIoB5RZ_b8EZ7lqhX-n8rwefjDswUwfNjk6lR9nq_dbaVG5-VRid9xtBxUD055J6lTuDwqGb8ageUqfR1gysuUDrwxuGYiP6Iim8xw60nPPGsQat4MStQP2nuW1rVXAM6GxC4JD5lYoLFjGm7zitapJF08yuUGkBhFD9VdR5IyYDYo3G2An1qK16KHAevc0qgguL5fohfSnKIr2xTzFJu7G6thgAqbNvbO2N_eF0j4k987Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه پاکستانی: روسیه هواپیمای روز قیامت را به ایران اعزام می‌کند
روزنامه دیلی‌اوصاف مدعی شد:
🔹
در بحبوحه افزایش تنش‌ها بین ایران و آمریکا، روسیه ظاهراً گام نظامی بزرگی برداشته است.
🔹
روسیه جدیدترین هواپیمای مرکز فرماندهی روز قیامت خود، Tu-214PU را به تهران فرستاده است که در شرایط جنگی هواپیمای بسیار مهمی محسوب می‌شود.
🔹
این هواپیما همچنین یک مرکز فرماندهی پروازی نامیده می‌شود؛ زیرا به رهبران ارشد و فرماندهان نظامی کمک می‌کند تا از یک مکان امن با یکدیگر تماس برقرار کنند و در مواقع اضطراری یا درگیری‌های نظامی بزرگ، عملیات را رصد کنند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/670520" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در امارات
🔹
منابع خبری از شنیده شدن صدای انفجار در امارات خبر دادند. وزارت دفاع امارات با صدور بیانیه‌ای فوری اعلام کرد که در یکی از انبارهای نظامی زاید آتش‌سوزی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/670519" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
