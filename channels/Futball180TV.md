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
<img src="https://cdn5.telesco.pe/file/Yg0vjgrv1Ox2Ty-ArkAxqB_5TKLeR3ZWGpdFSEFx6-OIZDkKfrwy_0R5jnVa_gzUpsOWUK1dVV-5JgBxsIHP_VTVbk73YU1FDTmCTbYpuWa3Wu83z46eCsORyolQ4irgm_pQlnFoPnG_4YpcFoSmzEtYJGq93aRc-nqxYFZMyVMCMtXFUBv3Ow1G8E9U-Q-3x09DqIX3WWNdcRdFZKnCvy76Yq0Xy92x3MeCVKzYrr6A3HpWAKHUkwk1cu2HM3Tf5YuRcUnAbQbbxhs-eXPx-Xo4j6IPSq7fHMJ_tZN5FOtJEs5HlSsliEI3Xexc0fEB_n-BMTxjqCNHAEIoXn_fhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 658K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-97644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUDpE5Z0gqi9CiItg_g0CtGt4JnyQ1pte6HLsChSX_UbgTpA-_eRQ3mG_kjPDTpUwGAuAqspySyBaHmtj9JdwveJd10ksa3C9wF-2oNi8R8T4vjtNoeLXdI-pajAL7plDqla84it9KR8LQBsilJXM5U9WvCiFbL31sV5fKNYWHGOrUfb-lzhERKk7P55t3hd9idEf8PIjxF78hmT6m5b9P36p84Y0mMNm6-q7GnigT2N_7UoGstElR2vn_pOFiMXzoU_du3kgHR1lNfbebo4P1u7kiQLIxHTqH8qFS8zynW4KzTT3-EcXTx_F3EjiaQQabhXehQqQwsDN-W64GCvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
بازی فردای پرتغال مقابل کرواسی، دقیقا با سالروز درگذشت دیوگو ژوتا مصادف شده.
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 309 · <a href="https://t.me/Futball180TV/97644" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQaDtMrdCKZXwHsHbgYDBDBMg-Y62G7x4ngOMAtoOqorfa-gvcWWpf1KM4W-pLU5x7wyfm9dogTjdUTTC3dlK6DPDWPUBTjVc1lbgnOxT4KhS59gByQaipO5WrIBND-zvm05Ub_8ttI0-01O5T-ZCkXBkrKyz-mRxyvVt6x7ll9ofttS31xbtYulGBZR9sMGc1Bdt5esjbCYxE-ABAK1LCSH_TNmpH_PsQ96gHYApdN9Tuo3NnTVuNETN6KvXxACLjGG-GeZfLiDgynTmUCtg8Ynf8S4GYSZl5gXe7VzTdfawVWspvI4aiIiAlYlW1m5Gn7PyHPQn4fWns9uw2pnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
سرمربی تیم ملی کنگو سباستین دیسابر قبل از شروع بازی مقابل انگلستان خبر فوت پدرش را دریافت کرد و با این حال تصمیم گرفت تیم را هدایت کند.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 311 · <a href="https://t.me/Futball180TV/97643" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/Futball180TV/97642" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=oAqVYqFuSeVlb5LJmD5v8wYMlBrS0rSN_s_ImIP_7JVyB0qM1FS_FB5OrWwVclw9gwSlngfN97mBmL6dgFNfewUPIPlUbxLN90dIbxwPD_m2HtGhCFEae1G2-2FibBQ9izxULM5ALBC1BT1HBJDe2o6lGj4pPehzxhhTACZR8xBivnZePVJQyMtbxz5iOZayQc-A4KWhpO-Dw-5sHfVMg40K2wL9QZefKNe7zO9NDRyjGEVNWOTUXUHlhWT1Yklcvf1467JM2rdXi1o3q8lsH9OTY15o1qc0uZMmEtkoHy_JCTSO1qeffnkpGSZ2pSkE7CYDHQbVmnuf61b88kdo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=oAqVYqFuSeVlb5LJmD5v8wYMlBrS0rSN_s_ImIP_7JVyB0qM1FS_FB5OrWwVclw9gwSlngfN97mBmL6dgFNfewUPIPlUbxLN90dIbxwPD_m2HtGhCFEae1G2-2FibBQ9izxULM5ALBC1BT1HBJDe2o6lGj4pPehzxhhTACZR8xBivnZePVJQyMtbxz5iOZayQc-A4KWhpO-Dw-5sHfVMg40K2wL9QZefKNe7zO9NDRyjGEVNWOTUXUHlhWT1Yklcvf1467JM2rdXi1o3q8lsH9OTY15o1qc0uZMmEtkoHy_JCTSO1qeffnkpGSZ2pSkE7CYDHQbVmnuf61b88kdo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇲🇽
پلیس مکزیک: در جریان شادی مردم این کشور پس از صعود به ⅛نهایی، حدود ۱۰ نفر بدلیل ازدحام جمعیت کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/97641" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که باز کیپ‌ورد و‌ آرژانتین داره پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/97640" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=G69aiw649HGhf25pf8J_4udU32DGPksvqXZ04Iil_ji0zgqXBfLSnyXAS_EisnBHQVmbnspgHDswajDcuVSE3XzX4RCfy9bIT7otbE6ncvPGZ8GeSuK3FuPLWXbUOsrvP4ITbjF_5xYFPawCI8xbH8Ishmq04ubHuREJdRS4UrLzb0mF30Lh9CibR4FzGvzWNdLbB6I0ZkMjuApsjiScQ7sMAbjPn1lGcg1PcULJvqOeuoEP9lpNGnl9UnRnUa_GQ6cR2aqZ81WmfhOjQOxPmAbAc3fO8mkHLubfjFIhq1kT8Q5ATYMlecQQomOFWQvHnscRUEIDcGuTUQMt1ZH6gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=G69aiw649HGhf25pf8J_4udU32DGPksvqXZ04Iil_ji0zgqXBfLSnyXAS_EisnBHQVmbnspgHDswajDcuVSE3XzX4RCfy9bIT7otbE6ncvPGZ8GeSuK3FuPLWXbUOsrvP4ITbjF_5xYFPawCI8xbH8Ishmq04ubHuREJdRS4UrLzb0mF30Lh9CibR4FzGvzWNdLbB6I0ZkMjuApsjiScQ7sMAbjPn1lGcg1PcULJvqOeuoEP9lpNGnl9UnRnUa_GQ6cR2aqZ81WmfhOjQOxPmAbAc3fO8mkHLubfjFIhq1kT8Q5ATYMlecQQomOFWQvHnscRUEIDcGuTUQMt1ZH6gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
وضعیت آقای‌گل‌های جام‌جهانی ۲۰۲۶:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/97639" target="_blank">📅 17:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های ستاره تیم‌ملی فوتسال بانوان درباره رقم قرارداد‌های بازیکنان در لیگ‌برتر فوتسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/97638" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZd7cYtE18rMev5kfEXWwVFA01d7X5kn98sh_zSEgnX624vptuTEAQprd-BdnezlxHt1lZCDS9R2qHM0_7zObf8rem2A9TW2vxA8ZhCqfXeHo--1MH3a2pIr7xMF-3Q9b2aIF0To4cfdzxxI00ENk1gX_WfA3cO9P17LW1bAz8N1XnfcdohPVOuBGIua1vfV74mNNzcC3M7J7DEDk3tsp3E0annCssXW9OpMRPgwWXsMFADHMzC3BQ6FAZmIvGw6MLLE_aDb-N5F6_8Xbuf5Yuo_nNjTlVQbsA5lUN8yOsAjn4LEYsG8xd1qG1A67yp37lVf6bAqA7L4mIjWpN4vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی اعلام کرد الیوت اندرسون را به مبلغ 130 میلیون یورو با قراردادی 5 ساله با امکان تمدید یک سال دیگر به خدمت گرفته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97637" target="_blank">📅 16:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sn9JzLg7BNB8D9cQPy6pynaKWttHUjtQldMbg5XG9SuQgo883f0KaDMGjc6KBvzr75I-kaTQrIAsOuYc482EU0-qNCAGZawMGToNdcQrhgCzdNALJ2IN3iRLDYDXVrGUrTwOMshzqjhAYum3d6Y6UWTKGYNscSzrgrhwytb3HfBKujSxofSbncFUTmmpFlM40cwi89dMHpsJTdu4sA5xUfx3qe6tdsWK04IKNVUvmv4rv82hmfphlIp8OWMfxAaZ4ymAFtX4JUVY4Z1BjWZ7r6CiVgOq2IePurygQKT4rjyIxA56xUM0tA-6EBRZit1P8YnAXIt85Etp_REqzYYuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCD__zBBbgpfc9AHRz2x4_abtsFUSll9a0rYjVNzFJ3nZLB-DLsMm9yR3He-DNPsXLDWxSDO3qLs1a83sldl3sQLSHSwHxOVC9IygWnEGie6nCxSvCIttX43THqgB63m73CqKuryrHfwNy8mjo_vTU2PKvHY9xTKlYRRubdvdigT5Ehtqzsns0rwg90MbD1FuOAngFYynx3HpMvN65eENsWJtjeqy9QVcKOZhVWZZ_oncxs3BEXidtVk1zs_JYnaYAGjC3ULaisNaeC_vmr5QuIU4d3YFsKN6VzicPgQFq-nY1D6EC6xVVJpjzRt6pbKuNx5bCnYxa6oRwKrauP-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ociOgRYFHUYCTYNc8Ej_2FY5BQJGnAm3sdu9-tjLiTjtzPdk5HiCZs0LrnpSdcMInsPy4E8fv0_ke_gPA3CTKlmYpovw6sDZl_qhCIUxrKJs73MPStxjbazjrCKszU-qTY78_7HZ2kMbQ6ZoIap2ishtpBU1cgzeIuapTMfaNSDy6shR0leMQfwl7xBb9GmK2xmh1qyXMCw-DT8LoN3zraS8XEQ9BYku-pNm14f4yL2D1w3vuKZclNzAg7WOAvfKZLJSn-v34UEx1lLhJoTt2S11JXmMMSlSgq6XfyWHMIpiGne79i7Ux1dP0eZUicjMsZDoAY4ccYPehyAygUB6CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🏆
فیل‌وفنجون سکوهای جام‌جهانی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97634" target="_blank">📅 16:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuPEp7WngtHZPf0Cya1bnpxSrbRa1bj-nHjT13DlSlFNLA4tBQ2d8HFoVtBrDnQkdbkYH5tNhJgXnVPYHhvtF8ht1RXGVsdcJidwe_TeJS_1YsBfknvawn4eDfNTmK_-5Lcn9Br8ex8QGd7_mxwtpfOlL292AUos5N1zvjyKWradMwrtPKZEbf05bBdIXVn7XJnmKufUMaH7UtnD8jiyKdgNXWkNVs5rx4fc86S304Ca4C1hVUkqTxMcNHXlc-maKkCT68Ehih66wBWmfxCmwPJBtspdTP49cx8TBh8mx_mZ982-xUrYxAr6PyUYM6zhTOAGgUTJtWdRoEyKR86RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
عملکرد مکزیک تو بازی های اخیرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97633" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97632">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbjjBpspj5yrPWuo2HIjhtglB_gCYulAh91PI5UCZQ4fSFXyqIlYJE4ktiY9yU4vebsZgZwZUxjf-qAaSQkXFwxyv1zGGNZhPaVZqRPTS_HJ8hXFxYo5RMZyE2PRFskWJRWmN6QdadTx6hhH5FO8uWUsC5riuLXvpceACznHAemUbWYfImVxlZqIMboddcANX7bsoOTb8GL6U6TgSJ7g5AvyLdjT9vyXb-ntExbeRJ_G8QL02WTsqQsQkU_0IBMDsBId2F41ILdK_eTrHwtbEUqzdDwyd3Pt-QfMwFuDIty94a_eLLU8TF5DZTS_cgIXSci2MIZ7VzHsLDz8pIlaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل هلدینگ چادرملو در باشگاه با انتشار تصویر خبر «آسیایی شدن چادرملو» در سایت‌های رسمی فدراسیون فوتبال و سازمان لیگ ایران نوشت:
طبق اعلام این دو سایت، چادرملوی اردکان آسیایی شده. آیا کسی منبع معتبرتری سراغ دارد؟
با استناد به همین منابع، تیمی که در زمین حریفانش را شکست داده، به آسیا خواهد رفت.
ما به زودی تیم‌مان را مهیای این مسابقات خواهیم کرد.
مطمئن باشید از حقوق مردم اردکان و استان یزد، به هیچ وجه نخواهیم گذشت و به هر تصمیمی غیر از این هم واکنش محکم و قانونی نشان می‌دهیم.
مسئول جمع کردن این افتضاح هم فدراسیون فوتبال و شخص آقای تاج است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97632" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97631">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
تصوری که پرتغال از بازی کرواسی داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97631" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97630">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های بامزه نعیمه‌نظام‌دوست درباره خیانت پیکه به شکیرا
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97630" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97629">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsDCMOyoxPQOv90uXppXtcoySJApt-LjpAyEVNMv30CSfUvtEqyY_8x6SlguVV6C83TVjURnm_laHG-uofAt0pMPCzd0fPfvaXPdm2T9dnzk0t9B_NXrLyENUPCFOY_ASVwnojNjAfeg8HFwqWkz792MiLxXq8hDdkMFO5SoRjJsT0W4j9kbTWtT84ATp4yFiYgzGpiTohwNDEGoGEt6X5_R-8lZddaF80t_5DIerPrfKor71GVhs25kppU7ofxIRpXL0UL8Np1I2xxoLI-3i9qymc_m6h5c1ioYVUQJr7-Ydmjmir3r70Tm0UPLmvf8egMNJ0naq87-O8f75oYKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
تیم ملی آرژانتین برای کل مدت حضورش در جام جهانی، ۵۰۰ کیلوگرم گوشت با خودش به محل مسابقات برده
🥩
گوشت‌های انتخاب‌شده شامل این موارد بودن:
💥
فلنک استیک؛ فیله گوساله؛ اسکرت استیک؛ فلنک استیک شکم‌پر؛ پیکانیا؛ ران گوساله؛ دنده گوساله؛ ریب‌آی استیک؛ استریپ استیک؛  تری‌تیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97629" target="_blank">📅 15:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97628">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSRMSb9NPvNeV9D6XfhZyaXAcfJHemJPBrN9DiNUnwEs3rLbuXmLhl4zfCgxaOeeSf1bnVaFMDahRsmHYlQ-Umi7tQu7lQYWVRsBMSVlRA9PHWFNA_LcRsl20H7AueGENZNdShMwjz3nfUT2bgLdbqLH4oAgg1h5oqI1-XIoAEEZoxzVP7GzteZMkUvtvZW7JG_tTsn-t8XOY9ivLtVVKfUmV490KRqggmOVb5kvPNgnw9TkWS6frVj2li6fx8wiag4JbM71ujxR4O2Z2mVGRpB5DOcwuuSUQiG_d7aHotkP3lyQwqblGAhGRjQg-PZnuKKbv3wpQpm1quZ6qyJO0vM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSRMSb9NPvNeV9D6XfhZyaXAcfJHemJPBrN9DiNUnwEs3rLbuXmLhl4zfCgxaOeeSf1bnVaFMDahRsmHYlQ-Umi7tQu7lQYWVRsBMSVlRA9PHWFNA_LcRsl20H7AueGENZNdShMwjz3nfUT2bgLdbqLH4oAgg1h5oqI1-XIoAEEZoxzVP7GzteZMkUvtvZW7JG_tTsn-t8XOY9ivLtVVKfUmV490KRqggmOVb5kvPNgnw9TkWS6frVj2li6fx8wiag4JbM71ujxR4O2Z2mVGRpB5DOcwuuSUQiG_d7aHotkP3lyQwqblGAhGRjQg-PZnuKKbv3wpQpm1quZ6qyJO0vM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جیمی‌جامپ‌های بازی دیشب از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97628" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97627">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=NI9tJynsSvfkNF3I8DcbbRNPYj3LAAogrJcWI8mZp37M1ZRHrR2E9COSv-9Xd9KNYVi91kbOn474vYpxdDJHx7lhR-OcYtHj-lfVSICRemmCDPjC0YCZJ-JM5Q6bZxQZ1LSV8Vd3KUHbgIm9FoPNTk69iMGC898_CWn2G4od6P-yM41Fv8tTreeogAItOLsmBl3UQYFVsanwoBerI9jKbFWyjArSJixZ2AtXF5bATRuWkGyIt6-brq4JchgYrGQeHtWL7jmfAU7IXInlA2kkT0Tl9kUh3xQ5d4akg2EyjflLd-YhHZq8BxiQWqIskHaFp9eXgUeO2xX_Kzm4K5Dgew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=NI9tJynsSvfkNF3I8DcbbRNPYj3LAAogrJcWI8mZp37M1ZRHrR2E9COSv-9Xd9KNYVi91kbOn474vYpxdDJHx7lhR-OcYtHj-lfVSICRemmCDPjC0YCZJ-JM5Q6bZxQZ1LSV8Vd3KUHbgIm9FoPNTk69iMGC898_CWn2G4od6P-yM41Fv8tTreeogAItOLsmBl3UQYFVsanwoBerI9jKbFWyjArSJixZ2AtXF5bATRuWkGyIt6-brq4JchgYrGQeHtWL7jmfAU7IXInlA2kkT0Tl9kUh3xQ5d4akg2EyjflLd-YhHZq8BxiQWqIskHaFp9eXgUeO2xX_Kzm4K5Dgew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژکو داشت مصاحبه میکرد که اونور زیادی سر و صدا میکردن یهو برگشت گفت هیس همه ساکت شدن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97627" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97626">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAlTaJ_QN280UjpuRAXsezSmtHE8E1jTLa88PAu2zk1Cd4zJns_HeNjOy5dhpUHyCjDf8hH7RX_hrtg--SKM85zfevf3N_SBh-QVF1g__Liz7uW26l4RQoARI9dMMad9XhuYp_tJkJGmvnPOGqbBNLTBj6UM5UiB2mcpn-FgpR0cIqJe57T1xGVPvd4n0YMHSJgnxkQ_IxqUqkBahzk2hZZ07_Z2mBG50mDSrgJvxZdR1Rjewq3-u8qwSDqodF6tZJXLXy4RDuRBT1zvOe7TCHO6xP-qTDz8FnAOQd9bJ1Z3gVaYvFg2V5JRRCGRfJ3mF_V8NAr_X4TOhNpKiZ69_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97626" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم ایران که نصف شب فوتبال میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97625" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97624">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koQOvvvSqC6dSymvRgWPHvf4gOblUWOCVRzSvjsMZhacs80hWpV4s7emeZ48q4CUjp68XH_HNVaN6kAfRo2sXTfbLvtXA-uLfckpatbQr9pzxO8GzU0RPAp__2-aW0dZ1mhuG-KULblsAH-NMhELeeBo-9y3b30ATiietZXO2rkoF1PbknWaqntGdPYKt-bHSRdPfrWNLcVHBnzVic56SA1jmj6cN5kWwzx5vSpvWjlcAY195e2uzFilDeeCphSUphGBf5JLGGMj2DlwDN8gyHfkp9QpnMq4GVb5fTUA8QYZX269McnVegxkwKH_O3mIGZihaBaBd-P9gd-j2BreyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاقه رئال مادرید با انزو فرناندز:
👀
🎙
خاویر پاستوری (وکیل انزو فرناندز):
چه کسی رئال مادرید را دوست ندارد.. من حتی آنجا بازی نکردم اما الان در مادرید زندگی می‌کنم. انزو همچنین دوستش (جولیان آلوارز) را آنجا دارد و بیشتر اوقات فراغتشان را با هم می‌گذرانند. و جولیان هم برای انجام برخی امور کاری به دیدنم می‌آید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97624" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97623">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdlci-0IN7rdpv_yWUD5af8NuHC0eeTCgOxJ4YEi1nOWHChfr9OeVUZ6LePfAgIxRM_iZYkAqpVwdIG27V9q9CV-LLeMFTDAkjQOTGmXmrQxr7jxinH1wascxn9ANHMKzcZNSuooLRPOlCLUqZXpGklc4MQoW0afxzuyUC2uIFe325uhertJPCRzck4MDdAn2tcohPRW0U4nW-DIiJwNZoqfGslh57YfP6SIah7JqPUDtem3hmKosrhUK0vzg4UkF0lTry6brQ3UGGACYmq6Sau4uQg8kiQwKZk5G7AlEV9ca1RSj65qfZFOPrvuWDZS95mKQgEBLhYLG5WkM1dOFwP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdlci-0IN7rdpv_yWUD5af8NuHC0eeTCgOxJ4YEi1nOWHChfr9OeVUZ6LePfAgIxRM_iZYkAqpVwdIG27V9q9CV-LLeMFTDAkjQOTGmXmrQxr7jxinH1wascxn9ANHMKzcZNSuooLRPOlCLUqZXpGklc4MQoW0afxzuyUC2uIFe325uhertJPCRzck4MDdAn2tcohPRW0U4nW-DIiJwNZoqfGslh57YfP6SIah7JqPUDtem3hmKosrhUK0vzg4UkF0lTry6brQ3UGGACYmq6Sau4uQg8kiQwKZk5G7AlEV9ca1RSj65qfZFOPrvuWDZS95mKQgEBLhYLG5WkM1dOFwP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمجیدهای زلاتان و مورینیو از ایران فیک بود؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97623" target="_blank">📅 14:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97622">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un7ldE6mFKyG6hwiiYLLWs4twH3mnBh5zx1p3xWbl7HwHIbxaNOSDNc8r914DuRNNOFa8-PsFBTb018M043lQtYOfOC4eC546r5Nmak-stxz9Dx8TyA4dzgk5b-ThUx4AtGyr-srfeMpBss4b4kXf4TCf4KFJTD3INFi8fEAho7kt8SjyCP0ng8YN28q9_ees1rIZhfQEgwF67P158zl0I-fJvbWztWvej7yD0wAkPuOlrEG_vvWt2Ej-e020F1zo0bDmZ5l1dKj12ok0UuLUe29a7fQtoKL7S2DBabJyKRTR2vs_tDygF7THME2LFtCyApc8i1lkbQLdYj-3kkznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فوووووری
؛ ترشتگن با عقد قراردادی به تیم فوتبال آژاکس‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97622" target="_blank">📅 14:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97621">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl0sQXYgrPaV71T2132nZeEhIiQv_l6lzpx2k3s3JZqzg3dQ81dnQ_pbyCn_h5OM9a5X4-Peoh29HVwozEgKkua0mR-8NBlIiL7NBZiRl9cpLujX97vCaJZ3VXDleqRA560RoyHP7Ysk-d0n8BIgDI-QEGrRxa7ta2901Hon1xoI4bK7Dn5SdNX9ID0ygRX5PXbsKbT78u6pPcQtA6tKRBQdub591pV-4x_RqWEwykQLRz4pBhM97TL3KtdFOSFK5tjbEsADUisidkZ4jANRATgpcT1rmxoS00pLTLsfq2wCWtXYEYHQ3orNG-Zvfhd16MwH_ps698hEaUZQ22zFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری #اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97621" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97620" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای مکزیک از فوتبال یهو سوئیچ میشن رو بوکس؛ لامصب چجوری همو میزنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97619" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ6pK0I_kW21hWcCjMnywzd7vEw7RL9E3WW_PT7SLHk0Dsv2cg-s3O7frpkLls5xfbAEd0tWy1Y4AqpwYpPJEd7lxdffhGkLrEnZEncME3Ya2_cvH-7sCBLeeKR8-rtaNTi9Lrx5qO5otXsZgWQNySemJdMmAI9YqP3xkftxHNQp18Sy-atT9UuhoWEMaWB2yVJnWqq6kOfFFsR37Lco87drBRP2xOAXxEx8pqW-Y4lQ16DX5dO2haEDKLI_OLWIwPfxyTdu80KLVICIGTY1d-FKUHSasIBP9Rv9LYpEThl1fkYctW1f_eYLCh_g3XMPt7a4yeN58Iz0O-5eRPWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی کازورلا از فوتبال خداحافظی کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97618" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afhn1ffJ9ZPn1w2JVvP3TcoSy2ieN8s7Gs0Y_PZSnQI742BciQsb6yZguEwHX3HMwFaCUB2GYWPNaKfrdE4yKmBtQHgMWcJLG-AzPA2cr4rIhmru69LEH3uAO3OdhaTtF9K4wpARDjFENl4pJB2_rO0PqrqF5BAt8FQEmGVsccgCuQUubFeMf2Y2SQsW4AfiKjLlYbfV4gFe7dVuZ1idX-QywDvwsc5ab25on0FPS3HkVGNKqDHQV98xJK5C1HaQXCQjjnMFTCA_36wd35Thsb8s8TSD9BYlQxXpF5VzvsMfRIXDVU-GfgfqU2UI8Wrl2hguoy3um9lShyry2bxiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🔥
مکزیکی‌های جذاب در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97617" target="_blank">📅 13:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=jCuOzxmc43Szg-dXCwuUdVltI5EzOpUeAPp1J0Nh4q9tyTp5qBZuJn1krnV98sMhqdSqd2JzWd4d7HjGGsxpyri3gPoLMTm_J84UR-wK97CaIH30OG8E3MCAfRL9oHrU9AJoZSdnlXx5BPtNkq1gL8h7HneM-BEowAtHg_xJQrZDxLzrygKp6HgEqsyi4vFAkHWHsnD-KwgeVWEWKWyXLTpgbzGmYuzsWesKj6ESXuW6vbrF-ihvwqIW0VyKNOZ9XSYMYYF8XCPhTcM5_UsYwCwUHd7LrTWBYiqkQGKfNT36il-zh8L9Yn0McYWzYpDSmDzUgBqabqtB1NASPMMKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=jCuOzxmc43Szg-dXCwuUdVltI5EzOpUeAPp1J0Nh4q9tyTp5qBZuJn1krnV98sMhqdSqd2JzWd4d7HjGGsxpyri3gPoLMTm_J84UR-wK97CaIH30OG8E3MCAfRL9oHrU9AJoZSdnlXx5BPtNkq1gL8h7HneM-BEowAtHg_xJQrZDxLzrygKp6HgEqsyi4vFAkHWHsnD-KwgeVWEWKWyXLTpgbzGmYuzsWesKj6ESXuW6vbrF-ihvwqIW0VyKNOZ9XSYMYYF8XCPhTcM5_UsYwCwUHd7LrTWBYiqkQGKfNT36il-zh8L9Yn0McYWzYpDSmDzUgBqabqtB1NASPMMKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ما تو ایران چه کار خوبی کردیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97616" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjdUZEE24Nod2R8H3pI1GDE38MadHzn31SL5uhXarwmq02ZgKPR9Reb5_NdFu5Wg1WFs_Le8v3r0BHY2lYjOLyz9eTyRDIsYEKq4Jf-_bcG1hm5ADMGU1dKQqSGP6JmuHXd8LGYxCZAoknx13OYdAM410JJFJdCx1DZQc3nDfuvbgW1XT3Hlq0hvHoSlpky3dHdWZ4UzA0XU_SSahM8lrpM_2_W0NpdNTMXKl2EHyrBdkF_yQsJA3wUT5F8e-q8xgA4adjijqT3waNFCPgUQZsqD5J1OenWBD4TPeKsOKXX_WtkSrzBoPrPy97VCTgL3DhsXMhz4OmuSEtoX4RTusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از حواشی بازی مکزیک و اکوادور
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97615" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oLOy9QlxQPwhyUOOIikkdfVlKSexav1BgRp8442eykpqq_mRxhkYiW3XkG-hF-T6sIUZ8hx7aNPyRu7PZmxa0UTUn31rAWeSTCdVm0wICDY3zv0uUEgpLOCn4_dM5SgZHZcJ9nrJ2Pr8cLJBTZoNujST6Kd7oDVL61wbOT1txCv7Oerm4OsZfZFJpepAjwlI6xirRxbWE-wOO76XOStFYtRdFkD3fzTD8T1pN27-3XABawnYULtD_TBe8Nwb9zT8TrAjbXBXBVV8eVB0xuYV0jQ6y694fKeaRHyql20gtrNi-pCvs0B85MNbvdCeHn25k6mVs6XQ7cb43-uuXK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرناندز تو تاتنهام شماره 18 رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97614" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
خوبه کشور بنگلادش تو جام‌جهانی نیست وگرنه با این هواداراش سوژه رسانه‌ها میشدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97613" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAM_RKzIGYyaP4zTCthA06LCZ6QykEeulplMXykw_x-7lAI0Wd3HnItprs6KYuidwwfPAZ00v0PyTdPoidj7JYa3BtMsC1UwBrnUzsNGvDYIRPUq_V717akN6WlGWHBxkM6mLvwj8Z33crhALrbHfhxh3snt_K2lX_uBh_u-1uE_unukMmIya9DIMMaO2xPyg4MD39lNE-dld8Lh1PkAMwFteck_ldbPhlPXVASKS72V6wQ7stB0nRzBMXk_EM8f77TC-mV9JANoPGJlNR7Zn5HAAFEQYQXn0oI0kBl-16veDns8ZTDiu8luIpxeqN4vup7iGPBLBYxisygDLE5Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی؟
🔴
تریدری ولی همش استرس اینو داری ضرر کنی؟
🔴
یا کلا ترید بلد نیستی ولی میخوای سود دلاری داشته باشی؟
هوش مصنوعی TimeTrade این مشکلاتو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و به صورت live و روزانه درامد دلاری داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97612" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhxRzSxeg_-ee65Xy3IhVuktsJFSCMe6psR7Y5Ou81dd4sf5CckOkamb5glRbn-zdYcY226Yl3NQG00EZt0Yn1J7Je8xXBm28tLQORfCSoENzbPQ8Cida929TR0ATskSia0P-2_Xie-pM3tkGYYD5gLzVFolOH2hd-YTpfOjesB-5ag6NWXq2qjohkQ2COyj8g1-Bq8rAxIrNbjt7XYvjkFRU8j2B-0Sva9KSCokXzrBvy7cXwibNwPZZB4uKtJRo2tFy_sJoLma62qz2lbL1dPMiipritDkTMlEQXRVS1MbXlRW1Odm2hZs8MN-RPiWvWwgfLJDNKiiMugs6Ct7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
#فووری فابریزیو رومانو: متئوس فرناندز به تاتنهام؛ !HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97611" target="_blank">📅 12:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97610">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EERB2GcefyKp6FlC3uZXb1fs50wdGy5MZOm8WvCWu5Rlpp_6Gwx0sLMoh2CcBZQpKdTo2FtFkHbgu_ayOx9Pyxf0_0BK0xgokuBGr6FcPHtD4z-uqFJDcPqNBwnU_GK9eeBbeDyyfC7CN8nQHsU20EqEtzdqssLJyby8mBrCtyh_x3aVgySXGbe3UJ9S7OVbRXAz2h9A88dO81ZPmNQaDpJwtMwCrzZiYuXSs_IodEnW57VQV5m0aKnQvxEBAxPx4CJEOAhdU3tgiLsrEoklHMlFRdMya4jJjb1uCee_f0evJtlLjHngjfNbJwL33jll3q9GJswJKeMCk7l8i1y0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از باخت کنگو جلوی  انگلیس، سباستین دزابره، سرمربی تیم ملی کنگو متوجه شده که پدرش حین بازی با انگلیس فوت کرده و از دنیا رفته
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97610" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97609">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drl9zykZh_Pp4m_WQY2EeGvXBFjV-hemhE3QPi8uVs0DVa55o8bl7wuscrPTWZO5mpb36Ml_jvLhir9QZpOBTfOaVMFM8AUfhiX3m_ypSPonHrRggV3EQi5hm9e2Z7SQfRR2QqZIywksTv50SbeSakTpA5tKal-4GPQyI1AePi5Ofom_4J1U30xOQC1naT87BIDGoLj6B9FVtitedWBdxda0CBHHk-uLZC7y5bc3Kiimlr3KZFdaid2kL3Re8pi7Usz-8A-KWaynJXsXXXa9-82-3-KTXCme8Z8J5CG3YOyFKLOQQE_N4BB16-nJfJEFUYcU_h5Z6mY4F7ybmQoTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🔥
کار درست مثل گاوی که بین خواهرش و زیدش رفاقت به راه انداخته تا زندگیش بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97609" target="_blank">📅 12:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97608">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
🇺🇸
پرواز جنگنده‌های آمریکایی بر فراز استادیوم دیدار دیشب این‌کشور با بوسنی و هرزگوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97608" target="_blank">📅 11:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97607">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97607" target="_blank">📅 11:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
ژاپن، غیرآسیایی‌ترین تیم آسیا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97606" target="_blank">📅 11:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDqJofLqEeUXS72OlGTk8PoDSmEQFXXTjnn9hrOZJ6WkIeGmmWEGj-JF706CxOk2f9Huu0nnrhPeFoXDV9la41I_uq7DeiEnp5g3iN6J4_fBcSIUQw_9cOBSLMHGHFCAYOeqhcRXT38SyTBW90X3gQ2V1e7a5AlM7470X0tCA1RRQRqTtzqU8DOBiDsQRAh-PE7KD57HZ3A2Hg5w-YWSuAcMy6r2MhephzOsa8m1HdLc6O6YCEoJfEchrR6ifDBu2g084KjSuutmvmOxnRNeIekpaOzUpB039hgJ6wxlP--_wKM2kvCTZ2zlTtzazQjvn1DmwHZ68L2fkdAhDPWlrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری - فابریتزیو رومانو
📰
|
🇮🇹
— هیچ تماس، مذاکره یا پیشنهاد رسمی بین رئال مادرید و اینتر میلان درباره انتقال باستونی وجود ندارد.
❌
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97605" target="_blank">📅 11:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
آموزش رقص‌ توسط ایرانی‌ها به هواداران مصری قبل از بازی این‌تیم با استرالیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97604" target="_blank">📅 11:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97603">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgiG563rUtKuP9ZbZxnCWoBG44yQUSsowwOUsdmBjQ3kZD892II_qJWykw_b4SZbLeAvXjYeH6PORscrO2OT2ZW1av9VrH6j10YBqYuFPfQw6R3qQLuVPA5IE-Gib5RzRinWoksOZ_9go2Qymr4ybozoCv3t3TlGoT4dK04iQt21-vYoBGGT55w3LLHxkP-0s2CmE4pRz6gUZk6UXBSUU5UsQHPAgIzVSo1sqCNLIr_fy9FY0NnDrtkXqvV7vJaJjZk1Mjcf5G3dVbp_7nU2kzW9MvdzF4LZndoE1AXwWlltr_30cnUNflpY7CPuTwhds-2NKc5D-p3jYjN64h83-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
#فووووری
از آاس:
🇪🇸
سران رئال‌مادرید پس از نمایش درخشان اولیسه مقابل سوئد تصمیم گرفته‌اند که برای این بازیکن تا سقف ۲۵۰ میلیون یورو نیز هزینه کنند و رکورد تاریخ نقل‌وانتقالات فوتبال را عوض کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97603" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97602">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=aVd_DP__H_K4Yopk_69ad60S6K2JmB4I4L8gG59Xt5N5jvmYqOLmkslf7AbQWKw1ob4w07IETQV7uxDbGJhAhUSvIjDUwHIZnKKPeGT9_4GnCQu4dPA8fYbeu7Gkbo2NZ67PS6HKio5oE-mRHntkneNB-No43qGIYlbqjdpixOmvMn7IpSztOQO6k7ryZ5oJU3vjEvH3pClO6C6_MSuMG2GkbLaOFyuTcyNm86bJUXBcGPQk-LqDmqzoMegLRbzOUaudlSWGIrDOD7HhrHuOXpX5j_zgli_59rKSG80y9JezQKwpALqCJEo7v0Fh0UJNwaAvYMqRY1mbScGBtENmew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=aVd_DP__H_K4Yopk_69ad60S6K2JmB4I4L8gG59Xt5N5jvmYqOLmkslf7AbQWKw1ob4w07IETQV7uxDbGJhAhUSvIjDUwHIZnKKPeGT9_4GnCQu4dPA8fYbeu7Gkbo2NZ67PS6HKio5oE-mRHntkneNB-No43qGIYlbqjdpixOmvMn7IpSztOQO6k7ryZ5oJU3vjEvH3pClO6C6_MSuMG2GkbLaOFyuTcyNm86bJUXBcGPQk-LqDmqzoMegLRbzOUaudlSWGIrDOD7HhrHuOXpX5j_zgli_59rKSG80y9JezQKwpALqCJEo7v0Fh0UJNwaAvYMqRY1mbScGBtENmew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
🇳🇴
اینبار تقابل دیدنی گابریل و هالند در سطح ملی و بازی حساس برزیل
🆚
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97602" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لحظه ورود تیم ملی آرژانتین به میامی
تفتیش بدنی مسی و در ادامه خنده هاش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97601" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
رومانو: فلورنتینو پرز برای تکمیل معامله اولیسه دست به هرکاری خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97600" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9d1TmSCw5A0m0vRAuwNIft-3GcYsdCfuvhvKbKBZl5t87EtmNe8XbOREtbDeF91qC3xj-fKdJtBVKQ6V-zpQNL9kErr_9KTvgUsYVZc2BI2_zU2BgAMFKW5j5ihUEPE1FM4Y7VbGevIR2C2n-FeZvJA9cCre8VBI7qIzv3VOuNWhLNLBuMd-1XbAsPXcVGS-y6-Po5EWE7eLrIEZV8zHURyOXCE4ChB9l30sGcjCZLt5ZnJOoVwaa1ZFUnN66rLa572vROdwnmvTlHNW4DykV44iI6d8B8r--lveRZMpNo9dv7ZEOCmcpE6c9Kmw8xhsYlaX3dA42H1qVxVsuJ5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97599" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97598">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDKL5ufiwTN6Uzl5kP0hwY8UHrb5uQWUlx0esIpObsd0kyhxKPQtiEtyeEUM3MzeWz2Y5s5JMH4eOKynPBOLBgX_Da-FeK2308lKzYhmhItxwFReYXuFix9LcaBXnKonNk2JjClJwywTrHrE1G0D9T-a_GGVu4hTgFh-shQsqr_vszd1eZIjbvWNVmchN-Yuvc_Qia-y0dKLF5_c02V5zRL1KSgcZqVV8x_LXjXZx-gq3XqZjmPldKb2y9cF2ORQNDznnaqJ7LMqbwpE2evpsLabv2kzQP-SD3hGod1Jl3RZfJdSm6gBBhd7AFGo_vWAyYhtdWpYGcN-u1kmwvJzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری
خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97598" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97597">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T82AG2U2yTtC39dfuj48n2C-OJuwoRZOH-17EHkFDYv8LU3slpW2mNwCehkP0MoG2iR61e9id4ya1LQUD8YbjlRUrhrMRq9oGLf5mVAG5WaE2Qn0lJOsODhGB4uaVaqEsNVBU4C9T9ZTKo8dYz1oFmwKJWimzJ2ZimKuwUKeYAVYG2etyQOiaRLB9FYW8a4M2dA2RHjeFVW7IMcVQLVrdexBH0ituCuEbhewQL3Zw7sWzzWKai3InDov3R0ChIoz3D0t1CFSs1tObJUICa_EJ5fDdp3HeqhsqCewUZ6EK_2be0b1coXz1AncE29wId3KAC21DDbCEt__PehGAvVbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97597" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97596">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=d0e9lJFMlt2v9f5YmAA51R6vz-uHk71yuDynw4OomDTbRN_hxChHp2tjMkMj57lvca60r0imkjbtGVioOMC3-sVvqhfsqm8BbZPu3x_Cj0_pjx1wd0pyADuul4RAZKkzNBuD0V0a0JePxaL54IhAw5MyF6OLzm7GM38uTDnHCuuZZL-YFkqYuwKzYrCbo_xHAcQEJspv2w9g4bT17Dxrx_VflBBXCwehfgdlKiAqiOc5QyTYIKYH1Af-t4Fq-7ZzEyWWoe_5TXOGE9HG7KqluRxFjlYA4CGlZ4pgRtlTgBYU3W2wMfISWkErjWfDE38qZQLaml97WHrhFD8-hAUHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=d0e9lJFMlt2v9f5YmAA51R6vz-uHk71yuDynw4OomDTbRN_hxChHp2tjMkMj57lvca60r0imkjbtGVioOMC3-sVvqhfsqm8BbZPu3x_Cj0_pjx1wd0pyADuul4RAZKkzNBuD0V0a0JePxaL54IhAw5MyF6OLzm7GM38uTDnHCuuZZL-YFkqYuwKzYrCbo_xHAcQEJspv2w9g4bT17Dxrx_VflBBXCwehfgdlKiAqiOc5QyTYIKYH1Af-t4Fq-7ZzEyWWoe_5TXOGE9HG7KqluRxFjlYA4CGlZ4pgRtlTgBYU3W2wMfISWkErjWfDE38qZQLaml97WHrhFD8-hAUHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یه زوج روسی معروف که صخره نورد هستن، بدون داشتن تجهیزات ایمنی و در سکوت کامل دیروز به بالای برج Empire state رفتن و یه پرچم با شعار "وقتی قدرت عشق بر عشق به قدرت غلبه کند، دنیا صلح را می‌شناسد" به اهتزار در آوردن. پلیس آمریکا هم با هزارتا مشکل این زوج رو به پایین آورده و بازداشت کرده. حین انجام این کار، تو بالای برج پسر از دختر خواستگاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97596" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97595">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=IuGy1R4KQGviwQz43FYWzApe_lvvoEbLSsjN4Y3PhxrS1sWH8PSwf61YqVbC1m6BpkPc7DSqw7n69O6jDHy4j-2HlWwxBqWox2cbVl_g8OEyzHsCS7pFYLWZ46nuZPJ8z2bPwecgrhHhdlCqWQ15ox9I8wW2PZqmMf6-wKZH6frX9t2wmrTPQHf7HyJlGDoIHLeV-ZZg39Los_XGs6VexkBZ-0xH1lyMXBg8EQXgFZhyOzaDwP_ccAVEREX13DIGLpiIifrhomOpuVnK_jPSo51FfdLe0zKNhZZYEbkCIlcZuvvr8XusH-_CJ5RAS8z_QveyVtSj86f1GtCkPhW0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=IuGy1R4KQGviwQz43FYWzApe_lvvoEbLSsjN4Y3PhxrS1sWH8PSwf61YqVbC1m6BpkPc7DSqw7n69O6jDHy4j-2HlWwxBqWox2cbVl_g8OEyzHsCS7pFYLWZ46nuZPJ8z2bPwecgrhHhdlCqWQ15ox9I8wW2PZqmMf6-wKZH6frX9t2wmrTPQHf7HyJlGDoIHLeV-ZZg39Los_XGs6VexkBZ-0xH1lyMXBg8EQXgFZhyOzaDwP_ccAVEREX13DIGLpiIifrhomOpuVnK_jPSo51FfdLe0zKNhZZYEbkCIlcZuvvr8XusH-_CJ5RAS8z_QveyVtSj86f1GtCkPhW0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
اگه قرار بود با مربی ایرانی بریم جام‌جهانی بنظر این قاب برای عموم مردم دیدنی‌تر بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97595" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97594">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97594" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJkk1V9_xLs06P1hypH68_pnlqYyXeMY2s-HHU7Sm59VsKkX6anFF_WPO6K2o6l_gkOCiv_hPaJN9-oMUPoe-myLHGtKL56QFqANqtg7D-vG_Tilnafd1oTf2sreXGh6qJwLf8pwwcrIzKdqBhkKs7znzxMgQ96I7AneDZyJfeDmsx6cf7o91vVyrDlLkIFm_utKsPIbBeCyZKonXM-9yShoAAubwe-OsikzBczzr20_rz8Lbv0AjGowYE1mD74H9d2cxKQ_8j4iPSkgRTQyHeUjzQtRLCQOH1EIFvosGMtK93pwZO-GO4hWNf5t6iceUWF_-Rhl4gI-qwU1mlFnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فلورنتینو پرز حسابی عاشق بازی مایکل اولیسه است و رئال مادرید هنوز هم دست از فکر کردن به جذبش برنداشته. توی باشگاه، خیلی‌ها اولیسه رو «خرید رؤیایی» می‌دونن. با این حال، فعلا بایرن مونیخ اصرار داره که نگهش داره و قراردادش رو تمدید کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97592" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRKBmGruQGt5A5yJ_h27ChuDrOqMrLrw3jBlamZhCZJwGcU5CCog6PbDRksHMPqaZ6LHvNBUMKPgJMXzj43CkhbaUWicWQM6BsIA16SMMCQNEsoMFXd6K-tJPI-zyD5xUCkz1q3kMSUCwIYQAj4LQR0M47hBqTJQa557Z8nIBddhQVuhSrWwPN3-hB3eBpzeL40QJTZq-89zNyhqMb5fgravM1aRSW5EpX_I5f09ZT-y4Ij4b1ngz409YEP1hQCDhKdyFttLuqb3iIHYo0ezDg4bjIrKTz_SyiD-2uD75fkLLFtlB2HkmpfGQ8xqi0hHC_ydMi0_fetiCA8GF2W0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0hVbmYADjXeJTKaI_OhARVdBoXYlNNo46LlN4i_VXkKP_Anwtb6o_VEN842uEMFNSJutg1QHekrnwpO_nEzvcS6nhujSOE7lqHB1uwbTx5JdAhKKwCZ7od_1KrvUPydahVt7UhWrfV0QfS90l1W7eRlmIaMokNqavy8vrSIJ_yTQg9IWk81CFbD08lLEGphqQprRafWluK1943dKg_QBCZCUv7yyolwtsuFbWAYE58wokEymPCtk-KdOXT6lYQ-_4lwF18EhGFdRq0olWFydf0-XUDHibQcPWhb_1fJMQM_cEbDPpWyHh9V_5tWlY0cw4EBvVZQA8EFJDUboqtKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgL81RsQKmhMGmcSZ60VAfGaHU0EfveM37-7lNQGPWYPIPQ7FZXqnCPrfGScloBmJnY4pXzRmuFbwCFGYqUa7Mm2TcIzV0SVvpiZpyyhK2RXcJN5uu-YCOZcirqNj2DQtUDemXz9AxDhn3D0k5yU047LU8zwE7UqakPXWtJEYyo8BavQPC1XwD7fxFdADFRzTCOY3fneSZI3OZLfSJuGsiechP0neKNS9Va8DWWrgqBiVtHOcIl-Hm2DCjnF2x2rPfxyr5ocAApJmF7pASNvdT4mlpWSEUEnM5wsdMgKscaP0e45tPkZhc2N_nHvF17Rl-UAjQi6IHK6BMgboQnu2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تفریحات تابستونی خانم آلیشا لمن ستاره تیم‌ملی بانوان فوتبال سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97589" target="_blank">📅 09:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKfVPiG8WGXQjzF5q258jdb9owl7xW6Ryz2eZM2Ht1R8tEtR2Dt_rqsawwz77vxfyJb2UuRp2Rswp6H6_7-zLr1b6-K8-dSu6mjzN7SjrcnhaaYnumC0Gqy7W-MqNHPA8KN0uRprxy9nHNX1jpbCFZMEvUGoyCVhCLeWawGQhqRZbYgImB-r9BOJKe7-XZLMU3gWzZsrtVERpdfB1COOL7FH2CM7swAxlJsNIyfVxSiG1DVe1YnhxgRSkV1obVMuxPF99Ft51hxuLq54P_Zt2-T8pd34SLx-7WR8j-x41czAYIjt5Vzvbq0u7aLOgx-Wpt2eRkHQQ5SzJAwr4h4aIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
چیزی که وینیسیوس از هالند میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97588" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=PaMcjF4vPl2Jr69kbSoK1X3OVQbKn5AHjpYn_ctwbA5EbOl-KJS7mebRYZsbddOKbW9wa7dgSkwpUxNmivCQjs87uHKZ7ZKk_WuPL-6SsNnCddXKduPQmmg4NAzqrMx7ZL29M7OT3e6XCNolU1V_15bRg4Ux0ISRdptNxDkUGpUUMUdPPq-F-C-18hyk-JtoLohq29yrI_p3P2kpBGdHkMYtfmVEpWPKgGRCK1K88mQPmW-lRelYFxFvz02uS3Uapx3ArpYVsjmYHpinVMrqW7gcSDEOW-xmDPDWQA7W3EmQsiJ5XZOAkv5zdO1TKSxblNuvUOkYX0oWNex_96jeTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=PaMcjF4vPl2Jr69kbSoK1X3OVQbKn5AHjpYn_ctwbA5EbOl-KJS7mebRYZsbddOKbW9wa7dgSkwpUxNmivCQjs87uHKZ7ZKk_WuPL-6SsNnCddXKduPQmmg4NAzqrMx7ZL29M7OT3e6XCNolU1V_15bRg4Ux0ISRdptNxDkUGpUUMUdPPq-F-C-18hyk-JtoLohq29yrI_p3P2kpBGdHkMYtfmVEpWPKgGRCK1K88mQPmW-lRelYFxFvz02uS3Uapx3ArpYVsjmYHpinVMrqW7gcSDEOW-xmDPDWQA7W3EmQsiJ5XZOAkv5zdO1TKSxblNuvUOkYX0oWNex_96jeTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یادی‌کنیم از مصاحبه سمی سوشا مکانی با خبرنگار برنامه نود که فوق‌العاده وایرال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97587" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwmyLdglg8tA9bLZ-9S-aAvm2N6Wa4q1JSRI0rChxMVSutWYawTHcswtYAXZCKx0IAb24E7f6p0BMFPKIJfXJZlaa4BdX3EPRuDMLn5dh5idiXjBjMI0nLzwqCsFHg42HQpihwqrxxB4oOLBG2Faz0QgvJenFqTxa_FZ2epDe5IT50ZJ6GDNkXFU7oi15ytBLyVmnSDFO9a8ZZjjx8lu6uFaaCPOsc3XV0O1xJXaOUVx0cOg7EbC9VXlgX9Ylj7DsnEMSa9MezywtP_Xj0b3SbcAoRAOF3SxTFGp0-FrEGekALbX62Dj763yBM1zBqY01t5Vr-3w54i7mCtv5Dqppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL_33O2f0nKVqb4WK3S36ae-aWwNZZbIcJ1V7d3mX-QXaNV3F1Srt3WwCeWbiru8MCFUv5q5D1Q-U3XL9-cEVvr3KYdIsA7It-menq9sH3gEfJ67irlLWmW6hjaiXpIsNlHEmWhZ70K4gEW9EJZPU4r1DrKWXha-NpFtuUFBHiQc3bcjxTe8GgZTDS2Z5m1o_qcr45U5gP3Je9EAUGSA-6h42Umh0xhmHgzno2Bqh4DaWH9GjKgWZ3F2cV0VkAktfu0lvutnEaEHJi0g1EiyYn_cDrkyTGFOEi7bRT8sNhrAis2WJwbIuKXLkq_sfCf70HRMAnWhOeOso-3KLE8ETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEkEI949svdwV3rwDq1b_i3PFxFbqc06r4Zm3rTviY0nlrvSenCLz60g8C38Px1b4GXHWHPYGlPHbbLetI2yS-65bxVRswi3RzW4t3OetfqJI1kV3C7r_nz-GWSnuitSUk8oBpbugIPjl3pwqge0OFmfJiX2dq5DIQcPmxjBp50CHoOMMQXHG33tX7qayvF-D9NzVEnthnBpFf3siitvEvDy6ARx9A8s08N07ZJxyntW2m97UULOSxTO3bTlGdFBHvUh4boDyIZmgflqRz8mE46iBAWs0SdJlwzQlngDrL4UnTRBN7bqpFB1mnur9j8waK916HSYKQHThgm6LE1Qeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA_rQ8HqirnhnpgQlFebkfVjHcp8fqtUEJ_t5Ob1ngK6T3TfRWT2EvOuw1F1bgg13bS7pknXy0WltuKgtXo-hGQ4wTujZfA1Ndh71MsLdtdZjqJr054GbiWtqc3TxfjGgg_W3LWwIu-yREyHYR4TydZeVAouetzk74V36kJea3YwG_a9ZqFFejNWI8KXiiFyP6XC7t8naxn3tyksWiKbjRv5b8bUwVTV1OnBEBw3bslNXZAEIMc7LOWMtqfzLJZ6ONWbeLjMXAzCVnXrnCD6uxYaL8uyec33StAchMU_voU4aSs9OBxtqFSk3KLyPLvnJ8erQHh7iM_4gwIE3xZToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmkfQtY0DwVFFYS2MmNF6-L8ldoIc3CQPL3-OLG1IX6iGWzvxPNXbBK5dRtgN9vkn6eQlRhoHct5j7UjCx7YEtufh19sNKAB6Jb-D8gKfQ2-6m8VT3uAPYV6oE2-h1AA76SQWvACQ20qynnPhq0xJ2Z6U8JBFwIc6YPeuyGbOXm2FWOSEZJe_TBYy7AlYswm6q8xBueyGyQn19aNc_MLoFtQiQ6I8675wS01hcGsBAbFItNHjussFBuQQqmeTISyhj351s_h5zQrbcN_-UK8_cUMbI6sgoBrD9TDcCdTyFD8XgCOh67fQvCxNi71AHnMcrp-p_ymd9NjeSX6TfB30w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیت‌ بازیکنای انگلیس با زیدیاشون بعد از حذف دکتر کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97582" target="_blank">📅 08:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=hTMezoOQyPo0WTqk7soushOPdgXb_ZbqKAD-5kgzpQRIDll5IbdJkUAa03UYNdrhWhDnYTgOAlF_ebw_D2w1S6cmCBzKp4qy6QgaeoouKdKH2AJUk_tc36RTZJYOQ6YIgsV4ssdgfg8cLozQCfacJMypmJmNTf62RPez2vNSGWOwYU8o7va1DyRWshbCI9vO8kV-FVXTnJIHbbEP45SXN43-4mbzW4UWBNRy5iRfvrAehrTDODUNpcd8yRNGPMAXBw4tipTeeoaIqzXU10sQ5vf4XCnm9Zy35TDh0rgioM0MNU1KyGw6QiTyMtAeTfEdZ55c1MQXJJMGobDqpBL9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=hTMezoOQyPo0WTqk7soushOPdgXb_ZbqKAD-5kgzpQRIDll5IbdJkUAa03UYNdrhWhDnYTgOAlF_ebw_D2w1S6cmCBzKp4qy6QgaeoouKdKH2AJUk_tc36RTZJYOQ6YIgsV4ssdgfg8cLozQCfacJMypmJmNTf62RPez2vNSGWOwYU8o7va1DyRWshbCI9vO8kV-FVXTnJIHbbEP45SXN43-4mbzW4UWBNRy5iRfvrAehrTDODUNpcd8yRNGPMAXBw4tipTeeoaIqzXU10sQ5vf4XCnm9Zy35TDh0rgioM0MNU1KyGw6QiTyMtAeTfEdZ55c1MQXJJMGobDqpBL9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
نعیمه نظام‌دوست: روی عابدزاده کراش داشتم.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97581" target="_blank">📅 08:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmA0vB_jaoHYX_zOH9TJWphLQ10NThR_z1_BYz4i7EbeeZsvpOSQswgU_veLnx3KQN2TBbdOjBAMC3FzYdn6O6OAstyn64eSvtGp24uFnHOLJns177rLEauMPYop9aGCdn2RVGixZjCAyLjLWBB980jLEkOnTjWVjGN_dpr4b6qSFv4LKJO6oeVarZanybXBIoDEfdgpbBjaOBKbajG06wce3jQ4qrtjerB3_NWmV6-mK7jeotrCNNTsaSHBcTWstTyshQlDmiCbLic7UEjnCYfWkuYBDsiMOXtgQiSD_efVM10im4WQzwormEIgE3v2URZnqYhpPd8IuObipJU0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
ادینسون کاوانی 39 ساله پس از 3 سال حضور تو بوکاجونیورز به صورت توافقی از این تیم جدا شد.
🔺
کاوانی از اون مدل مهاجم‌هایی که وقتی توی زمین بود، حتی اگه گل هم نمی‌زد، جوری برای توپ می‌جنگید که انگار آخرین بازی زندگیشه. از اونایی که دیگه نسلشون داره منقرض می‌شه؛ با تعصب، جنگنده و تموم‌کننده حرفه‌ای
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97580" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=GkPqWo7vPe0WOKd8N3_4oPNd7i9IHyUS1TCBvij98jNDgwj5aaH32XFCURF4VyQRjrdGzQVG5eN_VAzsXYIdmFkHzlPtfggtCGecP-DS5h2_0MQ9Shc6WUd6IJ3U7pYVD5rWvqLpXwVsyvaLWHoQNtHV1koBerpBAoWH3pZnvJ0EbPPcYFFUf8nuxvL-EDenCD6-xZMEyD5_hXTHTByUbedpCAtDNl4zXO9b8-aqNLtSkXxTdx6msZ7Z8UvDdAaUstLY_FO3nwSGbWCEcTZefx3Pxl2vDmXmfvXUQ-erc39Naki0AmRv6LIu2hO1KVxIz9HHhutMlur3rV4Vyr4ckA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=GkPqWo7vPe0WOKd8N3_4oPNd7i9IHyUS1TCBvij98jNDgwj5aaH32XFCURF4VyQRjrdGzQVG5eN_VAzsXYIdmFkHzlPtfggtCGecP-DS5h2_0MQ9Shc6WUd6IJ3U7pYVD5rWvqLpXwVsyvaLWHoQNtHV1koBerpBAoWH3pZnvJ0EbPPcYFFUf8nuxvL-EDenCD6-xZMEyD5_hXTHTByUbedpCAtDNl4zXO9b8-aqNLtSkXxTdx6msZ7Z8UvDdAaUstLY_FO3nwSGbWCEcTZefx3Pxl2vDmXmfvXUQ-erc39Naki0AmRv6LIu2hO1KVxIz9HHhutMlur3rV4Vyr4ckA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط فقط بدل رامین رضاییان رو کم داشتیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97579" target="_blank">📅 07:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=PbLZlDcjPsjTH-qlxwRD6ihn6OmHWcpEa-nHmjwzaCdw8X1JIJFMwgSaPHK5BgGTOJMCd08vzbzpMgUVL9jNIYlnqYSseAp-8nYBhUSwAhftSJpnyZSALyn5cnAGwxHPbaxluH1ySKPmRAQvtsHys2i-5772p5K5gVRJaq5myJX6d_sXZHWJy23R5LTBkKSWeZepqkbHmRmSf5DaBoaIqbXlIscAfPTOP7sxlmqqCsA6ImlbrXAvcwHWLGGnKEFFD3tZkDuU7D0rz8ZZ8znb6zL54s3q_x8WE_tXUD04wQg2z0u3CE6bABCrZCHJ-FtB4B0tTRgzFZf7STnrcjPqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=PbLZlDcjPsjTH-qlxwRD6ihn6OmHWcpEa-nHmjwzaCdw8X1JIJFMwgSaPHK5BgGTOJMCd08vzbzpMgUVL9jNIYlnqYSseAp-8nYBhUSwAhftSJpnyZSALyn5cnAGwxHPbaxluH1ySKPmRAQvtsHys2i-5772p5K5gVRJaq5myJX6d_sXZHWJy23R5LTBkKSWeZepqkbHmRmSf5DaBoaIqbXlIscAfPTOP7sxlmqqCsA6ImlbrXAvcwHWLGGnKEFFD3tZkDuU7D0rz8ZZ8znb6zL54s3q_x8WE_tXUD04wQg2z0u3CE6bABCrZCHJ-FtB4B0tTRgzFZf7STnrcjPqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میفهمی بعد این بازی باید اشک‌های رونالدو یا مودریچ رو برای خداحافظی از بازی‌های ملی ببینی
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97578" target="_blank">📅 06:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVns2EiMmACK60ZPVEUP6stEUjExmDKqp4U3JD2CzX-rLCCS-4ASyKzkYn70N4C_xSgH4Ab36N6dOMKJxRzUoKOzUw3NMxkatAqFmrg5C1H77-2CiaDq2Kpy4WgDdZvOrc9kX9ACkpFcI8JEmUa-0L65iMWS-i1VFUpatbQV_CzUpSjC5aGw1sLNj7ic_oqQTahmWwdswQIvI1mPXSG64EInhb80-4vpi4I1QF51UZSLGOhtwyv149K53pOR9XrLhB-7WLOAn7SMRU7PNQ9IOp6iyA3ooK9zLQQjB1Yt3SlH2q6xy50X8ngfoVVeo8GGENJGZ_AtVu9peIeWDTJu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
تنها ۴ بازیکن در تاریخ جام جهانی در مراحل حذفی هم گل زده‌اند و هم در همان بازی اخراج شده‌اند:
🇺🇸
بالوگان (۲۰۲۶)
🇫🇷
زین‌الدین زیدان (۲۰۰۶)
🇧🇷
رونالدینیو (۲۰۰۲)
🇧🇷
گارینشا (۱۹۶۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97577" target="_blank">📅 06:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UElg6QiVUmo1uwGk4DX8Zu3ZUqQt2BGOC_lWWPZTmnYn8CAVU0LFE7ImrD-3-glhx_vl67zTueo3759ENUgAMP9nGZbSJCoQYYq6Q-R6riwjJF0TxXMnebu7Njvxl-2OSTV0_pdc7BEicFtq9QqxW_rMSwp2yLoYoyx0EACZtk1ChQsf_2Y7it_aLd0Y00V3YBIfw1XseaK3GCKPrvOi4MEClDyOoP48CQwIbJYfmhmGb4UlE3Ra3tlPsEL4pfhTnkTjgPsGpVmUH20_WzNcESVnes2-7vnhDLHMqb0GKuq_iDxJVQUCLJjxm4Ro6iKVR7Xv9o3U3HYnCVPnriwV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3o2kw_TlMakzxGnHGjv5wa3Kc3zU1ArKSWUKapbWQ-BbRVpcdDSrxLsxfqoSRjx6QrufZQp1Yhhb6UN5K4Mlo0y4QrX4sPu0nCiSON7_wvlUi2miMgS7dmM2ZTGe7u2R1Vz-QG_HI3Y5Vlefudb9g2CQRZqHfxQWlZATClb866lyK2wBvhkrVHY6K6hXv1wch3W3ZgPfHFy7ulKoMbZmusCTV4wJ5HNY-HTn3o_erA_f0wq3GbaADuuV1fWY99_5NqsB4q_xUfGYsv9vt2aiSwGYJ6_5KmFk4GeR1neb6iL86RyWRZl1qKpULd1XJDEknR7l-XNSx4FCKuk57iUTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔺
پاپه گی در اینستاگرام:
🟢
بعداً درباره دلایل حذف صحبت خواهم کرد. اما امروز اعلام می‌کنم تا زمانی که این کادر فنی در سنگال باشد دیگر در تیم ملی بازی نمیکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97575" target="_blank">📅 06:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeHmFEJi3Wimv4WG8VW1ewjLxMWM3l_bAqDwOe4q35hebr2GFailjgLhWtb4zxTCq4TRKTo6uLq7dR107suLJiT-xFDXAi1vpIy317VBMGBKdPXy4y1cxigEEhzJ5mF-pip6Uj1NrD5Grd59kutTcVy6LToMidJSXKO5joTmE-9WPoibfmSSo0_E4KLs8H6lggW8ZJQmnyOrTDTFjBtz4V-9ROVZ29tMw6NRCb1ABFCdVqL42gUXJQgcuxZe-XMJzWX_AVU02-YqP9NapyGqGdR6XR2sBcDJXxh_2zlQ7QOk5PLdGaVBC00zB1MuZKp5q3yj9T0j4NEnh1yEtjshUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjpHmvltbfWeZh0oXzCenlWf1bX85IO8_xI87q3B5bLEFBtpy8RKwbOf73AQI3QSxbqSOKfutTowPibmKzB286KbDgvZQxyMwjBT199ALPfHN0VQpYr1nrOjUa0GyzJ34sAz5QsAzSqEXm3fu3ODR3YcLaP962-0jX_aHZxwkk1gEO26I-De2wtUDZuAzEjEc6gFQNgNuwfMwc4qSHmvIGnN3kAR2YrmwSpL__O4W4XaqAt1ueiafWoOZF2BlHihAMmlVH5A7kNuk3fu3Z2fIbsxnkA2RNXNbeX4Ois9mCWxhv0Yi37WwgZyXaROYNuXxacesEMOiwkR_D_J4H8UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfm_uulNTFC2AYejd0Psu5B3qkgAshkE3Tpsr-SDYZEDkXOWDCK5T5SvYT-id3OmeXqYXSP1i02G2-bWZec2CN7QCV8DKI3HhNr0vC1mBHRia0KYJaTZAdzJ9By-5bn1y8V6icMy0ftGjEOskcqVD8kNNnEzx8p4lbAw0KnzLWdqnSLqnRY7VT4nb7zOWJ11phjuiEdpt7f3Rxe9_Gd6Y9WJ3GEW4JvDgfRx3Y-SZxXrvU2-FD6_EOSRobIQbZEWkWPfq1oYYkEaYz3ZJ8xNlNEIu7UZyAm1hwZh4S3MbqV-zzCY8Ba7KR-6tqnextOsDeHCm-QTP5rgi-CGe3wPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd0AleQPQEnpASm8CcWaaQ5zXHwPqT2DDT4ULXXkGSgZ7KzwpifiXsG_rAN7YRh5eHfmgj8zuCZ5WvjxJYFSwBhz10YJKtRRSK_9XsDIWInrDXfqmV9KFvEaElb85eo5_rNmX55DDibEAxNAUPTNFeYcEpoTSbRrctY4olV2dHfUNpb_uesHsQW2YMW7Se0ZzkZ2s72CkKALzTtEKOMXOXqGjRCT3dzEfgxAjPveIeEQ3ekVV0vJoFm2f623RNBzsNoL6fFvlYyWp7NfhKD5v8rCW6MvcakA3kwKaqxLwwz0Q0-C411QinYQrFnV0oGPrO8JIaax786KjE8TFtucGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ده دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97570" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=AlTy68wGwzNwyHWf6bznsIZHR8jR99eMuwyr-U1NIuyvn4t_zwqXhiDVzseIT7_BPK7ZdiNczOxgs_AQmogZTwXJEJRhrzK7jsFdtmr-857B0Myyru46VeOcW79XoDvuG_ehtjeoIiIM3kuW2seBHDCNbJLGw__cA0wt16o_izUs94g9oWZo8XPDbAj89tEde0Cx-yHDZsCdSmp9VWcBr8CNOuRHlRSz3gNyG0DIEQK2YI6lJm0qmdnW5BvMIG0SvnDJrf_Co-zGGlqWDCHs3EkTJ2cXjVmy10jTUCQmB-bPo0o5x_nhIvlKQArNEu2hKTcNAqIsfcCHwwIY56FnJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=AlTy68wGwzNwyHWf6bznsIZHR8jR99eMuwyr-U1NIuyvn4t_zwqXhiDVzseIT7_BPK7ZdiNczOxgs_AQmogZTwXJEJRhrzK7jsFdtmr-857B0Myyru46VeOcW79XoDvuG_ehtjeoIiIM3kuW2seBHDCNbJLGw__cA0wt16o_izUs94g9oWZo8XPDbAj89tEde0Cx-yHDZsCdSmp9VWcBr8CNOuRHlRSz3gNyG0DIEQK2YI6lJm0qmdnW5BvMIG0SvnDJrf_Co-zGGlqWDCHs3EkTJ2cXjVmy10jTUCQmB-bPo0o5x_nhIvlKQArNEu2hKTcNAqIsfcCHwwIY56FnJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل دوم آمریکا به بوسنی توسط تیلمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97569" target="_blank">📅 05:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عجب تیمی ساخته پوچ
🔥
🔥</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97568" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ده نفره زدن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97567" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دومی آمریکااااااا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97566" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلللللللللللللللللللل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97565" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftmoSypzqNMG43S05OxP0oIYyHerg1eMotOiw9V-2mokXmkspdA1xwA5dKtLtLRZTXDdsdmc_xObUfpKnFxZa8x2KA6VM_4KR6W5NckrlmH31JyoTCxugkRGh0fTZKppWnLqR0nttGIBkTYtsbMqUvJKrY_kIVVEXcNCDcDxLWOVD4YKuv72gqcjdkkKDlfTcvXr1-2Zvt-Tzk9YjF4SeXE_EwsYrdEzB9OxMT56QY4ZD3muvu4PhegRtEmCAkHfJoeoTWnQRxgKypC1H9Fd5IZXrfmhzPvRbmV2YEjXgR3fCl7mQgOnEyDNF3K3CJTc6-o1DLZ3FRPUQn-TquN73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97564" target="_blank">📅 05:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دومییی آمریکا که رد شد
❌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97563" target="_blank">📅 05:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZVxNdPoulVlml9JL7_fPj-hkXsXSyT0yNUrFWjYhSgUXUaHL8KcCtyNuv6-m9waycWo451-E7HB74qg_UUXvk5BI9_xKhS-d05UoAwHYBfpC4Q41_qcBJJMa6G8iHR6X_xHV2B0oBzWriIz6YwIiYq58A3MuAZwze-13DWV5aJxZVd-8zOqPxLOw5ozS31Ccf7FGxlEFrJcBvgq15h68v3VfzABthvviynea3mu0njSLJC4tz_YnjpA8sd2-HeSWDXYorXMLUpkV9sij1BKWiXlmwSOxDf5JhBN9jUowfD075cyAVfa8a0nxHL6SP8zmIGiv2e33AOJn_wswyiSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97562" target="_blank">📅 05:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97561" target="_blank">📅 05:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دقیقه 62</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97560" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اوه اوه رفت کارت قرمز برای بازیکن آمریکا چک بشه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97559" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97556">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOSRXXA38IttzGsd18JkhI-ruDFGSCPf9jvtubaHir9o6C30OwcpZlvvKK8hzY0GpseHooxX0BcIJLoJKd8-bQSGpMnCoGcjslQViSkz8M2B1d7K-_yySZDEGeXW0O6mSxQ0rbK_3jOcKwnR-Oo0XSBjh-wBzrSc5MBXjJB4q4B4AMyYkJzpxxZqmQwaVOadfV0SkLNU2dW8FaoHEGDVcFUzySFzEhGoBAaURvj3b_Kq9gTDdIuXjSf0LNgpCrD_mQOMRUjGuKTjGYbPsgy9Ijjrw921oPzbILLyofB_n6KvfRW_aZNtWL6sHvOI_JeuoRgo_zatTK9KpBVknmzH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgxMAiWUE5_PPb5fYE3crZW7Mv2u99X6VbTMaUMWuK-Zp-eES_mXqS0VLY2gSGSwZQRoTLy2cWN7U-kjm-F8JOXmxN28qBn9_14D6CanS3JY_Ch-gCgN2biUKrs2WQRdq0iPS9HSSO6r5bHgnwqhpnvlktSWvPmFTkK_XzQWaiPfU7NhH8_8Jia1O961k5y_tg_-TH7sQJDPyiAogB-h97beNtlPKGkemWO8XeEaa_oiOHrUF9OjWPTwDM5-xHU-YSJmw6MZOLM69v_6-HvlMGqEo1ZEIi6Q7_LI5Znj0dytAQCx_bU9WVRmePn_LVAailstBWwZCLrKMrb6GMYtHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NgRzpWXZi9kAe41iXok1Tsl7uXc9wFSz1QUlK_JZ9jwODIvCH-EkrZQd1X2PbmWnXq4Zq_LL8SW-LDMHufpVt4vGNiwlORcqE-rw2AT74Gg6sVeFsD_mWlp1-mMLtosf9ztO3H4BYWYDmfNLARWqlhZD1o_90E02shxOgbUD-9RWP2UFBOl-MPVIqoZPD9V-gR3499rlHjxe23tFM4HcbGAVw3NKmtyHrHAL3KW4M1yqSUTlAigo-4mE86CzItGOVuKCsvlnwe8m2LYXW6lEbxIuWfaU5PYcLHz4gavzgJc1Yx5Z49DNrX9eB3ZPazVhAksEThLRoGFsLW_WBqWC7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97556" target="_blank">📅 04:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97555">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYEfxJhY1ABSUkKize9wWGopx925jJG1Q9YdQ00NL1f8JEn1wHKdJGtqVP6JeoeLCEFyvRcgVyZGVzzhNZ75rcqxD6MckuowiaehkC_RZpjebQmh-HUrGo6s-izTqWDaEyl6g5OJtn5Wn9RyaKJ0kiNzltapYWAfZKjb03ilX0wAtX3n_FOCj6AtOiHZTf1KBczK__8oXioYzBda8Ml76VHGWFIvOk-my7EeEoLG13iR-00QN2WzInHoin8a4Viy-_3N4vrGVsDzBE0ZLP-8XnHhA1KoaxcFRHLVTzv4j2GHFq5t9r1MGpvOVlvXVdLEBe3B8zNcvZQeP3gKA_2p4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تاریخچه دیدارهای تیم‌های اروپایی مقابل آفریقایی در مراحل حذفی جام جهانی:
🗺
اروپا: ۱۴ پیروزی
🤝
دو تساوی (که نتیجه در ضربات پنالتی مشخص شد).
🌍
آفریقا: 4 پیروزی که دو تای آن در ضربات پنالتی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97555" target="_blank">📅 04:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97554">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntpncyevefum4JyI-wDY0NEGYYyF09L8enE98ZRWvUBy-9LFFCYeXZwnyB4iKJ9oC0o1kNwKH4-r09Z1CuRD8uxfLgwePSssraZCDs12a3ePyhPC5WfnEpn1W2zV2s1uQwo95A7nwwNZxOrOdm6UPjzGqCct1fN9J8hoxu2emyKDcIW7Pzf8_4DAOPcUKz-D1NJmDY1qTxAPnLRQprs7z-wqvobWkEoWld8MNMoPSTKSk-gjixKPBqsCxYxuifDcSZ3RYr6FOy_7JwmxIwco7pvlYwspMlEtA6zQ6a1rkHBAIKsJKOa2z5nVs-RdklXIkoDmG2qXyLl8W1i6lis-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخ داد پرز بخرش
😛
🎙
ویتینیا : لوکا مودریچ برای من یه الگوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97554" target="_blank">📅 04:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97553">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=Bloid-PJHw7Wl8dtyhJSHLsXEdAJGb3taWu4HUDUcyM8Rscs-4DWyUvWwBL6NMUOYNQT8qE8zsOi0Ksh2XKxzE_3xP7GrhFFCjlgBaabV_Xy5SkbVLWqnLRgMCw90ADmBwN-nKpDaP2V-8w1GTGsrUsDsRyWzRDAd6J2E_1QGiSfaBa9bgJrqACBRiUN1egOOJLXIAyj2WcVAky_GjDOb4inFMv95bcw49SrcknESYbi4QRN129RCKUOgjATVYcRnm5N_5_-rwOj_PzjgjWWF3KLyskWLimGYn2zneCkjhikX57MQvWwomJcEwcfL37yGdwLSMB9-in7X8W7CjstoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=Bloid-PJHw7Wl8dtyhJSHLsXEdAJGb3taWu4HUDUcyM8Rscs-4DWyUvWwBL6NMUOYNQT8qE8zsOi0Ksh2XKxzE_3xP7GrhFFCjlgBaabV_Xy5SkbVLWqnLRgMCw90ADmBwN-nKpDaP2V-8w1GTGsrUsDsRyWzRDAd6J2E_1QGiSfaBa9bgJrqACBRiUN1egOOJLXIAyj2WcVAky_GjDOb4inFMv95bcw49SrcknESYbi4QRN129RCKUOgjATVYcRnm5N_5_-rwOj_PzjgjWWF3KLyskWLimGYn2zneCkjhikX57MQvWwomJcEwcfL37yGdwLSMB9-in7X8W7CjstoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل اول آمریکا به بوسنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97553" target="_blank">📅 04:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YviGCl3Y0FlFYlzm6jh0o7rorh39wMJCPV5ZEQdgz8sSeKuJ_ndYQszvQ75gWgP3jZL4QzwxS8cb7DYkBMXfju4EifCqL-CgiNsANiBaQF3jJ2iLGSKNDomZY6wjWc9AQljq1MwMm-g5f86o4nKj6i9qwVpLulEI2-1zLOI12fWMoJw_BtpSgzsX-j0DTDZ1o2wdIwIM-Rim1QgLTWZKm9wY8a-f6W26HmWYj7EYM2DzaRF8Ir_XsGVVfUZp6NYcJyvnxL0DrUDOAuuwcuG8aPS1wgH7x44ILF_9VJGM74948avfPpawPWOEJjhnvM6anxgxPFXYg-N8FhikiAWYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇸🇳
| تیم ملی سنگال اولین تیم در تاریخ شد که پس از پیش افتادن با دو گل در دقیقه ۸۵، از مراحل حذفی جام جهانی حذف می‌شود.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97551" target="_blank">📅 02:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qub6lnDPzzX_sQn9hkbKg7qEcZ2qEHvIwCgZe0oA9VsYFggQVbZBXcRKZAV58RfCNG82lzDNlER1DaWetFYWx9Ard67X6PmFrIu7mhI7l7AKWCi0s5jQi_L1tY3yYBiF1H81NRxuJAFk6Qlh4CI581rLMnbcVcQNyUqct6JNwRMDy74AYx0wqPX6nC4kZ9OofHSCuWyv87FcrfMX5dT_vhgJK6EK9mjZjhz-Eim0e_RbhDmbxKEOJ9ufDZhAlBt8oVZeCDmTzn5pw37GkqACidPsUWfXXD5HmyMMy-ixGszkGBuUlGGpyUdUV9z1e9AitkcgAB3nLArfYk9_upWSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
بلژیک در ۱۷ بازی آخر خود در تمامی رقابت‌ها شکست نخورده است:
11 پیروزی
✅
6 تساوی
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97550" target="_blank">📅 02:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agrRsnjS2gIedbr-YJZTEbhVmsSIErQBjLM6jszBhf1p9PDMujOYV8-binkic3lIZ2TCjbMEp_Sc2L_yelt5ZT1_2xPuXVw2ljlIGcnYCWijDAQDYI-n5X6YEnUD9Q6Ojlha2cI570AWKcy9Lgo4YpTjmDTOCIl4yzfuLgXc8A93r5th1Qr9tNxqOeg1pFBLWg_NKHY4VqeYiWKD-xMWZWvkfj5xYR4u98ElQmzE2qWi9m2wmObVarDpliBuJgdcQHkFA5nFRbsu4gGQxy0-IZmX5b0_Deeyrd1R-viKzc7ms6HFzPMtBGi3f4Mi-c28bAK1ema4gJwHJWAWMZ0r0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🔥
🏆
بهترین بازی جام‌جهانی تاکنون
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97549" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0Tu9K32FZjV-IbN5rXWEPWi_3T2XsirvPFDGaIkwi5Xuy0UtLtDrdged_MUIOs1-F7NmBEKjm9aIQUM3p7s7xqy37HH1UNV5kFw9isfwrpOu1PNuyDs0VuSyhYW1aWkdiJaCSpFY_VHw_CgDGDYt92tJYzzuqRm01t6oacMu9nFW-CjLvhWO9bsqe_md-PVfCrSxk6HphNodPgpnCS6A2KI2c35_BtjJ_pA-xG2l82c2HnRfa1hW5Og29lm5C-j0-pts-JrWrAMF3i4PmpH4_Ai8M6DLYL-jaBuUxE-QnGmd41P-cFIFB8s4vxGVOxI9780BGS3eydTPv2G3wPN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
| بلژیک برای نهمین بار در تاریخ به مرحله یک‌هشتم نهایی جام جهانی صعود کرد:
‏— دوره ۲۰۲۶
‏— دوره ۲۰۱۸
‏— دوره ۲۰۱۴
‏— دوره ۲۰۰۲
‏— دوره ۱۹۹۴
‏— دوره ۱۹۹۰
‏— دوره ۱۹۸۶
‏— دوره ۱۹۳۸
‏— دوره ۱۹۳۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97548" target="_blank">📅 02:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxeIC1JxzsmR3St_H4M8ruavWO1gbq5Vnb78eQhYi55yLB3kzcF6eJ5z31lGFvU_Cx9J5GuuLJO7hwSTOBzKZ-X7k-6xPtxCNy7fNaBhRyAcx5UBRrIUM2gEhIaBSHY2Rii7sh-gO69z9qNcSkHb-OKcRs6-IhyICF3RL--ayI8WtYyoYdOtOaakXRDLQMLCUoiiUVMJyLOD4G_-XW8GKpwxKQUhCUinuz_tfE4Bck0FMp_CX1FgtZtCBzYhYAUP5hUNpmxr8j62O1o_Op2F6iBMJeoM6elsU2kWk22afPOGLtwt5A21FcVvSmAIc8doH4SMNOjuM_D8ugdO2uwpbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
| سنگال چهارمین تیم آفریقایی است که از مرحله یک‌شانزدهم جام جهانی ۲۰۲۶ حذف می‌شود.
‏ــــ سنگال
🇸🇳
❌
‏ــــ ساحل عاج
🇨🇮
❌
‏ــــ کنگو دموکراتیک
🇨🇩
❌
‏ــــ آفریقای جنوبی
🇿🇦
❌
‏• تنها تیمی که صعود کرده، مراکش است!
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97547" target="_blank">📅 02:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGSwpxKFShWfSUw7jSVmhI51l0ylW4OMQ2wEvbc3jYwjMCDvEXpzaKuFDWjyu-LkIMgaz8f0_FZqt9gPao9551HhP6QKs1sMUarQQRmgaL0NaQfoAL0_TSZCaicCihhUy14PSrMmNhfTVQ88pDXQ9kj_MnmCV_0y0H1phmRyPFzVvzFGS4CwaIhBJWPImypYElnOTlnTqPx4zHQHfIlPMaL3R8gl8Ou7xpo51qWqdSl7hJY-nVzSZjKV3mG48Fji33DfNFtkh0akUiaSwukrlVU6tralkcrznCk6GVNdrA_i0RQ1vlQfmJKlpnY9PO6-Fal5KORoadFctKMnY_C9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تیم از بین آمریکا و بلژیک تو یک‌چهارم بازی میکنه. بعد هلند و ژاپن باید حذف شن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97546" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_xntuT8qEWWnYyZEq4PKMWl7KBaQ3kSw1hjpZDzUy0yfsyoO0FuDCaOzDpISsuuGrNrqEc1WpHL0ILW-ABdarax6xe-PVJYVKyQl1podbUJ9c-rP5wnSjpEQyRtvWopmHT1pMWXNQ9RVVRS9q-lW8HUf3nluIOYNfQQAG-MRjY0RvkTTKkEAUdxy5gndI0X7xcUFq0gqfYzPbad-6nKI0dIMbfeUC3PTWi6qYV6w-EvhaJx1_592uovWKLR18YuOCVcpePr5DIosgvMXyj4jQxNTX5rTEr7_SFXNxdfqjRffkuEY7wwebmu-kX2xN1b_61P7HwBfgvF11gG3xsqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97545" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxvVB1UTBFafTjwFdEb6_zhIuG6mah3wBq4qFZ37jGKCV-y7FtHTpaaTvDnwINRxUKT5F0mTPe1yEVn0w6loa0NUJnoWeMydku6YPxTl4JHMg6AUDvxChtGj8la1Yj2XOvac6MCDITtSic3sZLlWYDat2cz3QRVPzH2MBWciywU1hVsfC1bRGPIyjbopR5mdvlbBv1bpXsmx7veDC_ceSSwTdj0OFHjkwHTLipuOXH5JwA_-XMYmBL23LZX0x3mDUcTJMXJZZgP16MUpKGdr9cV-A-98TPPqoBlKquV-xiJgWtxfkAsFijfnEPdLBrxgvr4t-otlQamHO0P1-FNy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
گل‌دقیقه 120+4 یوری تیلمانس دیر هنگام‌ترین گل تاریخ جام‌جهانی فوتبال لقب گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97544" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHdn2r1RGwiSvlo6qnnzXMuQRhbajkTMnxHDCvubtxCY4MhFB21bHT8YphyRY84sseUQw5XiZtvVNuOpBEyfWsm3mo0koe95GSJqlM7PGdsMgj5G4R9EEm3ii5ICEdNjzDrtwxyDFk-iS5_7izZruR4Tv1pYRg4wJxZcFOxbiJGxE3uxrTp2NN1rND_IwuX6Osh_BHZVcfYUghtLDSidp6Qo6bsNVn0I3NRAyTshtGIigaqRDHMrdDxcCiSSBlezSRYItd9lNEid0A3chF4rn_eVYnp2ppAlrG_PNjC7Cn_EC7fsfU2FVR2AQOr_9M2HofsR-mRmas9JkBadEuprEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
آرشیو وار:
پنالتی بلژیک درست نبود و به اشتباه گرفته شد، بازیکن بلژیک خودش باعث برخورد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97543" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSQ8D1laU88Ft2Tk-8iWGssVavAjKwkui6utNZCrNXoICHdY1oebhHJwS5Wxogl-ohA__BSNoKN3abBW_bEZDoXfnBCbsCUW2eHBWUuPYdEK70aF_6geVtV6tKiSeA_tNIYCJbi_i4-g-Z7VdJ-fd0HMICiMfqx9cOwBNi47_wtJgyFsl6dB1leR6E5H7-64a4SN3fGRHw4Q1qPKWwRRmuf9XyDgwI21ZGFSqZ5_qPCGtc-p8zfr6QX7o03OqVVIsV7uYGN_kb5oD4b_FEw1bn-Ljf-JNyrN7bl3RykNohQOIOIdvezA_OcbOHGnQxUqydjp_LeipQJ9mdi6ZZ8bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dF7gGASjZrqoPc6dHXpTIrJ2vmU8RIAIov7ZLWPMrxRoQ3vEiMOcIPgHUwehQORdSc0aV1Ez82eioFnCT1PnnSnK4kw-cCOic9LqQVp_OfdrPGx7Te2pw-wmK5wuzGB36RUQ1YDkYPmhk5-fnWZIVZCpZCfWObrSrL0xN-ILPXqzSFmXA4l3Ruc0jDAuc-xNkyhGhOE0egwsVeenyYlYACJems_yl-XN7v8X8VxS_gDjcye1TsbvqmYef13QKbzxuBV9DnFAGvWEBBVyZsFuPN7AEp7HV2djLXy3Srd5brpLey0EqQsvbyHAHz0oi7mnPRmNKuDz2bGnHFL2blltuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🏆
🇧🇦
ترکیب آمریکا و بوسنی
⏰
ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97539" target="_blank">📅 02:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7kLdFvoYwwQt_l0cJLPLOglVaoaMT3uxl0yCA8Vaen20LnrT8a87lxqs-ijnuKbtt_GC2Rh9dsSYqClZmhtteQzPjqFEoXSQm654KgtIv7tfIC0u3J-ZdBx7AJevPry5vU8jHI4VsPIq0yKgTLOMWwIIO9L9rCTvSJK3whfRS5Aud6I6WokTryGyzJA--75OP7JaN7Xx4nQm4YMvqRm1QZ0r-sWNelB3o6AEo66_PwiGuQGGg2XcZkNZhSctQWVCug6MjFbR9CScvnnnff3PQzK_lLk0FQqrgIAATa8zshVsiy_To6MdHgu26tVArTBpFnGrIV2a1CbvTqXQnfmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
برنده دیدار ساعت‌دیگه آمریکا و بوسنی حریف بلژیک در ⅛نهایی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97538" target="_blank">📅 02:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97537">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwrQ8pODcjUvObfU7XqVdBXUllMe1Esq3Bmt1LQTwiHG3NDYYBWEkI-HrUhd2OEAF_NhjncWew7UUC6MA1UQG1UUKzQ8ad0yt-Daay_gw_qjqxXLKU2l5DMmG8j2eQ8Kegyz1jrs7GHX8PS3EBjZYV2ldAomZIgVw8NfoWqo0Lht8yBDBpWZ5SUBjLLsfy-COVjMNoKKGDLpIe2FQ6Z__Eh_VLdCHDxCNsxHiKxzVJZmo9GX7B0s6ts1LODgnMKCfqucz38PhVC49nj3IrS6bFwrTtNGnLnIvBJCrDprG7Ih6PFdde-2iXOQGK7wgXO1chQVdgaw6LmmZYMAufzRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های فعلی مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97537" target="_blank">📅 02:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ldbs0k8TOShtX2THZzmxZIhvEYEhyjDKaOoNCgRFjZusKatp82ZE1yRIVXHYzdDTw7JUL7GwILtsYhtezydSpbnV-RK1Nln9vfgM9CDz7RBUHc_saAKD6YA_kdxkfs0tqz446C2-noQRc3sByXYONV-zgFT-e_SRk6gxpWE72gSIJmDK6VnW4tq16XZmNbUJyRKUiwt8OSWDyIW4BeL6sYDkYnmVzvUJjGXu2-hRXBU7h-3TADskMSxBlYJaT9M-1TrUh_UDsr_3ge-s5Cwl76MMpeYRIcuBZxGJ017NS-Qv98TYz0mhMKbIusDlTZFqKfWkfeNHPWlBRJ72TwhCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
و تاریخ که باز هم برای بلژیک تکرار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97536" target="_blank">📅 02:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-Cxp9XlInyp9SOJHMcSPR96RLj5Agf3oOWMZnD6Dccc2wWqSZSv0oWL-wAoyIas06TsTGBPBvG45jLEAzS8T8b9-A5q2m3ztPYdUkPlp2nL3WCKwhnXXuvU-zFlCYjLA1STc6KG-5taZfzn0519sfMSpWRKC8ij-Bt1tDrdF2quytz1mzMUZe3QYaswSyzxHMjOOdcea9Ye0_g6n6BSuMsTym5ypDju-wjfsXhfXmpN7htQpM9ZiDUqLIU4pdnqH3wlTDO614h9CjRfqNFvr4CENYfcFlTmGd2Sm1QC_wdTbDh2rcAZYqG0Jp5LBqJlfl2OWjaymNutUCzICu_8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک بلژیکی‌ها با پنالتی دقیقه 120 تکمیل شد؛ بدون دوکو، بدون دی‌بروینه، با تیلمانس!
🇧🇪
بلژیک 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97535" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بلژیککککک صعود کردددددد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97534" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97533" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تسلیت به هرکی گرفت خوابید
😐
😐</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97532" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دقیقه 131
😐
😐</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97531" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">میگن پنالتی شدددددههههههه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97530" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چه حساس شددددده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97529" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
