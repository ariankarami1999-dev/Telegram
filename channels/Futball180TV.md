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
<img src="https://cdn5.telesco.pe/file/g_T0J-9oMiFcHbOwG-iYQulyaeUCybY1nE82xIt_tUkMj_r4eHzPazEr5xgPkYhn1JLFqjMeDo9Eh0n-sw_E8QlSzveSa2Pilm6Q3sCLlNv7CJbh6s5TkOWCOWhefuJ2nwET6MnhNfxLvikj61SWjECDsYynS1wrBcJeDCzUCTkBDsAWC3DUO3m24YubEyb3Q066zMIL2_O_n1rWI8xieTMgkIc9s44oIihAJ2Xqvp-TSWpTr-avHQsbrHoJ-832feQcRYHdUMwANZvLsIeQ6yFPRCaLEc-q68gypUo8-L1LniEHwREvxG1i2rYRoh2RkYa2FUvuHyba1_UNo-JG0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 417K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-106276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
دلیل جدایی هانی رامبد از هادی چوپان: اون مثل برادر بزرگترم بود ولی یه زمانی از من خواست پشت جمهوری اسلامی نباشم که من قبول نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/Futball180TV/106276" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkdtYwK23yGjgok9GeJpU2rYRHV0U8ZERIeiQKsS6OpPLZII4kAFXfRg9fgGBipBMK_DxBYnvJ9zsuOor3A_SxW1MNUWLbyyOTJd3peKBHg-sG78eLGShfgrAyfuRmFrluCi2AFg9Je-EloejLMhJxQs67UMSWvn8RcxWbtel27sO1ek1PoBQs2Egx8ySCG0rn78GaFk7rAJ-0p16a7bedqPsuzYi49zDJ8HHjpjSubQkCsUCQqJKJ4eAmwIr6VNVt4xYNze2hs45i73dlWHA4A55Rz46rzdx47wzx_tc1M_el6D8vTi-2Ck63oApL74eybPzEo3QuDyRZ6OqPxrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لواندوفسکی و دی‌پائول که درگیری‌شان در هفته‌اخیر جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/106275" target="_blank">📅 14:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4SuPig6yK8t3LszTfZMWGmiQ8bO-Ac0Qxh9ycVwPjGVb1QvHIGjgkqME4cgSDfbWTRBa2Gsd8owFQ6NZ9QLoDZNQ1dVLek3_k6Zay1Y8qG8aVGYkGdlnfBNEqpNQF5fOmz0206Aje6G1oqkTVQRtxmEGhi5-kqI-2e31sVEEys2sn5f02Obxjz4kk5UDMm31mzMJmPBUFTpWkYs8lN5NRv3wiIYxzzcvjGt2rNY4KJGXgdGs2Y3xaoTNiAIaENSaIhAiUU827cxzMnFnhSdymNB1VGkXhBjgPAIC-upq7KYLd0754cK5U_Jz13eGqLjzQrqWe3piQ_J6wMo1K_JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
درخواست تاجرنیا از هواداران عراقی برای حمایت از استقلال در بازی مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/106274" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمود فکری: سهراب بختیاری‌زاده از دست صالح حردانی حالش بد شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/106273" target="_blank">📅 13:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFpeiqMFsZn1Q6zKBcKGqV_HpdP4St75VNstKAP77OsGYuIW2a3eRf4xGILiCT5OvdArEM4gU2O574zyDx9kHom3J-LD8_FHMcfPwGlgoPm9sn8L22vvHvlHWw5r3jq8BhyItKu-Tx38qK6Z1tpMQgtWjChiofYV1CXmnNUamDGU1hRBjUDPBUVb2JxhjOGMUxVeyPlmDthmeJgms763A_8dFR7ltMIN4xRfbL0Ligly3qWMRb8RrI5Plx_3o2SDTuwNhC6sIpkJF4LMCobuMgtXUKnSyVeTaMk0lud6BiOmimmRnUT7ANdnBpOzopPTqVaX94cY8XUh0cQ_KbBgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان‌امباپه: اگر عدالتی وجود داشته باشه بدون‌شک توپ‌طلا امسال باید به من برسه. درسته جام باشگاهی نبردم اما در جام‌جهانی تاریخ‌سازی کردم و این جایزه هم برای عناوین فردی هست نه صرفا تیمی. پس مطمئن باشید به خودم رای خواهم داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/106272" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_LYZMWXQOJ0mTG_13JQDUpK4DXOS_NZsV7I1fKY8cWViyD0jqitdmQwRSP_Zw_g8ygLtIh0KHBUe9d5-d5zS7ngncV1Dhisihm_5M4FNQNR_fTu4sAG8ZUlhKhjMbkOWGzU7Je-GWEkU2vMneN-Q80wUjwpj_bLXit1-ysCf-bbNyt1Bb66smnW24t0rb4s6bhfSvOY-71M_NYi7xAfpt9KR0EIogCAxmjZbUgjepZe0iLpkzCoGtVM5NjuBhyySO7sPA63wIodNCqaGzWbuxCgPYYsU2Ar716-5n5VqRRvckTkMs7L7s-9dtrpTk84lQP_XudrtS9v9eIDNUPj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
با رایزنی صورت گرفته مشکل پرواز استقلال به بصره حل شد و کاروان آبی‌ها تا ساعاتی دیگر عازم این شهر میشوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106271" target="_blank">📅 12:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
پاسخ جواد نکونام به سرمربی پرسپولیس!
جواد نکونام سرمربی تیم تراکتور در پاسخ به صحبتهای مهدی تارتار در کنفرانس مطبوعاتی پس از بازی با استقلال خوزستان صحبت کرد و گفت که «آنها از آب گل آلود ماهی گرفتند!» تارتار هفته گذشته خواستار برخورد شدید با خداداد عزیزی شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106270" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106269">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106269" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106268">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVUqGpsYK3zxLRfP0wqJspvY_pcf7Ud_RmUNzlYVA_cXHky69Mt-WFuNROfUpROEya4e0HsD2vXL4Lqp_arG6-agbDBmSuC3mvCcAZajVv1K2srYPn8WldU-VAtrk2iSn9WQ7fhVABElX6rGoDdYgVccfsK1UnUJE6ZsG_UVigE_37lszFLWzjmZTw02PNF20qYyaoIn4Gjhl5aELBrblr2fzWG42kGQwfsAwLTMgiJhogk2v2iRZ7Jjn8kwViNa9OyLKGByHVOCZY0csIWSwRe6oFXCvToqgDggiPhlsDT1OHAHlwNos98eSEDztRTub9qchrQ-RVJ9hJV0RN1xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106268" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106267">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/106267" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=eSU2raGGBXmp4JM7UizmkqUK_yNwoA_mF1hshvktUpo0MdWJZYgK2n7L248xJGg4n2STfdeaxBf23mtJzl-v4h7x5mhihCw807VHhXed_frdParEh6x5AMxySpREFssqPma4AC8Ok-aDqZSIgUS5ul796UXTEDRaAFuMSHY5wyr7paF9JMO8ihZZEOdyQudvWg-V9ADNxRHssMx7t4txBHv4o9FdC5mjQZX_WQhG6IUChFZ8XC3VNNm75GfZ0mgdQ70vw7TAnNeOEZaVp_jl7Z2Hu19uumYx4rDuhPofF36d0WLWRwxAhKLHnBprG-P6VDRy6QEMHnkEFUIWlGKeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=eSU2raGGBXmp4JM7UizmkqUK_yNwoA_mF1hshvktUpo0MdWJZYgK2n7L248xJGg4n2STfdeaxBf23mtJzl-v4h7x5mhihCw807VHhXed_frdParEh6x5AMxySpREFssqPma4AC8Ok-aDqZSIgUS5ul796UXTEDRaAFuMSHY5wyr7paF9JMO8ihZZEOdyQudvWg-V9ADNxRHssMx7t4txBHv4o9FdC5mjQZX_WQhG6IUChFZ8XC3VNNm75GfZ0mgdQ70vw7TAnNeOEZaVp_jl7Z2Hu19uumYx4rDuhPofF36d0WLWRwxAhKLHnBprG-P6VDRy6QEMHnkEFUIWlGKeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/106266" target="_blank">📅 11:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=KKtk7BK7bGkDg8gEwyBgWZ-8cQeI9wV4Pzk9yEgzc1qX_Ok7-pmypnaoxPyqJobDjk4d4noXsgNriWSC1AZ6e9XL04sHVJR0VTjsNwPKf1wKrCpaqYqxteD7mxmOa-0lgZ8_6y4LvkuqmzCOel_tsDsZ-6bA-85V1GlwwkF71YVO5Gho0_Bn14K01NYf8y8z7NS4LDIXxJVHDC0ucKArcPDqQQgV9c7Pj3-o7apypZ7Im4TVNCyPesKfz3_y17c2zPTRRywvdCYEwdxl52yge4l4AZ-L8mQpdXiUPxozfjqjSWdQphZLPULQKK6xcfDzBfD9jgXy9isGDe7j4MTG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=KKtk7BK7bGkDg8gEwyBgWZ-8cQeI9wV4Pzk9yEgzc1qX_Ok7-pmypnaoxPyqJobDjk4d4noXsgNriWSC1AZ6e9XL04sHVJR0VTjsNwPKf1wKrCpaqYqxteD7mxmOa-0lgZ8_6y4LvkuqmzCOel_tsDsZ-6bA-85V1GlwwkF71YVO5Gho0_Bn14K01NYf8y8z7NS4LDIXxJVHDC0ucKArcPDqQQgV9c7Pj3-o7apypZ7Im4TVNCyPesKfz3_y17c2zPTRRywvdCYEwdxl52yge4l4AZ-L8mQpdXiUPxozfjqjSWdQphZLPULQKK6xcfDzBfD9jgXy9isGDe7j4MTG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
🇪🇺
🇪🇸
کارشناس چمپیونزلیگ: امسال نوبت بارساست که قهرمان این مسابقات بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106265" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=kEu56XLGng-xda74qWs6uz5-ALx4l7EIExM8VQMZJBtD7mc3TNyj3RA2-lqmVj7vJGnVOy1A3IU7p97vpFCVsz7Edr_ehoNV6D0YGw-G5mtjIiOIrepFxZl3B3PiUWmXtP6wgBZvle8ZMN3vW-ghkfj3E0zHV0_GV461sYkFziJjO3F95Yhjw0zAOU6hvY_aTUK5y1TQwo5lVYoPQcx_9jUczjocub_e3wuCnwc_d_94g7Cj7gBcnpzJIo1q8vOo6rC-68AnOF5Tsz4oj-Xr_XjSC5qIAtOJFZ9K6eSZM03PLSGqgfAEkAwxE8rX3-NNEN8POIUb71pAFtRBZIZRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=kEu56XLGng-xda74qWs6uz5-ALx4l7EIExM8VQMZJBtD7mc3TNyj3RA2-lqmVj7vJGnVOy1A3IU7p97vpFCVsz7Edr_ehoNV6D0YGw-G5mtjIiOIrepFxZl3B3PiUWmXtP6wgBZvle8ZMN3vW-ghkfj3E0zHV0_GV461sYkFziJjO3F95Yhjw0zAOU6hvY_aTUK5y1TQwo5lVYoPQcx_9jUczjocub_e3wuCnwc_d_94g7Cj7gBcnpzJIo1q8vOo6rC-68AnOF5Tsz4oj-Xr_XjSC5qIAtOJFZ9K6eSZM03PLSGqgfAEkAwxE8rX3-NNEN8POIUb71pAFtRBZIZRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هیچوقت این دوراهی سخت فراموش نمیشه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106264" target="_blank">📅 11:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106263">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=bVWBAhYi7a3nPzi3ZsujCz4mMg4ILFzMJo5o8b8ERxyM95NwSlPZz15yrJ7ES7CHnbLBwf_HEOuDl6NtImaCu_ItmLXGYkqdkw0vn9AGP0cxW1CtE0zDxsenR2q-4RP8LtGUOKzKmb_OOaq1BZ34oi7_CGHwjo0erlT-g5HdNvAnj__TOCrnGYEUn2QmEaxlDIvcEzXpwAfdcUqcxEnDUqKMZe2Yu7NNT-HF8jDG6r9yVBofzHm_ScYyGQca0N81vYZfugq16FNthax5K5S0St-e1GY0KhSfGzqhsouz0qupqC43BKZnZaKhKgvjM6aVLWn4E4giEEdjaWy74pLFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=bVWBAhYi7a3nPzi3ZsujCz4mMg4ILFzMJo5o8b8ERxyM95NwSlPZz15yrJ7ES7CHnbLBwf_HEOuDl6NtImaCu_ItmLXGYkqdkw0vn9AGP0cxW1CtE0zDxsenR2q-4RP8LtGUOKzKmb_OOaq1BZ34oi7_CGHwjo0erlT-g5HdNvAnj__TOCrnGYEUn2QmEaxlDIvcEzXpwAfdcUqcxEnDUqKMZe2Yu7NNT-HF8jDG6r9yVBofzHm_ScYyGQca0N81vYZfugq16FNthax5K5S0St-e1GY0KhSfGzqhsouz0qupqC43BKZnZaKhKgvjM6aVLWn4E4giEEdjaWy74pLFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اعتراف جیمی کرگر به اشتباهش درباره لیساندرو مارتینز مدافع منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106263" target="_blank">📅 10:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=EbvR1WWjlt4nRzOt6Y_-kxPJt10PrJqvUgqg0S5ZuMKxdFqFIAopKpvR4QwrLTemtHZ54mz4qiHNUZVk_IjRgIWSa7PXzmYVfnA76pF1LO6N5WWEds0UqAJCnAEmmdazI2Iyv1UcTSRW5DlBB40q9-7SZ47Xc9ZNvJQ2HqL0qNe71vzwFrbY7p-KD5mrHk08Wqqt2Wrm-6OPgCfZaJebOsIQePL_UkEyPkNy2nriiOu8377XDvDWp_8-1xw84Fu2C6JvffKVuo5pNQBGeDxqdxfrSXM8O9CWUfePXvz30FBhWGKK1RkAI3rn8zdoTBtGL5GT5DI4_A0pEhDU9jjkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=EbvR1WWjlt4nRzOt6Y_-kxPJt10PrJqvUgqg0S5ZuMKxdFqFIAopKpvR4QwrLTemtHZ54mz4qiHNUZVk_IjRgIWSa7PXzmYVfnA76pF1LO6N5WWEds0UqAJCnAEmmdazI2Iyv1UcTSRW5DlBB40q9-7SZ47Xc9ZNvJQ2HqL0qNe71vzwFrbY7p-KD5mrHk08Wqqt2Wrm-6OPgCfZaJebOsIQePL_UkEyPkNy2nriiOu8377XDvDWp_8-1xw84Fu2C6JvffKVuo5pNQBGeDxqdxfrSXM8O9CWUfePXvz30FBhWGKK1RkAI3rn8zdoTBtGL5GT5DI4_A0pEhDU9jjkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
جدیدا تو صداوسیما دیدن که مخاطب زیادی ندارن دیگه خیلی احساس راحتی میکنن
🎙
مهمون شبکه دو: زیر کونشون میزاشتن
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106262" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106261">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106261" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31134b7828.mp4?token=Fq8dcJYsfwKiFGVgCKxHoAtL-W3NmwxuMVyuUtVfRAp-MarHXIMpFcL8E8XBLXqtv_-her0DlPz3YLPEXRO0JdphHnPsFwZIxyQH4o65w070gdKwZNhqwwr2pDc1AJ_OI0TaY5yFIxX9CUOieoLtQ1OxtPKA9S5OiLqsPYdtzXAqBuNOT6UclIayoNca9ox6xpWnJ_alZtiVshq036euu-V0SOFkYyYzDCJfeYFgCQR1HCBP9yUTvkB768DYyW3ep98KmLlOVLMoD8ZnO7w-zrvrxAWZtliWd9wRlU8y73Krb3p1AlDfsTBCo-dTN7U6glnJkgiX9PP9Hzb1Pb3R-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31134b7828.mp4?token=Fq8dcJYsfwKiFGVgCKxHoAtL-W3NmwxuMVyuUtVfRAp-MarHXIMpFcL8E8XBLXqtv_-her0DlPz3YLPEXRO0JdphHnPsFwZIxyQH4o65w070gdKwZNhqwwr2pDc1AJ_OI0TaY5yFIxX9CUOieoLtQ1OxtPKA9S5OiLqsPYdtzXAqBuNOT6UclIayoNca9ox6xpWnJ_alZtiVshq036euu-V0SOFkYyYzDCJfeYFgCQR1HCBP9yUTvkB768DYyW3ep98KmLlOVLMoD8ZnO7w-zrvrxAWZtliWd9wRlU8y73Krb3p1AlDfsTBCo-dTN7U6glnJkgiX9PP9Hzb1Pb3R-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇹
اولین‌حضور کومو دوست‌داشتنی در UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106260" target="_blank">📅 09:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=pdtx2KZ0aPzSkyJAC-sgEiShv-7vUYSUUCbXDOh9HqnE3hWrwFGAKJNRuKPPdj6np_495iU4UlvTsMBbm-XrnQUAAL5le5dzCQGU8psZVOwVuTz0IaAF9ztmr0qxd1SnWHnAx6EYTF6fuBYAqzNa4pkbPAYjM103_IWx36zsIUS9uFmoC1dUH8mHw5EkRzl9DMErYOEZKysRuikfpM_9ZH-E2Ilu1W10Pv4DyGRP9Yk9CUa71y8Ezj0lOBGCbCGmPRCxC6J4c3RDvellxgxIbUsYchWUJP39eToy2lj6oXLvFaYtdmcl-BFzaqGVz1BnrvC3tSz38N7jYjY_X70a6hzR5OHpg9_QOVqRLxalDVJoTXvrZDsJ-vA24OyOhodxtX9_6BsFm5cvoWqDa_jHz37Xi--e5mMZmpMLbNT0Os0diFhSJ8vN5rw1Ta_5HK7lHAtBBVz1gwk3ybZs6BgflqnrmIyRItGnuuHKaDO3LMKyebndNZ7FnqwqeJVgGSMgcEBUZ6m8KBJZO0u7Nie6dm2biCl9roUCPJsdnzWMR9jizeSF8S2JsDLLcfgsRptZkNN_AOaLbaHPSjEHxhao5_ws01T6hKqxvdxbghxPPZOWz91DoMddZgybA6ad2dZbFNN0KJNtjz9SMvwgM0GzFAhRfV0QzRLcpfB-LJJ_Sms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=pdtx2KZ0aPzSkyJAC-sgEiShv-7vUYSUUCbXDOh9HqnE3hWrwFGAKJNRuKPPdj6np_495iU4UlvTsMBbm-XrnQUAAL5le5dzCQGU8psZVOwVuTz0IaAF9ztmr0qxd1SnWHnAx6EYTF6fuBYAqzNa4pkbPAYjM103_IWx36zsIUS9uFmoC1dUH8mHw5EkRzl9DMErYOEZKysRuikfpM_9ZH-E2Ilu1W10Pv4DyGRP9Yk9CUa71y8Ezj0lOBGCbCGmPRCxC6J4c3RDvellxgxIbUsYchWUJP39eToy2lj6oXLvFaYtdmcl-BFzaqGVz1BnrvC3tSz38N7jYjY_X70a6hzR5OHpg9_QOVqRLxalDVJoTXvrZDsJ-vA24OyOhodxtX9_6BsFm5cvoWqDa_jHz37Xi--e5mMZmpMLbNT0Os0diFhSJ8vN5rw1Ta_5HK7lHAtBBVz1gwk3ybZs6BgflqnrmIyRItGnuuHKaDO3LMKyebndNZ7FnqwqeJVgGSMgcEBUZ6m8KBJZO0u7Nie6dm2biCl9roUCPJsdnzWMR9jizeSF8S2JsDLLcfgsRptZkNN_AOaLbaHPSjEHxhao5_ws01T6hKqxvdxbghxPPZOWz91DoMddZgybA6ad2dZbFNN0KJNtjz9SMvwgM0GzFAhRfV0QzRLcpfB-LJJ_Sms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
عملکرد درخشان اولیسه مقابل بودگلیمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106259" target="_blank">📅 09:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=Or28nh3MmCTLvES-kdNcfSmK8wEZMHNiG2Dhrt-NDwLcwROcpPBcausjWukr0yukTOLmuUmccp4v1Kn-DIG_56NYZdspUv8NMGDJQnnR2bMBbePZwOEItQw2F3n5n2Ovu0SCg4gWQp4uH7UEhGny2BPSW08NIyqkHZ25qgG2u4fMPo53s_5iEdUfdyspvFtLYNkkZRyc5-LF5mz1QwvvyoC0Cw4wzWVz2OzhkrD27Rp1nXE-Y85kjOlBh4Vi7V5BOqxw_tDmJp-kcZXPk87ooan5SWa3-G5NPa-P-hbNHsL7Tj2WeUSQ62RQ-_-dAD4O3ol0duEPy9kvTOg4q3KmPm4iDVLsB-K9kUbmEbHPAsECDKK00hlt8l0fzhH2MJyR3WuT46QkUW36ec_ZSwWnOaW8b9u8CA-wj6DP-K2pS0PhwegHRls26H_Ia6u3n--CpaOCD9JadsJaW1owew4iexnIAycCbA0H8S4wYjKYkqa3agNV0CM-SnXLzILPUH1DgnhSBSsFyZddbjwUbWiZ3zu_fGadPuUUI1GkyE0cnZHr9AqYVj_pfJuFWHbHCnX3ZKOY1FVK_FcI5qzB5Y5c8Xn_ppbeBtNxbeAWcpADnaXK3CAESKmRqGT8nVujyL-tpZD7Uy5Q-35YEMQH9NwRsgdkoZxNCRUVFAYF04gm7bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=Or28nh3MmCTLvES-kdNcfSmK8wEZMHNiG2Dhrt-NDwLcwROcpPBcausjWukr0yukTOLmuUmccp4v1Kn-DIG_56NYZdspUv8NMGDJQnnR2bMBbePZwOEItQw2F3n5n2Ovu0SCg4gWQp4uH7UEhGny2BPSW08NIyqkHZ25qgG2u4fMPo53s_5iEdUfdyspvFtLYNkkZRyc5-LF5mz1QwvvyoC0Cw4wzWVz2OzhkrD27Rp1nXE-Y85kjOlBh4Vi7V5BOqxw_tDmJp-kcZXPk87ooan5SWa3-G5NPa-P-hbNHsL7Tj2WeUSQ62RQ-_-dAD4O3ol0duEPy9kvTOg4q3KmPm4iDVLsB-K9kUbmEbHPAsECDKK00hlt8l0fzhH2MJyR3WuT46QkUW36ec_ZSwWnOaW8b9u8CA-wj6DP-K2pS0PhwegHRls26H_Ia6u3n--CpaOCD9JadsJaW1owew4iexnIAycCbA0H8S4wYjKYkqa3agNV0CM-SnXLzILPUH1DgnhSBSsFyZddbjwUbWiZ3zu_fGadPuUUI1GkyE0cnZHr9AqYVj_pfJuFWHbHCnX3ZKOY1FVK_FcI5qzB5Y5c8Xn_ppbeBtNxbeAWcpADnaXK3CAESKmRqGT8nVujyL-tpZD7Uy5Q-35YEMQH9NwRsgdkoZxNCRUVFAYF04gm7bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
داستان جالب منیجر ایرانی مسعود اوزیل؛ مهدی کیا: پدر مسعود اوزیل باعث پایان فوتبالش شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106258" target="_blank">📅 09:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106257" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHXr-DNmb26V-Frol3AQFWFPu9f_KodnRLbWr_mo1WJ8Zd_ZdoZw0JrHdqWzuVe9fQB8hRtdgsP8b1kDUhWiZVwq6qJM4D8zKipfEPugcktMnq0LiPJVUUeLltsqo507847VGwkBIaXt0sZtGNHRRWWIlzYu2IvSnwYppLX5yWVfqRha7liCk8jM4bRUCNAafGiVPxQaCVQeZ4-VYc7IkSIhjFn57zEwJYToHEwIAM0yZn0fmuvoZTrGOno-qWC7aFC-jgkUL1EvlNQa1AgpDtheRNMUuh3p3MPheufZ1qDqSyD-g6wU5bN0IZIeoK2vcDAsFN2Y9Ij569_RrZIJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106256" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106255" target="_blank">📅 01:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPG734juzKSpOoYgSL2FYxZOzYNpRjnD4pVZ5eQGVZOvFFW2FDrzDTGZDCY9s62z-hb2kzxpWM-TvSS9Znv-LpmocwmTyn-8iVdrG3j3z4w09WC63uuf8k6ZJfuNjAJVQuSI7jbx0g_WuUcULUUggBKz-z5ldy1SgbH4rrPEloSCEMn_EEgF-eW8mmUl2LNXNtqLmpTDIxDhLuUY-Rmx9OKSFahSSMLkk9q1KDmeLwcL7XwhJ3Vug_v-5xgV8CMrZXvZbAcYVBunhK9qNXvtAmHu0BpWjfkFsBR7_AhWBBgBlIswF4N4NpGgO5lOuFjC3a7NG-eOUGKwudQq6-Gilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
✅
🚨
کیلیان‌امباپه:
🔻
من سال‌هاست که خودم را بهترین بازیکن جهان می‌دانم اما اگر در مراسمی توپ‌طلا به مسی یا رونالدو می‌رسید، اصلا ناراحت نمی‌شدم چون می‌دانستم آنها چه بازیکنانی هستند. اما درباره سایر بازیکنان و کسب جوایز کمی تعجب میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106254" target="_blank">📅 01:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egB80Nhyh4qciCZbQqyfqu07irIi6uyWILRdpCqCXidhhGA2KzqL4CAJqVwtq-Y7Z8p2hk1v7abSkLWgNYmC6-EjMtbmOZhcfn1JeKS3MuO563aUaivdjTP-rGeyLoI0V7ZgMeqRKWZPaQSNGj8a5tXFxGp6jmmT9xYQTilqFBtBu7bKK_m1scNAANK_-xxHmfJseNStOZjfox06FdX6NU33UayqmlkGIUfClE0ZU5T5XI1pkOfBB4glvpRvKxBiDTv5w9Q7gHZ4YUKOotkM86OeztnILQDAZd4j5O6pp5-i3Z2seDZ04Q1dH4HGBNF0aeoXUI22eE809EX4alN83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:  اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106253" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwlCufMp5r9NEjGnD_baXlRt9FmYmziJtkJyrny7d59Cd5YuAViYPJJig9cPHgyHo1hVcZQ_pFtYotQ00fZWfzsNarzK58NdUei-I90MFnRQxFTR2Kt3WtEIYJFm4_2B7cGMqNvGFT8Ni5nHjdNl5_ntbnFrsOWiBN5tFlwQwnAdbI0Gfb1-oZ9L6LHMgFouCT0uyS4O2JmJQ8CATlsDfFG9f2fd-uuobEtJUTB4GKRpOuGxQwq9_7oXsmOwbLX5oPm3RT5C2ntJtWp_Bb305zaUya-3OOGXgdlLA9vdLq2xCqptE4i9oTGn-FKwzSlOW_qPcztnB6KoVX8680GfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:
اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.
🔻
او نیازی به فکر کردن در این مورد ندارد، چون هنوز می‌تواند این کار را انجام دهد. ضمن اینکه، مسی خودش یک بازیکن فوق‌العاده‌ خاص است.
🔻
من خودم را یک بازیکن متفاوت می‌دانم. اما او هم یک بازیکن متفاوت، در بین نسل‌های مختلف بازیکنان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106252" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAq1h7WKBtXOjfoTGrEHERbEkrrYSTLxYuG7FxzMhMzP5liVs76_EVvJ204775MKs19FAGnUBUhYjqhhYIcF-QqjxCA4u0MaiyUQA4tZyl8c7KbWPP7KqLBnEntc_wgslL5WisojyJBKfXMTlw669ZKruD0iyduf-rcfQ3imOjDIiw21gEE3Ebcj2nkAoGarF_3Bx_WV6tn8aP0gdWBrIbA6ZD97plceB1tbFGsGaXAW6IchLMjYMFaWhYXyAlAb-NcGeK_yhWK4ABtaSwZSA5aE8Lf8ZNCOE_yUaViNDqKLv9tHiSRYp2MO73ZikEq27Fb626BwW22UbeGOB0__xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
📱
استوری ابوطالب‌حسینی: ما نبودیم دیگه تو فوتبال حاشیه نبود و همه پاها موازی بود دیگه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106251" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=ol59WqiYzSSF0MGUNBrht6gUSvo9OkAiSQJ22b9XyIPJ9jE1LCPJ9Vy2-4BxVdvoid7Y-w2WIBM9d67jFY8AdPe1lyqz6pG3FSWyUFyx1n0zom_N4bDAWwQeKf_eAnxMSDcUBZs86jcD1xGGVU054hnfgYSbxeYXRKpBxT9FSheOiQ_j_z625NqD4IjoDdLOqSv0h-6jy5Ye2VvQ74uw3Ll9oZB_9etVoziwk6t87VNaIhal9D4Y8u0bPQ99pI42id3dKIVU90LlcX58NWu76p3tbKphBdP_rrb6KIV5ZX8LQMfmxcJ8q2pt4l2y9hLOyWpjZgSh8PURJyK69MaScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=ol59WqiYzSSF0MGUNBrht6gUSvo9OkAiSQJ22b9XyIPJ9jE1LCPJ9Vy2-4BxVdvoid7Y-w2WIBM9d67jFY8AdPe1lyqz6pG3FSWyUFyx1n0zom_N4bDAWwQeKf_eAnxMSDcUBZs86jcD1xGGVU054hnfgYSbxeYXRKpBxT9FSheOiQ_j_z625NqD4IjoDdLOqSv0h-6jy5Ye2VvQ74uw3Ll9oZB_9etVoziwk6t87VNaIhal9D4Y8u0bPQ99pI42id3dKIVU90LlcX58NWu76p3tbKphBdP_rrb6KIV5ZX8LQMfmxcJ8q2pt4l2y9hLOyWpjZgSh8PURJyK69MaScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز بازی استقلال و پیکان توسط تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106250" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki6c9qgAj0H2rpDsdJEHeXPxgEbNjYmf93wwkSsCKbtmbOZbIwMczr9WwwDhQuOfW-e_cCxzJEDXFH46CW82v1_iYadEWmRLpkwob89I2q1NJM7nPVIVJCUbCJ512B2P8sJT-drjtCpIvjDCqPslp2QZTp4l7wOQZJJl3ABfZ3wGZuSzLMaUGG7feCeYMWE-VDG-zRBqr8s6zfqIStLUKfDIddLw7Mn880pLL_9PMTL1s8PXGrEwzVvVqJiRNK1YR1EupmD4HFhfMQp-lzeqqkRKqVm_mpEcGjc0NNdriVeXOZBrL1T9izMLwxfsnCf1dCWwFJ0AJm0dultlX8guvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106249" target="_blank">📅 23:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOuwTmJzYe4rzbVQlspnKHvt-sMB8QQh9sqXOgu8HDr9LB-0uwJxcUPsTg_tckpHBedbyB2KioIL_GarM5oeeTJnH_MISRBL0lqrTmY1amK6AL7kJhHM1scB-cDg1i_Ja6g_2SX6N_qCdux_lGU2kh_YnqhRQUdpV0enGMK9DZRLC5OjKwYpHCBAGgNnV0J_GMmf1RFibX6g-fEmDQYF1VAlWf31mjZd0h9kK8-_Nip6tqanbCoaM5GASXrE-1ox-W-M-Ozo_R1YMwnxsque-fneDx1Nfl7Dbn1xVIJqoeemWFSBFJaw4-XlHzTxZlpvThPJB7jRpWbYXOlbqV6n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106248" target="_blank">📅 23:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های تند وحید هاشمیان به حدادی:
🔻
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106247" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمد تقوی، درباره پیروزی استقلال برابر پیکان در هفته هفتم لیگ برتر گفت: «استقلال نمایش خوبی در این بازی نداشت اما باید این بازی را می‌برد. خط دفاعی استقلال آشفته است و با این شرایط در بازی‌های آسیایی مشکل بزرگی خواهند داشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106246" target="_blank">📅 23:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7gnFuQ-Sk8LLZ6bIRTebgTHzEcxOVBw8PQt4Yb7QcjkG1L84jxPzJXta_iLQdUmpDQ2xpX0IZ2XIp0DPa9rAgh58RVJYc0wbE4T9d2u7_eEzA15DgHw4MEWKqoaHu8MrbDaJhUygT3rKQvzHXwJ3agIJWVzwNSClWjfwjizBOI5_hGUD6IjGfD8nhZ6gf01kHZ8T9iuopJeHJatX1r_5_5KCXCdB3BXWMIcKAgHW2d4M0U-G5EEsjhv8apPHacbHrnzdq13_J7Mg8rfEr9Jk8AlzTvohb8Vchnoijn2Gaxkp6ha4FzMtYXGwm-0iWyNvTHI8t2kGmMx_W5aKYvT40VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7gnFuQ-Sk8LLZ6bIRTebgTHzEcxOVBw8PQt4Yb7QcjkG1L84jxPzJXta_iLQdUmpDQ2xpX0IZ2XIp0DPa9rAgh58RVJYc0wbE4T9d2u7_eEzA15DgHw4MEWKqoaHu8MrbDaJhUygT3rKQvzHXwJ3agIJWVzwNSClWjfwjizBOI5_hGUD6IjGfD8nhZ6gf01kHZ8T9iuopJeHJatX1r_5_5KCXCdB3BXWMIcKAgHW2d4M0U-G5EEsjhv8apPHacbHrnzdq13_J7Mg8rfEr9Jk8AlzTvohb8Vchnoijn2Gaxkp6ha4FzMtYXGwm-0iWyNvTHI8t2kGmMx_W5aKYvT40VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
کامنت‌ هواداران پرسپولیس زیر پست‌های السد: قرارداد آسانی غیرقانونی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106245" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=YEllYRrhSxkfTvqb8sDuwHkCulTrk_JpUc7M_CNaQpYuUpnZ_zXQwRGdLu0I2_BG8ZphLIfCMi7lVOdETr1QA6i7My55Mmy9Puv2aHbFehMFD2FgCrS2bQw3WE1ackHswetZK7h2W4O_0EN7SV6nl_NW9vUCqa7KT84EWWvCNMloKDOmDD2k0jBFUL2q9jldCnPWIvyXqJQrX2ADpvh91c3BpXd27imZ0oOpeonzqtpUa0UJOGyCYEcj1j0BTYZqVPXVuNsX1HBibfQ_qDmb-fwAulHz_bnxPlC-VN7xLHxK9VHeaCZWZNBc8tBO3jZn5Jri3M20WEiTFhdUmKTbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=YEllYRrhSxkfTvqb8sDuwHkCulTrk_JpUc7M_CNaQpYuUpnZ_zXQwRGdLu0I2_BG8ZphLIfCMi7lVOdETr1QA6i7My55Mmy9Puv2aHbFehMFD2FgCrS2bQw3WE1ackHswetZK7h2W4O_0EN7SV6nl_NW9vUCqa7KT84EWWvCNMloKDOmDD2k0jBFUL2q9jldCnPWIvyXqJQrX2ADpvh91c3BpXd27imZ0oOpeonzqtpUa0UJOGyCYEcj1j0BTYZqVPXVuNsX1HBibfQ_qDmb-fwAulHz_bnxPlC-VN7xLHxK9VHeaCZWZNBc8tBO3jZn5Jri3M20WEiTFhdUmKTbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سعید فتاحی رئیس سازمان فوتبال استقلال: به غیر از خلیفه و گودرزی در نیم فصل هربازیکنی سهراب بختیاری زاده بخواهد باشگاه استقلال جذب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106244" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=SSLESN-LdGJZbbPhJbgP_gRuoUpknf8W-m2g2KrVWKUbPwC77eU36-8m796iEByY6ZPB23ZfbBY7hxEgrLmwXXP8ay4YNnGLPt-OoISMwkN8rjxZpAobN2C29xrKo55lkHMJrISJ0JfB3XW2284sOvaAEGde15tJeiiIr4NX8ZuCzYwVnkRFQqKKtFX_sHleo4XMPGT6yu0Uz2GCXyhe55GqfFSA18cqthRMg6cIcNVIm3bHKuiardgHIMK0v4WthwWh6XmSTsPdUtEpah9jTgoon-PNiQ8OAgz5lICBjWE9PJM-XqOZw_hAneyzve1-vGwNM6u-y0wHdfFDEJg_Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=SSLESN-LdGJZbbPhJbgP_gRuoUpknf8W-m2g2KrVWKUbPwC77eU36-8m796iEByY6ZPB23ZfbBY7hxEgrLmwXXP8ay4YNnGLPt-OoISMwkN8rjxZpAobN2C29xrKo55lkHMJrISJ0JfB3XW2284sOvaAEGde15tJeiiIr4NX8ZuCzYwVnkRFQqKKtFX_sHleo4XMPGT6yu0Uz2GCXyhe55GqfFSA18cqthRMg6cIcNVIm3bHKuiardgHIMK0v4WthwWh6XmSTsPdUtEpah9jTgoon-PNiQ8OAgz5lICBjWE9PJM-XqOZw_hAneyzve1-vGwNM6u-y0wHdfFDEJg_Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
نادر محمدی منجنیق: به صورت اتفاقی این نوع پرتاب رو یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106243" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=e9N57IRG-Y_8Mh0sfkfvfZC47_WuQGVOF5ef7Jowk4QIM0UFQRzks-I0pEnXi6thSS_W_xPd19A4GcA4z5y5bEN9GdM_PNWIQm_buCSLwPubXPZ6j_gVoW8DUZDt-m_jzX-xU_N4eLM_gVjAQWGEgKZL3XsW_Gyo9OhD6eF0LuIkPC7gJvj1K6G4etCJ6MfvUYG0V6YbJqTZIB0KlwK3TvF7oU5YB-o_WZOR1LDgbWh9Oo3gH5-YZX7WJmnyFtjBE6WG_uxY3Tiwsts6lxVyCAUyl3VZ48y4UhUeRxnTHKVyAIHxdNAf09d3xTQOqVfZtmXZtNNQ50wWhzw6U7ThGliFEx0Yf_rBNYLdthJILhi7lUG1JNYppXgC-RE0u5l1elwZIkD3tfYerii6X4etGGPAlA_ilRQHd2Aa0QxyQ7jDh048PtQUZl8Vv2ZtTQbLOhFMS458DcEpQbiHcaFFwXiI_to94SjkwCb6B-XdXbfKo3RrsdXYK-5QVvvbAotUvdOsMEvLB_6MFaKrVoyEote5ZUGgRYnr3ZJ2p6KggigGzxFeFDLMjse23_avhsNgC28E4RZ8SjN7MncMyuJgwMG4LDGUBhuHRwL6XIqKCZ0UmFPBkXo-y8wLKOfJz3f4C1ltCZmFtQ34Y8AYAlyqi6o0MBST0_VND23Z8dHe7Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=e9N57IRG-Y_8Mh0sfkfvfZC47_WuQGVOF5ef7Jowk4QIM0UFQRzks-I0pEnXi6thSS_W_xPd19A4GcA4z5y5bEN9GdM_PNWIQm_buCSLwPubXPZ6j_gVoW8DUZDt-m_jzX-xU_N4eLM_gVjAQWGEgKZL3XsW_Gyo9OhD6eF0LuIkPC7gJvj1K6G4etCJ6MfvUYG0V6YbJqTZIB0KlwK3TvF7oU5YB-o_WZOR1LDgbWh9Oo3gH5-YZX7WJmnyFtjBE6WG_uxY3Tiwsts6lxVyCAUyl3VZ48y4UhUeRxnTHKVyAIHxdNAf09d3xTQOqVfZtmXZtNNQ50wWhzw6U7ThGliFEx0Yf_rBNYLdthJILhi7lUG1JNYppXgC-RE0u5l1elwZIkD3tfYerii6X4etGGPAlA_ilRQHd2Aa0QxyQ7jDh048PtQUZl8Vv2ZtTQbLOhFMS458DcEpQbiHcaFFwXiI_to94SjkwCb6B-XdXbfKo3RrsdXYK-5QVvvbAotUvdOsMEvLB_6MFaKrVoyEote5ZUGgRYnr3ZJ2p6KggigGzxFeFDLMjse23_avhsNgC28E4RZ8SjN7MncMyuJgwMG4LDGUBhuHRwL6XIqKCZ0UmFPBkXo-y8wLKOfJz3f4C1ltCZmFtQ34Y8AYAlyqi6o0MBST0_VND23Z8dHe7Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
🇺🇲
بررسی حادثه ۱۱ سپتامبر از این زاویه؛ برای دوستانی که اطلاعات کمی دارن دیدنش توصیه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106241" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106240">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=VQICLhFztAjowQkj7UKIpq6aywK0g6PfHax4ZT12WMYYzYADOVJ9Pr9wVLfv2t1YYOopt4FUa_l2M0SEtw7r1yxHhXoPb-oJ0QaUzefOyYmRgla02hniPhyCoK-tUbBNmCirpPi9WavJPItbpoImCQfL2nByXFOIcOiqYpqEOVVIKBtTokoUpzlNPvEVUtLVEXShGsIhrBY6cNavqFY62SuJdwggUgVPLMzXhMg6g4hgyEVXGMI6Syc-VoORFvcfAzaQbGVLe6S7xf_se13EHh399R5ynqrroJW0f2eSmJYs4dW5jOQiBxy38d9PD-es7FskA5qSjK3Jp3mlAuPIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106240" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106239">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=KvG8a5am65pd2UCvYTpPlUc422jnBaG_LqYH_yO6n0beJihLmhlNTWA7MZofVGuG5LeMI2DX92j85jzE6N7EerQbP_i1i-xb5RrJl6ziSqeP14pxBb7bf0_qaIVSpDEA4OQ8KVuAWcp4jg6Nrw9tr4pGdICXx8L4srSvyHsoenV3tpUnEg9N1A8q2ESpMmD8xypXJRzvoltF75NwDM0n8VNSN37Qvza5dxFX9-U41OwRZdM5TddCnPeLdnTvaNGZmduZbb43rmqJy4ewwMVdiDdD-nAMvnegHQJsHHVp0-Qtpa3oSqDwyNdGVx3R2DqRqs-kJjLTwlbx__wMC1WHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=KvG8a5am65pd2UCvYTpPlUc422jnBaG_LqYH_yO6n0beJihLmhlNTWA7MZofVGuG5LeMI2DX92j85jzE6N7EerQbP_i1i-xb5RrJl6ziSqeP14pxBb7bf0_qaIVSpDEA4OQ8KVuAWcp4jg6Nrw9tr4pGdICXx8L4srSvyHsoenV3tpUnEg9N1A8q2ESpMmD8xypXJRzvoltF75NwDM0n8VNSN37Qvza5dxFX9-U41OwRZdM5TddCnPeLdnTvaNGZmduZbb43rmqJy4ewwMVdiDdD-nAMvnegHQJsHHVp0-Qtpa3oSqDwyNdGVx3R2DqRqs-kJjLTwlbx__wMC1WHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس:  2 تیم ( استقلال و تراکتور) با تیم ملی امید همکاری نکردند و بازیکن ندادند چرا کمیته انضباطی با آنها برخورد نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106239" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a557a62450.mp4?token=H5yg1GtssXxTE8IRdM-JUA7Y71WTd1uhhzbvQhToahtNK07KHTdaSpVob01CIKf4VfduVZjK-4oxa9sDTrKthbUETMz8e0UzjsG554OjvhZ1hiqcHBgZYBPMPBjYrQK2Dh_3ZFOgzBafRYON_xEIJbUkvuDk7a0UDmWxUR_kh2k2vL60Arbm37XNtYIkGXRuq_WIKHg5A2LOOaJKwtxIuHeZRzThyPYIvFdgYzur22d36rEYyIuQJgexbDnMDmj6ebvuiOPWKQGMtq80G1bXMLEJXcqRlu7ACM4g5Cr4XZwnGW-LwDKu0HS3onQXavXebdV33R-DAOFYS_R5I8aYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a557a62450.mp4?token=H5yg1GtssXxTE8IRdM-JUA7Y71WTd1uhhzbvQhToahtNK07KHTdaSpVob01CIKf4VfduVZjK-4oxa9sDTrKthbUETMz8e0UzjsG554OjvhZ1hiqcHBgZYBPMPBjYrQK2Dh_3ZFOgzBafRYON_xEIJbUkvuDk7a0UDmWxUR_kh2k2vL60Arbm37XNtYIkGXRuq_WIKHg5A2LOOaJKwtxIuHeZRzThyPYIvFdgYzur22d36rEYyIuQJgexbDnMDmj6ebvuiOPWKQGMtq80G1bXMLEJXcqRlu7ACM4g5Cr4XZwnGW-LwDKu0HS3onQXavXebdV33R-DAOFYS_R5I8aYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم دیشب در لیگ قهرمانان چه خبر بوده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106238" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtq6rKVsXQGTGqE1S09Svb4-TzQNWQefROmVCkDXaboczIXHn37fvqnYgN0fD-6LmX3Ept4iPUHXqowbO1qKaS7iB9JFLV8SVKVUw2ynoD_Oz6TtzJ_zPBKE6DcDf8Wsvj_eo5-zCv3UrL2YnVaIbyVfwCIMwvt-UkN4riA_l9CA5P344n1jauGG81Z64RdnNEbXM30VPuqdeNLDDOLjFZm_xKBO6QfmdHn2CIQP1Q67we1oKwsiMbm5AkXin8Qy7VsD_bOure9MGsQJhRqjBOzj0EnVzPlYoH8el88EfTNudsnrjpe4K56Kg8YL1VwV9PZxM4C1ffSzxf_1OCRieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇹
🇪🇸
سسک فابرگاس، سرمربی کومو:
🔻
«بارسلونا ترسناک شده. سطحی که تیم در حال حاضر داره واقعا ترسناکه. بازی دیشب رو دیدم. فاینورد تیم خیلی خوبیه، ولی بارسلونا کاری می‌کنه که حریف ضعیف به نظر برسه، چون در هر لحظه راه‌حل پیدا می‌کنن.»
🔻
«می‌تونی مقابلشون نفر به نفر دفاع کنی؛ همون‌طور که فاینورد سعی کرد این کار رو مقابل رودری یا پدری انجام بده، اما بارسا از هر نقطه‌ای راه‌حل پیدا می‌کنه. فرقی نمی‌کنه چه بازیکنی وارد زمین بشه؛ سطح تیم همچنان خیلی بالاست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106237" target="_blank">📅 21:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525ed46310.mp4?token=BnPvImjLhsRH2wmLlBgOL-adYIQbLDF-3Ro2rFCTWc51YTeGKuaLOCzMpAiVt1K9doi42DKT0ohM7l22QbLSG6mReS1rd0UpqBpcfUPXm7mFkpQpPvU1mSxj6W7dFjSWRAil2CbJ8rCaU7Im-za-FTuBkzruNjYFHcrMl42ELU8C040ypMumekAaDr2jeLlsKGKtJ2B1VDTWCbpoiAHMd2fjJcRFYPhRXg6Z4ETubOBGhe7j0LADhj5rSWPb49FpCuQtLw-ncIeHHMOrv5gaq2WYLi2p0CM2K5AWfuxklipL3Hxza291FVZwA6xa_cUjGwYAd_PvqCH2dzSP08PQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525ed46310.mp4?token=BnPvImjLhsRH2wmLlBgOL-adYIQbLDF-3Ro2rFCTWc51YTeGKuaLOCzMpAiVt1K9doi42DKT0ohM7l22QbLSG6mReS1rd0UpqBpcfUPXm7mFkpQpPvU1mSxj6W7dFjSWRAil2CbJ8rCaU7Im-za-FTuBkzruNjYFHcrMl42ELU8C040ypMumekAaDr2jeLlsKGKtJ2B1VDTWCbpoiAHMd2fjJcRFYPhRXg6Z4ETubOBGhe7j0LADhj5rSWPb49FpCuQtLw-ncIeHHMOrv5gaq2WYLi2p0CM2K5AWfuxklipL3Hxza291FVZwA6xa_cUjGwYAd_PvqCH2dzSP08PQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
اینارو از کجا پیدا می‌کنن
😂
- کارشناس صداوسیما می‌گوید ذخایر طلای بانک مرکزی ایران ۵۰۰ میلیون تن است!
یک ۵۰۰ میلیون تن و یک ۸۰۰ میلیون تن دیگه هم گفت تازه
😂
حالا جالبه بدونید که کل طلای کشف شده توسط بشر در طول تاریخ ۲۲۲ هزار تن بوده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106236" target="_blank">📅 20:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106235">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=ZWriskzAXy_1DRrewILDzEJNqHoFo1AB3ingdbxU6FjCQrnMENm4QvZmSRH192s6hjozuJURbXsP2dEg1eD4lvgcpVfKOBD4xl3ENPX9qNlRdHe7aijQHHhbfU5gUCQWQA-UOXgWwO36HDpSTdprLq-lyUxb_hlycdyNdCGOgg6OIz9cJhnqGc5MkxyIdonMjMEaweMf6IRnJOnuv3L2pSx6CA9lg6VMoKuijONOHUA7COsjxLKnk32M8nuN-1XBA7xLODMhbdWHvCzxUOvMPmMRQB9Q3V97gNUII8j8AXqeDcLGabrzW6TUzIQR7ypL36OEgilMF8UVLXxORHptTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=ZWriskzAXy_1DRrewILDzEJNqHoFo1AB3ingdbxU6FjCQrnMENm4QvZmSRH192s6hjozuJURbXsP2dEg1eD4lvgcpVfKOBD4xl3ENPX9qNlRdHe7aijQHHhbfU5gUCQWQA-UOXgWwO36HDpSTdprLq-lyUxb_hlycdyNdCGOgg6OIz9cJhnqGc5MkxyIdonMjMEaweMf6IRnJOnuv3L2pSx6CA9lg6VMoKuijONOHUA7COsjxLKnk32M8nuN-1XBA7xLODMhbdWHvCzxUOvMPmMRQB9Q3V97gNUII8j8AXqeDcLGabrzW6TUzIQR7ypL36OEgilMF8UVLXxORHptTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
فراز کمالوند سرمربی خیبر: الان که پرسپولیسی‌ها مخالف هستند 3 ماه پیش هم که پرسپولیس اصرار داشت تورنمنت 3 جانبه برگزار شود همه مخالف بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106235" target="_blank">📅 20:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106234">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmFtdxztLJKPir9DKFgBliy8PK7tGUEixPp8E6lUemmq3YzTQ3fFoT3tGR_4qxEx8DqBZU3apm5KpMd8TgzHQAhbVgY1YxfNp3_lgbRcNXLn0CvRolX3l-vD4fksGpeqr7-W2iEIDnHbVM7l8rYxUJ2ygCRmufu62Grj5N8q5mn6sHYjZmywbvlf1xjfO3U1NPx6VMtsL4xHJKc43OTP1O1ywWnc0R_WkpjjV9DahwCYDpDbO5ZkIOFI7b6SZ-PKo4JM-uYm6okK4HZW4k3D-GVPMR2pp-sqrZDwchoGFaA0WodTAawkC4nHSO2_kUxzuiQ3ww2VaL0w9Sr3Ny4ktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین‌ماهینی عزیز و همسرش
✅
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106234" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=R_SBVVIsqdyUzYIfjUCL0kMBm2pIdIT-_sKbBQ72oUK5PjjH0BKw39onV_1hu44JX59ZW1OrsGXwwIMRACARXU7w6QFmvWyxmU-XeSkdOFTxJZeoZTCuG0m4U6ibtGmTeAlrjZnD81GjYNS_eQk-hkl3pwznxHKeL64CumbWtDvI9ydVQPrWUVu5qDgJ2dO_UkJpZuaH4pKDHwCYs_Y1o8fjfTNcfafJiBQ-o8vUYMZNpyIfqEMi4U00FoOzf04tjjDX9gsRF0fcxyz9J-t_u5yK2n2AClWIGzwLn99_m4iVdVR2tvC5-TL-eCUAfImwVNutiP8DvR24NtX8Y0YlGyLqPjGcX8820DM6uGwN3hCTrA2NfMx76Nihem-MDMI8ZB4j-v78mFNHXtD06Ljr9yFXpa0Mg7syfDN72cYk6vormEXeNu6nfikNZJLSofD_IeRhWf6TAf6K9Zb-uGfyrxTbFSU2HFpesUBwggN1hajpILsBSGfo7jgeVkjYRBg6Vp6lMiCUDymw8a5HjxoiLpfMygMQl3vMVwItcuWZs59IJMIxd9Xmd8wKkCFb070AEy-smMzgj_9ZCoVXm232va4rO_q99YP8W4X9qd-6ZGqZV8uMFeNT0p0-CKiboR1ulHYtao3OWNuRa8G4W2w01PgFQY0JOxXA_RT62wYD0bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=R_SBVVIsqdyUzYIfjUCL0kMBm2pIdIT-_sKbBQ72oUK5PjjH0BKw39onV_1hu44JX59ZW1OrsGXwwIMRACARXU7w6QFmvWyxmU-XeSkdOFTxJZeoZTCuG0m4U6ibtGmTeAlrjZnD81GjYNS_eQk-hkl3pwznxHKeL64CumbWtDvI9ydVQPrWUVu5qDgJ2dO_UkJpZuaH4pKDHwCYs_Y1o8fjfTNcfafJiBQ-o8vUYMZNpyIfqEMi4U00FoOzf04tjjDX9gsRF0fcxyz9J-t_u5yK2n2AClWIGzwLn99_m4iVdVR2tvC5-TL-eCUAfImwVNutiP8DvR24NtX8Y0YlGyLqPjGcX8820DM6uGwN3hCTrA2NfMx76Nihem-MDMI8ZB4j-v78mFNHXtD06Ljr9yFXpa0Mg7syfDN72cYk6vormEXeNu6nfikNZJLSofD_IeRhWf6TAf6K9Zb-uGfyrxTbFSU2HFpesUBwggN1hajpILsBSGfo7jgeVkjYRBg6Vp6lMiCUDymw8a5HjxoiLpfMygMQl3vMVwItcuWZs59IJMIxd9Xmd8wKkCFb070AEy-smMzgj_9ZCoVXm232va4rO_q99YP8W4X9qd-6ZGqZV8uMFeNT0p0-CKiboR1ulHYtao3OWNuRa8G4W2w01PgFQY0JOxXA_RT62wYD0bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
آشتی جالب هواداران نساجی با مجتبی حسینی سرمربی تیمشون بعد از فحاشی اخیر به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106233" target="_blank">📅 19:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gp6gJhtgz1OVdwwFt22Gx7hepGogV7dM6JAGOEYyLQ5tqUChXWrXaelAMh3SMuLki_IRN8uOyZ0typ68fUCk1McKNrzLEq4wqmjromWC1CSpuuFleBJoUkShm2A86s-qiIMrHFaZxv-1KrWTecNRVWmENI-ksYC2DuECxXfM_rD5BJGWgZDZcme-2vP5pFasWxmya3qvBI96lytHRcGmLBpgNuDfx7DHwi_5IhRpyAZnijQHrcMUXa-ZPlRdwwzJwacQR7UM0wW1PGlL0stiJ-QHj7_Dmixtdkqv-ePxANFQdi2KbtN57o15NBpT0q9VyT01iRdsLqAilt2LfNtZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🇮🇷
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها برای ایران در راه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106232" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URm56nhe7ooyqOZbhauxqi5Mc-cGW8Ayj9PCf1-p3w2ZSJ4m3ROj8Oa3gph1c-GMc6MK9i6hyaWiSl8__Cdl9VzzEFiha6--WkksYahMCQjjnTGlHLJfKJau-ZvlOksl9b0RcFoCoDzXaVQ_hKhD189AH0AhGWBJlEibRcd8kfGOstJfvQdn4cgKnPYbgKgfkV9gp1DDo63NrF_kQsjy51rMAKid263y-lCmE34xqc4Jg_GR_82ogwmhgHC2_Ge8n8OKGGAYgbL5wyYytZBVnDX7uOEQQIBGkyAWvCG827Y9L8UixdWI16wnV8hriYIcIEkLKeXXS5zSCNyCJZrH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJEJ_5LpyraOn7FouifJ8BNnuXgHTnUyOx6gJIgk-4-wjRi20VLO3gWVVaVq-PP8_y8fur-G4VfcETC4gSRcWnGSVD8xJxg-k6ysvria9mrvGc461TOnjfxEEr4uSYewYTFHXnOQcCfYCGlcRXCPogl3pahLHeCgNRlHJEutaN0ydRjxBZskrb_tUBPoPdm1f_Jxo52O2yMGUQYQW0g613lHerba_UBJa9ST6-EqWnZa_Jcl1nYLdhMChjoFpO1VYHnVaNJ2_FUTlKiW1IZuwmI-ldIdNlc4SdqKUVWt7btQ4YsEc_z1lII_r9mx4JEERln3x1OvrP2bDPvTPguEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VliDEZCNJZXcgt5wC_bpFUo72XloO4sOwIHDSq74PULqnRY1-PPeiuckX7MqBcVe4Ti-a-1CEdcjE7ECdwzXt1qwg9BcUTEteos4B6qjmDBOrnRRwsppgpKiHAWcD-7NGIrjZLxx1xGNZwP2QQ-c02aiW003wTSTOoYYuHFp8wRIgd6HeqhlTueny8R_gY1WFePNvQHsmJhCTXAuHV_GRfDaCUlWPzLd3LgDTWamp3sNEUL-YMt2ZW63ibWZx1LRKmegoF7d8-I_h_maAzOe6B5lsdFsjS0yAQaYy9kQ4iCWTh-WEN6E7dL3BRSSqmwKkUPnaNcT1VFV_UL7kkaEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2YLmWotD85HHpPyghyeHUl2U7sRkYAevwbU4S5LG6_HZaFz2dySck2ZbjExxy8m3ol_gwaeihPywi78JSZWhtLmU7v__HbeK-Uc11H4W5Q01WGva-P-map65V4rvXpYUc5rLJzvHpvDIo605QNdR3rHQQyj1rv95x8IUeySoJkBm_k5pnMjqyiUfdc2nkM2i6K6S6B-q4zgV_SHrsFxd7Wv3_AxULVxPI69idXUgItWpCr8U3ip2r0LuHK8ANGE7cHTVlM2GnN7MUTQaC5-PR6wqSNYwyfcNoxnqUQoxqInfaDQcxaM_bVQ1VHewbNfOIy4BoKz3sRoZj3Sihnw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8jduY8N4wIVfp_Co9301ycYNCYHDp0ztMsGvOxIjTl_0FLD72mCmdjtDVd0sYerhs6snw7qPetsS5iX_Ge9m3lNI3o_6hn7CR6oC2UsJA6fXGNQPnxY6C0p3aSOFeunpm915Ze9EcbLEM_y5UVKuhJp7Fl4favTwAXq51YvBx_T73m-sVCpKSLsz-lYPa2_Dz1I2PJ8izfsJ9G8b_P4r5usKwr-fwNfhAP6DwW308-7VplgHbGC21xG7fqsJJcS_zW2XhLoX9RH9jnPR77Ljs7_xYfi130OwPChKZyF0Q7it7SPjRGC9lIj4nGQWhYTaBSxe8r45xWhU8CIjuwBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
واکنش مجتبی‌پوربخش و علیرضا مرزبان به تصویر تلخ دستفروشی یک‌دختر خردسال در استادیوم اراک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106220" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ANU2-kyxp-oxUVoGEpntamnWrdqSZok76D2u92h84R8oo09qa92TSZVXDj1TfpWrl3ccTiepWGTE-tljB2Ii_Cnz0zPYvsRoxW3EZ8bqi7f4S4MSUInSdrKhLz7QfzhDxLciOOdonpenZSnJIGJus6RccERcnUU3SE3HAqrvN0lCQpx1FUoHcL8qoD_lELA-barf-pQVeYabE2vMgeW0qv_Xm5mC7S1Q8bhM_kQeQ3mrzkCeWzuV7Rh6JfhS87UkDqsG_jnC2S5Fq8bkc7t_6WRYUUR-yqMjyfi8tXTkQassd4jbdWIf_R219TTVSs6k5-povPXWiiLaIUvCqLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
📊
🏆
سوفا اسکور: مقایسه میانگین نمره رافینیا با نامزدهای توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106219" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kth7B57sV-h_kMvnKBBJ6ghtlqmcPeHc9BLQW2dZmn224572_yK0NiGol_RMVYzFal6hP3GvfHNrsubnVCtHEaT-wBJzyA3uvY5yPsundCwM-d2LW8w-bXMF1LxyP3MzievyX6bEj6Envc0ZQDQIoYH7yr1E8v6JhOvanJSmb9ecH5VAcZ6_dMvCEc7P_v7w3g_-ti8Y0n3UqC4aPFVNNccSJeIS39VpaLRzokS8I8rsKyu6t5qszLhyRk7uzH2h-eVy-Sd32Uf8SpzUAEhfKRuVIikUzad-_6Y3CMXbAiykP2YWr5z5nmV6H3EGtBkKMKWwZZu0ckc8KSKIPLnW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
امار و ارقام لامین یامال در کریرش
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106218" target="_blank">📅 15:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از مالیدن روی آنتن‌زنده و صحبت از قناعت تا عروسی سوپرلاکچری سامان گوران مجری صداوسیما
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106217" target="_blank">📅 15:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
حس‌واقعی هنر در ایام‌قبل از انقلاب با حضور ستارگانی نظیر بانو گوگوش...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106216" target="_blank">📅 14:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDyzkyGXuhwcHma2DJtNcPBLPBiuCfCXBm6_99weEKvTXwCzbKYoeOsBza5LjtPG2f-kSY5afgxqLYW37REtX7GWC9BKOx__npA2LiNsdNHdgvnVPkvpklTrNFLevL3aUy3tumXwgkNdZqASINx-6KD1dJUicibNL9UCHQ2JOekCQ9_mU0cXE69XtfTouuIBO0zq9e35g3-OhbYIecgQyBQelPCIG-jQ35xPbcYYKMCsuzs1dqD-8qvH_l5NwiQtXV81qgikbWEbHi10OvGCgHG1byWUucpuRLknu2pvSEgrn3ahXRhD-ADOMMCKmBc9DFIEn7oPA-AgskU5IhemYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
عملکرد فوق‌العاده رافینیا از شروع‌فصل:
🇪🇸
الچه
⚽️
⚽️
🔴
🇪🇸
بیلبائو
⚽️
🇪🇸
رایووایکانو
⚽️
⚽️
🇪🇸
والنسیا
⚽️
🇳🇱
فاینورد
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106215" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=l8FUBDqpDwMIDRxzX1mGb1PhgF3NNaspclQfpCJWVusNRXQQjkTIFAaAzN1Lp1lsApbCYlJveZ1IH9BT4q-zdsMJ4o6Yl4wkSctrVTmIHn8R6a9M6nA44f6sVld1aLIovSiyYTMxSYD3GJT8m8N5IN_sUCwWAZNSSY4NPb1kxGRsNcFQfSqwHcOdSnKNGSUo7Q4MjQcjBr7uLreFRSU7cfSxb_KWLJrK6xUeJWccnatoRGNQ-bo3l9_vVGRQkO5b_P8yz9CumU9LS2XZwZz-LNwgfnk4MFyxlz4crPrHgTAH6oAFpf7wAWg7TFYEa6FakbBjmmQ9L8hC_LAdnZMiwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=l8FUBDqpDwMIDRxzX1mGb1PhgF3NNaspclQfpCJWVusNRXQQjkTIFAaAzN1Lp1lsApbCYlJveZ1IH9BT4q-zdsMJ4o6Yl4wkSctrVTmIHn8R6a9M6nA44f6sVld1aLIovSiyYTMxSYD3GJT8m8N5IN_sUCwWAZNSSY4NPb1kxGRsNcFQfSqwHcOdSnKNGSUo7Q4MjQcjBr7uLreFRSU7cfSxb_KWLJrK6xUeJWccnatoRGNQ-bo3l9_vVGRQkO5b_P8yz9CumU9LS2XZwZz-LNwgfnk4MFyxlz4crPrHgTAH6oAFpf7wAWg7TFYEa6FakbBjmmQ9L8hC_LAdnZMiwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمین یا بلینگام؟‌ کی بهتره؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106214" target="_blank">📅 14:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovU_wK9IumiG-O3eMZvjdQnZ_3h39HXcwg6kdgNGrTtFY1FsKDXyKWZEItidPagsto7zxyVr3zx6XzW3yfQgVWiv_75kl6vyiPkdIqBKghwkNyTfiY_nFwYNARJncNSKSC2bIQ3wikOfb7TQdYrxsneyYQHW0G9ugM2qu9edrcw4KCHAu1-3s7hbsXjZEHKNF3lOJf0cWZgOdIkSUgYgSMDXwW4xdrjia820ZbVxzZfTmlhyyCzwWbV3j841mnB-QEEEqkOqgjlo1d7ohTsnbPZOrIw1ZMi1aqVpMkkNDekp-9NtL5sYTraN2KTon4gR-97K5ZYxbFIyHDZeXZrOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد درخشان مورگان راجرز در چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106213" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=Zy83TIpLB096e3_g3lZJRCoWhn-p8DBW-C3mk8Myzl7W8fKit8FPl2ri-N3xMCJ8B7HpHjg5FvebK_fZF0zzJM_MjfT6C4Dc4rxC8bhwpW8CtNSfDv3z5WgMmp5jlNVZ3sjHRM6xbfmaSygvn1YL5XuP939xixLrRweJ6zwNvtnYfFYrNbB8dTWEPWqByuDScOARfbavs-t12RmN67t4v-DXuyQwPiNqi792nkeGvn_UrAopeSjezdUQrw-SDpJGVYoiPUlq30T_BwOYn1dXH0eKf1682ptYgwH9QAhU2HF4oX9KsGFFmu1mrtbTaeLSXEG_yvi7VNKcIY0we2rytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=Zy83TIpLB096e3_g3lZJRCoWhn-p8DBW-C3mk8Myzl7W8fKit8FPl2ri-N3xMCJ8B7HpHjg5FvebK_fZF0zzJM_MjfT6C4Dc4rxC8bhwpW8CtNSfDv3z5WgMmp5jlNVZ3sjHRM6xbfmaSygvn1YL5XuP939xixLrRweJ6zwNvtnYfFYrNbB8dTWEPWqByuDScOARfbavs-t12RmN67t4v-DXuyQwPiNqi792nkeGvn_UrAopeSjezdUQrw-SDpJGVYoiPUlq30T_BwOYn1dXH0eKf1682ptYgwH9QAhU2HF4oX9KsGFFmu1mrtbTaeLSXEG_yvi7VNKcIY0we2rytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ویدیوی وایرال شده از تجمعات شبانه:
«تو تاریکی می‌شینیم، ذلت نمی‌پذیریم
بنزین رو کم میگیریم، ذلت نمی‌پذیریم
دلاری گوشت میگیریم، ذلت نمی‌پذیریم
مهریه کم میگیریم، ذلت نمی پذیریم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106212" target="_blank">📅 13:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=RScCpgF79zysThRiZRUPSQ5uFeO3RFl2ae8qCOi3gg3QAxxI5BtgtmaMt12j4LSGeN6dEjzPJ5ron5qUS-R2FB8KSztBGJoavXXxu7gzARni3mm7L4QOo_4_Ng7R1F1vDq_YtMBw456XWrmFz-0NbVlzlRtvIPBBCpVz8lFAQLb3PG2DkLPEOiA4SDGY1N72pZn59VvYBR-CNeVW1oyB2viNDntWnmwaUbkoYXWEeBQUgIJf1ErHCHTYaq6jZze5QNn5pgmbrZlXVeLjwjvGYCqvWyOD4tthEwoPdfo2AbQG664YS153Mnc7qQLer5RblvEOtFU-7d9rfwdqLyDyHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=RScCpgF79zysThRiZRUPSQ5uFeO3RFl2ae8qCOi3gg3QAxxI5BtgtmaMt12j4LSGeN6dEjzPJ5ron5qUS-R2FB8KSztBGJoavXXxu7gzARni3mm7L4QOo_4_Ng7R1F1vDq_YtMBw456XWrmFz-0NbVlzlRtvIPBBCpVz8lFAQLb3PG2DkLPEOiA4SDGY1N72pZn59VvYBR-CNeVW1oyB2viNDntWnmwaUbkoYXWEeBQUgIJf1ErHCHTYaq6jZze5QNn5pgmbrZlXVeLjwjvGYCqvWyOD4tthEwoPdfo2AbQG664YS153Mnc7qQLer5RblvEOtFU-7d9rfwdqLyDyHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106211" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106210" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1pRaHGpw58qkmxlFtTnFi8bEK9rY57cHEO9rJosq6KQ1r6JtC-jPbDK1TJkiLSdvvrO0YhdJKq0ZAk0hcU1Il3IuFIB0PL_PAiEgMdjEVSRKbcllLgBtbl5p8t08s6EeV-FRrDJr7rhVA8QgNhFGuXnELOCrCFChf-iTEPde3-Ah0ZtdVdr1HFSRWeC--i2r3dXKC5OEdL6ahgFw1ApP5qmmbeGYjD0RptEFtd3a_CqmzCse_KtxOKxn4PrExKmdD3WvlXQm1Wvxl9_YK8DVhVawYXFZRFhQugs9IJykcYdviHjn6jHw-H0HU_U6vx3gGP9BsIFHDwWdofr8Kd0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106209" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106207">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👀
🎙
🇹🇷
اسماعیل کارتال: بمولا از ۵ تا بازی اخیر تنها یکی باختم اونم جلو بشیکتاش بوده. تو پلی‌آف اروپا هم لیون رو بردم و به مرحله گروهی رسیدیم. نمیدونم مردم دیگه از یه سرمربی چی میخوان. دهنم سرویس شده و قصد استعفا دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106207" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46400b9012.mp4?token=bFzY4cPY_gtQDcu6oy2_nSdC4p0x9HZ_ljTCt0fHPM3afRKfTRcx_snFESizYjxigblfJwAmZsDctA8xaJIN4yw3X8uDmpcvOv-LhXY9kdfGcJNYVCDONXxX3AS0YROSrpJz6ORV09jnaIsBGXXeHAEC8zArNMePfWSWnIky5Mu8YVxFCuzwSdO-KKlXwz1qtTfSoYj5VRPbcF80DofkCMfBo4IFV1144StsbI1OwpPto6DnmIzLfTb8CIOHs7nEBFzIED0IhFAt5uakOTCiBiZ08aft2E2vsgY24mZHp665cFlf5wFqtdyEohztrGRnfZPgXWIW9NA9X6EUm7E-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46400b9012.mp4?token=bFzY4cPY_gtQDcu6oy2_nSdC4p0x9HZ_ljTCt0fHPM3afRKfTRcx_snFESizYjxigblfJwAmZsDctA8xaJIN4yw3X8uDmpcvOv-LhXY9kdfGcJNYVCDONXxX3AS0YROSrpJz6ORV09jnaIsBGXXeHAEC8zArNMePfWSWnIky5Mu8YVxFCuzwSdO-KKlXwz1qtTfSoYj5VRPbcF80DofkCMfBo4IFV1144StsbI1OwpPto6DnmIzLfTb8CIOHs7nEBFzIED0IhFAt5uakOTCiBiZ08aft2E2vsgY24mZHp665cFlf5wFqtdyEohztrGRnfZPgXWIW9NA9X6EUm7E-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
محسن افشانی: اون شورت و کرستی که استوری کردم برای خریدن آبروی یک بازیکن فوتبال بود!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106206" target="_blank">📅 12:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106205">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=Wa-kXQoBXGEnoMJJJura_NvM6vhfgLCnrgPayIdpo_AhcDv_QpFQsXdEy4hUTBOm_3j8swMJjC3dVAmSEOqVPD3MZV6HRekDHOoI95ZpQ5ZNY3iA9sE2Hl5JsF19HoET0FjhdruTxxlID3T6a880L8NaBQ2OKeK-y2USR6Zuai2m4nbWbuoQCC5qgGdXwkrDiqYcaPiX4uzO4i9_stdle34jdQTkqeB_Ik3aN4SjNlXLwfYBAsmH3riXP_LUTVJ_1bHnpGzYD4F14-L5YbAEsasEUc64GlT_qpcT5-CqeFmmjCDnx4_iLWlwnMYg9K9TMN-X40lQOxjk2MNSTTxO1RqfxLBI6MNLDbhxl1FNhfb2l-ow51n-u1sF89LRL5zpk7mvvilWVgoXbpOqLkofw2ew8EUP5LJM9qn0y0m1fYWrAn0m6ccvuq9qk47q7k23LbBEntbErSksvJoNlCZVh9Gk418djExeJ9TxT0BcmMzaPBN08j1lufmi3j-rn8mRtbPEojUWOM9j4LcBcFI14VUZr632cWChRO3dA1sUKRYapm4qdKaOgQzsxBlh_R91HqD17RFePemra3R__WqBDiB92fES6WOc4XjsspXjYXyOUifSVhwy5r_yOCjgNEcSKeC10a7iUvq7B1NMHiFvA1iHCViAa9WSDe1nOPrETWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=Wa-kXQoBXGEnoMJJJura_NvM6vhfgLCnrgPayIdpo_AhcDv_QpFQsXdEy4hUTBOm_3j8swMJjC3dVAmSEOqVPD3MZV6HRekDHOoI95ZpQ5ZNY3iA9sE2Hl5JsF19HoET0FjhdruTxxlID3T6a880L8NaBQ2OKeK-y2USR6Zuai2m4nbWbuoQCC5qgGdXwkrDiqYcaPiX4uzO4i9_stdle34jdQTkqeB_Ik3aN4SjNlXLwfYBAsmH3riXP_LUTVJ_1bHnpGzYD4F14-L5YbAEsasEUc64GlT_qpcT5-CqeFmmjCDnx4_iLWlwnMYg9K9TMN-X40lQOxjk2MNSTTxO1RqfxLBI6MNLDbhxl1FNhfb2l-ow51n-u1sF89LRL5zpk7mvvilWVgoXbpOqLkofw2ew8EUP5LJM9qn0y0m1fYWrAn0m6ccvuq9qk47q7k23LbBEntbErSksvJoNlCZVh9Gk418djExeJ9TxT0BcmMzaPBN08j1lufmi3j-rn8mRtbPEojUWOM9j4LcBcFI14VUZr632cWChRO3dA1sUKRYapm4qdKaOgQzsxBlh_R91HqD17RFePemra3R__WqBDiB92fES6WOc4XjsspXjYXyOUifSVhwy5r_yOCjgNEcSKeC10a7iUvq7B1NMHiFvA1iHCViAa9WSDe1nOPrETWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روش‌های نوین تیم‌ساکت‌الهامی برای وقت‌کشی! الحق که رو دستش کارکشته‌باز نیومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106205" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106204">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249d50f161.mp4?token=LB03QSO7iibCst9BchiynCOHH5KBDF1IS7DQoeZoNKd1dP8s6ZwuOdjW_3HUeuvVjG0Rfzc5PV-JaKEBBQkFCnE5QAmmHbzr6r28E78PuEMwgYsXbtWfiuK4TB6O_DidMOp8QSCgxvNdk58nzMcRsAHHNyyM1cSICitofn-YgwrGNuIdkhtEqB5Z3ZAfx4NIJQNGUtmwyB0iiA87BgDsmUSrLsht5ImnZcTF818CTaoASd-QR99-XQ-HV1fhb0jbJeQZ4KQJu7vfqALcrW9GcjHdrzh7oq8M8edsQi2QyX4xhquNfeLMpuysbeSNHHqpaELPHC1wZd9yEwbPencmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249d50f161.mp4?token=LB03QSO7iibCst9BchiynCOHH5KBDF1IS7DQoeZoNKd1dP8s6ZwuOdjW_3HUeuvVjG0Rfzc5PV-JaKEBBQkFCnE5QAmmHbzr6r28E78PuEMwgYsXbtWfiuK4TB6O_DidMOp8QSCgxvNdk58nzMcRsAHHNyyM1cSICitofn-YgwrGNuIdkhtEqB5Z3ZAfx4NIJQNGUtmwyB0iiA87BgDsmUSrLsht5ImnZcTF818CTaoASd-QR99-XQ-HV1fhb0jbJeQZ4KQJu7vfqALcrW9GcjHdrzh7oq8M8edsQi2QyX4xhquNfeLMpuysbeSNHHqpaELPHC1wZd9yEwbPencmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
پس از ۱۰ سال ایران در UCL نماینده نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106204" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=HBrW1aFkdqAfm4k4jK0dT41yeXV4Mj8SkcUVPFnL3_xm81PqUBqHj39W7d2hJV3e6ckZ9AT2TCEe1kCyC-gXRvKqboGExPzuD5YGYhe05NXYnKfjb_dCwEuQYfmMpE0HDgHecI6GJ8ROZ5I8aIbBryDhTvycqHJDxGs-godCpuBcjj8DADnZFtuSNPTG4TmHXZciZb3RERC3ZcxDZDMEj8B2-DEGEdWa6SrIRWSrFINXhgc-4Kxno-QU_VkmG7pldpBbod_mWS3wIu0y8rPngU-9v_DF2aLXL_DAdTQhfUSRpaN0Gm_lTImxNClsSjBQqNPNrei6vb2BAM0KDLPpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=HBrW1aFkdqAfm4k4jK0dT41yeXV4Mj8SkcUVPFnL3_xm81PqUBqHj39W7d2hJV3e6ckZ9AT2TCEe1kCyC-gXRvKqboGExPzuD5YGYhe05NXYnKfjb_dCwEuQYfmMpE0HDgHecI6GJ8ROZ5I8aIbBryDhTvycqHJDxGs-godCpuBcjj8DADnZFtuSNPTG4TmHXZciZb3RERC3ZcxDZDMEj8B2-DEGEdWa6SrIRWSrFINXhgc-4Kxno-QU_VkmG7pldpBbod_mWS3wIu0y8rPngU-9v_DF2aLXL_DAdTQhfUSRpaN0Gm_lTImxNClsSjBQqNPNrei6vb2BAM0KDLPpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚠️
ادموند اختر :لويى ويتون هزار دلارى رامين رو با دو تومن تو منيريه مى تونى بخرى
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106203" target="_blank">📅 11:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=MB7z6ZDeaAIJTtQ10mJ6VBQ-dw7N1mWOzMekm8r7_fhqSJ2dJpoIPWhHH_xpffmoHR8-u-g1eahprtlTPLmAuihXNq-dEEmA66UJUYN9gxcuIlvtHNt63UPNxUxnCpf6AeI7yHXvv2pj_dAaxDLl0GMvLlqVt3qFJSzrlpur06pvyd8-kmWLCcscAd34uUVDUbAduwqqNwN8edyt4vQYmzhRbCC4JSUuz4HJ0d77A9EW5uGKAA8Xm8KKdlLZmq89XuB31ODCL6MOwk9yrohuJU2nbuhEtxSSDEfGvswVNeRnHK-Xf174fJ9L4qr9Bylv8C8T2vQ9TXTnRq01ZWCXapvlrntVWeQf6b8ySwuUiAiSebQvIukrNmzmjLtVShOFT-uAtL2O6B9uDTCYy5LjICv7OXt7imRqOmlcI8fRuT1O2nqv1HNssBIzPIkViMpCX7vstb9MijluCWLfIhxXgOd2FeKxOTYIsqeMcaFpMHZJ-3s03GiMRNm1plqURLRA-qQMC09A2OjHRnd781mXfOeah046iA1Et3pWB2xzdmXYPVXM0_5XRuRmKaw_K9w_RR9gUiuLCUdHkFoZuyowrA6xMJtcvBd_c8R1Pt_wqAJ68KewpPHcSEjlbRcpkf5kXA2NLs-OlvShjksKoudkHb33i2wqURxUg8WT7kSVI3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=MB7z6ZDeaAIJTtQ10mJ6VBQ-dw7N1mWOzMekm8r7_fhqSJ2dJpoIPWhHH_xpffmoHR8-u-g1eahprtlTPLmAuihXNq-dEEmA66UJUYN9gxcuIlvtHNt63UPNxUxnCpf6AeI7yHXvv2pj_dAaxDLl0GMvLlqVt3qFJSzrlpur06pvyd8-kmWLCcscAd34uUVDUbAduwqqNwN8edyt4vQYmzhRbCC4JSUuz4HJ0d77A9EW5uGKAA8Xm8KKdlLZmq89XuB31ODCL6MOwk9yrohuJU2nbuhEtxSSDEfGvswVNeRnHK-Xf174fJ9L4qr9Bylv8C8T2vQ9TXTnRq01ZWCXapvlrntVWeQf6b8ySwuUiAiSebQvIukrNmzmjLtVShOFT-uAtL2O6B9uDTCYy5LjICv7OXt7imRqOmlcI8fRuT1O2nqv1HNssBIzPIkViMpCX7vstb9MijluCWLfIhxXgOd2FeKxOTYIsqeMcaFpMHZJ-3s03GiMRNm1plqURLRA-qQMC09A2OjHRnd781mXfOeah046iA1Et3pWB2xzdmXYPVXM0_5XRuRmKaw_K9w_RR9gUiuLCUdHkFoZuyowrA6xMJtcvBd_c8R1Pt_wqAJ68KewpPHcSEjlbRcpkf5kXA2NLs-OlvShjksKoudkHb33i2wqURxUg8WT7kSVI3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
💥
یک‌دقیقه خاطره‌بازی با اسطوره آرین‌روبن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106202" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106201">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=rSNrvLrHs_QjtaojyBJevqfFnSIoSfUd_Jj4jUiptHO5W-zBGOSFkxtHts1lr_2GK1LGENy-IhI1aNizgw1CH6qx4nwelHnZ2VbGTE98B_VASbUl-H0xh4kXweSBL-CtT7-rZuBt6Lil1zsfnnZkhUuZOu4c0uBoK6bZv2ryuJlBewS_tsLnvTEdVyLoPCCXMwQ-p3eTXr_NjsEEhOUo3gunPoJrEFPdeVQgw4deGU8FaN0_VGRHA_F9p_umN81YFUWNf9iEtQFB1CWiDw7tpx4pr-UF1p4u2xhUHbaR953Q8wCrjw2VQ4nb7xPKICT4Pj5sPeQZ55YdMvJM-7ZS0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=rSNrvLrHs_QjtaojyBJevqfFnSIoSfUd_Jj4jUiptHO5W-zBGOSFkxtHts1lr_2GK1LGENy-IhI1aNizgw1CH6qx4nwelHnZ2VbGTE98B_VASbUl-H0xh4kXweSBL-CtT7-rZuBt6Lil1zsfnnZkhUuZOu4c0uBoK6bZv2ryuJlBewS_tsLnvTEdVyLoPCCXMwQ-p3eTXr_NjsEEhOUo3gunPoJrEFPdeVQgw4deGU8FaN0_VGRHA_F9p_umN81YFUWNf9iEtQFB1CWiDw7tpx4pr-UF1p4u2xhUHbaR953Q8wCrjw2VQ4nb7xPKICT4Pj5sPeQZ55YdMvJM-7ZS0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
نیروی دفاعی اسرائیل (IDF) دیشب با انتشار این ویدیو از انهدام کامل تونل‌های متعلق به سپاه و حزب‌الله در منطقه استراتژیک علی‌الطاهر در جنوب لبنان خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106201" target="_blank">📅 10:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106200">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxHbC3mfFFrVAe_D6S5QAvsm3u-1-awRvyz7ulSuML5pNa7-J-ToEQSIKzo3X6lPsVpKYw3OAw2BukHS4gWD54WIpNzK-k23FApP3Pdtaj_-gpcwfcIhP5yD4phm52YZEfpzSAiBTkzU18P5ghZ9kXBhvtfy4bpT0eEE5hEjeYF9KUkdty08-hheM9_BXeShLvF66qI8iN2uW5vL_mdT5pCuPGxR4YSHknNz0NCzIU9TvpvmYERIn8SyXj9UDvQ4pk6YTczWYuP78S55uBDjm66X4gFwXS2PyzkJHY4KUkxeJVttGMHG1VMPk5U3CvCNdVXI3Ymlz8GXes22xTotgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نامزدهای بهترین بازیکن هفته اول UCL
🔸
فران تورس
🔸
رافینیا
🔸
ارمدین دمیروویچ
🔸
مارک بارترا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106200" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106199">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=CZeoyKScQHCtR-nrqssOcCB6Ae_X6S4TYa0T9gaTPFP10qTKaUCljsb7DXt_0tponatgaWTRXx-tTl1ACiGv-gIXTya7TE9AEN5ww7BELCAMcm9xpN7i-j669FFVdCAVFmUmEBdq4jAlpTiArkWIg3jJ1ivN0VObJUgfuqSq7E2c6t2M-KiG42GfNw_FqqcPLYmeO9T2ixh7YPsYBcRdg3cKg84O_kLFDn3NP3dTNyXBXnvu_DptPI8B5S040dGoXnoxiCZ8UmkWESc-4apZGhg6iXo0xYmVjr0jpHJXGAQ0yg_HXcYpq5f4Gr8RLPUVvSlTIe6CowkoCMCYKk9DsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=CZeoyKScQHCtR-nrqssOcCB6Ae_X6S4TYa0T9gaTPFP10qTKaUCljsb7DXt_0tponatgaWTRXx-tTl1ACiGv-gIXTya7TE9AEN5ww7BELCAMcm9xpN7i-j669FFVdCAVFmUmEBdq4jAlpTiArkWIg3jJ1ivN0VObJUgfuqSq7E2c6t2M-KiG42GfNw_FqqcPLYmeO9T2ixh7YPsYBcRdg3cKg84O_kLFDn3NP3dTNyXBXnvu_DptPI8B5S040dGoXnoxiCZ8UmkWESc-4apZGhg6iXo0xYmVjr0jpHJXGAQ0yg_HXcYpq5f4Gr8RLPUVvSlTIe6CowkoCMCYKk9DsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده و دلهره آور از جنگ اوکراین ؛ سربازی که شانس میاره و از زیر تانک سالم بیرون میاد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106199" target="_blank">📅 09:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106198">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
🇪🇸
تعریف و‌ تمجید جالب تیری‌آنری از رودری خرید جدید بارسلونا و تشبیه‌ش به سرخیو بوسکتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106198" target="_blank">📅 09:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106197">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
اینبار کنایه تاجرنیا به پیمان حدادی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106197" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhLbOIv_uUX0Qu5kh8J3o2qOylzac7FeVSjltaHM9jOkGLvj0eOck1PA_iFW_FI-eVXmkF8OAStVq6QtHhoDPdv7islGwYExO9JPmDGwQFKFPOB3N0MBl8kNJrTaE26iAIwxCRSyX6WnCf4hIYxB_fdZvD2bXAT423QHPgY7yRfZnf9bugXDLvWh0eEV7jRSfrlFbwtlh5QFqbgSUbNPRqVowx30SDpURbnh7xsrZpsfFUKOegIhACc3diiJrPmdeKMfPE04rESxt-NuH0ocWElPK8ww6m1MX80oxsuwzfe2HZFiZgrMBlCNcXViTJlJ_smIC-bhrVWCmJ-aWvOXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
🇪🇺
کمترین تعداد بازی برای به ثمر رساندن 55 گل در لیگ قهرمانان اروپا:
◎
🥇
🥶
ارلینگ هالند — 49 بازی
⚽️
◎
🥈
رود فن نیستلروی — 70 بازی
⚽️
◉
🥉
هری کین — 71 بازی
⚽️
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106196" target="_blank">📅 08:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106192">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcya1R4DbStm6DXtHQSSAhRvjXMrloKIhrPx1OmofoFds9dM0f0aXfpDN3XvHiDhzEI0gCjI6Ui9319hxJkE_Cb4I2y5Ay5Aw56HN7BZU5c8V97q56u5z8Ig4TCuj1-k7VczIDjbxDLcMIAADXh_T3p3pDCtwouDFqiVxnfNQGzIo2Q_wnkOPOXk1xnNXCWCG3sFoOR3hHGuE0VBQfP7rVkzVyYGOc2eqBhdngbQS0EC1cvyvwYpovosajV5cJo2zbJ2zgG6qIw-a2x0Lsunu0BevyESYutDsdX8ift2PZK7bH-8mK0sjq9INhprvoxRI-u9yafrzvkGELzPFaKORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
مقایسه آمار السد قطر و بارسلونا در لیگ:
🇪🇸
بارسلونا ۴ برد و ۱۷ گل‌زده و ۱۲ امتیاز
🇶🇦
السد ۴ برد و ۱۹ گل‌زده و ۱۲ امتیاز
❌
پ‌ن: دوشنبه هفته‌آینده ساعت ۲۱:۴۵ قراره استقلال ایران از السد قطر میزبانی کنه. ایشالا خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106192" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106191">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHd3W8nv_Iwq2cjftAr7RmBokgdA0wcz9a6NuhdRssUx4SJJczIVXrNh1PG34tqvudzfAhkV6Af4_AI1ji2AVcbsaxEvAqTYvFUBYuH-MVRzO1vQtUC1g4JkTz2kqXQq1lSG1QMchWH67NkzMh2_fuiLmmvZT8Z5Aiw31VFZSu9_AAci7UwZPqKW5bJvVUc-iVqQLkBiq-ZgvdseYk6wC0IC_76tNMeSGnpvwhH_KCJNgrYPrEe80QhxSJi0suxCTH0FZb_vfLsRmoR0S6-kWFpBVMCDrVtzjitlNFiSMLwLutHhYjalgNL3koEd8grTWKYWg6-ro3Z0GWbyf12L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106191" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106190">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4pgcebeju3zKsXv4F7LbjxKO36hNYkiPbT6RzO5eS552TxFg2XMNmXCfsclAj-3qAvaWLBy_GlJOIvAaIDiI8JD1nrpJGIahiUHdQPeL0H7ZBndq8sgsF0m-KxTbUxqL7hOLBV-5rrYk-Ejse9SkalPMIe6Pjlbws7DGTg4mJ_aDkCZa7Sz2phE2BUldE9HonSSLNHaPg_o7xMHIro5606hN_fEEfgU5KU4qv38290fzYA7GRsyTx2rH_RIJUx9Kja-_oi4FSy1m0FlihY1GlNRS1uczYKd-IviyEJ3ionTmjOycUucuVPyqNDwcyFnJN2MIzaeOcukbL-jEnBthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106190" target="_blank">📅 00:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106189">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇿
هایلایت بازی منچستر یونایتد 4-0 صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106189" target="_blank">📅 00:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSomEmoVWc5Rz7vy7YtVVVsGOARJTTE_Ri3HQC8yUbiH1qGVpj-_XnPmeRNZG3xyDCivsH4N_OG2Xzm9DRqI09ecduXlE1cKkVVE-7kqdKOH5KdjzWu-W6L2C_bopVYtwJmCFrkq79abQD9vAQ4G0Kuf86VtBSX5YZMc2ZLxVINPUqVk8HFi-Ye4I1BF_KjcBN6IXa7scWbWNwogulDmym_nyiW7FELR1Ufc10sW4nWSmLpCzaP68jdETiUc4nf0Wtcpm4n0mMzgE8r0bhuaXLk__nJ4tDert3mWNfm3e8hYr3c5SKuhOcFynkltRlLpbPo6iQ3EMfN2hEQ5PEb9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106188" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106187">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3993269f13.mp4?token=V-w9PRNElMs3MLbCu8qvZH3Fou0Amz6fTVC6Xh-Z6id7kWZTa2PyP263sAk6JlleUGrKixp3nWE9h9lPsJES37l_0t6xux_8fQA_HuO8bUzP8bi1JybGoCOyODmplV225Y9LH7KCHCkhHZ8EYrWrumNuAckk4ZViY__rrr1JWN4ovkxEs40Aeu-nzQWMR6bb71OCSn61PoqwpEbe7gPqp670_-M9lN6PapZ7cD4eNjJJCX4sbppEbp2sPYCvndZp94HZwcneqaZ3YsiksnheTctyNkrGGnGXANQWAyLPdThL5q_F5OjkMIZnzk78_q2My_wqRY75CskJv5EGoA1lbgiuszdItrLME2GaANHG3VIAGK56uttFJT_bDwEN5NJVAnWCRcRg9zJ68EEhBWYKqwbKmDyVMNAum3DQ3x1w86_adZSVfsDae5Zj2_cLYJGDXq5RO68o4MU42QCXyBITiAu9gTJ1Yoblw0YXYUewaD4H01g_65jyeoTdYdf_KZ_9emZWdhpxkLhvyFv14TOW2a0mrL2tGg9PTlOZIjhkziqode6dUpppDFmUCTdCvyCybTNzRNP3tUCGppVKNZ8fpTR7-U10E4I1IAzh8Rfo9908Rg0iCiB2VmUY7nsdmjiqQr_oxiQA82G_FBJBltD3rc9kHz2tNhXRwYPVlze7Fkk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3993269f13.mp4?token=V-w9PRNElMs3MLbCu8qvZH3Fou0Amz6fTVC6Xh-Z6id7kWZTa2PyP263sAk6JlleUGrKixp3nWE9h9lPsJES37l_0t6xux_8fQA_HuO8bUzP8bi1JybGoCOyODmplV225Y9LH7KCHCkhHZ8EYrWrumNuAckk4ZViY__rrr1JWN4ovkxEs40Aeu-nzQWMR6bb71OCSn61PoqwpEbe7gPqp670_-M9lN6PapZ7cD4eNjJJCX4sbppEbp2sPYCvndZp94HZwcneqaZ3YsiksnheTctyNkrGGnGXANQWAyLPdThL5q_F5OjkMIZnzk78_q2My_wqRY75CskJv5EGoA1lbgiuszdItrLME2GaANHG3VIAGK56uttFJT_bDwEN5NJVAnWCRcRg9zJ68EEhBWYKqwbKmDyVMNAum3DQ3x1w86_adZSVfsDae5Zj2_cLYJGDXq5RO68o4MU42QCXyBITiAu9gTJ1Yoblw0YXYUewaD4H01g_65jyeoTdYdf_KZ_9emZWdhpxkLhvyFv14TOW2a0mrL2tGg9PTlOZIjhkziqode6dUpppDFmUCTdCvyCybTNzRNP3tUCGppVKNZ8fpTR7-U10E4I1IAzh8Rfo9908Rg0iCiB2VmUY7nsdmjiqQr_oxiQA82G_FBJBltD3rc9kHz2tNhXRwYPVlze7Fkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106187" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=dO6oBcIU464LC8EZ5_nQzvrwG-eZr7ic7rOh73u6_WLqxGwSujAerVrDYnuRwIxzliGCTipt_zN1ZP2JLfzfysXEwtlXg2fhvXHvtPxrtEbt4HXM7WIU6VOTxs4o50EANhHilMqq3okuClxPyVvd2y-O74o4wDbS7MtZe4MbyVZ8jIRFZe-0--KRX7m5RHdS6_LbputQuteOJ5wJ0tdt5ZqwTy5bUeLwSvw0bkywe030Ydv9Y8zjAcg-e97CZITh96ffnqulF9_o7DsH3tjPgcrxg1s7BwkxD_dTcoZu5ihh8eA3wmLeIdRkhlW0tCZLnAxNQ82SkcSiHgQJwY9qxGEqjweyhzg65s39hU3UY2l61DZwFnnTXYhUQuC2yp45XGUtbTMiR0PSVNttmZ3H_iq7w0SFdzS02egTluitVsN6WXwy0LXhLU7Fme9aVAKo_OAwZaNs9QL3gHkGGbc1fhj1KuiVq57JoFnzR7I-AUOn7nY0aBWOXOGHNbE-NahD2w-N5Q7QCKC0XQNQBHh6XU96sEyVFA70TASyJs4D5K_resx2Cmk5KQWFqzim7XfHEIn_ZvJbL6CmIQnpTHprH_8jIjHT0MVbxpCnF3zsIc_vO5JIvo-nITIm82bgCtE6e8b0X4zbrz1Qa5sCP7XU4oWj3faDSBdwVMEGUMm9t6M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=dO6oBcIU464LC8EZ5_nQzvrwG-eZr7ic7rOh73u6_WLqxGwSujAerVrDYnuRwIxzliGCTipt_zN1ZP2JLfzfysXEwtlXg2fhvXHvtPxrtEbt4HXM7WIU6VOTxs4o50EANhHilMqq3okuClxPyVvd2y-O74o4wDbS7MtZe4MbyVZ8jIRFZe-0--KRX7m5RHdS6_LbputQuteOJ5wJ0tdt5ZqwTy5bUeLwSvw0bkywe030Ydv9Y8zjAcg-e97CZITh96ffnqulF9_o7DsH3tjPgcrxg1s7BwkxD_dTcoZu5ihh8eA3wmLeIdRkhlW0tCZLnAxNQ82SkcSiHgQJwY9qxGEqjweyhzg65s39hU3UY2l61DZwFnnTXYhUQuC2yp45XGUtbTMiR0PSVNttmZ3H_iq7w0SFdzS02egTluitVsN6WXwy0LXhLU7Fme9aVAKo_OAwZaNs9QL3gHkGGbc1fhj1KuiVq57JoFnzR7I-AUOn7nY0aBWOXOGHNbE-NahD2w-N5Q7QCKC0XQNQBHh6XU96sEyVFA70TASyJs4D5K_resx2Cmk5KQWFqzim7XfHEIn_ZvJbL6CmIQnpTHprH_8jIjHT0MVbxpCnF3zsIc_vO5JIvo-nITIm82bgCtE6e8b0X4zbrz1Qa5sCP7XU4oWj3faDSBdwVMEGUMm9t6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌سوم بایرن‌مونیخ توسط آلفونسو دیویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106186" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29ed472619.mp4?token=MpPg_tawl2Q7BFKmnNpt1csLB2CAyYoYQ554_K2b_ft_gnWXV8KgbYYbFuME0_Y6uVJkw14dvOdozErmmt4Z31jqxTsyaNt8-bA26bsYAvAi132YvYDUA_ATWiAY26rSe8rIVJzBawbk93LdJuNFZZpjpTOsuHCLmzz_daOyuhLcFhvw2B0jbWYC4ZEarW9XNU4Sm9aZMdcTjscZr39lzogm9-bGs_OPf7BcciQ0P5_Pdy35qCBMJDwqS-cyMKV1NozkTwK0Q8R1gCp2nLA5JuXmOHvVLn0GiYy_LGlN-kGiX-bfWs_bkl9X5lKKm_Z_xC2wilHsJm5GqXDbTJO2Z2yOpSVCXhn5zuJOmccE17qlDoFzvWbLM3TJK4gDM57TdszPb5Ajsd3OViOec3I3KmVbKpNvWbccG5TnWuL-X-_7sVfOSmseYoxrAOiksRLJ_5U37ImRI7INoyZ3_qP9i3AFWClw8sCP6Z9OrsVBgOLMatkiFzKgbWuJxtOvC2Qd8zV_x3hg43xCD4tnVtnpX0i0TXWVssgQ2o_m8o1UfsoNGHfQvm-bYddic41GOR8jDx6Har3Q2YsNt1JPhkPOwSair4g7xpOktY7nv1YxHb5F1R7kzPFRlZUU03gvkZAWzfrlHlLwbRydjbCX5FL0os5_BybG8pf6bmCwuK3hfTk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29ed472619.mp4?token=MpPg_tawl2Q7BFKmnNpt1csLB2CAyYoYQ554_K2b_ft_gnWXV8KgbYYbFuME0_Y6uVJkw14dvOdozErmmt4Z31jqxTsyaNt8-bA26bsYAvAi132YvYDUA_ATWiAY26rSe8rIVJzBawbk93LdJuNFZZpjpTOsuHCLmzz_daOyuhLcFhvw2B0jbWYC4ZEarW9XNU4Sm9aZMdcTjscZr39lzogm9-bGs_OPf7BcciQ0P5_Pdy35qCBMJDwqS-cyMKV1NozkTwK0Q8R1gCp2nLA5JuXmOHvVLn0GiYy_LGlN-kGiX-bfWs_bkl9X5lKKm_Z_xC2wilHsJm5GqXDbTJO2Z2yOpSVCXhn5zuJOmccE17qlDoFzvWbLM3TJK4gDM57TdszPb5Ajsd3OViOec3I3KmVbKpNvWbccG5TnWuL-X-_7sVfOSmseYoxrAOiksRLJ_5U37ImRI7INoyZ3_qP9i3AFWClw8sCP6Z9OrsVBgOLMatkiFzKgbWuJxtOvC2Qd8zV_x3hg43xCD4tnVtnpX0i0TXWVssgQ2o_m8o1UfsoNGHfQvm-bYddic41GOR8jDx6Har3Q2YsNt1JPhkPOwSair4g7xpOktY7nv1YxHb5F1R7kzPFRlZUU03gvkZAWzfrlHlLwbRydjbCX5FL0os5_BybG8pf6bmCwuK3hfTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل دوم بایرن‌مونیخ توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106185" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106184">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌چهارم منچستریونایتد توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106184" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106183">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=c-W8RbvzTKo8O-S8UZTGcjohmyY8ApJ3EvmFX6O-bNCU_puzHvnLTRfQr3BpJuGodXOYirZXfMT2gerc1O1qUJV5_t5-KRn9bWH7JHKKVhXFK4Ub6i4LCiyA-y7xk1HPPuJmpKhdeT4FVLYCr1sGZ1wXrLGvcJ2rMZkMNwtEzSRQH1xfSYfcQbBnGAIUE8_09Q519CT0bjm8Eb14Fp9WdCyyu8-uDkUfappVKnPo6svvoU-adghTDFBkSQj30YYzrUmQxMINoy0AYywnowkV2hWQeVB2ZUyRJFw2ckNlChuucDUdriYfKmQvskuSQ1DEUzE2o17WbZp3tr61luzGi7TiE3Gy7AkxnJ6TyT15afZd8xc5EMnW9n7scR7cpbIaOI4-Wp82rCSKgPZGTuEYkUM0bUxcHN3LLWiHeAth_NqkrafHzqEBE1tjhY219aXOQQRB4D-9bNsqwK97aqWZD8kAQuu5vWPO2ob22XvrW3dzjWSQ_5bhLOoF8IF47SihAHfr5UtcCNlJc23V6gGwoKCyLJDKch5iM3uYeFk8uJCvUR1sT1lb7Rg1Eed_ruSOKnWSrAu07B-BNS9MRXLuPUEI7subYLOHzZN24pS1mh8kDGnDnj66dj_wawSulvWXFP8wVyDUxw6ftqkI9ftSVEKgZP0ZgQhwdh0krdlm_7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=c-W8RbvzTKo8O-S8UZTGcjohmyY8ApJ3EvmFX6O-bNCU_puzHvnLTRfQr3BpJuGodXOYirZXfMT2gerc1O1qUJV5_t5-KRn9bWH7JHKKVhXFK4Ub6i4LCiyA-y7xk1HPPuJmpKhdeT4FVLYCr1sGZ1wXrLGvcJ2rMZkMNwtEzSRQH1xfSYfcQbBnGAIUE8_09Q519CT0bjm8Eb14Fp9WdCyyu8-uDkUfappVKnPo6svvoU-adghTDFBkSQj30YYzrUmQxMINoy0AYywnowkV2hWQeVB2ZUyRJFw2ckNlChuucDUdriYfKmQvskuSQ1DEUzE2o17WbZp3tr61luzGi7TiE3Gy7AkxnJ6TyT15afZd8xc5EMnW9n7scR7cpbIaOI4-Wp82rCSKgPZGTuEYkUM0bUxcHN3LLWiHeAth_NqkrafHzqEBE1tjhY219aXOQQRB4D-9bNsqwK97aqWZD8kAQuu5vWPO2ob22XvrW3dzjWSQ_5bhLOoF8IF47SihAHfr5UtcCNlJc23V6gGwoKCyLJDKch5iM3uYeFk8uJCvUR1sT1lb7Rg1Eed_ruSOKnWSrAu07B-BNS9MRXLuPUEI7subYLOHzZN24pS1mh8kDGnDnj66dj_wawSulvWXFP8wVyDUxw6ftqkI9ftSVEKgZP0ZgQhwdh0krdlm_7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌اول بایرن‌مونیخ به بودوگلیمت توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106183" target="_blank">📅 23:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106182">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C09UiPzVl2v12_EX5s3BhGB90rNjkAfzByGMvzx2M-TWwogYIVOv1zzjj-PF5zLz5ZJGxPJEZwNLFRN2gYjTkcR7qh2FXui_o00zYCp3p4llw7yzekC-lvFDJStCcvJNJgpDtb5mB8--WwOVnYsMitmE3zmfvAUtbWiA8UJTAuPeSf_y4Vh4WrlSe2eS41HTz3fd-Kwl8bUOY8RXw7gTK7rMu_EfLzjjbAS4LlmtrIGCJWLykZYsppiVyzwunC35Vo0L1JZF5GwLqJxdztsPaIgxCsgAIHN4ccS0U13vBWPBzADRNTu6Lqwp4jXaICiygj53BwsRvpaOhnAjq3IFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔥
🗞
رومانو: فیلیپه کوتینیو با قراردادی آزاد به سانتوس پیوست و هم‌بازی نیمار شد، هیر وی گو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106182" target="_blank">📅 23:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106181">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106181" target="_blank">📅 23:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106180">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxtK3pVvfSUNehXigAgl7oSU2Lhh9ggkrC1OzOvLzBaXjRP_c4XtF_G0kjIlKlPSAT3Wf26bWfaxuU2nbIjuzg6OWDmSkfj3x6Qn_TBEt5LNiVw-eqm7eCWg0rENqHTbuiQK2Y6vYmaBhe85ktSdcNRimOaO5J3m7jk8yXGnfGmAbWwE8CtKCXsZ9Ad5VbE0PpKTe1mTSp9-gJJ-Hb_kAU0rbJZsvxC6Sm5ic1x7Z7b8XeXyRjnZl5qTSRZbsGUtOCx0yE9lQ63JTfsC88pa2lAjRpaFXP_SsRdum7t6zsOUblXMsvoYo_7vg6QEu46dfXPThh59iskYso3RarPucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106180" target="_blank">📅 23:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106179">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=LxTEz2PjqrVl4-EmESY8U9h50LeA6_sNV594doK8I62coY1VuBmBsCTzWmaw6a0Mv_lKuETLhJq_NmN4PsRdL2KPAMyhVMyPydYADpnFw5T9Cr62bp_RfT-qJVA0-1UC47IkOFVnAso1znCeR2h3pCSQxiHm3oRgaLX81movaWDX1kjR_l6Np7wP7CkFHA_JfDohW36A4VFemhydsGDZzCxLW8aFREeH-19tMsCk53YzWzjpWM73IJo-VrjXb1LXYl91J5GzPgDAno9wTusD8NACMWbvQ1QDC1bUZ5uH5kNSZZV6IA3GtytElup5Joo26X51TooQKp2ftFlH5aAKax7UnOQ_cLxzBZYwTBRDpuZA3P-wGWZaCKfZlsNFMv5fSh6kN5QrYxTkQDuSximOPx2q4jgsWD1EkmQXfxTuPNQTK6-6Zqfdx8joPmNawinQcOytQpBy1p1YKbyDkcbdsGa2HJfDrCOfT4FMaz2c69Yys76nIdTRpnbSWETqkQSuaiCelRcGvGcLpiplpc2ZuhYgErBSC8iSepzBKU_1DdWvMfn9_3RQ6MH1KlIsvGVQbb5vrD0CslJJ53YyD38nRZU2NdoCqCt_fwQGSAX_A5XhSD1MY14GY-UW9ZjjZHNHy4p6Lm6zg4RKKnStba2roPO9D5ZAzFq2S7X7pjVt0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=LxTEz2PjqrVl4-EmESY8U9h50LeA6_sNV594doK8I62coY1VuBmBsCTzWmaw6a0Mv_lKuETLhJq_NmN4PsRdL2KPAMyhVMyPydYADpnFw5T9Cr62bp_RfT-qJVA0-1UC47IkOFVnAso1znCeR2h3pCSQxiHm3oRgaLX81movaWDX1kjR_l6Np7wP7CkFHA_JfDohW36A4VFemhydsGDZzCxLW8aFREeH-19tMsCk53YzWzjpWM73IJo-VrjXb1LXYl91J5GzPgDAno9wTusD8NACMWbvQ1QDC1bUZ5uH5kNSZZV6IA3GtytElup5Joo26X51TooQKp2ftFlH5aAKax7UnOQ_cLxzBZYwTBRDpuZA3P-wGWZaCKfZlsNFMv5fSh6kN5QrYxTkQDuSximOPx2q4jgsWD1EkmQXfxTuPNQTK6-6Zqfdx8joPmNawinQcOytQpBy1p1YKbyDkcbdsGa2HJfDrCOfT4FMaz2c69Yys76nIdTRpnbSWETqkQSuaiCelRcGvGcLpiplpc2ZuhYgErBSC8iSepzBKU_1DdWvMfn9_3RQ6MH1KlIsvGVQbb5vrD0CslJJ53YyD38nRZU2NdoCqCt_fwQGSAX_A5XhSD1MY14GY-UW9ZjjZHNHy4p6Lm6zg4RKKnStba2roPO9D5ZAzFq2S7X7pjVt0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
گل‌سوم منچستریونایتد توسط ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106179" target="_blank">📅 23:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106178">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=U2zV4KJldfgGtaUCbdE1ix9rU-2ijmSj-cXFgv-bsPoCv2q7PCKLhvUixKRnhsXFJQHSLXoZWq8UaUrsp_Z-9LoWoZBX8SMLyfgN9KJVBrdiaXodIzV6EZ7eaSvvM-4X8dI35OD0Vc7dBjMIJWHexw5wBe2WVgnTbUAqtEA-sOIQ7gTMQVWzXbNjKeqqtyfu7mqs-WQklAtPL_QeP3JyDfpIThNpyPpgRJ9h_Cc62XAp1qK-z3kX2zNlm6GoQBG5XInRuNy3UhICfcB5iLVTxP_jNu3Rrsv-LtJiYeOmXgXSKRDt_rqd5wC4EQwpji91hCRrPMQy2XZ3UWpvxv9C3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=U2zV4KJldfgGtaUCbdE1ix9rU-2ijmSj-cXFgv-bsPoCv2q7PCKLhvUixKRnhsXFJQHSLXoZWq8UaUrsp_Z-9LoWoZBX8SMLyfgN9KJVBrdiaXodIzV6EZ7eaSvvM-4X8dI35OD0Vc7dBjMIJWHexw5wBe2WVgnTbUAqtEA-sOIQ7gTMQVWzXbNjKeqqtyfu7mqs-WQklAtPL_QeP3JyDfpIThNpyPpgRJ9h_Cc62XAp1qK-z3kX2zNlm6GoQBG5XInRuNy3UhICfcB5iLVTxP_jNu3Rrsv-LtJiYeOmXgXSKRDt_rqd5wC4EQwpji91hCRrPMQy2XZ3UWpvxv9C3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچستریونایتد توسط برونو فرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106178" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106177">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=lvvJYDNSa11CxgeMDLPNMVS6Sn6cuSbffQLpJY7hR7YHpid4mlc5iXMf9bQrKoPUwgBcJ73HBNiceGVcOBLSBVZLyVKXh7S8EqIapL502KAC6CljPk2VvsHGVsqMNmwkD95fMLBE_2CbIjNfHJV_0K_iTCUnjvPdsoagjsJWIy-bQNvYHkE2d_kXUhCdMXDcr12VS4NgB2sokY7XFrGS4haThiMIl2juoJZFa0FPW5Ghjoy5h7HUxJsR9VA12DeoNA6Y5pAPtvReLqI-wXy53LiU1hRBTZJMMwwrYnqOMbOcKiwJKhS1VwbU0q_S1kgrOyz-AlGqFxykE2SYvef-FHo2AI98G9mg8RbIZqCHdTHUQZatmiT-JRInueeIDf_MD95ITnVZ9BEEM-fIeBoEHaW2Rao4at2G5xt6XzfFvfohWhpZfRy3y6sC0kMu6VtGp4V2qdvkT9YZsMRY5gtrkpIv_xNgz91F6IrSLHl4ytfJ8V0ojI31rSKGVMvTSEvtldAW2a3AfhX8oDS0nHV115hqTTRuPH3B8rHCQfgwlTfnhSsLqtTw84g32m51wJnCeheR_Ork5bCdrhKZgka4c6B5Je_N1IVFtihkKB6boMdB6S5EwYqeterEQjfPKs80cfP9gjnHZbDcVC-Wu8HEWH21QkgOw11jJrZrkA121to" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=lvvJYDNSa11CxgeMDLPNMVS6Sn6cuSbffQLpJY7hR7YHpid4mlc5iXMf9bQrKoPUwgBcJ73HBNiceGVcOBLSBVZLyVKXh7S8EqIapL502KAC6CljPk2VvsHGVsqMNmwkD95fMLBE_2CbIjNfHJV_0K_iTCUnjvPdsoagjsJWIy-bQNvYHkE2d_kXUhCdMXDcr12VS4NgB2sokY7XFrGS4haThiMIl2juoJZFa0FPW5Ghjoy5h7HUxJsR9VA12DeoNA6Y5pAPtvReLqI-wXy53LiU1hRBTZJMMwwrYnqOMbOcKiwJKhS1VwbU0q_S1kgrOyz-AlGqFxykE2SYvef-FHo2AI98G9mg8RbIZqCHdTHUQZatmiT-JRInueeIDf_MD95ITnVZ9BEEM-fIeBoEHaW2Rao4at2G5xt6XzfFvfohWhpZfRy3y6sC0kMu6VtGp4V2qdvkT9YZsMRY5gtrkpIv_xNgz91F6IrSLHl4ytfJ8V0ojI31rSKGVMvTSEvtldAW2a3AfhX8oDS0nHV115hqTTRuPH3B8rHCQfgwlTfnhSsLqtTw84g32m51wJnCeheR_Ork5bCdrhKZgka4c6B5Je_N1IVFtihkKB6boMdB6S5EwYqeterEQjfPKs80cfP9gjnHZbDcVC-Wu8HEWH21QkgOw11jJrZrkA121to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچستریونایتد به صباح توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106177" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106176">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=XcDBDeOaUB8b-dAOAPWN9wl_LlTe3KPelq68IJJUgzGyWrR0qNN-nk7GX6cPkuSCjNq0nrmz_Ra94v3iwxeQvQwG9gek02lRjDZBve3u9QhHBVL4ULwu_8Fvg_EtS5MFzQ1nEeCtWqfnmE9zTNjj7kqBznZXD4T4MoXztgFktUrmnnEAOG90JrpYRoYm-r2i9-DZeVqKw95Qdh6yOnIdZj-AwSxgNCm4stFIiJmaQfvky24FW7hICz33Mbis7Kyod2hiO7za5QOzHu8W7IfPvR_uOY3g4eRCdytG9NtdyvRWVXZA1LHVTIWF8uk8-ywOXC7n3l3FQkg88UcgyzA5Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=XcDBDeOaUB8b-dAOAPWN9wl_LlTe3KPelq68IJJUgzGyWrR0qNN-nk7GX6cPkuSCjNq0nrmz_Ra94v3iwxeQvQwG9gek02lRjDZBve3u9QhHBVL4ULwu_8Fvg_EtS5MFzQ1nEeCtWqfnmE9zTNjj7kqBznZXD4T4MoXztgFktUrmnnEAOG90JrpYRoYm-r2i9-DZeVqKw95Qdh6yOnIdZj-AwSxgNCm4stFIiJmaQfvky24FW7hICz33Mbis7Kyod2hiO7za5QOzHu8W7IfPvR_uOY3g4eRCdytG9NtdyvRWVXZA1LHVTIWF8uk8-ywOXC7n3l3FQkg88UcgyzA5Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
بازی استقلال ـ پیکان، داغ ذوبی‌ها در دیدار با پرسپولیس را تازه کرد؛ باشگاه ذوب‌آهن نوشت: دلیل مصونیت تیم پرسپولیس چیست؟
❌
⚠️
باشگاه ذوب آهن: دو صحنه در یک نقطه از محوطه جریمه و در یک ورزشگاه
🟢
یکی امشب، چک شدن صحنه توسط وار و اعلام پنالتی به دلیل بی احتیاطی مدافع. دیگری سه شب پیش، خاموش کردن VAR و چک نشدن صحنه به بهانه پایان بازی و اعلام نشدن پنالتی و دقیقا همان بی احتیاطی مدافع پرسپولیس و ضایع شدن حق ذوب‌آهن برای بار چندم تا هفته ششم لیگ برتر
🟢
⁉️
قضاوت با شما؛ چه کسی پاسخگوی حقوق از دست رفته ذوب‌آهن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106176" target="_blank">📅 23:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106175">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهارات خداداد عزیزی علیه فدراسیون فوتبال: پول ندادند، VAR آفساید را تشخیص نمی‌دهد
🔴
فدراسیون پول شرکتی که VAR را آورده نداده و VAR اصلا آفساید لاینشون کار نمی‌کند و نمی‌توانند سر صحنه های آفساید تشخیص بدهند.
🔴
آقای فدراسیون چرا خط کشی نکردی صحنه رو؟ شما وجود ندارید اگه راست میگید بیایید خط کشی کنید و نشون بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106175" target="_blank">📅 22:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106174">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge4LT1pMA7WFf38aeG1kfgkngQAOUIzrhcAeUwagVMY1D1eZG10jsGljCNhnZxxeOff7ca-hmet59zsc7uFWx10nzrNQpy8mYzxBwmgSPSpvtJyMJPqtyoC_AU4-TGoMznUcnd7yubnM00RkbJkLmCAM1_BVm9B3sfDICGsZL2BQsc_WIsgjCzACRf1mCo66-oqASA9d90L_BNb9YWHE5RPy3W8O2uOyNlGAzer9LATg0Wtt3CwnQ7bFeuMPgSSXVa5nR1CMOAoo0nlBbZ4VjfHTK2pvbD-sChJcJaOLJf-Jv5_BzhRk1Vu3iIt1SKFVzvT9pxkX32DoaBf795Po0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
‼️
واکنش خداداد به داوری بازی تراکتور و اس.خوزستان: تبریک به فدراسیون و کمیته داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106174" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106173">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
❌
🇮🇷
🇮🇷
بیزاتی مربی استقلال:  دلیل لغو بازی رقبا را نمی‌دانم؛ شاید چون بازیکنان پرسپولیس قرار است بروند تیم ملی، بازی آن‌ها لغو شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106173" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
