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
<img src="https://cdn5.telesco.pe/file/EnJBuxfszWoaL-HsYuzSU6FxouckcfnR32clTw_UVdRzcM484bijDWNd2ZDEaZp2RJDQQhVWs5ZfgXOyLQVMzoTUc37SJNRE5iaqIxaqny37-6HSCL8ff_McrZedigrzlwErL1nTS72WFuP1rA1oKn3cmDYQt_5WKQo1819cxEMCyF-enUOxtiK7bglya_EgJKub8oKsfcaKaZOMv5vebAHrUcEX-6HWLoFA-8qQuLYm2yxJmStgT62An13BSy2KurbqFBveMQtdepEqHvuPJGuyFHVliG4O3pmJI5BoYz0AFvVJtyUYPcvf-54wckA-tExxpjOt-XAGCDlR4I7Q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 706K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 01:19:55</div>
<hr>

<div class="tg-post" id="msg-95097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0036204705.mp4?token=VOrY0Al3HkrFKi1FyHDsN2Xr1Xu5gXWykZ-965sRchTI3uTnghTfGJvaK_VpRkBA0upOIoFHTZQeGt6bmFzbM_ng6-Hcu0nYhAWjnRB2Rn0YATlWxJ2oP7KrU0JmeCfdHLyk9ZzHV2R08kj8Pzy43JrHzswe9DfHsJ4t1pSLO35SKEANaldYeo8QuReNXJxQwG5g_J5JVYHciiOLcTtrdXNkYiQQVq870Mk54JoMVPdBY1-YwylzKV1e9gL4OwONs9-fghAlssBvwsbZH1D19bDCIp48hkZLygfGK5-PNfXO-p9_k43No8kvPZgx9kR1DsQ2gQ2SMdIEEJ3kSiOvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0036204705.mp4?token=VOrY0Al3HkrFKi1FyHDsN2Xr1Xu5gXWykZ-965sRchTI3uTnghTfGJvaK_VpRkBA0upOIoFHTZQeGt6bmFzbM_ng6-Hcu0nYhAWjnRB2Rn0YATlWxJ2oP7KrU0JmeCfdHLyk9ZzHV2R08kj8Pzy43JrHzswe9DfHsJ4t1pSLO35SKEANaldYeo8QuReNXJxQwG5g_J5JVYHciiOLcTtrdXNkYiQQVq870Mk54JoMVPdBY1-YwylzKV1e9gL4OwONs9-fghAlssBvwsbZH1D19bDCIp48hkZLygfGK5-PNfXO-p9_k43No8kvPZgx9kR1DsQ2gQ2SMdIEEJ3kSiOvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ریدممممم حرکات دست قلعه‌نوییوووو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/95097" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssZzmC1yCsFlKOZ_DcrixSxPEntzuN6w4TA9lcsJ7i9x1ZRAHCb5LQOLgAnM2wqVa_-tSBCqnm9p4EL3WZv7fbNgTHFCrBzXpzFMmbg6m9nujx820t6HxaSjRsfhd3zmTCxchXuarhr1Sv8fG0u2vXJVe2mwH9PO5FzI8t3FmpXgB4pVH4r5g7G7QdipVojKFBp9SM0Jt0vsAaOFLfMzmwWX6KpVgnYiXkaXXU_nW5WCcpigVu6E4yBnAQSK4NcyPBjOuYdlm3oqpqKB5-IJIY5Ex7iYQ8A9BJZfSpR4LISFkH1gUuggbNyOhxh0UTZtVbxn09s_gDlWF0kkObj0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
آمار پشم ریزون؛
دروازبان‌هایی که تو تاریخ جام جهانی نمره کامل 10 رو گرفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/95096" target="_blank">📅 01:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17l29I9HVQpEjlBtvHYwE_tw1LoSzD7Wlq8TyB4fLHxbgdDuRnTu2-FeqvSzFUl-OPhiWpg2zOlMhq1BBT_X02qALneed_gayXeAOBT0w9oQsnpBAwKj2svvaG9BwSSuni4cvr1Q1crh4obZ1-6zyagcUi54hUdtac-gdwTxGTCNlYFkIodk95fRJpwdDfvhqkKXVBWmKWgwreb8HUnss6dvAHKamXCuVklBFP-Ti10ScuuikEgNsJ2unm5VnvE-saF7vQO29uxTVS0K2pu3AMn_hy_Szm1eqTBtRBac_it1Ve9bnqXAjOmVLS1unDrT1TU6Fg-1moLUSqZRgDyBt8uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17l29I9HVQpEjlBtvHYwE_tw1LoSzD7Wlq8TyB4fLHxbgdDuRnTu2-FeqvSzFUl-OPhiWpg2zOlMhq1BBT_X02qALneed_gayXeAOBT0w9oQsnpBAwKj2svvaG9BwSSuni4cvr1Q1crh4obZ1-6zyagcUi54hUdtac-gdwTxGTCNlYFkIodk95fRJpwdDfvhqkKXVBWmKWgwreb8HUnss6dvAHKamXCuVklBFP-Ti10ScuuikEgNsJ2unm5VnvE-saF7vQO29uxTVS0K2pu3AMn_hy_Szm1eqTBtRBac_it1Ve9bnqXAjOmVLS1unDrT1TU6Fg-1moLUSqZRgDyBt8uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
سیو خایه‌افکن بیرانوند از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/95095" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95094">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=VckpsSJF6i6aJdyVX_MgEi8M6_GZuY6NrNsbJ-PmlDThb7UUMFurxJASKzRnO4eZVEj8I8LXXmi6t-Prc-P0dzOLKP64BIWIhy5nLgdlmzQrN0ceoA99bzlBTdx1VThHXA-fXFJLzFpBvP2KAEWj9PoSsla9CoKmL_KqEiLY3WXVbAk5sFUguuCC-T7XhbgV_x8RN4lJvp3E10UQy6wa5WzctnLV7uH1FeAv62O-JdFvbPBsifPy20Izyx2K4ljr9Y1Y-LN_DS74fAxh_95w4NSJK-d-RbMy8_zkjNzKcj5Q5SFEe0tzcYbTP4Z3ktmGMseyfP_kiTDgzk9PFJ7O9ii1wGE3Tve7rOYMJiAFUlaz38zMqCzXnHIj1C1FhLLCBPxu6fPop13Z5mIrpntoFHfUgX4sCBKwtPRAbwUkxZ7WApX2ARpj4n8tg8I574QZbKX5SeU1AiRnDWecMWnljNB-4KBefoQ5bn388fB9ONXFsfolMKD22nAzvqrZBAq0KnskEk6fil2ufUs33HGScaNQ7Oa261SK1aWA7kDRiU-7QbaVxZYAkU14O1NGOLvAb32_KRFyqJ8EqpUwITbKu4jHakRzdG9JoUlMdX-AewA64nl-eSPFo6HPAX1YK2QgLTyNXcRh4K4_yR9N4cKN5tlBNLdlFRvjCtrz7J65YDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=VckpsSJF6i6aJdyVX_MgEi8M6_GZuY6NrNsbJ-PmlDThb7UUMFurxJASKzRnO4eZVEj8I8LXXmi6t-Prc-P0dzOLKP64BIWIhy5nLgdlmzQrN0ceoA99bzlBTdx1VThHXA-fXFJLzFpBvP2KAEWj9PoSsla9CoKmL_KqEiLY3WXVbAk5sFUguuCC-T7XhbgV_x8RN4lJvp3E10UQy6wa5WzctnLV7uH1FeAv62O-JdFvbPBsifPy20Izyx2K4ljr9Y1Y-LN_DS74fAxh_95w4NSJK-d-RbMy8_zkjNzKcj5Q5SFEe0tzcYbTP4Z3ktmGMseyfP_kiTDgzk9PFJ7O9ii1wGE3Tve7rOYMJiAFUlaz38zMqCzXnHIj1C1FhLLCBPxu6fPop13Z5mIrpntoFHfUgX4sCBKwtPRAbwUkxZ7WApX2ARpj4n8tg8I574QZbKX5SeU1AiRnDWecMWnljNB-4KBefoQ5bn388fB9ONXFsfolMKD22nAzvqrZBAq0KnskEk6fil2ufUs33HGScaNQ7Oa261SK1aWA7kDRiU-7QbaVxZYAkU14O1NGOLvAb32_KRFyqJ8EqpUwITbKu4jHakRzdG9JoUlMdX-AewA64nl-eSPFo6HPAX1YK2QgLTyNXcRh4K4_yR9N4cKN5tlBNLdlFRvjCtrz7J65YDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امید نورافکن: بازی با بلژیک، بازی تاریخی برای ما بود/از لحاظ بدنی در مقابل مصر، تیم آماده تر به زمین خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/95094" target="_blank">📅 01:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=oMO9ymQ5Mb1ykNflMH85GxDo-3w10Xw6jFOf0vUlloRZ8XmemfDrpNdiswM56cT8G8h3xZG8_8rAgFD2Jag4swIpk0LyZ6D5fzG5JA1W-8e7AqNmksXXCvqRqhy1-2FieCpXd-4zL8DsFgEywHfgkxdLdFwkVmXeycT4Sn_Sk2_roP3SNBqh5EGYNRp9_Qdl7TiIbf8dyTyprd48jVpqnhImMrs_HHcYApeEJ_p1M8ZTi4JnChLtF32fAAWO0ZE1vHOOW_lhyvXoIXtof7oDnY6YS-671rSF-WJ4yCQFpw7AWNNhu96sek_qhN8Gqo9kNP1QciuwNpy1r_sA5me3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=oMO9ymQ5Mb1ykNflMH85GxDo-3w10Xw6jFOf0vUlloRZ8XmemfDrpNdiswM56cT8G8h3xZG8_8rAgFD2Jag4swIpk0LyZ6D5fzG5JA1W-8e7AqNmksXXCvqRqhy1-2FieCpXd-4zL8DsFgEywHfgkxdLdFwkVmXeycT4Sn_Sk2_roP3SNBqh5EGYNRp9_Qdl7TiIbf8dyTyprd48jVpqnhImMrs_HHcYApeEJ_p1M8ZTi4JnChLtF32fAAWO0ZE1vHOOW_lhyvXoIXtof7oDnY6YS-671rSF-WJ4yCQFpw7AWNNhu96sek_qhN8Gqo9kNP1QciuwNpy1r_sA5me3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استراتژی امشب قلعه‌نویی که عالی بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95093" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/95092" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95091">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vTSCCCCsIm2uGCfGJmTbCLrt-63vpnu4z5p8Ef4n3lJghxgpjxsi3w5Jym18uJlXiI5Ti05ZAtaGU7uK_Nn-onYa1JP7FQXqM-1UUOCG_BdXFZZgui4drR-lu52_onz779t7yzw5yxdz1ZzQD2f6SKTigiVlCN4SmDE6XFiDkoc760EeVqbjZpVXzUQ9o7SckZ71P4P73-W-QT7UTSxpRr8y1K5gtPRTTR9Qs7FGAFNrLzf2cM1ilrQ5nj2KDaNyUlUJd2l8CcRe75-bJnxznwVhKLqrUngCVqcQbcipqX-msCrxwSwlL40jVvIpAxIlCSalwN4NqUKfL6-jmLAZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95091" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95090">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو   بیرانوند به رئال مادرید  here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95090" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95089">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RkkzD1Yqmp37DMnFhjFKeedduhtCdU40uPMm8VCLdqCpw9UjCHs4dTeJv58nVa9E3SMQMwbMNqYo_aAJAWLDcntHJkUMlSp72xYP6Y34VrJCGk3JvQSDsUYCNPoa9Xq6UGiiQPqXYNRfinHyiJ7C5IpVE7ZrGvoSBN0oJXvNeuXA9wh16XSWkARZC3PKVtP45ac2qDOSt3n_Vdugf8esyIFgBusgla45SK7kisZc1gw6QzRfCBXeGXli91LqgOaQoUKNgF1FJornhD5itBuPScm7lgVbxIMCk0ko6ZYDxyzhL6pINjr1t4DKyJU4yx33-K586dI-dOZerxciV2Ai5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو
بیرانوند به رئال مادرید
here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95089" target="_blank">📅 00:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95088">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csUhcNeVNfxP1-4Z_7FuNRJRVSjp1v7QHNZBhx-dwlHrLNJpXJiF3GEezNqvig8lOhxHFOdscOMdoURZO_wqtaxf8GEmhk7cYb8wqIXwGqyAkE6CrDDoPH_iumowtvlllpd0q6paIqIcMKGi02fHIBtE1PxVPuuhOWDTVTUdeSbEgHUioSMZC0ugEGkpt6EjbuBHf0sykUU_1k5sN5odEnazTdgGbl2kcQcUU5dATtnmrtoaXNvOgy8UNp0rFOqLKXf9yYKuUBsuKE1_0JM2gSBC6vNX3Mk3RNtiJIx6LkUky17956WRW-gPm6fpGB_I6hG-wYcsx_rTfzONMFfOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیرانوند و جایزه‌اش بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95088" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95087">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=LNRpI5qAeh1lc8wHnM8gRnnl4HcJOc5uhNKOl-Zi_Ch_uUpz92GzB4GwHNpRO2o-rChNmC6K4orq4hC56Q8DJExPlrGqt3ltO-pOvR1mK6G2GPjpYR3EsLStLCnuIkRdptMuYvOgyoHCkXeeMQBkxUnhaeVfPHHM8wvOTFgiKjax5satkjLosr5hUec9zR_jskBpmFyMXd-rPmiNxj6pY9W7yC5xe1f6N-rimbXZGDN-R8xvzZgz5nLsoV27pRx91EtrEmuTEg-TGoVblgop903SPBfTphr43kX-DYgb_PhfqG9Mnlx1rMyA0W9qfjCYUPh2ooPfvR_CmfGDDxnfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=LNRpI5qAeh1lc8wHnM8gRnnl4HcJOc5uhNKOl-Zi_Ch_uUpz92GzB4GwHNpRO2o-rChNmC6K4orq4hC56Q8DJExPlrGqt3ltO-pOvR1mK6G2GPjpYR3EsLStLCnuIkRdptMuYvOgyoHCkXeeMQBkxUnhaeVfPHHM8wvOTFgiKjax5satkjLosr5hUec9zR_jskBpmFyMXd-rPmiNxj6pY9W7yC5xe1f6N-rimbXZGDN-R8xvzZgz5nLsoV27pRx91EtrEmuTEg-TGoVblgop903SPBfTphr43kX-DYgb_PhfqG9Mnlx1rMyA0W9qfjCYUPh2ooPfvR_CmfGDDxnfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
💥
واکنش فیروز کریمی به سیو بیرانوند: خدایی خیلی تنگ بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95087" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95086">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjS-BPLyROQy2duslJBTsd3kvoc3KlNQ44uMvxed1zGTJetRZ6Tt1zMBunjdRdAdl08K9-_KHBbwWZSZUfXJbZ-iNpEH19e2Ez8R_L1K686y84rF94nBs4pzD1hJ1mu_VB_KlLFKLYZ_nLbhbwrINB3lCuqWgUgd797MmO0qaIRByT-YU04N__zI5ZZF2Jo1poO7J0HGtW4rvK-sKfu4cfR4kM4MFHJxcAmm94vYomjwo_UxRytRNeSm38fsbdgKMZJKr3CgvbQ4reZyWHTR4q71B354FbdpMRf1NC-efVlsQyUDmRfmmmIBPfegWmjIC1Kd6hStCkxgCZ1hbfciiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🇮🇷
زلاتان ابراهیموویچ: در نیمه اول خواب‌آلود بودم و در نیمه دوم چرت زدم، بدترین بازی‌ای که چشمم دیده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95086" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95085">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD8TmTUqp5Vua_sSrw8t7vLLRz3vezAsGOICmEYMxhHEs587-dbXSOjwhPBd0E77FaEvzXBJ-hB41mqf8gXTNk9qxBVj6KPPukD13b77iEPKCgIGwwREFuRHBIJSaGXJbckCmYyCUGs8hPmNpLpW9MNweJIwghBZZ1fmR855AnvklG9SsWsfi9WFbQlU612aoD7QYPcH6uOhqxnT6uSdLjfUvttnQYOFuuA58v_GlaDpkJ3TdoQlKrseZuzpwWbl9yT4veKssrdAqjI5UNiu-nNr0kYc3N572JXAPN2ZGUzft1eN1GhCch3nMhhjwhEOClKEtxYqAAGvwHhI0jrr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تا اینجای جام جهانی کلا سه تا بازیکن نمره کامل 10 گرفتن که یکیش مسیه یکیش بیرانوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95085" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95084">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-5v7t1aq08ZvKp2_EZxZ8xyLPavCVewZ7cdi1v--t6vHzCn5PExduglusEwaaYkG7oyAlKuskbRAVG_VhLAMNfIrpfjzo78OCU-dUydCNnCVQJQ1XGOmYAkjqlRwGLB9Z-OraLjFyn3pO1QlfDLDtxS0QsD6FtXNDOdrcso-xTQM1rdB6VltwuNa-xmsY3cjoI0rHknQ0E-dZapfTUyqp5tXHZyDlxBGYOkojL7nHE3RLqWYeNdT-5A2voglEik303pv2bicAAstv0VwhTCb_eTlk6ftTqczxmWHgIiMdxn_4AYHl2zx82ijxpkrsfU4wnkpk0xRVGOhhMo11UBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو محرم وسط خاک امریکا در حالی که داغدار رهبر شهیدمون هستیم رقص بندری میرید؟ ما ملت ایران خواهان اعدام تک تک این بی‌غیرت‌ها هستیم که داخل ایام عزیز محرم بندری میرقصن
😆
😆
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95084" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95083">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95083" target="_blank">📅 00:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95082">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evYcWf0zJxhITQprB02JL9iQ12iYAX3EcuWBTp9_I-r59yYFQn9I9uO3aAUaYDMd4yIVI59Fdfu2EsM419PSNqgQPrnZ-EOZ6p9coz9T-Vl6cx3Hffj1uWng_ENw7aPtjV9N8mkU0Z5-Q_HOSGBfezM9fw3qVo9krx0jvOjnq9bHVL2Eq0S8AAtcRAS4HiiYJ0YnZYne-B4GIFFsGMYetFiQ1BtI8IXqB2ffMQoPGfhySOUvkugzXdT20JeqJjfrPFsOoZ7rjx3kpoxQx9eGTz_SlUG6KSQHDo_wrjsa7otnjvDaiA0I0rJ44gSmSIEwlHJRw9EMAXqjzlwoUIhCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🙂
استوری سردار آزمون بعد تساوی منتخب ایران مقابل بلژیک ده‌نفره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95082" target="_blank">📅 00:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95081">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پرزدینت پزشکیان شییییره</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95081" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95080">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVZppffQVzSptH-SBznow6armIX-FQgC5NLmNM0Nl96DqupUAVJClIUozDuF1El6RJ03Vr_n0wuS4_RIU3pn07w4MCHY9iyqPmqRkRJgNzhw1rRYuAnJm6_cXwyU9G2klswwZ5oIMgJAF1Qtg2jWDZBCyCa6Qg6vt_C3HL9x_SptXKFdc58AnF31I_vF5JF2Rw3sA_YGlgRuyoPO9vt1k-tnZaEJ1STbVfF-9n8-c7MbKM_hxsO7iSCPrqScEKdO1veT-3UI_kGMOLGIbZ15RuNFXXJJ9aReQ6qhKoXDsoDb8ADJ02b7ijelJlMiImIuEeynduMBx67xuO71x4PFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آمار روملو لوکاکو مقابل ایران:
- دریافت کارت زرد
- 0 شوت به سمت دروازه
- 0 فرار موفق
- 10 بار توپ را از دست داد
- او تمام درگیری های زمینی را از دست داد
- بدترین امتیاز (5.7)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95080" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95079">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95079" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95078">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95078" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95077">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d7eb4f82.mp4?token=tXfqL32P1OCKO6mfrWpCEWWQ3G_0j-fgYlzSCHBvcyjhS2AVhkBhv9-nxz0tY3ttcUhuqPp9AJx3bx8ahzvbeKy_S5AepbIYkDIqcdzWBW6lY1MB_WxKwpDcqCchVHlF3Q1LUpiuaRYHMjdC1TvFKVE_rUOijCn-n2U4uCAzp_dN0hRUXtxDC8CDnaUM62yclpTWzVjDLxHJ01eVhnOSOw-pfd7hLu0B4enT4hnbcXPEykz2nbNlyndwN2tFJ8Pd-flzS4AJzKjXUeo_B8IzebqCU1TdJnVb6W8O2BZXPquhYY30nRU_rujX1U4wfInxE1Un080caY9m2XDdWgbLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d7eb4f82.mp4?token=tXfqL32P1OCKO6mfrWpCEWWQ3G_0j-fgYlzSCHBvcyjhS2AVhkBhv9-nxz0tY3ttcUhuqPp9AJx3bx8ahzvbeKy_S5AepbIYkDIqcdzWBW6lY1MB_WxKwpDcqCchVHlF3Q1LUpiuaRYHMjdC1TvFKVE_rUOijCn-n2U4uCAzp_dN0hRUXtxDC8CDnaUM62yclpTWzVjDLxHJ01eVhnOSOw-pfd7hLu0B4enT4hnbcXPEykz2nbNlyndwN2tFJ8Pd-flzS4AJzKjXUeo_B8IzebqCU1TdJnVb6W8O2BZXPquhYY30nRU_rujX1U4wfInxE1Un080caY9m2XDdWgbLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/95077" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95076">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ دشت یک‌امتیازی منتخب ایران مقابل بلژیک سردرگم و بی‌دقت؛ قلعه‌نویی با بلژیک ده نفره هم موفق به گلزنی نشد
🇧🇪
بلژیک
😏
😏
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/95076" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95075">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خب کم کم بریم برا پلی سالار عقیلی تو تلویزیون برا مساوی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/95075" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95074">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q67j-J-6uVMUu9ZnS32eWTB0TF6GdbbGqAi648pvb6SJ7LFxlL27nR-9lNcRQG3SHlGtJrI4-EJHvDhr1vJ90qXRChplEi83YbXGHo_32JrpBBLk-RF4MV7dcsX_R7q26bz9ZlMp-vyxQ8UKYjHX-zwIKPcguMWni7CkkSsrXwRNt5VCMquGYpJhbCf2SBrg2MuOcMGaNDnJ3VHOrZzNYvuGLKZvgMbWsyqsuKjgb2YffK-LZszXMCwriWjo2ioiGSNXqcp15aZE118u_xX_VnYRdi1FWfV6Le4HfuBVQQti_xAzxA0qh0yCeDQ9rcSpmpte6t0isYt_YYIWgHBwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ دشت یک‌امتیازی منتخب ایران مقابل بلژیک سردرگم و بی‌دقت؛ قلعه‌نویی با بلژیک ده نفره هم موفق به گلزنی نشد
🇧🇪
بلژیک
😏
😏
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/95074" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قلعه‌نویی از کوووون آوردددد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95073" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95072" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95071" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95070">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">علی نعمتی واقعا کسمغزه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95070" target="_blank">📅 00:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95069">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95069" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چرا دفاع میکنه تیم قلعه‌نویی
😐
😐
😂</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95068" target="_blank">📅 00:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95067">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترابی جقی نزدددد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95067" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95066" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95065">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دیبروینه هم کشید بیرون</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95065" target="_blank">📅 00:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95064">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">از کون آورد قلعه‌نویی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95064" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95063">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیرانوند چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95063" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95062">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95062" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95061">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95061" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95060">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قایدی رو واسه دکوری برده اصلا بازی نمیده</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95060" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95059">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عزت‌اللهی رفت بیرون
حسین زاده اومد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95059" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">موقعیت بلژیکککک از دست رفت</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95058" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95057" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95056">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کورتوااااا چی گرفتتتتتت</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95056" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95055">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95055" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95054">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بلژیک تو دفاعه کامل</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95054" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95053">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فردیناند هم تو ورزشگاهه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95053" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95052">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سناریو صدرنشینی تیم قلعه‌نویی عذابم ميده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95052" target="_blank">📅 00:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECOck7h-vNJHgA1auy-ZieWIQQcdG76iy1_fNRPEDSWVdtPALAVX8mBA0Wm0bAiMYramfYPotzj4sDPo0o_q91P4yxoBZeMIFY327FgLsioVQj68h1BdWRaVqhTc3jw_ahhIkHk2aDaG77GIxQLqD6J8F5fJfYQJF2OUzTGrGEbMRdgajJcyXwa_dJJGj5EXExCbqwJ9x_m6yO1bze3P0LWyl1utRliVNQLeW7YKDHjraDI4qKvIUwQZw-pC44zyCAioPRRjsfcfOBTPh8YIT-ffsuWddUwOctBSFAqSD64uHGESDfpOgj1UJl9ovvg13rS9KB5QHpV35WK9NMeIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🏆
🇺🇾
ترکیب اروگوئه و کیپ‌ورد؛ ۰۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95051" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فقط و چوب بهتر از بازیکنای بلژیک بازی کردن
😂</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95050" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">لوکاکو تعویض شد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95049" target="_blank">📅 00:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr7-RrTar-SFrpRpWTil2pBm6PjiQ5S4KLgMz94tWezxZpo0WWpC5FskTDOFOVlTzP6SYN1Ob-V22QAd_sKQM1SHFQMxDBAqE1Z6H_8RBmc4nfbae6d4u6iSGteXTIF7oOSv18exiwpAgu3wBKf9CEBa7UKxyoUUDbCU1OR9crbQecR8A3yLxGB2Kbf1qUdpqfx3_tXN56DK94akRqGQ9xHCcFkYyyK0Vi1VVq5dEHQspeIXBDpPUUXoy-iKMe9duhHMPFZI7kRkuINuGczCwcM9yYKODiWkywo8CQRlOkQeweX4P1FOMkEQ3fq6LIKLunYs3fsR4g7YOotu4jZ7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاع بلژیککککککک اخراج شدددددددد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95048" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حاجی چی داری میشه امشببببب
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95047" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95046">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دفاع بلژیککککککک اخراج شدددددددد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95046" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95045">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کارت قرمزززززز</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95045" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95044">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منتخب قلعه داشت میزد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95044" target="_blank">📅 00:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95043">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95043" target="_blank">📅 00:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95042">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c120acd1cb.mp4?token=FAheOg2Tv66KtSaRbb4IroymvcNYBp434Ag-A8p1hvoYzKXv7k3uBsIXcT36hQCJWv03Vzvar6HlHn01yl3rY0CqgoTK0Z-PB3mjC-GEV03J0MLQ7gwQlJXa_i4aUfVPBDoUjOLUoYtq5sl5tyddw8h8wgEF54lmYFHuW1YU8A_EaLGhGwPXbIsidWGYujJ8JtpuuCuJXgxbVYGMew--UePj3pbczmmsgRnuUHevRFkVHfeyQw0ILT2HdVSbxmkK5if3CHwT7Z4A6HHyQL7VNgKw_gKbtRMm8tZtvKnjfimw7QTfvJTaQVZjz9L4kjM07ULnpjxhFxpoJ-vIKYKlFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c120acd1cb.mp4?token=FAheOg2Tv66KtSaRbb4IroymvcNYBp434Ag-A8p1hvoYzKXv7k3uBsIXcT36hQCJWv03Vzvar6HlHn01yl3rY0CqgoTK0Z-PB3mjC-GEV03J0MLQ7gwQlJXa_i4aUfVPBDoUjOLUoYtq5sl5tyddw8h8wgEF54lmYFHuW1YU8A_EaLGhGwPXbIsidWGYujJ8JtpuuCuJXgxbVYGMew--UePj3pbczmmsgRnuUHevRFkVHfeyQw0ILT2HdVSbxmkK5if3CHwT7Z4A6HHyQL7VNgKw_gKbtRMm8tZtvKnjfimw7QTfvJTaQVZjz9L4kjM07ULnpjxhFxpoJ-vIKYKlFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😐
😐
علی مولا چی گرفت عمو بهتاش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95042" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95041">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اوه اوه طارمی داشت میزد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95041" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95040">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بازمممم گرفتتتتت بیرانوند</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95040" target="_blank">📅 23:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95039">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95039" target="_blank">📅 23:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95038">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b0f8f952.mp4?token=K8fsbev5UBTmBX8Vj5oH4Z9w5KehDHnEbDuZgu7uA_Sa0zpdl39_Stz0ER_g1tZvU5nt6xEW9kiLq2iA0PKUh89JHp4leur8M7Ie5yuU1GXrJwxYjknLgkKO8aenj9y3MxL-kpUT-n93f3uvRBcO2hobFlWgq8igcD1uXrZ0ew-73fIoJ2Ii1ktNoluuVjz9y-l2JMg8Il9QrjiRlVpjgxjL8thF4rBjSi4DKhy7K1rH_0cFSn-un4C9e-vJNdhLMoTPmwzoJoK0u4yn6OfVo4d4cVfPp3IS7ehQgUED52vO-oMSe4RnZtnSrSEQybanS0pvnyBZUJ6eJtQNTsdemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b0f8f952.mp4?token=K8fsbev5UBTmBX8Vj5oH4Z9w5KehDHnEbDuZgu7uA_Sa0zpdl39_Stz0ER_g1tZvU5nt6xEW9kiLq2iA0PKUh89JHp4leur8M7Ie5yuU1GXrJwxYjknLgkKO8aenj9y3MxL-kpUT-n93f3uvRBcO2hobFlWgq8igcD1uXrZ0ew-73fIoJ2Ii1ktNoluuVjz9y-l2JMg8Il9QrjiRlVpjgxjL8thF4rBjSi4DKhy7K1rH_0cFSn-un4C9e-vJNdhLMoTPmwzoJoK0u4yn6OfVo4d4cVfPp3IS7ehQgUED52vO-oMSe4RnZtnSrSEQybanS0pvnyBZUJ6eJtQNTsdemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم بیرانوند اینو گرفت
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95038" target="_blank">📅 23:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95037">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امشب همزمان تنگه هرمز و تنگه بیرو بستس</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95037" target="_blank">📅 23:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این چی بودددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95036" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95035">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یا علیییی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95035" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95034">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چه توپییی گرفتتتت بیرانوند
😐
😐</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95034" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95033">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پسماممممممم</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95033" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95032">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95032" target="_blank">📅 23:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95031">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bb775b09.mp4?token=eCTkLZEkKNbR8JKLoPqPs7_88Nuk_7TJT3scKHQpwd_C7lRlgTAtrIfjelQ75DrB5B7DDdGH5bHRXkH-b78vMDldKt0VWcmG_EsQf3s9c2rVAoQ6kJ5_ukmee7O4qs8RmoctmkwD_wCBYSA0ynCmmYTrEz-HyADg-rQ48xygD0mA5CmAn-RCjak5G7qiAKRP_lmowuP_o9mxjCV4JsP9Mwj5U7mweGIv87iVR0WD5-Axs0oxORoSdM21BoXzLXvFvjbV3sz-T9ldpQG0yLUL05dFyfce4aTrucgf9eel1foTiXTqv7ScYcG8S9S5V65Qc3zU1DTw94yykgEOZpy-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bb775b09.mp4?token=eCTkLZEkKNbR8JKLoPqPs7_88Nuk_7TJT3scKHQpwd_C7lRlgTAtrIfjelQ75DrB5B7DDdGH5bHRXkH-b78vMDldKt0VWcmG_EsQf3s9c2rVAoQ6kJ5_ukmee7O4qs8RmoctmkwD_wCBYSA0ynCmmYTrEz-HyADg-rQ48xygD0mA5CmAn-RCjak5G7qiAKRP_lmowuP_o9mxjCV4JsP9Mwj5U7mweGIv87iVR0WD5-Axs0oxORoSdM21BoXzLXvFvjbV3sz-T9ldpQG0yLUL05dFyfce4aTrucgf9eel1foTiXTqv7ScYcG8S9S5V65Qc3zU1DTw94yykgEOZpy-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مشورت قلعه‌نویی با چت جی‌پی‌تی بین نیمه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95031" target="_blank">📅 23:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95030">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قلعه‌نویی تریلی پارک کردهههه
😂
😂
🤣</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95030" target="_blank">📅 23:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95029">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پشماممممم از کورتواااا</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/95029" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95028">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کورتوااااا چی گرفتتتت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95028" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95027">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95027" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95026">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بلژیک نزددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95026" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95025">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95025" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95024">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3oONW4ZEq6tTPUsQFJiR-1Z-0o_q9VhAiybX2-l-U0wDzRzg3UcX0hgtYotzxJXClD6mrxFwYfQB50ydIghuFIHbqxvAi3QJco3qDpKXPn7dByGo5x1_suVTX9OwPN4TFTnmJcKioP6N5nJIyeD6OLRf8QaNFxSXejiEYEC9pjopzovkxP1QpXIeAShLxX0mvjr1m45mjpUUFhdPkRcbpo_VKGMrYq6nXwKTosoV4STlgNJNJbsIHaDeRNFApTWOVyVJIhp0tbDft772HIt53MlW_YYgCzVyiv4HXRtdYJBl7Hcg-5atZlH2oPbDcYx_mkyKPh7ytE26DL647kx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تروسارد بعد خطای جهانبخش</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95024" target="_blank">📅 23:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95023">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تروسارد مصدوم شده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95023" target="_blank">📅 23:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95022">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارشگر فوتبال عباس قانع نیمه اول:
پرچم شیروخورشید پرچم فیک است که هواداران در ورزشگاه در دست دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95022" target="_blank">📅 23:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95020">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2R6u_1ChfKlcsqp45K9bRzeSdM6seinWLz-eoTTtrWSuR1gcg2p-V_DMsGAYDOC8AuUo0oIKhv0krJYzLAdrR63WxQVQ85JH_Et-mCS9crKhNZVeJVmLiMjMyNNnGzo5cMqGfnq7OovF-v1wVXk96T8MB6opTXP9-uQEJ5062fzpR1a293E8R9sH6uxfvxcq33BRdr8zKrnzeD3ApR4bSuaBPYffxvJ5a3Bu-zPE8X4HuZhkXlJmXXpKqp-oiDW90G2gET92lCBKJMQK3KBpx9HN9-nC8MTgvjwYEvRuHFsHqSAZprZSqRl500-OXLh3kbT64bZr6o0WZ9HPDx4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyBP_p9uP46qV7Hgj84bEp8kBleQ86PEPjQvSfiRQ270Ct8yMVJzO0FYbPyUJJDukJwiMTk3aKHgmBGaRZIBRh76NNC1A4V6lrnx8Om6GGp00qmhGbEjy91sqI4blDuL0XNPPYI_0nP8HWKF8pFDTi_LtTTRuz1mZ-xOmeaX-GfrUUc1KWbzY16NLj7clXZy7lZzaNv1hPsaOQwoHbPdjO8meiwHkum8wo1mcoC-3To8AYwQO3lNratOGxldu-R-yIZNQj9Ik3-xSrGP2xKHMS6gohLRpjvFNIFuzuZ6Qm9lP08lpzbJIf31LGa8WDcOLAEOp5QRoR8IdqlWRTrrTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مثبت فکر کن، اونی که حدس میزنی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95020" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95019">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95019" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95018">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOV7CxoVhthXpYQauwp7qrgMnb7qV--jxDcGzf1Zb02jV2l_dy5Z0NaZbPEH_43Tb9K8sVRRlfPokLJV6-TdJe5-OLvJ674il4Rh1jBb71lJMqT7gWU5v_iYmzcparE9NEw5-ntAM2Dc1za9gRksGcIee1dd9ndYRojohp6Uq4lptQdmgA7lXSsYhVwv4cC0m-oKVGUHcgp9CG3pg9Yy87SpfZJraimut3hFV5npvOc4CpuX9jHTDUE4yFkpeP8IK2-gd-1nIaXS64bSAvqaaIByhdY45X0pK_-CZkBPB5bv3ENSZmst0DsVu425NqPNqkVW4-AAjAOwHLdJcxWb2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیجای ترول خارجی این عکسو با کپشن ادای احترام طارمی به اسطوره ادن هازارد پخش کردن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95018" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95017">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klmafkLmH7qYVXOxvfI4n6ZTFsqC6M1KxEE-Twe7gi1ZVMjIOY15xFFK-Ja-1-3cEXWtJGVq6VQIlZI018JqbNZalCvurwbW3fY4qsRc9TReyo2ag0gNjVr8UowMTqvF04Z7hE4F5WVzWcx7JGKN7ETZz4VCCl4-m-wzyFudv-HxH2tO0T9U2ha3zbZLC5lC6f3PSPvwGU3REEC-9IwpHCjqRYULan6XKdBYrPF_mDSHlEoyPpkZvgg2JWnK48eO8YkdmCdx3pJWzFCZvcZ8daAFYZhaP9j9aRIqJWJDcBY18udj6AB0eD8aS9Ug85MMexzci34fjsvK5ICEGgA9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیجای ترول خارجی این عکسو با کپشن ادای احترام طارمی به اسطوره ادن هازارد پخش کردن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95017" target="_blank">📅 23:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95016">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVcPQScXiGfLpT9STqNZ1akI9NZ_P0-2Mgao9EdZnbmVvAVVjTdSj4Cc6vAEeQijNc6WjP5HtGd_WzYW0zo_n_bo4yimW3aemGBHe2hvDHT0E-2PGBmUKu-f3VOQh0REHyX2jmpBlGO-F6EZ9HqsjnbpC5Q5x3kY0CWu-I42v_jZ5Cuyyg0KMO-VZy5yZ6WS1MC9YxSwg7WAnck5Kpb7IUQgjDHa8Yu8bSgknWlgArynyCKmSOwDdg5I6-3_sOxF172s6Sj6nFE5QCfaTvoY7hDElsvuukRAtKdNvG-hyQgmgWQYGdF3TphIMxjSeJnjdEcdAFyrb36tg2dYhXzchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمه اول؛ توپو میدادین ما هم بازی میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95016" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-e9LfmIo5UKp9gEsrN5Vw6kiPofOCYmjUI5xj7L8nz11tId4aw6Y2DEQG59rTbC7iX3M2pogKvuRphPYDu3LlmH4WusgbpILu53rwfJHFkvQTwDcIg-fJSIuOXDrFQ6cBxQdEvW64ATETI1X70sDSy7tvJBf3sx7ACKmNrCeDmMr2fqDq4kBAyExZZ_xeEvcVY7mlsNela1-UMMoWe0jPWBiUUrUK3JONndEVABcg8sOw9YZwVYUrQvoGEpFpsZ5svmMVWAlbhROVy2ptyx1JEelPUe2RJopYaTV2AiTHK4Qr1v6RELQYRcJIkj8_lYusuJ9kQ-KWn_tNgxvOfZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب سپهری اگه نوک حمله بود همه چی عوض میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95015" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95014">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول با تساوی بدون گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95014" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95013">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دفاع منتخب ایران خیلی کیریه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95013" target="_blank">📅 23:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95012">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لوکاکو بولدوزره
😐
😐
😐</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95012" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95011">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۸ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95011" target="_blank">📅 23:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95010">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شجاع خارکسده نیم ساعته خوابیده وسط زمین
😂
😂
😂</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95010" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بلژیککممک نزدددد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95009" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95008">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95008" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95007">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دیبروینههههه نزددددو</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95007" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95006">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95006" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4Y4XVIHah0xpi9h1T-iL0WTT_qY8ypPo-OPUGco3ZgE91ptQRgVAIcj0KF3gHGTHE-zh8sU1gdSQoI1kvaCkYOTQjbxZAPhelhFoL7PrWTzDw500Vs_WQ7EhqNvxxPssIkvklyywnRxMXYke2FNy1IKpkNamzXf3cnjlrtS8ECMddvbC449Cw_weXQ2TuMtgpk1XZZbxJRJfH4bbKHRSQoUSdCkzcatDQMiP_EvH0Pt0TMwRdT_jbCQIaUYPaQ8BAdImvw3Lmph1c4jDl4scI5lbkM3YPTGi0CAUIZWICC-Bqgm4as16yOgPRKdgY6v3w0dkVp1W6rFwpVjaSEBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون بزرگ طارمی خوشحالی ژنرالو خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95005" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاشته خوب برا بلژیک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95004" target="_blank">📅 23:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">لوکاکو با شکم گندش همش ضربه سر زد رو سر شجاع و کنعانی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95003" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95002">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95002" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/416694c9e3.mp4?token=cbiVph094HN1iCFbs6mP7KPhaXDI5K9XMibGlsaOKodO3B7SRh7__CWgQq1XbBZP1nhGJpwK2g3lleEphZ9gs1QvxQOm9XKw2D_VM3GvEoyukg6C1oFL5kUr3AxnNudQT5DnmroiXaP7gAssLyKLb0SnKdCrhLOAFf0HauYZXl6oqu83PVwodKNRORpXpVe6LGyE36FkYxuX8qq6QDO0vG4eCKIezIEB7RDA2FRejoZxLfSv0rK_fl_orGpF3dXnxoKrwT2jQQFsKldITMc83N4v_sj5R__fyrFZVutK2TXV--AlbhNpg5XNpDx-U-qwbDXz90-TkJREMicAWqM8VjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/416694c9e3.mp4?token=cbiVph094HN1iCFbs6mP7KPhaXDI5K9XMibGlsaOKodO3B7SRh7__CWgQq1XbBZP1nhGJpwK2g3lleEphZ9gs1QvxQOm9XKw2D_VM3GvEoyukg6C1oFL5kUr3AxnNudQT5DnmroiXaP7gAssLyKLb0SnKdCrhLOAFf0HauYZXl6oqu83PVwodKNRORpXpVe6LGyE36FkYxuX8qq6QDO0vG4eCKIezIEB7RDA2FRejoZxLfSv0rK_fl_orGpF3dXnxoKrwT2jQQFsKldITMc83N4v_sj5R__fyrFZVutK2TXV--AlbhNpg5XNpDx-U-qwbDXz90-TkJREMicAWqM8VjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95001" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
آفسایدددددد شددددددد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95000" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قلعه‌نویی خوشحالی نکرددددد
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94999" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94998" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آفساید بوددددد؟؟؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94997" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
