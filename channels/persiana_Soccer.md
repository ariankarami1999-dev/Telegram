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
<img src="https://cdn4.telesco.pe/file/XETzMfOayefOqAtJhcquM30reFV5FAAe0IazcTHBgxiK8PVoh-N5VGtUWPaAec26L5m5SHIB7r4vss_NdaNOIB_j1hNX_D8VQhYpKx0NrsZYh5RViVdgPWuxTYtPEnW44z_-ycmh11DPfwH-WOAT9Uxg7Cj5M3YMkzshiISfv9YtQ5m4ZzfuDHylfXfh3bu4SelNxacmrn6fuFM56sR5739Z3n9qXCSPsFi3SUFHyUn-YdsbIxSaSlLDYnYqk_vCg2qQ2dsGPVjLBMJDD8jvDJJluim57R2zGa3XqVyhDESux6XNi9BrscDaknlUNVxLNAYTuXwkAuOAcvkuliDjng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 639K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-28625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQHwH27NtaUyEzqfdQfknprlBQAeGcaITj-cXyRPLJ-VZA7pznOgD-Z-TowNRp1UkV9uz2kvslQ1GVDfgoqRYPi1XnPa25rcA-Gw0jNENHF_CjyvM413Sj9shGx_EsIHc71pq_X9MVsxYuIJ9NFhZGsPtY7IT8x9anIcqZWHk87gYmrU1J8Ox1CsgSqB37yUoQtPdq20xs2-sk9ZF8wxqEUL3XfM8Fj9A_r-MrW_JnwhhENa7y5WjsCa6spGbBG1O_GkLf7THv4cZfkYcrP55xPmpqu1ZQpNMzCZ_63nE9rQFS6gZ60mu73LTMjrDst6zliJM0B5nEeB0Aby1MaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه SPORT اسپانیا که معتقده که امسال بارسای هانسی فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/28625" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28624">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXGuziSMPHgfqlL1yvyLT2APNf8mpVZTyeRbvpkq_50nYSyhhrb6l5G5k3ooen02aY1Wif0oEZMVh_UMkv5axWMynyh-idN7N53At2mo7BMHUGfUxEbQ1tYkHA_3QyMz6iwyTe6PZHS6WWI4DbnII44zTGpv5e-Hg0gJ16egGdhOyrgBGRZ8Ix61yPX0DGGrgO4Y7h8vz_Gm7y03wAin3AT21dFVbh7R0zzdniArb9ssJF7A9ZSrzbIbzPx0UnrcIIZZVKkxNNviKBVhvsddA6Jwn7OdzXPokzWXBBVFc8As8ClAGBe2VB5URd3HNVV0YCQKagxchT44nL4Y958v6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/28624" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNKuQoc-FJ_jtmrtthFrWhtgqN75zO7usj1lu5NQFEFxga4PkfidEgfymBWanCM5qffzCIruiX7g_R2quJjiVqZWJwOqpsU-zYLXBnXh6cQW5G4EYi4mrT97FFNPmriHJoiNwv_c0P93l-qyJ32YYmvm_oGbwiRHeDo_cEpXoLF_z1KWKbqpK08sdk4i6kHHBQfX3jU84tdgANki07c9CTlY4Xl8T8tTg7_Zb5m2BgpFAyjc0mpUx7xfEk3Sj5JrOAD6ScubRKdLh5KAsyL5wm5BlwfuZOo7vSXCsTLMX4kEp6p4Z9zvBHgEJdjTrIFzwuk72ZtAanF00yfjcV6dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOWAqvzSAgNbw8Zy6rvUF67OtTPhVrhl67Hs6AuatlO-tIzwEqab0sFrtAFJOHEE7T4D5ccw0V6PSlfLr0AzOcfk9Gl01sHF95vnhmebfhgK9MedxAi2UxTcK5XB9LQNenjo59bvNrZ7GY47zIF0u9EWCEFfsre_gY3DaSo-mKqlLc-NGo2zpiqag500BwzDhwZ8Fd63Yg-_cUcGy1t2XnyH1Yy2KH4Pjpet0K4W0omaZaNAuXKsbtDyYwqW2T6lqTsSTeFxjqkQq-hZbwKc5GdlsffNF9Eg2ChIXy89v-oEBiNmH48fTBdcVrlLvhgnyc2fLR1qXkn56u0wSqNXbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/28622" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIcp9klOCRgKQ1ajAJl23bQuFe6dnvm5-NEbc4RzFcL2B0u4s6Aw2-5JdRMlt74P8Ajd73MMeGeg0_MmFsW3j2hn9t3lMH7f1UpBGnKWN2ZkwfWZSn5BuV_iRDQdR2t0edPCP6APv5RX3fGZam2qxITjHrQdEqDBYIgDH963VJ2-2oPbRoh6S-zRV7H4hlCQataYrei_yO9_zonQWpxM_jh9LC1YgVIiOUWvb0vEoAYowns8ZMkH88Tck8dm4yLt6ozJ5iEpe8-1gVHsU_Q1lFEwDdpTPV74uhuiSekcfcJWzT-RTJZu3kokZyqlsp5yWM3E6fnYf4e33haxLKpOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده کیلیان امباپه، وینیسیوس جونیور و جود بلینگهام درکل دوران حرفه ایشون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/28620" target="_blank">📅 15:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObNOp8QjjtQF8vsobeo3zunoqnwQn4QsLZiJalVb29xkrwAqTeG1sYmHzw6ZDi4z51IkQ5BU4emMcqZyEPkaD3y_5RquTNedoSdilj5gMM4CZDHSHX9e1gWVD42y0ZLlfd5_Cg_Noivthzz2xGwir48zmfYI45uFdbMHGWEiVRHm5I1PoxkP9iK0Dakc8j_eDeyNh6ffipYP98hQ_3oc84Z9yxJZEnQ8A4wdh4g1qMdsDeFZl_1XvPvDzJ83demh1t1z9HAr07KIbiOX_blZKsagqJoJZvbWwFScIUrzZ96b-PhnynTpyEZANqW5dOo0M2Rd7mv4HVTH4CS8CqLUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک دیوانه‌وار تیم ساپینتو در مقدماتی لیگ اروپا؛ پافوس باهدایت‌ریکاردو ساپینتو شکست 2-0 دیدار رفت مقابل هایدوک اشپلیت را جبران کرد و با پیروزی 4-0 در مسابقه برگشت، به دور سوم مرحله مقدماتی رقابت‌های فصل‌آتی لیگ‌اروپا صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/28619" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imGUMMlbN6nv76_yHnkVUDNMNUrAC46PkgaaTlAes_LpPPzy5JqYoOKTcZHTpTyX_GTETa3bW1_onueRfznJ7d6QtQjoaZHRGZJju-3xCy36gy0pjZfrz8djego265_8cFZn6pVK57hnlhDvEzveW7CIcnhPM8K5iiB-x_OcoCSlkieJiZnSqiqItY6b5AnodsfpQu2ZTXrDTz3ifO_KxGEMZQPN_Rfj7ojiugdbODKN6d9kPnv0COWUFb18sqzGo1MnF0y1uXBNqdXf1jgx-_Ehyqb-M24L6A-XmdSpvRfj0f8icaVpmh4VWummDdgnKvNG09u3tYDqRo5dwxIFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/28618" target="_blank">📅 14:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28617">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc0WV8v-7L-oyY5EilsaTUKmCoh5CP-ymBkJu_FfMaDf6EJpBDZxJ0DttB5p-kub4fCilPNGo0MvM-iak-fQ3aYrTwG3hcfVmLiAlsrOoeMIm8oKtzhj1EpYs8VTvygGcclFjIPVWbheAoM6HzZ8-j6oOg0x4LQvFC-t5X2PNV7T2VpaJnJNcqbZLeVHDbeU5-SNNZqirLH04Rzz975XF_Rl27TwN7xPUJQCwq9xQLZSNxogx3W0c10vJbvE-0i5qpt7hVxUfI-iCBtFRTwUSJkS5ZxZuEKF_QGcpJxqPyDKbiK03FLn8ueEF3jTCtvmXe2hk7cpx-KaetoQ6wTyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛ آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/28617" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28616">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFt7StSDpAmvYqQM-XZI6rFZu0b1f9Eg-F0zwX8n6F9zBvd0rGI5sQ39CNasX5-yq6eTRxofC2ZpCoa5ArF_rIK5Xdl3VEHBQk4KQHFFmed8bbH-dxk2bZa1-Hl0LwyE4x_qSLJLQspktXNoc9gq3kv_c5wxYf7qdJXwZ1-qNsXv8VUpMjiEL6Q_mviGjh_xddRPmKuKvpoVNtrVfOA7EBsRvjvCxbJnvOLnTJidMiEj3vFVwKHIFtW3JikQlBnjRvB5STCiW1eq5gKsxgbuAX8RuU7uzk-scmitePrIp-Of3y4yeWNwO3rPIPQtcctzip2tqy2-h7FEVjIVeG-CEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28616" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsyAsd-LXW4yic8kBWKk_-OxbQEAoFsnnzW26ofq4Z_yBR2cqXo2S6c64IcJKPPY4HiW7zYw9o9ceJeZV3qneJS95sDvvsd6TeljsazJVI4NWHYJgQLXK0_WupB59YIxtopQTplkZUtIkb6zld3-x4l_GS_WS6YYmQVqJ1gRsITa0Csfy0fBKPzIlXdz80LlYMnrfu1okeSVeC8DuhwayMRyiuWiY_Ue9eZ06iBxuk7XwYHvwfJJHkLOcJ99xc7ueeKxRkNntgHJm33ussxKPWN4FU5VCdkXVE1-JWdgcOKlmhg4ab58zXfPPXMZO4m07KBhqUydmAj1elniDGQNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28615" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EphsBTT1EHlkhccU1etIT_Lnu88hmNXFlvJ7C4zYn-aUC9ncSVx-7Hrv5Yi0iBb_QIS8EsGdy8PR1bv0mLvI1VUrRUieaIl7ThaGIQ5_7elJ6spiHngnoI9hOJUVLkowc7bbHxz5HE4c5pX1ZmevwKASJQpsp6AykPzgSUlbb5BFb4t9nZJJBmMo9b1Ipo396xnVV_wkCqPCR7T8yH2nYK6h7eSkLzALfsXMTIq4WK65aqcncLbVVJDkTLb1QYP0EdZW2B0QTF08jHUfxLssRe2BV-fQDHuJgGPdmILyjxjR1hgTFuhOg05UCrudeaXS1IopY9dAEspstGNC7kO9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/28614" target="_blank">📅 12:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy-4EY3jP9kotbvJIDCTKtaBmHpH4IsY1rpdWIyaQQTRaxwwos94sP65h2tVhi4GXCYuV6yVq9mfDrrqE3x80IXAhBKRBHm_xXeCNt7dNrUWvuwX5bY0TjWfgaeAzb4M_VUr6pfBfO1yAU4HPAiqhvuE68ONmNkin_bsu4b_kn9d6oksntxuuILz23l6UCI13mRYWkXo577uEkgkkh62eSeu11TS7ZcHuc7J3yuEuwzEkOjpabOIxIJ-FZ-CyhK1GOAHGVraxsFmxwEFBjeS1eY9z2L3r4rHL98gshLb1-jup7kpqYFY5QWtF8PeMkqNfM6fNVTKb8mOxoMCSZroAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28613" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkaqGXWxPeW0vY_io69Jv5I6ehyUZbYmDc09kTZRNy8xD8T5oZWhs30U4bOwHaDvfOV5klfLJtbqofGDE-fdqt8rAcNHYNEuySd41GmZXRmbti0nUovU1n4C3tmbHZW_Hi02JwizvoIsMwzRXBPp73ChUZn-0Egb9lhXKWGcDpXpvu8Bip-wXVutp9Uf8fHGSfJhfCo_VflMKGQwAaEWiCAPAb0_8_KF_-Om1qOYVkJItG5qFILFgCqTt7uBEuFrxlpapOZHfxOw9HbRF-4eby2CTm2nuDwKOzJZ8yTppG3TL9RoFdjPdEwulnjpVcmcS_e9MeA7CaYD5Wg4R9dkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28612" target="_blank">📅 11:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPwacYorwErf0HZ9MNA57yMfUdjML-hhcVkqgmLhitIPHzXr0HqovPYlUlnt3z7KGJmJyZFLObQ7vlLmmbez7WmK5bnSCGVsVRYHbWjZ0xOZvrj5TA3dyC5kLQvCLdCHFkv1k8zIDLWRmRl3Njfy_aX-Acc7HJhFhFlm9GunuRdQE9Ch1hfguFLjMfnBzHS6DYWbyUZAbuJ-s5o_slPULgik0IyiGQ-Wb26dzqItUSmrbhljelej4Pyg2QtQ-Ka2AqZi2rCJiolsD6fnOASGUa415Wk3lw58haHirrMnXQtOk9dFaJDB0bdVHBNdQZg4KPOXyJCEUteHFZalavar8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28611" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UleeeumL2NYpGVdqJgFwxthVu6JNKw51Bp0nAnXG1HinZXyHhIGuxXzpIYNfe0XO7CRodnm0TJzlmgZ0vx_L-HheH4y0GTgtFKA976xqI9hX5kGqDTQ25fi_kCO5tdbJdPBC6V5a4ta-AQC6HifWJ_Nt7jSw0atum2g-AP5qED2Ekni4eE0yFQgLNek1FypO-hGCuuFYmkQ7xAgxCOzpP6a-abSJuPjZzVt-TsdzQhcd_CRc2A9yYUTXbNvpjPQtRcFwzQ8jcOQ5U-G8L1MwqLQB5f9DYCOwNUsrzky5rkn6tn7IeUP5pKfE4kacYG_BDU-Z5Rs2TVd3T9h6H6UNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇩🇪
‌اسپورت‌ امارات: باشگاه الوصل بعداز جذب مهدی طارمی و ریاض محرز در آستانه عقد قراردادی دوساله با مارکو رویس ستاره 37 ساله سابق‌ بورسیا دورتموند قرارگرفته و پیشنهادی دوساله به‌ارزش 10 میلیون یور به اسطوره دورتموندی ها داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28610" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdYOPgHxfFIscUwoQv88nZKKHoGR_8mLctRH5MsVVfn7FIBSTN18iBCmPO2XIv9l95MJ9rzlawD5vRFObjPHl0BQCPO9Hd7TqYial_a3yKgLrQAsFR0Bmj-O-2fCAe1aZTf2WZPzICsojPRhrcjCMu-cZPqs7HtDgp57Fmmz6Bf_zfB0BA4lk7tWDL57M5eqf4bItSLh4mvK0WJIdZ5aIjl26VSzyIF9PL8ssUE0hDrw9AEOkbvJ6TTU-nzZdqD6narwwflhuUVsRaSUXtGJ1s_sWZ5mEs8qz-n8wPtBtQNq6dKcHlgWXvLnx79jB17KnLC0xHkgylf4llmLgjfhPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/28609" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28608">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvSf4gKi_eoraBFgre29KjR-VcIChXYKZ8-YTHJBYqQSbtBUvJATDu09pGZSmZU2k35oRJA_68BjBlfOD-McCHvW51Pkc2S-Uxa8-izWouYLUdkMn09lrnH8j2ajmQ1HdBl1a1lUn4DwBMZN4NbfW7YQZ3vT11nQ85xR9NK2dCDqxfgyWFjuaD8U7fVfdxFwtzsVAkl1eNv7Bgka36JKXV6hoOKl_Ek7ijZXxL9uO2CpS-ldoclQn4oA_y9vx6Gp-BVs7OdSWRsy2JelVee7rjjrYqxJi4mL8_UdxxW1nmMdOW0J2fRuXP1mr9Y1PL1ssfBCbBAgIx6RRySGvdBpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ با اعلام باشگاه تاتنهام؛ عمر مرموش ستاره مصری منچسترسیتی با عقد قراردادی قرضی تا پایان فصل همراه با بند خرید دائمی به ارزش 50 میلیون‌یورو به‌این تیم پیوست و شاگرد دزربی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28608" target="_blank">📅 10:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28607">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEmPxiHRVJeQgWSGNUfculGwP947fhrzPH6Hm3t2ETaqrBf3Y7bOSNz6dXA6WKe0rw-GWfUx5ETAypPAgVuZ6q197-D38ka5uc_NJhsfhvzy4GUD3pwth_HHcyXRfhE8wvJbPLPY7BjqbWtaFYb_v8h0S5mgjXv-R_BDYt5jN4c7FbUeiP6H5okjAjwFeonB3NCm0zNSLKfxAft4LYKUjyd2AU_E1_lCE8DOMwHB5_AAq3OWRE77lGdMLWbvQ3b3Eh8kVVkwLmm0lSIhpQNaA4S4AXohI_xu7EO6ZuxBNQAtyUgX7iLzzSffTJp8un9znr3VS_1fVfmqZOmy3R09ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28607" target="_blank">📅 09:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28606">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbu91yUyU0jImVR95R_LKqxKES27zIoi8jQTtYIH8-G1QW2JpwIlMk3y693bkBoBD8HEN_znXab7vBl1T5cD0TBmB9kGBFL9xyh_GW8_xRq9g-fRkaDJLYD-8GJctWIoEvSYRO3S090Vf7zLvnZ20UjmAiKwNHn6eifbE7Ye7szFtDM7choI6DSFIU5wpTkY3Wie9BZDepqfNyum3KKNvhOFv_iaGixQq95fe53e_z6CDyxReRVA6gIDVN-mXkUF-rLcOKnN4P6QawPlZbu-Pv9oqLb40Tk2FdMJm3vKUXNzWvddw21oUirAgJ9nM6bY3zVAA8OEI-RAmjQxg5fBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28606" target="_blank">📅 09:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVmPMJUwfXW1zLDl5S9M46CqxBvOss8hNr0XsnO8YOyBMidM9b-4a668jqw0DqgAwm_nlXpCiWNM5u9Y8Nl17doc9tt0Eh5W5bKZQLBBDWkJUondTRvk3VwNCS2-R8b3FWIP70TOxLjCexOeW6KETEEIbsu50XZN5I7m8WrX4C5rgz2YbPd1iynkbu2To07Xn0qBVfBC_rYq3LKgbxR9Iya7KvjJi4id3tRmUSLh1xqxVmcuVS1sCe9jBCRZIqy3zQNnNxHKOdIDllvp3lp1ZMKWB08wauIytVpP8RNKVVzoCKN_a-HppJIBItBZOxwmrE60xNREfYmAAGytWvcJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل مرحله گروهی لیگ قهرمانان اروپا در یک نگاه؛ چه بازی‌های جذابی قراره ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28604" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b440142175.mp4?token=PnnxD6MR7XlEzFbkbRLpO7ct3uXL-6AcOp65PKWOgQGCBDFm6_--kt8CPg7T_UwPrlGpEAnivkBijXBHc9zTGtHKoNPuPUduNj_B_xbyxE3C4KiN6f-AtT28_XyXaxCL0T99FCKY7TXOD-RhLkJaZkUf_m4zp_VR_2phL3wzWLET18Wtsq45fQlp3NPW7jreuNFnTpdppFQdyZ-ZTYZrZCJaiYfbXEHcXy3xJPsNP8474lkS5IejESolfiispAC1ZQLQQsLnhORMBAVkaxVFdhX18Tq1KGcS2U-wXUpxUDvDn6pC9hqRkejSwDrwMMoeiPLKMlznA8bFZkOXRc0HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b440142175.mp4?token=PnnxD6MR7XlEzFbkbRLpO7ct3uXL-6AcOp65PKWOgQGCBDFm6_--kt8CPg7T_UwPrlGpEAnivkBijXBHc9zTGtHKoNPuPUduNj_B_xbyxE3C4KiN6f-AtT28_XyXaxCL0T99FCKY7TXOD-RhLkJaZkUf_m4zp_VR_2phL3wzWLET18Wtsq45fQlp3NPW7jreuNFnTpdppFQdyZ-ZTYZrZCJaiYfbXEHcXy3xJPsNP8474lkS5IejESolfiispAC1ZQLQQsLnhORMBAVkaxVFdhX18Tq1KGcS2U-wXUpxUDvDn6pC9hqRkejSwDrwMMoeiPLKMlznA8bFZkOXRc0HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی جالب دیدارهای هفته‌چهارم رقابت‌های لیگ برتر؛ سیوش‌کنیدببینیم چندتاش درست در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28603" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🗓
🔴
🔴
#تقویم
؛
15 سال پیش درچنین روزی؛
شاگردان سر الکس فرگوسن در اولترافورد با نتیجه‌ تحقیر آمیز 8 بر 2 تیم آرسنال رو شکست‌ دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28602" target="_blank">📅 08:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1ZyggpBevHT6HKVddAiq41IxT0iXCQo0_4oJ9-E2UH7dbrU-JwyPmOR-cX5U_oGyddu6ItsTRSeipUlUy87FsXqmYwFJMGOPneaOrPZwX0zdI5iRGq3-ho3WI9PRoP9Hghcn1dtJFLXwBPygCpKreg6Kr2Y_iX4bGoAYuGw7zXwLp9iAYsD2Y6VV0hdr0gZVS5zBAFxBavC9TyKpok7udy-E21JBGH1oYR3wK7skqU334gJOYw_atOvt3zYPlJ36ap6yzId2mo3iH4pbOWDaeZtZtY2_oS3S4Zx8EpLeNHt82JwrvB3yXBNvOKTDXGqDJPPvq8uOfjpg7UFQZilHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
جدال شاگردان سهراب با فولادی‌ها در هفته چهارم و دیدار افتتاحیه فصل جدید بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28601" target="_blank">📅 01:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcBewzjCn97lXEZRGOE08h0kP3VFJCueDrZdht3cbY18yb5BcUltXMxF26IuohUeAyE0nCh0qipu1brT_d-y3ackXxqIyxbMRzOazmaJcv4Xv_sPXZ-NMsCZpDKACodwMbnCTA5PX5Zi2SdWCYZWIVVjnGmaiG07C8_T39SIC5j_SQw8N26uyEFBJ2ynCn1Rcf0mr9hkK-TSmTLv1I3LWv2vPtGlqFvBz2pZFOwRHphdG20BqLKpXuBC7FpAO_lruWn5KRY5uzo0Xtm4kyH3E-T8zYPeUSqcV1cFbMeHzXJzBkevTz49zmwiaiaC8Tv2hwWbh3ulJYLkA2qlPQzSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
برد آبی‌اناری‌ها در اولین تجربه حضور رودری و صعود چلسی با گلزنی ولبک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28600" target="_blank">📅 01:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT8wZt7zf0CVbsy4e0C9k1isd2KQve0_h_wzZvk9aTXhHXbXrP8i4BcOquLqee2Z1JbWSn-JM8Cwc-QGkiQlDmYQPcQ3WUy803sxuaLbXLGx_zdBNffSIj_B78fUCFoRzRLzmQzcjcQm-Kk78x0wSNCN4JmlR3EMXUkBwe78_2xexPgp34dOunFwtjCoiEbtVl94M0OTiK6W4bOq_Mu8-Rvzw0BvqYoLL1DLX20DZUCTDi_uaNf6YcrAMdko62-xlHNB0NslyxeI3lF71ehWhOTyvfJZOZj4hw0TgIeW_b13JwME5-Ksg7q1MI1l8cwDVZ6_vjX_o2gfIbsxfrkeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28599" target="_blank">📅 00:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGLQ6Sy9mEvbjiaKwpfjev5_y-YbSniHsiCpdsbMjdeEuWeVT_F3k7ICk_vgYzWvynd7dGO9anqBzkq3lGCk_GUxJu6pAr9i1RnWMut2L-CRJ8xEHo92Fzbxu8rBFtIKNFpbtnjkqPuVlpJGCN4Y-6VCvxdrUEUfIzSvgCJLojbI1RVAnbIlU1hP3ax966kZxctO-dly2i3mlXw4HNc3I9bX7UaGwNNLKb-ZQkrTOD-tfu8mOy80kMNWpyC2AnZGDhqPSlFeAJF5PsvBe25jxMvpsb2-eya6jB-0RWUZUx8aUCTK4ddWWpqOWb28Ij1axCzww8ZSEPye4EyNPTn9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده و پاس گل از سال 2020 تا کنون؛
کیلیان‌امباپه‌وکوین‌دیبروینه در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28598" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=qbBUSp7sCWNZcdK1z2uT6_PKM4MkS_P_N3qE_P0N5ke9hlSj5taB24q423hPPmVOLH29WGHsdjZTW72RFJM8BZTwr2YVUULbsBP8x2AdurPJ9OK4Gse2WUo08K11r8kbhAeDQQlmbHV0yR_p0Z3UG6KJubKdum4tZXnUb6H5LHbEwK05-2kaGk32JsQWOcTizxfpde7z6_Wz_M_9BRC3G2fNDTCPNMhAkOy2OzBXJbrxxLmw3jKGrbzfxNiyKBVdl-czNMAv_lqkQCF8CwXh8EjlaZOBVMCPKV__apY4-SKR_9kw6iHouYgCoIRaJ19sM9BidTr8zX9IAF9BqISDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=qbBUSp7sCWNZcdK1z2uT6_PKM4MkS_P_N3qE_P0N5ke9hlSj5taB24q423hPPmVOLH29WGHsdjZTW72RFJM8BZTwr2YVUULbsBP8x2AdurPJ9OK4Gse2WUo08K11r8kbhAeDQQlmbHV0yR_p0Z3UG6KJubKdum4tZXnUb6H5LHbEwK05-2kaGk32JsQWOcTizxfpde7z6_Wz_M_9BRC3G2fNDTCPNMhAkOy2OzBXJbrxxLmw3jKGrbzfxNiyKBVdl-czNMAv_lqkQCF8CwXh8EjlaZOBVMCPKV__apY4-SKR_9kw6iHouYgCoIRaJ19sM9BidTr8zX9IAF9BqISDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28597" target="_blank">📅 00:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsocyBPRn1MnqTI26-p4wwDCBgsTOaVmwNZiqM-UB3CqB5udmL4IL4VVvP4sK1KNhdnZYj_DMz1f7M2w3xQ-N4VikowYssIudWs4lr1ebdChVrTGb5vkcRF49E8eVOzCVU5HEw7-8l-9wE7Jz29ILv640wSTPI_JmZzNbZe3Vkdv-JTIrVZ7Vqvuoxe6mtG20LlHUEn5Gx8MwDx_ZPLYtD3NgIt0irWD30tg0uiJOnzLql9VGGefHElB-IDJriP0zClb_ZathG4olQff8b9H7Lr4KwUW29Tcc2uRGk6L65P1RUcrQHbZbn_jTzNT6tOYN-3v1ygRPq5FEVqSoGpiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28596" target="_blank">📅 23:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZZu_jwM6LwQlcTrQG_32Kg0GM9tRfWZrDm1m0Tctg2T3KkF7sFNbM2N7Z1gfroI_8FUwqWqB1zNt8pZWcv2LqzwyTczylQ3DjJpjz3L4Bi0o1aUyqYAs-Jyvw9GXn_rSyaZKf8-zC9QiRKj-dT8OIdHUFWBPNwNJUuW1tADmJZ1QkRnyiQHEdwsZymCIkp58f9ygXbkxmYYt51fMT2Klv5wLJWpmINdqWz6VkCzpydXKKMAIVpoOrN8PsBgNHLOwuEBDNY60we7jDCeJeUZgVyvAaeav0NgkBkJ7VquqAWg0v_NUzkNbDubK43WGcafMi5le7MiNNSav6CesfvPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28595" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_czT5bHFA6BKhHTp-pMGZ2GgiTxy7V2ZyW3weF84LQU6SrJf7uisLhRLhuvE1p1vTTLl0GeTYk3WGL7ArPwx6rZHsd3p0Jl0Q5Pw9Y8q9vJaEd-et5lMrSJecop0ctME-jzhCldtgfD7vZ90bA2Zpu6aRNyJy75BOQYpD3uQ8bWAK2dZRWnT3Upv7hAi7n6wYtjViAk-2TiL06INqZZilv_zZLqygckcohZhoJQ976U0g-pjkZbFqozWzgYuerdnDZSMGpAOAGvir-61NXTQ2SzSME9g0bY26Esksd8rBDFnkMZgtdwL1Ce2BowJRjD6K_w-ap1yY8O5HntarZUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
🤩
بیانیه‌جدیدباشگاه اتلتیکومادرید: تحت هیچ‌شرایطی خولیان الوارز رو به بارسا نخواهیم داد. تنها تیمی‌که‌موافق‌هستیم آلوارز رو بفروشیم آرسناله و هیچ گونه مشکلی هم با این انتقال نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28594" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg1dCBu23UBOHgFsw0sM2exXSVgJ6n6r1hLjVcZPoupDROaY86kFAl2y0L9CNCdHC01mq8NlclzEcPY8n0IR7bQ7pd1EtEiSLAOKAyijmqihZC8Ms8SybKfsWF_gV9UsVuNvr78nKgO_vbAmKJ2bBOlMzdVg2H9wULps4uVdbSzLAhO4mAbJ8vN3yqX72qXVk4aQ-juSgHOzJlN8cg7YsrGg9DbDF1VKz0Y3zz2d4SSsdu0vzwgxXBse_jnr8AsbcpIAx4KWzyh2qYpTKNx788ZZFhUsdlRU0ptedakW6OJxOi35toqAgc9YoEDJW-X8fh1ZBhbzqdDopvIv5l9HQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28593" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbQY7ttCNkKJJ5dM3VmO5KfCECC-OAEohFAGLhsJEj4xMyj_0py1X3O2MhJGFBraGSJA5Uz8IPHi_l7D3gaVNTktZxSn3rorXgNMx5iAnQZRzaP6MAxdq4wkkFO2LbLoAhlAPRKGtsRMJvwVoUTxn7ahSvOc6EZ07A6XcwityuAFdwjpXPhJCJZIiyygRat1Ivux8D2RRiRpEMBVdUILIrKB4h1hJpRrY3KVPhOIRFITC2eTxzPgG57vTFN7yjr1c31JvZxsqkaTTceebZOdq63ZWGVV3W_VvT1Wyyar5aCII5m6cyD1Mm47K3pB7fHfEfp4o-nqro5cf0FozZ-nWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار به مدیریت‌تیم پرسپولیس گفته اگه پیشنهادی با رقم بالا برای فروش اورونوف به باشگاه ارسال‌شدمیتونن اورونوف رو بفروشند. حقیقت اینه تارتار اورونوف رو نمیخواد و میخواد فراریش بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28592" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4KgIesEiDK1zrT2GCrkoKbc5wvxxYqhW42KaRKjtYf_I_0PUIS1areuSafqd6KPpj0unLecawmK0cabl_raviecmziP_fqrovIqD-78LvjBZRj1fTaskmHqt6X7ZWep-arbUdPK96VL5i-LTAi-7Z5McHp1QgY7wLhZgcd5T9jfi9fFhHEzjxKYU2BuFeIrlaSkyl6h6xfhvJ1ml7ygft4PV2_wuPWK6YjsjkAv5z2fGnNQluvstyOVp_KLA60exKV_95P_7IzPwZHCiLILWRuG5x0jflxTC4JL0AvAsvxNiKaTx2RdkeBbVR65od-_Hm56bYLP1gJ16oqsMWugWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28591" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28590">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKyD_KRTaCpPYvY3MeSTyQOijd_GYtww7sxhc2wdf5RDhmIms1ZNGFVkUvhWM1fVRQDUgIOCbl5QePmQNF6_MKBtc1ckRXNWFLhH2-991Y1zMe2HD3jxxKSkMiNDUQh-w8fZGOA2AtNONu1joSQPqRVhji8G69isgfAm9fEgFiZRsxaSZdfQ0xq5plKdQfuv7n70Lpv1QbZ5S-sfX8e1qG3suby1I58LWyCW_atpIWF-ssuv5GSyblNWiUJcaAcGR3G_hIkKElWImoMxmAam1A6_nVcWjtAEK003wRZbEotDVbBmw5Xdqh1IBTNzkfrSSEig6gMLs98Q4eahvy28Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28590" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28589">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016588e26c.mp4?token=RUv4a3aCf2LBS-AR0hM4hu32S9W9A25fSd5KLxki2iDInAfkNdyb7c0-kGH8ClBlTUOBKqZfLARvlm8g8LRsxOVBoE12WS1-ky5KmjsM9wQOG547JeMo3AW7TzGmzEDSvoXmvhylYI2lcH0Xyg_k4_bVfS2QpYZn37-E1kOoSOiOaNFEzpcxBSmqpGYFtsQJT8Wi47qwvulUIehIvn79EfXfRIjmgzsAZxWJ26iwWhful1vO6-SIS27FkdIhlnro6dBu24SshXrBDTQQn2JSQ3zLwfEBEDIBeLLOC7lH2eKaC8Yoy8Q92jnnrlLmMYxGr9omiZoWkf0h0HLTtayUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016588e26c.mp4?token=RUv4a3aCf2LBS-AR0hM4hu32S9W9A25fSd5KLxki2iDInAfkNdyb7c0-kGH8ClBlTUOBKqZfLARvlm8g8LRsxOVBoE12WS1-ky5KmjsM9wQOG547JeMo3AW7TzGmzEDSvoXmvhylYI2lcH0Xyg_k4_bVfS2QpYZn37-E1kOoSOiOaNFEzpcxBSmqpGYFtsQJT8Wi47qwvulUIehIvn79EfXfRIjmgzsAZxWJ26iwWhful1vO6-SIS27FkdIhlnro6dBu24SshXrBDTQQn2JSQ3zLwfEBEDIBeLLOC7lH2eKaC8Yoy8Q92jnnrlLmMYxGr9omiZoWkf0h0HLTtayUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28589" target="_blank">📅 20:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAYUhZQmm4qQ_Q8iGN9CD0nQpSSHxJDdpxXh9JTm2IzcSSKPHkseP51Yk_mKFzpmVEA8Zv1SqEWOitbux6h1zzay0Tsk20MCUYeFMipVl_Jf8-WF2lf44hc1tgBDKzG_pe3knneoK8xvzAx7Dhav-idbuo72WHpv6wDZNcvb6sbMPMXcrZqRMLlm_7ZP8kUye8vwPGQtqGXi7ciSRo0J4E9MgFaKxeIWlXCkCzxNVv06lD0NELS8k3HCiXErYKlyJawoea6O_ib1os3qwtUhEOTMvBhzbmRekCcdzvfH1B6k-Slz9Lgbfdk61_pPYAf9ah5BTPUCgV6xwTb4Ltgemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28588" target="_blank">📅 20:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoHnguWcfNw8d1dEAaRPHncb_N73ZT_YmNyTP8IWdMyauDKjZ-yJ-Fy4cl7-FlLInx01mAhzl7uQ5BtThJu9BthiUqnGUPl1B1VCqxKtQpye8iqcyy1otEFFUf0_T1GnlpkyMOoU_8COp5er_Sg2wzBCmizVIc_7KELOoMqOx9yHJkxFCyMLT8xUi1maOyDl0kbUQQFHqXNFqVN2-57qPsvfphYjitoYvQLq416EigZxx-r8CGi40_tLyj06rCAGaZXwVGgpEg0NqOK57s_kmSSZBHRupm3bECp5dWMtPF0In9CQeJTHWdkiARi_orQPx6QFFUOPtIHyMHs3sp4VFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سید بندی فصل جدید UCL مشخص شد؛ قرعه کشی مرحله‌گروهی‌هم امشب ساعت 20:30 برگزار میشه و مسابقات از اواخر هفته آینده شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28587" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28586">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQWiFtZcueHreMpzc1Ip5BYrPs7gGoRjivRc3hXgskudZgpaoxoY8JWspMooEaHQKOkQ--7b6zIIQP9bf4kwDrLLntUBMMdFA4ZBpCp2Fjf4wjBrRbXc9DoYecnGq2VgABkioixXcRbJGKqa4ymbwTZKsbuHiItofnoEjtivMontataOW_9el5LViy7svISjZEJSdZtuVdTiTyWKgvpA1i7EY1QzJ9S0z-YI9PXC5-sOU2rlM-8ay-6yt3BWIHljhmKgi_um2swVYAU5NTHx_GuE82jKFZBnCc4pYHxM9g5Ab-3IazNdGfpg6H3uzuuHgkT9Iob59Z8A_4BR2yUbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28586" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28585">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry5jK_sFiv3ycjltH9v7ufowszfe8P_k3kxEBBYP5OgXVfwzyM5uZGueJ0LEZFUAQpYv29GcvP2cEl-AFAI1JntXYYaWigI6TL4LZZda9E8Q2YMvGYcWD9xBhVGmpG4fAb-NGBgY3MAZb7YySA_3c2Iy00MwMus2To-maOkgQGwtq9WD7Npgi5f6_q1Qtlqc5d2VGfUGURo1Gkv1i6YeroUVBn54qwhzDqQidEiCnbM8BUmvTlnM_CtZ4EYrGpU6Z2Nz1j38vIRoVohkjI6i_IZzNE_zw8BTN28VuC7XlnwLyBJa2aLYCsCczRZwIF23l5sx2_oqdSce50ApOpln2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28585" target="_blank">📅 19:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28584">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nST7ms-ITcXgO0wnL7exLWG7S6hjOH0yViuVIyPoPpULAumwSyVTLhPKM3-5fDSckLhWyQvETQOqm9qaFlEHpGCqnmEY5FFJXBWDerREGIocoHxKwTGFRa7Hd2GaIp4puhZrqP9xWqR9362FtUcEFtc80IIbWobxJE6d7wI6_UKe38qLb4ogK5K4US6CYjq-jR_XbmOGhg_Q-4NnzmvQr4pfCtXEkbUrylWgismgo-DN6jSjCcLuiAhp0l2DqU7EicAxlu2Ist2L16NOBeGNRnyrejBdwiCkTsP8uYs9DZrO4gwmI9TvvWFtTj-LRAUfNEsVvmK64pzSae2tlr4vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28584" target="_blank">📅 18:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTC8_E7oR-UdF4Epie-KGWDolv1U8jkiXXHB3TKILdk414CuOeCOiNufgRgH337-XLWjb5hZ71D5AS2SNPFpW3txFmJxyLldhtfr9_cu0T8OJL3yP3wkRs3Q6S-36OGNUaB9GhgWrCiSN43JlysHwN11FzZF5yJFR41VpO_Pc76yvwlrKe_EXgnS2rTNwpHis-4zZBek70j6M8DibOyQQ4pwlcN8-9D3E7gjuJjP61o82qu5Ssgyw5ukYVaqFAzy9kQZFKTpLD-pFHBKm_eLrH_Zws7MkAuo0QjupQlUZAQ97i9yOSyOx2u5xZt7TZB7MO4SvuWxqBJQtgwQHAho2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇬
با اعلام رومانو؛ عمر مرموش ستاره مصری 27 ساله منچستر سیتی با عقد قرار دادی چهار ساله به‌تیم‌تاتنهام پیوست‌. این یازدهمین ستاره من سیتی بود که بعد از جدایی پپ از سیتی جدا شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28583" target="_blank">📅 17:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsu-qjBud8-sOYP2UyijEe9jK8E-PFXb6_0MXrAtvk8rCU5kefLaKqr8Z6ErFR7BKAQ58XothK0b0FPi0-PAaLILHqGovPZmue0-ijH8260HkcFSk9QJpVnP2uW1lz4IZtdZtrTalwJ5LHZ4F5e8m0bZ1pJbbQJGFwmG5H7Ty8Ar6vLmPDTDa2-LptksDEPChtvia9-vDH69h51brGuMBFieA-4Pfqk_CzC5-HV_zUX6X9m2mIwLVHPMLqIfQGZwzZcyD4qnTArmMoh2cFaZwCN1GcWp8-h_P1JsWvzBEuJyEg14sfHLoTNVeD20ll14iH7YtwKOzK1QT5hy7IFp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
#اختصاصی_پرشیانا #فوری؛ باشگاه آلومینیوم اراک رقم‌رضایت‌نامه مهدی‌مهدوی مدافع‌راست جوان خود را 300 هزار دلار اعلام کرد. باشگاه پرسپولیس طی روز های گذشته با ارسال نامه ای به این مدیران باشگاه خواستار جذب این مدافع راست شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28582" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28581">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6phbwokFlU4MEepfpWK2P3U7qix8cxN5zdf2GfB7b7Ew0kCUWSQ9wW5e-Q09btnL3jRwYuet1Ia1mflCY_C0nqtpFV45XzDxr2f0jNMdz0BSooXSW_dJF2UttHFCd2Hg0UkkqPbBgqfNY-a8fapNuGgggfOq5t2xpn3BgHSfQvQxTe8MBhmsepO25u_9oArZmpFhp7p3QTb5_NZ9VfqOppAqoQNt6zAXZt0mxlubYa-XnI6VAridQl7eU6AlBMJVqVOFpd2C4rQViJVEL15eBMbNGzfxx9ZI0R3xT2e6t1oiqLzx0UX980ny4goVs_KIFolRXGLv1GKp5aA_KAVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
#تکمیلی؛ همچون روز گذشته؛ خولیان آلوارز در تمرین امروز اتلتیکو مادرید شرکت نخواهد کرد. آلوارز میخواد سران اتلتیکو رو تحت فشار قرار بده تا با پیوستن او به بارسلونا موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28581" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giVxgprPOc6cQ3RZbb2RI2SDXgwLq-VP-ub0Yg5qFLp3opunSb3q-Ltn7dq4ii5hOTGzI0uZMZFJ5WwgwX6Zm7b7GPOK5lq6PplxOJiTSWqqKCcbMpvAIJhF0TLT7-0RCFJfhv8ZFnDfSuosKbqFoCtRyY82lJEux2A3-4yqb0P6fEYQPhr3A8kTnuVSjYr-8FpTtxXGXRHwulH9ejU9e8AesIH9sQt6JDhGjDMj5xYdk7WKuldm3V0zsxeVN4mAoaEVkMDU-bD2QHPURQw05Iby8PXTouoYmoAkdVl_1AkO9NCXihp0SP1dHFILt_IGOHuZ4BJUGC1LJgpmNd28cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه نساجی؛ کوروش اژدهاکش وینگر18ساله تیم پرسپولیس با قراردادی قرضی به این تیم پیوست. همچنین یعقوب براجعه مدافع راست جوان سرخ‌ ها نیز با قراردادی قرضی به‌همراه بند خرید قطعی به نساجی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28579" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoB_Kgmvnc7JYB7pc4DjhaivxiRcPK4T0jK799CgwpGgYjvl10hvxcXa0ZZ-UTNdqWo1RfiI1pgMfeBv11UJfl8UIaA1BaL7phx4XD4QJ08CZl2OWy4kJrnZGxhjHYeVyugVJR-BHA0RTgBuzw4xe9nj3Z51XuBJ7egUnnBw83bwuIT1FPYnamTIsdhjLtiJzmqW0oKOoVEYeYGWW0_xa0u4RGlGtxKNpqLkXofGa1wVC6mW2hVl9Fcr8XF5u_mJfgUeugw9pZHqochZpMsqe7x5fSL4yQpdDLnHsrhGQ6QBFV3he8CyIESSP9EnSACMtEVe-IZKjKfiUpcUmd8Vew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات:
پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28578" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcsMhDFiH04mDg1q6KT0EwUKWFL8Zr3jf3ESmKahqMnfIT_wS3FfKNl8wW_r1MgIQnzOfMzwo4Hgd2tuKAuGwyFJW_vYzJPgmRw7E4BYHNsl0OxiMmoHTB1ImwRu9n6TurPQvdEAbsT54RizKxcheZC3y5DkcQ2fd4J8UE070uCVh4Wo51YNfVxVxqWGRcwGpmHFh6bq7jyB7Sfj4ygHqIWdiQYz0LFMeuVWu6Q65D5FMY3BFADod0bvRTflIxVpttN0RDlLKfbetweLrfh7iQKINrsHhh-4MrzixfNo92ORjAIfyXbSRs10UPDw3curNxh2gK-XJTyUWeatF4mkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28576" target="_blank">📅 15:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrQMFpO0HcnKN5SJ6sWzjMdmhQ2vOCexPphtLfRPQS7bVm62_0pv643cTHQPHXgGnEQ7yY_K1XADkZ27DIl1u4swAzhR8aYPKpVoYwmPVrfg-5I_0sUxtFnd4dbetGUl0dxrT60cXpP1DQL8ysr18xzQui-JBT4Htthiljw0uPNFeHK71E82BwUCMXqlEhEzy_tOA8GnACFSWl8UEI3pCPTpKeVlicnjE3gxnADYk9iC5DqIHx9bF8VF0XSq4I8unTS23TfHHfl9EUzNr7GXsdXFGeUWMJr-ih7Jj7rjKrX-8OfW0_NeBXhqoWCeLeeiY0P7wlXq_urXnEwtqhlzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28575" target="_blank">📅 15:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=dfI-X3oi38a9AogUP8WO-edbq3zjnDqxzfnv7VDC_HiR226NP6WIJK3AVDZ0sTi6j7K3_kf0KYJQ9vahAecRv9GTTzqTJxges_uEJg6kO7bqzt-oXBWhSELIPOj--FmvaueX7fhmiqzJYukK2W5E515YYxBvHkJ7ufjDNxN9gyBdkEKI393U74yBcUWV_Adfl0fP_7Ttja1kyw6IlNBZWc_AHOwTo6jvJzchtfD1FMM7jD4HNGLHZnHDjdczgaZ7EwaKpneDKtWcCnpAgvUEFDcadO3B_a6jeCk2Ap2xgmunmz0ku42FEf1DGvl148pS4UdtsEbtO_FBzKkE4ar1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=dfI-X3oi38a9AogUP8WO-edbq3zjnDqxzfnv7VDC_HiR226NP6WIJK3AVDZ0sTi6j7K3_kf0KYJQ9vahAecRv9GTTzqTJxges_uEJg6kO7bqzt-oXBWhSELIPOj--FmvaueX7fhmiqzJYukK2W5E515YYxBvHkJ7ufjDNxN9gyBdkEKI393U74yBcUWV_Adfl0fP_7Ttja1kyw6IlNBZWc_AHOwTo6jvJzchtfD1FMM7jD4HNGLHZnHDjdczgaZ7EwaKpneDKtWcCnpAgvUEFDcadO3B_a6jeCk2Ap2xgmunmz0ku42FEf1DGvl148pS4UdtsEbtO_FBzKkE4ar1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
خبرنگار در پایان دیدار با سوسیداد:
امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣ ژوزه مورینیو: من چهل گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28574" target="_blank">📅 14:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZTHx09aAguxkfki3mxTEnCH8TYNFOPvLrlV-FpBmBtKZrOr_kw8lkEwZPcrwsTAQ1w2kaHp-PUWLHi1RyfwYvkN6sCzscYUySnAKG2FzdJrVUJ9mcMh2WUgusRrgP-8-9y2ShHmz-K5hY3saQ7M94KDyo8Bf8Bf7QzBaiNbm9SOtn_hjs-r662Vcs5FplZSaTxAWhXyYHa2wcS21yimm1JlnnTbKzDTztjr5ZUwtkXnqF1aF1WyI64ZJEpuCSEdXc0yKTrOL56ir0ENUpVqK7btieVpkkaYpZi0kQz7K2Z262l8fbmu9rxbD7a796NdGoyJFnqKJV0Kvcmzg9lnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زنی باطرح‌شکایتی مدعی‌شد که توسط سرایدار منچستریونایتد در دهه ۸۰ میلادی مورد تجاوز قرار گرفته. این سرایدار در سال ۲۰۰۹ فوت شده و شاکی به تازگی شکایت خود را ارائه کرده. باشگاه منچستر با اعلام اینکه این موضوع ارتباطی به باشگاه ندارد و طی این ۴۰ سال اطلاعی از آن نداشته، بمنظور عدم مزاحمت این زن برای خانواده متوفی مبلغی را جهت جلب رضایت وی پرداخت کرد و پرونده بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28573" target="_blank">📅 14:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8YIZlP3xTFpSgAZQrMGM2FOqgdIKjuPXxWblaUncrR6jxM44usmDDEMh7bJdZyzfJ1IcsZwYhHvn3TvQbTf9I7nHTEjcp7fnqLieWzAkeqk9DBPGXny66OAuweempIWK2sLjtQPbyBmzz57x2Toyrb5eK5wOaHUgMPpueV4UtQc8YKQDnLFEfqQ8mUdnTnxxikRUNikJs3ZlsvWnG3FPSQ8HMBo5WLJbmeKgnwPmMZbiiZm7iymWeVpnPiHnbF9YtJ2K91k_ru5IxsJfTyIDpDpntJrpFOImln8mRRDTO_hh5w7JOd04KuQvcnx-i9ZiMMJcW3VOOlw0gjoo1bPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
از سری اتفاقاتی که فقط واسه تیمای ایرانی رخ میده: استقلال قراره تو هفته اول لیگ نخبگان تو ورزشگاه السد میزبان خود باشگاه السد باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28572" target="_blank">📅 13:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNDpQfa0A7masH198-5e-y4AFkf5F0I9YjX_fXxfazoScL_pvtwnyNhHhrBAA_4AewACQpYOF7ueTZ-CJprEbGgxBjqHE7ZPQywxs-V1Tz0HZV6yBFnj8aDRBdctM468pH_stJjY7AxORxd7FdSJSi6dEZav7T-omgwEAijfplp525mbH-jrQP8KTnQ_xgHBxL4pUsD6fCC4j0XVf40Cw2Z79ol5oNocESkzQ7zrCSRPqoNKX1IVFG6QiX8_ffhxworQSJUDnY8oY2xexGwblaH0QTUN0AAr4KF_yHdJlvTh9taWHtV0aS4Zqb7y0LWhzlkyzIVNfppdb7DE1-5fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0XXWCkcupYdkt7Rc861MwRaJ2zY1x11hQjWBgN2xPVBl-PGIRY_nAusq6rLBm6MDiV5c2inurznXM-J-lZbLDSEIcPdtWiPpDaTRh0iTaIeSGsnY5M-07k_2BIktI4D6d0x62_psx2hlx0WCYkXXutyjd6-yMLhmWBpCy2EjQYR0YImv4OM2QRD1VsYZgNLnkRtU9bmp5hZN-SFUzQF51KKmdid-A1WbNghSADhBPhRFXXKhncIyzcaOXYS_Xdemo-zYpl4EhU6gb3cMjlZaOHKSov0_9gFBf9ZsdXSLnbGKi3PN_KeeXvjg4GVvY0sHqRDyRIUELm3qw1mUMg8Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛
ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28570" target="_blank">📅 12:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If5astCdDwS-RR3Xxi-uhw9y83TEt_8tdpYBs4xuNdpzEWzKJVD1cyOIY7g1X-6GbeDx-4rraGQrX4C94hRAZBpSFHzg14MBLV5a8GjNy8O4Oh8DhDoGYikhhUp7kZS1isRzaX9G8Zj7cIUrv452TI7U-x636HoBpLFHPa99-cqadcbMrR6hFWtECkkEUBDyVuNZxZ9mJYCMbgaP3cZMHnMBqE1q4Y5B7I8namuudTw7Esqye_aY7ATfY1UDQXgGgMdRCvyHsEyMJNrQuNu_WiWZPIYUcZ24wPYdyN0Z5qKBpx8MRCKrtpbXurl8oTYatuSpg6lq0dvfC8TuYXm4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتلاش‌پزشکان‌باشگاه‌ استقلال؛ روزبه چشمی و جلال الدین ماشاریپوف درلیست بازیکنان استقلال برای دیدار فردا مقابل مس شهر بابک قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28569" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk5ijEVRoONXjwYfJjd1PWTQyzuxGpQpIqRPqNvsfayrXXXsrRUiIDQP3FftI0aRqqfAl2KePMZ5BIQjJ6w4HNtR-a-HQTjaJpNkmso_G5jTR-qRoIu614A8GpXwWC3_aNmTr5lxovZu3DvzMEzVfe9Dsw7yEndfC7i5Nwkfa_Ynn2ochBAHxhKvxGoRBk3KzkUnyhtIMETdWvMnIdaibvMo9X8DwcQIOvKKf4-ZNbEBztSn5YbBWHEH0D-Dsn8a9xGZLIDBYxH1F_VuYjWJeUIGdZgDNUn6DafK0M0iXAmv7MhX6ynoIfwOJ-qi3Ejz3euVEZaFlRCoE1xcswlDyP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk5ijEVRoONXjwYfJjd1PWTQyzuxGpQpIqRPqNvsfayrXXXsrRUiIDQP3FftI0aRqqfAl2KePMZ5BIQjJ6w4HNtR-a-HQTjaJpNkmso_G5jTR-qRoIu614A8GpXwWC3_aNmTr5lxovZu3DvzMEzVfe9Dsw7yEndfC7i5Nwkfa_Ynn2ochBAHxhKvxGoRBk3KzkUnyhtIMETdWvMnIdaibvMo9X8DwcQIOvKKf4-ZNbEBztSn5YbBWHEH0D-Dsn8a9xGZLIDBYxH1F_VuYjWJeUIGdZgDNUn6DafK0M0iXAmv7MhX6ynoIfwOJ-qi3Ejz3euVEZaFlRCoE1xcswlDyP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28568" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz88E_PIudmYcu0XYTJ-xGSIVs9GCVZ2UHqQqq8YSnPte4hplXxmCenGU70U3J9VYp7iX6k0spCFHwsvZ6lg7XtQLK2yr8VWN1eeWyKj_QuKeXto_P8YDeD1FCi7gppObMWkntVwm8FX8tM-o-9UpF0izzw17zy27E3KsPxIWgETPzVblMu67fk3kmaMMcs5CT9VGmkuZjUq_55O_oX6EalWVge0g1TGewu42zxROKUIJ08h0nBpCKpwnijDLNqKV0_PxeVRhVFO66gcpFQdfRmCmybcM7l4kKyD8EBM0Cy6MtZWiluMq_ml618AVMS_xwErp8ltuuQ7b8ETqgqkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28567" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPYQCBubSqCQ_m2iP-WTJy9jwfE1LlFz_4XI8B5FFwpf-7zZAU7BWLA-kcT5sD_lV8yYZGbx2Tgbjs9vn3XyGN-HmxHFhMtDs9s1aItpQdCugmpD86wZK0wBgqQriF6x5y4PWuksr2E7V_0YH7do577I_fpqHwxhW38JTDjUbFOa9_SxsIR7jN88a-KRrA9phOVRXZuqFyZTqN0l4BPc5FbIRFQ6ZfwwN2IYkocWUZKc_WoqD9jFwp-I0Adr8w_rVg7EWADUbsG5T9NfVxZdRauMp79aL22pFHgQwNGLbFX90pD65yqp3k1M_O37uKN_b_5eqg-B6AebiLNHoIkLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛بردلی‌بارکولاستاره‌فرانسوی PSG در آستانه پیوستن به لیورپول قرار گرفته. توافقات شخصی بین او و باشگاه لیورپول انجام شده است. بارکولا گفته‌که‌نمیخوام PSG بمونم سران پاری‌سن ژرمن هم گفتن لیورپول 140 میلیون یورو بده بند فسخ قراردادت رو فعال میکنه. لیورپول…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28566" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو؛ هکتور فورت ستاره جوان بارسا به دلیل زندگی در اسپانیا آفر دورتموند رو رد کرد و با عقد قراردادی به رئال سوسیداد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28564" target="_blank">📅 10:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=e67yfrumDxPJFB4S6d8chSIqKUh__qDqCxJJUlk8lwGzLvjs3kwAeUOiMDihvPZFx8cTGZTD_7h470K80AxF9wZrU5YsnXqSBvGNY5LjX0MVcNxjBuF0KTQhVgLeVERxkso_f_ybzfCKsWcxamvfIbwZAfSmeQh28hqE87DscHDUisXGvpJrSjUtnS2KM0rFeMVt2SElaDnObu_dCCmajOcob4MbpmWkU3vwc5_bC8f2iHC5DJO47f_FvDjHZchVxZzz6QyLEE9ngFmpMB1jzOyzJBrv09wMZsAFVmNCGrSqxOfCSXAN2MmGdZw6_l5JqvxpbDYIHUz8snbtuA7kbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=e67yfrumDxPJFB4S6d8chSIqKUh__qDqCxJJUlk8lwGzLvjs3kwAeUOiMDihvPZFx8cTGZTD_7h470K80AxF9wZrU5YsnXqSBvGNY5LjX0MVcNxjBuF0KTQhVgLeVERxkso_f_ybzfCKsWcxamvfIbwZAfSmeQh28hqE87DscHDUisXGvpJrSjUtnS2KM0rFeMVt2SElaDnObu_dCCmajOcob4MbpmWkU3vwc5_bC8f2iHC5DJO47f_FvDjHZchVxZzz6QyLEE9ngFmpMB1jzOyzJBrv09wMZsAFVmNCGrSqxOfCSXAN2MmGdZw6_l5JqvxpbDYIHUz8snbtuA7kbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند حرکت فوق العاده خفن و البته ساده حین ورزش کردن برای درآوردن سیکس پک‌های شکمتون درکناریک‌رژیم درست به قطع کردن قند مصنوعی و مصرف کم روغن در برنامه غذاییتون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28563" target="_blank">📅 10:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
این تیکه‌های فان داداشمون به امیر قلعه نویی و مهدی طارمی مهاجم تیم ملی عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28562" target="_blank">📅 10:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKCM3mA-BADTbg_60b_aVr_lYACFTfJvV3AIS9OivlYRFQcTE8jxZMwN5kprgyuGMKwRzsEQCCI6OFNAJeqifctGTFoSy5CpLLr740GH-AQsv_amngg4IE0fmIvigz1JwH8tRCLogllGUVYpBtmtGYM9BBMpsJ-RpX1VpwzUPwDZWIh85jJWj5HEH_Hpp7XWU5ltsdyInOW7ghaZ55liyfxW0xFfWiYTenAtIKZp4as9Gyyf9U_wMlnDJ4xluzyk0M9C4F5LElCmW2k0u2qcmJPX4CYZSkvj3E-1jiC_fF617CE_IMpL6RAzJlV9vbOuoo-OIO25pCtmjW5Ap-rFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28561" target="_blank">📅 09:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spli_T1QQ-ODqfaG3kG4HrtCLCngHhEDuSfPWH7E10YuqR17EMFbz9dE2VgTr-cqNb2Mx-l0ibPCbuUhqObiJXvbCyK8vcZdhSMgKkOPvdoOr1WlFq0wQqE9GCtPaGROLdA9FAaaIXM8lkh36TMjvVCt1F8q6YeSPDqX3N18kCwBnZORrkYFTeUzdLGjN0G3yXVgmo5vPUYGTOrmcjHRl3rEzkNdO4pQBIVP80bDgTzPbGzyu-OCR11C7VmDWU2FOQkiwlwzQZ0M31eM2JN3IDTqdGtBcyo4BwiewrVer8EAF8N2fBS2_K8iQXA26gJnIvIv4AMgQjCvn2Wki1PuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28560" target="_blank">📅 09:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN0DBI-DIajdi6FEMt-AvfEGBtIwg5OoQxI3ne9c01_q8ZV8f-wM_dQDTuKkq8sVyubuRIM0eTVpJgcHkzZ9jbH9pfRQIv5ICM1yBskYWjkhjTn2_cMp-d6WsnjyT8f_IghTs4l46zmdnub_e-fW3KbP_1GedUhIaUvqr6sTaVUXT2ASXmQ-IazLss91VjnVKR--bvd65EPwIma4TmIjoNkLlfix8dTvT3U4n3mSxWAsZ_b5By7tr-3IOIUmOQUWytvN4QSsziwBaQtXVMfRPlRLm8bIS_m6k6N-MH2B2dN-ry_H8iVQzr37NVPsDUKhhZAW24fb3YSSeuYblG4Y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛سال2021درچنین‌روزی؛
کریس رونالدو فوق ستاره پرتغالی سابق رئال مادرید و یوونتوس با عقد قراردادی دو ساله به منچستریونایتد بازگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28559" target="_blank">📅 09:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28557">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9MlCjt8EGrqYeKDf9KKTzVdbdUSf-HWtjqfoUsRi0_Km2qnDPtXbTwNt0-PRacqmz9G3ww4CXA9Ekx9JDxiKYZKGhnzwRMTsUi1bDm5QgbGhf7alAQrw9IY4kDSjh2jbYPFlhfHgN33OnhjE7KbYnREbzRs2ZRkmUI0puq2-P61zHqMoBKM0-C0R_n7CCrjT9A0miBqBYgkWXf3_wzaK-OfAYZXsE98mINhA6LFfQ5TKPCA423FSwjVCf8475ORsM3AdQ1XRJKSeWY7JeaSepU1NZkSG2FPBdggU3eyt7Tt7ilUmmdLUeOLfLylKCBy9h0MgE5e7uvJdp-l6MHrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
دوئل‌جذاب‌تیم‌های هانسی فلیک و ادین‌ترزیچ این‌بار درلالیگاواستادیوم نیوکمپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28557" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28556">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujxvUnPKGhyBMN7g0cu-LI_p6Os5IF5WRZaqivxO_k9L4plQC2jdVFWqqFTLQALUKkxpr2anVealSSujubBR8q-Xsx10vOl4IIPeAE5f6ajMGTxnQomjIDS-KOQmzOVTn2OuPlBiwL51tgsBFCzBxqEOI2L2vwBt4dHmBYJYK-8Gp3rbGll4cA8W2JSGKYCAhcfZqhukxrmiysuqpldeNMfZ_o9O34rpylAtCtZSBU1CwvW7_xyDojkjJPWTeMTrG7_ZMVfqEe35LO67pkUhidCGSf4kx0cdny4SGdy9bu24yWgNmTe6GcsSPeCzxhJzp61mOtpjfDRvzK1muWNR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
از برد رئالی‌ها با هتریک امباپه تا صعود یاران کارتال به دور گروهی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28556" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28555">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=hrXUFkEcPL4O3nh9EmiKQILNbtkbYjBsJCwhfCP-U7zKrkxeFslYv99uZdXk2LnYmtqyBk_cAEfSUmaFK5llWkN4jPQlDC202GcjKIQ9RmT7wq8k7h1MUFG4KB0MjNS3tbaTPAhzWRqdSamEhShcilelUM19L5W2sfKb0dHWiHlQCDQHDCyQw1KTQ0aPvzc90Mlwm02qAMFaUGhHHlAbiaxhfbQDIYS3ios2sx5hyAiyLrtg_xUReBTLJxZE8A2R_SaIijXj6NcEOU4YcbKJ_QUwryYHjJk-yImY8CeUgpaBm75BPXbMOeTNmm3tUjeCzXH7WNrtHXQsZ8oYGwAHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=hrXUFkEcPL4O3nh9EmiKQILNbtkbYjBsJCwhfCP-U7zKrkxeFslYv99uZdXk2LnYmtqyBk_cAEfSUmaFK5llWkN4jPQlDC202GcjKIQ9RmT7wq8k7h1MUFG4KB0MjNS3tbaTPAhzWRqdSamEhShcilelUM19L5W2sfKb0dHWiHlQCDQHDCyQw1KTQ0aPvzc90Mlwm02qAMFaUGhHHlAbiaxhfbQDIYS3ios2sx5hyAiyLrtg_xUReBTLJxZE8A2R_SaIijXj6NcEOU4YcbKJ_QUwryYHjJk-yImY8CeUgpaBm75BPXbMOeTNmm3tUjeCzXH7WNrtHXQsZ8oYGwAHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#هشدار
؛این‌ویدیوکوتاه‌از صحبت‌های مهم دکتر علی کرمی مدیرآزمایشگاه‌کنترل کیفیت مواد غذایی ببینید درباره مصرف آب معدنی برگاتون میریزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28555" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28554">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2GFW0jtDmbhgh0E7sZeMATQR41CEAAvlFo6M7Ruol03oKaBS1Pf7mIAfQlc1t_2Hi2twqMhTwWjL-hdoBcO12GDVHFZw1fxa0qP_rqmnl8Q5YvBqkhnP-1bjoZjd1yHYLVC8PDdkfecDH-nsPqAAM4Ka6HlKWLNCM2bfw7m0_NgiPijCid7GpXxX4orVB6hECA0xCtCerBErjyLD7vwHJOaYGNiKR7Nyr4KhjWcI3c8kFOfNFeIfzt32MuEwUvFh2TRpe9UYBZt-Lek-R9HAUNt6uokzXRyI0hQRC2EuSM9Xrggk-pNa1JdinPn0egLl4Bc-qhG0ITNgSnXzyFqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28554" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28553">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXBYw4_RzQWPCGXPdmS2vzRjOuaa7Jk25srFcyNLDrhznf-N3PJpS6hfqn2xHj7SJYJ-OE8QUeyFSevbS60IHV89H71jg-iKdK00RtAxGPCsYojBu7QjTfQ6OZBu4K_ElolB3uGAGrh5NEl0nZ9CQn8W7Njt_8dLPaVSSQdmTqIeTJ5Z-UQh-M6jRt-6z0okHBocNdiaVuddFNKadEEIAR5CC0N0FpGz3qdm3xIOS2KANT4SGyobSwHzSkqgdVauU-XJMD-cTBDcEYA_eh9MC6TK7fbqF3pI-30oeEEC9c4aBNDkvGhNZzT5L2jOgnP4Ktqq8LSY7IHPWFdHq4n3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28553" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYlhPKuapDh6r5BAhRyMn9T4iMNfRQAAgHSh6I5cUJ0zMa1fwn7605w4gOT2VrYNEzrec1b8FVvTbid_WmHbCH8HFrHPSA5PFwNPI5yiQRqiRAr4Tj9WLyAnRwB3RFAhrk828sdEC6gfRe-ePOtGa16eIsQVWU1m7L1_RgO6x_hxwl0aW42ouHYIWOWlHSz5qiHZqUuiv_k67rxM3BrbolrrwLX09HEc029vGrNQRrKpnTBC8NagffhVrOFL1De59K5cbxHfhh5KA_pdnb-5aftFM7Hhzn5RI-Ff3O1EOMoHfWrONnY3_MOfnGaHmLrBk03XaY-pOZx9kCi7CO7Y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28551" target="_blank">📅 01:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwK9ojeh0Hdmk1uogCeHyYbtgYsJgYEwoPPf--P3ul7Rz-b5c24dwcSxDncS8ujp7XAPT8fPfkeLeD6a1_R5zrUACM_wPdDoW-l_VqO0Z13yY2To_n5_qBc03_TvrJU3s4Fjt5rWvNlHgtUD-uHzZL6yrw4-6UEmFkcBNMxTqfZCy3cVBcpiyJ7KyVG57-7dPPdd5TnScjEQ8EPXRuktlFS6MdakuAFFdfYhYMLy0WnD86VZkefDkoVn7n86ACL13E2MoVVolowH-MEEkzzG2jO-CJ2qZmzFZf_4xCVu31TgWvQOoH6tX7YhxtimZls0m0Nkkl_LH3R_EEh1p0yecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28550" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZNA0b0TJZYuJFJBmJs-bxETUv5g-_IGQYHhgoKWaXCB5cnb6ynrPfxPWFcxurbOLyLhA3N67QpbAT8Y2ffHddfB68Gd6GDtS0dJKyj1ZRjQO5M8enM4j0LW3cG9c0rJB14zvnbJFxHEJLcmKV5vEkRAyUdqAHHBifqI9LuDooDIXpiiSLEtxm7DMYW8BFr9srkEdG169aIV3TW7RXBQ4KS0qAk9fp7q1NA-gus0rU_jiQ5yo7XrYF0SB7YVST21_NUJr_9kXILYUBX1CV_E277sbeqLW4Jo4VLeu0liGK-FfLemDuOcyuuTMyyXWP7aNqaIYiT9SmrjsaHRWiMjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28549" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haMg2OtOWtwn7yhZOZ244-5vkuB-FBiqZOcdmtl9HmXAR7phAS8xvbJlq8f7MFVVwyiZuocgdPYpFoa2IxdPqDMD1r2NS7ixx-qWNHO8nGA3-GpyuLjpw-prUrT7vdSzVw1FEDpOtxjri4Q1WO7U0DQW7_DoXcnXKq-Bq8CnD8gvroi9WNxNzABhUYZJfh6Jk8gTUVAw8xnTRmaeaCYXxU-KkQJATY-T0FzJ5dikfLFez-jtMplCQrnBHGi1vXXQjhOsRMKNsTaYkvbl-_8C4MUULf1_a8X3sYd-PkRhMJzhwnD76G18J-p4B8hrQpcFxJigzPmLMEsFG_kXczeLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28548" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
ویدیویی‌دیگرازجشن‌فارغ‌التحصیلی دانجشویان رشته علوم ورزشی این بار دانشگاه آزاد تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28547" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5WqxMkYAmHk4B8fghy48chA-aOJFfVhbD80khzw4chj7Sr66QANnzXYdIejBtRkxd2q26yEfBEHTsXL98-8FxVMhZwwDqpoLocXzRkXVEOMht6kp_Na0EUXZktvYUaGRjp1rkVXh_6w5oAFaI6wkSKnjUeL1M2uxaM-XFeIccaVhSe-CA4e1U_LZhWXmOQDsRf_bB5a2Ew5I_aWqNQeH7sR-hnDT4x6ZMBgtwSJcVRg4xqoJv7q6_JvsVFswk2kI5X7pmukoLKJNd4nlmFhIacOyeH-9WGDyPffssRJ3LIS93rc2V3hIqp9rPg--850tyHq5CxDFt9x-3AbHamVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌هفته‌چهارم رقابت های لیگ برتر؛ شش دیدار روز جمعه برگزار میشه، سه دیدار شنبه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28546" target="_blank">📅 23:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mldS0fRP5Bqwoxfyy-1Vdbv78w_s0YoaEF_AzFG7tXOPjQ-UKRu8g-I_Gk1-vGdkO4eAvsoGfNCAu61s6g8yoXB4k8MyIpzXSX_wE7ZtNcFsgy0d5bNPdIogYTqti_XwMysBu_yZzTrsWsyuQ9F-r19hMg23bvif70SQKozdKTwHw0scMghVMCdLQUp_xK2jE7MGe8LONsChAFwy3GSwotNWcWosr3ExqZDKrreeCkHJUh3F_hn4qR8bQ4rPuq-oWIfDsIsAGn0eGMO2qo0U588xawtLVNDUcIvGGzrSWU_shJTF8SAbhezmUgLwrheHzkaj6VAzMlKYz3G3R9MlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌پیگیری‌های‌پرشیانا؛‌پاسخ‌فیفا به درخواست باشگاه استقلال برای‌جذب 3 بازیکن آزاد بعد از بسته شدن پنجره نقل و انتقالات تابستانی لیگ برتر منفی بوده و پنجره ابی‌ها درنیم‌فصل رسما بازخواهدشد و این باشگاه مجوز جذب بازیکنان مدنظرش رو داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28545" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🗓
#تقویم
؛ 3 سال پیش درچنین‌روزی؛ لیونل مسی تو اولین بازیش درلیگ MLS این گلو به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28544" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28543">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za9iOMQr36BC1nb7JEYfQ4zWRjwRovU6aZ8pWsLutJSxvMgqyQlhEDRWmm2coDozbt6ApejjXAN5lTLZrbFvF_JrKWKgt4qr7X_CpIrBlGCTIReP8Fkz0YTG84jCV5O7smoQlQl4qNoko087DWRNp3o1JiRLe2kH1VSmRDpE86RGd6jc8bVwmZKOOQ3hKR7Ikc14z0HZgEMKDNeQSviueh-nJlZ4dAPwmiwNDVcWntYCMMP7BYHbXubsfsRf2q8Ko1MWnFgnpruTF85eFbWEUxwQiezeYib6X6_TTkbvSlEL15RWRR1t0Lz6g6Xuo4S1I-Er-cw-2YqtPoPSHs5K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28543" target="_blank">📅 22:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=cZCqkHB1hB29MlH8zHUmrsAv5tVfVwL5tP629vXpd6-k42KJ5vaZFkKwPQFNNlEzPMIbBKfc1G2yipr2kZYiC3Ki8pDA6aHuzcysqa1Hw6BBOgrRXYq-PM5WZvorPR71q-N886uY_LSzbbrXpTLMuVfHHFrmB2Vs1-DdGB49Mc4vD-zMuUN8goZL0asy7a0l4ug4nkS-J2Y-7yBC8cT0l1OsByNIqIPEQkam7hL7j6oee8Znb6UrySIWkDWKm7t1fqC-ducJ2aXVvQEl3elQfbgej2zOeXlCUOt6_pGrRR8RXE--vDGp84fajLy-tAv7v3cFUA2j4uvKs1KEaQscfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=cZCqkHB1hB29MlH8zHUmrsAv5tVfVwL5tP629vXpd6-k42KJ5vaZFkKwPQFNNlEzPMIbBKfc1G2yipr2kZYiC3Ki8pDA6aHuzcysqa1Hw6BBOgrRXYq-PM5WZvorPR71q-N886uY_LSzbbrXpTLMuVfHHFrmB2Vs1-DdGB49Mc4vD-zMuUN8goZL0asy7a0l4ug4nkS-J2Y-7yBC8cT0l1OsByNIqIPEQkam7hL7j6oee8Znb6UrySIWkDWKm7t1fqC-ducJ2aXVvQEl3elQfbgej2zOeXlCUOt6_pGrRR8RXE--vDGp84fajLy-tAv7v3cFUA2j4uvKs1KEaQscfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانهTRTاسپورت: بعد از جذب لوکاکو، باشگاه فنرباغچه‌بدرخواست اسماعیل کارتال سرمربی ترکیه ای خود خواستارجذب رافائل لیائو شده و قصد داره با آفر سنگین او رو از منچستریونایتد هایجک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28542" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28541">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X63QF1PJ3R7VobgePi13n0jYbE5F6WEs2F6FjoNyLNZjX1cKBiTYT1KWWCe-lZy4e6KcCnOEP0X4QfWEDASdcg1_kcRV8I1DAzuK9KQlHloKeJGM4Gi5SGp8ssWTAhtviPXcgzF1aXRut8yJL2UmKlLXkxaPMaiaxB-4dUdsHDTutNBzcMj6WO9EsCVc479GWY4vscNQ1m5KV1LFsItcOOTxEDFL8Qlol-z3MedVgcv9i7CYXd_-LPXOvmPwPw0_VyPB9CpaezR79iJ6YwzGffV2l5b8umusl1ztN09o-jRwSAC0kw1t_WEU2ff3_U4W0d2BC5lkuDEnX3w3MYkfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
آستون‌ویلا با پرداخت 65 میلیون یورو به چلسی نیکولاس جکسون ستاره‌سنگالی این‌تیم رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28541" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIS8_j9ovHZCbLNYvXnxK7J_Yxc9Jgd24iNuu1sRsj1TM-HobjK8oZLky_KRpWdHFjsr_QLZ-iMqW97bAndYmTfT41GMKWZeVm_28ffrzotwmVOmlyQmZYXKWj3hut0JZxQDm3e8xh8_GT-a4NXPOdcI4QIu5jrvLqv-H5Ud6J7nCHlt_a6zERKCPr-qjj09ktAicjZHqYXREKCcn3p7SurY1c2jgD2hBtNbZPjw_i-fcyL5xd7YOqpvmJvzkcG4rL37gdFh41NZ9HAK3D4W40vA-lRVQ9hEAKWXUckMcoEsbELzt5en8GhtjwizIn49qQLPXL9IF8No_nmcUFjFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fz8OgMQ4mqPrztPdM5NFIRJ9BsmTx6wdFLW9Mjbpu0XUKyAjuWPg8kU5ftIZfArB5HdumnfvOFdXnhPoG9Plp9cjXvikDz4cIUdLV9troEhpgNM-B71xOXeDQSUx04MiYWZGYq9kA1jN8yoDd2BFaT3zxH-cupbKDZYS4DqHUI4eKtp1I0zajrVhNqyx3m8Yo9JnO0cYOyb9OAEmVbY9y0pnhLoe6FX0qGATzdNwjWgqhAKytJJ74ozGnRoVNE8PhPudEPnZiYYiaIT_ZjAZlR98HzvpuBULKDBEWm0Q-Y1o3AFX4X9iUCc_laxoJbwl12j6wpGfjEaOaO9dD_iIdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9Uxfu3edO71ebAh-fAhOclQKAgZv3Yj8XqrOdMYzZ1p4f0Hprj_fRtiAWObDZWM-eTQd0HLGETHYaeIu16Xhesu-CmjjFk6m7UlFt0_5FUaxANPy6TZ7PvCLUUim2vLEbg0S4mhb_6isgGfoQk_2OGmFXTczsB4qfPEssHgWbZLIv0m4s8j-RH6FYs-ZLipIL2Sy1rRRSpwM0x3x7fObWLvCvZSB8ISJffxqE18raro4n94vR6OHK2y0mUuCugDKJlzN39niOvsChiLkZB4aAtmLLcQSfszvMG1PTdWmdOX0mLwdDXELFCHjnWoacsgG7it41WPWN7Er6skBKOwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aba91807.mp4?token=ewxa3yQ9zZBOBrStBV-7i0CNHaJD6tT7ffVzdfgDKCV03W0y3PjqKTgWnLHyeswcRUYmlDWf13-tA_LYdSiJzZpubINL9E-V76wXfG_Y4t9L2B-i35M06-hxaZu4osTl8RbWIhqL6EMJFdpAejYKH_laUstHgZZYEciz_asBjdu9F2556Z8QqTbfj_PwZuWHGhvumAO8jRaaU80dzkgTtVWC-a8faiHvWZ_JYCV2YBo9vUVJ9dCX2wFjTDZk3ARB3ggX9qhs1K8Fk_NGmkK0vE05SNPxvhGvVPVDB8NgHMrB77jOhfW20FrPvZy0Ep9u6OobFkVgZa_mRnwrYuV79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aba91807.mp4?token=ewxa3yQ9zZBOBrStBV-7i0CNHaJD6tT7ffVzdfgDKCV03W0y3PjqKTgWnLHyeswcRUYmlDWf13-tA_LYdSiJzZpubINL9E-V76wXfG_Y4t9L2B-i35M06-hxaZu4osTl8RbWIhqL6EMJFdpAejYKH_laUstHgZZYEciz_asBjdu9F2556Z8QqTbfj_PwZuWHGhvumAO8jRaaU80dzkgTtVWC-a8faiHvWZ_JYCV2YBo9vUVJ9dCX2wFjTDZk3ARB3ggX9qhs1K8Fk_NGmkK0vE05SNPxvhGvVPVDB8NgHMrB77jOhfW20FrPvZy0Ep9u6OobFkVgZa_mRnwrYuV79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی از سیوهای حبیب فرعباسی دروازه‌بان بی ادعای استقلال در سه هفته ابتدایی لیگ برتر که سه کلین شیت برای آبی‌ها به ارمغان آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=Zse-1niqPWrf0hgIVANXWDv2QrVezqEPXz_3Hbvlp6uXJMzACnPsuy9BPzaLLWU8x2b-qkK378c4izE-aLVyxEOAcf4YlKvc0VLLfcr-HRJeN60t5_5ISSJZdRGGHDQVBiffbAlplvm0vXwpKb5PVPs-MXUMSQeUw7Ixq5X3sGBLIGNcEP8R-bLHFjon-0hG36xytVCD_3F2VsgoFIM-1O_E0DSLzAlbXLnoVT2DDurSE3O_zbKjYoov3aTGXbo8kCjm3ABEQQxA9yPrMmPYrmDzRkPMEaCox_mACU507pdHfIRuKfEJ1PltQaSbOBfpF4sO50-5Gin94Rjb15OmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=Zse-1niqPWrf0hgIVANXWDv2QrVezqEPXz_3Hbvlp6uXJMzACnPsuy9BPzaLLWU8x2b-qkK378c4izE-aLVyxEOAcf4YlKvc0VLLfcr-HRJeN60t5_5ISSJZdRGGHDQVBiffbAlplvm0vXwpKb5PVPs-MXUMSQeUw7Ixq5X3sGBLIGNcEP8R-bLHFjon-0hG36xytVCD_3F2VsgoFIM-1O_E0DSLzAlbXLnoVT2DDurSE3O_zbKjYoov3aTGXbo8kCjm3ABEQQxA9yPrMmPYrmDzRkPMEaCox_mACU507pdHfIRuKfEJ1PltQaSbOBfpF4sO50-5Gin94Rjb15OmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد رونمایی از اولین آیفون تاشو با نام اولترا باشیم. اما احتمالاً خبری از مدل استاندارد آیفون ۱۸ تا بهار ۲۰۲۷ نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28535">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATIw0SSpBLhr-WeJrXdKEeE_JX5Ke_H8Ad-vsO_i2PWSarC_ibjxxdcCjfriEcBrVgn2Mh9h3VUQDuT1f6rns4qVmHowrfa_I6vfg4L29EImTvMG0Hmfej8_fbWRvYvaAvFUfUNzKZdywkITDI5jLtfhseFWnYwo2wJ2V9EgRoJ0x_3PBK8eM6nV2OnXGgFmOqTDA-CkB7EHzlgCPBL3J0iXaczG719RktJzGiLOflfq9609HeruW2K0F7H6IH5LTHE4XlmKOfEWsbdKWI1QlAPY25K1pcu7tHS2t9yFVYSbIyfhEcoSYpyk2pL5qLICbd9ua-O8lUwhP6ORj5Ae3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ هکتور فورت ستاره جوان بارسلونا در آستانه عقد قراردادی چهار با دورتموند قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28535" target="_blank">📅 19:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=T0NlySckwIjNFhkrUn9N-La6NAEXdcHx6FmJIJTCUeMJvg-cMitS6xxT4aAe7aPa2sWB8IhYIYMv8wH1KSuzDKY0fU64F94WnjlNyoPZTqicNrfyh5KxOd7AEMQL0GEn2imcpZLVIYlGEp4jmyK4aIsXzWmsRly-M1Rzp6_oPSxT9p1MusFrGVbozBLMJBBAlgLM_pGeNYUc966EIE99pMB5lMZ0idi5RyqU2I85FGwhy8jmBOSr8Q7wEu19zr_A6vOurBC3OTJ5LBbEW5e9Ywnr7rWUxqCUkWRsn2oRDl0gQKxInAG3SYnN1v4rbjT-MqHrug3RB8eIlIVbnhBbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=T0NlySckwIjNFhkrUn9N-La6NAEXdcHx6FmJIJTCUeMJvg-cMitS6xxT4aAe7aPa2sWB8IhYIYMv8wH1KSuzDKY0fU64F94WnjlNyoPZTqicNrfyh5KxOd7AEMQL0GEn2imcpZLVIYlGEp4jmyK4aIsXzWmsRly-M1Rzp6_oPSxT9p1MusFrGVbozBLMJBBAlgLM_pGeNYUc966EIE99pMB5lMZ0idi5RyqU2I85FGwhy8jmBOSr8Q7wEu19zr_A6vOurBC3OTJ5LBbEW5e9Ywnr7rWUxqCUkWRsn2oRDl0gQKxInAG3SYnN1v4rbjT-MqHrug3RB8eIlIVbnhBbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صحبت‌های جالب عادل درخصوص یکی‌از پیمان کارهای ایرانی استادیوم 105 هزار نفری نیوکمپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZkXC4RCD8yc3yKjoK_IVR2bXdnr5jPdIYpnpSRpntiSRe33YmIrfGblkQRMx86SfNZhwX4qxxSfZLGBteX6AXhVNW13XI7ztwnX03smcMsbqlySdEp5Cq99RJRBvVWk4WP7fTG1_bdVcEUqbJM3S3-cx1t7xFM1qQJR3vBSqtDYYd1YY3cVXc0KJLSLb800rRUOxWYT-vL0ft9Q8aqPF2RzNezmNxniObsuIt6gDIDCO1unxLWYQhg9aBpi_eU1nrX4Fy2sTVev5cnHDTJ9LsdULKNQ3fDd-hb-K944j1kNQXNmliAnwmJlnErYlQTiyAST70h8nBQdObaoQC7lkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSk67b1YkbbfNMwIcF3ORUJa08k6u5xDOHuBtdfyg_PiefeX6e3LQQ07MUD9z5UCYADRqsZqcfOABfsg8kXM5uhDervI41pH3Ja1b5Iu2gqE0_GZLmWQX_oBmvxmZe3ZLpHeP423cipxJIEooaaQ_R1mQNN5QHhwkbdRcydINzG8bRS1DSTAFSYyZuFzj7dTqLQPK2pVHAoZUKjmw1iu6CrhWz5xYDY9TO_7kFcP0dkthgYcD30pSYpRoMs17XqImL0tEea_pduT5ccO14nLfxftkB4KLgzJzjXDqXAHbKbNiD_ESfR1wtf5oW5275GJEETSnEyvx2EjUlM-EQidLdqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSk67b1YkbbfNMwIcF3ORUJa08k6u5xDOHuBtdfyg_PiefeX6e3LQQ07MUD9z5UCYADRqsZqcfOABfsg8kXM5uhDervI41pH3Ja1b5Iu2gqE0_GZLmWQX_oBmvxmZe3ZLpHeP423cipxJIEooaaQ_R1mQNN5QHhwkbdRcydINzG8bRS1DSTAFSYyZuFzj7dTqLQPK2pVHAoZUKjmw1iu6CrhWz5xYDY9TO_7kFcP0dkthgYcD30pSYpRoMs17XqImL0tEea_pduT5ccO14nLfxftkB4KLgzJzjXDqXAHbKbNiD_ESfR1wtf5oW5275GJEETSnEyvx2EjUlM-EQidLdqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwUIsZa6OzVkJKXrDqWfHRzIFJcaw70FLvkKb8C6vo4MZUiAl96uY5tn4foAow2UGOsHjSfAhBdTMAivfT_vAc9qxwBRuoefl0kjfTnVh16Jm-YeBf9-4HAwRR9fb3hue54YDt4keZnn6FaY-VQo9IzPCq3ZPN-6j2pFiBXHc84KlCvSiiQfrM7S0YSGjxNa3tnMiQqo2Jtn2eZmHC1FHgGQhKX6ifjPK-OMvFPssViag93KF2tsSvukxWe_eyUluAkUAmlpcwg72QxR4UU94CCaszFVHNJXP5e5agXCVrGx6Ui0Ij4oO_cb-vxRJ6ZCVOKL4F0QegOHglQQtUtZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=bKAYcbON0ShDNhKJzsP3mW4YqVLoQQaxExZiW1yWQrd2Pk-8gJfWAdlLm5q7wwzFxZTtarSMg4MWIRFnuCRtYU7FlAJMJgLHWXE1JMl29UHHP3z5VklJNyjbsqx0S6Hzga2hKSrnRQfMYuXmcFRVOO6nsYQmyHWLn7UI88XkngxbWIjihFn711r8wvB1z78CvkHlXW2lecFqcQ7sv8TSn9H92DnNd0ttuLedzMtZ4Ki_hsw25riqEVu7Y24gEqEjux-e_GOo4tRECdj0cr4x6qsXqSvcaMxWWO5pLh2h95r_bM6qvMThexSsKIEwcutp8sEa4apehEiARSGKf_nCFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=bKAYcbON0ShDNhKJzsP3mW4YqVLoQQaxExZiW1yWQrd2Pk-8gJfWAdlLm5q7wwzFxZTtarSMg4MWIRFnuCRtYU7FlAJMJgLHWXE1JMl29UHHP3z5VklJNyjbsqx0S6Hzga2hKSrnRQfMYuXmcFRVOO6nsYQmyHWLn7UI88XkngxbWIjihFn711r8wvB1z78CvkHlXW2lecFqcQ7sv8TSn9H92DnNd0ttuLedzMtZ4Ki_hsw25riqEVu7Y24gEqEjux-e_GOo4tRECdj0cr4x6qsXqSvcaMxWWO5pLh2h95r_bM6qvMThexSsKIEwcutp8sEa4apehEiARSGKf_nCFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etqtuS8C9JSSIYccQAYtz6UAkY1P1HSEe-jsEsvdxh8tkYRmry6vG7TBj8hRMgzDUwO6vXY8KVRGDIXNXzCR-Uf7tjkTulAysTuxEKrrXf6O3KyIu6HmXoC0L9tKArBz-Nk5f_XUGVt0-_oYnL2ApT50zzcFyv5P91yIpReDzhTiaZbiG-IVOXODtCQz5VaNjWdRRtbTjKomsKDruTPD0QAuWX00fDBYmxeg0HDlcJIRCC-XMRji2KvJF5bIeuGKB6jWX7vb58gYVnhZYtYIp0EYlp7iCoRVGgWeMLbPhyXPjuEDKx0kdIj_U6Xf8LTr6Qz3Kn2vTg_mobMLh9slQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I75SiaPHjpCnlvEc9-pErEf4Bf1JKXFgdbC5ZZYOW51OycvD2EhG2lP961TgGgOCd5--9M8BCUCDfd5IMDbRIKnB34oelyK0Cq_M5NqhYClKwKqFZs6OdDC9VmD2Baa6I_bTy1v2o4gJDXmJAH098Jf61bqK7-O5AnjctvkgjezcrsMXdz70tjv7qyI33O5x7ytdoQNHR5MhFgQPX27z_FI40TVXfVPvnThgOdXdtrukPr5JCQ2a-u1t9SPTIt9yUvwwMinHmHZWM6VvLf8zOsWsGmTec-BF32MbQwreuCA6CnqZrUWFkpl5Ry2TgPz7D0a8AHKtTSSUGZzEw4ygqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRmVpXjgz9OBnn7v4UKKf-Y8PZ1WXRuqw9-KLawdFTcNbHiKOKLE5Zwlf7AUEm0H64a1FtCu-4YrUCvSg5snooVb96wRQhT6xs7SKJ53cBRpItI74aM1EwsoLpIl-POS2Lj0xkG8WL9Ylz3bR3KuxdbsqP3LZLwctAmCZFq_V7QopbDUTojTgBEnNzqaRAyHa8tl4xnpq4cyAyfFE-Ox08SboEHomjYH0VZhQa0Hj9NELf0SxxwlKtb31_Bz4dJLoQ1XLCgf1OVdlBkxe8ItEoSHzSLzCG_rKWl1P8Tsfg2a1u1RKbE9TfSPe6-KNxPOg0dXKYUBIEpyCsUrLL6YzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaZHsM6dT51N0_wGfjmbW-w7BVs1pkDmuELHLsdKxPoX80swjsrXIIZ4gqAqXj86MV-KsqI0E5SmpCdbBdwCgwKxtPrY9oQDS-yhis42ZkDilCl2o_cKgOKp1sTQD_2Xt9hk66w7NHlIRjX10dEQoFNoeWDKBhwYJwtr9SykNZZBJlYlZ-h5NTD9b0-ChZtdEqKal7RvAgQYmmqnU2f8Rfnd_Zb1KWgLnSS1u5JXGqwDvVavcd0tFei7bht9ahf-VVXWOK1noJ7fnkzTcIAjyPoypY4vCfDjBRgDtCKwosAbjDobR4tcKNeQPOyXGY-PhPvCWIJFztIcANL2FjEuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=VLZNoz0q6wdvbo6myO5xGCaTEm2_WerzWxh7eMv72JTDmIRu53Mk6Vo2Z6Tbk5hLtwxNoIqo6HO_-fRHmGVC8WUKBToYhHzQikVMR8GemdgIelxz0VrfiuMoasCfcXWYoNiJZARtgwGqn2ZGJxf-mASDphCZnm45fHd0zSvEeBP1TeeuT9OzVrB10tuxXuDN5QjE0bKBzBONc4nctRTxWPnSc2D4_CUBed_eB8EVPqyADfXTlCmLgTTX72zgQkbzcocUdTbXT8GzyZlIyy3sdlvWpfeANcM8cE3RstfQ5b9ykg6Z32NC0ZRUL2I9USy_D2mGWwA5tekmnsV7PUSEOzURZyoJLtY0ynpVzh2SJN3E3T0ugi5KQ4t06QwQRZm7JtuYni3kzk-MOOV0XY8H6-BlD2P2KO48uJ_5zc-It04_e5HbPT5cCqqdG_oL87l5hfGkka1DFbguTjOldmbccJnUUCBULc0TzdmJPda9QQTkFMNHWi_quZtAUcd3MelI0uF52I5wVBxPEJxWhlYfob21P_F5WWgkdRvgTntdNKNPGh93Lbq3Oui8ywYtPUqEB3ZOwPql_F4XnCCjhDNCnpT6iOfWKRvu_qpSYbuBT6H5lvQlhO81bS_iF03bKkpeeS1DSt9s-8208Sfi7tJepoMMBNYsCF1vmWn684RS2lc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=VLZNoz0q6wdvbo6myO5xGCaTEm2_WerzWxh7eMv72JTDmIRu53Mk6Vo2Z6Tbk5hLtwxNoIqo6HO_-fRHmGVC8WUKBToYhHzQikVMR8GemdgIelxz0VrfiuMoasCfcXWYoNiJZARtgwGqn2ZGJxf-mASDphCZnm45fHd0zSvEeBP1TeeuT9OzVrB10tuxXuDN5QjE0bKBzBONc4nctRTxWPnSc2D4_CUBed_eB8EVPqyADfXTlCmLgTTX72zgQkbzcocUdTbXT8GzyZlIyy3sdlvWpfeANcM8cE3RstfQ5b9ykg6Z32NC0ZRUL2I9USy_D2mGWwA5tekmnsV7PUSEOzURZyoJLtY0ynpVzh2SJN3E3T0ugi5KQ4t06QwQRZm7JtuYni3kzk-MOOV0XY8H6-BlD2P2KO48uJ_5zc-It04_e5HbPT5cCqqdG_oL87l5hfGkka1DFbguTjOldmbccJnUUCBULc0TzdmJPda9QQTkFMNHWi_quZtAUcd3MelI0uF52I5wVBxPEJxWhlYfob21P_F5WWgkdRvgTntdNKNPGh93Lbq3Oui8ywYtPUqEB3ZOwPql_F4XnCCjhDNCnpT6iOfWKRvu_qpSYbuBT6H5lvQlhO81bS_iF03bKkpeeS1DSt9s-8208Sfi7tJepoMMBNYsCF1vmWn684RS2lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
صحبت‌های محمدنوری سرمربی صنعت نفت خطاب به بازیکنان در رختکن به سبک نقی معمولی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZcOmXMbqy2_aH4d1f0bidOWLe5oJcYWv2Et3cPWQR3XVZVN2jY7rYPuMqG_hSOb99jbOMMHFUyuRrbv-yua5koxG2mYytyaH6aGPx_PaYKyqt1MB9xHv-W5nywW4zzDVbp35cj_cpkV9CZ-zX0u2MKd35eHhbSo_NENS4CUaatGR2v4bNjN-IFzHlxLanA8_HmD09cBUJEEDV1IqqrG8pWb8_t1psVNadJiydCpxhf5xd-AfpLExKwn_N3yMvGw5TY--SkpYUXyUZf5UfIEDzCqHjOu-rKZH1jWITkj09yzwpJRfBWfZHmcmLDJ9tG-wde87dC_blnx338kn_H-wWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMK1HtNO6xpRG55rCmU3IVBgZIHpDWJyx9x3ZYwmB1sgnb3FldHJxusv6Ug7Hl3FVpsDBMyCrSOplQ1OEdhh99l63rZW8IdLTv_MMWlXsg029z05qTsSBkrdAqVHLTxU5i8szVBWZkGR4zEKhM2QloofwRf_EGD8C_FdD9IzZyGrpcbup_0JZiG2ySt2j744EKqg9pNQqyQ5GsHPTDkTD4rn5VB_i89ENMTUNtwiAbYpVl5kvTG_mNMlNktH5prrm127VdmV2Ufeu8SqCNsLyh4CTUr79BNnF3eIcnwjMZW36A0pCHx9bgxeI5V3M2PC1WzCxTh376Ffw01w8QbbQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN3HMwh2CR6lAk-UGV6AtNxVbligiWBlMsNf2MUzRdyfkzhMcyiL_zMmNNg_1G4GzZAUfegSZUj9epUNQFtv26q8-ot0jlZG6TBhqNGMYiHVqdaKrCd1PEFh1EAP22mQHrZzGHyhzCET3iP2G-69RES2BbCi8VmR_q_s6PNqbGulpJqco3nqQReI0WNuDorjAI62dFUf0w7LVVCHP4biTE8UGc-WELLPZZ5x6CmXryWLO_axlEJvc1if2GgOarGK7pVPgwH6WIJB_7XD9JG5r2d_ZygTaACJlQo50h3oDQn_x9MFcaXOCcxke6Ps9BvsINygezt15knhBeGafKoG7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_LbN85eWEO93EOfsN3fmaPYnrIEV8ZhwO3ePwUPCzMpm9THsHfFE5I9hFrPafZBKJRFgQwg7NWt1Z0gXrgYcfScoq_GxGaow6ZW129ClvRf2wwa6SuG7EFSJFPKyPw0hzSU31lSEbu6p_SGcppO4XnWmpPTBcMkdcr2JIlzEL7s1LxJK9PUlTktf7QKZzkvtg5PbG5UvrC0K3jtsryB_qSCHSDZTdDX9oAmXXoMg1-ihVQqA2SWpoUCcu9nWubh-PABuXa2wC5jxq5hJmQM6GINutJmIqFgu5PpLF-XSdnnCDV0xz7fHUDDTMlUsHArNX9QVqkZQcK4ozyi07bfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHtFpvm4Xhg5mCWNDxq_2iP6NWJ8zIochhWVusgS4WVyVLdZjO6AfPXn6epK2-8FdeGbRAhbkb7RooFJ_HU5TpSPvGAA2ebR_zH2LtObIh73OnjycdWbxRcfgV8rMGJOeDeTuubdZLpmeLIIat7QU2eAtVD7sAa66xvta_B-Od_c7fXnxdH_awN3EEtQiOCbF_iJzlMv3ZeC0JnOXmHh9brqShjPRpwa7sWdafhA2y47ZXJ-TfMHCRzKLw-Ez9KveGiMOOOKWlvR--jYd0j_gACLg-8wLOLhRubfGM8-LMSFh1KFaVUatdmv-RZPVIZv_dEO68Uas884jyOW0mDkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Juefj4Qus7dIzfGnJ4ZCQncuxbuFLpmNZwTNLW-rejqbXulxQb7XOBatvZxSfZEAQFX8hwGcyZG8_yYwjRL4dx7Q6i-bdnvRMnPEQHqRabDcvHTLBKrdj-PXjubwoYeF_8nayWkC4ynkTmKWcnWddxqNeFDH-XWDtIDBbeMFiEWq_SWb_bFeTAecN1rOZEXgnjWLDwm3sY2pDK_tD4vMVh8_giIikTpZynEGGG72k5ZFEgG3X-dVsgBxzOCKKh-qmBjuDCjF0K-cG0nyZ74f1CdrlFHWie8Izxvvpr73Dt8piD1DuvavJNvSXiMyPhp1P4zU4bH3Wm_gueB1Z3SaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=S0ipd5Fd-OP3rkFRbUC2B5gyUxYEP8UzIckzQuK_x55UPQtsXfsZO-vz6RlRxcV6DdBB_bUpXKlMVb-xyR1RzGeCcOcD1zTH125npZSLEKAfFtN19SHrQDDCy3ewG74tvKLfvU2qmrjXigU8m61dXwv7FIr-8acpEW8tHfjmS6kMMPw08_8RKEoF7G9fvRiirO-5LQSbMbMnFn2dek8xi1aGDonIp-ewB-chcyTlWgKfbG5sBCsMGJa4EsHDC5LAj49Im26mQBju4x1oSIbjsRoyoiQlvLR9EWKpvdbmbMQIhzBgsX1XnBlsR9m3SJro8AWY7A6fzsvU4MKjPCeDpT1u8wkiDes9UUy4W1x8OQbJn8dTG_sxMMd1YFzdHuo60Kti75sO7264w3oamBpHOEIpFMZEballGczUTpGazti1WSDDxBENH_U0cX5Vh6qVFLWlbOXDLLHhtam6cFxembxyhLgw5G-6gjUxsopIwA5Lq4IWlSZaw9CELffwbm6b9OrBdpoFL4gijVlwSD1ytUXUSrzc7JMSzZuXMHlcBPoeUMJU79dkQ467u9NGZgfutSWX8rGRleTlyh4285utSiHWZX7rMW9N1cHx_HYEcLrkcNqmviG_iFN9NespIi90D4ppHSg63iXVVDCMWvaCm7e0SrOHRwCy_zdpc5fbF9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=S0ipd5Fd-OP3rkFRbUC2B5gyUxYEP8UzIckzQuK_x55UPQtsXfsZO-vz6RlRxcV6DdBB_bUpXKlMVb-xyR1RzGeCcOcD1zTH125npZSLEKAfFtN19SHrQDDCy3ewG74tvKLfvU2qmrjXigU8m61dXwv7FIr-8acpEW8tHfjmS6kMMPw08_8RKEoF7G9fvRiirO-5LQSbMbMnFn2dek8xi1aGDonIp-ewB-chcyTlWgKfbG5sBCsMGJa4EsHDC5LAj49Im26mQBju4x1oSIbjsRoyoiQlvLR9EWKpvdbmbMQIhzBgsX1XnBlsR9m3SJro8AWY7A6fzsvU4MKjPCeDpT1u8wkiDes9UUy4W1x8OQbJn8dTG_sxMMd1YFzdHuo60Kti75sO7264w3oamBpHOEIpFMZEballGczUTpGazti1WSDDxBENH_U0cX5Vh6qVFLWlbOXDLLHhtam6cFxembxyhLgw5G-6gjUxsopIwA5Lq4IWlSZaw9CELffwbm6b9OrBdpoFL4gijVlwSD1ytUXUSrzc7JMSzZuXMHlcBPoeUMJU79dkQ467u9NGZgfutSWX8rGRleTlyh4285utSiHWZX7rMW9N1cHx_HYEcLrkcNqmviG_iFN9NespIi90D4ppHSg63iXVVDCMWvaCm7e0SrOHRwCy_zdpc5fbF9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6eNbSOeEv62KNcTPq6PnJMz7M0ru7FKe0Vyl7c4QY2p9nt4-GjcZ20ydaOvdrWSVW6UKsQ-sEj9LXXZ-0Y0HkvlKCMs3tGvpauuXKJmm9AMfvoqk5UpVAd1JhcwJIR34dJ5zyzS-wTuunCeO3uly9hgPrpMMnVlkK0QO-BM_ff3XytvOYqpGb4uvTISIS5j0R5DDe_hfADI4jIa9sHufQw8_WiaDbwybQVvDSNWJLbOp1Xk2AXzmF7OXCsozjYWS_0JW8dRAgeCZ4OyVIx5-sjfbuQDGi7M7O_lmPANTVAIzGqWcNwWOGMuUiGMVsk7Fu_kigIR6PTBc-tqqQYnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuUW02vJvCjFk9olGLxb0918KPEraS-0n98-aUrZKdtgkxgDaVGBS87J3XaMzYi9_pHl9_Wk9Hfelr_hDuOVDCoHuwbSZ_xWByB2Hp5MklahVij27GtOZ-h_JPQaOc7mIel7WaiQ0pniesRYHUZeWBr56ZKIahlTzWGgv4f3P6IGFvnNVtNt68v3trhO2GPdP41H7ServMZn-D4ubiCImrfZyQKZ2BXqf1PVWG8LoqWaZK9jkFPzD_846moWHyqF979L_O88rg41iBmchuqXqqXCn4Xagf5Kla7B2_n7kqk_9eheWvPVG8k6KmLKFevctuNudJ5eOU1lxCmIlaPirw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
