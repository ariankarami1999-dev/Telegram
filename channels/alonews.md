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
<img src="https://cdn4.telesco.pe/file/o9dZy5nQlUhSL222gtmk9640dRbnHsLVsUe3zxCjFF4TFWKqQp_lbfEj83AuxWBH7F-bqSoDBg3e_aDofWl_3soe6FsX_GxsDmhNyJ_Q_jggjpBsbNHt4jzZzrWlRAmqAKErtRZNKBGHQHrFr95JhJa9tTKvKOY75kUzqsxsdqdJGgcnH3lmm57gESSR1gmZ0P_LPjh594PNKQoFHInAmXSBTV5fPLgDhlq0kzxPopyHEh39las_X5QQu3vylqKd0-iNwwbiHrA8csi6qnfUqkBDRb-mo7R-TDkGG37_NxRr1alp4pXBtszy-gx6HL5RjPvvPSzu8aJ1RKW4Zi8NaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 20:19:44</div>
<hr>

<div class="tg-post" id="msg-137737">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psz4k2wUv-HQdLI_HrHAadbnfd93EU2we5PU39P8HV79SgzrsB7Z2P4EvEZ4mPmvQsAfe15hvccwidkp6-omkDlk3rh6jndNq4yJQKcdTJuZPnyz5uU89npKH-4P_PbqgGXHWcOCiEPne_oijAmSuqATTJmaODdd7o_Vmp05RximudW4ORtAPFqzlkmRcOwhd7dOI0_6bhHBKFAw-FduRa-ZXOp7hfIbCvGyalO5PWUdcwjpXtDGPqCP6vvr0S15s4gJJscrGufrJXRmclu98h22MaBOZJXA_AUN_9wYgWrrWzOrn3RPSbRVUT-eYLTYBSYz8wcVOk-fofkVIMQ5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برنی سندرز، سناتور ورمونت، در گفت و گو با سی بی اس، عنوان کرد که به ترامپ گفته باید با حکومت ایران سر میز مذاکره بنشیند تا کشتار و خسارت به اقتصاد آمریکا متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/137737" target="_blank">📅 20:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137736">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c20258523.mp4?token=OQqmFa-ygj0ojnOEKDVbgzGVKng7zzm1b66KL5T2zCfA1jWDsGDu5VT2ukqxnkyc9BtLY5p52MoQK5J_otIdifdk1vdaSvh2bdnmw97jp4VdMzzlug_cilqAGeaxFdum6Q0vJ9XW3TOp0hWSBRZkyKM8IY-8B40zFUxPA91nhkNgtKbow9lMl9-UQPUVuYXYRsgG_wakWLHmuu8nheIrWOFHy55kWR7EKO78T696YG-z6Vxwk2m-Y-II25-agIcfoiW_uYACH984mDGJISCQGM1nLkyQeshB1jBuUCSmQy4q9HBnz6KZtyK_04Oq0mqMpHijmvt40zD0VN7CqaT1gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c20258523.mp4?token=OQqmFa-ygj0ojnOEKDVbgzGVKng7zzm1b66KL5T2zCfA1jWDsGDu5VT2ukqxnkyc9BtLY5p52MoQK5J_otIdifdk1vdaSvh2bdnmw97jp4VdMzzlug_cilqAGeaxFdum6Q0vJ9XW3TOp0hWSBRZkyKM8IY-8B40zFUxPA91nhkNgtKbow9lMl9-UQPUVuYXYRsgG_wakWLHmuu8nheIrWOFHy55kWR7EKO78T696YG-z6Vxwk2m-Y-II25-agIcfoiW_uYACH984mDGJISCQGM1nLkyQeshB1jBuUCSmQy4q9HBnz6KZtyK_04Oq0mqMpHijmvt40zD0VN7CqaT1gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: تا سال 2036 پول دیگه اون اهمیتی که امروز داره رو نخواهد داشت. وقتی هوش مصنوعی و ربات‌ها بتونن بیشتر از نیاز همه انسان‌ها کالا و خدمات تولید کنن، دیگه پول قراره چه کاربردی داشته باشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/alonews/137736" target="_blank">📅 20:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137735">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت نفت ایران: در طول جنگ، ۱۱.۵ میلیارد دلار و در دوره آتش‌بس، ۶.۵ میلیارد دلار نفت فروخته شده و با این میزان فروش، بیش از ۶۰ درصد درآمد سالانه پیش‌بینی‌شده نفت در بودجه تحقق یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/137735" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
عراقچی: اقدام اوکراین بی پاسخ نخواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/137734" target="_blank">📅 19:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZ4n-JRk1UWmTeorcPErt51x6EJkEUyIFOiepMuLzhmrWk_VYwhDT5jByLA6iTvIPmO-foCvqHv7c1I3wSaHlrZtjYUu-z6X5bWwVSOoVSHkgwvqb3akGbTQd1soJQ8D1WoHmaNjvCx9kO5k3p6DKesoVSaVjzNIh8aDUjQGAp_-ZSpiJwg2-q7ounKPLmzcxKFOQylIRIT6U9PonV5XAp1KEos-fwn4JcV6-MPINXSVHQY1eWRYAR3yZ5YAeV7ZF36VyseORAVz2qWrim5--fwExRPsX2D0LFI851CIwGqFbRZEpyaVD3Zt0QgwPTykudVSS2LV3T-m--YEQpYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: اقدام اوکراین بی پاسخ نخواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/137733" target="_blank">📅 19:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وکیل پژمان جمشیدی: موکلم در رأی نهایی پرونده، به‌طور کامل از اتهام تجاوز به عنف تبرئه شد و تنها به ۹۰ ضربه شلاق تعزیری محکوم شده که در نوبت اجراست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/137732" target="_blank">📅 19:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: پس از تصمیم دولت آمریکا برای توقف گسترش خصومت ها، یک منبع سعودی نزدیک به دولت ریاض به N12 گفت: "ایرانی ها با ترامپ بازی می کنند، آنها به او اعتماد ندارند. درک نحوه رفتار او بسیار ناامید کننده است. هیچ کس روش کار او را نمی فهمد، او گیج کننده است و هیچ کس به او اعتماد نمی کند. همه از رفتار او ناامید شده اند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137731" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmReNP6jA2Hf5iY36An0-H19IXmFoQdQG7deRJNY85Xbbi77UQO0_Tdnz0k9VKsIxWC3TW6Smlp2qgJbzXwQsCfPKFOeq3Bb86f5rD-MBK26dAtXghxQHOq6Y7dR5gSoIxtSvIKdGQllg-BeKctqDUE8e71JklRLVPtX0Wtweq7n1UUFiltmLikOzVHOb09pXPBha4BfMkh9CHSQCvNFdrhu-AdVieGA6lVAAk3FgjIoK41h7LjBPKVLAlwjInOEAJ-6pqWKLmITYsvRVVbiPaNO8QaoSXo3ebrw-gPpbXBB5pKzCdL1RCmb9_hGjqaOA4IMoOsBOlVL4ey1ZRVR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت عجیب عضو کمیسیون انرژی مجلس:  فقط نفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/137730" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137729" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24096cdef.mp4?token=ehyW3yu-PAIXoXDRbw2Luhe0fX18OHODJjTOMC7oK2TWAjEMFtUCWHZIKGHCDt2b36ljrJsUzX1G6JxeGXpvckkEJiiF2p4I6LCBXO9Ln4boIk3fUVvdi0b_FwpM-uhc_gM9gANzsVcYEJk3LTW5wlQGJWBnfxzj3Kk4bvDYpLSb4ovp3xQOvtV3Ik2IcGw1kKk7rkmdOyDgDlvi1-Q_FgUHG96nEDCm80jrQ4HwofVlU2tG5k4OtrIFqnUPgt4vFK99mn_lGiWljO2GFWOePr13VjWUOZL_xcimROI4c87snCXpmPxOuPqAKHQ5nOzpV3TAYxVdABsN1Iys372gIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24096cdef.mp4?token=ehyW3yu-PAIXoXDRbw2Luhe0fX18OHODJjTOMC7oK2TWAjEMFtUCWHZIKGHCDt2b36ljrJsUzX1G6JxeGXpvckkEJiiF2p4I6LCBXO9Ln4boIk3fUVvdi0b_FwpM-uhc_gM9gANzsVcYEJk3LTW5wlQGJWBnfxzj3Kk4bvDYpLSb4ovp3xQOvtV3Ik2IcGw1kKk7rkmdOyDgDlvi1-Q_FgUHG96nEDCm80jrQ4HwofVlU2tG5k4OtrIFqnUPgt4vFK99mn_lGiWljO2GFWOePr13VjWUOZL_xcimROI4c87snCXpmPxOuPqAKHQ5nOzpV3TAYxVdABsN1Iys372gIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
تلاش‌ها برای منزوی کردن روسیه، حتی در چنین حوزه حساسی مانند دفاع و امنیت، شکست کاملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/137728" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نتانیاهو: عربستان سعودی در ازای عادی‌سازی روابط با اسرائیل، یک برنامه هسته‌ای غیرنظامی دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/137727" target="_blank">📅 19:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نتانیاهو، نخست وزیر اسرائیل: اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین، اشتباه وحشتناکی مرتکب خواهد شد.
🔴
زیرا پاسخ اسرائیل بسیار بسیار قاطع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/137726" target="_blank">📅 19:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Fm0CRPoyvAFAPIjcE-x4H59F5Ker7vPkd8hyyLLueXHxAyww1t9J3xRP32QdDnDaor-by4SSex484Hbsms-1Od5Ubkx89p_KH-1DljAKJdBZk6YfVn0S8K_7sQOc1Cl_QTKuWX8TS9kgIzdMqMniCuomLTMEbmH8V_2EmVtfwRvBPrO1fJ8RmUOaX0AjjtKxhisHYSEhHZRH8Ag7DDk4y3-zZLQkdDBV_coJUVJHeCK20fY7sGGrhsfqHSoa7WsdhMk62kXobRKdzfrHpbiFhOMc9h_l2BHg-89GJREiiZV3102ALl8ylXFENtoQaxsAjyd_VFz0cKvRY20x_djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/137725" target="_blank">📅 19:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پادشاه بحرین حمد آل خلیفه با رئیس‌جمهور اسرائیل ایساک هرتسوغ تماس تلفنی برقرار کرد که توسط پادشاه بحرین آغاز شد، طبق گزارش روزنامه تایمز اسرائیل.
🔴
دو رهبر درباره تحولات منطقه‌ای و بین‌المللی، همچنین تقویت روابط دوجانبه در چارچوب توافق‌نامه‌های ابراهیم برای ترویج امنیت، ثبات و رفاه در منطقه گفتگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/137724" target="_blank">📅 19:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59abab6717.mp4?token=EsQlYn12S9VeerXtvOpNYy_LUcD_QLz81rFVVH107pbl3dECRrD3XumTu3SDDkVzWNvakJuDgpLYXtg632dBX_8NMAWnFJKAuGr6jjdYz_27aYdJQ_6mQ8XMcYk52yw2o15GxgLZBwD5eT0ivWDD6LK43SzsQQxzRc2fXqLs6LGhyBBulxQm3rjBYto5gonNKljzdEZs94BZ8C8Bz0gjktZWt3oLjLGhC87w24ot72FZeKiQXEZqAQWTkSTUtV0TAfPnn7kDf165IsagYrT1jQaZH5dpwdlLjVkT2T7GakPn9Zw_mexvhYIG923MhCV7w8HCzs0KJGX-SO-wq0jHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59abab6717.mp4?token=EsQlYn12S9VeerXtvOpNYy_LUcD_QLz81rFVVH107pbl3dECRrD3XumTu3SDDkVzWNvakJuDgpLYXtg632dBX_8NMAWnFJKAuGr6jjdYz_27aYdJQ_6mQ8XMcYk52yw2o15GxgLZBwD5eT0ivWDD6LK43SzsQQxzRc2fXqLs6LGhyBBulxQm3rjBYto5gonNKljzdEZs94BZ8C8Bz0gjktZWt3oLjLGhC87w24ot72FZeKiQXEZqAQWTkSTUtV0TAfPnn7kDf165IsagYrT1jQaZH5dpwdlLjVkT2T7GakPn9Zw_mexvhYIG923MhCV7w8HCzs0KJGX-SO-wq0jHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارتیرمو از فاکس نیوز: انتظار دارید کدام کشورها به توافق‌نامه‌های ابراهیم بپیوندند؟
🔴
نخست وزیر کشور اسرائیل بنیامین نتانیاهو: آن‌هایی که می‌خواهم بپیوندند، با افشای نام آن‌ها در اینجا احتمال پیوستنشان را کاهش نخواهم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/137723" target="_blank">📅 18:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کریستن ولکر از شبکه ان‌بی‌سی:  آیا حملات برای چند روز آینده به طور موثر متوقف شده‌اند، یا می‌توانیم انتظار داشته باشیم که امشب، فردا و در روزهای آینده حملاتی را ببینیم؟
🔴
مایک والتز:  اگر من رژیم ایران بودم، رئیس‌جمهور را بسیار جدی می‌گرفتم. ارتش ایالات متحده…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137722" target="_blank">📅 18:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNJP7GQ-oASFsBaOvGLsz-2x2SCSmMwVP7Cmh-vcVyRH1LGdC5YaybkAlIAyJUh8mkGj2ynL9_rKgeY_1LHdKbdhB3tJPibyBZpmp9W0jVolCEzY5CwiuYZSM1zsS0F-VPD8I_jTqeFoiwcnwmjTNvTcKZBLOVWQ-5VUBpmwm8JUq3mdPNCtxIDm33Z2c-6KExRKIzHY3HI4T1E2yD6Z-0RqdXqoOjs2UHwhVj1dt68X47gKwY-D-nRujB0-j-mWUld0QYI6d5-gqBffOJmbDuw8uKq-ZbMpRBCWJBhEsYFGeeqmUNZ32p4cOlPlGha7b7C15sOt8BTKj5NNUWVxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو عراق یه دختر بچه مظلوم ۱۰ ساله توسط پدرش کشته شد
حالا دلیلش چی بود؟ بدون حجاب تو تیک‌تاک از خودش ویدئو گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/137721" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLZ4Si3gEJbu5m2aAfcJ4OaFAuY1ocRUj_3kfmqdY_21N-0WQvboh5R34She3vWmH4Iv-LA0hHAtKIyIWp2IAwCcUlCFzH8xRrRK-IQ2vkJNouupxKkR4Lq-sj25r6TvK7ZqOEZ_bloiAGRPxmXBb8n6IcQN-34d4Y-_YDJm1RJe2cmlorqr520E4TLWf9enwoGURERM0XVmjY361zMs8DD1Kzl7HivBfaaqlwZBahU7UuW-FColoXFqVRsvsNwMSPhOB0ZkkvxU4Cpi9aRCmwxpRPK1RMsgxYoLETkwGK9i1FX1GaD-opBdW65_h7FKTAf72kuKZqrDS4QCth7ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی با گروهی از اعضای جامعه‌ کوییر ایرانی (کونی‌ها
🏳️‍🌈
، دوجنس‌گراها و تراجنسیتی‌ها
🏳️‍⚧️
) تو پاریس دیدار کرد؛
🔴
شش خواسته این جامعه که تو دیدار با رضا پهلوی مطرح کردن:
حق تشكيل خانواده
حق زندگی تحصیل و کار تو محیط امن
جرم انگاری کوییر ستیزی
صدور مدارک شناسایی متناسب برای افراد ترنس
دسترسی به خدمات درمانی متناسب
آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/137720" target="_blank">📅 18:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87da6000db.mp4?token=flmCJhzw5aLs6AWAG7-DUj1EgIUKyrh2TpChCxGcLcPuLnNE9MkWWT4oEtLnfUIj9aeOkhIJ0VZBmmYzn3NhCjVPWS7BoCi16PBVbPpxmWLmtAHRvVxmSoXl5H0ueQ-X1jm-Tx_L22mClyEZ9rEl4jP7kcNPkUvdFdFbBKynTvGzIaarWY2u3cLCdTrkSDHZZj6BwEQHcqtdN3Y91pBh6QRC4I7bq3pGsFfuFc8WUVYQDLOuE9wFP7esDvnYGgR6xw4UdxR1nShOgec524c8GW6NMTrq-9WOgEy5Ok29NNaIiJgv40-HSdvkSJ7ferEKwSAMW1TV-Q9koYI-NopPLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87da6000db.mp4?token=flmCJhzw5aLs6AWAG7-DUj1EgIUKyrh2TpChCxGcLcPuLnNE9MkWWT4oEtLnfUIj9aeOkhIJ0VZBmmYzn3NhCjVPWS7BoCi16PBVbPpxmWLmtAHRvVxmSoXl5H0ueQ-X1jm-Tx_L22mClyEZ9rEl4jP7kcNPkUvdFdFbBKynTvGzIaarWY2u3cLCdTrkSDHZZj6BwEQHcqtdN3Y91pBh6QRC4I7bq3pGsFfuFc8WUVYQDLOuE9wFP7esDvnYGgR6xw4UdxR1nShOgec524c8GW6NMTrq-9WOgEy5Ok29NNaIiJgv40-HSdvkSJ7ferEKwSAMW1TV-Q9koYI-NopPLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدرضا باهنر درمورد رادیکال ها:
اینها در کشور، ۱۰ درصد هستند، پس باید به اندازه ۱۰ درصد توقع داشته‌ باشند، نه اندازه ۹۰ درصد جامعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/137719" target="_blank">📅 18:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز: اگر ایران چه مستقیم چه غیر مستقیم، چه با موشک چه پهباد به اسرائیل حمله کنه، جواب اسرائیل بسیار سنگین خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/137718" target="_blank">📅 18:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3da6c5df1.mp4?token=VTTD1D-DEAUJyL79Casa6X0w9KkvYNj_gtfW-wlpDXY6KvIaArgPK0TEttVmxuTt4vhsg17P7-j_t6PxOZzK6u5uWA2p1pPbewsUI6iaqGRaNwxvZoqbVm0i0iWvCHy1yoIgSRWLb_fC7le0yi-LijM0PAI92hjjFiTchyr-zvD0NTGGkkqca2ny5nloL4e8ELFcXuGwomphu2hBnQWv3bjUvZ2YHcuVPrjLR4NAgwSVkRzS8rsFmu1-toJUJJJNUgGJgtBNhaAElvTXTX56sOyHApBm3yEX7B9sZvRat-H8Ap3IIUni1ZIYKwWOwJZzJjr3jA4tapL15yyN3bcXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3da6c5df1.mp4?token=VTTD1D-DEAUJyL79Casa6X0w9KkvYNj_gtfW-wlpDXY6KvIaArgPK0TEttVmxuTt4vhsg17P7-j_t6PxOZzK6u5uWA2p1pPbewsUI6iaqGRaNwxvZoqbVm0i0iWvCHy1yoIgSRWLb_fC7le0yi-LijM0PAI92hjjFiTchyr-zvD0NTGGkkqca2ny5nloL4e8ELFcXuGwomphu2hBnQWv3bjUvZ2YHcuVPrjLR4NAgwSVkRzS8rsFmu1-toJUJJJNUgGJgtBNhaAElvTXTX56sOyHApBm3yEX7B9sZvRat-H8Ap3IIUni1ZIYKwWOwJZzJjr3jA4tapL15yyN3bcXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز:
اگر ایران چه مستقیم چه غیر مستقیم، چه با موشک چه پهباد به اسرائیل حمله کنه، جواب اسرائیل بسیار سنگین خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137717" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851a7f43dd.mp4?token=nlC-a3LNevLUrgZ-PnB5owUxG-L5ZEMxc9HJUPUIxYp7sduNT_8shqCTcsBV95_3l1D2dsNLO-tsjjC5CHIGHlsj2M6cNUQ6hHPZhn7p0TbVWUeVhZ_STOQTpoaJM8979Wvb0O3OmKw4v_j_qZ2MRERjxsaCgsXTb3ctx4KaiaxEZugut3s5p-BDwTgI4txsh_R7KjQMVNdGRZ084cVFvODacEY-OSBBhOUBPUzTAcFvsXSueveQ77llqNIAaY-hWAkSKXXAvZxgpbajrOiEwD4RU0-ede3Qb2a42SugCxXxZ5KjsIo_W0ER9UhLAZIO7VsALf6Ep7jOu-vNw3-8HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851a7f43dd.mp4?token=nlC-a3LNevLUrgZ-PnB5owUxG-L5ZEMxc9HJUPUIxYp7sduNT_8shqCTcsBV95_3l1D2dsNLO-tsjjC5CHIGHlsj2M6cNUQ6hHPZhn7p0TbVWUeVhZ_STOQTpoaJM8979Wvb0O3OmKw4v_j_qZ2MRERjxsaCgsXTb3ctx4KaiaxEZugut3s5p-BDwTgI4txsh_R7KjQMVNdGRZ084cVFvODacEY-OSBBhOUBPUzTAcFvsXSueveQ77llqNIAaY-hWAkSKXXAvZxgpbajrOiEwD4RU0-ede3Qb2a42SugCxXxZ5KjsIo_W0ER9UhLAZIO7VsALf6Ep7jOu-vNw3-8HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستن ولکر از شبکه ان‌بی‌سی:
آیا حملات برای چند روز آینده به طور موثر متوقف شده‌اند، یا می‌توانیم انتظار داشته باشیم که امشب، فردا و در روزهای آینده حملاتی را ببینیم؟
🔴
مایک والتز:
اگر من رژیم ایران بودم، رئیس‌جمهور را بسیار جدی می‌گرفتم. ارتش ایالات متحده آماده و مسلح است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137716" target="_blank">📅 18:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سفیر آمریکا تو سازمان ملل گفته ترامپ حملات به ایران رو موقتا لغو کرده تا یه فرصت دیگه به دیپلماسی بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137715" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19b1e9d73.mp4?token=seXWceEFwNzzQKnXvrj2Pf822U4HnrI0ZZ2P7j3umqvSevKxTBKYiOOODANkrF-SzPyzcyljy-5ksQNsEc22wMMgesE9W-dSV-Em1WHeQO7RTQWFkZxOwG1pQz2kRj2hnOaE1dD_YcQCH5wL45eFFhV3cke-g3GS_eZ-JCr_xS5rn4TxAgEF5_wfcuVE7ST6JfZ5ukDoT9bCBgWUDjuJ7HZn0xVpKpvwJEjCutVhh4FOOd3R1QfRWPExJ7-2oNI7FEJrjQn1zQgzcaFd_d-WWfu5ttWR0-9dxlOJA2H0V-q0thUJnyWbKqE1quzSRoQRzyeuqQsOLasUqr1bQCb-cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19b1e9d73.mp4?token=seXWceEFwNzzQKnXvrj2Pf822U4HnrI0ZZ2P7j3umqvSevKxTBKYiOOODANkrF-SzPyzcyljy-5ksQNsEc22wMMgesE9W-dSV-Em1WHeQO7RTQWFkZxOwG1pQz2kRj2hnOaE1dD_YcQCH5wL45eFFhV3cke-g3GS_eZ-JCr_xS5rn4TxAgEF5_wfcuVE7ST6JfZ5ukDoT9bCBgWUDjuJ7HZn0xVpKpvwJEjCutVhh4FOOd3R1QfRWPExJ7-2oNI7FEJrjQn1zQgzcaFd_d-WWfu5ttWR0-9dxlOJA2H0V-q0thUJnyWbKqE1quzSRoQRzyeuqQsOLasUqr1bQCb-cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم عجیب مردم به سمت بازیگران در مراسم اکبر عبدی برای سلفی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/137713" target="_blank">📅 17:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed262802b.mp4?token=aTtuiuph2EkThJNfaob6wMLfl-1TPML6kjXS19eYbpHx06jSlEIxqd1cuK8Kd5PT62xRVr80mQofmbExRC1Ez3k28QL_yTCtAFf8tnIR-7OAD0hJN_I0YBR42zWxDyD-F7NRM08ljDNc4vxD3s9hL0XvLRbMP1dbJ94h77RVLax2esxZXiD7QbKsgS0s7tJNRr7Bu4fZZgSlvCvUB5X0qBvwX3Dt9xcpe91cvH48_DVy_u3ixsCr1gIPFTgC8Z6EESgaGhzO-mcVZ3yfs2Rz-qua51w60Oinhn1-MhwRKmJKgPcUVgesyKAfmNhNow-CniGAGNf781D2rHQwG8uqaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed262802b.mp4?token=aTtuiuph2EkThJNfaob6wMLfl-1TPML6kjXS19eYbpHx06jSlEIxqd1cuK8Kd5PT62xRVr80mQofmbExRC1Ez3k28QL_yTCtAFf8tnIR-7OAD0hJN_I0YBR42zWxDyD-F7NRM08ljDNc4vxD3s9hL0XvLRbMP1dbJ94h77RVLax2esxZXiD7QbKsgS0s7tJNRr7Bu4fZZgSlvCvUB5X0qBvwX3Dt9xcpe91cvH48_DVy_u3ixsCr1gIPFTgC8Z6EESgaGhzO-mcVZ3yfs2Rz-qua51w60Oinhn1-MhwRKmJKgPcUVgesyKAfmNhNow-CniGAGNf781D2rHQwG8uqaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز تابانی قهرمان سنگین وزنِ چین شد و مجددا جواز مسترالمپیا رو گرفت
🔥
بهروز تنها نماینده مردم ایران در در المپیا است
@AloSport</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/137712" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روسیه ناوشکن اقیانوس‌پیمای ۹۵۰۰ تنی جدید برای نیروی دریایی می‌سازد
🔴
فرمانده نیروی دریایی روسیه گفت: این شناورها از نظر جابه‌جایی به‌مراتب بزرگ‌تر خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/137711" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مقام‌های فرانسوی اعلام کردند آتش‌سوزی مهیب در منطقه ژیروند، محل استقرار شهر بوردو، همچنان از کنترل خارج است و تنها در شب گذشته ۵۵ هزار نفر دیگر از ساکنان پنج منطقه در جنوب‌غرب این شهر تخلیه شدند. با این تخلیه‌ها، شمار افراد جابه‌جا شده در منطقه ژیروند به حدود ۲۲۰ هزار نفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137710" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فعالیت‌های دریایی در خزر ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/137709" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع بلندپایه ایرانی: اگر واشنگتن به توقف حملات خود ادامه دهد، ما نیز حملات خود را متوقف خواهیم کرد.
‏
🔴
پس از توقف حملات ترامپ علیه ایران، تردیدها بیش از خوش‌بینی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137708" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اولیانوف: درگیری ایران و آمریکا راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137707" target="_blank">📅 17:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPtB6lflaxaOEO7cRKROWxLG_dy6ZwxLI-fOxMoP0uo7ZQ2-yaohV7UT2C5_dsN88J-W30FxUJI_Oz4L8vu252WFLYW14bUp8kk8OGYT2uTD0V4csJcm5weGkZtNqqWWBk0PXhPz4nwgK0rQ5agQRCKMvdel4Gb6VmIOPUpiK3p8XWmQQYFPUTdETuVA4OBdSiAdJ5vYZNMsGa4woeSPE6I0jPbwikfwel67EJAEKcL2Jz3B_aQLGePTtRoyv-FkX_8auQMrHydeF9oenfS2m4THaCTaWI-lwFRZIKfoqvUhq53v8Co10hLSLWm5ffJKVBFBsZdDjoHx9CuIkgv1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/137706" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مقام ایرانی به المیادین: ما آتش‌بس را آغاز می‌کنیم به شرط آنکه طرف امریکایی نیز به آن پایبند باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137705" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/ الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/137704" target="_blank">📅 16:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
منابع سعودی:‌ ایران به پاکستان اطلاع داده است که با ایجاد یک کریدور جدید در تنگه هرمز مخالف است.
🔴
ایران خواستار از سرگیری مذاکرات در مورد تنگه هرمز، سپس دارایی‌های مسدود شده و در نهایت موضوع هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/137703" target="_blank">📅 16:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع بلندپایه:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه «آن را به تعلیق درآورده است»
🔴
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137702" target="_blank">📅 16:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfU4xEmFDb4UFd1WSFDJABER5cHaIN7VoyhsUEBpyYmJzea8p8kRS_OLk9IgcwPbih5Wb1IS7pdiZGRSRHMQNZepDdj9wPVndeoWqmVVchk4FlGsfqKolM1IuTkMqK5Hb5_eKHlLniJ68V30Z6Ex_mV7iA7hVU7IrhUFCJQHTNNBYCMfkegXeCDhwyyZ3xhVCtXpQS_bMAJ8-qPfOQpiqaWWYzzIcXa48piPbGSuYDuptGUUbV8jbhwoncRCeCbKvwFN-SzjsiSOCl48g_22SbIEBfGUwQR2caLTVvdg8YPX4rjAvKOsS9cQ94WeobbySaHu2kZNCkGOVG-Oxp5log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها تحلیلگر مشهور عرب:
ترامپ حملات علیه ایران رو به تعویق انداخت؛ نه بخاطر مذاکرات، بلکه برای اینکه منتظر جلسه رهبران اسرائیل و گزارش بعدی اونا بمونه.
🔴
این وقفه بیشتر شبیه زمان خریدنه تا تغییر مسیر. تعویق به معنی توقف نیست؛ آخر هفته آینده میتونه تعیین‌کننده باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137701" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAR03uXTFhPVeQ0hHEEpsT4W7oVA766JKtSgaN-SDZnRWzKOhT88X2sWNxeuZTIr4l9cF2PPC2mLp0vGvo1LW2HChmk2CYleK8ea0NxvOe7h6iQZSej6rHy741yprKTMRqa3xpeW5eST9ktfSmtd4zmuQkLAnxg8OKJmi_NS0MXWFF-iTSZUa6kcTY_ZrGzFzePDJRBoVE9z0QbbDm2ld3wFZCNgbuJQq_CXwylc-skF-xdw1HSv8cf-4zljks-eTrc0y1QOJKX3QV0rqyL5u8fIi7pXRLaP0GlU2zKndAPJbwz64AJtOv1GwlLMPh2T_vrzyFX58HHXn7HAecOVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود ۶۰ تا ۶۴ تانکر سوخت‌رسانی هوایی نیروی هوایی ایالات متحده تا ۲۵ ژوئیه در سراسر اسرائیل مستقر شدند که نشان‌دهنده تغییر قابل توجهی در پایگاه‌های این کشور است. ناوگان به جای تمرکز صرف در فرودگاه بن گوریون، اکنون در پایگاه هوایی اودا و فرودگاه رامون (ایلات) در جنوب اسرائیل پراکنده شده است.
🔴
فرودگاه بن گوریون: ۲۷ تانکر
🔴
پایگاه هوایی اودا: ۱۳ تا ۱۷ تانکر
🔴
فرودگاه رامون (ایلات): ۲۰ تانکر
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137700" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل متحد به شبکه فاکس نیوز: رئیس‌جمهور ترامپ فرصتی را برای مسیر دیپلماتیک با ایران فراهم می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/137699" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ES3laskisRInyiLGYWShg_ko2qoIrI-GLeEQDpTqn6U5EfmqUkjDQ5dk7R7SjJUyg8yoEPvFU6goBPT_dYjUrGrAIkQsUBE0dKhSLn-9rRTcz1j6PuhZGmeAHcW8Zef4M6zM0gIV9IkYVRpf3WrnD0uSsqwIZ9dZus1RMrx6qMIIajukp5AD1ExqcoxNjRrE-7BJNcjKAfsYShO7ryJpkRebusOenxFcEyvOAULlpc76SXjsw2pIJl8eAk_LCeq3T6jn8IrWj0Z1OfchDTZHy3qX7TBCugawnvvcSzd4xuga1n4g5l5kpLpZE6SLhUcpR2ZODF4ctYiiMWR_us2jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyrHeisv1KRH0jZ0_n2spCyZLPn9xBKdcYsNgbwzQ_0UOp2bIm-hjaNznyIggUOPKtcRNzOoG3R84ZOCk_GC9OmSY3JXZCBdVvJercuB-KwfKAzpw_v6Ap4_UJ2FEt19IPPSsf7pMhDFfl5xh8GmiTfZN_er2bQ52lv6-Aw0FKWcNhQa62LW5W1hx5L3liZ9G8xLyJQTIPMdVTScgW7rxTvxsJoWUqLPpIrxpne5Rxgnuw0LXmwnmhhgge9pBYIySzGnr0B1usJa83EdwYr_TdzdrFq0ROcQ-5sEfgk1nsRTiveenlfiUvPFW5m78qDnM_U5vmcauH0N_H9BUMMW-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای ناسا، آتش‌سوزی‌های گسترده در پالایشگاه نفت جازان را نشان می‌دهد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137697" target="_blank">📅 16:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHtklxFPGmCGsf65jNdKSOnajw_Qcz45TC9TI1n2JNGI4LxdsOZtd81SuP9UL31pGURbW1Ic2FU_F9OrfuRHU2C1wD2uIL7zDmGztfKnhgSoMKJx-4_jqLw71nirAQl2X-aAjT3dS2GpOEGwPDOOVUvNjS9Wy0XHPAV1vV7GpFcimDZpm9n_zVRmv_jXx5RNXtRMVLYEe903NSpZoFzEjpcXk7MVCq-wV9-F5XkXCMBLcGKd5umr3Urn4Tft_Gdi5_rulGk4rMn5yM3jt5qYoAHGJEu72qrSvW_xRi4jlb5X2BCAR6dnajRL5SvYuU2PSs3c40OgcH8ull2E3KRJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جاویدنام #طاها_نادری_سمیرمی
🔴
گاهی برای «آزادی»، باید از «خود» گذشت. طاها، ۱۸ ساله و ته‌تغاریِ خانواده و عاشقِ کوه و هنر، در میانه‌ی میدانِ حقیقت، ایستادگی را انتخاب کرد. در اعتراضات دیماه ۱۴۰۴ گلوله‌ای که شریانِ پایش را درید، نتوانست روحِ بزرگش را تسلیم…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137696" target="_blank">📅 16:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5797ffb0d1.mp4?token=uaPVIOWSEQWBjeF3oWqNMk9GxryRz6BkmyHaH8LlXOjiWSTq6fj4XJqy38LJXmIhVDBxRIaqMW-skl88fU7bXrUWkjA-1hs-nw8Dw4xgzwtqn87fTb3xTU7pgvLD0LTqHee045jk5iI9tIwR1svU-nVGYVqGyEinH1V7HCQcAi7C8wgMeb4f04_IMHYhlZRqU6qSnbK7gSFHWJAFhPJWjLOBj_Zk77O2byaZYkntoUnqoZGwK7vINjIDE-ODOMAI9j4lMSDLlA43Ll9Ug7n7-XHC01Z7xcp7JwYrhDxH7N3KWwdFlU8FYKmduxz4NbrrU3HmoYOFwm7K9cU093zDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5797ffb0d1.mp4?token=uaPVIOWSEQWBjeF3oWqNMk9GxryRz6BkmyHaH8LlXOjiWSTq6fj4XJqy38LJXmIhVDBxRIaqMW-skl88fU7bXrUWkjA-1hs-nw8Dw4xgzwtqn87fTb3xTU7pgvLD0LTqHee045jk5iI9tIwR1svU-nVGYVqGyEinH1V7HCQcAi7C8wgMeb4f04_IMHYhlZRqU6qSnbK7gSFHWJAFhPJWjLOBj_Zk77O2byaZYkntoUnqoZGwK7vINjIDE-ODOMAI9j4lMSDLlA43Ll9Ug7n7-XHC01Z7xcp7JwYrhDxH7N3KWwdFlU8FYKmduxz4NbrrU3HmoYOFwm7K9cU093zDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگردهای CH-47 شینوک آمریکا
تو ارتفاع پایین در دیرالزور سوریه دیده شده
🔴
منابع محلی میگن این نوع پرواز برای نیروهای ائتلاف غیرعادی بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137695" target="_blank">📅 16:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=tcyG7Nh18zi3ZNdySpKz7j9dPwlUwehovHqo7iOPYZlsJ-7PadTLvMINjo3VE7FbWaMFouXQRdaS-fXo6jbLhyRocrL7z6Xa6ewmKsESGvXWyFubqfugkKC1SS5GUuUTu0a-anvrzQQLb75gRCAVAVGSZ7Wzu4i1ynT_RWR2lpwfoyOPvsGWcz51zuhwc_k-zaDsZRkpbYDYtx4nEmpUDOgjbvklLBpzJ11D4PeAZsHlFN5sCWdlkuBSs78GDwwTa3M7QUE4cMbeHBH53hDqfDpgUo4IQXDxpWm4Cc_e9dkIPMBIo54KtwLuyN0G2se1Cjp_wHVkkvxPmcMjkIXSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=tcyG7Nh18zi3ZNdySpKz7j9dPwlUwehovHqo7iOPYZlsJ-7PadTLvMINjo3VE7FbWaMFouXQRdaS-fXo6jbLhyRocrL7z6Xa6ewmKsESGvXWyFubqfugkKC1SS5GUuUTu0a-anvrzQQLb75gRCAVAVGSZ7Wzu4i1ynT_RWR2lpwfoyOPvsGWcz51zuhwc_k-zaDsZRkpbYDYtx4nEmpUDOgjbvklLBpzJ11D4PeAZsHlFN5sCWdlkuBSs78GDwwTa3M7QUE4cMbeHBH53hDqfDpgUo4IQXDxpWm4Cc_e9dkIPMBIo54KtwLuyN0G2se1Cjp_wHVkkvxPmcMjkIXSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت شهر جازان در عربستان سعودی را فراگرفته‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137694" target="_blank">📅 16:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32055b970.mp4?token=rSetmW7G041ieLtBzfmXRqIa70qgwc8alLJbLpiEqMJ5qSLesIjwCDxG8f9d4NF0SRRscPvfSqRp5YT4tOKf6JjMWA_F7IdtknYzc_8GQFwsk69VNkT93dD9nGXfEdbG8KqvNUCICt3_2mtIBNdu-ecMXNovt9Gb-17__0MGva19YwjX2HSzRG1Z-7sSIvUbxAScfdNM3XmzyRPCVzP4qBIIGwxfdFfs-vt0EkKQxNilMcVYG8fI16SHCbsrLXYy9be7EA85V8Wilz3efJewWN1n3S43CgOb6vXkx5RfYZVf_kcARi7kKhwWWTvZJSk4R9wcJCvVg2fuJPm2CEsS6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32055b970.mp4?token=rSetmW7G041ieLtBzfmXRqIa70qgwc8alLJbLpiEqMJ5qSLesIjwCDxG8f9d4NF0SRRscPvfSqRp5YT4tOKf6JjMWA_F7IdtknYzc_8GQFwsk69VNkT93dD9nGXfEdbG8KqvNUCICt3_2mtIBNdu-ecMXNovt9Gb-17__0MGva19YwjX2HSzRG1Z-7sSIvUbxAScfdNM3XmzyRPCVzP4qBIIGwxfdFfs-vt0EkKQxNilMcVYG8fI16SHCbsrLXYy9be7EA85V8Wilz3efJewWN1n3S43CgOb6vXkx5RfYZVf_kcARi7kKhwWWTvZJSk4R9wcJCvVg2fuJPm2CEsS6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع روسیه تصاویری از آزادسازی شهر شیفتشینکو در جمهوری خلق دونتسک منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137693" target="_blank">📅 16:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سی‌بی‌اس: مذاکرات ایران و عمان  شاهد پیشرفت بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137692" target="_blank">📅 16:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/ الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/137691" target="_blank">📅 16:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fodtex7QUwq6RLixIzn4zqxi3AQmOQqU9Qv2sYyN5xH5j0gVUGqiJtg0AttlGffp9U4HNyW8v0usGPkRbBUDPbHStlXEGKiR4g1SSfm-3JYqtuGzzOSp8x0J4Nfy_hw0_p7ur37DqdfoDBasmA20tK5RdVcMnIROVYlQvaBd5nH6DJsGd547Sx_BDRMJL9LqGobwawrsb-jk9uNSP2CDtWW0S-sdKNeTMODbfXR4Nd9Xkw14UAxH6kYwsSiSHDZnithrphYO6drwT-QZfH0P3vEfGWaHeCAJVMZsBvdtjZtD2SEJUcvQVf-BD1FsoIDA685UWDjFshkLPe9DhjSqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZPASV0NJqJ55iuYfBKP9mdmQBeDY2kKFQZFYnEShEwbRMSLaIeyCtonOdgabct69aUjzVSy0VLMGHT-spaJ13WjHi6lemJHmo6OO49vE_lYBGk66mOPWyzGKuF_aHcWV0bz_K2t8hCxwwPwOYKp2U8EP0zC59RxTPlcfBiUnEwaVInuTxZNCQfj039UKysupEUipheeoWoXHNmSny4u4cHvvfFq5XE2_TYlcTIZw6wz4pfUY7y3G1t5RZr0QoVryKqsEtMrTa6fJI4tT0Jx1XRXprs_KTLFrf_UF7JzSm6d6qltPa4Tq6aKitq7VcJF5wds0RFVL9zhrwWpjlFXnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برای اولین بار: اسرائیل سلاح لیزری را با گنبد آهنین ادغام می‌کند، اقدامی که می‌تواند معادله دفاع هوایی را تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137689" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فایننشال تایمز: بیمه‌گران اعلام کرده‌اند که پوشش بیمه‌ای برای محموله‌های مرتبط با عربستان در دریای سرخ را متوقف خواهند کرد
🔴
این تصمیم پس از حملات انصارالله به دو نفت‌کش سعودی اتخاذ شده.
🔴
برخی شناورهای سعودی برای جابه‌جایی محموله‌ها، تغییر مسیر می‌دهند، بعضی هم سیستم جی‌پی‌اس خود را خاموش می‌کنند تا از باب‌المندب عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
به گزارش بلومبرگ، الکساندر نواک، معاون نخست‌وزیر روسیه اعلام کرد مسکو محدودیت صادرات بنزین را تا پایان سال ادامه خواهد داد؛ اقدامی که در پی تلاش دولت برای مقابله با کمبود سوخت داخلی انجام شده است. روسیه همچنین قصد دارد پس از بهبود شرایط بازار، ممنوعیت صادرات گازوئیل را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137687" target="_blank">📅 15:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کویت به‌طور رسمی توافقنامه همکاری دفاعی با پاکستان را تصویب کرد.
🔴
اقدامی که به گزارش رسانه‌های پاکستانی، گامی مهم در تقویت روابط نظامی و امنیتی بین دو کشور به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137686" target="_blank">📅 15:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شخبرگزاری آناتولی به نقل از منابع دولتی پاکستان، بدون ارائه جزئیات، از پاسخ ایران و آمریکا به پیشنهاد مشترک اسلام‌آباد و دوحه برای پایان دادن به درگیری‌ها و تشدید تلاش‌های میانجی‌گرانه میان دو طرف خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137685" target="_blank">📅 15:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
امیدیه و اهواز با ثبت دمای ۴۷.۷ و ۴۷.۶ درجه سانتی‌گراد، در فهرست ۱۰ شهر گرم جهان قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137684" target="_blank">📅 15:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1173bc5673.mp4?token=WCLNsgYpLltfx0mJRasrxFR3cBxcbDDuk8k8mIl7VPt5laxpkkkdi6o1v3D4f_8JzLRTBL1uC2L0T2pFPnqNlcWyOdeE1PicxnPgYbqcfI4LkyqQ5f4Yi2u0WLEpqmKj8K7JVgqT2gtMi3QwLpH6xrPRuG8DaJ_dwdpSBte5-_iRKkiWcgF5CzjeZq7bGnwRkhysll-5xLWHdqiFJvmXSC7IhAitevK3i27hQq9iv_Ild4Rx_DCQkBB1oUeruZx8NMS_VNnyRXemvpsFl0CFCR2dGSNWD0V2KPVwmsZQu4dffXNuCeJj2HZ_BztA544rp34F1Hez8yhUyvQLHdifLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1173bc5673.mp4?token=WCLNsgYpLltfx0mJRasrxFR3cBxcbDDuk8k8mIl7VPt5laxpkkkdi6o1v3D4f_8JzLRTBL1uC2L0T2pFPnqNlcWyOdeE1PicxnPgYbqcfI4LkyqQ5f4Yi2u0WLEpqmKj8K7JVgqT2gtMi3QwLpH6xrPRuG8DaJ_dwdpSBte5-_iRKkiWcgF5CzjeZq7bGnwRkhysll-5xLWHdqiFJvmXSC7IhAitevK3i27hQq9iv_Ild4Rx_DCQkBB1oUeruZx8NMS_VNnyRXemvpsFl0CFCR2dGSNWD0V2KPVwmsZQu4dffXNuCeJj2HZ_BztA544rp34F1Hez8yhUyvQLHdifLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌بست در تنگه هرمز همچنان ادامه دارد، زیرا این وضعیت ناشی از محاصره آمریکا و مقررات ایران است.
🔴
طبق گزارش خبرگزاری ایرنا، در ۲۴ ساعت گذشته، شش کشتی مجبور شده‌اند به دلیل دریافت هشدار از سوی سپاه پاسداران، در آب‌های این منطقه لنگر انداخته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137683" target="_blank">📅 15:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یاایر لاپید، رهبر اپوزیسیون اسرائیل: تل‌آویو باید تمام تلاش خود را برای جلوگیری از توافق پیشنهادی هسته‌ای غیرنظامی بین ایالات متحده و عربستان سعودی انجام دهد، حتی اگر این به معنای آن باشد که ریاض از پیوستن به توافق ابراهیم خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137682" target="_blank">📅 15:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حدود یک سال پس از قتل فاطمه سلطانی، دختر ۱۸ ساله‌ای که مقابل محل کارش در اسلامشهر با ضربات چاقوی پدرش به قتل رسید، دادگاه حکم بدوی این پرونده را صادر کرد.
🔴
بر اساس رأی دادگاه، پدر فاطمه به ۸ سال حبس تعزیری و پرداخت دیه محکوم شده است. برادر فاطمه سلطانی اعلام کرد این حکم روز ۳ مرداد به خانواده ابلاغ شده و آن‌ها نسبت به رأی صادرشده اعتراض خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137681" target="_blank">📅 15:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137679">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne3fYycpta3BUWkhvZxTZpvR1YIqPfOGz9bZBHVLPGkQVNG6r2j_8G2UH_YYUKiIZW-yp4aYR2_QDbTqBApykEljNMYlROSqpLhctgiHPmON-A6zs8OtaZSLbAQuulr3x2d7uXqwWOT4XqtV-cd3gTpxpR694liSSnKi3gaXTaSUIATTXFm1D4-0gk_KeH6RxpxW9vZZC_HGN36jYaDESqilTF2Q_JGnz-5q9hxsPqXodh_XMhHCHZxYhgRZHAWMYNRXJEHreo-VbhSrGy8eQhLODqR3usNQpzb9ofyqqCM850gWgoN4nojSecbZD9WJK4YHc0fEXelR_mMbsveHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1uW1-95uzJEKP2KQwKO5J2m4JOGaQcDiNzzdYp57bjUCMdL-I7_E_QxyuIh2UUKNIGyhoU6A-BgLBNXrv_oBTcSvvxKvIBxD9m05nWTLXq8LhX093dWd6lHWqyevuqeuoZ7Jnhi2ruq3b8eROnRiTH14fF-Qy6FWYjp9zBDN_LXbi72dnz94SkrzQ5hhzLGb5KdbHyfr7rp8MBD9cDpULjEFaZFTmion9rw722X3vPRs1ef4RAB0VBIENk3yAdRXrzR0_FiM7z5aRjq8cyNDFY9OrYkculdCu71dLXuokm012hGj1BgRKazu6UqF7rVUdxI8SBEcgu5YpCSrY6CkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برای دومین روز متوالی، آتش‌سوزی‌ها در مخازن پالایشگاه جازان در عربستان سعودی همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137679" target="_blank">📅 15:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137678">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
دفاع پرس: انفجار نفتکش در تنگه هرمز با مین دریایی
🔴
یک منبع آگاه اظهار داشت: ساعتی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری ایران خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137678" target="_blank">📅 15:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b85e271b.mp4?token=N1eRg4B-z5IzFUDtkNSp0f05JXYyTI6g7hjymPGW_0wGrTMbVMomd3CmL6Vxz36hO47MoJ7fFM8_iOUJTUFxv2tEueZMWZHm87CtdKwwp3TfrpH6iKD3qsdjsbjqiLRDWOTpfXEAo7W-H16_XNKr-5tgZp6ySyxTZalh-yecFVPKExvxPlaA1-kLzA7__BI1JfEdAuuUq5a8alMu1RqlJuyeJbaDMGb28E9Zb37dDRnhOyL3v_As1SEGorL_SdB9uibnBLtlyBFZ9I8ib6VuHQmcUmWKrI3kVncWrgPKMwYXzy_HRe8om6bQ5UOUs2BCg6aJqnkOUmHQovRJxZy9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b85e271b.mp4?token=N1eRg4B-z5IzFUDtkNSp0f05JXYyTI6g7hjymPGW_0wGrTMbVMomd3CmL6Vxz36hO47MoJ7fFM8_iOUJTUFxv2tEueZMWZHm87CtdKwwp3TfrpH6iKD3qsdjsbjqiLRDWOTpfXEAo7W-H16_XNKr-5tgZp6ySyxTZalh-yecFVPKExvxPlaA1-kLzA7__BI1JfEdAuuUq5a8alMu1RqlJuyeJbaDMGb28E9Zb37dDRnhOyL3v_As1SEGorL_SdB9uibnBLtlyBFZ9I8ib6VuHQmcUmWKrI3kVncWrgPKMwYXzy_HRe8om6bQ5UOUs2BCg6aJqnkOUmHQovRJxZy9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فضانوردان روسی و یک فضانورد آمریکایی با فضاپیمای سایوز از ایستگاه فضایی بین‌المللی به زمین بازگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137677" target="_blank">📅 15:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137676">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الجولانی: ما در تلاش هستیم تا به یک توافق امنیتی با اسرائیل، با مشارکت تعدادی از کشورها، برسیم.
🔴
ما از درگیری با اسرائیل اجتناب می‌کنیم و هیچ علاقه‌ای به آن نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137676" target="_blank">📅 15:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137675">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عضو شورای شهر: گردن‌کلفت‌ها جای پارک را به مردم می‌فروشند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137675" target="_blank">📅 15:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گزارش از شبکه العربیه عربستان سعودی: آمریکا و ایران به پیشنهاد پاکستان و قطر برای از سرگیری مذاکرات پاسخ دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137674" target="_blank">📅 15:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRfhunljnregiJVo-3nmeri3I7sbShMwgb8vk22Nf8VH_dfTzBXarbox16Sglp-FXdAOyhcHHpD_41D56FIZhHyha7QyZ6nZsRz8FSVMTj1AHzapfLPrr9qfTEOa1Gl3241FzOBZx4sallQm97SK_xZ82SFmxSnWuI6F85ZEfImTmYREhonTM1_ZtAcMKv4uPUqjVsC5u0CIvqxFXSS_U3nzKCuqmglZrHmh9rvX8ronuSX5EuRuLxMF173UoFwzpSfUxTckyYHPlEydG34KAmvDnjCieVUB8XdW2vUbzwTC_FNftD5fD8nmc8XpkuWTszrHW9XOAtGaIlZ_y7xD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: خسارات واردشده به زیرساخت‌های حمل‌ونقل باید از مراجع بین‌المللی پیگیری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137673" target="_blank">📅 15:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عراقچی: ما حاضریم روابط خود با کشور های همسایه را از نو بسازیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137672" target="_blank">📅 15:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرنگار حوادث: تو قلعه مرغی تهران جسد یه دختر جوون رو پیدا کردن که خانوادش چند وقت پیش اعلام کرده بودن گم شده و خبری ازش ندارن.
🔴
لیست تماساش رو درمیارن میبینن اخرین کسی که باهاش تماس گرفته دوست پسرش بوده و آخرین جایی هم که رفته خونه دوس پسرش بوده، پسره رو میگیرن و اعتراف میکنه که خودم کشتمش، بهش میگن چرا کشتیش؟
🔴
میگه چندین سال بود باهم بودیم اون روز که اومد پیشم خیلی بهم اصرار کرد که برم خواستگاری منم عصبی شدم با یه چیزی زدم تو سرش و کشتمش
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137671" target="_blank">📅 15:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b207bf62.mp4?token=lQyUqxb7zLjk-x_D4v7j3p8JRsterWieO2cyGRpfK03A9Djd1hrJcbe2qtwlUPrmPYMjSkH7ZI5s7UnC0fk-trYZnOKipk2T8UQfwyhmiowelBGB5igEZbJphEyzJM7kzOa5ZMctMigvKvBqiTgan99n8CCYfBS7gqpX1xV3ruEMTEzmpbQEHLbuodYZZdPulrPOd4zp8J726S2V0I_n5HJOPrskY_aMSKHPe2p-M3GoKRr7sMe2aPriLbWB-V1VyJQwe6xPT5yJNwk3izYF5Rww-zo8__4L995qb96c7GTWbcEuICtjngodktaCeKxHk7lCUwkII8nKsIQvFTKV_AMB-WFVqn2pSUwPiu2Bsh3FCUfi9VzGy7EmSCkxbAZ4xI3kUXQWPRqSa98HbWOtFXcxT54GK_WoTte-3Xir1355mnqfKNt-CGmFRXRnsaPrIwtCr8KiU1joeEzv8MNsAV0AxhxdySd0KOJtBVDhE8Zh8EMSGW8eZLdnn2oHjl0cNUzQGUPTTF_8sqPN3ZEBjXL_c-r8apL3mdcsX4igGIvku4aCR5awkS64h5_MH3MtnDYNfYvgf8dtMOsygRzR5E2OIFkJrYeLWkS0e6P600wUToO4gALIhmVVapVFFWiyI7Vwoj8hIEhqJYL_EfCLw1mRfE2aTU4L4A0MrOo2NzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b207bf62.mp4?token=lQyUqxb7zLjk-x_D4v7j3p8JRsterWieO2cyGRpfK03A9Djd1hrJcbe2qtwlUPrmPYMjSkH7ZI5s7UnC0fk-trYZnOKipk2T8UQfwyhmiowelBGB5igEZbJphEyzJM7kzOa5ZMctMigvKvBqiTgan99n8CCYfBS7gqpX1xV3ruEMTEzmpbQEHLbuodYZZdPulrPOd4zp8J726S2V0I_n5HJOPrskY_aMSKHPe2p-M3GoKRr7sMe2aPriLbWB-V1VyJQwe6xPT5yJNwk3izYF5Rww-zo8__4L995qb96c7GTWbcEuICtjngodktaCeKxHk7lCUwkII8nKsIQvFTKV_AMB-WFVqn2pSUwPiu2Bsh3FCUfi9VzGy7EmSCkxbAZ4xI3kUXQWPRqSa98HbWOtFXcxT54GK_WoTte-3Xir1355mnqfKNt-CGmFRXRnsaPrIwtCr8KiU1joeEzv8MNsAV0AxhxdySd0KOJtBVDhE8Zh8EMSGW8eZLdnn2oHjl0cNUzQGUPTTF_8sqPN3ZEBjXL_c-r8apL3mdcsX4igGIvku4aCR5awkS64h5_MH3MtnDYNfYvgf8dtMOsygRzR5E2OIFkJrYeLWkS0e6P600wUToO4gALIhmVVapVFFWiyI7Vwoj8hIEhqJYL_EfCLw1mRfE2aTU4L4A0MrOo2NzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جاویدنام
#طاها_نادری_سمیرمی
🔴
گاهی برای «آزادی»، باید از «خود» گذشت. طاها، ۱۸ ساله و ته‌تغاریِ خانواده و عاشقِ کوه و هنر، در میانه‌ی میدانِ حقیقت، ایستادگی را انتخاب کرد. در اعتراضات دیماه ۱۴۰۴ گلوله‌ای که شریانِ پایش را درید، نتوانست روحِ بزرگش را تسلیم کند.
🔴
او حتی در آخرین لحظات هم، نمادِ استقامت در برابرِ تاریکی بود. امروز، کوه‌های شهرضا بیش از همیشه دلتنگِ گام‌هایِ استوارِ او هستند.
راهش پُررهرو و نامش جاودان.
🕊
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137670" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=ULX5kaZ9TzdSeF7YQyfgSpOhp1nvLjo--zbK2r7KEm6tzFb8267Z8QHm5xmQSbj4IQZJP3oBglLgebgJ2nkxsfS7dFGkagGJgYALe5EGu1oCgaR0BygvS2TmK5_UwFdkSpj85Jjb6CAZwQ7LwOAxdqlkhn1WgBO654YEIX0_JJh1HwEA_HkJtc7alWA-lLtqW8kfZyayOIKK-q7VdYi_LYIwbY1dsAJZB5U8aQdYuQ89Yy5uvpSOWbP5OW8HPhzCTSX-PX1YguBYhmjIRBnS40jDhFfRXH0U352HKdiC06sXqsxU7A84k5V_ZwCL0ng8CJZXlOSgA3px69QlSKW6yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=ULX5kaZ9TzdSeF7YQyfgSpOhp1nvLjo--zbK2r7KEm6tzFb8267Z8QHm5xmQSbj4IQZJP3oBglLgebgJ2nkxsfS7dFGkagGJgYALe5EGu1oCgaR0BygvS2TmK5_UwFdkSpj85Jjb6CAZwQ7LwOAxdqlkhn1WgBO654YEIX0_JJh1HwEA_HkJtc7alWA-lLtqW8kfZyayOIKK-q7VdYi_LYIwbY1dsAJZB5U8aQdYuQ89Yy5uvpSOWbP5OW8HPhzCTSX-PX1YguBYhmjIRBnS40jDhFfRXH0U352HKdiC06sXqsxU7A84k5V_ZwCL0ng8CJZXlOSgA3px69QlSKW6yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔴
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137669" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سنتکام: محاصره دریایی اعمال شده توسط آمریکا بر ایران همچنان به طور کامل برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137668" target="_blank">📅 14:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین بی‌جواب نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137667" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی سعودی دیگر در دریای سرخ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137666" target="_blank">📅 14:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAeOaHH3QHp4F0IHrWgHtbY6xya0v-0ZOQNUYMxihQyrnG4y3m3hOmaZtTiSQoTI0UHdnPnB7bGy6D_dqjFIReW-utIq6IhHtRm6ZXTjKbNCFUDgWLcEShhd6lQLnuL2M7yDzXb4v6dqD6bBDIk2jb_vHdpcOGkbu_Nm6DkoNZ9z-0TogkL3csDT55kpHmi0A7RIIMNz9xFy_WtW2xhGtPc_2gRbpVNSCB36a09pnxBFqCGIqdK-u3vCq3WIMT_MO-XfNKOG85jpNbfJN22XUJi-vMISfqhe2XYVVC6Jhvyam4YhmBkAlkE67bSES7vSafEJqMWUoPDA1NU0Lax5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی سعودی دیگر در دریای سرخ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137665" target="_blank">📅 14:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jogSyFJo5X4xnwe3aJwxlIIzuDZYi3jS5FT6g2chNyfX486E04nCsOrr0A1WLbxfm3siaMI9EhAfPVnXK9qGHNxPfOvDADS5LHx3RjSktkqpcZeVUl2LrrXH4jWOCoDhfguH5qcCrXw3l23BLLJwgGxwU9SBiPS-TPii9y5ys2GKsAUHq90mCzXuYlxnBfCxt9HqIQuLIb0kBVAuhws1gocsRm8IcI3v4YkJEWKcRi4Lp8Ee1DwlttfJcPbuTthqm99HLtcK-slqwuM29ydXK7byo3ch0Gb-sda-ooZfSjDsvjwvryy7IqA2BSm_rAgsjgIk9qe8hI7dmdAUyJfN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به دلیل جنگ ایران و آمریکا، گرندپری فرمول یک بحرین به کشور مالزی منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137664" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الحدث به نقل از برخی منابع گزارش داد که امریکا و ایران پاسخ خود به پیشنهاد پاکستان و قطر برای ازسرگیری مذاکرات را تحویل دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137663" target="_blank">📅 14:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: هر شخص یا نهادی با شبکه فساد «بابک زنجانی» داد و ستد کند تحت تحریم‌های همه جانبه قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137662" target="_blank">📅 14:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان: حمله به پایانه بنادر و همچنین حمله به زیرساخت ها و راه های ریلی و جاده ای محکوم است و از طریق مراجع بین‌المللی این جنایات را پیگیری میکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137661" target="_blank">📅 14:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137660">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUilH-39e4oco2F8p1QxyBaMOhpy9oyevOt3K6Yx4loTx1Y6A9NfeZorDtxUyFR1Gd6893w4BgBUKAx0234vwAEHrvjw2Xx0pOjNebEfrSyC04PTQpQslUGqpkhUcYB7GuU4zaV5a21_-ubZwiU6h4kKtQCNPwnbOw26W3zlXiVlrffoI9DUpEnGgINWy63MAtr1sSOXOavexhKSQpMMlfdPvtisFNWy6j08t5BNqxPEK1xT063O9SHcWVoXrdAoH0I0L25lDuBO7fGR93fcki7e4lwv_jq0FkesWCJZPHKGFul_56uqtfz-B7K9fj3CKC_xCiyMoCT2rZFIX-i-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گزارش شبکه NBC News:کمبود موشک‌های رهگیر به حدی شدید شده که فرماندهان محلی آمریکا ناچارند تصمیم بگیرند کدام پرتابه‌های ایرانی را رهگیری کنند و اجازه دهند کدام‌یک بدون رهگیری عبور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137660" target="_blank">📅 13:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137659">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwAIr60z2AMew5vu1KH8r5qWphB52AQ7uMwIKCoMmZg68X28VmJbIks-UfZrpTBb9_qRnT6XA-ZPo4u91Zc-Rn-QaRZcoqMVtojQMVvLnfbf8iK9ydeV-2JYKD0kid4ZEGZz9eicks6Aqdk2c4CwmLf_2UXSiwmMT1xpVDVyXwCSfZkNod87ZEKdg4s6nZKb9RpjOemuvXzvdX9eMZEyuKEhN4jqy1gdMpq4gOEZQ3Oqezo8zsTepYacdBytuyOamhNbfYecrz6BwCkJCzyvSTKLQ-iEcF-A7Rq70gfqN4iY5fQ-0-7mg54SIyA9Oe5WdlMB6fSJWrWu-qeB_OFN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد الشرع: قصد دخالت نظامی در لبنان را نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137659" target="_blank">📅 13:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6bd19d716.mp4?token=GI--pmVHOjvHn5y5jbhI5JeM9H6a6EW3XWksCtUZHouStlNwgNKzz2uUfdFOWNc_WJ7hjSVWgX9RuIlfrJN0M1rTreqXVnUY8y147mzTdPx5JjUK7IOdoXIyUWKqnpQltk1vTpzwSFGZFVl_Km_F5oOg_xqBmhGJtDKw5xLzeEJribdCGebWTR_sQHmU7N9p_qONi19EW3cL30C2FpNEUMf6oZcsR6Li4exDDkdOkHbHmJe-YCbmbVx0vXNwy-ndeiTQndxYilhdD0HuxqwM1t_v2MIrVkFwQ7ahtL95mBr1Yrcv3jsjEg8ig36_SpkfqvCWK5qsqdOYNInkjRiGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6bd19d716.mp4?token=GI--pmVHOjvHn5y5jbhI5JeM9H6a6EW3XWksCtUZHouStlNwgNKzz2uUfdFOWNc_WJ7hjSVWgX9RuIlfrJN0M1rTreqXVnUY8y147mzTdPx5JjUK7IOdoXIyUWKqnpQltk1vTpzwSFGZFVl_Km_F5oOg_xqBmhGJtDKw5xLzeEJribdCGebWTR_sQHmU7N9p_qONi19EW3cL30C2FpNEUMf6oZcsR6Li4exDDkdOkHbHmJe-YCbmbVx0vXNwy-ndeiTQndxYilhdD0HuxqwM1t_v2MIrVkFwQ7ahtL95mBr1Yrcv3jsjEg8ig36_SpkfqvCWK5qsqdOYNInkjRiGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : فردا برای دیدار با ترامپ به واشنگتن می‌رم و درباره ایران و سایر مسائل مهم گفت‌وگو می‌کنیم
🔴
در کرانه باختری هم عملیات ارتش برای بازداشت افراد مسلح و جمع‌آوری سلاح ادامه داره
🔴
همچنین از اقدام آمریکا علیه دیوان کیفری بین‌المللی حمایت میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137658" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا به بی بی سی:
ما آماده پاسخگویی به هرگونه حمله‌ای هستیم که ایران علیه بریتانیا یا متحدان ما انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137657" target="_blank">📅 13:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQVoVi77g0eAoUaB0_h4Poqu14LWGcU10QXYYLK61xep-Mpd5YFNL1byHXc8xeG4jvKLbP6GUHBp17ZcdCpyQH0JS7v-JjhCE8gk6IumPUd2riJgXE-AIQCqD1DR9haIeJPbs32xU_U6WiWVruC7vieUYJf1tWfZQAmfJ0hx_yxukLHud3E4DCtoQxA_dffplrhFXpLmgZ3SM45Yf36_Rt0rcbZjlnApp4ClhhZsdsihiIOeO5bqFSYBqo_huFFl98aJKxE3wttJGQibP6fF4_gEa1MfptwB2X0Npe1D3ex-izLGe5sT6Sg6a_5QDO6rGSjLk-6hZUQLKOkB2mwQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نرخ مصوب برای ۳ محصول لبنی تعیین شد
🔴
کارگروه امنیت غذایی و تنظیم بازار کالاهای کشاورزی، قیمت مصوب سه محصول لبنی پرمصرف را تعیین کرد.
🔴
بر این اساس، قیمت مصوب سه محصول لبنی به شرح زیر تعیین شده است:
🔴
شیر بطری یک لیتری با ۲.۵ درصد چربی: ۱۲۰ هزار تومان
🔴
شیر نایلونی ۹۰۰ گرمی با ۲.۵ درصد چربی: ۹۱ هزار تومان
🔴
ماست دبه‌ای ۲ کیلوگرمی با ۲.۵ درصد چربی: ۲۶۵ هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137656" target="_blank">📅 13:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سرلشکر صفوی : نیروهای مسلح ایران معادلات دشمن رو به هم ریختند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137655" target="_blank">📅 13:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137654">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عراقچی: ما حاضریم روابط خود با کشور های همسایه را از نو بسازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137654" target="_blank">📅 13:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137653">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da6ea7622e.mp4?token=Q34Dx2kGCEitCpl43dyNqF3b-ylu0nrzSRjsMsE7e8bLdFBezsCpuLos3kIXBNAPL95UhVoI8arggTv5H4DomzMlr-I7IGYq1hBwIwwhVlCTTpLfaRUOi87ZECid0_vvASJCgwMx1FwG9eZZQZy84OJczJBC1fF_Co3eatq4XROG-Fo4S37nIk7OGEShckM6jLb5Nh3gLgcQkho4VhCQ8WxhpLdSMTnmY2CCM01HHHoghy2HETqZsueIIshn28Se5sFSMlAc9Y9bkH6YMYJDC7eaqq6qTyxD3guviCc2PSRAzAgPpovOQ-yuGJtzj4ZVYlBBVEjnXCNOWhC7_WKd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da6ea7622e.mp4?token=Q34Dx2kGCEitCpl43dyNqF3b-ylu0nrzSRjsMsE7e8bLdFBezsCpuLos3kIXBNAPL95UhVoI8arggTv5H4DomzMlr-I7IGYq1hBwIwwhVlCTTpLfaRUOi87ZECid0_vvASJCgwMx1FwG9eZZQZy84OJczJBC1fF_Co3eatq4XROG-Fo4S37nIk7OGEShckM6jLb5Nh3gLgcQkho4VhCQ8WxhpLdSMTnmY2CCM01HHHoghy2HETqZsueIIshn28Se5sFSMlAc9Y9bkH6YMYJDC7eaqq6qTyxD3guviCc2PSRAzAgPpovOQ-yuGJtzj4ZVYlBBVEjnXCNOWhC7_WKd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جامعه عاقل میلیاردها دلار زیرساخت و نفت و برقش رو فدای لجاجت نمی‌کنه.
🔴
اما تلخ‌تر از شعارها، لم‌دادن و بی‌تفاوتیِ اون طرفدار حرام زاده حکومته، اون‌طور بی‌خیال لم داده رو مبل چون نه نگران سفره مردمه، نه تاوان ویرانی زیرساخت‌های کشور رو از جیب خودش میده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137653" target="_blank">📅 13:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137652">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLyNBJejp0YiMvO-H2Zu7qZRBnmL1c0csa6p7hEoRBPkfLJ5VrcdfNATLmRDZOhtMwTW1Nzbivt_6l0ZAgCG-eMGaRR-BUplebfygLiW8PKlDqoRj1woP5RT7qsJ_ROQJiZr1jRdx85m_D6EM-g4ZEel0jAfyC41DLu_aejmasq6yWKidrB1FNqnhr6nNWWU6Q9mYU-0glHxrHu9jIQJV7vz4fLjnjLrp8rwcmvGMeVI4k-t5gSb-LAU71agCV-P5cUxNMhG5TTFJ4WLOcozIzDXgjXxLC7wlWqZl2_lM4zt7gsRJHINeuse94ydCV0nbhiaa9BOB1r1w5Bd7sbmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته دو مقام ارشد آمریکایی به نقل از ان‌بی‌سی نیوز، فرماندهان نظامی آمریکا به برخی موشک‌ها و پهپادهای انفجاری ایرانی اجازه عبور از پدافند هوایی برای حفظ منابع محدود رهگیرها را می‌دهند.
🔴
با توجه به پرتاب نزدیک به 9000 پرتابه از زمان آغاز جنگ توسط ایران، نیروهای ایالات متحده اولویت را برای رهگیری تهدیدهایی که مستقیماً علیه پرسنل هدف قرار می گیرند، دارند و همزمان حملات به زیرساخت ها مانند باند فرودگاه، رادارها و تأسیسات سوخت را می پذیرند.
🔴
هدف از این رویکرد حفظ ذخایر پاتریوت، THAAD و رهگیرهای سری SM است که پرهزینه هستند و جایگزینی آنها ممکن است سالها طول بکشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137652" target="_blank">📅 13:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137651">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی:
ایران روزانه با نزدیک به 20 میلیون لیتر کسری بنزین روبه‌رو است.
🔴
واردات بنزین نیز در شرایط کنونی به‌دلیل محدودیت‌های منطقه‌ای و بین‌المللی تقریبا غیرممکن شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137651" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137650">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwspjOYe7WUJf08rBJNBU9stD4d86NE7TKz0DviCCRb56cRz8mi7b4HhzvCo8C7p32_IHGXYbMLW1_lF4aj_LpTUDzn8Ox3lvF2KRB2azMXoWSetzobUw2FbK_Tk9nz-HMNCIJzbbjT3nLqRk1veHsbT7VVUrudpkIjK5KAKb6MEX6wwsFdHJ2pFD6ET4VCk6mlLRYbXyb1-RO9UfZU7kgGO2Q01zjo1OpVi9UUhg0s97KFvOYYgk3rCqrR86dC0ddRGSTTPRhkkZUxbi5lSplXFzArteA3-d9WpKogQQFykgP06WNM3hvqAVdPULIkpIg8n07Vk7PTuGEt0eNYn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۱۰۷ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۰۰۲ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137650" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqStHbMnxuHiJEBjacLhrw83WcKoF6piK9RzIr6ttrA7cPvcvWq5F1sk3gN5yNjsc6Yh2tLpv2_oqp6_I-wdAJwSRBGwQhDd9NdZ5xGl4cocRXaP1Exui_GNhEDiuz2uV9kWnMpadkOV4uf9H5UJPcpOj3IyqqA17vPanh8f1IDIA2p6AGaV5foaIBEVUmtA8tqTADbvQSS1TmRLXbzUkIsFzY3gtOyju6ts-gIfS58q9FsoDzoY79yaaB1Y1TdNDMTQviObGJPw3pkx1xZYWGUFbWaDjtNVCaToTnpYjq4X3SfDBma0tM6er-KR_CWNxUHMv2AICme_NbHwVXsS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریایی بریتانیایی: ما گزارشی درباره یک حادثه در جنوب دریای سرخ دریافت کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137649" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137648">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ، انرژی هسته‌ای را ترویج می‌کند، از جمله توافق با عربستان سعودی. خانواده و حامیانش می‌توانند از این موضوع سود ببرند.این توافق به ثروتمند شدن ترامپ، خانواده‌اش، مشاورانش و سایر افراد نزدیک به او کمک خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137648" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137647">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نیروهای اسرائیلی اطلاعیه‌های هشداردهنده‌ای را برای ساکنان منطقه الیرموک در غرب درعا منتشر کردند و از آن‌ها خواستند که از هرگونه مانع‌تراشی در مسیر پیشروی نیروها خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137647" target="_blank">📅 12:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137646">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy0hNKDmpp9N-Qko91Kpm8v0X0d36jcuKM0X2MUc5yAnBpAtKNeeNYUOCXx_UIfi3ddt77fWDGLaiJ874G3zgISPzZFqN1JcoY9UblW8H6rnR4SD9vrY5mctgGCBG2SwWgut8x0lu3G7SvIyS3M7nk15nZNd3ZkrdO5B-vEK2jUzwmfY8LK_3DmCDPAA3OUahD2gEY90zFBe19-nJVuLv-K5ce4xB6kCFvsCZ_FRyFoGWdJhBgWCXHHn3-1yKdNkinZw5Jpid8QK_rgUu6DyK2Z5r2_iizQuX45Po1kfcYTdzG5QoiQa2Tye5A28R4EGeYBJCvxcDUVYbep8qaHo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازهای ترابری نظامی آمریکا به خاورمیانه همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137646" target="_blank">📅 12:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137645">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137645" target="_blank">📅 12:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137644">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
غرق شدن یک کشتی ویتنامی در دریای جنوبی چین/ ۴۵ نفر تاکنون نجات یافته‌اند
🔴
یک کشتی ویتنامی با ۶۲ سرنشین در آب های دریای جنوبی چین غرق شد و تاکنون ۴۵ نفر از حادثه دیدگان نجات یافته اند.
🔴
تارنمای خبری «گلوبال تایمز» با انتشار این خبر افزود: یک کشتی ویتنامی به نام« KHOI NGUYEN ۱۸ » پس از بروز مشکل در آب‌های نزدیک صخره «یونگشو» (Yongshu ) در جزایر نانشا واقع در دریای جنوبی چین غرق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137644" target="_blank">📅 12:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137643">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سخنگوی ارتش: با توقف حملات آمریکا، عملیات تلفافی‌جویانه را متوقف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137643" target="_blank">📅 12:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137642">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک آتش‌سوزی گسترده جنگل‌ها بخش‌هایی از منطقه مادرید در اسپانیا را فرا گرفته است. آتش‌نشانان و نیروهای امدادی برای مهار حریق در محل حضور دارند و عملیات اطفای آتش همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137642" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137641">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مارک اسپر، وزیر دفاع سابق آمریکا:
بر خلاف اخبار فعلی، ترامپ در آستانه تشدید حملات علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137641" target="_blank">📅 12:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137640">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شایعه مجازی شدن سال تحصیلی کذب است؛ آغاز حضوری سال تحصیلی جدید
‏
🔴
وزیر آموزش و پرورش:مجازی شدن سال تحصیلی آینده کذب است و متاسفم که بعضی‌ها شایعاتی پخش کردند که آموزش و پرورش سال آینده به صورت مجازی خواهد بود.
‏
🔴
از همین الان تمام تمرکز ما بر اجرای آزمون‌های نهایی و پایان ارزشیابی تحصیلی پایه‌های یازدهم و دوازدهم است.
‏
🔴
تمام اهتمام دولت جمهوری اسلامی ایران و مسئولین دولت و نظام تعلیم و تربیت این است که آموزش و پرورش به صورت حضوری از سال تحصیلی جدید آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137640" target="_blank">📅 12:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137639">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279c2568c4.mp4?token=YbAa_Y9XS5k8bFGHSmcuNPuD0cR1CzxP_yaYQhmDPjMkNepSq_m-n-VCnuGXZPIAUCOjdXLhb8t7f_VowxJq-Zbjoyg63tEtWLnth1ql8CRo0mMQeUMLZICwZ4YldnriF3iiHdIQIQDPeNukZVuxHXTv3kNxhJV6b6vFRzRZkLeiHTSKngsXYf2mublyFj86MRRSy1TbDKRUaG3Z3zcBXuGTZCyBkG8KaQt7dyM7bBrGFkQIYWDkPo0rmE7S_cDJlZF2FzLw1TbItILoTMpnCAeQco7AfEC_LNYSpPffA7qIAUQAgoUeZ6sv0cu5GV5GhisQCdXk9L6sjyLj26LHWGKyJuICJSpqSRvcEoiC1NV2FGAI_uzqccNCS1zEUQfTCsQSQDm0gJvRIgpY4Z06gC-pCnmD_4I5yWieBFY12-9YLARDdcv6zyZh6V8emzlYGE1usjTCQV3B3xXB7M57nHoi1rSV1TnrIeoXje8EoS1kdbwAMYXu9l1U9LhMKcXxaOsEWis_vJsWSnj7Z0lJUGx6XPFvY28nrgl3eK71FsJev6D-oDS3WZZ0rVwR-Zh_ZzPludz6FoEBhFCdxleVfxAqkwqV3oigmTWOZ46aVZyju8w2A0_QFWAz7wONIa3HgzeV4_wJvgnXp3TA3HAGuYvXCaccy7THfSU45h2479M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279c2568c4.mp4?token=YbAa_Y9XS5k8bFGHSmcuNPuD0cR1CzxP_yaYQhmDPjMkNepSq_m-n-VCnuGXZPIAUCOjdXLhb8t7f_VowxJq-Zbjoyg63tEtWLnth1ql8CRo0mMQeUMLZICwZ4YldnriF3iiHdIQIQDPeNukZVuxHXTv3kNxhJV6b6vFRzRZkLeiHTSKngsXYf2mublyFj86MRRSy1TbDKRUaG3Z3zcBXuGTZCyBkG8KaQt7dyM7bBrGFkQIYWDkPo0rmE7S_cDJlZF2FzLw1TbItILoTMpnCAeQco7AfEC_LNYSpPffA7qIAUQAgoUeZ6sv0cu5GV5GhisQCdXk9L6sjyLj26LHWGKyJuICJSpqSRvcEoiC1NV2FGAI_uzqccNCS1zEUQfTCsQSQDm0gJvRIgpY4Z06gC-pCnmD_4I5yWieBFY12-9YLARDdcv6zyZh6V8emzlYGE1usjTCQV3B3xXB7M57nHoi1rSV1TnrIeoXje8EoS1kdbwAMYXu9l1U9LhMKcXxaOsEWis_vJsWSnj7Z0lJUGx6XPFvY28nrgl3eK71FsJev6D-oDS3WZZ0rVwR-Zh_ZzPludz6FoEBhFCdxleVfxAqkwqV3oigmTWOZ46aVZyju8w2A0_QFWAz7wONIa3HgzeV4_wJvgnXp3TA3HAGuYvXCaccy7THfSU45h2479M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع طوفان شدید در منطقه روستوف روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137639" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137638">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1dc51b5c.mp4?token=fz0tPI2AuviSFSm1eWaT8QVKvo21uJXjUx8qKf97oNdzaQXCKFUSZHoTokGP0pa-t5Wu3MmJh-h8WIsw03x90Nz4ROABfLVdHunL9Xxm_O6k-LN6mVzMDdWB9FzxC0TsqmeCFtvighEpcED_93-HxFBUIRdx894g8hSx07rWG097K8LC8ex40sgVPfcRQsnDhkOVkcO_-o_DiUYcT3mIfAmdWJsyPcALGcfaeF0X-8vcxghjZ_3hD1nbVHBoRf3JC3HKsXh16Vw38lkViax6rmcZVZeasmcl5fOg3mkGFC0GSAdFMxs-kSfp-651GNx_h5L-jmiOyF8LOm4u5FiXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1dc51b5c.mp4?token=fz0tPI2AuviSFSm1eWaT8QVKvo21uJXjUx8qKf97oNdzaQXCKFUSZHoTokGP0pa-t5Wu3MmJh-h8WIsw03x90Nz4ROABfLVdHunL9Xxm_O6k-LN6mVzMDdWB9FzxC0TsqmeCFtvighEpcED_93-HxFBUIRdx894g8hSx07rWG097K8LC8ex40sgVPfcRQsnDhkOVkcO_-o_DiUYcT3mIfAmdWJsyPcALGcfaeF0X-8vcxghjZ_3hD1nbVHBoRf3JC3HKsXh16Vw38lkViax6rmcZVZeasmcl5fOg3mkGFC0GSAdFMxs-kSfp-651GNx_h5L-jmiOyF8LOm4u5FiXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
مجری فاکس‌نیوز: اگر آمریکا نتواند چند ماه قیمت بنزین ۴ دلاری را تحمل کند، دیگر نمی‌توان آن را یک ابرقدرت دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137638" target="_blank">📅 12:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX5XWK7DTQj2GOxjldJM6r7aPZQRGd3yfDpRkxWKQeTEiusXJIqq18MD_e1yUsSvTQDST-A8dCKNKU8lz38RQNoxAkBOJl9bUc6i6R33Fw_3uC8cJ0RByqNRS3avDVHBCEj4l6FOxoxQ2AxeUmuKmgJq7iKkD1Vpka43zY-N3PheTosROK_P5pF_zTpSGhpsDvSSZogO4HENp93c3cnGNAc1R9n-xpjAjtdkkYm5QkiElgeZh-updTMtrHMUly70b01G53UJmvrDQue4T4WYNkzj-S-XlL9giu2JhsW_zQ8ntHSBsKVLhBaeLjH2BDHdPVPCpHrQ2U_OOcr8nFiyYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از زنده یاد اکبرعبدی و گوگوش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137637" target="_blank">📅 12:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سلیمی، عضو هیئت رئیسه مجلس:
برای برگزاری جلسه رأی اعتماد وزرای پیشنهادی دفاع و اطلاعات، آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137636" target="_blank">📅 12:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137635">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روسیه با شدتت زیاد اودِسا چرنومورسکی اوکراین رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137635" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137634">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
علی قلهکی از احتمال استفاده آمریکا از «بمب اتمی تاکتیکی» برای کوه کلنگ خبر داد
‏
🔴
بازگشت تیم عمانی به مذاکره و آمدن به ایران برای مُجاب‌سازیِ تهران برای همراهی با شروط و امتیازات جدید واشنگتن و همچنین مشخص شدن سهم مسقط از تنگه کلیدی هرمز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137634" target="_blank">📅 11:57 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
