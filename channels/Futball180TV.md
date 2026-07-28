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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 519K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoj9O8u2w1hi1S9tQztRtwls3r-Stm04PBqjsKwg6HP07zJcRC2L_IAgRHRIwFBg3KvMfXRym0-MSzUhG2P7SdOFpvDE5s4TnMgONX1PjFHopNEPn3E4DW3sO8HKnIuY_GBSMoPE7u3OGxT0dm80xTAQOj5ynkQKN6BbvCTyg4lzmbqmxEULmEEIg0iOc5AWCjIfQQvmgPhJKX4-BSddT2sKvJgHT3QfVkXNcIAZE4wHzrS3NpDjW-WtaGWC_IhPDNVAIWUE16GsHtZqRb0x3yoAccrixXQzeYqUbp2QkxuxJGcU_ITenpMlD2_EyHQFtvEKSM7T2ThKWUKhZ1I0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjb6-pnzDmprmuJk3LPiBPFtcL2cPuZU9SV5FkcUCfUfkMdOZ4zwgO5mL4fCkg67G3evqQdiCaCS9c7MEGzSOoHq5M8k5g2R8jCgMX-XHOG5ELhbkM2oj-wfBwntKToZIGkMPkaMeLFS9DwybAowiSBOu02CW86Fi8UvDQPK1fZcawtQOr7YwAjWSkuZFzIzeC9hx1hqXapSJeVJUY6tcw0Xop_h84JpWn6Oh4OQjbgdYC9ZW_85trPMt95sRb8-afWRYnxHAtYSBGZnpGu2lsbavCxB6PqWflzlWk1bLhu8MkwkrPKFtT20yTrQfm_Aln3gdQT-9WJ6Bwt7OMqhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoBhxsxdKHAONZ3jtq_svla7rdRx1cSitgfTM4bXNxgaAX4LRw8A4VKYqAvIbH-HDcMrYUUmP_Qqh8LN5ZwPqO286BlyNgHOqj95M09AOG7lhP9JOnsvB5GPa62vN_fltwWJ-pFM1gnRxaggija6Ob0G-Ph9dIe5_ukw9fp-MaCTNyTAPczOy-rbCMW0qs-9gapCc7nWCeztL5spSudHxYm_8M4mTnKxSA0IC9m0LzNZ1HuEcVpYyfWdMjYoweNHm9ZjCPYeqbDzIY5HFaGyCDyx7twAeO592RKxwDFtFhL4IM6taQJ5fS4Ve4BSuuX5-tFVezVJ79StsF1hriFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVNKw5JVl66Szvb2AkjuukNI7zu_4_qDBxj6SEPkFRl-ecUQKSqIA09x7kh0t_5m0CUbTqWT8moSgjREbKKlGRdr3uqZwATffMISpJXunUjaNSGC1aQTjZuHgb_qZlP3kL5Isfn7bMytT0AaR8g4JWIlvalyrtq1znXVgeNnjVcYm8phHU2y75gdrsk7wHsqwp2U_gb5jfh4L6qjOX93Qsb6FpfvqL-UMLoVtES4e9JIKx2hfNV6z-AsbMXVZ3B97jamQBDGicJgXGnsWnMjTe0E2r4P0b--QGXd143fD0dJzO-gC-oAer_x_O8NapB6NbhefS_lF0yv2S69ZgVYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq0iXaaicdVpXAmuSld-PH3gH3h0pTysAdTFHR49jFwKC12aMFqcTRiw4QRx-CZqfvaA4e_1yVK9YJTnTbwujJyWWmMTxDS163rPcbFUvMWksQ2NQiWnjPlWQ1rD6ew2G3wpGuOdyHeBLdeDgAwdIJFeN8sMnRVGWrdzvybHN8MQaCdSJLhZ2cQMumeavPjg-97LI3nEtp7u04LsFZSD_U8Tb240-6ERuLUX3eWjr1AJ0WybnPHJ5gvVOxb9yh1ExdJeNN4YHMQZmIwd0twoRqlw1PhLIdrVyqhCcUMiF-R0gDQxVj0qTfnnrAe3Pyg2aLveumUsfOa4ki8I1Otjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD5ka-4F9pbmf4NfyxziuDhsldzHyeHdzv4vuzChAInisz0dTBMIwJ5ehhtSk8uIxVj48f8XhjlCO8GGTIONfADkmbWeYq2Jbc4goxc7uHdAQ3SnJozbPQTb3pX6UkqQGNacKYDPzhRYO2rKHvZKEzTz0nAE9uy7V3y0M-2Udd1nmUJ99aaPd8IUZzX27GoiSGE-pafIZcaE14CctrFJ1bVtq1vC1-8mXx9gnsA_Ih9Q9DF9ih6DZFa6TqAKP7z-621HHEfYhj2cR5aN7EGMNZyopzsrFomoOGmKalw7g95r6O5Ydn0jrcsjOoTTEE-iolNRfsyiaS3t_k4EI-ZpGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WagISHqPqPD3xBhl3TjGbm53-h9acJ32rLFhXFHNSa328c3whBqZ2GnSaq7Rnzcne7Sa8vkl9ZgCeuokY7OWXxZj5Z1EwtU-ldNhQCxrJ_v_XvCfetbVntQfSyG4i6Xzo4b5Ut5N0PeXPU3FcMwmGuIABHSpAavpU0O6phUfk5g1Ro4iOIuSsWE-Wx80GZF94U3cR1U2tf4tIeZ30ktJMuuzDsnR1HkknEfcd3oydi7pKTEeHyWLbVaRLEy4onMa_pgpvCy4M1fV-MSw7hXjqxtQrDZ0-EHGlXW0uQVPJgFKPCovxsO3OaQegsAvamVOpBHza8FLG1SF_aVFLRIv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlObJskKKrx9Po9y6OLvAuHxfaDQxTgMkQFPJpEzv0eh0OZzfoMe593-zbYYSc4tB4Q5RU_Ay-yiA4JfK13zvZp6g6m52QWZYjwsiWp7heWUhy9TUJeAXJMp0tHEQBTI8Hz5jT07zo3FdQhyoUGnICczv90ReCIf9qVmlBodaSqBT0TVM272ad49hCYIKBo0P6xpMyphU7wfm6XcqSvY1md4Xi5uBziPokSvWrwlssVIAq14lCCL_Ll_s7233AzOiJ5DM4Ap0nYt1kgYc6mvkSelHexOgX1GMDQrptPtqC4AgHltcKN_ds_4ROCxx6ekw-HnWfsSEmluUgTtonmINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzgFRUA5qXGmmHLHiXAW08HIMbtoYgI0e2KZuCqz0dOoTqIYu90EiQwq5vm7kJkSnwAuzV-H1f03WzM5QJe9yR-VxTXCl85OWQ5R2sgTXnubwB3w_mNgenyp-sBKytrAwu2Mhjdh2jZLyvuovGEd5aTI2cRLKMS25O1icqgj5j6BWfP-Rf78f2VCByj6wUkCTEdJimRwsjaTz0fyoMlqGrcoMpZNguucCUmDqx0nJ9T-OvC7aQJKas900-t9TJbrGULd5y3AECyDiEpPRUQlEuudv9cp-LE5hXnuaQ-xjvT2k0FPL97FwAZ6CxmAuhqyl1PbPMOAWqvkFwslMRklww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpC2eyjADYddrM7ryjTL_td8U-X2R3McUhiQXIBqwcdjaz1H_P7mvQCnaBKG3n8vzixOOl2jqKrPMnOhtqcrLoGyS0mVn8-BIMBqAYYVHUDQLVkYsiBqgEQeVKUXXN09lU6tmCC3SpfvtqtvLki56qrXXJAgTjsjMr1iamLOtbbULVp2vQvxcyDMw9SXge5Hj2sl1rQeRUv8zm5i5iXrjRR65dg_7EKOLZpr48HqjJZmE3h57vrfTuBdolb1jCbaXQEje8D_dbgfPN7AivMJrgikNtp6dXfn7CTQPosJSXqNnlH9UpQ2nu7jSjC6KmmRolHI2K7VPwaHEhLZ7irdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=V4PRM22_jO0J9r5eS2qVoN4cjflvaI_qdn6SAKkuuvGPVM9d9QSnZ-lenqNFqBvuKAU0Hk-18ZuubErXp42nQkS_4MLSkMDDs_4lqBrXtFpt4F-LTSrTOheRcZ7vFP9xoeCat3zXy5IvWh4-DEJAnl2YxzyuHdjVt-lL47JI-kspMCt8hU5QF_W6eu4Vhy1BjTMyXIw6y_up2WuX4b5w11DYMLMuQuWOqCv8GZZwoji5b1Uex0xRDURm0nFU4ZjH5hYl0YxwKFn6r3B8zTKRNJNvPW7kRv4giH1t0y3GIlBppVREsXOQEG-fTlf19tX5JFcN530MiKMxvxNEbZj_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=V4PRM22_jO0J9r5eS2qVoN4cjflvaI_qdn6SAKkuuvGPVM9d9QSnZ-lenqNFqBvuKAU0Hk-18ZuubErXp42nQkS_4MLSkMDDs_4lqBrXtFpt4F-LTSrTOheRcZ7vFP9xoeCat3zXy5IvWh4-DEJAnl2YxzyuHdjVt-lL47JI-kspMCt8hU5QF_W6eu4Vhy1BjTMyXIw6y_up2WuX4b5w11DYMLMuQuWOqCv8GZZwoji5b1Uex0xRDURm0nFU4ZjH5hYl0YxwKFn6r3B8zTKRNJNvPW7kRv4giH1t0y3GIlBppVREsXOQEG-fTlf19tX5JFcN530MiKMxvxNEbZj_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcXt6VHpJyLQD6AVmFxHgIgxN6YLXGgoWSHVkWv--bTYLU4_AIbgOUWlvku2Bzrc8KQnNRa4pFEZava8iKd_ONWsXeYEj8ZoD-qZfLZL8uh5KegKFOCnxGBAdktxf_MlkpFNwWUpJqHBatW1mSphbinC-Nd3h5EpqknL-3a7Y54W69lxy6e9tcoYUq2HP70jCrKGWwp63voK5CHOJQW5_aBylvUMTzV1NLGEzGkX5D9iBOKTNt1OqAIiPhRIEquhZ7jQ2EkYQOzqZ2jZ8WfY8Xa1gA6vex-vOrDpnSQ9zdJ0lJL1gLfuLq2oP4kLL93CxH-5KFqPTLeiCR1FrLLgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1LMa9Q66cuGTRuOfthPVQRdr9OIo3EHmWq3WAqZv4QgHnRGDqn9A7jReKVqQ-3ZPXsjS3LFjZDYfbiL41GU8AUa0zIa1UFM78nlS6bqu3Ke1hHD07WlFGpL8EQOorekG_7kiMVn5T6GkmBIv7rtlxeDgoaYiVcK45Ij3EbbMKytcLL96Clov4Xngai_jynHHvMYvsRVzVe_Ge48Yb2jgJxDmlhBlDLXUi5R7ylcGgCUDLyCeNMeOeS35XHbfiRW3XqZxQ_3vOzOUo12oaIAThlbuq9kTZFfNB8i-GfSRnOPPywuG94tovKMrm_ixsVWaiCJn9oNFowA8EZYFyHL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urtWxM_KkDonZGYAM74oSMQgeTGhfkIJOoLc1OUTP-MEjvSyb4qrtJcpUvU_z1LI567ZYNyxFD1URVUUV1VHBetxp8f1CiH8OGqSoDy7-jVFXyDkRG0hHGhO4MXh_E8vKB1LyOmd4sC4NcUFQGlf0-AE3ikG1hSCfF1ZyHloRt299Vg3x6LRxSjObvw7rtD6RVGAf7-e__-8CDfXHzATyaGHOEBGqzlYjV7lmaqmhwyXjtgEPMS9lWfirkV4rwqTpSoLzxDYS5AwLlV-PNReCVNE5KKHG05dmabcVKG6nw9vNUEqJgGkjOjvpOeIxzdVceSbPYI5H9rtn-851lBvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5WA6Qk8QfdVGPeUEAKyjV7yZ3iFYE9TgVustaZfook6OX8Sj5SUn8idSXJYsxT828dFIS_xkwUDhaVsgSMvsGKlH7Nf5sRwhlscMqnP1MESIhAdkKhXjZLgU_ieFEva7EpGSQGCOIQYkMrnSGSutJuimsvUsH7alDMvcrI8577j6Padc8lcIMUXb27t-QDdsEmr6NMAHwuVzjtiz-yxfFlAfA95C7CdSqlZGVYq2KiwbfR4q9e36g_y1uQ3yhcsJkeaY6vNEfkaiWLaKskO8i_eNfkCO01Ql2iLveNuLOGKNU4JvS7PKd6PLbV_4p9fGVNARyTciMLwAc_4yH4g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmnOI1wHHLZ-DSvIVIib3E-LbipKc9WShrOJ1tXWaqtmI19mFp8bwQcYx3BtWQ_PhyNi7Dt-eoCU_iDOwIJ9We324jGAWBCaAE6OIeY74Hb-jZuG2n012xH-AxhnbCelhb9H7mfYpk4HVZJ3vaSzY00qX8CEYpMGTGcRNA1KQ8687w47ZhV1L2prrrkr4LNhzdjXR7Ha4le3nhx0b7v1_n_Mu-L7quy3eprUlbt0aRXK-AXkh59ZXbebrAQIEWEa5YrWOiujFobZos2L2Dd5APq37PFRGV3oL6N9pfhZdqnPe6xASkuEV6URtQG8_zLUQtBN2hUTJBr9YtP112vn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=t8Aui_UJRHfbOjkdB3-H087DGTzWZ29p038iNQFUXtvKmmQRkGWg0H9Bl5d3d7sD13hItCaP_pN-2fGxQVnnzMvTKDgh4DtFB5a1BTkzsZIsBjBKn5e08CXLuCNYTdzXDuucdmbl5cIoK-rracUIRsd7v-bgdVYNPr7iMhOBFVsZQlJAZYta9X2c_ktIY_XmdxF_DpOqbcwyvUdW7gjjiuHNW_b1fEqdUQR7Jq58Feqh3OJkkLEOmlYI2VIpnpoxchP5crlO1VelsDHq4NyFdPKgtu9ez3Ck4VCugDBMH69VG6-OurytDzJO8_YTOa10OEMMi8GLdjGfRym70tlEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=t8Aui_UJRHfbOjkdB3-H087DGTzWZ29p038iNQFUXtvKmmQRkGWg0H9Bl5d3d7sD13hItCaP_pN-2fGxQVnnzMvTKDgh4DtFB5a1BTkzsZIsBjBKn5e08CXLuCNYTdzXDuucdmbl5cIoK-rracUIRsd7v-bgdVYNPr7iMhOBFVsZQlJAZYta9X2c_ktIY_XmdxF_DpOqbcwyvUdW7gjjiuHNW_b1fEqdUQR7Jq58Feqh3OJkkLEOmlYI2VIpnpoxchP5crlO1VelsDHq4NyFdPKgtu9ez3Ck4VCugDBMH69VG6-OurytDzJO8_YTOa10OEMMi8GLdjGfRym70tlEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmba4M9vSkL-k4zOEo7LSrwY9V3jrGWLtEipKeLy_nKDTQZz6ZSq0s1OyEHA0cjI9c_zrL5NkDjgiDLir-R0C1RRmIjAEfU0umD3cZvPyVzAWifnlaIAkecKNucr2eJhVG-n4Dw9rE_SCMSutkmqjBrYJJt6MlvhZ4EX3cfnAjf056bYTW-gYpj7yNoN3aV3Y2gESLL6Np6fT_p0_J38zzTsPBbqNzMr6DFpVLmNO6-GTQywInex54IrDfoKkoJyOQ8Tk3ggRFJIngJaYTe_lFwxDJ2ezEQGJyZxHVXOTwLWUkDmvC3dmoNLO0YvsDB9o8V3tzWuCTOvok1myXYyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyDUNfHCSIIgkHAuh-k-XcXJQn7HJvZfrlsBH9QM4-QnoOg6G1t7IA9rWaViKq0xcEeVf0PVt2priac4Qy1mrHiMI-9A5uoRYm2WJw8LGyeflohxJhNCU6s7nml-oIUcnVkdPb15vGUSsEsI3G-2sCb5sIDCtvQGJY77M0-MBRtvO92O2C9jbFvradES2vzTDEUE1msa16fTf36D6oVX7mariygXrcva4Id0ksuoS9XLWkEF4m0idjhrpYMRWicfkta1FJKUu3gcllyeaW_oUDSnRVNEJ80HfWe2SMv5fLK4XtjsQzMu-Y7ETZXvEjABS_3qPGDcZSYbIcVzY_Bhzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=he-LiNg6_9T17biursuiLERmgdjkZTxlY21EF4-2fc9d5FWI90R-BV24FdZywm0HbYRIJHuhGJCeqRtAnrBOKdvLML1fNG8krpHlsXMqcvNP-ZjSmrhWwcDySRvU3w66A3eeenVuKym67rbmGWiVsL30-9D6FMrpsXcTP9-LsyxQsny4_eUgspOshF2n2EJ5hqZ4a64WI7XgqRA_ie9MKuydT6xAlsTEXRmXekZ7oxR7Ao7nvZe_8IiCg75lSw4DRvfTNIJvM7SI27N21ud8zhK8647FBdPXL3_W4Fm4UBzhJTZt3okRMdP-MD3rnDgiAH7iGBwaXjczZZHR_iunIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=he-LiNg6_9T17biursuiLERmgdjkZTxlY21EF4-2fc9d5FWI90R-BV24FdZywm0HbYRIJHuhGJCeqRtAnrBOKdvLML1fNG8krpHlsXMqcvNP-ZjSmrhWwcDySRvU3w66A3eeenVuKym67rbmGWiVsL30-9D6FMrpsXcTP9-LsyxQsny4_eUgspOshF2n2EJ5hqZ4a64WI7XgqRA_ie9MKuydT6xAlsTEXRmXekZ7oxR7Ao7nvZe_8IiCg75lSw4DRvfTNIJvM7SI27N21ud8zhK8647FBdPXL3_W4Fm4UBzhJTZt3okRMdP-MD3rnDgiAH7iGBwaXjczZZHR_iunIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfBgxnBuEnK1aFhxzYI1ydQGfF6b5KpzFtpsqUXy99ecr651qbHYvvWpBJfghX42SGgzTKhJA02n88LIqttLWfYJI7eo4v8mWgTIu6X4D5La4sWT9c6UBLZGOAwDUF67TZGMNdBcJ92CXnc1Higrxdezz8pNwbi4rc-v3s2BKaJIdyAI7S6Nj-sr3yX9lfLBnwY5fqUGSKVHVy41qtSqpgXkh6w5ZHCXKyekCvYl2y6P04bq8jF14XjlBtmGDzcVSkqT3VJC7PQ4_xXC4rk7JC-C6dqNjcGmBA6YOr8EhHdti3GS-WhWqzTFEpf5n7tt_KiSOT-GnX7QM1HjpVP-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOsPkChsUeRCu01aoiCtAWvm5doPpnhoScF8EigadQHHG3hRX4FpEqbtBJnhz6Hm0jKihnC6NDWIBPy3_qZb2w-rQOQVJUuukQOudCICuhTbPXrf9EDytEdPsC3tit-_jmTUB25NIvOJuv1BOV72HtUX8EKVbRYpcVk5Yy-7CWwgpAAKMvWw_jbrSpmwVjC7ytmTz_gk4IHlQXvYBPqcud99smLPGn7MkZ9ZaLTYduqd8biQeac0uvXDwu3Zvb0yjuDS7BHU0sYBRGXOQ7_r9h_R2L5OVT51rarNQZxRgPe0az2xflZkLd-ylgN2z1edeCdFvqa4Gy4rpN65kQQF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVoIofhK-aXnxWKvYDk-7j4sr4Buqi8g25osgx_BSBvcQ6j2IWS69cmhqDxUN0uCyBpdT91yhHkGOWFVliS6LT9edajnaSA8Zn7eAr-BWDE7JDyYMaxMHuBepc1q9e9Doo4k7TzH8p8WkPqcKgoBjZ4_G_x4kW7EkWVkygPTxD3qC_oKzYfhyJZYa21jAagyKV1HPMJVwBaPvkjhYpHbFrC3fKRIV9ZbKtzH1ZTSPsfggGsCdIssLnWMhWgZXSgWGM38DBPAErvBzcHyGjkfHYkYOghqepX3lZDIxk7eJrUkovsuSqfWFSkl9PGUmBFtjny4KJMLqUopdquY7eIPyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKPgOiakNKl53N_qnR4PubCQ0NNZfoGA2v0SFO7aQIwGCd0YPgI6DNTzke_pvg3HWnuX0SKz6O1nqjNtwoOJQ351uWanMcqQ3hYGWDjH1Xc-YYQjqPqNPbM4AveJgB42NhAOFjS8-DfSpSADOk47N2_fPulN2W-aWWhP0sv23RPt6h236jVTOyDdDV-peK1nATxE5Kt07DRoN8IM17dpTAi_zl1fwQaLy9QMSLwWPPgfISP6m-8021_iwmY7iLR0LKEHEJeV7ZGBZuDDIS9BNL_PX7WHv8SQ3cMWYjyYE-0MnqtDp64htpfmDZCFYEtC27no4_tna985woq9lIWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbGYpkD1jDEFQrZgnMmyLjxGDYmuF13BxasyhjYiQbMMvqQic-HYG-G6A9hrH3Xh77_crjvsNHJhe0Y2IHc-cilYwqZxaLoiIFmY_JMDAEsFzu7y4zVlzMdtqCjQbgrisoZaBUFvV3MUoB3fyF8repY8HgLoYfp9splQrl3NQo4525V8i7_n_zqq4BEr_EmdcWka5hahPswmXjGW13Bxi8_kBymtVsu749uswA7ooTqrMSjL3sb5hkMNZJma0nKH89mAFteEeCKPxBo65ydKIr8CXdGaK-OEIgy9dmtxIeD9-uqV4NpSL36E-3iUQCP2pxWQuE7EnheINW6o6MrunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZySUpoedLvmValKfuRzVO4_ywSpLcv1IxkIU7w_llg-lYT6zveoEe5kKzE8b231KRSxTl9cQX6Fyd7RAsrx8nhl8xRsfpPj2PaTqF1Z0HNj8QRyxcvvT4WaWWwJm1LtshCMzApAaNTRWdGS0CaQlCIi2nm5kM7mBq6py4B-lMZxquuHcfDpKxZSni3ROBI_WbfTcfCwdJGmw3Yj7_eUc8ZAj9O9FNXakwu4cnPslYXJW04ulorb4QWP15A6Q4EKViv3ldtiLHQ3zcRWPFekxZ-nnLdaWOCYfr_sm8gsCW-q6nhaRIYGK7Kfc4IdkCpRRUYfaCN43GFiiNpt18G1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLiA7rKCKMSyb88wfeHFDBDLu0NvWpAG8WAGyYLr333ZzlvZ2efoHZhc8VUDi_bbiaNdj-CQarCbvCW-A-9T6seGWy3g5Twwnsy0ul-ANtgRQ9nJ1uvr8m0nirMn2W03kn7tT6NNZwoo08AxoLWnX4DP2n65sUBhCBIL_LU0KuxnRJCL91sFzbnLss2PMiewLvTkmCISEY0kKNHFA6Apc3YVUKic8-gsUlQGsUYGXeM0e_xNe0WISrfZ1CiUIDfm5sWYqe5Kjzo_bJ2F3Nu7tVoE11crd5lG4XO0U9DNPqRsmbMlF2enRKQfeyxHW4SVtJBfKAQAJ5WPz_ZNgWpacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVf77KjXtwBH9q6JF5AsNT90x9Prs4Nes91JWtfpTKE8kd76X4c9ya00aVopC-1Ya_4uLExJnG_dQGze2ga_8fXQ2n9FmWiGyBhCTa6phJEJ1eP8KNCSLesHBUzlXsn7oCvXoE9c9PmcE-EqmYxN7F5NhO-SoOZWaZ4WEQeQiGSt4SIg9E53nQzlqpO6wVuVBK51hmRkRlAokCKUquodhNGnRvegGUyTixZCtSuM3QBzcVvAWMT4p5mlRR-L5Hi0GpcMqJjN8HETchmCi5u-61M4BlDtZMgTlT48fkVRtvkMl2LftBgkW-Qa2WLLZ4PRLat5t9Hh0h07f0squgKvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKPGpCIyeI0o5nrw2pQ1OKWnUUBgAAv0PpOoLcbR_U0k_IBHzyBQWemXH5wm3BMZGDCE1CuN3QL-4Vj1dDlCMGEd9KKjZsZvIUg-eQ3uW-aqNpgaJ6cu7fEHm2cu8CDvb9KqfTtweSkyzknS6iuStj4RwMKN6rmPV2hPfmtkNkAQRNEboZgEWyDsNGk960jaSXIlsKkwbQ9u1SibmPYX868k_zy_5eEDmLJ2mVT4nErcqd2_Lecb9qpc4e8oKPoqKQrGQ_OOs0s6iGK3Koq4Q7QJi6y4S1SQ-UDSTTX_MXDWMDnv54zNChGrPbSEsea3MbwzIMnjqyYn0pKPxzubcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxX90uO7T6MshIvu7FOR3gU-ovvc0yVVPM32mteDbyVundhx44bvYPchc5PCZ9yEm-sjn0IVEsPVOabRfCnaqGsSNNJVNSNrUoyiijWyn_QqIYPM1V3s_HxcvivH4avCkZLcedJ8u0-RrZpVOH_XqssHBDXOrl0ZGA4XPf-lYTDqyq9VFEnBAZQL8xJDY8DZ-gWbQTm2vtx9wsphjgJaoeTib4Z891QODX3FybZ4bpTS67iWFaxOiDPHBQOug9jR0KY9eabC_0FK-EIU9BP-FlcZsGNPvASxr056xh7nfISccQz6AMuwt_ywrd3zl6KS94TTFqt0jpBXMxaotcK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-X8xnqfWVgskM_qz3Y2Aa8OBr8WvYO08UIh3iSXXufuZUOui9wB0Ug2bkiehnMcorCEaP8oAzolDJ0pF9iS_m2-HJaT3sSmeefKtsfIpqg77dXFkw60aajQLxV7lS3NXQkPJTPuiLACzW7cHMcxzdBXEuKzY1BUWB0vZm1JBtXNHjMNc2ugXEWCQZPxQVv4OltlGGscGNKpc29VuzntQ6AQOJuzXknxq9gZ3MwOEvcdbs-fwPJeLbn30sDWwhuzYyLiaB-GPjAez9ZsWeGTmwnaddNs7czckZyakBUdhl2_JwaHIxhT34D91VW7AeZZSteS8YJKgbr6LkxKOtGbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKGmlC5OyxO4AcjgRs_1YZ376tJwB8okr8aqyE5Qa33nOGBPTt0iyl5a8UjfDCDyoS4vJdDAq0WloGKjut3NSctXAncXOfsVpaDtgEXSy8gwgKqzXChYd6r5TkrrMlUAaNOCbtPHwZj29L67ors--6ACZh60kMETMMPpRJceT6Niu_CuVFWouWrzFQGQLqr66sXTk4Vwx9yD4gIHSNGEdEp7IhI668Vp9l3nPiQB2QiQqg74avcSeGMKPL96Gcwp800fRbgJ54sWsfGw4KHzaSIgku4rHgy6XEMzK0_pKqk23JAz1n7iM1r2uyW6VQm4gPb5DHn8vITxQX8Dm2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Gdv_on4BwfjkDyOCX6iu2J-1NbwwFOIf6SzEi4n6KotQlDG5mR4ZWxWjCkEkzx-F45Zac2hrbHJ3-3JgtG3dTxXv4DsoFv3gFoUMiorpjWV-rRj9qQ1ZpCfM2BNyW46ui1deOvTXKJipJmxBrzdCISN28oxoRuscLAh2_5B74qv9DbiYGlicztYKsCHmmRzqWkYPCtoXd1VECMFCuRmC5KU0UIaTK5l6lNr8kMDF0AwKvQyTHeZsF-6RozKuCFy5fD07-_q3j5WwXaebyfreHzlKZZQs-j2gRF6NAwVN34TJx548K0gVEwyD-15674MDoQXY--zFYpUY71hrOIoUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Gdv_on4BwfjkDyOCX6iu2J-1NbwwFOIf6SzEi4n6KotQlDG5mR4ZWxWjCkEkzx-F45Zac2hrbHJ3-3JgtG3dTxXv4DsoFv3gFoUMiorpjWV-rRj9qQ1ZpCfM2BNyW46ui1deOvTXKJipJmxBrzdCISN28oxoRuscLAh2_5B74qv9DbiYGlicztYKsCHmmRzqWkYPCtoXd1VECMFCuRmC5KU0UIaTK5l6lNr8kMDF0AwKvQyTHeZsF-6RozKuCFy5fD07-_q3j5WwXaebyfreHzlKZZQs-j2gRF6NAwVN34TJx548K0gVEwyD-15674MDoQXY--zFYpUY71hrOIoUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=sbDg3g9iSp3ThAc0L1TwODRbrG7ptTKARmA20_Fq7UW1oyVF540kf-p_mF4V0YUHghtEp_J6dAZBczN53XLoRXkiUpqPIOJRwQQCE-7nIWWq3VLuk43oIngkrvxVLB9AN8fAism-pHX_IdiwAUBcU_va0NRUmDFVNaFvjO0yFWLsy8RsBJx3Rv_qDacG3gcBludyaKqXyTu062BBrGdvKsvRvc0oSR09YSxs0bDiCoztUG4NsAqoNTrE4hPOc3QkTjPGfreLR442ZOiybg_n55EO9-9tIe9T6u6LKwPMP49xFsvPp55vm8y8jhmDqf64zjnk5Xckm77zoZgTqBjfZg2RYaIBsZU5tBJ7vKF76rG9f1ftMZwjcrQX84SRES2bXHnoNPoDICRwRkft74DBln39W-pRBXNOdUF-jjhdqS4VgNnfJbdB9FkEDow7CF_DyXTmxTgGy7n0W1Nun1Xr9xYQoopqZUAD6KGz5zW-NQUozipu7gPDNguCP7IJWUQhNmei4cPSdcOI17zggGqhMcnmnaTjjZQxeAUe6-PqDfo4WyeRGFLLG_wVU_rzbJi6gBH976SgAFML05SxlCNPDoosod1kB7FCq2SLaTCUHphSroZZe-Iho8D4PUMsMTbZ6aGCKU5zEKVIiwHH0DBm5Cgmi25L4VQeIykmggjW3GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=sbDg3g9iSp3ThAc0L1TwODRbrG7ptTKARmA20_Fq7UW1oyVF540kf-p_mF4V0YUHghtEp_J6dAZBczN53XLoRXkiUpqPIOJRwQQCE-7nIWWq3VLuk43oIngkrvxVLB9AN8fAism-pHX_IdiwAUBcU_va0NRUmDFVNaFvjO0yFWLsy8RsBJx3Rv_qDacG3gcBludyaKqXyTu062BBrGdvKsvRvc0oSR09YSxs0bDiCoztUG4NsAqoNTrE4hPOc3QkTjPGfreLR442ZOiybg_n55EO9-9tIe9T6u6LKwPMP49xFsvPp55vm8y8jhmDqf64zjnk5Xckm77zoZgTqBjfZg2RYaIBsZU5tBJ7vKF76rG9f1ftMZwjcrQX84SRES2bXHnoNPoDICRwRkft74DBln39W-pRBXNOdUF-jjhdqS4VgNnfJbdB9FkEDow7CF_DyXTmxTgGy7n0W1Nun1Xr9xYQoopqZUAD6KGz5zW-NQUozipu7gPDNguCP7IJWUQhNmei4cPSdcOI17zggGqhMcnmnaTjjZQxeAUe6-PqDfo4WyeRGFLLG_wVU_rzbJi6gBH976SgAFML05SxlCNPDoosod1kB7FCq2SLaTCUHphSroZZe-Iho8D4PUMsMTbZ6aGCKU5zEKVIiwHH0DBm5Cgmi25L4VQeIykmggjW3GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=HJ_46zTqfvEkIfUqZN3v0NZM0CTJQIVeyg3EZqbsXVvTW7t9NpXKEeBGAsVtF61Urmly9Z1dlyk4YKTKXHPXvXv9cHMdkrT1c1_WaJFEYnq6kosgajtjFBwsWHwnclqnl0iNTM8jnm5jTrRgHi7x6qjE5Pf1E2TW-VLTew9CG623v3nJ24M0kRi5rGbnZ7UNcOoXRRRoIn1efFAJEt8UFE_3-IWX4VhVGda-19Lg0wdoATzOJGqq0bV4-QUqwgHrvVIe6fgWdMvu04RDh2XP1dE2SOuf4qmbzMJ6evBVxPNKwH8yUOrC-pWBQ6JasoXCFKBsB0ceVEIzGJU9X6wpczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=HJ_46zTqfvEkIfUqZN3v0NZM0CTJQIVeyg3EZqbsXVvTW7t9NpXKEeBGAsVtF61Urmly9Z1dlyk4YKTKXHPXvXv9cHMdkrT1c1_WaJFEYnq6kosgajtjFBwsWHwnclqnl0iNTM8jnm5jTrRgHi7x6qjE5Pf1E2TW-VLTew9CG623v3nJ24M0kRi5rGbnZ7UNcOoXRRRoIn1efFAJEt8UFE_3-IWX4VhVGda-19Lg0wdoATzOJGqq0bV4-QUqwgHrvVIe6fgWdMvu04RDh2XP1dE2SOuf4qmbzMJ6evBVxPNKwH8yUOrC-pWBQ6JasoXCFKBsB0ceVEIzGJU9X6wpczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=qo2elD7N7zLmtOkv3iKsTBn4XW41-DRwB9zEg1G8Mcbn5Rdt45LLr9-DjVtgrYmQKBGcLHy9DmqIjI27ZdFBk1K0BTRoniI9ID_hgV5liEoUc_ED0jzsI-DxVaeVzUhe2f3-ulOSO-RlNhzC_tPsBSW3koRW29RUCAGh2HS4Uiyz3QLDfHYKbhkfCV2EA_KfWH6YsURNMDyASD7RE9tn0lEzFhPi8tyzfmGOmCGJIHgpVCM5uVxnDqRpPizVWiEU1kogDhCalztcLWWBaqox9hIzsszVv_u3TIeDS2TwGNeuA3efJslAEagPj404sFYynFPJqUAaZ_Ggdo9zqvJw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=qo2elD7N7zLmtOkv3iKsTBn4XW41-DRwB9zEg1G8Mcbn5Rdt45LLr9-DjVtgrYmQKBGcLHy9DmqIjI27ZdFBk1K0BTRoniI9ID_hgV5liEoUc_ED0jzsI-DxVaeVzUhe2f3-ulOSO-RlNhzC_tPsBSW3koRW29RUCAGh2HS4Uiyz3QLDfHYKbhkfCV2EA_KfWH6YsURNMDyASD7RE9tn0lEzFhPi8tyzfmGOmCGJIHgpVCM5uVxnDqRpPizVWiEU1kogDhCalztcLWWBaqox9hIzsszVv_u3TIeDS2TwGNeuA3efJslAEagPj404sFYynFPJqUAaZ_Ggdo9zqvJw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwpCGCftILaoW9HhPVLMb03nzyXi8MFvGGYsUeJdUES_hBSISuG275bzvdmcznfhROs7D37xXdVmk3W48wYrML-JJbHYW2OY8AHaTybJNdS2wwdozf5keeky7RbkQEMXu_WhIeFrVWckeQmaCv9_Mm-cSKyq1kmF6tiE8T4ozQCxewUuQR9UqYX36LuXDNFUnHlGjEUjj3_oaK7PX_Hc_k95hzUkYCJms0WU80K8Nt7ktoTK9YdOCs2nwV7u-yOo4dug5RJPsXz0CqRDSLgjecQ9ULDsc2QN_tIPYq9Me9Q9obUu-HKQsVDUr54aohAypKiTjXJOMulgCR5yJssQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=kleI-EhT_ZtPf4_8bc1YB6yVbyljt0EeAL56slbtoywekZAUvdMOWfAVCse9QpwrGtlnu-AFGEqPjuHClNm5WacNgCCFn9Dyy3G5-EeFUZJAXhbvin0pP9vL_JnVd4BnnbJUqM4hZq3wCNaby_Q9kh1kO6JomLkbsmYhUOn6Q4yAI98GygeL_JGiwJJXTgzUtPvoip9xgKoXM2wTVDYYMxWo-tyD5rGXiXAkjY1q9mV1dhqYpHL0Kgz2VZ8DDbrDG0JDf8rSlC-pg2XmowLsho8IT-HTL_rDxleO8rlnusipbkjvziOzbsWSF2v0mK3cPZHKGyAXiPedmbc4HXK5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=kleI-EhT_ZtPf4_8bc1YB6yVbyljt0EeAL56slbtoywekZAUvdMOWfAVCse9QpwrGtlnu-AFGEqPjuHClNm5WacNgCCFn9Dyy3G5-EeFUZJAXhbvin0pP9vL_JnVd4BnnbJUqM4hZq3wCNaby_Q9kh1kO6JomLkbsmYhUOn6Q4yAI98GygeL_JGiwJJXTgzUtPvoip9xgKoXM2wTVDYYMxWo-tyD5rGXiXAkjY1q9mV1dhqYpHL0Kgz2VZ8DDbrDG0JDf8rSlC-pg2XmowLsho8IT-HTL_rDxleO8rlnusipbkjvziOzbsWSF2v0mK3cPZHKGyAXiPedmbc4HXK5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=KUtW1fxmThblXCF15TqlFCfm5bGH51lrLRfaxaU3DiWKyu5Z8oaoNj4Q6LFkam3N-jf6zeYgTPRmTjTBDEK2OeKZgjcjFILw6u9JD9mfWTqp29Le7jA35HCOMi0yd9fn-kuvXQWXq1ZMynOEc640dfNbI-iBwYLMmi-nKi-GE8j-NSngDLdm4j40gxEN3ROEDu5wwU-ZID7BOWOUb_DbFr9LyshtXDEiKSKBIBZh4Fjh8nB0s9IxfM-SV4bwTt6RFdCM6_akqr9RKvM3SogvxAuzee8NVB7YBzOEJlS_SNUByNdmMRYmUHreOxog9cCg76jgtpHdf3Uqu4sZq318Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=KUtW1fxmThblXCF15TqlFCfm5bGH51lrLRfaxaU3DiWKyu5Z8oaoNj4Q6LFkam3N-jf6zeYgTPRmTjTBDEK2OeKZgjcjFILw6u9JD9mfWTqp29Le7jA35HCOMi0yd9fn-kuvXQWXq1ZMynOEc640dfNbI-iBwYLMmi-nKi-GE8j-NSngDLdm4j40gxEN3ROEDu5wwU-ZID7BOWOUb_DbFr9LyshtXDEiKSKBIBZh4Fjh8nB0s9IxfM-SV4bwTt6RFdCM6_akqr9RKvM3SogvxAuzee8NVB7YBzOEJlS_SNUByNdmMRYmUHreOxog9cCg76jgtpHdf3Uqu4sZq318Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=NZRldR6zmqdCi-TO6N35ydeUUmtjrqSe5nb8mdPFKEZwTGg4Zz4uy27L9d2jo58fwyWQcRo8zMuM7-GXDnz2wn52BvLj2CiYP1h6pvzJOdrYmEVFAh_IOzbaqvsGrQJd8NIO2b-i_q378JqWrGwp6KwwX5qmI-QhUbGVJZGDx_hBkzae-K6UX11HTITpehkUZRVNDi7Wbkgz8eDHXqaauEMT8kZiQG0DJU1wZobQqiW0NTF27O4yjW2Zg1_GyQyxyAiVOeBO07hiODPonA7Lt6iYd9ZwwECcrkr73EbTYGDkQWPEVa0FQrUfN2t55Zf8-a9Ltw2BvC4HlvckHVfruQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=NZRldR6zmqdCi-TO6N35ydeUUmtjrqSe5nb8mdPFKEZwTGg4Zz4uy27L9d2jo58fwyWQcRo8zMuM7-GXDnz2wn52BvLj2CiYP1h6pvzJOdrYmEVFAh_IOzbaqvsGrQJd8NIO2b-i_q378JqWrGwp6KwwX5qmI-QhUbGVJZGDx_hBkzae-K6UX11HTITpehkUZRVNDi7Wbkgz8eDHXqaauEMT8kZiQG0DJU1wZobQqiW0NTF27O4yjW2Zg1_GyQyxyAiVOeBO07hiODPonA7Lt6iYd9ZwwECcrkr73EbTYGDkQWPEVa0FQrUfN2t55Zf8-a9Ltw2BvC4HlvckHVfruQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=VADo2pxfC3lz3WyAOZTokqKVMsAPDoDz1YUbMMY14RpbYBhuoMsx5gq1eFyaSdmJxTVrz4XvXaLOfpFPduFXHHTDwL7AtwgOFFLkU04aliB2QyFAPJp_68ZIQl-MCLFGJcN_GQ7MuRpc03AXUOQXJ4id8RiZmLYiPlN0pfUvxj7TMegm-xyZxTSPq_3L9vzdra9HyHY4cHVvBP2ofqatOVYhWJrst_EN7waumuxT5pBoaVSNjlPF1q1vfg9z6dsWKdBpDW5DfVz1hG0Sx5xaAIgAc-mGt3fRJmncoaWa-lcL1q8W0dVODdEyJ8mfH65oKLw1-GSuz09n1wlWOvjY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=VADo2pxfC3lz3WyAOZTokqKVMsAPDoDz1YUbMMY14RpbYBhuoMsx5gq1eFyaSdmJxTVrz4XvXaLOfpFPduFXHHTDwL7AtwgOFFLkU04aliB2QyFAPJp_68ZIQl-MCLFGJcN_GQ7MuRpc03AXUOQXJ4id8RiZmLYiPlN0pfUvxj7TMegm-xyZxTSPq_3L9vzdra9HyHY4cHVvBP2ofqatOVYhWJrst_EN7waumuxT5pBoaVSNjlPF1q1vfg9z6dsWKdBpDW5DfVz1hG0Sx5xaAIgAc-mGt3fRJmncoaWa-lcL1q8W0dVODdEyJ8mfH65oKLw1-GSuz09n1wlWOvjY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=QnnttOXlDqDdxt1SHa47gUAd99h8oJPyHsYeOBn85udmiLJc_z8zme2rv7_Tfg_dCd0FN8ORthf_u4XlkIeQVuihYKiWIRZpda0rJerajZU12WwS5_Bv_7KRKP5Vm3FelyIeiEqI-CvVnyXFKP-e7ftqMc0oPUp86GunSs9tZGXfI_mDVsbp4S7ai5NzN2t5wBm6DTneTc64_uFQhR_V9xjI4DqRFCySBhrzj1iI_n-EFSd68aRI_OLf4lCLh4EkdONoi2_18Jfp1Js7voOyBQTymmoX2WnMfXeYPNXmBkn8DkV198eJRYU_mLW_EjLJiUVUjociwFMOwctRqcokBXuzpyhGANizCjYU4CNb4pMbBk15mHykjavO2QTH-pB13DwDZhKNC-ZjeNcf42Pdau2HON_7HRmYDPoirY9HLR37RVsI4lrezQBLD0uEnlZPl-MZ-rsqc83WJcARHXgQsgI86wralyGA9C5MiDkv8fPy27O_ISzlmz91AmmD1XtJS-_7hstpF5oFpz9WkJrJ1GeWrIxA8iy-PdWzBWNzKszl1F5F9UeUlS0a076Cb1kvNEGpS8J7tu2Sk1elK_yEjfgX50XHrCsJA5fc_lHGV8idVW5pjU9Iap3V6GpJ_c8bnBrfjuU_mWMpiyewOqSuJhRiYxRKrLIZaLj-8Leq6IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=QnnttOXlDqDdxt1SHa47gUAd99h8oJPyHsYeOBn85udmiLJc_z8zme2rv7_Tfg_dCd0FN8ORthf_u4XlkIeQVuihYKiWIRZpda0rJerajZU12WwS5_Bv_7KRKP5Vm3FelyIeiEqI-CvVnyXFKP-e7ftqMc0oPUp86GunSs9tZGXfI_mDVsbp4S7ai5NzN2t5wBm6DTneTc64_uFQhR_V9xjI4DqRFCySBhrzj1iI_n-EFSd68aRI_OLf4lCLh4EkdONoi2_18Jfp1Js7voOyBQTymmoX2WnMfXeYPNXmBkn8DkV198eJRYU_mLW_EjLJiUVUjociwFMOwctRqcokBXuzpyhGANizCjYU4CNb4pMbBk15mHykjavO2QTH-pB13DwDZhKNC-ZjeNcf42Pdau2HON_7HRmYDPoirY9HLR37RVsI4lrezQBLD0uEnlZPl-MZ-rsqc83WJcARHXgQsgI86wralyGA9C5MiDkv8fPy27O_ISzlmz91AmmD1XtJS-_7hstpF5oFpz9WkJrJ1GeWrIxA8iy-PdWzBWNzKszl1F5F9UeUlS0a076Cb1kvNEGpS8J7tu2Sk1elK_yEjfgX50XHrCsJA5fc_lHGV8idVW5pjU9Iap3V6GpJ_c8bnBrfjuU_mWMpiyewOqSuJhRiYxRKrLIZaLj-8Leq6IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=eX1zVJn-z5CvsdmemePey2_kt9HZpudi615t40OmF2nqF54HHbTbs6H30zQdjKx-OyajaIE1Cxm6VYjaf_VLNxc4Pub6-PON2dI3sdoHDjI5IFMAon3cwOJ1ENbIHYPsVZ_d6Ly3qXEYMdZDSxBS0KODgbkYNc5rZLyHPXeO6_h-BLAxC0KUgVd3KnzmSGP6KBeNxhRzQN7c8cDaPl-VNwHoxhe-PjJt3HhScO2EJlKWITtuPb3L6GuShIVZmeP6BNERoVN6NjZLLQ3AoXQdVSia62cy4vP9XVivW_oGyDDtgHV6UVG31vtH8lMCSJTQRRJuWNRH3KU8oq6oOhB67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=eX1zVJn-z5CvsdmemePey2_kt9HZpudi615t40OmF2nqF54HHbTbs6H30zQdjKx-OyajaIE1Cxm6VYjaf_VLNxc4Pub6-PON2dI3sdoHDjI5IFMAon3cwOJ1ENbIHYPsVZ_d6Ly3qXEYMdZDSxBS0KODgbkYNc5rZLyHPXeO6_h-BLAxC0KUgVd3KnzmSGP6KBeNxhRzQN7c8cDaPl-VNwHoxhe-PjJt3HhScO2EJlKWITtuPb3L6GuShIVZmeP6BNERoVN6NjZLLQ3AoXQdVSia62cy4vP9XVivW_oGyDDtgHV6UVG31vtH8lMCSJTQRRJuWNRH3KU8oq6oOhB67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaWlzxzNhHKy9YiosozcbQ-RbR9WKX67v02u64X546UjY8kvfHtDuJFnwBfT0F3QfdYLUnt5_xjpmqfqvODqdV-Cq9_BoP--lLwCn6xGJec92pOrVZ6MjMPulnbuXYLD1Z4gzsJyFT4dLzsROjTQpwRyZtynU_RFbNSVRzjJOMa8NcrfUHVjMGxh_wKBZEBTdQbVcattSTnI8eN3-m79qYxvexIF74NBID7YxJk7Ot0JKvgCqxL0Xs-akBd7T9WHvrDPgGYzaQquhV1S5uA2wfm7ECYnn1oQ21lVzEGGsnJ4LbGdHmPxcMeO1BckFNmXUdhTUx8JHmafEDuXhQFGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkN10hv8tVVVkeMt99QE37VxGDxzL0wXuN9o_-Je8l6wXp4pBcV-Oo_Lv2srfogyFy4U4uXiIkcsKZpIdlZfyZ3Hdnowdf9-u1PR9sHHlsotFSLhYCHcKpNjAr3gcdJs5s_6-rNvaVwmDnzm99rS3LQ_-PC12KjwzGmjZV4PejWz08CMbactyecaUAnae8WL14yYA_ghOUQ9QGs_gBA0GlTNwHnrfyq1e60A6O57tjYAbV5ePI-JofTK74S7646n8Wp_IdLJC36hxfIGLsb8a3lwrZ_VNfKQ_bV71og6cYvZp_LOCm7YdOMNV9Xe7pE61Pm37MN-gffht44UKm1aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=H_wOmFj--zCLztf2-hxdoom36d3MOrhFE-sHlo-MMP5sJqAFi_ZFw-68G4XXzyqqxi70Mj6q3tWCz_f74jbz8eQmqmsOO-cCTXlDt7pCmJlIjJIufdUDjv9MtRhcCCtzE9IpZBrh1fzKoFYb26LYVGTBBuFuKooWind72ZCXayIi8HiKUrem1xmEHsKa9LrLGchliv8hFmd46wi0OzZ5l5AeT1kL2QM2io1dfItJcoGGH44ND5hgARdOy9M9jD8OrJ64RALop-B1oyyLYT6nfpuNl5TFhPBAEV4ZVZCIZJhbc2WxOWLki3_yKA_QY5iNUzls694QeIXmkYz3VscQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=H_wOmFj--zCLztf2-hxdoom36d3MOrhFE-sHlo-MMP5sJqAFi_ZFw-68G4XXzyqqxi70Mj6q3tWCz_f74jbz8eQmqmsOO-cCTXlDt7pCmJlIjJIufdUDjv9MtRhcCCtzE9IpZBrh1fzKoFYb26LYVGTBBuFuKooWind72ZCXayIi8HiKUrem1xmEHsKa9LrLGchliv8hFmd46wi0OzZ5l5AeT1kL2QM2io1dfItJcoGGH44ND5hgARdOy9M9jD8OrJ64RALop-B1oyyLYT6nfpuNl5TFhPBAEV4ZVZCIZJhbc2WxOWLki3_yKA_QY5iNUzls694QeIXmkYz3VscQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ZUVNYzJWqMsuXWDoU-MNWh45wKh6ur2NNwcnWU0eNR8B-uxbHzlZB8wMRsUuhrdZcLpGoCNiwmyHOZyiebQVBOjdXm3nRJ1B-TSJWmSW998VAIIcis5YWekdywGGntclkyJr1W5VCxOPZ2IUbmOHpdN51RHTG2EgDC1Y7NK-r2yMsZ01PiBQ5p2sMAG-koASLWuLIS1GfohGq8gV_v52lsaoQpZraxCQXn-rNbXPbAh9KJxfUIkJBSym3EO_MpSeQMWy-PWPYMifmTmawUD_MWqBVuIr_qcQ8MV4NakQr-Nj1mOJwUQkjJvR3_PWik0PMuP7mBHD-_obiwKNhF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Pf7RqTDgBou2TG2bE0ZNGuWuMABZrBHyELw2RVTeo5e2sDdZTMMx4OYggTHMGzgA3dK4f9UzuGNN3FmQsy_vcvqOYrWFz5iUjr2R0rQwnFwbZ4gkyD_1wpo3XQPenO1fTs1bvAdeC0J9ildW1W6Cd7nIwjdrdPTDBHoBpp8q8OSze9zfuUUtfkn5Y4EIpdwN6CZX4aMqfHScLnVcwxiK1iREoGKAJJiSmE4zumEzUv4a4nw359YzO4KByGAy33cfw2PAP9spZijrlW3Mv6P-NGsMXmxuvYg7h5-GGhWyLWUL5m2ej0GobiiQIfeif0u4PmO-H3R9Er7y6VQwOCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b085DgYzBfKEcvbCcmV11OMja2lM3DtAnXwFEAjPpItWU-wno-taOqP8EV0zp9EYoweyLxRsZ8vYIfLpeFnxs6hjv-U7BAecRxdp_whw7rqvqm3taCh4s4N85jt7kngVtLNFCwWQ6DuBzGJk-x1lz-h4xAqhCzdKPwEhAOVyCQ_DjeMQk6CPoG2YcxKu8aoks_WeF60xJmtfz3JARaHLoan5uTrGObK1QSJkm4A85OVw1MyqywnTuSoy0QI7pEeBXnCRe0kRF-qaNLQTdjPaN9TqbvQgVVGM0Yh6XeGhQJH0m1LNRkmaHJ_2WiJvZThBQr39fyeza6ut-mRJvdVO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgGC12WsOqN_KqaDuJg2FKig2-l_bul50jmymbX_RFIRkY2mZu7utdMEX3-GYplm3Ax9ZrwkonrQGJWbWCuQ7BG0R20SHBhfjmz64whkIqMFG97RedVvpWVtvAJRV4-LqIvZty7kxcRgLYsNtfsm5EssJUv9VeAiLCwdsLqoFNkucQZoM-NSMEDWVRhrs17DZDBN1Vm5kQmsm2GDi-WCEX7bhaB4e6erhryLBgynEUuE-3EZGRnbVRzioLOR0U4yxAAY6M1pW_MhX6h_T_7idgz7mVHS3_HNa-M8c_G4YuRfGQWi6upPvxdSsH4dthoBx3lqXoAkjgBidjIihWBtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edoiSOfj65Sdi0ErBDmUIkqoDDuqncplcztz5FyE7iol-5DzNJJNo-VhYNB1CwSC2f-VpQACyXZHt9VG8oqsz0vg7QIfblny2s1jKW0BjN_PrU2J3YgcSJrW3FoMXA3RfuH4jiFiNdhhF89Td3VLl_tWpAzoZry3xiIGvEedccVQhPfBWhHnPUZ7SjMxoJZ60uYcvV5ONkVgbCTPOo-3jovZ07IBqGwmdzq79XLj2NOyJyYBmcXTQzLdNIG7KA3B-20-KLYwiShWGZWarrrqCqrwALfaWTNnR4wMDpYmTXskiiNQSIjswMoZMdLwprAyoCmc7z_pQ6RAzotG7hsbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=TZ6NKpqoSqczxgzGtM8SBaS61y72O1gPfx5kKspNeFQjnt-c806tLOCmyEq6aR3gc2NFoCI38kqd4ZFH9LlkSwyjgxq6GBO5yXZBGk8R_e4DymHHcn5ulb9MromyR20gIiyoi3SpIlwXMA4W8O8WWiFQHUShrvYvWAEzW2r6baILLjkppmO-9ROuzGfDk6fBner-MkqyuSJzh_BMwYBon9Bpq9YG0C5usduaGLSVRqCYRy2ODqQrFkLMfeG0ibWXlH0qds9fsCmRVWzh6PvmBqBOYNeT3e9fJ_ou_taTFHuvGvQTr1DWL7oLSVsxfOLWefZTco7C6aztEZ_ToSlWdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=TZ6NKpqoSqczxgzGtM8SBaS61y72O1gPfx5kKspNeFQjnt-c806tLOCmyEq6aR3gc2NFoCI38kqd4ZFH9LlkSwyjgxq6GBO5yXZBGk8R_e4DymHHcn5ulb9MromyR20gIiyoi3SpIlwXMA4W8O8WWiFQHUShrvYvWAEzW2r6baILLjkppmO-9ROuzGfDk6fBner-MkqyuSJzh_BMwYBon9Bpq9YG0C5usduaGLSVRqCYRy2ODqQrFkLMfeG0ibWXlH0qds9fsCmRVWzh6PvmBqBOYNeT3e9fJ_ou_taTFHuvGvQTr1DWL7oLSVsxfOLWefZTco7C6aztEZ_ToSlWdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTI7n7QVTuliZsxNDdA0i6U7eOQ2TrgV24YMidU02r1JAFVrToXyV739tmkBjiOPJAzAjaenh18wcH6xeDs3m58tBRCFQXe83Zl6rxPrMi5CKtmJ0Q8CebDsdr_Es4u9rdkG1qpSH_ywmkM_KCYN10RCnd1VYhYVb5UrO6d8vygxOEOg6NElrLPxGx5ocJhDgjr9C30hJGX2QOGDn33x3MLlIIDgvukcIsbkckVZTuUTHreFF4i_qNHjvS-5gRSoQByO_ZlxscFf_iRAyWqq3O1fclYSZPQq0Gn595rjYwvy5a7RAldQqYXppWlYeSzWJo5YJg3CF6jsoZakglS_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btylI5vipO_5UklPTgZA9EqlFSbMuW5QyzDurzwJI9WeFNA4ZPsn-nlmGVFPtH6HXVr-2fMwhmRdA--hlEHYcvv40f-Sq9QqQ_13d81OBuu14d6XSJzh696q2YeM19j1sTAyC45BV8NXjT3INvHRh8E3fbQj7D12k72i5X5SNzH5ifD4zxl0hkLNQ3zaem7-KkvmLXGfTHir54qAHRDDvmgCsOaOwujCUrofCZlo2bqHwIYE3p5nHLnNHwuKRy84zIFtlg1rbP_o8JdXVK0Mg06acbA_hWDFxZP0xdHqlvMUyujBFRsKU1H5KPKc3ZjwG5Pi_Xd_aT439x8DsTEvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLyz1pSYtCvwBMwb5yb_bX7Q23gceeqGDokDrUCBtgzI2usssBYT-X7cCFqC1Ldp5D67KxhjCPsRCt5cuEOFpF-wQQn59m-_5Pd7SrFoG1NHXOcavCjbKSjSfCj_sRTgOoEeeinbP-1AAk1N3xSZP94GtHEX8lWJcVOC2SIrldIS-JtsNVqyhkAN3ddjVK2P9IeDdEUk7cnqAuWUTrFnLb3zu7x5OkkyRbqQS4x_yn5XsTAOmuCb3XuJuoTLm6pMWkpcJBjLuPa2QTwpmAcKXxkHaQPf_nU3dlDONoYY-YcsdtX0dNTIqAxIAxd_l_adYMq4LfmSVzPXUN1ExFcXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTuoOvoRylhRapAqXBmx77PdHs-eXYvOuUNDZlzVtuR8pL-KvZ_CnnBash2HR62icLPFL9cgM1AxNSx53004M35F-E-MID3eRQVFwvdTWZatG41RZVk6M_boxhuZ1nNjgTSs0s2ODtW4D2XS9E4wTPfcTIFEa9wgvExI78SuuWVF7Dk5xi97rChVqwkOJzR541XmVUgV2aT-9gn4wTSWB6NsypfPY1B8IItARdtlSGrcp13wIHcUmrFB3LV_4yIOAH8Klp4X6hdH8Q9iT43ZcxrvZ1Xzs5XYfcXZ_YXifBhPcDIYz9bdRJZOCK3qcXVjxUhKRcO4Vdy9GKt-EWMOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMHDI35b7aVIq7AxfUbrM4lsrXxP-ZBoYGQvOGYLpYeXVqHYFOcCBCRRW7VDc4MtWt-bxe-tjQg-IerhlV9fGHHhfOMYp_ybqAaOHSZ7wow4TL76zVCo6j1e4802HVL7W3IgPN-bnIrjGd1h9IbtNSBbUcZNq6CjT-ycOlHNpEicWWqr0snSF_phkP45FFxAFdm10FFjcppfW6DQXKS_b9z36owRfxPDFLNK04h1dQhu-pA1B71BOjfXQ1TuiFhPx9ihsxCfA4OKl0oXZiFJCb8xMypO1INe9O7yBFkIvCtsQT4nA_mSxB2eC3ngekkCFBhhlhVllVDnNwvKizyENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH2-W7fRvIzK9Wu79wytTgnU2xwRwnE74KMpUGhOJyBRKEqBiKsl1uuLmr4P7_u0k_UZ-5ilmB3iug8SHuhyBN890SBWd-0yHkhGf9EsXcJvpns7ZWCShJc3MIiZ3C2VTGsp2QTCFabRY9HHLtykOKZO3rI68Yhvd_N1Znz2Bjy5dmrCqYkoG-4HagL6vRK43nWaeewjKGaHgYpLJBbviY80jBNvsbWvslswVSA1vmILzWJGBxg0JYz5T7EI6Uml3nHoSyDT0E69aQvXpt2-_g2j57pDQy4SEjciSVjsy29Ft2T_QM6EDtSCDfGcOlj0-pHgBOzXCz46bU4Zvm6V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYeHGqY-er3A2-tDgvc6-IvtJFsHjh0P0Jnvdz3QUHxOZkN9U9YffI6-gpHtJNu76SgCg9jnGUhybxwkb1ndYSG2I6ZVeU_yyz_6dKLBvjOyw_RMhaZLMXv3-1iX-oMuqxTw5C5kbpGOmkjbfRwV7TzkwCiNOodGDxRu0MUIMyNx5dC1NpoJ-L0glUl9c38H5oFI-eSo_nMwc4yFMSfCVYSHXcDkCtnWgxzntUrCiDb15H98-J3iCSTxu4Ba7v_fg8bT77Aax_iiDviMoerKzkEto1LiFbgj8b6RYyn3dQw8PHxb7O8LIRedAVx6irwCEagLyEwcLwyn6Lyo491UUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEt-_If3CugbLPegX1EwiBiZrexC_mQiPwZ_QDDe0Hrl76lP-1OL5gs7YNTfA94v4cBmVJvuk05ezAlz_CrqV-tp5L35_R3WxR2yZy46kXgN2rcXPq54T4uJrrbZ3Bc7-oi4tjMX-mnqpfLZmA9xCPuUsG0YcWSYnfZMba6P0zmxQQXESUZqeolGQddxBf7aSq_x_0wxpUE-WzwM7lZ_tmr1Cc5AEgEcgbTHAO5qOFv1IWWHDAqS2gdGtLZPSzH78hmp9jdwnSJSCP9ON-LbdrohcljZt-qeldnS3Th0PbUlF2FNcxWj_OeqdHF7OO0dty1pDPKZXp4CHXgQMDq56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keq-IfE6rOoQv15cYgdnlnG49jtJuUnehqX04iZPbQ_nDZn_YW3UYDbJ-9vkF-jI5HQo_8NZ2bNHk11z4LJUKFBxpjKuaoahxgVxGruSfOxuijj236sPfRfG0_3qq5l0h2IT4RGUJ6hFYntxARPajXs-aLgIgfVKKW80idGOl6opascnzD571mOQfCBAxcF3zTWcEJZcYT5B5_iO2r2cxpSZhkA0KaI9CZ95HR6wMggUDraEXlluldLwhLyJfVVcDlF0NRQ-pfZRxWtUj2_uZlQJlIkgSThbL5ECEHp2ucTEJOlX3Ocvvj8nyNNUWT4txbI8HHOPwBaTphQRyMCowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6vYeFSWCQa5RbGDHYijPqGF41PjMucqvEnGff4vxf45yHYMj-Teg49xNakF0it3yS0vCLI6l1Ddcpyd9V76nFky-grLmtLVDNV6EXYJsJ0znFG7RnU7khoe0tHAgVXIrzr27KRW9kJSjqvV6XI1VJ7iCeRV0vtQNqLPFuS4rNhyoLm3-i2Sq2eO0HguyQc0Uix2KTrpWxCFXD0VSXnqQ178cqgHgcku7FPyP7EyiA3S6KGvkJsJLfqtID87dzDLPhxT6xPcI_OiRyhJIP8k8LbbHRHAlJR9aUffQl9BIvJZUcvdsCQrCRmcpU2zOn-nsr1RHWWWld-KWNHuEUZ2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RY3p5PAJEz4Q04UrJpUe0unMkhMmj-o1WBwL_eE5no47Thl4XgfrKguRW7_PFtWIHdJ9A1wuD6zV95Hp9uGFTfP8oU0UZ3sCn3X2Sv8WxjK8ZJprRnp1syl3wX5HEhLXfIOfgs8b_H3MkecvplshCk43jUbGT2b2YSmxJpLVSvKWmssGWSW1I8GyMHDoZrlR-_nqLxh7V82wbpDleYorEYwR1mLB4vteCIKQxkvJEGjai6cS0Vypn05dVGGNWA8ip9_Y5K-idP8iY2pZep9lo6_eRhJs488Q5ZyleBfD4UGowP27VEgOzwvKKaGNJ-X_OI97kZO1ChNtLP3iqWM2tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oynLdNazH6cxlZqFFxQxJcYIR5ATxNIF6SRiiouTuNlXP0rerHQuhnApHZy6VsJ-HyioVn5Pyz4UtCiFAXCMhVRMgHfoh8C6QvTFK6juQlBzzqRs483Beqvhseg6UUL7v_qhbeZiszH5NYBlqF1dzUZuWu4SUVL69jlU0RfTH2_BdHBfTS39IJkgy3-9bwOk80A4R6y4HPwGG9H1Y3H5HJllZbr0Rdt5juYblXiIdvdI6LaXXOCjARkJqrRAVCotQx-tdFfVXUvhK8dk-mUcXH9DfeuWrtcGM8DhDFrgTHE-xd_e8Z4d0aHG078g5UbAhUYzST5XqnMbQN34AUClwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdYcEI_QKzAQVC9DPVCbmC-u1x8tU47K4-pJB0DRjT-7cto_W6Jala7a3HzskxTE_EdtTKrMXMgiDy0FUoVUfvxAV3ORryfKpVtY0rcwPsTVhsdtPtZJEUOFESQmA1Ff7fSQPGXiuip1NqXddOWdSwMfntMCBVCBA0lu6JtqLxQAKm-ASW3kqjo0wrbcbpObxnBGUuSWXaP7QKMlisL7wkAJo_7GfvKG-ToOj7whIk2oq_zADgmh_JD-TN6lBX_p9cb8CKUR4KCfvzi7OShSUu8NiL4g-Imks4cH72dwSQ3QbEUb8wEACGjRUN_lJkaJV_7Dt9y8gjb3no1tNmhP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlL7cvepRX52HzuMcomGYzM3xeegmyXSJptWDMIICgpMWEuh1rJq7I29sTzEyqIkBhcH2bCmQ54gktQ1by86yLJHHVfftGcU4ZY5Us7byS7ktvHrIo3xpEqgZtEMmp_4i4-Oc-cO88OLccKT8KukVLx07RozAMMIwatNLSMDcFkiLVPb1f9Xi4RgDKyWw8Qy-fJldNR9P6RcsYo8A42k_ayZ2Oi5sEJ9uE99gQjlfnINn4wJr9BAhh7-uqeQIMRYKT5lyUUEthhE5WFEd2t9zyFJBxYAoKzRkYv4mkL7TUfpenJGScJp2yP8UKx9Zcvsn8-PWoyaq61mmx2sx_LP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUa6SJUaV2fUu_9pvVV2FzX3Rgt2WyI-crYk7h2PNF1BnGHxfJgC906p49TlmPRgt2pdwroos3OrtOPBS8WYw3GMvYmvxJq7pBzxrXujv3Z_2Z4VYr9TbRwP7V5cZe194_5wfgoEkUR3418FqDdYoGq4Y9SY5q9uF8MH84v7ThGflArVfSVZ_XMvT8P4flqnI0mvwzMYbWPOh3_0DTtL82Z7bsiv_d9p5oM2X64qTcIZuV4NWW_wyZEkZZuTxvgkoY7Dv68oyj1b0WJobdlycwR2vUcjMeAzq-jhovxuvxOVqNfv43j9prBcFo0yJ58Knx5-lMeyu2qGSBf2-1rTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEz5JGUkoVb8tY5cPnneA0sAVzW7UVvbjAYzxqz0xx0x6Gp349VS_KNrLC6TTPwKKzxm4_XZbndio-cfrc5vhUccVwqtcBLq2dLZRNGOPuhP1q-ojMstlrgnaYZgY5gBBIYKtNxMMXkV3_mdgLRXxr7lrglSoseNHOlre8kJV1LLO8uToP4JoC2V_TSL6qqthMe4o2t15wdnV6kQXteNAYAzSYtlbBqxgIjkgyIpaVHXDVFL50UoVoLqptMqHsum-TBz0fqqDABmCHg9oI3B7z4_KvTasI7qW6DTfzAgw56iWu_iMMsuOOYqtB9JlF1LDb17XXWQrRsB38rbeK0F5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=DJZE0gfvNIu2_ymuhWIm-HPzNkQ23-SUIHKt1H5c1L2AInfEgq0M0_o9ot3j5g0tNh358-OFaAlc7vyqNQ7PuYWOFIPXM7XvmugqZyoEIZkHwj1Fcl4iEgmexqWbEpXSI98BQw6CgAuPJYntQVBlXShy7XaNXJDdj3XKvFlbZsRko-Ib1cN03KKfQrui9hBlp10XsfEnXx9MEAiQQLOyHYUI6X-cVy3XHSoexGw5GGGgEF-65x0s54GEcnWSUOKfcnn-HkMy1sQnx_qlqs_PkAPhF_GtJjG5VCagd1VbtNpQxJvGW1QxJee7qBAveKx8a7B_J3_zBiqS2a6EJix9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=DJZE0gfvNIu2_ymuhWIm-HPzNkQ23-SUIHKt1H5c1L2AInfEgq0M0_o9ot3j5g0tNh358-OFaAlc7vyqNQ7PuYWOFIPXM7XvmugqZyoEIZkHwj1Fcl4iEgmexqWbEpXSI98BQw6CgAuPJYntQVBlXShy7XaNXJDdj3XKvFlbZsRko-Ib1cN03KKfQrui9hBlp10XsfEnXx9MEAiQQLOyHYUI6X-cVy3XHSoexGw5GGGgEF-65x0s54GEcnWSUOKfcnn-HkMy1sQnx_qlqs_PkAPhF_GtJjG5VCagd1VbtNpQxJvGW1QxJee7qBAveKx8a7B_J3_zBiqS2a6EJix9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-nRN8ipkIAK-1BSDDEdwFGSXZQH4PdELzG2K70AaWHtsxQF0hMyTQiY2hINt9kgP0y2krubLoQRWVFUnVq3k-BNk77W11dFqoRFERcIQqhEzIbwvdRr1WPCpTMMUW0Po3AGJq4mJEtEx6TOLxlPCbzhCnXdAavuFPlIve_5_uGht0l0qnTLhkt7_2OXVVyPGgnAsxcTXN2ILWvwm9wPitHgn_z1cJ6Nv67OGS6GvRt54YKs-285rDvRk3kQcrVUaTsSFEpgFnYy3l6-XY3hrepcwUoc4VRcJIvVSyDJL14eJPDN8xjiH8W9--jPW4hCKFnYi92eFBEpT2iBv6MfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKF1dmHPk-ptMKtN1kbwa0lNA4CwBqpAnvjvlmTWP_Z0_Kslq6cW5i3WbCoC03lKHPL8PAExmfrIft0fPGFCn2C6mPbf9OwurMm3yEdekg841Y3ZesWhnba4SOtlBpcQLoYnEWXpQf7dR5SjzY8NALNOUFNCJXzaafiyxtKcXcyNdpajeu9_49LK8Bq6TObSSYf-e-b_f52rA5G45lomQpUnaAsp3JpKnx4gidQOJtUdZd3amFqw2dP0iF540n99Tx9kCju4SwG2w0n9fKCH_-yyqXkz7lT-nXjrBKma_lR7GhCblyVIpNlzNxuuTZAFbvzepsUWt07xj3XflTC17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shxkYSFvC50LPHehPGJb4TggOlLcuqpyLerzzEE17CrCv8vFe69SUJicWuSdAvZ3WXf7VawnsZ97HS_K3_xX0XbdzAKUL-stTQAg9QNK66t-J4734BdG3v4aAGr_sb1mP7-gNcSOCEuz0YbBoDMTGIYDlAlP7ofbmtZ5q7F2qdHoDUVuaarO_WYJsK7I8MzKdWb6eZkOvx977XHDHSxGofEFKXHleesmGX3m6Cr_xIzOJPBqeXp0snmSPpnSCyJvgiieGt12zLOhmlaEvmjwJ8aqbIKWlUSnHBkkDQGVjKmAJ9H4Pd5y--c3z0yHos5ldPBZ2SmroiL-IbS3oOI9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haFschbHtmyYGXnAwm0Ksi3aG8GslcoO0ESb-Iyg7TiEmYCSxSrcMccpUvUbLSF1_r71sP9nTTJEhNU5VjhZpCKp0HvUTAg8A2xvOQR4x74BxwVsokSteWGB1losyRylqIB5hjA3aQmqylTaPJhLsX39zVN8H_d5C2Jrh7KsD-x2w5NKn7ql35O3u6oJFoSHgKD9ZL6ltXOSOriZfwWCjlXZoyDxeF5BN2GoafJUHuhvnfVMD-PGMGf5ScPkK29fCif4YEZ8rYtp6uLUWFDTdvghy_XugvaCb_U2c4P8nGsDJc-qKrrSy_-FjZJEpwy4DisjnNt6qaiUIRPuC8t5kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b07GfZyM39rHUvGHFFFEZi-q74QGBe3Rd5bSDiu3arwZdK1zP4IQFte8nV0bnVw0gd_--YVssWRyCpvZQHZU14XPBXx69204kJDIAQLlN5DuI9iTuVpfvle2U192RvFBOw2H0LGWQt7LEBgwwmww2LyZGYkgsMf5pQON6aHLHkj8n-LSU0KF6cjgZz-ETdRszeIQ5rUp_12BHJ7xffBGERmheDjQP-PX6my6pyQFSx9dLRrLqzC-Mrgebja1vJ1xMgUy_AO20fVGMau3AP0pbwAF-duJjNRVsLOJVAwJRUlNZwSAa3P5iEEryDNDGWIuvA5LdmsKqa8ROWtfmCx2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G75IjWnZ7_a7i7sMOawFGdFArIA0w9kSnzfArLZh95sr88a35WJW8B_7Ba1PL8ZzaGWr6vTCoRO9nK-nVcNuUCBjWYhMjMQRTXclkj0wSDZbzWU4uvN2RAxHWBX8NYaJD_iMTJtmGQiEXWlHtN6etzx1L2zvm8PZZb_A2J5Bgq_e98SVZ67GD_zdbHNCClELRE02a40JWEGCvOeSmYyi20msMin307NyZTNAT8Qer8CM7gl3T89IhQ68hXBUWYk2mpHprVU_K_4GcRi8NvW5OlnBbyZDbuLAzbqH2gxvevXe-_DIftpC-8urXFVvQ6gsnfOW8spPi0r52hgQ5OzPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD5nF7QtebAYvaj3xxcZKlNFRieeofwGg5vaLC1t9-LUYbRNbaYIy7N6LtcwDzvjiubptLYhBy2jKTkjsV-ekh4kz6WEBWI_IVCccpVM6GK93iCCwm1DtkchNikm8Y4JVaVfM-c6RhJRODv-K-qpk6G3IjPKiP9ea51hfF_RGotDQyY-zFvEEPZ98Lm6Yr4BAecNDbia6Q4GLXGnMnl6lm6UdsiaR-nap-47bP_Owgms_bmkZ9HgdBNNSram7V5TBEbRI7cMiXs7UnfJgqypV5drkkNaBqmcUPrArDgsPGOBR5Uny3tBFw3edlZOlqYQNrkrdQkVtrKbAGnt3tleYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBwKL9qndxcIkIjBy01D2dDBiUd__oz29k9IXldfGLk1_SwneH15v7C0mDSRB-hncpvS5rLHEdAROdXPSFCBY5GH2VPh7F5T2agdm4sE8iS1b0DeAFALuTUPG70hZs3hUMVEFhE-yqvvBvFUJrzflwCMO4Vvi8XLxoGFF6qRPFRPuLkWqvdQmpf9kTQDL6JPmPh4RxjCCUGfcx5GgBe-ZoHKZUPkHINyGwue2G0U2DBZCWWnm-fPssHIWh6X2WtxkkcrOKH4SKBPn0NvI-4d06UZRrbw1392JDam1KghEmpRAEnLxXBrJinHGBolPK1FNQWLHtaNxGiRxlB0o4klFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7nOMtcc3NMojlHdxRhPrfr1Sx4_0w6gL9bNrugaz0ZpDCxF-sZKQCJKCoMJlxjCG8j56fkTwNCWDd6eJrbaMUkqIzCib0lzsiHlSXhNO2K24hvqME4M1XtiaCzx231fKaTL-Iwl-99EOPqsHuGCFAo4vgVq8snib4PK4WXyK_A2FBrIFCwpb0Bp70rJidOXrZlmsrvBZ-xuVa9jB2oREwpDweyvekXeOg1KJgRv3hlEcI0cwHfstp0iIydF2NtL8P13eYsYeSn2rE-mrxGHCHXTokztg1KLImqruEQmBxX5pqNoyBDuVNfYhnqxJJSse3V9T3yLsuH1OCeAGHgCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=jGty2DMbi3xJnMmryULaOWHVJWL3qtaII9UT2to6xaoLHi1MkqeYrntLAtqdZ8eBKYPfJUHltf1x57rk3cSrxL160HHv1UWC8Ou9vd9SmT07Kw6uFjyOZoUsEn7XsHywLzZcNYkgMILW8-F4daOnu4Snd0wyMAoVCTQQ4jkZnzcr6w5iEiwNAP77NzNta3_AyLXxvk0NzOOYAAc0klgu975IIam6tyeJxeKJ5tQIixKRmmenL5XTI18DiFfoEsnwvg8dnYb4waewfUEO6rgyVsaQB0e2rmWL2-DLVodES_cLdvlNFAEYaaGNYmqBK7lYB6STpiT8twGpvLI8darWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=jGty2DMbi3xJnMmryULaOWHVJWL3qtaII9UT2to6xaoLHi1MkqeYrntLAtqdZ8eBKYPfJUHltf1x57rk3cSrxL160HHv1UWC8Ou9vd9SmT07Kw6uFjyOZoUsEn7XsHywLzZcNYkgMILW8-F4daOnu4Snd0wyMAoVCTQQ4jkZnzcr6w5iEiwNAP77NzNta3_AyLXxvk0NzOOYAAc0klgu975IIam6tyeJxeKJ5tQIixKRmmenL5XTI18DiFfoEsnwvg8dnYb4waewfUEO6rgyVsaQB0e2rmWL2-DLVodES_cLdvlNFAEYaaGNYmqBK7lYB6STpiT8twGpvLI8darWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZRnqkjSwC5E4A7vN488t--YhJTRyXaGeU73r8tiMLteuRex7tHfZEh692Pd6ikoCsTkvxyCy7kN15ybDAg45cviyg6c6k6cfzCYKI6FfaRaxSkkYUVlxTW0UDxkqpzYBwZ5VJAQ7f8onWe8grYLjFKCtPimN25kTmqKXPLjS5Pjq6oyfB7psWTZGG65A9oCXCxxMv7u6AGcWfEgByiFgZYylus6OVdQeCVtfyyRDKFFyrkMLBnxnhLXNX3M1gMAr6sZv60m5aDlK2HtRurxIauKCSqmwf2Bl5nQ0NlvRzbdVQGmgypT0TzDOtGHpAaXo-lc-CW2zooj_qlIwqRaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtjXDPwsldu2JcpRpl7Xdh4tktMlBoWP1L1I0h8-Hnwbmyi1dhkM_S2V7vFdeSRyEJV-CyhFV5tl3NyxRABPiPDb749KaAJsThxOkg5PepLBhMSnhl4QOjvZahR7r6-iKAXhRXLwLXIwfeZjgnbEHA1f51crrGOPi6zv8VtlXnj2yvT2tFiijnp99iHZYrMj7gBDVUcCZggMq35qbfFuBiHIOErRTSl-miIXMlXxeR4m2pXpl9NgCC1dDvJkJD34q9zOX2hr_boXqW7SEAUvMfgQIPM45l1JvutUs0efrmXM4xrxSwUWWfhLHA_L9QYxdzLvBf9jazQBT85e5wKw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlbqHj1PUVvjvsSa167WvhIhaYasZCMK6j4IixxdLboe60EUuBeaqOuO4M2z15uXbuWEKs6oEjD2RssfHPxvhiuLHVbVn7zCpaQcRYQODYzGd2RMwG-HxM0f7PntUkO1YtMGWEJUqwobs_uyGGiF7W-fE-BHllC7soUFVofRnJ_lhBuSHExpYfMlmI_E09WlQ28cMf4FnOSC3CsOJUhP30v_JfztchgtRHfHWrATPTEpRHDIxGyNlKm46m9ZYBanFqoLgjOnm46NtsnFo0agKcALlcCsPGfiMNn6JJi_J58SIdmGuJ3IYEerleJ80H_7OVhuIeAMY0ejnJCxhWXHwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=u8A6fIwLAZewQZAt74B-9VjmqDvFUTC_rF6ywTMI535iWJA9CvnjKSXWh7EY9PszzP5Y5PjyGY21SJ24XU_T25WKc8cRjfnMQdh7mDpoXJRjuIZsqeJivdFCs2Tbf1iURpAz4AvjFUChHe3BVAXoSlAvxFm7xSrKq3HK9fnvyWa_hsTklaX4DbbOcnwPPd4iKJVNLtFbSBP_NdHi7AWY22U2Nyeg7NO-4_58Uq9q4SYSz6g2HivEPR_BS9demT7C1bDNiB8OXPEz5FfD6zbyklPzbhmXmI8gPSwBEU5xXNJNsQxSOOV8O-dNoxrz1WMusVxu_SXbMImIOu4RsS4oLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=u8A6fIwLAZewQZAt74B-9VjmqDvFUTC_rF6ywTMI535iWJA9CvnjKSXWh7EY9PszzP5Y5PjyGY21SJ24XU_T25WKc8cRjfnMQdh7mDpoXJRjuIZsqeJivdFCs2Tbf1iURpAz4AvjFUChHe3BVAXoSlAvxFm7xSrKq3HK9fnvyWa_hsTklaX4DbbOcnwPPd4iKJVNLtFbSBP_NdHi7AWY22U2Nyeg7NO-4_58Uq9q4SYSz6g2HivEPR_BS9demT7C1bDNiB8OXPEz5FfD6zbyklPzbhmXmI8gPSwBEU5xXNJNsQxSOOV8O-dNoxrz1WMusVxu_SXbMImIOu4RsS4oLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc8tdwk3nHAhR0WfM7Vd3QcmvdNzxypkbo5dnVj3nXo5Aca_yILLC8ghLSPFkmsXNzaGlc0dWZxWZeI0iGHNAmviFWFFEt0LwhkcRjrddYwKjqbJfQrfxGintk0dnKow324fGPL5CBJyRBptCbWAz4ShCVw7HoUfK18ypS93nVTJHTGc0AS0UWPnlc6Pu7rsNhmsBaNnkPvsqj5kg5WQ-GXJSYEzBpoe6bq8ycf4CRsSCVih9cx32rfBBfaPC64mpPM0IQ9PzBRg83u2oet1zXb5pqUHsd_M-o1Ub0jK-1sStetKRadn2UM-9tET4DLe6uxHreNhqviY2j8hxBthEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxG7yqED2_zN70lV_biV6j-yKYS9DyewZEfZHImSHhbL4JZxYMDguOyV5Pd8IK7s5Y1a7lUksqnu1RpkUG2OQzVhyQ9xFNgvneH7dgEPNCSMA6xDgGUqndflg0x9Q5uFzjo9Vc1jqzxy5JVII5g86YRAdcp7eKtN34EQgViJvAsQNy3mDtIzZC6S4UoPo1aRpp0LLFBdc8mh6OlD8Sq0tPZmLlMWCoY4cNLUyiKZ5ijVhhoTZmoGNZr_5VQS_Ya_2Zb_nYZiAUsbwoF-9hMuS4IXYQGLB2-PWWS-EYPJe_PBUIekTD_KeIcbXBA0vBIHyRv9hKM3dxN3VYH6e0uQ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeQ-E4ey_8-l1V85NEor_iK1sBigoHlI_1lZY_mlR_Sb0mURGfdfPPfQofmx2lf9g5E8JhzYwRsR_Q5ElFJeeqznHw0YiHVYDVrEzzSHL9OC_KQB2-qrIwyoNZp6W4EjF15HC5R2QRmP0iSKQAKWkTr9i1R9_6rLitmomQ_a4Bld37WNs-83_gg8wS7G6dRudt7poWtyPRVNq_MtkDOBzyC_s-xvcbccPR5ivEDx4M2A8ZkHrLMFosNanfrTwmZz3vwPGotxl4LyVTzwNJJU_ijZ6d4bYn99ANPW68a3i6sy9xBzBY1iHmCgy5KNFDUvSHmYdEhrUqKzChsIn4FPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=OY_5S_2Dp89Y8L0i5MQo-BfjjHo7NAZPS_pOfBzaOYTgauq4WO1Xs3o8v0hGCfLjFz2A6PxIoVGZRNIKijd8KsBEJDukdKBZeXrn9da-Q-EOeUC1wqtsw0N2SBIpuwrwywjErPf9H-AIj7MF3MJVG2uB-83B2XSyA40B6aHBeUiWZISUw86KjPKXHx2uaSOBM9JWR9R8ED0KgcQ-f7jB89dFeZmo968FAXdJbKV5JAexvyQONaJeLteW4v4T5-2WBt12213e56JVSCn0vlR5UQ1kx8Dnh8OCnCVt_xhikI-op0tRM402gGFugk8pPbLIOM3YzXlFmxUCfB5WAIIXhwnqjNKfmbZq8QA3np47E5aZkxjxLDbXlD_709huyhdhxrHv-Nn8d2A-icA1kG1_Yh6ls-x6vKluf9VpmU4eMxk25ajLSsySECR6PDdNKP7-mEyBDOkjMAIjcvdbgMjCH3iMhOw-kZrH4IjG2CF0k8xjY2Q0_BSGrvJzqTw7EgPnrpmRx1Lg5-oAsgIoTgFBI8P7sRLuTax6bLClQUWRN7t_0mJ6_UEX-s1gKz6LwOC0vp5WW1au13igTRqE9bu09qkNYpTb2VVHfDI63pjAJ_zaWUPidLKSzNaXSWedwb_DxkfhTVpNqoOYk66HDTasAYaRyvFogH0aL5-cxi_wVYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=OY_5S_2Dp89Y8L0i5MQo-BfjjHo7NAZPS_pOfBzaOYTgauq4WO1Xs3o8v0hGCfLjFz2A6PxIoVGZRNIKijd8KsBEJDukdKBZeXrn9da-Q-EOeUC1wqtsw0N2SBIpuwrwywjErPf9H-AIj7MF3MJVG2uB-83B2XSyA40B6aHBeUiWZISUw86KjPKXHx2uaSOBM9JWR9R8ED0KgcQ-f7jB89dFeZmo968FAXdJbKV5JAexvyQONaJeLteW4v4T5-2WBt12213e56JVSCn0vlR5UQ1kx8Dnh8OCnCVt_xhikI-op0tRM402gGFugk8pPbLIOM3YzXlFmxUCfB5WAIIXhwnqjNKfmbZq8QA3np47E5aZkxjxLDbXlD_709huyhdhxrHv-Nn8d2A-icA1kG1_Yh6ls-x6vKluf9VpmU4eMxk25ajLSsySECR6PDdNKP7-mEyBDOkjMAIjcvdbgMjCH3iMhOw-kZrH4IjG2CF0k8xjY2Q0_BSGrvJzqTw7EgPnrpmRx1Lg5-oAsgIoTgFBI8P7sRLuTax6bLClQUWRN7t_0mJ6_UEX-s1gKz6LwOC0vp5WW1au13igTRqE9bu09qkNYpTb2VVHfDI63pjAJ_zaWUPidLKSzNaXSWedwb_DxkfhTVpNqoOYk66HDTasAYaRyvFogH0aL5-cxi_wVYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lESTEgFpkrLQ-B33rv4caFb3VWEXtl8SB7GTJ8z3A-5HTiB72cWjU9B8oNlKYficVdJ8TVG3nciVTGbFmP5CPETGOUi4e83QCeZUxC5lrv86lbmhNK8TFIbKPonfFWDWEqJRwRrygelwl1H--8fOCINmlj1Daw6Ui6pUvqAygWYAu1R37JoMDYAOkcRVCVX14y0ZuR2gSL9qY_jRVH8v7pYnWRRZcvQokMxb7WL_5oeOEMh4ghACFpX3EYv9opL_aYgmXt8s3i0HvnLEVKswB7ml_dZGMJOTpI1mD0IFievX4szItUzJ_xgyxcVOnjArY1yvwAg7p2Vghy4oo2ZH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
