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
<img src="https://cdn4.telesco.pe/file/oUgmBj3vJh4rP-RssZh4ouOyeV4EjuIKhHmK5-MCDX-lD46_FrrJ50-aUiT_w6yS4b7e1g-Yy13VtNTNZ6fFf3WqxQ06yKR4CJlATgD3fTXQ-cNikAkES35Sqohhk_Inh5irqSvhg1N65tYgS9e6Ht1CJ6GcmCBJ2j_re4lHPN6XyX67YVNTMgWIBbYN3giZCNht0mrLBPMKs-Te33l892eDE7Zk_jmfb02Id5Y65uMrrRPKkRJ0KwnGz4YVxVnwgY9GhkQPyuejMIoIAkQnv5VJTlDl6jy4QjmIvEV6wWT92ubArA-lfLP2KE90WdRS-r1GYRDEcVdH6BWTC7w-Ag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 253K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=fnI0hO72arWdQ_KIQqg3tPLLb9Y7rJRMEmffhukMNRtxCMvLxRFsWZSM58ja9EwXxIytlY2kpIJTj8ct0Fp1A9lHig7Eev_7BFBOn5-us8ca5tHB4zjg4yzZWPbuS93aGYM9nqzcGKWnvEYZgB4uyQwwWqZ0p3KVAXfyeBvlzmpPhzp0EefSHRA2CZjQXvCAYtZfVawYm5AzrVcaKFsi3GegarH2Qr-L--Ju03Atvp5yYvUwXzJjG8vMDMIMu2aJ8aqKWmMWW1CxSaaAcfOLApK2UyAtd1p5pWMwmn6WfbMio8QnW15ao3SSnQfSVDiqBz3Hll8QtaKMqhfqVLCHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=fnI0hO72arWdQ_KIQqg3tPLLb9Y7rJRMEmffhukMNRtxCMvLxRFsWZSM58ja9EwXxIytlY2kpIJTj8ct0Fp1A9lHig7Eev_7BFBOn5-us8ca5tHB4zjg4yzZWPbuS93aGYM9nqzcGKWnvEYZgB4uyQwwWqZ0p3KVAXfyeBvlzmpPhzp0EefSHRA2CZjQXvCAYtZfVawYm5AzrVcaKFsi3GegarH2Qr-L--Ju03Atvp5yYvUwXzJjG8vMDMIMu2aJ8aqKWmMWW1CxSaaAcfOLApK2UyAtd1p5pWMwmn6WfbMio8QnW15ao3SSnQfSVDiqBz3Hll8QtaKMqhfqVLCHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند مشت زد تو صورت بازیکن ازبکستان تا نشون بده مشکل اعصاب روان داره و نباید بره سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/funhiphop/84002" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/84001" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/funhiphop/84000" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urkHPnmpNmEN6zWpMlBWF6EsC1bdJ8egd6N67lOHIFsqsYc2G-8thvXvcGiw5QKVAYgn1hZ4k7vy-MWlZq1Io-WgtfVRRacgTeLoAgOUb4TGWeCSZ8k-tH8CG9Qy8TcE4bu2-2b1JzUkbfgMg9SGogLCTavCqyIHuiXFkc9dJ5P9GWlqJjqQZihr858Zg8V3JpKWXoykoP_xaLuPdSdHfwfT4qgMAKmoV4wAg2F64nc6EkuQmBC5AoIHJQBOIbt04-ptRK2azDmfoHJXDWYzHeXaOQ7PDeLg5BslwbCxrPxUvp5WIzpqQwZH7y3PClkEigg4lFhu0jeAkQJfKZtQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسی به هیچ وجه
ترامپ:
دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست؛ بهتر از همیشه. بانوی اول شی هم، مثل همیشه، زیباست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/83999" target="_blank">📅 16:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاید باورتون نشه ولی کوروش تو چنلش هنوز با پوتک درگیره</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/83998" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9H0iB9JShfI4WwbnYY7QEpc6pG1hU_W9_kodM5OI-kWKmFaiEHQXlUXhM5BzPwVJNSo0ambmcA2KJTKlgoVF-jMRdMFgxRJADr3UiN4LuKdj3iGpFKOy_erctMPiaq8CO8o3L5-zO56hsX26UDYr-cRo4mSo6emSkV0__CG34gO2MlqmMIMHcURJxYuWAr76FTVb01uX_chDqmQKcsgILppjCCy1WmavlwZyuDFSMyj-GJdvCDuEwOb5VlXyxVDoWKedLhbcIfa7UbcW4CaTRFKdscAnwSN1ORzq1_lpw0prQncnLgE0MYvStbyOwo6gc7D5iDPRDyztSTWMHGrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اینا تو وان حموم خونشون ناخدا بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83997" target="_blank">📅 15:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA83rTCSfETzKN3yA6puB9h21sHTIPlSo_FlP6AqK-VfG9KGxAUvaJP3yXzqUL7zLTd6uWNulzomMex8yU0YTUfWo7DPPOOrTZCPt3OikGcbd-LVGyygCVhx680yEc4PC3cDLUlrZA5tjgQb6KKPe_RP1QA1iVkcAHK__C56LMdkJyjCdJSOaGcXq-pIHpL4sh6_dPRgn9vWv8voKbzss_zAXmAYgK9qQj05ZuidFzwBdunvziI9RP896MLRVs8xoJ2AdH_FiDIp_ez2guE_E14igCdIhNHYXBTrawBbNmgj1DiQ1dBpTEom6-DtG_Sr_UEoHrNcyA5pwnNMSd--Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد به سلامتی به کدوم سمت انسانیت عازم هستید؟
حموم؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83996" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پس پزشکیان کی قراره بیاد بگه گور بابای دنیا ما رفتیم بمب اتم بسازیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83995" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=heVYicZBEbg9dWOLNvHGycyAeEAqIQ-xf6i-bXmRD0OQFXjTdG5O73sUGh9hdPNOdfX1dwrBlSEetzzne_H0R0QkuLwDCl9kGXfEmBwm5sIFci_pTYAg-QhjEtlg1Iys8IV9vEDtPrk16n3C5x1HkrJPi7LldW_kbrK9-BV0OxubTo6HHiYH0WccAmh9Se2B3ka5-WWLzS35XhU6cu4TLa5M0t5mhnFqeaBYYsX2whO95QtLB1Gf7P_dKkwDletHvk442EGFJubikxcpE7jkUrJVmrfxHSwgeXtHu7-_qP7itdIJRUFvvCxQUxkwudgupMJnmHVOrGpU00Lq6zWkVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=heVYicZBEbg9dWOLNvHGycyAeEAqIQ-xf6i-bXmRD0OQFXjTdG5O73sUGh9hdPNOdfX1dwrBlSEetzzne_H0R0QkuLwDCl9kGXfEmBwm5sIFci_pTYAg-QhjEtlg1Iys8IV9vEDtPrk16n3C5x1HkrJPi7LldW_kbrK9-BV0OxubTo6HHiYH0WccAmh9Se2B3ka5-WWLzS35XhU6cu4TLa5M0t5mhnFqeaBYYsX2whO95QtLB1Gf7P_dKkwDletHvk442EGFJubikxcpE7jkUrJVmrfxHSwgeXtHu7-_qP7itdIJRUFvvCxQUxkwudgupMJnmHVOrGpU00Lq6zWkVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور هائیتی یه ایرانی درون داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83994" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسکات بسنت: نمیدانم نمایندگان ایران در نیویورک چگونه قرار است به ایران بازگردند.
پ‌ن: منظورش اینه هواپیما های ایران تحریم شدن و اجازه خروج از ایران ندارن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83993" target="_blank">📅 13:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">باورم نمیشه برا یه سریال نگاه کردن مجبورم ۱۰ تا چنل صیغه یابی جوین بشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83992" target="_blank">📅 13:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=FsFldtDLvo1U7segK_Rg2XymQPHpJAmsRqXROBjzQqDQOyAt06svS75i88qcsf6v02Dx-SVsamRiOo1VtB_sHnFB4fKTm6aquz7EHZwks8G2ALrkK1TT-dcHeHqaP09E1NB-t-11XeaGyq6a-Eb-uQFp4QTJBBObPMhjpGN9UHEUec_TaebzaWQmtznu_CTbHveHc6d2ojH3QhBGdDvFanlREGEKKIZaifseLCQPUZT5pkk6fHyuMAm2KqEPIeYhwTPPvPVz0KjBc-BHV7mx-h6BaDRQmx4ZXCjkqo08AmmXWW0EWDRYaKuRLfhdcq4W2nLDbQLBtCtTAdjHnvNNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=FsFldtDLvo1U7segK_Rg2XymQPHpJAmsRqXROBjzQqDQOyAt06svS75i88qcsf6v02Dx-SVsamRiOo1VtB_sHnFB4fKTm6aquz7EHZwks8G2ALrkK1TT-dcHeHqaP09E1NB-t-11XeaGyq6a-Eb-uQFp4QTJBBObPMhjpGN9UHEUec_TaebzaWQmtznu_CTbHveHc6d2ojH3QhBGdDvFanlREGEKKIZaifseLCQPUZT5pkk6fHyuMAm2KqEPIeYhwTPPvPVz0KjBc-BHV7mx-h6BaDRQmx4ZXCjkqo08AmmXWW0EWDRYaKuRLfhdcq4W2nLDbQLBtCtTAdjHnvNNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83990" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نارنگی برا پولداراس ما فقط سرما میخوریم
🤙
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83989" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804d882599.mp4?token=qYB0ms0usfNtUzWVXN-Pk9nkGuNiWtOuTfQH1CPCka1n5FYbi85YGyWCwZWI4cYRKj2sWt1zYeWY2hkGzgIy7lTDo6VDSm1wzj5XgnOvX2GchoGdyTpsgXz20ZMhGKGvrmxNaI5iVE-or4iYgB6by0vp9js1aB9etwepGO7LxYTJyoujMf8Qp_Vbvq7HSroCvh5ytJJxfSy2-BVlCKeWn46d1wC8micj0gSxgGQdqDrgej4N-tcDQfQWXCEdW6908itScWL5u3WzqdlHLrLMLUKSZ1qvTRzi8QvIf32XONHGJyEYXzBk0h72Ac5615PRYiCUbHODvJg1_5fo_sUkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804d882599.mp4?token=qYB0ms0usfNtUzWVXN-Pk9nkGuNiWtOuTfQH1CPCka1n5FYbi85YGyWCwZWI4cYRKj2sWt1zYeWY2hkGzgIy7lTDo6VDSm1wzj5XgnOvX2GchoGdyTpsgXz20ZMhGKGvrmxNaI5iVE-or4iYgB6by0vp9js1aB9etwepGO7LxYTJyoujMf8Qp_Vbvq7HSroCvh5ytJJxfSy2-BVlCKeWn46d1wC8micj0gSxgGQdqDrgej4N-tcDQfQWXCEdW6908itScWL5u3WzqdlHLrLMLUKSZ1qvTRzi8QvIf32XONHGJyEYXzBk0h72Ac5615PRYiCUbHODvJg1_5fo_sUkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شی جی پینگ همیشه یه نگاییدم خاصی تو نگاهشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83988" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrLx1Q0mydHwYrRpCjQNavxEjXal9TbLu2U6czPqHmvyc0Az5Zt1jmLL7ysbs7zlFloI2zEqEOBAGyKhAWN7n8CVG5ytoO2Il9KsxFRt82B4DwZ4zinZHQpWXxwTuwe76ZOkmA4sUeWxP5lbOlxv-84Q9GgEx5et_gPjQWDeX98EWUyasNdvL_Yb54zBQ8FjwU0V-14nbP2pRDF0Xlr8jX3Yv4TKRDhBPQcA-klufmUM8mrQ1fE30SRhJYfF2JxojO8aHXYcQmpBuq9AQ2lCxfCzKjbOzgDKWqrjCyNxeWxADCQseeKN24xw3Cf_CNnH1YgKmHXze05JY1Ot4eBXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
نروژ - دانمارک
⏰
ساعت ۲۲:۰۰
🌎
📲
پرتغال - ولز
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
R2
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83987" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2YVqTxm4VgUjzDcEWmm2ceOZePjyvoBveAL8yxleGFkozK7_HeRM5NMcNx4qFqyDja0vk7OZKWXs2v4ySMZIi33bf46XdWkNTDbi5ng1rnBgvAZXuwG1EvHPIlFq3XxGdQCmL5Qg8myIKQh9gS0WlBQIAxAdWC4RPesXjVRsSzQAwnBMR5Cvl8gVdJ_Kq4hls2RzoTja274uYm8hixGfFEXGTuvqilujCm3AW2NBnynKMigTNHk3q4L3EiJG6cXyMQBTL9mxHJ4zQu_2139zCmZ5dIQ6y36Pl2gQWWomvsCgHDyly4jIL9qACujtuCz9fPAxVHt2zJtUri79dU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش شبکه خبر از اول مهر و بازگشایی مدارس:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83986" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqT5TXjtXU-txeLVa2BpnJnKe7W5BIHVlC4BsyCx33EThEDaSnW6S0h0eTMEf7fwGMmGdIv-PlMU2_NIN_UD93JMo1PbLXi5TneriMOAEqNUQrWrVSz7fH4lqq3hK3_r3vTVgHbbY47Rx1BdL6xxWPwFownp--ltH9oekj3yED5kZUZ0UJlTaZsByS9Ewte-JJiXfykDfWungYASFNtU-IHEHxdfvvslBUyIDQTrx5kbmXZAU2xNmy5dG-peQX8gY1AOwUqpR2SWmw_1GZ1l-xRmguCDODuMNuGXps1JMmOI71HHj8qd001M4q3IOjJC4yGPqEpa3zNh6BmpP0LT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلورمو از این کصشرایی که با هوش مصنوعی چند قسمتی درست میکنن نجات بدید
مخصوصا از کچالو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83985" target="_blank">📅 09:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9Ot7l_u5d__8hTa5VR5r4wGc2weEqayPxljOGW_gp54BhIC8T69LbW8En7xqw4NGaaiubuATXeyu4As8iIvxiuDfU2gTamKd2gnkk7WoEg4g7evINteC0P26G-t0EgwAOmhTfzim2cukgELGMViaHPI40r8Wd1xdUdktai9lel6iMRA2FtXE3E3tHqnEKkakXjCjw7nXwXVoLCwH7y4Uh9_N7l8nfDtBAglj2B8hWhjdk3MvliG65De1eAEsUbJh9SNKxoz8cQHfgKHRt6E3rNDQLZPx8WyG0wmi1xs8Es6AoON4CSjEDrj2m9jSC9KwI_Wl-lHMMSyovfRo8oxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83984" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBuk1cOj8Oyji_CdM-JJpJAnHL2EM9fzATwkWDo--EXCeXy2Hfxzd4jFnU6aAyJdug8GSjANMWGiS5oqBCcJZjehJi8DsFDHKhOGK9x9IroE9NQLsrmG8aIrM14hp-K35MY_v34tZhPGQKvgv_5K2Qx6lY0h7OyOKpQc9WsLu5RKtPBy2zjmzBmkjp_z8Q9I97yhruYMiQO-kqOGybgYt1LPuW1qzKuALb5MUcGv0a35XHKOiGVhm4aeCpo73HsqEhqqb0dnMJw7qE5ermz_g1ndF8aRdWxlDKP91_6EfJXCRCW0J6rhe4OKO-2uCp1uDM7LjZ_jQ3woPW4pCYSEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید پسر شایع
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83983" target="_blank">📅 23:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83982" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83981" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83980" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrlmhVYgJfOqy7MFcBBirTlU5Z8eIY0QyBBZ9hgJuq5cOfzFnN0ymB9Rt9vqgarYlFwT8y60QE_eSuWsp5vGS3b3bDig1YTd94UgkvwiD96aqcqnwn8cqhgGw6xdBZTq10RXvEI6IMmf8oGuGnFr6Z7pRPlXLQnk9ljcQkvy8moKiiBMb6TFd-eOeikiYke4ZMx38cNmA7d2HOwDB_ADtdiXKzBIevXC9h7CRZBS8dkLfKeXXJ4Y0AoiZbFrECVTAh0Fb50-u4QKfJmSmTQmVEw4Q6tov2mHVpF321-qalj1HUVEGIiTWq4wdzqvTpsyp-8YwSW2aYaezpEuReYY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83979" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=g_8aiWwacjQSxLzL-UPvOzDdzPeiPZboxIJWoKuBsBr1qvvMAMmhM14VGnPxb32SpWbwq_m4aUagYH3MXRGNIS7k5fOeZGlf8W0hX6s5idPqoCjqQX3gjSwcbDl95h_E2peASjpolKVdbNk8Yy9bUIrBXvaElAhMIg1tdoaPLWFZ9slnToe-YizVwAXVqjFmDZZID-_BkowPgg1YF5raE3avKWKmFZeXQHWOr3SvCqv4yMVyWcn19Syhl3geITUme-O0Ar7qP5pRZ5a3CpPxEgZBmeYBsWMdEN1SGyKbZ8lcaJwjWFCWEiQaLbMKhvnyoSOLcIoQT_216DXoKLXHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=g_8aiWwacjQSxLzL-UPvOzDdzPeiPZboxIJWoKuBsBr1qvvMAMmhM14VGnPxb32SpWbwq_m4aUagYH3MXRGNIS7k5fOeZGlf8W0hX6s5idPqoCjqQX3gjSwcbDl95h_E2peASjpolKVdbNk8Yy9bUIrBXvaElAhMIg1tdoaPLWFZ9slnToe-YizVwAXVqjFmDZZID-_BkowPgg1YF5raE3avKWKmFZeXQHWOr3SvCqv4yMVyWcn19Syhl3geITUme-O0Ar7qP5pRZ5a3CpPxEgZBmeYBsWMdEN1SGyKbZ8lcaJwjWFCWEiQaLbMKhvnyoSOLcIoQT_216DXoKLXHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83978" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VskAgDfGalp2Z1arubtsp3Oo4qSsHjjxQl68wrQ5e99UQXd3mRVLJBOaFkLthzX05mKPG1DCYKQTe913FlKQVbP14H_1nTPZiEQuYXZqzdOOrLnHVl8e5psR32XX7bhdYcbd8Rg3dTu3kLov1LK6cT3-eWf58fOx1VjB_qynDbTV56t2TjtTxVLgHdk7g47oZNI2MsSAHgP8TSWsH3YmHEx9D7c-_msXZpY7eE82Y3sBjoxzwfaPSOiws2-a3R7TROdtBim-0rPvWLt0Pcq5r1DmRyEcspJbJURaDxDD6yQnYuWEAM15N_ZYsiQGnslNFxRg1W9KgrTRXhz_-Hoh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی دو روز شکل آدم بود باز طاقت نیاورد ریش‌هاش رو بگا داد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83975" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=JyR52FRsqZVXS_tvn8895fTxIMK3VpIkqg5din78zw5hhDwyDHYd8ukaK9qr-JaRfw_uzfVaHgHypG98YGSKGa1V_RLpPWR5Y6XzVn5KnEBWfUUF4iJzm6Vl60gvZqOFTqgjeUFo8KxWVZmMjtRrtT9CCGIZnzbTvrQrB2Ib451lvHv71eycLbN72XwrM56K1ERXONuvWWLapxIsHRSWrOPHoX5ydsEzG3uL5rgJjUjuRRNwwI_UvEBqefDUGnNqB31rxSO-m9XgFukjz4CDL03B9bCAQoEXn8B7pd3HQkQbkaEcHCpc-gcJKIR5EsvaiJw1nv5NQmRYXu1emZfJ_KNvkncC-IARk-uVQXTNTAO7TKdDtVdzHDpTa07NqLK64RcRGQ2PvP5O_FDxVa8w2FrCr6HWuUeHpFKmRQr-IOtfzivZljPH7gjMEXBcGaRBTIzoXqngTLtSxcyiUvFfGVtdAJf1xQppKzdDM75pemD1ae5HGQ9eVJqCeFcm644dfiesF72vUeph-kBpi5PQ9M-maXnfQ5X6aN9E5z8SCWsEVGwGVroev6ZkrNXl6JInOgSC9FxqBjSLde6VxjNQlGBBX8qN0aALy9eNi0wpmbc_j9ZkgFGxNy71cdPUlJtys6hF838TxojwQSoxbMhWCSlGM8ydsHNuIrOU3C8kwRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=JyR52FRsqZVXS_tvn8895fTxIMK3VpIkqg5din78zw5hhDwyDHYd8ukaK9qr-JaRfw_uzfVaHgHypG98YGSKGa1V_RLpPWR5Y6XzVn5KnEBWfUUF4iJzm6Vl60gvZqOFTqgjeUFo8KxWVZmMjtRrtT9CCGIZnzbTvrQrB2Ib451lvHv71eycLbN72XwrM56K1ERXONuvWWLapxIsHRSWrOPHoX5ydsEzG3uL5rgJjUjuRRNwwI_UvEBqefDUGnNqB31rxSO-m9XgFukjz4CDL03B9bCAQoEXn8B7pd3HQkQbkaEcHCpc-gcJKIR5EsvaiJw1nv5NQmRYXu1emZfJ_KNvkncC-IARk-uVQXTNTAO7TKdDtVdzHDpTa07NqLK64RcRGQ2PvP5O_FDxVa8w2FrCr6HWuUeHpFKmRQr-IOtfzivZljPH7gjMEXBcGaRBTIzoXqngTLtSxcyiUvFfGVtdAJf1xQppKzdDM75pemD1ae5HGQ9eVJqCeFcm644dfiesF72vUeph-kBpi5PQ9M-maXnfQ5X6aN9E5z8SCWsEVGwGVroev6ZkrNXl6JInOgSC9FxqBjSLde6VxjNQlGBBX8qN0aALy9eNi0wpmbc_j9ZkgFGxNy71cdPUlJtys6hF838TxojwQSoxbMhWCSlGM8ydsHNuIrOU3C8kwRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب رو بیت کاگان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83974" target="_blank">📅 20:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCEzUImEpmNKflA6dZ-krzb3GCE_Dc-IkQML0d7aKE7u-tLozg-k3mYVPqDkrXiAMad9mE_PEY-FHtBKIZs4hc3gEycpAAI0W0pSC6vP9G2bFkE1IWn38Gyp0yvanlys5Ue0jQWHDVutGrXmdBEqumuJBSrbj34OmOrDmKeyXSfD16xkO55a98KVuH0ytMAl1CRB9ZNNVZVlE3DhCQBtZ9ebMwH6BCb70aq8wz_NUccwRD9aM1U-zcRmMXi3ErPJVFLcymub7zjWwFj0TXLpiKY3-OgFmVQb_1Oq1QMxUW9VYi6YAMlcp4Ac1WwnvRjXoYIFs05cCJZ6e3BnAeFSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف:
رئیس‌جمهور پزشکیان فقط از طرف یک دولت صحبت نکرد؛ بلکه صدای یک تمدن ۳۰۰۰ ساله بود. او صدای قدرتمند شجاعت، مقاومت و قدرت جمهوری اسلامی ایران بود.
زنده باد ملت سربلند و مقاوم ایران.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83973" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83972" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83971">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=Zh_ho6ug1s4E8Peu-1PLIxcU3wrYJY6jDPVjf6LUjsCi7xLm3vYYs7dTwbgwn5t9ejlTISRgmRH0DFJy40w2tEHwZhdmaoV5Ot-xYSn2JRCQNdeRgHLN_6nY52tBta4FBPLjJ0g5C4RbDPbtAz-75hxbzBZkjsIxiAEKscThwPbb11OAOxDIBxevcFMtNG5QlMjVLKEpQMtczIUADa8PWhUDEVCNZvXIjjzLs5NFlspfU4RqbQcgp82x1T3yDxcwQMAqPHxdN6tpp32QQjh850G550-IVrBoMVqqcVw2C6-iXXGrFyWQuMulMbyI-bYI-RxQN1zaFqMeyC_0k0zj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=Zh_ho6ug1s4E8Peu-1PLIxcU3wrYJY6jDPVjf6LUjsCi7xLm3vYYs7dTwbgwn5t9ejlTISRgmRH0DFJy40w2tEHwZhdmaoV5Ot-xYSn2JRCQNdeRgHLN_6nY52tBta4FBPLjJ0g5C4RbDPbtAz-75hxbzBZkjsIxiAEKscThwPbb11OAOxDIBxevcFMtNG5QlMjVLKEpQMtczIUADa8PWhUDEVCNZvXIjjzLs5NFlspfU4RqbQcgp82x1T3yDxcwQMAqPHxdN6tpp32QQjh850G550-IVrBoMVqqcVw2C6-iXXGrFyWQuMulMbyI-bYI-RxQN1zaFqMeyC_0k0zj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g1
🅰
📎
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83971" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=jhkl-_yiOm6akuZ5PC0nxjZuhjZvMIrxHDqFW4fhGOd3AhKycdQBmjza8cV-RWt0Oai92oSUqmp_ARxrrT15Bc8lln76Lux7RUUOOrNqs9fgc7OZO-MFcJq2dBPA77p9MVwzGXsTX2Mg5sl7N9zhZE4pd_YgMCtopvJXTd5sd1H16Weyy2QkEpT-maZLJvZkrKrCbVyS1BQtZBdA01FuzYI7j_2advSroUX-vKTZ1cimoGDZR0XzH82V4JFPlFT3VCNhf51hOh2TZym6H2hkG9zFBRLPjvK3Xju9ZMdnr7MAcwFhBrZgXBQ4nAXffvLk7AAoLefSdq0Dhnu_LblJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=jhkl-_yiOm6akuZ5PC0nxjZuhjZvMIrxHDqFW4fhGOd3AhKycdQBmjza8cV-RWt0Oai92oSUqmp_ARxrrT15Bc8lln76Lux7RUUOOrNqs9fgc7OZO-MFcJq2dBPA77p9MVwzGXsTX2Mg5sl7N9zhZE4pd_YgMCtopvJXTd5sd1H16Weyy2QkEpT-maZLJvZkrKrCbVyS1BQtZBdA01FuzYI7j_2advSroUX-vKTZ1cimoGDZR0XzH82V4JFPlFT3VCNhf51hOh2TZym6H2hkG9zFBRLPjvK3Xju9ZMdnr7MAcwFhBrZgXBQ4nAXffvLk7AAoLefSdq0Dhnu_LblJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
من فکر کنم تاکتیک ایرانی‌ها اینه که فکر می‌کنن تو انتخابات آینده دموکرات ها پیروز میشن و اگه پیروز بشن دیگه ترامپ مجبوره بیخیال ایران بشه و از جنگ خارج بشه.
و خب جواب من اینه که خ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83970" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تسنیم:
عراقچی دیروز خودسرانه و بدون اطلاع دادن به نهادهای مربوطه و مجتبی خامنه‌ای، زنگ زده به ویتکاف و باهاش لاس زده و مذاکره تکنیکی کرده و برا همین باید توبیخ شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83969" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حین سخنرانی پزشکیان، نماینده‌های:
1. ایالات متحده آمریکا
2. بریتانیا
3. آلمان
4. فرانسه
5. اسرائیل
6. سوریه
7. لبنان
8. عربستان
9. مصر
10. امارات
11. الجزایر
12. لهستان
13. سوئد
14. دانمارک
15. کانادا
16. ژاپن
17. جمهوری آذربایجان
18. مالزی
19. نیوزیلند
20. استرالیا
21. جمهوری خلق کنگو
22. اکوادور
23. قبرس
24. ایسلند
25. مکزیک
سالن مجمع‌بین‌المللی‌سازمان‌ملل رو ترک کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83968" target="_blank">📅 18:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83967" target="_blank">📅 18:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=twbsH7dvc3qwU4qcm4gzAYRWjTwqsPkIq2obCOwVbUqDRJ_WMHVjwHpiTLqY9Xse_u4bo-PqjezBbfCA05ncXUJuaa3eqa1NMIHeAaf6gFx5a0vGn5L2_yEJYECMnoXHhX7SpURtGTG9zJD9GrAzlVi20ZUWkUuBtbMX227nEWFQp595P-2BN3egqhWTwCT92xTN5CpYa2owgOECg5VzfU_rQuH49ZPsyWZKurbfjZ5kTC0rfVvER1EfrirAgtN0eUk3KxZ_HWSlMeESlwE5PwP7KGGaQj8eGxGm77YbNefm9jjyTKi5fFhOBdLmr8r7w35zpT_XiiCYXDNtOavinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=twbsH7dvc3qwU4qcm4gzAYRWjTwqsPkIq2obCOwVbUqDRJ_WMHVjwHpiTLqY9Xse_u4bo-PqjezBbfCA05ncXUJuaa3eqa1NMIHeAaf6gFx5a0vGn5L2_yEJYECMnoXHhX7SpURtGTG9zJD9GrAzlVi20ZUWkUuBtbMX227nEWFQp595P-2BN3egqhWTwCT92xTN5CpYa2owgOECg5VzfU_rQuH49ZPsyWZKurbfjZ5kTC0rfVvER1EfrirAgtN0eUk3KxZ_HWSlMeESlwE5PwP7KGGaQj8eGxGm77YbNefm9jjyTKi5fFhOBdLmr8r7w35zpT_XiiCYXDNtOavinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت آمریکایی در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخنرانی می‌کرد، سالن را ترک کرد.
این درحالی است که نماینده ایران زمان سخنرانی ترامپ محل را ترک نکرده بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83966" target="_blank">📅 18:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn2m681HABPJB24bl1JQeZyiDToKW9xa7rKxbDRPsiNgpe2BMGD3lPX96XkmyAk-_9wtWueXL-dydUjsEtDAK7frEssXuQ-WIM5Ig0r1DZ9trAXVFZP07D9JXIgLjI9b1FA9JsBAuSuSm-r6WvJ2Su80tU72OpJFKvaUhZcwx6iQi8t6OwiYqZSNPGgYnXqbMCrbkYP1XZV30wpsHsxVUztthH_3i2sFpi93n1pxIPz6dCZBRFUNnz6GJozB2WvClbbLHAvb6qMhPndR13VkxVevCNrOq7ypfivL7C8vFoDDwksUi_2FcMB7IzGoS9GZR3ctF0-moLHB-oOzvRvuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83965" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGHdDjDQM2abMGKaAprg-cliTt297RfmAJVXNV02oib5DpVPhMzNfc7Q3hp6XlklIh0dLWe21EiwfQ6T8A4n9bb0VXS6fr9vm0ybJ-ftJ5yhMpcuyTN63YUPK2fxiPcagbov_dq-zl36-hRskDnaV227-XQd63D7VZfyjiwnnfpNxNrozg0yQ6GxAsbc9FEAGxtvl6OEnIvqs210yKHcNwchzPopT40p5YmhzNcG9JeJ6ueW9XP5uRgSuTtTv75kC19Prgl7KPWOr0G-tBu0d6hcO366U6Cg-X49T-RHB-3cs5140NgfxMNs5ZSImFocOkZkhnn5PxUEeMIRFnEfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار کوروش از فناش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83964" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تو سراوان باز بین نیروی های نظامی و افراد مسلح ناشناس درگیری شروع شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83963" target="_blank">📅 16:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🕸🕷</strong></div>
<div class="tg-text">اقا تر بزنه ابرو ی مملکت میره</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83962" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWD-mFvDDYq8aZYQHMMpJSidqm4J2UyLBcw3hYvQ1OXvqhtsmmScUr4mKnlhP9peEswLmHx3kRAO3LK9kWn5gpCaMqG-XbmLsqd-xe-04DnUQ14WpafCPD9nk0CWpayrHzindEAPAZ6J17wrm05HFm597s1kptFCTKSMvecmYUA_hkC8bDhZv_DehcETVB8NlUJlKUgV_HQwePXAg7E6IYnKkLNGgvTzfv7YFmqOKtQST1TB9q9GNBERzUIg3I1_7mbScOgWURrK4DNJPh5IDvdZOd2iujjFdkPvljYSIsUZkFYnR46En0vuP4OpzyC6B_WGI7iQTjCs7vCzkgLI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بترکونی رئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83961" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کوروش وانتونز:
به زودی یه برنامه یوتیوبی میزنم که هیچکس دیگه نخواد چنل پوتک رو دنبال کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83960" target="_blank">📅 14:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استاد خوش چشم تحلیلگر ارشد صداسیما: کیری قوی ایم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83959" target="_blank">📅 13:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شرکت کننده های عشق ابدی قشنگ ۲۰۰.۳۰۰ سال وسطن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83958" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spYebKs-kY7KdhIImP8dUyT9FwiwAuIs0xlbv8o8nT2kkzSjvD_rSZ2xOQz2zMot-WpZzJMgeqE9RFvPK9dkvcQBBjCcwnWvI-Rhbt1GXbIxVzwASUTuDQDP0OV0lz8vClNKjKNY_SJ4vV89bhhkbFTLM3lFxnLzDovCM_Q2CqoQL6sadSc4FUlmPaiAr-lPEdph2xZUe61i9H9O3mAvBS9bJMmWdcS0Hvx4bt1cFs1zy6R-Cu_euAQ5W0Boxc_FMacQk6ix2z1NcPitkOwGKxWS8lYfCItp3GaWpJLoeU3-fAIrYcg5zLI-iJHAqY0FvGRQug9jKBzMY_YefD69Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالتی هستیم که تورم به ۱۵۰ درصد رسیده، محاصره شدیم و هیچی وارد و خارج نمیشه و داریم بگا میریم، به دلیل بگا رفتن پالایشگاه ها و پتروشیمی ها و کارخونه های فولاد بعضی اجناس تولید داخلی حتی ده برابر شده، تو پمپ بنزین ها باید دوساعت صف وایسیم که ۲۰ لیتر بنزنین بدن بهمون
و تو این شرایط دغدغه‌های ذهنی ویدا سادات:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83955" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBZL3vU1ZpdOylI-T1nw1phsCeT8BKzxHy7gAgziskxmi8cFqnWydqAFTCFCfFcYKrP0Lh9xYL4iZE0E7ip6LM4TD1wZMfLpwMv2QQlO9dzZkPKH-ukYg90-AISbn47qWH4lnRqWjztt4zbMZ7WBQ1Y4E86cCcLADuVHoSpBsGNp85jmB6gU8O7oNdUVjeE5hsCRGfGD2y35EUFAPWxJ5qKP47ywvS2s3BLPFbMBMZ1wMeUmT9sxtCOaNtrjRmLPqXctt6tf8Vpt6WRZ26cO96RlFDJ5d4Mcuj4N2Xcm8_8S-wBKK03A4lIDfaNTVTgJM154SaEaHhF1m-651axUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - اسلوونی
⏰
ساعت ۱۷:۳۰
🌎
📲
ایتالیا - فنلاند
😀
ساعت ۲۲:۳۰
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
R1
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83954" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp9r60Dws6k1O3osF70gbOSPr8WtlxEsY4mwb56Ncv7wggjSAc8jKirCsJYwt2qc2HNGUNTRrSHzhykF2kLLQyeRqTmKiVnd4LHAngGMOKPPAnvm9tB8L1WPn4gbFsMxhOiP8s-z9UHYc6He0K1PURyKvWr7BQF5repxb3i5xUUkzmDA9vKvzYO4USp-_NQhTvLaVrF_2s-D5NkVrDGWT9aBkqkF72MycB6pYnd_LB7pNwjrqvTm_tMhUnHEifbJrLYoOaMXvt6_Te5O-pNrh3aAMN1rGbhlvdxPcTAIZSrBQqcwu5zPo4Sck3E23xWd5Ux0VUjFw0hHC-byzHP1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان بیژن بودا، از خلبانان نیروی هوایی شاهنشاهی ایران و از اعضای خانواده نیروی هوایی، درگذشت
او سابقه پرواز با دو جنگنده F-4 Phantom II و F-14 Tomcat را در کارنامه خود داشت و از خلبانان باتجربه این دو جنگنده به شمار می‌رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83953" target="_blank">📅 09:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اونی که امروز نمیره عقل نداره، بچه زرنگ امروز میره با معلما رفیق میشه از شنبه دیگه نمیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83952" target="_blank">📅 09:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مدرسه چطوره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83951" target="_blank">📅 08:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFYBlnBTekDkyi5lUb_8DahKGQ3lz06pVdJsbdmm3UFXvV4gjrkxLhwyvRJeJaxn0X-r_8Wgy3rXvGyG4eHvp7iNVILxqvlESVtrt9N3huq-VMTta1CAJ1Vz9g4Ejvhz96OQMI_faHGOGQi7s4QmVOfw3AoGeFGvlqHd5M58ZCDADPN7vf_S_4IlsdvowMjDZwlhwrtlbyY7k4S75dWJ2DRZ6j3bDF-HPqgw7zxu8CEqPJERLIJ5-LzaczbaIS8PvTOpXf85rcFBB79BVnsF0q9_nm6lxH1kDp8aBIvW_-BSm7mIrwpgNCypP-EmFbo6jAl9HakX-mQKLQxJJ-cwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نیویورک بگید مسعود اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83950" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آخجون ویلسون دوباره مست کرده</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83949" target="_blank">📅 01:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر پسر عموی مهدی چیکارا میکنه سپاه یه موشک ول داد سمت یه کشتی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83948" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044b34344.mp4?token=qGWCr_LBD4EH4XCdKZVKuorLCCqTIBKuQmVeqH3v1QstW7jFiSe0pgie-Q66d62hkk0gZXezDssYnMlXAzb7vZ07kVCcDitGrK6qR1ZISoUFaZynXNoAGoszI19JLy1CRZ4YR0q1IgRFdubEV3iNe3dzM4Mw9DnPMA6-3Nezbn8tEHYF1wt2Qxho9leqvFtpUp5bZZuQoI1WTuJBtTU_J3CDPAL7fzQ69ojmfCn4gxdORSaX1plFa8B2nDztsAmBQ5N0klHR6vZAPYcXOjZ78xsMKdcTxPv17gGEjtFG_7VXKl89MJU8Jqj6_VPaDmZzcEw5xggXDGeNwbp1vpn1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044b34344.mp4?token=qGWCr_LBD4EH4XCdKZVKuorLCCqTIBKuQmVeqH3v1QstW7jFiSe0pgie-Q66d62hkk0gZXezDssYnMlXAzb7vZ07kVCcDitGrK6qR1ZISoUFaZynXNoAGoszI19JLy1CRZ4YR0q1IgRFdubEV3iNe3dzM4Mw9DnPMA6-3Nezbn8tEHYF1wt2Qxho9leqvFtpUp5bZZuQoI1WTuJBtTU_J3CDPAL7fzQ69ojmfCn4gxdORSaX1plFa8B2nDztsAmBQ5N0klHR6vZAPYcXOjZ78xsMKdcTxPv17gGEjtFG_7VXKl89MJU8Jqj6_VPaDmZzcEw5xggXDGeNwbp1vpn1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یعنی کیرم تو این زندگی ای که من میکنم
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/83947" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ناموسا بعد از بیف وانتونز با پوتک هروقت چنل کوروشو باز میکنم یه کصشری به پوتک انداخته، بس کن کولی خسته شدیم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83946" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZ_XsRvaC35ZkwaCmJg9Yg7Smospx-j-C4N5fa2fjHVngeaVe0HFUWBQhBbW7C4MsgfcrHK91X0dK8YNAc-T4NV4b86K-u3caVhoEAmTV4MTZ0nZcFALlF59gte0RksbFx_1Cer2w-WX3KOLbAbG_mUREwP-y_9YLC4tgt2G0yUhxotdnh8D8AiewvnOsv-Std43si7EpkbNhLi3gzs7UOebHfdSWj9Kklshw4xcIMv_regbDTdP-0R8Z-_upe8lWNB80VqGqXFlqqUrQjbIeHFgi9KMPYm_25K_IxGrnyO8UBcKb1dphXg7OGYcoPt2WynjdU6gPYGx3AUrXk3MSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_91tvszToxKrxK-ma7UR5evMAHMEK3BsyzT7BEIx2A8CTGfZfnrIlXlVC0g5WJIOTYoMBEmkYLl7xY-KjMtzW32_Xxv0Rdx1BT7xaxJmpO0XzVZUaXnR0Uh-amtLlrHTFevNRidnSUa07lSBw4kEveFgM34LlLq1robHnp5tw0MYvtS_Jf-nKlwJ0rsBZmSrvyKSBGWTUgTISxqAmNHs5d0M9bJK8lSoft2_TxOjdnXqhm19fGThgOUxX0KfDIg_Tne4ACex03MiZUFfcggNWZTs4epyVZDtnQSbok6bIkn-Xl45bLcJJ1qvDF23rDY5PQaqU8srGwvAxu8qM2hLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پول دونیته ها حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83944" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=hpTvLAvgshHAwIziDkl03XZSQfOB7ESexkiQ8KoomQqBrU8ss1OAAzTpwMLF_HliR9Coj51Ns1J4BMyuiZSD4sUU4RDM7Ye8KkSaFoWBlQmcVIekkAJw8hh2oeAtDJh1tOF1myOXWbvgSAk8RzSXQBDKgp61fMXOAUL4wdFcFjAJi-0V4AmIltc_30VDMWfYIHfRSsL5qUSDr6FupwDXnB6o1BGmDV3SMzym57mGmFD4vA-p6PssrK76fGAqkhD2McGrX9rIdt2SQexBaL5K1dD-5oONkxQU9hxDWpn0j9s8cdHCfLOpFTAvszPnYtspzCySFH30qNJT6eVEq5sqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=hpTvLAvgshHAwIziDkl03XZSQfOB7ESexkiQ8KoomQqBrU8ss1OAAzTpwMLF_HliR9Coj51Ns1J4BMyuiZSD4sUU4RDM7Ye8KkSaFoWBlQmcVIekkAJw8hh2oeAtDJh1tOF1myOXWbvgSAk8RzSXQBDKgp61fMXOAUL4wdFcFjAJi-0V4AmIltc_30VDMWfYIHfRSsL5qUSDr6FupwDXnB6o1BGmDV3SMzym57mGmFD4vA-p6PssrK76fGAqkhD2McGrX9rIdt2SQexBaL5K1dD-5oONkxQU9hxDWpn0j9s8cdHCfLOpFTAvszPnYtspzCySFH30qNJT6eVEq5sqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکارو یادشونه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83943" target="_blank">📅 23:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83941">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRapBadVpn - فیلترشکن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx758443Z86TH1ktgeMGNP9g4uIXeDzSoqkW8SdcNEsWAUBYY_70CaecRTXpEfGYCy4_YPyr_G6XiKDdLnecZkwk5J7oaezF0xmkt1tmXZ-8-QpG5eXd4UwkjnnmkwESm5gRApNx3jnmZqmnigE-ehhSy6veK_bXG3fKPfYB-m1Gtf7yMzRKCG7X6GCyNjYV3ves844n9cCUR9Gjfc28jxBmAES8UgN0-zSemQ_OFbvTfJ82Ey_Up5Ty4YAJ3toRHqPIRLmzBKIYP8nbEBeutAxgInNmVZGnmA8diuSCuX_-RwfgS4afm4c6RbWe6JEwQqTbQfP2ukUT6SL97xrMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
وصل شدن آسونه؛ خوب وصل موندن مهمه!
اگه از قطعی‌های پشت‌سرهم، سرعت پایین و عوض کردن مداوم VPN خسته شدی،
RapBaad VPN
رو امتحان کن.
🌍
سرورهای متنوع جهانی
🚀
اتصال سریع و پایدار
🔒
امنیت بالا
📡
پینگ پایین
💻
پشتیبانی 24/7
🔥
بسته‌ها از
۴ تا ۱۰۰ گیگ
💵
هر گیگ فقط زیر
۴,۰۰۰ تومان
و مهم‌تر از همه؟
لازم نیست به تعریف ما اعتماد کنی
😏
اول تست رایگان بگیر، کیفیتشو ببین، بعد خرید کن.
👇
ورود و دریافت تست از لینک زیر
🔺
@RAPBAADVPN_BOT - Test
🔺
@RAPBAADVPN_BOT - Test</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83941" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83939" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83938" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83937" target="_blank">📅 21:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8382999db1.mp4?token=DRjzYnKUG0R4xXowQkDVcwdVNS4I-0cg4-fGBcfpBJtcuaovOwSoGUZAHWjGr40EBG4mLPV8XByQV2ITwQ-MVERkmvFr19mt1C5hoQL9Z_k_jaklaovhF6CKW6W_yILY33lzUsXd3ezekNDPg2PvWctKwKuUI5JOG3tuNiPEB9iolzc1uaBAnzJd1IlsP-TcUwtnFib0yEG6ySN5mDBDSl3suiNrW5jKDL6JEkQ7I-xKtsSXj5vRefhSkPzTK7DRnumVAj-2w_UX7zgr7JevLawJLjMa_KTHletpsnqARUWQBa4tocjUnRC5qaWkf5LYso_4IiZXwBPlLpJS_lxROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8382999db1.mp4?token=DRjzYnKUG0R4xXowQkDVcwdVNS4I-0cg4-fGBcfpBJtcuaovOwSoGUZAHWjGr40EBG4mLPV8XByQV2ITwQ-MVERkmvFr19mt1C5hoQL9Z_k_jaklaovhF6CKW6W_yILY33lzUsXd3ezekNDPg2PvWctKwKuUI5JOG3tuNiPEB9iolzc1uaBAnzJd1IlsP-TcUwtnFib0yEG6ySN5mDBDSl3suiNrW5jKDL6JEkQ7I-xKtsSXj5vRefhSkPzTK7DRnumVAj-2w_UX7zgr7JevLawJLjMa_KTHletpsnqARUWQBa4tocjUnRC5qaWkf5LYso_4IiZXwBPlLpJS_lxROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو سرحال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83936" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان تروخدا شوخیاتون با باز شدن مدرسه رو تموم کنید، اینا انقد تعطیل بودن الان از خداشونه مدرسه باز بشه چند روز برن مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83935" target="_blank">📅 19:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سالی یه بار یه خبر میاد که یه زندانی حکمش اعدام بوده بعد از چند سال عفو خورده و آزاد شده، بعد از آزادی از ذوقش سکته کرده مرده، نمیدونم چرا این خبر هر سال داره تکرار میشه، بس.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83934" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کی فکرشو میکرد یه روزی نتانیاهو، پزشکیان، ترامپ و رضاپهلوی همزمان تو نیویورک باشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83933" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=Eui8EkUQeDjzQuHTF7hzDHKyLg6V2pm71mXIWrzbYgGSy0ZXAIM9iLxEaAEcEdiq0I2kee37Pe6mgkiJs4i_lIv0fls3J4pMbtkWfLruwcoRzRbzUpl8yiY0HNQs9pK3atBC35vy-UbRHdTmMWnpnlLZm-fc8MeUrB0MSsblCyQTDPcJ55f0NLS4-c9DTdMv4NvjGmxyqzaqyremb5YJRcA-Bzo9tv89BwvmH2xWh5Y95LvUeaDNEVIgfpdxj17RTkOdif58u81cw70l1XPVK9-U-HRIgdaH4by6EEo6J9s_2-xZiNakuQgAqWaBIk56IFwvWJMTQPTsX5oQZ3S1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=Eui8EkUQeDjzQuHTF7hzDHKyLg6V2pm71mXIWrzbYgGSy0ZXAIM9iLxEaAEcEdiq0I2kee37Pe6mgkiJs4i_lIv0fls3J4pMbtkWfLruwcoRzRbzUpl8yiY0HNQs9pK3atBC35vy-UbRHdTmMWnpnlLZm-fc8MeUrB0MSsblCyQTDPcJ55f0NLS4-c9DTdMv4NvjGmxyqzaqyremb5YJRcA-Bzo9tv89BwvmH2xWh5Y95LvUeaDNEVIgfpdxj17RTkOdif58u81cw70l1XPVK9-U-HRIgdaH4by6EEo6J9s_2-xZiNakuQgAqWaBIk56IFwvWJMTQPTsX5oQZ3S1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برا کی ویدیو میگیری مشتی فنای تو ماماناشون گوشی‌شون رو هفته پیش گرفتن ازشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83932" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83931" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه سوالی که هرچند وقت یبار میاد تو ذهنم اینه که کوتینیو چطوری دلش اومد هفتمی و هشتمی رو بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83929" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9SirWlcXBESUpjggAHnmJSxNBhO1kR7t5bpDpe-7oGhpk3BLFYXMR4KkzrFNjivSZFPavXJAgMi3QIcuTvCjJrFrstPKZ4C59dhq52mpsgWRpFTDyHGubcbt9mFFva49brl_YAQrO16BVJzA__9H3nVMFIbBWe8fmJlFqfeKgjfl68imtpDaYmm1xGm-7FCHylsWwFCkl6YR9pgTVqmS2AKcuSG1olm2x-7fFn18SEfFPdXKSKNhNA7inSVsszSx8v-PvBWOWV7wONwGsIoBdktQEBJJ28oJg8D6eK9zfgQjd-B6vXNpM1YHh9Zwu11Decb6wPefw3GlLkIyaaF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین خاطره ای که از جوونیت یادمه با حسین خاک تو ماشین بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83928" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83927" target="_blank">📅 15:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwqS02HXfrdo7WS8vVF5kIs-R3XEiarTLMJPQfU08A9HrIxeycDV8jnvUY7GuDDHeI48GhcOFybBJ5uLIff_BcdwVhv3REm5GPaS-SJW2UglFoc7zX68gTR-G6vXF0szOvkhD2FhpUspG5S0V5LtkWe1F6VxZFk3C6Atkvu_ZwRWaqBoWfU5MHWSPwMDegCaxJNzMNMLHnntgDYeLo0pWf7cAU2tnMbUsaAcf7wtVj8jAzjtji-jV9h4r-Z1Laa2LN2nVOG8aag1y_X-ywXnApI08e1ML1v8vcJEMt5z01lanZuAOXVuOpXqcViCWdWvscp8SvFS_XErL3kZtbnJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83926" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شهریور ۱۳۵۹؛ روز آغاز تجاوز عراق به ایران
ساعت ۱۳:۳۰ روز ۳۱ شهریور ۱۳۵۹، عراق با حمله گسترده هوایی و زمینی، تجاوز به خاک ایران را آغاز کرد. ایرانیان در دفاع از سرزمین خود ایستادند تا ایران به دست ارتش متجاوز عراق نیفتد؛ جنگی که پس از نزدیک به هشت سال، با برقراری آتش‌بس در ۲۰ اوت ۱۹۸۸ / ۲۹ مرداد ۱۳۶۷ متوقف شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83925" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بکیرم
ماکه پول نداریم سفر داخلیشم با هواپیما بریم
🤣</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83924" target="_blank">📅 13:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">از فردا محاصره هوایی هم شروع میشه و هیچ هواپیمایی از ایران حق خروج از کشور و هیچ هواپیمایی حق ورود به ایران رو نداره
احتمالا بعد عملی شدن این بزودی محاصره زمینی هم شروع میشه و کلا زندانی میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83923" target="_blank">📅 13:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83921" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسعود رفت نیویورک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83920" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=lGl_9QC_FDGsllb8dk2en07y5HcuYviRVgqmCY0NldbJIm45z2Ryq9yge4VlCXG2b2-gkFGySDgSM-1JqbnTCVNfXQoCSXM2Z9IO1fLKC5DDrZl4zooAuseLhxn5BXKybU0j6hQwadOPI8WwW4darok3wE7Cj7pTJfZgyHkxAiTI20kGL9wgXkGBvrQypcRvOVwNB0LvgXIaQIvP6RdRez71XapDKcTlQ7L2wAMx2Ehs2nU3t54OSwqoVm0ENUZuwVWxJIpdndzDqykFXV1PJCjNoSnYMJZLKfMVG-W3CPuoqff2QqeJXUhfLgiDm_5OkF1ppundEtCsypx_yBv6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=lGl_9QC_FDGsllb8dk2en07y5HcuYviRVgqmCY0NldbJIm45z2Ryq9yge4VlCXG2b2-gkFGySDgSM-1JqbnTCVNfXQoCSXM2Z9IO1fLKC5DDrZl4zooAuseLhxn5BXKybU0j6hQwadOPI8WwW4darok3wE7Cj7pTJfZgyHkxAiTI20kGL9wgXkGBvrQypcRvOVwNB0LvgXIaQIvP6RdRez71XapDKcTlQ7L2wAMx2Ehs2nU3t54OSwqoVm0ENUZuwVWxJIpdndzDqykFXV1PJCjNoSnYMJZLKfMVG-W3CPuoqff2QqeJXUhfLgiDm_5OkF1ppundEtCsypx_yBv6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی تو تا الان همچین استعدادی داشتی اون کصشرارو میخوندی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83919" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83918" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کوروش وانتونز گفت که می‌خواد یه سایت بزنه که توش رپرای مطرح رپفارسی (مثل سروش هیچکس) به صورت ناشناس رای بدن که کی برنده بیف بود تا امثال پوریا پوتک با بات خریدن و جو سازی نتونن خودشون رو برنده بیف جا بزنن.
همچنین در ویس دیگری در ادامه اعلام کرد که زنش او را به خاطر فحاشی‌ها و توهین‌های زشتش در بیف اخیرش با پوریا پوتک سرزنش کرده و به همین دلیل او اکنون یک انسان باادب است که از توهین‌های ناموسی و زشت خود به شدت پشیمان و به طور جِدّ در صدد تکرار نکردن آنهاست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83915" target="_blank">📅 01:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خب برگردید بخیر گذشت
صرفا رادارا یه تهدید نشون دادن برا همین جنگنده ها پرواز کردن، بعد فهمیدن خبری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/83913" target="_blank">📅 00:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">من به شخصه اروپا رو به خویشتن داری و کاهش تنش ها دعوت میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/83911" target="_blank">📅 00:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/83909" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/funhiphop/83907" target="_blank">📅 00:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نخست وزیر عراق اعلام کرد همه گروه‌های مسلح عراق سه ماه فرصت دارن که خلع سلاح بشن و اسلحه هاشون رو به دولت تحویل بدن و اگه ندن باهاشون برخورد میشه و مجرم شناخته میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83904" target="_blank">📅 00:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNyTEtbJJ1yfdP7y_4D5PhE6MUUtfAvM8lqN5Nszlu_SidFjU9tWiXhp2nHtd0HjJpZoegjuP7VR-dIVon74Xy4tJvEfAZf5GmIIbC1dOQew6B6SeqKV7OI9JDx3z10nmcF6mXKIsXwDf8AKmY8hV3hAfysfk52jsidDG8UG4Y68ovq4iC1GplNoq588OocQ6sLHv57VmpXplYSsTRIEmEt8y4Jj5y8ouybWjqEB56TuQFVrSYMuv_I4z2YlLmr1PvEGXAewxzmgJ0WIGCPnUGZ-ePSeLf2fbKlmWTGQ39022VZbMzkc_Whor4WkUjzaJe8GYJoVBM8pF344M7JBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح حرفه ای بودن نیرو ها رو میتونید از کلت توی جا خشابی تشخیص بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/83903" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCXbS5tmLp5Uw9jxTYuluDBoF2e2N-gTOvEh9xBuzFXXm3gEm-Ugb77iUtzyFQgwcMfVnEkuOgK3JMZweQUrq0MT3vDblIb0DZVv8PQaPhUSWjRjlc5LpUJp2cgS7pjB1Y3kbBE8p6gA8UZ8xhtTpE85uquWUhQRn8i2CJ0-NyxtKGCFDFr1x9lMWD1aDyKK0jVZX5XqV3MIc5A-Uq_7OwF07GmxnN4Uac6PZzfu-TrrHlQN2k-_Rh5_UaZFmU4VcLAp215qvsswo2K-5IF1dyg3m7ScQBGe8k_WIhwSv_87GpADamV63CRDRWDOpCqunQWVEDCv8uPVzdy5_MVVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف نمیتونم به جیک پاول فحش بدم اونوقت بسنت چنلمونو تحریم میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83902" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=fvPMMF94WBd1njDNhuG3VaD2Nb29Y3BXmr6wMAh5-KepwaiPtowNiuVqtGsvxJfdnPWJ_oIrGFIsF3oI4HZst2b19u4c0K4A4dyyNc2lS-eJ_2x1zIJQHr8BOk8Z38EZQ_5iDyO-qFUJtpYDOvR6UMdPTMDfeG5uOk7o7Zhg-106DMBHLZbrtGCnD9p4wK-NfaGLiArg8tCCmWeD187U8cHIdoWZmYK_HDWyhJeT_2NCgWlakdWR9IWnKJxAsupnLr4zWEN9iqzwRAq1xWumjE30dYyKXL2qGDMnq4AddleV9fUWL3FT2Bk5Z82RRbUyJg3TZcctwBTQx8jHplYeg6D-RKKZcrPzLdLUZndZUsL2r8V_iWVNNm6iAj528aggpOr_A6ok6D_W9FXafxv79Xm8D9Y7dI2pw9pGJPEDvE5z_Y53P_fXWYawPZ9bOelbHmj_N-FAZhOvQiVjruHi-DnbtakpZWk4hiw011InxE1-RknibJ1e_rzva5NDa37ythKqJosvcQtJwnmqaYodRwkNsDVwmxI0p73UTrONika4PeoAWhYkLniVxxRY6Mxd8sJ63a0dLHdyF2KWQKhLTY3UnYQZXMJSs5TyzvwoXtUXX_UIX-Wrn_3D5HChZryF4dhB2GaDveR20YLyOc1qJi11TOeZLSR3Xe-8H025xg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=fvPMMF94WBd1njDNhuG3VaD2Nb29Y3BXmr6wMAh5-KepwaiPtowNiuVqtGsvxJfdnPWJ_oIrGFIsF3oI4HZst2b19u4c0K4A4dyyNc2lS-eJ_2x1zIJQHr8BOk8Z38EZQ_5iDyO-qFUJtpYDOvR6UMdPTMDfeG5uOk7o7Zhg-106DMBHLZbrtGCnD9p4wK-NfaGLiArg8tCCmWeD187U8cHIdoWZmYK_HDWyhJeT_2NCgWlakdWR9IWnKJxAsupnLr4zWEN9iqzwRAq1xWumjE30dYyKXL2qGDMnq4AddleV9fUWL3FT2Bk5Z82RRbUyJg3TZcctwBTQx8jHplYeg6D-RKKZcrPzLdLUZndZUsL2r8V_iWVNNm6iAj528aggpOr_A6ok6D_W9FXafxv79Xm8D9Y7dI2pw9pGJPEDvE5z_Y53P_fXWYawPZ9bOelbHmj_N-FAZhOvQiVjruHi-DnbtakpZWk4hiw011InxE1-RknibJ1e_rzva5NDa37ythKqJosvcQtJwnmqaYodRwkNsDVwmxI0p73UTrONika4PeoAWhYkLniVxxRY6Mxd8sJ63a0dLHdyF2KWQKhLTY3UnYQZXMJSs5TyzvwoXtUXX_UIX-Wrn_3D5HChZryF4dhB2GaDveR20YLyOc1qJi11TOeZLSR3Xe-8H025xg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار رو به جلو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83901" target="_blank">📅 22:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH5r6vDl3TprJ2z_DmkLZmVTfWHyuDfyzrmRON5HxezLPmi_cV8boeyE8Z36SjkTHM6DqhhCWJA7LgwUACMB7n4nV0EeQbs0U4UMjHzrnqTi5j-FzsYvW9_SFIJiN6T6SB5AM0NUiUveZs46XriA1WTlqjLpyRU6l8ZgF7jYEDY6UwjWiEGuZ9tkSH_Qz5EDurmrOsaJpUr0xoxRyOQ4jdedWXjufEYRyqYjkU84X1JKeqIz49VD5W9EBaSQ3thHKyew1gACyIOjS0DsT2aVBjQ_qbWD3oItp6WqsixGumambFKQxaW5be30q7BKCyBru50YvOH9G5x-iiznKgNiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی چیه این؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83900" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: کسایی که میگفتن "۱۲ سال دیگه بخاطر گرمایش جهانی میمیریم" الان میگن "هوش قراره مارو به کشتن بده"، در کل به این کصشرا گوش نکنید، هوش مصنوعی خیلی ام چیز خوبیه و قرار نیست بشریت رو به گا بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83899" target="_blank">📅 21:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83898" target="_blank">📅 19:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83897">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=dB0KxJMy-DykrfikhHtb5xGSm7McaMKdOf5NzjuhFjRyLzye5InW-8_02i6tY0zGLxovmwDrHYpCDYz6cdxDkx2c6jt8ATgbWiUJ1QRyc4VAtVfVXb7o4y6S3CRPE4ShD5rnehzfkVAtASvNOLrbQPZGotBlBqhtBHYiiVvhufv4YhYazDHDZxt3hAD187MqT19aMRL0UgveHP08tur2KJLsuLfsx1yrFTjtXZmRlPWRAB_ZHzg320AlPB9GGwO6T6zgSpV56miuBG895nz4QPNzdzV1fMLZQgESPya4dtoGpmh53qtElMpbfFBuiGaogFJHJNO9fLG7Cov8MMAbcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=dB0KxJMy-DykrfikhHtb5xGSm7McaMKdOf5NzjuhFjRyLzye5InW-8_02i6tY0zGLxovmwDrHYpCDYz6cdxDkx2c6jt8ATgbWiUJ1QRyc4VAtVfVXb7o4y6S3CRPE4ShD5rnehzfkVAtASvNOLrbQPZGotBlBqhtBHYiiVvhufv4YhYazDHDZxt3hAD187MqT19aMRL0UgveHP08tur2KJLsuLfsx1yrFTjtXZmRlPWRAB_ZHzg320AlPB9GGwO6T6zgSpV56miuBG895nz4QPNzdzV1fMLZQgESPya4dtoGpmh53qtElMpbfFBuiGaogFJHJNO9fLG7Cov8MMAbcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حس میکنم بعد قطع شدن ویدیو کامران و هومن به شاهین نجفی پیشنهاد تریسام دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83897" target="_blank">📅 19:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=AV1uuZ0tF3w3dSSZkHjHB5FHpNmpEmWinw37HX0-A_yF3Gt9GK-C6x20xHnbYTn5CK3us4rjuZ7Pe07DdVMc4tUIADd-hO5qk6bXf76rKhihD2GWW39mI5ON3COb3K1B2Y2v1pT0h2xfvDFdgjjABV-5WaHKcs4AnkfLbs3_6TK-xba2_COjDUy2X2lTpAe4OcZQRW0m-1ZjylEAUUNbU8UqEf7HIo3yLG390cTxQhuF9NTPtctutimJWgJgfkH4j7HAnkJqCsVDz_lBi8AcFhhIQ4xNZJ2CzriqAxd6jv7NhtLYI6wfwhMcp2S4FcLQiatLsu1RaKMES_V9iPNLNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=AV1uuZ0tF3w3dSSZkHjHB5FHpNmpEmWinw37HX0-A_yF3Gt9GK-C6x20xHnbYTn5CK3us4rjuZ7Pe07DdVMc4tUIADd-hO5qk6bXf76rKhihD2GWW39mI5ON3COb3K1B2Y2v1pT0h2xfvDFdgjjABV-5WaHKcs4AnkfLbs3_6TK-xba2_COjDUy2X2lTpAe4OcZQRW0m-1ZjylEAUUNbU8UqEf7HIo3yLG390cTxQhuF9NTPtctutimJWgJgfkH4j7HAnkJqCsVDz_lBi8AcFhhIQ4xNZJ2CzriqAxd6jv7NhtLYI6wfwhMcp2S4FcLQiatLsu1RaKMES_V9iPNLNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بین دخترای دبستانی:
میدونید من اسمم رئیس جمهوره؟!
دخترا: ببببلهههه
مسعود: میدونید پدرم کارمند بوده؟!
دخترا: ببببلهههه
مسعود: آفرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83896" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکبار امتحان کافیست
👆
👾
🙂‍↔️</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83895" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCSa-2AaWraNWSreuwZakBOzjIvyOsv1Y-LpDJAX-wknTkgYutTKDjtOpVNyDvrUOMtzxSstH13ifeckrsrhZiAFPqLob6_Hx-4FyngiqsYYwuC0zOtRo2wdj-hiKpeqkcCa_hrh_pEf3aQu9jXUULaORQ_iz3mJW9VaAu-IcptQa-wdbw35ROCnifctF0mZLgt6T7GZvvNPfcknHgkF763xpxaWfURTLHGFhvEic5HoLZ0efsLLlC4wpPtmoKDzOWiirc26_-4x3wLXS6B5BB8diDpb_l1xKFgylF9TZf0tRkIfUZC7uAbMJdEEQRKb16tksivHbDzVO7VRpaGo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83893" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFqnG-GoQjNX02VRamRbkeaa-CdHVCIU6lFiTaYXyf9ip1N97HRKBDzxycO3ajBrzsGEKr2-UfaovllB5w6hgSs1dNC1cGNl1coxziuB-q0mgS-R_TizFdn0GMpyTITIGLdwmVt1H76TxnZ591yvflUI6WBb_Qb-Xbkzesb4U7n6R4HQ_VeCdJq-UocYB_nYL8KXxe5O5LmmoV7XMmUygG3UvEneEzrkVQHfJUHqtYJNrBRDJfTvMZ7xf8ynPHxtSckKlkpRcCL8Wq63t95uWWjAsuSEhSJA14_cOivDByWHEKTsTHuI3382EKeqCx5ksAudUKVhd_M3t1oRFuiW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=su1E3j3CtX0t45__RwXDABIC3FMhWQ5MC3TyIh9pe2NtAPG-uND5VKaojNgs03jfvF6gGrTtUMr02_511KQ6yQOB6Uo3kkSusLq-h4L63BQfuxaBcaJuP4wZ3xPj4LS5nqTwFrHK5Ro7v03bhUtHLkJGc_8BdmNvyQEdqB9uBWeOoSUW4th1bKYXikDGmlOZvlubaiT16-LLPOz60mpYlsr17e4fa5VMrp1pAxGg3CKLhSk1mum7PieaTWdnL_SGS9jxpppvAnEnBWl7wtFNIKAyzpgcjpum0dlSvyzLmeUJlETAEFkzDjZjrKQJN6aqp9Oe87ks0N5UZDF4mJBgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=su1E3j3CtX0t45__RwXDABIC3FMhWQ5MC3TyIh9pe2NtAPG-uND5VKaojNgs03jfvF6gGrTtUMr02_511KQ6yQOB6Uo3kkSusLq-h4L63BQfuxaBcaJuP4wZ3xPj4LS5nqTwFrHK5Ro7v03bhUtHLkJGc_8BdmNvyQEdqB9uBWeOoSUW4th1bKYXikDGmlOZvlubaiT16-LLPOz60mpYlsr17e4fa5VMrp1pAxGg3CKLhSk1mum7PieaTWdnL_SGS9jxpppvAnEnBWl7wtFNIKAyzpgcjpum0dlSvyzLmeUJlETAEFkzDjZjrKQJN6aqp9Oe87ks0N5UZDF4mJBgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشکان کاگان یه ویدیو از حضور ابوطالب و رپ کردنش تو استودیوی کاگان منتشر کرده که به شدت طبیعی به نظر می‌رسه ولی خود ابوطالب اصرار داره که هوش مصنوعیه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83891" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منابع داخلی میگن مجتبی خامنه‌ای اجازه دیدار پزشکیان با دونالد ترامپ رو صادر نکرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83890" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0bokyz8CsSqL00-79AX4tw09E2_cD0Nl_w2vv_nUB6iG5pXIpIYW26uuYRptbiQicBxttW6HXzF3N_vc_P9K_peAgapJtthIiiQ8XHprRxVo0DmRKDpBUR6kVztFMuamalWY3MJLvGT4X3fnBga5Lj7qYvn55N0VRda_D9nRp4ZZIBNpLUlnGeo_CjoP3f5TYig6c1LmDdB6tUnKgZ7L29L1ukpp10Vz0LtO2Pt8UtIc1aIgDHhLqlo6Tc19dqaExSZgkfLseAdmMXUdr2a2it2fsDi71WbRHg-DzN481UgZmGWQHcQ2hObZIWLkhwpDWW5o3u2tCblGnSM5ANIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کپشن دیگه‌ای این زیر بنویسم میان منو می‌برن پس سلام
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83889" target="_blank">📅 17:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2zJ0v25R7IVVA-PScSOzxmfXRmICoMrAUGkTwHcxiLJn_nujnu1Bc7mLXG-zb0OOO-gA-4qRqoa7LDAnptGvPpz9awKpqsknB_dwPzFG_s9xq3WkCkhHYBaM9YhfMtHaF5eCm1mnTTZ6rAl8bgNXz3JLnWjYh-jNrcOLBdFJVcHzfPNYveEpidPUxnsfwSwdNDtNt55FzAYCbB-_zg5kUXxP58ozf--u02VdXYiDYT4mnQWGCE6yKLST4si11aKPsms07F_QeqvMKSoXhfQWG2jXUaNl4kfFmmaMmRDKCp53yXpNI04xLLtIcFBU67NDV8xC3GIGIVnjiV0ivaMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بازیکن فلیک بود میرفت نیمکت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83888" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABqiDnvLuJXZcuEXk7uFOLL3Hz2Ajr_Eju6ZWDCClNy_Ufd6-0uiISZ6Km_BiGEkmFEJykL-62-iZtwIV7fwhNZ9PdWsjPMB7YfGnE_iqCRD6RwcZrAQFb00gu6wJbbCGltLnw1zleDzqYgjCCxFoaX08f68CRAlDe13mdKZM5UtZ3Sp0xv3FaUm2jt8Yu2nhyfEn0vMtzmg3akrOfe4spZVWQU2wO5rm0z5Wtv8pg0zH2u4oF3uOSJhqKvqFUNmtZmj-vBxG-wKdy4LxTZ5KcaR9zaiyToWMIaEUJoy1KJ1L1DhnlEoDie6vJyhtMGqBUmtS8O422BxVjMML6wRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83887" target="_blank">📅 16:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=r-ZldeYMzIiNYuI2QDOE74Vlsxn65yBuRTCinb_sHnVRpurFXIUGMkKd9xZfQhXworxwCMa-_cba81_VKeWuv9cGkrP5rr6JPQMm0yseKsXtjZ4Nt21TBh5EAdDlv63QPDxJIzVS4YK5IW0N_5-KluOyjSm5j0FjoZIuD7qymdShB5335lkL8Lz5RT9vH-FlXp0LbWnAvmZ-LXUhzZvwW7fGBfCA41cuE-2EbjGnupzGBZZS5mfIwpDSaAHXJrNKZJ-IrOsCMWhKIIngFML0_XntzkK_wl3cj23B4esm0MrFWX0iAE1sgtC3xuWoTiIAiuNOkRvqOR-k4RCvP60sVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=r-ZldeYMzIiNYuI2QDOE74Vlsxn65yBuRTCinb_sHnVRpurFXIUGMkKd9xZfQhXworxwCMa-_cba81_VKeWuv9cGkrP5rr6JPQMm0yseKsXtjZ4Nt21TBh5EAdDlv63QPDxJIzVS4YK5IW0N_5-KluOyjSm5j0FjoZIuD7qymdShB5335lkL8Lz5RT9vH-FlXp0LbWnAvmZ-LXUhzZvwW7fGBfCA41cuE-2EbjGnupzGBZZS5mfIwpDSaAHXJrNKZJ-IrOsCMWhKIIngFML0_XntzkK_wl3cj23B4esm0MrFWX0iAE1sgtC3xuWoTiIAiuNOkRvqOR-k4RCvP60sVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی سطح طنز مرجع تقلید هامون»»»»»»»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83886" target="_blank">📅 15:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آقا کامران یک نسل چهار</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83885" target="_blank">📅 15:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آقا شما بد جلویید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83884" target="_blank">📅 15:03 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
