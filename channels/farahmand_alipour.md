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
<img src="https://cdn4.telesco.pe/file/LKw2Rrp86RoJRNZXzxC_qK7bF_T8LSccWPwEygA2huMj-hdF_lmbUuQIlQD8c-C9a6MyHK0JqEgPPFQJWPl2Q5N7CNYIjMOLkf57N3UQWDmndBc4pkTzFuuQ-dwdB6teseAT37GL0KrSn4kH7GWInaoFdu2XrgwogA9LxNfBsSDZAUSL6SLFkP7iWKBS_-xsxZLbpiUaoFcukyNFHjtO_BSgak-8C_WTeJ4AhPNuORUgLEFIoRJUVBURfER9xI3TAr3IL465btl_9A6XRi1SPmcqnfbIC1vehyc-yM4FSIE1NQKHBj8z6Ile3xPnN69g3gsG3XZVqtsCatp0EoJ-wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsdBrk39VUkaHgUUDD1WoOmMQmDMorD3dhmQvAO7we9CoD6EHJ8_PsYOX_BGSktm-NENl7KEAXE616KH2zV5sCqbG36qPbbQ-xmkgpvTf99pllSTU9IPdA0_IMSxk1qG6Xqlt8CW38BZ02J-SBY4PnWVk0fv-Bj3mVVWrVf0bhCro15YMeXEGtQK0iG-HN8ww2hE3GAqONoMk5CqEU8JXbhAMOeFuD6BWgw45hNNWLTgBu2GNYpDPj4KIK9kXC2PN5wdOLzXxxVSGGySY0vz7gyocrGk-pVFptS6iZecRscGil-JSr1MYurFryI-32rCSFuTSgayzzviY_LJBOsNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=KoeCSgVYTmaY20OqFKGozP9C7ZiCvMr9GOAVMdovKvtauyzUoDdY9tgrXoxVzI1xtnwoGpPzRAplVimglaQmWVa9ekjZ4V8DqH1VXCnCRlQL4gFHbJ9tuKITHXvKnyjncY2mI44a-1oELjv8If5lHSpQ5wi9Xqa4ZTFSK5S679WyyRE1V8oQpFI4XvBxbr_wQkcZT_19MSDEosUioHUZ4VrmI0PTyQF6HSJ-HE7mTGBhrYIOdcbQV4edjYi1KqnMh6BYiwJMNhTym-xhgqGZD2DzXEw1cRkLfQNuiRjsvyX_EJ92OqToallW42L9VUfbfpXqAeuHUbDJ-WdFximUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=KoeCSgVYTmaY20OqFKGozP9C7ZiCvMr9GOAVMdovKvtauyzUoDdY9tgrXoxVzI1xtnwoGpPzRAplVimglaQmWVa9ekjZ4V8DqH1VXCnCRlQL4gFHbJ9tuKITHXvKnyjncY2mI44a-1oELjv8If5lHSpQ5wi9Xqa4ZTFSK5S679WyyRE1V8oQpFI4XvBxbr_wQkcZT_19MSDEosUioHUZ4VrmI0PTyQF6HSJ-HE7mTGBhrYIOdcbQV4edjYi1KqnMh6BYiwJMNhTym-xhgqGZD2DzXEw1cRkLfQNuiRjsvyX_EJ92OqToallW42L9VUfbfpXqAeuHUbDJ-WdFximUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=noiKo1joVIa1LcucPtvWpTmZtJ2LxtuWLWMI1NmBY8VhM_ISdiSe1aNbqOozPEaqvN-3PKByGQac4kKB-q1H9p7t-qPuPYDltwOT0VqzUX7M8lnYBh_hMfUQOunFKWeRRwLolYJqj929xRHeLSlF8NrqHd19uT1s0QOjTdc-1GkYPRnXSga9xLwmM-Jk3fJmbIY67eIvaLOT6G-bz_hHa3fbEsW9__TvlNJaVjHUUiX-lYCQ_wxklxFJ3Qq28nXVRAUD1MbGy8aUvSMUTzIg8McveJubKGkNQVU1VaABRbZkJ_ebvX38Pgx2aRnJKnTiRr0wAfgPm2C0pm-vOd78Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=noiKo1joVIa1LcucPtvWpTmZtJ2LxtuWLWMI1NmBY8VhM_ISdiSe1aNbqOozPEaqvN-3PKByGQac4kKB-q1H9p7t-qPuPYDltwOT0VqzUX7M8lnYBh_hMfUQOunFKWeRRwLolYJqj929xRHeLSlF8NrqHd19uT1s0QOjTdc-1GkYPRnXSga9xLwmM-Jk3fJmbIY67eIvaLOT6G-bz_hHa3fbEsW9__TvlNJaVjHUUiX-lYCQ_wxklxFJ3Qq28nXVRAUD1MbGy8aUvSMUTzIg8McveJubKGkNQVU1VaABRbZkJ_ebvX38Pgx2aRnJKnTiRr0wAfgPm2C0pm-vOd78Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcV-QQ_P9iv9O3kfr7wZfieZsr6DJqDM_lem6OKceUxIo0vrhm_yNwF8q4wZbMOpo7JsKv7fNMVjbA7aXA_8SsWGbcm0yvvlK4JG14o4Vl-sC37OpNHr9dOz1VgwO2tJrkelbQx3fYsfAJkEXT4BAunTJMJfWI1ToOA_MDWfLWh4bnzCbWXcpR6UTe7cMC66pAI1S4Hpy7CNNL9xTFC1zKrPu7LbFrxHrL8qVkk0mptaUezJNmzxN8Ked2oo2T_M3cD1cM8V1D1s0f-tZJlDLn9ZTTTm0UdAr0kMkbltAQuXrWypw0TifSgtfC93KCpoNJqmENfwloF240RN6sIpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=HIs5lJGSbB17dTvwu7CVevaU92eGB4TnNg7UBZkDqzbkzahiG0LEEpnw42isz3Q4Hbypc7Xv41pRZGYGmZps2l4HQCzsu2qeEykTncKNsT4-cVJk3YLFS663-CtvgTtMGpZkhXY219ybIyA9rIqEqqtkfs_6QRvEnH4k8n_ris7iCXFj5dkh7omPDX_cxXLJTaQ7o3O0ND8WT34mbVSzn6IH0eZ0KkJvB0G7tmGYGrfQsy6D7FC4axtOTsmSdSugz3HmvKPXNG_NJ7uqmL_vDjaNXqR6HdFIWFAHsW51A_iOrHLrp3CZNeHIIUIeB5hLWYgY70dIke-2XaTE0-bQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=LKu6egwxhHEu2bh9pznF_odH34AYKDZGNPohJBzxQU151Y0emuoE9TzM-7KHnDjNqYp0ZHFg459miKbRioBxugygU-lENuGHD3CHqI0Am6cWVXkPx3vHS32LM58VqmGefjzy2Bi5OtHWlhf1fgHEeel8tMOkEGqjscq5CF72xB61CMelS3Wk2unK9oGV5H_9vFPq4qBj7_xE24UBygkC9e4Tz5HNnrDuA-y7WJ9Y-7ZuMUDWwSLnlHL-OQVF-XXWWJZLLxYE1XjHWmQvKeSG4b7WbUX9NEzGAhZGLclPXx0RtKRlA1Nh28ewcND7jfgLxf0ZBPYjG133MAovXESo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=tRZZ7kuzRnwQN7olUEkZLvwiDrQcOD1xOhi7zqg6_VdVppxf361jkvrmaf_tP8jqR2_vCSU4zDGBwvih0rONsXzEL7H9f4dN-rc6Tn5wlFk3AoCErCnqf-7iyN08idCbjlxX4HcSxIIgyX3cZj7dEZqTTZGKN3F42hVfFo-FkVA0JtpApcFmeLGP-MUl8YvKEZEe7cDKr0NgAyceROgtDl1xdw6GhlzThF4oHnyS4PY2V0cxl74x798HIrTTZGuce9BNzRYu3dzLHp_aVOxu6oPlj7LILseYeiwWs6H3sN7JBDX2A0MgXuf2Y7uXFI2_4jEw_IG7p96-GEniRiJWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=tRZZ7kuzRnwQN7olUEkZLvwiDrQcOD1xOhi7zqg6_VdVppxf361jkvrmaf_tP8jqR2_vCSU4zDGBwvih0rONsXzEL7H9f4dN-rc6Tn5wlFk3AoCErCnqf-7iyN08idCbjlxX4HcSxIIgyX3cZj7dEZqTTZGKN3F42hVfFo-FkVA0JtpApcFmeLGP-MUl8YvKEZEe7cDKr0NgAyceROgtDl1xdw6GhlzThF4oHnyS4PY2V0cxl74x798HIrTTZGuce9BNzRYu3dzLHp_aVOxu6oPlj7LILseYeiwWs6H3sN7JBDX2A0MgXuf2Y7uXFI2_4jEw_IG7p96-GEniRiJWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnEgnb5v-DkFCM9muFkyDD5mgVktlJVGnTthevCcTt4VF7T9zs3dzn5a9GLa-GAKJljX2tJOByMgefE_uXnVBse2Tc1IF92pm_BiJcEzcSn5pUUtO9nuhgGSGxy11e2O5bb8Lds8dPHhyvzN8C6Otpjr8PZuimvk7RefXOPwFFFwJP8NfV17jmj5QK4eIvjOGQ9uiheBdvxbg1sGDweAk4FRVLMkyQcQFweGHxyF6MPG-3I4ZRNT1ygl79tFIAE4DyXpOQgidmCvfIK02e-yOsqTpdIkKFoAgMPrZ8FBA2FEnr_gLtE8GPWEkQq4et2-0yezH_DLX18__oxOahrcUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=RBZce4AN-9qXKBIlrWZzYLr9gcw8KaY2DT0L8FbZ-jvQZauekwlIxQVjWpo0n5bX9UPjsQ1FOGrPxOM9MksYO010lKAZ2bnYHxZh-FlBJYAl2pLYD6Jp-kJXXaEe4pjCgwhvVHNLm8u2Ma78iUtDQwLt2RFiDVYBpL7WwMOdHRRGPWB7mtC6dgokSwe1t9RWLq8crtmPYj98W3vyyTozB6h3jRWWqNaSXkGnsiBxDfyXfBWqdE2o9XNkMPJV9W-iGlH3EzLK_bXjP8CinfDDBh9ZmoisOQbn4CdhapGDsg77HHbJNm2ql8agT77Igu6U1GqraRI9lTO4YZgSK8MmGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=RBZce4AN-9qXKBIlrWZzYLr9gcw8KaY2DT0L8FbZ-jvQZauekwlIxQVjWpo0n5bX9UPjsQ1FOGrPxOM9MksYO010lKAZ2bnYHxZh-FlBJYAl2pLYD6Jp-kJXXaEe4pjCgwhvVHNLm8u2Ma78iUtDQwLt2RFiDVYBpL7WwMOdHRRGPWB7mtC6dgokSwe1t9RWLq8crtmPYj98W3vyyTozB6h3jRWWqNaSXkGnsiBxDfyXfBWqdE2o9XNkMPJV9W-iGlH3EzLK_bXjP8CinfDDBh9ZmoisOQbn4CdhapGDsg77HHbJNm2ql8agT77Igu6U1GqraRI9lTO4YZgSK8MmGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmLPsF4slBX1HdXVp0Sa1gPbtj8fyAbPxuMsrQMaE9zMQVK501azP5keLVMdoOELvj96ZrmdJN7M4kX36Kjkz3jMb29RCOVTn1p6IdTokZt0JH2cXOepl0kJlzEiYhq0VxUzdV87D43CClnIUJL2B4ClRvDmr9YX5KR7wKVGNx2_CDMgixqJAE2glx3s370oZ3AlPlD8LEFq8Eh3IaqR3RJSad5kY5O9WJt93ALtuSFHeA3CpWxU8WVBoyGfwTCSStskVuGBBSKTkGVz0RBfn0firJrXjUKVdUCsc7Bg1fteVoqe1AP1WaFGvzwDkWcPtfL5OPaee9_iZri-uqh00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=DSrrFgxkg92LQ_U0mPdwNN3309G-hzarFDX851fEC5y_EROzwiNBaMMhbU_4mW30eyqq-ka0NUwqVsUGl61vnX6gR9wFvVqTxrc2J_BYZBHSkIZbUbRe0yEj9sRkhZuTt-kXhKDv7fQM3FOTjXjGLF0Ypp9wbIdgDB-XlLbSjxmhfbRk0ZrMUp1xeG7CRUC2ko4dP4NcypAn5taZ9Sck3E__sYHQSzfM0wcEjus6z1qAzPExVv8P7HFj2slUQdBVNrAM-o_BRWqoeN2Pu8nX9EMlaPMSw9Y5f_c5GQmoZlSgfyvdt8dshvGdB3bPynDbS9-hMyrcLSgYQWkZmsNYMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=DSrrFgxkg92LQ_U0mPdwNN3309G-hzarFDX851fEC5y_EROzwiNBaMMhbU_4mW30eyqq-ka0NUwqVsUGl61vnX6gR9wFvVqTxrc2J_BYZBHSkIZbUbRe0yEj9sRkhZuTt-kXhKDv7fQM3FOTjXjGLF0Ypp9wbIdgDB-XlLbSjxmhfbRk0ZrMUp1xeG7CRUC2ko4dP4NcypAn5taZ9Sck3E__sYHQSzfM0wcEjus6z1qAzPExVv8P7HFj2slUQdBVNrAM-o_BRWqoeN2Pu8nX9EMlaPMSw9Y5f_c5GQmoZlSgfyvdt8dshvGdB3bPynDbS9-hMyrcLSgYQWkZmsNYMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2eTveuPvcAKANspUcqfGzxiFyU2F4cMG3dNowYMgchbZzui_UjuhmF3T27C744qb0-MGIaeyvUNX_AFIDnOq3diVG82ksJ8MdcREsvjL0KmTjr5BTr92OcMiQoO-JCG3RShVB3MRgqw81itDtoVP7k6iyWNlO88EmkWw5tIiH2aZb3oXC2SMbRuu9kIgVB9wQLK7PLo6KdorjGPzlOvlJe9EG-dw8DScEuPwELbVVZuSoGCOotwkSP3vMEkgk7bmPRigfIXFeDB7l9yByTwquPhFGt2njDw6oN_P8-8Z7ra_J3W76n4wZZr8b9A0U3jFR27tA6qS6OLG1kfW9FL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=CL5hh0dOg-OWiyFkNPZCkwmlBfPMtFl9yB5vMzK4vfv_ZrIJbeGmDWoXNu9CVCY5KFQjWRAZ6TZ_E6y2NC1VpFr7111TmxNQMClc4BLuKrKrlznrEnSaVWv-Uo8nHnYABtLAS5utxolEufreRpsDkVaOnPqFxMsQi-tZygHSQhvKGCMqbop49xjQsvBlzSzHAbpELyOhmC8jhdxN7FPuYjHaW8MGD81h-tg2ii-621fvxrUZBp0gkgnpAjENA_J7fA9Sjge_en-j9-gNkt9qPRPWdPhJqYc43HCfght9u-JpGpnwwBP1Ag7aRx2C39se_KnT2fzDy9wHjt3BrWjM7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=CL5hh0dOg-OWiyFkNPZCkwmlBfPMtFl9yB5vMzK4vfv_ZrIJbeGmDWoXNu9CVCY5KFQjWRAZ6TZ_E6y2NC1VpFr7111TmxNQMClc4BLuKrKrlznrEnSaVWv-Uo8nHnYABtLAS5utxolEufreRpsDkVaOnPqFxMsQi-tZygHSQhvKGCMqbop49xjQsvBlzSzHAbpELyOhmC8jhdxN7FPuYjHaW8MGD81h-tg2ii-621fvxrUZBp0gkgnpAjENA_J7fA9Sjge_en-j9-gNkt9qPRPWdPhJqYc43HCfght9u-JpGpnwwBP1Ag7aRx2C39se_KnT2fzDy9wHjt3BrWjM7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG1pQ5V82Fu2mtzi24MfSOTQOfWz4rTfx96TxUTiTuglp_5z2eV545xvIeYN-se9Wh1Fot0il96Oj7xT1tJfFpazAHxfbv2zWes2tDQOfNyqRL_jNwHnDg0HPIwYlTz72Cf9YjFVQcCMvkbGQR02LCvRqEy2W8LGhqFqEkS80tcseTkwGRbleT6KfrR_hImTesgECHYs3e_hxwXoJjuEtIQnLC1NMfhdrvnCzNtnOutZrrVLhIruW3PKJHyw1toFQ1MWe-7ifaX0o6HbGHFdhOuG5umMHFWX7zQSjN97oEzeCk7av1HiSVSg91IqE9hotU8IPW7MbRio1cC94s1XIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nO2ywaIrWEAFIVMlIaYgAzzsfInPJtI47NjWprWqX2NQNuN8KVtF_3AesEWxat6nCoFfn0KAUrEbAIwWSChbFI4Ld4em7ESo8b-n8ZCb74quuwbJBDvqxyXYwldY2Tursm2z7q0ZrRCFbkxIffp8POBTNBRhq44bBxV0R8YvgmQb3Da7Iqr6kgsArMhAyQSdA2XQE3EMT1oMv4ppTHgAI3IgAq0OF5xO2v9ydHqdu9cg92uaZUio5wMeqlN_7ASBjsgF2RhUAvfXNR7Lw5Qja8Wi0Y89M6sQEB_4A2DA2tEccQ4I_wVZbq8bD64SUU9hocGauyJbqZb2oWXsB1Iolg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=if9vqCiaiw5bc37KBiLVshD1TIElui3uKGFK5GYh4q1y_LkjZ2WsTun1iiRtI8nXi6HoqNpmhcJ0BvKO5Q02Mw_irOqjXikOokdnVBwNk2UKLM9uvPuZz7c-K4XHlvr9tWPJuTZK8gNDjDGPv_REF6DcS6041F1dWC593sKVUq4-yqhgkZACKbM6qcmAYiDPVQ19L78lEJZbhg-PME1d_H4Zt2O8gWD5mD4g3v7XUHsY7LBl22IkawtmCokbuo5GD6zkizPU33FXzclv_YA2vrbW2cWvOCYVh6W4vVPROqJTIlAY2vgc2TRXFl2YqcuwlBbLZVvJZMHcdJQvH26Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=if9vqCiaiw5bc37KBiLVshD1TIElui3uKGFK5GYh4q1y_LkjZ2WsTun1iiRtI8nXi6HoqNpmhcJ0BvKO5Q02Mw_irOqjXikOokdnVBwNk2UKLM9uvPuZz7c-K4XHlvr9tWPJuTZK8gNDjDGPv_REF6DcS6041F1dWC593sKVUq4-yqhgkZACKbM6qcmAYiDPVQ19L78lEJZbhg-PME1d_H4Zt2O8gWD5mD4g3v7XUHsY7LBl22IkawtmCokbuo5GD6zkizPU33FXzclv_YA2vrbW2cWvOCYVh6W4vVPROqJTIlAY2vgc2TRXFl2YqcuwlBbLZVvJZMHcdJQvH26Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmJ_k3z8Uo7eufcdDiMTD9RUxSiWPFNMfMgpmYO3oGS52zx_CYHzf-9OFMyqmyu0vU_sTJJxFByldNuRjWBgbV6_fxwUBqvJWNnwsgNFyXxE_MlTHUNizU9M3JPsr36dFRr-loPpyuCGMT0lURlNHFr9MwnbViLj7m2Rvr5O-z2QjFXa6RN2jLXsO2Z-jP_fZV8YTkn-ouli6Qd2J2zIRL5KFxhIG4ovVXit5oDJI4ascWzXQbh9ye2vLPTVso24gBE5mdwIDM5ya7YGtJPIPqy2K81HZQAcFdrb10onT263W0rOMG0MkXrJf00tjZtanvxdxPunQQWuI239g8LZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TilCnAReSNSjgKjnQ9UT0Gs4dqps4QEXMk2ArmciaIOLzQrY4xTDW2uXDUSu18YG9kFmtTNCj-yAs4jBbZTqsMp7tcay1gPSguVJvuEYe4k4hsWziXSY5_TPWreKkaugZ_2ABJdvELPe7AkuFDfnq_QBdtYW0id7CgZBIpA_gZcAN2Y5KsNFHNtkQEirHjz_OYPIyZp3_cg2Ej_Xc5b2fyMn7sk9lAHqHuUisFDrtqEv-TC6Vha8a28B74sqWUD4EVGZrxTTWe3_J8haJc5mTClrMTz3vMnjcbaZq6qUnJ2c_kGcFKyfE47aTRVabHeX_cUEF966HWzgwaoDXjs61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYe9b78alNtuo4UoDjqM7Rj0cirGJ1sUs-rzeEcAvP1JK2cuzI9R2HSDrcFaTPd27ueXqCFkhEgdsNRXGRBeOC9G-Kaghdwd6gfZ0qD6RE8iOf9wDgAL77b7wJAFJ0B1AvvwUr8P_IZgX47Ej7xMBcXGPFJZP7UAUlyyxlZ5bmIuKh0zyGsgi-AGUb_J1r9MDf0jZafbgIW9ANaCeJG0uJNrqyqmXLB1kWreCC7ZeUZk8mUgpo01n8lH24UyGRcs1u_fw3ogEUUClqYGXqfiG6aKk2GULJquiZNdQoFP9oRRyH7ZetXYgI8zIoM6zDalyi-rP3bEvvbI8OaVPeUsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPaUWjsMyf_inZV5L3ZYv7F1WenZ14sgno9EgTDqu1y3Amuz8EaAfc266KV-_Pm2BpNiHBrv3KGHlnsmZNF1OIg3sO_qxqDX5RuscK9ijbSdeedtf39ANhdN4MNzBqPKDWA9vBP_XoWWDjGqK9Bi6lY6j5e644elYldbmg2unxZAuV7wJXTqsuBcW57waKubnRXeTj74RPpK7V8A4ZcuPCyembJdit5uNkaJMEGxyOIy5rRQ14fGrTtq0pfPXTbDRuJ8AHtFPODDA_J7VELa7RXNH64tMfqSgqO2PRMdzEjQl-PNQKcU1VMAYVl9AmyH6wFKdYgH2QMQ-HTRGlbGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We4ae427Dry2aABaalMQ6c-Dtfl6-kStmViDVGh2BcyjMNnwTADDZLw4n06mHOnihM2BT7_qjlihjzDZPBVdeMutlqwJpvfTEurqyfi2GXApRk9_IwlHNL5FbhsdDO8SCgg96lex2XNYMu2BW0OgyhvwAV1njE5XJSwmxv7ouxyTcVNOR6Z_4MZP3rcGfW4Vb13kegGXHeZpn6b2h1cKGHJhjBYekRDJi2p1o67wJsobsEQGpOdYFTs8lZoxVH_8MrcL7y2H4CWutiMrV6HPTEi0glmIiUiUYVTJk-cYacCxEDpBW7doHA8Nmj2ZH0YlgJ0gwTQtZNcaeuWoMzhtkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=OvIjafaMdI7UvwCilBPDSkERirX7MpJypugoOtdkwGZsdtawqVuvZMDrXmIImDxgfuz04__sf5tCHLiEMB0hq0EtkOn_2zwX3oZaDtynxy-pdwv-VNiElZ0LenARgmMwCwZKeR5ptYpqgzIcUUuic_w2OF5T70xnkmroUFF1Gi4aQUbYLDjGHPAxptH_Z6Zp-mSBOSBDu0gcF_Lb1dAwgO0QYQzpcpYMlg-5P6X49DEb5CIl-Y4IMg41k7mQTmTgSu1Qi-D477IOlcrB2NaokDBOGNU3HUx-EmD9JHnvkMx9ugWcr_KCskMvPswwjwPRlMU9I89d11ZFTwav_zhePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=OvIjafaMdI7UvwCilBPDSkERirX7MpJypugoOtdkwGZsdtawqVuvZMDrXmIImDxgfuz04__sf5tCHLiEMB0hq0EtkOn_2zwX3oZaDtynxy-pdwv-VNiElZ0LenARgmMwCwZKeR5ptYpqgzIcUUuic_w2OF5T70xnkmroUFF1Gi4aQUbYLDjGHPAxptH_Z6Zp-mSBOSBDu0gcF_Lb1dAwgO0QYQzpcpYMlg-5P6X49DEb5CIl-Y4IMg41k7mQTmTgSu1Qi-D477IOlcrB2NaokDBOGNU3HUx-EmD9JHnvkMx9ugWcr_KCskMvPswwjwPRlMU9I89d11ZFTwav_zhePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=bimyjjVL220Avqq8GWw46LeJ2J7Bp3xFtBrxNmjh1sNFwDL6f4mvNo9AYC5zVxhqUhhvPVGNwcmt9pdNOKN120WQ4wSMQeFyzaG0-LS5SxR9w_PJElPcZXuuY4rsk0Dt4xFCnccT6h2gXD_Bo22GGVHDhNNDtCXjeaysNMaLLJBUawGh8BlERDEFDbLeLEGGfPwYgo3IOTeCNugGO0f4ZJzLcbNpiCBL-32PMV_DrGxjcdvIlMmKjknRE7NI_LeZ0xmeNRe4wOEh7_yBDdzPo1x3cVoW3Ac25CckbaJElDFNJhYHQ8knbOsO8ImGia8UCfZr1zWJj9lqvOv7AVAteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=bimyjjVL220Avqq8GWw46LeJ2J7Bp3xFtBrxNmjh1sNFwDL6f4mvNo9AYC5zVxhqUhhvPVGNwcmt9pdNOKN120WQ4wSMQeFyzaG0-LS5SxR9w_PJElPcZXuuY4rsk0Dt4xFCnccT6h2gXD_Bo22GGVHDhNNDtCXjeaysNMaLLJBUawGh8BlERDEFDbLeLEGGfPwYgo3IOTeCNugGO0f4ZJzLcbNpiCBL-32PMV_DrGxjcdvIlMmKjknRE7NI_LeZ0xmeNRe4wOEh7_yBDdzPo1x3cVoW3Ac25CckbaJElDFNJhYHQ8knbOsO8ImGia8UCfZr1zWJj9lqvOv7AVAteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=jEjd6sMHpiC0vio_JS6TCvSYOnkiM-bCIGQwiYuCbelbLd1iZxxSrzgqpyUtfiDG7Uam7ZkwO6yzNdJiMyt69Mj3ra01HJV-0e9oMW6VCK9ra5mskRZrYcXRTcLdRkT8dduvnRFNn7BwEjii-g5N0_8IJkH9ylbSSkHtGW8o_4Ch39IHSHaDxJ04GXaxWUpC5dIHGoB15S5lB-r6vUXzy3NQVpdWOOAxK-3cPGoq34qutQCp0JW70Z6vbqOsU1MGkJ5mYMwFemBPgU0336m2jR0bQUbnxepkDoKWFVW7g6ieYX-Vkc70CFIVBAkNXzIdK4CRvo0YsaGRLYi0Bo66Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=jEjd6sMHpiC0vio_JS6TCvSYOnkiM-bCIGQwiYuCbelbLd1iZxxSrzgqpyUtfiDG7Uam7ZkwO6yzNdJiMyt69Mj3ra01HJV-0e9oMW6VCK9ra5mskRZrYcXRTcLdRkT8dduvnRFNn7BwEjii-g5N0_8IJkH9ylbSSkHtGW8o_4Ch39IHSHaDxJ04GXaxWUpC5dIHGoB15S5lB-r6vUXzy3NQVpdWOOAxK-3cPGoq34qutQCp0JW70Z6vbqOsU1MGkJ5mYMwFemBPgU0336m2jR0bQUbnxepkDoKWFVW7g6ieYX-Vkc70CFIVBAkNXzIdK4CRvo0YsaGRLYi0Bo66Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=lP4UDHLppZIdB62bvCa7LwxkhxBLcy1LZnqV-KExQ1LnRtcsPYQ50soQHdUP5fTp2SVIZAXVVy7lZVvGuxm2verBlMn5225wQ8WL162J1ldvLyHkm8a_T2K_eEJfntxtel_zbQ6No0v1NS0LbhueIdGhJ9IuaxKjgEL-exzP4WQ6G2LxcU7DoyCYsuY6jbkSr8E9ecIgILNo72exvFDg3ntOZXpK7LZYARKQaEyHEEie5IqGD5tkrIo6U_K_Mf7ILnhvchSspYZDP_ZVzmuUP0_bfmVb1eIhUqT088oeeGNDz0w2lBIJtb5JoyQhFk1-r1bPyiw6cyyrWZ8Pusn9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=lP4UDHLppZIdB62bvCa7LwxkhxBLcy1LZnqV-KExQ1LnRtcsPYQ50soQHdUP5fTp2SVIZAXVVy7lZVvGuxm2verBlMn5225wQ8WL162J1ldvLyHkm8a_T2K_eEJfntxtel_zbQ6No0v1NS0LbhueIdGhJ9IuaxKjgEL-exzP4WQ6G2LxcU7DoyCYsuY6jbkSr8E9ecIgILNo72exvFDg3ntOZXpK7LZYARKQaEyHEEie5IqGD5tkrIo6U_K_Mf7ILnhvchSspYZDP_ZVzmuUP0_bfmVb1eIhUqT088oeeGNDz0w2lBIJtb5JoyQhFk1-r1bPyiw6cyyrWZ8Pusn9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPaKmKR3DdHvLKYI8-r5ygKQNyb8ItMtsVErSnOjrk_NtmwQfI7l8FrFSepEhIY7ALLGggxltli-3OEcRxDEGy_FBbBJu1MsrK71l6MDS9ecaY8wcny6WpIJId6ZuXdepD6FU6o8TKMeOTUBWSwX5U369E6WC2JG3weEvVzbPw9meRrngsrY81q02l-_QCeOQwJ2SUV_X6DTwW0JgZ8L-7zOawxuL2WE-Qx8e28iRha-RWwkugOK1SmwzpbR3xQ1seVmC0uz_ZHu8egtiX4YtWWLVCjiQWY1u8Jt4XxDp_rdOmEOolh3oLhrm3YVaE3Do4VOKInP6ZKjOzJ45VcZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVIVg7bJ-BPCVWTaKy9JncJlqqRh3SBg9CV4poqV25D8gOxok3c2NdiSDbjAabsydD5a63YhxqvlACNmt7XxUAjimEkAmRJmxtxGTw7_7ZqYlwOioiSr15TJuXUerXQuY2GUQMpN9AhRZoqA1P_YRJ5DIOy6eoxkApzJTJgcOqtxpxgiyLUqDaufFhaNn8WFDkAdSmM9TkxUG1_qvLQLUmph1IMXwbLX4lzT9uOocQ36dDRSYaMyfyqZvHL5h_dJTrj__z5UTew8Cp7wTnLW08unqW4mnbArsWAWuzgCqnnwfwfZ8iXh4egdFgHaC25DfYxHoqbkAa-AaydTtfbpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Ay0D4Sn7LMo7AhDVc9c3hw5O0MTJ5XPUZAtlMKzW3y1zfF2i38JtAgPf66LGm_ydkso7O4x694Nmys9cVi7492O3BMqrmaW_IQKI056qtqzR9srO-XDwjTINMcSX_kfXlMkjDWjjuTXXpy9B20Xi0vBawqEFLYBMyG80C3fq8IGUdf3PsOVMEkdVlH2aR0LY1MsjzIqARUXcIqq6oEFgptaDEd3dprBGGKtmK1x_ozJWa1TESoBzo2MIaI11E_zPxfeTB39zyJ3cijnuMWGj5oaHva1BoUko8Ia0D9nN9ooFfHQp1eXP1pViNfxHXrtnFKtSNXA22DKRM-1410il4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Ay0D4Sn7LMo7AhDVc9c3hw5O0MTJ5XPUZAtlMKzW3y1zfF2i38JtAgPf66LGm_ydkso7O4x694Nmys9cVi7492O3BMqrmaW_IQKI056qtqzR9srO-XDwjTINMcSX_kfXlMkjDWjjuTXXpy9B20Xi0vBawqEFLYBMyG80C3fq8IGUdf3PsOVMEkdVlH2aR0LY1MsjzIqARUXcIqq6oEFgptaDEd3dprBGGKtmK1x_ozJWa1TESoBzo2MIaI11E_zPxfeTB39zyJ3cijnuMWGj5oaHva1BoUko8Ia0D9nN9ooFfHQp1eXP1pViNfxHXrtnFKtSNXA22DKRM-1410il4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikh14K-qOjStFtZJV8jwM0O80yMVzWlHKCyJFCNvyuf0W9WN-ZdEiHjMrseGmJT89cIjezyuoTw6ndTV6fKtVHpKwGTE-0rZP_3QFfsjAB2p15B4XZMjqJDsJXkVwa-CvXzOg0oZzMCkpzpyiGLzWpBKGKCguihO7skzA-DO0eYQCswJwktsvOgQj1GbIHBTU6_QjK4P6nz-qM5pyYYYSoVj6HSQH9X0rzX-agqQX3cEFAt4SBA9XWiXxiV1LfTu6zv6H8_r3nP6jl0oBqG0wVE5U-XesACXP1dLrZn_E5hBTaLVjlroF1_8IYW0rBdhOuiUguYrwgX9iQhI7Q-ayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=PLiGz6vdnOITkigdH-koSowNgnbfCzTXbI3vTYzt8iGOQknDOYzXkEqJvaJI9GrU-pgGK6cssQvobx9bJf_2ki88MFFVbikikZIkQ2mmxYkheONLKLBaTMBNZBEl-GDuOOxl6S3YukGTiErmdMf-kqueNIBI1DxuS-7LXfVl3W-0Q1yxcrcooCFUnX37oHTxYbpK_-8Da1LzsPpFwA0yLjUIEity-y7D3RDU5ucuBS1F-mPOtHkPCV8Hl__vkn0tlbnSUyVoCcYb-h9PdNmBJJVIzW7eTzHD3TfyJavwvg9O5-KUapF9KXQuRaqMFRJ-rO7p301CkW5w__OUYYa1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=PLiGz6vdnOITkigdH-koSowNgnbfCzTXbI3vTYzt8iGOQknDOYzXkEqJvaJI9GrU-pgGK6cssQvobx9bJf_2ki88MFFVbikikZIkQ2mmxYkheONLKLBaTMBNZBEl-GDuOOxl6S3YukGTiErmdMf-kqueNIBI1DxuS-7LXfVl3W-0Q1yxcrcooCFUnX37oHTxYbpK_-8Da1LzsPpFwA0yLjUIEity-y7D3RDU5ucuBS1F-mPOtHkPCV8Hl__vkn0tlbnSUyVoCcYb-h9PdNmBJJVIzW7eTzHD3TfyJavwvg9O5-KUapF9KXQuRaqMFRJ-rO7p301CkW5w__OUYYa1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfbfVrIlsdSnaZp-kzJ-ibFqfBIR1nejK5JYmMwvMNRJHY159X1Bs0iPxDSxv-B82MoSy2PpcnYtDdU66tbXhnbs0isV4tFXB2g4MxC1HkM32o7g2TCprgIPbht_aTDHvbpU6foXXohis53rvhZuby5xMdOBbM1BO9mK4xYlhgIjN2cg1pT9aRr6N_pMjic0qn0daAOqjN_6nDm5nPVYG7aBhQ8yoxdB-535Wjp92HPJ9RXvP7dZXjPJQaaBkE387UctvtnD7jvFOGOcFWtF1wc6o5urCaH7MSzq2Wut_obXugz--mXfiXNovPzY3qlu4Nt1ee1Gja9Zhg4RptcDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edNSNTc-3ZDDXnv5GdYMe16lWAz6zCRWznydJ-CHyNvfVQzRY_LyB0Woo967AH1n25CRmla34rqZvgpbrIF2im7UaZR1bAp-OL1slzPefBHsejqTeFLYjIxMNl_RlTNyFkOktE0KBrG3YSydR6VHOdmTbwI9WG1nkOj3zjN9Cl02jF1ukhd4jArYqUm7EBJMxQ8dDgrRxImUIeciDl64bfBOf2JvqQsE0cp7Jc6pCGVYwyzWU1nd4Q9jnN-Cy3iTA-SDoXax3IzRvPupobRT1hOCqeUqsQ26d1xk-WRwwa3_WzmYf3uZKnrLeJiXKMWBCUlSq7tI-8G2oef5A7Lm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=GaOie0e_zfk0TcOpxgfNvcths8tYYAzBLqKwOwNyit-FckAnvZTfYsZ9WOmkqCECF-HcFyWbkzxckhc5tWIcRJH1jCyqLuw_FQ-usvFBkEqdMMpjfXNW3s-FLU6fb5XsZVmv3fEpULBcDvJV30zXhQqcKoypa0GTMgEMjWB15ujBY_07lcCisZO9wIEsZK0d4Shr0fUnKFMxx2id2KLJ9l9K7-NQ_sbGrzr9AoHMSZe2xgsmS1bzsqddOIIFeCUv8Icl1MlZm2-5xgdhhGW9YiVhrD8GMaTeL0A0RApPTxhytvqGRHXajABNDBQ9A5wZ0KqWy0JziWj2HYq5Tg-Gkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=GaOie0e_zfk0TcOpxgfNvcths8tYYAzBLqKwOwNyit-FckAnvZTfYsZ9WOmkqCECF-HcFyWbkzxckhc5tWIcRJH1jCyqLuw_FQ-usvFBkEqdMMpjfXNW3s-FLU6fb5XsZVmv3fEpULBcDvJV30zXhQqcKoypa0GTMgEMjWB15ujBY_07lcCisZO9wIEsZK0d4Shr0fUnKFMxx2id2KLJ9l9K7-NQ_sbGrzr9AoHMSZe2xgsmS1bzsqddOIIFeCUv8Icl1MlZm2-5xgdhhGW9YiVhrD8GMaTeL0A0RApPTxhytvqGRHXajABNDBQ9A5wZ0KqWy0JziWj2HYq5Tg-Gkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=i1wbD9TWq6O0afpxBhh_A3kp4-DKIp3mvErUGXr6Pw1tMZENSBGBChWBUqkaCgkyI38HfTEnQstxDYwnBzk4METPbndIEp-yIiAuo_dICYReTMnlW2bEMEZoDVYRF2xOcZ2Sd7inGFA84hcT9sXxfJyPBRVOznGyTRary98ED1UOl_6iIbFrKrOJxbsj_iswfjXFXzM-IEC6djlZioDgsji5FvCbkP6I6gFZ1Mm4NHrgfRVSTW3PEtAInVHeLhVeBlRRZo5xJ0u5FxkJwp14kdu_SCrcLKIAzeZUMGKmRBRd0Qa22cWGjWTzhIlT6YiosnwKZjjJ4-nw1WiEQQQX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=i1wbD9TWq6O0afpxBhh_A3kp4-DKIp3mvErUGXr6Pw1tMZENSBGBChWBUqkaCgkyI38HfTEnQstxDYwnBzk4METPbndIEp-yIiAuo_dICYReTMnlW2bEMEZoDVYRF2xOcZ2Sd7inGFA84hcT9sXxfJyPBRVOznGyTRary98ED1UOl_6iIbFrKrOJxbsj_iswfjXFXzM-IEC6djlZioDgsji5FvCbkP6I6gFZ1Mm4NHrgfRVSTW3PEtAInVHeLhVeBlRRZo5xJ0u5FxkJwp14kdu_SCrcLKIAzeZUMGKmRBRd0Qa22cWGjWTzhIlT6YiosnwKZjjJ4-nw1WiEQQQX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re9QmE6yBKYr1FL8Vi4iuwcqyOIpzMSblJqsZ8KCQca1GMUBOLhWy_ZrTsNPdVDmr9v3vf4MOSXtBCmQAfFDA2nAZ-ELdMgZAJ7ajnCf4oYNV7eVd5XheiKgWf8btFhN0XiiJHspbjAaNaCT2a6e3oMD3WTcTA4eHIbjD49ZoeIE89Y0eQmXwgbRNLT6wN92ETbsuYZ-WUda3fWFTvZk3pg5qJMHnw_RY0n_prxOArX3wfI4ytrljkXV1cGuIMsjhNpRL2bmnXaiwTYOZXImaukSRN2rxP4YLKptZyw_kHjNT_XglOn-EGnFhsLwxMmhpoy7fkoRjpFWm_kjCYff6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p611Dg-yZEL2ijszDwgj2fWnOh2lcwyZzBpAtDPfazdtCjziM8qLCbvVR-j8r7WkagIsREOwy6WgfS1rYGd50jyAdedqV9fVqV4z9Gs_SxCniqnyj8RKbHUQSGLgB8KkvDAbm04sqh3zhfbAGhY_dxK7VCiDH1dZrfxvVpcuC_8Nu4tEIzKLnVQA75EEMhOqWb3y2dL1j5LXWoe4Yz-MvsxeiP5ekJskx4KPi1icK57dY-ePbvBwbEJAmcoroXActHV4VKRIe1miSwunpww5C26BS1agAP07OumiBDgZUk5gk-3PRDINxpCZjIZtzNGycC1Oful12_k0gijACZJwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnhWX6snhmpzom9QdmrdNwbZodVE0fscBLD_1WiPLXlpmzpExsZzaw_g5z-4q4w908nUd1PqvC_cjqFTn3pWj6dwEI01pJTZDUeWkrl_XaZM49hNMK3SViMowj0zRnHD7Ml18pjMuPOoTgxtJQphKpJ4RZcl3u1UqgkNZtdJSOPJwO_2hrc_ne30x407-FBf1vWtYGRbkaL0W7zTDrvJ49pYz75ULff5mDnLQ6pRvjHFYb34NKYzg_RgaQGLT3fbeZ8Tyr37ZBTsDRhyai17lUGmpNSMTcbrGMLD2Lku2YqhnpTCv3cGXL-h_sFOiTqoXGaqyMwhWsPzez0cfZZCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=HNjKXsgQ4BKQ4rEXcjclWBl1DpOR536kPsFfZxjswAyPXPYdHLt0V4jndlD3pSUBFFDd13zrSyvwcLcojcACeAZDiZP8LgTGHpzbPwntKDcbIymxmv9MX-soqYnd-nTDaiZHVULEdTLV8_vjwx7t8z8jTH6gWG9HQzJH_1G1qlIqZbXERkJe0n1GFsxuNZ6GS5FFJlKllV1RfIHbpIMU8a0lWctfKGs0lnlJGWAd5M7fcg9H3SxLvZl_BO2Xw-lwgQ9JPfmTYiYclHhvipgpLT4zT6etffdm0m1iR2j2VWRHvjTV5CXCwo6uEbwMNNTv-ohW3LV0HSECmY2uZeYEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=HNjKXsgQ4BKQ4rEXcjclWBl1DpOR536kPsFfZxjswAyPXPYdHLt0V4jndlD3pSUBFFDd13zrSyvwcLcojcACeAZDiZP8LgTGHpzbPwntKDcbIymxmv9MX-soqYnd-nTDaiZHVULEdTLV8_vjwx7t8z8jTH6gWG9HQzJH_1G1qlIqZbXERkJe0n1GFsxuNZ6GS5FFJlKllV1RfIHbpIMU8a0lWctfKGs0lnlJGWAd5M7fcg9H3SxLvZl_BO2Xw-lwgQ9JPfmTYiYclHhvipgpLT4zT6etffdm0m1iR2j2VWRHvjTV5CXCwo6uEbwMNNTv-ohW3LV0HSECmY2uZeYEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZbFzm_y8fNjY4a-9YjHHpm4mBKK-tFsMq8CJ1_AEGn-tb7ZnJMrFbirsX4oXkfS8UneoTZVpcgS19j2xfX7hRsUOhQkFdhhzaXIFG0jZajx0nTP_ia6Dgog39Lp2foiDkNIihsZlRVhnOP6lagK5kQ88XjOkrHPxbSF0-Eq5OufLRfznPWjpFAVQt4__p2Od5YGoxJ-IGPSS97XDC3-VJif_OcXAouNkWaOQwOZRU0CxnQZADJauuUlbpHbvhdBci7ADEtOC9N8r6iQT0Ivn3buBMP49wiRMvdjQVJqYVwA0w8zHVKQbwTJ07dnVpgg6xqB2oiJCt59kk2-MY2DIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8WGmNNXbuSugsdyvHA1CU4Hx-dStMzvGVe4oAjFPR5QxpUFO3urQl0WJ-usibQhZmqP41EVH7UAt-qX-jLdDp75FyDO1XHQpLijIOvUaMFW5a0Rup6IU0KiP3xvHIJfe-Y9CEDYL4usAML-YVq7kv0vZrcaiO_3TGYR9aW3hKoyD30GY23PhC4AfR_kWm3PSGyjmTGhhz3fJRh0MMfTPS0HNfwOsefFsgzfz6uLARe8OSK5TpY71oOjVdQ8mWgOcySORxtD0Ldvd5ayvqFnhQz-AF6HYq033SFX6IpWQZeKv-jqvP0AUim2FIEU9aB3zEbCRDxHxsiwyoYZnuxq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XED_gQXXihf9n8hXV9epwwkb8dxmNrmA_x_x6sF3ISNw5neiKRfINcuKTT-cdJlaRiHZyfMP_yZ0vI9Cyy48AZqjWQzfDMTS5aSooBEJmBiopEWraa8eRV0iM4F-CP5TMTj1qey8H3bYg15Tb91fTqfuQ3iirmUtmR20NN8ZI3SGRh58yTBnRjjmBg4jediCzgT_E0TbCbaD3eYdiAuQ02R_JzSrD7MGulm8c_MrLf_-ERQ74F-9Ow2gcmyAdYX4ZA0Av4UHG4qNKyUHmulyF3BMvdImeQA_o1C1lY5ahRZckHV6AZe8kLJIvlHK_TtYFId4crbAcpQcTDyK0schQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux3eS6L6AHUCWDttn8T8wkG_paXRTE6jPXki_GDkGYnWQ6Fz3oIP33ZJxJPOcCncQCtQrDAlu4tR1PoTctocqrEVOE_OTbZubJ-hiwboRGezeHtrBP55kjzYnh2YA_8O8gi4dyW0Gfm6CL7LTMJWh76l3lz5X9YEwCChdAB3GYHRrPis1aDQ60rKun7sMPHneY_VV3nX6aGw29NWy4BEV1UoQyaybJ12-wVG922-nwlXUspqVAukgx9cHCi7s1tFCr9wpkEBHADaxCf2jBVZMs5ezpgiiFtw_btGoEbfavlccj9hCBvTb22XqYaOAYkCRGW39LGmvDqiuvR1oAbp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=kNuLUe9jPn0PpYVfVz6kcPJORPaje1uXfraeUfjQ9gXReRLuC22vwrkVJz3OJvKCEoI-OhzXfwt6FKpOaH4iT0Q7KAtDtgFQRuFw7bvmAv-qKlQ8yf_i_k1lYe_UXuXIKi_i09j8R-T1YInTzyfeHliAzaOliEx2d4Gb0YFTD0Rs6f7WtfQCjiY_tePvISYfKYOUU-stnnQz_XX5kKdxKVSeHYy_SPOT9b-1zCam9dvbdPiFAyW8U-aEu_v4gpcpD3JvX-0RxoeuA-Qu9zbC7XjmT6WnV4imANtgokrKDxiKwq_pvu_3sI7WCU1Ail0Cvt36JtgqqBKVnwCz1nXHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=kNuLUe9jPn0PpYVfVz6kcPJORPaje1uXfraeUfjQ9gXReRLuC22vwrkVJz3OJvKCEoI-OhzXfwt6FKpOaH4iT0Q7KAtDtgFQRuFw7bvmAv-qKlQ8yf_i_k1lYe_UXuXIKi_i09j8R-T1YInTzyfeHliAzaOliEx2d4Gb0YFTD0Rs6f7WtfQCjiY_tePvISYfKYOUU-stnnQz_XX5kKdxKVSeHYy_SPOT9b-1zCam9dvbdPiFAyW8U-aEu_v4gpcpD3JvX-0RxoeuA-Qu9zbC7XjmT6WnV4imANtgokrKDxiKwq_pvu_3sI7WCU1Ail0Cvt36JtgqqBKVnwCz1nXHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkyYuj4c7OzbeKmr2LRZ4DdOQ2ZEvGZu_IPQ4uRn6nH__P5UfBaa7NIuYJBdDGMoKr-ypODvUyCiXbvypt7XsSOgX5icsD9PEnlmAjhUq16m0IMGKp2NDWEG6_zfaMSxuDxmHNAvFKBj3vzXDccNykQuBOufO4H9s8VbLOnb99508PDZblC0sIV1_UTBuSVRxXf7dJbQ3ixdEGsYens1UllEJ0ayICtQGtEPJs5q1_VfT8RR1V4ZjVCQ47EHnpsR6Xhf9uKqiESMVO1Up5wSSIjMRZDphZzJnadz2dWHvvbN5mE0MTlrTSVN3IkH-yqc4fHhFAptP6l3ICbml7ihrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=L2arzF7Q0fDwX0uLwYWvfavtScCFmPJeNkAlAFoJA-tKKceSVuic64ZXjmbMLRiqp6UiVNIH6qEGzpfFolSrf1aDPxzk6NV6LJgHtLdurtr1iryGmXXqFjTRez5OJNhIBEgQSQgmiiW7uFaMszFQgpfxyzD8g4PgxPw7Cl3edNV6Jln-Ozg0GFlviZ8M8DyG02Tdw0_t4r0WMJ3sreKY4Dvtmy9qHA-zCk1E8ZwPmisTQMNz6KsxFL6o4GFYfy5PL6I7RmGuNPf51596HfZZKuX5lTDPBvI_ge0gytnzkWoq_H4LKVAWrZnnWg78VHwZhYWvhdy_uN0BKdJ42GvJGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=L2arzF7Q0fDwX0uLwYWvfavtScCFmPJeNkAlAFoJA-tKKceSVuic64ZXjmbMLRiqp6UiVNIH6qEGzpfFolSrf1aDPxzk6NV6LJgHtLdurtr1iryGmXXqFjTRez5OJNhIBEgQSQgmiiW7uFaMszFQgpfxyzD8g4PgxPw7Cl3edNV6Jln-Ozg0GFlviZ8M8DyG02Tdw0_t4r0WMJ3sreKY4Dvtmy9qHA-zCk1E8ZwPmisTQMNz6KsxFL6o4GFYfy5PL6I7RmGuNPf51596HfZZKuX5lTDPBvI_ge0gytnzkWoq_H4LKVAWrZnnWg78VHwZhYWvhdy_uN0BKdJ42GvJGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=BicFT5kjBmYxSQu5S1mUTGBuiM3fO9BjN1ZbcOkEvFOCn1NjYiAtCprxbx1J3PzD3u6liTN3iHEdlYjl-xZwX8mWZVYPgu2flM6FZF5ZSp3v_ZnkNHxZ9wILFcErpvhZP9G5qWp9azg3S5sf9DFJ_QI1y33jIdzjDAlOp_U5S6M0f536BwPFFCN_lRU5lZFLZjANaBKtwRj31vocbaBJu2B1Bhi5ZPqlI9a5O-LIRYdL9PS-iyB7jyrVtZ0GE-jTGYK8wf534FSGwElSS2E-XIBeDRR0-MMivHSxV19hzxiH_jQ2EuoPE-yEGF7VIAvUw2zrX0fO6SOE3zAbFUMtpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=BicFT5kjBmYxSQu5S1mUTGBuiM3fO9BjN1ZbcOkEvFOCn1NjYiAtCprxbx1J3PzD3u6liTN3iHEdlYjl-xZwX8mWZVYPgu2flM6FZF5ZSp3v_ZnkNHxZ9wILFcErpvhZP9G5qWp9azg3S5sf9DFJ_QI1y33jIdzjDAlOp_U5S6M0f536BwPFFCN_lRU5lZFLZjANaBKtwRj31vocbaBJu2B1Bhi5ZPqlI9a5O-LIRYdL9PS-iyB7jyrVtZ0GE-jTGYK8wf534FSGwElSS2E-XIBeDRR0-MMivHSxV19hzxiH_jQ2EuoPE-yEGF7VIAvUw2zrX0fO6SOE3zAbFUMtpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRnKoOjvvRCuep-6pezzYS-5uUZy958oHSYkSUjgq5vRcfvtAnuHZLF5cTOiekpoHlZRQIJcJHE9yOLGwWLZ4_0UQJYj57PafZyrhCait9I1oXjxEsfvDFQfh5ZR14D0PHWbZVVAAbXgZDzE9bZ_qr2e6_7sGiODiwGkF5jebYehhoWs3S29nzUqvVHUxzDMjMedPvaJ8H43DMvNCSb57XZcgTg27NqiWD6qeci84mTFh_dt5iAB8WDO3TpwfkvYOj_YikTzLmGUNPsL6QVaf-VBB2snOQid1-BW9Sp2AuaJOt_MFXkJ1_ANyF4SfVXSEA7sf-o6HyHWb9ASRuIXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=KlLNOZ6_TeNTwz9VSevr14tc6KNES0Q9Tdf3K9Q4Tu2kC8EmDnKQK2mmSzlw69OVZGpHidqynSjDHDZtHwtkH0A627KvwuF_DG-HnJtlC-IE8e-8nFJl6_JFYZDBA5ySgNHpkqs81zLidjTbCGO4UAblEIOQpCsH7x_nLRm7SJzD64IJ-qcTgN83baPsLGXSFP9f6JDwqPONlE5mn7k9rk1boBdRRRsWWcuV3IJn7wprSGM6rYTCOLSY1c-Q3GH4MeRz4s1QjPLJqM2KRq2Fcn_egxVuUGQhqJp5OG7g0KsVcSwL4HUTOWbe38GenWBCe2WYweRc8_9TKdKGZ7mxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=KlLNOZ6_TeNTwz9VSevr14tc6KNES0Q9Tdf3K9Q4Tu2kC8EmDnKQK2mmSzlw69OVZGpHidqynSjDHDZtHwtkH0A627KvwuF_DG-HnJtlC-IE8e-8nFJl6_JFYZDBA5ySgNHpkqs81zLidjTbCGO4UAblEIOQpCsH7x_nLRm7SJzD64IJ-qcTgN83baPsLGXSFP9f6JDwqPONlE5mn7k9rk1boBdRRRsWWcuV3IJn7wprSGM6rYTCOLSY1c-Q3GH4MeRz4s1QjPLJqM2KRq2Fcn_egxVuUGQhqJp5OG7g0KsVcSwL4HUTOWbe38GenWBCe2WYweRc8_9TKdKGZ7mxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Wrf3ChCItGqfiLPxHxkmKEaglyLBkgm9HdYkoP_VWg2efF9DA3Hq1k1nQ__sCsWWB9F4ILOJbeKHEjocUDG5LEqoVrv4Wu721l7W0EUXcJ3bS4xI10ZgrcSoAbDKoeTztSkfkVFtZ3k4_LR4d9BUeaY3Ck6nhMpFXSJeZyw_HYUlptUNgKybYLhRJ7KoLQF7m6VWkpoqspcH0NolJbSwyXzFJVSZTVhX7Yqtr6Q9Ko3su3y1r-ubfVdRBJkWLgVQvQ33ycGZRps0jO3rrlehKjO5oe0t_tZJFYZkqBRGCvCRSwaHHjnIe6YJYb_qebdk6D3XlaSWosd_DSQneGCZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Wrf3ChCItGqfiLPxHxkmKEaglyLBkgm9HdYkoP_VWg2efF9DA3Hq1k1nQ__sCsWWB9F4ILOJbeKHEjocUDG5LEqoVrv4Wu721l7W0EUXcJ3bS4xI10ZgrcSoAbDKoeTztSkfkVFtZ3k4_LR4d9BUeaY3Ck6nhMpFXSJeZyw_HYUlptUNgKybYLhRJ7KoLQF7m6VWkpoqspcH0NolJbSwyXzFJVSZTVhX7Yqtr6Q9Ko3su3y1r-ubfVdRBJkWLgVQvQ33ycGZRps0jO3rrlehKjO5oe0t_tZJFYZkqBRGCvCRSwaHHjnIe6YJYb_qebdk6D3XlaSWosd_DSQneGCZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5llyEZvgyQcHlcNXQ6h8pC7nhNv4LMQ-BblmKru2pjng4A6OLx3YDmJzIWSDzH6O1sRX-TemDLywJYQNpqMc98cQJcPj0s2lOuMOfp2T_vmLQ25G6Zj7mnlgXH7aNiAL-PSUnVwGkojyJqdfCrF9qtDtjU31uQufRLGqr5aWl8Ny9zyMPGg3qdw51_blWA8giVHc9Rv7s1KoRhsXGbYSctN3ThU3f8-fF8FTCWSf_KCyunIvGlYAdl_T2NChDNtIlICzLMoOqHKmnlBTUurA60CJ_fLVZfFvTWeihJ5rm6Smij1MVAYedZfNwyVy9JEQpLh4T6Ydb4owP8Xv9_Chw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqCyN0_l0GX5Yqf1UUe-6sBo14v_bIhQDs7x8FnoQduT1e2CfGkKvSLa_uM_ml0ukwpFfeLe-g-sAZSxgoB-E-8RiM0r7PvRhQOzOCceoCYcNQAYeWcrZaGPIU5aBtnPcsCFLf9QWKEZWZBfoXDTE-0rbZ1_j_txH317ZGFbUVYNNbF7rKfV5r-ZkUSPKp4jawuRqQ1ze4qvaY_kXETz_k-gMtSaxQ5HQYOInneMCykaX0Zc-fB670_5KevI3cPly4JtsaF1FFBP26hKTYiUcBDP9tIp3kYGqt_f_ddypm7b2bONLUtZwPqHfntMFYT8iEp-Pivo7cYT_cPWYILnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gszNDiGYyNojMPT-ykU6bzH8YBQAyJl8fNShCgFx-P7_1B_bIoJMSYX2e-M7HzW_7EjCD_Wl0CiwYRvyRF5KwiSWtd12xr3Y-umsyRyNu05FnDKb5dklcZvHnT9N6W1gj_NO93FZmfLGVJfKUyDZLMgRAQ_MshOecEyKifw4k5_A7N05xXLLVPQFh-rIZzxJdRo2LHlYVtQWXTQcnO72eH7DCceoKJohJk0w4B_PVgRaApABOEwxgSCLFV-sSQ8rOzcuogY9T2YeSBDqzqMclkCEgGfVmBAKoK7MbkwWvI4N6wPYH5VzNvjWFximihy3_fT_dugqH4Sp69uuTqHCGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izwzOP8Sg3VNVyegD-7ygIJqZ0epEU_qTr3xWCmjw9j7CmvuLFiJQlvz5zGJMCbfwKyf5JRmqU9iQfL0-BVub923VvUr7vziuYbmuxhrpcZl9CfkoBgjUKonF1FNdbogifAvqbbsm0n8qnGMMcCtFkrVc30liVgLkQqsFYqt1F8Mh1WmY2v8HyYmQQyfAzZzjxCnlI4QcEivl9l-LirhBTybHNyAFfDk6pXNskit6zBdDC5SSMRhrcvI0WzekvQih6fpv4NwnQaekvPhVoot-DhFhZDekq2EckPL4F1F24xuK_P7hl4JfQRwp5-bDpKtuaYuNmM26DHCzK6jAUvwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=Lwj2AtbUOGVo_nDZkFvzxWIBsEvRbijX2e84d5xeIZ4v2qr2cOr1p-YCoaHmCVvir5lPKEdzBvO3Z-YNLA0kI_SO4Zvdo9SKpN8zLQtXB57252HOCyQoazolVajHq_dofqo-OWFkTkBTmQZj06WWBkd18piMXy0nzT_MLQrm0s85o3hiqb_sBpXSWtEMCPcLC7dQFs7Ohub2VVGS8lfEMYUkRBSwkQcV7XZFBXGy0ysMY_1oXCmqRgTt0rgv2ZF3GtNPNECbizl0hsrEXuSxocuKZT5_eM1tpBwvVczrrxfIOj4BiacE8Xyuew7komvGsf-RRWOZO_u4ir9h_UfFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=Lwj2AtbUOGVo_nDZkFvzxWIBsEvRbijX2e84d5xeIZ4v2qr2cOr1p-YCoaHmCVvir5lPKEdzBvO3Z-YNLA0kI_SO4Zvdo9SKpN8zLQtXB57252HOCyQoazolVajHq_dofqo-OWFkTkBTmQZj06WWBkd18piMXy0nzT_MLQrm0s85o3hiqb_sBpXSWtEMCPcLC7dQFs7Ohub2VVGS8lfEMYUkRBSwkQcV7XZFBXGy0ysMY_1oXCmqRgTt0rgv2ZF3GtNPNECbizl0hsrEXuSxocuKZT5_eM1tpBwvVczrrxfIOj4BiacE8Xyuew7komvGsf-RRWOZO_u4ir9h_UfFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftSII9OFCLU2JulXPpST3oqttTEnDOfEjaHDljfm_H8eA4IAL1y6B7rvndVT8P5y1SwD-C7PJTmwd60GZHBJkrp1efJf0WlnkLmOAnoEP7AGvN3GDtGCKUIVSMAlhfnrQusjttmq-YpvEvD_T_6uGD0skbX5ltcZoAKM96IoOFkTr2lFD77VHRywGHXTA6jPZmEDv54ZDXo0THwZhfD8XWmnbQQkrMIZGQb2GnaMqjyGJJaxt4fNMUuz7Do2RfMrV0sW7yZj1Gc4XnGgeizG7V71647BNxLTrGERIM_5D8iRj7ld0yD-khj9rDTT7XkUzhMfmup_hhfy99tD6Ud7L6nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftSII9OFCLU2JulXPpST3oqttTEnDOfEjaHDljfm_H8eA4IAL1y6B7rvndVT8P5y1SwD-C7PJTmwd60GZHBJkrp1efJf0WlnkLmOAnoEP7AGvN3GDtGCKUIVSMAlhfnrQusjttmq-YpvEvD_T_6uGD0skbX5ltcZoAKM96IoOFkTr2lFD77VHRywGHXTA6jPZmEDv54ZDXo0THwZhfD8XWmnbQQkrMIZGQb2GnaMqjyGJJaxt4fNMUuz7Do2RfMrV0sW7yZj1Gc4XnGgeizG7V71647BNxLTrGERIM_5D8iRj7ld0yD-khj9rDTT7XkUzhMfmup_hhfy99tD6Ud7L6nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhbFEngk_rVTHSNgqSNN7_aI1PyC8Ej-FnvZLTZ4RWfmI-hPdCGZ6tmBz7mcD_GLLL-Pig8HsiC1Vf_OUfClfBDkT44K87-XMOw8jHkQ5SB2g6AIbLMZI-hXhxbWK4Sia7Egwo3ENo-IgJChvLVWF1ZS3QzJkycOijPb08SksGrUcwWA-6zikdh0wrr1M8AVIc2CphSJBrETy6iT3VYIwnoxGLwWuEmQC_NQNP1qKM0LlKwxS50cIWNgcShit_TvR3IhyFaEW4nonu1YTJihyJf4VZiV4mMTFXSRf8PvrnOng05pRJa1orb12SkFGqO6KLTAJUoeEiGxfn13aA7abQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwWf6A82nBYox_FrcacjS7CVAVsGYXscNXTCUIk3I2oen3EMZEjXdBN_C0oii4dWLFubz644mEl6g2FG9Rc7OakNfI9gtb6GnvFyomDJ98ur6m33Hxo055ckIQTQTDD9P0OGyU8BNabyeTzoZ0aceVD0-NUs8UZ07EJtwzreNjw_Mm3A28L--TzAmh6_l9jXrbb2njBIcrN_OS9Fj0qmJkaj_CIN-y1Ise1jyWz74rKvTKpRslYIc1z5S7dWVqZQKeALvVjyCTCy5TjBpeH8OhmnEc7yGrw0LVbOZLymwEMMWWk9sBnGpqVhT7bRYE19s2FUrmtHThE8rV0Iov7qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZtDEzQ1QAlTqbGfXKVNVF7VGDxdA43cF24FyzTGzjQ65wvjOCypWDhUgriitwlgOpMVIw5od85w6p5lIwt3F_o8jF47vR9KWxR4Vipl-nYpp0ICqVPf5oWWDpgPSfle8K7i9LcuOoKZTln3-EnSjMcvhqJoc9fgT5ZrsmL4yM636mv2rULxBS2-8LNfApChVdiErB7foesXCwV0m--stM801uDNo3r04_kk2TDHCNKqH-6G7mcMIomd62h8_9KKcQwWGSofNJ8V3wGL6SX2pxSR3Yf7FkgaAjbxz2VF-CYgxefTMixGeFPj3pFS_RzuiYBPzHU0VoDjWkSpOO3V9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJq1VR-bKMuKjmx5JGzmgKd0TBfxTLtkvPt3oKZzWEL0H5HxIAc-ePn_HpU7vaSUB524Pnd3V4GbhfqlSBEjGMxC--FL1SHM6X73rl29ABacrGuG3XxPJjWGtNlAU8IqbstljrwPbME4jTuIa5fwYS6s-IFlpJ3eWJ9KJWvzrHgMidVlclI7x6Ai-mqwTOCe5IQV1aus6JEZjj2f6NLn_ZEA3t8oFWjbA3pjL-s5q4PQW08cTA8KMXWopOKJygcKhYhDbBkhMV0iYW4wGNcRJ5o-DYAh9EGLEyMqwkF7aFxrMkb7hY9pmONGKgn9yacKzuQ40OtbhDc7J26N41A22g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIpUXmjYmFN81RneONZCPS2azZg9Hrgs3ab8T0jcL2bwR2s2O3reMqQL_ZpMwUra6S-q2Z0Rx_yTJ4GqM4hKoQPieQ00DKIIqKR-6YfrC0YhOmxAWs5-96xuEAwOMEQRahdRYC2HonTdoBLkV0Gkmv4rBjGwu9_y4W0RgjGw4ilQyJ6kEPgIEdISOy6gUTf8Q_wAUGFlYSd_s8lRMww-dVlFJykGd5KM5DlK7f7NZnNllK-V03PAiAhqdzpdh7KUFNkcmT71Wctue7q7K53bC03J0xf7jWVoq2nLbNgC2FhG5ZPcyutEkoPsk4tPEIJCLB9luJ7RfGhtm_jUPfnk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=Wj3Hhh105LHymzAsJOm1zFOdsS7A0_cfxSCCpfH1vEV9r3LgAJdk2vGLouWB_9jD1hFV1xgVUyC7WGxkxDGzoHRe0gyURbU2CrUu9pGe1Ri_kFM7v_KriIDg0h90yuFcazA6Nbaald9eEnytlAlm2lRK91xHo2JcUUjy8vEmHalc5Kg0QHAAMOmt2SrLbM6TuckOYBaTLqC6jW9CThRQ7wtR31wHbcTVKiJxJznrsUeH0mBlB5GpPN5ygHpm6UimjmXBFBcCDL5irJWGyi87LL-x4YfvS9jhf78msjm7QS_m0h11-mefapu4ZdZEZXSYwnZNLn7MSrMAucXhcyEg_m-u3q1K_99xEM-Ij_J96pkB8N796nQKr4ie108NQo5PGSUI7XIYUFZqSu6HYIL2AvLy2c1KrRRnFhgJIBZm9xw4bUo1zmAbvyChsUJTO02F0KcNCHniw27nIu1z6wNbZkWzZJWJrDG0Zv9i2_OQjij2peYP2U-A6U838v3xvyxbeB79OAnzRVxtEKopJYVAS52LRg7etM8gdsAkZSweE0c45Cc4qTJlOe2EE2P16-YLeYKzOjc4Otqc1fhHvV4ff6hpYNl0k5M02ea3XJcN5pefrQRlRjy3RqIGK-mcchr1jsrlW7acD7QnVkqL4up4xl2J5ABtw83MApn9h0pNNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=Wj3Hhh105LHymzAsJOm1zFOdsS7A0_cfxSCCpfH1vEV9r3LgAJdk2vGLouWB_9jD1hFV1xgVUyC7WGxkxDGzoHRe0gyURbU2CrUu9pGe1Ri_kFM7v_KriIDg0h90yuFcazA6Nbaald9eEnytlAlm2lRK91xHo2JcUUjy8vEmHalc5Kg0QHAAMOmt2SrLbM6TuckOYBaTLqC6jW9CThRQ7wtR31wHbcTVKiJxJznrsUeH0mBlB5GpPN5ygHpm6UimjmXBFBcCDL5irJWGyi87LL-x4YfvS9jhf78msjm7QS_m0h11-mefapu4ZdZEZXSYwnZNLn7MSrMAucXhcyEg_m-u3q1K_99xEM-Ij_J96pkB8N796nQKr4ie108NQo5PGSUI7XIYUFZqSu6HYIL2AvLy2c1KrRRnFhgJIBZm9xw4bUo1zmAbvyChsUJTO02F0KcNCHniw27nIu1z6wNbZkWzZJWJrDG0Zv9i2_OQjij2peYP2U-A6U838v3xvyxbeB79OAnzRVxtEKopJYVAS52LRg7etM8gdsAkZSweE0c45Cc4qTJlOe2EE2P16-YLeYKzOjc4Otqc1fhHvV4ff6hpYNl0k5M02ea3XJcN5pefrQRlRjy3RqIGK-mcchr1jsrlW7acD7QnVkqL4up4xl2J5ABtw83MApn9h0pNNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJgErKYVmkMNxM_Xy08pH8JgDgXNluLXP3_G1ddIUxC-g8JAvNHQ7p4YKwneAJj_0oQ0AF7d294p2Lq-SyUGCgCgRCIIpXXLKHB8aKTQoZVixRP4GI0mgsfdD5EQkfMCHbbyStc4FfmIvrdQgRGG-Ll68CVT3KTZ3QlaMlDiyrYVql2UfEWpDIrtpYONrJ9Eix6nJEaK2u4wqquLPM32y5t9A7EHdNVRQCJnZmyl21xUKfNm39ClpPrSjvdsuP2sHqNUzhRdSE0Gq7MqLxpZYP6Y1dJzyiqDmvXdLjdvMh5iV6Y-3uT1vm80-ZjlYOVMFY8RJkrstexlzK48GnRNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=SsJS-KyQ5BKNiAjvMRsJW1GfxGtyUGWy1LUr9bXQF8PfFpt9qdqHgc3bf6fgY_vVAQtxtzX4uynZsVyIeYWNdbifzWXbVpsFNVVkTx9hlqI3rEU5Af2FNJHHoE6VkgPueOBe4npJDYM6kgrTz729gGBXEHZMK9OBI59zlrKM8XP70whpULQ7hP5LgUbe5wl_ML_fw1Ufxg-NIX5HzC-uZ_l8Qi4rGShFqr_3odC40CtzKk3txuuT_6tfLpwYGEYUhLhhOw0hp6jxYkZ3WJaAQw3I0iJXd8KyBQGPixORjPcwqiPZlGbKiIUm8L3MQOpSDtHwl49T2s6QbLmIAj1B9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=SsJS-KyQ5BKNiAjvMRsJW1GfxGtyUGWy1LUr9bXQF8PfFpt9qdqHgc3bf6fgY_vVAQtxtzX4uynZsVyIeYWNdbifzWXbVpsFNVVkTx9hlqI3rEU5Af2FNJHHoE6VkgPueOBe4npJDYM6kgrTz729gGBXEHZMK9OBI59zlrKM8XP70whpULQ7hP5LgUbe5wl_ML_fw1Ufxg-NIX5HzC-uZ_l8Qi4rGShFqr_3odC40CtzKk3txuuT_6tfLpwYGEYUhLhhOw0hp6jxYkZ3WJaAQw3I0iJXd8KyBQGPixORjPcwqiPZlGbKiIUm8L3MQOpSDtHwl49T2s6QbLmIAj1B9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=p6vlYFbj_0DpALntm0aHIHqEcNN19qsUp5mqyeafB-BJ4M_PQVjTULLi0_RlHnoovmP57VOq0LpbkB920ATyjxYY9AE06tUtT0BuXklQiMxPRMEyFFCcMcRBYvCkz8HkJP7fN5Fi1fQy9ksbSYEeb1eOGDl2eaievNtGyvpkEACT0JLCBkmq5XvR5gWRO3IIlh6MA6QSvItBpE91zp2XTQbvAcpIpEG6zCJCG38DQuTx8-x8mbWp-Rnb1-JcWpVCfPDQprn9_n5NEzr4D5MWCCzqyOlvyBZZ-43e6a1AphpCeDlLHDJmyUqhWdmqbpSdpo1GcIAxcGJ5VLMMn62nhVbpPtjC9pN5b90j3zDg2gLaTmW38TvaBt6A2JZ0ruUCoK6-vEF_bGbS4OuSJt4z2PMRZweMUFx41hHS8GF-sFAHqBJtov1DiUcq1Z9eOsotLczSRXMYaJSLW3CACIi-gWxEnJvXe-juQK_-w9dHse8djj_m3f7T0-WgFajz_iYAXq7GtKZJCvIBuAkCNUNaI3qRvtSPmidKqbTP0wkq5ypcs-W3rS2fnDbbV2cWureoFKCvzFgR13ny3INJNlVIS-RaVaEptCPCWWS1E6v2y1hkxtnNFltJ3vKvm-vQ4p1HTsb7mgGyrEYMcrIOpObI-6_DKkQKyI6SXzWvBw4qG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=p6vlYFbj_0DpALntm0aHIHqEcNN19qsUp5mqyeafB-BJ4M_PQVjTULLi0_RlHnoovmP57VOq0LpbkB920ATyjxYY9AE06tUtT0BuXklQiMxPRMEyFFCcMcRBYvCkz8HkJP7fN5Fi1fQy9ksbSYEeb1eOGDl2eaievNtGyvpkEACT0JLCBkmq5XvR5gWRO3IIlh6MA6QSvItBpE91zp2XTQbvAcpIpEG6zCJCG38DQuTx8-x8mbWp-Rnb1-JcWpVCfPDQprn9_n5NEzr4D5MWCCzqyOlvyBZZ-43e6a1AphpCeDlLHDJmyUqhWdmqbpSdpo1GcIAxcGJ5VLMMn62nhVbpPtjC9pN5b90j3zDg2gLaTmW38TvaBt6A2JZ0ruUCoK6-vEF_bGbS4OuSJt4z2PMRZweMUFx41hHS8GF-sFAHqBJtov1DiUcq1Z9eOsotLczSRXMYaJSLW3CACIi-gWxEnJvXe-juQK_-w9dHse8djj_m3f7T0-WgFajz_iYAXq7GtKZJCvIBuAkCNUNaI3qRvtSPmidKqbTP0wkq5ypcs-W3rS2fnDbbV2cWureoFKCvzFgR13ny3INJNlVIS-RaVaEptCPCWWS1E6v2y1hkxtnNFltJ3vKvm-vQ4p1HTsb7mgGyrEYMcrIOpObI-6_DKkQKyI6SXzWvBw4qG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=ZkPB_t54cBd9WP7IercOkKN-7xuSPkGy76VjxdwqIZoNXBYhNrA0fqL0JsXN7kZPD0tfnVAVaItZ0s8M5gP9Ek__7IgXNxGAao9xY8k1QfmGmTRYL6QG6fZtDlfZRYqylZbqxuc806PjKEuJD9JCstgOed2ttEHzk8ePGInIlp2YznBopYz2i23oWWLd9ZYTwXmnR_GopOPPWUWiv6ceYMrAZpxIi-7C-zam18WuZB7ZkNvxV6-4dAAb1SRjmk1paATqR1d-GN5132VUzmJwqK8GO6M0m2ZpzpOLAArINSnAVEeOGqlzZl_hImzbTaFrxhdT8WgnpoaYrYezrmuw_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=ZkPB_t54cBd9WP7IercOkKN-7xuSPkGy76VjxdwqIZoNXBYhNrA0fqL0JsXN7kZPD0tfnVAVaItZ0s8M5gP9Ek__7IgXNxGAao9xY8k1QfmGmTRYL6QG6fZtDlfZRYqylZbqxuc806PjKEuJD9JCstgOed2ttEHzk8ePGInIlp2YznBopYz2i23oWWLd9ZYTwXmnR_GopOPPWUWiv6ceYMrAZpxIi-7C-zam18WuZB7ZkNvxV6-4dAAb1SRjmk1paATqR1d-GN5132VUzmJwqK8GO6M0m2ZpzpOLAArINSnAVEeOGqlzZl_hImzbTaFrxhdT8WgnpoaYrYezrmuw_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7TQKSxF3aLgV9_-DN0oRtkSsaU675tja7wq5NRarP_HOA1XmAKMok6eq2K0qkSEzhkbtZf0RO8oAcX-n66grcL0REC8e8BwZM8iCsjat20DUtp4W3Zf8kHEHef9oRMm_KOAwx2cRL_M_YhBaLFons3sc5N1Xh--8b-QqzBA11me-ibxvuvhbYt-Dn5Ig-XDcv0R526hYESTasMyHJVyBtsJGP1UQEv-6L0yHMPzu845p4M3qrfbcE6ho_7QR3OfIN3fC27qyw-DbcUtIBOc23bPBY8a5rrBZ5CJaNWn7LIIHoaxxdlOyrFxg-hVrWdco7qydBf85TJpIv4xVYAgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHLRD_6eTXJl7YRptPx2A8kFUUHKP1YH-r7WGn2KJ2bTMe66g1JGD5CYpNdlkkoXc3sTC2NqfPutMwp7Ea-vodkZ5DDKINPbSHUfcRjnJ4w8JI75S8pOSSzewsDjYE9CyMLUIBltI5NkR-R2SiYUtSUGWj1ZBUr15VR2wM5SPYrAxme_uwjvXena2sFhalqcE4Gr8qP-ZSWx3zYafnxRfGE_FLAUdOIVc3cntkly3fuMP5LlHNFhQJ1XLEbr-B4lUpGkw3hmTE8zMEUzXNWZHqo7s-1oDJpe8LlIdTISaG7OqxD31PF649fGvp6F7e-uvTJmUHS7rvPHPDe-wr0pwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kic7Y3A-HbKKnxavf0IhFHEq8FiFINjVghVEaeQTd5__P2LmoreNUL9JY793JvK9m0WAasneh9JHHH27_mAQIESTbnt_W0l0b5N1V8fdsplihw7230bDQbTyF73_458byhpoaZlB2BDIctG0hcqipfkIOJDS-OzRrU10cwIRhyJvGQ3cRFmDshtcXdALrD6cOxyUCDVQPiFh2J2YeiXOWb_FfmbZ4Lmu7DBZHqZw5LMpZY-BRULIK85D-8ZMBfBhBO3VpCZIUOtX5_pVCJJRmiPiiTYtDRt1de54fLHj8fPmEQko1Tb9uCafMgCPiAQV_KAEqxOWfI4Y4SSXv0lXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQZqMERGR_0KF7w8cmskhrXguQhj93Pl6asB3kHmryPbQeqDcvlkmB-GmR9VlYxRnPlcPq-cK1o9er2STytVid3HGtu8QrSELxpwR4M37W4jALUJhf8yyBFwL8lQlzEo243UfOBJ5QsNZUVvbn2YZz-Ryp-eOYw2SIA_engcyX7LBChJoQAf6Z8TAcSVmRoOsmQA87g8aWrlqfESH9IjU6LiNKCD_nkrNdpSSMsnITsnAddHIYoHbFkS3xaD54We2GLMoW6p4GZG6HdjrvzImp4-7ll3JVkimGR8jtBVX5zQtxu7gXM2zppAfdvfwIHy005OHJQT1gA2W0D222XINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz17ZuDDi0eD7sQxGpqRW5m9TxqKGamLRulhlqSWxvNh3ZCPtafEL7hDue144DJU4nvkYDFQHDxrzC6KsISrsMe8_fX1kFfVI-wXOnbpE4sPHP7sEqx7rMCS-NyltsqVHzqc7wqsgo-CcMGNBdXkZHf90cxeQNakX1w99pEgZVFcvpuox6avGIENboA5fcVq772A4BchfstF3eUJyaIBwr5TJsuShum6PXIIKjo8h3ZO_DuHQEom6eue38Q2BpOpK3agK_AYz-YrDe3cHvl8KWzJzgHRHz_RaaTIzmUj-gtxR6K_cICT26aFdxngiJVlTGr3O5TQL1aEsLHfp3v3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=lNjHVYP-KCo5DAMXfAN6RdtoSRXyCU_V-tiJqprL3iQ49ZlMWIZxh9izDj2d6GWK3vGDdMEAnFuZny2wpWTvYTfGQw_nFp38WLYsxtLg2r-qc78b_-MrLgRmXlhLVvhwvgz9Llzf9jwa4Yd1HBekDxh7Fiudi5pK5Jnz8eZHj5KeywOO-fhA-BqjPJ3ZErDWiyJ5bloOXguCHe77gTEdoAlgBWzVj2wHfz4unT29OQG34Yh7DE5kqvRrfwFY20FZtRjgSL6TkFZgWG046DdQFErOp15JY_faxzjH9GwPgiAVaE2LeryxV3LK9678eXB0dF6CXwefJ1QATxc8bggO2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=lNjHVYP-KCo5DAMXfAN6RdtoSRXyCU_V-tiJqprL3iQ49ZlMWIZxh9izDj2d6GWK3vGDdMEAnFuZny2wpWTvYTfGQw_nFp38WLYsxtLg2r-qc78b_-MrLgRmXlhLVvhwvgz9Llzf9jwa4Yd1HBekDxh7Fiudi5pK5Jnz8eZHj5KeywOO-fhA-BqjPJ3ZErDWiyJ5bloOXguCHe77gTEdoAlgBWzVj2wHfz4unT29OQG34Yh7DE5kqvRrfwFY20FZtRjgSL6TkFZgWG046DdQFErOp15JY_faxzjH9GwPgiAVaE2LeryxV3LK9678eXB0dF6CXwefJ1QATxc8bggO2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsVeu1B7mkmrX_cJeADX0F560Mv9gIm1NXywlT3GjsuhK3i94I6SC_4ehjaBQSs2O_CoUY8DvW994wgjGYGT3xPVijX99f2d4r7TEk0ynapG5dSm-n35MdZ6pTy2ve61V2r4N4FoHYYtqYOHI7yUv5XV_K7NqeP_IMWA6oHIdJMpPdJQkmO0aqFW7h-K-4nICLNp9DzRYsWKynsGHmK3R10wtAySJbSCh5ayZE50kjINP6W3WU5CzkR0QWQqjZyUhR-K9BLP1r8I-pdcGbfs64JRbOz8HYvYYsMyZSLiAQmTLpw5ECKyvTqOguKOq_TMMr0sOZJ4D-IjCgW7LNSL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiHpkfeHBOXYYMRO5XT2wnk0_JxyAmJ63iNCWWl4t-LBehF-VfzICrI-7aZv-CK3FdqEvhfJkE_NlrVH1om9esKrDt4mKRDV_z7oKHnVVJCzTm3FxqPiqsiW5cvH-dbPPu5pRhTUzgMijO9PV9vjZp9afsSmrCCVJEb6FXEa12aYtxSuDOz4mk2ug67ODqVgOONl0UcxdXikLawWFmxsK-nQ5Kf1DSReTJ-qz4p1zPolMOyhznTTPOzjnxt8Tt7WAhL9CfOSXjDKBtfc0rmJrYapClwBSBi8tgZJ3jdRCB8mTLY29c8sWtzoDcIz1cUOMnpYGmRlE5-6dKieRMGXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
