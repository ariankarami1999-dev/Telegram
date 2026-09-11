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
<img src="https://cdn4.telesco.pe/file/PvhePQbDwlmvTt6lD6Eoj88CkRUaojBHP4hmNUDqrZX0aUfDJ-_sCcjwFVNgstue2JXS-af4FWDkviMDnnWmHIY_iRyU6QkqiLKR_yvzNXZ71oz6-nERdoL1IzNqZh-9qTG8X7r5WSTBK4_i3B-Z-cy7ZPPassBiUVDxlmYitNbiV9mFknLJZKq4hWuIBkd32JH7ic9BCZbkjm5S2-KuQPzaZ0NtYVAE1ujdVHql83dA2fznMe4OTS7pET7CseVDuWH1kUk8FcW3ZrpjKHbaF9Tum8NvmD0GV6viddBHmAXy9Mfse32r0a-EeZd15t6595P37RSuL2_-i7DzimaX5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-689025">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad652c96e6.mp4?token=OnOpI7hxGJCQo-yUlS0dBvEYATKFJOjlwyV2Vo5h9BMMSiPAnyohQxgObl1kkjulGLbRVZjXdgGppSy_1eLCaD5ZZF-o1_mJzsCOVfp3pcQitgcZQvKe9Tz_DIKYmnGkZb_1YCQTOqNpCLx4h0Bz-r9NAaUJJaGaeiJQCCFmlCxWNzPBQvV71UBJDR6EkWoJ4kQlDMI8EzDhPnYqYg64WOvfG_YgL05gMGfmgam_B95VZL1_Lm7d2JDO--MQ6GrVuNb6uCKF4qJmrgTmKDlHumhMNjVxG2bqZtL9Y53CZ8wayl7xSYJmR0Tz2poarpObX7DVP1arvoRG1u3WYMo_mKkHoOdiHVciQkwq-P9ThTmG7Ok0rAPe7MoyLALFKWmxiJWMv8t-pkMFYnLf0dESGgJ13QbBO6GPg2ydPxj3d4qq_vUjm1Ij_SrZNo80FmKkRVXSkSzLkeNTVpFMMmgpTqh4UWAX2DKGDwTf-bIulTCqMJ95bzql97Xj9h5lNkxp1vXEuyrclV2Tzke6yR0TQDICtHEbLNTGBPZHx9ZbFyx8EuygSu8JfMH2nRu_qjaY6j-wKsOYcK_xe3rVsPCXcxuhmrFGd9lhZth4ptZus-6O2N6iPKaNNYMohgFNdXs9iUZ8kVu2aXpRV3A2HFnxBb4V20ouGCc_OuCSlhtUTq0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad652c96e6.mp4?token=OnOpI7hxGJCQo-yUlS0dBvEYATKFJOjlwyV2Vo5h9BMMSiPAnyohQxgObl1kkjulGLbRVZjXdgGppSy_1eLCaD5ZZF-o1_mJzsCOVfp3pcQitgcZQvKe9Tz_DIKYmnGkZb_1YCQTOqNpCLx4h0Bz-r9NAaUJJaGaeiJQCCFmlCxWNzPBQvV71UBJDR6EkWoJ4kQlDMI8EzDhPnYqYg64WOvfG_YgL05gMGfmgam_B95VZL1_Lm7d2JDO--MQ6GrVuNb6uCKF4qJmrgTmKDlHumhMNjVxG2bqZtL9Y53CZ8wayl7xSYJmR0Tz2poarpObX7DVP1arvoRG1u3WYMo_mKkHoOdiHVciQkwq-P9ThTmG7Ok0rAPe7MoyLALFKWmxiJWMv8t-pkMFYnLf0dESGgJ13QbBO6GPg2ydPxj3d4qq_vUjm1Ij_SrZNo80FmKkRVXSkSzLkeNTVpFMMmgpTqh4UWAX2DKGDwTf-bIulTCqMJ95bzql97Xj9h5lNkxp1vXEuyrclV2Tzke6yR0TQDICtHEbLNTGBPZHx9ZbFyx8EuygSu8JfMH2nRu_qjaY6j-wKsOYcK_xe3rVsPCXcxuhmrFGd9lhZth4ptZus-6O2N6iPKaNNYMohgFNdXs9iUZ8kVu2aXpRV3A2HFnxBb4V20ouGCc_OuCSlhtUTq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه CNN با مهندس هوش‌مصنوعی شرکت آنتروپیک که روز گذشته از سمت خود استعفا داده و هشدار داده است که هوش‌مصنوعی ممکن است در آینده‌ای نزدیک بشریت را نابود کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/689025" target="_blank">📅 15:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689024">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
از حفظ خدمات در روزهای جنگ تا بازسازی خانه‌های آسیب‌دیده؛ روایت همراهی اسنپ با جامعه
شرق نوشت:
🔹
مسئولیت اجتماعی شرکت‌ها در سال‌های اخیر از کمک‌های مقطعی فراتر رفته و به بخشی از فعالیت آن‌ها برای حمایت از جامعه تبدیل شده است؛ اسنپ نیز با اجرای بیش از ۱۶ طرح در این حوزه، در مسیر همراهی با جامعه گام برداشته است.
🔹
در جریان جنگ ۳۹ روزه، اسنپ برای حمایت از کاربران و حفظ دسترسی به خدمات، به ۳۷ کاربر آسیب‌دیده ۳ میلیارد و ۵۱۵ میلیون تومان کمک بلاعوض پرداخت کرد و ۱٬۵۰۹ کاربر راننده از تسهیلات بدون سود بهره‌مند شدند. همچنین راهکارهایی برای مقابله با اختلال اینترنت و GPS توسعه پیدا کرد.
🔹
این همراهی پس از جنگ نیز ادامه یافت و اسنپ در تأمین و بازسازی ۲۰ خانه آسیب‌دیده برای زنان سرپرست خانوار در هرمزگان مشارکت کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/689024" target="_blank">📅 15:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-EpyAwddiKEJW0ywcjxbk_Fmk1hcDyj-cNODsqgiUsdra5FJpekzT8ibhfTvDWgbvPjNKu3XHkr9_g_ccke4mIrUlIMEcECAe8fdQtXqrLg2mmXhMxjwbM3rroqoboVLq7qOy6ZgJrtAArZkEo68tf0oWHhCWp6vIKlpC4uG2PN8yYDEn18Dk9kNlf9sGfNYrIHJVUhNrBzwNWQlyroYOzZEe3ZFsrdX9oEgGlR5Z8ZvcrEqdqtZr4MQXxrJUnWp12HrjbAI8WYITzwG6raM-3DG7JFCHtseWMSB3rmsKp3zB0PK1hgt0n9YYbqcSBP123MmsRwgWhHma3UThYrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGnERH8A1vXINKY5hlP4xp3pSKtiXwS_W2fJ0lG3zyOoStMiDsaJN2OOSh59I0GYz8LR0Juj5FaahCuJY4cYo9shE3pVh_V8vBIpZGpv9KxmachGhN-yga4T-m2n-vEOkPMx7LpkeA5xbhrzKLS_No-DKX6oe9nVlsIDmVuOWW2j6cdqwu4XbJEidllrzebFbA3AIe9iVQ_iaNTU-wSVHqgtWDL-9xkYelVIDlj1oQg-XwoRIiV58b8tTyD2KR8zI-5PeEoTn2aCojdhZ_gd7S13y13mzAccwmCZJ_MGav0DgqS8SIvu66JbdcsWh8tuoijfPX-lu2KN2wapqYKJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oknFwXbTsZhRdy353AKGxLFWmMXdEnr5M7vG_jg4TEKpi8cwPZEn7afck0tdFdEXTK1-wPgJ-2XHOo_hbTgBJFa2iRs0wBeQmLa-kYZ15qwWyshYPwXrA7BfAqHUxxgmZifRImJpShx_ThUPU_p02Rhhv8LF5K9hqTolext2BBBRF1qO4DpXtkX_bI1O90P9oVTcaCPzOzadjhmRIcLFLraCXgcg5BjFautUQPZG1GVMm3qrB_MpVRurlqZYPMHbdiK-sQEDt5IgOaC-1uYQEnFQ6iu4Rg_Yf5lyT7LRdgOOk17yJ1Z0qMB_TONqDzCSvQWpmkTWStgHzia0dky3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Knm92FLT9-DCk6CT7B2qP4sMhJjESlXzX3_BodiV0B6Vyxb_ZrX2IgEGHRgAHEizvAd6_MTeuWpWt8-ZJaohwyHau2RqRohZ_TbxmCSTKeoce-q7XUSt0oTyF-zspzA4s-GfrHy3Ri6Zih847JSSL0UBPTYgTu9iO2KG2KgvyYGOsQTjQAQrL6uW99wrq-lWd_RpyMel409QyaeRvmXuf0iGL16N4_YHfKrdPzzikirG-bt25Cs08BfaKknM6S_VUJGWIhUvmMgvIWNA32lS13F7mWfucmL9AopyZmgMT8aKz3aiKpnSvseTGwqfTBD-n7f0Wal4Wb0jEyWUfFbujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7r2hdMAA5U0X493e5uDSAd2uZWYClEPq2jDEz_z4-ciLk5UwknsRJB-H9JJ4vrpZcVMwCnM2YMSX9Ww-xSA-51jcaOGlMqy92EmYRyPMy1Hkq6pwFGuhDZ_i_eTJht1zPfBPinULqt8bK0vlwlExfUSWFwcJ4yMO2xUu_H9GuY_iXz2wiozfPLtu5zxWl0fiRnWXipF-TNSEO5vc_ZE7IVQVOq_Q88JYHn5ltKn4kBKHSbbdR4hwm_PBfGlhE6bTbBOwMdTlE-yd_E2ti5GnYMUs3o17TVesPAmD5DR1tFj9p_PDamuf_gbSYmT_MtB8EUV9Fll1j6dWoPRkgoEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qciD9i4ZNCGqVAAqJa7EH2PdZbeHhVniHjV8aARBa9AIvYgj5o1M1JC5WhR50aT_JuHrmM88X-pUiDw7y2kwdtCN_i5qQ7Dq3qoAYajiT7YcY3cUltNHUY7kh2McMyzUqHhJr68VEnVGmRVSCzjtBiZDjKcoan7bfTLiW013d6oCFly1-JQ1rO67kRwahIG0ny533Apbu6Z4EPFo0tPEqXlz1htUT8bQY-x-G7TR1tnk6AX-d0NB4lgaSZAj9xCXaNkvmoFRm3TbAcvq_EfMxhY0w64-fLgPIoEOlRxS48BfIIk-nQBre4Y_TNYf9GOwOd7L0MW76SNrVgJRjnKYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0hUf5BJewZHGVu96QHohzLJTRIbVq1HmpMoLZFfV3LXhWRPkkv0iYHEt9b9Pr7HUl9Y-HDY7-CCeQ6zMKayBwUwnNWgapP3F39WIev29AF9Nh7Z938ehNU0554Fcby6zTF26MfDAxJhB0OuR2Ez3dl0SAu_ekCiRSzFyR642YW8shvxzAyJIemburtou3XyKl4s8jsB5FCiqW2l1f7fBhF_BBRW2m3LZvAZQ6EeywGuSJs3KG-h6P0yyn4GbYPx4VLK8Yf1pjkLViGw9nh9BhjfZZ717xgg3DnmJeEsYUPgwzEWQG81IG2yWeVjSb9TVvBx_ZF3AxK3O_JiaoHS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viR8cqUEBUVxLhF_yDa8d-ggFo6Tzicn5BmeMKfhY8viXi-ios3dlQzuZ1TGlGR01hGJk-9C7LhXE25iNVcB0OP3Oet-Tk18PDYlS1gWn98yowayBAR_e4thFsu3oRlETGTNHa9s2WVMNur8oiLjqUktD86pz3HuZbFidQ5OtnCfJvff-SF8RkZz_HK8kJS3LnFENxFcSLEUGntL7eo2FAGjl5pV3W3AgnrzjL4WSqbhSFjfr31VCy1bEbyCHhSDieKCwxxFa_XAxszE2yNm0G6nRqyoeiFtZXcc947n8l1r5sOnQPfMIzEtHAyf5OrYtMM4Udt8SAwyR-9HDX9dBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPISHbvLsoRRpDJXoGcsYE3H6eA-NB2c3Xj9uWAXKFmxCUM0980YY70HmuhKsG3BSifXnSyGZGnO6mulHu7xFUqp4yB76U4aPnMadvHqpQxJ9APoht8jmK3Cpw3dOHAdS7YVxiF1njEzFCZUdTo5nwvZOR-wj_SvRISJEs27M9hA3basEld8izphBpKQjkeYg5A0bRajGRA0Pm1WtI5VHWQZP45n_vquoZ3jM4N67D1l61z3Aj4Oxu7d3UIFxEbyuoaflAkl5iuVCLhircdOJZ9-BHjXE5UE2nDKjfAVdJzuF1JBeyblcrjymcKyc72L1sI61FOMU15tiHvlPxi_pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
بازتاب دغدغه‌ها و مشکلات شما مخاطبین عزیز برای شروع سال تحصیلی جدید
🔸
روایت خود را در قالب  متن کوتاه  ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/689013" target="_blank">📅 14:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrLu2zs8VpY83Alf1dIYghISgzBgAwzHFaJXivf0sIvOp66h0z17ZEDxK-SCZFlt5tnkoEYnQZA8l36HKjjKJq6yqFxkaYQHdtcsbNlSKLeZZfhRVyKWwbNZJmuCILlDxjfDWoZ6fv0fUVYGVIA13dhA03Td4sCnBbxTBvhRf9VOfBcVz0YyayzPl2MVk7QYpBDoysTAyrMhuYXcF6n6U2zuvZ7U5wmrkj_PoGeTYvojyxl-sQsn0ZhQWcnSD96lUQ2-n0XWg8MSa5eXnNCDIitTM8MTkCSw9rm5oOHI-XbwGvRaQfzANW7gx4_NFKjd0kNGnIxClh-bxKcwI3HDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: فتح‌مبین انصارالله ثابت کرد امنیت خریدنی نیست
دستیار و مشاور رهبر انقلاب:
🔹
آمریکا و متحدانش در استراتژی و تاکتیک به بن‌بست رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/689012" target="_blank">📅 14:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5aee1199.mp4?token=gyysFzaAD3D3qVg2vc31-h7N_LdW60LzFGYLb-OOXGmsHbJ7BRCNx1t5Y-mzG7e95kpePNUJAe_bEM_PWedz1rpgZjxuqgR2bBIv1y0l8c_0if5cH_gqZ6XaTxjr1d3DTYsbWNVBBGn5zF3ubrr_gKRgYbMWwDXeC4ARS1xzhKKs7YCH4teHW6_d3slrzmQzWMaz7lUICAjK86tRDaxZMVboKVzBrGRCJkSq3cbr4tGxMKQFuyLqXf6kJgJinovbG1UrML8gJYOPR5N45-jZX2abnS06Y3YgB4ssz1aVBLkcr-SCVp3GKAYBW44P2Hs18XF-sD6mGRH7er1SQyJH5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5aee1199.mp4?token=gyysFzaAD3D3qVg2vc31-h7N_LdW60LzFGYLb-OOXGmsHbJ7BRCNx1t5Y-mzG7e95kpePNUJAe_bEM_PWedz1rpgZjxuqgR2bBIv1y0l8c_0if5cH_gqZ6XaTxjr1d3DTYsbWNVBBGn5zF3ubrr_gKRgYbMWwDXeC4ARS1xzhKKs7YCH4teHW6_d3slrzmQzWMaz7lUICAjK86tRDaxZMVboKVzBrGRCJkSq3cbr4tGxMKQFuyLqXf6kJgJinovbG1UrML8gJYOPR5N45-jZX2abnS06Y3YgB4ssz1aVBLkcr-SCVp3GKAYBW44P2Hs18XF-sD6mGRH7er1SQyJH5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/689011" target="_blank">📅 14:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/689010" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/injAyme6zg01s8m7wqugvIWkeC8YNpfU9oAls-C3XrFTPbro1zgHDLIgekDTz4W0mEea6V676WYwKwqct3ACJpJQ18jmK5Bc0qJLecInJk6VBjItPrDfwMJcHPXyiiadGAmaZJnsMNFZAFmLpazVCB7bPX5-8Tl_7mOlwlCffen01slpkuM2YoH1VqCboNVBy13f4pnSumlUmN9vYkWAMSO74KQgEpLSnTCWVjwKH_8B8V5_h0780J7b2sMbsVKFIFSvPwhpQDmvgoekHCvqbejPzfXc79Ri1Xuv0SDiKAjg9jBdXH5nEoK-ZdSYJDPiKVv6S67tPZT1jj6NygkEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار بیانیه‌ی نیروهای مسلح یمن درباره یک عملیات نظامی گسترده و ویژه؛ به زودی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/689009" target="_blank">📅 14:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda9e6a4c5.mp4?token=BlSfrjhjNmnHHxaluuj16OZHC9lX72YauMI1ck_s5Bczyd5hgXMVXDwtqul1x1_qVN9wrSRRBesp8WHxd6hUETSn-wC-bQr-yoTC5V71BjGrJhV7c_6o3RCUyJS4LdIk-06IgZ_bH4JnqhlspMXJ8jJ3lMtq8IiQZCWhM0xqIIZKT84-JrXD13o6o-z01qXJlcyAjBwgjsKl5XkvqQGq8FtP1sPhwXtibMX93mCy89LPdEQjNkCKyYlsR-wzbmTbNwinKALzfZYtD9G83BW9yaEakLmM6OgQ0zD0EYdWT8eDZB74Qy0YHDfOdtlpcheq6s337-iurj6qVkDSTNcztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda9e6a4c5.mp4?token=BlSfrjhjNmnHHxaluuj16OZHC9lX72YauMI1ck_s5Bczyd5hgXMVXDwtqul1x1_qVN9wrSRRBesp8WHxd6hUETSn-wC-bQr-yoTC5V71BjGrJhV7c_6o3RCUyJS4LdIk-06IgZ_bH4JnqhlspMXJ8jJ3lMtq8IiQZCWhM0xqIIZKT84-JrXD13o6o-z01qXJlcyAjBwgjsKl5XkvqQGq8FtP1sPhwXtibMX93mCy89LPdEQjNkCKyYlsR-wzbmTbNwinKALzfZYtD9G83BW9yaEakLmM6OgQ0zD0EYdWT8eDZB74Qy0YHDfOdtlpcheq6s337-iurj6qVkDSTNcztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر
فوری/ یک شهپاد آمریکا امروز توسط نیروی دریایی سپاه مورد اصابت قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689008" target="_blank">📅 14:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
در فصل تابستان امسال در آلمان ۱۴هزار نفر بر اثر گرما جان باختند./ در سراسر اروپا ۳۳ هزار نفر در اثر گرما قربانی کمبود وسایل خنک کننده و گرانی انرژی و عدم رسیدگی اورژانسی به گرمازدگان شده‌اند
🔹
عجیب است که آلمانی‌ها با حقوق فقط یک‌ماه می‌توانند بنز بخرند، ولی از خرید کولر ناتوانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/689007" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فرمانده تروریست‌های سنتکام برای بررسی تحولات جنگ یمن به عربستان سفر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/689005" target="_blank">📅 14:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84db58b274.mp4?token=FMjog-lXEkMvDct7oFr4S5mI2AK5HVDLGFL1qqcrs6nnA_Z23mgtvVbuO5BIdFOf0Zw7AJsNctg4Wlvx5khWiITEtEUM95jPfqU4JHnX9XwVn82WSleRdcrCyg1zNSANK_jxPhUeAFHZYGNWzxvGWh-fB0qY2K40NJ4sX17gXO4TUpBBi2529Yr0PE7Nm3rwTgr3TSKLDQA3RoqlpkZ-lJc7LjjGjbgt1DMFDHktYSqpWUYcnUqkFCOLsf_nLMc9AfPQmzf-HoWrx0eFhnn1xtMBUDX7gATlcEfxd7qGepH53uBvbOo0QcS2tcEgxriAzy4kxzf8zu82h1gKwIHrmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84db58b274.mp4?token=FMjog-lXEkMvDct7oFr4S5mI2AK5HVDLGFL1qqcrs6nnA_Z23mgtvVbuO5BIdFOf0Zw7AJsNctg4Wlvx5khWiITEtEUM95jPfqU4JHnX9XwVn82WSleRdcrCyg1zNSANK_jxPhUeAFHZYGNWzxvGWh-fB0qY2K40NJ4sX17gXO4TUpBBi2529Yr0PE7Nm3rwTgr3TSKLDQA3RoqlpkZ-lJc7LjjGjbgt1DMFDHktYSqpWUYcnUqkFCOLsf_nLMc9AfPQmzf-HoWrx0eFhnn1xtMBUDX7gATlcEfxd7qGepH53uBvbOo0QcS2tcEgxriAzy4kxzf8zu82h1gKwIHrmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک فروشنده داشت از جنس فوق‌العاده شلوارها برای مشتری تعریف می‌کرد و تضمین می‌داد که هیچ‌جوره پاره نمیشه؛ که درنهایت این شاهکار خلق شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/689004" target="_blank">📅 14:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD_g5AEcchz0UJ4qsF0C5al1FubVc23SiJreiOFi5-3JpjotY6yXBMpiIPcCaWV0TkCTrgSRZI9FlGv5545VJ0ROPfLkLdtB2YjHRx9_g0QWM0NQOpKM_pQqMjpQJsG8fgk54ipW5Vb1nD6cAmn_SLga1TrZsrRNDF82UgGHlDYM0qQ-5pmoMU6JJ2jMSSlm3adcTEGsAVFQfN9M4AMizzzQS0z-CT0jSyApIDj_fVsjGsUejHRNCPJc2bwtHMV_hRcQ4x-xNREwHa2Y-4D9xCgM8ZI0EdhpWRw8dHv_cQi440_gaOUwIKxUqmCMM940cTtlaRdqxdIXJZRfO8s0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه الحدث عربستان نیز اعتراف کرد جزیره استراتژیک پریم به کنترل انصارالله درآمده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/689003" target="_blank">📅 14:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFIwniBS9PN2V5K4LwqUaYxnA07luPKZqTwA_U_6eIzFsfZQZh20dKrlBGX05N7ZOwkWb7NCy7G2auiV48mFJjin0aD_IdyvvZO6GP2Ez6lXq9fggHiaVPHUshF04V3uIMIfQo9wQSP_07Em7JD8UseTi2UYhGuwNLDXizgbKIVM7IA7O1c4KYpeH_UIEllMmsLqlhLJFyH7uP5LzZI7Ny9rIUTRk6ezihq7WGHHoEbwK7664KvX1hWmEQNbnNMhx2mshoqbGq-xzxfwv7TvftpiwpQuCnomW1oFmRI73HobsNX_BfG0fP-zJK2jNSeiZtTI6YDZLY3UBLjamgcHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه را یهودی‌ها کشیدند، آمریکا اجرا کرد، تقصیر را انداختند گردن افغانستان و رسانه‌ها هم سناریو را نوشتند؛ تمام!
🔹
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2098341193172341123?s=46</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/689002" target="_blank">📅 14:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb2b81260.mp4?token=unBXAYKLX5tCIKkhV7XdPXteNiaWr9ZO9JnnB-MgeverloMYyIxp_YIgmizyQ8oxkUwDOsmx_ldFvyNRvax0nCAsjSgDzgL0YlKTISknoKvcfwmVa8fhZhM-_rGSgWJB-KcO6ejGmMkvHCz0Wp8XouNanUcd2-3KAUUyUtpIsyyGOf_zo-24_oxwWVakx_IT-aFtfask6xBbkqBZDa94Sf0dvYMMVOVNmDWIdf92kORbiqqT3x0PEJAneN5vzRQ-SRYhyN524GqEJAwRCxHA9ADRLLNM6sJ_PAjhFAi_wSbsNFECSCsePfEXvylGTOkx2W9AbJNgSmVNZnag15u8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb2b81260.mp4?token=unBXAYKLX5tCIKkhV7XdPXteNiaWr9ZO9JnnB-MgeverloMYyIxp_YIgmizyQ8oxkUwDOsmx_ldFvyNRvax0nCAsjSgDzgL0YlKTISknoKvcfwmVa8fhZhM-_rGSgWJB-KcO6ejGmMkvHCz0Wp8XouNanUcd2-3KAUUyUtpIsyyGOf_zo-24_oxwWVakx_IT-aFtfask6xBbkqBZDa94Sf0dvYMMVOVNmDWIdf92kORbiqqT3x0PEJAneN5vzRQ-SRYhyN524GqEJAwRCxHA9ADRLLNM6sJ_PAjhFAi_wSbsNFECSCsePfEXvylGTOkx2W9AbJNgSmVNZnag15u8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشخیص چای اصل و روش درست دم‌کردن از زبان چای‌فروش تبریزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/689001" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=PuwcNiKnOrkOYF-9z1JXs-DIWkhL3z_-vcysLJ83aoxWmjuTYGSF-gcTbzmjgpefobbHlTtKbY-juaqwE5ipZ3BMO3x5z2nQ0f6IMf4-uvqNF9CriEMPkRp7ewxATPTdVSMRDPXqjYZtP5G1rBl4RQaKH_ZS8veQArHlLc40GBiSG9pPI1kWz1-DZUUE85hdSboJdPYhRrKz7WHONcTie9PuVYUxZR1Pji4tGJE-OtxfgmFzyEePpRE_gD1i1oZn9dp94dQGJHazuvK3eJJJiSTeyPy4w529LD0tCpTK-UsGPd5R2lyKjBzezeh78uEHG4TjW5RTBJGaaZFbIqjv3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=PuwcNiKnOrkOYF-9z1JXs-DIWkhL3z_-vcysLJ83aoxWmjuTYGSF-gcTbzmjgpefobbHlTtKbY-juaqwE5ipZ3BMO3x5z2nQ0f6IMf4-uvqNF9CriEMPkRp7ewxATPTdVSMRDPXqjYZtP5G1rBl4RQaKH_ZS8veQArHlLc40GBiSG9pPI1kWz1-DZUUE85hdSboJdPYhRrKz7WHONcTie9PuVYUxZR1Pji4tGJE-OtxfgmFzyEePpRE_gD1i1oZn9dp94dQGJHazuvK3eJJJiSTeyPy4w529LD0tCpTK-UsGPd5R2lyKjBzezeh78uEHG4TjW5RTBJGaaZFbIqjv3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎉
فروش فصل پاییز شروع شد
🎉
جا نمونی !
🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
*
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه*
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/689000" target="_blank">📅 14:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688999">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای العربیه به‌نقل از منابع پاکستانی:تهران و اسلام‌آباد برای ازسرگیری مذاکرات و کاهش تنش در همه جبهه‌ها رایزنی کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/688999" target="_blank">📅 13:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688998">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90319df618.mp4?token=RVN3zXsWdYe9mezGgtu6nB7BPpMBp3gIDjq-lNEHZkv81aicsLav6KbC_z471JXcBWytqWo_8zFHx1Ym_griw8Rs8m9BF26MNXRXTeDFCdhxwZ3hEpGThDPGxMAtjxcWy10nHNtLtvE9lN4_ClnNfbw1PYwPnAPQRBei8YEA4XAKLCKa8ggMicLERg6tL2gcNIvPvvh3OtCs0M9QDZD8_JM81kp2Mxt98hJ10hKCatAMVSbovw1lGqOcFibmri6_gstnmCwCcWk3_LwwjixO0fRI_XWHKW2cTUlNV5U4njKtTfd1OsPpWSlgM7tsZHaD3U4PrApsSqGV4HkQe1bwp3r1Wh8mX-Q2nMSCgdUWSqrzGAEYtrPtGgNoZyJ7V6gHB8SP58EubDDBpUBrT03GTpkhwBhZr1Xp2SzgWhOcxG8I3mnJ6lT5bhZKGHF4dZNZHnwJOYTUIEf-iKiy7lEz5QMxfkxJrUisAHT8yvu3-YxI8eDipxaCcgRLEHaqpFBxeenl7BZfLkEt-jgmb4gA3jS7_dLRCVBEyiWJinQaFZCDjv3xdXpY0EQeysJ1ezvIdkRW9PgxdSvyJ4mn_f67EbJ_72EvkQ6V0ef9ocBb9a1jdRevWYIr9EzjqKbygWANZm4ftuv3cLH7VECtJE7n_Lseu6anj117QLsM5bm8kgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90319df618.mp4?token=RVN3zXsWdYe9mezGgtu6nB7BPpMBp3gIDjq-lNEHZkv81aicsLav6KbC_z471JXcBWytqWo_8zFHx1Ym_griw8Rs8m9BF26MNXRXTeDFCdhxwZ3hEpGThDPGxMAtjxcWy10nHNtLtvE9lN4_ClnNfbw1PYwPnAPQRBei8YEA4XAKLCKa8ggMicLERg6tL2gcNIvPvvh3OtCs0M9QDZD8_JM81kp2Mxt98hJ10hKCatAMVSbovw1lGqOcFibmri6_gstnmCwCcWk3_LwwjixO0fRI_XWHKW2cTUlNV5U4njKtTfd1OsPpWSlgM7tsZHaD3U4PrApsSqGV4HkQe1bwp3r1Wh8mX-Q2nMSCgdUWSqrzGAEYtrPtGgNoZyJ7V6gHB8SP58EubDDBpUBrT03GTpkhwBhZr1Xp2SzgWhOcxG8I3mnJ6lT5bhZKGHF4dZNZHnwJOYTUIEf-iKiy7lEz5QMxfkxJrUisAHT8yvu3-YxI8eDipxaCcgRLEHaqpFBxeenl7BZfLkEt-jgmb4gA3jS7_dLRCVBEyiWJinQaFZCDjv3xdXpY0EQeysJ1ezvIdkRW9PgxdSvyJ4mn_f67EbJ_72EvkQ6V0ef9ocBb9a1jdRevWYIr9EzjqKbygWANZm4ftuv3cLH7VECtJE7n_Lseu6anj117QLsM5bm8kgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت مرز بازرگان
/
تعدادی از هموطنان‌مان پشت مرز ترکیه ماندند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688998" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688997">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ابوترابی: وحدت ملی فتح‌الفتوح ایرانیان است
حجت‌الاسلام والمسلمین ابوترابی در خطبه‌های نمازجمعه تهران:
🔹
وحدت و اتحاد مستحکم ملت، هماهنگی میدان، خیابان، دیپلماسی و خدمت رمز اقتدار ایرانیان است.
🔹
امروز نقطه ثقل راهبرد دشمن پس از تجربه شکست در میدان نظامی و سیاسی بر هم زدن ثبات و کاهش تاب آوری ملّی است .
🔹
دستیابی به رشد اقتصادی پایدار از
مهم‌ترین ضرورت‌های امروز و فردای کشور است؛ ارتقاء سطح رفاه عمومی و افزایش قدرت خرید مردم مرهون تولید، صادرات و افزایش درآمدهای ارزی است با نگاه به این واقعیت انرژی از مهم‌ترین نهاده‌های تولید و پیش نیاز رشد و توسعه کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/688997" target="_blank">📅 13:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5b8d5aea.mp4?token=hd4q-QebjKdtOcvBR1qnzK59LMY_IbTlG8JxTvoItMupAKJFCSe4sG1K7DRRU2JCCUVnAzNk3tKK2FRPdvonK6BqRRog3x7xw0kt9AUUd29JYFyR26pEDDuWoxMVTwa4xMNpVzqRcxpoqrXE94ewqRcLLW39MhKh4iGkhOnnvQGteZ5J9S1pS_FmRHbCt3Y5HU6bbrO9tWT9c8OJOjpanC24JnCiEw2OC0Li_UGxOw64l3AkfJ7VjiRvh2y4-GhZLSx1hSJ0klBndvSqVp3hL0q4VZG0_-21W9K8vhKwYsHGBL-ZB5PJ8HaUiwx_ir7Z2Pg7p8dyPob-qRtqvRB60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5b8d5aea.mp4?token=hd4q-QebjKdtOcvBR1qnzK59LMY_IbTlG8JxTvoItMupAKJFCSe4sG1K7DRRU2JCCUVnAzNk3tKK2FRPdvonK6BqRRog3x7xw0kt9AUUd29JYFyR26pEDDuWoxMVTwa4xMNpVzqRcxpoqrXE94ewqRcLLW39MhKh4iGkhOnnvQGteZ5J9S1pS_FmRHbCt3Y5HU6bbrO9tWT9c8OJOjpanC24JnCiEw2OC0Li_UGxOw64l3AkfJ7VjiRvh2y4-GhZLSx1hSJ0klBndvSqVp3hL0q4VZG0_-21W9K8vhKwYsHGBL-ZB5PJ8HaUiwx_ir7Z2Pg7p8dyPob-qRtqvRB60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرایط عادی زندگی در صنعا، همزمان با تصرف کامل باب‌المندب توسط نیروهای ارتش یمن از زبان یک شهروند یمنی به زبان فارسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688996" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFZ84dqzVINcJWV--Obyl7h78hNfNCyMknW-S9np4xQ_BNkPNa3R5uLXD0XVtUpjpE6FRcIrf90Ti9gGlG5cxgLZ4UFpiXTKtAnPZmNPlvTJx4t5RZzL67xM5-cqg73SfuVZuwuNwKvNeE5CSQcTWJZenmq5xYFjCHImQ-4txlSERR7heFTkMAOxjeUo_k4HB462k-8TZqffMgGgJqygivkpLeVB2-_ooSmXJ5p2YWWwbxqVdQGEx-m3Mq6LrzNc3oHqW4k2d_pdZzwd4jmXWsfi2DCJEAc5WBUSlnxXWhA-ir4lf8ePXRAUu8WWQVIvaSi_ZH21af0IqGYOTZJUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nB2fNT6Z1QhyJf2LXnflMogSV9Vfe4zXXDYzJfD372nFzVHGdM9oAvFdjlYE0eeKsbyWJtBPLdIwhdLPhNnRVJRwkbb9qDclBdJ7fsrpP0EvrFYnG0L4qEMuzqT22V6EBlAjNZ7C6-Y2g6Zjy1KtZwA0HR32Eh1d3_MjhgGJH2bDCjbdKSWLbXmxM7b_KsI1sQwbc1rjMG6e-Lw5BHIQdc4wY_lTvH2W1RSRRDy5wHcDd8R1Zk8OkivX5VMEomsUcrFXAFrnNseHQwP7hef4sSFGZrg6kaaoCFz2oHuVvxsOdpQ1kHQNXr8Kv_QV_1_e4safAtG4OFcB2BPE07GLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYOOr-SIE8cUUAjV1ifncYaryTVWKUqEE_5lSOgHa_iyU0GWftDX6lkCYAZud6-pd-KLoAlbcgsjHs3Tj0fwfvMGIxSpyPOqt-Z9I7HfMVfesy3X_hh8q2scj7INbx5gsVdm2bv85QJqO80FFk6k9IF8bAFkvtHkORM2mqhe5nHOYQXcI2VLnsiRHlPNUyF-ulIah0c34tGdGsf7R7852Y6M9be1RAt1iu6VXGmNZw-6H9p54Yix-Z-Im891otkwzDQTmm_BSij3-hLoJUSE51ybDLNypNXdG534Mufh3jKYP_awKIJ5BWN4uzQcU2vOiVXDDHfncFtHUH4WEy19zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXb8vaaEycgF2IRBvBp7lEAiJczCXNPzfb9cB1hs7EuEAMRIm1XyXma0XJKR28X1SS_b8WxwMas2t6sGt93SExw59-LfKQLElonlq8icNBzlAHVhKiQR58ZKHjJmX1Uhm5aH2nBMfKb29a8Jw6hReP5HBXXXrHg-FgKcd4cPIzDeoXnzXMFM1MTJxiGewfxmhswou39LJSo0hTlPs_xkYGTKA1DLWtceFBkCts_mKq72Tmj_BC_UHGnoqGUAOxZhgJ0BGysawWQ1HIpKeXYCynuxQMQchqXkFshQgXOV18R1C0BtHLGlIRlBpEfmOU1BYs-9ga_3k_52OBnanIjOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deQGE-A6dO1xfGk8DV5j-YJ2AntBwh9syhNM5LK-1bUlSpzl5EyGA-cHmuDRQbEt-ajM9tAafHfOPplwYGhq7h_NXMdJW6X0qpw6MjqDl-JfhYyx4dG5n-yXz8OhWAkG0GgLkwGvx023CKSbYNJ4q1dnroNeRcmOOVJz7epuTXCOWOrRaBRXJYVpfO8JpUUFPIsMQy_4OA6-5MTAG-0y9_Y6SUbixJUtswzvz006nQakstE6RlF0-HOxldWfZ6HnsKtvwEVDIgTuRZqNI5q4Pjd-1nNaEef_LDIYZe_uPcbz4xgaKwURjipBG9W8xTKv8MiqKRKoP-rX2yd6ddsr8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نوشیدنی‌های عالی؛ جایگزینی برای نوشابه‌های مصنوعی و پر از قند
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688991" target="_blank">📅 13:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
لغو ناگهانی بازگشت صیادان ایرانی؛ امارات بدون ارائه دلیل مانع خروج شد. با وجود صدور بلیت و انجام هماهنگی‌ها، خروج صیادان هرمزگانی در آخرین لحظه متوقف شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688988" target="_blank">📅 13:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f35df25a1.mp4?token=pcDyS0P0XhM0ru9JE1MScKR1RZPDlob6ZmLST8XTyi5PWO6icnJzI5s-4alyiLE75IVlcCwTGXLxwEzAsrYLSEJoRQLaSvnsbql9pfHRZxGofbCf54bVcsmgI1OkQ6w8I0vL9wymDCU3eR9QKma6lEO0OAnmwVd-UAr3NvQd_KDJL0aMPB1fW3VkqQYkTko_RyMtJ8FsN_7wvNDDiO5MQEO-1LZ6zcp84K01Eh9M2yHlQuln-JSTOXfGk1y6fKGSUjGUJktTfndZKpkBbmEVZ5BTcK3z1pDmxX77GHW7LjrOv6IBQJxNtc44qAb17UexbM_Tr8BOwLsAqRYj5pKwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f35df25a1.mp4?token=pcDyS0P0XhM0ru9JE1MScKR1RZPDlob6ZmLST8XTyi5PWO6icnJzI5s-4alyiLE75IVlcCwTGXLxwEzAsrYLSEJoRQLaSvnsbql9pfHRZxGofbCf54bVcsmgI1OkQ6w8I0vL9wymDCU3eR9QKma6lEO0OAnmwVd-UAr3NvQd_KDJL0aMPB1fW3VkqQYkTko_RyMtJ8FsN_7wvNDDiO5MQEO-1LZ6zcp84K01Eh9M2yHlQuln-JSTOXfGk1y6fKGSUjGUJktTfndZKpkBbmEVZ5BTcK3z1pDmxX77GHW7LjrOv6IBQJxNtc44qAb17UexbM_Tr8BOwLsAqRYj5pKwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی برج‌های دوقلو با ۲۹۹۷ پهپاد نورانی
🔹
پهپادها ابتدا به صورت مارپیچ در هوا پرواز کردند و سپس به صورت گروهی از آسمان‌خراش‌های ویران شده درآمدند. تعداد پهپادها با تعداد قربانیان حمله تروریستی مطابقت داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/688982" target="_blank">📅 13:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
الجزایر روابط با امارات را قطع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/688981" target="_blank">📅 13:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e952a2f5b6.mp4?token=qpnCE2GsL1v6SQkqKNS4wgIfR3I-qQ-yY-ge6bdxscGWwy_tpfySE10jYyrL5awQGc5vBAOMq6KR10KYdW5Qe4X8PBtx4sXU5ywgIbGYVpLtH8YzqZQwuqL14kcj9BvhljJ8FSvPnwcuucVthwg7P8s-qWskHiD-Y5bneCQtNDxz2-7ABJl4fh9hLl56B_Z3-L_NLckOX_JHXBoR_13ieosMZRSzgN7IQ3yqvC98psqH3YKTr331A1f-Mb2H5NlzWfWkeFS2Zoej-etHotN_OiRPWj99QDbMw6MjCK0xCsQRpOP1nn5N6CUmeOLlQfX4_pdRYL7miU8QDOlBzAPgAZEzuayEcI9OxLlcHLJb6Utlm_Bnky38Di-bf7RwPfAx3rZtz3g-_rQcvwBewpYRjWr6WAHFszAJQcY0Oyj6FjiTF2aeeeC_aRIc81Lhf_gvdkZEbMfc74x-O5Ci52Y4XFcD-a_YpBpicxRYnb52fSKblFulyTc-YUrHaTRskKpzUYcGcdHLGfAeEi0viS7p5VN0yVPI-XLDpZ-Tj0j9YdgUW8jXCFjurjMuHjEOaFYBJuPtMbaEXPkMSvsR1rhNKUtARjcLU7Kxyc-tz5K7yL_x5k42e7gF5XX8yRrYtwYJtGtZ6Y2rarCIqci4WKKWZqyEJqFdtwDVOXUa3ga9aYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e952a2f5b6.mp4?token=qpnCE2GsL1v6SQkqKNS4wgIfR3I-qQ-yY-ge6bdxscGWwy_tpfySE10jYyrL5awQGc5vBAOMq6KR10KYdW5Qe4X8PBtx4sXU5ywgIbGYVpLtH8YzqZQwuqL14kcj9BvhljJ8FSvPnwcuucVthwg7P8s-qWskHiD-Y5bneCQtNDxz2-7ABJl4fh9hLl56B_Z3-L_NLckOX_JHXBoR_13ieosMZRSzgN7IQ3yqvC98psqH3YKTr331A1f-Mb2H5NlzWfWkeFS2Zoej-etHotN_OiRPWj99QDbMw6MjCK0xCsQRpOP1nn5N6CUmeOLlQfX4_pdRYL7miU8QDOlBzAPgAZEzuayEcI9OxLlcHLJb6Utlm_Bnky38Di-bf7RwPfAx3rZtz3g-_rQcvwBewpYRjWr6WAHFszAJQcY0Oyj6FjiTF2aeeeC_aRIc81Lhf_gvdkZEbMfc74x-O5Ci52Y4XFcD-a_YpBpicxRYnb52fSKblFulyTc-YUrHaTRskKpzUYcGcdHLGfAeEi0viS7p5VN0yVPI-XLDpZ-Tj0j9YdgUW8jXCFjurjMuHjEOaFYBJuPtMbaEXPkMSvsR1rhNKUtARjcLU7Kxyc-tz5K7yL_x5k42e7gF5XX8yRrYtwYJtGtZ6Y2rarCIqci4WKKWZqyEJqFdtwDVOXUa3ga9aYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادلات در یمن چطور در حال تغییر است و چه تاثیری بر نبردهای منطقه دارد؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/688980" target="_blank">📅 13:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5938cb26c9.mp4?token=ZW4hnWAd-NmiR0b_V5mBm4Y66LTNyuYVOclyrhPClrzrW97nwBdyFYFKvFU0D0zqB1xODuecfTZRFDCvna1SBulhMpFordvzojr3n5HW1FGCf943s-5UCo2YOjJ4F4N7EsqcuQ7mk8Z_rElf7bZVRPdCuPvvXSg9iDbRcatmkD5peYkpfpdgM9BAO_jtdqLQfW1sVrKphVBkP-912mt8_CxvtWetTYGyYbrE2Zk0t67f9PVJypN8ckNKVex-IhxjRPMh8SkJtsIOf_Ae6S3f3xke1QpcdRPqTR7AaD_IEDY-U8n07veY-MzawM93MM1PBFmq5rEoYy82vSBq9jFo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5938cb26c9.mp4?token=ZW4hnWAd-NmiR0b_V5mBm4Y66LTNyuYVOclyrhPClrzrW97nwBdyFYFKvFU0D0zqB1xODuecfTZRFDCvna1SBulhMpFordvzojr3n5HW1FGCf943s-5UCo2YOjJ4F4N7EsqcuQ7mk8Z_rElf7bZVRPdCuPvvXSg9iDbRcatmkD5peYkpfpdgM9BAO_jtdqLQfW1sVrKphVBkP-912mt8_CxvtWetTYGyYbrE2Zk0t67f9PVJypN8ckNKVex-IhxjRPMh8SkJtsIOf_Ae6S3f3xke1QpcdRPqTR7AaD_IEDY-U8n07veY-MzawM93MM1PBFmq5rEoYy82vSBq9jFo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه به شهادت رسیدن ۲ نیروی حزب‌الله که از یک حفره زیرزمینی در ارتفاعات «علی‌‌الطاهر» درحال جنگیدن با ارتش تروریستی اسرائیل بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688979" target="_blank">📅 13:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/688978" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBNKvHubR-ptM4xnNNiHxaRk0TzsQDJLWKzdHEUtmDuI0rrqjqLMadjiZl6rm-BfBRS81ZSivwKq9cuxXe4p7M6NWL4CbyDLXpYsFBxYRZWkDjTnf3L9MrDRj1JxdrEpNj3fmt2Wb3q2aC_Z6G7dmwNv4jjRx8m_5CFJ5eURTuWSPbOQSw-zam_oyVsnY4oKwISE6k7ROOONIGYenIEuscuC8FMkJj22rjbwmdjEHgJDLwgmNUWQK2zd4RzZx69GkNSU5cxE6qwndkHZcaL-4VFuSXMsMB_xMFX6iWviJr9ZruOKP65kBeNpdE7-ohmkDhciKsV6Xb05fDduk9Q2nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام امکان نمایش پست‌های تگ‌شده در صفحه اصلی پروفایل را فراهم کرد
🔹
قابلیت جدید اینستاگرام به کاربران امکان می‌دهد پست‌هایی را که در آن‌ها تگ شده‌اند، به صفحه اصلی پروفایل خود اضافه کنند. این پست‌ها بدون ایجاد نسخه جدید، همان محتوای اصلی را نمایش می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688977" target="_blank">📅 13:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
♦️
۴
جان‌باخته تجمعات مشهد با دستور رهبر انقلاب، شهید محسوب شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688976" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اقتصاد ایران بیشتر از دوره ترامپ دوام می‌آورد
🔹
فارین پالیسی نوشت: اقتصاد ایران ممکن است از ریاست‌جمهوری ترامپ بیشتر دوام بیاورد/ تهران مقاوم، ابزارهای فراوانی برای تاب‌آوری اقتصادی دارد
نشریه امریکایی فارین پالیسی در آخرین مطلب خود نوشت:
🔹
با وجود آنکه مشکلات اقتصادی ایران روزبه‌روز آشکارتر می‌شود، واقعیت میدانی نشان می‌دهد که اقتصاد ایران، علیرغم همه آسیب‌ها، همچنان ایستادگی می‌کند و سناریوی فروپاشی قریب‌الوقوع، بیش از آنکه مبتنی بر واقعیت باشد، حاصل محاسبات اشتباه کاخ سفید است.
🔹
فارین پالیسی اضافه می‌کند: تجربه‌ سال‌های تحریم نشان داده که اقتصاد ایران توانایی شگفت‌انگیزی برای جذب شوک‌ها و تطبیق با شرایط جدید دارد.
🔹
شبکه‌های گسترده‌ تجارت رسمی و غیررسمی، تنوع‌بخشی به تولید داخلی و سازوکارهای تأمین اجتماعی، چتر حمایتی را گشوده‌اند که اجازه نداده قفسه‌های فروشگاه‌ها خالی شود و معیشت پایه‌ای مردم از هم بگسلد.
🔹
ذخایر ۴۵ میلیارد دلاری طلا، درآمدهای نفتی فراتر از سال ۲۰۲۰ و تنوع جغرافیایی ایران، عوامل کلیدی‌ای هستند که اقتصاد را در برابر محاصره مقاوم نگه داشته‌اند.
🔹
حاکمیت همچنین با تکیه بر تجربه‌ مدیریت نقدینگی، بازار ارز و واردات در شرایط جنگی، می‌تواند فروپاشی را در ماه‌های پیش‌رو مهار کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688975" target="_blank">📅 13:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a30512e6.mp4?token=vJesbQXGfQVRId7Vx5Uk5XVyOkKKTMLsqyBYueCEzkA236PdgeGUXjGyf6kgQWS1A6ykpG7kFZKcR-MjR8B3nU4CZOKx74lqWkJWYDnYFUKH75YED1KgAnX1r93GOef6IXGf1pR5ckOAWE0NdjM7SYYVqZ__QrzTnnh8COdfZKOWKrLS9D0_shL1fqo61ue2D-1qGXOPgnLxJgPw8I-c1-HSyrOF8ZMBrE661hqCKgM8X7BkihG2PQHiKAme6a1RInqqxs-UrgUtF_-pQhOSTEpyb5YkOZTeeeUjNyZ95PJutxzZ9z6FElGc9s9hZ0dMJw-MFek0xqq4pn0BlLcHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a30512e6.mp4?token=vJesbQXGfQVRId7Vx5Uk5XVyOkKKTMLsqyBYueCEzkA236PdgeGUXjGyf6kgQWS1A6ykpG7kFZKcR-MjR8B3nU4CZOKx74lqWkJWYDnYFUKH75YED1KgAnX1r93GOef6IXGf1pR5ckOAWE0NdjM7SYYVqZ__QrzTnnh8COdfZKOWKrLS9D0_shL1fqo61ue2D-1qGXOPgnLxJgPw8I-c1-HSyrOF8ZMBrE661hqCKgM8X7BkihG2PQHiKAme6a1RInqqxs-UrgUtF_-pQhOSTEpyb5YkOZTeeeUjNyZ95PJutxzZ9z6FElGc9s9hZ0dMJw-MFek0xqq4pn0BlLcHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مهیب در مدرسه‌ کنگو/ ۲۶ دانش‌آموز جان خود را از دست داده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688972" target="_blank">📅 13:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شرایط قانونی دریافت خسارت تأخیر تأدیه چیست؟
🔹
نخست اینکه موضوع تعهد، پرداخت وجه رایج باشد. دوم اینکه طلبکار، طلب خود را از مدیون مطالبه کرده باشد. این مطالبه می‌تواند به شکل رسمی، مانند ارسال اظهارنامه یا طرح دعوا، یا در مواردی به شکل غیررسمی انجام شود؛ برای نمونه، پیامک، ایمیل یا سایر ادله‌ای که بتواند مطالبه طلب را اثبات کند. حتی مطالبه شفاهی نیز در صورت امکان اثبات، می‌تواند مورد استناد قرار گیرد.
🔹
سومین شرط را تمکن مالی مدیون و امتناع او از پرداخت می‌باشد؛ اگر مدیون توانایی پرداخت نداشته باشد، نمی‌توان صرفاً به دلیل عدم پرداخت، خسارت تأخیر تأدیه را به او منتسب کرد.
🔹
شرط دیگر نیز این است که شاخص قیمت‌ها بر اساس شاخص اعلامی بانک مرکزی تغییر کرده باشد؛ به‌گونه‌ای که شرایط مقرر قانونی برای تعلق خسارت تأخیر تأدیه فراهم شود./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688971" target="_blank">📅 13:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25559859ad.mp4?token=YuoOG6EOg-bY7fupBpV1auXbXMGBGr68bco0EvsRnnelx0hJ2gDrEaQkH8Wi_EWey6vgEOS6nsUWUakfZ-4saSur4uJRv5Ci8kHTMl9zdtfXh08lOqjE1pryc2wx0HPN2fAptiE6TK7JLMGUjbqT7st7d1USQV3p3h4_505xemvGG7rlxCJM5hFzPydeDijTzr6RcbR4wASYMkxB_Un-OFKLzEX3rYp35X_qxnoT46LQJOAwHT39GIyXXYhpn5mUkPqlDJ0dh1IQhiQ6V26VzUjMZuixsHUWWjH_fHA-uhbNKAOHENDnCRBlqVhj3TVaIwjetITxxymxzLq7cfW5IYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25559859ad.mp4?token=YuoOG6EOg-bY7fupBpV1auXbXMGBGr68bco0EvsRnnelx0hJ2gDrEaQkH8Wi_EWey6vgEOS6nsUWUakfZ-4saSur4uJRv5Ci8kHTMl9zdtfXh08lOqjE1pryc2wx0HPN2fAptiE6TK7JLMGUjbqT7st7d1USQV3p3h4_505xemvGG7rlxCJM5hFzPydeDijTzr6RcbR4wASYMkxB_Un-OFKLzEX3rYp35X_qxnoT46LQJOAwHT39GIyXXYhpn5mUkPqlDJ0dh1IQhiQ6V26VzUjMZuixsHUWWjH_fHA-uhbNKAOHENDnCRBlqVhj3TVaIwjetITxxymxzLq7cfW5IYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از طوفان شدید در ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688969" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688968">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4904b61bd.mp4?token=P_VsTRh7IscZmvjfSejh_vQe_7uFjK_Cpl9hmQTK2xVV7ik25ygnbxRU-SNuvQdm-Kt7PYi4fltUgUGJK7MVG4SUa1_FZzRRGmRfh3coTszxna_3htNzI672Yl_T7RMKibXZogzh2SDcAMdVPxWRTX_DMdqfZNSUvCDmVIh6xZwQatLwVbk4xSi80NhH_qhhHQrWmNvcc9fuOcjer6aWCncK-l1GHIfUfc6yWfL_kdRfUZeMRRt97mC1rStSc7EwoSK7NdI5k9dUxiHPmartLyQZSLv4jV0l-Ol6eZii5B1jXl7Izr59Nv7dBUOAPLUcQ64yhbwRDQ5RU8q_icbkkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4904b61bd.mp4?token=P_VsTRh7IscZmvjfSejh_vQe_7uFjK_Cpl9hmQTK2xVV7ik25ygnbxRU-SNuvQdm-Kt7PYi4fltUgUGJK7MVG4SUa1_FZzRRGmRfh3coTszxna_3htNzI672Yl_T7RMKibXZogzh2SDcAMdVPxWRTX_DMdqfZNSUvCDmVIh6xZwQatLwVbk4xSi80NhH_qhhHQrWmNvcc9fuOcjer6aWCncK-l1GHIfUfc6yWfL_kdRfUZeMRRt97mC1rStSc7EwoSK7NdI5k9dUxiHPmartLyQZSLv4jV0l-Ol6eZii5B1jXl7Izr59Nv7dBUOAPLUcQ64yhbwRDQ5RU8q_icbkkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گره طناب برای بکسل‌ کردن؛ روشی ساده برای مواقع ضروری
🪢
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/688968" target="_blank">📅 12:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688967">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy4CfZCNcsFtjhiRwFhcPw8U5UX92R-VO_MiHI5bZhy6b_vrLOFR3COqQpw4A71sIaDYrXpJpz73XKKh0g3pHr5-8J1Ux0g7eIM37nSjMCqF4UceblfKSwincrXGo5KnPaYYVOALGla2KNLUPEd5gPt6pjEKQHEU_iv86-W_DJzrDNa8j94C0S9uBi3JdmO_R6qqV-MqBRpZdwvwRv_amtBTA6t2jUc8Aut_uD8l9sQzd45uO0esSpL8yzKW6nDr9iwUq3Cp0BEMKlswRJzowBjBhwMLdLy-2uP-Vq_BDKSfq3eQAVFkR5K85zfWL2SG5JOevzAXIRR3pdNe8V_0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پک ویژه «علوی»؛ سه تکه از بهشت، همراه شما
نجف، نه فقط یک نقطه روی زمین، که نقطه‌ی آغازِ دلدادگی است…
برای آن‌هایی که دلشان در ایوانِ طلا جا مانده، یک مجموعه اختصاصی از عطر، نور و غیرت حیدری آماده کرده‌ایم. مجموعه‌ای که با عشق در کنار هم چیده شده‌اند تا عطر و نام مولا، پیوسته همراه روزها و خلوت‌هایتان باشد.
✨
محتویات پک اختصاصی علوی:
▫️
مهر تربت بوتراب: خاکی متبرک برای زلال‌ترین سجده‌ها
▫️
عطر حرم امیرالمؤمنین (۲۰ میل): یادآور نسیم سحرگاهی ایوان نجف
▫️
گردنبند ذوالفقار: نشانه‌ای از اقتدار، اصالت و پیوند با نام علی (ع)
💰
جمع کل در خرید تکی: ۱,۳۲۴,۰۰۰ تومان
🔥
قیمت ویژه کل پک: ۱,۱۱۰,۰۰۰ تومان
⏳
موجودی این پک کاملاً محدود است.
📩
ثبت سفارش و مشاوره:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/688967" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551a668ee8.mp4?token=LkXStghObzNPfb9HOhIMCnI-Po977FpIbD31b2clds9Q82Lw0cOwHn3DqQg4RGMO6EbfOOsd-WS0wfwB8Yj-bqJ_gp4RSN-NM_8fKBnna7wXdJR_PzIfARiC46-TdxRhbFCso5_I3rodC8pIwCAVML8oW6PmmTlX2lp0Rfv7XdyEh2SA-3I3c3p_buDCMolj6vEMUMU2BdqvCrDxDKR7DbV98H2SaoQI7jLiBMKGIIb7bEixPtHeSMSfg6CguliZdDQ-byANZD8THX1Rz42Wb9HGnJ5FFTc0oNS1g8hn3s-QvA88d_wRv5mRY0lffiQG9FlrXOPCBpn6vo4j3qbcnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551a668ee8.mp4?token=LkXStghObzNPfb9HOhIMCnI-Po977FpIbD31b2clds9Q82Lw0cOwHn3DqQg4RGMO6EbfOOsd-WS0wfwB8Yj-bqJ_gp4RSN-NM_8fKBnna7wXdJR_PzIfARiC46-TdxRhbFCso5_I3rodC8pIwCAVML8oW6PmmTlX2lp0Rfv7XdyEh2SA-3I3c3p_buDCMolj6vEMUMU2BdqvCrDxDKR7DbV98H2SaoQI7jLiBMKGIIb7bEixPtHeSMSfg6CguliZdDQ-byANZD8THX1Rz42Wb9HGnJ5FFTc0oNS1g8hn3s-QvA88d_wRv5mRY0lffiQG9FlrXOPCBpn6vo4j3qbcnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید اسرائیل از سوی عضو هیأت‌ رئیسه مجلس
علیرضا سلیمی:
🔹
ایران همواره پشتیبان مقاومت بوده و خواهد بود.
🔹
نیروهای صهیونیستی حرارت آتش اقدامات ایران را خواهند چشید./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/688966" target="_blank">📅 12:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688964" target="_blank">📅 12:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
پزشکیان: به جلیلی گفته‌ام هر کجا که می‌تواند، اختیار می‌دهم مشکلات را حل کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688963" target="_blank">📅 12:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837de8e830.mp4?token=NOVgGWnh0K5KS9RhaUVazKEURJ-cJJZViOl_Q5D8cT3_GudFnYsIgWW2wehHepCihYrXmtxzHlIbXGxgQLRu26wP7osn1zNglVd1I72WA2qvysUMQX_vhTAO9ta4yU2WCtBlaUM5U_40i_TV2lXADFhJLBKrmzsGVsAk1GjqTVXMgPYCCZFORHokZDf1-EpScnc-NYF-L_iPQD-1wzX1xmy1apuNhGhNiU9QDV-p_90ae_Si6K6M-UyrSUo2IP7jN7mxxX4bJ4GS2iN7FtOaZVOuqj6uVhgHHWv3n2Ak7uDoKxsT_L3g10tn9VII-itCYUODVFNCpKCyKh0GlAe3NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837de8e830.mp4?token=NOVgGWnh0K5KS9RhaUVazKEURJ-cJJZViOl_Q5D8cT3_GudFnYsIgWW2wehHepCihYrXmtxzHlIbXGxgQLRu26wP7osn1zNglVd1I72WA2qvysUMQX_vhTAO9ta4yU2WCtBlaUM5U_40i_TV2lXADFhJLBKrmzsGVsAk1GjqTVXMgPYCCZFORHokZDf1-EpScnc-NYF-L_iPQD-1wzX1xmy1apuNhGhNiU9QDV-p_90ae_Si6K6M-UyrSUo2IP7jN7mxxX4bJ4GS2iN7FtOaZVOuqj6uVhgHHWv3n2Ak7uDoKxsT_L3g10tn9VII-itCYUODVFNCpKCyKh0GlAe3NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند ساده برای آشپزی بهتر و راحت‌تر
✨
🙂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/688962" target="_blank">📅 11:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrR9I5AmkkdJjgTPVTAgPgKevVl-3J6RBPQGPJupBvBjurcrzx_LXxQ8E96DZ7lydggX3PzOOuErbHVELBo44Pfh1bnFOR-04JSPbx7Ur1OMdwkvzWMeTqeWoLHBLWq1y4gqu-vD3eBtBXH2qkFEjEzycMK_ORsL_LPzXRZHZV0HXZVvVnf6kUGwNla9rtIAFHAARyimTp4YgAqU_8zZ6f0L05cYgHowEmJAc94JzlmqSI1-JlE7HC6UTUOHZ_AVjJRmtGq7tY4LhRGKjUhM2H9QeebITaPC0kkmo3dB83i0B-C-rTzTH2_Is1EeUSduSiDtXUA1uD0rCUpEPuqRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ پایان ست سوم
🔹
ایران ۲ - ۱ چین تایپه
🇮🇷
۲۵ | ۲۵ | ۲۱
🇹🇼
۱۹ | ۱۹ | ۲۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/688961" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688959">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
سخنگوی هیات رئیسه مجلس: ادعای افزایش ۵۰ درصدی حقوق نمایندگان کذب است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/688959" target="_blank">📅 11:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
سخنگوی فدراسیون فوتبال: برگزاری بازی‌های فوتبال، بدون تماشاگر ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688957" target="_blank">📅 11:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
همه‌چیز درباره بریکس / در هند چه می‌گذرد؟ / قدرت‌نمایی منهای آمریکا
🔹
این روزها نگاه‌ها به هند است، کشور میزبان اجلاس گروه بریکس که اتحادی به‌دور از قدرت‌های غربی را تشکیل می‌دهد. از پوتین تا پزشکیان مهمانان این اجلاس هستند و موضوع ایران احتمالا داغ‌ترین بحث در جلسات سران کشورهای عضو.
در این‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3243892</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/688956" target="_blank">📅 11:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ پایان ست دوم
🔹
ایران  ۲ - ۰ چین تایپه
🇮🇷
۲۵ | ۲۵
🇹🇼
۱۹ | ۱۹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688955" target="_blank">📅 11:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6902f42c.mp4?token=q8DK6CHa3ixNXr1OW6fX7jcjXLkTZgE1Ap97c1Nn90u-6OdaXkxkO59QnRE_Wnk4mBDQM3zBQutjOgGUVxIJ3Eq8E1o2G2hqWXzSt2hKMk7Zpic0J1dJvm7hShcqKxKJ3vQ_tfW0cjXtW8AOocXxMo5EzDe1ZGaCk4HDRRQr23Dr_W53w94NtUCkrOzO6QqWSl5K_RIAe4bBU0n6i5rPiXC-lktPlUJWjf7NtKQfheCeb7YD-N7uyReEdvFEVpS90eQlPQc_l8hxEJNODzlmvfWA4GecpFbxUee44CSy-tOCi80w2XkuR5K23vGXtN5-IDJntqJiPGInsP8R4rzo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6902f42c.mp4?token=q8DK6CHa3ixNXr1OW6fX7jcjXLkTZgE1Ap97c1Nn90u-6OdaXkxkO59QnRE_Wnk4mBDQM3zBQutjOgGUVxIJ3Eq8E1o2G2hqWXzSt2hKMk7Zpic0J1dJvm7hShcqKxKJ3vQ_tfW0cjXtW8AOocXxMo5EzDe1ZGaCk4HDRRQr23Dr_W53w94NtUCkrOzO6QqWSl5K_RIAe4bBU0n6i5rPiXC-lktPlUJWjf7NtKQfheCeb7YD-N7uyReEdvFEVpS90eQlPQc_l8hxEJNODzlmvfWA4GecpFbxUee44CSy-tOCi80w2XkuR5K23vGXtN5-IDJntqJiPGInsP8R4rzo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب گلس با دستگاه مخصوص؛ روشی متفاوت برای نصب دقیق و بدون حباب
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/688954" target="_blank">📅 11:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688953" target="_blank">📅 11:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d286b54d.mp4?token=cUWo_5ZGVswrg0Sv2FUbmktvJ-VvAbMVv_h3CWrSbptAojVyNF5wvTsZI8CjNNK3eBs-OmEM2ldQo-n-XzDP4dBEj8SME7NZ_dep9NP3PvW1o2Ms-Du2PlW8M1ELVHGd7O_Be0FOtdzgKLRDMbI0hFx3JvbzZEF_wepgCcIbzsBjE0hL-SFu1gkbb5gsNmS_n7dMvtUT9g2Vk_6d7_UnthIia1j0RjxzCA7Er5Ql1irMUepPfnoRQ-J1UEPDD1tLJMDjY5H2btrrX08daz-gYf1Q9NovNTOJ5ZVfZHBxWVW51ptsoEy-YE4wwU2y0-4J5Mnet8gFpux2Bg-MGynw-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d286b54d.mp4?token=cUWo_5ZGVswrg0Sv2FUbmktvJ-VvAbMVv_h3CWrSbptAojVyNF5wvTsZI8CjNNK3eBs-OmEM2ldQo-n-XzDP4dBEj8SME7NZ_dep9NP3PvW1o2Ms-Du2PlW8M1ELVHGd7O_Be0FOtdzgKLRDMbI0hFx3JvbzZEF_wepgCcIbzsBjE0hL-SFu1gkbb5gsNmS_n7dMvtUT9g2Vk_6d7_UnthIia1j0RjxzCA7Er5Ql1irMUepPfnoRQ-J1UEPDD1tLJMDjY5H2btrrX08daz-gYf1Q9NovNTOJ5ZVfZHBxWVW51ptsoEy-YE4wwU2y0-4J5Mnet8gFpux2Bg-MGynw-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرایی ترور علی لاریجانی از زبان رئیس سابق MI6
جان سائرز:
🔹
علی لاریجانی عامدانه توسط اسرائیل ترور شد چون تهدیدی محسوب می‌شد و تنها فردی بود که می‌توانست به توافق صلحی برسد که برای هر دو طرف قابل قبول باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688952" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d4f91d52.mp4?token=U9KRWH4HxMsb9dtBaLf-kl2wa7b6_JPngeGeGgE_DYTaV2rXZRtpAiiRVdMxFDYDXhTgMzZ05fTRIJhWsV10Lsmp05HDaq0chya3zbCFV0S55t0x7Pk683m6r1UdBr0Z_2QvSu76VYEw0a0_-aewTpyMS0QeVSSqtngDPPdYvSAuIj4UZuLWnLWoDv--WPJ1uiTWnJdqF8ETEecQBAFmRLw36T5vPJM6cLcMmK6Iy8v_zOxY92h-tc_BYltmjgeIBPihGm_G1JIIGjmcUW0yXYUZJvehNcgAc9wubRhz1Bo6YHgAFynu0BpfHm3rCnJivsyQI94aL-45DO22JtO3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d4f91d52.mp4?token=U9KRWH4HxMsb9dtBaLf-kl2wa7b6_JPngeGeGgE_DYTaV2rXZRtpAiiRVdMxFDYDXhTgMzZ05fTRIJhWsV10Lsmp05HDaq0chya3zbCFV0S55t0x7Pk683m6r1UdBr0Z_2QvSu76VYEw0a0_-aewTpyMS0QeVSSqtngDPPdYvSAuIj4UZuLWnLWoDv--WPJ1uiTWnJdqF8ETEecQBAFmRLw36T5vPJM6cLcMmK6Iy8v_zOxY92h-tc_BYltmjgeIBPihGm_G1JIIGjmcUW0yXYUZJvehNcgAc9wubRhz1Bo6YHgAFynu0BpfHm3rCnJivsyQI94aL-45DO22JtO3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لباسشویی سنتی در رومانی؛ شست‌وشوی لباس‌ها با جریان طبیعی آب!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688951" target="_blank">📅 10:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ پایان ست اول
🔹
ایران  ۱ - ۰ چین تایپه
🇮🇷
۲۵
🇹🇼
۱۹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688950" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688949" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cic24i0ql5n61-i9eI9S3HYN9HqhpC-Fv1CMaMtjDmF0c9L4m6sZ1jrD8yYigKe8Gc4dRY2_YwFEn_Jgml4VZLvsVE2KwwhNiBhZFj7gqzb3pJhxJi2qe6IjGguEJTULvcAQ5PC5y18dwqcLXXy4TlUCUMvOD6LpoxV4-CllcQ7zFUknUPrZm47qvsL1dP7JBZpcYKTy9h3v4cNEI8-D4Jql7mprlXzfOHEwQed-G6sFElmkz-wv6qckbDuZ1r78nwr7KW-Bte-LIoMR767Le7P9_n9eaT11VYgGBj_ksaeYsgUjqFypz_t38yVmCjSftBSQULfbdkT5X05_SJOkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ مدل نوشیدنی خوشمزه با هویج
🍹
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688948" target="_blank">📅 10:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ پایان ست اول
🔹
ایران  ۱ - ۰ چین تایپه
🇮🇷
۲۵
🇹🇼
۱۹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688947" target="_blank">📅 10:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای جدید ترامپ: هیچ هواپیمای نظامی آمریکایی در حمله ایران به پایگاه هوایی در اردن آسیب ندیده است
🔹
در حالی ترامپ این ادعا را مطرح می‌کند که شبکه خبری سی‌بی‌اس آمریکا از خسارت گسترده به تجهیزات نظامی این کشور در جریان حمله موشکی ایران به پایگاه هوایی «موفق…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/688946" target="_blank">📅 10:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
پزشکیان: بسیاری از ساختمان‌های دولت از جمله سعدآباد را در زمستان تعطیل می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688945" target="_blank">📅 10:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0ba2da91.mp4?token=TCBPxNkmoy7sdre_zJl5ppXNzLPkjLskcxQK3fA8Jqtxqfvn87W1gLPz6aM8dpexXwW1BTZ52ubRjjzhc5NM-CgniAGyqUvxCbDmf39fju0wk9X3X3-0DGzKWRlAd6nkW0TXRukeE2Vp4Mbt9ErTcu-HCSY3WYCZXRUet4iCWhZtIrd4nO7y2Svp0-7B_arBT47HoTpOeSlihY4NKU7QgpfuBluKTBBk1inAwoai3AHZ-8-ol9U7fBCcPfyPi3e3n9fRgRnwLINto5R5OaN2Awk-3b3s-FKFgaHpAAbehqV50fpOZGT57am2YEvKBV7f-5BxalK58vlxeMxdD4kfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0ba2da91.mp4?token=TCBPxNkmoy7sdre_zJl5ppXNzLPkjLskcxQK3fA8Jqtxqfvn87W1gLPz6aM8dpexXwW1BTZ52ubRjjzhc5NM-CgniAGyqUvxCbDmf39fju0wk9X3X3-0DGzKWRlAd6nkW0TXRukeE2Vp4Mbt9ErTcu-HCSY3WYCZXRUet4iCWhZtIrd4nO7y2Svp0-7B_arBT47HoTpOeSlihY4NKU7QgpfuBluKTBBk1inAwoai3AHZ-8-ol9U7fBCcPfyPi3e3n9fRgRnwLINto5R5OaN2Awk-3b3s-FKFgaHpAAbehqV50fpOZGT57am2YEvKBV7f-5BxalK58vlxeMxdD4kfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مستندی درباره فلسطین در جشنواره ونیز رکورد تشویق را شکست
🔹
مستند «NAZA» رکورد تاریخ جشنواره ونیز را با ۲۵ دقیقه تشویق ایستاده شکست. «نازا»، درباره نسل‌کشی اسرائیل در غزه ساخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/688944" target="_blank">📅 10:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تمدید دسترسی رایگان ماهواره‌ای آیفون
🔹
اپل قابلیت‌های ماهواره‌ای از جمله پیام و تماس اضطراری را برای کاربران آیفون‌های سری ۱۴، ۱۵ و ۱۶ یک سال دیگر رایگان نگه داشت؛ هزینه پس از پایان دوره هنوز اعلام نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/688942" target="_blank">📅 10:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688940">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دپوی شیرخشک و کره در کشور/ انجمن تولیدکنندگان شیرخشک: ۴۰ تا ۵۰ هزار تن کره در کشور دپو شده است
سیاوش سلیمی، رئیس انجمن تولیدکنندگان شیرخشک صنعتی در
#گفتگو
با خبرفوری:
🔹
حدود سه برابر نیاز داخلی در کشور، ظرفیت صادرات شیرخشک داریم اما به دلیل افزایش قیمت شیر خام و بالا رفتن قیمت تمام شده، این محصول دیگر قابلیت رقابت مناسب در بازارهای منطقه را ندارد و صادرات آن با مشکل مواجه شده است.
🔹
در پی این مشکل، بخشی از شیرخشک تولید شده در کشور دپو شده و از سوی دیگر، جنگ باعث از دست رفتن بخشی از بازارهای جنوبی کشور و کاهش تقاضا شده است.
🔹
همچنین حدود ۴۰ تا ۵۰ هزار تن کره نیز در کشور دپو شده که این حجم از موجودی، پرداخت مطالبات دامداران را با مشکل مواجه کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688940" target="_blank">📅 10:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688939">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3f719970.mp4?token=ABVyEXlTAd6Ghl-skeAp643ZCtNGxdfeeLtazNKrGtgZ_qMsZzJoW0T2RZhdQ6CTourjwIHQhdNkVRd5fT2WiVp12HprHmNbMN_4dhZBiXP4U_yOzZ-W1AQWH2cS-TUxGtGKuJYHC30PWOTeyuYWRGURaMlSFV0L8a2gzuXAWa3s1sSqCCTcW4Lcj7g_CAb6UXLO3V8OxhOolFPz4YJMGtDD7pVLhh3-CX0_m1I1aJaHjUi6-n3zLkI8lULr7vcICKEvYYK47W_3bp3stsCK16cJgUU3Zb1C0kVCuspP36JCt2qPXI60gRAywmTZVQEJsWQgVI7wCexTARFalwUR9wcqaLdisymlTgL4aV-nR8u9xb2r7pv4DnASkCQlbG9Ig1IBOU9K8haMRNp1SjmfDUikvHl309jw80dfZ-GhiqHmvJMVk621g_Au4bzeuXnRrOoVSuKo_RjbaBhnfaRl7gJOdRudDeWnhPK9sVlt3lPgfJ0VIxkZ3mexUV75HuSjYCZa_NnIGcP0v46hB8wkFNtF3S_D2_2FhdFT7gW7xZK6HTdhyG3Vhbuc8oR4DvwLxvkJas1zeKelYE0oZbcXIYiUjygSrh8cL52OTSivdMK43c0Ay-pmagZBBqUr4cF5rsenBVf526ySvZ8qDxCOt_TAiorbJHrCI2jnOZ1ht1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3f719970.mp4?token=ABVyEXlTAd6Ghl-skeAp643ZCtNGxdfeeLtazNKrGtgZ_qMsZzJoW0T2RZhdQ6CTourjwIHQhdNkVRd5fT2WiVp12HprHmNbMN_4dhZBiXP4U_yOzZ-W1AQWH2cS-TUxGtGKuJYHC30PWOTeyuYWRGURaMlSFV0L8a2gzuXAWa3s1sSqCCTcW4Lcj7g_CAb6UXLO3V8OxhOolFPz4YJMGtDD7pVLhh3-CX0_m1I1aJaHjUi6-n3zLkI8lULr7vcICKEvYYK47W_3bp3stsCK16cJgUU3Zb1C0kVCuspP36JCt2qPXI60gRAywmTZVQEJsWQgVI7wCexTARFalwUR9wcqaLdisymlTgL4aV-nR8u9xb2r7pv4DnASkCQlbG9Ig1IBOU9K8haMRNp1SjmfDUikvHl309jw80dfZ-GhiqHmvJMVk621g_Au4bzeuXnRrOoVSuKo_RjbaBhnfaRl7gJOdRudDeWnhPK9sVlt3lPgfJ0VIxkZ3mexUV75HuSjYCZa_NnIGcP0v46hB8wkFNtF3S_D2_2FhdFT7gW7xZK6HTdhyG3Vhbuc8oR4DvwLxvkJas1zeKelYE0oZbcXIYiUjygSrh8cL52OTSivdMK43c0Ay-pmagZBBqUr4cF5rsenBVf526ySvZ8qDxCOt_TAiorbJHrCI2jnOZ1ht1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرنمایی دیدنی دختربچه برزیلی با اسب
🐴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/688939" target="_blank">📅 09:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f0571ecb.mp4?token=E8bu8_TzzbBcMCGUHRyTclt2m2sEqjGeWlVC20tcZ1vImJS4UnfT_b6kY9vtvA2dzy5IaClN1Rv7BlSYS0lCZZvSEOtubZGg0gQqVBYjmEcQT5GHYfDC7U2b3PylbaogWxAiX4UyiNYKpsjbQYSZFMy28BCUSPALiGTa65djSnYQOexAfUq_XD8BeqeKcDd4CzOq6PVe5Ztx4XPSe_Pqlz8sWQW1fc6g1znfV2pc1aF4p0Wi7JcvttVT_eTqowBFnHIvI1X_qPRg_rsWh3AuL3xp2itODiPwnMGGsPzfmh02AWwNsQc_ZSa_mikewe_3qGP2d_RQFQtDWb-LcVwlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f0571ecb.mp4?token=E8bu8_TzzbBcMCGUHRyTclt2m2sEqjGeWlVC20tcZ1vImJS4UnfT_b6kY9vtvA2dzy5IaClN1Rv7BlSYS0lCZZvSEOtubZGg0gQqVBYjmEcQT5GHYfDC7U2b3PylbaogWxAiX4UyiNYKpsjbQYSZFMy28BCUSPALiGTa65djSnYQOexAfUq_XD8BeqeKcDd4CzOq6PVe5Ztx4XPSe_Pqlz8sWQW1fc6g1znfV2pc1aF4p0Wi7JcvttVT_eTqowBFnHIvI1X_qPRg_rsWh3AuL3xp2itODiPwnMGGsPzfmh02AWwNsQc_ZSa_mikewe_3qGP2d_RQFQtDWb-LcVwlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی سنتکام از سوخت‌گیری هوایی F-۳۵ آمریکا بر فراز خاورمیانه
🔹
سنتکام ویدیویی از سوخت‌گیری هوایی جنگنده‌ F-۳۵ نیروی هوایی آمریکا از یک فروند هواپیمای سوخت‌رسان KC-۱۳۵ منتشر کرد. این تصویر هنگام گشت‌زنی جنگنده‌های آمریکایی در آسمان خاورمیانه ثبت شده است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/688938" target="_blank">📅 09:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469234ffb1.mp4?token=U8-tWbMvfzU_suHf7sToelBGjTsWFAsRNk5mkZ7H041W1x08mH0ni-LkJO-j_PXWGaTYRaIRPcek_25IARYWsKE2nkrsMt-e1VgxuBvjcLXeObI53fMIYLi6Zf2TjAgaDTlzux3CsM9y3jPbqNDH98suPAw9fMQWlartHk2JxQV1YZq2Zz7RWr0wCTADzz4AGQx_ldvKuCUnzGbRIoKUoCfvYXVnuT4KNXw-E47AmmAGkFskgNr9pcmctz-LiAcsHbhk-14M3ndZCesbcfZq4dYfoSrWWOmcirMGr5D3UenCMMUs7b_sHMZ5LLOekgmv32OyJtMOge2OYgH_WQwfoLVpOFdNuXXyzeXE3OCM81JkOuuZNosfTk2e7wTd28MchYZYVGqDicdWmtPixUFb_ozQgYf6NSv9Jp-_SKvt33E6kaLhXx0R9Zf25tS50zmWfedrlsCXnKnDOY--RD8t8Igd3Wdmu-4zbGBSLQzIIZ_l32AORSDc2fXqqrDe3DGSqss-pV7Xd2bi9Gz7d5gukygkzgm9NGRg-25uNcFcFL5f_WbIJtBnPGdEC-w5DxlDJ9BZc1EhOXJwQPeuw5bKgsMOVwfgXqxwcBrFtNeRUhqA8mUFouZkaZVQbVf8yrBXj9EE7Np-TMUtVXbI3bdiJTR2PIXH5dfIZx7koh43Iuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469234ffb1.mp4?token=U8-tWbMvfzU_suHf7sToelBGjTsWFAsRNk5mkZ7H041W1x08mH0ni-LkJO-j_PXWGaTYRaIRPcek_25IARYWsKE2nkrsMt-e1VgxuBvjcLXeObI53fMIYLi6Zf2TjAgaDTlzux3CsM9y3jPbqNDH98suPAw9fMQWlartHk2JxQV1YZq2Zz7RWr0wCTADzz4AGQx_ldvKuCUnzGbRIoKUoCfvYXVnuT4KNXw-E47AmmAGkFskgNr9pcmctz-LiAcsHbhk-14M3ndZCesbcfZq4dYfoSrWWOmcirMGr5D3UenCMMUs7b_sHMZ5LLOekgmv32OyJtMOge2OYgH_WQwfoLVpOFdNuXXyzeXE3OCM81JkOuuZNosfTk2e7wTd28MchYZYVGqDicdWmtPixUFb_ozQgYf6NSv9Jp-_SKvt33E6kaLhXx0R9Zf25tS50zmWfedrlsCXnKnDOY--RD8t8Igd3Wdmu-4zbGBSLQzIIZ_l32AORSDc2fXqqrDe3DGSqss-pV7Xd2bi9Gz7d5gukygkzgm9NGRg-25uNcFcFL5f_WbIJtBnPGdEC-w5DxlDJ9BZc1EhOXJwQPeuw5bKgsMOVwfgXqxwcBrFtNeRUhqA8mUFouZkaZVQbVf8yrBXj9EE7Np-TMUtVXbI3bdiJTR2PIXH5dfIZx7koh43Iuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ کلیه چطور به‌وجود می‌آید؟
مهم‌ترین عوامل را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/688937" target="_blank">📅 09:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688927">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnfp_SiJ9QTuVn-YXeIeT6SnuQbIpqOeGYC6HBubqX8yucaJyH4JUmam1SK5stpNJMU3P2EXztXNuPoqoYbnt9sQMhbiZPc-eRSBdBqiMx8AgUUSuLVnOUlFY1N32GbIHqk9RHItlCfa5tyME5--qW6Ol38xl1dlgvw6QQ4tN0nVYFmko5HZLOh7q27gCT0TE4gUqWXJBfEHLh9Nc52fegjI9_YBOvfIgNXO4pcT-PuvJ_iUqQlq7niwg3-ZJtAPegwYg1pzue_ypdEeeMPxkrq-8S7ZvJtTD9pqLuK7YP5xI0sbOcux8nwHKSeL4yD959bpZizKjg0-YC5AR9wAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LcGQ44Rr-oY3_maI-DjWrDDMikBNq1-63IDqB7l-hv9-ulkwzL2V9AsZf4FODTvmE5mZmoE0trgFYYZVmZyUxduT7mHklm06Z1GUXgUAS9lnp9YE3YhHuRu4zILGH6FCSgMNMB1_XcxFujsHE81bJMh-iGIMTbQRR59ba2S0FcDRPtsn8zq1Z1u5Y7vxOwbr2TH2dFjv0hQT8YmBq4wrz-d8lojvSDMoNE2XWNF99tiNDYfRhXLaOHu-9ZS2TMogGh4wulSdGORMKPrW-YgCTvLsQAgQ5a-UcYXcj4K-nLHEVo0a6tJtkdsBZzHLxkhTJEUnbToHKYKACkL4MbRzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrmXGmI6Wwfuyg1T314l-3GnyBPlXocieiC5wvmqVKnVXHlg1g0GujqzFo0SNFq2VKNNaI4QFHJsPwB7Hp1_2MJj7TOcImRp0qKWIG5zSA5bLbvYAdbphxAreu6D7Z_WFhmKDkDiKtRc5j9Cr8u8evt29gQmjCXalpDRREm_yC8Y-Kauos_3VBeVAJYKEEkg2n2q6hdHYVrzszg4Sc_OwyRL55V2UlfczAzhyltFPHSlS_93GSA0jRiDzV2xKkHtDGmoSe3IT6f6KoL4v_On8iYRLXAsXI1dHZXiHzF6BRDo2VjCrD71gV7wprNv21U133_FQIYEap3oueicPomK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bddv7sT27vz_bh3D7lmEzVy8fItLUc_2voBSqtL_xXHghV9LpcG_mNT9-YFI4FiMDEOAPfKxzj4WYmcuf476ltR0eedCRre5SC1VZG1XkHl0D63bwLcW-tWfT56Z3JYPwc3WDhQHxpPZ4CC0mwycL2jSqkHNYysmx27FQj3dI9sF7dP8PwDP4QKo2KwZZO47_4D3aaU5gBud5-9BUZPDQYGN-VUnFt_uvR4VxKgyvkRxebEW7irHWETCk19kqtBVqG_01cdzrYCbr1Il9nqzraXjBGXiSYVsIXCXneh1swYqg7jesqNszwk32_BquejmCuYyEZoDkJeNF_SsoZhJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8OdSrUYQYyNuB3M3ZoW_MwZKAkfrCLs-9jjUY6nIfSs_jL7zj--vXlj59oagIGYLJbilvtKslQG6-E-p4-7VEcZNNiC6KBTLP68rV2bBkV-knyWa07DUVIOiuDokz40POgCUkxRw8TWEpW1f2oR1SI99fyz0w1oYn3w4XssZQ5nEwxk8NymCPtGUOgP5N3nJN5b6eer3RrnEoU4V5j93QWhlGp_UnNLsfgNT901w9x3YCFArSd915C88SO7flhXQNH9NO1Guph4RR8jZj5rSquujXvKk7NUSiJme-kzyYryOoFNAIeY6k_dBpyxT6dPqtBWXx7EKktxFT5ckzF9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mviliLIsc5OCscXegVgWPQpVYB-YGwjMflmJw_42qx-bC8vt-D1sM2feamSSs8bD2_7seS2IEAAkjDYJj6tkvy4iaoIf7MdtzkQNOo8-qFCV--YTbGmdsdxm7lrbUg_L1kJiN1tv_8w4PX7XYduqcV__baldXEZvycco8pQcxWKPeFnaeABcDxAnufUmcAiDgnR7WADqC-dCd49fjzAe8XflR5XvYwGMuVT3vkSnrdCpJ5i9ybOGlW9bsRWpGi0vmtVj03Ds8KdV62bFwgZljLzD6ILlcaKdhSj6vVxWC2nbQJri9EzVq-17tO1eheTU6vZXUtvKVd3I59NMkH4H9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMoeUMAMaPHSMnrz3RYFiUWAR0XQYPkKH6tFGwccWIONBV5zR_TtV5WIP7Plc1iDDvofG-iBPBmj13jbhIl2NbfsuZDJnyWcEdfnruki-tkCzfFkH59Z8gw7XNqKfrO4ebUcZqSElgTFyHUJEPkATVMnV4rHOvuxqMDV1Tag6c0PgfKMJXKKyPpa6V6Rkp9mErwnU9lS76xPzfFu-eJX-q44QUw7kuurlGG_EtFkgFwOZ3De1IclKLqEzvk57GbrzhnJJDHJLKlTGbbHrHGRjHbyNhgfkl6FsWt2LJjh4bSR7OqdjFeXHMCBWr4og9gkBzMitNQs8Pu-NeEdJI6SEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ISQ_ji3HYqOWqe3haPYdkIbfyks8-72Ss6QkRAz25_nfTwmrwNTe9HNYMmENv0lbR8iYxy78ZgBTeFQcFI2W122pE9XWdN5XIcx0BpXEfF4QMVlaTlTpYnEMx9ZmoPANy9vl8z6an_QqC77SrL2cnRcQCVqKkcgP9bekiY1Nlvrb4lvVB1jFaJQ2aABSbD1-Kavu_Gc7Xi2llJTtQcYNKne2xzcVS9smns9qP1j_tRhelplgSKpYuWYeuZah52T270dWOwtyxmjSZz2SsUxcxzunq5WOPYsgSTfnaDNrf7GRL-5t4D0ljALiQNMvUnc2fq3HitVEjNGL0OTj0dqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGQaUqowfFvBc-VDarPCB5LidLtT1oAuLS2OGVi5nc2SJn5T6SGnSHcmNbI4PjZAh1mdq_MhUshf9kVJ62IY8qplQX50vdUsWDEARbiV95clMzRmTiyJJsYSQTMvJLWSMNeS69lHy8gBVrlUsJZgaFd8BFHi_xGOQrJLryOTaWdQGEhcLVXnsIBdI3gf3T1uSj9c5RG5SZStXNwHVTzKxKkLODPOxL6Tr9ykeXuIxKCqQfVilifOncLaKegtd3JOleC2LE3REMioq56KNdrX4yy0p9qZkFp3OgZQcKVQR_-vYORafZnHuTrtaWZxqN1l7dbjY_QAKHU6ZX6qKDuXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwPyeeWcIlkI2F6b5VzqEssTNBLw2cpmE43VEzl8YyXFF5fx4lK9WFI1ZOaTJBdhRcsK0OT26cQeantanYJelUUseRfz9rU4eNLp1eADnT_Hdb2JXLMWB1rd98PblM7pQD2ZmS4sbdjazS0_MqnMt_dTHinPFlGVIJD-YcS1TRYSZjA6ARGVeyYV51HDsFB6v5S2EQpoLF3e7aFoC75-q2a2JD57lMafpkQ5APUUXLhT3J4rTSv0TLB7gcIw42-WehW-7rwY9qPEt9jJcSK_w4tpLL6V9hCuPXWs8tpxs4o44DER09fvVg5foVBQn19srlu2wcpsurD7Ca5Rf_3NUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاسِ مشکلات و دغدغه‌های  مخاطبین الوفوری برای شروع سال تحصیلی جدید.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/688927" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688926">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج اولیه کنکور اوایل مهر اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688926" target="_blank">📅 09:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688925">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای آکسیوس: محمدبن‌سلمان از ترامپ خواست مقرهای نیروهای مسلح یمن را هدف قرار دهد/ ترامپ این درخواست را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/688925" target="_blank">📅 09:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
جمینای گوگل برای ویندوز منتشر شد
🔹
اپلیکیشن بومی جمینای حالا برای ویندوز ۱۰ و ۱۱ در دسترس است و کاربران می‌توانند با میانبر Alt + Space به‌سرعت آن را روی هر پنجره‌ای اجرا کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688923" target="_blank">📅 09:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7LxH98NySFbCVfXxT4IXthT3zRDJCJiixgZB_5bPL8Hb6rcuccfg2YpCC53bF93o378mBtVDAzHwRffcU7aku2BYM_UGJYXLmo9YdKbY2c10siMm_cjBCx6FizzJA2srUkLGWuXTgIWZLx8g_6SJsJ3LyZ0iANIWtHjkLTi9ocVNTaU4LgOzE9fqHF4OiX9UKXQ_JXXl-p9hAMEU4un36vMJCRk4BpBYw8dyMFBEMl1hMLz-jZWoxgUD_hAq0-guYfGoHDqh1PnmR6PZ-LkZHkEFUKn_0IkuQpOAKdAwt1eR67v58uC0CW9D5jdMq9-fOkNJqrnzr_rH9K8J5Bs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری بی‌نظیر از شاهین آبی با ترکیب رنگی خیره‌کننده
😍
🔹
برای ست کردن رنگ لباس‌هاتون از طبیعت الگو بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/688922" target="_blank">📅 09:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688920">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: ضریب ۲.۷ برابری برای اینترنت خارجی باعث گران‌تر شدن اینترنت شده است
علی جعفری‌آذر، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
ضعف یا نبود پوشش اینترنت و تلفن همراه در شهرها، روستاها و جاده‌ها، عدم تمدید یا بازگشت هزینه بسته‌های اینترنتی در دوران جنگ توسط اپراتورها و محاسبه ۲.۷ برابری مصرف اینترنت خارجی و نیم‌بها نبودن اینترنت داخلی باعث گران‌تر شدن اینترنت برای کاربران شده و توضیحات وزیر ارتباطات نتوانست نمایندگان را قانع کند و مجلس به او کارت زرد داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688920" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688919">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdaaa3818e.mp4?token=RFqLJvfGC49671rlvzJXFecS1L4__fS-U6Q1dcR_NDRB-l5_eROg-73dzrBlVrgVeda0JD4vmu5kcYc5XvecHOOPo7gWN_u9i-Ng0DhsN655fpGUllJzQwcOBIVOU-QSMTG5t1tYifBJ1qkKklrt49tyquGctfySCYqRiS-yzJes3XymbDZuUAHhdpQ2ilhHur-f_CSb0eW4xPi_v3HX4IQ6SoArQP3fIVkxv1o0Us1FVJbmj_azu0Kqw5YU8DUCsJwXqZkQKeu-kJfz3YBnOye2sVXZzIFuC_Tlm8-NhL9MHrfTDEKnIT6nCDYajRk3NGVIS_0xc7gLA4Vb6EyK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdaaa3818e.mp4?token=RFqLJvfGC49671rlvzJXFecS1L4__fS-U6Q1dcR_NDRB-l5_eROg-73dzrBlVrgVeda0JD4vmu5kcYc5XvecHOOPo7gWN_u9i-Ng0DhsN655fpGUllJzQwcOBIVOU-QSMTG5t1tYifBJ1qkKklrt49tyquGctfySCYqRiS-yzJes3XymbDZuUAHhdpQ2ilhHur-f_CSb0eW4xPi_v3HX4IQ6SoArQP3fIVkxv1o0Us1FVJbmj_azu0Kqw5YU8DUCsJwXqZkQKeu-kJfz3YBnOye2sVXZzIFuC_Tlm8-NhL9MHrfTDEKnIT6nCDYajRk3NGVIS_0xc7gLA4Vb6EyK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «آقایان، آیا امکان دارد که با هم ملاقات کنیم؟»
🔹
ما با آن‌ها به شکل بسیار متفاوتی برخورد می‌کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/688919" target="_blank">📅 08:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688918">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35ee08b5.mp4?token=MXiJasV7pzN285EAqIVuKQJQFH54yIjkgKe1TT1wBm4z75OKRiZcMZG8Kho2rguBaw7PmpyVy6Orq4HLNiLYV1U-Ky9S0yzsKAgPq1a0BbZsD6NeOq5xo-9PqmOiZsejsDMoyTKc7g-5C8ilinXSaohztBp07fq45Sqgb92DDUl9Z58qUKud3N0Zihq6yYcsjOy_zthwihq75ti-VY7tytPPRN7-JF2bmGS4pCIedC183mc8rejDRMvMiWK93d9S-n2sSc4d7DuqW5mJzKKWqu7fpGLp0KSjwI1ty8Q0T5kEsIF2Zw2y5BqE-IbrgCml2cUTmg48YT90D3BiGxG3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35ee08b5.mp4?token=MXiJasV7pzN285EAqIVuKQJQFH54yIjkgKe1TT1wBm4z75OKRiZcMZG8Kho2rguBaw7PmpyVy6Orq4HLNiLYV1U-Ky9S0yzsKAgPq1a0BbZsD6NeOq5xo-9PqmOiZsejsDMoyTKc7g-5C8ilinXSaohztBp07fq45Sqgb92DDUl9Z58qUKud3N0Zihq6yYcsjOy_zthwihq75ti-VY7tytPPRN7-JF2bmGS4pCIedC183mc8rejDRMvMiWK93d9S-n2sSc4d7DuqW5mJzKKWqu7fpGLp0KSjwI1ty8Q0T5kEsIF2Zw2y5BqE-IbrgCml2cUTmg48YT90D3BiGxG3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ درباره پایان جنگ ایران:
من نمی‌خواهم بگویم دقیقاً چه زمانی، اما فکر می‌کنم این اتفاق درست بعد از انتخابات رخ خواهد داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/688918" target="_blank">📅 08:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688917">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53bb0ad15.mp4?token=eJGjVqlLryMB3d_SJjNNvbFd0RFXbyzrKXG4vGQHpUVtKztgY1XM2udMF0Z34vvldwCHVt603Zpo3yA7KjkmsI_QsWsJa6P4JThahaDnSWILkZ5ZqIzGOFcXWOUy9C5JyTClSQKS7staZl0lXJq_JoecjKyHuPm2H2ezYNTieX-DSY9QvdnH18wSbCKY8T7ecVfMtn6NhVSzShhTlSLiPF-knActB_g9AbOWUOgEwa49GBS_vA5qHRBJ2xcA9W-APlDPnHX-qY9a6Z5P2A0B4aY7ngYAcgFI0NQ4N41rYXx4EyUUHog4WBWmjCgDkclHWIK5yBMCfnJ7V5orJ16pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53bb0ad15.mp4?token=eJGjVqlLryMB3d_SJjNNvbFd0RFXbyzrKXG4vGQHpUVtKztgY1XM2udMF0Z34vvldwCHVt603Zpo3yA7KjkmsI_QsWsJa6P4JThahaDnSWILkZ5ZqIzGOFcXWOUy9C5JyTClSQKS7staZl0lXJq_JoecjKyHuPm2H2ezYNTieX-DSY9QvdnH18wSbCKY8T7ecVfMtn6NhVSzShhTlSLiPF-knActB_g9AbOWUOgEwa49GBS_vA5qHRBJ2xcA9W-APlDPnHX-qY9a6Z5P2A0B4aY7ngYAcgFI0NQ4N41rYXx4EyUUHog4WBWmjCgDkclHWIK5yBMCfnJ7V5orJ16pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس‌نیوز: همه می‌گویند اگر می‌خواهید وارد ایران شوید، به طور کامل وارد شوید. فقط وارد شوید و آن‌ها را از بین ببرید
🔹
ترامپ: خب، شاید من این کار را انجام ندهم، چون انتخابات در راه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/688917" target="_blank">📅 08:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688915">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
قیمت نفت به ۱۱۰ دلار رسید
🔹
قیمت معاملات آتی نفت خام برنت در جریان معاملات شبانه با جهشی نزدیک به ۶ درصد به ۱۰۹.۹۷ دلار در هر بشکه رسید که بالاترین سطح آن در چهار ماه گذشته محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/688915" target="_blank">📅 08:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688914">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJX9RnM2r6uccL_hXKEENMmvC2KG6N8MVFoR5QvSBjUXVpVtWfEqZ1hOnqIFYhVFJTl1arEt_TUAQ5xOE0t70XBRHDM-yXIpiM1hwdmEQZsmcUSMnBs-sQipQehvQweea3-kSB5SC4n4lAhVvIzpRMD0qP8mZ02xEdLDJDu9byhkra5OXtT7zubTfkuQ5ywM6ZW3Ndj7J8Gn7lawmPhyuQ2uoQH73k-l-gaT8aKLacQcPSjeIFl1d2EXPW1uq-kZw-odkSiIfy1-Bc1aZdtxBQRcTMnRy1jWZJssDqD0JdQH7bd6qwxeGOWyZKGHD92kDWBvnJItPTxIn23qdt-yew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در واکنش به تهدید عربستان برای بمباران شدید بندر المخا، محمد الفرح، عضو انصارالله، منطقه نفتی رأس‌تنوره را تهدید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/688914" target="_blank">📅 08:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688913">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b1f0f285.mp4?token=guhFgI4jy2q5GaRGjQbO4mhtuW0htbEuUou4G-YReW4UEsjEecz_-3pisc_e2qOr78uiBtYX_QntEIAQXSZxd7y9haQhdvd_kj2NB17614Tl7Nr8Y3Wgr09c2aNHrrfWbBZOdm03sf2byh5rX7qd2ZwJL3u6W8apUCIIOrykOPerAZ9FvSbG0h2b9Hz0wGsq-GNX5Vs1XJP-DV_JeQH6iFfx6Uw2fcsY-v4rbvB8Is7umZjHeDjKVm7khy4-YdI9O4_F8GPy6MU5t3pCmiwt779j3ksD8MzYNs7s3JT7qW4GJrJMMzh8sITabnUCttQ53nd8tEBGLjEy3FO-85IGUhK8B4P2cy42fpHOEfzSs9TZByFOinQJtMpGnI10ns60MCT9iQGjDOLClKUodxofblQYdQ7inKoDTijXwcEFCwtn2mZqvMwPcUXzFPCHQnj8AnVBf8E1HdVZf51oE7GXfSizWO2qz8c0zVkO1wuzTsq9S8cTk1O7naxsZ5cUGOaKku6bZlTt8MpiXGMtuYGQkstRhPm5pJBkNhvQTFng6CuLPKJ9zLPObE6H28VttByVNgNssx-AeLdNxzB2JuWeeZ4Z_1ah0DnfIUGxbTu9uqmIsE5Rnz0MFrKH8nuPYUCbow6gkyeRcn5dNqeUIxivPCqPW9wcE6p9u_PUntkJaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b1f0f285.mp4?token=guhFgI4jy2q5GaRGjQbO4mhtuW0htbEuUou4G-YReW4UEsjEecz_-3pisc_e2qOr78uiBtYX_QntEIAQXSZxd7y9haQhdvd_kj2NB17614Tl7Nr8Y3Wgr09c2aNHrrfWbBZOdm03sf2byh5rX7qd2ZwJL3u6W8apUCIIOrykOPerAZ9FvSbG0h2b9Hz0wGsq-GNX5Vs1XJP-DV_JeQH6iFfx6Uw2fcsY-v4rbvB8Is7umZjHeDjKVm7khy4-YdI9O4_F8GPy6MU5t3pCmiwt779j3ksD8MzYNs7s3JT7qW4GJrJMMzh8sITabnUCttQ53nd8tEBGLjEy3FO-85IGUhK8B4P2cy42fpHOEfzSs9TZByFOinQJtMpGnI10ns60MCT9iQGjDOLClKUodxofblQYdQ7inKoDTijXwcEFCwtn2mZqvMwPcUXzFPCHQnj8AnVBf8E1HdVZf51oE7GXfSizWO2qz8c0zVkO1wuzTsq9S8cTk1O7naxsZ5cUGOaKku6bZlTt8MpiXGMtuYGQkstRhPm5pJBkNhvQTFng6CuLPKJ9zLPObE6H28VttByVNgNssx-AeLdNxzB2JuWeeZ4Z_1ah0DnfIUGxbTu9uqmIsE5Rnz0MFrKH8nuPYUCbow6gkyeRcn5dNqeUIxivPCqPW9wcE6p9u_PUntkJaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال پیش، ۱۱ سپتامبر، روزی که آمریکا از طرف یک عرب اهل عربستان سعودی که در پاکستان مخفی شده بود مورد حمله قرار گرفت و بعد تصمیم گرفت برای تلافی به عراق و افغانستان حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688913" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688912">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a870a1584b.mp4?token=Y9dRJSnlKL6SrQkx5a96pXUTpqxgWrz8M75G357MSEDq57vJQOA1tBXNxdc4ObwuBNavuco6gJXG2antptZxsP3SrXNlHN-PJP9hvDbGOmAvEGC1FQVaJHm08MobMd-L0mHHBN7u7NxMG78LE1mcQkn1k-K1nYyHWfGh2D0zB587aVnSDKDUiv9ulIIpPdn94JY7ZlsxCmLSiVjBK8V-VRaTyofbbQ4q-pT406JTf-yZvMu0fcNLoMuhYgOHhAvxbEGN45QT9s5Uzkos98Ihs7AX0y0kHqgVCFqXvKHCJz3-UWCXFIlXk8KNtrXiOqxJYc3TVRQnurIISMBSybTtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a870a1584b.mp4?token=Y9dRJSnlKL6SrQkx5a96pXUTpqxgWrz8M75G357MSEDq57vJQOA1tBXNxdc4ObwuBNavuco6gJXG2antptZxsP3SrXNlHN-PJP9hvDbGOmAvEGC1FQVaJHm08MobMd-L0mHHBN7u7NxMG78LE1mcQkn1k-K1nYyHWfGh2D0zB587aVnSDKDUiv9ulIIpPdn94JY7ZlsxCmLSiVjBK8V-VRaTyofbbQ4q-pT406JTf-yZvMu0fcNLoMuhYgOHhAvxbEGN45QT9s5Uzkos98Ihs7AX0y0kHqgVCFqXvKHCJz3-UWCXFIlXk8KNtrXiOqxJYc3TVRQnurIISMBSybTtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت بانکی‌ مون و خونسردی نوری‌المالکی!
🔹
در ۲۲ مارس ۲۰۰۷ (۲ فروردین ۱۳۸۶) در منطقه سبز بغداد، در جریان یک کنفرانس خبری، چند راکت به نزدیکی محل نشست شلیک شد و یکی از آنها حدود ۵۰ متر با محل حضور بان‌کی‌مون دبیرکل وقت سازمان ملل فاصله داشت. وحشت بانکی‌مون و خونسردی نوری المالکی برای بسیاری در زمان خود قابل توجه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/688912" target="_blank">📅 08:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688911">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4XCUWlpBAQ9r8w_s3VKj6h_VkgTQrW5hgE2oy93u2drHn5HadbaS268KnEVEvv3JGpHkAlNThQ2g-Hoh5-ODTf3_Ek5WMx9kq83vE3gaaA_aPktSQcOjjMFTS8e_iTYr_E6OfgTV4FkR4gpyIdshUMTCyCVhd70iBrLuBUihalOLjUp1dzvHGGjJy1dD3QHOR6wzy_t9UIt5fv2Z6xczQqoPikKW9gnzUg7bRnSAk_YNDO6LLdB3K1HYTN26DMlDSEWf4Qi-28klF_XflQWxx4fwbuNAwRZWsV16qvock5hqtzZPFcESt7mNXqMaW3P5gn-sHcCMM7ljfsd1RRRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو: بزرگترین تونل ساخت ایران در خارج از این کشور را نابود کردیم، سال نو مبارک
!
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/688911" target="_blank">📅 08:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688910">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31074ae524.mp4?token=kS4fivwJfotHn64tPkVM0bAvAJp4TOMEfvlX0WIenfPTeiE-E1ly593aPvPt773nCnWPBVG_2b7dxvCMqtWA3gyF_ec_R2VoDjOtD6kkqo6aXciPmJwIYohFVN_8C_jk4m5bVWSYuoyH_nWQHJb5E5Vyb8_0-qmjrJ9Pne7OJTBdPbwcp3SAQ-H-IOWf0eM9Du4ieow1OWuA3DhXmPv9od5lKbTaijQGNJqKyd-usQNwYzfHuofUbEe3PhXY1gjbL2wj0N0F5KAMsvJNeVkYy0S_Fl_tXpcrhP7VIcLAlO0Jtk49n1mlVZxotOxFAL1i2_OlQ7yiU0U8qBFocFibng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31074ae524.mp4?token=kS4fivwJfotHn64tPkVM0bAvAJp4TOMEfvlX0WIenfPTeiE-E1ly593aPvPt773nCnWPBVG_2b7dxvCMqtWA3gyF_ec_R2VoDjOtD6kkqo6aXciPmJwIYohFVN_8C_jk4m5bVWSYuoyH_nWQHJb5E5Vyb8_0-qmjrJ9Pne7OJTBdPbwcp3SAQ-H-IOWf0eM9Du4ieow1OWuA3DhXmPv9od5lKbTaijQGNJqKyd-usQNwYzfHuofUbEe3PhXY1gjbL2wj0N0F5KAMsvJNeVkYy0S_Fl_tXpcrhP7VIcLAlO0Jtk49n1mlVZxotOxFAL1i2_OlQ7yiU0U8qBFocFibng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه گرافه‌گویی ترامپ: ایرانی‌ها به سختی می‌توانند به جنگ ادامه دهند و در تنگنای عمیقی قرار دارند
🔹
آن‌ها همیشه مقداری موشک دارند، توانایی موشکی ایران در حد زیادی نابود شده است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/688910" target="_blank">📅 08:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688909">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
شوک به رئیس فیفا؛ فرانسه پشت اینفانتینو را خالی کرد
🔹
فدراسیون فوتبال فرانسه در اقدامی بی‌سابقه و پس از بررسی‌های گسترده، حمایت رسمی خود را از نامزدی جیانی اینفانتینو برای ریاست مجدد فیفا لغو کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/688909" target="_blank">📅 08:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688908">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWRO6MIG5CAbo222ymB8xN6eZDgqW_3LSl62KstNusAUtaqmnfkAQ4GZ681X58w14PF7WsqpsKi36XsFa0Dgnjz7HV96A0SdsVlKvXirMSJEb3HM9s36YWypqLlj60p6PA_O0k6RcpEimAhz8qxTWVeb4kG3_GBc25Ju6midYSJg3KyerczcIsNYcinoWvhSKBvsyojzughbskAQXmbJr8d9eQ-pg2aAKp4daPjANhDulupeLtlw_QaS7jJV6zhuZtYx1J4hlK66eqcDnOvj3EqL918KYr0hF6Tual2l0rPNi_o0CxEoGiLMW1bVm2JAwruf5cHK1RtK5g0uv7pgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به اعتراف مقام آمریکایی؛ مردم آمریکا نباید هزینه جنگ‌های اسرائیل را بپردازند
وزیر خارجه:
🔹
صراحت «هانگ کائو»، سرپرست وزارت نیروی دریایی آمریکا، جای تشکر دارد. او درست می‌گوید، نیروهای مسلح قدرتمند ما واقعاً «ستاد ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردند»؛ همان‌ کاری که با دیگر پایگاه‌های پشتیبان تجاوز آمریکا هم انجام دادند. مردم آمریکا واقعا نباید هزینه جنگ‌های اسرائیل را بپردازند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/688908" target="_blank">📅 08:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688907">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران در چندین مکان زیرزمینی، در حال مونتاژ موشک‌های سوخت مایع و جامد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688907" target="_blank">📅 08:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688906">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlzaaWQosgx22IwxPMKgEo3NHZUp4oy_BU5YW7jh3zROENXzior9j5DbaxzK9-M2l6i9PFCHv6AjuxrSBR5mrEHPQsX7ysigb16uykmeKXl94nFeYO1SSfc95QG-815NY7yEiSepaPpWfw8fRnzARt1c5iN1JQH6f2b93dkP3R2-iKFvaZQPZffSwWWhgN1WtSGzIa0yyDznkTjCmfq5NL7Wm9bfegCTCd5qAf717-nLoZCBLgu8nTx_UAWaJnQiUrtPM_LwHe3Ez2qdG8YMzTsPnfhaDS89q_vm0eu6huCqNqmktQVacd9vBxJzBJG-wKwkTrIHvVQjE4OzwblwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروهای مسلح یمن، خط لوله انتقال نفت "شرق-غرب" عربستان سعودی را هدف قرار دادند.
🔹
این خط لوله، نفت خام را از بقیق در سواحل خلیج فارس به یِنبُع در دریای سرخ منتقل می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688906" target="_blank">📅 08:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688905">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP7dKBPK0RS48Eoryomkf62idenL85etrM-oulSUAZ4jN6ieIQ449W5A5Be2GaGG7kjj2nWFYfrJx5qRRzFa8TXTXDD2GRQ_FyIU613vZFDwDI1dsaKi97whU5npLEiL9rz47OOgU4iNdHFT11mY3S9LPbJps_2lt6iEHSGrakM5WbjLnpEAjo68ra7sv7jMOx_7fgA97hYLKK4Ks2iAvN6qrp8W_PbDQSS2itUxBHzSkTw82ckueBPSd8OE0Lps0ClCu0YBrnDoFD6OS-6HT2fmi21XdSmsqUmylxeExMJUkg2oLHP_mM2at9laARp81lbJYeys7R8BViqVlyg1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس ترامپ را دور زد؛ مستقیم از فرماندهان ارتش آمریکا، ارزیابی از جنگ گرفت
ادعای نیویورک‌تایمز:
🔹
معاون رئیس‌جمهور آمریکا، در اقدامی غیرمعمول و به‌صورت خصوصی خواستار ارزیابی‌های مستقیم و بدون فیلتر از فرماندهان نظامی آمریکا درباره جنگ ایران شد، و آنچه شنید بسیار نگران‌کننده‌تر از پیام عمومی دولت بود.
🔹
فرماندهان هشدار دادند که این جنگ ذخایر حیاتی تسلیحات آمریکا، به‌ویژه رهگیرهای پاتریوت و موشک‌های دوربرد را تخلیه می‌کند و در عین حال ممکن است توانایی آمریکا برای بازدارندگی چین، روسیه و کره شمالی را تضعیف کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/688905" target="_blank">📅 08:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688904">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
امروز آخرین مهلت انتخاب رشته داوطلبان آزمون ارشد دانشگاه آزاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/688904" target="_blank">📅 08:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yg3uea0bdmnN4_c8vMxmwEQraHO1BsmYWLFOnfLwh3k3L5-LGd9PORyUofzFfr5y-9D1PKyqyD_1qBOQPDq53Q7c8iinkBfvFT2Z9zC3iL7yNVG5mndtLvCQ0ZzMx8yk5U-W7AcGiQVXarHOhvebTOgrncNfzIE21q6_WR4xzTrvquYEkFS1uSKBGfU5r5huTEQkEAdIVN6k2AEBKbuvZtcOV2lRQ_iE0XPdraHLxGqeu1kyS47PayAVdJnNUQcNlwaKd2R9gguRqllB1LlkkMiirXVNvrEQlof0jl4y-Pn0C1YjIY67OJdwPsDffs1Sg5SmWlIWjcDrOVQvB-MNHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtFJ1DiqGyFTTQPSjnipJPTUImNEU5m42PKjy5GzevB3CK9pqI-CG8SCUaRJhRSqYBMgZW7Zx7JLroTuSwUduDDdpgsOcZACAvNqdLj9Nn45rIuKjpmSmZxau8MZxk0NsFkHyIdVZbJlyKnsV9oj0WuPCq6QkRsXW1wTShk2cYr56EbMUVAu9oi6pKD7VggV0lOAiH1rKl1aIHfn8FwIDgvpW4GtEG5ueDp54LVXjzdjVLYZqlynr4eK6iwnLTn2UOtE5IuecmgS56Qv3_RrMFDGg5brthx0qk1hBpV1TF0m9YLWUizNf_Y2aP39nAahVMQyy-chutP_WCEz5SQW5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
♦️
اصابت پر تعداد موشک‌های ایرانی در پایگاه موفق السلطی اردن از زاویه دیگر، همزمان با شلیک دهها موشک پدافندی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/688902" target="_blank">📅 08:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688901">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiwO7oUCACx4olEtr5kx0OXi0tpCyx28sAvWkZBhNAJZC_dWqOyoI1ifA5VR0DNYBK3Kf2BqbejnNHYH-O3F2r0wdZAg998wszSF5xuyfLkPB_NAx49nHmCd3OeWeqnWI_J51dcQJFFy8gwFxEHt37nkao3eXZe2TC4vpyiiK9BOgB8fSvsQsybbHja2mH0wuAwasmIjlj7EjOCt164tzuKwciINIyjqNR5V48bsRv5nbXCynD-WuZFHVI-nM5IU2WbCnf5Q_eXL85_ZQDf9BuILKxsXZM05wqa6mvkH6-84TqAD4tWzGfNiYBbohYZ0oczlQHXSsbVsEz5TW__1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۰ شهریور ماه
۲۹ ربیع‌الأول ۱۴۴۸
۱۱ سپتامبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/688901" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688900">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1VXge4sT4BTivmHZNYbnd1QnIU3_MnXehtkh8vUzx89EfMv29SfPOxowPRPaYNF_HUXkh1bIzksS0FujhBESm8ym3Whj4HGrH0cxRQb0jZdqfj7lx6KzyIPU8zPAlFTgWBDFbvh-r_sU0yzVqUD767jUjxDwAnC1mgKVXQ5GxUWOCx42bAtG4iJClP13tDmWqt_rBWSWeKjtsqHNiR-LfE2mVSwswe9MlVZVJc71YqqGYvFr6qUqi8fjL09m4QRoNHMzHXHqBgPAeUdKVw46wAFc7SeYPM6QtQSpMVI-p-V5hq9S66H1S0qTqTcldt-wtP82D__O-_BMTLVlf5gmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰
کانال خبری و بیش از ۵ میلیون مخاطب!
😳
🔥
یه پکیج تبلیغاتی ویژه برای پاییز آماده کردیم
با شرایطی که شاید انتظارش رو نداشته باشی...
🍂
📩
جزئیات و قیمت؟
فقط کلمه «پاییز» رو پیوی بفرست
👇🏻
@S3eti_01</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/688900" target="_blank">📅 00:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688899">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdsmhcikq3UD-StqrR7Z0ZgfO7ocbjGHmxscOyBesf979RLAeQF7ZOqrk1Bba4hDKXvgDClYNUsO-5QKhVST4EomQa7-9DegpWmy07UlPKM1-iXraMGXh_iBn3_-0izmCUyZY7BDiQ2-uuPUk9uHZbIVZCkrXm-kXuwawkB-hgaDdZXgWwdnrr9f1ZGQ8yVlqT6f1zN70N15ajv8bc6pKvS9txDp_VFT9zM-U-akW0E0egnqfbFmZ2KcQ1S3YY15nv-GZS97OBZMzr67diuyqP5zSnx4XBaAkz_tLgxi78jvEgWe9Sfo6GndclFpwIOviUk0PTC67dddXZ1v6TtxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست راحتی مردانه سوییشرت شلوار مدل Mpower
✅
جنس پلی‌استر باکیفیت و سبک
✅
مناسب هوای خنک بهاری
✅
فری‌سایز (مناسب L و XL)
✅
تنخور راحت و خوش‌فرم
🔴
قیمت فقط برای امروز  1,198,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/51861/180124/</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/688899" target="_blank">📅 00:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688898">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiU_lpS25OMRZt7SWCvxOYwkak2x0iR_8dnHD01ExGobXmkISeTEkcibiGvbVu4rQ_9QB3twNAvZcGbSKFaqiw7c5wxdy7P5QLj3Ju5o48jauY3yat5uBiLF8n57ojAc4evs7rWEc52MJl8hXSG0WtTOTUWJT__yebNDgeZWn93PfwGoyKd6UyIOV_PyLZtSWw4sF72uL4uz16kDSttyw0He-_gfafwcJ5CD5fDsrZsbIaSMMT0LfeghNUkkPcEFc05qwz8dE5b6RdJOs6BxUSaVdOMbJA7zhmaKb0pzNS6Vp62Fl8mBR7BmkYRWN88cq1J5WnLeMjx0Yv9wd60lMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حدادعادل: رهبر انقلاب با قوت مشغول کار هستند
/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/688898" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688897">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اظهارات
خداداد عزیزی علیه فدراسیون فوتبال: فدراسیون پول آپدیت VAR های لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/688897" target="_blank">📅 00:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688896">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ee5a7ac3.mp4?token=NmRLrUVf6K-Nd96xO-mQ6MIlQG8eXx0wwXDJ3qP-j2YYC-eHUGHe0hGM8il-M5FkJS6uJiy05f7dDwtj6FRJeLvrZakK-Jx6kT9VisYH5TGGGePHo3hZ6_Wbxi1dtnovbtsg0T1RaOby85F08jmiKoOs7It-CSdu52eFnswtdazNPKJb-Mi8MKr-ABvmO7CcK-lbRcBOwVWvROFHltZiJCW6tEFVHKphzlRSAIGyNdwhf_tpBkj0hdm60c7AfTu39VS97lqVBsSZivEc2-C8CAeke80OEe8q-Q8YhYfhbbiuJxkyWNX8P97KdL0x1U4wZ93yB56h0-7z-be6U3ge5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ee5a7ac3.mp4?token=NmRLrUVf6K-Nd96xO-mQ6MIlQG8eXx0wwXDJ3qP-j2YYC-eHUGHe0hGM8il-M5FkJS6uJiy05f7dDwtj6FRJeLvrZakK-Jx6kT9VisYH5TGGGePHo3hZ6_Wbxi1dtnovbtsg0T1RaOby85F08jmiKoOs7It-CSdu52eFnswtdazNPKJb-Mi8MKr-ABvmO7CcK-lbRcBOwVWvROFHltZiJCW6tEFVHKphzlRSAIGyNdwhf_tpBkj0hdm60c7AfTu39VS97lqVBsSZivEc2-C8CAeke80OEe8q-Q8YhYfhbbiuJxkyWNX8P97KdL0x1U4wZ93yB56h0-7z-be6U3ge5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تد کروز، سناتور و سیاستمدار آمریکایی درباره هوش مصنوعی: ترجیح می‌دهم ربات‌های قاتل آمریکایی باشند تا ربات‌های قاتل چینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/688896" target="_blank">📅 00:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688895">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIfhuU2DyeSG3f2da_ZpRLLMFQfjU5fhMruLb8b_XwJ9TrNgQyicACt_rsOYFnHrU-8kfwVMB0njrQpRGp9JWhB54Yfa6mn13W25aarcnb4s0a7ONMRH8We3PPfBudfJdEDde3M0U1BliDo-qB4VpuM-D3UDEqffaFtw-v3p8TOPR8T5Iupb-eVQ_TL1QAKOqJUeYqiRAoRvALzN4yTk6_kdy_NXxMvBUxvUcGl3fkU-LKL_X61Sq8yevt_FKMIWDY9D4f46s3vH1gXN9qITZCItDuq63TtgQv2Z_Bft6D5Sp6bhkPTtO5-6k0brGnm_k2U_h_5yjE2Xm61zZqSfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فتح‌المندب
🔹
رسانه‌ها از تسلط ارتش و نیروهای انصارالله یمن بر جزایر راهبردی زُقر و حُنیش بزرگ و کوچک در نزدیکی تنگه باب‌المندب خبر داده‌اند. این تحولات در حالی رخ می‌دهد که پیشروی حوثی‌ها در امتداد نوار ساحلی دریای سرخ مسیرهای انتقال انرژی را با چالش رو‌به رو کرده است. تحولات ژئوپلیتیکی اخیر در منطقه بر بازار جهانی انرژی هم به شدت اثر گذاشته و قیمت نفت امروز به حدود ۱۰۵ دلار در هر بشکه رسیده است.
🔹
هشتصدوپنجاه‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/688895" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688894">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTt5ziltUVSijss_W59d5SSjrTmRnf2ug5oomqf25YUeza1aJ3W0qsooPSbpQK3iBuuEO7H1oO_mv0xov6f-1lotSzA8RGHRva4tztwPhcj3bVHY4OzNPIIXW4kC3FcBdGHv1jpi8R0IG-l8cXi4LLrSYuNcdAQ_q1v7C3f_lD-UuMzWhTLls26TYHECfnCLdc4ICTRUAjux-0SEjNJdS4Objm4QGTzFaYCitSts7biSl3xXxN32xXXHdgrJPtk9SHMXf9m9Xaxa-cGvt2ZSaph7Evi-5bg0PltgNbQzhJRpcrB1fXJSVtdMJU8ptxqMF66P-heB6dpxsAOgA7JDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۱۰۸ دلار رسید!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/688894" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688893">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
عراقچی و فرمانده ارتش پاکستان تلفنی درباره تشدید تنش‌ها و ناامنی منطقه و پیامدهای آن برای صلح و ثبات گفت‌وگو کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/688893" target="_blank">📅 00:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688892">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7bc4849a2.mp4?token=XhXOr4RdBzDwAFfTyQREV6zJx6ikIMfAS_SHT-oKAoSgGW5f3HE5roCdaO1r5INZ8k0rNbsy1gtk1uq1Yor6hK-3eA2fonA8_OukI-dnft8GZKyHoyi8itnyDZycS7WNPCxCXBz0KOpbbw3JknUmZ6LF3Pc60VtQgSErSnwe3f0SA_arVCSlQDk0U4qSdO1VFbGYqfnXvWCj8DgQCvW4ewf20T75sALmqOwkR-bvhH-FdGVZPmQcV0KUKr8YOTzRcaSDS4L_QomW7WQjaTO_75DZAP6LP32-7fnuVZiBzC9rXJ3nSDOvTJP-pfjo0Ct4JO_TRLw4Puck2VBq6Auq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7bc4849a2.mp4?token=XhXOr4RdBzDwAFfTyQREV6zJx6ikIMfAS_SHT-oKAoSgGW5f3HE5roCdaO1r5INZ8k0rNbsy1gtk1uq1Yor6hK-3eA2fonA8_OukI-dnft8GZKyHoyi8itnyDZycS7WNPCxCXBz0KOpbbw3JknUmZ6LF3Pc60VtQgSErSnwe3f0SA_arVCSlQDk0U4qSdO1VFbGYqfnXvWCj8DgQCvW4ewf20T75sALmqOwkR-bvhH-FdGVZPmQcV0KUKr8YOTzRcaSDS4L_QomW7WQjaTO_75DZAP6LP32-7fnuVZiBzC9rXJ3nSDOvTJP-pfjo0Ct4JO_TRLw4Puck2VBq6Auq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیقات هاروارد درباره محیط: اگر برای رشد باید ساکت باشی، آن‌جا جای تو نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/688892" target="_blank">📅 00:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688891">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس: گزارش‌هایی مبنی بر وقوع حادثه‌ای برای دو کشتی در فاصله ۴ مایلی دریایی غرب شهر خصب در کشور عمان دریافت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/688891" target="_blank">📅 00:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688890">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درگیری ۶ استان با سیلاب/
سخنگوی هلال احمر:
۵۶۷ نفر حادثه دیدند
مجتبی خالدی، سخنگوی هلال احمر در
#گفتگو
با خبرفوری:
🔹
در ۲۴ ساعت گذشته، بارش‌های شدید و سیلاب در ۶ استان ایلام، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان، ۵۶۷ نفر را دچار حادثه کرد.
🔹
بیشترین شهرستان‌های درگیر لاهیجان، رشت، کیاسر و فومن در گیلان و قائمشهر، ساری و نور در مازندران و بندرگز، کردکوی و گرگان در گلستان گزارش شده است.
🔹
نیروهای امدادی تاکنون به ۴۰۷ نفر امدادرسانی کردند وهمچنین۱۶۴ نفر اسکان اضطراری داده شده و ۴۵ نفر به مناطق امن منتقل شدند و  ورود به مناطق مرتفع استان‌های درگیر تا اطلاع ثانوی ممنوع است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/688890" target="_blank">📅 00:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688889">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5chEC6aCjbAdKJfTbC-jdtD_Ra-ebBTid4DMrtwNPQfkl0B2-wB2oMaKHveKwSxBob79ZXX4pFVz3WmuO819RoQDH-2U5hqEGptMHdkU7ZFLOQcU-rFAFf119wXOsG9TIe6Rz-FmVnu1H988wrAIN52w9JM1o3ciG7yN2XY7NxpkbzI0oSrcNAM_A19czfizoyXTebz0DKg8exsygkFNAVuCnInZpgNPseRdt8Mo5RZuIdCi1XLhhA8LZuVD4h3vXk2tU9ytPYhkp7Shg0lVcEYqLKdau-daI4dURLC3pHpL3uNL-IH8BHupjD5wmBHyWVGDvcELmfTbG6YXgrqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688889" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688888">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رهبر شهید انقلاب اسلامی در چنین روزهایی در ۱۸ شهریور ۱۳۹۴: رژیم صهیونیستی ۲۵ سال آینده را نخواهد دید
🔹
حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی: رژیم متزلزل صهیونی و غدّه‌ی سرطانی اسرائیل نیز به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگر ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله نفسه‌الزّکیّه، بیست‌ و پنج سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله. ۱۴۰۵/۳/۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/688888" target="_blank">📅 23:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688887">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
به‌صدا درآمدن آژیرهای خطر در شهرهای ابها و خمیس مشیط عربستان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/688887" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688886">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25951e5e50.mp4?token=oAAijKBoOPLWBLq0zfT7Ya7mce2-M4j06Uo8vwVTpZKNHZKURvPmafh8YACuaW2DezJg_Cd4Kx4vom2kOJ3jH0DDhPe97QU1w019QeQAEnCpy-KezVcwWS8PJMJhhanHZcv6Imm54h521qj_1KNE4yG6WCJJvg_ov85vpbaK9iQBzwi63euz4oSGcU5G5MzuI3Kzplb_Jy0qeOLM3ok3xzI6mX2xzYS0h4f06uO509EetQbNpT3Xy4_PhM75f2Q7WPaYziR81WaaPhADONlRaNnVtFxaXztCJS7AlyQZn0erEHS3fnBqHMsLo2NNpQ-fjXEEfCuYouSn34SK4289qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25951e5e50.mp4?token=oAAijKBoOPLWBLq0zfT7Ya7mce2-M4j06Uo8vwVTpZKNHZKURvPmafh8YACuaW2DezJg_Cd4Kx4vom2kOJ3jH0DDhPe97QU1w019QeQAEnCpy-KezVcwWS8PJMJhhanHZcv6Imm54h521qj_1KNE4yG6WCJJvg_ov85vpbaK9iQBzwi63euz4oSGcU5G5MzuI3Kzplb_Jy0qeOLM3ok3xzI6mX2xzYS0h4f06uO509EetQbNpT3Xy4_PhM75f2Q7WPaYziR81WaaPhADONlRaNnVtFxaXztCJS7AlyQZn0erEHS3fnBqHMsLo2NNpQ-fjXEEfCuYouSn34SK4289qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بال‌های کفشدوزک؛ یک شاهکار مهندسی طبیعت
🐞
✨
🔹
طراحی تاشونده بال‌ها، الهام‌بخش ساخت سازه‌های بازشونده در فناوری و فضا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/688886" target="_blank">📅 23:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688885">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
۵۴ روز تا انتخابات میان‌دوره‌ای آمریکا؛ فشار اقتصادی بر ترامپ افزایش یافته
🔹
قیمت بنزین به ۴.۲۷ دلار و گازوئیل به ۵.۹۷ دلار در هر گالن رسیده و نفت برنت نیز از ۱۰۶ دلار عبور کرده است.
🔹
هم‌زمان، دموکرات‌ها در نظرسنجی‌های ۷ ایالت از ۹ ایالت رقابتی سنا پیشتازند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/688885" target="_blank">📅 23:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAArQIt7CoVJNBsTt1i9tzsqNxAVumR8PtYX92Tj-B1pCvnjrq7S-_IiOqeMjItBjsSVdenE9QhBN89OV-q2mo3MgRVACSSUDxoFo_9aGUx3LKjvM8SxhPeCJpmKanJiQmWe6mrByU61gi_Xs8frhp2qboY1UsXteI2L6Z_-QoQp4D-vfIH34mO-sRoNXK9GfwX0EWbMoW6IfNexxFhm_DI-YR0Hq93hyDvvMQvlgi4pbqzjNFQaRXQk2FV6AKY9wagFdKfncXTxXtsEcx79KZAHKV_QcXfdV1Ji2aJVVxvxZvspAlbJBANiBtQ71L_B2WdditYNxa5CPeoTWjX4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
پک رضوی؛ چهار تکه با معنویتِ یکجا…
همراه با حالِ خوبِ مشهد و هدیه‌ای مبارک از آستان حضرت رضا (ع). پک رضوی مجموعه‌ای ارزشمند و دلنشین از یادگارهای متبرک است تا عطر و حس‌وحالِ صحن و سرای رضوی را در هر لحظه همراه شما کند.
این پک شامل اقلام زیر است:
🧱
مهر تربت مشهدالرضا (ع)
📿
تسبیح سنگی رضوی (سوغات مشهد)
🌹
عطر متبرک روضه منوره (۲۰ میل)
📿
گردنبند طرح ایران امام رضا (ع)
💰
جمع کل به صورت تکی:
۱,۶۳۱,۰۰۰ تومان
✨
قیمت ویژه پک رضوی:
۱,۳۷۵,۰۰۰ تومان
📩
جهت ثبت سفارش این هدیه ارزشمند:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/688884" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00287ee93d.mp4?token=knCQPWxBeBdRbtYyOxAnuhfPNZZCKVJi4fdhh1FVgy4H-ae6rDQbbmeGDK7d-iMP17yutr_vz0UZvXY2hYrz55CtejKfGSuxfpmz-lP0-Ie3NgiigWEsZcsz6cLUMb8wuMXMCU3gblX9I5rFnx5I6HpA8k_RGoaJmRoUfFcKLxNtbKOjKIEc1sBv2CpkzKAnv-oM38Jm5D8Sva0GBEsoVcIzQOLIrDQUE2FsU_bXGlvrqpCH9fdg9NPV6cT6D0gXJrMRs-EAETfu02mKDl9tUxNdxYdV_RfYErPdz9bfaX79nDfmjvWiUgamBCqJJZ43G6v9t9OUK20DWMIEj6gETwDjvHFJXQBYE1mVTSAJkz66_T8i1wQJlrN83TiMTEa37GAq0YKS9AxpFjQhgTGRgUgzPuDo3tuXX53NKpEPW3k8ZDGVXiFAteFuXmeK26jmv5JdXwyHd7PSDlEsrxKMoZtegfE9PUWXhO3LPysXUFhvYOwOwedtbNTbUnjAcwDfQK2a1K-1T-gwIxz4PJ0WozSYnuykc_8XlbjkW_zXEeSLo9avFgL_eY2V0HUCXiL_yF7_p-CB-tIc3ewD6gYIaQ__ISXGacEMPg66tN573pqAKA2GgKy1BX4S-oolbJ7aPsIrBb8TrpiIfUrbnMPW-QgmkacO0RXrVk12Z0B6Dr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00287ee93d.mp4?token=knCQPWxBeBdRbtYyOxAnuhfPNZZCKVJi4fdhh1FVgy4H-ae6rDQbbmeGDK7d-iMP17yutr_vz0UZvXY2hYrz55CtejKfGSuxfpmz-lP0-Ie3NgiigWEsZcsz6cLUMb8wuMXMCU3gblX9I5rFnx5I6HpA8k_RGoaJmRoUfFcKLxNtbKOjKIEc1sBv2CpkzKAnv-oM38Jm5D8Sva0GBEsoVcIzQOLIrDQUE2FsU_bXGlvrqpCH9fdg9NPV6cT6D0gXJrMRs-EAETfu02mKDl9tUxNdxYdV_RfYErPdz9bfaX79nDfmjvWiUgamBCqJJZ43G6v9t9OUK20DWMIEj6gETwDjvHFJXQBYE1mVTSAJkz66_T8i1wQJlrN83TiMTEa37GAq0YKS9AxpFjQhgTGRgUgzPuDo3tuXX53NKpEPW3k8ZDGVXiFAteFuXmeK26jmv5JdXwyHd7PSDlEsrxKMoZtegfE9PUWXhO3LPysXUFhvYOwOwedtbNTbUnjAcwDfQK2a1K-1T-gwIxz4PJ0WozSYnuykc_8XlbjkW_zXEeSLo9avFgL_eY2V0HUCXiL_yF7_p-CB-tIc3ewD6gYIaQ__ISXGacEMPg66tN573pqAKA2GgKy1BX4S-oolbJ7aPsIrBb8TrpiIfUrbnMPW-QgmkacO0RXrVk12Z0B6Dr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۲۰ مگاوات انرژی پاک و تجدیدپذیر برقابی به شبکه برق کشور تزریق می‌شود
🔹
چهار واحد نیروگاه برق‌آبی چم‌شیر در مجموع به ظرفیت ۱۲۰ مگاوات به همت شرکت توسعه منابع آب و نیروی ایران در آستانه بهره‌برداری رسمی قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/688883" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
