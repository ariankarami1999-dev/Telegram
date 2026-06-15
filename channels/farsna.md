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
<img src="https://cdn4.telesco.pe/file/gF2A3lKwkaisNQhpP8hTq1fpplwJXLaZw-Fcv2GG6qOMrov4rvWb9o_Cbk4OGVomY_RL3OrgIx6DsqGlOOvT_vsyzVfRk0Jg_QDNG7RfKZZzTeTnH48X6QHN44a4Wt3SE238iKinUvP6HbeV4IuOUQqaBPcnc3vL0CEhY-4hfjSVwRpopcwmjkgo5qeuP237ikeas8PH-wnA-c9KyGmZkY5HG7qUtwtCv2ePWudgX2Cnw7-QCgoeKs7SesHJnp8I2QBr6JW25APCZvvMdeQg7UYdFwDBPY9TiVkAATqCIagdh9vQcQXiIf2HAOpj5kbmBlR2_ZdnynX_76yFPuv-rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 03:17:21</div>
<hr>

<div class="tg-post" id="msg-442443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTgSPZdRHxa0sO9XRNuNaqQA5CG5WUkUGcApwsp1p1F2_QKkZ_0_2Tgu2TKfrAh1ZDTW5l-navuR8J-kxvUwC7RxqnYfpRL6AaLWll2_rzhwVWM_iUAeoTcvLa4vqvWba7KHWSl3XrQYv9nPR01Q4h6UzFlVJeuV9PwSof2CdyY8KVbvUJg591ElIQ45UQUFf46I_etnw2F0JX7YdP8TDwacTgSwB8YcCy57SNyOvzfxwfBXNm2UtyZz8xpCCyt5Ni1Baw67i5WMW-2jm3gy7PC5kjiYqLDZBEvqG5Fl0teVEyrlyBCGCbZ7V3FbaFv0fjr0Q4BfJLJpXPjByrmBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم‌ملی ایران مقابل نیوزیلند
⚽️
ساعت ۰۴:۳۰ @Sportfars</div>
<div class="tg-footer">👁️ 21 · <a href="https://t.me/farsna/442443" target="_blank">📅 03:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📷
هوادار ایرانی با تصویری از رهبر شهید انقلاب، آمادۀ حضور در ورزشگاه سوفای
@Farsna</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/442442" target="_blank">📅 03:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGfh5-3nbEX9kym8mqEBOBpVCQ8MTl0KFxmM5VFXn8o1-uADFUNDyqr-9HpC0obTq-FRi1IFGYqhhgDFCXFjKIyb_1W8QP6jSQDgt-9FDBodfmsawsQIU66enCxt2keuZrFr5_p0YWtaji_eEpphpXdWCfzgJRxmNiFgIbiSKqqbEEbCCbFKOlBdpwbo2eCYWNkq6omOtiE2a_llt8R002NJIzW756pjkoYvZB_cZ-d9clHlq5aabdAl4mgqw5XV8D9U_BvL0He_spECUoZibIEvYZazxo9x4eJlzeeObYPGPVOQWtUzaoVylqrYPcnyPdoRZsKVYlJnb9rtNyS4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUMoYfz1GP3vheExhfcWJjp9BJ5T5w4KPZAruAHIwZ8Q-8AKVO8EUlj7-2SO3TuTLbMW2f6WwuRgwEoDF6XGCx5dhxsUms_Cu39tK_6-k-1CIo6t0iENRa-rg7yQMWtxTxgLptjS_LljnVI9MkNbVLb98aX9H7BcMpj8cXQbSfeWcMJvDS2g5_a_kOvS86Twvj2r_qy2VElhUK-bpHyBd4DY_pvt0fKbalghA6ZBK2sbW-KYmsPrMDYIkTEe30Faeltcs2Z4O3UpiFDDF5yEa2Mu7pQs4_ekJF7TeH6QEgAfxu1c949NbPl2IlpSER8fGvFqKgSN4N_FE5wawDY7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FolUm2-7527ScYEsZhyPXOSywM-mcNlcGYvnz-jKgrUppY2irRLdqxHdsGTP43m_HaorZIUonn0qS38iKOFhhLWX1RSqZ8dp94Y7t8FG0oTB-XSmWYRMeQdUVoCGlnZsn7Q9hGGdwmbm11XYhTsEwK58XM6z8iLI4V-XDYBPKsl8lHR94DPe4tSj4bc-ZhUlxoR8c-H6tcy7iKQPMc1bjX9y3ctAu5jxJ_mH7Lk1JtFEYGdxkZK4zmGLmS7p7dCtd84IKtiS-ZgtE0lgMTJ3589UiHxBD9oMMXzA_iXM6zsDrqDKvQkD53pN7Ew5mWVuVQiBcKv7EPVOLE-Lt7KDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPaVBmxaxW4hGNb3QVEexyHKCTJVIGHqhRI7miqyX8GSgF3-7kE77TogrwdrhIUflIz7fsKwtWJL5BDFzfmsZMYfx_kaYYp0HNl9SOusCNC6qqMBB4I7PobaV5yWvoMmuZGO2N52eC0kj6rk7ixEChvcguErCNdyXdq7sgzlwkKFD7AoytBfMlsVsieGQE5hGTIwt2fRFYFB7CCoF6Hokls0AzBuaA7UzzP5taZizwkZ4ELjXq9q8HoPQTW0SVhuyT-T0uEK_MLdSKK67V21Gkdl_bcz6DCGRZWufdixtn5GG6Fi7qZ9ZRvr8tkM5a1LfSHCb32MQd3LIjTBOPduoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzzQBGz41dnuW45puLm3gE-jStdvBlo-5d6cNVE3jeHlJ5ViCyoytQcGgWSVIi-j-OOCSV5a2ZRS7qKZmaj4w6R3K1UZJH7QTlyux7lSRAMXPWbbNxmZB7OrX90e3mw0_AWF71PXNiVnWigHgj2bK2-G4BE-_tXiikRb7BwN4xwv2nXZZJmkKOraPs6IFp7lYZkJ00gWlZmhjck6OskRZD-yi39B-l-2FrNw0SHaP4buCFPIg0_SG5sJxEFv3SbP4796b8Pf5mOfDwqxet4C5FnXK01W0gn26W-vMc_1ffWbZOiiFCbQyEkivXqIU0w8-WDQMZUFOnxOux_Pw8ZrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCFPl6LoouhYg3SRXkPJRgHWQDqlx9MkLBQopabGCpcX1RLjSGMoZiOO53UNjTTxrGKxk035pAQ1naZqiG0biFeq4t-x65mbUWraXlE3JkDkRCxZqZhqNHbwlSHYx0s1EYrL3M1zfpLwykq6zpHif8OsyyDHUsJkFw9Rr3dxovJzFkdB-iqIVgKperWzyk5gcNmwY4F6VI5jJnfLYrS46-xGEorRXCGH6h6_Rhdqk4Ducjkl5D0AxuI5XGZyJWLYkp0AXdapeGOKZlZT2UqRQCrmV_NmZhh7LQonrJIjWo-rdWMdWhm2Jwx1DTkOhZh0qIswFpdKGk9hcBCeO54vwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعضای تیم‌ملی در ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/farsna/442435" target="_blank">📅 03:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5coHJS81oJJB4DsLV5rSl9lXhzxP6_dE4WgBO38vGRHrqvgRdWNcdzgZhx8dmffTxl3OiZWWQLh04JUQavLcjohLhMX2RqTZTb1gAgrw7wB_hA09yH9G3H_HBa_2RYkNYZMBePxZvow81Van_F8T0MyEqIZV8iIpe57TCFYUonC4GWbXJnjKN_DmJWNfcfT7qCsonpYmqR0p86WMk-86BOtUJK9LZQx5Zp3FPcYFMcUIbB9yLVS1iq7PpWQibgVWbwg278pAEyMaRL6FIBPc72BZF_shGXHNM-9tb9GQtZQNg9y3EJC0m9JXUxQjD0wJ_HfS_str0sYabZgp1uxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم‌ملی ایران مقابل نیوزیلند
⚽️
ساعت ۰۴:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/442434" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9388295890.mp4?token=MxxdVKHc9EzZv5tDOT15-A_T_0RrX1fwcj-MSn0heBdSUphgCQTq2EzSNtVFDZOsdqh-BegVZjjXoCDkqZwrxhCJ9TF11eA6lRHtyZbxSQJqHJxRVL8hWhUxjgkANZ64J7s7XMdxgdj0laUIrK6vl59V45JC6tr1nMReM4995eSHyfNcqR6vDpTcGVd-lNYjUyv3Kvc9-FYhblxseeqKYRGHVAvT1aqF2zha08lmYXCShzyPh5KSlR0ZJjKe4COz8_bWUrWgC4Og-UQYT53EiiSvD5HToOxnX50n2Cd4L8GoRQjBZtxXfQ9pk72CPdM3w9zW7R7TZG-qKZh9761wXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9388295890.mp4?token=MxxdVKHc9EzZv5tDOT15-A_T_0RrX1fwcj-MSn0heBdSUphgCQTq2EzSNtVFDZOsdqh-BegVZjjXoCDkqZwrxhCJ9TF11eA6lRHtyZbxSQJqHJxRVL8hWhUxjgkANZ64J7s7XMdxgdj0laUIrK6vl59V45JC6tr1nMReM4995eSHyfNcqR6vDpTcGVd-lNYjUyv3Kvc9-FYhblxseeqKYRGHVAvT1aqF2zha08lmYXCShzyPh5KSlR0ZJjKe4COz8_bWUrWgC4Og-UQYT53EiiSvD5HToOxnX50n2Cd4L8GoRQjBZtxXfQ9pk72CPdM3w9zW7R7TZG-qKZh9761wXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتوبوس «ایران» با بدرقۀ هواداران تیم ملی، عازم ورزشگاه سوفای شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/farsna/442433" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1ec016a2.mp4?token=KAk_jqt6VKWUGzw7VrXY_IQvXUqcYIazyvm-wsoyqsR1E5E2Pjqcjnaofna_0vNIZS1hnEJ1J-y79xKjtsQwiyx3T6vXHVXVF6sVd9W5slwuut9IDEwi-eUAv2LE8e0oibpobXy3GrR-1PLIgxIJyfMQi6T3sYGd0EY5NQSk9rAWyjHouQMQmK7cy5Dw2J5lavPTOHDuhUa36hHgY781Dj4P5aE1-AT48UQwd_spMm7pN7-0C9nbHMQOBKrydDx3I9oR9azhIHBuUr_ndM1KS0jFTUP9wghPDRLzOK043f0SDe8J_sjtX5jwwTle_yWwkQx-Rr4vx9j42Lay5ydp3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1ec016a2.mp4?token=KAk_jqt6VKWUGzw7VrXY_IQvXUqcYIazyvm-wsoyqsR1E5E2Pjqcjnaofna_0vNIZS1hnEJ1J-y79xKjtsQwiyx3T6vXHVXVF6sVd9W5slwuut9IDEwi-eUAv2LE8e0oibpobXy3GrR-1PLIgxIJyfMQi6T3sYGd0EY5NQSk9rAWyjHouQMQmK7cy5Dw2J5lavPTOHDuhUa36hHgY781Dj4P5aE1-AT48UQwd_spMm7pN7-0C9nbHMQOBKrydDx3I9oR9azhIHBuUr_ndM1KS0jFTUP9wghPDRLzOK043f0SDe8J_sjtX5jwwTle_yWwkQx-Rr4vx9j42Lay5ydp3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
العویس بازهم دروازۀ عربستان را نجات داد.
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/442432" target="_blank">📅 02:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74d4133ed.mp4?token=SkcyoEyhT3JA9GKVV10UJazegUwAUVrG2OeT8aPUWOhcyC2pyeyxSpbFZzu77hNyAwYEKBVHSHp3NVn3bMtodXo2RpeNE-0Wc8Nq8qw0k7lwYXdC_RZX1URxr50rxdbIJP4ozAdJfCxkHGFxQEugSCLBU_49VoHVr5U_APj1jIUVworGLQzYYz7cf3CY4vCEGAg4UtkhBf9TW8bHrKeIQZXWqpwq4ZTNGQk5gpDRgvbx9U5STz5pVJfFd57wM9XSP2t_sDFuhosgClRBldnKIT-hrMHDxBkowAQ2w751JWKG2YMfCcINjKoSODK7ixeUGrR9okqsKNfV2Iq3Kol2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74d4133ed.mp4?token=SkcyoEyhT3JA9GKVV10UJazegUwAUVrG2OeT8aPUWOhcyC2pyeyxSpbFZzu77hNyAwYEKBVHSHp3NVn3bMtodXo2RpeNE-0Wc8Nq8qw0k7lwYXdC_RZX1URxr50rxdbIJP4ozAdJfCxkHGFxQEugSCLBU_49VoHVr5U_APj1jIUVworGLQzYYz7cf3CY4vCEGAg4UtkhBf9TW8bHrKeIQZXWqpwq4ZTNGQk5gpDRgvbx9U5STz5pVJfFd57wM9XSP2t_sDFuhosgClRBldnKIT-hrMHDxBkowAQ2w751JWKG2YMfCcINjKoSODK7ixeUGrR9okqsKNfV2Iq3Kol2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کرمانشاه از میزان اعتماد خود به وعدۀ آمریکایی‌ها، و حمایت‌شان از نیروهای‌مسلح می‌گویند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/442431" target="_blank">📅 02:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60882735c8.mp4?token=WQUnKM0oSP3-gCbSADrFcmX8GRykLVA7aqhk6QXMq24Wp8kMT2wrXteG-r2uHi2wmxbfPzHlUFSaYDxUkGfKK0jnyYZmprJ7kBoDDXSVhxycOZyMak4ky8QcU13ayc-BbQFJjfkQvCgAJnnzMgAE0Om5SBg6_WR5irX8D_T772FpkoLHNjREPWKUX1momRZHClEv-qsGw8cIAEldVZ9e9Z24f3ZILoTh0f6VeWaAkq7POjQhB7Eyr9VvfRYAzrxdXYZOmZqC9B3NW_Uc_js3NcdI6knbEYBY7Dp9C2yObSux8dxOqoeGf1jCaxTNfbE1SAYQ8wKiAD9mmniXf51ieA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60882735c8.mp4?token=WQUnKM0oSP3-gCbSADrFcmX8GRykLVA7aqhk6QXMq24Wp8kMT2wrXteG-r2uHi2wmxbfPzHlUFSaYDxUkGfKK0jnyYZmprJ7kBoDDXSVhxycOZyMak4ky8QcU13ayc-BbQFJjfkQvCgAJnnzMgAE0Om5SBg6_WR5irX8D_T772FpkoLHNjREPWKUX1momRZHClEv-qsGw8cIAEldVZ9e9Z24f3ZILoTh0f6VeWaAkq7POjQhB7Eyr9VvfRYAzrxdXYZOmZqC9B3NW_Uc_js3NcdI6knbEYBY7Dp9C2yObSux8dxOqoeGf1jCaxTNfbE1SAYQ8wKiAD9mmniXf51ieA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول عربستان به اروگوئه توسط عبدالله الامری، در دقیقۀ چهل‌ویک
⚽️
عربستان ۱ - اروگوئه ۰
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/442430" target="_blank">📅 02:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442428">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b108c8df8.mp4?token=goCDVT5-FHhqs8lWS84HeH6dW8y6966a3KlJAkWWAO9GQFiRGSPlJ_U7tmzW63qNmWjeGzMQZnJkZeeeuC5kaN34qO0IdXTIrLbCkd8vEB4lksdQMdqLQjVfOY80gFON0_zEqZTExfDW-U790NQIO1xHQoYx8teugw2Fi-Sc-3JD9WO5a6RXY0uhPx1VMlBGoMKj-zn5AOWCO0JkE9W7HAJZPu8wcOSQkYJRX6oEGx4kDHCAMwg6uuU9eTJ0536AjWymQ1SSrQPM80hqBLVgK3zyRa5gFiALywmWxftEAOYmGGmOQKA1XCnlZTOvQrlyL9nP2IEuTlHAudsQ9pP5yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b108c8df8.mp4?token=goCDVT5-FHhqs8lWS84HeH6dW8y6966a3KlJAkWWAO9GQFiRGSPlJ_U7tmzW63qNmWjeGzMQZnJkZeeeuC5kaN34qO0IdXTIrLbCkd8vEB4lksdQMdqLQjVfOY80gFON0_zEqZTExfDW-U790NQIO1xHQoYx8teugw2Fi-Sc-3JD9WO5a6RXY0uhPx1VMlBGoMKj-zn5AOWCO0JkE9W7HAJZPu8wcOSQkYJRX6oEGx4kDHCAMwg6uuU9eTJ0536AjWymQ1SSrQPM80hqBLVgK3zyRa5gFiALywmWxftEAOYmGGmOQKA1XCnlZTOvQrlyL9nP2IEuTlHAudsQ9pP5yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از بی‌-۵۲ آمریکایی هیچ چیز باقی نماند
🔹
بمب‌افکن راهبردی B-52 آمریکا دقایقی پس از برخاستن از پایگاه هوایی ادواردز در کالیفرنیا سقوط کرد.
🔹
تصاویر منتشرشده از محل حادثه نشان می‌دهد این بمب‌افکن پس از سقوط به‌شدت منهدم شده و تقریباً چیزی از آن باقی نمانده…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/442428" target="_blank">📅 02:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuJRbSwoUR4jiKbRBqLtxEcdYs5AjVYPKiv_555stuEGc1MRAChxwAsLxdAc8_XEAFuj__BqoGxf5yrJdgcW3tkDs35a_yDm6ur8f2BkaxQv1DVs8TXWKcInsKlsOxq7uCMp5siwaYNbpW8DvoXYZ37mp05pVaB_FJ_rXxPzj4Y0MyIrh5UZr7cqvdGJOcFwshZab4F3aOvLHH0Psky4Aa1xTRP0oaDyXIKRteVUT-uu_I6iWSpzHEiSYzFiC9y2vSnxATV1jVAyF81ZGw_wJO0Fu3y-kBU97LPyCxPOZfy04tGIF1b_l4K3gGRXlP85edX_BCaRiSPhAuysdtzZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gn-HiXIAF3sMLJLj2aS5dqhynUvKYpEgcHqIo7st0QyfZpTeztFHmCLFfcmyfnUBrnoQGnvlz3i1i-romhCPU2RLAk3OppMtvenpKCLYN7uTuwx8eTgRb3HEnoOBSG5EUJpoaUt-O6fSX8VeukrbXiHPP0ueP0hJ1Zr6jSnWJrTiulWQhgeNvySH_55Vzx88VbmTo4yolMF-r4XP_qYrkKesTsaKdhNqsV6KvOZ9dpvTSpriHGW6eyQjjqFca0POepBfVqq-166HETh7xWmAvrfxWOaZbQCChhH_sM0Pl25gkbjNXhHORGCH4s3fDRatS2KN_l-IAGhcCGnz31JRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOorv3m7qHn3NIaoyq3DJG2Nm3qnCnoZv4NzTb8vstP4GpjRZmLBFGrHKXTam-KtR8yhlohkKf37XVZEL6tf1ITdwx6BfIY-jeRy_PAdS9z9CnN2-DKFCV8Cf7nqnU7EXZ-Bud1DzrUuRTYI0XjoKjGeHwgJ37qMTFR7KovuIvWDQWHtK1dc4QeFb5bXVcl4vmCI8u_a9KPYQIAh5PkU6nCB0T0QQG7a0DouPrziSCyfKIo2uFGChFLlitErLPYJOdeFdvIxWmttiEl-DRDx8x7oPr4HhXvSgHnMy4B6pyPGDlHT9lVc39kzdKRslT2TwnKcIg3shP5ZedzkvWh-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cFf3Eu81sjYyazqGlte-lebtyHVpcZ-3pdwkHdPhj92epS2nLVhw0vvU_3wLJOP85O-LqvOkD20iLuRyF4chXgP6IyFwVkOUfB0gnO86kOJNJXRZV9B4ZEfZH8DU5oDDpL1svpf_nVS3SbQlgt60ZTP0JHmkB8uNhA8rbPp-c2Pua5gi6fIGdZPsQ2x8kWZ5T2zm-XbkhR8TlZxKtYm9yRbh7IQWelyejupcckILnO-pebmZQS4ikjjU8cujeypH0EsajSl1zkziP0hO9al38Xd6iNOTzqFiigsXUbYT8pPmT6YwKI0I2XgikCLoF_Yew3WHS3U6L434DVDmrqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXZeuyoo4UfC9jHDLnZLSXn7EVThCzFnwDPxxkL48qIuLLOHcx3dF6j8pBZv851lJDG53OBsQ4B5aoBFCS-XXiuoB-VGUQkgTt6Y31M3L7u3UJc3hVLinpzG7xQwjXVvTXGb4t1MlDJD1Sc9FLSSlwnW9kvEAoYvlH7DdhUq9F9usXTb02Eht8LbSAuH5xsnatzWrBYsbWgnq8XmoHUB6mqmUqRMOOuc6-nhDf8hha0_6YoAzr8v-ZNAJnriLb9XhkmoIRgJYVV27J5hVPZgw4BXMxiEa7F3sC43byb4wNkH62RQKhHD5JMNVm34ci-3hECqSFKNyw0Q0Vxs80kNBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7dCon2VJbwhxQuZTLaNajsAj9RO9z7TngjRlKjIaLAhCLHSdutfw4l_CN7jf3JTJzK7rO3Bo309JlPU6mfM8S6MzESF4jLAOPBGPwwCBHPOpAwAD8VWbjrLWggkMco9xdnRXc-CqOPssE84n0Wub4FVS55vez89OtVDSxnvC71TCzL7rgvq5e2_b9cUJ1rX4k0a2EV1s5V5fbNxIwjrrPvlH0e4y-eoOCummWetm8f-R5Cg3p0zpMbEz48Sg-7l1mbJf18Kdggi5PRVQBr2RM3GhqBaolmWr0mJFNIHDhhC5lr7lwijTzcacrbs484MCriRs45QjOy_aVIa28uE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPg4ygaXvfoWARmzA3lNuJXZBokjCPhQGpSbQhFQirsUOseacXr9Gy7KXdTCVPUL7Tun-P1CCjUi7ZWIRK_sauZv7Qpzc1CIsVuW2eUMTE0rcMq5nCMOTPGu8TMBjkmSYxavYRN8KSIn8yJWbRgxn-qjJpdVSigdip64A0j6H2agTUxOtrKRA_4qDH2h8cDxP2BSc8eD1xQxFGvMn3gUNnr927MlzFTC_lbsAUZG4jhqbozkzaOMp_bBR3PiUMKG4B3N9LQKQj8uVpPctB5CZ81AuVgG7aANLMpw3Pxj3bD7CPO_hpMtiWy12otjm-9VxntomlEAen9lze7ni3vrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asb3mIZjrfeJGvBapWLGwWYdVZ49i0R0pxhXsFvZ2jHPRb2UjTrt3bSxy99oBPn87vt-42qtaemrX-X764LckSQLHRPDM7pGD6lIQSN83GQyMMqMy7ZPPTqGYooEhiOXXQ3UtQuAlDYQhDVB_AKndTXJokT87ie8DsIy3X5CcqTwG1awdSc41jrf4nxCAD9e1uAWox8Dn9BQKnuB0PgRYFagrYoKB45pblcPEeNL8-pODlsMxulu4capnGAYfhh3cgcJU-19-0SyszwNK1fxaezkQQqCcf0dnm8SJBlwxipezX1iGCwIfze5WkbyCEK0saVh5ym-SGuARfFblCsqvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حسینیۀ اعظم زنجان سیاه‌پوش محرم شد
عکاس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/442420" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پخش مسابقۀ ایران-نیوزلند در سینماهای تهران منتفی شد؟
🔹
در فاصلۀ چند ساعت مانده تا آغاز بازی تیم‌ملی فوتبال کشورمان مقابل نیوزلند در جام‌جهانی ۲۰۲۶، به‌نظر می‌رسد که باید پخش این مسابقه را در سالن‌های سینمای پایتخت، منتفی دانست.
🔹
کسب اطلاع فارس نشان می‌دهد که دفتر نظارت بر عرضه‌ونمایش فیلم با ارسال نامه‌ای به پلیس اماکن، درخواست کرده تا آن‌دسته از سینماهای پایتخت که شرایط پخش مسابقات جام‌جهانی ۲۰۲۶ را دارند، به این دفتر معرفی شوند اما تا این لحظه پاسخی دریافت نشده است.
🔹
از سوی دیگر، با توجه به استقرار تعداد قابل توجهی از سینماهای پایتخت در مجتمع‌های تجاری یا مراکز خرید، راه‌اندازی آنها در ساعت ۴ بامداد نزد سینماداران چندان آسان و مقرون‌به‌صرفه‌ نیست و مدیران سینماهای پایتخت، رغبتی برای پخش بازی‌ ایران و نیوزلند از خود نشان نداده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/442419" target="_blank">📅 01:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqOhuN5iNQUKXxd_6gC-Tgydh2UNfQ_xpODLa4udDfFQmtEifTfoFmwMi2t1C5GCfuMD99OFdg4pH6-iOSMn0kNxnng1wM0ok3cRPiDGUAJUMGxo_eos-8jwUY3UmGfs03zVU_WXJN_vqQOcWs_2kEZ2jl1WuPHBJT9ZVQPwhKKMUPqOl9zZVKAm7p_OMwYYCqdeYQO3EviBTa18v17KTlEdAUIPgvQEyjMZWGJ_nWiAd5lBRH_K77iUlwZBKtvqVfdrTmsUvLbC3vQy5uOHrfzBe-RI-vZMCWCYV4g0jobzYX7dYdQD1mwSko1sls_9YcMKUW6vdJgawg8uMkDUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
امسال قلب‌های ما حسینیۀ شماست
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/442418" target="_blank">📅 01:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ed854ebc.mp4?token=h1Rd3STa7uXHeg4K6baSO1k1Iy9LnMU0gBJvilDROZX8Hh9Wnuihu8BQc_yLRT_69CaOPBRyrrp_YeJFqXE7yiIpoWDA1A0znK2wvBOveRliQ4N-N6EEu8LXjFfIqYB4bkKBClBPYgWU5fCW-VjCjiEW70NjMij4FU6Z7GEfU-jTEcj8OieytRvx62A4QWYCdFb1GyCIAquVMe4gjAiDM58oKH9Rt58B-Ub_NueAhN5AGWJgfvmhAK-BnlUbA_sYGPX34513IM2OxyaodSYYnL2tq4Rm411mEHXOIq6hAG8NYwmStZlSNEGUutczJqHtSk3whFZ0y6LNazzFvg_18A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ed854ebc.mp4?token=h1Rd3STa7uXHeg4K6baSO1k1Iy9LnMU0gBJvilDROZX8Hh9Wnuihu8BQc_yLRT_69CaOPBRyrrp_YeJFqXE7yiIpoWDA1A0znK2wvBOveRliQ4N-N6EEu8LXjFfIqYB4bkKBClBPYgWU5fCW-VjCjiEW70NjMij4FU6Z7GEfU-jTEcj8OieytRvx62A4QWYCdFb1GyCIAquVMe4gjAiDM58oKH9Rt58B-Ub_NueAhN5AGWJgfvmhAK-BnlUbA_sYGPX34513IM2OxyaodSYYnL2tq4Rm411mEHXOIq6hAG8NYwmStZlSNEGUutczJqHtSk3whFZ0y6LNazzFvg_18A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از استادیوم سوفای در لس‌آنجلس، محل برگزاری بازی ایران-نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/442417" target="_blank">📅 01:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
حاج اکبر مولایی پیرغلام اهل‌بیت(ع) درگذشت
🔹
وی در سال‌های اخیر در هیئات پرمخاطب تهران به‌عنوان پیش‌منبرخوان برای اهل‌بیت(ع) نفس می‌زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/442416" target="_blank">📅 01:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
خلاصۀ دیدار مصر و بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/442415" target="_blank">📅 00:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVPtufc-gLtnwl0nsByFmsISLPdR2P2F0-1MW_5CRJd9SDLyqpxpvsLYz0p6qiB36BBLHy1Sam1qGm4L8l5ddt_gishLQ2JUI78H-vyxmokk51kGyP3a2r7U03j7zA2psadVyq1CH9vwRXO0KNTuvKUroSux657zD3EJfJifLWDARvJ3axfJ44hkjMkyBP63pL68l2eLS1MHItGIhPKZMu1zSr7sviYdCUCweFW4G1ZvzGzXFQ7Hd8CXDT2ZQCcKCuvtAj9hWFUNKSC8kvgD4jXlAQa60gtITu5dvFg7YeKW9LutsfQrcZ01eY0fb9e5RAj5EzbipfZv-tfJHTQu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjLHTAGu8o4PG4mDDmYMHzg__SC4EjVjVrYWjVaIlVOp3r6qM_zcanUNTK-JsYTGvFK1awTlaGjs7YoDkFuWXMIDfOXwKWoJnIG_rK-Zi9CmNKb8WYCAiFewP6vaRPxAKVsww4LPEaUxSU_lPeL7DtGBvRCMdad-c-mGscvk0xhn4eH57iS6o9OQzm4hNbH9hKb04muD842B9v3JhvbYjUzM8wXRayIf_cuOJPjbhoS1txH2QHCu599OEYLAoInHtHW3rSPl1mRClzVc-eboK6KP6pGGJiDa9aVjfOc_zxU_kx7e4y4nDRNwAwQfI10n6Nddmr-jv4d-BtIn0jOJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX6EOBxABgtYuWLcKz6B6dG20I46KWmHtuAEtb_atA6ZfqiFyvuelHDRgUxlblgHHsxUxpQxJ6k_FtzE8eq4Vdfw_Q6V5abFyfHaftCOfekUqsDfGX2VRwNDgUhubp2zLz-y6g4jF9xIAoSgIYLkqumEg0ASRvdxce0hu6Lvqsi5SXYNgCDtOIiudlA4kIsafACyig_M9EOM7ZT3iA0MfQxRIHhRMV1rB51ooPZfLJ30xz2MqYnaRqdthDyTB8_G_S4mPI_q6xngyuRVrwKKH1t361sWAYpqKlfsnkQRrkqc0V6rNBLJob57iU0_VGYXYD1ur_9SJGa-ZJcbMwY_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgOdSxZGc3sAy0GZERLprI9YjPMeVCoG18hyOMUJ_QzqNmDFmTqQ5qv7R7oFpEB33uhqZlDK0whCHYvfYspiiyOe1rwOTQJd43m07dba0EBCLdmCJaDRTs6dayKWs_lt61flwxuz6uZfJGvgeOd5mXzYyvfdZkIFAN9kR3M9B2GNCnHoxeuOez6_34NPThUozEqH5rHkCxWUctsdxkoPRBbiPsiKHqP-Ld12ilN_cnB1jAbQaqs5yVZ3vjcNzExEN_W-87nABMyT41jZ4qAPpYuypsEgAnErCQucGO0Bj31Rz9wGmBD2E-WCXyqgEOMgFC6c7k0lmabqXo2SprNtYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۶ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/442411" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442401">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rg5U-arzMZSWrn28Z6x2qanTSpNKUPhbANvrqKzpPKsqGUiPC3fXMWq6RHdLu2X9rCvqvVFZq1Nw6NokMiwx-hy6yl7B1nwBGiT2wBec8Jm3QcIceykL1j7h45i686HO7yKh-9SPWeM-V-ow_5I0zTLFgnA-VbkwnHSB_uDUhePTI1CpcUjQ2DP6uFxxe0O7gXIUjlY8AYMuSFvNspZl5F1D5FqSKgmiLM___h94GBCwGPP1lXdpAkNMZe1h3K6chWhqyqDto3i4wfWLigR-TgguMYGxxc1VGPAdLZycVB4gptB-a13tfS5uSRhEtT1iu_FTEMZJlFT_i3peor5hpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZ1HwB7y4BTovZsMXGRi8-TSMzvEloezPqFobI8eqmZwKKbF3WB2eQ9OEqteUoUkDAz0b9QmC4R9iPreFsYvPT4eE7LZHlNgTkvjc1GHW7BnA_aj_ikpnVdkC5imgsyYgTBYYVmI9J_gPbw5a4OdTfomzg96RU9sr5icemWEzIywjl_K6GzgqjQxLYLTA5WrYKxoLccH213hA4o09QP3kgMZUZftoTuFaKMH1b4pruAGrkqzWbOVxcjorHkq7K3QVAaFRPbweQUmO8FmJ56-aSSoHBkfeh-hnBxM32MpmATquphakgtu19Fv7PZ0aySWtZgUcsotd-JGW-HJN3QNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzgpv5cbgOKNwuORrBa98fXQqjbsz6cIEgRvxgEr_EalarlLCgTw0S32Gu1lv6hJrSmlQAOFYONXwqFBJFIZ0XmmmsZsG4ACl1nFO256SGaZpVTtI3HICbUzd35_4eFAz_2xdMu2KczKDRYelOv58gfLKjlibIckc8QjzK2E8qeUizle14NoTwaDh3Bj4MTQi-VN6q5iSsqcO02GjHcTrfXwK_BSd3uYXTVDhsO2jsLue1eXUSMNQkcGlxVb26M_yxkUaiMT2TCAlGFMHzGWeKCdYvt1tUiwAfYpVFY-sQOHJjP6AizbbvM9nJoOPSUj8xudC3DrnQYNKzAzdD4GmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bikBLWQQll9jMMSvsjIn35HwWwFmMs70je7NZZJsq-k_oYhQ5Ttnaanh4o5avFiTOZberlcePqd559MPMYouIFIQngeklFrZhn-Af-3RO7PptitTf5pf_Y1u1oKgBgO0PVGhGtJsYiM2xjXYglR7fSKvP3LwatG7jhm8Dh7HYNE1Pph1dd9ze270dNcXTytWOD23pMv0GvZFTFaJVkrVe9EnbHt54orbOGbTfOcfbhDCNbPYOSLmwjJEwtgrVDS955WI3encwrAvB2N2196CZ1raaJd1nMIs7DeSYtH1xmDeB4S19T6QldTS8C6djLBoAy8SXVqxtOmLoYS6csq73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmJTa3C7FQq9Parz1tGZr6chDzii7V-kRV3fMiYb9Gm9BfU5X73sVlRc1E7vYeUgZPEkWs8JaTFG4gHxP0fYxma2VXLb82grU6sJfC1JAaTsOOEOJLoz9pCXGjti0ZS1Ggt2EzsUqFbCuXH4G4J7kUX5RWw4sinh9MApRva7kyoaFlS835c-FcLsbWB4W76njcvFPPm9iS-1Kpze9Bvpa53qNNIJZOIslPX8FanplwseM3E6A-tT59dfo9gyh_4Jf5c0vO7oXce0tzPoJ4FERNZMZDvrZ4PK1yuYFxEtqVaNXa-CkYwFCMzjWOhmPXj0nLHJEsIsmE-amowtxak4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne6HKYVO-ElA8jv04QhN1Yic3m-0DybR7TFv6fDH3_RkJVuu9fhMhYD3M6-GbynGyz2NeQxDJdjFLeRpS5dblxPA5MWvEUKx3S9XQNCmBNf3fMNFOLyU784v6Jxt4r9qOA6j15yBEfJLZPyBe1RH5g2oMGuYFIt2xTYOc8Z8Xsk3No29WxrG8xeDQHIQQ5J6N5YwIWPidAyoscYA15HPAaIUHSnQ60RHR8sjigrgVJXNSWmKs-Bnp4YC-HOHJelAyw08K99QYbFXLKwqR0Ag1q-aX4_Fc48slxMX0UjWNqeUNoN__d7cpZp2QOA-Iq_2uRjLVN8_N3mGGqK9O2aFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHyCCByubG80RNnVWodEdvAvEe94GK5zwjxGeaCYxBpwYzAj_l_oom9k3INanoG-PvTHrK4XcC8IBQ1kf4krRAkKH8MHmwQKHJM42YYLfm3uV9vf55XYhCDIp-mCyuZKWBQAUv2g5PFNYRWG1tB4lBhB2FtpcyM6RcN60K85AO7xXOqJ_KIvGKcyR0IczuvrxiRe6tPSk76_Znsp_LLRg-LinMgjfPHgXCq7jq91qLJGRvf0lj25jHstbGTF1PReTegySfYmQLKc_AJoizb8Q7oPnySCcK81x59NX_nWIBsi7MyNgV2NXWTgOLajUinX8p3efhiZTr8vyr6uSXW0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgveZ8qjYH054Jm3kv5n-gDAZqxx9UPBFD7YmqQKi1ngrch_AMYDUpvUnaT4AjzWXjq48X-IAsKpSZTiL5lYPGS4Dn6Qv7gFcu6PqQ2OUtqffZH2CMPXqkGS8ggtUhwIrpxA25Hs0uFC6c9KVoFkyVPDDGu05saCkIvRIpji3h3JptApxVQRmS9AnwrWISbdiKSk_5nNfMW5dXRDX1vlrwIvePKOh_Io8biS5gZTRczCQYXfKqREwshZs2s2TMHQJcRldaluTJK0icuQV8MyTl8q_TGrNUeuWyTRT1NtwykFKL__eHpiX4K6peaRcWU5P0LaQevTcCQA37rTtZy3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksX6L1_lzDSnZl-BOb_fS-LQSmcCbCGR8v6tAXRWDNxIrbwqeyJRKBNII5qfRXzs3xfonzAv_ZZ9QKf0qG5637h6LrZHPE6ZJ3KSjkeqzSFuZmcLcbXAyjd3rPemDOGs4Rm6LU0eBHOJRsD0uxQAfWq4KGowz4wHT-sVmqrVETwfx7sRUK-Lq5VQwJtFvEg6SKYl1DFj_Fqq5WYPPDBSXCAS4yIfBOQtDxKWyv9TEA-RXwo97MZLzGjEOPuFvlcZg_DvxHF4F_a7-tVdq2_ce4sVEIPGlb3HiwuFoleHfqCJbG5bIgLosTCipQ-zr60jIxrv6K73lX8nNUcBXMtj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-_S3LQ0ptvazdGj4E6xtBj-KvrA4qNr1M50lMM1z1Iu-RyUIsuPuJZ0gZbMGe-2S1u4C2lwZHZdCJ4qAQFtTR-7dYachpsAJD9JJHulLUkO8I6_9cj9esHmzpxnW81DFjDXrx6zpYp15neH2uie77EaZc-FaZMOZilS2nBBZZ8vCyBfyc3t9Aa49p4jkI5jl2ic4uu7OcsGunqje9-0jLQ25CUx7oYziysd7Cjlh53RW2LOQ21J0-okbN58kIB6IHO0Rt-WKdYJHo3M4cJUweE8rrQeE_dGSu1h5Rwi6A3-JbMqJ1vR2Pgt0xrzp7PVD3q7x0LZ_dJgJXIRdasvBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/442401" target="_blank">📅 00:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G47oHqLrtMCeHhZ8_8ESn9L3wNLu4yO-3AY_sTvp22CRScGzLemRWjwFLqMk5Q1Y0gz8A3ERoj_7_l3H7RbmYhk0OdbqejWZMSp_PKTb2pdvkLzBjqTA3jiH5_s6oCZSUP1tk73d0gtjRpYAu3gPegMTsB-GM44czeLN7Z2bkZcbxL_x5EwSpFA3zvh3AD0l_Sf146tqc63rF6LJfd0x5A4p7iicyh0siYqNrorqm9MIb4TzHJ1mB8ZACCyZWArAPnm0QCzm4ztlZC6FIPzM4qIgBpAzWfOie9ja1xj97SNP_baGy0R3PmLucaB-tRA5YLaGa46o9S8_QHeVBiSyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی مصر و بلژیک؛ نتیجه‌ای که به سود ایران شد
⚽️
مصر ۱ - ۱ بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/442400" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5187626b6.mp4?token=Rlc6-fGDtHXDE77yTsP-O6kNuWJHGJT6r5Qde3Hy7XuaAH9_5ivB4p9OdsuZUyQ9Ao3_QWygyW6IxjC6v1b3p5Ije9znswgcRe5vcWQrb4H0RlIW20cg2dq76m6tl3t3w2ujR_f43xfkvN2Di05qCi_4rlAbm7Hhk0JupVNxgulWKj66KkP7GKblo1cbD86BNCMomONY008FXoPfJgev9QELpBHrPhn93-DrIGXq-lNvOEhsZvehl7SKtky4FO9slltlvN4mecw8BgcB3oJQp-j3IW04Vcbkz1Y4c82SQad3HyiRIPCdWlnwqgC95t2L9CQQLDdoh1d9kXkNLhkxAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5187626b6.mp4?token=Rlc6-fGDtHXDE77yTsP-O6kNuWJHGJT6r5Qde3Hy7XuaAH9_5ivB4p9OdsuZUyQ9Ao3_QWygyW6IxjC6v1b3p5Ije9znswgcRe5vcWQrb4H0RlIW20cg2dq76m6tl3t3w2ujR_f43xfkvN2Di05qCi_4rlAbm7Hhk0JupVNxgulWKj66KkP7GKblo1cbD86BNCMomONY008FXoPfJgev9QELpBHrPhn93-DrIGXq-lNvOEhsZvehl7SKtky4FO9slltlvN4mecw8BgcB3oJQp-j3IW04Vcbkz1Y4c82SQad3HyiRIPCdWlnwqgC95t2L9CQQLDdoh1d9kXkNLhkxAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دو مهار متوالی تماشایی توسط مصطفی شوبیر، گلر مصر که مانع گل دوم بلژیک شد
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/442399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/442398" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
مرگ معاويه، به‌ خلافت‌ رسيدن يزيد و خروج امام حسين(ع) از مدينه
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/442398" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
سردار قاآنی: باب‌المندب مثل موم در دستان مقاومت است
🔹
باب‌المندب فقط یکی از نقاط استراتژیک در دست مقاومت است و جاهای دیگر هم هستند که اگر لازم باشد فعال می‌شوند. @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/442397" target="_blank">📅 00:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پایان محاصرۀ دریایی آمریکا، با عبور کشتی‌های ایرانی
🔹
دقایقی پیش چند کشتی ایرانی نسبت به تردد بدون مشکل از خط محاصره اقدام کردند.
🔹
طبق اطلاعات ناوبری کشتی، یک نفتکش ایرانی VLCC از آب‌های آزاد به‌سمت بنادر ایران در حرکت است و از منطقۀ محاصره گذشته، همچنین یک کشتی حامل نهاده‌های دامی‌ نیز با گذر از منطقۀ محاصره به‌سمت کشور در حرکت است.
🔹
یک نفتکش پر از نفت ایرانی نیز با عبور از دریای عمان و خط محاصره به‌سمت مقصد صادراتی خود حرکت کرده است.
🔸
روز گذشته، ترامپ در پی پذیرش شروط ایران به‌منظور توافق آتش‌بس، دستور لغو محاصرۀ دریایی را اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442396" target="_blank">📅 00:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1558868203.mp4?token=ms3PPCb2JetOgtIHUIWfU7PQHEarFCOEB-J3wd_6SUSZFbkmi2Wq8HjJEXs95BCUjzYphQrK1nOjbmN83ZsL_mexMvdpXwwJYQvas-JO1vOPJ_EF9nu_2Umf_9dMI-WCzsRRpMRa1FfW--vZwx-a_QuWYUWISOQ_ZghVmnCIAtX0OQ6onGO7ttdWydAez70F_2lWgg-u0f_Ty5xiFZx1vCXtxKgtl3SwwlzgTzBDh6SdU0qzsN_mvm4MfsFSklKmAQHz4n-fPc-YMIWE_4X2K5es_iFooDysHh44CDDNZWbfJF74v1S-TiNkZHAR29HEWfBg8STmFDum4WmKhisSO1nS9Foql1DYOZeRX9ApYsIj0_p7pqtu3HY-ZXW41OGgTRxgPjD7-gX-K3lDW_65sdcJqE9YkOjtkkINQq-9_6ayIOg3hno75XfM3SDPKn2uH5a-i-LBWgSwltgtM3JUz00dea5GfVtG9kyg-JaypxzTgd9Ld_BKkGwWQS6f9WbxOmKyxEspFFsmNVvfooiGIy8qDflSMejCr8EqluKWX09qyuaNZ2WLpPxZnHvEo44GCIbg0zh67I5K-jKXW0VWcFbQD7MtXrz9aLUXRcQmUJBC2KDr2D-Q-qIkE--PT4FOYvYs5EmVjvQ7V48UEQ9YEx1-SvVxpe6aTx8agpFrAnk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1558868203.mp4?token=ms3PPCb2JetOgtIHUIWfU7PQHEarFCOEB-J3wd_6SUSZFbkmi2Wq8HjJEXs95BCUjzYphQrK1nOjbmN83ZsL_mexMvdpXwwJYQvas-JO1vOPJ_EF9nu_2Umf_9dMI-WCzsRRpMRa1FfW--vZwx-a_QuWYUWISOQ_ZghVmnCIAtX0OQ6onGO7ttdWydAez70F_2lWgg-u0f_Ty5xiFZx1vCXtxKgtl3SwwlzgTzBDh6SdU0qzsN_mvm4MfsFSklKmAQHz4n-fPc-YMIWE_4X2K5es_iFooDysHh44CDDNZWbfJF74v1S-TiNkZHAR29HEWfBg8STmFDum4WmKhisSO1nS9Foql1DYOZeRX9ApYsIj0_p7pqtu3HY-ZXW41OGgTRxgPjD7-gX-K3lDW_65sdcJqE9YkOjtkkINQq-9_6ayIOg3hno75XfM3SDPKn2uH5a-i-LBWgSwltgtM3JUz00dea5GfVtG9kyg-JaypxzTgd9Ld_BKkGwWQS6f9WbxOmKyxEspFFsmNVvfooiGIy8qDflSMejCr8EqluKWX09qyuaNZ2WLpPxZnHvEo44GCIbg0zh67I5K-jKXW0VWcFbQD7MtXrz9aLUXRcQmUJBC2KDr2D-Q-qIkE--PT4FOYvYs5EmVjvQ7V48UEQ9YEx1-SvVxpe6aTx8agpFrAnk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سردار قاآنی: هیئت مذاکره‌کننده ایران به محض تجاوز رژیم صهیونی به لبنان با اقتدار با دشمن و واسطه‌ها برخورد کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/442395" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
سردار قاآنی: بدون اینکه ایران یک کلمه درخواستی داشته باشد، نیروهای مقاومت در جنگ اخیر با ایران همراهی کردند
🔹
تمام برادران ما در مقاومت از مدت‌ها قبل همه‌شان می‌گفتند در نبرد با آمریکا ما باید پیش‌قدم باشیم و نگذاریم به ایران آسیبی برید. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442394" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
سردار قاآنی: بدون اینکه ایران یک کلمه درخواستی داشته باشد، نیروهای مقاومت در جنگ اخیر با ایران همراهی کردند
🔹
تمام برادران ما در مقاومت از مدت‌ها قبل همه‌شان می‌گفتند در نبرد با آمریکا ما باید پیش‌قدم باشیم و نگذاریم به ایران آسیبی برید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442393" target="_blank">📅 23:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac486f2dd.mp4?token=gxXzQf25oep3IYzZ0RqaFBXypWVCgLey0N7TGxbfassxQ9D_RJvV8ovh4iTTcxJ7oe1dmEiT1abYDupXX9WKWhGH6djzBQx6YDNLMA8Gs6UDF5cWVmaNfuFTnxJe3QL0YSL8vszjRmNDT-Xtd3TpXTEfy8BqCjLDPNXfv5eGeDRNE1ope_yC1fBmGc8o-_PJGp2Z6HQxfLrqTglJgE5kcKiK-HHF-p6_kR-2tpvarwzB9OuEwW_OSGZAi-lhnEL3zNjgdCk_hU3h57oGA4xrZ59nYwCUNcyTnFvHpE19l2qUX6AuXp38t_-Lu83GhrZpf8ItEPAGc20E_ZeIRJEA8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac486f2dd.mp4?token=gxXzQf25oep3IYzZ0RqaFBXypWVCgLey0N7TGxbfassxQ9D_RJvV8ovh4iTTcxJ7oe1dmEiT1abYDupXX9WKWhGH6djzBQx6YDNLMA8Gs6UDF5cWVmaNfuFTnxJe3QL0YSL8vszjRmNDT-Xtd3TpXTEfy8BqCjLDPNXfv5eGeDRNE1ope_yC1fBmGc8o-_PJGp2Z6HQxfLrqTglJgE5kcKiK-HHF-p6_kR-2tpvarwzB9OuEwW_OSGZAi-lhnEL3zNjgdCk_hU3h57oGA4xrZ59nYwCUNcyTnFvHpE19l2qUX6AuXp38t_-Lu83GhrZpf8ItEPAGc20E_ZeIRJEA8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پس خون رهبر شهید چه می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442392" target="_blank">📅 23:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e5d07062e.mp4?token=NLHdqfNJ-FL8UpiCH7-FALjbf4opOE8II_nTso35LJbNOcJ6iVqKrwYWosksl_plk8brwLMr3qAZhimC5gDYao0IFkvYLNfIPQ4gCNPOD6raDsQGKqQS3jXIR2P_Rvx0mXgapYI92GEll9cm-OTs9SFs5AfZmZ7dtBz1D7Bh3ZCAnL7cLfbkWuQAv3wIK71Ackuu2xp75zL0inckWbKb_7sqh-8JW0OcZkCev-URP-kgj2i9MoG0CUIeDekEaDndI8b_3GMhwJT0woRyV7DfjIP8iDgWFO3rUaLQc8IEEbaDooKDTvCsV3Se10pzyoU0qjMn5u-RtMLStbMyh_h1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e5d07062e.mp4?token=NLHdqfNJ-FL8UpiCH7-FALjbf4opOE8II_nTso35LJbNOcJ6iVqKrwYWosksl_plk8brwLMr3qAZhimC5gDYao0IFkvYLNfIPQ4gCNPOD6raDsQGKqQS3jXIR2P_Rvx0mXgapYI92GEll9cm-OTs9SFs5AfZmZ7dtBz1D7Bh3ZCAnL7cLfbkWuQAv3wIK71Ackuu2xp75zL0inckWbKb_7sqh-8JW0OcZkCev-URP-kgj2i9MoG0CUIeDekEaDndI8b_3GMhwJT0woRyV7DfjIP8iDgWFO3rUaLQc8IEEbaDooKDTvCsV3Se10pzyoU0qjMn5u-RtMLStbMyh_h1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ما در میانهٔ جنگیم و به‌هیچ‌وجه کسی نباید فکر کند که جنگ تمام شده؛ جنگ یک توقفی دارد و آمریکا و اسرائیل دنبال تکمیل بانک اطلاعاتی‌ خود و مهیاکردن دیگر آورده‌هایشان هستند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442391" target="_blank">📅 23:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442390">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abc7b4f64.mp4?token=OubwiZd3yWjK37Ui7rRheg1VGT0kRDHti7gSn9RJWJQKvZeyoPq8MrVbVeDRJQUFQFvcU3dZRH_X_CWOBsKBtZRyRhkL6fQkgyhH-HfiwUoAPcFFYKgMBXqzeZq0aWAu_yXg4wV1ku1vSx1mY5vVjaieRdVhWvXbPoYtzalqxDzab56G7iPPy9qO-JmqpfktfAc5PqCXC5Xfqf6Wb7Hitp5kwt9_txF_TLRaovO0yjTo34-M-3XI-JSHqHIpToEMKHWHrps6RCjTI4NAduWTd6JBhPXsfG4c9919FRX_0MG37J5FBGiHCANJ2CwvtdUPT7wnikxhcLJxd7CGydKwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abc7b4f64.mp4?token=OubwiZd3yWjK37Ui7rRheg1VGT0kRDHti7gSn9RJWJQKvZeyoPq8MrVbVeDRJQUFQFvcU3dZRH_X_CWOBsKBtZRyRhkL6fQkgyhH-HfiwUoAPcFFYKgMBXqzeZq0aWAu_yXg4wV1ku1vSx1mY5vVjaieRdVhWvXbPoYtzalqxDzab56G7iPPy9qO-JmqpfktfAc5PqCXC5Xfqf6Wb7Hitp5kwt9_txF_TLRaovO0yjTo34-M-3XI-JSHqHIpToEMKHWHrps6RCjTI4NAduWTd6JBhPXsfG4c9919FRX_0MG37J5FBGiHCANJ2CwvtdUPT7wnikxhcLJxd7CGydKwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن B-52 آمریکا سقوط کرد
🔹
منابع خبری بین‌المللی گزارش داده‌اند یک فروند هواپیمای بمب‌افکن B-52  متعلق به نیروی هوایی آمریکا به فاصله کوتاهی بعد از برخاستن از پایگاه هوایی «ادواردز» سقوط کرده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442390" target="_blank">📅 23:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442389">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
زاکانی: اتهام‌زنی به مردم در خیابان و مذاکره‌کنندگان خیلی بد است
🔹
سطح امتیازگیری ما در مذاکرهٔ فعلی «میانه رو به بالا» است. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442389" target="_blank">📅 23:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442388">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4IeR67hz869a-9bqoOTFC4OBf1sEaAkrcl2nBBWcK5dpDCcBOWmmVERngqI400W5dwC0QMvIOWKtoue5Q3tqTBNCZDnoggTkMxjplimfw3nK8GsgxzY6suPsa6ERD9wblmGw08VbI2eHc0ERIDGs7M3sJbDDONszv-hBnrOl5Ge-YwfYfoybLQX-PerpJKaCiQpWCQZ0_sGYn8ODu4X4LeBIDMHh-RiDTAGuvxzI5pybHaUw9lgp286ITpJc7a1adn-kfpufAspQDVGq1deLVj4xeT1U-hPcowWOFz8O0wrhwzcKODTVLIOwsxWkuPZshj40048iDhaxngQO6Cn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه ترامپ برای تکرار سناریوی اوباما در یادداشت تفاهم
🔹
اظهارات دونالد ترامپ و مقام‌های دولت او نشان می‌دهد مقام‌های کاخ سفید به دنبال زمینه‌چینی برای نقض عهد در اجرای یادداشت تفاهم حاصل‌شده با ایران هستند.
🔹
در ساعت‌های گذشته ترامپ و معاونش جی دی ونس و همچنین یک مقام ناشناس آمریکایی اظهاراتی درباره تفاهم‌نامه مطرح کرده‌اند که خطوط روایی کاملاً مشترکی را دنبال می‌کند.
🔹
محور کلی سخنان این مقام‌ها را دو موضوع تشکیل می‌دهد: نخست اینکه ذیل یادداشت تفاهم حاصل‌شده منعی برای برخورداری ایران از امتیازاتی نظیر رفع تحریم یا تشکیل صندوق بازسازی وجود ندارد اما دوم اینکه، این امتیازات تنها در صورتی حاصل خواهند شد که ایران به گونه خاصی رفتار کند.
🔹
این الگو البته چندان ناآشنا نیست و مشابه همان رفتاری است که مقام‌های دولت «باراک اوباما»، رئیس‌جمهور اسبق آمریکا بلافاصله بعد از حصول توافق هسته‌ای برجام در پیش گرفتند.
🔸
ادامه این گزارش را
در اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442388" target="_blank">📅 23:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442387">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdaff8d552.mp4?token=PTxrntes3px_pW8_1ZGt7nAU3qQUCC2ajS2hO8U_Tw05Ms2lBjf9BaBh7NhPAtcl2K7ErE58PHzvL9YwALeyKZnYMMK4RywBS6Nt6uI9Ci2n4CJ2egEcx_aWzYS7xOc3kFr3hwDnTX1_Q1z4sHkzCgRHZN41DlQ5BK0HfpMNSlaGLvf2YioNmg3ji4d2JPh1WHbqeqt36aAnEZ_ggaVHNkNoyYdI6NhoGe-Ng071PpW01LMU0qmFjMofa6KjwDfVH6V5zcYl7RjNlzICTxb8i97MiPZk9gCXZG5dWtZ4uP_WWJgpuZwF9ta6ZUAkOY2IwXlbNEbjLK5SqjxRB9qTsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdaff8d552.mp4?token=PTxrntes3px_pW8_1ZGt7nAU3qQUCC2ajS2hO8U_Tw05Ms2lBjf9BaBh7NhPAtcl2K7ErE58PHzvL9YwALeyKZnYMMK4RywBS6Nt6uI9Ci2n4CJ2egEcx_aWzYS7xOc3kFr3hwDnTX1_Q1z4sHkzCgRHZN41DlQ5BK0HfpMNSlaGLvf2YioNmg3ji4d2JPh1WHbqeqt36aAnEZ_ggaVHNkNoyYdI6NhoGe-Ng071PpW01LMU0qmFjMofa6KjwDfVH6V5zcYl7RjNlzICTxb8i97MiPZk9gCXZG5dWtZ4uP_WWJgpuZwF9ta6ZUAkOY2IwXlbNEbjLK5SqjxRB9qTsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ما نباید فقط با آمریکا مذاکره کنیم؛ باید با چین و روسیه و کشورهای دیگر هم مذاکره داشته باشیم و نقش خودمان را در جهان آینده ترسیم کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/442387" target="_blank">📅 23:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442386">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h28I0nJt02vOtat_ud9xzfIdulD1u0Y2QUwfXHh-T1na8UD6ldSsjn-AML8enKh41S1Aa7pbFbYoxpoVyEYsuzEx0QvnnNOMuRnLzS9KOpYboKJxlhuI7fMhLQN4h1hKswFUTBWtHofpjdKLzgUrlqGJSdJ9aqTRoAfHiDldpxH73WletKqfRdZ7IJbdc9YZquBm49KVc5mAtgMtzBGpTwW8JIY8s2mHeNi_6mbA9-mNMoKbD2kk62pIFSweDhuZdQM3mL7SKhTYEaCUOjL3KvXr_uw9VzkJK7M-cA-gZLfkkPEie_c515ghtPhgo64XfuH4IxhEnTDYCV5Uosqurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید سپهبد باقری در دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/442386" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442385">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a39f0be2.mp4?token=TJYbS3-csafN2S-rh8QCEUbgKKg-ncKww8RoKrMQmBMWKtMa2XKKHxq85pl4vbBRuiaiLpY-83uy6egPQA4EZZT3MNjy9urajL-UtAb4CZ3UCRquw6IC3-RAktCXS202LF2tVbrXAjEtNsZjfEBKOdRIRxzN9dhRmv5bSiVD8T2ShDb4F2-y7EcBjwnOWHKb8UJPi8qq5psMCyNU3DqfNXorm_5DL-4Tu2mJRNt-DekAG7XqOrBvH-3MWI9S_clgLmV1YpRRzezKTWK9zHF7Vokya-a62YowIepkXejZu3S1bivP3iXgBmYJQDOMaPdDkBCzODncFstEmMoMmBKL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a39f0be2.mp4?token=TJYbS3-csafN2S-rh8QCEUbgKKg-ncKww8RoKrMQmBMWKtMa2XKKHxq85pl4vbBRuiaiLpY-83uy6egPQA4EZZT3MNjy9urajL-UtAb4CZ3UCRquw6IC3-RAktCXS202LF2tVbrXAjEtNsZjfEBKOdRIRxzN9dhRmv5bSiVD8T2ShDb4F2-y7EcBjwnOWHKb8UJPi8qq5psMCyNU3DqfNXorm_5DL-4Tu2mJRNt-DekAG7XqOrBvH-3MWI9S_clgLmV1YpRRzezKTWK9zHF7Vokya-a62YowIepkXejZu3S1bivP3iXgBmYJQDOMaPdDkBCzODncFstEmMoMmBKL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد!
🔹
روس‌ها به ایران گفته‌اند باور نمی‌کردیم شما اینقدر قابلیت داشته باشید. @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/442385" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442384">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a1ced860.mp4?token=m1teiXsWXecKv_x4qHbCW1czeKczvMlJTKvEhk_kdYJBXDXA2BOWiaPp-z71ZCfrXkITWEXmpeTWww-snIBLxhceI6pzlpcShdzMii0DK5TIfm5mtFKfFzjZ2qqbY7EzVtnV029HioeW6A9g4pEsyQMaP328C90xTEwQ0zuxSiEAtr8GAmxL-iGzKFb7ibrCHWfXLKI16jAPUmWw1UrkhNeIr2YTU2IofQX1oX72MgbTfrouXFeivw4hxtCaH0no--AqoivnGaRlvPCdYpkhWYI8SKXqvBs8-So37qULUnx-MmFTAzbBjG6H_TwKd_RxF_FH-XL4xOfZDPe01BtHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a1ced860.mp4?token=m1teiXsWXecKv_x4qHbCW1czeKczvMlJTKvEhk_kdYJBXDXA2BOWiaPp-z71ZCfrXkITWEXmpeTWww-snIBLxhceI6pzlpcShdzMii0DK5TIfm5mtFKfFzjZ2qqbY7EzVtnV029HioeW6A9g4pEsyQMaP328C90xTEwQ0zuxSiEAtr8GAmxL-iGzKFb7ibrCHWfXLKI16jAPUmWw1UrkhNeIr2YTU2IofQX1oX72MgbTfrouXFeivw4hxtCaH0no--AqoivnGaRlvPCdYpkhWYI8SKXqvBs8-So37qULUnx-MmFTAzbBjG6H_TwKd_RxF_FH-XL4xOfZDPe01BtHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهد در ۱۰۷ شب حضور مردمی سیاه‌پوش سیدالشهدا(ع) شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/442384" target="_blank">📅 23:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442383">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7342d0d8c1.mp4?token=GiwqK0DN5I0edfPGnqP1PWjk60HNpeJtORiQ17aCdezUk1Z3WDoQ-a6a27ozkDwv4aKdOJi156n5hSFPtg1Nj_f0oQ5BbZ4kljT4d-0sF3FoBdj-wnyAFBOP0FilR0ZJ07tvY2iQ58EavRm5899yhBjKh8_3Dt5xOgHNlK12BPkPGFVDkihHIXfmEFpNeluOSV6fkYCz3fSw29Xy5veD8KCeCBy7hQJj30cITgAGceRuIUQ_MxLvtJmxAEILYa0vCpN8DeC5wbUT8RH5JMfSkQu1dnkZgt3SZjdUKNVrh1Jn3IPcW0rE66KK-do_eQ-ee85e9es8nVa31IrSMze6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7342d0d8c1.mp4?token=GiwqK0DN5I0edfPGnqP1PWjk60HNpeJtORiQ17aCdezUk1Z3WDoQ-a6a27ozkDwv4aKdOJi156n5hSFPtg1Nj_f0oQ5BbZ4kljT4d-0sF3FoBdj-wnyAFBOP0FilR0ZJ07tvY2iQ58EavRm5899yhBjKh8_3Dt5xOgHNlK12BPkPGFVDkihHIXfmEFpNeluOSV6fkYCz3fSw29Xy5veD8KCeCBy7hQJj30cITgAGceRuIUQ_MxLvtJmxAEILYa0vCpN8DeC5wbUT8RH5JMfSkQu1dnkZgt3SZjdUKNVrh1Jn3IPcW0rE66KK-do_eQ-ee85e9es8nVa31IrSMze6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد!
🔹
روس‌ها به ایران گفته‌اند باور نمی‌کردیم شما اینقدر قابلیت داشته باشید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442383" target="_blank">📅 22:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddzDO5pCBk_JOV3lJ3D09znsyILzm-3ULQ6ZOqoyT5PNQfGDrCoazdFthVm4P_OV8M6ldmS8b6KZmwPXHqsKgiMAq0VnflFlNjTJF1NLr1U4ApAuEAG2f7xaelmpv51AGYbaOOmamy5iJDbojuACdKQeNvzDig0FJak9jxq_owzmViZ_I1tt2vwtkRJIeibIP0erPW98KuUvwlNa5BDOpDiKKw9qM7engcxeLhEQoXFM5oLAUv8DHdRVQp-AzF_YeoqxJFJo202CE3ZgGwVyLYQjNVJrE8EgPB67etHw0kfv70ygVYFIMdb4TiLy4KzEfmYRHAD0SEeeRfxQUhK_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85a312912.mp4?token=I0xG88PFZ_pbZ340tH3DYLJ9PlimSA38C5hJHsuJp1VDuUwriNP78PRCS5Pe7_6trfCMpEQTGB2WvkQBLgpHlW4GXvMxMSuenjLNGUtwduD7v26VYY5mjnYeT798TCWAenQcjhHoRlKcyJKYuZObqIj9_R2fORNj95hrxZpMms0sS9ka15nRtXLLKEz7LoGYYH6UiQqY9HmJ8WqG8-LqqfPe-GEJpXwP677OzCQ2NrfwEI6u1mnKf_FarySQrtf1npC6iuO9T3yymSkDfISpK1StHwqN6rJVdrGcEPdImN9fSZCBMzALPWy0BB4sMuMJTmAYkl6h-Xkz123Q3S2XJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85a312912.mp4?token=I0xG88PFZ_pbZ340tH3DYLJ9PlimSA38C5hJHsuJp1VDuUwriNP78PRCS5Pe7_6trfCMpEQTGB2WvkQBLgpHlW4GXvMxMSuenjLNGUtwduD7v26VYY5mjnYeT798TCWAenQcjhHoRlKcyJKYuZObqIj9_R2fORNj95hrxZpMms0sS9ka15nRtXLLKEz7LoGYYH6UiQqY9HmJ8WqG8-LqqfPe-GEJpXwP677OzCQ2NrfwEI6u1mnKf_FarySQrtf1npC6iuO9T3yymSkDfISpK1StHwqN6rJVdrGcEPdImN9fSZCBMzALPWy0BB4sMuMJTmAYkl6h-Xkz123Q3S2XJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن B-52 آمریکا سقوط کرد
🔹
منابع خبری بین‌المللی گزارش داده‌اند یک فروند هواپیمای بمب‌افکن B-52  متعلق به نیروی هوایی آمریکا به فاصله کوتاهی بعد از برخاستن از پایگاه هوایی «ادواردز» سقوط کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442381" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193e2e2d08.mp4?token=ikurfVx8qL19oQkpjJtvtSGo7YyduNJE4g-1262e3HnjA86Zb65Am6AkdOr5GQuSZFk5MAsbezDYD2AX0RMP7aFrCdfPFQ9b9ApR4_W-Le7a0J5Tu-MhYh3shMHGnPN5tlRQpsC6FkoTNGGw0OCyO5QP1QMFgiN4wdvmfY9CW7kmRHeormJPEXgQ4o3oP7cocWiGrPZpzuBIBwJZqiOon84szlEhjEyYwlQZ8HcZpLDSNEbZizBXWENhcozkC1Q9fmiYXirh8FRjk364I1pBq7MG5vJx5P1zU7KaJjft3d1NPhZGJmtp6bmD1ndyHUWuV3D3HD7t0gANAEI7A8GorVIaok4PQHGKWDMY2fbtzCYcKJi0xYRyDn3zabyF6b8QIRTGPHstzApj5FoMnJon1rVUatGRvuKbIdvtczXDQTwVw7lPlJe16Rev9ItFRPptQ0bqleMvN1MXtcZOpOvPU0U3Xe-NOJi-Hfe-s4Es9KlhAUK8k6RCNbE-e82O-xq0EZC8uZqGSjokxe0WBMH83Ko2iTvf47SPAqB6QooNdRUgcDNYbRt-QQe4C5ml6tLpzhk8QGeqDCPYzb0BW8tF8hDH_SrPmIG2AFNhir6SacL9dVWeo3UhuzBRi8mxa6wY8gIx5OEMZxSQl0b0RL19vw3XpvEtzeRkXw5SBOX4zQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193e2e2d08.mp4?token=ikurfVx8qL19oQkpjJtvtSGo7YyduNJE4g-1262e3HnjA86Zb65Am6AkdOr5GQuSZFk5MAsbezDYD2AX0RMP7aFrCdfPFQ9b9ApR4_W-Le7a0J5Tu-MhYh3shMHGnPN5tlRQpsC6FkoTNGGw0OCyO5QP1QMFgiN4wdvmfY9CW7kmRHeormJPEXgQ4o3oP7cocWiGrPZpzuBIBwJZqiOon84szlEhjEyYwlQZ8HcZpLDSNEbZizBXWENhcozkC1Q9fmiYXirh8FRjk364I1pBq7MG5vJx5P1zU7KaJjft3d1NPhZGJmtp6bmD1ndyHUWuV3D3HD7t0gANAEI7A8GorVIaok4PQHGKWDMY2fbtzCYcKJi0xYRyDn3zabyF6b8QIRTGPHstzApj5FoMnJon1rVUatGRvuKbIdvtczXDQTwVw7lPlJe16Rev9ItFRPptQ0bqleMvN1MXtcZOpOvPU0U3Xe-NOJi-Hfe-s4Es9KlhAUK8k6RCNbE-e82O-xq0EZC8uZqGSjokxe0WBMH83Ko2iTvf47SPAqB6QooNdRUgcDNYbRt-QQe4C5ml6tLpzhk8QGeqDCPYzb0BW8tF8hDH_SrPmIG2AFNhir6SacL9dVWeo3UhuzBRi8mxa6wY8gIx5OEMZxSQl0b0RL19vw3XpvEtzeRkXw5SBOX4zQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دهه‌نودی‌ها در تجمع امشب مردم شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/442380" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951dd9db33.mp4?token=wATdsV5BBSXKVHSnSAySKLkBDL9MXbrLz1DR9cMRmvI6yAUropKrcO0Bvlu8hbhT3cMSfEd41nt-k3DZa06DsISWj_03RaWyLcdgw3JPyhSJMVN2jiNZX7bbBpCzAOqkx5GT3gkK83-du48AfEfnBX2DiPpFYS7ZR4bmPPLFrXV1-lA46I78P_2sASDrziEz-ZzIKQRe1blnd0sr_cbOM0L884MHqSmCFyKEX7UT3OJ-radTATYypbQ0TgAThHTGzZ5OI-QubCnYdc3Qksq90XrL7MmSMxc7Vvg1zSUjBNK6YgqojKArQ72PxlTeGZANK5tFCMqtirWRQ5mgxowb3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951dd9db33.mp4?token=wATdsV5BBSXKVHSnSAySKLkBDL9MXbrLz1DR9cMRmvI6yAUropKrcO0Bvlu8hbhT3cMSfEd41nt-k3DZa06DsISWj_03RaWyLcdgw3JPyhSJMVN2jiNZX7bbBpCzAOqkx5GT3gkK83-du48AfEfnBX2DiPpFYS7ZR4bmPPLFrXV1-lA46I78P_2sASDrziEz-ZzIKQRe1blnd0sr_cbOM0L884MHqSmCFyKEX7UT3OJ-radTATYypbQ0TgAThHTGzZ5OI-QubCnYdc3Qksq90XrL7MmSMxc7Vvg1zSUjBNK6YgqojKArQ72PxlTeGZANK5tFCMqtirWRQ5mgxowb3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمام
‌
زنی با شکوه گراشی‌های استان فارس در اولین شب حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442379" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c89d0f414.mp4?token=l_LtehXPo_nv2UCMsst2UqjT2GbqEp6ayyZaWmc7IC1UvnT5YFSQtVxXCLCZ1mdyvsvMMtI8403ZSWjnW7kQO-xKjoxHMb3Dff7BXm_vQqc0BY6c5CQtaXWg3iJoY46ozxPgQZ_pjWsX_AobIGM_TK7BziEsV3xGaRmrMlE0EW7D0YbCi0ieZjVbTeeVRjx9TZJuuZ7FE2K9mgf9NmSWSY4pDcVju9agYbWi4sfbbU7nw6LTNClR9VTPKsGyx2mL-0NNYM7MhxAoTzl7MSqPtawyFm08FgnL9OpuXHCRmB5mLBQXSydjk5AZ8HEyMxB0oHgAemhKi9fUkkhxbdnaRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c89d0f414.mp4?token=l_LtehXPo_nv2UCMsst2UqjT2GbqEp6ayyZaWmc7IC1UvnT5YFSQtVxXCLCZ1mdyvsvMMtI8403ZSWjnW7kQO-xKjoxHMb3Dff7BXm_vQqc0BY6c5CQtaXWg3iJoY46ozxPgQZ_pjWsX_AobIGM_TK7BziEsV3xGaRmrMlE0EW7D0YbCi0ieZjVbTeeVRjx9TZJuuZ7FE2K9mgf9NmSWSY4pDcVju9agYbWi4sfbbU7nw6LTNClR9VTPKsGyx2mL-0NNYM7MhxAoTzl7MSqPtawyFm08FgnL9OpuXHCRmB5mLBQXSydjk5AZ8HEyMxB0oHgAemhKi9fUkkhxbdnaRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین شگفتی جام جهانی
🔹
اسپانیا از پس کیپ‌ورد برنیامد.
⚽️
اسپانیا ۰ - ۰ کیپ‌ورد @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442378" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c2e418b00.mp4?token=knp3pCo4avWBuxPe1KDbRVTC7Bgcx_MBVzQq3mIYpvKmjummKNHSvzLHSSQiLGEVJRiEfLy8u_0N0_R7X37nUxvNCtR9dEfZWVgehb27ioY4BFPLj7CkPlrUZF60qw0HYMzwM90OsFapldmGKuW58kLwIy9q8kS90lQ2mAj6HsR7k60ccVGNt3Wo-7UYMAZQtAU6MN6pn-IurR1gDea3DS9IhmolP4wcyjRTzDBns7tqt39DSQxsEHddJEQMYTGEKqGDIFXxXDcuSdkeqstXfrTwgATxcE1Ej41tf-VPA_kGirSTELXRICS_Y04npISxTYgJMJ1lK53lCrb9Knn8Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c2e418b00.mp4?token=knp3pCo4avWBuxPe1KDbRVTC7Bgcx_MBVzQq3mIYpvKmjummKNHSvzLHSSQiLGEVJRiEfLy8u_0N0_R7X37nUxvNCtR9dEfZWVgehb27ioY4BFPLj7CkPlrUZF60qw0HYMzwM90OsFapldmGKuW58kLwIy9q8kS90lQ2mAj6HsR7k60ccVGNt3Wo-7UYMAZQtAU6MN6pn-IurR1gDea3DS9IhmolP4wcyjRTzDBns7tqt39DSQxsEHddJEQMYTGEKqGDIFXxXDcuSdkeqstXfrTwgATxcE1Ej41tf-VPA_kGirSTELXRICS_Y04npISxTYgJMJ1lK53lCrb9Knn8Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری گرگانی‌ها به محرم‌الحرام رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/442377" target="_blank">📅 22:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442376">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">منبع آگاه: ادعای الجزیره در خصوص عدم شمول لبنان در تفاهم‌نامه کذب است
🔹
پیگیری خبرنگار سیاسی از منابع نزدیک به تیم مذاکره‌کننده از اعمال برخی تغییرات در متن یادداشت تفاهم طی ساعات پایانی گفت‌وگوها خبر دادند.
🔹
براساس اطلاعات دریافتی، یکی از مهم‌ترین اصلاحات انجام‌شده در متن نهایی، اضافه‌شدن عبارتی با مضمون «احترام به تمامیت ارضی و حاکمیت لبنان» است که شامگاه گذشته و در جریان آخرین مراحل جمع‌بندی متن مورد توافق قرار گرفته است.
🔹
پیگیری خبرنگار سیاسی از منبع آگاه نزدیک به تیم مذاکره‌کننده همچنین نشان می‌دهد در یکی دیگر از بندهای مهم یادداشت تفاهم بر «خاتمه فوری و دائمی جنگ بین ایران و آمریکا و متحدان» تأکید شده است.
🔹
به‌گفته این منبع نزدیک به تیم مذاکره‌کننده، همزمانی تأکید بر پایان تنش‌ها و اضافه‌شدن بند مرتبط با لبنان، از نگاه برخی ناظران سیاسی واجد پیام‌های فرامنطقه‌ای است و نمی‌توان آن را صرفاً یک ملاحظه دیپلماتیک یا حقوقی تلقی کرد.
🔸
پیشتر رسانه قطری الجزیره به‌نقل از یک مقام رسمی آمریکایی ادعا کرده بود که «عقب نشینی از لبنان جزو توافق ایران و آمریکا نیست».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442376" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442375">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02aeee65d3.mp4?token=OUCIS8m5LHrD6YZvtSmvh-VAbvIuIyIyWs1V_PdSRdxvLmJceypRzztrQRacqtzDHRl7k_rM11IkIS3SB6bRr9kiQzffowMFk2XHsGcW2XisW19s7D9CoGpfuxpCfF6Y6UBLUsWbZtXb4UMecuHzfg-lIgFE3sP0HsxYvMVhBG43XN5T_MF9fVrTlBhec3JvLeXEQPw1uhXcNtySaFO3-6r3AfknUWHl3j7UEy5161uqdtF8hZ37I8vARle2MMwO8yx8xcfp9vL_9oSh5ODgjC_8mzNOB0m14mjdhhcYCmXBmUqZrGNczxCXA18Y2V0quuGHyycvG6YAPt3Un2MDhFHuEMRKGlB-FWhnp7iEur8kHUX4XPsX0CmlLbtLxnRgWRmR2GXRxafhN2W6ozCQnHeUbDJ7I50UYG7nfSNSZy-EqT9Ny3lfqCq09XSKK6NHRpPCg2XBpeq90O4q89pf-E53KPrdpY8sf8ElG38TIRp2lKIlyVs17eWyDcboaUhLnAA5nY9_fddFPqea2MgxU8-oqQRDiVOGCyRKHdXiIrXYcCAt93j7m2EFNEL-Pqgjck58A0LP_sCHxQLvLcy2nqKcffnvzZ6di6vMX-elp1lz2aGIO-tVhs1ifQfiJX61grWYj6Y7gV5KBGpBTCrI2NlTN_PE-laRh38YZ3CEveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02aeee65d3.mp4?token=OUCIS8m5LHrD6YZvtSmvh-VAbvIuIyIyWs1V_PdSRdxvLmJceypRzztrQRacqtzDHRl7k_rM11IkIS3SB6bRr9kiQzffowMFk2XHsGcW2XisW19s7D9CoGpfuxpCfF6Y6UBLUsWbZtXb4UMecuHzfg-lIgFE3sP0HsxYvMVhBG43XN5T_MF9fVrTlBhec3JvLeXEQPw1uhXcNtySaFO3-6r3AfknUWHl3j7UEy5161uqdtF8hZ37I8vARle2MMwO8yx8xcfp9vL_9oSh5ODgjC_8mzNOB0m14mjdhhcYCmXBmUqZrGNczxCXA18Y2V0quuGHyycvG6YAPt3Un2MDhFHuEMRKGlB-FWhnp7iEur8kHUX4XPsX0CmlLbtLxnRgWRmR2GXRxafhN2W6ozCQnHeUbDJ7I50UYG7nfSNSZy-EqT9Ny3lfqCq09XSKK6NHRpPCg2XBpeq90O4q89pf-E53KPrdpY8sf8ElG38TIRp2lKIlyVs17eWyDcboaUhLnAA5nY9_fddFPqea2MgxU8-oqQRDiVOGCyRKHdXiIrXYcCAt93j7m2EFNEL-Pqgjck58A0LP_sCHxQLvLcy2nqKcffnvzZ6di6vMX-elp1lz2aGIO-tVhs1ifQfiJX61grWYj6Y7gV5KBGpBTCrI2NlTN_PE-laRh38YZ3CEveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بوی محرم در شب ۱۰۷ شهرکرد پیچید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/442375" target="_blank">📅 22:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442368">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaTC_HabmPnM8LJIyIF_T5ngfqyagUrPmvdJ6ekpurrYx1LKNJVrfGBcMjauSHIcZXCGrXU8oJfnLaTnUC_ghNVlToDLAWx7ysKoo4rGEInRbEwOAnf-MUi56b_yZz035_J3YENLHZRk7V2_7LsGRpBaz44luWl6iXk8EI9XqKMJ3OIZyNM30t-wQUKKxKyJKNHGopD1E9NvtFOEWv7wcGnz8AyGJ4qKR_EmWGo5kKGjNAjqwVs81N3qdfDFIwsftepqhdvNaatKjzynl01ObnESCioNqWdzPE-eZgCnzA2M_n7IJ-lmjrxnIiUplePuGmC53FvuZ0Yzo1cq3jh4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpe-_8OJJ2IfCwvOO6eH0fwSCYX_QWYU46eWI-ZyCF4ag-DYhyR1J4YFIKlIhmUow7L581oyHoqFLi20J12fgjH6znnl-Aq1o6Ec2Y3fII26RexXJ_K-o-X3c-RXXpsRd9RGFKP_X8-za5Oe6uDussfM-loCKqyPiNp1ydze1C2xGEVfHqNQxxirj4VJ3GNqBJDq903QkkOsjUaYZ4rGsAbpazeT0zaa0slx2wObJtF6fDvtAz5WENkPumVhqmZw23x3rF55xZjauhbBRxHJsfKrwOggYk4n_8thBMPQ92Oad3OND59IhvPq-LqfIQcBS1JdzSwOrlapS0eYRTAdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/re_C0Qa8uJ-Dy7dcWu5lrtHWfJWYWjK0cFV4YYR3gNsJDwzY3Aw9azz-e61ApqYqFS2cvZfh2-HMoKamX3tawv_RQwsCPG4nTu6MdQQ0uCGlWvXbIFBFDr_5fWnSlDuxiDW_iKd-VsaHCIGN_HvqYSCGqYPPEjQjkz44wyvpcqzFrgJNS0agEiPx0VtChGeO50GemDwu1r25GLlTqrvFXKvQaOgV0Ghz5yDrSU6eM57L7TwqCZaX7epXHjmHHPiKDL26y7KRnO4fdcJ9V1n9niM_58gUhaj0xKmXy1G3R6x_NWdV_N90RvlHym5Tdxko-yiDvylvmSgWPN5plaKWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWPPVgIkutJhKHYp0iQJGOdjAQVeZDxBQnWq7fL0hH_kRuQEEKTHP1fnFouqPsQ3ryBx_zIrRdxzt4IpDnBE2Dk_Qw3yz5rXxoMiucn0ymCVnzsmEkquzRO1y0___2p_c89U5Py_UT_TePfTIlECp_oBsUNVpoHflk5rmsZV4rHaQBMtgC-TkvFXDmyOTh9y3Bw7t1vVAv3U0A5t-VT4k6rtbcCiCKL4sstBTorzieoBnAplnsOTvz8-3zyO7EpbgdUGMiNt_Ecb_it6Q8jcSzS1C4qXz3jHMYbILjG9mPnUnz8cnIKAP8RZNiM5ZW78a6zHzxs1lTFniboMu84qWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byia2wdJVO3De295pYGc7xKXA41dHta3QWoCIKMiL9we-3BrhyXcYbco8J6FFIDPL5hLRs5ODzuIwCizTvc8aICJnpGVO8nkWODZy2ZrZOAjUXKnnPc2ez9NSjSJD5qEEp7lo7zuYrnZZnUfxjSa8PkhSf1cgwZIOupEi0N6xGDoH-556S4hp4IyFU_K9zGSVGJI_i300WMFmxvItjIH5fjt-Dr0eByInOdra-UCsLwkGDZwmqqyi9JZlBcxQpfazxgVmnIUGjMb19hr8Uv7Jt0hZ7Z9VQX0xVbkXHEvyfe_Cw-dh-WGzarlP3eYDWYkiypFfJWXmKpCwBhN6Ui6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpeZfsYieWjyv5nPHd4Y5bB8Ef0xY4qNOlLPQdY_7CV6KN3QeGjkcNKQDB09rcrZ5oA1YfjKnHNlqwxlSMm0BMjCaVbHCZyNLB58-UVr057j2BZp7TY5qO3kk2fvIcLSmw3G3SENaJCoiT6GHveNhBeQdkiqgaWD1qpIqjfOczqNcDyaVQmXq2y-JN4GZC5fQ_UibXgxygFTDcL5dVBXXQkYzzxt4h4NPSoV_7ivQCde5xNV9uv5sn0pIrgXN78k_WfDf613uI1zSSeT7taa87RUGyfoOA16KTgvtuD1lFFS-P8hronfdwDg5qB2xG7QGrlIv4b9_-6X6BhK6PXHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQZ7YSjYwai5JH-Ua_ddhiFlsrtCw8IX83-PHsck8k7sYNfbSz9m4Wh2Pf045Yv0UxxJ9jGJEIqWoYA-OVTfJmUcMIJC7CFQa48sNAWrE_O3zkHARP7XE249XDDvkFjQxuElES2Ls_U7m5DV-qlBBLd2D_LxnRvj5KIdkz8DgSMylhPEHOi2i6P9Xdf1jDxIWCCc4k5WOTJinwBeOh_ozB2xCh-1q4V5WbZ3L4HG5ZeVRt5htGvAK1es1OcsKMWJyzc_YsZ40KG_4pCbXgrtpmQ_ftvUSBP_svzQVu7wOjX74EMHijGvJZsRzRThiBOXhGyQTFmG3UprnyqY9uKT4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اذن عزای ماه محرم از امام رضا(ع)
عکس:
امیرمهدی آقاجانی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442368" target="_blank">📅 22:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843c083ba2.mp4?token=iuLf1Zbrvp8iSsLi6J9qNElCmVF9MFjZFzhCrfTtUGaPzYTNsKduEFyzWb4Mz5LCDqICEmdH8mabo0hT2l6rFQ5d1qXHONj2LwaxZwcOj3i2xAeFOlCpHC2h_edFHQ1EyT9Mjqzx8Y1amJXOQYzmIUwYjG3546hCigdUxJ52ujBBmqhLm3ACPomKVmksgA8Z7rF91XpbZZzqAt4QiNv_Pd39vExqU8k5GhnAv-hqdE1ap0sYY8eviwyg5dcymi4wzaqu577RENxkAl8GX95Ok9UHoH2PyLkudHfjtYDrEmkGcHkSWzCRydZ6ty3M9K1LWEM9zv4xc2VSlZ1HZtKT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843c083ba2.mp4?token=iuLf1Zbrvp8iSsLi6J9qNElCmVF9MFjZFzhCrfTtUGaPzYTNsKduEFyzWb4Mz5LCDqICEmdH8mabo0hT2l6rFQ5d1qXHONj2LwaxZwcOj3i2xAeFOlCpHC2h_edFHQ1EyT9Mjqzx8Y1amJXOQYzmIUwYjG3546hCigdUxJ52ujBBmqhLm3ACPomKVmksgA8Z7rF91XpbZZzqAt4QiNv_Pd39vExqU8k5GhnAv-hqdE1ap0sYY8eviwyg5dcymi4wzaqu577RENxkAl8GX95Ok9UHoH2PyLkudHfjtYDrEmkGcHkSWzCRydZ6ty3M9K1LWEM9zv4xc2VSlZ1HZtKT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین سنتی علم‌بندی آستانه‌اشرفیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/442367" target="_blank">📅 22:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ee9477bc.mp4?token=H2a69lYhbDHQsnFvLqCfXy6VuSh-l6U4z-jNefTdSt0475Db_gHlkf_Vv-IKBpqRnIS62zV1y50mzvKHNGq9_Rms1WPuZyTnb6nl6EOWcotnJXCeoSwonB1W0TPMAwuVLxn7yBEZ8mS9LYjPNED6vp2wkMZisnWJ_zelt6BZXvHTCBkyauE_eCOGC-N1haeCS93BOIMfQToscI4CZy96QBuD-iq40jyFxll5CwvmJjBeQaZuPK-9fbyHlZHjGBG595D_ZQdh9CNzoFt9D3zCeDBSU5jmR62RdpMKbX25kKDu_AhI99SLQXZ0iwBvqVJLTZDpmUbS_NaEP0f7aZyRnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ee9477bc.mp4?token=H2a69lYhbDHQsnFvLqCfXy6VuSh-l6U4z-jNefTdSt0475Db_gHlkf_Vv-IKBpqRnIS62zV1y50mzvKHNGq9_Rms1WPuZyTnb6nl6EOWcotnJXCeoSwonB1W0TPMAwuVLxn7yBEZ8mS9LYjPNED6vp2wkMZisnWJ_zelt6BZXvHTCBkyauE_eCOGC-N1haeCS93BOIMfQToscI4CZy96QBuD-iq40jyFxll5CwvmJjBeQaZuPK-9fbyHlZHjGBG595D_ZQdh9CNzoFt9D3zCeDBSU5jmR62RdpMKbX25kKDu_AhI99SLQXZ0iwBvqVJLTZDpmUbS_NaEP0f7aZyRnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماتم ما امسال دوچندان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442366" target="_blank">📅 22:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
ما لشکر ۹۰ میلیونی حیدریم
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442365" target="_blank">📅 21:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/442360" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب اول محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442360" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/442359" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcfRUSnBcGwW8Xa-HRVX8fkDiF3HawZzuIo0--42HJlEjFlleJUTqROWlmgLYK7cnhHwtiB3R38X8QQKUXJNgDmmLEmPCq_plInO2dGN14Eqey5NE8p-xhrvef7x5KJ-bnsoutHYvrW4yfn8UXt-_aOkRaYrDCmvcvu5fJeM3yQzcH3cLCicmJawq3hnPXeOZc7sMIFwAkpijveJpL2cz2zVOrUVhuTFc5n2OvLLT5mQrDCG3oYJISQlUkkmXPoP07fACPSSpcG1FOGuTwK05u0KTEOjnh6SgmL1CyXvpUIwMHbFJgooaog6yN-eC_di4p0y2t8SBeZ8nRrHwcsq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین شگفتی جام جهانی
🔹
اسپانیا از پس کیپ‌ورد برنیامد.
⚽️
اسپانیا ۰ - ۰ کیپ‌ورد
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442358" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e7bf7ca.mp4?token=g6wbEBIT4YnK_YKoy1XTMpkmYslflj_0F2COoU99cIXvasO89h6KMtuF-TAiXyfjGU07wrncPoiaLdgXUGbhaer1KQICxWwuqkHJw2gcJ9gJqVkV_YBDjBeOnTAGP-vJesQgaU6xWHDMlnkdpuE1ZbQsDoo5ggnJ9RvVvPODCoTedHEUe0ryt1ZHjnQuMZElRV8RJEuiMvDzDUVusGUJWutiL00hTcyPunPUs1yk4tiAEuh1FWH-0AxieORQVEs2NXRkJhT5cTup-zebB1x4QiLbjFBFPL5Cduw5_z1ZHyidi385UTP-5a-9nyrBYj-jrZLdhAjTrvR9ca31h3d8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e7bf7ca.mp4?token=g6wbEBIT4YnK_YKoy1XTMpkmYslflj_0F2COoU99cIXvasO89h6KMtuF-TAiXyfjGU07wrncPoiaLdgXUGbhaer1KQICxWwuqkHJw2gcJ9gJqVkV_YBDjBeOnTAGP-vJesQgaU6xWHDMlnkdpuE1ZbQsDoo5ggnJ9RvVvPODCoTedHEUe0ryt1ZHjnQuMZElRV8RJEuiMvDzDUVusGUJWutiL00hTcyPunPUs1yk4tiAEuh1FWH-0AxieORQVEs2NXRkJhT5cTup-zebB1x4QiLbjFBFPL5Cduw5_z1ZHyidi385UTP-5a-9nyrBYj-jrZLdhAjTrvR9ca31h3d8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۸ دلیل علیه فراموشی
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/442357" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37089622.mp4?token=ARoovH2n71afOoPdt2i5wwYdR8Tg4I3NQoZl7Eiaw9AcsdhMA6xXnENbpQ3YUXAgk7LjN-UDl-WzC9OHdH_2DcwcmLnfYDdMb8x6FwuBaTEi_mbRdPs5dOZ0lNW8eTEf4F0sihkebSD7aleZzg1eAFJOAZqhuO_gt_Oo9HGTgD7XaOe9p4-O7ict-vNnmsLJFf5WA0hOQVq0ldwanLvP07129c2uPMyTMy3-A-Aa8Hl5pbWL8KN1uJBuCmj-XBslBpEkdinVYXhYHbgPbNKk50TTdvKcwqToh1kFjOtIpWCqscRtLoTzR_Li06QeWbXwthHmbuyvYxN1MFw50ZKFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37089622.mp4?token=ARoovH2n71afOoPdt2i5wwYdR8Tg4I3NQoZl7Eiaw9AcsdhMA6xXnENbpQ3YUXAgk7LjN-UDl-WzC9OHdH_2DcwcmLnfYDdMb8x6FwuBaTEi_mbRdPs5dOZ0lNW8eTEf4F0sihkebSD7aleZzg1eAFJOAZqhuO_gt_Oo9HGTgD7XaOe9p4-O7ict-vNnmsLJFf5WA0hOQVq0ldwanLvP07129c2uPMyTMy3-A-Aa8Hl5pbWL8KN1uJBuCmj-XBslBpEkdinVYXhYHbgPbNKk50TTdvKcwqToh1kFjOtIpWCqscRtLoTzR_Li06QeWbXwthHmbuyvYxN1MFw50ZKFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه هدف قراردادن تجمع سربازان صهیونیست توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/442356" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت باب القبله طهران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN_WEUC7S2lZKaK0za-8cy6Rjnph1yn-5CSbYfCuDSYQxCBHIXl838u_3EjmNvpGtUIgcgk7SpYC4YRJzsPZ5Q-lCKY4ulZXHU7OBtyw-iiR3spSAGrrigAaluXQwkVFwGXuGsYSscnMieiXGC9qBzw0aIYfQdbADRx39tld6Ay4HsEXu4-jRzuvsI4Hu8MyZn8GWJjkGflmJtIYFYv6TMggCrFPplKQq_rFxK8EjHHjKSTQZc2Cd7Sgl0Vpk4-hqnvx43YLiSbO9AAu-ZvjwtgYaEjKnIT-teSr6oacDJW60xEz0eQ4R_YoUpfPoe0ZGqi11JHvBXlDU0v9j-Scxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TghB90IRTLn17_SZD6lcChi7s7KTSf9EZXdKD9hGUEvtjxbV5SoTpL_iuxP5nwpkCZ3cyL3OcGl4D2eMMm4Gr2rm1uyJ1_3TxjmQYBNwvDcrKlLVFQs2uq1lyRrt1LHM8yVdvjvWPebDGpzDIc8ULVSfVyNA2zZN-WvCJZLcSSLSFFMO4E7ItX2xwKN61qapVmERnxjPiY0zLfFzDICIbAuPF3LL-zHnLBHnCIVpGVoMW9LKFI0nEwZk7NTYBgLDBQvpiE1LZxcgeyOiGi6mL3ODiK_QvxpUTd9NOUH_3JQVKJmBEAzUuQB-OrjlkK5OMIOSNSFIRWDLal_3ITny1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بـسـم‌ربِّ‌الـحـسـیـن
🏴
اقـامه‌عـزای دهه‌ی‌اوّل محرم الحرام ۱۴۴۸هـ.قـ
به‌اِذن‌الله‌وحضرات‌آل‌الله ﷺ ودرضلِّ‌توجهات‌حضرت ‌صاحب‌الزمان‌ارواحنا‌فداه  وبه‌یادقائدعظیم‌الشان‌امام‌خامنه‌ای‌
و شـ ‌هــ‌ دای عزیزمان
🗓️
دوشـنـبـه۲۵‌خرداد‌به‌مدت‌ده‌شب
🕰️
ساعت۲۳
سـخـنـران:
🎙️
استادمعظم‌حاج‌آقاسیدرضـاجـعفـری
مداحان:
🎤
حـاج‌عـلـی‌عـلـیـان
🎤
کـربـلائـی‌سـیـدجـوادپـرئـی
‌
📍
لوکیشن حسینیه باب القبله
‌‌خیابان‌سعدی‌خیابان‌جمهوری‌کوچه‌درختی
🔺
ویـژه‌برادران
‌
#محرم۱۴۰۵
#محفل_اشک
#هیئت_باب_القبله_طهران
‌    ━━━◈❖✿❖◈━━━
اینستاگرام
|
تلگرام
|
واتساپ
|
بـله
|
روبیکا
╭━━⊰•═
🍃
═•⊱━━╮
@babolghebleh_ir
╰━━⊰•═
🍃
═•⊱━━╯</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/442354" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/442353" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7373d222.mp4?token=F0TEB3vH2070iU_uSl0J_RFO-7oaapOdvay8NszO4Yn2IGcvrD1wz2haWc96rw_Jk3IrByWVn3uV2agalRyzCL5OZIiVI2N19Gf_UJ69PKM1csCIfHQWEw2-AeWZjIg7E_PfpJ4Wu5or_2kJnIiL4LpIZTbpEpxWAP19dVNdi7qsOfJx4zxeajxICo9G6PpcOKgmaHWgH8nYhHxyDNgc_Y34Qe6YplOElaiS-CckphIMgG4ycdkjA4U5tXz2IJzmlEZBkBUMz0D3_tGilFeo0cLw-JxrNFvLlyX6EMEnGu6L9COpVk3ETSApgStHGoSY3YSCXhezjzN2hvRAwmk9rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7373d222.mp4?token=F0TEB3vH2070iU_uSl0J_RFO-7oaapOdvay8NszO4Yn2IGcvrD1wz2haWc96rw_Jk3IrByWVn3uV2agalRyzCL5OZIiVI2N19Gf_UJ69PKM1csCIfHQWEw2-AeWZjIg7E_PfpJ4Wu5or_2kJnIiL4LpIZTbpEpxWAP19dVNdi7qsOfJx4zxeajxICo9G6PpcOKgmaHWgH8nYhHxyDNgc_Y34Qe6YplOElaiS-CckphIMgG4ycdkjA4U5tXz2IJzmlEZBkBUMz0D3_tGilFeo0cLw-JxrNFvLlyX6EMEnGu6L9COpVk3ETSApgStHGoSY3YSCXhezjzN2hvRAwmk9rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرنوشت «تنگهٔ هرمز» چه خواهد شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/442352" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442351">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_1ElsQw_ODqEuSo_bPy1Uc1uHwM67c1MKJteGoOrUgLSkRKPJNWsFGsEDCoqKxKiJB13nBHg5D3hqoQrJhYuXnilz0NL9wUhn23lEW4POJp5TvvbvtVtCtTCKobYmlc_ReLd-KNad7gfpIcF3Q7t5GGg_5_UMPoTie5I92MiukkCL1Q1mQXPUl7yG-Q6J8clYswzas9cABDSCTZ7ZyeelLZUzmCv04VUHsIhq3IUHt4HrFsh0GlIOHq8U3xClC8cSD-XqBGDo7PC7xtLTif9wGD71pXU6oJY1hIKoQP8Nawr-eia22VPCHl5P52USeYi43GJTK6xjSIWPBOhYMZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: تمرکز ما با یا بدون توافق خدمت به مردم است
🔹
آن‌چه تفاهم شده، گامی مهم برای توقف جنگ و شروع مذاکره است و هنوز توافق نهایی شکل نگرفته است.
🔹
جمهوری اسلامی ایران خود را برای همه گزینه‌ها آماده کرده و تمرکز دولت با یا بدون توافق خدمت صادقانه به مردم است؛ ملت ایران از امام شهیدش آموخته که زیر بار ذلت نرود.
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/442351" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442350">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5rxRGBQpFohTvRaakA3Zy_Z3M2sWIJoxUEUcaa3IqNmxMcAXsz6xkelnKWuIZZeEWQNaL3cX-B6Ku38CMEbXoHITKIDLS0QWL0TDgmtEn9XejN4kNSY6laZU4PBis93hkYIKvW0imyp2cbmPugYQ4HP1DfgKvzzwMj0GnEHxjYFnQQ83xDa3AkCbTp6mDqHhv5Sb1rhlTChAhaPd1b6zGMA6V4hW-Y4Z7jAgCFr5M16B2-ZGWUW4mY7DJwF5d3b0sPtkKAn8VOXDCPYxoxZR19cr6gmZCv3idsREDOp21efH3kY37Zpd1brlcF_dKjknFw-uN-Acb32Ssp1WA34QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: در دورۀ توافق توان دفاعی خود را افزایش می‌دهیم
🔹
ما از هرگونه تفاهم و توافقی که منافع ملت ایران را تأمین کند حمایت خواهیم کرد، اما معتقدیم اجرای تعهدات از سوی دشمن نیازمند اعمال قدرت است.
🔹
اگر دشمن در اجرای مفاد توافق یا تفاهم‌نامه مرتکب نقض عهد شود، با سرعت و قدرت وضعیت نظامی منطقه را به شرایط پیش از توافق بازمی‌گردانیم.
🔹
سطح آمادگی نیروهای مسلح را بیش از گذشته حفظ خواهیم کرد تا دشمن ناچار به اجرای مفاد توافق و پایبندی به تعهدات خود شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/442350" target="_blank">📅 21:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ac2f8c5d.mp4?token=oC3VqLm7pcY8NJiVHSOglS43aV4Z5L4EX-ZtlhQxDCFAlZNMGvLnRwzvZb4Gnq7Yh2S_Ty5wGlO-ORsA_mtegL9G0M5tP8eo9B-Qlh5Fe8cJY1Bq4Y0FfYxv9Ap63RUrmk7I9uWVZw5U4wogEtvh9tbGxuZ8Go0_356tVaUH8HZkZV_NO0a1HdEO5g2CepVG2TME-ONAH__YIus2WYnYPY5YfwZb9P10JUoTvZMpGIXdxCAETCqzWMJ-2UcnyBgInSPu-qIWMIZ8lNDQ2xwfO2gRs0vsVJ1qMNJr-elTOTrUStN5Nmwk9hzXYCyfUbp9z7Un_NRFXxr9o0FDbJGqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ac2f8c5d.mp4?token=oC3VqLm7pcY8NJiVHSOglS43aV4Z5L4EX-ZtlhQxDCFAlZNMGvLnRwzvZb4Gnq7Yh2S_Ty5wGlO-ORsA_mtegL9G0M5tP8eo9B-Qlh5Fe8cJY1Bq4Y0FfYxv9Ap63RUrmk7I9uWVZw5U4wogEtvh9tbGxuZ8Go0_356tVaUH8HZkZV_NO0a1HdEO5g2CepVG2TME-ONAH__YIus2WYnYPY5YfwZb9P10JUoTvZMpGIXdxCAETCqzWMJ-2UcnyBgInSPu-qIWMIZ8lNDQ2xwfO2gRs0vsVJ1qMNJr-elTOTrUStN5Nmwk9hzXYCyfUbp9z7Un_NRFXxr9o0FDbJGqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا پایان خرداد فرصت دارید از بخشودگی جریمه دیرکرد بیمه شخص ثالث استفاده کنید
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/442349" target="_blank">📅 21:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763b20fcc8.mp4?token=DplhGVZqPLIyxh0wgw3f6TK2x0-1A5EESsRSp5fvmiab2uSqArFXQ8h8Xix3B9Adau-rxtrGHc6llIwGDUzE7EWG8UmpJdjecQL3aGa_R2m66A8-n5EIwh0GHxNi226qrafnNrpoGACMaT32wy-CwAM4PDhpuPvhDoWqKGNsPKU4BFptPoyhxq3MVlqOY9b3TfCiWXggDzv_Jq-V_Ia3ipgdmQZnnfHtshqSpLiVMuHUXSIfQm083IBXxCNMLyP0oJcHcvJoR6frrGahENvb3M0PrfpBdnTb2TQAaD1ohxrsx-HIcVKJkuskxLND2OTI2i9XWwjDu0oI0QcFllb_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763b20fcc8.mp4?token=DplhGVZqPLIyxh0wgw3f6TK2x0-1A5EESsRSp5fvmiab2uSqArFXQ8h8Xix3B9Adau-rxtrGHc6llIwGDUzE7EWG8UmpJdjecQL3aGa_R2m66A8-n5EIwh0GHxNi226qrafnNrpoGACMaT32wy-CwAM4PDhpuPvhDoWqKGNsPKU4BFptPoyhxq3MVlqOY9b3TfCiWXggDzv_Jq-V_Ia3ipgdmQZnnfHtshqSpLiVMuHUXSIfQm083IBXxCNMLyP0oJcHcvJoR6frrGahENvb3M0PrfpBdnTb2TQAaD1ohxrsx-HIcVKJkuskxLND2OTI2i9XWwjDu0oI0QcFllb_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ما برنامه مذاکرات و اجرای تفاهم را براساس بی‌اعتمادی به طرف مقابل تنظیم می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/442348" target="_blank">📅 21:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1fc1dce5c.mp4?token=hkhk0SC-3qzkmxngOwaCC9t3gPzVZMB8DLjb_3moMk8vHG9M8nXNkD5wU63s8E5zePjRLDhlERzx1fpGpbvoGS6lRI8itAW8Ltry72eo7IosZ3gjrAfKXnA1niNcSqIV0Yg8vmgntMFBIYK0bYkYOpYpmzXBOy_HEvz_0FQ7ulL54EKYPHKv79Sl9vhKP_rjg6l7NQpVzZGd1bgs0M_Z9plyeNJbHxIcqpKfQVgP-pGG_gJDveilZljdEpQi-W9sTl56glhgdziwa6joVqRG0Uk43lvcPcWe4Ffl56zB4otG45o0ofQ8DyndpEbxZQhWeL0RodEm-fP3fLhEu5pllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1fc1dce5c.mp4?token=hkhk0SC-3qzkmxngOwaCC9t3gPzVZMB8DLjb_3moMk8vHG9M8nXNkD5wU63s8E5zePjRLDhlERzx1fpGpbvoGS6lRI8itAW8Ltry72eo7IosZ3gjrAfKXnA1niNcSqIV0Yg8vmgntMFBIYK0bYkYOpYpmzXBOy_HEvz_0FQ7ulL54EKYPHKv79Sl9vhKP_rjg6l7NQpVzZGd1bgs0M_Z9plyeNJbHxIcqpKfQVgP-pGG_gJDveilZljdEpQi-W9sTl56glhgdziwa6joVqRG0Uk43lvcPcWe4Ffl56zB4otG45o0ofQ8DyndpEbxZQhWeL0RodEm-fP3fLhEu5pllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم حرم حضرت معصومه(س) به رنگ عزا درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/442347" target="_blank">📅 21:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442346">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حمله پهپادی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری گزارش دادند پهپاد انتحاری صهیونیست‌ها به شهرک «مجدل زون» در جنوب لبنان اصابت کرده و یک نفر هم زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442346" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442345">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر اقتصاد: مبلغ کالابرگ دهک‌های پایین به‌زودی افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442345" target="_blank">📅 20:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442344">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69117795d.mp4?token=hTRyPhE50wCk_C-Goz5nGq-N5aWPNEW8x0QZWA2TsUok3WLo169EuxhL7J6lYF5k-ZwTbIWMoVP5D9zJeFiwC3OxPfACBoLNStUNLmbxn1k6E3oZk3sGDKm5kdFNwpBiS59GsrSqI9pVlEbfezLx4auWXWeh8eVWC2CcYj4FbIKwlBNZh6MbjqBa1ttZ9NFSfft9PYI8XQ_i96M6rhgJpNcf3y8vmZlZwM2-xv6J-9Z1Jd7UoS4atXddagW1mvfDpPrj401dcLMCZ6s9KPtUm4VDnzG4KuQMqWmrwedplhmZsst72eiQ-XSd8t0jpCR4njYoQpVZ2l2Llbr07G5_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69117795d.mp4?token=hTRyPhE50wCk_C-Goz5nGq-N5aWPNEW8x0QZWA2TsUok3WLo169EuxhL7J6lYF5k-ZwTbIWMoVP5D9zJeFiwC3OxPfACBoLNStUNLmbxn1k6E3oZk3sGDKm5kdFNwpBiS59GsrSqI9pVlEbfezLx4auWXWeh8eVWC2CcYj4FbIKwlBNZh6MbjqBa1ttZ9NFSfft9PYI8XQ_i96M6rhgJpNcf3y8vmZlZwM2-xv6J-9Z1Jd7UoS4atXddagW1mvfDpPrj401dcLMCZ6s9KPtUm4VDnzG4KuQMqWmrwedplhmZsst72eiQ-XSd8t0jpCR4njYoQpVZ2l2Llbr07G5_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: آیا توافق با ایران شامل رفع تحریم خواهد بود؟
🔹
ترامپ: خیر، شامل رفع تحریم نمی‌شود. این یک چیز وابسته به رفتار است.
🔹
معاون ترامپ هم پیش از این در اظهاراتی که گمان می‌رود بخشی از تاکتیک‌های همیشگی واشنگتن برای بدعهدی باشد گفته بود که هرگونه رفع تحریم…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442344" target="_blank">📅 20:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442343">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI-b1JxkZ-zUKnOLesNn7KyceHRBeNg-VmZm7TGzrNSFupuRxsSOtkMvGyBUssT4qwWDD8b698hom9nbeHs1HyOzDxwUMHdBObQVjLHVD8AqNnW19sucpxoSbZYO-ioZ5xIdEltkdDTjLtWTv__gTYRGDgFk-YQox6pkAwr4Y2zO4c2tb_1PrSpHPfkgK5W6qsjcT-XE88pMJS_VNlzDlU6sqpOsmBDLQjNeaylcC_QRm5ARh_A5sJGRVb37DnK8uHkGXrIg5yWCMYWjL6EfKP_0lfYaLq6vXZ8fDgdFpIEEeIVGv5PkhJqmP4g1ae0wIElB1y5k10zMWo3bA6VyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سرآشپز»؛ کپی موفقی که از اصل عقب نماند
🔹
برنامه «سرآشپز» با وجود اقتباس از نمونه خارجی، توانسته با بومی‌سازی مناسب، استفاده از غذاهای ساده و آشنا، طراحی جذاب مسابقه و ریتمی روان، به اثری سرگرم‌کننده و قابل‌قبول برای مخاطب ایرانی تبدیل شود.
🔹
سناریوی برنامه چیز تازه‌ای به نظر نمی‌رسد و آشکارا از نمونه‌ خارجی الهام گرفته است؛( نسخه جهانی «Next Level Chef») اما نکته مثبت اینجاست که سازندگان توانسته‌اند آن را تا حد زیادی با فضای ایرانی تطبیق دهند.
🔹
این «ایرانیزه شدن» را می‌توان در انتخاب غذاها دید. همین موضوع باعث می‌شود مخاطب راحت‌تر با برنامه ارتباط برقرار کند و آن را از فضای تجملی و دست‌نیافتنی برخی برنامه‌های آشپزی دور نگه می‌دارد.
🔗
ادامه را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442343" target="_blank">📅 20:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442342">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2769169015.mp4?token=Y5KlGvhkV_-wH3VYBOt0OqLo7ubzdWBOFtGFMuVTJH_2VSu6h5W3dP8HDT-dxW9pJBT0LZID16_BGfmagcSH4X-8VxsCh20BzEz0-h08JaeE1Ej4FlxkHfrx4ShhaRbQ8U-pmabU9JPGugCQEFgctOiiRyX-d932XB1rP05im4F0rBrDJ6q7Af-3jxwe4rS0ufcm4GinkezpiOyW4FFOY36bfSvkahw5dJrQnkXBAxKhIyTNLOVGxBCJPjO9UuojpdjzeP74Lvuw149V-O8xCLGfBOhz2nUaZXaV1eJpqUI-PB-7cRjyJOIG66iO_pF6fwqlNfYulEZV-Q4HlNpq8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2769169015.mp4?token=Y5KlGvhkV_-wH3VYBOt0OqLo7ubzdWBOFtGFMuVTJH_2VSu6h5W3dP8HDT-dxW9pJBT0LZID16_BGfmagcSH4X-8VxsCh20BzEz0-h08JaeE1Ej4FlxkHfrx4ShhaRbQ8U-pmabU9JPGugCQEFgctOiiRyX-d932XB1rP05im4F0rBrDJ6q7Af-3jxwe4rS0ufcm4GinkezpiOyW4FFOY36bfSvkahw5dJrQnkXBAxKhIyTNLOVGxBCJPjO9UuojpdjzeP74Lvuw149V-O8xCLGfBOhz2nUaZXaV1eJpqUI-PB-7cRjyJOIG66iO_pF6fwqlNfYulEZV-Q4HlNpq8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: آیا توافق با ایران شامل رفع تحریم خواهد بود؟
🔹
ترامپ: خیر، شامل رفع تحریم نمی‌شود. این یک چیز وابسته به رفتار است.
🔹
معاون ترامپ هم پیش از این در اظهاراتی که گمان می‌رود بخشی از تاکتیک‌های همیشگی واشنگتن برای بدعهدی باشد گفته بود که هرگونه رفع تحریم علیه ایران تنها در صورت پایبندی ایران به تعهداتش صورت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442342" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 نتیجۀ بازی ایران-نیوزیلند را شما پیش‌بینی کنید</h4>
<ul>
<li>✓ برد ایران</li>
<li>✓ مساوی</li>
<li>✓ برد نیوزیلند</li>
</ul>
</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442340" target="_blank">📅 20:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442333">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG_bF05fsAruZsGCl_TZfc-Es-pf4zrNJQ0jfjEJk28bx7KkH3yo0BLsxdAhG9p5egxRJ2zvxa6PXdW8ZCIx-npAFeJOEPl0Z8ykJQMgogHxDyFWlBnx3AGqtX2UW3w0l6k9z6h7cMzq-Dxb0vZ1_s3zifTZ69lc2O1QNEQNvmT2GNxmPf8U9f68rMXwFPogH6bBPwoMmBNEv6aN8TFoN6lmWGET4UTfHCJZv3JKiVtfkZUq3w8olsaERNP2TtRbUVNHDBPmZc6xKesr29k6j4IJYV_KUFDgt53nBX3gScsrsHvTTvD9Pe_mRbXKwFJJVWX9kVKD4cML753VSJRRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwRCnO_m6EGrKVdMXbOHqyBTr0KNMiEkQ9IPndKDwgI_jM7n-02ZQrPqUQsXPeDpu7fMwsJ3vxaBh2cEtUOpyOm6HSulEQoYbbNVXVchmFWiJw5NWcl9f1wNfD3H_HEVs0s4WXovTokN7SS2UkAQiD_AqY7-KXGRHecw3hiMzLV4-pICRfkKpv3rsI2IvE-YNyI9eCyLS_JVkBA5upU3N7KLuIKzDLRVjR2m4G6voPz1t86H2uuKcMtNMUqzQEJYBJmTm2oL9v6LPpY-ukZWEC5zF6VGgUymSCLe9pX91qXw503f1aJUtzh-dV2p3MxJdoqpZDUiuy4v4b3BPO3Qdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fv8geIdFVDw062wxdGDMSmlf-XLBS5PDsQf_F2ZgFZckwr5AklMpqPubruWvAnfxMH-xVxMGdJd106JeAJ63EMEsX9VS3QfbheaNWcWpUsDjSKZcqVwlnBlcJYMbME9amvUxh37nf9fNgUi16jirXDzAXpbFzhe4jscUHvcMB7MFGFyT9Sq1nPBUJxbISOp926nJ2Iu3GFOnLf-7aiM4cgV4TBsSiNf7EDYs4TRf1qAiAkdl5UtgS6hMHuN-VkSj-CVtqAqFk4weqIupTbvSrO4uKVgfJIYegCBBmF5sxtXvpT11I7mb-vYJG8MAh8phhCxNrBOU99V7rH92LQqgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bppNjiOxRKi2pk6zvDMSr-HD7mB0zS807WtoVwVao-RpuDIkWntMNzjSIFhaj5wC06QYzPA3_vul_rBSicCx5eD4_sIjhSGsGdVYugkgPIGt8LDbng5WGKv23J1nGEFraoSObJpCRFXLbwGv3fGZnntrbUu_4ekd87cjbRkVms8o8JmuAwcrp56ZgCw-8F9tbfrnwbaTvlRzOnhemmXxukPpKJP5vkJQ0WwnKSmfC272IeggMa3Nbm92MQNYe3neQuB3RCYc-8u06zLipRIVIdtAr4GvIIrLFfedjSczp_bKNM7Ro4g-KntKIMPnokPvQhrN44WarW1ztIrIYIlXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYqBVyUyzguedUUh8jfNOuZn7cwGSkw7bIB9f7OC0KpjFVoknZoYCp6mawIuf5VQ9QYpgBWJM8HycyJN_rH5gqVb7u3U29Ga4438R3ChtY7yaAMLay-VDpw0x_BPgLAv3g5OwtvdhW3Ie3FgbVuqKgaW_ubE_W2MdgJQDSvLG_ygMqxwuwY-rFeq2iuILzvEtYbHmZwbg0u2IG_4eIci-ewwdUAnLrPoSqZyn6yjgiZ-rxplbaqbkZh8C3fWKJgIrg6r6oPseUJri45hte5OPkV5y3rG35Z8X8BEW178BEUzlWqws3K3c3hAKTkNZ2WdJk13fWhI7v5wDZt-alYbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7QqO7sqv1AI1LSfNAhDPBtLp0QkTyldemjEDT_U2PgkLApBN6OGh4l1TITGJyecbT3QJ4zKJtQq_UaT3CQ04vUIRSUgZR18451ewVnoUe1EFeGQ3ijZ48fhwtk-lfhbBrT5J29Bg-tC2xO1guMWBRA-MIvb7LA6XXMPtfIX4whq2beqVi1f1VvEgm4KviJH9n20L2bFqVPXBo8-vUcKp0B-JR4RgEgpZ1XdX01GnXv8_CU9WcGK6g_VmwQNXr1OLHqEBhineU0i65FuMjeuT_qyMBpH-NJ6b9d_mOkCKyWUCryCllAXFcqMV5oFyzvPi7V9Pmh39knvuzhwH5k78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6n_ALNflPVO3TW27CiNGZH4K_UXuMK7HBaE3ikme_R7e0xseb5EYMNyMaGW30k3npSKeCZzfeN7ukmalHNBE06Rv1wvThHIdRpzUb1R1-iWnIb_tWgvJiroJ1E56Z1Cn09Nw24a3a85c3ulb_dU14n-F5StPSeykQ-tchsTIZ_QlyXgHYE2S2IY749yyoA_cyP8ngv4tHtdmGQueZ0u0LcQ4ZERo8Fteazsc-rOzRl_DrQWcvWb21yD3HoM5kUpg0p5JwNU0yuUZsYJLxjeJM6B0SQCuF-Oej-ruhkoK0Uj5dK4hNaRb2Y1eJV0WDGgzuCFYSdY6UEXPliOxW7ugg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سلام بر محرم
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442333" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442332">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b30da167.mp4?token=rP8II9E7mCFREXtEvGo3rMqrtdx_cFnCXH7vyPzNQp088rSM3iQA3rpmHUBa97iJPyf6KoSJQHKfxluVZc_mBgAexUnze9T9CZ44LrrmjTpf7CrbVIQHTKuu1nRl_1WsBgPZoxwYYpR-qyREmyC9fBDSh_-KXb1kpbCRZ8kLRg6dVpZMWlFc0vR9xaFlh-WH7bmLkK7TwS-B-TlKmXMYA5gX5sxFY76B6nO7-IhLLanQ5UcLOdxU9e-67XEqtqf81OvkmbmRItni7JW_NlV0g3VxQtNlhYwEbhGuTmjerl4VvRg2JCSgBPfpk3GaOK7MxaemzPLL-t7JaYcxYrRIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b30da167.mp4?token=rP8II9E7mCFREXtEvGo3rMqrtdx_cFnCXH7vyPzNQp088rSM3iQA3rpmHUBa97iJPyf6KoSJQHKfxluVZc_mBgAexUnze9T9CZ44LrrmjTpf7CrbVIQHTKuu1nRl_1WsBgPZoxwYYpR-qyREmyC9fBDSh_-KXb1kpbCRZ8kLRg6dVpZMWlFc0vR9xaFlh-WH7bmLkK7TwS-B-TlKmXMYA5gX5sxFY76B6nO7-IhLLanQ5UcLOdxU9e-67XEqtqf81OvkmbmRItni7JW_NlV0g3VxQtNlhYwEbhGuTmjerl4VvRg2JCSgBPfpk3GaOK7MxaemzPLL-t7JaYcxYrRIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از آسمان منادی ماتم رسیده است
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442332" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7DDD7qxezOsfjS-t9ytMkFXwj8f8z0Vn-FF848tF8aaVP_2wqVzzKAW0_GjW9l_ayxV3uIfkPCQH-xpuxMsHa3N4fhrqLHvx9Wchp_VvYiHkM-4_DMdlVstC22uamngj3dWyUB33rqfuTKjHTs2rlyu2KcSWbpPkUtgH4pJ6jQwF1ZnfN88tULPuRzmAebWdsin-gAlXKUP4xPc-EPo9NKnqc91cy_W9Y--YUbdLLE9qDeynEhbNynbfn_8xQ6se3urtVyGuocVjZH-2xHcr4mjCsT9oGMlnhrsRL303oj7l8gZaUVqhKrmr9iomwZDnozBqOelUuortcIHwiREdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق ۲۲۸ ادارهٔ پرمصرف در آذربایجان غربی قطع شد
🔹
شرکت برق آذربایجان‌غربی: برق ۲۲۸ مشترک اداری متخلف در شبانه‌روز گذشته قطع و موجب کاهش ۱.۲ مگاواتی مصرف برق استان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/442331" target="_blank">📅 19:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442330">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDm70728H_HN_ZAo6YWiy4nil_fSVq1ikUypdkjxFPRFW51hColcm5W1DuBUqn-oIGnokjHLJKDNTTItho9g37O9F5zv917swzuYsHfaMxvsHFUd3qXBwptGio6euCC81Rhjy9TB8AkeKuKAh0pGbsJpfq9AAJc4hWDxZkCMwncumJPuLy5WUpQ6A41CbElbm0ZpXuUmYN6sYXMP8TgbsmtZq17l0Llt3CzGDfw6A2tJ2pn1jbUOUyUSB0AmqxUMBokHw9jxx_CJnlh3HBMa1EOGY9oo6qvBobbQvkCCwQqoauMeHLNgghICtFa2fzuwadiYE35DmJrxoTCRwj5oJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دیدار شهید طهرانچی با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/442330" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442329">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bc485bd8.mp4?token=Tz8F7nKCc4i1dWJr-s36niZve4L77QjJpbZBfFc-NFShgQZWA8R-zJDiFoY6O-58u6TMkLCv21dHzAXfXlx-8EfhQf6ZE7WojIv7UpcatURnfPtW4OXSdZ9m0EdRnub9w6Sxma5DefuPR0-OwEXbsgdbSOy0HHPt_z8eUtMnDqunxC9ZO_z203jCRqYnOPXG-oBD2EXOO-hZB4F7eL6GzEkNBtgDLScL4oN5lrNS1ujmcd8bKMlS9O_IjbzuhMlaxwS1A1nbw_5zj3-VOguVXkQ9dOLkPsvTHeI46CNiI-kR-sjlCU6Ort3Npru4rGpbkp_C2p5IBMFIIdpD6V2Ygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bc485bd8.mp4?token=Tz8F7nKCc4i1dWJr-s36niZve4L77QjJpbZBfFc-NFShgQZWA8R-zJDiFoY6O-58u6TMkLCv21dHzAXfXlx-8EfhQf6ZE7WojIv7UpcatURnfPtW4OXSdZ9m0EdRnub9w6Sxma5DefuPR0-OwEXbsgdbSOy0HHPt_z8eUtMnDqunxC9ZO_z203jCRqYnOPXG-oBD2EXOO-hZB4F7eL6GzEkNBtgDLScL4oN5lrNS1ujmcd8bKMlS9O_IjbzuhMlaxwS1A1nbw_5zj3-VOguVXkQ9dOLkPsvTHeI46CNiI-kR-sjlCU6Ort3Npru4rGpbkp_C2p5IBMFIIdpD6V2Ygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسم «خاورمیانه» از کجا آمده است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442329" target="_blank">📅 19:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442327">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/064ed5ee18.mp4?token=mXPGoNG7gJZpFVayCL7_zIxZ9rit2U49Z1Tgi2zwmSGLnQBq7cueR7r5T3nm5CO9jPMw6sKCxCxZ8Cb8xPG1AKUkBdq7Ef0t-YjEaL4QFnKs9_hZcjawXJigKcEPUOG3zVciSNmwI4Ko7sEkE-mR-0G8mQOBqVnNNRG_VXgVRF1kZtRjs9xUw63dVLvuEHIS6a8AT_s5MXgEp_vdAzQ2Muq15-yKJv805PhGiF4ICH3VD0vwmKKk8FkVMy94Wtd9Iay8KmEjw9uRgQdbrPMY8A681oBF729fcF4dpDmPte5naktBYfpQ1ODczhqXRIR74KGnTwaDwkPfgoGNbV1-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/064ed5ee18.mp4?token=mXPGoNG7gJZpFVayCL7_zIxZ9rit2U49Z1Tgi2zwmSGLnQBq7cueR7r5T3nm5CO9jPMw6sKCxCxZ8Cb8xPG1AKUkBdq7Ef0t-YjEaL4QFnKs9_hZcjawXJigKcEPUOG3zVciSNmwI4Ko7sEkE-mR-0G8mQOBqVnNNRG_VXgVRF1kZtRjs9xUw63dVLvuEHIS6a8AT_s5MXgEp_vdAzQ2Muq15-yKJv805PhGiF4ICH3VD0vwmKKk8FkVMy94Wtd9Iay8KmEjw9uRgQdbrPMY8A681oBF729fcF4dpDmPte5naktBYfpQ1ODczhqXRIR74KGnTwaDwkPfgoGNbV1-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب از عرش خدا بوی محرم می‌رسد
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442327" target="_blank">📅 19:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595a7e8117.mp4?token=LQVPwsQvuAfV6NABnxqbGFztVRVcW-83BmPKaADzO2snOMnHEzT-_Nvg-JoweafcZWqT1DslTXbugfk-i_cOMwdEV4JujJrZw9ahlimiFlw0wSWOZRhPshJMATZF5YqN6tcOIC2eUR575bEA9JGUPozyW-JZP6HOX68gH_TpTzXdwBsbnHaosbf37U7DZkpuhKG05-gya598v75j4NVjdHOWjZMHLzkbkSbdXbrer162Sq1HjHafQPaZEsgyN4FBlod511COvomivHbCglyzzjXUuVGiHzLIEJUs2C0HHJ9E2VLLoxkpKzThY5FPWPYhgOmW9VmAf0F8VCCZ31g8aYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595a7e8117.mp4?token=LQVPwsQvuAfV6NABnxqbGFztVRVcW-83BmPKaADzO2snOMnHEzT-_Nvg-JoweafcZWqT1DslTXbugfk-i_cOMwdEV4JujJrZw9ahlimiFlw0wSWOZRhPshJMATZF5YqN6tcOIC2eUR575bEA9JGUPozyW-JZP6HOX68gH_TpTzXdwBsbnHaosbf37U7DZkpuhKG05-gya598v75j4NVjdHOWjZMHLzkbkSbdXbrer162Sq1HjHafQPaZEsgyN4FBlod511COvomivHbCglyzzjXUuVGiHzLIEJUs2C0HHJ9E2VLLoxkpKzThY5FPWPYhgOmW9VmAf0F8VCCZ31g8aYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقابل طارمی با نسخۀ خشن رقص بندری
#جیمی‌جامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/442326" target="_blank">📅 19:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXZjw9WmhKN-qMRG5UvSREEQ9q1qsAZp_qx5BqvC_55bnJLHrEPd7GGzKXJ0xet5Gy7bWDNt3Ib6una1gA0dzn95c-0pdtlXIgcrWNRA5uQtVSaEAHyAgJvkj9xrJLDaoAG71sj5sBOnGaprGwPOmm6_5ews97QPB9CQlQVQRSq3MnL8mpakeoDqT7rQ4Drsmsg7sVay6Mj65Rd5ofvlwnpwvETVV3s4BUOx0V7fAGsu-m9cw9kP2rcuK_evaw1aGuFf-L8U7y5MN-evdIosVVFNYKgwo1LGh9VDa4qt2a7NqJHxWmBVP0od0Md81x58Yh_WitZ4JeD120pGx4ZWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: با مقاومت تاریخی ملت و رشادت نیروهای مسلح، ایران گامی بلند به سوی پیروزی نهایی برداشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442325" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442318">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzC-YDQ7v3JFsigMBpi7qs9EbOF_QhznKH0siKkUWLyOxhr0Lu-pzLxOyACnAEhr3YQvPmNGZCx3SDQv3ldxASiSdFXA-pK2WUDSfRGhspYCB66vMS3B_wsPBuN2C72ELugDig29dV8jHkLMOWbiOgPOXe2wOw2RciDiNkym9EmCK47WXGLkwDeVNA0nGqAUeMXEhsUiaE1Di_a7fmHWp5b13o8vsZRvCvAo_PfIcmO5e_JqQdBxQ4v2esM9gpk1DkbHVYYti0uS5RxV-0_R5xcMLszibVeD0sl4shyt0fsSwy_iYopO-AZdka5lJi9vAhH9wi-vWD0HM9ibFdk3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVW0eVEWuf2XjjP6SJi25fP3B99w_MemvqaAziJeAiyJf0pUffHO8VMLUbYOO9FDQ-2IvB8Yuu__Py3Ms9wdPM543UHyeJdZ683bOLf_ThHVi_FMAdvxJfwg33E97rse4AWJpClGA_gGTJDKTQcAa_CEeJKznYTlKBvzxmzLBi7Di55NTwPC-YbAnf-mcqUKQfihjF_oq7YWR-xKokcSIp6PpYlQs4gpG6HNwv088KjejOdYekHFQ8f1Wmc3OLVZB_-kUi2710bGgqJG2Rgc_5mcoRA-JgZxBLthzXo7Vf6yRx3NKc4c9T8XeHtz7M4DdQ9XfvqS000TsLqXGN9Ebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfwxM0_ZfFp5-S22x-a03ORqQmslUxSQS_5xi57BqhHH9LIlCgwS3MV-SbTepXrds9qv9fLkIP9dT6zXvBZhdY6uKrX9BGlQsKEI_U1cG4_OfTRjQpiHxWNuwSqBiCi6VsViECu61IuKgjyJEJyWdJjsOjFvQcLca9sQK8rWx6Z054rc2SIc6tWQKGolluFzZ0vjpIKEJoPbqQhdXSy85Vq-Z1k1AtCj1vEBuZdZq_IcAMLHPissYD393WkfXWmPeHza9pRQhWxxGKxjTVRL3j02mtpbzzdCxajCC4WJNdCrAlS4t8ICG8WpvPbAqOGWfSTKG356pangrlV-czzPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGSkVrz6YEMZZ7e_9n38PfsYEM0f__jGSnwWDj14q4lN8alHRnBKIfct4mv6xXon0rIY-ypVcr7mWkQt-rDRhfQ1v3g0v63Sv0sJmBGxep09BvQgmMkXe4RUWyPo5fUFf-fEgZ522ocG8GnvsdVVwMrMb2bng-CBQtXBHPBcDDHJNtNtFUCeckiC-mnM32Lziq6uRMwPALzRHLv7PwXWvvmLPueZSqXvQ3nUxW2V2ecZqa_4pUOwoyj_0ZMyWE1Rnkpbuyy5y8eleZ9UKnGk6w06WjcZTQ5ewt0OOWINuiQfERs9fccw3bvR-r7PMySMnJTKA8b0RT3HPAgbdaa5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUCLZ8RBm_NQV5c7n0yMfB4hPRgcsDYBR13LhmW4UTRo9ONHBtogpKLWvxKgrK-DzNr8dJmMyhvtuGf_g8B5cRnkZHdYUJ_TmyDUVqpF79hmjl3BAcB5n4nZSndFu8SCp-eMhcxBdTY_De6TjZEapYTe8YNCwFOtXJuBPmnBKVsEC4wsURGGrDN1j5bvwa5--ptDjEf3dE0BMHwtx4PnaOqa7EVp277GZZ-PKZDjXTOqr20oMzH0WJZczx3i89vqeBMyN_yLnFbD-X3xxiWQuoKzfU2ZyMFXeGQwAIjz4Onl9AtfACIRVESwTeUhQytPmKCYp3MsCJ351y3VeAjSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zjm4YT7ODKR99VkrVBZoauf1cblYlQq447fEb5024GNsNmfis1gkKm0uaG0J0xfNrZLRLxoHIpQYc--sstfcqes0YqNGWlKEnoqs2Hs-D36PQzjALlZuotOe_AWb6PamdXlh206frkrRe16iBYiErDry2bhypUb1WuvtrHUfDcG79WgfUHRdYfE4iFPqgdFtbfog8l7_w3i7YjsSLOXPLrgm6jKS6FATgu5aOjxRpc739qfJ2XHBZai8gxp6fjcW0TBvziRduBvFCcdo7zmGekFBwLmeFmoRF1dIOMCkoKIkGzpwK5KSGCVeoHioGZMC8JCaEpOsSIvOPUtKXnA8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxK-Hivg9xv5oVBw-yOlTNe_mwO3xIMcjpu_1nHCVDPl1mvuuHYGcUyp3YaGrwlDvfwvuR_Y8vIC5XtF40tjgxbCXAVOlyjHv9oOds-fwbQY10t87TaYmE0mo7qizryQNwKQ7vG1ROtiJ1ZpxN4jBiCcXX6pyBMvqPL044c9zm99qKkTXKIebiFVNVnWvwl0-Ju_JWSwFHKHau5vOoRpgQnkFOaV7lJz99OD5z8uJGnVC25f6goDGMlyy0zENcGotPu2BxI-K0KYJ9JLaECrIp52SR-uPRGmAPSDlqohIrY13yBmNtr1RFvgoi1vKl1BiSlyICRmh5xl-r8cCHfilg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفره‌داری ۱۰۰ روزهٔ مردم یزد از مدافعان امنیت
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/442318" target="_blank">📅 19:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442317">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3a877e1a.mp4?token=UyTInMFl1PtBjgGolNsZK2TrTm0tHFQ2MXbrzWU2zJlVsTFpVygdQEAxFtcXSr0uFVf36TsKJjhfoIg-bMu1tWHTsQIzWUjOBoJ5542t0G_5LhLEmM6n6sr99Wtk-mz2Jv_2RHoxDrGWA16Al2qYoTkf9pnIv8YKj1eb2KHZwivpzUr8vdABA0TUVEkr_KjyQCQvUW2E8osObacQiDSOWbZo0wKQuHsGkZANguGbbAyZy2VjKcQhMSFhGBoUPtA0Fa0Vj5mjTQQbdUsixB14t6ZZ0xbVjBDam09DSfaJfOQmfWJNtmXXKevJWuffrTbmYtDt3nimzOdRwhEr_n9c1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3a877e1a.mp4?token=UyTInMFl1PtBjgGolNsZK2TrTm0tHFQ2MXbrzWU2zJlVsTFpVygdQEAxFtcXSr0uFVf36TsKJjhfoIg-bMu1tWHTsQIzWUjOBoJ5542t0G_5LhLEmM6n6sr99Wtk-mz2Jv_2RHoxDrGWA16Al2qYoTkf9pnIv8YKj1eb2KHZwivpzUr8vdABA0TUVEkr_KjyQCQvUW2E8osObacQiDSOWbZo0wKQuHsGkZANguGbbAyZy2VjKcQhMSFhGBoUPtA0Fa0Vj5mjTQQbdUsixB14t6ZZ0xbVjBDam09DSfaJfOQmfWJNtmXXKevJWuffrTbmYtDt3nimzOdRwhEr_n9c1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گنبد حرم امام رضا(ع) به رنگ عزا درآمد
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442317" target="_blank">📅 19:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442316">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4qi24URBn6-NsFSTWa80WN8hWwI8rlcsuRP91Lbs_uOBqCqOw3QPMoTmcjW1YUR7Phw4Z1LV5_-fuHyZXm_KAbnCrHTB-J85GYV5YpmFLgbj3ceVbhY1LgnuZpjpRCWwzHpC4zUP3E7OEcCIzIN7e5oLRckUuI76GnI2n550137KQZBRO4QXve3oXSMtLyZQGn3S_qdyNVunFxXqgQkR_a9Yf8DxLr3n4JfrYK7YyC3qU0_IgZhT0bm73LK-q5OclbDn4ffklDi089iMvd_kDOV1aXBirXLD7aLKIizEyiEEqHFi8_lBdAkY7qQGHIIKXM0JULiyCpaS4AVBbel-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442316" target="_blank">📅 18:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442315">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57edac52d2.mp4?token=Lyv0pUhticy9aVM6kDYk3aq_LSCPYpuIH6YktVHtfK9WyF-bwMtZrdHuPPHMkv5fCDmjIVsEv_42d5XYlqJAj8pEFQ8Cvz6bfpJMxBaFfCNIcVNPCcnjHdC9ozWl2wYx5TY1ravV3WZfyWASFvxDjfRQ4VVgvfy2dAD280BkiuHKHJzKe17x7VuPFx7sPnHPAFNAx9gW-HJTeEdOU2mrfhlkHougBR5QIxOs4pFYuvr0OheLT7J9vHawuPDlDP7fSVpioBpNVOPadHmCLi-qc2s0EP98xBKYTl5LcTo8xJYweIxfhPD8aIpECoxSrE0pPl4ky2wglk_EKIR-QkTBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57edac52d2.mp4?token=Lyv0pUhticy9aVM6kDYk3aq_LSCPYpuIH6YktVHtfK9WyF-bwMtZrdHuPPHMkv5fCDmjIVsEv_42d5XYlqJAj8pEFQ8Cvz6bfpJMxBaFfCNIcVNPCcnjHdC9ozWl2wYx5TY1ravV3WZfyWASFvxDjfRQ4VVgvfy2dAD280BkiuHKHJzKe17x7VuPFx7sPnHPAFNAx9gW-HJTeEdOU2mrfhlkHougBR5QIxOs4pFYuvr0OheLT7J9vHawuPDlDP7fSVpioBpNVOPadHmCLi-qc2s0EP98xBKYTl5LcTo8xJYweIxfhPD8aIpECoxSrE0pPl4ky2wglk_EKIR-QkTBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای اولین گویندگی مرحوم رضوی  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442315" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442314">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش‌ها از وقوع یک حادثۀ امنیتی در سواحل یمن
🔹
براساس گزارش‌های اولیه، یک نفتکش در آب‌های ساحلی یمن هدف قرار گرفته اما تاکنون جزئیات بیشتری منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442314" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442313">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خداحافظی با رفت‌وآمد بین سایت‌های دولتی
🔹
وزیر ارتباطات اعلام کرد اجرای طرح «زیست‌بوم‌های دیجیتال دولت» از ماه آینده آغاز می‌شود؛ طرحی که قرار است خدمات پراکندۀ دستگاه‌های اجرایی را در یک بستر واحد تجمیع کند.
🔹
با اجرای مرحلۀ نخست این طرح، هفت زیست‌بوم شامل مالی، مالیاتی، انرژی، سلامت، تجارت فرامرزی، زنجیرۀ تأمین و مهاجرین و اتباع به‌صورت یکپارچه در دسترس قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442313" target="_blank">📅 18:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442312">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8535b8b7f8.mp4?token=EjxpZ2Y95T2k-4lfD-5siJUV11pJi_IBdkx_ea21tYrE8lc9MJGf2yRy6VErqZ-4zXXqyMbq1owp-tp5zTG3PoK3Ay5Wo_eIoDHm7_QmPTQIA6Fwpzit6nE57yYXe0EtJLaM69c36FKEEfFNd6NRMKiOM6wamje5vD-JS3e-fGt8kdvR0t8OMUoXE5ULb04RAbhe499gAVeNYZ-uM6rOcpk4J4JdJoEUBN6Yd4__JzkhnOzwksOV_OYtXNKTVmlCIL0pcWiaU-2hlSmGP3ONolLJLEfY-__J2wL4vXgnNzpiIKr4aLhdm97BglBgreMFYEAESwbpzJaGwy7ffE7S4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8535b8b7f8.mp4?token=EjxpZ2Y95T2k-4lfD-5siJUV11pJi_IBdkx_ea21tYrE8lc9MJGf2yRy6VErqZ-4zXXqyMbq1owp-tp5zTG3PoK3Ay5Wo_eIoDHm7_QmPTQIA6Fwpzit6nE57yYXe0EtJLaM69c36FKEEfFNd6NRMKiOM6wamje5vD-JS3e-fGt8kdvR0t8OMUoXE5ULb04RAbhe499gAVeNYZ-uM6rOcpk4J4JdJoEUBN6Yd4__JzkhnOzwksOV_OYtXNKTVmlCIL0pcWiaU-2hlSmGP3ONolLJLEfY-__J2wL4vXgnNzpiIKr4aLhdm97BglBgreMFYEAESwbpzJaGwy7ffE7S4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام رضا(ع) با آئین اذن عزا به استقبال محرم رفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442312" target="_blank">📅 18:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5HdhaFTfG1tSTyBNFJEgR9mtJ6CZ0_P-MKy1yCF0D2dcP7jxBYhNA_JlYhWkSw8ULjHQ7SisypAy_g1MXfSqnln-0innFSeL5z9sQrnv18_17OlyvNtUW97Or-q7QHp6KuiGFMzbyEuBDO24aXuIwjRlO7s3t0MEqPuZrGKc6jA22JPtdq2PgE0l27mCbBbK3tasc9eLo4NIK32m53ri6c9zLYc4Xk8NlUHN2F-1y5vnT0aeLfhIryr4EI2eSA1cQnMk4hd9jqC9SHKQ59167G-LfVSJiRKc8WFAI4h7JaJxROzTzR0ZZ0gW76Oc6KlMS0qSffzdAJHF2oVYbXLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اینفوگرافیک | روایت نقش‌آفرینی بانک صنعت و معدن در توسعه زیرساخت‌های انرژی
⚡️
۴۱ طرح نیروگاهی، ۸ هزار مگاوات ظرفیت و سهم ۱۰ درصدی در تولید برق کشور
🔹
بانک صنعت و معدن با ایفای نقشی مؤثر در تأمین مالی پروژه‌های نیروگاهی کشور، از اجرای ۴۱ طرح در حوزه تولید برق حمایت کرده است؛ طرح‌هایی که با ظرفیت ۸ هزار مگاوات، سهمی ۱۰ درصدی در برق تولیدی کشور داشته و گامی مهم در تقویت امنیت انرژی و توسعه زیرساخت‌های صنعت برق به شمار می‌روند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442311" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt5IAQ6unVBTTVEcM6tymEaCbwCdhHfmoXxvJ55cLxMkTRKjLdtzDlhgU1-mxcKS6TIDXaS1DYot44ibtY4ShPz104mEB3Umoae8qZmgSx2uH4qIjvN56SXDQQSLkK73-Fepc8QdaJ3FLGbEGw3oOZTJ_9R5vl8pYJfTKSXFeSEPM0PxbcBt-5XnfbWuEW3Ii8OohWD228gVKbCdQMIgusoCBlONPDX_O8ZueN6zirfRWN3UuwhAtihMvABF3Y1AUJsvb0VDQzj9jkVYIoZPKmChleHQRh1wuqv31ic5YiCzelI6v9FMOS57NcWZGJK8nZq4SNDYsyb4aW4igVphXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در مدارِ آینده؛
🔰
دومین شماره مجله «عصر مس» منتشر شد
🔻
دومین شماره از دوره تازه مجله الکترونیک «عصر مس»، روایت صنعت مس ایران، منتشر شد.
🔹
به گزارش پایگاه خبری مس‌پرس
، این شماره با یادداشت دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با عنوانِ «مس؛ روایتی که باید گفته شود» آغاز می‌شود؛ یادداشتی که بر ضرورت روایت‌گری ملی از صنعت مس و نقش آن در توسعه و آینده ایران تأکید دارد.
🔹
در این مجله، با بهره‌گیری از روایت‌گری، رویکرد چندرسانه‌ای و طراحی تعاملی، موضوعاتی همچون تولید، طرح‌های توسعه‌ای، بومی‌سازی، مسئولیت اجتماعی، ورزش و روایت‌های انسانی از زندگی و کار در صنعت مس مورد توجه قرار دارد.
🔸
دومین شماره این مجله به تاریخ خردادماه ۱۴۰۵ را ازطریق لینک زیر دریافت کنید:
👇
https://media.mespress.ir/d/2026/06/14/0/15451.pdf?ts=1781420523000
#عصر_مس
#روایت_مس_ایران
#StoryMag
@mespress_ir</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/442310" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/442309" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442308">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۶.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/442308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۵.pdf</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442308" target="_blank">📅 18:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442306">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGM5FrAzG_Opho9VhPXEyiOUdgxuYx6UBIdsbavAlkbRAPXOA2ijv5WdUeTFFuuj93oqhco1qTMAt572ZNHBY6Dt8B0H_A1YbPLDA84HXfBbhGuNgw4WEydVtUpAdVkG4Ezt7rwtwL-TKfl0IFFwfGfJz7RLY4eqnC7jc4KjNmZdwrbrVEVHAl7MHfFqt8ALhz6oGWaptD8l628V2Ouw9JtCiUHWAWCs8lyfst8XuzS8yipvaVBHs34JzFokBzW5yB4WVxuQSKzl-x6u6DbgJXOFyCrc7Zs5-oRrDc8sVAgcW5k6LdlfbN64SXoWJ_X7zauCCX8h5QzpDdD4ERFPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تو به یوزهای ایران در جام جهانی چیست؟
🔹
ساعاتی دیگر تیم ملی ایران نخستین دیدارش در جام جهانی را برگزار می‌کند؛ مسابقه‌ای که برای ایرانیان، فراتر از یک بازی فوتبال است.
🔹
اگر برای ملی‌پوشان پیامی دارید یا می‌خواهید حال‌وهوای خودتان هنگام تماشای بازی‌های ایران را با دیگران به اشتراک بگذارید، متن، عکس یا فیلم خود را با هشتگ
#میناب۱۶۸
در صفحۀ فارس تعاملی منتشر کنید.
🔹
همچنین می‌توانید پیام خود را از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال کنید.
🔹
در پایان نیز به قید قرعه به ۱۲ نفر از شرکت‌کنندگان هدایایی اهدا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442306" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3d4695485.mp4?token=FOZLBY08gZBqZ8oHZ7qCgSPFkURlxeNy_Fdn3xsLV2TuyhPZ_qT7pDxAn6ntOsxrLLbxCIneWsP-ptwZB5YtC-UFzEea97fjkIGwu5LB8_rgo8MbqwYDg7JBpaClrN8FqceE6FsRfm6BXFbaEak9Pqgho2KTUkCo0T3jHlmMUCsnNxP0tiwsdiiIgxlNUKbgaLdmTrJ9wWfiyJ78g9DMjhpxA08pkefUGgAGRfECLuvFpYJjNFaZFRwA6UWR8XEPX2GlnhioNkRZJcfa-pgIg6P8UygDpxfC-yI7hcFCVDCP4BjfmNXlEDErlvJEjI6up8q5MAj4rtayajO0HRy4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3d4695485.mp4?token=FOZLBY08gZBqZ8oHZ7qCgSPFkURlxeNy_Fdn3xsLV2TuyhPZ_qT7pDxAn6ntOsxrLLbxCIneWsP-ptwZB5YtC-UFzEea97fjkIGwu5LB8_rgo8MbqwYDg7JBpaClrN8FqceE6FsRfm6BXFbaEak9Pqgho2KTUkCo0T3jHlmMUCsnNxP0tiwsdiiIgxlNUKbgaLdmTrJ9wWfiyJ78g9DMjhpxA08pkefUGgAGRfECLuvFpYJjNFaZFRwA6UWR8XEPX2GlnhioNkRZJcfa-pgIg6P8UygDpxfC-yI7hcFCVDCP4BjfmNXlEDErlvJEjI6up8q5MAj4rtayajO0HRy4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر امام رضا(ع) آمادهٔ‌ عزاداری سالار شهیدان شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442305" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd29612d12.mp4?token=aUNHqTKnk4roQREnzYd5wqfQgeB9XyEttXwmCYK-544keT6_Pc3aZGgKhIXQX44B3tYOfxobvwbVfbNBaOtmquZJq0-RWR8UVvRuR8uDr0iFN8CoR-sQdv-NFyS5RDDO2k0EVwj4RtxI3mVbGu-GnXHwGNUQpa0rz9wMAbrAhCHAOznZRiDc7ZdTNmM1WFjx-r0Bu6oE-vSm_3iaTct4k1z7KoLs-D9foNmkKjN1kg7O1YeMxj7uH9UU7JXZR4oFqbhh36urL5KE6Va5tUrAerb26zyuO2Fn6fllZxKDR6UVriSi80rgXVtxO1SOfxN-QpNvx4Qk45gwE4D-9yQ4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd29612d12.mp4?token=aUNHqTKnk4roQREnzYd5wqfQgeB9XyEttXwmCYK-544keT6_Pc3aZGgKhIXQX44B3tYOfxobvwbVfbNBaOtmquZJq0-RWR8UVvRuR8uDr0iFN8CoR-sQdv-NFyS5RDDO2k0EVwj4RtxI3mVbGu-GnXHwGNUQpa0rz9wMAbrAhCHAOznZRiDc7ZdTNmM1WFjx-r0Bu6oE-vSm_3iaTct4k1z7KoLs-D9foNmkKjN1kg7O1YeMxj7uH9UU7JXZR4oFqbhh36urL5KE6Va5tUrAerb26zyuO2Fn6fllZxKDR6UVriSi80rgXVtxO1SOfxN-QpNvx4Qk45gwE4D-9yQ4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۰۰ خودروی جدید آتش‌نشانی‌های کشور واگذار شد
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442304" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه برای کل منطقه و نیروهای مقاومت نیز افتخاری بزرگ به شمار می‌رود. جزئیات آن نیز ان‌شاءالله در زمان مناسب ارائه خواهد شد.
🔹
لازم می‌دانم از اعضای تیم مذاکره‌کننده تشکر کنم؛ از آقای قالیباف که زحمات زیادی کشیدند، از آقای عراقچی و همچنین از اعضای شورای‌عالی امنیت ملی و همۀ کسانی که در این مسیر نقش‌آفرینی کردند.
🔹
در شورای‌عالی امنیت ملی، پس از بحث‌ها و بررسی‌های مختلف، تقریباً بیش از ۹۰ درصد اعضا با این روند همراهی کردند و رأی دادند که این اقدام باید انجام شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442303" target="_blank">📅 17:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f89a4ac.mp4?token=dcwgFkAgY11Nz3H7vZglrubw24HMKN7R5k8KnL786napt7qagvOsi6wDbfgVyqIjAHULUHymA0Gbxg9mKNbYA7NMieK71VJ5OshKAdpIra1CEt2_q_Aht54fMHlTYipf0LehvvJZkxAbxzJHlWRuHtHfA_IprrwdCU6S6pbuHEsHQIDbyCc7mx2koB-kamL5VrOhHp1e5r6iO-vizo6u_L-T02_2CK5qMThbZNJT5vyd_N5kOkjF1JSC6Vq-6khcThifWi5ugC5IvQ7RjvJVV6jTRWBLgQIsn_ICjLPo_f31rOnmjWn2icsToGsl6BGfOgj3MGtepZWqJyLrDJBjDhboXxP4mDi2ID5pBnEnxaIyecvxPx2fw4YP_36JRWv8W8L7xhoP4qK7mEFkbKDbJJqOK--WNCmmBt07S_-k7hgWKji6G5gAyF0uAAkBrpgYs8s4yJ4bg1g8PmXZNdxvWKUXovZftq-rlE8SFnD09L9AH2koKhh0sEPxkZ2r2kMoWK6LyOBOQEDWxA5C_KnqVoUh0IQs2oMnrmj-8ivyzxPNf62mIFrR43AP5xlv_JmiPCjbgnnF8joKc4xFb95wq23KKKzQeYvAC0RG-CAmQMPe34a6ePsLOsl1meLe850lWaeQCHuW3aZHDBVIe3KrGSilfGEJo02OAtJRvtTZeys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f89a4ac.mp4?token=dcwgFkAgY11Nz3H7vZglrubw24HMKN7R5k8KnL786napt7qagvOsi6wDbfgVyqIjAHULUHymA0Gbxg9mKNbYA7NMieK71VJ5OshKAdpIra1CEt2_q_Aht54fMHlTYipf0LehvvJZkxAbxzJHlWRuHtHfA_IprrwdCU6S6pbuHEsHQIDbyCc7mx2koB-kamL5VrOhHp1e5r6iO-vizo6u_L-T02_2CK5qMThbZNJT5vyd_N5kOkjF1JSC6Vq-6khcThifWi5ugC5IvQ7RjvJVV6jTRWBLgQIsn_ICjLPo_f31rOnmjWn2icsToGsl6BGfOgj3MGtepZWqJyLrDJBjDhboXxP4mDi2ID5pBnEnxaIyecvxPx2fw4YP_36JRWv8W8L7xhoP4qK7mEFkbKDbJJqOK--WNCmmBt07S_-k7hgWKji6G5gAyF0uAAkBrpgYs8s4yJ4bg1g8PmXZNdxvWKUXovZftq-rlE8SFnD09L9AH2koKhh0sEPxkZ2r2kMoWK6LyOBOQEDWxA5C_KnqVoUh0IQs2oMnrmj-8ivyzxPNf62mIFrR43AP5xlv_JmiPCjbgnnF8joKc4xFb95wq23KKKzQeYvAC0RG-CAmQMPe34a6ePsLOsl1meLe850lWaeQCHuW3aZHDBVIe3KrGSilfGEJo02OAtJRvtTZeys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم‌داری سرتیم حفاظت رهبر شهید انقلاب از زبان فرزندش
🔹
فرزند سردار شهید سیدمجید طباطبائیان (از فرماندهان سپاه ولی‌امر): برخلاف برخی تصورها، امکانات ویژه‌ای برای تیم حفاظت از رهبر شهید انقلاب در کار نبود و پدرم حتی با راه‌اندازی صندوق قرض‌الحسنه تلاش می‌کرد گره‌ای از مشکلات همکارانش باز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442302" target="_blank">📅 17:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt9M5OVX5wgHub44_8xhmMQYYcWEUGesfzEkVULvMMOhg7o3smJlAAPYHOOLsgtxihzmVmGm2nWtFKPYZctvoOlSkCy4GRWfvPGP-_xpKBcVZAqzzXNOp0CvQewGvfuepHVVsHo1G5WxhkFHZKd1HlAPPfq_YmR_Zbp2xpp32qqfOREmmYFiI-_CrcL5iP0LZEDu9DdUsK1cHSo5FAlSxHE4vlBdggb6WgBaZLeDjVROkh2fB-8NB1C34m_qP8BoRuFte6vJ2xgSBALFoUrqA6OUy04_yv7Rln71wXNsryVs7D88QQLb8XOUSpUcWXIzXYygeQvRaEUdbGrBghVUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقلید عادل فردوسی‌پور از ابوطالب حسینی
🔸
«فوتبال ایران با مدیر انقلابی تحقیر شد». شاید فکر کنید این تیتر رسانۀ ضدایرانی اینترنشنال است اما این‌طور نیست. در هفته‌های منتهی به حضور ایران در جام جهانی رسانۀ ۳۶۰ متعلق به عادل فردوسی‌پور از هر فرصتی برای حمله به تیم ملی استفاده کرده.
🔹
بخشی از کارکرد رسانه‌ها همواره نقد برای بهبود شرایط است. به فدراسیون فوتبال ایران و تیم ملی نقدهای بسیاری وارد است. همین حالا می‌توان رونمایی از لباس تیم ملی، کش‌دار شدن ماجرای سهمیۀ آسیایی و ناتمام‌ماندن لیگ برتر را به‌عنوان‌مثال ذکر کرد.
🔹
اما چیزی که در مورد تیم ملی نادیده گرفته شده، فشار خارجی است. تهدید جانی تیم ملی از سوی ترامپ، تلاش برای لغو بازی‌های ایران، ندادن کمپ آریزونا و صدور ناقص ویزای اعضای تیم ملی همگی بخشی از کارشکنی است. سنگ‌اندازی که در دنیای فردوسی‌پور محلی از اعراب ندارد. او ترجیح می‌دهد تا جلوتر از نوک بینی‌اش را نبیند و تصویر بزرگ‌تر را نادیده بگیرد.
🔹
نقد ساختاری به بهبود شرایط کمک می‌کند، اما تمسخر صرفاً جنبه سرگرمی دارد و ارزش‌افزوده‌ای برای پیشرفت فوتبال ایجاد نمی‌کند. مسیری که فردوسی‌پور پس از جدایی از نود آن را شدیدتر دنبال کرده. حالا همه چیز به «وایرال‌شدن» بستگی دارد.
🔹
«قلعه‌نویی حالا طوری ساعت می‌بندد که همه باید ببینند». جمله‌ای بود که «عادل» در واکنش به فتوشات‌های سرمربی تیم ملی با ساعت رولکس بر زبان آورد.
🔹
او قبل‌تر حرف‌های قلعه‌نویی درباره سخت‌تر شدن صعود به جمع ۱۶ تیم برتر جام جهانی را هم پای «خنگ» بودن خودش گذاشته بود. حالا دیگر نقد فنی قرار نیست زمان برنامه را پر کند. همه چیز به اندازۀ آیتم‌های ابوطالب فکاهی شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442301" target="_blank">📅 17:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ad819e65.mp4?token=Xb5O48MuTbu8ZAgpn6nqPVjCLCuAXw51eRS5c7jGBEDQoPEGeFiZWdxcgnALWEAJiHrIrDPbXP4qr5bsgg9yeutr7lQ7U_awiQ8ZLOi9W6cIMnAJ91fs-77I3ucIlnYlqi0WrSxxrP37OHdMDulHH-0JCBUdTnt3iIxzE1OVDW-rlYDkebbRTpQ9pOfoMpDNp-Rf2YB1pHKk6eQbko6YzAfdFq7fjuc2-IlqtkyesNlLOsEDgboBdOc8Ax7nyEhvsRu_xzf8ZIrNZ06-6JDihQ9RGzcfavxpzuIDhWO-5XTytsvhHqOamtdDoQQZKgu0v8rJ88hCVHSHV9RMjjtUXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ad819e65.mp4?token=Xb5O48MuTbu8ZAgpn6nqPVjCLCuAXw51eRS5c7jGBEDQoPEGeFiZWdxcgnALWEAJiHrIrDPbXP4qr5bsgg9yeutr7lQ7U_awiQ8ZLOi9W6cIMnAJ91fs-77I3ucIlnYlqi0WrSxxrP37OHdMDulHH-0JCBUdTnt3iIxzE1OVDW-rlYDkebbRTpQ9pOfoMpDNp-Rf2YB1pHKk6eQbko6YzAfdFq7fjuc2-IlqtkyesNlLOsEDgboBdOc8Ax7nyEhvsRu_xzf8ZIrNZ06-6JDihQ9RGzcfavxpzuIDhWO-5XTytsvhHqOamtdDoQQZKgu0v8rJ88hCVHSHV9RMjjtUXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم.
🔹
اما…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442300" target="_blank">📅 17:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442299">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=GGaxiOoti5qewyFQyn1ux6rXw1Oo-WQ0Q87y0us9K8vm4dpcLEQJTCm0YJmP3rj2IUXDA9DdlrVJMxh95nyjHsdGjr8bZ4jZcSmDCApmagmnSGlMuNggmfcLabXqsJGJ8OFHA4pNBXBXQEbuOPpCJ0v3eXSQdgaP7G9xa1liOOL4tdgU6mJxLcf3KMmhdiU9QyM_zesp0QLfCKguJj0t_5UIg4xTatQvZB0aI5TExnkWHd9gtGwcuEqtnG4lA6qNhWMfIhVGgeRO5Qh6QWlFMKMUr2Zs84Fg4VO_cDU_7_4dTdZxd68NoY-aSgU2E632f0l6fI8JUCJg3ObLW-KYAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=GGaxiOoti5qewyFQyn1ux6rXw1Oo-WQ0Q87y0us9K8vm4dpcLEQJTCm0YJmP3rj2IUXDA9DdlrVJMxh95nyjHsdGjr8bZ4jZcSmDCApmagmnSGlMuNggmfcLabXqsJGJ8OFHA4pNBXBXQEbuOPpCJ0v3eXSQdgaP7G9xa1liOOL4tdgU6mJxLcf3KMmhdiU9QyM_zesp0QLfCKguJj0t_5UIg4xTatQvZB0aI5TExnkWHd9gtGwcuEqtnG4lA6qNhWMfIhVGgeRO5Qh6QWlFMKMUr2Zs84Fg4VO_cDU_7_4dTdZxd68NoY-aSgU2E632f0l6fI8JUCJg3ObLW-KYAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم.
🔹
اما تمام این اقدامات تنها در صورتی معنا خواهد داشت که یک توافق بین‌المللی وجود داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442299" target="_blank">📅 17:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442298">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d1ca889d.mp4?token=q0_7d_FiJMnQ0DhFEI4yX60FwZz4sOZ0fA_0K0D67OV5wQdcwq5MjnKCFT0tFRaOMu4FkNTJuYOTSaWKGLxi3Y8EK1vyMQjaP6UundAXRASllnfvboVWfNZCeWqx0jPKkeO9EmBXySYaSwO4dazqLs4lYZsVOipu8tVxamOHskjqIKMIZy-P-49qvz0D4PsGe6Qij6Y0XQhfejjh6YPvkdmJfJ8KQMtuqI-vC65jLDNyZv1qDrh3C4ackIYIBmGuE0CPg-b0rziHKhPaRxiEHQxm7rv-bzHxYJqDiSJz8NFTe7kVvGm6snWPAuzK1zY5UxA5VDP6sIP077qovMyEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d1ca889d.mp4?token=q0_7d_FiJMnQ0DhFEI4yX60FwZz4sOZ0fA_0K0D67OV5wQdcwq5MjnKCFT0tFRaOMu4FkNTJuYOTSaWKGLxi3Y8EK1vyMQjaP6UundAXRASllnfvboVWfNZCeWqx0jPKkeO9EmBXySYaSwO4dazqLs4lYZsVOipu8tVxamOHskjqIKMIZy-P-49qvz0D4PsGe6Qij6Y0XQhfejjh6YPvkdmJfJ8KQMtuqI-vC65jLDNyZv1qDrh3C4ackIYIBmGuE0CPg-b0rziHKhPaRxiEHQxm7rv-bzHxYJqDiSJz8NFTe7kVvGm6snWPAuzK1zY5UxA5VDP6sIP077qovMyEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش بقائی به ادعای معاون رئیس‌جمهور آمریکا در خصوص سرازیر شدن مزایای اقتصادی به ایران: ما را به خیر تو امیدی نیست
🔹
«از آمریکایی‌ها خیلی زیاد رسیده است! من فکر می‌کنم این مزایایی را که می‌گویند، باید از مردم میناب، مردم لامرد و خیلی از نقاط ایران پرسید…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442298" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442297">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663ecfe4e0.mp4?token=hdrv2bCwgVddjd9RToKtEWPd5-r3UQm1_fRRuzdptaa5pnPwmaHr_9xqInzsFpVEzsVmOTPmSMr-KVN967JpPosSbbTFGqastAFwYTfCBEStx45uU9OJxszSn_GnFEO2uaJcNuQvVq5-40a6ekWEVfMeGPLDe6t10p4NACsVeQkh9a6VuiX6f4UbWl0nVThTv3g-eORTEUIFqEDqxQBYS2whDXPRloZvGIMgqR3dMY3qxb-K7CqoY9ejDPmEuBWXpla2PGy9FT02CKLX28V662CYKrHjO-Axbf5TeUGKnohjVqIuOmj1CZTJkmtYip5IkUQv5dNY24M4FtuvdXe86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663ecfe4e0.mp4?token=hdrv2bCwgVddjd9RToKtEWPd5-r3UQm1_fRRuzdptaa5pnPwmaHr_9xqInzsFpVEzsVmOTPmSMr-KVN967JpPosSbbTFGqastAFwYTfCBEStx45uU9OJxszSn_GnFEO2uaJcNuQvVq5-40a6ekWEVfMeGPLDe6t10p4NACsVeQkh9a6VuiX6f4UbWl0nVThTv3g-eORTEUIFqEDqxQBYS2whDXPRloZvGIMgqR3dMY3qxb-K7CqoY9ejDPmEuBWXpla2PGy9FT02CKLX28V662CYKrHjO-Axbf5TeUGKnohjVqIuOmj1CZTJkmtYip5IkUQv5dNY24M4FtuvdXe86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ بقائی به حواشی امنیتی پیرامون کمپ تیم‌های ملی مختلف در آمریکا
🔹
خوشبختانه کمپ ایران در مکزیک است نه آمریکا؛ از مکزیک بابت میزبانی خوبش تشکر می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442297" target="_blank">📅 16:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442296">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZb6ihTZLnPuO7_uvDc1oqkuuBAvTsrwnMYOlcRl53AzweBtWWSR2qSVNt3QSusQmlzAvEau6iWw1fuXkagFcnPDw2qHHdR8GlwjAbg2DWx27OF-Xy5RmTSLelrBcTMh6ht3IH1oV_4bDOw1DMTlAhfGUBc6-2iGL4jqhoFR9qk7E-zDFblbK84KNtDhWE4yS-kNRwOfVL9boggsg0_6hZ6a0OmglfAAijG7fJWVbAwaw34k6DfyXsC2V4j4p-028yBZ8U1KCAvqr4z8NL0axpvf1jidR4-Sr-54bGcYK0H79SpnL-kdrR9xcEcwYFsqOrif0T88SyR680ertXR7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر صفحهٔ رسمی جام جهانی برای بازی ایران و نیوزیلند
⚽️
این بازی ساعت ۴:۳۰ صبح فردا در ورزشگاه لس‌آنجلس برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442296" target="_blank">📅 16:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442295">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=WOD_If_ZGPdERI8ZX-SQnOt6beyxVnGrbIiyIZ_LFkGREc2pFtmjGBExJy47Ns7WuTN0D-Z53PCVNYZfbZ6mP8bSEhcHJJdYCvbtYPpMUoosuhSpuvViKzB5wYh7vToDYBBViOj2KOlC7RC4pYMgE0QG_uRAsBC3YaVxQb9Gt_ky036prY2vmsqzUFsl3X7oHMrqJr-1JlSe3DyCnY7j3rVldeOCfZc24kcZjJnYX72K_aEdsQ_rh9RJv5YPoNf9fuU7vEQ3pfyw4_CRC0f3bmmLAf-doapIRyn7960rqUfKVD07PlZRqvNKtJHXutBULxEE8yf0qnRo0-SfxUFwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=WOD_If_ZGPdERI8ZX-SQnOt6beyxVnGrbIiyIZ_LFkGREc2pFtmjGBExJy47Ns7WuTN0D-Z53PCVNYZfbZ6mP8bSEhcHJJdYCvbtYPpMUoosuhSpuvViKzB5wYh7vToDYBBViOj2KOlC7RC4pYMgE0QG_uRAsBC3YaVxQb9Gt_ky036prY2vmsqzUFsl3X7oHMrqJr-1JlSe3DyCnY7j3rVldeOCfZc24kcZjJnYX72K_aEdsQ_rh9RJv5YPoNf9fuU7vEQ3pfyw4_CRC0f3bmmLAf-doapIRyn7960rqUfKVD07PlZRqvNKtJHXutBULxEE8yf0qnRo0-SfxUFwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مردمان ما به‌عنوان صاحبان کشور حتما مراقب عملکرد مسئولان کشور هستند.
🔹
مردم ما وقتی مجاب و قانع شوند که بهترین تصمیم‌ توسط مسئولین گرفته شده است پشتیبان ما خواهند بود. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442295" target="_blank">📅 16:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442294">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f9ae212.mp4?token=p1iddgT7-UaZxsIdhcnBjgPgvQAH3qVlL4CyFiKJ8I4DudoGRD0_cSpixs_WpJyQUqV9eTp1wFCY200j3WT7Bi40Off1ble_SaWVTwxv-0w-8ORWSFDnjKOIfojEp4Vo33aRI9J2SeoDEsSRv7VZK28lwvUjYMTcr6AJh04DktM6-WIXWeFdvVJ2nYH20jmMV7mBQlkOK3iAeA2iRiCM_jW7POkzXd1BZKY6zE-Bxs_OajULLl7An5CDnkKrkpq5OhUKaNzxHrl9xACZA2rk_DUuQNoMXUv4jBVAIhxF2l_vK22Kuy5E1Mtho1YoVICkjRCUfBtUVpgHAEY7SEvKSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f9ae212.mp4?token=p1iddgT7-UaZxsIdhcnBjgPgvQAH3qVlL4CyFiKJ8I4DudoGRD0_cSpixs_WpJyQUqV9eTp1wFCY200j3WT7Bi40Off1ble_SaWVTwxv-0w-8ORWSFDnjKOIfojEp4Vo33aRI9J2SeoDEsSRv7VZK28lwvUjYMTcr6AJh04DktM6-WIXWeFdvVJ2nYH20jmMV7mBQlkOK3iAeA2iRiCM_jW7POkzXd1BZKY6zE-Bxs_OajULLl7An5CDnkKrkpq5OhUKaNzxHrl9xACZA2rk_DUuQNoMXUv4jBVAIhxF2l_vK22Kuy5E1Mtho1YoVICkjRCUfBtUVpgHAEY7SEvKSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما به رژیم صهیونیستی هیچ اعتمادی نداریم کما اینکه به آمریکا هم نداریم
🔹
این امر ثابت شده‌ای است که این ۲ در اجرای تعهداتشان هیچ وقت صداقت نداشتند.
🔹
در عین حال ما ابزارهای خودمان را داریم. آمریکا باید تعهداتش را انجام دهد و باید اطمینان…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442294" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cd6fc55e.mp4?token=fFZJz2_9lgspmvHHLb-fqVy5r3ot1C-dLjr7zbR0gxafZezrfNxMO1sZx0tEcBbDHRxgMSAnqKJW7fBbVIL0O7KWOHZxBHB2lLRoTKrDtQ9JuzmX8b-kQeJ6cKqWSTmxspJue89aZhfImfCOpylUphKSJH54MwjekipJwBIZexTMsJy0rlXVK1SGLyjMXYbCBZr5bzdTRv5-fgNmrTrZm6htM32GaWfqtPpPaCLRaFv_q3UmtXq9WAJDdRRnKVTVCsVotMSQbxuqmlZl6diPbzEit6Cpsj0GMB6ojY7GMT2IrOcUzGLrtkW-ua3Pj_V_0Hru-KhMc7g1gAAMlIFyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cd6fc55e.mp4?token=fFZJz2_9lgspmvHHLb-fqVy5r3ot1C-dLjr7zbR0gxafZezrfNxMO1sZx0tEcBbDHRxgMSAnqKJW7fBbVIL0O7KWOHZxBHB2lLRoTKrDtQ9JuzmX8b-kQeJ6cKqWSTmxspJue89aZhfImfCOpylUphKSJH54MwjekipJwBIZexTMsJy0rlXVK1SGLyjMXYbCBZr5bzdTRv5-fgNmrTrZm6htM32GaWfqtPpPaCLRaFv_q3UmtXq9WAJDdRRnKVTVCsVotMSQbxuqmlZl6diPbzEit6Cpsj0GMB6ojY7GMT2IrOcUzGLrtkW-ua3Pj_V_0Hru-KhMc7g1gAAMlIFyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرات در مورد موضوع هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز انجام می‌شود
🔹
در متن یادداشت تفاهم راجع به جزییات موضوع هسته‌ای بحثی را مطرح نکردیم و به‌صورت کلی تفاهم شده که در یک بازۀ زمانی ۶۰ روزه بعد از امضای تفاهم در خصوص موضوع هسته‌ای…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442292" target="_blank">📅 16:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حزب‌الله: انعقاد تفاهم میان ایران و واشنگتن را که به برقراری آتش‌بس در همۀ جبهه‌ها از جمله لبنان انجامید، تبریک می‌گوییم
🔹
این موفقیت بزرگ حاصل ایستادگی کم‌نظیر، پایداری استثنایی و فداکاری‌های عظیم ملت ایران و رهبری خردمند آن در مسیر حفظ کرامت، حاکمیت و استقلال ملی خود بوده است.
🔹
حزب‌الله از مواضع ثابت ایران در حمایت از لبنان، مردم و مقاومتش و نیز اصرارشان بر حضور لبنان در هر توافقی که به توقف جنگ و حفظ حقوق این کشور منجر شود، قدردانی و تأکید می‌کند جمهوری اسلامی ایران بار دیگر نشان داد که پشتیبان و متحدی قدرتمند و وفادار است.
🔹
لبنان باید از این پشتوانۀ منطقه‌ای و بین‌المللی به بهترین شکل برای تحقق حاکمیت خود در چارچوب وحدت داخلی بهره ببرد.
🔹
آنچه محقق شده، مقدمه‌ای برای تکمیل آزادسازی کامل سرزمین ماست.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442291" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfrzMyaQaQ1VbuJGOGsCMFciqK-QDp9JqIIEKhFm98JKBL8UvO_87WjXgg0xrRNZnE6OurCjTnUhar1wtFez3kDKAnK2tnYeiMDzU-FMae1ZP4IMnNB1gXV6AbfanfPavx4mY0yCfO1yUgzxlsTwMETlO48oV_8VjFOOJeBjhZ06JixByC939K8_CSFnISMaoWHMW4Rwv0TZZbwzqU6jU4BAENPpOPOE5JCHrz3ctiTeR4LBKsRfxecZHfuJReApHw5Cl9XLFJLnkrqvS3zE2sWdLNRL8hT75HTQ9b4k6VzvILxSve_lmtGVHwesjzVs6xjrOBnnU3fWC9DvbHYqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر صفحهٔ رسمی جام جهانی برای بازی ایران و نیوزیلند
⚽️
این بازی ساعت ۴:۳۰ صبح فردا در ورزشگاه لس‌آنجلس برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442290" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
