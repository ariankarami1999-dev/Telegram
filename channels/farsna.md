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
<img src="https://cdn4.telesco.pe/file/jWzjyXyU8AIkvGy5S8l6PfrHmHeK6jb2awPJr0bo0rgfbQ-R5Y-yH5Qh7ypRG07UDBYvRmb3gUuTRXLx7FzE4Rk_JiHodGhG8_yeIlx0yT_xOx_QyRZIfqrC41TC4tdFTB6f1CpvaOewuYjyBjf-Lnnj1j75HAHEwnGnK94BeKl0WBZQtyVu2a0quHRkEtuq1J2x1BmfhkuKJLJ3Qc1e7YpdUjyUTCJ1o8WWUG289gw-nPZikcnG-I9Gjju_EoJorehY39c8y6svTBv1-yFC7_X5MWBIfhEMkedfiBPOiP28K433V0OQL_P-cCrBgkpXPaNlV4bHbNCn5h3rg3uKIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 03:30:18</div>
<hr>

<div class="tg-post" id="msg-454325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1839906b.mp4?token=MoqmC-tzCzMdIhpzJcoLPNGHHBvgCdrYo2ZjPJ2YVI3odcQrwFAEAjgdrLGU27r_7fXFfeausPw83u7xHEgpnTdHiCE7Ci6uUYDACTmr9hvl-WjKB4IUshqbYBjqtuurjY4mv1yll8LVXRZSnpYmGp2vUFtqurjeMMoNjsWK8HXlb3ipF2WSu4urdA6zex5QogwcfUa34OWLaNVfTMjt4NbwmiGjt14gXTGcmuPX7Y6gwFOnYNWXRxBIMCijR8F2dsrS10jZQGtVg1WSPiQmxbU4i8QyptWdYxSAJrEvn1cJ9znUdIh2S1dBXpl0RsxGXLgxYUH4qtVplA-RZiheKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1839906b.mp4?token=MoqmC-tzCzMdIhpzJcoLPNGHHBvgCdrYo2ZjPJ2YVI3odcQrwFAEAjgdrLGU27r_7fXFfeausPw83u7xHEgpnTdHiCE7Ci6uUYDACTmr9hvl-WjKB4IUshqbYBjqtuurjY4mv1yll8LVXRZSnpYmGp2vUFtqurjeMMoNjsWK8HXlb3ipF2WSu4urdA6zex5QogwcfUa34OWLaNVfTMjt4NbwmiGjt14gXTGcmuPX7Y6gwFOnYNWXRxBIMCijR8F2dsrS10jZQGtVg1WSPiQmxbU4i8QyptWdYxSAJrEvn1cJ9znUdIh2S1dBXpl0RsxGXLgxYUH4qtVplA-RZiheKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران مزار رهبر شهید انقلاب در حرم مطهر رضوی در شب اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/farsna/454325" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-qwMlXwPs6SggoY9m0Zp1FdAs2EGb20cz8uHIcLEHp-YdG4alEO-__oCxGTIj3lk708u1vD-ru0d02boFhE0rW8N9YtDcuRivhTb_NCuLZfgckr9HcD8DciGG4vYmKWGor1N_WJlXvsdaUHhegCgZKz5bGOL0NLRSlF3q5h5JaITLU9-JJujzAfe_HVvsGLDrUs8dlWBBvc_2iWY01xQGCJ1n0zDQYSmjxCVEjNadh1mNNP_K2xGptOt3ODc5utxR5-NK5iyON2PAp4Ug5wCzb3HpTVU3ssfYzic8VEFa74ITE29I8XN5dZ-sjNa67IIn8bCBG_fw8rUuSYzCg8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوزویک قدرت ایران در تنگۀ هرمز را هسته‌ای‌تر از بمب خواند
🔹
نشریۀ نیوزویک در تحلیلی به نقل از یک مقام ارشد سابق نیروی دریایی آمریکا نوشته است که «قدرت ایران در تحمیل هزینه به اقتصاد جهانی، از برخی جهات، سلاحی قوی‌تر از بمب اتم است».
🔹
به نوشته نیوزویک، کارزار ایران برای اعمال فشار بر تردد بر تنگۀ هرمز، تأثیرات ویرانگری بر تجارت جهانی انرژی گذاشته و این تأثیرات در نقاط مختلف جهان از جمله ایالات متحده احساس شده است.
🔹
به اعتقاد این تحلیل، تسلط و اهرم فشار ایران بر این آبراه حیاتی، می‌تواند در نهایت سلاحی کارآمدتر از جنگ‌افزارهای اتمی باشد که آمریکا در سال ۱۹۴۵ وارد میدان نبرد کرد.
عکس: حسن قائدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/454324" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCivr1U2LJyhVDsMYmppCzcuAZmH6q6YC26kmK79fVLha_X27gfU33A_c8UHSN42YZCsLNy-zbRfmLx2F6G-TLfRDNc2SbDhrE_7wnHr2lphHzPmjsys76Q0-jqngk1talOgcLE18kBYvNh-YRf8M9rpnjwdyZ-oy8LhfvylMRP9d2ipbJ-jrMDb6TufCrs8Vc1C2EyBVBm7bS1tO7THH1JdXeyQLVotYz7EmWPFYb6YTk4pnEad8Lzg93T8MEPTPJqJcIFfNxS6E4FP5-LAJuceyrf5Bu4VP8LNkSiKU4eVdcuvj-Ba6pSb10nqALmOFDSKon1vhoQpKVn-rZbfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anKWIoNXN0ayGY0_itzABWUUsHhR563DrqOfgwgZJ0mdSiBFZ5zt7wbYuOLPstf3EPaSkY-1owEMcPA8bZRsqcMP8IXsaxlBfmLaZyacfuBf4RMQi0e_bR0N4dQJLtPJDyEKx1PidAwsEKRXahcPDIJMPfk2kTEqRrdZe04uzJp9X_euVmoIEKi-E6uGACD5MWzZfLyalV3Ygy_Hw3zgNdYh0taVMfmKbb5zF17MANVsrTH731ZK-OsVKVYI0h6fi-1oMQzumRKYhNlmxG4_r0eVykxBsaBSIBKwUQIoH3nh5smE92jn0utItUci4P85wf9SoI5zGMwa-UTVgWaMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exVa3VDxsoo6JDd5-1p_7GE6E9kkjB9y0mF0-DHvhefSMXG6ObnmFnc4vFVLu8cun6Da-lsr_VkLZWiWYpMc9OXaaw6v3K7RzyUBHO9eWxKJhpc2P_BTswIrxuhRWJ1HQ3hWpUG1vY_QGZzO5WBLt-2zR4_yFhHi3CGHN_qUowDVQIbD8hDAViK3BelcfKPaMfZBwmps_goNmcfKPYb7mgXluFFNS_tp54Xzqhj5gNcZJ5Hzmr02HZ0o3nk6m0LE3TUVB-5OYRsaAnNq1htu8ua-DzjFmPgv7rX6R2TGs05E5L5G1mZxpNnb0FnyXexkfyMsUt923cYSni1nimj2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XodA2A1SXVTLTh32VAh8-xupnbiBtOOMOowme1V7nTem7Rh31SGrEoYIsO-oJKATcfSs3DRy6SIlsbQXvOVFxY_07Z5QpJ56Fux3d0urBHXuieoLFt94BWHFFyQc-EL7k3i1XyuYnvRnb4VFTmVUOgDJXKPQLBNhkLZ_fwD9mZzBhvjcZBkI3o3OSKZ1yqOVeUAEVb3TBH8CD1MqSb8PsTpw5QVKejS3JfBDtlYLijkXSJAIvuSEoLF18HDpKt6ph_O3q8jcQmqh_0a9eCexSN3y4LPWRWA8PtAYNS0v_pYYDgAlM2poOjNrvQuGxYWclwhzeyvpBbgxtuPy2KDiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYYvx79K6F4-_BWhpl_exKV4oTWe44y4vNbf8QrsBDJ9rfQfNIc0Kdlz6PLR8gfRJPbPdW6mbd9V-eM1BKKbBTbtoB2IigFmLNNcJ08rFR5hIm70IwoS0SP-htZGJvUurzuCum2nupBjX348kCxdQsBuSjCt45ZrgzicwbU2tOW_NTsJcb5bQgP5oLdlxKsGyZ9s7bbI7LxtzEcpi02X4Hpz7ujMR3C5HpKlhfG0_eu7ktsh7ydOUF6AvLeaeA_eLVQXZlPXlt779L7qF5ndPxmAb3Lap-UPkbFmRXpodOaOGUc-kzXsYQkDJf3XABfFuMnQRa0gxrSO18l_pHWUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gK5B9JUfZdVwhqqpYA_X-0hmbLYyQbfjz6IysQCP6cmgmYpKsbctFKhO5zDiCFKDofSADVG3oMGtmZyO0BqyrGzK75MThz5DQZb7fyo6Ds3Bq756o62NVDXgyHekVkrXx6Lkea5OnUR01P4CfyNstTIZDs9gq1jX-JNiw1MW0i23bT4HsUXwNETONNbyy_YAhx6Mw_mZlrzJHE-K-NBP6W-gLq2MqsnAHchkP98UJkvdj__XxuovMjheIKexxfuClQak8_4XQUATyTLP7nLf94j8pADWWxP00n1obs978K1HTniKFVjdGskqffyKSb_-aE4MXfz_7orWJhNxtDpHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkyGdjaEIpfj_pS6rr8mgrHVRlEC-wbCtUjpYzUYt6lsgV_0UEtBk4iQIv9dAvk1JR2aKLEx4ZtbM0af0O_Ykfk1x-cwMBL3SHvjol_8DuR52Wz2epoMWDc6MCxYkU1jiQvfGxaJpVK9FSJzpogJoqdAY9LZAGZsb-Fwfz0rVD7cJi6uy5CDN1xDtPfQf1Po1iG5QNbADXlrMYd-LfuxMAPlliT0J_AiiBeYWrw0AywAHfZMbeeIV6LEuZCquSZTe3iHfaEDkvX3xfi8KJq7CwPDPfabcMTS2E9Bb9B8jjOKW71iOuycorEF3j2eP3x3CXHlEZxG_hZAsU0PSSP0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6l7xGr_De8TQr4XXcAcx_MK2noahZDEvvBJKDR1TaNxKBS746HXrL4NE7O7C9D7fxsReVj7FO51qOSQGmJz7TEn-3xA2oey4qSIjcAZAJzDshBYwhw2WnZhuXr5sXJ9r3W__Nq35GrEwKHTZWkbMR4ugZwV1CnYnTE5ueQaW5NGQ9DbRlYfGksnv3QisJ6a_CRxSC9bxgGePRE5dc9nU1EXYu50MexF7RFBMy-Hhy5e9gSeAdCrtccedNtecqgIHYeMpFNKe2393YMA1gha-sKfuNW5NoRU74IiEyofpBJF7PBGaE_YuX6hru9tKtDCD-RRUlSWeC4IA6KtET792A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXa9zsVUp8dVGDHeCt3sadVObOuU6vryRT0r8kOuoFpV_Lr8p9mGcEJs9Kmu9iJbQK9oF7h0zjUFLB23AZX84ZZG4CCDZUozT88KojiJpGnsFkPvHKp123cApB__lXpCTjT5awWY2ssvAG710F-LhvjETKubJwK1gblfnAuappWplBj-F4U_7HQ2Bijif5deDAXEeZ6iRZRD6NIuI3Y7Ra5zDa_xUzW5FkzvVr1ptnInBrc7IQmw6e_ET0zF7Knjukf4spxat2UNbfT3yGoX19_3LZtvfcW5BlYp8Ru4Io6hV4ahufvtGpNlHcTiOSRyi4EqfW_JUw7Ggp0g5UF-RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بین‌الحرمین در شب اربعین حسینی
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/454315" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
رسانه‌های عربی از آتش‌سوزی گسترده در مرکز کویت گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/454314" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa8d399fa.mp4?token=L4ZulVy_3_MFA5-qEZp6LJq_ZpB3eohe8hB2tATBDw3Ec4G4eJrn7abi8psmeFmXOqWoEPLF5WQpBL80LnIpCOXGXfn3hrPX-umXj0zbe6vuOMjXvAbZxOyPkIziYugyu4khzC2DeElmh64aDGbPMSlalsMysjqZ4khsu8uioHqqf2pfmVktJDAFcx9-NS6btv713RtQGa3pyTpJqzPCY62zw-agjwcO1NYWvsiua9nbU1jrq_8RFQL7oAdTCSolM8WRF8MPegD5oZJXnzuiDe_1XnjVGKhE-oJHTUjjZDWU_g3GhCow14RoZ6lPfCtpIobkZ3DJ3_MyCbCGi4_STA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa8d399fa.mp4?token=L4ZulVy_3_MFA5-qEZp6LJq_ZpB3eohe8hB2tATBDw3Ec4G4eJrn7abi8psmeFmXOqWoEPLF5WQpBL80LnIpCOXGXfn3hrPX-umXj0zbe6vuOMjXvAbZxOyPkIziYugyu4khzC2DeElmh64aDGbPMSlalsMysjqZ4khsu8uioHqqf2pfmVktJDAFcx9-NS6btv713RtQGa3pyTpJqzPCY62zw-agjwcO1NYWvsiua9nbU1jrq_8RFQL7oAdTCSolM8WRF8MPegD5oZJXnzuiDe_1XnjVGKhE-oJHTUjjZDWU_g3GhCow14RoZ6lPfCtpIobkZ3DJ3_MyCbCGi4_STA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از وقوع چندین انفجار شدید در کویت خبر می‌دهند.
🔹
گفته می‌شود صدای این انفجارها در جنوب عراق نیز شنیده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/454312" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
منابع عربی از وقوع چندین انفجار شدید در کویت خبر می‌دهند.
🔹
گفته می‌شود صدای این انفجارها در جنوب عراق نیز شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/454311" target="_blank">📅 02:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuGFja_To8RN5P-03x-wjGmJnbJftnS5aXEY40xacDrHbarQq029edhQj1l-ULm8xFQmnfmI3EB4T10NbTWUXWu2FRxK0en2wGkAwCQ4lXFgveVGPtvyS88NubuqkZn2tkSOXsvJCKZlQhvTAM5xn5hpVTiGmN05JrG1b7TceRmVANmV3Hfe7WlxI76MdEBIY6E5_PoeGjVa-BJgHQyXYxwvY2VPbDKeBxp9GLZmTwIL_5yhVtXa18A9QC_P75cfrwlaOjDDaUYtCahAtpy3024O4W6lnToKO102ioOxhGUznBO-3F5oK9Da2LEc2M3ocamwyXHnPvRvO8PQEnjaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر، ساعت ۱:۴۵ بامداد حوالی فارغان در استان هرمزگان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/454310" target="_blank">📅 02:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a992f7e7.mp4?token=kZhiWxEltcXwBQfByQHLQnZfQs-CmZ-vV9E9KKYA6ewfyjtyt7Dp1PeEvbHAeHzI8kL8TWXkZpRABwy7wsoIRFkvNu0hnoXy76WkoewiZkxXkmcFVBSpvy5xHKjct-afXLGS_URR1qXosDElYZXFS9Gq0SmgUBDQiyHTkHo0kSB0LpKjuNm2Pg5PdKcrD_nGN09XScHcyKZTyerIYNt0wNNpQ9BG4CZI-GZuRte5nPzalvpD1mHP6wtpfEgjjMUbsVLbjbE5eC2Qo-qQhqfqWBQmfNypMIc4wFEKBTx1BP04sDINjB08a8bhVyQRKar8OyCxRoaOM4pJ7_-gYJGV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a992f7e7.mp4?token=kZhiWxEltcXwBQfByQHLQnZfQs-CmZ-vV9E9KKYA6ewfyjtyt7Dp1PeEvbHAeHzI8kL8TWXkZpRABwy7wsoIRFkvNu0hnoXy76WkoewiZkxXkmcFVBSpvy5xHKjct-afXLGS_URR1qXosDElYZXFS9Gq0SmgUBDQiyHTkHo0kSB0LpKjuNm2Pg5PdKcrD_nGN09XScHcyKZTyerIYNt0wNNpQ9BG4CZI-GZuRte5nPzalvpD1mHP6wtpfEgjjMUbsVLbjbE5eC2Qo-qQhqfqWBQmfNypMIc4wFEKBTx1BP04sDINjB08a8bhVyQRKar8OyCxRoaOM4pJ7_-gYJGV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور شمار قربانیان زلزلۀ ونزوئلا از ۶ هزار نفر
🔹
رئیس پارلمان ونزوئلا اعلام کرد تعداد جان‌باختگان زلزلۀ اخیر در این کشور به ۶ هزار و ۱۲۵ نفر افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/454309" target="_blank">📅 02:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm327kTRTs9q51UzeXQohDOLlE8_VbwbD7rSK9DZA1fhud07EXFQc9bz2P5gVGdqIqVCFDCiWDUBaubo4bhmujcl-WA3aVgLFn-GDHeW76gD0ps-_WgRgHoX4QZfE9Gbb2JocznLh29u9GnVDc7Oxp64QERJfR982vIHTYoN_DOeSFc4IZW2XjNESPgTV2ovAelLOZxduWpAAWvKdty6Vg9XsEa4GjMzqlSbySifz4u_Sh95QQzqz-wyNP6h4ORpFQlCsCshZnW4V2je70NYgT1APEWkoc9HtKpAYjOybICoFs0AgKtI9v59OuZs-4Ie5em72LecB7My5k8jTZDFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بین‌الملل: کنوانسیون دریای خزر در خدمت منافع آمریکا، اروپا و اسرائیل است
🔹
احمد کاظمی استاد حقوق بین‌الملل، تصویب کنوانسیون رژیم حقوقی دریای کاسپین را یک امتیاز مستقیم راهبردی برای رژیم صهیونیستی دانست و گفت این کنوانسیون علاوه بر تأمین منافع راهبردی آمریکا، اروپا و ناتو، یک تهدید امنیتی برای ایران محسوب می‌شود.
🔹
وی بهره‌مندی رژیم صهیونیستی از تصویب کنوانسیون، حضور غیرمستقیم آمریکا و اسرائیل در دریای کاسپین، احداث خطوط لولۀ انرژی به سود غرب و به زیان ایران و چندین موارد دیگر را مهم‌ترین دلایل مخالفت خود اعلام کرد.
🔗
اما چرا تصویب این لایحه از جنبه‌های حقوقی، ژئوپلیتیکی، ژئواکونومیکی، امنیتی و نظامی، پیامدهای متعددی برای ایران به همراه خواهد داشت؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/454308" target="_blank">📅 01:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fbaafe73.mp4?token=q6GJ9QAp8kk7rRYRGMpkq1hW-laX49pCSzhE0gXoDvRDH6sxv5zh7Pz1tdKfPDmvSib3NsYNMvB3eGxGXRoXYLOlo2qpjFArOTwM2GHyrJx2M2e4FqIMvksFFBspjI24-s6CRKG65wmFHtxk3aQWY5zDIcxcsMPrZ6A7eCjPYC0n8Cupx-7A-lx6GZAMXZO9MYleEIjeOTocGZq8xAZADoEaTs0EEJ2rPyqY9SZPvMyhDI4Kwvg2xawjORJhWtLOPV9oNg-m0t6gY6FNfaD96NdgMTfD8kemp-d9o-ziiAbhbRttfavCbnQzqq4K67SvhXWT18A6cbGAvzAPwo4uWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fbaafe73.mp4?token=q6GJ9QAp8kk7rRYRGMpkq1hW-laX49pCSzhE0gXoDvRDH6sxv5zh7Pz1tdKfPDmvSib3NsYNMvB3eGxGXRoXYLOlo2qpjFArOTwM2GHyrJx2M2e4FqIMvksFFBspjI24-s6CRKG65wmFHtxk3aQWY5zDIcxcsMPrZ6A7eCjPYC0n8Cupx-7A-lx6GZAMXZO9MYleEIjeOTocGZq8xAZADoEaTs0EEJ2rPyqY9SZPvMyhDI4Kwvg2xawjORJhWtLOPV9oNg-m0t6gY6FNfaD96NdgMTfD8kemp-d9o-ziiAbhbRttfavCbnQzqq4K67SvhXWT18A6cbGAvzAPwo4uWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا صادقی برای پیاده‌های اربعین خواند
◾️
همزمان با فرارسیدن اربعین حسینی، نماهنگ «پیاده‌ها» با صدای رضا صادقی، منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/454307" target="_blank">📅 01:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZnBX0d9FepiNsD8WjAeT8yHw312fK9Ie1RvN-Wzfjl6AWiBB8D2QIBlX9p1V0aib-W8dJBhATpoxxFhwHnzBeIUJw5FWrqxNWePjjYTB2IsN8bLEDOyzdK5rgJmNefznhn60FOsCPiIHxGAdu5kWW7X6gp1CPNsMF5E_Vvw6fhcKeOqG--vAZLey_7Rka1jeEB9WalGDlWPoSOvnBLpvGOvXaThQcd0CrE-2vD_g8mf4-yLU60wagYlFziHmbHSXWE1MsRO8uGpUWXhQRBXfW8TSZMx_-qLPX8YWNsi3lPhwQXeepQo9BHkIG_9VK7gUxVyVFErZI8AtKUc8Y7eFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش حماس به زیاده‌خواهی نمایندۀ ترامپ در شورای صلح
🔸
ملادنوف رئیس شورای به اصطلاح صلح آمریکایی در دیدار با نتانیاهو مدعی شده بود که تا وقتی حماس به‌صورت کامل خلع سلاح نشود، نظامیان اشغالگر از نوار غزه خارج نمی‌شوند.
🔹
حماس نیز در واکنش به گزافه‌گویی وی اعلام کرد: گروه‌های مقاومت به تعهدات توافق شده متعهد هستند، اما رژیم صهیونیستی به هیچ‌کدام از تعهداتش پایبند نبوده است.
🔹
ما منتظر پاسخی روشن و رسمی از ملادنوف و میانجی‌ها درمورد توافقات هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/454306" target="_blank">📅 01:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03465f95c0.mp4?token=fK8co7N3wQ2WOwU1gokrbRsIoIyNxC5n9lOnFRlqQLulVNFteEjUtElmXHCLvLUkt9ba2-TbaoM88jbdUg4XgOcC_plXSVwyTecf-hIGjbb1i8Cay8Xv_DV1lwNCd1EDvBawsULJTgvd63sPELWH6-38Z-auCeYpmCEqL4fZkBLRO8tG5thB16XgXHaQ9AnYKkSUQZ_rXqIAyBIxlkue-x730QYL6ilw8C1cfOLUHd1OjolqTiGZTf_FtCyY7K4Tb7mRouzVqtKYnrxQC7lMGWv-kpmFAeCEYZ52Rh4Lbp_P-pkUN7ScfNrI2FPI3ZSHSwknJUBYhYX3cGS1527MsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03465f95c0.mp4?token=fK8co7N3wQ2WOwU1gokrbRsIoIyNxC5n9lOnFRlqQLulVNFteEjUtElmXHCLvLUkt9ba2-TbaoM88jbdUg4XgOcC_plXSVwyTecf-hIGjbb1i8Cay8Xv_DV1lwNCd1EDvBawsULJTgvd63sPELWH6-38Z-auCeYpmCEqL4fZkBLRO8tG5thB16XgXHaQ9AnYKkSUQZ_rXqIAyBIxlkue-x730QYL6ilw8C1cfOLUHd1OjolqTiGZTf_FtCyY7K4Tb7mRouzVqtKYnrxQC7lMGWv-kpmFAeCEYZ52Rh4Lbp_P-pkUN7ScfNrI2FPI3ZSHSwknJUBYhYX3cGS1527MsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع اربعینی مردم رشت در میدانِ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/454305" target="_blank">📅 00:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بازداشت معترضان به جنگ علیه ایران در مقابل کنگرۀ آمریکا
🔹
تعدادی از روحانیون مسیحی و فعالان حقوق بشر، در جریان اعتراض به جنگ علیه ایران و ابراز نگرانی دربارۀ حقوق رأی‌دهندگان در مقابل کنگرۀ آمریکا بازداشت شدند.
🔸
نظرسنجی‌ها نشان می‌دهد که اکثر مردم آمریکا مخالف تجاوز نظامی علیه ایران هستند. آمریکایی‌ها معتقدند که جنگ علیه ایران ارزش هزینه‌هایش را نداشته و خواستار پایان فوری درگیری‌ها هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/454304" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تأکید کشورهای میانجی بر فشار به اسرائیل برای اجرای توافق غزه
🔹
کشورهای میانجی توافق آتش‌بس در نوار غزه (قطر، مصر، ترکیه)، بیانیۀ مشترکی دربارۀ نقض‌های مستمر اسرائیل در غزه صادر کردند.
🔹
در این بیانیه نقض‌های مستمر اسرائیل در نوار غزه، به ویژه هدف قرار دادن تأسیسات و مراکز بهداشتی و درمانی و شهادت تعدادی از زنان و کودکان محکوم شد.
🔹
این کشورها با اشاره به اینکه این اقدامات نقض آشکار قوانین بین‌المللی و حقوق بین‌الملل بشردوستانه محسوب می‌شود، بر لزوم پایبندی اسرائیل به تمامی تعهدات خود بر اساس قوانین بین‌المللی و اجرای کامل الزامات مندرج در توافق آتش‌بس تأکید کردند.
🔹
در این بیانیه تأکید شد، ادامۀ این نقض‌ها به معنای شکست توافق بوده و تلاش‌های صورت گرفته برای اجرای مرحلۀ دوم آن را تضعیف می‌کند و مشکلات غیرنظامیان در نوار غزه را افزایش می‌دهد.
🔹
میانجی‌ها بار دیگر خواستار تضمین کامل حمایت از غیرنظامیان و دسترسی بدون مانع کمک‌های بشردوستانه و تجهیزات پزشکی به تمامی نقاط نوار غزه شدند.
🔸
میانجی‌ها همچنین از جامعۀ جهانی خواستند فشارهای لازم را بر اسرائیل وارد آورد تا به تعهدات خود بر اساس قوانین بین‌المللی و توافق آتش‌بس عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/454303" target="_blank">📅 00:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349825ca84.mp4?token=rZYslTCfNJtqSpZ5j23Zg7dk_WFO1Mc1pN3u7dc1VJ60dyY-SCUfAMLlC9THXFg-7HsIJ1S8qg9NpP5FXW8IM2UWmRO41bIbczejM_NuZQp5QbPJiTi-j9tWNFuRe680mqgMt9BbjcvVyy5AMzg0qNJWto6mft8YUTXO23SfJmGcqt-6obvrIUixXy9MjGQvPKby9psouijGBEx2R-u1s0Cl7OOT1ni5QmJSJ6Uedvz0dgrByYxkgtHfs4Wyi_QbjmPG1UXIG2vqXZfb84kcYHaYoFqxcShRVyvOoo6Zmbqb-kt1H7-4mF8VrLTfcRMqZ4UuRu3wsE8urkAf4LLpJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349825ca84.mp4?token=rZYslTCfNJtqSpZ5j23Zg7dk_WFO1Mc1pN3u7dc1VJ60dyY-SCUfAMLlC9THXFg-7HsIJ1S8qg9NpP5FXW8IM2UWmRO41bIbczejM_NuZQp5QbPJiTi-j9tWNFuRe680mqgMt9BbjcvVyy5AMzg0qNJWto6mft8YUTXO23SfJmGcqt-6obvrIUixXy9MjGQvPKby9psouijGBEx2R-u1s0Cl7OOT1ni5QmJSJ6Uedvz0dgrByYxkgtHfs4Wyi_QbjmPG1UXIG2vqXZfb84kcYHaYoFqxcShRVyvOoo6Zmbqb-kt1H7-4mF8VrLTfcRMqZ4UuRu3wsE8urkAf4LLpJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تایم‌لپس موج بازگشت زائران در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/454302" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70140da514.mp4?token=UHFXkKnfmsv0ZbkYpniA-7YMiaUeUYbmZ9vb37qMA4KEjXB0BpVkXV08hS9HBJvk_bv42nRgJYyjrXDHxHxXRhoj0w51zOM_EW6O-6FGPOtIu9gGUncO0ObU9DJLCyZPiAON9muFM5vg4LKjO8iCtazAfBuUUXDKH5KBnpj-RA89ZWMPFZ_WVAon0R3eZjc2yIrnnxxWiFVqpnmqr29Jy2YX5XxYBIvq7hEtRgQrCVGL5S0Stl2Z-2LvG91Qd9c6uYuNxBoGEQmbJQ7EohYf1qpp3mxVn2GV0FxzWSFrI9pehAGLZ9qqUyUZXWWtI3BsmZj8CWo8eMVG_GIg7W2PnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70140da514.mp4?token=UHFXkKnfmsv0ZbkYpniA-7YMiaUeUYbmZ9vb37qMA4KEjXB0BpVkXV08hS9HBJvk_bv42nRgJYyjrXDHxHxXRhoj0w51zOM_EW6O-6FGPOtIu9gGUncO0ObU9DJLCyZPiAON9muFM5vg4LKjO8iCtazAfBuUUXDKH5KBnpj-RA89ZWMPFZ_WVAon0R3eZjc2yIrnnxxWiFVqpnmqr29Jy2YX5XxYBIvq7hEtRgQrCVGL5S0Stl2Z-2LvG91Qd9c6uYuNxBoGEQmbJQ7EohYf1qpp3mxVn2GV0FxzWSFrI9pehAGLZ9qqUyUZXWWtI3BsmZj8CWo8eMVG_GIg7W2PnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از قرائت زیارت اربعین در حضور رهبر شهید انقلاب در حسینیه امام خمینی در سال ۱۳۹۹
@ّFarsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/454301" target="_blank">📅 23:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454300">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e029fa1916.mp4?token=sHYn-WTwtAH3PAAkmWD3LuMqHHmnBrDoDsOAC43zlDRGcWfLeoCs7OijqsUnhudantLlg_0Qtbx88Vcb1-IDkaGQLfmp3Fm1BQoUh5VjrENF2RBEzeO48rl09fCqND5xVWiSlkuWdxZ4Hx0DU0ceEkVjFe-kkDXm9AaW2rF3n0BWxU_LBGmhA92U5D7oZ3DDggkbbAlryHDh6pAdXfKEEbvjnYndCJunfjhqXIeXEVub9rctsoPnvd2dWzbzCOyI3wTfpDBIXp-WKnLEChIuHO-PUj6ylQ6tfa0-aMq6TkCof85Xb3QrCkgNzqBYDRkRIoffQPJIKuPJZANvMJndug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e029fa1916.mp4?token=sHYn-WTwtAH3PAAkmWD3LuMqHHmnBrDoDsOAC43zlDRGcWfLeoCs7OijqsUnhudantLlg_0Qtbx88Vcb1-IDkaGQLfmp3Fm1BQoUh5VjrENF2RBEzeO48rl09fCqND5xVWiSlkuWdxZ4Hx0DU0ceEkVjFe-kkDXm9AaW2rF3n0BWxU_LBGmhA92U5D7oZ3DDggkbbAlryHDh6pAdXfKEEbvjnYndCJunfjhqXIeXEVub9rctsoPnvd2dWzbzCOyI3wTfpDBIXp-WKnLEChIuHO-PUj6ylQ6tfa0-aMq6TkCof85Xb3QrCkgNzqBYDRkRIoffQPJIKuPJZANvMJndug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کرمانی‌ها شب اربعین هم در خیابان‌ها میدان‌داری کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/454300" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454299">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f36b90c1.mp4?token=NQ7kNlBrx8yKCYR9-ihBHYnZKS7QoLF58b7qlLd7vomfGj-XlxTUFXwPxQWxfr-fo3e1IFH16bF4zATcqaR1-8xDLyyxPgvFfvdUEeVuleL59adQzBgsmB862Jwu1a7YWHkuOBQSGS9L8LF4Rl8bl2pa623DVkaOG2xhoN13deK9lpHkXR737BxmltkqaMcUVI_4kZfYE8NMjpMO9bkncibOEDs9DoarJSzciHAiJtVMog1zk1TTwRFbxxKaNx2LrCKFO0MW9RRy-3wereorrtRwZYw707I2NKKIK-TOgn0GdMzLn9Ds2sfWn5_RGwzqCuC2-sT0efit9NoUw0n6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f36b90c1.mp4?token=NQ7kNlBrx8yKCYR9-ihBHYnZKS7QoLF58b7qlLd7vomfGj-XlxTUFXwPxQWxfr-fo3e1IFH16bF4zATcqaR1-8xDLyyxPgvFfvdUEeVuleL59adQzBgsmB862Jwu1a7YWHkuOBQSGS9L8LF4Rl8bl2pa623DVkaOG2xhoN13deK9lpHkXR737BxmltkqaMcUVI_4kZfYE8NMjpMO9bkncibOEDs9DoarJSzciHAiJtVMog1zk1TTwRFbxxKaNx2LrCKFO0MW9RRy-3wereorrtRwZYw707I2NKKIK-TOgn0GdMzLn9Ds2sfWn5_RGwzqCuC2-sT0efit9NoUw0n6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفارش امام رضاست، برا تو آه می‌کشم
🔹
نوحه‌خوانی شب اربعین در حرم مطهر امام رضا(ع).
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/454299" target="_blank">📅 23:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454298">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a7dc3048.mp4?token=UsaUEyk6gOLfJ_AWXbImnTLK_iDURwTn86pAnX60KFCYjvzckVXrbKBntj_H3ey-EHOQAgOhHE5xpwVOKpBaFqKQEk1cau-420o5aJMmVA-KOs9jqdgFFzqjhnZkUlT6iGCUswNZiTcOz95k_BnrakvTIhnHbQV6EBPALSEkkyONcyXvYnJNKXmUmfhDBI6WNz35u40xri35L8-5bLmRrOCwzdwNrH-S1tFVKu-dzfzGqJ-MJe9R_4r6GwrmiX1BPqQxkYMhEECJPaH7eFHz5wBcNHwlMA38p9S8UJ7UhRvOd6nYq3cA9ShAynXsunYNqOa3QJWgeAnZWaiMY5iR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a7dc3048.mp4?token=UsaUEyk6gOLfJ_AWXbImnTLK_iDURwTn86pAnX60KFCYjvzckVXrbKBntj_H3ey-EHOQAgOhHE5xpwVOKpBaFqKQEk1cau-420o5aJMmVA-KOs9jqdgFFzqjhnZkUlT6iGCUswNZiTcOz95k_BnrakvTIhnHbQV6EBPALSEkkyONcyXvYnJNKXmUmfhDBI6WNz35u40xri35L8-5bLmRrOCwzdwNrH-S1tFVKu-dzfzGqJ-MJe9R_4r6GwrmiX1BPqQxkYMhEECJPaH7eFHz5wBcNHwlMA38p9S8UJ7UhRvOd6nYq3cA9ShAynXsunYNqOa3QJWgeAnZWaiMY5iR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی حاج منصور ارضی در کربلای معلی
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/454298" target="_blank">📅 23:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454297">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی گروه فولاد مبارکه</strong></div>
<div class="tg-text">در مجمع عمومی سالیانه صورت گرفت؛
🎥
تشویق سهامداران فولاد مبارکه؛ اعلام رضایت از عملکرد مثبت در سال پرچالش۱۴۰۴ و روند بازسازی ها
▫️
در مجمع روز گذشته فولاد مبارکه اگر چه سود بیش از ۱۰۰ همتی حاصل شده بود اما سهامداران با اولویت دادن به بازسازی ها تصمیم گرفتند برخلاف رویه سال های اخیر سود کمتری توزیع شود.
▫️
همدلی، همراهی و تشویق های ممتد سهامداران پرشمار در حین ارائه گزارش عملکرد سال گذشته توسط سعید زرندی مدیرعامل گروه فولاد مبارکه از جمله نکات قابل توجه مجمع سالیانه این بنگاه بزرگ اقتصادی و صنعتی کشورمان بود که پشتوانه معنوی خوبی برای مجموعه ای است که سالهاست ستون فولاد را زیر سقف بازار سهام قرار داده است.
#گزارش_ویدیویی
#رضایت_سهامداران
#مجمع_عمومی_عادی_سالیانه
سایت
|
ایتا
|
بله
|
آپارات
|
ویراستی
|</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/454297" target="_blank">📅 23:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454296">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRLUeHEn-DrEDIjI0ccXcfZjGWDgtPSb3LkCmoiy2tY-cfw1hEcGHEd_nDVpajTQ6l0t16NsD6F8-o-E3RsuPOGYtlf-xT9pwtiuFVuDmpffYwzDbr_P41eHycFmdNfApaSHTGjXlqiYnO3G3axNFRF7bSBHGXAkSUckrCWLcBEtSEsXTopjZUDuNuv94PUGWFxV9Ua8Xpt6CXzVjgbYsEUvEUVawhCT-ZdEmkZOhitpbBEVpF5_1a2LleN0UrYiBsFjtJSaR9argatR0F2C4Rc3yjzeZ23FhYQonlvO2S-EtsUBLlzoFIfB34JK1Yt1J4kvEIS1OCdwFSbG3e4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش بلیط اربعین در مستربلیط از ۵۴ هزار مورد گذشت
داده‌های مستربلیط نشان می‌دهد بازار سفرهای اربعین پیش از آغاز موج اصلی اعزام زائران رونق گرفته است؛ به‌طوری که تاکنون ۵۴ هزار و ۲۰۲ بلیط به فروش رسیده و اتوبوس همچنان بیشترین سهم را از سفرهای اربعین به خود اختصاص داده است.
جزئیات خبر</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/454296" target="_blank">📅 23:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987517445f.mp4?token=cMvme8KvRWpev74iLBGsK4rWK-ezuYOXtyCWWC_wbee90ZEyGB1kP4dgWY4X7rDA6EEk2DvtNboti_IrABGORCNFsC_fWpmWVFXcr5ZD9U6QVDdLCJgNsK-1lb1bd91CAvKzSTmUQUjBCFivtMKXH3H826MC8lfDsG7vOJf_XI4RIJnfj4SVn9JcfbpliEXLqt0NBBInB6lxjXnw4AU4tYtj0kS9iR3Om9LO81w6Fz7KAYLAA8C5aIx8r2Wbq1qD1UpyYIj5glRRph6c3KP_-Uv6pw8b9vjxOB7YHR5o9kNWJLK5zQcPS6yofNrGpn7UGKHzqYGisXNs1BUbNkte0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987517445f.mp4?token=cMvme8KvRWpev74iLBGsK4rWK-ezuYOXtyCWWC_wbee90ZEyGB1kP4dgWY4X7rDA6EEk2DvtNboti_IrABGORCNFsC_fWpmWVFXcr5ZD9U6QVDdLCJgNsK-1lb1bd91CAvKzSTmUQUjBCFivtMKXH3H826MC8lfDsG7vOJf_XI4RIJnfj4SVn9JcfbpliEXLqt0NBBInB6lxjXnw4AU4tYtj0kS9iR3Om9LO81w6Fz7KAYLAA8C5aIx8r2Wbq1qD1UpyYIj5glRRph6c3KP_-Uv6pw8b9vjxOB7YHR5o9kNWJLK5zQcPS6yofNrGpn7UGKHzqYGisXNs1BUbNkte0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان مرشایمر: ایران برندۀ جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده؛ او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/454294" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCor690PTxCqfKZBN04H9tPCfEzasAR8vupUzfViOhe7-ekcyLjwLGBwAsBMm-Gf7YWfoq2u3svBJ8ukc1gG7XXhLIMX2jOEkSgXw_QPTkWR0v0_PEH_yXUYhAe8Qi5yejXSMc-kx9NFVzlyCtBTZUcQVabaOglHkt08qapiEqqXGlK-1I5vhJG0G7bcEpdZOylPx2-yS7Tje0dARu-7b6cT1dZJuXrFYPRQtgmoI5-hIPjm0XdVQphC-u0w4eliq3iH2RuYlBCp3pmX8_HKNwPZiYU2UENE7aUiBN99IVN2Ns4f101l63X15I9nHrBmproB66GyRY_WWwPG8UDSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spyt3wofUUJtJiJSZFXoBx4BJjXz0E9EMnAm6g_Ditt_RJstD2upMgqdSiErRU3rp2ZEHfvL3I10lWXLEFteW3If32Dh1VM0PUtiVN3V6iSOpjGK--CvqSvhte9AlTCWaLonXx0KltEta6wXR807YA1InfD6ZIethCPvTVbHA4phy7_7FuVLlnlQ15Afr4aMpjw9nMIF1G4qIHpkK9NIBWwb0D1jUM8PnvguXFnO9ZG7hIPC8dL4SHSShvh4YpTl_SrjCsoSDB9ogNw0E24L19nn2Riztm9Mp-ixYyDnpsByE3seHKOYOwBBpJyJa1pGThd1Jbvt4w_jKeJj0oA_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvI7kgAwbN3wTNfQBqKS5Wlb5UicISaJFx2zMX96pCYwTyCWEwTqGWqyDzCR02pxB7vG5v4iwxdG3T_lGROKJaogYRqaMY2hHq206M_dvD3J4gLZbn5LrwQsR-9mj060SpEe5mvBSlG7igPRfw1ba-aNn3SOpYodIVC4xR9W6Zlg0r_xrvuLf_e0eBDWFJaHtLHBm92D4vQ0Lyg71bTCMKlhevv7QTDVfwxRp7hwEnxqlP-5ARuGPjYaiccOtf4-3S6F2lWk0tJrZMqTotpJY0yK63yf4UITqUbAnBoDUSL6xEOoSUzuLEyYGs-BhjqsxNmmwb3V3xWl6IRtKKNcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmkVDX8YYp26ik8Pe8FvURDTPUKPJudDI7q-ebX94qcPdZ9pquYyzg84-yJFZG4tkSHtCQcEIGfZwvI5k-CBsrA63VzdIm6dtAJZ2J7qb1jRPG0cqCR13HUm0Sp2iEp1JDc9EPw04QNrOeMQT_xLq_X_ZCh-vCIMfjG8uJHgSEG_Ard7R6kl6oAk_-s_zEPK1il-0zav426kVsAR3zJ_TxKTEMT_apHUwjmroTkVNUYo7YMeZV3qfnE3C6SG7H5D-rD3jKmTI6-YwyTQyBBOL4AKXm2zR1hZEOyuCRSyvH8tH-yxZRR3iVcZ7cj_yGbDeR32clrtaT3e_7Q8buGjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsF4D5sxs2m31m9KnBIUP-Is9s06H6Ip6N2fUrSSX7eaaTAGvucZUCvSDSVz7RQLJTzFoTJ98vMYI4Jg39NBZoU_aJVdeDBoVyTG7VkS94lYi-vhOwccoyjNR0s5PPJjbgOL9X9kKOrCpaibyiB0AamP5swYkzRkvQUtB7Cbj_VvSgBlwr9KgG0sQdVq4uQceYSVkFRBPu3rvIzrOjyEoZSz3riGFZei8o8uVtocpe7q-c4QUvq9O6XHNfdc_nGpevc77S3d_nfjMf7TYeMfu6VWc3kiMSyyfJFLaTcVasBhiY237kVJ3TIkbvTlrNa896QXSbAhWqzH9D79w2zfLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اهالی خراسان‌شمالی در موکب خود به زائرین خدمت می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/454289" target="_blank">📅 23:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768146331d.mp4?token=DC_o-X60DuHXq99aBKLmGMuhTN6wB4oap6lDMsB7qbIqsplAJ45_L9Nv-t9VAqvPXTKmfCuJnCMG4Zy4i1KfGqvc5_Q6SBI4VC6EBJBfSz0IIpaiQTKqzzmA6J0ARVaZxkkwkz0OcX1TvavQZpqYo1-TOzoEiCsx8VCyXNsikWL0N0VkbEBlnHW18s4N3y5XAFukVR5wcC10NLt4VCqPT477sOT-mKVD0gCeKBod0eLgI5W7Zxdy5MozhW0x1hxZgdVFJS1TykA1Nm0cnJ9E4sic96E32og49T-RHAOzg4Eo31ADiINNVzue6UbPVseJRohw_lDoUMe3KJhQUj8hnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768146331d.mp4?token=DC_o-X60DuHXq99aBKLmGMuhTN6wB4oap6lDMsB7qbIqsplAJ45_L9Nv-t9VAqvPXTKmfCuJnCMG4Zy4i1KfGqvc5_Q6SBI4VC6EBJBfSz0IIpaiQTKqzzmA6J0ARVaZxkkwkz0OcX1TvavQZpqYo1-TOzoEiCsx8VCyXNsikWL0N0VkbEBlnHW18s4N3y5XAFukVR5wcC10NLt4VCqPT477sOT-mKVD0gCeKBod0eLgI5W7Zxdy5MozhW0x1hxZgdVFJS1TykA1Nm0cnJ9E4sic96E32og49T-RHAOzg4Eo31ADiINNVzue6UbPVseJRohw_lDoUMe3KJhQUj8hnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشق اربعینی گنابادی‌ها در میدان دفاع از میهن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/454288" target="_blank">📅 23:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6233b98d41.mp4?token=V_ewCbjNBVRtUeJdAiTF8n6c3p_n_KPQSpgkwXa7DGvL8ONcP0JJsIRjtzzUxbfQPOhx4rtkUSQTSzbes1sw_eZIy7VCjuRSjmMxhhvRT7BxEa7P8QJ_mhrMwHDYo5MzETpF9VK2LeQ296sF7xlGGRsGxNCVIYfiRlch65w6vri-fudFsQb4KVPl973-Yq7UTI5U-YnkYXnAaOXvZfzcsu5EAp-k2Rd9t8J33i6fvwDPmyX3Azs_gMlPezwH_SgabwWq_xqUStuDYsVDO2ZT8-dA1CVWkbPlPdxQNUeZ1D6CWYbapr7b-R_ij3wVM1ohj6mNV8S8rns-O8dNQuMXFTL-WrFhLbgEDf3uRhEmJogattmHaDZq0NRnclvZWSwDhrMlTfR_JzQ-t6mGucqPACB7RfysTb0mZt9Vtc6EmHnrJke7_xWuJPww0OQbhFJa9Cqqq0TVbfaIt5ivci3UeA6LTtOR-n6ctFp5Bv3iMWwhhmaMCb2euy-o9zsjlNs4NVVUFxmpnfpvKfjFZHZzQhH-0XKHlDxUGHh2nGwEliWMNO1-fhKr1EZXekWuRymOxWDGUx6hoQZ60nmJ3s3ZA24pRKPGOzuHy35GbZimb9fLq3v6r6MiQzm06g7381rz-BO74d6LXarlgAuLlH6L2eYKqIlmTay0Z51lS0JT_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6233b98d41.mp4?token=V_ewCbjNBVRtUeJdAiTF8n6c3p_n_KPQSpgkwXa7DGvL8ONcP0JJsIRjtzzUxbfQPOhx4rtkUSQTSzbes1sw_eZIy7VCjuRSjmMxhhvRT7BxEa7P8QJ_mhrMwHDYo5MzETpF9VK2LeQ296sF7xlGGRsGxNCVIYfiRlch65w6vri-fudFsQb4KVPl973-Yq7UTI5U-YnkYXnAaOXvZfzcsu5EAp-k2Rd9t8J33i6fvwDPmyX3Azs_gMlPezwH_SgabwWq_xqUStuDYsVDO2ZT8-dA1CVWkbPlPdxQNUeZ1D6CWYbapr7b-R_ij3wVM1ohj6mNV8S8rns-O8dNQuMXFTL-WrFhLbgEDf3uRhEmJogattmHaDZq0NRnclvZWSwDhrMlTfR_JzQ-t6mGucqPACB7RfysTb0mZt9Vtc6EmHnrJke7_xWuJPww0OQbhFJa9Cqqq0TVbfaIt5ivci3UeA6LTtOR-n6ctFp5Bv3iMWwhhmaMCb2euy-o9zsjlNs4NVVUFxmpnfpvKfjFZHZzQhH-0XKHlDxUGHh2nGwEliWMNO1-fhKr1EZXekWuRymOxWDGUx6hoQZ60nmJ3s3ZA24pRKPGOzuHy35GbZimb9fLq3v6r6MiQzm06g7381rz-BO74d6LXarlgAuLlH6L2eYKqIlmTay0Z51lS0JT_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع جاماندگان اربعین جزیرۀ هرمز در شب ۱۵۶ ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/454287" target="_blank">📅 23:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27205720f3.mp4?token=jSpeXg_92UDVeGHIIfXeI8I67x8Q7xP1X8gRW68tYvoUytWclqwwW5R8i3tsVnjfzuAn_9FZE83fpRzSz-QX4k9LSQQbcsIxJFA4vkR3uK5h5IRSXRTGTwn52rnPA3M3MJDG3HEsbtwn8zQTA-L5n7TaLKC0sGzSDbbxeDIrO15NRowXmMnID2HJ-nXwSPCqOugUCfsiOyIl4sOJMp6OHaRjytbuQ6TEYZTDwl0vdU3MWO1TYYYYDZTTktzDxVJZ5_2U5ZB3ksb6QjBY_b8ZNETaesPaETvDqHw3Y7l5Ded_8xpivz-Wy9BU0AUk8szuqOxhw2mK2HD5iP39xuFOCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27205720f3.mp4?token=jSpeXg_92UDVeGHIIfXeI8I67x8Q7xP1X8gRW68tYvoUytWclqwwW5R8i3tsVnjfzuAn_9FZE83fpRzSz-QX4k9LSQQbcsIxJFA4vkR3uK5h5IRSXRTGTwn52rnPA3M3MJDG3HEsbtwn8zQTA-L5n7TaLKC0sGzSDbbxeDIrO15NRowXmMnID2HJ-nXwSPCqOugUCfsiOyIl4sOJMp6OHaRjytbuQ6TEYZTDwl0vdU3MWO1TYYYYDZTTktzDxVJZ5_2U5ZB3ksb6QjBY_b8ZNETaesPaETvDqHw3Y7l5Ded_8xpivz-Wy9BU0AUk8szuqOxhw2mK2HD5iP39xuFOCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع حماسی مردم گرگان در شب اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/454286" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950dbc2faf.mp4?token=lAagJPakXjnWFMI8_TuVOn-bRFFZ4bz3CGu-7TVVK8QwUgcc1JF0hgK_KW35ErkpnLbXYPHteUgOoa3RMVQqPIaWgPU3J1BCccLjeX5mV1o2hEnoKjMI7UUwfNnM9sysDq-30pJ0xp3sy7bM1vC3wufKUVx86cDHHbBb3P1kvWQsI4r6mWix9TvM2rcVV_yLxaM8nC-_NUFbCOoJgJKmUp6TZ9Sc0UDiDvdaOYNpIQnrko5_7MweHuWr3pIWy2VbB7o3HJR_6ZLE3--b28rE8CvQv8dcH9iUt5gb2C1ndZM8JZaE20_WpbJ9sXFtbzS5WyjoqX_c71nfp6nYLQtswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950dbc2faf.mp4?token=lAagJPakXjnWFMI8_TuVOn-bRFFZ4bz3CGu-7TVVK8QwUgcc1JF0hgK_KW35ErkpnLbXYPHteUgOoa3RMVQqPIaWgPU3J1BCccLjeX5mV1o2hEnoKjMI7UUwfNnM9sysDq-30pJ0xp3sy7bM1vC3wufKUVx86cDHHbBb3P1kvWQsI4r6mWix9TvM2rcVV_yLxaM8nC-_NUFbCOoJgJKmUp6TZ9Sc0UDiDvdaOYNpIQnrko5_7MweHuWr3pIWy2VbB7o3HJR_6ZLE3--b28rE8CvQv8dcH9iUt5gb2C1ndZM8JZaE20_WpbJ9sXFtbzS5WyjoqX_c71nfp6nYLQtswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی وارد نجف شد  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/454285" target="_blank">📅 22:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec765ed50c.mp4?token=JaQRfo1pLlEZUXyN1FmGrrAoF0XG0DhXrfgH7NbnWNCpeGYKpFExrG68IPiBF0H1XvKiacZJCRx7Gi5CF3yutgf4y9mI8rkyT9LcnklnOl1Wn6B6WQfBhKxYFbsjN-3U219ks2-RgBQRLDyLCdbVE-aKvi8V5YZR6fC3o5VDilE32YlAAovICinzJqkfyjSL4Z-Nrs_XC2IS8Hg22db56VGJJqHc5p5AoeAPt0_YpQPRtx23-yK3N8m5VrfTtqN4buoEQ-V_JH37827V60uAvCqw1O_sor7ezN9mDHF1Y64dOcPFDRuxCAW3zvAdIXtTJMjjK9nba4JBdqk59yDKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec765ed50c.mp4?token=JaQRfo1pLlEZUXyN1FmGrrAoF0XG0DhXrfgH7NbnWNCpeGYKpFExrG68IPiBF0H1XvKiacZJCRx7Gi5CF3yutgf4y9mI8rkyT9LcnklnOl1Wn6B6WQfBhKxYFbsjN-3U219ks2-RgBQRLDyLCdbVE-aKvi8V5YZR6fC3o5VDilE32YlAAovICinzJqkfyjSL4Z-Nrs_XC2IS8Hg22db56VGJJqHc5p5AoeAPt0_YpQPRtx23-yK3N8m5VrfTtqN4buoEQ-V_JH37827V60uAvCqw1O_sor7ezN9mDHF1Y64dOcPFDRuxCAW3zvAdIXtTJMjjK9nba4JBdqk59yDKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: دست‌وپازدن ترامپ ممکن است جرقۀ آغاز جنگ جهانی سوم را بزند
🔹
خلیج فارس و تنگۀ هرمز چاشنی بسیار خطرناکی برای جنگ جهانی سوم است. @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/454284" target="_blank">📅 22:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6307a090.mp4?token=p1xwxrg07STUp_TFz4vJgA7-ypHk2Otpfss8BiKZ5T-dQqX-7EUfnUJWq5gWGpN0fvxnTDsn7dXzhzV88iC9F6dMN00mCZrlT9k_3G0R9B19wssxYFtAw9O-uYvO41aJp3wA_vPXXWNQnwKGgwkHeFaNPerxOW3Ng8clViVpf2py7DpmPvk57LOcPF2eyfobF5aSGsTzzdijdl3LAg9LRgUtBQtQ8yX-qH4MUKBk8pmQ6sgKJJcEX7iZtqUVAT1tVLJDohzcJ65cxAYoSCw3r8j4zF9udBa5jxOygA-LvqFj6C8ERHoq4yHME6jqhQwx5GmcNCjYwf5-3FBxXoCfnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6307a090.mp4?token=p1xwxrg07STUp_TFz4vJgA7-ypHk2Otpfss8BiKZ5T-dQqX-7EUfnUJWq5gWGpN0fvxnTDsn7dXzhzV88iC9F6dMN00mCZrlT9k_3G0R9B19wssxYFtAw9O-uYvO41aJp3wA_vPXXWNQnwKGgwkHeFaNPerxOW3Ng8clViVpf2py7DpmPvk57LOcPF2eyfobF5aSGsTzzdijdl3LAg9LRgUtBQtQ8yX-qH4MUKBk8pmQ6sgKJJcEX7iZtqUVAT1tVLJDohzcJ65cxAYoSCw3r8j4zF9udBa5jxOygA-LvqFj6C8ERHoq4yHME6jqhQwx5GmcNCjYwf5-3FBxXoCfnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/454283" target="_blank">📅 22:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b215ef3f7.mp4?token=chS0uC5WkKdKy6X6hLy_LJsfMdU2w3nuOMwsOQAl592flYHyMRhU4dTo0ge5RwKFJXk-OK7j6KtDeouHkrajtKOuaHB3YdAwpxDdOHji0B4NwzV-BE03AjXZNETONokMgTM_JGKpxllvLaMbT0SK5hbO66lxf0oyUeHjG-DfrSTKd5lIV5Kz_5c4VHZvb9sKsiRajIjPes-NIRV9swxgULohEx28V1r-dk2_F71tQJUMHnalKrLvAqUY_qv5Gj3OFJLVzl093FAAE2EO4gN_vwkkVdifBbBZIsmofXuc_O6rEmolxBsj1x1kZAa7PL8Ito8iYzzbgkl_rASiDHRLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b215ef3f7.mp4?token=chS0uC5WkKdKy6X6hLy_LJsfMdU2w3nuOMwsOQAl592flYHyMRhU4dTo0ge5RwKFJXk-OK7j6KtDeouHkrajtKOuaHB3YdAwpxDdOHji0B4NwzV-BE03AjXZNETONokMgTM_JGKpxllvLaMbT0SK5hbO66lxf0oyUeHjG-DfrSTKd5lIV5Kz_5c4VHZvb9sKsiRajIjPes-NIRV9swxgULohEx28V1r-dk2_F71tQJUMHnalKrLvAqUY_qv5Gj3OFJLVzl093FAAE2EO4gN_vwkkVdifBbBZIsmofXuc_O6rEmolxBsj1x1kZAa7PL8Ito8iYzzbgkl_rASiDHRLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: بعد از این‌که آمریکا حملات را متوقف کرد ۲ روز دیگر به حملات خودمان ادامه دادیم تا حساب کار دستشان بیاید  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454282" target="_blank">📅 22:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e260f8ebc.mp4?token=Bvxo8mNPdbJWu3W11no_vZYPcIr5BE0L2zCkXA-y5igzJl6CY9g_igRqGkWLveuhoDNljnAHtlOQKdzTkxkoUcM_0O7lvdltAnNjOK-La06vPTTixphfENJseIFAm-aiTfZwLvQK5OIwCVlm2OleyLUGbL9tW80ubV00I5czIVpTxBU3Ay3aNL3qn2rJCmdN55bq80OYCI-8dkCZBOFAX77XQPo__iBU91EdJxZvIX35NEPwZyJxKF5WdsTalkPp5hvftJqpSokLFHYKde_ivzj4wY40GydH2X6jTPuWbSjs3v7X691PxMfzulS2iLi5W4fqKHMIuOe6jz7J-KbOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e260f8ebc.mp4?token=Bvxo8mNPdbJWu3W11no_vZYPcIr5BE0L2zCkXA-y5igzJl6CY9g_igRqGkWLveuhoDNljnAHtlOQKdzTkxkoUcM_0O7lvdltAnNjOK-La06vPTTixphfENJseIFAm-aiTfZwLvQK5OIwCVlm2OleyLUGbL9tW80ubV00I5czIVpTxBU3Ay3aNL3qn2rJCmdN55bq80OYCI-8dkCZBOFAX77XQPo__iBU91EdJxZvIX35NEPwZyJxKF5WdsTalkPp5hvftJqpSokLFHYKde_ivzj4wY40GydH2X6jTPuWbSjs3v7X691PxMfzulS2iLi5W4fqKHMIuOe6jz7J-KbOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: با حملات ایران فرماندهی سنتکام در خاورمیانه ابتدا از قطر به اردن رفت و بعد از حملات دقیق ما به اردن، به سرزمین‌های اشغالی منتقل شد
🔹
حملات ما کاری کرد که مواضع آمریکا در کویت به خرابه تبدیل شد و در اربیل بسیاری از نیروهای آمریکایی تخلیه شدند.…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454281" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c317899793.mp4?token=mEUYqE5Ha8A2Xv6WGiFPqy9spvMswRMXCO38yaN2W3em0IGE9h_eCITdKy1fRRqYLcJAEUTeUbhTcKN_6edlCeGgmAdCPTB5dAzLO45c-webrlyWYdujwuZHJF8cbJd6HEG_NvlERi_me6w45UqZs0HCWgtqX1MipZ9SekbwVFRsArHfEEW0PqlqUyABCuk1qtM0u3CJMzT6j6WNxAKGUCkGgpLAI4r2eAg9upWFCHtCOoN0MMCkm5JptdRdOyork-3eiL3lm-bCy05TTH3zP46yGwKdxQsjMosCNdxwOeJ5fy5OvMagVtD2VnwAJyjyZaO1hrbzL22Irrxa1CAoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c317899793.mp4?token=mEUYqE5Ha8A2Xv6WGiFPqy9spvMswRMXCO38yaN2W3em0IGE9h_eCITdKy1fRRqYLcJAEUTeUbhTcKN_6edlCeGgmAdCPTB5dAzLO45c-webrlyWYdujwuZHJF8cbJd6HEG_NvlERi_me6w45UqZs0HCWgtqX1MipZ9SekbwVFRsArHfEEW0PqlqUyABCuk1qtM0u3CJMzT6j6WNxAKGUCkGgpLAI4r2eAg9upWFCHtCOoN0MMCkm5JptdRdOyork-3eiL3lm-bCy05TTH3zP46yGwKdxQsjMosCNdxwOeJ5fy5OvMagVtD2VnwAJyjyZaO1hrbzL22Irrxa1CAoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: با حملات ایران فرماندهی سنتکام در خاورمیانه ابتدا از قطر به اردن رفت و بعد از حملات دقیق ما به اردن، به سرزمین‌های اشغالی منتقل شد
🔹
حملات ما کاری کرد که مواضع آمریکا در کویت به خرابه تبدیل شد و در اربیل بسیاری از نیروهای آمریکایی تخلیه شدند.…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/454280" target="_blank">📅 22:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88dd872897.mp4?token=eWSiX_zz3FV9oHsGtG99syD4Vqs1H0rHTf-3ZNWOpuvezYmD9ia9WXFkdL3rL9oI4jZPYo86S7_sPuPwlJBDC2aSHGF4tLfVOfJEqY9OnjRyvl--ng6GIkGXSIfU5d57TjZ1C9bR2-JcIhfLXRLAO9AyA93-Tuy_wN6oVF_Tqal7xt5FHGPpp_UuJnZ1DRvVPGOl3EQLE_aqlWY-ECcO5_zdMJIjZisaEkGTBxAnXt-th34Uc8e-C65-j90Phg37w0W0k1_tAaoKgagmOW8PH8uJd_jDEaveg4iqS4GKHnV3kZrTQNLr1LQrsDyZ9MHO_QTgrIHdWW9jvfB1A9NIvWKxcT5T9mD5DZjzeg1x_R7XF0H0kCjnlbnbmrcvqZ7gUn5M__zaaNzBDJge-vFaXGcofHUY-eK44Bc9i0JF4MT1Y0ogUasa4ALfzygTo6nR5NcaTMf0oYyk-tHbT2Gn5I0FW4Oa91nAhTFonh5kv8x9flkKPWg4KrDjjVPUXCZa921n4heWT5btNM3m1S2e3qpINnD4yfiVGfWWDzDc7U5pULk8phL9B5s5XFrq3IwcXQyy7PD3fp03WjJRBRBsPapHMEUtNLwvA9eT4eh4jLufkp0KGoeADcrHymvBhtSRP9p94TQXystNk1rme65lCQD7u4EItG0W0L6OYi3M69o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88dd872897.mp4?token=eWSiX_zz3FV9oHsGtG99syD4Vqs1H0rHTf-3ZNWOpuvezYmD9ia9WXFkdL3rL9oI4jZPYo86S7_sPuPwlJBDC2aSHGF4tLfVOfJEqY9OnjRyvl--ng6GIkGXSIfU5d57TjZ1C9bR2-JcIhfLXRLAO9AyA93-Tuy_wN6oVF_Tqal7xt5FHGPpp_UuJnZ1DRvVPGOl3EQLE_aqlWY-ECcO5_zdMJIjZisaEkGTBxAnXt-th34Uc8e-C65-j90Phg37w0W0k1_tAaoKgagmOW8PH8uJd_jDEaveg4iqS4GKHnV3kZrTQNLr1LQrsDyZ9MHO_QTgrIHdWW9jvfB1A9NIvWKxcT5T9mD5DZjzeg1x_R7XF0H0kCjnlbnbmrcvqZ7gUn5M__zaaNzBDJge-vFaXGcofHUY-eK44Bc9i0JF4MT1Y0ogUasa4ALfzygTo6nR5NcaTMf0oYyk-tHbT2Gn5I0FW4Oa91nAhTFonh5kv8x9flkKPWg4KrDjjVPUXCZa921n4heWT5btNM3m1S2e3qpINnD4yfiVGfWWDzDc7U5pULk8phL9B5s5XFrq3IwcXQyy7PD3fp03WjJRBRBsPapHMEUtNLwvA9eT4eh4jLufkp0KGoeADcrHymvBhtSRP9p94TQXystNk1rme65lCQD7u4EItG0W0L6OYi3M69o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آماده بودیم به ۳ منطقه از اوکراین حمله کنیم اما بعد از اینکه گفتند اشتباهی حمله کردیم، پاسخ را متوقف کردیم تا ادعای آن‌ها را بررسی کنیم
🔹
آن‌ها  در هر صورت باید مابه‌ازای حمله‌شان را بپردازند.  @Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/454279" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039faea8ea.mp4?token=QHeNhL0hj80vUNUrOZ2z1VRY1TL9P1--JVP9NQOE6_dZsJttSzrsWJCXiEuLTKD2M3-51A_VraPoWxfyIle4WWj0MhznmAGQ1WVBf4OY2VcID0dt4T10CbJ7vT8OGtTMcy__g2SUuzuYLKt-MLG66QQI3mFMWSdVXtkpoOBBryFwJ7Ts1ks5PtFccQB4gWiSNXut0SH0JqNy95yBK1wK0-e7q3g8AVYUnZ0F-WU6qhewXwqOjRf8xwkDdSG7SzrHi7ktlJ_RoCT_oS-uBk60x6T3mB675X9Tvuq_4Mh0TxhsAkm3cQXr2l1gHqC_RsfOMpFuP6S-7aynh3qyO-17Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039faea8ea.mp4?token=QHeNhL0hj80vUNUrOZ2z1VRY1TL9P1--JVP9NQOE6_dZsJttSzrsWJCXiEuLTKD2M3-51A_VraPoWxfyIle4WWj0MhznmAGQ1WVBf4OY2VcID0dt4T10CbJ7vT8OGtTMcy__g2SUuzuYLKt-MLG66QQI3mFMWSdVXtkpoOBBryFwJ7Ts1ks5PtFccQB4gWiSNXut0SH0JqNy95yBK1wK0-e7q3g8AVYUnZ0F-WU6qhewXwqOjRf8xwkDdSG7SzrHi7ktlJ_RoCT_oS-uBk60x6T3mB675X9Tvuq_4Mh0TxhsAkm3cQXr2l1gHqC_RsfOMpFuP6S-7aynh3qyO-17Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا پل‌های منتهی به هرمزگان را زد تا یک اقدام زمینی علیه ما انجام دهد
🔹
طرح ناپختۀ فرمانده‌های ارتش آمریکا باعث شد حملۀ زمینی و هوایی متوقف شود. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454278" target="_blank">📅 22:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c98a052b1.mp4?token=FK5hzKvl_42jK7DGz2E_ZBo7ZPcz0X01KZxM9DeAt0gGFpEbKkLvoHRAALbaZrojYjTH6pwwIV4PTmol8w7KdxLAt0SkjxI6OMkmwg6YmBrv10yjwNlZUciniAALg8PCP6D6QflvQ5K_EwDKuXdDn-k47o0tDwYj_ms-F9BhLhACcM8bFo34C5SYGU-RkxL9SUndyGjr-WZvNHLOfZvCRlqAKYRGQD6gzV-hlguQg-opeGhzz1wo07nRkKT7Og619epCpz4IvlsKYzbls61F1od9CRnuT4tzg_W2IBlWtCoRWrnHz8S7AiIQueuUCPRqm1vEGd-ogcPUC94ofuLnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c98a052b1.mp4?token=FK5hzKvl_42jK7DGz2E_ZBo7ZPcz0X01KZxM9DeAt0gGFpEbKkLvoHRAALbaZrojYjTH6pwwIV4PTmol8w7KdxLAt0SkjxI6OMkmwg6YmBrv10yjwNlZUciniAALg8PCP6D6QflvQ5K_EwDKuXdDn-k47o0tDwYj_ms-F9BhLhACcM8bFo34C5SYGU-RkxL9SUndyGjr-WZvNHLOfZvCRlqAKYRGQD6gzV-hlguQg-opeGhzz1wo07nRkKT7Og619epCpz4IvlsKYzbls61F1od9CRnuT4tzg_W2IBlWtCoRWrnHz8S7AiIQueuUCPRqm1vEGd-ogcPUC94ofuLnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا پل‌های منتهی به هرمزگان را زد تا یک اقدام زمینی علیه ما انجام دهد
🔹
طرح ناپختۀ فرمانده‌های ارتش آمریکا باعث شد حملۀ زمینی و هوایی متوقف شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454277" target="_blank">📅 22:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a5e6e348.mp4?token=gL-9wcyqSQQdvkAAjJptLRgOr5jj-zGEkBI-bK_zaoxzczOZgm9LcLF3OYtF5qZKts4ouEOgd79B6EICJFn1B16b6PV07_PSbGFzPS-TUoWPvx9Z0l_6VUYSHGTFvexbdKWGA5D9A7tpdCgUe-o8gVFOL7OcPQGVP15VSMJW28XaQRPCgE8L9jRA408RVhOhYygZ-Ox0LfJktF89Ir-Rr36CovKEoED1H-j2JXgvaW5mIA1vUMIxp2eVTQhjzPKinNy3DKu95duqCREnPnhu-sS_qgIFYI6I15PhodOo12Cx3b06fyKr8O_cV25yacEq24n88vvvCxyn46op119c7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a5e6e348.mp4?token=gL-9wcyqSQQdvkAAjJptLRgOr5jj-zGEkBI-bK_zaoxzczOZgm9LcLF3OYtF5qZKts4ouEOgd79B6EICJFn1B16b6PV07_PSbGFzPS-TUoWPvx9Z0l_6VUYSHGTFvexbdKWGA5D9A7tpdCgUe-o8gVFOL7OcPQGVP15VSMJW28XaQRPCgE8L9jRA408RVhOhYygZ-Ox0LfJktF89Ir-Rr36CovKEoED1H-j2JXgvaW5mIA1vUMIxp2eVTQhjzPKinNy3DKu95duqCREnPnhu-sS_qgIFYI6I15PhodOo12Cx3b06fyKr8O_cV25yacEq24n88vvvCxyn46op119c7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگهٔ هرمز در کنترل آمریکاست</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454276" target="_blank">📅 22:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bac9fbb15.mp4?token=Nq992CdRndTXDDB3Q9pDvSZrKrzj-NCSQk6Hy4llqbL_A5uwuG6Dev1Ccw_FOboevqhvh6BKDnrYsyf2XpyhyMLQLiNfAek9IbtitGUXUyKtFUP06wfszum7pIpXJuR7J9b0x9myiR9eaK6VFOW446WC_VgDY6yOfMf2fZd9S-8QtbM2oUI325WDya6xnoQmkwTiomBJCJCfg0_aJ8XvBWIgT3-ykcfSYzAbrM-ZMR2UExIdVXktvXb01t7zr732usJQJUjV-7my1RCmNfClxjmjJoLuyw1bQnSo--rRYaHvHlPIjCwYxmYks9TfzRgeoZ121yH83p0UiXgkSHY5gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bac9fbb15.mp4?token=Nq992CdRndTXDDB3Q9pDvSZrKrzj-NCSQk6Hy4llqbL_A5uwuG6Dev1Ccw_FOboevqhvh6BKDnrYsyf2XpyhyMLQLiNfAek9IbtitGUXUyKtFUP06wfszum7pIpXJuR7J9b0x9myiR9eaK6VFOW446WC_VgDY6yOfMf2fZd9S-8QtbM2oUI325WDya6xnoQmkwTiomBJCJCfg0_aJ8XvBWIgT3-ykcfSYzAbrM-ZMR2UExIdVXktvXb01t7zr732usJQJUjV-7my1RCmNfClxjmjJoLuyw1bQnSo--rRYaHvHlPIjCwYxmYks9TfzRgeoZ121yH83p0UiXgkSHY5gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌بازی بغض‌آلود عراقی‌ها از روز تشییع امام شهید در کشورشان
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454275" target="_blank">📅 21:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIwNFIOaK0KqDhtbyCqcHBNnY0UHMX4W1h91K2QFXljyOVWGXbsoUjaGEeAbD00cxahU5oczWhKIpXn-IBI_Nq003WXY6fnza7zZW4rF5tuydVwmQ6tj2doz9-cb94kjs2fN1DbTpIB1z822PSudcPtYTt9iUDnxHZsIWL4O9fTzrPKJ73n6vGe7UGG_aXiwIu7ODBTKYw0QjUvTLNwx9RuygubGprh_xjrb8dvb2hnJzp9Vf_p8PYjinAIU8azzRT9iXdICgb443ZZb2QLJ4LwAipsH9IwGT5FTvqN67MHmfZFaFt5xCRguBxpw1lv1D0gwn1aDcq3LQfQhRkWN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5KfGUVanxEGPss-YYg8cB_OTARHj64rCekFeAQoFpxHex82OJD9iLq-cpsY7hreC_j_xsMRps9gjZHBkE7SlzQXP6WV4_DakwjZiQexRLQK0VYD7Pd7_8Z7uIj5kzn6XGhLZE8L7FmnumMGBx6OLkMXRnRFS4dxgmXDYjs0FzWaJCbabqQvAgrJOcYRLCzPltXsmN95Iudsb5MVvtwBdJdIpzHo_8AZy8fj22lLYmxvV-0lqxYbkWcChAs4KS2_pagKbJo28rs5pV6atvRf2mXh2ydLy5x-QF9LQo0GhoKevFiakWXwudak3tO9CE07SZIQtDFEV7_hAAyr2FFKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAEjlUFAh9XGX0BgtrtVYTuNJpg3ZLUBpd8UpZa31mu1xEg4LwnqcJQCFSOzOHPkwBt6BkyJos5SjZOGtAMX-sCVXIBm12uN_zVscoo080BKiyBxOyovvqurAeTygOWCID95VKIAMr6Om-DsOganfMMxywivbCWyZiLSwB9snJKvFYEKSx1BCqKTTXO35CGeafYR9VmE2-r9N2v1Dgis2VRW5WFVJ0FOtS1WKaueHdWTVNjUcG_Z1gan2cqRTJdbiUUyJB78ceUygnRWO9XuIxqcnkv-wMW9Qq1U1RRXA2pYIx0kazcFD9cmr2T8GiXbKT2YCTkl2NXRJIvVdQrc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0L24nstr2fXXi_XO1R_QIyiKXJU8VZc9HstVgrtyEZkPxmuuRpqDOm1FW5EEzARfLq9I4cXx5W64QbOZpoE7-zpmE0ly-cy7oE8wJ0OhqIaXaqmV8bcj8cv-qAw3CQ30qSXd9pnQ0sSd3FO82T0JmivS6leN0lBO0Ve9V69S0SRRtjXMNADd79NU6xlGwle64k2hf8uBvgwnntPt649uGJFToXcTsoxcsbZZIiqonPXwlbc7Yq0JMZJWZvw8ioo53aeDJZk1z7-Ue9mfUUSs1MCJBqocfF9LrGDiQS5nsnxIjUnSfYKPUEw2MpU4UzpCO7fBczmNQb1CKo2G57aOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsC154MMlx3Qj7sdjFMt6K68bKliZsAe6FDMyW8399ex5xXfgWgKFZ92w4zjPjtBeYxqeT-qrQmSPgOKX6f5W8BFPme9-FfDNmygPVsom2RU-o7sH8fLzCyP2h0phF1FDCqgiQyLuagb4tPGhQu33pS9cfilw_Qe7FESuz3-CvhGc7zYZ13MKNZCjFMT1wclgjGal9IKSXVTjacrTSMvmrPoUkv3C3NUARUXNvYx0WCtZebOWoYTg0xSvXPK2IdpycrPduojhQCKWtW1jH-NvSc5ZRnSGb4lAPaa0UnvoBY4-eC_x-LBpzdDFjiOF8RxmebkJXvxuDsXAA56lYwRng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران اربعین در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454270" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPAmvO3jMkDipn2z_JY-QXQmnjx5BUWUKUX8h8lkOrIs0m_A1zM3wfkOdfJ8nTxgSlrH6x17YHtEqXb6E1siYccAoAeiWJkwOBw25TvSqFVeXNTE3It0SoZjuqLcy7LW8W6ffDJPBLMulKsPENas5VWqnhzKsbjhg3BqFuZS9NrS8S5D-7FqqPex5bbXKZt6Jz2PTbr2pnQveTiS4ffc6I6OJNJIeH8ZGkcQCPG_Xy_lsHVNHpZUoSxXj4ajlSySOkMKpJIlScKkSKrF1uKdMI2H2iFJHiy3C0_Z7skWeI2eUyGOyYtnSE-eaxf1-z3STQIgi8_bLUDvv9_iN9ry_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
واکنش ایرانسل به ابهام درباره مصرف اینترنت: دقیقاً به اندازه مصرف ترافیک بین‌الملل از حجم بسته کسر می‌شود
1️⃣
بر اساس مصوبه‌ رگولاتوری، هنگام استفاده از ترافیک بین‌الملل، به ازای مصرف یک گیگابایت، دقیقاً یک گیگابایت از بسته اینترنت کسر می‌شود.
2️⃣
ترافیک داخلی با ۶۳درصد تخفیف محاسبه می‌شود؛ به‌طوری که با یک بسته یک گیگابایتی می‌توان حدود ۲.۷ گیگابایت محتوای داخلی مشاهده کرد.
3️⃣
ترافیک پیام‌رسان‌های داخلی با ۷۵.۲درصد تخفیف محاسبه می‌شوند و با بسته یک گیگابایتی، استفاده از حدود ۴.۰۳ گیگابایت ترافیک امکان‌پذیر است.
👈
جزئیات بیشتر و متن کامل اطلاعیه
@irancellnews1</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/454269" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
گزارش ویدئویی از مراسم امضای تفاهم نامه همکاری بیمه دی و گروه اسنپ
#کانال
اطلاع رسانی شرکت بیمه‌دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/454268" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/454267" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06725d913.mp4?token=RvVSIrcFTo4tMb1E-dOlDHwC3QWYoSfwbEogD4IMWh1f31FnYXk7BO0MxqeqxExloUxGe4O76C7UBPJXC390qqv3RPayrjW9jCX3uY2CZYd0QUYZsKtx_3oK0SamHPzJX0rw2zGAnCXq9W_kkzIbDiXCkcWTlAHO_C2VBUeJqto7bVBM9zaupug1_XGrzuxa8MJBJbIsGv3-mqTJKIGRH4y3Zj1al7JnpRuqgyLZuIexeC4eIu5R2ET7iYVx7b6-hqRnNypd1I7A_zt_aa6ZVxzyGF1-C36QE6F-vAOEupJimHyHBWWjOG3UW1kcMX3INs3HFpRpRfsSt4nB5Kmk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06725d913.mp4?token=RvVSIrcFTo4tMb1E-dOlDHwC3QWYoSfwbEogD4IMWh1f31FnYXk7BO0MxqeqxExloUxGe4O76C7UBPJXC390qqv3RPayrjW9jCX3uY2CZYd0QUYZsKtx_3oK0SamHPzJX0rw2zGAnCXq9W_kkzIbDiXCkcWTlAHO_C2VBUeJqto7bVBM9zaupug1_XGrzuxa8MJBJbIsGv3-mqTJKIGRH4y3Zj1al7JnpRuqgyLZuIexeC4eIu5R2ET7iYVx7b6-hqRnNypd1I7A_zt_aa6ZVxzyGF1-C36QE6F-vAOEupJimHyHBWWjOG3UW1kcMX3INs3HFpRpRfsSt4nB5Kmk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اجازه نمی‌دهم ایرانی‌ها در تنگهٔ هرمز عوارض بگیرند؛ اگر قرار باشد کسی عوارض بگیرد، آن آمریکا خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/454266" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fc616a97.mp4?token=DbjBKqZ6-JOuqZFGyrWKAB7NtFg3F_-hWrhwV8kl-wu-EbuXQpMY1MEN5xdVnzsvSD7LgQi3TuAHYs6-gUeNUM6z6zBABGQ2IP9WGn0GkbHLl_Ua1_c2XfTk8T5ibtnqsdypJjiKt34GaCsxt-yejp4LUdSXTuXCicJJuHMDOhdP8ctRgnUIcIdtVyZ75_kQrsBob3aDe3lWlSB87T7twQTTXkZXWBULrIffvzd8rNXfifxHEIqQyG5QnxzO9xxfOjZ7lB-FPyUKJjraQOUR9mxWfNCWbNEU1jjSf2sXlewMP4Ix8PfIl2GVs5JKYF1ZSjDGDZehwHZThuV5xuCOrUdvmHpI59ZQxmgOFoYeI4oncfiw6mNkQjp-RFldVVt3UoQevs1eTWkwlemSaHKACNRL8qjMK_Uuub3mkCow8AMQINuZG7vifbPyy1rbH7tHb_dODnDkAyJAMXhXyzWJrhy6fcEDMUB_MUfccq3xLlt0awDsvfwV8q3YEK29ndZ55MnQ2voZe2MRlfLvLrt7mWOzhHVvJKnW4cflsUinVYUJ3zY2ZEuALDvI3RJRj9gqRr9zNcA6NgbOlp0iyeWcDdFOR5IylF0sA7OqGE5zy52EGgI_Bfl9HiIOoXFPERs-BdT1pidPq6M8ZJ4e0HcCTCE9IhZNZbM1iixa1GyhNwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fc616a97.mp4?token=DbjBKqZ6-JOuqZFGyrWKAB7NtFg3F_-hWrhwV8kl-wu-EbuXQpMY1MEN5xdVnzsvSD7LgQi3TuAHYs6-gUeNUM6z6zBABGQ2IP9WGn0GkbHLl_Ua1_c2XfTk8T5ibtnqsdypJjiKt34GaCsxt-yejp4LUdSXTuXCicJJuHMDOhdP8ctRgnUIcIdtVyZ75_kQrsBob3aDe3lWlSB87T7twQTTXkZXWBULrIffvzd8rNXfifxHEIqQyG5QnxzO9xxfOjZ7lB-FPyUKJjraQOUR9mxWfNCWbNEU1jjSf2sXlewMP4Ix8PfIl2GVs5JKYF1ZSjDGDZehwHZThuV5xuCOrUdvmHpI59ZQxmgOFoYeI4oncfiw6mNkQjp-RFldVVt3UoQevs1eTWkwlemSaHKACNRL8qjMK_Uuub3mkCow8AMQINuZG7vifbPyy1rbH7tHb_dODnDkAyJAMXhXyzWJrhy6fcEDMUB_MUfccq3xLlt0awDsvfwV8q3YEK29ndZ55MnQ2voZe2MRlfLvLrt7mWOzhHVvJKnW4cflsUinVYUJ3zY2ZEuALDvI3RJRj9gqRr9zNcA6NgbOlp0iyeWcDdFOR5IylF0sA7OqGE5zy52EGgI_Bfl9HiIOoXFPERs-BdT1pidPq6M8ZJ4e0HcCTCE9IhZNZbM1iixa1GyhNwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات برگزاری پیاده‌روی جاماندگان اربعین در تهران
🔹
معاون فرهنگی سپاه تهران: پیاده‌روی جاماندگان اربعین امسال ساعت ۶ صبح روز اربعین از میدان آئینی امام حسین(ع) آغاز شده و تا حرم حضرت عبدالعظیم حسنی(ع) ادامه خواهد یافت.
🔹
«اجتماع بزرگ خون‌خواهی رهبر شهید»…</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/454265" target="_blank">📅 21:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b00c95db.mp4?token=KQxw9_2I_QQW0wynyAlH46IaT-7HOWADIB56_jC_jeG_vu7xQrdd6wnH1ldXA9dEdaVSGaaXxNaiP0rnp6zRaCDg7Zyf402N9jnBUPpvIvYnkBo9gupYc32pfxKoZVXuknVHRGZyr3E0orWqlcZfV-OwZrUt0BH8iz7pc6cEsQB7jHSsqOMBYywxLZ1m8r0NZ1U7mqMyUYR7c1FTsNvQcaFX6t6xbm1tcbER1oVW9-I3Lhup4n3yV_dk5XJi7_4_UefcKNchoxexoWH08TBt23aD34vHHwDVuAoAmeSxsQdoupS3g-zlIkno_Q9AckWB4244s1Hyr6jFQPAK1iXwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b00c95db.mp4?token=KQxw9_2I_QQW0wynyAlH46IaT-7HOWADIB56_jC_jeG_vu7xQrdd6wnH1ldXA9dEdaVSGaaXxNaiP0rnp6zRaCDg7Zyf402N9jnBUPpvIvYnkBo9gupYc32pfxKoZVXuknVHRGZyr3E0orWqlcZfV-OwZrUt0BH8iz7pc6cEsQB7jHSsqOMBYywxLZ1m8r0NZ1U7mqMyUYR7c1FTsNvQcaFX6t6xbm1tcbER1oVW9-I3Lhup4n3yV_dk5XJi7_4_UefcKNchoxexoWH08TBt23aD34vHHwDVuAoAmeSxsQdoupS3g-zlIkno_Q9AckWB4244s1Hyr6jFQPAK1iXwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک اربعین دلتنگیم رفته به سوی کربلا، چون بر مشامم می‌رسد هر لحظه بوی کربلا
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/454264" target="_blank">📅 21:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cacd7384.mp4?token=VGjitkeo4Wz_glJLoalcoVUCQnguhpUcqJbhEY3hsfSQqOcWm-9FhO27yYg_7InK6MLkYpitH37mEUCnafAdK1EzqDgqomvqquZyVmHCjrxbtXA__BJ-bPLtcPa59lyatYYkrOe5lM6yr1dm3U6HyE_DjuVewrCv0GVomY_aeqfsKI9tXJTIrGHoNLf_17r8a4Pa6OBttw2Nd-SZaFW6SqfLUeE6be8uCwLKbWFFB-iGSQSthd3pHC4UNARNmjaVK9fhAimbz3_HI112z1Rtdl8XY1EzA823H97Q0BHpWCQkyFkfvcZ5AW62lDJH6kG188jIyh-vtvqxis2BGLQCog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cacd7384.mp4?token=VGjitkeo4Wz_glJLoalcoVUCQnguhpUcqJbhEY3hsfSQqOcWm-9FhO27yYg_7InK6MLkYpitH37mEUCnafAdK1EzqDgqomvqquZyVmHCjrxbtXA__BJ-bPLtcPa59lyatYYkrOe5lM6yr1dm3U6HyE_DjuVewrCv0GVomY_aeqfsKI9tXJTIrGHoNLf_17r8a4Pa6OBttw2Nd-SZaFW6SqfLUeE6be8uCwLKbWFFB-iGSQSthd3pHC4UNARNmjaVK9fhAimbz3_HI112z1Rtdl8XY1EzA823H97Q0BHpWCQkyFkfvcZ5AW62lDJH6kG188jIyh-vtvqxis2BGLQCog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌شه به‌ نیابت از پدر شهیدم چند قدم بردارید؟
پاسخ متفاوت عراقی‌ها به در خواست زائر ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/454263" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926ecfcfe1.mp4?token=cDZLg0gvyD8GZDLTvYqP6CNvBBcUoF2DzKbiVA6_rw45Bq6XD9L3nbnKjMoPZibR4CveUyUvP7B-IJPOR0OFrryAfYQQ3rRoCtc_FWgljTW2tf2gpH1AlqrDcW56KqNDd_iGJKLDTy_WYijZ-1kHmpXn_7csRTEK4arl9Qo14gQazkPC5JiAJDUQJDfU7vZWIvXcDkd4uq3qESqgNdibBIgS_fPzGNspGtB6eKbYDXXBURm1hqLp40v1cDCdzihU9586kw7QuyqvH9atknYJqkl21NWpm6Em6mMxzz8Tqm4XayZMqmRqtRO9SDatRdRaBAlC2E9rA8MNKN3wNiYkm5s_psLXfJIxNFqjlXN2Gkmi8nDtHMkJztV7BHPJPM4be_nLKmtq_l9Z432RewND19LF3XA9vHzE3p4_AcYq9x2M4ja-cj1zbq6DwnkdDDM_AUayBGcap80oEZsduFsqyLcxStiGg-EQZeSh1L-fBG1ucx00YtX-7hQMaZzq-WOFW3h5f91--es5TytmrVVMFlSuOGKfG_bR00i67p8k0Wdf2_K68x4hHRZkqPCDda8HyaPB-NctJt_zIhQwk-VZSehByULXKkZuq3V_ZtY01f4VFPk8b2wKxs76GtvS827iL-VeBmZ7Y44Oz-he9iKLf8SiL7zKcJoN6BunBPCrwuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926ecfcfe1.mp4?token=cDZLg0gvyD8GZDLTvYqP6CNvBBcUoF2DzKbiVA6_rw45Bq6XD9L3nbnKjMoPZibR4CveUyUvP7B-IJPOR0OFrryAfYQQ3rRoCtc_FWgljTW2tf2gpH1AlqrDcW56KqNDd_iGJKLDTy_WYijZ-1kHmpXn_7csRTEK4arl9Qo14gQazkPC5JiAJDUQJDfU7vZWIvXcDkd4uq3qESqgNdibBIgS_fPzGNspGtB6eKbYDXXBURm1hqLp40v1cDCdzihU9586kw7QuyqvH9atknYJqkl21NWpm6Em6mMxzz8Tqm4XayZMqmRqtRO9SDatRdRaBAlC2E9rA8MNKN3wNiYkm5s_psLXfJIxNFqjlXN2Gkmi8nDtHMkJztV7BHPJPM4be_nLKmtq_l9Z432RewND19LF3XA9vHzE3p4_AcYq9x2M4ja-cj1zbq6DwnkdDDM_AUayBGcap80oEZsduFsqyLcxStiGg-EQZeSh1L-fBG1ucx00YtX-7hQMaZzq-WOFW3h5f91--es5TytmrVVMFlSuOGKfG_bR00i67p8k0Wdf2_K68x4hHRZkqPCDda8HyaPB-NctJt_zIhQwk-VZSehByULXKkZuq3V_ZtY01f4VFPk8b2wKxs76GtvS827iL-VeBmZ7Y44Oz-he9iKLf8SiL7zKcJoN6BunBPCrwuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این عمود در مسیر پیاده‌روی اربعین حال‌وهوای متفاوتی دارد
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/454262" target="_blank">📅 21:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce25d15ea.mp4?token=mQ3dg4UGiOqg7bVHtnzkTNEbWcB4n4rtS4p10E_7Jvvrt0sxZ1AeAjW4IetYSzdXx6MCxkQFnusCTl14Zd2BG0yC8F9gj3soZrv0EPHtZMk2iQTWIb8QAbGbSqgLZMiSnWw7BgkhHYSOySNlRE8T0-Og1F3DU2os5qKaI4-ijhGoZDQCALRorEl-e4ewqMD14whLb_pwB0IZXRGTSz--S4I3gqRKsN9HwrRfscQI4CDsnd9IWD9Dk3VmD-DtBCh2um0oBc4HY3jWAF7TItcmmnUJq3qfBHwOFNfr6hNWjOVQUvYVhDmVFFCbcbVgm4WFG0sywDICZsOiTuZkWUt38Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce25d15ea.mp4?token=mQ3dg4UGiOqg7bVHtnzkTNEbWcB4n4rtS4p10E_7Jvvrt0sxZ1AeAjW4IetYSzdXx6MCxkQFnusCTl14Zd2BG0yC8F9gj3soZrv0EPHtZMk2iQTWIb8QAbGbSqgLZMiSnWw7BgkhHYSOySNlRE8T0-Og1F3DU2os5qKaI4-ijhGoZDQCALRorEl-e4ewqMD14whLb_pwB0IZXRGTSz--S4I3gqRKsN9HwrRfscQI4CDsnd9IWD9Dk3VmD-DtBCh2um0oBc4HY3jWAF7TItcmmnUJq3qfBHwOFNfr6hNWjOVQUvYVhDmVFFCbcbVgm4WFG0sywDICZsOiTuZkWUt38Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسرائیل‌هیوم: تسلیم‌نشدن ایرانی‌ها ترامپ را آشفته کرده
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/454261" target="_blank">📅 20:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c316fa21b.mp4?token=jOjPZyuKohQeFFFgA2jJjDY-sQggjJhg3X8LEd-yChQauFzZ5pBoYyNuyK8P_uKdQRLQ5vWJaDGOCwUjMxDQ19JXRwUJoK0Em-IWCYROpGa6TxFstoaBf2yDI2rIQnK8QygW5ACWeTQhNady3-wOpIoGrnzqt1JJlorfbgIsis6U2w5ZqRUAa3bnYIXeswhqGfxpnJQyMROxbIjVA-FWyfJQ5AzhfxLl6Ty1_oelu-2OPlzO8ZC59AahPIhJBi6eC3ijgVoRgb8Q_flGK4KTl1FRoBNH7hPhG0LPE4MSu4v5b3BtkV3IVf0l3YxZvHzRPyqxFBnUOzwcSMWn_fkqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c316fa21b.mp4?token=jOjPZyuKohQeFFFgA2jJjDY-sQggjJhg3X8LEd-yChQauFzZ5pBoYyNuyK8P_uKdQRLQ5vWJaDGOCwUjMxDQ19JXRwUJoK0Em-IWCYROpGa6TxFstoaBf2yDI2rIQnK8QygW5ACWeTQhNady3-wOpIoGrnzqt1JJlorfbgIsis6U2w5ZqRUAa3bnYIXeswhqGfxpnJQyMROxbIjVA-FWyfJQ5AzhfxLl6Ty1_oelu-2OPlzO8ZC59AahPIhJBi6eC3ijgVoRgb8Q_flGK4KTl1FRoBNH7hPhG0LPE4MSu4v5b3BtkV3IVf0l3YxZvHzRPyqxFBnUOzwcSMWn_fkqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: دشمنانی که گفتند می‌خواهند از طریق اقتصاد ایران را زمین بزنند، آرزوی خود را به گور خواهند برد
🔹
برای حداقل ۲ سال برنامۀ مقاومت در اقتصاد داریم و برای هر توطئه‌ای که دشمن علیه ما اجرا کند برنامۀ متقابل داریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/454260" target="_blank">📅 20:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmMSOvItiAdaHXz8GhowPO2j3pL4HVTZUuBtaH61iunkABylufcn5ECDbLSIg30p4Dn8V0c6GurSO8uZfLY0mQXTTeqQ7czFrqkIFfw8iyp_AtnIkKoWPufmkR75EBtyjPgc-69rsxi0dI-cNWZoh9KNGlwSjdgU10n78tcY0_Z4ejQ8TRd8XENCwgOX4YLr-O-AQo10y4ymRW7m4pFYxrVNEsvfKIQ5ELLSgBwSRzkZWI-vayyH2F_sqbaeVip__JCw20duediSFha33c9ITp6hAJJrMmA9fNd3vUSxMHIq5H99V6jSForQ2jtXQIW6zLx9er74cL57LNqvrLsnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrnCHSqOwJrrd6MuqxlOOyM0YcNLUYfGuJXpxa-Xcsv3tXrAjmngV1IpJsZuZqUsc1A4qvjXpMIjr3McDgsBoaCSfzw-PpxpzR1bO0XC1RaY0cV8Va47WZiJsKnghTwoaxrxY5NqzCrcumNxNWERHc-Uh7OLG2nerbgZzJV8w_aCFIC6X1KQKpOrb7fEq5uRMWvVzGEoMwpZ2oGEoj9JVDVb4VnW8GE-_VU4frnozQhvaN6vSeFwmDlGvLM3JJZV3qMeAl1GnKqyL1KpTxCqtXb714H8j32rYt-jIPYY2LIFHEY7jYAulopcjxM6V9cJBxDPQJUEa8UhDNYl8HFAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQF5p7rr0exrFhj_r6chMm1jyQVnDVVq4hWOGANWoB5QEJ-1zovZJlN_soCobn6Ic5JIRz-M6eMvIdeZte6EdDpPGGUhmv_zGxjyO4oSburajjF0EcCSXKSPGnmjHXkBG4uNjRhkV_hY5cdLjiqZSuveCpWF55bI63YyaB7MBERx1Jl0B7if7mSv_k9A-lQHnrvXnnS0GqpG16SGDj-rdW_1eyf0_O_dng3V9lpqbtWAAZ7IjU919Et80r1nL5MciqxLRiiZX24ib9PWj-_J0ak0iGNDeWGs0UuzYdy1W99Wrdax9BEOonn3vHVurfOcsZvaAo911btx-9o4KS-GBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvMKb6XrtvBA3OiP9nq2Ur7craw-yuXFRXCL1EIygCTpa7xYx1b54lG_hNhmtvCSMRjlHCEnBO1MYCM2N5XM8_6ggWQOGoQQz_0fpGSMhAFKOu0247Ajc4ky5v_APIHH9DhXZUY7oNYgdp0lkXgtxBj-w8QoQF40x1wPn5cArQM39K1q4AI8Tq5jlp2-X8RcH4WuXlmg4BpqSy-Q0keArLpZ3zqjdfJ_Pafb84DIewrhsJxt5WCbq2VOVjl0cTkt3ThrxvSWSK5o-MEpJr94O8yGURLfKB3JtrDE74jA2rUBLxucYXlA8c6wUY9xOxuYTLgXcIdVO6u6YATlwgurZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/II6eksHeObI46NnCBg3--s1c6qodr55e_ShFL8334oUIXvTJ0ZcMej5jvhH-uKQdBEnxieZD_eZGnCj_C-FZU6Pgoj4L9rvdxW62E3ubkX_ZM8wSaTx4Afthk7OjdpHq9Wkzn8RvOk8dntduQSprir0Ldnj7Z8DOXvnQUEka8E-0DAY5nJfJ-DURdbgXuo3KCxhHQ3N3QLaad33ZLzfDT9cV0wNkPOL73tsBTb5CqAIuFlxmceUOmQmgUfs2h-EwoXUPWcGNJUof7xIYi8zxuDq8SiMN8uhM03F5-u2UKmibevDjCouNjO4LekFH8zVc7msnuCje0TKgQ4OMg6YUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlXDNYDEwEmWSfz3jCVFMj7L5L_cq7-XbAeVnzp1pZ3zhTaa9qv1HecdTYYGEIVUQkgKh6l79umowZGcIjySm9gIgMWllAk_gVpY64BeSRf5mrORb6cgFzgVajJCrIqVcB_usffHm-dvfZC0Bf_Uj97B4uQEhuSar6YdfeYWDkGzCf4KG3t0QdGZ7nWQ0uUvM08rUmYjQbFiPwKiZfcebNvEfVL0pT8TRLEOtBTqXsyXDN3Y0J-PSvD2KTi_MMQyib6YwPfoTBXpypoo5t4YBVaNDTwJePfpfA94AHJGtGa5gh1cr8rzKuvouO3mZEO-RFBmgCdkW55blUjjbAD8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMl3xvfwk2Axk0QHaHe1emVnwI-Nnw7A7lln4kb7DQK-jtXnHpmO-g5l-rW0pI0I93m_9Smc1aByM0qYo6uJOl00lnKFEjr9_uUz_5qZralhYfdBNn_vI-9ekm78bg0f652h6CWisrIyNi9-HtKP__T_dZfY54ys6750S12Of7aS7nKrTEXjM0uTkkKcmIC4kJ4lf4tYoI-WUi3DP-tiqYTkrLcbC82KpDpQ8Vz705UVb1sxLcSjZE22gbl-J5JRwv-3RT0R_D7EFbuAoCuAnt_VCeunOzVhS8nzKAcqXr9s1BJhLpQIa1sUKnfsWZO9xaeUPPXjjnc7Vr1-aUp4-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد شبانۀ زائران در مرز خسروی
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/454253" target="_blank">📅 20:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">درهای استادیوم را به روی تماشاگران باز کنید
🔹
«زمین و تماشاگر که ندارید، لیگ را پلی‌استیشنی برگزار کنید». پیمان یوسفی، مجری برنامۀ ورزش و مردم این جمله را در واکنش به‌احتمال برگزاری فصل جدید لیگ بدون حضور تماشاگران عنوان کرد.
🔹
سخنگوی فدراسیون فوتبال گفته جمع‌بندی نهایی درباره حضور تماشاگران بعد از جلسات سازمان لیگ انجام می‌شود، اما تأکید کرد: «لیگ با تماشاگر، لیگه.»
🔹
لیگ برتر اواسط دی‌ماه پارسال به‌دلیل ناآرامی‌ها بدون تماشاگر شد. بااین‌حال بهمن ۱۴۰۴ به شرایط عادی برگشت و چند بازی از جمله مس رفسنجان و استقلال خوزستان با تماشاگر برگزار شد.
🔹
با وقوع جنگ آمریکا و اسرائیل علیه ایران به طور کل بازی‌های لیگ برتر ناتمام ماند اما تماشاگران در بازی‌های لیگ‌های پایین‌تر از جمله لیگ یک و دو حضور داشتند و بدون مشکل خاصی به تشویق تیمشان پرداختند. حالا رئیس فدراسیون فوتبال گفته آن‌ها تمام تلاششان را می‌کنند که فصل جدید لیگ برتر با حضور تماشاگران برگزار شود.
🔹
برخی معتقدند باتوجه‌به شرایط بازی‌ها باید بدون تماشاگر باشد اما برگزاری با حضور هواداران تیم‌ها باعث نشاط بخشی از جامعه، هیجان‌انگیزتر شدن بازی‌ها و از همه مهم‌تر درآمدزایی باشگاه‌ها و فدراسیون در روزهای سخت اقتصادی می‌شود.
🔹
وزیر ورزش پارسال در این باره عنوان کرده بود: «همین کری خوانی‌ها باعث نشاط، سرگرمی، تحرک و صمیمت می‌شود. خواهش من این است که برگزاری بازی‌ها با حضور تماشاگران در شورای تأمین مطرح شود». تاجرنیا، سرپرست مدیرعاملی استقلال از زاویه‌ای تازه به با تماشاگر بودن بازی‌ها اشاره کرده و گفته: «ما مدعی AFC هستیم که چرا میزبانی را گرفته. برگزاری مسابقات بدون تماشاگر، پیام می‌دهد که شرایط آماده نیست».
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/454252" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d7974cae.mp4?token=hfKSZsg1NjDVeSOWReAe4k7CJGOluRHwuy0hGFEQknoNHHcnggvV8-_I5yFMc6M75IZ0RovXGkDKPnnYKnhQvm4LB92hzTWbPD0dgPqg4rRHH7QNVRT_YvFyLVi-ZFJY_4aH8rNP-idyIjoXJMMneS5-WDb2zFqeKcWpdd8b41fW1aDBi8M_UwVmO2qQX87eKgv6r8cZszUZh0WirxK9oH3f6S1X9w7NN1x9jCdv1yA-6yOKj3n-FQxpX6FOs642uapC51yEd8Y3OX8xxbITVIWA74wVyRW54pr4gTNtXTkKxmXFiqxgGERdcgxY3F6hDNwK_4OHHbq6Zx3wel8YXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d7974cae.mp4?token=hfKSZsg1NjDVeSOWReAe4k7CJGOluRHwuy0hGFEQknoNHHcnggvV8-_I5yFMc6M75IZ0RovXGkDKPnnYKnhQvm4LB92hzTWbPD0dgPqg4rRHH7QNVRT_YvFyLVi-ZFJY_4aH8rNP-idyIjoXJMMneS5-WDb2zFqeKcWpdd8b41fW1aDBi8M_UwVmO2qQX87eKgv6r8cZszUZh0WirxK9oH3f6S1X9w7NN1x9jCdv1yA-6yOKj3n-FQxpX6FOs642uapC51yEd8Y3OX8xxbITVIWA74wVyRW54pr4gTNtXTkKxmXFiqxgGERdcgxY3F6hDNwK_4OHHbq6Zx3wel8YXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این کودک ایرانی گم‌شده، شما او را می‌شناسید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/454251" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2714274f4c.mp4?token=SBVRc80rqbMWHbzaPCw6Fq6t8MMbQJWu5hPEYn3kzDme9rftRZWUyUXhVRVxOhGCgjGdkHYWGTnTUaeNawlbBWpgnpQzWQA1WhzyUrDg3FkVB2NxzS_BS3-kDBBvEEcr3CYJEHV7MS9jTAQvTTYnA27koccfd0UoSPPCDSSNwgXdYjks0VeRwSVp-Lff8I8yWLx9Kfb0gcYzp5-SIil-TOxLQqM9NP9Fj0eXBUAx7rNUg1gA2nVdYGdkTRzDOdNBvD2m4SHTth314N0eEff7JgxF-19H2x7HSmONuAsIF6YGHhHaRTu2t0FRS5IW-KH_rs8LyTdX8jvlNiNALy9_eblEgfG_YnDEOC1mGAWNnRVrvXxjTZ89nfFag7EwFdXC8JtbYNq0YuTSInjuVVbvR4pz35vFE55ocV25YNsdeZ8_WUMJjVrRDAnoMcjqATEV8Pc8f1UZG7PpiBIvUypM-uE5JLzDDO4TedloKQFTVD0pBrXCFcGa42vVf6HnU3FFjyhT0hFDX3eJcqlGdMt1zcOoYFp5vEFlc8O73qTgz9f0x7tQulQtzm-U9CuUrfaWlX8Hvkj9rbrA0BlhZ60EHx8TsE4Ixi99dwLdfYlrLlBziTUXCbf-Ntg6Uh3q-YZ3Th8GIAg2CEICjL4pKJHKGDGUJ2tQfT7qvCDfUyxwALk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2714274f4c.mp4?token=SBVRc80rqbMWHbzaPCw6Fq6t8MMbQJWu5hPEYn3kzDme9rftRZWUyUXhVRVxOhGCgjGdkHYWGTnTUaeNawlbBWpgnpQzWQA1WhzyUrDg3FkVB2NxzS_BS3-kDBBvEEcr3CYJEHV7MS9jTAQvTTYnA27koccfd0UoSPPCDSSNwgXdYjks0VeRwSVp-Lff8I8yWLx9Kfb0gcYzp5-SIil-TOxLQqM9NP9Fj0eXBUAx7rNUg1gA2nVdYGdkTRzDOdNBvD2m4SHTth314N0eEff7JgxF-19H2x7HSmONuAsIF6YGHhHaRTu2t0FRS5IW-KH_rs8LyTdX8jvlNiNALy9_eblEgfG_YnDEOC1mGAWNnRVrvXxjTZ89nfFag7EwFdXC8JtbYNq0YuTSInjuVVbvR4pz35vFE55ocV25YNsdeZ8_WUMJjVrRDAnoMcjqATEV8Pc8f1UZG7PpiBIvUypM-uE5JLzDDO4TedloKQFTVD0pBrXCFcGa42vVf6HnU3FFjyhT0hFDX3eJcqlGdMt1zcOoYFp5vEFlc8O73qTgz9f0x7tQulQtzm-U9CuUrfaWlX8Hvkj9rbrA0BlhZ60EHx8TsE4Ixi99dwLdfYlrLlBziTUXCbf-Ntg6Uh3q-YZ3Th8GIAg2CEICjL4pKJHKGDGUJ2tQfT7qvCDfUyxwALk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توزیع ۵ هزار پرچم خونخواهی رهبر شهید انقلاب در موکب مردمی سازمان رفاه، خدمات و مشارکت‌های مردمی شهرداری تهران در مرز زرباطیه
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/454250" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=JdMELVhaBvfdld6mGeiiumpTKplBwKZvBTvlG51V3JeTvcO9ZHThn9fZQ0BwUG_AlS3nNkmYjCJXv8M90-jUEMdyqni1NvMXORsxsqjVldqkVpr3icx4M3-jryiizTVro2quO9h8JX6kEMjAD6XcuvdCILXUkSXWE_4qtsCMc_gjyIiACVEi_dlONwJJMW4h-1W1caCodSfn36ajxWARhdp-HOtRvv9BsgJYyIz_Tj4uRH5xMZfkiH3VEa2s0nfKfY6IA8fSiaZcnoHzjortIH2F4aOjHMdNAWZFLSXvFlD99P3CYrGAoMPdyp2C7OaYgRIlWRfu2OJmkGS-xH-GKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=JdMELVhaBvfdld6mGeiiumpTKplBwKZvBTvlG51V3JeTvcO9ZHThn9fZQ0BwUG_AlS3nNkmYjCJXv8M90-jUEMdyqni1NvMXORsxsqjVldqkVpr3icx4M3-jryiizTVro2quO9h8JX6kEMjAD6XcuvdCILXUkSXWE_4qtsCMc_gjyIiACVEi_dlONwJJMW4h-1W1caCodSfn36ajxWARhdp-HOtRvv9BsgJYyIz_Tj4uRH5xMZfkiH3VEa2s0nfKfY6IA8fSiaZcnoHzjortIH2F4aOjHMdNAWZFLSXvFlD99P3CYrGAoMPdyp2C7OaYgRIlWRfu2OJmkGS-xH-GKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
این کلیپ از حضور قهرمان مسابقات مردان آهنین در اربعین و خدمت به زائرین، میلیون‌ها بار در رسانه‌های عربی دیده شده است
.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/454249" target="_blank">📅 20:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750dcb2b9d.mp4?token=bbE0OgrIN7s8AuU9hfqswRHt010YT7rkhoh-8NA_gA237WMfTzoyH1hShO9XYQNX1patB3C9VCtYYk2EdH0GCJ3z8Xf7g-DXkDhaNTEnoSxMWsjG5emmC1RqLeW5zamuJ90uFoct84JVQnNSRZ-8sU-n065kA9bATumDlfGNs3mLIQv2oX03b99b2Wr4-DTGGEzpEEl6gN2B4LHFWGBnFTih4wTWdaNoQu5c_sJZcwlE161zGvhJJDb96aV_HrWFPtMYHZj5Ij9tmt2jUM3uwybnM4m5lmUA2S93Z1Un7GppBJ7AjoesuT0V-iTxEn94zlPJ8vsvGVkp6lklpsci8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750dcb2b9d.mp4?token=bbE0OgrIN7s8AuU9hfqswRHt010YT7rkhoh-8NA_gA237WMfTzoyH1hShO9XYQNX1patB3C9VCtYYk2EdH0GCJ3z8Xf7g-DXkDhaNTEnoSxMWsjG5emmC1RqLeW5zamuJ90uFoct84JVQnNSRZ-8sU-n065kA9bATumDlfGNs3mLIQv2oX03b99b2Wr4-DTGGEzpEEl6gN2B4LHFWGBnFTih4wTWdaNoQu5c_sJZcwlE161zGvhJJDb96aV_HrWFPtMYHZj5Ij9tmt2jUM3uwybnM4m5lmUA2S93Z1Un7GppBJ7AjoesuT0V-iTxEn94zlPJ8vsvGVkp6lklpsci8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواکب گروه شستا در پایانه مرزی شلمچه
🔹
اربعین حسینی(ع)
#شستا_کنار_مردم
@shastamedia</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/454248" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/454247" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ دوباره رفتار همیشگی‌اش را تکرار کرد
🔹
رئیس‌جمهور آمریکا بار دیگر ایران را به «رفتار دوگانه» متهم کرد و مدعی شد مقام‌های ایرانی خواستار مذاکره هستند، اما آن را در رسانه‌ها تکذیب می‌کنند. او همچنین ادعا کرد تنگهٔ هرمز در کنترل آمریکاست و در پایان نیز از…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/454246" target="_blank">📅 20:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
مقاومت اسلامی عراق: پاسخ ما به عربستان و آمریکا قطعی است
🔹
برای حفظ امنیت زائران حضرت اباعبدالله الحسین(ع) و خادمان موکب‌ها و جلوگیری از هرگونه اخلال در مراسم اربعین، پاسخ ما به تجاوز آمریکا تا پایان این مراسم به تعویق خواهد افتاد؛ اما این پاسخ قطعی است…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/454245" target="_blank">📅 20:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
خادم عراقی: شهادت آیت‌الله خامنه‌ای و ایستادگی ملت ایران دربرابر استکبار به ما انگیزه می‌دهد تا درخط حسینی استوار باشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/454244" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c001b59ea.mp4?token=TvwPSrXeH1bm_I8q-Yoimm33g4k2U9N990czhyt5xpZJ8HzAq2n20BJ1hGxsaXaE4Ye8P1hYa-NIQmaT4VZc6y_oDZxVcwpV-0jCud586LmOA7GtkTmjXGynqIL1SOvPDosmdCxK5nany-cjV6pxR4XuIsnnBUJQKDiXNf2EyhPviqaGtcq6got0a4LuxAemxLWOKGCkxrkdfDFRE108w0kcoy8k_RV2XB3Mw6MydMgNF2H3mCY2ETguxhLjpCo2maH1vjAKtj9xS22UV60-iyuLOjoRdPvG3XMkATrXPPKbD22-rfCIUnLMl27Pl0MSICthrM0-JUs0V7O8X7EYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c001b59ea.mp4?token=TvwPSrXeH1bm_I8q-Yoimm33g4k2U9N990czhyt5xpZJ8HzAq2n20BJ1hGxsaXaE4Ye8P1hYa-NIQmaT4VZc6y_oDZxVcwpV-0jCud586LmOA7GtkTmjXGynqIL1SOvPDosmdCxK5nany-cjV6pxR4XuIsnnBUJQKDiXNf2EyhPviqaGtcq6got0a4LuxAemxLWOKGCkxrkdfDFRE108w0kcoy8k_RV2XB3Mw6MydMgNF2H3mCY2ETguxhLjpCo2maH1vjAKtj9xS22UV60-iyuLOjoRdPvG3XMkATrXPPKbD22-rfCIUnLMl27Pl0MSICthrM0-JUs0V7O8X7EYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بزرگترین پرچم خو‌ن‌خواهی امام شهید در بین‌الحرمین  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/454242" target="_blank">📅 20:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ef204199.mp4?token=eAu5NC0xixu4FdaMVjlFSZOwPAli-SvEvI1-ALDqt2NfUJk-IbNhilHSogUVVHQljOf_7YNLezGkUf7Qsx-MlfBqJdBNqyBU_vqKqAmJOq5xdhypXSLpCdKsQQOMV5Q7TP4F-yOOd7CcZ-o-Bk-0zZ4LsTy5xSzLyH1gmF3iTKozKLTRKO8aU56lTyhmojmO8O0Bvnjx6Tij23WeeSxDhrrLNmIarnxZDRQsE_NzwQHN703a1Vok9ZyflxYuNU3yel1di6FlinkJDO2khcCpMXNMsH3Vhs_tZ1jo0P7Gebie11VzYdGgSlxRBdqx1KeavZmzxcLz8ljhGM9-dXYZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ef204199.mp4?token=eAu5NC0xixu4FdaMVjlFSZOwPAli-SvEvI1-ALDqt2NfUJk-IbNhilHSogUVVHQljOf_7YNLezGkUf7Qsx-MlfBqJdBNqyBU_vqKqAmJOq5xdhypXSLpCdKsQQOMV5Q7TP4F-yOOd7CcZ-o-Bk-0zZ4LsTy5xSzLyH1gmF3iTKozKLTRKO8aU56lTyhmojmO8O0Bvnjx6Tij23WeeSxDhrrLNmIarnxZDRQsE_NzwQHN703a1Vok9ZyflxYuNU3yel1di6FlinkJDO2khcCpMXNMsH3Vhs_tZ1jo0P7Gebie11VzYdGgSlxRBdqx1KeavZmzxcLz8ljhGM9-dXYZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کوچک‌ترین خادم اربعین، مسیر پیاده‌روی زوار را نظافت می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/454241" target="_blank">📅 19:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNydNhZOCf-6RsGZd4w7y7Ac9SgBtICa3_r0ZM-mloAy-G7NQqhC91E2oBngSuRvIPygwxxe8r7mlKdkM1kb-c2l6BHgDYqQolNiRJQFJtnmvs7I-x2M_INeseAnhgcXXGaPed5iliFBJRV1uqrtx4Nd6kEJw9q6HAmE9N98qbV4shK6FeLBQH0_3A9oX_dwwptnG5zn6Q6oOcPzOPmXfwdKptAwv01YPxXf4pR-LBcskq9nqz1TZhjG5tzr8h0cvSKXyM-E9yG4FPtZPrlilT78Gq0VeTxKAlAxrvNMlnfE_WHNT6Pe7wJ9O1lZzdp_fu_HaHjbcxJlYBDBraxxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: هزار مگاوات به ظرفیت شبکۀ برق کشور افزوده شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/454240" target="_blank">📅 19:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FB3nF8ewoZ4KTNHnHdFgEStEVa5t7CUstKafzY_XRue8PJprsl3Vo_2Z4HIPGQnVpIW77hEatITunvm1qOwi3xp5knNkHpH50hQ2-zgW9y0kfD2lcfUVruHj-UQvTgvbBIslF5sCMjABqiCQ2um-8MO8qdXCazF67DfGjq81VLHmyeuaUfxOF3RAP0EnenrKAsQGMJavWTmAUelt3S0MRQMs177GComEFWZLrdZcGS4RYlkHSIRWPa3CbHkOAQBoyGOUu1rViKXK9tPaS2U9FZGdCB8pnaTT5-IXgDx6nparn09kwrpffSwQQJ6L-YbzYqU8eztZ3MjYIdgcCo3E0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzlbcfFLn57LrH6NjXdVVhLYCyoXYV-5yqRbRRAV_vG1Kthp9Am-4g659ZDR4lSFDmoJoPHyhnz3djO6WdzPUnyWMvhlQE0kicpCn09GGEUZW_mmyZJGoGu6TNk6yleQLDtKutH73AjoC-XP28uakFBEhL48TWJp8mIFDFJxl3V6OlWWxyKFrqiA2DJsuZWGlter4dx9i_gdrsR4KwJ8qUFazjMEI2jFsJx9szn5U4dUnVFDlMw3GsyAQVS8p85Jo7tEunzA4vh1Ab9re5pStE_G93UVw96mOc3GlGKQbdC-FJ-RX5NwqPCruDbtONqIb6h9vHawIBJWs9ZzxiCcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7-UV3skdKZvKNJa8_nLoXmgOsU2vgvZPakx3QAAMC_Uzhij9guGEi25_f7VvVsT8joHeKtUw3lZIWYTE8Dfj-b79d8962QDmDhBxSi5MHiA2IiALfF2BlgtMqx9R_YEh0pnxh9KZhGU_7VfsZZex1-Fj6YlRD2iDi2Hd1FCGJSHklVQE9ckBmiBzfjoNyILlOq0159qy3OctgPUYXacBP0NQkhzZP1DNNkwgvHdVI9Cv10gS3Y9RDvgD8xlnbAwNLVbrHBilwKteruLJHsDkZRhTUDN3L2lL89XOY1z0sAAXWsX0KdyFT5Wy1Xd_3bmFclm5DJhsqweRxxdrWU3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNCtnmx4xqoBtdVKcB9f3eygyn6Px61RTivVRGViJIm80179NBfbuqxGINoQBa_wyeJUNOE95PFTAjy4Rz8Z3--SIvYrHM4DSEqOM_I8LtSRY2LVkrdu3mqD4kL8XcclxhVwhsCpzMbSSg58_RagxP_ixHUb0grK2MLRU8R_3e9GBbYiMb1l2xPIEY6HDD_YlP0r6WRjVGuOdt_YY6WhqCNkBHsBHMbW8n6tZeJPeZrvXyvJK_75jNfqKXZi4EoMQ1upGdQUyO3S71doWgt_U1eHySrackgdRSkvD7UHht12wEeTbdv49hpMqu3gPhBfyHcCKaXlDNy8bNzIGY6J7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQp6xWjMsGdmctNifHsoAJvjjeHNkg1FXgzNyYSD2Ng_EfuQaygfiRNfVBLVX47SejHzPYw3kplVk48ANDB4rvV7fbULAggivE3vaFTDu4vhiG6664f_x4pvAjZAVTV98wxwanXg004jfVLkbiQOWqfWp2Dx7XMo7-MPicn7h6YnV171LHvtxbz_ZuNQcI2lV5efI4GnnAC1YGkj5gM0RXPYHW-REybuSzBDiAdvwiYs6oMcpMGiRW-_BGBUfi_AzhYlFA53nogdjeIHp3WXRs86XelZ80AYWDhQwQUJwYUe21s-sVkipFBWyNuDAtBebgenjLal3Z6zSg7VnaP_lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگترین پرچم خو‌ن‌خواهی امام شهید در بین‌الحرمین
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/454235" target="_blank">📅 19:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOBw_rWShrmnpY9AzAPxVRlqkmMXtzpzm9P-E9RtiwJqY1i5Oeii_23xwuAIcgbI3daN38MWuvl9gjbx9OP8QbVok8CMoT3UJkM6sNl-_0Kr1YbP99cUAOcOh9Pm_8xl0oJMVxQXGPZ6LuXjt550P7BLKecqzNd3dzFgWq6jkbErbVk8WjSiwQ7AA-PJ_v6kZyERd3JpPjd6ZE5s8SIqDHfVAKjeZpkz4Mgr6Rzgn3RNrF_7NgKdlrcMlUbTT0mHMlZ0gC8I6Yk2FMLRppu2Tbq7sJY4M9ajnGBDumD6uevW7D3vaLKsURRYKbrmnTIYzTvX562oRh0EoUOMeBNtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پاکستان هم ادعای ترامپ در مورد مذاکرات ادعایی را رد کرد
🔹
درحالی‌که ترامپ مدعی شده بود که «مذاکرات با ایران دوشنبه آغاز می‌شود» مقامات پاکستانی اعلام کرده‌اند که «هنوز هیچ تاریخ یا مکان مشخصی برای برگزاری مذاکرات مستقیم ایران و آمریکا نهایی نشده است». @Farsna…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/454234" target="_blank">📅 19:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
تردد زائران در مرز خسروی در آستانۀ اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/454233" target="_blank">📅 19:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNGQrxhbmwccyovq83gT4f9z48LJOatM8GUxsnVL-_eVfFfxmZ2rG5zNe5vo4wMTQT69pE3oTZxMBWM38yjOR_oLaHER9yqe9jWG6k1EQrcjOUOwteZL61Caq76TGfYYzpZD9T2Hmq00yv_HMmDj41ooNaiaxG62BiWVBnvB2FllPp0ouoWFU83nzZWLMCFX-zDvmWymUX8Wn1lNvbrhpDHPDvPySKBnDl0xh6KteOTTnkaXFUoFDKyTHnLt_cP2jolJXBsO-xA-Kn0V0Y3ezN_nBPzPTLqnPjtzdMrIi8G404IDUAXL0u7SnbtE_Ifco3x9BHn6jOHN_iYOeuS0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: میراث سلیمانی آمریکا را در خاورمیانه رها نکرده است
🔹
نشریۀ انگلیسی تلگراف: باوجود گذشت چندین سال، یادگار سلیمانی، فرماندۀ سابق سپاه قدس ایران همچنان در منطقه درحال نقش‌آفرینی است.
🔹
گروه‌های مقاومت، به عنوان میراث‌های او در بافت سیاسی، اقتصادی و اجتماعی عراق تنیده شده‌اند، شبکه‌های تجاری ایجاد کرده و کرسی‌هایی در پارلمان و دولت دارند.
🔹
دولت ترامپ به مسئولان عراقی فشار آورده تا این گروه‌ها را مهار کنند، اما کارشناسان عراقی می‌گویند که نیروهای بسیج مردمی را هیچ‌کس نمی‌تواند منحل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/454232" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABNRLrEmfQe20X6CcYWWmjRLoV9gSVJuqqoLsaLn5WTsiREjWPIhKA1ByKhKTGtKmnC6Y17vSEwVx8ziE9xi8UidJQ144TBUHYe-JwJ1wevfm1Ascmj5MbqQsVFWYP34n3ZwNGA-a-jv9Zts-PrrguZXuun87_luryvgU09vDRNAd8Zo__GrwFAZDvwt9rykVxdjhEEkPExETg4LPa5KSPa6covzsVjJ-OCDo7S5xHAYrNRvGFHsEOECGKo5iTe05RhbPPq1M5oMhZ9CKL7qbQ7I_K8a7Y5ycnpiZyVPz3JTDUw30VeFMaLtrwD2_hsAue06U9GWJioMWhNaalwNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار رادان: تصادفات اربعین ۲۵ درصد کاهش یافت
🔹
فرمانده کل فراجا با اعلام کاهش ۲۵ درصدی تصادفات اربعین نسبت به سال گذشته، از رانندگان خواست با استراحت کافی در مسیر بازگشت از خستگی و سرعت غیرمجاز که مهم‌ترین عوامل بروز حوادث هستند، جلوگیری کنند.
@Fasrna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/454231" target="_blank">📅 19:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454230">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb9aCT50v4JFfZHpAOHLhsu2Azrj2eQoCg-ysaKfcGDjFm1PSjUYjk8IIpnSmiKxYd0V-wBxTdeFQkBwaAcxw1JU6gut_aIlexKHo2jfxOUYLU1kI98rl_PGZg1-FvUIgbvIImb1prsDfmst6UJeveDZnATjOwFgznsipofIJ9C8yJPYfl_9H90Z188gfvp4tSco6VjVkFldA479tAGomQlNG-UEbT0yBPdqt_Z1Pc1OCRzhOSjG1HPVvWF7p0qiqkowgX1P9F__PO-zE-pj1Re5XfrovvRh4kDNTXqDS7XcmJJLn5IYaeIL5oxw2pRiz2dCJPv51SF2PP2BzrutNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی زمینی سپاه: درصورت هرگونه خطای گروهک‌های تروریستی این سرزمین را به گورستان عناصر مزدور بدل می‌کنیم
🔹
سردار محمد کرمی در بازدید مناطق عملیاتی شمال‌غرب: به حول و قوه الهی با تجربه گرانقدر سال‌های متمادی دفاع از سرزمین مقدس ایران اسلامی و بهره گیری از ایمان و تکنولوژی و علوم روز، رزمندگان قرارگاه حمزه سیدالشهدا علیه‌السلام نیروی زمینی سپاه، تحت فرمان فرمانده معظم کل قوا، آماده برخورد با هرگونه خطای محاسباتی دشمنان خارجی و سران و عناصر گروهکهای تروریستی هستند تا این سرزمین را به گورستان دسته جمعی عناصر خبیث و مزدور مبدل نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454230" target="_blank">📅 19:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad128bef1.mp4?token=q9pPc5skLzbVh1iB_nbCEdLHUwWpvHpgEE0axYtsml6zu978sR6ko45J9wDwEJIKPSS36b2uXAwS8LGl2wUFIKUtSntyApo4dDVBOpThDQgp8mcSNS2VX1RDzet6uEbnXAfHpYjmRutoIeAQU6NF8RI_rf8umQodyFn3P9xIO6dg5L3SZG1uMPRYu-OLU_UP8Uj-58xiSPjbohgwtsQJ11-op9akJlcV_hLUt18mG3Z9NbcYNlufpKj-h6yqBia6__CPBUg3DLnuf-9-mbcCehGZcgdueTtA-laDTuMM6JjR4PwEYMTL3tPYN3-FVTNrsgzPZOUG1E6-_CMxz1Is9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad128bef1.mp4?token=q9pPc5skLzbVh1iB_nbCEdLHUwWpvHpgEE0axYtsml6zu978sR6ko45J9wDwEJIKPSS36b2uXAwS8LGl2wUFIKUtSntyApo4dDVBOpThDQgp8mcSNS2VX1RDzet6uEbnXAfHpYjmRutoIeAQU6NF8RI_rf8umQodyFn3P9xIO6dg5L3SZG1uMPRYu-OLU_UP8Uj-58xiSPjbohgwtsQJ11-op9akJlcV_hLUt18mG3Z9NbcYNlufpKj-h6yqBia6__CPBUg3DLnuf-9-mbcCehGZcgdueTtA-laDTuMM6JjR4PwEYMTL3tPYN3-FVTNrsgzPZOUG1E6-_CMxz1Is9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای مضحک نتانیاهو: اکثریت قاطع مردم ایران شیفتهٔ اسرائیل هستند!  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454229" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76554f0287.mp4?token=qYiB35ANUKFrgutilK2ZYG6T0Z6s6Y64ACQtG_xfDgDJgqptF8WTD7ZMaURH1yqzLJsGJ7D-3WEKJf8aZX0Ym1eFUPoxNo2hD3MvzcCMOAqrhJKZuE2W-Qlv0kNKgzmhURZMBJu7SS6284uD59789mUUhnHohjJ9z6mG1Qd80gOO8lGUNLh4PgBqj3nzRCHUJvuNbQ8BkXMJJq4O5VuDcVoO88TMYGeY9C2etrPjxAPazTNJjXejXTkTZcR_nHKwyAmu3mp8DRBckmoA1XVAzaeCuAWxkfY68yjx0BIy9AA3wr-e7aRWc-6AMmV4VICVw_-6sinF9VbczeCVuizJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76554f0287.mp4?token=qYiB35ANUKFrgutilK2ZYG6T0Z6s6Y64ACQtG_xfDgDJgqptF8WTD7ZMaURH1yqzLJsGJ7D-3WEKJf8aZX0Ym1eFUPoxNo2hD3MvzcCMOAqrhJKZuE2W-Qlv0kNKgzmhURZMBJu7SS6284uD59789mUUhnHohjJ9z6mG1Qd80gOO8lGUNLh4PgBqj3nzRCHUJvuNbQ8BkXMJJq4O5VuDcVoO88TMYGeY9C2etrPjxAPazTNJjXejXTkTZcR_nHKwyAmu3mp8DRBckmoA1XVAzaeCuAWxkfY68yjx0BIy9AA3wr-e7aRWc-6AMmV4VICVw_-6sinF9VbczeCVuizJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای مضحک نتانیاهو: اکثریت قاطع مردم ایران شیفتهٔ اسرائیل هستند!
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454228" target="_blank">📅 18:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گفت‌وگوی تلفنی وزرای خارجۀ ایران و پاکستان
🔹
عراقچی و وزیر خارجۀ پاکستان، در تماس تلفنی آخرین تحولات منطقه و روند رایزنی‌های دیپلماتیک جاری را بررسی کردند.
🔹
وزرای خارجۀ دو کشور در این گفت‌وگو بر تداوم همکاری‌ها و رایزنی‌های نزدیک با هدف برقراری صلح و ثبات پایدار در منطقه تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454227" target="_blank">📅 18:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31ea1a5cc.mp4?token=MDT7sYnArKUYB5TkzhlHsATJ46jmgk71r55detzDJEwwawcAIUK7XQBfT4GcjJhEKV8pVg5aTast5P7N8wz4aXZ50qEoOq996KJW0f8U8Uhr_LpBruihMlYgMtTnQBwdcadPKjIIQc-V1-3rozMzZrZNoRE7nrd7ps8_AfIoeLx7-lvppLKdVICtg5U7Hn021JRooHpWyQmRmaxvLWP4eWz7bK2w6G0AQXniiHF4seW4WGgsP-Eh2rvM-_L4v2DfuatrHrPGYgR_PsETld3vg9j7IGMQkaAvPICPBgKv2dJ8ZiVgfuhiJ7cfKQUeshE_7DCKM4ykP9nN3KJTJ13qKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31ea1a5cc.mp4?token=MDT7sYnArKUYB5TkzhlHsATJ46jmgk71r55detzDJEwwawcAIUK7XQBfT4GcjJhEKV8pVg5aTast5P7N8wz4aXZ50qEoOq996KJW0f8U8Uhr_LpBruihMlYgMtTnQBwdcadPKjIIQc-V1-3rozMzZrZNoRE7nrd7ps8_AfIoeLx7-lvppLKdVICtg5U7Hn021JRooHpWyQmRmaxvLWP4eWz7bK2w6G0AQXniiHF4seW4WGgsP-Eh2rvM-_L4v2DfuatrHrPGYgR_PsETld3vg9j7IGMQkaAvPICPBgKv2dJ8ZiVgfuhiJ7cfKQUeshE_7DCKM4ykP9nN3KJTJ13qKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاص‌ترین اربعینی که رفتید کِی بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454226" target="_blank">📅 18:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCDOJmaoN7jKIxeivlGHXyHIed5gO6-lvYtlsdkNjm3MHuulDYIpwxFjbeWe6Ljb2yq8aqRe9HJwtNIZOWSxzwerjCGz5SCBQIHF6hE_McOsVgsh7D2R0po9IIY_K_RSMA14hdVZxQ5LM-N4QfBbN617TLKqpNJnX8JzuNM4Tz9pi2ISK0bFB1ymEmGNsJkicC-iEPSXIoi7bG-qqM2puH1Ws33dRK79gCb-cKlYXxya7dCm4HGz5IOL8przb_7ZkiiYuLsoEiN7dywMcGkorghou2U7lqALTFqTI7CifB8KqD7LY2OmKOd_PP15cESE73ULGd6aOLFDWFf-FJRTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: شرکت‌های نفتی آمریکایی باید همین الان قیمت‌ بنزین را برای مصرف‌کنندگان کاهش دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454225" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff59fa69c9.mp4?token=n64-ZX56zNcyLMFs67P32sDogH6yez3JRCUVQ6UAYhNmS5pwnzjWtcOcfjVDqzD0Vp3Zds9VDQfnnvYpXvj0JgvvJoLhtzeR37M4EjGJKAqL1zI1-l9aF6wyZf8J25rQC0pGATja18TqX8mq3wCObMT5v_ViOclQEsiKcY0wSauTT5dIopyz_IuXolhPyF9Tmc4g13CLrR8nQ14SVgPkcMoL28ox-15btOwRDsDnd7cM8_qpV6KpVPlfmiif4dAZA3Y5z5beG0zwX7IPmKVoj4PBeblmNVdsVlvZjzNqq-aYn1d1yZVqxAcUqP2SBUz-UnGETyLuzFiNnYIRkjOF57m3rAYPrfG6ZrvN0cFW7TnGhowp5K6fc4UN783BloXW1Sasxntl-5xIGOjWHmdzI_M0dKHJIcBp6SEDydbNLkjBEAwB569kvsTE4VP5WFam3cesJ0k1pi0U_eXe-y6d0lrgaaJ09rxpNYPBfev_0JKkH-OGUB-8GC4lk59Wmt5aHGaiLpD6exWItb5GmBRqUnwdXJY44k2EWDlSldNd1k6JFRC-NNhIu6xOFfWIl_HmcKJy1kQ0Xlqqgsi4BXs6CAljOgIESFnSB_-vPXtZJ7n-uHM9FBYgqqchBif4dza5Eb6GD6RcQVv2WnSBVVeOj_s_VJlO7NAv0mGqZd1tnJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff59fa69c9.mp4?token=n64-ZX56zNcyLMFs67P32sDogH6yez3JRCUVQ6UAYhNmS5pwnzjWtcOcfjVDqzD0Vp3Zds9VDQfnnvYpXvj0JgvvJoLhtzeR37M4EjGJKAqL1zI1-l9aF6wyZf8J25rQC0pGATja18TqX8mq3wCObMT5v_ViOclQEsiKcY0wSauTT5dIopyz_IuXolhPyF9Tmc4g13CLrR8nQ14SVgPkcMoL28ox-15btOwRDsDnd7cM8_qpV6KpVPlfmiif4dAZA3Y5z5beG0zwX7IPmKVoj4PBeblmNVdsVlvZjzNqq-aYn1d1yZVqxAcUqP2SBUz-UnGETyLuzFiNnYIRkjOF57m3rAYPrfG6ZrvN0cFW7TnGhowp5K6fc4UN783BloXW1Sasxntl-5xIGOjWHmdzI_M0dKHJIcBp6SEDydbNLkjBEAwB569kvsTE4VP5WFam3cesJ0k1pi0U_eXe-y6d0lrgaaJ09rxpNYPBfev_0JKkH-OGUB-8GC4lk59Wmt5aHGaiLpD6exWItb5GmBRqUnwdXJY44k2EWDlSldNd1k6JFRC-NNhIu6xOFfWIl_HmcKJy1kQ0Xlqqgsi4BXs6CAljOgIESFnSB_-vPXtZJ7n-uHM9FBYgqqchBif4dza5Eb6GD6RcQVv2WnSBVVeOj_s_VJlO7NAv0mGqZd1tnJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌گونه جلوی خاکستر شدن طبیعت را بگیرید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454224" target="_blank">📅 17:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجار کپسول گاز در دبی کشته داد
🔹
دفتر رسانه‌ای حکومت دبی اعلام کرد انفجار کپسول گاز در یک نمایشگاه در دبی، یک کشته و ۵ مجروح برجا گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454223" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9e00a49e.mp4?token=KEjjnL8oJReNBUARgAZll39fDVTpwIdTbFXwRJTEfVHA0gD-Woh3IaCoBokHsfQ7JJNzvTRnOc90-32Isvgk0QTphNaX4hG0M4WJSCxw2Frbs-fAsROTOaxK0OLBrrRrbPY4QfhWvGopD0o7G45jH8gS_5DMiIAPE2kb4MXTsEEvYoLsk8THNWOUURD3PVDfxveerSeGwCtWJSei1FxibmckiMkZXDgoVN-5_u97KqI7BoB_lg2HIKbcMpRT-cnH9pX_BGq0AIE4jJv9XFvQhxoGVUjIqcteC_Q86pgLNMlYBpq8tEZ8b30pjkb2faBwnqf9vt494hxSVN6eBqe37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9e00a49e.mp4?token=KEjjnL8oJReNBUARgAZll39fDVTpwIdTbFXwRJTEfVHA0gD-Woh3IaCoBokHsfQ7JJNzvTRnOc90-32Isvgk0QTphNaX4hG0M4WJSCxw2Frbs-fAsROTOaxK0OLBrrRrbPY4QfhWvGopD0o7G45jH8gS_5DMiIAPE2kb4MXTsEEvYoLsk8THNWOUURD3PVDfxveerSeGwCtWJSei1FxibmckiMkZXDgoVN-5_u97KqI7BoB_lg2HIKbcMpRT-cnH9pX_BGq0AIE4jJv9XFvQhxoGVUjIqcteC_Q86pgLNMlYBpq8tEZ8b30pjkb2faBwnqf9vt494hxSVN6eBqe37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بین‌الحرمین در آستانۀ شب اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454222" target="_blank">📅 17:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR7okJffFQefJNva-lkzs85PzVQ4Xmj66cGlS4Fae1gyuYsO72wqfqB3wdHOjJjdvP7tsku0tPTM6XlApIsEhCupfUNU0scqHrv-MjLgV5Mo3BHV0S1RuNZJCB8X5Io507i_mW9yhxCUPltc2HmRcQqWj8abUpSNZ6MYOYXFABLHLTz1DYYTfhhEb29_q4lTou9H8fUtDc_YnulKkGsS8kGVgnlVHLFafP-GbFjE5ADG2Rm5gf52r2btbz9IWzvGtbFiej7FIOFQt-w_uRZNu33EB7lts3t5K_sj4ld5h2DCUshBq16dfmWNDB4yXlfSSOFpJVu8q6o9mZ-kfIYUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibVl2Gqx4hNsQPlAr-6I4VL730RIMttiybZN8M5SE6uJSszhJz7VBjhEMAfgBQBIAjOM_pYT1VB564yO3mTeBDQKWm16zWe_M-kfklx7F9Ca-S8MIsLYYqxd1O-_mgax-D9nU-LCrtJTbJEIiKYbBpLAvN_UXgxGMy0SeFnHDecYQUE3F6I82-Niw3qvlLf5Ccd0ZOe1pX6bk9uM60JJawfhHnB3RqHge9vc3rTtO2RWd91XeAgd2koEQ5orPjDRQB2x5m_xtyFED6DvmoKn4FkcMP_56c7UBzbXyIntfTL9Oa7xI6vEtwQvq_8687_6frqpK-kZ6dya69gLPUVHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzq1OHMX4ezilhSR3R-5hQsDCbgxA_P1zQwsmvv_0V6pu7q2vI-64I3DUlXbRGV5L8AO84_6R4lz-cD5GgMyvFCtKrHBGfZkGNZzZQbtcIvvcLznYTk2Xs3ahAXh4HVT2qTXVDIpOAdnPZ6BFtjZedXcPLWOJ4rCS3o74my8NtrlFOzebmXY4pvKimiooLmmeSvtR49fYmfN8GcymYJrS1Cx9cgAByCXS_pxT_HxfPKxgB0ptvbaALsp5NtiLN8OphplcmeS45bgN4odRyds8w5U6MpIDPwMPghduF037WNleA-AeSK314eUmxoUeOXCVw_7YMtvd6tRsANEM1OjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxWOtrZ5hVOCYtEGdO7ZlwjFSfEwlSq02MvjVaDVeL9XxQBs50LwzQCTd9CF_mOqtzvGiHszKcZNbQsLFu1GJ_Fvp51DsHkvFzjSGej8KAFnUHd8PYGr9nI2EvI8rvnz1GwcSvoD2uwOcmsiPg4XJ8HDxmks4eZsdKoR25D8wAeBE6objxXw8ZWAprHS0RJIUcl2T4vGNFEn0KgnRLhRGZtMnClwGKEsY1tvnqmLO7Cx33cNoP4dAhBGTN8L3EJnIfVabPRPse-TR2EWFlBY66xZEwdjt2juhK0_pYRM6cQdbsz9KWjJjdsimspyP0-Y90CB3Hs4T50V4Iacoff--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6pr0xHnE_8pkjsOnUUxvkyLIKeTD7Z4KvuMpmYEdY_UzskoJiIIWGzTXb54S-jG8QHtuhARgqawGRBEmjOR-v4kNoOIBkICZ6SIZrgIW0g6Rwk584CMvCaboTNP7fksH1Pz_xi7mdqqnFOtXT-23_i44b7QC7_1RRv29mVKrXRVZlRbXi1vniA4IyN9CVkWHqcXBxi77_PI2QiB00b4warF0lXwv2CyFvL4skotPHewTg1PSMStzkc0rbTWSLbI2pA8mhz2tsRQ946oT3rBlJ86p_0mIXuSnkGn5FLRSzHp98lWg3mUGIgKxQ4hFaKL19YUbxK9HBNPfx9Yw7G-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz_Bpw1eEVESBhwq5Os7g4WA9zfL8nH84uLzTVL6ulXpLFy-1b5jYt-4xJK3szrnFs-noR6mzveJ2GziOZM3xadOKZ1nXnMywzQQ6W-di_JzXWBrBFdbKTljs6sF3IQ5RGczN4l_BQQBX1G1DVFzuBee4YixjIpv11NQAItYYOfEZWwCBcYIdUXFzpygNPCeLfHkDwaX035-p8jsAofTs57FRxpBPMn-t5bYot9odTFnT25tfx1j1E67zQYNf5Y58kSPgaBrgoXUcC0WyCAlgTGGGXORbMBChIgyJglHywZ6n9XlxJlOxW2wBexpy8DTmBcychWjtcbcq-9Mg0FGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNCV8EevwexJloPoDyNmmFo0r-9fMHE7bIEGmt8-y7VmyVTn99uuYhO9VGQWlNmINiyOWtTEwXbQSbgpxHBTzbxHqkhRgKgfwsFCG7L-N_iqhEPHBjjzayLMyRr_edKXxuvySRRdqFO1UsO8pQQwHmhojvYWWN42xYqKJekYjqDucw2TQ_h6cPTH764its04QGT2yMywBXxlXVmYdH5dK182PpcgceXnFL24AAvih_mrOVt6LHSNZuY3k1Wmrq0inl8fGmxkbRztHKOxZx2g2wkWH2E715Fw8euDFBYmHwJh5_f4xIvMuU8wTY0YmG_xY9irozlvrpqgR5-T7AV7vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستۀ عزاداری زائران ایرانی در کربلا
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454215" target="_blank">📅 16:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH9xz_DcCkcQH_KERBpzBTerTrXqx6ZcpsIZH07Y853DmIJlQKvGH0WiauF6m5JHLdNpRldCwyHw1dNjlBsUucDNa2SPhglemZjDRaJVR6LxNTvJqB7UcXYRR2yl3fopUlyRxoHt-Vg0CCJYy7hsSjgkZzRg8JZY7CZdzJ4O_jOWi_oD4vWO--hBUZ9Wmo7Ve50Nqc3_6WmMiSfM9_I9mUykLu9V-c9oo1E_7YWpKXSHOeNV6KIzkkz7mcUqDNwk-fiuC7MQoYbKSiHxCDLtllHw_4UNtKLh3xqCWfQsLWcrI2KIjtDt5OazPlVxrGl0c1pHmpVjx4aN_viC9_cJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت متروی تهران: جهت تسهیل تردد شهروندان برای حضور در پیاده‌روی جاماندگان اربعین، فردا خدمت‌دهی مترو از ساعت ۵ صبح آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454214" target="_blank">📅 16:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiKOy4-x_oDMDRq09uoSF7RhzVcUfVIJMrp0rOpf3q68RAl5wlFc5a_XwBL1nMgfMCuQ51wgWDmiO9sl50f_12deaiPQAFauklFvDZHJFIzoKDZL3GXCDWYubN0og53Sm1hsLzeKcYMCsgeaj3NH7pVvEVGlON1fwqLET0xtFtPFqq4dmRo1x6GikELRkb8vudVAeqZ3t48YEGqhLg_Bf5_ZPRw0zMIlIJY0V07BPcUYkrRBO3jiL7bzc7hDMBjlQALE7XA6MFPqw6lpOzwLJMoch_aLwDIGFYID2rx7p7Wm31Cy5ZRWuWuZJMFZTjma2TXvnRgqmgZNEcTEz5MbKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت: طرح پزشک خانواده از ماه آینده در روستاها و شهرهای زیر ۲۰ هزار نفر اجرایی می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454213" target="_blank">📅 16:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
پاسخ سخنگوی وزارت خارجه به ادعای ترامپ دربارهٔ آغاز مذاکرات از امروز: امروز عراقچی راهی سفر اربعین است و باقی اعضای هیئت مذاکره‌کننده هم در ایران هستند!  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454212" target="_blank">📅 16:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سازمان سنجش: نتایج آزمون‌های ورودی مدارس سمپاد و نمونه‌دولتی اوایل هفتۀ آینده منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454211" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
سید بشیر حسینی در مستند راویان پرچم‌های سرخ: عظمت رهبر شهید را بیش از همیشه در عراق دیدیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454210" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7RbSLj-fKL4uAeHwu6n1lCD77FPQrWaws2LiN4h9bOFXOtIO2csVofzU5_R3Db9SCLBfeY4gQS3gM-nZoEFiqQH0QUouoTkWHcI-2-hi8O_H8Mxc-i5Q_jmNF-U4CdoYtUA7o87sQ3fSG95kzFOn3BWAzvZKxxHQOJctDYUTsWUTAKX4Snltv_TJDQYBrVOWeqWSfxfpd448UmmVftXBrcuOwRG6pI9EBAPxoGY5in1d7Nd-bVW5sLvthlC_Wmg8SbWAq6RmG6nogWapK5UNFtqqn-5_hPzXsGseSTqzRUf9Z6re_QDIQIoXPPB8QfMn9Sy0Z-ScSempL_rvpwy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود اتوبوس زائران را در مرز مهران معطل کرد
🔹
هم‌زمان با آغاز موج جدید بازگشت زائران اربعین، کمبود اتوبوس در پایانۀ مرزی مهران باعث افزایش زمان انتظار شده و زائران برای اعزام به شهرهای خود با معطلی روبه‌رو هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454209" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5cba04d5.mp4?token=XjngzR-jPQylfLeQezTQ8oI-mgB8rokDTEgqYzJHcuXnujHdxTF5Aqcs3cGjTcrTXgU9etE3AESefvhV85ypX0kfAQNIrDhsoe-NizAMJk79Vixf2qNYF2hi5gRa4KrRg3by8b_h3e3_kRsllKlu5UO2r3yHTuu0A0q-7sC-MIrjNHffGKWrYWmn8xW6WUwpRVp_LoMsJexOm6b9KCZMTXkTXA0vVbcVlZpO6NeqTkRmn5Kyjr_4IO5fNcgQPP6f-9Z34Dv-17AibAPVnvCWBx-Qe8TfI1N2IINmvmgT4pEPaFUtlv1jes6OxFaVnTyN41-d8GsX7e_RpDy3iibkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5cba04d5.mp4?token=XjngzR-jPQylfLeQezTQ8oI-mgB8rokDTEgqYzJHcuXnujHdxTF5Aqcs3cGjTcrTXgU9etE3AESefvhV85ypX0kfAQNIrDhsoe-NizAMJk79Vixf2qNYF2hi5gRa4KrRg3by8b_h3e3_kRsllKlu5UO2r3yHTuu0A0q-7sC-MIrjNHffGKWrYWmn8xW6WUwpRVp_LoMsJexOm6b9KCZMTXkTXA0vVbcVlZpO6NeqTkRmn5Kyjr_4IO5fNcgQPP6f-9Z34Dv-17AibAPVnvCWBx-Qe8TfI1N2IINmvmgT4pEPaFUtlv1jes6OxFaVnTyN41-d8GsX7e_RpDy3iibkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدم‌های آخر سفر اربعینی از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/454208" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f93f35ea0.mp4?token=ZI_xQfRqn3pQC0ebvGtxuQrdn7tG40lvQudr7_kRNlfPOllCdDduUNt67IQ3mB56e6ISm6d0Uz3dm8V4oUB1LmX4FU8CRF2BBGF0xliuVjLsiuWEcxuM5ojjBrrgJXhxE2znxYK79RM4XzujFOcYsuUpJ8j7775s--MVuUmAj6Gi96JuTTPJvW8sQgiMjawhMNBu_AyHwdp37i5e1HDwjol1SXciKirf-y3N55Embyg7aKABqZs65byUSh-aA6kIjT8bQ24vbkg2LtmqwDb1qwDGOtR9m5BNuCMJdNwmgzVI4wAEsQkfw5gFdjhwdN0F-8VQOFWHpWc5QPGIGe1BRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f93f35ea0.mp4?token=ZI_xQfRqn3pQC0ebvGtxuQrdn7tG40lvQudr7_kRNlfPOllCdDduUNt67IQ3mB56e6ISm6d0Uz3dm8V4oUB1LmX4FU8CRF2BBGF0xliuVjLsiuWEcxuM5ojjBrrgJXhxE2znxYK79RM4XzujFOcYsuUpJ8j7775s--MVuUmAj6Gi96JuTTPJvW8sQgiMjawhMNBu_AyHwdp37i5e1HDwjol1SXciKirf-y3N55Embyg7aKABqZs65byUSh-aA6kIjT8bQ24vbkg2LtmqwDb1qwDGOtR9m5BNuCMJdNwmgzVI4wAEsQkfw5gFdjhwdN0F-8VQOFWHpWc5QPGIGe1BRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان بجنورد در تابستان بارانی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/454207" target="_blank">📅 16:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
وقتی گنبد امام حسین(ع) را دیدید یاد چه کسی افتادید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/454206" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iesOatCY7QNeEh0F49wW9pybBRAWka77ikCdKOMyn2OAte9sE8XY-M_d833ZoIh8h4jBdTYjwDWe6xCoqNed1ji0TWnOW2Heu7HJVP9gkGCX91Z8OKB619rAOyE1oXk2hpxX3IMqLC5iMdisqFh2NoczDze9WOYnMGr0RmuyNljPHflMe6o-sApraMFq-QDIDsXinqaI0mT_XI83fTvt952RaY2H32yU22xExM6UNzOissGcPIdqQI_VvwwYiut9eohRb93E4rUhynJWh0y1LXVHAM8qLyZkeh06hPhonjtmdw5Zx0VYdgap4aYLQ_sTICT0WBZppG4ZlTXIP5gmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای زدوبند رئیس فیفا با ترامپ
🔹
اینفانتینو درحالی مدعی بود هیچ منفعتی از طرح فروش حقوق تجاری جام جهانی ندارد که براساس افشاگری نشریۀ تایمز، در صورت اجرای این قرارداد، سالانه بیش از ۳۰ میلیون یورو حقوق دریافت می‌کرد و علاوه‌بر آن، مشمول پاداش‌های مالی نیز…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454205" target="_blank">📅 16:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌ قم چهارشنبه تعطیل شد
🔹
معاون منابع استانداری قم: با توجه به تصمیم کارگروه مدیریت بهینه مصرف انرژی استان، ادارات و بانک‌های استان قم چهارشنبه ۱۴ مرداد تعطیل است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454204" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=FvMDCVRsLGYCKhBYAXPFGkhXHVJahSU3N_snjEdR7PmEXY6Gd3LvogN9NxlzG7nDnc_nCGF87K0Lo-onhW_aVtnnBGtvWRJiIRAixkeWxjyyPHqUoYuQ0Vy2fV24r37-aEPfo1PxIHdRcJgi3VytI7vBdUNJjorMGGXmhwLeLSPHCkTn4LgYPY7D2hsISi18dpx-79VPuf63U5CYXVVptLbBt0epes4Yr0YWLUqnprb62-JgDlsuTasAYPsAIGb_XOz_3BMN2IDtSaz0_XJpNluu5FfQQNAmg2DUE67RcNEebwPCo3sfeTxrG6qmMUMB2jsQVISdKX8cp_yMIhb5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=FvMDCVRsLGYCKhBYAXPFGkhXHVJahSU3N_snjEdR7PmEXY6Gd3LvogN9NxlzG7nDnc_nCGF87K0Lo-onhW_aVtnnBGtvWRJiIRAixkeWxjyyPHqUoYuQ0Vy2fV24r37-aEPfo1PxIHdRcJgi3VytI7vBdUNJjorMGGXmhwLeLSPHCkTn4LgYPY7D2hsISi18dpx-79VPuf63U5CYXVVptLbBt0epes4Yr0YWLUqnprb62-JgDlsuTasAYPsAIGb_XOz_3BMN2IDtSaz0_XJpNluu5FfQQNAmg2DUE67RcNEebwPCo3sfeTxrG6qmMUMB2jsQVISdKX8cp_yMIhb5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام شهاب مرادی در مستند راویان پرچم‌های سرخ: ایستادگی مقابل ظلم و دفاع از عزت مسلمانان، مسیر یاران امام حسین(ع) است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454203" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454202">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trX0JPRoxDCMKgqZ-YpQ0bxa2fDkxlCRW99Ddb7fYfqiQMYzbBnLd4HiJe3t7fI78GCJCOOP-11Qp1ffR1pp7A7JEya3ae1EZqY7CczDPdwhfEiXwJ_UKxvg15KyRFWI8UaqQMUVE_BYzmyIDDWCfKlGjulpewboidxfWL_So0AlBCZMpTxHy_ng9t9s_t7oVmdffBbfHEoTcwqcll53x9t8QBO-Kk7qWOQ62-1RJMgDAjdLJZu-NEpDAB9_mq6nEz75PuZkNXvpMGr2UVgPNiiBQR0A3HaZEOBrVS3ochcwQK3Ul8NO9YarBf1o7lE3vihoNI3xr1aVqLKyD50s2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: در آستانۀ سومین سال ریاست‌جمهوری، گفت‌وگوی پزشکیان با مردم به‌زودی پخش خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454202" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454201">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhpeHRcbTvIP-9Yp9iGtG3wC45BBUm8nPv0aky_tcG3v19dqL0CqX_irL_gWSdniJNsfU69qwSSdKYPg0-qXJRxZeGKFnbsc9nhvZhSSHDzimYM-Y9aJSJzryID5F_R4KbSC7-8WnLswr9cgSyTg09hM0XkSYQYRxjC-ZyJ_u6w76wx8O8njnJPfGBfe4p7-jqNmgMAzmx7Ti2hw6EOMLE5_gRYrpoiQO59xD89vBVWWoTzLbFPLUKqV9oTCBgFKuIL6GtGxnGS6SydbP6wkiLttyDGOXuDxmrREtCzcS2DODsjHi19HHom6LpWC_hgzpypYgeElU1etHEOEH62GpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت رسمی مرز چیلات از ۲۸ صفر آغاز می‌شود
🔹
مهر رسمی گذرنامه مرز چیلات دهلران امروز باحضور سخنگوی دولت رونمایی شد.
🔹
سخنگوی دولت: امیدواریم زائران بتوانند از بیست‌وهشتم ماه صفر از مرز چیلات رفت‌وآمد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454201" target="_blank">📅 15:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454200">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKk_RW0JCtBoGUhGi-Hjci9O7aEa4wlbpIjl_WWCx2qrYCdAv_WYJiYXfYgSLjkAVr_sMKfQKTzLfo5zTcUWQqjqxoGJMN3wyfAwO9oRx2_Xcng-9rFLo40lH7Xf3fcGDxaUWChvhVsPOUmUc0C3fefJyWfBOv6FF5Ktqh8jfQ_8uHCMt6JphCKloRYVC4ffftYqx0UIKp480javZPeR-9j1F4SiIH7YGSkp5oUZSLwaWjUH4tJg9vD6ICEj2BvNFjZgSYB1hutkil1Wnk5TezK0t1dpcb8uq9EUC2w39IKzdQiPGnCrNiJ7rzRmSHpU7igLtb1zh65Y5Iw3Llu8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال قهرمان ملی مبارزه با استبداد پهلوی به تلویزیون می‌رسد
🔹
«پخش سریال حماسهٔ زاگرس با محوریت شیرعلی‌مردان‌خان احتمالاً به سال آینده موکول شود». این را مهدی نقویان، رئیس مرکز سیمافیلم در گفت‌وگویی با فارس بیان کرد.
🔹
سریال «حماسهٔ زاگرس» با کارگردانی حسن آخوندپور از جمله سریال‌های الف ویژهٔ تلویزیون با محوریت مبارزات شیرعلی‌مردان‌خان بختیاری است که نقش اصلی آن را رحیم نوروزی ایفا می‌کند.
🔹
به‌گفتهٔ نقویان، این سریال در حال فیلمبرداری است و تا فیلمبرداری آن تا بهمن طول خواهد کشید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454200" target="_blank">📅 15:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454199">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbu4lGF0o4CiSaM-SEfUx8fKTXXv1cgzyIqT8-0WqMCOQQffdodYxylu5q8uYjiu0VQo88EfrIdl68cNTM1TPgS0FKexAn7YmwUhrCb7onzFzLqDiLUm3vzRmD7CVTa7YQXrO_gJK0pUmGh0_kpcL_EREOlnyvi3YaPo-H8Tesm2OyBXzvSHB3tcNyLjsldc2MQ-4iuY-UqZ7VXorpvUgphp4lF44u70AAnQbssLESJDnjWLCycmU6EnA-aIOlGO4wvk8-xwsGf4ocuf-DywGJZIhYCEpR6V1ybPtEi3vz6IFqtomexT89aC6dcqg2HjelY8PbMH_XdprrGb4uapfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز گوشت را در آمریکا گران کرد
🔹
مارک وارنر نمایندۀ ایالت ویرجینیا در مجلس سنای آمریکا می‌گوید: «قیمت گوشت گاو در آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافت».
🔹
اختلال در حمل‌ونقل دریایی از طریق تنگه هرمز دلیل اصلی رشد قیمت از سوی کارشناسان این…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454199" target="_blank">📅 15:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454198">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌ کرمانشاه چهارشنبه تعطیل شد
🔹
استانداری کرمانشاه: با تصمیم کارگروه مدیریت مصرف انرژی استان، ادارات و دستگاه‌های اجرایی دولتی، بانک‌ها به‌جز شعب کشیک، بیمه‌ها و نهادهای عمومی غیردولتی روز چهارشنبه ۱۴ مرداد ۱۴۰۵ تعطیل خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454198" target="_blank">📅 14:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19878aefa0.mp4?token=XEdgZ7882-NnyxbBg7daczgObH6eUcsxoST3xdeTJZ7skBhtQFVR4jF9_VJD9tROyDqcHxCh7-UQciVVhoRk8_F26yvXM-eNRmRjnZ-JiRDemOG3T8n8zMnIZXt0TpwUmQ25QICuvwFbeCyhIHrzUQwGw5XwBaiuMOMoyzDfSLkY7axuWBO3tlKzNTsFuL5yVFjCHf7pgy5Ksd9O16h2y2iYd4bZ9vd9HuVKpZyFuVfx3wkTRy-flvHwz3dIBMkFNKCfF4mOeuS3wKE9XwzNXk-ikFgaT5yuZ8Zp9Hz5qPwEGxNb5UMypzfBCngjVcXt-FJg6Oa-j4nj-V0owICsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19878aefa0.mp4?token=XEdgZ7882-NnyxbBg7daczgObH6eUcsxoST3xdeTJZ7skBhtQFVR4jF9_VJD9tROyDqcHxCh7-UQciVVhoRk8_F26yvXM-eNRmRjnZ-JiRDemOG3T8n8zMnIZXt0TpwUmQ25QICuvwFbeCyhIHrzUQwGw5XwBaiuMOMoyzDfSLkY7axuWBO3tlKzNTsFuL5yVFjCHf7pgy5Ksd9O16h2y2iYd4bZ9vd9HuVKpZyFuVfx3wkTRy-flvHwz3dIBMkFNKCfF4mOeuS3wKE9XwzNXk-ikFgaT5yuZ8Zp9Hz5qPwEGxNb5UMypzfBCngjVcXt-FJg6Oa-j4nj-V0owICsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات امید بهزاد و پوریا صفوت عاملان رژیم صهیونیستی که صبح امروز اعدام شدند  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454197" target="_blank">📅 14:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciaKxRvdNKhYgAgWfJ4_uGhSmzqbECryTy4yCI5tkJQiSx_UWQjHggFbLJgdVuUhFd9l3dtuF7d_8tqbWQcA4ei3-Sf__5T9oxIvyKneMl5lBnq344FFSAV86An139OB7Y_GbrbvYWBbFBlmDZkzVsCGZg7s9VRTp6hYEx9qKSsHmxAKTjJkDPlyGXTTHizcxwl-HixjQ2ZaKDR2Ggc3YN9Lm2qMy4ZXxHrreWQp8-bxooeVIRVW_y7NrnIRoHUkTUUmpt4rnIhodmD6Hz5DF81viwZzDlH9XsC7S4EjRbXj4vtKiPKGLJIjMq9Xq7bX1H2GIHZxvj9yxIHYGbpxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فردوسی‌پور را باز کنید
🔹
«من را در صداوسیما ناجوانمردانه کنار گذاشتند. از چه می‌ترسید که اجازه نمی‌دهید کار کنم؟ من بله‌قربان‌گو نمی‌شوم، حتی اگر بخواهید مرا بازداشت کنید.» این جملات را عادل فردوسی‌پور پس از بسته‌شدن وبگاه «فوتبال ۳۶۰» در برنامهٔ ویژهٔ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454195" target="_blank">📅 14:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454194">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4270bcb2cd.mp4?token=urCcf2AWiPsIOVyBIV2W9CYi7prte8MtFshXRtP-9ZtJrFMi2A5ecHmdvIPZUxzX9mV9uKNV8_2vnMWSZmykrNsaOQyvIDKmSpdDMSaXydpF1U5qyM_KxL7BePfiaOp-xm30_mO8GLFomAYuirUtCtRIovA8Rqzmg01_4bdrmk-fQINmXQ9D_EbTA_HazS5NFP1MTR3YkucJVQkYg4w-tVqwXoK4B6J6z0KBegkX6DNcluP5hwtzlBo3py7QDDnBXARm-vtKrTGz3vEn9mw6ZX7aLxAIEJgfe9LUmncMalAJIJ4TGlLFLvqkUDgckNzPLEGmfXsW2sgTLQODA0jKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4270bcb2cd.mp4?token=urCcf2AWiPsIOVyBIV2W9CYi7prte8MtFshXRtP-9ZtJrFMi2A5ecHmdvIPZUxzX9mV9uKNV8_2vnMWSZmykrNsaOQyvIDKmSpdDMSaXydpF1U5qyM_KxL7BePfiaOp-xm30_mO8GLFomAYuirUtCtRIovA8Rqzmg01_4bdrmk-fQINmXQ9D_EbTA_HazS5NFP1MTR3YkucJVQkYg4w-tVqwXoK4B6J6z0KBegkX6DNcluP5hwtzlBo3py7QDDnBXARm-vtKrTGz3vEn9mw6ZX7aLxAIEJgfe9LUmncMalAJIJ4TGlLFLvqkUDgckNzPLEGmfXsW2sgTLQODA0jKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: تا الان ۳ میلیون و ۲۶۰ هزار زائر از کشور خارج شده‌اند
🔹
۲ میلیون و ۲۰۰ هزار زائر اربعین به کشور بازگشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454194" target="_blank">📅 14:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454193">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b99256aa.mp4?token=GP86JqzhpH0MyRyt1iQqs_zCpj5TMjiOseUvg3fOchqI9ArFTuanIZV5JbSQUCNd3oZWp4bBdf5o6Jo-lLORvb1_Ag2vPUsY5V6DA0dzc-UpmQ7uAir4z_p-z0UcST8jHGsZzIjG6yhVdbPlHrgdwm9VmVcMNJBOsAfyfoXMBGP0BarXJPydPpXtn8G7HBGxcjL9Xy5tQqURB07V23QpuVuS4Kq3p-0tOkfVkZdE2PCbtsALIDebYz8JSccg1Ext8faQd7d36hBLY4-QubVma--qJQObBXYAr-JPT8xmmLQB3rPyflfoVdL1spc3h0WAOrqm8GrtqSlDHi6PLMiJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b99256aa.mp4?token=GP86JqzhpH0MyRyt1iQqs_zCpj5TMjiOseUvg3fOchqI9ArFTuanIZV5JbSQUCNd3oZWp4bBdf5o6Jo-lLORvb1_Ag2vPUsY5V6DA0dzc-UpmQ7uAir4z_p-z0UcST8jHGsZzIjG6yhVdbPlHrgdwm9VmVcMNJBOsAfyfoXMBGP0BarXJPydPpXtn8G7HBGxcjL9Xy5tQqURB07V23QpuVuS4Kq3p-0tOkfVkZdE2PCbtsALIDebYz8JSccg1Ext8faQd7d36hBLY4-QubVma--qJQObBXYAr-JPT8xmmLQB3rPyflfoVdL1spc3h0WAOrqm8GrtqSlDHi6PLMiJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز عراقچی راهی سفر اربعین است</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454193" target="_blank">📅 14:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454192">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur-fELOY2FZOjdiWhOcLHqegFrlBfnYdXVCn_AVIgjAqEJ_lxmkemhMI8KRFCL5600gFN0pf5lPxEsEjTIun7r6obCun7Z0o4y-AgIpJt_4EJRyKzUd6AA-72uTT9VrhcC1kY6eYhy60XBf6yFXWVPM4-xQ8qBbEggeVQbacmNLkc3UJX7PszIqFHXyyopEuX20N76wETl5iLI7pXgHksMT7_AogbqDAXjn9tv95QPGJF24zhMMH4fLfgZZxVdDYh_Fknm_nphNYKflmcSoIdACmDhsQ50XzGibuhA3BuyzBmvkrUrcugCT2yYn4xzXl4gooGAJblSmWQYWmHhetNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت مذاکره با آمریکای ترامپ بن‌بست است
🔹
نگاه دولت فعلی آمریکا به مذاکره با ایران نه یک نگاه تاکتیکی و نه حتی صرفا راهبردی، بلکه شامل عناصر کاملا ایدئولوژیک است که با نگاهی به ماهیت آن، می‌توان نتیجه هر مذاکره‌ای را از پیش دانست.
🔗
شرح کامل این یادداشت را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454192" target="_blank">📅 14:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454191">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba17c5d31.mp4?token=ir1zNN4T4ZLjrbJ9UZZqEYfGKAPXkUTqK1o2qv3NyD53Iv926j5ULKCZVTFI9P7W-Bjh2NSeD09xR_ZMIkLfs4iGVT378uokkajTrGzukllfkY9H8qqrm6RQFopq1qcWKkwTJ7NyFbwkb8er3lEdP8lJ9t-kF_HRuFGGs2lbZ10psyaZ-VWbx2D0QPG5PRv8R4eqhB66tMt6-mQ6Ov57jQ0UTEuUecdo5ULjrdlSnpDfzt5j-Eqd3AITcwPaqxjWZOXWUbIre4fPGeg29Jmz-ngRCBSMxs36jY9TGi_kW5RYMLACv8q7fl1USoesd302AfUz1Y8g30WSzgWW5U4jKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba17c5d31.mp4?token=ir1zNN4T4ZLjrbJ9UZZqEYfGKAPXkUTqK1o2qv3NyD53Iv926j5ULKCZVTFI9P7W-Bjh2NSeD09xR_ZMIkLfs4iGVT378uokkajTrGzukllfkY9H8qqrm6RQFopq1qcWKkwTJ7NyFbwkb8er3lEdP8lJ9t-kF_HRuFGGs2lbZ10psyaZ-VWbx2D0QPG5PRv8R4eqhB66tMt6-mQ6Ov57jQ0UTEuUecdo5ULjrdlSnpDfzt5j-Eqd3AITcwPaqxjWZOXWUbIre4fPGeg29Jmz-ngRCBSMxs36jY9TGi_kW5RYMLACv8q7fl1USoesd302AfUz1Y8g30WSzgWW5U4jKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: طرح پزشک‌خانواده از این هفته در روستاها اجرا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454191" target="_blank">📅 14:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNf30l0NgGlxoHsfBFlCcPj7mKNiaPsjb0r9RO0AzqmQ1mjiWeXe3VuOusHH2MgaxirBb8K47cMXmVRvX80oCSLwyQPcu3CceI00F86fdKI8iZ6RqmOvCPwBmbLFMA5yObpvNYSRwqYo39ngXY74CRnHbAhXpQOfZf278pL3wTmpII0I2xpN3ITasMHh-w4cxxRePBlQmZd_eazUOzb0bBy5-h8_WtUsu_MK54VdyWySyAOMCG_kC1n7NJf3lsSty8Ffqaa8Fz68Bx79mi0X6MTLmuTNUNLZipBAWbYkXW0ghefnfm_vp3vt5wYB63zTzgc1gONxeiA62m1a4pLG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکورت هوایی آمریکا در تنگۀ هرمز
🔹
پایش داده‌های ناوبری هوایی نشان می‌دهد که هواپیماهای پشتیبانی نظامی آمریکا در خلیج‌فارس فعال شده‌اند.
🔹
پیش از این هم چنین پشتیبانی‌های هوایی هر زمان که نیروی دریایی آمریکا تصمیم داشت نظم ایرانی تنگه هرمز را بر هم بزند، دیده شده بود.
🔹
هنوز کشتی حامل گاز قطر که جمعه‌شب می‌خواست با اسکورت آمریکا از تنگۀ هرمز عبور کند، در بخش جنوبی این آبراه زمین‌گیر است.
🔹
براساس تصاویر ماهواره‌ای، هواپیمای هشدار زودهنگام و کنترل هوابرد آمریکا از ساعات اولیه امروز فعال شده و به‌سمت تنگۀ هرمز در حرکت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454190" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
