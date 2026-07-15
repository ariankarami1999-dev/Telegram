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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 459K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKv05iRbg_w5qmDgUGZT-U9QsY1kIcHKl4V6bhbevT_rm0jOOOD-1IKAUt0khezXhVJMwBrRC-DAwBmvYnK8CDltc0Mee5uF3hMUgRe6jvvCFVKywIM6RYtdhHJVeMqNIfSsj5w0ILYnDTmT82QZH-2N80__8Ou3YCwtRCK0Tlxcx85CpIbrmgqFN61tykSd633LRtkLfLS0BgVg0mhLAASdn3uNhxGzoJgNx21lp9bU-Mg7BxZdNfjVTzth4EByGXLh2pPCtHq51WSmWkEScdyUxWQ-iNc5yw1eSA2jCucJgA1L3GiPEPxY2X94l6yhwOyuqvixkMmy6UpaBpwXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRP5ammiu8y8AcNi2fu15ogD9zUs8kT9t8DbieNsB7DphgoqkbL6jebcKhDn6CPEyV4zMraZk2Erg9LVygaMaOxcCYGrFDNkAtUiVV6oN7tb-hcabQIfsEBFQi7wLnhD11D_1gA0LwbvyvlVtZsY8fOZzXYPzUlcHmxQEV9L_rZXyP5tzd4RwCsglSEKl_vZAqcreUQQfNFDB1o7kqDpobefPj89vANRAP7hmr_EoXzzCCxLOb8awR9qwr0M6-9XWsOOkiUvqNjdqJmtsogOr-iLhF2ZDxxeNApBGqRlCG1y_xVyB9Pa30kYK3lSbJSixBS3YSFD_vMRp7V82T8fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWRl7JGFqhG07MHgWG-Oh-Zbm6R1qv07dVgmQyl7vEHG4sMrPCQxt-Rc-hMPH1AmbOyvLRFKqTkEztfevQvl23EHB1LnW9b68iER_mNV8ieDlOuyTs6ADnZl_UsBDAw-lO3be9k2yz6AuVoLDwcNBSHjtKuw-zOJeJPHewCB8mPGuk8QMK-PrClpa9xGyQe8o4FXXJkRHaUcn0CkrBatWX4ftoxzx3KfkL-kdVsE8R2WYdsOoiisoBOBfJPsaMXOZc5KR3fv6ZHw0TiyjOa2biR1PC1yYm2OqkLsvdIbWvawJMYEXV5810UrLA7BPVXSyQRe6kwFuoE3dp9f29BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwp-az-yU5-SQJe3gezLMywvBxvkqLEP-Zqcar38tP1tQiq5HDemCpC8YFearJw52Eku-4CbmRbU_aMa-vGoZeTMl8eXZ9gw6ivXB69Nwbv0Okik_hXUjRn8erFLcM641xWKX5NNdKBpgj1J9g2JwfLbctkRzPmWGYhYIjv7uQFmSgssXTJNuRJ7eq8Vf4n6ne10BCpekl61bAuP_P-aWKxcrD90l8tggVgq1uWQtOY2-F-Ub2I0GAZe2lOk64x0Afox9hdiDjzwCqBOTjcL7uMLRGPT9HghLZ0HS39T5dO2dPws8VTWEd-5MaqhhY8TGyrscPelH4W8Zgloll_l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6J8Z8v22e68jgA8K_d2vFmKLN07YlB1w0VXSHUev8Aw2N3-ORX2j5_LcKSZmdeRs6WRCUKb-0Colq79JfmIsnqIUZlepDdZfJ5N0rryPxFYhfRXWgi1AM27giqMObJjOSUo1QrXnKtSOuSFYFbH3rZNBjwsm0lgxE_ZVaheI2BJ4e5LfjnpvM_4giBGITlljUWpJ79B-b5_RouC17xO2kqMrcpL8zcMVyiVQdKMdUFWejvzI8c7kNhVvwBrd3zPeL7Bod6KZXsfkttybr9Fe-Nc8qD5VuNrp9ighBhPgchnPj_kJXSTc7LZvJGRbUOjU0zQMfMDgFy6HVt5EoC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=PyaRouDJ0YmB-WfDKA1nCU-WhaZOSEu_rGlPSyw3q1zVUTcnEpSRcJAXb4H9royvOR9EyjEMF52wq2oWUlkHnXMCKv3MK4AM3Xy9tiIcJW4kw0cGCy_gmRm_pHM9TIA2dk_ZFNJskUnULFyMjm7OwyBvKcbjgwCsnrBlemRFuv8pUzEYZ3PYw_Vx6luyUST_u4XP9jlesFJpVBjnjE0CGGUR2r2fH7RrH6UfKUsyZ22vtVCdi5sdJFJTuhMjul56HP1HIMhcRKJ3kBLEdxhoijeQ7e1a8tRcF6nRM6V9QJpfa5BGVAXgKI7f8qsDoncdSMEz7T6wOZTWiic__eEm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWOdb-g1lc07xnC2M2hSLsZdBb2P5_9Gbg0qAdWpYKr2rksaYYCGl7H5tBDjASi2SDNLt2-8gNXbZKvX_6sw52DE7oMwn1-xJ3lP9hd0jSoET4KC8HCA_IE5-UwLy5ri9dQGplXH-iL8fYTYzyPy8EeTqtEBOWoGoCXJmsge3io-3Jw7T1PjaFbP0zpg7ahtZS7U6Uq4eXSfJPX2MEQGrL1SducwqRbcOEE7Iac7-o-95d_wQhdpbzz1JRDiUkHu0pPO7hWaCPpv7jbC0xoMatInuqKosMjrre3RN6OJIkgtRULgZt2nX0Cl21KNbAgj7SesakTwCpPx1iT08XkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB3qC-glbsoN8z-7G8g5SYBZ5DDYk8pO28AmSyIxZDI9i0rRmtoMdHIhWO0B-I8bn27jlKMo2frw6U41ZW6b8XL0Jz7v6GG-ACQIL0vNiq_l3slKzJA9EVo3x-US-YUzJByhzBsM3i-SKTAhWicuqnr-xsPY_3__PcpTtkcVWlauFH48FsicbYAtyz06iSNrGqm0yXt8tBx0C1O8rdiGOfFeEujyS-2jeOLmNsDvAyz6NbFLm7CPAA7SCEeV_yKuj5hOXCVMXGet2CmsCfpZ854RoGSu_3jKknArk2wRikwHo8ldPQ1ptheiYgBj92_-0zFEBNrzYttD7NYZWRsSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWnRT52FHCZKEA9s5TT-JY46PKw3-fXgxyOT0Ag82-_Ovhq-mo466VMzp-E3OwYcEcUogzETOfLH0T44MoobTVeJPyrHWLcnrygd4uQD6hVQ456NG2iio_gW1RVef496T7JpCjUksztdeVlhQbejSvykOyjqKGH6qPODODqXzaQHuAFkZuLS6cglU24nvoX63HqZeG2iRGVwyEcv2tnk9v6k6VtpVtjGrak4a4_2EINsqHcBfMBO0gre4ES9QtdXlkCDxqSgWXV0xxKhvp4EV3ff3itTesiMp1wLfnajxOmS6aN4YfNkF6sffxAFTh-0IWvF7vLjRDM3egLMt07QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0ReULuo-p7yL1I9Rh-kcePaX4qgkwrbH_gOmKouwJnjaOL59f5vBoK5QPJBWyiRsa14MxxYjfqtvaSHGhpWNsF9ZqHAeb60t_qKPtU6x-Zde3eAZ_JqEj70v1yQTyI6EQ7aYjNY5EWZBEQwXtvN9AWfH3UFZy4s4p_fb1MVS-X2gksaRb_IsyKYYK5ZqXplIUOHxx47L2goCayhb8801LZOssbP2CjqjtAeweAurcos2xCq9EY_aiRrQy_NdCoLFvYbnD2yTozaNtgXJ-vhiKzOT84P7brV5ExntjslXjzelddfNwtgRbyqSISn7MVvjRqq0czVEAeUIqk7DHhftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyaNw6Y6nqRFN_Oajqw3NT5UdYXVNtRFrVkacvfg90C7zCjijwK8nLgEUjbCDVOpIwiup30mPtQwCwYWLOo33FTeOl3bvLS9zG4mVQUy2CuAR4ukXSZywFaLmFFGgKubxNBGxIqUqS_lMi08zjidR2y3kodQENVd2JqvenQx0LHjRVeDPpEmDQutMI1dMWojDGoUIhOjW9xw4oq1SLU8c4OP7krbn5nBW8YOBsNDfrM_CGyo7WWJwZoFvqt7qzGC7hiP0dGJTyE1vyhNqHFHucce0asKfERHxUxKzguku6GgOmcA-kcAMbh8zbNWLqkxtzk1r9gwhtelCb9KaXFFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=FAzRtR36fE-MXtMTQaxpKvdt0ZIeXK_SoouHeNYPzdOvKtabN0Ps7geE0XEGLg3YwkiHlPemCrxsg0UDJ8PXkSjLTv8G2sdk-PRgZ2l_73xw6z7nRnrjskLjIDcfM1ms56161Cz7bclV3zJ17rg9_L5hjHkPfxRot3wq6hrEr_NeVMGc5sV3f3YXPOLqyBJq3JAvAtB6SR-RkSxFF4HnxtlIowW0ueJ2DFSC2jeZrnIf2kxCOVyjN7CLS6HWKWtoPq5HVwhru-omnilY7UwinVu94OrZiTmtl9pRQhyq5jV9O_UtFWtDaV7JCIF4RkAuC71F5FdxLNqQAWJjuXZ2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=FAzRtR36fE-MXtMTQaxpKvdt0ZIeXK_SoouHeNYPzdOvKtabN0Ps7geE0XEGLg3YwkiHlPemCrxsg0UDJ8PXkSjLTv8G2sdk-PRgZ2l_73xw6z7nRnrjskLjIDcfM1ms56161Cz7bclV3zJ17rg9_L5hjHkPfxRot3wq6hrEr_NeVMGc5sV3f3YXPOLqyBJq3JAvAtB6SR-RkSxFF4HnxtlIowW0ueJ2DFSC2jeZrnIf2kxCOVyjN7CLS6HWKWtoPq5HVwhru-omnilY7UwinVu94OrZiTmtl9pRQhyq5jV9O_UtFWtDaV7JCIF4RkAuC71F5FdxLNqQAWJjuXZ2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuF6wy77hm5XO5qkBs8D0PgnericKY7Rfe6ulxDp2ulIxRFz6O5z5Vjg8pU8t8x42szhOV1DImlbraccZOcV52-JAm14Fxc0C1wEH1-5CjwXn2v7sqTk0SrNf2ueNJXt_FeZUbH9qvB3ZLAenn80pxhX_a34sxI7dQyAAosIDz5DtHS7Mob1WSYFhNTfEY6nLF8bEjBvZ3AmT_mW7pSMGQKN0VloYzv--Vv_3ItguEJTrom2AGqub0d-kGfDeCYaFSnYQEXnBTpM-SYPdh4NWfkcl0NO5eyCipGSb9e2Y7T9oOQW0Pp3CUvsN64ad2rxjdhxhX_o_AlQNhxbY-RjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJkRoIheXulO6d-j8NogDmAioConPDtxgojKSJGNNK1Psa3gHCr7aMUZM1M3Mploxs0TSvPA2PiuTjdQH2u_m7aeYDgH14Gs0gjR5lLG2DVwxNjiUGJACoCsM2V27GDhMAJTI4MuutrEw_Byx3IUnZ7GSbm_DJDh6u7Oe4U7RrAuBAyjnyHJ9YVPgRSiOWzJfzDuRgcWHTkZgwmm0nJNmH9WJhnRBgmu8oD3CZOwF9Ull_FGnZfwbEDGJBQ4K6CdiCH3HoDN8fjEeOCAEAwrTb0Cm9otdFdQVCoXOY-g9tTTzOv18jO1csovts3RLz-2TAl1enlSbpKZq_0IdWZmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=iyV13s67lvwqfTssR5DDw5ekyrJMQARUbB91y1OziNc_O-K8DkpQF1c8AJ9DXlVOwr8slZbR4a_zmvx8p2ujBEl55TiiCAUL4VK2ye94hC8uBtN5pJb1T5DYThfaW9sndh0uozWBb65WW_9vi5DlUAotElfSIESeTMPk2THWz6b1_UgP2i9gTf-_mHGY9GFi445YlePpRyMs-zI5XOIOOdr83lrMMtFC5wk4bc5WFqKuyQbHG0aOkUVIlRr3ZA1CHBM_Xn-wMQxV9WluUrEIsEHwRVsbqk_-ZJcSoVayOnPf9PR11jCfw7LnjVWGoc54n4HhoZYHnojLzetHLR0H4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=iyV13s67lvwqfTssR5DDw5ekyrJMQARUbB91y1OziNc_O-K8DkpQF1c8AJ9DXlVOwr8slZbR4a_zmvx8p2ujBEl55TiiCAUL4VK2ye94hC8uBtN5pJb1T5DYThfaW9sndh0uozWBb65WW_9vi5DlUAotElfSIESeTMPk2THWz6b1_UgP2i9gTf-_mHGY9GFi445YlePpRyMs-zI5XOIOOdr83lrMMtFC5wk4bc5WFqKuyQbHG0aOkUVIlRr3ZA1CHBM_Xn-wMQxV9WluUrEIsEHwRVsbqk_-ZJcSoVayOnPf9PR11jCfw7LnjVWGoc54n4HhoZYHnojLzetHLR0H4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PI1tdyKYEXqznEynSe2ACHsdTOEqD3rmzxl2JC7woqUWcIPPNNfL1iY4BR67dOB_DVAbv564Z2HnGw8mD5cRiM557B0Ee69j3ee17kZGB8ttaFYJ5z1BQ2H02_hKfMTkiaVrTmvYgpNwnJ3xmfYJpCwLdSm-Npi9V0uj0jYEkwLsX-82TvO8-T9QzWCJ7-M5mx01St68hAQm5KtWH0n0TEFeTfX3N2wtrjTJVx_jKuTb0HGKHBTrI3NzHKKZnD3CQiQXs7iKDCwXaCpJv3yuXA8tQ3l9TO2QT7Z29hR8BSqYQREUmEn6ZNQcmuIXrgOqsy5melbQdY5BDfj-AqY_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VO8HMxzJWBsCctLvx5tqSGwwqXTsp-a1uILpCuFolVoHjoB5cRQ0gqgpN0nrB-BI2VMPxbPHxSGjQRcJdpOBoWQcTem05o6keRkPJ_Wa96v-YAAmhh4clqw_8Q_p3ZInQ6AjQCXgU701VlJn8lfpuzJO1T-Ih5X5GPqdUyEz4Onwf4ipZKjqgSdZX6-vFw0kv3CPoM_j9jNIG2ymtIeP0wEeEytYvVj1jGnxQEcazgn55l_V5I8A5xRFUrlkerPODst0FFvrKeNPLxKTSEbO4TNQsAOpIlX37S5WLZB_dIZAkOgApG9oWVVSuubxM9OWduFHQxMc_hJYDlngFYD7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VO8HMxzJWBsCctLvx5tqSGwwqXTsp-a1uILpCuFolVoHjoB5cRQ0gqgpN0nrB-BI2VMPxbPHxSGjQRcJdpOBoWQcTem05o6keRkPJ_Wa96v-YAAmhh4clqw_8Q_p3ZInQ6AjQCXgU701VlJn8lfpuzJO1T-Ih5X5GPqdUyEz4Onwf4ipZKjqgSdZX6-vFw0kv3CPoM_j9jNIG2ymtIeP0wEeEytYvVj1jGnxQEcazgn55l_V5I8A5xRFUrlkerPODst0FFvrKeNPLxKTSEbO4TNQsAOpIlX37S5WLZB_dIZAkOgApG9oWVVSuubxM9OWduFHQxMc_hJYDlngFYD7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvOBbOZfBTWbmpeJhPODZfEtupRRRFqUeT3J6WG7kKC9sNB8pSJ6vyIT976TGTpaYw69mACJxL8IrZdNxw4JwW3RBAs0zQ6hg_6ITtrL5qg8UXrmj3ziIOoJvQaQo-Azv6KockadoinxLjd18DBArA0F0H0GUutadzfZgk9XMWbq4bY37HOy-K4ZcL42ondJHJ9skgBs2ByhwkAYhqhwW7GXwvUQGTRTlyJxuhtL-QUpw0RE-ArNVahDoKRedLbJdKqxFr2dMgvlWbB9xx0kpXfGfdHlmiECo434lzNvOSroT5doCMVnFYPHwhNEQM2pB7aZI0cUZ0Uc3FyLFYakvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5a_Fz6mUt0mH2M6SH7cr0e7KP0czjdwgiebObXnVysctzWgTRMXGtrjNG0GI7ySx3li53T_BP80qAfuL-TWv8NwxNpRuV681liXNUcTs4CdKDuqiBt9mStEEro2cAMGOTDyTSdhiRK8YR-2Jlm8NuZwQa8yvjUBHJYFhBycSmqqGi6eXe2zlPsa21wtMmexMdlRa5VH7AuscLZXszUTaejLz9qiraXI_KHXaIEvzOE6IcoVFa5-q1eWKoGmSmETuPG-k4qaUpOHxt8wMkDgztKvcdBATpjesajUJ90BlvS06VlMqJHteZHbu_dp7TSzySsUfc_Jh_iUMK83LR6ZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=Q47ubYABGQhgijM8wJuVrCXLKG3_TUb7pdtpsiCMfvanBEevqKqOZ8RGPt73gdb4KCtvVrzHoIHOiTU5fUvJ6YBUygkDa0O4e1IkaJ1XO-bmOw-l_dCQqW2uKjEgxE_KvCn8K-kO2syQMGBna7oCdVDCekwUv7TJHXZFuy8McLxoKf9hqjJc_zH2NEFCTzCGvjV266F68ob0IaUtJbO943QJ9fws_frPI-nZQgdDkqa2rX-6EowvhryAuX0OZyRR9G4mVXZp8G_QBVZ2WC3jVeOeI-PrXSCYBBvNdEnCmeZMaL8II6I7l9LiV3Tk1Be1ku8_aoBM-riyfx4Ekb-we0aMItUYgQAgBj_E1Oyz_pbGTDndFem2hxWWKGziLIIa1RJtGWI3lhrc6A4hRj3bwtJXBQ34czDC18V7QCrvKKVnoI5zEX0UFe1lLFQzEISYOQJbSqJGvq_5INIV05hGrmBz_WkjUhmEsGnnYPo_-r39aqX19YNAQ7_PivME4Q1yokauEcmOAwt-HPKl9xkVLC_HhmFCt6SJ9CEuDcQ17Ftz369kn3fr6D6TYXvAwWmQumPecyrlRRdVPc7vDS4MeyF1JvCFEbu1-0owKv9HpUN_5yNazYtDjXsgmphd5zd9qMb9zP06n-RQxlYcbcVyAE5G6FYnG7lO8zsn-l2E6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=Q47ubYABGQhgijM8wJuVrCXLKG3_TUb7pdtpsiCMfvanBEevqKqOZ8RGPt73gdb4KCtvVrzHoIHOiTU5fUvJ6YBUygkDa0O4e1IkaJ1XO-bmOw-l_dCQqW2uKjEgxE_KvCn8K-kO2syQMGBna7oCdVDCekwUv7TJHXZFuy8McLxoKf9hqjJc_zH2NEFCTzCGvjV266F68ob0IaUtJbO943QJ9fws_frPI-nZQgdDkqa2rX-6EowvhryAuX0OZyRR9G4mVXZp8G_QBVZ2WC3jVeOeI-PrXSCYBBvNdEnCmeZMaL8II6I7l9LiV3Tk1Be1ku8_aoBM-riyfx4Ekb-we0aMItUYgQAgBj_E1Oyz_pbGTDndFem2hxWWKGziLIIa1RJtGWI3lhrc6A4hRj3bwtJXBQ34czDC18V7QCrvKKVnoI5zEX0UFe1lLFQzEISYOQJbSqJGvq_5INIV05hGrmBz_WkjUhmEsGnnYPo_-r39aqX19YNAQ7_PivME4Q1yokauEcmOAwt-HPKl9xkVLC_HhmFCt6SJ9CEuDcQ17Ftz369kn3fr6D6TYXvAwWmQumPecyrlRRdVPc7vDS4MeyF1JvCFEbu1-0owKv9HpUN_5yNazYtDjXsgmphd5zd9qMb9zP06n-RQxlYcbcVyAE5G6FYnG7lO8zsn-l2E6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b512fOGI-5V7KbPwI72KeBdgI-u-VWldwKSUuXmHcjqbL_MXPNLg-P7wB_LJgDjn44qpYSo_R7lSWan6hvqQc4GnbqBsexfmo9w4zxZ7XLdmT1ZOXL-HzktSq_HOulvdcZ8keIEntM97lxQxugTjRYLRgWmMT37rp7FEpLrvntArAs4hgyOilAvltbe71Om5Jr-VfeVb6YrjMsY9KCSxq5dEz4gO3RJDiNfShr2BUo1uJr9OIZ1TvEhleaH0f16tbwodpWLYOJwSfI79gezKIyAiPNXgt2_gHaEcQ9Tk8HQuQEog0KGDwz6IEWO6fU9hgc8Au1OAzTeDBkSAP6m_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oem9qpJOtXsdSezFGb1gw2DJXjfo-xTc4HGH_Ot7rODoD3hDquVFPUT38cR3uqQi0MGa3Et7sgyh4e9kIG1VZQMVpM3NCIR9J5Cgj1etlj5_AJXYY9ZEwmcDW1dbs508ih0SGrdQQQYbqC3OeNwpJfT_Q6zvVnOWxW6U2c0ywUFkFDpmUyYUGQR8wTr7WmzDDOdnXLc36DkbFjdO0QvoudZRUxDHWhx3e1HjOQ3t8mV904Jmisx8iGsG9gfVDnCl_rkjklt_neTCpVsqI7x3czgrtrl7wJwz6aSrxkeovmH6W6iWAorZ8UZpXcav3zwBD9laj1DqMVJObi2TiGUlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpxoPMK5xe93eWcMpICWYARTqa73n8hxxVpaL5QRu96qAjDP4LEQ5thHCcxKhFjmTBwngrrAyH9nEl2ATQKa7PYMe8NWGnkKqn77D0IgcqQDMS3vElkMrQjrdUsPhwA1tS18bXek5urmolJ_3QNaJBeuk59C-C0fhSvFV_1KqoJez7__4O6Vu6oosv5q5sdDsVpbxT2EPv3_LsOLZT-f4KPBldV40aJn70FBTHvECAcNVqs5Hc5Vkub-Sg5ShaU-qBEc5a5iBw0o7SoqUSa0N8GcfSWrz3zfG_Q82JR5XSgeQWMyjA5mVEbFayNQA0GdzxQ-ZGfhApXfRYFRWviZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJQ34acsS189yaWTHx1mOYY5gJbhu5nxxHGQ1NDsFAeqzLCgK99lNjcZgz0jeIep-xdg8cxT-XWrvt4CTOCwHlZqHL0SWDwLaWEedMpoBb_krfX9Z-_QGG2E5QqjVihbxg3GKt9Se844HUknXYjfBekDwdkRjRw2HxhsNIyIVTHotR59NQgwneP2gE6DhNxl5dUN19nugel_gF4afNhuV2f3VloYt-lxqIeXTkcksGeunV4j_SFkNscHuBTO0HDl8U7p53_ktmxyD8f6XDnNTywFnbKeCyVBa6su-ff-V3xl4lTvjKbLQHSjc9pYCkaYqmcxYcCfCtmxcPOPWVYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGMHT60lXFwxiJ6BYiC1U7KnpCUBUHQ3uUocKZwRAqo63O9LcQt7C28suwii0CiXl0d_hVCzWOV7Gm3uQue0yW8g-LAh8OYvNjN3xMErt38HpCB_uvuefiNOIiO_xLiKIcgJ-NO0ZzzThe9Skk6e9dcp-tWM9L-ucJ_cDFNwqk359lTgG4EyKrs9c4BZ-53IgE0LMBvGQaP40nIM8rNr9fvai1emU95vHA69TEK1ApqMP2Is1h39BkytJhaFWjYYoGwAfWD9-E3-OW2DzReS9HJgv5oprSJI9PJlc9g30nSFJr2RrwByZKukR51KCMQ7JnyV_AFILKawd023uZ13hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8mBkTBzs-Cgph1A_WzXP4LuBYWeaPnq1S9wNDz-CgU0vPf61iK_sVAFxp2RYWOoq_R75ft-9C-I_5i7wHmIzqR53AL0lPkBOeR4nfgLrP5-id-h9hxWfMxxGYjynjegs-ODaGSzjTBqzbgoIo5RLrEqsTPjSCtvKGvsBNG3KknxNVkdMaVm1samDfAWJwEV2hLZmyR_h3er9zOn9gMwugbFCyKUpDk_CEAjwDcho-zReZaBVxyRCmdD9-iwcuXhuvv6c15b_U_IMgejRGPnSsadExUAg0Jda1VUeBnUVP7rU25t9NCQ4YZpvITo8slWLTmN0fnNyb5SvEf2zREzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlEekSHKfllcM7yk4G1FZ8wN4BFLc7nFVTfOZZhsMu9khEMXp6infbqSbISxpISqYgHfMI_lGxLi_9Bi6xAY6fcG4tXYTeKc3blr5aickVrXUvZ95ZW1gZWaUVxMCObpkxvJq1fVrUCAiwfIXrro580WuEwQbTmr16zm3acoT7K2NbOaEJej21ebWGcElnKYbGEXulam_KMhge7u1CNJPVWI79EQ0eLSpx12d_B3vo20StLScfgu9BX6n54zyQeM_ntz8ftkdPXg6JneFNIWtL1OitJ3PGSVjnd6q0QX9FV3hDBvtRKEluj8-azN6QpsSk9p1u1mXukDlovj_Y2zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dH-oJtKIele4S4cI4AmUOh9ocUZ_ZO0orx2rYKJ33cmli87SBbT3-QaBqlXJNiyvKQNncCUp-2qqLsZNeVT3Dcl3vun-qH7jldQ0SIVXUAwhgGSZWLTHs0tIeh4lBqND35AL9xu0_jaa2tj59rKg4azG_4Zq4oxthp6cwVBtgGormAY4B5s8sAhe8C5SYbYd4n83-Viks4OiL88u17pyX634SSmpwBIp7jLdsZC7iqliTeXY3GZ1OmDnwoZ9OCIdRM8Y9LO-CDJMsw9qfdZ2CMuQYiRFNhtVonASPeIoAqyUJB5umKe5SRDryyIMrew3a7xZ8Twk517EcmNqzmjvNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R61qpiPap0R-u2vpbNVVcAZY3pmuak5_4-Pdph3F6LgbKexJgigLMGT5qkwchXF2UEsf9S2x5yegCuthhFXid-ngJUaWDmPvhVBTRAJwbe74ieW5FnA9iGzHbvzdwv4qdS44gFQoRJMnZYRCFWGVJNDxXGp383hYgTi55N834vk0qTpmXRo5TCYieAuuyslVJU0HYbmmUBxmYIdCzEpExa-kNO3Ho_lc8NzccIo86surYJXAOIdqZuPNul_C6XojkoeQILr8JPJSGjiiJe8RUA3eu954nLCtifP7kw32MlbxDgva_kcOuBysyAw02eam9iRWOpTH4sKBgaBlAv_-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt3LIVuUh3ZsjB1Dw6_8ldm3JhYeeXhgrbh_ps2UZNZc8P9Ixlpj1JB8HkKM2Sz05iLStMHecFsFTniy9YUOiboB3bM_-zz4oTUW3Sf5H7HzmEySQ0GerAE2Hb8pMNu5YzztPEw9rD1hHnRxIBaNHdHt3h9Nu6wDXeirsHcyuZav8EuB1uPodOH81kIEb3oLWEeD4jKmFExyyc2oTWPAYwdrAKcom7zVHLXPjDjXI5lwBCj3QxQrE571ggTin9nNtZvg8gmWWI4GFMpqi98hwbqrSAhUupyyVFjeDogh_LA1YKVRe9GdJMs0fghwYcx3klJPLhqU3jfNB2BPDwavEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcyB35bvZu9XHV1vhMX_fAiy4K4h-NWllhkx9Qx5Nd-fS2vcqAph8rtcNgjrmDHxf1nb9aUVfHxvhKmSMiPQSqG4i7lw4KY066B7rYtosQQSd23n_2zpmWCIdt6jHMRoiAckqfjcbwSOYVulmYZzyNyx6vFWaWCdTgU_kjUiuRykD4A3pHBFD2ZM6Xw262veA3sRiDOubULrK5mqBMjewq9HX_d7xAt2iK6BXgOInTKQ8AYGctlwsUqputT2SZOCvFUqU4SVfQqsheF58yFs7XNP5rCAjDiLXwqqqvYiVdfvB8CkUHlwnboA1sOg_C76SuMdIedPGP6x02_FNlmjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiKVeqflHnqx6S_JyknpwZnblAolpZ_IMm4LWD5nC9ZB6U1ViZzpfPtoCuARES2whKSG7xkvHupoWJJ7nngqOWtes86q4iaHqpSK3n48OvjWmnHiz8N-u1ZzrnFtXi14lUsafrTfrqCN7K3SJ-rXJD2p8_eTbkVQXTkQNXAYmRpGkb-vyaPUQvimyIn94m4Wp8sQgsfr43Cgf6Xpe3wdO089pxZUUATqgB40Gvah7O2MOy4n-DQrLp6uv4g2zU1raLMTFTHrA0f0D7_iLHEhjmkCc3BjJjyB8m7PSzZlHvceBqktxKJ6SDHkDaUUkOTpXqS4rCCJr285NtkON5KuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG0ySUQPDFlXak4x5S0Yore-8E57wvc5oz4Y2nzEXjsc0dUHmlG5L87KdgOicIDckR4otl4fL1G9LEXB0V4JuBoru3hywGV_9h7ytUlWxS_rXYJLU0PQuGYRcIW7veiAfBWZDOWuT3x9i8fn0XUK6fUsZ9gKZ92EpiZyR67x46yGMCLK93Tk_WZ0z2aG4mA352l3WcwmzgfbokItmDJ8U71eRsItqGC1NTojWlmb75IyvFSD1PAX32ejIXDSAqRcX-KFBroR-i75KHJ1e-dTSLLJBQd8oNSTBkV20EE9CIC4k6vSOcazr-jFYke83Hgar-6v5ICl2JsF8r5Vxuur3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8cdOqqxHgPT4CqNs01bxwU2J7mfRk842DFPuSUTUS8F95-InmHCmV_D9IFEgyK8Upfnj7yMdgjlcu3NY7iE5su3xZ-GNYhhZKIhoV3LyaCTUQPgvBSXIENpAnWLPrBUXvO0Tnih9MxOkUvRvIcfK7slCfnCOuu_RgoZ-Ms4rFdVwHOnUxD3TiJQ28emZ4dxMvwzRzxTE1aXNIRzs5is4z49a95Uvhh0xxINzh0C8_kdP0M-RyeTjXJ0YMQr4RHKBJUjWBTLL_aEGkva6AbhcLR9x4m678_Hxa2jvOCZEqbW8tXTO3EqabyfpiHIohcq7Ihi23gSdCuRnRUba-vx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQTBZbd_BrxGpQkzRm8JLY6Boy67c6UK0DFRn3OYcMwzsneouqGD2JDXfWwc58RFm0l422hR4KWQB5eycrZQh1-sCuExvt5pOI6vSLbetmiUV-pR1v1RWrrvdWSePZTyzx7vVYf52Odh_oihiu9wN6atWMiBvoiHfXLXArn1l-vGxtkRHeoZSuWEJe9WvED8lqXQLKyp4vGi8MkaUGopYEqySMyec8OiD_KPAk4afk_O-oSYvCFFvTghiwjnGfhzEuBTFeHdFsPLk9Oqkh0AeT1YPh2zFq-jPQvspmsSQED7nn-sAw4qmVfGTLSV555pwSqyiF7WtPmJLrgu0qvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7CdIG7FtWFB-sgKlXwG_deBgO7XBCaZvUFjKwWOooxYWtcLm1wPWhjHH9RkyaOgBDpBYDuxcfC8LUN1eoklXyCZa3hNOzJykNrJnUOp9cZWaeDzTDB65AW-9G7hYElCQARgGS3g3KmUGMabsTNkY5TPIqggrXrC5SrDvEH1C507hWTGPJr5sEXWF9Oa77Y25UQ7APEwDp53bgTxhQAtiP937hqlKE2gks9ZtYWPmuvW6f9tdRAQicXygwPslXcU14KPGnuS_z0OZrZLPL6vM1uhoFGlpbSzEMoLRGYn_6V2-xuTieEVoy9TwQYfNPt34SBBVQ0mTgIvoXto-9ZJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3rb7R7hhDXLy9Y8Ybfo1oVKZLRgTEMoVSMRHAawWld6FEyIB0EUIzMGXSeO22434eyRGE8XumkBh0sw8w0jsE14L2huNklupyLAMdwkVYChRvRCue4fna_nst9JyhPuCjgsoc78G2aNLo2ESWUXaKBh_XdAFGuEGc3piwgzi_q65f2DYSgAl72f3eLuTFmvGgYAKwu4m001VRJpA4vpIjfm81nu1MEnBz001mjCk99ej84OtBYPvVviXnSxuE6xWGLyEhtCHX-UDb_A2w_toVhZZU_2mb93sK6t_wi0efPkzqJv4KeFaJHSl4DM8gYN3hFZfLSqEL9AhHxsqOm2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vct-i5wFP8bD2Z_lRkGsP0EwnTss3ur7snb6IWMc-Oq2Tk3MpHE-71MjZJrA9thVyN-NbmCAoTVcfDtdSSZ2Agfjnio9YDeFPLlbuZGeuevO-1ff9K7wcOzDA4TLqBJxNQLpTf1kR_a_PWzXykazeb2p0HkXxr8iCCEstRuBmhbrUzuRMwCRqp-qW_1QudNbHRMM_gQm_hVAWKj3qGDgmaW9hS2aA4IMnN_Oxe0TSgHYnoVd643VyiII0N3URuyYgZr9b_YDtuiDXQLq39hPxf_WC1YPj2eR-NSrs1g_8kUxm0KNpUvwtNwn6IZlwiQjKhS51R8IrMxTiPsQUXp0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI4_h7lSGAvgX2ctnn6sbtbWrkaSydQR1lt-dmdHMXiOb6gzfEquYSvSykT6btRqTHmGWcBfyl08LPLYcS5BfTaFZ3ELRqBTcXiIwtTjG5TB6rjFcvWLJljtAs2iQ7lRokYlTsPJiworUB8LR-L2c8LR7xl1ok6tXs-qsROVTLWuWSEG89RfFFOjU0QVjnXT4M_9LofuAkmDNWdCW_TDPNDn1-wUmK-mY34sXUhSJ7PygWpKQY7KoxIPT7DUH3dXv3vsd4YRFcuwPSzW5tzPaCNlbwvaG8_GhaE5SDKr5wz-iXrZt8M0k77aDuTUSK6m9aAi-jbBRR4K2yX4-Ut0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVll5NXK4EzpNuOgkDLu2R1BIqZ6gt9qvQUUWDBPxnSzlS-OkaZxf5fUSsAZtPP4UKvGziMZvmVY3RMZUHuLaiUlk_GIVjHUPqqA2GDtg8Axl_mbSz8kLpD6FdFmosg9AtUGM_BXOoWkOf8lM6n-ctNNkX71H9ki3It5fF5Dp1Zl3jHpW5qjSreWJHmMY7-G2xVXNnx0xmkJ80EE8z5pCuNID73AyeaX68n99ImLvEoTnR7Kgw6_ddO-l3wtITWQXKNkvDHE1cE4U11SsncpPCHIwFkw3digb6SagXaePtTQkOzSeG_jrxf2AgR7vgpGOP_FcV6jvKCEv-1692Sybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AKGd6EyCli1wJdXSqcL-yR_OYZDgfSyB_ATw56iPMYOgp0DLN-spHd9f1rs8AEL6uT6DWtU0Qk3xV_b-uVNb_p9LMZK4EEGgH2eJUV1dvRF6fWfEkBrJkaebjBTljPWlBl-UMiwB5vf5UFa6Wqcp9ZZWFkeMbvsAYISbo8VphJ-8IpEgs7zVfHORMp1exn11MJTHxvlv3JZRBSnjwK4UVw2oy1TIRKP4qvdwXylANIwABNR4x8-F8BM8RhjErl0sNqliDfgcdYVm7QazQuBYcL9HyIoLV5P8LZxtd0jV47T82TdQbQef7TCGQpBG43KH-2PdOOjanDxoNvaX6GGR5V0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AKGd6EyCli1wJdXSqcL-yR_OYZDgfSyB_ATw56iPMYOgp0DLN-spHd9f1rs8AEL6uT6DWtU0Qk3xV_b-uVNb_p9LMZK4EEGgH2eJUV1dvRF6fWfEkBrJkaebjBTljPWlBl-UMiwB5vf5UFa6Wqcp9ZZWFkeMbvsAYISbo8VphJ-8IpEgs7zVfHORMp1exn11MJTHxvlv3JZRBSnjwK4UVw2oy1TIRKP4qvdwXylANIwABNR4x8-F8BM8RhjErl0sNqliDfgcdYVm7QazQuBYcL9HyIoLV5P8LZxtd0jV47T82TdQbQef7TCGQpBG43KH-2PdOOjanDxoNvaX6GGR5V0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=ksrwEcggaxj--YcsZ7dQpDwl9MK-jcmCIRIj14c90rje7614CG1CgyXmAVbwoIHGjeg_AVSOwEUqCkQBV42BKXslcLApvXd0ClzLDJWhzqrtg6ZFwDn-pcqcp1temLQyiE8NUPLdn0ChgJNzjz_axDurjGWpbN1TsGhoCPnCu8LLa9uJhW8ID4hd8X4X_WDirXIPUsY0XkZZbcm42TudWj3Df_7G_xccjMuJ827HrUCOLe23XSyGkg0proxo2LKb8G8RZiGx9B6eK32_yfHRRN2b5CE5fOXl4zjhDdotdDLQPzsfqAIB2k-nunRLYsif1m80iDBzM_jsL_QD6fXIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=ksrwEcggaxj--YcsZ7dQpDwl9MK-jcmCIRIj14c90rje7614CG1CgyXmAVbwoIHGjeg_AVSOwEUqCkQBV42BKXslcLApvXd0ClzLDJWhzqrtg6ZFwDn-pcqcp1temLQyiE8NUPLdn0ChgJNzjz_axDurjGWpbN1TsGhoCPnCu8LLa9uJhW8ID4hd8X4X_WDirXIPUsY0XkZZbcm42TudWj3Df_7G_xccjMuJ827HrUCOLe23XSyGkg0proxo2LKb8G8RZiGx9B6eK32_yfHRRN2b5CE5fOXl4zjhDdotdDLQPzsfqAIB2k-nunRLYsif1m80iDBzM_jsL_QD6fXIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa6Fho8QsoMlO2LhFrzdjWkmqH92zxrJqC0Iyq61XUdNVKjWOKJGAzp4JvhEuhUhltAvAFFuufvyh6I-zPI4lXwI4QkcHaPSDmbgE9O04xAD_sRP8yjA9ZqosnjZWiYHo-wRw2TSSxTD299nizx7fS8FVkEf1raVwsoFoQbHl_8exaWcWWVqrqRMLM4cKV6XaMNjCPCpIWWXDiVIf2IcmRnUlSQgwTGFuBEWqaqYuXG9pli8z75O-EdwDNEMeL0eVpcm6gHAtyO_c55gs6V8DIKY6VtkdJLAGJ9CnNB4xLS8DrsCW5Jwm4yI_OKkz7X43OTu5mj-jGIG400Sg-AQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjMlOugHQEKq0PFIL0LtMjSAw_7MDDC0u2XW9fxaJToQnmegm9mi9gA4dQPpqOIzYj6XmAvk8AKDbMSBa87skX6vEakT07gbDOPi0-YpJd9kM6v25XU1AyeFBbso1hW-8LHYnSlxJVzZ4jH5mQ5C3ZZJ_d6VRbb4VffjnzFDeryQHu0Xa9OfYKuzZvaXUi7P-i508sxu8C65uoRe8QYpGZRB5wH3mCAByTOPNfZrAd-0csn3caoCWAXAD01cGiRRUJRZViWukboMh6z80rxpx6Q7zjs21Ws-FQDj-taMnCu_P340QbVdk1qseEzxEvmNxESHBoOtxnTPRbcUZoMlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGhPPaUVXKJ0bydK2VAazrhzHuNIQu7iVPQjxjsI9U-BOTJXdPfD8FmbcGLUWjDOJorJjr2kmq5t4Gp58dj1mzB10NMiJp2kXkmGAzGzrpRHYRg89jWeW59PfkzNWyvqnBgnoqfPP49Z21Mgr7ef0Um_ZjkjMfkV-n1DzEtD1OnbpJ3t4FfsCFLpd0_9PDAuVzASfkDL_6O1LZEzDL0-bQBEo4Is1WyCXlep-EIQ45xyx9NZsOqbrWEa0xW-8JoD6784LDkMCvfiKXUDMndLLjZ4XmBbOLiR_gwGVaIdMVglyiKnkzsDIC-Un6fYOBnblObx_hlcrcWzI2FWXC9hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhR6JYZnncyi_dU2yJt54tllBcWWm7lPszIMvJy9EGLjrmvk_cVT_DnAz2zqsAfCmAx__aBRPCs4C8bhjTQL4aXbI7Q2alH8edZrZQchsz6gaC5iSUwPsmCYrza2RxAUhiVyWFchB5gbERyTAgEHeAhAkO-WTrb05Ij5s56nkDJb65-TpuNRTMuRzzg-9qc4FPni9eWzCf7a6wiPmPUo1ugvx5K5-h7kUFdePnJILeOKN-9SRbe4QPd9TyiQORnpqM3Vcwu23DCzRpJag848Wj3OilNU6wy2EV4Az8Xw9whopFWlrGR3YiFbXgkPmh6lHhhxe_ReO5klU10WOPhMMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpWxG9phORumHq9q006hvwTiO_rXL1v3oSgpWjQrx-zzliKKtLz_7o3igDerJiRUTSStZsictIB_2ssVS16Wla3rBsv0jqbLvUS2OaafRrzc-r0O5A__D76ba_43xnq7FB6yZKh-LxClLgYqNRI1u1zchYyYgmRs4X1iyQnl8qbFNrtMVOzuf6NmVgn_b4l7ITUclLBMSqm2LA4rwDJ_44hw57f2jLbBlko7aSPMjXWWBTj5qclCMZnbO-FqMv9hdWOqkEKvkCs72xKOn-UiGR3X4YecDEkZfxW5wDGpLpQ2ELrgofpPCUK7Ay3eeDJYVxe3kmjOTKED73Qf99JEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxQRzNNFAqXFjo4HLbSJaeRteEB75FeO7gOTEFhuhhXG3YTo9Ipga1lIs68AEaFyXct4wqF0WwEbPaWmyMIemjSjKWzb6R7SRDPJ4Hay1VW9ZGV5OavNDabbhs1UVt8q6S4lyePWmDYKhM7PBbxlgKEWWVWqjqyTbRSNzmREbitSTChjjkEYQr2DdPWQjIbBFHN97lk_8NMAi45ucmjckTxOLjk7w8fV0Lp8v8ZwhJZLpm8NoR3fKPLxLWD5IRGJfScjrphSzwHDpU0oV0USJBCFSvd8ZZ6W9WdAApngnOSfikjsM7TmOE_s3qKMSKaQiGsQWOsRl3fKuu0uqnkSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiptvLKxsMOmP41DRkQY4cgKDwZol3CS-P1mYEQF9ObSvpUooYsT6bePygFBCDFvSyB9qZy1Ccy6X_kqzsF3L7ITOa-ikMmzK2NzkF3nJ6zPLxE1A72fQWZzU_FPZB_NYw3toT-kUUtI40JFpg372zCisxrSwwj7fxg7aC72-uCH9DqyZ4Q5N2jYZ_zkJxspgELhJMOQctFSINAj-MZ8X1sBXck37S5n-GfZY-mRMiOEnzdxzt38thrZvwLs-QO28B-iRXMbE2cCZJpm8_T3OvlmtOgP8tEZuzAeDzcsa7ZY4h9-IRb0SvORInwSs8mws7DQe5-rNqZIccOC9XvTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEUCLVOWwpFbxzNI2PZCfBYCT50qFumK8mqbAOVOEfgDHaarvdoZkNExC1gbIQMo_XlAQAfD5BYZAbqlI7WtXxpqF_pm-EuHKF8DgTC4b5XbMfegycYlJ8IaOTbkR0b0uTp7xrUZAsfhudgV5YfgyByIhLixj3VRBMdiIfNsb-ogDYVsWQe43n1SKOjwNpU9cN8xm5v2h-8i1pQ_fCzMz859l0q_5AWiE1fipSZcp6-1uxj36SCxKkxQTwfogMTPqhYpbJTTckuGIgrlo4_KLPm26GW3A0ltbJW7RuLIZMDQq3mzIoYTON0ILSDNb5wDEb0Rx6N1FUkHZrDp9MDyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC-3ABPG3yBQzVa-Zueaq-ALnGEvuFQIhDmS4xiBtkWqXfvdZCZ13n98pX9z-nFlkup9VU5gB-cjLQyVdlt8pmaXLKu0XFvwJZxNGy5Y_FbaDuLKKfY2gjmRh0rZ8BI9DLdE2C-DcGj0S3RcRqUlVevGXCGsQQM-f0SWU0ULr5fs7GtrZiqd2mrClSwan56psl_2oxanXNdksgiiOrxa4koVJRSnQ3qW8-BjhlYCmaxtEmwaRQP_A-Fg6tpiuAkEuVAkLbBkPca3iX11tZlCviAMM5TCycjK-75Ks1ujpLq7RzE3lVh498PjVb2rnT1T3AI8Z5U73RTWAUed3KYP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEBbZ_N-GVtSv_TVAZYHdR9Y3gkhZEMkcmJmeKJ2ryXR1RVzXvDS9tXo93mWL2HzN4fHRnqD6Vt9FVUsWK2YlV_sq8YCoMCHf4d9BKQEyKY4kHOtpmYmRVgOtTi45uk-RxjbWqYUz1tBVy7atH7JtV6oP6Ebh55a-0JwDBzIBmzbodlTseB5zfxHmc3ziOe09soy4pE3pB3WkPLiK11Q8js_AjWHk-PYN2Af-WuJGaRM9VZ7Je199-T-7nmnsyd5BwMX1kTylKjrdEjS9IxtW3E4fzuX3F_Oa2y1O8nEkrE6zBQWQ1BqHmyyd2v7YdL_bWed9XILicj1TvjUnzCSGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=dYD1jfQJAMJjAbsGObImkjbFU2lf_XRDK2FtIHHu-90AodYBvyzPQ65IT6uHLB7tV1LwrBYeEt8lq2FlbLeDuO8MTrcXQGq_9yjTGOR5bZ5PzOY6HfDErvNcDZ-kuXmiJPji2iFxR0KKGeTs_h7ZLIL6228CcxH0KW7P53SfpoAMlgQb5f7th2rDshdfpo5n4objCQqGcyDAeiDNCtFeOVc-nfwZZ3db31NIJIGNxBFzTSgMMaui_cv6wrSxQ4Lzn_uded5x59RdRObTrIcxMLT3XCNsy0eBAFJaRNtWqY_BLqsbaZuY1LpqKPvQprJLi3mv5ICqVfnN2RkfJh5_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=dYD1jfQJAMJjAbsGObImkjbFU2lf_XRDK2FtIHHu-90AodYBvyzPQ65IT6uHLB7tV1LwrBYeEt8lq2FlbLeDuO8MTrcXQGq_9yjTGOR5bZ5PzOY6HfDErvNcDZ-kuXmiJPji2iFxR0KKGeTs_h7ZLIL6228CcxH0KW7P53SfpoAMlgQb5f7th2rDshdfpo5n4objCQqGcyDAeiDNCtFeOVc-nfwZZ3db31NIJIGNxBFzTSgMMaui_cv6wrSxQ4Lzn_uded5x59RdRObTrIcxMLT3XCNsy0eBAFJaRNtWqY_BLqsbaZuY1LpqKPvQprJLi3mv5ICqVfnN2RkfJh5_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIR5WcZggU1ecpck3TWe5LzKTRpGjNa_LTAmxrjPfIA_vKb_cH7uSC7APx_XkadMZ41hDWKH4pyn6FLC1DSBSR9mVTpVp536OF5wwPEz9aOraWygBf3ItfhW-DoRMw9Cy10_PjmL2pOyWQmG5lUwvldasCftxVzprBweRT7eiYQwrH9WrZbAH786QPEBKuq5rF0EWawRsaSa1AJZNEYBkibZpy8LU6lp4oDs6omtBlGKi3glTNM3uI7G_SreJsoreJ5J05uT7HToGLTU8IUGphpToOlG5_aOLQN-q8Ab--o8B_wUMoLX9GoIP0L3TJUo7dzLnHU0nzag9giFNXTUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7Ri6NzfwzetrhVs3Ce8f1D_NZJBfhdOA1zu8kQ-4bfbayVdnstVFmlCBAFrkQ4Yqnuug7I-ZRR_B-eR5wo_psMUt130q4gxPUb9QHBDXv7cvjzaRD9L4MCqctuTzTPl9BQWPhLLhroRtyxZOI-uDtPaO0NTDsV57AE86E0lW2QH8mYIADkFD1mC5_gvgYHJc0IX3v_9u64rA7uzo1VNMM-2LhkDBCVfq0ym1DHOTKu3q2M_DkPkwAzxcNiPsyeIK_Oott7Lrb11UNHnjdgqtDdc9N2Ahg8BkJeY5T4Kb64i62meo7iBxScB3tbbq0efgty0cXDp5F0jJHgx0Bwx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdSyqRMjk36KQzO2u4yO5SuupbF1lW89dnJBv8OiLiLoIzSpXRD50LKilN-UWLKDC36Ippre8DcmCt1WfsKkDCv4jW_yKvPkCtUDnXlO0vXNy9cvK4RyBTOQ0vaz2RIYVng6NwSBjfJY6EuxBM8bqLvKfCeXyCWfrDmqHAMKRkTpBZehcT5LT-BT24nRQdOxujbcfhPyROZnNMte7YQAdiqG8MrfghBNqkuHa3qwyumZyo4gzGBo7cPk-zZoZSdhqPfQ9RKYLSwGIoLlq54-QUHLr6RtNcvTPHOdD0qw2Ukf6DwvAcAsRg3q0JNieYj5xLubou_rsBxtdAf1merfaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEFzdkar3WcKGQow0n8MMuqi1fP7tQflUcQSdOW5OwI2tistwJfy2_rES4fqff4WYL9Yr-DveVD80lsiJIywMMKmP0s2J1nX7O3o21l_AiLj1Sd5N_2Tout6oAEiXLMOVCrz2_qigvCJIZwl9vUUCZgNeyId6rHZF2SGjOW06-Zbw_Ng-3vordxA7slg2WN07opqwPSi4wd8tCC7y6s3qDpSrgorQmN1ZTDcYxZ4FVXDVYn8XZrc74fZ9cVQFPRHbvw3sGhc39vItMNKkGfDRnmYFbZIvfa07zd4D4Uw0AvzsruvWtBWKv_po56aRWpRzfZHbBMxifBv-DVfpglUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hydwu5ar04RXvRdrluhIizgUdGCAxnR3CWPpesmGvHVQ1QTXYiyiZGu2C2bfo5phMK3uW9hCqCEisZoOLmnxwYP0URHfpBm5wwHWs5I0nl22kc5jEMeV6GaXYt8DWuWQTNaFODTpzCn4Z0j5vtLHjpaJAtdFUu2iDmxp23aOstn1bTXLFCujW6auf2U3f3BF_YhSRgas0ZcnBgFQueMl4KmStUYODsPH8zijVFCNMdATGPria09Iu_HeFQJOmGZCijNWdtNxemlJpIl_IbmtFxHot8abm81Szs0AK1E0irrUBMZDQ3LloP6kJaR8DRJeIs1eEVOAxuJUskufyOqgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqRmr4RXlQ1tfHK9bMtuZfKgPbMG-0eeP7pY6H0ctCbNVjfpfsTvYuIqex2FeeeNMcyv3UIDM15qYoPDc5VFkFs3dDKBQ30VeT5fBS1kCKmRL_jQwqPIB45qxIJGmhLgxc3VOVUkn6oXsS4dEf0krCLMKMfvb2yd10v-pROM7r-t4WuxIAegKQzo9nrydDTr6oT0bzvBo6KVVdMmEnCimJ0VjjceIHTXPikm6oZGFbUr3FLL__dUGQwHvHg7SkmJZPJ_BGZefCI-lZgiCJjwNf8v8sjR6nsbkx_vvd8ESu9LeSn9EYVdlYvkRYnr5GduO_6OJsKb26WFgUiEJqjpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXNcvMsbM0PNukWJsZNd1OMtLjluKlhUPhjRk-XvMSC9dp9RnPFBVZcjMpuWv3eWC-ZN4KoGWEmhoqhMwf5kzR-iZQm7ezTEicFkg_OhrqvZyQNg5fPbL-bLP-eg0W4sgAhx2jQRrC-sMJhVHWWBKPb7K0Yjo607rals5bI0nXlWvnVE_mL3I9AKOoQBDsWUQ9N3a829Sp_dRM1G656bNGyOPD77SGLbub1MjQwLQ4TIF0Txc0S0Wy3pKkEK9T2q5m7t8a9de2rH7fg_HHH3n86xkBZLWEp-weFZdZpa_PyWJp53JGRbPlNtv3ndUylJyeCanQ_6tf_CcTZAD1_ANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyQ0mJCUyR59BqhwhLC0zi7hlcUHqBzIrxNUzkdkExFpewvhnn76wlL0_4uO4w2oMHtl_QYgTP7JHStA-b04CLcp8-6yjLLhA5rtmz-Y-6dD8aboCurWug4LsVq8C442o5luc7R7f5JQMzzZkI_7b2KrcC-O-nWiLvmqMFwz7qWu5rYnrvcg4gDHbHewLzGk6W1OI5LCBHptBkkuX9BxANX_yZLNU8rmeE_40iiQeVE4CUnW831kzYYMW6UVFBWlGzC5ftwSb7PaASIoFB_seY3nT6P2rDT9vSGQ5NdMu0I_YYpyvJQ9s9yiDCb757zhiRfYIUQNltEffOjAecwncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTo3eu2Qwpw0tLQcEZh8rzgCUJk6Opd9MzNT0Vst86EYTmcGnufX-FgJJdA8hgVhllvv1AxXbXDy3te5_7AmTJTJ21FT-XRCoe_qCajRSsx2RuhPNLZmpudISugFvalR1dU-jSt_N8v0pRSwkIcbBBAX2eIiupWuFZFI0GEZZTv5LT0NTUWUm0W27yd-MR4Q6vKfTb2dgP008n0M5xTISpF9J1Z63OVYH4RP8s1c9-BeVWS5ocNzCEwSQ4VjN64EPPR9iiZcFHZI2v02a-gTQRtuKJn3SvP13MBALJY4h5NPcOW84uzJ8XKZb5zR5STD24Gk2m7qe1kNIbNm9BL6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doRj5-ydKu7ePToNdLHlJNkW-DzPbHYi0TQEZF27VHCg5BpPCdeBBpzdaLq7YjB0zeHcaLwz_qIcAa7YWyL35YfP2iaBjWqlCwOYsYNH87MleBuudXmdVm_BRbDLqcQeaJskqWPdD_oRJx4C7WCXdNH7O4ayHCTNSJcLnopafdqkK-dfmR10hztDE3yxZPCutTBiQzGFOgVjxj-5GDpQ0waJUAzoqDvk0q3gomU4ZoLXhXKTBsaqHuM3WZJbYldlSiWHJPQhtOWPa526NrvfcQ89qcAJ4p423jxKEROK9sr7yVpsGEcg1gUIIXPcwecn2UNXf4C9tDzbmdfYMkGQtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGlNXJ3ms_8jBcGJLKjChm4qXwmEhLMIw-xYJxRtgEpsy70RmIGQzQflqKd28iC0kv0KlTu3XJ0Af9TZDvwr6QjyVpFaDXhaydBLl9qfyFNFgmUnAxrCi1ABxFT_uwo9RjiLyfMdsbhoihUN6DYi0Jc5bXrZtwHFxMDq_L2nH4Qu_yuZfZvE5nJeBTvTJbKvDdXPQZnEbwn0pQNMsOZttqk980BdkplI7FktYmrrrZxaiYjDxq5DD9r55ElTz96NQjewa43ubQICokHkbsSc0nZBv07nlbQTUiU58YlfvDH8ygct-sMgoQ7ufJ9ULCawgPH2DoZ0bNYKPadnpSxthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0eCbdIL43xdcT_1sRCDbsaeJHEuLyz7mGEHsPjB_OPgDXF4I5H5xwYkCY3kJi8bL_mpbqopFn01banTZRa3Owr4Wfoqsy13DYyYI_UttDYw1WOd0CpEw2ljVG3UspQguPf19Nm94tFDvE__rT7Rurm_8bYsCTI2oMzyowfQkqn59kkr9ppYidhsYMTYz6Z-Lp7kx_9a5R0o8coiWTRVfB_zfKG91WsZqsm_cUtQkPg7FJ2-l4h3rUZv9vbZTZLQIEs-KUJzzNn-0u0hbxXbhGd35HD6Lqr4znDFluUVi1cbHS9qK7e58IJ1dzoo69y4XrxsacZydNd5JPn7GVoX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRM9758BpSEkoxuE2-fvjNnuX74js9MIo9wfCYEMqIHLf0ERqHlZ-SvbWj2OlztxcbZ3pdlqqbr-1Du6MWwqxHxtUUanENOWyaRoSrbDnMVoDvjxemc5dmsxhFfG6UCIZAjygjBcvtgk43tIrCFqfi8D2GUCu8bbGKMZUIo8V-6xw8gRm6uhoSvZVLuYVZIdDfISQcdAex3ElegUmbd2wZQidJziowIFxhh5Tjq4VW-1AI4B4WKJGW2RHk0mM-Zbc4f9V_ctW9OoUjojjnfplb26QPGIUnCu9K3VO4eT-MWs8XW24b2Zjlbfvh4upjc5GSIyuPXA83L_HEbc57hvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MeVulm7D8-72oSxfPlSmF7psXkYiNqjbdRY6ZWiBCtae8Kc1n4ZvTOaeTo1dITXG6RqrcyQ21iXyH8ZXFReLR3-UBFbc_iS6olSgQqI4EtPaEfca-DNKEukP97IYL7zxPHdE9NKspxAxQPNoCJHwI0HpF6VT3yweYwa37PZ3qSZNtfhu0XJn7xrsNpmoOmqC4wvqX8_yMcKJxpvaiOs4caBN2vr9-D0yPPhVXMoUdkjQ2bygqAUaStXoNBzGAD3dMV64ptajNFZIer4BxS5rnSKrlNI1Eb_COptv7b4J9vueh4EPRCRN1G6qOwm3jgkVzdzTVQYZeN1Bi5J1_ILatQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phpJ8RXcVQoNyBgIX-Reni0D6Ve3Tp03qNOuYj5CMA--p0q7JMM5M9XTV0WSPaRGcOyE_LZlTthM5LWZnKqE7Medh73nEvHB0ER6e3eNXSROIs4JxYPo1gYcBsNps7ScsYiQBNrHCE-30BfwwFSsNBJNfS9rFwDAVtPsRZ6KO_RyrsGv_bvCxpKxJ-0pebkIqtayR7J8vh9D5ivR-HK_XPdsZg-Poj0xOMPYctd9jZr9rWN912kxTo25N6s0vVyyAUjOPyBEg5u5eneFGKSI3yaGrMrx5I8kamH0Ju1ZV5_YS3sO0S9lw-_SaJUU_FMswjGJezNfxIboLzK59cq6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3Upmf-xhi7_zGqCSv7-BiQDeMRCwuB7bdbPotXemye8GNw1OBFpSTEUhClxvmZLWXDqjsOBudkE3LyQvrv3DPZdArJwnH21UD5Exrbxs1o5vPw8zNge3upUpqGsvX6tYaSIgvGOk3H0QE-rOhcQ3iyq-M5GqqN4Q7PT5I336EQa-y8ZmcZvFkn1XAWgjn-xYaTYP_QxqqSTkcraAjyNYiqokpWxrY8qZyXQCeP-FSGkwDP0FY1rzGa98jPmwISIDHEN-L2SNBOHCCwSFMQtl9KzzS3LtwthTN_fSEDBF39hP-N8C6Os5wfsW7CnofEJwEAjn-BBTwwqQbgvFeXf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1R8jdxawXPrUhK5qE9YxoCn9365MjhNRif5I1FNYKB9kHTxqlJlGTvTRQqiQMHpL_-44jaQxzT2u8f6_Z3Mlo7d51F0EYbp4_Gy1Qasnktguz0Xvnl5BtGuvokgu8UCAI9LYYO7kB6eMzQiuLgy6cCm4Pqk2kiIm9mEzvqAIVIUvh1RrvWp7XaAwVSyOKOf3uh3wW7CWU11e_BNStsKIQZp2LCcXfcTTCeLqaU2ujczacsRuYOCjFKpwGP4b05GOrKA78bL1r9dZtiQrjCO6rg7YVHqQTFZ0q8YePkXKOP8GrLv2kOKGJXODtfJqgW2W6yxsHqgEigYOEEdvVfieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsBORP6P25MFF8SOrvmEPEVO8HimXdFURK4A9l2FD6WZWcx8QCxdk3jgwurE_1UtaxN0IrTQDsMnVoZqTTVeqke-HG4W5mJ4GxLJus9JBCzMtSbKQx6TLjUq0bEnvD0Uew2kzW4t7TBKUUQcaFn6kUMM5CKtvb5mAku0MpvAxm03znz_TA4JdjWlyyI9vgFe4-G-uvC-Hq0-9HNqQoySReRu3sYz32NH1djsK22sbv-bWClet3uC6wRD9wZ4X-JdDbR1P6dh59CFbNYd-JG5TBMvH9dNI1K9VPgpprqdobX2AEt8HQw7UqqeOrQkoNQrzEd5Yf0Vz3-5QYAnASlnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTyHwLYbFtqMrnulUZEfI-Ns2yIzkJlvPRstupsdwNaIhZlw6vKINmH4G-uMYSG72jQyTAn3eVTtglo_V_5348TijIyoT5hZf4T_UgTKmNyhJ0QWc2OruoKNHtGQJZ4rzM8gncFxIZPdYJUZpvxayDOTNKnEOA7dwd5tQ5wyyB-9vRpuTfZpi0MnG-5PHQhA_3H47mPhuoNGP3OCb_ll1LXxVAqGKZH-w8tNORG13QerctU702WnCUtCJ0V3E4wndERcBWFpDfIwsckg7veuTU4fVeBGEez-AtJOx6SQ9BrLeOoElH8PVUCMaeW4GUvnIIBXirtp2qIK7PdRE1siyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZoSMCBwyO_rHzTjtdH_PVV4KFX4SLGFg0LKlOLhx7vwdHI_FVBuOgt1NM6EGBEzb8KHq4fzNW1O7o6b0X-V4cvph7WN5yyawoXClwh6ENnHkdXCz224M67dNIpwbZ864rHWGzODJdSn1hmBdZJhMBwHJXWDpXa-eUYkqOYbIjUk0ocnigV_EP5IQfkKLJf2yZ8qupa1UuGJ76hKKbl5sVhqE-4cfJ3GIAjZpVsx87mW3vCCcbe12r8yx9ZDn-hKp3q1P4VJdlHgcWdfB__DSomeS1B-ENQTtdCif9LgtCcAI64X15egkhLkdc_YF-P58KxyagearZPFf_bKocTrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voyWuqA488F87RQBU-VE8YyxGw80j1daKUwUTLT7zsMyQo5qVEGtpCFXb5ZgEakBvjRSORn_N28wZKKYZwoP0oRpD9Z8kfNBJNltFwz8b3idYZFisMDEV_WOYWNRmJDQvO96DUjXgmEkZUutkUCBDS1RXIgwemSXyNLoUDKYQdjSlt6FXrSahOhhC7re1jZ54iDXnI9bHKF8ddOp-KJfIwT9VE3PRjAhaDEWsxPnQ9aYHjj3CPuER3uTNCYzTQ6SOMTNcCDMSdcUm3lMghOW1dFsJ4iBGF4xB3q-Rs9Rk_D0XIyjxzTxEmAM16oiwDoxAVq0R8BsafujFHTdns-lFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOAORrGINLsuLhqI51mTg2RVkRmDZa2_2y6DyIYrIA3XcK7LJEH2HQ2MI1FsEc128aFxa5i6Txgo19qjjqISWBY1zsM_VtKCcAdmFitk7RmZ8nEuAAWZa_YdlL302sX_9Xcb4jqRo4hDoQ0sQy-HgUARU2aGptafiSqHJyUuPcc8vY3gYEQLJ9fy5-xO_M0OOa2yDovJzun-YWZpzP7Tos6g5JTWkMUZFjte3q27hBu_MP2z4MuJzP7l8WcK0lWnexTFi0ZOlihdcSGCKACfjkomB-gtvRaEt3W8VXs6XbKj-LqvA6-nfAvdAK6GwXVDvNr5yxRyZc3B8WOwwTEIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=jnL2KIo9Bm4bvgBH-6yvJ9woefM6JKlywuUtzi2qSlDV2fBbSWvtS0okJm1FP_EpT-tbkjPDup8f_wPxKthbWSviCTSjK61Hbabq6CITJaBv22fa9O-NRPt65zob2J1UK4rHZjTJFKU87cO_uG6gG5LypxPoMAffZzXXL0V1Vz_QD8izQSRZzDB7rkrF3sNUhJaXUpZYIGYfXAuGm8X1I7tgtCL7paB1Wu4S7IDsVMIYpqgj8RbMIX9kqrNw2gsXah3km4-byt4XCR8l4kND2O-qTkIyQb8z3rsXEkWTyA4b-vjx9vWr1eWbynG4KBiyWADr5fTMMF6PgAgVNrVyLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=jnL2KIo9Bm4bvgBH-6yvJ9woefM6JKlywuUtzi2qSlDV2fBbSWvtS0okJm1FP_EpT-tbkjPDup8f_wPxKthbWSviCTSjK61Hbabq6CITJaBv22fa9O-NRPt65zob2J1UK4rHZjTJFKU87cO_uG6gG5LypxPoMAffZzXXL0V1Vz_QD8izQSRZzDB7rkrF3sNUhJaXUpZYIGYfXAuGm8X1I7tgtCL7paB1Wu4S7IDsVMIYpqgj8RbMIX9kqrNw2gsXah3km4-byt4XCR8l4kND2O-qTkIyQb8z3rsXEkWTyA4b-vjx9vWr1eWbynG4KBiyWADr5fTMMF6PgAgVNrVyLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1HOgKdLYLtpCu_F0KpYoD9tiV_APEKMoALcHgww7wo5e7-Ij_RRNKE3fVwu8JHi3kMjEA6Sl-tXqsCLUDYQdxo_6HF3l7EFm_CevoV3V7pUVJnEzxzZZwjMsJOKnsIS3jBE9gMDPWOCpP6RkL_egH-OFsGowkOB4hE-FEvkpmL9NSMdJEaAHujB3zMW8HkhqY1xNn-yAxvr_kZURexU4V-a-OuubQLVhfXiSSNaC3lav8yDKhAtmAKOqbvsx-JlzEp7mbIx0lLvCLMAs_w8Iiylz5bmQ_lr_D-YlAe5drYfkWCD9Rp9SG0c0XOQZDaYwDVEUz7rQUNOTSa3ox0VUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=IifoR5UkcajE6IxSJd9-FTZQYxXxoQ8e7G5U-G9Z-TlQkxc5Kk98VFPFdfCnjtnhIxIGIZQA6wj0sElmY1g02_bfuJOepDIKv9RxhcSMgKEmPgnyV2KgitvJJGKkyumt3FNN22aeEjLj7NdoPg6qh8xsAGs86MsGSZpfeTf17p-lmwfQemx4-yYzCinfJRETTU_beUdADyMZz_RTFvgkLqF-qhwgouLFm8GXZuZ-ojxC-IHtxdX7zHvKWZlP-HCpRYmu23keyMEDfEa4eIGgLzg0g4KXcd3G4pHJkPNnWxoXzwKzYRRvIaUnOjTo5Y9fn01nSBvnFzj7M3YZaI_1dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=IifoR5UkcajE6IxSJd9-FTZQYxXxoQ8e7G5U-G9Z-TlQkxc5Kk98VFPFdfCnjtnhIxIGIZQA6wj0sElmY1g02_bfuJOepDIKv9RxhcSMgKEmPgnyV2KgitvJJGKkyumt3FNN22aeEjLj7NdoPg6qh8xsAGs86MsGSZpfeTf17p-lmwfQemx4-yYzCinfJRETTU_beUdADyMZz_RTFvgkLqF-qhwgouLFm8GXZuZ-ojxC-IHtxdX7zHvKWZlP-HCpRYmu23keyMEDfEa4eIGgLzg0g4KXcd3G4pHJkPNnWxoXzwKzYRRvIaUnOjTo5Y9fn01nSBvnFzj7M3YZaI_1dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=PzsicPh-ASmXRKaFuYo0snM-hsv7ic2GajIlvMpemcbYT5LxomqhwT9xuHyKKiJhGm-NR0l5I448N8zgW2nuMzNebyPYW9-GIiQjyvLwjfzVlOy4UUNL4PhIWKGP0epNSaz4lfeXearXLdko80FM_oV89dj_K2dncjrQuY_Crv1qsoExmduiuhiRg8fn6yIrgfTotmWSEYYzceQV4jiU11rP9JkoxwtLEE7VLSJLsJEjMrqJXx-lj5-WueozCQ9DqdJiRyFexC0At_WtZpbWnQ4QUi28wvB65jDXNrvf5UXao_MHgqFYYN1bf8iRqGdxcJZzKT4RtVX7rJxr7YmETodb5xrH8d-PwdsFHDjTCEvojt0Jav7DvwmI7Ub5dGH-7e2N6D7q34apv53pleSqX06K84bbxrEdcTpwUE2K8P6c_B5BRAFH-FGsBtNgvs653gr22ksXiRjBUd3OV3UUKUXnx9qiB09F8KtxCbb_KEM9gSlLzY-eUzOxXlqBo_dDhNrFMs177XaT74VeUBbXAHtrqlZ8R5m4g3jST7loKgWDlRiXwV_HqAry-A9o3bFY22dF70HYPk1q9rmmNDo-AUhzFYbqM8r83WCPVFqrpU2_KWKjfwaXdGoLBpw3aYrTsR54Om5DDpGFV_OvZkeHJvB7nsNEX3fvlLUyCdzWba8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=PzsicPh-ASmXRKaFuYo0snM-hsv7ic2GajIlvMpemcbYT5LxomqhwT9xuHyKKiJhGm-NR0l5I448N8zgW2nuMzNebyPYW9-GIiQjyvLwjfzVlOy4UUNL4PhIWKGP0epNSaz4lfeXearXLdko80FM_oV89dj_K2dncjrQuY_Crv1qsoExmduiuhiRg8fn6yIrgfTotmWSEYYzceQV4jiU11rP9JkoxwtLEE7VLSJLsJEjMrqJXx-lj5-WueozCQ9DqdJiRyFexC0At_WtZpbWnQ4QUi28wvB65jDXNrvf5UXao_MHgqFYYN1bf8iRqGdxcJZzKT4RtVX7rJxr7YmETodb5xrH8d-PwdsFHDjTCEvojt0Jav7DvwmI7Ub5dGH-7e2N6D7q34apv53pleSqX06K84bbxrEdcTpwUE2K8P6c_B5BRAFH-FGsBtNgvs653gr22ksXiRjBUd3OV3UUKUXnx9qiB09F8KtxCbb_KEM9gSlLzY-eUzOxXlqBo_dDhNrFMs177XaT74VeUBbXAHtrqlZ8R5m4g3jST7loKgWDlRiXwV_HqAry-A9o3bFY22dF70HYPk1q9rmmNDo-AUhzFYbqM8r83WCPVFqrpU2_KWKjfwaXdGoLBpw3aYrTsR54Om5DDpGFV_OvZkeHJvB7nsNEX3fvlLUyCdzWba8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlwP1_ZJoJ9oIYSymVDTnjRKN2wfZadvaAEQIk6vi_PqWOpqBuyLx2tXq7WqgyeR-ekiy9cxGdut85W-_AsLg7YtZoSAkYHOKdU72gSMcsStX4d_lHiKnUFVuw_DtuKRCVmLe0fYkusAzeCE5xJDhKqI8jN1YIr_DEYA205J9_d_OXwuqlEqZm5ZznaliO70pKXbQXLMhTyqwXCPBqcBKfJ2t-bWZD1DPgB4mou1jssoP1OwmANSZJhVwE3-oZK9xHPhM1nLuDR7kReLVPp27JEeenq6mdgqCStzgGsDLgdPKqJChlq9Q52GUHKuoFjjUTHmG1FuMvWRND0rRzrcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=NwXquN8d573eyfsPYmM5nraBA_R4dz9-dHSBP22PpFv4NVpBc3C2rAoEu6_Cd51j_I3tUhh8bvCdChUlGGTwGIULfDNS5OU2Zq6dVBKUDzRPvtLFpVhMxk_3xU-w0n0GQqOxPiEj5BD0M--czV6qTpioMeejF_m-IJmycKdxbZI7QsBOIpO7TrEGaQtwmWi8RqiZRdgePjVYBw2Z0Jj2aj8Q6CiynnQQqlL--X1_fcvBH4LJaDY8cWv9y-P3YqMqvuZ7bk8fNXvtUXYBYyUixdsTayUafqgjiL1Cgs7yKtRF_BahdLma6aIGnlaqTPDyZ6ns8G-nFNj6OMvFjh69uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=NwXquN8d573eyfsPYmM5nraBA_R4dz9-dHSBP22PpFv4NVpBc3C2rAoEu6_Cd51j_I3tUhh8bvCdChUlGGTwGIULfDNS5OU2Zq6dVBKUDzRPvtLFpVhMxk_3xU-w0n0GQqOxPiEj5BD0M--czV6qTpioMeejF_m-IJmycKdxbZI7QsBOIpO7TrEGaQtwmWi8RqiZRdgePjVYBw2Z0Jj2aj8Q6CiynnQQqlL--X1_fcvBH4LJaDY8cWv9y-P3YqMqvuZ7bk8fNXvtUXYBYyUixdsTayUafqgjiL1Cgs7yKtRF_BahdLma6aIGnlaqTPDyZ6ns8G-nFNj6OMvFjh69uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=dPW4nEkzN-vc6HC-H_sUQZOuSfOopOt1is2vTiYreCJ1QMf29kLdLj2ya-r1pm41vhlmyb046E0tSaqdZ3ak1UHLczNGo1e3pYH7LyzZBfIvEeJt_hefPJ_WZ3fvQ-8ue0Ov6kedM_jqVmdWmNFOM2QR6T2qXdn1SZbPIcI4n-SR44tZkhhAppQHkKwVDHSaaeOt1vs19XosdFza-pqJXFpTWi2wKcdNDH9HubOfRMXldkLy2JeMJ4S9_EWL_Ua_6g9Fv6_zqJPbwBO4cXuxLRPTzteTjUEo3Jd5pMYJwLlZJNMOgj9pByfyGJh8YrSInLCGqIwaYVM8UdNNsvUnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=dPW4nEkzN-vc6HC-H_sUQZOuSfOopOt1is2vTiYreCJ1QMf29kLdLj2ya-r1pm41vhlmyb046E0tSaqdZ3ak1UHLczNGo1e3pYH7LyzZBfIvEeJt_hefPJ_WZ3fvQ-8ue0Ov6kedM_jqVmdWmNFOM2QR6T2qXdn1SZbPIcI4n-SR44tZkhhAppQHkKwVDHSaaeOt1vs19XosdFza-pqJXFpTWi2wKcdNDH9HubOfRMXldkLy2JeMJ4S9_EWL_Ua_6g9Fv6_zqJPbwBO4cXuxLRPTzteTjUEo3Jd5pMYJwLlZJNMOgj9pByfyGJh8YrSInLCGqIwaYVM8UdNNsvUnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNj-sfU3gVsVBJExn1kwYURFnB0S99ERg7Wkr_Rzoln2kDLdRMPUbOV3gz33hNiWdvIro8VgfcK4GKz0QjO0RdHE3HpxPF89y94HhMGDAcoCvf_qDrL1AVkkbopXcTv42Ga17CgMamm25AlCZ199ppFSL6XIYZ8ty3ahL7SRE5pFl7XsIXgc5LZTLNecIev2lVmqDc1w6CAogOIHMar9oUPq_amdQ7PZxImoro1NkRVzFFSfIjTWZ0Jwc2YYHLXjJ6j1Q-uq6yHaDpLEudvbOGroAujbM5c-bcR4KPDyl-TaptPHr_gt45iHFdwPzugZCNsrd-cGtwsIzJ5NzpGtJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=R0tnCYOEZKLEUbyKI6cJg7StuSJG0R-eyEOXLDCVI605vDifz5owo6TPGSnFum9yqVpVVIoTO7glhjMk4bsRdSdJIRPjGJxsz6vY67vSrhbS3WX1wiL9wbfhX-z-4v1NJjZyipwAMksUBsu25bXaggPy0hzuecXHSEPn8orzRfMxXlpwLw98U2lnH24lXP-TlqsiEr0GR05eZeKLkUcAk0STrwu0EBroHxynaufsbY3R-LcJ_8I0MEuOwHReOm-1LmqUD6htzAeoQqysQcCHmsw7aeEWu7i9mkFWE11J1VvvotkcjFokHwNTnNtkFC4SAgys8uN3sIxIgrkmBCUv1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=R0tnCYOEZKLEUbyKI6cJg7StuSJG0R-eyEOXLDCVI605vDifz5owo6TPGSnFum9yqVpVVIoTO7glhjMk4bsRdSdJIRPjGJxsz6vY67vSrhbS3WX1wiL9wbfhX-z-4v1NJjZyipwAMksUBsu25bXaggPy0hzuecXHSEPn8orzRfMxXlpwLw98U2lnH24lXP-TlqsiEr0GR05eZeKLkUcAk0STrwu0EBroHxynaufsbY3R-LcJ_8I0MEuOwHReOm-1LmqUD6htzAeoQqysQcCHmsw7aeEWu7i9mkFWE11J1VvvotkcjFokHwNTnNtkFC4SAgys8uN3sIxIgrkmBCUv1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWIGsGICLVrPAhG7R6gD5LLj7g__CfLXRyN0MhuqoE-QOHBCncuy5TZSSRs_sUuoMsqK-IsRmb-262D7YN_NaxApt0ePbyqV5CmTTVATf2IJ_pGnVjJNpveJywQoj1mnKzQE6MgA9SgP6gO21e-w-dh6ZiDV1I4vsRimTW4S6DQrWMTr9keNuiPogMU02L-uOLpa1v0vpJT0IB6MDSbpch905UAyZr349Jqi3gEXdqR8ohxDXn46cF1xbijZbQJGA6GNxMT5SorWGtJvunJvsHMCnKK3LLMXPRx2-ROPUPma58F_2US1w3_uP3OOo1Hj_9TWkwaJQoBE7_yaZCtVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=GL1j95Lzqzsx00f1FbAvu23gVxv9sDU--MCVaE-5_oX17isA_Kd7U5LHZk183Z6lhq2mmaf4NosPLsAzBJ6drxukN353ZPCSeRY6kzIf4lrytC8zsFl6alJ8KofwzEwg-Ws05e9p6kYa-OaRgS5W0dZu0uvkJKOKoABaQK__pUZscy91FA1l1gfyne2KCYJgOuhtpZmus9O157l0C4ow0IE0g3NTHhoIEYnqTHwOp68HHbjloha7gPhOpHI1q-S16ymiY4z11K32j_UGP2CMxxWZYdT9aBjmCPAWQHyKDfL4WlslKxfpIBLOEJVRxNNzWbYcMsXftBjprn-RnX6FwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=GL1j95Lzqzsx00f1FbAvu23gVxv9sDU--MCVaE-5_oX17isA_Kd7U5LHZk183Z6lhq2mmaf4NosPLsAzBJ6drxukN353ZPCSeRY6kzIf4lrytC8zsFl6alJ8KofwzEwg-Ws05e9p6kYa-OaRgS5W0dZu0uvkJKOKoABaQK__pUZscy91FA1l1gfyne2KCYJgOuhtpZmus9O157l0C4ow0IE0g3NTHhoIEYnqTHwOp68HHbjloha7gPhOpHI1q-S16ymiY4z11K32j_UGP2CMxxWZYdT9aBjmCPAWQHyKDfL4WlslKxfpIBLOEJVRxNNzWbYcMsXftBjprn-RnX6FwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBuvyLr7oUfcjazi6Hyflzb5vx1ex5mk5knCRsKyZhiUqnT2g_EeGnIAWCB98e6sKiWOvsCbepiLrVwnM60bkYaDeN2FkqtYvAFuL-b6kM2tA2DnSKbzx5De6rwOYXYmFiKdcV-18RSPCSWI5DDoLcuhnfhQRjKYw5me9nAMuBsK01HdatoWLbvaRI2PnovHYwuBefenPLNqF_vVffDi87ncV0-vx0LOuAGsKamvsG529e8IH0JxVru-iNCxZ8bFz2SGSx32BdP-k7GcpO6lQIjW_PcQSLIcY6rz7e87qCL0CD_6l3Etsz-H7ByKWybKVJ4RKUwHMocAVjzWYPrpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDoiFi4dhkz37JeX3R7Q2JNlSzIvOPLywqcOMKVRX-qsmeRSM6XYVfcVHXnKX4jgpbeu7nEWWgfwP4yw4coztTkn04lRdzY-5RL2hUNVVdZ_xeT77bZ7xVkDxkspT402A9CCuNc2tH-ujM40WYUCihzb8zuuGlGdlW1vdE0MncLO2DZ1abigGRThQUAeWqLuSRlpOcrhuc2D4EvLTbsGK-4TU8apw2vhxwst2c1JEQVnsIezDBwDAMxBDdabPbhwkjd5YzzHdK9H_fZ5aKKmDSITDHa4_3hqAyFvlNb7Xb2kXGi3Kc1FqIa2yOd2cuQrLjrzkJDj_zkpYSm7SnPLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR-DoVjzuu2RKMB2CxwC9UqyJ-4rG_QlmPoRDiaWmvD7q8mnSwyLxnYwALtLxqgCsWadELB_R6D2dYW6XeOmDMBPXxxsP71kZOq-l5PkBYq5TwNr__d0qm4HxKwt4lY2-Bmsh-bAvBmjbBiMZIOT1-hD-rZst9aA9iegeVCRKV7RED0kfKIp9jci-NtoE8SwfrURaURkyUF-NP5SQ5tepR7CSir_HWTgccCt0PCs3ax6AJYgNwFrkP0svTWncAw6raVDB0ePJHCEJ421VZFqXf2wX85U6hUNssPEJlfEnKOqNfEFg2Ij_ZFKQaXLcpldORoGcRPX8cmRSmE2V3_goQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgqH1BJzMJUz9jOAR6M3R0aImK183IcVrVMCx2xyat-OBNb4lOtdZZJQPVNlzAcx-18Tpml4FTjrD7V-0oNpcfF5cmLp1jlR_I3fbKlsVGRrrV5dvfiwzJScbXMRLBUbAm4_QticVfCt7A-BDs7VqAzhLt8Du31ZBp031oh4g1jHO1djjITWaSUJ7YLcAbciEiv3GotJiu_J21MtPxWfOTtsURIwqDXJ8pRcKhPky8H9MoUcFZOJ6LZpSPUy_otnxNZCukQbWMptDlq0JqCsUM7hbh_pFiOkm25ebiaTaT4S0rXq06lZafWgPbdfZRsZogvBhyOn3GONzWm6uK3-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=hhPii8HZHSM6ND6YSVtEJhCIUgxqoc3D9Wgtl501m2fkgreyIURPSaeAZXOOcTk5TsCk1LanMHxv18UITWTrxt0eHZ4ss1dzS8u4q0LZyGXAZ7B7qh0WKLp0H4N25h783UmLtuUnbF7VPlWUToXzD5Tp7O388oYce-WWqaecZROGnskpkjoePz4rBY_bsNGaV2T46U4iZlL3PcRBAdzWJe3W_yTuvjK26IrBVSi_yTUC653_7hdwu8x07ZE7mlkNqKHjBY3chxBXmDeSljurDcgFSswVLqYh-d0_ApI2L_oXkhipOKhNB4UxFH8M15-jhYADGmKvIQgTp_KEwvxuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=hhPii8HZHSM6ND6YSVtEJhCIUgxqoc3D9Wgtl501m2fkgreyIURPSaeAZXOOcTk5TsCk1LanMHxv18UITWTrxt0eHZ4ss1dzS8u4q0LZyGXAZ7B7qh0WKLp0H4N25h783UmLtuUnbF7VPlWUToXzD5Tp7O388oYce-WWqaecZROGnskpkjoePz4rBY_bsNGaV2T46U4iZlL3PcRBAdzWJe3W_yTuvjK26IrBVSi_yTUC653_7hdwu8x07ZE7mlkNqKHjBY3chxBXmDeSljurDcgFSswVLqYh-d0_ApI2L_oXkhipOKhNB4UxFH8M15-jhYADGmKvIQgTp_KEwvxuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=c4v00W9-Flex1VVwYZkPvAGCiU1CYd0-7CLydJTakVt348tqjuwAu74Zaoq19boTaq_WrVslHFQpqHWaDKxLs6nTZUM7DvwlL6LrKjOwGMeJ5KUwa7_pFwfGjFMIiKuFHcZI1UIs-DOhVGdzsfoHe6HDKXI2sCYZK2ktWLpW8aXX7pFVt0Itc4v3hmUYPkbhd96b3pp-bnOXdGbWzsfS2Zr7e3TlQx1EhEOWItb38AyqtqHiXPBwsGhvAZZQ7dSVQ7Q_qqIpAV_grb_T9VOQRHZu6tpRsqg8gndpRaEBQgimg9oKL2JPhhLuQEqsTdzUS1zi47nrC6y_YlLVqJqSOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=c4v00W9-Flex1VVwYZkPvAGCiU1CYd0-7CLydJTakVt348tqjuwAu74Zaoq19boTaq_WrVslHFQpqHWaDKxLs6nTZUM7DvwlL6LrKjOwGMeJ5KUwa7_pFwfGjFMIiKuFHcZI1UIs-DOhVGdzsfoHe6HDKXI2sCYZK2ktWLpW8aXX7pFVt0Itc4v3hmUYPkbhd96b3pp-bnOXdGbWzsfS2Zr7e3TlQx1EhEOWItb38AyqtqHiXPBwsGhvAZZQ7dSVQ7Q_qqIpAV_grb_T9VOQRHZu6tpRsqg8gndpRaEBQgimg9oKL2JPhhLuQEqsTdzUS1zi47nrC6y_YlLVqJqSOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCqrPoyRquN3pQeCmvgQg3f3V0ECpUnaE1xsRNcau8HbFGQAQXSUi3nqKXGqrwM_4fn0qTcNP52365-4E4u5skeHDqTNbU6Rs9QDSOEw2mqJEFlij43hwt2G_2H6kCub_CaQaB-LLzI6zWsLT5w57ENQPnWA2iBg8qhtOpF_AfiT-DhR0BMUadXIfFs_AxDJXrq2PztU8kIJdoyuALYb72YqhZ9I_e4D6d8tvX_wWFGyZSGZFqdNonxXI4KSKKSjY7RTDn8o1gr1DFFNt6XhCXtlJpkJ5cnkoohLrlDc_lswiqtBTJyy8Q7ONZtmWMKPZCvithTaCgQgmh9dBCyPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=Ku4LdfjLZ3UTLum_Qajs_sNFt63qqdrKyQPiW0a8Y6BrjyKm9Ki2s7Bi-Lpo66hM2Lni5wF5RV3JqkQa5Wrce0_XvEiUjpJcuRLBeidbV6Ahv3jP-82SZLapNwc9BmD49hwO2xPuvEYDbbZuhuEBE00HipJj7GTMDDXemqnMmhgo4uSbVv_haBmaXGzWnSYJtiRut2Ud5YeJ7BNNMatz58wi8tX0pteNuh04eVBXfgGqcSp7B_9Lp6jxbTxxlpntMZeFB1zkLSA6KGKG2BaJ_paCd6H3nNAPk2eszWrZVK1qinpgfVhS4sNoLSrAD7DYXKHa0h6AazZzzPBbG199nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=Ku4LdfjLZ3UTLum_Qajs_sNFt63qqdrKyQPiW0a8Y6BrjyKm9Ki2s7Bi-Lpo66hM2Lni5wF5RV3JqkQa5Wrce0_XvEiUjpJcuRLBeidbV6Ahv3jP-82SZLapNwc9BmD49hwO2xPuvEYDbbZuhuEBE00HipJj7GTMDDXemqnMmhgo4uSbVv_haBmaXGzWnSYJtiRut2Ud5YeJ7BNNMatz58wi8tX0pteNuh04eVBXfgGqcSp7B_9Lp6jxbTxxlpntMZeFB1zkLSA6KGKG2BaJ_paCd6H3nNAPk2eszWrZVK1qinpgfVhS4sNoLSrAD7DYXKHa0h6AazZzzPBbG199nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=flBOLNlMwHcmosXErwllUIOPLmRiotPpvf2q8tTljTJ4cufbhTPMeCRHmCzxATKeGJAp-NocyHFZAvJQTTrIy_NS3jexosneCh6XwVcgweKjrDAhST8dukW0b8OgK0x2ipXXYbnOjfkdczSy6TPrx33RLHsHTictGOFli7YRxucCEZidH8SGOZFC8NY5AGgNJFnji-m5Qa8-WquvBTHLQwJM2fwujMFdpPfBc-26GvgfSDfd0-1WRW7Z1mQ29H_LLWd_fL9YqA7ki7mkS7O-WvnmAtzOoYqfzsuHy-OTOvECuZG4hkbJSUGHgdxnATLXLEXHbgX0IUXJWrOHeUbUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=flBOLNlMwHcmosXErwllUIOPLmRiotPpvf2q8tTljTJ4cufbhTPMeCRHmCzxATKeGJAp-NocyHFZAvJQTTrIy_NS3jexosneCh6XwVcgweKjrDAhST8dukW0b8OgK0x2ipXXYbnOjfkdczSy6TPrx33RLHsHTictGOFli7YRxucCEZidH8SGOZFC8NY5AGgNJFnji-m5Qa8-WquvBTHLQwJM2fwujMFdpPfBc-26GvgfSDfd0-1WRW7Z1mQ29H_LLWd_fL9YqA7ki7mkS7O-WvnmAtzOoYqfzsuHy-OTOvECuZG4hkbJSUGHgdxnATLXLEXHbgX0IUXJWrOHeUbUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=Q7TCKgmRaQV9boSbFePIvyLaO8TLWt4wHWWBR1hmoEdPIdGsTbBWA6aPLszvzVRxKBuo2pisoXRpfeMyIQgRdE3l5lwuksNtIobt9-HipVZW2N5eLd27iu2pUfG715k1W_aVT4FjJzdgBNoSvbo0yXolcn_5KKN40-QLSDsnvB_wyH9LELZ5E4zLZLxVEppSLYdXNZtMQCryRVUXlnUGrMRCXEYv2OXfdqPZela3zgF-tIuOM7wo6XuqGsWmsK0dlddxO6PUzO_eEAbCXtyOYGkiAcfchhE_emXEQtQZNmF71bB_Dz-9P-biZZ4hMH6yQ9Ue6Jh3OZAeTLVZ71YZHIoqeG-EoZxqVncIXuYTOMv_qJG5CHa7pX-48mCqVcHqAD4uf3AH7HGX3tiKuDMAYFJsMPm6TXWVrX9grQtqEEQCy8Yq6SlUQCwLVC9i8K0UDcOfhdpl2lAdsZNcppI7BhnkB13-Gx4n1zpnIiWx86nlEMOLFj_bU0fE3z5iOqibgEVzkcaWeO-M6VVcycRaB5E6oOpNhgJUidwW1BJVbzkZEddx5eCLm-a_yzhjpvnrcfMfM4GmS4-e73pBYZA91ZElLinrVw37Hbocjp21jPvD6Aiicle9yvlcZi7dn7jS5QITFeELmlJLggSHl4XngWkjCx_AmbTDtDWqoJCDDKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=Q7TCKgmRaQV9boSbFePIvyLaO8TLWt4wHWWBR1hmoEdPIdGsTbBWA6aPLszvzVRxKBuo2pisoXRpfeMyIQgRdE3l5lwuksNtIobt9-HipVZW2N5eLd27iu2pUfG715k1W_aVT4FjJzdgBNoSvbo0yXolcn_5KKN40-QLSDsnvB_wyH9LELZ5E4zLZLxVEppSLYdXNZtMQCryRVUXlnUGrMRCXEYv2OXfdqPZela3zgF-tIuOM7wo6XuqGsWmsK0dlddxO6PUzO_eEAbCXtyOYGkiAcfchhE_emXEQtQZNmF71bB_Dz-9P-biZZ4hMH6yQ9Ue6Jh3OZAeTLVZ71YZHIoqeG-EoZxqVncIXuYTOMv_qJG5CHa7pX-48mCqVcHqAD4uf3AH7HGX3tiKuDMAYFJsMPm6TXWVrX9grQtqEEQCy8Yq6SlUQCwLVC9i8K0UDcOfhdpl2lAdsZNcppI7BhnkB13-Gx4n1zpnIiWx86nlEMOLFj_bU0fE3z5iOqibgEVzkcaWeO-M6VVcycRaB5E6oOpNhgJUidwW1BJVbzkZEddx5eCLm-a_yzhjpvnrcfMfM4GmS4-e73pBYZA91ZElLinrVw37Hbocjp21jPvD6Aiicle9yvlcZi7dn7jS5QITFeELmlJLggSHl4XngWkjCx_AmbTDtDWqoJCDDKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTGRli6Bs9w_Xws72AUn1qYIJOM5cnhdr03YuvZlU_dzHOsBJeasYkTkjamqus54GtqiibJmFGszE5Fd504cwjNLiSPDMTiVC3-Mmo7JNARblVD-8vSV6IPVAyGdOEbMMWzw2wDclm6jKcUtTbWeqME6-U_z52SgR2fCq95U5pmIctxccGg-axoJdaC2praJ6N5QpqT2DKp1bhq6bEFl3-4lc3bOhFOyQLbVUJ42DSFA3ubRdkXIXyybZpb1Jb0ksRS2C7ujL3_7BmAqXgvw0JCozKLWOPWZZP6yyhOgovQgOGEPvKRHb7dtXDb_IYbGr9EtASo56kqi-Poi5e4WRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=lhNIwIF7Vt_qcxo8Co_lu1FGeDPNaa_5o_TeYl8ih2rP56E8LPrFzWvJvjFG3KvtXkLfBcWhZMTi0FES86SY8lkXzDLuETP2CTFEc-zdQUrC6kKTsjLBhejxiTQJZuQhTGMkB7wNnTvjtdTR_vYace_FeGjm5-rTlM_yspf44eDzt3C6Sus-HeXWvucB2VF0UvCYqGVMzo5rThJh-YHmAKkf1iiLsroal1zBPrakwqQSQj4D1fn_In6pixS99NDuZeMLB0jZn7-g4jJ_mwXkgbqCCnXeBLERpGs-b13FJixgpwt9AIL6Z2LDLBdYfPtuyFk_EmhJxrIrkn9xYy7Mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=lhNIwIF7Vt_qcxo8Co_lu1FGeDPNaa_5o_TeYl8ih2rP56E8LPrFzWvJvjFG3KvtXkLfBcWhZMTi0FES86SY8lkXzDLuETP2CTFEc-zdQUrC6kKTsjLBhejxiTQJZuQhTGMkB7wNnTvjtdTR_vYace_FeGjm5-rTlM_yspf44eDzt3C6Sus-HeXWvucB2VF0UvCYqGVMzo5rThJh-YHmAKkf1iiLsroal1zBPrakwqQSQj4D1fn_In6pixS99NDuZeMLB0jZn7-g4jJ_mwXkgbqCCnXeBLERpGs-b13FJixgpwt9AIL6Z2LDLBdYfPtuyFk_EmhJxrIrkn9xYy7Mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWhpOs50Hxc9CzvdL8wWBwq0KCOG1w1TTue1AI8rC8QZGQjHOkMGq6V0e23CFCXAnZOGOv0u1VYLSfwIbIwXVL1XjYKf3jLlQki8oOOXcSXqQ-KuliPKGuMZT0a4FDBICLN_Z6lnkL_LjHlk8wvkBSORMlxtQmQ28lfH8M1xUBebzj7aurztc12JXQxIPMUWs5pC3U_Y_iozbyoleYYLU05snshgQ8pqNDX75JsjILJfZa5eQLXJhUm1hPx16XPwbExuNz0scKrGsVs_zP309RNpzs5HYngUQ1eEO1kU_Jwwq1gmotDmXtVEXd1eUPiyL9PUALZ1RLOAmwNVderngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjOuFE5habLYGmbDSTPue6Zgta6p8NKw3LQGEepfaBVP0E4bxJROMF2M6ZxkGK8uwe1EeJn_AevZsfuDmx3HQ2_Krn5-IGYHi_Pg6FRsfwOLH14F-CB-RQ2zxjEr1u01exNXLGuTWSNJvTP40FMitGFxacZM-COS6kuUfvp-i9As2etVAtVPZKYzqDY7j9Vz6smIFLTZHULmJaXxYUJeTSvH91EtiGHqMRby9ijVtDqDYZKgIOVZBAmmxa8CRHIXao4b2w5b0_NTWRK0wK1rFmVc1SgGxEl1UbGGUIwzVAOmh3WjRDao_Z7wPpc5QBpMdnc_dsZioLuAuUPwDKbrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=jHliiP8X8tYoME7oJRgrz5eWKYm4XSix3uzm8A3hzVEX68zSCfiHBz7M2ac3Mj0WJ2K0Fw8R71l8nBGm4119Ydf7RcvCgMkjkBncQ-Fp7UJr_duIOw-PlxYJlRVgWhCG2u_zO-GjhktO_StptN_CK97uT4UO_W2STAKLPm7969JAihPbIyt660eYyycearV0MEU2hzVBnqgLqIRJBI9zzqQkcpe_bledzoYWKkYUiw_4oR4-YAw3SFb1IDklJaZSrzO_ZaGBfeQBWhOdBde4q6xBiGUBYj8XLY1_12Lm_G9srieh_05eVgQpZn6qPuzlHeRp7l05Hg-7OTvqZ1ckjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=jHliiP8X8tYoME7oJRgrz5eWKYm4XSix3uzm8A3hzVEX68zSCfiHBz7M2ac3Mj0WJ2K0Fw8R71l8nBGm4119Ydf7RcvCgMkjkBncQ-Fp7UJr_duIOw-PlxYJlRVgWhCG2u_zO-GjhktO_StptN_CK97uT4UO_W2STAKLPm7969JAihPbIyt660eYyycearV0MEU2hzVBnqgLqIRJBI9zzqQkcpe_bledzoYWKkYUiw_4oR4-YAw3SFb1IDklJaZSrzO_ZaGBfeQBWhOdBde4q6xBiGUBYj8XLY1_12Lm_G9srieh_05eVgQpZn6qPuzlHeRp7l05Hg-7OTvqZ1ckjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3YkZw0P0FLxoQASWqjXk_VJu-jZPlojEvnIJTaQ72bAONauDDmhvfxlgUcMuSwPPbEWswuX1HA1TIZUfM0wrIzu7qNthMpCYSGxDylOv5bLzr7jJ6gRu8qTxDk7SwWe0SjaQ5U5FoL_qD9fbdmaQGiMuUNkuI5bDrZ_UeV44uwoD_gDx1ltpnI3kC4ccs_FT1AkkH8ftQBveDMSozmtIOjj2vlvL8f67dhXfnbSsjvOk6mAb43bV0DoXw5YjfRuup8e-lfDC1swrmcXSrDpBbOay2IkEgfVMeR_6qbnFxIJzyoHyK5EFBzrBJJ7V7PnQnrIwklH1rfjIEpNmO9f7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=KDMxj7tX_0nfh48sXKsAg7Vt-M4tzFBQPXhOYaS4O-urjE6JdhaMIbCTcEI2h1dJf0Z3OPA1PtxatDrAOBsDxWtJsxbuVnlPAV7z_wTOcozC6aSc47Gplz6TWzgEoAD_KDsVe5pnV7JLb70x-CvTdeaXe4HuDfh1fDRRQlSOSg5vnfByCyWWoOEPnqYX6d5UhJnWHCOnmvoW6QzbXw8yt_YvI16OVYSk-Lt3w-E_6zRLZGzXVYxWiwUWhKzduOCNajJh9WKd7c30rOmT-J55IzHL8uq8MqrBjhqJMc59LQbId3hKWgDevhlf8XH1wyEbYcnjw1rVHgciRCW45qx2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=KDMxj7tX_0nfh48sXKsAg7Vt-M4tzFBQPXhOYaS4O-urjE6JdhaMIbCTcEI2h1dJf0Z3OPA1PtxatDrAOBsDxWtJsxbuVnlPAV7z_wTOcozC6aSc47Gplz6TWzgEoAD_KDsVe5pnV7JLb70x-CvTdeaXe4HuDfh1fDRRQlSOSg5vnfByCyWWoOEPnqYX6d5UhJnWHCOnmvoW6QzbXw8yt_YvI16OVYSk-Lt3w-E_6zRLZGzXVYxWiwUWhKzduOCNajJh9WKd7c30rOmT-J55IzHL8uq8MqrBjhqJMc59LQbId3hKWgDevhlf8XH1wyEbYcnjw1rVHgciRCW45qx2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
