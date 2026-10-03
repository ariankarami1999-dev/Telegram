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
<img src="https://cdn4.telesco.pe/file/ginW65TtoNAGL0srwEef1eNtnMGLJzzqnH6I-o7rExEYGdYL52VMGVan9OSVpaqXna1oEYNkSUun4nuPVv2WNuyUqFUQF8U6yJx4J1bKKbBikBcFdEgvYgGb_KnCxQYkPtbQM5xyfx2AQfYFyuDx-CbonknPZluWigO8BdD-7pg9CzVhTM70j6ePsry6aqUqsJOnlATU9GAI2b4LC7l3yxVyTkJ1Q9Et-UQ7YWH9sA6jcLBd7u_YZXAcZAyc1AIoWuSB9usyFcr92IXVxWqt-mccHvYNMCRS44aTdg_PxFtlEPYLq1L4sH7JRUfwt0xQbIlwkL_MCPC8OGDeZCvWHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گورودن با اینا حرف بزن نزنن بعدیو</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/funhiphop/84382" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXHqMnAZKnvmZgfgcibtotMUAuOcm5v2pkdrqWyV6eaPRqKz5jf0zMQHlYmqkFsh-4vMptXMnUP2S7YdCKYUKhYHrIy3SjpcrGvKUR_hnnBMmraLo9fTMkA4oVkG-njD6d3BLQLbx9xzXPXMvRYjc06su3j5AshKOx0e53Sds6ouTgkfqy-ndOdlFJ1hgMJY_9Zzmhxx-9i0ozcGE4jzkaYJfCObolCg9Shffi9S-WwcOqOD_P8vbVjgNQCDkI-PJ9FZahMhYRfB3OXKLuMFHLB_tG9hLhXMYQqC1DNL1YN8LBnHDy_xj-9yMoUDlurDhbelS73vJPLifpJHICodww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
پ.ن: بیت بالایی شو هم کونم نمیکشه ترجمه کنم تورکای عزیز تو کامنتا خودتون کارشو انحام بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/84381" target="_blank">📅 20:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بلینگهام داداش لوییز انریکه رو میشناسی؟</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/84380" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YedkJHb9jPYv_BFjLoLPbORNek4AE9CXCOW_Z6kAqKTXQdGwJNms3MacbOomGHFeibqiR4cIj2YKbO-X6fx_Slhwkrn-4sFwaM8nY1V2GGiFiWepKy2sBvwLEyUoqT6ohI4tV12pKxh7xpfDOZXPYnhfoidG2a5lqBH_1zYtgbpEwy3zCkfAWin4g2V2mtKDSbFCc1Sl1mno2CPk7TJ_EHvo01IfiAHqAsgIniN6bDAnc_bd9-2OBZPWexYSXREjO8akYlArWgx2WJcitbESblUdZz00EUal-MQIuEKEatpOYr_ipZrzyJP1EjTM_q6534911KRqqNTgIn9FIU79xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/84379" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترکوندی شیر
به دستور بانک مرکزی، نمایش نمودار قیمت تتر در صرافی‌ها متوقف شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/84378" target="_blank">📅 19:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=bQxZiuELLBTBwkzWh7zPRRBmnmo5gzzS77SBOHYEDHUEfbM2sFRrChVotR4kOZnMpDyDoVAaFS1SxnU4PeT8snVOYlcCyhW21boXkDnBM7TivwVFYaDvIfXSPPReMC4v_DDJdDfKJeCferYtTAWwYUlFAYIajUByR9EsTRMVWnN3LYNrDG7CYcgdydFZHsgjsuGjharJUPaugm_g8GKxUGa1ejodmSgH2w_Tjl7kvSyCYeVEumY9YpyslFEge1WCa_kcjv0kwnVbQN6dSq2cD98r8FwO7nODeDTuZLCNSzrOhftat-gXmgsZmORBm0EiB4AvUeaaiYCv2XJZq3pvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=bQxZiuELLBTBwkzWh7zPRRBmnmo5gzzS77SBOHYEDHUEfbM2sFRrChVotR4kOZnMpDyDoVAaFS1SxnU4PeT8snVOYlcCyhW21boXkDnBM7TivwVFYaDvIfXSPPReMC4v_DDJdDfKJeCferYtTAWwYUlFAYIajUByR9EsTRMVWnN3LYNrDG7CYcgdydFZHsgjsuGjharJUPaugm_g8GKxUGa1ejodmSgH2w_Tjl7kvSyCYeVEumY9YpyslFEge1WCa_kcjv0kwnVbQN6dSq2cD98r8FwO7nODeDTuZLCNSzrOhftat-gXmgsZmORBm0EiB4AvUeaaiYCv2XJZq3pvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چرا هرچی خز بازی در میاره بازم جذابه، خسته شو دیگه کصکش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/84377" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حالا سریع و خشن هیچی، باز خداروشکر از دوره ای که ملت با سری فیلمای یوری بویکا فاز میگرفتن رد شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84376" target="_blank">📅 18:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwTP5bOPhP5kL6dsiTO8h17W8nsZeQTT7k6WmY15QRx07G5G-NaOmevA5-rjlKfl2_chBjXhYSeERmtjX82y5Og5c7LJQ7cxqKbv0DfNul87gA4AWSayJNqpAuB7XaMTafkuOKYOn6MkBQS6TZcVUooUQsUFUEoHlSpgHKbB7Y6WI4aXDv9MRrRF3vXq5SpBffpqduxhS8_76cEIBb_jO50QQBDozgY1QHcF0cKjI7BWvM9byRkIeaHfY5ClKZeZN6lRLvePnqyn1dC6LfCYoXEW2pIp006uTPlIJiWNX8GwZYjxu_SlIhj0MHU8rSYq668TsbcQWGP8lv-wwwWw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شید ناموسا
سریال سریع و خشن در دست ساخته و ۲۰۲۸ منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84375" target="_blank">📅 18:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=rVyb0dzNXUXB5YDIhbOCSXM6MGHy1B8XsMkVRlFWlI8TS5GNxc-4NjpS7ffA6FhnETsmeNCybU443Z-zRqs9fmCV_9YzNcWV0RTaGnnO7ZRdbux-ImNbA7WWwHXZ3pd_TQEB_yqf9GvAsg6MWoSGkWoa7bLVIBQ9s0zWp__cGF-O6GBuIAstub6PMavL4z4XLxJom27ralDPJ7ZybkH8vorxJLdRxCn94P1hih__Xv_iEpejZ6_M8dDMAOor329zlS5n_pMoWlatpniM7bWQskDDvdBAGWZMKo1zZ6n15GBJWI9iXbi2PWt2Fi_Od3bDBqyczXHfhvi2KF9mYWiQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=rVyb0dzNXUXB5YDIhbOCSXM6MGHy1B8XsMkVRlFWlI8TS5GNxc-4NjpS7ffA6FhnETsmeNCybU443Z-zRqs9fmCV_9YzNcWV0RTaGnnO7ZRdbux-ImNbA7WWwHXZ3pd_TQEB_yqf9GvAsg6MWoSGkWoa7bLVIBQ9s0zWp__cGF-O6GBuIAstub6PMavL4z4XLxJom27ralDPJ7ZybkH8vorxJLdRxCn94P1hih__Xv_iEpejZ6_M8dDMAOor329zlS5n_pMoWlatpniM7bWQskDDvdBAGWZMKo1zZ6n15GBJWI9iXbi2PWt2Fi_Od3bDBqyczXHfhvi2KF9mYWiQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دست این پیجای ادیت اینستاگرام
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84374" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روسیه: به زودی میزنیم پایتخت اوکراین رو کص باز میکنیم(
چند ساله میخوان این کارو بکنن
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/84373" target="_blank">📅 18:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aySvMuiukOi84XB777aclXULa5yw0RRF9Xud-GNg3o_dbsSzlezbd4bGAWTsPezyQdYorhQDf_c05wlVtUgOQm2AkMEHG2IOmhAHMkriQPVz4w0NzUcY-UGsmvENeMpbiOzwW2xmgl1ns-7yxquSN1MFvGBBcmdDBclh77YoS0MkjYWLE7YKB9nRdNoZO1PtUKBluxfAGh0TU7e79CNcKpyhnzD6fiduCBWZzS9-XguBxvJ72mPKLG_9gT2O94aUrU6aA_7k4MN-jsNroVD9JNwhxiPV2hyZZ1Bo_zPjX3EkacjYTeoljYy35olPVCFT5LjrPKeDvK5g4QM0BeImnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا منم با این تصویر موافقم، به نظرم قاف باید برگرده به خیابونای تهران یکم جنس اعلا بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/84372" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84371">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/84371" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84370">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAsaoDrXySAskFquOUihmIdWzMe1FdAHupAhx8mKS1mt6YQ_rbGm7dzcx3U4itsPsxzorgoBLHEirB7tsKAjbxvn55O2mPv-uNIxLrjQpTJHkEcAtHtvOHC9YZvwiqbdmt8U1iwlBeN2g57_9ikFIQ6gTeoP38xLu_UitGWhl_nx24nUAN5uef5DXmC7cftiCpZu0DTtrIvMc7zgVabB6yzIF9yNDokhhRwEnIkIya3yoaV8FNx_1oSOqooyUXchy2i7rZ_AurKZlMTxyjTW6XxUMiZ1PNn0Dr5H8LsvnsWYvpW6-EcyhqT2azfAN8bZlBkuHpgYWcXWT3uC69kQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G11
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/84370" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عجب هواییه پسر، امیدوارم عشقتون تو این هوا بهتون زنگ بزنه بگه ما به درد هم نمیخوریم خدافظ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84369" target="_blank">📅 17:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qts9kM6_tdn5tNvUeuuq8gADpXjGXxBHH-M6yYbnkv9pWZ_q8v0K1CC8bg7-gtmO_Aq5k0IT2cipo8rXcs9kZ4NqcVTYBp9hTqocy1F79vQOoiKpK8yhS_UeQAV0XBuM6xfjuOmvxytdEfhYUO99FPiYBV3IupwgrS3zGGOx8A1HSSvNt5rARv4n0pBdcxet7i-uD7fPu0Yuzsau5mpZFzf2ptPwkkcRg0f7YjBOK-mikjCGgv5mopbe60cNG3_nCsWCDUVr-iKXELzBEbxqn-us0MOZeM73ueo9VwuixEhR1Z_vxu9g9K0uc5qoZYIBK0UqMNIK-RIx4G6xmPFuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال the gentlemen پیشنهاد میکنم ببینید فصل هم ۲ تازه اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84368" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگه مصاحبه فرهنگیان دعوت شدید همین الان بلاکشون کنید، بعدن میفهمید چرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84367" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این میمای کنکور چرا آپدیت نمیشه، هرسال موقع اعلام نتایج همین میم ها تکرار میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84366" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84365" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk1iyzdtE1orgX1mY5GhF6y6vdeH8EvJCdCO3tS3jcZ551WrC94Vcz6RBSHTYlwCb6nH4dz83qMqOUE3uIRMgvCtayQvDbSr3EVB8s6swUvkgllC654eCPBVGU1dijpjpCUTlxR5gpS67foCUFPvTM_4zFzfQaHTnM4ugtFt_H3ZF0ZrFx6-0_NWMIsYC9C3-WxoGEmOaP7L_LFYUcqyZmfpmxwXJLNIAQhAC7HVmkhANLZllEYR8XoAkxV6QF3pBg4I4fYa0Bgf1EPww0pBs8Ot0JfV7xZkP_fKxkG6hUWJpKn-83W9fjR_1YwACRxKAa9zv99G9wgsV90CwmIPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84364" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik-7VwS5QIswV4lu78894fKwVT9gmZNWaFQES6vBH8iLpp4oCjS8RxZ0KoLVGlpAiCPvvRpa6E-xfQZVmSxIJXupca3pGOEZ9bCFXdd_in11YIeyot3dfvdckkvJLop6CMOhsHWKdWRhklsGDzdD5FF6hNluAdA-Mt_KtJYNQ99SEyfEpcG12XVWIEbUirZPeGeD2oFdC5SrFN7_RZrQ_LzPdwdzYGwVM9-Om7IJGqjCL6yNqEB4Kv1AXyBKwHH9qnhi0zKjQJiqgyRfqW1z32WLbzPHxVYFVtUtP0euOnsk8mjsS1uk4oAH9ngC0THwatonM5y_Y74s2micpTdLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84361" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTileKhersuk🐻</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnFEjoq7H3OGfgaasW3Gsa3iaW6oTyWCgYG2ZmJVvWnf6MwxKygO0tmHnG_dPzCPD9JXPMaknlfNTavai44MzLswQuueH0xAhLmYVUAl7nxHQqbMaXd6MCO9ThWFcI-tIFTLbi1bX2I4zBAVtku1b7njc-OQYNKhXDvZ-HNvjPZwtBcE_my-RnqiayxyoX0AwD72y9O_JI8nv_UkVg51Db1c5_n6BD7bv9OXs_8SSJ53_oOGOXbawxWGhze_7YYgVwtGmOk843ERsD9-T185x2ocoVRdArm9faQRSHai-ccifuHxp0jfjsFJVyBZK-lg8GUkyNluYRLWBYyc3h-6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر خوب</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84360" target="_blank">📅 16:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتایج کنکور اومد
بفرستید ببینم چه تپه ای فتح کردید</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84359" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جردن های تولید اسلامشهر که مسخرشون میکردیم هم دیگه زیر ۴ تومن پیدا نمیشه، های کپی ها هم شده ۱۵ تومن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84358" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بسنت اومد گفت تو دوماه آینده دلار ۳۰۰ هزار تومن میشه، همتی در جوابش گفت آمریکا هیچ گوهی نمیتونه بخوره
حالا دیگه خودتون حدس بزنید تونست بخوره یا نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84355" target="_blank">📅 15:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان استرستون برا کنکور رو درک نمیکنم
کنکور فقط قراره انتخاب کنه یه بی سواد بیکار باشید یا یه با سواد بیکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84354" target="_blank">📅 14:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ux7WyYkqbF4xlNOW5NuGg2qTdIyYqLb8njU8ZZzF7SaCDRWVhiavj56QaSnhTbIk-A6qrqg5uIy_rEgNHRYsgMuWaKw92LDjd3cOGTHWNxdN-N8wD-WAthKZ8PceSw8uKhrKI-HsRQNCjFml7d4CqrHlTRH1ZhLwQtnmhmx7rcwCaAd3ymh2SUPKtOBx6ABJpWv7w3CVBpPzbxq62OjqTtHSk8-7kNlPjaSc1Hy-PeKzuDN73ZeJSdeS_X73BmkKH0QODv7QZd7dZo_dJKqnA1_j2uzi9kfDuqmXJzF3J6q5oedhokRQAb_ydPZrlBhR_mA5IBJgmSkkyci9o_T8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنشنال یه گزارش جنجالی منتشر کرده که میگه یه جاسوس موساد به اسم «مهدی نادری جهرمی» وارد دانشگاه امام صادق میشه.
بعد از یه مدت وارد سیستم حکومت میشه و انقد خودشو حامی حکومت نشون میده که بهش اعتماد میکنن و نفوذش بیشتر میشه.
انقد توی فسادهای حکومت و مالی دست پیدا می‌کنه که دیگه از موساد پول نمی‌گرفته و حتی بهشون کمک مالی هم می‌کرده!
حتی توی یه مورد به یکی از نمایندگان مجلس ۳۰۰ سکه رشوه داده!
طرف توی انفجار کارخونه موشکی ملارد، شنود فرمانده‌ های سپاه و نابودی برنامه‌ هسته‌ای دست داشته و در نهایت از ایران فرار کرده‌.
و یکی از مدیران اصلی برنامه معروف هفت هشتاد بوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84353" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هروقت میرم اینستا میفهمم نسل چهاری ها بیشتر استعدادشون تو بلاگری بوده، شانسی رپر شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84352" target="_blank">📅 12:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیگا ها و فلسطین فن ها فرانسه رو دارن بگا میدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84351" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1jmAaoHeU-P8YYUnvAVvhV2rNJYI2gaj0Fgi86tYsFUvhGXzWlpQocNU88CGEaE2PpWcNsRDBvXmARdQycTAzXL4ZLtRb7aA0hXGEFyRD2YOJkHLgOfDBIVCHUB24lydvCSGBlpXs4v818ljBlY6vL6Ta8jsIYXDf9V2lmIdVYAZ9JRmvfzuTxK9wGSCq8b4RPN4p1Jr70XIDkCnnqJabV6hPNtEx-7_sjaPSLCrL491R9JogVneSqBdKhjw0-eGs0Iot9MsJsNkoO892Y88wJY2IEfap0FZHDdOTSqlTX8VfEsIFnLpX-QV4aBOKSNehor_sM81mdi4j7NDve4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا کیرم تو این اکسپلور
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84350" target="_blank">📅 09:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=q5-Y3OZF4bD9dekC1JHi3uHOWaWsW10cUZYfTU2yDZ49bBdtu8dO1RnBqK0sNG7JdrBg2A4UVhEwVUlhdHNSmUl9E1EDxbptYLmGIc5fiBBc6vUb3yZX6UBEgqsx2h3eQqJEazMcu8kBldveds_0u3A2MblnRZXdfh1ttvmC8j5IHfLDUUtqND2NJE_COeStRken40M-XVG8---WJh6o2En_Gv8f61aXxHkz05Ol1nfCFsgZzXIxezJp17go_GGm1gmBWpYfKZEpsutLyGySLu-CrmzGWuYeHdmzkf80K8xO-oeEfI8212wAZNRGefcPaBTVOvvPvjFLSOAXvhxK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=q5-Y3OZF4bD9dekC1JHi3uHOWaWsW10cUZYfTU2yDZ49bBdtu8dO1RnBqK0sNG7JdrBg2A4UVhEwVUlhdHNSmUl9E1EDxbptYLmGIc5fiBBc6vUb3yZX6UBEgqsx2h3eQqJEazMcu8kBldveds_0u3A2MblnRZXdfh1ttvmC8j5IHfLDUUtqND2NJE_COeStRken40M-XVG8---WJh6o2En_Gv8f61aXxHkz05Ol1nfCFsgZzXIxezJp17go_GGm1gmBWpYfKZEpsutLyGySLu-CrmzGWuYeHdmzkf80K8xO-oeEfI8212wAZNRGefcPaBTVOvvPvjFLSOAXvhxK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش هایی از آموزشای جنگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84349" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84348" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1NCTOD08nKafPTtIY4LgbgzMAoeCeuIwdxrWg4nSYRauWX10--hGa3PvspytR50FA5ThjhAy4EebDFm9FoBm43EbszWpdJtwe5GeacBTlYpQ_yqWwFjXfli6FDe6hvawOLM0EurPvmJymnTLXynBy4Ltcr0FhqQy8bLBUl4ggTUBAP2TWYyFZ_re6C3NhO_Jd-5eDRQI-sM43Sr0D9zeJ_GqZ-8Cjpfu10h_zGM4LzJn7w7fcJSM1wQrniq21zgGZYaaTM_6Uj1CDyuigVuKGmiBaJHBVTFIaOD4vGAw1x8v_kuRX_Xj6qX83eHM8TJz6vgV4x0G1Cq3fTAi3Q91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیا - جمهوری چک
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - اسکاتلند
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R11
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84347" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=e9EOPLZfY5vxhfpxWoDGcSeRG_2Wcco9wM7VHfKgViXKLgkW4HOkwwd_UKcOO8155RG1tgTySpUR03IwRfvxStLWMgplIXgSgkVtzVbOVMb8naXGLM8BhiHQ46wztQOI-TWz7MkZ6v2vk0MXUyKxcnmxguORJU52bIhm85T308_w-Y4BlcRVZwznY83GjPMWDvlaYGB0p60ONmdHsqECqBxrVHWype-YOXh-JoseghkfKMcluPpdswTcwHBgDC6f8AEDsj-ZcfLV7Mw_0GgcMX5uJGYpvQZVAztS7Z3YiYM9MoyUvuqmkbrrU8cx1hRBlvYlMhLazeBiF9FQBJ9M-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=e9EOPLZfY5vxhfpxWoDGcSeRG_2Wcco9wM7VHfKgViXKLgkW4HOkwwd_UKcOO8155RG1tgTySpUR03IwRfvxStLWMgplIXgSgkVtzVbOVMb8naXGLM8BhiHQ46wztQOI-TWz7MkZ6v2vk0MXUyKxcnmxguORJU52bIhm85T308_w-Y4BlcRVZwznY83GjPMWDvlaYGB0p60ONmdHsqECqBxrVHWype-YOXh-JoseghkfKMcluPpdswTcwHBgDC6f8AEDsj-ZcfLV7Mw_0GgcMX5uJGYpvQZVAztS7Z3YiYM9MoyUvuqmkbrrU8cx1hRBlvYlMhLazeBiF9FQBJ9M-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز خوش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84346" target="_blank">📅 08:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgdTcaGDZgpMa2f7S9F_wmtS5Xx_oqw6IDOiU3AhCZI1U1lxH3jHrxConvmYsbL4CS4Ti_H_IY5PId9oS_M_e4RdA7sOOWYl9-8eSjEYgVcz_C36IPUCQx1tTDGsfllvx7Jg_s6TyuHZ-kd56-aamDOCzLHLtM-Tc-o_2ppIklU4JdyJOqz21WjwsgghymUfFHzYFNieryyOfbQfV5M888Iy4p5PTzbmYsw36sRJaBVDtZhHLwL9PVBPDuhLs92YUMBTHpamlaoCKFm3WCE94FextJwj-JcRVApc9i67cA769ylDTPG5ok8tZ-nPJ-F5c1-eJCK5Ntqx2TWi_9R7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84345" target="_blank">📅 01:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR3x19B9mdH5BbfFTm2gWBWbCZa7oXQalpYDPRG7LtlIkVACz1JuqL4k1ZNrxKaC0TrPYr0kA5E509LBlS0Pxfevady-ehrROYL3bE3wU4oQPqxmCCroi9hLeezuAiTZOOzLMYN_ajeYYKATsUU28DIkq9-0GORRIIAs3jGGr7iK18MGIdoB165D5J5w4BVj0Fv1io96eWJ1bI301AeuxrOs0OarDLjc1JEzTEYJGYf5EhnLq3nODvhmdP_SGyCT1mSDkp1nReaGqqU2TRRgeYJsllQQyu65NDwtQK_4JjWsOrbI68rmG4kOw2o_nTI9KGC0RgqSzEK_EL6A5qjCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Batman: Iran knight
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84344" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=sATeLC058UlM31rKlBFofK4gjnEZNbA_Wddp9vJA1sbmKiu9YeLQJQUd3PZ021IiYhtnRovkkzNRnQGSBK_qgauULioGcL_K65o-TJ6-fjZ_SLrdwT4k9gMtD5g7iI2N0XW4Lgt7wfQTS5gh9JQgTa3FtB8idRKn76rHhRgWB0LWKPFeR7dtpHx6fep-yPiwHMZJxLsVEGo6hfDR92KjgQDAPFlR4V2VOSc_D8nQjoUyGB3UW5StSTddLPPZlItrmODFrpD4Q-R7uk6tdz_EfNxxJw3_kguqW54QYCa4-O39Xsd0YM8rnLJmmzERpEHAE76jU74cv0I57X7QWs4aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=sATeLC058UlM31rKlBFofK4gjnEZNbA_Wddp9vJA1sbmKiu9YeLQJQUd3PZ021IiYhtnRovkkzNRnQGSBK_qgauULioGcL_K65o-TJ6-fjZ_SLrdwT4k9gMtD5g7iI2N0XW4Lgt7wfQTS5gh9JQgTa3FtB8idRKn76rHhRgWB0LWKPFeR7dtpHx6fep-yPiwHMZJxLsVEGo6hfDR92KjgQDAPFlR4V2VOSc_D8nQjoUyGB3UW5StSTddLPPZlItrmODFrpD4Q-R7uk6tdz_EfNxxJw3_kguqW54QYCa4-O39Xsd0YM8rnLJmmzERpEHAE76jU74cv0I57X7QWs4aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کمتر دیده شده از رپرای رپفارسی که ریلز با مضمون پول رپه منتشر میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84343" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLpVsqv0hnkk-TC7mo5oXQ8uM36rvoVYjC-2U6BcjkbgbWx5UbE04XBJc6Trf_hyokc9r7caNo7FLy7uOcQmNMq5A5MaVhl12ql-rJcALI1sJfravrU1JWNo1lj7432PjBQfZGNBxgPRaQgrn74Dpw00oYBHykqw65cOpJ3pfCLXZF0ORC3CWXhsLGYEzJDPamHXZ_eyM-wpT_AVc63UE4IkivS5qZffyfBWkehkXU-0hzHpDieMWl54dkN6xSHwufElr30YUV2GrAVDT_sy39ksspY-cXk1iF25MURY7JihTk6rlp2i0xMlZ97Ts7WuEbU8Qy_CTqSlrw4hvWs8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
جهانی شدیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84342" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چه عجب آقا دانیال تصمیم گرفت بعد ۵ سال یه موزیک خوب بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84341" target="_blank">📅 20:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84340" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u29jyiSUu1gfBDuQPvob2XufXoRECvgQ0LCEQu3lSywhoQrom1xHcgx6Hzb9-KvrYjLcmGzyLfntr6wLAnqgjE0Tdqx7FF46aJEVBcsE2UjGZbWTT0Yl_u6q37MlO7MRq76pNM20n4hylPMyn-mXNG0EZwi9SbHFayFcCt9Z58DfqsIATtAj0FhO3rfRUeG1znlcvvskCYatAeUhI8tuoXalsMyB2DJVxKFhoQmTaXr6fU5xNaz7S4PzprsaKFOREtvD2xz2H1_oF8xTJevPW2UNuu1Kg2znSxawnw4ePU3VLH_9wDTPEklujLQ17pBfvp5AAddz4O1SWAx9yNyHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84339" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7ol3t1H6HnVmP847tq_UzfMhGPxoGwj1SchrVbLyvuWU82P_Ee8UXBh_nUJADfpU4KKHrBGEYoM-JCI4A4zyNU-X71gKkGDoOaBjsGHPuOJvaWWuZ_7-mBMZ-Vz9eFJTKM0FDLA1mJpuLdJybvY201so0irsqllDFFXykEhBpT_kg7G08U0sp557H4ZOX8q0oAKMcfzq8GtzoiXAxUbtunbFATaWA1r_wCTE5r4Nq2TmG3RSu5ARrHtrdzfVj3WIZAzQCF3ujA7_1jUs8l9ZbXJv2bi-MdFy7IKqdVAEsryhqX-PyF6vXQezElNugidkVzWR-gvNk5ljpahe3GLzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=uaAHo9vtM4OaUDIlEPcyciwsCozLcop9Pq7QCiOFlJf_5BkpZ9nU1OGYYTjPZ_JL-9fn7bAKuGA1wElA_Nt5KZ_sC-ZdD0iZd6HoG63FloXXwBhRHnRQnvTRqeI7Y2TNal6ajS8vLdXRvNE7thwJkSepEc1C5T03lMTLlyNF8F5ptUBH3081e5Q8Qg1xg5EA3mnqDfdIxkR-yK6tRIZ3Y0Wpy-94QRimHIc3GtqMSbjbp0qeUd5o2OisW1PIX4OJEQV0dR3ac7hWh5ieWzHxE4IPR8Mcqam2LGm4231RZOL8q9vyBTHZrqVvq6UuNClv9L7ldgO0zyeoYDz13yFzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=uaAHo9vtM4OaUDIlEPcyciwsCozLcop9Pq7QCiOFlJf_5BkpZ9nU1OGYYTjPZ_JL-9fn7bAKuGA1wElA_Nt5KZ_sC-ZdD0iZd6HoG63FloXXwBhRHnRQnvTRqeI7Y2TNal6ajS8vLdXRvNE7thwJkSepEc1C5T03lMTLlyNF8F5ptUBH3081e5Q8Qg1xg5EA3mnqDfdIxkR-yK6tRIZ3Y0Wpy-94QRimHIc3GtqMSbjbp0qeUd5o2OisW1PIX4OJEQV0dR3ac7hWh5ieWzHxE4IPR8Mcqam2LGm4231RZOL8q9vyBTHZrqVvq6UuNClv9L7ldgO0zyeoYDz13yFzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها یاسو دیدید چقد متواضع و خاکیه؟
یاس:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84337" target="_blank">📅 20:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26448031d.mp4?token=AwQ3hLJpXD4B8Kn9mUg6wL5O593xqzbN2DxH6rfdN3KnbWCFoiN7q4O93KTbJ6MpGam9xBF8Ix1qX8l6XPUlY5KL-R6bKR0c-HtuVGPYpJuDEsLyWSwrC2eF-ZCimZUL3F4x2rutIbbYwNeq70w8ptCUqugiYapd2C-Dnx10_biMTTFKzGiONb28uASjou5i_7_TAeKehIhZABqbp-hJ33h7tPwuFho_9uS0Aax3w2Pc6SvRSi4gpd9S45sJ6s9-ijB06Vxxt_FwubQVb3Whjr6soSs-1ws-Gv9WxA2qt9TZW36jCY-ZObeDun2uDiMJgfSCV2GMI46TIaSghPxdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26448031d.mp4?token=AwQ3hLJpXD4B8Kn9mUg6wL5O593xqzbN2DxH6rfdN3KnbWCFoiN7q4O93KTbJ6MpGam9xBF8Ix1qX8l6XPUlY5KL-R6bKR0c-HtuVGPYpJuDEsLyWSwrC2eF-ZCimZUL3F4x2rutIbbYwNeq70w8ptCUqugiYapd2C-Dnx10_biMTTFKzGiONb28uASjou5i_7_TAeKehIhZABqbp-hJ33h7tPwuFho_9uS0Aax3w2Pc6SvRSi4gpd9S45sJ6s9-ijB06Vxxt_FwubQVb3Whjr6soSs-1ws-Gv9WxA2qt9TZW36jCY-ZObeDun2uDiMJgfSCV2GMI46TIaSghPxdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برام سواله یمنی ها دنبال چی میگردن که با اسلحه ها کاری ندارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84336" target="_blank">📅 19:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سلطان حمید رسایی را آزاد کنید حمید رسایی را آزاد کنید رسایی را آزاد کنید را آزاد کنید آزاد کنید کنید  آزاد کنید را آزاد کنید رسایی را آزاد کنید حمید رسایی را آزاد کنید سلطان حمید رسایی را آزاد کنید  #سلطان_آزاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84332" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فان ژوله غیر فان ترین شوی فانیه که تو زندگیم دیدم</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84331" target="_blank">📅 19:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpl_M_E0Zjk9C9I18oP6kcXsUX5w7RYJu_eHOi2hg_IPvmSlNSAZrAJfwwdVfgkHnjN8RbjD8pvvoVrS8McHGoQuV1QFBvi-cv5sfrAnSqXxTnWQErWVJq39hucd4QxVz_g9NbpZSDzgD9bsB9FaG20mDMcHisJBiTMB9MXMWyOaxaaF1VeFfj7tnlH7A7zzZ3UvTYNitNsueyzlZdLdChPFjVglOXEmmoevks1-RYlafVgPJpjpLODYfk7RBBgsBRKwAwlOvbAH7Ddl9OcjY4RYENEMjE2kWTWtUgIkLzAMhHwOQzfmCxUTd1w9P82AW_wAkKydk5aFDsOmnUdq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران حتی تو معروف کردن کصشراشم پسرفت کرده پسر، از این رسیدیم به امیرمحمد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84330" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA6_5YrGdYA5QANHIUWhORmckSB8AN6NUwtEWMq9uLdz8Ppq0fvhIWHVTut0oE9-8IAX29YOWzfYzHJR_CEBRw1lD9wObawsfIPPTAISh1GWeef_tu3jF9GIvKnTlIQq5nS8T5voHJiYEq-DoGW5sqPdm-tBWce3p7jWbLwLE31CECHCeSzJUbgijRcJfrpUnNKp8V4QxBgiQO0-qKWQ-G34IJx3i1lgrxw8jLdCujkD58Vi-WkCeDQuC4qTEsphfVHZs9eCppRgp5cxlKoDI9JmpKoS0TK7BQuUQAGspCwxymZawMD8jeJiLbcf7QVYhYg94EnhLA0_02oZ7XisZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oa0TEOVLxPAd8GSy9nA_iclwUm5kUj4t5RwaVhfFGP6uw96rbKuQxrpydVlTX0e2PFVel0INozaFht7Cz_WuWflblt-U__Mi4tYu7Y0krO-apBFVrkeSWDbSTOvR67xjqhlljMaa4HdHOoY_3DJcuanS6n_jTk2pA7eHVQ3n9MxF8eGuz2cjaf4QFxy8lws5_bBSjB6UH365UB91EqR4iJUeS9g0FQKjWLqY2LTAMLc7OMZZpnCFK-IsKXRXTCxdCx4abOmgRey0TRunKgs7yqb7d9QVtyM2ds-Bo06I3DTCrbsijLDK62MX0n8jYcfsUlihB2ARXyOacIS8MTlnuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترند جدید اینستا اینطوریه که دخترا دارن کامنتای کلیشه ای و کصشر پسرا زیر پستاشونو متقابلاً برمیگردونن به پسرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84328" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84327">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3qzqfkdLr1zs41qE1ZiliV0zv9KdDkj1f4o1tAOwLyb9RbJmXy2BpygfXxyiI1YIr6nyU4G8XgA8x3xPCn0AZcTNtczCXJnN1fp4Bz34ydDMS4MISineOLPfbQ5BFaax7vt3Hl4BEyII6VovHx-qcwP_pi_dsbWJQAKVkZtbmiQl9MEUD4oVg8K67_pHLaoO9njZhooyowf08AfmFanA-4lQoJQ1ygS8pWTLWsM9tyZQ0Pa-qnNvtL9h4HIc4RUz1Uu1SUsxK_w7uvQOyFz-bldK33zY3cLhyUaS5HLyOU8tuSE9fr57k1khOiiHUKlLgb_9zWFizXa3lzyuLfeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G10
🅰
🛒
ورود به سایت
👇
✅
https://ewreioxko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84327" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرسی: شایع اون تایم برنامه گنگ گوه میخورد که من اطلاع نداشتم برنامه قراره از فیلمو پخش بشه، اشتباه کردیم ولی همه اطلاع داشتیم که ضیا داره با اون پلتفرم حرف میزنه که از اونجا پخش کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84326" target="_blank">📅 17:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=l8v6UXMpUfbmGfdUP1dmB8UengiGbau_pAiAKgU5GXlXl3AYtsoZrTUge2YcVL9iltQ7Mv6zHQb2qX7L_IoE7bn8dgTac3ZWrsYZklMGUXxXjd6009UV014SLhx5UpRdqzVklNq9vijFXMBJIBrkU4Z9SuiorrJFSosmSoDBG5tpc9fpGvtN3rEj8stNdqZQXqE2FnMhJk3vEPssRaHoWTEEMQjqJ4YL4Sj8O1fI_N1Zx1yKvytpIj0RxiVSoN0FmicwzMXML7HxKlKEF5M1xmlU_MK5EvrEGtNWz5kvgBAb_S2-J6Wpam6WJBQdAvQcEC-W3ZpgWyS-EsKkBcqwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=l8v6UXMpUfbmGfdUP1dmB8UengiGbau_pAiAKgU5GXlXl3AYtsoZrTUge2YcVL9iltQ7Mv6zHQb2qX7L_IoE7bn8dgTac3ZWrsYZklMGUXxXjd6009UV014SLhx5UpRdqzVklNq9vijFXMBJIBrkU4Z9SuiorrJFSosmSoDBG5tpc9fpGvtN3rEj8stNdqZQXqE2FnMhJk3vEPssRaHoWTEEMQjqJ4YL4Sj8O1fI_N1Zx1yKvytpIj0RxiVSoN0FmicwzMXML7HxKlKEF5M1xmlU_MK5EvrEGtNWz5kvgBAb_S2-J6Wpam6WJBQdAvQcEC-W3ZpgWyS-EsKkBcqwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی خدا لعنتت گنه بیماریت واگیر دار بود فک کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84325" target="_blank">📅 17:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یعنی این گیر دادنای امیرحسین قیاسی به مهموناش برا ازدواج کردن اتفاقیه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84324" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلار 260.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84323" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84322" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شماهم جدیدا ترجیح میدید یه سریال کصشر و آبکی ببینید که صرفا زمان بگذره و دیگه دلتون نمیخواد سریال های طولانی و با محتوا ببینید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84321" target="_blank">📅 14:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqjhZ_DrsmUsA0xlDVNDbktktO-VZSaltjgbdwUDI2xKGiatx_G2yxabG2USNMz_mf74wv32EE2tkbu-LeLQ_IvOMdp2G0AuyG_mlqXMzEanWrtVv121vqClIIgBEIjPoZrnzJJtjlUTs18HCdEJLyNKAuwhKJKRK3L6ECi1RWPewM-g2X95i_2jGcdgLNtf-yMljfhaUxkWW9szvzV4ur1-x_SAWciuE44H9VfYRqSejodRw3A1JDSZ4QGZzLjb-dk2CmeqqrYB-wnQbh2CTafdGtG8OIrgx7bdwLQsx5bLYDP8RCw-7pVXw8SmO4PCcF0MMS6x9JIy71kPOwxBew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا بعد این که کریر همو گاییدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84320" target="_blank">📅 13:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3j4PUsnu1UQCZRhrB5gOZAu86nzjgLwTr-S7RUNcKazFkawqOKIbzBAP47d0Whx8fevSC9xg_gdBLFH9_VXOl1MZYOqDRYb1SWXuqjDkAbgAKR6n8e0rqXgxYtxNA7FxO83rE_sT39OCzhfsjjmVrA2RzOo7UHb3VbElmR-cEwydfIgk65rVWoh9yatxmT-zO8-4x4cLFG7l-3Q1acT-pM4cYboJCDTLgUxopixPTw9mBRRFiInLqS7B5ZTf8fRqxjIr9YT7nIDRjfTPgv8jAERmy7GDFV5NnoXXT3G7gw62i1SB9OHRhoYufgRnVoTtNkADb6amCjNBFSXLHjGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداروشکر داره عادی سازی میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84318" target="_blank">📅 13:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=TUqu4AFDGI43ZM1VXFtYa_RAiGIpRk9EdyJTOaO1Fnl5GCRnQlnGolUz1yAnqZX0g6ZWcuFsfY_Gf_EYb8hXsheB4ou5fFT3h3VbVZvnekJmHl_aET5Ernt9OR5OltpVSMTqA88ty1XEN4M6PTLJkPJAnqhqx7sVDTX5LcLcIWIiYfIq3RdYt6VwwbzpBuOVh4e6dhy9i79oM2oZ_0eAim8z6Pl8LjAvaBkmU92eslYiV02l0-BjJ-s9WfcVWhjEokWFZb6aUeok2BqqGnYzkzb6I3SyaH41F13fveFp1ahnC5HGdP3MchThd53cQZ5BtI_bAC03v1Kd4Z_hAKcyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=TUqu4AFDGI43ZM1VXFtYa_RAiGIpRk9EdyJTOaO1Fnl5GCRnQlnGolUz1yAnqZX0g6ZWcuFsfY_Gf_EYb8hXsheB4ou5fFT3h3VbVZvnekJmHl_aET5Ernt9OR5OltpVSMTqA88ty1XEN4M6PTLJkPJAnqhqx7sVDTX5LcLcIWIiYfIq3RdYt6VwwbzpBuOVh4e6dhy9i79oM2oZ_0eAim8z6Pl8LjAvaBkmU92eslYiV02l0-BjJ-s9WfcVWhjEokWFZb6aUeok2BqqGnYzkzb6I3SyaH41F13fveFp1ahnC5HGdP3MchThd53cQZ5BtI_bAC03v1Kd4Z_hAKcyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر ایرانی وقتی میره رو کار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84317" target="_blank">📅 13:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=D66rsyHJkvCR62lCn7nGLAgMWkm5ljOvsHsn2Ytj0Ikm7PRTq7mpvFP6SSjusgD2DxFMqXyFWbEBOK1ytd_yyzbTi_oM2IzIJDejKvWiZt4ybxYKJByFdKLfeJQSJGG4AVd291acf9v8Y3ymxVUYNUo3g4ZJtXKIXFVyAC_7V0a65SjSyYuTZQ8qMAX7PJmwQNANFmoIQ5VU4Ug-b-OsOD4S58kh_Dq9ON-HFQrEt-QPd9F9TeK9EgbPEuCEbEXERrGR2bcfPXg_eoS1MPOY5prZkM7G8EADNsRNzmzY2p0PAqF6Fs4H9IgMKtVgwBTpDFaUpX4O833sGOG5f0zcaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=D66rsyHJkvCR62lCn7nGLAgMWkm5ljOvsHsn2Ytj0Ikm7PRTq7mpvFP6SSjusgD2DxFMqXyFWbEBOK1ytd_yyzbTi_oM2IzIJDejKvWiZt4ybxYKJByFdKLfeJQSJGG4AVd291acf9v8Y3ymxVUYNUo3g4ZJtXKIXFVyAC_7V0a65SjSyYuTZQ8qMAX7PJmwQNANFmoIQ5VU4Ug-b-OsOD4S58kh_Dq9ON-HFQrEt-QPd9F9TeK9EgbPEuCEbEXERrGR2bcfPXg_eoS1MPOY5prZkM7G8EADNsRNzmzY2p0PAqF6Fs4H9IgMKtVgwBTpDFaUpX4O833sGOG5f0zcaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقریبا هروز تو شهر های مرزی درگیری مسلحانه شکل میگیره و سپاه اینطوری یه خونه تیمی رو با rpg ترکوند.
امروز تو درگیری ها حداقل ۵ نیروی قدس-فاطمیون کشته شدن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84316" target="_blank">📅 12:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e0832652.mp4?token=NlJv2UlaKQM-T2RvWRaU3N_erZXP4YiZia1onmMMyCCbPkKBrGouElL_-dA2W3U6rORh3g_Z5lFKZNIPA-cJS_4CdUMwYDRzYZFvOxJO2n6upd2dmvJrBVu6cmw95fOAVWNphwqrVay5qsKBhbRzMYawQHRcqqtmxZg-cFGyXtH5oPPfNFXEdAD-oW__JghgGr9iXi0mj5_Q8woyV9GKr6wvsfYWH0zwrVoD11R5BjPQcPdXZQA_pZ7YfyHdqc2LAi6NN6wguEAmbe4wzIj4iUTP67KP44XaWzzUqFrKMYQ3dsiU0yzQ12pSsuOPz27j-tiv-KibtuOwy3jNqTehDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e0832652.mp4?token=NlJv2UlaKQM-T2RvWRaU3N_erZXP4YiZia1onmMMyCCbPkKBrGouElL_-dA2W3U6rORh3g_Z5lFKZNIPA-cJS_4CdUMwYDRzYZFvOxJO2n6upd2dmvJrBVu6cmw95fOAVWNphwqrVay5qsKBhbRzMYawQHRcqqtmxZg-cFGyXtH5oPPfNFXEdAD-oW__JghgGr9iXi0mj5_Q8woyV9GKr6wvsfYWH0zwrVoD11R5BjPQcPdXZQA_pZ7YfyHdqc2LAi6NN6wguEAmbe4wzIj4iUTP67KP44XaWzzUqFrKMYQ3dsiU0yzQ12pSsuOPz27j-tiv-KibtuOwy3jNqTehDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پورعلی : مجتبی خامنه ای شبا به صورت ناشناس تو تجمعات شرکت میکنه. دوشب قبل نیم ساعت اینجا بود.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84315" target="_blank">📅 11:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=OGcLmrPtf2Bvl61GHGTj4iPquEWj9XjOAkkotQ5f2GxOag99Cu9b0X05TJrQd0MnYHKZ94MvCFr8MWHHZj7FE-AIJR6Lj-3aaAJme9DnCtZtsqKjdwtMmDZjtFdCda8Q5ak6NCcWi5bQP7NoILg6kR5YUiZpEywTAnvSQnyPa5oeAuqg1SfsIhwIkS2pkdw2y7AtIK1sXv61JixC-LZ6SDjdLDFwbUFSvIlG_W-z3qh8Bxf0zs79ScFIHy386XEpLlZG-LIvH8p590MFCi3-N770zg2sr-bfc9wtjsciVqdXPF3Xo4ECB9sum-Zyhaf9zWx9RYp9PUKSQnePJvFJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=OGcLmrPtf2Bvl61GHGTj4iPquEWj9XjOAkkotQ5f2GxOag99Cu9b0X05TJrQd0MnYHKZ94MvCFr8MWHHZj7FE-AIJR6Lj-3aaAJme9DnCtZtsqKjdwtMmDZjtFdCda8Q5ak6NCcWi5bQP7NoILg6kR5YUiZpEywTAnvSQnyPa5oeAuqg1SfsIhwIkS2pkdw2y7AtIK1sXv61JixC-LZ6SDjdLDFwbUFSvIlG_W-z3qh8Bxf0zs79ScFIHy386XEpLlZG-LIvH8p590MFCi3-N770zg2sr-bfc9wtjsciVqdXPF3Xo4ECB9sum-Zyhaf9zWx9RYp9PUKSQnePJvFJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84314" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84313">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84313" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84312">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIDj7ySN1CEeRSjR3lsgUnoKA_p2S727TgEia3nqN3l9RsEnKh9YE1wbYpB8aun38dRURgeGncPnWdveN2UTNBnJEknFTexS3V18slWRRozh1N6pn7iBipfN9UIXbdXxZ9pLaJ0jqvBon24hhGiXW7wy9yrnZ48esmORIGUR3btMURQW3ptnuA7AAcOg3oJBl4WJ14iChYmw-vOtuasJ8LcPcgQBmwZOUZGvwoEHFoy7kFWSa-KNZZz40aiI9SYbJ22oEnSi6-OjeMg4zLxXSx5ZYiQBJnpgoHirodsACxO_Hl8RtSCzOb8OEDhZEzTfsemHRCAA1VjZ0avTHVOGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - ایتالیا
⏰
ساعت ۲۲:۱۵
🌎
📲
لهستان - رومانی
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R10
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://ewreioxko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84312" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=T64FT8iRZfS4fXDAGrID9KnIB_R9JKtBgE7Okebnn4RpgozXhoLZzZcnBDAdBi0rpR7GQDsvyEM-ykM9DG3VlFpQYos34tppp6eYorqMnNDQcYi7vpSQ_X0v4LRcBIGFR8dAq3TEZfAXh28Wif8x0AHWC3ALRRdha9bakeLWmZLD_JVg-EesmuUxz7JMz1KZMGxsDDvnneUAleeaG7BlvPByV1M-O2vJaYMEF9rJu_RtV0Mqi-LZgQEw3EK9C1BtCNED5vmlPP37b1x2JgACISEZllq0o9kae2gOCZZtv-vlQ8rAq4T3gCKG_q7CafFJRjK8yPvZmcuCTmMAbEFt1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=T64FT8iRZfS4fXDAGrID9KnIB_R9JKtBgE7Okebnn4RpgozXhoLZzZcnBDAdBi0rpR7GQDsvyEM-ykM9DG3VlFpQYos34tppp6eYorqMnNDQcYi7vpSQ_X0v4LRcBIGFR8dAq3TEZfAXh28Wif8x0AHWC3ALRRdha9bakeLWmZLD_JVg-EesmuUxz7JMz1KZMGxsDDvnneUAleeaG7BlvPByV1M-O2vJaYMEF9rJu_RtV0Mqi-LZgQEw3EK9C1BtCNED5vmlPP37b1x2JgACISEZllq0o9kae2gOCZZtv-vlQ8rAq4T3gCKG_q7CafFJRjK8yPvZmcuCTmMAbEFt1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رپرای جدید تا حالا واسه زلزله های مخرب تاریخ مملکت خوندن؟ نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84311" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=bz5RkGbdKjZSrbwTBoyFhj3BYmX9StHn9x5GDD3Vvlqrf3oqx1k8JH8-XYDYuvFo9IhSXqOFRuskmP1GCVy9kzjvRHX7CM5qkIycQD5vUm793cpLD7kER8q6uOvJ5gt9etQ4Z20bK7EFtKRyVoap573T0NXvT1HSO6zpxaoQKtCKkgsbjYAyqwURvWkuDktANF6Nn1lcDHswnMt3S0-0sA1QhIXWiwB2aw_33p95GOL30_9hKlYyXRCygiUlP_gjt4SIOyDW-6FVVCngtCkPHxGjTuzdTHzirBZZt9BcT6Qa2kbbXZGz2bwH7Hu_TF5Vt6Qb_AY5-sJJDQaZZw8FwmZV3mSQP_vWWmTPCd26r4qmerbZWXDMhBsiINixnyioS8_2Wxheg5rIq67-_-sunEmyhkfQvRKhZV7-bpd9uUrWpPHfDrFHcY8DXABB8mlvMkKwlH9Ees1Wn2dSYJKnkASx52YLiJtIVgvM1Xyw-WT9sXa__oDMc77n1ChtvVlq9DO6-EdLARdSCqNG2NvSCKBX5_yB91lG3hVz6GscTjmEr1jQArawmrS1by9v6Cp6V9dQ6S2QcNtkYNETLqKJMMTKrohQlacLJXp_Kkm7frUOKVjTo2gSnqMb5JoxPda2E0z4tabEwmZIeK-lZ2HS0qBHSeDcVYgxHat1RR7Fywc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=bz5RkGbdKjZSrbwTBoyFhj3BYmX9StHn9x5GDD3Vvlqrf3oqx1k8JH8-XYDYuvFo9IhSXqOFRuskmP1GCVy9kzjvRHX7CM5qkIycQD5vUm793cpLD7kER8q6uOvJ5gt9etQ4Z20bK7EFtKRyVoap573T0NXvT1HSO6zpxaoQKtCKkgsbjYAyqwURvWkuDktANF6Nn1lcDHswnMt3S0-0sA1QhIXWiwB2aw_33p95GOL30_9hKlYyXRCygiUlP_gjt4SIOyDW-6FVVCngtCkPHxGjTuzdTHzirBZZt9BcT6Qa2kbbXZGz2bwH7Hu_TF5Vt6Qb_AY5-sJJDQaZZw8FwmZV3mSQP_vWWmTPCd26r4qmerbZWXDMhBsiINixnyioS8_2Wxheg5rIq67-_-sunEmyhkfQvRKhZV7-bpd9uUrWpPHfDrFHcY8DXABB8mlvMkKwlH9Ees1Wn2dSYJKnkASx52YLiJtIVgvM1Xyw-WT9sXa__oDMc77n1ChtvVlq9DO6-EdLARdSCqNG2NvSCKBX5_yB91lG3hVz6GscTjmEr1jQArawmrS1by9v6Cp6V9dQ6S2QcNtkYNETLqKJMMTKrohQlacLJXp_Kkm7frUOKVjTo2gSnqMb5JoxPda2E0z4tabEwmZIeK-lZ2HS0qBHSeDcVYgxHat1RR7Fywc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا لحظه آخر منتظر بودم بزنن زیر خنده بگن جدی این کصشرا رو میپوشید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84310" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337199248a.mp4?token=IzFnfoeNrKm8BNcxsCFFIOhNgYDAyCSdivJa8mVovfDq82-xOZ4h_o1l_cptSO7G8pj109eHHJ2mVOG9ECetkOK9uiBt3tW2eYooR1Z4cjy9MjHbcIGfxeKGMHRFClDX_BJxfIxwYfsnV10FMWPYNie-rb-Iyardx3e1VJ28MOKt6xrtNp0TPd-kimFeqXA-4k4xBQlP7fmL5o851iKB0iGO7tnuDpvhyld6k2NQQQmdI7Jae_LmWMe8VCgZ-ojo5m29ZIzVCyiMDAxdc7Ka7gzVkg-MjDDQowph-k_zw5XSOVPu4GUSbnE2ZWGFq2ZYB4bFysV7iGslgjtpkuPF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337199248a.mp4?token=IzFnfoeNrKm8BNcxsCFFIOhNgYDAyCSdivJa8mVovfDq82-xOZ4h_o1l_cptSO7G8pj109eHHJ2mVOG9ECetkOK9uiBt3tW2eYooR1Z4cjy9MjHbcIGfxeKGMHRFClDX_BJxfIxwYfsnV10FMWPYNie-rb-Iyardx3e1VJ28MOKt6xrtNp0TPd-kimFeqXA-4k4xBQlP7fmL5o851iKB0iGO7tnuDpvhyld6k2NQQQmdI7Jae_LmWMe8VCgZ-ojo5m29ZIzVCyiMDAxdc7Ka7gzVkg-MjDDQowph-k_zw5XSOVPu4GUSbnE2ZWGFq2ZYB4bFysV7iGslgjtpkuPF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمدی شاخر : (شاهکار+فاخر)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84309" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=LhsVaVD0iPFkrn2mj9gAE4iQ_Uq09ll3vU94Qn8KDcDPeYt2fTiK3S41Q--lm5q0wsklQi8trtypoG4JxjLPCvEYi0AtaQFs6t3GRDaft2b8r9MjxncOA8fetgi_XcYIT4hjI2tjOe7huP-kHc8QJ2DQ0Qt2vv5FOCdr6H3fCCkNvlx1yZEcfJwcCrWhQjDVFTfWfC1gG4TfbA5UJ4z2zjGMgI0HTzbGHAPqhS0Zmt3G9ZMf2CefpUlZb9c4OoZ5RfDQG8Z3ckRNj4gfNzkUYuoYXXA7-kXHZeVz102TqR3kTuDFFHLLAjwBD0KbwfuT-_rNprMrCThDlrQmHbEggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=LhsVaVD0iPFkrn2mj9gAE4iQ_Uq09ll3vU94Qn8KDcDPeYt2fTiK3S41Q--lm5q0wsklQi8trtypoG4JxjLPCvEYi0AtaQFs6t3GRDaft2b8r9MjxncOA8fetgi_XcYIT4hjI2tjOe7huP-kHc8QJ2DQ0Qt2vv5FOCdr6H3fCCkNvlx1yZEcfJwcCrWhQjDVFTfWfC1gG4TfbA5UJ4z2zjGMgI0HTzbGHAPqhS0Zmt3G9ZMf2CefpUlZb9c4OoZ5RfDQG8Z3ckRNj4gfNzkUYuoYXXA7-kXHZeVz102TqR3kTuDFFHLLAjwBD0KbwfuT-_rNprMrCThDlrQmHbEggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=ZrT3ZXbuTtgyuyR74io5VOFaVMcpe5DuZe5n3qrM13kBU8ZeCbwhgAAUjaP1chucgK4-7LLkOH3f-tNE2HgwMT4-Qf6SFhtwso_cXAnlW_ZSQ05q0j57qC-DNv7kpntBmvUCwuf8Oms1K5UH2ndlTQBvWjAiZpePCxBFHCSZVIi3VvbY2omFONQ5DaIZeXj1KpxuczIPYWEPcIs7cUq23Z4wbIFOf19F-DG2rzf4Emt5G1FH1bDlMt3kCvOo0j098iwmyMLWc8eBNV4fAyMakYRz7l2zq0T7Q8GsZR_3CAIUbinxbqnAR3hIMwQPboIrecGIZHjObxirZo5yDsltyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=ZrT3ZXbuTtgyuyR74io5VOFaVMcpe5DuZe5n3qrM13kBU8ZeCbwhgAAUjaP1chucgK4-7LLkOH3f-tNE2HgwMT4-Qf6SFhtwso_cXAnlW_ZSQ05q0j57qC-DNv7kpntBmvUCwuf8Oms1K5UH2ndlTQBvWjAiZpePCxBFHCSZVIi3VvbY2omFONQ5DaIZeXj1KpxuczIPYWEPcIs7cUq23Z4wbIFOf19F-DG2rzf4Emt5G1FH1bDlMt3kCvOo0j098iwmyMLWc8eBNV4fAyMakYRz7l2zq0T7Q8GsZR_3CAIUbinxbqnAR3hIMwQPboIrecGIZHjObxirZo5yDsltyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ7wTgvYiasFEAzG42qaWavo1Ah1RgyiYhSQa5d_KizVdSRtmKF6FmaZaKJfT5zCALEwriLMu-mDj53PK3qzvk3EYiQqSlc-h_WuVhx99YXVYP1ZwV4w9GJTfvV34kz7U8BwF08vwI8PZCCmDoTYTv4k1YiAbDK_xKuD8bxsI4JzQ_tRmozAxqgLVSD911SYit3Kr5G2nhsPvExc3d4cTppTYEMr49QaLUo-HuyC4YThONx2DDSQorimzyzbecCOsPb7d1PMMNNJ9StIMNRSb_n8wtDNzQUa2mpc_hCJcxo00xkvox7kaR0PSCIS6Me7fomgK6znLCjy5LieVijFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43faf33322.mp4?token=gfF5b0ueNAtrZW7qTGFE5WEp-8wTsr5QAbcGcUW-deTaHjVMLiNu-Y2PtxUr_E74q94G9UaJoMjSwuLW1HgrzgLOIR5-eULLxNoBMIvAedxXhDP4mO824ESzUoagiuhPQCsY4BIFv_JsqEvgQzTkqKNSoJmsNYjuN7sQM6mYJMSS3BtltA938tHhM0Iv-FA1HLevqj04ZMFe2ehB4YpOdDrp1yip4phqDPXqWPLImwBRkwzIsB7X0ztvbRwaU5Zrrgv8Vtvm8mayQislAHLSI5kBgP2Tblq9n-Dl9jVG5iRqquOyhip95kAFZXUpzELO2ezcixheuTa6TpDu-PuoCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43faf33322.mp4?token=gfF5b0ueNAtrZW7qTGFE5WEp-8wTsr5QAbcGcUW-deTaHjVMLiNu-Y2PtxUr_E74q94G9UaJoMjSwuLW1HgrzgLOIR5-eULLxNoBMIvAedxXhDP4mO824ESzUoagiuhPQCsY4BIFv_JsqEvgQzTkqKNSoJmsNYjuN7sQM6mYJMSS3BtltA938tHhM0Iv-FA1HLevqj04ZMFe2ehB4YpOdDrp1yip4phqDPXqWPLImwBRkwzIsB7X0ztvbRwaU5Zrrgv8Vtvm8mayQislAHLSI5kBgP2Tblq9n-Dl9jVG5iRqquOyhip95kAFZXUpzELO2ezcixheuTa6TpDu-PuoCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید میلی گلد بعد از حواشی و شکایت های متعدد مردم با کپشن: این طلا، بخشی از طلای میلی است که خارج شده و حالا با آن، تسویه کاربران در حال انجام است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84298" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لیائو کصکشو تا ۱۰۰ سال پیش ۷ دلار میخریدن الان شاخ شده شماره ۷ رونالدو رو میپوشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84297" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne1Xmp_OoDwZpjpMEWuNZ0mLrArZ2BvgK9BUyNmAJ9Iwj1IN7tB-VF5lT4obnMoouG58gvrHCTM-M7ET7tL8d83WzdvNsC6CmtJ2Ezq86kGqZFNPOxKdCFlLdyD02rxuEhHf9Fh9Mj19n0qmK0QYTEQ19_vWICkYUidwGiXaIfcp9jlySbANiTtGRkrjCXDUC47GCNzsP4XNEjL-J1Wz5mDK3THmzxBd6Kg72v5fymNVE4iFIQ-560TpKDdFbFrT8_zEqEISmJiIKhNJCTXRwwLPvY-hklT8nNDTx2kDx4EWKzaBUESuJJ1BnjkQiFdaO09H0Akt1XO9GTIulKeoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا جای این کصشرا یه شیر چای تریاک نمیزنن این شرکتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84295" target="_blank">📅 21:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پوتین رسما ناتو رو به حمله اتمی تهدید کرد، ورژن ۲۰۲۷ کره زمین قراره هیجان انگیز تر باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84294" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پوتین: کسمادر هر کی که به ما حمله کنه نقض هم نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84293" target="_blank">📅 20:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مهدی چند ماه اینده این ناوی که زدن چند میلیارد دلاره
یک مقام آمریکایی به الجزیره: تا پایان نوامبر آینده، ۳ ناو هواپیمابر و دو گروه آبی‌خاکی در اطراف ایران مستقر میشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84292" target="_blank">📅 20:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖕𝖆𝖐𝖍𝖆𝖜</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZwNfXhfd8KB6-bdjwJksbcajP4c7AjK_yeectRO71nqlhT7p6zE3XGumTj-w_Z4oFJSe-EPTiTQPMOSf8KHK-3wjtKxCIAs1e6c3HAxjspPrwB66GBxVT26EdeiDwBnqKAcRO52oz8cDAdSUpdq4ktcjoL_brX0G5uN2mUP5ZB341FrQAbGXr-9DvEf6mdpOBN3BG4Thi4mg84b9CvIh8jDEKB5X6KcrltJKtnUxbnwo6fzMd3X8KZ_Wmwru7u4JBMreLa1Qz0SxGgLwMFhetypRTb7p5EBKGZl-eKUZaGmhRHTfMBuLnO7EQxTfNW4Qn5WdN9isqjUflFAh48Jew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84291" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIXRDjw8q1p89hV3YqI4CbcbqAJgqPPXBV0f8cLcgB9nv9UJkZpqP_Pkq0H5cjxE0fGnVDDRLcd1Qo5LX5xvyW7TeRaLwYHhrjqwzMWAIy-JpU7Mj9ChtdieyTiXcCQ0dU0RqhKSe-RAaDzy1-LVZZ9wjhqsYr5rmFEsnJ5i5HNmMUEpAkRHmLQCCLWuRrQ3YZ2halNF8w0qRcaH7ngT77cP4n_Wq1Kdy7mPLHBBOWJOYLRJunpdqM7shaWuNbOa7GvP6FD-dWExpiyDnCIyHucs4Dt086-U1b4gyunOXQZRnFxSR2YfZltwXE37V5Z0Dl4mYefU5cK7SEZlE_iGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این فکر کردید امیرمحمد هرچی دلش بخواد میتونه بخوره بدون این که نگران چاق شدنش باشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84290" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6bPAbdAKP5pFJ7ChQ3QBxGB_JhazDpE8A4KOMN-CRD1h9Ba_sZ-GoCx5dUSYf7Em3dhGcIagOpZvQ4OMBsuyj6euYWAi1aWDIhMKOHKy1KWFDSWfGCgt6LbdCKqXNP8bjZJPdriA_WNfR3HWDTOPQ5dxMAPFI02fl1vzfeLM2QJjDmtKon-QKTRPZI_o9y9s2-HBbg1b-prZ96Edd0rlkPSj6EOkE16hJh-rvR89xHgT8TMtV9Q1KJRvXk8sDWh9A95RtwEkwXHAvM6OwYoSAN_MMAVyxYIKllh6myLNTDhDjDH2xCBWE1mcIJOZNK-fcU6l2Jbl0ZXCiywhyKohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIrrHBZAiOPO7NUG_x1EeoipZccA2EycqyTZXdhC3SybU2tFQfm2TaCxonfOPvC3o_KjJEu6WZrjaIAcL_YnESQgP5_DaC9bz9gp2kbJMmM9PW0knsAqEuKy9xqt3_Bp6vrC4BcnjrjvLgC-c3FaejEaecghWCRGM5-bZWEbIeHLOObujexJ7IPX9RKpBaOfWFHEbLK3nwXrCpEG7otqdCfBz7p1ArBjOizX8WNzZqrxjdR8x3x3BWFGlbRL8cKjp3-EKHZ3AGJslggnw-22I_ie3fpBa4TyRc088QvrMT-Vk0jb0oAWo-GKduN1V88PztFjZd0YYEauiJ0giu4gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyUTF8K6v-oDEh7WUlgJHCOmW3pTkj8GrwnI7UyzVUwUK-iSe90-KROuCMBlWnzXgbwgttepJGCOp-6Kb9Uoo3UwLSY2Y5GP5x3qqjaFtqDoxiqOu3gfEU_Egp6KZDnpU43OhAMk1zSJ_H2AYBcpPy-3cCensG0r_jIqnmXfwed7SZVP4VNW1jsGqRm7xP1mUz_jijD9B3sODFstoWKMERqbgrVDLsGNHMHW0UPWxZPukLeVo9ov3jJaLcyG2m15b1D_VqjobKkDiwWKZsk9I6g8OXbM7sU7tlGDSLhgURVr7JNWQ0-nK2BHIFwweCs-7sgLn6NxLt1aTZT-MYfzVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریری یه جزیره رفته، ۹۲۹۱۹۹۱ تا ازش پست گذاشته اینستاگرامش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84287" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84284" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جدی باورم نمیشه یسری آدم هستن که موزیکای قدیمی گوش نمیدن و پاپ جدید یا رپ گوش میدن فقط.
فک کن حس فاز گرفتن با موزیکای سیاوش قمیشی رو درک نکنی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84282" target="_blank">📅 17:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84281" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJoqVpXaKvOyJD7ecxQq50begPD_W2YV_NAMWTVn2L17dYEZpe4vlkM58WyqX6KeqrIeApMw7Lgl-ceNmRByWlYsGsvgRkTl5nSXVWUQVA-HiLYnlL6rAajwe5F8JXw8vejWJ7IH_IFXAQMkOT-l5_5uMYfofMo0HSpmzI8KDCRCvFVSobwvXFpo4j-SEurGEQ6KSa4PvCu2nos1trFysa0rcGwfwTV62dNDlU_rGgVscTGUL5lXMVLwQ0ix8wa0fcmUNDrxnQCyfvkJmNqgv4TisSosVbxpSzb4RKelGtRg6ts0zZ_FvDSPGX19DzY-AfPDgYCNz58mJvQZ8HNIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84280" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVeESbjSzEoBr3DC7r3ChJZuVEhO6EjoAopAweUZa0tdFpWTq-1ETzg3cggP8ncpfS_NQrJmsoQnfmX1WbmcdrdedeXtzkAqjIoZFWs_ieP88feNRglHuHMbZhMJei0CnqqrruXCAqcLtkvFO4UWCIyWTat7inYp2pFVOB07YJf-TCFIAqKnSTyw9NsPW8hX2Zhwub3zG4y8x33OKlJG8hfGloAJ2mvW8tSl7jajDZcobBCN9I2ZzgnXJ6GCqEDUWqCeY9Ik_1wP6zp3J_Pg8Gp1ZOeHttoA_H7SwXIYx5TaEMNjAacRVjSRG54k87JgfZbqOltO0Gw56drZGoTAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی انقد شاهکار شوخی کردی که مردم با شماره ناشناس زنگ میزنن ازت تشکر کنن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84279" target="_blank">📅 17:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf_XAxi_PocoreT8RJ88FQ_xaXyuhvtlsbTKN2ee3EqeEU6eh4u405UpLKxvGJ0WOvHscDxv7TtGicJuoNo5xv6LgBaBfdTp3Rhd_Ke9Lmp248iUx2VlyjQvLe__5nOw27qHaIaakf0BvFaODxQMwr6C_LPOUiUD1fc91VCmZke4U4cAFe6kRDSOKza9KegJqMgJL32s7n4IEcenVYDlgwVxano5I-IQEpr1M7_dfqVWOH5_WOI298nr0C-8q2Csc0UQ4VCNaxBQHjFLM-wuBwgWp-CfodogXAB5BBkQMs-A2CoPLYCGNjR7wQR5u6-0Kaz8q25A3yZ4adMRX9gjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=DHfIZA58-A7mh5CJwP9_bKdBCbXk8WyEK0X1rc6C84qwXpzfejM6xdhRFbI6YarufJWvof-oKFfXH6SYXtG9bHxF-p015OH01e1BzKjoD9t1O8xREquv94sQyE51Q7OC1VgShvan2SHeY33wlgMiy8LvuPgW8E7Cia4tktunhA0eDl90QH4cDmTyfIEybh4gpaxKUCPzoWbWHwWpkJ45dQxKNoX3KfqVvJRdgQ3Sgpt6JIYG8FgaeaFa5Hd_fqRz7vsB7YoafaDmjLD4l5UEpeErRCZsU9gSBVN1oiPi-BhMJnKjAfXAgIaTE1o1oPpiufz_NdqvFaTrfb_G3nSX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=DHfIZA58-A7mh5CJwP9_bKdBCbXk8WyEK0X1rc6C84qwXpzfejM6xdhRFbI6YarufJWvof-oKFfXH6SYXtG9bHxF-p015OH01e1BzKjoD9t1O8xREquv94sQyE51Q7OC1VgShvan2SHeY33wlgMiy8LvuPgW8E7Cia4tktunhA0eDl90QH4cDmTyfIEybh4gpaxKUCPzoWbWHwWpkJ45dQxKNoX3KfqVvJRdgQ3Sgpt6JIYG8FgaeaFa5Hd_fqRz7vsB7YoafaDmjLD4l5UEpeErRCZsU9gSBVN1oiPi-BhMJnKjAfXAgIaTE1o1oPpiufz_NdqvFaTrfb_G3nSX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید جان ناموسا تو یکی دیگه بیا برو کونتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84277" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84276" target="_blank">📅 16:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واقعا فید کردن موها یه کلک مارکتینگی بود که آرایشگرا پیاده کردن، مجبوری هر هفته بری پول بدی بهشون وگرنه شبیه جنگلیا میشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84275" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کصکشا انقد به پر و پای بلو بانک نپیچید و نگید بزودی اونم پول مردم رو میدزده، یهو عصبی میشن فیلمای ثبت ناممون رو پخش میکنن بدبخت میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84274" target="_blank">📅 14:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZZFZADc3BNbZJ4dxPmzSx_LxIYsO14JyhArVHPe5PdhxsSBAdEpveJKeFVIs5DEB6Jb3jWpFBVpW5mvEl_rPtLdrTg7kgkVhf8VcwvsXoM5o3YyFpfwRcJRKJiXhEWh31zpF__w3FRz74v7NSHcdIfd2keb4qyH5Ai4XYUGvVRwKvTUT1XL9g8cMsleNgVhWMLi--dDH7BcbS-aBHjyYFqN2-LjJhtXpxSJB21qixsylEGqissqDLeyIcBHR37tqkZNT2sr2nDyCQYHlmfA8sye3Qpmq-YMP0H__ktSZRA3c0DNZeyjXVG0tZykj5NI0EFGIAy4etjiXpHPbGV7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بازی دوستانه دیروز کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردن و گفتن ادامه بازی زمانی برگزار میشه که فلسطین آزاد بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84273" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=J4CKA6fggUCqtdBYVVLRdd0KbpzUEvEDz_ERnT5utJ9jXvBlkZK572nMYn8g9OrXy0H4p6qQ-dt01AR44fFqAVGNRwbPHZDgjC_JUg4X-7SHRbN0XXCoCyFEU3Lr_RY0PR6skh7opOzu-xmqzsn_-k9POTN282nuc3QukxlXAjAX4TncEBhzrWvINNSonV5TAOdQnDPjIBcNY9pxhikdCRzYwvffUL-HZ3t_Lrf507t9TZYZuo2MWoGO2pFGm9FYxmsnbQ74OpKwk7SFnXd4f9mmeI5XK7G5rqOlME75hqcfrW6d4lbzF8924smhPdJ0TukXM9Ddsy1Q4xVinJ60DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=J4CKA6fggUCqtdBYVVLRdd0KbpzUEvEDz_ERnT5utJ9jXvBlkZK572nMYn8g9OrXy0H4p6qQ-dt01AR44fFqAVGNRwbPHZDgjC_JUg4X-7SHRbN0XXCoCyFEU3Lr_RY0PR6skh7opOzu-xmqzsn_-k9POTN282nuc3QukxlXAjAX4TncEBhzrWvINNSonV5TAOdQnDPjIBcNY9pxhikdCRzYwvffUL-HZ3t_Lrf507t9TZYZuo2MWoGO2pFGm9FYxmsnbQ74OpKwk7SFnXd4f9mmeI5XK7G5rqOlME75hqcfrW6d4lbzF8924smhPdJ0TukXM9Ddsy1Q4xVinJ60DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آ
مریکای جنایتکار با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد
.
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84272" target="_blank">📅 12:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84271" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محسن رضایی: قبل از اینکه انتقام آقا را بگیرم شهید نمیشوم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84270" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
خبرنگار حوادث : دیشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84269" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgnJ1Q4Bfjhw5MQLc7RRJciVkyoSfWijFYh7rKgXSp3qknGGvQsugtmV0LpNeMfzkVpWtN0xIIelK4w-crOxQBd8pQb0Zy_UU9yiE2byRTvwf6XrQmKZp7Gx_0BjBw-fFjPO075siQlRgt0uh5e4dLqQnkDoXSXZ4-4NChkvYs9vQdiYjEJ54fHa3ad9Nh3dMQBws7luSQ__fkxo65wcLA9WRv2c4T3Gvk8fjAx6qFAUpZhxNOvLvcew32h95Lk_tv-s4byozrlaqbUyc5FA5f9nSh9NP1Fi8b8l1Ru2mw0xcc9nwVRD8gDljUk5Cc9knyeVheCMM9flAE_4zz86WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بوراک میتونه نجاتش بده
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84268" target="_blank">📅 10:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaNg620dbFNI2_TYoe8a4po5rMepEcC5gvmA7uVMIiEAfF48qmUX-YJBBqN5tPIJ7kFbZa3zPZ5vNKaGlcsi93hjxfM-iLb1VAXIauKKDF1OZmiJ8DXA9ckJ-2AMT9LEoJilfBDY71HIz4ux_fVrc9zDkowLZBCGASTEdctFh4xOfHaqDRn8OzDqLco-WquFo-XCu8rlw9w4uVYbd-2UtG36Iq3tTK5bfMF3Y-yWWPrYvFpa760POqlSAgqSq6mYZT_fMv9WGG6H3_nZIn3RsBdSXDnueI15rBnsTvQmxAJEp3rlfHvqiVo4rgpCx9vaUMDppiA5DWjDkbchlxjzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BY_f9E_z1cAYcUR1zGgF4KLzHmRCXZ7qmrRrePR16hfsofHWrvk9OzdN7_8b0VZDkUt2nwrhMdkg03jBYt8AMKvot0wze0mAVUkZuK0weXJ-Jwbzz6GxFsN5-pkaX4ooGDlGJaEm8sfBkbzZDtIk5uG1bJFteEgHMeBniJtz_byhaDueV6SHrxEJAGE450mAeayfCuRBi0DMt4Dg6wsxuyRvtBImiTEABm1jVfZXmuJjApxtVW0cN8UTHfSG8i8GAf7Qs5TOFnHZDjHDvbLngwY7G1GxMdgaoL7e2zA399T1_-K7X8zfTZL2dWdsc-D8P3s4L74BrZg3oyZv-2Zp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzX9yyuesi9kaO9-MxcEyuanFpkZi15AL9pnAG28ICCzpwmtP5CPUfR7wNt0eMc3pBUQxsaSxmYcFvNF0tAgf2FZ_aMbu0RsvhyAa0iJ612VKBg5JWdAb6tOyRtTIlXkBucOCeb3g6Jc29k2OIpBoBXK9nt2AUnEHsA_xj9dB5Vwbz1okE28poi2XaiQ_wM-yXC0p5ZTHrvgG8WdyzVsa5LTIiI2o6zrLjiXxIGgd9g_CvpJWWwfjRJR0F2bWbzXh06kbKJFTH3X9PJ8E7eh9GVQGxuxS2wGdxBfxp-iC4k8MB6LZuR4LCqVtkLG7Sdd2oG0csSKAqWjqybc6_t-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFDhJZ_ibsTBcMnKGVnvW_7e7ouM9MzdcpfKYpnaJabzPlCZFLXMmwJF4k5qLcCabZN0to0H4FPd0IaHPpEBZeZ2SC1Ma-VAHW76msln_o_AyBeg40z4-7dPWl0iPW3faemK9jzUlUf_ic1HZZ1XJCSvdcsdEL8M4Md_CQD_StTWyiSar4zYTx3apIz-EwwU_-VFWOhLzW_Fx3OE39h6D6vYHmQZrNfqI1d3qtf0WjLAayECJwDQb4qrwIgOjJMBoBK7U4QrikqTPjoypFEvz4WVrlpgSg_mNcDKf0Ms7x0FKXEC7kQWxgHdLavIVikPZrU8aYQ_6PbifBHLeqBUEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های جدید بوراک
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84264" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در بازگشایی مدارس امسال جای خالی یک نفر شدیداً حس میشد، شهید رییسی اگر زنده بود امروز بعد از انتخاب رشته مشغول به تحصیل در دبیرستان میشد
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84261" target="_blank">📅 08:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=AhBOM1elJNaqOPB5CGK1tdt9-9xlV-n_A82Dt7h67_cg_Kbtc7cSPdPEfwzPhHPGiJXIo6khrqbwaLCcDkiLzKjpt7wPs3hu7efw7KeXDx17miinjCJLiy8jS_D7PKRwwAoWzweP2HKM6WS2dhaO_WKAaa_DSbjq0qSHJpYbbQCXgsnUXV7k4RAIWoNgcW-cBAWot6bDKj_s7MUrd0hRCXDfDGCEjr0I93bu4QKVg8hWQAWXXZee9Iah7TU6O_e75Ora9ldM7WGDO7A6arrAN8Fo2D6Q8B7w8pf6aSTNDqt9tdwTG5Az_uDqeFyOcXi0GRnozENIiiAEm75UF1Mvgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=AhBOM1elJNaqOPB5CGK1tdt9-9xlV-n_A82Dt7h67_cg_Kbtc7cSPdPEfwzPhHPGiJXIo6khrqbwaLCcDkiLzKjpt7wPs3hu7efw7KeXDx17miinjCJLiy8jS_D7PKRwwAoWzweP2HKM6WS2dhaO_WKAaa_DSbjq0qSHJpYbbQCXgsnUXV7k4RAIWoNgcW-cBAWot6bDKj_s7MUrd0hRCXDfDGCEjr0I93bu4QKVg8hWQAWXXZee9Iah7TU6O_e75Ora9ldM7WGDO7A6arrAN8Fo2D6Q8B7w8pf6aSTNDqt9tdwTG5Az_uDqeFyOcXi0GRnozENIiiAEm75UF1Mvgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل: «تنب بزرگ، تنب کوچک و ابوموسی، جزایری هستند که بخشی از امارات محسوب می‌شوند و تحت اشغال ایران قرار دارند»
پ‌ن: بیا برو کونتو بده ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84260" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: میخایم بزنیم ،بزودی تصمیم میگیریم
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84259" target="_blank">📅 00:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84257">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=W_nnQabLkPQMpVGUrE5V2ukqbeIlqDZi8HBWUMKaS8JBpbLFBL1sjWWMwF8sbMC5ib--mCRE4S__ohBSfihQ-fMeylag52UL_Ftp32YmFNkyYVcROFX-Rm_zSoKURx4LdbNq1gvVG3NCEOLWDak76ncQBhUrZJHuNdMa5PsstOcfTKVm7VK8Hc3sNT5zs1Rit3k_hhD77RqIrgzsTl0Z5AfO56S0BkY8h4wY8y4JIlztKKL6sMVij4BcqBLp5PgafDG91eX8oQKpYwCxNs2VKAWg2RKbyMh_NaTq9sgJsTCLQG5s9OdClA_pOvG4jGzAX8Pax2rdZPc6B4c66VD6UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=W_nnQabLkPQMpVGUrE5V2ukqbeIlqDZi8HBWUMKaS8JBpbLFBL1sjWWMwF8sbMC5ib--mCRE4S__ohBSfihQ-fMeylag52UL_Ftp32YmFNkyYVcROFX-Rm_zSoKURx4LdbNq1gvVG3NCEOLWDak76ncQBhUrZJHuNdMa5PsstOcfTKVm7VK8Hc3sNT5zs1Rit3k_hhD77RqIrgzsTl0Z5AfO56S0BkY8h4wY8y4JIlztKKL6sMVij4BcqBLp5PgafDG91eX8oQKpYwCxNs2VKAWg2RKbyMh_NaTq9sgJsTCLQG5s9OdClA_pOvG4jGzAX8Pax2rdZPc6B4c66VD6UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یجور هرکی که فکرشو بکنی خایمال داره فک کنم اگه استالین هم زنده بود خایمال داشت، یسری بودن که میگفتن قضاوتش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84257" target="_blank">📅 00:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84256">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وقتی از زندگی خسته شدید به این فکر کنید یسری هستن که بصورت جدی موزیکی که توش میگه "بِچه ارچره من بربر" گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84256" target="_blank">📅 23:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84255">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=Nk2ivsL0PDusHRlyDdJh-_fLmMOnKmDmzjZKF_wM5LrW5NC3npQqG8lrFP3qnXZy2ClmDsZ1qaODXHbcUrtVYA9tZGLROXg3glWRb-i_Nv_trckEERNCEj5aQG3jEqxUgzHtiEvU-tt4czX2VduxS4rp_6t-57QNBTRgn8X0hfoYL_okDnc0Cvd4WUo4g3SYYE_KR_Sa3Lj_S6mpbzdLSXEnad15rGigDnTOH0Hw6f222YpUghgcFYYujTIpe_SV-kbXLEk5aAWDQxUF6DF7bD2H1nApPC_d4oxAPd5ch-iOZoSzscoPHA1nQYqi9G0HanY2XlrZePRNzxz4ESybjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=Nk2ivsL0PDusHRlyDdJh-_fLmMOnKmDmzjZKF_wM5LrW5NC3npQqG8lrFP3qnXZy2ClmDsZ1qaODXHbcUrtVYA9tZGLROXg3glWRb-i_Nv_trckEERNCEj5aQG3jEqxUgzHtiEvU-tt4czX2VduxS4rp_6t-57QNBTRgn8X0hfoYL_okDnc0Cvd4WUo4g3SYYE_KR_Sa3Lj_S6mpbzdLSXEnad15rGigDnTOH0Hw6f222YpUghgcFYYujTIpe_SV-kbXLEk5aAWDQxUF6DF7bD2H1nApPC_d4oxAPd5ch-iOZoSzscoPHA1nQYqi9G0HanY2XlrZePRNzxz4ESybjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این رفتار ها در شان مردمی که چهارم جهان هستن نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84255" target="_blank">📅 23:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84254">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کاش شرکتی جز دلپذیر سس فرانسوی تولید نکنه، خر میشم میخرم بعد پشیمون میشم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84254" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
