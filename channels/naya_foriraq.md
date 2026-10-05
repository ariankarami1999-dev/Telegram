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
<img src="https://cdn4.telesco.pe/file/pY1c3vwG2wyE7Vch64owomQdHqsyrmrvhw_D7WUPt0OJvgyztPDYUaWNz94it0oMxYAxWyArVvz6DUmZaF6lgz75ajTi3g4MwcGUgELi92MhiUp-CRhVvWHddHD9LmT5uQDidbrETJBZmuqho9JvZTYMqsi67zQxxNGOsYaPZAXCPMi0va5HQBnZoB6Gkp9gh5b97CR4InAkGfcxN6UuCgDfnFUeUTWPcxrl4Qh9SlErcOz4O5rDeK69CuBAvfuwn91oodZFurdYmBSYt99D7v1wk9U63aBadSdZ0sT41PL1nLkO_VR_hnknSAKosHtBSR9FO5sA9q6NSXHVaqoxJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-92627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3J9P144Jz_cj_7tsILDXSxvE3GWUy1umBiUP2uWKTBO1zSpg6AKnBAbzgt7d7xY6ZEuwJeZWVf7DPKyKChaOjmLAxFZm86-mA9RBxm0FwSKbTeGoo3DdFbL2K97yWG3lg07ksH0nte4kYWfZhBYpY6z9olcf1Z5R1OCYbZ76R73csaPft9SmXomrEPPhdXyKC52Znw1CxeIc86J63VHU-SdgCM2vhOT02J2xuDscbSP7nhD-tLX3bxO4HKU7eBE6W_7pK2gTFnhI3x-Iqc8aoeC5rJE9jeELwdcaALPA5dlDzm_J-HgfPzUD4w0s_KYthAIBXCJGBWOMn-1sav6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
وزارة الدفاع السعودية: اجتماع حلف مكة يؤكد تفعيل الردع الجماعي ضد هجمات اليمنية وضد كل من يقف وراءها.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/naya_foriraq/92627" target="_blank">📅 21:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇸🇦
وزارة الدفاع السعودية: اجتماع حلف مكة يؤكد تفعيل الردع الجماعي ضد هجمات اليمنية وضد كل من يقف وراءها.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/naya_foriraq/92626" target="_blank">📅 21:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇸🇦
وزارة الدفاع السعودية:
اجتماع حلف مكة يؤكد تفعيل الردع الجماعي ضد هجمات اليمنية وضد كل من يقف وراءها.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/naya_foriraq/92625" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ_bQADMihBNFhLV-qy0mrUlj9Hn8U8UjuaDzrcQWjfez2N8S-yQtTf9sEOf5BIuFFUXjkIalMIKkTEVWUvg-7wovirc6giEWCtUUGktEq9NcEjSHcM7PyZzIxnHm01F30ABKO9kVRxSUbaQr2NUrSOVS7FRz3KnWwRk2bbjRJMXZ6a-gI7CTgW1C1bGnFUnunS-KYcgc3DNwquWnXcQL7HobWwDhtQpeTtPpZ8fPExZtw9ImF6Zru_HnNSGAaUlAmRo0mOcx5XZI55xdQ_K265fbpS2aaTuMOyC2Tu25hHnCu63jZWGEBRMoYIUM9H30kIH1TXiospiyLIhsaoXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هجوم صاروخي يطال ناقلة نفط في مضيق هرمز، والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/92624" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
أنباء أولية عن تعرض في محافظة كركوك على اللواء التاسع بالشرطة الاتحادية بمنطقة تقاطع الدناديش.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/92623" target="_blank">📅 21:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a67504163.mp4?token=rLYqZR-igvx24YLromZw8oNb_MbbWjS0gw9sIAUZ9iaZ3pumSJRuKH2PHcZjezajc43helIk4YRJTS7DtkkEG8pfQvuRg_WTa9zzwRj8-tfM6B-xrR_0ygoT71uFoO3J_icZXOYDIEncg9kfStCSOJhHERukiuuFFcuMZEJrv85sE83TiroUhwuR94b9VGDwQ0hUU4363Xc2CJkZZ6nPbVctC7vVMiA9weGW7yp4n3my_3gcNvRjJbuZfjlPCG6H3K1bPq8MKlY5FGNxN5WLGKxBtZZ4tGRJ8sL60Zb2kEMrQvnH6vAhU-cj7Q1d-COZRIse71t2cf7uS9oq5llEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a67504163.mp4?token=rLYqZR-igvx24YLromZw8oNb_MbbWjS0gw9sIAUZ9iaZ3pumSJRuKH2PHcZjezajc43helIk4YRJTS7DtkkEG8pfQvuRg_WTa9zzwRj8-tfM6B-xrR_0ygoT71uFoO3J_icZXOYDIEncg9kfStCSOJhHERukiuuFFcuMZEJrv85sE83TiroUhwuR94b9VGDwQ0hUU4363Xc2CJkZZ6nPbVctC7vVMiA9weGW7yp4n3my_3gcNvRjJbuZfjlPCG6H3K1bPq8MKlY5FGNxN5WLGKxBtZZ4tGRJ8sL60Zb2kEMrQvnH6vAhU-cj7Q1d-COZRIse71t2cf7uS9oq5llEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمنية من مدينة ذوباب تكذب روايات السعودية.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/92622" target="_blank">📅 21:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
أنباء أولية عن تعرض في محافظة كركوك على اللواء التاسع بالشرطة الاتحادية بمنطقة تقاطع الدناديش.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/92621" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">السفارة الامريكية تحذر : ‏المملكة العربية السعودية: نظراً للوضع الأمني ​​الراهن في المملكة العربية السعودية واحتمالية وقوع هجمات جوية بطائرات مسيرة أو صواريخ عليها، تحثّ البعثة الأمريكية جميع المواطنين الأمريكيين بشدة على توخي الحذر واتباع إرشادات التنبيهات الوطنية الصادرة عن الدفاع المدني السعودي. للمزيد، تفضلوا بزيارة</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/92620" target="_blank">📅 20:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sKXUmN_M3x8si622Ue4fz-oPeh10Ue-11iKI0mujFBktzmnWGbiIverh2xCqNKkD9XDrGgDgdYYuJEnmDmlJL0zXmUjLWGRljuN8e1oWOKx5IJijhfYVOKQR6_3MaDkuo_aWXOGRrWlgJ7PZDDad68UhGxP3BOvcfJJhLEen0KIplgc0yag2py6QQ9UJTwEs0QjTOEBub_c8L5pEUysRAbR01g0A1UeWgqoRwFgYmn112xbMMVH60OK5nMA44Gy_m3nqW_rfsyzxjV_Btlb-9NOOyrK2MXou95ss1mMPqQwyf5ysMDwqJxmi5gIu8ktCDAbbB_XWmAKI1olqbgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
حزام الاسد:
لا يوجد في باب المندب وذوباب والمخا إلا رجال القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92619" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aab362af.mp4?token=ZXp8H3co9-Lpd6UlXQU4PMWspTVatRH11pKV9ffnn1gd0Z2TcFhKz4qYDDGvbOHckpVDtxl2JiVI4gGO_8kOyDO-7LM-uu9BhQ3UuBibIC8TD3n-qDOQqidLL1qeZDfkFUcHlSdvr56NfIbDqZLjMp6tWTE6uRLxb3lY7oe-KHRcNe5yNU3P7GuvfmD91IiRvxDcE-9RGWHMxfTkXdFbguPL_lAdk_sbNoKCNjP9QVUC9VE-6VOmFzTaTuGcqlt3NZE7YJUzUw2lgRPdjwLEIRbYh-DU2-_yUCa4KohhcVh097tYmSXZJmajXBIbbEgxi-XssPFRi2UkDCtYUZFkihw1xXsg9W-haXWgFr741c_fUvn4Q8k47K8GaUNCKifSsRxM6bu5d4SQCRG9uTSm3hllwWK05fOwfPxxBuWr4DUzT1Q64nnx-_SZYhhiMSRx9ikB4HLJS7zv1CId1MAH6_ovFeVt6OfXDi2xq9wV8YuNAblfW3SR1x-heUFbafneeMdusTJI43zgf2ryN6AOXoFGsZc1zSyDXBoJV_22hkBLMgS-fe7U4BhCkQjWkJTS3yIOqjxNiKPy-RJO5vllzJfSIKMN9w0VICZrZIEVubgZtGWOLu4-lEj7DbfNSEX0oOeV5lzsYYvHP9734jFmRbMWosGd_vD_X0khqKKh7sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aab362af.mp4?token=ZXp8H3co9-Lpd6UlXQU4PMWspTVatRH11pKV9ffnn1gd0Z2TcFhKz4qYDDGvbOHckpVDtxl2JiVI4gGO_8kOyDO-7LM-uu9BhQ3UuBibIC8TD3n-qDOQqidLL1qeZDfkFUcHlSdvr56NfIbDqZLjMp6tWTE6uRLxb3lY7oe-KHRcNe5yNU3P7GuvfmD91IiRvxDcE-9RGWHMxfTkXdFbguPL_lAdk_sbNoKCNjP9QVUC9VE-6VOmFzTaTuGcqlt3NZE7YJUzUw2lgRPdjwLEIRbYh-DU2-_yUCa4KohhcVh097tYmSXZJmajXBIbbEgxi-XssPFRi2UkDCtYUZFkihw1xXsg9W-haXWgFr741c_fUvn4Q8k47K8GaUNCKifSsRxM6bu5d4SQCRG9uTSm3hllwWK05fOwfPxxBuWr4DUzT1Q64nnx-_SZYhhiMSRx9ikB4HLJS7zv1CId1MAH6_ovFeVt6OfXDi2xq9wV8YuNAblfW3SR1x-heUFbafneeMdusTJI43zgf2ryN6AOXoFGsZc1zSyDXBoJV_22hkBLMgS-fe7U4BhCkQjWkJTS3yIOqjxNiKPy-RJO5vllzJfSIKMN9w0VICZrZIEVubgZtGWOLu4-lEj7DbfNSEX0oOeV5lzsYYvHP9734jFmRbMWosGd_vD_X0khqKKh7sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمنية من مدينة ذوباب تكذب روايات السعودية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/92618" target="_blank">📅 20:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
مشاهد أولية من وصول القوات المسلحة اليمنية إلى منزل الغوي الخائن للوطن رشاد العليمي - 05 أكتوبر 2026م.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92617" target="_blank">📅 20:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اصوات انفجارات في الرياض</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92616" target="_blank">📅 20:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92615" target="_blank">📅 20:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اصوات انفجارات في الرياض</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92614" target="_blank">📅 20:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10dfda8f58.mp4?token=EhMu_7z5lnPkJxaicrpMbh3Ek-6hZnrcF-MGKlc_LVgkv23PIstU1g8ua8gKxSaQuG6_zkLVQmuB-8o7pDO5appYe6cwGKPErACeaVhQzFIRhLsz7EFA2MrBMNdRo5X8pLzo2zKTpsPU6CT4uM6eXBVnrO2ag2jD28-XJCP-FCVBiF3PYfq89ccutMVy1oVROUNsO0vNUJSlETwUDTO5f7sL6m_POj8O_4GuCVLWEIq_nlO9-kh3VK2m7kOE0eLS5_QxvbuZKzb0lfPv0JgWW97VWWVSUfnPZnIgOTEGHRW4HNgauFxMva8JJhA_He0BZfEWHiJuMhCe676p4iEqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10dfda8f58.mp4?token=EhMu_7z5lnPkJxaicrpMbh3Ek-6hZnrcF-MGKlc_LVgkv23PIstU1g8ua8gKxSaQuG6_zkLVQmuB-8o7pDO5appYe6cwGKPErACeaVhQzFIRhLsz7EFA2MrBMNdRo5X8pLzo2zKTpsPU6CT4uM6eXBVnrO2ag2jD28-XJCP-FCVBiF3PYfq89ccutMVy1oVROUNsO0vNUJSlETwUDTO5f7sL6m_POj8O_4GuCVLWEIq_nlO9-kh3VK2m7kOE0eLS5_QxvbuZKzb0lfPv0JgWW97VWWVSUfnPZnIgOTEGHRW4HNgauFxMva8JJhA_He0BZfEWHiJuMhCe676p4iEqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الاعلام الاجنبي يتداول فيديو لاشتعال غرفة القيادة بسفينة شحن في مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/92613" target="_blank">📅 20:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-b9DP1NNpkhzr7zMu63GDmhHgjwdCgk2B-z90D3kBQ9mImj_3Of87DDjfwn2fOdTluyKJtDKKp6LWt2OQ0z0c9s0DEk2M8hK0N149f3EdGTgejneFWP7JE8NBRgBPXWF6TrTkoFGGGj9ywRX4zhM8EkgGizG5YGHk5_upXoSl-FLfLNYfJ_nZLMhUhLmO_Ya64EuufoSw197Macn-loVZHMYjGznZ2AuLKLUexaMsEWHRUud0E4Avci7c-wAMOfTSoz088EeWT_7YSuh6SzvQoDvFGD6Isa9-cU6P-1llSRBdr3wsALrjNd4pjF3bdyoYoA_dbcgK6CQVsMwbc93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
‏لم يعد مضيق هرمز هو ما يرفع أسعار البنزين، لأن أعداداً قياسية من البراميل تُصدّر منه الآن بشكل شبه يومي، بل كلمة "مصافي التكرير"، حيث تُفجّر أوكرانيا مصافي التكرير الروسية، وتُغلق مصافينا في الولايات الديمقراطية، مثل كاليفورنيا، على يد الديمقراطيين. الرئيس دونالد جيه. ترامب.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92612" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c814447da4.mp4?token=PbVQN5ImBdRehdDgiKWcdbmrP9Ic-94CIi8vBIpnGPkCdmIag3ZGs7X64UVb_ihbZluZmJoHxq31PvdIvRQvRk91XauuUNKEG-czcZXvsn3TGaCwyf1251AX6WB081uv3OQliMnivEaYPiGX_DPeV9Ga7_Qcm-lMqVf27u7B2z2xMXLgUNFW_AUArZV2w9wveFAvMszTAchyqRZ1NbfGsyug5eouxAiaDtF3ue2EXkGpcsAySHO0Qt6mTR1_VYyVwXZqJoMLWMfyetsXOYywYTXnf8lWMzboTfj2dlFjVk-HuA_weYVVuxEDO1BJ6PKvnboleeRDqlbJ8BjDyo_3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c814447da4.mp4?token=PbVQN5ImBdRehdDgiKWcdbmrP9Ic-94CIi8vBIpnGPkCdmIag3ZGs7X64UVb_ihbZluZmJoHxq31PvdIvRQvRk91XauuUNKEG-czcZXvsn3TGaCwyf1251AX6WB081uv3OQliMnivEaYPiGX_DPeV9Ga7_Qcm-lMqVf27u7B2z2xMXLgUNFW_AUArZV2w9wveFAvMszTAchyqRZ1NbfGsyug5eouxAiaDtF3ue2EXkGpcsAySHO0Qt6mTR1_VYyVwXZqJoMLWMfyetsXOYywYTXnf8lWMzboTfj2dlFjVk-HuA_weYVVuxEDO1BJ6PKvnboleeRDqlbJ8BjDyo_3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
استمرار الانفجارات في عدن وعدة مسيرات تسقط بشكل مباشر على اهدافها.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92611" target="_blank">📅 19:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق:
5 فصائل وافقت على تسليم السلاح وقد سلمت 3 منها بالفعل أسلحتها والحوار مستمر مع الآخرين.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/92610" target="_blank">📅 19:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd280b6adf.mp4?token=d_0t4NYPSAnniRzKtOO63U2VhKJQU9mh-TOiKJaOKArggx_CvQIhTBylxqOCg-bKxATLNrSNidwFhy8ROKG8FhnuiW0UePKfcjXUvhJ1SgqC3DpmjK2hcu-8aTx8yo4KRUzrQKXK9eN-mpBuMMigXtfW-QaomNhEWdQ5wrkAuoRATqpY9L7zBVGGQk3li2kEA13KslfvutLYnf6dD7dModLaVpIVhozVIsnHcrQ30X8v-9l8cUS93IJHQ6nbb-LVncJYqJHdEwduB064mUfopXOHY489qhVoyGlIM8wSGDOYsTY1L8RGTUcrLkZqDSTHP_78i7U1SE-di3ezdILXMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd280b6adf.mp4?token=d_0t4NYPSAnniRzKtOO63U2VhKJQU9mh-TOiKJaOKArggx_CvQIhTBylxqOCg-bKxATLNrSNidwFhy8ROKG8FhnuiW0UePKfcjXUvhJ1SgqC3DpmjK2hcu-8aTx8yo4KRUzrQKXK9eN-mpBuMMigXtfW-QaomNhEWdQ5wrkAuoRATqpY9L7zBVGGQk3li2kEA13KslfvutLYnf6dD7dModLaVpIVhozVIsnHcrQ30X8v-9l8cUS93IJHQ6nbb-LVncJYqJHdEwduB064mUfopXOHY489qhVoyGlIM8wSGDOYsTY1L8RGTUcrLkZqDSTHP_78i7U1SE-di3ezdILXMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصوات انفجارات قوية في عدن</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92609" target="_blank">📅 19:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
سرب طائرات المسيرة تناور في اجواء محافظة عدن لتسقط على اهدافها.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92608" target="_blank">📅 19:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/92607" target="_blank">📅 19:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd36aa0b1.mp4?token=vNVtBvHP6fjTS8UelOqvDvlT6oB9DSehTPxE3SI9W42JXizTqp4w2Q61TCr-Ki_Il31WI858BHAIjzyxa4MHr4BpBrn9XDCLqVrVLc6bpachRAPEorATQwfrnuumbFP8aeft41u3Lj-1u0i69UiekEaFXBLBfPtVqyidrL_5jgWHKOZKvAi_jr_Xu-9kjjqjXmjp7AMdIXMBiXE22ADQZHqBWwSe5P1tfRC_0Sh-8IvySNDws0NxomQgi0YIj1MTPDUL3EdvdJm1sWaiQREl_hd7VbDZRvKQ5kI5SrzcOKaMitWkJUU3tpGOClkpT3VytjU7RPnRw0WcBDVtjUB42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd36aa0b1.mp4?token=vNVtBvHP6fjTS8UelOqvDvlT6oB9DSehTPxE3SI9W42JXizTqp4w2Q61TCr-Ki_Il31WI858BHAIjzyxa4MHr4BpBrn9XDCLqVrVLc6bpachRAPEorATQwfrnuumbFP8aeft41u3Lj-1u0i69UiekEaFXBLBfPtVqyidrL_5jgWHKOZKvAi_jr_Xu-9kjjqjXmjp7AMdIXMBiXE22ADQZHqBWwSe5P1tfRC_0Sh-8IvySNDws0NxomQgi0YIj1MTPDUL3EdvdJm1sWaiQREl_hd7VbDZRvKQ5kI5SrzcOKaMitWkJUU3tpGOClkpT3VytjU7RPnRw0WcBDVtjUB42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
اشتباكات جوية في محافظة عدن التابعة مؤقتا للمليشيات الموالية للسعودية اثر دخول سرب من طائرات المسيرة الاجواء المحافظة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/92606" target="_blank">📅 19:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812d57e9c.mp4?token=Bp0mPC2qCLlz3Ay4EtcHzhjz7qK1mxzopQgyx1ZlidZMNyABCsVeD4Ejgh9LiJaHPcFx2-LmNai-tjAV_7KGdcHAc6f92DUaCeq2Loijd19wNz1iuHONEwSYHCSRhg5eWSCrjjGN628AXKcm0Uwm4KI2X07wRNPGudwMC5x3UYd1CkGuwRcEd_DOOsf8pq9lERMM8h12Uc2liYSsr7y85A92EYZ_6H1lNdg-6wZh0UAScf4VitfrIU07Ibzll1rH-nwIBiLd4hNFcHRknATrrJ9ggkE1NLiWQAfaUD_gA1_G4I5L4FJh5DYVL3PIe8EcSrmp9pEHr8y96aJeaKDwbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812d57e9c.mp4?token=Bp0mPC2qCLlz3Ay4EtcHzhjz7qK1mxzopQgyx1ZlidZMNyABCsVeD4Ejgh9LiJaHPcFx2-LmNai-tjAV_7KGdcHAc6f92DUaCeq2Loijd19wNz1iuHONEwSYHCSRhg5eWSCrjjGN628AXKcm0Uwm4KI2X07wRNPGudwMC5x3UYd1CkGuwRcEd_DOOsf8pq9lERMM8h12Uc2liYSsr7y85A92EYZ_6H1lNdg-6wZh0UAScf4VitfrIU07Ibzll1rH-nwIBiLd4hNFcHRknATrrJ9ggkE1NLiWQAfaUD_gA1_G4I5L4FJh5DYVL3PIe8EcSrmp9pEHr8y96aJeaKDwbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
اشتباكات جوية في محافظة عدن التابعة مؤقتا للمليشيات الموالية للسعودية اثر دخول سرب من طائرات المسيرة الاجواء المحافظة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92605" target="_blank">📅 19:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇱
🇮🇶
الاعلام العبري:
منحت امريكا إسرائيل الضوء الأخضر ورفعت القيود التشغيلية المفروضة على القوات الجوية الإسرائيلية فوق الأجواء العراقية ووفقًا لمصادر فإن هذا التصريح يسمح لإسرائيل بمهاجمة فصائل المقاومة في المنطقة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/92604" target="_blank">📅 19:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUtDgRJ0NfJks2pYAe2l9pxNeYv7sDqSusW2KYfRq-uYZODeDSqyggfJLAX22A7THpbWep5Ks5HqchWjQ-RAXCxnPJR8GRahc0BnmBCbK4REK2U6cNpJEnzl1VPveWKnwoKUqjACcEfjK8-4GkRXrRgPtry_KGHl_gT1Jx-YsHWANmbZbNXFjDYCVxNWzICGWfnOo4ZB8Srigwnp2Bd4FRK0kUIpZ6_LsZcJl-SgnR4cNEcpEnxxMdcuELu9MimTbcSbQT9311_A7OP4rVa_di8IQaVM0TN644mY1X1LBnOZftGB_rFssCEh-vAZ-RrUtqnVEMHY6IRU1ttY8k7V7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEM8HnWaej9TgrOQ54KhMYSAbv-VMA6n4tBrMb5L4dxBwNy_RBknq8wPoCcNcj7ZHw6xu2HWMo4B-5lVG7iOUIM8QERPd07i73iS4yUojRPSUz73GgOkh89nLboV-pBhuMUlyRFnc06czQSTUlJjuewiYhjS4Cm1BQsJU3dJBvcevrVp4G-HTzid8Pc3WJQbznhmKS8etcSvk9V7GAgEXSgSwy_2waxzfGy0LjrZFcVMqfc6eEy_4ng9nSSJIr57DX9ZSXmIIa-ETSrtLEWybLqGLeclOF6fd2nrzgyfuGnapR-JKzPZdUA1YDD8Ktmkyh2zzybsiIsLFO3BR1Ha8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من الاقمار الاصناعية رصدت حرائق واسعة في شركة البترول المطلة على البحر الاحمر بالسعودية بعد الرد اليمني الاخير.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/92602" target="_blank">📅 18:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇦
الاعلام القطري:
القوات الأمريكية ليست منخرطة في الحرب في اليمن وليست لنا أهداف خاصة هناك.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92601" target="_blank">📅 18:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
مشاهد نوعية لعمليات ضرب التحشيدات التابعة للعدو السعودي في عدة جبهات بطائرات شواظ الانقضاضية المحلية - 05 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92600" target="_blank">📅 18:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
من إنفجار العبوة الناسفة التي طالت عجلة تابعة للجيش العراقي في صحراء راوة جنوبي محافظة الموصل؛ حيث أدى ذلك لإستشهاد وإصابة 4 منتسبين من الجيش العراقي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92599" target="_blank">📅 18:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇱
إطلاق صواريخ إعتراضية في سماء إيلات المحتلة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/92598" target="_blank">📅 18:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c70a185ec2.mp4?token=VvHEw8WZzJcftwu3OeJx-EJlrZrYyMbR--b0gpSTg_7i6cosI7-SMuYIlw8QF2rttLj1iu735BSUbn8UJTjEMNnMRzE6F46taXiSCBQGkEkEPxRuLwx4BagAsSMoIiSo2D3BZuL1syQQbqId3_bwjQzrqQUKgf042jkiviM1Gt_VwN1kmrt8KsORLRTiUMPYKy2bsd_cMjnJP9eV8Kstxpfo6q4lmSluak7uHQDLp866t29TZAOdkjxlGDYcYcMEtJYk3gqhrecmILMkOPFGytU7f3e44uVO7djHg5xawQIK3FpsfjzEuUQTRQCxOwOTg3S0HNVr67dDkTpM7haL1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c70a185ec2.mp4?token=VvHEw8WZzJcftwu3OeJx-EJlrZrYyMbR--b0gpSTg_7i6cosI7-SMuYIlw8QF2rttLj1iu735BSUbn8UJTjEMNnMRzE6F46taXiSCBQGkEkEPxRuLwx4BagAsSMoIiSo2D3BZuL1syQQbqId3_bwjQzrqQUKgf042jkiviM1Gt_VwN1kmrt8KsORLRTiUMPYKy2bsd_cMjnJP9eV8Kstxpfo6q4lmSluak7uHQDLp866t29TZAOdkjxlGDYcYcMEtJYk3gqhrecmILMkOPFGytU7f3e44uVO7djHg5xawQIK3FpsfjzEuUQTRQCxOwOTg3S0HNVr67dDkTpM7haL1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
تصاعد أعمدة الدخان في مدينة جدة السعودية عقب الهجوم الصاروخي اليماني على مصافي النفط التابعة لشركة أرامكو.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92597" target="_blank">📅 18:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
بعد قليل.. مشاهد نوعية لعمليات ضرب التحشيدات التابعة للعدو السعودي بطائرات انقضاضية محلية الصنع نوع شواظ تستخدم للمرة الأولى.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/92596" target="_blank">📅 18:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
الهيئة البحرية البريطانية: استهداف ناقلة غاز البترول المسال وناقلة نفط أخرى بمقذوفات مجهولة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92595" target="_blank">📅 18:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyaE-MaIQaH1eJc6UtuisKQGcXtsgIKKVxetHTYjQl5KxZWP23vjqXxTxRGCDzWC_Ep-tGrL6r2jAYsKrpBFWEojwMDwGoe2FSHNVyuaGr52JHOHrkUIH-7_1dvk97C0Cs4aYRFSl81867IOFpSHOiMfkKNKXYKAacwpa1wnc3UIp3Gq9_GEtWFofzxpOMC54PZBVm-GgYCr0-VTj6uvfQcPsrOTryFwdAOxiAzkiIyQMmd2r5HWjmVk2l8N8hmYOBP6lc59hnSv5G8FjMHPNGJ_Ou5ZUTHe6M0We92xEwQdut925ttqNpYPvAnK90Z9vwYCU-8qJxoz5ZEuUOM6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الهيئة البحرية البريطانية:
استهداف ناقلة غاز البترول المسال وناقلة نفط أخرى بمقذوفات مجهولة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92594" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
رويترز:
احتياطي النفط الاستراتيجي الأمريكي ينخفض إلى أدنى مستوياته منذ العام 1982.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92593" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae16afdd70.mp4?token=EDugKuJFkNu_XbSFT0OhbKa9bRd2i5uTwHT5np-i1iULjeKlreab3Z47xrrEJFLk4E2BPJECwxcHfEtwdeiabCNqedlF75DO9OpmM3O0_BneEUOVhxQH7bV5eln_Td0-uS0_pX26_74gJYunt5jC16Y0sA8iTzTRcvqp4wra1__GVMmcoz1mxVdM4aAr0YxDzvd66Ck8y1vqHDwsLwoavIvxoc1EbgswDqRK-CT336OYqaIkJhWETenX-lYWD1p4CJ3AYnnRyIzpebwwKkm9cULDlrkG2NYX5Q57ciCBTHJqe8yVyTpLS46LsDVdqp0nYMj5E_IZZTttmrFPyrn-rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae16afdd70.mp4?token=EDugKuJFkNu_XbSFT0OhbKa9bRd2i5uTwHT5np-i1iULjeKlreab3Z47xrrEJFLk4E2BPJECwxcHfEtwdeiabCNqedlF75DO9OpmM3O0_BneEUOVhxQH7bV5eln_Td0-uS0_pX26_74gJYunt5jC16Y0sA8iTzTRcvqp4wra1__GVMmcoz1mxVdM4aAr0YxDzvd66Ck8y1vqHDwsLwoavIvxoc1EbgswDqRK-CT336OYqaIkJhWETenX-lYWD1p4CJ3AYnnRyIzpebwwKkm9cULDlrkG2NYX5Q57ciCBTHJqe8yVyTpLS46LsDVdqp0nYMj5E_IZZTttmrFPyrn-rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
بدء الرد اليماني.. قصف صاروخي للقوات المسلحة اليمنية على مرتزقة السعودية في باب المندب.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92592" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
🇸🇦
مركز تنسيق العمليات الإنسانية اليمنية:  حرصاً على سلامة الطيران المدني، نحذر شركات الطيران العاملة في أجواء السعودية بأنها غير آمنة مادام العدوان السعودي مستمر على بلدنا.  أجواء السعودية ستكون مسرحا لعمليات قواتنا المسلحة، والجمهورية اليمنية تُخلي مسؤوليتها…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/92591" target="_blank">📅 17:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني لنايا: القوات المسلحة اليمنية تستمر في تقدمها نحو مناطق أخرى في ريف محافظة تعز الجنوبي وسط إنهيارات واسعة لمرتزقة السعودية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92590" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
🇰🇼
🇮🇷
أسوشيتد برس:
يضغط جنود أمريكيون وعائلات الجنود الذين سقطوا في الخدمة على قيادة الجيش للحصول على إجابات حول الهجوم الذي شنته طائرة مسيرة إيرانية في الأول من مارس على ميناء الشعيبة في الكويت، والذي أسفر عن مقتل ستة جنود أمريكيين وإصابة العشرات.
أخبر الجنود أن القادة كانوا قد تلقوا تحذيرات متكررة بأن الميناء عرضة لهجمات الطائرات المسيرة ذات الطيران المنخفض، وأنه يفتقر إلى وسائل دفاع كافية ضد هذه الطائرات.
حث ضباط الاستخبارات القادة على عدم نقل القوات إلى هناك، بينما تم رصد طائرات مسيرة للمراقبة فوق المنشأة في الليلة التي سبقت الهجوم.
على الرغم من هذه التحذيرات، تم إخراج الجنود من المخابئ القريبة بعد إعلان "تمت المسح"، وبعد حوالي 20 دقيقة، أصابت طائرة مسيرة إيرانية مركز عملياتهم.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92589" target="_blank">📅 17:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط:
معادلاتنا مستمرة حتى تحقيق أهدافها المتمثلة في إنهاء العدوان والحصار السعودي الظالم على بلدنا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92588" target="_blank">📅 17:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قسما بزيد الشهيد ستندمون   وغدا لناظره لقريب   الطفل بالطفل  التمثيل بالتمثيل   تابعوا الساعات القادمة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92587" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇸🇦
🇾🇪
‏روبيو:  الحوثيون هاجموا السعودية وشكلوا تهديدا.  لدى الولايات المتحدة اتفاق أمني ملزم مع السعودية ونعتزم الالتزام به.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92586" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3bf61c39.mp4?token=ZjE5lMpj7xtH3tGM4xIwoosTAc6AyJVArDKuq1pcmqbZ1wakne4OGRsKlkRIoZc6crj2SDvTApAZIOx4BzZVUKa13PBkdAxQncDj5heJi1mNYuMn5_QtYQfADGoUn3p3EgGu6y9S-9YJ2CnFBxypVF8yCh4PGxhk-tWM5RSxxJAUv6bcjMH8rrNzbB6K1Tkffaz3zckoSjxKe0IsDFhBKckbcGg_tuNoGlJ42DrjtcrkGTInhLs3pKViFSpZmFZk-I3bA8hU8Z2knJXqxEeh4dvPQDeaIHKh9Pf32pxUGu82CwaAF9N5JqlOMlAkejsSS9C-MlqnLjE0SGKd3jJmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3bf61c39.mp4?token=ZjE5lMpj7xtH3tGM4xIwoosTAc6AyJVArDKuq1pcmqbZ1wakne4OGRsKlkRIoZc6crj2SDvTApAZIOx4BzZVUKa13PBkdAxQncDj5heJi1mNYuMn5_QtYQfADGoUn3p3EgGu6y9S-9YJ2CnFBxypVF8yCh4PGxhk-tWM5RSxxJAUv6bcjMH8rrNzbB6K1Tkffaz3zckoSjxKe0IsDFhBKckbcGg_tuNoGlJ42DrjtcrkGTInhLs3pKViFSpZmFZk-I3bA8hU8Z2knJXqxEeh4dvPQDeaIHKh9Pf32pxUGu82CwaAF9N5JqlOMlAkejsSS9C-MlqnLjE0SGKd3jJmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: انفجارات ضخمة تطال مصفاة نفط تابعة لشركة أرامكو في جدة السعودية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92585" target="_blank">📅 17:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92584" target="_blank">📅 17:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قسما بزيد الشهيد ستندمون
وغدا لناظره لقريب
الطفل بالطفل
التمثيل بالتمثيل
تابعوا الساعات القادمة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92583" target="_blank">📅 17:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇰🇼
بعد المنع من تصدير النفط عبر مضيق هرمز.. مؤسسة البترول الكويتية:
نحتاج للتركيز على إخراج المنتجات المكررة من الخليج لتخفيف الاختناقات بمصافي التكرير.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92582" target="_blank">📅 16:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇦
عقب سماع دوي أنفجارات.. توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة السعودية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92581" target="_blank">📅 16:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
أمس (الأحد)، خلال عملية لقوات تابعة للكتيبة "كارمِلي" في جنوب سوريا، بهدف تطهير المنطقة الأمنية من أسلحة تابعة للنظام السابق، تم العثور على ثلاثة ألغام مضادة للدبابات وعبوتين ناسفتين.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92580" target="_blank">📅 16:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ4fTFbnZYep_t6vAEtA4_DHQfuKLswNTMH3FGrfOgh3toq4auhZYoMG_M4f_grN6P6OzaTtCFKIe_HgQ0VSfPSD8QvuyQx8jQNnQ_aJj_dtPWEk8NubHtz3qNsPDEcGzXOf__tNvbn7OIbg5i7hm2cJquAkMxIGM3WAUV9bDroMEQYqF0qNhzUFj1yXA82GW7CNiKBSARAICKFdbvO0bHRahCFXGgT-44aZdvpafvkUx9Y7CiGNbgz8MiXoqpEUeRgNN_hpWr8k4iAgE7iX32MbzmwrE3nxAseBY1iFvR5u2cb9rBxrV3CnhBvWW2kJzg8ZyN9XTL8lkRbfLQzllQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
عقب سماع دوي أنفجارات..
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة السعودية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92579" target="_blank">📅 16:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد استهداف تحشيدات للعدو السعودي في رأس العارة بعدد من الصواريخ الباليستية محلية الصنع - 05 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92578" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني لنايا: القوات المسلحة اليمنية تستمر في تقدمها نحو مناطق أخرى في ريف محافظة تعز الجنوبي وسط إنهيارات واسعة لمرتزقة السعودية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92576" target="_blank">📅 16:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇹🇷
استهداف سفينة تركية قبالة سواحل رومانيا بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92575" target="_blank">📅 16:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9878e70264.mp4?token=qo-5OgoVO8tKTGSvDJZklSkAzNCb17X_xeRy_Fhr_2y9tyBGsz_8cq7Wy0jtUHyJae1clzYN97w7NYDxVvuLIJIy2hc3-9J5aGlAHIpa6ZM8cYk7lihnzcLBWtpwc6Ak0SXJkU3HgeEjS8VKIiseH6jCnx1uyEnVeuSJK72dXm4qY9hNAOLSwXxViWYES3ZjcMpB6u_ODdDbaBX7MCM9EglFYI7S4xg1piCVPTydisDTDZGNbGTxxX9NLpYY8eZwudF8bDVdeJmP7p3MrDQzquI3Rrcq6JAUKP2jonsG8t0Fio8k4tov8VXVRjNLVS8uDFb-xI6mIBNYDd71T3gevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9878e70264.mp4?token=qo-5OgoVO8tKTGSvDJZklSkAzNCb17X_xeRy_Fhr_2y9tyBGsz_8cq7Wy0jtUHyJae1clzYN97w7NYDxVvuLIJIy2hc3-9J5aGlAHIpa6ZM8cYk7lihnzcLBWtpwc6Ak0SXJkU3HgeEjS8VKIiseH6jCnx1uyEnVeuSJK72dXm4qY9hNAOLSwXxViWYES3ZjcMpB6u_ODdDbaBX7MCM9EglFYI7S4xg1piCVPTydisDTDZGNbGTxxX9NLpYY8eZwudF8bDVdeJmP7p3MrDQzquI3Rrcq6JAUKP2jonsG8t0Fio8k4tov8VXVRjNLVS8uDFb-xI6mIBNYDd71T3gevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
🇾🇪
‏
روبيو:
الحوثيون هاجموا السعودية وشكلوا تهديدا.
لدى الولايات المتحدة اتفاق أمني ملزم مع السعودية ونعتزم الالتزام به.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92574" target="_blank">📅 16:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
🇸🇦
مركز تنسيق العمليات الإنسانية اليمنية:
حرصاً على سلامة الطيران المدني، نحذر شركات الطيران العاملة في أجواء السعودية بأنها غير آمنة مادام العدوان السعودي مستمر على بلدنا.
أجواء السعودية ستكون مسرحا لعمليات قواتنا المسلحة، والجمهورية اليمنية تُخلي مسؤوليتها بعد هذا الإعلان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92573" target="_blank">📅 16:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇸🇦
على الرغم من تدخل الطيران الحربي السعودي.. القوات المسلحة اليمنية تتمكن من تحرير والسيطرة على مناطق يفرص وتهمود والعدف والعذير والشراجة وشنان والمحل وسنوان والشناخب والكريف في محافظة تعز، بعد دحر وفرار مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92572" target="_blank">📅 15:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
🇸🇦
على الرغم من تدخل الطيران الحربي السعودي..
القوات المسلحة اليمنية تتمكن من تحرير والسيطرة على مناطق يفرص وتهمود والعدف والعذير والشراجة وشنان والمحل وسنوان والشناخب والكريف في محافظة تعز، بعد دحر وفرار مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92571" target="_blank">📅 15:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac631a8dd3.mp4?token=FPhWNlPrE4gCW6IO7ySuYi630qUUJd9EZZQ9Z8G_5STFhN_SK7VxcG-puD2x2VX1B45PTEmzDgfAv-QRIYBdiwmYTQ3vLUcuJr_zOUanSHIcQeGB7jdqo9vHqA_PsclU-3O_6wmCSPZARLTiDOCcmgxmnkXJ5l110WNNkwPJwxUv-ssUc3H87uorPY3TuhEENe4NLAe-qDd9CEib8ohwG_DhAdvYG_PbtxiRGvYXGpQclRmd74bRgOvQkLqs3HOouGqiEn-heTmGtnTpdPTVQ2XZj_7U_Ov5NdjafKnL-UfBsNzz6JRDmbX2cm6ckJzNCmEN7XWhMWIZ7jHCvuhKkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac631a8dd3.mp4?token=FPhWNlPrE4gCW6IO7ySuYi630qUUJd9EZZQ9Z8G_5STFhN_SK7VxcG-puD2x2VX1B45PTEmzDgfAv-QRIYBdiwmYTQ3vLUcuJr_zOUanSHIcQeGB7jdqo9vHqA_PsclU-3O_6wmCSPZARLTiDOCcmgxmnkXJ5l110WNNkwPJwxUv-ssUc3H87uorPY3TuhEENe4NLAe-qDd9CEib8ohwG_DhAdvYG_PbtxiRGvYXGpQclRmd74bRgOvQkLqs3HOouGqiEn-heTmGtnTpdPTVQ2XZj_7U_Ov5NdjafKnL-UfBsNzz6JRDmbX2cm6ckJzNCmEN7XWhMWIZ7jHCvuhKkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92570" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce509edb.mp4?token=G9zo5OKr4ampA22NRhmmEEoBycEdTWtRR3GdSCjo9iskRNFv1mLtogvM28vcfqDQa-HJDRfuMbJ5SlHX2OlJKnxvPiDd2hDbQUvxZ5xo4unaX3l6LiWeCcFpQTLfRsS6UZFhSHYWZu5rXS9P_XP4Nkdez0Inir2CmQC9j5GUzJIND4l4MDHFzJ9C-NOqrGdbMvx_e8nWlvOMgiRiiYWndffFL0y5BJBWssT0suoguIXmEHfZp8B3lf3V6GDBjBBOizDAtMkAl0A895JxRaiQ6w1Q1lvdUH9m_5JJiqbQBsrfe-EFsgvCZk-K_ar_AFOQnihKoJ6PPWg6LMsCL1LUv4l3nZhy_eTCmddoqsqgvq3IF9AzAqWUsKAYHVHuX9ozTdZEvCa8xCE97coiKABo1YGRqIsx9z8ChtriZ2a_mNllBz-9PA9-scI0b9s_Z5ptoQw4r4j9UNsrIpHiIr1ctYyn0IUM8PiUpgTgoWiuW3KNuUplt2tOypclPfSadEfd1VAICltR5Sr2lKzNRWY2S3v6UGiip7uq5EGyIgXKXFhjXwOgZ7AoiE-cg2NE0P5JfECSXtY0LnPNtzNynwWPrN7UD-cjeCRaDfKmDhq9YYnnTh4LzrpYE7WrH1FRY63WVF8f2WQgi7hupoUO92NR0TGJjy0Yd4H-94I9fu9CIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce509edb.mp4?token=G9zo5OKr4ampA22NRhmmEEoBycEdTWtRR3GdSCjo9iskRNFv1mLtogvM28vcfqDQa-HJDRfuMbJ5SlHX2OlJKnxvPiDd2hDbQUvxZ5xo4unaX3l6LiWeCcFpQTLfRsS6UZFhSHYWZu5rXS9P_XP4Nkdez0Inir2CmQC9j5GUzJIND4l4MDHFzJ9C-NOqrGdbMvx_e8nWlvOMgiRiiYWndffFL0y5BJBWssT0suoguIXmEHfZp8B3lf3V6GDBjBBOizDAtMkAl0A895JxRaiQ6w1Q1lvdUH9m_5JJiqbQBsrfe-EFsgvCZk-K_ar_AFOQnihKoJ6PPWg6LMsCL1LUv4l3nZhy_eTCmddoqsqgvq3IF9AzAqWUsKAYHVHuX9ozTdZEvCa8xCE97coiKABo1YGRqIsx9z8ChtriZ2a_mNllBz-9PA9-scI0b9s_Z5ptoQw4r4j9UNsrIpHiIr1ctYyn0IUM8PiUpgTgoWiuW3KNuUplt2tOypclPfSadEfd1VAICltR5Sr2lKzNRWY2S3v6UGiip7uq5EGyIgXKXFhjXwOgZ7AoiE-cg2NE0P5JfECSXtY0LnPNtzNynwWPrN7UD-cjeCRaDfKmDhq9YYnnTh4LzrpYE7WrH1FRY63WVF8f2WQgi7hupoUO92NR0TGJjy0Yd4H-94I9fu9CIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
حرائق بالجملة في العاصمة السعودية الرياض جراء هجوم صاروخي كبير نفذته القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92569" target="_blank">📅 15:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
واشنطن بوست:
أدت خلافات داخل وزارة الدفاع الأمريكية في أوائل عام 2025 إلى ما نشهده اليوم من مشاكل تتعلق بالمخزون الأمريكي من الذخائر، حيث حذر مسؤولون من أن حملة واسعة النطاق من قبل جماعة الحوثي يمكن أن تستنزف كميات كبيرة من الصواريخ وأنظمة الاعتراض الرئيسية.
على الرغم من تلك المخاوف، أطلق الرئيس ترامب عملية "رايدر" في شهر مارس.
استهدفت هذه العملية أكثر من 1000 هدف على مدار 51 يومًا، لكن جماعة الحوثي صمدت وأعادت بناء جزء كبير من قدراتها.
تفاقمت المخاوف المتعلقة بالمخزونات في وقت سابق، حيث استهلكت الولايات المتحدة أعدادًا كبيرة من صواريخ "توم هوك" وأنظمة "باتريوت" خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92568" target="_blank">📅 15:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا، مشاهد استهداف تحشيدات للعدو السعودي في رأس العارة بعدد من الصواريخ الباليستية محلية الصنع.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92567" target="_blank">📅 15:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92565">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d67fc1a6.mp4?token=SWLE8moCiGrPYtAh7zx9jgLcbxLVX7xBjtHEBZuLoY8MG_6TvHLpCXc5Z-iFYChqlj3s54TNnNvuNQaD4h-JQv9ZJ_xkKnLitEQdjYbRxGgB_UlCNe4oOXP5vHRyAbcgt1RBXLgfgOsfvhSjCgjv179vcsWXvewnhx6VrsZxxC8pHmlsRKERSGVCbvQ-86fOMmcg5KgyCL0ceUhhqlXMi9PZ0mc6AZhyPckLv6kzLGZ4Htk6JHScIfyz-2YddLvFOacyzx4nZjC0pU4x1sBkM5nlww4mVEUjEM8g-kda64OoW7eHdvE6sByojoN8W0DUjVoluQozIuXblqkeBOSAwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d67fc1a6.mp4?token=SWLE8moCiGrPYtAh7zx9jgLcbxLVX7xBjtHEBZuLoY8MG_6TvHLpCXc5Z-iFYChqlj3s54TNnNvuNQaD4h-JQv9ZJ_xkKnLitEQdjYbRxGgB_UlCNe4oOXP5vHRyAbcgt1RBXLgfgOsfvhSjCgjv179vcsWXvewnhx6VrsZxxC8pHmlsRKERSGVCbvQ-86fOMmcg5KgyCL0ceUhhqlXMi9PZ0mc6AZhyPckLv6kzLGZ4Htk6JHScIfyz-2YddLvFOacyzx4nZjC0pU4x1sBkM5nlww4mVEUjEM8g-kda64OoW7eHdvE6sByojoN8W0DUjVoluQozIuXblqkeBOSAwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حديثة للحرائق التي طالت مصافي شركة آرامكو بالعاصمة السعودية الرياض جراء دكها بالصواريخ اليمنية يوم أمس.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92565" target="_blank">📅 15:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2 Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية في أجواء محافظة تعز، وقد تم استهدافها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92564" target="_blank">📅 15:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92563">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
🇾🇪
حزام الأسد:
ما يزال العدو السعودي يقدم الكذب ويبيع الوهم لمرتزقته؛ فـ«انتصاراتهم» لا تتجاوز وسائل الإعلام ومواقع التواصل، أما الواقع، فتحشيداته في هروب مستمر، من رأس العارة على خليج عدن، وحتى المواسط وبيت الخائن العليمي في تعز.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92563" target="_blank">📅 14:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92562">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bfe7f6f14.mp4?token=PLQf8UOZmmArFs84pndWiWe2H7frptRlKoEwwv9gmGWGHSTYdJwWGOrMpWw2an9qYTQKYYEeXVUsnDSGnqmPWov456qOGc2CzbU_gWjBBS0InKE4utKPjAbTcti3nIJ_rtr8QfzmTaX_9pMzQdqofXFIwUWJoo3OAkpEi3jB-QwuP34ST0gVISnJ_jtNNvFO1pPqqz6IILBnE5zZBFzvcN074TAeT_yyWUjpt14GIc96-TDvr-E8uwIALCFw_K3CFi-e6VtGrnd7gctgVuoShqZrg-D3tvDhgOcFcldg0mwsHouoJNXZ48TJj7MCcP3ifA2jVUweLZj1OUmcDHG-9lmcxArsYq9F_gtYLdHwV4VK4gqEngw5E3sGeb30IixFSGE1TkC3mzvA3RB6we2wVbA20_V5lAOvrwRw_1W4KjXCANqfSAJSan7UDooUtBUW8iCOvX9t1dxnBV_imOcayGFMgmNVeknxGd5ieqMc78ZXOUoSF3lJ5HAeF5U2nHOwJsDroxR6iXb2vdQLX5t61s2dXquPtDwXc4o6bktuCkJVUWPztHq2P26foZHY2YCRra0E-gk9vImlrV8delVjZw-oyJa68AGSQ-fMwhZqodPypkYjWN38HAUIRY9BqhTREfC7Pq-n5oBLjC6qqTf6J4SP4bOfw94KbfZVVX44IEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bfe7f6f14.mp4?token=PLQf8UOZmmArFs84pndWiWe2H7frptRlKoEwwv9gmGWGHSTYdJwWGOrMpWw2an9qYTQKYYEeXVUsnDSGnqmPWov456qOGc2CzbU_gWjBBS0InKE4utKPjAbTcti3nIJ_rtr8QfzmTaX_9pMzQdqofXFIwUWJoo3OAkpEi3jB-QwuP34ST0gVISnJ_jtNNvFO1pPqqz6IILBnE5zZBFzvcN074TAeT_yyWUjpt14GIc96-TDvr-E8uwIALCFw_K3CFi-e6VtGrnd7gctgVuoShqZrg-D3tvDhgOcFcldg0mwsHouoJNXZ48TJj7MCcP3ifA2jVUweLZj1OUmcDHG-9lmcxArsYq9F_gtYLdHwV4VK4gqEngw5E3sGeb30IixFSGE1TkC3mzvA3RB6we2wVbA20_V5lAOvrwRw_1W4KjXCANqfSAJSan7UDooUtBUW8iCOvX9t1dxnBV_imOcayGFMgmNVeknxGd5ieqMc78ZXOUoSF3lJ5HAeF5U2nHOwJsDroxR6iXb2vdQLX5t61s2dXquPtDwXc4o6bktuCkJVUWPztHq2P26foZHY2YCRra0E-gk9vImlrV8delVjZw-oyJa68AGSQ-fMwhZqodPypkYjWN38HAUIRY9BqhTREfC7Pq-n5oBLjC6qqTf6J4SP4bOfw94KbfZVVX44IEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي على صنعاء</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92562" target="_blank">📅 14:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92561">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
🇮🇷
الخطوط الجوية العراقية تستأنف رحلاتها المباشرة إلى إيران ابتداءً من الخميس.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92561" target="_blank">📅 14:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92560">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy6emLoZjXhUKhG8wCj2u4-OwQ7iNhbuJOuza5ILrv6NIxudwifwAThQ2Dm-qeGlVAwtS58uzclny1kpdQGp9YShgnwjlEC590G5v-Y9WygGn5OTqO3a7IMxm6xwl_omYAFTW7xJm6guEDX13P92tS1qTWfBaVIxpo24uKQ4cebHc5rrRKnGghPdoHGu8G2CQfHOCsknwjspxW-atJcfS25YkSilNsSoTxp_7DuCSW_mDk1PWKF6QFnc9-aIcv8SaT8-DjDcfuPI2rokXPXg_9OzUDGWyARkPLxJwTNLdF-WK8d2yemK_-p8lNmWcvrwgWoiPiJ32h3qrpH3zphF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بحرية الحرس الثوري تجبر ناقلة نفط على العودة وعدم المرور من الممر الجنوبي لمضيق هرمز والذي تزعم القوات الأمريكية السيطرة عليه.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92560" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92559">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa1534f592.mp4?token=Lpzb3iGWX5zJ-WPw5dLhfL2G9yYpUsJREU1AAQzk0shm6WndEI45tUOTGPHurIogPVyNUY4USZ1kstfTY6XnAVChLqnKMFAT74i4BQK1eeZmxR1DV9pbCodUMNp37XYyKSno-LlS8lgYuwDRoNuxgAX5x2Rz6RZeqK9PtxSu2wDzzCwYEbqZ1x8s0BCqPOqEOPgP2EPyhPkiamjxh_KeGRktN7ay3qVaJQUunMv-wykU1jQEaFTlBSPciR61bJKSTEcOdJHqrNWfE2PwcohDem9MOlIbQmpQ1PY1ou9RPCy8IAdN9QNbSpU94ujjpr0j8sHuaycBeHK18Ni6Q52xDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa1534f592.mp4?token=Lpzb3iGWX5zJ-WPw5dLhfL2G9yYpUsJREU1AAQzk0shm6WndEI45tUOTGPHurIogPVyNUY4USZ1kstfTY6XnAVChLqnKMFAT74i4BQK1eeZmxR1DV9pbCodUMNp37XYyKSno-LlS8lgYuwDRoNuxgAX5x2Rz6RZeqK9PtxSu2wDzzCwYEbqZ1x8s0BCqPOqEOPgP2EPyhPkiamjxh_KeGRktN7ay3qVaJQUunMv-wykU1jQEaFTlBSPciR61bJKSTEcOdJHqrNWfE2PwcohDem9MOlIbQmpQ1PY1ou9RPCy8IAdN9QNbSpU94ujjpr0j8sHuaycBeHK18Ni6Q52xDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حديثة للحرائق التي طالت مصافي شركة آرامكو بالعاصمة السعودية الرياض جراء دكها بالصواريخ اليمنية يوم أمس.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92559" target="_blank">📅 13:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92558">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daecbfdad5.mp4?token=fdyEcPvC5bi2HgOV7mk9nAYAV_8HQ1n1DFlsqOuqnkIdOV3JBqJsI1unv5jYkcpgaqaC51n8v-bPxpLvwpo290Y02_p6I9mUhBuW36-5UYIuLx7Lf-sE8ClUlzWSyUbue1SztEYN14sQSEnaks9gEYK0OXbsNYtFo1Qvwp6SsNlOgVu60-kByLG9EkRxjjiIfsJG8t6s-0AP6hBvePP81QnbTP-9doEerpzdYntkGBvJgH5uSk6IDyVUHNVEip_TGsJs0iEmpOTvTB571aw7lnyCPzD5Q-h-LblNfhBipu-34dX5SSx1Ulyv3uluWapuKvVQo99PQaun5z1tttMOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daecbfdad5.mp4?token=fdyEcPvC5bi2HgOV7mk9nAYAV_8HQ1n1DFlsqOuqnkIdOV3JBqJsI1unv5jYkcpgaqaC51n8v-bPxpLvwpo290Y02_p6I9mUhBuW36-5UYIuLx7Lf-sE8ClUlzWSyUbue1SztEYN14sQSEnaks9gEYK0OXbsNYtFo1Qvwp6SsNlOgVu60-kByLG9EkRxjjiIfsJG8t6s-0AP6hBvePP81QnbTP-9doEerpzdYntkGBvJgH5uSk6IDyVUHNVEip_TGsJs0iEmpOTvTB571aw7lnyCPzD5Q-h-LblNfhBipu-34dX5SSx1Ulyv3uluWapuKvVQo99PQaun5z1tttMOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
استهداف سفينة تركية قبالة سواحل رومانيا بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92558" target="_blank">📅 13:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مرتزقة السعودية يهاجمون محافظة حجة شمال اليمن والقوات المسلحة اليمنية تتصدى للهجوم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92557" target="_blank">📅 13:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jt4G9iF1-ZVvyQb6V3AEDT3SQ_V6F-badIyPGfoQFG9fSkhR6t5ErWKemd2nxoDGmdWCUg1hiQK4Z6PNmiFfxe_Eei6pGVPESbkEIUmbkBTxChkb-QXKyuypSN2gC1U9An9fcueksCoemHQMBT4Z9bHNLRHsCchlKFnu4oMdJ78LQjaK2xlRIzjG0O6lSyKUJnuWf394nOihf-IjABGxbq91Q_LBlcoG-5KARs6KHscwxZyUlyVS_XNTIMf8WtJGVmyeAF2LxkeH1bgSI1zrg-G_w04Mnc9CpFz3AbpXZfKcjDhPzBTYYQA4dAmzVpuwf89IbKeUH5o-tRGpzdAZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzvMSmHuRPdRU57-UJZbQumVlm0hsqrlm1-YdrJ2-7u1tuAPs_e_AC1bIF42FIg8-ldvGc9yBDKmOhTTZw-TEw0gW9fdm90tmoDMRTkINvS02-p9X9_1aXHYrI7bntWWHJGAG5f8IeEjOOw6W5MiPqG4hU_wBYsPRdFYcPyOVTTHPgbdGK11cBn3wur_UEJRix7zLmgXBthVtdhK9I8xZaxMwHTCv6YsUHBl_3rfrLXTIjKUHDAsaJ0syWrNKRl0lR5KXI06iAeohT3kSvDb_21tEmFmiBVsaGKuKriE3FBkGU5BdOlwAZ7e1AeF-D_NYrCxTuFV15uLackKjcEEfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدوان سعودي على صنعاء</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92555" target="_blank">📅 12:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92554">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عدوان سعودي على صنعاء</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92554" target="_blank">📅 12:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92553">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">النظام السعودي: سنستهدف كل هدف متحرك في مضيق باب المندب</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92553" target="_blank">📅 12:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92552">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">النظام السعودي يعلن مشاركة 100 طائرة مقاتلة اليوم ضد انصار الله</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92552" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92551">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">النظام السعودي يعلن مشاركة 100 طائرة مقاتلة اليوم ضد انصار الله</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92551" target="_blank">📅 12:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92550">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
🇾🇪
الاهالي يحتفلون في سوق التربة بعد دخول القوات المسلحة اليمنية الى مدينة التربة في تعز وطرد مرتزقة السعودية منها.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92550" target="_blank">📅 12:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92549">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad6eeb18a.mp4?token=Y4hHiu4BakWmR8cWPEv9wCsU20byraH5cmpCt_Mc8hVzNGFTRM2F1R2bKQ1IXmjQ65SKgaaZuR6tFHu5cdBX8QwXOW4DIFJ6I__AY7bGb8ftxGxG8iDVXuuKXWyfsYhOAbD9JCZGq7GDDjdvaWs5psqFm9muMiH3nMXZ4oe36d5o2X8WbpVEOalSQCYUBHoZGmzwg1DWf29f2mSq3hmv04kAuf8iWsTYCDDJ_b-zg-LF8qhozBTE94D7TgD759R0hnfvjvZwN7PU5ajrpDz3Fyi96LOI9nE3LlYjFCI2i5SgUECTDUEXLY0124heWYlnP-LfFh8kiZzSiI6uNhF6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad6eeb18a.mp4?token=Y4hHiu4BakWmR8cWPEv9wCsU20byraH5cmpCt_Mc8hVzNGFTRM2F1R2bKQ1IXmjQ65SKgaaZuR6tFHu5cdBX8QwXOW4DIFJ6I__AY7bGb8ftxGxG8iDVXuuKXWyfsYhOAbD9JCZGq7GDDjdvaWs5psqFm9muMiH3nMXZ4oe36d5o2X8WbpVEOalSQCYUBHoZGmzwg1DWf29f2mSq3hmv04kAuf8iWsTYCDDJ_b-zg-LF8qhozBTE94D7TgD759R0hnfvjvZwN7PU5ajrpDz3Fyi96LOI9nE3LlYjFCI2i5SgUECTDUEXLY0124heWYlnP-LfFh8kiZzSiI6uNhF6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🏴‍☠️
نجحت القوات الروسية في اعتراض وتدمير طائرة أوكرانية مسيّرة انتحارية من طراز "ليوتي" (Liutyi) فوق موسكو باستخدام منظومة الدفاع الجوي المحمولة على الكتف 9K38 إيغلا-إس (Igla-S / SA-24 Grinch)، ما حال دون استهداف الطائرة لمصفاة نفط في المنطقة في اللحظات الأخيرة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92549" target="_blank">📅 12:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92548">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يدور الحديث عن محاولة دهس قوة تابعة للجيش الإسرائيلي. وكان في المركبة المستخدمة في عملية الدهس ثلاثة فلسطينيين، أصيبوا جميعاً بجروح خطيرة جراء إطلاق قوة الجيش الإسرائيلي النار عليهم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92548" target="_blank">📅 12:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92547">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الاقمار الصناعية تظهر ان خط أنابيب النفط السعودي بين الشرق والغرب قد تعرض للتدمير مرة أخرى وتصاعد اعمدة الدخان منه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92547" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92546">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf2Vs840BsEXhssQWOG6zhpP3cXajYmbolK0pzPv7YBvNev7rtU1ZUK1Vf79AYa0FiYtrht3_NrcOZG6Tqg3ef95_Y90RKYsJ04mhF-ka-SCo7e45yubjrs_b1Z1fj71OVfGXaSl6_NL2JU1u-oKULam98aDcYQ9vtOwCys71msE7oa8W8Ivv0wEn9YniK-cHeLzCh5Q0pzUZhyFZaSSMuri_rOVbmRxSLL6Rh3ZwMW468XuUU9TG98JayZA_U1HmHvXq7eg1QebdoP2wSyaJX5M5iKLXV8c3oJ_D2z3pzDKR9wN1rO5zyc14Yhc9FqJvaC83P6qxTL6mLTocI2jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحشد الشعبي يعتقل 45 متهما وتفكيك شبكات للإرهاب وحزب البعث المحظور في 12 محافظة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92546" target="_blank">📅 12:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6634fd1307.mp4?token=gUvd_Pf889aaNS3Y1A3Kiywv2mMeIqOLt8yMXZ11WoJhyjoEEW8bGx9cAkNOqZPPd-4MDfSe_u8sM4amOtAi2sYtZ_vLwYPlf4LQQ_5Jku_k74qCLtJe7eOfpWpDsogDrIJe1rrKvxDaYfCBbR4VSZoKmxJR1XHkRPBULujDk90LOND-iBX9jxIU-Cglz354AGoOEo7Ahf9VUdafvI-oV1E553ZsM7sM2z0MKfYm16DtBcaafnQpku8tDeMRZ_DEe9rcJCtBya0Ei3HJFsBrd1fio4mKuu7epzKo2kRktojvjjtA8bDAgw0mzuTzz0AM7VQIm9dDbf6835R00URKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6634fd1307.mp4?token=gUvd_Pf889aaNS3Y1A3Kiywv2mMeIqOLt8yMXZ11WoJhyjoEEW8bGx9cAkNOqZPPd-4MDfSe_u8sM4amOtAi2sYtZ_vLwYPlf4LQQ_5Jku_k74qCLtJe7eOfpWpDsogDrIJe1rrKvxDaYfCBbR4VSZoKmxJR1XHkRPBULujDk90LOND-iBX9jxIU-Cglz354AGoOEo7Ahf9VUdafvI-oV1E553ZsM7sM2z0MKfYm16DtBcaafnQpku8tDeMRZ_DEe9rcJCtBya0Ei3HJFsBrd1fio4mKuu7epzKo2kRktojvjjtA8bDAgw0mzuTzz0AM7VQIm9dDbf6835R00URKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تصل إلى منزل ما يسمى بالرئيس اليمني (رشاد العليمي) المقيم في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92545" target="_blank">📅 11:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92544">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">القوات المسلحة اليمنية تصل إلى منزل ما يسمى بالرئيس اليمني (رشاد العليمي) المقيم في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92544" target="_blank">📅 11:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92543">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئيس أرامكو:
ضغوط أسعار النفط ستزداد سوءاً حتى إعادة فتح مضيق هرمز وإعادة ملء المخزونات العالمية قد تستغرق عامين بعد إعادة فتح المضيق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92543" target="_blank">📅 11:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">القوات المسلحة اليمنية تصل إلى منزل ما يسمى بالرئيس اليمني (رشاد العليمي) المقيم في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92542" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92541">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">القوات المسلحة اليمنية تتعامل مع هجوم غادر لمرتزقة الامارات وتتصدى لهجماتهم مع تواصل تقدم انصار الله في جبهة تعز</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92541" target="_blank">📅 11:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92540">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مرتزقة الامارات في اليمن يعلنون بدأ الحرب ضد انصار الله الى جانب مرتزقة السعودية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92540" target="_blank">📅 11:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92539">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مرتزقة الامارات في اليمن يعلنون بدأ الحرب ضد انصار الله الى جانب مرتزقة السعودية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92539" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92538">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b010f7c4.mp4?token=dHaFlyTwJMBb8ynOtfdebBUJ7wAMqS9P--MAnFAeZ28OHceA91MFv1Zr-Vixkfeq0kNnFa_y-agSgc3GGSViReWAL2YOKnTtxXOJT_pE_5_LAfCxNGr3vklMfcFC2r3TXtXrCaxIgVZSkXsDxaetz9QBuhJ6tQNBo72iao2Cl1tKP6oaojGVOPNYEn8bvvYzm_c5AJtRQX2MiZG0dLXG0lENePmFFY2DPAjUxmXaF6O6HxHcWgzQwmL7T4OSeU6xGFTW07tPgffjWMv2e7ROHAkVvWcRdTvP-JbYhvUrR13n1bcXewW6mQyqHodiMOOh8lHmMl64zIzhH_lQyvMWEQw6LCT2IAoBJ-d6GXAiKoRplegjTxW2CF7K15P0HDbzUOKGeB6bWHpBqFRgKkcr_QaW3wbmM37CMBjtKc4RAz5ej_ZfGv9SgXQuEgd7ehlReMhcVce-VMPdH1Jjwb_Sd0v2kFw-xbkyJ4N9EwSK6J9qvmiPPIp4bfVzZ08FkyR8etVeqGlQH_HjnKRNF5eEERaoEKArXD5_pOwynBy8vCcn9NTsNSzaOvPaWUtAg3yCaKZIkZGT3Nt4CxTIcytPeLpLYGh6nDeXdd-GssAs5hJsnZctFUhRhH9G_6my45Sll2elA-e5xpYyv7AdsfnqpyXZ2ttkTwQ84joGXm-8oT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b010f7c4.mp4?token=dHaFlyTwJMBb8ynOtfdebBUJ7wAMqS9P--MAnFAeZ28OHceA91MFv1Zr-Vixkfeq0kNnFa_y-agSgc3GGSViReWAL2YOKnTtxXOJT_pE_5_LAfCxNGr3vklMfcFC2r3TXtXrCaxIgVZSkXsDxaetz9QBuhJ6tQNBo72iao2Cl1tKP6oaojGVOPNYEn8bvvYzm_c5AJtRQX2MiZG0dLXG0lENePmFFY2DPAjUxmXaF6O6HxHcWgzQwmL7T4OSeU6xGFTW07tPgffjWMv2e7ROHAkVvWcRdTvP-JbYhvUrR13n1bcXewW6mQyqHodiMOOh8lHmMl64zIzhH_lQyvMWEQw6LCT2IAoBJ-d6GXAiKoRplegjTxW2CF7K15P0HDbzUOKGeB6bWHpBqFRgKkcr_QaW3wbmM37CMBjtKc4RAz5ej_ZfGv9SgXQuEgd7ehlReMhcVce-VMPdH1Jjwb_Sd0v2kFw-xbkyJ4N9EwSK6J9qvmiPPIp4bfVzZ08FkyR8etVeqGlQH_HjnKRNF5eEERaoEKArXD5_pOwynBy8vCcn9NTsNSzaOvPaWUtAg3yCaKZIkZGT3Nt4CxTIcytPeLpLYGh6nDeXdd-GssAs5hJsnZctFUhRhH9G_6my45Sll2elA-e5xpYyv7AdsfnqpyXZ2ttkTwQ84joGXm-8oT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ان خط أنابيب النفط السعودي بين الشرق والغرب قد تعرض للتدمير مرة أخرى وتصاعد اعمدة الدخان منه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92538" target="_blank">📅 11:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92537">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">▫️
تصاعد اعمدة الدخان من بلدة بيت جن في ريف دمشق الغربي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92537" target="_blank">📅 10:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad89acdc29.mp4?token=ibQEufnUgGfZrYyVyH1xITovycZC5g4WShgXk-DXPW8z1hkk329kxGQ-fZhJCvHJZuWXj-AZG5aeqf1IO_EBnwBfdajxfxq3QLDE_MYFxIe7bvgmGYoT00mfvGsw4nVllcsZUypHw_bMk-qw7aBL8p3d_D3ARDNNn0tqBOFVVGARbELcSm6m8-AQjVk7AbDce_PdWX_DL36aH5PQlPTPQA0wcStWcDF8YyIHm0HJlE-sUQN1rdn2d96VEvThWnTLXQsd1Su8KgITB5rWoEh8cSvGwTMHQA7ppQIHNuOssFq8TlfnmrsYUT-k4Lb3PYk6XhgIZ8i_JT2EbsXIT5lzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad89acdc29.mp4?token=ibQEufnUgGfZrYyVyH1xITovycZC5g4WShgXk-DXPW8z1hkk329kxGQ-fZhJCvHJZuWXj-AZG5aeqf1IO_EBnwBfdajxfxq3QLDE_MYFxIe7bvgmGYoT00mfvGsw4nVllcsZUypHw_bMk-qw7aBL8p3d_D3ARDNNn0tqBOFVVGARbELcSm6m8-AQjVk7AbDce_PdWX_DL36aH5PQlPTPQA0wcStWcDF8YyIHm0HJlE-sUQN1rdn2d96VEvThWnTLXQsd1Su8KgITB5rWoEh8cSvGwTMHQA7ppQIHNuOssFq8TlfnmrsYUT-k4Lb3PYk6XhgIZ8i_JT2EbsXIT5lzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم يهز ريف دمشق الغربي</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92536" target="_blank">📅 10:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم
: اعتقال سائح أميركي قرب مقر وزارة الدفاع في تل أبيب بعد أن زعم أنه يعتزم تنفيذ عملية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92535" target="_blank">📅 09:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92534">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxd_igIJ0Mz2ynjbLVdi9OttWNLqnO6wVKBim95F9awjDyyPWfTzkorwsqNvop7NQn0RZJDXZEgGwQXhzUp2Y9s4OnnsMwxnHlwR-6SKYu5V6b7E5MXbOy8JjdoiZ9WhqMh2xAQ2PcBd1kZHw113SHdotly6BQ3iBxfQfeZtL-XUyijspJF3ouRZdX1JEkDLN4_LhiUiiVhSAlvNQm5k42QAQnzmQtIfbkldQgXEgsjbC_SAcUtV_vVlzCqphAsKXQMjdpsFdP-3TWG0d86P52CSeiNZX5l6uuop0rQLl-GOsDyxFBiDtbd3k5L4SGfYTsfb-OkMCAY6lycnhf9LvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استشهاد شرطيين ايرانيين في هجوم على دورية للشرطة بمدينة بمبور جنوب شرقي البلاد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92534" target="_blank">📅 09:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92533">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار ضخم يهز ريف دمشق الغربي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92533" target="_blank">📅 09:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92532">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuATB3MYRSJqytFxAbXbfYLhCKd-Ry91dZjDZHj7P7vTgSpcDpHgaV6KfjtI6GVnoEGuWnbYWlT1eXp3DtyV7YFRijOyhoZpPSWhvfOzpO_jrR8QaBSPlSWhLeokJ-Ef7fRcyYPRWccaDvtvhsYvLFCCdziEyRJAFgRl1AFgWFPggVtMnBdIx7F73U-i8Wdkfdo0OXTfwinMGU-H1NzUUuohnF49Awlp9durpKX1hWc-8s4mQDbctiuKTWka8sRlvZWCVZTsIgKFmD0SxaPPV5F218bdoLasKoKOqp7QoRRVc_gusHCJxv6Om7jSWx9eAWXZ_pVRCT1ctgq41Fn62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف حركة الملاحة الجوية في العاصمة السعودية الرياض و مطار الملك عبد العزيز في جدة
.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92532" target="_blank">📅 03:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207f1330af.mp4?token=gWH-PbTemXNpULyVoypr5WPv9Fqec04d2hS9ADNoLw2OHUZlXbIOLYd__90UWBhXsezAjhBKCSP5KnqGrzJmmkQZLMkFzmykpanHgwNpOT_U8JU8TEXVPRNT_tbPfHJ9JfhSbZM6wcabxWQHveF5_FGzosI4bzFYVy6d0pRj1PHkYXKHCkHFsHf4gZVM8iu2MWb8-S7DoR_afP2T06clkDUqa8iwRYWl_mA5W67QrI0pG_HO_Hww4uyaEqUDUqnji2uKhyFYuv76H0cPRviIVZcDNbtR67RS5Za6O0IGdzgf1uXkMhZWC1VEchXOfXAW6kH8JFAAPGQj_pm3dJ73BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207f1330af.mp4?token=gWH-PbTemXNpULyVoypr5WPv9Fqec04d2hS9ADNoLw2OHUZlXbIOLYd__90UWBhXsezAjhBKCSP5KnqGrzJmmkQZLMkFzmykpanHgwNpOT_U8JU8TEXVPRNT_tbPfHJ9JfhSbZM6wcabxWQHveF5_FGzosI4bzFYVy6d0pRj1PHkYXKHCkHFsHf4gZVM8iu2MWb8-S7DoR_afP2T06clkDUqa8iwRYWl_mA5W67QrI0pG_HO_Hww4uyaEqUDUqnji2uKhyFYuv76H0cPRviIVZcDNbtR67RS5Za6O0IGdzgf1uXkMhZWC1VEchXOfXAW6kH8JFAAPGQj_pm3dJ73BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇸🇦
من اندلاع حرائق واسعة النطاق في العاصمة السعودية رياض اثر الهجمات الاخيرة للقوات المسلحة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/92531" target="_blank">📅 02:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92530">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d457ab53.mp4?token=c858emqgHL7Qk0Ryx6V-k66PF_0ZG7i3Eq2yfkukgrd1UGBvQGfuponwjcgty4Z4Kba8mFz61M24ZYpC_bCHIFOgNQ4IbtwRysiiARH_jv6vjgMbeTsFvpXM5kYUuiw-8LpgcjXHaoqgzPo-JwCKFSqK0CdFnG_sfig5tilin_q-ef3EJBM3jeXEX56513Uvn5u1g11oq9TtqpGFU8H2PsuUlp2hjjQo9FsBX9Q4GugeCGYbqnUtxxREp_PtcMcJplZuX6XzNAM-Cfa6WkxmwvHp75QJdO9HrLhdVUnga-QPDX5qGWC-YC1DYvttGP20sxGXJ3--YmsdISWg34QSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d457ab53.mp4?token=c858emqgHL7Qk0Ryx6V-k66PF_0ZG7i3Eq2yfkukgrd1UGBvQGfuponwjcgty4Z4Kba8mFz61M24ZYpC_bCHIFOgNQ4IbtwRysiiARH_jv6vjgMbeTsFvpXM5kYUuiw-8LpgcjXHaoqgzPo-JwCKFSqK0CdFnG_sfig5tilin_q-ef3EJBM3jeXEX56513Uvn5u1g11oq9TtqpGFU8H2PsuUlp2hjjQo9FsBX9Q4GugeCGYbqnUtxxREp_PtcMcJplZuX6XzNAM-Cfa6WkxmwvHp75QJdO9HrLhdVUnga-QPDX5qGWC-YC1DYvttGP20sxGXJ3--YmsdISWg34QSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش الاحتلال الاسرائيلي
: رصدت قواتنا شخص سوري متسلل الى جنوب سوريا وفور رصده تم تحيده فورا.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/92530" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tu_STmx8xOGcnpqi1w4JGi4Rn4N0o4ISi4XzwpSD18ONQ5bXKyBioJzNnonrgZJTOZNm0RV9Chj4_JTLOC6ETjn133ITbSEDZ3v9ogACV-1yrZN5bXox_FSi_7Ju4XziePXO8mv_SROFEEw99PDFWJlsDnDyCxp1wMaxMarQovMHYRsMv99ZIUoO-pUp0TQYDviyH8hTG8PbqpwWstoR0YT4sUbgduF6AymYgxACv05Px7KRIbqo914R1N8OWLEMmLH6Y39Zne66QSXFAUcbRFrkVYmqhDuAOJBMg6h7eUjRt2QnoPNum5AyMUCBGO5ZZeSnBnjscO9XEJaXED2KXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rE3-mQGKCEnSLPI6Vp5pEFGqFbrD7mKlQssb-jncVa8Ekac_1W9QxwACSAqzIa4lUnSU7JVmjVYlj8lNGdVrvEm0ZtOE6sTSt1rgAKOL7NElgvGE4cMyWsmJ6I0wbGjWThmwEXPhRdBvY7WK2pKliDOqfJdQ8Tg8ArscHHpEgG-O2ePrQ8rGkS9xAVhtfNCVhYAnhF6n9rXfTxUMRbKVq5X6Duyv7jg22Jdzw_kK54LabEigyrnLJeI2MRemQ3RbPswGLOEwAfBE9Ab-QlkLjZ6bq20A-OqIKDj-zhkLskueOqhdUSNbbe4PA2ZXMOK2nAOSjJ-Ck2JcXaRoe7Et-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ترفيهي
🇮🇶
🇸🇦
🇪🇬
بلوكر مصرية كانت مقيمة في السعودية وتعيش حالياً في العراق تعلن أمس عدم احتفالها باليوم الوطني العراقي معللةً ذلك بإقرار قانون الأحوال الشخصية (القانون الجعفري) في العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92528" target="_blank">📅 00:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
بعد الحادثة الاخيرة لمحاولة استهداف قاعدة فيرفورد
صرح
مسؤولون أميركيون:
سحبنا قاذفات B-1 من قاعدة فيرفورد في بريطانيا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/92527" target="_blank">📅 23:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzmMg0_HWtpoxMhgfbbcxNfqZq8nueFA1bmow6PyZOG5Ch937shcper-y516kxuLmCGPiUcG2mTUfjJSlspiG0fg-nhymSDZaEsGkSe6cFh5fmIwpCKhBFD3vFAkKHWRGJwwO-j3OXDPrE8mEkuV-oSHUVkp2gUxBSSPT0eGHaQ5JffLLmW5zccptN4CMJ7gRKZsWmDYuPORXPeg_wchAuzvzvczcTarlfmMBPb7MEbyCVCJSzh_rYqfwCuGY8hlMspm6sb9mgSYhK5nbUt76U28XRWUgb18oSY3M8gygaCf8SLtPabORxWCmNueEwKx9CUo7zguw-R8mzVxnREITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
نشر خريطة الميثاق الوطني التي أقرّها آخر برلمان عثماني عام 1920 في شوارع إسطنبول، وتُظهر الخريطة مناطق من دول عربية عدة، من بينها العراق.
🇮🇶
ننتضر هيبت الحلبوسي ينشر خريطة العراق خلفه
😆</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/92526" target="_blank">📅 23:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
انتشار قوات المسلحة اليمنية في ارجاء مدينة التربة بعد معارك مع المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/92525" target="_blank">📅 23:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuNRsHexpu0grX3wkyVu5u_Lz4wNb31G8qxkDnZwtE9JrMQanRr6fLdL3SbYbG5eka_7ynS-CJqUNl4vBze-zn_KpwR_kQS2ogxhNydro-kkWkpqjsZwoA2p_AFf971_D38lnAwneZD0zwXgAgxPbaSbBuxDHEWpHnIAq_9hhO3PevSFCCc8LzlzrxaFKvdUx0UXhTQyl7QneWECleqj2rbhztXjXseaS1ByKmrt9jCi0koy21sHjJyJ7tR4PPEo5uuDk-0kNho92NxjGQeJvgrYPBKfLg3JycgjUkjg-n9vTbi6GbvTnD9JujRsIXGq7Ml246MWk1QZiuKePcPCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة مجهولة في مضيق باب المندب.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/92524" target="_blank">📅 22:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/92523" target="_blank">📅 21:45 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
