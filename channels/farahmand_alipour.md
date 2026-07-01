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
<img src="https://cdn4.telesco.pe/file/L6eANzg5E2ope30iE-H-ULCvd7G7wVWIzTloBYNqXcmq7zn-BobyVwCd0ZwAclmZtL_4gOq305cOK_MNfXllWc9Ghw-N5A-7QcSViJlWV32TqHyeaEgq8bzSO_VEmRmyYqaAbOdW_vCzZ-JcIb07rKRQLOFSjUuM5iS6zvwXmoMvJua5fn0wrpvSzoQ9IMvMi_pwZhmhqxKiIlhITFeABtp7aJT7qOuu73bYRJCtsrv958Q73_FuX_29Ohm1VrCwbsH7Y0Y0jWezT3ftlakOfIwZMVPTN-iDEDm_jFnCuG7Yl3sQV64eReV09A-6N68B1MZWsFNVBiZk5FFidrM78g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 00:15:32</div>
<hr>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=CGJ2IYAY_HuuP9opo2RDZmPfUK9IrLdV6HJGrjMspqp_xVLj7ljyzwUtmifagjtJQJub3wJeo3p-MFm2C-RtYrESu8AHUOXZ9ObtxlwmmYIn6_vziXgCoSmCo5RH4VB8-J3a3IbRThW8KE-c4PK3IkBpHaqSowFE0tsfeLKTwL30doDT25wFFi1CJnbeoG6Ws1YF1YHXZMEHzRLWfLUFCQ-8ZxWjOAeeyVTPfupZBu8I9YLqMfcic2pSaQxsBQEk25g6nD6M1cqifVDlfYkOoVor4j2e1l6uS5O5s8QyY0Y3nE2737miUQnQMpTvTJm4wpKO6wiQAnpRunmLtKDHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=CGJ2IYAY_HuuP9opo2RDZmPfUK9IrLdV6HJGrjMspqp_xVLj7ljyzwUtmifagjtJQJub3wJeo3p-MFm2C-RtYrESu8AHUOXZ9ObtxlwmmYIn6_vziXgCoSmCo5RH4VB8-J3a3IbRThW8KE-c4PK3IkBpHaqSowFE0tsfeLKTwL30doDT25wFFi1CJnbeoG6Ws1YF1YHXZMEHzRLWfLUFCQ-8ZxWjOAeeyVTPfupZBu8I9YLqMfcic2pSaQxsBQEk25g6nD6M1cqifVDlfYkOoVor4j2e1l6uS5O5s8QyY0Y3nE2737miUQnQMpTvTJm4wpKO6wiQAnpRunmLtKDHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePD7R4akJNHgtADoLLrEGmggcBlHSCWonPMhTvzps1rXUU5QHyOhW7AEJU-wsoCKCUkneA0rIVGxQdV09hWNvoY_TGlJ5JscAuvtZwx_FjQPBCNolGMx4uy_2miPHn3C0he8F-Gdy5AhkwXxOAByaQgsQ6GpjfFXJ4p_LDkiDMTeeIU7FewLD761zzIK_nzdyGFUILhJoniqmXXl9-JDzIa8tRb9z7d-WDIwbk4RDxJ302fMiZ5dqD3kwvZ6QpD9-bgN2Xcb8y5ApKiAcjQ1GStsDV-1ajjMCVLCx40W1Q92zkQk43Tf-lPU9Wl2idMzPSEFegspk8Z5VfDYGxnJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahTgi4jsNM3S9IweY50s1VBGNfoHpiiZlJ1GG4UftA0KGr1gEJy8J-zr4MhwZ-xKyLYgzPjYRgkxJgtuXDJCLQYxnqjIsn6yowDqYlu7yIpsWs93Z5j-MppWVYNi8GMJOdoZUwlM-cSJHRx2JWfmljPzCP6Y7_8Mxf-yGHtVHEZWj0zfPgXUZc4Oe8QlqmovLr-ViaaCaqSe-U0ZoO4S2VTwtWyVXVxBnz3hdD7_r28_ydLtBIATwbt6qFTAlD_8jyV19w0aJzIN4o8ep0ZMIaiwXTfojX8gmDD66CPQP_35DRgUUfe0oDfTavWdnVLieTvkCe8yQYqlN3ctkyt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fKtz9aVfS6J92jL69gAiGDLK-hG0_m_Du9Y2aq_OjI1YQUEsBqRGdm1rNOwFBZFWpQY1Qyvm18NDHceTCKgn5vRB_LWiExThmh8TkQ6f7cGwXIc-aV7YhrQUYgHJT6rRXHehEP-aosnmcK9z2Bvv71pt_Xo4wx00bpAcrgZJtPo7wcpRaT8tHOmL_hxZpB0EDZQiw6kS8u-hyX6BX-wc7CEDlEXqBbjNbOh0PP3ONGn0L_dX2hQCxkjgB4lBpL_qw7WhyPdfJ4-hxX9AGeowUnGHk2_5FwgXo1P50MSQ-8AyaqOF8R8aKCDxqcaNOzABPwBgoofO7RS3isGG6oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4HqklxJfku_mrrXqYQ1CIzBAaSAdMXnTBy2XWgsIZ8NLZpYhdYtn_0Ffil2ADCLPv5yaEQLKbn-1vkJRDS4nQJNYSdsJlnh_ev36mChCgcKMggsMDhaNSi_KyKQA5p675Mf9Pd3eDlUTcCJJrjAuHhTqAeN2sodFUvihxE92uuUigBTsTgyrn7CVmuUPICvqDNITQBDMw6q1IbVqcI929Dg08qTsuwE_3iEWeC3HwJWisRYmWud7z_-PoUxJEERLLbI7p2ycV6DFRuL4e_u_n1Xqj6u52voOKN9gn3d6a6uSPSnCmJZRekX9_iU6-6Fx0FKaWuLy2XRmpe9_Gjn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSh8XnVVJtqMeqBeoxSdMkzBP_9sBj26r_9c7BS5O8G50pjkEuePFJQs5eo_jZGjkFvKIoU3A7UhkGeML7_jHBDPg7_jYGZ8Ufy7LCfo_XN9HuwXrMHjrtDPwGs9MXLshAfn4KYhEYO1kIxBEObAKUfhEELYFiUPtJNNpWvfY7gOV2twztQrUqAcD94kxPXcBt7xKe_WTsTodQSqcx_OCm-dqyBoLnjbODXdqhZ1NK9XYaf7iuuLbOcDMECGn7ObWNXsGTAjXWhYWia_4xk0U5IylXiR64mEu7ObKRNND4F2k1Nyn2c7_NBzdCsKHWDQdngLx7rizzeCc7pYRja47g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUgyRuPHGfoBzNjz_qKV2ynpKmsOiKaDYcjLsTVVo8MQI0VqP0uRnyqfoDbmHADBRSVMQW4krTK4Avt-bHYhBn3rwQvEhCMMOtwm73H_EyzxX3MXo_oAPoAcWF9qC_BFuzFWVirrGe4HQo_6dMxdgLWM_a5IdPyFqbYBTYhaFko-G-mvJentcqXn3qnUR_ponLAuvlw2c95RnsorSuEJNWnNyy661Ev3OrnCSin44VR7goG6AYs5sI3PSZuTVo7Uk0Jmo0M7gcn95z0TJRJzJ-ZCqX3A68VmAQ_k1Updg-20aWhVXplP9t7TSeBQIPFMJWD_MzcE6B0-YLijBu3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvlJ2Gcfpc20kd4-xLcnOdM2ZA_9XeSQZyfY-Bt9WW20t2FUoUdeMT-GFFpfz59GcRy2PfQ4S3seRRWmL_I0tchrYWvou0ScPa2_fFXlQILnbf-YPBMAfYxfasbNGcbCSrclSvStEi8THdVEdxFDjfVhKpnXp8M564lw08EyQJ_4qXCv9LLnhyuvnKtD_G_AButi-E2Aft5SEKR9DTD01WcNhx_MHZJSs7BQqdtj7CqFWzMFx5ePbUlPG2WiRMy0Ut0TRYHXqAcAyRuprg0iegzlqwynwymgEtUj5TPdwYVCsoNj5veR_nqXDR5wE05H9GExCwJIsVXKyynQWXmw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=NXSImXi5SWM0KjfVhI9BqN9Y4prI33KEQYDIOdeDwC2xK_nNDjAObEtZ7M9psHHsKGa3-JDOG2niOn3WiyHRVckMmo8j488PHaUWFpliRxeryXhD2MukzCBtmnLbDxW8yLYkU_fCPaHW76Q1ZSAxuhdgpK-HamC71KcHwory-jO0hwaA8jKF1Eb0ntxUvJIvQPQpi1ywAZDyORPM-nNqAwNCyr-gOHzI2jgjoUwHExjwH-j_UwnLh0OI5KYqGnU-drZ06M5z5UhfhrJ252MRz003bkELJFbNfjZlalEbVFAjVvJJn5WY2aIhRpXNAFYd-UdxETWHivzRtLFJiKJiXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=NXSImXi5SWM0KjfVhI9BqN9Y4prI33KEQYDIOdeDwC2xK_nNDjAObEtZ7M9psHHsKGa3-JDOG2niOn3WiyHRVckMmo8j488PHaUWFpliRxeryXhD2MukzCBtmnLbDxW8yLYkU_fCPaHW76Q1ZSAxuhdgpK-HamC71KcHwory-jO0hwaA8jKF1Eb0ntxUvJIvQPQpi1ywAZDyORPM-nNqAwNCyr-gOHzI2jgjoUwHExjwH-j_UwnLh0OI5KYqGnU-drZ06M5z5UhfhrJ252MRz003bkELJFbNfjZlalEbVFAjVvJJn5WY2aIhRpXNAFYd-UdxETWHivzRtLFJiKJiXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=bD-xOHAfUEKdvlFJhCZ9fe7NR1lZn6LlEthooXLBGRmmOR4RBNPfyQdjCzDWpkFWT_2Q0EX3bWbmwks3CJtvwG_grtoBoxdKWa10VFU9xk6IWx8iAmQW7ax5Q90TLKcaUU4RXRJhoDiUB-2_SNknG0Bv8EIA-3Mn9nCssh2HketqPCOnAEBid4XNUFjvjPuqU5Co5lK0uzHFuPNGwlCnsVVhNl-D3pHON-kNYzeP4X04dnGyGSfwXZ9y3ggu7PPsrShGn38vfuhZVz8TVa5TUkHYRVa4furnJt5-H_AqkdI9EY7xIJ1Ouy1a92bEQ67KnPUTTAVzoRBndw3bGZkWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=bD-xOHAfUEKdvlFJhCZ9fe7NR1lZn6LlEthooXLBGRmmOR4RBNPfyQdjCzDWpkFWT_2Q0EX3bWbmwks3CJtvwG_grtoBoxdKWa10VFU9xk6IWx8iAmQW7ax5Q90TLKcaUU4RXRJhoDiUB-2_SNknG0Bv8EIA-3Mn9nCssh2HketqPCOnAEBid4XNUFjvjPuqU5Co5lK0uzHFuPNGwlCnsVVhNl-D3pHON-kNYzeP4X04dnGyGSfwXZ9y3ggu7PPsrShGn38vfuhZVz8TVa5TUkHYRVa4furnJt5-H_AqkdI9EY7xIJ1Ouy1a92bEQ67KnPUTTAVzoRBndw3bGZkWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=mn73Rm0vbi3gJkUHcPRgV0T-yetfcNXyI5w3ZGFgPQ2iCWGFNztnsA-8UaoudRRAEzRWwbCXKYPCW1Qfnjk90rKQ9WNELkfrYCBz4Gc5vFh2mJir-ljTNiV_p11lGIhXO4NBMundWK-budptE71CuvRicb6l0auvv9PnPLhZosUAKOpYBJglbY8Ff575qE0_5VXTDKpP4hRlcAlruXoV0GoGHrgTKCL784NiFUE2I14L67LhhXy248xjJsfdgugoXupCsGakyEdrB5kiVE1BX8f05sN2iH6BGeqMLDbqNsz0-p9RuSTs-ZgNX_V9vAafjhD17icbpGkINzjMMhi88g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=mn73Rm0vbi3gJkUHcPRgV0T-yetfcNXyI5w3ZGFgPQ2iCWGFNztnsA-8UaoudRRAEzRWwbCXKYPCW1Qfnjk90rKQ9WNELkfrYCBz4Gc5vFh2mJir-ljTNiV_p11lGIhXO4NBMundWK-budptE71CuvRicb6l0auvv9PnPLhZosUAKOpYBJglbY8Ff575qE0_5VXTDKpP4hRlcAlruXoV0GoGHrgTKCL784NiFUE2I14L67LhhXy248xjJsfdgugoXupCsGakyEdrB5kiVE1BX8f05sN2iH6BGeqMLDbqNsz0-p9RuSTs-ZgNX_V9vAafjhD17icbpGkINzjMMhi88g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNsPYGZ0qvEJfuL9Z4J5N1VHys0RiZdUrqdWm8bGwSZNU03sND2ojuxXl1sHTTNoWRS6gRYB2ANuYFtB2R-dvRpUCBVr91dGBwZBfNQi-IN2lWDJ4rqXTvJugZR5WrD6g2vxT-cSUB733sBfEFwwBXBO5tDAzi8dmHa2cE244Igp-kcrbCg_X6ezBruOmcHKl1-6KoTf_vxNeMvs1sr7IilNPTp3wABVo1Yz-0kjo0nq35sU8fYP-JMdgR19hWSpQRGpH3E2GUWNm3LN94S3cHESndtySP7r3iccWFPkhRshLdwwHEU2JmsHBj8REOaYQ-m_1UJUAQ2dRnW6mvExeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=vEtuUMEa6TGA-vZ1QeLK5RMKLYbX5BC91bBSuPVrz1y4R0ke-yhuT2LeRqsOaOEqQGW6lSJNzlP7gRHeJpDcy6S9si6KklLy-aK012QkqmwjPYIXraAOQpyFdXpXnpvsmmAgOT6s6fU02uOEAqnkjCGtLcjClzgkypQ9RTunzTwU9v3vPi9VRFJZ2Esl9ZlCnnADujCsTGZurLFIWD8aoBt6DgtvzDgxYfueQ_8B6JsSJG17HO7UCA8l3h_NW7SFHFHKNFRMj1kX4FUnaagrn6QPpYBtBfcq8ZKumkyE4lkUD8Drz2RR3OQUPWBluHtfgsNc2g7_BioZuqPTBmTnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=vEtuUMEa6TGA-vZ1QeLK5RMKLYbX5BC91bBSuPVrz1y4R0ke-yhuT2LeRqsOaOEqQGW6lSJNzlP7gRHeJpDcy6S9si6KklLy-aK012QkqmwjPYIXraAOQpyFdXpXnpvsmmAgOT6s6fU02uOEAqnkjCGtLcjClzgkypQ9RTunzTwU9v3vPi9VRFJZ2Esl9ZlCnnADujCsTGZurLFIWD8aoBt6DgtvzDgxYfueQ_8B6JsSJG17HO7UCA8l3h_NW7SFHFHKNFRMj1kX4FUnaagrn6QPpYBtBfcq8ZKumkyE4lkUD8Drz2RR3OQUPWBluHtfgsNc2g7_BioZuqPTBmTnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzItsqMlCjH6V2DulLeFyCczLPnAlS4UE7v5D72szodrhz2xvtTafEDmBhk5okv64wYsvBsTaMofgn-rwZTILM0CYPRH12fyeKYbmBwqjeXfoQWXNoWnUY-z7akuRXLVAzSBKcVXD5MUnrMWER5Jhi6MbCr2L47POTaoVZIkcloGrdUXpcQ5wXrVPpAKp5IZptnxLU6dxzgL7sleLqnZ7_Sp1xP0HIHlFMU9sPDJeXmDIXykCke_RtfwTp9NN2kXc3sNfIyDqgpA8caJ1qYWyWj4qXI1Em9c_yjiiVT50uDTPVbh7FhHCWXGB63op56QsPEtE_HhsZirg5YhtgAs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNotizy9hHn_t-0A1xCC5PjtSvzMLX3GWGfCAvLtEXBWpMBFohqhCWLoS7yIjx8n8MxHSDe-iq39YZiQArIOitwB2NGO5Vglktp1bHtV7bpr4fnwujH4SVxUSuh4T9hxnoki367p6hmNTSjYI9lXX9BD5_9QyIEmNFa23oANcWWTZ45WGDEeS0zF9dwahuWgomjoEF-cKBssWVVJWiINfcVHyGmOGVO3S2W1Hp3LjOTZS0EPXo2oiNNAf1TOknCwM_9hmQcoP6ypkrIzeN8CdmFS2NqVoPeBXnJA654NNZd64Qs9eOZi20fJxLz79qwkGBATg3riWiiEkbezwASOmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Tt5qQl_sk4MZc7z7GZxO3btsKSXfsA-IxhmWQykBGhnCxr3Fz25kpNNqUC-EmcCgqkMq19ZaE3lDi43Iprne3HM54wngB4shc56nVaUjPX2ki0UTui7WM96mGYbZ5AdHOVorBvkVwG8_9-yCa54OD5-5_eIJL6Ap390eKaB1xtVk9XBg1l5-bZ5yiSY39mwNVJnIsM8SmuQ9dJyshwq_uyxmPCU-NB6w8-SgcA-KtVKBNbbpvZQ2SAxLSCgXD56Qgihmr8x-WmusgCAKi6tjUoNScwrKNAEJFJktjZNb9AzSUsx50JaZPvIhkHn1omTLWBBcejCxYJBqrya6fCGHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Tt5qQl_sk4MZc7z7GZxO3btsKSXfsA-IxhmWQykBGhnCxr3Fz25kpNNqUC-EmcCgqkMq19ZaE3lDi43Iprne3HM54wngB4shc56nVaUjPX2ki0UTui7WM96mGYbZ5AdHOVorBvkVwG8_9-yCa54OD5-5_eIJL6Ap390eKaB1xtVk9XBg1l5-bZ5yiSY39mwNVJnIsM8SmuQ9dJyshwq_uyxmPCU-NB6w8-SgcA-KtVKBNbbpvZQ2SAxLSCgXD56Qgihmr8x-WmusgCAKi6tjUoNScwrKNAEJFJktjZNb9AzSUsx50JaZPvIhkHn1omTLWBBcejCxYJBqrya6fCGHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0qANt0XMrdVXyzf91dCA2O1OmBBbIhE9o1L-DBZO2wLSe67jKQZxYGxHMfwfRDGzjq6f_bjhrNFTbOAv7Y8kAK3MUdgL6iGh9eDiZncmM01rmy76KylHSoPrqFkuFBjo04I2jyuZlofuf0Q6aOEqCpyb9X23upQfpkhY4zPylk6C5TEAmb1BtF5v8Xg5ZovcF2Gst2Ag9ve1osSAUVJb1P6wtavwH5tjpKErRKl7nWjH-2ca4vHVeR7GKu8fyXmyss9We4sET-yG9bfQt2S6FlV1g9QLEclI_X1yl1HAMw1NcQ_YjTanx9ZLk0JwyGJPx4ZROGpaYi9dHYpMW-RRgbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0qANt0XMrdVXyzf91dCA2O1OmBBbIhE9o1L-DBZO2wLSe67jKQZxYGxHMfwfRDGzjq6f_bjhrNFTbOAv7Y8kAK3MUdgL6iGh9eDiZncmM01rmy76KylHSoPrqFkuFBjo04I2jyuZlofuf0Q6aOEqCpyb9X23upQfpkhY4zPylk6C5TEAmb1BtF5v8Xg5ZovcF2Gst2Ag9ve1osSAUVJb1P6wtavwH5tjpKErRKl7nWjH-2ca4vHVeR7GKu8fyXmyss9We4sET-yG9bfQt2S6FlV1g9QLEclI_X1yl1HAMw1NcQ_YjTanx9ZLk0JwyGJPx4ZROGpaYi9dHYpMW-RRgbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=c2scu6zMMslNpVK1i6xWQ3m8C4FCMOX5zaJsBK3M75cWIutYE46unq5X5lYZSo1TniKCFaKn3-amjL9zWvA7BENVN7xV0VKorQYp8OuReET--_LG-FX1_W-jdYZyMOjy7OVrnXDynr26nGEXkmzPB93EWvFLSkucmefJWO3yGghQ65fnAlAkry9FUsGMnonIa4Hdp_4W5dicNyqQIVemwMtEIhxgnGvQJAx1NqrOd0TqZUaNWz75pmQKQOfC5zaeQW3yJqCCKCgmKOjcnP3U_X0_60KS85vwNOuN4x3iYgdQoLP4fghYaz1PPAHBATdwYZMDPIk-ro4wGGFmSVzsWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=c2scu6zMMslNpVK1i6xWQ3m8C4FCMOX5zaJsBK3M75cWIutYE46unq5X5lYZSo1TniKCFaKn3-amjL9zWvA7BENVN7xV0VKorQYp8OuReET--_LG-FX1_W-jdYZyMOjy7OVrnXDynr26nGEXkmzPB93EWvFLSkucmefJWO3yGghQ65fnAlAkry9FUsGMnonIa4Hdp_4W5dicNyqQIVemwMtEIhxgnGvQJAx1NqrOd0TqZUaNWz75pmQKQOfC5zaeQW3yJqCCKCgmKOjcnP3U_X0_60KS85vwNOuN4x3iYgdQoLP4fghYaz1PPAHBATdwYZMDPIk-ro4wGGFmSVzsWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egLuU1TS0eyvUX65pY6BTIUbeapoB3pOczPulWX9SZZWdkyR66szbInKs-4oH0oHDWlxSy8848pwOVpK6O27QC3WX_SHi4Ys7Y8DaHsLBHxtlpxfzx2nYh6JZD767cPTvMQvpjHwhzIdw3QkBIsu2yCIeKr1aEU-VbrWX4M0kozmxjBeEmqzPiTAtLIs4eSkM5jNIX33LofLDUO1MBTWfRRd9FCqeY0hUBzoqCrBuzJfitnutcVjzLxgHPeK5DB2oix5R-egYX4AAz-MJiwWrscGwUrT4N0-bf6iJoSoYy0sdpnunXtmSScTAGT-T7H3Wo2wAHfLcztIrhNVKf20uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=hGZC1gYkoL9OwiYr_IGsplJ3U4S0hBzp3lhnCC-ajHCU5PbxgnRVAztBOncmt97r9taiN75tYx0ikeXU8JAeU1V4BWqLEKH-4BQD_nvaIG4t23jIk26D6eiGkuklfOUdiY3LPfaF85400dNTO_mBiNL4BGGo1u03Rs1PTfeHgDHQciGpdL_HsoEJcydCd7TU84qHAFz67IsswR5Oe8UAU1AYu2vQQmvnVzKBESTlXZ9EPDGVIiN4GlwCoWyApqYZnW7ki_Sg0gUcs6Or1weWzPGrl0zDr7qP79RJOcJkKS3VOxpeZaW_HV20uxfeaPbvbsru_5Buxj2zXAdhta0jHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=hGZC1gYkoL9OwiYr_IGsplJ3U4S0hBzp3lhnCC-ajHCU5PbxgnRVAztBOncmt97r9taiN75tYx0ikeXU8JAeU1V4BWqLEKH-4BQD_nvaIG4t23jIk26D6eiGkuklfOUdiY3LPfaF85400dNTO_mBiNL4BGGo1u03Rs1PTfeHgDHQciGpdL_HsoEJcydCd7TU84qHAFz67IsswR5Oe8UAU1AYu2vQQmvnVzKBESTlXZ9EPDGVIiN4GlwCoWyApqYZnW7ki_Sg0gUcs6Or1weWzPGrl0zDr7qP79RJOcJkKS3VOxpeZaW_HV20uxfeaPbvbsru_5Buxj2zXAdhta0jHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=W3X1WV2KLrRZRv7k4iXhU71XQxbSY-DA3bhDUN3YGgny6WE3pO2pd5piZpU5vpoCvnogM9Mcw0UaUM2fRA1Hnb0b_EhznHyU6yrfSxUDUCbqgW_QkRsKPS82F3kaWHIbTcH_8XLXbmHe2TVToqVFcFMjoB6G1vtuT9XTEscHlmLiFM8Wxw9py-YHwfgFOPE0G1rd3l3CCSP_4rpOD25MSvEz3-Z2nX3puEsccsl_4XUK1DdjQycimAZHnEW6DCu5P1M1f3839DwDeqfp_UADngiNMj0iKoVTMyU_LNSim2LMXpWkJjDaREjf1wSD8z3YnIgQ8TVTBriqVW2SSNQAiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=W3X1WV2KLrRZRv7k4iXhU71XQxbSY-DA3bhDUN3YGgny6WE3pO2pd5piZpU5vpoCvnogM9Mcw0UaUM2fRA1Hnb0b_EhznHyU6yrfSxUDUCbqgW_QkRsKPS82F3kaWHIbTcH_8XLXbmHe2TVToqVFcFMjoB6G1vtuT9XTEscHlmLiFM8Wxw9py-YHwfgFOPE0G1rd3l3CCSP_4rpOD25MSvEz3-Z2nX3puEsccsl_4XUK1DdjQycimAZHnEW6DCu5P1M1f3839DwDeqfp_UADngiNMj0iKoVTMyU_LNSim2LMXpWkJjDaREjf1wSD8z3YnIgQ8TVTBriqVW2SSNQAiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=eMq_jn3XNen4-BriQfBbHSHAzBfQgAlcgK3nMFhGqFPouGLoSPbyNo15fMIUu4FwsumFuc6eGbVJbTvjhQsp8gQaxb6BklbHw3KaOwoaA5TD9lWO8nQhKgsPOxRqAFoIs-IAI405qIyV2hTlBIzyu2gpgUPkvMfHdfP7WYgceYZxk-6szq3Oq6pPbdraBGpoQXv2bIjQFThjbN50MTFEAuFIOENPDZWzrmyS5hHApDvwkogCRRVsQ6_SEpWEwAkILtqLfQyxEkYdGqX53N62vOfvtWXpDAjrhCdQ00c98ER4-Yz1-N0ll6lNuKogBKFjh5iuV0c8A3cNeGwM-R7M8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=eMq_jn3XNen4-BriQfBbHSHAzBfQgAlcgK3nMFhGqFPouGLoSPbyNo15fMIUu4FwsumFuc6eGbVJbTvjhQsp8gQaxb6BklbHw3KaOwoaA5TD9lWO8nQhKgsPOxRqAFoIs-IAI405qIyV2hTlBIzyu2gpgUPkvMfHdfP7WYgceYZxk-6szq3Oq6pPbdraBGpoQXv2bIjQFThjbN50MTFEAuFIOENPDZWzrmyS5hHApDvwkogCRRVsQ6_SEpWEwAkILtqLfQyxEkYdGqX53N62vOfvtWXpDAjrhCdQ00c98ER4-Yz1-N0ll6lNuKogBKFjh5iuV0c8A3cNeGwM-R7M8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=qX1BHB6Vo53aGuuGrhgflgEVOMLmOQtEsL52aKklgGzZVsIwd7NBAHR1mBn02HyhU39XoVOqIIIwVt-qee1gt-JiotomqfBsmcNWP7RIUwmsz1Dpgab4qftjGLNTFDz1lWCcxJB02Dnqr9ZGrwiQaJfcImDKsHd7pnu6-tiRBItD7TitTTwooIqmjOzCC8XdMHxaUKp8zNnvUR4Iy36K1dh4JTRU57HuTs19j-Lz-yzB7RNI_G9CJckEuycUEIR2ZSGNzJNzrZxKCLJY6JXU8DjElspkbEutJ4KAWBpiH5-rVU7xydVQW2hey-71e1n4FoCO8TgAlZJ2pYb95vifMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=qX1BHB6Vo53aGuuGrhgflgEVOMLmOQtEsL52aKklgGzZVsIwd7NBAHR1mBn02HyhU39XoVOqIIIwVt-qee1gt-JiotomqfBsmcNWP7RIUwmsz1Dpgab4qftjGLNTFDz1lWCcxJB02Dnqr9ZGrwiQaJfcImDKsHd7pnu6-tiRBItD7TitTTwooIqmjOzCC8XdMHxaUKp8zNnvUR4Iy36K1dh4JTRU57HuTs19j-Lz-yzB7RNI_G9CJckEuycUEIR2ZSGNzJNzrZxKCLJY6JXU8DjElspkbEutJ4KAWBpiH5-rVU7xydVQW2hey-71e1n4FoCO8TgAlZJ2pYb95vifMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej7b3xF3WrMHzUg2bL05DUCKAESNSENHRwD2nwXEzQHxcMZgauz2LzYm-UP9XAbPgvM9_BZRocv6_hEr0Vxp0YM4etdN5GiYK_L5sYMxVy7bywCPNA_HF32n4BOzE4M57pPFzozy4g_yA5GRG1zN0x0bub1_UCStUcJ4MmN8-LxM2pzWxjNocBgLoCVQp9uHDgVvjR8wL-xQzWLZ3HqQ3a_28Bo0IaCOupFVqd5YYhEZ6e4_hwe0h2Xc-vD0MeVBrl99Sf21aHc-KY3O3BZJAfVOJlJq3V1aVCs8VGgJs_xEtdk0BegAZtlWzsTdl4FD6wcTuR1m3Ji_H3XiojU_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=SwnfvtZxI99dTBlH6jnTutA4p8D-WjMCDDY8kvkjYh-jF28q4JhrUaernsox5M369gduBb1aw5V0mj_Wity-p82-Vz0pME4QACiZh-lI6wZyM1XYwTYffI9AXmjj_EHLxfveHO-LuUxLNvHBrF4jis9WS9ziLX-mc-46fo_argU6NZk3eqagLtxavBVYoLJd60Wk2AtsF6qcLu-cIdl_WHuVBM8zT0FE2YNtjQYDPVenPzLwHGF0R4gvVauIez2K-tMEHtGmJNMW9CTxLOwdlV38E2ZIdOn0ODDu-wTWdk5hYzz6fagOOenFDUSDNORzAhpMwcxi_pI69rwM_ovy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=SwnfvtZxI99dTBlH6jnTutA4p8D-WjMCDDY8kvkjYh-jF28q4JhrUaernsox5M369gduBb1aw5V0mj_Wity-p82-Vz0pME4QACiZh-lI6wZyM1XYwTYffI9AXmjj_EHLxfveHO-LuUxLNvHBrF4jis9WS9ziLX-mc-46fo_argU6NZk3eqagLtxavBVYoLJd60Wk2AtsF6qcLu-cIdl_WHuVBM8zT0FE2YNtjQYDPVenPzLwHGF0R4gvVauIez2K-tMEHtGmJNMW9CTxLOwdlV38E2ZIdOn0ODDu-wTWdk5hYzz6fagOOenFDUSDNORzAhpMwcxi_pI69rwM_ovy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=oCxbnbl5OUQtJ4p_oaOtaDg7bKz12Xb67Xw77pGx_P3xCrNPIxgjoj8qZfzQvRDD--WMA5WA3TJembRS33wah2-DbEdQY6-YO_CxRMkXL-fu9RhOEMKEeaAUazW8GaJPJyLwIDafa8seTe85aNqtwn13S1H0zQFCiiZ3CSbEnTuJyLtFTOYUwpQ3Oz7dIximAzVvZQ2RPXRzIy7AhSCTPYhMVyosHM2wltcd-CXCJgh9ZQ4Yf9sqfMCehkYZw65o_mCAYzVIlAvxwgVM360o3ddDemLr8XeLnHsl6ADJdbZqZswBc_0MwbXwx3mz7XPxJiT3FTWxkm4eKDeioqDiNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=oCxbnbl5OUQtJ4p_oaOtaDg7bKz12Xb67Xw77pGx_P3xCrNPIxgjoj8qZfzQvRDD--WMA5WA3TJembRS33wah2-DbEdQY6-YO_CxRMkXL-fu9RhOEMKEeaAUazW8GaJPJyLwIDafa8seTe85aNqtwn13S1H0zQFCiiZ3CSbEnTuJyLtFTOYUwpQ3Oz7dIximAzVvZQ2RPXRzIy7AhSCTPYhMVyosHM2wltcd-CXCJgh9ZQ4Yf9sqfMCehkYZw65o_mCAYzVIlAvxwgVM360o3ddDemLr8XeLnHsl6ADJdbZqZswBc_0MwbXwx3mz7XPxJiT3FTWxkm4eKDeioqDiNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvaQS7izjg9RgFXStjajoZp_HkCJlU5-CFm7KQEMuMBGpee3oLCJditPZPrxYUjbm1N0uxJrHX8vHjcCIA4DxO8ntJom6xi2fOYupp3SEcOYdzVPN6ZoJ0GFUhn8aVmm3p681HZJvrA-QNpUKcwWOyPr8_kFl-mkhbxsIGgfwqnM9NSAerZcYlto7atgc-ANYEybhSie0tCKsaX6pUWyPTI8nYMdPjFI1Uy1dGvsIBYZSxFcfBJC9i0V7khzWPs5unPEmLmnRgXdOwjzNQx6qvIr1mU8AtoTDnCBoLBMWfGqltA2ez228Q93kRCSouv3_-Siol0NXYJnIsgw_Oifwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=bppD52HhylObm0wKHUuMwIctabKx_UnaPYTeD8gDnI2jW0zFh8PLnRGuNs7PirpizWYCpFQmRnMohpy__N-FKUqsLXkTwSXZOCRugsRL1dQNLnwiXLZeWenqVxpUbwdVwatZ1MlNKxmFo_AX0bTntZLevlD5Gpu0G6dsLkcgrS59IjtiiJ0-XCZu2ao7o2Ul9-N8Bs5FtYoZwQrZOTsohZPhJ5JqL8LSdvguxTHkQf-PN4cBe6LkVpFgI60WqKCJNtlTH17ZmbnOMj6_4dYFdA_SvmtZOK34VSyQuQCRvlLRa3MiWvVFpj_ehxZORgvtl-LI1Casz-RhqEnBLL69Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=bppD52HhylObm0wKHUuMwIctabKx_UnaPYTeD8gDnI2jW0zFh8PLnRGuNs7PirpizWYCpFQmRnMohpy__N-FKUqsLXkTwSXZOCRugsRL1dQNLnwiXLZeWenqVxpUbwdVwatZ1MlNKxmFo_AX0bTntZLevlD5Gpu0G6dsLkcgrS59IjtiiJ0-XCZu2ao7o2Ul9-N8Bs5FtYoZwQrZOTsohZPhJ5JqL8LSdvguxTHkQf-PN4cBe6LkVpFgI60WqKCJNtlTH17ZmbnOMj6_4dYFdA_SvmtZOK34VSyQuQCRvlLRa3MiWvVFpj_ehxZORgvtl-LI1Casz-RhqEnBLL69Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=VtxX3K8qaqMgKj5R7othJaqIKKVX5MdhMGZIqeSoHPqps1BFVVSOA9PxuGPGGB1POb1Uz7cyDVew-6rmiEs6HIeh7FKc33y_yevvomYHeEpdAJMXYEZ0O6HqEG7GmQ266CtS9ykFYPwMGfUvSuXSc2EgfqXUwY6tOOVzhc_Zem6euhJ0OclvBNLCdTo4artPyzEDOg8ordF0gNye0jZHo3IRRCf1ciw3biPezRO2Yt8uVb2UJp9tDgyqm6NF4ch196pEk6exqJY1U2eTNli9KrxLYdUzcIH_0m_AFKgIfPOdSK6Wa_LOpIc3-UYa3kHFza_CLjILyuAsOVZttnI7lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=VtxX3K8qaqMgKj5R7othJaqIKKVX5MdhMGZIqeSoHPqps1BFVVSOA9PxuGPGGB1POb1Uz7cyDVew-6rmiEs6HIeh7FKc33y_yevvomYHeEpdAJMXYEZ0O6HqEG7GmQ266CtS9ykFYPwMGfUvSuXSc2EgfqXUwY6tOOVzhc_Zem6euhJ0OclvBNLCdTo4artPyzEDOg8ordF0gNye0jZHo3IRRCf1ciw3biPezRO2Yt8uVb2UJp9tDgyqm6NF4ch196pEk6exqJY1U2eTNli9KrxLYdUzcIH_0m_AFKgIfPOdSK6Wa_LOpIc3-UYa3kHFza_CLjILyuAsOVZttnI7lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=m58Z7Z4-mpMiE5y0xNcLCinkyWg2pk6VkeaUW9ySTdf7tvJnCFHczc-lOzYlqeSvfx197IzaCPrCgDIZtmO4s8dcUIW3NmLUTXAXtwyOD8nufeEqC_bZr4M5hFu6GEYKCsOyQmmNvgKYN_pxyZCqm2500WL6p92KFj-F0XHpbt3iE-EzYXkOLaUkE_Ccy7TDmEcOND4g5wHBzIDO11HKSeBrbm0SDvA1rU1Puz2KgaAAaCSMPIAVIrHwglooIx4dWaxZDWqr3T8_vetNf7oItU0Z6sfU7r7PZr2ZSCQ9HrZIJKoNpWxs9ARRLQxN1pWkuJRkYApraZFtm5cNtScg7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=m58Z7Z4-mpMiE5y0xNcLCinkyWg2pk6VkeaUW9ySTdf7tvJnCFHczc-lOzYlqeSvfx197IzaCPrCgDIZtmO4s8dcUIW3NmLUTXAXtwyOD8nufeEqC_bZr4M5hFu6GEYKCsOyQmmNvgKYN_pxyZCqm2500WL6p92KFj-F0XHpbt3iE-EzYXkOLaUkE_Ccy7TDmEcOND4g5wHBzIDO11HKSeBrbm0SDvA1rU1Puz2KgaAAaCSMPIAVIrHwglooIx4dWaxZDWqr3T8_vetNf7oItU0Z6sfU7r7PZr2ZSCQ9HrZIJKoNpWxs9ARRLQxN1pWkuJRkYApraZFtm5cNtScg7jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fxWSjE26fznnVhy_fbpZbOt9Dk7n3CrGA69itzpSOwhw-SEtt_CcSh6lfXYEG7JwxWhfH27AwuKIAbh5VFlbOGZHeK1ZsXpTHJmb83EkynE29riF4K3UOCRvXlfyosu1rMxaX8HvYFPTRdM5l6g6qKw3_0KZmKBmuba9ZmpunKSJvDByl_s8SmRmePm_33tSAYVoxD0iQbC0MYonDgrusJHVuW2GadOuRqVX1VC8aGp5DgV7zVvjRc1F7hzl4aqsCvGR8sdAQDdcp1cV8cVmBN0tEmct2oxsrLhuXH_yFDatjIxpUZ8A-wcb9dINLgBFnoq6VTiPIF4Dq3QXrtJTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gj-gvLpruvNjTx2vsQl_HNsxUcUOTpwuzTS68oBqwif_sSzI-MFNohKCeGP7TAr2KCwIUSknR0Z0zsXtPkfwM8S8B9xHc9ColbLppLckBqV7jzm1rlKLc6Bb9FxO4pKvmx-4fg91XPh8P172p1YaN1GOVMVMVNDEdw57YOTTw9-X85YNr22FxQ2ta8Vso74vSLUZim3PC2pnbDqEbcQGPnQKWPlo0ZFs_a09jZz7agfjY6tOcVYldQZgG8Xoq5wxATg_HogL0-K70-EaAKfzdwpGyZ1aZXgh55hg95BXVYT7rnOk4KQk0kkjV21Yntf1fJoMws507BalkALHq7w13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFx5wrNRDpqN1uyCLv7n-vh1aaE7qgIQ59dMNrmpFfPs0_fgcYadtMKrFKKp3eR1WNmX-QKKOxwV7giafoNHQ3LDfHwj5lEuCK3R612EgFYRuCoM_n-jZHWqM-8E_LgYjYuFoIHRQ84i9UL3kqTdCq3Fh7GUd8K2nzaqY2CVhqD6yGPaE5Gy2RXQ7pcHKb48ROLUwYB5hkDutbvoMN-xT8UAA9J8_wFcf1IoGB0nAhq2gJqfy4lMzLNO2F7iI3Va38SGkSsU2TWCchOjf_EDfkBD2zRH_nmLfPjTvPsq9wbJ7Dst4FCaIXrANJdEM8cNlQTVLOSsg5RTejI1irwM0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=fDMG0HNWa4Rum7DI_lWxcU2UHpYARuaX5-b8t9QlCQQxaeCa96G0ogrWUxXUZqfQzz58hRD9HnZOtMyP5riFRzcurgAEzC7GPI71LCWJd7vRDrQ-XKslnX6823I7dZnJVI_2_Hs8HYofB7B4-CcrQUHC5h3zd1ROBvlCJwkXzpyVFhw_Fqq5HUPMknMuhT9USgfjxCNPcbiaI6Vnj8BoJQoLIlS8c_-n2Lej80ejWhQ1MNDDE1ItTX7TfYGm3OBtfL3SJiGWfpNuzp_7rQYxQHJYIpY68ToZDC22iWnZHOST1Gf9tdZaCkYcGgaakbKicidyIwUEliTXMvqTtjm-bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=fDMG0HNWa4Rum7DI_lWxcU2UHpYARuaX5-b8t9QlCQQxaeCa96G0ogrWUxXUZqfQzz58hRD9HnZOtMyP5riFRzcurgAEzC7GPI71LCWJd7vRDrQ-XKslnX6823I7dZnJVI_2_Hs8HYofB7B4-CcrQUHC5h3zd1ROBvlCJwkXzpyVFhw_Fqq5HUPMknMuhT9USgfjxCNPcbiaI6Vnj8BoJQoLIlS8c_-n2Lej80ejWhQ1MNDDE1ItTX7TfYGm3OBtfL3SJiGWfpNuzp_7rQYxQHJYIpY68ToZDC22iWnZHOST1Gf9tdZaCkYcGgaakbKicidyIwUEliTXMvqTtjm-bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUSoBzefgVNAs3gXnq6H38EQQ2jUNaNas6altCbIk_HYfJ8dRl5RP0kIGOBuMWT14lXMDRUH_vtEoqTSDQ9FcBekdWThgnBlXaPcmVBBJLb1-BpYvoR03x6dsVH-vMtYsDXJUDkDGql7QlvaFK1rceHHrRG89Zq4v2koJ8VeTKEGnQeJTcHq7uoTuez285J3CxnW0_swwBwiN28clZrNDZuoA-iYmVLCIA4a5QqR9j1LMWcGbslUkjI73oq96Lbz80hWeO44QMynDChnQRqOAVAciXSCCnyxfEoXOfA-raad7C270B8qXk2qbNF8iI4eObrjPKuGVQYsPxst6Q0Zm5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUSoBzefgVNAs3gXnq6H38EQQ2jUNaNas6altCbIk_HYfJ8dRl5RP0kIGOBuMWT14lXMDRUH_vtEoqTSDQ9FcBekdWThgnBlXaPcmVBBJLb1-BpYvoR03x6dsVH-vMtYsDXJUDkDGql7QlvaFK1rceHHrRG89Zq4v2koJ8VeTKEGnQeJTcHq7uoTuez285J3CxnW0_swwBwiN28clZrNDZuoA-iYmVLCIA4a5QqR9j1LMWcGbslUkjI73oq96Lbz80hWeO44QMynDChnQRqOAVAciXSCCnyxfEoXOfA-raad7C270B8qXk2qbNF8iI4eObrjPKuGVQYsPxst6Q0Zm5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kDWoUgdlXpzWkjHXiQ6LWU0IOza36UxTdR7fErV91EnF0tHUmskMvhqfTDfn8DNxzcazEJddEW6Qcx2DC7Ss35FT3guXtVjSbMVieC8NbtdHcCp0gZenldhpsDsjE_ELXihds76xEVRIgHltdZZW4vaSE6E4eojla6kPMPSY4Heqwzuw_-F2G5PR6T40yoyvzPqveQM38KlAzuAdnfl9nbnJdU7RPcFtFHABwU9XRoegwJVRHyTySDxUtXFsnZmSyQcwd-GNQnWBT_a54mo5ut8l3YBhVkL3UmmXwVsxdO-WPPjZE08-CCBfKQ6L3oP0788Fspb_noe4XkULr5nfvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=kDWoUgdlXpzWkjHXiQ6LWU0IOza36UxTdR7fErV91EnF0tHUmskMvhqfTDfn8DNxzcazEJddEW6Qcx2DC7Ss35FT3guXtVjSbMVieC8NbtdHcCp0gZenldhpsDsjE_ELXihds76xEVRIgHltdZZW4vaSE6E4eojla6kPMPSY4Heqwzuw_-F2G5PR6T40yoyvzPqveQM38KlAzuAdnfl9nbnJdU7RPcFtFHABwU9XRoegwJVRHyTySDxUtXFsnZmSyQcwd-GNQnWBT_a54mo5ut8l3YBhVkL3UmmXwVsxdO-WPPjZE08-CCBfKQ6L3oP0788Fspb_noe4XkULr5nfvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCA5xAFap8yhBAxzlF7Jo7ElwmmgWbIIFj0E-svCg_9NCQpWcEP86YcYeyMAIGkV7O-Cfa7kxYoQ5xVHiyl5AV8RxuIxGC5LIjeUDxO9wahm2gAFqAlWEiJ1WCs-NyZQuZm6nl46o-zFIp9yClxEZoxCmbv_MP5Bz_Wa952kE6SSgegz3deuUk-dgBXDegxEO74s0EO42EyGvd6yZ2h_sg-y-u3c8FQq12YGmXMArIhGAz1IzlwxcRwpx6QXAbNMK4wnlFI-pP10TIjyxX2_aJEqjf4nWnaOXOuWj6PAeeDsHQohL0e_frCqt3jxXZgQj1K0o0FIDn_P9kEq_wtnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTpsE7xhxY_cNr03xmKkBKAGTQWF4zPjJHgMmV_Yxhc5UB3J2F-xoXj1mPgB4LPVU0NVG5T3zMbw6nsw6ng-TRuQTJdlepBQhAWPbLpKdqyPeEsFjqjUs4OK_fP1PUrWfUhfEZlExei8-VqcvOH9YzwVdjV67Af5hb5MMgt1Es_Lc0Trsy1Y7QljFF-n6bUecpnruQApjCXZnogIH-d4gVFI3qx0vsP5veNfc-lO4QaT5kKeYFPTv8DMhd74XMjR7BLZl6DWXDnA9AuoZKjl0P6DmBGO1ry-iqiQZ-ThnZo0StcjkJPr-287DUYpUNaOysW-daNBp6F1YLOe0ntWYHbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTpsE7xhxY_cNr03xmKkBKAGTQWF4zPjJHgMmV_Yxhc5UB3J2F-xoXj1mPgB4LPVU0NVG5T3zMbw6nsw6ng-TRuQTJdlepBQhAWPbLpKdqyPeEsFjqjUs4OK_fP1PUrWfUhfEZlExei8-VqcvOH9YzwVdjV67Af5hb5MMgt1Es_Lc0Trsy1Y7QljFF-n6bUecpnruQApjCXZnogIH-d4gVFI3qx0vsP5veNfc-lO4QaT5kKeYFPTv8DMhd74XMjR7BLZl6DWXDnA9AuoZKjl0P6DmBGO1ry-iqiQZ-ThnZo0StcjkJPr-287DUYpUNaOysW-daNBp6F1YLOe0ntWYHbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-oELiT5u8xW2wrRnNFsXjplG9SLulAJzElYNlvUlimMirTCmuOrmj9EqkiV__CTBPnyOyIFlgHMm2OlR98pYd12bXSYThPvNSwUFBgrEcMc4OspdTwklbllC14vCeVHdNaEAh27sK8O-TTmDDq07rOPONQhbI3xmG1GFYENJkg0No7dbyJX4jrRaj55pSNWTTWLk0z3p3-I0VV7W_m0tlRMGGYVxO9ItmDC2K9SILWOHTKQtVbARSrHQ42PRnBOURGdNJpw3yVGav2PKMuc15vUKw7dC8bfRiTAZ_Lg12M-o5FDQUjz8BDPMmecIJQelkp7WBO5SZ34b0DMJ_WYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=COvURXu9V6APsYdmceDj73GWnFgDrSTyPqf0GiCdE3wcB8XYPX2xU2UpL-uMDbLAWlbEaNHI-LLimSx8Z0K1rvoOwi2aNRiOqvZ7q9_WOaEt9yzK46H_2YPCEoTYo5I_LHA009XQHSAtLVFJKj0TK7enEMsFfsb1cFkLwEzqxZFrmExRVHhpfYkYYSo98oIkYgjgHUMDDMLcR2EdwWXlZt27r1cbZWZFyz7jbw8qlfisT_NaqyB3O6V8ZOqK7eFaApsH_7wnNHl8CjKYtvdYhxY_KxyJUxp0FjkSS7-Cdi0kjIBFmJsv9A5SQBTDeewpPlHX_f2rG0Pz3aNTB0yRmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=COvURXu9V6APsYdmceDj73GWnFgDrSTyPqf0GiCdE3wcB8XYPX2xU2UpL-uMDbLAWlbEaNHI-LLimSx8Z0K1rvoOwi2aNRiOqvZ7q9_WOaEt9yzK46H_2YPCEoTYo5I_LHA009XQHSAtLVFJKj0TK7enEMsFfsb1cFkLwEzqxZFrmExRVHhpfYkYYSo98oIkYgjgHUMDDMLcR2EdwWXlZt27r1cbZWZFyz7jbw8qlfisT_NaqyB3O6V8ZOqK7eFaApsH_7wnNHl8CjKYtvdYhxY_KxyJUxp0FjkSS7-Cdi0kjIBFmJsv9A5SQBTDeewpPlHX_f2rG0Pz3aNTB0yRmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=PKwWbXpe0iEnjNfGrNG4ryBr-5MbKdoSaVnomidfEVFAnvjcGeBjYwuDgAIdFuXNxJotAe55H9lzkQOAwbMfM5z-s9fk6DYRo7n768MCHDV_bZxXJx7BDfpRmdWpMq8mf6605U2_-iHSf8qYmhvHEsyuAHBy0y3RYhsdMHIupC-B5hjBY1k-5Kps7611fNNjnVMeP9gOr-5Baxq5fqL0jzYMT4_t_rK58F_Td8PObVCGt22no-lXUQMHc1cBAE-V9VhAWcdPkL-9XMwigtSOeUbXt-rsSZL6U1LF9DaU0snqVkzSOXz78qA8SYTVGGUcEu3jrtIPhicKVxPJ4Pb80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=PKwWbXpe0iEnjNfGrNG4ryBr-5MbKdoSaVnomidfEVFAnvjcGeBjYwuDgAIdFuXNxJotAe55H9lzkQOAwbMfM5z-s9fk6DYRo7n768MCHDV_bZxXJx7BDfpRmdWpMq8mf6605U2_-iHSf8qYmhvHEsyuAHBy0y3RYhsdMHIupC-B5hjBY1k-5Kps7611fNNjnVMeP9gOr-5Baxq5fqL0jzYMT4_t_rK58F_Td8PObVCGt22no-lXUQMHc1cBAE-V9VhAWcdPkL-9XMwigtSOeUbXt-rsSZL6U1LF9DaU0snqVkzSOXz78qA8SYTVGGUcEu3jrtIPhicKVxPJ4Pb80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=r0xnktXIYJIYEKL8ribp3mvEagma_zN-zkM6N1TkjI-_phgQ0mjINMKChwkj_IXgdlwxCg8nOOcJLuLe3eXQwFhUY4OyQuI9rwyRl8xNjTNiD-48CEh0RTSpwfi4hDnI_bQrPvJeP58e1RMo9tFZ3f5nXWRvpCVmMPb-9hZ0DBE9wAFmzltfWc_MX_UCvB2EMk9VbiO-wIsP2o5f-wMTOUSkEEN4QZSO0DdpBeeUSanKPHTH5FsibMApZkLVNt_ux_QB_8hO3F2A5ywfCgPAYP89yyzXj5jaRVh2FZ7fY8Rr3vRoPJ1J4ifwrZvZ194lNXBbhsX2ZNkDJPizyumxUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=r0xnktXIYJIYEKL8ribp3mvEagma_zN-zkM6N1TkjI-_phgQ0mjINMKChwkj_IXgdlwxCg8nOOcJLuLe3eXQwFhUY4OyQuI9rwyRl8xNjTNiD-48CEh0RTSpwfi4hDnI_bQrPvJeP58e1RMo9tFZ3f5nXWRvpCVmMPb-9hZ0DBE9wAFmzltfWc_MX_UCvB2EMk9VbiO-wIsP2o5f-wMTOUSkEEN4QZSO0DdpBeeUSanKPHTH5FsibMApZkLVNt_ux_QB_8hO3F2A5ywfCgPAYP89yyzXj5jaRVh2FZ7fY8Rr3vRoPJ1J4ifwrZvZ194lNXBbhsX2ZNkDJPizyumxUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4jX_Kr6eAbzUS4Hmu5WpTy2FOFTr4Mk3wSfEuzLWxPfsPKZWURBjESaxa5ji6konTg0qSNPSOwEokeyfA70krUgWOyQfjRsTC1L4tOVt0s2CPoSRllIr_zjsIfrTVu10eNiW7clzYOTzJILpCjNGZQWeAWON_V8WSzrfujrPl0u2vB-0pBeLm9bmri4m-q2hFX76oC1ts23IU9O1ehwecYRNKRoFgwV92w5_vLOiLOe_SAfzXGpD1yuYxpU9gqXca0_0XuL_fZdHVrnXFFMAEf7Lg_VJIqsW07ggEjtDKLVZoKqkrYkGOsb0muih-FWsTN_5CTj9zpJyvyFT_jAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0jjZs9uJGw6HQKI0n9siEU4S8i05tUow5_vnp9U2gELeU_6KiMeXZ10aGY_tR_idwUz_g2Vr5OyfN9xwsyZTMVCT7mHJZvpMs3nU9-r71ebRErxqd2KI0UBcfaYhahPEZ6iijKRzJAmjZKk8pJ3JXU44NCYMGjNFi2NCKbBlbXk2ks6WHyWwOt0-A-V3IBurqEexLdomET9ZXdM0SkhREjQiLhakBrdy0uuLRQuOBAOMaoMsrTd8Pdsi13v9Ls90RarKConyO68QlpfVd52eJXV48dReOCdnV_8yFTlobBCqKH0gXZKJRduzR2Pu9Bmlxn_a06wVWgVjNps3bRzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=U9VvOAmA2Due4I979jeg3Ycd_iGcqqhuIjsV8pffExqyApgu3RnPXUd-KFh69rWM8qE6zqo5zM3TYy6-I1T3yx4_mQnH5PBxSYfOCQ7UN-HT3IyUvNuhbuKgohaDv-1QIfzDUwJ_6mAX1DG_rO5ALIwI_t3f7IhBIyGfo-HMqyAUBGz5n5ChhnRgpEjXtmNwgp8MaJrPxpGOKCMCwEYqhCUGfwYzwnNiAbLz74c4RmKO2IxEpzxRJxWOaa7dMyoVgjGRC0wsGpBGw8aYh2p12WQDb7N1wxgJjRQ-P0sKML5WzRc7RDvYSwJWMPY5XLMUtw0NoZED7xYb4Y5sn3Y3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=U9VvOAmA2Due4I979jeg3Ycd_iGcqqhuIjsV8pffExqyApgu3RnPXUd-KFh69rWM8qE6zqo5zM3TYy6-I1T3yx4_mQnH5PBxSYfOCQ7UN-HT3IyUvNuhbuKgohaDv-1QIfzDUwJ_6mAX1DG_rO5ALIwI_t3f7IhBIyGfo-HMqyAUBGz5n5ChhnRgpEjXtmNwgp8MaJrPxpGOKCMCwEYqhCUGfwYzwnNiAbLz74c4RmKO2IxEpzxRJxWOaa7dMyoVgjGRC0wsGpBGw8aYh2p12WQDb7N1wxgJjRQ-P0sKML5WzRc7RDvYSwJWMPY5XLMUtw0NoZED7xYb4Y5sn3Y3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgADYMG2fdj5SCY4QC5tHLVcOWHABf40rA8lio5DvBhhUhSOzijEuB7tGAtOdqrggfZJHKcMylPJYwewdUg7rBVK4lzw7wqPMzLYvzucBzodCn_Y_fH2UCOMwsp0tEeZjgJPG_W5Pu8fgYTsIrR6Yp3h-QsPAdljHbkQoykProc2SxcBP3mLz1wevvcqWXaB3ExQxHitcxP_IdPxSeqncaqrkKANWKisGX1GnV3O_3bQh7VePOrZStQThP1oYLcsOFbGxG8JxHu4FMKJ0hviDa3bTmAmA1z-G6BxFHXhM1A-WenOduIJSV842dKaXGt9dV5IIOIQiW7Yu-A8ubV29w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBmmNcwTlvZL3uqjmW-QtgiCgPrzSH3lECv1ENxGJ-K20r4aejhk8vTK12Bvs9HEgpmkttqCt2PqG7lxBcK9kB-lOWDf27XfXGqnew11ptUc37fo1XvfocOAPTAIGTG-ni214IJ1xlX8VYhncJBND9MGbXpnobavGz9Gg1E0oC1NrPug-txAKgW_Q85Iww-uEDVxc0v8wkihA6cp8aAsweXbhQMCe9rUtE34YeTfrgw6tWZBYzHluyNEEVQluO63taVvQ4T-BvJt35dKm1FovDsDXIYUrB5IVBNsAOoK-Kl1yWUWXfoiAqEYUBqcY3zaI9MdV_7HAUVugeLHvL7mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=me3fHPv5aHG5NEiKkKMzJ0LM_emRaN3Wnd04ZR1r5I6a2M_7ZoksLDCxlb_Lzchz3oKB_CAKe8E6uUI_vCZDrwPK9pEVEMn1GAvUQIWEBy7oPSRhY_hUPkkRhYAsJ3sF-BMKs1Bgw3O4hu81DBczusezFhu_wNRBPcqX-gpN5n6NDP4XjVNMTPVZJ818ZJ0l9hc9nloLLzkiU4VoNmk7HhoXuAeyk_4S7SH89ASEBSbJtYmodkdj0MVzT27pRFtOdayfv3ubJ-zNhqln_JgssCdDNHkESBBKGx5MbqyEUeUvzzLUe66rI42b6QXi8y3naSTWIbqG7eB0E_qPINsDDLKp2BXNUn9UIHgP34A7sRryH_tTwG4O9AQv3dggEbvhp0cYnTqeA0qIThFKZQNe4plTF6tvtEyE_j0p7L05_hzXXOUOxMtmcGYbYBZ8uv1bdHDs8eU8pjpRr8tc25DdvQNUhpo3KujGotnvcdMH6JjmJXLlvN9ct0S6wRPUMNXGt2KcFZjIdJTNhpqqOJlWE29yEXYInaPX0RH0Cxdwa5figGs08-la7DK97Dqzaw70JprvuraGxMoVKiMNDJGLYw-3lzWm3401cBJGBjbdAAbCVd8zHXugTcK2SRyCmTRJJynaOwQO7ih8iRLeTTWtgAuOJr-T6E7EUar-9L3bop0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=me3fHPv5aHG5NEiKkKMzJ0LM_emRaN3Wnd04ZR1r5I6a2M_7ZoksLDCxlb_Lzchz3oKB_CAKe8E6uUI_vCZDrwPK9pEVEMn1GAvUQIWEBy7oPSRhY_hUPkkRhYAsJ3sF-BMKs1Bgw3O4hu81DBczusezFhu_wNRBPcqX-gpN5n6NDP4XjVNMTPVZJ818ZJ0l9hc9nloLLzkiU4VoNmk7HhoXuAeyk_4S7SH89ASEBSbJtYmodkdj0MVzT27pRFtOdayfv3ubJ-zNhqln_JgssCdDNHkESBBKGx5MbqyEUeUvzzLUe66rI42b6QXi8y3naSTWIbqG7eB0E_qPINsDDLKp2BXNUn9UIHgP34A7sRryH_tTwG4O9AQv3dggEbvhp0cYnTqeA0qIThFKZQNe4plTF6tvtEyE_j0p7L05_hzXXOUOxMtmcGYbYBZ8uv1bdHDs8eU8pjpRr8tc25DdvQNUhpo3KujGotnvcdMH6JjmJXLlvN9ct0S6wRPUMNXGt2KcFZjIdJTNhpqqOJlWE29yEXYInaPX0RH0Cxdwa5figGs08-la7DK97Dqzaw70JprvuraGxMoVKiMNDJGLYw-3lzWm3401cBJGBjbdAAbCVd8zHXugTcK2SRyCmTRJJynaOwQO7ih8iRLeTTWtgAuOJr-T6E7EUar-9L3bop0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToZM8M0eZ6X8khC6FKpeKI6RhmOiEaWRKHljsHIBO_7mI2x9LvDDk-UGYbXcC_OKwcllWcIPR_7iiIkddY9kgDW8SEWu4mamJvX5LfmroNxEeJZp9wZvIRDgjCIPXv1COArYF4EsYt9XhqeTvicW-B2AjqCZxCnj7QeDRs2fX2RIz2mOM6kr4gVu8LXGT4mQrdsPgdvjtdrRkdtTb9zvpab2ganwF4hvPQ09gy_7Eav--DRYvdQxgYZpPhpMT2g66AfKoh35lp9-aRWEgmW0oX_dF2aR7UTgBODIz4xH3A4hiOPNR0RLACjuGZ2UfCcYO000k_XL8wLRFXhodTG5dMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToZM8M0eZ6X8khC6FKpeKI6RhmOiEaWRKHljsHIBO_7mI2x9LvDDk-UGYbXcC_OKwcllWcIPR_7iiIkddY9kgDW8SEWu4mamJvX5LfmroNxEeJZp9wZvIRDgjCIPXv1COArYF4EsYt9XhqeTvicW-B2AjqCZxCnj7QeDRs2fX2RIz2mOM6kr4gVu8LXGT4mQrdsPgdvjtdrRkdtTb9zvpab2ganwF4hvPQ09gy_7Eav--DRYvdQxgYZpPhpMT2g66AfKoh35lp9-aRWEgmW0oX_dF2aR7UTgBODIz4xH3A4hiOPNR0RLACjuGZ2UfCcYO000k_XL8wLRFXhodTG5dMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=fhy3d8Evd-WF7wNJIeTuNZimZZ6pxqMzfNaYm7W-FKUKbwaPqPrB-kPQv-ASMBDEWwzvhBuVuDeoHGZZDYczYCZUQ_Ghhm4z3FqSf06dcrLUqZWktCJEE53X2Kie81Vj2OD-DcTDIptiEqj_RhJelOqaPm-RuWG6NoZCb2GrE6ttM2fseooKKj3I_8gmGIpBJI9SZkTPaGiSz-IlLJjG5_KV3JyxTVYFxW-vwbtKnxJNNsapRrTn1zk5kAPj9DSObfiLxG5V67ojTJXwtkvWoHP4QfZZbgSTkLlx1EV2DnDwlYeFTaxWw30BLHkYOQPGe8ncr-nQltqaLFrOD0T5IIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=fhy3d8Evd-WF7wNJIeTuNZimZZ6pxqMzfNaYm7W-FKUKbwaPqPrB-kPQv-ASMBDEWwzvhBuVuDeoHGZZDYczYCZUQ_Ghhm4z3FqSf06dcrLUqZWktCJEE53X2Kie81Vj2OD-DcTDIptiEqj_RhJelOqaPm-RuWG6NoZCb2GrE6ttM2fseooKKj3I_8gmGIpBJI9SZkTPaGiSz-IlLJjG5_KV3JyxTVYFxW-vwbtKnxJNNsapRrTn1zk5kAPj9DSObfiLxG5V67ojTJXwtkvWoHP4QfZZbgSTkLlx1EV2DnDwlYeFTaxWw30BLHkYOQPGe8ncr-nQltqaLFrOD0T5IIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=FHQ3jyIm1ylKe8_7UQPTafZkVkh4DRiZqPKfZYNpXoswtrWl5BGAGItZvyxYa-x8TOda7F8i_4hSZUlJD6AvQKcn-VadXvZ8UweqsdY7ExwjnqAfZMEGKMkl8YNgtI7b7teM0WGnnMYDycUcvbd9XOKTOw6e0vobVfjdGWwfp7KtpdEHYfrwtvrjSCzhVgynPrRFlZ3-czrW4cc6F0LW4tJM0qb4dKAD7GCEy61Z5wUx_Z7mZaD8GF9Lf8C6gSLRxLK6IVOZyQlMIC5euAGayQ2_gPa2WovlMIbUFaZZgxLYZvNrP-HDBp3AxrW4BvntUv1MIi3vDAw3Vql4Dgpyrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=FHQ3jyIm1ylKe8_7UQPTafZkVkh4DRiZqPKfZYNpXoswtrWl5BGAGItZvyxYa-x8TOda7F8i_4hSZUlJD6AvQKcn-VadXvZ8UweqsdY7ExwjnqAfZMEGKMkl8YNgtI7b7teM0WGnnMYDycUcvbd9XOKTOw6e0vobVfjdGWwfp7KtpdEHYfrwtvrjSCzhVgynPrRFlZ3-czrW4cc6F0LW4tJM0qb4dKAD7GCEy61Z5wUx_Z7mZaD8GF9Lf8C6gSLRxLK6IVOZyQlMIC5euAGayQ2_gPa2WovlMIbUFaZZgxLYZvNrP-HDBp3AxrW4BvntUv1MIi3vDAw3Vql4Dgpyrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNMgRY5FWRzoaYCZzZIjs5iPLGDl0Pmrm4rLpyai4adh6kvlcDnYNPshVU4qt0ohRMs0X5D_K67ZXJQ8nvKHWv7CWH3G2-cL3-9YJmay0mnziRpW1fd2di4w3eWzidXBIXBDr_l-PrFPbTxK7-QIYPY-prM2yOCk9PsSSUfEK989zEkpm6wP7yj05Bn9uJixqYxjzzInRR463XeSjSs4na7LRz-xKJb-8duKEnBYMG9Z7R4BIFnLTJQOn-vlHlHv1JxeaLddWCQwZsXa12vL6fiBHUpoga7o8-ctYyFo2_Lg0ny2GCqPMOD18G8-QAbi9oHvDoOIUTIgqkWqgzlbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Re9jKb4zTe5ceq_FLbTxAMFEyGwL8b3-y0iQWy90UhKA98EF_8t6QPQxPCwZ6xFFVkLRdnPHDDXPl4WCQ1_E-UmQMzLVxfYf2GK4i_nr6xVQaSsroulCTMdQwlxgaZ8bjDaUo7p4Ov1acj0N59Q0HeiQ30JO1JdtI4RLS7_4di2LuGLwR-hhX2ENroZL66UTCBB069rN0N_QJZLRQ0dvM-EWli24xvn4b1Vb-hx0ZPiDR3fP0Lo3BVD4TT-Wx0Amu1apZtA1gapKCJrUhI3rOJemTrWo9SVlInPJwlJlh9Xe2ex7ESmL0-3RzrVNeTlBNNhG6tLXuAA7AcXCSrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_E71S7JQxD6ZLxHnMZ461W-q2-UGVcIoutZIGErZHBgrwHxQLQtHU3JL6QIc_hnmBGL0mkFBnPWSwYLEyu-uM-0JJEPhGvNqBTzZEKggCkp9FMp_hewg0EHQm5U_P6nyHvF2TXO6__7vp393DaCM6-CP8ezID1KK9XKNLhq_4dskFJZPYTqxhEPuWd6X-vJl9_OLVqxUInFQM7d9WqzAe27PiPUI96_Mb3S0akGH6ydAvn7uAGDsp61ZMCHqS--AcWkPDgJDnUAQ1jd15kRSuElsotcNpjPE-hizZgWD3l5YZGz25VN4vAIZa2mCcx6Yg1UrpcaRrg74dUN5XauJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt3phIAE8kWfFwrHx12wjQk2p9MWu7OGAlGf6FnlYAR_8dOBQWWOaK06cKgcYd9CnrcApyEHs0dk1lkjsM7x-7vEGQi0UHDRXtgRhaLACbTdk8CdBi_o2nzNgg26qP-TeG9E7Gy9DUcs8jUp7FbUQvQwAqE1nyqYfJHqVAqNNbQt_M7BdHOqKmu09vGxPJod7JHOC14LAEsswKNHv56J-lP856dJGOZTAu5ADcgRwxlC6F4Ul3COoSgAaqXRdm1DU2PfhGyFc-Tb8zEjpEGW9v8gmxHLvZI6e3to0VRMHsIGFJig28_tsOOqQ6lfLAPOR_Yj6v1egQjx0ekhkLneYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCwQWJyFOpa3KTvnDfBVhWqTvjBACSaPtUhE0yDS283jXhJ3mBcaflCRZGgx2n-Vp7Oa0PhV71NYo9Aw6BOA1XGdGoGbAvv-12h-2aGmpJk7KEXkOucCXqFQNY-ZtK2_oe5D9eB-3BNcOcsOo2ME3ifVyzPklsG_5Tnb4LZK8Uy7JXne02FShgE5PxYajIh0NvttFP74EH9nshRgxuHcv_7oITvgXmKyQ_6YWzzpolD22ISXGwoZHZyiMCrEnQb9OlOhnis_Xj0OOMmBawOyL9ZgNhDEas1zNUafin1TGHXXAh8kNk1MniY5CoDe_x6BLrkIQxIuYfjCzJePZm2BDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=CGcUSxemx0wwaV2YajkniMcL-nvkV95XPgniYo_RIV-VV8AgyHvkzs9awarWVdoRVrT9JuiGO9JQeONNWz0abHtf8c1x1eEBmgQ1qxG9yq1jKzuuV3ZtqqtvW4v9nLrynDhZGg7zPkAxFSOKuBA4N-woGFZssjOwGiPEZrex9Xeg-yRqofK4cJ2g7gZQgpJCXUCYkhfSZCFZv7ryy7ofogW3DdtE3I4Cd0VS6ZEtF8ZjKfoUIRUKrBdM4l_l876XJngzTY33OjVMfwIhdExKmm77fi1ERmQytETAbjACvtl9YedEAHFLYxOIzO4Ipm4hpSnxIdI5FvgZKbVKAOlPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=CGcUSxemx0wwaV2YajkniMcL-nvkV95XPgniYo_RIV-VV8AgyHvkzs9awarWVdoRVrT9JuiGO9JQeONNWz0abHtf8c1x1eEBmgQ1qxG9yq1jKzuuV3ZtqqtvW4v9nLrynDhZGg7zPkAxFSOKuBA4N-woGFZssjOwGiPEZrex9Xeg-yRqofK4cJ2g7gZQgpJCXUCYkhfSZCFZv7ryy7ofogW3DdtE3I4Cd0VS6ZEtF8ZjKfoUIRUKrBdM4l_l876XJngzTY33OjVMfwIhdExKmm77fi1ERmQytETAbjACvtl9YedEAHFLYxOIzO4Ipm4hpSnxIdI5FvgZKbVKAOlPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=KwU2IAitaL3uTTqjp8vTFQxELUBX8T3S5AfSpSPCVt2rHmO4lbg3wuqHaRTCMPY33xboVaGND9zfDckoBIhn6ZQP_P53U6_n8_rpiUk7eIIXbXCRvbxqQym_OKzmacfHX1v5sXw5JV7gbxBizDQ0F2D-HHV4cb3ncaV3bvb7c8muUujytyIIpv5o_U4cWpVEJukGLchcV7bmxAZ4zrHy-97UQhs7jFcfM63yc2vxjR1bCCjL9mX5BkKDmKFoMAMP3Y-rGUwFTZmMIfv_CYvHClmqvu1kkxFmVIQ76huQ4vbSKMgmqZyTY5j_LCDs7WGx3RU2IL8ZRuZFj7VO4ECODQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=KwU2IAitaL3uTTqjp8vTFQxELUBX8T3S5AfSpSPCVt2rHmO4lbg3wuqHaRTCMPY33xboVaGND9zfDckoBIhn6ZQP_P53U6_n8_rpiUk7eIIXbXCRvbxqQym_OKzmacfHX1v5sXw5JV7gbxBizDQ0F2D-HHV4cb3ncaV3bvb7c8muUujytyIIpv5o_U4cWpVEJukGLchcV7bmxAZ4zrHy-97UQhs7jFcfM63yc2vxjR1bCCjL9mX5BkKDmKFoMAMP3Y-rGUwFTZmMIfv_CYvHClmqvu1kkxFmVIQ76huQ4vbSKMgmqZyTY5j_LCDs7WGx3RU2IL8ZRuZFj7VO4ECODQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyh4EtL8MftaJ7f47N8rUWOTpWPiVtRZ57xFVZZGWXYID8D7p5UtkPMUTCSrIMO0RxghK6pkooTXH-2XKHQ4QIPDBzTc4NpeT6FDnpvmruavh_UcY_aPeq4UA38a87patqXaQJlPQE8hgDGWos_xyOwReLzKYUJgd_P3fIur20ae2EGzSo960_vZnTYy19KNSYnkvsHmIIxsqFTOYHBnC4z3VCRqMBZOr4C5s60DHdfcNdnmES7pe9QuInOe_HbXDighqydaYx_PmH8S_IsZGjx99P1o9V2eqQ_0d5XuaIsB2UB-72rq52TmkhOwMS8gv_agbt_KE80-t3fJMLAGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEqg-im9Mzy_tDBRrtJeT6Ep-ahQp_peNsg5wMk22eu3WmqoJhPjcI-5M6dhntnHQYAVNmFTKINBeNtb_qyAMHm9Rkeo8xcBmk2CI9a3JmIPDYCgl41i23nf5Uuuk9JrrFitHiwaaGLNxASiegHKUks2CUUWQQOZy8HW5fduW2TJWwJQZaaVt-oW4OAyOlcbuKX-tpze-FGTalaMWNX5tLMl2T2GobyK45TGWNUwZuw7hPi0sgfVBtKt5lvO9xYlCjFunDVFDEJBjmsNXAAxaZ7PrrAE4tIKbtkN1M9JYnPsohU2nhMf_Pe1di2wcqrRBDnY8m0YTL6f9GyNaUKJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=uNFgdpBBCfWgqdaZ_dKFua4ybSArtEzJJuwInTmhl2rjPzDnmhXj-TLkxJbOw-MJ1Rm_nAsgHaWcK3kTvUomkstUg674El7DMlCt_3JFxYU2XMwjnXaAoswvuFWSah5rUOaSZm91KbrGxXJmthijgiPSKOEK5Z-DSabpcGRfpFopsLN9yAUdNymKyMGWDOjMrq73I0OB9CNoDEwIN9COWDoHuQeHXmf_UVZF7zkS8tYC9JAS_DETisIjbE8_Ko2Lp5E6O_Hqvwsc6Hlh-Gjg6vasLlZmMmLRBHnaOtaTdfBDje5_zE-4OErm64JJ8Ad_iDZn601B-q1uEMDSNXbOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=uNFgdpBBCfWgqdaZ_dKFua4ybSArtEzJJuwInTmhl2rjPzDnmhXj-TLkxJbOw-MJ1Rm_nAsgHaWcK3kTvUomkstUg674El7DMlCt_3JFxYU2XMwjnXaAoswvuFWSah5rUOaSZm91KbrGxXJmthijgiPSKOEK5Z-DSabpcGRfpFopsLN9yAUdNymKyMGWDOjMrq73I0OB9CNoDEwIN9COWDoHuQeHXmf_UVZF7zkS8tYC9JAS_DETisIjbE8_Ko2Lp5E6O_Hqvwsc6Hlh-Gjg6vasLlZmMmLRBHnaOtaTdfBDje5_zE-4OErm64JJ8Ad_iDZn601B-q1uEMDSNXbOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=BL5H2b2GZq9FEhADn195ldPqVU4TbdG4jUC8Dlg3jgZdOrstLjCSp0ks4ys43C8nqRH-Jaz5EzPkXmyJthGKY8Tl2vuyoZf1nL1S-O34g3_fHueO_Vhcuo748cFJl4qqN0HqMo78QV76JikxAsf5GVfGcIsBKnnekpo34RSGBjZb_okSjG4fR03FqtzNX7LzY6RuI1Y1x8HKvzRipgfAvXNvNp6N6vf3VKPBgxYdEpYH8iO1ADYIdOKqHDfoJsUXFkc8qRtLa2ENLqBmvVQ3XuJYTTjc2PoHbRnvkaOqp9EtoGwbrGNozVAW5xMFJxfglJFMvplS06c5PbPoVzPh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=BL5H2b2GZq9FEhADn195ldPqVU4TbdG4jUC8Dlg3jgZdOrstLjCSp0ks4ys43C8nqRH-Jaz5EzPkXmyJthGKY8Tl2vuyoZf1nL1S-O34g3_fHueO_Vhcuo748cFJl4qqN0HqMo78QV76JikxAsf5GVfGcIsBKnnekpo34RSGBjZb_okSjG4fR03FqtzNX7LzY6RuI1Y1x8HKvzRipgfAvXNvNp6N6vf3VKPBgxYdEpYH8iO1ADYIdOKqHDfoJsUXFkc8qRtLa2ENLqBmvVQ3XuJYTTjc2PoHbRnvkaOqp9EtoGwbrGNozVAW5xMFJxfglJFMvplS06c5PbPoVzPh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQsUQPYeRYwogENgE96rDbCMsrSVmfAh1fQb1-o7NgQELB17kEIwaUbfnn5ecdxe9Y6c4hqYKuNDGnqn0aznaWm-l-rYWO_ib63btAUkUxBDQUyR7sFgAtMa9ykAe5Vuuhy_o1akdDE_6pRBWFxp-lvGlb4MGGQElC8yqRjedC5kUKLJuy5zYuhbA2WmGh44ky0-F_TBGJOx7rFmxnndheosT1opQzMBu6pNl3bfh2V7bircTF3OXQi4WdxEE-37eoog7GuEiCS_IDrNzipThyQe83-RAuwyRtICx3cGuzAoLcVvZvtCXFM1m7jJLNmNI7YDK3wlMVSh-8TBRqo6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJocwpQvEF64EyZfIHocOZDtpGylFn_KsDuCgMeA1fhSAMe9AtvkB7qxj8Hv0olJ-F-g6PnlkJ1Kif5Wc9U_r_603AjKfyjSuQ7Bh4TTNKD7R0VAuRK3JMK9S8Guk5npSNeiSiG2Z5YUtLmb2ix_lP5ssTT04hKcVrIMEqC5y1ofBKAMpzrx44gMVnN7DS_Ln2BELYS5r5jKeA-uVKuDRR_RrPiG2AVUnYs0QrGfY5VALWwi1KLxQnrqdWQF99ME13CrpwHrrjG-qYR4AWJTNNkTDpa2MI1eFKQ2Src3f2BUIHXUJp7KtNS6IUkLnn54Lh5a3tcX42fIIzI5Ud04XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tanGiQD9-4jcBjAxSPml8_CoLzk0iM210ikGqADZDFcCh2Xr0sxitUtSnvkJH4zBNIeagO9UZt50Q7SfeG2up9FKgAw_cFCCfIhaBIvWMpFV-FyPpTGJr00XEPvVo6e1D8VSABVeSMmv7_ZobkluqMofP-o0b0ESb9koh8A4nA7N9KwYfjQfvtOCTr_9NAM1sHAHOGdjYtyPi31t8OWGDObah0cu_d89eRx8JQbJ0YWKbHBIqWMeBBh4RMtT5Rewch-YjptURcH96sVFPZ2l440XCACwy36_X8KAnD8cV7BJjDew6DPKGk7UgnXecXCdAzTE4dPkME-DCzdNpBL_yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=Uc30gbi41qbd-CypELGJwRJCtzVDISI-YoCYvgZTxtcCeZCs-Mtwf4uxEjJ4o2XKH4xM1m4UG2mD2kKQJWgDeVNDN8ZzEw7Cl5T3ZH7phLifF9dI7BogwB_hCHfVOpoLt0qeg0LECAjoVom9AAN_mIG2B3_7QYL0D5mEidkIelwRNEyXAVyWwzapDh3NDXvLmTt-CFYhxuN49IiGdKYnnM9tUr-UQqDihDmRe9k-n3e90UYdgsDPjb20-xlHLS3GWq3kOqcy04Btcp2Bfw6YCM5DYcbeCqPC10SXxs55RcvuuACsUhbdkYuMFKhbLcjLZIZCbGhC2E35iXHYECClLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=Uc30gbi41qbd-CypELGJwRJCtzVDISI-YoCYvgZTxtcCeZCs-Mtwf4uxEjJ4o2XKH4xM1m4UG2mD2kKQJWgDeVNDN8ZzEw7Cl5T3ZH7phLifF9dI7BogwB_hCHfVOpoLt0qeg0LECAjoVom9AAN_mIG2B3_7QYL0D5mEidkIelwRNEyXAVyWwzapDh3NDXvLmTt-CFYhxuN49IiGdKYnnM9tUr-UQqDihDmRe9k-n3e90UYdgsDPjb20-xlHLS3GWq3kOqcy04Btcp2Bfw6YCM5DYcbeCqPC10SXxs55RcvuuACsUhbdkYuMFKhbLcjLZIZCbGhC2E35iXHYECClLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU83jG_Eyrq3KXZkRZKCusA6DBo9lQ-eFTjO-riDUcdVmAWaOcH9Er5_C3L331lPScnsL97iHCsb50YJgKq0-TcFCB22KBM-v6UG7zmaBBreCS5d3E_XER7KENo54wGoSSSkssxUbtJgJEYy9twKZCKETEVNl394V4Q4D_v7ZjEZpnwIHn-z-M2OGPekjdyO9fdQ2eDnUgUGWin6Ruabng4-fk_87UguDT0gINGzg7YdOkE2NMRrh9cupJoQmHXsH_KkwnDOIW3lipAUQaM128aZ426laaWOn_Tt8c1xf2Wml_lHieIh8R5T4mc3R1PUyDApin53q7qvpWdZ5KliQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv28ijbanGRgEWyS5fJ-dD1uTPjgNG5tQEsBYiwSYXQLl32_6mjJCqb0gVi-devy1utr6lAy1BrcluAyJtDOfohbbyynQhsecLgLbN5_aAzCsoAPLmK7ntz2SS8Yiyzx9KVQApcNwg7fRKPZF_uGm8_QXyeNkpCWDFaG4kG2p4OGvEmTTpPPPAIqS3rg0snbS5J_zV9MJ5RXfsIczS1N_ZsUH3O_ABFKTjnIodWq5nDeLJwTVgoaLEl06J6qqpNCMlQzsIrY9kBwQ_UCWhGj2fznUeLzVOZM4we-otxReZK0QghwUrfOeoCF5caF9a_WsPjlsTNCNdzPe9cStBEIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdoobfreLV68jXMFN_Tk-dt01g4Z9jK9gSc_8v5XrAZmayneIg430vzuUSyAtW1USGTRv8x8AsesGXH1wOzBhOfePsbNdkOJxUNAx45x23Kqt7t5wV21vTjtQb_jlvuMBZN6bKuup_5FpYilCfu9aBqSQ3W8sJTK-l5Sck3z3oRa6y2oDlYvplBT6pXqXrd3v5Q6rwNiKhntxiEQGEBGiUlzE1eT3RC3dzXfuADu8FbG07FNOQW1ieB8PtMJDRg92wH0fv-itNZsZ3HsY-LSrDUFyIHGrd5RQLdIa63ZSu0CoKrsUqJemhPRwMyx_2Z1Ly3Ahhg8lQEma3GM-JpfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCb0jw3U-5n0wW901IMpF2kC-hd27S4Sqidlyj8GbGgumvB49OGcif84fh0y72IE822Hn9XLoA8qtflXLLhqoq1ne2N4yashOuEziJlcLzEO4NAyIOlNbSMIoeinPVolkdJvrEu2X_ZVmH0v101EYV81Mq4u_Ga5fJyGiJa2p8HIVglnp4PTrv1aAFaG4yw_Q2esPKZIOFMu846bqmW7NolbWpplNsEZvR8dW3_xzOeZeEoxVYCEOXwIUGchVqTOL0jWehlL24LTVQcEvCyHiLqQrIckpDDarrXaIGfUaYFKIKvqxW3uzrBB0rQXzS8Ry_6YKoj7q_DBvbRz_8nREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Upd01hDI1HNhrct7n-ipGJQAr9oSpMiMkcUcMF0CQMxFMBwIE_oLqEYsm2rZXS6-4yxMF5sTB1zE0t7Qz7FwiFoOS8i40jbvuIR6duTXpArWFeS5XixxEN4-Qg9bZwR93hZjIsROBBWhFwFem08TEUIYSMxMsDfdtVuor9ORf0TmDT4v3l8RXQNQgy_6wKscK4TV9CnFahVuonsaz4aNnnsFRHt95kf-s-KC6TOhcdKl0ihdELHTnL06xZXUDRBjCSp2Kl9UQ5dNj2CfqVw5jZmhuRqNYo_77mm_SOY7UghcrwVYBiT5tzbbZTs0D7b3xxY-DrdZiuCsIqc6uwvAcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Upd01hDI1HNhrct7n-ipGJQAr9oSpMiMkcUcMF0CQMxFMBwIE_oLqEYsm2rZXS6-4yxMF5sTB1zE0t7Qz7FwiFoOS8i40jbvuIR6duTXpArWFeS5XixxEN4-Qg9bZwR93hZjIsROBBWhFwFem08TEUIYSMxMsDfdtVuor9ORf0TmDT4v3l8RXQNQgy_6wKscK4TV9CnFahVuonsaz4aNnnsFRHt95kf-s-KC6TOhcdKl0ihdELHTnL06xZXUDRBjCSp2Kl9UQ5dNj2CfqVw5jZmhuRqNYo_77mm_SOY7UghcrwVYBiT5tzbbZTs0D7b3xxY-DrdZiuCsIqc6uwvAcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvD5F36dh8bvsLQOFeisYiVjw-Sj5o0HqW524jya3XgtcBIQBRItu68-7eLLuayZkChDGkJQuD7qSK6a1AXHY2xQ83FeUlGWMxuPAEI-i43emRGKQJMssDWsV9hntfVgmVF98X88DWFZADDe-6j44k9zwMHJ9lOtIXzzDVxAlZxQ3sew-rxGzwOCr0j1bt74yAgmKuskui5eltnOuQhOlt86H8o7AF8_BvdRctam-nDj0IOYs26kn-9dAcgDl6PINElgPfUI6bpWS-I-5djKPbPTC6g2fro47ZbCC4B_n2dSjuWZmyuHjJfK4156jdEkHKs888_Ll_clGuRz9xH5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
