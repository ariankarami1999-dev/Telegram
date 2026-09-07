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
<img src="https://cdn4.telesco.pe/file/E6cKWQOx-yDAbk-v8gzhJlDanBJCqXifrCkbS27-ovHnwsD0DB_3GjzFkgbGGqAHTErkPoq6Ge-GpiReSDNavJJxu2HS5P64PMp-Y71jlRBWXawHpFzRtVnqYtiwNGEsoJ463ongW-X835ElEprmG2s7n7TT4XODT-ZHu5YONY4lrB_uBRNJOFNp1xzAf8WaBhDWHa3cbe2H1cd9W1JoQ_eRk1smpTsOZOi7SEPahnyFeu-i0gbYeuG09vLsiKQ6sCBiYakcuGEnZaYf8G-cpnbUFbhNpyhsreTwvzXbx1m51DshrhgmdJpJv4sGqMmBbZQufdwas8fEmmy7bHr0Gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-146066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2eb91028.mp4?token=K8ErV3j08SGaGCEBT-TZTEOPuGCLYzAgpP5jo3Gflcf_N_4DeGWclEeZ2g8UPJKX16f0Jw0SE0TFRPfTXuC-c1uqbJ1LWVRFNO0vKiZ11Caf6CTFRJDU2E1k1h1p_qIMXX_4pibu4huuLEROziyWINwmnPDIsC3gAdMduWDBt2bezgI-wfpTUFwwJXViRN2CCvRnXxAkinNmrCKKTtpnru6xDlanE2tbNeao_bhigd-w47Fv2Kjw3oTqRy5pBHvsghfU2OkexWgv4CNhne5QTVlOMYG2fJkKfTZe0eGAPQc5mlZjqC7JyGWN67uJQNCGmyiAW22YF08Lds2CnwV6an4WATktYt8PwVBO6Qf9CWZPBoPrreXCRxFM10r8TjNBnPCeNzGo5j41dFn8_gxt87ZJ4-N9jpKXXUvSdRqxZYZ7ydYX8b-KaJYfZEnAEYgtiZUVQOvMa6QCCd4GdADY7jVEYHzNfmkpZej3Xc93tBf4dRnQLVJ_Dwo2CrK6MH9CHbP2QicoN47dNTwCdbsSazgj6ujToOeXTXBFbM8W_x5Lq0hu-yrC4SNd4_nMEtbJDf7b5iyQLUMJke8DM6-S_ZyoejA6EZ_LAXKlLkHifdTJPXpAtbqpd3WbkbKQP16SlYWMS1qjb5WiPEr0StbdC9N8_T9l_dsNrAEy2Ok4Wuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2eb91028.mp4?token=K8ErV3j08SGaGCEBT-TZTEOPuGCLYzAgpP5jo3Gflcf_N_4DeGWclEeZ2g8UPJKX16f0Jw0SE0TFRPfTXuC-c1uqbJ1LWVRFNO0vKiZ11Caf6CTFRJDU2E1k1h1p_qIMXX_4pibu4huuLEROziyWINwmnPDIsC3gAdMduWDBt2bezgI-wfpTUFwwJXViRN2CCvRnXxAkinNmrCKKTtpnru6xDlanE2tbNeao_bhigd-w47Fv2Kjw3oTqRy5pBHvsghfU2OkexWgv4CNhne5QTVlOMYG2fJkKfTZe0eGAPQc5mlZjqC7JyGWN67uJQNCGmyiAW22YF08Lds2CnwV6an4WATktYt8PwVBO6Qf9CWZPBoPrreXCRxFM10r8TjNBnPCeNzGo5j41dFn8_gxt87ZJ4-N9jpKXXUvSdRqxZYZ7ydYX8b-KaJYfZEnAEYgtiZUVQOvMa6QCCd4GdADY7jVEYHzNfmkpZej3Xc93tBf4dRnQLVJ_Dwo2CrK6MH9CHbP2QicoN47dNTwCdbsSazgj6ujToOeXTXBFbM8W_x5Lq0hu-yrC4SNd4_nMEtbJDf7b5iyQLUMJke8DM6-S_ZyoejA6EZ_LAXKlLkHifdTJPXpAtbqpd3WbkbKQP16SlYWMS1qjb5WiPEr0StbdC9N8_T9l_dsNrAEy2Ok4Wuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش این گروه، گروه اسلامی "تحریک طالبان پاکستان" (TTP) یک حمله با استفاده از پهپاد علیه افسران اطلاعات نظامی پاکستان در شهر پیشاور انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/146066" target="_blank">📅 13:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jaxD82p84EFUUiBNB4m1MWj90KcE7sx_jbtVYcVXCyahFHkspkrmV5FE1EFGrE_TO11apNpe1vh-jrJyp8scuYO3qttOn0IjDe1NuApojVBy6P02VvRPLCnfZc3BEkYpsuX_7rLnpZkE7n9GuxJMYymdJvbosx9QgfC9ykaj5quKDsKaA24mRJfI3pUZt3WhUQ7HEYA2iYrVzEbcOT8sFRq2RedSz-a0vctTFLRvmtp02eDwhzCF_cz-5EntEaUzxBKJ8VtZhBR6GifHlpk-VcW459ANrOI8NCArV9Xyog0uaxPhoEiZTuZmuO6iIdoygo7Z-BxmmebTfvm_fCE5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال با استفاده از Ai
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/146065" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvT1R2SCEbQmAIzu7GsvTzORqpyGQcdPSe5xHjaRchrIXLmNoaFQIPUn5GY_rHq6aR_Di4JNubSPQ1wBelaMHO6MTtSvOCWckyaHVqSz00vQ8KWTbbyCRuLUm-FCISg0ypeiYqPym4e6aQqJXgFBQ-pXU2RSlk-UodgCjmMpPQjEW7ljon7P3ViHxSVZj9lzPzAElqkpowKc7oc22sSbHVSTtwMX32ZicMX4imRH7QNVxdVlC4oC8DGhb28GYiKQlhuTJJdX0aoWbb-uei3Kd9-cEBJceQh0PzcbNXKQyqpN6VYK4zTnyvNzeNWnIGjvLU7XHOy6hyOm853OQc1Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۴.۴ ریشتر در عمق ۸ کیلومتری، بوئین‌سفلی کردستان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/146064" target="_blank">📅 13:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx4_y3X72Q69QyxQqPY_aleiVsi6B-x1fix9YhkdsL8e-G2D9Kimwaz9fOCQRdMcCZaSwrbo7PQgM03ju7kgRo9UTnnfqe3ZVqBjV8BozLXBjebWAqQ_zZxaT4kgBi8BR9dxuXQm0QFl4JUH3TnmAapOuvlYaYHyVbg5j7G956YkUW_1e5909w0qiKoy67D44nA7H60W_mnaA9t8I1kA9n0-zg3AomZmlUlyFFSAXEkXKThRgsahQ-AsgV7OhvHhR174KQeBVKZEiEYZFBFWmV9KOAZb5h6JzBYfO-LKJkorUtbpozal_uJ_5_3DpSR-D2DwxKfzh629C2us53ameA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل مناطق نباتیه الفوقا در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/146063" target="_blank">📅 13:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146062">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b643721ea6.mp4?token=WgveawNLZfZm2pD0QkD0npM1_r1zv2NnJnkja9fKZVK2OZM-0dLLvU2Isq83GaG47B6hqpWpK7sbBxAe3hR8fS3RcfROMY9yKe7LW_ARbkO16x72l6gqB8I42LJsVCCveIgVSIZnFY-V255XfeJIDM6yiYMoG8974KCo1Q18zAUe3oOZI-qkbyX6fyXERaPbhFO8PRngFPURme440RTcrQ9AHZNW-FnCWX89CjD_CuOodGuhKSobyDViPbijKY37AiON8evciCKidg-A6nCxq-oduk20ERoww_MUYjav3XGqxy_uBJJ0OqgZKTCz7JhzBJd83uGrVqi9UEVCK90DXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b643721ea6.mp4?token=WgveawNLZfZm2pD0QkD0npM1_r1zv2NnJnkja9fKZVK2OZM-0dLLvU2Isq83GaG47B6hqpWpK7sbBxAe3hR8fS3RcfROMY9yKe7LW_ARbkO16x72l6gqB8I42LJsVCCveIgVSIZnFY-V255XfeJIDM6yiYMoG8974KCo1Q18zAUe3oOZI-qkbyX6fyXERaPbhFO8PRngFPURme440RTcrQ9AHZNW-FnCWX89CjD_CuOodGuhKSobyDViPbijKY37AiON8evciCKidg-A6nCxq-oduk20ERoww_MUYjav3XGqxy_uBJJ0OqgZKTCz7JhzBJd83uGrVqi9UEVCK90DXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویروس کرونا همانند دوران اوج ، از سطح هشدار، عبور نکرده است
🔴
معاون بهداشت وزارت بهداشت:
برای پیشگیری از ابتلا به کرونا و آنفلوآنزلا، همچنان رعایتِ نکاتِ بهداشتی در اولویت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/146062" target="_blank">📅 13:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146061">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fec8ba7a.mp4?token=AvNGr8LOOrTgZL5gsm4fBcKr0l_ajMJUyk1uh-dtDFljKE8Y17_GMk7WGVj3M4I57sVZfSm9GGvBNQP4Zn0ftdvu7l-V1Lesrk3An8hQSPkF_eQaRkoAZsLnyZ6YB2LLTPiJdOW-565sLOcRZPbftyEmdn7VEZLAfYSWj-eUgzfidJ7PeG72TzNPMUFkwHxt3pcvqmEy4AeWYwwOqcsHiodaOQJN6kH91qnhVTJplzC522la8q8nzyVtSmot0xsWfjfi2A4onaNW0S7CUxCW_ALoATRQG1znX98NJBuJj85_77QZjdcPSbV-h_wNPll9JfFzcEfkv1CvXa7b4DWQEINxkYLIBd7vRjeKOONEYUSaHHOyZlzealpKoJ0yjRBfx7GcsdbCyPtVUi410bMjzf6FjZ9Yo4HbwuHuAsRBxsC81tndQjBCzoDP3RZpqaR90BFDTkY-gxjLfu7NgQ1n7TihUlHCJbqfh_Yo1MHC6JpDg84AN62voaG693ROK4G7p9oABEZjYZw3dJVIDD6VPK-2TqPWd428i2MoPTfJQ1YYwibmxd34Gmp0OEBP9IGonmMEyCysbhBTQIfGuDdrfvh5vq_S2tOc5KBeZx33AWIUvsPJym64MM35CsF4olvLMEOLP3_SYEIhr2koMwDxcZTTAfrh3EbDxuE1gSG7IY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fec8ba7a.mp4?token=AvNGr8LOOrTgZL5gsm4fBcKr0l_ajMJUyk1uh-dtDFljKE8Y17_GMk7WGVj3M4I57sVZfSm9GGvBNQP4Zn0ftdvu7l-V1Lesrk3An8hQSPkF_eQaRkoAZsLnyZ6YB2LLTPiJdOW-565sLOcRZPbftyEmdn7VEZLAfYSWj-eUgzfidJ7PeG72TzNPMUFkwHxt3pcvqmEy4AeWYwwOqcsHiodaOQJN6kH91qnhVTJplzC522la8q8nzyVtSmot0xsWfjfi2A4onaNW0S7CUxCW_ALoATRQG1znX98NJBuJj85_77QZjdcPSbV-h_wNPll9JfFzcEfkv1CvXa7b4DWQEINxkYLIBd7vRjeKOONEYUSaHHOyZlzealpKoJ0yjRBfx7GcsdbCyPtVUi410bMjzf6FjZ9Yo4HbwuHuAsRBxsC81tndQjBCzoDP3RZpqaR90BFDTkY-gxjLfu7NgQ1n7TihUlHCJbqfh_Yo1MHC6JpDg84AN62voaG693ROK4G7p9oABEZjYZw3dJVIDD6VPK-2TqPWd428i2MoPTfJQ1YYwibmxd34Gmp0OEBP9IGonmMEyCysbhBTQIfGuDdrfvh5vq_S2tOc5KBeZx33AWIUvsPJym64MM35CsF4olvLMEOLP3_SYEIhr2koMwDxcZTTAfrh3EbDxuE1gSG7IY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری دسته‌جمعی با بیل و چماق در سعادت‌آباد؛ ۱۱ نفر به دام پلیس افتادند
🔴
درگیری دسته‌جمعی میان چند نفر در محله سعادت‌آباد تهران که با استفاده از بیل و چماق به نزاع و ضرب‌وجرح کشیده شده بود، با ورود به‌موقع مأموران کلانتری ۱۳۴ شهرک قدس پایان یافت و ۱۱ نفر از عوامل این درگیری دستگیر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/146061" target="_blank">📅 13:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146060">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
لغو خروج صیادان بازداشت شده هرمزگانی از امارات
🔴
مسئول نمایندگی وزارت خارجه در هرمزگان: بلیط بازگشت صیادان دستگیر شده در امارات به بندرعباس صادر شده بود و همه هماهنگی‌ها لازم بین مسئولان ایرانی و اماراتی برای بازگشت آنان صورت گرفته بود.
🔴
در آخرین لحظه، طرف اماراتی بدون ارائه دلیل موجه، از خروج این شهروندان هرمزگانی جلوگیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/146060" target="_blank">📅 13:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146059">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خسروپناه، دبیر شورای انقلاب فرهنگی: امروز همه نهادهای ما باید پهپاد بسازند؛ پهپادی که اف‌۳۵ را بزند، چون فضای هوایی را مورد تهدید قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146059" target="_blank">📅 13:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7d7ebd36.mp4?token=A7RXFUcQBJf0s3tMdHU-qVMRe0a2vo_ukQJVdd_YfXmm9j4Vrkrik2eVCfcn5RekHPFGQokbmkv1tcAee2-hzQny52DeIOzsbSkaofRo8yayTB_5KkE94aPdR7k-WKcHMC0Ep3q5XpnTYtdc9gLOvHkjjx0d_RXYa-kHkrcikuA2cS6ULpcLi_Sncjrkz0a12ecARWOzempIHpjcXVANQdwqia3IMDQFZ83-vuwfc1l78HRL4lM0rOxHlbPxdp1lqJDnnfsXSbAq13M6VOhieAQKJNrZiyF1rFDXvC3E-SLkVnaAw7UbktDtWmf_oz6fGjwzDIr3fGs_yuMZZGirVpoNS3HSLW4lXdnB52fg4yWf4A2DJPOhM0jRuY5EyZ7wWUUYwpJDuIxvg9DQs8pU73bFwPLsgaUK8FmRJVsLiG7BxbEiC-eXFxOXDkb1aTm0dwzrNqSZ5zdZEc6AVovxCmYVGz5FcreHFPfFdoU1DR1PD7_cayVe8gqsKr55ao7CyXkpBqCCFVMRKE05MB3Ns2bbA82ueTe-Og6On7jKUBVstrsZb8Gpy03CdiVee40m-ZErU2ZTXYlyAyB9KzpnvlHHqZ_-bCVc4oAIQ0LRLcBlQfhOg9Bs5dcyNKDLjOrfCZMytn2-UKtSuQwuEcnEusb9nT6UMNHYHsezxqTUSG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7d7ebd36.mp4?token=A7RXFUcQBJf0s3tMdHU-qVMRe0a2vo_ukQJVdd_YfXmm9j4Vrkrik2eVCfcn5RekHPFGQokbmkv1tcAee2-hzQny52DeIOzsbSkaofRo8yayTB_5KkE94aPdR7k-WKcHMC0Ep3q5XpnTYtdc9gLOvHkjjx0d_RXYa-kHkrcikuA2cS6ULpcLi_Sncjrkz0a12ecARWOzempIHpjcXVANQdwqia3IMDQFZ83-vuwfc1l78HRL4lM0rOxHlbPxdp1lqJDnnfsXSbAq13M6VOhieAQKJNrZiyF1rFDXvC3E-SLkVnaAw7UbktDtWmf_oz6fGjwzDIr3fGs_yuMZZGirVpoNS3HSLW4lXdnB52fg4yWf4A2DJPOhM0jRuY5EyZ7wWUUYwpJDuIxvg9DQs8pU73bFwPLsgaUK8FmRJVsLiG7BxbEiC-eXFxOXDkb1aTm0dwzrNqSZ5zdZEc6AVovxCmYVGz5FcreHFPfFdoU1DR1PD7_cayVe8gqsKr55ao7CyXkpBqCCFVMRKE05MB3Ns2bbA82ueTe-Og6On7jKUBVstrsZb8Gpy03CdiVee40m-ZErU2ZTXYlyAyB9KzpnvlHHqZ_-bCVc4oAIQ0LRLcBlQfhOg9Bs5dcyNKDLjOrfCZMytn2-UKtSuQwuEcnEusb9nT6UMNHYHsezxqTUSG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: مردم حق دارند به شبکه با کیفیت و اینترنت پایدار دسترسی داشته باشند
🔴
از این حق اصولی و شهروندی مردم کوتاه نخواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/146058" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146057">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
گزارش‌ها از لاذقیه سوریه حاکی از وقوع تیراندازی در داخل دادگاه جنایی این شهر است که بر اثر آن یک نفر کشته و یک مأمور پلیس مجروح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/146057" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146056">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از امروز در وین آغاز می‌شود؛ نشستی که می‌تواند آغازگر مرحله‌ای جدید در پرونده هسته‌ای ایران باشد.
🔴
آمریکا و سه کشور اروپایی در تلاش‌اند قطعنامه‌ای را به تصویب برسانند که زمینه ارجاع دوباره پرونده هسته‌ای ایران به شورای امنیت سازمان ملل را فراهم کند؛ اقدامی که در صورت تحقق، نخستین ارجاع پرونده ایران به شورای امنیت طی حدود ۲۰ سال گذشته خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146056" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146055">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ایران: مشارکت کره جنوبی در عملیات نظامی در تنگه هرمز پیامدهای وخیمی خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146055" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146054">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: پیگیری پرونده ۳ خلبان ایرانی با اعزام هیئت فنی به قطر ادامه می‌یابد
🔴
سفارت ایران آزادی شهروندان بازداشت‌شده در کویت را دنبال می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/146054" target="_blank">📅 12:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146053">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">اگه تحمل بی حجابی رو ندارید وانمود کنید که ندیدینش، همون کاری که با گرونی و فقر میکنید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/146053" target="_blank">📅 12:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146052">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
تو این وضعیت اقتصادی یه چیزی رو برادرانه بهتون بگم:
رفیق گلم تو کشوری هستیم که بدون درآمد دلاری نمیتونی امور زندگیت رو بگذرونی.
🔵
با حقوق کارگری چند سال کار باید بکنی تا یه پراید 500 میلیونی بخری یا یه خونه 5 میلیاردی؟ تا کی میخوای شرمنده زن و بچت و آرزو و هدفت هات بشی؟ میخوای زندگیت تغییر بدی ماهی 500 میلیون در بیاری تو این کانال عضو شو ، نیاز نیست هزینه ای بپردازی
💰
:
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146052" target="_blank">📅 12:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146051">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEXGwcdL_Rhja0IDSxzGXlb_lDjkQBwyDcnSluRFCTJaH6JA6vupLOfqoqqIIlF69PcwONpZFY-6nPUsej4ZFWIRMdTcY2Tcn1kRauahGAv9W5vcKPEwFP4oW6C4RvmmUTL3_UDOz50NCscpE_QZ9mRYA5GkTyXCQehc_JbcO3ar5QepL2YX3pt4dmMfiU9lIEE-nBkZzG7bR4IolHk5L8X0yP-zUL7EJWyJO16_1WFVUvG6CjzHnsw-UJcqqQmPpjTgGbY85_S9PnFzrrZ_2HFQIpYOgG_2y22wO8va173iIW0pJ9mWDWEUc64eCdUxJhJs8ZLqTE0EWoZQCZdkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسروپناه، دبیر شورای انقلاب فرهنگی:
امروز همه نهادهای ما باید پهپاد بسازند؛ پهپادی که اف‌۳۵ را بزند، چون فضای هوایی را مورد تهدید قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/146051" target="_blank">📅 12:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146050">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که یک پهپاد شناسایی-حمله‌ای مدل "وینگ لونگ ۲" متعلق به نیروی هوایی سلطنتی عربستان سعودی را صبح امروز، در حالی که در حال انجام "عملیات خصمانه" بر فراز استان البیضا بود، سرنگون کردند.
🔴
این سومین پهپادی است که در ۲۴ ساعت گذشته توسط حوثی‌ها ساقط شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146050" target="_blank">📅 12:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146049">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=b_an5Qj9qXX4htgZSkSg6JZHo_4qPvLeMipp1dZTAuNogCqs4Dl-kfvnas7UQ3wUgzxzbEIi_vu2Y8M_uGOpHxqxHqFrc_SUshjTQL-Qa1WQLUxfEIp9N0Gxlbz-ssqLu4rO-OkukEV3teGeW0Ht3pdQtzYbC9YbToJ93yePx0bOJ9PMtf7kvgg3fJZlOEtV8q5yVKzsIbQgHFD_lQKC6MfALgpymk9g70NqE8v7u7LsWRHlDVpBPBsB7DUYC2gGo6jxX4BF2MbQurnL4YMvJbviGpI_4NfwTrqTDCosd8sxBPK5dGQRxaMYHmKEJPEQQMy7JKxK0_ehbJBw57p2fUWZcfBX0QHAgCsbIVDksSu4mUiZwyKv1b3reawLvOI-FmrU8tk0u8Engla5quAlIYyjiQBLPqMKOdp3FeCIw1CTLNJyjbxfjp6VreNWGRK5Jvv_6kXyhKvY0VCNMPoCcRy6NAxzrniVQZ2AaLlsdO8edKIIz4wjfJ11SQRhftB6bVZcViet1TwUsP--vPmXJRwChM_Pmkoouu_chabXi-zq-VFfHBZDCL6NPlWQBEfy_XJKS3cAOkmt5vvkGFPw4MxgxdgivFbIEvTCqtlBvskuzxAiPF2anVzJp81jt1Ifw5oUZvVCivslG_53hQMp_LEttjypbRIEpWHk2uYqnpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=b_an5Qj9qXX4htgZSkSg6JZHo_4qPvLeMipp1dZTAuNogCqs4Dl-kfvnas7UQ3wUgzxzbEIi_vu2Y8M_uGOpHxqxHqFrc_SUshjTQL-Qa1WQLUxfEIp9N0Gxlbz-ssqLu4rO-OkukEV3teGeW0Ht3pdQtzYbC9YbToJ93yePx0bOJ9PMtf7kvgg3fJZlOEtV8q5yVKzsIbQgHFD_lQKC6MfALgpymk9g70NqE8v7u7LsWRHlDVpBPBsB7DUYC2gGo6jxX4BF2MbQurnL4YMvJbviGpI_4NfwTrqTDCosd8sxBPK5dGQRxaMYHmKEJPEQQMy7JKxK0_ehbJBw57p2fUWZcfBX0QHAgCsbIVDksSu4mUiZwyKv1b3reawLvOI-FmrU8tk0u8Engla5quAlIYyjiQBLPqMKOdp3FeCIw1CTLNJyjbxfjp6VreNWGRK5Jvv_6kXyhKvY0VCNMPoCcRy6NAxzrniVQZ2AaLlsdO8edKIIz4wjfJ11SQRhftB6bVZcViet1TwUsP--vPmXJRwChM_Pmkoouu_chabXi-zq-VFfHBZDCL6NPlWQBEfy_XJKS3cAOkmt5vvkGFPw4MxgxdgivFbIEvTCqtlBvskuzxAiPF2anVzJp81jt1Ifw5oUZvVCivslG_53hQMp_LEttjypbRIEpWHk2uYqnpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146049" target="_blank">📅 12:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در صورت صدور به‌موقع روادید، رئیس‌جمهور در مجمع عمومی سازمان ملل شرکت می‌کند
🔴
نمایندگی نیویورک تا اعزام سفیر جدید توسط معاون نمایندگی مدیریت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146048" target="_blank">📅 12:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37f1a3a50.mp4?token=FDtmEPACsgx0hs2CJuyfw372WNP2lQgTmgRlNOLdxAKrAIBKFm3aT-wZMbc69rXXZRlB5kI3l4j2XBMGVyfkbENJ1msmX1P5Wa6QkxveqGt9vgDd-HL1hzl7z1C2Zjp6jkzrzoUVFRfl-rB_Rvu6f2xpbVyR1P2s7TEdI1lTAl1PDd9_LxMKHd1-FyeB2kdmQIUhB4AZsygZCIZqTlHBNWH7Xza_w4ZUmenJ8GJeaOynMLnSjJq0YrkleD3BPHB_3sTts58psaYJkN06Hgn5O6bfz1DoOHeB5CZzBepvcSJymeZpuD4nQBieKifGuwqZOSnJvgsrj3GU6AatEfTaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37f1a3a50.mp4?token=FDtmEPACsgx0hs2CJuyfw372WNP2lQgTmgRlNOLdxAKrAIBKFm3aT-wZMbc69rXXZRlB5kI3l4j2XBMGVyfkbENJ1msmX1P5Wa6QkxveqGt9vgDd-HL1hzl7z1C2Zjp6jkzrzoUVFRfl-rB_Rvu6f2xpbVyR1P2s7TEdI1lTAl1PDd9_LxMKHd1-FyeB2kdmQIUhB4AZsygZCIZqTlHBNWH7Xza_w4ZUmenJ8GJeaOynMLnSjJq0YrkleD3BPHB_3sTts58psaYJkN06Hgn5O6bfz1DoOHeB5CZzBepvcSJymeZpuD4nQBieKifGuwqZOSnJvgsrj3GU6AatEfTaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: رای منفی آمریکا به تغییر اندازه نقشه جهان شاید به علت کوچک تر شدن گرینلند بود
🔴
علت عدم حضور ایران در جلسه قطعنامه اسامی جعلی روی نقشه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146047" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/70ee904e74.mp4?token=RKx5avryYHPOYbh3Chv0sPAgHdTYbtjmKJ7HAQm8sbIVBS5KWHE5zSZGKOEAPwY2WsqTpdqmSek4NBmmqrj7HyPB3c4QkbtD_4-MmFtBkr3-aQxjgYfLgLR4DcXvmus6s5JcApPQu2foSKfee_-nD5frmn35HrWqBn92Uy-QDD_IZLvRrMp4hrWRa9FUZY9AMjdap-k6448HnMBo7VkxGi8_YEKuax1dy0fwsqsgRUU2aCtnH8SrpOQRNxb7E4VjLdiKQ2jJHn8bkZmNRw_jEQ7V-hqkCo4kaLLGJqoE9UMzMLTExp2MwDefWuVfsWsSejyQ83BdQAsSVT6XPeT8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/70ee904e74.mp4?token=RKx5avryYHPOYbh3Chv0sPAgHdTYbtjmKJ7HAQm8sbIVBS5KWHE5zSZGKOEAPwY2WsqTpdqmSek4NBmmqrj7HyPB3c4QkbtD_4-MmFtBkr3-aQxjgYfLgLR4DcXvmus6s5JcApPQu2foSKfee_-nD5frmn35HrWqBn92Uy-QDD_IZLvRrMp4hrWRa9FUZY9AMjdap-k6448HnMBo7VkxGi8_YEKuax1dy0fwsqsgRUU2aCtnH8SrpOQRNxb7E4VjLdiKQ2jJHn8bkZmNRw_jEQ7V-hqkCo4kaLLGJqoE9UMzMLTExp2MwDefWuVfsWsSejyQ83BdQAsSVT6XPeT8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش بقایی به قطع ارتباط پرو با ایران: خالی فروشی کردند!
🔴
قبل از این هم ارتباط دیپلماتیک با پرو نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146046" target="_blank">📅 12:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bb5afd21.mp4?token=f1ifnfeeWNBAecmXmyOUZP4pG_sgkB_0Y4_TWn86h46hEKzwqEem9hnxItD1jIyyliUvZ4XWi9m2UZy2nhmJ4wEChnrY__No6vDzVTCznrSw2eTb54TrJUGv1sSFlw0gKnGKT_L4aa6nAOIF53IUFLZoG3PAVaez5iPjI1RoOZ7ESwbwPRRE7I91iZH32nZDYqgv9HZwtJ5ycrsXL9bhofx1cSMwkyOrcyjMSLi3gPS0J_E50h9tcBlrLJBET8ihuFn3MgXxpsw47FF6GXeiVEIJ1yUIWKAZAqSDI2Jc1tEEUBePPCXne10PcLCEqeFYjawbnjwq-TcJIQt--0Rp7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bb5afd21.mp4?token=f1ifnfeeWNBAecmXmyOUZP4pG_sgkB_0Y4_TWn86h46hEKzwqEem9hnxItD1jIyyliUvZ4XWi9m2UZy2nhmJ4wEChnrY__No6vDzVTCznrSw2eTb54TrJUGv1sSFlw0gKnGKT_L4aa6nAOIF53IUFLZoG3PAVaez5iPjI1RoOZ7ESwbwPRRE7I91iZH32nZDYqgv9HZwtJ5ycrsXL9bhofx1cSMwkyOrcyjMSLi3gPS0J_E50h9tcBlrLJBET8ihuFn3MgXxpsw47FF6GXeiVEIJ1yUIWKAZAqSDI2Jc1tEEUBePPCXne10PcLCEqeFYjawbnjwq-TcJIQt--0Rp7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هیئت قطری دیروز در تهران حضور داشت و برای کمک به کاهش تنش‌ها دیدارهای خوبی با آقای عراقچی داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146045" target="_blank">📅 12:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYgeJnVP1Zmov-QL3iI9gQWkjpMoe-6VfIt8_FMDBo7HckOs38ZkQ44iCqiKgSbj4x0zTRGfXEHo_yOzZjhA9qo5NSzQFce85fjBw9BNOo0tn0ULBCtz82pG7-M03DQoRtHmtD8YvznCVhoPaCjC3HbMFlDNwdk6-uOH-aG4ZJNhwfqy7S1Td7Pw0FU7bx0c2i5FW55wgs4bCotm5aIjrXO4EVXg3pcaIzXIZms7ClXOpHSkU1phMzUn0vVOaX9Ew15BSaKAi2OSqPzdtTQvG_KidGbTORIYvfoBAHh4jeXfarNE5mxTWRzKdqXD0QxS-utnngiKvqZcwk4-Futobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف در پاسخ به تهدیدات اخیر پیت هگست وزیر جنگ آمریکا از استراتژی نظامی جدید ایران گفت:
🔴
ساده و قابل‌ فهم است: زنجیرهٔ تولید نفت و گاز در این منطقه گسترده و پراکنده، در دسترس، و آسیب‌پذیر است. شرکت‌های نفتی و گازی آمریکایی که در این آب‌ها و تأسیسات فعالیت می‌کنند نیز همینقدر آسیب‌پذیر هستند.
🔴
اگر به دارایی‌های ما حمله کنید، مورد حمله قرار خواهید گرفت. ما این توانایی را قبلاً ثابت کرده‌ایم. از پایگاه‌های نظامی‌تان که غیرعملیاتی شده‌اند، بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146044" target="_blank">📅 11:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/146043" target="_blank">📅 11:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس: نفتکش تحت حمایت آمریکا هم برگشت خورد
🔴
نفتکش TITAN HARMONY صبح امروز هنگام نزدیک‌شدن به کریدور جنوبی تنگهٔ هرمز مسیر خود را تغییر داد و به‌سمت جنوب بازگشت.
🔴
این تغییر مسیر درحالی رخ داده که قبل از آن نیروی دریایی آمریکا درحال پشتیبانی از عبور این نفتکش در مسیر جنوبی تنگهٔ هرمز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146042" target="_blank">📅 11:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بقایی: فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند/ حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146041" target="_blank">📅 11:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: جنگ اقتصادی آمریکا علیه کل جامعه جهانی و تجارت آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146040" target="_blank">📅 11:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر شلیک توپخانه در منطقه قنطره، جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146039" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b44caa0c7.mp4?token=LGff02AZOQsK48_jvOMIH7Bi9-4Gn0fJ7jX2qCga2YnV9GIzcLbFP2ZXNWu1Tm8fbkFcfWO3Qb50Hps9bdQjdyunpcJ5rLfEplFnC4TusW1Ig_Boq3EhwfE-jc3dGz5oiDp5NhEb8LZDY9Ps3JtUWIMD0z-BjPszbVptlxvdYchNjclr9pGMLWlaKsBDF5ELwkSBAgQASaES4q_cLBmCBtGEKOQCHsApJCOwelT0nnegKOUWebj1UcDVHwX4754ej0WKFch2nzdDTZdWhwh23f8AR2-VsaRYZhXIZ6OcrJJAeTL2zPm0d_z5e1fkcl2EJ3Q1ZF0b3OO689r6VaDkPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b44caa0c7.mp4?token=LGff02AZOQsK48_jvOMIH7Bi9-4Gn0fJ7jX2qCga2YnV9GIzcLbFP2ZXNWu1Tm8fbkFcfWO3Qb50Hps9bdQjdyunpcJ5rLfEplFnC4TusW1Ig_Boq3EhwfE-jc3dGz5oiDp5NhEb8LZDY9Ps3JtUWIMD0z-BjPszbVptlxvdYchNjclr9pGMLWlaKsBDF5ELwkSBAgQASaES4q_cLBmCBtGEKOQCHsApJCOwelT0nnegKOUWebj1UcDVHwX4754ej0WKFch2nzdDTZdWhwh23f8AR2-VsaRYZhXIZ6OcrJJAeTL2zPm0d_z5e1fkcl2EJ3Q1ZF0b3OO689r6VaDkPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئو وایرال‌ شده از بازی دختران محجبه در بازی مافیای نفوذی
🔴
در این بازی ترامپ، نتانیاهو و رضا پهلوی نقش مافیا را دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/146038" target="_blank">📅 11:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فحاشی عجیب و بی‌سابقه علیه حسن روحانی در تجمع شبانه
🔴
اگر به خیابان بیاید دندانهایش خرد خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146037" target="_blank">📅 11:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مدیرعامل شرکت فرودگاه‌ها: ۲۷ فرودگاه در جنگ آسیب دیدند که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/146036" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHo4sLHuJZ67jrq4Vi84qty7xIevwxcdUdwkKZPgYze4zLOD8ZMcv4UC5RzZDsfOxJXPmW-M1sUrO6NPhXJSA7PHGJ4BEBOFZ2P12IkFRfE8jUE1uB5rH-t6DwwBr7TJkNpMGh7s3spe3E4uS0BfRwm96HmKD2uYFzmDcoxUNQssSAOj2hVKKibPV-_hxt8QkNKf431daL-KB_NqEzoomlN55goGrJg27DUcyuUe-3LQWxOCp5xOUWizuG2Qr0yNHOCWcYpaqQ-z1m4e0bWLpbXgbc-tVsatSyPQevveaItKoizPn1f8Cpw_LAUA7UdD8fW0v2SpHE4g8e6zvA7BxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به ۹۸ دلار در هر بشکه رسید
🔴
وال‌استریت ژورنال: افزایش قیمت نفت در پی تشدید درگیری‌ها میان آمریکا و ایران و بالا گرفتن نگرانی‌ها از قطع خطوط عرضه نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/146035" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز به نقل از سخنگوی وزارت خارجه قطر: «ما در منطقه خلیج فارس باید درک کنیم که ائتلاف راهبردی با آمریکا امر خوبی است، اما کافی نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146034" target="_blank">📅 10:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینه آن را بپردازد و هم‌زمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است
🔴
این وارونه‌نمایی، به‌ غایت بی‌معنا و بی‌اساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/146033" target="_blank">📅 10:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بهای معاملات آتی نفت خام برنت تا ساعت ۰۵:۱۲ به وقت گرینویچ با ۷۹ سنت، معادل ۰.۸۲ درصد افزایش به ۹۷.۰۷ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/146032" target="_blank">📅 10:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146031">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huTPiBnlP2kjwqMC2LhmfFkieA4DI9O-8mtzDfMqAMJykRa91CdM0nEnKGd3yyMaRpbWp6RGJe5XK8NJBWZlFxlctXQhdI8lR_ME2IdztQxGVM_pXBucHEvLY2CXDOu4xlMBkP5BBG9mWky3tF40ci94Eg-PXFfZEdi7O41EElO0_ZMMJ-twzV1-63CIsieUO_oQmXUMSz-qho2nvY3yg55BBU75ugrtt3QnQVjruS2GHaH6by_tfQCQ6GbFEhcwHHhQQJB-MbDt90fLBWCB-toqKUBxtbJg5NLb6zB9h7aiunH22X1gNMuhPBTNALDulaIvL07q0sAbnKNsqd4s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کاروان کوچک از کشتی‌ها در حال حاضر در تلاش برای عبور از تنگه هرمز از سمت عمان است، و این کاروان تحت حفاظت نیروهای آمریکایی قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/146031" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
به گزارش الجزیره، حملات هوایی اسرائیل به شهر کفر رمان در جنوب لبنان که شب گذشته انجام شد، جان حداقل 10 نفر را گرفت.
🔴
در این حملات، 9 نفر در اثر اصابت به یک ساختمان کشته شدند، در حالی که قربانی دهم نیز در یک حمله جداگانه که هدف آن یک موتورسیکلت بود، جان خود را از دست داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/146030" target="_blank">📅 09:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87849029ee.mp4?token=ReRDfh6pfE1OTO1RTl7z3UugLcKefMhZW-6nL1VgYVKgPMiDLiYo8cNib6P2IdkS2GhnLpI2FhdWdUBxLLtG6ILzZ5W4Wcl529uUnRGE7hRhs4bEkdpIdmA9LyqLXQR13izMUU2DbKYM8306OuWPPwKXAK9OUnyN1rJRcHOk69m9yNwn3M3RyQxORbY0FmsXvx1MY4a2GPL0IDjR2tqxpFzS6b_vpx-pJvTob25RHHGDHzWA63OoMNj8hdSBhzzfAQDsF_S8RlGaZYOoQkILJW4WjdJ0-YuGs846GtFVzetecLmtRZv-iic05eiRNAEn4JZAwwb0NXT8RlS-ZKDMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87849029ee.mp4?token=ReRDfh6pfE1OTO1RTl7z3UugLcKefMhZW-6nL1VgYVKgPMiDLiYo8cNib6P2IdkS2GhnLpI2FhdWdUBxLLtG6ILzZ5W4Wcl529uUnRGE7hRhs4bEkdpIdmA9LyqLXQR13izMUU2DbKYM8306OuWPPwKXAK9OUnyN1rJRcHOk69m9yNwn3M3RyQxORbY0FmsXvx1MY4a2GPL0IDjR2tqxpFzS6b_vpx-pJvTob25RHHGDHzWA63OoMNj8hdSBhzzfAQDsF_S8RlGaZYOoQkILJW4WjdJ0-YuGs846GtFVzetecLmtRZv-iic05eiRNAEn4JZAwwb0NXT8RlS-ZKDMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشته در انفجار مرگبار مواد آتش‌بازی در مکزیک
🔴
انفجار مواد آتش‌بازی در جریان یک جشن محلی در مرکز مکزیک دست‌کم ۱۰ کشته و ۶۰ زخمی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/146029" target="_blank">📅 09:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f89acc91b.mp4?token=nturszN6xB7Lnpm9TWg49EuVuMegA_fxzDhPPDguwacY4xfg73R_yVeZmkDjgIdTmG1w_DcqcU3wrhomOSj0njqufNB0ICgYdXParOlYRWz4QDvGPy5LHVWI9-So8uUzLRIf-s7RoN3TAtutpGC8TtYkz_Z8dxsyf84cjXEBXsNJTgMK46366wsZ44ao80yVLsSuTfl0QmQmjrddxC3jJuj80GEV4eVXWKYPfJ8talrJmGFt09baAbMrp5tkOKnzrRkK2TObOfF1ljaBvIZ1_psVfe0-5oEUyHUUIt9H6O5Y_qxfvQz62w4jWIVqtuKPZ6L76hiojT3BwEiPb6MazQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f89acc91b.mp4?token=nturszN6xB7Lnpm9TWg49EuVuMegA_fxzDhPPDguwacY4xfg73R_yVeZmkDjgIdTmG1w_DcqcU3wrhomOSj0njqufNB0ICgYdXParOlYRWz4QDvGPy5LHVWI9-So8uUzLRIf-s7RoN3TAtutpGC8TtYkz_Z8dxsyf84cjXEBXsNJTgMK46366wsZ44ao80yVLsSuTfl0QmQmjrddxC3jJuj80GEV4eVXWKYPfJ8talrJmGFt09baAbMrp5tkOKnzrRkK2TObOfF1ljaBvIZ1_psVfe0-5oEUyHUUIt9H6O5Y_qxfvQz62w4jWIVqtuKPZ6L76hiojT3BwEiPb6MazQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از پیامدهای حمله شبانه اسرائیل به دیرالزهرانی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/146028" target="_blank">📅 09:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d1c3bb64.mp4?token=CqOUYmKzV-UkDPs-_RQHyZ7Uu5KsQ3F3q3rc9Pi9OefqeFoAvdB-sHIdpgtkTc_K3HHEo9xMju2VbB8kgvQMk0BKvlkGwcnfKCt5PaZVWVoW3IKH_gYBcFG-UloEcFndUHa_IfrHJC4Qc7XL7UV4kVn4lMIqwUhkcba6_pXo-M4PL9w1p4p5WHHeVb2hnqecrSFIJ-KaB_Z1yqbL10DVXVjPndHBnL8rH0d2Q03KA8373A9LGWDOQ_S8bdVcjopJFDzMBfHSKCVvFm4Sb46XfhcuXKK4-GvsIx1GabFEgSUY0rPvfxGkSU53pHXOaUbuXIepSHTWJK1GQvZM7uoccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d1c3bb64.mp4?token=CqOUYmKzV-UkDPs-_RQHyZ7Uu5KsQ3F3q3rc9Pi9OefqeFoAvdB-sHIdpgtkTc_K3HHEo9xMju2VbB8kgvQMk0BKvlkGwcnfKCt5PaZVWVoW3IKH_gYBcFG-UloEcFndUHa_IfrHJC4Qc7XL7UV4kVn4lMIqwUhkcba6_pXo-M4PL9w1p4p5WHHeVb2hnqecrSFIJ-KaB_Z1yqbL10DVXVjPndHBnL8rH0d2Q03KA8373A9LGWDOQ_S8bdVcjopJFDzMBfHSKCVvFm4Sb46XfhcuXKK4-GvsIx1GabFEgSUY0rPvfxGkSU53pHXOaUbuXIepSHTWJK1GQvZM7uoccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کفررمان در جنوب لبنان پس از حملات هوایی شبانه اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146027" target="_blank">📅 09:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=W586nkKczWtWLodQYWbN_jehfWOWcf7uSyolF7o1fHCGSDWdJ5XZMh30ZTpgMnVuWie3L6QCLntPOcsJdb2AkxQ2q5uxi5HKv7eiJ5waRw46_wAzkKLWGYEWdYtbZyxF7IgaBkfmC2v9SIDr0c312ezpEWHQZSUTTuwV73q9lK9JxIi2zOyV6Mpxf5wRqKxGZgOmYovdeB8ZQwAlj76YzyZjAuR2OIFbH5isJAN4HVWv3Q8sdRvc5du2DA7P1mjNmZ_vRccBWnosK7Oz90EUcPqaKfzArC6P1W-r9aKGokDkTSyqFLvHzBGOXddv-dtWBUo6gilrked6M4jQ-3FWZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=W586nkKczWtWLodQYWbN_jehfWOWcf7uSyolF7o1fHCGSDWdJ5XZMh30ZTpgMnVuWie3L6QCLntPOcsJdb2AkxQ2q5uxi5HKv7eiJ5waRw46_wAzkKLWGYEWdYtbZyxF7IgaBkfmC2v9SIDr0c312ezpEWHQZSUTTuwV73q9lK9JxIi2zOyV6Mpxf5wRqKxGZgOmYovdeB8ZQwAlj76YzyZjAuR2OIFbH5isJAN4HVWv3Q8sdRvc5du2DA7P1mjNmZ_vRccBWnosK7Oz90EUcPqaKfzArC6P1W-r9aKGokDkTSyqFLvHzBGOXddv-dtWBUo6gilrked6M4jQ-3FWZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید در شبکه اجتماعی X: «در روشن‌ترین روز و تاریک‌ترین شب، هیچ شری از دید من پنهان نمی‌ماند. آنان که قدرت شر را می‌پرستند، از قدرت من برحذر باشند…
نور فانوس سبز!
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/146026" target="_blank">📅 09:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=cefPq2UatWZtSXKfjBl63j24N96AzPH_IakB0Ove7Kk8RwkmxR9f5GN38I85zS5_MI1OtBFE6cTTeBBNBSLZQ4v1us0p5kbZM0mBILp0zeHgwO0I4mEE8goupULytDk4utoCrtNwciAnzCfBKWvHxceLvPmX6gxdDT-bD6vjEp64eeT_csz-7tAFhr6GztUNcHr3AsmktE5rB64WxVJZdPyZtw97x0gC2__I5KinaAd18RhQ3p3zJz4CzzRMaix44InJhvJw-i8OwvVUm6SUFjPn2AY-NE4FP9w-DBiDXJsds66BmpSiwXgJCqZNFM4s5MZjtBYj2uhMWlNIUEV_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=cefPq2UatWZtSXKfjBl63j24N96AzPH_IakB0Ove7Kk8RwkmxR9f5GN38I85zS5_MI1OtBFE6cTTeBBNBSLZQ4v1us0p5kbZM0mBILp0zeHgwO0I4mEE8goupULytDk4utoCrtNwciAnzCfBKWvHxceLvPmX6gxdDT-bD6vjEp64eeT_csz-7tAFhr6GztUNcHr3AsmktE5rB64WxVJZdPyZtw97x0gC2__I5KinaAd18RhQ3p3zJz4CzzRMaix44InJhvJw-i8OwvVUm6SUFjPn2AY-NE4FP9w-DBiDXJsds66BmpSiwXgJCqZNFM4s5MZjtBYj2uhMWlNIUEV_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی لحظه خروج هواپیمای باری آمازون از باند فرودگاه بین‌المللی میامی در روز یکشنبه را نشان می‌دهد؛ این حادثه به کشته شدن ۵ نفر منجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/146025" target="_blank">📅 09:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت نیرو: تاریخ دقیقی برای پایان خاموشی‌ها اعلام نمی‌کنیم، شاید زمستان هم برق برود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/146024" target="_blank">📅 09:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8AyamNwWDz4uWRVTvqM-SaPfMNha4nqSADFySsfOQDOf2n3UkPSP2eHLwUu3rboYfJFK_6fb8laZ9Z3-_ppgLrVNZURyfe0LWUAgeTW9MFiOlr6lCNpvkVRiVgrNQYS_3LaJU8t1ZTdCUhTpo5z7YFVjIUSbB7WtOy7zoVGttUaYV78gozc00cpN26Sc9y4IVI1pL5DDPi8t1hNgKuW5OdCtDEUMJcsn9qojW5q46tBHqp_flKZPts2A49QxDjTxdjN4OkoXO8rvxpgVkryv1a_GTqviEUzfy2_GIAj3-vUdfzAxhcu2CraVFnUahrJQ5owuLZwVizq2WKdmC9saA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
برای تخلیه یک ساختمان در
دیر الزهرانی
در جنوب لبنان هشدار صادر کرد و مدعی شد این ساختمان متعلق به حزب‌الله است.
🔴
ارتش اسرائیل از ساکنان خواست حداقل
۳۰۰ متر
از این ساختمان فاصله بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/146023" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سپاه اصفهان اعلام کرد: عملیات انهدام کنترل‌شدۀ مهمات امروز از ساعت ۹ تا ۱۴ در جنوب اصفهان انجام می‌شود و احتمال شنیده‌شدن صدا در محدوده صفه، بهارستان و اطراف آن وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146022" target="_blank">📅 09:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آتش‌نشانی: آتش‌سوزی گسترده در هتل آپارتمانی در مشهد
🔴
۳۰۰ نفر از میان دود نجات داده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/146021" target="_blank">📅 08:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر ساعت ۷:۳۱ صبح امروز در حوالی دانسفهان و شال در استان قزوین به وقوع پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/146020" target="_blank">📅 08:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کپلر از کاهش بی‌سابقه تردد کشتی‌های باری در تنگه هرمز خبر داد؛ میانگین روزانه تردد به ۱۰ فروند رسیده است.
🔴
شنبه فقط ۲ کشتی و یکشنبه ۶ کشتی از این مسیر عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/146019" target="_blank">📅 08:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا جنگ را آغاز کرده، اما انتظار دارد تمام جهان هزینه آن را بپردازد و هم‌زمان ایران را مسبب آشوبی جلوه می‌دهد که خود عامل آن است
🔴
این وارونه‌نمایی، به‌ غایت بی‌معنا و بی‌اساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/146018" target="_blank">📅 08:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtBodCo6Cu7Oxr6rFGmHsHwKo6-yaISsDlogT88S7Mprua-74WOJTyPrmx0LfAE_R-a5TNVG33l3Zt0Lt1aa4Wa6b7g_zcx2xJpWq6oJP5NEw23z9RreBHmlyNjuYq_7CMttV4qVtaKKvY9KKpHlAwAaMJqrh0Sw6QohjYjkY12f3qwH_WRKV3vaD22r851Nmf2vYrBuIFUCV1TXSG6k9jgZ4_BtqMTVnrX4291USQo5cUqyet6xVmytPS4iAZC9jppAem_88pWrVvMheiGj82BtXBBw2NwGEfcjulqjTRQkPtQzv0VP6xI414BV1Ph14kpms9WL4RcqKqYPgLXNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید تروث سوشال ترامپ که یک یونیفرم برای نیرو فضایی آمریکا نشان می دهد.
🔴
جالب است که این یونیفرم شباهت بسیار زیادی به یونیفرم نیروی ها امپراتوری (نیرو های پلید) در فیلم های جنگ ستارگان دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/146017" target="_blank">📅 08:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b63173fb93.mp4?token=pWJSuKQ-g-qMw3KeaRKloildVp4T1n_4-BD4j9n6fFNg5ihG0jHDkYDVbf1bZ7fn4YqnoLeMdv9I6lR2SRm7huQFTIkGzFxWHli5y18vvmvQ2HAea3Yf1Ey7i0m451YE1GSKnVI7IrsQD6f6K5oK2NKsRyPPu6dKO3OR0bGxTbpUhfjKZvEH14o01as7LfTIcFj1ssj9YJaxM97W2kPojeh007fzupxN7eBZ2SCtzqIAunV9Pm15TPnlC0BIBeZhPcRtqG0COsDKFLfEnmLvcW2jYxWHR2vx2e96Ozfqk5TNOcTVP0MBaI1WbyUrGhBht6jUFnFhoVoZG1TOOr2j4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b63173fb93.mp4?token=pWJSuKQ-g-qMw3KeaRKloildVp4T1n_4-BD4j9n6fFNg5ihG0jHDkYDVbf1bZ7fn4YqnoLeMdv9I6lR2SRm7huQFTIkGzFxWHli5y18vvmvQ2HAea3Yf1Ey7i0m451YE1GSKnVI7IrsQD6f6K5oK2NKsRyPPu6dKO3OR0bGxTbpUhfjKZvEH14o01as7LfTIcFj1ssj9YJaxM97W2kPojeh007fzupxN7eBZ2SCtzqIAunV9Pm15TPnlC0BIBeZhPcRtqG0COsDKFLfEnmLvcW2jYxWHR2vx2e96Ozfqk5TNOcTVP0MBaI1WbyUrGhBht6jUFnFhoVoZG1TOOr2j4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درحالی که ما داریم غصه دلار و قیمت ها رو میخوریم یه عده رفتن شمال پستونک پارتی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146016" target="_blank">📅 08:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVSpXJegSoBPhd04Tcyet0ihP0H7HU_xX_IA3osZl8M-7tIvg9gYDWDDV6oUzth0mF3zBYW7dsJgkDGo2DpauV3yhXjRq0XIrmQaIeg1OlVcMDcSqTTEtk5NxE7vhO3i39VEACp0YfMe5oQsHf149TopkE7dnnDlCHXPUD8vlKlM2TrhjJW9RxpQeX2OWfzWPURRF7gHTrxu3w0ooGt6coRKjZUy3MuhQyv9a1jlAhv8PkJguQDSs-NVi0o-kL4PDk2zyLgkTCX1CD9fU2w9vdcPQ8-O-tESRLey2IpvUmIAWucawzxD6Kxj865NqhVFw5lkQTwpQutUg_KJ_NRz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: برای آمریکایی‌ها جهنم تدارک دیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/146015" target="_blank">📅 07:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH3IwQDGgfwmtLGDvPs16SFEhb7_PtsI1KFLYKp7N6UXd3CEJhynd5YRiT84OJx0K9ZO_Jq-KVFaMg-ZoYThgzhsiouuPgm9SjXMZCEceSuPWEFevaeuEDUTdbYWB9Qnr6UlDACGLgpoVogHTyAHo84mR1PNrcOwwIVfkOo01bP3e9ZHFk_XB4laIsi_pdrfIKExyXFGcsOGzAnOME7lRyaItIjPHNC0q8hk6TIMT7pj1mI3z9eAErbi4jMZ8ps1NDbHFLT3_j2hQ4tSP2GlAqBNCaREu7GnnUzFxX15W1glDq6YdTHahieAXao-CHEOtk6KWgilPwVdKVAwnxjJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">LIT VPN
نسل جدید فیلترشکن
🔥
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
🔥
فیلیمو
و
فیلم‌نت
و
نماوا
رایگان
‼️
سرویس نامحدود فقط ۱۷۹ تومن
‼️
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کدتخفیف ۲۰٪:
IRAN
❤️
ربات تست رایگان و کانفیگ:
@
litvpn_bot
🔥
ربات مخصوص
همکاران
:
@litpanel_bot
🔥
پشتیبانی
۲۴ ساعته:
@mahan_lit
🇩🇪
•
🇫🇷
•
🇳🇱
•
🇦🇱
•
🇦🇪
•
🇴🇲
•
🇸🇪
•
🇪🇸
•
🇮🇳
•
🇺🇸
🇨🇦
•
🇯🇵
•
🇹🇷
•
🇮🇹
•
🇬🇧
•
🇺🇦
•
🇷🇺
•
🇸🇬
•
🇪🇬
.</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/146014" target="_blank">📅 01:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEl9xrNiRGk9XSUFmDPaL6OoEep2Npx3SpAcdeQKStCXos-6rXBG6xnCiC3-kIaUXTWEzz8uOfjoRKFxYbeEacgtCrAm-ppepuz0R8WWWBLJ1mBz5-5vcpHfNCecprESqYCRHvWP_Ta6SMFRFhFnwdkafwEL2OUbMNSO6MNcgvXLiuKV8-T0hORyGmLtnOPXa-aZFlpHa-CQwgmNAfT84GGGWPvE_zfn0Eyfsrx_lryEc2uvJB_GwqcFcFMLPNH7HT5teFoymPIo36dTaR7hxsPFZOtDF5JavCNqUbiKtQ7RJwL2VVoWuqTXOB1kYCdk1kDoyl78IpUD-byN9HqA-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رویترز، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دستور تخریب سکونتگاه‌های غیرمجاز شهرک‌نشینان در سراسر کرانه باختری را صادر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/146013" target="_blank">📅 01:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e8536959.mp4?token=CLNWunLZph812ybxhwJrrDem8EkWKxho3_xfxgiTxnVa79DeaPg_xjEP5FFfROJ-xPqBGe0WTrj8gWEUh8RugXZZ1BuVgWaIi1qA6KwM0s46vIwElQmmw9O-2eBOO-jfqE-Wq2Dgl-quTYK0iERek3vSl-VJqC1k9HIUwA5OznKUbX6DyUEYBIU80vwxeg6lv4SeLzccZ-s9mzjfXpbxNowqjHa7rTdXREqJNM4uv3J7sqfPoPxQFLHC_zRdOUpol_eUmv2N1IN5sKp-BJiYIlhqZm0EckqGmE0IVJ8i3quZvtVOQOQIM915Rt5CkxUqqehjn2T-_EK0sv8kQlmsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e8536959.mp4?token=CLNWunLZph812ybxhwJrrDem8EkWKxho3_xfxgiTxnVa79DeaPg_xjEP5FFfROJ-xPqBGe0WTrj8gWEUh8RugXZZ1BuVgWaIi1qA6KwM0s46vIwElQmmw9O-2eBOO-jfqE-Wq2Dgl-quTYK0iERek3vSl-VJqC1k9HIUwA5OznKUbX6DyUEYBIU80vwxeg6lv4SeLzccZ-s9mzjfXpbxNowqjHa7rTdXREqJNM4uv3J7sqfPoPxQFLHC_zRdOUpol_eUmv2N1IN5sKp-BJiYIlhqZm0EckqGmE0IVJ8i3quZvtVOQOQIM915Rt5CkxUqqehjn2T-_EK0sv8kQlmsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز: پس از فرود اضطراری یک هواپیمای باربری آمازون در فرودگاه بین‌المللی میامی و عبور آن از باند فرود، دست‌کم پنج نفر کشته و پنج نفر دیگر زخمی شده‌اند؛ این حادثه واکنش اضطراری گسترده‌ای را به همراه داشته است.
مسئولان میامی، پلیس، آتش‌نشانی و نجات و نمایندگان اداره هوانوردی فدرال (FAA) در حال ارائه به‌روزرسانی‌ها هستند، در حالی که مقامات در حال بررسی این حادثه مرگبار هستند.
اداره هوانوردی فدرال (FAA) در حال بررسی این سقوط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/146012" target="_blank">📅 01:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om9w1K7Hv7AqvpgnwKu31Yk3nj1TnOVvAe9TWWRzt0Qbe7wSPI4z9PbxEd9yLCrtv3MWWL_Hd1XAnPWANV2iF1BFUMgVMOZtJItBfvAo1sraBg6jsfwS5A0KKniTj5wdcQ7Gxf4v8SEdRdLvBrPmAbBwMNNk4knCtbOU6oQeVqqJyeFaH2JHhszOT550uP49O1LeBn-qO2KWCCakiDoooAjH6gyEs7tygY29dlZDysj1wEsKY4ISZ9s1atyzPgvxhy2g78i4qa1v0OdxMHk5ZVClJLhVBJsZWW59hnpI7y0ndNXDFXeXRxA9yYzqRvL58J7HYtyFnSzwcpqq3UTJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور چهار فروند سوخترسان به همراه یک فروند آواکس در آسمان جنوب خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/146011" target="_blank">📅 01:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/146010" target="_blank">📅 00:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=T4gZuX6gOAne1I1acQkAyrB0sXntqJhIcxJBFmRzuSBaQhvkrd5OgCSuNcqxw8y32xEh9H8ZFeeUQRUd_sslU4Om9vwzpk3OTjWmXcWyc5-_9J86VfJNhHYrswHzwjSNiQS6lMsgqmWZNYUhsDG2ErdKZfHNIS1q-yrbuYYSzPT9YzmMUv55h6UkwiY4B18apsV05NzIazWkIO1UD2VcEt4_euiG3W5UUy8Yw2byZwpP5KoXoCAsdWmnTuPTgL10dRq2iKBD0LMipaBbNS45EMmNya1UyEzClKN3JmttxyrKJsYbMIzVioiXkx6uPBfsJTfecnua4szvlIn9NwOzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=T4gZuX6gOAne1I1acQkAyrB0sXntqJhIcxJBFmRzuSBaQhvkrd5OgCSuNcqxw8y32xEh9H8ZFeeUQRUd_sslU4Om9vwzpk3OTjWmXcWyc5-_9J86VfJNhHYrswHzwjSNiQS6lMsgqmWZNYUhsDG2ErdKZfHNIS1q-yrbuYYSzPT9YzmMUv55h6UkwiY4B18apsV05NzIazWkIO1UD2VcEt4_euiG3W5UUy8Yw2byZwpP5KoXoCAsdWmnTuPTgL10dRq2iKBD0LMipaBbNS45EMmNya1UyEzClKN3JmttxyrKJsYbMIzVioiXkx6uPBfsJTfecnua4szvlIn9NwOzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلایه یک معلم از آموزش و پرورش:
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14
تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/146009" target="_blank">📅 00:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
🟣
این کانال ممبراشو غرق دلار کرده با سود ترید
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/146008" target="_blank">📅 00:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146007">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2s7c0CVIkH7uWlAtaDge4MTnh935BCwcvzAMFSOZFAGqZR2Iqe-LFLQ65h8ASnfeaYn4m55DDKj0hR2gGjj3UrmQ6w_Y8mrJ7PrzAXz1y30i4xrXhN8TWGOBYDLQaKZUqdVUsI8OdOZY4j7CQ2grTmd9o-1k6fZl2DlhKcDGI__SRpx14XLaPc8bz282RH3aRV4osNmOfm5p1gK1Oy77kDLvCiCyrq4-zsKL0_43nYYNOfQv0KApSKJBw8wJJthv0izVGCgwfb28hepUNztXqwQpO10z9Nq9HfR8vBAYk6IYb0g81VxFVAAzh1CJr5A-_VSqpoPrcMPNzF44HO8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار در تاریخ ارزش هر درهم امارات از ۶۰,۰۰۰ تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/146007" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146006">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
معاون وزیر نفت : تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/146006" target="_blank">📅 00:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
متاسفانه امروز یه جوون توی همدان بخاطر مشکلات مملکت خودشو آتیش زد و زنده زنده سوخت!  مامورا برای اینکه خودکشی نکنه، کتکش میزدن!
🔴
حاوی تصاویر به شدت دلخراش، اگه بیماری قلبی داری باز نکن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/146005" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffcc64417.mp4?token=ng7AZfC99MSSYXIR9zvjdpE06wyWXFAJ1KGBI40DGdLLY7hnuFPOxIr7yPj1LywbSSRnNVbpfHZby3pCHTbcFGGjYL7XkRqPVnBokIxanzVJXEWv6aoTPXTISiapvsLtFA5tDsxzYgeVyZZn3Qpep4xJXy2wZgfu5qQpbzHDEU6ji8RJ85bJTpasWoyPqhixnTp_HoLQvKlX5XMnbglE5LSVuDN80Jeabfk8tBQbYTcCZkWMyhWKTETlptSiB0-cF5LJV-JgYsSqShMPTtiwq10tW9CGtf81KZEJr68wtCCzFT2VmQ_c0-xC48xA_tWZy1Qgd-E5RAz0EZQ-_PwkVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffcc64417.mp4?token=ng7AZfC99MSSYXIR9zvjdpE06wyWXFAJ1KGBI40DGdLLY7hnuFPOxIr7yPj1LywbSSRnNVbpfHZby3pCHTbcFGGjYL7XkRqPVnBokIxanzVJXEWv6aoTPXTISiapvsLtFA5tDsxzYgeVyZZn3Qpep4xJXy2wZgfu5qQpbzHDEU6ji8RJ85bJTpasWoyPqhixnTp_HoLQvKlX5XMnbglE5LSVuDN80Jeabfk8tBQbYTcCZkWMyhWKTETlptSiB0-cF5LJV-JgYsSqShMPTtiwq10tW9CGtf81KZEJr68wtCCzFT2VmQ_c0-xC48xA_tWZy1Qgd-E5RAz0EZQ-_PwkVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های انتخاباتی پزشکیان درباره بنزین
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/146004" target="_blank">📅 00:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAhM7caZOjMI4wFGqwixkscbWB8OIp4wS8sVBUzEloFAU7WsTu9ATuoHOTdQAjRwUYcGTKsdKDONaxDmo3_sUj7dNaDSo8I6OQGzUbYOvSIO3Emk5NjtCoU3Pmls8Uf7H_i1l49VNlTIegZ0NuVHFwzq-TOdLsEzHhNlOfhOj_YcssHSpN3jHRnKvPg0E-AkxcK_SJLeedm4nBRSBlYeLKU4ExUbaG-StQ_w3GkegeGYH0GwbiPDNxUB4g3LnkplO39jZtPPQmZhS1dm6TWhvwMjQJRnGuQV7CTuBLciIdgFYWLQvsT0qIbW2RKrkoqo8P7V87aKCWCFMBMxOyk2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی درباره قیمت بنزین :
هم‌میهنان،
جمهوری اسلامی باز هم با گرون کردن بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خودش رو گذاشت روی دوش مردم ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/146003" target="_blank">📅 00:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
معاون وزیر نفت: جزیره خارگ در جنگ اخیر 550 بار مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/146002" target="_blank">📅 00:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0OqQC0s0LwfPUPpXMTNpJw-wF3Ltv9t90_b5ulni5pkmji030Hza6ddPr6l2VF1_mY9Jbnp4ZtylVFhJ1pKyhgVi63X_g670AEm_Vt-raK6cK2Y4sZiy71-N5r4QwlIHItlDjy87TjF8Pytwv_u1Nf4ZGm2HWquOORWHc50Qp6XEYVZRcrxytom5rZywgqsaGHqMxs1djGdcjr05qgJMtZ-QlA_oqW0ezVELUXHP8iznxOsd-cHJlynA5ZkVeMPSoZX1E-_YJ1TrXPMMNkHSC5ljrklpCTosvyMKTXosL15gB31-GjsxCGeD9UZOT2TF7sy2Y95tjVf2coIefLfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاپ لئو چهاردهم خواستار صلح در اوکراین شده است
🔴
او به طور خاص گفت که قلبش با کسانی است که "سال‌ها در اوکراین در رنج و ترس زندگی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/146001" target="_blank">📅 23:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e2881c65.mp4?token=o93o6iSFlVKAx0_08psy7OEOEfxGj3BOIL97lfO9oU_aUnlrwiwMLAvDbmhvL2wHPaNFj4LdY0kYLyNXZdJM7jAFEkG30J5sltrYZPh29dPcNlkoGF3ioIN42X0zJMc8juYPoyjU7S45dXGy7m8rukQaci4CVQH1LebbLeKH4dwg_LT8KJGqoHHrzJmzoglEhOwh_OcWCpA6t6MeY6Vk-lk5RV0926zaYcgzhuLzR6C3y4Ahzdga1MZvQpwtn5hBLcQPmlc6rf7AqtUb2Zf9x0Wpq4agJ84ut8D9Okl-P1hUPmkAacqZjI4GU9wGlskR7shgJZRFOGJU_9JTKxvodKKHiw9rTCBw4IT0Xv5S9CHOAPeYU-WmZZqWY-VeMN3eRnDJF6KMKS7UiZLs0xog1GGkgwLJYEkJzUXETx-v2Z6rjGG5w9mDGW1KbJmZoYW0VV6iVll__bRjdLgxlRTa75JOhwKAgVi0eKAZmTVDW-57a4i21Kr3vD3GAqETO17S9ALalvO4WNKd0s8JKWwrB6O7i20scFUo5LeYvRBbnNHDqk9X98Rz_LdWZ9j32wAMX27lS9s2f7zigVAy8fdazkegMNgfDDT6JRfVqFChwaL5nFz7-9IgB8rt_r-qBvKCgLGxfZzPHktKOYmNfj1EnqWlgT0GRF9AFKcsOZYmlmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e2881c65.mp4?token=o93o6iSFlVKAx0_08psy7OEOEfxGj3BOIL97lfO9oU_aUnlrwiwMLAvDbmhvL2wHPaNFj4LdY0kYLyNXZdJM7jAFEkG30J5sltrYZPh29dPcNlkoGF3ioIN42X0zJMc8juYPoyjU7S45dXGy7m8rukQaci4CVQH1LebbLeKH4dwg_LT8KJGqoHHrzJmzoglEhOwh_OcWCpA6t6MeY6Vk-lk5RV0926zaYcgzhuLzR6C3y4Ahzdga1MZvQpwtn5hBLcQPmlc6rf7AqtUb2Zf9x0Wpq4agJ84ut8D9Okl-P1hUPmkAacqZjI4GU9wGlskR7shgJZRFOGJU_9JTKxvodKKHiw9rTCBw4IT0Xv5S9CHOAPeYU-WmZZqWY-VeMN3eRnDJF6KMKS7UiZLs0xog1GGkgwLJYEkJzUXETx-v2Z6rjGG5w9mDGW1KbJmZoYW0VV6iVll__bRjdLgxlRTa75JOhwKAgVi0eKAZmTVDW-57a4i21Kr3vD3GAqETO17S9ALalvO4WNKd0s8JKWwrB6O7i20scFUo5LeYvRBbnNHDqk9X98Rz_LdWZ9j32wAMX27lS9s2f7zigVAy8fdazkegMNgfDDT6JRfVqFChwaL5nFz7-9IgB8rt_r-qBvKCgLGxfZzPHktKOYmNfj1EnqWlgT0GRF9AFKcsOZYmlmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی: افزودن متانول به بنزین به صورت گسترده صحت ندارد و یک دوره آزمایشی بود که تمام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/146000" target="_blank">📅 23:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XX8hMzzszurFD6ZmRj3GHXx2sByrvdDP0Am0LzSmJUMVNp26APlKmrh9Ukotz0CSGM3-a0L0P9H3fWX_UBipmqRxoze0G_eEyOQwjz2gRq9lUP4_BlTX3thwI4xQMgNYEtkEeE7nG8biXq2EsR4OME02DwHZtfr1hTMKUUh6f_5IP_9XfP9abPViVEKEg6Er8XqGWHiY2yRLOphQTgaVR7YRv7YttDSi4RAX-Un_JjxJGQ9mFYqHyOrabzluKXWsQPSnE8qkviw0IkOgu9vREHzSce6OAFybazjFxtj0CpiCkIlbq1GDMjFn1-1K2DhEhYUXHhdJFq7KvxQ8ibq7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8-82bWOQ9Sx41XjzG-24m2iReN82CBl9mHjMlyM9PC1mmz5tcx_-GHQ0QjAb6sMxQEBQrNT4-jDdrZ6PuNnZhTSjNZwgE3LoJPUaYS-YYA0y_1SBCD5NulhQQ8_u-yKXGLRmP5gRDzu5Q5mh5f2tjD5ax02czIBNTYpBRkEfRk2NP-w-V7XWqOVLwUWG2pC43o6r2nnrvl4zOcv_GFFh-rkmNkVUzTXpGHC6RRrhbS9ZobZoVfH4BcCoBNT8ArsReaBhkTIVtcAFFVrjEzM0h_KosSTcBkSc3PW9_qZTPInkbl53Hdb-1o8Gr0dgqqTW48gPNubqjtLDGuyqaNcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYMDZZoQB2TVt1PuOWnLvbS9CqCQx2upZ5TEDuQmZS4usl-ikOUKIb7KdOLivYtSi9z5Cd81paZj5K3vJ8z1-hUfJzX_b1ISwxLKxvy82ujreGnxGGTxVOzMvVOwIgUBE9cHfgyCF49dKgMeST76nw85TKVvk-VbbuF2MusUaNBwh2sWk5qY1QM48b63NIfEkSn9mvQaOZC5_ijgbbZ881hyo-9ua6qALa8k99MN_b5l1qU1VbWoD_kQdDD5d4xRSWu9rjlmaBTgmwhTH8dQBiZ46INXt8d5bqgA7yU7B9RXs6HnXcGDw8AhabRkCWSblytSy5c-hbnh9_1jqWqTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJA15-xi6BXkQuIKmsfkxHZkUzl0kh8kzoqnr2VukwigtcFn6a1hCLqmV4hskfWQThvRgqp_8zJVfPuVdbRox8OpQUCzrsM_CwsO31MJV0xfr80a1fGnYPaXT7EQxhHvlhmcHj3x2Qw_Q00HY0kanhHR2YwcuD1WONs1d6LSwwR07TATjwm34n_wmCpy3n7OSpINQfhI4Fx_uQzvGCLweHBQeJC2tRfVC_RUHD3i4inQAhb_YXOVfsuARjFYjNJ1B_8l0-FcJtpIJTWY-h_J-0k5Uz7_DXGZuDQyqjOcnYD7GOQOzzLt4PyVQcWasQyN2ln8Yp8wguu3zH5hywE9cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ
...
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/145996" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c4b43fe31.mp4?token=oc7r8hJmsnzEu5bmzSd2GTMjqpWcH7f4ZYj15A8qfmsjbxZWKd1eTtKNOmsczxc1wPRya1zYJCOMPDOkSLIu6cKtze99N-z9CszkfpPdBXpUXxdpU8_iV-C_jijIDDyyvRQyIIxK-Wu32pJFunNTGMv3M5pKVzaMjrcH_isIDM86jon0olQEQNVEKDCujwyWgHO9QEjy_72A8Dv835M6AahvkSrPULAVLd5nFlRgcKDi7Jt3aHcsO2UdOWxvLY7PxHrWa7mhjo1_Yl1j20iRvwupA7SEgVd02M43LTDOFgdYf0008Xe2ySYHTx2aH51OhtbEbgzSE1CrYlD9s_nnJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c4b43fe31.mp4?token=oc7r8hJmsnzEu5bmzSd2GTMjqpWcH7f4ZYj15A8qfmsjbxZWKd1eTtKNOmsczxc1wPRya1zYJCOMPDOkSLIu6cKtze99N-z9CszkfpPdBXpUXxdpU8_iV-C_jijIDDyyvRQyIIxK-Wu32pJFunNTGMv3M5pKVzaMjrcH_isIDM86jon0olQEQNVEKDCujwyWgHO9QEjy_72A8Dv835M6AahvkSrPULAVLd5nFlRgcKDi7Jt3aHcsO2UdOWxvLY7PxHrWa7mhjo1_Yl1j20iRvwupA7SEgVd02M43LTDOFgdYf0008Xe2ySYHTx2aH51OhtbEbgzSE1CrYlD9s_nnJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متاسفانه امروز یه جوون توی همدان بخاطر مشکلات مملکت خودشو آتیش زد و زنده زنده سوخت!
مامورا برای اینکه خودکشی نکنه، کتکش میزدن!
🔴
حاوی تصاویر به شدت دلخراش، اگه بیماری قلبی داری باز نکن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/145995" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thxnqaNEk81q1A1rkjrgEiqO6UiVPBRUgjDMf4DB0VkewY5-0KW1DkUrDzOUvCRK5exfjXJm7eruU2ExzjrMcQjzQN_BNDoNmiUyhS5mT57kbhcpnjup2HU2a8tb_C7YAoUnzCHvLByw-WeVhYjXOecbUVP2Aoc131iqK_tbN3vOSPL8FgXACTYcqlVMOOkk8vCt3vMot_7dAhIrJTc-fZ9Sv5yT9q1ZPNdyfNTp_vAmazySBiTyk1c8bKLdzt2gjhJCmQSLwgFZyJSQOiraIH70fnpzwPftgfsTQc1RMR4hCXBJT-rjjTPMHSPquHIKLmby4S84Rkzv9yf2wSyXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ایران یک کشور در حال فروپاشی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/145994" target="_blank">📅 23:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNq_hQSVpHaosaeyJF5my0bAd4nPySiZyrqq1rJd_z7ixXbq2sLRUtk4_dXrh1sa8jXq6b2uGIV52r9mwexAPIIkOtNL6dYFETmZx57PTNA8Qs4HbRSY1peb9UE4PoHYn4MY6WQ2C26jJTx3v2V-FpJR9-ezOImQVonCZ7y5o8eVhfwMBFRfd2x8X7_RhU4xeNJmjAnTR_sM3IjeF3KnbO69K6wemCDaR2NY0AAlmiC68PwMVnl-GjmoAahbBztmbdg2QBghclZ97buK5L3HWaX-YK1A5twzON4jPB7DKJcyOCcqDp2Gk8xhNP1LtEIX4vOLZT9CuPtRQ8OV4lhq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی
‼️
یه دختر مدل اومده چت رامین رضائیان رو منتشر کرده که رامین بدجوری التماسش میکنه تا عکس نود بفرسته
😐
مشاهده عکس‌ها و چت لو رفته
⚠️</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/145993" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند
🔴
توانستیم با برخی تدابیر ۵ درصد افزایش تولید بنزین داشته باشیم
🔴
افزایش قیمت بنزین به صورت تدریجی انجام می‌شود تا امکان انطباق برای استفاده از سوخت‌های جایگزین فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/145992" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون وزیر نفت: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/145991" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f556fb6178.mp4?token=CvFDRWYLNIM954RXfDrEo09V3QQFX71BEki01eQ1KMNNVZvADb72Mq1KFW2iY5dC1mtNJ31t0fiVPh08jBKlvyd34JkwE6ziEPAI4oXsawllx-znGlW0XkcLtcr7XqVN2IM1AW46qpVYHAkvjqBRLe7C-aeFVPiMTW8bVcg5rDBqNOhH0RVVceoTLdwz_Frd_oa0SmqeSbZHhZhIyuuw-LcMgy4MyPrjPD5zp-wXe93057hDWj3SBMKMgPplBp0sKzuSBLfFPcctfqGAluNZDdKFZnBHGeydCkEHbXRSsAOcZABg-y1Jdiv03MR-A60QXYB4NCETrJfjqvadUgzKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f556fb6178.mp4?token=CvFDRWYLNIM954RXfDrEo09V3QQFX71BEki01eQ1KMNNVZvADb72Mq1KFW2iY5dC1mtNJ31t0fiVPh08jBKlvyd34JkwE6ziEPAI4oXsawllx-znGlW0XkcLtcr7XqVN2IM1AW46qpVYHAkvjqBRLe7C-aeFVPiMTW8bVcg5rDBqNOhH0RVVceoTLdwz_Frd_oa0SmqeSbZHhZhIyuuw-LcMgy4MyPrjPD5zp-wXe93057hDWj3SBMKMgPplBp0sKzuSBLfFPcctfqGAluNZDdKFZnBHGeydCkEHbXRSsAOcZABg-y1Jdiv03MR-A60QXYB4NCETrJfjqvadUgzKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی: به طور میانگین روزانه ۱۰ میلیون لیتر کسری در بنزین داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/145990" target="_blank">📅 23:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی:  تفاهم کریدور جدید تنگۀ هرمز که ورود و خروج آن با مدیریت ایران است در روزهای آینده امضا می‌شود
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/145989" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYvgjmOi4wX2IgRl-1sk_zv9e6lZwjbUiOcrdDGRb7OXSKVlrrct42fcAW3llsYEVuwsOL7mMSKSS09130rVgYDJJwFzhCGHHYSACeFFr9UmjV5shA9m82ncqPhl6uBPo7FXKu_8TTIW3hxjBfzZVBZlsJl9Fpr3CTbmJYMQxUOwgvg-RIyjDMutY-dSwZLN-d_59LiIkpOP4LsgzASr5QxY_J1fhvS9FgVP_4C9yfEm2WL7E02HTIKooLyvbCkKEs5HdWcg7tKIEQv_sPgAeC_qQK0gE4-S3EFtLnleEwtzZVmQ0LeWpt88TOD2uqhZ4h1qkHBFNicxJPwp_SXZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من این کار را برای کشورمان انجام می‌دهم، نه برای خودم.
🔴
من صدها میلیارد دلار از طریق سرمایه‌گذاری در سهام و سایر دارایی‌ها برای ایالات متحده به دست آورده‌ام، نه برای خودم، و تنها کاری که انجام می‌دهم این است که مورد انتقاد جناح چپ افراطی دموکرات‌ها قرار می‌گیرم.
🔴
این بسیار ناعادلانه است، اما چه می‌توان کرد
✅
@AloNewd</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/145988" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4LQl7W0tV9dHgAOnUlVPYSDclnjGOsnpXYlj0fC3mtZd4bajG8rlrpL8hmH9FZMhzbKtfKFP8z581NiNbgQBnhWAJcDVdfwKw3GVM4AaU7eF77FCmJytlQgALEZbECpIG1jjzplterBFRRS8MLAHzylKoX_3rsoFBfCpT2bgq8HpY3NohMdX6nouh4ZF_N27nw2WZ3iNbiNMP0UiJU5rIYe0vxJa-CFiIvxQBjK4OISyhcugWjaqPmDYS14tYNMO2awwiCu5T53JegzN7BnI4lt6JOs7pNYvwFiBz45v5fTPCix41C2migL7P-lXUH0Rkf8n43WhJnC1Odb0fXkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر رفع فیلتر اینستاگرام تکذیب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/145987" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145984">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZkc_k8C9iOFZxBVTT67BgcPvMklrtSWiKlvINtVt0zK1tp0usjvBYilid8kcOCEEESNse45lupWjdPRXF6sbENsRuT4Y4XWgmWuOv2uKhFE4xRwcOvTFoYLGF91L8jRf_Yf2p4N7FoURR8spP44q0jKh3dlzjtMror6OZe242-DrFZkEBTNxsxrZrwlwauDlYe0qclfeERxws9r_eNSDjjh6pFcd6qvjASUSy5mo8865TBshhNfbtBGS-_uw7naaYTzjUpCbs5n2R6HM25vY8lmXhoKJG-32YLf4l_jlC5uBEI4cUnNA5Pgbyi0uDxZalgpJemmOrXx1v-hR0bt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcVis4J7-P33zHMsId9E_auadgbFhd6rOFBZp1Gxeas9-6I7hd27AtRzkIIVVygHhLSesd7HLIGT9oEaAg1i8YUBBvA1OH4yO53CbXLAGonIxm_J2t-widg9rOq_XXNXbLm_4m2VCkdEZLkrZpjlrXsxtM5pfLbdTYUlYIF8CiOOv49HiHxDi9WdL__5Y1QB83Ah_YN_J-0d_Mw2pc--HNbSaDZSkWYFpBgxTLmlu3dOZvCd9FhMySVvcBXjYAwU44fyzWFAZYFfrmHR6C_udddEqt5P0SlJFJ0alFSBh_UGh1_RVKssm2UTt-cGYBlxCI1Z7yBEc7EOLZWoC6mqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZZpxGMKL5BGxSGqUu-rsurvfa4nPmZQBWSyHAV6ECuNiosVKP4RNkccROvXE_98ttMzP_wC1UiTftSTQ-N2qtiJWvzn4eZLK5rHKin_n6lX02OhoOZv3Sqi2892kyZsU12sbPiCqqqEraop-eXyrmaCJOaleoXApZD8zbBM4xiH7MjLCFAf4ku4tg4Wvbjp9AxR1lTjkGAc2BFchIp1b2PyFSCAJ0-VFGBwruSWQYC1vxvNW4upUHzVJa6rdnhZIGHgFZjna-7Mp9EWazmEF3xBA7K5D3HDsLYJOZwbZWDbvptDmgJ9shu5kCJO5IVtOT_klrgXjFNk_dpPN8uWvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ درباره سقوط اقتصاد ایران، افزایش تورم، کاهش ارزش ریال و افت صادرات نفت ایران پست گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/alonews/145984" target="_blank">📅 22:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145983">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BglCKYjPKw8j3QPm3W944q7Ffg4wCrpsEtH6wczxN7rH1X-0Yj0ssHBbarJVDJCvjcTofO0nFcZI8nYB5Ibgs7CEgIw48yuUBd6hO4fLe14Bih7BiqbvtaYpG2d4GMlh89sEQBGG6rNMzR3ySe_CETF-Vttv8wmB_lr3WJ6oTqy1hUenOEYWao_9sLOLuuHEWDm38FOyD6QIPIZWyI1FfBaD4TvJYrHZ6J1Kx_Em-GNSywJQmrb9YFqlSpWHnQ659CR-bJB5TJZHl0JFOKyfKdNP_vue0YtcaKlrGsNo67EXzYSGpF_lPWW5ambBiT1YuRVRafL1umGr5zkK52ekNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث: بای بای، خارگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/145983" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145982">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
محسن رضایی: لبنان دوباره قوی میشه و اسرائیل رو هم شکست میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/145982" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145981">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فیلد مارشال گویا از تحولات خبر نداره و فانتزی‌هاشو داره میگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/145981" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145980">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فیلد مارشال رضایی: نیروهای مسلح  پایگاه تیتن آمریکا در اردن را به شدت کوبیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/145980" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145979">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فیلد مارشال رضایی : زمانی تعهد می‌دهیم که تنگهٔ هرمز باز باشد که آمریکایی‌ها خرابکاری و حمله نکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/145979" target="_blank">📅 22:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145978">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فیلد مارشال رضایی : اینکه گفته شود محاصره اقتصادی آمریکا عامل قحطی بزرگ در ایران است دروغ بزرگی است.
🔴
دولت ایران از مدت‌ها قبل به فکر بوده و به اندازه کافی ذخایر مواد غذایی و اساسی را دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/145978" target="_blank">📅 22:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145977">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da6516527e.mp4?token=QckYWfFWdsK48mb_g62UgEOCIVa64qzz3aigEEv5cnglHtTeOp7iqQytKEmSYBGv3GT1EUmI7lZ9jKuV9D9_B_JjWxFi3fUlDJhWTqE2NqleZz6Y8KhgzZouoP0NiFJuk9Rxvqv_upXNrh8xFPCU7qlHWcaE50bePklmnlBMRO4o8dlMH5daHn3KZS9PHMUfGvBvDN8GG49JMQ-PnJMzuhCdgL0LLp_b834hUvd2gEQZMVY4aETWO78tR3dfxfCK60PisMxwpVtCstknZvrcOWeR6FO4stQfvSe4Hjn868YmKo8Pcn90qTn8e2fu7koZBrEhNd7Tq3eZKGuNOQNFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da6516527e.mp4?token=QckYWfFWdsK48mb_g62UgEOCIVa64qzz3aigEEv5cnglHtTeOp7iqQytKEmSYBGv3GT1EUmI7lZ9jKuV9D9_B_JjWxFi3fUlDJhWTqE2NqleZz6Y8KhgzZouoP0NiFJuk9Rxvqv_upXNrh8xFPCU7qlHWcaE50bePklmnlBMRO4o8dlMH5daHn3KZS9PHMUfGvBvDN8GG49JMQ-PnJMzuhCdgL0LLp_b834hUvd2gEQZMVY4aETWO78tR3dfxfCK60PisMxwpVtCstknZvrcOWeR6FO4stQfvSe4Hjn868YmKo8Pcn90qTn8e2fu7koZBrEhNd7Tq3eZKGuNOQNFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: در روزهای آینده یک محدوده ممنوعه خارج از تنگه هرمز اعلام می‌شود
🔴
این محدوده از خط محاصره نیروی دریایی آمریکا شروع می شود تا مناطقی از خلیج فارس را در بردارد.
🔴
هر کشتی وارد این محدوده جدید شود در فهرست تحریمی قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/145977" target="_blank">📅 22:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145976">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74089a78df.mp4?token=QhBTi5clVui4Nf1IRbp3bpOS8tMo3A_uhO2hos7Z3XhQHkxVu_MZW9YnUwvSgsXrQIhFCdAK-D1yckY3kfSR4vysaf-0EOhBpxZyOhl8IitZuKxCgX5XUcAkfn26RpgYswkQr-21nix29pubdchlgq9mjZGZt4Ldf5kFrrneDoe_M89xZxklDu-nvUVjlXH4vHrUVxIvKGOxJ_auJQe50Yt-VqgfnjeK7dHC5VqGimRgyi3JO6lfzTfjan33BOC9Og9bH26pAGyZCM05WvdKzqECPKj6V3z3WIMkhwBa5UhkICmNjSm40wOdpLSEeNykhqtp_ppcx9bjGazrLYWOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74089a78df.mp4?token=QhBTi5clVui4Nf1IRbp3bpOS8tMo3A_uhO2hos7Z3XhQHkxVu_MZW9YnUwvSgsXrQIhFCdAK-D1yckY3kfSR4vysaf-0EOhBpxZyOhl8IitZuKxCgX5XUcAkfn26RpgYswkQr-21nix29pubdchlgq9mjZGZt4Ldf5kFrrneDoe_M89xZxklDu-nvUVjlXH4vHrUVxIvKGOxJ_auJQe50Yt-VqgfnjeK7dHC5VqGimRgyi3JO6lfzTfjan33BOC9Og9bH26pAGyZCM05WvdKzqECPKj6V3z3WIMkhwBa5UhkICmNjSm40wOdpLSEeNykhqtp_ppcx9bjGazrLYWOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن رضایی: هم نفت می‌فروشیم هم پولش به ایران بر می‌گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/145976" target="_blank">📅 22:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71c571fed.mp4?token=HXg5cJAEInpI3T91pr-N1nLBqcgKtbFvzp18F4o841pu-NmCeID7QPhbq4hyZKLYWUN4-UFhTmYpRvUEIUXzmNnRzEllD9NCrT5LeBbs2BjgRt0p_2DRttjLRDjStWia9GXL9ZvNJtQw9aLGWsjAV5dZGSpyFwXPJsB9Vr_euv91dNzNYO3wiq_41jKbOQiqCO8E14Ii3RZRG7Y7hygx28mBy2J6sqsZ2Wm1psDiE08QDmv3pptojeblizx1I_wgbtxI7D1kxrozqdonaIs1WRm1CoAZg1omJ6E_DgnBJ4Sl3wOheNahRkmw1m4HLqQf8XGUzG-6vl2k-_Kv-PwBmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71c571fed.mp4?token=HXg5cJAEInpI3T91pr-N1nLBqcgKtbFvzp18F4o841pu-NmCeID7QPhbq4hyZKLYWUN4-UFhTmYpRvUEIUXzmNnRzEllD9NCrT5LeBbs2BjgRt0p_2DRttjLRDjStWia9GXL9ZvNJtQw9aLGWsjAV5dZGSpyFwXPJsB9Vr_euv91dNzNYO3wiq_41jKbOQiqCO8E14Ii3RZRG7Y7hygx28mBy2J6sqsZ2Wm1psDiE08QDmv3pptojeblizx1I_wgbtxI7D1kxrozqdonaIs1WRm1CoAZg1omJ6E_DgnBJ4Sl3wOheNahRkmw1m4HLqQf8XGUzG-6vl2k-_Kv-PwBmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظهٔ انفجار تانکر سوخت در سنندج
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/145975" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK4lKmlVsNuVT_QEv_qSOx9EGFoN1Nzdj01p4o2z4gJs-Ep9RwbC54Xszm6Hcf-wjtdwHHllrPO6blrfB9qcqfCUfc88HIAQ46bwutm57p0yfZHR9M0JCUrv4x-nfpfZDkM13MeXP7Vpnpt7ax4HJBg2ZV08i6Cn9QETWMlHe9etW6lcZF5UR2BCM4s5qdvWi9V5YWiQZ0YLmqEBvsP84aKRVcu5LEfixBIDN9n5-FU8At1_FMWi5mmYLB2sJdJj_KrijDbQ9mCwGDmDItC8o74EA3TcWgnxIQ9K_UIjYU4sPErvHWy6JMOhzBpfNHoLeF-5xrJdRisa5D7dO5a5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت اتاق جنگ اسرائیل چند ساعت قبل از اعلام افزایش قیمت بنزین
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/145974" target="_blank">📅 22:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
محسن رضایی: تنگهٔ هرمز کاملا بسته است!
🔴
بعضی وقت‌ها آمریکایی‌ها از صخره‌های متصل به عمان ۵-۶ کشتی را عبور می‌دهند و معمولا این کشتی‌ها هدف قرار می‌گیرند و هیچ‌کدام سالم نمی‌روند و معنای این بازشدن تنگه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/145973" target="_blank">📅 22:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⛔️
فوری/نرخ سوم بنزین ۱۰هزار تومن شد  @ramezanii_fx</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/145972" target="_blank">📅 22:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
از دقایقی قبل سرعت اینترنت برخی کاربران افت محسوس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/145971" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b309972321.mp4?token=Qfq-LDtmUI70VkZzil_WSFrRhVPAcRCHkr70zNR_6uvAA-j8oSAr_yq5tUQMLmzcq1wuQI_CMoObDN23Kj9BReUXBHQBNEcoG382A7qa0BMlFuERXn67gNzfjcCr94-TtAZfuxDf3oFdjjGdavbgo69tOqcLX3DQi5pDsLIB--q83XoCK9wMiIdQhT7ibqOuUbXjPZJlMoV5Z-WBy6DkEaOJqVfaQEqqPzoKb3Va1wbeKT_Wnu_ZWVuVrxHyMQJh41s5b4ZYdwcOiZRe1pyaXhOh0XZiq9vv--Mv3oTAglufVwL-tLhZXwC7m7SNpQOOZvcFCtSfs50fDmq2VzKVMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b309972321.mp4?token=Qfq-LDtmUI70VkZzil_WSFrRhVPAcRCHkr70zNR_6uvAA-j8oSAr_yq5tUQMLmzcq1wuQI_CMoObDN23Kj9BReUXBHQBNEcoG382A7qa0BMlFuERXn67gNzfjcCr94-TtAZfuxDf3oFdjjGdavbgo69tOqcLX3DQi5pDsLIB--q83XoCK9wMiIdQhT7ibqOuUbXjPZJlMoV5Z-WBy6DkEaOJqVfaQEqqPzoKb3Va1wbeKT_Wnu_ZWVuVrxHyMQJh41s5b4ZYdwcOiZRe1pyaXhOh0XZiq9vv--Mv3oTAglufVwL-tLhZXwC7m7SNpQOOZvcFCtSfs50fDmq2VzKVMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای هشدار زودهنگام آمریکایی بر فراز پایگاه هوایی موفق السلطي آمریکا در اردن به پرواز درآمد؛ در پی نگرانی از حملات احتمالی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/145970" target="_blank">📅 21:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145969">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
یه سری شایعه شده بنزین ۱۰۰ هزارتومن قراره بشه… ولی تکذیب شد فوری
⛔️
✋
معلومه با این ناترازی شدید انرژی بنزین نرخ بعدیشم بیاد… یک سال اینده بخش انرژی خوب نیست…دلارم میتونه دوباره بده بالا تا اسفند
‼️
@ramezanii_fx</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/145969" target="_blank">📅 21:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6PmUQBhemws6vb_dFpCROOF8WKYR02LV8T06kloz259GcrnzVhMW21bo3Erw8zAK6bFRldvG_iULwtrKT8ronkFEFyCI3DLz3ARWMvOVJLOowDRLNLK6FWd-ny1BvmRxgD-ZJ-sbCdPihAjv4dzvdasoFTprprKSILoxVshLEOtsv2fl5TRClhoL9b60pjwjD6ABAyjodvvabLZaAxU1Lli2e9w9vSSqBO0uLuHjO---IOy_MRzP4eDDkOHyKHHaysmEoWblXPp5th8HEsZtt9zHGirrAi_djO8G1V2VdtJxpy4-1dIXhoAvyc8QCH0eZr-uuZETFIo6uReSzh2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای آمریکایی وارد شهر جدّه در عربستان سعودی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/145968" target="_blank">📅 21:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCniPMnKF0Lk55U6zALEiRV6YFX-VdgfCvYoAcTiigXsCH0ZEBeEV-0y_07sW8bIdxfNRzmqYnNYb7-gcWUaGRYweTEZ1r36C519pqqlB_8hPqczIu58SIgFLPYr1JuMI7MlhOfUowuGUvWtv6j94KCsCWZr1aO84foGl3wyyQTWb-drRkzVc89GhU_vv-XkfZASkFHgJNxxD8mZlw0PuytcRs4jglJb22MRQaatxCcqiB5Q3Hoh43DvJ1rPBcShxID33U2G3xKsuMI_ktKvmMM067nmtzEyHmXXYw0Jecbn20CUIenWWDHjFoQa5Wd4qXdt-pXHWZJ_kPNoPuui-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: ماه متعلق به ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/145967" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoDcoIzxs_-beUiYcmuZ7OB9hsAMHSWE7U5L2TdcZYdQiztG9bS0vbuKtm8uM0pZTGy6Ra-nSiLYAwCJonWIRp2rNXA5GxuhgLbdhST8h9RbwMt4QG_FCwrnP15UH1Y3xwMtN_qWVgzh0QzxRoBuW5n72Z16NzozfBJSsZctwEgODB8fqRy_mXwAR0L1d1v0WBZh0cVxDUL5lqin4oW7h-fFjWb8t4_xbEoOW68Tw833NrNSzetch8zoep736bQm-1728PJvgEHII5k3mSTdL0SWSwarBzltBlUtOO6ig8u77IlARJlcMq2YjCt-EAkTXJqbbt_8FcFHVbh7xv0wzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/145966" target="_blank">📅 21:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAD58ewQazSkL5jPuygHNJnjojwQpLisYjgluY5R26qSrc0LogYNvuyVntaZX_tru1QXHCHC2JK8v1LBpzG0MC7yLVM30xNGA7LzpKYpZPDWkj_9-HJdX-IchvhfRwKWA6ET7UlYuusxeZb8h6drP0yuSVSIgEk1diAsp4AFBjVHGEHiuiIbf0qt7YUqfI1qOLcu0lDqeJvrYrTH5HE7iSHear_0L7OjLOVIgCQlQWSST7Mim35E0ykDYGUrWYI1eZmyIC1Ur4yEkrWN1EslmckYzUuMKhW4JVumTsxvnYPtuttIy084ozW1arKuIVzIZ-7o0ZzVeWClUWO_ZCndVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  نقشه ای را منتشر کرد که در آن ایالت نیومکزیکو با عنوان "آمریکای جدید" مشخص شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/145965" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piaT2ct49hxocFEVWLnuBpZ8CxrPNUS5oaiFaZ394Ov_lu44Kw-13n_vMtjIY5pwk3seRvHkBFCZ3QCIdGJhaww8PuQxKfp_6aqjpLU91DM1QfbxwM_aYEd-_jASKlfzi4vfOu8nKbmCcNSPKDRMUA8xTP2IphFNO8CniP7Fad_KUymwQfolPOQAsJuSL46LXt_6rAKpQmJcXN0oMcYyOWmwENy60j3E59tXpPafeW5mPFvpcQ_8MPMEMR5vNv6e7YqrPYvNNDW_22KSfe4FPjwUNyWKTGF6poNVOyuu_aZL6xX3QKWwnEbgucKvCtlVdWLNOQiYUEzwoJCmruwf6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، عکسی را که با استفاده از هوش مصنوعی تولید شده بود، منتشر کرد که در آن او و جورج واشنگتن سوار بر اسب دیده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/145964" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSSYGK4REiV7Kp3AX-OzXgX0KQD0_4DhbOmS4fzGwxhuTwf4DWF794adxZyVkjwQWJqo7orWQWfK8bCtAQrdmNkglXXA_LHW0OR8A6XeynYSkFs6l7MZw_cg1hUE0m7IWrR9UgUH9H9FivTnPF70Jb9WDBYUDh0OCJa1uWXldMbMF_ULgoefZciDH092fpFF_k4nlVYB8lAXB7pEec1uXeaiDMdY5tjLzH_Es3OLLlSxXN5d3Tb4NEDdmbqQ-nfVv16fiQiZei9nJxmPK5eZC71p7AQt1NYRZ1q1GChwEPIvkngUl90w_fA_uxMYiwPZfnDc_zMMgZbbdS5VO54WrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: رئیس‌جمهور واشنگتن از رئیس‌جمهور ترامپ دیدار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/145963" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faTS-PcFazS0fjcnCt0qicLd4r_RsotzoHCL14fU3XcO3LOiRQH04kMmTOpzgoiL6F7eJ-Mske2aVSKeA9mIjda4RL-r3FE1Zqf6Bub-Sn5j3WleIZFrx-k5KwXamRwYPcII8weptIh9Z0KZ2JSPFi2y9Mcp1UzWLPZ2JvqA05Xbg1jo7ismt0Gz-2b9FjIgGg8cdnTmr15ooHAiH0y1tM5UF_3AyNhCDQQ0GsopeYnDeGotqkFOA7PRfc1Hr6Vx3tgiQmFL_znsCxmxK9qj6_q2GkQpnUuZQP2jjRFLDzYHDGrNqcWedQh7et2ldhyrJyktRYaKDvKVfjVx06mXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت وضعیت ارزش دلار کانادا در برابر دلار آمریکا که به گفته او سال‌ها ادامه داشته، «غیرقابل قبول» است.
🔴
ترامپ افزود: سال‌ها همین‌طور بوده، اما دیگر این‌طور نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/145962" target="_blank">📅 21:22 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
