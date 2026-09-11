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
<img src="https://cdn4.telesco.pe/file/PADA92dWzcoVkG2MMFL-kV6JCddL1Xa518iWoi1j6RWPNZE2nxq_1glLQdbswKQpVVr1zsxMhGh3FM5yeLd4wyn5rgSdeUJzeBOwYM-bt2AcCjpasmG9wKWIUUNN_JqD_volbI1ie6tqdafsE8tbndpDo_FGuEZFJey9BWOg74-_HP-prIWT-aBfl3mwbb7HVpZ1HWc61TeX8Fk2_1BZe7omBTtLp0dnLRHUQJLCIz_QDfFMCbOsF5_pd5vDU4ar4XDw3NTpAzIjFfBB1QaIXQgI256CWnIv-Jv_Kw6fmXI70J8viLFOMJnx1RgzH4pgFD5L0N_Z3aCpJgZbnNQjaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qia-P_vF1XX_UfyE5sf1mODjf0HuKmM_aLxspRgx-ZtoJAHhZX26lcNYHdK33b1dglUCTjD-hVFxG6vX22Ix9P1fDCiM7v3UVZ44tNIDGjF3Zl53zVMHAo_Cdff3zJUwCf9dlosAhjwicAJX_RtdrkarJsnNNNziYW86XJPmeVNOvUH2oMMIHR9r-67PiAYWEnN-cRfRWQwlbSoEuP5oWGVWnWWPUnsgsbg_pAF3KE7GSDFo12fkzXZBJ0LSKojYvUdi9sQaaZPnDQn2RSsrBukAAwZEfO0l0cZDTKuhP-S_caxClY3bBd1Acpk2bN3qXIjb6Gi86hOrW8DOaiqgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MMj3dUKaTOLzQxCNSksQBTAHxGykFoF8bi_rVBYkBBvLHASudwk1WCtrOWpaWYkLjduY3j-a9qdc5pqXRajERKbZzcyYomnK1TKxsM-nnNMIA_uYbqLQ2BJH4ki9LkRFtIKaeLEtodNWnXQ8nchoEsA1IF7jodkq167grpNjtU0IQmgJJjZ-bwiSlfxWnq8ucXgHwCEJT_aew6to3-KJb5SYSDUPQ1QCP24g1k1UhYa9WTtoiesT-8RlriiB10uGMDplzTtO-qD2-IvkbYrKbDLdsbDLyxbo2KKTghkfOGdheVM5VBv_3gi1wCOTK8PcPSYLQiZTMIhLYyH-7z-Lua_9sr8SwwB6Dm3mZZqN1Mz21CaQH0Op6_N7uHjYtYylLeoS7lCxa52CRrvfEvu59rn8QCCbBDPxnGnSQXtWoKE5Pvx6tqw1xQznNrOqX-wIa2L6wDnIu8SU5LG_yJ6dvl0bxTcXO3sBjqF_uU920n5yCCuzPpnT29YFFQWw6ZOq5zuAgNoYIZ7EbAjtCl7HJ4jHNofg981RasGzDxrYgmozS2CLTJUvmATZor6EDbTGNWMPG3EvNYBSrIhQRWKhQ90MW_MOC2KvZeJw5r8Ggv249etjpU5XQegeBxOzTEScrecxAUBDoIoAWDtMXhHf5wrPhv_M0AHVv9KbqQnRb38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MMj3dUKaTOLzQxCNSksQBTAHxGykFoF8bi_rVBYkBBvLHASudwk1WCtrOWpaWYkLjduY3j-a9qdc5pqXRajERKbZzcyYomnK1TKxsM-nnNMIA_uYbqLQ2BJH4ki9LkRFtIKaeLEtodNWnXQ8nchoEsA1IF7jodkq167grpNjtU0IQmgJJjZ-bwiSlfxWnq8ucXgHwCEJT_aew6to3-KJb5SYSDUPQ1QCP24g1k1UhYa9WTtoiesT-8RlriiB10uGMDplzTtO-qD2-IvkbYrKbDLdsbDLyxbo2KKTghkfOGdheVM5VBv_3gi1wCOTK8PcPSYLQiZTMIhLYyH-7z-Lua_9sr8SwwB6Dm3mZZqN1Mz21CaQH0Op6_N7uHjYtYylLeoS7lCxa52CRrvfEvu59rn8QCCbBDPxnGnSQXtWoKE5Pvx6tqw1xQznNrOqX-wIa2L6wDnIu8SU5LG_yJ6dvl0bxTcXO3sBjqF_uU920n5yCCuzPpnT29YFFQWw6ZOq5zuAgNoYIZ7EbAjtCl7HJ4jHNofg981RasGzDxrYgmozS2CLTJUvmATZor6EDbTGNWMPG3EvNYBSrIhQRWKhQ90MW_MOC2KvZeJw5r8Ggv249etjpU5XQegeBxOzTEScrecxAUBDoIoAWDtMXhHf5wrPhv_M0AHVv9KbqQnRb38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rtIy4Eyimgli-AUpel4-NAZ5Xl9RgLzDofoeFfO4yv_aYxKSVaRjvMV9TYY4-C5WYE4uejPsGW4fuDb5XI3_kQRHU3wgJf1qhn4Kr6l-R_rYmqtqXsvB2GnGAOwiF44EvjtzpWN5wW1lrrUUTfQhALkQG4K8tZUPepcKEiQmk1j6vj6Engz7jR7_7s4izNaSYu4_PPzek7tbsifP4GB6fEc8VS4NExUk-MHluoM4U3kv43-3H7QyJHrjy7HDdUDZDwlRBhWULEebTbTlWY4uRwywqjaU4nnbRwHqV7x5UOpfqH3CVFwO2waQ1W1ur8EmEI5uFyCRSLhgJz72Prm24a2j-rkL26EmjqSLViw_MMKY6v5ydC8OJk8EdrkPw_qhBkYe1DRgK1XPgcWksl8yJ3NMunfEdT3TAEXq6Th2ZMWzMMLzZ325VgW5d3pP6faa5AGKI-FzZL_c84PsONbk2TsIERM-DEd3XeX3MtWXTG05pK0Z8zERqcYV2CgrBwGzQJdM4aKWGwSGwdhhKrzIz536UWXCy1qJhNwcZnu_cjtbsENtBNZ55BlEZ1GnmhAvHwVt7Mae2wlH0fwRqv-1iZ674jpwUlXGPaqX9rL7geVOugeb88o--_I78CcrxEoNG7gg_Tzcj8rS0Q8coy-5o9c21s9bypXZ66EYOgcoLeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rtIy4Eyimgli-AUpel4-NAZ5Xl9RgLzDofoeFfO4yv_aYxKSVaRjvMV9TYY4-C5WYE4uejPsGW4fuDb5XI3_kQRHU3wgJf1qhn4Kr6l-R_rYmqtqXsvB2GnGAOwiF44EvjtzpWN5wW1lrrUUTfQhALkQG4K8tZUPepcKEiQmk1j6vj6Engz7jR7_7s4izNaSYu4_PPzek7tbsifP4GB6fEc8VS4NExUk-MHluoM4U3kv43-3H7QyJHrjy7HDdUDZDwlRBhWULEebTbTlWY4uRwywqjaU4nnbRwHqV7x5UOpfqH3CVFwO2waQ1W1ur8EmEI5uFyCRSLhgJz72Prm24a2j-rkL26EmjqSLViw_MMKY6v5ydC8OJk8EdrkPw_qhBkYe1DRgK1XPgcWksl8yJ3NMunfEdT3TAEXq6Th2ZMWzMMLzZ325VgW5d3pP6faa5AGKI-FzZL_c84PsONbk2TsIERM-DEd3XeX3MtWXTG05pK0Z8zERqcYV2CgrBwGzQJdM4aKWGwSGwdhhKrzIz536UWXCy1qJhNwcZnu_cjtbsENtBNZ55BlEZ1GnmhAvHwVt7Mae2wlH0fwRqv-1iZ674jpwUlXGPaqX9rL7geVOugeb88o--_I78CcrxEoNG7gg_Tzcj8rS0Q8coy-5o9c21s9bypXZ66EYOgcoLeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KIbnb80nsbs7h1CSs22c02oIGCYoGY8mHb0hiGmPi9TPdu3-WcPT353-r5LmBdG8i6AkSmgXKmtIM9_6R5pcIg3FL4O1UxRYvd8jgepMqHUDACqHPQcde5xtFXPjmtvqTS527Et2yQN4SOdX_W51K2vrmHkROGujcZ8_YXK1aOGQ32pjafVhI8GFkKLsQHP-Q3z-oyUqmEcGz8XaSSBl-3Kk_r_RIW1y-ylBG_3k2Vigxx-etq-DMpTjHLShkWXvAOkqD2V0_rniO1r7XSe0FJQe_d4ZY-Vm2JdXjfAFszN7a0F10U-ufpbf1p9id_qJYvS1GRh2UzbjEIxTrVRFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KIbnb80nsbs7h1CSs22c02oIGCYoGY8mHb0hiGmPi9TPdu3-WcPT353-r5LmBdG8i6AkSmgXKmtIM9_6R5pcIg3FL4O1UxRYvd8jgepMqHUDACqHPQcde5xtFXPjmtvqTS527Et2yQN4SOdX_W51K2vrmHkROGujcZ8_YXK1aOGQ32pjafVhI8GFkKLsQHP-Q3z-oyUqmEcGz8XaSSBl-3Kk_r_RIW1y-ylBG_3k2Vigxx-etq-DMpTjHLShkWXvAOkqD2V0_rniO1r7XSe0FJQe_d4ZY-Vm2JdXjfAFszN7a0F10U-ufpbf1p9id_qJYvS1GRh2UzbjEIxTrVRFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pEfshKPhUeOYiXOAoShl4NqZ-y81MO_Y7oUz0tkTOsUHPAoZ7e8bJiwiMnfBtHdgyKjjtMTmKvK5smoh8dQXAGwTnR_vfh8Od_uf4vv567qByA29yYujhMVaB-twQCBcyzmBYnhpNjiqFTIYTFkE3vna1svylgCQqUIWc_D4xxyKVq-PUtYkl3Ds4lTyKgndm4o85c_1TjaTfEBR_3IrLzVetbMdUyvsXRN8B-tN1HmNFCl-BClMGMo2PMJE5u_9jRpxeu8uxyQMZh1IxvSAA1cG-AgNAdCwaQ_SDADBFIHBos0Ejg_SBv7f0klamHqQIwk7iJUI42NMQTkWq7Nh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pEfshKPhUeOYiXOAoShl4NqZ-y81MO_Y7oUz0tkTOsUHPAoZ7e8bJiwiMnfBtHdgyKjjtMTmKvK5smoh8dQXAGwTnR_vfh8Od_uf4vv567qByA29yYujhMVaB-twQCBcyzmBYnhpNjiqFTIYTFkE3vna1svylgCQqUIWc_D4xxyKVq-PUtYkl3Ds4lTyKgndm4o85c_1TjaTfEBR_3IrLzVetbMdUyvsXRN8B-tN1HmNFCl-BClMGMo2PMJE5u_9jRpxeu8uxyQMZh1IxvSAA1cG-AgNAdCwaQ_SDADBFIHBos0Ejg_SBv7f0klamHqQIwk7iJUI42NMQTkWq7Nh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZbeoRQ1rpl74-annyCplLOeMaaQm9FbkOfph933nQ05me9RghIF3WzF-CN-CUrKvrADxZ1eB9cO1BHGVnZwD1bked90K1M-cNh8Seh8WEFnUSWmFfNJoQtIkhF0n18WMRrUPZRsx1fzOs6D9ln6hwI4oRee8X6iBI_H6GbB3BMhE9VkzTg_D4Yt5JxLFq1h9wPjfEgtoWK5JKrMNun6xrCB80i4zHUHXFbV-qRzydL-mIhxL5aCkMJhYQscqIsqEizfqJg8OGvU3nQ0w8iXLgVrEaQAa-gZ_ekBl1Y2Vc2TOA-XD8PV-bXCAb3uBiRXyqG2A-bwblbZLJ-SXJ5v-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZbeoRQ1rpl74-annyCplLOeMaaQm9FbkOfph933nQ05me9RghIF3WzF-CN-CUrKvrADxZ1eB9cO1BHGVnZwD1bked90K1M-cNh8Seh8WEFnUSWmFfNJoQtIkhF0n18WMRrUPZRsx1fzOs6D9ln6hwI4oRee8X6iBI_H6GbB3BMhE9VkzTg_D4Yt5JxLFq1h9wPjfEgtoWK5JKrMNun6xrCB80i4zHUHXFbV-qRzydL-mIhxL5aCkMJhYQscqIsqEizfqJg8OGvU3nQ0w8iXLgVrEaQAa-gZ_ekBl1Y2Vc2TOA-XD8PV-bXCAb3uBiRXyqG2A-bwblbZLJ-SXJ5v-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=S7_4XnPGV7hckGwFtwZIf3CoW7vEtfNYH056Gu4x4KcUmbZdSX2W9zi5k-sRbUh8P1U9DsGx70h1PeTfTfCAcZImyO4gsL-LYWr7povNjo3sN3HEkJePLQkx7W6jmuw1XFCzZKJ9-Q3MZvyh4K2o38rFHDZ5SFy-RZ8G_Z8kIGKvjIggN1t_SfVAg8zm2ERUBhBL6HOpXgKk4qzxOLD9dvxx6WN_tVSKWgAItx6197yjjH4bRG0VuBJQCa8lQ59n_QuMqs-2EeL2pSeKleBIQCQ-ajR0xQ7AyP8pmIBZKy0K96VFKRos8TCcEc93wMUMQeeoxaBHvOlxCiaW8J2wLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=S7_4XnPGV7hckGwFtwZIf3CoW7vEtfNYH056Gu4x4KcUmbZdSX2W9zi5k-sRbUh8P1U9DsGx70h1PeTfTfCAcZImyO4gsL-LYWr7povNjo3sN3HEkJePLQkx7W6jmuw1XFCzZKJ9-Q3MZvyh4K2o38rFHDZ5SFy-RZ8G_Z8kIGKvjIggN1t_SfVAg8zm2ERUBhBL6HOpXgKk4qzxOLD9dvxx6WN_tVSKWgAItx6197yjjH4bRG0VuBJQCa8lQ59n_QuMqs-2EeL2pSeKleBIQCQ-ajR0xQ7AyP8pmIBZKy0K96VFKRos8TCcEc93wMUMQeeoxaBHvOlxCiaW8J2wLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Ec2Uz5HtP61JMu5Ud-_Kqwa6paD84jmozTUhmBQI7yPFscRF7W7DqsNb-9qqTNe7yH3kSyj5R0YAuE1oO7-3f6hmd-5HdFuVAKbspYe8kNSkCf7C0NE-TzAfU6zIQuf5YlLbZCX5bY_W72p63sP3I0cqQdwpEr8cbpPHPEpwGV3Rm3jnIMiIZydMDU8XJ9q66rngF012Px8mbTCuWDHtjzWXa8u29my-eTkthuIWrwjsufZRAwDFiPzx8pxjyv-z9tU7nkSy-BWQI63BabWMOKVWBUAe3Mv-znCo4gGGIgscSuwA5HSkIt16Pv9fh8CNZswMCXILf6041C-lSRXlHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Ec2Uz5HtP61JMu5Ud-_Kqwa6paD84jmozTUhmBQI7yPFscRF7W7DqsNb-9qqTNe7yH3kSyj5R0YAuE1oO7-3f6hmd-5HdFuVAKbspYe8kNSkCf7C0NE-TzAfU6zIQuf5YlLbZCX5bY_W72p63sP3I0cqQdwpEr8cbpPHPEpwGV3Rm3jnIMiIZydMDU8XJ9q66rngF012Px8mbTCuWDHtjzWXa8u29my-eTkthuIWrwjsufZRAwDFiPzx8pxjyv-z9tU7nkSy-BWQI63BabWMOKVWBUAe3Mv-znCo4gGGIgscSuwA5HSkIt16Pv9fh8CNZswMCXILf6041C-lSRXlHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jG7_krJUwxhmHLfRqeYzVhQI5saXpHa2qNRkaosR1uZq0XuPJu9EJeYymsOJK1Zh3jZUNu56vhI4d4g-NbIH4dXosXtGW9pgPSHN2Giiwdsb24xqEnoJ6tLEZwUSwOPXueGSdUjFNPmvrMwFWXNhPochcaSOIu4VX2W0nUbSIUkngcPl12f9vfi2cj2naUiN0TmpmltzRqL4patywI4v190JiqFbEi9-Ef8nVfy4oFnE5h-DPHsA97z3skLLNHsEZxxrzRxTdpReiFrL4um2ItXVsC1j5NaZa91BlTbUIttAMcRpcE_Rr5bvyuRWqvmtMQ878Enk5KSyPB3iACv2uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jG7_krJUwxhmHLfRqeYzVhQI5saXpHa2qNRkaosR1uZq0XuPJu9EJeYymsOJK1Zh3jZUNu56vhI4d4g-NbIH4dXosXtGW9pgPSHN2Giiwdsb24xqEnoJ6tLEZwUSwOPXueGSdUjFNPmvrMwFWXNhPochcaSOIu4VX2W0nUbSIUkngcPl12f9vfi2cj2naUiN0TmpmltzRqL4patywI4v190JiqFbEi9-Ef8nVfy4oFnE5h-DPHsA97z3skLLNHsEZxxrzRxTdpReiFrL4um2ItXVsC1j5NaZa91BlTbUIttAMcRpcE_Rr5bvyuRWqvmtMQ878Enk5KSyPB3iACv2uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Rls82BPG2iPz1dCwmIRyiYua_ylDu3qVL6sJne-13zR0wlu_ET4caH7dDr6rHjkPlz7TtIT7smpvDqVERr_TdVKdZ8LfY5aacndrc0cDaOaES2ieLmhCJPZMYpJNd_n4uaNEAMoN0GPzprr0Z6E01pb3DykWFPKoD-kz5hjTbPbRWDtFucOYSXYjFMCMsfEnCxktXz04Lha8n_Ua71qbAhbQ5lVb00u0L_q46WYsoXLwPoFU6YhIArbL-QqGiOZ-wWVEmGnoEb1K7ZrB8hngKF15GrIvA96ImKue8XPW58mo05uw3kdXVwgAal_apwI8POh4CWK1WXzpCvO-HQLNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Rls82BPG2iPz1dCwmIRyiYua_ylDu3qVL6sJne-13zR0wlu_ET4caH7dDr6rHjkPlz7TtIT7smpvDqVERr_TdVKdZ8LfY5aacndrc0cDaOaES2ieLmhCJPZMYpJNd_n4uaNEAMoN0GPzprr0Z6E01pb3DykWFPKoD-kz5hjTbPbRWDtFucOYSXYjFMCMsfEnCxktXz04Lha8n_Ua71qbAhbQ5lVb00u0L_q46WYsoXLwPoFU6YhIArbL-QqGiOZ-wWVEmGnoEb1K7ZrB8hngKF15GrIvA96ImKue8XPW58mo05uw3kdXVwgAal_apwI8POh4CWK1WXzpCvO-HQLNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaYauJPGdhTKToXoQWKinEyVQ8tLEd90vSeI6HFyNcScWGzyCd427O2JTJZXwWZTW0ysgyOcVqPUKzCzRlMqN2Oyhmsxc0Y_cXX2R9M-M9GszqIiX65wPa2IXQoyV2FutvwYSvjfGXkKR2eyd0SuLclGXBVAvjIvfrduzVEL_Y7NMgqaNFnGWTMsTgTZrgk0_yXeb-jVEjKxwKfQqJ03GZMIMyipjRwbtN8DVvoBoHx4yO0F7beO6Z1GCgeJis4UiMOdhftX1S7NLlErKuSqgoKdOrZLv1e7zFM8q2TOFTUfHdBkMo1UqT4XFQD0wIhYMRNCfPscIW9Sgettdninyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=OCNw1fCrlj6F1QS3i26ETevxZdGhuFMSMVVw6AXrIj7PxU4yKm-cl5p2Ltv1uziKz7Iz8Mnkr7kCucxOkkBodfLX7l3ZHxetX9FF7gwGJvoMTCtJQw2zj0trCIFPSTXfXdaMQZT6fB04_RGAsBONpLlrqMEz1kpNgGylx53pOlhPPSc6iPI--lQ9_FTdNFsBsvfLcOoTmoZQwN8LEktRVRsRZc4pih4MBLtiwyC7Hgx6d-N1rVRJULTfj9QYJGAzweRXG3m1cX78rb3l8mSI3L7pta-GNwjHuPStj4F9qjzeijWxZh-tRnpEJIq-KfmtrpkIbvN2UMS6BX1nalIgJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=OCNw1fCrlj6F1QS3i26ETevxZdGhuFMSMVVw6AXrIj7PxU4yKm-cl5p2Ltv1uziKz7Iz8Mnkr7kCucxOkkBodfLX7l3ZHxetX9FF7gwGJvoMTCtJQw2zj0trCIFPSTXfXdaMQZT6fB04_RGAsBONpLlrqMEz1kpNgGylx53pOlhPPSc6iPI--lQ9_FTdNFsBsvfLcOoTmoZQwN8LEktRVRsRZc4pih4MBLtiwyC7Hgx6d-N1rVRJULTfj9QYJGAzweRXG3m1cX78rb3l8mSI3L7pta-GNwjHuPStj4F9qjzeijWxZh-tRnpEJIq-KfmtrpkIbvN2UMS6BX1nalIgJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ZcaGB4J2P5qvjp_zi-Xryf5fQa5Ch3ML5Q5_27ZLoy0EniKIFBGLrzFu0ErZgAMzkHT5jmKLr3idvwIiei4iT6dbk523z8pqaNXbfIzqNbvu94PO3VhEOOaUC3J2pIf-9VP758gjwf7nOnhKVH2i7aNzGdAvIiQ9OO0sQA-nN3sDJsoQ9T1YQFyohUWMm4GXBvQj6hou2tI5x64rsByRxRKBS-KuzSJSY6Xyw2G00L8mX-x6uy2bz2ZW7lQWIVhJXXB9LpAkaEGAqGsBaSNc0SWvX1VGMTA9X5cVFZmZLOnGlnIuwbdHAJgm2653oxYLmUVju4zZuENaDTwFQfHa2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ZcaGB4J2P5qvjp_zi-Xryf5fQa5Ch3ML5Q5_27ZLoy0EniKIFBGLrzFu0ErZgAMzkHT5jmKLr3idvwIiei4iT6dbk523z8pqaNXbfIzqNbvu94PO3VhEOOaUC3J2pIf-9VP758gjwf7nOnhKVH2i7aNzGdAvIiQ9OO0sQA-nN3sDJsoQ9T1YQFyohUWMm4GXBvQj6hou2tI5x64rsByRxRKBS-KuzSJSY6Xyw2G00L8mX-x6uy2bz2ZW7lQWIVhJXXB9LpAkaEGAqGsBaSNc0SWvX1VGMTA9X5cVFZmZLOnGlnIuwbdHAJgm2653oxYLmUVju4zZuENaDTwFQfHa2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PaKKaIuwfPala-MvmkqTK1rkpTamYZB8oHAPmyfklxM-258wx3WzXqMsCnPYuHtv_oqpNIMwrR_DOLOVtpqxuuqmAObig1xQTx2s0IbLByhm3nFSogDcblcpKXWlgwn6qfwpmQjSFWXehw_3jrHMn1Arl0X25YNBBPOmw0mAfYoXjMPBK7NSQDqtiuKc1OMKMIQG0kGC-I3z1l2QfFcsS7dsAlbE9amdDuiwuQEDTbSaEnqS3tl-f2L9cyEFMMlpsYO-fb8gnlrKd15gXA0NLgbhFhDM_Db4zNvZonaeXKck-lYqvFH-a5ioHPlbuM2kza1objI1A9QsBnn7Zl4Wkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=PaKKaIuwfPala-MvmkqTK1rkpTamYZB8oHAPmyfklxM-258wx3WzXqMsCnPYuHtv_oqpNIMwrR_DOLOVtpqxuuqmAObig1xQTx2s0IbLByhm3nFSogDcblcpKXWlgwn6qfwpmQjSFWXehw_3jrHMn1Arl0X25YNBBPOmw0mAfYoXjMPBK7NSQDqtiuKc1OMKMIQG0kGC-I3z1l2QfFcsS7dsAlbE9amdDuiwuQEDTbSaEnqS3tl-f2L9cyEFMMlpsYO-fb8gnlrKd15gXA0NLgbhFhDM_Db4zNvZonaeXKck-lYqvFH-a5ioHPlbuM2kza1objI1A9QsBnn7Zl4Wkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Rx4MLvkFBEcRTneBo1b_-NcEM57KPsn2rbLnkfPupZGNXbIWBdSiIf4LsQIl52dttwz18YUjhD5pXFp0PBO81kGKiSaSKM0cwH40_swzqX_m26z8lUEugqcfTHf-cbvTjGfZm-sx32rOQ4yLMuFdNx1pFuykXPiwOlFnYoBokx1Ut9JejX70TtRT3-txK6nXoeqjH4QufdE4yHMV5XS-c_SrQwMj82lPL6HwXV-7ERqNVPQf0pbd1Babt_tNpPpErK_aA2TozzsHO88COkIeEjy-X6i_9kBNogLpPUFCguQRU-M4MAxPtCG-zazunGUcBUsKtInEYEyn0oyNyVAsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Rx4MLvkFBEcRTneBo1b_-NcEM57KPsn2rbLnkfPupZGNXbIWBdSiIf4LsQIl52dttwz18YUjhD5pXFp0PBO81kGKiSaSKM0cwH40_swzqX_m26z8lUEugqcfTHf-cbvTjGfZm-sx32rOQ4yLMuFdNx1pFuykXPiwOlFnYoBokx1Ut9JejX70TtRT3-txK6nXoeqjH4QufdE4yHMV5XS-c_SrQwMj82lPL6HwXV-7ERqNVPQf0pbd1Babt_tNpPpErK_aA2TozzsHO88COkIeEjy-X6i_9kBNogLpPUFCguQRU-M4MAxPtCG-zazunGUcBUsKtInEYEyn0oyNyVAsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhLRdJt_SoNEWmdZR0EBKtJXWYO8h_61bL5Ds9OuAb-h4WeqLs2p6uHCyLsS972Ai2tDCxsODqteRW-v2TDbeQst-oBRSFjzrFourMMXx79Kd_0iJuYPJUqpSJ77BR_stWsJK-678g8UnXHHVru8HOagv1ucl4Ic1mJ_JNzvZ4-3CLLU2BnyeohTWENEcHXXL-LpWuT4LwJcDedP_B9Njn0yG5qtJRQ8BVVYOuXJrcP57ZLd5acdO-RDm45SKEq1N1AUWRIDnmRcRVFl074RKrxBiH7aps0BGqqzohw39Bt8OsG8Yu2cMpR7ToTBfHD8tnEFIfRFToq49rr3U-AXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=GlG4ufbvQMDCC_dVS6_tZvuS5jOC6_FEa97Q_-hrNUa5Z8eRFh-dpSvBN1xT5qVlF25wXYNlmG0ElXM9NrIcKrLyafY8Z_6rNz4eAVj05HS9__cUZdWr_dU3mePlX_TxqkuXeBg49F9aizMF73RIsfYX5Llkf0bhvRsOOuEk2adWqLAjLuDvxveH9nklj8ULpWIiD7EDWJADP94v_UNzac4jCc7K1DDRgisN1x_nYnTp5p5JX0XaPrEObgUGNUpf3Jm_PcU6d1yINjY-SARvZLBCcZuXO5_qr3smI2xoCbJ6ApoV2rQOmYz123PK7ifkCXUZv5GCID1dl7imFx2WpDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=GlG4ufbvQMDCC_dVS6_tZvuS5jOC6_FEa97Q_-hrNUa5Z8eRFh-dpSvBN1xT5qVlF25wXYNlmG0ElXM9NrIcKrLyafY8Z_6rNz4eAVj05HS9__cUZdWr_dU3mePlX_TxqkuXeBg49F9aizMF73RIsfYX5Llkf0bhvRsOOuEk2adWqLAjLuDvxveH9nklj8ULpWIiD7EDWJADP94v_UNzac4jCc7K1DDRgisN1x_nYnTp5p5JX0XaPrEObgUGNUpf3Jm_PcU6d1yINjY-SARvZLBCcZuXO5_qr3smI2xoCbJ6ApoV2rQOmYz123PK7ifkCXUZv5GCID1dl7imFx2WpDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ueQvcFNkFGbs2dcmigOec3BeXHiojt9c-qu72FQHcudlaf4TLzujC5-EEWUq94JclKzA79yBkXiRJa6VP7jlfoB9cKEkqlo362kzMBpWRef9TbmSFaeCz51Zhz1ndE7Tly1VW_HHJ-TmCAoQTOBa9jw8nbz2rA36H8Q-35GfnZ717b1CDXPfO3xPrpRBn9tvEoFzgSV2uK-tyz-UXUEzJ20rFwkgMMiI0a20VcmP4plj__I49Rwxp4yTGXDtEUHzhowUzXfCgo6V7gIdlgFu_nTe_46imQt0vBt4cOSc07S6JP5DnF8Kdu_T6JIEmLSgV6a-2fhLXHetpfXAv_rosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ueQvcFNkFGbs2dcmigOec3BeXHiojt9c-qu72FQHcudlaf4TLzujC5-EEWUq94JclKzA79yBkXiRJa6VP7jlfoB9cKEkqlo362kzMBpWRef9TbmSFaeCz51Zhz1ndE7Tly1VW_HHJ-TmCAoQTOBa9jw8nbz2rA36H8Q-35GfnZ717b1CDXPfO3xPrpRBn9tvEoFzgSV2uK-tyz-UXUEzJ20rFwkgMMiI0a20VcmP4plj__I49Rwxp4yTGXDtEUHzhowUzXfCgo6V7gIdlgFu_nTe_46imQt0vBt4cOSc07S6JP5DnF8Kdu_T6JIEmLSgV6a-2fhLXHetpfXAv_rosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONqiN78vxcSDpEUxni599NzRr7RNSXqrFf5lQwFfGgPe49lA9L6IkNNS_sdNw6TpkWcXgjbe2eck4ly46PFDNZlrxlYniBCDsol_vsyYNZwg1hAO-54XhnLxPWFOkrYr04Uoq-r4ohghSS2F-Cw5XzXqAYeZplQmhLUZM5wBxGBKpsP4jKzXMDqfva0lUpeK3jfMzWB-X1o3-buLXqoTNQqKAsiRNAJ_w7Ty7GRW578fsgv5czI6X7YPyhzqphELw9vnYwuILDj--tWeOX04OR-_Im-sRJuU2wh82h22GB6jvILRc6aJrgizBRAuJGgww3CnVAsppXHUUrqdoEn8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ewk7ueEH9EJF8B0Rry86Ij-gfHHwrlhwQ5h6PqxqtJjvujnRBystAzeS2RDJuiq0o6fx6B1yHZ9VADzPEdOzwZnt8Ym0RMT0X82Dp8D_XG19L55a99WTKMNerXuD35Mjw6AO3kE9zlA8bvi2pteYEPpVtr9n2k3Q1DAnJL6BdDBLXN0CrMso6vmXEoUZsC0XXn0cu9AZ1MOgznsfmQe-DSH9bFyURml4UuhGablDZs40p6GE3_neAnsYYMgtb94MV3Zwmqqa9urkEk-GsegsYy095bUktoINx83e-en1MNSsthygTkCZwKcqjh_ViNsApnaFzh8wJgwV3llRSK-8IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=rFhbqnt3uDbHWN10OumABOoU16KJGPk7YRmloaLNUKKd-AC0S-f-CiXNobexVU02Rnt6KiWQ4K-Zm_h8pHxGv4OmL8g8uABDRfhycWNb0Pi3-A1hLMltgZP7vcTZ9rf-7QYj7-DzvvxfbkmDX4YunUo2cGk3x7smeBFjLzAEGLSMKfAWn7BwHLaTfDHhEbjkIajIno38qb_ar-3OGD2T_oHCIplfRw3ZU81vAEtxqhvejz8mS1FOeSCKOyH-jLsSrIMzRp7UGy_hD_Y-0dcusjwqrkT4RcjdgNcpBlbePfth3ACs2hT0Ht2ooIZojeeXy38pFVLzDJYdxhOkwc9wiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=rFhbqnt3uDbHWN10OumABOoU16KJGPk7YRmloaLNUKKd-AC0S-f-CiXNobexVU02Rnt6KiWQ4K-Zm_h8pHxGv4OmL8g8uABDRfhycWNb0Pi3-A1hLMltgZP7vcTZ9rf-7QYj7-DzvvxfbkmDX4YunUo2cGk3x7smeBFjLzAEGLSMKfAWn7BwHLaTfDHhEbjkIajIno38qb_ar-3OGD2T_oHCIplfRw3ZU81vAEtxqhvejz8mS1FOeSCKOyH-jLsSrIMzRp7UGy_hD_Y-0dcusjwqrkT4RcjdgNcpBlbePfth3ACs2hT0Ht2ooIZojeeXy38pFVLzDJYdxhOkwc9wiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIR4VcPQzdIBl08N7KYrKzEqi2Y7l3JCncNyb3QXFfSn-ArbOudSiKn6wjQE-RcPIN9mWwSwEKcgDdXylWw6yt2XELRFETaEiTPSWR1HUgIpxHzKTcLhs0we7yoccelKFHCQlWFQP7uBdOS863L81wyls8FJaQAayLk5sNECV1zQX-I73z0qroPiSvZrtaQMmbLceed6uRVTFUbbUzgOROq9lMSX9lpM99zpWNPYa3wtkZJAqztH5TSzxOAYynMFes7numgecpSLMzb2Etohp4BoNx3r9KcHU5NexG-2O1Zh8AcumKZ9_oYNXs7orgYEj4wpGbSZpG9YJ0PN1-AjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmW6t5O_MIm7rOMGy3bnlJ9DMBq6tOicrFlKgguHa5vSTS0AhL4RCHtpNVLqUa5XpnQn0hHj4Ueflzu809DzGDNs27LEkCnfHgZev9H9Qpoggra4aC43BS9sUDNsVvExt5D7JzAQQ21BiTe5gZJvjirT-yQxnobAXvag-XAJWGZf4TbsOXUM_m4aZXusDJrN2zcD0b4rgRXsfccshpGttUFfGKJb0PjOdszzgIyZDvehgX0hAgKV2jgfOXGzjK6m_hQf2pWZw2MrZDcuTo3FUyOr67UbqF1PU2mrWYdhe9_9atkKrmHT3reT_BKeSCayF5zpRzanpTPb8BPzhY9OJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJjl7ZGKzM-TqYV2ZEME92UchFCW8gBavVVFL0B_blqHnnC9QjWQOiCGS3JwL2rbNAYZtPE2AIONNLLM1DMvQHaDA34akwQrR84gs2wFwzkONKZi43xMqm2t1yZCcphP8alDAcMwUhMOBZmsP3n3PZBLLVFCWHljHXJrHaRaepNNsMqe2KcXNLAjmlQybdPdYs05Ux6xun0XWivisBtpervLkHLa4xZnPE4pkMR28wnokmwqUUNwnQ-6_VOya84mxnlY1pDFq75Q4Dxlw5ms3vyisVJ0fG6Sbac9Xfc9lFSOU-0GiSJvuksvB1NgAirslhMXkLm5RxuvlgteRJhMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=i9iVXSjaYrfZXZMYSFl8Iwmvg1g2G0qGbPXz8yJYsWw26GzNovqdkoubKSdPMmlAqSt4pOT4Q9uKb-_0YQagX6wyoqZ_y5gCMKH1RSHnB0GX6FV8Nvr-8t_G9WbVuoh1I3cboxymkFKR97meVVDVKg5RJPRnWBwFiXILMBMUNTTi1vT0gwsbnJgn87j4zTmWRs5ET2bUhw7SYP6dGV3kOBbZyCk1mmZzEhzxsadDYFjUmw39SgK2dF3zCSPa9WwQPpGHRUTNocJWFHLy-xmjOZgDQa-NI0_hq09p0jbFuMYe-YaJIhw4vWVh3kKU6uPiSQwNPQSjYWPLwmDgkMA6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=i9iVXSjaYrfZXZMYSFl8Iwmvg1g2G0qGbPXz8yJYsWw26GzNovqdkoubKSdPMmlAqSt4pOT4Q9uKb-_0YQagX6wyoqZ_y5gCMKH1RSHnB0GX6FV8Nvr-8t_G9WbVuoh1I3cboxymkFKR97meVVDVKg5RJPRnWBwFiXILMBMUNTTi1vT0gwsbnJgn87j4zTmWRs5ET2bUhw7SYP6dGV3kOBbZyCk1mmZzEhzxsadDYFjUmw39SgK2dF3zCSPa9WwQPpGHRUTNocJWFHLy-xmjOZgDQa-NI0_hq09p0jbFuMYe-YaJIhw4vWVh3kKU6uPiSQwNPQSjYWPLwmDgkMA6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=GyJ2SuQhDHVvmqP7SI8lTmM7zcyFSSeleDwofxi1S8bJE82ODmru2u0juMdKhaRy_2_Pp6lBgSpFdL93tRJhKdV_I2RbesE6LbN0w0oj6b0V-9n7TnTPpmmQyYg5arVorBiel1IC5dKbJusnOqUilRkFBFBCab_gAPIMHrEkWUbAFFQ02Km6X_miBq5Q8ZzNBAAUeCO0UvT6UNu38BPIWm8r5OeHguyXMBOP7ci1hVDb9w7kmaRNtaBpXxebMIMKtV860HZTuglRLuujrrQR06wLLBWMeyCZXNXiMp7_XXA07yQRvgWycYARxDljR-5_SwdMGqQBXNYyR5gtK7TNoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=GyJ2SuQhDHVvmqP7SI8lTmM7zcyFSSeleDwofxi1S8bJE82ODmru2u0juMdKhaRy_2_Pp6lBgSpFdL93tRJhKdV_I2RbesE6LbN0w0oj6b0V-9n7TnTPpmmQyYg5arVorBiel1IC5dKbJusnOqUilRkFBFBCab_gAPIMHrEkWUbAFFQ02Km6X_miBq5Q8ZzNBAAUeCO0UvT6UNu38BPIWm8r5OeHguyXMBOP7ci1hVDb9w7kmaRNtaBpXxebMIMKtV860HZTuglRLuujrrQR06wLLBWMeyCZXNXiMp7_XXA07yQRvgWycYARxDljR-5_SwdMGqQBXNYyR5gtK7TNoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fWd89e6KMSv2hL_ptxVh-zKrYnzwQX7Hpf5u5gozLGzBsdxZW3QhGjV565PZ47M30NX7MHJYWjTKlRdt6zIRuv8ulTjJjD2gLCCrK5bnPuzY42rTROg6eGQO9sHV5nqAxZ7jduIXQfgRiK_KYRPRInWEIUrGXgsPA6TTlP9qZ3Lb1VPVq9tMLa_xBLRJUWgB0X1hBIMmClIrKgqLk7lL5BWgvRf2RrC8l3eySdSA9zRYWGo4j2HRkFijSCjVeIfWsiZ2eJ-00_Ynfqa7eG68zakqqAwF0C0-cNdmFTKdSqigNLovOOq2zbxpawqaWlu7p7NRXCY1OcAJEiHGNlNvMQZbS7Wwl2TxzwuLMd3h-opCcilzrbtblmT78t20mhOfY0VENQyeLN_W99y6tgQx7U7WefBNOcTGbWrc8Lf0hrT6apk2pty268z6_L1sf387hnvTk5PpZhF_lqQNNHwDb08VIWX4pKuKKsDWsrFJneWwb2Fnvb1jPmbQSL6HD5JTo0dXn7td64RZBL2Vz4tK3RJdCljsakxpK2jKiZ3uxkt0qajU3QtV5AJ0XJK6gVYYb8EzFufNv6U69bxyYNGU1goFr-zvddOnCv19gH_HMgMYQJPXzTLgCIDzmHPKzqcGaYIrlUWuiXeRVBKz6pvOTPhgm2HmG021lro7JMdsGD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fWd89e6KMSv2hL_ptxVh-zKrYnzwQX7Hpf5u5gozLGzBsdxZW3QhGjV565PZ47M30NX7MHJYWjTKlRdt6zIRuv8ulTjJjD2gLCCrK5bnPuzY42rTROg6eGQO9sHV5nqAxZ7jduIXQfgRiK_KYRPRInWEIUrGXgsPA6TTlP9qZ3Lb1VPVq9tMLa_xBLRJUWgB0X1hBIMmClIrKgqLk7lL5BWgvRf2RrC8l3eySdSA9zRYWGo4j2HRkFijSCjVeIfWsiZ2eJ-00_Ynfqa7eG68zakqqAwF0C0-cNdmFTKdSqigNLovOOq2zbxpawqaWlu7p7NRXCY1OcAJEiHGNlNvMQZbS7Wwl2TxzwuLMd3h-opCcilzrbtblmT78t20mhOfY0VENQyeLN_W99y6tgQx7U7WefBNOcTGbWrc8Lf0hrT6apk2pty268z6_L1sf387hnvTk5PpZhF_lqQNNHwDb08VIWX4pKuKKsDWsrFJneWwb2Fnvb1jPmbQSL6HD5JTo0dXn7td64RZBL2Vz4tK3RJdCljsakxpK2jKiZ3uxkt0qajU3QtV5AJ0XJK6gVYYb8EzFufNv6U69bxyYNGU1goFr-zvddOnCv19gH_HMgMYQJPXzTLgCIDzmHPKzqcGaYIrlUWuiXeRVBKz6pvOTPhgm2HmG021lro7JMdsGD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=v4e28I4l2AgZMEaX_nfI_4RLyFFGkoODwFbR7xVwAGcVHynSWSb3MCZPHhR-TQkax6i_fjhEEQIcNvEy3dDqppYOIw2r-qCJKND9IdaKlymwP22Ho62SQkmlRWJXz1CKMd4s-eiWm2Vi5jd5NWWzLlmtljtImJ4d3I0F-TsKyYTq9EoGgVMnnAAd70A4hR99Y6n2Eedfb2kn2Qi6SdSdVX4-OGN0fSaAoPNhCFz3kDTvI-EffLMJmw3y0WJUVqeawNpHKt5_MooCfn3f6zoOahGGlAxPdFLTo_MZGtFJ3zgNpXh7fcJdBx3CWbqnvgqmkMxpR3ENARQvWt94G4_J6KtcXfZ-HNlJK2PvT6rSYrI473JWrA56vnktQMuvesdX1hMO48fUSdTuK0nFXJlAwWYQwg2cE48kofRHthMYH6zmN0o4pxknr5xswsZ7ZFj3VlQ3BRbjdM2yBwstmJGdBOuHHA8Kof6VyQsrpYDz4h2uHllYHPLPV9AM2gkT4HMxLs041-popWkgaedXQ7qznzvJ6wc-T__BcOZ48dF3SZFo8gg5U74AInJk_xh1jJ2N3-I-1Eghk3tPU_rtjVFPhAkuNZoDz4m22BrUWNs_gfSd1EytuZx31zyy-nWSj8VgygixK-U4vO6Fv-C09DXHHdsCXLxawDETo0osqIjiKdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=v4e28I4l2AgZMEaX_nfI_4RLyFFGkoODwFbR7xVwAGcVHynSWSb3MCZPHhR-TQkax6i_fjhEEQIcNvEy3dDqppYOIw2r-qCJKND9IdaKlymwP22Ho62SQkmlRWJXz1CKMd4s-eiWm2Vi5jd5NWWzLlmtljtImJ4d3I0F-TsKyYTq9EoGgVMnnAAd70A4hR99Y6n2Eedfb2kn2Qi6SdSdVX4-OGN0fSaAoPNhCFz3kDTvI-EffLMJmw3y0WJUVqeawNpHKt5_MooCfn3f6zoOahGGlAxPdFLTo_MZGtFJ3zgNpXh7fcJdBx3CWbqnvgqmkMxpR3ENARQvWt94G4_J6KtcXfZ-HNlJK2PvT6rSYrI473JWrA56vnktQMuvesdX1hMO48fUSdTuK0nFXJlAwWYQwg2cE48kofRHthMYH6zmN0o4pxknr5xswsZ7ZFj3VlQ3BRbjdM2yBwstmJGdBOuHHA8Kof6VyQsrpYDz4h2uHllYHPLPV9AM2gkT4HMxLs041-popWkgaedXQ7qznzvJ6wc-T__BcOZ48dF3SZFo8gg5U74AInJk_xh1jJ2N3-I-1Eghk3tPU_rtjVFPhAkuNZoDz4m22BrUWNs_gfSd1EytuZx31zyy-nWSj8VgygixK-U4vO6Fv-C09DXHHdsCXLxawDETo0osqIjiKdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=SgU-x5lYrTkQMwG8pEx0ZYi_WQzCx4s0YIdQUxPYeKe6odgLy5B_Glp59_XFfBKAHuXx2f3h721zhJ-LJtpVVQ7_N25Siy4WrOIp9euLNC77cocfTqYhvlQFUTFbrXhXlhPejQUsN0ZgW2hfkIXDLEnA2SKWaDBTjtQ16J-_1OWXWFqrZMKQCHbDAwzk7EM28xxgX53kzzZsPpmNzTakBgnsjhFPRrmuFmw8URh08DR1POmpbTp8M5_KE6qhJ7zbx2glTWwwt8TOkKbiifehHCqgVTK-jGhtyWcugE3oLcghKSLAEkJUDluN0zEAaAXCdCfCvmiEAaHo8jZegp-mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=SgU-x5lYrTkQMwG8pEx0ZYi_WQzCx4s0YIdQUxPYeKe6odgLy5B_Glp59_XFfBKAHuXx2f3h721zhJ-LJtpVVQ7_N25Siy4WrOIp9euLNC77cocfTqYhvlQFUTFbrXhXlhPejQUsN0ZgW2hfkIXDLEnA2SKWaDBTjtQ16J-_1OWXWFqrZMKQCHbDAwzk7EM28xxgX53kzzZsPpmNzTakBgnsjhFPRrmuFmw8URh08DR1POmpbTp8M5_KE6qhJ7zbx2glTWwwt8TOkKbiifehHCqgVTK-jGhtyWcugE3oLcghKSLAEkJUDluN0zEAaAXCdCfCvmiEAaHo8jZegp-mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd9cmicdNNJzRn5EWHxxkW29SsvT1LjyLFmUPptZjrdU5QCsdOdfnBM1CJ-XD3uCbBObzsdGS6eZBTpf-cDh2Qt5EmRgiSAoJ2OxuDNFCbXUrVBgI-Hd24fUuoU4vdLkXMzrP5bnySFGKvPjQTWWMQbtk0t4WwVNAWAHoN70dKljHDtNVCqjirbcQi0dkc9GC66pezxqDqvBcO7Bf8IYoeJspTd6B9NJhLTmzpA8tyV74PUwTSDXtcsQK8jM8bEJWVZRaTIQApLajXzt7lSRmhLlLDZZ6aN3Z7IbYgsgkR5GTpzLCsBJxzRd_ybyyGd1wg8BAjzfhHHTwwJe2nNyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=in5zVv8RiOc_qSDMKurisUyrFov76VH5npf4Dp8kda7J_pqXsYExRqXBuaeSyY4N0JbmSPFE1Eg1IrGhoBDp25p5WW3ZTNg-FbRi1miJsgMHFE_6P0h5nJZk2NLJHvjI8aPGIhpwtQ7Uqt4QzVBLb6f43qaZTk1NaEeXH4jOg-mzxU7OQkehvivas67Plz7CPJ4Ff_8TQVtrKhRF2FOZ7tbqq10L5ThrJ4IRMMuI_VchVzDBCBKZVOzIPn65vjgXg9riQix89QwpU56LMKlf0S2ZhK5S7uM-Jjj_iNfuHdlV2H7MHEzrja_-pi6VJdNFq9V9WrdPILXMOLPamSE4gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=in5zVv8RiOc_qSDMKurisUyrFov76VH5npf4Dp8kda7J_pqXsYExRqXBuaeSyY4N0JbmSPFE1Eg1IrGhoBDp25p5WW3ZTNg-FbRi1miJsgMHFE_6P0h5nJZk2NLJHvjI8aPGIhpwtQ7Uqt4QzVBLb6f43qaZTk1NaEeXH4jOg-mzxU7OQkehvivas67Plz7CPJ4Ff_8TQVtrKhRF2FOZ7tbqq10L5ThrJ4IRMMuI_VchVzDBCBKZVOzIPn65vjgXg9riQix89QwpU56LMKlf0S2ZhK5S7uM-Jjj_iNfuHdlV2H7MHEzrja_-pi6VJdNFq9V9WrdPILXMOLPamSE4gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=CoXOenUBGnFU2oTMaaBD0K9hx00H5J8YILu-xupx2P53l10EgkmpXPO6s-vE3OQJJg2Miai9MIBpvqzVaJmvDFPzpErAFPJu8vI38i3PveQ6JsWR7e9wIVsPbc8YAvPRZhkdPr5AHhcGE2VLXIQC_m-RJFWS570jV3YuB7IcMVAoW_XZYGKvot3_yLmb0jsI85VuuGmXfCSehdNAW0Huh6oeSwqn8n9_5Tfs1-WzrYcYM7BTAQtqWnJZVhYfy3fMNAHUe070gW4p1Z6-La7yLNaU4-MYSKS7_2VoZXSlNBPu1pgQLzyVdsjHddW-V-bMc10Vftw0v-YI_PBVAeZ9aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=CoXOenUBGnFU2oTMaaBD0K9hx00H5J8YILu-xupx2P53l10EgkmpXPO6s-vE3OQJJg2Miai9MIBpvqzVaJmvDFPzpErAFPJu8vI38i3PveQ6JsWR7e9wIVsPbc8YAvPRZhkdPr5AHhcGE2VLXIQC_m-RJFWS570jV3YuB7IcMVAoW_XZYGKvot3_yLmb0jsI85VuuGmXfCSehdNAW0Huh6oeSwqn8n9_5Tfs1-WzrYcYM7BTAQtqWnJZVhYfy3fMNAHUe070gW4p1Z6-La7yLNaU4-MYSKS7_2VoZXSlNBPu1pgQLzyVdsjHddW-V-bMc10Vftw0v-YI_PBVAeZ9aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNRnafrJ8qL8tBrK1yDLPHWxsIZtTchrqd4DAIlUa54psFkyCaWK9x61ooHH0oBqkcXYrxvFxg3Blf2GM_kLQxehCi1fhXt8rmj-qXeFyudPWQ3IJNK51MTSeDp4L3VedmiVkSDAdPQqZ9YSGkAstoxqoB3goQnbHJJyb8PSnHurSDTDEwkAFqZ5dZt45MarWw96V6Ok_wU9dUKWMODV_kmqJT_q-mrJNdHDLbrpJvW4cDwzW-YSJY6Hf64Wa_rnJfDWEZOywwUCyGHCTCawsoM1ZWHk5jXVFcmvcOY8_N2rfy5I9KbJ1opRptn6bq0474ZM3hyHTov04iXkV1jjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUeCvYrfY5HzK6QAK4Bu_BmJdFIyetKvSmZ936g0SAE8OqhzYkCfY3x5qKAgM7kMztbrkdSDIAwL-E36zv0WoqPNgxx0b2emsbhzeGmPk_It00rzunaxdOhaqQO8Ng02o-VtejQyPwuSyb5jQa3pmhL5RuPGmhuvfCcgumNILWfbH09T_m8WdbBon4FtEYcZXme47ShgmTRKjKmNasPcIxaKkE4vEzJCj4p1kthvuYhqxlVEdIsQ7qGnpxbqFznClhuzHSCIdJuGFxVRyhGG-VTpUOlfSM2e7t0o6Ubqs8iyl59HRgH8vUTPUkaqG3RyBCAf5Jt0pUHrA05Oj8r4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqH3NR5-fQ-buRXgDuPqVs_aqJF5-nZ8i9rZFUSPhJehfl5amu2RkUCS4AVmYenU2CU4tT0XJZFuVw8hd1-mCKs0G0lES0SNyyXmAXnef_3rYz0pqg8iHH2GQBZTYZeyhe-LNm_otKVTNn7Alk-yDfl3sD5AMy_M0KFGbgoeVnvbbBEqy2EdMOZRnU34SIXqlyzR_ytyJ15D0fLjGSyYduYEp8bwJIvsii6PqPaczDYVJCTCk6MG-pjnQErnHWi9zAZ_lbSOLEu2hptGEzy0oRohNApMTlkUahK_bySWV03zArVJN7We7XvTu0P9hjWCCG-u8PLEWYlZM1REFFDnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RniGAvLtZbJCsXSUnGv7ETb3ZcvN7QwtnvO5GkCnoMes_5A7Rqnh0stVI5Ny45-jbl9PpQxWHHhvreJ6d6dpGavh0ok1o3CIBTyEtgedNuZtHY-Avzn3j7dwKBc4YFqjGXK0FnZhK2CzXUEHru7fjTEQOTWB0MbCUTP6_GEDlFlkhFSle7XoozWSTrpcgG6T76xysEDfJr94MgVOlEiYYfsiBRae8K8f6tvT6LHdk601MIi2X7IqqnCtKym9xlXHGSLBKa31uDyMDx4c2FKSVZrvg6F7zd2Aukyfr1mTjzfcoB9JSN9PJdApVnsLKsGbYDRvqfIMOlqwQ9eUy0UXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb0kJCc9MMCUhI97BcRJ8v6FGvXo90-Yd5aVIwGJibnaCau2NvJUwdS_24AJZ78cQavp374J4DSp7T4dM0QbNlTHRibDoGV8IAsbTGj2p3__yg9LvzJ52U2Ecb3c9toYht1SuHdB7QRnZl8YpNDOd9yEijqz7XA4UN_F4H3mjq_btKh2X0BcajTWamcxkBTLDVew4TwmprXIlKE0X1rwE23PSBqRRE2zG9mi-22dzNNdm-9MB32pPA0qLVds_X68UFUua5TFW9fji04KA9qk_7wtamiN4mxlQuG0nVTCoLsMsImNDIYG27eFOMAx7I5rCTwer1qdRVSFtYS-jlXDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2PkeAL36u08dyenm-ztZo2_yA5o0HgUWEBosnzgAFfKMrsvzxfcf93xgUsxZUMpwFH1WSdOZymul5AdDIHbQ3eY7g_Wq1pa0W-z1EGK229gIjqcpQ6BtMp8SDTS2A1iLUxRAKa5UdVqCM99uVxOVfkGMRCNp6PAh6nKZotzSAf63QdTegRdvleX0I_9VR3hb4APSU-0pwZlwt1eUsGUsTHdxA6skTRAZ3LKk7XQdH-tHJDNwy_G46MOkgM0DtsXKmyNVnINpDqIX1WvZ1MSyMmp754o8lx9Ijvm8cQpgxNeCZg8m-3nEDdylCCXrVY9_kzO2msg6KLh0xk_T6lwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBzN17TGqjuNBc7gWMiI4JVlii76h7zf3Ul2sfA5_SjQyAV_iGCq_XNxeCyYhbStExPFIUOkNe821dc2-Dgrx00RdXfmXz2Z6vrYoITJ9064NL2aGx2J8E9UQVQBeqpyA1BJx856zUxdrJA-uNaoQHHcPQBfg4DUI6sbQWR4lr0-CuFWUeGJCobYYUUt5gUIPkfHqhgAfpkJANRTknzJR8eYXo25DZRa3Uh7YRk6Rk7uO9tlaQmomX10v7ok8nvzr-RE1WqmzrUBvTCx0u9Eu3O9d8InUcw9EERt3iqNSnmVTiX-5T9993K4u5q0VMKNB53TTROsKzyg4oThZb4aIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg7X6bFx2d3SLKrjozZ7NoLTk0n7r4-NfuFjV2opyliQr3c8x2yzi7gMnj60EtI8bvchxiHkQXsjaLiUFaaHLh3XbFZrqoA5f_CmUwXS7L6beybWmzupUwpF1veGoZG_d_Dt5w4JAntgQJ9ngaw7VV4tnNI0w1bwS5P27oGcMzFEAJc2d5sdYidWobeGt0iSlWC1u4hqy1RwZleDVyD4JY7540rS4DM2QFEP1FNjPpkjWqVzaI_mWVNIaWfFB3aWXr_BED3RS4XCyrziNS941YYmMlbdvVszmWztyHvmTiaQITnIKpSaelLB5mOu0YxPkp_wxJhAQvqki_Zw03f5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsjbiYgjOrV_mnfZnfItgAcY8ZYhR_5fKzG7vxOxtaEDFJNKrLP188SxSVr4n5NSIcZbidnN9h5etDEKKyR1RleLo8bSgZxwzaxEed8LDfdC5zNhpcV2aonJOSvcg3m9B0rC9sOY6Qw1kLm34_hzfa2auSFXuHam5OOnJh8hx2kRk5-fFwUZbQz4rkEc0nIlwe752CeESYIzcALDGkMAwGCWBYHGEiMUVSNro3PUPzZB4BEAuW6OvnFg4226nPd4Wqyhrj1rK-GIcp_2Yeye0uXjvzb3Z9DbcORWKiwEc4gHhRdS-S3igO-Ek2I_IDIgvlfZjplQm2Y9QFzVh6egPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvRbCptMehb7WE-fEscwp9W9ie8wSUSdLNNGXCVN-hnQovpSqYLjyKks_J__1ZSR1vLF0JzrPwHdQqayErrg7HwKE1bSj9SRkhyqyv51Uby4QekStc9iyETxxX5oE64QR5cagRI9V2CO6usUfgGJMNb3QxeqOA6lLIvk5BmVujCACwHxgb-N-03Oz69QxekrZCD2hxkjibv2JggA6s7xKdmqvybpk4hxi8huTsvDhtrphQnmry19pp9PvFhCVR3HLoKux8g9sqbWZal_B2ezXS_ZtE_pdtbO7OYWD5KxW2JZi6VXbkJGXrdkK1ihaXKpuIZfyCIoezFOQuVUMNWavw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o04yTEce7a_wZBcKDwe3mE4u4oIAD_wLn0f1qYo9AeT1MsOhDov7CpcXGoT3B8-e4JESka5tNAj2VvXykbaZEKWSEpJHvSen78wMjh_P_9J3fKKZ8n8sbEyjT4301lu54nMcEvA1WB9kwr39CeZ47EnZrqW9ygKLB0tLcr2HzUB4Xb0Z_9rhw2sHWC8st2wo3Hive0ydlcXqOjsxbC2WsSde03yXl2bx7BPXmVB9HeDz0ZBFYqlrzdFAgTYocB5hJj2_FvHUw84uyJkSUbiDJ1QvDDSMx2l6bfji_Wq9ccoxoZ-fLGSz6F0rDuvI2bcPp2Zw-Z6AXsVTLrb1ATxBLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o04yTEce7a_wZBcKDwe3mE4u4oIAD_wLn0f1qYo9AeT1MsOhDov7CpcXGoT3B8-e4JESka5tNAj2VvXykbaZEKWSEpJHvSen78wMjh_P_9J3fKKZ8n8sbEyjT4301lu54nMcEvA1WB9kwr39CeZ47EnZrqW9ygKLB0tLcr2HzUB4Xb0Z_9rhw2sHWC8st2wo3Hive0ydlcXqOjsxbC2WsSde03yXl2bx7BPXmVB9HeDz0ZBFYqlrzdFAgTYocB5hJj2_FvHUw84uyJkSUbiDJ1QvDDSMx2l6bfji_Wq9ccoxoZ-fLGSz6F0rDuvI2bcPp2Zw-Z6AXsVTLrb1ATxBLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-vjCiZIxpoPOcyd8-SP18Go5biIzO_MOs9jcWaUIATMiTX6RzcX7HLiKRVeT9-2KFmsfTrlcIMHFIR4tXVFwlwcp4gFkbooEBocZzEQCZX8JYHkQ59jNXtNKpFXsgmJzquIN6EwPSA51i0cF-7KtwRfqFoRD-SX-HopbTuypVy85alSx9MzYEeBG5Znd_fTafVwr4g36PybxluleUy220E9hkJa38xUcYVt5FFEh_I_b64trB7jEkkh8QeDejyTDm_SuiEmx5SsbrVDqeyxC_CVqMGZdNZaFMrjsaTLpGLuKJ8YBJSpFtrguCSz4HgdnKLP6vDc17yiS5w77kkB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9bFmk3BHJnQgAMTwN4Ndg9YJzhzWY4IM0UfHyYi8CPYvdgGGyPYcqaeGs6AE2HwJqGiqU6sq8c2-HkEiVITPtjH6CYtZYpFyZYvF42xOf-HPwSJKoTDHKVpnVBLmoGZ9zl2n2Dfae7kaKtGtQ77D9CSR1YbLLW8tlYqcnlfCdKi_DVp6kmnDeCLRHboa1TKg7tOX2zz_YhsHHfDyi6lDEGktsE-r8lv7GRE3oX3tkEdQtnhw8UkCZ1wFmYFN085gP_y4P1h2gov361YGHBXE52sRbgdHLtd5P5j9cJx974KRy4bzyw7NXbJ0TuMx4QbW0J0d1_KX2EqsyXF4QzP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=mxREoi9yaoTIFGtuJ24X0FN7Z6AAeMhE5KCDUUxgGMo9oN7yeO8vB5Ap3yEiCK6terIATFBZDrpbo59WtoT4TVMCssU_koWqs3cs2xojUfgioA5cnKKK90PEFxT7n5iMY1lysmxVfiExuJhAXlg1ox4orPXIjEX_mGahyiQKAN7hKawofLdznG8xPnalZLV_B6jmV_QLw0gFqcXfvNrGtythtwvKkuxOKj_lIM7i9RJelckFJ1vT3_BrRDgxfygyXarxypfgIXlbRBJIp799UDnqvW2A546wYBI01xLEZY9_BxFrUqVK5XRvKxwPCrnBTugU4uOhJXqzM8rMvVcuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=mxREoi9yaoTIFGtuJ24X0FN7Z6AAeMhE5KCDUUxgGMo9oN7yeO8vB5Ap3yEiCK6terIATFBZDrpbo59WtoT4TVMCssU_koWqs3cs2xojUfgioA5cnKKK90PEFxT7n5iMY1lysmxVfiExuJhAXlg1ox4orPXIjEX_mGahyiQKAN7hKawofLdznG8xPnalZLV_B6jmV_QLw0gFqcXfvNrGtythtwvKkuxOKj_lIM7i9RJelckFJ1vT3_BrRDgxfygyXarxypfgIXlbRBJIp799UDnqvW2A546wYBI01xLEZY9_BxFrUqVK5XRvKxwPCrnBTugU4uOhJXqzM8rMvVcuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=SlBFSDnbSPa8pyE1wGGbHmznCEiLRbv58LDiI5Q-95NMue8Xh7ghZe9aKHeS8LFypp-qN4toyyYPECq1I3tvP2hRhHtNfwBGGsGoyuXs2TTGO4H9YlqZ9n9oTeImnNGKDqfWuVWh5R2aIIRKVZKVr3fYOG58vIvMbnTHNW5B9tDiZ_QV_IYr8tDuuXjnCHlIfiiJXNHHC5k0E5C1PC1oPNbZSXGD6YiLv4QbWJQKejMSqjt0QbWd2e_yv_CiUvsy37Zxu_ONZWle-FUxj4hSOUUXIRqVjAlgOLkdSknPVgQesxO4BJerEm5XwvILGhvr6HtI9pocdndDUnfQvNXDwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=SlBFSDnbSPa8pyE1wGGbHmznCEiLRbv58LDiI5Q-95NMue8Xh7ghZe9aKHeS8LFypp-qN4toyyYPECq1I3tvP2hRhHtNfwBGGsGoyuXs2TTGO4H9YlqZ9n9oTeImnNGKDqfWuVWh5R2aIIRKVZKVr3fYOG58vIvMbnTHNW5B9tDiZ_QV_IYr8tDuuXjnCHlIfiiJXNHHC5k0E5C1PC1oPNbZSXGD6YiLv4QbWJQKejMSqjt0QbWd2e_yv_CiUvsy37Zxu_ONZWle-FUxj4hSOUUXIRqVjAlgOLkdSknPVgQesxO4BJerEm5XwvILGhvr6HtI9pocdndDUnfQvNXDwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYaqualo4DFmKuKISABUUTguo1viva69cy-aH4Ow-NKlf_t3837XGLZXDJz6g3YHomFtxSdat2nCxjn5zm-NpHkTbDrMGcxfFkblpKFoYeHsDptBWfzGPhanU0l_O3fKEsIl3nlOlYWtW2rRZWyce3MxkR6qIc6chZd2DOx30jtWn9rvyRKY_eJAodYP_cCiZaKJh3XHDNsa1zC7HepPSwkqRkX-JaxBuwAWAYr8WB0yypu5M9DKQvOhrPM0AVRRGabbwYYU1a147rJkvEPIycMtZLD8QtwpRgqZt5Q6itDC-hsQe0dSeX6lGm83VpghOvfqNRSGJqJBIOJrYxZR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhiIawTGR6rAOLU8HloMoq4isbFwFGjQU-UOPMLWtbTCyPZlmneepPR4hoNnKSz_tysNvq4q_Q4EeMCTNxkAH3zMazcXPxPjExYojR7YPhFpdAjD9J5guRtUtJuc3Ini6dRdYlq3mzCPQiZNvt0avQRhFmcKsGikkYOemAZU1op8XZXfGz75Jzj_K4PIdSB_1X9GWutZGt2PhbEtE3fNnDtgXRQ-dlYfuAAKzWZTkMI6eBGodaTLjDNb_eCtjhoo-wBr4tBQIq7XWaPB4Z4Cc0KcMrTEVeWaRCzxB1NCYCxtqJSFmrkahJQbFc8My1Ak0ZSxqPkEeUfyMvVpWZCOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyYKtimCd0DIip7DNTpIAkXNLkiOO6L2Jh8t9Z8E2dMCnAdUGVBEq1rjyOmLgOTodqxo9VRDcgCns7bUZK__iv1j7xkYYAPqPpovVy2tVbqMGzw_8gPcnBvFkYzPp3BBsIOXEoeQhANpTEG7FnOaGu2An2812XrzLpQCeM8sb158iaEhSnAZSCiv5BuLBJoXVaH4RpFsdGLhcsx5OvWAOE0MkaV-x7l4ALaBLzJTFKLYCoq4Bb7vv73vnSGWs1ZX1DSWoWJ1ZqFbUdcRF7V3QsY9YM7ByK8FPonKWkTr6Wo7hCjBBxN7kgMOIelEI_WKpcprpvkbESiA5tAbCckCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlxwqPvYxTwbcCgogXoacNbJ6jLmGCoJWnbJmCuJqfeQ8U2OYwOlgMKIAI87qzLHyhmk5aaMjki8xMDIAUBYBDoHscRvQLNdgTXhAj7Ilja59jmaokpEPKxZi5SW7-rXleqnFxdO6_GOs3jQXWSQaufDlOaAMTc0mI8cz3xGcC_YgzQXxEWLhvnVuwwtFCNydxsaaoxFyYQNF0cz_kV8LXA1eeiK8ZRhuH2kS4z02vOmV-fLnaGYl5z1A3Fg6tPg3ygc7AmE-ujzslSMkt2LPGQeIoSJhkmwKjArwZn_fGnoPGPFoyUZGyMaL8EcykOKT9mEPkAOIQVK1XTrSdhUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLXSxyfpYIe4GOeisn68uXBGn97cIBz7X6E6fVVAEmN08PDA9ZAvI3ycrqKvl56_Uye0Rasfm0rbkQoViNl4_-q6LXF_Mh01FNnKtYptmhsrH8kMYaRehzbzDQxjY1i38SUc_Pwo_MtZjc93aYFd0XiN0GI9LBunmevLjmqLbTbBG0_9G4EmC4A9La8FxFdSKlQzvHXWsu2CCDrJpKURuk3z0hzD2mH1jI1nttUOdc0Rw7DW0rRQMmJ-wnx8BYtflbSXu4-N2pH3-izwCIvKnFr5ccIQXrlApCt5R2G2oqf1nxuWpABhYPumvUJjNJ812SPgjo3-z5IesRpmxttkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AepKK15WtOWw6r7I8NsKINZgB3qasTABgLtfyF_OEY6afFR4VPxxAikT_c7FNr7pvAmbRfBpPy93BaJus9JLvGEwEgqOqwF_7CISG_xH3WbGokweSNfDqTpVXHWh0aY3QBVyQqnZV7bUmk4ivF9JlOlfmYkNbaFV6GFIkB5C_W42PxCj_rGWIRZExf3mEvEiNH2PthUYQKyVK_21WVGvDKMjKnnDDBsv-pAc9Nii8n9oDE5o04r61LdJmGcQdClqCe25uXY18lphPzza7p2c-joW-Fb5HpcGBhZ-EtaXWb9EhTjd44eTRb6tVyUsBx3AGYnjdepG-9zs03nVJucMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5k9xBNq2m2AbZlBY_bX18sOty2mbi_tabQ1qGmIO0cW8Mf0Forpg6xNNQZ3W6PCOdJyNZrHJYkYLEk0urzkwZYitFAL-Y-Js-ukLMyDUkgAc9ExfyCz-53dK64JK3upahPJ73b-DkBlEXE3I7IuPmy3chiEU30O5VX_lpeYI6rOvXAazcgZd263oOLUIUl14Q6EslO3rXV6nlift6I0TMuCwFRuufEccxtavXaRN5XJh-IDlyKsZ1xn1FIjEzVqzaZknp1JpeXUy-kZfoS8ftlAAs245E8dv3vh5cP1669Rcr57hUNyUP-G4fzE0f6VmKXiJy-63zv2H4xT2r6c5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSWL1vIubR-aVYwx7-QYoS7BeE1DGXO0wogL3_UBHhRziCLGWxSvLkPuwv9Lz04aqTqOmSzgQ3E14EgzGs9VfhjguakOqTjHK6DNzLl5Kt8Ua5nVObzECKdJLEOy7jqXcxKk8MG9qoOiT4BQ2eauvV6kkxP5q4DtB4XDvF8GmVtnvUZCP1atKRN_dMWb61Zn-BnvoJ1vfBtrdFcL9iy6APZeYWr9D9aIxlxZvT16HrEIw7YFNmumVlK2RZn4a2lt8_N456WCUleXHeg8qrXQQfsYMZ9eIA3YTCVBSO96by-Qm5it9Xh617qvha8BI7Hl764jpEHdtcZnhx3fLrySJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=fpp9xiD0hVB2CbDRYfANsCwkUJXEnpiqikGAQQnQEvajjpEBj-NHnLQRhlyjEUpy_3CZ-ov6ZZes6WeEzV7eii5tsqPVzKfpArj9x06lwo2eACAj_Y4jZdyfw14JvLa2GLxQwtc4eE2jjx7XH4LDXFQklQmqJIbcbb1KZ-2LkLzB9eNvoGHL-hRTtuL32cSl2kx6nyOIFJtkB7ZjtnFBGvTAHEqoaZh9haL_k0xMxI7cTReQeH2cM9TOOdJAGdONnNsEFw3LmgTX3-Ke3wn14F8Z6iQvJtmj_0gQk8QudjAkHuwRq_8qke1MzcWWGK6q3HMvp5vvABKwFgAmtSUfKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=fpp9xiD0hVB2CbDRYfANsCwkUJXEnpiqikGAQQnQEvajjpEBj-NHnLQRhlyjEUpy_3CZ-ov6ZZes6WeEzV7eii5tsqPVzKfpArj9x06lwo2eACAj_Y4jZdyfw14JvLa2GLxQwtc4eE2jjx7XH4LDXFQklQmqJIbcbb1KZ-2LkLzB9eNvoGHL-hRTtuL32cSl2kx6nyOIFJtkB7ZjtnFBGvTAHEqoaZh9haL_k0xMxI7cTReQeH2cM9TOOdJAGdONnNsEFw3LmgTX3-Ke3wn14F8Z6iQvJtmj_0gQk8QudjAkHuwRq_8qke1MzcWWGK6q3HMvp5vvABKwFgAmtSUfKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTS7Hpi9wksyYldVipBd5WNPBvmP7siACXsnKOrm0R9uWPCNyyAw_kDWvxREoiSivMiq7OzNylfydPE7Nt6hGUluvUkxYGGLn-oDDIgtTIK8N-2fNPNWody_JUuC0Ch1bCRpxaL9Kyw58Zv8LEvwJ68kQ-pB2J-_Cv6BreX-OmxEpuOM0_rKJ_QgxskaG2uh--XLI8Mqfb_94o2jxHs3bOiOeTCqGb9AftO4dA46kB9RjAfLs8HH4fjPInTK_f-KTpLevgovzY3Kh0q46yb9KlM2kQhBLaREaVEpwBxoqnjFMhBbJJa-ses8sZygFKRBbwLZFtOOBxA2Exqb4QO99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=PTvDzXchbLVbPdzvftocZNnS3Gx_5efCIu_AuvYcqT65p0zhu6FmTmXm0n2n3z55slMgPlvRKulABOho-t2ZVJ9qFFlb3utudBQFEynv-p91urF6FcKdCmfxkCKOhfNsjibCVwk2lwPZTzuN0iRshcxWUASXqlpVkZWVPWoSLvkm9ZtD7afngcj_PBv7EbEfOEhfV5FQ3PeD-RvDrtog1ge-SteE-VGdAiQCbQ9vFb3sAYyq0FTMM91r0vcNKQXr7hk-E8XApuRc1yZkHQcJNd0fUMwtzpD1tQ6HeuzL8Bhy2xDzFS0ncau7xiC2-ScmUvPhyW3ky2hgKSwiKLFsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=PTvDzXchbLVbPdzvftocZNnS3Gx_5efCIu_AuvYcqT65p0zhu6FmTmXm0n2n3z55slMgPlvRKulABOho-t2ZVJ9qFFlb3utudBQFEynv-p91urF6FcKdCmfxkCKOhfNsjibCVwk2lwPZTzuN0iRshcxWUASXqlpVkZWVPWoSLvkm9ZtD7afngcj_PBv7EbEfOEhfV5FQ3PeD-RvDrtog1ge-SteE-VGdAiQCbQ9vFb3sAYyq0FTMM91r0vcNKQXr7hk-E8XApuRc1yZkHQcJNd0fUMwtzpD1tQ6HeuzL8Bhy2xDzFS0ncau7xiC2-ScmUvPhyW3ky2hgKSwiKLFsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=NMR9cfjDZCR9mnqyw08jl94S3YUscgEqaDLPwgLOgmJ0vIuf_veJp3KqU-K5yFJzcEEaCErIbruxL3ORfsqf7kEtTpbvLoJGUI_Z8CFIZKwseEOVaXPF5437rBBzY052ph-lnovpZJCN-cc8tY8NnpjYqbccX5uyAHUXaq2XU154EwVjeRCkZiblnghS4rkLrDYMxZkDg9f6wAwc5Pl6GbCu9hEtFSAD2p84ml2abwx4dlXGXl3jQvB30ny3qMeD8nb1y8X7Jcmb9agEQzxqEdc9lnGbBFV77ikodU-8NF3lHGTGcWFVqI6kKdbRH6XcRlRIQd6I1xc1oZ73EnME-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=NMR9cfjDZCR9mnqyw08jl94S3YUscgEqaDLPwgLOgmJ0vIuf_veJp3KqU-K5yFJzcEEaCErIbruxL3ORfsqf7kEtTpbvLoJGUI_Z8CFIZKwseEOVaXPF5437rBBzY052ph-lnovpZJCN-cc8tY8NnpjYqbccX5uyAHUXaq2XU154EwVjeRCkZiblnghS4rkLrDYMxZkDg9f6wAwc5Pl6GbCu9hEtFSAD2p84ml2abwx4dlXGXl3jQvB30ny3qMeD8nb1y8X7Jcmb9agEQzxqEdc9lnGbBFV77ikodU-8NF3lHGTGcWFVqI6kKdbRH6XcRlRIQd6I1xc1oZ73EnME-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxhJiMRZRDqvIZPeOHTtY7o4fwowNHioKvdgbDFGLQPw9eWDIn5IW9RtCIrZFsN4Nn9346tlTbWBcTKV-1DdrxB9XQmp3HDeUeu78IQN3_FRPH-gNFS_r2onkSYu6FvNpvjJl5W2LdtuizILdUJB74uPKdrABVFMwni2EodZC7ToW4am5VYL84t9Q1I2R_4VvIIhl5wUi3_CHE7SkDB5RI959JfeRXPHOsQbwedY2AXUcNFH-HyY5ELc8HeO7LG4flgm-2IewaakLT23537nAJohx3cNn--6AUUYAv5Pg9wNBoTTy8GfmFQ5iecv5J5lSmT7YYOhsH6q8yKEFbbs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut3AjVnHvWG_0EpMXsUBf4wSGjd2j2wWwoZVj8hzSyo49ckD1IUQZFYWYt8mzgzS4_aaSghgz9Q0PZ6vPLFY3zKlHUTkxp6L66zSACeZsBrMiQmfx4-KPwya19YLo3TQnlel4g4WzDMtHbBOezZxCdHcFKPGhelSdxQIh4YbvFZ8lixvTX22hBS9UxkwLF1F6YVduNMOVdrB8K_A85QCpQ2w6XHX49FK_kd2mBEHpzff8m_oEq6jBh-CCLGN7odc2vPrMpdq1xVj_EG8Sh8M_7259QEaIeWhPart3EqmWGHSwZBzYDATChMupAV018jtCthBsajJrN_uhL7V8A3wPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=DepqObLMAC6sMoTqsxTcsPVLziE2M6Awzso2vaCqqkj_SfCk2Ju9X7Mp-0tNaV0o6sRgqDyQAV14Oaxk7nnkGbUaGWHm7Y3l75oq7KUP9YOnkrmmNfUU1uFE2PcObPW1lpOpf4GCuB0nAiW0Dg35TLBo8dyo6o0LTCpjzFDq3KyZc6BqrMQT4AuInEHlZMm8qT2eCL-rpB1iNF8BZLFzxey5M5YDsCfo3nie-Ajkss_7iDJVy51_XGCowuAk_Eg92yMtcAAdsk_k_L2aNI281u_8doFyqUVJb1ifx8_dk4D79HCqVhgwduvEqgnMbQyLJtvcrc6_JSO4VukplpmZakvJLYIrRvTgsl9N_bfDgltNHqPCUXhHrHqCjfMfqTOjqzRCNXKEZ4--cHzW1c0ygvSaFDVbNHitYaW5Op30MYdnGM2Oie5qOWyZuw0Aw7ejCIZJKTCWbY6q4SZtIzhpG23icDONFiftlbJijFZgC-My3jwP_naGmbuG6r4dUnZ1pWPJ9KLT9SxoYqJQbnWv3UkA20EsyTdxLvkOQfrykqNXDidZq5cHxgTC1QXJi92fNcAbs6YrUcbdq7hdY9xeX3HzcfqHdrI2NwPJqFW4RZM1x0IM2bNO0wJ_qjkoQSrw6xayOnFs2f8DEelj3D28eB9YIXWfO0fXRZsmRKYGw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=DepqObLMAC6sMoTqsxTcsPVLziE2M6Awzso2vaCqqkj_SfCk2Ju9X7Mp-0tNaV0o6sRgqDyQAV14Oaxk7nnkGbUaGWHm7Y3l75oq7KUP9YOnkrmmNfUU1uFE2PcObPW1lpOpf4GCuB0nAiW0Dg35TLBo8dyo6o0LTCpjzFDq3KyZc6BqrMQT4AuInEHlZMm8qT2eCL-rpB1iNF8BZLFzxey5M5YDsCfo3nie-Ajkss_7iDJVy51_XGCowuAk_Eg92yMtcAAdsk_k_L2aNI281u_8doFyqUVJb1ifx8_dk4D79HCqVhgwduvEqgnMbQyLJtvcrc6_JSO4VukplpmZakvJLYIrRvTgsl9N_bfDgltNHqPCUXhHrHqCjfMfqTOjqzRCNXKEZ4--cHzW1c0ygvSaFDVbNHitYaW5Op30MYdnGM2Oie5qOWyZuw0Aw7ejCIZJKTCWbY6q4SZtIzhpG23icDONFiftlbJijFZgC-My3jwP_naGmbuG6r4dUnZ1pWPJ9KLT9SxoYqJQbnWv3UkA20EsyTdxLvkOQfrykqNXDidZq5cHxgTC1QXJi92fNcAbs6YrUcbdq7hdY9xeX3HzcfqHdrI2NwPJqFW4RZM1x0IM2bNO0wJ_qjkoQSrw6xayOnFs2f8DEelj3D28eB9YIXWfO0fXRZsmRKYGw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbilp559Imai-Q3eewa6RGQr_wLcrJdk7v3kJ1M8U9sSAmFPVEYTUaeuPpZSQyEaMV5SCohhTjsL1TyDL-7v9DvCheP5BxPUornF-IVDq-gQq7ETKCizRcKxCGoeorWqzBnlRZE17NvWu0VmmoziCYPb-whsUR2XhZkrRwmru6cLvJeGcE5iJNnyE4jxV4NU4PEyxCwNWYy4l6y1Y8lbL9X2zH8rcmUdt3J2rP3kuZAqJtszlI_vt1Osb3wPvLn20BlhgLZV-wu_1PxsRuIMhvndUseLLAt035pQXsH-nhT2Rl-ASFWo5QnzsVntVcTD12nC4lk-e3EzSBCdGyUScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=W0rhOuctanIEk_9sfnOHV-K1ywUO18tZn1L9TgfcVuPStXRqHzm3_KEltNfzLpu_liVkDcmB2WkV7bXAXzDWQ_zp0QSvqkioQZK569-KIIUa43JGciIU8wOn1imkvWfPdRLc6fwnBCgtQof0BGcdKj232r4Mf2qRAg639qCH408MDT7SPdbJmFbWUPjMON7N9WjLMYiCH9-Lyk8WG759uO9kGFnZm69zgxk0N3e_TdCJfsIwfWceuY_kIKPkq6-M2fNEcBApVc1MVwRxt25uZiHDXxtbD_6Sr8RIvhgkht20MhEtiGvgwn9flE3Zh7TcyGUUuECEGgy0yu3KyRAf1G3UFg4zX8pufGAGuGQB82JPjosTUkPb9-_na5liU7h6njLRZXe6FEL_JxnvVrabQ1VEK2fnbLU8MsK6dMv6vfUf8iCHKGksvW7KPcPAaCKLuXNK1DhXyFEh7cHErPdKHlzSCIfpxc_ymIx3fzhpZaHaee26V-7dl3ESJ9HyV2o-YGfNSRamsSxeDPM4qaI2SeKHYcrvFDJRgn7tSxzHrjCVnkBvyC-aFo5mcyOkynohAcz74ZZN5l3YiCKfsoMgXngulQ-Lv48r3GTT_5j-Ne3RsYdmFIs29joOfd69dTvdGMnT7JuISF_qYrSDjzsLUDvAvjudAtiUgZFNr3WrAzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=W0rhOuctanIEk_9sfnOHV-K1ywUO18tZn1L9TgfcVuPStXRqHzm3_KEltNfzLpu_liVkDcmB2WkV7bXAXzDWQ_zp0QSvqkioQZK569-KIIUa43JGciIU8wOn1imkvWfPdRLc6fwnBCgtQof0BGcdKj232r4Mf2qRAg639qCH408MDT7SPdbJmFbWUPjMON7N9WjLMYiCH9-Lyk8WG759uO9kGFnZm69zgxk0N3e_TdCJfsIwfWceuY_kIKPkq6-M2fNEcBApVc1MVwRxt25uZiHDXxtbD_6Sr8RIvhgkht20MhEtiGvgwn9flE3Zh7TcyGUUuECEGgy0yu3KyRAf1G3UFg4zX8pufGAGuGQB82JPjosTUkPb9-_na5liU7h6njLRZXe6FEL_JxnvVrabQ1VEK2fnbLU8MsK6dMv6vfUf8iCHKGksvW7KPcPAaCKLuXNK1DhXyFEh7cHErPdKHlzSCIfpxc_ymIx3fzhpZaHaee26V-7dl3ESJ9HyV2o-YGfNSRamsSxeDPM4qaI2SeKHYcrvFDJRgn7tSxzHrjCVnkBvyC-aFo5mcyOkynohAcz74ZZN5l3YiCKfsoMgXngulQ-Lv48r3GTT_5j-Ne3RsYdmFIs29joOfd69dTvdGMnT7JuISF_qYrSDjzsLUDvAvjudAtiUgZFNr3WrAzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_pixS_QBNs0cYJWUR3DMMW7-9Rfj6g09KGrRPHqFkNj94rlvnt3xWuwKh0203-8aitIJ0ZiXozlrHGYWh545ih4MhmcGXOi67bwQGjFu8p-7n7hIjwZdLYKw8F57mGnufixkfg-I14zfgce_Vio5FyagLKupDiaL3InyX8aQV397_Tp_YToFPq8pARqyybxHzXCI3tPrcL7eCPnEYsvKXSzCf45cw7PxZxsuviRt8oS3IQowZ5i79QHsnMclH3YkRV2C0EDlErixAdIiCeJuSg7LgxHT5M8THjvmC0dMD_I6iatM_TgRh6hi1-T_yQkwDe3ySolrtHsmRtdKcOdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVozI1BhPPrg_XTu8XaVI_HHANIySUf5XbNpydr36k9ijFXby61Y9gr3hDdfHykU3-Ln37rYpJ_cPg5vxTd9RgChCKs8c9Pw0Ez0ieZ3rdFTvp2fjIU0wxiUI4Gq1atPDc5jQCwRHd3ugoa_3VpIhQkY8cjgw_SuTBw0sjew7jfq5-6Yee-dBsJx4uFFfYrVyzfqNFqWJph6XZ554Dez4ZTophMbgDxwhlhPWKnrRuUNRsLSSGAcxtDUU-cYZa0k43I7Eine6ItnkbrVhjZn0XOQjMo1KaS-hc2tQqlGRb0m-Kq9SuwEcX0hEnr0mIQJ8i5m0_MFvlVVXSxyXP3h_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDTpLp_a3lrMonhNLVpmC84MX_QfevJQzJU5oo4XfYp4X2DlNmiJ414FFLTQVJZDu--lVdA3nyzFuYTzjNg4tnhgS6KxKX5lPCylXRBDW5qFVNM-jPPBiPSiO33dJO7PiGQfeD_Rk1GSrMu_tUj8Z3AAAWjV43rcIo6YgXxzI3X_FizCsgvjleo56zc3nXhwMjjt7213nl8SFkrWsUILD5w05XfJWvjqHDvyaONXnGeEspwbUnav20bCWAkEYIBPSgeoro4X27zBpBIKg-zv3GYSepqOOetd8ZQaNY2ayl4RII-HawdT64iwehB7gnaDnYpI8lPXGds4Ew3XsP1JuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcLD8LmTM4aZtMurDJxv8jSmQn2plxi1V6GgSvklDCw87mRMHN4HRH7IqLNrTunjnB3H-J1xUPAlzqSUYJ7j8rtA2IZdL5HaNfyyvJo_Vyspzj7zqyrXn8UPBM6IrqVKSoNgEPXSEQzFaHa7g7caoYWMZJDCWnMsb9XBAECMoZE5s2j5TWUj8fE_umhgwXhgpBr2xalu4SzoqHkfpP0i-lLUWjLGtdi749pvcTLVmbQedeko-BoKBeaWZxouththouRiqkbQLuAi_OHWGdbBusw2wGwvVfCXNOhn26cwjCyh9sAdYGsNTBIOdhZf6nTz1EIfi13LpvmZwKS9jpj0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG21XAV4qHxw89_J3g6WKB2nBFtCbPHOHwC1RAtY_N2F2kPRyQZVdWNa2Oem4FDjsl1-_U6t89GI_MdBW3QBWVfXTKZXaLysdcGSCQtqU7Kcs4BVBw5MW1Pt3t4Xh4f-JGmgTey3IU0Ll9AEb0T4pw7xF2VObnLf5QeQM3Gq_LoQ1WHPVj3MsPxJFsqkKhFe2Az0MbUEZae1dinWFnFLupNIj85W0s5giXSZYFdiCT5CBwPTy329XZULQwEipsoL2_dqh0gO0gtGLBRAjW2bALV2MzHt1iwR6J4D7R_lcBX6s_ZNFSc9lHD4p7O5wLiNCVJ3YBkT2tpANoxyIfeCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
