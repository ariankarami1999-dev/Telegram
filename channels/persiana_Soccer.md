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
<img src="https://cdn4.telesco.pe/file/VKu9A8sneObxPkHUzJ-kWjwrk8uFxltL1gYWfVlv8Hvfat8EetXMgHu6rq_d30OMSeNsDFjDKeHcREfoh0Oo6xmw2_SA1-tpNauuoN_QwbZRGWiuzA4524T8fbMgNGA2IPk8w7i8Jr2M4vuzSnVooLR519ErL1hc6AJamMqL5Bk6ZP1ArED64DotO2v1KY5FcmBx6XXRzNbhp_t-tPs1CbwGs8-M6lxPY7N8XYK-5-aUTnO71njNNqangil5CNRdupWDles2wBRuCN7f5M1p_kqkYSK15unpYqYse01P5iHd8MfHDleXSChci2VT7UAe4S_Ng9W5HG02EtDeMxwSTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsV_DEs6mJATN-XRnGnkUj-qTWd9mxfv4D-RZz6Dl5UolhoORP83GNR4xCK7DKr6XFOA7OQNR14MaqEaPLeaYe0Wnvxb5ms67TZlWI4eBY0xpVmiRB8YESq9MIyLwI1nhmqGt3NqbC2sX6eMlx3wBgD4xbKU14gXPcwqzkHiiQsZ5v0nKzs5w9WkqpqhHs3MgSsYbAgIu1G52mD9eyNzbXAIERS_OYCtweqV6XEk4TuKqPJ-yghVYn_alNv9lZdnBLpz1hrPlf3rxasmFkuj_iuAJ4Kt7ngAB2ITSXNeAnUKR4wLyyTizub13QmkT8HAeSQSUky2pkvb3X7NbbwsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYZHF2v5D_k8QlClRyfCy2dyx_2Gx_xeQnbBrDW6Pnp4WqAe9SW0UlpOrbahwrKknMsjYclaII7c-54wv6kAy6CmCZuYl4V2JwMncPkVds59LqmaxWohRbwiLtVkjn0wOlxa8shh2NajY9P0Qy9oH9yqQSJ7dAUwH9D4fiIN8BjozlnrAJRfSpXRtj4WfU3c29YY5avPiGL8k08H66rk0yWr_hDikSFz4zsDXymyGHcB_fi2Ij4mljuk70jJjvv7JwdGBzSQ7Pe-cZfQQnGDhNu6uyL73daHsemwDkaE9M54xWeQmp8uLHLNMH-aJ5PuAAmJ3uLdl9aUNji-ssTyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkHypx4JSvY3Hthpy4QbOPSSndWJWv7PLjbujmmufyX5QP8Ie-EooIJuqFpO7l4PHWgdU-gzVUTbu_zcxaqSoOh9MCMmHI5HeD-ZAEJRmz7O6yXCYK06DQovS1rBxqLVPgDoX3ruKMRXNEiyTAALRBvCUdx2r42DhmWs6j7vO06JhhDjLK7dIFUQaKDB37lMPj9RH4Xs8eXAP9M_qGq9Zmdf6sY5pywasG5flGdUXnN5qaAcBo0zNAIsEYxzXEfSCMCodYVpk6jVl6MEOA7dKaH1WSS4BPnEgyKHE_PvjzqKirVCQe8wINRYXO9ss4lfPWb3WCislip_MIngKPzj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl--t_ujsnkzdg2QumfNs6wFJDwLZ_I5wT8BNfzmIwHWwCLEUYlUBNw8OFJHY9de6d0Al0I5zEa5VqcnKVDioUfqaQ34_wDpeDsQEiEGUusk76Gju4Kd5MHbwXIj4HJADN6eb68ym_te_7xlxE8f4cVHx64s1J0QGG2SbQkhBovouPe8-558bcaMQJvo5v1UnNil2zKKgpUsinvdaRaxhKWKPAK3VQ9zF_E2uVMDBijUtfA7EdQEeP0EzxIfhOvpdFypdf5gIqCszWQqhh-wRjeH61z8eaxrTLbadk3f9h8qhjLxDIWbNc-XanspDymYpSCb0Ae0TxQgYemiAZq0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4fNl0pwje9QdvmgVRKDF4bSfCM4RUkKF9SoKj2ki-zzhh230vjNL8Cce5uBSFEev5l5YtQRoFgXjD2hjA8muMb7wxvLRWDx6tvPX4fUz7AvHDKZ9F_O-jdyjLy-dVpnZMs2k-uqfKvFCXuiykZwMOZXfoefwcbXndlCuQWN0gCr9LLicwuq2WnyAZh3YOAIKmFTc3BVBrorNTrdap0E7o5LgGbDYoqyyd1Ta6KsMWu9HbggvsWw1NWKSOjWurq3qrPiT0p3DhWVmCqYtc_0ibxysl7nje9-NDeHKyEDkat-Nacc8TGP7DZaG3eA61_F5cBjgGyNT9rpbvM0h1MixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSMPc5bqTLdb2BNvjXb8kn6nr7PxEX5A89vx03lPQE2AnXOpQxpwyEgw31jgs4n8owUdXXyNSzZCrmUR9pGNKkLvs76ES-vLZiNqZstCPemHCAI8-oDM2lFzSOlvD0BP78ui-dlecXNV15XuBdO9O_u3MxBPaYuY1mh7kL3ijG7cNIhjxKjtUAC_B54YfV0kPAgH8b1Yb_sN8ofRFhRoiCjKUBoBX2bPw11E3DVhd-tRPqUdkdTLYt0FMH8Wy7zbhkbRuK0eyu--hK43nMJ5v5zQvfb5kX7uxNv_TN8F9mnS5WVJ640wtww-Jr1KtzEfMOWOMT1h2T-0ltufCA7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzm1WrQrfP6RHpoGERwekZwgpHukWj-ZjhkHObUIchQiGh0m6ZOglCS2gZtvJymthRoKujHmjxVjzWljJg0Pggk4GoWgPIru-vlVGrJRQx48qT6mngYqWhAIP60hBKXRdjsZn1IdNa5PkJbSaYFgfSe7LZOETZ2rtTMfffsdOVbb8biz8z04GhuluOOsJB_EQ53ygBrsRDuiV9qP5cfj_dJrQUy3zNYck5zFtTjb46dcbZQKLY40R8UlPjim18wDrk877ovR_CRmlIobB8rQcG8e6Yp8CoVwW9S9OjyD-5ARFYvx_urBGm44NLcDLdXrPBon1NV3nVNJdvbZUHJ9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuabUtGAQk117PZ94MGcVua33YwJLdY_ENPs8biQt2JLZx4OYoq7nDzsHAP9hzyBxRZubxd4jAskKOD1TeidEVu5iue9AUqkLg6CPl4nzGO5zpBApiw5SrBU_x-eIW9b8keB79ZsJbBKRfp9DslGCHsuL4gOx27fOT-5kG_xChUrmwPVepPc_UwjjWRLXDyVFyscxS-SpnXZX6TsKQXfjRxZzqBnuJ1_OUplyE7umMNwtXyWo1gnCqO4i7NuGR_qWxlEoandwHKLnaHz9GUBeIuzdrlKmXUZ6RcOrDeL0IPi9yQdQX31gnz_EpSUxOdFRJeM3ngVxSack8b6KccjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=iG4p1b_Zdg7YnmnbnPTI4mdRblz7p7zXDjykA5rT6QHzonsWXjcset5BU6q_Yq2rpMjTP5uLuNxoBIOUwKOgyTDfbFpi4t5zG7SedlaUctU3OAMt-UfajHdtUX_tV3_BzZeAAdpnIwUl4tXN2jBIDL_Lj_L9j1NYOJZvlNMOgNSLOh3zxeQPBFaA5pH_jnA2PN8UWQaZ8WBCJB_wz46R_MFaLGtFbKJxgLyV6P2EqDMnb7xTjdgx3abEuMfv1DHkEfSZOlYfTCLmrdhuBytlLr8A8oFNfC3tNa9xpsMjRIdrqNa0kyyvlf_zv0znqfmUffM0U5PhvG_pnkX-J86W2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=iG4p1b_Zdg7YnmnbnPTI4mdRblz7p7zXDjykA5rT6QHzonsWXjcset5BU6q_Yq2rpMjTP5uLuNxoBIOUwKOgyTDfbFpi4t5zG7SedlaUctU3OAMt-UfajHdtUX_tV3_BzZeAAdpnIwUl4tXN2jBIDL_Lj_L9j1NYOJZvlNMOgNSLOh3zxeQPBFaA5pH_jnA2PN8UWQaZ8WBCJB_wz46R_MFaLGtFbKJxgLyV6P2EqDMnb7xTjdgx3abEuMfv1DHkEfSZOlYfTCLmrdhuBytlLr8A8oFNfC3tNa9xpsMjRIdrqNa0kyyvlf_zv0znqfmUffM0U5PhvG_pnkX-J86W2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9m9S2Z_jI_BS9LJCpbqfWmEf7rCWgY-xC90NN3lg-FE9_GmrNz7qCKgUsfXfhPtxNnWlTu571bPBgHmz72hDKn8VrWyZcdp7xUY1ZHipt8PGIYeWswvZ-TPP9wlcLY3lwUky2ufshyXp-Dr63usIEmDg9a3GqUdzvOVDQMvHoQbE-1elZFOZPPW1GYaECAJJ9m7sIHXJcOhiOXpApEXkKg7SHeLz7-VP_LHMPjJiSjcfVma-8iNXkFvhb5dj_ZM2ItOYsy-5p6LwI1dkZUeuic1h0LzAKLnGi-ngwpVtVsF1jj9EtvGlNep6oVUZn886kXhZX_p7Ml6ZoDrOOlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1DdSHGZh9Y4NVnSp_ls-LLDIbZ4X0FDuhA-3UafiZox71xtEMZ9jLHC9maq09gookL0AmI8u8eu1nuaXj9cyAcLW4PmT_UG2IclioTcjegG9XH0rFc05Pjz89He27drIENvwa_OCUsd6xohPi5GboAkI5vC5oIceSFfWPWmSYl7IFX2UZ6orFn9w1D3uwQIxMP98JswB3OL3Ku-AjyAkva2xcv2WWyZqx87cVyh9S6HBnJHue5LnxKWWf8cC5f28Da1gSKChO5a6FcB0X0mmu1L88GkktgZ6FsvdTpJMHgFhnESVqvaxWD3H-EfE4DLZKUWf_tbkw6XOtZhIzJ_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqqLu7js0EJl-TcfT3kiPyzemML-50DAw9YFS56JCeF5EBQ-s-KCCKg2LRWR6PkaA7Y93FT42Ppqjtv2GN4nSTqkHxuTwCigPxd4Q_PIj3S8zYnMkgW12HWbBJel7ePFMbuK_QyKb3PMa_2RDNvW7EqrtA33XfWYpYNBe44EjPTSUdBWZK_SBMp1WeCN8Q2V_yenstMIXIMuAlfPT4SnJv0sS_qfneNz8PHVeGrriKtDINYFu6VYNLgC5luw_v3YSz92DWQRg-Bgrj_UnLamc4gPemK2i37TQ0RItkUWhvXBILbrzYktC1bhA7fYNiGiK38EpFtXk_kQKuFK9o3QOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiR0Z21Z1yJQ5JTzWrF0CDNIhX9uPw4vSGR5ijJEWSZ3yVhjKLkOwHRdlCNSCDhFQ7_sG5WwWzK1gQAyOloJ5EWtTJpM55QtrvdW1PWVdHTAZuSAiAf5GnklSYLaEy1q2m6wOd-1s3dC0wa2Uzh6gyLV5_GrlbgBIiuCXsynmSjgnKk4qdbAfMq39hHhaMNHjnOjDDYM2-D0UtwazkuEKuB_W7NJB23kMPJx2uuS7cc9EkD7rk91_3OOoxwNoGY6oBbGD1jZ549is7VSEnicseOXvojCyaSFiMtV5SblShkKkXlhfus7jrH0Q8vJLPeCmB9hq1p73fVxHipmWemcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=DWtE6acoCBVhrE3kG_sODbbKM9tAH0ez465biGEj3mLKzghPNEzVzUhYCnS_tKHwz5XkMxmoSj2ZC3cjYZRLfTeo1RZDDPulk3NK6JzR22Vt4uFpRHgr9KuYvxI783Hexi--O-Yqeq4OflMdtMR4S0E8dK5QAoczICP6r5ae-FZb6h-wE9dPDMwBECjqaDXaFaUn0NQGD37BDrh6gc8taWMWU2rPQM4Eoz_qtIupyngjTPmhjjbpOYDI31mTYYawhvKTicHgKWHtwrlLEH4p44ZWAJzyBWGO8On-QkFq0WOjVsLFZpZyE_sD-VjxdMzcrO_wTOouP0XrbOqyI-OYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=DWtE6acoCBVhrE3kG_sODbbKM9tAH0ez465biGEj3mLKzghPNEzVzUhYCnS_tKHwz5XkMxmoSj2ZC3cjYZRLfTeo1RZDDPulk3NK6JzR22Vt4uFpRHgr9KuYvxI783Hexi--O-Yqeq4OflMdtMR4S0E8dK5QAoczICP6r5ae-FZb6h-wE9dPDMwBECjqaDXaFaUn0NQGD37BDrh6gc8taWMWU2rPQM4Eoz_qtIupyngjTPmhjjbpOYDI31mTYYawhvKTicHgKWHtwrlLEH4p44ZWAJzyBWGO8On-QkFq0WOjVsLFZpZyE_sD-VjxdMzcrO_wTOouP0XrbOqyI-OYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBr7_7czQ5vKhyKX_UMqVUt3lFODUFgaB9BxfURMnIUw5urH6u6yxAV6BgOXCc6Qxn-2XRgjYYQKXrQd-7AYD6P0wH5ejp9yys8r7CBVfcg1ts5InwdfyQP0i3cSmouszDu-Vsb_VNF4SiepoMBn5yS4T3qYCBrOQS8El9HMdg9TMrlFxwv4ZHBcJbMowoOKb6wrcmCw1NioL3HTRxOxnVwrgmcr2Snj0uI4E48JYF7Pv2Yppi54jL0CrvXw4_X6ub7pZEn912PWpClRFR_Wvo1AI_xPwCiLy83-AlEJo_zDxpFG_QX_j_srPcyFUpSy4zpf_7h3HF4kV-jX4WQBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1uSboyGPbOStG5EiwczjbvcihBc6_I1huxguqzU4_buVUQm9TUb9Me5BP-toMJcI0tunYJu6Q2cKRJAFXVHjHKVTO_bGQPUPLVbO4V-nUihEsx3M-AELqmCM4iaBKs486IFTt6LXz_nS3HO5Gtl2Xlkeo1P-7pN-O9JHba6P6h6mVY-sZd1mWEVZVH5vUY_UvlF75QhSmIpLM1wV8SC7GSVxObBtrQjoJXBQtUFYrmSnzSyA6BAYd6daz8zygGvHCUPiO0GZQg3xT92K724IgH5d8F4JlMyJbcEO4lpnmIG6ry0E-ZWIX0GKTmTrBeAW2NMtIEyi8jU84oepCBqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
بدلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🌐
MelBet1.net
🌐
MelBet1.net</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQJnvbW4PdHV4hyCnfbL8avtOxw7Z6297cMHzV3_L8tpW8tIU1RaGkxjCIVy7m21CX4ltjQGIY3Tk5TrfPILIuPKPZPM6Cf64IWOuTJDSIfmiwzL863cgUDdC8ih2YWQPswcW_iPXajK4uPBzBgnp4eEEEevFyhxwmnVYBzIB7nKgcn-Hf5q0dlaciqcn-iyoag5U_uExMxpjB-X5C9XGgYK_F1FSPBYAljxHsLpF4EpvfsXea-7xjjDPYXJGwMfWeXEikJxC3-qAllNCiBsBUKyHx-IQoeB6AEqFSU7wdqyThGQQQGw8_RKgKergJfDvH4LJDJCgUlpAY7TZx9JVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oM-xOesnNoUp2EZrXQgofdXDiub2f8hlTzjCehCpWrAecJKj1e6bFUCR3D4rq_GcBfmgPDZB4z-y39BPya291K4ms641YH5dS4pzbRhoFdZBQkxgKWDlJ-wb8XfWmXaLwxh6oBd18N6iQbJJD3TG42hv1Ts0YPOLNo2G1I-86FrRaLSNN2_hIisT6y-DSDWn9kGqgjakCZgQwMwMKVEfLBDCan2FM6m_AkOUXdkRFgmb7OK6K0mTAwJ7VO3JjB4BtyZMD1HcFRPtYEugZW15VIvwQc6q6_-RG6oDlIuluAX1U_DDMxmoGUOGXCvgGk3oK148YbIZdv9TISYR0mc6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oM-xOesnNoUp2EZrXQgofdXDiub2f8hlTzjCehCpWrAecJKj1e6bFUCR3D4rq_GcBfmgPDZB4z-y39BPya291K4ms641YH5dS4pzbRhoFdZBQkxgKWDlJ-wb8XfWmXaLwxh6oBd18N6iQbJJD3TG42hv1Ts0YPOLNo2G1I-86FrRaLSNN2_hIisT6y-DSDWn9kGqgjakCZgQwMwMKVEfLBDCan2FM6m_AkOUXdkRFgmb7OK6K0mTAwJ7VO3JjB4BtyZMD1HcFRPtYEugZW15VIvwQc6q6_-RG6oDlIuluAX1U_DDMxmoGUOGXCvgGk3oK148YbIZdv9TISYR0mc6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-Qx0C_LWnv4qoauad2K57zrbk8EEJfaik_TXLmp3UpmmIpozI34tO85hM1SzWB7XpO8gSK-1Cq2-HGq_W0TfXqpuDyy-DaEhnnOInybVGkVLGJMw4A99zWO6YHqjqm5YSMgx7o38NEcgDTR7Vr6-Pr0TYu90zYVGi79P64RG1jR1GVg1rMwkkzryOpp-SMKOVOdG4KQLZmHAegNfDDYr33xkSIw2stuRRa1ggbNNEVmjLltT8Cmlm54aQUwqLB-VlXa58T-RW0KuPnN2zilUSl6w1xznQqtZOC1trJMnN7XwF_dIPosgo5MAey865VnqJSJDrPCj-zWBl0cLuOZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUzv5sbO43-MGhzXthEccAmbdEpVu_-Ky9UPsq4QIfJIu30opvFbYnhVp5Entp2wSyqVmwCspC90k0X5DsyiXxpv1U8MZEQ6ZDpCnMe2UJiE2Tapf5YU8puhGavlBWJ3WF9gfpvQvJPqXpS-mSD_UVb4eN6jkixD1Y-yiSXjTihUk8QEos4tpTELRulFGzRNxsQQ0Lo61RHHbf7PDrSBVH6saMUhNL2WIkMQlq57REhdMWIAyvdOTmV4agp4P32Dw1C7V-pFqQpRve_Ivd398sachWx-lPRcV7j7VhI-AeJKzfGAXF9Gu2RwycujXYh_nbh0Z-gXfRX8uL6j_XVWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTUXs81CLrhkOhO3zXPvr9UTBQtv5RFoT_zuwx3oLMfRr7V6ZpLpR0ahTMBZNcaeur_iFcL0KYnfsRdk8GAKExBYn6i7oaAFPKRd6GwF40gJa5f_CONnscUcbbS3ADbP32Zfky49f-Dc0B4rUcFsLrMIbBK7AWUNxIETzS00fvf5i46_LFhj1FliaVqf04YGspCrwoCb47IVarY0IatyrPvaMwwX_SFPhVdAbj4zwY0-BIszUJghSVPgNLr5F4V0CCTXDN4OiqRR-bpIDI8kvOcS9B8Uf36ttRBq8lMvwImPiTfs4168RD1xZKqZO7DxTHxDAGgjnkG3-SsDUWV_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu-ds9iLQ-1L4T9i5a9PTVr-fqZ9narnEyzAq8DmjEy7VhSbE1p2VY1oH1W9f3jp7km2e1_SUE1F1ofOotCheE9zeT_8QHIygRnmouL2YOHG0EDNW0oIY4SjW3xKThvhkTRedd35rW2zKLVgrS3OvGEKmv_UotdShQ5bnKRZtuq5GFrrX_U0xi0Nquy_Cp8y9i_S1vU8nU0ItJd28rz8sLP2BI9zxDP5xWhBqVifLIgIoQmXU05S7eQB9yFVK0kBja7qQEXRopO3IFiv-O5SHPMUw262LS9hmXDY7M7l1VE3o6ciHyyO7mUVDAwkcoNOUfzf4uv_x7vCjJHcw_Ykgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOkuLkMa8djLHtL0TKobt53Ho2_fR8ZJwuvjJexqFVFTzExUBMHMRX83grAkU8s3CC1rBi_U9aAqvBiuSRnAbd8E7GWa8XlgRgAg2Nkw3BsmYr5vTgLMvepIPBWCmTa9eN40BTEg8YaXYNcKrZMBeVxoB--Ve1wprk91gPbdC3vy94Z1jc5nnbInb9wFz3cTystWc_RnQkBVgrms04ArXkuBhJJUBi6sFjt-fjmcUsvFZV9RT4BLrgx2Ws4i6UEddBbiUJROmQk2x20ojsJc9essx1tDC4HI40REjDsD4eDvqclf7lR42AGYaP-wcU2bos3DPdqGOCGLQ_dhoCzHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZABlZd4IgFaHPSbLhBugzzdDlfJrHNZCwv7GRZ0bVEjZ8r6Npc3lKc3s4djgClYUhe6lsgd6M5RAoVi6yMry64Y7hkfCLJrSC3E8dfxD2aBSgZyNLg49clmRP9-TmQfvpYbTwsfmDI3IX-3hgu8auuDb-16OYN8QPRPgJutlLdWB-FrH0IysCtj_RkzliglRHKRIhvCeo-LU2QEMzxJFuHsvu_CHoQce7lY5uc8bt7nu-edkg3IUWudNvLL_uhvo_Bko78Wq4z-5k2vS1plBLT6rRWIJIzsTTeyle5V2nI6q7XiyZuE5cZ_ak0A3mD7Se8zEm819vdxEJVzA9FDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkqEn19KUHwwnHBsl0ZM8jwwtW1-0UWubnO80U3oKaOa6IklIm6rBXtIWEqud69qxal4ctQNygjMgXq4yDO1eAfh5Wsp_tD5Qulk7rLao3rGW4uFDusD5TZXlHaU0fIzXU4hhWrQOj5GJ3g4Qz4Ha_H5a48YkdBbKHQtMLIgT7coD8qJO3MapVQBsRFhHxgw2_0MMyHQ6Sz8Crl-5AflEeDiYni7XZ6vDMiY9TaT15nr7wD_pLv8XnySPC8CHE1kci-LW4ujhTXp65DtZXXyC7YWhlmmCvlRavm4HsU7q8yNpJkGLxJo2wdLKHOr-gdtxa4V9GLvWsUtlFE_kZ9isQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWH429dZwS4s5qGqqkrrP0d3A8WscnzjtQ5aVBYxlAwQnSP9Ik2nF0XK6rMCRu2SOFYYOOZ44AAPFicuoK09XY8ZLOueu6mxolNmGWZCIavBmJwfBYtPZ8nu2cdM7zL7zAqkFA9VAsiRNpbRAKQP2apJDGEbcXUEo9NyiQeQ3sbXPu7AcTbGGjDpEz_Bu_tIPZwa7xdNGY8_q6t9b7ylieaaMGfh6bgeftXLjdHqctHHAJtfMXO0WapaDV6SR7lirZtGZzj4hrHEa1CSPs4a3reYA_pEGKd6PBBGsyoYFcxFw6u8MTTp6H2HYmeJJVmS5O7TmVX2tL1lEyOuO430w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPSqT1COfq9hpHL8IKZnbC3HtB6dMyOxPN1MS-xIpkZljs-Pcjhaz2jwLrMopxILrh7iGzFczIGk-BJGkA1uc5ekhTuinDEMldxWNlrvsqvUhPMySisGkAFAddmBZA9c9Al9_wR8aORgeRTPmbreq2przpTbH0Z1Ejjp3c1lEemE8iHd4gdYSmGieAOQNrEN6HKW0zTJN6y9nWpzVpiYbPt-CnF5KQUFVxATUSNCFQRceZL7-nCjs14LumOlN4-c-_DTjKMM34kBjqFn1A_MQey5RKueW06Q6eTsIufhJSwUVX1u5z-dS8w_yG7rtDCgkhyhxNdgyl6oEl_7oBQ16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIYKqOwyBm8Zem3Y8ufJtPfdgYd6A2TtwI-6KZij_OAYObW88XFblGtdq9apomG_n6qgfYWkETDxpgHk3L0oMMj746MeEDHI-oJxpZ8oaCuW3iIcNTe62o0A9CMIr2PHn6i2K6JuCTYf1c1naN_UABE4p6caiHFuRXX_cBFWZLf4qlFKzjwqRhFeA-5AInM74US860nz-fdSVepCIf_SHHUH6IdVfMsoR4aHGVewhacKLLdTf3gsWQc66enXAG0BPR3C5jsHUUCIrUfpVioBYD9tZuo0KXd3HcCrjivKXk_8q02MbvO9HV5ANLah1Y75NVrsMMM3QCqicdmUjZUrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW9GTQETuf2SxHQ7ImkZjKHiNP8cGfbcycQC5RXD1ZemrMdoGQGxekSubwAes7ER12VPPELnLb7TQ3jpyD5xoDs0qlbasknFfvZTsBqGKBNrvjywxusLXjkUmVpCPOX2jOq5QZZgUDHbRJCrQPHc99qwGt6aRho00t9Ntp7Er081dS-X7piLkAXjObNQi3UQb8IJTr-fqNEsfcsJYoZxu6P7bM3GFK89svcLiIrpZ1Yw2e9h70V_d8sqLE5v0cUBupTSigRxEvu65J8trvdCK24Sn_vXpJauCKGLnpvclOE4_HX98lSk16VpzLzqIJih6ol6RGv5-mthnKjl0f8F_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of0kmnMB0AHTyeKlop1VnduOL1BP-KI6GLrAKmw7nE-9vNU-MjZEevMpHn90dtQoVMrzjTtfkM97w7wRZKbFItznMjq7Xii-e6bM8lGVNXsWlyiO1pwa4TFFDetdhE0Lsw98YyhoZA1rZGF4JuUbH1t8S8-mDOGcL7cbdEu0GgV-HmvVRrYl_2tuGv5zrwMOSoXmH75LWXUDxlhDWZrAoEhLftN_EAytTH-nu_joqdkWnA3jFqYcoq3JgFvuRgDetu5i6imodTlVXsD44PlNnfmUt89YFFWkNSqOMxzC5bFHDtk723UdNtOPFtm5sVuCFCzzgkx0A9fI5NsKgpxU0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOzryHWVh6weTN78NUdWhdWQlW_nvQaL4mwk0Ivlb8kjnz-ZySOJ-hJA8jdb26Ll9jKFYKaJYV6XvRqPFfuuW9bMUqYi-LouLiGjdf-NRe6fX5clE2uz-AXXmy6VldPW5kgnzEatpvIoJ5QBFjfdNECzjOoZVC0LCa_H4_Dfkevwxs8pnEAVPbIsUyKECCCk8K-2M6ep52f44fIEer2txwyQYf6ORWmR0Y9JCA2XJmU5vPV6dNA62pPyluQ7I3LpxP9RNhiJRpq9P-9yG9suOgHXARaGtXtUz90zRhxw-_Eecer2AS3cZqe0ZuPLyZ5hLqh0bxnzdJlaCNVxaFwtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CYwB1L7VtH6M9BREnKsyWQIjFTce8Bb5t_XhrUlQKOmQ2Ce_WHhSlgcZT8F6gYgi5oPAeCu6dxx6PbBcW166fBFJTtS7SP_qUAljBOKBIDP88mVF8J59G9eZdWoAnDND_0HG-7Pe6BMixUB8wTgzDJbbudN3tM1eO13C_k5uOSHWy2AbIU-cj50Eafq_60Noby2si1hKpoz9W0JOo7PZ8qaowCX4fn6ZT03zwRa0yNRd-YQBcgqzQrjLUkZCtBlqphv5-JFFpz1WhaitdEyNaCCWmii4mLnRE4YP4CA5m6H-9vMF3iLvh0YCWRIUtxNdApU72QfaQ5242HOyxsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp7Fl1Omo36ciV_65P8RFO47kGTg7vQLXouR8VXZRZlONn9G15gwixsBXwLlEMw0AXcO-orD7uj8VmxtKqVtVT3Ez76fE4mQBpOMpj5r36iwEmMAE8L5D66p2PHv5BzACZ61CzbwxqcX_vXKGaShDNaD8N-zY9z1ZkF22T1liy0S9N7WZuxYgJguhY1uglXv1Bhdk9odyL3MGlgkS8ZWcWiQq8LriG_HdhOhstzxCKQWHivfHgzpahcZb2lKAjnB080Yi9jqebjspnjxFq5-m_Ul1NGxGN4aC6D20jQ5XD4ue2jcB2t3xWIvV6Vc4Y4xqmnBEso6AzPnKb9IaGfuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVYMcKRql8T8_SIFeI9B1BQvl9t_5wTZTZp2bMZHfMV4-4EORQ89A4N-IwPqd3qlImPDORpogA7o2GoMUNAtYQCwrHwVizGDsmkcPEBEszd0uESk1Ju7ISHr-7n4SzFNq5fwfycloCpj9C2MPOA6dFAIn5L24yDznTlg1BrNCLPNxj4k5syrrabRP3w17y7og0tdv2Akea2AVxv4WnbWwqvx1dgtJt4LB96gqc_H7pJRz9HC6yMD36Ncayn8WwKb3h9OGnBBnts2cKDZVNkYprHlxgJUukvVGuXKxUsD6xN6e8z7VQ2lFt0_gOoWW3zFjy6HSoZGUDsHmW5mxPVXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cM_Uv3pobqw2Mz7yvs4PHu8bcqecKVmF7aM-wiw7eaXRSLX5g1Xawg2-iQa7FGhUMb-gvxi7YQLCD8GD1YVdRw6jtLpjQwKFoirT1Ek85ItxmCPF5qK9X4H5lS_0E0A7SoTni4OKcmY6LPzT200IC4wue43wsED4J7AWrldiEEZ5Ov6Vp7CgDrh1xWxcSbVfjMFs1K3rISpni-eUHdbpk9_ZVRqUpF1Fp5dIYFcwf2_QmWrBIa8E45oSeGcNouv0hNhpsi5BHmaTuQTotuydRDBDk-qPVBCPQwWTp0yyOHXHXhtoLZwJlUHSDWL1u8inGPxgThNLwoesu14mGRRcKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEAqnzZD9FnZ5uXkBocyQGQl2NorprL8Km9Gp2fOYMwugHvWtNtkBVOfLU4Rcczx16jumWlwMICauZI1bzY4-zoMiE1ZENoi8n95YokCIVvnjnT3qVOm9x1RbuFi0Xgkham6Cl_Yw1oDwyo7D7o4GzhQJ32BG5gXF1rwKaGXAl9vtZbQzbDuUT6JymBfn7LXDQdRMKm8ux0DPqoU6h3l0nRtndACEobrFuJV1bmTRkGSAr6VHBEyEnkmtKAvZ3GVphha124x0aQw21F1JT11fWcfbOXMYKiPtV-wMLOg2_bl_MxmlY2V9mSvDoRKLR6K-5Kbt0Q6yNJyR4njam09gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUAZM6tevkjQfztqtcM3p36QP5IaD4HQc8DHVhyiB0Fbn7HlIic8ZoxpyX5b_Sseq7ttlprFPbk_RTrU2QP-a8SKW6Mt_uCy5KSm_taVS4GnYqT67YYmroi2MBHztOnglQDx73790wV4BmdMt7TRV458DJX_g1Il3r8h2m1kjgWtaJIAWAYK-MgsMq5K-zTJIjpZlGb6mzp3VvdMuOPC35wCVvsPCV-Rvez4YhBD1Xs5bV9Uca7NO-ncJc9h5bed4SC09PFAntHcypWsuRc_qAqPtRKK7xWBavh1m6QDUv6-rcyHODxXsrfiwWVoY7b_I6FpjmC2xFlI_dcEjQyBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEKoMh3VybDaMCOT2D6lG_GXvvu3ZNqME5Lul724KU9BJQ7sWIqhk3oblnUjxAXS-VEU2PL28ujPirL6Zv24Sar07QfMbkGDeRsbdTlFCQQ2SydPi6F0cA1pHO0bKbdM9SL0hzoS9NXtC-fzpqkMwkZC-XvH4o5KuVLofM7fWmGEa4ASK6hyiPNuhVgDsg_devYNoyRzQor0cycAegEOH5KshHWoOen-YQIycO6HRX8O13JD7uXhcOyuHaEIUTjcNVLdbNyUQyGMvVztS5KfjyNT1LNKnNlIrfStQP_2lCvOwC3FX_y3crs6woh9JbuS6Ky2ZUohB5ngQcggqNfdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZusMshfXq4YwCzDYZvz_WgoKSYNtqf2ApWW9X2Ao4Yc5OwA7-E1dUEFV-aQ0M4BQHb978tGmsSI49DafnP9W-2IxgAdD8m4vicCoYv5sDb2EKOHrqESVz1LQ1u61DuaSq8zKCbz82azfZPiYsoCI1ZW2NB8GAz6d-ymYxPVAzadoLqNTpbdiTO1iq9N7q1mgspViAoBRdef90DGE7XvH9JuYRPNt3BZhl7WFWtlRJL6QA6kblTw0xGhsonWUMx5c1CZ-r6tJVZukRRn17wQN8ta9keOuOnzqRN_XTjhhjQ_hAVCGjex4rKyHrWSWAPv0m16YTOaSHPrdjaEINmnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZNsPWpEPdt24Qu_16sfvQHofDE9KrWrvV3dgp2r7YMZaoiUNZkT_j1jXUzQw1MjpVxVLfQvfkECl7Sqii98EgBT2zMHXQsKPoS8XtcVlBDxxPN58cgc0_UMG3wfWfhjjKNygKaee4gatA5uMGJa-reRZlUyWitPPYAUieR9q-0XLCRsGW5GB1UMrvC-tCBI837PReqOHij8aYMXV-pDjku9XCaPftguMspdX1rZQVxxodLb4Hkn_2NsH5X_wswoL42XegII6qpVlIszJQzzr9z11k0UfmJ_qXF1AdPbADQFs9_3CugdsoLR2c7pExDlPtspSZJJxk_GiHvf2B0nwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJQsvE89dMVU0Nir9DbygkaHuGiHGGLGXwfGAogueXs2flhPuJx6AaTrOfd2x7Z5bBM0eb3EZOZkL5Rwxn-yva-OUE3bX7qskibuYmK1CgYwTyBj8FdWZ40BaU0I8_i38TCIVfZjP8_tbJp2koUKLf4-83VsOBkutgrF8lnKmXNlxklPdtvDdJ_RvHyg_PpU8Wr0wdExR-P4hDPCIUWdzcvYrpL3mppyrMGeRpayGy6WpvtqJJ54eDyH5XQHDdMBetZKEuwXP1R6tb7RzlKctfI629Y4iBtzDVqaokGmTPYt5T2abkVB5Laz8CSL2hfcb-yl5fuko0zwscZ_OH2x1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkFLwKmdNXeka7TX2w1_DKo1T3XZNTFIiDCEhac6sRbu4xzPbOHQjqW5yl9fpsEyKUu7gOS5A8Jx8yr40kwYIMZwrTT4c0tbCm33Us9RXhYlmN_2MMNZEx1N2W-X6xbMDEyIIweKwclBqwLxHFKKoiAN5zg8U0nukj2JI5x6W4sRbzKz7qovsNBwun3peQ1ids1u_8yeP7SGC6Ym7w9ixAO86KZGanCjkc7XtYQvUzZ77CI_Vr6hVWeLZmHtowU2EYY_MBcSED7fF-CfB95mNeaWZuP7-1hmKgl6pfcTKFNNYnb1EvkCHLV5Koe9LL1k7xsRkSW2KwhRe5jEX1I1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=sLWgIcVaZCrIBbnU9H6nBuKug_F1s-Y4REW1pWh4kmv4qQKTs-3LQarUegKE7BeDFM74sGPFprEnSMQcrHGVxGk9CjLgd7Yzxqr5efJb33Wr7rRU8gZpT_P0m204a_U7xIsRFM-XztzhQ24qs24wiqS2hIdOgxzsiSur5VFeWB4y_J__9lkgXs4gEVu1AYVzn6bKMWLnOxUxOPUvn4oxCW1bniDI-zpVxGcBZEu0pXvTyDgF2JNDx3Tnlfotan1grAXIXjEm3dUN8P9D7BqTG8zIpIPxecX9JJ0EkTzK8ZhVp5AtnxNRVef-TtQEQsBRDVxSTg3czSIUzaRzTl5MSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=sLWgIcVaZCrIBbnU9H6nBuKug_F1s-Y4REW1pWh4kmv4qQKTs-3LQarUegKE7BeDFM74sGPFprEnSMQcrHGVxGk9CjLgd7Yzxqr5efJb33Wr7rRU8gZpT_P0m204a_U7xIsRFM-XztzhQ24qs24wiqS2hIdOgxzsiSur5VFeWB4y_J__9lkgXs4gEVu1AYVzn6bKMWLnOxUxOPUvn4oxCW1bniDI-zpVxGcBZEu0pXvTyDgF2JNDx3Tnlfotan1grAXIXjEm3dUN8P9D7BqTG8zIpIPxecX9JJ0EkTzK8ZhVp5AtnxNRVef-TtQEQsBRDVxSTg3czSIUzaRzTl5MSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjAHK3OrU1HI-_csUTnpqIItejM5eGph8Fg2AqNolSc83JHhcnuu82qPuVJlvwYEUROkUnVc9JjqlBK3uz60ap31BN2Hh5zNS-dD3lxrZbIb8ZfObZyORZTfJLcyQ3Jq81zp8GSqDi7mzJJEbsq7Z5xIRigJO6qpGU0cFagn4X6ZEEvA4L--a7dOZ_NuuA6rbdUCTLrVAjGmp3USrw3Gvszg5spfoZRXceAmNcB-T8N8md8lMMdeAfzNjxfD7fz5d1d_QC8SlJhYJbxf2SdWMcJkG1TFd2spBjyR6TbJtvuHnWjfwBI83iPVX7aWZ0rCr7H0MUrebfBto_yIx-HxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN6pZHDA_KX5q1XFpL8RagSRsQwyKvmR5k1ztninR5yaUTShyDAfbo5kUVxC6UlNLccCZtlx6Vui14YIn5GcmN6dafisrkRMlm6gvbm4i2eguhDYGTzTG2tVTPmZidGqy-_pFe98rzEyQsRz_7eMhrmgrEf4A3ysCxLU4evTWwetlfJGkruXRyIlSCV8ava2FsBkJQCt9iu7Ad12fiRqoUIDuwxaTxaXJaixQktEyMCMhmCuZ4cLfvsvxFvl8ThpzL0P3UoP4_QGOyRAFN3qv912ja6Xo71xh3JHyGhHTKuWwDDmdSVzOSl8xqdD86Uxn8Hjf9e6gWPKY23RtUNTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQSeUsEgY6o3nSKgIjdDtAVYzPGZo1AIlqcYlq7y1rxxEyHYf-p3y_1IkfKGUfIdlmAxF5CQUYVHN1CwCA_oVo09HCjwOKRdWz11lwNBMHBgt5WHH23a0-GXmjQvNnQYJrRhuCw8WZ3yFYU-XGt6meEhTkffXrqv6HmI9YHbrZQOTzFx90krM0SxcV8O-NxfeUxtuIwr58LMkLQoqvbmuz0nKsHOLZ7jPd-cpLcvKehKtI1AG5G5lqssVsQZfT3eZ3PyGYkbFZDRuNFi6hGuY_V5ggPLfBI7iW5yC6KRugFDqtFNc-wDsHGUKhUDPLC7JnJ1lBRZCnOzfJoXGLCOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUgh_LVMVq_2XdUZGFyB_i7BNiclPP9cpSP0NXg1PZMnNdr720f1ad7CeEBGBP_8vRYtgULK2YyfB_XakIHUkOZgVoUmzg6BsFZM_caGE8IwpXCz-2Mi6SzpBgvWJ8-Wkp4XRUgKlTpx5DnlQH0g70Dce260kJdtH6x4M8ktPs-jZY2Ub5jehwnG0L7f12CWoR7-o2a9Ud-Bwc_jpBN5YiKZjr-eVt1uMIRujNlzQToOaRlu-KphdHRMKyXTtROmfBTjY3RLR7EWizynG85d-WIFpTLTeZbCieNiurILnm0DFQVkln9DbEYf6L4KyJ-VOpPe0auEfiuZDEpq1vCzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-VnJLqBt9ZiJPr44T7dvtU_wQx8bRUQ_TKZ815UMNP8QsttS62wi1pEsm0nZVVRfIJ60ZxN3eogAu2FXOtGtji3RncgYwHhedr-AnUwPH38VpKh0magaU1I1EyrhXqcsmdlgpo2A-50T6cBeS9NlzABDYu8Sya8ZfhQ8ta0xr2gBtAfpmGTzILdDhP2-SmzWwacu6Z78CJXtQSDetCuKnDwHUN7jmK_NUVM7zcR_Ef8D_oT54pIPlL9vxWKWk50396WRm0j9Kj_3WNa7ddRMQqiZflx8B85nFADCGHmiOlrqzYRlOxAA-IohrAUgy67e_f8ncBCSP6K4LtPIHex0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRBkpyqHKd0s36k4L5lrfPMLalnt_u3QH6KmQox6m9hoku9wK6dKC8R_2MgWJvQHvoEmPvMkok_qieVHU9uC5G06sr2sW4FrDRs9OPtHX0a_RUNYoqk8qsvzaAVcQmUfHGpvjuwjrAPxXEq8Ky_Dg2yIe63SuFeg-C5KBy0r_dQ8twAbFGgQHRRY_PB8ujXVb7kLc3Cjd4POe4lngS2q-0IxG2UH3_2B-zLVMBbFOgkO3CXQRNub32Lgkrvk-BI481zvNDw6epVGBhALwkWJb-I3dT30lNIQShYx6lw6jxiLpiOZ-0CIV4Q-1WLtXJJWOTZLCK7e_yo-z57XGvH0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCg5AwCpqZSK1izpv2j1Q1Cz4TbNuUjP7fhzZkDTp3ZxlmMMyw7YJxguQDtbSKxDe6aiGjbJiYErPorJ_ep7_zG994oP4QLyNoYRx_VbOGxszBa7Ng26ChnKte9l5kcRZd3b_tQ7ayBA_vZxsCQ8E-OnCAR9H4qY7jSuFh-reHORVGqf7CHlpsQjtKa0nKdW_dQkiFtKf2US5tIfkOs228Y2U4a6RzZJ-RQlmGoS0aVCUWklKo6_oX5xU4EpKFu7sbePEVVXEe4a8VN2_jyC2hOhrSFsbkfUShxoKo3jENIhXS-3XkQSYGYqntEJhFbmZqH83oeeFOldTJ0EzmfMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2DoWs0UiamYn8gk_KcFfOtq0Q9U1eMocNYOJSfaDkqE3HfVybO1YXvHemxYg268Ji7b4zEnJc1orLF6m8zlZA0aZx7-TMw3PXE32Y6H0AKcc9w8enScQ6Pd-Y8BCr5fVvmIqxIEAJkDtTZqO5uKRkZg89Atr6fXTrPAIixDrlu3RpgrDdUExXLZ7b_qyIOWhjHMQ32QTPx_uUfm33gmXIdm-9vkcUER4qsKuFhnuI12BfYLVwl5SFLSXoQZKtD0xVGKRhca38rq_jjAABbUcxcE09Ke7M1XOuQE7tnbs2tchMUawbRgW7ynDcSCDy2nZgehUhK7g0trn7IG3RPgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6K9kA385B5ZiDRn3kbLYa2MNX4QjiKD0Vd7w7OWsTC3nDGt-QdEXcriVZf18rLyGyalYf9HSPr_TRlUNgvN5pYeE7UC6th3lRsX4h_WCpu2C1XitIuJHKjG7CKtSfAbeAsvwH0wqD7LQoWQsrvKvvRLvJBljFczkFpJGg3fGWn4zdzz_g75W-MjcubiPyt8aq36efDESJe-LfvS_rd6fjqAT_O6ICy8sbjCT2uN_241GAtWMZm9byjoryanqP1I-329Q48Vy75v6nlQqGeuxrwtzwp_oJsq9U1mIxrAZ6RsgVRMCdp_Q_UlIXFrXhXmRDeb2Ru4-CViaijuuqeSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgxvUjveitpDrijZA05huqsY26sO_Rzbojp3oFnUgl27_2ako3UpiH5Zuco1P1RJ_Rgg5yShQHQGkS_Dc4QVQM4b8Zh7cxmU37ue9LVY74I6jajImcIr_73gPOaS4b9-hTVoJZ5YgOsvOTLpHctWY3JjcesV78ieI0z10PJqgFYk16LOB8JyT1WbKNdOdpz_bVshYRwR5vDTcZaXL4GZ9R4Do4lz0c4LPARzr47QaBJucQY9oIIN6UJT9_zMgLs4yOahZMhg7xCUz6rrLfaOr8rnzqN50Ul9l2H9UI8jeXMp7KJmFjqGIRCKD686gnb-HaR0Z9SzoanMiC_Q3cANGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=oB8t4H0G0zVS9oljUeJTRXq3DhhpNU6lITBgkPERI_Af-LAlEGI76xWp-F8Ilx2H6lHss84bEzCHQzTvqlIFJ6yNKjuXFGThAl9AJ913SnOJBbELEHLHNZIn4-Pv2_ssMFSaJ1XS0JdD2fhC6hJIsOPfo1HUP5BZy2grkcXDsGxdLdnFQYIpIthULvTatdJJNrLvzi0tMelfrLqvLtfzD53k6kON_hA6o1ULn67eKgjeuns1u97wZNIGIb_4WI7kcesigiQvNR8IbYXlKm002mpIJ5z1JZjotnmpvD1gUpyHEQHcQOOqI_VqViWPP_92zHV9yIa2QLsgPeIN_9gFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=oB8t4H0G0zVS9oljUeJTRXq3DhhpNU6lITBgkPERI_Af-LAlEGI76xWp-F8Ilx2H6lHss84bEzCHQzTvqlIFJ6yNKjuXFGThAl9AJ913SnOJBbELEHLHNZIn4-Pv2_ssMFSaJ1XS0JdD2fhC6hJIsOPfo1HUP5BZy2grkcXDsGxdLdnFQYIpIthULvTatdJJNrLvzi0tMelfrLqvLtfzD53k6kON_hA6o1ULn67eKgjeuns1u97wZNIGIb_4WI7kcesigiQvNR8IbYXlKm002mpIJ5z1JZjotnmpvD1gUpyHEQHcQOOqI_VqViWPP_92zHV9yIa2QLsgPeIN_9gFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcR-Lah0xyqRelg7J9mIlPJScKrfxeLRz-Sdi_R8tUBDjB4YpQcj3YOhneRCqxvUOFvCEoCh-nuI161mGn46NLSacJmqVJiyeGfGWJQWuGusY9I6xfOg7NkiZ7WCOcpR4-Sn6IX_KqxMAZhr-M6zOFvaz52oudoTGF9FcFOm-K7lp1UI-i92lZ59vyqSZduf9sTIAuBqOKxTQqzYl_T45aj6MT308TQ6GcsL9ctLTllXilo_K9V_YbopU8QQp3ljA2DYTN4RvbEDRnl4WRIH-MyzMfagTbCoyENPemYMQcjdEo1Wav6_cwjkHR0jC1hE346n5-kOl9OkWa3QdVYw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZpUe4d54KpojBhfmLUt1YU_4Ywkadt3fevZQRmMr3lIAdUzUN-AmJQitbC6yaq_Q5X018k7_nYoL9NIAUQ0IyorKi_chsMWAglY7wCjH1uuV7nZuuRuOjG9zKjORFtGPZhmJEIUt6Y8mNeXVPHySzX7iT01zo17THB6hJiJtxzvkPMhP4uAiMqtLaOabLF1TX9sjXrPOVymBb5ynR7LQK1AxK-M0rO5THMahuGyHsTxx9bmhqlyqfIm6by-FcDcR_KcFfvxRNQpwFPRwzC_7Do1jDAU3FJIBCv2vzmKk3lhckZ5GtiU46NM1g678NbnqUS2UFGi8Gy_o57bx9XH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=O9yjKBNc-I0KtTMo8LAkOD5WJh5-2TjDGcyUqpdw2qSOKvpF2KGy-M09b26uiodfhOVEuDshMs4GrFRgEs1BL7GxKBc5xUu1rYkparyCFNQ-2DOzcADMJl2Us7X9lzwaGEU8SVaG1vXhe7f-snftxwW-Nd6yB7kWMBRp-q5s_mVZWJH7EHmThoi6mgVyEwGUEoYgTghtpEixBfqsm5XQSlkrj9qqqSRbnWry1o2BhJBwxZ8M_KrrxaPRhaVUfXgKB7ic2GkmeQBiQem302xkw3kUYqA1LTrnacCyCH_F8gEKko-LsgdM4h09GJAcIQ5DkfVERCpYc4i67GaETYoNFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=O9yjKBNc-I0KtTMo8LAkOD5WJh5-2TjDGcyUqpdw2qSOKvpF2KGy-M09b26uiodfhOVEuDshMs4GrFRgEs1BL7GxKBc5xUu1rYkparyCFNQ-2DOzcADMJl2Us7X9lzwaGEU8SVaG1vXhe7f-snftxwW-Nd6yB7kWMBRp-q5s_mVZWJH7EHmThoi6mgVyEwGUEoYgTghtpEixBfqsm5XQSlkrj9qqqSRbnWry1o2BhJBwxZ8M_KrrxaPRhaVUfXgKB7ic2GkmeQBiQem302xkw3kUYqA1LTrnacCyCH_F8gEKko-LsgdM4h09GJAcIQ5DkfVERCpYc4i67GaETYoNFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAIdGL_9_KaWB7HCAiC0Ig6zYhVSB2Svzze-29oeQf3uxrtjIeZOEBIlMqhVQG0WL25-51XXxw6QAMwjKg-PN21CTeggZ9fX4c76fWejPEakXd1_9vI4CGFfpsBQrcx-Vo3yu2X78yj_zwGrUsmS5VzKa_c6jJK-wzYzsfBSfasv-L_tooMT9gX2rcx0pSKQSlRq_-t1xvZ2UM9fEs2zG2e_PSeCTm1BVLbY3MIm5yXSeZBVtDbm-FWWAcb76JVGnLOlJNhAwh9f809NwNoXSV4O5wZe4aTMF1WlD6xgcp9QqYvVZib8HlDAyBVVtLXc8nSun5W6WZ-2iiWEAaVb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5NIXJ6ZcZkxE9z45djwFSWE5Efen0RpuaxTlbkyLTeVlA_G3vzRcuMlhmBXYg0nxFBF1YaMovdstx08354EtwkXcCZ5eeEV_z2iBiqo4IvT5WhvNQGV-5Wh87G1VGsnMmZjd3OhvgepIAW_m1xgsVvdneDTameRUScRTMJGJjehg8LxLkVuHax5nUetHMLFiTSpX82oxoQsOCNzs0HbxCuPEi8ALRZpX8Qe2Lj0_1yzxgZRAZFONkdXhCbEYjrqYgUpqc-TmGJVf4FXwaUkHLpQOACvIYVZb-hxRH9ttQDR3rGTxQSJ3Swc9N3KacfG4I1UaAmTWuFvJV5UvkxzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=bOS9LAuf4p2xArrzYQH15WTfOvOrh9p0jfKMo4CIYk0hbbu9GvjyXnp2HDUdip2O740zd1cVHDRf0WrI62hraWJ9WYzIydfYpFvHF_49kA2527lQiCjeCsy-rgnJ6SDWr-1lV-CH0bVKbijPVXtvxB72-JvwAwE4h_E4wHvh8oWHKLNPvv_qzIwnKUFRkF3Uh5lmwClFTtWpdI4iSR8QlYEEF7b7P0COq-FBOxih621-LfNk1kbyVLLizKyvln2GjSg1sz8oipKSkBd7CIMCMQQOOPEAiS1xy-DWoZ_L8_2UfqBBOffSbcCvmiij5T2Hiq2LDzYAeS77VIcu5kYigJmQoWOM_fGaM2QDO9JWE7cMTHFPhZBH_Sen34xwwjB_-4igNYy_ypYlR3oJSQD983HN2XNQUaKOnBcmSTJLzN0rnhQXwumI5BII84On-BaZmKt5wFOGS0NSPqVxDtRCSTiuYLHsupzekmj5H8S4PRQ3iMGecmPLQZ8IahOt9OM50qsWI6pEvjkbU5NCic5q0vbCXLeHARpJ3OsneALB1kbiu5_yH6LFrWg73KHfcr2WitxkOHEHH4PxnoZNHYlJaI9Iw3tEaTrBployxrq_-uM7TRJFs9CERHY7PT7DTmQA0OUuwsCcLICb_zdvNBaCclv1FCp-HT0NXthBn921VAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=bOS9LAuf4p2xArrzYQH15WTfOvOrh9p0jfKMo4CIYk0hbbu9GvjyXnp2HDUdip2O740zd1cVHDRf0WrI62hraWJ9WYzIydfYpFvHF_49kA2527lQiCjeCsy-rgnJ6SDWr-1lV-CH0bVKbijPVXtvxB72-JvwAwE4h_E4wHvh8oWHKLNPvv_qzIwnKUFRkF3Uh5lmwClFTtWpdI4iSR8QlYEEF7b7P0COq-FBOxih621-LfNk1kbyVLLizKyvln2GjSg1sz8oipKSkBd7CIMCMQQOOPEAiS1xy-DWoZ_L8_2UfqBBOffSbcCvmiij5T2Hiq2LDzYAeS77VIcu5kYigJmQoWOM_fGaM2QDO9JWE7cMTHFPhZBH_Sen34xwwjB_-4igNYy_ypYlR3oJSQD983HN2XNQUaKOnBcmSTJLzN0rnhQXwumI5BII84On-BaZmKt5wFOGS0NSPqVxDtRCSTiuYLHsupzekmj5H8S4PRQ3iMGecmPLQZ8IahOt9OM50qsWI6pEvjkbU5NCic5q0vbCXLeHARpJ3OsneALB1kbiu5_yH6LFrWg73KHfcr2WitxkOHEHH4PxnoZNHYlJaI9Iw3tEaTrBployxrq_-uM7TRJFs9CERHY7PT7DTmQA0OUuwsCcLICb_zdvNBaCclv1FCp-HT0NXthBn921VAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=Z6Ecs2hU0645yCSG-yZaUiZpsOd6O0e6wrCeIje7JgVfhJqJXS8qQIpph7aWUsfe8dI6dQq46CiEVCvqMFhU1hnnSVObh-P82oWQtoJo7NctK7SaZpMD1EMJ9lXHvEpGB01lhMlnhQfjhw4RBPoBpEA4aC7CvNt616Ktu2PF4EMqYA97CdTO_MDFnTD-IpBoYbojQ9XUYpVY9FFMFz7ZVlbbt1LwsZUSHHoanCqI8RbuobgLVl9J22Tj-pZv3Y3qTqHUc1pwca_l3UElKMw1aebF5EN4yyC0wwQh5ZupW6__7AWMTDzbItv34NFrPJ3FfjVurKuOKWZA8AcKeuOKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=Z6Ecs2hU0645yCSG-yZaUiZpsOd6O0e6wrCeIje7JgVfhJqJXS8qQIpph7aWUsfe8dI6dQq46CiEVCvqMFhU1hnnSVObh-P82oWQtoJo7NctK7SaZpMD1EMJ9lXHvEpGB01lhMlnhQfjhw4RBPoBpEA4aC7CvNt616Ktu2PF4EMqYA97CdTO_MDFnTD-IpBoYbojQ9XUYpVY9FFMFz7ZVlbbt1LwsZUSHHoanCqI8RbuobgLVl9J22Tj-pZv3Y3qTqHUc1pwca_l3UElKMw1aebF5EN4yyC0wwQh5ZupW6__7AWMTDzbItv34NFrPJ3FfjVurKuOKWZA8AcKeuOKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpKJYT5-0DIvg5GUMlXYc_EdTom3yjyhVHIMbZs_Kpt2Sc9MqDuVBGw4Ms3i78dtIdaVS7-OE8zTrVDv1jBhdghg91zBxIUl7wERviFHIUvgAGhJaNT9uwK-Q4D0M56pBG__Fqhf13ibAE_cVkYqH-glURwADw6s99BuxbTk6RG91Jz8QNjgGAn3xFArpHqtSV3X4XS19jlq_BFc0EaHivOOvt8fpFnsKBucKpStfEJDtqlivyYr3BbjM_UWLDBrIfQp8kWIb_Oqssx3xJC_MGlCwW-_L7t8WX8YKZgObROREzql_wtwfAbla2ZXPdTQ0QOc5L052zmQsmBjlWB90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ea121bqmvpyk_RM3DMJ-d7Gm3Y_v6mUZGWl-6cLfSnlMk4YyFv8oL3F500BmIF0tHTuNc3mbXdOWa3Vh76bA_QYQ6S7d7nrr3yYYtMq_R4zldqVxTZBHq9-i54DEzqNsRABElPNE2ZRqENURLGso2lPnX7FNIbUL2lB2f4Ctu6OU5D1JKNen3ByYfdyP2Ac6FqgLahdwD_CIRaC3YFMzxvvv1LIVENj6c1LdVUhJkKJkLli-UbQxHuPd_LHuxgjoMzZXB0sTKnsp7ypXhhshMua0qVq0OzgnOmU4l7zxzlEmDgQD3gk4CU0R8wZ6-1tGYK-aPzH0lNV0Oe7KNUrBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpK6IiMxKm200OZsNRs_XQHFnSvUA9CXACEwPSkGMfyy_WMX117OCpI7a5y-QbKdBkpl1DHSFZDVsnlFt_a9WkxxRajOEih0RozqtWo6hkbgG1HIAwdCkE6F_zjeMbAqJsAMttB_-7a_jyx5KVaQWsvIfCZkq_crouU-h6cD2yAP6XR8I5pun2nTPvvShp4uwoBuxB3LIE26tg2DDSiI17Di6HdKdl3geHPgHLZrWDo77qR-QLSL7Lha3_1vFnQMD8CSn_umPnl5KtOArdtXdPjfoxHtTqiaGdA5e7Cz9aemFVfzbGjHCBID-IG2SkxnK0u09HQBxWp-KVQEaYh44g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffVJ0r6v4bTorphPWx8Z3xSznyFmJ5WlD1iJHpEjI3xmzBotm8CvpF6kGEljD_GoTeLnNY0ILJnsj2ksoUNjtgd9Bc7yppAxfNAjP3smcKCLN-9dV-vHYpc20JrnI84_Qt6ikQi_Z4-7yfvsttzsa4nH6e7UqlIlYrJcyiiD2e2ciE_2mghIrXFtG8BSQ8TACEo67zpP9pSIq0Nacf7ClYlOboxupvsyDcyxsz7FBzTxbjG8xHAWn_NiqMfQ9NXayzof9lyr4UkqVqHbUrueYfpmaLTMp9qYJFqRbUPz58mKqJyJHOFsx6OVgks_iFamTG1upHx_reW53h57zkx-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=NZT0Dc-3oRcDlYt0i-PE5IM5G_6OXw7IOBscMlZ_wMAHkdIP3Q_CIEWQSLfE09IeneCTNWeh1pR9WOluT_bx31NyAq8f0siQgB5DniZcm4EcGAUC2ZC42iCltjgtPObs8Dv3Bh5io9y0-6OLrZT8-poV7K8R9FmXMdSuvof9YfVQY_TgvaF2haEFqTVat7Lo1ij8_adFeaqC4fx5YA5aA91klcgMaPaq1sVsjUvOtmQ9QjdWJr5Ap5MNfRbvkRbHW5eG5ycvJpcFtGaEGaOFjd5d3BUBlbTdaujeZunMWXNNxJ3z8ko_uCE1rjs7HguZ2awqk6t-Ak8DuVGKTO0ZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=NZT0Dc-3oRcDlYt0i-PE5IM5G_6OXw7IOBscMlZ_wMAHkdIP3Q_CIEWQSLfE09IeneCTNWeh1pR9WOluT_bx31NyAq8f0siQgB5DniZcm4EcGAUC2ZC42iCltjgtPObs8Dv3Bh5io9y0-6OLrZT8-poV7K8R9FmXMdSuvof9YfVQY_TgvaF2haEFqTVat7Lo1ij8_adFeaqC4fx5YA5aA91klcgMaPaq1sVsjUvOtmQ9QjdWJr5Ap5MNfRbvkRbHW5eG5ycvJpcFtGaEGaOFjd5d3BUBlbTdaujeZunMWXNNxJ3z8ko_uCE1rjs7HguZ2awqk6t-Ak8DuVGKTO0ZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8RfGuUN-Byh_xMAdCXC4CbAppNSK7U_nUBFPiPb5pLUnCVj0WjAe_SuurxyAIgJw8WFXKTKA-WC_7DBmfUcQ-I7HPnYJMx6FAISKMh86nvJQ8j8MD5KYnGn2sYL2y60bc4v2VZrYARcQBqxsPMJgPtag3acc5end-NDeVX_X6ptHSaOxDp4c10T10QkinjVOm8UiAD4-2CtsAGmloH7q0QBVh2QZ4M3l2cMgtfbhGf3YotjIZjd5rIxP3XZ3bfQRGSJYELKvmOJx9fkp2MuC_R3qFKX_2srK9Saca4GWwc_h1DjYWcVGq8GBnO6XBaoNjG-SQ2n3mwExduzSZDSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=Z-A0BhgFXLGbIwX4rwjhSgtsr-V6Ki8WkqnD3GiewUuoRHMhpNdtIn58Yi00HshpkjKM7sgvL3gb0OG4pADOHjQK1ZnQkLEm5tIQxiK-qvCxa0nDvyEcy08TA4ZKfdLhYjL8F31TNjkURGtBQNsRU7nmGdwLEMX_b_lCA4kaYZ58Er0mR36bRmc2Y4woauIjDRnre9KpM39egusL-L5TI4BkUbVc0U7U6AmRCwyEnTC6PDNx9BBuQn1f048cVrVfqcSBXsgCLMykftgpxB5vgYkhJjK5_mLKqnv0tUQd-GGfmbMtOhrrSLfzyX14RW2N3i5oaiSzqZ6s12Y5kmujrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=Z-A0BhgFXLGbIwX4rwjhSgtsr-V6Ki8WkqnD3GiewUuoRHMhpNdtIn58Yi00HshpkjKM7sgvL3gb0OG4pADOHjQK1ZnQkLEm5tIQxiK-qvCxa0nDvyEcy08TA4ZKfdLhYjL8F31TNjkURGtBQNsRU7nmGdwLEMX_b_lCA4kaYZ58Er0mR36bRmc2Y4woauIjDRnre9KpM39egusL-L5TI4BkUbVc0U7U6AmRCwyEnTC6PDNx9BBuQn1f048cVrVfqcSBXsgCLMykftgpxB5vgYkhJjK5_mLKqnv0tUQd-GGfmbMtOhrrSLfzyX14RW2N3i5oaiSzqZ6s12Y5kmujrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud06JJmhAoK1nhqPJjB6JaU_sRbRy4Dp0h0KvbQVXz9WXGv2X3lfzjDKAYaPvAbkXWKyp2sVQ04iNiwok1j1Ho8BE03m5RV5zXiej2t-jVxJlJCureKzFuqmcHD0IiV9gTM3JkS1rqJeusxw-4LfKCzb13U7wIH9SqlXk9bkKWIqFLy9lJktDJI5szgtw-hw7_HzdN7jUHSWZURCMRtW-6ySfQujyKN5__y-mHZ4khyLnLhiSlB3RGzb0PofZGSUhJfj6QwwWvVdjjIugdk5MV6wtXatIpX6zhMebG4DrwiY_NjYmgA7gubkNttoXWM_HlMq5joD8Bi9aSWMxwAITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg5S07MGmg3pZke0wB1sIKcP4qEea_7ZQFKla015EPFPfWYUt24x9cyZRWK03UZ6-CbQtQiX9WcrHQ9n71-CotOEFxol8XuujhSS-tm4gmmTQjC1tB__UGV9t7EHXrk8jotfs4QPGRwrnyyqHq00sMLRq9oBSk339a7WqWTFi6vTJnk-LeCfFsPCrTwegEHRV5tUidi9Jkri2rskDjuWp4OJ5QA_1XCbL2cZ5rlILq0EzeVrLVhQkELLkjIOWOkv8pmN8kcJ1vNOOheR3DcrYrssVkatdJfSvYeLKDoQ5w0YTYST5viL_ZRw5eU0N60t00qqdjIDQxSDtlpsjzw3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=rXtmTxyobCuKCUk2OTmtQDtasQCE54s8qUPOO6-6ZjcNnllIoB1-hcCaqlZapPC92xz3XjcBEyo86ZDIdcLh276wjLlyhV-Bb1lAHsXBF1a4M7b0rwsIkSNnyJ-2CTu6S39lqtxMEiTw49xSY8fR6-6tGKIuHJgiYzFgjE-U8AmXnM5uCyLnSJljEexiplvXrfFMvib_k0my5ctFkPeFj3jd2NmtHXBLisnBhOnrrzc1_GwKivyYtbj_8MzMvuF7GwhYHdfCvwPhovFDAElGNDZQoeFndj4M9nnzHIri6tdJ0y32vbwKnlfo41xAhyq-71ldI65BApCWseG7hzUZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=rXtmTxyobCuKCUk2OTmtQDtasQCE54s8qUPOO6-6ZjcNnllIoB1-hcCaqlZapPC92xz3XjcBEyo86ZDIdcLh276wjLlyhV-Bb1lAHsXBF1a4M7b0rwsIkSNnyJ-2CTu6S39lqtxMEiTw49xSY8fR6-6tGKIuHJgiYzFgjE-U8AmXnM5uCyLnSJljEexiplvXrfFMvib_k0my5ctFkPeFj3jd2NmtHXBLisnBhOnrrzc1_GwKivyYtbj_8MzMvuF7GwhYHdfCvwPhovFDAElGNDZQoeFndj4M9nnzHIri6tdJ0y32vbwKnlfo41xAhyq-71ldI65BApCWseG7hzUZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=Bd_a_O0RITQWSmBfUzn3mx1aG1YG8aQgv5DXx_daMKmhxtj3f6E3mXRJZCzWfJ9sIbKGJ-vThgeQeMtMs6IlGeejEOihWAoXcExVr__N6SxaHy44rI48RcNMxvow4imFhGcje1y_1GeRBUesiczXLhL6fElUD-_BTO0HsZ3FjSRxjl-twCcpYM7w5V9oisQwGkT03LEnoY-SalJHXoUZ9BilCxbDe57hJqNqcxuuZrHBA3xjhC4GGJpejh1_vD8yVAMFDH_Si8gpYp7083pm5UuYo5D11Zg3w6zqTCb9vjFHHrPx2PoMKEQBGeEiYFjvGP9s-KrSgw1zyVYvF_I7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=Bd_a_O0RITQWSmBfUzn3mx1aG1YG8aQgv5DXx_daMKmhxtj3f6E3mXRJZCzWfJ9sIbKGJ-vThgeQeMtMs6IlGeejEOihWAoXcExVr__N6SxaHy44rI48RcNMxvow4imFhGcje1y_1GeRBUesiczXLhL6fElUD-_BTO0HsZ3FjSRxjl-twCcpYM7w5V9oisQwGkT03LEnoY-SalJHXoUZ9BilCxbDe57hJqNqcxuuZrHBA3xjhC4GGJpejh1_vD8yVAMFDH_Si8gpYp7083pm5UuYo5D11Zg3w6zqTCb9vjFHHrPx2PoMKEQBGeEiYFjvGP9s-KrSgw1zyVYvF_I7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9sJU6Ub0FHPjHJUcfude7K2Rc7kQvE9xTm6XvZ1q4X6QtzYqwYptXEk3gvS46lcPkRkgingRlezEeP7DZ8WtG-igHRsj7pr59JVOSITbDVsbz-PpkrvoRQ2CadXbPL3ZHs3r95klcmMXNn2dV5ygK8Blefe0Qb9wuS1uXoTaGxPfzCiQAKdOc4qAfL97QNgElQNOSVeaf4QmIJ9CwVbqn3BVnbPYo4q3z8Ri4Je-ObPie2ScVAy0Oqbkk_ImagUi47ht5cjQFRDc2TwnuHwMMofGyOInfcFAG8t7XzlGE7Vwscq1CCgbSgpAaJGGT4k7kkd0VCCPK1A4IGmtfJd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=nFP3_-sfzXXheHX22YYzVrfg1U0Oo183SYmOvluJQEIZwE9Oy4KEm4T8oU0bf4l82DTe4j1lU6pm9Go76TdDhIwEXF_uRjppFzaq0t3LxN4UyG7ujOB6MVlMKlns6Fj_Y1PG1ZbcyXGgO1efHNV-pwH1QA6UdVZHIKG1m7e9sLI1EQK3Aa8sm2nzqy1xkABM4Ulj8Lsnhl0KALGflHL-jBl1UeDC1mzJRDSGq_BQEP1nU25gS9naEfpNO528i0Y8SJ6-Pg-fbJhUBCDw9HtSkVglVlSdiHXi4lcRFDth6kVntpOP4bJD-fkPy6QSihQ1YBS6SErqruFPDSrTqw2STQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=nFP3_-sfzXXheHX22YYzVrfg1U0Oo183SYmOvluJQEIZwE9Oy4KEm4T8oU0bf4l82DTe4j1lU6pm9Go76TdDhIwEXF_uRjppFzaq0t3LxN4UyG7ujOB6MVlMKlns6Fj_Y1PG1ZbcyXGgO1efHNV-pwH1QA6UdVZHIKG1m7e9sLI1EQK3Aa8sm2nzqy1xkABM4Ulj8Lsnhl0KALGflHL-jBl1UeDC1mzJRDSGq_BQEP1nU25gS9naEfpNO528i0Y8SJ6-Pg-fbJhUBCDw9HtSkVglVlSdiHXi4lcRFDth6kVntpOP4bJD-fkPy6QSihQ1YBS6SErqruFPDSrTqw2STQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=YEFbNdGrfIbV8Q4WsjHMlsoRZFmRe21DA2XamAiU2_yMK20A8RjJ_67MaAriS_KMBz3nMuR0-cWI8PNC3Wfp6IyjaV-96HYH_TlNICea1oiZPwm6BovVBp8NV4DU0dIInIYR0t7Rey-rEJ8S3zj20wJfRRttWAanL689krwVj-MHkGNvd8GDY5LgRPUuJOTGGcw9QrI3NLbqwFpbq6Rsz4XKR279bCY0CozlfzJIWQGFarlRxs45eba2R3VsFe7r0CXpw4IiUVonwkELuuMEd31vX-a5OMWxuTraHBrOVuthDxnrTeoLupQ52Fi0SV7xtBc-STxWZBbypJmo7PqjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=YEFbNdGrfIbV8Q4WsjHMlsoRZFmRe21DA2XamAiU2_yMK20A8RjJ_67MaAriS_KMBz3nMuR0-cWI8PNC3Wfp6IyjaV-96HYH_TlNICea1oiZPwm6BovVBp8NV4DU0dIInIYR0t7Rey-rEJ8S3zj20wJfRRttWAanL689krwVj-MHkGNvd8GDY5LgRPUuJOTGGcw9QrI3NLbqwFpbq6Rsz4XKR279bCY0CozlfzJIWQGFarlRxs45eba2R3VsFe7r0CXpw4IiUVonwkELuuMEd31vX-a5OMWxuTraHBrOVuthDxnrTeoLupQ52Fi0SV7xtBc-STxWZBbypJmo7PqjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsDWr7nyqxGZy9Hk7tkMgZauSjQujxvuCzrU-X364SnomybsPMgNUduTng_1wauZP4OvtfOsJa4EV9xUl5Y1r1kR7V4-kst9LWeDazOIwHjQ6YNDlyes5DoWlTiEy2a2mYWn8iM6WsOs_w-CpNr9gv5DplJcK7KKvsHL9YCabo_uvHbszSz698y8u7HbDxtANCAu-7LsP7ctUAhPncc57YqSYAtUbvwe4ui2DlNKYpvXY24T23hKm5NeP_cRW3wWpXg6Q3yxNgRETjbeP8B9lB8GjNPQpuhoRarkqNamTPsxaAKJKK_ZFitWNxKasRA63z7BgUguG3vJ4mC59UZhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PElHgs5qi7BA-0lsjecRv5-eQqOgQHQ5JegGMqi4XBoKkVvvtpKxNRHdIC3LhFnN98ptHsuzTYJvacMW_TgA_S3vBXw-HIngLlrWUJBrrz3UsQSgRPVYjEXu8XoXuYuv0Xz-V0YL6EtYI0uOyun1K6og5sGEvZn2hIG_mlohfjU8F8DXmA_CRIDonEFE7Sg_BoIBLughpUIC6c4NNjBLhqqpkv5uRDnCGykT953hJIsQH_GNQyI9wZWTFM0qsO9LUvjNfGaidQSROeJ2UCU8gPjrZgFpyLHyfVq1to-t_iIAtdhvRTyCo-oQSUI0ck9zx2_4nELmbrEN1QqdQOHkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=ZPLFTjA1ccABf1rZw26vyWth8KYLM6QmKz-3Uu_lqQmrRZwLVxejPbL7eY1L2NpFx8N5HcjfoJI6iEQu5M1xnwRLu8TfvtUk0LeQ3NGVimD4vOpHnTpcpD3QfBL2d7khCldS1MFfRMqhn-3qQHkTbMbOHP-FVywtgpK8hd0NOViKqBKCtO6Uly0HEKqOuyfunwDkiUXnJ7SxoGIoL3P0_r5ZJpuGXiXp3U6qZSGS368H5p8guSomkwrJFh0xy2DUETgZo26TebyfP8g6Kv5VcWEiHsfwZLE66VrQHKZAfMCU76fbXQWrgB7CnmErsBkPjv-sueH7plPgfWW7hLwSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=ZPLFTjA1ccABf1rZw26vyWth8KYLM6QmKz-3Uu_lqQmrRZwLVxejPbL7eY1L2NpFx8N5HcjfoJI6iEQu5M1xnwRLu8TfvtUk0LeQ3NGVimD4vOpHnTpcpD3QfBL2d7khCldS1MFfRMqhn-3qQHkTbMbOHP-FVywtgpK8hd0NOViKqBKCtO6Uly0HEKqOuyfunwDkiUXnJ7SxoGIoL3P0_r5ZJpuGXiXp3U6qZSGS368H5p8guSomkwrJFh0xy2DUETgZo26TebyfP8g6Kv5VcWEiHsfwZLE66VrQHKZAfMCU76fbXQWrgB7CnmErsBkPjv-sueH7plPgfWW7hLwSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1J-TPse4V7TasbKY3G6HY_TxX_hU06EGCSiCL2mo7_9eQzl5zK9TyzpvnBVD9yaoLZW4q1U-mlL7rT-vwCLaNQRMb49nGpsMvUT6icJyjUMn7IwNcFbGkR3CsLDYQjj2GQ5xNx8ysPuQT6fybIL5LH1FJvVZFMkkN5Dr16szLnlJ8F43p7tVOixXxlyaBZk1OUSVNjORB4e75MWzFFnb50p4sQPtDFawe3GZ7bit4_sfeWG_huByeW0uSh4wA6u7YwVjiKAKWaKu98TcMOGGK8mIuL_rbNJieuWZaU1XBrJ6NUTOVQCQG2stODduTEZ8wxeIF9-8BZ5WK7mKHNIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_2pBPLtfvpcKx5ZgIpXCou4hG6uGDGzWvVHQoPCG-gBVdJOL6njxoHtosVqBpeOziYPXaxmalRg8_lkzsPeRfbPckhxvryV-aZMON3HmDAkVT8Oxvw-4qxz5SZzwE9Si9_MiGv3y4znAYVaFUJ0cjIVO37AG6J_nUNA_6I5IyXi5R5MYXBUQnFzRGRxEnaLc9eyVK4iIY2k_-F7tTP8VT0CKK5AayWjYCazCsyO4cAngcJ7lzHPC3QF3QEgWBspObH6Bk9uvYvSU_AtcUoc52jeFQpm7HaD3-qen1XjfV8Ox1OihfBDZKVUZtxcBRrnLgz6e6pRm-vEKrfrWO-KrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qto-zT-o7tuCnU0CCoBmGKOKuK3_5STJO2BjtLuLd9W4--TDMWr1kpQbQkjkqTv3GUknt-fVAkuuLr4kPZkYsxLoIJVEvbxeLUhJsm2_grX7Y6U8Gg45IBfv7xv3M3-rttAxB_Fida6KGntdDqPuL5LDS7T7QUvx0VswfKaJ-fJqHhyuKFE69igoC_Vi4VpMpxmHz3m1Lnv6ZC1sUu-opaxnQZu2QrYTZYqnwERrQqbFAf6T73ilj4EbWxI0W6XFQbzMlqqU_qdeFl3CWtcbGWSeeB8Ri8itg0AyR_9KdK6I_0wPj9MqxCGjB8fCg5dBCGM1SfTeKWzIJSSZSitWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=oz3XT6yP4q2w63ao71W24b94gFqN_QlpZ4Y1bQN75zbwgAOym9x0mOCGQEmH7Dw1ll4kfAYerYT0HUh9U3VHwm0LX4TELmn-_zK446ZF3hGseyssF1-dMZ18l55haQiTrxU8N-6l-VXTaP3n4GpFcss4SlqKdfkJcWJ8i6trcbVm5tMC-xNf4CCb6U0PbFEZ2sdgOQdtOfy2lJ3hbARMQyRwjNjJFzsnw0zXjSrx9shwqiGr7fFgkK8cxpG3z2RShgpWNL0ld6q2rP3oIUEU5u40yIi1pvJ5_5gmYd_Ka2jd4PHKL6SkKYTKK3ywLyuOmwcC4sB3DtVTsCWJA7VVt0bYgdSPMbDvZlcpKabXsdbBkTRa_aj7w9vLIYraYZQMJ8y4ShaEnYUJB9OhdzwAy9T1K8kznzqh5qqH0DkavlIf8AbGJ0L49Pl_idphYrzNHB2csgnui03A81B-Fv-5x6PUs79G4wGwL2wOJtYCxTE1WyO_IHOeDTh5hNRHg6i96ObLYvQ8C_s0U91RX_58bzW1ZfXxlCPr5gtjwgx6cirzhmC8p5y3yLMXY4359lHIOjhckHlOi_8lmVdcWaaVQqb-6vbQC63c1Q8K80-A2yT3VwU6dXcqXDEwMPVGRnpugRPx4KHdJ0pOTa7BK7AWgfrtG_fcvGolJlKEUXOwo3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=oz3XT6yP4q2w63ao71W24b94gFqN_QlpZ4Y1bQN75zbwgAOym9x0mOCGQEmH7Dw1ll4kfAYerYT0HUh9U3VHwm0LX4TELmn-_zK446ZF3hGseyssF1-dMZ18l55haQiTrxU8N-6l-VXTaP3n4GpFcss4SlqKdfkJcWJ8i6trcbVm5tMC-xNf4CCb6U0PbFEZ2sdgOQdtOfy2lJ3hbARMQyRwjNjJFzsnw0zXjSrx9shwqiGr7fFgkK8cxpG3z2RShgpWNL0ld6q2rP3oIUEU5u40yIi1pvJ5_5gmYd_Ka2jd4PHKL6SkKYTKK3ywLyuOmwcC4sB3DtVTsCWJA7VVt0bYgdSPMbDvZlcpKabXsdbBkTRa_aj7w9vLIYraYZQMJ8y4ShaEnYUJB9OhdzwAy9T1K8kznzqh5qqH0DkavlIf8AbGJ0L49Pl_idphYrzNHB2csgnui03A81B-Fv-5x6PUs79G4wGwL2wOJtYCxTE1WyO_IHOeDTh5hNRHg6i96ObLYvQ8C_s0U91RX_58bzW1ZfXxlCPr5gtjwgx6cirzhmC8p5y3yLMXY4359lHIOjhckHlOi_8lmVdcWaaVQqb-6vbQC63c1Q8K80-A2yT3VwU6dXcqXDEwMPVGRnpugRPx4KHdJ0pOTa7BK7AWgfrtG_fcvGolJlKEUXOwo3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlx_SbEFWD-yDhKAxugh6ZsT-d4nLgx0Hwmg0YNNJALTlPyAhzeIjFeYAD3BIH6YdyKtuFAZlIcwjk0OpPq_Lk3RxFqI3t6jNGBg0CelbA_NvJzTAjxx-QhzjX6_3SkCyuZBJ5lXBERlP4awiVle1OHKDlqCI2UZQ1sK6fAI0k0XVTnoihaxytcdZP5pPNGJmVbhaE0UMAvrVDMqZ_mEoMnyHYgaueDx5MXfDzI1kk1Zpb1Zzg5l2nvVWDA51PSS4Xip3Zfei3FS27ey8Sj_r9eNjM9ilXyCA2aDG_l30Z0VCgUj_QzIJo4EZZ8eDFxaizOcookVHD3_EbyoWK4UbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7gmfIsWcUx0jUOCTeiifKjeZ2ScYSRa6qRqqa9gj3YGwjj3_EBui6MfQH9Oq2ZAlbRVcXwh0raczx-o5TcqwBmrhO2BN6iuQCZd2jlChXaprWFrMKFlJnqcM6Q1G4q8kmxrV7VhbTCdA7g-5eRGhapv7mQqjLtNr_DV-BzoOYeGYSktPRjRRX5ZvOL4DZFnbsKxBu1AIbHvJaafC0BLWsqXf3uxNhON5Wy8XEuOc80C1eB1-8uVO-o8urR8dynw9MMam9W9k1m8ooqPvGYxuInT7Kan6WzAyL25wceUIdKqLs6l0_3XPjlqVLqJvafyXbx5OvMRD6kIGMWlHxB8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=kTh2MBTBDIVfkFSqWmC2MpZOpI7n7cuQX2L22hBIxLNGvNigapk6QroyNkVF2nEZLtMRuFfM4lSMadx6wdv9L8wVaxPHilLqfZYoe6qyM_YPytQjco2mFG3YyyUnw3crMh_owTLRYzO505maC1BkUwNvMBHxd_xwalRRvpm9Ejd5uV17zIhb1kjYkgZ71sg4oKwo07GynYtVYNIr_xpK4rVZu31yUIjqVWBnCnv4PVb6xJFbDcjOV7cHW2SVmweqK6nXRK_PM3FsAwgN1KnFdMwvnS1yKGy__VA2CF1wBRDOQg1RU0eQzV73jXun7OJYXD7TJLh31XticuEYUE9ZpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=kTh2MBTBDIVfkFSqWmC2MpZOpI7n7cuQX2L22hBIxLNGvNigapk6QroyNkVF2nEZLtMRuFfM4lSMadx6wdv9L8wVaxPHilLqfZYoe6qyM_YPytQjco2mFG3YyyUnw3crMh_owTLRYzO505maC1BkUwNvMBHxd_xwalRRvpm9Ejd5uV17zIhb1kjYkgZ71sg4oKwo07GynYtVYNIr_xpK4rVZu31yUIjqVWBnCnv4PVb6xJFbDcjOV7cHW2SVmweqK6nXRK_PM3FsAwgN1KnFdMwvnS1yKGy__VA2CF1wBRDOQg1RU0eQzV73jXun7OJYXD7TJLh31XticuEYUE9ZpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
