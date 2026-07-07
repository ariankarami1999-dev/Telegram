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
<img src="https://cdn5.telesco.pe/file/DBUGyP9XCfgTskyw8EO2l4-RpnBK0_ZTVJWRtCI5E91WaIR6xpo2WHurdDurbgmH6xqcmllNw-UjnxmcpsO0d1oe-1Uv_yAmQrWuBOdtwPYAJWXva-WTUxitvYs0kQIZINNLH44h-RgFA8sccEI-2Ny-1zNJW6tXAbmlcBXP4gcDJqHGpolqv1_Yg051_vs4Jk95oaTlPCPveQkVazjw6hv1rsWx2bZXGe8TVociXohw8qF4np_vMxbtuyb8oyEO4EgAY87W5l98c6uyVxzLceXbO2eltfrEWo9rT9-s1wI87MTfZAZr42z_vwEj994isPXn70fnvwK6ZJIIXmt-Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 622K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-98760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4HSIayb7GyKDWWTAaEYmiYN_7j4W9qIeAHi_xpMaLp-l9Zfzb1-Mz5iK4mrgxUZttaTmp4uao6E43JMTFFeum0gH1ePcNw3Xe7VTL2ZqQ8nCnikajpr6icAUyAEUenhE3nzh6jJoVtEWpKrqDhvYsRUw4Gb80tfzaq9n3UFc9KXWMvFEUm6GpODTyu-_Aux8BJNYomajX52tGwdbX1ZGONpsXXOcKJOuw4bcggEGokX5pybfdaews1tKOzpIQ0z0cagHScicJy12kfrejxTpy_iKRFeViHReQrOknCQIGWIFDzDSiacuAPlvW6xsGfm0fRs-LwZicQE4YUktd9MPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
اینیگو مارتینز با النصر عربستان برای تمدید قرارداد یک ساله به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/98760" target="_blank">📅 11:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Pxc_emWVzkWgBneIfrs9DjSz7PRMk4MfENlqZ_16Zzd4REOdT1YaTOG91mzN4MdxWDnCnJMVj3IIHQhXcJedqsplPJqyrKDwF3WUJa75plxKXWJhC73zTiQ987wh8ke4bzUcN_kt86MyIwH8r-oEJ3Qje1GvpITUMM4WeQ3uXbmQSUdGlfqdfb1q3a2mquTq52ZemAFj3t9nz_eV-d-XhbDi0eI2XH3F6Nrw15ucHYVUQOf9IcYH3XvxQ-3RY5K1LpejVyCWm9fROHx6snu1dCoCssrldxszFXjzmUZooI_XmDlz-azODfagQ0Apmiys6HB1YlM9iSDqoJIt_Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنان رئال مادرید تا به امروز، از بین تمام تیم‌ها، بیشترین تعداد گل را در جام جهانی به ثمر رسانده‌اند.
⚽️
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/98759" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
🇧🇪
خلاصه تقابل آمریکا و بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/98758" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ-1rofA9pYvpp6gt4kP3N8KW2A4Xn2Gymqhn2bMpA6uo3kSUCy2DXG2UwHRTJjNZpMjZqtrxF6f6TW-sPZNA4EK_BpxUmAvf7rYwQqWTgFQK4Pmsp0zUA1ZCaZjbcMV4LL7fV1nCgXL28DQmP2JYA4BTB7cna_sqIMWj5iFfR_BBHNQhW0LPnGt9bblfdvMg-w6kMwISDAmjQB_oeBIIkiJcn0o7mdYpu4EV8RvqOftXawnM6upWI_Z8pOoEJYeKCIFenOo9OwR5kZ3wd0XGT4bMVYLcZ9t-6tSeezLw5CvOF517ifzhwCU7Rm9XnMbpFedpL9DILB0feNBze-Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استوری پیج تیم ملی و کنایه به حذف آمریکا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/98757" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6KyX4WQKOVwirJpxEjrG_LKB-RkgZQT-SlUK9jQG8wpX-rpwxSlxdQ_JYKWSp_-hrvYWNOPW2L-7rMd9r0ruR6LqX6eNCugrpYMx8T9pvsbmtWpCGq5BOoyz3edTOdvnjryo2BaLHm-KDBTjSk7zNevoo3ZEM0RNRawArf_Y5Z8AhR5HjakP1tBlkqeXAMwKEkdJgk_NMgWuFzp_8Npx1GhaHTZhnTkQUFkW0S0LWzn04fitt_SaR0G-kKqU9ig80aoKyx4JDq_XBGNSRfXKnZfKGejgj_iIJF9k1nOLV9P7bqNpbEqbVhYGAiF53X_ccVlqoWfJK7RU1UJG1JjI-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6KyX4WQKOVwirJpxEjrG_LKB-RkgZQT-SlUK9jQG8wpX-rpwxSlxdQ_JYKWSp_-hrvYWNOPW2L-7rMd9r0ruR6LqX6eNCugrpYMx8T9pvsbmtWpCGq5BOoyz3edTOdvnjryo2BaLHm-KDBTjSk7zNevoo3ZEM0RNRawArf_Y5Z8AhR5HjakP1tBlkqeXAMwKEkdJgk_NMgWuFzp_8Npx1GhaHTZhnTkQUFkW0S0LWzn04fitt_SaR0G-kKqU9ig80aoKyx4JDq_XBGNSRfXKnZfKGejgj_iIJF9k1nOLV9P7bqNpbEqbVhYGAiF53X_ccVlqoWfJK7RU1UJG1JjI-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
مشکلات واضح کریستیانو با برونو فرناندز و سایر بازیکنان پرتغال در بازی دیشب...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98756" target="_blank">📅 10:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98755">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b541523a.mp4?token=mmdyR3EhrnI9haPstaAp2hU-IqGgKGACItpi2QdYsr66oY8bJQYh7x0hgmqPsB8TbFHBs67Epl5aigJx1RX5QzFQ1vvXCR5jaNa11mTU1eZjn37ITgtZGzhinXJ3RnwMz3xpcawkAhmZoJ-CvKPSF_YRNw9mJrA45yHnT0sRYPMtoqo_5L4ZrRoARBaLLXyx8FSfwN0J8muXgPNJpua1a3iY6DI_fSsXFKPoBME5e6XbdAc70NKeG1Nxs1zjxZkf5xrrRNXBu4uE7ge8BmrH3cBoXQC38TRuN2SUjfJ5sYqbBUwAtwGuxrP7cy7motNBYGqunHr-mltMBJWTSTCz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b541523a.mp4?token=mmdyR3EhrnI9haPstaAp2hU-IqGgKGACItpi2QdYsr66oY8bJQYh7x0hgmqPsB8TbFHBs67Epl5aigJx1RX5QzFQ1vvXCR5jaNa11mTU1eZjn37ITgtZGzhinXJ3RnwMz3xpcawkAhmZoJ-CvKPSF_YRNw9mJrA45yHnT0sRYPMtoqo_5L4ZrRoARBaLLXyx8FSfwN0J8muXgPNJpua1a3iY6DI_fSsXFKPoBME5e6XbdAc70NKeG1Nxs1zjxZkf5xrrRNXBu4uE7ge8BmrH3cBoXQC38TRuN2SUjfJ5sYqbBUwAtwGuxrP7cy7motNBYGqunHr-mltMBJWTSTCz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
خوشحالی شدید میثاقی و دیگر مجری شبکه سه سیما از باخت و حذف تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/98755" target="_blank">📅 10:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98754">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2731679c05.mp4?token=mIDEamKAi6dvygxQ5lhWFHYlUdpRpgIiq9s-oeBIEGI-ziIB2VH4qTfr5wk20Z31j0-5h2qpJenhZCn5VpcUwcdjB2ZTKjzIxCbvTHseS8jBGxEf_zFyodZ_K2tzFJGf4_hmbZqttp4WgR3B4tL9tKOXrDCjAatiJJJK4_FPHxsJetLplk6P-2zxaLP9JQ_BuC5sN7ZNk80MQCyIlGNy5liqtOg9r122-ntVEc8DIGPLZLiWFppSczi7qpo6LJmyUix0vX0XEKnUPm9223ra13pndZEMOMK0MJyYyMpCff-4vT44l7hMH92IW3_FFZdA6SP7D5P41Ki70u2Xw_h0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2731679c05.mp4?token=mIDEamKAi6dvygxQ5lhWFHYlUdpRpgIiq9s-oeBIEGI-ziIB2VH4qTfr5wk20Z31j0-5h2qpJenhZCn5VpcUwcdjB2ZTKjzIxCbvTHseS8jBGxEf_zFyodZ_K2tzFJGf4_hmbZqttp4WgR3B4tL9tKOXrDCjAatiJJJK4_FPHxsJetLplk6P-2zxaLP9JQ_BuC5sN7ZNk80MQCyIlGNy5liqtOg9r122-ntVEc8DIGPLZLiWFppSczi7qpo6LJmyUix0vX0XEKnUPm9223ra13pndZEMOMK0MJyYyMpCff-4vT44l7hMH92IW3_FFZdA6SP7D5P41Ki70u2Xw_h0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💔
💔
The End
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98754" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98753">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=YyKAeTCTU8dmP3QqyLgP6P_kF416GiIyp-d_lN7N9FJtgZq1NThV1e9kw_HrooQNsKbCrG_c8iL274mnCpMwG_4CduUPpihUzrxilqFmltdAfpSuqOiQys3PJgR3t2FPPZXKBQxSNxlj_-Xe8kiR0iybBtVQa8l2nJx5TrkIops3UDknCLGscdnlNAk8zdqQ4iu8r54zE54KlE9zBRtCQa-xRnEgF4Icz0jUbTQVyqyzhoXxFlJ3al8LQP3XteQJUHzVLO7Xxo0od2lO1nS13BLjJtKgJVenTf2Muq7S9B76bkFD61LCuHPGHXBGwbqx_aQVhj1K54sniFLHHTIDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=YyKAeTCTU8dmP3QqyLgP6P_kF416GiIyp-d_lN7N9FJtgZq1NThV1e9kw_HrooQNsKbCrG_c8iL274mnCpMwG_4CduUPpihUzrxilqFmltdAfpSuqOiQys3PJgR3t2FPPZXKBQxSNxlj_-Xe8kiR0iybBtVQa8l2nJx5TrkIops3UDknCLGscdnlNAk8zdqQ4iu8r54zE54KlE9zBRtCQa-xRnEgF4Icz0jUbTQVyqyzhoXxFlJ3al8LQP3XteQJUHzVLO7Xxo0od2lO1nS13BLjJtKgJVenTf2Muq7S9B76bkFD61LCuHPGHXBGwbqx_aQVhj1K54sniFLHHTIDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب فوتبال گریست.
💔
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98753" target="_blank">📅 09:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98752">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=Cif3qn6QSFK7np1xwD9XX6hYrANoVAaKRQoDyVA6CtqnV32fipiiQi3khom2KwmpJCvTX4affVpdQbn7X6ZPvPDv2FjxEboUbD6YWUA1-gM1zmZNO0ygkFy-mJnz3xOMfJUP4Isie8a7jzYTZ4KO6abJcoxWRpxTEnCX2H2NGSKAtybZHDkrGDmhoJFaqqj1hRibz7JcitmDgl6gtGWZq0PqKTfx2aXAzXVqfpkYs1DSsB8g1_TL3iSJE1iTNSpRSwxAclqOkeoOoF-_owc2xMBlkF9wVPUwFMZvvZpUhn9L_1eEI0I9mlp0CIPZZ-UjZyudreiH0F-vxxClVhGQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=Cif3qn6QSFK7np1xwD9XX6hYrANoVAaKRQoDyVA6CtqnV32fipiiQi3khom2KwmpJCvTX4affVpdQbn7X6ZPvPDv2FjxEboUbD6YWUA1-gM1zmZNO0ygkFy-mJnz3xOMfJUP4Isie8a7jzYTZ4KO6abJcoxWRpxTEnCX2H2NGSKAtybZHDkrGDmhoJFaqqj1hRibz7JcitmDgl6gtGWZq0PqKTfx2aXAzXVqfpkYs1DSsB8g1_TL3iSJE1iTNSpRSwxAclqOkeoOoF-_owc2xMBlkF9wVPUwFMZvvZpUhn9L_1eEI0I9mlp0CIPZZ-UjZyudreiH0F-vxxClVhGQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خداحافظی رونالدو و پرتغال با جام جهانی 2026! اسپانیا به یک چهارم نهایی رسید.
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98752" target="_blank">📅 09:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98751">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=AWpPwpvRFeOfsohb8GdensTGIf-cdsGJ8DjEG1Iy2BaDupggMgFYp7Wleqsn0WTVZxes49f0YabtfVXdqt4UlAD--Mnqkky7zydKL5antRqGKKHP38GzmQ1e6bZEpGRva4tLcTAMDhqhXDC2fboaQXYwjkd4EsA9I6YzXiUNHGpoxEV35m3okWmSAekqAuVTZS-wo18KD_5N-4Z_j1lZL7XlImGhME-6b_As2uUN3Me_s-F9mChax4I27Gz05Qx7oFxn1ARff1bIRXXccmA0fVKaard9CMRYg_tI3ac3yuykswGXsDp2eSwkF4P__niTdcyuizt09mosjJLDg8NetD6Scdk2b3I3Q7TjJBjyBGdMlf8TIt02KnM88ud644_1rFNvNSTc9dKCeCxOWUhumsRsjAzW3YEY9r097fkWDkb_qLfsADOYf7zN3ka_m-vZ6MXsP6OWEEq3LIkMBZbrlW6SNxCPcX1I9XKUqm1laK9k34Xi8pnwUNUeRxwbZ1BWVhzaxuOpQm_d3cGjgM8xRDAIj_xeBHMqlYxfkrxb_sFgY0qoqTv_eUWB9pusseOnMPU7FSM5gu1jtYGaUQG2XhEb41wuRAlCD5AR-5UVeDNVWK06VL0Xi2TAX61Q8YcQki9KHI8taMhTjcyJ-BnRg1S_TTJdbWSt1I0TDPG1De4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=AWpPwpvRFeOfsohb8GdensTGIf-cdsGJ8DjEG1Iy2BaDupggMgFYp7Wleqsn0WTVZxes49f0YabtfVXdqt4UlAD--Mnqkky7zydKL5antRqGKKHP38GzmQ1e6bZEpGRva4tLcTAMDhqhXDC2fboaQXYwjkd4EsA9I6YzXiUNHGpoxEV35m3okWmSAekqAuVTZS-wo18KD_5N-4Z_j1lZL7XlImGhME-6b_As2uUN3Me_s-F9mChax4I27Gz05Qx7oFxn1ARff1bIRXXccmA0fVKaard9CMRYg_tI3ac3yuykswGXsDp2eSwkF4P__niTdcyuizt09mosjJLDg8NetD6Scdk2b3I3Q7TjJBjyBGdMlf8TIt02KnM88ud644_1rFNvNSTc9dKCeCxOWUhumsRsjAzW3YEY9r097fkWDkb_qLfsADOYf7zN3ka_m-vZ6MXsP6OWEEq3LIkMBZbrlW6SNxCPcX1I9XKUqm1laK9k34Xi8pnwUNUeRxwbZ1BWVhzaxuOpQm_d3cGjgM8xRDAIj_xeBHMqlYxfkrxb_sFgY0qoqTv_eUWB9pusseOnMPU7FSM5gu1jtYGaUQG2XhEb41wuRAlCD5AR-5UVeDNVWK06VL0Xi2TAX61Q8YcQki9KHI8taMhTjcyJ-BnRg1S_TTJdbWSt1I0TDPG1De4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
▶️
امیر مهدی‌ژوله یکی‌دوسال پیش این حرف طلایی رو به عادل فردوسی‌پور گفت. بفرستید برا هوادارای فوتبال خصوصا رونالدو فن‌ها که بدونن ناراحتی هیچ فایده‌ای نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98751" target="_blank">📅 08:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98750">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=SFBh_KLLI15cSMwzCismcaPQAkN5sco1nnSVvr0JkHSi6ocG3ClUTOOeSvF8PuMs_RHeLohpVeeir189m9feLe6vC_r-3OQYQ3rALzqklktE2PTe-G08h69_1HO7Ab4dsYS8ldYjRK88dC9muOgDdsx4cpOp6f2bx5V5Alh54JkpHHMsllsdBjAdiUOKCmLMTJbh_RcJ4XMUsVSA52V7ZSgqdtCcokmMB2p15yFFM6xg194VlV0Mci9Dz8kJTExBUwFatedt4_Vqd5YeBmiUngICHLMmaQov-wAVyslTf3qbfbFxcq1jIHifnjeX5WzfcSD7oPeWx0A41JxBvxM55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=SFBh_KLLI15cSMwzCismcaPQAkN5sco1nnSVvr0JkHSi6ocG3ClUTOOeSvF8PuMs_RHeLohpVeeir189m9feLe6vC_r-3OQYQ3rALzqklktE2PTe-G08h69_1HO7Ab4dsYS8ldYjRK88dC9muOgDdsx4cpOp6f2bx5V5Alh54JkpHHMsllsdBjAdiUOKCmLMTJbh_RcJ4XMUsVSA52V7ZSgqdtCcokmMB2p15yFFM6xg194VlV0Mci9Dz8kJTExBUwFatedt4_Vqd5YeBmiUngICHLMmaQov-wAVyslTf3qbfbFxcq1jIHifnjeX5WzfcSD7oPeWx0A41JxBvxM55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
وضعیت آسمون بلژیک بعد از بازی امروز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98750" target="_blank">📅 06:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3BFj3-MOKZLZmal3j8mBHdAZh301MVEoNo53oAhYeciT7MmG7-BcKQSntxSwI1uiD4xvIOxBWmYRTigK7LSs4gC0tS-_pAhl_UC_vDdZdling3JjYWH89qRZqjSxFYUy3HAdwjM9lfjsujcsYiGVIhqlpiM5YPbdwT8a6vFyPcFJrwHoES3PzX2iaIs_MPelTsApI4tuJt3IYaGpUFoG3CcN4YKMUIlkW60f3FfBg1OUXxWIAFKG04yNpbaV3sm0N0-D7O01j724lUjaX-PuP049Li9ESVgKYBTev9TcGXMXMiajWlf3IziXk-f-dhpGdz_AT653hcfN5voGNMqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98749" target="_blank">📅 06:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGtaNIDXH6KGUryDa63rOy1EcFoPD-hMZBW2nWp7Q_LYw1jctLbIEzU8kTPyR4Menm3oKAPh3HFnx_L9ayA-OR_IVY2dagQgl2VC2IUTEjeQOWxYFDOmOZT6CkZjsTkbF6BoX2QYZZOxsr0gn20vC5nz5ZvzMREU0Ntt_BqZwTHCCfLu2nv1SUrS9vTgkuGNASn-N0xNwuZ_-Tsc2dAVzXma2TEzBnr2VA6gadYRGflk_IWM6fyiseF7IK3OnCRA8hx4ouNV2L-4o9TmN9q3o7oeHAHRZYmhK9IWzZ47IXDc7nYgDEtK6B7ZIBuAPJI5Gp7UUDkCAB4zLDvN_2T_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98748" target="_blank">📅 06:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkanwpFZVwpe3Yp685742g4NKbpIHxK8QvK-6WmC0tFl-hAw4EzePFL09gUGz8ptcVz-HwoucDGgiE-aRaPwb7rxjxKbs0Coj-Dv9yqDjgx5hgPqS9jmqJoEo8aA0rO-bWGjnsftc8jhtHtk6iAdVRSm01ETJawm6yPeTsrOtfrwJblNRNlK6Thb1lPioQ-igDIy10F3qxmqAApooqP1UC4Gc4q9pIsoxOv_FGWeYbZAMrWE43A2V4aAS6UczlQY_7NWVe0DR4jqTBog1joOBRZufqpS9mET1Hrw5hENtZYhfvtdfUEZOhqy_VSMwDDvllo39FeXiuGv4T4OBHJ0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج توییتر تیم ملی بلژیک به آمریکا: به این میگن
ساکر
فوتبال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98747" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYpY1AJ3i8d-SboAIocxbFPGeBk6XmYPPrjzpy2MPB5yIyLaZePUcRUHh-mNkYGagAG2AeqnDUftK5nwc3uIa0E6s3Lt4xaFvpDWfiYrjbhlHJvld0RitupJaI7cX9fOKQOVKHjq8Wu6_dOYtPjf1p3XSKREjlBHHxJBZ08kFxQkkg6yafU4g7QCja4S8iVYCymokW20RAwEVfOk9cX8o8Rht36x2SshhC_sL6GbDFLF0fBFycLgwRp7mHcxYI_Bh_MYpTNUJkF5fXI8aqlDWPoqVDvQj2J_niI2BmQ4Y40Ej7LFHlOa6xxl1rbtQ6jddoNV404ivbkOR0MoKR3eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابل جذاب دو ستاره این‌بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98746" target="_blank">📅 05:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98745">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BobE2QSoKQ80LuQIdmNFVWb5_InAdBn0pTLontmVSqDEBxrGcrH2hGAlAd7akXdjKpxvlouOUv3s2n0VUaj0tkJwkaQJ5cMcKt2LaCHDwwdNHliIgN2QadJG0J4mOEXg-7PXTd0zSWCa1bnfZAk-TOlgLQaGxNfsr_8P5EObpwrCq21DL3m3nc7puNIQkfNxCvOgOI6IlSVlwEcExvmS3YvLCgFP1odqoTMLZ3qO93uZ43ebEeS4oDEOFDARptc1NaKoZu4XsY0umVM1pOGkKXM85h5ycXQAhRUB3Cz0wXxHrvw1npb9ul0x8o73QVEtopJbke6D5art5bIK_sjOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇪🇸
اسپانیا - بلژیک
🇧🇪
📆
جمعه، 19
تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98745" target="_blank">📅 05:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98744">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7macHP-2wy2mN5StMVRQy6FUOwGyTk65FnOgrxnE76Pmrpl5Kv_pCnH8I9lDXJaRbwcpQZFK2S1ygy17pJyq4TtP8gLYdqYjGAi1DwidRNgxOsIDyWgsAhv_7I7vP_6zCQMu0tCJBn-qnomryAHFc53LUUapUBsfRWcceeq2zjD2fZgssxlFOMF9gwpY9q7NwcdqUg2OWBzBPpNNgxMg31WNV6e66psMlbt9FAIEM3a-YcM0CZ-3if7UnDfTuVZhQ-Y6DTdewoeFW86kSDVou0UKIN1manqys-RktAY8snnsUh0adKILVO8OCm8gOoEW2wZG9IaE8vC5uBvQ-A6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98744" target="_blank">📅 05:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98743">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAMua9AER_YSgBShkJe3qT4OI5AZwtGxHRZ0OGBp4sDv278MKI6FBf-IBWTI0EGRMTEyr2Eip3bWdW1oghXf5jYWx-E9TQXA-rwlPzMJT6gUMbG4V6DbU1gslV-PmlRTFcewd6mBzeZJLe1MjxKeueLoNTqXvi-KHHBPKnu-Yv8RvIwipiazGqlUa3fCV6q4doNBOMbo0F_pxZ0esQL8ReJuA0VXX9Eq9jXxI_TsNP_8duip09Orp2NP8wHBHIsObz9BtsYycZVEak9joeqKo0SUn8B626_0CokUyWsklqexw72xJHkHKhk6AGwim6hsmtZrDh3XtiGHhTelmhBLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد قاطعانه بلژیک مقابل آمریکا در سیاتل؛
کارمای بالوگان!
🇧🇪
بلژیک
4️⃣
-
1️⃣
آمریکا
🇺🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98743" target="_blank">📅 05:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98742">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=hbCwasM_FVldeawmGoLBopdpW8_4AvDNY4QFkHRWfu2MWckGsInLSrtSCPrhFNGXVENkPWcut87BwvNyWzXmQ1qvlkZ1M0E39ZZUHvhJspKQp0GU57UtqmiN8H2tx0NOo6YVKDTTGfuZBYH8h7ofJeIq_G5zquu652X-z4YEwH87b3eHgxmlZNihRF91MOeBCnf_v1Z09qs17qTV1vKPY9yVyiVmune9NojXPJYmQ-WRM6vGnpr4dw-hSv0Pk5Agmp2K9uBl1xR678CS835KzrMLi8TcyeMPPBqZomBtA7ezyGAsJH8pUjRjEgVsOkfpeXpfkLmPosPZOMjG0juQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=hbCwasM_FVldeawmGoLBopdpW8_4AvDNY4QFkHRWfu2MWckGsInLSrtSCPrhFNGXVENkPWcut87BwvNyWzXmQ1qvlkZ1M0E39ZZUHvhJspKQp0GU57UtqmiN8H2tx0NOo6YVKDTTGfuZBYH8h7ofJeIq_G5zquu652X-z4YEwH87b3eHgxmlZNihRF91MOeBCnf_v1Z09qs17qTV1vKPY9yVyiVmune9NojXPJYmQ-WRM6vGnpr4dw-hSv0Pk5Agmp2K9uBl1xR678CS835KzrMLi8TcyeMPPBqZomBtA7ezyGAsJH8pUjRjEgVsOkfpeXpfkLmPosPZOMjG0juQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🔥
تقه چهارم بلژیک به آمریکا توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98742" target="_blank">📅 05:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98741">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بالوگان فردا املاکی کونت میذاره.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98741" target="_blank">📅 05:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98740">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جوری که بلژیک داره میرسه به یکچهارم نهایی ماتحت خیلی از تیمایی که حقشون بود تو اون مرحله باشن رو به آتش میکشه...</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98740" target="_blank">📅 05:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98739">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=MbyrfCBJph8M8OwNksOpEaGUYsJiYqaog2M51Ul_KJEjDfCmsbbNtPTX3Z-9d3XmjBFzV5l9RPY7i7J1sD-K-mvpRv_2r6OsPiVengewkkUoRyVPxidUW264Asqa29AfkNTk0QhBegdPuMdq9qbGdePEQX0U7h0WbUaEiZe-4_SkPTJmdwLJuODwfCO_OI7o9mPHVdjwJneFrYVdLCm6wvp5NdHote-_dTq4aToaG4AIojFb6_68hp2-n34gdzz36XNXWkNnWRZVh6qLZBkMW-iN90lWKK0h-5V5jSjeQhNhPrUXga937CcAdqIdI2XAcI2Yk_qnFkeUWusQ8BiBQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=MbyrfCBJph8M8OwNksOpEaGUYsJiYqaog2M51Ul_KJEjDfCmsbbNtPTX3Z-9d3XmjBFzV5l9RPY7i7J1sD-K-mvpRv_2r6OsPiVengewkkUoRyVPxidUW264Asqa29AfkNTk0QhBegdPuMdq9qbGdePEQX0U7h0WbUaEiZe-4_SkPTJmdwLJuODwfCO_OI7o9mPHVdjwJneFrYVdLCm6wvp5NdHote-_dTq4aToaG4AIojFb6_68hp2-n34gdzz36XNXWkNnWRZVh6qLZBkMW-iN90lWKK0h-5V5jSjeQhNhPrUXga937CcAdqIdI2XAcI2Yk_qnFkeUWusQ8BiBQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل سوم بلژیک به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98739" target="_blank">📅 04:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98738">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/palChTQ3vk7u2ycn8I6HuBnF2PVmkfQ0KZYcnC-5QdOil6fj0rPcrZCubRmkIsHZJ95Tf8G0W4ISpIbY9OB84pqzjELTykTrw2JgOit9k-SvQ9KmLflRDWnPu1JRbxJp23OSRkmn6Tf0EtPYUFibr80FEhcvo0H2jC1swEZdsWltKnSiuDyCEEiRotPJeNpFE_ck148NQrKAPNtwNSt8bQdBS7LcDJP9G2SeIuWG82X19hQPiJgLoWxPOdLoDFS1A-DuvL-zNtVj36XxvJf9sEICPpydBPmuLYvo3U1LbamN7fkWpWbZ2OzeiciMpvgVyk4T0Kc7Ug5L3mbpztZDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی ترامپ قرار نیست برای گل‌زدن بلژیک به آمریکا با سنگر‌شکن B2 حمله کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98738" target="_blank">📅 04:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98737">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=mlqrccZ7TaB_nHIvOy1DANSKOI0aR3Yovz36FAEsV5T4piVPALgxDGnx8e0hoYvqHYEjRXnX-cMPkFjCjhGf12YFz9eXsib4C3hV2QL5H50ltgrHbk6fx09kcy_UfOiwvKk-S3q_rSyAVQYmSjtVJWgsBzA3W9gFP7D0O81rtEe8gyy1zaqMym2rtdbQKAOqNe-R9nKcWHuoP1pJzkSQMNa8hPNuWeqsFBtvHxe0p98Kd1ZpzJDxPmwz8sFHZVqG1iI_8tKjedTzqsmnwYt7l8FHWCE0DLTzTyP-_Ad5XBlMd8Sno5XbdkKJNDchxZ90s0568j40ofu4c2F9bz6lmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=mlqrccZ7TaB_nHIvOy1DANSKOI0aR3Yovz36FAEsV5T4piVPALgxDGnx8e0hoYvqHYEjRXnX-cMPkFjCjhGf12YFz9eXsib4C3hV2QL5H50ltgrHbk6fx09kcy_UfOiwvKk-S3q_rSyAVQYmSjtVJWgsBzA3W9gFP7D0O81rtEe8gyy1zaqMym2rtdbQKAOqNe-R9nKcWHuoP1pJzkSQMNa8hPNuWeqsFBtvHxe0p98Kd1ZpzJDxPmwz8sFHZVqG1iI_8tKjedTzqsmnwYt7l8FHWCE0DLTzTyP-_Ad5XBlMd8Sno5XbdkKJNDchxZ90s0568j40ofu4c2F9bz6lmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل دوم بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98737" target="_blank">📅 04:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98736">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=U3Y_1E0cU4h50tqfEiTkV2z2sXAIR4WS8LBOfvbmGw05sBOD_j9IT2rgqu_6CNt7IGEWIv7BqyQC_mVAlgRFk-HvD2PFRpbwu6BC1M-zP77obHFpXphauT2n1sfvPVLYnDNQO5psa7k51s4585FjDgXC3wl9iHDpHT7yaf6GVm_xgZNvq-OMTUkq61laMKdcBBX_uvr_eYvvp0Qgd-ygdCBQNol2_tzaEj9gv3vX3szLDvT7LfNnVFLAVRZ5AfKD8hpht4JTyyQ4ubgwGjRdcENTydepuETZd0c6V2ewrR1OV_-zY_J8Ejq5_I4C8kACiC8GsVceFMzyYfSUwofwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=U3Y_1E0cU4h50tqfEiTkV2z2sXAIR4WS8LBOfvbmGw05sBOD_j9IT2rgqu_6CNt7IGEWIv7BqyQC_mVAlgRFk-HvD2PFRpbwu6BC1M-zP77obHFpXphauT2n1sfvPVLYnDNQO5psa7k51s4585FjDgXC3wl9iHDpHT7yaf6GVm_xgZNvq-OMTUkq61laMKdcBBX_uvr_eYvvp0Qgd-ygdCBQNol2_tzaEj9gv3vX3szLDvT7LfNnVFLAVRZ5AfKD8hpht4JTyyQ4ubgwGjRdcENTydepuETZd0c6V2ewrR1OV_-zY_J8Ejq5_I4C8kACiC8GsVceFMzyYfSUwofwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کاشته خوشگل و گل تیلمن به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98736" target="_blank">📅 04:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98735">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=lduB8LpMRKD_kUZwPqnJGMaeDnYWCEGkYtayqlmi2eU3N2221xN091nAP2637V3qh9H72WVwKXm95NRt10PAvUFuvbxwG8w7DHTArngQawk2vmYu1eCSlAiCUpxf3aTOVTj5KWQhoApEZjcBX6ekqDHsp7reafy3MIfcrYwZJzobyUcO6L7VOuYjYxgdZKvn28aZdVZQxDPxtu1RQM3PmKzsMGqy07sffs4xsBqk23D4GP5lcPVtyFwOgRBdyCJ3NZKr1RcB8biWUFqq59VbtN77f1lRHDeuLAMJpM2HUcEETTrXv3h6OuyiKsk00UfUXZNLff9S2-VL5F2w9AeA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=lduB8LpMRKD_kUZwPqnJGMaeDnYWCEGkYtayqlmi2eU3N2221xN091nAP2637V3qh9H72WVwKXm95NRt10PAvUFuvbxwG8w7DHTArngQawk2vmYu1eCSlAiCUpxf3aTOVTj5KWQhoApEZjcBX6ekqDHsp7reafy3MIfcrYwZJzobyUcO6L7VOuYjYxgdZKvn28aZdVZQxDPxtu1RQM3PmKzsMGqy07sffs4xsBqk23D4GP5lcPVtyFwOgRBdyCJ3NZKr1RcB8biWUFqq59VbtN77f1lRHDeuLAMJpM2HUcEETTrXv3h6OuyiKsk00UfUXZNLff9S2-VL5F2w9AeA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل اول بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98735" target="_blank">📅 03:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98734">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9kkJhglmMjlEXD763G7ssT-_F4VAz7laEG_RMapExJTaWcX2z_K2c4WYBpbS_-yqdhlxrHEFsTfJZv0Xr-wY3v6Cby4r7y090WskTI5jHqxoL5DTS_YWXSs7-yub836BHubXOq4-RC7dAjpuFPKXBY96Z-wu4B9XgjDtsLlCEpzY6vIgAMTnFkx6-Wq_kAB3cFlFl9E6rTvSSmuPQ0IEE0RkBwQ3udUXwB0GkUfH63-rS19zPL6pcndU_zagWOULRMmLERF_K863RGBQswxbo_v1cGWF2D5OceEWTvLzHSjsUMaGgCFX-4bJYhE5UQiEG9vSA_x2bR9pJfUcRYkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اینفانتینو بعد گل خوردن آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98734" target="_blank">📅 03:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98733">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXAoXhSIoggCSFYxsG-T7yI9ckb7poBDEXuNyPXyHzXFmbnBo5lP_KIoD5eOSZW6BqhCsZCCefbmV0klbKG3GeZIqvpWJue3_JU1_58PUSF1CPAilgYTHWE0vmZxPVOVb3BQZURgKoTDRU-TfFLDmol6lIM-Y8SgCE2YbCC9HuD9Td_yBOMXI-hhGKHJJjIpEJ7kQRBlYczBBEkK5mjOWy2pJG4wnADUG8BmebmaCByK35je203kiYOjVE7VmcZ6RwbYyXFuRy-6znPFPVsK_cSISzhje2bH0zEAImgtsXj0hrZyk0sPYitE6ylZfITXiFNcGOJr_rq0YpYmS3wRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای رونالدو کامنتای مرینو رو بعد بازی حسابی گاییدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98733" target="_blank">📅 03:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98732">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گللللللللللللل بلژیک
🔥
🔥</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98732" target="_blank">📅 03:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بریم برا بازی آمریکا - بلژیک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98731" target="_blank">📅 03:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDiMAboBWIrXZpTn76zTQltUvXmSDM5z4-TXat077flw_BZTQVyiYSYpEDKbFr2xZAz-_SCJTGzO6rwbJ5kAr12idKs43UkbCvA8eFCosmFTKdR2AzCASV3mrd2OqsUZm0Hu2zuZ-bXAvDXNrMszwGTg-oA4SLxf7sSbQarepnZo1HeAcUK7Vc1IUnXccfPTdI_kCT0kzML4zm-xjUloxZsiVg-bZYrBQOR0Enyjqmz6hfohZTI_vedkh4UHwF5nKNN9vE3yXWC_Ry9ygDuPMLqheULQEM_ogalXUlyN5xClYbWwhbxnSltrWvd45LdMylmmg0Rlj2nw6m7ZFMxqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه عملکرد هالند و امباپه در تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98730" target="_blank">📅 03:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98729" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mANrtYm_nNXXz-LPpqonBs5-GfpcGKX57nFsXnoHbwIiKF2snsLlP1ypYykKOiuKiFn381mEL0jJ7J22vBD01fLCyGypKqlSTD8sw50T5AZwzz4erXKGRIAJCtl2eFqmynqkV4d-IQM0Mc0j_IvXpGSUh4icyd5w0nRH2EHd8YgghaFkzkW3pcK1W2ttcshaB02Tw9j9QehEpK8Ncqpq5jl5GcrUQ5i2BJbRiEqfRnc5eN6Pvy-S3cyRy41TztCgrTohg8bn8Caz97ndcEteWtNNNSJATdRkHuehkzx_8JxYzi2lDX2aZ9KPslfDORb5rZm2JvfGDp0eTgbkmprIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98727" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های اسپید بعد حذف پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98726" target="_blank">📅 02:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98724">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuIOTmTgbIW65pfgADkF-jLohcpVo55bmc4bBtCIeQkj630krXd6H9C4RHtMcq4OSNW0YXLttuAuo_HEZs290KzVL73IfqiSV3ggzEO6OKK9haxlBydhVqYn9GlKH0Xpx36eCO0ZAzRiMkVyQY9IWsv10YVZB2wCgScH03gqk-Rfvb5IT5p3vDc098MULSa853PfYnp_AQUtUW_Mlshk7K69V430Ydl-nCT-6tARyumuaMGauK6KY1jTRcxNbtS9Fu7m7JSkqZlIopC0_8f2kyl97M_6ZsVZlYB8QCGOZBj84kBfW4OpqV3PdG1dxmCNocVXkn78JZbnPxd52qXyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn5bXCM2HLxteAfILY9fIRqe7nl37FoZYlY_uNBhKS6T_wzPh-HPaNu2Zo_rJOHn8ka5H7yoPL6YE1w0xmFukIlalDlnTZdatmlfAk9EgviWeNoTjBfeh9Mn9K8I6G5dlaZevJ-MQ1e8Zd1rJvkSi84WB9nJeCsyfSxCIlB_mU4SP5qWbjrtTVnPZKK5DMlz0_FoCz9MRU__KAAN4zO7gHCjt0JJ7kZbe9D_R6jQE7HJ5GYjDN44bMgcAgiS36YUA6UjJkEJSvIeaGIHaioU5LB6pf5J_VL64D9ZFQv126tVEIEykUaNcQJqK5sA71cbuZwlAmuMUUPzfiDGBrn7bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">-
First dance.
🫣
- Last dance.
🤕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98724" target="_blank">📅 02:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98723">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
رونالدو: از فردا در آغوش جورجینا خواهم بود و با فرزندانمان تعطیلات را با لذت و آرامش پیگیری خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98723" target="_blank">📅 02:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98722">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔥
👀
#فوووووری از جورجینا بعد از بازی:   برای امشب و تعطیلات تابستانی برنامه ویژه‌ای برای ریکاوری ذهنی و جسمی همسرم کریستیانو دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98722" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98721">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98721" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98718">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoG1XxNRATTLPPEqz3ZcULpK1eJR24v9t_Atb-PS-e5_kXR2xRY1wkYN-p6FouaEtl473dFQ-KT8IFc5iMf-YD7Rdibxjl0ZdMNYCISRIpGPk_LMdinnhDhf5zJVJdIF0bF9N59MyjUE88sIpmLjnvRQiXNsEOcpSI4JqA790KMHI7cQ1WMi19_j1JwyzO2R8wj-CLpwVOlFhgeFm8Q9XhByyjQ31T6gHbQ6-jOE0hqUsObGgVEszJykFqbZBe8iDDk0zUvFTAIIT2gV64mgOVTMpBaM-VFV9sTZnJI9XCJVvaa0YVP3w2zLb2tP4P0zvN_De_uS3kcubPWo6ILNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇧🇪
ترکیب تیم‌های بلژیک و آمریکا با حضور ثابت بالوگون بازیکن جنجالی آمریکایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98718" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98717">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98717" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98716">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98716" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98715">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgEI8hBkJOinUw3GK30zzAb6csi8NWTK3kVKJILZa-BzSvU3KNDIZyu8zkEQnruset927LL8p-1zch8FAHrN1oYJ9OCscfPUQneyrjE3HlGYqVmTTUevTGp_lLbFZg33N1awB3MCDYgqTPscs55vLdawjCWevim0kGh581b1pjjT8mdfxBpY-BUgBfQCD0a5EK1YaWzGnA1cXkZbClCxLXYmyMA-wKPfNbg5Y2VYmivI7t0iYhB6gdLaXOIN7HmpUoCM2-sXxBlSuJ-sVg10xIXd7WVmQmhYd5oEiB2lFjpNRFOZMbCAMue8eH-sJD2NlhjHovSjCOkka-KkQAyOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:
‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."
"زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی من با تیم ملی در سال 2016، با قهرمانی در یورو بود. برای من، این مساوی جام جهانی بود."
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98715" target="_blank">📅 01:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98714">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1tsTqAW0Hncl2p9ohYF-OGPRxOPqZEK2VQ2kWC6e6DhliZZ3dFbJemXz0cWyIxNA34t5JxwXrwPkmiQpxdz31fPczxYaH2eoWxzCkY90Ef9o2rjRtpRPr7AdH40On4TerR9fytQWvsCZpU0Ztt9Q37YHILbQmEJhv0C9fQM3nYmulzpcsK3Zzho61igLkPnmj3Nt6jnS7MGved3cWa4K9SqrSPRStE_myO3p0OdArMOm2BupoAtRP76O1n9qlSaa5-Lh23ZhtsN2CeZCPdFKwF8QCr5uXBDVKuXVG3iF4zMyI0XpmOlqAAlcba57NxE8QpWONFMD99-RMgvM2x6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خورخه ژسوس گزینه اصلی جانشینی روبرتو مارتینز در تیم ملی پرتغال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98714" target="_blank">📅 01:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98713">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhz1-QMAS4YilNnn51xvHdETJT4_GKxpFJc7KsCSvffnFVsNkL95m8Oc3_pTI3iTXYbUkaraQbiKT4x_DO5aKc_ab8lRdra6jWQRqbssxm1b2UFnbA6pW_5erAvVvzrbR28h9jo_RLS_FYyGxFb-p6seTKhH1W4AP7nyYreXTSEAFSRaWerM7CsYjKLU60gg2cUAIzKeaNruiuYA3la8SR9pPw5ksW5h3quWp0pbxQwU5dEcMlgwnRYRRhKXeUWKYGN7jCzHSKq-StWEiGpaO1K7dlRo5cUn18AUsONX9Vq37VMckZZxd8DHwN8DUPKFjDrLK8sP8gsqB0f2Se-rOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
کسشر و خیانت‌کار اگه قاب بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98713" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98712">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOmWgwO3U2FvOu9BiRVtEbufMmzXdKE9IqSP40qm3eOYDV61p6pOb7iUKBiyoM9VTHyfFNSPQoMIooMph_pV0LZpY8Mqj7zG2xcXuiqzVNNGWh-v2DXrECJA-t1SLe-i8SeVXifsQuX5Z6kXADnb403XkiWw2_Tw4NrnNBoM4aDhHrCwsVe9-hoXZcB5puLCUkYciwWhgv5nFxC6mzUE4c_OCoU8Lc8NvhrXUAVHYuwdsig6jCi_hnfu-F5qvd-8UnlpqKPStnQ5Kgw1F8Y81Bl_wWx0itUJAxrC2z1J0yStgio1aKEZPKmbO9RBC4V3c155GZ-ZWO5AGWJDdllkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🙂
ژست لامین‌یامال در رختکن اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98712" target="_blank">📅 01:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98711">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmIo-10Dw-vksksFuyaoowN_f1SXQcnJsgFK49OLrwnfVUUdAZhTexkCTjnjytE2J7_3tb0l7_RlB7gbyGVnPxWimdVz6SDqOsrnu4Fhwr5EoeB1KhB6cp_6lEj-a5fa4BgxkChTps0WMybb2flE8W4Zg1c6j2QaO13xHxVQcG0PfELFEW8TEmJh-BQVyoMJnvZJkeikFBZrVaUCl-C9-vrC1oLy2rX82KTfLKNiKzIq5tYfML5mmdYtd0TewC2EBT5QFjv1GtT9Qt4HMsfXrvDGwZICxCckoMa-wrI5wv5-Kl_P-CaCyD_yK5dSZ56smFzQvQ-ax0gcvHHgGVXvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی؛ حریف اسپانیا تا ساعاتی دیگر مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98711" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98710">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejgppp6awqSCnew2O3XaZf-FZ3-1F1XkHYpMpOzEo7LV2nMilYNltTDw-P-TS22WHUO8MuGBvzHdRecTDOgNi4T0rz4ejAsQdNMnM_ZnrRhRzjwDuOQevSWBvpsUWy0WZtzxGbuzvrG68p1XX_zbXlMnh-PXeTO44cpiVt1bhLE72YDc80zDo3XDgIak4OcsWUyf706dGMQN4SR6BKEJHKAhP6vZOrJajfBk3M5GA5ho5KLNaQOLAslRR6eHg56PGDBlKFe-aVIdcuUVt1WiHdHTBJ05OwYsUpciaCBWpFs31Pkbnpid4EyDVcq50ICgDm3ZkxpQg8Z_tR-pW-znAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پرتغال قبل کریستیانو
🇵🇹
:
❌
در 3 دوره از 17 جام جهانی شرکت کرده است.
❌
در 3 دوره از 11 مسابقات یورو شرکت کرده است.
❌
0 قهرمانی.
📊
• پرتغال با کریستیانو
🇵🇹
:
✅
در 6 دوره از 6 جام جهانی شرکت کرده است.
✅
در 6 دوره از 6 مسابقات یورو شرکت کرده است.
✅
قهرمان یورو
🏆
.
✅
قهرمان لیگ ملت‌های اروپا
🏆
✅
قهرمان لیگ ملت‌های اروپا
🏆
— پرتغال بدون کریستیانو، هیچ چیز نیست
🐐
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98710" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98709" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxGp_kOm5zDUcWmjvETW474QzJtq6vKTPEAKInEAZty-N5V7pQK4ptou8AIBfjsn5vPO3ejBHwbHwMTAEI7GUXP8HVRs19lDDWlBwOm7Guh0QCeSZ9QkH4n9ovy2N9lV1yUqFZTVzF-LCBUQ_6o3y9ZL6fYX8o1d5aVaHD42LXLa9IAjof0UUeAZefAEVQd8mEjj5pFUYDMFdbZkpnL6bmsPMH0xjsu7IPIGr9SaM32D5cteMfhY76e0mwmJOwYFh0Hkv1RYI281yLlZRRoBD0OMV65Tq6eZTQt8znnpYhPG8i6-IFqW0H0Dy7MKMVdGo0tyA3mNOHMkghM-s_9rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98708" target="_blank">📅 01:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98707">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxT85dFW5gi6UQwAeKIeiBgsAUeBPvZ48IKe7kKyL6UcseQ4IzVmWjZnpUXEIHoKH5NV5uCEoNPaWT02qEdcCONZLZSsEWFlBDAtNQK7YJnU5pU0zqkNaxpYH-Bol6OF-alA2PiO7q5hBhhfaopIIsOA9WR87onKmouRh_mRH00xxqCsfHE1sUylOFSYEYwx5JmgFpvyDpKd5TjpCunz6r3ehPYfxtJzE8roTtfrsWyMqgEx5fb0ps6wKRvvO6uSnpYOv7saAFw_i189I-XCT7_e-gofrTwru0j4YL1AuOQa4v29TQ_3ehVXqte-F1Pa1a-IoI2xw1aeZnc0UTc43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بیانیه فرانس‌فوتبال برای رونالدو: - از شما برای خاطرات بی‌نهایتی که به ما دادید، سپاسگزاریم. میراث شما و پنج جایزه توپ طلایی‌تان، ابدی هستند.
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98707" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UePB9sx1-VgCjbYX0QvSvUMpITpRpHhU1hhhfZCAEdk5Ctamh2dxKp5a_0QIYoGIXy7j20Q2OzN14EAijqGetpBtwZltQXIFUP6Ch_V713qPOud5X89C8vVccPrA3-CNX_CyZXC8Dyt0DTdhK4EwlzHspk98I81XVGnHE0zgZheqR-QYZqX2qn3VExSPCy_WoAtbrKIDrOQPE7ukQFB6XyyJGEfHIe3iYWN6Cb6hpvbk1GWFAhS6_OOBCjWE0x1sy6ZdA9gq594BJkECpc4dgKPkgQ2K58Vdkjckh1R0AJsnpn4PB2WdtVe5VX_EezvGKfZhgE5IBWbewnZMpFN3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مارتینز از تیم ملی پرتغال جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98706" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153aac5990.mp4?token=lEeUeKPT3EluBk0dl-Y-ac8aZvxGRqKQHxRzPhggcmR7A3UlMUsi5Zz3HMbtHo8YAP1sLy0UXLm80RKFCwAzOBWi34RMiD1LGeCV3GrHmOJWhZTi87LPonrwPyKq_-iiLcP84xcMfELDSW32JELC1jxSnLoV4R4g8ikL4Vgz5UCMzBnApmsdqEmlQ-KxOzCufUCdEen7gmK3ygswkuzO26pCzJskK-SCun3Aj_hB_aRWrg0dFmFlRZcKIvY3MvCTYLCN29EseIGb4sOf9nIuSZWxSVDuJHqwM3NVjw67C9b4iaey7c4R5iQG6h7JDh6rb1QquzKKl5Q4rCeBrNt5Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153aac5990.mp4?token=lEeUeKPT3EluBk0dl-Y-ac8aZvxGRqKQHxRzPhggcmR7A3UlMUsi5Zz3HMbtHo8YAP1sLy0UXLm80RKFCwAzOBWi34RMiD1LGeCV3GrHmOJWhZTi87LPonrwPyKq_-iiLcP84xcMfELDSW32JELC1jxSnLoV4R4g8ikL4Vgz5UCMzBnApmsdqEmlQ-KxOzCufUCdEen7gmK3ygswkuzO26pCzJskK-SCun3Aj_hB_aRWrg0dFmFlRZcKIvY3MvCTYLCN29EseIGb4sOf9nIuSZWxSVDuJHqwM3NVjw67C9b4iaey7c4R5iQG6h7JDh6rb1QquzKKl5Q4rCeBrNt5Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
💔
💔
▶️
عادل فردوسی‌پور کاری کرد که امشب هر فوتبال دوستی بابت رونالدو اشک بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98705" target="_blank">📅 01:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=mCM2KwaPxYo88mqAgWdYVf59XK9mZraVbvIoT1ozCfTyTZO2oEIHYjkSnj2LFzr8JYTxu1LumkCOz_9yLhWhvj_aHtslO8_HU5w8s2MGNpjRs1h8lIe_0kidT68Ax2b1dait6D-4BOguey8Dq1jDinGZCGaCwlbZDqbMqY7CiVawi8pibgnhl57Tr016IC9LT7-jP6dBlu1U9sA0n_tfc5L_LYQwS4BCG7eOqobjhtFSpmLrcx1g966xGl1O91X5Yb6Ovu7bHUB86LXBCS1lzsdsWy0tzKm_4TINgv7YkvX0Uw7qy4Uz79X5Cup57zxag-RyF9noB7eP8NV4mK2A4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=mCM2KwaPxYo88mqAgWdYVf59XK9mZraVbvIoT1ozCfTyTZO2oEIHYjkSnj2LFzr8JYTxu1LumkCOz_9yLhWhvj_aHtslO8_HU5w8s2MGNpjRs1h8lIe_0kidT68Ax2b1dait6D-4BOguey8Dq1jDinGZCGaCwlbZDqbMqY7CiVawi8pibgnhl57Tr016IC9LT7-jP6dBlu1U9sA0n_tfc5L_LYQwS4BCG7eOqobjhtFSpmLrcx1g966xGl1O91X5Yb6Ovu7bHUB86LXBCS1lzsdsWy0tzKm_4TINgv7YkvX0Uw7qy4Uz79X5Cup57zxag-RyF9noB7eP8NV4mK2A4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حرف‌های رونالدو قبل بازی: شاید این آخرین جام جهانی‌ام باشد، اما امیدوارم این‌طور نشود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98704" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98703">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP_horxXCm0KiecFA2XhEAgxJMdf0SKITJazx8452uLgOUZ7X-ZUVK_dntUewcxnc9MDobddpUmjn8C7ozKyYPw6ricm0gqwoQIU63Walg5IItJ5qkgmtJfFfmHQodBjmbaQtCjzOb6fx8Q_6_0eUem-r6TJhF31HWCsgf0z1Fe1NI-mVH19iTqatf-CIorOJjM6Fek8H-AqwXmiiXLIhQ-LLtbiTPbgGbNx6eSEskk8CUs7vkYNrJYZp8OeREI_DFHPhIf2Mag1wDLZ6LRXLRYUiBq3M6SCwrIIzCn1cLSlhAM6Au9dV1Bijv1tPbU_xnWvJE1qJxjS0l8rUau-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل میکل مرینو به پرتغال ، اولین گل اسپانیا در مرحله یک هشتم نهایی جام جهانی پس از گل داوید ویا به پرتغال در سال 2010 است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98703" target="_blank">📅 01:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXke7RINXvofivbJm2MfHMvKyJThLelxHvmgr6Gyf2SsBWmR9CK9Hke8P_sXaiUPyYFQAVIn0ptoNFLwMEwY4IWhOmcHQB-76ZNVMyvtGaUwsXMth_BhTXIUidcQGGfAIg2JfwrfYqDMWBBLEiVuleb0EiFBgjou9p0wOOvG3_SzdxEuK9SLXaM2lyX1_3nTVLT8rFfUl5xzCh11EUJeHuoaIal6DcoR7uasTK0yKxk9rxsfQCuOISkEFcKjvGCRLONWnHLxUQOY572DAK7QPw1yvKDq2-Cgw5g7RJeJgdeRCMo4DiFI9GRe3swBwYKctXkEN8_itzyeJdhuC_ajeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
♥️
کاتیا آویرو (خواهر کریستیانو):
سر بلند بدار، برادرم.
تاج تو هرگز نخواهد افتاد.
تو یک غول هستی، تو سرنوشت‌مند و انتخاب شده‌ای.
تو فوق‌العاده هستی.
از تو برای همه چیز سپاسگزارم.
از تو برای خیلی چیزها سپاسگزارم.
از تو برای رویاها سپاسگزارم.
از تو برای شادی‌ها سپاسگزارم.
از تو میلیون‌ها بار سپاسگزارم.
تا ابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98702" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QVrb4utUuoJi-yg5PksgmumG9izerz9Hr2H45YKgpOHuYfl8mXoW4icRDlJEGiCYVLGt3ZTgxvpoSzVtClPjgGYF1pAyJlz0To3sS9o1JgRNzOJgMo3QPfNcx9SyZRsrl2wtLd6vGnNJIDM5jYwtEqeWqfcXRfSMF7XvU1chUUhOBaWta_uCtUMWyKG-w1dd6PyncE-smMHasibY1wiEerqr0pUA5Lx92U7MEiE-I6gpGW_p3HLHiQoBMa-Pwy5NriqO7XFzDkDdm_hvbq5wSj6N8JPnoUKUNKllTaRXUqq6zQ6AfWpVvBnWOaPsxf-zP4TWav3GGLevAKZANdCdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج بازی پنج کلین‌شیت
✅
خانم ها و آقایان معرفی میکنم بهترین مدافع فعلی جهان پا پا پائو کوبارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98701" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98700">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-LbhvZDciNgsAToff6jQojYabO_S7rwgzMj8E8RKymO-wh49-r_wEMoHdINcbHY2d-GhKbK4kyO5rXKuYunL18_XuQYiTsemU-VJ1xosjmFGHQHzH-QPmnU7tULZVZIKwgBFafN1ZtilgbPxdb7Lbaq-sDeHxjbQ9HjdWxs3EDCmiXKpdjRTScYDB4llXtVTv_cQ56yrWaoxJhONBmsX4-HQrLepigaomGL5PMssX_Cc6FD5lZ0hG8E2thFZo08I75BKE9IiIwTPCeC3o4vW7PUfve3ZYhIQYkScgDw8Sx6g0G3OokD7mKec9rbWXqixJSCzLQPfKdkhUa-A5MDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙️
رودری [
🇪🇸
] :
"از برناردو سیلوا بابت تمسخر کردنش به خاطر از دست دادن فرصت در آخر بازی، عذرخواهی می‌کنم. اشتباه من بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98700" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98699">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3q78jOtK05kvV6hw-QHyRFkgPMmgFbNlLpAIfRSiKDtQjOuKPIpHxCuebaebTbn9v8M7U_5EUlJwFvcwOx9vbmmq3TkX-L2yQpcwrUOHbykw7s0Z_1K_oViaIIptieK9WP7BvBnC0sGKSzUUwpA5MMXYxbOrbz1eIUTJV64gcEfri44PlnN1XObQS8GymTnbgiURjeE8Hv-nyyti9rdYR9UB2uyzcA6agMFxBzirn3xc8xFtpJAaDWnRVidTzzbcj4cVfdxfoDMcq8Ufr-tzCdBTPBNUFTW-IMGOiR2VoDV6_H8-sVsmdCNNj1zohBbsnIvnvHbbK5PrAUZVktEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
و تنها یک‌اسطوره همچنان باقی‌مانده؛ آیا تاریخ را رقم خواهد زد؟ برای گرفتن پاسخ کمتر از ۲۴ ساعت صبوری میکنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98699" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98698">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این جام هم مثل جام جهانی ۲۰۲۲ به کام بارسایی هاست
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98698" target="_blank">📅 01:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98697">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98697" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98696">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DehmeVW2dCprC_UoNKmwfI5MzgJOoQA9bJsJaZ0f9v_ZcIcTjUvKxK9qHRspnTwkieXCIxJYVMhCGoyWdVi62zwZ5WlejNCWvZkDPM3Wv1jzunowU5DmnMw8Uuiqko3f6EkyhVs-HL5-NXwf42oA4valgOtPcHveuSX-EZhuqXNdsyiOn_qC7oPpKLGVrKpyC3IQBMwTglIRoSi69j5T_4MvQjUHCqxSMSdEMwohWmUFXRY_2mkKNzzvsdEkp3G0P4IouVySsbncVyTx91PMcZ-RB7MeOM6TUOyKqD3yPU-mh_KflKPM_JINW_bh2pCsYYOwU1wCqy195-2BqfrMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
سجده شکر مدافع پرتغالی‌ها پس از حذف شدن از مسابقات جام‌جهانی
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98696" target="_blank">📅 01:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuJOPfT8wL4KKcPws2gWSt8C56xRmFrBLyDLAJ9peA0eQr3zDgBijCAb6_OGC9V40xhS7TMAaFbw2IPg8gM0jNK-yfZtaI855kxO-D23F6wS6uT7YFhIkS4WI09hnhm0tBGiOkhtcjEGSidTQA6Kji7eb0-yRge6D7HyNc3GymHEkm5QEoXahVmgrIUyWUjZsrHlJZdkowGFJRrC6KhvqK_alPpxqwbLdd6mb-N58hOvTWBFMbjzaQbfZZT9BiHdn1_Yh9rmc_wDRW6n0lVRrESxTAI3MvJgGmHuHVsebubSTYdp4JGQrbrOy-L9tyr9e7hpHZgGqtxizMTeqOHoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
تمسخر پرتغالی‌ها توسط مرینو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98695" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QChcG5baO44W1O1SE3k7tvePlEjsyApsVcfYfDEoiq4xX7SSF87abnUAVRnQndXQ4lyW1UxBuL9fiK49yR05pwPpDPd0qK-TsfMtj_BNnV6mNdYMqS8we_pawCUnS9IRXi2FhDxWo04IAv5EsYHaYfwqKmEM-ohXGe-2tQQN7qfYwPOp_PlOOijrTdM0s6SJK8anKkku_i2WlEmGGUxvNsq_x4RptMDgLl17CNo79e35kEm5gBa5SsGEcgBu6KEy6fnytSgJyn6UVibmYF0ZFyFMv79_1vWFffsQJCkKEBwbCV97GnjrHuLAbgDQo4N3IyTNTrHKNuNigSX11MYa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
تیم ملی اسپانیا، اولین تیمی در تاریخ جام جهانی است که ۶ بازی متوالی را بدون گل خورده به پایان رسانده است:
🇲🇦
مقابل مراکش.
🇨🇻
مقابل کیپ ورد.
🇸🇦
مقابل عربستان سعودی.
🇵🇾
مقابل اروگوئه.
🇦🇹
مقابل اتریش.
🇵🇹
مقابل پرتغال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98694" target="_blank">📅 00:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=W8G5bofXE6Vv1fS4UDDbOnck3qiRbw5HoCfMK3rgoay1K8vmH9mJtit3qz_yGDQL2tk4CY3jt4QAk4zbq9qgpCyEkE1Wvw0me9nkAdVEw382wLEHDWqDsywrn56PL0DnqXwGDp2QLHMUrKfDHfznyAaWv_RuypGuv2eTPT3-Rr_gauu63sGzl_NAQKcEtOOUCvPmFp8LxffpfpF0qMZSVmz8JDQinEFPYc4MFlDVTqddTWIYB2yhq-1r-Sm5Wpu-vEzBa0RFBRoXIxAROAmzCuyNwD7SBEDlayiEVJ_AZ6zslvrmx3YFuk4yOOwbRqXqmylMcr-JeEoSjgMVK0OUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=W8G5bofXE6Vv1fS4UDDbOnck3qiRbw5HoCfMK3rgoay1K8vmH9mJtit3qz_yGDQL2tk4CY3jt4QAk4zbq9qgpCyEkE1Wvw0me9nkAdVEw382wLEHDWqDsywrn56PL0DnqXwGDp2QLHMUrKfDHfznyAaWv_RuypGuv2eTPT3-Rr_gauu63sGzl_NAQKcEtOOUCvPmFp8LxffpfpF0qMZSVmz8JDQinEFPYc4MFlDVTqddTWIYB2yhq-1r-Sm5Wpu-vEzBa0RFBRoXIxAROAmzCuyNwD7SBEDlayiEVJ_AZ6zslvrmx3YFuk4yOOwbRqXqmylMcr-JeEoSjgMVK0OUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال
؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/98693" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMJyUw8WvaUuQiNvIW3em80duOPOU028847ydNf3idJe0Ryn_5NXriyn6S5izmvTx72Xt-9OlVRIDz-wtpnKVs6VHyFDUAclQfe0gbveaKZSiTHH6XFENXhkP9f3_ThL0_jNuHfgKdDcdZ2YLDskXt9hRs_E3gu-25AUGobRTjA3BRy7A8vG_F3eTWg58q0bXdxmWE5FdCygZG-sjjM1Enz9ApNobtQWDBJFfnFJPKS1bkuRfhKo8qq_Uci-elQLcSMLuhBoozJM1qVw4poLNSZIamP8Ujoepi12gL400bFvBjCByKzsGJWE1jCFTnE7EJFv2k0JhQ21Ft7GcCfHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید هم یه گوشه کز کرده و فقط گریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98692" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6ZKNtq76IV7Jq91JYyqxam5n8fokfitHSy1wCMImcv6SSsuPaG45cowsadTr3qEbj-6J6Mbu9KZCm-d9Z7OpB5FJ08I4Fgaj8fGuYanx0uCI4Lyh8uA7GJ6Y2hvJrf3h0BSfvEmApYf6jK38csK6mmhv4dfji5qc-8qo0bcTPTlZqY6EAnKASH8F68hqVbY3SIGrZyJ0CyVUcEqs-lLQaOquNW2ODRo44WjJaWkunL84z3Kw7AYjhYC67h7rMDZ-t7hHpzNdbT_EtMq-t8HsKZhNjkE3YcP14LLxPyffVzfKfFLYOGa7urL-OnjSq944F2cKl64ITT4Bx5gyF1o3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
📊
🇵🇹
مسیر اسطوره، کریستیانو رونالدو در تاریخ جام‌های جهانی:
‏•
2006: حذف از نیمه‌نهایی.
❌
‏• 2010: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2014: حذف از مرحله گروهی.
❌
‏• 2018: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2022: حذف از مرحله یک‌چهارم نهایی.
❌
‏• 2026: حذف از مرحله یک‌هشتم نهایی.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98691" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
🇵🇹
روبرتو مارتینز سرمربی کسخل پرتغال: این بهترین بازی تیمم در جام‌جهانی بود و اگر بدشانس نبودیم به راحتی برنده می‌شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98690" target="_blank">📅 00:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98689" target="_blank">📅 00:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98688">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=ZeqEffFpn5hQzKKfRlIrHnooGYdLbw5Z5dLF6b_3shctk0GonIrebR4tPgRKFf8-KEMKzv4UMtfAIYNcb3P2lJJyC0htBbTTN44mPH21gcJf07vWm4GAnj_o_SkMkAKvnsPYgAq-vJfvR3zeIKSg4dhL0KQz4G2odg1gVPR05uWROYVlgliUfJW4yhtKhzL5QP213MAmpUf9j_AUG3FtTG-0Eo1tJiutHnoCifhxWxzDsG3qBW984HbgeQZb8nLbvvW-632UIVcmvryi7aJFdePfzyLicVNF4pnCSegsExZUYVBu-I19TXTyPOGot_aZNr6YZ-1lwKwDoLzw9HJmKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=ZeqEffFpn5hQzKKfRlIrHnooGYdLbw5Z5dLF6b_3shctk0GonIrebR4tPgRKFf8-KEMKzv4UMtfAIYNcb3P2lJJyC0htBbTTN44mPH21gcJf07vWm4GAnj_o_SkMkAKvnsPYgAq-vJfvR3zeIKSg4dhL0KQz4G2odg1gVPR05uWROYVlgliUfJW4yhtKhzL5QP213MAmpUf9j_AUG3FtTG-0Eo1tJiutHnoCifhxWxzDsG3qBW984HbgeQZb8nLbvvW-632UIVcmvryi7aJFdePfzyLicVNF4pnCSegsExZUYVBu-I19TXTyPOGot_aZNr6YZ-1lwKwDoLzw9HJmKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/98688" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98687">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW_OgFUN3N-x6B6SzGd09roKC9ZXroNsGrPf5ZmlwJell-M2EGV0H4onOpFSiFwLWFAeY2QAI--1JUktyGeoou8wLeG2qeKAJaOUK7-Z-q2afVkBSgsLePgM6ZNuR2095Bu3b_YpvcgRvf7OE_aIpOzZqx_d6JqY9ZniSUK76WethLcdIXt3tVWcshMpuBGb2ZxU3GpUPlJEXZxkm98tnJ9buOdT1ePGLihRlQ-E9RufGigQoQPWddbm7X3FgQj1PLjG8ofEhV3V3_Wln_Bk2L6mdWvhs7Hb-7S9U7deIYp0VwQPLMIelgu1sQdfQ0wQ984Nz2NgeXfeh1IvgKnmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
خلاصه جام‌جهانی ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98687" target="_blank">📅 00:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98686">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0Yjjs_pKpejDjKE5sm0Cq-t6lL-VoPZ4Z8_l9p6-uS3je6aX001NpWMJGGT-kc59H6K0_COLRiDZdJWCbIo37qH7NkG2MxzCHtr-lXlOhSU8f2xnHkgHLoyfPQl7y24vZsjKy0owMQAuyiPiLzuyH3uGp9b7jFx8zbnZi1J5vBz5h6v22_IMiLlrU-U0xCE3SSuzI_c5SAJHU4XFn7sOPwe0bpiQUhD5oI94YikpmGf1vyH7Ssa1y0VJeQQT9cfVXqUX78cn3fIm8_0MK815Hp6EkUkWyAmNbiz7drSrfE1JgjHaqeg3sTVIvUzHM3HchtpG54u9gglzY1R4q93iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
👑
👑
🔥
🔥
🔥
۱۸ سالگی و اولین حضور در ¼نهایی جام‌جهانی در اولین تجربه جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98686" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98685">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98685" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98684">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzYs1BGbNEN8FZifMyqSoZT6DOp2YL-otWnOOo0nSyvz81VtDkv-Yvt0gtmwByEcbt_09AnEDNf6TxilOVJDprk2r9VgNj2CkwRHB9d4nUZOgOaW3tc0yB_GLFQl9AAFw_SDwcafIfIFUHsFhnVTJFwUFsWdbnlablpL5kjjhP5cZnYd57t7zM5Xh7SuAPQMpw1SmXosaHlkI4NPD8YnixFmXp2QihzkYJuxAGVoB5HFrW4hK7I85f7G4QN7NEzEEDQmW0WdGflZRQqPfgLrdHRvpn1aqJx7Q78P1a6NfClEEo1Pso8ycd-oajCTAtn5TPuUHXtbJf5OfZqdw0TbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/98684" target="_blank">📅 00:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98683">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw8q2QVxmPnvoqxBZdLRJBPTtulJp-MWQn2qAiZ9S_iI4aO8a7wiTC0qwYnhkLR2BpSKf0C53Wg81i-OsMog25G-SK8XaJqvdqbk1ykOSfHn44fhJvT6QlD8tBtlxsUA-0tlCg44kOzeYzs9Q7cjRyld3WHsb2AryYaTQt1vKv3vQ0ZabSKD74XOpXwXt2u1NKZOKOTGrVdRHLS2A3iTUyMM5KGv3Lg_nA6Y25-URZF0liTgEuBJ1aUcFEXm-kUSMM8vNc5BgDQV91GG7OtKYRXabvhpTmEXrp4I0dbrkptORPubkr3w9HOp8y3nbfi0Squ8WlBseLYV3TIRr1lufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
💔
💔
💔
بدرود کریس؛ تاریخ فوتبال پرتغال بعدها حسرت داشتن چنین بازیکنی رو خواهد خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98683" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98682">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98682" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98681">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vyS4zr2UJDfVzPVDXN1vFywzpz4vMmOe_kRE0R-DXdii5jFxKw8fjpGUNmkCHDTVN3r52BmArZvWrpnN_kudG_Y_2C14fBnYKivap_gHlfLkKThn-2BVZeqXikzsKrguek-IeJEboWxtJG99o-bRS1c7I5jNET3rjtLpd4Lr5ZbxqrUz4_D6amRJM_94kc_2giLEnE8yYXwzqoQ2wIfpdXLtntJNcdtYdS4Z5K8OpBVpieTU5kC9v9qobQU86LxF9d3eF-mwNs-pfMIMrfn1WapLtZXnt5iaVagKUqCwpmB-Lveyw5hq6SdrN3uBxT7BvlQ3ELl9Qh6TdMtDmlMQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98681" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98680">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hophld3SfcK8sdfDsn9TlC-vd9S62gHkFZBE0x7rJzqAz55IhZqjrD6E7Eyui_ggqPJbagZ2dqj2_yuo3pBZyew7DKu4B1DyV-edVnc34xZNFSznsw_tiE_i2UkAnKiVxMAfqza546qNFNxt_Q0GCoF-TrHlUJu0UizXpztrJqqDuK5NPAW5fIQ9nHcxNCPPYKAV0ZU2Azx81yWLCaGisxOYQLAppaqfXVpszKXezK_90gxpsnjge5jS_34iBBQImmVQ4MQd5FkAHQS89JJ7Rc4qWvaUQSHrB9Q2-X_u4IxIbgVvahbdcyZ1Q_Wisi34Jl9z3UOo8y4OGQwbKmBHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و فوتبالی که همینقدر میتونه بی رحم باشه.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98680" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98679">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH2iugUw1rR77kqp37ue5NMi4_ME7FDQN8lncBEgGDxxJ1YE2kepLxDybE8sZJzjVwtoooCTYi11PRNb9RyS6w8lxma0XNFjb5BT3OiI8eEmTkn0CuW_Wd7Jc4pDswkOWLyulMF-8DGP2n7mikEMJVjRp72PZHS35Kif08WM9Hs7sjtIWQWeahMa0Uk53kZ0-9e-RnPXbm9MRc43aCzE1nG7FjkC9eAV3ZZeCbTn_sZTorBXfyzcOiresORECE5iNtE6rnljfemkSyxTc5_yZvrDLB1OLxs5os7BakhjuGrqHNIndwcmBp485fexy_YF8C99RTiaLYpKgv4icUasAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
😔
اشک های رونالدو بعد از حذف پرتغال در مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98679" target="_blank">📅 00:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98678">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b45fc1c41.mp4?token=DUXnWjQbz1qx4tkCSE_kWuG01XxMTAEKpuDBWiUuel2wLM_Lvw2pxoVNbBmNKf3zUrvyRnNh3G9XAU6LJx1yZxaxARpkJq6eLP522I5dK1tWCWqo7wTI5W_DOZezMnqb-TeZvyng-gVOA3OiNcVhSbYi8PSUq-2WD0XM4tiEi-qVc3ELJ9kNxmTX5lDQUlvVRfXA3IWEGvYq5vvRHcDaHYPhxPRCkjIq7qMkX21SzzAJAeCdmAvQZnNsqOOMFN2MiSkLwKH267K8ZHm4K97nvwrofv-tD1hbnNW_zV1orllPnxDPyvsl8HdMZ3hVZpqW0yfMIREOrv2AdSYg-9hTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b45fc1c41.mp4?token=DUXnWjQbz1qx4tkCSE_kWuG01XxMTAEKpuDBWiUuel2wLM_Lvw2pxoVNbBmNKf3zUrvyRnNh3G9XAU6LJx1yZxaxARpkJq6eLP522I5dK1tWCWqo7wTI5W_DOZezMnqb-TeZvyng-gVOA3OiNcVhSbYi8PSUq-2WD0XM4tiEi-qVc3ELJ9kNxmTX5lDQUlvVRfXA3IWEGvYq5vvRHcDaHYPhxPRCkjIq7qMkX21SzzAJAeCdmAvQZnNsqOOMFN2MiSkLwKH267K8ZHm4K97nvwrofv-tD1hbnNW_zV1orllPnxDPyvsl8HdMZ3hVZpqW0yfMIREOrv2AdSYg-9hTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😔
اشک های رونالدو بعد از حذف پرتغال در مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98678" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCnr0pvU3gDahBm0wFWnnvSyI0e5B3aHBfMJn8noQn510hZS0pqwVYwK77jtHts_gBV6syOndagrkx4mn_0m_JHSxn1dAUiQBaGpECcVgeF_o_wSJg7ec5HmC-rPii7aKIgHzHwyQ2jmHO8OqiV2BJ7nH_FOvP6vNA7WFHzUNhrv9egvgHwHwfONR--fCxjevBYqEC7GIIzyc9QJwTVo0F0_K745m7jUuP35DEf8j5gVX8kZ5l_DT62Hwxeh5dKrPiDkcXJ21tvW23p-M2jFOp9ns4E29WLDmfQhxRJV2ugEfRlXIbnAAXg2vNJszfP-DEY9TtB_PTCUeUmAiCmeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
دوتا کچل اما تفاوت زمین تا آسمون؛ یکی با تعویض بازیکناش ورقو برگردوند اون یکی با تاکتیک کیری باعث شد ۹۰ دقیقه رونالدو تو زمین راه بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98677" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7ALfrN12OeADd0Ff8xGVAkHp2Y7oSVhnRhS-bB25r_qjxnUlH5ZtddsCTaMer4VpYMH2_7I_b7gDCKBYxgbX0qz_y7J18_3LcjPqM4D45CNYoh0EzQdJxtz0Sweewe0f63Kz72DotA3F5ycqcBQAPVZsRn8jErgTCaixEefg6KxBOcf5b8G8q3Y2bBbu21oYtKBpA8Td-1R5MJRzEV5nWjWWPhXJkABrZUTH6t1xsr4oy6_Rs8c7yodk5FVCzeDJrsQrGedZxBucKnpfpju4Aru6s1XkuP089zcZlk56e9nVZzxWttKqXmpCrWnfd_oEVNQlKd3O604kXvSoJVsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
رودری بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98676" target="_blank">📅 00:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRlLRcptSdfH9E-w5_awHDVbuKbepKdOaGcOPfIHaKGoMG7qkzLDCtW-5FMtmce0NylRZR68qsw_EpFcKJmdeoZ9QQY2B7thhdlBXZBmc75ukDlDI0SJJe4fZrbU_6DST7WSTRyku_IVpOckozyQSvcGrfRac0EmDpR_tVNOaeHLS9mKBO2OXh3Dz-q_nGUEnD55n1iJUtIcfm4YFfjODwFcs9l3bvCKH1cCzjckvEsCp6QY9nMPVgdcsGYhKagDL8zHqXPeEOS448gY3AX_wTN41sIm942BnxOHlpgabtN6Mm8vNNnR2IoXbt5j4MIRDhfr3fDI2a4lLxmy2CLSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GksO4voHtASBEcDP_FHG9rwUDKKbYB-KZCvkaiYeiYUcv8rDh94RT9QaSRyPt6cdMP9jOdXABAa5ZYVlxzBKDKv5Gt-futs8eU18r8Nmx-dLaiU42I-VyFZGoqhmNznMiy9KFDJiIKADM6LAJ-5SomHZsSR_TUCw8p91eDQc8iUdg_cUFwN6UbvrEfF1I0zFBsYq32FSn6cuFnV0D7Ch9A_9zXpKtbZmLqRAQ6f47lD0Mn93PlhB1p5jaXgEPxHpgA10r490v7kk7wfaZKLdygOcAuEbRzb6u8Li8XGxE2EClVIJh_0EVvSOVYnznx4pEqHmiGo6u9J3VHK2mQuwVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
❌
و رویای رسیدن به قهرمانی جام جهانی که برای همیشه به پایان رسید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98674" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYgqKUlhnlATMh2VHI0zgY1wrxG_DO35XLI2kh-aD8KJg6stdv9cM7P8TyMjRsdV8GJYJDKS2R0S5xBHnVOs06BHdD6MoLjKJTCfJIEpXyo5CHSo-JrZujLQ-mQvdH0wU4v5AXQ2ouD_8SQ1wT2xwS5i8tmWWtAwKynRO-GCZUqeYtC9d3Ta07OIvmXAP-hIgujpJoE5aTfQdQOsdBWFMp-cUSMUakjZF-xZS6FQ0uzoEC0H_9wcAZG4NhxUHotdbewlAxR1wjZgOPiOyZpySU5EIAYZQCJ4Kf2E-Zb9gAG9FqV6cqTpUi00CZqPqbMM1F-GmdtegIeq8gEtMoYfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آغوش لامین‌یامال و کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98673" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be6Ngw4x8sLqMGhe42cd7BK0lh0sDRJvdRRvUOGsE9LewO1d-ILwFEd4FZZ05c4_L6TsquktJafj1chWd3PuwZ7wTJL99u1_NGvJGxT4xNopHFlS-ETderL63b2nrInvg3Wicm_Trj9vJULAkxh1xJRROrCB2nTWg-IoHHfe2Su-uGDL_BoMxIHzvJcyqfJpQIAAFgpm8XAOiksfljqOqTevYJ1ypGCmbgxv6gKoBCZ9euwwTp_1_pmulU_OkIopmMa8_eANrcHS-jS_Ya5q4JEri2KdOOXKXxoIGEQSMbs7Z2Pdl-auO4lm9dxAym8YN7KjInA9nTawf49Os5YKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😔
🚨
🚨
🚨
🚨
پایان عصر یک اسطوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98672" target="_blank">📅 00:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6nGQ65Re2uTsG24OvPpeyDWqDmUbGmM9dpPfQoaOpkB6Ypk_GFs8bGeNmXlekcTJsmZeerWn9nx7uqcug-cQhG9Y5hTvR61g4dgtpjF5LXZN-SlEmwfJbE7MZp4VwOMij_mAGyRiBwDl9o6InhckB6OFPjOVj0un4cBPG7FjSNfDMOq94v3ET7ucbsh3NzPMelg-oYD8BT6vr9a2clHeGM3MWLAg0hXaitt6HYfo5KgqxgHbU4E6-t-MzKtJmkyWx-N35zt35y8nBOR2UR51pNi2A_r6uTn9mAVpBMIn5BK68SkgrdWwL0AZrJRMCtqEYx9ATFthx6Nx9GjTf7yKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پایان‌بازی؛ رویای قهرمانی جهان برای CR7 نابود شد! بازیکنان ذخیره اسپانیا شاهکار کردند! پرتغال و ستاره‌هایش با جام‌جهانی خداحافظی کردند!
🇵🇹
پرتغال
😏
-
😃
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98671" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98670" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کاستا جلو اومده</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98669" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فرصت آخر پرتغال</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98668" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۱ دقیقه تا اشک ریختن های تکراری رونالدو در جام جهانی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/98666" target="_blank">📅 00:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6_CW1nZ5Iy2kWYUmtL7XOEF6Tx8KS9fDTXnaj2FVaEUbpWuN45lQcZrXMuvn9o0oyaur_dorTAjqcVj_56PzZCCaJ2u3gj7vTFgUautxW-DyGseCOzsP7EwdmCyP_zFusk11rV-n2zsuHDY85CvbVMwHJmFfX_uQ4Hs6Nzz2-rWmbq6Hcn7ZXxy3Tne2CftVUQXQMFfPdIYNJz44oVe4WMXq_cc6zFZfrmlt9LWTGRF_F8YNRS1cYiOmfiiWfVHSxMAVtutZi2QKxxMsKCMdpq46hJ9hoyHT0jzcAQq9cvUmxHz8k-so28WNTkwFRq4qNKcSb9EhQpscJO71D85OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPRGZ8PuO-kclNyTsktAxau68mF-Ooy2B4HvIjaOihxHuvqo6MGBMAEdYzy04rm1ktntrJt91zqonmLnHb6Do2yCxz0OWEbYtIc9rl1jKTWOPVSR5aOgAmzIAYznO_Ly9FDGXcgE5QcG0R4BnuqXgPM0B-Ttx0hr7L6BemXsTPx-3dMHUxO-eVj2k-HqFQKd5lZRM623VB4aKRf8Txrhups4RJj1-2eotwfaTnCg5X5X8wYgj2UH3vXQu0rhV8j-EB8A_ccH2I533pJi6sitHFcVFywd3nukEtv-tG_3Zz-toaDtNn4VD4TM-op2Zx-UqkJvoelGTF-ssEFU_xFhSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لست دنس و این حرفا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98664" target="_blank">📅 00:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32526464ce.mp4?token=kHM2RsbvMQHvRnH4r43fbVu1zU8D9EzZcmIBU3__EzRQ0Jug2Y9QSMAN6SA15X5M3LYpk2U9YNdI7f4Hk45OxlNdfEG-184TkVdhAPiYARlmnIY5Lw25HwWeGlNJ6vJn42RwSjVyBs8ZeA_n-6Q87jQIDBU83q8F25xDz2vaC5dnJTNj_f_MFVVZnqptSZttUwvRm_5Z2y2w_WITlda5Ga49SfTt4LibT8DQyyJIHHS8Y27GjMr8D7DtGnzDRYkub1-eehaA5qmo3cFDrXPEFPK-lUGlP5_TX0waUDv8u4tet1VRakDIH-wZtATPw_tuIXAECGI6ykf8zehlzJ_hNJJyMzOlmuKBlu5u_9YDouO2m6H2bjONiwgyET3nuWXmq_9tR9eiyz0mX13xnwXgeQXMfJKllW___314bHWFDcExU9yGYDepAqr9mE-IdM8fVGdRcV0We-ysMN-nlzXVY99pI_JUO6fvS8-NAiLbVDahazYSBPgyhpEXzebDkxEeJ27Qe0qyMt0p-HAmUZqevn-5_CtAAMW_UH8j2KjIV2fm3_LG_2XZ-Ue5RslbDun-Cb1iQcQRsKcD3567MDpyrVxG6kNmxo284q7Up8Bk1R2xBNsmB3Qe2kF3FSn4JKq2Qyxm0p9U3T6M3mXRvdNA-3OsVumqcpIY_qNmQMcgYO4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32526464ce.mp4?token=kHM2RsbvMQHvRnH4r43fbVu1zU8D9EzZcmIBU3__EzRQ0Jug2Y9QSMAN6SA15X5M3LYpk2U9YNdI7f4Hk45OxlNdfEG-184TkVdhAPiYARlmnIY5Lw25HwWeGlNJ6vJn42RwSjVyBs8ZeA_n-6Q87jQIDBU83q8F25xDz2vaC5dnJTNj_f_MFVVZnqptSZttUwvRm_5Z2y2w_WITlda5Ga49SfTt4LibT8DQyyJIHHS8Y27GjMr8D7DtGnzDRYkub1-eehaA5qmo3cFDrXPEFPK-lUGlP5_TX0waUDv8u4tet1VRakDIH-wZtATPw_tuIXAECGI6ykf8zehlzJ_hNJJyMzOlmuKBlu5u_9YDouO2m6H2bjONiwgyET3nuWXmq_9tR9eiyz0mX13xnwXgeQXMfJKllW___314bHWFDcExU9yGYDepAqr9mE-IdM8fVGdRcV0We-ysMN-nlzXVY99pI_JUO6fvS8-NAiLbVDahazYSBPgyhpEXzebDkxEeJ27Qe0qyMt0p-HAmUZqevn-5_CtAAMW_UH8j2KjIV2fm3_LG_2XZ-Ue5RslbDun-Cb1iQcQRsKcD3567MDpyrVxG6kNmxo284q7Up8Bk1R2xBNsmB3Qe2kF3FSn4JKq2Qyxm0p9U3T6M3mXRvdNA-3OsVumqcpIY_qNmQMcgYO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به پرتغال توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98663" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پرتگالللللللل پرررررررررررررررررر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98662" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرتگاللللل پرررررررررررررر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98661" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98660">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مرینوووووو</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98660" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98659">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلللللللللللل اسپانیاااااا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98659" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98658">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تورس چیکار میکنههه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98658" target="_blank">📅 00:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98657">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برناردو و کونسیسائو وارد زمین شدن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98657" target="_blank">📅 00:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98656">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تورررررس خرررررر ریدههههه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98656" target="_blank">📅 00:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98655">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسپانیا فشااارر آوردددددده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98655" target="_blank">📅 00:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98654">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98654" target="_blank">📅 00:11 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
