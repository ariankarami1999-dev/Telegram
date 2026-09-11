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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qia-P_vF1XX_UfyE5sf1mODjf0HuKmM_aLxspRgx-ZtoJAHhZX26lcNYHdK33b1dglUCTjD-hVFxG6vX22Ix9P1fDCiM7v3UVZ44tNIDGjF3Zl53zVMHAo_Cdff3zJUwCf9dlosAhjwicAJX_RtdrkarJsnNNNziYW86XJPmeVNOvUH2oMMIHR9r-67PiAYWEnN-cRfRWQwlbSoEuP5oWGVWnWWPUnsgsbg_pAF3KE7GSDFo12fkzXZBJ0LSKojYvUdi9sQaaZPnDQn2RSsrBukAAwZEfO0l0cZDTKuhP-S_caxClY3bBd1Acpk2bN3qXIjb6Gi86hOrW8DOaiqgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qJDW3ijL-EADTKjVkptjbrxjvuYAM6NrijyH81V-LEiY1ZeIEZxfZDNnkwkHeysDTv-5Ap1KoWS3l9-WVvXkA4usETYByqGxwj2i04CtpIDxoOKvNu8nh4ST39685Te5ZiIllsHeubXn2jX93Yz7u36pbzo1txDtVZGzFF5RrGs8-4Xq7G0ikZjfuW9mqpD343LJiTslubiseJhjZVOCrINLllQ3A5-r0e6szlhw5piOVhNV-Y3RnygW61S6uYergyeOIbL7iX6xKlY0SeLKfaUubgBPBKtaCiy0uIy1-8o0zSvB88YGnPEo4_oZA8Tp6HUyeJB6qp862ZpMwox1izzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qJDW3ijL-EADTKjVkptjbrxjvuYAM6NrijyH81V-LEiY1ZeIEZxfZDNnkwkHeysDTv-5Ap1KoWS3l9-WVvXkA4usETYByqGxwj2i04CtpIDxoOKvNu8nh4ST39685Te5ZiIllsHeubXn2jX93Yz7u36pbzo1txDtVZGzFF5RrGs8-4Xq7G0ikZjfuW9mqpD343LJiTslubiseJhjZVOCrINLllQ3A5-r0e6szlhw5piOVhNV-Y3RnygW61S6uYergyeOIbL7iX6xKlY0SeLKfaUubgBPBKtaCiy0uIy1-8o0zSvB88YGnPEo4_oZA8Tp6HUyeJB6qp862ZpMwox1izzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Krr1suwTeJxBXWgalVX5Fozbjw-857CZcXIJmjgOKWNocsPyMsE7VYzdmgnXBEyDS3IHJEoL56dnLzcmLTLbkZn5yy2ZLTG_Hnqbp8VlcURLCPuPlFIDf-fQGfADbFocQf8XCU9mBOwQH_4PZgUoeozYHjyVg9hH4m1N_9Q6OpxHRLRw_uDJZD8binXMu_mTZ6BpouTFmWj922sjvGujrJSLwl6_Alp959KZVqpQwixnkoUCwdfWACceIL5puNL8gJ7quztYsLFwihLqBd_N2WEcdzgWXolUAAkdwI929Rb1Ktpk1yV3tcEhn1YTwynfXf_00q-NEzJvUFwnvU2mAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Krr1suwTeJxBXWgalVX5Fozbjw-857CZcXIJmjgOKWNocsPyMsE7VYzdmgnXBEyDS3IHJEoL56dnLzcmLTLbkZn5yy2ZLTG_Hnqbp8VlcURLCPuPlFIDf-fQGfADbFocQf8XCU9mBOwQH_4PZgUoeozYHjyVg9hH4m1N_9Q6OpxHRLRw_uDJZD8binXMu_mTZ6BpouTFmWj922sjvGujrJSLwl6_Alp959KZVqpQwixnkoUCwdfWACceIL5puNL8gJ7quztYsLFwihLqBd_N2WEcdzgWXolUAAkdwI929Rb1Ktpk1yV3tcEhn1YTwynfXf_00q-NEzJvUFwnvU2mAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCvur7gqGhDbgM3TKCyPWZba0KXa_zIoFkWBUXRCFnVizoKbpkKwKWkjm8AwjBAwZmu9wuIXz-_AYPzSgfwpIaLKT4y_XZxjytvYqxxSkK8gkMyuW25mY-hFUAOdCkt1fMuqKH4UMKKxPqufJbbW8W7RcIuEuPbdRVJ4SIIdBwV1hxcGRPKM2e0ufh6MIrOzbisn4bjqQB94dXHC9oXCbWOBQyIaQFJdvi4LOzWBBBXOROsR-srezpnAyet6rvtdUGMSN1-cN_xrsC---dio6HdhEEc09LILPJTwaWsUXJzCmcYILKN12QpTljKLwJBR8p2kErmATQBVP1A42UPCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdSaHxqw8Ul-c9BnUyYEWZhc3vZdH-bUIgAS5EO3YIz5_eIIJ27XCLRDALnG-3G7ZjZrcBb0kRM3UII4WeE1B6XIXMA6dGHZEGQKzGgAnOX_KS2h9c1Y98bHvBnJflrn8tUQWNA8wnw_fqDRQd3N5LABkZXc5N7MvMUJZblXIC3Bfes5NBh1f06xAAzIg2Nt15RHskYrkq5SF9_6i8OER8QUjfoivMFF3J-cvZEEtAcmSKKBW8wqX-_xxag1ZtHRsYjyIWafCzmXnCiN8BkWCQg_4DW5HURd0JqmRteN2KvHS4_uS920ethFP9i92AIBsGmECOoxsmBvDcV-82KJIw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=GbCDERHb15DNyYnMsDLsLn4yEEIbihiwh3Qn7weK4Z2H_3WIzBH6oBFyu5dRuCbuIwlREg5obyL3_r4c3ALGz4P08KuGaeSNfVw7pXsVfvxWWihHwpwZCLWoh-46cbNnNdmR9ft_UCPTTrV_TRuPzLzbUcbAOLxeH9vfkAEI4InngG2zTckX5urWtEpBtZ7omvSmmjhm9dD6rSD9w4h_0IkZ-YliKCZ18wvJ_uhTFmhrbidY4cUkI6_M6zNe7Y7GaolikdrGxtBcWQlJt9JCU7u0z64O34jwBWEVF1xv-Zh3UTfqK0D8_ksVn-_TPLA4ZL_fB40mBZ5gyaPQj2xAkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=GbCDERHb15DNyYnMsDLsLn4yEEIbihiwh3Qn7weK4Z2H_3WIzBH6oBFyu5dRuCbuIwlREg5obyL3_r4c3ALGz4P08KuGaeSNfVw7pXsVfvxWWihHwpwZCLWoh-46cbNnNdmR9ft_UCPTTrV_TRuPzLzbUcbAOLxeH9vfkAEI4InngG2zTckX5urWtEpBtZ7omvSmmjhm9dD6rSD9w4h_0IkZ-YliKCZ18wvJ_uhTFmhrbidY4cUkI6_M6zNe7Y7GaolikdrGxtBcWQlJt9JCU7u0z64O34jwBWEVF1xv-Zh3UTfqK0D8_ksVn-_TPLA4ZL_fB40mBZ5gyaPQj2xAkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trftaCC_yl_doOsWQwS5SZTgyr-pQ1zQmC80mxMR3y-KwpHIJLRth5_BnNYIalM0sp2zCCBes5Wsv9aIeT7HNNsFispe-7HmAlEvsARiUfJolHQdU8Y-JSz9_4toBL-TuGGpwx-O1fAX77p0rj12PI4VrTyz11SSH1lAB8fzc3NseAE8OfbJ8g-aMsGYJUbffPhnT9pl4JLBtE23M06XouUgIryNqEHW5rfIEsMhMD_lsRMmqNnOEuTYwtD-gaoFCftjZIdJoVfEZCRyVD_OUJC59qj4CBm_kaWv9ybp9q1ZrFxZ2XAB_VKcYCE5gLhg6hUuT1VmAPhw3JonJOmyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NioGghf-LfdSLavDODfeWFCkQOJcxD-j1z5HDLv8t2kOqtcPs1SZ2fhYBfNhwhB6oWn0vP8J_Zcciee6bBwJ-UR9Aejgvp0KA061-XAVepM0wWCJKr2DKxVWKdmWe0ko_QsV8bXIVN8u0ruTHNWGqrXNlLxNuzgKPSfCYwaB8MYNb8FiKz8ZNTlRqe8c31wdNzFo4acfhVtSHIBDDGKuUEdz2_tTGydu6lv-ZW5110hwgARCB8SmiK8DFetl-kkjd5E_VbO8Fhw8IoO9BRTh-XBG4cLg_hqTiUlY283KChuXIT7RrceOQF3wL9oIhdzmo6Ehy9PTk-Gxi4jSjNpjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A63Xu4hqFglkJMX-Wbr_2X_UtqZtMIGByrCMRC57fMPG9_qoxJiMse8FhJQucqsLn_gbUxm5bGznpzSlhgy962h2TB-TLDwIOPa0qqQFN1jNZyfF8UN2QOCwlYLceDeSpBHA497HEx_fAGYjh07aQ508nx1n7kH2ImZNXVDLwxC7q3C5CutQlrh4rkpzDoyepXZt1F0manRy8IPx9-IVTcPnbE01EBDdsEk587N1q7xzzGw6ggQw1nly8-vAcKM6j01bGehhtuuBUQ08lNHPROh9fi2pU9IhVROVbSqrrLGIZ8pEs-XF3lwHkPW9Mk66PG8u_XZVIxB1-bR2xh4BLA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=H2dW5Q1ReBijt_PzQfLH54FORgjM2BGh90eSLayvqFBLlux_XSkGHa75sLwN3WsraGxNwcfe7gfm7kg8hmrIFqSdgSw4xCIRCEBmBDYi4EQ_e78oub7IYSCBlcEGCfWFlv4C33a7mMVclUviZxrmpvYzC1GHFaPxLsDCaoK7oPJb6u3GpMD_eHlDaKewWeczplj7xvfvXjGdj1eE6uzGimpOAsm3UTa8sbx01gjl2WICWOuDaPJFxrw5mw2Blg5njpBAmVlHyh0-EFmXwF4KqFHRaFeQ35yrrkJnrg_YZUQEwpWrrpWyhVOzYiFUzbWpLCwFxkXbsLmJG3VXVoFrFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=H2dW5Q1ReBijt_PzQfLH54FORgjM2BGh90eSLayvqFBLlux_XSkGHa75sLwN3WsraGxNwcfe7gfm7kg8hmrIFqSdgSw4xCIRCEBmBDYi4EQ_e78oub7IYSCBlcEGCfWFlv4C33a7mMVclUviZxrmpvYzC1GHFaPxLsDCaoK7oPJb6u3GpMD_eHlDaKewWeczplj7xvfvXjGdj1eE6uzGimpOAsm3UTa8sbx01gjl2WICWOuDaPJFxrw5mw2Blg5njpBAmVlHyh0-EFmXwF4KqFHRaFeQ35yrrkJnrg_YZUQEwpWrrpWyhVOzYiFUzbWpLCwFxkXbsLmJG3VXVoFrFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=sy6RRaI2mgMZBs4UJTUvWYky4ZtNfHUZ1CL6S4dbJ1ssPwb2eiyqoPW2rxSPOq4SBoX0wkBClLXuZq8PO07Q_h1-wcZ4FNNfJUmMNvOKp4FwBbGPs1OY0R4aOn1IED7b22vDoYiiYi07tdvVY6NZmdazyyMGXSZ2nIUS13AvBGQgsdkExOPpi_iJ2MWlXJrq4MGBa3JUVer7GSKPw7xC7i_J1RXtu6Uwgt7JvwOI7N6bxAxDR30MQzfNv6b0ir4PlXEUtjoHv8wFOQqSbAKXLTVQzYJ3FnDBuM_sEMbdmfO6tMEIPvelntsMoQxmbHyIbwSOPHt75dnebRyNJY5J9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=sy6RRaI2mgMZBs4UJTUvWYky4ZtNfHUZ1CL6S4dbJ1ssPwb2eiyqoPW2rxSPOq4SBoX0wkBClLXuZq8PO07Q_h1-wcZ4FNNfJUmMNvOKp4FwBbGPs1OY0R4aOn1IED7b22vDoYiiYi07tdvVY6NZmdazyyMGXSZ2nIUS13AvBGQgsdkExOPpi_iJ2MWlXJrq4MGBa3JUVer7GSKPw7xC7i_J1RXtu6Uwgt7JvwOI7N6bxAxDR30MQzfNv6b0ir4PlXEUtjoHv8wFOQqSbAKXLTVQzYJ3FnDBuM_sEMbdmfO6tMEIPvelntsMoQxmbHyIbwSOPHt75dnebRyNJY5J9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jHXaBekiKsheVWKH0XZ5gmnoS9aFer9LNjeAOnnS-0AhokXEHR2q5E7Ct33sWO2NGdaqJmnXayT2-MqBWin18Ict6a-GlJjrI7vjXEFQYROgUrk9YjN41EImNaxDoEe1zVtRCj53PlFveVq1z7NF20QR-4ri1sj3dt0FH0pflkMxoouIsHDh4CmYg-KxUbIGwTCw1bWMFOUPpyoVZ1oAr5o9AATG9zeHIO28CyEqivEBCyR3x0Ie_daZNZE2NyNtnDgvG35ZDbhYk3Qo8Ctr5va0xQnkayZdwHx2zLeLV7RX-i_lA191Av3nNlrJSZRUTg867NPqvQyolusTkDhEWFYpG4mu_GgdsR-c6kI3bfuofMCaHPc988UYB_eTv4xkJAdSQ77FOzvG9Z2vNHRNKnVuIe2qTnLdp2ijQ_ArhcS5-_gmQUR7rlzhcKNAAQU8yizZATms3KS8REC8TOzdN6Pu-4YOfReUCts7XTiZoOY9FLFQluqO3-co-FQvaxJa84eUK4mCy_BaNg9zHWJm4gUTaeG4xDdDkTi5uTzINdJ1iFO0hQ6BGn7ZokiyulbM54Zztv2yDPE52vezlChJyNUrXZLyu8s3SuDO8gJ23e39OcRPvKp_Px0B8Xt-92O_CbRMzRv-OVLNJzCeTnA3k2SulITXyUp_wlyAIGcKR0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=jHXaBekiKsheVWKH0XZ5gmnoS9aFer9LNjeAOnnS-0AhokXEHR2q5E7Ct33sWO2NGdaqJmnXayT2-MqBWin18Ict6a-GlJjrI7vjXEFQYROgUrk9YjN41EImNaxDoEe1zVtRCj53PlFveVq1z7NF20QR-4ri1sj3dt0FH0pflkMxoouIsHDh4CmYg-KxUbIGwTCw1bWMFOUPpyoVZ1oAr5o9AATG9zeHIO28CyEqivEBCyR3x0Ie_daZNZE2NyNtnDgvG35ZDbhYk3Qo8Ctr5va0xQnkayZdwHx2zLeLV7RX-i_lA191Av3nNlrJSZRUTg867NPqvQyolusTkDhEWFYpG4mu_GgdsR-c6kI3bfuofMCaHPc988UYB_eTv4xkJAdSQ77FOzvG9Z2vNHRNKnVuIe2qTnLdp2ijQ_ArhcS5-_gmQUR7rlzhcKNAAQU8yizZATms3KS8REC8TOzdN6Pu-4YOfReUCts7XTiZoOY9FLFQluqO3-co-FQvaxJa84eUK4mCy_BaNg9zHWJm4gUTaeG4xDdDkTi5uTzINdJ1iFO0hQ6BGn7ZokiyulbM54Zztv2yDPE52vezlChJyNUrXZLyu8s3SuDO8gJ23e39OcRPvKp_Px0B8Xt-92O_CbRMzRv-OVLNJzCeTnA3k2SulITXyUp_wlyAIGcKR0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=sZpPN2KYhF82YAip79mRqgF9ACM8LVxWapj3aAr6KKvrhHHroGZ0C6ndpH_eJfdXQ4s4p4LQhni5jiYfRgQOFrhGW9fYZC1wU8K-6EqnnyIpdXI4w7sriwuxnDhMnKaGLTLs7TuyWVLTSJwuFY2yr3QO1nu-i-mIK7WrtRLj00Xck3O24MV7Hbc-XGYogk7q3GIC-J4z3QdjWtTZNmj7hNMCBmSxssXeF6b_3bSr_eVAgLXDMR_Q5zorR8jqmhs_2cYklM-BfFMhyZTln7RK5DsvNbyggTAq9uFbwYGFV7ud-I3c4oQjM7BWn8nSc0dyoEJg_s6-lHwHu1Pcio_TR0zfLuhtGyHB6faEqso1jkcl9O84udsUqBVgAWGuHnOsWn0fXdJ5-WWh820QYNvOdUe8_-CxrCOxhJNBNhtKoEURBjKXIdmxlW0N62645P_o5An1mvwUSizZSOAy3l0OaHPOvkuW-YdSTPZaHhrEID3aDa-ULJ0AuLSvPxmG0xyjjJ6IsueUwi-OtYKmZUb_QoCwUVftYhEWg5eObFkQJy2pgHXT9GTpw94Dy2ETVQrJWYBb3tAit3VZEJV9UdIeIB0OvrQlwLdF12ms9SIz8lQXPA_ExFBChf68csxVFUeP42i1zvgDttNQaQdxh7xtDzY2HnWWKFBjWsubQRmhfdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=sZpPN2KYhF82YAip79mRqgF9ACM8LVxWapj3aAr6KKvrhHHroGZ0C6ndpH_eJfdXQ4s4p4LQhni5jiYfRgQOFrhGW9fYZC1wU8K-6EqnnyIpdXI4w7sriwuxnDhMnKaGLTLs7TuyWVLTSJwuFY2yr3QO1nu-i-mIK7WrtRLj00Xck3O24MV7Hbc-XGYogk7q3GIC-J4z3QdjWtTZNmj7hNMCBmSxssXeF6b_3bSr_eVAgLXDMR_Q5zorR8jqmhs_2cYklM-BfFMhyZTln7RK5DsvNbyggTAq9uFbwYGFV7ud-I3c4oQjM7BWn8nSc0dyoEJg_s6-lHwHu1Pcio_TR0zfLuhtGyHB6faEqso1jkcl9O84udsUqBVgAWGuHnOsWn0fXdJ5-WWh820QYNvOdUe8_-CxrCOxhJNBNhtKoEURBjKXIdmxlW0N62645P_o5An1mvwUSizZSOAy3l0OaHPOvkuW-YdSTPZaHhrEID3aDa-ULJ0AuLSvPxmG0xyjjJ6IsueUwi-OtYKmZUb_QoCwUVftYhEWg5eObFkQJy2pgHXT9GTpw94Dy2ETVQrJWYBb3tAit3VZEJV9UdIeIB0OvrQlwLdF12ms9SIz8lQXPA_ExFBChf68csxVFUeP42i1zvgDttNQaQdxh7xtDzY2HnWWKFBjWsubQRmhfdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=oXijdKFpUoAeO3wT8nuWsyQOgCTgfsoCxMVJMPIJLKRa8I2K42Lxo_kl5IsyKVpYuy-CHoYIRWLNwsy4wSA3zJ9ZOAtJiKnc-Hl6yokPMdxCHbcbdHY2kS1Jn8Aj7aqQHGDSDkoe_aAiIuiA1zMFQZ6jv8fg96qW5t77qQC4hlGSQf5VkTG6vu8uFZ2WU09OAB7i_FfwoAa71HYeL37bTuySYdbICaF6dtcfl5uqUZBVRDDz3feBGjGH9SfhX-J2cXEMYqz9uK2t8QR4_gPiJUGud-XYdTB0KKBgc0kj7SCMBGGKYiU0lQmkReyOpX1DhLotd_Yy3nb71eLUWyfvjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=oXijdKFpUoAeO3wT8nuWsyQOgCTgfsoCxMVJMPIJLKRa8I2K42Lxo_kl5IsyKVpYuy-CHoYIRWLNwsy4wSA3zJ9ZOAtJiKnc-Hl6yokPMdxCHbcbdHY2kS1Jn8Aj7aqQHGDSDkoe_aAiIuiA1zMFQZ6jv8fg96qW5t77qQC4hlGSQf5VkTG6vu8uFZ2WU09OAB7i_FfwoAa71HYeL37bTuySYdbICaF6dtcfl5uqUZBVRDDz3feBGjGH9SfhX-J2cXEMYqz9uK2t8QR4_gPiJUGud-XYdTB0KKBgc0kj7SCMBGGKYiU0lQmkReyOpX1DhLotd_Yy3nb71eLUWyfvjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC_v6Rn7OlyehNcrsvNiXy_MrMmB3erht6Unscoe6MJL3l4cthN5BAoz-NB_DVXgZ5cxvXDH-wnQhSC0uhiGceh-PTSSJBJBzr6IWatVY_1FaY2FM5AthYgUvDRe4Lny74QuQgYGW5_QHAQpu9p8iemx14H2PuSrN7GBk0FKMkGFFjkxUJvuwYb3cjDP9d5uPyNMVDF8q2ZYSkXjSCfCJX-BZhcRlRjTf75rqgU03m_GX8yiijTqSBVFHAQZ3BrKn7bdFdoqA66WBxI3G6_thpQtFzogT6ycZlD4cT7Q0681i5_bnqO4SjmODPUTOIG1WmE4PwMgxOPZYC043z6o4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=qKa9kgDkhc-1Dd-ytK2SLbjtZIqrBM-VO4msyffZeelFgFKc-bnNua9FkYU0t_wVqeUyFKlfde6OB_jAetI1SBeAFbE0ZtNsefRh-NGFBzXCFesI6jZp649_RXEpKfyU8p_DoA7j-d8fFvqXk2xoORgS9LL2HBNDdrD8NWq8N8U7nzoWR84bmeiqhPCrqWiM__QqLg-hnXrOSJyG-PBM6cz-TKfVMsaZe22cNu6EuS_ZibwtmHUpNzuZHz4vMWvz9nu1mHpHHHGB8gc8w62oR8Sexc0yBpVrYgaGtjgxb_EPHMev7bC69GrEQE0ZLdkSk80nzGXTjtkCIvSoLXZ6cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=qKa9kgDkhc-1Dd-ytK2SLbjtZIqrBM-VO4msyffZeelFgFKc-bnNua9FkYU0t_wVqeUyFKlfde6OB_jAetI1SBeAFbE0ZtNsefRh-NGFBzXCFesI6jZp649_RXEpKfyU8p_DoA7j-d8fFvqXk2xoORgS9LL2HBNDdrD8NWq8N8U7nzoWR84bmeiqhPCrqWiM__QqLg-hnXrOSJyG-PBM6cz-TKfVMsaZe22cNu6EuS_ZibwtmHUpNzuZHz4vMWvz9nu1mHpHHHGB8gc8w62oR8Sexc0yBpVrYgaGtjgxb_EPHMev7bC69GrEQE0ZLdkSk80nzGXTjtkCIvSoLXZ6cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ZaSDVsMiIaIYtUbfxwvuMUqVU3wVm0WGJbpA1NG_FL9Y-g1rkJog2VCR7oX0mUaELZ7zcmkBgN6iZa7qhzHRzpd1THHFw8CS507Bz8VL83Hc2YSO55TVY3igBXhdlGCcgvO2U-cZqYvfUdJZtZZu5PrgNKJwpVrJAGlCbG2L08wslHOlJB-kxO348nNzdMQz1LYoSb4iLxG64YoitycUdNbzz_w2iW9rKq5uvgdEwGqxRcEac1rx4IePqMt_eyljpZz9Vx9jvrbHycfE-jtof9e5_lC_R7fEbAPqkgGEMwlew2yLGshb3VYzuPzYM8EPMssI6MHrndXQ9lou2hMoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ZaSDVsMiIaIYtUbfxwvuMUqVU3wVm0WGJbpA1NG_FL9Y-g1rkJog2VCR7oX0mUaELZ7zcmkBgN6iZa7qhzHRzpd1THHFw8CS507Bz8VL83Hc2YSO55TVY3igBXhdlGCcgvO2U-cZqYvfUdJZtZZu5PrgNKJwpVrJAGlCbG2L08wslHOlJB-kxO348nNzdMQz1LYoSb4iLxG64YoitycUdNbzz_w2iW9rKq5uvgdEwGqxRcEac1rx4IePqMt_eyljpZz9Vx9jvrbHycfE-jtof9e5_lC_R7fEbAPqkgGEMwlew2yLGshb3VYzuPzYM8EPMssI6MHrndXQ9lou2hMoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjjt-iLl4wKogBKI5tEizSvCU30aX541fx0MzmsxR9h_6pfg753qCmvJtlNDb63uNHDlfMJoS6tHR-isXGrkexEXShWoTb8JTyMA_dPqgeVB7CW5IeANFWuPKOoSkMrc8K5E2Ac8SKrFZowTPhEwnP_tPQyyODpncoO2rFKsQLFU4VKjJaC1052mS9J8I5zEUH04l-4M7iOLLKNN9pt7Kl6tELVc0GmnT5cE4y931Ri-tZSXMlLjF5xtL0Odm_fyauvmbQnrGPwFdN0zq1Ihk44NvBYPCsSNDjkiDxmm7hjBDPzZJ5jgkFkKs5KCJ5OC2bQWplwnM50iRxWpFCjmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzgUV8IjoAO445FciFiNz7Qyk-ga0fPbE01i5VxrdVYa4WTsqLtB3uGMRFB10feOFc8dNbgyRCSiftEmaDcavBfVrfIFmqANyzdjV1Ja96xeNq7qECQEnW_DW0vI1nN4BqYpwG--mmhWVyds_VV7ksl-bEoSZQjEB7w-aF8KW6F7Hu-d6M5GUC8KQn4hWAK_s30jWMrxNjJjxtEfwW4pHskn9K7LxZDBKy_gMMxf0bnQmkqU1g7Y48caXDTb55JyQ8x1X8vQ0eQv9dzJOG5McBXcgDJTYCTIut9G-zrEUB7Ipkk30kpGW-BittF901mIUJWQmyqG8OZrYiYdVcHcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqGscrJwKYH4kfMIlsCobftBOoB1KsVcKwVm2ztiB7zfSCchVfOa4rUsM3PmH46W_UXPiP8wh2A3X7sm_Q6CqX7JTIU5pd60fitqKovPATInsq2Q0W3fdZN5x2t34yO8U1OLCjbVcGRhEbWT9iRoqNAflfgnPp_HEbFl44AmWwdnlBKqqRqKfHu8h_dnL1FpH0YnT7QDrVzIvn4joDIGmi9zR-EuxEDV1tl8vwpxfNTyNBlgS7sAPXmSWAb-YzBVnAtZy9vrpZjZgWvXQnT14-xvTE6LRKZm5tcmyiTbd51OxNRDiTjaXXezNd7WGEu6FIGByI_svBUmtWu6RoH1uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDjC1U5zQ3D38qA1pHv7mNQzk448nb4NkJwwEw6bnOd9Gs8lhgIn2Stee7likDdk_-Ih2iFOQs8b1-6RPVJWoFxHe_dKl3f7RkLGC0TWUeKv-4zhvGbi9DsO7NFB8Y2zWpVbXBfEJ-r3F6Z4NaoFjhbj21GgNdV4rAYuaQb9qLu6gYRj3yXt9PpVPwM9LQBuv8-gvm_9-AdIVX8NWAmYCE4RVjlqC4Fd7GSNafY0TsVIuBO4JYsCb1E8t7HzSwUaKTiwtgjkL24OF0rrNtxIyWLGV7odAd3Yp_duz_72zLluCWm-RQrm8Na339_AHs4aBcciZyM6m4s7LK-BYRMz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU4ykqU38M8Qa68OIrsMW7fRHqLGQQxnBGPNtxfoMExgdNZQJDs2R7wk0SIPX0I54bKjVrW7Cg59m21QTQD0fLM08fdPpGjPQPs46o9NL-pucIrVkTCMVFTePnShtjr4XaqWISzuJVHohC49Haj1NQci8VDwyUG9Z633tAql4IeB3AeiBC3bmnGC4g9NhCm3hkkTPvNrlGb-FaUJ3cSyUnVs1N_oCU2T26IwZ1ajEyYRTTKkRTZv-3yLRkFXdGruKG62eJqJwrUMw5IIOdUUCXRv20gwmKLlXk7ltQ5Vw3oB4tLqxhbIEUU7-L-Gwl1Hlg50OsXfwAd4sWCBYULZWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWv5gqt_p5rR4te2JC95t62uHtd0qJGBY6wjx4HQy7nhHGLFVhd1g-9C0A62oxCEDXer4I5AzpTnY6Y5Zphxv8GRkr3VYK9xvR57l-a4aUXaEDzD-UmvFQTg-kjf2-TXeuU3ZogO2NYar3zVr1C408Aubi2NRTuQaq3ZMTVQQw5Jn6QHJM-IhLjXNgYrUJVqPxoVn67AtXekcrEVbRUav_06UtguxgLZwpe1JeWQcIy8ogcZ7qeBFGIe3_z3tzxcpEjV8M7DKoE6uV__8rRUyuNQ6-MBZ52SDCyx9K3T0mgCQJ5MlCGSTWKByPSmdkYuVE_NUhY8R6bcangIKjT5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTWTDpxFfe8tM0W_dL4S0tqK6xvWGo7fLQDkMf1cjZNQO0rbncaRgBMmuqYEQE6la1CU0tCZ1jAmCkSnkFsJSq5_d6A__W-pDnNUjCtB7kUtTkoA1DID-nW26VGT1zamSzxIipdWEECDzkG9gfe0GzrHtDLwLPklGopn3NlbCZ2ydTAfYQxNcLWQLLXgWU4_H71S51DgJZ_XmOSzb2Nu1tIdroHZCX6hGr9aTJc4LTLOz3PfnGYxzztQY2nGEHCuv-R3B0277nCm6Cpkq9LemUvPF8pOw-Qb8clkfw2dT43UwZCrAneimrwDu3hVtpPij62e3WyvUReCH1-nfd-23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4HTtPpOhfHINMtYMXWmM48fvZMUPkoKYrrDh65R7JUZdgowcoWIjn5wJEncRZzkPTTEn-5gWeTNzu_f7f6pLXG-QQH_-3fUUkl-giho-6I14ygQ8HmffJMUmSKJQVGqG9AaIGW1qSnoSvRAqrRe99f__BCsL-sCPru6K6tkmVMOG_5eEWPhqbnW3cFrck5IL7sm2Gs0RUPKojq-vdZvgWHg877fumTviiYCL4EH51HwUpppFQTMglRspzrxDbkTNEHC9df8W2E13wR-2sAEqhJ_qnJDcD7K-FkubY_o76dm5Zi3gJJmLYEf7oAug41Eof0t3OblWeFzJXDDE7bj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9zuJCEgDib5Sq3muYGeM1EwGg-nX_GV18592j84PpBsvYoYlhlODE18jnsTkY2w15jBX-YqcRYq8aTH6AHat6e6wX_U06d1lAzrsCvfkYJkbx-ur7rg1K6W1DFHoTkG2frJToRa9weB5tdEPchXzOi6hqfgi0mXB9ewl7S_y9zJX8Xz4259BkDF6OK2YWupCo-pyG-6EoJkvxmbmcFs7l-jl7xbt-jb3cok6yHLVEyyvqcBK5Mb_PJyRvrcbQV-6ozIW7x-TKRGeDJSinLPK7h6ZM9N0kvMDKyawZ4Wgbselll6VALjCpgOw66_PTTYVxj7GvqtspA4wMy192gJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZnhk3wQAWdABanGe4yQUdpkVick25NJe3VwVkJwpb_nUYbuchDx-sWkUq1F-7oK0I92Xte_eb8fM8J7i2nbvxTCRlFs8UQKsA7PlWVakkg6p4VvA6mFW_luuoP1UgRODD4k427MVpUWKgPX0BRtiEY4fI_vboUF5gpZjTFUZTGTmnRrguYoadjf6kgth8rLuVnvpKAYReLL-Au-pE9qyu9vnKzJPd2ZexKgl33jEWC-ULz1l-7hHJCS4SByp_s494lvCBnZ73SYSq3a1aikSQo_51Bk2z5NIC6QH3969ZIKpVCCoDvV64aztIUvzoFPWhEU8KR46YSZHaMBsGwhIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=G5i0to5ZnWe4QOtJ2Vqb8KRmT-2fNzRUtBQXGaw21c9Q3lFCr23cjVFc8B6B3DgZYBvDfy76c6M3R1IQS-K3AsoBLETznJ8eGouqkuTQYpY_cvLXxF1cAzZyr3i_DGRuLaIl5mZZiXpo8Qqg0omEJK_65MDDPTC_lHi8W5s2N2QLbAQ9AfPossOCkZzB7FmLDnyz2oM3AIOqhOIBvT31dE6QBuR2xFVYC1-ZF7zeiwcNxGe6GHDW4qnLJ9st0ENqG-oJZLavd3ezlYD6n7MjhTRE0H3expucYqkP5pmGnApRhYb4iHjtT958FufLfv5UV3dkjFljkvlOr9l5z1z8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=G5i0to5ZnWe4QOtJ2Vqb8KRmT-2fNzRUtBQXGaw21c9Q3lFCr23cjVFc8B6B3DgZYBvDfy76c6M3R1IQS-K3AsoBLETznJ8eGouqkuTQYpY_cvLXxF1cAzZyr3i_DGRuLaIl5mZZiXpo8Qqg0omEJK_65MDDPTC_lHi8W5s2N2QLbAQ9AfPossOCkZzB7FmLDnyz2oM3AIOqhOIBvT31dE6QBuR2xFVYC1-ZF7zeiwcNxGe6GHDW4qnLJ9st0ENqG-oJZLavd3ezlYD6n7MjhTRE0H3expucYqkP5pmGnApRhYb4iHjtT958FufLfv5UV3dkjFljkvlOr9l5z1z8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0bSKjqbxTMBZxnBoCGyGvLzaCXbvDH1mMsnCbY_gYSzG8pATzOHVwszPgN1w6TikEsxxOkoWXNkBv-lorNq9JBDriOsA5sCOtvNii4D2VYyKOohDtm5O4R0goJBs2i9smmeAqkrjFb9_pLAi9SKGn0OY7XUhqs2RX6o3qBLYf3B1edlUDowrEOzasgLjFqfU9V306TQLbjjv5lZM3wNIiOjXGCcgg8X8nq1KL8AL171bM67Dpb9_DbZ5rTyNvFFRFKjldksof1DYaZY27VS4m1CdAblGAFb7r7q-GyUfb86HqZn4wTD64I_8L4d4qjtcu8AlImYk-5j6QRXNDTqbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQuTLG6PiVzAVNUra96MqKeHKD_GF5rdkujBtOZXAOCeOijw_BNkOBGq5TEfNlqxYLUr4JXBMI0h1xBJVGi8cGTRcBgFITgQPJhfnif8OAUxPf9oOhDIN4nMFsn_IF7pqSvheZOyt0MH-pcUQm5I8qGFWP40DSZYosR1CCCLVgcWb4GG3NIHf6ii9q8E8UxvwoVH73Wz82Oi_Kss0UcGMfbp_iml1oU52ZNhJsVD7S_9f5_mrr_qsISwG-9tU9g_ejvP8Sij2uwkPRk_loGUMfotdZAHJPsblLK5C5k8Jx6HjRsqJan4zgtiVJZ95MhSR4LfjGeXAXgYEaUGdXMv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=YHL8IGGPxS8v9gvfNN13Ne1Xv4Q3QGd2FdTQ_9BoYneb-rlEXOivhRz_TL8onGRO4r2aRg8xBaTwX3D1dyQOQ_IB9szCHr86iAvfqyX_E1uVm-7fUm4QkCpQtJQZnLw51nCDiBg5kIa-sWWFqPoNfKBVjpCl4rtV6IpoBgvbjk6MtjW7W6NX_rK3g-Q0LUwwcfU7T6BsUe2nJaCk2xztpo7zneTig8E34-HJHKvzZ6tiBhRwfQ8BENZhcJEj_B3uleva2KmjR38RzHzurRq911NJyQqfVNM_DEtNWfwOdMggSsExkKYVhC9s-_m-6PAMQ7gLyYcmdkYd8dSbm89SVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=YHL8IGGPxS8v9gvfNN13Ne1Xv4Q3QGd2FdTQ_9BoYneb-rlEXOivhRz_TL8onGRO4r2aRg8xBaTwX3D1dyQOQ_IB9szCHr86iAvfqyX_E1uVm-7fUm4QkCpQtJQZnLw51nCDiBg5kIa-sWWFqPoNfKBVjpCl4rtV6IpoBgvbjk6MtjW7W6NX_rK3g-Q0LUwwcfU7T6BsUe2nJaCk2xztpo7zneTig8E34-HJHKvzZ6tiBhRwfQ8BENZhcJEj_B3uleva2KmjR38RzHzurRq911NJyQqfVNM_DEtNWfwOdMggSsExkKYVhC9s-_m-6PAMQ7gLyYcmdkYd8dSbm89SVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=aUtZ0aWj7OqAeCz9fe9up4c2ziSW6u5Uzbh00AyK7TcNFBNN9FuAH8Lgy0u6Kmy-iMw5ZHToE4Rvwjdmjn-ibXv1Cybv9BY7dXTh0okfGv6XXV5prvNMScE7izZho4Kt10kcbmNGmHnZN-oPhsZIQiHfcmoPqbiK7Cd4O2pKV4ogkEmfNjN_LGff30tHlEOpEyQTZTMo3c1awnhTv1AuTFtzkB4JN60k38f82IsWRlVXSJNr-b9xL_NMiX-h1J_xKCdy3eJV7O1JQAhewijB1BBjkFq6qQk-MaiNq0WnFHMwr8VIGHMIK_1SyDtoVKfaVBxYCS9EBZFeQRP6RsLjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=aUtZ0aWj7OqAeCz9fe9up4c2ziSW6u5Uzbh00AyK7TcNFBNN9FuAH8Lgy0u6Kmy-iMw5ZHToE4Rvwjdmjn-ibXv1Cybv9BY7dXTh0okfGv6XXV5prvNMScE7izZho4Kt10kcbmNGmHnZN-oPhsZIQiHfcmoPqbiK7Cd4O2pKV4ogkEmfNjN_LGff30tHlEOpEyQTZTMo3c1awnhTv1AuTFtzkB4JN60k38f82IsWRlVXSJNr-b9xL_NMiX-h1J_xKCdy3eJV7O1JQAhewijB1BBjkFq6qQk-MaiNq0WnFHMwr8VIGHMIK_1SyDtoVKfaVBxYCS9EBZFeQRP6RsLjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM0VArOdkVuu_kuHojH4As-JpN7BWGh6NFNRDrwVvJn4_xErF8ZAA5HXXiX5l4JTHeTRGJZF0PAX-S6jHWxo1Nm7_wWAFEJQpPzZ7Zf6l_nYGcpcJnICAQxhiUaMrYOzxXCpffKAntFNnkd3dMN1DlddfcEgISe9fL7kmA-pUHQh9I66f5cvJacAOmMqP-Wx3iGNvTvrCDRt8JyHmTwRCowLrLK1D9D9lB_AGC6VKHHggHzBogf9IUh8lWYcvRpMwjigvdNOhSDw7rsf65lljRh4Dy9DP53T1JwlYtoZ24sEvSqsdKGSIuKhYInI4r4h0MuQaj34_RmBEIoCYOc6zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7H1Zo-5PP7idB9eBEub8RHHZ_p5GK-MTlX_oqHFPzLYHyw687GMKBy4fVi9WA6wfr6XfwFXA7ZTkuOpLxcdJhP6qe43r_eG-UXW5mdlXmYmsRPxVLJfWEdN_LaBvhv2J-gE0qrUSVhtpKdxDVTkqB8r0DPXBuwY6FxiuFswAALfU6--X64KAmyqy9iQQP5y1oOdwKS4gvoa1bi6uVX8uS6Lq3H_gJrdsr2T5iJaFfFzl_ON4dnlF2oQgNXyer413wd1yajzmxM-FaoVNxj3dhwuukt5aWc7zAORkFoHPZ5epbLw5bQfekhABvTNcTRmhhOiTTAIrmBlrh3MIcWP5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTNy29goCZ6LtJZr7UgEKcWoLHgr08Dl3wHVDdPB5P2eRi4t9bRpTORrJK31_cn2INY5T2JzogyoPfFuSG7yZWomr40Dwm_fBwnuj8LIjkFP028JUSjDv6zP_Z2Usu3rhce1aNX2PKXWy2aWwhrkf6iq2yGRrlhvWxEsmfnIHbStZH1czzT3n5YbfaP71u2qqgKCfFAYFJCYByz5V6xnGy_VX1cwiUxoXF5boU7TjicILipYBtklrrQ1gvT4pRqQpnI4mlAoI_Nm84-dzWqIDYDGUFAkt1WcSwCWRJLqQIfhkWFkBGPo9fZSPw9Gk74IrEHHkb7XxDWGZTAJ8kfWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp1xTeFFvjCsAwACdVTLrL38H2chYh12DWJ2A164iByDsjRE_OaHpvTFVAepo9uHbcvILT38WQP9KDER66puQpOWG52NliJc4BkgbL93X54Auo7JeQkyyWnNSLSMw_eu5cDIxkOCPiq8YK0atxWuQMYzMPVSdWK_YB0-Po-4Ke9xFeVYLc4OvL_tN_PjhlhUnd25jj8mAuiP3mBw1Rf0c1IsajBVZbje1dkpoagIcoKuy3xvHELaWfoW9PW-CauHwus5SJ5mCe6W-tV6SgvcxzS_OHvgsxvdvVKfik3b8qabGDZ53Z120Mhep8w_XBY2Wzw0IMeCjOGVd3BUnYkkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXEgjEL_4khRCPpXolJuw_z0opTZEz-A1hQBczmHWpZjskMfZdM8dbK9_p4wmUj8puNN4Vyc9nK3P8-gJ4tK4VyDtrbQmb8xKNJJwOS4d-H-KCl5PHj0GTg9oMs5DwXNpL3PeHwMfWLZC0QWwYlw-CSZl1VIbxEbq2liVmPWfqys3UYqcQgN_MHKzM-fdh1Zx_B8osR37u0bI2n8HakkrFQg1C4TK-B8a7Fsm7-3jVa-FKN1du_UdvS9l_VBKKPlGfegCxWYsVRO7vtFrTjbPATlyx7YULLU5ojCKGuH15gfCRFqEgNYR9d_4BIkujmRjL6D0YS7l_8FCjd5O9IHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDVqiHOBB1MTuzx9d_YkjdHfcQqZkGvCIUdE-54I4S5pn-kEsn_p_jlCK-8Kij4c3IIJKSM0Tf22Oj9B4xjb4rTtA0ESMGw5aoEYO21T_uCm5S4P3P07SgnfavjfPmRTh0IVPY5gGQ97md32048bZXkbLPF59p6mSueO6rFgtyaZwi-1QIPRKQeHAnEjmn76Pih6sZlChjL-OVxIUCZr2_pQ8mfX9lT1Vti3umIfeyATKXZkfTCw0tHHTqpHc_r3GzMLxJQ1-kfKITXuZ1co44Y8yaTR9t_DKTWk6ASwe0_1toBeqW1CAm_tjDYyubVh9sMVAqmKqB-_uO0c1wFo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMJjohU0pso--xN9kUwJ738jDMvAUkxiIy3C9Xlp4qlh8_0vHDHun4vT4W4QbjbYiOW1Te3Mh7PgZ1InnYoaebx48LzUoiyy8k2O6W0RVLfytFiIfaxuseR_pbM3gCBRxdy1ZcQ1pDWf83-S_ms3O_Ac6mdOHZyTJ5EyLyFfuQf3nVwWJ3lIUjqQM_4mSq1NyjmyTCiaYobuOl0VE70314YLKIw57eT4KB2Aoxt02kiLIjVZxJlx_akUJOV3wY3V2PIQbtsNaiikZkd_FGxqp6rGToof18SRu2Or0DdXpp-kQGsn8OMWWjO0KvYfFUfVetj_r5MS2lwQAVL5QrMazg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=USBp3rmm4avCl70PWXwBbGK0DxjR9nu1Xs__0VQOkp0T-HmPWQP95NQjYk9-WDMjOsm1-O1psKj7lgxG2ksYoZajpVyFNX9WIHK7b8N4eQPExOigmW3UA6NwoK2X-dVgwU3PJeTj_Kh8ZUEFFZZMHqDLrfGGoetjPKOXj0RBD_KdpNkASrOI1cpAhP0gqccZZHOr9X5lpXkPmBVusX-YDbQui09Cc43yCC2yV09xBcploFh160gsFAc4rflh5quyXsCr6880grpNtyhcp-y3ugCuF73IdU0CUfifuARHDXRx9zln3X2FMgM6Fg9pRBEjRFewmXHk64uh0GEBgRWqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=USBp3rmm4avCl70PWXwBbGK0DxjR9nu1Xs__0VQOkp0T-HmPWQP95NQjYk9-WDMjOsm1-O1psKj7lgxG2ksYoZajpVyFNX9WIHK7b8N4eQPExOigmW3UA6NwoK2X-dVgwU3PJeTj_Kh8ZUEFFZZMHqDLrfGGoetjPKOXj0RBD_KdpNkASrOI1cpAhP0gqccZZHOr9X5lpXkPmBVusX-YDbQui09Cc43yCC2yV09xBcploFh160gsFAc4rflh5quyXsCr6880grpNtyhcp-y3ugCuF73IdU0CUfifuARHDXRx9zln3X2FMgM6Fg9pRBEjRFewmXHk64uh0GEBgRWqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAJWquVwp-pKuwPMXz5iKTlv1cNHETYN5SQr7Zsg92D73yN7x7jHtjIrB0fEpEhhIbXBzlKrVejdx2hrR7n_ieMRAiKTbZ8XnUWBsB_WS5RkIeTmls2oapNwlMnvAMcNl1Got9-YHTW85FU8Lynsl59yTUuMjmJsJSMK1rVmDD5621TMYE2naiSj6DTs8ES3R3uiZvWo3QHiSRm5j0rZnjLSqZVRQQbkz5Ogh1DjUjX86x4UBtahzcAhxmkjtWtQMQ5QKykLboeYs5_sksBIbdkidM7tncLB2gDKDNrjkmtFp4-I5i4d4YHSkZ0sKvNig1aOrIRi8suSY89LRO7RJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=vGa0wzKl9qOdgVtKNrzSbdMaO8dyNyRFgRtVdmOvU7cy2qrAKYYmeHTNNkP-_ocQsuOHZHVSxH5UVwwhlYSTFPkyZeONpfFD5SqVFc4kyWC8EnLXvPRQcLprE2jRisvgCW_vPhuUZr-8UOUee4hfBqS3lc__fi0G2E9vHj-FxsJ2pzzFjnc7OLW4FHTlpLcKrLU072-14FiCAXt4o0uWyQAyJDLiI31-bET1o9-kSj6_W5oqZ9KSbIT4ioJ0HRUJBQfJclfWd_qa-t9l2PVbmIJzwNDrSSqHtOzRem4cCG3V3iVJswF2nOFyPOSGKOJED35jss1BqBC8zbAQ_kfukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=vGa0wzKl9qOdgVtKNrzSbdMaO8dyNyRFgRtVdmOvU7cy2qrAKYYmeHTNNkP-_ocQsuOHZHVSxH5UVwwhlYSTFPkyZeONpfFD5SqVFc4kyWC8EnLXvPRQcLprE2jRisvgCW_vPhuUZr-8UOUee4hfBqS3lc__fi0G2E9vHj-FxsJ2pzzFjnc7OLW4FHTlpLcKrLU072-14FiCAXt4o0uWyQAyJDLiI31-bET1o9-kSj6_W5oqZ9KSbIT4ioJ0HRUJBQfJclfWd_qa-t9l2PVbmIJzwNDrSSqHtOzRem4cCG3V3iVJswF2nOFyPOSGKOJED35jss1BqBC8zbAQ_kfukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=hPydA4rBHeCCvjDRGcJYm6Mp8dwNWgP97-4FpummzqYiSrHyAjKIKmpjMwzfB8PfRZ5oKHkG1XkPxI9ntkEjHZACE3PDsVr7PkTMwje3m2wTwfIqPsyTqHXHj7oaZTb07hoB-X_I7q4EbV8ckebGiyrIX_v_LL3aeo_-Wixa4NPXw-zTdHeZE_tvys2NW231FDFlJBF7EGCQHJtre27dAjh4LBfXep3ghOfNiTLAjn17pievJd5M7UiS7E0eKDcuya9RWZutYMuln40fMvKr-leZprcCdvEdoBmvjheRycNQD-olFfL7I_nxXaIsEt16p6duBmUa5JW-SUhSOIOsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=hPydA4rBHeCCvjDRGcJYm6Mp8dwNWgP97-4FpummzqYiSrHyAjKIKmpjMwzfB8PfRZ5oKHkG1XkPxI9ntkEjHZACE3PDsVr7PkTMwje3m2wTwfIqPsyTqHXHj7oaZTb07hoB-X_I7q4EbV8ckebGiyrIX_v_LL3aeo_-Wixa4NPXw-zTdHeZE_tvys2NW231FDFlJBF7EGCQHJtre27dAjh4LBfXep3ghOfNiTLAjn17pievJd5M7UiS7E0eKDcuya9RWZutYMuln40fMvKr-leZprcCdvEdoBmvjheRycNQD-olFfL7I_nxXaIsEt16p6duBmUa5JW-SUhSOIOsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgjcO9O4WwSja0wDYOs8FwDJnxVDRXalZiW-1QfLdxcRGUtjjCBXIc22KGCPU0SHgA7tv4W8SNc0kR_hw6b7_AeIGr1tnBLKW4Fs2XCcumB5ABT1jkIbO2LyAcmclhFsmtJt_9TdBWryvJxk3V9HcPJBYS0U3OKGMKTXX8O83IqHbmLwW73zvwML0hYNIehf8HLYp0V0jyyI_g35yBpMN3-agsj4cncV9LXadC-v1d1AfbQDa1cLjHNpVxUbtckR9VMg8dMj_ZTf9eYCelxTcBl6Yoj-mw7giHMVBnEe0dwX1EtVnLNEfvsZjdvk-7kU6DqcPLUvOcMLfKWQkKuyeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InyH-zHJKJb_Re_a9_IYwFYsUPyTrFas5aXMkS3cYpvHeuNqew-KtDNzyTO1xq5EmdcMKklMa-XuGTqqAPm8QFE-rxl_RKTIO0Q0F6AJEZ8NxJVuQgqnb-pVtVYkjHUyVzBiirkNIPIQnb1eyRM-1yObgXo36gtfGwA0FJbavUejmnbwdipidjHZyLBzcS47xAtmhIcQjEMgzf390Eb6magJBCKGG9TtAyHCNVUqXRTwfORTh4LfbktrC9N67AZtvuSQFazUAbvDl1Dub9lxpiK15RzmwBjBw_2Xqc1LoQc-uOH0oixbxx91sD6c-tfGQlRsS60o5rEyFeqT81vi-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=oCMyUW2a1qKu8HfzEbXKsFW2WN4snDdvdVaE6dhUQvT6c14EzmOS6QZ91KliTbd9D4bPzh7UkQZY0ekHjktm7IrPalt59xIZCMJzf2HNWC8FTu1cyhtdjrFt5n41L6VQc2JLlQ5QQ3LL7YQ0vbGkBo87RF1ylvYfM80PjHiLagIpNAuaF00SfG3_sXAsGO7ZgYLAeZLe59iu8pF-mOWkTgLWOL0vk0XpFxORgqy3n7HGyl88YBZiTgBrfqrmbMmf5kBFo547Xh8qZhP6TYIIYJUS8c5BFZ2Xq0H09H5xKaaOAyKHp1qtUlYwjIfEGEm2rfBcCP6fUkIBAh8Y_qEy6IXj-CehtnaRdYvojj7QWdA-TxxBuQ3Po9W-2VN8EHIorAbMjCoNI1mJLPROTMBsZUG_2unvPLKZVzitG_-7YmRfLaqfQGfzO5yoXr4jD8X8CYIrqX56E74Z4wfDmJ1ScNSsmzeNlpY5AL2_lmfB6e2aXUnP5_t8g_o4FAFe-OUN-8l5XCs-xniLwaFwi7XvsBVqFM43rvhvbBvYny5bNWuBO0mHcN4e3OACS0MYWLROLqs_l_asLX1LU5BBqVsy7_wYr1-OaW129-0X_EreOjoYL1bhA2lslCAgMjw-AKRLlgYlPjexMIk4oZN6cbOBdSFtwhQVJ2TKAv5RxFM2jVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=oCMyUW2a1qKu8HfzEbXKsFW2WN4snDdvdVaE6dhUQvT6c14EzmOS6QZ91KliTbd9D4bPzh7UkQZY0ekHjktm7IrPalt59xIZCMJzf2HNWC8FTu1cyhtdjrFt5n41L6VQc2JLlQ5QQ3LL7YQ0vbGkBo87RF1ylvYfM80PjHiLagIpNAuaF00SfG3_sXAsGO7ZgYLAeZLe59iu8pF-mOWkTgLWOL0vk0XpFxORgqy3n7HGyl88YBZiTgBrfqrmbMmf5kBFo547Xh8qZhP6TYIIYJUS8c5BFZ2Xq0H09H5xKaaOAyKHp1qtUlYwjIfEGEm2rfBcCP6fUkIBAh8Y_qEy6IXj-CehtnaRdYvojj7QWdA-TxxBuQ3Po9W-2VN8EHIorAbMjCoNI1mJLPROTMBsZUG_2unvPLKZVzitG_-7YmRfLaqfQGfzO5yoXr4jD8X8CYIrqX56E74Z4wfDmJ1ScNSsmzeNlpY5AL2_lmfB6e2aXUnP5_t8g_o4FAFe-OUN-8l5XCs-xniLwaFwi7XvsBVqFM43rvhvbBvYny5bNWuBO0mHcN4e3OACS0MYWLROLqs_l_asLX1LU5BBqVsy7_wYr1-OaW129-0X_EreOjoYL1bhA2lslCAgMjw-AKRLlgYlPjexMIk4oZN6cbOBdSFtwhQVJ2TKAv5RxFM2jVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRmmNiob624xFoUn_F1E5UFmfOeuwzdc1AVmy6fRexJLXcSzpas--LvkPsTFM81XNXawAVMm0PsSoGLMSpbFHyWd-xxxMJL3lkqt5M1wJM8ionH3ZJGIcmhMQRgFsDJhboJm7KM2j4XOy5C3Wbgo1RSoDw9OZigX0CEJ0j5xd-QEzf1WzBL1AMozZKbOEV7p01qe1yZz0D5U7ln9oZu0_mkNfFsYjxF0ouXpSizOBrQPNkdU3PQ4V5QYGFK8KNSb6f1fa9c0KPdFRXSVQlKfJHlvsOkWrnOLPtJIBGO3_S1vT6BWX5lARgeQgPryrXss8IVB0aeAi9zdCym61o82JA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=r8Qg3tzo_siH7E01N8nO-nFKFLNtpRmDE5fxEYLp6OXtHPbxtV8cw3HSn7vPOm9zyMCW_A8Qd0UYacJPJx0dYapBZl7Yv62RDLzGWzr3fXDPG7jxq--_vizL1H3MZV5s_t7WE080LWVBo_AUAdvj6lpjh0LZotKHJ_QzCKAVXONbUo9406QYreGtULeQ5M0p68DMUCH-KxcB2mAxXwhoHXWBRSEhdVUdHgB66lcjLxnjUC3XyBOuRgYEfaOKGjwyGAUCnDbWRUnKWHyT7jDFZDwgl60Z72Hb312TBzl0AHwhAJzi_Pww4XsXMp4VJ7bSFeCfGimNnMKRnK7xH5i9viOkJiXZCk-jcdLyyIjdMfvlBuZJbOilsZZnSCyz5RXiBhqxwCO2iBxMdvneIECIjED4WTZAgahrMqjEkSW1-_LI9yiARdoT6uIpaIrSVzWpxSXnlYCnqIjbMHBt6sELCcxUgkqjpD9Vhhe6dOxlZDWuqidm-LeunfVSq7s7MUrAbJUh4tNSr1_bJyv2Tyg0XrKQG-z5MBhJmpx4jMAPRhDZ1vU0NlDdVKjCQd3h5lh0TSTHpQk3AS-ONAo6dZKTv8VdY8_1yG0z2xES43GmAW2_9bMPPAd05Q2FzDy4C_ohc-AW0z6yAH4fhq8_0iyVy5HQ07AHu7FQ52-tn1STIyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=r8Qg3tzo_siH7E01N8nO-nFKFLNtpRmDE5fxEYLp6OXtHPbxtV8cw3HSn7vPOm9zyMCW_A8Qd0UYacJPJx0dYapBZl7Yv62RDLzGWzr3fXDPG7jxq--_vizL1H3MZV5s_t7WE080LWVBo_AUAdvj6lpjh0LZotKHJ_QzCKAVXONbUo9406QYreGtULeQ5M0p68DMUCH-KxcB2mAxXwhoHXWBRSEhdVUdHgB66lcjLxnjUC3XyBOuRgYEfaOKGjwyGAUCnDbWRUnKWHyT7jDFZDwgl60Z72Hb312TBzl0AHwhAJzi_Pww4XsXMp4VJ7bSFeCfGimNnMKRnK7xH5i9viOkJiXZCk-jcdLyyIjdMfvlBuZJbOilsZZnSCyz5RXiBhqxwCO2iBxMdvneIECIjED4WTZAgahrMqjEkSW1-_LI9yiARdoT6uIpaIrSVzWpxSXnlYCnqIjbMHBt6sELCcxUgkqjpD9Vhhe6dOxlZDWuqidm-LeunfVSq7s7MUrAbJUh4tNSr1_bJyv2Tyg0XrKQG-z5MBhJmpx4jMAPRhDZ1vU0NlDdVKjCQd3h5lh0TSTHpQk3AS-ONAo6dZKTv8VdY8_1yG0z2xES43GmAW2_9bMPPAd05Q2FzDy4C_ohc-AW0z6yAH4fhq8_0iyVy5HQ07AHu7FQ52-tn1STIyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CylfPYdQkoIgcxd-OhafeFDjBies4TJvSOO-dbCCa5KBV-Xax3U1JQBA6s9FAegwY4jKrUwfCf5cDngMBXvpOTEsNE7guVsc0J-mvFY8buYf-TZwLKSzEn3lBxC3oXxhqSmFY7sVxF3w9SEcABCis5IDYL4zlowY8b7uStnMjt-vl9Am5lYWU50uNuKyY-PMbxEHotn_7pZyc4smfjN3pp2Ya-MOC731oEQ0azyZZigGmamUUeoFlIzYALzFqkxzowPz2MFabZsJrz59xQihALuKmvqlDZfmCEOQMD1Rt1BgX1H_L5v9N-fOqgG1xALkM0LpnWx03Bq7MGvnEbnL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbrKRs9eegbi-Qbx7_fqh7C2c0JeWw2QrWs8TcLf4lkdCPW-ReDSOcCDPRMvPQZd1LbWFqCRp_n2pi60L2YLdQAjpzSvGr-HXOi2JD4kuiAi5l6gJNp9U-UOKo-mW52njNT_cwB8sHKI0sCRRHDyRfGDYA0yrE6i5MaxfUgk-i210-rTPsALOnmcp86in7DFXp0FNWJTfsLb49vqJvdxiverz72dCsIbPd5R_eyzLJUtSMaemmOBbm-RXCVc8NfBNOKQ8duW0lBs9lhS58AEmD7nzvbwCLj6NA6gjTNqLpsxvrJc_rusX7xSKbu2sVCL3jiC0Psc9DbfsLaqTunF4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4O4XcT04p8ft9nzqCehRB9BlaxL2kZ4GuW_RedCOlx4RslFxHM_F42LK7_6NFNDvx9qTI0lfumDP77LYHyHv6rPmsB-ri7hGN3boz66cyAkTIXncWu_aQlQN0DntXdIY9wtmZtrG1nzDnzUR6bWGyYbdyHdC8uTYsEfoQxWbyTxavZpgxScMo8c4e3zFC50Srli6JT5ncGChJ_P-MXZbNNDY-MrcM_1yWGrlYyE0NFhyxYvxT2OoCwqHUGRml0lC7wsXSn3YnXZvcJQfMK3vAWTI6k5Cc5S1Frqg56u0RaJhASpB7gbwuYkAw2J7QnfISKbbMp1l2pnveVegOrZuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtceI4LbMcWZb0znMwAMSMbBVa0IC8FgO2e4EFGzYdENvXcphJWCNYRLaobGmmWbH_X8lIO9RQdzqzwtsfRnWuwS2iboQNIISX5Wwg1SPPRBpqKbw3XlSGqJ-vOH1AVob_jKzwOI6tKVOElBP8gcwd6b7mHFWjEJw4edNlGzHZ9g31Uswlao0RfqE54Jlo2cJc8e0CVQXbgouaPCkxnIJ30otz2YsaJZ3R2jnaJ3Ruy6qHpro1uKiJFhw70gNvCGF7bQlDXTOo2m0EcWJtfAfBSHLjGJtZ-CZBw8ola_mXYtcfqbGy1se3Gm6vOj8s0TW8O3geTfJGipeiaI2YSkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouT4y_RCq8q_LlR4eUM7JU2b9A9nwraSEe-j0B5xwGisb3GtpyZVqIK3Spk71gZKbd16eQoUIcCnbgd36DZ1V7itqKMPhCwhDskhOg80glaUrghkO62qPgZNWI7YgrgKeuGjU63FTOjdGT03BmKvXIvtfimySO-rm8QdEbuuGT4vT1ijoWiWe3bhR_-AXoqcJFWCvpSk0K9mT-qesG6OCkOcOkPiTiMouOit--ZotPkA-b6_YQeItDiKpNxcjI-cbM1gSpseLniIm3plWrnZMWzEff3yGnwEaxdyxW4DA2YTuhaSdLZr0fMpx107Zlkm3sYsBJ90AHxEJbynEUx-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
