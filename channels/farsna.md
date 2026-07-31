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
<img src="https://cdn4.telesco.pe/file/f-_UzI3bKAlnbEwH0HK9GCMvbZ9Mcw0fOHGJacI47gkEtouPBGNRVY2T_gqXOyQtOjEdAxtsERi6TmZHDZUJuqlIdGQ9jEmemFAZ1i_6BJZ5zb3Vtz1U_pT8A9FDws2PaSrd4K5Abob2EpKRQErxBNRA8iNEheUbyFY51tTwXeqZ4MU4mDd7hZl8jAU7QgwxZVeBE26j22DqEOzv3sykp_3PJCv6bi_RR5Q-M63S_4q-KyGWNCJRnZ4hwddMfxjfdXdOrYkdqrAqxaYExZQUYyr3xfQAd0BsTY0-2bnq7ZAEqCwoAmIJ1EwU374wpEm575N3d6WCW6P-qACWiGlztA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 09:26:41</div>
<hr>

<div class="tg-post" id="msg-453678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30549b220.mp4?token=u-dD2qR8QyELxRPJ8ucclH4ZINZWFosfjQV5bCOTRisbWwEpmBNa2fN6_03n-c1ZR5L7bAEnJBYgRrE53jyAKhJKVFsmlEhOiKQIzf8XvOMlBeRl1M8vwt182S7LcQJ9xsFh5gBKM-OC1yIug72gnQECW_bYrRwr36dIaRrz5qADHEemlzi4a9nK5ufnW5naPWtKw3ucYdFhudKo21rd-I-I6oknxR52eku9hRJ_euwPWzctK_tGzMq987ENM8jEbey-aWeQXYyo9Fo4lk6KJW0VBoYX_6l60B4n3w_kSi-Mz40Q-bO9L-bBwaOKrdk5RawP7kxE0hD76D8MTRvRyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30549b220.mp4?token=u-dD2qR8QyELxRPJ8ucclH4ZINZWFosfjQV5bCOTRisbWwEpmBNa2fN6_03n-c1ZR5L7bAEnJBYgRrE53jyAKhJKVFsmlEhOiKQIzf8XvOMlBeRl1M8vwt182S7LcQJ9xsFh5gBKM-OC1yIug72gnQECW_bYrRwr36dIaRrz5qADHEemlzi4a9nK5ufnW5naPWtKw3ucYdFhudKo21rd-I-I6oknxR52eku9hRJ_euwPWzctK_tGzMq987ENM8jEbey-aWeQXYyo9Fo4lk6KJW0VBoYX_6l60B4n3w_kSi-Mz40Q-bO9L-bBwaOKrdk5RawP7kxE0hD76D8MTRvRyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیشترین پرچمی که در اربعین دیده می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farsna/453678" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae415fca5.mp4?token=NZLDH5Lu5rLMJI0VTcLH8FAocn-WwNwO-LnOMOov5LvU0jtMFsGuil600w9U83hPKG6QBqmdO2bcDN_4jCpys-FAGSmxAR3gi09d8pcrZsdL1PjcmcTfozqESb7dsYRkn0SVmYctQXa0Y9ixR58KN83tJMpF54-mhh2OvtFhqmj9eghcBF5_Orm9SyP-yvZGZPrcXh0Cia7qzdhupducBJ4mwnc-gqSMuGSUThjfqRh8jkXXDnLH0a1baovlnL8X5IXWEa4Qz0ykPpYNiFJgOrwncPpReY8FzsIBUguas-2HE_wa9bmjkozjJYF8J3YEX67KHt-C3WGjTkooSL20p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae415fca5.mp4?token=NZLDH5Lu5rLMJI0VTcLH8FAocn-WwNwO-LnOMOov5LvU0jtMFsGuil600w9U83hPKG6QBqmdO2bcDN_4jCpys-FAGSmxAR3gi09d8pcrZsdL1PjcmcTfozqESb7dsYRkn0SVmYctQXa0Y9ixR58KN83tJMpF54-mhh2OvtFhqmj9eghcBF5_Orm9SyP-yvZGZPrcXh0Cia7qzdhupducBJ4mwnc-gqSMuGSUThjfqRh8jkXXDnLH0a1baovlnL8X5IXWEa4Qz0ykPpYNiFJgOrwncPpReY8FzsIBUguas-2HE_wa9bmjkozjJYF8J3YEX67KHt-C3WGjTkooSL20p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ‌جا کربلا نمی‌شود
!
🔹
روایت دلدادگی زائران کربلا را از دریچه دوربین خبرگزاری فارس ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/farsna/453677" target="_blank">📅 08:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae919478b.mp4?token=QJ3oUSjf-NRm2G4Q3tRjCKwPvlY2-P6HNsXLvOu-I5q4_ADvNrGU23ppQ8BMoVV9eCtqpAgZw5XvxMlgJHCK4sCf7x7QXxqHdZEQNX_mopoc1zbw6GOlPy-rLNf0bPfJrZsvPSqK9omkkuvurYeydUqcaSNH9b-htaoEqCRZHFFpNTGAeAViAtuW288RU8weSp9ZlKEn2BKBzuyrWK5IEMm5RLwBNmyr4z9H6iDbAbTJknE8TbFF78jxfn9tiPQSAiH4KUls5-Mvj6uRyFxVeaEbo1t0kCRVAAKhfOKFwVoSZ1ljMRtZEUkgCkZlYjBuSTO0vQat5DaXmupzp6DzipX1yV82IimUsMOxsWiLy7F6ymDHr6AKYPFAdrRnD-OhCHPLljutko7i49Q6LW7MetR87oMDtFUK1ERVhz8SNOgc497JH97RXhl0Nb7azfFprBbwZBW4ArOHgxOG6V0Ux9caEAUOf7DDsuhfgVOSz--qwP_LLgYzFV1wHLYE7vAiBK-a7ux6DeotdCSUv_9wQhVkK0vbkPrOwI42Otah7fok7u4k4wOi_6qhr3kclc8UXFVmGWpiorslO_yywLSQhBLRiE_AvB0OhQJRcCrswLDCFk6cMf7tlQrdXxRnGIVsDfk4I6VAT72SU6YuQTqTDIIujccSSQFrGE7QmVG2I0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae919478b.mp4?token=QJ3oUSjf-NRm2G4Q3tRjCKwPvlY2-P6HNsXLvOu-I5q4_ADvNrGU23ppQ8BMoVV9eCtqpAgZw5XvxMlgJHCK4sCf7x7QXxqHdZEQNX_mopoc1zbw6GOlPy-rLNf0bPfJrZsvPSqK9omkkuvurYeydUqcaSNH9b-htaoEqCRZHFFpNTGAeAViAtuW288RU8weSp9ZlKEn2BKBzuyrWK5IEMm5RLwBNmyr4z9H6iDbAbTJknE8TbFF78jxfn9tiPQSAiH4KUls5-Mvj6uRyFxVeaEbo1t0kCRVAAKhfOKFwVoSZ1ljMRtZEUkgCkZlYjBuSTO0vQat5DaXmupzp6DzipX1yV82IimUsMOxsWiLy7F6ymDHr6AKYPFAdrRnD-OhCHPLljutko7i49Q6LW7MetR87oMDtFUK1ERVhz8SNOgc497JH97RXhl0Nb7azfFprBbwZBW4ArOHgxOG6V0Ux9caEAUOf7DDsuhfgVOSz--qwP_LLgYzFV1wHLYE7vAiBK-a7ux6DeotdCSUv_9wQhVkK0vbkPrOwI42Otah7fok7u4k4wOi_6qhr3kclc8UXFVmGWpiorslO_yywLSQhBLRiE_AvB0OhQJRcCrswLDCFk6cMf7tlQrdXxRnGIVsDfk4I6VAT72SU6YuQTqTDIIujccSSQFrGE7QmVG2I0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله صفایی بوشهری: قصاص جنایتکاران بزرگ وظیفهٔ همهٔ مسلمانان جهان است
🔹
هر مسلمانی که شرایط و توان این را دارد که قصاص خون رهبر شهید را بگیرد باید دست‌به‌کار شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/453676" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp2I9cm93nA2nCbwoq9sCPNHzcGLjbR0HOBSPoGianPkClgcTxoQ928fnFb70h9JDxKy_NDmMg6QinEwW1ml_Ss5om9WAlKjTL1KVj4WH3MCt47qw0jDfLzXVSYPE-Ki2KYNV7Qtlc7EHLnZKFiQqSf0DDUjnwfZ5Q8KRKN3ZcuW0lrDYRJm5r8cufBbDBC2WyA535yaGpE20c6kzv-UU4AEnF-bD0G_XdZ4f6XTNLMDwTTAhqZ-iJMkhhD_ZFvoEawmWU4O5071jgnypTQ1TBtbr66_sGfU1zIUr07MCWZ0glahJjz_I4XGv54ncs5Y6FwZiZYpNwycw0_qC2n84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان سفیرش را از کابل فراخواند
🔹
روزنامهٔ «نیشن» پاکستان: اسلام‌آباد در واکنش به تحولات امنیتی افغانستان، سفیر خود در کابل را برای انجام رایزنی‌های سطح بالا فراخوانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/453675" target="_blank">📅 08:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1b6f1ea1.mp4?token=TGNcF0hmydyRQW8i7eQW6k_9NFIqzjrI_EZE5H2J6jXz-UfUQDGmN3kqznzeT7rV_Ok2gvtNY6E6nb5K0EJtCm85LffDlfpwHbxdDREIWqtKjpvcNyg_eeCE5mPU_WwuiiYTSPt_jBSnyfwoyGImw5r3dSzfnASR5tKnzEkCG7HX2O_PeQOO5eUKyMsHwwJXFVjIczXjwZ2AHnjmn95IDfSbjELP_6WNjtP3OdpfOSw0LyWc1qqSsiGCcWUNB-hPSMjql2JVuY5YtjlKbMaKiLUlkyHnO31VmPB3-PlqEH0ml5x3nl58Fh5lvtchfhuaglWLiQOTogIFipc1jpxu7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1b6f1ea1.mp4?token=TGNcF0hmydyRQW8i7eQW6k_9NFIqzjrI_EZE5H2J6jXz-UfUQDGmN3kqznzeT7rV_Ok2gvtNY6E6nb5K0EJtCm85LffDlfpwHbxdDREIWqtKjpvcNyg_eeCE5mPU_WwuiiYTSPt_jBSnyfwoyGImw5r3dSzfnASR5tKnzEkCG7HX2O_PeQOO5eUKyMsHwwJXFVjIczXjwZ2AHnjmn95IDfSbjELP_6WNjtP3OdpfOSw0LyWc1qqSsiGCcWUNB-hPSMjql2JVuY5YtjlKbMaKiLUlkyHnO31VmPB3-PlqEH0ml5x3nl58Fh5lvtchfhuaglWLiQOTogIFipc1jpxu7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اصابت پهپاد انتحاری به پایگاه تروریست‌های ضدایرانی   @Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/453674" target="_blank">📅 08:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLaaq5rwNS45udjP9BfkFjp3WKjAFXrB4hzh__rPELM1PURH2_-XvjYgpywGRaE2ZciWbSu8nRRIJeNbd45sD4h1Up0dpsVT3jeUTRCiltfeGymrbPd_4GoaSKamMFdk28bp7JXDxVPWnDgzNWPG3nWwecak7k65ean970Yt0RDeNobdSbS-Pl0LldH119PGMmsqvnSnwt3b73mdvgiQBC5eipMa76eaf-1FSVWobqnmBatCeLkitr4lP3SLt0NP6nraNzs83p0ap8qLhUOf1LKJdGwA5_QUa3uVDX9o4unzcxIwjqghDP5FRlisIfJUBb_CxykC91wtko4sBT3wzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیمارستان تخصصی صحرایی سپاه در مهران به خدمت زائران درآمد
🔹
فرماندۀ سپاه امیرالمؤمنین(ع) استان ایلام: این مرکز درمانی مجهز با حضور پزشکان متخصص تا پایان اربعین آمادۀ ارائه خدمات درمانی به زائران می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/453673" target="_blank">📅 07:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972d98a60d.mp4?token=mwVLNJsWXQIY5Pf8WsjQckD-5LB39rIE1yzKvGauwOa673tBMRC-Cq85yG2XD-CZIZmjqu7N5xGAS32Ki9JaaooSue88j4ahoiQtsw0s9fF65jJtEFSMAe0XP18BxB_YNp6zkjh7onUClJ8pk1eX6E8iprZPdUFq2D0UA5K1cLyPj3-JZ-cnCghpkIgGfyszAZeeR1hcBN4qunfX9iO5OgWkrMniNvIeRNhgJhdbNrf7C4d-ZCIzpyI6VYLlHYldQyS9z8L8b0u1xai-XqvEeLr0OuCBDWuh8i5VY51kgYZmpUVWgcXteA0_mA0kiyWaC2FoQayj9J-VtySmzlW4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972d98a60d.mp4?token=mwVLNJsWXQIY5Pf8WsjQckD-5LB39rIE1yzKvGauwOa673tBMRC-Cq85yG2XD-CZIZmjqu7N5xGAS32Ki9JaaooSue88j4ahoiQtsw0s9fF65jJtEFSMAe0XP18BxB_YNp6zkjh7onUClJ8pk1eX6E8iprZPdUFq2D0UA5K1cLyPj3-JZ-cnCghpkIgGfyszAZeeR1hcBN4qunfX9iO5OgWkrMniNvIeRNhgJhdbNrf7C4d-ZCIzpyI6VYLlHYldQyS9z8L8b0u1xai-XqvEeLr0OuCBDWuh8i5VY51kgYZmpUVWgcXteA0_mA0kiyWaC2FoQayj9J-VtySmzlW4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراکز راهبردی آمریکا در کویت هدف پهپادهای ارتش قرار گرفت
🔹
ارتش: در بیست‌وهفتمین مرحله از عملیات صاعقه و در پاسخ به تجاوزات اخیر ارتش تروریستی آمریکا به کشورمان و حملۀ وحشیانه به منزل مسکونی در جزیرۀ قشم، ساعاتی قبل، آشیانۀ جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات این ارتش کودک‌کش در پایگاه احمدالجابر کویت، هدف پهپادهای انهدامی ارتش قرار گرفت.
🔸
پایگاه احمدالجابر کویت، نقش عمده‌ای در عملیات های هوایی و نظارتی آمریکا ایفا کرده و فراتر از نقش عملیاتی، از کانون های حیاتی پشتیبانی هوایی برای ارتش تروریستی آمریکا محسوب می‌شود.
🔸
حملات قاطع، گسترده و پرحجم ارتش و سپاه، رهگیری پهپادها و موشک‌های ایران را برای دشمن با وجود بکارگیری پیشرفته‌ترین سامانه‌های پدافندی و تقویت آن، بسیار پرهزینه و دشوار ساخته، و دشمن خبیث مجبور است با سانسورهای شدید، مانع انتشار اخبار آسیب‌ها، کشته‌ها و مصدومان شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/453672" target="_blank">📅 07:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f6a42e11.mp4?token=tRyV8sOZs5lM_uFYH6aTOFvqLToPxyyMKLzHzBh4ZsVoG_lTM25C18wMbbZHuWcvom2tf-rXQNijIlbs5aoOH8QcM9Eg3n1f0J6FE_7if4o4QzGU7wFOlHQLbyKFa4M2Z2N4OXepozROPjwIIYiFbnffIftQWO8Da6gh6oADfJJLwL5i_kaovN48a0vv6DKodas9Sme4d2jxU_D6LkN2feuaEJDLR2DeovvyR04KnfbIc6wM8wxVc0xedcVLEGaNYap4xVc7YwpUhbgYSAaws_vRmycELHXnKZMnrM-vzqHxjjXBOy63BT2zVp39zhBemH3OGu3dH1UZd5QdG56PsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f6a42e11.mp4?token=tRyV8sOZs5lM_uFYH6aTOFvqLToPxyyMKLzHzBh4ZsVoG_lTM25C18wMbbZHuWcvom2tf-rXQNijIlbs5aoOH8QcM9Eg3n1f0J6FE_7if4o4QzGU7wFOlHQLbyKFa4M2Z2N4OXepozROPjwIIYiFbnffIftQWO8Da6gh6oADfJJLwL5i_kaovN48a0vv6DKodas9Sme4d2jxU_D6LkN2feuaEJDLR2DeovvyR04KnfbIc6wM8wxVc0xedcVLEGaNYap4xVc7YwpUhbgYSAaws_vRmycELHXnKZMnrM-vzqHxjjXBOy63BT2zVp39zhBemH3OGu3dH1UZd5QdG56PsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای جدید از آسیب به بخش نظامی پایگاه «علی السالم» کویت
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/453671" target="_blank">📅 06:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال‌استریت‌ژورنال: آمریکا کاهش حضور در کویت را بررسی می‌کند
🔹
روزنامۀ وال‌استریت‌ژورنال گزارش داده که ایالات متحده آمریکا در پی تحولات جنگ علیه ایران در حال بررسی گسترۀ حضور خود در کشور کویت است.
🔹
اقدام آمریکا در حالی انجام می‌شود که مقام‌های کویتی اعلام کرده‌اند که همچنان نیازمند تعهد قاطع آمریکا به حمایت از کشور خودشان هستند.
🔹
به نوشتۀ این روزنامه، تأسیسات و پایگاه‌های آمریکایی در طول جنگ بارها هدف حملات ایران قرار گرفته‌اند.
🔹
تحلیل‌گران می‌گویند آنچه به احتمال زیاد باعث تغییر در این روابط خواهد شد، درک این واقعیت از سوی آمریکا است که حضور نظامی دائمی و بزرگ در کویت دیگر حیاتی یا از نظر نظامی عاقلانه نیست.
🔹
مقامات فعلی و سابق آمریکایی مدعی شده‌اند پنتاگون حتی قبل از آغاز جنگ ایران نیز در فکر کاهش نیروهای خود بوده است.
🔹
مقامات آمریکایی به وال‌استریت‌ژورنال گفتند پنتاگون در پاسخ به حملات موشکی و پهپادی ایران به پایگاه‌های آمریکایی، حضور خود را در کویت کاهش داده تا ریسک را به حداقل برساند.
🔹
طبق گزارش این روزنامه مقام‌های کویت مانند دیگر کشورهای خلیج‌فارس از این‌ که ترامپ جنگی را بدون مشورت آنها آغاز کرد که آن‌ها را در تیررس قرار داد، ناراحت و آشفته شدند؛ حسی که با طولانی شدن منازعه و بلوکه ماندن صادرات نفت شدیدتر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/453670" target="_blank">📅 05:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع چند انفجار شدید در استان دهوک در شمال عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/453669" target="_blank">📅 05:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453668">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4792668f.mp4?token=DMmGNvIUs0yuZcqOYi94lZUym5XvSQHvN1w7es8WTvEnNTfIl-zrS1x3PQDKfjOpd0hXkbFIuXFbfSXglMv6Z3yR5w9_4wjafnJapgybwT9YGNSRCgj-YqU9aVkbuQxfei7A0S1k8RfCpeb8th9iEj7o1zcuCYpemvIozKd5KNSZ-t-M05VzL2AVWH_kykHdm6F2kiu5Furtm7Swa7gdsUTVysE0lzWQutveaTShwkIr4_ZJH1AP78FIBuXCQEXtu4EYjRG2soqyuyTgyOzMfNZ8_ioOir_KsUZzJFMgNoca9-TxX9yb1oOMhIdYAc_RHl7xbE034P-3nw1wxkzQ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4792668f.mp4?token=DMmGNvIUs0yuZcqOYi94lZUym5XvSQHvN1w7es8WTvEnNTfIl-zrS1x3PQDKfjOpd0hXkbFIuXFbfSXglMv6Z3yR5w9_4wjafnJapgybwT9YGNSRCgj-YqU9aVkbuQxfei7A0S1k8RfCpeb8th9iEj7o1zcuCYpemvIozKd5KNSZ-t-M05VzL2AVWH_kykHdm6F2kiu5Furtm7Swa7gdsUTVysE0lzWQutveaTShwkIr4_ZJH1AP78FIBuXCQEXtu4EYjRG2soqyuyTgyOzMfNZ8_ioOir_KsUZzJFMgNoca9-TxX9yb1oOMhIdYAc_RHl7xbE034P-3nw1wxkzQ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع محلی از آتش‌سوزی گسترده در پایگاه‌های تروریست‌های ضدایرانی در اربیل گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453668" target="_blank">📅 04:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c17263c56.mp4?token=seIoxXERr8OZT6u1N0pjyHpnrDi6y3lkA9qGqugTtoTPgnUV3HL5LdL2LlYfqOcFjeAidfKRqx6NbXVNrtNwwRcZk-3tXeE7lMY_TXbI4D1tKXZi2vst6gO2Zdykm0JkR5SNnbmeTKKECTT6XemUi-wwPGei5PPSXkweIXd5X2HOs4dH2yrcaGMkWSU4AWV2CmFvmztkOu8XUyOp1Jp_iwtzKDmfM1a9A8W7dcv2xPtzMK6nAUXs7bE0Kl9CgntKbGlwbEo4rdACNkicm6qJE7H37mIogaEjENsg-mjLzaa7fOSKA3ADsBCI4ioE5jdUwbPBrTbtMqnqv3NZCHCrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c17263c56.mp4?token=seIoxXERr8OZT6u1N0pjyHpnrDi6y3lkA9qGqugTtoTPgnUV3HL5LdL2LlYfqOcFjeAidfKRqx6NbXVNrtNwwRcZk-3tXeE7lMY_TXbI4D1tKXZi2vst6gO2Zdykm0JkR5SNnbmeTKKECTT6XemUi-wwPGei5PPSXkweIXd5X2HOs4dH2yrcaGMkWSU4AWV2CmFvmztkOu8XUyOp1Jp_iwtzKDmfM1a9A8W7dcv2xPtzMK6nAUXs7bE0Kl9CgntKbGlwbEo4rdACNkicm6qJE7H37mIogaEjENsg-mjLzaa7fOSKA3ADsBCI4ioE5jdUwbPBrTbtMqnqv3NZCHCrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع محلی از آتش‌سوزی گسترده در پایگاه‌های تروریست‌های ضدایرانی در اربیل گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453666" target="_blank">📅 04:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
منابع عراقی از حملات جدید به مواضع تروریست‌های تجزیه‌طلب در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453665" target="_blank">📅 04:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTUPZh9S7OnjztqlARi6EuiYymccbvYyPy-UNZ1ik8OciXZFOvShF0EkLSU7U8hbt-oExXnNU4z7N5PvgsajR2bPdii8xbECJBV1ypqzIBFxe9wGKeQe2qG27mM7P_knHYnBvxtnY27X_YUNRqZs76S29PnOEzp5srzjORAVe6LQy9iCeZGMT4MxZVqfoGmE0ys3Tq1P7ai5-WD_U3HROcJJK5er_e68Od0iXav8Bm0VcO9FJW-DmaDOXmrQ1E3vGA-yJS8s6l1z-_j5L_xxS_WhfyTK8lxr3CyPQgpdMpTRy5_0cWlkFWlJvLNc-FD26kiGtv4F-TXKur_ScRhoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صهیونیست‌ها با ۷۰۰ تن بمب جنوب لبنان را بمباران کردند
🔹
بنیامین نتانیاهو و اسرائیل کاتص وزیر جنگ رژیم صهیونیستی در بیانیه‌ای مشترک مدعی شدند که ارتش اسرائیل سیستم تونل‌های حزب‌الله در زیر منطقه کوهستانی بوفور در جنوب لبنان را منفجر کرده است.
🔹
همچنین آن‌ها مدعی شده‌اند ارتش اسرائیل برای تخریب این تاسیسات زیرزمینی از ۷۰۰ تن مواد منفجره استفاده کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453664" target="_blank">📅 02:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35df706702.mp4?token=gCO6z7dfM5HpGJE7Xfyu865TKvNbVD-yPTW3qZsMFIIfjQR3ugZQqnzCPQspNcNqL7nTnpT7ZgutR1Fb-N3nxMNyzUUaPLhxGoJIe-bMjtZthc21aSpwIg-e5txr3lw96mfvVDA_UvGSYT-jHvFgJkAEWoUeo2jvfZdCUP5rBYlRiUcN_0b_ee86_X5p1ly2WU8raHzBvoEflRYBtDs_NBe1dNVTS3J9wEvuA7HT8OUyWOQXlYu0cdmvfP0ypbCJgOBv2YkYqgtxd7e0TrlqNOEj5hcCMmhjpXaD1_OaQiHgs3ZaF-KnlH1sK-BoMIqtPLJoJcRRZQhpoRexkLjQnZ_7e6ycJkrVgieZJT--zSqXDe0ahastur8Qq78PYFdXaXXEtts4rtzqVk4TrSDMDvBjw6r7LiZ2i3y6F_W0UbtsnNZ6GHJXZthBe5OMgzy_EOlcdRRh-CwV6YFan7NVmAiibFLs21FNrdzaUdkOP40DoLrMIB_vYyh8-f87IKZMiXSz0p3uNiZ8iK-6WgtX5UC5BbdPVE-S1aAtqYXoGa-TrdJcqbv9PMGWci4p_LesFa9mttWeuKpktnSc2DK91burIbsk1XyS9uf0-ZEutDI-Bb0vd2XywMF-lD8XR-IXrGeipfKTdj3Kp0Po6ZT26s8m_lIdbhkUqtIYrR4o0TU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35df706702.mp4?token=gCO6z7dfM5HpGJE7Xfyu865TKvNbVD-yPTW3qZsMFIIfjQR3ugZQqnzCPQspNcNqL7nTnpT7ZgutR1Fb-N3nxMNyzUUaPLhxGoJIe-bMjtZthc21aSpwIg-e5txr3lw96mfvVDA_UvGSYT-jHvFgJkAEWoUeo2jvfZdCUP5rBYlRiUcN_0b_ee86_X5p1ly2WU8raHzBvoEflRYBtDs_NBe1dNVTS3J9wEvuA7HT8OUyWOQXlYu0cdmvfP0ypbCJgOBv2YkYqgtxd7e0TrlqNOEj5hcCMmhjpXaD1_OaQiHgs3ZaF-KnlH1sK-BoMIqtPLJoJcRRZQhpoRexkLjQnZ_7e6ycJkrVgieZJT--zSqXDe0ahastur8Qq78PYFdXaXXEtts4rtzqVk4TrSDMDvBjw6r7LiZ2i3y6F_W0UbtsnNZ6GHJXZthBe5OMgzy_EOlcdRRh-CwV6YFan7NVmAiibFLs21FNrdzaUdkOP40DoLrMIB_vYyh8-f87IKZMiXSz0p3uNiZ8iK-6WgtX5UC5BbdPVE-S1aAtqYXoGa-TrdJcqbv9PMGWci4p_LesFa9mttWeuKpktnSc2DK91burIbsk1XyS9uf0-ZEutDI-Bb0vd2XywMF-lD8XR-IXrGeipfKTdj3Kp0Po6ZT26s8m_lIdbhkUqtIYrR4o0TU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاجر اندونزیایی از آثار عجیب بستن تنگۀ هرمز می‌گوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453663" target="_blank">📅 02:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ادعای رسانه‌ها درباره موافقت حماس و گروه‌های فلسطینی بر سر سلاح‌های مقاومت
🔹
شبکه خبری الجزیره و المیادین ادعا کرده‌اند به پیش‌نویس سندی دست یافته است که نشان می‌دهد حماس و سایر گروه‌های فلسطینی در خصوص سلاح‌های مقاومت در غزه، به توافق رسیده‌اند.
🔹
طبق ادعای…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453662" target="_blank">📅 02:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453661">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای رسانه‌ها درباره موافقت حماس و گروه‌های فلسطینی بر سر سلاح‌های مقاومت
🔹
شبکه خبری الجزیره و المیادین ادعا کرده‌اند به پیش‌نویس سندی دست یافته است که نشان می‌دهد حماس و سایر گروه‌های فلسطینی در خصوص سلاح‌های مقاومت در غزه، به توافق رسیده‌اند.
🔹
طبق ادعای الجزیره این پیش‌نویس بر آغاز فرآیند جمع‌آوری و انبارسازی تسلیحات سنگین، مراکز تولید نظامی، زاغه‌های مهمات و تونل‌ها تأکید دارد.
🔹
طبق این پیش‌نویس، فرآیند جمع‌آوری و انبارسازی سلاح‌ها پس از اجرای کامل تمامی تعهدات باقی‌مانده از پروتکل شرم‌الشیخ آغاز خواهد شد.
🔹
در این پیش‌نویس، شروع فرآیند جمع‌آوری سلاح به ورود «کمیته ملی» و استقرار «نیروهای بین‌المللی تثبیت استقرار» در نوار غزه مشروط شده است.
🔹
طبق پیش‌نویس، گروه‌های فلسطینی در فرآیند جمع‌آوری و انبارسازی سلاح‌ها مشارکت خواهند داشت.
🔹
در پیش‌نویس تأکید شده است که هیچ سلاحی به اسرائیل یا هیچ طرف غیرفلسطینی دیگری تحویل داده نخواهد شد.
🔹
پیش‌نویس توافق، مدیریت پرونده سلاح را به یافتن مسیری موثق و قابل اعتماد به سوی حق تعیین سرنوشت فلسطینیان و تشکیل کشور مستقل فلسطین پیوند داده است.
🔹
پیش‌نویس توافق، مراحل کنترل سلاح را به خروج تدریجی اسرائیل از مناطق تحت کنترل خود در غزه مشروط کرده است.
🔹
این پیش‌نویس مقرر می‌دارد که «کمیته ملی» تنها نهادی است که حق مالکیت، انبارسازی یا کنترل سلاح در غزه را دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453661" target="_blank">📅 01:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc030dfef.mp4?token=Vs1-tEeBKpYjubys7u00yC2ma_cVEbB7FO3oelAUoWXKS59HrZPd86BILkAqqQSpFcTGI30v-rS4707xLO1YcJ60YoHQMeK4QQpMr8JHQYCH-WcnwPeOmIRz3WtZj26HpjDXqWkY9q5-8zSS8L4OkAVdhWmq7izXMsOtKupsP9R4AmZ0-R6M3VxF_OUrSnOEy-x23Q8Lpg6zpfKWTuLPq57yGBJgBXOSPRVOma20Y1Q498eEPKQZZgbSoqIavws9LE58r1y47hEGFnhgyd0QI0rdwzFWk4xJ9_nbsBxhdXQR_FH0Q9oHoqR2yH6g-r71qXa9hZ3QX5XRVW9PoL10wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc030dfef.mp4?token=Vs1-tEeBKpYjubys7u00yC2ma_cVEbB7FO3oelAUoWXKS59HrZPd86BILkAqqQSpFcTGI30v-rS4707xLO1YcJ60YoHQMeK4QQpMr8JHQYCH-WcnwPeOmIRz3WtZj26HpjDXqWkY9q5-8zSS8L4OkAVdhWmq7izXMsOtKupsP9R4AmZ0-R6M3VxF_OUrSnOEy-x23Q8Lpg6zpfKWTuLPq57yGBJgBXOSPRVOma20Y1Q498eEPKQZZgbSoqIavws9LE58r1y47hEGFnhgyd0QI0rdwzFWk4xJ9_nbsBxhdXQR_FH0Q9oHoqR2yH6g-r71qXa9hZ3QX5XRVW9PoL10wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی مرز چذابه
🔹
تردد زائران اربعین حسینی در پایانۀ مرزی چذابه به‌صورت روان در حال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453660" target="_blank">📅 01:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دقت حملات ایران، آمریکایی‌ها را به تحقیق واداشت
🔹
دلیل حملات دقیق نیروهای مسلح ایران به مواضع دشمن آمریکایی در منطقه یکی از سوژه‌های گمانه‌زنی در رسانه‌های غربی طی روزهای گذشته بوده است.
🔹
پایگاه محافظه‌کار نیوزمکس در گزارشی نوشته که حملات دقیق ایران مقام‌های آمریکایی را به انجام تحقیقات دربارۀ نحوۀ ردیابی نظامیان این کشور وادار کرده است.
🔹
این پایگاه به نقل از یک مقام اطلاعاتی ادعا کرده که ایران ممکن است از فناوری‌های تبلیغات دیجیتال برای تعیین محل دقیق نیروهای آمریکایی در سراسر خاورمیانه استفاده کرده باشد.
🔹
رویترز هم روز گزارش داده بود عالی‌ترین فرماندۀ آمریکایی در خاورمیانه به نیروها هشدار داده است که فعالیت تلفن‌های همراه‌شان به ایران در انتخاب اهداف کمک می‌کند و ممکن است به‌زودی به برخی از نیروهای مستقر دستور داده شود که تلفن‌های همراه خود را به‌طور کامل تحویل دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453659" target="_blank">📅 01:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453658" target="_blank">📅 01:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsWVIqUZkn3IWqHm8a7Mbus-dwsKhtzAU31DHPukVf0YpfO37mj-FIO_JHf0eyM8QS63fhy29G355xuQO5Lj7ZIVWktotiuujO2WmMVZvplloVb8bi6QtWSvE2Y6paM2G_xu3J-Aa67HV1hsQ1u3QJiubwXopVIYX54K_MzbE3PoXScSgSbHVLsgA79bVJJkD2vbbCmNe_RIJvaU9llm8VkYkN0lifv86mvhAjeLPbc8ZuPYbjdAQ47xmyo-vY95DtIJgvA1YO8zmtn21InNc31PR07FEuNIYrl9pZk9HKDg52bnvOUZ8IM5aZjAR63_S9ObuZYbCasX7HMbVfqe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین آمار از تردد زائران اربعین
🔹
رئیس ستاد مرکزی اربعین: تاکنون حدود ۲ میلیون و ۷۰۰ هزار نفر از مرزهای کشور برای زیارت اربعین امام حسین(ع) خارج شده‌اند و حدود ۹۰۰ هزار نفر نیز پس از زیارت به کشور بازگشته‌اند.
عکس: دانیال همتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453657" target="_blank">📅 01:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=eWp5Fkce16schysUkDJjjn1bXoubUJ1SRYIU9RIVPDoQ3tkXKo4K3TmTYxafCbcfnfHxTFeVMliT4ibGyXxy9eZkAVU4U-Nvl9MfTFqeYRH0vlVk8J_ANbHkJDDheDU4dBZZYDOwSIbH6PVRc81cMxvhwxhCi-agD5WrWcwHMwBzWNWVpLEm6P8PrIeAGxuPGOaevNQneKlWa1XsBc15sLyLr1bBGv4a8yCqq4qjBzMGSqm8SG2_-CBpbPJffOxT-BfOKqtO0VbtFCA2SOgS6gYVsCZmZ1bcCtMyA5xymFYN9V9cVEDmDughKYy5IAymPRsW9Q384WyrUueWFxr2N51-l47L8XOwBNxb7juKvsi-pCYVDU2BCqH9QT6YpAOu0ZKm1hB5gW3DrI6BbjgxTDcS0RwcIJH-Hg3-rBGSsb2bTsaNg0T1U_jg2uMCny6WUNm6vlrG0QMsGU1EbLWiIvknFRgjtqRCNGcR7ePNR46Qp-xT7ZHSurW6VyUZtZp1gL1A1knaZOuXHSNxtIBed1sYuFrDqpfGxQhc3MxyzmAL5c15bltMrtseLRyih5ZJ4_mW3vSuW8PP1qeehdtwPUuXMcrilrfWRFprpKOXMentB3lhoALzbvRDB9rA-d_if1q1T-VEUMZVO6UsxgDf3DkgoJAhJkKtrvX36Rg4_Us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=eWp5Fkce16schysUkDJjjn1bXoubUJ1SRYIU9RIVPDoQ3tkXKo4K3TmTYxafCbcfnfHxTFeVMliT4ibGyXxy9eZkAVU4U-Nvl9MfTFqeYRH0vlVk8J_ANbHkJDDheDU4dBZZYDOwSIbH6PVRc81cMxvhwxhCi-agD5WrWcwHMwBzWNWVpLEm6P8PrIeAGxuPGOaevNQneKlWa1XsBc15sLyLr1bBGv4a8yCqq4qjBzMGSqm8SG2_-CBpbPJffOxT-BfOKqtO0VbtFCA2SOgS6gYVsCZmZ1bcCtMyA5xymFYN9V9cVEDmDughKYy5IAymPRsW9Q384WyrUueWFxr2N51-l47L8XOwBNxb7juKvsi-pCYVDU2BCqH9QT6YpAOu0ZKm1hB5gW3DrI6BbjgxTDcS0RwcIJH-Hg3-rBGSsb2bTsaNg0T1U_jg2uMCny6WUNm6vlrG0QMsGU1EbLWiIvknFRgjtqRCNGcR7ePNR46Qp-xT7ZHSurW6VyUZtZp1gL1A1knaZOuXHSNxtIBed1sYuFrDqpfGxQhc3MxyzmAL5c15bltMrtseLRyih5ZJ4_mW3vSuW8PP1qeehdtwPUuXMcrilrfWRFprpKOXMentB3lhoALzbvRDB9rA-d_if1q1T-VEUMZVO6UsxgDf3DkgoJAhJkKtrvX36Rg4_Us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ دشمن آمریکایی به دانشگاه اهواز از زبان شاهدان عینی  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453656" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtlqvNT0kvdacFtleQzHfJ7wnsPjic6LpW7VcicOghuA9UT5X_SosxJKT8rWb3t2gaMCpcRpDf0X8jIWjoPgnzYltLTZQwfvDXGOryJ7TyRkLo-p1PTNG-7UsBGMs1kyliRt7ov3cpB2vG3D21OFraOvmsb4vxszN-XhV2-S1YFLpZJ9TxjeKMi2AmibCkyYXidEJTayQEUC23wcp8Mg7pKqqUd7N3esXCRDKcuDOrO41GyLUWC8mBmuCWb8lS3ZKxYgoQifsWLM_zIG1rjnnRP0XvKFdR0R-lLktsLUdzZEipq10ORWgnY69Yb2e8xjHS9rs1FV5Yp55V3SGl5UJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
انفجار مهیب در باب‌المندب
🔹
منابع عربی از انفجار با صدایی مهیب در تنگۀ باب‌المندب خبر دادند.
🔹
به گفتۀ منابع خبری، این انفجار در حوالی یک کشتی با پرچم کامرون در میانۀ باب‌المندب رخ داده و این کشتی هم‌اکنون متوقف شده است.
🔸
بیش از یک‌ هفته است که یمن اجازۀ عبور کشتی‌های مرتبط با عربستان از تنگۀ باب‌المندب را نمی‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/453655" target="_blank">📅 00:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453650">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1DLVa5QQLG-dvuqaWPoDBxUfdaFmhBkTWR1sTBxENnZT0vJnzab2GGxSJk4yV4yeI3aCp4vC1GdapLyNhBjFJP_hc-8-gReBI1kJIWL7CxS6XhP_koYauPHxVaDbvmv-b2aWEGFn0t04dJjIBxvkmNTFOsf8AmXvciBXI-ZrNipoJBI3OQUwCJ_ebqFbG1KDgrcdN1LWxwNDRj9Rgq1vXFoz0XvQYtwiRWQXNfG19s6mJo74WHwd6nFSwUNMs5lWx45KNPBwBWvjtuSTbPAz-Ni9LZKdAKjgfXmzvLu6s5BbxZbZ1FmeykG28bKshSZVjc8JDe6M5K4dsgFeD7IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF4uDdeluOkrQ7atDUNIKqJEa6KBktpqZ4NqbJ36CSOmROSzJsi7uOJnfnIc5mfgDANcFJ8BOGImhohmr-UUkRiyFBETv8Fv7rO8d7r1OLj1Ln_fgSXEMJaYg1-O75ziHOOKzloH601ofZQL-GeryqUMZDSTo4OpEUp2bK6uEmP7utp0nB_nAgkQjEgQwArc47o_FCzlEP1sbQyhd8Y86wbneG_FPz2fMGkrlK8C6a4VYF67XIoQx5L24od3iokpo_Dh-yIkKN7n0xwkBZD69jUuOdOrqXkKkSWh0vMcVFHyTzeEJ1chbdWw24rScjyF0kHZiCxpVtEcqd4jF87_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wlwi4vMRvGbTeqImbvQwwzbvIeF2FZ49ksiI4e_K7moQWzHliMrVXdBiJuSkK4XLNbwFP4tLQ0s1aIZTyOk3IL4pytDz0D5XeVRN5_h5-UR_BQRwpX5gvg6MlA5lgXt7ZhTvXUqR57YtnVckKTB9669ytbP5-9c4MNSsQ0bd0EsEYzHCJ1f83BCpnbQeJt0Crtf414y4vMMXEyMoFSlkIx9SeXJ9jT3YP4BASIMSKi5nHfePU1TSa_JNjUGmaD37EcSpWpd_mqTmtLg0hed667ytNuVBTvhYOaDqN7ivVnsb98cVn-qqFDO4rkARFWPegpFgodfxjUMFqV7DSLouMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABptKxXXINx-7ifP10BdTvXtaqWXXcpXejTDr3C-uePiEyEopxb-DIH8iLwHH6wwzYzvITeoR3OHWVMyYdct5uOiJHgq63EqSkvRcT_Jg1Slp8zVBDtOib_2gL5NczwKFumu5wGuzUA9tiLuF7YAGdNSmj8MrTnE5rIr4Zeej145fk4rRvHD8aRJtmxIk8kBHmKk50c0Yj7FFBFB6E5hdAaqH6qK8vuf_OwnoNU4mM8Vx2pgrIwdJ9ihdUyyw7Tvu3ytqhkC-ge0T7ehIu2-rUWDrKSiN_peznpPOoM89PLduB5e3oOtCLwgB0ivxVlS9hS-9qdXZ_-pnz1ZmyzB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDltUI60xwAzIf_C9hVpaefL-Q2PQjzHFMHR-7jGZq2El_AIO1B52nM8Ofu-NNGhwDWjc1imu5tEXM3bH83yhjYe8XexwYF54probKzclWNt-qJ1qLj8XUT8mrkz4gdAMuseo__9VlGgoqiPWw5hLyxJ-_u1DMvJSx0Sgb0rJCU1mM5dzzgabFnZNTzIVK8eRR-JH6spPKx7Iwifk-3Z8tjVyUTHiFwORbeJCHSilKA_IRDcS-cbESQ3372fH08E2ckeBKMP_0BCMTpQoNdLoQwP8lbHMJmDlchTkCUbddway3BdXmVX7jTu-vYZS4FsIcRlRdHtlRF35ALl5YziUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غروب زیبای مسیر طریق‌العلما به کربلا
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453650" target="_blank">📅 00:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919084637b.mp4?token=CgbXiOjZbh18foK4ftCHZFKMUxOoxieLUD_2RIgHJTCQJXBJuqiW5YXRmf5OW1eMBkPyyGn58lSKlZjkW3CEOcIGScF7kGLGaK0kU16L0RDKHQPULsnfe_z04BGLrvO52mxikfu_ZMTLTlqpBoaOf1rb2z6ejDDHz1IKahmzPbqIYDh__ZjStYGd3aHE4aQwMpvLdXdjsnpKX7Gb9bsmHL1ES45_y911BYS_A_2Loa098j3TsEruGlWXYrWHFjZeF-u03yF5hV1ClsuGX5F6Z6SQBg1BGC03YE7ctX4TD357uptOaFw6VPKoqWOb38JhB7lohJHdojjSAgFio-ImkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919084637b.mp4?token=CgbXiOjZbh18foK4ftCHZFKMUxOoxieLUD_2RIgHJTCQJXBJuqiW5YXRmf5OW1eMBkPyyGn58lSKlZjkW3CEOcIGScF7kGLGaK0kU16L0RDKHQPULsnfe_z04BGLrvO52mxikfu_ZMTLTlqpBoaOf1rb2z6ejDDHz1IKahmzPbqIYDh__ZjStYGd3aHE4aQwMpvLdXdjsnpKX7Gb9bsmHL1ES45_y911BYS_A_2Loa098j3TsEruGlWXYrWHFjZeF-u03yF5hV1ClsuGX5F6Z6SQBg1BGC03YE7ctX4TD357uptOaFw6VPKoqWOb38JhB7lohJHdojjSAgFio-ImkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پارکینگ مهران، علی‌رغم افزایش تردد‌ها همچنان دارای ظرفیت و پذیرای خودروهای زائران حسینی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453649" target="_blank">📅 00:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emJiWhBNPhkhC4Uy4-rkT9YedYMUsA1vwmL5475ydgHH3iaZy55bpS7I_v-fFy4EasMw5SQWgq_CY0zF748elXaRiog31-LUFryv2R9CYfJnzwF-pout7kBBuOpF8ZiU5fpWdzcrTd-LvDXNEi1JSjLYPqYsSk7o83ePdLoqq20QEK-fjTrrxUVLznEuEKFFDv0pbS7uXtXU7wGUIMzXvx-wKCr7F_5qalUs2xBOcYr2tvMUi38WGRuar7fBufcBF8-Tf43-F8YiGbkQGj608_h1g_01R_eSr1d03ELEw8rEHDudni2cdQtjHocA-M2QzR4J4FA7Mpbq4mBzGKoJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: آمریکایی‌ها تاوان‌ حمله به مناطق مسکونی قشم را خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453648" target="_blank">📅 00:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/614a5bd431.mp4?token=GZ_w7E-rZfk54dWZEJBuiB4hqWxHlv8XqltmdR7j7r3zxBcK7OS0-WrrSnPbHSMvhDUjDUwZrDHtzwT96qeAytSn1eez73casttHVH717iX0iHTqpkt9mTEsFvfrTGguGLq1WB9a992qvqTK6opjnjONDoQ0sVJG_0GpHtiiDtHuMvILX9dYhsTz3ZvKnjQQTCTPu5uKlL-q2d9L3JqsOazyU20j13tjH8bDxmLrL4_GMT-T2Wg7_ZOkMAMuDJ5ECi1Fk5yZMOGZK_0wnOFukMQnEdHBllZ1pWl9xVPFQFCNvdvErBdXEQAWasTkFb0JpWxGv5Kmh7uxnGJSsHdxZrAda5i_PfA0uDyQKFe_AuJmSSg_gIgb5ZOOyMnHzj-EGFntFAs-QuCw_6Nug93T_8SxtSmWljcSHSKCUE2Uxk2HwKqeAKfW2HOTBG783eIKnbddNSPexQS4gp9GoWiNnUL071HPFiAothTPGic9mV2u7YhAWxIeDBOc8ihXu5sr01B6t8mdhZ1b5pz79f5XRNsBTsuo3hgIP88XGeU3qk00lrrOskn0mfZzVR9SO5IqaYJ9BrXS5PyYI2PU-6ktYx_u4z7IrHxrhk8R-MfjQgbFm4EuvtX-BiZWehTUjcj545y_d264CTz2hTg8uDW2gKouNgZAtNS9wmV5cyOS1mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/614a5bd431.mp4?token=GZ_w7E-rZfk54dWZEJBuiB4hqWxHlv8XqltmdR7j7r3zxBcK7OS0-WrrSnPbHSMvhDUjDUwZrDHtzwT96qeAytSn1eez73casttHVH717iX0iHTqpkt9mTEsFvfrTGguGLq1WB9a992qvqTK6opjnjONDoQ0sVJG_0GpHtiiDtHuMvILX9dYhsTz3ZvKnjQQTCTPu5uKlL-q2d9L3JqsOazyU20j13tjH8bDxmLrL4_GMT-T2Wg7_ZOkMAMuDJ5ECi1Fk5yZMOGZK_0wnOFukMQnEdHBllZ1pWl9xVPFQFCNvdvErBdXEQAWasTkFb0JpWxGv5Kmh7uxnGJSsHdxZrAda5i_PfA0uDyQKFe_AuJmSSg_gIgb5ZOOyMnHzj-EGFntFAs-QuCw_6Nug93T_8SxtSmWljcSHSKCUE2Uxk2HwKqeAKfW2HOTBG783eIKnbddNSPexQS4gp9GoWiNnUL071HPFiAothTPGic9mV2u7YhAWxIeDBOc8ihXu5sr01B6t8mdhZ1b5pz79f5XRNsBTsuo3hgIP88XGeU3qk00lrrOskn0mfZzVR9SO5IqaYJ9BrXS5PyYI2PU-6ktYx_u4z7IrHxrhk8R-MfjQgbFm4EuvtX-BiZWehTUjcj545y_d264CTz2hTg8uDW2gKouNgZAtNS9wmV5cyOS1mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453647" target="_blank">📅 00:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cedf8c9dd.mp4?token=UzRmAFErm_8CFjPT5ODRmJnecFA5tCFAVPehY5aWnexSY0BJ-gnUVfRDZmkPowBNBcfxAhdPbYSFXPaZ2jLgTUAZevEr60XoLF4nxVA6d1ptcCbvAu3s0gEuHu9joxeqxfx1hjGKzHEUTi1BbPBK7plyCUglQQwyn44v0PA-NgyOhdV4fET7sWQ2RvIRNPjD0U-3OtNVZk0Y1SvnTJZ4mlxD4qjV7hsbEOaSw6ZZ55ANL_mjHvgb3jZBJjQr2vn85y85Hgrlo7aQZv_b_2z6cjmmuzY0uaAF86jb7z1qE37lEWs_69xQAzXAtS7TFeux5KjSv7S0rGoaZXSloWLTqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cedf8c9dd.mp4?token=UzRmAFErm_8CFjPT5ODRmJnecFA5tCFAVPehY5aWnexSY0BJ-gnUVfRDZmkPowBNBcfxAhdPbYSFXPaZ2jLgTUAZevEr60XoLF4nxVA6d1ptcCbvAu3s0gEuHu9joxeqxfx1hjGKzHEUTi1BbPBK7plyCUglQQwyn44v0PA-NgyOhdV4fET7sWQ2RvIRNPjD0U-3OtNVZk0Y1SvnTJZ4mlxD4qjV7hsbEOaSw6ZZ55ANL_mjHvgb3jZBJjQr2vn85y85Hgrlo7aQZv_b_2z6cjmmuzY0uaAF86jb7z1qE37lEWs_69xQAzXAtS7TFeux5KjSv7S0rGoaZXSloWLTqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از رگبار باران در جنگل‌های مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/453646" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453645">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراق ادعای ترامپ را تکذیب کرد
🔹
حیدر العبودی، سخنگوی دولت عراق اعلام کرد دولت این کشور هیچ‌گونه اطلاع قبلی از حملات انجام‌شده به خاک عراق نداشته است.
🔸
پیش‌تر رئیس‌جمهور تروریست آمریکا ادعا کرده بود که بغداد را پیش از انجام تجاوز مشترک با سعودی به این کشور، باخبر کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453645" target="_blank">📅 23:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453644">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT4sr5tU8UVsr-VR5wuzt54uLTgCFPmDJ9_J6CfjCbEaWGCaopN1g7qE9ejcg2VkpS07Q-GypLh-nim53lcnSoFGAGeDP_8EeVGFvhkGYTJ77w6HGjtcrydHtv7_LWMsb1JUO8v6k_OZl4x_-dm1TJBnxT5zvxOqt-YEnhRgNsCL5OBd3rQCMGd6_doW-OCmE2f10jQOjlcEawBXL3gYrfQ_pEEaHYV8XPzC4SSe6dS-S5sBhEQT95QXtg3JgAbZMhyaVPv9X_daevWN6TaMwKkMLb9CuPEdA1Hv4QWcTKYsLulx8OBINx6I3answarTx-tOYP9eL4Lt3VIQ-4eHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ یمن: به مصر حمله نکرده‌ایم؛ فقط عربستان را می‌زنیم
🔹
یک منبع مسئول در وزارت خارجۀ یمن: شایعات دربارۀ حمله به تأسیسات گازی توسط انصارالله در بندر دمیاط مصر را تکذیب می‌کنیم.
🔹
موضع یمن روشن، علنی و صریح است و فقط رژیم سعودی را به‌دلیل محاصره و تجاوز مستمر…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453644" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453643">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366698c896.mp4?token=NWuvsV08VehNFMDQQVYFTiGwkeyde1ljDfS2fB1h07mAQpgBdxmeYtIHqXDS_DOEmGlXFU2P5gH0qqouXnDSDE6kL2DplnoamnQtaglvtqkNosnwFKKFXQwKUREIZkuUVkUSaOUU34ULLS4z_QzwtjC5Redinc9kNrNmyWSKxCvsVvBLqormYdO-KoFM8YgrXLQRsoMvlkOOgQhsvai486IclkA0AxGcmqojSTmp8lN_d93QX5APkL0dPlqD8u3qcvKg4b43iB-PBf66lAgzdsWiUmCVS0w0HhhU_C-9Cdo0oJ4rqkLyiepjEYwk69MrPOqMEUSaRSbZ136wpEn-ih-jUCvks0LOVDl_e_dzY_ddfg0Com3hYDubvuBJWaK7ogELfSNd8DkPRzc4cczAD2oNT6Knyi2j5p0NfWyxHte_Diz7Rg0tP4AXO3PSR576U3mMdAmJfW1WWDar37xZmss6lp8oQlVq_FG-ROPSFvI4OH80bTM0FCAMdpAMw6lFSV_HsbHaO0ebJKB-rA9UYCylWKv2DXG2izF9Vt3Xo6HpHpMba2FFtn3giA9Klpehypb_91fQgcNaCU0rNv67I-ViWZ6CDfA345s6TC2w6ZgIBcQo13-oho3u89aOg8NmZaf34kF-xLZZLZtOzP8rRwPKr5CF1w1etJNT96zuOXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366698c896.mp4?token=NWuvsV08VehNFMDQQVYFTiGwkeyde1ljDfS2fB1h07mAQpgBdxmeYtIHqXDS_DOEmGlXFU2P5gH0qqouXnDSDE6kL2DplnoamnQtaglvtqkNosnwFKKFXQwKUREIZkuUVkUSaOUU34ULLS4z_QzwtjC5Redinc9kNrNmyWSKxCvsVvBLqormYdO-KoFM8YgrXLQRsoMvlkOOgQhsvai486IclkA0AxGcmqojSTmp8lN_d93QX5APkL0dPlqD8u3qcvKg4b43iB-PBf66lAgzdsWiUmCVS0w0HhhU_C-9Cdo0oJ4rqkLyiepjEYwk69MrPOqMEUSaRSbZ136wpEn-ih-jUCvks0LOVDl_e_dzY_ddfg0Com3hYDubvuBJWaK7ogELfSNd8DkPRzc4cczAD2oNT6Knyi2j5p0NfWyxHte_Diz7Rg0tP4AXO3PSR576U3mMdAmJfW1WWDar37xZmss6lp8oQlVq_FG-ROPSFvI4OH80bTM0FCAMdpAMw6lFSV_HsbHaO0ebJKB-rA9UYCylWKv2DXG2izF9Vt3Xo6HpHpMba2FFtn3giA9Klpehypb_91fQgcNaCU0rNv67I-ViWZ6CDfA345s6TC2w6ZgIBcQo13-oho3u89aOg8NmZaf34kF-xLZZLZtOzP8rRwPKr5CF1w1etJNT96zuOXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر ایران در عراق: آنچه در مراسم تشییع پیکر امام شهید در عراق دیدیم، فراتر از تصور بود.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453643" target="_blank">📅 23:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453642">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUgbjEF3xiNYbzDqnTomzLker_cnWgX6e8YLmCAyX9FdAhs66_tW4HZD7_h4_dPNnxQmM6mxrX5LP2KGinxoFIFoD9kcv_3bgDeXGBRBerGQqJoXJpt37UGrQO7DZEyh9Qc965Ieao9ZnBFFuj8umjt4LavFI4thFU-jrzhfZiNsO6AckP7un0Aq3qARPxnKUrXY3pvB1xAHqYAR2wLJr97Wbg5dgX36Wh0vlGZFVc5jm_LUytiqesCZzIJsq7-cE3QzaARTODt5T2T5e8PJwiPL3_EAqmph1IzZ2J9lJL6OgV1SgfmlsZctVPfvbtsj3GK5H_fC7dqyj2ZRMoqHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاکمۀ سرمربی کره در پارلمان به‌خاطر حذف از جام جهانی
🔹
هونگ میونگ‌بو، سرمربی سابق تیم ملی کره، به‌همراه مدیران فوتبال این کشور برای توضیح درباره عملکرد تیم و تصمیم‌های مدیریتی فدراسیون در مجلس حاضر شد.
🔹
در این جلسه، نمایندگان کره درباره روند انتخاب سرمربی، برنامه‌ریزی تیم ملی و دلایل ناکامی در جام جهانی از مسئولان فوتبال توضیح خواستند.
🔹
هونگ میونگ‌بو که با شکست و یک برد در جام جهانی پیش از این با انتقادهای زیادی از سوی هواداران و کارشناسان روبه‌رو شده بود، در این نشست تلاش کرد از تصمیم‌های خود و کادر فنی دفاع کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453642" target="_blank">📅 23:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syUF8md5tPExbflJsGlYpyk6qeHPEUXS7HT9hovj4n9CRHazBRagj8vntOSSNYcX4lI0izgn5XGFSg-zJagKU52AOhGNo7a4_7miUha0qr6wS9uw7FdNOaB_HPFZOSAhYmE7Jt4iQQKjrJP1oBWenfGgKazqr5ZxbpJHkVeEVk0JJ9SBFhX4TT_XszS9h1VIgOLc5xezvYSOFJbCkkSTBNd1ilL9FUY5zUIPXg4wJ4MqB-V7omx48GmGoVa96AZzkOSMkdyL2o3VOhdtlyMidyeohmz8_fpUk19hTmplszWnXbut9LbUfrKiKGyUngzWYMTAQjhhyAxhVYmHK6mUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlVMLlqzkxHNOS2MQGQccM-8z6WqU88bYT0LFiB82usfV_-Nb6nRZJHXxHlUQkWXEcEsvpEDMfpMc3czYOnLj7mSafxDp0MpMElTI-wfARxSzQJCeMtzFHV-rzsrc0M6cmCUVWYwTc8marKF4LCjaOM_sO49l5ogEeTPYJ3T4tBtxjVpMAY38dRxroxU-2jIMPp91NWo8pkvQRaiwspqGxW5uJaYRfAC1oMIJIl7BGL6bdEq55BoROaO7u7xEM0pCp5-wk10N0yG17JWE_rXrMTcEcBBfgaB03NzA1LS6C_rDs4NM0wa73gw2h--gT5BSdpJ6UYRYyHfafrky4xW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KX5gFKsftJMCCZuN5RU7F1cBkreL-unHe138bzfsJlbm5h0kZeWInpYdjttnsz1NsCgjASN2uw1TVheV72nW8_YIHmTm4qd-EnrzHd2jMltKZ7D1CQQlv_552WbGI0k5iqW8m91lYtwHsdjfVAcC200nFdT1DmIkmf_62-wx4lFi2xOQZDlApdPwNyQRGwvIa_yuH-NTXIxAXulJL9ZfXcl57Qg_xFcT386mi6nzLvjmy4SHHCd0PooYLlr2ZeXYM0pjoWURyN7T7csn6Cl96XW_mZ0XfQUk5FaJglIWdxz4vz9-dZVQt10hHuHsAw-hb6CwPYO3XjQG9gWnIrqQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7J4uSGY7d4A5gpcFIzVyHYSO3ChcniSadZxtX2YbdKr27nkrAUl8wvtYRnmY3f5pjIj8qGfxAsLQljkhiA6dGQm-dDjJWfd1L7eRz3GlN9Cd89jsZnr4mFTfnVmc6HBqO0jjqGFQyf2FAhFH5IinwaDUzRUpNZdT_dK7hYOzcJjpePmyThZYVuq2uCReR3ZlptfGuV8aH1uK0E8Ypk-VI8NpjN8W6qlRWo_oNgtuLEEV5fic2Gfw3GfORqCs4T9ulvEiArXnMF8QADc7dAeoPr0HFlfVCKXYXFAkz7si3Oj1j-wNH1u80NlG34qRh3IKdEeHfOUSjvf4-pPAbcgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wb_Rw-W9U9zLrlj76wK6OAGvjlrJLEsZLZdl2uldSAsYK6WP31iir40dXpU8DIG8sbVNujqSx2ReIfcCCdSPkOSYS_c43jIqeoWlpBCZRHjEG5-HtSddLdeIeiahyxQOi4V4Xl9MbgLmHVOPMsfvaq24UDBPStVdfoVozMdAL8YPXrBEOS7cX41vCLLirTxTDy9eOnmgdUzgG3-usMNi7tqpGfjy2YENCy7jjlPLq6D4Fb7-qM8kFJbuzxAHXlj8jEsB6ZlD3UXs8vbd2Jy5kwuF2XfiU2Ft6YhhLeCB2DsLy_cyPlSozez_OZUCsAOzQOEbMX4M4eFNTaJSWyTDtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۲۰۰ متر از خط ریلی گرگان-تهران زیر گل‌ولای رفت
🔹
مدیرکل راه‌آهن شمال شرق ۲: به‌دلیل بارش‌های رگباری در بندرترکمن و بندرگز ۲۰۰ متر از مسیر ریلی دچار گل‌ولای و رسوب شده. عملیات پاکسازی برای بازگشایی در حال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453637" target="_blank">📅 23:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZekmMwkjE9XS9tV5c_E5rJkeHTJGSdnt9JXJ4wK1d8ip2ri2uSe32c7Ac-_k4Tyn5ljVgCmqjaG5neIRNifDaGC1yYvu2YwHKyne-l4HTEGjp8Xh3t89kBrFVN-51X3YksIj2FDyzXxm09MgMVRk-ELPClNFCtkc-ai6GeKXfqmccHwj0OXvFDSMRUbo7cTZgysdUvLKhrveYjtyXcbIuQ7k-49PXQPF1kdM9sNVPJkamTdvuAUdnMTodlYe7fzmxcB8jbgqNQ4oQQToR3C44JtzWuSwgsUuQj0xyCgjT9wZQFuSIcr_dHy8tv0PJrPAtuDfrp6eNz7agdU-usYFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش بذرپاش به توییت کذب یک فعال سیاسی تفرقه‌افکن
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453636" target="_blank">📅 23:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دادستانی علیه افراد حامی محکومان بی‌رحم و سنگدل کودتای دی‌ ۱۴۰۴ و جنگ رمضان اعلام جرم کرد
🔹
پس از اجرای احکام قانونی تعدادی از عناصر کودتاگر دی ۱۴۰۴ و عوامل دشمن در جنگ رمضان عده‌ای قلیل از چهره‌ها و افراد با اتخاذ مواضع دور از انتظار به طرفداری مستقیم و غیرمستقیم از چهره‌های اغتشاشگر سنگدل و بی‌رحم آن وقایع پرداختند.
🔹
در پی اتخاذ مواضع مورد اشاره و حمایت از کودتاگران وقایع خشن دی ۱۴۰۴، دادستانی تهران ضمن دریافت گزارش از مراجع امنیتی و اطلاعاتی و رصد فضای مجازی برای تعدادی از این افراد پرونده قضایی تشکیل داده و پرونده به مرجع صالح ارجاع شده است.
🔹
دادستانی تهران عنوان کرده با افرادی که به حمایت مستقیم و غیرمستقیم از کودتاگران و عوامل دشمن در داخل بپردازند و در برابر احکام قانونی رسیدگی شده در مراجع مختلف قضایی اقدام به تکرار مواضع معاندین و‌ شبکه‌های وابسته به سرویس‌های جاسوسی کنند، ضمن بررسی دقیق محتوای منتشر شده اقدام قانونی قاطع و بدون ارفاق خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/453635" target="_blank">📅 22:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار ایلام</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e49f71821.mp4?token=MpuqK3VjNsLxqEXVB4dMYtReX4QoWLrV9gHj7uqt6hViUbdjTgO_oylNzp1X2CGfxqnNMVn_7fx1WtsXQQn5BLWFiRcIm6ZePIwcnenFQK0dd4-xKaFl3EVsJqyqn9z8GMyMds1QTgSzPuXUyoCdXRVr__m3EtZ6XcMZGirMPuYggkEiHl7fu2tj9QG6F2V7aW0jMaXCeph79HZgr963ou3xcIvA_ti6u_8zqzga2WmwqLwic58kqGNdtRMTrgFY58b8tV99gE8xqna6zD3cKZP4T6pqdnoON51h_E6HGsNnJ8VCgfjp8ltCPMoIrC0zvOjRjYEVsGC_D1DHa-7HkwqEFbzBjQa-uPSZcmUM_RNspEkmNcYTks4U5R-woGoCJXauf7TeQEDwQgujqiGrTKuBB3SbGqNOWUm1cVvSxOWZPYhdtvb8IpIWuMuxF9-Ay4W8payFcaIHf_mTAXRZLzAGscUYsFMjJ2KiJKHM6WEMsRdTVKHQe_uYyLm8r1pf4Nmazjs0pD0m8oPhbU6Y9wNKvnb_I3FLNDC4KgtTkmUFD-EsDmp31MBhNLETolGnR5xfLmQDkjDioaNlInotKP7HxZBPEcvUEWr2PsI-VHMl8C18y7-hNgnG1Ac_lGCxo4aJo9tXBLQUihokeGYrKH8-V180L-tjNao2Ab9UxbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e49f71821.mp4?token=MpuqK3VjNsLxqEXVB4dMYtReX4QoWLrV9gHj7uqt6hViUbdjTgO_oylNzp1X2CGfxqnNMVn_7fx1WtsXQQn5BLWFiRcIm6ZePIwcnenFQK0dd4-xKaFl3EVsJqyqn9z8GMyMds1QTgSzPuXUyoCdXRVr__m3EtZ6XcMZGirMPuYggkEiHl7fu2tj9QG6F2V7aW0jMaXCeph79HZgr963ou3xcIvA_ti6u_8zqzga2WmwqLwic58kqGNdtRMTrgFY58b8tV99gE8xqna6zD3cKZP4T6pqdnoON51h_E6HGsNnJ8VCgfjp8ltCPMoIrC0zvOjRjYEVsGC_D1DHa-7HkwqEFbzBjQa-uPSZcmUM_RNspEkmNcYTks4U5R-woGoCJXauf7TeQEDwQgujqiGrTKuBB3SbGqNOWUm1cVvSxOWZPYhdtvb8IpIWuMuxF9-Ay4W8payFcaIHf_mTAXRZLzAGscUYsFMjJ2KiJKHM6WEMsRdTVKHQe_uYyLm8r1pf4Nmazjs0pD0m8oPhbU6Y9wNKvnb_I3FLNDC4KgtTkmUFD-EsDmp31MBhNLETolGnR5xfLmQDkjDioaNlInotKP7HxZBPEcvUEWr2PsI-VHMl8C18y7-hNgnG1Ac_lGCxo4aJo9tXBLQUihokeGYrKH8-V180L-tjNao2Ab9UxbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طریق‌الحسین؛ جاده‌ای که عشق را معنا می‌کند
@Fars_ilam
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/453634" target="_blank">📅 22:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn0cUU-bUvw1hxledV85NdAYs7t-OqXRbRP7JT1ZVlABNipwqslBWctm-99Mt1MTGmd9PRsR_LcfCZQnWHE4yFMrm_S2549mbLM2zAVIG-Wdzb9dol1U_Wo_BPS5GqE-eUoMErhsI69geGCGaIy1uG9j54-mlZtY5enkP5Q-ZwNUhqYTx5_FC-whIz0NqZkNvkfZl7ru4CYfIe41YXEDtHDPIZTw5GifkqwG8vJ-HPeNhAvyMb7MhUnHpVghiKeI_YoM-2lXNis6iyUn6pQBIGG-DNqfm-Td38NVnNvu7Zoz2Qmi9IAmKo7DKslEL8jVCjXQon5RGk2uLZVsXYmnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
۳ شهید و ۲ زخمی در حملۀ آمریکا به محله چاهتنگو شهر قشم
🔹
دانشگاه علوم پزشکی هرمزگان: در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و ۲ فرزند ۷ و ۹ ساله بر اثر این حملات زخمی شده و به بیمارستان…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/453633" target="_blank">📅 21:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad5499559.mp4?token=LHEEECnCo0Vyk8G0OzYW3HXLTjrtxrzdiKCnjSRpSJedkqk8nrOQNI77kHi0DO45m1B0PdjXELEFnXg0Cq7KS5ZaArDo3PKwGBoYYmi7QhOhJUj0rF3_NoQEB7XhAte5STd5yn7UElracdcAV9wXwjUpfOJx8DICBx5hJ3Tblne3UEAtFgS0ar9OJp_uFMaW8F7EmM21ctHlfNV7ZEaIbbYosymxUKVZHnO-JlEOnYqOpIAn4TiC304tZRUk1j-l_T6oPZJ4GJS88qmjSCPpYwLjmrHYtrkOcnxfTJRWTtBWekKdZE5uaMbj-HXuNLDw2N-2Rptpsb8c6D1C2n0EBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad5499559.mp4?token=LHEEECnCo0Vyk8G0OzYW3HXLTjrtxrzdiKCnjSRpSJedkqk8nrOQNI77kHi0DO45m1B0PdjXELEFnXg0Cq7KS5ZaArDo3PKwGBoYYmi7QhOhJUj0rF3_NoQEB7XhAte5STd5yn7UElracdcAV9wXwjUpfOJx8DICBx5hJ3Tblne3UEAtFgS0ar9OJp_uFMaW8F7EmM21ctHlfNV7ZEaIbbYosymxUKVZHnO-JlEOnYqOpIAn4TiC304tZRUk1j-l_T6oPZJ4GJS88qmjSCPpYwLjmrHYtrkOcnxfTJRWTtBWekKdZE5uaMbj-HXuNLDw2N-2Rptpsb8c6D1C2n0EBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  آسیب به ۲ خوابگاه دانشجویی در اهواز در حملات بامداد امروز
🔹
استاندار خوزستان: در حملۀ شب گذشتۀ دشمن آمریکایی به شهر اهواز ۲ مجموعۀ خوابگاهی دانشجویی آسیب دید.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453632" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453625">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7rlwsqIjD33SrF_Q_NR6snrXlZV3cQ8hXPmxTv6EJV1gpJhQSEYKPja6RLdxnwbyXRh0KiO0rQHdTtA-RhnEoAubiI7dBbmrExGpeFaRjANEkE-JbBOsVjcRRzfPX3LJpHv8PIZ3KZKep59bJVkYI1mMK_frwZ8P3rX-kgr9bHeZivo_THRXg7HVWU7HzCZAO_VUpw53FvLRS2yRAU9EXqlpUWgdcHIbpmrd7ibJnRCYzirMUYd3YsF_0TlbVRKdUotKKMgyhY2_wbk2uZ_ETKq8WP9KTofhxKSxTR7FtlZLpaZdFxlaiOMZH_W9O2_zFrh9ASO4NaogZ7QQ4EAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZ8xEDlrGx4uQ8PuZW7HIzqsiS_xk7VahFGn_Y893YITdJg8Tqehtgld2yD5ceRKLNm5mI1mfHHXdcw9KPYbjsUgyTTUWfJC7U-kKO2zYZGTfj3w0dU_5PR7bCqruVtoOn8pM7kW1lmKUJ4XtF52nX_LONfTGJYMkbAiTRxoWA_KdMXrLSUbu2xHLKGwDxrQz0PARf9K9-lkqoiNT0Dp27VWR_Pi4IpT6zo_eAazxmWDBO4QL0zxdS3DbOR7d2Ns8JeI22p6JfygLRbYlC6Dn1A8NuFS38vRJiE0A4PRvB5SulXLaCjh-_pCbHOa0Qi9Zx-iIom5ant15Gl9a-Ru8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BWqivfvsHCKHNl-mu-QNlj3-hct2lnzdSs9g6Mufqrn0lVC45cj4-bjxSnQa27iRByf1-9f3RlJOlYgBGiM-I-pZpG_4q28nssjWG5F_h99ZDQTePHIoUalQEiOMoClqsnKBq2p2DAB-j31zfvEioD_RVlyyqOzAzS3h8pFE423Xr8eD1Pi4EN9unWDKAXOuzGL5mFht-Mf_CO8RvxnFudamCMzwbQaV_97PwFzxGosNcq7FPpaoxqubvQoXFw2amUxTJFhPUNmqcYiucxdsYfQjwisfSXB3xX0msotWXY27iVPzN0-i04jLPTNH0ecqD9ALtbzW6Cef2EzUOVM33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iD9l1i0w4mc1loEvEVIQidPRgnnZyguJN-fulPtCCP6ZA8tfTwppNGCzBfsAtRJoXYE7-28v_QcG22kPvu11oZDz_zFgq7WlIRG1NOpsTGbRSV2-N5anM7xyc4xVgY8--w35Tmxm3Hq_5r-pAO0xv39siEyZJyu1fXGcdfd-caPrZ0DA30xzv7BiC2Z2o0FZ6CcdVc2sXpSOp6Vm84XndRqKnLCtaA94bM1rFdsuxIP81sc83nJ6SOhvjJMia9vmHI0M5aeERRdsZi1gg35cEZLsaHVL20Qc_sHi2AIY6E6t9oqhgQR6mZkReS_R5xEXI4RyqrLQJuNF77NPmdmq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7vRyFCIBQpDu58YZKwLbwHNJqHO3-aJdzIlOyMjxNirGNuQCwQhrE2hFEsJV3WX_qWztqSBl-cGPxZmS_yRT0torm8XnLc-0qxOWs9I5umwv8A4Vt_H44FwGX_dTXEZ0VU-aikokIaZeFFR2jwxkiRyQU7h2gsITU_wqDfc_cBA3924bIpAzVwn5p8ROnq37OOzsIvCHbKXhDs21Xy_uvKXKi4caxu-pN6HkLE25OhNmLegjU0i5SswNuYVz-KVpDPddPJ_3-lHl84NTxAA4TDGFs36Mq0AGSSmX6idfr_ZAOgjFQq1bOtWD_ne-x8c7Cp34xMduSDSyuMdikYM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szPzKPNEgyVG7UcGpurBooLQ1871LPzg5fxmzZpZL6IY_s1ZpNPEyzokzN-asrMKc3Jj1nxXuCuJzwWghPyaGsqiBZqkW7zolBEpLCCTzBpCkmaVUbN1lvux04Svii7pJo9EyrS26MkX8uQPUAue8xbcc0EIJFdW7W9XXeRqLnpW-8XLdBs77lo5Si_IhUQh9wYSjg4tsxFAlAI5XkfFcI8BVwOP-FtMqqbQuAe9hQKza-lhmRJe6PiFwnMO2c4-CpNEZOldR3HRrChhWO2BpHPobTXPgcuORliITFtfotdO6-GIQD_Y4NVfiwO1jKAd6dC_jLCxUJd0U_O0vBqIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLIJ5cL-8P9jikgZpGjk1GLMVieIp-O67eo2ekwtd-uJpOZdYSiie8M2WoSc5m6OoS6BlAQnjyOsRqsCri9jASTYVtjJ3I0sj2FHmU1b24T_CiGyFK-cfEe4mIUVqM470819_IiMhxq1P51h1PUpe6cOYc96wWJwZqnvqNtpRgKhsMfrgr0po9XpgH9l81guL5274bRCbKQqg9SlfD1zwHVCkJAUREAr7wvy4Kc6MqX9Hg5HAU9a_vv3QC2o0slechTGK344AOCiJPNaS8WEBRAOEFrGdcmLMAUD8p-UExAOFMB3PMT9RxdVYsbBvG6kyFCbacKxaGemYwEBLcoEQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تشییع شهدای حملۀ تروریستی آمریکایی-سعودی به عراق در کربلا  @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453625" target="_blank">📅 21:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453624">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34983a6e00.mp4?token=dlFIno_euOpDknsnvEDFRDBUqtNXKfFFfsFxaM6QIkIWW8noQ9XAEb9AUQQMhNpcG2yjevmdhUC1jrzvRYTJF7mw_fiL5VCjDBoOKul8jtHAccEQk7igDFA_G3B8cYkoOVFZb_vfwcVDLaPd8EmMb-wvsY33OzWLIDGhKMJ7zxLnxSIHjO4jM0GBkXn5mwEBTn7_r3rhV8zNRmxSYKGNE0YYtDtfkz0CGWMceHESoUuw4Abi-lOXwgXI_N3Ig_U2Fp9fbplIMZuHUOm3GmigmvlIbSOYAu815ddtVhCEHI4E901MPB8-bdzV5JQ3Pm5rCNjCT1ELnV71H4cVk9OMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34983a6e00.mp4?token=dlFIno_euOpDknsnvEDFRDBUqtNXKfFFfsFxaM6QIkIWW8noQ9XAEb9AUQQMhNpcG2yjevmdhUC1jrzvRYTJF7mw_fiL5VCjDBoOKul8jtHAccEQk7igDFA_G3B8cYkoOVFZb_vfwcVDLaPd8EmMb-wvsY33OzWLIDGhKMJ7zxLnxSIHjO4jM0GBkXn5mwEBTn7_r3rhV8zNRmxSYKGNE0YYtDtfkz0CGWMceHESoUuw4Abi-lOXwgXI_N3Ig_U2Fp9fbplIMZuHUOm3GmigmvlIbSOYAu815ddtVhCEHI4E901MPB8-bdzV5JQ3Pm5rCNjCT1ELnV71H4cVk9OMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد شبانۀ زائران در عمود ۲۸۵
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453624" target="_blank">📅 21:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453623">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txow7NwKWNX1HMYpyiZuAEAqhy6ET1BIMQKjpYMHIyJUMDOWLVYt8E3gkwYR7EAlvbF2Znd99Fgq6FYV83ytJOCUyS8CIcOAlWx8lEOQCMG88P9nOppSvNNdYLMOo6MKdnzbma80WbTfxiDKCh7WSvd5Ijyu4VK6GtijddD2ZETb4LYURyzx4POkwFFhd2fIJ0-Aepxsx5Su9LdKsjiZJl_oCWw9-krrBBGbXBewgTGCoIjvPfrxYLDKGTeMWeyLCwI9ZI2cxic8_NkmDrJzrec_1FAfcArSp9KBEVZ_qOypcOceYmXKlA06x5Smqobw6dEGPZywqxY2ahFB-WZZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر عبداللهی: آمریکایی‌ها و مزدورانشان، امروز تا اعماق جان ‌دریافتند که تابوت‌هایشان جزئی از تجهیزاتشان در منطقه است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453623" target="_blank">📅 21:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453622">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مجلس سنای آمریکا بار دیگر به قطعنامۀ توقف عملیات نظامی علیه ایران رای منفی داد‌‌.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453622" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15bfb7bca.mp4?token=eajxIBQqttfLm6n2kcEFMiZY3c0aF7kyr1qu93aZIKXmXfRXFwfOkxS3mvCX1V2NYU_jSyAMoZTucYelxcGZ0DGXjanhH9VQ5QUoKBrAxmXcnQ719LPplRzbUY9e1bgaB1prmdiJSAdJWlPonnKQJUW8sdQZXdR3dSetciJnjGkGLUVRiLgoqfsISu-xD5up4nJn-DcC2EMcwa6N7Mx1oJJrNvN17fNquNBD00q4G1zZvYHa_i6lt7yfT7wsryJWiR3-gkhVNSHZzGBS-mMKNrwv9MG8VWDQXab5XvhpmPU1Ph293oStO0bJ4xU0ZNiO6HH11QD_zhMO_yAXNY7Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15bfb7bca.mp4?token=eajxIBQqttfLm6n2kcEFMiZY3c0aF7kyr1qu93aZIKXmXfRXFwfOkxS3mvCX1V2NYU_jSyAMoZTucYelxcGZ0DGXjanhH9VQ5QUoKBrAxmXcnQ719LPplRzbUY9e1bgaB1prmdiJSAdJWlPonnKQJUW8sdQZXdR3dSetciJnjGkGLUVRiLgoqfsISu-xD5up4nJn-DcC2EMcwa6N7Mx1oJJrNvN17fNquNBD00q4G1zZvYHa_i6lt7yfT7wsryJWiR3-gkhVNSHZzGBS-mMKNrwv9MG8VWDQXab5XvhpmPU1Ph293oStO0bJ4xU0ZNiO6HH11QD_zhMO_yAXNY7Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یورش آرش‌های ارتش به مراکز و پایگاه‌ آمریکا در بحرین
🔹
روابط عمومی ارتش: در مرحلۀ بیست‌وششم عملیات صاعقه  و در انتقام خون پاک شهید امیر سرتیپ دوم خلبان مجید کاظمی، خلبان دلیر سوخو ۲۴ نیروی هوایی ارتش، پهپادهای انهدامی ارتش، ژنراتورهای برق، سامانه ناوبری و ساختمان‌های اداری و پشتیبانی ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین را هدف قرار دادند.
🔹
حملات روزهای گذشته و همچنین امشب به پایگاه‌های آمریکا در منطقه، با وجود سامانه‌های دفاعی متعدد و تجهیز پایگاه‌ها، تاکنون خسارات قابل توجه به تجهیزات و مراکز استقرار نیروهای ارتش کودک‌کش آمریکا وارد ساخته است.
🔹
پایگاه شیخ عیسی بحرین یکی از مهم‌ترین و حساس‌ترین پایگاه‌های آمریکا در منطقه خلیج فارس و میزبان هواپیماهای شناسایی، از مراکز مهم تعمیر و نگهداری بالگردها و قطعات پهپادهاست که با حملات متعدد نیروهای مسلح، آسیب جدی به توان رزم و پشتیبانی رزمی نیروهای متجاوز دشمن در آن پایگاه وارد شده.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453621" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b780c515.mp4?token=Lagt0DJQ9zV2RX-Cn7Du0QRvhFQTnDR7eRZFTliA0mUQrc_GNdzGIsMZjXvjZuGIs3K1ufNzYAuH-a50e0w2HaYlbmCjeK9tFsD5aP_a4ZpzbmJCIfWPT_Ri59AYDCAf-a__8vJcKbW2GucZyOhcMiZAHMCAgdosJdabX25FWAlz2lrp1FDPwqdCiJKQjV2r9bNmUT_jJ1JqWuEwikgFugZSCjS-hPLNM82nCZSbVOWOkODwoqsNQgvc-5dHZezE-aJRe3lP6cAGE3eFRMJpCd5_tE4_M74Z4qyHOHdn_ip3mtUqOl8jqa9i0BSaDQpN3X6BDsI9mIk9l01V_1ja0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b780c515.mp4?token=Lagt0DJQ9zV2RX-Cn7Du0QRvhFQTnDR7eRZFTliA0mUQrc_GNdzGIsMZjXvjZuGIs3K1ufNzYAuH-a50e0w2HaYlbmCjeK9tFsD5aP_a4ZpzbmJCIfWPT_Ri59AYDCAf-a__8vJcKbW2GucZyOhcMiZAHMCAgdosJdabX25FWAlz2lrp1FDPwqdCiJKQjV2r9bNmUT_jJ1JqWuEwikgFugZSCjS-hPLNM82nCZSbVOWOkODwoqsNQgvc-5dHZezE-aJRe3lP6cAGE3eFRMJpCd5_tE4_M74Z4qyHOHdn_ip3mtUqOl8jqa9i0BSaDQpN3X6BDsI9mIk9l01V_1ja0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزهای عراقی چه دلبری کردید
برای مردم ایران برادری کردید
آهای اهل عراق، آبروی شیعه شدید
🔹
شعر تازۀ احمد بابایی در وصف حماسۀ مردم عراق در حمایت از ایران
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453620" target="_blank">📅 21:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453619">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4074816569.mp4?token=jmLt_SqUCtS6a9KzBpdYW2w6u2kAqZAxACCSvvts-9e0vvaNLzGwbc1nGlK2ipsPWfPx0jj4lQC2NnwLxoVlfhWD6Y5x_3WWDDwjWugRmZAMx7clqeQYxcsYPPrXRcQvuSPkmJzrcu02pV5GGc8mfvouoyjfZkQa0krYhn2gWFEzPALlP1CZf3ZXo6HTa5WReIHb9xb67WY7Y0N5KzhJkLHgXZMw_lelIkwRAQfQFPj-teu5LC-WIRD8OPZPHL5IoXPK0Nliv4AHo2mYH4oqNwGRbAsI8VvjM4suG_b5Pa7BwSlmNb7Z3bdeBrFWKC1WgTuieAFm00ODB6sAmp9eF4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4074816569.mp4?token=jmLt_SqUCtS6a9KzBpdYW2w6u2kAqZAxACCSvvts-9e0vvaNLzGwbc1nGlK2ipsPWfPx0jj4lQC2NnwLxoVlfhWD6Y5x_3WWDDwjWugRmZAMx7clqeQYxcsYPPrXRcQvuSPkmJzrcu02pV5GGc8mfvouoyjfZkQa0krYhn2gWFEzPALlP1CZf3ZXo6HTa5WReIHb9xb67WY7Y0N5KzhJkLHgXZMw_lelIkwRAQfQFPj-teu5LC-WIRD8OPZPHL5IoXPK0Nliv4AHo2mYH4oqNwGRbAsI8VvjM4suG_b5Pa7BwSlmNb7Z3bdeBrFWKC1WgTuieAFm00ODB6sAmp9eF4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب موشکی در عراق
🔹
موکبی در شهر سماوۀ عراق که تصاویرش[ساخت موشک بالستیک مزین به پرچم ایران و عراق برای پذیرایی از زائران اربعین حسینی] این روزها در فضای مجازی دست‌به‌دست می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453619" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453618">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تحریم‌های ضدایرانی آمریکا علیه یک شرکت هواپیمایی
🔹
وزارت خزانه‌داری آمریکا در جدیدترین فهرست تحریمی ضدایرانی خود نام یک فرد و ۵ شرکت را ثبت کرده است.
🔹
طبق ادعای خزانه‌داری آمریکا فرد مذکور تبعه چین است و به‌دلیل ارتباط با شرکت هواپیمایی ماهان در فهرست تحریمی قرار گرفته است.
🔹
اسامی ۵ شخص مرتبط با این فرد و شرکت هواپیمایی مذکور نیز به فهرست تحریم‌ها اضافه شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453618" target="_blank">📅 20:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453617">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aad6f861f.mp4?token=L0gQZnWBm_IRRpmDQFvMxO4LyzjV0AY8AAjGWSNcc5lTqA96p69zgKOdbgZEop6WFy1TatTPAiBF24J9ctE-qAqnHq8koUh2mxB4zBoykUBB5cLmXV2h3iRDKO4iTggRVlNnAisLdUx_LGKNpG3tVIbn6wpOYLzZNuAnTszduZCp8EBJ1GppOUe9_UsMYfodBKV4TLkUTPsobDoexG_9JshgegQ2mg2KSeYFe3-E__kb5zhLPgEDEBCPZltwBl_bgfPX7MxtIWBx777Ssbufni7mSoJbvlOtW3RU_Y17DJopqtjtNm1qgm8phSZ0UYoLKnBOhqzYu5InMwqQpu4E-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aad6f861f.mp4?token=L0gQZnWBm_IRRpmDQFvMxO4LyzjV0AY8AAjGWSNcc5lTqA96p69zgKOdbgZEop6WFy1TatTPAiBF24J9ctE-qAqnHq8koUh2mxB4zBoykUBB5cLmXV2h3iRDKO4iTggRVlNnAisLdUx_LGKNpG3tVIbn6wpOYLzZNuAnTszduZCp8EBJ1GppOUe9_UsMYfodBKV4TLkUTPsobDoexG_9JshgegQ2mg2KSeYFe3-E__kb5zhLPgEDEBCPZltwBl_bgfPX7MxtIWBx777Ssbufni7mSoJbvlOtW3RU_Y17DJopqtjtNm1qgm8phSZ0UYoLKnBOhqzYu5InMwqQpu4E-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از دعوت به حضور مسلحانه در خیابان تا چرا قاتل را اعدام می‌کنید
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453617" target="_blank">📅 20:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453616">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tY4RqKI-SuUQ900F9vQnZ82KNPvgz1h2v7x2n13_J78l1IsflRNuXP60o1WYqiValflDKKXWniszIVUA8py1YKXYzjijRuYQlAiesfiXq7EGB2vARip7hnzLNONTW-TOd_hpT5FGUKbRUl17HbKlqcrEIPPz1O3AKAuHLu2LEictQd9OSufBUQsuQtm39nrFm2Q1RlUWr50HvPvzyxvlxi6TcgNHbvDLmYu8cxa--CLjofv1M5a4o5zbzHQ2uQfapHCOh0nusGG1VGSVLd-RGh9ntpe6WTymSk8CG9ZS4LWavypJJnUoV_S-nmVEjOEoGBBbPExei3zMhz424bZ4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال در بصره میزبان رقبا
🔹
پیش‌تر با برگزاری بازی‌های استقلال در شهر بصره برای لیگ نخبگان مخالفت شده بود تا بغداد به جدی‌ترین گزینه آبی‌ها تبدیل شود.
🔹
بعد از پیگیری‌های فدراسیون تاییدیه لازم برای ورزشگاه بصره از عراقی‌ها گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453616" target="_blank">📅 20:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453615">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cea330b48.mp4?token=r0XczFWJ9bJLqDrj2g-MCOc_U9A9oP3oTedg4Qp_iG6slypf_fkmu6i7pGqSb80cGZsdHiKUFBiNlwYVTwo7mSE7C5zM7o8QaQLbVk1oaKxKttCS-lhBqOijRYybpVO0bXizjWcEfp-A-Lmu0-_3lQKCzmEDCs1htqnnR1gVHcE84SNB581Rdv0VZ0aIdYiRJRNddyAH_2QV39V5D5czaPIJB7AZSfiOE6D3jQXMjZv8McT9kdS-UqJQziFavDh4EpBEVSrUcnRlZ37rqS66IYSn5l0mWq1Y_hCPIvermnSXQKOjds4IxJx03zGMnG0P9gwB3cb0cjCH00LgWbGvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cea330b48.mp4?token=r0XczFWJ9bJLqDrj2g-MCOc_U9A9oP3oTedg4Qp_iG6slypf_fkmu6i7pGqSb80cGZsdHiKUFBiNlwYVTwo7mSE7C5zM7o8QaQLbVk1oaKxKttCS-lhBqOijRYybpVO0bXizjWcEfp-A-Lmu0-_3lQKCzmEDCs1htqnnR1gVHcE84SNB581Rdv0VZ0aIdYiRJRNddyAH_2QV39V5D5czaPIJB7AZSfiOE6D3jQXMjZv8McT9kdS-UqJQziFavDh4EpBEVSrUcnRlZ37rqS66IYSn5l0mWq1Y_hCPIvermnSXQKOjds4IxJx03zGMnG0P9gwB3cb0cjCH00LgWbGvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر اولیه از سولۀ تعمیر و نگهداری جنگنده‌های آمریکایی در پایگاه موفق سلطی
🔸
این درحالی است که سنتکام مدعی رهگیری تمام موشک‌های ایرانی و همچنین عدم آسیب به هواگردها و تجهیزات درون پایگاه شده است.
🔹
سپاه خطاب به سنتکام: بهتراست دست از سانسور شدید بردارید…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453615" target="_blank">📅 20:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453614">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq7WMUcl7uTxW4dTAh98qiIwCbwbWx3OJIEIif_NSfx3LpKC0eJ_VXneHKGlTiu97eufUS_FxCHQQ8h1fMa6Lp_eorpRG7M3uYiHbjI5jnCKm0l2-5SaBlqdzk1ReIryIuLQnh0MnxbJRANDgSexB3f4x5DsQG7l6wa1QvM4Of7-HFRp5DbL4AWfjnc4wr1pKpcCzMGmU30GTX5EbAbvIBRX1D_MktnMfNbRycGxucK7a0LLbRX0ysVQyjJ-hwQpiPoo_cuqITVBML4ED1ek1F_qP8WMmvJJXxZLiE7C50uRGftS9vmKVUXtZ6_MouUsKfwJbLA9AzlI2SgOYn_d4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از عملیات صبح امروز سپاه پاسداران که منجر به انهدام سه هواپیمای F-35 ارتش تروریستی آمریکا شد  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453614" target="_blank">📅 20:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHd8W0rDN5h-P9nCt2_plSMjuAOJmy5XD7_1Zgiij7So7Qz5SG0abdpdj7b61dAoWIroUaA3a-LP8T3drw1ONMBoWJJ8m8TZV-HKsh7GHigvq_DRQtZWlMH5TjzIAk-e7j2XvN4tbNTlIYFSf0lA8Rl3LasWWAYHPL37jzYtbFfgyTE0TE5AbkBihp6OwNX97ffWteM7mOLwqYffckdjN19XSpKpNFfHnP2JTJ3Z4YteaYK2df7T6pBgDC0XtoI64voVbfpX80nPxWTv06fcx0uDZyDLX4nifLhgfOw8JtzniSDRPdLNWx-UFa26Xb3mpa-4yDpU_ym5mM1rhu3bhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rI0WYMDXLRFovZwOPdy0CyKJBKTwqDjqRuScbvwrBJTDo1LlPk0i-q6Vxjd8pV6BaAWrRkkfmVHfSWlVazw9VQpJIiLT9GJjWcnk9HiXKi9zQUdbIIFW9Eyl-rr_jRn9KK7CbQrmKi6Dd1px-3k9ZOa2IBCrXG2cSMhoLNIqGkPv61tLsoLE_ZauPvVCC9bJTC2ku7YnLGHVB3i0_9xL15kpLrdaJB7o1R7DyNJ2mmbHRIQT3iebHj0pyJVDD064t1GvsDeKaUx_iKMmH5JaEC8eNHL00Hhq-UHVpi9w_ooO8wlMC_-vVgFB3OuMT-4_LSux9yyfPoxutlUQLdTF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nakumM72yRII-VYCloIlJh_JKxfZI_WR_qpJjL-tFh-H8zX50IAvb_nMyRxHTzwaQrKjp2rXIEMSLbT9o_dmWXFwigjgt6bgKGC8f_CmmY8hfhE1_msuFKfHR6FA-IWpi8NYVFijZ_HFEljSAIxbp9Mu9wrrMuTFyetRHWHBtty-E5JTRXuxd4jFNvf4s1gjfUkRZ41phQEgLWQ-zLwBmqX4WCJ4MiY_oZZjkSPevETd7vH_xlKk3VQrFPU4OUJhl6JiN66qFThDjzgifNKdxrlxS1onDvGfGRIduRx3KgUAPsHk_rw0IhjJ0-mclBla07jxXpas1R_-8JRlks5LuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453611" target="_blank">📅 20:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453610">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEJNKHzUd7OiiIdTzlnKl_xjXyX_YTZzu09gW-3z0ljY6lqFE7V8UZh_gLtqTGzKrB8jd207mFwslR6HpnLxPYJYxepUfl2PjY7BlYVVZpn9smCPEoZ_j-3Lp9VUbcT-3CLVH5uqOTy0cOcA0wAltqvNAt4PfL9tbyTqOexXcL8Wk2gh8h0BYj0pO09luCkMHBcPDMwEzuZrZFSjkyT-s1RGaGRrlR7vFY1agfM0xQqp7LjuB6EcTUO0O4eZvohjVgH5IyRJJIAXPf3Un8yxAdMp_uOQm9FF3M-c0IXTYZo--9SRvTT1EU9h0Y2JLcUD6HrMYtC-OC_7-HXI32H6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوفا، فیفا را تحریم کرد
🔹
اتحادیۀ فوتبال اروپا و ۵۵ عضو آن در واکنش به پیشنهاد فروش سهام فیفا به سرمایه‌گذاران خصوصی، بیانیه‌ای منتشر کردند و اعلام کردند که در صورت انجام این‌کار در مسابقات جام جهانی ٢٠٣٠ شرکت نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453610" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453609">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237d13b6b2.mp4?token=g4_Wu4NagWcusyZdsKeKh1b19FJk5qJMftEKVlJEeX722Wpr2BCrgG8jfOSA_f65ZqeWHVFcTQKz2MDMtO8Q79fktX60mgUatkQR6Aqh5mUiBRiTL5gXVk-IG2HiA1jyqSBZ-btDFGc6cQV34X8cKuAEP0IR_RGvM6QXdQG0s1JdAqKqhyVwX9Tewfywbu8fDODenVFwUpTw-35zUSmsWph4Nr16xGnxlKGgdZ9BqBq3g_fkDR6TOPR-ANawLYTeQfA-te6VUPpkGtnVBRVvXthpV81U89fGwkV2MsSxlmGuVJzHHvywWQosnSOLb38GwI9JpefNgIhEHhvZDF8hyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237d13b6b2.mp4?token=g4_Wu4NagWcusyZdsKeKh1b19FJk5qJMftEKVlJEeX722Wpr2BCrgG8jfOSA_f65ZqeWHVFcTQKz2MDMtO8Q79fktX60mgUatkQR6Aqh5mUiBRiTL5gXVk-IG2HiA1jyqSBZ-btDFGc6cQV34X8cKuAEP0IR_RGvM6QXdQG0s1JdAqKqhyVwX9Tewfywbu8fDODenVFwUpTw-35zUSmsWph4Nr16xGnxlKGgdZ9BqBq3g_fkDR6TOPR-ANawLYTeQfA-te6VUPpkGtnVBRVvXthpV81U89fGwkV2MsSxlmGuVJzHHvywWQosnSOLb38GwI9JpefNgIhEHhvZDF8hyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📽
مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔹️
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده مشاوره در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی به زوار است.
🔹
زائران می توانند با شماره گیری 4030 بدون نیاز به پیش شماره از عراق به صورت رایگان، تلفنی تماس بگیرند و یا با شماره گیری  *4030# (ستاره چهل‌سی مربع) اطلاعات را به صورت پیامکی دریافت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453609" target="_blank">📅 19:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4072d131ea.mp4?token=rqcLUpir8zR2QXBs7aL87Hno2uzIttEgcsZsP-GQD-91hdDTMYOjCM1DKoYjx-QSopDUjNHBp-f3GFlWn5Rd0HIq2yAZqsIpNAZHcp_IjQW9tJEmj5k9S8l_iNTQzmbgagr7qsPai8ZH4Ryf-yQOx9cWyU3XdaaMY1QM8Wc1JsmctvTmya3PkDAvu7FVNCjgLluRErnUuF8CNhf1o3_xhDB6gelnwV_UGiB6m_-mnisaM6qF_vFZLqWmdgWHZ5z82rwwx16cuMkT4W-OTMGwEv1ekwPxDuTeqR1UeQzeWYB13Zh1q5N6Lf1w-E7UmaVNGz6KThTr2APiMNiOQn3x8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4072d131ea.mp4?token=rqcLUpir8zR2QXBs7aL87Hno2uzIttEgcsZsP-GQD-91hdDTMYOjCM1DKoYjx-QSopDUjNHBp-f3GFlWn5Rd0HIq2yAZqsIpNAZHcp_IjQW9tJEmj5k9S8l_iNTQzmbgagr7qsPai8ZH4Ryf-yQOx9cWyU3XdaaMY1QM8Wc1JsmctvTmya3PkDAvu7FVNCjgLluRErnUuF8CNhf1o3_xhDB6gelnwV_UGiB6m_-mnisaM6qF_vFZLqWmdgWHZ5z82rwwx16cuMkT4W-OTMGwEv1ekwPxDuTeqR1UeQzeWYB13Zh1q5N6Lf1w-E7UmaVNGz6KThTr2APiMNiOQn3x8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارائه خدمات درمانی در موکب گروه شستا(کرمانشاه)
🔹
اربعین حسینی(ع)
#شستا_کنار_مردم
@shastamedia</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453608" target="_blank">📅 19:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453607">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453607" target="_blank">📅 19:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453606">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6e32b797.mp4?token=UrgSCqkCPYZ9sVCBHn0rhmVgNu6azNE66dCKOkdGOtwWSOCepH_HOiSbk-KQM2d_SYEIgJvVq6qAk4_BAc_ll_NiQZO0HRlQHwgrfwbNHtaTTZUYEVsS3qTjsa_8DPwLF8rrY-042VD5z_Ik_EWGin2CThWs0NjshgBvFxWez0S8vLyU66rIBLsBizLRZOBU5zB0Rk1sq6xy_PelRDOhww_GHyeGtsvUiW6x52Ay42ecywB1jqnIs33tn3XrDs_L_MSBgQIlLt6vyn8DrASZC7cMD5dURcmoQNvXbH6ZuQn3jUVJqaCABXF2w6LupihGMD2VgLImHLZws0sL6V64zrL5pmYhKTatQVfTJ3m6DAWjWuX5gs0EXyU37LLq6nmMevhgC--YQKVZp9LSYty3w1oo3usfcBfv5SJuHiwz63ViMgU6xwLKJj0EgljPU0GJdNQXOwQ6bttiH2F5gHpZbzP3pzHULchMB9nMrWONwaWOawGe4xVufMpiyjQHS9bHMf60WQtXFvEIhNNRqN96EekdBYHtEVOjU4p4LAjB3zg0Pjj5-zqL6jMtcVsz44t2UWcxUNReK6u5LDn457ORAXs9DOW3o_03rn-Mo__APrNacQnlkrm_vpz9wBs31wc7TLApBtpcjMnRjEJsJMQxicV1_WgHvVB7UMWE7rEls7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6e32b797.mp4?token=UrgSCqkCPYZ9sVCBHn0rhmVgNu6azNE66dCKOkdGOtwWSOCepH_HOiSbk-KQM2d_SYEIgJvVq6qAk4_BAc_ll_NiQZO0HRlQHwgrfwbNHtaTTZUYEVsS3qTjsa_8DPwLF8rrY-042VD5z_Ik_EWGin2CThWs0NjshgBvFxWez0S8vLyU66rIBLsBizLRZOBU5zB0Rk1sq6xy_PelRDOhww_GHyeGtsvUiW6x52Ay42ecywB1jqnIs33tn3XrDs_L_MSBgQIlLt6vyn8DrASZC7cMD5dURcmoQNvXbH6ZuQn3jUVJqaCABXF2w6LupihGMD2VgLImHLZws0sL6V64zrL5pmYhKTatQVfTJ3m6DAWjWuX5gs0EXyU37LLq6nmMevhgC--YQKVZp9LSYty3w1oo3usfcBfv5SJuHiwz63ViMgU6xwLKJj0EgljPU0GJdNQXOwQ6bttiH2F5gHpZbzP3pzHULchMB9nMrWONwaWOawGe4xVufMpiyjQHS9bHMf60WQtXFvEIhNNRqN96EekdBYHtEVOjU4p4LAjB3zg0Pjj5-zqL6jMtcVsz44t2UWcxUNReK6u5LDn457ORAXs9DOW3o_03rn-Mo__APrNacQnlkrm_vpz9wBs31wc7TLApBtpcjMnRjEJsJMQxicV1_WgHvVB7UMWE7rEls7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اعلام
شهادت
قهرمان سوخو ۲۴ ارتش به خانوادۀ او
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453606" target="_blank">📅 19:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453605">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeY14BBF8DmL4oqiI4I7SVd7dwfvkm07y9MYZYji4quWJEGlPDVMkfAUfRSc0gzo6WF1eNoNkMXAvg_zMO4Oa1uRyxk5ZQ8vQ6vksGKqn0xh154w_X6CtT-9rZtjzWkD9JCJAvSxozNjl537p69OlXZdvoL3k__GcGAPgerjqKV5LJRCI3nRnbFL1HbTGqGADtvkf4AFa61FeqAu2ULiDuyu_hk-YwJuGHCgxzDznhhDyOvUgX4P6ME0yLLD91KZN2MTNjSWIE1KkbyfvV3aAFDu7X8WPn9cM2d_mXezKdRHEDszsUMjTsZeCtE1s4njIJe2uWMizX-qmdjd7kvFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بنزین در روسیه وخیم شد
🔹
فایننشال‌تایمز گزارش داد ۴۵ درصد از ظرفیت پالایشی روسیه پس از حملات اوکراین از دست رفته است.
🔹
از ابتدای سال جاری روسیه یکی از مهم‌ترین مبادی واردات بنزین و گازوئیل ایران به حساب می‌آید.
🔹
حملات اوکراین ۱۸ پالایشگاه از ۲۶ پالایشگاه بزرگ روسیه که مسئولیت تولید بنزین و گازوئیل را برعهده داشتند را با توقف تولید مواجه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453605" target="_blank">📅 19:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453604">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca0371478.mp4?token=hXuVIgjZ6o23g-nrOQnzkA8dXY48jXwT0T9HppZ18O1HZ6J-d3hrtvnTGxC7OHMSy66zEfMnSwvhp2HI5AIY2-f5y1lxiuE1WJJxEKgbVKXhnzEZVwa0umJFNPG_CTMrxxzcYMsx35OImJ1IgHGZJq4uwLKx7xLkEAzQfAp5zHC9DHvMGeL8j1_YlWdZEaskt-jlTyWdDrR5VjM16VTB6dligGK_c0IoMMwKwbpBSMLHTI3t_m2ef7dc96Pmzj5w4CT0A3uata-vFiZqUIxYsihJ1i7H0IRhJdQ7zJwQIcpylk39QdK6z0HHmEDbm04FyA488MJkqSDtVisuprb5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca0371478.mp4?token=hXuVIgjZ6o23g-nrOQnzkA8dXY48jXwT0T9HppZ18O1HZ6J-d3hrtvnTGxC7OHMSy66zEfMnSwvhp2HI5AIY2-f5y1lxiuE1WJJxEKgbVKXhnzEZVwa0umJFNPG_CTMrxxzcYMsx35OImJ1IgHGZJq4uwLKx7xLkEAzQfAp5zHC9DHvMGeL8j1_YlWdZEaskt-jlTyWdDrR5VjM16VTB6dligGK_c0IoMMwKwbpBSMLHTI3t_m2ef7dc96Pmzj5w4CT0A3uata-vFiZqUIxYsihJ1i7H0IRhJdQ7zJwQIcpylk39QdK6z0HHmEDbm04FyA488MJkqSDtVisuprb5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام قنبریان: خون‌خواهی رهبر شهید باعث خیرخواهی برای ملت است.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453604" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453603">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a375d5668f.mp4?token=oXcK8-2aBqSThaqK0oge3ViybQPYMNMNUpZEa15Nq8A-lIxQgRMJkRzn-hfHpP3JUMW87vHI0R6yV83YuA3s_gtP-wlSGOQFkbeT3K0HgdAdOOdxIDMoNqOfTJqy0Ezaajh97jFfAgv5sCe-2gDF7P4XZAHPoKmDglnQgMrBtteQCcILl9arZL2C7A-8A4yE7pHQC3tAHWo3_ItLXBDyZYZa1Rh3ZtCTNJNjBXOhEuXEoA-1hmphE0hLZrG6zfyDq0KfWm03IQWUqYwTMQAanaJKscLsOK_TA7YgXFUg0peI2Py5AhKEYfs9bkz8E6-vPKw20T-vyvPztwMcv9Mb0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a375d5668f.mp4?token=oXcK8-2aBqSThaqK0oge3ViybQPYMNMNUpZEa15Nq8A-lIxQgRMJkRzn-hfHpP3JUMW87vHI0R6yV83YuA3s_gtP-wlSGOQFkbeT3K0HgdAdOOdxIDMoNqOfTJqy0Ezaajh97jFfAgv5sCe-2gDF7P4XZAHPoKmDglnQgMrBtteQCcILl9arZL2C7A-8A4yE7pHQC3tAHWo3_ItLXBDyZYZa1Rh3ZtCTNJNjBXOhEuXEoA-1hmphE0hLZrG6zfyDq0KfWm03IQWUqYwTMQAanaJKscLsOK_TA7YgXFUg0peI2Py5AhKEYfs9bkz8E6-vPKw20T-vyvPztwMcv9Mb0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آمار شهدای الحشدالشعبی به ۲۰ نفر رسید
🔹
الحشدالشعبی اعلام کرد: براساس اطلاعات اولیه، در حملهٔ تروریستی ائتلاف متجاوز آمریکا و عربستان سعودی دست‌کم ۲۰ مجاهد شهید و ۳۲ نفر زخمی شدند. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453603" target="_blank">📅 18:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453602">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1WxK2UBKc79BFTm_Evu2IVEqY6syjCAEPRbBpAFcXrFD5i8aSz22IpoVJg8jgjzEKOmPYg0jJvj-1WAnIn7JiFmDCxB30PUCMm1dZzmESu67N_Fyxb_4ewtR9BlzWsOh0_kSg3BVGgmWkbdEvw5-HRVhCF6YaeVm5PF1A4pL9mBqXIeIPM9r9voqbmgLkMr18s2HAbZg7qL7LOOTXwlStHiLvqkhL3CCbQ8tLpA-LMIrL0c6Wcc7dIEKocbQMT3E7Yr2i123l_OCKA3Fo1_CFR1AV-pnBDbFIPkstL5-BDKIFqeEJ5vwgb4Jwu-jL8EmddTALy7buGUYPlvB82W7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس تمام صفحات خبرگزاری تسنیم را بست
🔹
پلتفرم ایکس (توییتر سابق) در اقدامی خصمانه و بدون هرگونه توضیح یا هشدار قبلی، تمام صفحات فارسی، انگلیسی، عربی و عبری خبرگزاری تسنیم را بست.
🔹
دی ماه سال گذشته هم دامنه com. تسنیم توسط دولت تروریست آمریکا از دسترس خارج شد. علاوه بر این، ایالات متحده از سال ۱۴۰۲ این خبرگزاری را در فهرست تحریم‌های خود قرار داده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453602" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453601">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804a06c2f5.mp4?token=XSRjIOFf7RWMuPsqPF1dAIR2cAG5A3OLBe8NkDifDChjirK_CDG8H8SW48DTLOikWmc1AUYArUQ_QLKyE7hfB8Rfs_XowrksKJEpaGOMsbIrcDAtCH9dX0kBVwg-ZXrF5xejJMSYcD8dV34tU2jwDABerXwxGV02h003n9IxcW27lJpaKs-0eV32PMHeK375qhwaRThkIXT3KY9rqyYbJwFFRvi8L10wNhOqVo4jEI7S4LH8X8JhgyH6jnUZw1dCn2gVNZhDWvpbkmMnFOFtHebEOl7r3-jhkxZMjg2UymPsCIqNmfFwvKbiH-lgTutjEGBAMmRDt8F3wOC5OclvHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804a06c2f5.mp4?token=XSRjIOFf7RWMuPsqPF1dAIR2cAG5A3OLBe8NkDifDChjirK_CDG8H8SW48DTLOikWmc1AUYArUQ_QLKyE7hfB8Rfs_XowrksKJEpaGOMsbIrcDAtCH9dX0kBVwg-ZXrF5xejJMSYcD8dV34tU2jwDABerXwxGV02h003n9IxcW27lJpaKs-0eV32PMHeK375qhwaRThkIXT3KY9rqyYbJwFFRvi8L10wNhOqVo4jEI7S4LH8X8JhgyH6jnUZw1dCn2gVNZhDWvpbkmMnFOFtHebEOl7r3-jhkxZMjg2UymPsCIqNmfFwvKbiH-lgTutjEGBAMmRDt8F3wOC5OclvHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الحوثی: رژیم سعودی برای حفاظت از رژیم صهیونیستی برخی پهپادها و موشک‌های شلیک‌شدۀ ما را رهگیری می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453601" target="_blank">📅 18:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453600">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرهای تأیید نشده از حملات عربستان به صنعا
🔹
برخی منابع از شنیده شدن صدای چند انفجار در پایتخت یمن خبر داده و گفتند این انفجارها ناشی از حملات عربستان است.
🔹
هنوز منابع رسمی یمن، صحت این اخبار را تأیید نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453600" target="_blank">📅 18:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453599">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
مسیر پیاده‌روی نجف به کربلا، ۵ روز مانده به اربعین
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453599" target="_blank">📅 18:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453598">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c2e264da.mp4?token=m5XxadwX4-fOghXSHdGFklcaDgPpdXZDhmjf_v1DLhlTGrXicf9yQoXPJtYov85s_zw5_Bdthamzlly3umc8PAUEXlcOJ9yC1I7RfrPkXUtI_Diz1yA_nokHKjp_X2fD_a0fNVQH_pzAX3y8av_hEeM-nkdEQtvgZ8bQ6kFzuO5BuWESPEvJQBdPvDxLFeKlTB1ZIF4I09gHI-ylpBFV7_EZhi5voEBEjwd3-hj6wxjJGoyqpNQGBoPfDrAwimKz7lLflFpZSJ0nYH3VjpHIlxxdj8joPAmGC--E8REvFdf7ZrXSGNrD-63lW77WQ_WwarXm-5yM-NphYFY5m_eY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c2e264da.mp4?token=m5XxadwX4-fOghXSHdGFklcaDgPpdXZDhmjf_v1DLhlTGrXicf9yQoXPJtYov85s_zw5_Bdthamzlly3umc8PAUEXlcOJ9yC1I7RfrPkXUtI_Diz1yA_nokHKjp_X2fD_a0fNVQH_pzAX3y8av_hEeM-nkdEQtvgZ8bQ6kFzuO5BuWESPEvJQBdPvDxLFeKlTB1ZIF4I09gHI-ylpBFV7_EZhi5voEBEjwd3-hj6wxjJGoyqpNQGBoPfDrAwimKz7lLflFpZSJ0nYH3VjpHIlxxdj8joPAmGC--E8REvFdf7ZrXSGNrD-63lW77WQ_WwarXm-5yM-NphYFY5m_eY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انصارالله یمن: حتی چهارپایان و الاغ‌ها هم از دست رژیم سعودی در امان نیستند.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453598" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453597">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شهادت یک مامور در درگیری با سارقان مسلح شادگان
🔹
فرمانده انتظامی شادگان: در پی درگیری مسلحانه میان مأموران و سارقان در شهرستان شادگان، یکی از قاچاقچیان به‌طور ناگهانی به‌سمت ماموران پلیس تیراندازی کرد.
🔹
یکی از کارکنان پلیس در این اقدام ناجوانمردانه به شهادت رسید. اقدامات برای دستگیری ضارب آغاز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453597" target="_blank">📅 17:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDLPBcAApJ5KVAosrmC7itTGsBVESqToYsX4f824G1svvYrFrh1xeWlZMdxTTdo6mDzIAhSkOnhNxXNDNA-f8HgF1Mo8xVHwNG5AlRRvJ9Rc4AB2VZiYRisMOub4Vioppifoq62dJ1APLvQ0Fq_WkvseKsJTbc8YibTVYDhpn6T2DCIgZDDhfxOBE4YhMs8KPtOUrhkMaZSBzDx_q4i3Cii2SubgTrsw4WRxjcX-gEIDX1w5hW8n2O7bxz2GvqVAnFEWhkj1ZoXx6wDkaakw1iZ3xrfFd10hbGYKlR7VpnuCA1Qxq1IR4D7DHsTGY5KUgYCq_WAWj4kxcS14mkx3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30beb59350.mp4?token=LZHNjsF-THH-wLdp6I-Hk7--IgPNPqNnCL4JOn253W97q33qiWTIMFMEpPSmFUusCsk8i2-fNG5BHR3XCfbVpH8Aphj16oihjvDT4CETg1UM-IJj5jdL0jUWEyzi_oHNMAuuc-sz-JTucN9n13JtKYLtJK3E_it-nSnYLbBjZf_7yW4a5Q7s4As8vLD8qCha6fp9aBpDWZsVWqQLnVAkQlcTOR0dFAsOOaaAKo1kB2qUGcYZli_ZIlb1iJADWnqE50V3goJsWRGFvrybwIw8id-so5PouoOfdJOlq7fzgvYUAmubaVuEcgIADrV5Wm5zPaIKLPYLA30eyBSk_rGc_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30beb59350.mp4?token=LZHNjsF-THH-wLdp6I-Hk7--IgPNPqNnCL4JOn253W97q33qiWTIMFMEpPSmFUusCsk8i2-fNG5BHR3XCfbVpH8Aphj16oihjvDT4CETg1UM-IJj5jdL0jUWEyzi_oHNMAuuc-sz-JTucN9n13JtKYLtJK3E_it-nSnYLbBjZf_7yW4a5Q7s4As8vLD8qCha6fp9aBpDWZsVWqQLnVAkQlcTOR0dFAsOOaaAKo1kB2qUGcYZli_ZIlb1iJADWnqE50V3goJsWRGFvrybwIw8id-so5PouoOfdJOlq7fzgvYUAmubaVuEcgIADrV5Wm5zPaIKLPYLA30eyBSk_rGc_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌بس اسرائیلی؛ زید ۱.۵ ساله در خواب سوخت
🔹
اسرائیل شب گذشته باز هم مرکز و جنوب نوار غزه را بمباران کرد و شمار دیگری از کودکان غزه را به خاک و خون کشید. یکی از قربانیان، «زید محمد نوفل» یک‌ونیم‌ساله بود که مادرش پیش‌تر سه فرزند دیگرش را از دست داده بود.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453595" target="_blank">📅 17:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c33fc1d5.mp4?token=Zlli6HkSr6RqhYVQJ8S0JF3Q9Tb18Ru9MLuHT2vBKbaVOIj5gOU9hzUM6mXI4VfZMBfCoAjLw7PYT7WmQ_-D2cgPXDjQ2-WETlrsRj9Ud8xCktrvw0De94PPrgG8ZdGyfilhDNbyDdFFJfZSuFj5baoOHrk_j56vvN8Il__YJQXpGhjkz22TJ4lkyVDMp5euS3R-vWbYp2HT3PI8oiQroKoZb5GBrWmPOeu0W3TSQ3rctG3lgWV2P-BZ0HQzJ51rfQEX4bKYvEuN6bJRfOTFomf-xoQajEkiIBERVlfgGd7eW46K3xEtWKV5_dEMqGG3431g0b6AnZ2BtxdwHTgGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c33fc1d5.mp4?token=Zlli6HkSr6RqhYVQJ8S0JF3Q9Tb18Ru9MLuHT2vBKbaVOIj5gOU9hzUM6mXI4VfZMBfCoAjLw7PYT7WmQ_-D2cgPXDjQ2-WETlrsRj9Ud8xCktrvw0De94PPrgG8ZdGyfilhDNbyDdFFJfZSuFj5baoOHrk_j56vvN8Il__YJQXpGhjkz22TJ4lkyVDMp5euS3R-vWbYp2HT3PI8oiQroKoZb5GBrWmPOeu0W3TSQ3rctG3lgWV2P-BZ0HQzJ51rfQEX4bKYvEuN6bJRfOTFomf-xoQajEkiIBERVlfgGd7eW46K3xEtWKV5_dEMqGG3431g0b6AnZ2BtxdwHTgGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام قنبریان: خون‌خواهی رهبر شهید باعث خیرخواهی برای ملت است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453594" target="_blank">📅 17:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04131030f2.mp4?token=mXe50RrOVwfvQffjNOmQUB3h7-vBhZyNdR2Qnbl1iqmWpcEpKz3ju7mtSZIZ8yEOd3VkgnG92YptBvCNHL47n2aRdArrisLZxk4lG0SBatMTHcOd4T_BwLz88Cpl8wAZm9ztVqLg2_0LgEoVa7AzYy98qo0XdfXXW4r6ypmEFw7LuGoKUQezgzifBQSRi5cxflni_3cyPIhOJMogrLgbNFNOb41S9AEy59dKExWA_x3M2b6gWj__EJS8sSOlDG3zcPZXSWdH_Nx8RSgS1EsLnCjQAWQ1_Xp0e21sRUovNg6STODSWgzGVYex7Q4862L1VTUnmlsv26TfwPFQJovb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04131030f2.mp4?token=mXe50RrOVwfvQffjNOmQUB3h7-vBhZyNdR2Qnbl1iqmWpcEpKz3ju7mtSZIZ8yEOd3VkgnG92YptBvCNHL47n2aRdArrisLZxk4lG0SBatMTHcOd4T_BwLz88Cpl8wAZm9ztVqLg2_0LgEoVa7AzYy98qo0XdfXXW4r6ypmEFw7LuGoKUQezgzifBQSRi5cxflni_3cyPIhOJMogrLgbNFNOb41S9AEy59dKExWA_x3M2b6gWj__EJS8sSOlDG3zcPZXSWdH_Nx8RSgS1EsLnCjQAWQ1_Xp0e21sRUovNg6STODSWgzGVYex7Q4862L1VTUnmlsv26TfwPFQJovb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر انصارالله یمن: رژیم سعودی نقشۀ آمریکا، اسرائیل و انگلیس را پیاده می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453593" target="_blank">📅 17:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca567ea645.mp4?token=ojNwWmWNxxVQjlBGEuVfboiMqfvBto-1xjDxF2oJf4ZxFxNzlJWChLiYm9EYAfB_Ve_HSnOLvV7cYkIPnIQnoBv9zkjA99dwfVPLvB08UnqjN4LjWtULXBiNxGCNQLt-OnvcBhYUjuhZugKUrGQ-SrS43HLCt40O78_uEtxl4yVcz4eZ9OjxLi1lpgbI6Us3N3iudxMLeVsjgzGCP0c-WvDnmBLQ2TQ4t-dLxEEGSFL2DFfCNk6BJViwVgotJ3ckjiNfW0zov9T6vOGywf4aIwr0WI5h9IBp-U6NXBveHywdq9eDBBnQoFBqoWX5dmjibqDBoEDDwMzJaAlmTP_YNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca567ea645.mp4?token=ojNwWmWNxxVQjlBGEuVfboiMqfvBto-1xjDxF2oJf4ZxFxNzlJWChLiYm9EYAfB_Ve_HSnOLvV7cYkIPnIQnoBv9zkjA99dwfVPLvB08UnqjN4LjWtULXBiNxGCNQLt-OnvcBhYUjuhZugKUrGQ-SrS43HLCt40O78_uEtxl4yVcz4eZ9OjxLi1lpgbI6Us3N3iudxMLeVsjgzGCP0c-WvDnmBLQ2TQ4t-dLxEEGSFL2DFfCNk6BJViwVgotJ3ckjiNfW0zov9T6vOGywf4aIwr0WI5h9IBp-U6NXBveHywdq9eDBBnQoFBqoWX5dmjibqDBoEDDwMzJaAlmTP_YNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد آسان زائران اربعین از مرز خسروی
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453592" target="_blank">📅 17:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
رهبر انصارالله یمن: رژیم سعودی نقشۀ آمریکا، اسرائیل و انگلیس را پیاده می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453591" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e642c32a43.mp4?token=iNAzJJfhBnfMQ71D9CTBJQT52C_K0K-CbnRY0pc9tKaVwVNBR8-ntlMfERkZ_VQ9mCXjdjI2KpyVvMd9SXSZ8GYuH7wr11tnePTdvxNGPWDprPn4DZiyRo7UIu_AdQyU1-Ry8TIcdk4ZRi_Q6Mk_x3c_-IVUxbGjaq1dWAw0DWmNyDb-vQVMil_YzYlA3EPe_aBDvweWKeQob7lPPDHEiuPQNvduLkIlfJKABLg-zwQe7Ko6zdPt942_BcK5GgMqO23OQf_TI50d87fdkc8evDn13DZjBvlb2bZjowfolkeKXaJO8RDj3rbHVfMx2wuSEpSe8Ffe8Ao9EvT2pcbbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e642c32a43.mp4?token=iNAzJJfhBnfMQ71D9CTBJQT52C_K0K-CbnRY0pc9tKaVwVNBR8-ntlMfERkZ_VQ9mCXjdjI2KpyVvMd9SXSZ8GYuH7wr11tnePTdvxNGPWDprPn4DZiyRo7UIu_AdQyU1-Ry8TIcdk4ZRi_Q6Mk_x3c_-IVUxbGjaq1dWAw0DWmNyDb-vQVMil_YzYlA3EPe_aBDvweWKeQob7lPPDHEiuPQNvduLkIlfJKABLg-zwQe7Ko6zdPt942_BcK5GgMqO23OQf_TI50d87fdkc8evDn13DZjBvlb2bZjowfolkeKXaJO8RDj3rbHVfMx2wuSEpSe8Ffe8Ao9EvT2pcbbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  رهبر انصارالله یمن: کشورهای سازشکار نیز از گزند طرح خاورمیانه بزرگ اسرائیل در امان نخواهند ماند  ‌
🔹
نگاه آمریکا و صهیونیست‌ها به کشورهایی که به آن‌ها وفادار هستند، تحقیرآمیز و بی‌اعتنا است و آن‌ها ابزاری هستند که دشمن زمانی که به آن‌ها نیاز نداشته باشد…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453590" target="_blank">📅 17:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
رهبر انصارالله یمن: نشانه‌های خطرناکی وجود دارد که دشمن صهیونیستی در حال آماده‌سازی یک عملیات تخریبی در بخش‌هایی از مسجد الاقصی است.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453589" target="_blank">📅 16:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رهبر انصارالله: هدف اصلی دشمنان تغییر چهرۀ خاورمیانه و ایجاد اسرائیل بزرگ است
🔹
تجاوزات دشمنان علیه جمهوری اسلامی ایران، لبنان، فلسطین و تمام امت اسلامی در راستای از بین بردن موانع این طرح صهیونیستی در منطقه است.
🔹
دشمن آمریکایی به صراحت نشان داده است که دشمنی…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453588" target="_blank">📅 16:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1JGNiAEGVv0N10XuzJZ2oJ-yOpwfZpXnBZURRBcsuLQim__wFX94rBfz213Rco9iESyaSSORI-V0Z6GH1kOYKcspV0tpOnwCt3Qs_UOjv2WJPbHhHw5A34ibW3VOG_YNc2h-dtj5qwQ9YwExIyOYufZGBO41eKuZ5J5-xeao8ZmJuNhDKXKEwouDsEA763WWhXJThR6h_zlJYSfDIVJUJcYEWVxFBxm19e8ANS4sD-0mlT1z3kzNCmb_RowTE4lV_qiivY8keOxlWI-PWO5EIpfMTG3y0su6i5KfubN03Ujh0qauSysIZ7Zan3RDjXIBdPw0I_1namgqCAuwIwlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله: هدف اصلی دشمنان تغییر چهرۀ خاورمیانه و ایجاد اسرائیل بزرگ است
🔹
تجاوزات دشمنان علیه جمهوری اسلامی ایران، لبنان، فلسطین و تمام امت اسلامی در راستای از بین بردن موانع این طرح صهیونیستی در منطقه است.
🔹
دشمن آمریکایی به صراحت نشان داده است که دشمنی طمع‌کار است که از دوردست‌ها به منطقه ما آمده تا اشغال کند، بکشد، غارت کند، آزادی مردم امت ما را سلب کند و بر آنها مسلط شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453587" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
یمن: به مصر حمله نکرده‌ایم؛ فقط عربستان را می‌زنیم
🔹
یک منبع مسئول در وزارت خارجۀ یمن: شایعات دربارۀ حمله به تأسیسات گازی توسط انصارالله در بندر دمیاط مصر را تکذیب می‌کنیم.
🔹
موضع یمن روشن، علنی و صریح است و فقط رژیم سعودی را به‌دلیل محاصره و تجاوز مستمر علیه مردم یمن هدف قرار می‌دهیم.
🔹
عربستان با طرح چنین ادعاهایی در تلاش است خود را از مخمصه نجات دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453586" target="_blank">📅 16:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQV30QrppYQPCp8CUN3IMKUgj13p6H4MXeZOQRNnW1Cm_mtHhgLBnfwxOq5ExgkzNzVukH1zpyVg8ls3ja3kh3Xej6siEOcNBe9f7uhd7PaYRLisYf2Y7fHAjgPismgLBIaGM4SBkcWvcjwIH_XMB1VHTOJzORBjjANiUMUOIWaPtsET9v61T2sJ-UNIgDZvl1Didj_2DoZs9Xi-qUumQEOCi7gv9WFrV_jns0--OxUz6Aecf5mTl8ISd-u8RAUGyW08ZHWma9yoiHSfKBSsIrS4CuktyUI7N-tIi54mLUJnTGg-mtdz2KlHozyxJruoebvJN9kWq8XxYGJ72VwpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMfiKJJPRoHSGLFqCpGkfeymZI6qjmbUtyp0vOrVs-_uT1TbzRrKMpAv0uIC0xWJgywQ4rjTnbYEvv_XWu_IfmyVAlgHo7rLGdqs8WrioPb8_BGl2l3_NLgKnJRHlBkJQEgMK2b0RfaAVfJYQA2Gh8VB1Oxjz-jJQsbuDqnMCbeVpCVKtIzYbYPkxcmEMEoQOP0AftzI4-5_godmN1tf2G4E7CkWLxgskMXG1ONFa6OVhKogO5HorBZEFhmRape7-5wjuwLFjEmBrHef6CwM0hR2ay382xDOm1VZGEG4wh1UT9Zs0Yd11Snkx2q3L4kIKMwv9Y0f5NbD-uew68sOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwjEkZHZX5lAxKDtm1MQHIa1Pc0bzoOFs8qkOWMkMyM_ketOEkqFH-eMwgJMKyf8-RTnrXS7LA7N2SMe89UxSJrvlhUty3WEErFiHtK2wlS_rZ1uf8bMdJE3x8pGLyRerQrxLZG3aoVBGdPNRwC3jMoqRnFD4pQo8cvB1K2xypX1K8nYYMNdxVTrh1o3bI013Nkufp32sbe4u9RFH8Btbmg_OqZonht1VfR66KStb7xOYcDBwnpiwfhRM2J_g1yFn_fG11gvygxCZEH1fuj05HjA7WZcEk7S0v9Z_rao9yrTdMTptdGNivjnnPxj6glzU34Diohv3bKFl0mcCm25tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ia0fekxoiG_cRaW-C5oBMZYqAD9ZL3wWA7K_SqoR31rYg7CQ4qkoFXALkxlqSrq5gLeKUMGGn62mFOtgc72bwFz-rzcIe7Lbij4a4gCsu7xHEUJTN41pcOvTBlY_WOI1OBr9aaCAtQQf9cK6_LUIv77VDBqXzrAiC865pRPjzoWtO8Vjj4OusggEUowePX5OilJZk27Ik1vO52rKJB2mtrdsdkDVPBDU2_1sI_x1QFtPS7Ajg5D0LFHbkHEsGYEtDstbgEmRguNDFZ38i4dYgEuSn6U9PnftJWSvtOG3KFWvGNbrbaKCg-i_KK8ohXynwBMjkFop2VDtxabc7qfl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMbl-XTUqjDLk067PGaw6PNXM4a8-6TnhedNTs4Pqe09dPvcvBu8kuRqishw22T60l54zK11GEnyFjBBjfdG4CwD4o8G65QOjNYMokbUVF5IEof2J9fT6lynUWUNJK2ddbAjzuTo8VpcB40fHB1HgKgQQFEznXsScGxwqy2jT-vgvB2uUGtJoBUXK3B42ihOFmKt2xaAPQQ7iNXXL46okeBtGufelyZr01zCa-9gPgcpUXh_FvBeuim4YxAeTaNngEW4Kim1pIqXGKP1rheIbi_WfNGdaTsNY7md5pJqdDKwV7p7L4h1sTXkqckhk5YYbBLfk7XBY40xisa4vWkWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fo8-EF9Or7_zbUB02Dvmy42nGtjoY3uVce0uZ3ogxxpTq9SgWyjR4tTOtE3PGEz4kkgO6a5ZIGn58C0fsTDGE6ikwiEnVW9EX-MkV9N92r4LUFRjwKktPF9_GPrnVnX6eYI4e-FodWt1fVOL8ct2UgZa1jaKBRu0XzlBo3rWh9aoi_xXUn_IOWPBxvC9K7OxvJ4k_8tgBELKbHpvPyZkjjbYDQFv6LzYxN3CiMWHQbBDNy1p3wqX2CeVhliZeZ0zWn_K7kXGwB1AVWRw4UoOp9VyPd3dk6DJwTtsGo9e8GH7jrDeWY4qJ9iWlxdFTHyWaG-4cXhPSxXi6NEGAhm3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2z6k7sEQpBQXM2OmT5KHMWruwQZzu-M9PGRAhkazQYKlyLQSCz2CGggHjovnPYF9itX0AukTs_e7OWcVaIKC9GFYONhO32Yyu4yLrnr25tN4rvAFLxTEAe-e0Ibke7mCMAAP-LneIcEERKjCj0KMaaDwuzBNpPT4CnlDSbrcLHwEO1-Gk8XlRNmg2fduFE6mfiheXWF2Z7E--_8AeJWh2WEq1stIM9zn31Jmn6Ip4LvkrG7gD-HLKW--MVVpQo-KxM1e03I--VmAQNDW1fphFLOmA3bgVB3rzcSqXt9wHt2eGlybMDYqpUWwrMkYtSjf1q9a7ZbdoWqvIDP11oR4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خدمت‌رسانی موکب‌های اربعین در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453579" target="_blank">📅 16:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npeE04GFxafFOPe3KrvGT8KgUVl75ZmYXjCc143Z0bx9bHb-X6E3tY1qZiTmLU2DkYA7HcpY1MuKhE4Y3AFNXv1uYTm1hMlid9tJoSD-rnWtnCAFcl1mj_WgBCCOdsrWDjiwOmGOuTvBdvLQtlRp-lQtc6yG_B4Pe0wEfk5p37rt-Y-tq67jvC95ab5fhjx3Yn4wrKyvhnIu7cUH_G5ODUmqgzySWYYVGwbEppD45HeApVZQ1P-cI362kbNxmeI206cWLe74YYQkGDafkhsriTUVdbTcvXGYlslYCTnmwB6p4uIA3s5-7EtUsm9PVhOMoFkG7vceoCVooI3s-lJliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار عراقچی به وزیر خارجه بلغارستان
🔹
سیدعباس عراقچی امروز در پاسخ به تماس تلفنی ولیسلاوا پترووا، وزیر امور خارجه بلغارستان گفت: موافقت دولت بلغارستان با درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» با هدف پشتیبانی از عملیات نظامی، از نظر ما محکوم، غیرقابل قبول و مغایر با روابط سنتی و دوستانه دو کشور است و مناسب است  دولت بلغارستان با فوریت در تصمیم اتخاذ شده تجدیدنظر کند.
🔹
وی افزود: جمهوری اسلامی ایران در دفاع از منافع و امنیت ملی خود در برابر هرگونه تعرض و اقدام خصمانه تردید نخواهد کرد و قطعاً هر طرفی که به هر نحوی در ارتکاب حمله نظامی علیه ایران مشارکت کند، باید مسئولیت تبعات آن را بپذیرد.
🔹
وزیر خارجه بلغارستان هم گفت: بلغارستان قصد مشارکت در جنگ را ندارد و بر حمایت از دیپلماسی و کاهش تنش در منطقه تاکید می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453578" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509315b70a.mp4?token=mIicuuYdzQayAj4p_-4x5CoGeFSHsgZpLpwPFK4eO3Ko0DrnaYFhHkWH6ix0kCuXgzwviYO4v3vaQFuHx0btWU4PEByKgeFYjoWgI3B-ZQ4s-yVNXi4w1bQxkhHOvLNsmA15c7BOKWFKkGtajEeZ2ao266aDp4YrgzyG4Eqtudi9nJYIpuzgmMDdpuzTSnOcjKdDaokZw3tcK2oA0nQgsi_GhjfBW7FZNLxt6j79OLC9pgn2x8fAWI6xoiQScUdy5BFEQ9b7YbQP1LOpt2yCRFx4feGEgmxeV2ANIiBmHhvwmqqT-4xxyUpw8mleQScEHOF305vC7pANHBKlRtzb4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509315b70a.mp4?token=mIicuuYdzQayAj4p_-4x5CoGeFSHsgZpLpwPFK4eO3Ko0DrnaYFhHkWH6ix0kCuXgzwviYO4v3vaQFuHx0btWU4PEByKgeFYjoWgI3B-ZQ4s-yVNXi4w1bQxkhHOvLNsmA15c7BOKWFKkGtajEeZ2ao266aDp4YrgzyG4Eqtudi9nJYIpuzgmMDdpuzTSnOcjKdDaokZw3tcK2oA0nQgsi_GhjfBW7FZNLxt6j79OLC9pgn2x8fAWI6xoiQScUdy5BFEQ9b7YbQP1LOpt2yCRFx4feGEgmxeV2ANIiBmHhvwmqqT-4xxyUpw8mleQScEHOF305vC7pANHBKlRtzb4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: بالگردهای نظامی در پایگاه آمریکایی علی السالم منهدم شدند
🔹
روابط عمومی سپاه پاسداران: مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453577" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2fNd3K-aWrPQWD6nqDuHP1_gQrEKvJqfl0rviRWsnERBypFEYjgVKzuQh6tPJBInx_dCZshIEhGZ7tNCIRSI05o6AShq8IgDXpdkxH1HLB2icGNls5Al0jvSp1l6gEFJnaIY6aaW2k9aTykR3MBwtm8ZPDjfLHodfJBGDaz6Qjun_EAAPJNeAHdegElz05P6W1hEYkbnuJZ6_QElNL6BQd3HOAqrL2gnkVVPGjs6XGM0XHZWilGG7EmC462v6ci498trxSwBwmKdHWrCKN3a5Rf6wMec3SyUlu2onPIQSyc7BqO_8mJAXYMbU3EefXtAKS9w2IAqINNWU0m1OmyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: بالگردهای نظامی در پایگاه آمریکایی علی السالم منهدم شدند
🔹
روابط عمومی سپاه پاسداران: مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453576" target="_blank">📅 16:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
سپاه: بالگردهای نظامی در پایگاه آمریکایی علی السالم منهدم شدند
🔹
روابط عمومی سپاه پاسداران: مردم شریف و بزرگوار ایران، صد و پنجاه شب متوالی است که شما بدون وقفه تجمعات خود را در سراسر ایران اسلامی ادامه داده و انتقام خون امام شهید و اخراج متجاوزان آمریکایی از منطقه را مطالبه می نمائید. همگام با شما، فرزندانتان در نیروی هوافضا و نیروی زمینی سپاه پاسداران انقلاب اسلامی در میدان، نبرد با دشمن متجاوز را با قدرت و شجاعت ادامه می دهند.
🔹
صبح امروز در ادامه عملیات نصر ۲ و تنبیه متجاوز با حمله به پایگاه هوایی آمریکا در علی السالم، دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی را به آتش کشیده و منهدم کردند.
🔹
مردم مسلمان کویت بدانند، تنبیه متجاوز تا پایان دادن به غارت ثروت‌ها و منابع ملی مسلمانان و اخراج اشغالگران و غارتگران آمریکایی از منطقه ادامه دارد.
و ما النصر الا من عندالله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453575" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
قصه ۲ دختری که در یک عروج خانوادگی پرکشیدند و شهید شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453574" target="_blank">📅 16:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71bf858467.mp4?token=AV2i2oLLdclbEDC3QQIGgMOebvMCZknxABvzCAsnATowqtPwmkSIFi8jfTo2gZpDSmju67oOCDO97otx6KMeWN8cRPpLPcYoWUinAuDB5ikeasRnsKgvjv9TLFCWkDggylcSvarMAADq0sIu4s7txJb0CJjbSa6PcKP4WCsMIX1rexPaqpmQonf_rmFxa4GvS_nWSmrXNNi0AAXjUBn1ex-6WE2lCzUJknt_Uk0WblwhbHSFIonXbMawfuvpNfAxLFZKK1QPXsINWDwB0ztVREcqy8CwBneSbUwl5WgE0rQ3z0Hkqpxg-1nKf3lWKO59tM8ntJhFnLSHdEfbvPA-bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71bf858467.mp4?token=AV2i2oLLdclbEDC3QQIGgMOebvMCZknxABvzCAsnATowqtPwmkSIFi8jfTo2gZpDSmju67oOCDO97otx6KMeWN8cRPpLPcYoWUinAuDB5ikeasRnsKgvjv9TLFCWkDggylcSvarMAADq0sIu4s7txJb0CJjbSa6PcKP4WCsMIX1rexPaqpmQonf_rmFxa4GvS_nWSmrXNNi0AAXjUBn1ex-6WE2lCzUJknt_Uk0WblwhbHSFIonXbMawfuvpNfAxLFZKK1QPXsINWDwB0ztVREcqy8CwBneSbUwl5WgE0rQ3z0Hkqpxg-1nKf3lWKO59tM8ntJhFnLSHdEfbvPA-bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453573" target="_blank">📅 15:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_jWz0FSL3r8itk6rVrTxcq68vPyBmNhdOH9dIkqa1G2lEvaQs4I_O2yUR_-JVupAFmUUU8bAwVywIL5ItBO44kjoVniu9c9cb8RU7pXkfOdMRFfYs1OAaDJYs0SYy7B1dVbEg6fdPe8-iNtj0n2eEAVyfjs84Im7kDAv3p9Qbcbv4RlazPAK3Lyr-A_EjvHImOj1NGzyS_7jDPEBUZ-NTg92JYKluBcwE0KLRjZNv1_dqyA2elZCmT9rsPucivgIwFbS5m67D9jw21x8elnT8LSN5J8SWdFkPvTgCEeSTOyPodqYRghO7dKcQeBgfzHC3Kfk6sLGEGvKBx9pxcowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ خلبان سوخو ۲۴ ارتش چگونه پایگاه العدید آمریکا را به آتش کشیدند؟
🔹
۱۱ اسفند سال گذشته، ۲ فروند بمب‌افکن سوخو ۲۴ نیروی هوایی ارتش ایران، در پاسخ به حملات ارتش آمریکا و رژیم صهیونی، در عملیاتی از پایگاه هوایی شهید دوران شیراز برخاستند و پس از عبور از سد سامانه‌های…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453572" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
ذوق‌زدگی سلطنت‌طلبان از حملات آمریکا علیه مردم جنوب
@Fars_plus</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453571" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تمدید مهلت ثبت‌نام آزمون‌های علوم پزشکی تا ۲۰ شهریور
🔹
وزارت بهداشت: با توجه به تعویق زمان برگزاری آزمون‌ها، مهلت ثبت‌نام آزمون‌های علوم پایه پزشکی و دندانپزشکی، پیش‌کارورزی و پایان دوره داروسازی تا ۲۰ شهریورماه تمدید شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453570" target="_blank">📅 15:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
اسکان اضطراری ۲۰ خانوار آسیب‌دیده حملات دشمن در قشم
🔹
سازمان منطقۀ آزاد قشم: درپی حملۀ سحرگاه امروز به مناطق مسکونی، ۲۰ خانوار آسیب‌دیده از محله چاه‌تنگو در هتل‌آپارتمان‌های قشم اسکان اضطراری یافتند.
🔹
رسیدگی به وضعیت این خانواده‌ها تا بازگشت شرایط به حالت عادی ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453569" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIRKUqVZCv1AVnblKe1WcZFOWp9jKXRMeS_DfXN-Zq_BURAYaWfOWS5Lh2BfRVOBHSz3Jc8_i1RlFAdTW59w3mqx09u7p2s2lzhzDYbrZDZv-uPRcf1pUj04kRnz1H9P4S4aUJ0oKz4W0ASvwilsFiVCsTr_8Yieh3UXykb5kNTV5B1ppaxjHOY_HM9rc5XNimzS4mJ1MZwY4-Cq1YXHVY4jplalrRlUi7_o13j_bJX19rVNuPb6wABMh9BO0Qii9_lWxLezym5z1xN0BjffxWRLg5AJoHICEt0U7b36El5R75ziY2nTcFbAMakoUDJ9Bvr-sq8kvjbfCzGhL9-Yzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت عراق به محکوم کردن تجاوزگری آمریکا و عربستان اکتفا کرد
🔹
شورای امنیت ملی عراق در نشستی اضطراری به ریاست فالح الزیدی بدون اعلام اقدامی عملی، صرفا به محکوم کردن تجاوز هوایی آمریکایی-سعودی به مقرهای الحشد الشعبی بسنده کرد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/453568" target="_blank">📅 15:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c62c7834.mp4?token=PgHUqQzICYsxzcZLmT1-kPv0VcSbGA7dqEvC0bKA4yLsKVSSNlq_ms1VXlzPHQGBBqPCrMBRd-xIXUqU96sRpm43rw7wQKNa0ZGMWRUPfFziKK-w1c8DIAtDt3DSJJAkrYN5fO68AKoWIb0U8oTV51PokVG7f4cmI5pgZPfyT510MhUCKbgO1JsTnpt2-eh1kGLIbazfj_1RlM9qqzQAFHNKM54uISk_Dfjho8VR2NRbWgCbHCPEQlCyQbBpBUKEI1CT9QrN0tUq7jtKDOhn37WjIPqTEZP_2DfxsJUQehffsV-8VXIURpZOjw2veGN1U2XYg3-Ab31t8baLyQ5bQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c62c7834.mp4?token=PgHUqQzICYsxzcZLmT1-kPv0VcSbGA7dqEvC0bKA4yLsKVSSNlq_ms1VXlzPHQGBBqPCrMBRd-xIXUqU96sRpm43rw7wQKNa0ZGMWRUPfFziKK-w1c8DIAtDt3DSJJAkrYN5fO68AKoWIb0U8oTV51PokVG7f4cmI5pgZPfyT510MhUCKbgO1JsTnpt2-eh1kGLIbazfj_1RlM9qqzQAFHNKM54uISk_Dfjho8VR2NRbWgCbHCPEQlCyQbBpBUKEI1CT9QrN0tUq7jtKDOhn37WjIPqTEZP_2DfxsJUQehffsV-8VXIURpZOjw2veGN1U2XYg3-Ab31t8baLyQ5bQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: ۳ فروند F-35 آمریکا را منهدم کردیم
🔹
​روابط‌عمومی سپاه پاسداران: مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به‌ویژه مواضع صریح گروه‌هایی از نخبگان اردن عرصه را بر دشمن تنگ و آن‌ها را مستأصل کرده است.
🔹
​سحرگاه امروز دشمن آمریکایی عاجزانه از…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453567" target="_blank">📅 14:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انهدام پهپاد متخاصم در آسمان بندر امام‌خمینی(ره)
🔹
سپاه بندر امام خمینی(ره): بامداد امروز یک پهپاد متخاصم در آسمان شهر بندر امام خمینی(ره) رهگیری و منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453566" target="_blank">📅 14:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac1b1dac4.mp4?token=etYT-edscnTBT6d9mAthail8WC_Yl9v7JsLdOaUnJ2T6UGH0_RLOZSnKXzYHFGJbFSwRAt1Z3QNOd0ecRwkup0J7jIxlEBvT3YJYfRk8eLWUnuijl2EjBcM4TeazxTNB9A7RFrwcy6eEwpWHhTxU8wVfaI9nQKzIlCImDaNfZOLVRCdn7VomutJcdyXrlqXp2AL4GKJNzSpGWH7PqAwrOSBG4PvaJUmU6__FZnHmwHuuBAZIRvjlEAZfHrMyEoImRqkKaX1P7MQln6nbbpsYNKZiFP6RPMMlBh2gdNHZwTkPuBHaYV7dLbWtHPHeX9Ge5aWqVkiL0baQZ6vtdBczDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac1b1dac4.mp4?token=etYT-edscnTBT6d9mAthail8WC_Yl9v7JsLdOaUnJ2T6UGH0_RLOZSnKXzYHFGJbFSwRAt1Z3QNOd0ecRwkup0J7jIxlEBvT3YJYfRk8eLWUnuijl2EjBcM4TeazxTNB9A7RFrwcy6eEwpWHhTxU8wVfaI9nQKzIlCImDaNfZOLVRCdn7VomutJcdyXrlqXp2AL4GKJNzSpGWH7PqAwrOSBG4PvaJUmU6__FZnHmwHuuBAZIRvjlEAZfHrMyEoImRqkKaX1P7MQln6nbbpsYNKZiFP6RPMMlBh2gdNHZwTkPuBHaYV7dLbWtHPHeX9Ge5aWqVkiL0baQZ6vtdBczDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم بدرقهٔ زوار حسینی در میدان آزادی تهران برگزار می‌شود
🔸
آیین بدرقه زائران اربعین، امروز با حضور خانواده‌های تهرانی به‌ویژه نوجوانان زائر از میدان آزادی تهران در قالب برنامهٔ «محرم شهر» برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453565" target="_blank">📅 14:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJyWS2J4JdNwxXX3GuWvwafoJcu1DOJWJ8sqeIfr-tDevCfd3YybY5PMKkbIxRB9wqkzjKCGR_gISXBXMMgsVBhroPTyRjpND0bXFzp5pd3VVOdnwEMo4Ty4X3JJ08L9l1CyX5aKBIxWzPPu9Af3tKZZnU5hRltSkbjoC-c_XYaAfosDBKmPMm4e69OdrIm5X8FoPzKWAeu61Aq7Ht50GIXxK8-o5sKcu4pXVJ5JwYZKaePb0rpvPul6AtcXNEX99jBPmqrlD_VQr8Gj2eQQ-Lrrf3pLIqBC8yR-7EB8dlG-aocFGvAMy0YHy2AxNEEjf4egvdAoy7H8C3nF78CUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSKvJJ3w9M4x_CL7X3kdAvCIiQPW7jpW8j6iDF8ZI1NE6kf_NLCoIMyw9gVTMuIAlnfG2Grx_GjIjgOD59GgcK4Y-AzCJ1lZamsFPG8-NQHRq-xLgw4NOW6ZgNwZT61ySopvBjy104UcdOqa_FbwxCMwMjRK54SbnAm83Jj8WNxLDst7KU4-26TYhybswDcxOadZPQeaIuxj18LxIeAXM31w4yuA0I4QIn2fj5kdKuTyjk4L2gqe87_nR-h4T959-Fn2k0TABfrfyisyLXMsill39Y5ihS4jpQ2oa0uxwOa-UBiMB7b_BRGdoYoR7Q8dxB4GfDe0wqVTLu9sxoh-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6mRxtPLJs6XBfY7fBROrmxuixJhpOrD0d14t3IjZT3Zt75Vrscc_GahND_nn58PIfBP-vkQUUmyApPpGoLD7GgvD9WzTzFdgCQZAFLqUudmYffCEHqgAixfGWJa7tHwi-IM__pTYy6PlYpRgcwRZeNIRSpmstDNielcVmDISodTphJ3gVN7VzIN4S7Mx4blRV7St-FtycOAtc6IG2GGKZ7ytBmZ3NlVrAuD1GQ8yIUIPyfN4dY7VCTADZSUxRCHfzYsV59JrSjDbBU2P242KZ0l1RGak7YCuz1C0vwQAOw5ICobEohY5ruNM20eIFxNcnh1poh9uhwjBZYNGnJs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLfOsOTRz0Q8s843kRl_DQaLvW7MEVg2fix0Yfkl2kq2SEae96xQTbqapwg7SfauC___M5ObZPMTjIA0KLtQSL1XtzEjM7vaTyInVFnOytl-fbV7izvT_4kNXMJoBJd96C1hY_0e1GBv8nQTYPIATn1VruhpWwc_xSkG7E80JqaPCwECaNLlwLyi366VA3Eg-Ljad2-_iYfi0j0OvIL26HJkOZd3yriKlyd6cyzW3DT83iXqLGVE9gu-d2aoGNDVkIFp8cj5Ece5vwhQADP9YC1kj3TyaH6_q0w2kgQP7ZUutz8YMA9Sd5O1yMnxzaS8Hyao3ccllV5HWXY_6sXMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/isuXbymHR68LOc8-ANqLiK7yL-3xkyhzUZQ6pgDF0-SmiienLtz4bXfG8JL38LyC-HKKvAt0nPCYpAG8V_zdFFKJymsE4A3n10FNSUhlwkTWIND_fZr6fvzYch9E9HmrpmEbgqV0j9qBzuwK2_G_TsY4ai5Z-oHCoG5A-oWGg5d9Dqrg9epEdKT41N_2IDiVyMIGxSmClrIS9TgtZXrDVmigYGTS3-WH0uyueQDMyqXy-lC9c1uQ4eNmTRGA4Xn9dEDbcnvqo-9ppzSLHn26ueOgnlXjTn4GP-2XCNkESl-961yMa22ezTQ0IIso1AM2m7zMc8TAKXx_qTdB3_qtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfdLx9DSgFonfmiZOwVtzSSANmf08X6THfUo55A_hxc0MtpKkqaMVB7Rs6dfKRQxTKJ1OhYP0TMunOqou_3Oqt9yaNbU5V9voU3xtwCUXYRDcliUMVEZEbk54lLZW0ScIUqkW-x5N1IKgs6nU7_pArJDq-q-61RaVw44v2wWKdgp55A3fhH8S37LmK23jaq7iuloMBgTTwldaTXae5xPth8UflU4GUXebiu5MLAXwt48gbBClciaGlvB5LhNHot0AGZDXVFJJ5YqUZQrk1sibsU5Qos_qperT80ytLdzmD2ujaocAKE3HMwBmrXAim7lOSYkQti-J7sMfHIsSBp73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUkuKbPI3SmDmze9ZzbmlqX-hr8xriXEAsg_jaJFkqf1OKHvo9Ql_xGcVID8GNkFrO7PWMe4xq5g0OZZkLbM8SqxbRhpCHOslGKd2NdIAFwYU9tk6GgcAXk_Di-eTx3wFNOX-BK-lMWyymsEx-5EP3sJSWYsOApFvNKM2_d9YLR7JLRTHFNyZzTte-fgDsPG7JCIimRnMeNLyf3waihH1MywEXjIxKp12WiQlHf9CxRKZhvEBIFLR9seJiFvdEjOaASzT867JFDw5khp-xZaPoj-gWHsUvMGJN0yTaHKwcxQyAWl26xv5AgyJKDq_l2vuh4UK1_g2rMWUicCXJ7RXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد زائران اربعین از مرز باشماق
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453558" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
نقاطی در شهر اهواز هدف حملۀ موشکی دشمن آمریکایی قرار گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453557" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453555">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC7t8OzWMRY9_bwW6euV92a61BtM8vxNcXgwgVDlkoyAajfdrWAr5e-DY7vW83u26xWWRv47BFM7a46XRR7ouerZ7Gxz8XLYVCE3axzszL0pka8Rb-B4ZQPWR5cy6z0DukQqrN1-2w9w9k53Zcgd1icDa8gkiAHWTrRjimzzSCIJeKzPsz5KhyZw9ar7RAH1dbrKLb9j1_YODKb3id1A-2syXfpF1dkeCUL8u9E7x01I9-0oz6sNbZB3TpOzQUv5muPLolJ6lDCJt_QwA7MQBElzlpW4wr_TPcvlb9ciiz5PeH-gdF7wZXJFshQW3tSbAAYzVU_YNvOR7a6fzh85mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی ایرانی خط محاصرۀ آمریکا را شکست
🔹
کشتی کانتینری نورا از خط محاصرۀ آمریکا گذشت و وارد آب‌های آزاد شد؛ این کشتی پیش‌تر در نزدیکی قشم دیده شده بود.
🔸
دور دوم محاصرۀ آمریکا علیه ایران بیش از ۲ هفته است که آغاز شده و دشمن آمریکایی درپی اعمال فشار اقتصادی به ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453555" target="_blank">📅 14:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453554">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY1XRqM1rGj9XpTTMvk1Ij4RzJsxk4ANt_8reqwm72fOse8W9l3ysKz2vnpBLsLQWoxR4sd8dLV2N2Ue75W4la8ABBs-UPICRGguppQlmrd-PCWWrN8JFVCUOskfRtpNqrKDWvRC1OFawJjRQivJsgnHDGhY5RQ80s0GqQYqnoz4mmui01embf-cpoCZGZrwMNCIg90rfX7OvwIQzZWHKH3j9N7OHDgnIZ-MElwFn1YoJ3dK7KS3zQzwUfvK18LvYnBs5VsajSmaWZim1KcdupuFDTRMs1Djw-Xjv0cENOpRtFj7PKxNVt-3191aqXdH-sgdKm345xkIFS0lxyHlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آمریکایی: سناریوی اسرائیل برای فروپاشی ایران شکست خورد
🔹
رسانه آمریکایی «ام‌اس‌نَو» در گزارشی از سفر بنیامین نتانیاهو به واشنگتن نوشت نخست‌وزیر رژیم صهیونیستی بدون دستیابی به راهبردی روشن درباره ایران، کاخ سفید را ترک کرد؛ در حالی که شکست پیش‌بینی‌های تل‌آویو درباره تغییر حاکمیت ایران بیش از گذشته آشکار شده است.
🔹
به نوشته این رسانه، نتانیاهو در شرایطی راهی واشنگتن شد که جنگی که آمریکا و اسرائیل علیه ایران آغاز کرده‌اند، با مخالفت روزافزون افکار عمومی آمریکا و پیچیده‌تر شدن شرایط میدانی روبه‌رو شده است. ام‌اس نَو تأکید می‌کند هر دو رهبر اکنون با پیامدهای جنگی مواجه‌اند که به گفته این گزارش، «از کنترل آن‌ها خارج شده است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453554" target="_blank">📅 14:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه: ۳ فروند F-35 آمریکا را منهدم کردیم
🔹
​روابط‌عمومی سپاه پاسداران: مردم شریف و فهیم اردن؛ همراهی و همکاری صمیمانه شما، به‌ویژه مواضع صریح گروه‌هایی از نخبگان اردن عرصه را بر دشمن تنگ و آن‌ها را مستأصل کرده است.
🔹
​سحرگاه امروز دشمن آمریکایی عاجزانه از رویارویی جوانمردانه نظامی با استفاده از پایگاه‌های اشغالی در کشور شما و حمله هوایی به دو خانه مسکونی با بمب‌های سنگرشکن خود، ۲ خانهٔ ساده مردم محلی در جزیرهٔ قشم را هدف قرار داد که پدر، مادر و یک فرزند خانواده شهید و دو کودک دیگر مجروح شدند.
🔹
​در پاسخ به این جنایت و کمک به شما برای رهایی سرزمین اسلامی اردن از نکبت اشغالگران آمریکایی، صبح امروز رزمندگان نیروی هوافضای سپاه با حمله به رمپ استقرار و سوله تعمیراتی جنگنده‌های F-35 دشمن آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، ۳ فروند هواپیمای F-35 را به‌کلی تخریب و به ۳ فروند دیگر خسارت سنگینی وارد کردند.
🔹
​در این حمله همچنین چند افسر و کادر فنی و تعمیراتی دشمن نیز به هلاکت رسیدند.
🔹
​منطقه ما جای ارتش کودک‌کشی که این‌گونه با قساوت خانواده‌های بی‌گناه را نیمه‌شب در خواب به خاک و خون می‌کشد، نیست.
🔹
مبارزهٔ ما و شما تا اخراج آخرین اشغالگر آمریکایی از سرزمین‌های اسلامی ادامه خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/453553" target="_blank">📅 14:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453552">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e636e78e72.mp4?token=dksrB2esUT8vjrCXFSE6pzSTDlKX7YOZYrgptjJgg_7POccnTmOvexwKU-0Y8Ljl-YmDSZSQrWHvZdptYMxK3MnCnvNDFUW6o5PROaf7zZIwnNph6_nPL6EM-oHNhvpw7Q6Zab1zfJd__SeUr8zGo4kw87tcyIHcFWXfJDeKXzLWCp6lbnSQ-O-DLLUvjctbp4pvXrZ6hXj8ml2rRNHPFk9IPwSakqDRy6N49gJBbs8IqWqhSHvcCDXpzVo7U-cjH2sW0mq9CyFK9cxBwuZJjHoQ4Z9I4Az1UhBHhKW0GQjG8dwyydmWonE0pDbTUATtnnpv_PoHTSnVpApVXtTdFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e636e78e72.mp4?token=dksrB2esUT8vjrCXFSE6pzSTDlKX7YOZYrgptjJgg_7POccnTmOvexwKU-0Y8Ljl-YmDSZSQrWHvZdptYMxK3MnCnvNDFUW6o5PROaf7zZIwnNph6_nPL6EM-oHNhvpw7Q6Zab1zfJd__SeUr8zGo4kw87tcyIHcFWXfJDeKXzLWCp6lbnSQ-O-DLLUvjctbp4pvXrZ6hXj8ml2rRNHPFk9IPwSakqDRy6N49gJBbs8IqWqhSHvcCDXpzVo7U-cjH2sW0mq9CyFK9cxBwuZJjHoQ4Z9I4Az1UhBHhKW0GQjG8dwyydmWonE0pDbTUATtnnpv_PoHTSnVpApVXtTdFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ رهبر شهید انقلاب به زائران اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453552" target="_blank">📅 14:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453551">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زلزله ۴.۵ ریشتری در امیریه استان سمنان
🔹
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453551" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453550">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شهادت ۳ پاسدار مدافع وطن در استان زنجان
🔹
سپاه استان زنجان: در حمله وحشیانه ارتش تروریستی آمریکای جنایت‌کار در بامداد امروز، ۳ تن از پاسداران سرافراز زنجان به نام‌های «محمود ملاجباری»، «محمدرضا چراغی» و «جمال امیری» در دفاع از مرزوبوم ایران اسلامی و مردم انقلابی و شریف ایران اسلامی به فیض شهادت نائل آمدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453550" target="_blank">📅 13:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453549">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR4BoKKzGz-4KYHfbEMEzQOJbCSMZ8WIM5dRXPi0ByN_JIjsVC6If7ZLYYmhPc4q6CXT2AOI9eME7V0r9nBZm_pKgFBF1fDodDduqySwjagjI9mn9uvXgYAZNHcHA7SXiYyOYiwpfoidhnrK9El7VS_7h6YudTPtaROVj5CGPlELHRkfXQCOMMXuhghNMnX94V2fZHp3x3GAVLqed2KUSvGO6o0WNZzYdqc2KHlp5qo1Zxqov-bYyhWx_TkZmV_os8rMaL7FEwSoryz4oQVgRhXMcMcIuqXu-aF-o6lVcKWNVHqLZBXy-R9k9xq6lfQ1KKpU2VFx7wrw5kD_H5B9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان استقلال آبی‌پوش می‌ماند
🔹
وجود اخبار ضدونقیض پیرامون آینده کاپیتان استقلال، ادامه همکاری روزبه چشمی با آبی‌ها تقریباً به مراحل نهایی رسیده و اگر اتفاق خاصی رخ ندهد، تمدید قرارداد این بازیکن به‌زودی اعلام خواهد شد.
🔸
روزبه چشمی که قرار است برای یازدهمین…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453549" target="_blank">📅 13:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453548">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw568qkqPSi2kOfGqR-aHiCC-OyuYC0UnVyZmUQ7abE9WO3pdKZVi3Mf3A9zvwZdy_Tc2DK6ml4x8TWW23o9xJAwjPCFt5KY2CQEAK1guDN9BaBUKKikF-0oJUOmfoacQ3hY3ZmjYmnKPq1RzwRxDzKlkcl_bcFzhgsjXJRIuSRSr8XjENF-7WZU3fSmxauNcVZ1bs1JolSANZIx-o9TAVNxB94GPqywXl-1FBaI9mO_IO7vVcrihvHKHxZUFP6a_7WWadRoOJF3h-wYs3FAguCCg56HWldfz0w5TDtjDEOWcMhfhAbiffqWLX1SnpBQNMCBMiD4Il764ss2C0sG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فروش سایپا: پرداخت جریمۀ دیرکرد در اولویت ما نیست
🔹
معاون فروش و بازاریابی سایپا: اگر نقدینگی داشته باشیم اولویت ما تولید خودرو است و پس از آن جریمه‌های تأخیر را پرداخت می‌کنیم.
🔹
باید ۵ هزار میلیارد تومان جریمه به خریداران بدهیم؛ بنابراین با برخی بانک‌ها…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453548" target="_blank">📅 13:41 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
