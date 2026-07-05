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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 09:00:04</div>
<hr>

<div class="tg-post" id="msg-666804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf4ob46WLyIQY5a1GUudcoIJwLW_aRfKcd_IldcMZggbOgt33y2G1eHKHZPyqkjktjYudV9Jn1DSAhm66xdE2xtSQWhnKvPgySNbHlJrlydlBEPffvAZTdBDJ9c86rea4JQ7HoPUU9LpS7ahUrZytAKAmUkcuNj55_KZ9NnSXwWGiC0BO9-Pkv7Em3XmameEr7EDIUnATrD1aCfbre-e52rVP2_IndnPH2vTX60i2-8oPNesMnZVGltEzJiJ_ZGv7rTLKOg5TXwWxrFwKTk1_cgF_Ufd6LBqFMMp2LOEeJ7VobEVabI-bMpEBkIZeaEJoz1BPt9k-b9vSb_60ti4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون| تصویری از خیابان‌های اطراف مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/666804" target="_blank">📅 08:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5fxf3L9gBXECNkEg_31pwxXRmw165OQw41sdo8DKsXAMDTmNLn8nCZva-UMuSpgaKjoJRMLzEMRzD558MMY0YgioenmKSuof9sSAWdgqULVEamCDLIdUScjN_M5BDYxj5GLZKODFcAF2GSo7n6oDPotCP3UxnBYkIkz0aUfSRnGdWebN-3RZeujs202w4QQFv7x2Q3wUvo321k0j31lPnB-3vFJdiNrtq4Kvgs5IYfi0ttGLyfgLVUfW6klucyhUdDLiVqGX0gmbG_6Q8smyriIZdmzjsnlyJ_RxfbiF5qrCsJyrlQ3V1K_8Ino-Pj5z_1Xa7faM8IoRNlpPlqJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد‌ یکی از شرکت‌کنندگان در مراسم وداع با رهبر شهید: « اماما؛ پس از شهادتت، ما هم خانواده شهید شدیم»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/666803" target="_blank">📅 08:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=kd8X-TYEYnLsLPFx-n2YRFosZkUIJDLkh5SAvBQH3C5qh8ZZyu2REnDswTVBrRlxAetSkhjA6uEiYN4TBhrZymJw_EN8ka4KwuRzSiiU0sD6k1pF2Va1U8yEDjgXFdRSIBWfp610zXy2C-qL_jnuwBqwKIC8jNc-FfqewozqjjHDYKfdam25ULohRNB_5v_ODiMyjFna2OMtR5GCLeR61NAaOJFvm9OrTKb2bbmbzYMza4wAV15l6nNR62xNHEa73mgW6MYti25ySWuU_rj8jiFBTkD9pP3-w-ANCdyEM2gQBv61Z1wzdIKrMWV08qOuFkUzlgyHKV8LX0g-iUw6VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=kd8X-TYEYnLsLPFx-n2YRFosZkUIJDLkh5SAvBQH3C5qh8ZZyu2REnDswTVBrRlxAetSkhjA6uEiYN4TBhrZymJw_EN8ka4KwuRzSiiU0sD6k1pF2Va1U8yEDjgXFdRSIBWfp610zXy2C-qL_jnuwBqwKIC8jNc-FfqewozqjjHDYKfdam25ULohRNB_5v_ODiMyjFna2OMtR5GCLeR61NAaOJFvm9OrTKb2bbmbzYMza4wAV15l6nNR62xNHEa73mgW6MYti25ySWuU_rj8jiFBTkD9pP3-w-ANCdyEM2gQBv61Z1wzdIKrMWV08qOuFkUzlgyHKV8LX0g-iUw6VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای غیور ما، سید علی صبور ما، خدانگهدار
🔹
لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666802" target="_blank">📅 08:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHR-cPM-GRMorHgimJb1oP0fNWhwK2GFtVL7lAHNrTkvNDSsVev9ISNXZ9l_ygo6Yu1KSR1cqeqglLZK7Q-Fp81HGHOYk3WU31Et9-q1sla9ig_Fda-qEZ0zohXt67FjfyDcgLg5H775ycmgPcuPIOiWiw0MkXfR1rn7peVuUobcOyPfFdBEBnapM5__RV-NEHKbQ-Y45fF6-5yOXsXHMZ1NhPQqcqjTwZ85S5Jlse4HTe78Ta45VbPXhspqf7m_qDHMhD88WlbQnUWySxeoSZrTcCTV48KY4NVoX4WODNoI7YDXwismwiQTslSgMHfVpHddtwCw6Bu34k2vvxtXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد سوئدی: ترور رهبر عالی ایران، حکومت این کشور را قدرتمندتر کرده است
آشوک سواین، استاد دانشگاه اوپسالایِ سوئد:
🔹
انتظار می‌رود نمایندگان بیش از ۱۰۰ کشور و ۲۰ میلیون ایرانی در مراسم تشییع پیکر رهبر عالی ایران شرکت کنند.
🔹
ترور غیرقانونی رهبر ایران توسط نتانیاهو و ترامپ، ایران را به یک قدرت بزرگ و حکومت ایران را قدرتمندتر و مشروع‌تر از همیشه کرده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/666801" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfubpvhAs62rMh1gNsCfmZQw6qkFxBekm7iPXU_rUKojTs6wD3KOXpD7tx6r9Irl4jyl5-9hPM1kRnhhjIn05mIzY8ImTi3eEBBy9A5NNSV148U97sOBB8odspenpMS9dN-fjH4ypi_1evARHFDhk0ISbFH5lBvgYB_abAeOz1sVnLQL4L5uco4C3m-tVC_jmWHwP5894yI6nB3TceC1tIS9ups25wgXloZ6ZflGh9mqO-TJLFzh3IYBgU3WTWhBneu6iynFJ6GvIBKZe8wlfOkaV0S1_OVcypWjqszuHAuePUBZksVcqxkRkH2MiKaCQOUwmuFNTBDZAxo8gCObRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلویزیون عربی: خیابان‌های اطراف مصلی نیز مملو از جمعیت است
🔹
جمعیت امروز بیشتر از دیروز است؛ خیابان‌های اطراف مصلی مملو از عزاداران شده که با شعار و پلاکارد خواستار انتقام خون رهبر شهید هستند.
🔹
پرچم‌های سرخ و محور مقاومت در کنار تجدید بیعت با انقلاب و رهبر جدید دیده می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/666799" target="_blank">📅 08:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666794">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-zqWwUVQQB9jzjhNg0fn_ibKBdpndxS_c9xLO5MRyM4jyLy_oPPCy8DeBxV2CJEDZZYfw-c9mBBPdG_YxjhzyAlFgH1mTflfv0wTrZnns-BS9Kj28jRb7ch_e68k2_MJV-1Nm6bMQhFNAOxY9Mxm6uuuFTvxm0oKA10A4a6bXOJdbeg9hMy_ewRslTETneLp1VGCofeaOnLas8gkGuSAzOvjbEyecOi_5P9QPzNyOOTPliSSS_sVhQBYu7tTSONORzxyFO5odx9Y7EjJjvIQW9_sRyEDuDGICnKg9_RaXqlLxBZeR89WBU0otBM-UFWjpfsQgyf7VLCSl7qeQZ9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw0RJXVPBwezlEDO60KUvOTO1jX5_MFcQ5GVKf3xKpVA-REz6M6RGji5t6Zgl-NImQzir2kaB6oLQ1WAgj6TiTS59awVvMMoI2N6IT5wmYKr86FIMfCSSDkhwCiVnaO0u9JF7IbBPztABZiMIcrdUPOW0tMbV6qqA7vx2mtl7Jvmh-K8FwY2Wi9aJZsXpB3OGwByL1JkPUwcI97ENmvih9MN-4Zump5WWnhJrIKRsF0t6jndLgVIoxA_cOHNNiXtdEAYLIaRT2PzNyE5rG-UBvp_0fCI1Nwijsz14m3BH9y1HhHog2SdctPPo0xc--G5rmZrhJ5O1m-2HJsZGSG3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5_D1JwQa2ZGSp_E3F8qVuHMqidrBI8VqLyFPzbddpo2U-iSfpUJvYupVZ85uFhS00ZYkeSiGekrqpMRBWK5gIacWRY1IL_oq1rkqGkfjl1UtUidTPma1VsSx8Pcc0cPBkrYAyB9gN--UP2Wj3JphMjdb4zibDstogUYHw6oY8W9YTqz9SN_oLqpXB07GTkizEj_MWdiBmkzRCtFXgtUPDPV0MoiGOaG6BG52IEIkVIILVc9srEqnWaXnbD6OyRJvE-7o8erp2Qlg_lfYvDY-rg4EAniWbonXsERKgEO8v0Y6jKUhKrpG4-99TcWTL1fBPtrx-GXMMzpyus4X3A1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc6u4Om-s0qKa_XLQrBq-E884Ygcu__2uW1eF5sBMOmh3HLsJiw426DW9qgzwm584w4SS-A-FNC8IReg18LkhFkjpTxwOtEQxZXcLfsQlM86jJ9w5LHQfJEwKoLXK7XhXGw-5th4F-r0rFqnHMEXt1nDfe6IutpxwRPquXRupgVoWmL22CoIi7xYX_z4OsUcWb84OyfXILJl5S1JjYXBsUqHlRVWVars6-vpE7v2QIJANeUZmqQycPD9ZsIUe9k6LawYe_yktqOPRcg2CQeNJBluchqjqdmqhnvJgxetHiulMD-O0F6Del-ZqIMoXyvJCTWnDjAv3szXSl8PW0ur-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnfruFPyTVZ3we8sNM0Sk5wBqOPIQIZYgqgUkihdzaSnEXd5TuMTx5aqj7zZfrjh7s9SUPlIlSrCE7ACiYwUJlvkZffi_hlItvLAgzZg0O1gKAGZzFcq0B5jphL-DsgPvVvzRIM7seNvxeq7wYkwBXz1Cra0x1_9eYH_87YMF8eA7sOBk-lw_7MJru6K9QFUWto_F-BRVh7vFgbFPFIG-aXv2-fIdlgLVOo2D40DcFGniZAABitIranU03mm6xi9ZJqswLLLmDkftOtf0hSmncVMR6WFP8fshOiwWjS5Vh-wb2BMkLcHUQ89Zhvrw-3cJjFomBQRRdEIXcfSD9qkBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم اقامه نماز بر پیکر آقای شهید ایران
🔹
تصاویر خبرنگار خبرفوری از اقامه نماز بر پیکر مطهر رهبر شهید و خانواده ایشان در مصلای امام خمینی (ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666794" target="_blank">📅 08:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666793">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7451993ab0.mp4?token=CuW4-7CFshGPF0o_OhHwwBjj1hhRaffASDEfVOdnVcw001PZcrkgrBhupeG9LAf7AYNPPGIh40sxs7PlsxlB5m1pPVtEqBr3wXgB8CTYDn9GBelIKuWCLkmddLBlSmhBOgLs81NqH_rw18126B6Wp_DchgAupUJ5CYcok8l4yszb4RsmIT-bWd11OZgE1VTwfmUgCn06Lh7Kg89jIiRNedBSLn7rjMDJza71Qmc507NPdRC5rizd9_m7kdzPwD9EUi8oMy91l3eKbGAZmppEFWk-_j10CqzhShekP9YWmFnj0KQbu4ef3iBl7DEw_Z3Ovz63kkIOvpjPALC3M6utDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7451993ab0.mp4?token=CuW4-7CFshGPF0o_OhHwwBjj1hhRaffASDEfVOdnVcw001PZcrkgrBhupeG9LAf7AYNPPGIh40sxs7PlsxlB5m1pPVtEqBr3wXgB8CTYDn9GBelIKuWCLkmddLBlSmhBOgLs81NqH_rw18126B6Wp_DchgAupUJ5CYcok8l4yszb4RsmIT-bWd11OZgE1VTwfmUgCn06Lh7Kg89jIiRNedBSLn7rjMDJza71Qmc507NPdRC5rizd9_m7kdzPwD9EUi8oMy91l3eKbGAZmppEFWk-_j10CqzhShekP9YWmFnj0KQbu4ef3iBl7DEw_Z3Ovz63kkIOvpjPALC3M6utDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های مردم در فراق رهبر با مداحی حاج محمود کریمی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666793" target="_blank">📅 08:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0057730d.mp4?token=okkXl6rOZJ4gXemWEs5G2hX2yTspL2HSvwa96pSOgWMBmLgJ4xdjb3k3Q8ZAnGd-1wKhkdoUNW6oKRIYU2gU7r0mUxB8RL37VO7DBNO8y3_1TMqTfJB2DR1ydDDm4MTCIwoyRzz7nogYbwpl_1TA0BTYTUy8nPE_aKTFz7ABlldG3kKm_83Icy2FjatdXcj4ePNAed6J6oUdaFswJ8zEOCQW9cPjP5IoCULd7Ckx2rZ1NV304xocKJVlqoJClglLLDINBTvMP1zP2wzboG5WZ_7VMEz19OChfzV8792geIChAIk8OTzh7UpuwVR5RqXZog5piSCBwYDa5mAaySot1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0057730d.mp4?token=okkXl6rOZJ4gXemWEs5G2hX2yTspL2HSvwa96pSOgWMBmLgJ4xdjb3k3Q8ZAnGd-1wKhkdoUNW6oKRIYU2gU7r0mUxB8RL37VO7DBNO8y3_1TMqTfJB2DR1ydDDm4MTCIwoyRzz7nogYbwpl_1TA0BTYTUy8nPE_aKTFz7ABlldG3kKm_83Icy2FjatdXcj4ePNAed6J6oUdaFswJ8zEOCQW9cPjP5IoCULd7Ckx2rZ1NV304xocKJVlqoJClglLLDINBTvMP1zP2wzboG5WZ_7VMEz19OChfzV8792geIChAIk8OTzh7UpuwVR5RqXZog5piSCBwYDa5mAaySot1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات خروج پیکر رهبر شهید انقلاب پس از اقامه نماز از مصلی
؛
حمل پیکر مطهر آقای شهید ایران روی دستان
مردم عزادار
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666790" target="_blank">📅 08:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9510708df.mp4?token=SIIw0e5ZI3d1OQ06nwAphVqOMTQIEVju86gt-3rxfIXKNs3KmMAXepEsSXkza_ZPH-UUjvo0i6lpfuPbcgBwFXzNXV0d38HpMzwoEtqqKu0ky86x4a9K7soS6lpbO5oytbtuYbqBaMHDrR6O9o2EfPX_dy-NXjLSBTw_BHTfWuaCr5CSB2sD77IPXkm6qAJ-wRZB2uDoxKvLpHBFK2-pyuaU_9AeC0CtQf9HHvsp73npF1SG_EZet4R9znvrnBiHo_NdjP-lVswpY8FnUbO1Wuba82gxSar_40lcnZuw1z7nlgmhjeiVG4RnuL2XCInhgFx3WcLfVms9_9XQh-4KpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9510708df.mp4?token=SIIw0e5ZI3d1OQ06nwAphVqOMTQIEVju86gt-3rxfIXKNs3KmMAXepEsSXkza_ZPH-UUjvo0i6lpfuPbcgBwFXzNXV0d38HpMzwoEtqqKu0ky86x4a9K7soS6lpbO5oytbtuYbqBaMHDrR6O9o2EfPX_dy-NXjLSBTw_BHTfWuaCr5CSB2sD77IPXkm6qAJ-wRZB2uDoxKvLpHBFK2-pyuaU_9AeC0CtQf9HHvsp73npF1SG_EZet4R9znvrnBiHo_NdjP-lVswpY8FnUbO1Wuba82gxSar_40lcnZuw1z7nlgmhjeiVG4RnuL2XCInhgFx3WcLfVms9_9XQh-4KpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت قرآن توسط حامد شاکرنژاد پس از اقامه نماز بر پیکر رهبر شهید و خانواده ایشان در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666789" target="_blank">📅 08:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bff61228.mp4?token=tLkccoEASu-OGCO-Emvw6AbmruOeMGcdKmerIPkOOiVn_VKRmbhrflDPHKxxSN2vgAsdxesWwkbcFLMDKS7Qi6G9zTF3kiLCK7Up3jX37IxeG_cfzJXJH8AD6QWwSsd3eRF8B4dvRVttdXJ44vhT8Cl-9X3C5C6BB6avbt3MqKUwzX21bNrMl0Ub3HqFhOSKBHzt_Zl3t4OfElwcFzvjxWygEd1HnaSMPJBQKFtOasmTs-7ZyzuQ8N-HeRhY_8xoMSaRmQx_dzllbBEDKZQTHGVIlKhOKM11c7TX_bNEX3KCQxlMMF9rqH4dg5Tz50ob61uq2jRfodgswnl_-_Gr6JfdQrCc6vrAqZy4uGNE2ZkBcZEneZqXTJkshXla_wEFbhJ2NGgBpmjr7CzF4cHmnqYfSiFvgHhMddiY63ReOiOdEggH70uSSdhggsLcJf3yYTD8GExzXvo_33-ElBq4mNVvIal4rsqsqYZmjMaWH7LySR9IYrq26eAeHUJool3kTfdL6m-BIauUTW2Pp1Iy1PuLTUdEIiJaebWCKDQcytE85EJOuinnOCsW1j11hZG5URTFHZVCozRHqa5mIRuJ9zlr5QINEPohItcEL8oXvkwMD4tOb4Gu5ALyhAlG-Bh5l6JWZf-2ljcDO1aKjzwh0EtTGKpSqoSMeG-j3uep2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bff61228.mp4?token=tLkccoEASu-OGCO-Emvw6AbmruOeMGcdKmerIPkOOiVn_VKRmbhrflDPHKxxSN2vgAsdxesWwkbcFLMDKS7Qi6G9zTF3kiLCK7Up3jX37IxeG_cfzJXJH8AD6QWwSsd3eRF8B4dvRVttdXJ44vhT8Cl-9X3C5C6BB6avbt3MqKUwzX21bNrMl0Ub3HqFhOSKBHzt_Zl3t4OfElwcFzvjxWygEd1HnaSMPJBQKFtOasmTs-7ZyzuQ8N-HeRhY_8xoMSaRmQx_dzllbBEDKZQTHGVIlKhOKM11c7TX_bNEX3KCQxlMMF9rqH4dg5Tz50ob61uq2jRfodgswnl_-_Gr6JfdQrCc6vrAqZy4uGNE2ZkBcZEneZqXTJkshXla_wEFbhJ2NGgBpmjr7CzF4cHmnqYfSiFvgHhMddiY63ReOiOdEggH70uSSdhggsLcJf3yYTD8GExzXvo_33-ElBq4mNVvIal4rsqsqYZmjMaWH7LySR9IYrq26eAeHUJool3kTfdL6m-BIauUTW2Pp1Iy1PuLTUdEIiJaebWCKDQcytE85EJOuinnOCsW1j11hZG5URTFHZVCozRHqa5mIRuJ9zlr5QINEPohItcEL8oXvkwMD4tOb4Gu5ALyhAlG-Bh5l6JWZf-2ljcDO1aKjzwh0EtTGKpSqoSMeG-j3uep2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای انتقام‌جویی «یا لثارات‌الحسین» مردم در مصلی تهران پس از اقامه نماز بر پیکر رهبر شهید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666788" target="_blank">📅 08:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2157a035b.mp4?token=gWWIBxW7Xujk0_g8tbCv6T8EjS6bEEjctZKbNdzAdefnpPBk8SXzzErijhgwsgKt4XE-3pxFVcBCKFqoV3_W3AKG5gkSiXxIvomcvUMh53cobddG-BkQwBWjEIgk9nxK4bTwwmX71GYEIQF8nwHQqyKl85cpgT5TVEfMEHSCyBwiYVDEZ1C1vlYfyQZk803gkFdl6LWgRuezZVRVW6gbO5-y7RKSYJI0RkHZ9J0K-2j4Uj5PP5oybohyR7PRiHszmRAqVq9-DS9Ayj-3U108JQUp5RH2u5Szr2EqvZQX933-zG-CdKjNxojtSpKu1Fc3lzWl-IUHk25ytHeBzf6Vew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2157a035b.mp4?token=gWWIBxW7Xujk0_g8tbCv6T8EjS6bEEjctZKbNdzAdefnpPBk8SXzzErijhgwsgKt4XE-3pxFVcBCKFqoV3_W3AKG5gkSiXxIvomcvUMh53cobddG-BkQwBWjEIgk9nxK4bTwwmX71GYEIQF8nwHQqyKl85cpgT5TVEfMEHSCyBwiYVDEZ1C1vlYfyQZk803gkFdl6LWgRuezZVRVW6gbO5-y7RKSYJI0RkHZ9J0K-2j4Uj5PP5oybohyR7PRiHszmRAqVq9-DS9Ayj-3U108JQUp5RH2u5Szr2EqvZQX933-zG-CdKjNxojtSpKu1Fc3lzWl-IUHk25ytHeBzf6Vew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های حدادعادل هنگام اقامه نماز بر پیکر دختر شهیدش
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666787" target="_blank">📅 08:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXj1M6_9yg8pnZrSM0usxdfOczuVRDqTMy3zQPu7I464DV7DfUCrW4cx5DtCE5ziF54TYsTXIMIyOdMSvAJnHqr14nzQ_1hZe8w00UqdpsaVHGtFhpHBv6NFSTqdKLV7MRsjW5hq3L5Zdq5iIdEftg17UqjvUeWfwXkhma9QFtlR1IrgPyX3vnP7IdfLnkboOlbdqoxFOLAKXYRbnMnkXkmZIAbrkT89sGFchXMbrabhhyGHMk5Yxk6DNP2-aqy9kYX5NbHSb2X3dsRCKVIJBbXR3Uq_dHhVDDgE-AetHSTFXsRo6GvUsJGS5au-VoPa1t1TZEUtBGJsSxRdO_qJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از پدر شهیده زهرا محمدی گلپایگانی نوه ۱۴ ماهه رهبر شهید در لحظات اقامه نماز بر پیکر دخترش
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666786" target="_blank">📅 08:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338b21beb1.mp4?token=iK-RGs7bLII0QhHDMMszZ4fASZKCo4xerjBm62rp_adOXHmBTWYxkNfA6pSQC2Rklk33OW3QWZ5sxkVB7Tw6fTEm7nS1HCm0yTwMNOzDOtv-yS_OGZh89PAB8--0GVvhd9C5LYnqwODOkC_Wzs6L4ZPTDCOn2zj4uGE3M0MtdBsHS6CvxLqLKHLGytCTW6LZEDnogi7V1T_Ct3epPqYCViNaHv70nq4_2p_eNoNiaHjWCh-UV7meC_5Hy9boBONuim-S2Rrb6AYmNEW2FNOJJSbFNX9X7GTzxVyn897uL6Ue44Q_jvwo3bafG1kzY0qXYMgfa5hdGFGTEsXojQFl4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338b21beb1.mp4?token=iK-RGs7bLII0QhHDMMszZ4fASZKCo4xerjBm62rp_adOXHmBTWYxkNfA6pSQC2Rklk33OW3QWZ5sxkVB7Tw6fTEm7nS1HCm0yTwMNOzDOtv-yS_OGZh89PAB8--0GVvhd9C5LYnqwODOkC_Wzs6L4ZPTDCOn2zj4uGE3M0MtdBsHS6CvxLqLKHLGytCTW6LZEDnogi7V1T_Ct3epPqYCViNaHv70nq4_2p_eNoNiaHjWCh-UV7meC_5Hy9boBONuim-S2Rrb6AYmNEW2FNOJJSbFNX9X7GTzxVyn897uL6Ue44Q_jvwo3bafG1kzY0qXYMgfa5hdGFGTEsXojQFl4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در مصلی: یا حجت‌ابن‌الحسن تسلیت تسلیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666785" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10526db91.mp4?token=Cay4TT5yNoOSmKNKcyD--u4a1nKxGQn3ZdhqsOXSL2qwUZMZYz2TczOtM7z6GTq2KR2ia8JOtzEG3f22gLWnJAiOqkIdhCnLTVoGueBlEWdlrmWQQkjXXA6rJUkn7TCfFsoBaUkvZ2JcX2nCvev3auuPGNaFOnIWudbYE4kCiRoqR5ae5o6unU6Idb5Su4zBip5Y41MTw_ZQwajSQLKQ9nQw6yvQwR96NItBM_Jx6pjPLQQ0eZgkHhyY0TgihNJ7zIK_KcNprMhuA9EtwVMb8BXmrhHaSHfPKZv5CmrZ-v3PFKqOcWlMHZmLo9NzmuZTjM1td4s06zRBqKAOl78yMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10526db91.mp4?token=Cay4TT5yNoOSmKNKcyD--u4a1nKxGQn3ZdhqsOXSL2qwUZMZYz2TczOtM7z6GTq2KR2ia8JOtzEG3f22gLWnJAiOqkIdhCnLTVoGueBlEWdlrmWQQkjXXA6rJUkn7TCfFsoBaUkvZ2JcX2nCvev3auuPGNaFOnIWudbYE4kCiRoqR5ae5o6unU6Idb5Su4zBip5Y41MTw_ZQwajSQLKQ9nQw6yvQwR96NItBM_Jx6pjPLQQ0eZgkHhyY0TgihNJ7zIK_KcNprMhuA9EtwVMb8BXmrhHaSHfPKZv5CmrZ-v3PFKqOcWlMHZmLo9NzmuZTjM1td4s06zRBqKAOl78yMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار وحیدی در صف اول نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666784" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c90e72396.mp4?token=LZ2qvSD8W0it1grqWtXpeUHV8pJHnh13zT-HOJL_hOkEuTiSnOv_E3Ny9-Kifj0MUM3Ca6gfBa-E_IwuaaTY_U2cjEy4ZveMCMyL1zcLwKK_ZhfgCZTDhZX5FIfOfPoYp2un67nzAZ8l8SwVPLVED0F5lwMKDCPnWEKDMDEmIbGFJ_mEGgtDeD12SYrnjcjBjH5OUVUBomZO5sZiCtvhdO_Xy-c1u5DbQicXZTRNhMUAStTJC-Tvug8Ar9ze0fDhWAaqZQvGck060_T_cpbcgRyLyBsbKV_l7lMMbx23j3AxjOtLJeneAkYsz9F7r3mrkyb8NS60WmC5XZF3b3kY7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c90e72396.mp4?token=LZ2qvSD8W0it1grqWtXpeUHV8pJHnh13zT-HOJL_hOkEuTiSnOv_E3Ny9-Kifj0MUM3Ca6gfBa-E_IwuaaTY_U2cjEy4ZveMCMyL1zcLwKK_ZhfgCZTDhZX5FIfOfPoYp2un67nzAZ8l8SwVPLVED0F5lwMKDCPnWEKDMDEmIbGFJ_mEGgtDeD12SYrnjcjBjH5OUVUBomZO5sZiCtvhdO_Xy-c1u5DbQicXZTRNhMUAStTJC-Tvug8Ar9ze0fDhWAaqZQvGck060_T_cpbcgRyLyBsbKV_l7lMMbx23j3AxjOtLJeneAkYsz9F7r3mrkyb8NS60WmC5XZF3b3kY7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماز بر پیکر شهیده زهرا محمدی گلپایگانی نوه ۱۴ ماهه رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666783" target="_blank">📅 08:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666781">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c577d50cba.mp4?token=T4-gnLBB68MjRcC4KnHsA6ukFD3lzHuuoq_ISCHGZKNHJEWogsZ4gZG-Xdl_4TmBRM8xMnIWk4_WdtgxEC6C78xBmVtvfeS5NzFsJaCPNSQm1lovgndNer0ciBG25HDN3LzwDJfv7rTlVLfFRosoaiqR-J6l66pnYYDXlXsFwj_LJvRszV2I2XPkuuPeq59-GEFWt0joaxCCEqAdvMPmPf256bFF4cul_yCC27zYK5oxGA5cRCqO0sFz7XsSvugU21ccK1542oyA4vC4IlOqlnpimuw_-_3auLui2vS9JGiVCp4TXGRZQhd93QqajKq3JELRRsEGygIzIC0JsbTOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c577d50cba.mp4?token=T4-gnLBB68MjRcC4KnHsA6ukFD3lzHuuoq_ISCHGZKNHJEWogsZ4gZG-Xdl_4TmBRM8xMnIWk4_WdtgxEC6C78xBmVtvfeS5NzFsJaCPNSQm1lovgndNer0ciBG25HDN3LzwDJfv7rTlVLfFRosoaiqR-J6l66pnYYDXlXsFwj_LJvRszV2I2XPkuuPeq59-GEFWt0joaxCCEqAdvMPmPf256bFF4cul_yCC27zYK5oxGA5cRCqO0sFz7XsSvugU21ccK1542oyA4vC4IlOqlnpimuw_-_3auLui2vS9JGiVCp4TXGRZQhd93QqajKq3JELRRsEGygIzIC0JsbTOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از تکمیل ظرفیت مصلای امام خمینی قبل از شروع نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666781" target="_blank">📅 08:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666780">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آغاز نماز بر پیکر شهیده زهرا محمدی گلپایگانی نوه ۱۴ ماهه رهبر شهید انقلاب اسلامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666780" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666779">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اقامه نماز بر پیکر مطهر شهیده سیده بشری حسینی خامنه‌ای، شهید مصباح‌الهدی باقری و شهیده زهرا حدادعادل
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666779" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1db6da14.mp4?token=YaeR36zfTzciXBNvB0mPjk0LL3CUdnsEtKBb9-z-UFITv90sQrzTkdmH_qbY_UYcKoiCefn2w9wkGh_453nKCYckk5Nxa-Pbo3YCJvBsXA_ExQ0U1Lobth9vK5tU88lH64dm7o0oUJK0gsSxq55dtuZvrfZ5GN7vKzQTTiw0su7XMhxdpW9IOIZH2PMXu4iBXPX5nwi7_MRsT14zaPf95t1de-Wbh980GG5OcCoi2UsRajBAkhawhsK15rOMSmUmy0j9KOgueef_4GV_7rAhv6jOcqID0QTfN0uXOm42-bkr0Ka6nBWLC2-p2_lZ54bptWrpk6JaKq1m78awNOh8vCtjrIMGZXcdnLkAJhos4WwIaudHNmAseV2DYqOyMmL9nMYxIpId3R8y-MsgRo8EL2FKpZ3jzmLljcYhIY-Xb-NvZoo2Aqgl33HiC4nmnBLKUJkCnf_UcYqGPUK8Q0rYWmAibo7flrCc3cfxA7485KqLDGUQ2Ax6HFMDr0lvXjnJSRwzj9cQtZ8Q1DUw0uYm4pinwCy5GdmqG2uRLjnp5927YTnW6uo6fI7gn2HBOaASCHyMPBY8Wjafi-51wp4I-a9v2j3lX9wfR0dmwQkFJNYxvIjIlPTIW_b-ptFexNW7IlX2X-3PrKQQkKqmvUijP2V3fmFTi-6yS5ErI_4AxqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1db6da14.mp4?token=YaeR36zfTzciXBNvB0mPjk0LL3CUdnsEtKBb9-z-UFITv90sQrzTkdmH_qbY_UYcKoiCefn2w9wkGh_453nKCYckk5Nxa-Pbo3YCJvBsXA_ExQ0U1Lobth9vK5tU88lH64dm7o0oUJK0gsSxq55dtuZvrfZ5GN7vKzQTTiw0su7XMhxdpW9IOIZH2PMXu4iBXPX5nwi7_MRsT14zaPf95t1de-Wbh980GG5OcCoi2UsRajBAkhawhsK15rOMSmUmy0j9KOgueef_4GV_7rAhv6jOcqID0QTfN0uXOm42-bkr0Ka6nBWLC2-p2_lZ54bptWrpk6JaKq1m78awNOh8vCtjrIMGZXcdnLkAJhos4WwIaudHNmAseV2DYqOyMmL9nMYxIpId3R8y-MsgRo8EL2FKpZ3jzmLljcYhIY-Xb-NvZoo2Aqgl33HiC4nmnBLKUJkCnf_UcYqGPUK8Q0rYWmAibo7flrCc3cfxA7485KqLDGUQ2Ax6HFMDr0lvXjnJSRwzj9cQtZ8Q1DUw0uYm4pinwCy5GdmqG2uRLjnp5927YTnW6uo6fI7gn2HBOaASCHyMPBY8Wjafi-51wp4I-a9v2j3lX9wfR0dmwQkFJNYxvIjIlPTIW_b-ptFexNW7IlX2X-3PrKQQkKqmvUijP2V3fmFTi-6yS5ErI_4AxqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از مصلی تهران: تمامی درب‌های مصلی بسته شده و از مردم خواسته شده پشت درب‌ها نماز بخوانند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666778" target="_blank">📅 08:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8976e23934.mp4?token=qKGMpUqMSKavFANPtpNh3qzorNEk9RksgcBHintiGYsH2BR94UlRKkwzxa6pew0WxiXLIT1xYSP17U6Qu-lRrWVxpDS2lSSIvvLqxvgYP0Kzs-LRo6QzwF51NRGlbQrV3NVyFDiHSWTMpLdtQeweFi7_v307_zQQU-Wsw_5requSlfGogklnPhiLuIjXh4By-2RqF9PlSaw-ObX2Pt_bTzp0EiDXvTL36t7YgCejPEW0pFmtJmZc6CdRFHNF7oaAh0JJemN62T9obYud1BrGGYj9QeWhOyWLAO0DVkoA9Wl9y5rYLAYObWzwszixUz4TWcJxOL2T0m2P5e8OTKA7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8976e23934.mp4?token=qKGMpUqMSKavFANPtpNh3qzorNEk9RksgcBHintiGYsH2BR94UlRKkwzxa6pew0WxiXLIT1xYSP17U6Qu-lRrWVxpDS2lSSIvvLqxvgYP0Kzs-LRo6QzwF51NRGlbQrV3NVyFDiHSWTMpLdtQeweFi7_v307_zQQU-Wsw_5requSlfGogklnPhiLuIjXh4By-2RqF9PlSaw-ObX2Pt_bTzp0EiDXvTL36t7YgCejPEW0pFmtJmZc6CdRFHNF7oaAh0JJemN62T9obYud1BrGGYj9QeWhOyWLAO0DVkoA9Wl9y5rYLAYObWzwszixUz4TWcJxOL2T0m2P5e8OTKA7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللهم انا لا نعلم منه الا خیرا...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666777" target="_blank">📅 08:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCuB40J9WV-Bj09hooWe61GBAAVQllgT9DbURwnNmV4ljnrlgRzcuZKisGoPjMPwfAJ1E6BeeaXeMUTYFvkYkTlixk0JPlRi2UUL0hMsHEfFokMJxpzkzylm9McG41X5ss0LyN6XDV4logFSLhQhxiEjzyhi580K_lb5X19x5iXw5O068JRyuN1mtoQw3aWgR2YtJw50nlf0Hg7OqdL_e6kI7vQTxa3CIvx6rlkF4FVQ8oufuyA9ViCFiiRctnjNHNKCf8-kYWSKQWV7y9TjsWnla91vjDMbsrMbN17Tw1fy-SHAkgZltJeeZa8NH89fNLOtFbirayHxrVQO3-oNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر حضور سران قوا در صف نماز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666776" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666775">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2be1578d.mp4?token=c8GNQUXTlhm2nVXvYByDnmh_Fz8bmvxIs150iapt_dJ5IyALYOC62EP_i2GkfFQ1YFBUDTbMPPQqc6SpMxEqTIu9hMbkMmPNNs4njqt1bIApHOL2c2fUfBfDI3zPffnQYaMMINe29vCAhKbyiewBYTzhWel6I1TPWBZBMZf1ch4p5zBgVqQm8h0R0pe2s-NYqPg2kY9J5WNynOFE_ZUJYdO5Hj1wxuTkAHDpQac47e4jnf_T9GnJbC5QilIEQJEbG1MJhqk95HjCbburxYNrXIpan2qwXEp9aROLhwh1Zsc-a2gpjR-1c8n68N7BdZ1iLYayJeG797NA22tnLuSUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2be1578d.mp4?token=c8GNQUXTlhm2nVXvYByDnmh_Fz8bmvxIs150iapt_dJ5IyALYOC62EP_i2GkfFQ1YFBUDTbMPPQqc6SpMxEqTIu9hMbkMmPNNs4njqt1bIApHOL2c2fUfBfDI3zPffnQYaMMINe29vCAhKbyiewBYTzhWel6I1TPWBZBMZf1ch4p5zBgVqQm8h0R0pe2s-NYqPg2kY9J5WNynOFE_ZUJYdO5Hj1wxuTkAHDpQac47e4jnf_T9GnJbC5QilIEQJEbG1MJhqk95HjCbburxYNrXIpan2qwXEp9aROLhwh1Zsc-a2gpjR-1c8n68N7BdZ1iLYayJeG797NA22tnLuSUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز مردم در سراسر خیابان شهید بهشتی به سمت مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666775" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666774">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آغاز نماز بر پیکر‌های شهدای خانواده رهبر شهید انقلاب اسلامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666774" target="_blank">📅 08:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666773">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c413de9cb.mp4?token=fFnoY9GYD4yBelABGXvozRgeQ8iLvtnv0IWD0RxSfzzInkwvTKEAkGE8jTUTUlQlgBAB6YEcNTzYnFfSvxA9-wU0pplQZWHtHQzVHeyA2tAB6HxyLnhcDbanXc5zGxvGECqH5biUbRqq3GkH7M0r-lSERw3pVKWmIV18-YV88aT7n-A4iBroaDMB5p96lLknWtH2d7fo2zFFwPoZZaXbfLcT53h_qtSA5176vhyoqvpPHlAa81JbmleyZtvWlKHZ3xRqOxdcrhAp3wJZUccMA9mz3C8hHMuXhVKtePoP6e5EEKNgi32u2EfrqzIg_qdPdPUhFwsqUCLXNPFVTiovzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c413de9cb.mp4?token=fFnoY9GYD4yBelABGXvozRgeQ8iLvtnv0IWD0RxSfzzInkwvTKEAkGE8jTUTUlQlgBAB6YEcNTzYnFfSvxA9-wU0pplQZWHtHQzVHeyA2tAB6HxyLnhcDbanXc5zGxvGECqH5biUbRqq3GkH7M0r-lSERw3pVKWmIV18-YV88aT7n-A4iBroaDMB5p96lLknWtH2d7fo2zFFwPoZZaXbfLcT53h_qtSA5176vhyoqvpPHlAa81JbmleyZtvWlKHZ3xRqOxdcrhAp3wJZUccMA9mz3C8hHMuXhVKtePoP6e5EEKNgi32u2EfrqzIg_qdPdPUhFwsqUCLXNPFVTiovzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت انبوه نمازگزاران بر پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666773" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666772">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4828947107.mp4?token=D5c2o6DoIXBYJs42GKpVe69cojA-4YvuMDMm4MZRkko9Evnp3RAB3A61i3HR5t0Dr06RKKN00qaU6PPuCgJiQycMN4t18cw-Ddy94BA1P__hi6-H5EpJEgs9-O9UyzlCFUMfUeK3I6TTnwFWKmCuvjFoHbu8BWXGm2Ym1LD6-1A9uxz5PlYQ_TouWxZoU5VwCCIEfFOliGwu29k07CrwdaM9DmUJgpD6is1eDrk65eA6kiKuiDeXOzAJpxodG-smjy_-I0Lhv-fTsWJ2vGbtcPO_0H78WTLNnf8fsFpHKyRRbTEC_GO7Z1kgxX-pFvXskltvll6SZlHTnrkQ7qFV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4828947107.mp4?token=D5c2o6DoIXBYJs42GKpVe69cojA-4YvuMDMm4MZRkko9Evnp3RAB3A61i3HR5t0Dr06RKKN00qaU6PPuCgJiQycMN4t18cw-Ddy94BA1P__hi6-H5EpJEgs9-O9UyzlCFUMfUeK3I6TTnwFWKmCuvjFoHbu8BWXGm2Ym1LD6-1A9uxz5PlYQ_TouWxZoU5VwCCIEfFOliGwu29k07CrwdaM9DmUJgpD6is1eDrk65eA6kiKuiDeXOzAJpxodG-smjy_-I0Lhv-fTsWJ2vGbtcPO_0H78WTLNnf8fsFpHKyRRbTEC_GO7Z1kgxX-pFvXskltvll6SZlHTnrkQ7qFV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرازهایی از اقامه نماز بر پیکر آقای شهید ایران توسط آیت الله سبحانی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666772" target="_blank">📅 08:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666771">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7db1b638e.mp4?token=hda8vvcIupvVLEEp8pVbTAKQJMFiLr8Oha-igIV7gabhQpzkK8Zgb2Xm4rIj1MDOfV1spycqk4lve3I-oVZdZIPwkd9a7KtMUT2WnKobAtCA-dWEBnhrJQpS-E3dCEsBvVnaVdbL4L-m4Zf6abBIa7Hwv2Flfe5TuXnW6dkOe0J9DKyNfzud1m3hWKgrT0OTZUPTFqhm-xsUqOqrzNV8lKf2uGgXhqPrJ-VwtGW-IXlgsAFhrFvkRiuS5ZKJGJgMEocLJxaGGwxrx8D5M4kB5bCkNHWnb9-3_DsdTfPP3uLogEFGo37CUgFUyPoalK7__6uiQMq2GRWwvfQwej6jFmFe72tujf-ySvB-rywQbU3Bicf_kiw6HAk2gmX7TDY0VOU0rKKCmlMswuyK2LIgLc1JG-rTRJO42_fgIF-6JsSR5Tuc19Oh68esfnOzS7FWVeBD3qQ3XjqvLUB45af9bVIiIHt2iVaKUViFYpAoD7Np6tFUrbgAKe3BbHZgWLZQDsdSiuquYk8LwKSER5kqKDcltsLm5EMD9FhTW9GF2I4nKyf1mZlnFPLDD93MURfcns42NLzIv-EI8mr_O6OLFK-2Zl-FoeTf2cjruqutwbj5VR1vFSqtr47_4-sxcgMiFoRyTel6C7pMx7idGshM7jpBMvSOs_hBLBKhZJ06vCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7db1b638e.mp4?token=hda8vvcIupvVLEEp8pVbTAKQJMFiLr8Oha-igIV7gabhQpzkK8Zgb2Xm4rIj1MDOfV1spycqk4lve3I-oVZdZIPwkd9a7KtMUT2WnKobAtCA-dWEBnhrJQpS-E3dCEsBvVnaVdbL4L-m4Zf6abBIa7Hwv2Flfe5TuXnW6dkOe0J9DKyNfzud1m3hWKgrT0OTZUPTFqhm-xsUqOqrzNV8lKf2uGgXhqPrJ-VwtGW-IXlgsAFhrFvkRiuS5ZKJGJgMEocLJxaGGwxrx8D5M4kB5bCkNHWnb9-3_DsdTfPP3uLogEFGo37CUgFUyPoalK7__6uiQMq2GRWwvfQwej6jFmFe72tujf-ySvB-rywQbU3Bicf_kiw6HAk2gmX7TDY0VOU0rKKCmlMswuyK2LIgLc1JG-rTRJO42_fgIF-6JsSR5Tuc19Oh68esfnOzS7FWVeBD3qQ3XjqvLUB45af9bVIiIHt2iVaKUViFYpAoD7Np6tFUrbgAKe3BbHZgWLZQDsdSiuquYk8LwKSER5kqKDcltsLm5EMD9FhTW9GF2I4nKyf1mZlnFPLDD93MURfcns42NLzIv-EI8mr_O6OLFK-2Zl-FoeTf2cjruqutwbj5VR1vFSqtr47_4-sxcgMiFoRyTel6C7pMx7idGshM7jpBMvSOs_hBLBKhZJ06vCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری: محمود کریمی برای آخرین بار در کنار رهبر شهید، ای ایران خواند...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666771" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666770">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc049208c3.mp4?token=Nq-WRhOZBy-JUYMTrFd6iZWrSLI8PdqrQGdizB7-7WgGfELGyzkWlAFkgVCLH3sjIYWmbRaJrqwIFQw2j7H5LpK5EQ7HZN1CWvvmLgV9iCpjsMMyMbXxXp3ezycMebymwfX2xi3ENxlw-Azh5nDWVfkxRnbdC-joXd2kGnMCPVDyZ_mv1tMU04oU7oqTkMPkJ0BlKS_edioJxuatM8h2mwQYaSn1RWINJnB2TBdaKDNkfNCDLvzH74Rb1mwWNiXnoxl-vO5VWHyk1LZD5m_wSI1Oi5SHZatDtjd0UFWLlz8kFfdnyc1TGJDwSvB116DoX6YAJdXx5QiZ-wZZJsTWGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc049208c3.mp4?token=Nq-WRhOZBy-JUYMTrFd6iZWrSLI8PdqrQGdizB7-7WgGfELGyzkWlAFkgVCLH3sjIYWmbRaJrqwIFQw2j7H5LpK5EQ7HZN1CWvvmLgV9iCpjsMMyMbXxXp3ezycMebymwfX2xi3ENxlw-Azh5nDWVfkxRnbdC-joXd2kGnMCPVDyZ_mv1tMU04oU7oqTkMPkJ0BlKS_edioJxuatM8h2mwQYaSn1RWINJnB2TBdaKDNkfNCDLvzH74Rb1mwWNiXnoxl-vO5VWHyk1LZD5m_wSI1Oi5SHZatDtjd0UFWLlz8kFfdnyc1TGJDwSvB116DoX6YAJdXx5QiZ-wZZJsTWGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از حضور فرزندان رهبر شهید برای نماز بر پیکر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666770" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666769">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر رهبر شهید انقلاب به امامت آیت الله جعفر سبحانی
🔹
آیت الله جعفر سبحانی از مراجع عظام تقلید نماز میت را با همراهی جمعیت میلیونی مشتاقان و زائران، فرزندان رهبر شهید انقلاب و مقامات لشکری و کشوری  بر پیکر آقای شهید انقلاب و شهدای خانواده ایشان خوانده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666769" target="_blank">📅 08:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c304583c30.mp4?token=VAg5SgLP_NyCGhjloxJPwZSuHcdbWVJLjDHdxMhnd0ysfNkImgn7bcYJsJWo86nOYKaTVazn1JZw2YYS5YjnDS6Y_pUvrjJkAhwcdnBEjPBChcu0rNijmSipnd2jngge2B_9p7ExX-GFaI2g4lvo6AMX6jlSYypqoV5E4oik5nWnTkgrLqPYotAELvd04W0iajNKbyIJdwY0GsazWGCC165QrfeKPugGD-m9euiWFm-P3LdD83EKthqpaQY2bXd41UeS7WpS43OyoRyb-Ve1zfA_f7wU7SvXS9aOny7w3luJEvGruK4bBgiaiUMHEYctCUmi4P2-3WNYAUD76TwndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c304583c30.mp4?token=VAg5SgLP_NyCGhjloxJPwZSuHcdbWVJLjDHdxMhnd0ysfNkImgn7bcYJsJWo86nOYKaTVazn1JZw2YYS5YjnDS6Y_pUvrjJkAhwcdnBEjPBChcu0rNijmSipnd2jngge2B_9p7ExX-GFaI2g4lvo6AMX6jlSYypqoV5E4oik5nWnTkgrLqPYotAELvd04W0iajNKbyIJdwY0GsazWGCC165QrfeKPugGD-m9euiWFm-P3LdD83EKthqpaQY2bXd41UeS7WpS43OyoRyb-Ve1zfA_f7wU7SvXS9aOny7w3luJEvGruK4bBgiaiUMHEYctCUmi4P2-3WNYAUD76TwndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظات آغازین اقامه نماز بر پیکر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666767" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666766">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d449de63.mp4?token=F8IwZo601D0TSTAPIapTua4FuTCutKWANjgtgQlfJQWOoyw15IEf3sTdJl1GwSqGF7N-YC8LGHCAmnblpcqDuVKcRfXUetevhKrwGfFWeZFWipm2soorrPkq9_40H7IkROvTdH_T9jTFTO_rzHIqPU_ac52QAMd3OTsA0J04qX8tIKq1rQcaAnsE192MFJemJnF6k7Qa4uKdlzm13A0pAFjbVxy0SvCd96Clro3BlkS1XGXAcnC6ao479ZqnLUhCLf1iDwihzgA7fvWYURnCgq5NNVu98zOns-e4aP-n475JSbTzKqTPkkBeTXsRMgmIq1NnYYwOG_nMB-6duiLAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d449de63.mp4?token=F8IwZo601D0TSTAPIapTua4FuTCutKWANjgtgQlfJQWOoyw15IEf3sTdJl1GwSqGF7N-YC8LGHCAmnblpcqDuVKcRfXUetevhKrwGfFWeZFWipm2soorrPkq9_40H7IkROvTdH_T9jTFTO_rzHIqPU_ac52QAMd3OTsA0J04qX8tIKq1rQcaAnsE192MFJemJnF6k7Qa4uKdlzm13A0pAFjbVxy0SvCd96Clro3BlkS1XGXAcnC6ao479ZqnLUhCLf1iDwihzgA7fvWYURnCgq5NNVu98zOns-e4aP-n475JSbTzKqTPkkBeTXsRMgmIq1NnYYwOG_nMB-6duiLAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های فرزندان رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666766" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666765">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dce749512.mp4?token=KfcbATYf-p7vXzno0NtoIawPOSJyyBFGPRJe3lTIgTRzM93vxlXD8a3_p9uLePbfMkXCArKuH8rhzYN9orP8oOqgrXHwdV39RhykoM1kyvYX74o6Atl_H_FBeo6yzeM82dMlwSJy0xXG1bjzwwFjqhJzT3RqYcISs2vtQPSC7KmBYtSb1YNQawXnFMxs20scjcXyvVBo2esg6DdBVYiDwyyykT_N5wwEziUgWnCDPTTPZ7jfv6XzVQt70tjVt0rmvfV_f9A-6U-rhCa3bJLePPRpgNcpTV970F94IUKXBiQ7EfgwLHfOEeci2PgGo7udYPkBOkl1gDDkIa8gsyXgqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dce749512.mp4?token=KfcbATYf-p7vXzno0NtoIawPOSJyyBFGPRJe3lTIgTRzM93vxlXD8a3_p9uLePbfMkXCArKuH8rhzYN9orP8oOqgrXHwdV39RhykoM1kyvYX74o6Atl_H_FBeo6yzeM82dMlwSJy0xXG1bjzwwFjqhJzT3RqYcISs2vtQPSC7KmBYtSb1YNQawXnFMxs20scjcXyvVBo2esg6DdBVYiDwyyykT_N5wwEziUgWnCDPTTPZ7jfv6XzVQt70tjVt0rmvfV_f9A-6U-rhCa3bJLePPRpgNcpTV970F94IUKXBiQ7EfgwLHfOEeci2PgGo7udYPkBOkl1gDDkIa8gsyXgqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود پیکر نوه رهبر شهید انقلاب به  محل اقامه نماز در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666765" target="_blank">📅 07:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666764">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefc66037.mp4?token=T9-RMA0qmGRYR4gyxUa_t6b2Sz5K1dUpFb1kvot5TMH0njnCQiRJ5Z41K3vSJzSvFOoJZOacDVIAUYjYTszS5--BIoMgD8npdtePAMRTtH1SdmGq4eCdsCzqXjzik7BuljAZE5WS1tQJhM7o1mdizeRfOFpQ1f5EOnHYaRw-m62ppR7rfqnLOgtR_rt7epga_5VJgLr0eAH3TAWO6-a-e7O6pGscOZhqPASzIwgOBjm7HNOgJ_ZhCGKY66OorlFMb-DVxwM55qs3Hfrrar-7CgnhYDEJ57THyBwwzTn8qkV_2dY4_kkmmsS6jE4vh5CmGetPOjbbglKrQwuIUOT0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefc66037.mp4?token=T9-RMA0qmGRYR4gyxUa_t6b2Sz5K1dUpFb1kvot5TMH0njnCQiRJ5Z41K3vSJzSvFOoJZOacDVIAUYjYTszS5--BIoMgD8npdtePAMRTtH1SdmGq4eCdsCzqXjzik7BuljAZE5WS1tQJhM7o1mdizeRfOFpQ1f5EOnHYaRw-m62ppR7rfqnLOgtR_rt7epga_5VJgLr0eAH3TAWO6-a-e7O6pGscOZhqPASzIwgOBjm7HNOgJ_ZhCGKY66OorlFMb-DVxwM55qs3Hfrrar-7CgnhYDEJ57THyBwwzTn8qkV_2dY4_kkmmsS6jE4vh5CmGetPOjbbglKrQwuIUOT0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سران قوا در مصلای امام خمینی(ره) تهران، دقایقی پیش از اقامه نماز بر پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666764" target="_blank">📅 07:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666763">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180ce62363.mp4?token=bhTKKcPG98jxZtkZrBk5NStSmYUFC8Au6FBoEc5xrzGwK68yLT-atlRtWO2lMzbOUdxDVJTcK-xo3inCEtKKb4cwMEsF_YyGmiRii-ucq0IPiioqMflfivMxaR3h64eJ-62960-1Ze26xF6r1pvEG9RP0K6wK6j1qg1EJS0nI2S8uURDGa2waCOkoPSZruRQAe2gaxPIvHmZ7oXCm_DyQVBT2FJ2n1EVf0gf_TsTgoGbcxYe89Y9-qg_R_g4hx-We2ZCbzXUipb5uL55zmxLUFVU_uQdwEoycG5mC4jQKvu-2YL_35QB5sSESdkD4lrKTiBp-Aw9fRYt2MuWbn0nnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180ce62363.mp4?token=bhTKKcPG98jxZtkZrBk5NStSmYUFC8Au6FBoEc5xrzGwK68yLT-atlRtWO2lMzbOUdxDVJTcK-xo3inCEtKKb4cwMEsF_YyGmiRii-ucq0IPiioqMflfivMxaR3h64eJ-62960-1Ze26xF6r1pvEG9RP0K6wK6j1qg1EJS0nI2S8uURDGa2waCOkoPSZruRQAe2gaxPIvHmZ7oXCm_DyQVBT2FJ2n1EVf0gf_TsTgoGbcxYe89Y9-qg_R_g4hx-We2ZCbzXUipb5uL55zmxLUFVU_uQdwEoycG5mC4jQKvu-2YL_35QB5sSESdkD4lrKTiBp-Aw9fRYt2MuWbn0nnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف‌های زائران و نمازگزاران در انتظار اقامه نماز بر پیکر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666763" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666762">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abca84454.mp4?token=jtAc4I8xGC0eVYwViJaYrkHcHXDc6NGBLgi2AEvJ2o3PBjwNu1BP8sDXVeqTmjZ7x1EVaKhZsKDvWPdF4dITeOLfiuNAZVMAjqAfqKDVM4bTZ6GlFUC2aiyrJLan2ftbG55E181kMWdopT95KwIVq2vDSs6Jsl5khwAne6DvdOmpAlTqrnb5-nSMD-2-KAVGfd3RsG1Pvh34OZJUY0YV4JjWaYCcS1QXzkUB7bglofSbo6aLrFvTdgcFX-gXFCDk2fPQFyiQyw7tA3G3bC0HEX8xIJaMO-ASNo7VUE0SGLIa_YDbjDbuRnOMMiscI7Rkk5HnK9BBnoXTYDaaeyW344WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abca84454.mp4?token=jtAc4I8xGC0eVYwViJaYrkHcHXDc6NGBLgi2AEvJ2o3PBjwNu1BP8sDXVeqTmjZ7x1EVaKhZsKDvWPdF4dITeOLfiuNAZVMAjqAfqKDVM4bTZ6GlFUC2aiyrJLan2ftbG55E181kMWdopT95KwIVq2vDSs6Jsl5khwAne6DvdOmpAlTqrnb5-nSMD-2-KAVGfd3RsG1Pvh34OZJUY0YV4JjWaYCcS1QXzkUB7bglofSbo6aLrFvTdgcFX-gXFCDk2fPQFyiQyw7tA3G3bC0HEX8xIJaMO-ASNo7VUE0SGLIa_YDbjDbuRnOMMiscI7Rkk5HnK9BBnoXTYDaaeyW344WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666762" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666761">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b327e2e6f3.mp4?token=DBh3kshayuI8kGpr97ABvFpzYb4GqSxFg-cOjKP0rAtlbSuJsk3-6bBq47iLL-76uD8neN8v68vvjYz2RGv485UOnmgHeq3U0BKc9L-yS0nRJo2ZN79_gP9abnlPYsNUWXX7a97lENc8vvyTJIm_xDHx2RZeyPUPH5DyTPS0qmS3G-V0NynWd8fofQzCTyFi7DXCXOPu4iFkNTrru3c6efYojHH1EN4rhHyBCmk6PVeqHui84ntUMuaaXlVWELuVyWFFipcCytfVuWmAyLGwJil0z7ebscqiKiDSCGePXeIlIm9cJ0BVYvkktl6HKFT7yl3j4of9McaVuz6Iq7hmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b327e2e6f3.mp4?token=DBh3kshayuI8kGpr97ABvFpzYb4GqSxFg-cOjKP0rAtlbSuJsk3-6bBq47iLL-76uD8neN8v68vvjYz2RGv485UOnmgHeq3U0BKc9L-yS0nRJo2ZN79_gP9abnlPYsNUWXX7a97lENc8vvyTJIm_xDHx2RZeyPUPH5DyTPS0qmS3G-V0NynWd8fofQzCTyFi7DXCXOPu4iFkNTrru3c6efYojHH1EN4rhHyBCmk6PVeqHui84ntUMuaaXlVWELuVyWFFipcCytfVuWmAyLGwJil0z7ebscqiKiDSCGePXeIlIm9cJ0BVYvkktl6HKFT7yl3j4of9McaVuz6Iq7hmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود پیکر رهبر شهید انقلاب به محل اقامه نماز در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666761" target="_blank">📅 07:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666760">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010d6c2fd5.mp4?token=q888KfcsWZQtwG1TV5jNOgjVtwLj1xg6jY1OnTkD13Ag_whVCPVMrqyrsZda8U3BW41THL683gkb2zB1yu-JenNQlIxAgHsylQ4--Gb3OJ8XL1lE1-P8rIL6JSP8jWRgE56YjZz3j3gGmjMP4tTJfpuwoUEjIo3ABB6pzqk3hLK--76QTa4N138fWppZ9IFBvvDg7qewQz5fczxPHbA2zGx6EQjeDmq8SB-38hwkuZZdC6uhK7UbetvGauxOj42MH8xVqvSaqR_4MLV-DYjjdZ95tcmBlKNT1oYu-KGzHsW61-9ycjPlpqMBSYdgDXkvs4bhBUGCpHsXYKC47YDSnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010d6c2fd5.mp4?token=q888KfcsWZQtwG1TV5jNOgjVtwLj1xg6jY1OnTkD13Ag_whVCPVMrqyrsZda8U3BW41THL683gkb2zB1yu-JenNQlIxAgHsylQ4--Gb3OJ8XL1lE1-P8rIL6JSP8jWRgE56YjZz3j3gGmjMP4tTJfpuwoUEjIo3ABB6pzqk3hLK--76QTa4N138fWppZ9IFBvvDg7qewQz5fczxPHbA2zGx6EQjeDmq8SB-38hwkuZZdC6uhK7UbetvGauxOj42MH8xVqvSaqR_4MLV-DYjjdZ95tcmBlKNT1oYu-KGzHsW61-9ycjPlpqMBSYdgDXkvs4bhBUGCpHsXYKC47YDSnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مسعود پزشکیان، رئیس جمهور اسلامی ایران و دیگر مقامات دولتی در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666760" target="_blank">📅 07:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666759">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d88392f71.mp4?token=BtdRXlomiNxUzABu1eD50GfGygYCJ6B8benFDrAmxucON-5sxBuUWqdj6AZV-NwX-0ox_KjjalE2FsdmNY9bKm2d9IiC8JpdA9UcFyWhmpmaGDSgbqn8Db9x3kfolu9u79YFYIzZ_9NXIXrjYklgh2gqIi989EpSKek1ijzdtrZUEpO9KsWR81ptbB9irmoGHDoiI6u_oVNEIYiw_RMidHoZuPn6rBCyaYScLwy5O-7683lXWLjJyZIkyEVZZuWap8ysnVBNavPJc1HNncE8uFZ1LbzZ2pm0LUpWgUtgRngM84wGXpsBvAGtLYOpNyJQpIO9FiH3eIw8vfUDhGbH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d88392f71.mp4?token=BtdRXlomiNxUzABu1eD50GfGygYCJ6B8benFDrAmxucON-5sxBuUWqdj6AZV-NwX-0ox_KjjalE2FsdmNY9bKm2d9IiC8JpdA9UcFyWhmpmaGDSgbqn8Db9x3kfolu9u79YFYIzZ_9NXIXrjYklgh2gqIi989EpSKek1ijzdtrZUEpO9KsWR81ptbB9irmoGHDoiI6u_oVNEIYiw_RMidHoZuPn6rBCyaYScLwy5O-7683lXWLjJyZIkyEVZZuWap8ysnVBNavPJc1HNncE8uFZ1LbzZ2pm0LUpWgUtgRngM84wGXpsBvAGtLYOpNyJQpIO9FiH3eIw8vfUDhGbH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزندان رهبر شهید انقلاب در مصلی تهران پیش از اقامه نماز بر پیکر امام امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666759" target="_blank">📅 07:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666758">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5371ddc0c2.mp4?token=syySn7wsEgnGzvNg3PPSM7tIZj_iXOZu6SGdVU_kf56pucUDq0ip2bkPA58WRkkCLITldtTb3Vs_Z8Wu-6iYJ6O4op3oUh5IgXVHO2VHLt7TQzDnNa8usvYmsraihl8-Azi2RDNh_gb9F-z5I0k1VYvFE5U53a707QaJZ8d48O9WYbFOUobTgjtF1T20oK2NqKKq7zZHVJc-8wZ4-GtI9QZw35yTwyahBiFxtV7fIc33VP-UyhgEMHAekDnKJhYPNS4dD6Idtc3haY9joA2-EBiJAchEfSxE84SwHMWWKikCj-F7pI2ad3CwvoEQZc10XIOggl4fM4k-BNy5_jcsu5pCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5371ddc0c2.mp4?token=syySn7wsEgnGzvNg3PPSM7tIZj_iXOZu6SGdVU_kf56pucUDq0ip2bkPA58WRkkCLITldtTb3Vs_Z8Wu-6iYJ6O4op3oUh5IgXVHO2VHLt7TQzDnNa8usvYmsraihl8-Azi2RDNh_gb9F-z5I0k1VYvFE5U53a707QaJZ8d48O9WYbFOUobTgjtF1T20oK2NqKKq7zZHVJc-8wZ4-GtI9QZw35yTwyahBiFxtV7fIc33VP-UyhgEMHAekDnKJhYPNS4dD6Idtc3haY9joA2-EBiJAchEfSxE84SwHMWWKikCj-F7pI2ad3CwvoEQZc10XIOggl4fM4k-BNy5_jcsu5pCypY0vL-Wxhp_lT_M815KTFSLUcWVnBRp37yICAfqgsUk2mT0sVFDNQjnW3shDKKcvC84XZEK4U_g3vjgcCBKva-YFO5HOOEiVlChnMtC4uayBayMKSSlOKc535nQYsjp7tMZErkPtspEhvsAhPhJi8KRVPb4D9WssMq2_6QmVEIAPzU7xeSqzwPGQKZ8Sk9CIernbYTksljOpXrputdKsPmZgDTGPqRLrzid9hf-4IvYYs_822_FektG8hTpfgqK5eNjU2JLUjFyEfPaBfR8zdMX69wlwvXIqWnBpsX49nq_7gqHAYpoiE1bYcpgx0ZqmeZL5gP5aHHqWef0iy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در روح و جان من می‌مانی ای وطن...
🔹
لحظاتی از روضه‌خوانی حاج محمود کریمی در مصلی امام خمینی(ره) تهران، دقایقی پیش از اقامه نماز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666758" target="_blank">📅 07:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666757">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اعزام اتوبوس به مصلی در پی ازدحام ایستگاه‌های مترو
شرکت بهره‌برداری متروی تهران:
🔹
به دنبال ازدحام جمعیت در ایستگاه‌های تقاطعی امام خمینی(ره) و تئاتر شهر، از شرکت واحد اتوبوسرانی درخواست کردیم اتوبوس اعزام کند و در حال حاضر اتوبوس‌ها مسافران را به مصلی منتقل می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666757" target="_blank">📅 07:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666756">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3693a04af8.mp4?token=EshrmLjpMbNK7j_XR9UCqTwvjBxDIgmgflFuOedCEFztqXJleq-EGJrDds_MK3R0cpXIeqHU_bmkLTW8VSVKs3lrdZKcdC091qMn-DQ__3CmojQCMFc_QXnjaKX5k8Z9oggJQpeuxh2tPPm8zQWJBUbiOC-O98SRgbP-ZDpu684I9ypDeTiaL6YHg7Qb51e_b82PprA-Mi5lInrnrTekoZpji1Ln9Vtq3h4qlbZlTxPl1VrkjG6jTBXCJOY0Fhs4OjhkWzowOAj3faI1ZY8LxOORL5hdVMim0kuakE0nv1nK7Tq9O9Ofh9fs3RQRgIFMsosHVTMMZGu04dV-WMTngzmA5XT4B60fcufu5gqh8gE4eFDiLQ9coLKoCzzt1tTpxna6C-AucN2qWkwLqSmBZ6Rn260ZO0ZP6-d9JqX6P5fxEkssftpGd_DtCpmp1srobY4NqjQEIjxu-fNEHAX5jpGk590BtmGgZ5bRqO16c3C0XGhX6--h-JbfPCWRh4cPd5BMjGGVpbmUdsb-a8yqeTvhHwy-vk5nIQY9SGUeTXY8Jh8jrLp_tGX3YTWy2GC1MHttIMpeOzexoGswKXrZ_6CfTIcnenZ37K_YTcSzJ27X1Loe1__NW945HRvZ9zowKyDGEIlf62NuY2XPOb4lSTaSCE2ERyHAK8xBEONwVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3693a04af8.mp4?token=EshrmLjpMbNK7j_XR9UCqTwvjBxDIgmgflFuOedCEFztqXJleq-EGJrDds_MK3R0cpXIeqHU_bmkLTW8VSVKs3lrdZKcdC091qMn-DQ__3CmojQCMFc_QXnjaKX5k8Z9oggJQpeuxh2tPPm8zQWJBUbiOC-O98SRgbP-ZDpu684I9ypDeTiaL6YHg7Qb51e_b82PprA-Mi5lInrnrTekoZpji1Ln9Vtq3h4qlbZlTxPl1VrkjG6jTBXCJOY0Fhs4OjhkWzowOAj3faI1ZY8LxOORL5hdVMim0kuakE0nv1nK7Tq9O9Ofh9fs3RQRgIFMsosHVTMMZGu04dV-WMTngzmA5XT4B60fcufu5gqh8gE4eFDiLQ9coLKoCzzt1tTpxna6C-AucN2qWkwLqSmBZ6Rn260ZO0ZP6-d9JqX6P5fxEkssftpGd_DtCpmp1srobY4NqjQEIjxu-fNEHAX5jpGk590BtmGgZ5bRqO16c3C0XGhX6--h-JbfPCWRh4cPd5BMjGGVpbmUdsb-a8yqeTvhHwy-vk5nIQY9SGUeTXY8Jh8jrLp_tGX3YTWy2GC1MHttIMpeOzexoGswKXrZ_6CfTIcnenZ37K_YTcSzJ27X1Loe1__NW945HRvZ9zowKyDGEIlf62NuY2XPOb4lSTaSCE2ERyHAK8xBEONwVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلای امام خمینی(ره) و خیل مشتاقان در آخرین دقایق مانده به اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666756" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666755">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d028f24cd.mp4?token=aCfJwEZjOVUUevyJA0xZa7epH7dd4_vLcufse45hP8SFKithy9XN96_rNgKANsW66aQIBBbmBsZORANPTEn24c-pfr6t9VW1vK7M-VUQs-TNy-lfk4-7S3Avfqowh_M4HsvaxxCVdbu79tTEWtsksNCtZsm0o25E6AZvvLahwUQfL9iXdmpHrhydIbyDGfmwHETvia46z-89EQYM238jeY9w6ic56MulJYM38b4F-jChcaSXzOivIge6kAxC3xw_kMfPUG-rDw8F6BGDwSEedXnOABODG0iVn6p70OoMQeUgnKDGgr0KiHU7SHXAIbKm2QD7LxNsTDSxeu4_unmsIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d028f24cd.mp4?token=aCfJwEZjOVUUevyJA0xZa7epH7dd4_vLcufse45hP8SFKithy9XN96_rNgKANsW66aQIBBbmBsZORANPTEn24c-pfr6t9VW1vK7M-VUQs-TNy-lfk4-7S3Avfqowh_M4HsvaxxCVdbu79tTEWtsksNCtZsm0o25E6AZvvLahwUQfL9iXdmpHrhydIbyDGfmwHETvia46z-89EQYM238jeY9w6ic56MulJYM38b4F-jChcaSXzOivIge6kAxC3xw_kMfPUG-rDw8F6BGDwSEedXnOABODG0iVn6p70OoMQeUgnKDGgr0KiHU7SHXAIbKm2QD7LxNsTDSxeu4_unmsIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت مردم عزادار به سمت مصلی برای اقامه نماز بر پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666755" target="_blank">📅 07:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666754">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b5a279ca.mp4?token=CKQl4-SVgc0OfORaPijKQ4hu3n6FW5IvSQR9G2io0pb4bluL17pdXq-MLlSoXJD-q89VfCw21S6SJxWlW3sGBDxtPNZox7rA-Ubozf_Sq-u82aoETMRpKwL7hXQedDziCIK2GVpJmALU18YVgxzoej1eCMLtEgL6nD3FUoCX-7jRWky8mSLYRXEkwbm8RQLGBTB_NhEbBhGFHNFxzAmLPLzHfKsYD4pYF_BrLoacNPWXdaGiTuzDcBUYYnoIXLhxacLL3DVygjj_je_c-HGss-cxojSQTFB2kfKwzv5Xg7mdIHhBeG2WT-KodPabPDtwrfWo5lco9BdTSjvezV-o9A_WwyCWxHQAQktrqOXm8viXNGbW1FHwHOlb9A6J7X9vd90hj4z9IUhnE7sAYjVW0ns3SVib5sWjdyFb6yOVdAw85Qh70LI5ORVbKEDBQiHAZDKbcvH9_n0rjRSo1WUPGCOxIhtHp8fx1HKt10suPvY3Z10x-TkvrN2zLGwQ3-q1dBDXsxE7s6RtZWDv539ab3tcpyaVNMpb0iKo_FyEH2KHcehHkYKgeFL8STZnYRwiXxracozFz8Ef74-5UE0QMd3zKKcYv-j-Jpdx4Clbnu90OfEjY8DAojkmDaoUXJtR2B_f2bHrWyZnrf3xKS1jl_JF2LGKfpZBzHSWZH1K-Do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b5a279ca.mp4?token=CKQl4-SVgc0OfORaPijKQ4hu3n6FW5IvSQR9G2io0pb4bluL17pdXq-MLlSoXJD-q89VfCw21S6SJxWlW3sGBDxtPNZox7rA-Ubozf_Sq-u82aoETMRpKwL7hXQedDziCIK2GVpJmALU18YVgxzoej1eCMLtEgL6nD3FUoCX-7jRWky8mSLYRXEkwbm8RQLGBTB_NhEbBhGFHNFxzAmLPLzHfKsYD4pYF_BrLoacNPWXdaGiTuzDcBUYYnoIXLhxacLL3DVygjj_je_c-HGss-cxojSQTFB2kfKwzv5Xg7mdIHhBeG2WT-KodPabPDtwrfWo5lco9BdTSjvezV-o9A_WwyCWxHQAQktrqOXm8viXNGbW1FHwHOlb9A6J7X9vd90hj4z9IUhnE7sAYjVW0ns3SVib5sWjdyFb6yOVdAw85Qh70LI5ORVbKEDBQiHAZDKbcvH9_n0rjRSo1WUPGCOxIhtHp8fx1HKt10suPvY3Z10x-TkvrN2zLGwQ3-q1dBDXsxE7s6RtZWDv539ab3tcpyaVNMpb0iKo_FyEH2KHcehHkYKgeFL8STZnYRwiXxracozFz8Ef74-5UE0QMd3zKKcYv-j-Jpdx4Clbnu90OfEjY8DAojkmDaoUXJtR2B_f2bHrWyZnrf3xKS1jl_JF2LGKfpZBzHSWZH1K-Do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عهدنامۀ مردم با رهبر شهید در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666754" target="_blank">📅 07:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666753">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c7afbeb8.mp4?token=hPtCZ5v2CGrRpmfliwiXz4lXojrjLfAjP0vz4fDEQZ7smvozFXbIk3ufkQl2YDTyZBE2z5cp6wCwZlhc-PeNIrDZeVPwOgT-l2xYEE4H1nygNLB7G459XbRFaNXMQJildw9yhGRafpxhOAMDVAYejoWU4Yr3a0j9ognhabjymYb-YMYYANWiPAew9r8ZmZ-rccKM6uUHyqm8IiY40O3vwpsFimAHEqsVMcByHn4J6pLUbmoJS7cw0YUQLxRBdbo387kd3ECOkZkjPuepjD0B021T5OXQqS5e7HNAHExA4pxXonC1d9ua_fJCBAb_GBlnZ5OdKdI3y7F6slkYJzl9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c7afbeb8.mp4?token=hPtCZ5v2CGrRpmfliwiXz4lXojrjLfAjP0vz4fDEQZ7smvozFXbIk3ufkQl2YDTyZBE2z5cp6wCwZlhc-PeNIrDZeVPwOgT-l2xYEE4H1nygNLB7G459XbRFaNXMQJildw9yhGRafpxhOAMDVAYejoWU4Yr3a0j9ognhabjymYb-YMYYANWiPAew9r8ZmZ-rccKM6uUHyqm8IiY40O3vwpsFimAHEqsVMcByHn4J6pLUbmoJS7cw0YUQLxRBdbo387kd3ECOkZkjPuepjD0B021T5OXQqS5e7HNAHExA4pxXonC1d9ua_fJCBAb_GBlnZ5OdKdI3y7F6slkYJzl9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یمنی‌ها با فریاد الموت اسرائیل وارد مصلی شدند
🔹
دقایقی پیش گروهی از یمنی‌ها با فریادهای «الموت اسرائیل» وارد صحن اصلی مصلی تهران شدند تا در مراسم وداع با پیکر رهبر شهید ایران شرکت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666753" target="_blank">📅 07:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666752">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797d09ecaa.mp4?token=uUicUKvau5E2P9xwxEyfVi_gBU_-K58JEwXOmotCeampmtG47jECPitzY35jcms8_JpN8jDCTiCd6M4kmqqNIMqqiTXLgj-9ZaamPPVkG_6L8quwbjvQdKs2W6jVnitp8s_LlzFuM6CWmbYdoozDat9fw3QK2qUmqRgNE_1to2_vLC3MMSKzcGGrF0aGlnFTqH9yDF4n9DTo-pctRGIZ14oZCvDnxpaun-xK2Eh8nZRLkckjal3YgGYg_I0j1EzaNR3Mirxt6HL6iDDkphwtfoFbY__zjF1PXJzidLVSenHZBN1P2Sg8rBY-aVCyuBrVS1PAG4NLEZ_ubI13E0tUhJ5wY4wKGtLYMjzmSw_cWok2jD8EtsAlv9hhz6NLSSUXCz8mUDu03qUVGDptoFGsvRqQ4lIuWIm-BdkpCVg61aXrqfZdvg5R3I3X5tZnHrudz_HW7pWb3lSjR6vMsmbNBnxWOuULAMUsrXqwCbhwH9hBqKezb63WwXmOeGilYCPXUp6DlOp8afU-qpsVIrD7KYRh4bHhxIPDhvEUE60ZlP3AK5TyP65ZFMrJ8_nS9J_XO5iw8pt1TyBOq83Dwy7DMNaz8KBJdM7F2BGlAgfHa7V22bwIobn8sXJzWDkWRITJb7QF1uSC1BXXnoot0tfhioCTlu20UzlyrNMX79WRPCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797d09ecaa.mp4?token=uUicUKvau5E2P9xwxEyfVi_gBU_-K58JEwXOmotCeampmtG47jECPitzY35jcms8_JpN8jDCTiCd6M4kmqqNIMqqiTXLgj-9ZaamPPVkG_6L8quwbjvQdKs2W6jVnitp8s_LlzFuM6CWmbYdoozDat9fw3QK2qUmqRgNE_1to2_vLC3MMSKzcGGrF0aGlnFTqH9yDF4n9DTo-pctRGIZ14oZCvDnxpaun-xK2Eh8nZRLkckjal3YgGYg_I0j1EzaNR3Mirxt6HL6iDDkphwtfoFbY__zjF1PXJzidLVSenHZBN1P2Sg8rBY-aVCyuBrVS1PAG4NLEZ_ubI13E0tUhJ5wY4wKGtLYMjzmSw_cWok2jD8EtsAlv9hhz6NLSSUXCz8mUDu03qUVGDptoFGsvRqQ4lIuWIm-BdkpCVg61aXrqfZdvg5R3I3X5tZnHrudz_HW7pWb3lSjR6vMsmbNBnxWOuULAMUsrXqwCbhwH9hBqKezb63WwXmOeGilYCPXUp6DlOp8afU-qpsVIrD7KYRh4bHhxIPDhvEUE60ZlP3AK5TyP65ZFMrJ8_nS9J_XO5iw8pt1TyBOq83Dwy7DMNaz8KBJdM7F2BGlAgfHa7V22bwIobn8sXJzWDkWRITJb7QF1uSC1BXXnoot0tfhioCTlu20UzlyrNMX79WRPCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیان احکام مربوط به نماز میت در مصلای امام خمینی(ره)، ساعاتی پیش از اقامه نماز بر پیکر رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666752" target="_blank">📅 07:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666751">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36694e80fb.mp4?token=eojOVcw5_wUmu2bnXab92fBqwK1naC9bYfC1sApvIg-pi5Bdi-Hzl3AnxZuEAMXch4pfmHTnBUJUdz2Yy5Khd13X-in-gWAZu8MVd9rLGetH69i3I4YnKQOhjXst2K6wIW5WDr5sXYcI1v8gPPjqWn6eMhfstvfMYU4rf3D9dk0zNZKxuN9hu9lOQWtquCgGLEUHGhdSzeg_berN5BBpMidWm1fnzb4y-6Ze57kzywxm0NGAPWQnY4nvfY9zBgUR8o5bvuUaUzMqIB7I1HOE2M76gdAMAbPmkuve1Kpbf7-75qB3IPZtZw2KEhvleDZyYMKJ4n8Ncq4FYfLZsXl-pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36694e80fb.mp4?token=eojOVcw5_wUmu2bnXab92fBqwK1naC9bYfC1sApvIg-pi5Bdi-Hzl3AnxZuEAMXch4pfmHTnBUJUdz2Yy5Khd13X-in-gWAZu8MVd9rLGetH69i3I4YnKQOhjXst2K6wIW5WDr5sXYcI1v8gPPjqWn6eMhfstvfMYU4rf3D9dk0zNZKxuN9hu9lOQWtquCgGLEUHGhdSzeg_berN5BBpMidWm1fnzb4y-6Ze57kzywxm0NGAPWQnY4nvfY9zBgUR8o5bvuUaUzMqIB7I1HOE2M76gdAMAbPmkuve1Kpbf7-75qB3IPZtZw2KEhvleDZyYMKJ4n8Ncq4FYfLZsXl-pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در مصلی با سلام نظامی سرود ملی را خواندند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666751" target="_blank">📅 07:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe180104b.mp4?token=YH3sRr1PYb7IN8I_8Zxz0tBofjoMdL9e1BSwi-Udf8vfpm-g9kkA16vyGDHv-PEbaFWYt2gSO8KUvC5NSgc--ACrpsaX5EYuA3P7jyTzTdqlJuOw4XJmLIDwJ-1ZRqIqkgzRCjl6FfcFURkLQn6jUq-8Zze2rh5qZazz7Zj5Jzu8wWkYiRv7IDCN1M8W2QdImA-eI9XjUrwSW0f1rA6kjy9WuqqXmzGoktIMwkwah9ytTA08E3ySLowKLzuWc54gsCbN-3eAjn2YdExGu30OKUszA11QYq1RTxvIs9fXHCSCu2b10hhkWPiW8a4KF6yeJc_Z4fH4CxnosMdCkxRSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe180104b.mp4?token=YH3sRr1PYb7IN8I_8Zxz0tBofjoMdL9e1BSwi-Udf8vfpm-g9kkA16vyGDHv-PEbaFWYt2gSO8KUvC5NSgc--ACrpsaX5EYuA3P7jyTzTdqlJuOw4XJmLIDwJ-1ZRqIqkgzRCjl6FfcFURkLQn6jUq-8Zze2rh5qZazz7Zj5Jzu8wWkYiRv7IDCN1M8W2QdImA-eI9XjUrwSW0f1rA6kjy9WuqqXmzGoktIMwkwah9ytTA08E3ySLowKLzuWc54gsCbN-3eAjn2YdExGu30OKUszA11QYq1RTxvIs9fXHCSCu2b10hhkWPiW8a4KF6yeJc_Z4fH4CxnosMdCkxRSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر چه در دل ما داغ آتشینت هست
هزار شکر که امروز جانشینت هست
🔹
لحظاتی از شعرخوانی محمد رسولی در مصلا، ساعتی پیش از اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666750" target="_blank">📅 07:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aada24811.mp4?token=KFslWchhmJ3Pzc1E_VWTN2-j0adUnV2VLD8B2TWh7R45xbNMcWzZ-hORtaJnbnxnJe1D-UNuR2hefshpF88HVcaSJlBOTTqmrl5xLaoBAMNLZ3XbibA_fDZzaFEzDQEhg8IytuRBVSy8zE0qw_HpNxQ2D_qRH7A1-riZ8KXfYPW6MikXFVcgvbnL6iG4mkMvCWFVbg-17sMF9E41BKkBiflZ-07QAG1S1tINf0Evp09nLMxjvLiyYcI6riuUZ5RKZUerU3b9OA5XazKgnJFES-_A2eWgMjWPdCFYIjrxLc0dJVrRVX6FKvBi5JhD9OdRgBRakwZDIpk2-hZf3lw6bDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aada24811.mp4?token=KFslWchhmJ3Pzc1E_VWTN2-j0adUnV2VLD8B2TWh7R45xbNMcWzZ-hORtaJnbnxnJe1D-UNuR2hefshpF88HVcaSJlBOTTqmrl5xLaoBAMNLZ3XbibA_fDZzaFEzDQEhg8IytuRBVSy8zE0qw_HpNxQ2D_qRH7A1-riZ8KXfYPW6MikXFVcgvbnL6iG4mkMvCWFVbg-17sMF9E41BKkBiflZ-07QAG1S1tINf0Evp09nLMxjvLiyYcI6riuUZ5RKZUerU3b9OA5XazKgnJFES-_A2eWgMjWPdCFYIjrxLc0dJVrRVX6FKvBi5JhD9OdRgBRakwZDIpk2-hZf3lw6bDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادت ما این بود که در نمازهای مصلی، پشت سرتان صف ببندیم، نه روبرویتان؛ ای مقتدای شهید
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666749" target="_blank">📅 07:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666747">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd41cf86cc.mp4?token=OukrIKMe0rzZSW1yFol5SpxcsyeQspDRTQ73-EkCORd2Jp7Sj5sF0SDAQvjKyOxxWLxLgShEYDhfPRx3WmRArT76yYGFlKvqiEDoa0k4EVKsJfdIb8x5-zwpFICcZj4efE183GNrH1zI8UmYjogWgPPPJwyY-sfiuHhVU90zvKa8V9oRqiA62tbeTyMxTsD3TLMjoO9NbHM70EacFT3AHOUtHYyY76svTXaUJjFocchiok8DMuYndjyWE4eUqENwI49iui8NhL9CybEab3GZ8Jv_x5992G66X-zUuoRZICo7UwWPSX7iOebIGXuz3BF64qWZKdKLR-eCfekHjjP1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd41cf86cc.mp4?token=OukrIKMe0rzZSW1yFol5SpxcsyeQspDRTQ73-EkCORd2Jp7Sj5sF0SDAQvjKyOxxWLxLgShEYDhfPRx3WmRArT76yYGFlKvqiEDoa0k4EVKsJfdIb8x5-zwpFICcZj4efE183GNrH1zI8UmYjogWgPPPJwyY-sfiuHhVU90zvKa8V9oRqiA62tbeTyMxTsD3TLMjoO9NbHM70EacFT3AHOUtHYyY76svTXaUJjFocchiok8DMuYndjyWE4eUqENwI49iui8NhL9CybEab3GZ8Jv_x5992G66X-zUuoRZICo7UwWPSX7iOebIGXuz3BF64qWZKdKLR-eCfekHjjP1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ جزیره کودک‌خوران چرا زنده است
از این پس جهان جای این نجاست نیست
جهان نگاه کند، تیغ انتقام اینجا است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666747" target="_blank">📅 07:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666746">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keJS8lqiOxkCkt3HVDBmGkmH0RpGizMLY9cIVThWuEsUAazHrA8y5riaYB5lKzAp8EIAKuRuXGakFq8LxCraSpUsa1ReqvrJSQQNwMVhNGQ5fUktvmi6E9THIlXUO6Idk5rYVFDdrGjjEUTC7ZsiC_Oq-xBuyJdNnezV1GPkaQu1HyV_1cgiaC02he5GzbhhzAaWFQKb_xirUCyIIPWm5-nXAj6oix3AvPVPX6w_olYZUkwYdldNm16uc4BcS2euzNNtzx1I0uApgKiK7W27mzliyehMRLWinFuVPUB1jd7GW_akJpD0iYS2KHN5uo1-TPXQVLDHDsyoQo4W9SvdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۴ تیر ماه
۲۰ محرم ۱۴۴۸
۵ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666746" target="_blank">📅 07:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666745">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
درهای شرقی مصلای امام خمینی(ره) بسته شد
🔹
با توجه ازدحام جمعیت، درهای شرقی مصلای امام خمینی(ره) تهران بسته شده و زوار برای اتصال اقامۀ نماز بر پیکر امام شهید انقلاب اسلامی و خانوادۀ ایشان باید به درب‌های شمالی مراجعه کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666745" target="_blank">📅 07:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666744">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdf8c8e0f.mp4?token=IPXGoYWryVoAJ71n-EnigceJTtj9JqkfWXPIuZyKM5PejR-ILpUNFyokuUXE_J5SWQkGoh40v9WgsPDXALFeIrAjDphL0wqR1bbolGb26gZL5_dsMdLq_QFoZOVUwuz_zUoNNOdqxAP3Zda5cA76IxfbHH3zY5_7U8A-1m49-tNoddP80r0gkTgeWzJmCxjNDEukZ2AWLPet8JVSMJ7Xd9boddLNJzCLZUH-_3rMl1Mry8_ci5DGIJyRck-Sv3zF4t7gOCL1YK-iGqHqHoWR1mgsM_CgDwwx8YUMWOE6HGpzoIPx8laqV65bbFvyYgnzXW4WLmYXSKHG5HnPMpCqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdf8c8e0f.mp4?token=IPXGoYWryVoAJ71n-EnigceJTtj9JqkfWXPIuZyKM5PejR-ILpUNFyokuUXE_J5SWQkGoh40v9WgsPDXALFeIrAjDphL0wqR1bbolGb26gZL5_dsMdLq_QFoZOVUwuz_zUoNNOdqxAP3Zda5cA76IxfbHH3zY5_7U8A-1m49-tNoddP80r0gkTgeWzJmCxjNDEukZ2AWLPet8JVSMJ7Xd9boddLNJzCLZUH-_3rMl1Mry8_ci5DGIJyRck-Sv3zF4t7gOCL1YK-iGqHqHoWR1mgsM_CgDwwx8YUMWOE6HGpzoIPx8laqV65bbFvyYgnzXW4WLmYXSKHG5HnPMpCqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار «حیدر حیدر» مردم عزادار، ساعتی پیش از اقامه نماز بر پیکر «آقای شهید ایران»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666744" target="_blank">📅 07:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666743">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
محل استقرار بانوان و آقایان برای اقامه نماز بر پیکر رهبر شهید
🔹
خیابان قنبرزاده تا تقاطع خرمشهر و خود خرمشهر تا خیابان هویزه محل حضور آقایان و خیابان قنبرزاده بالای خیابان خرمشهر تا بزرگراه شهید سلیمانی محل حضور خواهران برای اقامه نماز بر پیکر رهبر شهید خواهد بود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666743" target="_blank">📅 07:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666742">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3360e3fc93.mp4?token=Mfn3Da_inxRmgjYZ_UhzyKSumXjeNl2xkVMm94k-05f8-ZTqknm-eeVTaSkq5nQKeekYb-hO3mmeQnlcy1bFkvse0hKFVD3qEU0QwD1yUJabSaoFm425uK5WJQNMGt9YM2QSRfkVQcwKeBv0ITQ5paPDeCf2Ns1IqI36gZv2C7uCZjF6MrBz80T_uOsd8cw58Za8uKqCVOANTuAWuKOf3wNsdquW82LOkz2bHqSFNnHo6L9IPBC97o4u70E4yiU97JmcUMB5RrWOSnIg35ek5LN40n3WBxSeOg7K5U5sh1mA7ZUYv0HipriDPD7QQKEaYGMzGSnPYO0DLzDi7YVDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3360e3fc93.mp4?token=Mfn3Da_inxRmgjYZ_UhzyKSumXjeNl2xkVMm94k-05f8-ZTqknm-eeVTaSkq5nQKeekYb-hO3mmeQnlcy1bFkvse0hKFVD3qEU0QwD1yUJabSaoFm425uK5WJQNMGt9YM2QSRfkVQcwKeBv0ITQ5paPDeCf2Ns1IqI36gZv2C7uCZjF6MrBz80T_uOsd8cw58Za8uKqCVOANTuAWuKOf3wNsdquW82LOkz2bHqSFNnHo6L9IPBC97o4u70E4yiU97JmcUMB5RrWOSnIg35ek5LN40n3WBxSeOg7K5U5sh1mA7ZUYv0HipriDPD7QQKEaYGMzGSnPYO0DLzDi7YVDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نه سازش نه تسلیم انتقام انتقام
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666742" target="_blank">📅 07:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666741">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پیگیری جدی ایران برای توقف جنگ و پایان اشغالگری در لبنان
🔹
وزیر امور خارجه در دیدار با هیئت حزب‌الله، بر تعهد ایران به خاتمه جنگ و پایان اشغالگری در لبنان تأکید کرد؛ نماینده حزب‌الله نیز از حمایت‌های دیپلماتیک و دفاعی جمهوری اسلامی از تمامیت ارضی و حاکمیت ملی لبنان قدردانی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666741" target="_blank">📅 07:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666740">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bee3eda96.mp4?token=H5BMHNeptfGQ7V4rEZkI3w_NfI-GuQcYfAK6Zk5S4B9TiIOe_TuaT_bf99DPvoWgzs-YfrDY56YEMPLnlzaun0ySICJuqe6VafpMmKu2WPFaYxBwKYCDWsNgtSKHAE9efoNXLGWhUlyvbMPPhoHJoLEYYCJy3SL8sPLooJ9pTXLU0hDGPkn_qzeDkwVUQS_ZZrrwQ8i7VzDIoH1c4iGjY4xhooWAiCzfus6c3UwveklxbfcuK7RLPMJIPRr0nV5iq8m8e_XTkrKtz9zGS9CmuJ_03-0iiqIWyov_Q_u7knAayKrbbpj_8W3rWa2P6v44vAxoMwFJVWL-C6FG7dUDEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bee3eda96.mp4?token=H5BMHNeptfGQ7V4rEZkI3w_NfI-GuQcYfAK6Zk5S4B9TiIOe_TuaT_bf99DPvoWgzs-YfrDY56YEMPLnlzaun0ySICJuqe6VafpMmKu2WPFaYxBwKYCDWsNgtSKHAE9efoNXLGWhUlyvbMPPhoHJoLEYYCJy3SL8sPLooJ9pTXLU0hDGPkn_qzeDkwVUQS_ZZrrwQ8i7VzDIoH1c4iGjY4xhooWAiCzfus6c3UwveklxbfcuK7RLPMJIPRr0nV5iq8m8e_XTkrKtz9zGS9CmuJ_03-0iiqIWyov_Q_u7knAayKrbbpj_8W3rWa2P6v44vAxoMwFJVWL-C6FG7dUDEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسم به خون تو، قتل ترامپ گردن ماست...
🔹
کسی که کشت امام مرا چرا نکشیم ؛که ننگ ماست اگر قاتل تو را نکشیم
🔹
از این به بعد کفن، جای جامه بر تن ماست ؛قسم به خون تو، قتل ترامپ گردن ماست
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666740" target="_blank">📅 07:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7778f0f55d.mp4?token=cnHXbfI0B_nImBWZ4rpNGEy-D1tMLIcTfS58ibvUaLkhBq7GXErVMKI8ox2c4dVw6mbK-w0jlduEYlpxZmKUPbouAQri6dlFMvV2-r38frEXjzXs3cJnYymKse5vKegqqYtX1KUfuQl-qj2L3kiGnhWSV6x6P2fM2a9UEZ3O5wGQdJUhFdC540qTpuDjCjvbxqa_vFIQPmqhPtZHwko7_qsQcyFyRobWc5I8uN85G_tQGl6FJNQ1aLaYQozvPsqqt1kLNW0pxrxMrqLQLTdGshCscJMfCzT8UJkuIJUA3kmiZzjyDSIoP8aiR2hevECL1GqQ4R9gFgSE9AXiRozQpkdLpBVpROSLSVJOwIFEC3U6pqhpIq11Mn1hi53lFQeBtJcG7IvScUo7Xx4fN13Tda7y8YlDx7jgX-GbR-zoHjP1rkkdT4jkHv3hwtV-0AAH1B-7-fdlHMQmroj1m9-RrXUhvF79iDBPBv4TXaoHZBR71hAffI-IGmQoRYS4t4RmwVGgVKgZdGw2eUGp2hicqGgAxq7KG5NelD7N5CZKX81NEM7K4V67eiOjGrvmWlCqcO3Ws7Aevar8SWXvU_wTDUpl9BJXF8bM22QTmOw8Q8MjVmhz3iKHxAsYzoeQigWbvVksAmWe2xcW9eR7TUu1ty1_e2G2iVmEjSfeR46JyUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7778f0f55d.mp4?token=cnHXbfI0B_nImBWZ4rpNGEy-D1tMLIcTfS58ibvUaLkhBq7GXErVMKI8ox2c4dVw6mbK-w0jlduEYlpxZmKUPbouAQri6dlFMvV2-r38frEXjzXs3cJnYymKse5vKegqqYtX1KUfuQl-qj2L3kiGnhWSV6x6P2fM2a9UEZ3O5wGQdJUhFdC540qTpuDjCjvbxqa_vFIQPmqhPtZHwko7_qsQcyFyRobWc5I8uN85G_tQGl6FJNQ1aLaYQozvPsqqt1kLNW0pxrxMrqLQLTdGshCscJMfCzT8UJkuIJUA3kmiZzjyDSIoP8aiR2hevECL1GqQ4R9gFgSE9AXiRozQpkdLpBVpROSLSVJOwIFEC3U6pqhpIq11Mn1hi53lFQeBtJcG7IvScUo7Xx4fN13Tda7y8YlDx7jgX-GbR-zoHjP1rkkdT4jkHv3hwtV-0AAH1B-7-fdlHMQmroj1m9-RrXUhvF79iDBPBv4TXaoHZBR71hAffI-IGmQoRYS4t4RmwVGgVKgZdGw2eUGp2hicqGgAxq7KG5NelD7N5CZKX81NEM7K4V67eiOjGrvmWlCqcO3Ws7Aevar8SWXvU_wTDUpl9BJXF8bM22QTmOw8Q8MjVmhz3iKHxAsYzoeQigWbvVksAmWe2xcW9eR7TUu1ty1_e2G2iVmEjSfeR46JyUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین حسین شعار ماست، شهادت افتخار ماست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666739" target="_blank">📅 07:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
آیت‌الله سبحانی بر پیکر مطهر رهبر شهید انقلاب اقامۀ نماز می‌کنند
🔹
مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید و خانواده شهید والامقامشان، به امامت آیت‌الله سبحانی در مصلای تهران برگزار می‌شود. #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666738" target="_blank">📅 06:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873b50fe14.mp4?token=lz2DE7-fRru8djWEE2sw5x2J5S9wVLl3JuZaewUJQEjVD1GgPlqpBQu4IsvxBQ01zCV0k485Ku_vc9PsrdyYc-3QqMDTkeZwBuSF_3HK9fkp2M3CvTbSpXgD6p4tDxb4gGL-nnZuudeUCWpCllQ30sdcb8hvCHjrjoyw5IlmN21Np_47XElTXVnG-DX81_yxml9ltOGabYC_NFT7LXc6o-DDIq84Rjf-XurIYBxxnHLjQFtBn-IN6Yizy815j1knxz0P1UFp3Uo8KCB8IB0zQvlmtMNtJNc0YOkxIPixblncCjlNp911RVpvpMhF1R_bdUyTFoAWkukyc1OAouXBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873b50fe14.mp4?token=lz2DE7-fRru8djWEE2sw5x2J5S9wVLl3JuZaewUJQEjVD1GgPlqpBQu4IsvxBQ01zCV0k485Ku_vc9PsrdyYc-3QqMDTkeZwBuSF_3HK9fkp2M3CvTbSpXgD6p4tDxb4gGL-nnZuudeUCWpCllQ30sdcb8hvCHjrjoyw5IlmN21Np_47XElTXVnG-DX81_yxml9ltOGabYC_NFT7LXc6o-DDIq84Rjf-XurIYBxxnHLjQFtBn-IN6Yizy815j1knxz0P1UFp3Uo8KCB8IB0zQvlmtMNtJNc0YOkxIPixblncCjlNp911RVpvpMhF1R_bdUyTFoAWkukyc1OAouXBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت انبوه عزاداران رهبر شهید در خیابان‌های شرقی منتهی به مصلی تهران
🔹
اینجا تقاطع خیابان شهید بهشتی و شهید قنبرزاده است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/666737" target="_blank">📅 06:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e14e1ae2e.mp4?token=LngotesOELi9m2VQxntybIcfUbdT3U1iGdy_wZf2K-Mo64GfGYpeNJu7-dcbD00ewyMM3HFVUYCgorR6xIRLPvAZgbynTeRtf8RMkfPQiBokJTmlQ33gVhLT24J6yqasG-MifAFH7n0O8lx-WrelBsAjT61_LGGaXQ8ZUDEuTLtYxoiCDnTULJTLiaQj51Fh_njkryyILi3jzf0c7ROobvJ0jUBMsK4lRpXKj03UU5vCdeeMwdD7Az1JakGy8vMrX2vJFqgVe7IBWlEc-mdq5TLdXpxB_mgtlt3lJeTxZOq3gQBi2U4eC1GwwsMQxA6YIwk5_gGA3dOAPS4UYIFjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e14e1ae2e.mp4?token=LngotesOELi9m2VQxntybIcfUbdT3U1iGdy_wZf2K-Mo64GfGYpeNJu7-dcbD00ewyMM3HFVUYCgorR6xIRLPvAZgbynTeRtf8RMkfPQiBokJTmlQ33gVhLT24J6yqasG-MifAFH7n0O8lx-WrelBsAjT61_LGGaXQ8ZUDEuTLtYxoiCDnTULJTLiaQj51Fh_njkryyILi3jzf0c7ROobvJ0jUBMsK4lRpXKj03UU5vCdeeMwdD7Az1JakGy8vMrX2vJFqgVe7IBWlEc-mdq5TLdXpxB_mgtlt3lJeTxZOq3gQBi2U4eC1GwwsMQxA6YIwk5_gGA3dOAPS4UYIFjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری: ظرفیت مصلای تهران تقریبا تکمیل شده‌است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666736" target="_blank">📅 06:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnwT_5x5KOTN7O4e-Z2NtkZWtCf4vuXlO00wBUWm5i4fBb6caYpd_kMfjPdXE3AxbLJvoIjM54jVA83t-0JpxKhiSZwuwAWSi9qnlerG_AV4xJJzo2DbbZNzcVSyAAuLlcKLMjAjO-jNyI4LKO4ukWIKfXLL6ai1wQjzuFYw-1NVqGYDLSKj-YBqE3b6iSTav5GnfiAk9SC9CucBnzXF9lnTZkJSK2q1RjbvycJKlKEPo2udd5ysZ8tgr8VIOoMz5qu-XHX6_952LdAKPbDhqEjUbybw1n-Yy2xDEVQYn5YQ-OLslSXh_qE1xNHFd2-GUkKzVqeZ6YiamBA1ZPnshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا
🔹
تا ساعتی دیگر مراسم اقامه نماز بر پیکر امام مجاهد شهید و شهدای خانواده ایشان در مصلای امام خمینی(ره) برگزار خواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/666735" target="_blank">📅 06:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou59wQOIrkOblRAzfZU4-8g0q_Hpb2WSPus4byHuESupG9uTBPfjo38Wqvy7zTV2xZZajvLwYQqb_tGydL9rIUKF7GjjGMXQYmrtFC7hQ4NHb1-DN6OFCRguPfSLLJ4MedfBejoKueo3MN8ConS93NL2Yw4B3PKnjm8xOeLyBMJvcAv1rutC5SgQn383Zs49XtjDww_zNxW9QUsLgaL1M1-iaxfLSqYxe2Du0quKOWyxNpjmb3hq3rn5L803_Aj0ngBuoVaFL8gNqlrAxqeargy6cYxuI78sBTw-WdqJAzXN0K9FUG-Xs9jGIL3HHddRbsSiuCvwM8ZGsu7Ttp5FuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/akhbarefori/666734" target="_blank">📅 06:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14186f071.mp4?token=j-BfV3JKVq70HofrSP_oJa0YL8e5AxiCjkIcXqSnFwZ1l81PF2TgAGfSJlUJUPYHh9nsMHRpwNQqRNtCXqZtF5RNuT1VMOlmlo10N8cmOP9k3vLOXkvmy7ULiOU2hrCiiU6Dod1-GcU0G9ohmIgrDxrdDgzCMJpbWBrKENKrJ4E6KtmFSOBpTOK8kAWpb1kZ8k1roEiUAbS0a6Rr-JP4zFYPFXIsdxf39KQUuXAjEcPt6YLygJKCkuWgZPNwSoEcKLoYMsQOi8m59yevkMznrr9T-GlOa1zwER81ynH6jpqta-j3qIWRH-1c9tiu6Y2PcITZf4fPrxIZrBqXYak74Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14186f071.mp4?token=j-BfV3JKVq70HofrSP_oJa0YL8e5AxiCjkIcXqSnFwZ1l81PF2TgAGfSJlUJUPYHh9nsMHRpwNQqRNtCXqZtF5RNuT1VMOlmlo10N8cmOP9k3vLOXkvmy7ULiOU2hrCiiU6Dod1-GcU0G9ohmIgrDxrdDgzCMJpbWBrKENKrJ4E6KtmFSOBpTOK8kAWpb1kZ8k1roEiUAbS0a6Rr-JP4zFYPFXIsdxf39KQUuXAjEcPt6YLygJKCkuWgZPNwSoEcKLoYMsQOi8m59yevkMznrr9T-GlOa1zwER81ynH6jpqta-j3qIWRH-1c9tiu6Y2PcITZf4fPrxIZrBqXYak74Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل جمعیت در خیابان های اطراف مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/666733" target="_blank">📅 06:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حضور میلیونی مردم تهران برای اقامه نماز بر پیکر شهید امت
خبرنگار المیادین:
🔹
تهران شاهد حضور جمعیتی میلیونی است که برای شرکت در مراسم اقامه نماز بر پیکر پاک شهید سید علی خامنه‌ای گرد هم آمده‌اند تا آخرین وداع خود را با ایشان به جا آورند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/666732" target="_blank">📅 06:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d9054a.mp4?token=muem4UdwFYtrhb_5PYxjchvzebo_GE__KVW67lm7kxUGAqSOugiV9tRSl0Ce15hRG_zu3tt-xWMN5YVyNaqOqarhShCIe40MFLutcXuSDhtRX9IcpyYL74Di1Ox_GBiN5QpaOxW3prxv1kP9l0xh7U-ABgkucTlCpj8DzVrPpS2q6PMVpeKeezH7yJLgI-2UsyjaNB3qgk6wz3UnXuiFRyK5zWtMrwxNz3gRgf52xYC5dkKb2-4o3GkScXyYdOA7D8AeVo6wnp9ieoHvmiovaLUOVzyTG2L-F-MQG6RZtwiIj1qsx8E5k0UVJSwBHxUtPFU1CpSXLX5PvbR3YF-9HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d9054a.mp4?token=muem4UdwFYtrhb_5PYxjchvzebo_GE__KVW67lm7kxUGAqSOugiV9tRSl0Ce15hRG_zu3tt-xWMN5YVyNaqOqarhShCIe40MFLutcXuSDhtRX9IcpyYL74Di1Ox_GBiN5QpaOxW3prxv1kP9l0xh7U-ABgkucTlCpj8DzVrPpS2q6PMVpeKeezH7yJLgI-2UsyjaNB3qgk6wz3UnXuiFRyK5zWtMrwxNz3gRgf52xYC5dkKb2-4o3GkScXyYdOA7D8AeVo6wnp9ieoHvmiovaLUOVzyTG2L-F-MQG6RZtwiIj1qsx8E5k0UVJSwBHxUtPFU1CpSXLX5PvbR3YF-9HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از بالا، جمعیت متراکم مردم در مصلی تهران
🔹
حدود ۲ ساعت مانده تا اقامه نماز بر پیکر رهبر شهید انقلاب.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666731" target="_blank">📅 06:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666730">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40c41061b.mp4?token=KWXRnSxfa9Vc9YMvm9MCjaW4C04m6_dNjx1OcoJkgieioqblx5XTeC5dq9y16lat9RiOAcQ3tnx9r9hGik4DrpO3fG0vyAIQ3cEd-pGnlW4i71hpCyCoW5zvqQJy2cDnRiwSyae474k0w2DZvDnRGekOuRL_roJ7MrzYCOs6ZwOroamKNtwSN3CCa6T2MgD1x9ctrQFnns6ddBOwQBzIMRbR8aBxCJ0Er4muB7unmU5GNlbsVsKSL18k_62PQ5WZF53sWVcXOIKsqVN3aWivxEDA5asS8J3cSiL3x0Yrpqee5NFnN5XmIIj7e1pXJ63iMJrfmaVHZiLku35VX7Zr6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40c41061b.mp4?token=KWXRnSxfa9Vc9YMvm9MCjaW4C04m6_dNjx1OcoJkgieioqblx5XTeC5dq9y16lat9RiOAcQ3tnx9r9hGik4DrpO3fG0vyAIQ3cEd-pGnlW4i71hpCyCoW5zvqQJy2cDnRiwSyae474k0w2DZvDnRGekOuRL_roJ7MrzYCOs6ZwOroamKNtwSN3CCa6T2MgD1x9ctrQFnns6ddBOwQBzIMRbR8aBxCJ0Er4muB7unmU5GNlbsVsKSL18k_62PQ5WZF53sWVcXOIKsqVN3aWivxEDA5asS8J3cSiL3x0Yrpqee5NFnN5XmIIj7e1pXJ63iMJrfmaVHZiLku35VX7Zr6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این آخرین نماز جماعت است، بازم صف عشق، پشت سر امام امت است
🔹
نوحه‌خوانی در مصلای امام خمینی(ره) تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/666730" target="_blank">📅 06:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666729">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
انبوه جمعیت در ایستگاه متروی شهید بهشتی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/666729" target="_blank">📅 06:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666728">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed8b59c80.mp4?token=OjE6j-IHpLprjuCNoBEJkbFAL_73fs75ud6-Qlu8EubMJ2JDJjJiEwnkNC9sx2pAL70vpkEsvp0zxFzcafTzoNDIvtN05sMofCQ8XlxEtH_9YEu34lnFRZnOQeWJjN2wc-5AOf81RPnNVdFmMY2hubMl6ucQ5EAxGrWr8KuN9bYhGi1uwn7dMcwgxV0J8_DIgl4Qlu-yvJnNfRM-q3UJ0m873iLalPLyeGVxpb-9RLWdg2yRFXM_VIkDSTI3nhL26BsiUIQANC2wIsnPf5bc6_Wqo1hU5VX7sbkWOaSj9-_-70ra9hkeRPqD8fYp8WeE8x4gYBlY-aZrwclz3QiEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed8b59c80.mp4?token=OjE6j-IHpLprjuCNoBEJkbFAL_73fs75ud6-Qlu8EubMJ2JDJjJiEwnkNC9sx2pAL70vpkEsvp0zxFzcafTzoNDIvtN05sMofCQ8XlxEtH_9YEu34lnFRZnOQeWJjN2wc-5AOf81RPnNVdFmMY2hubMl6ucQ5EAxGrWr8KuN9bYhGi1uwn7dMcwgxV0J8_DIgl4Qlu-yvJnNfRM-q3UJ0m873iLalPLyeGVxpb-9RLWdg2yRFXM_VIkDSTI3nhL26BsiUIQANC2wIsnPf5bc6_Wqo1hU5VX7sbkWOaSj9-_-70ra9hkeRPqD8fYp8WeE8x4gYBlY-aZrwclz3QiEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سر دادن شعار " ابوالفضل علمدار ، خامنه ای نگهدار " توسط حاضران در مصلای امام خمینی (ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/666728" target="_blank">📅 06:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
آیت‌الله سبحانی بر پیکر مطهر رهبر شهید انقلاب اقامۀ نماز می‌کنند
🔹
مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید و خانواده شهید والامقامشان، به امامت آیت‌الله سبحانی در مصلای تهران برگزار می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/666727" target="_blank">📅 06:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666726">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3ceca330.mp4?token=ufbT9aEsfs6fGFKPkgjSvS9ENyC5lbC3Pvu9Mexm-Vbwmb6yzcvVuvtbECU1PhZS0LpDqcjV_0tMHaPzlxKwsT5laYZNtex4mr82jaudVOdtC68_JI9061ztY-jhEhhR2Ju6cyvjhT8HyEiL1fasJq8LjraHYiUIQ7K0Lg2kLR58eophHc7Omuoqvj-iTeMG4GwkNgDxe8hWQ1OVhmr_80XLKmT7sdluXwRlnGbv3ToJ0FUlFz_RuNZV5DKrWvMYc0lB4tg7v_BqMEbNas8xHCPn5tuzyP03uaMG-WrCKRS_rvEUTMii9yi5QH4qO9tlbY8c2V46XwQPAbT-oRuk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3ceca330.mp4?token=ufbT9aEsfs6fGFKPkgjSvS9ENyC5lbC3Pvu9Mexm-Vbwmb6yzcvVuvtbECU1PhZS0LpDqcjV_0tMHaPzlxKwsT5laYZNtex4mr82jaudVOdtC68_JI9061ztY-jhEhhR2Ju6cyvjhT8HyEiL1fasJq8LjraHYiUIQ7K0Lg2kLR58eophHc7Omuoqvj-iTeMG4GwkNgDxe8hWQ1OVhmr_80XLKmT7sdluXwRlnGbv3ToJ0FUlFz_RuNZV5DKrWvMYc0lB4tg7v_BqMEbNas8xHCPn5tuzyP03uaMG-WrCKRS_rvEUTMii9yi5QH4qO9tlbY8c2V46XwQPAbT-oRuk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محوطۀ مصلی پیش از آغاز نماز مملو از جمعیت شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/666726" target="_blank">📅 06:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666724">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv2uips7ZlJBwqFcdYaaPSaa-SfWd8N8WLLMIfyVB4dXIgf1nBfOPcuhuazSJXSnK9E_7kg6COw-deO2Soa0GDST7DRBGoBwm8Gyx2L3NZL_dlQ-NBmQIJo-kNV7IKMU6KcgI-JGzYaS6PUWgb8kJh7_svLULtjiVDiMrUolek7xVc56qFH4QZTuh4GzEd_kKVeqJ2pEIz0LFTzD4mSBpXhcNh5QxZwTNPgT7J-Y08FypEIfGsa5IxORW05BnPbp7iYc4pfuvj0QgG2FZ-eQ4aC5_0VtgncLp27gtw3-kKTMlYzsJIkDFwAmEPPf5I124MCRoIM3xTvzi1V3W22zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKFJEIA7zWQs5EE1oJySSn5De2ouC6yIHyxZvH6eUcdesKonG0y39SvLWUL8If5DOsgrnD4ikrJl1oqfUH9drv34DXfRB-e1v8eF5Vre0inNxBnCXsE91LkCbdi4FmDNazA-xzaVjTlcoAGbZypADwW0wMuFXgUzwRcbV1pBUJtcmw1APDHQhwppdxeQuQyJXcTLJi_tsr9xmM3vK1kpCNVr99oHZ7nG4X7SxyWyDE6-t_J3lMG5VnKBNgfQsgLeljyH-6tCMVBDqOUpKD3GZz9QsjCKOXifLQayqp9Vwm6NmiZTo5MFvOml44HhebJiU8HaLOm1AUiuuGJtq7zAyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمل پلاکاردهای
#kill_trump
و
#kill_bibi
توسط عزاداران رهبر شهید انقلاب
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/666724" target="_blank">📅 06:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666723">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c0ed090c.mp4?token=sAs-zAr4RUGLVzhzsK9-afHYFjZecWP4eo2WaH1pYnZxIl0hpT9oNqXDT567ThqYh_-aPobWw1YAW__D0tTFIo6leKWYIdewYw4H6vWr1UAF05Iqu_5t3UQlnTbuz4mAAE51HuwlNYarnbsH4_njJxDD-tiLgZeWM53LAJGsQ6vD9RQkF606a7bE8ug2mQuyO6qOSVnx1wDb53_V69YGnAPlILzK1Ii_5ClkpaO2t5ozWY1nLwdGBCIXgErrhCMVRbao47fXLQZLx1HLeRa3l7gAys7y3hJLI_NEUs16OMw_-x2jq-KEonNsVhVYLoW1sKyJH4kQhn_5p-a6G46T9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c0ed090c.mp4?token=sAs-zAr4RUGLVzhzsK9-afHYFjZecWP4eo2WaH1pYnZxIl0hpT9oNqXDT567ThqYh_-aPobWw1YAW__D0tTFIo6leKWYIdewYw4H6vWr1UAF05Iqu_5t3UQlnTbuz4mAAE51HuwlNYarnbsH4_njJxDD-tiLgZeWM53LAJGsQ6vD9RQkF606a7bE8ug2mQuyO6qOSVnx1wDb53_V69YGnAPlILzK1Ii_5ClkpaO2t5ozWY1nLwdGBCIXgErrhCMVRbao47fXLQZLx1HLeRa3l7gAys7y3hJLI_NEUs16OMw_-x2jq-KEonNsVhVYLoW1sKyJH4kQhn_5p-a6G46T9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلای تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران مملو از جمعیت است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/666723" target="_blank">📅 06:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666722">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bce0f49c8.mp4?token=vGGhad1FOVDruCANFfK_itC3allIDpxW8EqphDsImXhXLA1PtaNbK5mARl-cp7hOIs4VimcEhB8iEDmZP_YKgFCw050oEMjE8Lkdgqjy0lKSH0RCFoHNMSu60wNs4aJR94SyjJ3vuE85UzuwAbRJzO1pn5LWe4mqJPOpJwM79T7m5gqJ4PC4o3PDZjXBZmtJ2zrYySTpPzTl3gcLwF5PMKKt-Bc-Uwp7XJZoMqyZrn5E6pt6ZW8GKgVf2s6SZVhGUkBi5EAGtI3IOQXto5vY_zVLTIwkKpABzeeh5H7yux0DytCmV9jFYmArWqv4TGpEPhhA4zz0zUTN8LykBGYx9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bce0f49c8.mp4?token=vGGhad1FOVDruCANFfK_itC3allIDpxW8EqphDsImXhXLA1PtaNbK5mARl-cp7hOIs4VimcEhB8iEDmZP_YKgFCw050oEMjE8Lkdgqjy0lKSH0RCFoHNMSu60wNs4aJR94SyjJ3vuE85UzuwAbRJzO1pn5LWe4mqJPOpJwM79T7m5gqJ4PC4o3PDZjXBZmtJ2zrYySTpPzTl3gcLwF5PMKKt-Bc-Uwp7XJZoMqyZrn5E6pt6ZW8GKgVf2s6SZVhGUkBi5EAGtI3IOQXto5vY_zVLTIwkKpABzeeh5H7yux0DytCmV9jFYmArWqv4TGpEPhhA4zz0zUTN8LykBGYx9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور جمعیت عزادار در ایستگاه مترو کرج در ساعات اولیه صبح برای شرکت در مراسم اقامه نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666722" target="_blank">📅 05:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsPZKSH8auJAHiRX4_kRWjt7YHhZFLvuawLUmqfCtn_A3Kx0BjPHeMtQh9MQX1gl-1QIWN08oWVWlHvUiLW9ckQ_wFGJvcoDpoqznI-5Q5Z8Y8eyjR5l8EHNGGRX-d1eExNF_7KUXUw9q88yzVCTRc1C5jLgoA8jgo-6caVEEYyOIDcVesWeqqUvH5kV16HGHIa0tfJg2Wlo3AFJW4g5wRR-w9JdP5nMTVMjwvzF0GTs4k3r7X2arEqzuTmdmqKqe5OMOV81CKj847W_UQ_fVSB7zIasjJ3eyKP5-0uh_e5NHhjUiPPCQpn3WGrgzD5vRVoIBiDhDQ7D_ES_6Y9Ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTTKW5ICp8pVHq_xGZKSvzfXz6mQnisg5krCM12Wjkv2nRF47nNoBd0SOA7SLIq6JpqRt0D6Ofc5_CW10Uf1nOuzH1L3xWYoWTXxUeTwj3-t49mIKgvKmD0FLOZ6aaQ8d9ojCXtXFOmkCHdPsekm2PcSS_fpGRBQbmyNR31j_nUlBLNYUwozbPyUgJ8t_OfB3IdmWDkEl9JCcHQFWaH4LZmV_Yle-b9PI9AOj0y5B3CIMUB9eiNClOEFgtdLQ7iL4OyMO8FxlPtCduKLjOSJW2ToKwoBgf8FsHnvxn2BOZe0WuPl_faxzNJtqg9VXEvWBmk8L8r0WUKEge3tojbs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxpdG4VhWnHqOJAj0G_3r7xXyUywDNJ9xKqR3-WemIM_QoPGKWDV77JRBJF7_1StTpVlj6EFjLjvYFWsGL6_B-fXySXpk3-dX9C8td_XlINNBL3uRv2GPaKxR4HRa6jHMnJtkAmKy4jD99vVI2NME0Z6rYG5z4hpS7dMMwWlDR1xkcxXyNTvq41A_wxhnzhHeeeaGWbNc6UgIAAXp6ZFgP6qhC6UoG6TceX_P3B97s7baUUl7ghuuTZ2VP7wZ1B-vA7Zn5aP_JJVQdD8Rrt2eLMkHDlUEp0oH2PbCc2ZYxwNWMAKdEqmV18SGf6szoNg3m4FcHW_y2sz4dj-JbIlWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اللّٰهُمَّ أَهْلَ الْكِبْرِياءِ وَالْعَظَمَةِ وَأَهْلَ الْجُودِ وَالْجَبَرُوتِ...
🔹
سه قاب از آخرین حضور رهبر شهید انقلاب اسلامی در مصلی امام خمینی(ره) تهران در ۱۱ فروردین ۱۴۰۴ و اقامه نماز عید سعید فطر و بیان خطبه‌های نماز و امروز یکشنبه ۱۴ تیرماه ۱۴۰۵ تا ساعتی دیگر مردم عزیز ایران بر پیکر امام شهیدشان اقامه نماز خواهند کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/666719" target="_blank">📅 05:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c04acf51.mp4?token=afYe9LKvIb0HMKkA0K8DaE36fiDgQXCSfpiA-IrvSINrfFjErzoxULWipO7KQLwp2bg7wZE6fEjemQAlQUSdpxJ5LSs_KfCLN3TzJIs3H183bRpc49tPj4ymjnb03NJsQ_e-wPPDzyGaG5sopkW-ndZ85IzKu-K_ConRVaUyAhSXkrPdjAb_wmC8fFa6K7q7zROfQuh8bZLFHFCCom9rG8Ewr0p9z6Dh4-N3MHuz4EfYPtH-VfuWQrgOaBCeWua8SGPHdvWzss-tIHVMoQXJm2_Q2RDpFH0-4NjF_HxOSN8_h7zM2mgCWWNykGpJNrk1Y4bdd5ObTINH4VbTp1r-RZvWBhYjueLWY9SS1lJD2N6MuoMgKEELyJB_6nZ5Ioh9UWu1UUjqKIOe0_AGbIOwT80_bRAMbXljrmKAJQXw3yiMkGHM1ImC3e1CFHvt9yYe7GQ_W1h1x3RAGMh1NowYmX91hE__ngRc276ZKudR3A_Owgkkrjs9EXkTZrwfwMmpuduGyruvKCNJNfEnvC2vQ7eeKGbtY_SEAhV7XkZ0PoGC_Qa7wmZNu4fjW2swS6ipbvsWmL-PDMAT8xGao0MPIUhsW_7xW1MKQoEYq5NRdhMdwuUOqzD_OCoMsm4g8xKMN9qAC1GT0wI7JnqcZfxkQs73wY8Iz5X0qvSGYs4JDBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c04acf51.mp4?token=afYe9LKvIb0HMKkA0K8DaE36fiDgQXCSfpiA-IrvSINrfFjErzoxULWipO7KQLwp2bg7wZE6fEjemQAlQUSdpxJ5LSs_KfCLN3TzJIs3H183bRpc49tPj4ymjnb03NJsQ_e-wPPDzyGaG5sopkW-ndZ85IzKu-K_ConRVaUyAhSXkrPdjAb_wmC8fFa6K7q7zROfQuh8bZLFHFCCom9rG8Ewr0p9z6Dh4-N3MHuz4EfYPtH-VfuWQrgOaBCeWua8SGPHdvWzss-tIHVMoQXJm2_Q2RDpFH0-4NjF_HxOSN8_h7zM2mgCWWNykGpJNrk1Y4bdd5ObTINH4VbTp1r-RZvWBhYjueLWY9SS1lJD2N6MuoMgKEELyJB_6nZ5Ioh9UWu1UUjqKIOe0_AGbIOwT80_bRAMbXljrmKAJQXw3yiMkGHM1ImC3e1CFHvt9yYe7GQ_W1h1x3RAGMh1NowYmX91hE__ngRc276ZKudR3A_Owgkkrjs9EXkTZrwfwMmpuduGyruvKCNJNfEnvC2vQ7eeKGbtY_SEAhV7XkZ0PoGC_Qa7wmZNu4fjW2swS6ipbvsWmL-PDMAT8xGao0MPIUhsW_7xW1MKQoEYq5NRdhMdwuUOqzD_OCoMsm4g8xKMN9qAC1GT0wI7JnqcZfxkQs73wY8Iz5X0qvSGYs4JDBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت فرازهایی از دعای توسل؛ ساعاتی پیش از اقامه نماز بر پیکر مطهر رهبر شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/666718" target="_blank">📅 05:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc61423721.mp4?token=cLufs6pSq_K14D5-eF5hYSXHBg4SqP52qfwe-0LflbDnxAqwb_qLpqmcJXTau0hfDXlX8-0lrnicqrTfNCmw2rAg9FFyTSC503x95bm2XQRXF1DqbP41rpbpmPwxpuDvzVHfLKaVhftyL0wHyKahJSFh6urr04dtHVEf8NKfUeiaGKp2M0pKceXA-KJrUG4Mx8A8qoVayoYoTSdIERLGgmn7wMpb4MXBCdw9fvGBdLDT3_IVoDi6H_Qmz8NsIGpRu1IWh59Tu1w2zJ_ifYGjqOdGR5v7z8VcoRzriLfo3EIHXB1MX7oITWFOMdFH8LIHKsjsA5hhLTpk7xMGCsO--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc61423721.mp4?token=cLufs6pSq_K14D5-eF5hYSXHBg4SqP52qfwe-0LflbDnxAqwb_qLpqmcJXTau0hfDXlX8-0lrnicqrTfNCmw2rAg9FFyTSC503x95bm2XQRXF1DqbP41rpbpmPwxpuDvzVHfLKaVhftyL0wHyKahJSFh6urr04dtHVEf8NKfUeiaGKp2M0pKceXA-KJrUG4Mx8A8qoVayoYoTSdIERLGgmn7wMpb4MXBCdw9fvGBdLDT3_IVoDi6H_Qmz8NsIGpRu1IWh59Tu1w2zJ_ifYGjqOdGR5v7z8VcoRzriLfo3EIHXB1MX7oITWFOMdFH8LIHKsjsA5hhLTpk7xMGCsO--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلای تهران، ساعاتی پیش از اقامۀ نماز بر پیکر آقای شهید ایران مملو از جمعیت است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/666717" target="_blank">📅 05:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f81a2fe54.mp4?token=Ildr602ibglFzeHfHC_PRKJ20S81kkem55QQ2mW23Uwc7X3LlXrSndksWTtAaE_DAhzPg725q1NrLH0pz_SPoukYZrvIFP70tCc6WTM8pbK15Bkrgysn6Jrz5xdcjsSkxVMITaEQaDxOU0Rt9BuIRfbGHWaEvFlPF9HzmB-CvezkaBARik2Ah3R6tfG2VV0LCnJBeH4Lk3jzvf4GBfDRSNF3q5RJWOSX36w9o25MHmSbUBfbzGwzV7wyEVDn9lnOkxlnb7XmjIIGSICTmhkSb9Xg42DCcZmObbO6dFByga7avlrltuv4be2Hhh-R4tj47J2fKER7zfk_mpDXQZYdLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f81a2fe54.mp4?token=Ildr602ibglFzeHfHC_PRKJ20S81kkem55QQ2mW23Uwc7X3LlXrSndksWTtAaE_DAhzPg725q1NrLH0pz_SPoukYZrvIFP70tCc6WTM8pbK15Bkrgysn6Jrz5xdcjsSkxVMITaEQaDxOU0Rt9BuIRfbGHWaEvFlPF9HzmB-CvezkaBARik2Ah3R6tfG2VV0LCnJBeH4Lk3jzvf4GBfDRSNF3q5RJWOSX36w9o25MHmSbUBfbzGwzV7wyEVDn9lnOkxlnb7XmjIIGSICTmhkSb9Xg42DCcZmObbO6dFByga7avlrltuv4be2Hhh-R4tj47J2fKER7zfk_mpDXQZYdLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود عزاداران هندوستانی به مصلی امام خمینی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/666716" target="_blank">📅 05:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ایستگاه متروی شهید بهشتی موقتا بسته شد
🔹
همزمان با افزایش حضور عزاداران و در ساعات منتهی به اقامۀ نماز بر پیکر مطهر رهبر شهید، ایستگاه متروی شهید بهشتی در مجاورت ورودی شماره ۳ مصلی امام خمینی(ره) تهران به‌طور موقت بسته شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666715" target="_blank">📅 05:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b2048af6.mp4?token=D3g5pGR-cy_WUZfJ2r1NoG2d2RuKOQcf6tb4lEonE142A3W1t6pnnSAPT-w-bjKR2hwVBPpoXbRG3iHzCfNFeQTmigO_-TtM-tULC7m-SVxAqqzWrxN-AiItbZ_fr6hB7fMm0DCcJGn-3RefsdhcYTPZ8_FKEZoAkVjE5mqPsKEAN5S5DIWiTFY01JwO5N2uPIQ0WSoSphlqQ7qGI9icTZafZ35NO67cx9SpSUSmmUrEtZy3dlx25OBEwZAbVJI4qKVnDK7OFeKBbXi0rqwVwMHVDb-ruMaxfk7TTZp7veRdBAirI3zUA2yImvCYfiUWMnxuCUYBKDiUkVMy-1uA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b2048af6.mp4?token=D3g5pGR-cy_WUZfJ2r1NoG2d2RuKOQcf6tb4lEonE142A3W1t6pnnSAPT-w-bjKR2hwVBPpoXbRG3iHzCfNFeQTmigO_-TtM-tULC7m-SVxAqqzWrxN-AiItbZ_fr6hB7fMm0DCcJGn-3RefsdhcYTPZ8_FKEZoAkVjE5mqPsKEAN5S5DIWiTFY01JwO5N2uPIQ0WSoSphlqQ7qGI9icTZafZ35NO67cx9SpSUSmmUrEtZy3dlx25OBEwZAbVJI4qKVnDK7OFeKBbXi0rqwVwMHVDb-ruMaxfk7TTZp7veRdBAirI3zUA2yImvCYfiUWMnxuCUYBKDiUkVMy-1uA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از جمعیت حاضر در مصلا، ساعاتی مانده به اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666714" target="_blank">📅 05:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff810f9b0.mp4?token=HOE7Fv03fI_iLFQrGnWQvzxBxlYYM42O8WfhB5Z7I7I7am6jYKjh2DTx0B6Mwaj34bJfCm7lYomZjwXks2JbssOGoee7rYoY2UAoL6SUOWTi9wNI8ItHc7amSlvz8xlZ9P1iw-EakyMutBv3wfLpmi4e1k-Hfjg8AazTGiSThhAPMcqN5XvOUm-2k5sDxQe_PGv5lK8lylbM_rVuecpLkg7paVn7YYNbQsMh173xgVhAldz0WWRIfd2J_ttg07j-pwym8Iz8ImxOy_peAxmvnMa47aRlBn6VNvZhzvmw0R1zT9N6KCXcoPs0nHky13CenF6G7lV0YWplZ2qP4jz_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff810f9b0.mp4?token=HOE7Fv03fI_iLFQrGnWQvzxBxlYYM42O8WfhB5Z7I7I7am6jYKjh2DTx0B6Mwaj34bJfCm7lYomZjwXks2JbssOGoee7rYoY2UAoL6SUOWTi9wNI8ItHc7amSlvz8xlZ9P1iw-EakyMutBv3wfLpmi4e1k-Hfjg8AazTGiSThhAPMcqN5XvOUm-2k5sDxQe_PGv5lK8lylbM_rVuecpLkg7paVn7YYNbQsMh173xgVhAldz0WWRIfd2J_ttg07j-pwym8Iz8ImxOy_peAxmvnMa47aRlBn6VNvZhzvmw0R1zT9N6KCXcoPs0nHky13CenF6G7lV0YWplZ2qP4jz_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان علمای اهل سنت در مسیر مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/666713" target="_blank">📅 05:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f424764a.mp4?token=Wl4X3hrsHvSEdFtoHit_ZK2neQYh2YmGNmWlyJUaDjFFTv6-7HQX9jP5m7pFzIcUndsUpV-fU-zL0TdYbIa-k9HFZ0RsiKSkMbpHaP6WJcxBYMy4Da7100e05F5wL7n3gT_ZChv2ks_jRHQr9T2Fs2_cYAsgyq397qaPwUnnDDUGWZ6GG8NzkHhku7ETLqRFIXnHgut8erYWIc6s5iTxv7_KE037UQkLdyiiu3Db5s1SaCeYiogTncdewkaPVay54ZCMYcRiwpBS2ZzUvigX84lGpUrwaxPcmf3rZH7AD65X-egt3AjkstB0bmMvoXM3mLyGTD9srQwuO4sitVEHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f424764a.mp4?token=Wl4X3hrsHvSEdFtoHit_ZK2neQYh2YmGNmWlyJUaDjFFTv6-7HQX9jP5m7pFzIcUndsUpV-fU-zL0TdYbIa-k9HFZ0RsiKSkMbpHaP6WJcxBYMy4Da7100e05F5wL7n3gT_ZChv2ks_jRHQr9T2Fs2_cYAsgyq397qaPwUnnDDUGWZ6GG8NzkHhku7ETLqRFIXnHgut8erYWIc6s5iTxv7_KE037UQkLdyiiu3Db5s1SaCeYiogTncdewkaPVay54ZCMYcRiwpBS2ZzUvigX84lGpUrwaxPcmf3rZH7AD65X-egt3AjkstB0bmMvoXM3mLyGTD9srQwuO4sitVEHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان های منتهی به مصلی امام خمینی (ره) کمتر از ۳ ساعت مانده به شروع اقامه نماز  بر پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/666712" target="_blank">📅 05:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db58329b1f.mp4?token=TO7xAKEnwmZ6OYCV3DdbQBrkKnKbuYpbaUR7ld-lepfIZFKc4xqLMhlitEJArZvGi7Afan68LYzaCA2AAx6LtqWhLzaecRCjjLp1sDP6ZdPHKpd_GlMfY_RQ_RwWfn66li3Erp9svcCRcIGTMouMQ9MG_W9c9r3YiP_Kladz4tiWi2BkK8yTc4o9VTgR0g-99K3vhKnXVmmad0ZPTluItCiv6vrLhzPf3-DkVE3i1-vGkaMZw3ERratKPuyhqaspvPhFUqp47szyKEFd99L2NCx6YVHUFtL38btPb_GYCQnlLS__7R4G4pdMR7ClcsObQW94sLpufpShRq_5v1OMMgL7O0GhJ4ZrGYAkk7KVsdbeO3rP9B-p7Y-ktcM7zcwhp8oIpHC6JgIPryrDe-qvT_rcWXSryBQ6Y9y4xwdaSbJTCpVDKP5T8VaAKqoIAhrdJ2jX5H-_ukHxPx7ahjxb-aSpd0l34iJo7uDxm9u63KltlcA-kYc1vtiW86bFGjwMJLtiAtbQ6EBImeAFOHzMrUw07aMVBSHAfUmo8FR_rmWWl9O8AwaHuoMdxeEtvvBHlP52UtIHcyDEuhwfumA0p5CXzcGiPcUxX41_ImTvbxn_cxmlLZMgmT1wH1n_rxEdirfk8I-8YFHLjheg77M_zIQgxQWKUhe9c0HkhS6HhN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db58329b1f.mp4?token=TO7xAKEnwmZ6OYCV3DdbQBrkKnKbuYpbaUR7ld-lepfIZFKc4xqLMhlitEJArZvGi7Afan68LYzaCA2AAx6LtqWhLzaecRCjjLp1sDP6ZdPHKpd_GlMfY_RQ_RwWfn66li3Erp9svcCRcIGTMouMQ9MG_W9c9r3YiP_Kladz4tiWi2BkK8yTc4o9VTgR0g-99K3vhKnXVmmad0ZPTluItCiv6vrLhzPf3-DkVE3i1-vGkaMZw3ERratKPuyhqaspvPhFUqp47szyKEFd99L2NCx6YVHUFtL38btPb_GYCQnlLS__7R4G4pdMR7ClcsObQW94sLpufpShRq_5v1OMMgL7O0GhJ4ZrGYAkk7KVsdbeO3rP9B-p7Y-ktcM7zcwhp8oIpHC6JgIPryrDe-qvT_rcWXSryBQ6Y9y4xwdaSbJTCpVDKP5T8VaAKqoIAhrdJ2jX5H-_ukHxPx7ahjxb-aSpd0l34iJo7uDxm9u63KltlcA-kYc1vtiW86bFGjwMJLtiAtbQ6EBImeAFOHzMrUw07aMVBSHAfUmo8FR_rmWWl9O8AwaHuoMdxeEtvvBHlP52UtIHcyDEuhwfumA0p5CXzcGiPcUxX41_ImTvbxn_cxmlLZMgmT1wH1n_rxEdirfk8I-8YFHLjheg77M_zIQgxQWKUhe9c0HkhS6HhN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاوت آیاتی از کلام‌الله مجید ساعاتی پیش از اقامه نماز بر پیکر مطهر امام مجاهد شهید و شهدای خانواده ایشان در مصلی امام خمینی(ره) تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666711" target="_blank">📅 05:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ab3494ed.mp4?token=J6okp_K4vTo9B9lgjteWxsyTmP4XadUAbBExGtGiRmn_bvWAl2R6bIa3P3xeRlgCuUeBLT7tLJQdWy3YCEBDhODKAHWrGaQvr54Soo18wWHBjIRiPh9MRJ5aTEhPI23YaMMNHr5LReSNti96W10pZ9EBQokrdmqGgN0NnuQ-GgwkcTg3MU-wOztd7MLxw1MtkLJghq9nnbYxGDu_FPf3pW0N6wnc4ax7YJ-a6zVF-a4F3VCSQ22YJHhIiyo4BBgNe-phLxHvUITKc510SSQux50d2CiBWD97ZXNG8sRPeAjF1zrI6k23UeX7X5p3ck9SEvOCOt9_IqJ1AfSSvbH9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ab3494ed.mp4?token=J6okp_K4vTo9B9lgjteWxsyTmP4XadUAbBExGtGiRmn_bvWAl2R6bIa3P3xeRlgCuUeBLT7tLJQdWy3YCEBDhODKAHWrGaQvr54Soo18wWHBjIRiPh9MRJ5aTEhPI23YaMMNHr5LReSNti96W10pZ9EBQokrdmqGgN0NnuQ-GgwkcTg3MU-wOztd7MLxw1MtkLJghq9nnbYxGDu_FPf3pW0N6wnc4ax7YJ-a6zVF-a4F3VCSQ22YJHhIiyo4BBgNe-phLxHvUITKc510SSQux50d2CiBWD97ZXNG8sRPeAjF1zrI6k23UeX7X5p3ck9SEvOCOt9_IqJ1AfSSvbH9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مترو مصلی امام خمینی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/666710" target="_blank">📅 05:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931c136654.mp4?token=Ah1zKO1HrY0XYCsMcAwXJExJRxgNmSUMXMoPJkMKTx6lvAcd_f2NehibFJ1aAZn2as3wd2wDhr9Zc-v26OIrW52qjSzdVC6tFz8ivnaB61sIAYkpc2zUBO9rdQDSCP7U0E8fJyAF7T9raynBfsRaGPn0rWKiEILe5lXRk57rF3RVFHWcTGnB6DBDXECKV0St-xsU7LfkHyn1BaykWlHmeFaH0IRcKrBeqUDnKNfhMKs9TOKu9K3leJryp41Z2CDQW-HuTP0K9QzpSEjMLdhkrZds1RnRWw6py3HFk7VJypSeBqw1B422aFHtEz-_IjwNeD1mVzD2FIT16_SpOJwn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931c136654.mp4?token=Ah1zKO1HrY0XYCsMcAwXJExJRxgNmSUMXMoPJkMKTx6lvAcd_f2NehibFJ1aAZn2as3wd2wDhr9Zc-v26OIrW52qjSzdVC6tFz8ivnaB61sIAYkpc2zUBO9rdQDSCP7U0E8fJyAF7T9raynBfsRaGPn0rWKiEILe5lXRk57rF3RVFHWcTGnB6DBDXECKV0St-xsU7LfkHyn1BaykWlHmeFaH0IRcKrBeqUDnKNfhMKs9TOKu9K3leJryp41Z2CDQW-HuTP0K9QzpSEjMLdhkrZds1RnRWw6py3HFk7VJypSeBqw1B422aFHtEz-_IjwNeD1mVzD2FIT16_SpOJwn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مردم حاضر در مصلای تهران، هنگام پخش صدای آقای شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/666709" target="_blank">📅 05:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd02608ec7.mp4?token=MKCCw_gg8bPEuSgCqRUZScW5pOlqnxcxReaYdPkdSEd_pm--WiNdb-whpHWjBb4FPhrEuk8g6CwDEzkuilOx0SjTGPV6CMnjaIv3_VVaDk3HhK5UxEQS8sfJpU9Qf2spzJRucxI8Cz3_hMAwJwMLEehsOgF8gT2BfUD8cxLYxX3EQF8GYFRF6r5fWNOCfWuCGrxvK0cLgSflzg-WIvzVzEQ9TZWv98u4xwOst9pd9RM6IXQowiRkVG6pHdw-60zK1p1addyMEV3kuWnbnyCUfVIyIXWiKIvC9NxUoOEt2zWMj6tKXDWC0yddJ86MmnTwS-vSgDCLHKEPoJmE5Tp0Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd02608ec7.mp4?token=MKCCw_gg8bPEuSgCqRUZScW5pOlqnxcxReaYdPkdSEd_pm--WiNdb-whpHWjBb4FPhrEuk8g6CwDEzkuilOx0SjTGPV6CMnjaIv3_VVaDk3HhK5UxEQS8sfJpU9Qf2spzJRucxI8Cz3_hMAwJwMLEehsOgF8gT2BfUD8cxLYxX3EQF8GYFRF6r5fWNOCfWuCGrxvK0cLgSflzg-WIvzVzEQ9TZWv98u4xwOst9pd9RM6IXQowiRkVG6pHdw-60zK1p1addyMEV3kuWnbnyCUfVIyIXWiKIvC9NxUoOEt2zWMj6tKXDWC0yddJ86MmnTwS-vSgDCLHKEPoJmE5Tp0Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت متراکم و روان برای ورود به صحن مصلی تهران جهت اقامه نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/666708" target="_blank">📅 05:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoYi5JgWCnWMhYfuqYuzQLLYDt5t9iO-N55Jsab-pmVMqeBp8b8OcDGTXtZF4SNfxdcQp6UxCQsAxTvp3vITKK7krmC-t5k5OKKj6wGpsOt5K9YL1CuAyQ0TwiUZLrkiw1opG5EJgXuUV4NQCEPiQl_T3wTid2AOHa5m20nJD9jW0vGm-tHLrxfZV2kKsnEJ3hMbUZPobZlGcyYnpcr2P1eCL-9gyXQT8AA8v28q0Ziy6WLo9I8zU6qJcD6jhHx1ge9qJrwDRXxAQ2jt2sA_XZg8rlllICjsfv4sroqtQ-tHCMIB-bIkELaCngXA3MpaeyDBha1vcZSVe3WnJOnEHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک‌سال پیش در چنین روزی؛
یعنی ۱۴ تیرماه ۱۴۰۴
رهبر شهید انقلاب به مجلس عزای سیدالشهدا علیه‌السلام در شب عاشورا آمدند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/666707" target="_blank">📅 05:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17903c3872.mp4?token=KuOTPwGIEpFeOhEzdka0gP0Gth4OEzJPW-mYL-cnHc7Fk_1ekKF7VOv06V8WdIq2K5WQmZjf6wMW7oMpUnT8BDyYrpxgQSQLgoo9dh-HMx53IHLy2vawTDupYTACHt2NuiM4BkUp0YsE6ArG2LAZJbnnWV9ODQD2KhBsAatIIib16P_Sq76AC6YsQR0ixIlJMs4QsbZsnIA3s82vkxgyW76oSEzUW2BvY5VgIHznlGrZEuXypP5IojNbbaAZi6BNqRRUqN5xafGkG_Lf8aly-6XNtXmxlkRv8mgyngssVWeS2WhALDXAXoddxzVWNJKObWYchaBmAh9rFYp2djFD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17903c3872.mp4?token=KuOTPwGIEpFeOhEzdka0gP0Gth4OEzJPW-mYL-cnHc7Fk_1ekKF7VOv06V8WdIq2K5WQmZjf6wMW7oMpUnT8BDyYrpxgQSQLgoo9dh-HMx53IHLy2vawTDupYTACHt2NuiM4BkUp0YsE6ArG2LAZJbnnWV9ODQD2KhBsAatIIib16P_Sq76AC6YsQR0ixIlJMs4QsbZsnIA3s82vkxgyW76oSEzUW2BvY5VgIHznlGrZEuXypP5IojNbbaAZi6BNqRRUqN5xafGkG_Lf8aly-6XNtXmxlkRv8mgyngssVWeS2WhALDXAXoddxzVWNJKObWYchaBmAh9rFYp2djFD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین «لبیک سید مجتبی» در مصلی تهران ساعاتی قبل از اقامه نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/666706" target="_blank">📅 05:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/245f44286f.mp4?token=NNzRv6K5ZMtCXxw3WMY6s0NbBS2Y8AQiNfvdT_cZpGaTrZINf72gKTgE_10ZO0byzOnktahON6XvALc-wbzEPPkQoLyALAI8SpmuFGX9BEpQ60I7zYKIvpna7flwWrv75X5cO3BHpfR69nRf1lht8H4kpMmmFYK2gVPOeZ2wKMrLx4nkYqIvOwZUa2ZygchhB-7_YmW803U7B-IvV14W7HQl_Ykej6rJi1jkWNkEudZB6flZKUC08ZNMKktAOhNNqH8vVsgxZ87X39sHVy-_xQrYjU38kgpZoldaBMav5N9uWmDdJZG9ETCHc0NjhoT9zrE1zV54vah2m9eezwKTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/245f44286f.mp4?token=NNzRv6K5ZMtCXxw3WMY6s0NbBS2Y8AQiNfvdT_cZpGaTrZINf72gKTgE_10ZO0byzOnktahON6XvALc-wbzEPPkQoLyALAI8SpmuFGX9BEpQ60I7zYKIvpna7flwWrv75X5cO3BHpfR69nRf1lht8H4kpMmmFYK2gVPOeZ2wKMrLx4nkYqIvOwZUa2ZygchhB-7_YmW803U7B-IvV14W7HQl_Ykej6rJi1jkWNkEudZB6flZKUC08ZNMKktAOhNNqH8vVsgxZ87X39sHVy-_xQrYjU38kgpZoldaBMav5N9uWmDdJZG9ETCHc0NjhoT9zrE1zV54vah2m9eezwKTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورودی اتوبان قم به تهران و ترافیک ورود میهمان مراسم وداع و تشییع امام شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/666705" target="_blank">📅 05:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1520eece.mp4?token=irgMhV8wzfOZs5u_jbbv2RRLkc3t18TSJxZ1JSDZFDLrSnRLSqAeCvNKFLcSawyKnAiE0nYyMi8gx9hkxouZCTtaasXlhhtWdDPVxyr_tLPqhU6Ll2gexfoYlAlZNen1Aa862Si6c_DE2x3o2FTq2-P5OxCSbPMlokowRJuZhM0UB852f0IwV539UbhyKweU3MvVJ66XVdZ9iYva0T1l-iHzHFyIWv729zTMtlz2Ye0yQ1ESQ493v7mvf0cMAwPSPTzv3tuqApxoUyd3zrDQWidXxn9P_zvCIqzYBoAHoeDoObTydlTT8Qd_kB-KV2wrb5Rdioj2zBlJ3FmnlmQpJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1520eece.mp4?token=irgMhV8wzfOZs5u_jbbv2RRLkc3t18TSJxZ1JSDZFDLrSnRLSqAeCvNKFLcSawyKnAiE0nYyMi8gx9hkxouZCTtaasXlhhtWdDPVxyr_tLPqhU6Ll2gexfoYlAlZNen1Aa862Si6c_DE2x3o2FTq2-P5OxCSbPMlokowRJuZhM0UB852f0IwV539UbhyKweU3MvVJ66XVdZ9iYva0T1l-iHzHFyIWv729zTMtlz2Ye0yQ1ESQ493v7mvf0cMAwPSPTzv3tuqApxoUyd3zrDQWidXxn9P_zvCIqzYBoAHoeDoObTydlTT8Qd_kB-KV2wrb5Rdioj2zBlJ3FmnlmQpJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلی تهران و جمعیتی که برای وداع با پدر امت در سحرگاه یکشنبه حضور پیدا کردند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/666704" target="_blank">📅 04:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae95ef246.mp4?token=BJGf8M3CvZKDUuO5GoI2HWDd0_R68-L_eapmWYOf3sYtHOckPABVfNecSQhM1nuwO2z-mozhIsxLu87Z5rjaKJxN34YcjEIcmcfJIC7dMIW6lh3D5bPNFhNaY_1mmE9pnsjMnhc4_ftPzPBoJtQweoZBYisB45_EYBMmVn1iTQIvcuRPseqdAA1Z2GKFpQfKhlFV9b48ul_gV5riSBJYpAeAFoJymFrExb1WaqWt0nJS5061wakXXXeZxGnnM3t28htbZeC7s8DSR5wO-PeFRM5NsmeDixdaNATAio4PyXkORxUFnrshK8z2fOD3Sm-CfIZGtVfcyPxF0z2NCR9BX7CoyMnmfbb2t3U0RF2eMo0dlm1OKjidN37K6jUeNBj36c2GAcgNMWTEojRqgywFdZ0jUX8XFs2wXaaKGG2G1SwtG5mdLOSSOvF2qIHd6ev3jryjUzcB_0LXfcUi4l_9sTFJkGyebcfoJ2ougjumjKbltYwTNDxSTkzKT_v7GTsrE9zZUAjBxpavgTxX4rrGBimnikljbJ3bHbtMqdMP6PhxDVPk1RcNQLviBLv5WKWzFVxmbAxjIOt2wOLqQBjc5hYN4I4YwaNapG7_b-9uzeIeuMC_iHlPVP1Rx8iBFGZ_W2TEZnH3gPKShZ0Bbt3413VAwBBpbAAbeoXnLwL8qhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae95ef246.mp4?token=BJGf8M3CvZKDUuO5GoI2HWDd0_R68-L_eapmWYOf3sYtHOckPABVfNecSQhM1nuwO2z-mozhIsxLu87Z5rjaKJxN34YcjEIcmcfJIC7dMIW6lh3D5bPNFhNaY_1mmE9pnsjMnhc4_ftPzPBoJtQweoZBYisB45_EYBMmVn1iTQIvcuRPseqdAA1Z2GKFpQfKhlFV9b48ul_gV5riSBJYpAeAFoJymFrExb1WaqWt0nJS5061wakXXXeZxGnnM3t28htbZeC7s8DSR5wO-PeFRM5NsmeDixdaNATAio4PyXkORxUFnrshK8z2fOD3Sm-CfIZGtVfcyPxF0z2NCR9BX7CoyMnmfbb2t3U0RF2eMo0dlm1OKjidN37K6jUeNBj36c2GAcgNMWTEojRqgywFdZ0jUX8XFs2wXaaKGG2G1SwtG5mdLOSSOvF2qIHd6ev3jryjUzcB_0LXfcUi4l_9sTFJkGyebcfoJ2ougjumjKbltYwTNDxSTkzKT_v7GTsrE9zZUAjBxpavgTxX4rrGBimnikljbJ3bHbtMqdMP6PhxDVPk1RcNQLviBLv5WKWzFVxmbAxjIOt2wOLqQBjc5hYN4I4YwaNapG7_b-9uzeIeuMC_iHlPVP1Rx8iBFGZ_W2TEZnH3gPKShZ0Bbt3413VAwBBpbAAbeoXnLwL8qhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر مظلومِ شهید، خدانگهدار...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/666703" target="_blank">📅 04:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5891bf502.mp4?token=BW2k-G4x7DEcus4uNrisMeueJmn30fWCDrniIpnhNfUY8WdzADG60Mda-O_Jr7ffuX6QwDZ2VYYYfhBq03JGTcDLpqAVigsXix0Bkh5YHrPm7e4tgIH5hAsyO40IDfTvtr9WMoRn43FC33n-UWGa4f4ygAzJ1qGeFBv3SF67qsA5G3ulYeV-ofropg90JqhJ32yORm0CHtd3BnBCPFgyd3Y-E4H-RkvsFYN8yodqITIjXnpdT6niGXoorBtEpBr62fZPBQB_FpleGLfTAG889QIBRPKaOOPtCLwuMomrJbYh7KjmylQXCKAPhkVqZJbAI-K_E4dMFqF8SJJXqN63Bl5IlFG8ItlFes4apMKfPV87shzVhRCtXN7RVahTGJKbiiSk5ggMg2cujgRyc1splzbZGzJpYkS6MR4ocNrw6qJOFq9YTpyarLMD6yW3o-86OBJH8XVurue7aU5oVule6Ok7ii8wEXYlL1C7W6BksqZwz_qOusFT3pb7PCItgK3F9R2GFBH1iOLPufMZ_BxD6URDeE80RqkmUMbHba6SZNfNjjJPnrDbvwLGsI0gAlsgIBsYFl7fKOlTTS74NqmTxEQAABermQaap-E4EC57ru6guBjqzEstuj3duu3VIwkVyIpHum3rjHSoa2CsslcB7uhysJmBWxxkDorzpBp0pi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5891bf502.mp4?token=BW2k-G4x7DEcus4uNrisMeueJmn30fWCDrniIpnhNfUY8WdzADG60Mda-O_Jr7ffuX6QwDZ2VYYYfhBq03JGTcDLpqAVigsXix0Bkh5YHrPm7e4tgIH5hAsyO40IDfTvtr9WMoRn43FC33n-UWGa4f4ygAzJ1qGeFBv3SF67qsA5G3ulYeV-ofropg90JqhJ32yORm0CHtd3BnBCPFgyd3Y-E4H-RkvsFYN8yodqITIjXnpdT6niGXoorBtEpBr62fZPBQB_FpleGLfTAG889QIBRPKaOOPtCLwuMomrJbYh7KjmylQXCKAPhkVqZJbAI-K_E4dMFqF8SJJXqN63Bl5IlFG8ItlFes4apMKfPV87shzVhRCtXN7RVahTGJKbiiSk5ggMg2cujgRyc1splzbZGzJpYkS6MR4ocNrw6qJOFq9YTpyarLMD6yW3o-86OBJH8XVurue7aU5oVule6Ok7ii8wEXYlL1C7W6BksqZwz_qOusFT3pb7PCItgK3F9R2GFBH1iOLPufMZ_BxD6URDeE80RqkmUMbHba6SZNfNjjJPnrDbvwLGsI0gAlsgIBsYFl7fKOlTTS74NqmTxEQAABermQaap-E4EC57ru6guBjqzEstuj3duu3VIwkVyIpHum3rjHSoa2CsslcB7uhysJmBWxxkDorzpBp0pi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت زیارت عاشورا در مراسم وداع با رهبر شهید انقلاب در مصلی امام خمینی (ره) تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666702" target="_blank">📅 04:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af442446f5.mp4?token=skqSUORSFfqeDUBq4yk3fyoBUtKYTj5jtelxawtWvPd8rcfuOwoTWQKLX0wb2z76UopP-TjAC39XhZQaelBVyWxd-uNy7trqytdkMnAffxs7Ptt8g3baGo-jD-sP_vHqEwQm8kwwSqC-xNFAyLN7Jo_BZkwhyfQVMuTOmbyLzBfkabjPbXFmlLnIUl91t8Xy5-sHiTsVkaWKjPlSrmvof9R01C3M8gFHuO-P4uveBPRLPp88xyNmoPfsarDg8WvRzJ1jLGUpP7QUY2-rolNKFi_sepLU5D_5v_5oKEDyJ6hqFJ8A2KpRQRMjKmg_Js9sx1RGC3rI8GwpSmrOB64paA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af442446f5.mp4?token=skqSUORSFfqeDUBq4yk3fyoBUtKYTj5jtelxawtWvPd8rcfuOwoTWQKLX0wb2z76UopP-TjAC39XhZQaelBVyWxd-uNy7trqytdkMnAffxs7Ptt8g3baGo-jD-sP_vHqEwQm8kwwSqC-xNFAyLN7Jo_BZkwhyfQVMuTOmbyLzBfkabjPbXFmlLnIUl91t8Xy5-sHiTsVkaWKjPlSrmvof9R01C3M8gFHuO-P4uveBPRLPp88xyNmoPfsarDg8WvRzJ1jLGUpP7QUY2-rolNKFi_sepLU5D_5v_5oKEDyJ6hqFJ8A2KpRQRMjKmg_Js9sx1RGC3rI8GwpSmrOB64paA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت حاضر در مترو صادقیه؛ حرکت به سمت مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666701" target="_blank">📅 04:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666700">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868bd0c26a.mp4?token=bax4iB_7pQZ0r7YOnIIGO8wbXF-qvb_fbhw9Mf9EtbEbKtQJpTgPvo-4btE09hNh1rd3u3aLLYkILEQ5ISvB7QCQ2brJFEKv0uSrkmReaQunCzqrmP0PgreKAm3qFbb3WdRh8W1gSK8zCffYPsVIkWP1L0uU2-fqGvcAYWyhC7K4aJWaCUUVD02avHjP_pg7sXgmchoPF97PxdDKCQU6_tMwST2rRv0nNQ1vZ1r9-WGuDJIRPRmtia61Y6g3hfKPnb83qjLGdrI4AxyqnvmJ06CofxPds9-7MF_dn7ZCtI-SSb9Xgim9NVzdOlxM0cUhUP6ogzqvLJRnUSy8BLSiVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868bd0c26a.mp4?token=bax4iB_7pQZ0r7YOnIIGO8wbXF-qvb_fbhw9Mf9EtbEbKtQJpTgPvo-4btE09hNh1rd3u3aLLYkILEQ5ISvB7QCQ2brJFEKv0uSrkmReaQunCzqrmP0PgreKAm3qFbb3WdRh8W1gSK8zCffYPsVIkWP1L0uU2-fqGvcAYWyhC7K4aJWaCUUVD02avHjP_pg7sXgmchoPF97PxdDKCQU6_tMwST2rRv0nNQ1vZ1r9-WGuDJIRPRmtia61Y6g3hfKPnb83qjLGdrI4AxyqnvmJ06CofxPds9-7MF_dn7ZCtI-SSb9Xgim9NVzdOlxM0cUhUP6ogzqvLJRnUSy8BLSiVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت مردم به سمت مصلای تهران ادامه دارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/666700" target="_blank">📅 04:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
شعار مرگ بر آمریکا در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/666699" target="_blank">📅 04:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666698">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4ec55162.mp4?token=hiX-8vJhR-rI4uAh_VJNY85oPoadX1HWvKw6xrWLFyowSjXeL2VSEJNPwLPcopPIrqWfWibNkcQsufctMz0hjahBjA4b28QgDSCpVfjmtcLoRec1oWmKeANrI7qy-AL4DIhxbDmw7Nt3BiNKM1evnF9v5tp3kjY9zJhQqRpjPVeHcbLkd7D9OfMVwbxatyBZSBMDKJ4uG0h1QOFptbYMAvggOi5S2YHwL3SAD0aPbi5CbJK50HLbCYbOWgebIK5Sg3bnjd3Tm-avdeiKKbW17Ebd1cjMMN3WW49xEYy-_eZNh2eGH-pEO7YPWPMdfs7RpGLR_yuEFx8iT5Ml8GXGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4ec55162.mp4?token=hiX-8vJhR-rI4uAh_VJNY85oPoadX1HWvKw6xrWLFyowSjXeL2VSEJNPwLPcopPIrqWfWibNkcQsufctMz0hjahBjA4b28QgDSCpVfjmtcLoRec1oWmKeANrI7qy-AL4DIhxbDmw7Nt3BiNKM1evnF9v5tp3kjY9zJhQqRpjPVeHcbLkd7D9OfMVwbxatyBZSBMDKJ4uG0h1QOFptbYMAvggOi5S2YHwL3SAD0aPbi5CbJK50HLbCYbOWgebIK5Sg3bnjd3Tm-avdeiKKbW17Ebd1cjMMN3WW49xEYy-_eZNh2eGH-pEO7YPWPMdfs7RpGLR_yuEFx8iT5Ml8GXGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم متبرک به ضریح و بارگاه منور حرم امام حسین علیه‌السلام در بین مردم عزادار رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/666698" target="_blank">📅 04:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqMfqeFREmfGgjR7mBzq2GsRRGxPuQYJjNemsQsWkbLfwI3lSrLI3YFS3_PT_6HB-kO7WhMf1q9C4KEuz4gRi5dXBc966m6pRBv_EhG-BYFZriuFMDkmwSVeyuKkbnwJjN0uQ6wkbnZL67McRamwK-lVexp67_Gm8k90lJ3rYpEDXDLrno8nIpyPJgwVdMaf7SUn5q6wqh2JzpnE7PzUpc9dhQe_-fKBdw1n9SbOZt4OOG8Dk7Wje5ShAS0z36CujBxmt-HNHvo56ybi0ffTpCB6NinynvY3WbtkvhnepqUpSvmpmzVJj2KzbJbE8ZXOLl_4uGwylx5QIYojrDK4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzmX807GG28oTJIAkRLqWlmfxZDQ3IsjqRlSEMU6jRddgccIopQp-l6XajyNcqVcwZ4p865vQ-PwDWUzm1CrAUZehcol3IiEeKGJ8et4XorpHMah2_TTYXDQysQBol48gX-_4KOgokzIi0YXZtVvX7hDpch-NbrfSEuhsbRITvWna8RW4JR5jCWqQaYNbOQJiZqe2Sf87oYa0UiV69WV3cR7poX7u87w6uW_d5vAkGp4EASv32IfuwMpw_NjWWs6_W4VFyAWsOMj2JZKYwSZ77mvUVKwwcBC0uITF-BY3PF67Yz_3rDzc03dHIPnktulV1uQV1m3JJKIRV7b6aeuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3xfXFUc1FQLD7dj6lCvKdKKQOF2NJUnp5e92p_uwSoVHPLqwrafLK37W5L_GP3HFn-C5jeD8PaoZ7mpUsAkvMbtLnJSm17rLqD4uGx5vfMyhlHF9Mv09_xWwhZFl_f6KJpvTrqOL70D7AG4a4Yr7lc7p2qN9SPwp71ZiYAaNnpFxI7RInSGxIoBkatNrC2-NfGPUqPN9KhHkbLF1YhwpbOc4v37bCXjiFYzzNcnn7LFDu3LYb4g4hi2rlD2uO-IgAulRKByOfWpJordx_6kZ3UIZ7LpYVcIvWDg-IkgWBSX6XQmyi0bwmaqjUiELS2jlxznVsa9QCqldCOcgMIewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUk1Bnjxhz_UtqDauDrn8ecdJGcIOYC4vIPeCPr2Ay2Z25-D1jER9w27ZX6a19QgD0yMNToWDZMlE5VQlC8vvkghwjODbcs52_h0wcd_0B964-45YtfZQ-8mCcE-yipMMEtMML8uNJQ_yiT0PaiCyk8Bd7xG465ZefeVlIL9T6v_s1hiMiJXpq4p5K9-PFUee5ZY4H6no3iRUbXEdUhtnlCkSD2HJgD4kM-pn7HsOaLEntEIANgmAxdW21J57qKYRp2iUp2q8KhrCJVJgW4bfK9TKQlYvWmBwlQHkZRC9DgLcMkczmscp9k3DttPWCVl-ytLTuiUvSSLuPz4KXGmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFi0454WgstoMSQRYP155E-IbGLtbQ4O6Bt-_E3xqF05zVlKXKFN08KayzOgvI-T88emAO7T8hHY4LU6ahidAakyFHquo2cnvjsK7idLYcZ4dqUkG1hc9AdJima5LZzhSl_OfOZFgir8aKqyXnhYCBjCYVbGxo6tAb6uB_xBgU6Y6Y116ZUXc6hPjbU-E7u3QPc9s4dDA-t0ylW9UeDN6QcH-daU7ml2As5lRvZ2UsS5o1xunS-YFASHFzemboHOQIubLIvDHTxGMCww2dMPH-DtbJJ83O8oXhSUdVCsKCSy1mcBLJgH7FWkUfp9FpAeyS2ESz1GVL1nhA0HnCTUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6rY9EmjeyDi_z61wUrkCjOAEqWw_LnQFIpxI67snzFsP5xXlH0SMYcvqwzXe6W0x9AXX8RAN-b_9BOTC1990NAfk9jQe9J7pNRosX1oEVgx1fzKpauf3cwcnG2t0MmBniilGe2lWXkwNg7EsRVlVXvkRCwJRzvVetD8d4uEe3B--SN9qZoRBcCvntKCAEr1fJA0OqGZc7KJok7JuuikP2ncVtlKScuveIOKvjIGPT_U5oQ68SapACwG8nVQrQkqDZMlsdkvyDLZivQE4LUvpWPU6LYvuLMvzOBPx1jBiYV7YD93q6FU834-sJeFxj0K5AbqMpECtrTSedd5iA3SOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvZpSpQu6CFr084Q6G0jkQJvc8SAl-D_2ujQ-ttaF9vOCvdCLICzdy94WDTYTtCi_3UwM-kZ1nce8LuK4AXizdGgWcIc1JZ0T-8PEC_Dvo6XTwlkxVaezRzRPq7MBq7NX8aqbxfIGSmloQ5G4X-K5Ifw7y4L4Q8U3YSJH8o5RWhvvz1PjPiuf630-axgOeNIrBzmO8x_NTh05Wgevo3canrgP0ih5xos5UNOXCs2AZb9eZgtFXhgjAoBVnmuOiagZZN7O3IqRJkXKElcY-LhRPxStTPsJ04eURBQ6s9A_wE5v2Js8ToEVpF0ycQYJzdQ7_FtpHU9lgDNq80uHDCmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9PaIjGgx94upnwlhI8fw-YQoJ8mENleGs8AEQpLECxovfI5qb9-BacKX8z7ziJxoRIdaXb5qTN70nUC9Pwxu-nvPwPEkbVLvyJ_c9NvKFt8RCgs4UpbEPk_l4XCwRkCpkprppT1pnXqtUiaJ1YqZzglPhzLgPQIUFGM4BZrDJp5gwUSOhyZm4xaLV69xc5n71YBJ2mKeUzTood8Lozi6ACQhwdWbxuTj6vs9_wJ9bTIxX8nj5tuIj-BFoOzqo5XdZyU9suA-CwCZOhKNumPVSAQejLi2BYhRHzLc0kaedwCO7DfwtT80JRbpz83blloz2Y74U5mKJujxI69VzUjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YozNh86vh14NmxYFKqMCdmbrq9sllPLBQEHTUkf6fiorXOPx2ySA1dbA8ST1SzAk6DXaBcgNp-2n_PVcxTYoNGRhkkBgri1ZoJmpbmf4JgLPSYKxwouTR_9pupE8hPs3iaXSeCgzBK1t69rAtmOQdnqclHFuzgf78UCGmaOion0ozoyDZqHX6I1wPssBigKahhUExQvc2MgHUvi2cum-Iv-sZzpbfrmzNWIPgGdJhGl6t7Bcc8YmgDqagzFLNpNLvnQxZb7dt6EDdfX4V1lnbjV_t4vgUT24Nn95T7isUKYIC9ODCwjvKqnatUHWK6W9POiyMfPoq5LPtfK1woOuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLtaoJ0iy2g4pcoyR43ecZ7VPY7xs5g3wY0PmJsr-HHu80ptNq70_SL2-UnCL8ndcWyXPie6dqbQA5aEKm8nk4ECF2HClHU8QJNOW6_465aj6Z3sVW-uB8DfmsqoEC9YDNYa_VJsXejfGGjidJJp5nbvy-tcI865xEBLN29Ifg-oB-DyZbY37fd2kYBc2vnEYQKxfO-cX7fdCDldIhDnREOjKzZpbyWPb6oSwOXN-M-945boehj1FKsy1-hE5Hljhkg52vFt-uqjuPLh0d9-98F5dZBTcxFi-d4BT87WA-a2I-cbzZgZIRgxRtC-A7adIU6mE2QtPDcMBG3eesPkzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور شبانگاهی مردم عزادار در مراسم وداع با رهبر شهید انقلاب در مصلی امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/666687" target="_blank">📅 03:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حال‌وهوای لحظات ملکوتی اذان صبح در مصلی امام خمینی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/666686" target="_blank">📅 03:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قابی از تابوت شهید زهرا محمدی، نوه رهبر شهید انقلاب در مصلای تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666685" target="_blank">📅 03:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666681">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrFmtNanMv_Df4Uzs0MIJN4GfOgVd8_i3E0pErszQtVUyF1RfS0p_sw7IQRP8uvxkM2dYo1tXKEitRccLFGoepAd0ZDKy_yqB-DngUOtS2yf5mCH_tQX1majpZK4zS-g7rV3ubvDlFTZcNPj3qL8AY5lz6a8BAFpegnIGQNUcnqwyORaZFbcuDNI01A9JYsgjBe6IyMFUD4cC5ojdfJ3uM3TczY-3gh__tOpJOgUH4LoUK3Tuc7dzHwku7MSezdyCmuiciKCruYvqFdMt1OX2LGe8zm7NbjCW58ScCPbCEHZEij3KUBdJhgTmKC8dQ_oYJJGHL2LQ6ed5VULmALl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASfDMGRTgvudeqIVSv2rxUkYdAWu69x0nPDUw-yXleJedvYjTzGFPcmPFR-sZOGiVVkCJDwzpD5V5pFPiW9-hwPxgYMpDmEqNoR4cxpcLHpf9EbxRUt1oV56yzT6dJtXUkYhJL8MmwzZ5HLSdendSAax0d-d36Q8k-C7J9q89EcFIifjEFsyWZeeykjZf2RFfeLjPiDLOG9UFzTN8awENLhjT3Gr5l8LvG01QWZc8Boc5W7fO6B8A9A0nSYUsN5dNJqyHyqM0DiTvx3N7MJ7IYTLP-Cnr0zKYa6FK0EsG-9RPsz10yIEp7xcTTtnOoF83lE_U_-69BfkpxoyKomChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1xNjL-q1ejgKB8txNbykLNLoy65nO4s4Wnvk0GErAIkU-IOuRpgfSGMl83C9OMgjjnC9dip5y1DS6-XOScSIsJ0V8UI-ioc9SdiJsnqo-SzJdekdoaTa-nzl6MUbbZy815TzVC9X8UI3jY3YCkZOamrzIZY7HPV0xHaKd2UsJtKMFTeAHtBXgqArxx5Odri0ZLtTm25hNVP8a3cSRNsL2iMqEmgkcHOsAu61dadY_rpWjvuhJh-EhiAgXte1qfLEfXpJr9hUW_emmBaRtYEkcXFNv-y_1EAlJ9XMH-f2In2nm-9TiBNL8AEJ2W5iiGpl_3KXCJPY3IwFrBGkTQPxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f1a683e6.mp4?token=mBtk0qL5EIvESWlzkcP8naiSwSDOB5a8EPevOWbMurMNHyYufKzVUNcY7zH7PoOJDVJX9dYGnbjGiXfTf7ecEQGA2mdT9WmrO-zzJH483ClDYRusxkkkCLItdo_e7lZLVH9jL63dEDvlfG_wvXrS4JQPbFqf26xC8UBSNdsPnU7JYTBTRgZqnIZDzPRboTHh0SG1Y8qaDvSoo_l2cOpqNhlGDJR18LQh17foDjKKEzXu-dtwItl9nrF3B2ZeBl3FFN7dLOHUnLGlUnXeENcmq0Fg8ewtCdnyi7oko6vNwpgwoZ90IkkUUoZXaW8zNkIfe2m-sD0BAIDNzT2eV2-TOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f1a683e6.mp4?token=mBtk0qL5EIvESWlzkcP8naiSwSDOB5a8EPevOWbMurMNHyYufKzVUNcY7zH7PoOJDVJX9dYGnbjGiXfTf7ecEQGA2mdT9WmrO-zzJH483ClDYRusxkkkCLItdo_e7lZLVH9jL63dEDvlfG_wvXrS4JQPbFqf26xC8UBSNdsPnU7JYTBTRgZqnIZDzPRboTHh0SG1Y8qaDvSoo_l2cOpqNhlGDJR18LQh17foDjKKEzXu-dtwItl9nrF3B2ZeBl3FFN7dLOHUnLGlUnXeENcmq0Fg8ewtCdnyi7oko6vNwpgwoZ90IkkUUoZXaW8zNkIfe2m-sD0BAIDNzT2eV2-TOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی خیابان‌ها برای استقبال پیکر رهبر شهید انقلاب توسط مردم عراق
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/666681" target="_blank">📅 02:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666680">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJzHMUnrbqnA8LJsolx4g208bVTJHIlOTlPAx0-HY50jwTw6GbZBPd3zjIigP-Sekx5QimbC3mSZLjlGCpNZ3Ls3ab_JDB4ZDqE5kXWe1T_Gx7ZoGvLV91F-XVNUQmmFb0nTs9e9pOgMMIbYW544lJE8pcI1gqqRcgAiQZ86rN8nhAZ1JszEl5bxiGwDsfiFOk-Ayy2RevBMA2ie1pdxkxYbQRXvJSB78PTxzEv462vQkLioOVCbsvmwZuFh09OkT0UZy5ynsDrFf2fyerXUFlC-9FsyPzPS5rcWY36UIpbMNLV0baT6dBiKb-EwGoCLKfsT37NpUJf1NImYDF1FDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون؛ قابی ماندگار از وداع باشکوه مردم با رهبر شهید انقلاب در مصلی امام خمینی(ره) تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666680" target="_blank">📅 02:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666679">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-SLjLr9QXRsZk4MbndDd7LzlAmO8hUc2baHHSi-s6Fo1lBRFkz8tPA9Hre0t0X6jEIog_k9T_gBN7U2JF2SSlOTMpNeZCtiRinFTIQQiA0uJmnCoRN5r1O3jPXBGuHBCsrE0UhLOa6TZITNmDs1jQF9qVLkAWIEy1lRMRZuIc9vl0KwhQYAu1V2HTXYZTVde46Hl-eNpjClaTnQaJPq0YBDCU8BcuPaIw6DkQEHLZOuXoA7p4HpgLGDTwYF3QV4-_Y8GE0sYn70m9B77KZbcXva1q-12zLcZgNtvRuDZEFQ7S_iTNkEDX19qo-0vXqEE9VAaNyUhnoS5ERJVWS1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بروزرسانی نمودار مرحله حذفی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/666679" target="_blank">📅 02:44 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
