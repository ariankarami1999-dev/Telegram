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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qia-P_vF1XX_UfyE5sf1mODjf0HuKmM_aLxspRgx-ZtoJAHhZX26lcNYHdK33b1dglUCTjD-hVFxG6vX22Ix9P1fDCiM7v3UVZ44tNIDGjF3Zl53zVMHAo_Cdff3zJUwCf9dlosAhjwicAJX_RtdrkarJsnNNNziYW86XJPmeVNOvUH2oMMIHR9r-67PiAYWEnN-cRfRWQwlbSoEuP5oWGVWnWWPUnsgsbg_pAF3KE7GSDFo12fkzXZBJ0LSKojYvUdi9sQaaZPnDQn2RSsrBukAAwZEfO0l0cZDTKuhP-S_caxClY3bBd1Acpk2bN3qXIjb6Gi86hOrW8DOaiqgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=m9HLUH0ABJXPj0JoAqJ-DVmLdKSA0pOlrPArhJilwrFG5lnY7cB7BwXo3mVT_jWFBuTKiXdzgTw7Gl8QJI9_uBcmAgIJS5h1KFqO-YCpI7ZHKmvrwbog9P3Qsm3C70aTufSoHH-MquFJzDH6fDJT8cll_aROGqGQmS64lCzpp7OtguH3UEEJ5f2SfR67PRJwBSVQaHS1WmD221bTS_eG9aNuYnF_fHE1HkzWB7H0-HNS0zdVVZgvqa_2CS_9DOE_NRW3_v_8flD26AI8_Oq78UIzSX1oi9E-Xz0Jmu8E4uiRyfqJsr4rJJOxU3nSD_uuoF_O-4aLAD8IsE2z1zn2uzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=m9HLUH0ABJXPj0JoAqJ-DVmLdKSA0pOlrPArhJilwrFG5lnY7cB7BwXo3mVT_jWFBuTKiXdzgTw7Gl8QJI9_uBcmAgIJS5h1KFqO-YCpI7ZHKmvrwbog9P3Qsm3C70aTufSoHH-MquFJzDH6fDJT8cll_aROGqGQmS64lCzpp7OtguH3UEEJ5f2SfR67PRJwBSVQaHS1WmD221bTS_eG9aNuYnF_fHE1HkzWB7H0-HNS0zdVVZgvqa_2CS_9DOE_NRW3_v_8flD26AI8_Oq78UIzSX1oi9E-Xz0Jmu8E4uiRyfqJsr4rJJOxU3nSD_uuoF_O-4aLAD8IsE2z1zn2uzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=enL_gHQ6n_ZK8T9pMyLZguohtfb5Qon9NL1Gvm08Sog_m5WFttJTSirra7QkuKWJLXgWfgx8xv1JM6BKR9NUZyPK8lsTWzR77RFtBoOt2gOmxse-uVzBrgiwZ2L7yLAJHLtOaWPzgoTck9zgLcFuU5s3hHCPP2zaLtGWTdP7hAg9-xn63tVPVEGSBLZ7HmYiS1G7G-JfC2VBuV-GV1STRDUS-TGOYsciyIus5BBbD3oH3CXRyQSC1qclbnlde8ECW6sauCDa9n47nsFMi2lpoKQTEFlD4aO7ndBJvOk9kI47zMoMLKdiPE-DKgVouvBhyy4fLJ6klzDNhtVIoOcfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=enL_gHQ6n_ZK8T9pMyLZguohtfb5Qon9NL1Gvm08Sog_m5WFttJTSirra7QkuKWJLXgWfgx8xv1JM6BKR9NUZyPK8lsTWzR77RFtBoOt2gOmxse-uVzBrgiwZ2L7yLAJHLtOaWPzgoTck9zgLcFuU5s3hHCPP2zaLtGWTdP7hAg9-xn63tVPVEGSBLZ7HmYiS1G7G-JfC2VBuV-GV1STRDUS-TGOYsciyIus5BBbD3oH3CXRyQSC1qclbnlde8ECW6sauCDa9n47nsFMi2lpoKQTEFlD4aO7ndBJvOk9kI47zMoMLKdiPE-DKgVouvBhyy4fLJ6klzDNhtVIoOcfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKJTbht-WtchVvHiuBmFFwCyCzGOdfS2kv1cTkMOZcoBWX5qgdKx6zBLOxFq3bpD7WC6l_JKFPVts3ldgT0oI4qM2AKqicM9igoJ_O9b4yaP3qaCw9P19u3LPgEq_wH-Wjt_hOuSHlwTd30TwS7CZYM2TaDLQJFVlVGJw4EWFMJ_3ONCyZosm8Nmi4h7r6ZspH859H_wRWAQujPrDfNaGQiJynuQE61PybYLvooYr3MQrc3v1yt0C2QWFtot-vt-TcDi3VUbnV1TS_hed0v3msTmqdm1xOMzg5p_W_FKYTvkoRH9f7asZnCttBij4-0r3STlztWBF8TflrJqIuPNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFpBcTLP3dFSGPYv8b86oLUqghvIxt9hIgSKoHftockDaPUGE9uQrFtvhd6Z4o7TrxwW6QXnawr5FVjX0a_52kHvYBt33VEZnTt0ttjLeCBW8wsm-H8qZBn8EB1CA8SlriYCeH19rsGXfRd7Nv8fXjDuAiEVHpo1PMOidZShjEukgMaRpCdZJkSzhymMtnVlmV531E1p_obic9rAAd2I-8UYm3ELnfflKN1kjLKOeLwrfVGypWSvictq6iCH7mZQNjwxLkBEix3-U-k8d0r9_Vhb4DiI5FjW7OACMCfS-0vCUHZppaGRqdKL4x8VlPoU1pmtMQzjLCE9pzmz8Nw3Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=YjgcAk45nkNYEss480SojQ0wuktHx9zfpWoAteEjDaCe6lGB8dI8hfHwY7tQPOVWfK993TzmmYJ1jwFWCMFHeLyBN9080yi8fJN8_PltYyRaRv-fuYkS4eGScDjinCGTRoeCwJy4421WvVA1gotjPIZDgl53MuHuJ1tcsXB18Ruuy3ujSbVMbhVGye-4xfuKoclqsFi9bo8GNZVsusd3bjqy0AvSVRHvWaEUQKuZTDdHNv72MXedCK6KYyfAi5UAjv0rBzd_5UJURKFl4nq_o3mNWT4nwf-zFaJaJ40IqR40Q742NqjRBTv5kBkcikIBVidBJA1ALSh2v1uE5lIz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=YjgcAk45nkNYEss480SojQ0wuktHx9zfpWoAteEjDaCe6lGB8dI8hfHwY7tQPOVWfK993TzmmYJ1jwFWCMFHeLyBN9080yi8fJN8_PltYyRaRv-fuYkS4eGScDjinCGTRoeCwJy4421WvVA1gotjPIZDgl53MuHuJ1tcsXB18Ruuy3ujSbVMbhVGye-4xfuKoclqsFi9bo8GNZVsusd3bjqy0AvSVRHvWaEUQKuZTDdHNv72MXedCK6KYyfAi5UAjv0rBzd_5UJURKFl4nq_o3mNWT4nwf-zFaJaJ40IqR40Q742NqjRBTv5kBkcikIBVidBJA1ALSh2v1uE5lIz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVLB87VCi-FA3xVtXjjXe5vsNl_8Vp8W7vV-_up71x8Em9cW3X0QfSoNLiNRhfxrC3RXUDHC5uQ4KMAAe09QPuRqBjWCjNCWx8yYfVVyyNcDojzksUr3BrrkLiSXGkqy8WxMp-TnBiLAxLl9uDs80ILtg6cJTECySFvPnZEQQ0A0hbRlaPHlowJ-Y_0ukijXVD8xfwuqPRNNTR8gRuTgLXugk-edEoZXPJHsYJHipVxF61OdMn-iRjNCJgBTW2q-ApkSKhoUWuov-T6UFw4V-qZKEDMN67nD8A9BGAFg1Iz38OjPvpCZFxZSxHt9-Zlij6WwriXYuEUejQaUGWVIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iveMpBeicbHIHzjwEt8kRKDQyQV6MEwA-37vCq86duuy18_aWISGRB9N7e_taEYb7Sm_TSrlW6Q_4So0mfkQeZtVCgsY8kVmCxhdOQfy119L0p-aY5qp6YkpERFNoErsymUvmt5gGBFBngxBJ7cnIiOC1-qhUM6NmXk0y7_xwecDU45jksCBBv5xm1w8rfqWohcNmVWN-mYhhrDju4Pq62kHKKIkHTjAYh_z3AvqnKJCyzFzALaDFa_7NKK1rc7rW-JibF5pars0WOEP6E-UFAUZIIVFeZzoet2E6BOSmRFlZiClO0AdeGav35_jf4oZ7w6hDLrxY6ueENMx4SaM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY8s98gd8R3e5u13rLiRkzE-ZK9nCuXMzjLiXp62uI5ykPklRjpnJoLoUVKQ4NWD6eM0qr5oHDhthn0Qn2uXGFQwl2KSo6b-Jb-Y3-enN0__0_RGD5ilJU3YmfsWGNmBR9ef-frpldjakuN-2pdIp_nQ_ymBW-XTqHsAzUwb0CrBd7OlTWnLBdVtykUbrd4ZZAfTxhU2CvfpPg4evlcRCIyCdD_2lCdcVLP1TPTMMurDfoQeRauV_ENbSKPV-oq_GU3fKPiFXLjW2i9ich_EaL3ji3pyWvS89mZimBeM5Tu6f6aVot6QuAJwhEBDSdw2I5U0FALEePzYCev-lvITuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=hVfQPlPU5fQY-qHUdJK3lo3MewVhTvgdIE24AUlGy2yNUzYuz_v5uX-jQ_uoNYzEHnE5GaKUebTz_OwBjJkWPI9Y6ZZ84St6SgfWTcCbrSeRqb3pMNLH7eomQT-JAY7pcSav24f4z9aXcgKIaePXueUiLKLYdFnjOMmi2XTH09LD8L-Yo1_kpPkppgj5IJapt5_bjL4IKdNSE0BBiJ_fV21AeSbDcQ1tJKSPrQ3JuaJBwkVHf23an_VPTRsoFkkwEvZy3vW1JxQTlrle-kl4aCFP5_DzY0_IkuHgcUDnm6u7duAL8qSwMVzoUUeLEZFVOafuzNj6Pnm39rSTAdb7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=hVfQPlPU5fQY-qHUdJK3lo3MewVhTvgdIE24AUlGy2yNUzYuz_v5uX-jQ_uoNYzEHnE5GaKUebTz_OwBjJkWPI9Y6ZZ84St6SgfWTcCbrSeRqb3pMNLH7eomQT-JAY7pcSav24f4z9aXcgKIaePXueUiLKLYdFnjOMmi2XTH09LD8L-Yo1_kpPkppgj5IJapt5_bjL4IKdNSE0BBiJ_fV21AeSbDcQ1tJKSPrQ3JuaJBwkVHf23an_VPTRsoFkkwEvZy3vW1JxQTlrle-kl4aCFP5_DzY0_IkuHgcUDnm6u7duAL8qSwMVzoUUeLEZFVOafuzNj6Pnm39rSTAdb7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=DQlnDgeI6TtHxVXOTHlhCg2WEFctl-7fiB9x1guo9b9upPBCgV5CbRyWwatl88PdDJ4J6t629uxmisFJy8QOfHCYyWS4CgK1h01CFXBNMqChQ5gdPbZvYn9_DgCA9rBEECGCsqzNVmcdJv0AduPwPixdROdx1mOQ2XtwGxgLm2aNL-7f6xHONLdyJwhP1HUuNtHzwBMHAAl6B26oLxMB5yX70h-rB-l3m6E7MNTuVNUne-e27_TGnwWGREg82E7FUge7Jdyg0h7Jn-4eM2aORSeWm2EoK1_uqxhhrEzD_koZ-WRS1CGoEWn9S4mFlsRoKrsZNZ8FDc1okUWfPHYynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=DQlnDgeI6TtHxVXOTHlhCg2WEFctl-7fiB9x1guo9b9upPBCgV5CbRyWwatl88PdDJ4J6t629uxmisFJy8QOfHCYyWS4CgK1h01CFXBNMqChQ5gdPbZvYn9_DgCA9rBEECGCsqzNVmcdJv0AduPwPixdROdx1mOQ2XtwGxgLm2aNL-7f6xHONLdyJwhP1HUuNtHzwBMHAAl6B26oLxMB5yX70h-rB-l3m6E7MNTuVNUne-e27_TGnwWGREg82E7FUge7Jdyg0h7Jn-4eM2aORSeWm2EoK1_uqxhhrEzD_koZ-WRS1CGoEWn9S4mFlsRoKrsZNZ8FDc1okUWfPHYynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fTvnLKkUWgimQZ9dnalulpC_KfZDH4RKlCkuFXrFDiJQJIFz35_Pt35OHXfjOPSHQVRyU6DYSi1da-EOpAomQ3RmCpoNLXYRX7gfouJ7gvFlQU5j4wD4Al_rKaNHil4FPKQJFJU4NVQTS4bxAgM77zFf_JNHi4TTEM2wpYzdZ3FrqwWaPEYOfkYKce_uu3Is9JmC1cKkT5qnh6M1g13Pr7HwdbA9_QvfYP4CpV1pbPG6cqSgFgnDcSGwVewGYecA0zV7fRrW9IVN576CSTFlMwMIaYIgo7VjernCEcHc7t5i0j4W-pS-l207Tjv1OBkJ98pWzqfo2qRtd4njAuR-LpSve4u8ZoacWpqwdN7bkJi2RRuNIji23SIBiG9XgT-dfLfH1Ea8JrtoiYOJ3o88s0Cwz9C_HdecWcp6SClDP3hik5CljtEzhkeGJGLx6uAmaYx0zr9SwIb-cfzDOyXAE9d4URAIR3HY_r5uhA5yYpkqUBW6uYQDkDAspZ323KzJopBlTVhnXJx2LZGAiSE8y50dKGPzV1ofjBDEax1uDZUZat-BA7suUaAoM-ypk5OE4fA9f3_BwflakHx8r_shKM6xQqckUGUaCQ5qMRT7tJtiB6elLm8BhU8mb5UJ0fwxSUc2Ch7uUu3JKiN7mKQySGNGYqRS3Mo962KYegladQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=fTvnLKkUWgimQZ9dnalulpC_KfZDH4RKlCkuFXrFDiJQJIFz35_Pt35OHXfjOPSHQVRyU6DYSi1da-EOpAomQ3RmCpoNLXYRX7gfouJ7gvFlQU5j4wD4Al_rKaNHil4FPKQJFJU4NVQTS4bxAgM77zFf_JNHi4TTEM2wpYzdZ3FrqwWaPEYOfkYKce_uu3Is9JmC1cKkT5qnh6M1g13Pr7HwdbA9_QvfYP4CpV1pbPG6cqSgFgnDcSGwVewGYecA0zV7fRrW9IVN576CSTFlMwMIaYIgo7VjernCEcHc7t5i0j4W-pS-l207Tjv1OBkJ98pWzqfo2qRtd4njAuR-LpSve4u8ZoacWpqwdN7bkJi2RRuNIji23SIBiG9XgT-dfLfH1Ea8JrtoiYOJ3o88s0Cwz9C_HdecWcp6SClDP3hik5CljtEzhkeGJGLx6uAmaYx0zr9SwIb-cfzDOyXAE9d4URAIR3HY_r5uhA5yYpkqUBW6uYQDkDAspZ323KzJopBlTVhnXJx2LZGAiSE8y50dKGPzV1ofjBDEax1uDZUZat-BA7suUaAoM-ypk5OE4fA9f3_BwflakHx8r_shKM6xQqckUGUaCQ5qMRT7tJtiB6elLm8BhU8mb5UJ0fwxSUc2Ch7uUu3JKiN7mKQySGNGYqRS3Mo962KYegladQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=OGYgupiZybeyrkt6QEuimOw184G4EN_OgQmT1EE9mdICKZOrPcbj6u4Y0gpQLKj3g4rvO3hpUkJA2-7AobgwPQOsmU-D25l4LHecTdWwEwqsKdTKrBrcHEBU8cxxAoyLjDHm2I3XJqeInj23gX280s4-kKqJPRgRzUAE6krYmcHCBf9EU9_Ss2DN6au6ybHDbw2Xzh117aMv7CMmESvra7FnTdeWIzUZMQWPBcja0xSD_xxnatoHWALhdEWuaQzDIT3sMXrdBEjCLEftPpF8IZKkCvAziK19IkFUIUQk1n0Pws7y-3mSxMV7SwJh9sNXYZU7DPXjtml-unV2vDfozV4TP7rnhL8t0o4EsSmF0foUGsk_VNQ5ErWzpGqzUU0U7-vdn8RntPKSxJMiJGQ0vL2Z0o56yXQY2sycQ2CdJ48C3jkQdYRPrOJq7wk5eyelFsCPz024Kj7MOfOtzBZcLdosPZ0jz1u5BXXoc9dv8vALypHeDfNpT3XEpCTKkZKT1V6cV7t_GIOMKec2nYMaEWe-NGzi6fh5E8wrKouCk6e07typ9-53NxzB-mrfYl6BQUwI4ZLFRJODx3rhjRQgUMT50l4NDR2O61OZ2p7NGjErpVtmopz6igpjbGI80lJsOHcBKe9BK_j5tgLJ3TKIpEqnHeL-fHtHq4_mdmktqcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=OGYgupiZybeyrkt6QEuimOw184G4EN_OgQmT1EE9mdICKZOrPcbj6u4Y0gpQLKj3g4rvO3hpUkJA2-7AobgwPQOsmU-D25l4LHecTdWwEwqsKdTKrBrcHEBU8cxxAoyLjDHm2I3XJqeInj23gX280s4-kKqJPRgRzUAE6krYmcHCBf9EU9_Ss2DN6au6ybHDbw2Xzh117aMv7CMmESvra7FnTdeWIzUZMQWPBcja0xSD_xxnatoHWALhdEWuaQzDIT3sMXrdBEjCLEftPpF8IZKkCvAziK19IkFUIUQk1n0Pws7y-3mSxMV7SwJh9sNXYZU7DPXjtml-unV2vDfozV4TP7rnhL8t0o4EsSmF0foUGsk_VNQ5ErWzpGqzUU0U7-vdn8RntPKSxJMiJGQ0vL2Z0o56yXQY2sycQ2CdJ48C3jkQdYRPrOJq7wk5eyelFsCPz024Kj7MOfOtzBZcLdosPZ0jz1u5BXXoc9dv8vALypHeDfNpT3XEpCTKkZKT1V6cV7t_GIOMKec2nYMaEWe-NGzi6fh5E8wrKouCk6e07typ9-53NxzB-mrfYl6BQUwI4ZLFRJODx3rhjRQgUMT50l4NDR2O61OZ2p7NGjErpVtmopz6igpjbGI80lJsOHcBKe9BK_j5tgLJ3TKIpEqnHeL-fHtHq4_mdmktqcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ki8PdilXU0EL8iHLCBDBnegNjN7ZP9HXUl36RUhML-OvQtWT3q0i9NFC0DAvX0OVj4zdPFV6e3r3PH_3f51z3JlEtXeZHpohmAzBIJ5me44aSp05RG38pDZxARw9W0E_UgueIu09Otus7S3fSg__UMmbFyItRkX2YC6AxE1et40a63OObUm0WO056H1i7wfP-g3N1wtNZoeRTVP35coxSD3g04MS4yR74qIrbDkmjDSSb9CXy92gRyC8qXDbc3osaN_CSR4Fvr2lrlSQLNbWMCloIX3yYCGitTuG8prrIuurKAuXWwLu7EYjMt67Aq5bakBmgqTEIQ6WiTp2vxeYsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ki8PdilXU0EL8iHLCBDBnegNjN7ZP9HXUl36RUhML-OvQtWT3q0i9NFC0DAvX0OVj4zdPFV6e3r3PH_3f51z3JlEtXeZHpohmAzBIJ5me44aSp05RG38pDZxARw9W0E_UgueIu09Otus7S3fSg__UMmbFyItRkX2YC6AxE1et40a63OObUm0WO056H1i7wfP-g3N1wtNZoeRTVP35coxSD3g04MS4yR74qIrbDkmjDSSb9CXy92gRyC8qXDbc3osaN_CSR4Fvr2lrlSQLNbWMCloIX3yYCGitTuG8prrIuurKAuXWwLu7EYjMt67Aq5bakBmgqTEIQ6WiTp2vxeYsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwDhQRTAk04ihL9rQi_JqwJucMg74UA9F0BLWr6okDUjjq2xxb1CwLfej3Gei3YhOB4BqFNc0PdO1v0hEFtbEsxitj78Fw_TJ4JQ1DBE6bqwsoZ3zOLrn--Wi7VD9BMOwIZzdjHluCCvnngdzwKUQGaMjIdcqXgoYwHyENyAorqzbNGYsMx-ZXP2Zdz_djog1G7eMPC6tr1cUqz_02WBILIBnT8ntS5A8oKYzFvWE2O6TNqreBOpVEEotGcIA2YAy5mSVWVE1uXzhsAXJtv_XgqxiZ_9_yI1ALK6lW5ih7EXIBYyvdINhRTa6KfFHgODH6DzcFtsYLcd-ba1OTXBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=d7K17AFgyzbOI5SXjeW1EPFduyX_cJFF80MVgB6sJbRJEke61NuBhmhuPM8KxGnj-xpo0JosSGGUVQPPh9cbDQ2pEpOiKMlb09T8xgtOwzpWgghtCleQ3kZK9bjiodInA_0yxx4mENA51OZ89sIMYhpob9Zbnx-ewguD7y2gmXJUAQ7QlNAQ1tLEAzD9TrPvgt2d4ELdsAq9EBhnnCmNY-GFMkmXM3SULFHnBG4smMVg229BlI8vEmQPP0Ienegu21UL4mNFdWmYFEGbXJsINfbFbYNqHuGlwwNUaOxFK-GItWfBbwg1DFQd969_qdT1oOfp-DyvuYNvrEtLQt2suA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=d7K17AFgyzbOI5SXjeW1EPFduyX_cJFF80MVgB6sJbRJEke61NuBhmhuPM8KxGnj-xpo0JosSGGUVQPPh9cbDQ2pEpOiKMlb09T8xgtOwzpWgghtCleQ3kZK9bjiodInA_0yxx4mENA51OZ89sIMYhpob9Zbnx-ewguD7y2gmXJUAQ7QlNAQ1tLEAzD9TrPvgt2d4ELdsAq9EBhnnCmNY-GFMkmXM3SULFHnBG4smMVg229BlI8vEmQPP0Ienegu21UL4mNFdWmYFEGbXJsINfbFbYNqHuGlwwNUaOxFK-GItWfBbwg1DFQd969_qdT1oOfp-DyvuYNvrEtLQt2suA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=RKT88IFJHUq-yQhOq0IUu1kog-pkQzLJcrB1ECiy72vXMjG0cCXArcjlG0FxawXaUNcwyzFXsaGeRafC_oIw75keRf34nhAgkB1C5IKSbQx_NWFIoDM4gumZrgzqYDfBS4DQSYXqK-ZsyF7pi9oCplTCsXiGHjxvq9lS_ARx4PihmaGZ-d6S8eE79CJifxbU3SoevVk2iFdNFkifiDSJWycxW7Sjp-Kz6HaD7mmRGhP3cKyYzpH-Xj8mNg4IYb3k7KwOU7nEyI5itleAcavV6e8TVYppo8qcwzoJw3FH_UFd3w77zJREZPvAsKxjNnNFoLM6j2KgpcSiXuT48EYPbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=RKT88IFJHUq-yQhOq0IUu1kog-pkQzLJcrB1ECiy72vXMjG0cCXArcjlG0FxawXaUNcwyzFXsaGeRafC_oIw75keRf34nhAgkB1C5IKSbQx_NWFIoDM4gumZrgzqYDfBS4DQSYXqK-ZsyF7pi9oCplTCsXiGHjxvq9lS_ARx4PihmaGZ-d6S8eE79CJifxbU3SoevVk2iFdNFkifiDSJWycxW7Sjp-Kz6HaD7mmRGhP3cKyYzpH-Xj8mNg4IYb3k7KwOU7nEyI5itleAcavV6e8TVYppo8qcwzoJw3FH_UFd3w77zJREZPvAsKxjNnNFoLM6j2KgpcSiXuT48EYPbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl5oxnZM5j4L-Jw1lpe26iw8lvhn5CioyzaaSVc59KhoF0Ot4gzkcZXLT3wm4mqp4jS1zJZL7UGm4mlRuiBnPgr9U2QauZ8kTEJMRQrIaT4zDQTX6y-4g2cFptmO0q3YrSSIDqaqekgmfpQIs8DWTXLwOHuisy2S39CsQDF7gKppvhgm0n6D7o-zNMytWuiTVkG64raGmEHFuTxAazZn1mnIKna2BloPaFF5k7SBRT-Q4TB_BACRyA6lr2_FdFbMZewO1MuvYhZ7S4LvsPdYaODIDvs6Mt2N5P4fsSURj9Hwc87sVPIZLV8YNkSQJmhlRsfd2SPmq5VoJW0NUIX2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHy4iKWXoyz08ds--vR8UjGdUzo0OVpCQEtP-IqO2pFeUorCdfZlZEWidS8Z7qBBWCeV9YsjmCoYZX9qi1sI1Bo4SHktIwg-dFPiJbVWJ1xYr3_kcGewiR6BEE4S3pA68ZQfSx1Eo-kzoSrZHYxmp9RZq1h3eXMehkfpNnTBjWzNV-_gmjO--3rJF-n7uPJEkSBny5z1zew9f-XHqkLXB1fJun3GxU3Vg0jdosJWqt_KroLZhm4qUHgdElnvXiAg6OYsjweoW_--8no5vgqsMq7ltRpxRuYb3ASQwFNS8a2Ms8dXY7uyf3lC8IYYyggGK9kWFa8cdCz4ToRy0Fm3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCjvCq6ypiVlUvQqC-cFiw82xN_5CfycXNprgLzRlT19XZkP14ZfCQHIzyiVjWlz-Y2zMzHgWXBRjEEToXbRHEwSGq3n0Q5fS7PNHUSNCqtLSHPN3Ou-LOzk298c0l1yy70Wr6XPNVkY0_oersDnrkEhtkToyaFkdB2AnRlfB02wcdId5Vy7DPqiwQ0ehNSoy5QaTeKFBOwbXzN51zTHGWuUWCwcPbQrHBKvW3d2TrLZ4pUtQB9XalABiCx63Yd_mUlDtzh3L7B9l6LI5-wB2_z8QtxR_3MLFt_WzoVTz5msoafcSW7jH_CMp5FelN-lvAB6uwHFQF-Br-A4nxK8-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3TvBOnYsKbI1xh6sQDFLmacvn6IApq0MyquLtxYDDPmEWQFIaUPIIfknpN9UQ2bfjdEgAZ-CRLj_BSYiFVDHYNOUcD-4ehgYC3o7X6vVEOB_WIeu-d-NAH1KFM0q0azwl3AA8YisURVU7sg3x7VX6gzx1LT26lG8tIhubU10L5Yqe1nqI9lUE0JBXW_iQeqSKeWGdlss1q0k3waqB8iP1iu7LPF-05-FPMD0GbGFMkEqK5nRUH0VgzrW3EzZ6RU0gOVkI0nu4edhooMVrsBkdvVypDnqtNStw54NErQBiwrLO20O5GMYSe9NuC8CKmePS4xRY5bLQSGaxLuAtnR0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJcq2My5hS39PX264m9Od__RHYwdUVVHO-G_qOS3DXpEeNT012jCQG6gSpmOIpIzoPc0qyBI2Evq6XcpPmWgE4qB_CDDihz7g4x2XvVfk1Bsxv2w1oliGW3Bm0YKSXTsEdDpvGxtVPUyY8XXWdK5OVkz-Rk10npo8g8UXd7x1em08KSH0jzxwnEV-k7WayWpMqw2qWXgrNgTOcrXZdVSyKt1cxlxRzVq01AhXbXJDMZRG2D12Ua6B-AllyL7__bXLnEOk5DhBl901fzjBzRdqWLMaDLs_kjQMKKEoa5FtPifrK9n2HiWfT8AZTBXCkZZ8_QchbfclgdpbOqXg_eYCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_QLMQkjzyfMG9tVc9T4JP6KET6gQ3QyZdLChJdWPfkQuWVW-SZADviYcM3AP-qpZEe89Wg1CH4mT17L_r9bc4qPtfKY-fbKuMKZk_59LuzuHHFZEpp1aS_3Yiu40ASVbNEKMEkyxIB3mJroKSdRi2PLtHBtdJSRPY79WBQrP682EsSYskUI5ACL4-AcgnOT0lvLffXzPgAt_t6ek-sx52uh-2Z9njNF39-Vjflv5o6J3OTIHRUT5DKpTOUtyS-lyLtLyS9TMAq312N0-0Y1j7k5p4xChu7FjcMaN8ScPY_TrO2TZx6c4MjwRkhgpNQhCc3WUUrfcGMWwXuSZOgqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf5TxEQUgbeUONA7XswU2mytkhI8p1eMQNL6kc-8Ow25WLVkf6-034TkzoyZkmNK6iOOjRt8poBA2TQH7Kwwear3lQuDQsG9MXKw63jKFQV2R6cEBrablreFIvJs8xiY1hJHN6LlBlYQASX371tCdlQBx3RdhUy8VALkoQ0CDK2hLACSVLA1AgG7TDbsyztEf0PtEqLRq6jAeql2tQhUMajt2HbQJQA27C4ZNlMDlrEVUp33we7-t6zLXy_UxP52wxBd71K57X-4VKFKbUBkGD7mT41W-7KMXHoxaFwc5u13VFcNa2bTopIwsitn0JdmNMkSC_vrOttdt5NWpambcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IC6s0L-yeEeQgN6kysezrZbzO1WBaX03MUikA7hDlakgaN5PyS87HpRXgPuX7iGKYFqoXHrZjUHUp79fxLP3FaeXOzE-g-cJXinOVWlKhBvwpB4ntoN1J4D0UHW5EmFDqamBFc-cbEjxwgpKq3PUGriZGHH-bm38Qkf0clUGoehSqkvUjdxHGpkEHeUWZJn-2SUdyeyCqzxvAZVQSZBLJDWSdAlbnKQx9zoST93Tm-7gnoJL5zEWUedodQShjGWYgD9q1luKrRPySAzq0DAEiTUzrNjVrTMacaPh_arVZddRjCUNFEu7xqfAu4TQ3isWyKPTxh2NhbVaLUwrPkFmMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-0bxZnQw9gFigpguxyc8sF4fe-jCkQkfdoKfknQ03hCkKwGFkVCUwpZghtskfFReL6fXcj_YYRD1OfoTedtvuiiwEOJgtsMoxoBD84irr2QZkuQf7QpcE741bvtQUjDdCZSVs6FFQxtvKmaRoMWB7sRDw5pdP6dZhrQEro_BECFSaPg1RFhNkXHhQwhYJ8IdvvGYFdTepUeo-RIfuTdI8suLG7n52tVQ6SkRETeMXPqG2BWpzU7kf5wZJXpzpzd6baPN5vrpRO4S531Zjn3FAc2hp2FhY8dG58XMih-3KaZ4tnXJnbrZinesGNUMQW6CL8HIrMZvaaMLi4R56RMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnhlJwm3nqpX9C6z8A75zdtRdQ3LnzbZS1i1mt7t1Lap6bZttIu68hePwCblKimxOEgfNyZlYs7sqkpafHl5IrMQburV6ZNt2k3zv-UYrsyjIhZIHlgRvQa3MqDESpmDlQenHmpswzgj9cCiZjEDcnG5x5xW6cNgMdRZYmYq5oCDxQvEbZ0xeDdU8ssljzUcrnvUvOL21F36KhhFZYArnDMPi-X-oul6-gyVL-dLgvFO_2O8EIRx8uTgb0wNWROljG5zefvfZrlH0-yZaMdaNQQAtuhYuZUq93D9xfs_5Fhq7zLuHTq9QJH7lCZzoyASuNCtTOqYhf6XG_pdophSCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=KQXo-MeiUTTfHswkNTS7d8rf-tP-Lk397rspDVFlSujXAAiwfZVMoisKHb4DX2qrxRLaxkRKr8hp1DiWC755hbOR6M5DIXRRNU--6mWxMdNgfV63myUd3ztAXCzXua-AKcB8Jf5bIY-6O9-VwrivlQvC4cJWekMieu4tO1A17nGjjf8UkH7e2B3wmyPaKEVhQTD_jqk8ZyJW70C4floRJwAkNybFeDnj4tbhRVPJyHm2b5MgITwBv9CEvJlfIEZAK38sfZ2vNj0Zk1kWk5tbJXfnRcTd98CiyzgrsV4tT4wVhMUUiJ8ZT0VGDj6nalX94nrOUAs2s0mw1ulH0K18sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=KQXo-MeiUTTfHswkNTS7d8rf-tP-Lk397rspDVFlSujXAAiwfZVMoisKHb4DX2qrxRLaxkRKr8hp1DiWC755hbOR6M5DIXRRNU--6mWxMdNgfV63myUd3ztAXCzXua-AKcB8Jf5bIY-6O9-VwrivlQvC4cJWekMieu4tO1A17nGjjf8UkH7e2B3wmyPaKEVhQTD_jqk8ZyJW70C4floRJwAkNybFeDnj4tbhRVPJyHm2b5MgITwBv9CEvJlfIEZAK38sfZ2vNj0Zk1kWk5tbJXfnRcTd98CiyzgrsV4tT4wVhMUUiJ8ZT0VGDj6nalX94nrOUAs2s0mw1ulH0K18sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVwcyJg6oD9oZAnNe74K7MwivRzI8_e3MQIr1PunF3Vglt0_aIme9DQI7OXhDRmIjtGjmQL5fSxesOzwqtAaJ1fDz9bpwenfBh2LqgDsHYIN9QcODI5CkdCODnPskpAl0u7OS1AMRplA9tEEGMz5IUkiJ8BDRi5K5Tyq0HQExHbb2AqL24wi4GLN9_RkNLQiwzpUdQ5RQACZ-G1m4qecQv3O9my26Jt68LlCrv8Ejh3672-xEom6R1uu-WPiTGU26fn1-PVymgTRL0dLKnYOV73Y106ZWgyTabDbi5byI08WCmZMzmmTHtn1wq52TDmcWrUu_1WoBM7Fra__WUF7FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MswVJwR-lmx_L_rydcooZcY-VoI6Cj1Bg8ROQCD_jLCPaJoa9rSC8YpxIzXU4qLfJA1jMv68z6cRjynmJdvJXieUqcYO7G_6K_Xzi-L6zFxuHVo-mehLTNIcGcdLnBRIrgl-N1el-R2pa5TijvS-HX7rMjNZJgjHJtZcesWG6U4IyH5bRBJb95jm8hv6e9rxvKx18RNik3IqgwWeY8ThPGq1X52851Nipj0RldOiIYqXfqFzFb0SupdqCcZuwbLKtBfcBq_sQmfJc6hOW41wVxRITUSSPep1TM37eeYHtePxdYj5RSKyEc0MLiatPqve09ETkQ9ih16BHVUzNdQ9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QxoiUSTTQfGJLjmw0NhEMW-kxgMEpQlNmt9GBUPFC7UsQi3yJDc8Lrd8jSSwqA0FJU8eiZn7ttAysDKCzDGUpJEvSDx_EsJrjTdkV3L0xsUtXoKZW6Lor-wdqnkS1dOwZYXIbnZgOFd47yXJZmtHJoN2QemAUFzxeqHCXLdqYkQ82psvT4T6EsU1oZR5jLjW2vRaINM1EiZPufOZKPuYH6KzRfuB2EwGiVIK55v-44WMP4O30agAd4M4w4DIrHIETiiM3RiqkKd8VOVSg30cRyRXsEnMj4_DNxvv1dK8AuZGAB1dXdpZbWGdimvcj1-AtBVgw8BnfRFAe5vNNG2GLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QxoiUSTTQfGJLjmw0NhEMW-kxgMEpQlNmt9GBUPFC7UsQi3yJDc8Lrd8jSSwqA0FJU8eiZn7ttAysDKCzDGUpJEvSDx_EsJrjTdkV3L0xsUtXoKZW6Lor-wdqnkS1dOwZYXIbnZgOFd47yXJZmtHJoN2QemAUFzxeqHCXLdqYkQ82psvT4T6EsU1oZR5jLjW2vRaINM1EiZPufOZKPuYH6KzRfuB2EwGiVIK55v-44WMP4O30agAd4M4w4DIrHIETiiM3RiqkKd8VOVSg30cRyRXsEnMj4_DNxvv1dK8AuZGAB1dXdpZbWGdimvcj1-AtBVgw8BnfRFAe5vNNG2GLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dDXKOIOw65qvp0QmTz14RPXoWuw1Axl_Aia_IGd9pXplBGrY4tvA-Eb3Yjm_GgQBdLBQ9iO5zlsQxYhJoiohw6hkTJ7uzD0llXPiWoasa_C85GnCW2bjtIR4XT3SOa3Nr4CBdrkwc2QxAyn_Enrxz1lUB7hzZiFgEFAT0JYZewWlXT_lMONdqDcl88C9h5li1z5qqpYuByFn2uPrDGeKKbQHvtaSe9WFkLgXdKLAsIgTmWLs3XN3FAy0x59kqnNCKzL9h3AL1CamSJFI52ngGCCFiqtCf-hweDaYWPVgGdtjf9dfC-8zgJeApKw0l1FELLyTFGCGhyf-guEGOEjPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dDXKOIOw65qvp0QmTz14RPXoWuw1Axl_Aia_IGd9pXplBGrY4tvA-Eb3Yjm_GgQBdLBQ9iO5zlsQxYhJoiohw6hkTJ7uzD0llXPiWoasa_C85GnCW2bjtIR4XT3SOa3Nr4CBdrkwc2QxAyn_Enrxz1lUB7hzZiFgEFAT0JYZewWlXT_lMONdqDcl88C9h5li1z5qqpYuByFn2uPrDGeKKbQHvtaSe9WFkLgXdKLAsIgTmWLs3XN3FAy0x59kqnNCKzL9h3AL1CamSJFI52ngGCCFiqtCf-hweDaYWPVgGdtjf9dfC-8zgJeApKw0l1FELLyTFGCGhyf-guEGOEjPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo0wUuXYSZMld8pj8vlI6el2b3G_0ro94qR-GJYGzpj67kb5wlQ_BNBIhmz9XWoZEIg2xvaLQRBvl0FGuKRbVrH_ziCfJEmkrjYEBmbulXgLtApl4ZpXunK7yevkWmcjiLn_QgEq0Xy3Ken7SbGydGrL5egI7zxpmI7nOMVeU8Rq8ZGEAz4s2ed7poYFCtpFxA3JowNHdIVDxDJRXMN4-DR6CbzI8y4CzTyuAoODgKjVxgCM_96T8nvTlLNJp3TGbyTuvDhwH5ZKCO3PRETl0N0ql3LIx1S0gQYDsvYUN1karIHrcAj4ypADapXMWbcznuTw9ryAqRZMYNND3ZvI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdf_NiO8m0sqlR2bp7R5I8gPf2KLdgNUTxeewJnqh2hyPZGWj2dzKic52gaeW6-ncH0_-TpnnHmEiBUBQtQmtU_aarVvyz6VGweXJmnVx7SbCFd0fHyrdkshs22CBKIqTwV-Lwgvuy8-JKjdyazR83IAIrFzIpD7TVrQ6EHwjv0TFnJAJvX9_cOYvyDhxUS9u6Ci8ZKWNThTVzSHDVMtiZyeSq3U5u6sZ2YiIIbw3b3F7iGotoZOX48cgnfR7GKDqh44KzMAqLV87PiFbDswNrjQmu-RYHH9jauvkDIf_nzmQhWjKsMaafttnuGktUEfNyjkN5WtKc6Ofw7DKYiaCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoFRzkSN05QM2_ayVkCBQqH3KsNYTJ1o-Emrs6QoDKSaD4Qzh-U8NmKspwB-tudo087YFvmheJtSr2VIPJoA7F9bDdlYgQtym8nq5eOUl4Mb9EUMKQQpIhuQulGvyhVy815tzY2xqIdGLDvKW6T07FnICO_pKT2aODJDr2buDIK5Qn36th4FXmOMBJq8GxoZ-7RdtgaXAjRKkdQ8XPUsaNiuUEXOgwNTnGaNuB-7iHgK68Ty_A44HvNjZ3vEVWfmQPZajyPuu9i2PNmmsDY5jo_b5D2XtkuJDr1oekJIEKC1YEgmRFUYV99pUAq_ezh2dIOPbiBtOeCJvXeP8vrtOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvu3Q0ewXqSDlOVq8giBQl9lpSAdDyde1bio7QThINm6ew5f7ckxrEThvtSQfJjgtyY2evgY48deoZtuXChZ5TfOkwrY5Gh8zGgZVMBG7qF_co1RV0Pe8yQJl1C0BT-dcOpIqYvWx3xicLXmxWo34VszT5D7vhm4xOu8eZVPNSRYv9_pFzqp5LXv4faprwe1zv-kjKnY-x2G2ifmIrNMppcnbiFkAYsUVE-Dt5fALHskqPp_f5ru0xrH_psSJsDpCor_sH0r26zkcvxWWGjy0Y-z_tU8UrnCYC7f3e14lXyawe0dnQKRUR6kc-6D-EGnOrgf676MUm815-AOax2WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIG8qYtIIB19D5q8Y-qfjr8I_DuDX8TfmqzWWfYXG0qtbhQMoWleQI5OzMM7IG-uqXczKAtUVrG8F6t3_0vjD5QDRmbKIYzKPzi30m8H9vIgO-53pGxoq4CpyqaivKhRYYCUDdJwKWiunIGwlgtH62tf2Q_c9sauYGFw15Ot50iHfbckA2yWRw3Ib-yu7W0itL3czXssYreDRzSVnbLHHKAp19Q4WhEcLwfeJIeKMeg66Yt7upXWTORlcQiocKmEiSNzBn62HPGPqQHHa27v_7nauF045BBW8FShnpgdWIn9x_3A5wn9UKPl4DvB1WojoI6v5S_s23wzejyPkhBR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnVlGqzDaNgCmPeSCyXsSHtAen_7HADehCvDDzeLGITLyJs_oBJAoLKXch5oIFIWRUce7SZowwtE32AsntKxw-EUOEMPpoyvN4rnibkSrQLyg8PsJ_eBtvAKPOx42LUkiVxZhYpY095QP_aNfgKhlxXS2PMkXTrFLxfivYDWLHry0AbycShgXde9pR9K9vi_CvwvYoXCSyDSFY84Oil8vp7Bnq1aISrZ25bgesLwueBg9wKyZGPjvN9nqzBPsyDrfN5cBv8uZhzsmCPGufD6QdLSvloX9foiOm5h6EACVY_Z5rFqUiloe4_1AmpQbVKmbHsF-wcaWCWPTVdKdl2_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgHL7aK6uNOg3SFP9c5phXbOT5xEOxO-vW6SGeP9eRN01ROfKgWO_HGwaI0KoJ7d2QghUa2CrBXkiTa55yWz6T5w-qHs9_x8-H9TK7z4Km3UXbTb2DYK7JPlXuMr4R_LfXqLafFlNkq6h5o8IWi_O9Xn4bS8FA-Uf8lhxnY7qJ81d3KhENiQcGi-gEBzDFHUs7u1i1PrDQ0BwNhHl3VR3OnYVkaDHx7iTPZcVICJEhfnscDvfGU3gUtgwZUbZdXaRCUKwAmH7lN-CA5bEj5BylEIur1K1AXO5GzK97Pz91Ci_s_VwSObBSS6eSm3zhd2ugphh0xunEwuy56sjv06OA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Vx0Ck67oev6rQuqzBXCg5RLcU_WvR9cDdD0vwYuUHXrA2O7f86VagQBIwFH-xflRJhGH0csyMVEY0_oUFTUsdk3032lTf6ar1ZN4yKvRWh4_TiqO_NqNc-GFSav0yRXctP3HHXdnfhH_BXOVAshDnWZCItJnVbfKpC2M2uxcBsYwPs0_BocHYq4QaCk5kfO4Y8hXi625-qi-9gHTKbwhQ-nh9dLlwE4O8QUdhlqp9wJ4uJaggjNNtU0TDZ4-nu18N-9Gj5IFaJP3OTiAji8jsreByzhvvb2rTXjiT80zksiezuAHQEx8oBye-ntaOUv8m5PxgX-2lSsOQC6aXfKmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Vx0Ck67oev6rQuqzBXCg5RLcU_WvR9cDdD0vwYuUHXrA2O7f86VagQBIwFH-xflRJhGH0csyMVEY0_oUFTUsdk3032lTf6ar1ZN4yKvRWh4_TiqO_NqNc-GFSav0yRXctP3HHXdnfhH_BXOVAshDnWZCItJnVbfKpC2M2uxcBsYwPs0_BocHYq4QaCk5kfO4Y8hXi625-qi-9gHTKbwhQ-nh9dLlwE4O8QUdhlqp9wJ4uJaggjNNtU0TDZ4-nu18N-9Gj5IFaJP3OTiAji8jsreByzhvvb2rTXjiT80zksiezuAHQEx8oBye-ntaOUv8m5PxgX-2lSsOQC6aXfKmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSgtKy3d3nWIuhwp6NibMIV29APl2qNr7OEkAvVpfGBZ3iB_RWeEkFnHVNuic-gPxD88vAfRcdFAXidW1qBbHj3UYE_rLmBD3LBxIxffArBU4V5gUsWU3L9-l6tnZ8aYh2_sI3IMozX65cwBrGuaGtgYue60eHNqAM0S8T0jqroK7k1prmtIUxzXLMx7LTFqdz4ATcZnpzPsq2nLRZTn_pm285gcm2zxlJpJUZ_g9CCehJVCUkwNLjj1U9rJzXqUta-PY9c2Min-Vepqgln2sxrID7mA-ikn3_KmzOOkI-iRUoGWOjAp7DNC4reDPJX6kjwFmZgfwO-qphIIGfMggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Y1UfRU5fCTmKBbYV8IFL9I_WA3ZOj2qTilHwOy4wBJT-hea1ZODZtO5teOp7yl2fYGSdzfL_KH_vbxj8EXhtWLuuiWZXGLJ0h1Kt0JXBNJvlxxakrbp16yO5Nz3M34tTYSo6Gxd8ofhnKDr2w3HLifZR5pwtRVuELBNd6KvaVnj-7grR7nDg462dyyW7ShtNReG4G9qDhkspFCfQBO7CmQHwnbmv-FeGvf5jW53Arw0yOvo5-flosOek5zv1LfIBDyGF40jE-LO9rPNt3GwM4BQ6nfyAUyA0qSa5m_FYXXhcAtlJKNghZ77Ynoh_N2ynnvVIXMyxqHBjsBba-KqyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Y1UfRU5fCTmKBbYV8IFL9I_WA3ZOj2qTilHwOy4wBJT-hea1ZODZtO5teOp7yl2fYGSdzfL_KH_vbxj8EXhtWLuuiWZXGLJ0h1Kt0JXBNJvlxxakrbp16yO5Nz3M34tTYSo6Gxd8ofhnKDr2w3HLifZR5pwtRVuELBNd6KvaVnj-7grR7nDg462dyyW7ShtNReG4G9qDhkspFCfQBO7CmQHwnbmv-FeGvf5jW53Arw0yOvo5-flosOek5zv1LfIBDyGF40jE-LO9rPNt3GwM4BQ6nfyAUyA0qSa5m_FYXXhcAtlJKNghZ77Ynoh_N2ynnvVIXMyxqHBjsBba-KqyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=NRSNaWM5s5WMpo0BqXNMQpxL6zDT7Eml1LTZWgOHJtY1vlMy9cVlMEcG-1rJZQ6YmapM4qB1fcmcJSqkhKcfZr7SsquXdZaM5uAPBSltQ-A4b5XxpDn_L52-GGgSgGVALIWS2bna5Q5wVzmFTQb5xNcneEIikBiqs63IbFaVAyzIBSguZMBT4K-jSUDdUlJ9Eu3__3y6jHKLHvez0W6KClzCYQ8JKN1MQ3zc2sAUx7xGBNFGdNjIO-Z3sUsOP0vMkvz2mDz1Z9ygOTq2rqchGL9TwkWDSGcNoUWvuaDRix1FREJ9ynISJNdOKUZfVkpY3lbxo5ztLZ-nlOdq9_XUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=NRSNaWM5s5WMpo0BqXNMQpxL6zDT7Eml1LTZWgOHJtY1vlMy9cVlMEcG-1rJZQ6YmapM4qB1fcmcJSqkhKcfZr7SsquXdZaM5uAPBSltQ-A4b5XxpDn_L52-GGgSgGVALIWS2bna5Q5wVzmFTQb5xNcneEIikBiqs63IbFaVAyzIBSguZMBT4K-jSUDdUlJ9Eu3__3y6jHKLHvez0W6KClzCYQ8JKN1MQ3zc2sAUx7xGBNFGdNjIO-Z3sUsOP0vMkvz2mDz1Z9ygOTq2rqchGL9TwkWDSGcNoUWvuaDRix1FREJ9ynISJNdOKUZfVkpY3lbxo5ztLZ-nlOdq9_XUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNkkcnurwfGNYoif82GZIF_c8awGD1f8x6g9VjCTEqnI-5_TTT29H72nMYxmCnaWAvxoa412vIG2YGvYvurvdfsFgfKfJdZ4dQqqkTPObo4nHl6Ttv8WS9SbhR5w7XRzgfeENgbf4_ytH2APp8LFqj79nVswJe6uk6cPdz2p6quDsT1DhG7qWuveJ46SIMAXBSEHq78iR9vx5opLS7ceahclMnXWJ7p5PQhAv2VYHnkZxCjuJlq1lGhUgQzRffc66SOVpcyQ0N_z9HqJIigKEQ25CSOi-Lrj_wt9VdsgJoGOZ9CSnn5ojGwyfCrWoYqzg6L_YmZ1ptdogUHwp5FFFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4pFwmEVVK47cTcSoeWb6dYvd2SUgqhok9bQdTyD47s9vJq9ab-slIbtLeFRv0iew1YKyy00ruIHTxPjvE_xMQ-qid-StjQvYm3_GtycqR6CO02BIMhxFlj51hthV0dhPiYaYVb4t_zPh3ESWUC1F343K-tDkIXA4aEEnSCdjZHr2yOyT9m8J53Pn0P3qotmOcB7TMDbA_pmCnmJ1r5itH5uxkEQRm_tVreDfMoOsIq47cAasNGyyDTCCH2BHH3le4zzwyAoidduLmGjDX_deYf636Srj8Oen1q6TwpR0K-rCWfzYiKznV_oajOrx7z-spK3c-_pK3yh9F8xbujK9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=j2nw5fu1Bq8bHhBZ9VgCytAG4MpHe2QCiP8nCv_N0m44eeEDEQ1SvULo-umH8aBnQrClIoWMu6wyY0Ph6idnr3XiK-YYIX2IgrKt1p5tXL_YlQA99ynDXZRLRVIrdkP7pnWA9Gk6cJDMhSo_cV4F9Qcr7QIQBSz_sXmDonDy-GuSUnKrW4ihkdR2WYEDnJICj8uqb1WxMGBsr7tAPDISJHAoBocyNB7fTRmF_o6dFeHTJOV8HPtgZvQWg76lkEmBBKYclcrcnVdJGUiH7tlMuXcRPP4UiGj7egaEL-ma1jSN30et1Q4EQeLEAX5f0_jbTR5K8sst6fHJP1VdqlcItxldsQmtKgrdmj__JtrOtKFQZ_TioLBFyZjn3c8CC6dD-E9MJHN1ZGr2GuluQaSjmyUeotvu_4WEw3nRKrfuc486a-VhsGJPweTjaXgyOqGV0OewZnBQ11aHLTBWlsd2lJqU20k4jOptE6wkuX5IasP1C403pCC5G4h9flJelIChKxgRtKV5eMVBvGOno-yI3GmSKvdaShSg4dYncdfWHmIgVTOHbQuBtk5Lk8KR04MhsUBSo7BbRgWpAoWValQtGSOEp5lZSJjIZ9IBITy-YS6J6_NEEJ1-XH7ccm8rk74jPfoYq_1M-Lae3il2qI34wPR0u-rksBL-eZM805aK2cE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=j2nw5fu1Bq8bHhBZ9VgCytAG4MpHe2QCiP8nCv_N0m44eeEDEQ1SvULo-umH8aBnQrClIoWMu6wyY0Ph6idnr3XiK-YYIX2IgrKt1p5tXL_YlQA99ynDXZRLRVIrdkP7pnWA9Gk6cJDMhSo_cV4F9Qcr7QIQBSz_sXmDonDy-GuSUnKrW4ihkdR2WYEDnJICj8uqb1WxMGBsr7tAPDISJHAoBocyNB7fTRmF_o6dFeHTJOV8HPtgZvQWg76lkEmBBKYclcrcnVdJGUiH7tlMuXcRPP4UiGj7egaEL-ma1jSN30et1Q4EQeLEAX5f0_jbTR5K8sst6fHJP1VdqlcItxldsQmtKgrdmj__JtrOtKFQZ_TioLBFyZjn3c8CC6dD-E9MJHN1ZGr2GuluQaSjmyUeotvu_4WEw3nRKrfuc486a-VhsGJPweTjaXgyOqGV0OewZnBQ11aHLTBWlsd2lJqU20k4jOptE6wkuX5IasP1C403pCC5G4h9flJelIChKxgRtKV5eMVBvGOno-yI3GmSKvdaShSg4dYncdfWHmIgVTOHbQuBtk5Lk8KR04MhsUBSo7BbRgWpAoWValQtGSOEp5lZSJjIZ9IBITy-YS6J6_NEEJ1-XH7ccm8rk74jPfoYq_1M-Lae3il2qI34wPR0u-rksBL-eZM805aK2cE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuYqfGAoadTcJjWR-mA41r8KQJz8du6uK0WLCLYHC1in6QqOxbHWjsYCseXyAynylv2Zxf-OGDt8BXbMYYljppMovH9Luhh9kYSI0BBGqvsrKjwFxTZQtmDafZe_SIH61qnx5Uoyrk6glIKSEsqjUnovWdY1-ptNkAgeq_HRGxhKC0ATjXSM3NTjWFK11OPH6Xd53e51_31wx0C1_FMYn-nLXqJKad7NnEirXZUA7w-yeGo-7PbNvefJu9AAWY4kGUqKqxR1FLZcZJX0ossja_kxiF8pI8pnBzfE-kz-X9rOxhxOr7rg2JHPF_mSL-QWxRW2bGZ9Hxj2dfEPPPfK8A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Od1kVhXRIr0TmQHEHMEcBDXmj44K0Cp_6-MMfFU-arXtGvjnrw3a6wNaGVawbSNZeCMejydVZ7PShmWKpr83bhWBdGhAl8U8WX0H3RXPhq2xVWxzz_WytVLqRYAj-fAGLEnT6u_iWa8eSQQ-9iYwKWudi1wE9h49jvKU5dRzsO7SCwTVTt5IWi6LXNY2wgqjTYE_MRZvoajpn_ZShYOA5HatDtLaZXpVJvSGvLSgB-LgyZgV73o7uIHSFsl4lK2UDRvqgi7OetJPevmOEylt-HfNci_jVOss80X5RxT1Ucns5HSzDURt4h-tAdKNJ0wP65v_yKtqKfXXC8NbFCm-BbeYvhp2JcGqVYZN4XgatP2pvl-ygI-2XxYfjewWlU1kmSodUUtwd5ahHF8D9qJPKiFxbKnna0LjxaqOvgFLTiVUk9XMIrGZxYxR-9YXeCwYbmcoOh5mI-pUU0-d2DuJb1p4T9BJWhfjQD1sSIIczQ-9ymDWMzTCn-GSCClmz6uf92T7PZHDhTWYx0rbn9UAitKIhaegRcICoU8UrQT1gS2UymXZ7rO_h-Jgt0ypttDV_bHoE_23mV3QbG7HyXxBQUod5U8WBnfecxdkBB_QTmVf9LDCHw_sAISqt7CGIZQux4a8v7HyyDgpps-0ONCY-HoTz7KyWxOkQ3dhhkSGd_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Od1kVhXRIr0TmQHEHMEcBDXmj44K0Cp_6-MMfFU-arXtGvjnrw3a6wNaGVawbSNZeCMejydVZ7PShmWKpr83bhWBdGhAl8U8WX0H3RXPhq2xVWxzz_WytVLqRYAj-fAGLEnT6u_iWa8eSQQ-9iYwKWudi1wE9h49jvKU5dRzsO7SCwTVTt5IWi6LXNY2wgqjTYE_MRZvoajpn_ZShYOA5HatDtLaZXpVJvSGvLSgB-LgyZgV73o7uIHSFsl4lK2UDRvqgi7OetJPevmOEylt-HfNci_jVOss80X5RxT1Ucns5HSzDURt4h-tAdKNJ0wP65v_yKtqKfXXC8NbFCm-BbeYvhp2JcGqVYZN4XgatP2pvl-ygI-2XxYfjewWlU1kmSodUUtwd5ahHF8D9qJPKiFxbKnna0LjxaqOvgFLTiVUk9XMIrGZxYxR-9YXeCwYbmcoOh5mI-pUU0-d2DuJb1p4T9BJWhfjQD1sSIIczQ-9ymDWMzTCn-GSCClmz6uf92T7PZHDhTWYx0rbn9UAitKIhaegRcICoU8UrQT1gS2UymXZ7rO_h-Jgt0ypttDV_bHoE_23mV3QbG7HyXxBQUod5U8WBnfecxdkBB_QTmVf9LDCHw_sAISqt7CGIZQux4a8v7HyyDgpps-0ONCY-HoTz7KyWxOkQ3dhhkSGd_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBkfMfAIJOzr9NOmT32fBfXzoHbzMpleJEKmaqtfptoPuaegTkWapf3-cBbgtml4LX9k-nqqgtODB9vFyluGioxGyZ5nDrL3tVidRWumVbKOAiLzqWL8Fi4tpT4OgXpSnZVMqRh3OZ0y143GdphX8K4b6bxrEhmUiOd56rQI479u6jD5hSuUyMYtf5khiii25ARQLMVnZJFc4YM0ceF0wTOLeQw48f2yw-UQJd9bD71EHyS6jaduP6TbWat29V9fhekGWZyOnc5Bh0goPthquQ9CGQLGt-onDW4iFMS4YrY4AjbKeHsXXS0FboevhFDF2ItIFws2AOF7nJomFK2CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heDiqZu3wrBZ0RQmwBuD1NB3CYn-WoP8bZ1WSUb_WL7cp2k0pafrIqh0U4c3TR6Oo0VxOlp8E-Z2ach9Ojd1StbO09ypapHO9aVL5tqUc76DTXBZzlASrq5CLSL9xabu7st7kstXQygdIQSLXretZ8UjQDbWD7ip4WX5TOM2TYwOIWDRSay8hxq8t_6Mfyx4EZVWsf-GTaOEBE3b32WUA_BMfJXTEz0vvDQUyp7bDkZqYvWtBhijJdwv4T9XSO1yvC1_wbmS6lrxHRyIyc3OyIUM1lt1rNyreKKpFVl9L-DDq_z4AL4yPvN2Tyx133FBK9esQQPG67T8CHxsibVOLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuGaVXTNpwuZ2Gb38FjyD-LsbnDwGF02Mdx35zyXzk7V4X2wbeWqK6XihNmbsMnf02UM9xT5cvBdVe5En-HeqiO8HqqQE40vgccEQ2QYjjRwqv3ktcZqbwtwoQWhKgDPvMd-CFJ9hn1t3AVxO5i3OA8V71QTYgBk3yL6ZQG6fXDv-TeUgCLNQeDBajkdzvAiq6VUyWluReJXCzNe38eOT1rVWcDDZD7NkgpqFIDE7VW5RAQCALC-AJYNo4OY9Tvd5X6MFVe7Byo2UqqHszye9QG-Kw-JGu99xT_Da0IBlJAuAIq6mpBoUki5M3-iL6_r0pIDNGK2aW_RB01KdbsSaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCnADGajDSmnPQXYCul6O0RDNSWQ23wJzWhGBqjPjQTjl-PgbCQ6od1TDAmgzVJz4BfxyTsMI52kh-9TiVL_uE8JeQOkVwUZq9Hr5pWTzRvfrpo7WOUbMa8YN0RfhZUQFS_vxK9t7mhYwFIvgGdBFv3ZixuHRSGeorsEcKGkEwwaZqPi7PhKR2RO3WHDYqkw-MfaKsLYi-8mvBNCSHenPBoxTO9VmXozdu1_sRvRSLymo6KcMmXKS1UzE28QGp8eYtmfHpDLHOXvx4HlTCcyp0JqwaWiTAZbIHmdHjyEVuOLJOPSOXnEK1fCX_Bx9Jh24KB6QlKQN_UO4ai2PcuMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0vEVek2FGvhkk9nGYf4FCKwZ_hBNV5Gb8aghv_FBiSUdflctF8D0qzM2OWf1AKsbSUuj5rJK_1dN4SLKhj7XeL-oLhG2ksfbh2IOX6UCoODXg9osrL0ER-Cs5BT064-uQ85nQOSVJBsDJc2diXEdbuleTPJnH1DQmQ6h6CbZ9JNaOFgsP1FFz1yZFnCaH3LjeKV20CTgLZtQFseATOfPo8cb22gHl1Orc5etpIMlqxrv7yr2TfzSlj9l0EfATNoUT3nLGuqnZn1tfUTOdPiQ4-OwuEYvdqw0BWtpFz5dx0TVW0ZrB0pqtgQXe7sXTnaOxwwwYq6EuIOKUi8WUtPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
