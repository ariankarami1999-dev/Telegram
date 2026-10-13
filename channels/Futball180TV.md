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
<img src="https://cdn5.telesco.pe/file/gykUWV9XQUAdp5Fx016ugoCslTVVqdkFyOXxBLquj_Viia63rMxXvTnjrMv9ljaeEOmcuJUn8JbWb9ZfFO_YTFiD5q6TQocY4hy5QHS7x3srDT_tDN3Mh_Vv4wWh2KY3ev0HKy06nJuQ3f-93v4vMaX7h1Qb67crqMVNMpBduw8UzFMm0UDOzI8Nn8juyXGB797GlFwlkABSk0xHpWxXdsP9JwfwVPBK6YC9nLMHkoUOFc3xJGzcH1ZMshbCJMsm1VacUf0R5qDT4hNaksgXUPYdszyi-Usddt9gbG_4kDF_StvhSibv6DNP48i6ToN5Dzq_W28j7yzOec6UXpQdDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 383K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-108553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ac4b09ba.mp4?token=iDniCI2O8sGForq3Bin-R-nafcabvTxBy5Y4RSuw64_YtvoSqzt225135ktt1eIvt34_B3G74VRX7SFzL-_GQex7tSvlbRSlFOBbY1o6DmCKNz4NYtOkSczisO16HIEOm_V3uoB_2BPH2AzOgK6ZQOuRHMNk9pXxYdquycn2HJeTDRIec-c_VI9vDqP5B1DDJ1XjpxIwPxPdnDwWOes_npev6pO0xWNqQ6sQuJShr2orfKkLo8t1hNbO6z0WajTPVEPzXrgoJWuz_NXXjF0EV98z0-mob9yo1f3q0nwiKL5HNffGjG9Vsgm9_jsmE7vlSV9iDhHHxjbie9mvHSG4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ac4b09ba.mp4?token=iDniCI2O8sGForq3Bin-R-nafcabvTxBy5Y4RSuw64_YtvoSqzt225135ktt1eIvt34_B3G74VRX7SFzL-_GQex7tSvlbRSlFOBbY1o6DmCKNz4NYtOkSczisO16HIEOm_V3uoB_2BPH2AzOgK6ZQOuRHMNk9pXxYdquycn2HJeTDRIec-c_VI9vDqP5B1DDJ1XjpxIwPxPdnDwWOes_npev6pO0xWNqQ6sQuJShr2orfKkLo8t1hNbO6z0WajTPVEPzXrgoJWuz_NXXjF0EV98z0-mob9yo1f3q0nwiKL5HNffGjG9Vsgm9_jsmE7vlSV9iDhHHxjbie9mvHSG4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله مجری صداوسیما به سرپرست تراکتور تبریز: خداداد عزیزی توروخدا بس کن!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/Futball180TV/108553" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xdsc5nKQEnzlEKdwfqVOtpURPe7Mq68ihfiyIvW2XLYQ2T6k4P1rFM-zbW1-G4MWgaIs37H8x0rpuUjCdyQmqZPqc9RW4BQeN31uANvuZLf6CyK_yVG5wwjrOYAYw5ZjEgv9TzIGqpF9MY8kx3kFdoqBSui8sxUUa3Zb746niicDWXyZKSOfsXirA4Hp5AY664YuYvpkYUaTi09WTxHlo0MT2gFusIsll94O9BunYykiczmiLtrCMlpwCLUv7z2CPJAp-V-siGZ07MZknAy9g0qfA9sZsDzhHqrNVleaddbXJbrJlGXjoZfCpQgBz4mv5Mg8p0DUa8_vlminZqGhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دانیال‌ایری مدافع پرسپولیس پس از طی کردن دوران مصدومیت به تمرینات این تیم بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/108552" target="_blank">📅 15:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eaea7cdd.mp4?token=UzRXy01dv1srVA9Ux2BvjEEZEgiYD3cPE2IdUBZnM_OKh49HI0dQhGEj4P8HN99VdAMgxif5rFbvPBMBDV1HlI5re_6GPEt2bz1LSzrvBJWiOTliwlsvfQVXr290dFNndrzrTTM_eo3awOpSLn6gLoivDO0h7vlqZCSNISyQ908C68greGUyBlXM8-N84sd3sRAFYHsOJrT61xYNjPVPWxwVSNk_fD0x9NET56PJmh5YAV1B4rMeqj9lWnA0oqm0yH8bc8uF9q5QIla_WgT55acHV1HKCKHeetEazywPwFWQaRtpUODKZvOO55XLuKfN-PhxyDV271D5zc_uJiPyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eaea7cdd.mp4?token=UzRXy01dv1srVA9Ux2BvjEEZEgiYD3cPE2IdUBZnM_OKh49HI0dQhGEj4P8HN99VdAMgxif5rFbvPBMBDV1HlI5re_6GPEt2bz1LSzrvBJWiOTliwlsvfQVXr290dFNndrzrTTM_eo3awOpSLn6gLoivDO0h7vlqZCSNISyQ908C68greGUyBlXM8-N84sd3sRAFYHsOJrT61xYNjPVPWxwVSNk_fD0x9NET56PJmh5YAV1B4rMeqj9lWnA0oqm0yH8bc8uF9q5QIla_WgT55acHV1HKCKHeetEazywPwFWQaRtpUODKZvOO55XLuKfN-PhxyDV271D5zc_uJiPyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سمی‌ترین ویدیو از حرکت زشت وینیسیوس
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/108551" target="_blank">📅 15:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea75d776.mp4?token=kNXlf1zxAN-Z3aaE76Xw6qIXnu2HuFPDZCjqCGz1_97345BIot1fCavbBwItZJCkylbMSJNf1oyDc2hurtGNi00ab05PBLoI_Tksq23W-OPNpCma86SUN2zci6K4PTZL9Kg7qNwdWoG2-YA9i-Gafm6Spy_RArRYqOHQCmbPS7e75cJ3Tfggya4a3H2GfdC32DSemdimM6XpMLA-kiw5ergRX4h8FoHEd4uv4LuuDr5yGcNxjn6JPqCoefb_TIgnBtVLjiFDaWdt3uov-awAKqp96lsvNixkkEfWUO8HB7D5967GJLlTDbIaUKq284veO_V205kQDBS19Z8ur7JWpEZMpN1XeZz4PWBelQJTs3X2IQxo4xw9Y8Cd7QA6lDLqkFjoBJJEM1XhcRp6V-x0jsG5TXa9fcMkx0uRNy3KfLrWT6ZvAj29L2cbE1I9OoT4VfsOsxjVbTe5BGz3tXNIyeFlmfMSMSxSpFJDNt6v5zURIS2j9KZSjoypxGhZFyvRX2LTQsMvsAbfhvdf4Hud0Dd-g2uJxIz7hHmgk8xdsRS1I7cPeBRdaDDyKmVgNfeGhUf2uUx0pBJvNI2oHl9HF_DHQ_TIUDzBP1PJ1z44oypxm7e1PGz7KiYm7bte_8wEcfiMmz0p352THO7cY7PUV264kzMu15RSEuQ0oJRB2oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea75d776.mp4?token=kNXlf1zxAN-Z3aaE76Xw6qIXnu2HuFPDZCjqCGz1_97345BIot1fCavbBwItZJCkylbMSJNf1oyDc2hurtGNi00ab05PBLoI_Tksq23W-OPNpCma86SUN2zci6K4PTZL9Kg7qNwdWoG2-YA9i-Gafm6Spy_RArRYqOHQCmbPS7e75cJ3Tfggya4a3H2GfdC32DSemdimM6XpMLA-kiw5ergRX4h8FoHEd4uv4LuuDr5yGcNxjn6JPqCoefb_TIgnBtVLjiFDaWdt3uov-awAKqp96lsvNixkkEfWUO8HB7D5967GJLlTDbIaUKq284veO_V205kQDBS19Z8ur7JWpEZMpN1XeZz4PWBelQJTs3X2IQxo4xw9Y8Cd7QA6lDLqkFjoBJJEM1XhcRp6V-x0jsG5TXa9fcMkx0uRNy3KfLrWT6ZvAj29L2cbE1I9OoT4VfsOsxjVbTe5BGz3tXNIyeFlmfMSMSxSpFJDNt6v5zURIS2j9KZSjoypxGhZFyvRX2LTQsMvsAbfhvdf4Hud0Dd-g2uJxIz7hHmgk8xdsRS1I7cPeBRdaDDyKmVgNfeGhUf2uUx0pBJvNI2oHl9HF_DHQ_TIUDzBP1PJ1z44oypxm7e1PGz7KiYm7bte_8wEcfiMmz0p352THO7cY7PUV264kzMu15RSEuQ0oJRB2oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی رامین‌رضاییان خودش رو چشم میزنه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/108550" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Gb-X875jYknWo6WIrsCdInBb-IgxZVEtyw7bPeyk98PfmZ6U7K2wagUv7CiAbM00DUqoEene4MbwNOqtjT4P3_Ov06lq16I3ZGvnaxKWeuknvS38ic7avObkxhep--CYhQF6L1yFV6DaKK5GLOVfaSALi3z1DPlpo1cPW1G6BF3lFX0MroXqbSwN7pVRUBbBGkAv1y_OgcDEQiVAzZKVhPdde--nXY0itJ8-KhomfLWQ7G67C413aEsBHFqSCQZsZ7qIhqlt3Sr3U6hbxZvPNC7O5MjB95PEz_iefGRSHmWq_abNb8hlvUU7QYSdK_EnNdK_GxDE7wzSXfMOXwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
بهترین خطوط حمله این‌فصل فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/108549" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZu9vW41i-ZhJB5JjI84u1JWXJ18MhgK-cJ9E1L-K1e0KNr-ah6q06RFp3D7xx-YZhHDafgpZym0pfScd0PYSEpBZaJoKyRcLQ-jS2r1nLsJI9cVJ40IOuIfwi9aRHbrotPt3BjUaP3VA03IXEDsi6SdtXZvxtXRS2F0kqG3vdW01z_DYuPSuFlGT-IqkUDX4cgFfohcrZLN_m12ro_JBkvqNdcn_vlKevnLBtG8uqAPoKD0FRVPkCRLpSowbLxgLr1QjitarJzRn4DdPAC2VkDuWO7x2kO9jGgwNp41iQNJ1aLymXO3S2cKJwDFk-M9i5e3D21mxeNLGjFpiSPn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
محبوب‌ترین رقبای ارلینگ‌هالند در‌پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/108548" target="_blank">📅 14:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbaca5bde.mp4?token=HRSSQN2lw_qDato1vACxU9s_ShnDky8y3lajsl7tKnmc0e2GWWNpLXv1CM0oM7MdeSUDDTRRowQ1Sig3Mwv9dUodxo275u1N2LasGo_JQKaE-pj4064x7KX0cgglI5S_fu9C1VOGLyYU_Nqy5rk7k_HjDfwbE_uJNJ10gk4sHfFxx5Izeq6z6tQNV7ZweU3YrVIc89f-xv1rLwuWRXHRCWAa3tq1IU4fjo7jYaj4c1kFMO1wCDW-K62J_M5AjHu0LNNfmJqyChYV59nGg5MSf6fXdKX3Ck0l-Gt_Fdwmz8e7J1vzcAUvYZ_pvfxUzSKgG1kI2M-IUo-krIRbj0GzaHfB6ahdFXMy9aeUlUkzfRKpt3lpaYzmXZqSIljQpCqJNGixXRd3wAwvrv3SaJ28LqM-kOsUbQ5fYhqLWIr89eqBXzfH06d4pv10_ClSwkLaTsP6_6cTGptKIKP0p6Erql3sDmKFeXhrB_NzUhGmgFwFkJFuEE3iU6v5MPtuOacruXbFY007ZF21hpCg6z27B-WU9guWqUV75fxCrzgJkYoHvZyLr63YYTWGlTYm-9WvZd-EoyX59ET59UZ9YFgvPuHkl3OpXLUvvJjYB-z0Frwb1BTT-L3s3wQeqE7n0SF8aXujXEGPcQK2k2RkQIne8L1zsAl7pHg3dCWWpahL6cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbaca5bde.mp4?token=HRSSQN2lw_qDato1vACxU9s_ShnDky8y3lajsl7tKnmc0e2GWWNpLXv1CM0oM7MdeSUDDTRRowQ1Sig3Mwv9dUodxo275u1N2LasGo_JQKaE-pj4064x7KX0cgglI5S_fu9C1VOGLyYU_Nqy5rk7k_HjDfwbE_uJNJ10gk4sHfFxx5Izeq6z6tQNV7ZweU3YrVIc89f-xv1rLwuWRXHRCWAa3tq1IU4fjo7jYaj4c1kFMO1wCDW-K62J_M5AjHu0LNNfmJqyChYV59nGg5MSf6fXdKX3Ck0l-Gt_Fdwmz8e7J1vzcAUvYZ_pvfxUzSKgG1kI2M-IUo-krIRbj0GzaHfB6ahdFXMy9aeUlUkzfRKpt3lpaYzmXZqSIljQpCqJNGixXRd3wAwvrv3SaJ28LqM-kOsUbQ5fYhqLWIr89eqBXzfH06d4pv10_ClSwkLaTsP6_6cTGptKIKP0p6Erql3sDmKFeXhrB_NzUhGmgFwFkJFuEE3iU6v5MPtuOacruXbFY007ZF21hpCg6z27B-WU9guWqUV75fxCrzgJkYoHvZyLr63YYTWGlTYm-9WvZd-EoyX59ET59UZ9YFgvPuHkl3OpXLUvvJjYB-z0Frwb1BTT-L3s3wQeqE7n0SF8aXujXEGPcQK2k2RkQIne8L1zsAl7pHg3dCWWpahL6cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
دلتنگی همسر هادی‌نوروزی پس از فوت کاپیتان سابق و اسطوره‌ای پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/108547" target="_blank">📅 13:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81a66e7b1.mp4?token=Tl9wTT5DyKW-SkoABM4tX9g_nC3XppdwOenBMi2stD1Qs7xOsmLMbzG-8nTmIm76-jmkREaKw8a6UfpT4stbY-NH5fUg8k_m6GMHznb5Z828vZS6VyFw1lWjRFZjWZ_xZ3mD57aBa94vARKTJqtmVH9oroN7tTVWGOPIzsLTB_kP9wgBS2Fq-iOX1U5K1QbyMJQDYGXy2oW-RU_hVQGrQooEoPGWrOos-5g-uZ9TrYO06OabGqRitxe2wJko8tMqMfmhFxrW5g-bmQfW_207YJ91p8p-ALTWgEOXijrWGjy1XkQDQxoNdSWgNK9yU_40kvrm4oNdF54RvSE5ZWB7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81a66e7b1.mp4?token=Tl9wTT5DyKW-SkoABM4tX9g_nC3XppdwOenBMi2stD1Qs7xOsmLMbzG-8nTmIm76-jmkREaKw8a6UfpT4stbY-NH5fUg8k_m6GMHznb5Z828vZS6VyFw1lWjRFZjWZ_xZ3mD57aBa94vARKTJqtmVH9oroN7tTVWGOPIzsLTB_kP9wgBS2Fq-iOX1U5K1QbyMJQDYGXy2oW-RU_hVQGrQooEoPGWrOos-5g-uZ9TrYO06OabGqRitxe2wJko8tMqMfmhFxrW5g-bmQfW_207YJ91p8p-ALTWgEOXijrWGjy1XkQDQxoNdSWgNK9yU_40kvrm4oNdF54RvSE5ZWB7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
محتبی‌جباری اسطوره استقلال: «من با کلی مصدومیت بازی کردم، اون با یه مینیسک خداحافظی کرد!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108546" target="_blank">📅 13:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab7ed9c6a.mp4?token=SR5odQD2AOsDMjaXnbdta3oOUYHqMGPi72CqqpMNIJO2hSb7nvrrxQNPOLLZe8f9-kRAphc4h_P7P_nuhBzGLnmtIbZjqu8OsHUibtd1lFO4Yyg4G6fRaRzQbusFdN1lHkaFrpGlJb8S75dLSkZuBcqRO_gWBZXD0h1s7mThhtTpssK8taAYsIrKpwqfbCLHMYi3rcFoPp6bl0lYgno9EKHcYTzQs9hmnaj1s8WeqULVMX9F04_fMk18TIj93ua8AteCTyzLU89oOmNInwbAmQt0nvn_sJdJ6qMaaLMskEAdRfn7I1rplbKcz9oJZcpQM_8Qc1b50nTaKua1Dna5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab7ed9c6a.mp4?token=SR5odQD2AOsDMjaXnbdta3oOUYHqMGPi72CqqpMNIJO2hSb7nvrrxQNPOLLZe8f9-kRAphc4h_P7P_nuhBzGLnmtIbZjqu8OsHUibtd1lFO4Yyg4G6fRaRzQbusFdN1lHkaFrpGlJb8S75dLSkZuBcqRO_gWBZXD0h1s7mThhtTpssK8taAYsIrKpwqfbCLHMYi3rcFoPp6bl0lYgno9EKHcYTzQs9hmnaj1s8WeqULVMX9F04_fMk18TIj93ua8AteCTyzLU89oOmNInwbAmQt0nvn_sJdJ6qMaaLMskEAdRfn7I1rplbKcz9oJZcpQM_8Qc1b50nTaKua1Dna5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
جلال حسینی در گفت‌وگویی به استوری جنجالی علیرضا بیرانوند علیه علی دایی واکنش نشان داد و گفت: «وقتی استوری بیرانوند علیه علی دایی رو دیدم، خیلی تعجب کردم. به نظرم این‌جور رفتارها اصلاً درست نیست؛ علی دایی اسطوره فوتبال ایرانه و همه دنیا فوتبال ایران رو با اسم و افتخارات اون می‌شناسن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108545" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1646f8600.mp4?token=Z0WuEfS4Qa7wNrbrCLsEKaoia5T1qA89h3nPh5Ij-jbLciciAiye899n1-SwsOaeaHhIKK4w6EllBC-2ZQ03ybDSw9i3jVTjEyBUPRw7o08Gkm2fyPt8lB2EAaPDdoLIaQ-68f8y3wCn_TRp2Ui1Pp1A7c3zjPzgeOjAshbCtdXrRofwpMCWLoVOYylL139DaScdp7mfr3_4sXBGqlBaZ4sR5k6NsumhB4VyBlHPHOcLqbG7bghCth2SNddcvGvgohj-dwqf2-_PCPczfScdJC2h5g_tALKqo3XciKg5HTr9-dJWzZTppuNuncW9UjWfCu8SKMOgyuqC_6xSzz0M2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1646f8600.mp4?token=Z0WuEfS4Qa7wNrbrCLsEKaoia5T1qA89h3nPh5Ij-jbLciciAiye899n1-SwsOaeaHhIKK4w6EllBC-2ZQ03ybDSw9i3jVTjEyBUPRw7o08Gkm2fyPt8lB2EAaPDdoLIaQ-68f8y3wCn_TRp2Ui1Pp1A7c3zjPzgeOjAshbCtdXrRofwpMCWLoVOYylL139DaScdp7mfr3_4sXBGqlBaZ4sR5k6NsumhB4VyBlHPHOcLqbG7bghCth2SNddcvGvgohj-dwqf2-_PCPczfScdJC2h5g_tALKqo3XciKg5HTr9-dJWzZTppuNuncW9UjWfCu8SKMOgyuqC_6xSzz0M2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دلیل جالب تغییر عملکرد سامان‌فلاح در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108544" target="_blank">📅 12:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa0bb0abc.mp4?token=JY6iLZ_67YSEa5t4kSrNx2v_vzaCFQRHfl1TWX2P3eOHbEuIt3YCrXZUkxL7tksZ745y3nT1SV59kTuoiTY9paHFwp_8afyYlDkLlw83LI9cw9P2gPOcw4E2XcuZElnVQZT61Jt_XPSObzOwbtKXEmdhIMW91ZQkyMOsLak5lqN86jxFo1XeLQ4zHTLb4LC6eEYRTCxzL9qiksTNnCEPHTjhbAJnpOO2ls93B1_isRdu_VcIIpQ1K23KZIXHZLvJkPiZsJEuF9Y6yS2I6mWiMRnM_lreDo3u5yRZWA7le-3v1vuIQol4g8gfb4miUxMMriYwmUSUuaA2B8awMdg_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa0bb0abc.mp4?token=JY6iLZ_67YSEa5t4kSrNx2v_vzaCFQRHfl1TWX2P3eOHbEuIt3YCrXZUkxL7tksZ745y3nT1SV59kTuoiTY9paHFwp_8afyYlDkLlw83LI9cw9P2gPOcw4E2XcuZElnVQZT61Jt_XPSObzOwbtKXEmdhIMW91ZQkyMOsLak5lqN86jxFo1XeLQ4zHTLb4LC6eEYRTCxzL9qiksTNnCEPHTjhbAJnpOO2ls93B1_isRdu_VcIIpQ1K23KZIXHZLvJkPiZsJEuF9Y6yS2I6mWiMRnM_lreDo3u5yRZWA7le-3v1vuIQol4g8gfb4miUxMMriYwmUSUuaA2B8awMdg_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
بانوی استقلالی پس از برتری مقابل الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108543" target="_blank">📅 11:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a065c7f48a.mp4?token=oz1Xx1bDL0RpCIorYQj4GVZ7nn-dCk2DLCkcWKs3gO9H3BBUbWs6bjmMrhhKsbSPa7Ldgyh0qbzILqi085OsBFNVOjfvLAScycUeL-NQB-aniq5DJ9jG8-hJmvVvfjXkMimeTTN5StQeJt2L9A-r6Gpfwyec9AKPS_hXUq3sJsCTKw_drYbLoZMmkw1embTVyOGe4Rc54aT5FfSYj0HiPyI3kgWQzBTcXqVHJIMu40YDJHdyAC8H8uEc15FuSQiAvIAE_0uX0UaSWXN8P_aK39aLcVrpn-bUC_0dpULBaOZU7T_kcO67CM2Y2hq3SKGeGPI1lF9XCiBfI_tgorxpIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a065c7f48a.mp4?token=oz1Xx1bDL0RpCIorYQj4GVZ7nn-dCk2DLCkcWKs3gO9H3BBUbWs6bjmMrhhKsbSPa7Ldgyh0qbzILqi085OsBFNVOjfvLAScycUeL-NQB-aniq5DJ9jG8-hJmvVvfjXkMimeTTN5StQeJt2L9A-r6Gpfwyec9AKPS_hXUq3sJsCTKw_drYbLoZMmkw1embTVyOGe4Rc54aT5FfSYj0HiPyI3kgWQzBTcXqVHJIMu40YDJHdyAC8H8uEc15FuSQiAvIAE_0uX0UaSWXN8P_aK39aLcVrpn-bUC_0dpULBaOZU7T_kcO67CM2Y2hq3SKGeGPI1lF9XCiBfI_tgorxpIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
واکنش‌جلال حسینی به درخواست بیرانوند برای رفتن به استقلال
: بازیکنانی که از پرسپولیس به استقلال می‌رن یا از استقلال به پرسپولیس میرن ممکنه بعد از پایان دوران فوتبالشون  خودشون یا خانواده شون با آسیب‌های جدی مواجه بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108542" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108541" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108541" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaDZC6mNc0n3abdKqg5SlKKICvK_ErHE4J2eO9dxW9TueaepQ1LgSlGrTuCYaU4VRUwAw2zM6vz9GxHSGBogrpGRMWsXA6NLhLqeAzfCSpU0zGR39iEazh7CpedG7ESQf7g8Y9cW4qFgLLkjDw8qXMbQTy1qAhY1rJJssZ_nVJBUi8EqZJOAXqFNGDph5SL9x_sTi1zc_AWEixoQAMFk50ee85TZ_iBYBk1IObxmLLVF7VyWLKas4v2ZeJcew79qwDCAWme32JeplBguf_MMOHQo-FnuyOEz37AaeBFr-rggdFyg03gbYawD0xCXfzYemUMmog0gB7JdWGI-RPQuNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108540" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd558a4adb.mp4?token=WeS9tmcwRFJM_P9xG6xutGObJWhXGyDmx348wKKVhWicjVbz_KmBYBrguqFiK9T8nURGOmgrodmE6OtHR7LKY11a6zum__HvryocsCg6-u9ctUf70se8wNtILnk2YGSXtFgwURRTk1e0pd_cLDtwDMxZB076sEbAWwe3gtqqOkY7cWUiOf5rAa0MkQ7f062-uju2Uz3sctg9dj1tjD_CscJpm9f34RDLSngcrHZXkpK_TSalJfx0H0GXpgttaV4-9fdwqQa-fQoz1pc4rEcos_S8cQMA1iy4dk2KGGjPx-YZ1F4ccn8IxwGJQK5nALl-KfE1U8ux9WN7glhjIrru5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd558a4adb.mp4?token=WeS9tmcwRFJM_P9xG6xutGObJWhXGyDmx348wKKVhWicjVbz_KmBYBrguqFiK9T8nURGOmgrodmE6OtHR7LKY11a6zum__HvryocsCg6-u9ctUf70se8wNtILnk2YGSXtFgwURRTk1e0pd_cLDtwDMxZB076sEbAWwe3gtqqOkY7cWUiOf5rAa0MkQ7f062-uju2Uz3sctg9dj1tjD_CscJpm9f34RDLSngcrHZXkpK_TSalJfx0H0GXpgttaV4-9fdwqQa-fQoz1pc4rEcos_S8cQMA1iy4dk2KGGjPx-YZ1F4ccn8IxwGJQK5nALl-KfE1U8ux9WN7glhjIrru5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
حضور افشین‌پیروانی سرپرست محبوب سابق پرسپولیس در یکی از کنسرت‌های معین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108539" target="_blank">📅 11:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108538">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇮🇷
کمیته استیناف رای خود درباره یاسر آسانی را صادر کرده و این بازیکن مشکلی از نظر آنها برای همراهی استقلال ندارد اما تا زمان اعلام نظر نهایی AFC قرار شده که رای استیناف به صورت رسمی اعلام نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108538" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108537">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26563f619.mp4?token=QpdBPxphcU2VdjapxjAg46CGL0bUIDYHjMj69c_ckwuzkdXVAs0guXK3uPxUVgqe8y2DCIwy-j89DwUHEzQHrgDyT7xqjx2iLIGY2xKdSYM_0ggDaxhRogktTLESajT7KhyfnpOMgIWjFyCR3c2bsQ9rcQVcA_KK8zZjEhTgbVYYI7nBMG_Z-OGWk1Hr6Xg-StklmUlwZExIqeCJdWhPUumlmT9Ae8sv-eZmasD6ony6qZYhafD1aNLgA4gN00UFgTmmVxwDrkepvHMtW-H8zwm7Th0ikoEbeR-c7joPZ6vy5gWgASxJZBL5Ymnay8bDR-AfBIf79dBqzdb2hI6zQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26563f619.mp4?token=QpdBPxphcU2VdjapxjAg46CGL0bUIDYHjMj69c_ckwuzkdXVAs0guXK3uPxUVgqe8y2DCIwy-j89DwUHEzQHrgDyT7xqjx2iLIGY2xKdSYM_0ggDaxhRogktTLESajT7KhyfnpOMgIWjFyCR3c2bsQ9rcQVcA_KK8zZjEhTgbVYYI7nBMG_Z-OGWk1Hr6Xg-StklmUlwZExIqeCJdWhPUumlmT9Ae8sv-eZmasD6ony6qZYhafD1aNLgA4gN00UFgTmmVxwDrkepvHMtW-H8zwm7Th0ikoEbeR-c7joPZ6vy5gWgASxJZBL5Ymnay8bDR-AfBIf79dBqzdb2hI6zQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
نظر عادل فردوسی‌پور درباره سوپرگل دیشب آسانی: واقعا با کجاش گل زد آسانی؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108537" target="_blank">📅 10:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd1a54114.mp4?token=QLSCRndU7HqvqF0OwpUyu3z0o8OMgu5LummpWEX861OnR9uS-RpueywAsO-SHZNGaDxN_LXWf7HrIn8TRJ754Ti0Otie7UR-wHxq6QkAYfr6ylZ-CxznlLBsBU7C8XOMlwzoDS9PKcoOw4wXEW-0_5W5OlNCnxTf2gfW0VNEK33sTGa2e__6fTELlAXhShPfaKEsd8IQxwHL28Lsvnl-LMyIkkqemLhUfRvVxR7az2JaTiDmEO277-h37fISzrDcVvlkEnPXjYIC_Fa-pbM0nhvgSxStwbT6TVCgusX01XyFlgwlu8v3Uv4OcRXsACIp0r0Dc-C8lUqp3rxWKfVpAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd1a54114.mp4?token=QLSCRndU7HqvqF0OwpUyu3z0o8OMgu5LummpWEX861OnR9uS-RpueywAsO-SHZNGaDxN_LXWf7HrIn8TRJ754Ti0Otie7UR-wHxq6QkAYfr6ylZ-CxznlLBsBU7C8XOMlwzoDS9PKcoOw4wXEW-0_5W5OlNCnxTf2gfW0VNEK33sTGa2e__6fTELlAXhShPfaKEsd8IQxwHL28Lsvnl-LMyIkkqemLhUfRvVxR7az2JaTiDmEO277-h37fISzrDcVvlkEnPXjYIC_Fa-pbM0nhvgSxStwbT6TVCgusX01XyFlgwlu8v3Uv4OcRXsACIp0r0Dc-C8lUqp3rxWKfVpAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سوپرگل دیشب آسانی با گزارش نوید استادرحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108536" target="_blank">📅 10:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef2c6d44.mp4?token=NqvdxchS3VHIPu9NQ42JdTFuLOIFBsRapkjZRhSoNh-Kf1mZ4C88c0bIeJK_cIWE8U_O_9gIS8FHWtntZxZJSHDHu8BVBGPauOI91hvvANXJ0MtdWnHoHE5BPfQJ0uvEDLJvnF6h738ZhwGD4APVMdFvprq5SGiJ6SvCwvJGDQUcm_wjXyH59qy-LdHS78Gg4qaz4AqDIyEsDY1x6MwoQLH93PB-M_hhKevNguGjVmrYzyfAiIQhQafOGLifFidyOVF-Xq5TOh6eufcOvZXO5M4GoaMZg1RuV-NEVI-4-yE0DSKGt4Salf80QSyWIL1eNmIw8pqyU_Reus5KYN3dBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef2c6d44.mp4?token=NqvdxchS3VHIPu9NQ42JdTFuLOIFBsRapkjZRhSoNh-Kf1mZ4C88c0bIeJK_cIWE8U_O_9gIS8FHWtntZxZJSHDHu8BVBGPauOI91hvvANXJ0MtdWnHoHE5BPfQJ0uvEDLJvnF6h738ZhwGD4APVMdFvprq5SGiJ6SvCwvJGDQUcm_wjXyH59qy-LdHS78Gg4qaz4AqDIyEsDY1x6MwoQLH93PB-M_hhKevNguGjVmrYzyfAiIQhQafOGLifFidyOVF-Xq5TOh6eufcOvZXO5M4GoaMZg1RuV-NEVI-4-yE0DSKGt4Salf80QSyWIL1eNmIw8pqyU_Reus5KYN3dBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
فلیک دیشب خطاب به خبرنگار: "امیدوارم بالاخره یه روزی یاد بگیرین که من وقتی مستقیماً با رئال مادرید بازی ندارم، به هیچ سوالی دربارشون جوابی نمیدم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108535" target="_blank">📅 09:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccc8c0b68.mp4?token=K6F9v-AJ8uu9T_D8ISG5G6SNB2GkEwD5xNuoKC3gPB6gd7zpgJvViY_hcisNS8iQ4u47UPor2fuH2IOh2D8QTnd3CVzlf4gk83jH0oZ7GM_kzGRc7-M0zSgrJZX6GE4XtLv7ALKcPhUrThmdkl2_NeMwBny2MWQFtH5BGupxTRDYXsCJnrUqZWDx5dNIW9_aa17dQYtvhgiKnQIpdm2Z_K7jit7hcyMLPkY1EsUK3xu0KzIO1OyxIGEY6unqB0ZFBMT61jfjBVnpNTQmS6XXKA2NSp3WZP0zW-4w35KDAro-6KoBGEDSf33HqpZDu8yPxTnMCMQfFSN_LbyrExckjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccc8c0b68.mp4?token=K6F9v-AJ8uu9T_D8ISG5G6SNB2GkEwD5xNuoKC3gPB6gd7zpgJvViY_hcisNS8iQ4u47UPor2fuH2IOh2D8QTnd3CVzlf4gk83jH0oZ7GM_kzGRc7-M0zSgrJZX6GE4XtLv7ALKcPhUrThmdkl2_NeMwBny2MWQFtH5BGupxTRDYXsCJnrUqZWDx5dNIW9_aa17dQYtvhgiKnQIpdm2Z_K7jit7hcyMLPkY1EsUK3xu0KzIO1OyxIGEY6unqB0ZFBMT61jfjBVnpNTQmS6XXKA2NSp3WZP0zW-4w35KDAro-6KoBGEDSf33HqpZDu8yPxTnMCMQfFSN_LbyrExckjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🔥
▶️
چهار سال پیش در چنین روزی، دیدار مس رفسنجان و پرسپولیس
- بازوبند مشکیه؟
+ تخمشو دارم داری؟ تخمشو داری بزار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108534" target="_blank">📅 09:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfecaa3ae8.mp4?token=Sje8-KJQhfECHQc4jUI1SbTiyDYuoKH57ATOH8OYjVdMyTUayCBv6oC4QDUHPps50OlQWcRrwg2TPDchrhEYyBncqG5aP-Ck1u_aXENW805MdsgSWkJ1K4ZK6fLCWuoMpJx5ue-MBS7yfF3nhZQ-HehHI7QcbcQ1uBq8aycu2o--kZOcy54vHmLNq37q0PyBvosLWelsGkmngjaW8d3DOqgaZ6zXJQOKyBFKvPmCEBNEnL1I8SlERFMwOvQiuv8Mu8Cg6AoAU-e4rpNMinLiD0kBche_RfAaCpG0GevlHzFl9o4Mf5P5iDZq3-2rQApHiTnFeNPxp0og-FZ_fYH9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfecaa3ae8.mp4?token=Sje8-KJQhfECHQc4jUI1SbTiyDYuoKH57ATOH8OYjVdMyTUayCBv6oC4QDUHPps50OlQWcRrwg2TPDchrhEYyBncqG5aP-Ck1u_aXENW805MdsgSWkJ1K4ZK6fLCWuoMpJx5ue-MBS7yfF3nhZQ-HehHI7QcbcQ1uBq8aycu2o--kZOcy54vHmLNq37q0PyBvosLWelsGkmngjaW8d3DOqgaZ6zXJQOKyBFKvPmCEBNEnL1I8SlERFMwOvQiuv8Mu8Cg6AoAU-e4rpNMinLiD0kBche_RfAaCpG0GevlHzFl9o4Mf5P5iDZq3-2rQApHiTnFeNPxp0og-FZ_fYH9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کنایه داریوش شجاعیان به مصاحبه اخیر میرسلیم: ولی تیبا هم ماشین بدی نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108533" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد. بیرانوند باید شرایط قانونی سربازی را انجام دهد. او تمرکز لازم را در این چند وقت نداشته است. حتی بازی با ازبکستان او را کنار کشیدم و آلن مربی گلرها گفت بیرانوند تمرکز ندارد و بازی نکند. من چون می خواستم بیرانوند را برای جام ملت ها حفظ کنم او ار کنار نگذاشتم. خبر ندارم شرایط او برای سربازی چطور است اما اگر برود باید برای او برنامه ویژه بگذاریم. من در مورد پرونده قبلی او هم هیچ توصیه ای به کمیته ها نکردم و هر چیزی که قانون است برای همه باید اجرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108532" target="_blank">📅 09:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d0cb95d7.mp4?token=vDlD6cePF_FNBaylTztEHMsGlPcOq-ugsLtt2gywyN8FFYYxQ3OtYOTUFvrSdtWT8rUC-zvGjr_W_WoqWYH06Gp49OtMcqoHL4m1wOb-zg48Hes0szZmxlHgFlf08Mion2BfY9XbDmPovXdGZuhGaxpVkMoCkaXhsLnQIPBb8XeKo4KuibuAOVro0A7oWuvIVY9dQIhtYUWwFrS4BpDtgV4xoa599tyij81jOUisbklwA73tPl4_M4I4UFsbZulHXvtOsPn-1STo4JVS3nUNZe8dp-cs_4G_fiX_LocgpoIjN-oUV9LtzcRhHivZDgWte8m_ct3ATD1VwFlOtb5-tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d0cb95d7.mp4?token=vDlD6cePF_FNBaylTztEHMsGlPcOq-ugsLtt2gywyN8FFYYxQ3OtYOTUFvrSdtWT8rUC-zvGjr_W_WoqWYH06Gp49OtMcqoHL4m1wOb-zg48Hes0szZmxlHgFlf08Mion2BfY9XbDmPovXdGZuhGaxpVkMoCkaXhsLnQIPBb8XeKo4KuibuAOVro0A7oWuvIVY9dQIhtYUWwFrS4BpDtgV4xoa599tyij81jOUisbklwA73tPl4_M4I4UFsbZulHXvtOsPn-1STo4JVS3nUNZe8dp-cs_4G_fiX_LocgpoIjN-oUV9LtzcRhHivZDgWte8m_ct3ATD1VwFlOtb5-tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دیدنی فرمین‌لوپز در تمرین دیشب بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108531" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=SDUA1zWEsxY6g2zP3lz7IQxRqPejaNKai95H14QSiTOokc89E_M6jgu0kq8JZfP45UGW1dNU0ziIQAYg-vrnbY7CrgsdrtKfuZ14azZMTmpLm_32aKn4G7lhhxmUhR01DYxZQIiTwFlMAuQ6kbMBrZ82TOpd0xlRp3VBb40BkNdOOt3zmi8DIQrEidXIvp035TWviMzO7K_eCMvEg7gBdSv9J-PlNfkb7nR2ftUSfwWcK5WQflVf_MvIaLINTEFyTomx6W1-9hcoY8wbaWV2X5LpHYrvfJLrMEcF3fMl8ANDI27Z5O4EY0K1Wg8CU95wjRgiz6VLopTvLABws50Y9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=SDUA1zWEsxY6g2zP3lz7IQxRqPejaNKai95H14QSiTOokc89E_M6jgu0kq8JZfP45UGW1dNU0ziIQAYg-vrnbY7CrgsdrtKfuZ14azZMTmpLm_32aKn4G7lhhxmUhR01DYxZQIiTwFlMAuQ6kbMBrZ82TOpd0xlRp3VBb40BkNdOOt3zmi8DIQrEidXIvp035TWviMzO7K_eCMvEg7gBdSv9J-PlNfkb7nR2ftUSfwWcK5WQflVf_MvIaLINTEFyTomx6W1-9hcoY8wbaWV2X5LpHYrvfJLrMEcF3fMl8ANDI27Z5O4EY0K1Wg8CU95wjRgiz6VLopTvLABws50Y9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
امیر قلعه نویی و پاسخ در مورد دلیل عدم دعوت از مهدی قائدی:
🔺
استقلال که از الاتحاد کلبا وقتی قهرمان شد بالاتر است اما چرا آن موقع آقای کی روش و بعد ویلموتس او را دعوت نمی کردند؟ ما یک اصول و چارچوبی داریم که قطعا در دعوت و عدم دعوت موثر است اما موضوع ما فنی است. ما دقایق همه بازیکنان را با آنالیز در می آوریم. آیا مهدی قائدی الان شرایط خوبی دارد؟ آیا بازیکن فیکس النصر است؟ مهدی قائدی در آمریکا یکی دو بار مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108530" target="_blank">📅 08:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108529">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdcb8a6f2.mp4?token=NCQjNfIFyBD3IvYviHDr0s0t6KGofMq7w3Y1gYNI9hwIVtyZ71D1g1MTDBN3zmbfYOD3xKTDkpYJqceOu5Er7YVjSuy7aEhqarNab9XbjsHAx9mPTGVnTCjmXPR8As3YgxjW98z9lxUpQcxAn7tBY3UbvMppimnnfsiSvwk2NX7oC7PXs4helOyQqlQdpwGZ0WRr_t17SL68Xk8_mMUb7lUrib964lrEGZhFW2LMKuRhZmZrhjUofp_OWF4j-GlwjWcmbLwyvTqU1u3y6ol_9GRxfF44GO4USXivjUDDDamBBNdzuZQUewTLUkHItAdgQMGWoQHMsn0_Z0Msz36fdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdcb8a6f2.mp4?token=NCQjNfIFyBD3IvYviHDr0s0t6KGofMq7w3Y1gYNI9hwIVtyZ71D1g1MTDBN3zmbfYOD3xKTDkpYJqceOu5Er7YVjSuy7aEhqarNab9XbjsHAx9mPTGVnTCjmXPR8As3YgxjW98z9lxUpQcxAn7tBY3UbvMppimnnfsiSvwk2NX7oC7PXs4helOyQqlQdpwGZ0WRr_t17SL68Xk8_mMUb7lUrib964lrEGZhFW2LMKuRhZmZrhjUofp_OWF4j-GlwjWcmbLwyvTqU1u3y6ol_9GRxfF44GO4USXivjUDDDamBBNdzuZQUewTLUkHItAdgQMGWoQHMsn0_Z0Msz36fdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
پست جدید AFC برای یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108529" target="_blank">📅 08:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108528" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/108527" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108526">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108526" target="_blank">📅 01:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108525">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c408292b8.mp4?token=qYn13LO5yMww5bV85bqzrRILh6mzPa2eOZjhNyrC4JgGB5nqvXzB1CnMldvCQLG8mS_UbW-aoRZHuxcMWp_6SQsmSHRMdIHg5PC2NWTRQ0HYQ9aTJG3ravIFwOUCstfizJVxlKW7K2lBjuRXuMsrv8DgKA1m9nytBzFxwxnKHu7HzBHi_XVd7urTE_GD6CRqMLqWm0NBpndNxw7Ns6ZBR-2QjRt57Mak-wjm1G8utoC6CYMrcImzTUteDG67DECMfUFk_2UCriH-HvTkBfP-i6uuDyMr8pXgozFxGowRV-qFPYqDH6-7YgHYsTV2T93gpQfbkpLseX6KBj1ho4UZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c408292b8.mp4?token=qYn13LO5yMww5bV85bqzrRILh6mzPa2eOZjhNyrC4JgGB5nqvXzB1CnMldvCQLG8mS_UbW-aoRZHuxcMWp_6SQsmSHRMdIHg5PC2NWTRQ0HYQ9aTJG3ravIFwOUCstfizJVxlKW7K2lBjuRXuMsrv8DgKA1m9nytBzFxwxnKHu7HzBHi_XVd7urTE_GD6CRqMLqWm0NBpndNxw7Ns6ZBR-2QjRt57Mak-wjm1G8utoC6CYMrcImzTUteDG67DECMfUFk_2UCriH-HvTkBfP-i6uuDyMr8pXgozFxGowRV-qFPYqDH6-7YgHYsTV2T93gpQfbkpLseX6KBj1ho4UZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
میثاقی به نقل از حسن زاده رئیس کمیته انضباطی: فسخی برای یاسر آسانی از نظر ما ثبت نشده است و او هیچ مشکلی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108525" target="_blank">📅 01:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fda9a24a.mp4?token=R_JEBdWMz4yQEQxHZyU7EfX7oKZjIi265zIn9609A3hpBzZicaTCTGiUibwuyxggmtIGCMqVHGmUkSmcOAd7a-uPOyYm-9r98Hqva-wyOyarm82SOs9Pm8BYPN9pmKZSn8DW_ujnYBplHLN4Cw4NGZyQH2-_qOK3k2-hVZVugOS7vE821e7Uun276tMuIwpBX0GYMIpO_fuXfPD9VJ_0Q-swu6dR19meyVpZcCZiEhVK-e_PSAKOCl01NWNQQLG1g04MXl72t3JELfdF0dCwXlK0XCtxGVPNZxAAbEaepNG1PLE_8YlYRjom-vX-v1_ErE76UEDI34djP9tq0p3tWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fda9a24a.mp4?token=R_JEBdWMz4yQEQxHZyU7EfX7oKZjIi265zIn9609A3hpBzZicaTCTGiUibwuyxggmtIGCMqVHGmUkSmcOAd7a-uPOyYm-9r98Hqva-wyOyarm82SOs9Pm8BYPN9pmKZSn8DW_ujnYBplHLN4Cw4NGZyQH2-_qOK3k2-hVZVugOS7vE821e7Uun276tMuIwpBX0GYMIpO_fuXfPD9VJ_0Q-swu6dR19meyVpZcCZiEhVK-e_PSAKOCl01NWNQQLG1g04MXl72t3JELfdF0dCwXlK0XCtxGVPNZxAAbEaepNG1PLE_8YlYRjom-vX-v1_ErE76UEDI34djP9tq0p3tWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
برای درک بهتر سوپرگل امشب آسانی فقط کافیه از این نمای دیدنی تماشاگران ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108524" target="_blank">📅 01:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFr8qinx6KVKaKwj1dX_Fqf98qnxjhPE1hBQb3-zKDyBQQcTQBi9mshQfFhGlz6AyU_b41Og7msk3YqxscdHZKklkysTQQs561J9PL3biaw5Ty3pzrWc_yJjZQnfdPV4RGQfiI-0fXcQVnxaVxR0t6TXuX0FDJuxie-zAhy2Kod9i7IgJsFIDdKMyxe_Ro4bQQndiWZHa9s2Gd5RvD6BhKIRl_yeu9ymnck4-Mf9zLx6sQlpQ4AnU0DoN0PeroOF6CQR1n9WrG2li8pCvBrXgTnNZaqmCYjR5Ojn6T0_fHV9yK13UcGIgdFUfVK1zBl8qy8vsXEbRHxMppDBMiNWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
واکنش تند و کنایه آمیز میثاقی به تفاوت میان سفر تراکتور و استقلال و گل‌گهر برای بازی در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108523" target="_blank">📅 01:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f09ab8993.mp4?token=s6IGxsI3QGdApc8GX05J6Obfm25QKy6xUUcbv7pkKUI0AbU8XkKUjC70j18JY-sVgIB7bP_CJgekIoxOD3ZsuIbXMmfRuB9NEwMt2QSzmGiQspPfNGPJOXJtsNxpGTGc-KpTa56QsOc-2BsOgw3bV8gGIIhQGJzxGjcGrjt2OWGhMdwT2VaqzCV2Ef5Vped3OOb8q-Ts_Cl1q5ZpE1_Oj7IAMg1jnGDsSL7dzJB3cPXgHPo27nz7U6LqnFZckFDSljvj9a8k9tiQMHkd8WeFSuV2e5gf__1mVuiokthCmoTkAQ112SvVAkPE9jU1GUwYRtLkzsUJXyAaFk8WozIpX5Ny_pRcsB91IJfp5vdzo6bjaTLU08q_mTmBZnBwPMJAkaHzLQ9fHBg4RiLAseATqnwkuLs3VpRTuNZFyodOGuQfijmomnC6GHqyuriDtce0acgoNAX_-pFiFu-h_8ElekkP0eQloHuEQNanx3k6GTyypogGyPHUPcZAi_VcBdO6_FYhRXolYeXK01lSQxymiHHc-njMGK4vHB5KhC9Vpsgq3JYA52DfmMtnehd0fXOj3JrfiuA3-_JUbab6c0I3X4tKXUBpk1lRy9PBKU7SLBBYbLS_Q7itRTYUjaqvWkXF2_kk5VyW7UCNMUxdfOLMuQrboprlLGLfd7WFOw_68EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f09ab8993.mp4?token=s6IGxsI3QGdApc8GX05J6Obfm25QKy6xUUcbv7pkKUI0AbU8XkKUjC70j18JY-sVgIB7bP_CJgekIoxOD3ZsuIbXMmfRuB9NEwMt2QSzmGiQspPfNGPJOXJtsNxpGTGc-KpTa56QsOc-2BsOgw3bV8gGIIhQGJzxGjcGrjt2OWGhMdwT2VaqzCV2Ef5Vped3OOb8q-Ts_Cl1q5ZpE1_Oj7IAMg1jnGDsSL7dzJB3cPXgHPo27nz7U6LqnFZckFDSljvj9a8k9tiQMHkd8WeFSuV2e5gf__1mVuiokthCmoTkAQ112SvVAkPE9jU1GUwYRtLkzsUJXyAaFk8WozIpX5Ny_pRcsB91IJfp5vdzo6bjaTLU08q_mTmBZnBwPMJAkaHzLQ9fHBg4RiLAseATqnwkuLs3VpRTuNZFyodOGuQfijmomnC6GHqyuriDtce0acgoNAX_-pFiFu-h_8ElekkP0eQloHuEQNanx3k6GTyypogGyPHUPcZAi_VcBdO6_FYhRXolYeXK01lSQxymiHHc-njMGK4vHB5KhC9Vpsgq3JYA52DfmMtnehd0fXOj3JrfiuA3-_JUbab6c0I3X4tKXUBpk1lRy9PBKU7SLBBYbLS_Q7itRTYUjaqvWkXF2_kk5VyW7UCNMUxdfOLMuQrboprlLGLfd7WFOw_68EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
آیتم جالب عادل فردوسی‌پور از کلید واژه مصاحبه‌های بیرانوند: درصد، دلار، ماشین، میلیارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108522" target="_blank">📅 01:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601362fff.mp4?token=iGiGXraYB0tQUNB9MwXU_jwMxhJeHYHpeiqBrlCbfvyIH8hzz_mRU26AArRhyar820DW6GUUJi80QRNiggRb2e1VdqawksU-cqivD58Nim1JwiUQiafS3FgPpOKYcB1z1MnYduM9CbI-nVLARk3a687oxMLnqOUKrpiq5rlqvC3ju9HoOwy6Zr4T8JkEfVqHTC1qtocM2EIicJ1kQbBp6PDVAUaD3J9xny4ZPH4sxRC_1MJXXHy9_5ivvAy15rNxf7M10GOArLBAQdN1gyhDzxbh98Vr4QM8Z6d1rOaqeVlcyt6Df1P56_lyVZUPIqjJLRLfEX_3iYgaTpDE81xIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601362fff.mp4?token=iGiGXraYB0tQUNB9MwXU_jwMxhJeHYHpeiqBrlCbfvyIH8hzz_mRU26AArRhyar820DW6GUUJi80QRNiggRb2e1VdqawksU-cqivD58Nim1JwiUQiafS3FgPpOKYcB1z1MnYduM9CbI-nVLARk3a687oxMLnqOUKrpiq5rlqvC3ju9HoOwy6Zr4T8JkEfVqHTC1qtocM2EIicJ1kQbBp6PDVAUaD3J9xny4ZPH4sxRC_1MJXXHy9_5ivvAy15rNxf7M10GOArLBAQdN1gyhDzxbh98Vr4QM8Z6d1rOaqeVlcyt6Df1P56_lyVZUPIqjJLRLfEX_3iYgaTpDE81xIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد سخنگوی هیئت‌مدیره تراکتور نسبت به شرایط سفر به عمان؛ مگر کور بودند که نفهمند تراکتور و گل‌گهر هم مثل استقلال بازی دارند؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108521" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله سخنگوی تراکتور به بیرانوند: برای مسی هم تیم را به هم نمیریزیم. بیرانوند که عددی نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108520" target="_blank">📅 01:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab8a7b19b.mp4?token=lhZpolFizXySCcAITv7DSmPnoWuhk4XN31t4MWlSemnTmKlj3Xaf5Yry6ot7KOJk9CxXvFnvjMM9PoT7s59yW_duFR88v8j7zZw_XCQpSQ-RjLx6ZrTn2swPX91NSS4e19QKG5D3rHxHo77KDh8kKiPwRYuFA_q6HZC_DO48DvcUH-NlcrdlnrR6M1DuI4n32zN6X5z8HLPj2fSnwTAoRodltC0lg0w_DSrQzH1qZ1y9OCNi8rZ_vTEY2fOWx05_uuKFaSoX044HRzVbF9g5PFVKuiWcMDrZsUV4eJiBgnd1txUcbZibRMZASHkkJ2u5qpkP3RCfJNvf_Aj5dqd53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab8a7b19b.mp4?token=lhZpolFizXySCcAITv7DSmPnoWuhk4XN31t4MWlSemnTmKlj3Xaf5Yry6ot7KOJk9CxXvFnvjMM9PoT7s59yW_duFR88v8j7zZw_XCQpSQ-RjLx6ZrTn2swPX91NSS4e19QKG5D3rHxHo77KDh8kKiPwRYuFA_q6HZC_DO48DvcUH-NlcrdlnrR6M1DuI4n32zN6X5z8HLPj2fSnwTAoRodltC0lg0w_DSrQzH1qZ1y9OCNi8rZ_vTEY2fOWx05_uuKFaSoX044HRzVbF9g5PFVKuiWcMDrZsUV4eJiBgnd1txUcbZibRMZASHkkJ2u5qpkP3RCfJNvf_Aj5dqd53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🙂
شاعری هوادار استقلال برای برد شیرین آبی‌ها در آسیا مقابل الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108519" target="_blank">📅 01:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a267abb0d.mp4?token=ftghupQM_beIoAg_tzSlongUc8csGDiZe5t2MnTdVbbOk70uLt2fa7xLIrGOJ2oTnvPR0ch4-V6uyXrtEEpp9-PMWC8Eg_kVaBFWreIxTmagGOiQDxguzRwqDidX1Qkx7CNjDDCPEucMc0JqaERtvI_Sku9u2gJy8pz_q11CkgtFFu4sgbOvtA0caZuDmWuIgjNWQBnYOtjl3CGcprnFt9s7DmK9-CVGWNsDe45cMfQrJr1l6iTEEdUMf_UPZS64cgBPezblfvs8HwndgZHePNK0cMxMwWhafFxOz6QsRzwGSQIqOA4PGRge8vMz6NPn8hONcoGNLPwjZkTyJZYsfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a267abb0d.mp4?token=ftghupQM_beIoAg_tzSlongUc8csGDiZe5t2MnTdVbbOk70uLt2fa7xLIrGOJ2oTnvPR0ch4-V6uyXrtEEpp9-PMWC8Eg_kVaBFWreIxTmagGOiQDxguzRwqDidX1Qkx7CNjDDCPEucMc0JqaERtvI_Sku9u2gJy8pz_q11CkgtFFu4sgbOvtA0caZuDmWuIgjNWQBnYOtjl3CGcprnFt9s7DmK9-CVGWNsDe45cMfQrJr1l6iTEEdUMf_UPZS64cgBPezblfvs8HwndgZHePNK0cMxMwWhafFxOz6QsRzwGSQIqOA4PGRge8vMz6NPn8hONcoGNLPwjZkTyJZYsfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری هواداران استقلال برای پرسپولیسی‌ها: بروند برای خیبر و سایپا کامنت بگذارند، اینجا آسیاست و جای شما نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108518" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW7GbXZncDr2a92zfJYQE-J8TMiSogXxGnqJr_xXTdvBCd1qs3VhuznK92gjBFGor4s3NUB0_uO2h3bwhawnomU8KWfghG0KOEY3hsHkoDnylV9MmOgjGzf7QlBqOxomZceH3nZt2ZmulSl_5sIs7yllz2J45WmadcNEzR05AxCisBd60ZW9MIKSeV7ejdVt7Xmi8kz7n4d_cZ9N6AcwRAxFZF6fFYXsylMbhZCb14x5S0u7N-36yIOdTp24ye5dRcEDSLtUVqlSytXxs71qctngJfWFxN2GVHQlexrNYKEY_1fHdWj_e27-KrlKBFYpLAQxL2u1ypGmoc9TajIivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🇶🇦
استقلال تحت هدایت سهراب بختیاری‌زاده، برد مقابل سه تیم مطرح قطری.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108517" target="_blank">📅 00:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217c826d5b.mp4?token=VTjRlpxDnjBjzOY_cUFdClxiObp73Abtn_MY84v-zMsmnLlhasl6INKB_LSBWg67s7OGvSIDh7yoHlSGFXHrSwXYeODgmbK0b6Y2Utq-BEvVTyLP_IZDjpbbsdlrrstpiUOnSEp5Wc3D1W3Ce9uF8SHBdWglSgd2TpqWUtV3-lSHen27geyE6elnhc5l-2Y_OTLhggnloETxVL1lxqcptsJxxzPkw_b0mb7hcPxjZsYbmsZddTXYsIPRIyxQNKGdeCkmHYXsvDdx1cnuTpFjEAruTIUKDTpjAPzx_YxuulLh3edXSIuq19n7j5-APlC7O_SEmGT6m9ab-SXh_8KY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217c826d5b.mp4?token=VTjRlpxDnjBjzOY_cUFdClxiObp73Abtn_MY84v-zMsmnLlhasl6INKB_LSBWg67s7OGvSIDh7yoHlSGFXHrSwXYeODgmbK0b6Y2Utq-BEvVTyLP_IZDjpbbsdlrrstpiUOnSEp5Wc3D1W3Ce9uF8SHBdWglSgd2TpqWUtV3-lSHen27geyE6elnhc5l-2Y_OTLhggnloETxVL1lxqcptsJxxzPkw_b0mb7hcPxjZsYbmsZddTXYsIPRIyxQNKGdeCkmHYXsvDdx1cnuTpFjEAruTIUKDTpjAPzx_YxuulLh3edXSIuq19n7j5-APlC7O_SEmGT6m9ab-SXh_8KY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
⚽️
میثاقی: توافق اولیه یحیی گل محمدی و فدراسیون فوتبال برای تیم ملی امید صورت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/108516" target="_blank">📅 00:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108515">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr1sucWCv1aLONOr7UeVKuDLXVNqMCmSXylnxxHLvcfiM4efakNRmOkYuT7L48TJFX7Ul3RgjgNCwZMxGjAiWCmXfVJ0wwsSoYmCl5FCd5ceDmmBCgqtMffM8EPcxCRr3qqhE_gvvY-FGu5yhjdRNIbyWqVA6oBfFadqTz-GJEHs9hgGPCH-CVe4mCcMhtaa9H8ICCZ1aFCDVia4lNz5DuHwxc85fFc_DH2qsV4OttMiyn1mq01dn-901Psz_Bewou_QDWReA2sE_vCuKXZUr6O9L45ZOvT19y00rJllDyMlhTYft5vNmmytbFGVeS-EokrN3kpfS6pDwTXWtxhu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
🇮🇷
استوری کنایه‌آمیز سامان‌فلاح مدافع استقلال به مهدی تیکدری مدافع پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/108515" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648dfd6944.mp4?token=pykUGiHxYFR4Hswdxk5gubCrq_tBuutZRgWwuiDR7iptT11g15JGTe5Rgni0etWb4Z7eifriId4Pcqtd7Yh6fznjFD4DjpPpnIZVtHTy3QnNIJmyieOpCgBHlhIItGkeK7_57sLpJFIIL1WNVTKcQYMC-gBVrBZqnRLVh00aE9OOPHVhubwx7x96ItWV6aUqhZDAjPhq07kRKu837P7qgTVJrPi-ZV2l86gGUMkcjBOGOTlFTMHg3b5ZhgBrUeMhsFcGqLkULUi-OxWq0Q8RbDKiQVPy5k8FcgEnA-73v1LRHGt18wk1-kAaySrE8onxv3ToIeEra-RidyoMGQLgQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648dfd6944.mp4?token=pykUGiHxYFR4Hswdxk5gubCrq_tBuutZRgWwuiDR7iptT11g15JGTe5Rgni0etWb4Z7eifriId4Pcqtd7Yh6fznjFD4DjpPpnIZVtHTy3QnNIJmyieOpCgBHlhIItGkeK7_57sLpJFIIL1WNVTKcQYMC-gBVrBZqnRLVh00aE9OOPHVhubwx7x96ItWV6aUqhZDAjPhq07kRKu837P7qgTVJrPi-ZV2l86gGUMkcjBOGOTlFTMHg3b5ZhgBrUeMhsFcGqLkULUi-OxWq0Q8RbDKiQVPy5k8FcgEnA-73v1LRHGt18wk1-kAaySrE8onxv3ToIeEra-RidyoMGQLgQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
واکنش تند و کنایه آمیز میثاقی به تفاوت میان سفر تراکتور و استقلال و گل‌گهر برای بازی در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108514" target="_blank">📅 00:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇮🇷
پژمان‌ماندگاری مدیر رسانه‌ای استقلال: مصدومیت یاسر‌آسانی جدی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108513" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdCW-88zyWq0eYKC2qfGfs2MMY9evXEI9szrTwT2s5S8tJXq9E3E0OIv6-3qluhzvhqyO3DShJu3-X0szNRisRwIt9vI_CskkYI42c-9ARO2QXX37EZ32f7yzWOztsZan8xG73k5qdpVYXP7rkb8uJA0A_VmOkjBgj7DbtLvdXdGP7-oPST9C8sCxr4ULoSZq2SGn6mPXRD6f04mZjLdWWOPWfAQ-Nt7ZYM5JNGAnkhdqksf2CQs693WtI-LIxYLFrBprRgi_-yEsjvcbCZBd7pVWHhBa85ds6s9kv-zWrJnXLqzO1NxES-m2dNO6GxCHXL3kR6vTU-vmrptG323cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توییت کنایه‌آمیز استقلال به پرسپولیس پس از بازی: یاسر‌آسانی به شدت قانونی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/108512" target="_blank">📅 00:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
❤️
زنوزی مالک باشگاه تراکتور: همیشه گفته‌ام عدالت اصلا رعایت نمی شود/ یک تیم با پرواز وی آی پی دولت سفر می کند یک تیم مصیبت می کشد
🔴
نمی دانیم از چه کسی گلایه کنیم/ آنهایی که می گفتند پزشکیان حامی تراکتور است حالا بیایند جواب بدهند
🔴
حداقل اگر می خواستید یک تیم را با پرواز دولتی بفرستید به ما هم خبر می دادید
🔴
بیرانوند جوانی کرده است و رفتارش را می گذاریم روی جوانی اش
🔴
امروز شنیده ام که تیم های دیگر نمی توانند در عربستان هم بازی کنند این را من شنیده ام
🔴
باید برویم به AFC نامه بزنیم  و مشکلات پروازی خودمان را اعلام کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/108511" target="_blank">📅 00:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔥
🇮🇷
گل‌یاسر‌آسانی با گزارش عربی الکاس قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/108510" target="_blank">📅 23:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCUqUme0tv1ULdUcOug-eDtR0oiCBxAlT4G82nC0eKb-SrqeiGJdLHsekSiQWIe6RlZCz1hlYdewZKXYn2tYax6m2QpiIUVZzpGsNL7j_YT6f23n2t8398UxKXz4CiuAmV4VIhRKafiDmG8T5PxYpSy3DGTbflc_Pt4kEFM34rkF9Yi8bdhmzoUzNeyUPwzCVj-7ha5s8DMRfirhk_Et-P9WzhDsvt9ZS3GAVYhV5TCSDMe49xtW2_hSxIt_brSNUdyhr1nP6BiTZmCtSkr2WiXrNR8OT--kkdKFSQhaRe4kGcJpDhvqbTWr5r8mnPvdEqTzyIKBzg651rjyYiUNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌نخبگان آسیا؛ دومین تیم قطری هم مقابل استقلال زانو زد؛ یاسر‌آسانی با عمل به وعده خود تیمش را با وجود مصدومیت به برتری رساند؛ فرعباسی بازهم درخشید
🇮🇷
استقلال
😀
-
😃
الغرافه
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/108509" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40f9d30d1.mp4?token=UB0WU1FcVPVD6upIVs5oEHH43XKZPMYik6VmWsvORDHMRQdZbx3n66yxhAKPrG-lXdx4S2PDBM0ZuTm7aW2up7_GWfgSNtUiDT3aAx3e0jKGiP_S0Tv9ubi75x3BZKss3meQ_808j3s4Mk194TDugXmkvlw69zLJwrpYEHuWyaHFjDml7GIPH5o3xB6p4timaZCQBVUDISnXnkS4aGQH82kxj1-MSN5hMVUIBg75DkW_zVGPQ9Ahbq0R_4tB-3z7q_a3A_m6B9ehC-JlDK_GGiw31LizQT2YwqSfnkGJOJ-LKOF0BrkI8XsxV_YiMFbiEWdCLSdMECGUKOiZdksBiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40f9d30d1.mp4?token=UB0WU1FcVPVD6upIVs5oEHH43XKZPMYik6VmWsvORDHMRQdZbx3n66yxhAKPrG-lXdx4S2PDBM0ZuTm7aW2up7_GWfgSNtUiDT3aAx3e0jKGiP_S0Tv9ubi75x3BZKss3meQ_808j3s4Mk194TDugXmkvlw69zLJwrpYEHuWyaHFjDml7GIPH5o3xB6p4timaZCQBVUDISnXnkS4aGQH82kxj1-MSN5hMVUIBg75DkW_zVGPQ9Ahbq0R_4tB-3z7q_a3A_m6B9ehC-JlDK_GGiw31LizQT2YwqSfnkGJOJ-LKOF0BrkI8XsxV_YiMFbiEWdCLSdMECGUKOiZdksBiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صالح‌حردانی امشب شانس آورد فوش نخورد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108508" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خوشحالی اعضای استقلال پس از سوت پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108507" target="_blank">📅 23:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwaQLE1cQzH4jUKmqbMsXmn7WVtsXEEhoSuqbBQgXVeIQORocA52M7DfwXAMbAlVInQSATSpW0vL70ULzoRUdKmjQOHbFylQ5JFrwYp8xVc-Hw-1uWJKpx79uiFeh4_wAiT3qibEHW5_JBS_9RJpjPrZTIWWcG8RDxOzC-4N5xRdAl2NmL88PViCAGUfF5oOYuLwH9euXvBZsN0BbuGvLH5kTLsdfRoYtNfJhOYFTI9tRSX4J60MMrA4H_oxPWkSKsGx0qUAqT1qpoDA0riyV4gmnaA6Fd5pem6cy9Q_-fo8uyI3Et6HueSAiShWJZt5pAJowUY_IAb6iq29LTMb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌نخبگان آسیا؛ دومین تیم قطری هم مقابل استقلال زانو زد؛ یاسر‌آسانی با عمل به وعده خود تیمش را با وجود مصدومیت به برتری رساند؛ فرعباسی بازهم درخشید
🇮🇷
استقلال
😀
-
😃
الغرافه
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/108506" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هنوز تموم نشده</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108505" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب دیگه بخیر گذشت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/108504" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از کون آورد استقلال این دقایق
😐</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108503" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بازممممم شانس آورد استقلال</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108502" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حردانی کسمغز
😐
😂</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108501" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حردانی ریده</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108500" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آشورماتوف نجات داد
😐
😐</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/108499" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108498">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/108498" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108497">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108497" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الغرافه زور گل زدن نداره فقط ریدمان بازیکنان استقلال میتونه این امر رو محقق کنه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108496" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108495">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسلامی هم ریده</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108495" target="_blank">📅 23:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108494">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرعباسی بازمممم گرفتتتتت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108494" target="_blank">📅 23:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۷ دقیقه وقت اضافه
😐
😳
🚨</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108493" target="_blank">📅 23:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpYJFhxLsgVQSl-2nEHP497URDVVfyFqeycdJJaxOyVs5-JnRtiw2wjpOErzCKMesBIdRRjTXNhD7cBDFvNWvaP4KHrG4jk1AWFnUAJMRUf844pBlRYI-1vN6GKG6eLv81X7AjlsPQRSVk6-KzeMYy-6nf4VkyIkToWktA7uHkTok5geLWvXQ5_0SDbvRXSeeGWbhtw6xA2xyjZNtJqvX0pDiA6IyvBmwjsesDDOA10QqcoT3f89AqCuu1qob8yud3Fb8oibD6VKtEiAtmW8M0gTeSXuY214vNnGdX5IGUWslTxEUTTuhSID6M2bNB_P8vIFzeL8PUJpxF8xfueoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العین امارات چهار بر یک مقابل نماینده عراق برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108492" target="_blank">📅 23:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108491">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24051a9445.mp4?token=b5rbmrmHemGQJgfxjjDZqDcHGG-oyVe0N5yKGmFoxkirssqOW_C6QHGGk-bpIzinlT1D8qbIONrjqs97tBiJkWDBikanjjdcg15RjCrLriYYpCspISCAR8ylg6m9ZJVgX_WFmAWbapAHGySBywBj4625RWaqiwQj5g7F4XN9CZNfZXAQdgVTGhEUrORg8_io4JDZcoIQiMlBkRHODhoGDRc1xletJSfztrLUYWPizeENED0veO0zyz3rl2lcagFur_lCAPgNFHf5jRIwkYp94vsyxyJMyGYtEtHZ7npnvSvQOJ-s6Xk_iAO3no8VGc7OMPBFaVwGXgVxpNQaB99RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24051a9445.mp4?token=b5rbmrmHemGQJgfxjjDZqDcHGG-oyVe0N5yKGmFoxkirssqOW_C6QHGGk-bpIzinlT1D8qbIONrjqs97tBiJkWDBikanjjdcg15RjCrLriYYpCspISCAR8ylg6m9ZJVgX_WFmAWbapAHGySBywBj4625RWaqiwQj5g7F4XN9CZNfZXAQdgVTGhEUrORg8_io4JDZcoIQiMlBkRHODhoGDRc1xletJSfztrLUYWPizeENED0veO0zyz3rl2lcagFur_lCAPgNFHf5jRIwkYp94vsyxyJMyGYtEtHZ7npnvSvQOJ-s6Xk_iAO3no8VGc7OMPBFaVwGXgVxpNQaB99RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپر سیو فرعباسی روی موقعیت تک به تک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108491" target="_blank">📅 23:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سوپر سیووووو حبیب فرعباسی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108490" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1974c7b3a7.mp4?token=h_ctoldG2AL34f_i8qSWbHpQbDxWzMaW4jzan-XZj-ZTzUxJ5PKsKrlLEFFHm4zl0Qofz6neIgm48FHxWhjT9UtIEH9P1I8kqz3SwEZp6WSOkQaCIeyX0unLuV3GctKQQkqS16xeoSBIUIyhq0dAEz7Voen6y7ypLKXVH-H7ptc7P5eOYmLMsFhGyTuaKSjR5YzwBvIux8svNUHBr69s1rT2Quwt1kLfnB_fdB652GTv_2ymvvlnx3HNfiBbilLOzjvIkOcyDCq4QdvhKCVVZi4aCHOZKgjFdo3COP0nTbR0M9F_uzZND8TzH4J61t4Ol1xFfZKuj0SCLbVAwHSk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1974c7b3a7.mp4?token=h_ctoldG2AL34f_i8qSWbHpQbDxWzMaW4jzan-XZj-ZTzUxJ5PKsKrlLEFFHm4zl0Qofz6neIgm48FHxWhjT9UtIEH9P1I8kqz3SwEZp6WSOkQaCIeyX0unLuV3GctKQQkqS16xeoSBIUIyhq0dAEz7Voen6y7ypLKXVH-H7ptc7P5eOYmLMsFhGyTuaKSjR5YzwBvIux8svNUHBr69s1rT2Quwt1kLfnB_fdB652GTv_2ymvvlnx3HNfiBbilLOzjvIkOcyDCq4QdvhKCVVZi4aCHOZKgjFdo3COP0nTbR0M9F_uzZND8TzH4J61t4Ol1xFfZKuj0SCLbVAwHSk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سحرخیزان عجیب رید امشب
😐
😐</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108489" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108488">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سحرخیزان بازمممم ریددددددد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108488" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=pkhGxfPfYgxKhJXHrenfTlhC5oHw_V0jAsR2cv1wfhxgDpu7Uk9dk248KSEE6NSOaCxo2poReZO4BwP9vKRY62Jx6Mcc8vY8FwJJxjEFhvwJajgjC2W6vy82N7SoCiyJKkmt0OJHqnuPV-Mt1hFdWj509aIOuR3QyoOK_LkfyhY0QcYflbM38vAjGMNWH1yk8Ch8BH5sXp8i1Fa3K6nSHHqKvVRYzj4Jn_Z-iw2vxG8ubvaur1z5Hb9P5EHbNVIUsNe1epcw6PETo-5J-Ua9txYWjb5oRGAA1C5CP2-g5kPsDAavSaBIwnF05WhrdX8iJoqj_ql4UqjE1bXT-oV1_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=pkhGxfPfYgxKhJXHrenfTlhC5oHw_V0jAsR2cv1wfhxgDpu7Uk9dk248KSEE6NSOaCxo2poReZO4BwP9vKRY62Jx6Mcc8vY8FwJJxjEFhvwJajgjC2W6vy82N7SoCiyJKkmt0OJHqnuPV-Mt1hFdWj509aIOuR3QyoOK_LkfyhY0QcYflbM38vAjGMNWH1yk8Ch8BH5sXp8i1Fa3K6nSHHqKvVRYzj4Jn_Z-iw2vxG8ubvaur1z5Hb9P5EHbNVIUsNe1epcw6PETo-5J-Ua9txYWjb5oRGAA1C5CP2-g5kPsDAavSaBIwnF05WhrdX8iJoqj_ql4UqjE1bXT-oV1_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108487" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108486">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استقلال کوووون آورد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108486" target="_blank">📅 23:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رونالدووووووو گل شماره ۹۸۱
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108484" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">النصر دومی هم زد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108483" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">استقلال سه تایم مختلف تعویض کرده و دیگه حق تعویض نداره</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108482" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از حلال بال سهراب بختیاری‌زاده نیاز به حرام بال جواد نکونام در ۲۰ دقیقه پایانی هست</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108481" target="_blank">📅 23:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108480">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">النصر یکی به نفتچی زد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108480" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آسانی با مصدومیت داره وسط زمین راه میره</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/108479" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آسانی با مصدومیت داره وسط زمین راه میره</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108478" target="_blank">📅 23:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79f4a95ed.mp4?token=eZ77L3pmzH3nHHkzFmbABz8OCqbN6ngaVwWPqWSiNIgixqfwAZE_xAHmRawcKmZT0VDmMcT4keen2chYvKSzQxQmfvwnKAOnRrAxz4CUp4KFWTSelTMu_5ld-CetHNd2PzvlXvAg2GZD13ZJrU_qkLgE6m9f_c4IOOG1ZSKztGIm4GYoU-rqpbagSRVdHg7ehL6DMBosC2p-ZAnLj6doxKxjw30b71Mg5f6ZvyaihULI6jUW3iajUdU1Y_nc1Tf75CVqXF0DPPceQ01_DKLqquoU8JYyPn9Ajq_2OXStbdn_PvlagMwgBU7pAfAugSHd9fZKjIs3bHtESggnudcJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79f4a95ed.mp4?token=eZ77L3pmzH3nHHkzFmbABz8OCqbN6ngaVwWPqWSiNIgixqfwAZE_xAHmRawcKmZT0VDmMcT4keen2chYvKSzQxQmfvwnKAOnRrAxz4CUp4KFWTSelTMu_5ld-CetHNd2PzvlXvAg2GZD13ZJrU_qkLgE6m9f_c4IOOG1ZSKztGIm4GYoU-rqpbagSRVdHg7ehL6DMBosC2p-ZAnLj6doxKxjw30b71Mg5f6ZvyaihULI6jUW3iajUdU1Y_nc1Tf75CVqXF0DPPceQ01_DKLqquoU8JYyPn9Ajq_2OXStbdn_PvlagMwgBU7pAfAugSHd9fZKjIs3bHtESggnudcJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گلر نیمکت نشین الغرافه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108477" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108476">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یاسر‌آسانی رو به قصد کشت دارن میزنن
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108476" target="_blank">📅 23:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ولی چه ریدمانی خوبی کرد
😂
😐</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108475" target="_blank">📅 23:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5ed1792.mp4?token=Q0I9V8CPrYSCNhhibVt37GwuwYxQnsM-jK7wTlyiaMvGHY_THVt7VCrqPreQf5eaOQ-pTK2p6zKTCk-CH3xpRbfaoofVYxI-kNXo8GjKZMRSbIHXrLf5Vrc3Gx8Epph5xVbU4xYzjsWYz8hMpthwyPP4IOIPWczPScwDCWCzwXtIgf1z2hfp0Lg7I8TljfCj5CzFdDCKlFaC9CoanUFdSTJ_2_wLsqBjDyrGFuXciG0mDEQMM0lAa3gBajShj7JJDjKmxu7o0QJ3fIRbJIl9GKDLkjlHdBDZAfIZQYaLb9kra1qNtpSzwNLTFGF1kJb0Q6dbblu5t_L-xqI8Dcc5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5ed1792.mp4?token=Q0I9V8CPrYSCNhhibVt37GwuwYxQnsM-jK7wTlyiaMvGHY_THVt7VCrqPreQf5eaOQ-pTK2p6zKTCk-CH3xpRbfaoofVYxI-kNXo8GjKZMRSbIHXrLf5Vrc3Gx8Epph5xVbU4xYzjsWYz8hMpthwyPP4IOIPWczPScwDCWCzwXtIgf1z2hfp0Lg7I8TljfCj5CzFdDCKlFaC9CoanUFdSTJ_2_wLsqBjDyrGFuXciG0mDEQMM0lAa3gBajShj7JJDjKmxu7o0QJ3fIRbJIl9GKDLkjlHdBDZAfIZQYaLb9kra1qNtpSzwNLTFGF1kJb0Q6dbblu5t_L-xqI8Dcc5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل دوم استقلال به الغرافه توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108474" target="_blank">📅 23:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلر ریددددددد
😂
😂
😂
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108473" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چه شوووووووتی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108472" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سوپرگگگگگگل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108471" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گودرزی زدددددد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108470" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108469">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گل دووووووم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108469" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108468">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108468" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108467">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازم موقعیت استقلال گل نشددد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108467" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108466">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108466" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کوشکی ریدددددددد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108465" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108464" target="_blank">📅 23:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
آسانی مصدوم شد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108463" target="_blank">📅 23:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
آسانی مصدوم شد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108462" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علیرضا کوشکی بجای ماشاریپوف اومد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108461" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سحرخیزان بازم ریددددد
😐</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108460" target="_blank">📅 23:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108459">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b597f0d9.mp4?token=uV8gGni-Y5_iNamk2qSY1ZPExYVTKenuhiaGDyIrShLlwy7aC2DS2PnJaCWi43ZfB_6pMbLqz3oO8-NtAjcXPNpAXQNpOl0Voq_D8IeDLDBGGxmEdBtx83RTpr7m0K0HSTnFPjr94O45TsDXODd3ePkH5MZnO5I0o8jlyK1awpomB1KOrWvJO9kewY8kMF4Bd49M9GHL0HE1jyIlMUQlCtNt_hLoJNRsjS0OE9U6vUQPFDbGH-w1BJHdfNnSgMWo3OWhuqZlHTMDvtExirq1JsGxJDIENXafI_O_3RdHuEQg8nO-IRqWHs2vXuys-GamfU85ASfDmyJeb1xlcCmPCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b597f0d9.mp4?token=uV8gGni-Y5_iNamk2qSY1ZPExYVTKenuhiaGDyIrShLlwy7aC2DS2PnJaCWi43ZfB_6pMbLqz3oO8-NtAjcXPNpAXQNpOl0Voq_D8IeDLDBGGxmEdBtx83RTpr7m0K0HSTnFPjr94O45TsDXODd3ePkH5MZnO5I0o8jlyK1awpomB1KOrWvJO9kewY8kMF4Bd49M9GHL0HE1jyIlMUQlCtNt_hLoJNRsjS0OE9U6vUQPFDbGH-w1BJHdfNnSgMWo3OWhuqZlHTMDvtExirq1JsGxJDIENXafI_O_3RdHuEQg8nO-IRqWHs2vXuys-GamfU85ASfDmyJeb1xlcCmPCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول الغرافه به استقلال توسط فرجانی ساسی
الغرافه ۱ - ۱ استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108459" target="_blank">📅 23:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108458">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گل برای الغرافه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108458" target="_blank">📅 22:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108457">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">العین اونور ۴ تا به نیرو هوایی عراق زده</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108457" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108456">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">العین اونور ۴ تا به نیرو هوایی عراق زده</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108456" target="_blank">📅 22:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108455">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آغاز نیمه‌دوم استقلال و الغرافه قطر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108455" target="_blank">📅 22:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108454">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇮🇷
تهدید جواد نکونام بعد بازی الشمال: اگر بازی بعدی اینجوری بخواهیم سفر کنیم، با تیم امید خود در آسیا حاضر خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108454" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108453">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6PypQpZufHbChnr_Dh96EJsbEq3SC-3LlqJDRsuyopXuRmdN0jwvi92hWrqyLb2tFbnkj9veYBiqFB1LvaSfFuDwDVlc7un6xlWu6pIcoQMWXtQsPHE2mR2WnQTbidqvywpviJUiDIMhEvnmjDkZcP-LPzfbarqcZ6BL1ilDeJ3sSqUFZXVN12EAIvTdAtiShG8u7jUCMlZ9mL6QQA8wdjnMZ1vl8dtafC7_XxCdJJTjZIl0fEEERzpbLV3wBe-zRY9xTXwJEOLBK3aHxnTdTicniZ90MHmDixjen3i9QoImN68W5xhneaGm8rklf3ZCf-UnrMAbhTkHLKBMPe8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی النصر و نسف قارشی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108453" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
