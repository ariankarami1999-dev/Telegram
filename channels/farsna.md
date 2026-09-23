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
<img src="https://cdn4.telesco.pe/file/LNf_NGgmGa68bjo5aD2m-CMOw4tjhd49sBT3fURp6kEb4yNRY1HbmU7dtVZ8o5h8vNFDBmSpDKmlfAj2SomHUmnIA3qLX3YcPTIpkvrE9ANRbqtxaQFWidahbc-hl8e6xpFqTETox49PCv4fCze1f_v_H3NE8AgWkpetv4Jiunl2UQ9iVoZe_c_9OmUIKWRlNTV8yvIKpmKBjOoF6sO1fJCYqdoASVcAaqZjUujMea9UWZb4X5A3JIwzK42_XbuvL6mULdPh93XkuIDTWvo-J3NJboIE6TqI_H7UGUeWn1v6sPtaOCJxbetA7ipVPWz1Za26yp_g3AXkOZE6R9mVyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-464015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dd9ffa59.mp4?token=qukY35rezEVW87PoN1MOSZtMhQz66p1DPn0YBgJ4zMmMB3DQ6xuv3KPrclzJn6lr1hQoWCKUI7FipOt46LBDNnYhu8uhvBX0WFlF3GGy6PJB4xtoY7mdPr4peO7bsR4gy3AHSi7ZTn6xSQDTwLhTQcIlxhm93OIQtiqC7I_Xk7rJjz_a5_cdT1vMkTqXLhx6EdBUWkYfSjZPYaztUYgXOvYDP8asS2Qw4JAB50GHRJX2tWHU4409ZXrkCpmZqWA3aauxM7sYnRvpu-U0JA0CpVtsAk0sXhrF0Uc3MiqehtGKKE91IoimK7d0c6n012cMhm3WCgZxNrs5hd3lw5KcCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dd9ffa59.mp4?token=qukY35rezEVW87PoN1MOSZtMhQz66p1DPn0YBgJ4zMmMB3DQ6xuv3KPrclzJn6lr1hQoWCKUI7FipOt46LBDNnYhu8uhvBX0WFlF3GGy6PJB4xtoY7mdPr4peO7bsR4gy3AHSi7ZTn6xSQDTwLhTQcIlxhm93OIQtiqC7I_Xk7rJjz_a5_cdT1vMkTqXLhx6EdBUWkYfSjZPYaztUYgXOvYDP8asS2Qw4JAB50GHRJX2tWHU4409ZXrkCpmZqWA3aauxM7sYnRvpu-U0JA0CpVtsAk0sXhrF0Uc3MiqehtGKKE91IoimK7d0c6n012cMhm3WCgZxNrs5hd3lw5KcCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر مردم شهرکرد از سخنان رئیس جمهور در سازمان ملل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 651 · <a href="https://t.me/farsna/464015" target="_blank">📅 22:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111b48b8d9.mp4?token=Kr5x01tYHC19uvbSIAsZK47G7yQIDDZ4aGvaHvQgo4om2jtzgK0MxGQXgKTs1y8ThISzEbruFvUo6Lcxne-nVSHNo2MMoiliHnFWYRHNa-vKpNL5qDPpGgRaizvl1lGFRzHwW1tMaqYIolce_yL4K09eZTW3QsnDBIzfh-nxCH2wS1WC9Kp6bv-9rG8OfjxNtCUmeS8ZgH5iWccLYid4Qlg4AMeW_MWgOefsA-d4mjyYYz1sFEx4vL5OIgAHhkaMz9VyuP1jm8LxFtomA4ViokplscZ3SNvXJIKKYBg8AOID8WY3g15h_ej-EITmuafxOvCQuawtMtoX160cXhe99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111b48b8d9.mp4?token=Kr5x01tYHC19uvbSIAsZK47G7yQIDDZ4aGvaHvQgo4om2jtzgK0MxGQXgKTs1y8ThISzEbruFvUo6Lcxne-nVSHNo2MMoiliHnFWYRHNa-vKpNL5qDPpGgRaizvl1lGFRzHwW1tMaqYIolce_yL4K09eZTW3QsnDBIzfh-nxCH2wS1WC9Kp6bv-9rG8OfjxNtCUmeS8ZgH5iWccLYid4Qlg4AMeW_MWgOefsA-d4mjyYYz1sFEx4vL5OIgAHhkaMz9VyuP1jm8LxFtomA4ViokplscZ3SNvXJIKKYBg8AOID8WY3g15h_ej-EITmuafxOvCQuawtMtoX160cXhe99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکای مردم دیار حاج قاسم در قلب کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/farsna/464014" target="_blank">📅 22:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3IPmTtw4DrIHxkpiqyrkGkbMdtm9BVuy7IJuHQS_UoQebYDGcnahOOLyyV8J-8fdk26Rp822nxY_LJQhkz37smxvqkkGQ7H4-K_QStXXI_FhfmkGjhJLI59aBuq1emav0kq1fMz0gBR8zla-mYdUw-P_ZiMcZ2b5P_Ca67uBTEY4a06-tbdwfLke_UzEtcrrO9WX4MCLZf8bM6C80nGssC9zNDQEf7T6tJo4OkbbnMqcjpBYlyHV1NK5v8eyd4_pdZvsyVJlFuZ2TgWHEIHO21JTh2zKGPUwjMDnc1CzhyLRAiUoJn2LBTqB-zRHzy5l_LrjZ3Ul2tqNu6zCA7qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع خبری لبنان: جنگنده‌های اسرائیلی به حومۀ شهر القنطره در جنوب لبنان حمله کردند.
@Farsna</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/farsna/464013" target="_blank">📅 22:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c274c1a0.mp4?token=BVtxW75PtbGqdjilDdkMtTzj4lzZ2vRo6Wgjzu0EeEZebyzn8pUSaYX5rVL6Q4Td0Kv3FrSlnY5Fw92BCcaY2BVZP_EVYdLNRgM8jVEsDNEk8hnlcGW6z0rwoWyVxlbL1t6GuUMjvbKYqqrX8Sg6MJWysRihU1BtVS1r0EJ_L51FgkrhHR0BTUh_NBRXbG2ZuLN32hB4XpiCHuJ2weEak_KVln7FObOcMgaqsKZ2puedwV2cOfdTYZOAluhsCJwHk_OJS7cZm-5MyPiy32Ua9JUfElQNMoV_uo4XP3quW1kyDaHYnBZMu5Uz9qGiXjKqBEwRZ_HyxS7LRXJNYX4XEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c274c1a0.mp4?token=BVtxW75PtbGqdjilDdkMtTzj4lzZ2vRo6Wgjzu0EeEZebyzn8pUSaYX5rVL6Q4Td0Kv3FrSlnY5Fw92BCcaY2BVZP_EVYdLNRgM8jVEsDNEk8hnlcGW6z0rwoWyVxlbL1t6GuUMjvbKYqqrX8Sg6MJWysRihU1BtVS1r0EJ_L51FgkrhHR0BTUh_NBRXbG2ZuLN32hB4XpiCHuJ2weEak_KVln7FObOcMgaqsKZ2puedwV2cOfdTYZOAluhsCJwHk_OJS7cZm-5MyPiy32Ua9JUfElQNMoV_uo4XP3quW1kyDaHYnBZMu5Uz9qGiXjKqBEwRZ_HyxS7LRXJNYX4XEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از اولین داروی حلال برای کودکان و داروی پیوند کلیه
🔹
وزیر بهداشت: کمبود داروهای اساسی از ۶۴ به ۳۲ قلم کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/464012" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909ccf2b29.mp4?token=tUI1aZSp1tV-cllk91VXcuaWnpKyUn5axjIqGnmmq50GPxC_nkj-lCUKRXangsvmZcLY4lYz_zZKcIWZaDwvN0dOSi150RddyWATwc1OuqNoezd-R_917jzcZohXeyHY4BpUhq4jillfvn2iOPxsrRHY439_uHn95acyxsCSrar__daGF9S0S02Quen-Vd4QRPRW_Tmk8T6fdzCYleAwAwAEIOIJBnNvyuDrVM9XRDxp7QYynbbjdG1sOMzGYMjnArRC1m0BfxZSjvd-fG5NgF8LWLrUT_LbfGL-fHvOfY3kgXJAOHhaTd1bc0qdZEdK6KOOA_hb75jaktpEeCKFdhJA4G3yU972_f5b83bIqwVTlUslDAlbxCYMmDOrInH-M2opE6pRj-n6Tmjp9een2JbskVsRHl89RdYXGBwF1EXrOrgP8CDzdAyjUjdbDP597k1yRP4OS7cSkTNT-IqlDeVrvab7wrXFKxBuaJN5-x6KC-b9LrNgVMCQpZcAaeRvMdBvH3o2CpBpZuBfHsR45024KKILVH0Lyox2Y4_iXBPyGV56ezJh85Zkr0LO6A_uFZ6qkrIEIW5aF1G-rG2TnDIstjDDWeLEGWjstMDYtaDvz_5F9viADx4QxK79v8aiIoFpY0L2vG_azfroUbQaP6xMxSFl2dejQkSJaltkhSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909ccf2b29.mp4?token=tUI1aZSp1tV-cllk91VXcuaWnpKyUn5axjIqGnmmq50GPxC_nkj-lCUKRXangsvmZcLY4lYz_zZKcIWZaDwvN0dOSi150RddyWATwc1OuqNoezd-R_917jzcZohXeyHY4BpUhq4jillfvn2iOPxsrRHY439_uHn95acyxsCSrar__daGF9S0S02Quen-Vd4QRPRW_Tmk8T6fdzCYleAwAwAEIOIJBnNvyuDrVM9XRDxp7QYynbbjdG1sOMzGYMjnArRC1m0BfxZSjvd-fG5NgF8LWLrUT_LbfGL-fHvOfY3kgXJAOHhaTd1bc0qdZEdK6KOOA_hb75jaktpEeCKFdhJA4G3yU972_f5b83bIqwVTlUslDAlbxCYMmDOrInH-M2opE6pRj-n6Tmjp9een2JbskVsRHl89RdYXGBwF1EXrOrgP8CDzdAyjUjdbDP597k1yRP4OS7cSkTNT-IqlDeVrvab7wrXFKxBuaJN5-x6KC-b9LrNgVMCQpZcAaeRvMdBvH3o2CpBpZuBfHsR45024KKILVH0Lyox2Y4_iXBPyGV56ezJh85Zkr0LO6A_uFZ6qkrIEIW5aF1G-rG2TnDIstjDDWeLEGWjstMDYtaDvz_5F9viADx4QxK79v8aiIoFpY0L2vG_azfroUbQaP6xMxSFl2dejQkSJaltkhSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای موافقتنامۀ انتقال محکومان توسط وزرای خارجه ایران و کره جنوبی
@Farsna</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/464011" target="_blank">📅 22:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHwzyt8cSRFo8hCPOOgtY7IbHKTCqwlKcRX6nt__AwgcdG3nfMf5ib22tAl9IQ7Irv4G1i-GI43I8hSVFWAeJPcwRY7AeWsx7qH8DBGBv7elshV_khx9KQbouK58PrkZAA2gN_Tx-LUB7K9E_b_WhA7lUR5u01q1B6CcnZe-x8BbLl_ErmTRSAtHwpkdwTUEyfs2v3k-qY271_QGGudvrUQJynNOPy0uDE1eY0xRl4p8zywtPTdeeewquPDNyGZu0QYsg4Y_zmtXm229yXYf_4vXsV7udUzS7kVNyGroAdLCtrfmOp2AqyGkBV5lNNnCdup7G6zJICqtVtKYdlCwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدیمی‌های تلویزیون هنوز برنده‌اند
🔹
آخرین نظرسنجی مرکز تحلیل اجتماعی متا حکایت از آن دارد که سریا‌ل‌های قدیمی تلویزیون از جمله «متهم گریخت»، جز پرمخاطب‌ترین‌ها هستند.
🔹
در آخرین افکارسنجی منتشر شده از سوی مرکز تحلیل اجتماعی متا، سریال «متهم گریخت» با 37 درصد، پرمخاطب‌ترین مجموعه نمایشی مردادماه ۱۴۰۵ اعلام شده است.
🔹
در این داده آماری به ترتیب، فصل سوم «آقای قاضی» با ۲۵ درصد، «مختارنامه» با ۲۲ درصد، «خداحافظ بچه» با ۲۱ درصد و «الگوریتم» با ۱۵ درصد بیشترین میزان مخاطب را در بر گرفته‌اند.
🔹
این درحالی است که به جز دو سریال «آقای قاضی» و «الگوریتم»، سایر آثار متعلق به سال‌های پیش تلویزیون است. «متهم گریخت» که به عنوان پرمخاطب‌ترین مجموعه نمایشی در این افکارسنجی عنوان شده است، ۲۱ سال پیش از شبکه سوم سیما به پخش رسید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/464010" target="_blank">📅 22:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار کنترل‌شده مهمات جنگی در جاسک
🔹
فرمانداری شهرستان جاسک: فردا از ساعت ۸ صبح تا ۱۲ ظهر احتمال شنیده‌شدن صدای انفجار در محدودۀ شهر جاسک وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/464009" target="_blank">📅 22:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
پارسال لحظه آخری به خاطر جنگ نتوانستیم
حج تمتع
برویم. پس از سال‌ها آرزومندی با این
افزایش خیلی زیاد قیمت دلار
باید قید رفتن به سفر حج را بزنیم.
🔹
لطفاً مسئول رسیدگی به
وضعیت پمپ‌بنزین‌های استان مازندران
را معرفی و این موضوع را بررسی کنید که جایگاه‌های سوخت، به‌ویژه در مسیر نوشهر به مشهد، سرویس بهداشتی قابل استفاده دارند یا خیر. در مسیر ساری و حوالی آن، در چهار جایگاه سوخت با سرویس بهداشتی نامناسب یا غیرقابل استفاده مواجه شدیم. واقعاً تأسف‌آور است که در مسیرهای پرتردد چنین امکانات اولیه‌ای وجود نداشته باشد.
🔹
۲۰ سال است برای خانه در
تعاونی مسکن میثاق ماهشهر
پول پرداخت کرده‌ایم. با پول اعضا خانه‌ها ساخته شد اما مدیرعامل و هیئت‌مدیره شرکت برخی واحدها را فروخته یا اجاره داده‌اند و ما
همچنان مستأجر و سرگردان هستیم
. در این مدت برای پیگیری موضوع نیز به مسئولان مربوطه و اتاق تعاون استان خوزستان مراجعه کرده‌ایم، اما هنوز به نتیجه‌ای نرسیده‌ایم. واقعاً سؤال ما این است که آیا بعد از ۲۰ سال مرجعی برای بازرسی و رسیدگی به وضعیت این تعاونی وجود ندارد؟
🔹
مدتی است که
لاستیک دولتی
توسط شرکت‌های معروف داخلی
توزیع نمی‌شود
و درگاه‌های فروش اینترنتی بسته شده است. قیمت لاستیک هم در بازار آزاد خیلی خیلی زیاد شده است.
🔹
خواهشمندیم صدای مردم
کرمان
را به گوش مسئولان
دانشگاه علوم پزشکی و نظام پزشکی
برسانید. شب گذشته فرزندم را همراه با نوه ۵ ماهه‌ام برای ویزیت پزشک بردم. با وجود داشتن نوبت حدود سه ساعت در محیطی نامناسب و بدون تهویه مناسب منتظر ماندیم و کودک به دلیل گرسنگی، خواب و گرما چندین بار بی‌قرار شد. پس از این انتظار طولانی، منشی تا دریافت ۸۵۰ هزار تومان اجازه ورود به اتاق انتظار را هم نمی‌داد و معاینه پزشک نیز شاید پنج دقیقه بیشتر طول نکشید.
🔹
من معلم رسمی منطقه ۷ تهران هستم. بر اثر یک حادثه ساق پایم شکست و برای درمان به
بیمارستان فرهنگیان شهید باهنر تهران
در منطقه یک مراجعه کردم، چون تصور می‌کردم با توجه به فرهنگی بودن، هزینه درمان برایم کمتر خواهد بود. اما در نهایت بیش از ۲۰۶ میلیون تومان هزینه درمان پرداخت کردم؛ ۶۰ میلیون تومان را مجبور شدم به جراح پرداخت کنم، ۴۶ میلیون تومان هزینه بیمه با احتساب بیمه دانا بود و ۹۸ میلیون تومان نیز بابت پلاتین پرداخت کردم. سایر هزینه‌ها هم مربوط به عکس، آزمایش و دارو بود. باور کنید تمام این هزینه‌ها را قرض کرده‌ام. چرا یک فرهنگی باید در بیمارستان فرهنگیان با چنین هزینه‌های سنگینی مواجه شود؟
🔹
در سال ۱۳۹۹
شهردار وقت مشهد
با مصوبه شورای اسلامی شهر، در قبال واگذاری حدود ۳۰ هکتار زمین برای ساخت پارک چهل‌بازه، به حدود ۴۷۰۰ خانواده تعهد داد که پس از اخذ سند زمین از اداره ثبت برای ۳۰ هکتار باقی‌مانده پروانه ساختمانی، ترجیحاً بلندمرتبه‌سازی صادر شود. ما از
سال ۱۴۰۰ سند زمین را دریافت کرده‌ایم
، اما با وجود گذشت چند سال
شهرداری
همچنان با بهانه‌های مختلف
از صدور پروانه ساختمانی خودداری می‌کند
. این خانواده‌ها بیش از ۲۳ سال است در بلاتکلیفی به سر می‌برند.
🔹
مدیر سیستم سوخت گفته ماشین‌های بالای یک میلیارد
سهمیه اول و دوم
را نمی‌گیرند. مگر ما گناه کردیم با قرض و بدبختی یک رانا خریدیم. بعد هم مگر
ماشین زیر یک میلیارد
وجود داره؟
🔹
ما
کارکنان مراکز خدمات جامع سلامت استان فارس
، ۴۸ روز پنجشنبه بیشتر از کارکنان ستادی بهداشت و دانشگاه علوم پزشکی سر کار هستیم، در حالی که حقوق و مزایای بیشتری دریافت نمی‌کنیم. با توجه به غیر‌اورژانسی بودن خدمات بهداشت و سابقه تعطیلی پنجشنبه‌ها، درخواست داریم در شرایط بحران انرژی،
پنجشنبه‌ها تعطیل یا دورکاری شود
. پزشکان خانواده نیز به ‌دلیل قرارداد با بیمه‌ها همچنان پنجشنبه‌ها حضور دارند و خللی در خدمات‌رسانی ایجاد نمی‌شود.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/464008" target="_blank">📅 22:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae2e5d0310.mp4?token=igops0-p90e8g5cGTxpA6YjV7qk90dQqoC2zlV_EN2FkEb1rmtvhM71wD4yoMRuCv_oOWpOj5UKeixwKx4jSYbLCBusnHVu9EOzaKtJX3uU1RGffo-G8Z9i5mOl28kEEbdLsdN_CV0Gp5tgxjRNjgxOwPQr0fPoe218srfllSOtHMAoxr8f4kDqh7kd_ZI_lFkqLrcadTOqVppWNjM19Okc2DcDCRHnxihF0B8z1Zotu68fy3JJRYR0ttesbqj6NYzt60LDi5ZUJjdmdk279MsKTPPC8s0NrMn99wfDpZBkk42pHmn4ePovJb2T_RDuGYlolYSpu2Y1dcsYniSB7Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae2e5d0310.mp4?token=igops0-p90e8g5cGTxpA6YjV7qk90dQqoC2zlV_EN2FkEb1rmtvhM71wD4yoMRuCv_oOWpOj5UKeixwKx4jSYbLCBusnHVu9EOzaKtJX3uU1RGffo-G8Z9i5mOl28kEEbdLsdN_CV0Gp5tgxjRNjgxOwPQr0fPoe218srfllSOtHMAoxr8f4kDqh7kd_ZI_lFkqLrcadTOqVppWNjM19Okc2DcDCRHnxihF0B8z1Zotu68fy3JJRYR0ttesbqj6NYzt60LDi5ZUJjdmdk279MsKTPPC8s0NrMn99wfDpZBkk42pHmn4ePovJb2T_RDuGYlolYSpu2Y1dcsYniSB7Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: در حد توان تورم را کنترل می‌کنیم
🔹
مهم‌ترین وظیفۀ ما درحال حاضر این است که نگذاریم معیشت مردم دچار مشکل شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/464007" target="_blank">📅 21:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464000">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stFe91rbjCb9UHPGOb58sMuQj9gE2VWGIAOlTBZga56rdflPXkV9u7fx0hBUNYIYKwKiUo4g_AZ2lqWxPawLCmyvd-8iutEkLKlFoX1nihKletDsMtAk7vzPPREEzCaQj0LJ8KnyG4vZqUqjc0Dyp-7FF3XHrS_7LgmgUoRxagjbX_8l48MN9KefaUnZkdaEMlitKEbhThQrl3SJCyur1stdNVRCNJFGnwFyp82y8nrqjYG6TpjAROqgYQpqsf0y9G389710QvIWez9wC5_quV4nWuQaDX5ztRi3blxskwDTcgfho5yt0s8c734N503TKDcc1Lx8p25PXV-KKGp0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilE0bpSmvWHVBnEeuncC2agAS8VW3a9GF_93IGvz2o9e5q4pdYp6hhOgkfbcGrNH1rmNpe60a8kU7RYy9DpYDWI0s2cwYfEV8AlKjYWdghwOTWHT-ldGvOUm51vmxByATni_R2hZD7Svs1KkOQr2IZBOc2jB3jUoa5JUD0KV0aeOzLpdJtEQRJ60soMbYZHPjzFB1QnXJpTzxI3_W1EJHKYb6Kve7WRlH1F0XE3xpAWeECbqHVfeiJtPEUc2Kngmew2RhpWkbXAYgvlHLdPrzNdklmI70nBy2TBBEvU3QXO-ByeXKHlQA5TTma02K5UCB40moAGs3sKrpeyB6HCGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHrPJFm1qRPpr9l8uzpM_GDrk98G8-zoQ7cJd_hlP723ABiTriBMUOeCH07jY7ZfYx3jNW5kxYKQPHiVqb5QfzVYNQoKztmVCHTJr_GMmMJU0NblORJ0RwiBuhDGo-jMLPt2LXArn2uoD_raG76K5dsV3W0Imb_B6PH9IN7Kt_5mngOBcRXmowAncIVvYO7lqaFC7szIY7etLb7mHkfjqxV9Pfo072-oDeJJ9G5XlyVzVtOzZ8RDtcbU_pluAm90K4Fi8uZMKHYM2uVfYld2ksQABq6NNh3kHNnpuQEeZ70VpcCKKtHt-lBA61Z_LkfoxWsAJe9xxsX-XAvg3wkhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxqyPnv_5z8B88UygETia7Fi7Wm6oeGYmN4VLE7MyWTi6wPO-JhAKztEaCq4zLAd2A6KbupmaB7gaPXuGozdCOqYDc6aKhAZONPg_0GUu7SmsVrqivttY1toCSfs50nWqooH0B0kwpo54Elnhm6x6aLYnl1UNQXI70MEht1ezn9lyGVXtXiHzIF6d4go4tLSOzXRObG56KAfwAeS_-9dqXY2kNGabPH1brwRDy-bpE_OFKeqFOx0ydfzCW972zJWrigUcbFyqpQu33VEqzkiG_4zn8Tuh7xWLzbqoBBO2AFys7TcKiQsn_BZfspkOfHZmw1sD-znBE19_lNpsrJwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQ1Zjz5Oa7ySJIrSen7DKR-fF7c1m1urAZYiPkz1LiYv-8szJ51Kp3YucikIRoInjrxFmWVDqJO8_Hl1uRWlXu2slbmWE_CDzfaI3mwzaIWOwbaWtH1smiS_VppwuFwaz7LaaamD8W-8GVO9RL2zDM41SqTKT9Dggtx99za77nYVJkJKDCuIL65tD3PNNPW0dWe6qikeRcIxodaTvkU9N6o54u7XeZ6Cg2QLwWPANFy3ep6kzpdV47v70hRbGUfevkApOTpiTAu2fiidc7amV2QIItSogx1RRvS6gxt-iulJtCqBfu4hpXGIqXUV1K0WKpKaxBxS0bKzyEmJnc1gZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgEwe5Pa2niZ16c8eFP_YlAcvhqtNsPSX4CrB8uCRJ3_o3CuLtBYZiZMqYPhrHUUlOt-J3AHwHsIdBKebu13QQffGeR6535KRs8Zz5xtd2UspASCjkRR3BPdC-o1n0HDkOYLg1Pp1i0DVFbcA_x3whuQ3rMH3Hd2LEIiKHlzBANshd1S5W6hF8Q1hIIjmUNxaHWmrS6Baf22P4g_ZwyUJi7RBIj7RuCYFLCM5SyZtQmP5IStHcUMrEQ5t2hc177kZTAow4Vnqp3_8xRfk5PX0TEX4HQ9PWyAR6EGTVds9VZRaSeeGPBR_Amy5z5Ohz1k49P5K4C_D8FgXU-Bzm8nxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSqVeDuVkquQpK0yX6ydqV9HU3rD-blLc_VZ3Dii3ffqSNfRxbn1zFqF2e_EaUonra7YB5PW3pqC9hvq-SEALIF1BGeZUgUjPYaXZ9gd6BZa5z-uAYwMggcp8Cq99XsYWfWdNMTwwtCm9vhDsiKDSSfOSFjJ19s2TuLDnjNOfL-Bdr08XqidU9aRAR2P_9y6bm1Sb4poeK0ukW7zKSEltLnJoY9RBB5YFQR1wy_l_nCAJ59y2oX9dlGntTZJwlsUuraDCJHJm91qw00y0OzMAFo6sViHQSFou4IaxpaWlMwUIfsa7ljiuvpcZQTJ6lD4Pb8C3GN5Pk_uM0mf1Y69Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم ترحیم آیت‌الله شبیری در حرم حضرت معصومه(س)
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/464000" target="_blank">📅 21:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463999">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e99c01a7.mp4?token=Bdc-c2135jhnL5VFmGgIPxe0Q3eFaYJb9Rv83eMNif11OdrpIFzlqGUbcJZleg5fDDV8JbPvHmVv3xC203xyQsaxXvXYnU__7PzT4r61th0y9KO-4XghQytMalkuWrgPUTD_VJ3lLW9nwYM6BUP1k4GuWNY4HhCUw69wDiva6d-uXH8CVf8935NVx913xBKSC3bs9LTWinqMJoOJs2MZ7bDrw6uQwdjONoMt2nytygf2Znz_vgslDwIZSsFbgeParXqKKCoQZUqtmnDKF8s_wZtRplT6XcQoPWPxRPvobsD-Ff5XOC3SJPSqbWaR5rlK3hXPDVuHAhCSAjfzCaS_OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e99c01a7.mp4?token=Bdc-c2135jhnL5VFmGgIPxe0Q3eFaYJb9Rv83eMNif11OdrpIFzlqGUbcJZleg5fDDV8JbPvHmVv3xC203xyQsaxXvXYnU__7PzT4r61th0y9KO-4XghQytMalkuWrgPUTD_VJ3lLW9nwYM6BUP1k4GuWNY4HhCUw69wDiva6d-uXH8CVf8935NVx913xBKSC3bs9LTWinqMJoOJs2MZ7bDrw6uQwdjONoMt2nytygf2Znz_vgslDwIZSsFbgeParXqKKCoQZUqtmnDKF8s_wZtRplT6XcQoPWPxRPvobsD-Ff5XOC3SJPSqbWaR5rlK3hXPDVuHAhCSAjfzCaS_OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۷ شب ایستادگی؛ زرندی‌های تا پای جان برای وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/463999" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c92bb3d.mp4?token=bZ7x3eOfzd24-NcnHtbc0c1LMDGI7OyX45Ib9tXzdJ3o_X36o6azqIZOEl9nyAKqn0fhYfNwoMW3cB31CzrGYSRoUmkRY0GBoMb6URyR0Z-UYynag6Ms6ymgDTmanh9CgexpxWI9lcgrDhvt2fs63BiaMcqn3NTuawuhzEt0ZSgC3kL7m6wK3S7awHgR1VQY09bJ-b1exb1QwhEz1FJ36l67oyQuuX6a5B4-zVP5updMj8cI84rXYDOUTseS5inLOgsRpjatgMoHA3mOGbYWx9EwaQAznH5COql7JV8E6MUeDoUi_hOIx-Gpgvwwmtpver-0aqU4Ju6lFdSYfn-RVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c92bb3d.mp4?token=bZ7x3eOfzd24-NcnHtbc0c1LMDGI7OyX45Ib9tXzdJ3o_X36o6azqIZOEl9nyAKqn0fhYfNwoMW3cB31CzrGYSRoUmkRY0GBoMb6URyR0Z-UYynag6Ms6ymgDTmanh9CgexpxWI9lcgrDhvt2fs63BiaMcqn3NTuawuhzEt0ZSgC3kL7m6wK3S7awHgR1VQY09bJ-b1exb1QwhEz1FJ36l67oyQuuX6a5B4-zVP5updMj8cI84rXYDOUTseS5inLOgsRpjatgMoHA3mOGbYWx9EwaQAznH5COql7JV8E6MUeDoUi_hOIx-Gpgvwwmtpver-0aqU4Ju6lFdSYfn-RVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی: امروز حتی ثروتمندترین کشورهای جهان نیز نمی‌توانند به اندازهٔ کافی موشک‌ رهگیر پیدا کنند
🔹
میزان تولید فعلی صرفاً کافی نیست و حتی کشورهایی که سال‌ها صرف ذخیره‌سازی موشک‌های رهگیر کرده‌اند، بخش زیادی از آن را مصرف کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/463998" target="_blank">📅 21:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p22hXU6A7WJlBC5Mp9bqHdo3dSfN1AdTEcfGUOBY_x0GeB5ibucvwn9ajVB3mbO1eN-Yrpb_pdRB1Vaymc7sNp7s9nGFxLllFYP3KjXJyV78YKtC7tgxSlb5hanwtgKXbsewlrWPPADvRjx6ey1tsNMm2n34nOQRlkv8REhRBBnmOqVlDhhZgOkHAHYehIX6XKuQaF7psxfauqpOXi8MgnQZrSA-jhrZK7a5bnRi_KIVfHyc83uu48gHaHD54EmmAi7smQKuXxj4L52D3D3e12s0SgdMaNEux0lAJmqwYxdQr1cP-j8VyxgBnqaMrRUK2F3W9-KASNlWsfY9t_4rpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi7kmVhNDVe4jP0-P0atVSWN92nkGt5JY1hJd-5LQk3MmehzJ-H9BOCnWC3AgdZKP4azKEpa8UBazvIKf2QvW8RFLt5Bs8CpEhEtWqDxQiG0VD1VOYYXpf7DAUGEAAxu_lguh72ukpMdKMJxSFjLRxajRmRp8qNzYn1Ntgc9wG64H-pwthFbWHRsPZoVU1juJQhXaHLJ14R0LGqrmS6lYuckkMuPk6FefxQRDM31XedDnKsy_l66Rqp92NXMMcbqFQyIvKzV-H1kAcQI917tWtWGzY2XUX3xHesxayS7mt6OO5WiXNSgcFAsDn8UK3cbZuZzdbxY6meQfXkqUDl7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reEgvBMey0JT-nMvrOIUJcu0Skp9bi-Tt3yBLrxk-iZh--TnWgv1VJkJYlBhwaoSiz6gYd2pMkluf5zfe2VOq_SZwtKNZ_YPHIPlTOWC604WFDe_dByOWcb9_IWg0ONfsNsE3UBQsefXDf2PKYSAheUuW62EWUeL2-VnYCMwCjxCFNujfV86Qqx7VTkGdfYMunwbaOwzugz8YdkjtSFVVu-6XiPE8URBN-OmHkd4c5mS2PNziXOXS7lTdksUSu_hJoLSz_4UseL539XyUUBUGHassqY1HOukMuIqw3hw2K5-jW2J491klZaO2F-RRpSUYK3JJ88M5DGLX7n__db63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muAiEpCy-uaiKB2jKq8RsqF7L9on6a0fVkrdMXMLjUGPK9IkgnGliT1KxvluJEvRmHTpsvwKcmrniX9XmV_NAiwlbfFv3sN96pt5SNkxStgtvW68X3DLcZMDpuHqTVtfQzsFA9UvdDP4GWbMC29Oa5gtCc3ZtnIN376dH18vQ8skAHHogZc2c5F2DFCTiVTkzg97yD-DpV-AS8eWGsGH2G0TuzG7LTEGRmvVWVbsrPNV5B8MOxdaV_dQn1pwD3lRcVNzX-LrFHSY43Yseg7TdMbKPYKL4x4TO6n7TpYxxpUVjHkBhX3UgsFooeDp_66WzIi3HsxQUxloKCRb00DkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lwt_dfm5okM3eU22GEyNeSpYwMDdV_d1T3Be5glMsSMN5NreiyGCLhB4C75z8ARI6Obxvg28gwKUnsuOH8phLA9YxVB6AIqhiRr9qJsf1nOwo6qY1Xe2WUO9XXEicfQrHmU2tycdaafNYKRYcELan29PNpoVrN98n7VxUZBvkLSk3ctUrlIn2vtQ78R3lDuk0yCA4-4_Mz8YGrF7uJXWio81rKJua2QvzB822LvgsC1ecz8OZYx0CP_f-tNfY-Ty0ZaHD1wkDkvDQ6PdYcizGLpUAwRfvnDxxwq-9uY4K7P0IJ6yU36l4OB6V8QwXxIfaaRIYIG8fh5ARfBIJ0oNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiTFf0xJWF_VFISjIqkckv0JBTSOh3knV9kZrHKsV6z6nQJPN-ynUj0K01Fdt_C3xykhds2JF8XhQK4RcZaqDQYcDsX5HRArF9E0mmvmPYivHD9NuE2m7vyKKP7CMB5SnM5NO4oBfTkTGm33j9R37qctDjmp66KCFRDfFf-HVBEDZ73lhSAl_rVPdBOmAhKAqRhwZbJ-Hc0VLhIj0KDirowT2JBbZg-0Ovj76Ss_N9Ki8_daS4kVoLAHletnEvuRLUaQErqN5hxOdTvSQdcan34VyFCtH84_C2I2FjaLLX27QFrVZTlZDMG7m_3-8Iw6z2pcQ9QesyKrZPsU7Jpuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsDFsnwj0yDsQvPNBB86JRHQ_pIOn8BZ1alm0EvljdoSzZy5M-zm_iEYPt1nZTmQjQBJL6FrS_5tetYHCyumblsxtwII6OFNAx352i47ZWn86zobnleoTvK34HYgWiISAcKrzsyfFmHJ2WJjbwkU27mog9AjHXxOCMSZ9zqXe7qEG8fQkcAZ6uWeohg9WoQdw5HfogEP-nG5kOND6Y7ibnx5_lx9Th0hHsFli12bam603CtTj6jK1qxtYJuWZ-G_lcNSbnxcb6G44z-b0hhuNExr1YExCXCkASYrOp5aDj5rFZTLtUYqG9SF5RHexokjqEyzcmHVcNsH4qDm3Nj1Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قالیباف در جمع دانش‌آموزان مدرسۀ شهید آیت در اول مهرماه
@Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/463991" target="_blank">📅 21:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb12ebd04.mp4?token=eTnR2Qk86ttiEckHqb0no3fT2M5Z3AqRxUgsHR-984fCsY5kuc6MRMt6jDpn8hxpnmatKXdysxVXX1Y1gWFfH65I7_pgGWhenotbFwTUa_3ESATNA7rtuXAsT14ij9rlkDSQaEv_OrgEGRl8OwoIZxo5S6TWvMmFwMWlaMFsRPm5omPtw6yFQD4NjDxa6Yf80kuRJgq84xwJReN6OG2OZZwHajT4VZKrk-v1dwlKdM7p1nAmVehrplcpgqlxjw6FV1b7O93loCx5JrV7j7shr59M5YAAr_hC93ceR0xNQuQFqPtw8xJPVrGMZgFEdgr4PWFgZZmcd811KkiS9pvJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb12ebd04.mp4?token=eTnR2Qk86ttiEckHqb0no3fT2M5Z3AqRxUgsHR-984fCsY5kuc6MRMt6jDpn8hxpnmatKXdysxVXX1Y1gWFfH65I7_pgGWhenotbFwTUa_3ESATNA7rtuXAsT14ij9rlkDSQaEv_OrgEGRl8OwoIZxo5S6TWvMmFwMWlaMFsRPm5omPtw6yFQD4NjDxa6Yf80kuRJgq84xwJReN6OG2OZZwHajT4VZKrk-v1dwlKdM7p1nAmVehrplcpgqlxjw6FV1b7O93loCx5JrV7j7shr59M5YAAr_hC93ceR0xNQuQFqPtw8xJPVrGMZgFEdgr4PWFgZZmcd811KkiS9pvJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با رئیس‌جمهور سوئیس در حاشیۀ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/463990" target="_blank">📅 21:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0xnBnvvh6Qu9Dak8YgJBEhncd_mhEDBo5SzUv6XVdsaXGaoQNFHmmljMRYdjo9DYyEl6OXu25Bs_Kc0WPImBcvY6NBnpq2BTdhqvx_TY7hd2EOKhnKdeC42bXX8LHam9T1NuTz_Umfu-Ea2aYjciY3EkwxvML4xH3Mgh9lzYe_rQRf4ieZtk7kUofnRTFNF4lAq_BRIS3t9IFdb3xCE-2TIl2jND7ZxrRofm9w6IoME397jK6Cu1yOUiu1IsNn9c-SSuy7hYqHcmzxlruOqNivx8grngkHGQuhNoT_eEEQ5vg2eKrWwbTIUBlWzuxozJAwxFOnwr0fJ3pg6KSLCpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: رئیس‌جمهور پزشکیان صدای قدرتمند شجاعت، مقاومت و استواری تمدن ایران بود
🔹
زنده باد ملت سربلند و مقاوم ایران. @Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/463989" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79decdda7d.mp4?token=N9qcjmFyi1Gqq9DSu4xbGB_Px0dSk6cKWIIyLT5o4pORAmmzZF_U-gDKobZDkNG0P2OhwcnTaMGya3lxBzljPG4o3yeKQ2t0DPOd76bRf2vDRFcTFJ7y6Mdnchc_buITnlRpr13t97dzorXWJDToUlU0trXqu0F61X65xnsBViQ8DBs6YNr_AnuyuMEb4sDElfgXuREjhsv1xpBOUobqzf5QWV5vHDX9It6qdxUjMmO3skNKvjQBILD8BLp2-_aIBJieotW2mwVZtoFzZsLu54Xn8ISwEbO8V9tGLvkKowlksQ7bpJEX8Htgmcq7N6QHmX2JsQEkMZo0W_fNFf0kWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79decdda7d.mp4?token=N9qcjmFyi1Gqq9DSu4xbGB_Px0dSk6cKWIIyLT5o4pORAmmzZF_U-gDKobZDkNG0P2OhwcnTaMGya3lxBzljPG4o3yeKQ2t0DPOd76bRf2vDRFcTFJ7y6Mdnchc_buITnlRpr13t97dzorXWJDToUlU0trXqu0F61X65xnsBViQ8DBs6YNr_AnuyuMEb4sDElfgXuREjhsv1xpBOUobqzf5QWV5vHDX9It6qdxUjMmO3skNKvjQBILD8BLp2-_aIBJieotW2mwVZtoFzZsLu54Xn8ISwEbO8V9tGLvkKowlksQ7bpJEX8Htgmcq7N6QHmX2JsQEkMZo0W_fNFf0kWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بجنورد در اجتماع امشب میزبان خانواده شهدای میناب بودند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/463988" target="_blank">📅 21:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579850fb0e.mp4?token=TBee5jkllklEGCaanx3_n7C-uTx825lpA850v2xblUgHTkcxK54YEmUUTeLT-cKzVOsTMi0LWVfI2S1BpLJ33Ustkx0ERUcKGbiHmtYFH9r-C1mlKCkZRgn0LEmCZ0idxJPhXStMpeb4DqZyxpn0Sgu8WopYLQ3EKRQDask_XX2yFFizXtrcosjND0b3bTwOyDFB8WzE6uL002ZbzYK_5Ab4OUk4h4Yrl1KRDhKoDyCFt6OaCUgwys6vO3Av-yeVNnSQr7qK6hhrJ6Xso5cbJ6JCyEcgV7jgdiRu0ejeheh-B-ZV5Oh-yEZ5pCaAOX5IBpPXyXhnkHYbmea0kib2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579850fb0e.mp4?token=TBee5jkllklEGCaanx3_n7C-uTx825lpA850v2xblUgHTkcxK54YEmUUTeLT-cKzVOsTMi0LWVfI2S1BpLJ33Ustkx0ERUcKGbiHmtYFH9r-C1mlKCkZRgn0LEmCZ0idxJPhXStMpeb4DqZyxpn0Sgu8WopYLQ3EKRQDask_XX2yFFizXtrcosjND0b3bTwOyDFB8WzE6uL002ZbzYK_5Ab4OUk4h4Yrl1KRDhKoDyCFt6OaCUgwys6vO3Av-yeVNnSQr7qK6hhrJ6Xso5cbJ6JCyEcgV7jgdiRu0ejeheh-B-ZV5Oh-yEZ5pCaAOX5IBpPXyXhnkHYbmea0kib2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با نخست‌وزیر عراق در حاشیه اجلاس سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/463987" target="_blank">📅 21:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79e1a0646.mp4?token=pwrPH2tW_XNDI2rl-c-A5u4Mq8qZYRoFwIAjl8S6ThyXDVPEAIBZ-M52ZF9HnAjNqEHKj3c6MVdMLdmkek6CJQrf8cUuur3eFRoFbefhM1W9elOCzqXCrB9FOJqIvXCBynbOlGnxKhbxv74GK-qvZj-lihwvhMLEBvJT1PaIFwlodyvFhiVA-1wWJQ6cfwWo1vHvSyUMDT4P7GexsK_rAAm9WN6L-vWvVEK5m_wdOnAPO12bI44zMSj2S-pGfNUnftYuh1JrJYUvV7MvUQMphaa3oztu6BA2oSqcJe1BMm4JVMAGZrah81ueAdxliFx1uRLtkp6DcsxBRrg8K8EC7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79e1a0646.mp4?token=pwrPH2tW_XNDI2rl-c-A5u4Mq8qZYRoFwIAjl8S6ThyXDVPEAIBZ-M52ZF9HnAjNqEHKj3c6MVdMLdmkek6CJQrf8cUuur3eFRoFbefhM1W9elOCzqXCrB9FOJqIvXCBynbOlGnxKhbxv74GK-qvZj-lihwvhMLEBvJT1PaIFwlodyvFhiVA-1wWJQ6cfwWo1vHvSyUMDT4P7GexsK_rAAm9WN6L-vWvVEK5m_wdOnAPO12bI44zMSj2S-pGfNUnftYuh1JrJYUvV7MvUQMphaa3oztu6BA2oSqcJe1BMm4JVMAGZrah81ueAdxliFx1uRLtkp6DcsxBRrg8K8EC7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌تنی افعی شاخدار در آبشخور پارک ملی سیاهکوه اردکان یزد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/463986" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ پوتین را به نشست گروه ۲۰ در باشگاه گلف خود دعوت کرد
🔹
مارکو روبیو اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، ولادیمیر پوتین را به نشست گروه ۲۰ که قرار است ماه دسامبر در میامی برگزار شود، دعوت کرده است.
🔹
در ماه آوریل شایعاتی منتشر شده بود مبنی بر اینکه ترامپ قصد دارد رئیس‌جمهور روسیه را به این نشست دعوت کند؛ نشستی که قرار است در باشگاه گلف رئیس‌جمهور آمریکا برگزار شود.
🔹
روبیو نخستین مقام آمریکایی است که به‌طور علنی این خبر را تأیید کرده است. او روز چهارشنبه در جریان مجمع عمومی سازمان ملل در نیویورک به خبرنگاران گفت: «اگر فقط با افرادی دیدار کنید که با آنها موافق هستید، این دیدارها بسیار خوب و خوشایند خواهند بود، اما هیچ اتفاقی نمی‌افتد.
🔹
«برای حل مشکلات، باید با افرادی دیدار کنید که با آنها اختلاف نظر دارید یا ممکن است با آنها مسائلی داشته باشید.
🔹
«بنابراین، ما رئیس‌جمهور پوتین را به نشست گروه ۲۰ دعوت کرده‌ایم. فکر می‌کنیم این فرصتی برای اوست تا نه‌ فقط با رئیس‌جمهور ترامپ، بلکه با دیگر رهبران جهان نیز تعامل داشته باشد.
🔹
«امیدواریم او این دعوت را بپذیرد. اگر این اتفاق بیفتد، در ماه دسامبر فرصتی برای این کار وجود خواهد داشت.»
🔹
ترامپ همچنین در سپتامبر ۲۰۲۵ گفته بود که ممکن است شی جین‌پینگ، رئیس‌جمهور چین، را نیز به این نشست دعوت کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/463985" target="_blank">📅 21:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ4N4Rc2Yv3u2Fa7Wf2cUYIUO6L-GaYUt4Unuqc41XMlhmhm-TSinl1MqyXxdm6inXNq0FosK2Pr4qAJhTlMA_aMcY5SjKMldEh6d8c_HEaHdwUqcnudZK9zNOmhPranrS_LgjfcvJ-z7EYOy7dREcH4CBrtkmIVfqcbjegC-FbiNti3tRu9bCRvjhiXwInRHPxnWN6k7YNpWxiqr4LxSfQRWoWY-ojdpVAA4E7UowizWrJ_egKBJokfrAeuH0cvkAk0O04GpvR2H55UXgj7FnWFnywBPmpw8Hz5Y-oJypOzuQCEbZdQAVSip3t9HBjjY3sc3pdWL6w-69-yWizdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به‌ دنبال ممنوعیت ۹۰ روزه صادرات گازوئیل برای کنترل قیمت
🔹
به گزارش پولیتیکو، دولت ترامپ در حال بررسی طرحی برای توقف صادرات گازوئیل آمریکا به مدت ۹۰ روز است؛ اقدامی که هدف آن کاهش قیمت سوخت در بازار داخلی پیش از برگزاری انتخابات میان‌دوره‌ای عنوان شده است.
🔹
بر اساس این گزارش، قیمت گازوئیل در آمریکا در شرایطی که جنگ با ایران و حملات اوکراین به پالایشگاه‌های روسیه بر بازار انرژی تأثیر گذاشته، به میانگین ۶.۵۲ دلار در هر گالن رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/463984" target="_blank">📅 21:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9947a74c6.mp4?token=p2-xLL9VstCBWofYAtHDxMq8dep9_Qy3MEhnklcRTdH0FmpioNb-VZUJwSQLrLxPQowBlklWBXqAwCkJ9BR2gOduXbu8Jw8JxS6a7K2ptCor-bNuYAoWREUi8MwAF0uqpqavxJ935p4bBvXNbwvkVYW3h5gnGCGLCmixrTtvB8OvOLUfOmnUbFlsVYUzwI3SSnRe6WMe-s1N_iDIA_78YGnq8J3nPZNvN_J4BplrWgMBt9wCliQF2cK6q81prK5DVdDgQNGRC5DNuyy1J76mkYwGdPnNFpMx4M7Wr7D_afwsf2DO2dBbrPXOmUXYjVMs0zoRfYlJRnGyawJufIn35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9947a74c6.mp4?token=p2-xLL9VstCBWofYAtHDxMq8dep9_Qy3MEhnklcRTdH0FmpioNb-VZUJwSQLrLxPQowBlklWBXqAwCkJ9BR2gOduXbu8Jw8JxS6a7K2ptCor-bNuYAoWREUi8MwAF0uqpqavxJ935p4bBvXNbwvkVYW3h5gnGCGLCmixrTtvB8OvOLUfOmnUbFlsVYUzwI3SSnRe6WMe-s1N_iDIA_78YGnq8J3nPZNvN_J4BplrWgMBt9wCliQF2cK6q81prK5DVdDgQNGRC5DNuyy1J76mkYwGdPnNFpMx4M7Wr7D_afwsf2DO2dBbrPXOmUXYjVMs0zoRfYlJRnGyawJufIn35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز بر پیکر آیت‌الله شبیری زنجانی به‌امامت آیت‌الله سبحانی  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/463983" target="_blank">📅 20:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f070b601e5.mp4?token=PStaxrXprKeyqNaVcXi-g0jJbqS8z_mMmdCrw3WEZEXKrYJO-x6YOzS47amBmhh60reIKmIp-Bqzgk-5GxkNzfqgikVM4PNrn7EnU7NSZjZ_YDnnTdOnoFU45Yr2lc7P22_h1DTIlA7tc3QCVhdI23_EsQnUNy6T_G6MAUmYIXTOISl1yrVcUd62rp4a4MB_RGE0ZsiM8QoN_x0EFZ8JqJdGDpbRXBBDMXZbExY0wwOwi15kaN5ww5apkQAGQLTfNvuR--7dl8R1k621La3BrqMx0KLKRDLzbij4mZKGJh-URxtA9cSzk41pjClRFtcyzeYmUhwtiqJ0BEdOD-1AQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f070b601e5.mp4?token=PStaxrXprKeyqNaVcXi-g0jJbqS8z_mMmdCrw3WEZEXKrYJO-x6YOzS47amBmhh60reIKmIp-Bqzgk-5GxkNzfqgikVM4PNrn7EnU7NSZjZ_YDnnTdOnoFU45Yr2lc7P22_h1DTIlA7tc3QCVhdI23_EsQnUNy6T_G6MAUmYIXTOISl1yrVcUd62rp4a4MB_RGE0ZsiM8QoN_x0EFZ8JqJdGDpbRXBBDMXZbExY0wwOwi15kaN5ww5apkQAGQLTfNvuR--7dl8R1k621La3BrqMx0KLKRDLzbij4mZKGJh-URxtA9cSzk41pjClRFtcyzeYmUhwtiqJ0BEdOD-1AQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است  @Fasrna - Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/463982" target="_blank">📅 20:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00c1412f7.mp4?token=AZJ6zinH_z1piFoHP9Bk3Fcrjecojac3KipKObhfSc4svcmjghvtrquWjWwc-27_s7i5Dik_g19FnNZifaybC8pH0IV9eMbDFBRpWjf1u6dwl9RDHi-84BzsSnR1Bv1ivKbigJwvTD3oOf4t9B_oYnTp7YR5WCwEnmrW7SWEoGS9vKoMR45UfYxpM1dQpF6kQpALWbzwVymYiMF-7OB2J_AKRDs8gQicBDWdbRBjO2nluwFYggq_U96OnfDidjYuEcnNJlrI50XULKnoVxkGcl9twnW7QztCp7gNeX19i-cENRL-bS3KgfbF9XMltKuk4CfAU38EcMrrOy7Dp8_-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00c1412f7.mp4?token=AZJ6zinH_z1piFoHP9Bk3Fcrjecojac3KipKObhfSc4svcmjghvtrquWjWwc-27_s7i5Dik_g19FnNZifaybC8pH0IV9eMbDFBRpWjf1u6dwl9RDHi-84BzsSnR1Bv1ivKbigJwvTD3oOf4t9B_oYnTp7YR5WCwEnmrW7SWEoGS9vKoMR45UfYxpM1dQpF6kQpALWbzwVymYiMF-7OB2J_AKRDs8gQicBDWdbRBjO2nluwFYggq_U96OnfDidjYuEcnNJlrI50XULKnoVxkGcl9twnW7QztCp7gNeX19i-cENRL-bS3KgfbF9XMltKuk4CfAU38EcMrrOy7Dp8_-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است
@Fasrna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/463981" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNVo6p9SR0G14h8ke4Py--SvFTD0jMbLVeD9Cnh00Powqaawe3Cy35BjxhkVr8pY66F9_Bn4zEWde5hpDFZpzPV1Lu6uS8gi05qjaAobXrMnW2fI7i_SrX4Oq_6b7OKFM8V67XPOABqVMlb2bNQwgxlCt0ikswhaE710LKB7JdKVT0fKl4twpTnhqLS118aCMjKE57mbFH7d7oQrO4EgppeJWyLRYR1Dm0kNbf-Yvkfsvd1k3LQEmCrOTw6ApW3rlLc0fHfFqnGMGgATNdg_F9T-tdeTVz5MaA_6UEKGOEFPcJFxAJcIVO64JSN0PlgO4Pm5YmGEMUwju4XuLy-GrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: امروز نه پزشکیان بلکه یک ملت، هم‌زمان و هم‌صدا در صحن سازمان ملل با دنیا سخن گفتند؛ از اقتدار، عقلانیت و مظلومیت
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/463980" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7e3c5727.mp4?token=EK8Wd1PYcGCZwO8ue9RvHKNjLJNqmStVqSzQm9x2p8SHUR4K7j3jNY-O_cbwX5omTEioEb_992B8TiwBeeaGcmtLr7wgmrnCa98I2drGFhYexhBICVHnL6xrAqvnWixJryt-DSjCX9sNa-VgSZk7kwIqqB2yaMdIv5WwQCtDfD08oEw1M88LMIehSSMLVVpmMxHM7eTJdFN5ABgdFVgUEY9_lRP_k2vF8QqnpEY-zEIe1rBs-EhQhguJXjsadfCVkUgm8VlbsHYmji7dT1Hjj8sjLe_6VUlJd2j02fv5UNKmIXKOl1PSTAooVc8gh-zPg24p_XBaR57MchOQyZg7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7e3c5727.mp4?token=EK8Wd1PYcGCZwO8ue9RvHKNjLJNqmStVqSzQm9x2p8SHUR4K7j3jNY-O_cbwX5omTEioEb_992B8TiwBeeaGcmtLr7wgmrnCa98I2drGFhYexhBICVHnL6xrAqvnWixJryt-DSjCX9sNa-VgSZk7kwIqqB2yaMdIv5WwQCtDfD08oEw1M88LMIehSSMLVVpmMxHM7eTJdFN5ABgdFVgUEY9_lRP_k2vF8QqnpEY-zEIe1rBs-EhQhguJXjsadfCVkUgm8VlbsHYmji7dT1Hjj8sjLe_6VUlJd2j02fv5UNKmIXKOl1PSTAooVc8gh-zPg24p_XBaR57MchOQyZg7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب.
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/463979" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1bs6UAET2MwURaAcOxjgAKjKRFOen7z0gHEi-9WnecNHy_PekVeDkUKU4Wj59r0iBmaqfljE_gj8GhC663PcEecr9IXxE1oZLZsi792begYFOWI6Mo19l1nWTTUKeins2PbX7G2ZXK7Agqhk9GWAccdIXuVQ-u1VG7ep9bhPAV_sFvrH8NxHLzfKy3Cs6pT1mBVlGlYfhgSkUo768amxKkvbtKfgSYEFwti8uGP2PUxA87gy0C2rIbYYOUWVRtg_LMgvIHX_6vTiJAgSGcoLUzsEwqfpcShyn3qbYJ6iRJEbETwcLmquv0lrQigY9bXJj-6sz4vP0ZSEdvuYVaQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ هلاکت ۳ تروریست در سراوان
🔹
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان از هلاکت ۳ نفر از اعضای یک تیم تروریستی در درگیری با نیروهای امنیتی و نظامی در شهرستان سراوان خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/463978" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiqGPIPLYfbqKq8g78jBQr9cLoX3AWkJjg9xsAOMUpI6XpsF-SXm_0et6w2ozJhZ6xB74p3lPy-1BUIeFzcKZmmrP64HeEynC2AnTs1wQaYG1alvsWi-2XYK4_cL6MnLtVQT4Q7GBu2ekIgV1oUih5ATT1iDVLuvbV5FUx559-vrggh-r6sUw_mO6_adOesu0v-TrEHio50Ai2f8DSn3yW0l7i0FbObJoh6dnzrwoKyfKQfci4tyX65_lvJ77ud1LrdadNnWh8xhxqKHVk02qGktaJfocxl5xX_rmttr1e-Fn238rpG1hiIZyQjvFmxh97K-fkiLZoYRmt2K37cmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومین شانس تیم ملی هم رفت؛ کنگو، ازبکستان را شکست داد
⚽️
کنگو ۳ - ۱ ازبکستان  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/463977" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqvJUneg5l9aQ-afniVpiy8Nv-GTQ6YNDsBr6ZrW2t-2vjZVkltFcdeUDQqxkTgzS22p_dwO3NuIZpnf4YEJq198ura6URmt8eIheIHRal3aQdXRNElkhiOY8CB_Iqw-l6ooMEgWUYw5DGa_jzUgHqyKaHWCiw-CCKgTH_TGDnj4PvcuVZsw8m7lC4f0QE4tDGS3R_gHqGHnZ15fbEuU3jSRlzDpz5orbQy2-ENcd6D2VnFvcdJknUnLWGytgXH2jYfzBF7ruEz30yqk-fYlhPuHpdl8pvWeuk_218VtY0ZiwHU07bSF2M-FV7gZTifu3bLWHgNJAWKf98Cw_huNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWDCn5iuYDt1t8mN1SOwMS_HXTx7oj1Ql0BPP9BeHAXP_s9sJoXu8Ee3yqi84aEOod7ZrPD1HnM19_GEkH_0S5kKxNh8wGqDwFQu2A1w9ytLsf7n82fm4sdL6WRmK2hkajiNX8DYb7UiBQlx4Bmw0bcDkOtJWoIZ5KguN8mPA5kKaYYU4ypt-VtB9YxWSv30d-M5hvrctQIbOq8gJwpbv_qzMAs1Uf_uBinwSoRAwprEimVvHfvmli7bjcbUUlS9Wgca1GedehG_RMElVfF0sh8g8E52xh-tXJ0UdUbhnFtYjrsdY7mr76no-PFZz6x_t1VTNA-T8dY0QA5XqASp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNnRWra2L0sc7csuDmum2T6Kat3zanFRQGTlXuBz1-E24-ges06nkRMV_sSx1QlQpdtmhRWeKXgHWsrQsKQAK5-arKQsacDmoJw4eevvBFT_uqFdP-mALibM9d-pN1yvMXev0qhMEkTVZQYrIi73cBAwSCIf6d_MkdVfPW_UazB5i9ekFJbvYVNrEcFLAxECrbFeupxLDrZMTY9nhDh5XAzI8FkdHfBaxSkDVSGk76kt-0NxwPMeW9eCeDscRhxV7_01M3yAsl01F2wNI2bVcCwbS4dKsfP_3BYwzt8frOKvkEwK0pa82V6RQkEUi8uy06_Cb9U2r4iVOC-kyjsvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6B-RhMGAhmtha_NWcHcZ-G3M_ty2cXOpRNLSwuRyzzWY5q9bhxGEA0Myy0MRi2WnIEbO45iMk_3imIj6gwWUXOIB5CfuYeZSDEQOqBU3xdmJbzvPHUKCxn_qpPWEFJkwUow33rDMveDmLxZabNyE5m1zmIsQHpzqJ1uh_ZeHn2e1Y5r7hINrx_AgYHLRcllOZRtHS_fmufn5moHeuOfKJhMnco6zRjCbpDyuI2iJYAYrzNbLsXiqQV9okdmKtuOSwg7ISpApxqw37JbSl5qgmDnU1NYAAD3hx9KZBs4aNaDEwbTfwahdb3x6aPf9SDI-YkUruRN28lwFFJcoHI1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIKSP4VeP-Ck2WQXeoCikeHTjyHafM5UXMAeSlMgCgboQarF9Y4Hg4sTrAVBHvFK-1yHI2bKkLZbP0eihuZRZ6tbc9MwWo4puUQbsAPl5hEdBrGnEGajRARzfqSCqqD6y71lWNr_Ou4sJTpdhpBQ9DWgfEE5A2_S08ytzGz10AdXx3jOFKyljQKXjTBoZzv0AE-8dM03mTqUkBtyHclrTzSdTDAP2QxS_bK7AfkmEh2hTvwtBzT0hJLgRTkgrqwfags29DrGW8WvxRB5sImb1EgHXDBibYXZvFqZ97p-Fd3ZAV0mNFyTTVXjOm27zlaMUPRN9fDq-frfy7KhVvcn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNcRpQuiVTlMWgtNUGQoPzhowinGeXoa1s6FxiMAUbU391eV67MgN3dfhizt2w_IZVCSl5B6dP4softLKNSaxc7U6Bf3xqU7tR0hHapw8sgjmew7k4E2h1lQx2N9i7cBrJ6hZ8UJywHXM8GDxVRa0NffZjRC0RubW3VFqq4mqQrb1QA_1gDOJDapRU35K2YgdIXeqhlsr-EBVQd1YzKaoR6MdzRh1YWZ1UNoYHoy20gN4lvNSuyTQC7lKXEqp-0lu0LVVg5UENLDcAmI01-Lwfsj3ThDR44QNXkkL1LS69mNFdWz3_yzgDOVu-8Syn3-gu4RzBdmq49Nf6ZuTZDXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IY42lHoIXxIbxfokeBlkfcjUekLJgwMsJ2NkjPow-pcyLNsGQEGZLx8ngRd0SnNS_DNOK7WjBfEHsM7hnMwYZ-rYj7w8PcpDKg2h8Hby0BztwUeu-0UeUVxjb45IZE_Z_Ht8B4SmB_l_3Om2KRHVs8fTfC9eVFY2t2U1AIQi_TVyfCe9GP62_A9Hh3Z1NwmOAUfB0EuNnIsi5Jox0-3ofu5VFK8aOtlAtbiRv5usE07XynejtvcrbOpfx17qJ_2zXghtxFAPa8pmi8LUZX1DrcWNqgMIa3Hl8zy5hZaL8GtkA2pvo8PAYa34PdxlN879nnP2TRjqNgF5Dd62NGmbkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زنگ اول در مدرسۀ روستا
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/463970" target="_blank">📅 20:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هلاکت نظامی صهیونیست در عملیات زیرگیری
🔹
شبکه ۱۴ اسرائیل از وقوع عملیات زیرگیری با خودرو در جاده ۴۴۳ در نزدیکی بیت‌حورون‌ واقع در جنوب غرب رام‌الله خبر داد.
🔹
بنا به اعلام رسانه‌های عبری در این عملیات یک نظامی یا پلیس صهیونیست به هلاکت رسیده است.
🔹
عامل فلسطینی…</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/463969" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9p_H6-QSG5HQbOuxH-4VmLFqGM9H0MfA-p6Ec-yeIfxx75-TLdzPG2A0cYnWphAjRIMIsRwKhUX3EAF2tPWkaxyVy2dpo1OgxVeW3BLSWs5N2iJ54gb2SALx07nC3VqoUQN0lX-Rb_rrnaMAI_UviM37PdOchTfTUDaWT27sKJU8QYZLLLzt7LZmVK0r_85L62LdTo7AHGnrhoZFyFTGxiGhz1Crj9Aebo-c3wUQ74kLZ-PJCb1NPGMXDUbb1pleT3cqhnsc-gH_Njy7m1nwEEbdPXmPBmEserj_POMuxeiLsf2aQAcGO4yP7FV12VZtys3PHSowIacQatexmKqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در نیویورک در هتل مستقر نشده است
🔹
پیگیری‌های خبرنگار دولت خبرگزاری فارس نشان می‌دهد رئیس‌جمهور پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است.
🔹
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای جمهور ایران انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463967" target="_blank">📅 20:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpaFaui-4NOkm1ddPaL7XqfXgtet4_MjNQZNGCyH2HH3fVPDAuhLF1ZseDm82p9uX2p-9VVaeP463JCuRPzE4-IuORtTF-zHodug2HCY3-mg2gVkR_8k4ad7F1G1B8flLUOVSiElquIZed-0N2y3YymeE0GquwcdH0jKV4vJkl1hjubnh6hdNq1umV_DN7KQegPmLYc7UsZECzJoNRpFOxcEi4roTE9Hj7DfwU0kLMCS0UjB0UjRzdYzYWarMkH5G9yTJwmxG7_lnrgDykJWEQK8E9lI2EDL6YTdTZZAD4lZc1Eg_Hcg1qMnSm5P7zZStDVtTIk7YpBoIyWNt4q4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: ملتی که جان‌فدا دارد، پاسخ تهدید را در میدان مشخص می‌کند
🔹
رئیس سازمان بسیج: ملتی که بیش از ۳۰ میلیون جان‌فدا دارد هرگز شکست نخواهد خورد و پاسخ هر تهدیدی علیه کشور را مستقیماً در میدان نبرد مشخص می‌کند.
🔹
سازماندهی نیروهای جان‌فدا شرایطی را فراهم می‌کند تا داوطلبانی که برای حضور در رزم اعلام آمادگی کرده‌اند، با ۶ عرصۀ دفاعی آشنا شده و توانمندی‌های خود را ارزیابی کنند. نیروها پس از این ارزیابی اولیه، برای دریافت آموزش‌های تخصصی‌تر وارد گردان‌های دفاعی می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463966" target="_blank">📅 20:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TybBP12BmUv2w-5gKJS-sB2d3axjGWJpMcmFRYBH6JEYf_sn8vDvWqIRZzVPOGwOFytnEgyGWwGtjyVKmTUu2Hlj8cdlyTZ0W9bsexnxW-VHAhFDp63Da7riHWXznzbYHHHtaeat0LVwbaS_JjlfdclIOvzDCgYjX-r9FMBcXDoKyrGOYV30HF2GipvGPkVpsreD46h4vz5bGr0QjgnqahUJp637k3HSkJFN7-HhdXx7VKnqsU158FAiMVY7mfdIFOtoNLYl_vNjkvUHq3xhmcJr_B8JfTsudUUFMrW7_z-ViymZ_PtBSO7bodfiJYFmWdT99MKysULsm_18ycubQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: دیپلماسی جدید ایران به گذشته برنخواهد گشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/463965" target="_blank">📅 20:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfc948a6d.mp4?token=vPV2oT6FoupMX8-VGg5-x4yZoLZMgDAr6L_dpUAiQ4iZMC8D3eJtUJNGT2yUjMRTuiD2S_GU6BPIyYutY4g-uSPidH0phkn_YX7CocRkkPFrc1QTkZdkF77F5bgR4lFD9RNqhtY0V_2skmpdYfUGKyixY9sEohrrXShQ4zVTridBBj6CfiUh3_pOArYOnsYX1JSODaos_Cw2Z0BBQHr-kU5N1j5RVarCUQBO9eTixg8jpgc_Fl_610rTrX4OFuIk6iEuo6hJzI61I4ci6eXJkIxgJ8UCpwr5iRPLO3ez1mFIjUMv-oIdNH8Q6KjCwEdby9JkdSe4KwIPdoqk8srcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfc948a6d.mp4?token=vPV2oT6FoupMX8-VGg5-x4yZoLZMgDAr6L_dpUAiQ4iZMC8D3eJtUJNGT2yUjMRTuiD2S_GU6BPIyYutY4g-uSPidH0phkn_YX7CocRkkPFrc1QTkZdkF77F5bgR4lFD9RNqhtY0V_2skmpdYfUGKyixY9sEohrrXShQ4zVTridBBj6CfiUh3_pOArYOnsYX1JSODaos_Cw2Z0BBQHr-kU5N1j5RVarCUQBO9eTixg8jpgc_Fl_610rTrX4OFuIk6iEuo6hJzI61I4ci6eXJkIxgJ8UCpwr5iRPLO3ez1mFIjUMv-oIdNH8Q6KjCwEdby9JkdSe4KwIPdoqk8srcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با رئیس‌جمهور سوئیس در حاشیۀ نشست سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463964" target="_blank">📅 20:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f6980138.mp4?token=AFswIVGYSc3ZykfUmOgXbXNher8aKpfQsYY6xydebL1HP4kKR-u7CnqNGu1bp-f0keU4HWBAMf8iTapA_LGsrZCY34tLHmqBTZyxBVPUSNG4bBSd7nsh8r8fsitjBPvw3jMr0nwqJ9P6uEiNxWk4sFqykXpe3lryDKIB80yjw326PIb9MQ3trxCBBnXfFAbXboQF-rIj93ULgcLcE0fc9gIhBnr27Ln2At7_evca7Qk5-l5ZLkw4zl75VF2TzV3eqJRorDVzDXCVv3K8Bebttw4wSlbeu9PysnIfBKFLHBOJMkPD2A9NxXLVkjgurwFvafTTsAtwpNT_iizG9nRlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f6980138.mp4?token=AFswIVGYSc3ZykfUmOgXbXNher8aKpfQsYY6xydebL1HP4kKR-u7CnqNGu1bp-f0keU4HWBAMf8iTapA_LGsrZCY34tLHmqBTZyxBVPUSNG4bBSd7nsh8r8fsitjBPvw3jMr0nwqJ9P6uEiNxWk4sFqykXpe3lryDKIB80yjw326PIb9MQ3trxCBBnXfFAbXboQF-rIj93ULgcLcE0fc9gIhBnr27Ln2At7_evca7Qk5-l5ZLkw4zl75VF2TzV3eqJRorDVzDXCVv3K8Bebttw4wSlbeu9PysnIfBKFLHBOJMkPD2A9NxXLVkjgurwFvafTTsAtwpNT_iizG9nRlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
سردار آزمون در شرایطی که امارات خاک خود را در اختیار آمریکا برای حمله به ایران قرار داده بود، تصاویری از دیدار خود با رئیس این کشور منتشر کرد؛ تصاویری که از آن‌ها چیزی جز حمایت از امارات برداشت نمی‌شد.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/463963" target="_blank">📅 20:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5551bcd1.mp4?token=MFJx_KPGOpVf8LwGx0eYE6npioRhk7X1t2akJzGxVBI8kDg8-HaaNkuUt2UOo-ESI-MtabSS8C2Po8F_rDA701gFqVStVwXCqfLBuqgTUmKVqF8hKi4Drhmdza68wCkZyhLQcl6BDHiyOk1T9TX0LnXKUaNIVtEwxN5Vr6iptaHx3pGC4dBFU3PpR0_a5m2w3El69avQtCfYwS1lm-MODdjsmGe8DaBI1078-1b_UCvSymGNzaTiUQ0LUGoSWvKy6TS1CeTrNxqtvvBGpqQ_hqIM0JlJDluwg6yMb-vT-kkn27Dnq7gmF4U826UgJIA7wmm-UvlQ9C_luUf9A5iVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5551bcd1.mp4?token=MFJx_KPGOpVf8LwGx0eYE6npioRhk7X1t2akJzGxVBI8kDg8-HaaNkuUt2UOo-ESI-MtabSS8C2Po8F_rDA701gFqVStVwXCqfLBuqgTUmKVqF8hKi4Drhmdza68wCkZyhLQcl6BDHiyOk1T9TX0LnXKUaNIVtEwxN5Vr6iptaHx3pGC4dBFU3PpR0_a5m2w3El69avQtCfYwS1lm-MODdjsmGe8DaBI1078-1b_UCvSymGNzaTiUQ0LUGoSWvKy6TS1CeTrNxqtvvBGpqQ_hqIM0JlJDluwg6yMb-vT-kkn27Dnq7gmF4U826UgJIA7wmm-UvlQ9C_luUf9A5iVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پینوکیو هم در سازمان ملل سخنرانی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/463962" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293587e08d.mp4?token=Thysjam1nwN2Z_p81uj_gDz71F6OknU3ow1SO8L8Ny2nlEjPQX-Nhr0yvrIOVFA05FcSRuAfp7OK6Gjo9AOsOV8UBPXyUnmP2e3Ae9atHkRhRd-3weUDNv1nGpmfVncCWnAfA8EyQjcXN-GfSnkJ9u03gj0LaABf3TynRPyqycZ6WyYb27nyjgV8UuW6uZttbI81FT4Jmzsgd62Lp82GAlt0lLupBJVGYphsx3bXElf6wA5kwEct9B0JIi02Sh57UhuF-_oBKGuN2npyeUHE7JvWQnuGRgrv4okeoSkyPSbgWN-6E9T8cV1jOGwGg3jJHwUsb76m4scli6F0Bdc_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293587e08d.mp4?token=Thysjam1nwN2Z_p81uj_gDz71F6OknU3ow1SO8L8Ny2nlEjPQX-Nhr0yvrIOVFA05FcSRuAfp7OK6Gjo9AOsOV8UBPXyUnmP2e3Ae9atHkRhRd-3weUDNv1nGpmfVncCWnAfA8EyQjcXN-GfSnkJ9u03gj0LaABf3TynRPyqycZ6WyYb27nyjgV8UuW6uZttbI81FT4Jmzsgd62Lp82GAlt0lLupBJVGYphsx3bXElf6wA5kwEct9B0JIi02Sh57UhuF-_oBKGuN2npyeUHE7JvWQnuGRgrv4okeoSkyPSbgWN-6E9T8cV1jOGwGg3jJHwUsb76m4scli6F0Bdc_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پادگان آموزشی جان‌فدا در پایتخت افتتاح شد
🔹
در نخستین مرحله از طرح جان فدا، اولین مرکز آموزشی جان‌فدا در میدان امام حسین(ع) تهران افتتاح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/463961" target="_blank">📅 19:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAXJTnWPTIdX588DdgItfKEeJTlHDKOWD3pGzNCdHNcTcW05I57o5X0nNqtUKxVkm84oFUpivJwUbcjWu0ch9IAOmOhsqeN9UN7YrwmPb-W7NrPryPTA9fNa9TjuRciKygrbWJ-TumhXz8n7w09kHV5o20myJFRxmPNbDenYNGfJynISxavhKfT2RtTVYK-5It8Hoyr99MOCPhmqqF7HGEKJ5n62CLy7kyt1EKM4-7KrXIwJRzbf4bWx5pmcA6SYq2YQ0xH3qBavYouBnohh-4g7OsPbDpkYvz5772PzniqUQ5V_l_Ogn-vDb42xYpBQGhi6poEsAApo4ZGwoKunow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: تیم ملی جای تغییر نسل است نه جوان‌گرایی بدون برنامه
🔹
سرمربی تیم ملی در نشست خبری پیش از بازی تدارکاتی مقابل ازبکستان: در فوتبال روز دنیا سن یک عدد است و آمادگی بازیکن از لحاظ جسمی، ذهنی و کیفیت فنی اهمیت دارد.
🔹
تیم ملی جای جوان‌گرایی نیست بلکه جای تغییر نسل است. جوان‌گرایی باید در فوتبال باشگاهی و تیم‌های ملی پایه انجام شود و سپس تیم ملی بزرگسالان مصرف‌کننده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/463960" target="_blank">📅 19:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RskOrnSeVW4M3V6v9Q6y1TScHIBKCjCAxS8J30u2JhM9ACsMlioAn8hoxQClIE9By2zYaoNTPkLdyeAe1W_oL4EaX7cXmbS6aGXvaO_qQBkPejvLW5Dwzu2yncxmgeSNXLbJUty49qsoRMbSanNGNlyobrY5Q4jbKJ31pa9mBt62ehUl_k3b9wAcYaB4yi1dZK4DJWUOkLAgnVlvW0FBcTpkGCg2AqcDypXWr6T6lacwyiZEqrDrs1YFIGhSbDO3_XV22P33oXF2_p0UVIKa7enkU5P5hlhC_XZu278hVeMYPrAVCUHXM0QmW7MBYQ-Uc9NkSsRfNOrc_1FkQpbabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از نیم تُن تریاک در شیراز کشف شد
🔹
فرمانده انتظامی فارس: در بازرسی از یک دستگاه پژو ۴۰۵ در شیراز  ۵۵۰ کیلوگرم تریاک کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463959" target="_blank">📅 19:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a911dbea86.mp4?token=DCpcK_9mMZy6clFvR4Syy-eMOFLvD5MmMiWPfli35fM3Zqp8fTUJdSvoK71dCaSqyqiHoL-EeFrYLnoeBCqT2q29SYMQSZc4dDiKjod2CKukuHK04b1LUNU43oTMwmY6VeoUmW3KUMcVDy3qxA84JOJfiDgtThGpVQz313dGBqQBuDd4Jk47Z7CscpTTYoW7eti5_lqHOcvmEOkns7jO1t0_jyYwxzhMI7AVYsl1vY543N-zTBf2vcsERN8jyxMjtDNMtSuNljSnR55FdbfETmCE5Hctl_PiK0v0cmF7sV_hRZlr9xCDuH1dpEGVIyZwR-zkb1d3mXdnlmBB3iVGRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a911dbea86.mp4?token=DCpcK_9mMZy6clFvR4Syy-eMOFLvD5MmMiWPfli35fM3Zqp8fTUJdSvoK71dCaSqyqiHoL-EeFrYLnoeBCqT2q29SYMQSZc4dDiKjod2CKukuHK04b1LUNU43oTMwmY6VeoUmW3KUMcVDy3qxA84JOJfiDgtThGpVQz313dGBqQBuDd4Jk47Z7CscpTTYoW7eti5_lqHOcvmEOkns7jO1t0_jyYwxzhMI7AVYsl1vY543N-zTBf2vcsERN8jyxMjtDNMtSuNljSnR55FdbfETmCE5Hctl_PiK0v0cmF7sV_hRZlr9xCDuH1dpEGVIyZwR-zkb1d3mXdnlmBB3iVGRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: دربرابر آمریکا از مواضعمان کوتاه نمی‌آییم
.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/463958" target="_blank">📅 19:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEpgVfRRQy31I-_gkfZcSoxMzZqD4u4k07KdrHqJKDVoA_gvYj3k3T-88if2J3pKc3lPgBlfwIjwHt1dftBNoAUGq23qh2jY37R0ykuc8O8L2Xd3RVhOCv2bUGe_tLjENOOBBQxanijKWSRmq-trh0duf_Yzr7cvu-xOxLnfkZ_59PBfZLyQvdv_0Er5xNs9uNdd4caCYSntVbgUGunB2GhVB6ml0BCLXFYo8fJOHx1XbWQquRMxOja_Gj6mdTEENKk99pWuwZgwALrzl6Ug1G33n2DJHD0cH-jRUc69zkjFdsgREitZBrKUXF7vYJAa2J_v7bpewvDZbl2-poOoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعام هنوز درباره انتخابات شوراها نظر نداده است
🔹
علی‌رغم انتشار برخی شایعات درباره تأیید شعام برای برگزاری انتخابات شوراهای اسلامی شهر و روستا در ۲۴ مهرماه، پیگیری‌های خبرنگار فارس از وزارت کشور و هیئت مرکزی نظارت بر انتخابات شوراهای اسلامی کشور نشان می‌دهد که شورای عالی امنیت ملی (شعام) تاکنون نظر نهایی خود درباره برگزاری انتخابات در این تاریخ را اعلام نکرده است.
🔹
علی کشوری، سخنگوی هیئت مرکزی نظارت بر انتخابات شوراهای اسلامی کشور این موضوع را تأیید کرد و تأکید کرد که تاریخ برگزاری انتخابات باید از سوی هیئت مرکزی نظارت اعلام شود.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/463957" target="_blank">📅 19:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc327c5b5a.mp4?token=XubKsGSZ9VzjhbPRzDdX1_5h98KAxS3NhcU6EMRkqWwJyDKePGl3icZ0R94l7JCdMKAONNET9om7_GXSqmdETIUguqlUgbjgLhBpY06PUhfaIsCR11rxPYwYGAEIX3vV4NIrYtKArscn8_fUuGkb6eUkJfvLXS--14MfIgE4UrJ3Frdirjls1EZFyFXFFb96IFK6rG2uzwKXDt1zExerz7pfovxXuZoEdDqgI0vQI8CSc_f7QFDi_QEzTW4ManTB0suyrh_uSQTuos3BFp_ZA5skTkhjKwYVOi0LAZPuwOs6jfr2SNm45102YtjhktIQxQTMTJScwqI5VHYoqtFNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc327c5b5a.mp4?token=XubKsGSZ9VzjhbPRzDdX1_5h98KAxS3NhcU6EMRkqWwJyDKePGl3icZ0R94l7JCdMKAONNET9om7_GXSqmdETIUguqlUgbjgLhBpY06PUhfaIsCR11rxPYwYGAEIX3vV4NIrYtKArscn8_fUuGkb6eUkJfvLXS--14MfIgE4UrJ3Frdirjls1EZFyFXFFb96IFK6rG2uzwKXDt1zExerz7pfovxXuZoEdDqgI0vQI8CSc_f7QFDi_QEzTW4ManTB0suyrh_uSQTuos3BFp_ZA5skTkhjKwYVOi0LAZPuwOs6jfr2SNm45102YtjhktIQxQTMTJScwqI5VHYoqtFNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای لشکر حیدر کرار خنجر یمنی را بردار
🔹
مداحی میثم مطیعی در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/463956" target="_blank">📅 19:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463954">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo49Au02syb419jPAlYRP_1T9qEiIvuIrEWV-E9mu2Q0kvkh8Sbwa8OKMDWYbAHzz2pC1pr3O8bpSkF3jGiX_sMluUAce6aZPATidicksVWGzG7bqVuWRIsc2pN8xlRFsNf0zQ3sKoZYrz7Ba69J0bmFQmMawB9xDFUDBsOB4_F2E-qXdlZZxrbimWUd8OgRS8F0GH3emtDYALM-I4BhKaDoSBVImJJxzAB0VVIqB4cJBqBzBTeC9r9fKcEti7z3E6q0_v6lLx2npr8lh8qZbGAEomwlYKYAIBRni0Ff_8okRjKhNXq1at7jeKeEn03lYSvgRMAemooxv530MKRpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مخبر و زاکانی دربارۀ سخنرانی پزشکیان در سازمان ملل
🔹
مخبر: پیام رئیس‌جمهور ایران روشن بود: دربرابر قلدر سر خم نکرده، شهدایمان را فراموش نمی‌کنیم و متجاوزان را پشیمان خواهیم کرد.
🔹
زاکانی: سخنرانی شجاعانۀ رئیس‌جمهور نشان داد پروژۀ اختلال در محاسبات مسئولان…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/463954" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: مطرح شد که ۷ شرط ایران را آقای عراقچی به واسطه‌هایی که بین مسئولان ما و آمریکا رفت‌وآمد دارند ابلاغ کند.
🔸
تا این شروط عملی نشود نه تنگه باز می‌شود و نه مذاکره‌ای درکار خواهد بود. هیچ تحولی ایجاد نشده و فقط ما شروط را ابلاغ کردیم.…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/463953" target="_blank">📅 19:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463952">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8390bd356b.mp4?token=SxLbWDzS93QaozwQlA9jf4aHG3vjWoa-v0GDDtbadM8XXeZYWwdvGBVWYk2Gp1nQEIP3hCBUJ9SJaLbxCLIwULrtF69gQZINlY513hcnhuUV_GdLqnJtgDPs-YKM7cbM9hV0Bg2ep1SRSJrsRMxa-Ql1nhHCafw-yp5gzWlPkjgBbiVaZLjS5jnUdWragwBXJ7nxunfq7-ekOm2dygtZEWT4FJ9v1fGt-gKX3W4n-m7YtCjXHh5Pwq_mBYHQEuX5mRxVYNiZUnDV82EYe72XACFSnBVnWRVPQpFaUiRKrzP0rrbywQ-qX-KPnk44_Oqo_75BesrtuC7gnINj5O6xPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8390bd356b.mp4?token=SxLbWDzS93QaozwQlA9jf4aHG3vjWoa-v0GDDtbadM8XXeZYWwdvGBVWYk2Gp1nQEIP3hCBUJ9SJaLbxCLIwULrtF69gQZINlY513hcnhuUV_GdLqnJtgDPs-YKM7cbM9hV0Bg2ep1SRSJrsRMxa-Ql1nhHCafw-yp5gzWlPkjgBbiVaZLjS5jnUdWragwBXJ7nxunfq7-ekOm2dygtZEWT4FJ9v1fGt-gKX3W4n-m7YtCjXHh5Pwq_mBYHQEuX5mRxVYNiZUnDV82EYe72XACFSnBVnWRVPQpFaUiRKrzP0rrbywQ-qX-KPnk44_Oqo_75BesrtuC7gnINj5O6xPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ هوایی صهیونیست‌ها به شهرک القنطره در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/463952" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463951">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3IM1IFEZF9sWBqgd2YJ9R-JLl3YjgAnLjEOEjXcZhQzJTZHLrk9yzWvS_VP_hF90VVR_NHuVIqT-_AewfbtDNoqfS8A73m3EvOWC1Y_Qsp23Pw_yafBhOcmqZNEWeRK2XIGy5jXq-6TChGRcN7Bzam2Ja1oBWIQNdhIOFAsXvOXsOvlveX1C77GXmhfWju9ppTyXl4u7rW63AILgiQ38SNG86Wn4VEZn094ygwNWE1wUgn9QuNVT_0cWM5xRGKeiWwF0zaeEuugWl7MgWAkmIg-Bq-ftnKU9tiFfz10ikKIfDwASNWww91wol0QJXmiLhfrvKCsJVMpwSg12sUAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام مخبر و زاکانی دربارۀ سخنرانی پزشکیان در سازمان ملل
🔹
مخبر: پیام رئیس‌جمهور ایران روشن بود: دربرابر قلدر سر خم نکرده، شهدایمان را فراموش نمی‌کنیم و متجاوزان را پشیمان خواهیم کرد.
🔹
زاکانی: سخنرانی شجاعانۀ رئیس‌جمهور نشان داد پروژۀ اختلال در محاسبات مسئولان کشور ناکام مانده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/463951" target="_blank">📅 19:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463950">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf5f4100f.mp4?token=cMyqbOu-qr7x5cO9oLibb3a7J9_TJJ0OlGKCBQ3TmswP50XF8NCcH1WC5A4PIubARpOc50z3gKbxhov0axQorEZDpbZZRFQ7fwHrqSYA2mYvNSkSPm2M8zfdEcC5QMv8NJnh74-mSoe0CtFRwYBAkPiyMAY5pbE-ON7L4R5E0oC4uFgaI1m8oxiYNRWeHudfEml47ZV57UpugoMnp9Vb5T4SceUyQfnHJxJb2clf_iXS_VxDguTz5VuIwW6orrRhhAA-OFfKmlqO5wrZYHU3fj4C0Pfu-2Q-gDTXohCAXLTLT0TRUe1GSTBfhYwKBPzqRYjsu94fHZ8_nJ1dyvPCOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf5f4100f.mp4?token=cMyqbOu-qr7x5cO9oLibb3a7J9_TJJ0OlGKCBQ3TmswP50XF8NCcH1WC5A4PIubARpOc50z3gKbxhov0axQorEZDpbZZRFQ7fwHrqSYA2mYvNSkSPm2M8zfdEcC5QMv8NJnh74-mSoe0CtFRwYBAkPiyMAY5pbE-ON7L4R5E0oC4uFgaI1m8oxiYNRWeHudfEml47ZV57UpugoMnp9Vb5T4SceUyQfnHJxJb2clf_iXS_VxDguTz5VuIwW6orrRhhAA-OFfKmlqO5wrZYHU3fj4C0Pfu-2Q-gDTXohCAXLTLT0TRUe1GSTBfhYwKBPzqRYjsu94fHZ8_nJ1dyvPCOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت نظامی صهیونیست در عملیات زیرگیری
🔹
شبکه ۱۴ اسرائیل از وقوع عملیات زیرگیری با خودرو در جاده ۴۴۳ در نزدیکی بیت‌حورون‌ واقع در جنوب غرب رام‌الله خبر داد.
🔹
بنا به اعلام رسانه‌های عبری در این عملیات یک نظامی یا پلیس صهیونیست به هلاکت رسیده است.
🔹
عامل فلسطینی این عملیات به ضرب گلولۀ صهیونیست‌ها به شهادت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/463950" target="_blank">📅 19:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463949">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📌
ببینید/ ابراز رضایت شهروندان از مسئولیت‌پذیری شهرداری تهران در جنگ/ شهرداری اجازه نداد، پایتخت چهره جنگ زده به خود بگیرد
✅
در نشست قائم‌مقامان ذی‌حساب شهرداری مطرح شد؛
رئیس کمیسیون برنامه و بودجه شورای شهر:
🔺
شهرداری تهران در اوج بمباران هم اجازه نداد، پایتخت وضعیت جنگ‌زده پیدا کند و حتی یک روز، خدمت به شهروندان متوقف نشد.
معاون شهردار تهران:
🔺
باید هر آنچه در توان داریم، برای خدمت به شهروندانی که با این همه آسیب و فشار پای کار کشور ایستاده‌اند، به کار بگیریم.
@farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/463949" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463948">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxDvPAzhffG7AHtuohWibRvuErWmtL23RdEXQr_jBiNqnpwCsU700wZPs9Kb4Fb-Zo5jVr5nPdlSJlXxMz2CF4JGgevK6W1pNU_TU1_7Mk210U8hWMhyarGDm4ww0XFw5TMb1Yxg_MqxVbxQWAwa-wo1fuY3aUUmyw6c5U-_swcEu3RIfb4tEEXlAqW3L_aOcC9t642xE_Wd7KDiJoCjY7X_Xvqgu5Crs7Hm9OdztkfZS7LAai4_382A2V5h8sb7V3S20eFa5o_eHeESmEQE3-4by7-HGXL28-xoWXIOCkxCLRio03zjqY6wG17rQfd3lOO3-KYyNcVKdJ6gJWugDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ثبت رکورد جدید جذب منابع در پیشخوان‌های شهرنت بانک شهر
👈
پیشخوان‌های شهرنت بانک شهر با ثبت رکورد 12 هزار میلیارد تومان جذب منابع، موفق به ثبت دستاوردی جدید شدند.
👈
به گزارش روابط عمومی بانک شهر، محمدعلی بخشی‌زاده، مدیرعامل شرکت توسعه و نوآوری شهر، با اشاره به دستیابی پیشخوان‌های شهرنت به رکورد ۱۲ هزار میلیارد تومان جذب منابع و تثبیت آن، از تلاش و همراهی همکاران و راهبران این پیشخوان‌ها قدردانی کرد.
👈
بخشی‌زاده اظهار کرد: دستیابی به این رکورد، حاصل تلاش مستمر، پشتکار و همراهی تمامی همکاران و به‌ویژه راهبران پیشخوان‌های شهرنت است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/463948" target="_blank">📅 19:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463947">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/463947" target="_blank">📅 19:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463946">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afYxbRuXx7hiLeKmAG_g37krkGtu9FgHF0u9U0pWrzVLE2FIVm8-XL2fb87emrVmnfwUzUY8hprGQ4b-IMgAXm269ddQ_z3xIgvwMobeIIwAprSSiIuUNYXQK3cmpEc7EzASv-HB262gBFzX9YOksI7RxTTP0rXEhuaTEcIaEI9d50u5B4bMw6KpQPPvUXMuFu1vT7eN-hqu_mHCJW_IzKxl13uOxTPu0RnoUwZTuFXyxUUdjYxuuacS-0nppJdSgVrLuaUghKIV5ykEjQN4AwHCTL_pBkk7OxpGe0AKM1EFFAmiPBuFtc9GFzFRC2C0MWAp_rJy3UanQN4PmA-ZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات جدید خاندان بن زاید علیه بانک ملی
🔹
بر اساس تصمیم جدید بانک مرکزی امارات، هیچ یک از شعب بانک ملی فعال در این کشور اجازه انجام تراکنش مالی به مقصد ایران یا از ایران را ندارند.
🔹
این نهاد مدعی شده است که شعب بانک ملی ایران مقررات لازم‌الاجرا در امارات از جمله الزامات مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه‌ هسته‌ای را رعایت نکرده‌اند.
🔸
امارات حدود یک ماه پیش نیز اعلام کرد که تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران را تا اطلاع ثانوی در پی تشدید تنش‌های منطقه‌ای قطع می‌کند.
🔹
این ممنوعیت به‌طور مشخص تأمین مالی تجارت و انتقال وجوه را نیز دربرمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/463946" target="_blank">📅 19:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463945">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9601bbb8b8.mp4?token=t7SbqJ-jrQASpnv64bMefZ9VxUNZDbe7BRlvaHB8AERgHvMHT04jhhmVp41hkzbcrQ9Y_L83va3rocy5DB2I8zPBmOJX7QedhW2KGHFo2gQiGdfKADNfv7BvPjV_wLdH8RvXNXrEdPfW05rXhyGD1VBpn_dQ00ISEasiZFVbMNEy4kVkcfselXDr5LfvksU-dJm49tyiGFbLIOCjBBIrX85eBSk0o-u7NRei43x2esfQuiQ1aZThGb-hZyqFllXiRvs-0MQSdaTBRoTnpMjMHsjmfGpu9OCDhSQIXOHTNAAVx8tDUa52OqAh9GWL78fTwSukN4pQNXLb1tDK1I33WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9601bbb8b8.mp4?token=t7SbqJ-jrQASpnv64bMefZ9VxUNZDbe7BRlvaHB8AERgHvMHT04jhhmVp41hkzbcrQ9Y_L83va3rocy5DB2I8zPBmOJX7QedhW2KGHFo2gQiGdfKADNfv7BvPjV_wLdH8RvXNXrEdPfW05rXhyGD1VBpn_dQ00ISEasiZFVbMNEy4kVkcfselXDr5LfvksU-dJm49tyiGFbLIOCjBBIrX85eBSk0o-u7NRei43x2esfQuiQ1aZThGb-hZyqFllXiRvs-0MQSdaTBRoTnpMjMHsjmfGpu9OCDhSQIXOHTNAAVx8tDUa52OqAh9GWL78fTwSukN4pQNXLb1tDK1I33WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اول مهر در دارالذکر؛ بچه‌ها به زیارت رهبر شهید آمدند
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/463945" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463944">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463944" target="_blank">📅 18:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463943">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162c43d47c.mp4?token=R82Bs1XJmJFw1W8w_h-A9AVRS046DmIeKN8HwQ4phMBxhQZyvMmNrNk1AqnbPFCFp9WTbi2EPAPAf-qWRMfj_vMoe7LwETm4xYHWmY2Frfqxbj4i5Q7bxT25UpKgUfsSTLhrdQz2-ZILUHeQzY2R8TosH-z2fH0OvyaGJbD05rlc6rLgSKiKQa4fMmZVnSf6tzaYCUb6oTgTtFiNuOa2eUvkp4rjAIefLUg6y1XlRNxVu2Yw6MfQN6MXJq9UvBpzYo3MpNtASEjf0gub7Yk67I4YIIvifQD-sHIDiUkiG7AlhjkMJNmda8NuA92m2-BbbquXMTF3me6BE91LLmChmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162c43d47c.mp4?token=R82Bs1XJmJFw1W8w_h-A9AVRS046DmIeKN8HwQ4phMBxhQZyvMmNrNk1AqnbPFCFp9WTbi2EPAPAf-qWRMfj_vMoe7LwETm4xYHWmY2Frfqxbj4i5Q7bxT25UpKgUfsSTLhrdQz2-ZILUHeQzY2R8TosH-z2fH0OvyaGJbD05rlc6rLgSKiKQa4fMmZVnSf6tzaYCUb6oTgTtFiNuOa2eUvkp4rjAIefLUg6y1XlRNxVu2Yw6MfQN6MXJq9UvBpzYo3MpNtASEjf0gub7Yk67I4YIIvifQD-sHIDiUkiG7AlhjkMJNmda8NuA92m2-BbbquXMTF3me6BE91LLmChmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
روزی برای «پرچم»
🗓
یکم مهرماه در تقویم ایران اسلامی روز پرچم نامگذاری شده است.  عکس: احمدرضا مداح @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463943" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492eb9cbdf.mp4?token=Mhhc4grYjovIDxZQ4LWRuISYdYLxy-x9lYxM48VSSDbu0wGNRQn-quyulCCAJCbAolBhhwMup3gWhsSNbTCcJK6NIifpN4pfW3aWOOy4PUWYpEyJQhHiMMoCCi4T2KlOaR8O3wDVHxlpDN9NRW8qJPDmOSoYVjroEKK8oql4k4atNTxv3AsAW7eaTLIeGTXqecVS1ExWbA9YKl6E3-5wXhmQmpzsTUtY8-nFGcg4JnhQU9N56gRhQ0faWqTBKZza65b5WZcZCr8JA9pk4Gx_Hen8mr1GxFJa5_lpesqc-bU2bk-Ha4rG6u6UifAbQIpLGessgJ8fwmliYt6OBuOonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492eb9cbdf.mp4?token=Mhhc4grYjovIDxZQ4LWRuISYdYLxy-x9lYxM48VSSDbu0wGNRQn-quyulCCAJCbAolBhhwMup3gWhsSNbTCcJK6NIifpN4pfW3aWOOy4PUWYpEyJQhHiMMoCCi4T2KlOaR8O3wDVHxlpDN9NRW8qJPDmOSoYVjroEKK8oql4k4atNTxv3AsAW7eaTLIeGTXqecVS1ExWbA9YKl6E3-5wXhmQmpzsTUtY8-nFGcg4JnhQU9N56gRhQ0faWqTBKZza65b5WZcZCr8JA9pk4Gx_Hen8mr1GxFJa5_lpesqc-bU2bk-Ha4rG6u6UifAbQIpLGessgJ8fwmliYt6OBuOonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی: نشستن نمایندۀ ایران پای سخنرانی ترامپ مایۀ ننگ است
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: درحالی‌که عامل و دستوردهنده به شهادت امام شهید ما، کودکان میناب، کودکان لامرد و دیگر ایرانیان در آنجا سخنرانی می‌کند، واقعاً جای تأسف و ننگ است که افراد ایرانی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463940" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbqNtgQjmu5PYEMwtvjJvAxyeXGysyIevCa_B3ciKE3uBOyqbMmyjl6GTwKMmsi-r7aMwczyRBPb1qRSucx7leDPktyEgjJ-hTCv4jkzuUF99gM9w4YecdEtPlW_TwIJHWiRIhVZYm5WlP_yf8lvVVs0eRdPVD-90hIgBGTlwAW_YFppHq12EodZGlz5YdZwGkBBHQ3xCRSRDrgHZwOYwKhSty7H-nJmXCIfXSeChYQEoecO07KXvXaKhSZGXpt0vhebXYaCLzuQaT9Ys_Qz4qKj-kXEAkI0Q6g4-ppzFpzQKQsnNlgmW4GZRdnArv8ISwiadwNTgEO3RETpqRaFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMYIgZbzhLmZKG8xUUq8RQ1eFC4AvjLgYgZ5GB3B-yVs8V8Z170uR_GjBE7YZKWzDwsrIn4Bud0Kmzridzwmos2-QuqzaFtYoov3cJnxcRY5EbackyA9IZ2fY7OIXs0yAsRt8kUNvF0muHj0ZGqa7iVDQygASlZmjuj13P_1xFWa_SQaMNN0_iPsCCgt5LbXfnM6OFQw66T7NEBf39_6sQ0Iis8lKJpFvBRjDTKnZHdejQXVZwlgyAWIvQnyVqSXNyEMEFWOIVzuplnJwvqd9No2P99NLNlZbuCsgEECo5-MrodUOhZXdg7LEOLkV5ZcAFpVkYtSUY5Q2IPsMxWW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-CjlAW7qmlwqZGw8osr5okdLpEXEnFx4IUhC8692YYVE3IrhMvvrpb1D07lUY7N9FcyE6nwhBsYGT6dCFXLYt9q1AMPO197f0zdSbqTGaIpyzZSpj0jpho1AZP1VX95jv09JSwy0QNWYjmz265kT9jJmjjh0L8XWRLpb8O9jqd7uTBthaDEJ6tSY6exnkRuNfVd2dX5ldT4Pi_Xbdeujiy52OQHFLErkrKeE8Tt-biDdJAXyqFho7GsxJoQNIHREbMsIh7x1GKY3FWrH2r4OzbLQWvVof441jTnlv-5Rbq6s--T3xk3mLa71yn4jvoIfu5wPeE2b1YdVtSaB2b4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6egu7zWS--FFBLQOaIsghzhC78VaW7IWzRvQgFiOdBcslWfFQDeLcSa_BpwEa2GYBgyCfkiHehk3yG1iHcXLnGW09JoZtSdNILuVMm4y6Bd9aqb9YkfUUWucxKicvYGrdg8Hp6QzDd3yd2KiQjk1IPObEu4L7TQwF-7mP8kuEMvJ0maewxl2RGxFCyJcNURyizbgFa-eSzim1WRRVL-yneJO5Padb-2gQ2E_VCjF1AN3xNyglQg5COU9dors_WIsTWcN5ZZqz7ljT0aA8oxHpry0vjmi-B8DKu9dbK-gCRuHQb4HC91-HyWXfBS3jRWojFWDKafgROaFiquZF47zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان جنایات آمریکا در ایران را به رخ دنیا کشید  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463936" target="_blank">📅 18:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74c9c59da.mp4?token=jxXWLwDZ2llx1veX-cWXFP4JaMDHwCIR9ns5pKp0dz730EZFVO2u2HenHg-3zKWI56n1-lfjsnrn7UGrky-TFjT5rr53-zirjAp_ZxUVuel4rP6p79fpBPDva-JiyImji7Us6TJgbObk_38HxsCZZrPCj5nwi7ArR2se8ZpKr3Yggwb-PjAC6xnEBJs9Tfu5a3k6obP4uDxvvB7Y9DsEX3zCEGh-5FTm_zFyUAX7ZWcbCGpRrzv9UKSG3sotHeRptng0ckxcaR4hyL1-efR6rnRuHSK9klwUuYfY-BfIwiVls-ILNnmygM53kp0n4ceaZBHuuWGrfy6r0I7OmDSuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74c9c59da.mp4?token=jxXWLwDZ2llx1veX-cWXFP4JaMDHwCIR9ns5pKp0dz730EZFVO2u2HenHg-3zKWI56n1-lfjsnrn7UGrky-TFjT5rr53-zirjAp_ZxUVuel4rP6p79fpBPDva-JiyImji7Us6TJgbObk_38HxsCZZrPCj5nwi7ArR2se8ZpKr3Yggwb-PjAC6xnEBJs9Tfu5a3k6obP4uDxvvB7Y9DsEX3zCEGh-5FTm_zFyUAX7ZWcbCGpRrzv9UKSG3sotHeRptng0ckxcaR4hyL1-efR6rnRuHSK9klwUuYfY-BfIwiVls-ILNnmygM53kp0n4ceaZBHuuWGrfy6r0I7OmDSuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران به سوی جهان دست همکاری دراز می‌کند؛ هیچ‌کس در این منطقه به تنهایی امنیت نخواهد داشت، یا امنیت را باهم خواهیم ساخت یا ناامنی را باهم تحمل خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/463934" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463930">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_5EelBrHqSOQ-B5eHhXeU6Xf9F5IveS7a5I8vg42kj3qAZg8BgjRgw72Gf1KrJ_0TTkuH5k-EbbLDrzOhxlvAPV5CBGWlXsbExQtCIy97Aub98C-26NeFFuVAD59JVylDAkbrfLc38CGI2Dw8ByN2_-XDomfrGtDNOvp8xGr4gftDh5tCtQ0WEIfAoLnCcs3u-YHt0nMdw33esl6tik2rybUnQ_nqJKnjMp6aONYVCwwb_jqdhDSwYwpi51hv4F0cQ55M0R5AyZ74TXly8AzBNHPPiWXENurG7tLqCpAL3t7De-tE60bn0wqP-G9ns5EAAzA1KjhBhgC-5IR6Ofew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4Qa2hiLcjMqdLM884Afy5BWH6g22wadiQ__OKzy7rUB6YKiNPEq2Fo3btJjfVujVpuQWsOEsowWpIh09i4zzPmmV5iZUElT_ogyzCaycwtIjyGdeGN3spbQ2xTEuJ3mtX9NyNSqws-sOuzhvF41oYvA5n3U7kyCUKGXiF0B9O4YWZyzDGXuoA05PUQuXDC5b9ORmpRb_Cxy4sm3HnXBkAHriKIrtidGMD18vY8zzr-DD_KMsUecqBTbhl5B81Qa4kRJKaiuAHASR3hJQhG3eV2DRkDUGK_-6ZDFA1nWq_-WE3sMyvU6wvSIxGXs-s7fJVScojfrop0d0r4ugdT5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBL3duclGyijKYdxxfWtrKgmAq_24G3NBTXrHP9JMq3NiF8BC8gcXqujws3OlvFH-e_EhoR3BRWxLUB58mU9zTz9MQ0x7aZeu25MX_6umBynhEZmazVu8cFOjDIY8n4s7uZzHIMyBV-iv7L740LOOxDuCKZiuxJMwiO-dlLwjnneJZDiPzWen5FcknTAy0bgOuENmGFxo0VoZIkk6wy67cbLdsGMWjKY00VYkmUhD2qsFmQfsukO8AIRZ98bPtpSDcFQq5pa_6qkDbqdMya6PuHFKATVVaFlIRMD_oU0mQtjZprrgOa9mJjNUJxVMpS4g9ln_m0Pjw5iAoTM64W_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnjlHe0rwzeQYzrLxkHLjUGWrD9-pz8G_0REDuIG5RL8F8w49xFuNHGjNrMydgUx23ZoZNEczWc2yjH95faHy4_n5gGwnegNjyN1oCkOl0WN3jBmHNgqXqgvGOhxIAZ1FDuQLZJdm4IxHY2yL5cSx04FP2P4ZU6yE6GMn3CFM_Qkr-qJsqZE0ogdLw0mHmyeX9VpOwEqF6iPlD4UN2JMre63y4T-kMhW9eFL4eS-y2QjLZENII5K7ScqUDEJcvVQB1eNl6t7g7ppwLZerOOrkkGX0_ppbyqG2ECm-jxpN5NSgjGT8jF5Qnpw3X8d_15Cw08O7SGZymV8m9XpF8A3nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان جنایات آمریکا در ایران را به رخ دنیا کشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463930" target="_blank">📅 18:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463929">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdae98e643.mp4?token=NP-bw4XI2jW_sdMyaxIVH_MJlYNb5iy3Iib8ij-tYQgMQTu1N1iiCRxQzfhJh6XKWyRME8MueP_8-ZhCjWzddLxZaKgq3F5oqAOQkkDfv3WBkjFvS5e3yG_Otkw9D90DsHDzhH_G69UtNUbZelOYEw2hM0ddVrDY4MTt7RsqKwgHYyDwAPfXDaOIDWh9dglfCvxKpVVtw0I061YmnwuV8FUmxMZcqicDwJr5u2FcsvyoFVSJ-VX7zpYR9SU3kyQiGQO_O7dtO2QbHPmqynifeVHe4TXj1BKqgKru8pMcvKxOA_mmK4C0KM3S5u8vnNERUJ1_hCm1iCG6ujMdVHizAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdae98e643.mp4?token=NP-bw4XI2jW_sdMyaxIVH_MJlYNb5iy3Iib8ij-tYQgMQTu1N1iiCRxQzfhJh6XKWyRME8MueP_8-ZhCjWzddLxZaKgq3F5oqAOQkkDfv3WBkjFvS5e3yG_Otkw9D90DsHDzhH_G69UtNUbZelOYEw2hM0ddVrDY4MTt7RsqKwgHYyDwAPfXDaOIDWh9dglfCvxKpVVtw0I061YmnwuV8FUmxMZcqicDwJr5u2FcsvyoFVSJ-VX7zpYR9SU3kyQiGQO_O7dtO2QbHPmqynifeVHe4TXj1BKqgKru8pMcvKxOA_mmK4C0KM3S5u8vnNERUJ1_hCm1iCG6ujMdVHizAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اسرائیل ترور می‌کند اما ایران تحریم می‌شود؛ این یک تراژدی است که به هرکس بگویید خنده‌اش می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463929" target="_blank">📅 18:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463928">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c00116d8b.mp4?token=RVh56oXvaKKcQWbjqNdUQYSkxhSTQIoKOUKGhkNgjRauaXzrSTcHt2HI14WuyHqOFsz-x4jCBpakY0eUNu2vdNMMPIL9N3kgTX4O4CWskRjQ11a5zVjcEodRxiXiV-ldplOygYpML68gIfYxP1b10GgFbW4vi8NrR8jTw5XzHOnKKOz6ZTumYAeFYU6ob6_JENniHBd0kgH5gTP6HrfumV1EJxOXC3-DoMeKM_9-mjaTb14ucNVqtQu2l5viJ0RZJxO0VwIYjXS5IfEPFuEsdKsxqa4RzHRWh6Qub9DDnJrh0wPAEAlnJmCuGTFZ-qIX8H7X601RVV8ret6-LdPueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c00116d8b.mp4?token=RVh56oXvaKKcQWbjqNdUQYSkxhSTQIoKOUKGhkNgjRauaXzrSTcHt2HI14WuyHqOFsz-x4jCBpakY0eUNu2vdNMMPIL9N3kgTX4O4CWskRjQ11a5zVjcEodRxiXiV-ldplOygYpML68gIfYxP1b10GgFbW4vi8NrR8jTw5XzHOnKKOz6ZTumYAeFYU6ob6_JENniHBd0kgH5gTP6HrfumV1EJxOXC3-DoMeKM_9-mjaTb14ucNVqtQu2l5viJ0RZJxO0VwIYjXS5IfEPFuEsdKsxqa4RzHRWh6Qub9DDnJrh0wPAEAlnJmCuGTFZ-qIX8H7X601RVV8ret6-LdPueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ثابت کرده‌ایم که از جنگ نمی‌ترسیم و تا پای جان برای دفاع از ایران ایستاده‌ایم
🔹
بمب اتم در دست اسرائیل است اما آژانس از ایران بازرسی می‌کند. اسرائیل ۷۰ هزار نفر را در غزه قتل‌عام کرد اما ایران بمباران شد. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463928" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463927">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2180626322.mp4?token=fTgIwiOeGp7l9a1puzMo7IFFNQESo4TJFuSU-jKRs6zxGvV-ahD7NxQclRhpt3kLodrmHw25Aj6-QWJ50CBzok4PrQcrM67w0d0Oj2u8l0WbygMT5dS4wzWFtJxkkRql3KQo2f_QposCh9AjbISvQamWWo9dlLXG2yyFpTC5KcqB3e54a7s51leEIahkZx9uU4In6rPgTwI0Et-5V2AJt6GgSqRdgrmyCzsbX3UTkj_9HxuJwpkXS7ubtVWDe6sc91Ii34RrnfI6JqZCcdMQ7EXZ5kpAKl_tBe1Y8uxIb5j-e7RDBdn-G9vMvubJgtm2NCR7GHyX02iIhF-Bq_9Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2180626322.mp4?token=fTgIwiOeGp7l9a1puzMo7IFFNQESo4TJFuSU-jKRs6zxGvV-ahD7NxQclRhpt3kLodrmHw25Aj6-QWJ50CBzok4PrQcrM67w0d0Oj2u8l0WbygMT5dS4wzWFtJxkkRql3KQo2f_QposCh9AjbISvQamWWo9dlLXG2yyFpTC5KcqB3e54a7s51leEIahkZx9uU4In6rPgTwI0Et-5V2AJt6GgSqRdgrmyCzsbX3UTkj_9HxuJwpkXS7ubtVWDe6sc91Ii34RrnfI6JqZCcdMQ7EXZ5kpAKl_tBe1Y8uxIb5j-e7RDBdn-G9vMvubJgtm2NCR7GHyX02iIhF-Bq_9Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: غزه نماد شکست سازوکارهای بین‌المللی در جلوگیری از اشغال و رنج غیرنظامیان است؛ صلح پایدار در غرب آسیا بدون آزادی فلسطین شکل نخواهد گرفت
🔹
مقاومت را نمی‌توان با بمب و محاصره وادار به تسلیم کرد و از بین برد. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463927" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463926">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a17e29ca1.mp4?token=KqL8ArOAbDqCZ4Qee9kh6g3T4BxUKldP738gJlyKRyw5re9zprbra3I6-2hKhfqrEWnSsq9oP0R9FYhqXPPIbHNKOn6Yc_jpzxwAMGdgAuow6M8QRrW72aHqlU2fCqbkBJ7KxMp8NYRglF59IF17F0vDV8XE6arW3JRzwOofTECXioBio9mtEGZ_fbGJ3-R8hRgXrrDhbqze9aGUfJgGneYjhkdUPVa3P4_cxinfvUDBU8DzyYRYPB__szn658slmvgZh95fLw3TMLv9uitBX4-lmzYvC9MTjepbNKrzLU71AyxglYychg_qMGA_7zU0L8Gg-Y6_7jjtGVcCdcXiKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a17e29ca1.mp4?token=KqL8ArOAbDqCZ4Qee9kh6g3T4BxUKldP738gJlyKRyw5re9zprbra3I6-2hKhfqrEWnSsq9oP0R9FYhqXPPIbHNKOn6Yc_jpzxwAMGdgAuow6M8QRrW72aHqlU2fCqbkBJ7KxMp8NYRglF59IF17F0vDV8XE6arW3JRzwOofTECXioBio9mtEGZ_fbGJ3-R8hRgXrrDhbqze9aGUfJgGneYjhkdUPVa3P4_cxinfvUDBU8DzyYRYPB__szn658slmvgZh95fLw3TMLv9uitBX4-lmzYvC9MTjepbNKrzLU71AyxglYychg_qMGA_7zU0L8Gg-Y6_7jjtGVcCdcXiKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما نمی‌توانیم بگذاریم همه از تنگۀ هرمز بهره ببرند اما ایران از آن محروم باشد
🔹
راه را بر ایران می‌بندند و سپس از تنگه اسلحه و مهمات و موشک برای نابودی کشورها از تنگه منتقل می‌کنند؛ این امکان‌پذیر نیست و ما اجازه‌اش را نخواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463926" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463925">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7b9c96ee.mp4?token=GljwKSNYBqvcIT9kBvrOshP_Vc7VQEHljPiCBWJ41NXpb_NjozNNqE-izfgm-CedAuvQhzeksbI_F8DmupdfEFoIOGNcTjO_KHq9AE6MhKyVqTfKzM0de_IlrB8Ba07gl2P97cAICfWseq2a8bL8-rJUPbiqOmEvsn4SU3a1O_7M12EzLywDRyiHeUdwmkqi_pUg109p4C5Kw83izhvs7ZH2Zd7Th-H3aJK5_pjjMvZ-yDo4zPKClqttZitWxTTi4p836-n9BWSo61J1oxLoUHSvglyMO6-_sn7lyNR1D26_Dl_3bS845uJ9d1R_bc8h4xKPCzph6MMFIdE6hq8dDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7b9c96ee.mp4?token=GljwKSNYBqvcIT9kBvrOshP_Vc7VQEHljPiCBWJ41NXpb_NjozNNqE-izfgm-CedAuvQhzeksbI_F8DmupdfEFoIOGNcTjO_KHq9AE6MhKyVqTfKzM0de_IlrB8Ba07gl2P97cAICfWseq2a8bL8-rJUPbiqOmEvsn4SU3a1O_7M12EzLywDRyiHeUdwmkqi_pUg109p4C5Kw83izhvs7ZH2Zd7Th-H3aJK5_pjjMvZ-yDo4zPKClqttZitWxTTi4p836-n9BWSo61J1oxLoUHSvglyMO6-_sn7lyNR1D26_Dl_3bS845uJ9d1R_bc8h4xKPCzph6MMFIdE6hq8dDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران نمی‌پذیرد دانش هسته‌ای امتیاز انحصاری چند کشور باشد
🔸
به صراحت می‌گوییم: نه سلاح هسته‌ای و نه محرومیت ایران از دانش هسته‌ای. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463925" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463924">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95f7b4413.mp4?token=qUJ0qLZ0ZsvJ24LPWJsZ-aXAT5WTZ8uq-e-KdbS9ozTleYOxppvQGR9Xd_LlUEgiOzYH3Xv_B--_mYU4asTCW7NnD7AynVBIB1TX7nRIhnWFkmVnjwv0rlsSXL3CBLRjNZDXYNjLB0SZcSldHltWYhrvpNr1jKjgWqHlK02XzG-CHED3kl577gCIEkN62dDgdYUp3PE8hLnMKsb57pimdge4CqmsdbFt0PCs-vRKTrGUvmGOSsPsQUZ843hF8U6gKexigkGHmWiukFhZyiA3mf9o21uwXZWPkGHlluGo3Hy-VpCt-5HsZJ7rXU4nliP7gSNM5aNt6nb4VWyJTsu7IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95f7b4413.mp4?token=qUJ0qLZ0ZsvJ24LPWJsZ-aXAT5WTZ8uq-e-KdbS9ozTleYOxppvQGR9Xd_LlUEgiOzYH3Xv_B--_mYU4asTCW7NnD7AynVBIB1TX7nRIhnWFkmVnjwv0rlsSXL3CBLRjNZDXYNjLB0SZcSldHltWYhrvpNr1jKjgWqHlK02XzG-CHED3kl577gCIEkN62dDgdYUp3PE8hLnMKsb57pimdge4CqmsdbFt0PCs-vRKTrGUvmGOSsPsQUZ843hF8U6gKexigkGHmWiukFhZyiA3mf9o21uwXZWPkGHlluGo3Hy-VpCt-5HsZJ7rXU4nliP7gSNM5aNt6nb4VWyJTsu7IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: سامانۀ دفاعی ما برای آن ساخته شده که هیچ‌کس تصور نکند بمباران شهرهای ایران بی‌پاسخ خواهد ماند؛ ما برای دفاع از ایران از هیچ‌کسی اجازه نمی‌گیریم.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463924" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463923">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e2387e6f.mp4?token=BUD9pnD49ys7ZTFyzk8bvtthvYyBZbY9NLATt2e-HvTKscG5JIiSSVKXGdLdHN9P7jor5Fkgv-mByTmVx354I_pokvALJmg6Yk_AQ2wOV0jzd6vgvvAblejDNXCTjmo23SBU1XLekob2KJZjKP-BULs8WZH7MW5OF8SaAft9_QX2hUzFg_6Ml237lIchj5zIf8J5dTgzYioYLHSD9Qbs7-Rzmi1dMplPEoAjusDgKYcEb7quTz51duaD9a0r_IQQ-do-IIFEV8_UP9dPhc8m0AKwz7hNpZjM92QJovUQ31QztRsrpy31_Fe4WHV-oOj0WuKFG81LtuSgVI3VotA3gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e2387e6f.mp4?token=BUD9pnD49ys7ZTFyzk8bvtthvYyBZbY9NLATt2e-HvTKscG5JIiSSVKXGdLdHN9P7jor5Fkgv-mByTmVx354I_pokvALJmg6Yk_AQ2wOV0jzd6vgvvAblejDNXCTjmo23SBU1XLekob2KJZjKP-BULs8WZH7MW5OF8SaAft9_QX2hUzFg_6Ml237lIchj5zIf8J5dTgzYioYLHSD9Qbs7-Rzmi1dMplPEoAjusDgKYcEb7quTz51duaD9a0r_IQQ-do-IIFEV8_UP9dPhc8m0AKwz7hNpZjM92QJovUQ31QztRsrpy31_Fe4WHV-oOj0WuKFG81LtuSgVI3VotA3gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مردم ما ۷ ماه هرشب در خیابان بودند برای اینکه کسانی‌که توسط آمریکا و اسرائیل مسلح شده بودند، نتوانند کاری کنند.   @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463923" target="_blank">📅 17:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463922">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0871b6d93f.mp4?token=gLZ49xGd4ee_7UFkRGH2Pm0dlK-UfpYTtd3AdEybHw4EyLSmJBwREaw4G8SBMsWFhs6vmoPptgOG3yIbplEdjZdVhSWzavvsupQ3gflzb8sr0gxW7FAkaRmyWOaOgnhkHM3mTc9RSfukqBH0-Qh7Qm4o9BEfCyZLdk0B5slLgtZWcGe_PvG6GQO4FdD1RgRShhfKyJ5rsCm3SrtxDOe6WS8q9LMBfx45SajdsHqYQGsv_n0HMimhjSy-eBFnkW3-aPFtY7ucufPZ1uG8syMUmR_A5dvrYbtwTa9snj10q41eVZnPbkDxJg8iOEgenoMnwUWXwoFGdBtMwUdHJAvRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0871b6d93f.mp4?token=gLZ49xGd4ee_7UFkRGH2Pm0dlK-UfpYTtd3AdEybHw4EyLSmJBwREaw4G8SBMsWFhs6vmoPptgOG3yIbplEdjZdVhSWzavvsupQ3gflzb8sr0gxW7FAkaRmyWOaOgnhkHM3mTc9RSfukqBH0-Qh7Qm4o9BEfCyZLdk0B5slLgtZWcGe_PvG6GQO4FdD1RgRShhfKyJ5rsCm3SrtxDOe6WS8q9LMBfx45SajdsHqYQGsv_n0HMimhjSy-eBFnkW3-aPFtY7ucufPZ1uG8syMUmR_A5dvrYbtwTa9snj10q41eVZnPbkDxJg8iOEgenoMnwUWXwoFGdBtMwUdHJAvRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران ۲۰۰ سال است به هیچ کشوری حمله نکرده اما ما را به تروریست‌بودن متهم می‌کنند؛ ما قدرت میخواهیم که از خودمان دفاع کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463922" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463921">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbe61eec8.mp4?token=uNT0Arq39zEqjscaaJanq_60sGw1Lyn_cqZxchY5SBjOy7cbLhH1czIw4qPsi-did_WH_Z9RYnnsKm_VTj0TPHSutOwZw4zvXLSOKKLJK5tGHsKC2u0Uhnsc8Gj_JiI2FmcCpSvT-Qlg0HcyLA3h89r41GYAeBuuGOsmQgidcLXyK9OAweHw-WaI8Z4BpMkJy1dVPMaHHFDbicBMhSaJu8HWjcqOT_pc0k5MotjHRrFFexnL45XWi6MlI_FOqSM1-HXcJtkkb6DaYutgegrwQadvTKl0EyFAgXFhhS2F_kASBh4OZExCxoNWStvueL3NWI1fCIh04JzZ6gzVLg7q5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbe61eec8.mp4?token=uNT0Arq39zEqjscaaJanq_60sGw1Lyn_cqZxchY5SBjOy7cbLhH1czIw4qPsi-did_WH_Z9RYnnsKm_VTj0TPHSutOwZw4zvXLSOKKLJK5tGHsKC2u0Uhnsc8Gj_JiI2FmcCpSvT-Qlg0HcyLA3h89r41GYAeBuuGOsmQgidcLXyK9OAweHw-WaI8Z4BpMkJy1dVPMaHHFDbicBMhSaJu8HWjcqOT_pc0k5MotjHRrFFexnL45XWi6MlI_FOqSM1-HXcJtkkb6DaYutgegrwQadvTKl0EyFAgXFhhS2F_kASBh4OZExCxoNWStvueL3NWI1fCIh04JzZ6gzVLg7q5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در سازمان ملل: ما تروریست نیستیم، ما قربانی تروریسم هستیم
🔹
من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیل و برهان و قانونی ترور کردند.
🔹
من از ایرانی می‌آیم که در آن آمریکا و اسرائیل یک مدرسه را بمباران کردند.
🔹
در لامردِ ایران آمریکا به سالن ورزشی…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463921" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463919">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fc224119.mp4?token=c2cKsn3v08lHQ02fo3zWZ4Q3ovHiOdoaC0ksjdPIg3bbIx7rIauml3nBNcxIL_duAuxH7w9Mgb3_Vj0qrCaMtO0JSh_87Q_4Lezwfz9Bq4A_2aco5PvRVtsA1JFcbRy1YQsdIz_VfWuUNklp7DRl-RSnh-_50ciQMzpdmhcG1yK2ejcFR9ccC1bN-W48F6AsL8I1e2ntPBRztxNMSYAeB54Yl0pVsY2h8x5DedOCNnBLVk8muhm-BWYIO85AgkgIiEJL90HvAsT5qhrGy3il5gy2VjEnFX_VWLLExYC1nq0r22dI8coVDSf4yFfwzpX25OBMwwMKVe-9IksMjSv0OKggum-6X7TgwINAEjfHlBFwbx4NXhAId-9F4ejKc3ovaC_NpZ2znCA_uMIwHpBrE87UJDdVaaBZx6Xb_HwH_gBbcv2SqE1Nax2lDK5ymE1rKXIEYt2K1rdEIrolPrS568Egj7wQTbIMlUaeRb-VhsLD2C0vc8eUVyPqWW5pSaqJLawNAX36gbZaD_SLNtPGtD5y8D6_uos2VFaPebtL-wekPtJzfadSY1IlsMhQ1Mh3eMUvA0QIvIizPbWGpjhMWuXXgaEVEWqZQ_YjCcV4gKfCq0e7Dcjxw5lPbbRcn9BcxpXuGi_oU3YWUgQVJy8sdIDNacY8zpv2sh4GO532Iu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fc224119.mp4?token=c2cKsn3v08lHQ02fo3zWZ4Q3ovHiOdoaC0ksjdPIg3bbIx7rIauml3nBNcxIL_duAuxH7w9Mgb3_Vj0qrCaMtO0JSh_87Q_4Lezwfz9Bq4A_2aco5PvRVtsA1JFcbRy1YQsdIz_VfWuUNklp7DRl-RSnh-_50ciQMzpdmhcG1yK2ejcFR9ccC1bN-W48F6AsL8I1e2ntPBRztxNMSYAeB54Yl0pVsY2h8x5DedOCNnBLVk8muhm-BWYIO85AgkgIiEJL90HvAsT5qhrGy3il5gy2VjEnFX_VWLLExYC1nq0r22dI8coVDSf4yFfwzpX25OBMwwMKVe-9IksMjSv0OKggum-6X7TgwINAEjfHlBFwbx4NXhAId-9F4ejKc3ovaC_NpZ2znCA_uMIwHpBrE87UJDdVaaBZx6Xb_HwH_gBbcv2SqE1Nax2lDK5ymE1rKXIEYt2K1rdEIrolPrS568Egj7wQTbIMlUaeRb-VhsLD2C0vc8eUVyPqWW5pSaqJLawNAX36gbZaD_SLNtPGtD5y8D6_uos2VFaPebtL-wekPtJzfadSY1IlsMhQ1Mh3eMUvA0QIvIizPbWGpjhMWuXXgaEVEWqZQ_YjCcV4gKfCq0e7Dcjxw5lPbbRcn9BcxpXuGi_oU3YWUgQVJy8sdIDNacY8zpv2sh4GO532Iu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان در سازمان ملل: ما تروریست نیستیم، ما قربانی تروریسم هستیم
🔹
من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیل و برهان و قانونی ترور کردند.
🔹
من از ایرانی می‌آیم که در آن آمریکا و اسرائیل یک مدرسه را بمباران کردند.
🔹
در لامردِ ایران آمریکا به سالن ورزشی دانش‌آموزان بمب خوشه‌ای شلیک کرد.
🔹
آمریکا خودش تروریست است اما به می‌گوید تروریست.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463919" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463918">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ جازان عربستان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463918" target="_blank">📅 17:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463917">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ هلاکت ۳ تروریست در سراوان
🔹
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان از هلاکت ۳ نفر از اعضای یک تیم تروریستی در درگیری با نیروهای امنیتی و نظامی در شهرستان سراوان خبر داد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463917" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463915">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjda0uDgoE3cJiFQd3NsPvgo3BNP_bdgVj1ak65T2FgJ58oVX2X7D2mafKWvFE9LO8WP9Bb3w1bY7H3mwr-sAH-eypG7AwQ87XKNkrHxQhnx31qGBHwwuWvxoqkSU5A4rqi_F-Oy7Sme-RRqDrRTxwnsmfYCoVD_l8c5yHRZn3_HmLFlV1IQ-J3mDU9HfNBW8bg4i1r8vxWPSRVlu8OQNNGZA3NFw9ZnT3FAw6kyw3-yL0B8C8ShM26wLJxl57SOBZuec6fcF-QNt0yLQTpm0kHO9YlZbZ2n8qwCJmIQ8IYqGc_gk4HUqQTABVVA0ReOJ-uu-Tqulqom1UihdRTBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azrm1j1wnifnWw7Dlk5MSTiaFO47odhiGSeltSHu3tsr_gK3YtDgnGsK5KD_qedkh3M9xWmaIAA_Q4ep2LHr1R3qNMsjdBKwzCaju0Ky6yWp1aT4fwVeFoRqVJ6kOU3vOqx-bYGUu8L_LTd4H-hgLxZr-wkJ5aGEa-FcEL1-MWBjys28kTltX39Uo3uvBaCiw-zbE1r1O3zyIUXye1IdawCkHMLmGmxMSIJLkXxZRzR-coNQrBI2hO_kFLIp9V4G8zQkutjfSs26BLm3l79gzUrMwgAsRUzRaAubWZkLFq-toyh_oVPzbRgfQU2roopRawzLcDalsoye2XWNw5d-2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: پاسخ‌ رئیس‌جمهور احمق و متوهم آمریکا را رئیس‌جمهور ما طی ساعات آینده خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463915" target="_blank">📅 17:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463913">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b4b36fa.mp4?token=FfT-15QyTN1F6peH4I8s99rpcTXDFSAFuitIj0C5z_m_CS5FSIV1Bc70aZ1U_ajyRIk8R2kU3wr3FCdKYmpDTXz2_jY0-c3dCoCY2tpnN6OZVw2JGRpEo6en3_b9U_4ERFWlkagl4hm4VsflnMQnu7XH9kWDTCV33Xo3KgFXrKWcCDpqV2O0CaL9rlJe6El0lRdM8VazOSsLJMyDnffFv0M_kTQv4jOBeA3sK_uogaJa_W4WjM7bVTzDSnNElf3x8GN28hZnAsg6rz4IiIUKW6ZE6DLUltgKBSYcOXc1HglmQG63AS1lkKz0xoNp6deN2qFMUnyAapnN6e_yha5lJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b4b36fa.mp4?token=FfT-15QyTN1F6peH4I8s99rpcTXDFSAFuitIj0C5z_m_CS5FSIV1Bc70aZ1U_ajyRIk8R2kU3wr3FCdKYmpDTXz2_jY0-c3dCoCY2tpnN6OZVw2JGRpEo6en3_b9U_4ERFWlkagl4hm4VsflnMQnu7XH9kWDTCV33Xo3KgFXrKWcCDpqV2O0CaL9rlJe6El0lRdM8VazOSsLJMyDnffFv0M_kTQv4jOBeA3sK_uogaJa_W4WjM7bVTzDSnNElf3x8GN28hZnAsg6rz4IiIUKW6ZE6DLUltgKBSYcOXc1HglmQG63AS1lkKz0xoNp6deN2qFMUnyAapnN6e_yha5lJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ ممکن است بخواهد در کوهی در ایران کاری کند یا به سایت‌های هسته‌ای ما حمله کند ولی ما همین را هم تحمل نخواهیم کرد؛ طرح نیروهای مسلح ما برای پاسخ آماده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463913" target="_blank">📅 17:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463912">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656e877e1e.mp4?token=uE7jv2-dIjNe-Dovimgf1JofPKqL3AjzCLKgK9A0Db0v4rJ1fWPvtfCDNbmhAZZQOXnwkcnTdDxR571UMvls_xnGHsbC2KRvDu-ELv8Memyqd7QyBN1by4H2UpJJd_Vq0uS8xWJGnDXTMw6HgHi9AxzuQD9gWxxU1pfwGquhugM6i5mVtu89hobz7NVgXrRFKTWwB8JQIMZGWjD6HimMOFsTqbUXgmyeERcHlG6-KTlCst7_nZrBxN6NHfRxsaYfYwzwJ8NmIS_T-1nrycW9utpT1lURW98XM8e8UeCjTLCQqmYLBQ8hdxv6aBde0bKKa_-Y015ZoPFDHWPxi8eOkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656e877e1e.mp4?token=uE7jv2-dIjNe-Dovimgf1JofPKqL3AjzCLKgK9A0Db0v4rJ1fWPvtfCDNbmhAZZQOXnwkcnTdDxR571UMvls_xnGHsbC2KRvDu-ELv8Memyqd7QyBN1by4H2UpJJd_Vq0uS8xWJGnDXTMw6HgHi9AxzuQD9gWxxU1pfwGquhugM6i5mVtu89hobz7NVgXrRFKTWwB8JQIMZGWjD6HimMOFsTqbUXgmyeERcHlG6-KTlCst7_nZrBxN6NHfRxsaYfYwzwJ8NmIS_T-1nrycW9utpT1lURW98XM8e8UeCjTLCQqmYLBQ8hdxv6aBde0bKKa_-Y015ZoPFDHWPxi8eOkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: در دیپلماسی جدید ما اهرمی داریم به‌نام تنگۀ هرمز که تضمین مذاکرات است
🔹
تنگۀ هرمز ابزار دستیابی ملت ایران به حقوق خودش است. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463912" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463911">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8337156e77.mp4?token=C89iKQ__59LMOKzHJPIoRHHe3z0SrQXSluVhUmaSOZqHGVzDR2ce2MCXj2QpZVsUiKMuaEZgiFyPEdUZC414IwqUGmoBAVOpGmUDHcliJRJBWeWyFSbJ8s0M-JQDJ1pLjMFH1JVf6BtrflnnJUB5RgpoK7379VYE0TYQBlbdJsy3i8wd-_kRvYCDZzBwrRhEtpI0K_av8EfvXIlMSq1fQepnPAQpyrUPk_x2x4mKsgeiadMG5nPjjnvWZgulqFsvvZCYOkC1wpoDTYYd1LMpGh76pbIsoQaLUzICEj5EEVRi4Z91QOxpz_FHVaEyQQFjZoadF3nDs1UJ5d8kQmZ9vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8337156e77.mp4?token=C89iKQ__59LMOKzHJPIoRHHe3z0SrQXSluVhUmaSOZqHGVzDR2ce2MCXj2QpZVsUiKMuaEZgiFyPEdUZC414IwqUGmoBAVOpGmUDHcliJRJBWeWyFSbJ8s0M-JQDJ1pLjMFH1JVf6BtrflnnJUB5RgpoK7379VYE0TYQBlbdJsy3i8wd-_kRvYCDZzBwrRhEtpI0K_av8EfvXIlMSq1fQepnPAQpyrUPk_x2x4mKsgeiadMG5nPjjnvWZgulqFsvvZCYOkC1wpoDTYYd1LMpGh76pbIsoQaLUzICEj5EEVRi4Z91QOxpz_FHVaEyQQFjZoadF3nDs1UJ5d8kQmZ9vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها وقت را تلف نکنند و شروط ما را بپذیرند؛ دیپلماسی ما به عقب بازنخواهد گشت، برای بازشدن تنگۀ هرمز شروط باید عملی شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463911" target="_blank">📅 17:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463909">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e65ab9911.mp4?token=qyIDTSVdCp2X2tlSvkvaZ4KY8GD5mmXk9ooHXJcgjC_W6gQyAYaIrDiLBFPuKSapJsc-F_1gPOPe0nRGGUeJ2C3qIwmFVgf9OnUN6JdU0AooFHnNV1zFVTM0ST-wlFNkusTJ93AVgd4JuW2dBoSpfpGFX5WjJwjsow43dzjuv1m8scefBST8lFxFqt1DY2sCRSE6fraakvmGRL4yloe0tpt68zhZTHtfBzR-mxObyHDZqw_4Viw0IQt2_f5eOBBZT1O8D_XLwcOn_gYGLkk7H1VshjYhdI9yOXdHvGVTLRBid99d7Snryce0LAUOAYgXy8XcP2axrPqdgL4lHTSfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e65ab9911.mp4?token=qyIDTSVdCp2X2tlSvkvaZ4KY8GD5mmXk9ooHXJcgjC_W6gQyAYaIrDiLBFPuKSapJsc-F_1gPOPe0nRGGUeJ2C3qIwmFVgf9OnUN6JdU0AooFHnNV1zFVTM0ST-wlFNkusTJ93AVgd4JuW2dBoSpfpGFX5WjJwjsow43dzjuv1m8scefBST8lFxFqt1DY2sCRSE6fraakvmGRL4yloe0tpt68zhZTHtfBzR-mxObyHDZqw_4Viw0IQt2_f5eOBBZT1O8D_XLwcOn_gYGLkk7H1VshjYhdI9yOXdHvGVTLRBid99d7Snryce0LAUOAYgXy8XcP2axrPqdgL4lHTSfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: مطرح شد که ۷ شرط ایران را آقای عراقچی به واسطه‌هایی که بین مسئولان ما و آمریکا رفت‌وآمد دارند ابلاغ کند.
🔸
تا این شروط عملی نشود نه تنگه باز می‌شود و نه مذاکره‌ای درکار خواهد بود. هیچ تحولی ایجاد نشده و فقط ما شروط را ابلاغ کردیم.…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463909" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463908">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5087f76949.mp4?token=QKuULVWVvCYWtVkFtiVV3U5W2yX_RQQuEBYHcyRwc4J95R5j0aLtHKYuMq2ieWYiB_bhI7aOxFCrnL2V0dse9aHqo2YI4PUwFclQFKiMLBcPkIdQ-kOtpjPBRUDiOE9CirHnRn_QuqpdIOCurw5K63QGXM7C655fdJlOfgo7Po1uS2ocsB9a4rN_hfv6zgLaR_bKf9TEQVdaSX8jyuqfV1ZAh-CJnQc75TrjRbimRkyxotuom6Pk--HwM4zZW25BslFeazzCXxA12CQUGIcDkTonDDgMyi31sJ1eADBwCXlJh2e7aXOro13QxHiHSt5P-hT3yTK4KTyBxGfNSfH_VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5087f76949.mp4?token=QKuULVWVvCYWtVkFtiVV3U5W2yX_RQQuEBYHcyRwc4J95R5j0aLtHKYuMq2ieWYiB_bhI7aOxFCrnL2V0dse9aHqo2YI4PUwFclQFKiMLBcPkIdQ-kOtpjPBRUDiOE9CirHnRn_QuqpdIOCurw5K63QGXM7C655fdJlOfgo7Po1uS2ocsB9a4rN_hfv6zgLaR_bKf9TEQVdaSX8jyuqfV1ZAh-CJnQc75TrjRbimRkyxotuom6Pk--HwM4zZW25BslFeazzCXxA12CQUGIcDkTonDDgMyi31sJ1eADBwCXlJh2e7aXOro13QxHiHSt5P-hT3yTK4KTyBxGfNSfH_VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما دیگر به دیپلماسی گذشته و اوضاع اسلام‌آباد و قبل از آن برنمی‌گردیم؛ آمریکایی‌ها اول باید ۷ شرط ایران را عملی کنند وگرنه نه تنگۀ هرمز باز می‌شود و نه مذاکراتی آغاز می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463908" target="_blank">📅 17:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463907">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e0d56947.mp4?token=UObKgfK9BLUZt4iM3Q3BoaQaWPQepEv-VGAk5kIggUtrmoJ541NKA3ADMrQ-a0fiwaSzU5PjBvflxcQ3qFylFVGlpSqIkUw764UA9L82khHdOpMGNuPY9nR4fp-_aTsLKaXoJI7_O_ePGMsXi280y5FrMK70961K7gMonc0WioEkyDgNpNdotAe53bOFG4PuTIjw5R8qiIvBDGfuYoQPrp4SMFn-yreQEfM_hhO4brYR98iKODi1VzcmCrJd0vh-81MMWO6Zh0HZnJd2G4dJYFcMSDwx8eP4T3J_rlnRHEyaEwQsf82jLh4noxVmBTlzRIkS0WMUPqo_QEWCwqb4gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e0d56947.mp4?token=UObKgfK9BLUZt4iM3Q3BoaQaWPQepEv-VGAk5kIggUtrmoJ541NKA3ADMrQ-a0fiwaSzU5PjBvflxcQ3qFylFVGlpSqIkUw764UA9L82khHdOpMGNuPY9nR4fp-_aTsLKaXoJI7_O_ePGMsXi280y5FrMK70961K7gMonc0WioEkyDgNpNdotAe53bOFG4PuTIjw5R8qiIvBDGfuYoQPrp4SMFn-yreQEfM_hhO4brYR98iKODi1VzcmCrJd0vh-81MMWO6Zh0HZnJd2G4dJYFcMSDwx8eP4T3J_rlnRHEyaEwQsf82jLh4noxVmBTlzRIkS0WMUPqo_QEWCwqb4gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: داریم زیردریایی آمریکا را مهندسی معکوس می‌کنیم
🔹
این زیردریایی تا ۶ هزار متر در اقیانوس تجسس انجام می‌دهد و فوق‌العاده ارزشمند است.
🔹
شاید برخی کشورها در آینده به ما بگویند فناوری آن را به ما بدهید و در قبال آن چند میلیارد دلار…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463907" target="_blank">📅 17:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463906">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4a673395.mp4?token=U0gHnASI2a_QUpm9gyx67q7JxYy0JLdxejGJyhi3usz7E8iDzXixMcLTmIvEsbKzHm5t8S5SYbuWnRhm2SRHZKHIbAS_F7DTnz7zGLOX0OK4NFsnqUHP2xDvQZrskM-2Qk6zfPm9bRNfkLLVABsNI5FKz3LJjDoLiYLyUtpz-1HrZRQOSF9F3nvz88dItnX_pgwicDV3nVAe9m33QA63Q7aiPFu3iGGnwBnn6uccsYxSpsPbTOWU9IDKWzO_ZsW-DzJOtQjjsoAOivyRfSxTlh_MKd1vf9oDDJJc72qE6UIFmy3hoSb4LQGNRKX8HIHiYdDlrtMcTzPTlqHtd5kzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4a673395.mp4?token=U0gHnASI2a_QUpm9gyx67q7JxYy0JLdxejGJyhi3usz7E8iDzXixMcLTmIvEsbKzHm5t8S5SYbuWnRhm2SRHZKHIbAS_F7DTnz7zGLOX0OK4NFsnqUHP2xDvQZrskM-2Qk6zfPm9bRNfkLLVABsNI5FKz3LJjDoLiYLyUtpz-1HrZRQOSF9F3nvz88dItnX_pgwicDV3nVAe9m33QA63Q7aiPFu3iGGnwBnn6uccsYxSpsPbTOWU9IDKWzO_ZsW-DzJOtQjjsoAOivyRfSxTlh_MKd1vf9oDDJJc72qE6UIFmy3hoSb4LQGNRKX8HIHiYdDlrtMcTzPTlqHtd5kzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما برای اولین‌بار توانستیم موشک‌مان را بالای سر ناو هواپیمابر جرج واشنگتن منفجر کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463906" target="_blank">📅 17:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463905">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d21ae2331.mp4?token=mhopG_un9LBM3bHyTH9x56gd3H6FSlbw-Usm50mzwhL_zppcLm5jk3mMiDXALH8RyFpFDK9PZtzT2gW6uHdG0UvBi9CZjhE0lXK5tK2cvuqu-G_7OLXkO8P7T5Aubczq603uVRr065vxt_zJa7E-eWVow-UL1EM8wLq_Tk5kiAHnjUOx4iU6e6EnDckitDcknccU50ZZmBlavFjJOJOwAGYYMb7AQoaDbjmMCv_c6To8GTFFA6uzm1joSLlRD5c80Ae1R_ZV-V9djXLg2GM6X2B3cPqj4Apayo42F-BgY4UnCNaJdRnIndUkR0Hj3OewGy7UAqJwhdY788hxfFJv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d21ae2331.mp4?token=mhopG_un9LBM3bHyTH9x56gd3H6FSlbw-Usm50mzwhL_zppcLm5jk3mMiDXALH8RyFpFDK9PZtzT2gW6uHdG0UvBi9CZjhE0lXK5tK2cvuqu-G_7OLXkO8P7T5Aubczq603uVRr065vxt_zJa7E-eWVow-UL1EM8wLq_Tk5kiAHnjUOx4iU6e6EnDckitDcknccU50ZZmBlavFjJOJOwAGYYMb7AQoaDbjmMCv_c6To8GTFFA6uzm1joSLlRD5c80Ae1R_ZV-V9djXLg2GM6X2B3cPqj4Apayo42F-BgY4UnCNaJdRnIndUkR0Hj3OewGy7UAqJwhdY788hxfFJv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما ثابت کردیم که آمریکا حریف ایران نشد و در آینده در جنگ با ۲ قدرت رقیبش هم با مشکلات جدی مواجه خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/463905" target="_blank">📅 17:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463904">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945c6dd294.mp4?token=kyQnW3YY8Vfyz2PtLEk3fiNB6iYIVlxRIf0zDPznH58c6ikt23qExWkvdNEfcbPqLbs9rHNoacNa2YFYg-EyLTV2X5LmOSxDKo7K7aR7HRNpmHj1p5vXgt3VTJVH-yqGfQglnT73TZipnz4dCriASpGEnm15CYZnGEfybPoIU8QaQdB6FjAbi1h2LTd6X0qstpdxQmzLujoVASH2hDBCXdQPel7J9a07W-Xei0Jj0rRNm4m3o1NriKCau7ppCWUolYTquLo8-T69DA4Jd1YIjaBNZuBlBDNTgNOuotbeGaYhB79sROcWURln1E8N66JNzGio5oXhVLUCneejW7_Ysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945c6dd294.mp4?token=kyQnW3YY8Vfyz2PtLEk3fiNB6iYIVlxRIf0zDPznH58c6ikt23qExWkvdNEfcbPqLbs9rHNoacNa2YFYg-EyLTV2X5LmOSxDKo7K7aR7HRNpmHj1p5vXgt3VTJVH-yqGfQglnT73TZipnz4dCriASpGEnm15CYZnGEfybPoIU8QaQdB6FjAbi1h2LTd6X0qstpdxQmzLujoVASH2hDBCXdQPel7J9a07W-Xei0Jj0rRNm4m3o1NriKCau7ppCWUolYTquLo8-T69DA4Jd1YIjaBNZuBlBDNTgNOuotbeGaYhB79sROcWURln1E8N66JNzGio5oXhVLUCneejW7_Ysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ خودش متوجه شده که جنایت‌کار است و خودش و نتانیاهو جان سالم به در نخواهند برد.  @Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/463904" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254ad4c36d.mp4?token=EOoT9ORnl9CxslXFpXTZChNMvNJ-bo0xtMIpjz5APmRP_AffuYNLCHf9xLjaTN0rKyhP5ySJv0Q5FFRB5_CbtsbRTJIf9tEhZAwAiqVKklfv7bBhePWvhpGy_KNV6hN1eONUV4HzmNlPfxiP3innz3KVMH_8PCJQnwoSj9Bt1EdagCbGlJmw2YXT2_hD4pHmE1oH4cBjtf2PBtIMzqljeZRdKywtVR0wb8bIaG8cC9G6hkSVT-C1OlBJPsdrb3t5BXRm_LpWvxnYd2Z8pxDjCQBAfxW4wst1tr3VtRsFwjNC0ihxeWdO9a83jo4n7JIRxYprAtQDaICM1-f4LiiHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254ad4c36d.mp4?token=EOoT9ORnl9CxslXFpXTZChNMvNJ-bo0xtMIpjz5APmRP_AffuYNLCHf9xLjaTN0rKyhP5ySJv0Q5FFRB5_CbtsbRTJIf9tEhZAwAiqVKklfv7bBhePWvhpGy_KNV6hN1eONUV4HzmNlPfxiP3innz3KVMH_8PCJQnwoSj9Bt1EdagCbGlJmw2YXT2_hD4pHmE1oH4cBjtf2PBtIMzqljeZRdKywtVR0wb8bIaG8cC9G6hkSVT-C1OlBJPsdrb3t5BXRm_LpWvxnYd2Z8pxDjCQBAfxW4wst1tr3VtRsFwjNC0ihxeWdO9a83jo4n7JIRxYprAtQDaICM1-f4LiiHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: یکی از حماقت‌های ترامپ همین سخنرانی‌اش در سازمان ملل بود؛ چون در جایگاه جنایت‌کار شکست‌خورده به دفاع از خودش پرداخت
🔹
این سخنان نشان می‌دهد که بزرگترین مشکل ترامپ و سیاست آمریکا، ایران شده است.
🔹
تمام سخنان ترامپ مثل دفاعیه از…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/463903" target="_blank">📅 16:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyrIH1rT0etqA0TB5qpWLcKhE8uGvWvMB7pk_6F0XS5UFynq1e_VSL2ct2uw8QENClJPI4_UQAFKxiSGimpNtzHqbraaXE3H_eUM40zfbcrleG9JVOymNQyg2GB9CimkOo8hLHhk-glQzCmcw_IImAd8zXCH5-m3n0b8zNVuqFTlRmM1D-mx0vDZ6ESyuXb_jSvFuTyjWoh7AYQkFXkstx-LkVe4t79pJm_30NpR5v904RPPUD1wZOy41xIZoEgKmNnS-9ycUxBH7B1M1pSD1rmJpbBUtOtiF_sKzD3_yiXAgs_1nveDlXlBnAsBsQr3au7msZeB_QjXOYs8kwYLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش نافرجام مدیر سابق برای مدیرعاملی استقلال
🔹
باتوجه‌به بررسی گزينه‌های مديرعاملی استقلال در هلدينگ خلیج‌فارس، همچنان مصطفی متدين بيشترين شانس را برای رسيدن به صندلی مديريتی آبی‌ها داراست.
⏺
كميته انتصابات هلدينگ پیش‌تر در جلسات خود گزينه‌های مختلفی را برای اين سمت بررسی كرده ولی همه آنها رد شده بودند. از جمله اين گزینه‌ها كه برای بازگشت تلاش بسیاری کرده يكی از مديران سابق بوده كه توسط شريعتمداری در هلدینگ خلیج‌فارس و علی تاجرنيا بركنار شده بود.
⏺
شنيده می‌شود در كميته انتصابات اين گزينه به دلايلی چون رد صلاحيت توسط نهادهای ذی‌ربط، انعقاد قراردادهای عجیب‌وغریب با بازيكنان داخلی و خارجی، ارتباط با ایجنت‌ها رد شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/463902" target="_blank">📅 16:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463901">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72dbdea702.mp4?token=JrJhv6S1X2UaevmUSSXNTCzUcrTdQ72R6zWBuZ5C5Uu3RReHtth2VrdYEo3-ln9fE6XesEBpa4rnUJV8Qby653gQ6gaaPa6CN1HjWnCFSZ_79J2aobUy8EC2-xLWKvLMh4cRJo9_u818ruK9Lvgqa652jvWHxEfuQyn0clD9b_sBru3q3Ep3XEKzhJ56xEcbd0WzriuZWuIqO4bDad2ty5taiQz1_mQEL-Ct6EUdkJRf-YMghEWiZ3L_KicVn2yamTELAllhOn30dhDlAgX7Lr-tj9xr4Ms73dHQKguiQCA_RTnxci282scfS5It4i_CQQtmhAZT0F5dYrpV7JDUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72dbdea702.mp4?token=JrJhv6S1X2UaevmUSSXNTCzUcrTdQ72R6zWBuZ5C5Uu3RReHtth2VrdYEo3-ln9fE6XesEBpa4rnUJV8Qby653gQ6gaaPa6CN1HjWnCFSZ_79J2aobUy8EC2-xLWKvLMh4cRJo9_u818ruK9Lvgqa652jvWHxEfuQyn0clD9b_sBru3q3Ep3XEKzhJ56xEcbd0WzriuZWuIqO4bDad2ty5taiQz1_mQEL-Ct6EUdkJRf-YMghEWiZ3L_KicVn2yamTELAllhOn30dhDlAgX7Lr-tj9xr4Ms73dHQKguiQCA_RTnxci282scfS5It4i_CQQtmhAZT0F5dYrpV7JDUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: پاسخ‌ رئیس‌جمهور احمق و متوهم آمریکا را رئیس‌جمهور ما طی ساعات آینده خواهد داد.  @Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/463901" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463900">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f70T0Akz4JP1-zxaOlDVUbutLhvMt_9x4OGDj_zf_vPy-curAyjOyCzCfrBiVqOvBNTAzYP5_Kxm-jGean-xVHDbx9_LSh07PeL1rZULZyIwtqR4qKQKQpG1zj1YRFUSvFjZ1kvmjW4aPQKkLOys8wlUCVjaZZfcu99_E7F6FXU_7nU6J3CzQPz9VbG7Fvhgp07foqFe79KgETiO5Y-yupfb3LdcNfJGUXmI9EqIFv5d0wXLAxbTpNN7czpDQfP2EyG6ISaFU1TRCz6KfbPtJOh003anmC513DgQghtondhnbdA7iMvgbFAbNZAEw64E3Q7DIe6hlSKOdj6HXqTOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی: همه کسانی که در برابر جنایت در مدرسۀ میناب سکوت کردند و از محکوم‌کردن آن روی برتافتند در این مسئولیت شریک‌اند
🔹
مردم ایران برای همیشه این چهره‌های زیبا و فرشته‌‌گون را به خاطر خواهند داشت؛ و هرگز قاتلانشان را نخواهند بخشید.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/463900" target="_blank">📅 16:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463899">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b85e9660.mp4?token=uvi_VFJ9_16zRWOYKp7Ir5lZ8F4mp9oVcXJz1R8NR8BGJgxTjgt1pqpKvjQWQkGtuf1oGYX_Yttib4cyEE8OCo5FV39piRq148S76qLxS3jYZ1FRUY2L9Fl6ucgulHU3X2QIuAh9NFqxzOwAheFUGKtn8CDzRe2MLiCG2pn-t2oXgUIKHfPVc4D2e1hqG6RHW61xSa4l5DEregQ9K4mAsoSBFG5dAm7xxdh2dQPIDOU79E4Rmp29uaiIjjNVroSd66gENUgI9A1ZEot8nComwiNGrCwplTbXAffc5XEWCi_txQ30CxAJzBHUhCF72LItRpNafroTfsKtZFgyHlke_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b85e9660.mp4?token=uvi_VFJ9_16zRWOYKp7Ir5lZ8F4mp9oVcXJz1R8NR8BGJgxTjgt1pqpKvjQWQkGtuf1oGYX_Yttib4cyEE8OCo5FV39piRq148S76qLxS3jYZ1FRUY2L9Fl6ucgulHU3X2QIuAh9NFqxzOwAheFUGKtn8CDzRe2MLiCG2pn-t2oXgUIKHfPVc4D2e1hqG6RHW61xSa4l5DEregQ9K4mAsoSBFG5dAm7xxdh2dQPIDOU79E4Rmp29uaiIjjNVroSd66gENUgI9A1ZEot8nComwiNGrCwplTbXAffc5XEWCi_txQ30CxAJzBHUhCF72LItRpNafroTfsKtZFgyHlke_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
واکنش‌ ستادکل‌ نیروهای مسلح به تهدیدهای ترامپ: آمادهٔ واردکردن ضربات شدید به آمریکا و رژیم صهیونیستی هستیم
🔹
تکرار ادعاها و تهدیدهای بی‌اساس، با توجه به فرسودگی ارتش آمریکا، نه نشانه قدرت، بلکه نشان از استیصال راهبردی آنان دارد.
🔹
لفاظی‌های رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/463899" target="_blank">📅 16:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463898">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc32ea4288.mp4?token=a7VAj-Ka2hlqLGmtmdvvIYnb1kWmfT5mDSvrcwvyP8U9fZKHsEZWDAO4p-uI9YxZRX9Td4uZbuK6LXn6ESKs7xi5W8o7I9ipRDUQ8XygU5QKlUHDmoyL_tCkMNoE1RtwJW8Ewo9sgsVMWYhYFoxYktsSdLgj4oUilRYtUkGSR5KEvznBxt1gYW9UmiOYK8X_SZ18ypIVLGw7nXaOW8mpv2lS8fVnQArtiF_QCwxJdNkUEIN5l7mC0soTKL8M1mlFIWdp2DLigrUmuDleBMUj3elkmt-weaucYGC2fzW9KLJMn4-_Nt9WrcOR81XJisIPFWrbfthcufsXu4kzi0hvLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc32ea4288.mp4?token=a7VAj-Ka2hlqLGmtmdvvIYnb1kWmfT5mDSvrcwvyP8U9fZKHsEZWDAO4p-uI9YxZRX9Td4uZbuK6LXn6ESKs7xi5W8o7I9ipRDUQ8XygU5QKlUHDmoyL_tCkMNoE1RtwJW8Ewo9sgsVMWYhYFoxYktsSdLgj4oUilRYtUkGSR5KEvznBxt1gYW9UmiOYK8X_SZ18ypIVLGw7nXaOW8mpv2lS8fVnQArtiF_QCwxJdNkUEIN5l7mC0soTKL8M1mlFIWdp2DLigrUmuDleBMUj3elkmt-weaucYGC2fzW9KLJMn4-_Nt9WrcOR81XJisIPFWrbfthcufsXu4kzi0hvLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
سخنگوی شهرداری تهران:  گفتند حال مادر ماکان چند روزه خوب نیست؛ پرسیدم علت کسالت ایشون چیه؟ گفتند: اول مهر.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/463898" target="_blank">📅 16:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463897">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">طالبان و پاکستان درگیر شدند
🔹
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔹
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/463897" target="_blank">📅 16:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463896">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e66e9f8a0.mp4?token=OulthoXzX08Ytoh4maa8oO3AyW3jgUZv6jkZJEcbOV58oYDe5vwMgrfA5z06ax6SPKQ-g6Yp9X2_O9PSLMbazqV_NutDW9a89greZ5goBJoaRkbD7YOMvbpyYgDNX06ToLzmIjWDPzaIBuuYZ2OvhnM1mbr3vSwrsH5eMgQrDYtpISoxIt2fz8x-qHd72qhn5SdBpHKhJN9HGxLUhKT2GzHKghei8q6z8aPJhB2_LfcX1ZzQ3gk46x4AsDi3OHryIQMQjCz7YFCyq4nNV-j6ngj-4cWEPb75DNcZuQz7t77PHYAwGcjaMgrE2KIY0pEw_dWoZPRlqWZfvNEPmghjQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e66e9f8a0.mp4?token=OulthoXzX08Ytoh4maa8oO3AyW3jgUZv6jkZJEcbOV58oYDe5vwMgrfA5z06ax6SPKQ-g6Yp9X2_O9PSLMbazqV_NutDW9a89greZ5goBJoaRkbD7YOMvbpyYgDNX06ToLzmIjWDPzaIBuuYZ2OvhnM1mbr3vSwrsH5eMgQrDYtpISoxIt2fz8x-qHd72qhn5SdBpHKhJN9HGxLUhKT2GzHKghei8q6z8aPJhB2_LfcX1ZzQ3gk46x4AsDi3OHryIQMQjCz7YFCyq4nNV-j6ngj-4cWEPb75DNcZuQz7t77PHYAwGcjaMgrE2KIY0pEw_dWoZPRlqWZfvNEPmghjQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جنگندهٔ انگلیسی در ولز
🔹
رسانه‌های انگلیسی گزارش کردند که یک جت آموزشی Hawk T2 امروز لحظاتی پس‌از پرواز در پایگاهی در ولز سقوط کرده و خدمهٔ آن ایجکت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/463896" target="_blank">📅 16:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463895">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyZ_48eVGvweV-_BnM-j8ICQzIHuWnvcezPRV-dW3icNPIPKmqTj4zEwg2N76AGc3hXl6tiI6lrDLlPUzOvpRubaZubIg8hfUjdI0AvPa3OH4ddpX10jGcgv2sV6MQatdWnck4GnVc9nKftNYb1E97mpbgYnctSN2SHI8PBfdNrozlUF9odlpBaP-yLHhgw4Ewk_WhHD8ixnAx2zhDE6-uZcywgNOuOQWvyb1dnGgXJC4iwjVkvRatKDWyCAhzu8VPce3TtC8EhB4ZayoAt9DrkqDc-SguImp8XmsyuZGJjDB_3rML8o1ovo6ZDQc8r5STa5uw-uAn6FI0oKlaFAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت دوباره ۳ رقمی شد
🔸
قیمت جهانی نفت برنت از ۱۰۰ دلار عبور کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/463895" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463894">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
پاکسازی خانۀ تیمی تروریست‌ها در جهادآباد سراوان
🔹
یک منبع آگاه از انجام عملیات ویژه برای پاکسازی خانۀ تیمی در منطقۀ جهادآباد سراوان خبر داد و گفت عملیات علیه تروریست‌ها همچنان ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/463894" target="_blank">📅 16:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463893">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3837d385.mp4?token=MUsxSM8G31RP24FUi_BbjTPHeWRxVE55z_18MzOVcMpRsAuoSdQ3WDFDteV-rnjUpEz1HF--M4kb9UXU5gbR5zE1ZwxgngHsJux51CYGVVxSoanR3O4QDw5GClgTMCcZuZ__YzsAnDNnhoSlcsa4S8blPb6pU5noVo2aWkhpOruRdHZ8l7y8wq1Su5xl1kbkbwF7cqwNb5hv6LpXxzwjFrBwCpzRv2jPKs-ZbsW0dr1HF48Ey0hBSyHGL38N2V_LblWm3lvZkcd_70qhw8UMVmVFA1bKDEPOX1ZOgr3qTJCN4QZv8W_jPdKL4lBvAyOkW9JmzjhlMar-zRU632JHaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3837d385.mp4?token=MUsxSM8G31RP24FUi_BbjTPHeWRxVE55z_18MzOVcMpRsAuoSdQ3WDFDteV-rnjUpEz1HF--M4kb9UXU5gbR5zE1ZwxgngHsJux51CYGVVxSoanR3O4QDw5GClgTMCcZuZ__YzsAnDNnhoSlcsa4S8blPb6pU5noVo2aWkhpOruRdHZ8l7y8wq1Su5xl1kbkbwF7cqwNb5hv6LpXxzwjFrBwCpzRv2jPKs-ZbsW0dr1HF48Ey0hBSyHGL38N2V_LblWm3lvZkcd_70qhw8UMVmVFA1bKDEPOX1ZOgr3qTJCN4QZv8W_jPdKL4lBvAyOkW9JmzjhlMar-zRU632JHaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلی‌استیشن ایران طلایی شد
🔹
تیم فوتبال الکترونیک ایران (حسن پاجانی و ابوالفضل آقایی‌نسب) در فینال بازی‌های آسیایی ناگویا موفق شد مالزی را ۴-۲ (در مجموع دو بازی) شکست دهد و مدال طلا را کسب کند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/463893" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZmY3WCwJMc4CioETzD-uZM8FuY7nR-u284k8UkjgGtyVh8k3hEUNrZJzoomj6B3HCn3pnEvo652LsITce1j8_jf_8_zzlIpSpnAYT84scje09yH4VOBPDjxH7mHqTOVYH0SMpVu2NC09HZI1I-6aiQeWBr7l3MNd6EkViMeuC6nZDu8bLYbXr1moVJigH58FM6XYOrploOIH24F4WbSmQTqAzr8bZlF7M9ByXLN7iRWZX2iwBiQDrXcGfnid0u6wu4mrRogZbrjgmuTwgeoaZ4yj6cepHQXk4wnHyq4DsbLrgv6P5iFJugmEdPZLNdjgjqggYt9elxfYujX89Ir-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pooRh_-B0JqFZ1f-rB2uR3xRA1yqD4m8g10NQNU6gAinGugIpjR8vkEHTdfzmV-gVfGrAdpDOoJyyyfYjIjHh8ysq4KIJ2rQIUX8errUOQ3LTT3ul2AWy2_dBaLEvRtRWBaIc_vZwMXaGvUFa7ko7i4Rfm_7oC8sLIIQZWev2skUuM6DMeyZX-aruWB88c0Q50J7pOCtK_rTO2eUGR-E1OGr07q_EtwclAWl8uLp13S6ec3-ZtEj7mSfDUdkG6UcGZ_IgXc22EmlPU5Pfp_6LMV04oyzIWzGxlZNhQF6F6bcYpD_tHr7EIm425lTeNu5J1VUY3QfUkVZcGiVICd0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfQ9N_jtPGX_CUsOATV0tx430nQwgkqu0PfZBpXvBRquMLMUXtGL010PoLOazGjJCIAbiarFW86r_OPTOZtXUtuG6iWpW2rw2uVELvf1BizwlJLLi6jxKd9RQVWlNIiC7dAIbDvOSX64vNl6GSMr5kmHXg91HphjFqObGQG6yrG4WmxclzZchPsoWB7e7PhuAGrlbACsWgllSi9NnnnqS6hXESHE2iVnQEBncoziWqWZtJ95RvfO0W4xW6fhiFwoNq85Al-50QbfRrbav-dxADOtFgfb-JbdIY__6FlQVO_pQs8VUtlZQmTRWmTyMBC9aGUKllLaKEcF9teC0uZDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQwdSzn7OS5zwB174uVYl397cW06ReWfvBTj5Iv9q-dP6-vHG4NL6aer7tjsLxFRZPrA-tFhPpudstt15W6WWUiDdSDd52faXGD4yFt-tfdHjb_1i3smt5gGIPGuPNs0z9PZaJzYdlGTh26LviejRUZjdnBF_gs0zjfGr-iorWCyxrE7HsdSZUGRi7-aPoR0a5KSUXaHHEbjo-b7EXLHtkSdWt2Ln02twecih9VoK6LF2F9_amCJkBI6EYQL4s13h3WILOvHX12dVsMrayK2jDUoBXkodm5nSWtC_sc-tjzG7wAVjPoeg-bUrZaAdTIFyU3Jyf-YSU_EbqI2fgWVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mo7sjCgNR963tsmsDt5hIDUHcPSQLfhMGZ3fE6O1P8XZPsQz9v_CC2Yr9wJqfmlarDshhLXp8ykTwgkiXjkfjAudMb0fuoB7ZJKu807heCfYmLtHHpKanYcDnSWCWcFDTnFpA0oQlhBCjfayN2hckzSkVy0f-Awqo-AIzL5WpMGrJsvwNFyLYo4I_q3_jFUxO7OclDKGuHhZyfQCXSi2mhJ19FgYSdAcfrfYO_yWEP-WNWpYdCC6EvuJQ7_q0gLCz4CXvh3rlUKQJxAdCu5yblBGM64-KM5B6-mRZsf8yQjGxSsbTPJfOvHenMS04M9Sawr5ls4UiLESgrGgbB4axQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEnouD1tAuRfadBLokPT1EpjlpL--l2m7Gdu4KhnrMCzOqOjvFxH1J4Mno_Dt3TMzRLathoW2TCfFzOGyTB5AFFD8x5FPGALCoVTeAOtnZWxnkTQ-Q28CXWX4ISsZ_5a3pDMs3Y8NCZwtJruBZAZL7ZJuWSHqakxKlN5eddaGzg4LS8P9IuQX3dHunyUMREF0ovd0Gqy6wiwDZxb3dQsvTbrBYbxXW7bnO_9TmIJwL2a-w6V7CMP5YO4fvtPvsvymDjMP0xv7G-eTN02tgbSpdxdGKHdOnLG7nlJmm0j5h8f2EsY44kSFttZHg7wbFlDtrgIC-XztMwaG9zxl7al0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1oo8gL99FDLrG34WWBx9wG35y6o1PfOLdHiBwR1d-J0ASL1v35LSvvXmwAhbHGhptfACoJuxycnieew2dydfYzdyC_ke4lvbsSOy83ziR6lv1CtBLVlQq4EOy4DpBXoP4Q2QOWu_3OWgV7okzCoHOyMm3XywpSUZkZYyCnzY8vo9DC2ekq8u8ixlU0RoAG8VKssPDa_l-rdJWKJ2NmZ9Apf8O8R4CwTJDC39gy_rexMLjbqBZFrtjeL4YXefYRUDNItZm1Kzdt8ZeZwZL-gP6fEFKniZ3DVBaYIt2ry6OIjCL-iua3jJdBHhF0F9cSXek1J0qTfIF6ReMNCbljVMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روزی برای «پرچم»
🗓
یکم مهرماه در تقویم ایران اسلامی روز پرچم نامگذاری شده است.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/463886" target="_blank">📅 16:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcaf48ab2b.mp4?token=Ybueu1F8pQygg-xxNwwYDxJe-oBoy5ki2xbPXu7Ef7no2YXEVVDkYIFPe-pUJUIXwePWe9SsGF5v13FziVJ4fcDxZnT2FR56p-5GxXE8T-7TGPSqJFyz7bQsxoJ79hZ4nRaBYUK1x3yp2myftDfrRb8vx2CSYvf8heBnJDhdWCdQD63m5Z3Dd5Zelp3S7rzObSgwxi73skYRnv0BZXvUmOFFJi8zO3yN1Y2MqIc5Bpc6ocC7vpQwGZphF-bfV05UF-s1qDk6P7qdHEnNQmdT8jnJsxUy2R-9zA7GtZ3P1FGUj_o3MQm5NA8baWVrpHIa99WZyWWioiRF22A6Ujd1fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcaf48ab2b.mp4?token=Ybueu1F8pQygg-xxNwwYDxJe-oBoy5ki2xbPXu7Ef7no2YXEVVDkYIFPe-pUJUIXwePWe9SsGF5v13FziVJ4fcDxZnT2FR56p-5GxXE8T-7TGPSqJFyz7bQsxoJ79hZ4nRaBYUK1x3yp2myftDfrRb8vx2CSYvf8heBnJDhdWCdQD63m5Z3Dd5Zelp3S7rzObSgwxi73skYRnv0BZXvUmOFFJi8zO3yN1Y2MqIc5Bpc6ocC7vpQwGZphF-bfV05UF-s1qDk6P7qdHEnNQmdT8jnJsxUy2R-9zA7GtZ3P1FGUj_o3MQm5NA8baWVrpHIa99WZyWWioiRF22A6Ujd1fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس مبارزه با قاچاق کالا و ارز: بسیاری‌از قاچاق‌های سوخت در کشور به‌صورت سازمان‌یافته انجام می‌شود.
🔹
در هر نقطه‌ای که سهمه‌بگیر عمده و جزء داریم، قاچاق سوخت هم داریم؛ در حوزه‌های حمل‌ونقل، صنعت کشاورزی و نیرو به‌وفور سوخت قاچاق می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/463884" target="_blank">📅 15:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8eyXxVVo1Ru8WQF9ig3jck-n3nANWGmdk5WCbVdG-iuPvCHI1Ao621BlOkcDs79yzBADFFMQDpDZ2QdWhoBgzNLcbAVcyxGumPz-2xSPfsGVgil8RzaXn6ePp_5a4k4VQ2RU_tXU1W0J1_A6l1J6PdCMLQ5B0jg0IDHlagqep_oB88yI5_52QgXDKsxvNforcjUhKXvkjZLQmSTOcPwqtdTdh3dRd6xvdgzXIs4UuwJoiUMR4ZO4t5l6biFi8eIMNhNLpVhjise8ZNpDg4-ytcfA-oU4tjjVD9sHdfx_JkGZ74YA5Vr7K8lLmhGGaiI0ykEtmN0az7lhks-HBBjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌دلیگانی: نشستن نمایندۀ ایران پای سخنرانی ترامپ مایۀ ننگ است
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: درحالی‌که عامل و دستوردهنده به شهادت امام شهید ما، کودکان میناب، کودکان لامرد و دیگر ایرانیان در آنجا سخنرانی می‌کند، واقعاً جای تأسف و ننگ است که افراد ایرانی…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/463883" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4171168b2a.mp4?token=QtKgHNoKM1jbTmYIy59u0X4w0YWm-hjtSz0jhZxnAQIzxZLU56kX8g87yKGo4vymGMgvTvwdrRVNu8pBPc_5O2HrEfV5o3kbbPUiyavU4GcrAu_t34ocOpnvocpO7shXQVgRooN1fTxyCEbYiuuuhdydVJZjMBqidmRPQmtcJpiaEzhfMcCLYuF6c2ITDOYQLr1sCLyctqJV8qKLIwPQx4VqP7Cm1028zA1WGf0Mmhnbwo4DxuptZXxUnPDLpwSpm2ifrM1cWloCni-p8ahv7CRDccsoPwcQeReSY2ngwbOUNeVDwNnPhDyIV_hKZOoq1y2UdyYxOp6mwvZ9H-vz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4171168b2a.mp4?token=QtKgHNoKM1jbTmYIy59u0X4w0YWm-hjtSz0jhZxnAQIzxZLU56kX8g87yKGo4vymGMgvTvwdrRVNu8pBPc_5O2HrEfV5o3kbbPUiyavU4GcrAu_t34ocOpnvocpO7shXQVgRooN1fTxyCEbYiuuuhdydVJZjMBqidmRPQmtcJpiaEzhfMcCLYuF6c2ITDOYQLr1sCLyctqJV8qKLIwPQx4VqP7Cm1028zA1WGf0Mmhnbwo4DxuptZXxUnPDLpwSpm2ifrM1cWloCni-p8ahv7CRDccsoPwcQeReSY2ngwbOUNeVDwNnPhDyIV_hKZOoq1y2UdyYxOp6mwvZ9H-vz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس مبارزه با قاچاق کالا و ارز: ۳۲ درصد از ۵۵ هزار پروندهٔ مبارزه با قاچاق مربوط به سوخت است.  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/463882" target="_blank">📅 15:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnKPABozTj-YI7Y0fMt1yrTYH6nJJ5gUnwUmacdOY8jW5jcUdWXAzLTJhtpBnnOHVvO3stD7IT1BJqHEFTx8MT_yxjllXxXNJ2ZRDaN2P-3P6TefPww4UpdNBGJjCQK2PepOznBto6Bm_HA3Jukdh26m39E83P8qtlmptG3_XipZxo0SW3SLBDnAFXu4YuZfMR2esuhM2J4Ag_-UC9FeB10fsvO7qk3UBPy4do4G6z6g96RiAXfe6Px952gFUduyGJjFy9BEuL7ZScFf_zQapXW0rMjZLJRssIRcT9zD7RxSs7YcqlGWeOsTq2PULOZI3OsX2BRL-hL4y-msKCso8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی سازمان غذاودارو: واکسن آنفلوآنزا هنوز توزیع نشده؛ هر واکسنی که به دست مردم رسیده قاچاق است و نباید استفاده شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/463881" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ee_v75A2WFvaVkmWbx_4dOjdNLh1PWT5cEFrR5P44ar6Qk_Ngg4rG-Fs8r6tXMSAhoIzv7O15WQV2xT7m21d-0LMerwZ-wYg2rZTcM2WFWxvk8QOHaEn1wGE04zjQ3Cn3tVZoDEURfIL5vLLOY9_AYMWhFzGSXmM_t2fecfNy-p0l3PcVp2DmZwtDCaKnzx6EFBGHDJa3xdtLWa2IJqfM1gDOTUKahncTA16WG1D66_hdB3UkZVDlzWBffuIqqPt7hGDhGG3UWa2KHuwRVTYc2yA4PXi2lzXPBX8IakiQ_YtiYEv3n0a9Ao_cGUoczn3zFejuhLD7zx1Ca791wHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دکتر «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های بانک شهر منصوب شد
⬅️
با صدور حکمی از سوی دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر؛ «علی محمد خانکی» به عنوان معاون مالی و امور شرکت های این بانک منصوب شد.
⬅️
به گزارش روابط عمومی بانک شهر ، دکتر «علی محمد خانکی» طی مراسمی با حضور دکتر سیدمحمدمهدی احمدی مدیرعامل بانک شهر و جمعی از اعضای هیات مدیره، معاونان و مدیران ارشد؛ به عنوان معاون مالی و امور شرکت های این بانک معرفی شد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/463880" target="_blank">📅 15:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک کارآفرین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd47d59cdc.mp4?token=hBePfQxrW67g3J8c0XumjmSaWncpuHG8CAUInhnEV1v5ks6U2OnAXDFk-__gqsNkdEsTreXJiIS9zm_5AZvUt9LeE5IL6RUL4WZmenx5PXKkd1LoE5TyDCK37nfCVYCov3-k6BpRzeaIgoZQHouUJYk9_4InujPgE3e_dvEq-WGgCDdMEBaok03RnZnyW3TVF2PIXKuvQ5sokQ6TgNpJ6HnacFHK80fSa3Y4WOxdvy-pW3_eDNQRHIJfS4Yh5Yc_Wdj9df_ifcClQVc6zoYWmrhO4TmNaYqQJ62jwAUxLe9uMeQ7KAaJ_NKVW-n_pe7ex1HsdDnoLo5FsAR0rk-LBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd47d59cdc.mp4?token=hBePfQxrW67g3J8c0XumjmSaWncpuHG8CAUInhnEV1v5ks6U2OnAXDFk-__gqsNkdEsTreXJiIS9zm_5AZvUt9LeE5IL6RUL4WZmenx5PXKkd1LoE5TyDCK37nfCVYCov3-k6BpRzeaIgoZQHouUJYk9_4InujPgE3e_dvEq-WGgCDdMEBaok03RnZnyW3TVF2PIXKuvQ5sokQ6TgNpJ6HnacFHK80fSa3Y4WOxdvy-pW3_eDNQRHIJfS4Yh5Yc_Wdj9df_ifcClQVc6zoYWmrhO4TmNaYqQJ62jwAUxLe9uMeQ7KAaJ_NKVW-n_pe7ex1HsdDnoLo5FsAR0rk-LBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بافتن پرچم، مثل ساختن آیندهست؛ تار به تار، نخ به نخ، باهم.
روز پرچم  گرامی باد.
🕊️
🇮🇷
☎️
۰۲۱۲۳۳۵۰
🌐
karafarinbank.ir
📱
@karafarin_bankف</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/463879" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/463878" target="_blank">📅 15:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
هدف‌قرارگرفتن یک کشتی در تنگۀ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد یک کشتی باری در داخل تنگۀ هرمز با یک پرتابۀ ناشناس هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/463877" target="_blank">📅 15:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-463876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f2453fbb.mp4?token=oqlmQSrEs2R_emxIQFNDRq3f2Lh710NaKchC-dQvconNkAUwFSmkYF4FXvMJNV1yDirYEJYBb4CQyTweOlxAhExcYsWEgIlBrH9B_p1g5DWWwlGT9NA3YHxwu6s4k5s6TjMaGVgePTem46r9uuxFdL_ZeG8FEfO-Ht0ponLp9-2ZP064MvRc-0FEZpljW2SKlp4PQaDbQeTBDYgeiJxYzYOP2oMstEDKmp2l9H15J3ouZXYoX05XWguVf4yjn9I-nL5RRKdKhtvbIXB29flffHRwZEe8vgyWpaWsj0lA-hKyCdReP4TscD5whKeYZle3cspaAzOA_YyOUvW83kpy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f2453fbb.mp4?token=oqlmQSrEs2R_emxIQFNDRq3f2Lh710NaKchC-dQvconNkAUwFSmkYF4FXvMJNV1yDirYEJYBb4CQyTweOlxAhExcYsWEgIlBrH9B_p1g5DWWwlGT9NA3YHxwu6s4k5s6TjMaGVgePTem46r9uuxFdL_ZeG8FEfO-Ht0ponLp9-2ZP064MvRc-0FEZpljW2SKlp4PQaDbQeTBDYgeiJxYzYOP2oMstEDKmp2l9H15J3ouZXYoX05XWguVf4yjn9I-nL5RRKdKhtvbIXB29flffHRwZEe8vgyWpaWsj0lA-hKyCdReP4TscD5whKeYZle3cspaAzOA_YyOUvW83kpy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس مبارزه با قاچاق کالا و ارز: ۳۲ درصد از ۵۵ هزار پروندهٔ مبارزه با قاچاق مربوط به سوخت است.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/463876" target="_blank">📅 15:30 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
