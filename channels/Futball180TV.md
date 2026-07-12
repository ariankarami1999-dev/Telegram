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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 591K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 11:09:31</div>
<hr>

<div class="tg-post" id="msg-99789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=Nu79AObJmEXgnLx9aQHGzLzeZfz7Oq2yh-rGRtXxgfnVP930-mUKdNCwzVl7yKdHCkchci6oPWoql1CV-D7O4InKSwW1PaDb3ChtErakXRTRgZu8vtL2LbrSEhF01BOKcEyo9ojGrmBmZNXTQeRYXG4uGP42eTaBoez_VFBtcrCHcDAuw1xAdTLRVxQ7nqxprGdjGtw2l9YoW2TOs89N-VByDW6shfbcfo7AVJCtACLqxBnevq4gNZNKwXVm7VZaZT7riwXIeZ-aH2S2fXvXHBpuvdq20GwvuwiVEfDvCRba7lGy52buqpkS39lyXWVdh74N5or5A8SStO4y93Zalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=Nu79AObJmEXgnLx9aQHGzLzeZfz7Oq2yh-rGRtXxgfnVP930-mUKdNCwzVl7yKdHCkchci6oPWoql1CV-D7O4InKSwW1PaDb3ChtErakXRTRgZu8vtL2LbrSEhF01BOKcEyo9ojGrmBmZNXTQeRYXG4uGP42eTaBoez_VFBtcrCHcDAuw1xAdTLRVxQ7nqxprGdjGtw2l9YoW2TOs89N-VByDW6shfbcfo7AVJCtACLqxBnevq4gNZNKwXVm7VZaZT7riwXIeZ-aH2S2fXvXHBpuvdq20GwvuwiVEfDvCRba7lGy52buqpkS39lyXWVdh74N5or5A8SStO4y93Zalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
لحظه اعلام خبر درگذشت گراهام توسط صداوسیما و تیتر: به درک واصل شدن گراهام رو به ملت ایران شادباش اعلام می‌کنیم
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/Futball180TV/99789" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: به پژمان جمشیدی با تاکید خیلی زیاد گفتم به تیم پاس نرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/Futball180TV/99788" target="_blank">📅 11:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=BgYBQdExaGgF-zT61CEfVPiw8NXWqWv8OHC_GZEEXor2vIEfUviwUqeKLHxSKOPl1GRGjGurm7e5obAvAc-S-TJhX7h7JRQ9JisUH5kZdqa2tYOavL90NHqJLgZkV1mzt0jN21RhnuXj5HAXhguKnvTNxJ2WNPkXJBkP9gQzMnfdK3fuz6O7lr16MDCVfQU_0oQoqGlU2ZCChiih1gY7qH0j45a2IpI9x-6wlfsp1-E1xmLibKaLL2LyqS8OmyL8oaQK3U3tXElqTBdeOhk1YlU9AP8vnCrpzh3WNtFnFACBs6iFuA8CMOOTXwBvdX6AnKx3pv10ZOZhQU111W8nuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=BgYBQdExaGgF-zT61CEfVPiw8NXWqWv8OHC_GZEEXor2vIEfUviwUqeKLHxSKOPl1GRGjGurm7e5obAvAc-S-TJhX7h7JRQ9JisUH5kZdqa2tYOavL90NHqJLgZkV1mzt0jN21RhnuXj5HAXhguKnvTNxJ2WNPkXJBkP9gQzMnfdK3fuz6O7lr16MDCVfQU_0oQoqGlU2ZCChiih1gY7qH0j45a2IpI9x-6wlfsp1-E1xmLibKaLL2LyqS8OmyL8oaQK3U3tXElqTBdeOhk1YlU9AP8vnCrpzh3WNtFnFACBs6iFuA8CMOOTXwBvdX6AnKx3pv10ZOZhQU111W8nuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
میکل‌مرینو فرشته نجات تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/99787" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=QIgypOu8EopJ0xFCIJ6YcUdONCBFnbfMeWxMbriuXB2vgrwtTmHRNknGPIPoSdv7LPK9wpwWBOtbEnnSlwXiE-KniETUUCuNag0UXPb3cszeXepeB2NC8qE-riEeA2vU6Hvcr6MGG0UT2mjBU-ZAk69K4dyWHceToGU1-vkCvSuCQyucgMrpCHn3gKGHep1Ngb5LAsF7UY1-qab3VIvGr38IQSvG-n9kTyTw8p3Q57UegUB3b07-17_u1QZ1JFD38RuBCjdeAxLBWgp4CdNsnoNFnJcGok81U1P00MjuwXYpJ8cbhcd3JIhd_qKK0agcYFxRl6KxX9z3aefHXK1q9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=QIgypOu8EopJ0xFCIJ6YcUdONCBFnbfMeWxMbriuXB2vgrwtTmHRNknGPIPoSdv7LPK9wpwWBOtbEnnSlwXiE-KniETUUCuNag0UXPb3cszeXepeB2NC8qE-riEeA2vU6Hvcr6MGG0UT2mjBU-ZAk69K4dyWHceToGU1-vkCvSuCQyucgMrpCHn3gKGHep1Ngb5LAsF7UY1-qab3VIvGr38IQSvG-n9kTyTw8p3Q57UegUB3b07-17_u1QZ1JFD38RuBCjdeAxLBWgp4CdNsnoNFnJcGok81U1P00MjuwXYpJ8cbhcd3JIhd_qKK0agcYFxRl6KxX9z3aefHXK1q9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
جوری که جام‌جهانی قراره به پایان برسه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/99786" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9VKKLPATwEn1zmyI-eMVZue-cynrZyOSsM5bW97wIX0wT__rOU8hO4TRf3IyQtUm7SUe_xE7Ghvn4BaAEeXFHHFditp2JY1SZgEijJ6suMfr9Gky3NelLKXzmBoPGx9YnvLLKPGdeVI3ggLABuu90YJqTiIhV2DNI1VFPkqPQLrhAUP-CmuZ62vtLOlrKSCvejRMhv__VK3uliKHyKR9lbP1DdLVX1chwsaoQ8-tQkgyF1utDLwrrr9ZSdsC9j-_Jxj3TKBAi5kV4tZdOLLeFAkpkH4NOane0n8jaZnMn-9LGw0SoWk39DKPZtG3r27b5mAIC-ReaNK127baf_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulEqZo3ODmo7nbSfda2xlqp0Iv79atwd62zoYpEKVkVSioMj-YoxTV2_KmaHgB8wE5u3OAsBHdfymAt7R6FblteSWRGdoEfd0rmWUxmNp8G9lY8sMx2C6lzmf1kPz5an9mS73G0xDhtyKIUr4_00hVkdpRfmtCXrF8yKXCy8jd3BkCDB0te0qoMC-X4-Ejwg_RJKb6dEhsUQmNMSUUxDU0bOBZzYxBjuIgqlJEUHLQThHltYBhpCaBuB92B_L0GAcTpqmuplGBEsBVO-8JH3D_4yE1LCrBEZ0EWd1yL1Hv-cKvKWkNJM3Et6FXpqeBApDAo64MWKh6meVqXS7MEwgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چقدر به دروازه نزدیک‌تر بازی میکنه مهارنشدنی‌تر میشه. انگار بیشتر یه مهاجمه با قابلیت‌های یه هافبک نه برعکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/99784" target="_blank">📅 10:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=CZ-0i-blSRaZUNhnHgTZItzQTKvnaF16skMkZnmZ8yp6RcqRhtvjQgV6K2nOnRz_32CAwqaRoH5sia5Ke_--bxOYe-Wtzog5tiFDEpa7tT3btlajjbjer5TepZUV_49IsWlUN3L7eC5aVn194KklA-H4h60GG_PgZ4dmbIOhlbidn262kqyiudADqGeIqTMjZukarqsrtfvJc1kWl4SrBVv8EULxmb93DG-O031C6rrNRTvMUIbFeKBP4lVxooSdZDvp0sEnnPpuaT9v-7sP7JGOsowG7v1dlkdq5dBlkyhtucHVQb4ndaM6a-EteqB3eW-jD_ZFebAkPwJmqi3_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=CZ-0i-blSRaZUNhnHgTZItzQTKvnaF16skMkZnmZ8yp6RcqRhtvjQgV6K2nOnRz_32CAwqaRoH5sia5Ke_--bxOYe-Wtzog5tiFDEpa7tT3btlajjbjer5TepZUV_49IsWlUN3L7eC5aVn194KklA-H4h60GG_PgZ4dmbIOhlbidn262kqyiudADqGeIqTMjZukarqsrtfvJc1kWl4SrBVv8EULxmb93DG-O031C6rrNRTvMUIbFeKBP4lVxooSdZDvp0sEnnPpuaT9v-7sP7JGOsowG7v1dlkdq5dBlkyhtucHVQb4ndaM6a-EteqB3eW-jD_ZFebAkPwJmqi3_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند اینقدر حوصله‌شون سر میره دست به همچین کارای کسشر و احمقانه‌ای میزنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/99783" target="_blank">📅 10:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK6SLFNlz8bBvcp8SyORv0YD1e6p1BptCct6Hx1y5hFqn2hb0i0WoTZJJl20ZoWqBJiwy9DQZAmJO7kt3I3sl9DS1IMIg3Joi_fLY7V1A8NyW-0BQtRo3TYPtUZDubY3N_6KXdBmqebs5JI_JvkTsReumhOkYZUtgaw-MIwtqo5Dz8EZRUel6YPIZkPCW2uwGjfZ8-2mzQYCw7dXEMKEBRtoldIkulXWBijIQUdqH-r5A0KlsjopkrejYX068uHoNiGTBu9MfLvVUy-FyB9eDqOw5H8T92niNfEsGiV4SpO82eNvjY50JFtcu-NTM_271y2GiPW50Vc6KY9OaXkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام سناتور جمهوری خواه و از حامیان ترامپ بر اثر بیماری درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99782" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=MuNX3ySVfFG5r5VfQK8WDGd9WTQIXyDiL-uYVnzxb2SE5aKJHuKNzz0sHkagEFPckbatv5z7RkP3HHJ1BR_lusiFXfd9j-ZApKLGItF7MxwfpDCRLQP5-g8-mkHV3wjW4VrVsTPw0e-91M0GC8gz3SNkxvF2XzJXrsByAbjL7MxWTRAweSGtZlQ8rb0trbAnNWlRLEhwO2CY8rOdBht3MFqstn2rn9DXvyHhtaBtPutTXhRfr22KD1kq9wsIihrEuYIiZSIn0qBd4hrFMtDqiVL8C1X0BYD5j2rf5dbRkZt_PbZm3e9UC41DKXRXQAp6AREcW-caKn9CwLwNXUE3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=MuNX3ySVfFG5r5VfQK8WDGd9WTQIXyDiL-uYVnzxb2SE5aKJHuKNzz0sHkagEFPckbatv5z7RkP3HHJ1BR_lusiFXfd9j-ZApKLGItF7MxwfpDCRLQP5-g8-mkHV3wjW4VrVsTPw0e-91M0GC8gz3SNkxvF2XzJXrsByAbjL7MxWTRAweSGtZlQ8rb0trbAnNWlRLEhwO2CY8rOdBht3MFqstn2rn9DXvyHhtaBtPutTXhRfr22KD1kq9wsIihrEuYIiZSIn0qBd4hrFMtDqiVL8C1X0BYD5j2rf5dbRkZt_PbZm3e9UC41DKXRXQAp6AREcW-caKn9CwLwNXUE3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
صحنه زیبا در حاشیه بازی نروژ و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/99781" target="_blank">📅 09:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iu09V4LnCM-6_JAy2pX2AXmSgnMkAyR0d-Dqx62RMdJ5cvT6rPieI_bShj_i0BFNxS6oiQlIfM2lsC9QfFO5nw1w6f5R4L9f2TqNdcktTxs1pzPbbsexvpRv55T59GGCcK5kd2CmcaVnPvdYiIiMVu0HAXIR-smRluJRfcBfNPCC5r4kj0-ROgGL_Y1j202wJrhHbgyFfl_1o16sIZCs3ij6BO3XB6N4P6doQs4DdP7MQFyKM3UrP_aJ3swPuHVkGQTkNKb8WROPlbz5Kq-LTNwgOXrtffxG6whipaJy-UmiLDMQqXEwYfHlHUcDauiG7KAfIONA1rUgRR9lSqSwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iu09V4LnCM-6_JAy2pX2AXmSgnMkAyR0d-Dqx62RMdJ5cvT6rPieI_bShj_i0BFNxS6oiQlIfM2lsC9QfFO5nw1w6f5R4L9f2TqNdcktTxs1pzPbbsexvpRv55T59GGCcK5kd2CmcaVnPvdYiIiMVu0HAXIR-smRluJRfcBfNPCC5r4kj0-ROgGL_Y1j202wJrhHbgyFfl_1o16sIZCs3ij6BO3XB6N4P6doQs4DdP7MQFyKM3UrP_aJ3swPuHVkGQTkNKb8WROPlbz5Kq-LTNwgOXrtffxG6whipaJy-UmiLDMQqXEwYfHlHUcDauiG7KAfIONA1rUgRR9lSqSwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
واکنش تند فیروز کریمی به عملکرد بازیکنان نروژ!
فیروز کریمی با انتقاد از تصمیم عجیب این بازیکن گفت:
«اگر دسته سه تهران هم بود، پاس می‌داد!»
😅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99780" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhV3PcdchCS7tpvcv0IgPAZi1YpLiYKFGvfFrdUpZNZjBj5e1bcQOHjK826XvmZKZyfu2KcKGZSpvFC-TuVwybio6uDbz6LaTBfznJ_wckAWFCy8yWGwrlqQVKyIVUQy6IWS24Z1pKkxM5uqgA69bUA7Z_XddKcsvRdjg6fV38Z_sS3hPr_PNxM-vZz2xN6zgx6I4KjOU6Xei4jsFnqL7o3_gYz_R1TJNqrRWjgR2p-8vv4zrbsB5r_uq_oiH3Wfd8h5ZWqSBSPH6MjN1uKsSUSS2Mo_yPVy28BcvHo_pG5fYKvwVFkGoi6Tm2YslJtUUmlhqOifBnZzl8YWMW2Bug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک امروز 1 میلیون دلار رو کانر بت زده بود، که تو 30 ثانیه اول باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99779" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=qOiBaHffGGC8PuZiG5Yry-NXBTz6MWbl3D2LKJ4QmpY_-8pcByYF8NIswU4avyDPXMKZ4uwu7_XATIIb0v7F8qci5afGP01hdDqyLKDMvAHzLUAekoy9yO46p8fJ9pgySQNTAQNwCO6QOEH5ZeRO-lfCqwLR8NebuKXoYY1O6lpGP-EAGG0V7QiVtLGJGCythvFlmtKOaye9AUwCSMfH10BDQ99QZlJyx-YIEmT9HTfMz4IGHNIevJBueO2XCaVOoL4YkXNvWPo18zcgvXigJw7sUbylUyLHwXU7exFTYH5colMSGqIw4kKlc9ExTGux81_rwEQ5pnVVK8U1yEBQLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=qOiBaHffGGC8PuZiG5Yry-NXBTz6MWbl3D2LKJ4QmpY_-8pcByYF8NIswU4avyDPXMKZ4uwu7_XATIIb0v7F8qci5afGP01hdDqyLKDMvAHzLUAekoy9yO46p8fJ9pgySQNTAQNwCO6QOEH5ZeRO-lfCqwLR8NebuKXoYY1O6lpGP-EAGG0V7QiVtLGJGCythvFlmtKOaye9AUwCSMfH10BDQ99QZlJyx-YIEmT9HTfMz4IGHNIevJBueO2XCaVOoL4YkXNvWPo18zcgvXigJw7sUbylUyLHwXU7exFTYH5colMSGqIw4kKlc9ExTGux81_rwEQ5pnVVK8U1yEBQLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در نیمه نهایی به آرژانتین رسید!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99778" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=dCcpVeNlq5RgfV4Td0piGIPP05bT2xKW9Zs9Cb83QcIia0AMFPb8duL0l2XuT8qHft5MJko27WlM0fNTuo3BF1OFsdzMNKJRw5OCTR2qTo6W_3QPZs-ueM51YmYh7276HAKWrFz4q_rU_9VVrCfpKKSThN1OLQi87Wx5_Hzx4xFSGJQezaT_ma6Hf-F7m-Njg9cErsoCTCJAiO1LnoEVgqMKN-98_hZJk4tAI1TWiSX47gTIWBtcBuWf1KEiBS4PZ77Yxw9qZ2m96Xh-hMWPPGaof75NCK-fEEzFjMC3UVYRnP1ncc2Bud3_Q8KLNUm4rZDGqmE2ZN98gp0p2o8nZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=dCcpVeNlq5RgfV4Td0piGIPP05bT2xKW9Zs9Cb83QcIia0AMFPb8duL0l2XuT8qHft5MJko27WlM0fNTuo3BF1OFsdzMNKJRw5OCTR2qTo6W_3QPZs-ueM51YmYh7276HAKWrFz4q_rU_9VVrCfpKKSThN1OLQi87Wx5_Hzx4xFSGJQezaT_ma6Hf-F7m-Njg9cErsoCTCJAiO1LnoEVgqMKN-98_hZJk4tAI1TWiSX47gTIWBtcBuWf1KEiBS4PZ77Yxw9qZ2m96Xh-hMWPPGaof75NCK-fEEzFjMC3UVYRnP1ncc2Bud3_Q8KLNUm4rZDGqmE2ZN98gp0p2o8nZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😆
😆
😆
مکالمه پاره‌کننده دیشب هومن افاضلی و خداداد عزیزی. کپشن اصل داستانه⁩
من از شجاع پرسیدم!⁩ شجاع بهم گفت! گفت که بدنامون خسته بوده! خواب بوده
😂
⁩⁩ ولی هومن
💀
⁩⁩⁩ بعد همون شجاع
😂
😂
⁩ گفت غضلاتم همه گرفته، عضله رو ولشن!!!⁩پاهاش اینجوریه دیدی که
👐🏽
😂
، اگه پاش اینطوری بود
🦵🏻
آفساید نمیشد ما الان بالا بودیم
😂
😂
⁩⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99777" target="_blank">📅 08:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0WW-fZTWPCJ8KecTEw4KuRGEjdkqr10JZJV5Y55kL3GzE9TphHyHed-O3Ei9HkcVCvXltYLD3-VMeiu43bJMvzA2FAXGoCC8FahMIzMAkfl9GsBvu_0-nYCttV9kLrmWlkFKIeIU7TmYdwLmkUKt8dHksn-8U2eJhD1JNM7M42jh0H4Sh6WgEp_kUoRjQV24bVtQ_FkC1tctwfrHp0aEDay4xNiHF9M2K4KaEjXKnSQ3JQz2jApGaBZWVKpzMhNCcrkp-2LMtf0LbxT6iejm9wcHueXqt_HbavhbJMjYDplYLTUDqPCvNzXsDsu1UvIugCyq68wdmSBESWwiL1Eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی اولین بازیکن تاریخ شد که 15 بازی در دور حذفی جام جهانی انجام داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99776" target="_blank">📅 08:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPp0gOm9Iehanw7u19b1EAIlafqTEbdTBy0rJuLFUbEQyjqDOEnlMpMGDLp5raY3TbDQ2Nf2TRdLFCtQ5qlY4EC7D7C5OD2pT0XOJWgf9nMxfs6OizF861LBVVMHk4ydRgOKIDBWDEv_9czwND-C6a6v10qh9Qi5ehy3-ljtzKcAEkHG1v-JIcNZmFVlXq1PChZMoXIX3aTtX5L341lvbi3COr4Ny9zJ2rRKximP62Y8lb9-GdwoZRF_BKqx5SbT-JdxVJ36geutikcCppefFLa-dmGdafja3bE64y_qYRMW4iYe_NeBSre3x3eY7S1-KsKOkOZyEjxwKjqAz5Snkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇦🇷
خولیان آلوارز: مثل یک ارتش پشت‌سر رهبر خود لیونل‌مسی هستیم و هرکاری برای قهرمان شدن مجدد وی در جام‌جهانی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99775" target="_blank">📅 07:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFdaxjjvYLzN4eYXQ0FZ_jyU-2KeFVflJ2085mw-nPviwVvyE9f9w1MPcH_vDtazvcq6V4W2ogcrl04AKRuBeotrHpXEOrcXVyuLxN_e1gNS_Ygtm7nNbwthMhCb0PKdXgJcIk8l0O0i-YmaFJMTXmiC3_Det2xPt2-9dvtbgq7ID2eXYv8L1no-SqRTCVXy2fPSQRFPCE7brTVHAbNkFs0BTrbqcul6dbiYM9GZ_TQu90NDS3coBwYNfKcXdwWh22rc3kVjzLhNU3b9qkDBkXP4Vk3KvWv4zz8c33x88-Okv2klTDy4axDFFgLuI1OyXX299Jmf46oB67SE4ouDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تیم‌هایی که در طول تاریخ بیشترین تعداد به نیمه‌نهایی جام جهانی رسیده‌اند:
‏12 بار —
🇩🇪
آلمان
‏8 بار —
🇧🇷
برزیل
‏8 بار —
🇫🇷
فرانسه
‏7 بار —
🇮🇹
ایتالیا
‏6 بار —
🇦🇷
آرژانتین
‏4 بار —
🇺🇾
اروگوئه
‏4 بار —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99774" target="_blank">📅 07:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTiUmXrG1tUYBQzTXjuoAR1FqM0vZljsSOqrIxneQRrHBuqYc1PHWIqFtqGO3Uabe_Hpj2ZUOmTCz3wJtQPDSVWGD1pmS6bjc0AWzB6n6QtIG7Zd_1Q2gEpuGcE-VowINHNQlyQrdF0nzXHDNAKK7lKkE7jZD38B9kVyjh2L3IFqYooXFV_mQQ3pI-7dJyBak8eLadtJ_C2SA26-QieBbRIOLo069s3o0fDqttgLzdbR87lw6ntQmOhBJYvA2Sj4w1iSqJEKXfT1VxTZw5-bJRG9yqIwjSGiDHloVtn8wCVvXg50MHuLYHEJBO5Y5-gF3DPhSO9hOE68ALQ6hthWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
خولیان آلوارز رکورد مارادونا با ۵ گل در مراحل حذفی جام‌جهانی رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99773" target="_blank">📅 07:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHu-O84uyAylojN4Z4YszezwNbD16Cp8Rc97otxmwMJOcuou-XYjz0mcxaf2j4EfC0u7p2F9T1TJSEPJ_NJhu6L5GqIUs9L7cYWePlsyLpoBRY0KkO7Wq80_jZPLHNLu6BDFWiE8Bc6fWirC29kuadXG9bjTq9MyCFVNAxd8i_8ILwTV7yjTs8lIFXrghKOt6BO4vtH2aIf7YpH2tzLNyPU7MN0-0QMxQ4IpytE5xAuhrN_fNEfgXI-GeA1TSgVnRPgVuPvEUgcQJ-sH9-MF8KDC-umupKc3m65oZX7qd66CyZwlJflAYdzFTJ2O5yVavq90JHanrLbCgUp2XPLGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آرژانتین نخستین تیمی در تاریخ جام جهانی شد که بدون مصاف با ده تیم برتر رنکینگ فیفا به نیمه‌نهایی صعود کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99772" target="_blank">📅 07:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIvArxtDIc6XuJlaQYmHsuC84HeOHYccE5h4_FrGfTm3kqINA97Ihy48JLIvfsZfURLxnRwPRrEizvvsopcs9maHUQRF4rnjFCYVWjqTF_8ZqqjuwCZAmjhX0bTiGmueJsR0-2t95f5WvPQyeA8ya-WjCPoLARO2jKxiziYGwNuRiBV_4ig3Vqi-GGFzAR0EpPq2v5hHMvT1F7FcqY53PgCIKezerARWGUTQ9hM7TZ7atqJf9yxV9DG8YF7V8LaEBPskeBLyPWCTTWDp0Zi-p1Tv2MsMztqKp_f0Cf2jhZbHcX7M9cwUqIqZmepY1cyHcIHj1-wO1XjAav0hSKEM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
| برای اولین بار در تاریخ جام جهانی، چهار تیم برتر رنکینگ فیفا در مرحله نیمه‌نهایی با یکدیگر رقابت خواهند کرد:
🇫🇷
- فرانسه (رتبه ۱).
🇦🇷
- آرژانتین (رتبه ۲).
🇪🇸
- اسپانیا (رتبه ۳).
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس (رتبه ۴).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99771" target="_blank">📅 07:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=HEpZI8rsx_hMzH_WRYvoJYwk9GV1YKxo1BYMTmLf6Yfe1YAlJBciFrRIsW52aBonV7RWE6Ykdm599p4_ZG5ji3Ngu9drnk_EhQ1LyGN52hs1I9C5RbX3xCMpyQ6PPr8Cn4cjNnDM5w1RO_d-_wFw8qw8-A6KUIzHSYJACRVHkMfEs7yz-MkBtsXFIYbAtlxj1e_AyhMpzszd__MriiVvJ4FaKHAHZb21m7K8g7Cjams36V2juiCu_YC0zUsKSmh8g_6waYl9MS1VMQBqR9V047uCIyGUVDyCOBj_fYTYm0QUuxzhjti25sZQTv_qRBkQwmISuxNdfUKUlhZdtrHD0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=HEpZI8rsx_hMzH_WRYvoJYwk9GV1YKxo1BYMTmLf6Yfe1YAlJBciFrRIsW52aBonV7RWE6Ykdm599p4_ZG5ji3Ngu9drnk_EhQ1LyGN52hs1I9C5RbX3xCMpyQ6PPr8Cn4cjNnDM5w1RO_d-_wFw8qw8-A6KUIzHSYJACRVHkMfEs7yz-MkBtsXFIYbAtlxj1e_AyhMpzszd__MriiVvJ4FaKHAHZb21m7K8g7Cjams36V2juiCu_YC0zUsKSmh8g_6waYl9MS1VMQBqR9V047uCIyGUVDyCOBj_fYTYm0QUuxzhjti25sZQTv_qRBkQwmISuxNdfUKUlhZdtrHD0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی عجب کیری خورد تو این جام جهانی اسپید طفلک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99770" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2b50xeXXX25DxxeAJ4NlBLlMvmXl_4K7ZHHYRCHL6I4Z7mWbUWrLEHN_RdnJ_5USyQzSoZGogH4k6jXKphxt0IA6JDnMxG9t1zM9fhtCGcoS0TFsV90_-tmkbLzJJ5Rjs4o0SFUq3dZh2ubMChEBLUobPBSPAyPSzqiUFuts3HBmvsGwl3vOK7eF0cnWdbtgUMLVEOZlextAM23me8mEqXQqbVU43ZFTV5_GlIC8fZ0KPyQbA6fksmm_ukYCarQybfGjkWY7a2CPvhuZ3drHJKX9gH2oKdvtz8yY9wfrdI5FCb65UIp1-PvL9_Iyr-pDycdEcVGfkfu-9ADONfDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🥶
🥶
قهرمان رو با ریکشن نشون بدید
🔥
فرانسه
❤️
آرژانتین
👍
اسپانیا
🤯
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99769" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99768" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpyr4SH4-R469jav-fycJK38RigEITIeWbdbNfIzaIFh28H4-HNC1SwtekuhGugQEdku0b0UP1ZNd5CbbbFyoc3y-GrDRMz5xDEVGP-LA5jxFcfugQiNQ4Kg_HsMwH8iNPrjtHkir4tLOVvaaf_nBI3Zahmoh3zu2HBxeu2ds0hJFQnhG8YDofCkbdo_cyGqhelXWAFUN1YysG9j7Jr-hj_pJi_VAnkM8mPndTOeQMHpj4mVntnoazrH9p36eUU-DZirJD0NIxj1yQHlB2eRI74K64HanVXfgYfXKsmlqb5zC6OC11o1hncaVA8Bc3G6W5ydOAYDPPsN3beU4w4bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
برای سومین‌بار پس از دوره ۱۹۷۰ و ۱۹۹۰، هر چهار تیم حاضر در مرحله نیمه‌نهایی جام‌جهانی سابقه قهرمانی در این مسابقات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99767" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99766">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGbcBRl_up9aDPyWieHubaYBrx9yzqRn4tmI1TRVF4_Th9rBxfpzTJLSb9MHhMgAEiz2hp-4pi_mMYpEouzGyzpyh-KxhBij3nO0cfbUGy03bxyt7XYZy1owT1qRyvm-7_P0T0O0UHFM1mMY6yPhu1hlM7bOJYBWRm8fO1U0ajafZdDKPeCQDKkpJQZ_e8f2LaXGB1sGFRRxb6di5pzWo9mZKTkGhFkNQSvKWXUcrr7K3JSV8V2tw99-dNFUgQJTpjdcF2V5TimK5vDst4fHUkPtnK23lEi32Tfwjo45LdkKCJwEEwJMA5c4xHyvsn__RcvKXDA3PMP8pNBEWQoWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسو ببین یا خداااا
🥶
🥶
🥶
🐍
🐍
🐍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99766" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBP4bvrj6z6mo-ul_uFDHERlmYPKa9lV6aRcNvek9CaBD6xutDSLpd6rZoVAhRKI-neeULFypY9R_bGLL1CXK3BKTikwsLPtOzIHuhkkbaFaN1pHSj-lc3XVYv-120olRUZXB7tHllhwHXT8vUrR_O-zP76Iz6aYRGu8K99kqiKbvWxEP7eOHLRs9WGsChyOypH72egemyZ3n2TYLxD-vPH33aeSQ1XFvpmlulQ6VbneZoZG-4I7vfVmOpQbX2XZE8Soyie08OuzobZz-S8wHoc_AdlVaK1D3npACG-hvAXl_zz3U56MoqCB8j5lKZyD9X6TBQcc1DE6mNTJUW2gXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی برای اولین بار در دوران فوتبالش، مقابل تیم ملی انگلیس قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99765" target="_blank">📅 07:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99764">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eecRMQBnSqVmK7pi-R_VVRfEoT1KEhneS5k7vxUnIxbP9lZmibgWt0XI4edJBugzaMjc0ngli3yLhvlZ0BRF7QTDTsKDs4UVTqS_cwcZPr_Mhp-FNuqwxj-5e9Y5Urr9FOk6LGqpZfg4qMWVvwbPGNja0yVvukQl3o3OqLIIbjLTBxOTVh62PRj7kU1LPOm1Y3XXwfdpS7sa4Nhv7Cwl4613KfbjDcF8jg8zGAJXzTRvw4fvab6lj4l5xuRUeoYLyj10rxIRjz69hA5tRHG3WOi_08SgHXvKCW0-ATNHzrAskzonfwkPT5neHetqKxXzBfqPPxZM9Xm-jXhfEiu9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99764" target="_blank">📅 07:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99763">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYKPdzA4LiXPDVDaTtR_prI0AIW0SkLhHGDDkNvMMPmDP2GyXp3eKhP67sH7AByXa_gLueEV5XlK-PGINhOIRLjNEqBhZGh_pI8Fmcbm1ahbxKLakdsSYfxNq66jZeCZRcenm4WGVBEGA2c3EEMdgl7o92Tnc6GXYS396Ser4wZIv1eC92bOo-fcTYjxl1npmAvyE_L7phQHJR832QLKAl8V16i0XV2INtySD-j4AoNR9AZMSJeoLsF2rWbgyeF4sKwMh4yZ0iJ5VcNBQcsDAMFUH6bQHzYZjadnHIOKTIobp7qHP8jGp0i8Z4AbjLy5A4jMh56iswWiV74TnAN7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99763" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9t7VH9oZOUbnkDP4NQ5zwr9b3mpgZ2krk5bIzDy8niRmmKmOFicOKrcd1R-3F4KgXtgQvP-gwigL7usiS9i9cNR-Iw19-1StqgEDVpzMhUfLkCnY9R_Z9dVY6jMLP_KP0KfAoTGh9qmmhtCzw-b_LT-p-Nel51PiQTWFrV1sV5gBa_QblXDN7c88WrU1IEAr1X--sj2mx5eRjweUNAYnXcVAFeCe2-TPo8jbfOa1gP-JdGlc8J75e7SRBVxoPsGBb7TF2NVbQWaWf8bEjG7kp3ZYK7qxizbdZIHKolU4gQT0kzSCobLjKAoo2sa-emSUwAxLmR2OpRcXUp384FXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99760" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSwOwD9P-wAg_Yw4JifPcCB1Xw1r72I_3nOBmhkZCexWtR6ndwxyxZ6o_J6jaA0nZNXxQOJsFUwkElQskXXUvIsQZdrPks2yZ33FdhZKvP4EDPLUGJJZ3f-_TO1FiVSpacD4TYjYlZbfsiaTcPZRUONSkCuMONywkK5IJ9Vjs0Xyo3_SteHK-NX1dtwI9RBMNgSMFkT2q_LiKUlhlHo-Vp-Zq5M16UYMVJaTtyV2hdiuO6MKwq-1KwOZ5y8DBQgy_zDXRzaCBMUNO69dbIv4pbeLw80XEVpoIj80-nc_QiCPiSEHAz5KrLKYF9ongnQ1GNkGyYxlwcJnpJetNpuaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
تیم‌ملی آرژانتین با برد مقابل سوئیس حریف انگلستان در نیمه‌نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99759" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TawV9NDvimXOSjzmqq2Wy2Tb0sjd5QeXbKRNirME3IsXa_mmyZemNLPLW8hHR2Ef-jp4capF3HRnEjK4uQKpOvGHeTA3nohKuHCxfxjjXVvh8tfDyXUes6p-gxihtVhUTWs4InT-q77gnLfJimBVbfiYLVSISJtDKi5Qep58Z71JH2V1ord_PzvXNLQAi9RV5xXEUv8Ca0OZaYullO2OPK0Qci4Eq9gUQMUwicDgpHVoH2x5PQsiFSLKkLvPehG0S7U9aAdE3y6uq_dzSl12lI846R2z6pO0FnFJnxXWsW24F5fSwmYaY7L7ABx1ZMQy4f8ZlkyC9Pl6uitDGcc2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|جام‌جهانی برای کشور آرژانتین به نیمه‌نهایی رسید؛ تقابل با سوئیس هم به ۱۲۰ دقیقه رفت. پسران اسکالونی با نهایت تزلزل مقابل سه‌شیرهای وحشی قرار می‌گیرند
🇦🇷
آرژانتین
😆
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99758" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مارتینززززززززز</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99757" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">لائوتاروووووووووووو</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99756" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">و تمامممممممممم</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99755" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99754" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دقیقه 118</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99753" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqeLsO2yZpkRSAsCT-ykb9gFKCQZvPDfLlRsAzY9QLPib0m73SOolrk9Eycs43S3afFOj5Z9eJVha_uOwrk7gszakUBJz6AWsLlla19NLKRhy4Bz1xe9uEs8Hrd5Ho-eDO1L_5v57lm8Njw6eyKPR8oH-cO56CegHsycTL-wvopi8RdPblhXy9XCKsBMklSGTwTNsJTkl7TaoGPE3YPF_J8b8xFtqNZwFZEE7_8-p6foE_1h9iXQFjkNS0da0n2J9hP-CYmuOf-sObjUf3iQj4Fyy1H2s_ZPhdHWn_u1x7D7e1wOtjAr-U82_53U8bTMeXDeGfpSbOSgxwJd4Bqntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز توپ رو فرستاد جایی که غم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99752" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9nDv5V_zUTGiDr3RJgLxJYzNBgpSFeHt0nZ4up6RMGs9VsYMT_yLqAF4UNKhiAcOhiAa9CR9_aZaHdw4W-a16ElOlZbXc7pmh0S-D9b80MQz8BOpoGktwoHsuKk3IkEzZX-GTtv-Qug7FH6U4HOVeO2dXDl68vpWIf6grD5lKugZuW6cYArZerujbL-wT8-NeKxDB5K4KYdMWYtOxRZVVo8K9cZSMx6cxRadJO6ByPBkVjD8exkPhZeAEgQ-Bd3k_OOEqEZt48zO43QtBGKH7WbVhscjJhFrdFkkghlu4rN57Ufen5v4lSoPOSlfqilzZ5xJHDQVwUwCbAccdcrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب جوی
عجب جنونی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99751" target="_blank">📅 07:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99750" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آلوارز از اول جام جهانی نزد نزد
چه موقعی زد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99749" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آلواااااارززززززز</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99748" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99746">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خولیاااااااان</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99746" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99745">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مگه میشه مگه داریم</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99745" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99744">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آرژاااااااانیتنی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99744" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99743">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلگلگاگلگلگلگاگاگاگ دودووووم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99743" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99742">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99742" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99741">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یا خداااااااا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99741" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99740">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99740" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگاگگلگلگلگاگگاگا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99739" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99738">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسکالونی با این تاکتیکت ریدی برادر من</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99738" target="_blank">📅 07:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99737">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیمه اول وقتای اضافیم تموم شد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99737" target="_blank">📅 06:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99736">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">از اون بازیاس که مسی با یه شوت پشت محوطه قراره بازیو در بیاره.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99736" target="_blank">📅 06:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99735">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عجب اتوبوسی چیده سوئیس</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99735" target="_blank">📅 06:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99734">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پایان بازی آرژانتین و سوئیس در ۹۰ دقیقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99734" target="_blank">📅 06:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99733">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">9 دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99733" target="_blank">📅 06:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99732">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آرژانتین داره فشار میاره.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99732" target="_blank">📅 06:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99731">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb5d00cec.mp4?token=FuSo3UhW0XhLCHh5UpTINNjb66T8oJM1g76zi5hTMwaVWhvIiTgYisCjvvz-pKC13UeslVflsPkWzeDow9HOufDIHc8M2V-4q2RCTLHvFKnBRuSiwCBX3RZywa0mvb7hCXBYFMyvnJzzDkn13uDCcl4oY9o6mtG61DpCkNeD_rX-FqUikNkelvb0N4nTsgtRWZvGt63tJt66fsutlaBIPCtCp_GUGAWdVqEk_whrqou2148i3xP8LNi1d0h5x37SyOLmCK2I7mH0GW7WtlWrmKCBUDLDGp3auNsRSI0RZC7EPfc_8R0cC3Ma6bpZL9nkJbolVW4UeeGKOCEeIbPf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb5d00cec.mp4?token=FuSo3UhW0XhLCHh5UpTINNjb66T8oJM1g76zi5hTMwaVWhvIiTgYisCjvvz-pKC13UeslVflsPkWzeDow9HOufDIHc8M2V-4q2RCTLHvFKnBRuSiwCBX3RZywa0mvb7hCXBYFMyvnJzzDkn13uDCcl4oY9o6mtG61DpCkNeD_rX-FqUikNkelvb0N4nTsgtRWZvGt63tJt66fsutlaBIPCtCp_GUGAWdVqEk_whrqou2148i3xP8LNi1d0h5x37SyOLmCK2I7mH0GW7WtlWrmKCBUDLDGp3auNsRSI0RZC7EPfc_8R0cC3Ma6bpZL9nkJbolVW4UeeGKOCEeIbPf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخه مرد مومن وسط زمین چرا باید اینجوری دایو بزنی؟
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99731" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99730">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بخاطر تمارض تو وسط زمین کارت زرد دوم رو داد و اخراج کرد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99730" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99729">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امبولو اخراج شد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99729" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99728">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b4b3a32c.mp4?token=qopqu6beXka4X2wLtpojtIA0NqqSu4w8z6bZ5HGs9AoV4buznMWHbjlNoWKMCgnnztKrxp8CyL_fXGyN9LBkjZMDhbN7h31BND1kVRcRkF6u1fFesL3tIV-yd_LVPyob1Ka1OIrekL1lnD_G8URP1JJgOApM1ggoK0mNd26OkEOb93hyxGQMMIvRRNxINmQQ77RqQPhaIb39B0qDJINHGxEPMcebzRaT6HXzFNxAwadoCySj_sHOIUpZiqlqvwJRRwAI9R1MTrtnY43-R5COQwIAYJTigsHgra3W7SGXoH5oFyZsTFTz1E-EHu3YZ62-gyXKOKjVyx4d1meiKkvsyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b4b3a32c.mp4?token=qopqu6beXka4X2wLtpojtIA0NqqSu4w8z6bZ5HGs9AoV4buznMWHbjlNoWKMCgnnztKrxp8CyL_fXGyN9LBkjZMDhbN7h31BND1kVRcRkF6u1fFesL3tIV-yd_LVPyob1Ka1OIrekL1lnD_G8URP1JJgOApM1ggoK0mNd26OkEOb93hyxGQMMIvRRNxINmQQ77RqQPhaIb39B0qDJINHGxEPMcebzRaT6HXzFNxAwadoCySj_sHOIUpZiqlqvwJRRwAI9R1MTrtnY43-R5COQwIAYJTigsHgra3W7SGXoH5oFyZsTFTz1E-EHu3YZ62-gyXKOKjVyx4d1meiKkvsyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل مساوی سوئیس به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99728" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99727">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">همه چی بر عکس شد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99727" target="_blank">📅 06:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99726">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پشمامممممممم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99726" target="_blank">📅 06:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99725">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دایو زد کنسله</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99725" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99724">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آرژانتین داره بگا میره</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99724" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99723">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پارادس شاید اخراج بشه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99723" target="_blank">📅 06:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99722">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اوه اوه رفت وار
😐
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99722" target="_blank">📅 06:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99721">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKxNAXbrxHsJbnt9e8Yrxr9hU0VL0MFspvsaQA7imOyPovwPA1ZpqEUVZCEaS4aNjj4fRnN5n6UDSuHfx0Mbu4fzfomR2rRUNTaBprNFKhzDZZTwB7Xa6mel5O7G44_x4nrwxDC0U687oC_rsUdn3GV8tjkpqxecRDojZPpUV61KRHI6Vov-lUS0aVzleb7LXWnpBwgX-cZk_aiBt6WM_akLeoetRFxcpxIBDGGsNxX3Rrr6merUeJ3FU3hpGC3aGFvOkkCNAup8RHo7vWNz2Y4hZ49WADTSpM7nHyHr-aZPMEQ8SAoOSfWCHMxy6aBZJT6Vdoxnik8d_incZhMKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99721" target="_blank">📅 06:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99720">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حالا بازی جذاب میشه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99720" target="_blank">📅 05:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99719">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگلگلگل مساوی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99719" target="_blank">📅 05:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99718">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پشمام سوئیس زددددددد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99718" target="_blank">📅 05:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99717">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گللللللللللللللللللللللللل</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99717" target="_blank">📅 05:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99716">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeaG_pt4xzdz-qhrftboehJud7nN03v1pe9vqZr-ffnmfZgt_NHk7cFuCT6CGt32yw5SgmXFUGjCJ4sQDEefs99TA20bhjkCOIp0g1Lz_WmgmZk4GzE-qlQNc2_EWKO2Efah5WfVGbbRHggioa9qdfWOTzhZ6YOdAIluo9Jndg73bDesjYqc-PzpaBHGVdLYvnDkz39E9Srda25XcuFj9o213C4XeyTvrpcbRKcU4jOHbt3J9HP9r_5qG2G4TLH_f5KYYnz_kKES2Y4z0UeB43U4o7Nl7d9skPcosylXHraBizIqXf2X224aj36c6RAHS-TkVkeSStTYMCO6F4mvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
صحبتای مسی خطاب به داور بازی با سوئیس: با من درست صحبت کن و بهم بی احترامی نکن چون منم دارم بهت احترام میذارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99716" target="_blank">📅 05:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99715">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لیساندرو کون آرژانتینو خرید</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99715" target="_blank">📅 05:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99714">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بریم برا نیمه دوم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99714" target="_blank">📅 05:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99713">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL0AEN7-vHdVvj_SkZgORbHkMsSA3DDGbFfKOh6hr0cEYVlFV-ZafENktMf6bZ7uFcVtu5nfgQwHvOJZjDsFjXziIfKYgypAKLlSXPIwhW4V361rfxRgv8ol6wWynjXSLliK2mqOUYwKJL62Bt8WahKc3ogW0UE5rRHN4Ha4eAYp4bFIc2dZErk8Plo7TGmNWhojL-wq6bOMIGqyeIghtS4On8YhyN935g_2SN3c3dGnt1BUwYG6KTyQ9GMRyZ36B9qjQG4d8J4KZcKAnJxQZyW1bLPpjyDMr0zGfJ2uD4Ex0L12KSMHIdxnKafr1oRas6Aioug6NXmnJn015fmkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر عکس جوون ایرانی که با کلی دغدغه و مشغله فکری و هزار تا استرس میشینه پای بازیای جام‌جهانی تا شاید چند دقیقه بگاییاش رو فراموش کنه یه عده چند هزار دلار خرج میکنن و بدون دغدغه تو همچین ویویی بازی مسی و رفقا رو تماشا میکنن
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99713" target="_blank">📅 05:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99712">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWOvuT8DAzZFvyfbJgeciffhRhFSKrP9qeWx_mpXHdErE4vf3cqZbQC9-TZcINPlzXHwreiDVh3GmF3dwYxOs997eJFmxAJwvssk6fSQxhGPK_dCfGybNgJIt1GeAsMSsOX3KjKnxKiN7fyUSTeaSsmkKhKjGe1SOEwz__PcmbypJ_KEURvpyryTsSsVBOkrKkkuAIMNwyIVoo3eByey2G93OWHCcZ7kNrR0G215TGbc8066gsmH8WZEQdmd37bLJN9GQcHWL3tyBFCce-E_tovaVB2U7nOPL2SveNplxLvnN03UnlgiqLpEjhMUW5nCDySeLSpeaHaGkxiwtCu6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇨🇭
آمار نیمه اول بازی آرژانتین - سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/99712" target="_blank">📅 05:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99711">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
پایان نیمه اول؛ آرژانتین 1 سوئیس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99711" target="_blank">📅 05:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqO5EaKsJwJBnsVWYgThGKW61d209sb654SuJS2LMPwy4kOJ64a2AAbSc--lnWBL4uU4CB3UxZWcCpW2cd_qCFf9Llv4Nu16YCZ69ys5SmI88xGEIVUgV9vkUmg60iUZU4tN3luvVIY4WSVZAneCVPUhK685ynNyDphPxdC8_JJdt33CgG_ryJUg4PQwn7AkD6jZ2z-zy4vqv_sXhK_EJ9kO7qsh0h93mM81E9dNJOEDuS8mJozzmUyyBjW4Iv1VtLk3oxaL7JyEx3_jG4wLjRxGADpP6RjyaDRbohwvepk0DQm1irOXsZtj40xhCJsVyhdqtsxSOZ8VAJY2f8_Q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقی نیست اما مسی با قد 170 سانتی‌متر روی سر آکانجی با قد 186 سانتی‌متر پرید و هد زد.
اینقدر بازی کصشر بوده که باید همچین چیزاییو پوشش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99710" target="_blank">📅 05:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99709" target="_blank">📅 05:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">برید دینی بخونید از این بازی چیزی در نمیاد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99708" target="_blank">📅 05:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99707">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تنها نکته زیبای بازی به جز گل تا اینجا راه رفتنای مسی بوده.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99707" target="_blank">📅 05:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUMv9inryafy9W5i2bTE17MkVUGffOEPHFe_Pu_bDzvgqAr5MvbaIOayxuf2zmd_FUqAdCH-_oUHBLpVZd16uGrQuDTrJIuK3YM5xooPLQR2zDzxAg-ATFriP2JO2UFIpIjczmlZSVLG1rSOWjC0a9y3NB-akN9kYjdSQhsw7hAjVgzB7-rwhxe6gNVo0jm1X0PfQ6g_J02ujUcZEuzRTeQMY_kIcKcooUx_tCnMF80tQAPvEE8Z4zmVNoNwfIkEprkq0iosoxZSByRIBmKf9heOI9Mq8rsjsYnMYrLtm3t47Ccqw_Po1LJKryeZFeRVWtfWoHaYALn2uQldek3l3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
عجب رفاقت قشنگی دارن بلینگهام و هالند
🥂
🎙
ارلینگ هالند: "رئال مادرید و انگلیس خوش شانسن که جوادو دارن چون همه میخوان بلینگهام تو تیمشون باشه. اون یکی از بهترین بازیکنای جهانه."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99706" target="_blank">📅 05:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxwydmdraQ2QOCXPT12cgSbIgbop5k08kHyY4ynoKnhJht9fMu9iguHIO1UFX-pn_vKV0ClTvzHJ6xhzU3a5nl-r1fD8xc9Xo7kD4KqyHJPgZkrW_guaJwumgIE8rTHs-8rKHlzBsucvnhXcm7dpPhn6CwslBQkM3g-CQmGh66OCepyZEFsicuK0g8APF2vkfglrSVf8pVbq94twsSAEOFckG_WlCAhfin9Uh9XN0830cgS4VAkl-iH9vkwv5dhCczlko1fTlVIBapgF-DYsWN-4yDwbaDfdxOuSWdSL4SJMCqm3ihjdiMw1YHaRim0NH7Z_UM-_b4uYygERhbUE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تک به تکی گرفت مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/99705" target="_blank">📅 05:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZbLx3OvlN5nHejFO7UXolnz06PLy5ZEpRoWW1IGzIv741G1p9N3ho9_VgxUjVI23k8Q6b7xYF0emb0kbhgYVuUSi010hM-rQM_JSrlnN2zk0NPLqzbqqIqJmiRwyWhmabPJ2neioIWp0gIr1fcW323zrHUrkGpbp2PEQk5NYR6Y9ITLb86f_QhAYko-iKlR9hPCPwFY6gJ4jib1aOVDEpch9Behod5HbgjMz6tCu-hk0NKRq7NXQ73PmtUDxMBY-SQLtNJsuaE6RKsUZCy1upr3nX2gmDnB0Umsqq0nvm39RAlOIlcYSgoIUkVQ24-57-5MEVk4nJNEiC07yadVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط یکی از شورت هری کین تو بازی امشب همچین عکس شاهکاریو خلق کرده.
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99704" target="_blank">📅 05:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYYCzf7w8HcUrZMkAbEw_eC5vzrY6d14UwpCYV7_IZ1Arqhf3HqxbG1mvhVBMdbmfONqKKGwLfV3Z6fwvyeZf_6YbQwCEyU3ivNUHYJpM2AnP8aWub-Ewv871t_3Sb2JpxzhCQDWYhapx7Dz9h9fnwrLFn8RjmzC75HM5nbp75bRluTugbr79QAeOCDhSId8Hvrzu-E8TNGkRz1W0PxjZhjAViLHWhl6t1JUUEZCL1vK-HGRhsS3wu3WxQJwiMRDBrR5gq-GurbzwU82MxgskA9Xwa3dZzibAgi7qqeUG9C9jvMy0I7k4Fud3v5EUb70yXwzmU02_FCIUlUdZdfL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اولین بازیکن تاریخ که 10 پاس گل در در جام جهانی به ثبت رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99703" target="_blank">📅 04:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99701">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vqt0WMavkwK9va4Bg2AyaLS6WyXzK7MxcoB1ROUcGKk58gwrhT-vO-xNIwj_g7yo1n3t-7aBs92gKl_Z6qb7mVG0J-AT39RYvfwVpYDS9Tjn8-B_JZnz7fx6TMFtv70vRwMu2V-dszSMhrjxMcdJdhC_rnM05TsEmZeGgUUeyq2F0wvSKy75PywxAvMqObjH8jaYaDLDPaK4kjbziweT-m3BYkUVuyZpu5-BEBRTTKI36WbyCnhJLG-XuD6cBb2h_qVXIHsj0KEPdVJB92mnwBlzNk2gzPMKizQigUVo8cdJ4Ey116FGQva6IJoI-Y5B6aa_YCuO8shsr3bTenunXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKOUu1QDnHWoarwHj_MuBGH7tr1N9Lvot14JtfT1ffegpK013EFD4ke3Uipk-Hmfhd0oaCNoKnHoC3-YEiktb3a0eoeIPFiybjjZWiCjaZXGpJd5B8iZL7Fxb--6YxgnO_WweguyljkGjhz9_7yvB6X2FFO7WRPJ7xACsXih0bn3m90C0pDgmWSSh3Qnl6LiDR5VP8Xz__EPgAOtVLLhB-YwMg7UUFsuj1Ht3f5rOJOM3LdNPd3W6i-sS1yUbS2wReySPVD6X4nXOmPpvQVw1Kdmwz-dwNnBWizk7LzBB6qXqLCqR5QIzanrbYUMF4CwQzx4WDOY3mzEszJSmXusbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پاس گل زیبا از لیونل مسیییی
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99701" target="_blank">📅 04:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99700">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf277a998.mp4?token=QrQdA2KxM9n0Lz8bdzGtxzYu37Jo0ju4vhRpxgNv44IkOtdKz5vKQtdQvvjbTZSN-4JKfaiS_tpLvfb_GhJYxiXpCBSLCWIyEkV-QwUsU_FAP8yy5LcX-Isg1i0hPMU-f3x9A9tBQDKURjXQ69Oqc2rh1hMcoSJjkUu9vvzE2zl2BafCHRRvY5UpHqbZH7drOBA13FnosFTp29gDMvd3kXuxBZJ1lowJzjPEZyI1cyrSsaH298j4RwpkDKDv65PjeOCQVCHs5KdW3By5I6qOHRZEYB9PLc4XJFTRP1ZgjkZC_30uR_JAXuJB68QtvbjnYJKTlTKbm_p40qMN9w977A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf277a998.mp4?token=QrQdA2KxM9n0Lz8bdzGtxzYu37Jo0ju4vhRpxgNv44IkOtdKz5vKQtdQvvjbTZSN-4JKfaiS_tpLvfb_GhJYxiXpCBSLCWIyEkV-QwUsU_FAP8yy5LcX-Isg1i0hPMU-f3x9A9tBQDKURjXQ69Oqc2rh1hMcoSJjkUu9vvzE2zl2BafCHRRvY5UpHqbZH7drOBA13FnosFTp29gDMvd3kXuxBZJ1lowJzjPEZyI1cyrSsaH298j4RwpkDKDv65PjeOCQVCHs5KdW3By5I6qOHRZEYB9PLc4XJFTRP1ZgjkZC_30uR_JAXuJB68QtvbjnYJKTlTKbm_p40qMN9w977A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول آرژانتین به سوئیس با پاس گل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99700" target="_blank">📅 04:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پاس گل اسطوره
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99699" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشمام
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99698" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مک آلیستررررررر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99697" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلالللللللللللللللللللللب</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99696" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2U37NoAB3qJvDQJ5Li7_z-T6T4kmk1GOVt0yyBBs9Dt8wEP622rhtdhwyzxAv_d37vYTvM-0UAiKp5dbyGQS-EbVWk_XIbTBXpS5hW0YckUYR4JVWsAHZzrgMjuzCzl87F2ZYPDy_LzTQ9_aICAFyYYA3CNRY7ZhhQ_4m25pEmQE8NCVreuxK5NOQbRoXSwTfvxjPciE7RnTrzjww2KUQjnRevMejSZ52E20iz_wiHAs4KNsqUa02SQXlr1evfTvvWOXtbn52S0FQDFIU-VJMbiQL4PzI6aT2ZTxOohRFDd8fzVoPZoygawHvNWRyfwA2cYDNz0llLwwqX4suorQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید نحس با کیت آرژانتین اومده استادیوم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99695" target="_blank">📅 04:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بریم برا بازی آرژانتین - سوئیس
🔥
🔥</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99694" target="_blank">📅 04:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYEPAJrDc-eyppcsN543OHyRqLc2gAzep-VZeyopmirs7paD5J5KZe_E5KbpQyKqHxx53GD7kmRrgrGW6hkcFVhO1kw-tyiMTCh37O_q3e1HGN6E_Tzih9y3raADFrxJEaVnp4X9d09TLxBoMuVTzh8R9DfxnDznxsErX55QPEQY4D-tPWHx_mjJJhVwqNxB_bpXbAgj_0hlFM_Ft5KdkNQ5t7XJd28HZio7oczu7rbWybLHra7heYhNqxOzYl8lPgPP71Eb1ltMbWr3uGXM_fhHMg7lOUynCCvPk8jALnVNETtq30IZCJLgwJppbombXwFuOqo488uVOkGdg2BQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیم ملی انگلیس اولین تیمی است که توانسته از به ثمر رساندن گل توسط ارلینگ هالند در یک مسابقه بین‌المللی جلوگیری کند. آخرین بازی‌ملی که هالند گل نزد در تاریخ 13 اکتبر 2024 (636 روز پیش) بود
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99693" target="_blank">📅 04:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q12wNumJbLLsDboEvwI3K9dxh-TXVTHl9z14AGghn2qniA2IFpt6zMIZd0qHS60VJuaBzz4LQ4S2idDUDssz3Ryu9sZhNxvSA71RfANOz59B0D9c-PYlolgjXZWVAZd2P08swGZpaAwSH4eDeeJekrQRHbPcINsyYHQftsGo7bWSq8AxhZhjMN9lz94oNfV4C2MWn8Fn6vdveZpHhjoRfsP-gBDj8VZD-3ha8f1PXWSNQ2PTrsGM-cPsmZfk7Q_Qg3RWtMLUHt9FbXsrAN-ZBgP8lRTT4rNwPgQR5DnaQSkSmBK3steiO0St9GfJou96GLmPibOyqQmlcwUtX3ARkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ همینجا با ریدمان سورلوث بازیو جلوی انگلیس باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99692" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1eK9h92X22_u0AWbYqETFRzYrigM05khbKDohnRhaxoGuN03Gy9kMuLBwnLuhFcpe19H0ge_Jz1RIdenhX4cvFmhy_v0D-Q5yM81AU03x-uzZj2QUk_5jypm17czmfL0nNVeE8_7V7zFcwYjey7uL4rumZWqE5NZShknIpZzNDphhtjjaMZPS9MSYArC8457lMJRw2uQuoz7rlKYVNCcGzNjD2GvwH6wHJ6-t9NMULKwDqsGFL7ATJea6NNfITsQt8Rfe05Q1V6iuArNDT79nYsH_wKjic9dn3dMts4g32O0XZ3nD-ANcNlnS3Vw6I5-ujLBMJyk3uTxoT5suqUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اراذل به خط
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99691" target="_blank">📅 04:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nea7yEzeT5T3OgAOWD5VoUjS1zJHBkhK6v1XIHK9rAS7EClN9ANDSxcA0pRueEPA-HGVIgCAgSpEkEwDG2BsHRNevF_LXWU8_yrgdRijRMXbCNRB4Cz4Luv-v9An5BNsGDUPx6oUp8X0Q3SyKOU8B_y6Gg0fUzpiJfV5zAVsqgB__LAefiXzwVd7gIzwZ0uK1P7ecQigUwpz8XR36kCC6yNIQdm00jX3heJoGGq1hij-kmbi-XdfldpkHHMNYIlrrMmw9FNDfAo7JjWRTsUGWFNqDC9GZKw6E4lhuKwfngeuQN7G004Z0nks_zKzkKClZihmyKAPmw8iVIwvceELpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
ارلینگ هالند در اولین حضورش در جام جهانی :
⚽️
7 گل
🔥
یک دبل فوق‌العاده در برابر برزیل
🔺
صعود به مرحله یک‌چهارم نهایی
🔻
نروژ دوست‌داشتنی که برای اولین بار از سال 1998 به جام جهانی صعود کرده بود روی شونه‌های هالند به مرحله یک چهارم‌نهایی رسید و با حضورشون جام‌جهانی برای ما زیباتر از قبل شد
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99690" target="_blank">📅 03:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99688">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_cDQHbGGKH75fqrwC8LKhswYsxEL_OCX5jm9XVn4hvmzm9RGfuJQfetTkoHBYE1k9hrvppLUNB0jHdm-1KepxF4I605ONUrDwsYW96gjZ4KmLSbA7pM_rNeFbiRlMYRbhy-rNdjYokIc91T2YkHklpTXPm8ChokbHq1MAMFoIr-wXzQGwXIgtaKHW_q6Gcxxe2HOq7cyWDTtz5vRUbuOyEXDUwMFnXG7rCaUIOzLz_IX5NsvbbI-PUdZWkFtrtS12cch1HUpLJ5U5lUTukrsn3j9hPIwUraFKmAJMt6j9ZbJDFVYHMR6hSotNI0tvg6VpYdQ9_4f944-AMcoskL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBdL74x5Y_D0NST9ri9ul3da-wlPXl-EJR6RY6wasKD2GwKO7LGXYtfrLDYoi7eMolR3lKvitaQQZBbveIQeoJUVrV7SBEo0Tgnp82d3LcagZlhQhRCYvft4RatsDlHP_vLPGasQyUaXCTctGaJVYROom1DnSODr4s6HQS8eiz3NAA8JY50-U7Lon_pe7KTvPq4vQmnW9vR4LBuP6SAGjGPp2N6bqm_jr0RgKEyshZKnO0IQUyhVBq6qewKSv3oe26JPArElDWYKQLPztWU5Xa26BVbj9rxJHUVehso1nZlAsOlNi52vCCqG9an4ubZ_67309_9gedF_wRYuPpf_KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👏
با اختلاف ایشون دلیل اصلی درخشش جواد در جام‌جهانی هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99688" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c68715520c.mp4?token=SvQDk-CJNA6lGlIE1wlUyxf_q5ojMKR-H8oh3gXxmFeZbgy_Rr5mg0puYJHjadtyU43k36vH6HimT21CIFPMu59kbMmIUnyNDt9dz6lRAqhLyFR5G2Oeo598FuPwdRVFD0bx_9DLpqHiSCMN5NUoEe0v_3kyl6AuPo7WJGa-iJynP0oE9BI5jXnTB3_y9ksCuj2C7hwH-CH8jnZi80GcS8ao_wF6AS6OSq3A30RWvNxJ1TN-pKaWQh77sCn_QIDWr1RFTZ2RyNsroGwln589cloAfzTU3cINmXNEK_WU7j9bJMp6tsNEIhu8ymCEBEYm0o9dMtKPX7BArQXal0WCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c68715520c.mp4?token=SvQDk-CJNA6lGlIE1wlUyxf_q5ojMKR-H8oh3gXxmFeZbgy_Rr5mg0puYJHjadtyU43k36vH6HimT21CIFPMu59kbMmIUnyNDt9dz6lRAqhLyFR5G2Oeo598FuPwdRVFD0bx_9DLpqHiSCMN5NUoEe0v_3kyl6AuPo7WJGa-iJynP0oE9BI5jXnTB3_y9ksCuj2C7hwH-CH8jnZi80GcS8ao_wF6AS6OSq3A30RWvNxJ1TN-pKaWQh77sCn_QIDWr1RFTZ2RyNsroGwln589cloAfzTU3cINmXNEK_WU7j9bJMp6tsNEIhu8ymCEBEYm0o9dMtKPX7BArQXal0WCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو منتسب به تهران؛ تایید یا تکذیب نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99687" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXdD6ygahE6ooCpNOhfz2UmAQ602J3_N6tsHOsJ7ExCHT8LaElAT7ogdj72jKsOtX3wehJVg3og655oC_N1mVyvms-QDnvFVfV-LeKCBivPXJgBUhsj5FQHwq6J2VzHkh245NJiY7UFSFdDMp8AysaF9KTSbPqcwm8NwDgt0TWMhUnDrv3Ai2OwjrOg83YmZdw3Y8yOtEcPimA2E2LlUKyoJIrarq4tsVp5kCbhTPByVFG2qOVffv_SB3O6DU3yPmQPUByPAp5Od6QpzmMLPN3cspioLa9oqXlecD--PnT5muAm3-RM10ptxh1rAOlGtq3jDTJy390M-jlHrj_6Rmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
تیم ملی انگلیس در این جام جهانی 13 گل به ثمر رسانده است. 12 گل از این 13 گل توسط هری کین یا جود بلینگهام به ثمر رسیده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99686" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwuIcM11HbkFib9ojpm4C4wrmf5N21yi439SGAmpCKtXQ32gurd62DKad_MSj4erOyQzDsgKZCCoYHJjPtAaUJ4SSyeQfFSmX6UoJx7KUrK_2meQNw--v5ZKYRcdK9MHUWYnmqHJQzLV6k3r9jDItW1nJS_3Z4yeov66ZGQGV7ZYIhaJnedskCPEWiCsgOz0M54hhc_etGvctSYpqoL34WOLIC5shi-xz5d3PlUNlXuY5agrgZWZ_kZ7CGnDrTnEScdCCGcpF92KaCVHChuqPUYeyzXCVJ3AepUTlC2aYkaXwA5nAk5WWRjVlHljUIWiI800ThikXLW17wcrKhUItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
جود بلینگهام با تیم ملی انگلیس:
🔥
[54] مسابقه
؛
[12] گل
؛
[8] پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99685" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0eDzObQtPGTaDJLY0s0f-CfcUUFZ59p7a-KTE_eZe7r90vCgv8XhppLgoq2w6W0_K6ZGNJ1d-pL1Oy6DLPq0Z7EM5-LjWAICsTu2uEb06mCR8C8XoUOwfWbNXoKZazS-TdGLA208kBTKXcX9jhKM0SXLruz1w8N7c22E52cVxDU3bntSVqab3xTsJgRR-gsaFIkqAhlCXq2rox3kexxY9JZFqAr6Pm8nkc104vtQElPcV9AZPCtvmvdQBDAJ4qzTYSy04ImAWlbyGEdHiVcA_1L7fhcLSK6tZHbITNjdlgUX2HxilKjnRLcRhPf3lxK8LBl5c6CLg7SqdcCU3mHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام، اولین بازیکنی در تاریخ تیم ملی انگلیس است که در یک دوره از جام جهانی، 6 گل یا بیشتر به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99683" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
